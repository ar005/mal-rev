"""pipeline/timeout.py — SIGALRM-based stage timeout for the RE pipeline (Linux only)."""
from __future__ import annotations

import contextlib
import signal


class StageTimeoutError(Exception):
    """Raised when a pipeline stage exceeds its configured time limit."""


@contextlib.contextmanager
def stage_timeout(seconds: int, label: str = "stage"):
    """Raise StageTimeoutError if the body takes longer than *seconds*.

    Uses SIGALRM so it interrupts blocking C-extension calls (r2pipe, httpx).
    Must be called from the main thread.  seconds=0 disables the timeout.
    """
    if seconds <= 0:
        yield
        return

    def _handler(signum, frame):
        raise StageTimeoutError(
            f"{label} timed out after {seconds // 60}m {seconds % 60:02d}s"
        )

    old_handler = signal.signal(signal.SIGALRM, _handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)
