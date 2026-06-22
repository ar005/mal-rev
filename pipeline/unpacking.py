from __future__ import annotations
import collections
import logging
import math
import shutil
import subprocess
from pathlib import Path

from pipeline import Sample

log = logging.getLogger(__name__)

_PACKED_MARKERS = ("upx", "mpress", "aspack", "petite", "pecompact", "fsg", "packed")


def _quick_entropy(path: Path) -> float:
    data = path.read_bytes()[:65536]
    if not data:
        return 0.0
    counts = collections.Counter(data)
    total = len(data)
    return -sum((c / total) * math.log2(c / total) for c in counts.values())


def _is_likely_packed(sample: Sample, entropy_threshold: float) -> bool:
    ft = sample.file_type.lower()
    if any(m in ft for m in _PACKED_MARKERS):
        return True
    return _quick_entropy(sample.path) >= entropy_threshold


def _try_upx(src: Path, dst: Path) -> bool:
    if not shutil.which("upx"):
        log.debug("upx binary not found in PATH")
        return False
    try:
        r = subprocess.run(
            ["upx", "-d", str(src), "-o", str(dst)],
            capture_output=True, timeout=30,
        )
        if r.returncode == 0 and dst.exists() and dst.stat().st_size > 0:
            return True
        log.debug("upx -d exit %d: %s", r.returncode,
                  r.stderr.decode(errors="replace")[:200])
    except subprocess.TimeoutExpired:
        log.debug("upx timed out")
    except Exception as exc:
        log.debug("upx error: %s", exc)
    if dst.exists():
        dst.unlink(missing_ok=True)
    return False


def _try_unipacker(src: Path, dst: Path) -> bool:
    if not shutil.which("unipacker"):
        log.debug("unipacker not found in PATH")
        return False
    tmp_dir = dst.parent / "_unipacker_tmp"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    try:
        r = subprocess.run(
            ["unipacker", "--auto-run", "--output-dir", str(tmp_dir), str(src)],
            capture_output=True, timeout=120,
        )
        candidates = [f for f in tmp_dir.iterdir() if f.is_file() and f.stat().st_size > 0]
        if candidates:
            shutil.move(str(candidates[0]), str(dst))
            return True
        log.debug("unipacker exit %d, no output produced", r.returncode)
    except subprocess.TimeoutExpired:
        log.debug("unipacker timed out")
    except Exception as exc:
        log.debug("unipacker error: %s", exc)
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)
    return False


def run(sample: Sample, cfg: dict) -> Sample:
    threshold = cfg.get("analysis", {}).get("entropy_threshold", 7.0)

    if not _is_likely_packed(sample, threshold):
        return sample

    reports_dir = Path(cfg.get("paths", {}).get("reports", "./reports"))
    out_dir = reports_dir / sample.sha256
    out_dir.mkdir(parents=True, exist_ok=True)

    suffix = sample.path.suffix or ".bin"
    unpacked_path = out_dir / f"unpacked{suffix}"

    # Resume-safe: skip if already unpacked from a previous run
    if unpacked_path.exists() and unpacked_path.stat().st_size > 0:
        log.info("Reusing cached unpacked file: %s", unpacked_path.name)
        sample.path = unpacked_path
        sample.unpacked = True
        sample.unpacker = "cached"
        return sample

    log.info("Packing detected (%s) — trying to unpack…", sample.file_type)

    if _try_upx(sample.path, unpacked_path):
        log.info("UPX unpack succeeded → %s", unpacked_path.name)
        sample.path = unpacked_path
        sample.unpacked = True
        sample.unpacker = "upx"
        return sample

    if _try_unipacker(sample.path, unpacked_path):
        log.info("unipacker succeeded → %s", unpacked_path.name)
        sample.path = unpacked_path
        sample.unpacked = True
        sample.unpacker = "unipacker"
        return sample

    log.warning("All unpack attempts failed — analyzing packed binary as-is")
    return sample
