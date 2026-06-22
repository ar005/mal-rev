from __future__ import annotations
import logging
import math
import re
import string
from pathlib import Path
from typing import Any

from pipeline import Sample

log = logging.getLogger(__name__)

try:
    import pefile as _pefile
    _has_pefile = True
except ImportError:
    _has_pefile = False
    log.warning("pefile not installed; PE parsing skipped")

try:
    import yara as _yara
    _has_yara = True
except ImportError:
    _has_yara = False


# ── helpers ──────────────────────────────────────────────────────────────────

def _entropy(data: bytes) -> float:
    if not data:
        return 0.0
    counts = [0] * 256
    for b in data:
        counts[b] += 1
    n = len(data)
    return -sum((c / n) * math.log2(c / n) for c in counts if c)


def _extract_strings(data: bytes, min_len: int = 6) -> list[str]:
    printable = set(string.printable.encode())
    results: list[str] = []
    current: list[int] = []
    for b in data:
        if b in printable:
            current.append(b)
        else:
            if len(current) >= min_len:
                results.append(bytes(current).decode("ascii", errors="replace"))
            current = []
    if len(current) >= min_len:
        results.append(bytes(current).decode("ascii", errors="replace"))
    return results


def _load_yara_rules(rules_dir: Path) -> Any | None:
    if not _has_yara or not rules_dir.is_dir():
        return None
    yar_files = list(rules_dir.glob("*.yar")) + list(rules_dir.glob("*.yara"))
    if not yar_files:
        return None
    sources = {f.stem: str(f) for f in yar_files}
    try:
        return _yara.compile(filepaths=sources)
    except Exception as exc:
        log.warning("YARA compile error: %s", exc)
        return None


# ── PE analysis ───────────────────────────────────────────────────────────────

def _analyze_pe(path: Path, entropy_threshold: float) -> dict[str, Any]:
    result: dict[str, Any] = {}
    if not _has_pefile:
        return result
    try:
        pe = _pefile.PE(str(path), fast_load=False)
    except _pefile.PEFormatError as exc:
        log.warning("pefile: %s", exc)
        return result

    result["timestamp"] = pe.FILE_HEADER.TimeDateStamp
    result["machine"] = pe.FILE_HEADER.Machine
    result["characteristics"] = pe.FILE_HEADER.Characteristics

    # Sections
    sections = []
    for sec in pe.sections:
        name = sec.Name.rstrip(b"\x00").decode("ascii", errors="replace")
        raw = sec.get_data()
        ent = _entropy(raw)
        sections.append({
            "name": name,
            "virtual_address": hex(sec.VirtualAddress),
            "size": sec.SizeOfRawData,
            "entropy": round(ent, 3),
            "packed": ent > entropy_threshold,
        })
    result["sections"] = sections
    result["packed"] = any(s["packed"] for s in sections if s["name"] in (".text", "CODE"))

    # Imports
    imports: dict[str, list[str]] = {}
    if hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            dll = entry.dll.decode("ascii", errors="replace")
            funcs = []
            for imp in entry.imports:
                funcs.append(imp.name.decode("ascii", errors="replace") if imp.name else f"ord_{imp.ordinal}")
            imports[dll] = funcs
    result["imports"] = imports

    # Exports
    exports: list[str] = []
    if hasattr(pe, "DIRECTORY_ENTRY_EXPORT"):
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            exports.append(exp.name.decode("ascii", errors="replace") if exp.name else f"ord_{exp.ordinal}")
    result["exports"] = exports

    pe.close()
    return result


# ── main entry ────────────────────────────────────────────────────────────────

def run(sample: Sample, cfg: dict) -> Sample:
    analysis_cfg = cfg.get("analysis", {})
    min_len: int = analysis_cfg.get("min_string_len", 6)
    entropy_threshold: float = analysis_cfg.get("entropy_threshold", 7.0)
    rules_dir = Path(cfg.get("paths", {}).get("rules", "./rules"))

    data = sample.path.read_bytes()

    strings = _extract_strings(data, min_len)
    overall_entropy = _entropy(data)

    pe_info: dict[str, Any] = {}
    if "PE" in sample.file_type or sample.path.suffix.lower() in (".exe", ".dll", ".sys"):
        pe_info = _analyze_pe(sample.path, entropy_threshold)

    # YARA
    yara_matches: list[str] = []
    rules = _load_yara_rules(rules_dir)
    if rules:
        try:
            matches = rules.match(str(sample.path))
            yara_matches = [m.rule for m in matches]
        except Exception as exc:
            log.warning("YARA match error: %s", exc)

    sample.static = {
        "strings": strings[:500],  # cap for report size
        "string_count": len(strings),
        "entropy": round(overall_entropy, 3),
        "pe": pe_info,
        "yara_matches": yara_matches,
    }

    log.info(
        "Static analysis done: %d strings, entropy=%.2f, YARA hits=%d",
        len(strings),
        overall_entropy,
        len(yara_matches),
    )
    return sample
