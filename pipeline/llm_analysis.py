from __future__ import annotations
import logging
import os
import time
from pathlib import Path
from typing import Callable

from pipeline import Sample
from pipeline.timeout import StageTimeoutError

log = logging.getLogger(__name__)

_PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

try:
    import ollama as _ollama
    _has_ollama = True
except ImportError:
    _has_ollama = False

try:
    import anthropic as _anthropic
    _has_anthropic = True
except ImportError:
    _has_anthropic = False


def _load_prompt(name: str) -> str:
    return (_PROMPTS_DIR / f"{name}.txt").read_text()


# ---------------------------------------------------------------------------
# Provider backends
# ---------------------------------------------------------------------------

def _ask_ollama(prompt: str, cfg: dict) -> str:
    if not _has_ollama:
        return "(ollama package not installed)"

    # per-call timeout: passed to httpx so a frozen Ollama generation is killed
    call_timeout = cfg.get("call_timeout", 300)
    client  = _ollama.Client(host=cfg["base_url"], timeout=call_timeout)
    options = {"num_ctx": cfg.get("num_ctx", 131072)}
    think   = cfg.get("think", False)

    kwargs: dict = dict(
        model=cfg["model"],
        messages=[{"role": "user", "content": prompt}],
        stream=False,
        options=options,
    )
    if think:
        kwargs["think"] = True

    response = client.chat(**kwargs)
    return response["message"]["content"].strip()


