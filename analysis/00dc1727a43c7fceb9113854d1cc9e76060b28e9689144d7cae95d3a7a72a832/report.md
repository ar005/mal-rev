# Threat Analysis Report

**Generated:** 2026-06-25 15:15 UTC
**Sample:** `00dc1727a43c7fceb9113854d1cc9e76060b28e9689144d7cae95d3a7a72a832_00dc1727a43c7fceb9113854d1cc9e76060b28e9689144d7cae95d3a7a72a832.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00dc1727a43c7fceb9113854d1cc9e76060b28e9689144d7cae95d3a7a72a832_00dc1727a43c7fceb9113854d1cc9e76060b28e9689144d7cae95d3a7a72a832.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 30,208 bytes |
| MD5 | `aa01a0f2676d6d564b52a9536a1dfdb4` |
| SHA1 | `a97c965f21695faa0f806c3fd62e4e0f1dfae572` |
| SHA256 | `00dc1727a43c7fceb9113854d1cc9e76060b28e9689144d7cae95d3a7a72a832` |
| Overall entropy | 5.741 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779119159 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 20,992 | 6.176 | No |
| `.rdata` | 5,120 | 5.048 | No |
| `.data` | 512 | 0.436 | No |
| `.pdata` | 1,024 | 3.679 | No |
| `.tls` | 1,024 | -0.0 | No |
| `.reloc` | 512 | 1.069 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `CopyFileA`, `CreateDirectoryA`, `CreateFileA`, `DeleteCriticalSection`, `EnterCriticalSection`, `ExpandEnvironmentStringsA`, `FindClose`, `FindFirstFileA`, `FindNextFileA`, `GetFileSize`, `GetLastError`, `GetModuleFileNameA`, `GetModuleHandleA`, `GetModuleHandleExA`
**api-ms-win-crt-string-l1-1-0.dll**: `_stricmp`, `strcpy`, `strlen`, `strncmp`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_assert`, `_execute_onexit_table`, `_exit`, `_initialize_onexit_table`, `_initterm`, `_initterm_e`, `_register_onexit_function`, `_register_thread_local_exe_atexit_callback`, `abort`
**api-ms-win-crt-heap-l1-1-0.dll**: `calloc`, `free`, `malloc`
**api-ms-win-crt-private-l1-1-0.dll**: `memcpy`, `strrchr`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__acrt_iob_func`, `__stdio_common_vfprintf`, `__stdio_common_vsprintf`, `_fileno`, `_setmode`, `fflush`

### Exports

`icudt63_dat`

## Extracted Strings

Total strings found: **125** (showing first 100)

```
!This program cannot be run in DOS mode.$
`.rdata
@.data
.pdata
.reloc
AWAVATVWUSH
 []_^A\A^A_
AVVWSH
([_^A^
AWAVVWSH
D9|$<u
@[_^A^A_
AWAVAUATVWUSH
9MZusHcF<
([]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AVVWSH
([_^A^
t.ffff.
UAWAVAUATVWSH
ffffff.
fffff.
[_^A\A]A^A_]
7ffffff.
fffff.
AWAVATVWSH
X[_^A\A^A_
AVVWSH
AVVWSH
([_^A^
u\HcC<
ffffff.
8MZu]HcP<
t=H+
8MZuJHcP<
:MZuvLcB<B
ffffff.
:MZu~HcB<
ffffff.
kernel32.dll
ntdll.dll
LoadLibraryA
TpAllocWork
TpPostWork
TpReleaseWork
 zI+Ka
@_6{lM
-!dso || dso == &__dso_handle
../crt/tls_atexit.c
  Unknown pseudo relocation protocol version %d.

  Unknown pseudo relocation bit size %d.

%d bit pseudo relocation at %p out of range, targeting %p, yielding the value %p.

Address %p has no image-section
  VirtualQuery failed for %d bytes at address %p
  VirtualProtect failed with code 0x%x
Mingw-w64 runtime failure:

runtime error %d

libtest.dll
icudt63_dat
icudt631.icudt63_dat
CloseHandle
CopyFileA
CreateDirectoryA
CreateFileA
DeleteCriticalSection
EnterCriticalSection
ExpandEnvironmentStringsA
FindClose
FindFirstFileA
FindNextFileA
GetFileSize
GetLastError
GetModuleFileNameA
GetModuleHandleA
GetModuleHandleExA
GetProcAddress
InitializeCriticalSection
LeaveCriticalSection
LoadLibraryA
MultiByteToWideChar
ReadFile
SetFileAttributesA
TlsAlloc
TlsFree
TlsGetValue
TlsSetValue
VirtualProtect
VirtualQuery
_stricmp
strcpy
strlen
strncmp
_assert
_execute_onexit_table
_initialize_onexit_table
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1800051a0` | `0x1800051a0` | 19542 | ✓ |
| `fcn.18000259e` | `0x18000259e` | 3955 | ✓ |
| `fcn.18000162b` | `0x18000162b` | 3955 | ✓ |
| `entry2` | `0x180005040` | 2690 | ✓ |
| `fcn.180003511` | `0x180003511` | 2186 | ✓ |
| `fcn.180005220` | `0x180005220` | 770 | ✓ |
| `section..text` | `0x180001000` | 471 | ✓ |
| `entry1` | `0x180004dd0` | 421 | ✓ |
| `fcn.180005530` | `0x180005530` | 409 | ✓ |
| `fcn.180004c60` | `0x180004c60` | 357 | ✓ |
| `entry0` | `0x1800011e0` | 342 | ✓ |
| `fcn.180001561` | `0x180001561` | 202 | ✓ |
| `fcn.180001350` | `0x180001350` | 198 | ✓ |
| `fcn.1800014ab` | `0x1800014ab` | 182 | ✓ |
| `fcn.180001437` | `0x180001437` | 116 | ✓ |
| `fcn.180005be0` | `0x180005be0` | 110 | ✓ |
| `fcn.1800056d0` | `0x1800056d0` | 90 | ✓ |
| `fcn.180005770` | `0x180005770` | 89 | ✓ |
| `fcn.1800057d0` | `0x1800057d0` | 85 | ✓ |
| `fcn.180005e90` | `0x180005e90` | 72 | ✓ |
| `fcn.180005ee0` | `0x180005ee0` | 52 | ✓ |
| `fcn.180005e60` | `0x180005e60` | 48 | ✓ |
| `fcn.180005740` | `0x180005740` | 46 | ✓ |
| `fcn.18000451e` | `0x18000451e` | 44 | ✓ |
| `fcn.18000454a` | `0x18000454a` | 44 | ✓ |
| `fcn.180004576` | `0x180004576` | 44 | ✓ |
| `fcn.1800045a2` | `0x1800045a2` | 44 | ✓ |
| `fcn.1800045ce` | `0x1800045ce` | 44 | ✓ |
| `fcn.1800045fa` | `0x1800045fa` | 44 | ✓ |
| `fcn.180004626` | `0x180004626` | 44 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/entry1.c`](code/entry1.c)
- [`code/entry2.c`](code/entry2.c)
- [`code/fcn.180001350.c`](code/fcn.180001350.c)
- [`code/fcn.180001437.c`](code/fcn.180001437.c)
- [`code/fcn.1800014ab.c`](code/fcn.1800014ab.c)
- [`code/fcn.180001561.c`](code/fcn.180001561.c)
- [`code/fcn.18000162b.c`](code/fcn.18000162b.c)
- [`code/fcn.18000259e.c`](code/fcn.18000259e.c)
- [`code/fcn.180003511.c`](code/fcn.180003511.c)
- [`code/fcn.18000451e.c`](code/fcn.18000451e.c)
- [`code/fcn.18000454a.c`](code/fcn.18000454a.c)
- [`code/fcn.180004576.c`](code/fcn.180004576.c)
- [`code/fcn.1800045a2.c`](code/fcn.1800045a2.c)
- [`code/fcn.1800045ce.c`](code/fcn.1800045ce.c)
- [`code/fcn.1800045fa.c`](code/fcn.1800045fa.c)
- [`code/fcn.180004626.c`](code/fcn.180004626.c)
- [`code/fcn.180004c60.c`](code/fcn.180004c60.c)
- [`code/fcn.1800051a0.c`](code/fcn.1800051a0.c)
- [`code/fcn.180005220.c`](code/fcn.180005220.c)
- [`code/fcn.180005530.c`](code/fcn.180005530.c)
- [`code/fcn.1800056d0.c`](code/fcn.1800056d0.c)
- [`code/fcn.180005740.c`](code/fcn.180005740.c)
- [`code/fcn.180005770.c`](code/fcn.180005770.c)
- [`code/fcn.1800057d0.c`](code/fcn.1800057d0.c)
- [`code/fcn.180005be0.c`](code/fcn.180005be0.c)
- [`code/fcn.180005e60.c`](code/fcn.180005e60.c)
- [`code/fcn.180005e90.c`](code/fcn.180005e90.c)
- [`code/fcn.180005ee0.c`](code/fcn.180005ee0.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

Based on the provided disassembly and decompiler output, here is a technical analysis of the binary sample.

### Core Functionality and Purpose
The binary functions as a **multi-stage loader (or "packer")** designed to decrypt/deobfuscate its internal payload and then perform file system operations. It exhibits characteristics common in malware designed to drop additional components or exfiltrate data from a target machine.

### Suspicious and Malicious Behaviors

*   **Anti-Analysis / Evasion:**
    *   **Delayed Execution:** Function `fcn.18000259e` begins with a call to `Sleep(5000)`. This is a classic technique used to stall execution, allowing the malware to outwait automated sandbox analysis timers.
    *   **Obfuscated API Resolution:** The code frequently uses offset-based math (e.g., `iVar1 + 0x7b`) followed by calls to `LoadLibraryA`. This suggests that the names of the DLLs or functions are stored as encrypted/obfuscated strings that are only resolved in memory at runtime, hiding the program's true capabilities from static analysis.

*   **Memory Manipulation (Loader Behavior):**
    *   **Dynamic Memory Protection:** The function `fcn.180005220` iterates through memory segments using logic related to `VirtualQuery` and calls **`VirtualProtect`**. This is a common indicator of a "packer" or "loader" preparing memory regions (e.g., changing from Read-Only to Read/Write/Execute) to host a decrypted payload.
    *   **Complex Decryption Routine:** The section containing `vpunpcklqdq_avx` and `vpackssdw_avx2` suggests the use of AVX instructions for high-speed data processing or complex decryption logic. This is often used in modern malware to obfuscate the underlying algorithm from simple decompilers.

*   **File Manipulation & Dropper Behavior:**
    *   **Persistence/Dropping via `CopyFileA`:** Functions like `fcn.180003511` contain multiple loops using `FindFirstFileA`, `FindNextFileA`, and `CopyFileA`. 
        *   It searches for specific files (potentially other executables or system files) and copies them to different locations.
        *   The creation of directories (`CreateDirectoryA`) followed by moving/copying files suggests the "dropping" of secondary payloads or the staging of stolen data.
    *   **Data Extraction:** The loop logic in `fcn.180003511` (specifically looking for filenames and copying them) is highly indicative of a **downloader** or **infostealer** identifying specific target files on the system to move or copy.

### Notable Techniques & Patterns

*   **Dynamic Library Loading:** The code avoids having many imports in its Import Address Table (IAT). Instead, it resolves functions from `ntdll` and `kernel32` dynamically, which is a standard technique to hinder static analysis tools like `strings`.
*   **Environment Interaction:** The use of `GetModuleFileNameA` and `GetModuleHandleA`, followed by string manipulations before performing file operations, suggests the malware determines its own path on disk before attempting to interact with nearby files or folders.
*   **Complex String Handling:** Function `fcn.1800014ab` contains complex logic for comparing strings that are not standard constant strings. This indicates a "string table" mechanism where the analyst must first "unpack" the string table to see what APIs/file paths the malware is actually interacting with.

### Summary of Indicators
*   **Tactic:** Defense Evasion (Sleep, Obfuscated Imports).
*   **Tactic:** Persistence / Dropper (Copying files in loops via `FindFirstFile`).
*   **Tactic:** Execution Guard (AVX-based decryption routines).
*   **Verdict:** This is likely a **malicious loader or dropper**. Its primary role is to bypass security scanners by deobfuscating its components and then deploying additional malware onto the filesystem.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Detection | The use of `Sleep(5000)` is a common tactic to stall execution and outwait the time limits of automated sandbox analysis environments. |
| **T1027** | Obfuscated Files or Information | The use of offset-based math for API resolution and complex string table logic hides function names and paths from static analysis tools. |
| **T1055** | Process Injection | The utilization of `VirtualProtect` to change memory permissions is a standard loader behavior used to prepare memory segments for executing decrypted payloads. |
| **T1027** | Obfuscated Files or Information | The use of AVX instructions for decryption logic serves as an evasion technique to complicate the analysis of decoding algorithms by decompilers. |
| **T1105** | Ingress Tool Transfer | The sequence of creating directories and copying files using `CopyFileA` indicates a "dropper" behavior used to move secondary payloads onto the filesystem. |
| **T1027** | Obfuscated Files or Information | Minimizing the Import Address Table (IAT) and resolving functions from `ntdll` and `kernel32` dynamically hides the malware's capabilities from string-based analysis. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the list of extracted Indicators of Compromise (IOCs).

**Note:** The source material describes a "packer" or "loader." Because the payload is encrypted/obfuscated within the binary (as noted in the behavior section), many network-based IOCs (like IP addresses and C2 domains) are not visible in the raw strings provided.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (While the behavioral analysis notes that the malware moves files, no specific hardcoded paths were revealed in the string dump).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Suspicious File Names:** `libtest.dll` (Note: While not a specific path, this is a non-standard filename that may be used as a placeholder or temporary component of the loader).
*   **Evasion Tactic (Sleep):** `Sleep(5000)` (Used to bypass sandbox analysis).
*   **Persistence/Execution Guard:** Use of **AVX instructions** (`vpunpcklqdq_avx`, `vpackssdw_avx2`) for the decryption of embedded payloads.
*   **API Obfuscation:** The use of `GetProcAddress` and `LoadLibraryA` to resolve functions from `ntdll.dll` and `kernel32.dll` at runtime rather than through a standard Import Address Table (IAT).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
*   **Loader Functionality:** The sample utilizes `VirtualProtect` to manipulate memory permissions and employs complex AVX-based decryption routines, which are characteristic of a loader designed to unpack and execute secondary payloads in memory.
*   **Dropper Behavior:** The use of `FindFirstFileA`, `CreateDirectoryA`, and `CopyFileA` indicates the sample is actively managing files on the filesystem to stage or "drop" additional components for the attacker.
*   **Evasion Techniques:** The implementation of execution delays (`Sleep`), obfuscated API resolution (avoiding a standard IAT), and complex string handling are classic indicators of a malicious loader designed to bypass automated sandbox analysis and static detection.
