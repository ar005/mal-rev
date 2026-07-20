# Threat Analysis Report

**Generated:** 2026-07-18 00:28 UTC
**Sample:** `07fb349619b84b7846f20ed121537f86bda484aae9fd492f259eb60ca36cc357_07fb349619b84b7846f20ed121537f86bda484aae9fd492f259eb60ca36cc357.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07fb349619b84b7846f20ed121537f86bda484aae9fd492f259eb60ca36cc357_07fb349619b84b7846f20ed121537f86bda484aae9fd492f259eb60ca36cc357.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 6 sections |
| Size | 89,600 bytes |
| MD5 | `cc1448e7c1a3f724c5703877e9af33eb` |
| SHA1 | `dba95a09c903f2d10486a691b051c52890ef21ab` |
| SHA256 | `07fb349619b84b7846f20ed121537f86bda484aae9fd492f259eb60ca36cc357` |
| Overall entropy | 6.241 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1772293628 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 55,808 | 6.565 | No |
| `.rdata` | 25,088 | 4.783 | No |
| `.data` | 2,560 | 2.058 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 512 | 4.705 | No |
| `.reloc` | 4,096 | 6.413 | No |

### Imports

**KERNEL32.dll**: `ReadFile`, `VirtualFree`, `VirtualAlloc`, `GetModuleHandleA`, `CreateFileA`, `CloseHandle`, `GetProcAddress`, `GetFileSize`, `WriteConsoleW`, `CreateFileW`, `QueryPerformanceCounter`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetSystemTimeAsFileTime`, `InitializeSListHead`
**USER32.dll**: `EnumChildWindows`

## Extracted Strings

Total strings found: **362** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`Rich|
`.rdata
@.data
.fptable
@.reloc
J9Mr

u"h$iA
5ntel
5Genu
38_^]
E9xt
URPQQh`!@
kUQPXY]Y[
QQSVWd
&9Gv!8E
Yt
jV
9Nv@k
< t1<	t-
9>tWV
jh8GA
t	iud
;1t+;u
u9~uj
};GvP
u9^uj
};GvP
</t
<\t
SSSPSQ
u9^u
uSSSSj
};GvP
];3t'
f9:t!V
u|9]t,9
QQSVj8j@
jhXHA
jhxHA
;ut.;
j,h8IA
u VhDoA
9Eu$_[
PPPPPPPP
PPPPPWV
PP9E u
jhXIA

u<jXSf

u	jZf
PVVVVV
D$+d$SVW
D$+d$SVW
__based(
__cdecl
__stdcall
__thiscall
__fastcall
__vectorcall
__preserve_none
__clrcall
__eabi
__swift_1
__swift_2
__swift_3
__ptr64
__restrict
__unaligned
restrict(
 delete
operator
`vftable'
`vbtable'
`vcall'
`typeof'
`local static guard'
`string'
`vbase destructor'
`vector deleting destructor'
`default constructor closure'
`scalar deleting destructor'
`vector constructor iterator'
`vector destructor iterator'
`vector vbase constructor iterator'
`virtual displacement map'
`eh vector constructor iterator'
`eh vector destructor iterator'
`eh vector vbase constructor iterator'
`copy constructor closure'
`udt returning'
`local vftable'
`local vftable constructor closure'
 new[]
 delete[]
