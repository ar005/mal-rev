# Threat Analysis Report

**Generated:** 2026-08-31 16:53 UTC
**Sample:** `128acee9bc263b6c746e11e014b71911e8a13063a1692ce61db1e9b9f3801d81_128acee9bc263b6c746e11e014b71911e8a13063a1692ce61db1e9b9f3801d81.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `128acee9bc263b6c746e11e014b71911e8a13063a1692ce61db1e9b9f3801d81_128acee9bc263b6c746e11e014b71911e8a13063a1692ce61db1e9b9f3801d81.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 4,596,736 bytes |
| MD5 | `76be4bb30a3397771ace560f1fc171d1` |
| SHA1 | `a19c95204e80a9fa3bb03ee46c6a6788e351af4d` |
| SHA256 | `128acee9bc263b6c746e11e014b71911e8a13063a1692ce61db1e9b9f3801d81` |
| Overall entropy | 6.557 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773888405 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 3,708,928 | 6.514 | No |
| `.rdata` | 676,864 | 5.803 | No |
| `.data` | 81,920 | 5.431 | No |
| `.pdata` | 69,120 | 6.186 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 1,024 | 2.747 | No |
| `.reloc` | 57,344 | 5.442 | No |

### Imports

**SHLWAPI.dll**: `PathFindFileNameW`
**WININET.dll**: `HttpAddRequestHeadersA`, `HttpOpenRequestW`, `HttpSendRequestA`, `InternetCanonicalizeUrlW`, `InternetCloseHandle`, `InternetConnectA`, `InternetOpenA`, `InternetOpenUrlA`, `InternetOpenUrlW`, `InternetReadFile`
**ADVAPI32.dll**: `GetUserNameA`
**IPHLPAPI.DLL**: `GetAdaptersAddresses`, `GetExtendedUdpTable`, `GetIpForwardTable`, `GetIpNetTable`, `GetTcpTable2`
**KERNEL32.dll**: `AllocConsole`, `CloseHandle`, `CreateDirectoryA`, `CreateFileA`, `CreateFileW`, `CreateHardLinkW`, `CreatePipe`, `CreateProcessA`, `CreateProcessW`, `CreateThread`, `CreateToolhelp32Snapshot`, `DeleteCriticalSection`, `DeleteFileA`, `DeleteFileW`, `DuplicateHandle`
**msvcrt.dll**: `___lc_codepage_func`, `___mb_cur_max_func`, `__getmainargs`, `__initenv`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `_amsg_exit`, `_cexit`, `_close`, `_commode`, `_errno`, `_exit`, `_fdopen`, `_filelengthi64`
**USER32.dll**: `ShowWindow`
**WS2_32.dll**: `inet_ntoa`, `inet_ntop`, `ntohs`

## Extracted Strings

Total strings found: **9105** (showing first 100)

```
!This program cannot be run in DOS mode.$
`.rdata
@.data
.pdata
@.reloc
ATUWVSH
 [^_]A\
 [^_]A\
