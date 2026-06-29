# Threat Analysis Report

**Generated:** 2026-06-28 13:38 UTC
**Sample:** `02da37c3491fe7de822724a98738563f905ad0fddf2a11abb347946af9631496_02da37c3491fe7de822724a98738563f905ad0fddf2a11abb347946af9631496.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `02da37c3491fe7de822724a98738563f905ad0fddf2a11abb347946af9631496_02da37c3491fe7de822724a98738563f905ad0fddf2a11abb347946af9631496.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 1,054,208 bytes |
| MD5 | `bdede47213346f1986922e05ffffb623` |
| SHA1 | `0de257a633e68be4015752dcffab498528d0d7a3` |
| SHA256 | `02da37c3491fe7de822724a98738563f905ad0fddf2a11abb347946af9631496` |
| Overall entropy | 7.184 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779800265 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 546,816 | 6.545 | No |
| `.rdata` | 180,736 | 6.281 | No |
| `.data` | 4,096 | 1.994 | No |
| `.pdata` | 32,256 | 5.837 | No |
| `.rsrc` | 3,072 | 4.867 | No |
| `.reloc` | 1,536 | 4.404 | No |
| `.gfx` | 284,672 | 7.999 | ⚠️ Yes |

### Imports

**ADVAPI32.dll**: `GetTokenInformation`, `OpenProcessToken`, `RegisterEventSourceW`, `ReportEventW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `DeregisterEventSource`
**bcrypt.dll**: `BCryptGenRandom`
**KERNEL32.dll**: `InitializeCriticalSectionEx`, `EncodePointer`, `CloseHandle`, `CopyFileW`, `CreateEventExW`, `CreateFileW`, `CreateMutexW`, `DuplicateHandle`, `ExpandEnvironmentStringsW`, `FormatMessageW`, `GetConsoleOutputCP`, `GetCurrentProcess`, `GetCurrentProcessorNumberEx`, `GetCurrentThread`, `GetEnvironmentVariableW`
**ole32.dll**: `CoUninitialize`, `CoWaitForMultipleHandles`, `CoInitializeEx`, `CoGetApartmentType`
**api-ms-win-crt-math-l1-1-0.dll**: `log`, `__setusermatherr`
**api-ms-win-crt-string-l1-1-0.dll**: `strcmp`, `_stricmp`, `strcpy`, `strlen`, `strcpy_s`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__stdio_common_vsnprintf_s`, `_set_fmode`, `__p__commode`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_register_onexit_function`, `_initialize_onexit_table`, `terminate`, `_seh_filter_exe`, `_set_app_type`, `abort`, `_configure_wide_argv`, `_initialize_wide_environment`, `_get_initial_wide_environment`, `_initterm`, `_initterm_e`, `exit`, `_exit`, `__p___argc`, `__p___wargv`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`
**api-ms-win-crt-heap-l1-1-0.dll**: `free`, `_set_new_mode`, `calloc`, `_callnewh`, `malloc`

## Extracted Strings

Total strings found: **3312** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVWVSH
[^_A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
H[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
u(E86I
[^_A\A]A^A_]
UAWAVAUATWVSH
u(E86I
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
AWAVAUWVUSH
 []^_A]A^A_
AWAVWVUSH
([]^_A^A_
L9D$0t
L9D$0t
AWAVAUATWVUSH
H[]^_A\A]A^A_
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUWVSH
ep[^_A]A^A_]
ep[^_A]A^A_]
AVWVUSH
0[]^_A^
0[]^_A^
UAWAVAUATWVSH
[^_A\A]A^A_]
UAVWVSH
e@[^_A^]
e@[^_A^]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
AWAVAUWVUSH
 []^_A]A^A_
