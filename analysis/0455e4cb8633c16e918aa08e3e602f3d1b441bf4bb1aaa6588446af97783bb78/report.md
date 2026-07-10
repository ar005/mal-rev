# Threat Analysis Report

**Generated:** 2026-07-10 00:33 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 3 sections |
| Size | 522,240 bytes |
| MD5 | `7fe7e8c3b5ffa8a69ece38196ee3f7d1` |
| SHA1 | `d298f44293f9b074a379465aae0c5ae01716dcb4` |
| SHA256 | `0455e4cb8633c16e918aa08e3e602f3d1b441bf4bb1aaa6588446af97783bb78` |
| Overall entropy | 7.058 |
| Unpacked | ✓ Yes (tool: upx) |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774631878 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 379,392 | 6.356 | No |
| `.rdata` | 271,872 | 6.212 | No |
| `.data` | 169,984 | 7.776 | ⚠️ Yes |
| `.pdata` | 18,944 | 5.432 | No |
| `.reloc` | 6,144 | 5.411 | No |

### Imports

**KERNEL32.DLL**: `GetProcessHeap`, `GetLastError`, `Sleep`, `ExitProcess`, `GetLocaleInfoA`, `FlushFileBuffers`, `GetSystemDirectoryA`, `SetEvent`, `GetVersionExW`, `GetComputerNameW`, `CreateFileMappingA`, `LocalFree`, `SetFilePointerEx`, `VirtualProtect`, `QueryPerformanceCounter`
**ADVAPI32.dll**: `GetUserNameA`, `RegQueryValueExA`, `RegCloseKey`, `RegOpenKeyExA`
**SHELL32.dll**: `CommandLineToArgvW`, `SHGetFolderPathA`
**USER32.dll**: `GetWindowTextA`, `GetDesktopWindow`, `wsprintfA`, `MessageBoxA`

### Exports

`BandSlab`, `Bind_Set_lift`, `Bindtestjoin`, `Coreupdate`, `Gate_Task_Band`, `HookNest`, `InitWipe`, `InitspanFold`, `PullClose`, `Push_Wipe`, `RiftSwapSeek`, `Send_quad`, `Slab_flux_Clip`, `Span_Hike`, `Trapset`, `Wipe_recv`, `WriteCloseParse`

## Extracted Strings

Total strings found: **3976** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.reloc
x UATAUAVAWH
A_A^A]A\]
@USVAVAWH
A_A^^[]
D$0Lh[
D$0Y;|
D$05|
D$01?#
D$0$q,?
D$03EnY
D$0et.
D$0Qx=
D$0xM
X
D$01]C
s WATAUAVAWH
A_A^A]A\_
UVWAVAWH
D8|$@t)H
A_A^_^]
UVWATAUAVAWH
A_A^A]A\_^]
x UATAUAVAWH
A_A^A]A\]
@SWATAVAWH
A_A^A\_[
A_A^A\_[
WAVAWH
UVWATAUAVAWH
D8/t'L
A_A^A]A\_^]
x UAUAVH
D$0<koR
D$0O2I_
D$0yq4{
@UVAVAWH
A_A^^]
EgH9uov%L
A_A^^]
UATAUAVI
A^A]A\]
A^A]A\]
USVWAVH
Hc\$PH
|$@IcF
A^_^[]
A^_^[]
s WATAUAVAWH
A_A^A]A\_
@SUVWAUAVAWH
A_A^A]_^][
USVWAUAVAWH
A_A^A]_^[]
UVWATAUAVAWH
A_A^A]A\_^]
D$0!5F
UVWATAUAVAWH
A_A^A]A\_^]
D$0jE3
D$0#k}

