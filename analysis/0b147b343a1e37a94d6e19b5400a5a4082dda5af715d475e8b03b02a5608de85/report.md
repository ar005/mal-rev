# Threat Analysis Report

**Generated:** 2026-07-25 19:33 UTC
**Sample:** `0b147b343a1e37a94d6e19b5400a5a4082dda5af715d475e8b03b02a5608de85_0b147b343a1e37a94d6e19b5400a5a4082dda5af715d475e8b03b02a5608de85.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b147b343a1e37a94d6e19b5400a5a4082dda5af715d475e8b03b02a5608de85_0b147b343a1e37a94d6e19b5400a5a4082dda5af715d475e8b03b02a5608de85.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 17,408 bytes |
| MD5 | `4553984db433d9de87bbc8a1a38f584d` |
| SHA1 | `04c411dc3a3af741449d17673645349639564287` |
| SHA256 | `0b147b343a1e37a94d6e19b5400a5a4082dda5af715d475e8b03b02a5608de85` |
| Overall entropy | 4.883 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766195975 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 6,656 | 5.98 | No |
| `.data` | 1,536 | 5.752 | No |
| `.rdata` | 2,560 | 3.863 | No |
| `.pdata` | 1,024 | 2.442 | No |
| `.xdata` | 1,024 | 2.714 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 2,048 | 3.336 | No |
| `.CRT` | 512 | 0.272 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 512 | 1.405 | No |

### Imports

**KERNEL32.dll**: `CreateThread`, `DeleteCriticalSection`, `EnterCriticalSection`, `GetCurrentThreadId`, `GetLastError`, `GetModuleHandleA`, `GetProcAddress`, `GetTickCount`, `InitializeCriticalSection`, `LeaveCriticalSection`, `SetUnhandledExceptionFilter`, `Sleep`, `TlsGetValue`, `VirtualAlloc`, `VirtualProtect`
**msvcrt.dll**: `__C_specific_handler`, `__getmainargs`, `__initenv`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `_amsg_exit`, `_cexit`, `_commode`, `_fmode`, `_initterm`, `_onexit`, `abort`, `calloc`, `exit`
**USER32.dll**: `PeekMessageA`, `PostThreadMessageA`

## Extracted Strings

Total strings found: **134** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
.reloc
UAUATWVSH
([^_A\A]]
([^_A\A]]
ATUWVSH
@[^_]A\
AUATUWVSH
|$H*umH
h[^_]A\A]
h[^_]A\A]
l$PHc5
UAWAVAUATWVSH
[^_A\A]A^A_]
(D;%FS
UAUATWVSH
([^_A\A]]H
:MZu[HcB<H
@' t	H
EqaEd
y<!B%v"C%6`
90h&i
n=x^c1a
f)'	f) 
d+#	f)7
6u"H'o#[041A%}
{1!=j+k
j"iK+ b\^
e~}L;k9|
56^$&c
$x ~\J"i
g$#D%u,Y\,b
,@;k<J+
=q7Qss8X+
$p?F%v:Q#
D%F	 Qg,g
`*%QH-~
f #@8|"A%u"A+
j7e^>v;_8s,4o"#@8|"A%u"A
@3|"G=s"G=s"G=st
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA`)
Argument domain error (DOMAIN)
Argument singularity (SIGN)
Overflow range error (OVERFLOW)
Partial loss of significance (PLOSS)
Total loss of significance (TLOSS)
The result is too small to be represented (UNDERFLOW)
Unknown error
_matherr(): %s in %s(%g, %g)  (retval=%g)

Mingw-w64 runtime failure:

Address %p has no image-section
  VirtualQuery failed for %d bytes at address %p
  VirtualProtect failed with code 0x%x
  Unknown pseudo relocation protocol version %d.

  Unknown pseudo relocation bit size %d.

%d bit pseudo relocation at %p out of range, targeting %p, yielding the value %p.

GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
GCC: (GNU) 13-win32
0`
p	
CreateThread
DeleteCriticalSection
EnterCriticalSection
GetCurrentThreadId
GetLastError
GetModuleHandleA
GetProcAddress
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140001ea0` | `0x140001ea0` | 2374 | ✓ |
| `fcn.140001b00` | `0x140001b00` | 922 | ✓ |
| `fcn.140001190` | `0x140001190` | 592 | ✓ |
| `fcn.140001990` | `0x140001990` | 368 | ✓ |
| `fcn.140002210` | `0x140002210` | 242 | ✓ |
| `fcn.140001550` | `0x140001550` | 226 | ✓ |
| `fcn.140001710` | `0x140001710` | 159 | ✓ |
| `fcn.1400014b5` | `0x1400014b5` | 148 | ✓ |
| `entry1` | `0x140001770` | 130 | ✓ |
| `fcn.140002440` | `0x140002440` | 128 | ✓ |
| `fcn.140002070` | `0x140002070` | 123 | ✓ |
| `fcn.140001920` | `0x140001920` | 112 | ✓ |
| `fcn.1400024c0` | `0x1400024c0` | 55 | ✓ |
| `fcn.140002580` | `0x140002580` | 54 | ✓ |
| `fcn.140001483` | `0x140001483` | 50 | ✓ |
| `fcn.140002710` | `0x140002710` | 50 | ✓ |
| `entry2` | `0x140001740` | 48 | ✓ |
| `fcn.140002790` | `0x140002790` | 38 | ✓ |
| `entry0` | `0x1400013e0` | 34 | ✓ |
| `fcn.140002900` | `0x140002900` | 33 | ✓ |
| `fcn.140001440` | `0x140001440` | 25 | ✓ |
| `fcn.140002750` | `0x140002750` | 11 | ✓ |
| `fcn.140002760` | `0x140002760` | 11 | ✓ |
| `fcn.140002780` | `0x140002780` | 11 | ✓ |
| `sub.msvcrt.dll___set_app_type` | `0x1400027d8` | 6 | ✓ |
| `sub.msvcrt.dll___getmainargs` | `0x1400027c8` | 6 | ✓ |
| `sub.msvcrt.dll_malloc` | `0x140002838` | 6 | ✓ |
| `sub.msvcrt.dll_strlen` | `0x140002850` | 6 | ✓ |
| `sub.msvcrt.dll_memcpy` | `0x140002840` | 6 | ✓ |
| `sub.msvcrt.dll__amsg_exit` | `0x1400027e8` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/entry1.c`](code/entry1.c)
- [`code/entry2.c`](code/entry2.c)
- [`code/fcn.140001190.c`](code/fcn.140001190.c)
- [`code/fcn.140001440.c`](code/fcn.140001440.c)
- [`code/fcn.140001483.c`](code/fcn.140001483.c)
- [`code/fcn.1400014b5.c`](code/fcn.1400014b5.c)
- [`code/fcn.140001550.c`](code/fcn.140001550.c)
- [`code/fcn.140001710.c`](code/fcn.140001710.c)
- [`code/fcn.140001920.c`](code/fcn.140001920.c)
- [`code/fcn.140001990.c`](code/fcn.140001990.c)
- [`code/fcn.140001b00.c`](code/fcn.140001b00.c)
- [`code/fcn.140001ea0.c`](code/fcn.140001ea0.c)
- [`code/fcn.140002070.c`](code/fcn.140002070.c)
- [`code/fcn.140002210.c`](code/fcn.140002210.c)
- [`code/fcn.140002440.c`](code/fcn.140002440.c)
- [`code/fcn.1400024c0.c`](code/fcn.1400024c0.c)
- [`code/fcn.140002580.c`](code/fcn.140002580.c)
- [`code/fcn.140002710.c`](code/fcn.140002710.c)
- [`code/fcn.140002750.c`](code/fcn.140002750.c)
- [`code/fcn.140002760.c`](code/fcn.140002760.c)
- [`code/fcn.140002780.c`](code/fcn.140002780.c)
- [`code/fcn.140002790.c`](code/fcn.140002790.c)
- [`code/fcn.140002900.c`](code/fcn.140002900.c)
- [`code/sub.msvcrt.dll___getmainargs.c`](code/sub.msvcrt.dll___getmainargs.c)
- [`code/sub.msvcrt.dll___set_app_type.c`](code/sub.msvcrt.dll___set_app_type.c)
- [`code/sub.msvcrt.dll__amsg_exit.c`](code/sub.msvcrt.dll__amsg_exit.c)
- [`code/sub.msvcrt.dll_malloc.c`](code/sub.msvcrt.dll_malloc.c)
- [`code/sub.msvcrt.dll_memcpy.c`](code/sub.msvcrt.dll_memcpy.c)
- [`code/sub.msvcrt.dll_strlen.c`](code/sub.msvcrt.dll_strlen.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C code, here is a technical analysis of the binary's functionality:

### Core Functionality and Purpose
The binary functions as a **loader** or **stub**. It is designed to perform in-memory unpacking/decryption of a hidden payload and then execute that payload. Rather than performing high-level actions like file encryption or network communication directly, its primary role is to "stage" the actual malicious components into memory to evade disk-based detection.

### Suspicious and Malicious Behaviors
*   **In-Memory Decryption:** 
    The function `fcn.1400014b5` is a clear indicator of malicious behavior. It allocates a new region of memory using `VirtualAlloc`, performs a XOR-based decryption loop on the data (the loop involving `^ *(arg1 + iVar1)`), and then calls `VirtualProtect` to ensure that memory segment is executable.
*   **Process Injection / Execution:** 
    Immediately after decrypting the payload in `fcn.1400014b5`, the code calls `CreateThread`. This allows the binary to execute the newly decrypted code in a separate thread, which is a common technique used by malware to run "hidden" payloads without them being easily traced via standard execution flows.
*   **Anti-Analysis & Evasion:** 
    The code includes several techniques meant to hinder analysis:
    *   **Delayed Execution:** `fcn.140002900` contains a loop that calls `Sleep(10000)`. This is often used to stall automated sandboxes or "timeout" an analyst's patience during the initial run.
    *   **Dynamic API Resolution:** The function `fcn.140001483` appears to manually resolve addresses for core functions like `GetProcAddress` and `GetModuleHandleA`. This is done to hide the program’s true capabilities from the Import Address Table (IAT), making it harder for static analysis tools to determine what the binary does.
    *   **Reflective-like Loading:** The complex loops in `fcn.140001b00` and `fcn.140001920` are typical of a manual PE loader. They iterate through headers/sections to calculate offsets, likely preparing the environment for an injected "hidden" module.

### Notable Techniques and Patterns
*   **Staged Execution:** The code follows a classic "Stub" pattern where the primary functionality is hidden behind several layers: `Entry` -> `Loader Logic` -> `Decryption` -> `Thread Creation`. 
*   **PE Parsing:** Function `fcn.140002440` specifically checks for PE headers (the `0x5A4D` and `0x4550` signatures). This confirms that the binary is designed to handle other executable files in-memory, a hallmark of packers or "droppers."
*   **Memory Manipulation:** The repeated use of `VirtualProtect` suggests the code is frequently changing memory permissions (e.g., from Read/Write to Execute) as it processes different stages of its decryption routine.

### Summary for Incident Response
This binary is highly suspicious and likely part of a **multi-stage malware infection**. It serves as the "loader" component designed to hide the primary payload from antivirus scanners by decrypting it only in memory before execution. The presence of `CreateThread` on dynamically allocated and decrypted buffers strongly indicates it is used for executing malicious payloads (such as ransomware modules, spyware, or backdoors).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of XOR-based decryption and `VirtualProtect` changes is used to hide the payload's true purpose from static analysis. |
| T1055 | Process Injection | The binary uses `CreateThread` on a newly allocated memory buffer to execute decrypted code in-memory, bypassing disk-based detection. |
| T1497 | Virtualization/Sandbox Evasion | The inclusion of a `Sleep(10000)` loop is specifically designed to stall automated analysis and time out during sandbox evaluation. |
| T1036 | Dynamic Resolution | Manually resolving addresses for `GetProcAddress` hides the binary's true capabilities from static analysis of the Import Address Table (IAT). |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs).

### **Analysis Note**
The provided data describes the **behavioral characteristics** of a malware loader rather than specific network infrastructure or file system artifacts. While the behavior is highly malicious (e.g., in-memory decryption, dynamic API resolution), there are no hardcoded IP addresses, domains, or filesystem paths present in the text provided.

---

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: The strings include various API calls like `GetModuleHandleA` and `VirtualAlloc`, but these are standard Windows functions, not specific file paths.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 hashes were present in the provided strings.)

### **Other artifacts**
*   **Malware Technique: In-memory XOR decryption** (detected in `fcn.1400014b5`)
*   **Malware Technique: Dynamic API Resolution** (used to hide imports from the IAT)
*   **Malware Technique: Staged Execution / Loader Pattern** (multi-stage unpacking logic)
*   **Evasion Tactic: Anti-Analysis Sleep** (a `Sleep(10000)` loop in `fcn.140002900` to bypass sandbox timeouts)
*   **Execution Method:** `CreateThread` used on dynamically allocated and decrypted memory buffers.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **In-Memory Decryption & Execution:** The binary uses a classic "stub" architecture, employing `VirtualAlloc` and XOR decryption to unpack a hidden payload into memory, followed by `CreateThread` to execute it. This is the defining behavior of a loader designed to evade disk-based security products.
*   **Anti-Analysis Tactics:** The inclusion of `Sleep(10000)` loops (to time out automated sandboxes) and Dynamic API Resolution (hiding functionality from the Import Address Table) are standard evasion techniques used by sophisticated loaders to mask their intent and behavior.
*   **Staged Execution Infrastructure:** The detection of PE header parsing and manual memory permission modifications (`VirtualProtect`) confirms that this specific binary's role is to act as a vehicle for other malicious payloads (such as ransomware, spyware, or backdoors) rather than performing the final payload actions itself.
