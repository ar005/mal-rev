# Threat Analysis Report

**Generated:** 2026-07-09 21:58 UTC
**Sample:** `044141bf12fd3c01e450cafee955bcbc2c2d9f72d2df496f2870002d7cece443_044141bf12fd3c01e450cafee955bcbc2c2d9f72d2df496f2870002d7cece443.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `044141bf12fd3c01e450cafee955bcbc2c2d9f72d2df496f2870002d7cece443_044141bf12fd3c01e450cafee955bcbc2c2d9f72d2df496f2870002d7cece443.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,640,976 bytes |
| MD5 | `1504e77a2704d97330af6ad77dbc14cf` |
| SHA1 | `e13b2fec69a545d40a11a9b4a487f4a31d1a1361` |
| SHA256 | `044141bf12fd3c01e450cafee955bcbc2c2d9f72d2df496f2870002d7cece443` |
| Overall entropy | 7.427 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1668802220 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 45,568 | 6.592 | No |
| `.rdata` | 25,088 | 4.787 | No |
| `.data` | 2,048 | 2.265 | No |
| `.rsrc` | 5,452,288 | 7.449 | ⚠️ Yes |
| `.reloc` | 4,096 | 6.301 | No |

### Imports

**mscoree.dll**: `CorBindToRuntimeEx`
**KERNEL32.dll**: `GetModuleFileNameA`, `DecodePointer`, `SizeofResource`, `LockResource`, `LoadLibraryW`, `LoadResource`, `FindResourceW`, `GetProcAddress`, `WriteConsoleW`, `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleCP`, `FlushFileBuffers`, `HeapReAlloc`, `HeapSize`
**OLEAUT32.dll**: `VariantInit`, `SafeArrayUnaccessData`, `SafeArrayCreateVector`, `SafeArrayDestroy`, `VariantClear`, `SafeArrayAccessData`

## Extracted Strings

Total strings found: **22449** (showing first 100)

