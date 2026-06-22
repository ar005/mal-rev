from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Sample:
    path: Path
    file_type: str = ""
    md5: str = ""
    sha1: str = ""
    sha256: str = ""
    size: int = 0

    # populated by static_analysis
    static: dict[str, Any] = field(default_factory=dict)

    # populated by disassembly
    functions: list[dict[str, Any]] = field(default_factory=list)
    disasm_chunks: list[str] = field(default_factory=list)
    # function name → decompiled C pseudocode (populated by disassembly if r2ghidra available)
    decompiled: dict[str, str] = field(default_factory=dict)

    # populated by llm_analysis
    behavior_summary: str = ""
    mitre_mapping: str = ""
    iocs: str = ""
    family: str = ""

    # populated by unpacking (optional stage)
    unpacked: bool = False
    unpacker: str = ""   # "upx" | "unipacker" | "cached" | ""

    # populated by reporting
    report_path: Path | None = None