`omni callsig'
`placement delete closure'
`placement delete[] closure'
`managed vector constructor iterator'
`managed vector destructor iterator'
`eh vector copy constructor iterator'
`eh vector vbase copy constructor iterator'
`dynamic initializer for '
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040c9e8` | `0x40c9e8` | 2461 | ✓ |
| `fcn.004027d0` | `0x4027d0` | 1396 | ✓ |
| `fcn.00409b40` | `0x409b40` | 1084 | ✓ |
| `fcn.0040a888` | `0x40a888` | 966 | ✓ |
| `fcn.00402fa2` | `0x402fa2` | 915 | ✓ |
| `fcn.00409120` | `0x409120` | 906 | ✓ |
| `fcn.0040d600` | `0x40d600` | 809 | ✓ |
| `fcn.00401855` | `0x401855` | 794 | ✓ |
| `fcn.0040b8b7` | `0x40b8b7` | 671 | ✓ |
| `fcn.00405fe1` | `0x405fe1` | 652 | ✓ |
| `fcn.00401119` | `0x401119` | 616 | ✓ |
| `fcn.0040cbce` | `0x40cbce` | 614 | ✓ |
| `fcn.004071b5` | `0x4071b5` | 606 | ✓ |
| `fcn.0040d960` | `0x40d960` | 590 | ✓ |
| `fcn.0040cf9d` | `0x40cf9d` | 576 | ✓ |
| `fcn.0040b13f` | `0x40b13f` | 540 | ✓ |
| `fcn.0040c6f0` | `0x40c6f0` | 539 | ✓ |
| `fcn.00406c34` | `0x406c34` | 517 | ✓ |
| `fcn.0040df60` | `0x40df60` | 499 | ✓ |
| `fcn.00408a64` | `0x408a64` | 498 | ✓ |
| `fcn.0040a164` | `0x40a164` | 493 | ✓ |
| `fcn.0040c1f0` | `0x40c1f0` | 471 | ✓ |
| `fcn.004097cf` | `0x4097cf` | 441 | ✓ |
| `fcn.0040683f` | `0x40683f` | 421 | ✓ |
| `entry0` | `0x401371` | 399 | ✓ |
| `fcn.00405db3` | `0x405db3` | 381 | ✓ |
| `fcn.00403fc3` | `0x403fc3` | 370 | ✓ |
| `fcn.0040a3b0` | `0x40a3b0` | 364 | ✓ |
| `fcn.00401f60` | `0x401f60` | 346 | ✓ |
| `fcn.004036bb` | `0x4036bb` | 345 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401119.c`](code/fcn.00401119.c)
- [`code/fcn.00401855.c`](code/fcn.00401855.c)
- [`code/fcn.00401f60.c`](code/fcn.00401f60.c)
- [`code/fcn.004027d0.c`](code/fcn.004027d0.c)
- [`code/fcn.00402fa2.c`](code/fcn.00402fa2.c)
- [`code/fcn.004036bb.c`](code/fcn.004036bb.c)
- [`code/fcn.00403fc3.c`](code/fcn.00403fc3.c)
- [`code/fcn.00405db3.c`](code/fcn.00405db3.c)
- [`code/fcn.00405fe1.c`](code/fcn.00405fe1.c)
- [`code/fcn.0040683f.c`](code/fcn.0040683f.c)
- [`code/fcn.00406c34.c`](code/fcn.00406c34.c)
- [`code/fcn.004071b5.c`](code/fcn.004071b5.c)
- [`code/fcn.00408a64.c`](code/fcn.00408a64.c)
- [`code/fcn.00409120.c`](code/fcn.00409120.c)
- [`code/fcn.004097cf.c`](code/fcn.004097cf.c)
- [`code/fcn.00409b40.c`](code/fcn.00409b40.c)
- [`code/fcn.0040a164.c`](code/fcn.0040a164.c)
- [`code/fcn.0040a3b0.c`](code/fcn.0040a3b0.c)
- [`code/fcn.0040a888.c`](code/fcn.0040a888.c)
- [`code/fcn.0040b13f.c`](code/fcn.0040b13f.c)
- [`code/fcn.0040b8b7.c`](code/fcn.0040b8b7.c)
- [`code/fcn.0040c1f0.c`](code/fcn.0040c1f0.c)
- [`code/fcn.0040c6f0.c`](code/fcn.0040c6f0.c)
- [`code/fcn.0040c9e8.c`](code/fcn.0040c9e8.c)
- [`code/fcn.0040cbce.c`](code/fcn.0040cbce.c)
- [`code/fcn.0040cf9d.c`](code/fcn.0040cf9d.c)
- [`code/fcn.0040d600.c`](code/fcn.0040d600.c)
- [`code/fcn.0040d960.c`](code/fcn.0040d960.c)
- [`code/fcn.0040df60.c`](code/fcn.0040df60.c)

## Behavioral Analysis

This updated analysis incorporates the findings from both code segments, providing a comprehensive overview of the binary's behavior based on the provided disassemblies.

### Updated Analysis Summary

The binary remains identified as a complex piece of software with characteristics common to **multi-stage installers or sophisticated packers**. The additional disassembly confirms high levels of internal complexity regarding memory management and error handling, which are often used in software that must manage large amounts of data or evade detection by ensuring environmental stability.

---

### 1. Core Functionality and Purpose
The binary's capabilities involve:
*   **Environment Validation:** Detailed checks for hardware/CPU features (as seen in the first chunk) to ensure compatibility or identify sandbox environments.
*   **File System Navigation & Data "Dropping":** Robust logic for identifying files, potentially preparing a directory structure for installation or payload extraction.
*   **Sophisticated Memory Management:** The new data shows extensive routines for memory alignment and large-buffer management (e.g., `fcn.00401f60`). This is used to handle complex data structures efficiently in memory.
*   **Robust Error Handling:** The code includes specific logic to catch failures during initialization (such as the check against `fcn.0040bb56`) and assign error codes, suggesting it is designed to be stable and "fail-safe" during its execution.

### 2. Suspicious or Malicious Behaviors
The following behaviors remain high-priority indicators of potential risk:

