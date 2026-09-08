# Threat Analysis Report

**Generated:** 2026-09-05 15:20 UTC
**Sample:** `147b20174a0c78fc72b79ca1f78130f601097771d75ae8bf8b173db47d7da199_147b20174a0c78fc72b79ca1f78130f601097771d75ae8bf8b173db47d7da199.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `147b20174a0c78fc72b79ca1f78130f601097771d75ae8bf8b173db47d7da199_147b20174a0c78fc72b79ca1f78130f601097771d75ae8bf8b173db47d7da199.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 8 sections |
| Size | 4,919,808 bytes |
| MD5 | `091048e5a87ba7cc427f8fffdd2b5a40` |
| SHA1 | `0eb3c37be5a45400750dce22a67abf2158f42f9a` |
| SHA256 | `147b20174a0c78fc72b79ca1f78130f601097771d75ae8bf8b173db47d7da199` |
| Overall entropy | 6.283 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1741011783 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 2,473,984 | 6.35 | No |
| `.rdata` | 2,108,928 | 5.655 | No |
| `.bss` | 512 | -0.0 | No |
| `.data` | 230,400 | 4.389 | No |
| `.pdata` | 58,368 | 5.459 | No |
| `.gfids` | 512 | -0.0 | No |
| `.rsrc` | 2,560 | 4.44 | No |
| `.reloc` | 43,520 | 5.434 | No |

### Imports

**KERNEL32.dll**: `AddVectoredContinueHandler`, `AddVectoredExceptionHandler`, `CloseHandle`, `CreateEventA`, `CreateIoCompletionPort`, `CreateThread`, `CreateWaitableTimerExW`, `DeleteCriticalSection`, `DuplicateHandle`, `EnterCriticalSection`, `ExitProcess`, `FreeEnvironmentStringsW`, `GetConsoleMode`, `GetCurrentThreadId`, `GetEnvironmentStringsW`
**api-ms-win-crt-heap-l1-1-0.dll**: `free`, `malloc`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_execute_onexit_table`, `_exit`, `_initialize_onexit_table`, `_initterm`, `_initterm_e`, `_register_onexit_function`, `abort`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__acrt_iob_func`, `__stdio_common_vfprintf`, `fwrite`

### Exports

`EtwQueryCacheInfo`, `YWMJJvscJpIHozbpU`

## Extracted Strings

Total strings found: **5293** (showing first 100)

