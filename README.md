# RE Pipeline

A local malware reverse-engineering pipeline for threat hunting. Drop a binary, get a full threat intelligence report with decompiled C pseudocode and LLM-driven analysis. Analysis stays on your machine with Ollama, or routes to the Anthropic API.

```
sample.exe  ──►  unpack  ──►  static analysis  ──►  disassembly + decompilation (r2ghidra)
                                                                        │
                                                              C pseudocode / raw asm
                                                                        │
                                                               LLM analysis (4 passes)
                                                                        │
                                               report.md + code/*.c + vt.json
```

---

## What it does

For every sample the pipeline runs six stages:

| Stage | Tool | Output |
|-------|------|--------|
| **Ingestion** | python-magic | MD5 / SHA1 / SHA256, file type |
| **Unpacking** | upx, unipacker | Transparent UPX / MPRESS / ASPack / PEtite unpack before analysis |
| **Static analysis** | pefile, YARA | PE headers, imports/exports, entropy, packer detection, YARA hits |
| **Disassembly** | radare2 + r2pipe + r2ghidra | Function list; **C pseudocode** preferred, raw asm fallback |
| **LLM analysis** | Ollama / Claude API / Claude-Ollama | Behavior summary, MITRE ATT&CK mapping, IOC extraction, family classification |
| **Reporting** | — | `report.md` + one `.c` file per decompiled function |

Everything is saved under `reports/<sha256>/`:

```
reports/
├── index.md
└── <sha256>/
    ├── report.md          ← full threat report
    ├── vt.json            ← VirusTotal enrichment (if vt.py has been run)
    └── code/
        ├── main.c
        ├── fcn_00401000.c
        └── ...
```

---

## Requirements

