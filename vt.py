"""vt.py — VirusTotal enrichment for malware samples.

Reads VT_KEY_1 … VT_KEY_N from .env, rotates keys to honour the free-tier
rate limit (4 req/min per key), and writes raw API responses to
reports/<sha256>/vt.json.  Already-fetched hashes are tracked in
reports/vt_index.json and are never re-requested.

Usage:
  python vt.py                         # scan samples/ dir, fetch all unknown
  python vt.py --dir /path/to/samples  # custom samples directory
  python vt.py <sha256> [sha256 …]    # fetch specific hashes by SHA256
  python vt.py --list                  # show the fetched index
  python vt.py --force <sha256> …     # re-fetch even if already in index
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path

import requests
from rich.console import Console
from rich.table import Table
from rich.progress import (
    Progress, BarColumn, TextColumn, SpinnerColumn,
    MofNCompleteColumn, TimeElapsedColumn,
)

# ── constants ─────────────────────────────────────────────────────────────────

_VT_FILE_URL  = "https://www.virustotal.com/api/v3/files/{sha256}"
_INDEX_FILE   = "vt_index.json"       # inside reports_dir
_DEFAULT_RATE = 15.0                  # seconds between requests on the same key
_MAX_RETRIES  = 3                     # retries on 429 before giving up a hash

console = Console()


# ── .env loader ───────────────────────────────────────────────────────────────

def load_dotenv(path: str = ".env") -> dict[str, str]:
    """Minimal .env parser — no external dependency required."""
    env: dict[str, str] = {}
    try:
        for line in Path(path).read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            env[key.strip()] = val.strip().strip("'\"")
    except FileNotFoundError:
        pass
    return env


def load_vt_keys(env: dict[str, str]) -> list[str]:
    """Collect VT_KEY_1, VT_KEY_2 … (any N) from env, ignoring blanks."""
    keys: list[str] = []
    i = 1
    while True:
        key = env.get(f"VT_KEY_{i}", "").strip()
        if not key:
            break
        keys.append(key)
        i += 1
    return keys


def vt_rate_limit(env: dict[str, str]) -> float:
    """VT_RATE_LIMIT from env (seconds between requests per key)."""
    try:
        return float(env.get("VT_RATE_LIMIT", _DEFAULT_RATE))
    except ValueError:
        return _DEFAULT_RATE


# ── key rotator ───────────────────────────────────────────────────────────────

class KeyRotator:
    """
    Thread-safe pool that hands out the next available key.

    Each key has an earliest-next-use timestamp.  acquire() blocks until
    one key is free, then immediately reserves it for rate_limit seconds.
    A 429 response should call penalize(idx) to delay that key further.
    """

    def __init__(self, keys: list[str], rate_limit: float = _DEFAULT_RATE) -> None:
        if not keys:
            raise ValueError("No VT API keys found in .env")
        self.keys        = keys
        self.rate_limit  = rate_limit
        self._next_ok    = [0.0] * len(keys)   # monotonic timestamps
        self._lock       = threading.Lock()

    def acquire(self) -> tuple[str, int]:
        """Block until a key is available; return (api_key, index)."""
        while True:
            with self._lock:
                now = time.monotonic()
                idx  = min(range(len(self.keys)), key=lambda i: self._next_ok[i])
                wait = self._next_ok[idx] - now
                if wait <= 0:
                    self._next_ok[idx] = now + self.rate_limit
                    return self.keys[idx], idx
            # sleep in small increments so other threads can also acquire
            time.sleep(min(wait, 0.25))

    def penalize(self, idx: int, extra: float = 60.0) -> None:
        """Push key idx's next-available time further into the future."""
        with self._lock:
            self._next_ok[idx] = max(self._next_ok[idx], time.monotonic()) + extra


# ── index (fetched log) ───────────────────────────────────────────────────────

