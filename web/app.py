from __future__ import annotations

import asyncio
import json
import re
import time
from pathlib import Path
from typing import AsyncGenerator

import mistune
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

from web.queue_manager import QueueManager, system_status

_TEMPLATES_DIR   = Path(__file__).parent / "templates"
_SHA256_RE       = re.compile(r"^[0-9a-fA-F]{64}$")
_SAFE_FILENAME_RE = re.compile(r"^[\w. -]+\.c$")


def build_app(cfg: dict) -> FastAPI:
    reports_root = Path(cfg.get("paths", {}).get("reports", "./reports")).resolve()
    samples_root = Path(cfg.get("paths", {}).get("samples", "./samples")).resolve()
    web_cfg      = cfg.get("web", {})
    backend_url  = web_cfg.get("backend_url", "").rstrip("/")
    cors_origins = web_cfg.get("cors_origins", ["*"])

    app       = FastAPI(title="RE Pipeline — Control Panel")
    templates = Jinja2Templates(directory=str(_TEMPLATES_DIR))
    queue     = QueueManager(cfg)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ── dashboard ─────────────────────────────────────────────────────────────

    @app.get("/", response_class=HTMLResponse)
    async def dashboard(request: Request):
        return templates.TemplateResponse("dashboard.html", {
            "request":      request,
            "samples_path": str(samples_root),
            "backend_url":  backend_url,
        })

    # ── report browser ────────────────────────────────────────────────────────

    @app.get("/reports", response_class=HTMLResponse)
    async def report_index(request: Request):
        reports = _load_reports(reports_root)
        return templates.TemplateResponse("index.html", {"request": request, "reports": reports})

    @app.get("/report/{sha256}", response_class=HTMLResponse)
    async def report(request: Request, sha256: str):
        if not _SHA256_RE.match(sha256):
            raise HTTPException(status_code=400, detail="Invalid SHA256")
        md_path = reports_root / sha256 / "report.md"
        if not md_path.exists():
            raise HTTPException(status_code=404, detail="Report not found")
        html_content = mistune.html(md_path.read_text())
        code_dir     = reports_root / sha256 / "code"
        code_files   = sorted(f.name for f in code_dir.glob("*.c")) if code_dir.exists() else []
        return templates.TemplateResponse(
            "report.html",
            {"request": request, "sha256": sha256, "content": html_content, "code_files": code_files},
        )

    @app.get("/report/{sha256}/code/{filename}", response_class=PlainTextResponse)
    async def code_file(sha256: str, filename: str):
        if not _SHA256_RE.match(sha256):
            raise HTTPException(status_code=400, detail="Invalid SHA256")
        if not _SAFE_FILENAME_RE.match(filename):
            raise HTTPException(status_code=400, detail="Invalid filename")
        file_path = reports_root / sha256 / "code" / filename
        if not file_path.exists() or not file_path.is_relative_to(reports_root):
            raise HTTPException(status_code=404, detail="File not found")
        return file_path.read_text()

    # ── API: system status ────────────────────────────────────────────────────

    @app.get("/api/status")
    async def api_status():
        loop   = asyncio.get_event_loop()
        status = await loop.run_in_executor(None, system_status, cfg)
        status["report_count"] = sum(
            1 for d in reports_root.iterdir()
            if d.is_dir() and _SHA256_RE.match(d.name)
        ) if reports_root.exists() else 0
        status["watch"] = queue.watch_status()
        return JSONResponse(status)

    # ── API: upload & analyze ─────────────────────────────────────────────────

    @app.post("/api/upload")
    async def api_upload(file: UploadFile = File(...)):
        filename = Path(file.filename or "sample").name  # strip any path
        data     = await file.read()
        if len(data) == 0:
            raise HTTPException(status_code=400, detail="Empty file")
        loop = asyncio.get_event_loop()
        job  = await loop.run_in_executor(None, queue.submit, filename, data)
        return JSONResponse(job.to_dict(), status_code=202)

    # ── API: job queue ────────────────────────────────────────────────────────

    @app.get("/api/jobs")
    async def api_jobs():
        return JSONResponse([j.to_dict() for j in queue.get_jobs()])

    @app.get("/api/jobs/{job_id}")
    async def api_job(job_id: str):
        job = queue.get_job(job_id)
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        return JSONResponse(job.to_dict())

    @app.get("/api/jobs/{job_id}/logs")
    async def api_job_logs_sse(job_id: str, after: int = 0):
        """Server-Sent Events stream of job log lines."""
        job = queue.get_job(job_id)
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")

        async def _generate() -> AsyncGenerator[str, None]:
            from web.queue_manager import JobStatus
            cursor = after
            while True:
                new_lines = queue.get_logs(job_id, cursor)
                for line in new_lines:
                    yield f"data: {json.dumps(line)}\n\n"
                cursor += len(new_lines)

                current_job = queue.get_job(job_id)
                if current_job and current_job.status in (JobStatus.DONE, JobStatus.ERROR):
                    # flush any remaining lines then close
                    remaining = queue.get_logs(job_id, cursor)
                    for line in remaining:
                        yield f"data: {json.dumps(line)}\n\n"
                    yield "event: done\ndata: {}\n\n"
                    break

                await asyncio.sleep(0.4)

        return StreamingResponse(_generate(), media_type="text/event-stream", headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        })

    # ── API: resume job ───────────────────────────────────────────────────────

    @app.post("/api/jobs/{job_id}/resume")
    async def api_job_resume(job_id: str):
        loop = asyncio.get_event_loop()
        job  = await loop.run_in_executor(None, queue.resume_job, job_id)
        if not job:
            raise HTTPException(
                status_code=400,
                detail="Cannot resume: job not in error state or no checkpoint available",
            )
        return JSONResponse(job.to_dict())

    # ── API: watch mode ───────────────────────────────────────────────────────

    @app.post("/api/watch/start")
    async def api_watch_start(path: str = Form(default="")):
        watch_path = Path(path.strip()) if path.strip() else samples_root
        ok, msg    = queue.start_watch(watch_path)
        return JSONResponse({"ok": ok, "message": msg, "watch": queue.watch_status()},
                            status_code=200 if ok else 400)

    @app.post("/api/watch/stop")
    async def api_watch_stop():
        ok, msg = queue.stop_watch()
        return JSONResponse({"ok": ok, "message": msg, "watch": queue.watch_status()})

    # ── API: recent reports (for dashboard widget) ────────────────────────────

    @app.get("/api/reports")
    async def api_reports(limit: int = 10):
        reports = _load_reports(reports_root)[:limit]
        return JSONResponse(reports)

    return app


# ── helpers ───────────────────────────────────────────────────────────────────

def _load_reports(reports_root: Path) -> list[dict]:
    if not reports_root.exists():
        return []
    reports = []
    for sample_dir in sorted(reports_root.iterdir(), key=lambda d: d.stat().st_mtime, reverse=True):
        report_path = sample_dir / "report.md"
        if not sample_dir.is_dir() or not report_path.exists():
            continue
        sha256 = sample_dir.name
        if not re.match(r"^[0-9a-fA-F]{64}$", sha256):
            continue
        content     = report_path.read_text()
        name_match  = re.search(r"\*\*Sample:\*\* `(.+?)`", content)
        family_match = re.search(r"## Malware Family Classification\n+(.+)", content)
        code_count  = len(list((sample_dir / "code").glob("*.c"))) if (sample_dir / "code").exists() else 0
        reports.append({
            "sha256":     sha256,
            "name":       name_match.group(1) if name_match else sha256[:16],
            "family":     (family_match.group(1).strip()[:80] if family_match else "Unknown"),
            "mtime":      report_path.stat().st_mtime,
            "code_count": code_count,
        })
    return reports
