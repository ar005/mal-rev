# Threat Analysis Report

**Generated:** 2026-07-19 12:27 UTC
**Sample:** `092d767d5794042a694447b05d6e2089c2834c0168206867a43bac5432880be8_092d767d5794042a694447b05d6e2089c2834c0168206867a43bac5432880be8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `092d767d5794042a694447b05d6e2089c2834c0168206867a43bac5432880be8_092d767d5794042a694447b05d6e2089c2834c0168206867a43bac5432880be8.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,622,504 bytes |
| MD5 | `59f7297f5e811cb6f3eb35b3765725d8` |
| SHA1 | `d2bad9d252eb9a5cc5bb39169915b1fbf99df2ff` |
| SHA256 | `092d767d5794042a694447b05d6e2089c2834c0168206867a43bac5432880be8` |
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

Total strings found: **22425** (showing first 100)

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

Based on the provided disassembly and strings, here is a technical analysis of the binary's behavior.

### **Core Functionality & Purpose**
The binary appears to be a **multi-stage loader or "packer"** designed to prepare an environment for a secondary payload (likely a .NET assembly). The presence of `mscoree.dll` and `CorBindToRuntimeEx` in the strings indicates that the final stage involves executing managed code (.NET/CLR). 

The sample includes significant logic dedicated to **environment validation**, **string obfuscation**, and **file system interaction**. It acts as a "wrapper" or "protector" meant to hide the primary functionality of the malware while ensuring it is running on a physical machine rather than in an analysis environment.

### **Suspicious & Malicious Behaved**
*   **Anti-Analysis / Anti-Debugging:** 
    *   **Debugger Detection:** The code explicitly calls `IsDebuggerPresent` (in `fcn.00405973`) to check for the presence of a debugger.
    *   **Exception Handling Manipulation:** It uses `SetUnhandledExceptionFilter` and `UnhandledExceptionFilter`. This is often used by malware to intercept exceptions that would normally crash the program, allowing it to perform "hidden" actions or detect if an exception was caused by a debugger's interference.
    *   **Environment Fingerprinting:** Function `fcn.00401c04` uses `IsProcessorFeaturePresent`, and functions like `cpuid_basic_info` and `cpuid_Version_info`. It checks for specific CPU features (e.g., "GenuineIntel" signatures) to determine if the code is running on a physical processor or inside an emulator/virtual machine.
    *   **FPU State Validation:** Functions like `fcn.00408222` and `fcn.0040a138` perform heavy checks against Floating Point Unit (FPU) control words. Many emulators and older sandboxes do not perfectly replicate the FPU state of a real processor; malware uses this to detect virtualization.

*   **File System Manipulation:**
    *   **Automated File Discovery:** Function `fcn.00405ee1` utilizes `FindFirstFileExA` and `FindNextFileA` to iterate through directories, likely searching for specific files or assets required by the payload.
    *   **Data Writing:** Several functions (`fcn.00408eb4`, `fcn.00409e92`) encapsulate `WriteFile` logic. This is often used to "drop" additional modules from an encrypted resource into a temporary folder for execution.

### **Notable Techniques & Patterns**
*   **Loader/Wrapper Architecture:** The integration of .NET components suggests the binary functions as a "stub." It handles the messy work (anti-debugging, deobfuscation) before handing control over to the actual malicious logic in the .NET environment.
*   **String Processing & Deobfuscation:** 
    *   Functions like `fcn.00407f6f` and `fcn.00404477` perform complex string manipulation, including handling escape characters (e.g., `\\`), quotes, and whitespace removal. This is often used to "reconstruct" system paths or command-line arguments that are stored in an encoded/obfuscated state within the binary's data sections.
*   **Complex Data Handling:** The code contains several functions (`fcn.00403b30`, `fcn.00402dd0`) involving heavy memory copying, buffer management, and multi-byte character conversions. This indicates a sophisticated approach to handling internal tables or data structures, likely for managing configuration settings or decryption keys.
*   **API Obfuscation/Hidden Imports:** While the assembly provided is high-level, the reliance on `GetProcAddress` and `LoadLibraryW` (seen in strings) suggests it may resolve its imports dynamically to hide its true capabilities from static analysis tools.

### **Summary of Findings**
| Feature | Observation | Risk Level |
| :--- | :--- | :--- |
| **Anti-Analysis** | Uses `IsDebuggerPresent`, `SetUnhandledExceptionFilter`, and CPU feature checks (CPUID) to detect VMs/debuggers. | High |
| **Evasion Tactics** | FPU state validation is used to distinguish between physical hardware and emulated environments. | High |
| **Payload Delivery** | Standard "loader" behavior; utilizes `.NET` runtime integration for final execution. | Medium |
| **Persistence/Drop** | Uses `FindFirstFile` and `WriteFile` suggesting it may drop additional components or move files on the system. | Medium |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtual Machine Evasion | The use of `IsDebuggerPresent`, CPUID checks (`GenuineIntel` signatures), and FPU state validation are specifically designed to detect and evade analysis environments. |
| T1027 | Obfuscated Executables | The complex string manipulation and deobfuscation routines used to reconstruct paths and configuration data help hide the malware's intent from static analysis. |
| T1083 | File and Directory Discovery | The use of `FindFirstFileExA` and `FindNextFileA` indicates an attempt to locate specific files, assets, or system information required for execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Several items in the "Strings" section were excluded as they are standard Windows system files (e.g., `KERNEL32.dll`, `mscoree.dll`) or generic programming artifacts.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` (Note: While this is a build-path artifact, the presence of "cwcontrol" and "DotNetRunner" provides internal naming used by the threat actor/developer).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Internal Project Names:** `cwcontrol`, `DotNetRunner` (Identified via file path strings).
*   **Anti-Analysis Techniques:** 
    *   CPUID-based hardware checks (e.g., `cpuid_basic_info`, `cpuid_Version_info`).
    *   FPU state validation to detect emulators.
    *   `IsDebuggerPresent` checks.
    *   Usage of `SetUnhandledExceptionFilter` for exception handling manipulation.
*   **Payload Delivery:** The binary acts as a **.NET loader/stub**, specifically utilizing `.NET` runtime integration (`mscoree.dll`) to execute secondary payloads.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
*   **Multi-stage Loader Architecture:** The binary specifically integrates `mscoree.dll` and follows a "loader/wrapper" pattern, designed to bypass initial security layers and prepare the environment for a secondary .NET assembly.
*   **Sophisticated Anti-Analysis:** It utilizes high-level evasion techniques including CPUID instruction checking (to detect virtual machines), FPU state validation, and `IsDebuggerPresent` checks to ensure it is running on a physical machine before executing its payload.
*   **Staged Execution & File Manipulation:** The use of `WriteFile` and `FindFirstFileExA` indicates the binary is designed to drop or manage additional components, typical of loaders that unpack malicious modules into temporary directories for execution.
