# Threat Analysis Report

**Generated:** 2026-07-19 14:31 UTC
**Sample:** `0948c44b0955957841629c838f8b6830def5ae8a2b6b162cb171485125dda638_0948c44b0955957841629c838f8b6830def5ae8a2b6b162cb171485125dda638.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0948c44b0955957841629c838f8b6830def5ae8a2b6b162cb171485125dda638_0948c44b0955957841629c838f8b6830def5ae8a2b6b162cb171485125dda638.exe` |
| File type | PE32+ executable for MS Windows 5.02 (DLL), x86-64, 19 sections |
| Size | 236,592 bytes |
| MD5 | `90ff7d2c3d53376f705b71dd22b9d999` |
| SHA1 | `197c7369cc5c2160b1db55e79681d09f2a80643a` |
| SHA256 | `0948c44b0955957841629c838f8b6830def5ae8a2b6b162cb171485125dda638` |
| Overall entropy | 5.755 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774275785 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 7,680 | 6.074 | No |
| `.data` | 512 | 1.666 | No |
| `.rdata` | 1,536 | 4.029 | No |
| `.pdata` | 1,024 | 2.328 | No |
| `.xdata` | 512 | 3.355 | No |
| `.bss` | 0 | 0.0 | No |
| `.edata` | 512 | 1.314 | No |
| `.idata` | 2,048 | 3.801 | No |
| `.CRT` | 512 | 0.253 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 512 | 1.031 | No |
| `/4` | 1,024 | 1.282 | No |
| `/19` | 160,768 | 5.996 | No |
| `/31` | 7,168 | 4.521 | No |
| `/45` | 9,216 | 5.329 | No |
| `/57` | 2,048 | 4.278 | No |
| `/70` | 1,024 | 4.013 | No |
| `/81` | 10,752 | 2.0 | No |
| `/92` | 1,536 | 1.382 | No |

### Imports

**KERNEL32.dll**: `AddVectoredExceptionHandler`, `CheckRemoteDebuggerPresent`, `DeleteCriticalSection`, `DisableThreadLibraryCalls`, `EnterCriticalSection`, `GetCurrentProcess`, `GetCurrentThread`, `GetLastError`, `GetModuleFileNameA`, `GetModuleHandleA`, `GetProcAddress`, `GetThreadContext`, `GetTickCount`, `InitializeCriticalSection`, `IsDebuggerPresent`
**msvcrt.dll**: `__iob_func`, `_amsg_exit`, `_initterm`, `_lock`, `_unlock`, `abort`, `calloc`, `free`, `fwrite`, `memcpy`, `realloc`, `strlen`, `strncmp`, `vfprintf`
**USER32.dll**: `DispatchMessageA`, `GetMessageA`, `TranslateMessage`
**WININET.dll**: `InternetCloseHandle`, `InternetOpenA`, `InternetOpenUrlA`, `InternetReadFile`

### Exports

`timeBeginPeriod`, `timeEndPeriod`, `timeGetTime`

## Extracted Strings

Total strings found: **6030** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.edata
@.idata
.reloc
AUATUWVSH
([^_]A\A]
([^_]A\A]
([^_]A\A]
AVAUATVSH
 [^A\A]A^
