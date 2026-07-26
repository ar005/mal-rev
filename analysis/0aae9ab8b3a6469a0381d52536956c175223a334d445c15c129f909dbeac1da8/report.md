# Threat Analysis Report

**Generated:** 2026-07-25 12:17 UTC
**Sample:** `0aae9ab8b3a6469a0381d52536956c175223a334d445c15c129f909dbeac1da8_0aae9ab8b3a6469a0381d52536956c175223a334d445c15c129f909dbeac1da8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0aae9ab8b3a6469a0381d52536956c175223a334d445c15c129f909dbeac1da8_0aae9ab8b3a6469a0381d52536956c175223a334d445c15c129f909dbeac1da8.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,777,488 bytes |
| MD5 | `9e3e9979d816dd5f549680c842cf6519` |
| SHA1 | `c9213b5a4165963a54923e034395366da960747f` |
| SHA256 | `0aae9ab8b3a6469a0381d52536956c175223a334d445c15c129f909dbeac1da8` |
| Overall entropy | 7.468 |
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
| `.rsrc` | 5,689,344 | 7.478 | ⚠️ Yes |
| `.reloc` | 4,096 | 6.301 | No |

### Imports

**mscoree.dll**: `CorBindToRuntimeEx`
**KERNEL32.dll**: `GetModuleFileNameA`, `DecodePointer`, `SizeofResource`, `LockResource`, `LoadLibraryW`, `LoadResource`, `FindResourceW`, `GetProcAddress`, `WriteConsoleW`, `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleCP`, `FlushFileBuffers`, `HeapReAlloc`, `HeapSize`
**OLEAUT32.dll**: `VariantInit`, `SafeArrayUnaccessData`, `SafeArrayCreateVector`, `SafeArrayDestroy`, `VariantClear`, `SafeArrayAccessData`

## Extracted Strings

Total strings found: **22617** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary sample:

### Core Functionality and Purpose
The code functions as a **Native-to-Managed Bridge** or a **Runtime Wrapper**, likely for a .NET-based application (evidenced by `mscoree.dll`, `CorBindToRuntimeEx`, and the `DotNetRunner` strings). 

Instead of containing direct "malicious" logic in these specific functions, it serves as the infrastructure to host and execute managed code. It handles the heavy lifting of environment preparation, such as:
*   **Floating-Point Unit (FPU) State Management:** Functions like `fcn.00408222` and `fcn.0040b692` are typical of a runtime's handling of FPU control words to ensure mathematical consistency across different threads or transitions between native and managed code.
*   **Math Library Support:** Functions like `fcn.0040a57e` perform complex floating-point arithmetic, which is common in standard libraries but also found in high-performance applications (like games or tools).
*   **String Encoding/Decoding:** `fcn.00408eb4` acts as a wrapper for Windows' multi-byte to wide-character conversion, ensuring that strings can be correctly processed across different system locales and encodings.

### Suspicious or Malicious Behaviors
While the provided snippet is largely "boilerplate" infrastructure code, there are several areas of interest common in advanced malware:

*   **Hardware/Environment Fingerprinting:** `fcn.00401c04` performs detailed CPU feature detection (using `IsProcessorFeaturePresent` and logic for AVX/SSE support). While used by legitimate apps to optimize performance, this is also a primary technique for **anti-analysis**, as it can be used to detect if the code is running in an emulated environment or on a specific set of hardware.
*   **Exception Handling:** The presence of `SetUnhandledExceptionFilter` and various "jump" tables suggests a robust error handling system. In malware, this is often used to intercept and suppress debuggers or display messages during a crash.
*   **Complex String/Path Parsing:** Functions like `fcn.004027d4` involve heavy logic for parsing paths (checking for `:`, `/`, `\`). This is common in the "preparation" phase of an infection where the binary determines its location or targets files on the filesystem.

### Notable Techniques and Patterns
*   **Managed/Native Hybridization:** The presence of `mscoree.dll` and `DotNetRunner` suggests that the primary payload is likely hidden within a .NET assembly, while this native code serves as the "loader" to initialize the environment and execute the managed logic.
*   **Abstraction Layers:** Much of the code (like `fcn.00403b30`) involves large switch tables or complex loops for memory management. This indicates the presence of a heavy runtime environment rather than a simple, standalone piece of malware.
*   **Obfuscation through Complexity:** The complexity of functions like `fcn.00402a2b` and `fcn.00405ee1` suggests that much of the high-level logic is abstracted away from the analyst by several layers of runtime calls.

### Summary
This sample appears to be a **loader or wrapper for a .NET application.** The specific functions provided are primarily focused on system compatibility (FPU state, CPU features, and string encoding). If this sample is part of a malware suite, the actual malicious behavior (e.g., exfiltration, keylogging) likely resides in the managed (.NET) layer rather than these native wrapper functions.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the relevant MITRE ATT&K techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Detection | The use of `IsProcessorFeaturePresent` and specific logic for AVX/SSE detection is a common method to identify if code is running in an emulated or analysis environment. |
| **T1027** | Obfuscated Files or Information | The report identifies "Abstraction Layers" and "Obfuscation through Complexity" as methods used to hide high-level logic from the analyst. |
| **T1083** | File and Directory Discovery | The complex parsing of paths (checking for `:`, `/`, `\`) indicates the malware is identifying its location or searching for specific targets on the filesystem. |
| **T1498** | Denial of Service (Potential) / Evasion via Exception Handling | While not a direct DOS, the use of `SetUnhandledExceptionFilter` to suppress debuggers/errors is a common tactic used to evade detection during execution. |

### Analyst Notes:
*   **Loader Logic:** The "Native-to-Managed" transition described suggests this binary acts as a **Loader**. While not a single unique technique, it follows the pattern of using a native wrapper (often for evasion) to host a .NET payload, which may hide the primary malicious intent from basic static analysis.
*   **Evasion Focus:** The high concentration of "preparation" and "infrastructure" behavior indicates that this specific component is designed to ensure successful execution while minimizing the fingerprint left by the underlying managed code.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None detected.

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` (Note: This is a developer path; the presence of "cwcontrol" and "DotNetRunner" may be used to identify the specific internal project or tool suite).

