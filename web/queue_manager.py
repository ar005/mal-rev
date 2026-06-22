from __future__ import annotations

import pickle
import shutil
import subprocess
import tempfile
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional
from urllib.request import urlopen
from urllib.error import URLError


class JobStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE    = "done"
    ERROR   = "error"


@dataclass
class Job:
    id:               str
    filename:         str
    file_path:        Path
    status:           JobStatus        = JobStatus.PENDING
    stage:            str              = ""
    logs:             list[str]        = field(default_factory=list)
    started_at:       Optional[float]  = None
    finished_at:      Optional[float]  = None
    sha256:           Optional[str]    = None
    family:           Optional[str]    = None
    error:            Optional[str]    = None
    completed_stages: list[str]        = field(default_factory=list)
    checkpoint_stage: int              = -1   # index of last checkpointed stage

    def to_dict(self) -> dict:
        return {
            "id":               self.id,
            "filename":         self.filename,
            "status":           self.status.value,
            "stage":            self.stage,
            "started_at":       self.started_at,
            "finished_at":      self.finished_at,
            "sha256":           self.sha256,
            "family":           self.family,
            "error":            self.error,
            "log_count":        len(self.logs),
            "completed_stages": self.completed_stages,
            "resumable":        self.status == JobStatus.ERROR and self.checkpoint_stage >= 0,
        }


class QueueManager:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        self._jobs: dict[str, Job] = {}
        self._lock  = threading.Lock()
        self._executor = ThreadPoolExecutor(max_workers=1)  # one analysis at a time
        self._tmpdir   = Path(tempfile.mkdtemp(prefix="re_pipeline_"))
        self._watch_observer = None
        self._watch_path: Optional[Path] = None

    # ── job submission ────────────────────────────────────────────────────────

    def submit(self, filename: str, data: bytes) -> Job:
        dest = self._tmpdir / f"{uuid.uuid4().hex}_{filename}"
        dest.write_bytes(data)
        job = Job(id=str(uuid.uuid4()), filename=filename, file_path=dest)
        with self._lock:
            self._jobs[job.id] = job
        self._executor.submit(self._run_job, job.id)
        return job

    def submit_path(self, path: Path) -> Job:
        job = Job(id=str(uuid.uuid4()), filename=path.name, file_path=path)
        with self._lock:
            self._jobs[job.id] = job
        self._executor.submit(self._run_job, job.id)
        return job

    # ── checkpointing ─────────────────────────────────────────────────────────

    def _ckpt_path(self, job_id: str) -> Path:
        return self._tmpdir / f"{job_id}.ckpt"

    def _save_checkpoint(self, job_id: str, stage_idx: int, sample) -> None:
        self._ckpt_path(job_id).write_bytes(
            pickle.dumps({"stage_idx": stage_idx, "sample": sample})
        )

    def _load_checkpoint(self, job_id: str) -> Optional[dict]:
        cp = self._ckpt_path(job_id)
        if not cp.exists():
            return None
        try:
            return pickle.loads(cp.read_bytes())
        except Exception:
            return None

    # ── pipeline execution ────────────────────────────────────────────────────

    def _run_job(self, job_id: str, start_from: int = 0, initial_sample=None) -> None:
        from pipeline import ingestion, static_analysis, disassembly, llm_analysis, reporting

        job = self._jobs[job_id]
        job.status = JobStatus.RUNNING
        if start_from == 0:
            job.started_at = time.time()

        def log(msg: str) -> None:
            job.logs.append(f"[{time.strftime('%H:%M:%S')}] {msg}")

        stages = [
            ("Ingesting sample",  lambda s: ingestion.load_sample(job.file_path)),
            ("Static analysis",   lambda s: static_analysis.run(s, self.cfg)),
            ("Disassembly",       lambda s: disassembly.run(s, self.cfg)),
            ("LLM analysis",      lambda s: llm_analysis.run(s, self.cfg)),
            ("Generating report", lambda s: reporting.run(s, self.cfg)),
        ]

        sample = initial_sample
        try:
            for i, (desc, fn) in enumerate(stages):
                if i < start_from:
                    continue
                job.stage = desc
                log(f"[{i + 1}/5] {desc}…")
                sample = fn(sample)
                self._save_checkpoint(job_id, i, sample)
                if desc not in job.completed_stages:
                    job.completed_stages.append(desc)
                job.checkpoint_stage = i
                log(f"[{i + 1}/5] {desc} ✓")

            job.sha256      = sample.sha256
            raw_family      = (sample.family or "").splitlines()[0] if sample.family else ""
            job.family      = raw_family or "Unknown"
            job.status      = JobStatus.DONE
            log(f"Complete — report saved to reports/{sample.sha256}/")
        except Exception as exc:
            job.status = JobStatus.ERROR
            job.error  = str(exc)
            log(f"ERROR: {exc}")
        finally:
            job.finished_at = time.time()

    # ── resume ────────────────────────────────────────────────────────────────

    def resume_job(self, job_id: str) -> Optional[Job]:
        """Resume an errored job from the last successful checkpoint stage."""
        job = self._jobs.get(job_id)
        if not job or job.status != JobStatus.ERROR:
            return None
        cp = self._load_checkpoint(job_id)
        if cp is None:
            return None
        start_from    = cp["stage_idx"] + 1
        initial_sample = cp["sample"]
        job.status    = JobStatus.PENDING
        job.error     = None
        job.logs.append(
            f"[{time.strftime('%H:%M:%S')}] Resuming from stage {start_from + 1}/5…"
        )
        self._executor.submit(self._run_job, job_id, start_from, initial_sample)
        return job

    # ── query ─────────────────────────────────────────────────────────────────

    def get_jobs(self) -> list[Job]:
        with self._lock:
            return sorted(self._jobs.values(), key=lambda j: j.started_at or 0, reverse=True)

    def get_job(self, job_id: str) -> Optional[Job]:
        return self._jobs.get(job_id)

    def get_logs(self, job_id: str, after: int = 0) -> list[str]:
        job = self._jobs.get(job_id)
        if not job:
            return []
        return job.logs[after:]

    # ── watch mode ────────────────────────────────────────────────────────────

    def start_watch(self, watch_path: Path) -> tuple[bool, str]:
        if self._watch_observer is not None:
            return False, "Watch already active"
        try:
            from watchdog.observers import Observer
            from watchdog.events import FileSystemEventHandler
        except ImportError:
            return False, "watchdog not installed (pip install watchdog)"

        if not watch_path.is_dir():
            return False, f"Directory not found: {watch_path}"

        seen: set[str] = set()
        mgr = self

        class _Handler(FileSystemEventHandler):
            def on_created(self, event):
                if event.is_directory:
                    return
                p = Path(event.src_path)
                key = str(p)
                if key in seen:
                    return
                seen.add(key)
                mgr.submit_path(p)

        obs = Observer()
        obs.schedule(_Handler(), str(watch_path), recursive=False)
        obs.start()
        self._watch_observer = obs
        self._watch_path = watch_path
        return True, f"Watching {watch_path}"

    def stop_watch(self) -> tuple[bool, str]:
        if self._watch_observer is None:
            return False, "Watch not active"
        self._watch_observer.stop()
        self._watch_observer.join()
        self._watch_observer = None
        self._watch_path = None
        return True, "Watch stopped"

    def watch_status(self) -> dict:
        return {
            "active": self._watch_observer is not None,
            "path":   str(self._watch_path) if self._watch_path else "",
        }