def _ask_claude(prompt: str, cfg: dict) -> str:
    if not _has_anthropic:
        return "(anthropic package not installed — pip install anthropic)"

    api_key  = cfg.get("api_key") or os.environ.get("ANTHROPIC_API_KEY", "")
    base_url = cfg.get("base_url", "")  # non-empty → override API endpoint (e.g. Ollama)

    if not base_url and not api_key:
        return "(no Claude API key — set claude.api_key in config.yaml or ANTHROPIC_API_KEY env var)"

    client_kwargs: dict = {"api_key": api_key or "ollama"}
    if base_url:
        client_kwargs["base_url"] = base_url

    client     = _anthropic.Anthropic(**client_kwargs)
    model      = cfg.get("model", "claude-sonnet-4-6")
    max_tokens = cfg.get("max_tokens", 8192)
    think      = cfg.get("think", False)

    kwargs: dict = dict(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    if think:
        # Extended thinking: budget must be < max_tokens
        budget = min(cfg.get("think_budget_tokens", 5000), max_tokens - 1024)
        kwargs["thinking"] = {"type": "enabled", "budget_tokens": budget}

    response = client.messages.create(**kwargs)

    # Ollama's Anthropic-compatible API sometimes returns content=None.
    # Try content blocks first, then fall back to any top-level text attribute.
    content = response.content or []
    text_parts = [b.text for b in content if hasattr(b, "text")]
    if text_parts:
        return "\n".join(text_parts).strip()

    # Fallback: some Ollama builds put the reply in response.text or response.completion
    for attr in ("text", "completion"):
        val = getattr(response, attr, None)
        if val:
            return str(val).strip()

    log.warning("_ask_claude: response had no extractable text (content=%r)", response.content)
    return ""


# ---------------------------------------------------------------------------
# Chunked runner (provider-agnostic)
# ---------------------------------------------------------------------------

def _ask_chunked(
    ask_fn: Callable[[str, dict], str],
    provider_cfg: dict,
    template: str,
    chunks: list[str],
    **kwargs,
) -> str:
    """Send disasm context to the LLM, handling multi-chunk binaries."""
    if not chunks:
        return "(no disassembly available)"

    if len(chunks) == 1:
        prompt = template.format(disassembly=chunks[0], **kwargs)
        return ask_fn(prompt, provider_cfg)

    summary = ""
    for i, chunk in enumerate(chunks):
        if i == 0:
            prompt = template.format(disassembly=chunk, **kwargs)
        else:
            prompt = (
                f"Continue your analysis. Here is more disassembly "
                f"(chunk {i + 1}/{len(chunks)}).\n"
                f"Previous summary:\n{summary}\n\n"
                f"--- ADDITIONAL DISASSEMBLY ---\n{chunk}\n\n"
                "Update and extend your analysis, keeping all previous findings:"
            )
        summary = ask_fn(prompt, provider_cfg)
        log.debug("LLM chunk %d/%d processed", i + 1, len(chunks))

    return summary


# ---------------------------------------------------------------------------
# Context builder
# ---------------------------------------------------------------------------

def _build_analysis_chunks(sample: Sample, chunk_size: int) -> list[str]:
    """Return LLM-ready disassembly chunks, preferring pure C pseudocode."""
    if sample.decompiled:
        parts = [
            f"// Function: {name}\n{code}"
            for name, code in sample.decompiled.items()
        ]
        combined = "\n\n".join(parts)
        log.info(
            "LLM context: %d decompiled C function(s) → %d char(s)",
            len(sample.decompiled), len(combined),
        )
        return [combined[i : i + chunk_size] for i in range(0, len(combined), chunk_size)] or ["(empty)"]

    if sample.disasm_chunks:
        log.info("LLM context: raw disassembly chunks (no C pseudocode available)")
        return sample.disasm_chunks

    return ["(no disassembly available)"]


# ---------------------------------------------------------------------------
# Stage entry point
# ---------------------------------------------------------------------------

def run(sample: Sample, cfg: dict) -> Sample:
    provider_name: str = cfg.get("provider", "ollama").lower()

    timeouts     = cfg.get("timeouts", {})
    call_timeout = timeouts.get("llm_call", 300)   # seconds per individual LLM HTTP call

    if provider_name == "claude":
        if not _has_anthropic:
            log.error("provider=claude but 'anthropic' package is not installed. "
                      "Run: pip install anthropic")
            return sample
        provider_cfg = cfg.get("claude", {})
        ask_fn       = _ask_claude
        chunk_size   = provider_cfg.get("chunk_size", 180000)
        log.info("LLM provider: Claude API (%s)", provider_cfg.get("model", "claude-sonnet-4-6"))

    elif provider_name == "claude-ollama":
        if not _has_ollama:
            log.error("provider=claude-ollama but 'ollama' package is not installed.")
            return sample
        raw_cfg      = cfg.get("claude_ollama", {})
        provider_cfg = {
            "base_url":    raw_cfg.get("base_url", "http://localhost:11434"),
            "model":       raw_cfg.get("model", "gemma4:12b"),
            "num_ctx":     raw_cfg.get("num_ctx", 131072),
            "think":       raw_cfg.get("think", True),
            "call_timeout": call_timeout,
        }
        ask_fn     = _ask_ollama
        chunk_size = raw_cfg.get("chunk_size", 120000)
        log.info("LLM provider: Claude-Ollama / Ollama native (%s @ %s)",
                 provider_cfg["model"], provider_cfg["base_url"])

    else:
        if not _has_ollama:
            log.error("provider=ollama but 'ollama' package is not installed.")
            return sample
        provider_cfg = dict(cfg.get("ollama", {}))
        provider_cfg.setdefault("call_timeout", call_timeout)
        ask_fn     = _ask_ollama
        chunk_size = provider_cfg.get("chunk_size", 120000)
        log.info("LLM provider: Ollama (%s)", provider_cfg.get("model", "gemma4:12b"))

    strings_sample = "\n".join(sample.static.get("strings", [])[:200])
    disasm_chunks  = _build_analysis_chunks(sample, chunk_size)
    log.info("LLM analysis context: %d chunk(s)", len(disasm_chunks))

    # Helper: raise StageTimeoutError if the whole LLM stage would overrun.
    # The SIGALRM in batch.py is the hard backstop; this gives a clean log message.
    llm_start   = time.monotonic()
    llm_limit_s = timeouts.get("llm", 3600)

    def _guard(pass_name: str) -> None:
        elapsed = time.monotonic() - llm_start
        if elapsed >= llm_limit_s:
            raise StageTimeoutError(
                f"LLM stage total limit {llm_limit_s // 60}m reached before {pass_name}"
            )
        log.debug("LLM elapsed %.0fs / %ds before %s", elapsed, llm_limit_s, pass_name)

    # 1. Behavior summary — full disassembly / C pseudocode in context
    _guard("behavior")
    log.info("LLM pass 1/4: behavior summary…")
    sample.behavior_summary = _ask_chunked(
        ask_fn, provider_cfg,
        _load_prompt("behavior"),
        disasm_chunks,
        strings=strings_sample,
    )

    # 2. MITRE ATT&CK mapping
    _guard("mitre")
    log.info("LLM pass 2/4: MITRE ATT&CK mapping…")
    sample.mitre_mapping = ask_fn(
        _load_prompt("mitre").format(behavior_summary=sample.behavior_summary),
        provider_cfg,
    )

    # 3. IOC extraction
    _guard("ioc")
    log.info("LLM pass 3/4: IOC extraction…")
    sample.iocs = ask_fn(
        _load_prompt("ioc").format(
            strings=strings_sample,
            behavior_summary=sample.behavior_summary,
        ),
        provider_cfg,
    )

    # 4. Family classification
    _guard("family")
    log.info("LLM pass 4/4: family classification…")
    sample.family = ask_fn(
        _load_prompt("family").format(
            behavior_summary=sample.behavior_summary,
            mitre_mapping=sample.mitre_mapping,
            iocs=sample.iocs,
        ),
        provider_cfg,
    )

    log.info("LLM analysis complete")
    return sample