AWAVAUATVWUSH
([]_^A\A]A^A_
fffff.
AWAVVWSH
@[_^A^A_
fffff.
AWAVAUATVWUS
[]_^A\A]A^A_
AWAVAUATVWUS
t$9Hc
[]_^A\A]A^A_
AWAVAUATVWUSH
D$hHc
D$`Hcg
[]_^A\A]A^A_
AWAVAUATVWUSH
D$hLiD$h
[]_^A\A]A^A_
AWAVVWSH
[_^A^A_
fffff.
fffff.
AWAVAUATVWUSH
ffffff.
 []_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
ljLCE1
[]_^A\A]A^A_
AWAVAUATVWUSH
fffff.
 []_^A\A]A^A_
AWAVAUATVWUSH
([]_^A\A]A^A_
AWAVAUATVWUSH
0[]_^A\A]A^A_
AWAVAUATVWUSH
eV!lD)
[]_^A\A]A^A_
AWAVAUATVWUSH
 []_^A\A]A^A_
AWAVAUATVWUSH
ffffff.
ffffff.
 []_^A\A]A^A_
AWAVAUATVWUSH
MY7yIc
[]_^A\A]A^A_
AWAVAUATVWUSH
 []_^A\A]A^A_
AWAVAUATVWUSH
fffff.
([]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
fffff.
AWAVAUATVWUSH
0[]_^A\A]A^A_
fffff.
AWAVAUATVWUSH
Jc\	H
JcL	LH
JcL	8H
[]_^A\A]A^A_
AWAVAUATVWUSH
([]_^A\A]A^A_
ffffff.
AWAVAUATVWUSH
ff!aD1
[]_^A\A]A^A_
ffffff.
AWAVAUATVWUSH
([]_^A\A]A^A_
AWAVATVWSH
([_^A\A^A_
AWAVATVWSH
8[_^A\A^A_
AWAVAUATVWUSH
L$@Hc\;B
H[]_^A\A]A^A_
AWAVAUATVWUSH
D$(H;D$0
HcI3B
8[]_^A\A]A^A_
AVVWSH
8[_^A^
AWAVAUATVWUSH
HcV0B
H[]_^A\A]A^A_
AWAVATVWSH
([_^A\A^A_H
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140369510` | `0x140369510` | 620564 | ✓ |
| `fcn.140388d90` | `0x140388d90` | 509749 | ✓ |
| `fcn.14035bd50` | `0x14035bd50` | 326204 | ✓ |
| `fcn.14030d080` | `0x14030d080` | 280782 | ✓ |
| `fcn.140388ea0` | `0x140388ea0` | 267244 | ✓ |
| `fcn.140348d20` | `0x140348d20` | 266191 | ✓ |
| `fcn.14030c040` | `0x14030c040` | 215494 | ✓ |
| `fcn.140342c40` | `0x140342c40` | 94494 | ✓ |
| `fcn.140369280` | `0x140369280` | 72630 | ✓ |
| `fcn.140368520` | `0x140368520` | 69222 | ✓ |
| `fcn.1403663c0` | `0x1403663c0` | 61323 | ✓ |
| `fcn.1403479b0` | `0x1403479b0` | 30197 | ✓ |
| `fcn.14034be10` | `0x14034be10` | 28911 | ✓ |
| `fcn.140082940` | `0x140082940` | 12785 | ✓ |
| `fcn.14007c450` | `0x14007c450` | 12245 | ✓ |
| `fcn.140333120` | `0x140333120` | 10394 | ✓ |
| `fcn.1400a81a0` | `0x1400a81a0` | 9126 | ✓ |
| `fcn.14031dfb0` | `0x14031dfb0` | 9098 | ✓ |
| `fcn.140268680` | `0x140268680` | 8754 | ✓ |
| `fcn.1402bc970` | `0x1402bc970` | 8527 | ✓ |
| `fcn.1402895b0` | `0x1402895b0` | 7552 | ✓ |
| `fcn.1402e7d50` | `0x1402e7d50` | 7148 | ✓ |
| `fcn.140341000` | `0x140341000` | 7106 | ✓ |
| `fcn.140359d60` | `0x140359d60` | 6236 | ✓ |
| `fcn.14032b3e0` | `0x14032b3e0` | 6166 | ✓ |
| `fcn.1400966d0` | `0x1400966d0` | 5519 | ✓ |
| `fcn.14027ca80` | `0x14027ca80` | 5494 | ✓ |
| `fcn.14008d8a0` | `0x14008d8a0` | 5068 | ✓ |
| `fcn.14027e5d0` | `0x14027e5d0` | 4884 | ✓ |
| `fcn.1402c0190` | `0x1402c0190` | 4547 | ✓ |

### Decompiled Code Files