# ── system health ─────────────────────────────────────────────────────────────

def system_status(cfg: dict) -> dict:
    base_url = cfg.get("ollama", {}).get("base_url", "http://localhost:11434")
    model    = cfg.get("ollama", {}).get("model", "?")

    # Ollama reachability
    ollama_ok = False
    ollama_model_present = False
    try:
        with urlopen(f"{base_url}/api/tags", timeout=2) as resp:
            import json
            data = json.loads(resp.read())
            ollama_ok = True
            ollama_model_present = any(
                m.get("name", "").startswith(model.split(":")[0])
                for m in data.get("models", [])
            )
    except (URLError, Exception):
        pass

    # radare2
    r2_ok = shutil.which("r2") is not None

    # r2ghidra — check via r2 plugin list (fast probe)
    r2ghidra_ok = False
    if r2_ok:
        try:
            result = subprocess.run(
                ["r2", "-q", "-c", "Lc;q", "/dev/null"],
                capture_output=True, text=True, timeout=5,
            )
            r2ghidra_ok = "r2ghidra" in result.stdout or "ghidra" in result.stdout.lower()
        except Exception:
            pass

    return {
        "ollama":           ollama_ok,
        "ollama_model":     model,
        "ollama_model_ok":  ollama_model_present,
        "radare2":          r2_ok,
        "r2ghidra":         r2ghidra_ok,
    }
