"""batch.py — mass RE pipeline batch runner with web monitor.

Usage:
  python batch.py run                            start or resume batch (dir from config.yaml)
  python batch.py run --dir /other/path          override the samples directory
  python batch.py pause                          signal pause after current sample
  python batch.py resume                         clear pause flag
  python batch.py status                         progress table in terminal
  python batch.py reset <sha256> [sha256 …]      re-queue specific sample(s)
  python batch.py monitor [--host 0.0.0.0] [--port 7000]   start web monitor

Workflow:
  # Terminal 1 — run the batch (samples dir read from config.yaml → batch.samples_dir)
  python batch.py run

  # Terminal 2 (or remote browser) — monitor + pause/resume/reset controls
  python batch.py monitor --host 0.0.0.0 --port 7000

State is written to batch_state.json after every stage.
Per-sample logs are saved to logs/<sha256>.log.
Ctrl-C during 'run' pauses gracefully after the current sample.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import logging
import signal
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml
from rich.console import Console
from rich.table import Table

console = Console()
log     = logging.getLogger("batch")

STATE_FILE = Path("batch_state.json")
LOGS_DIR   = Path("logs")
PAUSE_FILE = Path(".batch_pause")


# ── helpers ───────────────────────────────────────────────────────────────────

def now_utc() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def load_config(path: str = "config.yaml") -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def discover_samples(samples_dir: Path, recursive: bool = False) -> list[tuple[str, Path]]:
    """
    Return [(sha256, path)] for every file in samples_dir.
    SHA256 is extracted from the filename prefix when it looks like one
    (the format written by extract_pe), otherwise computed from file content.
    Hidden files and zero-byte files are skipped.
    When recursive=True, subdirectories are scanned too.
    """
    out:   list[tuple[str, Path]] = []
    skipped_dirs  = 0
    skipped_empty = 0
    skipped_hidden = 0

    glob = samples_dir.rglob("*") if recursive else samples_dir.iterdir()

    for f in sorted(glob):
        if f.is_dir():
            skipped_dirs += 1
            continue
        if f.name.startswith("."):
            skipped_hidden += 1
            continue
        if not f.is_file():
            continue
        if f.stat().st_size == 0:
            skipped_empty += 1
            continue

        prefix = f.name[:64].lower()
        if len(prefix) == 64 and all(c in "0123456789abcdef" for c in prefix):
            sha256 = prefix
        else:
            sha256 = sha256_of_file(f)
        out.append((sha256, f))

    log.debug(
        "discover: found=%d  dirs_skipped=%d  hidden=%d  empty=%d",
        len(out), skipped_dirs, skipped_hidden, skipped_empty,
    )
    return out, {"dirs": skipped_dirs, "hidden": skipped_hidden, "empty": skipped_empty}


def _fmt_dur(started: str | None, ended: str | None = None) -> str:
    if not started:
        return "—"
    s_dt = datetime.fromisoformat(started.replace("Z", "+00:00"))
    e_dt = (
        datetime.fromisoformat(ended.replace("Z", "+00:00"))
        if ended
        else datetime.now(timezone.utc)
    )
    secs = int((e_dt - s_dt).total_seconds())
    return f"{secs // 60}m {secs % 60:02d}s" if secs >= 60 else f"{secs}s"


# ── batch state ───────────────────────────────────────────────────────────────

class BatchState:
    """Thread-safe batch state backed by batch_state.json."""

    def __init__(self, path: Path = STATE_FILE) -> None:
        self.path  = path
        self._lock = threading.Lock()
        self.data  = self._load()

    def _load(self) -> dict:
        if self.path.exists():
            try:
                return json.loads(self.path.read_text())
            except Exception:
                pass
        return {
            "version":    1,
            "started_at": now_utc(),
            "updated_at": now_utc(),
            "paused":     False,
            "current":    None,
            "counts":     {},
            "samples":    {},
        }

    def _recount(self) -> None:
        s = self.data["samples"]
        self.data["counts"] = {
            "total":   len(s),
            "done":    sum(1 for e in s.values() if e["status"] == "done"),
            "failed":  sum(1 for e in s.values() if e["status"] == "failed"),
            "running": sum(1 for e in s.values() if e["status"] == "running"),
            "pending": sum(1 for e in s.values() if e["status"] == "pending"),
        }

    def _flush(self) -> None:
        """Atomic write via rename so the monitor never reads a partial file."""
        self.data["updated_at"] = now_utc()
        self._recount()
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.data, indent=2))
        tmp.replace(self.path)

    # ── public API ────────────────────────────────────────────────────────────

    def register(self, samples: list[tuple[str, Path]]) -> None:
        """Add new samples as pending; never overwrite existing entries."""
        with self._lock:
            for sha256, path in samples:
                if sha256 not in self.data["samples"]:
                    self.data["samples"][sha256] = {
                        "sha256":       sha256,
                        "filename":     path.name,
                        "path":         str(path),
                        "status":       "pending",
                        "stage":        None,
                        "started_at":   None,
                        "completed_at": None,
                        "error":        None,
                    }
            self._flush()

    def set_status(self, sha256: str, status: str,
                   stage: str | None = None, error: str | None = None) -> None:
        with self._lock:
            e = self.data["samples"][sha256]
            e["status"] = status
            if stage is not None:
                e["stage"] = stage
            if error is not None:
                e["error"] = str(error)
            if status == "running":
                e["started_at"] = now_utc()
                self.data["current"] = sha256
            elif status in ("done", "failed"):
                e["completed_at"] = now_utc()
                if self.data.get("current") == sha256:
                    self.data["current"] = None
            self._flush()

    def reset(self, sha256: str) -> bool:
        with self._lock:
            if sha256 not in self.data["samples"]:
                return False
            e = self.data["samples"][sha256]
            e.update(status="pending", stage=None,
                     started_at=None, completed_at=None, error=None)
            self._flush()
            return True

    def is_paused(self) -> bool:
        return bool(self.data.get("paused")) or PAUSE_FILE.exists()

    def set_paused(self, paused: bool) -> None:
        with self._lock:
            self.data["paused"] = paused
            self._flush()
        if paused:
            PAUSE_FILE.touch()
        elif PAUSE_FILE.exists():
            PAUSE_FILE.unlink(missing_ok=True)

    def pending(self) -> list[tuple[str, str]]:
        return [
            (sha256, e["path"])
            for sha256, e in self.data["samples"].items()
            if e["status"] == "pending"
        ]


# ── per-sample log capture ────────────────────────────────────────────────────

@contextlib.contextmanager
def capture_logs(sha256: str):
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOGS_DIR / f"{sha256}.log"
    handler  = logging.FileHandler(log_path, mode="a", encoding="utf-8")
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)-8s] %(name)s: %(message)s")
    )
    root = logging.getLogger()
    root.addHandler(handler)
    try:
        yield log_path
    finally:
        root.removeHandler(handler)
        handler.close()


# ── pipeline runner ───────────────────────────────────────────────────────────

def run_sample(sha256: str, path: Path, cfg: dict, state: BatchState) -> bool:
    """Run all five pipeline stages for one sample. Returns True on success."""
    from pipeline import ingestion, unpacking, static_analysis, disassembly, llm_analysis, reporting

    stages = [
        ("ingestion",   lambda s: ingestion.load_sample(path)),
        ("unpacking",   lambda s: unpacking.run(s, cfg)),
        ("static",      lambda s: static_analysis.run(s, cfg)),
        ("disassembly", lambda s: disassembly.run(s, cfg)),
        ("llm",         lambda s: llm_analysis.run(s, cfg)),
        ("reporting",   lambda s: reporting.run(s, cfg)),
    ]

    sample = None
    for stage_name, fn in stages:
        state.set_status(sha256, "running", stage=stage_name)
        log.info("=== stage: %s ===", stage_name)
        try:
            sample = fn(sample)
        except Exception as exc:
            log.error("stage '%s' failed: %s", stage_name, exc, exc_info=True)
            return False

    return True


# ── subcommands ───────────────────────────────────────────────────────────────

def _start_monitor_bg(host: str, port: int) -> None:
    """Launch the web monitor in a daemon thread so it dies when the runner exits."""
    import threading
    import uvicorn
    from fastapi import FastAPI
    from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse

    app = FastAPI(title="RE Batch Monitor", docs_url=None, redoc_url=None)

    def _load_state() -> dict:
        if STATE_FILE.exists():
            try:
                return json.loads(STATE_FILE.read_text())
            except Exception:
                pass
        return {"samples": {}, "counts": {}, "paused": False, "current": None, "samples_dir": ""}

    @app.get("/", response_class=HTMLResponse)
    async def index():
        return HTMLResponse(_MONITOR_HTML)

    @app.get("/api/state")
    async def api_state():
        return JSONResponse(_load_state())

    @app.get("/api/logs/{sha256}", response_class=PlainTextResponse)
    async def api_log(sha256: str):
        if not all(c in "0123456789abcdef" for c in sha256.lower()):
            return PlainTextResponse("invalid hash", status_code=400)
        p = LOGS_DIR / f"{sha256.lower()}.log"
        if not p.exists():
            return PlainTextResponse("(no log yet)")
        lines = p.read_text(errors="replace").splitlines()
        return PlainTextResponse("\n".join(lines[-300:]))

    @app.post("/api/pause")
    async def api_pause():
        BatchState(STATE_FILE).set_paused(True)
        return JSONResponse({"ok": True, "paused": True})

    @app.post("/api/resume")
    async def api_resume():
        BatchState(STATE_FILE).set_paused(False)
        return JSONResponse({"ok": True, "paused": False})

    @app.post("/api/reset/{sha256}")
    async def api_reset(sha256: str):
        if not all(c in "0123456789abcdef" for c in sha256.lower()):
            return JSONResponse({"ok": False, "error": "invalid hash"}, status_code=400)
        ok = BatchState(STATE_FILE).reset(sha256.lower())
        return JSONResponse({"ok": ok})

    t = threading.Thread(
        target=lambda: uvicorn.run(app, host=host, port=port, log_level="warning"),
        daemon=True,
        name="monitor",
    )
    t.start()
    console.print(f"[dim]Monitor → http://{host}:{port}[/dim]")


def cmd_run(args, cfg: dict) -> None:
    # Start monitor in background if requested
    if getattr(args, "monitor", False):
        _start_monitor_bg(args.host, args.port)

    # Priority: CLI --dir > config.yaml batch.samples_dir > "samples"
    dir_arg = getattr(args, "dir", None)
    if dir_arg:
        samples_dir = Path(dir_arg)
    else:
        samples_dir = Path(cfg.get("batch", {}).get("samples_dir", "samples"))

    samples_dir = samples_dir.resolve()
    if not samples_dir.is_dir():
        console.print(f"[red]Directory not found:[/red] {samples_dir}")
        console.print("[dim]Set batch.samples_dir in config.yaml or pass --dir[/dim]")
        sys.exit(1)

    state = BatchState(STATE_FILE)
    state.data["samples_dir"] = str(samples_dir)   # stored so monitor can display it
    state._flush()

    recursive = getattr(args, "recursive", False)
    console.print(f"[dim]Scanning {samples_dir}{'  (recursive)' if recursive else ''} …[/dim]")
    samples, skipped = discover_samples(samples_dir, recursive=recursive)

    if not samples:
        # Show diagnostic breakdown so the user knows why
        all_entries  = list(samples_dir.iterdir())
        files        = [e for e in all_entries if e.is_file()]
        dirs         = [e for e in all_entries if e.is_dir()]
        console.print(f"\n[yellow]No files found in:[/yellow] {samples_dir}")
        console.print(f"  directory entries : {len(all_entries)}")
        console.print(f"  files             : {len(files)}")
        console.print(f"  subdirectories    : {len(dirs)}")
        console.print(f"  skipped (hidden)  : {skipped['hidden']}")
        console.print(f"  skipped (empty)   : {skipped['empty']}")
        if dirs and not recursive:
            console.print(
                f"\n  [cyan]Hint:[/cyan] found {len(dirs)} subdirectory/ies — "
                f"try [bold]python batch.py run --recursive[/bold]"
            )
        if not all_entries:
            console.print("  [dim]The directory appears to be empty.[/dim]")
        return

    state.register(samples)

    if state.is_paused():
        console.print(
            "[yellow]Batch is paused.[/yellow]  "
            "Run [bold]python batch.py resume[/bold] first."
        )
        return

    pending = state.pending()
    if not pending:
        console.print(
            "[green]All samples already processed.[/green]  "
            "Use [bold]python batch.py reset <sha256>[/bold] to re-run specific ones."
        )
        return

    c = state.data["counts"]
    console.print(
        f"[bold]Batch start[/bold]  "
        f"total=[cyan]{c['total']}[/cyan]  "
        f"done=[green]{c['done']}[/green]  "
        f"pending=[dim]{c['pending']}[/dim]  "
        f"failed=[red]{c['failed']}[/red]"
    )
    console.print(f"[dim]State  → {STATE_FILE}[/dim]")
    console.print(f"[dim]Logs   → {LOGS_DIR}/[/dim]")
    console.print(f"[dim]Monitor→ python batch.py monitor[/dim]\n")

    # Ctrl-C → pause gracefully instead of crashing
    def _sigint(sig, frame):
        console.print("\n[yellow]Ctrl-C caught — pausing after current sample.[/yellow]")
        state.set_paused(True)

    signal.signal(signal.SIGINT, _sigint)

    done = failed = 0
    for sha256, path_str in pending:
        if state.is_paused():
            console.print("[yellow]⏸  Paused.[/yellow]")
            break

        path  = Path(path_str)
        fname = path.name[:55]
        console.print(f"[bold cyan]→[/bold cyan] {fname}  [dim]{sha256[:16]}…[/dim]")

        state.set_status(sha256, "running")
        with capture_logs(sha256):
            log.info("sample start  sha256=%s  path=%s", sha256, path)
            success = run_sample(sha256, path, cfg, state)
            log.info("sample %s  sha256=%s", "done" if success else "FAILED", sha256)

        if success:
            state.set_status(sha256, "done")
            done += 1
            console.print("  [green]✓ done[/green]")
        else:
            state.set_status(sha256, "failed")
            failed += 1
            console.print(
                f"  [red]✗ failed[/red]  "
                f"[dim]log: {LOGS_DIR}/{sha256[:16]}….log[/dim]"
            )

    if not state.is_paused():
        console.print(
            f"\n[bold green]Batch complete[/bold green]  "
            f"done={done}  failed={failed}"
        )
    else:
        console.print(
            f"\n[yellow]Paused after {done} sample(s).[/yellow]  "
            "Run [bold]python batch.py resume && python batch.py run[/bold] to continue."
        )


def cmd_status(args, cfg: dict) -> None:
    state   = BatchState(STATE_FILE)
    samples = state.data.get("samples", {})

    if not samples:
        console.print("[dim]No batch state found. Run [bold]python batch.py run[/bold] first.[/dim]")
        return

    c     = state.data.get("counts", {})
    total = c.get("total", 0)
    done  = c.get("done", 0)
    pct   = int(done / total * 100) if total else 0
    bw    = 40
    bar   = "█" * int(bw * pct / 100) + "░" * (bw - int(bw * pct / 100))

    console.print(f"\n[bold]Batch Status[/bold]  {pct}%  ({done}/{total})")
    console.print(f"[green]{bar}[/green]")
    console.print(
        f"  done=[green]{done}[/green]  "
        f"running=[yellow]{c.get('running', 0)}[/yellow]  "
        f"failed=[red]{c.get('failed', 0)}[/red]  "
        f"pending=[dim]{c.get('pending', 0)}[/dim]\n"
    )

    if state.is_paused():
        console.print("[yellow]⏸  Batch is currently paused.[/yellow]\n")

    ORDER = {"running": 0, "failed": 1, "pending": 2, "done": 3}
    STYLE = {"done": "green", "failed": "red", "running": "yellow", "pending": "dim"}

    tbl = Table(show_header=True, header_style="bold dim", box=None, padding=(0, 2))
    tbl.add_column("SHA256",   width=22)
    tbl.add_column("Filename", width=36)
    tbl.add_column("Status",   width=10)
    tbl.add_column("Stage",    width=14)
    tbl.add_column("Duration", width=10)

    for sha256, e in sorted(samples.items(),
                             key=lambda x: ORDER.get(x[1]["status"], 9)):
        s     = e["status"]
        style = STYLE.get(s, "")
        tbl.add_row(
            sha256[:20] + "…",
            (e.get("filename") or "")[:35],
            f"[{style}]{s}[/{style}]",
            e.get("stage") or "—",
            _fmt_dur(e.get("started_at"), e.get("completed_at")),
        )

    console.print(tbl)


def cmd_pause(args, cfg: dict) -> None:
    BatchState(STATE_FILE).set_paused(True)
    console.print("[yellow]Pause flag set — runner will stop after current sample.[/yellow]")


def cmd_resume(args, cfg: dict) -> None:
    BatchState(STATE_FILE).set_paused(False)
    console.print(
        "[green]Resumed.[/green]  "
        "Run [bold]python batch.py run[/bold] to continue."
    )


def cmd_reset(args, cfg: dict) -> None:
    state = BatchState(STATE_FILE)
    for raw in args.hashes:
        sha256 = raw.lower().strip()
        if state.reset(sha256):
            console.print(f"[green]Reset →[/green] {sha256[:20]}…")
        else:
            console.print(f"[yellow]Not found:[/yellow] {sha256[:20]}…")


def cmd_monitor(args, cfg: dict) -> None:
    import uvicorn
    from fastapi import FastAPI
    from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse

    app = FastAPI(title="RE Batch Monitor", docs_url=None, redoc_url=None)

    def _load_state() -> dict:
        if STATE_FILE.exists():
            try:
                return json.loads(STATE_FILE.read_text())
            except Exception:
                pass
        return {"samples": {}, "counts": {}, "paused": False, "current": None, "samples_dir": ""}

    @app.get("/", response_class=HTMLResponse)
    async def index():
        return HTMLResponse(_MONITOR_HTML)

    @app.get("/api/state")
    async def api_state():
        return JSONResponse(_load_state())

    @app.get("/api/logs/{sha256}", response_class=PlainTextResponse)
    async def api_log(sha256: str):
        if not all(c in "0123456789abcdef" for c in sha256.lower()):
            return PlainTextResponse("invalid hash", status_code=400)
        p = LOGS_DIR / f"{sha256.lower()}.log"
        if not p.exists():
            return PlainTextResponse("(no log yet)")
        lines = p.read_text(errors="replace").splitlines()
        return PlainTextResponse("\n".join(lines[-300:]))

    # ── control endpoints ─────────────────────────────────────────────────────

    @app.post("/api/pause")
    async def api_pause():
        state = BatchState(STATE_FILE)
        state.set_paused(True)
        return JSONResponse({"ok": True, "paused": True})

    @app.post("/api/resume")
    async def api_resume():
        state = BatchState(STATE_FILE)
        state.set_paused(False)
        return JSONResponse({"ok": True, "paused": False})

    @app.post("/api/reset/{sha256}")
    async def api_reset(sha256: str):
        if not all(c in "0123456789abcdef" for c in sha256.lower()):
            return JSONResponse({"ok": False, "error": "invalid hash"}, status_code=400)
        state = BatchState(STATE_FILE)
        ok = state.reset(sha256.lower())
        return JSONResponse({"ok": ok})

    console.print(
        f"[bold cyan]Monitor[/bold cyan]  →  "
        f"http://{args.host}:{args.port}"
    )
    uvicorn.run(app, host=args.host, port=args.port, log_level="warning")


# ── monitor HTML (self-contained, no external deps) ───────────────────────────

_MONITOR_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>RE Batch Monitor</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{background:#0d1117;color:#c9d1d9;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px;padding:24px;line-height:1.6}
h1{color:#58a6ff;font-size:16px;margin-bottom:4px;display:flex;align-items:center;gap:10px}
.dot{width:8px;height:8px;border-radius:50%;background:#3fb950;flex-shrink:0;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.2}}
.dir-row{color:#8b949e;font-size:11px;margin-bottom:18px;display:flex;align-items:center;gap:6px}
.dir-path{color:#c9d1d9;background:#161b22;border:1px solid #21262d;padding:2px 8px;border-radius:4px;font-size:11px}
.ts{color:#8b949e;font-size:11px;margin-left:auto}
.stats{display:flex;gap:10px;margin-bottom:16px;flex-wrap:wrap;align-items:flex-start}
.stat{background:#161b22;padding:10px 16px;border-radius:8px;min-width:90px;border:1px solid #21262d}
.stat .v{font-size:22px;font-weight:700;line-height:1.2}
.stat .l{color:#8b949e;font-size:10px;text-transform:uppercase;letter-spacing:.7px;margin-top:2px}
.c-total{color:#c9d1d9}.c-done{color:#3fb950}.c-running{color:#d29922}
.c-failed{color:#f85149}.c-pending{color:#8b949e}.c-pct{color:#58a6ff}
.controls{display:flex;gap:8px;margin-left:auto;align-items:center}
btn,button{background:#21262d;color:#c9d1d9;border:1px solid #30363d;padding:7px 14px;border-radius:6px;font-family:inherit;font-size:12px;cursor:pointer;transition:background .15s}
button:hover{background:#30363d}
button.pause-btn{border-color:#d29922;color:#d29922}
button.pause-btn:hover{background:#271d00}
button.resume-btn{border-color:#3fb950;color:#3fb950}
button.resume-btn:hover{background:#0d2e18}
button:disabled{opacity:.4;cursor:default}
.prog-wrap{background:#21262d;border-radius:4px;height:5px;margin-bottom:16px;overflow:hidden}
.prog-bar{background:#238636;height:100%;border-radius:4px;transition:width .5s}
.banner{background:#271d00;border:1px solid #d29922;color:#d29922;padding:8px 14px;border-radius:6px;margin-bottom:14px;font-size:12px;display:none}
.current{background:#161b22;border:1px solid #21262d;padding:10px 14px;border-radius:6px;margin-bottom:18px}
.current .lbl{color:#8b949e;font-size:10px;text-transform:uppercase;letter-spacing:.7px;margin-bottom:4px}
.current .val{color:#d29922}
.sec{color:#8b949e;font-size:10px;text-transform:uppercase;letter-spacing:.7px;margin-bottom:8px}
table{width:100%;border-collapse:collapse;margin-bottom:18px;font-size:12px}
th{background:#161b22;padding:7px 10px;text-align:left;color:#8b949e;font-weight:normal;border-bottom:1px solid #21262d;position:sticky;top:0;z-index:1}
td{padding:6px 10px;border-bottom:1px solid #161b22}
tr.row{cursor:pointer}
tr.row:hover td{background:#161b22}
tr.row.sel td{background:#1c2333;border-bottom-color:#21262d}
.badge{display:inline-block;padding:1px 8px;border-radius:10px;font-size:11px;font-weight:500}
.done{background:#0d2e18;color:#3fb950}.failed{background:#2e0d0d;color:#f85149}
.running{background:#2e2500;color:#d29922}.pending{background:#21262d;color:#8b949e}
.reset-btn{background:none;border:1px solid #30363d;color:#8b949e;padding:1px 7px;border-radius:4px;font-size:10px;cursor:pointer;font-family:inherit}
.reset-btn:hover{background:#161b22;color:#c9d1d9;border-color:#8b949e}
.log-card{background:#010409;border:1px solid #21262d;border-radius:6px;overflow:hidden}
.log-hdr{background:#161b22;padding:7px 12px;font-size:11px;color:#8b949e;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #21262d}
.log-body{padding:12px;height:240px;overflow-y:auto;font-size:11px;line-height:1.6;white-space:pre-wrap;color:#8b949e;word-break:break-all}
.toast{position:fixed;bottom:24px;right:24px;background:#161b22;border:1px solid #30363d;color:#c9d1d9;padding:10px 16px;border-radius:6px;font-size:12px;opacity:0;transition:opacity .3s;pointer-events:none}
.toast.show{opacity:1}
</style>
</head>
<body>

<h1><span class="dot"></span>RE Batch Monitor</h1>

<div class="dir-row">
  <span>Samples dir</span>
  <span class="dir-path" id="dir-path">—</span>
  <span class="ts" id="ts"></span>
</div>

<div class="stats">
  <div class="stat"><div class="v c-total"   id="s-total">—</div><div class="l">Total</div></div>
  <div class="stat"><div class="v c-done"    id="s-done">—</div><div class="l">Done</div></div>
  <div class="stat"><div class="v c-running" id="s-running">—</div><div class="l">Running</div></div>
  <div class="stat"><div class="v c-failed"  id="s-failed">—</div><div class="l">Failed</div></div>
  <div class="stat"><div class="v c-pending" id="s-pending">—</div><div class="l">Pending</div></div>
  <div class="stat"><div class="v c-pct"     id="s-pct">—</div><div class="l">Complete</div></div>
  <div class="controls">
    <button class="pause-btn"  id="btn-pause"  onclick="ctrlPause()">⏸ Pause</button>
    <button class="resume-btn" id="btn-resume" onclick="ctrlResume()" style="display:none">▶ Resume</button>
  </div>
</div>

<div class="prog-wrap"><div class="prog-bar" id="prog" style="width:0%"></div></div>

<div class="banner" id="banner">⏸  Batch is paused — runner will stop after the current sample</div>

<div class="current">
  <div class="lbl">Currently processing</div>
  <div class="val" id="cur">—</div>
</div>

<div class="sec">Samples</div>
<table>
  <thead><tr>
    <th>SHA256</th><th>Filename</th><th>Status</th><th>Stage</th><th>Duration</th><th></th>
  </tr></thead>
  <tbody id="tbody"></tbody>
</table>

<div class="sec">Log</div>
<div class="log-card">
  <div class="log-hdr">
    <span id="log-lbl">click a row to view its log</span>
    <span id="log-cnt" style="color:#58a6ff"></span>
  </div>
  <div class="log-body" id="log-body">—</div>
</div>

<div class="toast" id="toast"></div>

<script>
'use strict';
let sel = null;
const ORDER = {running:0,failed:1,pending:2,done:3};

function dur(e) {
  if (!e.started_at) return '—';
  const s = Math.round(((e.completed_at ? new Date(e.completed_at) : new Date()) - new Date(e.started_at)) / 1000);
  return s < 60 ? s + 's' : Math.floor(s/60) + 'm ' + String(s%60).padStart(2,'0') + 's';
}

function toast(msg, ok=true) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.style.borderColor = ok ? '#3fb950' : '#f85149';
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2500);
}

async function ctrlPause() {
  try {
    await fetch('/api/pause', {method:'POST'});
    toast('Pause signal sent — will stop after current sample');
    refresh();
  } catch { toast('Request failed', false); }
}

async function ctrlResume() {
  try {
    await fetch('/api/resume', {method:'POST'});
    toast('Resumed — restart the runner if it stopped');
    refresh();
  } catch { toast('Request failed', false); }
}

async function ctrlReset(sha, ev) {
  ev.stopPropagation();
  try {
    const r = await fetch('/api/reset/' + sha, {method:'POST'}).then(r => r.json());
    toast(r.ok ? 'Reset to pending' : 'Reset failed', r.ok);
    refresh();
  } catch { toast('Request failed', false); }
}

async function refresh() {
  let state;
  try { state = await fetch('/api/state').then(r => r.json()); }
  catch { return; }

  const c = state.counts || {};
  const total = c.total || 0, done = c.done || 0;
  const pct = total ? Math.round(done / total * 100) : 0;
  const paused = !!state.paused;

  document.getElementById('dir-path').textContent  = state.samples_dir || '—';
  document.getElementById('s-total').textContent   = total;
  document.getElementById('s-done').textContent    = c.done    || 0;
  document.getElementById('s-running').textContent = c.running || 0;
  document.getElementById('s-failed').textContent  = c.failed  || 0;
  document.getElementById('s-pending').textContent = c.pending || 0;
  document.getElementById('s-pct').textContent     = pct + '%';
  document.getElementById('prog').style.width      = pct + '%';
  document.getElementById('banner').style.display  = paused ? 'block' : 'none';
  document.getElementById('ts').textContent        = 'updated ' + new Date().toLocaleTimeString();

  document.getElementById('btn-pause').style.display  = paused ? 'none'  : '';
  document.getElementById('btn-resume').style.display = paused ? ''      : 'none';

  const curSha = state.current;
  if (curSha) {
    const e = (state.samples || {})[curSha] || {};
    document.getElementById('cur').textContent =
      (e.filename || curSha.slice(0,20)+'…') + '  →  ' + (e.stage || '…');
    if (!sel) sel = curSha;
  } else {
    document.getElementById('cur').textContent =
      (done === total && total > 0) ? 'Batch complete ✓' : '—';
  }

  const rows = Object.entries(state.samples || {})
    .sort((a, b) => (ORDER[a[1].status] ?? 9) - (ORDER[b[1].status] ?? 9));

  document.getElementById('tbody').innerHTML = rows.map(([sha, e]) => {
    const canReset = e.status === 'failed' || e.status === 'done';
    const resetBtn = canReset
      ? `<button class="reset-btn" onclick="ctrlReset('${sha}',event)">reset</button>`
      : '';
    return `
    <tr class="row${sha===sel?' sel':''}" data-sha="${sha}" onclick="pickRow('${sha}')">
      <td>${sha.slice(0,20)}…</td>
      <td>${(e.filename||'').slice(0,36)}</td>
      <td><span class="badge ${e.status}">${e.status}</span></td>
      <td>${e.stage || '—'}</td>
      <td>${dur(e)}</td>
      <td>${resetBtn}</td>
    </tr>`;
  }).join('');

  if (sel) pollLog(sel);
}

function pickRow(sha) {
  sel = sha;
  document.querySelectorAll('#tbody tr').forEach(r =>
    r.classList.toggle('sel', r.dataset.sha === sha));
  pollLog(sha);
}

async function pollLog(sha) {
  try {
    const text = await fetch('/api/logs/' + sha).then(r => r.text());
    const lines = text.split('\n');
    document.getElementById('log-lbl').textContent = sha.slice(0,20) + '…';
    document.getElementById('log-cnt').textContent = lines.length + ' lines';
    const box = document.getElementById('log-body');
    const atBottom = box.scrollHeight - box.scrollTop - box.clientHeight < 40;
    box.textContent = text;
    if (atBottom) box.scrollTop = box.scrollHeight;
  } catch {}
}

setInterval(refresh, 3000);
refresh();
</script>
</body>
</html>"""