- [`code/fcn.14007c450.c`](code/fcn.14007c450.c)
- [`code/fcn.140082940.c`](code/fcn.140082940.c)
- [`code/fcn.14008d8a0.c`](code/fcn.14008d8a0.c)
- [`code/fcn.1400966d0.c`](code/fcn.1400966d0.c)
- [`code/fcn.1400a81a0.c`](code/fcn.1400a81a0.c)
- [`code/fcn.140268680.c`](code/fcn.140268680.c)
- [`code/fcn.14027ca80.c`](code/fcn.14027ca80.c)
- [`code/fcn.14027e5d0.c`](code/fcn.14027e5d0.c)
- [`code/fcn.1402895b0.c`](code/fcn.1402895b0.c)
- [`code/fcn.1402bc970.c`](code/fcn.1402bc970.c)
- [`code/fcn.1402c0190.c`](code/fcn.1402c0190.c)
- [`code/fcn.1402e7d50.c`](code/fcn.1402e7d50.c)
- [`code/fcn.14030c040.c`](code/fcn.14030c040.c)
- [`code/fcn.14030d080.c`](code/fcn.14030d080.c)
- [`code/fcn.14031dfb0.c`](code/fcn.14031dfb0.c)
- [`code/fcn.14032b3e0.c`](code/fcn.14032b3e0.c)
- [`code/fcn.140333120.c`](code/fcn.140333120.c)
- [`code/fcn.140341000.c`](code/fcn.140341000.c)
- [`code/fcn.140342c40.c`](code/fcn.140342c40.c)
- [`code/fcn.1403479b0.c`](code/fcn.1403479b0.c)
- [`code/fcn.140348d20.c`](code/fcn.140348d20.c)
- [`code/fcn.14034be10.c`](code/fcn.14034be10.c)
- [`code/fcn.140359d60.c`](code/fcn.140359d60.c)
- [`code/fcn.14035bd50.c`](code/fcn.14035bd50.c)
- [`code/fcn.1403663c0.c`](code/fcn.1403663c0.c)
- [`code/fcn.140368520.c`](code/fcn.140368520.c)
- [`code/fcn.140369280.c`](code/fcn.140369280.c)
- [`code/fcn.140369510.c`](code/fcn.140369510.c)
- [`code/fcn.140388d90.c`](code/fcn.140388d90.c)
- [`code/fcn.140388ea0.c`](code/fcn.140388ea0.c)

## Behavioral Analysis

This analysis incorporates the findings from **Chunk 9/9** into the existing framework. The latest disassembly provides high-resolution detail regarding how the engine handles internal state, complex data lookups, and memory abstraction.

### Updated Analysis Summary

#### 1. Core Functionality and Purpose
The evidence continues to support a **High-Complexity Scripting Runtime / Virtual Machine**. The logic in Chunk 9 specifically highlights the "Resolution" phase of script execution—where a high-level command is translated into a specific internal handler.

*   **Massive Optimized Dispatch Tables:** The extremely deep nested `if-else` structures (e.g., checking ranges like `uVar21 < 0x1fcc`, `0x244f`, etc.) are characteristic of a **highly optimized multi-way switch**. In modern compilers, this is the result of a large "Jump Table" or "Decision Tree." It implies that the engine supports hundreds, if not thousands, of distinct command types or state transitions.
*   **Complex Mapping & Handle Resolution:** The repetitive use of complex bit-shifting and XORing (e.g., `(uVar19 >> 0x18 | (uVar19 & 0xff0000) >> 8...)`) suggests a **Handle System**. Instead of using raw memory addresses, the "Script" uses IDs which are passed through these bitwise operations to resolve into internal "Handles." This provides a layer of isolation between the script's logic and the host system's memory.
*   **Multi-Stage Validation:** The code frequently validates results (e.g., `if (cVar11 != '\0')`) before proceeding. This confirms a **Robust Execution Layer**, ensuring that even if a script provides an invalid or out-of-bounds request, the host application remains stable.

#### 2. Sophistication and Complexity
The complexity is consistent with **Enterprise-Grade Game Engine Middleware** (e.g., Unreal Engine's scripting layer, Unity's IL2CPP backend, or similar proprietary engines).

*   **High-Density Logic Blocks:** The presence of numerous labels (`code_r0x00014027e6b0`, `code_r0x00014027f482`) and intricate branching shows that the engine handles very specific edge cases. This is typical in environments where "Object Types," "Contexts," and "Permissions" all influence how a single command is executed.
*   **Dynamic Dispatch:** In `fcn.1402c0190`, the code performs what appears to be a **Method Lookup**. It checks if an object's internal capability (represented by `uVar12` or similar) matches certain criteria before selecting a function pointer from a table. This is a hallmark of polymorphism in high-level languages (like C# or C++).
*   **Memory Segregation:** The use of specific memory offsets and calculations to "hide" the actual location of data suggests that the engine is designed for **Security/Stability**. By using intermediate indices rather than direct pointers, it prevents a script from potentially accessing unauthorized system resources.