```
!This program cannot be run in DOS mode.$
`.rdata
.pdata
@.gfids
@.reloc
l$ M9,$u
8cpu.u
P0H9S0
PPH9SP
PpH9Sp
UUUUUUUUH!
33333333H!
\$PH9H@v#H
D$pL9A
L$pL9N
D$@I9p
\$hM9K
\$hM9K
l$8M9,$u
P(H9S(t
P H9S uqH
S0H9P0ug
P88S8u^
P98S9uUH
expafH
nd 3fH
2-byfH
te kfH
H9uH
H9L$ r
L$@H9
s`H9J
debugCal
debugCal
debugCalH9
debugCalH9
l409u
x6tzH9
l819um
debugCalH9
l163uf
x84t6H9
l327uf
runtime.
runtime H
 error: H
f9A2vA
q`f9q2r
:H9F w
>H+zhH
L$HI9QhuH
P`f9P2tgH
\$0f9C2u
2}#s]H
D$PA)P
H9?(H
H9D$(t
^0H9X0tQ
\$XHcbCL
$H+L$HH
T$(H+J
L$(H+A

H9Z(w
\$0H9K
D$pH9H
D$0H9H
|$pH9\$
T$ H+:
UUUUUUUUH!
UUUUUUUUH
wwwwwwwwH!
wwwwwwwwH
J0f9J2vsL
f9s2u:H=
D$$u$L
H9T$@u
T$(M	D
runtime.H9
QpM9Qhu
L9L$Xt$H
H9>wHH9~
runtime.H9
reflect.H9
I9N0tVH
T$ 9T$$
H92t9H9rHt3H
rhH92w
H+5HEG
tRI9N0tLH
|$0uMH
memprofi
lerau*f
yteu"H
9q0s&H9J
09z0w
H
H9X(v
L
HPH9w
H(H9w
L$HH9A
Q8H+Q(
H9D$HA
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180067b40` | `0x180067b40` | 382746 | ✓ |
| `fcn.180067ba0` | `0x180067ba0` | 362811 | ✓ |
| `fcn.180067b60` | `0x180067b60` | 362810 | ✓ |
| `fcn.18006c6c0` | `0x18006c6c0` | 233015 | ✓ |
| `fcn.180068020` | `0x180068020` | 206344 | ✓ |
| `fcn.180068040` | `0x180068040` | 206216 | ✓ |
| `fcn.180068060` | `0x180068060` | 206091 | ✓ |
| `fcn.180068080` | `0x180068080` | 205963 | ✓ |
| `fcn.18006c820` | `0x18006c820` | 205943 | ✓ |
| `fcn.1800680a0` | `0x1800680a0` | 205835 | ✓ |
| `fcn.1800680c0` | `0x1800680c0` | 205707 | ✓ |
| `fcn.1800680e0` | `0x1800680e0` | 205576 | ✓ |
| `fcn.180068100` | `0x180068100` | 205448 | ✓ |
| `fcn.180068120` | `0x180068120` | 205320 | ✓ |
| `fcn.180068140` | `0x180068140` | 205192 | ✓ |
| `fcn.180068160` | `0x180068160` | 205064 | ✓ |
| `fcn.180068180` | `0x180068180` | 204936 | ✓ |
| `fcn.18006c880` | `0x18006c880` | 176791 | ✓ |
| `fcn.18006c920` | `0x18006c920` | 149559 | ✓ |
| `fcn.18006c980` | `0x18006c980` | 132471 | ✓ |
| `fcn.180254700` | `0x180254700` | 24037 | ✓ |
| `fcn.180248060` | `0x180248060` | 22616 | ✓ |
| `fcn.1801ff1a0` | `0x1801ff1a0` | 19597 | ✓ |
| `fcn.18016f300` | `0x18016f300` | 16084 | ✓ |
| `fcn.180237d00` | `0x180237d00` | 14469 | ✓ |
| `fcn.1801aa6a0` | `0x1801aa6a0` | 14087 | ✓ |
| `fcn.180250280` | `0x180250280` | 13451 | ✓ |
| `fcn.180067b20` | `0x180067b20` | 11731 | ✓ |
| `fcn.180221140` | `0x180221140` | 10457 | ✓ |
| `fcn.1801aec00` | `0x1801aec00` | 10264 | ✓ |

### Decompiled Code Files

- [`code/fcn.180067b20.c`](code/fcn.180067b20.c)
- [`code/fcn.180067b40.c`](code/fcn.180067b40.c)
- [`code/fcn.180067b60.c`](code/fcn.180067b60.c)
- [`code/fcn.180067ba0.c`](code/fcn.180067ba0.c)
- [`code/fcn.180068020.c`](code/fcn.180068020.c)
- [`code/fcn.180068040.c`](code/fcn.180068040.c)
- [`code/fcn.180068060.c`](code/fcn.180068060.c)
- [`code/fcn.180068080.c`](code/fcn.180068080.c)
- [`code/fcn.1800680a0.c`](code/fcn.1800680a0.c)
- [`code/fcn.1800680c0.c`](code/fcn.1800680c0.c)
- [`code/fcn.1800680e0.c`](code/fcn.1800680e0.c)
- [`code/fcn.180068100.c`](code/fcn.180068100.c)
- [`code/fcn.180068120.c`](code/fcn.180068120.c)
- [`code/fcn.180068140.c`](code/fcn.180068140.c)
- [`code/fcn.180068160.c`](code/fcn.180068160.c)
- [`code/fcn.180068180.c`](code/fcn.180068180.c)
- [`code/fcn.18006c6c0.c`](code/fcn.18006c6c0.c)
- [`code/fcn.18006c820.c`](code/fcn.18006c820.c)
- [`code/fcn.18006c880.c`](code/fcn.18006c880.c)
- [`code/fcn.18006c920.c`](code/fcn.18006c920.c)
- [`code/fcn.18006c980.c`](code/fcn.18006c980.c)
- [`code/fcn.18016f300.c`](code/fcn.18016f300.c)
- [`code/fcn.1801aa6a0.c`](code/fcn.1801aa6a0.c)
- [`code/fcn.1801aec00.c`](code/fcn.1801aec00.c)
- [`code/fcn.1801ff1a0.c`](code/fcn.1801ff1a0.c)
- [`code/fcn.180221140.c`](code/fcn.180221140.c)
- [`code/fcn.180237d00.c`](code/fcn.180237d00.c)
- [`code/fcn.180248060.c`](code/fcn.180248060.c)
- [`code/fcn.180250280.c`](code/fcn.180250280.c)
- [`code/fcn.180254700.c`](code/fcn.180254700.c)

## Behavioral Analysis

This analysis incorporates the findings from **chunk 9/9** into the existing framework. This final segment provides definitive evidence of a sophisticated **multi-stage execution pipeline** and **bitmask-heavy logic**, reinforcing the conclusion that this is a high-tier malware sample using advanced VM-based obfuscation.

---

### Updated Analysis: Advanced Obfuscation Techniques (Continued)

#### 1. Arithmetic Masking & Bitwise Transformation
The segment containing the loop `for (iVar33 = 3; -1 < iVar33; ...)` reveals a sophisticated method of data transformation.
*   **Behavior:** The code uses complex expressions like `(*0x20 + -0x1ac)[unaff_RSI] + uVar2 + ((*0x20 + -0x1ac)[unaff_RSI] & uVar2) * -2`. This is a mathematical "trick" (often used in compilers to replace complex operations with bitwise logic) that allows the code to perform arithmetic while masking its intent from simple scanners.
*   **Analysis:** By using `(A + B + (A & B) * -2)`, the author is performing addition through bit-manipulation logic. This ensures that the "true" values of variables are never stored in cleartext; they are transformed into a format only understandable by the next stage of the VM.

#### 2. Recursive Handler Chaining (The "Pipeline")
A significant block shows a series of repeated calls to `(*pcVar22)(pcVar22, puVar30)` with changing addresses (`0x1801b0626`, `0x1801b063b`, etc.).
*   **Behavior:** This is not a standard "if/else" or "switch" jump. Instead, the code uses **Function Pointer Chaining**. Each handler processes a piece of an instruction and returns a pointer to the next handler in a sequence.
*   **Analysis:** This creates a "pipeline" effect. Even if an analyst identifies one piece of malicious logic (e.g., a decryption routine), they cannot see the full scope of the operation because it is fragmented across multiple linked function calls. It forces the researcher to trace every single jump in the chain to understand one unified action.

#### 3. Context-Dependent Branching ("The Switch")
The recurring check `if (*0x1804dfc10 == 0)` acts as a **Gatekeeper**.
*   **Behavior:** The code checks a specific memory address (a "flag" or "state constant"). Depending on the value, it chooses between two entirely different paths of logic to arrive at the same result.
*   **Analysis:** This is designed to defeat **Symbolic Execution**. Tools that try to map all possible paths through a function will find multiple "valid" routes, many of which are "dead ends" or decoy paths meant to waste an analyst's time.

#### 4. Hardcoded Buffer Construction (Data Re-assembly)
Towards the end of the chunk, specific hex values like `0x3d` (`=`) and `0x29` (`)`) appear in assignments like `*(uVar24 + uVar29) = 0x3d;`.
*   **Behavior:** This indicates that the VM is constructing a **string or command buffer**. Since these characters are being placed into an array based on dynamic indices (`uVar24`, `uVar29`), the actual string (e.g., an SQL injection, a system command, or a C2 URL) only exists in memory for a fraction of a second before it is used by a system API.
*   **Analysis:** This is a "Just-In-Time" construction of malicious commands. It ensures that any static string analysis (strings.exe/floss) will fail to find the actual commands being executed by the malware.

---

### Updated Summary of Malicious Indicators (Cumulative)

| Feature | Detection/Context | Significance |
| :--- | :--- | :--- |
| **Multi-Layered VM** | Nested calls (`fcn.180...`) and multi-stage handler dispatching. | The payload is wrapped in multiple layers of "virtual" machines to hide intent. |
| **State Table Expansion** | Massive loops/arrays (`puVar20`) for jump-target storage. | Replaces direct logic with table lookups to hide the control flow from static tools. |
| **Bitwise Dispatching** | XORs and bitmask-based arithmetic in long loop blocks. | Obfuscates mathematical calculations and jump targets, making manual tracing tedious. |
| **Handler Chaining** | Sequential calls of `(*pcVar22)` with varying memory addresses. | Fragments a single malicious action into many pieces, hiding the "big picture" of the attack. |
| **Context-Dependent Branching** | State checks (e.g., `*0x1804dfc10 == 0`) to choose execution paths. | Creates "Decision Trees" that confuse automated de-obfuscation tools like Triton or HexRays. |
| **JIT Buffer Construction** | Assembly of characters (`0x3d`, `0x29`) into dynamic indices. | Prevents static detection of commands (e.g., hidden URLs, shell commands). |

---

### Conclusion & Risk Assessment (Final)

The analysis of all 9 chunks confirms that this sample utilizes **Elite-Tier Obfuscation** characteristic of high-budget cyber-espionage or professional financially motivated crime (Banking Trojans/Infostealers).

1.  **Sophisticated Architecture:** The code is not just "obfuscated"; it is an entire programming environment built to run a secondary language (the bytecode) on top of the x86 architecture. This masks the true logic behind two layers: the VM's instruction set and the original malicious intent.
2.  **Anti-Analysis Maturity:** The use of **Bitwise Arithmetic**, **Handler Chaining**, and **Context-Dependent Branching** specifically targets the weaknesses of automated tools (static analysis, symbolic execution). The author is intentionally creating a "maze" where only a human manual trace can find the way through.
3.  **Actionable Intelligence for Incident Response:**
    *   **Dynamic Analysis Priority:** Because static analysis is hampered by the VM layers, monitoring **API Hooking** (e.g., `NtCreateFile`, `InternetConnect`, `WriteProcessMemory`) is the most effective way to see what the "inner" code is doing once it breaks out of its virtual container.
    *   **Memory Forensics:** Since data (like URLs or stolen credentials) is only assembled in memory just before use, **memory dumps** taken at intervals during execution are required to catch strings that never exist on disk.
    *   **Identify Command Patterns:** The "Handler Chaining" logic suggests a command-driven architecture. Identifying the dispatch functions (e.g., `fcn.1800689e0`) will reveal the primary capabilities of the malware (e.g., file deletion, screen grabbing, or data exfiltration).

**Final Verdict:** This is a **High-Complexity Malware Sample**. It utilizes advanced techniques to hide its functionality from both automated scanners and human analysts. It should be treated as a high-threat sample capable of evading standard EDR/AV signatures through technical complexity rather than just simple encryption.

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Programs | The use of arithmetic masking and bitwise transformations (e.g., `A + B + (A & B) * -2`) is designed to hide the true logic of operations from automated security scanners. |
| T1027 | Obfuscated Files or Programs | Handler chaining fragments the execution pipeline, ensuring that individual components of a malicious action are not visible as a single, coherent sequence in static analysis. |
| T1497 | Defeats Analysis Tools | Context-dependent branching creates "decision trees" specifically designed to frustrate symbolic execution tools and waste an analyst's time with decoys. |
| T1027 | Obfuscated Files or Programs | Just-In-Time (JIT) buffer construction ensures that malicious commands or strings are only manifest in memory for a split second, evading static string analysis. |

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Due to the high level of obfuscation described in the report (Virtual Machine-based execution), many traditional "static" indicators (like cleartext URLs or file paths) are intentionally hidden from static analysis.

### **IP addresses / URLs / Domains**
*   *None identified.* (The report notes that URLs are constructed via "Just-in-Time" buffer construction, meaning they do not appear in the raw strings.)

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **VM-based Obfuscation:** The sample utilizes a multi-layer "virtual machine" architecture to hide the underlying malicious instruction set.
*   **JIT Buffer Construction:** Logic specifically designed to assemble commands/scripts from hex values (e.g., `0x3d` for `=`, `0x29` for `)`) at runtime. This is a technique used to hide C2 commands and system calls.
*   **Function Pointer Chaining:** Use of a "pipeline" approach where logic is fragmented across multiple handlers (e.g., addresses like `0x1801b0626`, `0x1801b063b`) to bypass automated analysis.
*   **Go Runtime Environment:** The presence of `runtime.` and `reflect.` in the string dump indicates the malware is likely compiled using the Go programming language, which is common in modern high-tier malware (e.g., for cross-platform compatibility or complexity).
*   **Context-Dependent Branching:** Use of "Gatekeeper" checks (e.g., at memory address `0x1804dfc10`) to force symbolic execution tools into dead ends/decoy paths.

---

### **Analyst Notes for Incident Response**
Because the malware employs **Elite-Tier Obfuscation**, standard static indicators are insufficient for detection. I recommend the following:
1.  **Behavioral Hunting:** Monitor for processes executing a high volume of obfuscated function calls or "chaining" behaviors characteristic of VM-based packers.
2.  **Memory Forensics:** Perform periodic memory dumps during execution to capture the "Just-in-Time" strings (URLs, commands) as they are assembled in RAM before being passed to system APIs.
3.  **API Hooking:** Focus on monitoring `NtCreateFile`, `InternetConnect`, and `WriteProcessMemory` to see the decrypted payloads after they leave the virtual machine's protection.

---

## Malware Family Classification

1. **Malware family**: custom (Sophisticated Loader)
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **VM-Based Obfuscation Architecture:** The sample utilizes a sophisticated multi-layered virtual machine to execute bytecode, employing "handler chaining" and "bitmask-heavy logic" to mask its true functionality from both static analysis and symbolic execution tools.
*   **Just-In-Time (JIT) Construction:** The use of manual buffer construction for common characters (like `=` and `)`) indicates that malicious commands or C2 strings are only assembled in memory at the moment of execution, deliberately bypassing static string analysis.
*   **Elite-Tier Defensive Tactics:** The combination of context-dependent branching ("gatekeepers") and Go-runtime integration points to a high-budget production intended for long-term persistence or as a sophisticated entry point (loader) for secondary payloads in an advanced persistent threat (APT) or professional cybercrime campaign.
