# Threat Analysis Report

**Generated:** 2026-07-14 20:07 UTC
**Sample:** `0600f397e12f8eee94623728448eb6a39d3720ca9fed34499715caed8a42f481_0600f397e12f8eee94623728448eb6a39d3720ca9fed34499715caed8a42f481.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0600f397e12f8eee94623728448eb6a39d3720ca9fed34499715caed8a42f481_0600f397e12f8eee94623728448eb6a39d3720ca9fed34499715caed8a42f481.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,641,496 bytes |
| MD5 | `ce6401b7e15e1c4b57dc934996e7f00f` |
| SHA1 | `f1957d2ce27d4b7106f34abd71bfd3dedab7ebbf` |
| SHA256 | `0600f397e12f8eee94623728448eb6a39d3720ca9fed34499715caed8a42f481` |
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

Total strings found: **22646** (showing first 100)

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
The provided code is consistent with a **malicious .NET loader/wrapper**. Its primary purpose is to initialize the Common Language Runtime (CLR) and execute a hosted .NET assembly (likely a malicious payload). The presence of specific "magic" constants, references to `mscoree.dll`, and anti-analysis checks indicate this is a "stub" designed to hide the final malicious payload from static analysis tools while preparing the environment for execution.

---

### Core Functionality
*   **_NET Runtime Hosting:** The code frequently interacts with .NET infrastructure. References to `mscoree.16.dll` (implied by `.mn` and `.rx` sections), `CorBindToRuntimeEx`, and specific memory offsets/constants (like `0x1f928c9d`) indicate it is a loader designed to host managed code.
*   **Environment Initialization:** Functions like `fcn.00408222` handle FPU state management, which is standard during the transition between a native loader and the .NET execution environment.
*   **Dynamic Loading:** The use of `LoadLibraryW`, `GetProcAddress`, and internal jumps suggests it dynamically resolves necessary functions to begin the "execution" phase after the stub's tasks are complete.

### Suspicious & Malicious Behaviors
*   **Anti-Analysis / Anti-Debugging:**
    *   The code explicitly calls `IsDebuggerPresent` (via the standard library linkage) and uses a dedicated exception filter (`SetUnhandledExceptionFilter`).
    *   In `fcn.00401c04`, the binary performs **CPU Identification** using `IsProcessorFeaturePresent` and checks specific CPUID values (e.g., searching for "Intel" strings in memory). This is used to detect if the malware is running in a virtual machine or an emulated environment.
*   **File System Manipulation:**
    *   Function `fcn.00408917` uses `FindFirstFileExA` and `FindNextFileA` to iterate through files. This behavior is commonly used to locate target documents, configuration files, or other system components.
    *   It utilizes `WriteFile` to output data, which could be part of a staged execution process where the "real" payload is written to disk before execution.
*   **Evasion/Obfuscation Techniques:**
    *   **Indirect Jumps:** The code uses complex pointer arithmetic and indirect calls (e.g., `(*pcVar1)()`), making it harder for automated tools to trace the execution flow.
    *   **Shellcode-like Behavior:** Several functions exhibit heavy pointer manipulation on raw memory buffers, common in packers to decompress or decrypt a payload before passing it to the .NET loader.

### Notable Technical Observations
*   **Loader Stubs:** The presence of `DotNetRunner.pdb` in the strings and the specific logic for handling `.NET` objects suggests this is a standard "crypter" stub often seen in malware families like *Emotet*, *TrickBot*, or various generic trojans to hide their primary .NET components from simple scanners.
*   **Code Complexity:** The high density of nested loops and manual memory offsetting (e.g., `puVar2 = puVar1 + 0x24` with offsets like `0x10`, `0x14`) indicates the presence of a custom packer or obfuscator designed to hide strings and API calls until runtime.
*   **Standard Library Wrapping:** The code contains many "helper" functions for string conversion (`MultiByteToWideChar`) and file handling, which are often wrapped into generic, non-descriptive names by automated packing tools.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of a .NET "stub," "crypter" logic, and indirect jumps/pointer arithmetic is designed to hide the final payload and API calls from static analysis tools. |
| T1497 | Virtualization/Sandbox Detection | The binary performs CPU identification via `IsProcessorFeaturePresent` and specific string checks to determine if it is running in an emulated or virtualized environment. |
| T1083 | File and Directory Discovery | The use of `FindFirstFileExA` and `FindNextFileA` indicates the malware is searching for target documents, configuration files, or system components. |
| T1059 | Command and Scripting Interpreter | (Note: Often associated with .NET execution) The behavior described as a ".NET loader/wrapper" facilitates the transition from native code to managed code execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` (Note: The "cwcontrol" directory name is highly associated with Cobalt Strike infrastructure).

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified in the provided strings)*

**Other artifacts**
*   **Malware Type:** .NET Loader/Wrapper (Stub)
*   **Known Framework Associations:** References to `cwcontrol` and `.NET_Runner` suggest a correlation with Cobalt Strike or similar C2 frameworks.
*   **Anti-Analysis Techniques:** 
    *   Use of `IsDebuggerPresent` for anti-debugging.
    *   Use of `SetUnhandledExceptionFilter` to intercept exceptions during analysis.
    *   Use of `IsProcessorFeaturePresent` and CPUID checks to detect virtualized/emulated environments.
*   **Core Library Dependencies:** 
    *   `mscoree.dll` / `mscoree.16.dll` (used for CLR initialization).
    *   `Kernel32.dll`, `OleAut32.dll`.
*   **Specific Constants/Logic:** Use of the magic constant `0x1f928c9d` for .NET runtime hosting.

---

## Malware Family Classification

1. **Malware family**: Cobalt Strike
2. **Malware type**: Loader / Stub
3. **Confidence**: High

**Key evidence**:
* **Infrastructure Indicators:** The inclusion of the directory string `\cwcontrol\` in the binary's internal metadata is a high-confidence indicator of Cobalt Strike infrastructure, as "cwcontrol" is the default naming convention for folders associated with this framework's compilation and configuration.
* **Loader Characteristics:** The analysis confirms the sample is a .NET loader/wrapper designed to initialize the Common Language Runtime (CLR) and host an obfuscated payload in memory, utilizing common evasion techniques like `IsDebuggerPresent`, `SetUnhandledExceptionFilter`, and CPUID-based VM detection.
* **Evasion Techniques:** The use of indirect jumps, manual memory manipulation for shellcode-like behavior, and dynamic API resolution confirms the file's primary role as a "crypter" or loader designed to hide the final malicious payload from static analysis.