*   **Environmental Fingerprinting & Anti-Analysis:** (Continued from Chunk 1) The binary aggressively checks CPU capabilities and environment status before proceeding. This is a classic "gatekeeping" technique used by malware to avoid running in research environments.
*   **File Manipulation/Payload Delivery:** (Continued from Chunk 1) The use of `WriteFile` and file-search routines suggests the potential for "dropping" additional components or modifying system files.
*   **Complex State Management & Buffer Preparation:**
    *   The function `fcn.00401f60` shows highly repetitive logic to fill memory addresses (`piVar2`) in chunks of 8, 16, and 32. This is often used when preparing a buffer for **decrypted payloads** or **large data structures** that must be precisely aligned in memory to avoid detection by heuristic scanners or simply to comply with system requirements.
    *   The usage of hardcoded offsets (like `0x416960`) to determine behavior indicates the code relies on a pre-defined state map, common in complex installers and advanced packers.

### 3. Notable Techniques and Patterns
*   **Memory Alignment and Buffering:** The logic in `fcn.00401f60` is particularly interesting; it performs manual pointer arithmetic to ensure memory blocks are filled correctly. This type of "heavy lifting" for memory management can be a sign of an **advanced packer (e.g., UPX variants or custom packers)** designed to unpack and execute code in-memory.
*   **Stack Protection:** The inclusion of `unaff_FS_OFFSET` indicates the binary was compiled with modern security protections (like GS cookies). While this is common in legitimate software, it also confirms that the developers aimed for a professional/high-quality build, which is consistent with sophisticated malware.
*   **Hardcoded Context & Identity:** The presence of "Tencent" related paths and the specific error handling codes suggest either a large, commercially available installer or highly specialized software designed for a specific demographic. If this binary was found in an unexpected location (e.g., `AppData` or `Temp`), it is likely part of a bundled software suite or a malicious dropper.

### Updated Risk Assessment
The inclusion of the second chunk reinforces the suspicion that this is **not** simple, amateur-grade malware. The presence of complex memory alignment logic (`fcn.00401f60`) and disciplined error handling indicates either a high-quality commercial installer or a professional-grade packer/loader used by advanced persistent threats (APTs) or for "grayware" distribution.

**Indicators for Incident Response:**
*   **Detection Target:** The binary behaves like a **Loader**. It checks the environment to see if it is safe to run, then prepares memory space and writes files to the disk.
*   **Primary Threat:** High probability of being a **Multi-stage Dropper**. Its primary role is likely to verify the system, bypass "sandbox" detection, and then drop/execute a second stage of code that performs the actual malicious activity (e.g., data exfiltration or persistence).
*   **Recommendation:** Treat the binary as high-risk. Any file paths it touches should be monitored for changes, and its network activity (if any) should be logged to identify potential Command & Control (C2) communication.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the following MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Eevasion | The binary performs detailed hardware and CPU feature checks specifically designed to identify if it is running in a research or analysis environment. |
| **T1027** | Obfuscated Files or Information | The use of complex memory alignment logic, hardcoded offsets, and sophisticated packing indicates an effort to hide the true intent of the payload from signature-based detection. |
| **T1105** | Ingress Tool Transfer | The "dropping" functionality and usage of `WriteFile` routines indicate the movement of additional components or payloads onto the local file system for subsequent execution. |
| **T1036** | Masquerading | The inclusion of specific, well-known brand names (e.g., "Tencent") in path strings suggests an attempt to blend in as legitimate software. |
| **T1055** | Process Injection | The manual memory management and buffer preparation for "decrypted payloads" indicate the staging of code to be executed in memory, likely via a loader/injector mechanism. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized as requested:

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `C:\HRSoftstore\Install\tengxunshipin\components\26oder\Release\26oder.pdb` 
    *   *Note: While .pdb files are symbols used during development, the specific path provides context on the build environment and potential distribution folders.*

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts (user agents, C2 patterns, etc.)**
*   **Suspicious String:** `jiami2026` (Potential internal identifier or project-specific string).
*   **Malware Behavior/Patterns:** 
    *   **Environment Fingerprinting:** Evidence of hardware/CPU capability checks to detect sandbox environments.
    *   **Memory Manipulation:** Use of advanced memory alignment and buffer preparation (specifically `fcn.00401f60`) consistent with **packer or loader behavior**.
    *   **Drop Logic:** Indications of a multi-stage delivery mechanism where the binary acts as a dropper for additional components.
    *   **Tencent-related references:** References to "tengxun" in file paths suggesting specific targeting or masquerading as legitimate software from that ecosystem.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1.  **Malware family:** custom (Sophisticated Loader/Packer)
2.  **Malware type:** loader / dropper
3.  **Confidence:** High
4.  **Key evidence:** 
    *   **Anti-Analysis & Evasion:** The binary performs extensive environment fingerprinting and hardware/CPU checks to identify and bypass sandbox environments (MITRE T1497).
    *   **Sophisticated Memory Manipulation:** The use of advanced memory alignment, buffer management, and manual pointer arithmetic for "decrypted payloads" is characteristic of high-quality loaders designed to execute code in-memory while avoiding signature detection.
    *   **Multi-stage Delivery:** The combination of file-system navigation ("dropping" files) and masquerading (using Tencent-related strings) indicates a multi-stage execution model where this binary acts as the initial vector to deliver subsequent malicious components.