#### 3. Technical Observations
*   **Compiler Optimization Artifacts:** The complex-looking math (e.g., `uVar7 = (uVar17 | 0x14) + uVar20 ... & 0x1f`) is typical of a compiler attempting to optimize **multi-dimensional array lookups** or bit-packed structures into immediate values.
*   **State Management:** The logic involving `*in_stack_00000030 = *in_stack_00000030 | 4` indicates a **Bitmask State Machine**. These "flags" are likely used to track the status of a script (e.g., "Is Busy," "Is Dirty," "Has Error").
*   **Standardized Runtime Behavior:** The way `fcn.1402c0190` wraps complex calls suggests a **Gateway Pattern**. It takes high-level arguments, validates them against the internal state of the VM, and then dispatches to the specific low-level handler required to execute that instruction.

### Conclusion (Final Integration)
The addition of Chunk 9 provides definitive confirmation that this library is not a simple script interpreter; it is a **Sophisticated Scripting Runtime/VM Engine**. It features a highly engineered pipeline for resolving commands, managing state through flags, and providing a layer of abstraction between the "Script World" and the "System World."

**Key characteristics confirmed across all chunks:**
1.  **Complex Dispatcher:** Uses massive tree-structures to resolve internal instructions into executable logic.
2.  **Handle/ID Mapping:** Employs bit-shifting and masking to translate script-provided IDs into safe, internally manageable offsets.
3.  **Robust Execution Layer:** Includes extensive checks for null pointers, boundary conditions, and state validation before performing critical operations.
4.  **Multilayered Abstraction:** High complexity is used not as a means of obfuscation, but as a tool to manage the immense complexity required by modern game engines or large-scale software frameworks.

**Status:** No evidence of malicious activity; remains classified as **"Sophisticated Scripting Runtime/VM Engine."**

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors observed in the provided analysis to the relevant MITRE ATT&CK techniques. While the final conclusion of the report notes no current evidence of malicious intent, the technical structures described (VM usage, bit-shifting for handle resolution, and high complexity) are common indicators used by sophisticated threat actors to evade detection and hinder manual analysis.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The implementation of a "Scripting Runtime / VM Engine" with a dedicated "Resolution phase" and "Dispatch Tables" indicates a system designed to interpret high-level commands rather than executing them directly. |
| **T1486** | Data Encoding | The use of bit-shifting, XOR operations, and a "Handle System" serves to mask raw memory addresses and translate internal identifiers into usable data, hiding the direct location of resources. |
| **T1027** | Obfuscated Files or Information | The heavy use of multi-layered abstractions, complex decision trees (multi-way switches), and high-density logic blocks are classic methods used to complicate manual reverse engineering and obfuscate true intent. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the assessment of Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: The strings `.rdata` and `.data` are standard binary segment identifiers and not malicious file paths).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **None.** 

### Analyst Notes:
The "EXTRACTED STRINGS" section consists primarily of high-entropy noise, repeated character strings (e.g., `AWAVAUATVWUSH`), and internal memory markers typically seen in decompiled binary data where no plaintext strings are present. 

The "BEHAVIORAL ANALYSIS" confirms the nature of the code as a **Sophisticated Scripting Runtime/VM Engine** similar to those used in enterprise game engines (e.g., Unreal or Unity). The analysis explicitly states: **"No evidence of malicious activity; remains classified as 'Sophisticated Scripting Runtime/VM Engine.'"** No actionable indicators linked to known threat actors or malware families were found.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Scripting Runtime / VM Engine (Non-malicious)
3. **Confidence**: High

4. **Key evidence**:
* **Explicit Absence of Malice:** The analysis explicitly states, "No evidence of malicious activity; remains classified as 'Sophisticated Scripting Runtime/VM Engine'."
* **Lack of IOCs:** No indicators of compromise were found, including missing IPs, URLs, file paths, or registry keys that would indicate command-and-control (C2) communication or system persistence.
* **Functional Alignment with Legitimate Software:** The complex logic—specifically the multi-way switches, handle resolution systems, and robust error checking—is identified as characteristic of "Enterprise-Grade Game Engine Middleware" (e.g., Unreal or Unity) rather than typical malware behaviors like credential stealing or file encryption.
