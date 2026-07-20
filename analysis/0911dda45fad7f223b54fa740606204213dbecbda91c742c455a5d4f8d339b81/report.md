# Threat Analysis Report

**Generated:** 2026-07-19 11:49 UTC
**Sample:** `0911dda45fad7f223b54fa740606204213dbecbda91c742c455a5d4f8d339b81_0911dda45fad7f223b54fa740606204213dbecbda91c742c455a5d4f8d339b81.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0911dda45fad7f223b54fa740606204213dbecbda91c742c455a5d4f8d339b81_0911dda45fad7f223b54fa740606204213dbecbda91c742c455a5d4f8d339b81.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,662,264 bytes |
| MD5 | `de90bd5654d5cd7559406094fa05f224` |
| SHA1 | `201990b260a54d41fe5a50a7c3c901d33d9c68ca` |
| SHA256 | `0911dda45fad7f223b54fa740606204213dbecbda91c742c455a5d4f8d339b81` |
| Overall entropy | 7.428 |
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

Total strings found: **22729** (showing first 100)

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

### Analysis Summary
The provided binary sample appears to be a complex, potentially malicious loader or an agent (likely part of a larger framework given the presence of .NET-related metadata and extensive internal string handling logic). The code contains significant "guard" routines designed to detect analysis environments and ensure it is running on a physical machine before executing its primary payload.

### Core Functionality
*   **Heavy Data Processing:** A large portion of the code (e.g., `fcn.00403b30`) is dedicated to complex memory manipulation, buffer copying, and string processing. This suggests the binary processes significant amounts of data or manages a large internal state.
*   **Abstraction Layer:** The presence of many "glue" functions (like `fcn.00407f6f` and `fcn.00405e1`) indicates that this is likely an intermediate layer between a high-level language (like C#/.NET) and lower-level system calls, or it is a heavily wrapped set of library functions.
*   **File System Interaction:** The code includes logic for searching the filesystem (`FindFirstFileExA`, `FindNextFileA`) and performing multi-byte to wide-character conversions for pathing and file manipulation (`fcn.00408eb4`).

### Suspicious & Malicious Behaviors
The most notable features of this sample are its **anti-analysis** and **environment fingerprinting** capabilities:

*   **Anti-Debugging (Direct):** 
    *   Function `fcn.00405973` explicitly calls `IsDebuggerPresent()`. This is a standard technique to determine if the process is being monitored by a debugger.
    *   The same function sets an unhandled exception filter (`SetUnhandledExceptionFilter`). This is often used to intercept and manipulate exceptions in ways that can disrupt or bypass debugger behavior.

*   **Anti-Virtualization / Anti-Emulation (Fingerprinting):**
    *   Function `fcn.00401c04` uses the **CPUID** instruction (via `cpuid_basic_info`, `cpuid_Version_info`, and `cpuid_Extended_Feature_Enumeration_info`). It checks for specific CPU features and capabilities. This is a common technique to detect if the code is running inside a virtual machine or emulator, where certain high-end processor features may be absent or reported differently.
    *   The use of `IsProcessorFeaturePresent` suggests a check for advanced instruction sets (like SSE/AVX) which are often omitted or restricted in sandboxes.

*   **FPU State Checking:** 
    *   Function `fcn.00408222` performs complex checks on the **Floating Point Unit (FPU)** control and status words. It compares the current hardware state against a "known good" mask. This is used to detect if a debugger or an emulator has modified the processor's floating-point registers, which commonly happens when specialized debugging tools are active.

### Notable Techniques & Patterns
*   **Complex Buffer Management:** The extensive logic for buffer manipulation (e.g., `fcn.00403b30`) and repeated use of custom offsets suggest a sophisticated way to manage data that might be intended to obfuscate the actual strings or commands being used during the program's execution.
*   **Polymorphic/Complex Control Flow:** The high number of jumps, loops, and nested conditions in the decompiled code (especially in `fcn.00402a2b`) indicates a layer of complexity designed to hinder static analysis by making it difficult for an analyst to follow the logic path easily.
*   **Multi-Stage Logic:** The way "status codes" are checked at various points suggests that the program's behavior changes significantly based on whether it passes its internal checks (e.g., "Am I in a VM?", "Is there a debugger?"). If any check fails, the code may exit gracefully or enter a dummy loop to evade detection.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Debugger Detection | The binary explicitly calls `IsDebuggerPresent()` and employs `SetUnhandledExceptionFilter` to detect or intercept debugger interactions. |
| T1497 | Virtualization/Sandbox Evasion | The use of `CPUID`, `IsProcessorFeaturePresent`, and FPU state checking are standard methods used to determine if the code is running in a virtualized or emulated environment. |
| T1027 | Obfuscated Files or Information | Complex buffer management and high levels of nested logic/jumps are utilized to hide internal strings and complicate static analysis of the program's functionality. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` 
    *(Note: While this appears to be a developer's local build path, it is the only non-standard file path present in the strings.)*

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Framework Integration:** The presence of `.NET` related symbols and `mscoree.dll` indicates the binary functions as a wrapper or loader for .NET-based payloads.
*   **Anti-Analysis Techniques:** 
    *   Use of `CPUID` instructions to detect virtualized/emulated environments.
    *   FPU (Floating Point Unit) state checking to identify debugger intervention.
    *   Execution of `SetUnhandledExceptionFilter` and `IsDebuggerPresent` for anti-debugging.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High

**Key evidence**:
*   **Advanced Anti-Analysis Suite:** The sample employs a sophisticated array of evasion techniques, including `CPUID` instruction checking (to detect virtualization), FPU state validation (to detect debugger interference), and `IsDebuggerPresent` checks.
*   **Role as a Wrapper/Loader:** The presence of `.NET` metadata, `mscoree.dll` integration, and the "abstraction layer" logic indicates its primary purpose is to host or load .NET-based payloads for subsequent execution.
*   **Obfuscation & Complexity:** The heavy use of complex buffer management, intricate control flow loops, and manual string processing are characteristic of a loader designed to mask malicious intent from static analysis tools while preparing an environment for secondary stages.