| Requirement | Notes |
|-------------|-------|
| Python 3.10+ | |
| [radare2](https://github.com/radareorg/radare2) **5.8+** | Build from source — see below; apt package (5.5) is too old for r2ghidra |
| [Ollama](https://ollama.com) *(provider=ollama / claude-ollama)* | Local LLM runtime |
| [Anthropic API key](https://console.anthropic.com/) *(provider=claude)* | Set `claude.api_key` in config.yaml or `ANTHROPIC_API_KEY` env var |
| r2ghidra *(optional)* | C decompilation — `r2pm -ci r2ghidra` — strongly recommended |
| upx *(optional)* | UPX unpacking — `sudo apt install upx-ucl` |
| unipacker *(optional)* | Unpacks MPRESS, ASPack, FSG, PEtite and more — `pip install unipacker` |
| libxxhash-dev | Required to build r2ghidra — `sudo apt install libxxhash-dev` |
| ~8 GB VRAM | For `gemma4:12b` (recommended, 256K context, thinking mode) |

---

## Quickstart

### 1 — Install

```bash
git clone <repo-url> re
cd re
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### 2 — System tools

```bash
# radare2 5.8+ is required (apt ships 5.5 which is too old — build from source)
sudo apt remove -y radare2 libradare2-5.0.0t64 libradare2-dev libradare2-common 2>/dev/null || true
sudo apt install -y build-essential git meson ninja-build pkg-config \
  libcapstone-dev libssl-dev zlib1g-dev libxxhash-dev
git clone --depth=1 https://github.com/radareorg/radare2
cd radare2 && sudo ./sys/install.sh && cd ..

# r2ghidra decompiler (strongly recommended — enables C pseudocode output)
r2pm update && r2pm -ci r2ghidra

# Unpacking support (optional)
sudo apt install -y upx-ucl           # UPX unpacker
pip install unipacker                 # MPRESS, ASPack, FSG, PEtite, etc.
```

### 3 — Start Ollama and pull the model

```bash
ollama serve &
ollama pull gemma4:12b             # ~7.6 GB, 256K context, thinking mode
```

### 4 — Analyze a single sample

```bash
python main.py analyze /path/to/sample.exe
```

### 5 — Batch-analyze a folder

```bash
# Set your samples folder in config.yaml (batch.samples_dir), then:
python batch.py run

# In another terminal — web monitor with pause/resume controls:
python batch.py monitor --host 0.0.0.0 --port 7000
# open http://<host>:7000
```

### 6 — VirusTotal enrichment

```bash
cp .env.example .env
# edit .env — add your VT API key(s)

python vt.py                   # fetch VT reports for all samples
python check_reports.py        # summarise malware / benign / not-defined
```

---

## LLM providers

Three providers are supported, selected by `provider:` in `config.yaml`:

| Provider | Value | Notes |
|----------|-------|-------|
| Ollama (default) | `ollama` | Local models via Ollama native API. Needs `ollama` running. |
| Anthropic Claude | `claude` | Anthropic cloud API. Needs `ANTHROPIC_API_KEY`. |
| Claude-Ollama | `claude-ollama` | Local Ollama models via Ollama's Anthropic-compatible API — no key needed. |

**Switch to Claude API:**
```bash
# config.yaml: provider: claude
#              claude.api_key: sk-ant-...
# or:
ANTHROPIC_API_KEY=sk-ant-... python main.py analyze sample.exe
pip install anthropic   # if not already installed
```

**Switch to Claude-Ollama (local, no API key):**
```bash
# config.yaml: provider: claude-ollama
# Uses Ollama's Anthropic-compatible endpoint — same gemma4:12b model, no key needed.
# See: https://docs.ollama.com/integrations/claude-code
pip install anthropic   # SDK routes to Ollama, not Anthropic
```

---

## Single-file CLI (`main.py`)

```
python main.py [--config CONFIG] <command>

Commands:
  analyze <file>                   Analyze a single binary
  watch   <dir>                    Watch a directory — analyze new files automatically
  serve   [--host HOST] [--port]   Launch the interactive web control panel (default: 127.0.0.1:8080)
```

---

## Batch runner (`batch.py`)

For mass-analyzing a samples folder with pause/resume and remote monitoring.

```
python batch.py <command>

Commands:
  run    [--dir DIR]               Start or resume batch (dir defaults to batch.samples_dir in config.yaml)
  pause                            Signal the runner to stop after the current sample
  resume                           Clear the pause flag
  status                           Print a progress table in the terminal
  reset  <sha256> [sha256 …]       Re-queue done/failed sample(s) back to pending
  monitor [--host HOST] [--port]   Start the read-only web monitor (default: 0.0.0.0:7000)
```

**Typical workflow:**

```bash
# Terminal 1
python batch.py run

# Terminal 2 (or remote browser)
python batch.py monitor --host 0.0.0.0 --port 7000
```

The monitor dashboard shows overall progress, per-sample status, live logs, and **Pause / Resume / Reset** controls. State is written to `batch_state.json` after every pipeline stage; per-sample logs go to `logs/<sha256>.log`.

Ctrl-C in the runner terminal also pauses gracefully — the current sample finishes before stopping.

---

## VirusTotal enrichment (`vt.py`)

Fetches VirusTotal reports for all samples by SHA256 and saves them to `reports/<sha256>/vt.json`.

```bash
# Configure API keys in .env (see .env.example):
VT_KEY_1=your_key_here
VT_KEY_2=second_key_if_available   # keys are round-robin rotated

# Fetch reports for all files in samples/
python vt.py

# Fetch specific hashes
python vt.py <sha256> [sha256 …]

# Show index of already-fetched hashes
python vt.py --list
```

Keys are rotated automatically to stay within the free-tier rate limit (4 req/min per key). Multiple keys increase throughput proportionally. Already-fetched hashes are skipped; use `--force` to re-fetch.

```bash
# Summarise verdicts after fetching
python check_reports.py
# Malware     12   48.0%
# Benign       8   32.0%
# Not defined  5   20.0%
```

Pass `--threshold N` to require at least N malicious-engine detections before calling something malware (default: 1).

---

## Configuration (`config.yaml`)

```yaml
# LLM provider: "ollama" (default) | "claude" (Anthropic API) | "claude-ollama" (Ollama Anthropic-compat)
provider: ollama

ollama:
  base_url: http://localhost:11434
  model: gemma4:12b        # 256K context, thinking mode, ~7.6 GB VRAM
  chunk_size: 120000       # chars per disasm chunk (most binaries fit in one pass)
  num_ctx: 131072          # KV cache tokens — 128K is safe on 16 GB VRAM
  think: true              # chain-of-thought reasoning for deeper analysis

claude:
  api_key: ""              # or set ANTHROPIC_API_KEY env var
  model: claude-sonnet-4-6 # claude-opus-4-7 for maximum depth
  chunk_size: 180000       # 200K context window
  max_tokens: 8192
  think: false             # extended thinking (higher cost)
  think_budget_tokens: 5000

claude_ollama:             # local models via Ollama's Anthropic-compatible API
  base_url: http://localhost:11434
  api_key: ollama          # any non-empty string; Ollama ignores it
  model: gemma4:12b        # any model pulled in Ollama
  chunk_size: 120000
  max_tokens: 8192

paths:
  samples: ./samples       # watch-mode drop zone
  reports: ./reports       # output root
  rules:   ./rules         # YARA rules directory (.yar / .yara)

batch:
  samples_dir: ./samples   # directory batch.py scans (override with --dir)

analysis:
  max_functions: 30        # top N functions by size to disassemble + decompile
  min_string_len: 6
  entropy_threshold: 7.0   # sections above this are flagged as packed

web:
  backend_url: ""          # set to remote host URL for split server/browser setup
  cors_origins:
    - "*"
```

---

## YARA rules

Drop `.yar` or `.yara` files into `rules/`. They are compiled and matched during static analysis; hits are included in the report and passed to the LLM for context.

```bash
git clone https://github.com/Yara-Rules/rules rules/
```

---

## Report sections

Every `report.md` contains:

1. **File Metadata** — hashes, type, size, entropy, unpacking status
2. **PE Analysis** — sections (with entropy + packed flag), imports, exports
3. **YARA Matches** *(if rules/ populated)*
4. **Extracted Strings** — first 100 printable strings
5. **Disassembly Overview** — function table with decompilation status
6. **Behavioral Analysis** — LLM narrative
7. **MITRE ATT&CK Mapping** — technique table with justification
8. **Indicators of Compromise** — IPs, domains, registry keys, mutex names, file paths
9. **Malware Family Classification** — family, type, confidence, evidence

---

## Tuning the LLM prompts

All prompts are plain text files in `prompts/` with `{placeholder}` substitution. Edit them directly — no code changes needed.

| File | Variables |
|------|-----------|
| `behavior.txt` | `{strings}`, `{disassembly}` (C pseudocode from r2ghidra when available) |
| `mitre.txt` | `{behavior_summary}` |
| `ioc.txt` | `{strings}`, `{behavior_summary}` |
| `family.txt` | `{behavior_summary}`, `{mitre_mapping}`, `{iocs}` |

---

## Adding a custom analysis stage

1. Create `pipeline/newstage.py` with `run(sample: Sample, cfg: dict) -> Sample`
2. Add new fields to `Sample` in `pipeline/__init__.py` (keep them picklable)
3. Insert the stage in both `main.py → run_pipeline()` and `batch.py → run_sample()`
4. Add output to `pipeline/reporting.py → _render_report()`

---

## Project layout

```
re/
├── main.py                  # single-file CLI (analyze / watch / serve)
├── batch.py                 # batch runner + web monitor
├── vt.py                    # VirusTotal enrichment
├── check_reports.py         # VT verdict summary
├── config.yaml              # all tunable settings
├── .env.example             # VT API key template
├── requirements.txt
├── pipeline/
│   ├── __init__.py          # Sample dataclass
│   ├── ingestion.py         # hashing + file-type detection
│   ├── unpacking.py         # UPX / unipacker transparent unpacking
│   ├── static_analysis.py   # pefile, strings, entropy, YARA
│   ├── disassembly.py       # radare2 + r2ghidra (C pseudocode preferred over asm)
│   ├── llm_analysis.py      # multi-provider LLM: Ollama / Claude API / Claude-Ollama
│   └── reporting.py         # report.md + code/*.c output
├── prompts/                 # editable prompt templates
├── rules/                   # YARA rules (gitignored content)
├── samples/                 # drop zone (gitignored)
├── reports/                 # output (gitignored)
├── logs/                    # per-sample batch logs (gitignored)
└── web/
    ├── app.py               # FastAPI interactive control panel
    ├── queue_manager.py     # job queue, per-stage checkpointing, resume logic
    └── templates/
        └── dashboard.html
```

---

## Disclaimer

This tool is for authorized threat hunting and malware research only. Always analyze samples in an isolated environment. Never run untrusted binaries on your host system.
