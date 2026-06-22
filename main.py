#!/usr/bin/env python3
"""
Malware RE Pipeline — CLI entry point.

Usage:
  python main.py analyze <path>        Analyze a single sample
  python main.py watch   <dir>         Watch a directory for new samples
  python main.py serve   [--port N]    Launch the web report browser
"""
from __future__ import annotations
import argparse
import logging
import sys
import time
from pathlib import Path

import yaml
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn

console = Console()


# ── config ────────────────────────────────────────────────────────────────────

def load_config(path: str = "config.yaml") -> dict:
    with open(path) as fh:
        return yaml.safe_load(fh)


# ── pipeline orchestrator ─────────────────────────────────────────────────────

def run_pipeline(file_path: Path, cfg: dict) -> None:
    from pipeline import ingestion, unpacking, static_analysis, disassembly, llm_analysis, reporting

    stages = [
        ("Ingesting sample",       lambda s: ingestion.load_sample(file_path)),
        ("Unpacking",              lambda s: unpacking.run(s, cfg)),
        ("Static analysis",        lambda s: static_analysis.run(s, cfg)),
        ("Disassembly",            lambda s: disassembly.run(s, cfg)),
        ("LLM analysis",           lambda s: llm_analysis.run(s, cfg)),
        ("Generating report",      lambda s: reporting.run(s, cfg)),
    ]

    sample = None
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.description}"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        for description, fn in stages:
            task = progress.add_task(description, total=None)
            sample = fn(sample)
            progress.update(task, completed=True)

    console.print(f"\n[bold green]✓ Report saved:[/bold green] {sample.report_path}")
    console.print(f"  SHA256: [dim]{sample.sha256}[/dim]")
    console.print(f"  Family: [yellow]{sample.family.splitlines()[0] if sample.family else 'Unknown'}[/yellow]")


# ── watch mode ────────────────────────────────────────────────────────────────

def watch_directory(watch_dir: Path, cfg: dict) -> None:
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        console.print("[red]watchdog not installed. Run: pip install watchdog[/red]")
        sys.exit(1)

    seen: set[str] = set()

    class Handler(FileSystemEventHandler):
        def on_created(self, event):
            if event.is_directory:
                return
            path = Path(event.src_path)
            if str(path) in seen:
                return
            seen.add(str(path))
            console.print(f"\n[bold]New file detected:[/bold] {path.name}")
            try:
                run_pipeline(path, cfg)
            except Exception as exc:
                console.print(f"[red]Pipeline error:[/red] {exc}")

    observer = Observer()
    observer.schedule(Handler(), str(watch_dir), recursive=False)
    observer.start()
    console.print(f"[bold cyan]Watching[/bold cyan] {watch_dir}  (Ctrl+C to stop)")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[RichHandler(console=console, show_path=False, markup=True)],
    )

    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Malware RE Pipeline — Ollama / Claude / Claude-Ollama",
    )
    parser.add_argument("--config", default="config.yaml", help="Path to config.yaml")

    sub = parser.add_subparsers(dest="command", required=True)

    p_analyze = sub.add_parser("analyze", help="Analyze a single file")
    p_analyze.add_argument("path", type=Path, help="Path to malware sample")

    p_watch = sub.add_parser("watch", help="Watch a directory for new samples")
    p_watch.add_argument("dir", type=Path, help="Directory to watch")

    p_serve = sub.add_parser("serve", help="Launch the web report browser")
    p_serve.add_argument("--port", type=int, default=8080)
    p_serve.add_argument("--host", default="127.0.0.1")

    args = parser.parse_args()
    cfg = load_config(args.config)

    if args.command == "analyze":
        if not args.path.is_file():
            console.print(f"[red]File not found:[/red] {args.path}")
            sys.exit(1)
        run_pipeline(args.path, cfg)

    elif args.command == "watch":
        if not args.dir.is_dir():
            console.print(f"[red]Directory not found:[/red] {args.dir}")
            sys.exit(1)
        watch_directory(args.dir, cfg)

    elif args.command == "serve":
        import uvicorn
        from web.app import build_app
        app = build_app(cfg)
        console.print(f"[bold cyan]Starting web UI[/bold cyan] → http://{args.host}:{args.port}")
        uvicorn.run(app, host=args.host, port=args.port, log_level="warning")


if __name__ == "__main__":
    main()
