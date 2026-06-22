from __future__ import annotations
import logging
import re
from datetime import datetime, timezone
from pathlib import Path

from pipeline import Sample

log = logging.getLogger(__name__)

_SAFE_NAME = re.compile(r"[^\w.-]")  # keep word chars, dots, dashes


def _safe_filename(name: str) -> str:
    return _SAFE_NAME.sub("_", name)[:120]


def _render_report(sample: Sample, timestamp: str, code_files: list[str]) -> str:
    pe = sample.static.get("pe", {})
    sections = pe.get("sections", [])
    imports = pe.get("imports", {})
    exports = pe.get("exports", [])
    yara = sample.static.get("yara_matches", [])
    strings = sample.static.get("strings", [])

    lines = [
        "# Threat Analysis Report",
        "",
        f"**Generated:** {timestamp}",
        f"**Sample:** `{sample.path.name}`",
        "",
        "---",
        "",
        "## File Metadata",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| File name | `{sample.path.name}` |",
        f"| File type | {sample.file_type} |",
        f"| Size | {sample.size:,} bytes |",
        f"| MD5 | `{sample.md5}` |",
        f"| SHA1 | `{sample.sha1}` |",
        f"| SHA256 | `{sample.sha256}` |",
        f"| Overall entropy | {sample.static.get('entropy', 'N/A')} |",
        f"| Unpacked | {'✓ Yes (tool: ' + sample.unpacker + ')' if sample.unpacked else 'No'} |",
        "",
    ]

    # PE info
    if pe:
        lines += [
            "## PE Analysis",
            "",
            "| Field | Value |",
            "|-------|-------|",
            f"| Timestamp | {pe.get('timestamp', 'N/A')} |",
            f"| Machine | {pe.get('machine', 'N/A')} |",
            f"| Packed | {'⚠️ Yes' if pe.get('packed') else 'No'} |",
            "",
        ]
        if sections:
            lines += ["### Sections", "", "| Name | Size | Entropy | Packed |", "|------|------|---------|--------|"]
            for s in sections:
                packed_flag = "⚠️ Yes" if s.get("packed") else "No"
                lines.append(f"| `{s['name']}` | {s['size']:,} | {s['entropy']} | {packed_flag} |")
            lines.append("")

        if imports:
            lines += ["### Imports", ""]
            for dll, funcs in list(imports.items())[:20]:
                lines.append(f"**{dll}**: {', '.join(f'`{f}`' for f in funcs[:15])}")
            lines.append("")

        if exports:
            lines += ["### Exports", ""]
            lines.append(", ".join(f"`{e}`" for e in exports[:50]))
            lines.append("")

    # YARA
    if yara:
        lines += ["## YARA Matches", ""]
        for rule in yara:
            lines.append(f"- `{rule}`")
        lines.append("")

    # Strings
    lines += [
        "## Extracted Strings",
        "",
        f"Total strings found: **{sample.static.get('string_count', len(strings))}** (showing first 100)",
        "",
        "```",
    ]
    lines += strings[:100]
    lines += ["```", ""]

    # Disassembly / decompilation overview
    lines += [
        "## Disassembly Overview",
        "",
        f"Functions analyzed: **{len(sample.functions)}** | "
        f"Decompiled to C: **{len(sample.decompiled)}**",
        "",
    ]
    if sample.functions:
        lines += ["| Name | Offset | Size | Decompiled |", "|------|--------|------|------------|"]
        for f in sample.functions[:30]:
            fname = f.get("name", "?")
            has_c = "✓" if fname in sample.decompiled else "—"
            lines.append(
                f"| `{fname}` | `0x{(f.get('addr') or f.get('offset', 0)):x}` | {f.get('size', 0)} | {has_c} |"
            )
        lines.append("")

    # Link to code files
    if code_files:
        lines += ["### Decompiled Code Files", ""]
        for cf in sorted(code_files):
            lines.append(f"- [`code/{cf}`](code/{cf})")
        lines.append("")

    # LLM sections
    lines += [
        "## Behavioral Analysis",
        "",
        sample.behavior_summary or "_No behavioral analysis available._",
        "",
        "---",
        "",
        "## MITRE ATT&CK Mapping",
        "",
        sample.mitre_mapping or "_No MITRE mapping available._",
        "",
        "---",
        "",
        "## Indicators of Compromise",
        "",
        sample.iocs or "_No IOCs extracted._",
        "",
        "---",
        "",
        "## Malware Family Classification",
        "",
        sample.family or "_No classification available._",
        "",
    ]

    return "\n".join(lines)


def _update_index(reports_root: Path, sample: Sample, timestamp: str) -> None:
    index_path = reports_root / "index.md"
    report_link = f"[{sample.path.name}]({sample.sha256}/report.md)"
    family_short = (sample.family.splitlines()[0] if sample.family else "Unknown")[:80]
    new_row = f"| {timestamp} | {report_link} | `{sample.sha256[:16]}…` | {family_short} |"

    if not index_path.exists():
        header = (
            "# Analysis Index\n\n"
            "| Date | Sample | SHA256 | Family |\n"
            "|------|--------|--------|--------|\n"
        )
        index_path.write_text(header + new_row + "\n")
    else:
        index_path.write_text(index_path.read_text() + new_row + "\n")


def run(sample: Sample, cfg: dict) -> Sample:
    reports_root = Path(cfg.get("paths", {}).get("reports", "./reports"))

    # Per-sample directory: reports/<sha256>/
    sample_dir = reports_root / sample.sha256
    code_dir = sample_dir / "code"
    sample_dir.mkdir(parents=True, exist_ok=True)
    code_dir.mkdir(exist_ok=True)

    # Save each decompiled function as its own .c file
    saved_code_files: list[str] = []
    for func_name, c_code in sample.decompiled.items():
        filename = _safe_filename(func_name) + ".c"
        file_content = f"// Decompiled by r2ghidra\n// Function: {func_name}\n\n{c_code}\n"
        (code_dir / filename).write_text(file_content)
        saved_code_files.append(filename)

    if saved_code_files:
        log.info("Saved %d decompiled C files → %s/code/", len(saved_code_files), sample_dir)
    else:
        log.info("No decompiled code to save (install r2ghidra: r2pm -ci r2ghidra)")

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    report_md = _render_report(sample, timestamp, saved_code_files)

    report_path = sample_dir / "report.md"
    report_path.write_text(report_md)
    sample.report_path = report_path

    _update_index(reports_root, sample, timestamp)

    log.info("Report written: %s", report_path)
    return sample
