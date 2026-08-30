# Threat Analysis Report

**Generated:** 2026-08-23 20:25 UTC
**Sample:** `11a78dc6cd66955b18d8b541aa8deff11f91d7748e665f96a7b23ca628f73813_11a78dc6cd66955b18d8b541aa8deff11f91d7748e665f96a7b23ca628f73813.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11a78dc6cd66955b18d8b541aa8deff11f91d7748e665f96a7b23ca628f73813_11a78dc6cd66955b18d8b541aa8deff11f91d7748e665f96a7b23ca628f73813.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 15,076,408 bytes |
| MD5 | `422f25c62ea183d93d7b6af8f8374210` |
| SHA1 | `454fa9a857417276d80d7503fc0359c91b65eda1` |
| SHA256 | `11a78dc6cd66955b18d8b541aa8deff11f91d7748e665f96a7b23ca628f73813` |
| Overall entropy | 7.823 |
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
| `.rsrc` | 14,992,896 | 7.827 | ⚠️ Yes |
| `.reloc` | 4,096 | 6.301 | No |

### Imports

**mscoree.dll**: `CorBindToRuntimeEx`
**KERNEL32.dll**: `GetModuleFileNameA`, `DecodePointer`, `SizeofResource`, `LockResource`, `LoadLibraryW`, `LoadResource`, `FindResourceW`, `GetProcAddress`, `WriteConsoleW`, `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleCP`, `FlushFileBuffers`, `HeapReAlloc`, `HeapSize`
**OLEAUT32.dll**: `VariantInit`, `SafeArrayUnaccessData`, `SafeArrayCreateVector`, `SafeArrayDestroy`, `VariantClear`, `SafeArrayAccessData`

## Extracted Strings

Total strings found: **45193** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality:

### Core Functionality and Purpose
The sample appears to be a **sophisticated loader (or a stub)** designed to host and execute managed code (likely .NET). The presence of numerous internal runtime-like functions suggests it acts as a custom execution environment rather than a simple, linear malware script.

*   **Runtime Simulation:** The inclusion of strings like `mscoree.dll`, `CorBindToRuntimeEx`, and `DotNetRunner` indicate that the binary is likely intended to host an intermediate language (IL) or similar portable code format.
*   **Abstraction Layer:** Much of the code is dedicated to "heavy lifting" such as memory management, floating-point unit (FPU) state preservation (`fcn.00408222`), and complex internal data structure navigation. This allows a primary malicious payload to run inside this "container," making it harder for automated tools to find the actual malicious logic.

### Suspicious or Malicious Behaviors
While some behaviors are typical of standard software libraries, several are characteristic of malware designed to evade analysis:

*   **Anti-Analysis / Anti-Debugging:**
    *   The function `fcn.00405973` explicitly calls **`IsDebuggerPresent()`**. This is a classic technique used to determine if the sample is being run in a debugger or analysis environment.
    *   It also sets an **Unhandled Exception Filter** (`SetUnhandledExceptionFilter`). In malicious contexts, this is often used to intercept and suppress exceptions that would otherwise crash the program or alert researchers during execution.
*   **Complexity as Obfuscation:** The sheer volume of code dedicated to managing internal state (like FPU control words in `fcn.0040a138`) serves to "muddy" the analysis. It hides the actual malicious functionality behind thousands of lines of boilerplate logic that mimics a legitimate runtime environment.
*   **Manual Memory/Data Manipulation:** Functions like `fcn.00403b30` and `fcn.00408970` perform complex calculations on memory addresses and data structures. This is often seen in code meant to unpack or de-obfuscate a secondary payload before it is executed.

### Notable Techniques and Patterns
*   **Environment Validation:** The sample performs checks for hardware features (e.g., `IsProcessorFeaturePresent`). While sometimes used by legitimate software, malware uses this to ensure the environment supports specific CPU instructions required for their obfuscation or encryption routines.
*   **String/Path Manipulation:** There is significant logic involved in resolving paths and handling character sets (`MultiByteToWideChar`, `GetCPInfo`). This suggests that the loader might dynamically locate other components or resolve system dependencies locally to hide its true intent from simple static analysis.
*   **Stub Architecture:** The structure of the code indicates a "loader" pattern where this binary acts as a front-end, and the actual harmful behavior (e.g., data theft, credential logging) occurs in a separate piece of code that is loaded into memory and executed via this loader's infrastructure.

### Summary
This is not a simple script; it is a **sophisticated execution stub**. It uses common .NET-style runtime features to provide a "safe" environment for potentially malicious payload delivery. Its primary defensive mechanisms are **anti-debugging checks** and the use of an **unusually complex, high-overhead structure** designed to frustrate reverse engineering efforts by hiding the core logic deep within routine management code.

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis, the following MITRE ATT&CK techniques have been identified:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Debugger Detection | The binary explicitly calls `IsDebuggerPresent()` to identify if it is being executed within a debugger or analysis environment. |
| **T1027** | Obfuscated Files or Information | The use of "complexity as obfuscation" (e.g., FPU state preservation, heavy runtime-like boilerplate) and de-obfuscation routines are designed to hide the primary malicious logic from researchers. |

### Analysis Notes:
*   **T1027 (Obfuscated Files or Information)** covers several behaviors mentioned in your report: 
    *   The "Stub Architecture" used as a front-end for dynamic loading.
    *   The "Manual Memory/Data Manipulation" used to unpack secondary payloads.
    *   The use of "Environment Validation" (CPU instructions) to hide logic requirements behind complex code.
*   **T1036 (Debugger Detection)** specifically maps to the `IsDebuggerPresent()` check, which is a primary defensive evasion tactic for malware during the analysis phase.

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` 
    *(Note: While this is a developer-side build path, it identifies the project name "cwcontrol" and the specific component "DotNetRunner").*

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Core Component Name:** `DotNetRunner` (identified as a sophisticated execution stub).
*   **Anti-Analysis Indicators:** 
    *   Call to `IsDebuggerPresent()`
    *   Use of `SetUnhandledExceptionFilter` to mask crashes or detect debugger intervention.
*   **Runtime Simulation Artifacts:** The binary utilizes and references `mscoree.dll` and `CorBindToRuntimeEx` to simulate a .NET environment for payload execution.
*   **Behavioral Pattern:** Sophisticated loader/stub architecture designed to hide malicious logic behind standard-looking managed code environment overhead (e.g., FPU state preservation, complex memory manipulation).

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader (Stub)
3. **Confidence**: High

4. **Key evidence**:
*   **Infrastructure as a Wrapper:** The sample functions as a "stub" or intermediate loader that mimics a .NET runtime environment (utilizing `mscoree.dll` and `CorBindToRuntimeEx`). This is a classic tactic used to wrap malicious managed code in a complex layer of boilerplate logic, making it difficult for analysts to identify the actual payload during static analysis.
*   **Active Evasion Techniques:** The binary explicitly incorporates anti-debugging measures, such as calls to `IsDebuggerPresent()` and the setting of an `UnhandledExceptionFilter`. These are hallmark indicators of malware designed to detect and evade security research environments.
*   **Complexity Obfuscation:** The use of high-overhead operations (like FPU state management and complex memory/data manipulation) serves as a "noise" tactic. This is specifically intended to mask the transition between the loader's execution and the subsequent injection or activation of the primary malicious payload.