@dataclass
class IndexEntry:
    sha256:     str
    status:     str   # ok | not_found | error_NNN
    fetched_at: str
    path:       str   = ""   # relative path to vt.json (empty if not saved)

    def to_dict(self) -> dict:
        return {
            "sha256":     self.sha256,
            "status":     self.status,
            "fetched_at": self.fetched_at,
            "path":       self.path,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "IndexEntry":
        return cls(
            sha256=d.get("sha256", ""),
            status=d.get("status", ""),
            fetched_at=d.get("fetched_at", ""),
            path=d.get("path", ""),
        )


class Index:
    """Thread-safe persistent index of fetched SHA256s."""

    def __init__(self, reports_dir: Path) -> None:
        self._path = reports_dir / _INDEX_FILE
        self._lock = threading.Lock()
        self._data: dict[str, IndexEntry] = {}
        self._load()

    def _load(self) -> None:
        if not self._path.exists():
            return
        try:
            raw = json.loads(self._path.read_text())
            for entry in raw:
                e = IndexEntry.from_dict(entry)
                self._data[e.sha256] = e
        except Exception:
            pass

    def has(self, sha256: str) -> bool:
        with self._lock:
            return sha256 in self._data

    def record(self, entry: IndexEntry) -> None:
        with self._lock:
            self._data[entry.sha256] = entry
            self._path.parent.mkdir(parents=True, exist_ok=True)
            self._path.write_text(
                json.dumps([e.to_dict() for e in self._data.values()], indent=2)
            )

    def all_entries(self) -> list[IndexEntry]:
        with self._lock:
            return sorted(self._data.values(), key=lambda e: e.fetched_at, reverse=True)


# ── VT API call ───────────────────────────────────────────────────────────────

def fetch_vt(sha256: str, api_key: str, timeout: int = 30) -> tuple[int, dict | None]:
    """
    Call the VT files endpoint.  Returns (http_status, json_body | None).
    """
    try:
        r = requests.get(
            _VT_FILE_URL.format(sha256=sha256),
            headers={"x-apikey": api_key, "Accept": "application/json"},
            timeout=timeout,
        )
        if r.status_code == 200:
            return 200, r.json()
        return r.status_code, None
    except requests.RequestException as exc:
        console.print(f"  [red]network error[/red] {sha256[:16]}…: {exc}")
        return 0, None


# ── per-hash worker ───────────────────────────────────────────────────────────

def process_hash(sha256: str, rotator: KeyRotator, index: Index,
                 reports_dir: Path) -> str:
    """
    Fetch VT report for sha256, save to disk, update index.
    Returns a status string: ok | not_found | error_NNN | rate_limited.
    """
    for attempt in range(_MAX_RETRIES):
        api_key, key_idx = rotator.acquire()
        status_code, data = fetch_vt(sha256, api_key)

        if status_code == 200 and data:
            out = reports_dir / sha256 / "vt.json"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(data, indent=2))
            index.record(IndexEntry(
                sha256=sha256,
                status="ok",
                fetched_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                path=str(out.relative_to(reports_dir.parent)),
            ))
            return "ok"

        if status_code == 404:
            index.record(IndexEntry(
                sha256=sha256,
                status="not_found",
                fetched_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            ))
            return "not_found"

        if status_code == 429:
            rotator.penalize(key_idx)
            if attempt < _MAX_RETRIES - 1:
                continue   # retry with a different key

        status = f"error_{status_code}" if status_code else "network_error"
        index.record(IndexEntry(
            sha256=sha256,
            status=status,
            fetched_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        ))
        return status

    index.record(IndexEntry(
        sha256=sha256,
        status="rate_limited",
        fetched_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    ))
    return "rate_limited"


# ── sample discovery ──────────────────────────────────────────────────────────

def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def discover_hashes(samples_dir: Path) -> list[str]:
    """
    Walk samples_dir.  If a filename starts with a 64-char hex string
    (the format written by extract_pe) use that directly; otherwise compute
    SHA256 from file content.
    """
    hashes: set[str] = set()
    for f in sorted(samples_dir.iterdir()):
        if not f.is_file() or f.name.startswith("."):
            continue
        prefix = f.name[:64].lower()
        if len(prefix) == 64 and all(c in "0123456789abcdef" for c in prefix):
            hashes.add(prefix)
        else:
            hashes.add(sha256_of_file(f))
    return sorted(hashes)


# ── list command ──────────────────────────────────────────────────────────────

def cmd_list(reports_dir: Path) -> None:
    index = Index(reports_dir)
    entries = index.all_entries()
    if not entries:
        console.print("[dim]Index is empty — no hashes fetched yet.[/dim]")
        return

    tbl = Table(show_header=True, header_style="bold dim", box=None, padding=(0, 2))
    tbl.add_column("SHA256",     width=20)
    tbl.add_column("Status",     width=14)
    tbl.add_column("Fetched At", width=22)
    tbl.add_column("Path")

    status_styles = {
        "ok":           "green",
        "not_found":    "yellow",
        "rate_limited": "red",
    }

    for e in entries:
        style = status_styles.get(e.status, "red")
        tbl.add_row(
            e.sha256[:20] + "…",
            f"[{style}]{e.status}[/{style}]",
            e.fetched_at,
            e.path or "—",
        )

    console.print(tbl)
    console.print(f"\n[dim]{len(entries)} record(s) in {reports_dir / _INDEX_FILE}[/dim]")


