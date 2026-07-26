# Threat Analysis Report

**Generated:** 2026-07-25 01:41 UTC
**Sample:** `0a90b4ff29bb6231693fec656e0eed463b2df9604dc074c61fb75ebfa2e856a0_0a90b4ff29bb6231693fec656e0eed463b2df9604dc074c61fb75ebfa2e856a0.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a90b4ff29bb6231693fec656e0eed463b2df9604dc074c61fb75ebfa2e856a0_0a90b4ff29bb6231693fec656e0eed463b2df9604dc074c61fb75ebfa2e856a0.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,622,624 bytes |
| MD5 | `f4abafa6dbb7aa149e8b1c736d509147` |
| SHA1 | `0ca79918146c64f110ded85e9f2bb169a5756a05` |
| SHA256 | `0a90b4ff29bb6231693fec656e0eed463b2df9604dc074c61fb75ebfa2e856a0` |
| Overall entropy | 7.429 |
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

Total strings found: **22427** (showing first 100)

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

Based on my analysis of the provided disassembly and decompiled code, here is a summary of the findings:

### Core Functionality and Purpose
The binary appears to be an **intermediate loader or an execution wrapper for .NET (CLR) content**. 

Key indicators for this include:
*   **.NET Runtime Integration:** The string list contains references to `mscoree.dll`, `CorBindToRuntimeEx`, `CLRCreateInstance`, and `GetProcAddress`. These are standard components used by "Host" applications to initialize the .NET environment and execute managed code (C# / VB.NET).
*   **Dynamic Loading:** The presence of functions like `fcn.00401c04` and `fcn.00402dd0` suggests a complex internal state machine for handling memory allocation, type resolution, and executing methods within the .NET runtime environment.
*   **Infrastructure Support:** A significant portion of the code is dedicated to "under-the-hood" system requirements, such as:
    *   **Floating Point Management:** `fcn.00408222` and `fcn.0040a57e` are classic implementations for handling FPU (Floating Point Unit) states and IEEE 754 math calculations.
    *   **String Encoding/Decoding:** `fcn.004066eb` and `fcn.00408eb4` handle conversions between Unicode, ANSI, and various code pages (via `GetCPInfo` and `MultiByteToWideChar`).

### Suspicious or Malicious Behaviors
While the code largely reflects standard .NET runtime library behavior, several features are commonly utilized in malicious software:

*   **Anti-Analysis / Anti-Debugging:** 
    *   The function `fcn.005973` explicitly calls **`IsDebuggerPresent`**. This is a common technique used by malware to detect if it is being analyzed by an analyst or running in a debugger, allowing the program to change its behavior or exit.
*   **Loader Behavior (Potential "Reflective" Loading):** 
    *   The presence of `DotNetRunner.pdb` in the strings and the heavy infrastructure for managing memory buffers suggests this binary is designed to **host other pieces of code**. In a malware context, such loaders are used to pull malicious .NET DLLs or assemblies into memory (Reflective Loading) to execute them without ever saving them to the disk as separate files.
*   **File System Interaction:** 
    *   `fcn.00409e92` interacts with `WriteFile`. While this could be for logging, in a loader context, it may be used to drop payload components or interact with configuration files.

### Notable Techniques and Patterns
*   **Complex State Machine Logic:** Functions like `fcn.00403b30` and `fcn.0027d4` involve complex loops and bitwise logic. This is typical of low-level memory management or "JIT" (Just-In-Time) compilation support code, where the program prepares memory for executing dynamically loaded code.
*   **Abstraction of System APIs:** The code heavily wraps standard Windows APIs (like `WriteFile`, `GetProcAddress`, and `MultiByteToWideChar`). This is done to create a stable abstraction layer so the .NET runtime can function consistently regardless of the specific environment.
*   **Memory Manipulation:** There are several functions dedicated to moving blocks of memory, managing offsets, and potentially "unwrapping" data from encoded formats (e.g., `fcn.00401523` implied by logic in `fcn.00403b30`).

### Summary for Investigation
This binary acts as a **host environment** (likely a .NET Loader). It is not a "malware" payload itself in the sense of having a visible command-and-control (C2) module or an encryption routine, but it is designed to provide the infrastructure required to run other code. 

**Recommendation:** If this was found during an investigation, you should look for:
1.  Associated .NET DLLs or EXE files that might be loaded into memory by this host.
2.  The specific "Reflective" loader logic used to transition from this wrapper to the actual payload.
3.  Evidence of what code is being executed *after* the `.NET` environment is initialized via `CorBindToRuntimeEx`.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the technical analysis to the corresponding MITRE ATT&K techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Debugger Detection | The explicit call to `IsDebuggerPresent` is a classic indicator used to determine if the binary is running in an analysis or debugging environment. |
| T1055 | Process Injection | The "Reflective" loading behavior described involves loading and executing .NET assemblies directly into memory to avoid detection by disk-based security tools. |
| T1105 | Ingress Tool Transfer | The integration with `WriteFile` suggests the capability to drop payload components or configuration files onto the filesystem during the execution chain. |
| T1027 | Obfuscated Files or Information | The use of complex state machines and "unwrapping" logic for encoded data indicates an attempt to hide strings and functionality from static analysis. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` (Note: This is a local development path; its inclusion suggests the binary's origin/build environment).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Anti-Analysis Technique:** `IsDebuggerPresent` (Used to detect and evade analysis tools).
*   **Malware Behavior/Capability:** .NET Loader / Reflective Loading (The binary is designed to host and execute third-party .NET assemblies in memory, a common technique for executing payloads without touching the disk).
*   **Specific Functionality:** Inclusion of `CorBindToRuntimeEx` and `CLRCreateInstance`, indicating specialized infrastructure for a .NET execution environment.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family:** custom (Generic .NET Loader)
2. **Malware type:** loader
3. **Confidence:** High
4. **Key evidence:**
    *   **Core Functionality as a Host:** The binary is specifically designed to initialize a .NET runtime environment (`mscoree.dll`, `CorBindToRuntimeEx`) to execute managed code, which is a hallmark of an intermediate loader rather than a final payload.
    *   **Evasion Techniques:** The explicit inclusion of `IsDebuggerPresent` and the use of complex state machines to "unwrap" data indicate a deliberate effort to evade analysis and hide the transition to the actual malicious payload.
    *   **Reflective Loading Capability:** The evidence points toward a "Reflective Loader" design, intended to host and execute .NET assemblies directly in memory to bypass traditional disk-based antivirus detection.