D$0^+^
D$(rt
@SVWATAVAWH
A_A^A\_^[
A_A^A\_^[
UVWATAUAVAWH
A_A^A]A\_^]
s WATAUAVAWH
A_A^A]A\_
D$0na6(
D$08H
UWATAUAWH
D$0Fp 
@8;tAL
A_A]A\_]
HcD$8H
UWATAVAWH
LcT$@L
A_A^A\_]
@UATAVAWH
A_A^A\]
A_A^A\]
USVWATAUAVAWH
A_A^A]A\_^[]
D$=+L;
UATAVH
EH<Q'`
D$0WMN
D$PH95
|$ AVH
UVWATAUAVAWH
A_A^A]A\_^]
D$0HHa
D$0bvID
D$0Gh(
USVWAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.5700226f4` | `0x5700226f4` | 4323 | ✓ |
| `fcn.570018890` | `0x570018890` | 3107 | ✓ |
| `fcn.570045000` | `0x570045000` | 3048 | ✓ |
| `fcn.57002f510` | `0x57002f510` | 2623 | ✓ |
| `fcn.57001da48` | `0x57001da48` | 2502 | ✓ |
| `fcn.570027e48` | `0x570027e48` | 1989 | ✓ |
| `fcn.570025c00` | `0x570025c00` | 1857 | ✓ |
| `fcn.570031e70` | `0x570031e70` | 1692 | ✓ |
| `fcn.57001e410` | `0x57001e410` | 1690 | ✓ |
| `fcn.570017bb4` | `0x570017bb4` | 1559 | ✓ |
| `fcn.570027870` | `0x570027870` | 1496 | ✓ |
| `fcn.570025170` | `0x570025170` | 1468 | ✓ |
| `fcn.57001556c` | `0x57001556c` | 1413 | ✓ |
| `fcn.570048f40` | `0x570048f40` | 1384 | ✓ |
| `fcn.57005ab84` | `0x57005ab84` | 1359 | ✓ |
| `fcn.57002091c` | `0x57002091c` | 1355 | ✓ |
| `fcn.57002e728` | `0x57002e728` | 1351 | ✓ |
| `fcn.570030da4` | `0x570030da4` | 1335 | ✓ |
| `fcn.5700172c0` | `0x5700172c0` | 1305 | ✓ |
| `fcn.57002bce4` | `0x57002bce4` | 1290 | ✓ |
| `fcn.57001d4e0` | `0x57001d4e0` | 1254 | ✓ |
| `fcn.57005d230` | `0x57005d230` | 1227 | ✓ |
| `fcn.57001f388` | `0x57001f388` | 1185 | ✓ |
| `fcn.570006400` | `0x570006400` | 1161 | ✓ |
| `fcn.570014a2c` | `0x570014a2c` | 1093 | ✓ |
| `fcn.57000b100` | `0x57000b100` | 1074 | ✓ |
| `fcn.57000bde8` | `0x57000bde8` | 1071 | ✓ |
| `fcn.570007e0c` | `0x570007e0c` | 1041 | ✓ |
| `fcn.5700139bc` | `0x5700139bc` | 1024 | ✓ |
| `fcn.5700099bc` | `0x5700099bc` | 1007 | ✓ |

### Decompiled Code Files

- [`code/fcn.570006400.c`](code/fcn.570006400.c)
- [`code/fcn.570007e0c.c`](code/fcn.570007e0c.c)
- [`code/fcn.5700099bc.c`](code/fcn.5700099bc.c)
- [`code/fcn.57000b100.c`](code/fcn.57000b100.c)
- [`code/fcn.57000bde8.c`](code/fcn.57000bde8.c)
- [`code/fcn.5700139bc.c`](code/fcn.5700139bc.c)
- [`code/fcn.570014a2c.c`](code/fcn.570014a2c.c)
- [`code/fcn.57001556c.c`](code/fcn.57001556c.c)
- [`code/fcn.5700172c0.c`](code/fcn.5700172c0.c)
- [`code/fcn.570017bb4.c`](code/fcn.570017bb4.c)
- [`code/fcn.570018890.c`](code/fcn.570018890.c)
- [`code/fcn.57001d4e0.c`](code/fcn.57001d4e0.c)
- [`code/fcn.57001da48.c`](code/fcn.57001da48.c)
- [`code/fcn.57001e410.c`](code/fcn.57001e410.c)
- [`code/fcn.57001f388.c`](code/fcn.57001f388.c)
- [`code/fcn.57002091c.c`](code/fcn.57002091c.c)
- [`code/fcn.5700226f4.c`](code/fcn.5700226f4.c)
- [`code/fcn.570025170.c`](code/fcn.570025170.c)
- [`code/fcn.570025c00.c`](code/fcn.570025c00.c)
- [`code/fcn.570027870.c`](code/fcn.570027870.c)
- [`code/fcn.570027e48.c`](code/fcn.570027e48.c)
- [`code/fcn.57002bce4.c`](code/fcn.57002bce4.c)
- [`code/fcn.57002e728.c`](code/fcn.57002e728.c)
- [`code/fcn.57002f510.c`](code/fcn.57002f510.c)
- [`code/fcn.570030da4.c`](code/fcn.570030da4.c)
- [`code/fcn.570031e70.c`](code/fcn.570031e70.c)
- [`code/fcn.570045000.c`](code/fcn.570045000.c)
- [`code/fcn.570048f40.c`](code/fcn.570048f40.c)
- [`code/fcn.57005ab84.c`](code/fcn.57005ab84.c)
- [`code/fcn.57005d230.c`](code/fcn.57005d230.c)

## Behavioral Analysis

This final analysis incorporates the findings from chunk 3/3, completing the overall picture of the malware's architecture and capabilities.

### Final Analysis Summary

The inclusion of these final functions provides the "missing pieces" regarding how the malware protects itself and manages its internal state machine. It is now confirmed that this is a **high-sophistication Trojan or Modular Loader** designed for long-term persistence and multi-functional execution. The malware doesn't just perform one malicious act; it builds an internal roadmap of "capabilities" and executes them based on environment checks and configuration data.

---

### Final Technical Observations & Analysis

#### 1. Advanced Anti-Analysis (Timing Checks)
The function `fcn.5700099bc` is a textbook example of **anti-debugging/anti-VM techniques**.
*   **RDTSC Manipulation:** The use of the `rdtsc` instruction multiple times, followed by complex arithmetic involving large constants (e.g., `0x5197f7d73404147`), is designed to detect timing discrepancies caused by debuggers or virtualized environments.
*   **Purpose:** If the execution time between two points deviates from a calculated threshold, the malware likely halts or changes its behavior to "safe" mode to avoid detection by automated sandboxes.

#### 2. Indirect Function Calls & Jump Tables (Modular Execution)
The code in `bp_20h` and `fcn.57000b100` heavily utilizes **indirect function pointers** (e.g., `**0x570529e08`).
*   Instead of calling functions directly, the malware retrieves a pointer from a table or a memory location populated during the "unpacking" phase. 
*   This allows the malware to be highly modular: it can receive different commands from its C2 and use the same primary loop to jump to different functional modules (e.g., one "module" for keylogging, another for file encryption).

#### 3. Complex State Machine & Decision Trees
`fcn.57000b100` demonstrates a clear **decision-tree logic**. The malware performs several internal checks (functions like `57001aca0`, `570024898`) and uses the results to determine which branch of code to execute next. This indicates that the malware is "aware" of its environment and only activates specific features if certain conditions are met.

#### 4. Recursive Search & Data Processing
The functions `fcn.57000bde8` and `fcn.570007e0c` suggest advanced **file system or registry interaction**.
*   **Length-Prefixed Strings:** The code manages complex string buffers, checking for lengths and iterating through data blocks. 
*   **Recursion/Iteration:** The logic in `fcn.570007e0c` indicates it may be searching for files or keys recursively (or iterating through a list of potentially hidden paths), which is common in ransomware or "stealer" components to find sensitive documents.

#### 5. Complex Buffer Management
Function `fcn.5700139bc` shows sophisticated handling of **multi-layered data structures**. It uses bit-shifting and mask operations (e.g., `>> 0x1f & 0x3ffU`) to calculate indices within a memory buffer. This is typically seen when parsing complex network packets or custom encrypted configuration blobs where different fields have variable lengths.

---

### Final Risk Assessment & Behavior Profile

*   **Sophisticated "Loader" Capability:** The malware acts as a "dispatcher." It loads its core functionality into memory and then uses an internal logic gate to decide which specific malicious actions to perform based on the victim's machine profile.
*   **Advanced Evasion Tactics:** By using `rdtsc` timing checks, indirect calls (to hide its API call graph), and multi-part string construction, it is specifically designed to bypass **heuristic analysis** and **manual reverse engineering**.
*   **Modular Payloads:** The evidence of "modules" suggests the malware can be updated via C2. A single infection could lead to different outcomes (e.g., some users getting a crypto-miner, others being used for credential theft) depending on how the server configures the malicious "payload" modules.
*   **Persistence & Persistence Awareness:** The complex logic in `fcn.570007e0c` suggests it is prepared to scan the system for and interact with sensitive files/paths, potentially looking for high-value targets (spreadsheets, saved passwords, etc.).

### Conclusion Update
The analysis confirms this sample is a **high-tier threat actor tool**. It exhibits characteristics of a "Backdoor" or "Trojan" used in targeted attacks. Its complexity suggests it is likely part of a professional malware family where the primary purpose is to establish a stable, hard-to-detect foothold on a system before deploying specific modules as directed by the attacker.

**Key Indicators of Concern:**
*   **Anti-Analysis Guards:** Active use of `rdtsc` and obfuscated jumps to evade security tools.
*   **Modular Architecture:** Ability to swap malicious behaviors at runtime via a "dispatcher" logic.
*   **Complex Configuration Parsing:** Evidence of a layered communication/configuration system to stay hidden from simple string analysis.
*   **Data Scraping Capabilities:** Advanced loops for searching and processing data within the file system or memory.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtualization/Sandbox Evasion | The use of `rdtsc` instructions and timing analysis is a classic method used to detect and bypass automated sandboxes or debugger environments. |
| T1568 | Dynamic Resolution | The implementation of indirect function calls and jump tables prevents static analysis tools from automatically mapping the execution flow and capabilities. |
| T1497 | Virtualization/Sandbox Evasion | The use of decision trees to only activate specific "modules" based on environmental checks is a tactic used to hide malicious behavior from automated security scanners. |
| T1083 | File and Directory Discovery | The presence of recursive search logic indicates the malware's capability to scout for high-value targets like documents or credentials within the file system. |
| T1568 | Dynamic Resolution | Complex bit-shifting and mask operations used to parse configuration blobs allow the malware to resolve its specific behavior and parameters only at runtime. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the categorized list of Indicators of Compromise (IOCs). 

*Note: The "Strings" section contains significant amounts of obfuscated data/garbage characters typically seen in packed executables; these were filtered out as they do not represent actionable indicators.*

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (The behavioral analysis mentions the *capability* to search for files and registry keys, but no specific paths or keys were disclosed).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified. (Note: The values such as `0x5700...` are memory addresses/offsets, not file hashes).

### **Other artifacts**
*   **Anti-Analysis Constants:** `0x5197f7d73404147` (Used in complex arithmetic for `rdtsc` timing checks).
*   **Behavioral Signatures:**
    *   Use of `rdtsc` instruction to detect debugger/VM environments.
    *   Indirect function pointer calls (e.g., `**0x570529e08`) used to hide the API call graph and facilitate modular execution.
    *   Bit-shifting/masking logic for buffer indexing: `>> 0x1f & 0x3ffU`.
*   **Internal Function Identifiers (Behavioral Mapping):**
    *   `fcn.5700099bc` (Timing check logic)
    *   `fcn.57000b100` (Decision-tree/Dispatch logic)
    *   `fcn.57000bde8` (Data processing/File system interaction)
    *   `fcn.570007e0c` (Search/Iteration of file paths or registry keys)
    *   `fcn.5700139bc` (Multi-layered buffer parsing)

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Anti-Analysis Evasion:** The use of `rdtsc` timing checks and complex decision-tree logic indicates a high level of sophistication designed to detect sandboxes/debuggers and only execute malicious "modules" when specific environment conditions are met.
*   **Modular Dispatcher Architecture:** The reliance on indirect function pointers, jump tables, and multi-layered buffer parsing identifies the sample as a modular loader (or "backdoor") that acts as a host for various secondary payloads rather than being a single-purpose tool.
*   **Persistence and Information Gathering:** The inclusion of recursive search logic and complex data processing routines suggests the malware is designed for long-term residency, with capabilities to crawl the file system or registry for high-value targets (e.g., credentials or sensitive documents).
