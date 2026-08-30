# Threat Analysis Report

**Generated:** 2026-08-25 00:29 UTC
**Sample:** `122789db14d04b78b14c224259ab48f0489e98aa5255fd5bd6dff5c0be241b2f_122789db14d04b78b14c224259ab48f0489e98aa5255fd5bd6dff5c0be241b2f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `122789db14d04b78b14c224259ab48f0489e98aa5255fd5bd6dff5c0be241b2f_122789db14d04b78b14c224259ab48f0489e98aa5255fd5bd6dff5c0be241b2f.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 9 sections |
| Size | 328,704 bytes |
| MD5 | `e2b3ec8e6062a59e24f7d907b3fbad76` |
| SHA1 | `e5315454f94d0866235c476f790280b8be7001f8` |
| SHA256 | `122789db14d04b78b14c224259ab48f0489e98aa5255fd5bd6dff5c0be241b2f` |
| Overall entropy | 7.455 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 8,704 | 6.01 | No |
| `.data` | 310,784 | 7.455 | ⚠️ Yes |
| `.rdata` | 2,560 | 4.46 | No |
| `.pdata` | 1,024 | 3.231 | No |
| `.xdata` | 1,024 | 2.634 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 2,560 | 3.967 | No |
| `.CRT` | 512 | 0.271 | No |
| `.tls` | 512 | -0.0 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `ConnectNamedPipe`, `CreateFileA`, `CreateNamedPipeA`, `CreateThread`, `DeleteCriticalSection`, `EnterCriticalSection`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleHandleA`, `GetProcAddress`, `GetStartupInfoA`, `GetSystemTimeAsFileTime`
**msvcrt.dll**: `__C_specific_handler`, `__getmainargs`, `__initenv`, `__iob_func`, `__lconv_init`, `__set_app_type`, `__setusermatherr`, `_acmdln`, `_amsg_exit`, `_cexit`, `_fmode`, `_initterm`, `_onexit`, `abort`, `calloc`

## Extracted Strings

Total strings found: **643** (showing first 100)

```
!This program cannot be run in DOS mode.
$
P`.data
.rdata
`@.pdata
0@.xdata
0@.bss
.idata
AUATUWVSH
[^_]A\A]
[^_]A\A]
ATUWVSH
@[^_]A\
ATWVSH
X[^_A\
ATWVSH
X[^_A\
ATUWVSH
0[^_]A\
0[^_]A\
ATUWVSH
P[^_]A\
P[^_]A\
UAWAVAUATWVSH
[^_A\A]A^A_]
ATUWVSH
 [^_]A\
ATWVSH
([^_A\H
tNHcA<H
tTIcB<L
t	HcA<
tCHcA<H
@' t	M
tKIcA<L
tSIcK<L
,%6^>V/|
|W\84#t
V9\6U;
s-_\8$#|
WL946
E,pY>)
VL?$6
|7\8,#,
VL(L8
VL(t8
|_\8,#t
|w\8#|
|W\8$#L
|?]8^F
#$:#<
|W\:,#\
P8,#8
{^F7ak
{ZF'bk
{ZC'kk
{ZC'K{
{UF7fk
{UC'c{
s-e\2^
|?\8,#T
K`q;XS
[W;T7UL
s-p\>]
s-\\>]
1W;T7UL
P:4#4[i

?\>7V:
?\>7V:
s`F/x*
|o\8$#d
|/\:#4
]8VB's
s-+]8
8\0<#T
^,%V9\>
s-#\8#\
@F/q/vQ
\8$#p
\8$#p
\>?U8
h, \>%
V>TGU:
|G\8$#\
RF/q/aU8
|7\84#,
|7\8,#,
|o\8,#d
|_\>#4
4P8_B'a
|7\8,#,
-rtZ7
/F%,X8
|G\8$#\
X8/P8
B/~%>Q
=hU>#
\8,#,:#
|W\8,#L
|7\8,#,
|?\8,#T
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00402310` | `0x402310` | 2958 | ✓ |
| `fcn.004018e0` | `0x4018e0` | 1066 | ✓ |
| `fcn.00401180` | `0x401180` | 832 | ✓ |
| `fcn.00401fd0` | `0x401fd0` | 817 | ✓ |
| `fcn.00401dc0` | `0x401dc0` | 528 | ✓ |
| `fcn.004024e0` | `0x4024e0` | 250 | ✓ |
| `fcn.004017f8` | `0x4017f8` | 240 | ✓ |
| `fcn.00402910` | `0x402910` | 224 | ✓ |
| `fcn.00401990` | `0x401990` | 214 | ✓ |
| `fcn.00401630` | `0x401630` | 182 | ✓ |
| `fcn.00401704` | `0x401704` | 162 | ✓ |
| `fcn.00402a80` | `0x402a80` | 159 | ✓ |
| `fcn.00401595` | `0x401595` | 152 | ✓ |
| `entry1` | `0x401ba0` | 129 | ✓ |
| `fcn.00402b20` | `0x402b20` | 129 | ✓ |
| `fcn.00401d50` | `0x401d50` | 112 | ✓ |
| `fcn.00402be0` | `0x402be0` | 108 | ✓ |
| `fcn.00402790` | `0x402790` | 107 | ✓ |
| `fcn.00401563` | `0x401563` | 50 | ✓ |
| `fcn.00402dd0` | `0x402dd0` | 50 | ✓ |
| `entry2` | `0x401b70` | 47 | ✓ |
| `fcn.00402bb0` | `0x402bb0` | 43 | ✓ |
| `fcn.00402c50` | `0x402c50` | 40 | ✓ |
| `entry0` | `0x4014c0` | 34 | ✓ |
| `fcn.00403040` | `0x403040` | 33 | ✓ |
| `fcn.00401950` | `0x401950` | 31 | ✓ |
| `fcn.00402ec0` | `0x402ec0` | 31 | ✓ |
| `fcn.004029f0` | `0x4029f0` | 30 | ✓ |
| `fcn.00402f10` | `0x402f10` | 11 | ✓ |
| `fcn.00402ef0` | `0x402ef0` | 11 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/entry1.c`](code/entry1.c)
- [`code/entry2.c`](code/entry2.c)
- [`code/fcn.00401180.c`](code/fcn.00401180.c)
- [`code/fcn.00401563.c`](code/fcn.00401563.c)
- [`code/fcn.00401595.c`](code/fcn.00401595.c)
- [`code/fcn.00401630.c`](code/fcn.00401630.c)
- [`code/fcn.00401704.c`](code/fcn.00401704.c)
- [`code/fcn.004017f8.c`](code/fcn.004017f8.c)
- [`code/fcn.004018e0.c`](code/fcn.004018e0.c)
- [`code/fcn.00401950.c`](code/fcn.00401950.c)
- [`code/fcn.00401990.c`](code/fcn.00401990.c)
- [`code/fcn.00401d50.c`](code/fcn.00401d50.c)
- [`code/fcn.00401dc0.c`](code/fcn.00401dc0.c)
- [`code/fcn.00401fd0.c`](code/fcn.00401fd0.c)
- [`code/fcn.00402310.c`](code/fcn.00402310.c)
- [`code/fcn.004024e0.c`](code/fcn.004024e0.c)
- [`code/fcn.00402790.c`](code/fcn.00402790.c)
- [`code/fcn.00402910.c`](code/fcn.00402910.c)
- [`code/fcn.004029f0.c`](code/fcn.004029f0.c)
- [`code/fcn.00402a80.c`](code/fcn.00402a80.c)
- [`code/fcn.00402b20.c`](code/fcn.00402b20.c)
- [`code/fcn.00402bb0.c`](code/fcn.00402bb0.c)
- [`code/fcn.00402be0.c`](code/fcn.00402be0.c)
- [`code/fcn.00402c50.c`](code/fcn.00402c50.c)
- [`code/fcn.00402dd0.c`](code/fcn.00402dd0.c)
- [`code/fcn.00402ec0.c`](code/fcn.00402ec0.c)
- [`code/fcn.00402ef0.c`](code/fcn.00402ef0.c)
- [`code/fcn.00402f10.c`](code/fcn.00402f10.c)
- [`code/fcn.00403040.c`](code/fcn.00403040.c)

## Behavioral Analysis

Based on the analysis of the provided disassembly and decompiled C code, this binary is a **malware loader/dropper** designed to unpack or decrypt an embedded payload into memory and execute it. It employs several techniques common in sophisticated malware to evade detection and perform clandestine operations.

### Core Functionality
The primary purpose of this code is to act as a "packer" or "loader." It performs the initial environment checks, decrypts a hidden piece of code (shellcode) stored within its own data section, and then executes that payload in a separate thread.

### Suspicious & Malicious Behaviors

*   **In-Memory Decryption/Deobfuscation:**
    *   The function `fcn.00401595` is a classic loader pattern. It calls `VirtualAlloc` to reserve memory, then iterates through the allocated space to perform an **XOR-based decryption** of the data (`*(arg1_00 + iVar1) = *(arg3 + (iVar1 & 3)) ^ *(arg1 + iVar1)`).
    *   Following the decryption, it calls `VirtualProtect` and then `CreateThread` to execute the decrypted content. This is a primary indicator of **Shellcode Loading**.

*   **Anti-Analysis & Anti-Debugging:**
    *   The function `fcn.00401990` performs complex arithmetic using several system values: `GetSystemTimeAsFileTime`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetTickCount`, and `QueryPerformanceCounter`. 
    *   It calculates a value based on these variables and compares it against a hardcoded constant (`0x2b992ddfa232`). This is an **Environment Keying** or **Timing-based Anti-Analysis** technique. It aims to detect if the code is running in a debugger, emulator, or sandbox by looking for inconsistencies in time/process identity.

*   **Inter-Process Communication (IPC):**
    *   The function `fcn.00401630` utilizes `CreateNamedPipeA` and `ConnectNamedPipe`. While used for legitimate software communication, it is frequently used by malware to facilitate **communication between different components of a multi-stage infection** or to communicate with a compromised host process.

*   **Process/Thread Manipulation:**
    *   The code uses `CreateThread` in multiple locations (e.g., `fcn.004017f8` and `fcn.00401595`) to offload execution. This is often used to hide the main malicious activity from the primary thread, making it harder for basic behavioral analysis tools to link actions together.

*   **Manual Mapping/Loader Techniques:**
    *   The presence of `RtlAddFunctionTable` in `fcn.004024e0` and extensive use of `VirtualProtect` suggests the loader is prepared to handle **Reflective DLL Loading** or similar techniques where a module is loaded into memory without being registered with the Windows loader.

### Notable Techniques & Patterns
*   **Staged Execution:** The structure (check environment -> decrypt payload -> spawn thread) indicates a multi-stage attack where this binary is only the first stage.
*   **Data Obfuscation:** The use of XOR for decryption suggests the actual malicious payload is hidden from static analysis tools that do not perform emulation or dynamic unpacking.
*   **Standard Library Abuse:** The code heavily uses `msvcrt` and standard Windows API calls but hides its intent through layered execution and runtime deobfuscation.

### Summary of Indicators
*   **Persistence/Evasion:** High (Anti-debugging via timing/environment checks).
*   **Injection/Execution:** High (In-memory decryption and execution via `CreateThread`).
*   **Communication:** Moderate (Use of Named Pipes for internal/external coordination).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of XOR-based decryption for data in the `.data` section is a clear attempt to hide malicious payload contents from static analysis. |
| T1497 | Virtualization/Sandbox Detection | The execution of `GetTickCount`, `QueryPerformanceCounter`, and `GetSystemTimeAsFileTime` are standard indicators of timing-based checks used to detect sandboxes or debuggers. |
| T1055 | Process Injection | The sequence of using `VirtualAlloc`, `VirtualProtect`, and `CreateThread` to execute shellcode is a primary method for injecting and executing code in memory. |
| T1028 | Loader | The overall architecture (unpacking, decrypting, and spawning threads) characterizes the binary as a loader intended to deliver subsequent stages of an attack. |
| T1637 | Reflective Loading | The presence of `RtlAddFunctionTable` combined with `VirtualProtect` indicates a preparation for loading modules into memory without standard Windows loader registration. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the list of extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   *(None identified)*

**Mutex names / Named pipes**
*   *(Note: The behavior analysis confirms the use of `CreateNamedPipeA` and `ConnectNamedPipe`, but no specific pipe names were provided in the text.)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Hardcoded Constant:** `0x2b992ddfa232` (Used in function `fcn.00401990` for environment keying/anti-analysis). 

---
**Analyst Notes:**
The "EXTRACTED STRINGS" section appears to contain high amounts of obfuscated data, assembly remnants, and standard PE header definitions (e.g., `.rdata`, `.xdata`, `.idata`). These were excluded as they do not constitute unique indicators for a specific campaign. While the behavioral analysis identifies significant malicious techniques (XOR decryption, shellcode execution via `CreateThread`, and anti-debugging checks), it does not include specific infrastructure values like hardcoded IP addresses or file paths in the provided text.

---

## Malware Family Classification

1. **Malware family**: custom (or Unknown)
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Shellcode Execution Pipeline:** The binary exhibits a classic "loader" behavior by allocating memory (`VirtualAlloc`), performing XOR-based decryption of an embedded payload, and executing that payload in a new thread via `CreateThread`. This is a primary indicator of a multi-stage delivery mechanism.
*   **Anti-Analysis & Evasion:** The presence of complex timing-based checks (using `GetTickCount` and `QueryPerformanceCounter`) against a hardcoded constant (`0x2b992ddfa232`) indicates deliberate efforts to detect sandboxes or debuggers before executing the malicious payload.
*   **Advanced Loading Techniques:** The use of `RtlAddFunctionTable` combined with `VirtualProtect` suggests the capability for Reflective DLL loading, a technique used by sophisticated malware to load modules into memory without being registered in the standard Windows loader, making it harder for security tools to detect.