# ── main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="vt.py",
        description="Fetch VirusTotal reports for malware samples.",
    )
    parser.add_argument("hashes", nargs="*",
                        help="SHA256 hash(es) to look up (skip to scan --dir)")
    parser.add_argument("--dir",     default="samples",
                        help="Samples directory to auto-scan (default: samples/)")
    parser.add_argument("--reports", default="reports",
                        help="Reports root directory (default: reports/)")
    parser.add_argument("--env",     default=".env",
                        help="Path to .env file (default: .env)")
    parser.add_argument("--list",    action="store_true",
                        help="Print the fetched index and exit")
    parser.add_argument("--force",   action="store_true",
                        help="Re-fetch even if hash is already in the index")

    args         = parser.parse_args()
    reports_dir  = Path(args.reports)
    samples_dir  = Path(args.dir)

    if args.list:
        cmd_list(reports_dir)
        return

    # ── load keys ─────────────────────────────────────────────────────────────
    env  = load_dotenv(args.env)
    keys = load_vt_keys(env)
    if not keys:
        console.print(
            f"[red]No VT keys found.[/red]  "
            f"Add VT_KEY_1=… to [bold]{args.env}[/bold]  "
            f"(see .env.example)"
        )
        return

    rate = vt_rate_limit(env)
    console.print(
        f"[bold]VirusTotal[/bold]  "
        f"{len(keys)} key(s)  ·  "
        f"{rate:.0f}s/key rate limit  ·  "
        f"effective throughput: [green]{len(keys) * 60 / rate:.1f} req/min[/green]"
    )

    # ── collect hashes ────────────────────────────────────────────────────────
    if args.hashes:
        hashes = [h.lower().strip() for h in args.hashes]
        bad    = [h for h in hashes if len(h) != 64 or not all(c in "0123456789abcdef" for c in h)]
        if bad:
            for h in bad:
                console.print(f"[red]invalid sha256:[/red] {h}")
            return
    else:
        if not samples_dir.is_dir():
            console.print(f"[red]Samples directory not found:[/red] {samples_dir}")
            return
        hashes = discover_hashes(samples_dir)
        if not hashes:
            console.print(f"[dim]No samples found in {samples_dir}[/dim]")
            return

    # ── filter already-fetched ────────────────────────────────────────────────
    index = Index(reports_dir)
    if args.force:
        todo = hashes
    else:
        todo = [h for h in hashes if not index.has(h)]
        skipped = len(hashes) - len(todo)
        if skipped:
            console.print(f"[dim]Skipping {skipped} already-fetched hash(es)[/dim]")

    if not todo:
        console.print("[green]Nothing to fetch.[/green]")
        return

    console.print(f"Fetching [bold]{len(todo)}[/bold] hash(es)…\n")

    # ── parallel fetch ────────────────────────────────────────────────────────
    rotator = KeyRotator(keys, rate_limit=rate)
    counts  = {"ok": 0, "not_found": 0, "error": 0}

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Fetching VT reports", total=len(todo))

        # use as many workers as keys, but cap at the queue depth
        n_workers = min(len(keys), len(todo))
        with ThreadPoolExecutor(max_workers=n_workers,
                                thread_name_prefix="vt") as pool:
            futures = {
                pool.submit(process_hash, sha256, rotator, index, reports_dir): sha256
                for sha256 in todo
            }
            for fut in as_completed(futures):
                sha256 = futures[fut]
                try:
                    status = fut.result()
                except Exception as exc:
                    status = "error"
                    console.print(f"  [red]worker crash[/red] {sha256[:16]}…: {exc}")

                if status == "ok":
                    counts["ok"] += 1
                    label = "[green]ok[/green]"
                elif status == "not_found":
                    counts["not_found"] += 1
                    label = "[yellow]not found[/yellow]"
                else:
                    counts["error"] += 1
                    label = f"[red]{status}[/red]"

                progress.console.print(f"  {sha256[:20]}…  {label}")
                progress.advance(task)

    console.print(
        f"\n[bold green]Done[/bold green]  "
        f"ok: {counts['ok']}  "
        f"not found: {counts['not_found']}  "
        f"errors: {counts['error']}"
    )
    console.print(f"[dim]Index: {reports_dir / _INDEX_FILE}[/dim]")


if __name__ == "__main__":
    main()
