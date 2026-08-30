# Threat Analysis Report

**Generated:** 2026-08-23 07:14 UTC
**Sample:** `1151c11c4e2a407d9ac3fdbdaafd6ba876b700624109f4019d372e00c6e15692_1151c11c4e2a407d9ac3fdbdaafd6ba876b700624109f4019d372e00c6e15692.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1151c11c4e2a407d9ac3fdbdaafd6ba876b700624109f4019d372e00c6e15692_1151c11c4e2a407d9ac3fdbdaafd6ba876b700624109f4019d372e00c6e15692.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,672,400 bytes |
| MD5 | `f8789269ca9432c7d8eefd946d85d2fc` |
| SHA1 | `6fe7cb98d3b3bdc1db93f3babc6fb1e3a1b33b8e` |
| SHA256 | `1151c11c4e2a407d9ac3fdbdaafd6ba876b700624109f4019d372e00c6e15692` |
| Overall entropy | 7.434 |
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
| `.rsrc` | 5,474,816 | 7.45 | ⚠️ Yes |
| `.reloc` | 4,096 | 6.301 | No |

### Imports

**mscoree.dll**: `CorBindToRuntimeEx`
**KERNEL32.dll**: `GetModuleFileNameA`, `DecodePointer`, `SizeofResource`, `LockResource`, `LoadLibraryW`, `LoadResource`, `FindResourceW`, `GetProcAddress`, `WriteConsoleW`, `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleCP`, `FlushFileBuffers`, `HeapReAlloc`, `HeapSize`
**OLEAUT32.dll**: `VariantInit`, `SafeArrayUnaccessData`, `SafeArrayCreateVector`, `SafeArrayDestroy`, `VariantClear`, `SafeArrayAccessData`

## Extracted Strings

Total strings found: **22642** (showing first 100)

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

Based on the analysis of the provided disassembly and strings, here is a breakdown of the code's functionality and suspicious behaviors:

### Core Functionality
The binary appears to be a **loader or wrapper (stub)** for a secondary payload—specifically a **.NET-based component**. 

The presence of `.NET` runtime signatures (e.g., `mscoree.dll`, `CorBindToRuntimeEx`) in the strings, combined with the complexity of the low-level memory and string manipulation functions, indicates that this file is not the main "malware" logic but rather a protective layer designed to unpack, decompress, or initialize a .NET environment before launching the actual malicious payload.

### Suspicious & Malicious Behaviors
*   **Environment Fingerprinting (Anti-Analysis):** 
    *   The function `fcn.00401c04` specifically uses `IsProcessorFeaturePresent` and performs detailed calculations based on **CPUID instructions**. This is a common technique to detect if the code is running inside a Virtual Machine (VM), emulator, or under specific hardware configurations that indicate an analysis environment.
*   **Dynamic Loading of Modules:** 
    *   The inclusion of `LoadLibraryW` and `GetProcAddress` suggests the binary dynamically resolves its dependencies at runtime. This helps hide the "true" imports from static analysis tools.
*   **Hidden Execution (Loader Pattern):**
    *   The string `"DotNetRunner"` and the references to a custom path (`...\cwcontrol\Custom\DotNetRunner...`) suggest that the binary is designed to bypass traditional signature-based detection by wrapping a .NET assembly in a native C++ wrapper. This "Dual-Stage" execution makes it harder for automated sandboxes to flag the malicious logic because the core behavior only appears after the loader has executed.
*   **Complexity in String/Data Handling:**
    *   The extensive and complex logic within `fcn.00408eb4` (involving `MultiByteToWideChar`, `GetCPInfo`, and `WriteFile`) suggests it may be handling encoded data or decrypted configuration files. The fact that the code spends so much effort on character set conversions indicates it is preparing a buffer of instructions/data for another component to consume.

### Notable Techniques & Observations
*   **"Stolen" Library Code:** Much of the code (like `fcn.0040a138`, `fcn.00403b30`, and `fcn.0040a57e`) appears to be standard boilerplate for math libraries, FPU state management, or memory alignment. While not inherently malicious, their presence in a small binary often indicates "bloated" compilation where the author has included necessary library code directly into the file to minimize external dependencies.
*   **Manual Entry Point Management:** The `entry0` function shows complex branching and state-saving logic (`unaff_EBP`, `unaff_FS_OFFSET`). This is characteristic of a loader that sets up an environment before "hopping" execution over to the primary payload's memory space.
*   **Potential for Obfuscation:** The lack of meaningful human-readable strings (other than standard library artifacts) and the heavy use of offsets (e.g., `0x414000`) suggest a level of obfuscation meant to hinder manual analysis by making it difficult to trace data flow.

### Summary Recommendation
This binary is highly likely to be part of a **malware loader chain**. It performs environment checks to see if it's being analyzed and then prepares the system state (resolving libraries and preparing strings) to execute a .NET-based payload that would contain the main malicious logic (e.g., information theft, ransomware, or botnet communication).

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your report to the corresponding MITRE ATT&CK techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Evasion | The use of `IsProcessorFeaturePresent` and CPUID instructions is a direct attempt to detect if the code is running in a virtualized or analysis environment. |
| **T1106** | Dynamic Resolution | The use of `LoadLibraryW` and `GetProcAddress` indicates an attempt to hide the binary's true functionality by resolving imports at runtime instead of during compilation. |
| **T1027** | Obfuscated Executables | The "Loader" pattern, lack of human-readable strings, and use of a .NET wrapper are designed to hide malicious logic from signature-based detection. |
| **T1131** | Data Encoding | Complex logic involving `MultiByteToWideChar` and manual buffer management suggests that configuration data or instructions are being encoded/decoded during runtime. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` (Note: This is a developer directory path; while it points to the build environment rather than a target machine, it is a unique identifier for the source's structure).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified in the provided strings.*

**Other artifacts**
*   **Internal Project/Naming Identifiers:** `cwcontrol` (Found in file path; likely identifies the project or malware family).
*   **Loader Mechanism Identifier:** `DotNetRunner` (Identifies the specific loader type used to wrap the .NET payload).
*   **Known Logic Patterns:** 
    *   Use of `IsProcessorFeaturePresent` for environment fingerprinting/anti-VM.
    *   Execution of a multi-stage "Dual-Stage" load logic involving `mscoree.dll` and `CorBindToRuntimeEx`.

---

## Malware Family Classification

1. **Malware family**: Custom / Unknown (Note: While "cwcontrol" is identified as a project name, it does not currently map to a specific globally known threat actor's signature.)
2. **Malware type**: Loader (specifically a .NET wrapper/stub)
3. **Confidence**: High
4. **Key evidence**: 
    *   **Anti-Analysis Techniques:** The binary employs explicit environment fingerprinting (T1497) using `IsProcessorFeaturePresent` and CPUID instructions to detect virtual machines or sandboxes.
    *   **Dual-Stage Execution:** It acts as a "wrapper" for a .NET payload, utilizing `mscoree.dll` and `CorBindToRuntimeEx` to execute secondary malicious code while hiding the main logic from basic static analysis.
    *   **Evasive Programming:** The use of dynamic imports (`GetProcAddress`, `LoadLibraryW`) combined with intentional obfuscation (lack of human-readable strings) is a hallmark of loaders designed to bypass signature-based detection.
