# Threat Analysis Report

**Generated:** 2026-08-31 16:56 UTC
**Sample:** `128c332d1be99551d813a7aa847b7dafb4860ed9a1737312c1521154d23f772c_128c332d1be99551d813a7aa847b7dafb4860ed9a1737312c1521154d23f772c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `128c332d1be99551d813a7aa847b7dafb4860ed9a1737312c1521154d23f772c_128c332d1be99551d813a7aa847b7dafb4860ed9a1737312c1521154d23f772c.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,678,304 bytes |
| MD5 | `57a06a4446171a01f7cb336e56c7b428` |
| SHA1 | `9464439cae707b8b7c2efbe066964c737468e310` |
| SHA256 | `128c332d1be99551d813a7aa847b7dafb4860ed9a1737312c1521154d23f772c` |
| Overall entropy | 7.43 |
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
| `.rsrc` | 5,469,696 | 7.45 | ⚠️ Yes |
| `.reloc` | 4,096 | 6.301 | No |

### Imports

**mscoree.dll**: `CorBindToRuntimeEx`
**KERNEL32.dll**: `GetModuleFileNameA`, `DecodePointer`, `SizeofResource`, `LockResource`, `LoadLibraryW`, `LoadResource`, `FindResourceW`, `GetProcAddress`, `WriteConsoleW`, `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleCP`, `FlushFileBuffers`, `HeapReAlloc`, `HeapSize`
**OLEAUT32.dll**: `VariantInit`, `SafeArrayUnaccessData`, `SafeArrayCreateVector`, `SafeArrayDestroy`, `VariantClear`, `SafeArrayAccessData`

## Extracted Strings

Total strings found: **22690** (showing first 100)

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

Based on the provided disassembly and decompiled C pseudocode, here is an analysis of the binary's functionality and behavior:

### Core Functionality and Purpose
The binary appears to be a **complex loader or "stub"** likely designed to bootstrap a .NET application. Several indicators point toward this:
*   **.NET Infrastructure:** The presence of `mscoree.dll`, `CorBindToRuntimeEx`, and the string `DotNetRunner` suggests it interacts with the Common Language Runtime (CLR).
*   **Resource Handling/Parsing:** Functions like `fcn.00408eb4` (wrapping `MultiByteToWideChar`) and `fcn.00406396` indicate heavy processing of internationalized strings or configuration data.
*   **Memory Management:** The code contains several large, complex functions (`fcn.00403b30`, `fcn.00408970`) that perform manual memory copying and buffer manipulation. These are characteristic of a "packer" or "loader" where the primary payload is decrypted/unpacked into memory before execution.

### Suspicious and Malicious Behaviors
The following behaviors were identified as suspicious or common in malware:

*   **Anti-Analysis / Anti-Debugging:** 
    *   **`IsDebuggerPresent`:** In `fcn.00405973`, the code explicitly calls `IsDebuggerPresent`. This is a classic check used to determine if the process is being monitored by a debugger, allowing the malware to alter its behavior or terminate if it detects analysis tools.
    *   **Exception Handling Manipulation:** The use of `SetUnhandledExceptionFilter` in the same vicinity suggests an attempt to intercept exceptions. This can be used to hide anti-debugging "traps" (e.g., INT 3 instructions) from standard monitoring tools.
*   **Complex Memory Operations:** Functions like `fcn.00408970` perform complex arithmetic on memory offsets and bitwise operations. While this can be legitimate for low-level software, in a loader context, it is often used to **obfuscate the location of the payload** or to "reorganize" code in memory to evade signature-based detection.
*   **File System Interaction:** The presence of `fcn.00409817` (a wrapper for `WriteFile`) and logic involving `FindFirstFileExA` suggests that the program interacts with the filesystem, potentially to drop a secondary payload or write decrypted configuration files to disk.

### Notable Techniques and Patterns
*   **Manual Buffer Management:** Instead of using standard library calls directly, several functions (e.g., `fcn.00403b30`) implement custom logic for memory copying and alignment. This is often done by malware authors to reduce the footprint of imported "standard" strings/functions that might trigger alerts.
*   **FPU State Management:** The function `fcn.00408222` handles FPU control words. While common in math-heavy software, it is also frequently found in "packer" stubs to ensure a consistent environment for the decrypted payload's execution.
*   **Hidden String/Data Processing:** The extensive use of `MultiByteToWideChar` and complex loops for string manipulation (seen in several functions) suggests the binary may be constructing commands or addresses dynamically at runtime rather than storing them as plaintext strings.

### Summary Checklist
*   **Process Injection:** Potential; heavy memory manipulation and .NET loading suggest a stage-based execution model.
*   **Persistence:** Not explicitly evidenced in this snippet, though file writing functions are present.
*   **Network Communication:** No direct network calls (e.g., `WinHttp`, `GetAddrInfo`) were seen in these specific functions, but they may be handled by the .NET component it loads.
*   **Anti-Analysis:** **Confirmed** (`IsDebuggerPresent`, `SetUnhandledExceptionFilter`).
*   **Obfuscation:** **Likely**, given the complexity of the memory manipulation routines and "junk" logic found in the disassembly.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1435** | Debugger Detection | The binary explicitly uses `IsDebuggerPresent` and `SetUnhandledExceptionFilter` to identify if it is being monitored by analysis tools. |
| **T1027** | Obfuscated Files or Information | Complex memory manipulation, FPU state management, and manual buffer handling are utilized to mask the primary payload's location and characteristics. |
| **T1036** | Dynamic Resolution | The use of custom logic for memory copying and alignment instead of standard library calls suggests an effort to resolve functions/data dynamically to avoid signature-based detection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` (Note: This is a hardcoded development path; while it identifies the build environment, it does not point to a standard system location).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Naming Convention/Strings:** `DotNetRunner` (Identified as a core component name used in the loader logic and file paths).
*   **Internal Project Identifiers:** `cwcontrol` (Found within internal path strings).
*   **Behavioral Indicators:** 
    *   Use of `IsDebuggerPresent` (Anti-debugging technique).
    *   Use of `SetUnhandledExceptionFilter` (Potential anti-analysis/exception handling manipulation).
    *   Utilization of `.NET` runtime libraries (`mscoree.dll`, `CLRCreateInstance`) to facilitate a "loader" or "stub" behavior for an underlying payload.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Execution of a .NET Payload:** The binary explicitly interacts with `mscoree.dll` and uses `DotNetRunner` logic to bootstrap a .NET-based payload into memory, which is the primary characteristic of a "stub" or loader.
*   **Anti-Analysis Tactics:** The implementation of `IsDebuggerPresent` and `SetUnhandledExceptionFilter` confirms intentional evasion attempts to detect analysis tools and hide from security researchers.
*   **Obfuscated Memory Manipulation:** The use of complex, non-standard memory arithmetic and manual buffer management indicates a design intended to mask the primary payload's location and signature during execution.