**Mutex names / Named pipes**
*   None detected.

**Hashes**
*   None detected.

**Other artifacts**
*   **Internal Project/Tool Names:** `cwcontrol`, `DotNetRunner` (Identified within file paths and behavioral descriptions).
*   **Runtime Infrastructure:** Presence of `.NET` runtime wrappers (`mscoree.dll`, `CorBindToRuntimeEx`) suggests the use of a managed code loader. 

---
**Analyst Note:** The provided sample appears to be a **loader/wrapper** for a .NET-based application. While no direct C2 infrastructure (IPs/URLs) was found in the text, the presence of specific internal project naming (e.g., `cwcontrol`) and high-level abstraction layers indicates that this component's role is environmental preparation and "staging" rather than the primary execution of malicious payloads.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High (for the role as a loader; Medium for the ultimate payload)
4. **Key evidence**:
    *   **Native-to-Managed Bridge:** The presence of `mscoree.dll`, `CorBindToRuntimeEx`, and "DotNetRunner" strings confirms the binary's primary function is to wrap and execute .NET managed code, a common technique to hide malicious logic from basic static analysis.
    *   **Anti-Analysis Features:** The implementation of T1497 (Virtualization/Sandbox Detection) via `IsProcessorFeaturePresent` and robust exception handling indicates an intentional effort to evade detection during the initial execution phase.
    *   **Infrastructure for Stealth:** The analyst's notes highlight "Obfuscation through Complexity" and "Abstraction Layers," suggesting that while this specific binary is a loader, it is designed to provide a stable, evasive environment for a secondary payload.
