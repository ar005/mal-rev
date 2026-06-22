from __future__ import annotations
import json
import logging
from typing import Any

from pipeline import Sample

log = logging.getLogger(__name__)

try:
    import r2pipe as _r2pipe
    _has_r2 = True
except ImportError:
    _has_r2 = False
    log.warning("r2pipe not installed; disassembly skipped")


def _disasm_text(ops: list[dict]) -> str:
    lines = []
    for op in ops:
        offset = op.get("offset", 0)
        disasm = op.get("disasm", "")
        lines.append(f"  0x{offset:x}  {disasm}")
    return "\n".join(lines)


def run(sample: Sample, cfg: dict) -> Sample:
    if not _has_r2:
        log.warning("Skipping disassembly (r2pipe unavailable)")
        return sample

    analysis_cfg = cfg.get("analysis", {})
    max_functions: int = analysis_cfg.get("max_functions", 30)
    chunk_size: int = cfg.get("ollama", {}).get("chunk_size", 3000)

    try:
        r2 = _r2pipe.open(str(sample.path), flags=["-2"])  # -2 suppresses stderr
    except Exception as exc:
        log.warning("r2pipe failed to open sample: %s", exc)
        return sample

    try:
        log.info("Running radare2 analysis (aaa)…")
        r2.cmd("aaa")

        raw = r2.cmd("aflj")
        if not raw or raw.strip() == "null":
            log.warning("No functions found by radare2")
            return sample

        func_list: list[dict[str, Any]] = json.loads(raw)
    except Exception as exc:
        log.warning("radare2 analysis failed: %s", exc)
        r2.quit()
        return sample

    # Sort by size descending, take top N
    func_list.sort(key=lambda f: f.get("size", 0), reverse=True)
    top_funcs = func_list[:max_functions]
    sample.functions = top_funcs

    # Probe for r2ghidra: pdg? returns usage text when installed, empty when absent.
    # Use "Lc" (list core plugins) as a reliable secondary check.
    probe = r2.cmd("pdg?").strip()
    lc_out = r2.cmd("Lc")
    has_decompiler = bool(
        (probe and "pdg" in probe)
        or ("r2ghidra" in lc_out.lower() or "ghidra" in lc_out.lower())
    )
    if has_decompiler:
        log.info("r2ghidra detected — C decompilation enabled")
    else:
        log.warning(
            "r2ghidra not found — decompilation skipped. "
            "Install with: r2pm -ci r2ghidra"
        )

    # Disassemble (and optionally decompile) each function.
    # When r2ghidra is available the C pseudocode is used in the LLM context
    # (much more readable than raw assembly); raw asm is the fallback.
    # NOTE: pdg requires an explicit seek before calling — "pdg @ offset" is
    # unreliable; "s offset; pdg" matches the behaviour confirmed in manual tests.
    full_text_parts: list[str] = []
    decompiled: dict[str, str] = {}

    for func in top_funcs:
        name = func.get("name", "unknown")
        # r2 5.8+ uses "addr"; older versions used "offset" — support both
        offset = func.get("addr") or func.get("offset", 0)

        asm_block = ""
        try:
            raw_pdf = r2.cmd(f"pdfj @ 0x{offset:x}")
            if raw_pdf and raw_pdf.strip() not in ("null", ""):
                pdf = json.loads(raw_pdf)
                ops = pdf.get("ops", [])
                asm_block = _disasm_text(ops)
        except Exception as exc:
            log.debug("pdfj failed for %s: %s", name, exc)

        c_code = ""
        if has_decompiler:
            try:
                r2.cmd(f"s 0x{offset:x}")   # seek to function before decompiling
                raw_c = r2.cmd("pdg")
                if raw_c and raw_c.strip() and "Cannot find function" not in raw_c:
                    c_code = raw_c.strip()
                    decompiled[name] = c_code
            except Exception as exc:
                log.debug("pdg failed for %s: %s", name, exc)

        # Prefer C pseudocode in the LLM context; fall back to raw assembly
        if c_code:
            block = f"// {name} @ 0x{offset:x}\n{c_code}"
        elif asm_block:
            block = f"; {name} @ 0x{offset:x}\n{asm_block}"
        else:
            continue

        full_text_parts.append(block)

    r2.quit()

    sample.decompiled = decompiled

    # Split disassembly into LLM-sized chunks
    combined = "\n\n".join(full_text_parts)
    chunks: list[str] = []
    for i in range(0, len(combined), chunk_size):
        chunks.append(combined[i : i + chunk_size])

    sample.disasm_chunks = chunks
    log.info(
        "Disassembly done: %d functions, %d decompiled → %d chunks",
        len(top_funcs),
        len(decompiled),
        len(chunks),
    )
    return sample
