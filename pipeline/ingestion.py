from __future__ import annotations
import hashlib
import logging
from pathlib import Path

from pipeline import Sample

log = logging.getLogger(__name__)

# Try python-magic; fall back to extension-based detection if not installed.
try:
    import magic as _magic
    _use_magic = True
except ImportError:
    _use_magic = False
    log.warning("python-magic not available; falling back to extension-based file type detection")


def _detect_type(path: Path) -> str:
    if _use_magic:
        return _magic.from_file(str(path))
    ext = path.suffix.lower()
    mapping = {
        ".exe": "PE32 executable",
        ".dll": "PE32 dynamic-link library",
        ".sys": "PE32 driver",
        ".elf": "ELF executable",
        ".sh": "Bourne-Again shell script",
        ".ps1": "PowerShell script",
        ".js": "JavaScript",
        ".py": "Python script",
    }
    return mapping.get(ext, "data")


def _hash_file(path: Path) -> tuple[str, str, str]:
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)
    return md5.hexdigest(), sha1.hexdigest(), sha256.hexdigest()


def load_sample(path: str | Path) -> Sample:
    path = Path(path).resolve()
    if not path.is_file():
        raise FileNotFoundError(path)

    md5, sha1, sha256 = _hash_file(path)
    file_type = _detect_type(path)
    size = path.stat().st_size

    log.info("Loaded sample: %s  sha256=%s  type=%s", path.name, sha256[:16] + "…", file_type)
    return Sample(
        path=path,
        file_type=file_type,
        md5=md5,
        sha1=sha1,
        sha256=sha256,
        size=size,
    )
