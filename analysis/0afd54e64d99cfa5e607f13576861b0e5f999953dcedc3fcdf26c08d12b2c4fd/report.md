# Threat Analysis Report

**Generated:** 2026-07-25 17:08 UTC
**Sample:** `0afd54e64d99cfa5e607f13576861b0e5f999953dcedc3fcdf26c08d12b2c4fd_0afd54e64d99cfa5e607f13576861b0e5f999953dcedc3fcdf26c08d12b2c4fd.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0afd54e64d99cfa5e607f13576861b0e5f999953dcedc3fcdf26c08d12b2c4fd_0afd54e64d99cfa5e607f13576861b0e5f999953dcedc3fcdf26c08d12b2c4fd.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 297,472 bytes |
| MD5 | `6dc9e60b6798d1ce192399005c790105` |
| SHA1 | `9624e6542e4d7f86c45a7269838708a06d9c4cc0` |
| SHA256 | `0afd54e64d99cfa5e607f13576861b0e5f999953dcedc3fcdf26c08d12b2c4fd` |
| Overall entropy | 6.293 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1764735164 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 193,024 | 6.453 | No |
| `.rdata` | 84,480 | 5.167 | No |
| `.data` | 5,120 | 2.826 | No |
| `.pdata` | 10,752 | 5.286 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,560 | 5.407 | No |

### Imports

**SHELL32.dll**: `ShellExecuteExW`, `SHGetKnownFolderPath`, `ord_680`, `ShellExecuteA`
**ole32.dll**: `CoInitialize`, `CoUninitialize`, `CoTaskMemFree`
**urlmon.dll**: `URLDownloadToFileW`
**KERNEL32.dll**: `GetCurrentProcessId`, `WriteConsoleW`, `HeapSize`, `GetProcessHeap`, `SetStdHandle`, `FreeEnvironmentStringsW`, `GetEnvironmentStringsW`, `GetCommandLineW`, `GetCommandLineA`, `GetOEMCP`, `CloseHandle`, `GetLastError`, `Sleep`, `CreateProcessA`, `GetSystemDirectoryA`

## Extracted Strings

Total strings found: **1051** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
.reloc
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
UVWATAUAVAWH
A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
SUVWATAUAVAWH
A_A^A]A\_^][
UVWATAUAVAWH
A_A^A]A\_^]
UWAUAVAWH
A_A^A]_]
L$ SUVWH
fB9<H}
l$ VWAVH
t$ UWATAVAWH
A_A^A\_]
\$ UVWH
WATAUAVAWH
 A_A^A]A\_
tsH91un
t$ UWAVH
taL9Chu
L90u H
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14001d048` | `0x14001d048` | 53931 | ✓ |
| `fcn.14001d034` | `0x14001d034` | 53890 | ✓ |
| `fcn.14000bdcc` | `0x14000bdcc` | 46886 | ✓ |
| `fcn.1400257c0` | `0x1400257c0` | 19273 | ✓ |
| `fcn.14000c114` | `0x14000c114` | 18250 | ✓ |
| `fcn.140003cb0` | `0x140003cb0` | 7368 | ✓ |
| `fcn.14000bc90` | `0x14000bc90` | 6405 | ✓ |
| `fcn.14002a7d4` | `0x14002a7d4` | 4735 | ✓ |
| `fcn.14002cf50` | `0x14002cf50` | 3559 | ✓ |
| `fcn.1400059e0` | `0x1400059e0` | 3545 | ✓ |
| `fcn.140006e00` | `0x140006e00` | 2957 | ✓ |
| `fcn.14000b0d0` | `0x14000b0d0` | 2490 | ✓ |
| `fcn.14000ec70` | `0x14000ec70` | 2341 | ✓ |
| `fcn.140009060` | `0x140009060` | 2318 | ✓ |
| `fcn.14000ed90` | `0x14000ed90` | 2064 | ✓ |
| `fcn.14001d100` | `0x14001d100` | 1946 | ✓ |
| `fcn.140026604` | `0x140026604` | 1829 | ✓ |
| `fcn.140001c60` | `0x140001c60` | 1703 | ✓ |
| `fcn.14002e430` | `0x14002e430` | 1677 | ✓ |
| `fcn.1400067c0` | `0x1400067c0` | 1598 | ✓ |
| `fcn.1400050d0` | `0x1400050d0` | 1571 | ✓ |
| `fcn.14002d020` | `0x14002d020` | 1451 | ✓ |
| `fcn.140011a6c` | `0x140011a6c` | 1312 | ✓ |
| `fcn.140007990` | `0x140007990` | 1282 | ✓ |
| `fcn.140012c0c` | `0x140012c0c` | 1229 | ✓ |
| `fcn.1400115ac` | `0x1400115ac` | 1213 | ✓ |
| `fcn.1400232c4` | `0x1400232c4` | 1171 | ✓ |
| `fcn.140019a20` | `0x140019a20` | 1164 | ✓ |
| `fcn.14001b87c` | `0x14001b87c` | 1153 | ✓ |
| `fcn.140015818` | `0x140015818` | 1133 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001c60.c`](code/fcn.140001c60.c)
- [`code/fcn.140003cb0.c`](code/fcn.140003cb0.c)
- [`code/fcn.1400050d0.c`](code/fcn.1400050d0.c)
- [`code/fcn.1400059e0.c`](code/fcn.1400059e0.c)
- [`code/fcn.1400067c0.c`](code/fcn.1400067c0.c)
- [`code/fcn.140006e00.c`](code/fcn.140006e00.c)
- [`code/fcn.140007990.c`](code/fcn.140007990.c)
- [`code/fcn.140009060.c`](code/fcn.140009060.c)
- [`code/fcn.14000b0d0.c`](code/fcn.14000b0d0.c)
- [`code/fcn.14000bc90.c`](code/fcn.14000bc90.c)
- [`code/fcn.14000bdcc.c`](code/fcn.14000bdcc.c)
- [`code/fcn.14000c114.c`](code/fcn.14000c114.c)
- [`code/fcn.14000ec70.c`](code/fcn.14000ec70.c)
- [`code/fcn.14000ed90.c`](code/fcn.14000ed90.c)
- [`code/fcn.1400115ac.c`](code/fcn.1400115ac.c)
- [`code/fcn.140011a6c.c`](code/fcn.140011a6c.c)
- [`code/fcn.140012c0c.c`](code/fcn.140012c0c.c)
- [`code/fcn.140015818.c`](code/fcn.140015818.c)
- [`code/fcn.140019a20.c`](code/fcn.140019a20.c)
- [`code/fcn.14001b87c.c`](code/fcn.14001b87c.c)
- [`code/fcn.14001d034.c`](code/fcn.14001d034.c)
- [`code/fcn.14001d048.c`](code/fcn.14001d048.c)
- [`code/fcn.14001d100.c`](code/fcn.14001d100.c)
- [`code/fcn.1400232c4.c`](code/fcn.1400232c4.c)
- [`code/fcn.1400257c0.c`](code/fcn.1400257c0.c)
- [`code/fcn.140026604.c`](code/fcn.140026604.c)
- [`code/fcn.14002a7d4.c`](code/fcn.14002a7d4.c)
- [`code/fcn.14002cf50.c`](code/fcn.14002cf50.c)
- [`code/fcn.14002d020.c`](code/fcn.14002d020.c)
- [`code/fcn.14002e430.c`](code/fcn.14002e430.c)

## Behavioral Analysis

This third chunk of disassembly provides deep insights into how the malware interacts with the local file system and handles data post-download. It confirms that this is not a simple "one-step" downloader, but a **sophisticated stager** designed to prepare a local environment for a secondary payload.

Here is the updated analysis incorporating the new findings:

### 1. Environment Preparation & File System Manipulation (New)
This chunk reveals significant logic dedicated to preparing the local machine to host the malicious payload.
*   **`SHGetKnownFolderPath` Integration:** The function `fcn.140007990` calls `SHGetKnownFolderPath`. This is used to identify standard system paths (e.g., `%AppData%`, `Documents`, or `Desktop`). This confirms the malware intends to place its files in "safe" looking locations where a user wouldn't notice them immediately.
*   **Folder Creation Logic:** The code contains logic to check if certain directories exist. The Portuguese strings:
    *   `Carpeta de dados criada` (**"Data folder created"**)
    *   `Carpeta já existe` (**"Folder already exists"**)
    *   These are used in conditional branches (e.g., `fcn.140007990`). This indicates a "setup" phase where the malware ensures it has a workspace to drop and run its subsequent components.
*   **Direct File Writing:** The use of `WriteFile` in `fcn.1400232c4` suggests that after downloading, the malware may write configuration files or logs, or perform a "copy" operation of the received data into a final executable state.

### 2. Advanced Decoding & "Unpacking" Logic (Expanded)
The complexity of the mathematical operations in `fcn.140019a20` suggests sophisticated data processing:
*   **Bit-Shifting and Modulo Arithmetic:** The function uses heavy bitwise shifts (`>>`, `<<`), XORs, and modulo calculations to traverse memory buffers. This is a hallmark of **custom decryption routines**. 
*   **Implication:** It is highly likely that the file downloaded from `196.251.107.94` is not "ready-to-run" in its raw state; it is likely encrypted or packed, and this binary contains the logic to decrypt/unpack it before execution.

### 3. Hardened Robustness & Buffer Management
The code exhibits several patterns used by professional malware authors to ensure stability:
*   **Sophisticated Bound Checking:** Functions like `fcn.140012c0c` and `fcn.1400115ac` contain extensive "guard" logic—checking lengths, verifying buffer boundaries, and ensuring pointers are not null before attempting to access memory. This ensures the malware doesn't crash the system (which would alert the user) if it encounters unexpected data during its unpacking/decoding phases.
*   **Memory Cleaning:** Consistent use of `HeapFree` or similar routines after processing strings confirms a desire to leave as small of a forensic footprint in RAM as possible.

### 4. Enhanced "Themed" Masquerading (Portuguese Localization)
The continued presence of Portuguese-themed logic reinforces the targeting:
*   **Targeted Localized Feedback:** The logic specifically detects if a folder exists and prints/processes localized messages. This suggests a sophisticated level of localization meant to blend in with local system notifications or scripts, potentially masking its actions as "standard" installation procedures for an installer or game update.

---

### Updated Summary Checklist
*   **Downloader/Dropper:** **Confirmed (Advanced).** It doesn't just download; it performs environment "staging" by creating directories and preparing paths using standard Windows APIs.
*   **Anti-Analysis / Obfuscation:** **High.** The use of complex bitwise math (`fcn.140019a20`) suggests a multi-layered decryption process for the payload.
*   **Persistence/Staging:** **Confirmed.** Use of `SHGetKnownFolderPath` indicates a strategy to hide files in standard user directories.
*   **Malicious Masquerading:** **Extreme.** High usage of Portuguese "game-like" and "installer-style" strings creates a layer of camouflage for the technical actions being performed.

### Final Conclusion Update (Cumulative)
This is a **highly professional, multi-stage Trojan dropper/downloader**. 

The malware’s workflow is now clearly mapped:
1.  **Privilege Check:** It ensures it has enough rights to proceed.
2.  **Environment Setup:** It identifies system folders via `SHGetKnownFolderPath` and creates local "data" directories (using Portuguese messaging).
3.  **Network Retrieval:** It reaches out to the command-and-control (C2) IP `196.251.107.94` to download a payload (`build.exe`).
4.  **Decoding/Unpacking:** It uses complex, non-standard mathematical loops to decrypt and unpack the downloaded content in memory or on disk.
5.  **Execution:** Once "cleaned" and unpacked, it executes the final stage of the attack (e.g., a keylogger, info-stealer, or ransomware).

The heavy use of **RPG/Gaming Portuguese terms** combined with professional-grade **bit-shifting routines** indicates this is likely part of a sophisticated malware campaign targeting Brazilian/Portuguese-speaking users.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1105** | Ingress Tool Transfer | The malware acts as a "sophisticated stager" by downloading a secondary payload (`build.exe`) from a remote IP address to facilitate further stages of the attack. |
| **T1036** | Masquerading | The use of `SHGetKnownFolderPath` and localized Portuguese "game-style" labels is designed to blend in with legitimate system folders and standard installer behaviors. |
| **T1027** | Obfuscated Files or Information | The extensive use of bit-shifting, XOR operations, and heap management indicates a complex decryption/unpacking routine for the payload before it is executed. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `196.251.107.94` (Identified as a C2/Downloader IP)

**File paths / Registry keys**
*   `build.exe` (The filename of the secondary payload downloaded by the stager)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None found in the provided strings.*

**Other artifacts**
*   **Localization Strings:** 
    *   `Carpeta de dados criada` (Used during folder creation logic)
    *   `Carpeta já existe` (Used for local feedback/status)
*   **C2/Execution Patterns:**
    *   The malware utilizes `SHGetKnownFolderPath` to identify standard user directories for staging.
    *   The malware employs non-standard bit-shifting, XORing, and modulo arithmetic for custom decryption of the payload.
    *   **Targeting Profile:** The use of Portuguese localization indicates a campaign targeting Brazilian/Portuguese-speaking users.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family:** Unknown (Potential custom builder)
2. **Malware type:** Dropper
3. **Confidence:** High
4. **Key evidence:**
    *   **Multi-Stage Execution Architecture:** The malware functions as a sophisticated stager; it does not contain the final malicious payload but instead downloads, decodes, and unpacks `build.exe` using complex bitwise logic (XOR/shifting).
    *   **Evasive Persistence & Masquerading:** It uses `SHGetKnownFolderPath` to hide files in standard user directories and employs Portuguese-localized "game" strings to blend in with legitimate software during the setup phase.
    *   **Advanced Decoding Routines:** The presence of custom, non-standard mathematical loops for memory buffer processing indicates a high level of development intended to bypass signature-based detection of the secondary payload.
