# Threat Analysis Report

**Generated:** 2026-07-22 14:33 UTC
**Sample:** `0992a2d2f68b550a9d2c261aceece823810a184f6c599190f6382c1099dca99d_0992a2d2f68b550a9d2c261aceece823810a184f6c599190f6382c1099dca99d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0992a2d2f68b550a9d2c261aceece823810a184f6c599190f6382c1099dca99d_0992a2d2f68b550a9d2c261aceece823810a184f6c599190f6382c1099dca99d.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 2,839,552 bytes |
| MD5 | `24b4096627c8c94c23857dcad98674d4` |
| SHA1 | `f5299e11c85b1a5d14e7c1285485025fbe688529` |
| SHA256 | `0992a2d2f68b550a9d2c261aceece823810a184f6c599190f6382c1099dca99d` |
| Overall entropy | 6.891 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768555937 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 194,560 | 6.459 | No |
| `.rdata` | 84,992 | 5.177 | No |
| `.data` | 5,120 | 2.876 | No |
| `.pdata` | 10,752 | 5.401 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 2,540,032 | 6.89 | No |
| `.reloc` | 2,560 | 5.414 | No |

### Imports

**SHELL32.dll**: `ShellExecuteExW`, `SHGetKnownFolderPath`, `ord_680`, `ShellExecuteA`
**ole32.dll**: `CoInitialize`, `CoTaskMemFree`, `CoUninitialize`
**KERNEL32.dll**: `WriteConsoleW`, `HeapSize`, `GetProcessHeap`, `SetStdHandle`, `FreeEnvironmentStringsW`, `GetEnvironmentStringsW`, `GetCommandLineW`, `CreateFileA`, `WriteFile`, `CloseHandle`, `GetLastError`, `Sleep`, `CreateProcessA`, `GetSystemDirectoryA`, `GetModuleFileNameW`

## Extracted Strings

Total strings found: **80357** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
WATAUAVAWH
A_A^A]A\_
WATAUAVAWH
A_A^A]A\_
@SUVWAVAWH
gfffffffI
HA_A^_^][
|$0t&H
HA_A^_^][
@SUVAVH
(A^^][
(A^^][
UVWATAUAVAWH
C@H98t$H
L+l$8tVf
C@L98t$H
A_A^A]A\_^]
WATAUAVAWH
A_A^A]A\_
\$ UVAVH
@SVAUAVH
(A^A]^[
l$ WAVAWH
 A_A^_
@SVATAVH
(A^A\^[
@SVAUAVH
(A^A]^[
\$ UVWH
\$ UVWH
\$ UVWH
@SVWAVH
(A^_^[
(A^_^[
@SUVWAVH
 A^_^][
 A^_^][
@SUVWH
\$ UVWAVAWH
A_A^_^]
gfffffffH
VWATAVAWH
A_A^A\_^
VWATAVAWH
A_A^A\_^
VWATAVAWH
A_A^A\_^
@SUVWH
fffffff
gfffffffI
@USVWAVAWH
A_A^_^[]
@USVWAVAWH
A_A^_^[]
UVWAVAWH
A_A^_^]
UVWATAUAVAWH
C@H98t$H
C@L90t$H
A_A^A]A\_^]
UVWAVAWH
A_A^_^]
USVWATAUAVAWH
A_A^A]A\_^[]
UWATAVAWH
L$(H+L$ I
gfffffffI
A_A^A\_]
UWATAVAWH
L$HH+L$@I
gfffffffI
L$0H+L$(I
A_A^A\_]
t$ UWAUAVAWH
A_A^A]_]
UVWATAUAVAWH
A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
SUVWATAUAVAWH
A_A^A]A\_^][
@USVWATAUAVAWH
A_A^A]A\_^[]
\$ VATAWH
 A_A\^
UWAUAVAWH
A_A^A]_]
L$ SUVWH
fB9<H}
l$ VWAVH
t$ UWATAVAWH
A_A^A\_]
\$ UVWH
WATAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14001d7a8` | `0x14001d7a8` | 53803 | ✓ |
| `fcn.14001d794` | `0x14001d794` | 53762 | ✓ |
| `fcn.14000c3cc` | `0x14000c3cc` | 47238 | ✓ |
| `fcn.140025ea0` | `0x140025ea0` | 19273 | ✓ |
| `fcn.14000c714` | `0x14000c714` | 18474 | ✓ |
| `fcn.14000c290` | `0x14000c290` | 6661 | ✓ |
| `fcn.14002aeb4` | `0x14002aeb4` | 4735 | ✓ |
| `fcn.14002d630` | `0x14002d630` | 3559 | ✓ |
| `fcn.1400062c0` | `0x1400062c0` | 3545 | ✓ |
| `fcn.1400076e0` | `0x1400076e0` | 2957 | ✓ |
| `fcn.14000b6c0` | `0x14000b6c0` | 2490 | ✓ |
| `fcn.14000f348` | `0x14000f348` | 2349 | ✓ |
| `fcn.140009bd0` | `0x140009bd0` | 2222 | ✓ |
| `fcn.14000f470` | `0x14000f470` | 2064 | ✓ |
| `fcn.14001d7e0` | `0x14001d7e0` | 1946 | ✓ |
| `fcn.140026ce4` | `0x140026ce4` | 1829 | ✓ |
| `fcn.140001e50` | `0x140001e50` | 1703 | ✓ |
| `fcn.14002eb10` | `0x14002eb10` | 1677 | ✓ |
| `fcn.1400070a0` | `0x1400070a0` | 1598 | ✓ |
| `fcn.140005680` | `0x140005680` | 1571 | ✓ |
| `fcn.14002d700` | `0x14002d700` | 1451 | ✓ |
| `fcn.14001214c` | `0x14001214c` | 1312 | ✓ |
| `fcn.1400132ec` | `0x1400132ec` | 1229 | ✓ |
| `fcn.140011c8c` | `0x140011c8c` | 1213 | ✓ |
| `fcn.1400239a4` | `0x1400239a4` | 1171 | ✓ |
| `fcn.14001a180` | `0x14001a180` | 1164 | ✓ |
| `fcn.14001bfdc` | `0x14001bfdc` | 1153 | ✓ |
| `fcn.140015ef8` | `0x140015ef8` | 1133 | ✓ |
| `fcn.1400255c0` | `0x1400255c0` | 1119 | ✓ |
| `fcn.140008270` | `0x140008270` | 1002 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001e50.c`](code/fcn.140001e50.c)
- [`code/fcn.140005680.c`](code/fcn.140005680.c)
- [`code/fcn.1400062c0.c`](code/fcn.1400062c0.c)
- [`code/fcn.1400070a0.c`](code/fcn.1400070a0.c)
- [`code/fcn.1400076e0.c`](code/fcn.1400076e0.c)
- [`code/fcn.140008270.c`](code/fcn.140008270.c)
- [`code/fcn.140009bd0.c`](code/fcn.140009bd0.c)
- [`code/fcn.14000b6c0.c`](code/fcn.14000b6c0.c)
- [`code/fcn.14000c290.c`](code/fcn.14000c290.c)
- [`code/fcn.14000c3cc.c`](code/fcn.14000c3cc.c)
- [`code/fcn.14000c714.c`](code/fcn.14000c714.c)
- [`code/fcn.14000f348.c`](code/fcn.14000f348.c)
- [`code/fcn.14000f470.c`](code/fcn.14000f470.c)
- [`code/fcn.140011c8c.c`](code/fcn.140011c8c.c)
- [`code/fcn.14001214c.c`](code/fcn.14001214c.c)
- [`code/fcn.1400132ec.c`](code/fcn.1400132ec.c)
- [`code/fcn.140015ef8.c`](code/fcn.140015ef8.c)
- [`code/fcn.14001a180.c`](code/fcn.14001a180.c)
- [`code/fcn.14001bfdc.c`](code/fcn.14001bfdc.c)
- [`code/fcn.14001d794.c`](code/fcn.14001d794.c)
- [`code/fcn.14001d7a8.c`](code/fcn.14001d7a8.c)
- [`code/fcn.14001d7e0.c`](code/fcn.14001d7e0.c)
- [`code/fcn.1400239a4.c`](code/fcn.1400239a4.c)
- [`code/fcn.1400255c0.c`](code/fcn.1400255c0.c)
- [`code/fcn.140025ea0.c`](code/fcn.140025ea0.c)
- [`code/fcn.140026ce4.c`](code/fcn.140026ce4.c)
- [`code/fcn.14002aeb4.c`](code/fcn.14002aeb4.c)
- [`code/fcn.14002d630.c`](code/fcn.14002d630.c)
- [`code/fcn.14002d700.c`](code/fcn.14002d700.c)
- [`code/fcn.14002eb10.c`](code/fcn.14002eb10.c)

## Behavioral Analysis

This additional disassembly (Chunk 3) provides critical evidence regarding the malware's **persistence mechanisms**, its **internal command-processing engine**, and the specific ways it prepares the environment for its payloads.

The following analysis integrates these new findings with your previous data.

### Updated Analysis: Malware Loader & Multi-Tool Logic

#### 1. Enhanced "Multi-Tool" Dispatcher (The Internal Engine)
The function `fcn.140015ef8` reveals the underlying architecture of the "Fireball," "Ice Arrow," and "Healing Potion" logic mentioned in Chunk 2.
*   **Command Processing:** This function contains a massive conditional tree based on character checks (e.g., checking for 'd', 'S', 'A', 'C', 'E', 'F', 'G', 'o', 'i', 'n', 'p', 's', 'u', 'x').
*   **Implication:** This is a **command dispatcher**. The malware doesn't just execute one thing; it processes a "menu" of instructions. When the user or an external command selects a specific tool (like "Fireball"), this dispatcher identifies the corresponding logic branch to execute.

#### 2. Staging and Persistence Logic
The function `fcn.140008270` provides clear evidence of how the malware prepares the host system for long-term presence:
*   **Path Resolution:** It calls `SHGetKnownFolderPath`, which is used to find standard Windows folders like `%AppData%` or `%LocalAppData%`. 
*   **Directory Creation:** The logic includes checks and messages such as *"La carpeta ya existe"* (The folder already exists) and *"Carpeta de datos creada"* (Data folder created).
*   **Persistence Strategy:** This confirms the malware is not just running in memory; it is actively **creating a dedicated workspace** on the disk. By using `AppData`, it attempts to hide its "staging" directory in a location where users rarely look, ensuring that its dropped payloads have a permanent home on the system.

#### 3. Advanced File Writing & Data Handling
The function `fcn.1400239a4` is a key component of the **Dropper** functionality:
*   **Direct File Writing:** It utilizes `WriteFile` to commit data to the disk. 
*   **Byte Manipulation:** The logic includes manual handling of newline characters (converting `\n` to `\r\n`) and handles buffer offsets carefully. 
*   **Data Transformation:** The fact that it manually manages these transitions suggests it is moving "raw" data from a processed state (de-obfuscated/decrypted) into a final, executable format on the disk.

#### 4. Sophisticated Memory & Offset Calculation
The function `fcn.14001a180` shows high-complexity arithmetic for calculating offsets:
*   **Large Integer Math:** It uses heavy bit-shifting (`>> 0x20`, `<< 0x20`) and modulo operations to handle values larger than a standard 32-bit integer.
*   **Interpretation:** This is common in **packer/crypter** technology. The malware is likely calculating memory addresses for its "modules" on the fly, making it harder for static analysis tools to map out all possible execution paths because the destination of the code isn't hardcoded—it is calculated at runtime.

#### 5. Localization & Targeting
The inclusion of Spanish strings (e.g., *"Error critico," "Carpeta de datos"*):
*   **Target Audience:** This suggests a specific regional target or a developer who speaks Spanish. This helps threat intelligence teams narrow down the origin and potential target demographics of the campaign.

---

### Updated Summary of Risk & Tactics

The complexity of this binary has moved from "simple loader" to **"sophisticated, modular malware framework."**

| Feature | Technical Evidence | Threat Interpretation |
| :--- | :--- | :--- |
| **Sophisticated Logic** | `fcn.140015ef8` (Complex Dispatcher) | The binary acts as a "Command & Control" hub for multiple types of payloads (Fireball, etc.). |
| **Persistence** | `fcn.140008270` (`SHGetKnownFolderPath`) | It establishes a persistent "base of operations" in `%AppData%`. |
| **Evasion/Obfuscation** | `fcn.14001a180` (Shift/Modulo math) | Uses advanced math to hide memory addresses and calculation paths from scanners. |
| **Dropper Capability** | `fcn.1400239a4` (`WriteFile` & Buffer Handling) | It is capable of taking "raw" payload data and reconstructing it into usable files on disk. |

### Conclusion for Incident Response
This malware is a **multi-functional infection engine**. 
1.  **Stage 1:** The initial loader checks the environment (calling `GetConsoleMode`, checking paths).
2.  **Stage 2:** It creates a hidden folder in `%AppData%` to store its tools.
3.  **Stage 3:** Based on "user" input or hardcoded configurations, it selects a module (e.g., Fireball) and uses the **Dispatcher** to decide what functionality to activate.
4.  **Stage 4:** It drops these modules into the created folder and executes them.

**Recommendation:** Search for evidence of non-standard folders within `%AppData%` or `%LocalAppData%`. Any files dropped in these areas by this loader should be treated as high-priority artifacts (potentially containing credential stealers, ransomware, or botnet agents).

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547** | **Persistence** | The malware utilizes `SHGetKnownFolderPath` to create a "dedicated workspace" in `%AppData%`, ensuring a persistent home for dropped payloads. |
| **T1036** | **Masquerading** | By placing its files and data folders within standard Windows directories like `%AppData%`, the malware attempts to hide in plain sight from users and basic security checks. |
| **T1027** | **Obfuscated Files or Programs** | The use of complex bit-shifting and modulo arithmetic to calculate memory offsets is a hallmark of packer/crypter technology used to evade static analysis. |
| **T1568** | **Dynamic Resolution** | The "multi-tool" dispatcher and the calculation of offsets at runtime indicate that the malware resolves its internal modules dynamically rather than using hardcoded addresses. |
| **T1105** | **Ingress Tool Transfer (Dropper)** | The use of `WriteFile` combined with manual buffer/byte manipulation to convert "raw" data into executable formats identifies the binary's role as a dropper. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized as requested:

### **IP addresses / URLs / Domains**
*   *None identified in the provided text.*

### **File paths / Registry keys**
*   **%AppData%**: Identified as a target directory for staging and persisting dropped payloads.
*   **%LocalAppData%**: Identified as a target directory for staging and persistence.
*   **"Carpeta de datos"**: (Translates to "Data folder") A specific string indicating the naming convention or presence of a local data directory created by the malware.

### **Mutex names / Named pipes**
*   *None identified in the provided text.*

### **Hashes**
*   *No valid MD5, SHA-1, or SHA-256 hashes were detected in the string dump.*

### **Other artifacts**
*   **Internal Module Codenames:** "Fireball", "Ice Arrow", "Healing Potion" (These represent different logic branches/modules within the command dispatcher).
*   **Command Dispatcher Keys:** The following characters are used as triggers within the `fcn.140015ef8` dispatcher to activate specific internal tools: `d`, `S`, `A`, `C`, `E`, `F`, `G`, `o`, `i`, `n`, `p`, `s`, `u`, `x`.
*   **Localized Strings (Detection Signatures):** 
    *   `La carpeta ya existe` (The folder already exists)
    *   `Carpeta de datos creada` (Data folder created)
    *   `Error critico` (Critical error)
*   **Function Signatures/Behavioral Markers:**
    *   **Packing behavior:** Use of large integer math, bit-shifting (`>> 0x20`, `<< 0x20`), and modulo operations for dynamic memory offset calculation.
    *   **Dropper Behavior:** Implementation of `WriteFile` to transition de-obfuscated data into a persistent format on disk.

---
**Analyst Note:** The string dump provided appears to be highly obfuscated or part of a packed binary, as the majority of the strings are non-human-readable sequences (e.g., `WATAUAVAWH`, `A_A^A]A\_`). Investigation should focus on any files dropped in `%AppData%` or `%LocalAppData%` containing "Carpeta" related naming conventions.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

**1. Malware family:** Custom
**2. Malware type:** Loader / Dropper
**3. Confidence:** High

**4. Key evidence:**
*   **Modular Dispatcher Architecture:** The existence of a complex command-processing tree (`fcn.140015ef8`) and the use of specific codenames ("Fireball," "Ice Arrow") indicate this is not a single-purpose tool, but a sophisticated **multi-tool framework** designed to host various modules at the discretion of an operator or automated configuration.
*   **Dropper & Persistence Mechanics:** The malware actively seeks out `%AppData%` paths via `SHGetKnownFolderPath` to create "staging" areas and uses `WriteFile` with manual buffer manipulation to de-obfuscate and write raw data into executable files on disk, which is a hallmark of **loader/dropper** behavior.
*   **Advanced Evasion Tactics:** The use of complex bit-shifting (`>> 0x20`, `<< 0x20`) and modulo arithmetic for dynamic memory offset calculation indicates a sophisticated **packer/crypter** layer intended to bypass static analysis by hiding the final destination of its logic paths.
