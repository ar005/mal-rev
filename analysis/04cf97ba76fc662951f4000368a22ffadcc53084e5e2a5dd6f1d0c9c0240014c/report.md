# Threat Analysis Report

**Generated:** 2026-07-12 07:01 UTC
**Sample:** `04cf97ba76fc662951f4000368a22ffadcc53084e5e2a5dd6f1d0c9c0240014c_04cf97ba76fc662951f4000368a22ffadcc53084e5e2a5dd6f1d0c9c0240014c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04cf97ba76fc662951f4000368a22ffadcc53084e5e2a5dd6f1d0c9c0240014c_04cf97ba76fc662951f4000368a22ffadcc53084e5e2a5dd6f1d0c9c0240014c.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,642,920 bytes |
| MD5 | `98823de847446d0ffb86ee526e52219d` |
| SHA1 | `668268a0d5fde7be5d3553d410137ab87b6bc779` |
| SHA256 | `04cf97ba76fc662951f4000368a22ffadcc53084e5e2a5dd6f1d0c9c0240014c` |
| Overall entropy | 7.431 |
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

Total strings found: **22654** (showing first 100)

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

Based on the provided disassembly and string analysis, here is an analysis of the binary sample:

### Core Functionality and Purpose
The binary functions primarily as a **custom loader or "wrapper" for .NET-based payloads**. 

Several indicators point toward this:
*   **.NET Infrastructure:** The presence of strings such as `mscoree.dll`, `CorBindToRuntimeEx`, `CLRCreateInstance`, and the file path containing `DotNetRunner` strongly suggest that the primary purpose of this code is to host or bootstrap a .NET assembly within the process memory.
*   **State Machine/Interpreter logic:** Functions like `fcn.00402a2b` and `fcn.00407f6f` contain complex loop structures, pointer arithmetic, and bitwise manipulations on large data blocks. This is typical of an "interpreter" or a "virtual machine" stub that processes internal metadata (like the Common Intermediate Language - CIL) before executing it.
*   **Memory Management:** The code performs extensive manual memory manipulation to resolve addresses and manage offsets for what appear to be nested objects, rather than standard procedural logic.

### Suspicious or Malicious Behaviors
*   **Evasion/Anti-Analysis:** 
    *   The sample calls `IsDebuggerPresent` (seen in `fcn.00405973`). This is a classic anti-debugging technique used to detect if the code is being run in an analysis environment.
    *   It performs detailed CPU feature checks using `cpuid` related logic (`fcn.00401c04`), checking for specific processor features and instruction sets. This can be used to fingerprint the system or evade "sandboxes" that don't emulate certain hardware instructions correctly.
*   **Payload Decapsulation:** The complexity of functions like `fcn.00402a2b` and `fcn.00407f6f` suggests it is unpacking or decompressing an internal payload into a usable state in memory before passing execution to the next stage.
*   **Data Obfuscation:** The presence of "wrapper" functions (like `fcn.0040125e`) and large, complex switch/case logic for offset calculations indicates that it is abstracting typical Windows API calls through a custom layer to hinder automated analysis.

### Notable Techniques or Patterns
*   **Staged Execution:** The binary acts as a "Loader." Malicious actors use this technique to ensure that the actual malicious payload (the .NET assembly) never touches the disk in its raw form, making signature-based detection much harder.
*   **Complex Data Structure Parsing:** Several functions operate on very large arrays or structures using offsets (e.g., `puVar52[0x1f]`, `puVar52[0x10]`). This is characteristic of **Object Model Management**, where the code is navigating a tree of objects to find specific properties or methods for the next stage of execution.
*   **Environment Fingerprinting:** The use of `GetCPInfo` and `IsValidCodePage` in `fcn.004066eb`, combined with hardware-specific checks, indicates the binary wants to ensure it is running on a "standard" user machine before proceeding with more intensive operations.
*   **Instruction/State Transformation:** The repetitive use of bitwise masks and shift operations (e.g., `(uVar4 & 0x1f) ... >> uVar2`) suggests the code is processing encoded instructions or translating one type of data format into another to hide the true intent of the payload.

### Summary
This binary is a **sophisticated loader/stub**. Its primary role is to initialize a controlled environment, perform anti-debugging and hardware fingerprinting checks, and then "unpack" and host a .NET assembly in memory. The complexity of the code suggests it was designed specifically to evade static analysis by hiding the core malicious logic behind several layers of abstraction and translation.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the corresponding MITRE ATT&CK techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Executables | The use of "wrapper" functions, a custom interpreter/VM stub, and complex data transformation are designed to hide the underlying malicious logic from static analysis. |
| **T1620** | Reflective Loading | The binary acts as a loader that brings a .NET assembly into memory for execution without ever saving it to disk in its raw form. |
| **T1498** | [No direct ID] (Defense Evasion) | While not a single specific sub-technique, the use of `IsDebuggerPresent` and `cpuid` checks are standard techniques used to evade analysis environments. |
| **T1036** | Create Modules | The manual memory management and resolution of addresses for internal objects indicate the construction of modules/objects within the process space. |

***Note on Mapping Analysis:*** 
*   The "Interpreter/VM" logic mentioned in your report is a classic indicator of **T1027**, where malicious code (like CIL) is wrapped in a layer of abstraction to bypass signature-based detection.
*   The "Staged Execution" and the requirement that the payload never touches the disk point toward **T1620** (Reflective Loading), as it describes the methodology used to execute code directly from memory.
*   While there is no specific MITRE ID for "Anti-Debugging," these behaviors are categorized under the broader **Defense Evasion** tactic, specifically implemented through obfuscation techniques like **T1027**.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) and notable artifacts:

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` 
    *   *Note: While this is a .pdb (debug symbol) file, the presence of "cwcontrol" and "DotNetRunner" in the path suggests specific tooling or framework origins.*

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Anti-Analysis Techniques:** 
    *   `IsDebuggerPresent`: Used to detect if the sample is being run in a debugger/analysis environment.
    *   **CPU Fingerprinting:** Utilization of `cpuid` logic and `GetCPInfo` to verify hardware specifications and evade automated sandboxes.
*   **Environment Validation:** 
    *   `IsValidCodePage`: Used to ensure compatibility with the local system's locale before proceeding.
*   **Framework/Loader Artifacts:**
    *   `.NET Runtime Interactivity:` Presence of `mscoree.dll`, `CorBindToRuntimeEx`, and `CLRCreateInstance` indicates a loader designed to host .NET assemblies in memory.
    *   **Execution Logic:** The presence of "interpreter" patterns suggests the use of a custom stub to execute CIL (Common Intermediate Language) code within a non-standard environment.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
*   **Dedicated .NET Hosting:** The presence of `mscoree.dll`, `CorBindToRuntimeEx`, and `CLRCreateInstance` indicates the primary purpose is to host and execute a .NET assembly within memory (a classic "loader" architecture).
*   **Advanced Evasion Tactics:** The use of anti-debugging (`IsDebuggerPresent`) and hardware fingerprinting (`cpuid` / `GetCPInfo`) confirms it is designed to hide its activity from automated sandboxes and security researchers.
*   **Reflective Execution:** The identification of "Interpreter" logic and "Staged Execution" highlights that the binary's role is to serve as a wrapper, ensuring the actual malicious payload never touches the disk in its raw form (T1620).