tQHcA<
AUATWSH
[_A\A]
AWAVAUATUWVSH
https://H
files.ca
D$pbin
tbox.moeH
/ct9u20.H
Mozilla/H
5.0 (WinH
dows NT H
10.0; WiH
n64; x64H
) AppleWH
ebKit/53H
[^_]A\A]A^A_
p|bx?u}}H
ATUWVSH
P[^_]A\
P[^_]A\
UAWAVAUATWVSH
[^_A\A]A^A_]
ATWVSH
([^_A\H
tNHcA<H
tTIcB<L
t	HcA<
tCHcA<H
@' t	M
tKIcA<L
tSIcK<L
ntdll.dll
TpAllocWork
TpPostWork
TpReleaseWork
TpWaitForWork
Mingw-w64 runtime failure:

Address %p has no image-section
  VirtualQuery failed for %d bytes at address %p
  VirtualProtect failed with code 0x%x
  Unknown pseudo relocation protocol version %d.

  Unknown pseudo relocation bit size %d.

GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 10-win32 20220113
GCC: (GNU) 10-win32 20220113
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 10-win32 20220113
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 10-win32 20220113
0`
p	P
b0`
p	
WINMM.dll
timeBeginPeriod
timeEndPeriod
timeGetTime
AddVectoredExceptionHandler
CheckRemoteDebuggerPresent
DeleteCriticalSection
DisableThreadLibraryCalls
EnterCriticalSection
GetCurrentProcess
GetCurrentThread
GetLastError
GetModuleFileNameA
GetModuleHandleA
GetProcAddress
GetThreadContext
GetTickCount
InitializeCriticalSection
IsDebuggerPresent
LeaveCriticalSection
LoadLibraryA
SetThreadContext
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **6**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.ABMHaBiVJ3j7z_DoWork__` | `0x2774d1500` | 1662 | ✓ |
| `dbg._pei386_runtime_relocator` | `0x2774d20c0` | 752 | ✓ |
| `sym.__write_memory.part.0` | `0x2774d1ea0` | 544 | ✓ |
| `sym._CRT_INIT` | `0x2774d1010` | 495 | ✓ |
| `dbg.__DllMainCRTStartup` | `0x2774d1200` | 324 | ✓ |
| `dbg.__mingw_TLScallback` | `0x2774d2530` | 224 | ✓ |
| `dbg._register_onexit_function` | `0x2774d2ad0` | 212 | — |
| `dbg.__mingw_enum_import_library_names` | `0x2774d2930` | 178 | — |
| `dbg._FindPESectionByName` | `0x2774d26a0` | 159 | — |
| `dbg.___w64_mingwthr_remove_key_dtor` | `0x2774d24a0` | 137 | — |
| `dbg._IsNonwritableInCurrentImage` | `0x2774d28a0` | 133 | — |
| `entry1` | `0x2774d1d90` | 129 | — |
| `dbg.__mingw_GetSectionForAddress` | `0x2774d2740` | 129 | — |
| `sym.eXAUbhzTCtyOBG_HINSTANCE____unsigned_long_` | `0x2774d13a0` | 126 | — |
| `sym.R3Y7oQBJcun5_void___clone_isra0_` | `0x2774d1480` | 125 | — |
| `dbg.___w64_mingwthr_add_key_dtor` | `0x2774d2420` | 120 | — |
| `dbg._execute_onexit_table` | `0x2774d2bb0` | 113 | — |
| `dbg.__report_error` | `0x2774d1e30` | 112 | — |
| `dbg._FindPESectionExec` | `0x2774d2800` | 108 | — |
| `sym.__mingwthr_run_key_dtors.part.0` | `0x2774d23b0` | 107 | — |
| `dbg.__do_global_ctors` | `0x2774d1cd0` | 106 | — |
| `sym.DllMain` | `0x2774d1be0` | 98 | — |
| `sym.QWRFuQJanc__EXCEPTION_POINTERS_` | `0x2774d1420` | 86 | — |
| `sym._FindPESection` | `0x2774d2650` | 72 | — |
| `sym.timeGetTime` | `0x2774d1b80` | 59 | — |
| `dbg.__do_global_dtors` | `0x2774d1c90` | 58 | — |
| `fcn.2774d2a00` | `0x2774d2a00` | 50 | — |
| `dbg.__dyn_tls_dtor` | `0x2774d1d60` | 47 | — |
| `dbg.__mingw_GetSectionCount` | `0x2774d27d0` | 43 | — |
| `dbg._GetPEImageBase` | `0x2774d2870` | 40 | — |

### Decompiled Code Files

- [`code/dbg.__DllMainCRTStartup.c`](code/dbg.__DllMainCRTStartup.c)
- [`code/dbg.__mingw_TLScallback.c`](code/dbg.__mingw_TLScallback.c)
- [`code/dbg._pei386_runtime_relocator.c`](code/dbg._pei386_runtime_relocator.c)
- [`code/sym.ABMHaBiVJ3j7z_DoWork__.c`](code/sym.ABMHaBiVJ3j7z_DoWork__.c)
- [`code/sym._CRT_INIT.c`](code/sym._CRT_INIT.c)
- [`code/sym.__write_memory.part.0.c`](code/sym.__write_memory.part.0.c)

## Behavioral Analysis

This code is characteristic of a **downloader and loader** (often referred to as a "stage-1" dropper). Its primary purpose is to bypass security measures, download an encrypted malicious payload from the internet, decrypt it in memory, and execute it.

### Core Functionality
*   **Anti-Analysis & Evasion:** The code begins by checking for the presence of debuggers using `IsDebuggerPresent` and `CheckRemoteDebuggerPresent`. If a debugger is not detected, it enters a calculated sleep state. This is designed to frustrate automated sandboxes (which often have short timeouts) and manual analysis.
*   **Decrypted Network Communication:** The code contains a series of large hexadecimal constants that, when reconstructed, form a URL. It uses the `WinInet` library (`InternetOpenA`, `InternetOpenUrlA`) to connect to this remote server and download data into a freshly allocated memory region via `VirtualAlloc`.
*   **In-Memory Decryption:** Once the data is downloaded, it passes through two distinct decoding loops. These use XOR operations and lookup tables (obfuscated constants) to decrypt the raw bytes in memory. This ensures that the actual malicious payload remains encrypted on disk and only appears "plain" in the system's RAM.
*   **Shellcode Execution via Thread Pool:** After decryption, the code identifies `ntdll.dll` in memory and changes its permissions to executable (RWX) using `VirtualProtect`. It then resolves specific functions from `ntdll.dll` related to the **Windows Thread Pool API** (`TpAllocWork`, `TpPostWork`, `TpReleaseWork`).

### Suspicious & Malicious Behaviors
*   **Anti-Debugging/Anti-Analysis:** The explicit checks for debuggers and the use of a calculated sleep timer are classic "anti-analysis" techniques used to hide malicious activity from security researchers.
*   **Downloader Behavior:** Using `InternetReadFile` into a large, newly allocated buffer (`0x1000000` or 16MB) is a standard way for malware to pull in secondary payloads (like RATs or ransomware).
*   **Reflective Loading/In-Memory Execution:** The code does not save the decrypted payload to a file on disk. It performs all "unpacking" operations directly in memory, a technique used to bypass traditional antivirus scanners that monitor the filesystem.
*   **Use of `ntdll` Thread Pool:** The specific use of `TpAllocWork` and `TpPostWork` is highly suspicious. This is a common technique (notably seen in frameworks like Cobalt Strike) to execute shellcode in a way that makes it harder for security tools to track the thread's origin or purpose.

### Notable Techniques & Patterns
*   **String Obfuscation:** The "messy" variables and large hex values used to build the URL are a sign of a packer or protector designed to hide strings from simple `strings` analysis.
*   **Memory Manipulation:** Using `VirtualProtect` to change memory permissions is a high-confidence indicator of shellcode execution preparation.
*   **Windows API abuse:** The combination of `WinInet` for networking and `ntdll.dll`'s internal thread pool functions for execution shows a sophisticated level of evasion, likely aiming to stay "under the radar" of Endpoint Detection and Response (EDR) systems.

### Summary for Incident Response
This binary is a **sophisticated loader**. It is designed to evade detection by security tools while fetching and executing an encrypted payload in memory. The presence of `ntdll` thread pool exploitation strongly suggests it may be part of a professional malware campaign or associated with a known threat actor's infrastructure (e.g., Cobalt Strike).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtual_Sandbox_Evasion | The use of `IsDebuggerPresent`, `CheckRemoteDebuggerPresent`, and calculated sleep timers are specifically intended to bypass automated analysis environments. |
| **T1105** | Ingress_Tool_Transfer | The code uses the `WinInet` library to fetch an external, remote payload from a constructed URL into memory. |
| **T1027** | Obfuscated_Files_or_Information | The use of XOR operations, lookup tables, and hex constants for string/URL construction is designed to hide malicious indicators from static analysis. |
| **T1106** | Native_API | The exploitation of `ntdll.dll` functions (like the Thread Pool API) is used to bypass EDR hooks that monitor standard Win32 API calls. |
| **T1059** | Command_and_Scripting_Interpreter (or Shellcode Execution Context) | While not a direct "Shellcode" technique, the manipulation of memory via `VirtualProtect` and subsequent execution in memory is the primary method for executing unauthorized code. |

***

### Analyst Notes:
*   **T1497 & T1027:** These represent the **Defense Evasion** tactic. The analyst noted "Ant-Analysis" specifically, which maps well to these techniques as they aim to hide the malicious nature of the loader before it can be detected by a human or an automated system.
*   **T1105:** This is the primary role of the binary. It functions as a "stage-1" downloader to pull in higher-level functionality.
*   **T1106:** The specific mention of **ntdll.dll Thread Pool** usage is a high-confidence indicator of advanced evasion. By calling into `ntdll` directly, the malware avoids many common hooks used by security products that monitor the Windows API layer.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `https://[obfuscated_path]files.ca` (Extracted from `https://H` and `files.ca`)
*   `tbox.moe` (Extracted from `tbox.moeH`; potentially a C2 domain or sub-domain)

**File paths / Registry keys**
*   *None identified.* (Note: Standard system libraries like `ntdll.dll`, `KERNEL32.dll`, and `WININET.dll` were excluded as false positives).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None available in the provided text.*

**Other artifacts**
*   **User-Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36` (Identified from mangled strings: `Mozilla/H 5.0 (WinH dows NT H 10.0; WiH n64; x64H ) AppleWH ebKit/53H`).
*   **C2 Infrastructure Pattern:** Use of the **ntdll thread pool** functions (`TpAllocWork`, `TpPostWork`, `TpReleaseWork`) to execute shellcode—a technique highly associated with Cobalt Strike.
*   **Evasion Techniques:** 
    *   Anti-debugging checks: `IsDebuggerPresent`, `CheckRemoteDebuggerPresent`.
    *   Memory manipulation via `VirtualProtect` to transition memory regions to RWX (Read-Write-Execute).
    *   In-memory decryption of payloads using XOR operations and lookup tables.

---

## Malware Family Classification

**Malware family:** Cobalt Strike
**Malware type:** Loader / Downloader
**Confidence:** High

**Key evidence:**
*   **Signature Techniques:** The specific use of `ntdll` thread pool functions (`TpAllocWork`, `TpPostWork`, `TpReleaseWork`) is a high-confidence signature associated with the **Cobalt Strike** framework to execute shellcode while bypassing EDR hooks.
*   **Loader Behavior:** The sample exhibits classic "stage-1" loader characteristics: it avoids writing decrypted payloads to disk, utilizes memory-only decryption (XOR/lookup tables), and uses `VirtualProtect` to transition memory to executable (RWX) status.
*   **Advanced Evasion:** The inclusion of multi-layered anti-analysis checks (both debuggers and sandboxes via sleep timers) combined with the use of `WinInet` for remote payload retrieval indicates a professional grade of malware designed to evade security telemetry.