,.@:lzu
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
H[^_A\A]A^A_]
AWAVWVUSH
L9D$pt
x[]^_A^A_
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
h[^_A\A]A^A_]
AWAVAUATWVUSH
x[]^_A\A]A^A_
x[]^_A\A]A^A_
AWAVAUWVUSH
0[]^_A]A^A_
H9
tH
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140049fa0` | `0x140049fa0` | 243254 | ✓ |
| `fcn.140049ff0` | `0x140049ff0` | 243174 | ✓ |
| `fcn.140080c10` | `0x140080c10` | 229429 | ✓ |
| `fcn.1400492d0` | `0x1400492d0` | 228709 | ✓ |
| `fcn.140080c20` | `0x140080c20` | 222805 | ✓ |
| `fcn.140080c30` | `0x140080c30` | 221350 | ✓ |
| `fcn.140080a50` | `0x140080a50` | 220401 | ✓ |
| `fcn.140080ca0` | `0x140080ca0` | 218229 | ✓ |
| `fcn.14004c490` | `0x14004c490` | 216919 | ✓ |
| `fcn.14000805c` | `0x14000805c` | 216619 | ✓ |
| `fcn.14003c304` | `0x14003c304` | 203448 | ✓ |
| `fcn.140012de8` | `0x140012de8` | 166988 | ✓ |
| `fcn.140017b9c` | `0x140017b9c` | 150316 | ✓ |
| `fcn.14001c088` | `0x14001c088` | 131941 | ✓ |
| `fcn.14001c190` | `0x14001c190` | 131629 | ✓ |
| `fcn.14003c710` | `0x14003c710` | 108761 | ✓ |
| `fcn.14003c18e` | `0x14003c18e` | 101704 | ✓ |
| `fcn.14003c058` | `0x14003c058` | 101364 | ✓ |
| `fcn.14003c3f0` | `0x14003c3f0` | 79941 | ✓ |
| `fcn.14003fad0` | `0x14003fad0` | 50859 | ✓ |
| `fcn.14003f900` | `0x14003f900` | 50185 | ✓ |
| `fcn.14003c620` | `0x14003c620` | 48407 | ✓ |
| `fcn.14003c6b0` | `0x14003c6b0` | 45399 | ✓ |
| `fcn.140038910` | `0x140038910` | 41659 | ✓ |
| `fcn.14003d8c0` | `0x14003d8c0` | 39272 | ✓ |
| `fcn.14003e7b0` | `0x14003e7b0` | 36939 | ✓ |
| `fcn.14003e9a0` | `0x14003e9a0` | 36790 | ✓ |
| `fcn.140047fc0` | `0x140047fc0` | 33927 | ✓ |
| `fcn.14003fc90` | `0x14003fc90` | 33571 | ✓ |
| `fcn.140032e3c` | `0x140032e3c` | 26602 | ✓ |

### Decompiled Code Files

- [`code/fcn.14000805c.c`](code/fcn.14000805c.c)
- [`code/fcn.140012de8.c`](code/fcn.140012de8.c)
- [`code/fcn.140017b9c.c`](code/fcn.140017b9c.c)
- [`code/fcn.14001c088.c`](code/fcn.14001c088.c)
- [`code/fcn.14001c190.c`](code/fcn.14001c190.c)
- [`code/fcn.140032e3c.c`](code/fcn.140032e3c.c)
- [`code/fcn.140038910.c`](code/fcn.140038910.c)
- [`code/fcn.14003c058.c`](code/fcn.14003c058.c)
- [`code/fcn.14003c18e.c`](code/fcn.14003c18e.c)
- [`code/fcn.14003c304.c`](code/fcn.14003c304.c)
- [`code/fcn.14003c3f0.c`](code/fcn.14003c3f0.c)
- [`code/fcn.14003c620.c`](code/fcn.14003c620.c)
- [`code/fcn.14003c6b0.c`](code/fcn.14003c6b0.c)
- [`code/fcn.14003c710.c`](code/fcn.14003c710.c)
- [`code/fcn.14003d8c0.c`](code/fcn.14003d8c0.c)
- [`code/fcn.14003e7b0.c`](code/fcn.14003e7b0.c)
- [`code/fcn.14003e9a0.c`](code/fcn.14003e9a0.c)
- [`code/fcn.14003f900.c`](code/fcn.14003f900.c)
- [`code/fcn.14003fad0.c`](code/fcn.14003fad0.c)
- [`code/fcn.14003fc90.c`](code/fcn.14003fc90.c)
- [`code/fcn.140047fc0.c`](code/fcn.140047fc0.c)
- [`code/fcn.1400492d0.c`](code/fcn.1400492d0.c)
- [`code/fcn.140049fa0.c`](code/fcn.140049fa0.c)
- [`code/fcn.140049ff0.c`](code/fcn.140049ff0.c)
- [`code/fcn.14004c490.c`](code/fcn.14004c490.c)
- [`code/fcn.140080a50.c`](code/fcn.140080a50.c)
- [`code/fcn.140080c10.c`](code/fcn.140080c10.c)
- [`code/fcn.140080c20.c`](code/fcn.140080c20.c)
- [`code/fcn.140080c30.c`](code/fcn.140080c30.c)
- [`code/fcn.140080ca0.c`](code/fcn.140080ca0.c)

## Behavioral Analysis

Based on the provided disassembly, here is an analysis of the binary's behavior and characteristics:

### Core Functionality and Purpose
The code appears to be a sophisticated piece of malware, likely a **loader or a stage-1 dropper**. Its primary purpose seems to be environment validation (anti-analysis), ensuring it is running on a "real" machine before executing its main payload, and preparing the memory/execution environment for that payload through thread manipulation.

### Suspicious and Malicious Behaviors

*   **Anti-Analysis & Evasion Techniques:**
    *   **Environment Validation:** Function `fcn.14003d8c0` specifically targets systems used by security researchers and debuggers. It attempts to resolve `IsWow64Process2` and `QueueUserAPC2`. These are often checked to determine if the environment is a debugger or an emulator.
    *   **Anti-Debugging (Windows Versioning):** The use of `VerSetConditionMask` followed by `VerifyVersionInfoW` is a classic technique used to bypass anti-anti-debugging tools (like ScyllaHide). It checks for discrepancies in how the OS reports its version, which can reveal if a debugger is intercepting system calls.
    *   **Signature/String Obfuscation:** The large number of `fcn.14003f900` and `fcn.140080c10` types of functions suggest the binary handles complex internal data structures, likely to hide strings or configuration data from static analysis.

*   **Thread Manipulation / Process Injection:**
    *   **Thread Hijacking/Context Manipulation:** A highly suspicious pattern is found in `fcn.14003d8c0`. The code performs the following sequence:
        1.  `SuspendThread(iVar1)`
        2.  `GetThreadContext(...)`
        3.  Execution of a secondary function (`fcn.14003d8e0`) using the retrieved context.
        4.  `ResumeThread(iVar1)`
    *   This specific sequence (Suspend -> GetContext -> Modify Context -> Resume) is typical of **thread hijacking** or **process injection**. It allows the malware to inject a payload into a thread and modify its instruction pointer (EIP/RIP) to begin execution in a different context.

*   **Advanced Encryption / Data Processing:**
    *   **SIMD-Accelerated Cryptography:** Function `fcn.140012de8` is heavily optimized using **AVX2 instructions** (`vpord_avx`, `vpsubw_avx`, etc.). This level of optimization is rarely found in standard application software but is very common in high-performance encryption libraries (e.g., AES, ChaCha20) or custom hashing algorithms used to decrypt and decompress a malicious payload into memory.

### Notable Techniques & Patterns
*   **Dynamic API Resolution:** The code makes frequent use of `GetProcAddress` via internal wrappers (visible as the `_sym.imp.` calls), indicating it avoids importing many functions from the IAT to hide its capabilities from static scanners.
*   **Complex State Machine/Dispatching:** Several functions (`fcn.140049fa0`, `fcn.140049ff0`) act as dispatchers or switch tables, suggesting a modular architecture where different "tasks" are triggered based on internal state logic.
*   **Memory Management:** There is significant evidence of manual memory management and custom buffer handling (e.g., checking lengths, offsets, and performing bitwise operations on pointers), which suggests the malware handles its own decrypted code/data in private memory regions.

### Summary for Reporting:
This sample exhibits high-level complexity consistent with a professional threat actor's toolkit. It utilizes **anti-debugging techniques** (VerifyVersionInfoW) to detect analysis environments, **AVX-accelerated encryption routines** for payload deobfuscation, and **thread context manipulation** to perform injection or hijacking of other processes/threads.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtualized Environment | The malware uses `IsWow64Process2`, `QueryUserAPC2`, and `VerifyVersionInfoW` to detect if it is running in a debugger, emulator, or analysis sandbox. |
| T1027 | Obfuscated Resources | The use of complex internal data structures and AVX-accelerated encryption routines indicates an effort to hide strings, configuration data, and the main payload from static analysis. |
| T1055 | Process Injection | The specific sequence of `SuspendThread` $\rightarrow$ `GetThreadContext` $\rightarrow$ `ResumeThread` is a signature behavior for thread hijacking or injecting a payload into another process's context. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted list of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA-1, or SHA-256 hashes were present in the provided strings).

### **Other artifacts**
Because no static indicators (like IPs or file paths) were present in the raw strings, the following behavioral artifacts and TTPs (Tactics, Techniques, and Procedures) have been identified from the analysis:

*   **Anti-Analysis/Evasion Patterns:** 
    *   Usage of `VerifyVersionInfoW` to bypass anti-anti-debugging tools.
    *   Checks for `IsWow64Process2` and `QueueUserAPC2` to detect debugger environments.
*   **Injection Techniques:** 
    *   Thread Hijacking/Context Manipulation (Sequence: `SuspendThread` $\rightarrow$ `GetThreadContext` $\rightarrow$ Context Modification $\rightarrow$ `ResumeThread`).
*   **Cryptographic Artifacts:**
    *   Use of **AVX2 instructions** (`vpord_avx`, `vpsubw_avx`) for high-performance, likely custom, encryption/decryption routines.
*   **Obfuscation:** 
    *   Heavy use of dynamic API resolution via `GetProcAddress` to hide the Import Address Table (IAT).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Evasion:** The use of `VerifyVersionInfoW` and `IsWow64Process2` demonstrates sophisticated anti-analysis techniques designed to detect debuggers and sandboxes before executing the primary payload.
    *   **Thread Hijacking/Injection:** The specific sequence of `SuspendThread` $\rightarrow$ `GetThreadContext` $\rightarrow$ `ResumeThread` is a hallmark behavior for injecting malicious code into other processes or hijacking existing threads.
    *   **Advanced Cryptography:** The utilization of **AVX2 instructions** (`vpord_avx`, etc.) indicates a high-performance decryption routine, typically used by sophisticated loaders to deobfuscate and unpack secondary stages in memory.
