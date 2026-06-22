"""check_reports.py — summarise VirusTotal verdicts across all fetched reports.

Reads reports/vt_index.json and each reports/<sha256>/vt.json, then
prints a breakdown of malware / benign / not-defined files.

Classification (based on last_analysis_stats):
  malware     — at least one engine flagged the file as malicious
  benign      — zero malicious detections AND zero suspicious detections
  not defined — file not found on VT, fetch failed, or stats missing

Usage:
  python check_reports.py
  python check_reports.py --reports /other/reports
  python check_reports.py --threshold 3   # require >= N malicious engines
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()

_INDEX_FILE = "vt_index.json"


def classify(vt_json: dict, threshold: int = 1) -> str:
    try:
        stats = vt_json["data"]["attributes"]["last_analysis_stats"]
        malicious  = stats.get("malicious",  0)
        suspicious = stats.get("suspicious", 0)
    except (KeyError, TypeError):
        return "not_defined"

    if malicious >= threshold:
        return "malware"
    if malicious == 0 and suspicious == 0:
        return "benign"
    return "not_defined"


def threat_label(vt_json: dict) -> str:
    try:
        return (
            vt_json["data"]["attributes"]
            ["popular_threat_classification"]
            ["suggested_threat_label"]
        )
    except (KeyError, TypeError):
        return ""


def check_reports(reports_dir: Path, threshold: int = 1) -> None:
    index_path = reports_dir / _INDEX_FILE
    if not index_path.exists():
        console.print(f"[red]Index not found:[/red] {index_path}")
        console.print("Run [bold]python vt.py[/bold] first to fetch reports.")
        return

    entries = json.loads(index_path.read_text())

    buckets: dict[str, list[dict]] = {"malware": [], "benign": [], "not_defined": []}

    for entry in entries:
        sha256 = entry.get("sha256", "")
        status = entry.get("status", "")

        if status != "ok":
            buckets["not_defined"].append({"sha256": sha256, "reason": status, "label": ""})
            continue

        vt_path = reports_dir / sha256 / "vt.json"
        if not vt_path.exists():
            buckets["not_defined"].append({"sha256": sha256, "reason": "missing_file", "label": ""})
            continue

        vt_json  = json.loads(vt_path.read_text())
        verdict  = classify(vt_json, threshold)
        label    = threat_label(vt_json)
        buckets[verdict].append({"sha256": sha256, "reason": status, "label": label})

    total = sum(len(v) for v in buckets.values())
    if total == 0:
        console.print("[dim]No entries in index.[/dim]")
        return

    # ── summary bar ──────────────────────────────────────────────────────────
    def pct(n: int) -> str:
        return f"{n / total * 100:.1f}%" if total else "—"

    console.print()
    console.print(f"[bold]VT Report Summary[/bold]  ({total} sample(s), threshold: ≥{threshold} engine(s))\n")

    summary = Table(box=None, show_header=False, padding=(0, 3))
    summary.add_row("[bold red]Malware[/bold red]",
                    str(len(buckets["malware"])),
                    f"[dim]{pct(len(buckets['malware']))}[/dim]")
    summary.add_row("[bold green]Benign[/bold green]",
                    str(len(buckets["benign"])),
                    f"[dim]{pct(len(buckets['benign']))}[/dim]")
    summary.add_row("[bold yellow]Not defined[/bold yellow]",
                    str(len(buckets["not_defined"])),
                    f"[dim]{pct(len(buckets['not_defined']))}[/dim]")
    console.print(summary)
    console.print()

    # ── malware detail ────────────────────────────────────────────────────────
    if buckets["malware"]:
        tbl = Table(
            show_header=True, header_style="bold dim",
            box=None, padding=(0, 2), title="[bold red]Malware[/bold red]",
            title_justify="left",
        )
        tbl.add_column("SHA256",          width=20)
        tbl.add_column("Threat label")

        for item in sorted(buckets["malware"], key=lambda x: x["label"]):
            tbl.add_row(
                item["sha256"][:20] + "…",
                item["label"] or "[dim]—[/dim]",
            )
        console.print(tbl)
        console.print()

    # ── not_defined detail ────────────────────────────────────────────────────
    if buckets["not_defined"]:
        tbl = Table(
            show_header=True, header_style="bold dim",
            box=None, padding=(0, 2), title="[bold yellow]Not defined[/bold yellow]",
            title_justify="left",
        )
        tbl.add_column("SHA256", width=20)
        tbl.add_column("Reason")

        for item in buckets["not_defined"]:
            tbl.add_row(
                item["sha256"][:20] + "…",
                f"[dim]{item['reason']}[/dim]",
            )
        console.print(tbl)
        console.print()


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="check_reports.py",
        description="Summarise VirusTotal verdicts from fetched reports.",
    )
    parser.add_argument("--reports",   default="reports",
                        help="Reports root directory (default: reports/)")
    parser.add_argument("--threshold", type=int, default=1,
                        help="Min malicious-engine count to call a file malware (default: 1)")
    args = parser.parse_args()
    check_reports(Path(args.reports), args.threshold)


if __name__ == "__main__":
    main()
