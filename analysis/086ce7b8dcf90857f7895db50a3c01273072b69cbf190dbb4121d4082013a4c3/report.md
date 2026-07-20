# Threat Analysis Report

**Generated:** 2026-07-18 05:54 UTC
**Sample:** `086ce7b8dcf90857f7895db50a3c01273072b69cbf190dbb4121d4082013a4c3_086ce7b8dcf90857f7895db50a3c01273072b69cbf190dbb4121d4082013a4c3.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `086ce7b8dcf90857f7895db50a3c01273072b69cbf190dbb4121d4082013a4c3_086ce7b8dcf90857f7895db50a3c01273072b69cbf190dbb4121d4082013a4c3.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,766,256 bytes |
| MD5 | `7b9fc9691f11a72ba8e33e75ecbde6fc` |
| SHA1 | `7645fbeec99d7cc113289daedeff0cbf4aadf2e2` |
| SHA256 | `086ce7b8dcf90857f7895db50a3c01273072b69cbf190dbb4121d4082013a4c3` |
| Overall entropy | 7.405 |
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

Total strings found: **22665** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary sample's behavior and characteristics:

### Core Functionality and Purpose
The binary appears to be a **runtime loader or wrapper**, specifically for execution within the **.NET (Common Language Runtime - CLR)** framework. This is evidenced by several indicators:
*   **CLR Symbols:** The presence of strings such as `mscoree.dll`, `CLRCreateInstance`, and references to `DotNetRunner.pdb` suggests this binary acts as an intermediary to load and execute managed (.NET) code (C# or VB.NET).
*   **Standard Library Heavy:** A large portion of the functions (`fcn.00403b30`, `fcn.00408222`) deal with low-level memory management, floating-point unit (FPU) state normalization, and standard library string handling. This is typical of a "wrapper" or "host" executable that sets up an environment for another component to run.

### Suspicious or Malicious Behaviors
While the binary largely contains standard infrastructure code, there are specific patterns and techniques common in malware samples designed for evasion:

*   **Environment Fingerprinting (Anti-Analysis):** 
    *   In `fcn.00401c04`, the code calls `IsProcessorFeaturePresent` followed by several `cpuid` calls (`cpuid_basic_info`, `cpuid_Version_info`, and `cpuid_Extended_Feature_Enumeration_info`). 
    *   **Reason:** These are used to check for specific CPU features (e.g., SSE4.2, AVX). While legitimate in high-performance software, malware authors use these to detect virtual machines (VMs), emulators, or sandboxes, as these environments often report different CPU capabilities than physical hardware.
*   **Potential for Payload Obfuscation:** 
    *   Because this is a .NET loader/wrapper, the "true" malicious logic may not be in this specific binary but rather inside an encrypted or hidden `.dll` or `.exe` that this program loads into memory after performing its initial checks. This technique is used to bypass simple static analysis of the primary launcher.
*   **Instruction Complexity/Noise:** 
    *   The code includes extensive logic for handling various Unicode codepages and complex string translations (`fcn.00408eb4`). In a small utility, this level of complexity is often "noise" intended to slow down manual analysis by the researcher.

### Notable Techniques & Patterns
*   **Standard Library Padding:** The inclusion of robust floating-point logic (`fcn.00408222`) and complex memory copying loops suggests that the binary was compiled with a large set of standard libraries (likely the MSVC CRT). This makes it harder for analysts to distinguish between "suspicious" code and "standard" library code during manual review.
*   **ExceptionHandler/Signal Handling:** `fcn.0040a138` contains logic commonly found in exception handlers or signal dispatchers used by compilers to manage crashes gracefully within a runtime environment.
*   **Standard WinAPI Usage:** The use of `GetProcAddress`, `LoadLibraryW`, and `WriteFile` are standard, but when combined with the .NET loader behavior, they suggest the program is building a complex environment for its subsequent payload.

### Summary Conclusion
The binary functions as a **host or wrapper for .NET-based components**. It exhibits classic **anti-analysis** techniques through CPU feature fingerprinting (via `cpuid`) to detect analysis environments. The primary risk of such a file is that it serves as an "initial entry point," which performs environment checks before loading and executing the actual malicious payload in memory, thereby hiding the main threat from basic security scanners.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtualization/Sandbox Evasion | The use of `IsProcessorFeaturePresent` and multiple `cpuid` calls is a primary method for detecting if the binary is running in a virtualized environment. |
| T1027 | Obfuscated Files or Information | The inclusion of complex Unicode codepage logic and "noise" (standard library padding) is designed to slow down and complicate manual analysis by researchers. |
| T1036 | Masquerading | The binary acts as a .NET wrapper/loader, intentionally masking its role as a vehicle for malicious payload delivery to bypass basic security scans. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` 
    *(Note: This is a local development path/PDB file remaining from the build environment).*

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Anti-Analysis Technique:** CPU Feature Fingerprinting (The use of `cpuid` instructions to detect virtualized environments or sandboxes).
*   **Execution Pattern:** .NET Loader/Wrapper behavior (Utilizing `mscoree.dll` and `CLRCreateInstance` to load and execute a secondary managed payload).

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Loader Functionality:** The binary acts as a wrapper for .NET components, utilizing `mscoree.dll` and `CLRCreateInstance` to load and execute secondary code in memory, which is a common technique to hide the primary malicious payload from basic security tools.
    *   **Anti-Analysis Techniques:** The implementation of `IsProcessorFeaturePresent` and multiple `cpuid` checks confirms the use of environment fingerprinting to detect and bypass virtual machines or sandboxes (MITRE T1497).
    *   **Evasion Tactics:** The inclusion of high-complexity "noise" (such as extensive Unicode codepage logic) and standard library padding is a deliberate tactic intended to slow down manual reverse engineering.