# ── main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stderr,
    )

    parser = argparse.ArgumentParser(
        prog="batch.py",
        description="Mass RE pipeline batch runner with web monitor.",
    )
    parser.add_argument("--config", default="config.yaml", help="Config file (default: config.yaml)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_run = sub.add_parser("run", help="Start or resume batch analysis")
    p_run.add_argument("--dir", default=None,
                        help="Samples directory (default: batch.samples_dir in config.yaml)")
    p_run.add_argument("--recursive", "-r", action="store_true",
                        help="Scan subdirectories recursively")
    p_run.add_argument("--monitor", "-m", action="store_true",
                        help="Also start the web monitor in the background")
    p_run.add_argument("--host", default="0.0.0.0",
                        help="Monitor bind host (default: 0.0.0.0)")
    p_run.add_argument("--port", default=7000, type=int,
                        help="Monitor port (default: 7000)")

    sub.add_parser("pause",  help="Pause after current sample")
    sub.add_parser("resume", help="Clear pause flag and continue")
    sub.add_parser("status", help="Print progress table to terminal")

    p_reset = sub.add_parser("reset", help="Re-queue sample(s) back to pending")
    p_reset.add_argument("hashes", nargs="+", help="SHA256 hash(es) to reset")

    p_mon = sub.add_parser("monitor", help="Start read-only web monitoring server")
    p_mon.add_argument("--host", default="0.0.0.0",    help="Bind host (default: 0.0.0.0)")
    p_mon.add_argument("--port", default=7000, type=int, help="Port (default: 7000)")

    args = parser.parse_args()
    cfg  = load_config(args.config)

    dispatch = {
        "run":     cmd_run,
        "status":  cmd_status,
        "pause":   cmd_pause,
        "resume":  cmd_resume,
        "reset":   cmd_reset,
        "monitor": cmd_monitor,
    }
    dispatch[args.cmd](args, cfg)


if __name__ == "__main__":
    main()
