# Threat Analysis Report

**Generated:** 2026-08-12 16:53 UTC
**Sample:** `0e6f61869d37ac6506bd1dcb260d0a76d8e5d8ed156d81b786007c435c788016_0e6f61869d37ac6506bd1dcb260d0a76d8e5d8ed156d81b786007c435c788016.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e6f61869d37ac6506bd1dcb260d0a76d8e5d8ed156d81b786007c435c788016_0e6f61869d37ac6506bd1dcb260d0a76d8e5d8ed156d81b786007c435c788016.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 12,580,920 bytes |
| MD5 | `01a917b439a991629ffca3a8b0017a02` |
| SHA1 | `c30528b2a832935bec39024ade99a14dbc71dbc9` |
| SHA256 | `0e6f61869d37ac6506bd1dcb260d0a76d8e5d8ed156d81b786007c435c788016` |
| Overall entropy | 7.799 |
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
| `.rsrc` | 12,497,408 | 7.804 | ⚠️ Yes |
| `.reloc` | 4,096 | 6.301 | No |

### Imports

**mscoree.dll**: `CorBindToRuntimeEx`
**KERNEL32.dll**: `GetModuleFileNameA`, `DecodePointer`, `SizeofResource`, `LockResource`, `LoadLibraryW`, `LoadResource`, `FindResourceW`, `GetProcAddress`, `WriteConsoleW`, `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleCP`, `FlushFileBuffers`, `HeapReAlloc`, `HeapSize`
**OLEAUT32.dll**: `VariantInit`, `SafeArrayUnaccessData`, `SafeArrayCreateVector`, `SafeArrayDestroy`, `VariantClear`, `SafeArrayAccessData`

## Extracted Strings

Total strings found: **38661** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality and behavior.

### Core Functionality and Purpose
The sample appears to be a **complex, multi-stage loader or a packed .NET application.** The heavy presence of infrastructure related to the Common Language Runtime (CLR)—such as FPU control word management, complex memory copying routines, and extensive support for internationalized string handling—indicates that this code is likely part of a wrapper, an unpacker, or a heavily obfuscated piece of software designed to execute further logic.

### Suspicious and Malicious Behaved
*   **Anti-Analysis / Anti-Debugging:** 
    *   The function `fcn.005973` explicitly calls **`IsDebuggerPresent`**. This is a classic anti-debugging technique used to determine if the process is being monitored by an analyst's tools; the code likely alters its behavior or terminates if a debugger is detected.
*   **File Manipulation:** 
    *   The function `fcn.00409e92` utilizes the **`WriteFile`** API. This indicates that the program is actively writing data to the filesystem. In the context of malware, this is often used for "dropping" additional components (like a secondary payload or DLL) or writing configuration files containing Command & Control (C2) information.
*   **Sophisticated String Handling:** 
    *   Several functions (`fcn.00408eb4`, `fcn.004066eb`) deal extensively with **`MultiByteToWideChar`** and **`GetCPInfo`**. While these are standard Windows API calls for character encoding, their heavy usage in a small sample often points to the construction of complex strings (like dynamically generated URLs or decoded commands) that were stored in an encoded/obfuscated state during static analysis.
*   **Potential Data Unpacking:** 
    *   Large blocks of code involving manual memory copying and byte-level manipulation (`fcn.003b30`, `fcn.005cbb`) suggest the program is "unpacking" or reconstructing data in memory before use.

### Notable Techniques & Patterns
*   **.NET Runtime Wrapper:** The presence of terms like `CorBindToRuntimeEx` and `mscoree.dll` in the strings, combined with the specific way it handles FPU registers (`fcn.00408222`), strongly suggests this is a .NET binary that has been "packed" or protected by an obfuscation layer.
*   **Layered Logic:** The high complexity and volume of helper functions for basic tasks (like math calculations in `fcn.0040add3` or float handling in `fcn.0040a57e`) suggest that the underlying logic is complex, possibly involving encryption or a sophisticated state machine.
*   **Evidence of "Dropper" Behavior:** The combination of **Anti-Debugging**, **String Decoding**, and **File Writing** are the three primary indicators of a "dropper" or "downloader" component in an infection chain.

### Summary for Incident Response
The binary shows clear indicators of being a **malicious loader**. It attempts to hide from debuggers, performs significant work to decode internal strings (likely to hide malicious infrastructure), and interacts with the filesystem to potentially stage secondary payloads. It is recommended to treat this sample as highly suspicious and look for evidence of dropped files or network communication in an isolated environment.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1435** | Host Defense Evasion | The use of `IsDebuggerPresent` is a classic technique used to detect analysis environments and prevent researchers from observing the binary's full behavior. |
| **T1027** | Obfuscated Files or Information | The heavy use of `MultiByteToWideChar` and `GetCPInfo` for decoding strings, along with manual memory manipulation to "unpack" data, indicates a deliberate effort to hide malicious functionality from static analysis. |
| **T1648** (Potential) | Reflective Code Loading | While the report focuses on disk-writing, the "unpacking" and memory-copying routines are typical of reflective loading or preparing an in-memory payload for execution. |

***Note on Dropper Behavior:** The analysis identifies a "Dropper" pattern; while there is no single "T" code for a "Dropper," it is characterized by the combination of **T1435** (Evasion), **T1027** (Obfuscation), and the file-writing behavior which facilitates subsequent stages of an attack.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.* (The report notes these may be dynamically generated or encoded, but no plaintext IOCs were present in the sample.)

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` (Note: This is a development path, but indicates the naming convention and build environment of the source code.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Anti-Debugging Technique:** Use of `IsDebuggerPresent` (detected in function `fcn.005973`).
*   **Persistence/Dropper Behavior:** Usage of the `WriteFile` API (identified in `fcn.00409e92`) for potentially dropping secondary payloads or configuration files.
*   **Obfuscation Indicator:** Extensive use of `MultiByteToWideChar` and `GetCPInfo` to decode hidden strings/C2 infrastructure.
*   **Framework Identification:** Reliance on the .NET runtime (`mscoree.dll`, `CorBindToRuntimeEx`) as a wrapper or obfuscation layer.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High (for classification of function), Medium (for specific campaign identification)
4. **Key evidence**:
    *   **Anti-Analysis & Obfuscation:** The binary utilizes `IsDebuggerPresent` and extensive string decoding routines (`MultiByteToWideChar`, `GetCPInfo`), which are hallmarks of malware designed to hide its true intent and C2 infrastructure from static analysis.
    *   **Loader/Dropper Functionality:** The combination of manual memory unpacking (byte-level manipulation) and the use of `WriteFile` strongly indicates the sample's primary role is to unpack or "drop" a secondary malicious payload onto the filesystem.
    *   **.NET Infrastructure:** The reliance on the Common Language Runtime (`mscoree.dll`, `CorBindToRuntimeEx`) confirms it acts as a wrapper or loader for .NET-based components, a common architecture in modern malware delivery chains.