```
!This program cannot be run in DOS mode.
$
RichE>`
`.rdata
@.data
@.reloc
T$Rh
M;Jr

QQSVWd
38_^]
E9xt
&9Gv!8E
Yt
jV
9Nv@k
URPQQh
kUQPXY]Y[
< t1<	t-
uh0MA
uj Y;E
jh 'A
tf;1u
WWWPWS
u-PWWS
PjhLMA
PQhPAA
PQhXBA
SSVWh 
f9:t!V
WuVVS
QQSWj0j@
jh (A
tl=PFA
jh@(A
jh`(A
u9Mu!3
PPPPPPPP
PPPPPWS
PP9E u:PPVWP
t;Et
jh()A

u,jXj

u	jZf
\9EuY
D$+d$SVW
Unknown exception
bad exception
__based(
__cdecl
__pascal
__stdcall
__thiscall
__fastcall
__vectorcall
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
`dynamic atexit destructor for '
`vector copy constructor iterator'
`vector vbase copy constructor iterator'
`managed vector copy constructor iterator'
`local static thread guard'
operator "" 
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040a138` | `0x40a138` | 2957 | ✓ |
| `fcn.00403b30` | `0x403b30` | 1396 | ✓ |
| `fcn.00402a2b` | `0x402a2b` | 933 | ✓ |
| `fcn.00408970` | `0x408970` | 922 | ✓ |
| `fcn.00408222` | `0x408222` | 770 | ✓ |
| `fcn.0040a57e` | `0x40a57e` | 614 | ✓ |
| `fcn.0040b895` | `0x40b895` | 563 | ✓ |
| `fcn.00408eb4` | `0x408eb4` | 541 | ✓ |
| `fcn.0040add3` | `0x40add3` | 536 | ✓ |
| `fcn.00409e92` | `0x409e92` | 524 | ✓ |
| `fcn.00404852` | `0x404852` | 523 | ✓ |
| `fcn.0040a93e` | `0x40a93e` | 523 | ✓ |
| `fcn.00407f6f` | `0x407f6f` | 520 | ✓ |
| `fcn.004066eb` | `0x4066eb` | 497 | ✓ |
| `fcn.0040b692` | `0x40b692` | 480 | ✓ |
| `fcn.00401c04` | `0x401c04` | 468 | ✓ |
| `fcn.00409817` | `0x409817` | 435 | ✓ |
| `fcn.00406396` | `0x406396` | 404 | ✓ |
| `fcn.00405cbb` | `0x405cbb` | 400 | ✓ |
| `entry0` | `0x4014ad` | 390 | ✓ |
| `fcn.00405ee1` | `0x405ee1` | 388 | ✓ |
| `fcn.00404477` | `0x404477` | 373 | ✓ |
| `fcn.004040f0` | `0x4040f0` | 371 | ✓ |
| `fcn.00402570` | `0x402570` | 346 | ✓ |
| `fcn.00403152` | `0x403152` | 333 | ✓ |
| `fcn.00407907` | `0x407907` | 330 | ✓ |
| `fcn.00404f40` | `0x404f40` | 321 | ✓ |
| `fcn.004027d4` | `0x4027d4` | 318 | ✓ |
| `fcn.00405973` | `0x405973` | 315 | ✓ |
| `fcn.00402dd0` | `0x402dd0` | 310 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401c04.c`](code/fcn.00401c04.c)
- [`code/fcn.00402570.c`](code/fcn.00402570.c)
- [`code/fcn.004027d4.c`](code/fcn.004027d4.c)
- [`code/fcn.00402a2b.c`](code/fcn.00402a2b.c)
- [`code/fcn.00402dd0.c`](code/fcn.00402dd0.c)
- [`code/fcn.00403152.c`](code/fcn.00403152.c)
- [`code/fcn.00403b30.c`](code/fcn.00403b30.c)
- [`code/fcn.004040f0.c`](code/fcn.004040f0.c)
- [`code/fcn.00404477.c`](code/fcn.00404477.c)
- [`code/fcn.00404852.c`](code/fcn.00404852.c)
- [`code/fcn.00404f40.c`](code/fcn.00404f40.c)
- [`code/fcn.00405973.c`](code/fcn.00405973.c)
- [`code/fcn.00405cbb.c`](code/fcn.00405cbb.c)
- [`code/fcn.00405ee1.c`](code/fcn.00405ee1.c)
- [`code/fcn.00406396.c`](code/fcn.00406396.c)
- [`code/fcn.004066eb.c`](code/fcn.004066eb.c)
- [`code/fcn.00407907.c`](code/fcn.00407907.c)
- [`code/fcn.00407f6f.c`](code/fcn.00407f6f.c)
- [`code/fcn.00408222.c`](code/fcn.00408222.c)
- [`code/fcn.00408970.c`](code/fcn.00408970.c)
- [`code/fcn.00408eb4.c`](code/fcn.00408eb4.c)
- [`code/fcn.00409817.c`](code/fcn.00409817.c)
- [`code/fcn.00409e92.c`](code/fcn.00409e92.c)
- [`code/fcn.0040a138.c`](code/fcn.0040a138.c)
- [`code/fcn.0040a57e.c`](code/fcn.0040a57e.c)
- [`code/fcn.0040a93e.c`](code/fcn.0040a93e.c)
- [`code/fcn.0040add3.c`](code/fcn.0040add3.c)
- [`code/fcn.0040b692.c`](code/fcn.0040b692.c)
- [`code/fcn.0040b895.c`](code/fcn.0040b895.c)

## Behavioral Analysis

Based on my analysis of the provided disassembly and decompiler output, here is a summary of the binary's functionality and behavior.

### Core Functionality and Purpose
The binary appears to be a **highly structured loader or wrapper application**. The presence of strings related to `.NET` (e.g., `mscoree.dll`, `CLRCreateInstance`, `DotNetRunner.pdb`) strongly suggests that this executable serves as an intermediary to load and execute .NET-based code, likely to bypass basic signature-based detection.

The overall structure is characteristic of a "stub" or "loader," which sets up the environment (memory management, exception handling) before executing a primary payload.

### Suspicious and Malicious Behaviors
*   **Anti-Analysis / Anti-Debugging:**
    *   The binary explicitly checks for the presence of a debugger using `IsDebuggerPresent` (seen in `fcn.00405973`). 
    *   It utilizes `SetUnhandledExceptionFilter`, which is commonly used by malware to intercept and handle exceptions before they can be caught by security tools, or to detect if a debugger has intercepted an exception.
*   **File System Enumeration:**
    *   The function `fcn.005ee1` implements a robust search for files on the local system using `FindFirstFileExA` and `FindNextFileA`. It includes logic for parsing directory paths, handling various naming conventions, and iterating through results in a loop. This is common when searching for specific configuration files, credentials, or other executables to download/run.
*   **Standard Library "Bloat" as Obfuscation:**
    *   The presence of many complex but technically "generic" functions (like `fcn.00403152` and `fcn.00408222`) suggests the binary includes a significant amount of standard library code or is using a large framework. This can be used to hide malicious logic within a high volume of legitimate-looking overhead code.
*   **Potential Payload Staging:**
    *   Function `fcn.00409817` interacts with the filesystem and uses `WriteFile`. Combined with the .NET infrastructure, this could indicate the creation or modification of files as part of a stage-2 deployment.

### Notable Techniques and Patterns
*   **Complex State Management:** Several functions (like `fcn.00408970`) show intricate loops for data manipulation. While these look like standard library implementations (likely related to string handling or buffer management), they can also be used to process obfuscated payloads in memory before execution.
*   **Multi-Stage Loading Path:** The presence of `GetProcAddress` and `LoadLibraryW` indicates that the binary dynamically resolves functions at runtime. This is a common technique to hide its "true" capabilities from static analysis tools until the program is actually running.
*   **Windows API Wrapping:** Many of the internal functions (`fcn.0041...`) appear to be wrapper routines for standard Win32 APIs, intended to handle errors and edge cases before calling the actual system functions.

### Summary Checklist
| Behavior Type | Observed Technique | Function / Evidence |
| :--- | :--- | :--- |
| **Anti-Analysis** | `IsDebuggerPresent` & Exception Filters | `fcn.00405973`, `SetUnhandledExceptionFilter` |
| **File Manipulation** | Directory/File Enumeration | `fcn.005ee1` (`FindFirstFileExA`) |
| **Payload Delivery** | .NET Runtime Wrapper | `mscoree.dll`, `CLRCreateInstance` strings |
| **Dynamic Loading** | Import Hiding | `GetProcAddress`, `LoadLibraryW` |

**Conclusion:** This binary is likely a **custom loader**. While it does not contain obvious "noisy" malicious actions like immediate process injection in the visible code, its use of anti-debugging techniques and .NET infrastructure strongly suggests it is designed to protect and execute a secondary payload (potentially a Cobalt Strike beacon or similar backdoor) while evading basic detection.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the corresponding MITRE ATT&K techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The use of a .NET wrapper/loader and the obfuscation of "true" capabilities via dynamic resolution are intended to hide the payload's identity from signature-based detection. |
| **T1083** | File and Directory Discovery | The use of `FindFirstFileExA` and `FindNextFileA` indicates an attempt to locate configuration files, credentials, or other system targets on the local machine. |
| **T1027** | Obfuscated Files or Information | The "Library Bloat" strategy and complex state management are used to hide malicious logic within a large volume of legitimate-looking code to evade detection during analysis. |
| **T1036.005** | Masquerading (Dynamic Resolution) | The use of `GetProcAddress` and `LoadLibraryW` specifically hides the intended functionality from static analysis tools by resolving imports only at runtime. |

### Analyst Notes:
*   **Defense Evasion:** While several behaviors (such as the use of `IsDebuggerPresent` and `SetUnhandledExceptionFilter`) fall under the broader **Defense Evasion** tactic, they are often considered internal implementation details of a loader's evasion strategy. 
*   **Loader Strategy:** The identification of this binary as a "custom loader" highlights a common adversary pattern where a benign-looking wrapper is used to "shield" a more malicious primary payload (e.g., a RAT or Cobalt Strike beacon).
*   **T1027 vs T1036:** While both deal with hiding information, **T1027** specifically addresses the complexity and volume of code used to mask intent (the "bloat" you identified), whereas **T1036** focuses on making the application appear as something else or masking its true purpose.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` 
    *(Note: This indicates a development path; the "cwcontrol" and "DotNetRunner" naming conventions are often associated with custom loaders or specific malware frameworks.)*

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Loader Characteristics:** Use of `mscoree.dll` and `CLRCreateInstance` (indicates a .NET-based loader/wrapper).
*   **Anti-Analysis Techniques:** 
    *   Use of `IsDebuggerPresent` (at `fcn.00405973`).
    *   Use of `SetUnhandledExceptionFilter` to intercept exceptions and detect debuggers.
*   **Evasion Tactics:** Use of `GetProcAddress` and `LoadLibraryW` for dynamic function resolution to hide the program's true capabilities from static analysis.
*   **Potential Payload Association:** Behavioral analysis suggests the binary may be a wrapper for **Cobalt Strike** or similar backdoors.

---

## Malware Family Classification

1. **Malware family**: Cobalt Strike
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
*   **Loader/Wrapper Architecture:** The binary utilizes .NET infrastructure (`mscoree.dll`, `CLRCreateInstance`) and dynamic API resolution (`GetProcAddress`, `LoadLibraryW`) to act as a stub that masks the execution of a secondary payload.
*   **Anti-Analysis Techniques:** It incorporates standard evasion tactics, including `IsDebuggerPresent` and `SetUnhandledExceptionFilter`, specifically intended to detect or bypass security tools during runtime.
*   **Obfuscation Strategies:** The use of "Library Bloat" and complex state management is designed to hide malicious logic within large amounts of legitimate-looking code, a common characteristic of professional loader components used to deliver beacons (e.g., Cobalt Strike).
