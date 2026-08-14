# Threat Analysis Report

**Generated:** 2026-08-12 20:33 UTC
**Sample:** `0e90a3a7cfa876bb10a2e8711bbff64955f709b39df6abb3aa76f85328fc6a91_0e90a3a7cfa876bb10a2e8711bbff64955f709b39df6abb3aa76f85328fc6a91.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e90a3a7cfa876bb10a2e8711bbff64955f709b39df6abb3aa76f85328fc6a91_0e90a3a7cfa876bb10a2e8711bbff64955f709b39df6abb3aa76f85328fc6a91.exe` |
| File type | PE32+ executable for MS Windows 5.02 (DLL), x86-64 (stripped to external PDB), 11 sections |
| Size | 18,432 bytes |
| MD5 | `0859f93ed53ac3cceb08f99a6764f653` |
| SHA1 | `a5ccf263218cc595e9bb04401716aa4f2f69d966` |
| SHA256 | `0e90a3a7cfa876bb10a2e8711bbff64955f709b39df6abb3aa76f85328fc6a91` |
| Overall entropy | 5.035 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1640610757 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 9,216 | 6.007 | No |
| `.data` | 512 | 1.638 | No |
| `.rdata` | 1,536 | 4.048 | No |
| `.pdata` | 1,024 | 2.847 | No |
| `.xdata` | 512 | 3.667 | No |
| `.bss` | 0 | 0.0 | No |
| `.edata` | 1,024 | 3.192 | No |
| `.idata` | 2,048 | 3.595 | No |
| `.CRT` | 512 | 0.253 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 512 | 1.023 | No |

### Imports

**ADVAPI32.dll**: `RegCloseKey`, `RegOpenKeyExA`, `RegQueryValueExA`, `RegSetValueExA`
**KERNEL32.dll**: `CheckRemoteDebuggerPresent`, `CloseHandle`, `DeleteCriticalSection`, `DisableThreadLibraryCalls`, `EnterCriticalSection`, `FlushInstructionCache`, `GetCurrentProcess`, `GetLastError`, `GetModuleFileNameA`, `GetModuleHandleA`, `GetProcAddress`, `GetTickCount`, `InitializeCriticalSection`, `IsDebuggerPresent`, `LeaveCriticalSection`
**msvcrt.dll**: `__iob_func`, `_amsg_exit`, `_initterm`, `_lock`, `_unlock`, `abort`, `calloc`, `free`, `fwrite`, `memset`, `realloc`, `strlen`, `strncmp`, `vfprintf`
**USER32.dll**: `DispatchMessageA`, `GetMessageA`, `TranslateMessage`

### Exports

`GetFileVersionInfoA`, `GetFileVersionInfoByHandle`, `GetFileVersionInfoExA`, `GetFileVersionInfoExW`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoSizeExA`, `GetFileVersionInfoSizeExW`, `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`, `VerFindFileA`, `VerFindFileW`, `VerInstallFileA`, `VerInstallFileW`, `VerLanguageNameA`, `VerLanguageNameW`, `VerQueryValueA`, `VerQueryValueW`

## Extracted Strings

Total strings found: **151** (showing first 100)

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
AUATSH
kernel32
D$D.dll
wininet.H
D$,dll
VirtualAH
VirtualPH
VirtualFH
CreateTh
D$Qlloc
D$yrote
D$8ree
D$^read
InternetL
OpenUrlA
D$kOpenH
InternetH
InternetH
ReadFileH
InternetH
CloseHanH
AWAVAUATUWVSH
https://H
files.ca
tbox.moeH
/2e3lqs.H
5.0 (Win
Mozilla/H
10.0; WiH
dows NT H
) AppleWH
n64; x64H
ebKit/53H
Ic|$<L
[^_]A\A]A^A_
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
Software\Microsoft\Windows\CurrentVersion\Run
EdgeUpdate
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
VERSION.dll
GetFileVersionInfoA
GetFileVersionInfoByHandle
GetFileVersionInfoExA
GetFileVersionInfoExW
GetFileVersionInfoSizeA
GetFileVersionInfoSizeExA
GetFileVersionInfoSizeExW
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.35df32220` | `0x35df32220` | 7556 | ✓ |
| `fcn.35df315f0` | `0x35df315f0` | 1996 | ✓ |
| `fcn.35df32610` | `0x35df32610` | 752 | ✓ |
| `fcn.35df313a0` | `0x35df313a0` | 579 | ✓ |
| `fcn.35df323f0` | `0x35df323f0` | 544 | ✓ |
| `fcn.35df31010` | `0x35df31010` | 495 | ✓ |
| `entry0` | `0x35df31350` | 354 | ✓ |
| `fcn.35df32a80` | `0x35df32a80` | 224 | ✓ |
| `entry1` | `0x35df322e0` | 129 | ✓ |
| `fcn.35df32c90` | `0x35df32c90` | 129 | ✓ |
| `fcn.35df33100` | `0x35df33100` | 113 | ✓ |
| `fcn.35df32380` | `0x35df32380` | 112 | ✓ |
| `fcn.35df32900` | `0x35df32900` | 107 | ✓ |
| `fcn.35df32130` | `0x35df32130` | 98 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoSizeA` | `0x35df31e80` | 57 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoSizeExA` | `0x35df31ec0` | 57 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoSizeExW` | `0x35df31f00` | 57 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoSizeW` | `0x35df31f40` | 57 | ✓ |
| `fcn.35df32f50` | `0x35df32f50` | 50 | ✓ |
| `entry2` | `0x35df322b0` | 47 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoA` | `0x35df31dc0` | 46 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoByHandle` | `0x35df31df0` | 46 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoExA` | `0x35df31e20` | 46 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoExW` | `0x35df31e50` | 46 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoW` | `0x35df31f80` | 46 | ✓ |
| `sym.VERSION.dll_VerFindFileA` | `0x35df31fb0` | 46 | ✓ |
| `sym.VERSION.dll_VerFindFileW` | `0x35df31fe0` | 46 | ✓ |
| `sym.VERSION.dll_VerInstallFileA` | `0x35df32010` | 46 | ✓ |
| `sym.VERSION.dll_VerInstallFileW` | `0x35df32040` | 46 | ✓ |
| `sym.VERSION.dll_VerLanguageNameA` | `0x35df32070` | 46 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/entry1.c`](code/entry1.c)
- [`code/entry2.c`](code/entry2.c)
- [`code/fcn.35df31010.c`](code/fcn.35df31010.c)
- [`code/fcn.35df313a0.c`](code/fcn.35df313a0.c)
- [`code/fcn.35df315f0.c`](code/fcn.35df315f0.c)
- [`code/fcn.35df32130.c`](code/fcn.35df32130.c)
- [`code/fcn.35df32220.c`](code/fcn.35df32220.c)
- [`code/fcn.35df32380.c`](code/fcn.35df32380.c)
- [`code/fcn.35df323f0.c`](code/fcn.35df323f0.c)
- [`code/fcn.35df32610.c`](code/fcn.35df32610.c)
- [`code/fcn.35df32900.c`](code/fcn.35df32900.c)
- [`code/fcn.35df32a80.c`](code/fcn.35df32a80.c)
- [`code/fcn.35df32c90.c`](code/fcn.35df32c90.c)
- [`code/fcn.35df32f50.c`](code/fcn.35df32f50.c)
- [`code/fcn.35df33100.c`](code/fcn.35df33100.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoA.c`](code/sym.VERSION.dll_GetFileVersionInfoA.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoByHandle.c`](code/sym.VERSION.dll_GetFileVersionInfoByHandle.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoExA.c`](code/sym.VERSION.dll_GetFileVersionInfoExA.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoExW.c`](code/sym.VERSION.dll_GetFileVersionInfoExW.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoSizeA.c`](code/sym.VERSION.dll_GetFileVersionInfoSizeA.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoSizeExA.c`](code/sym.VERSION.dll_GetFileVersionInfoSizeExA.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoSizeExW.c`](code/sym.VERSION.dll_GetFileVersionInfoSizeExW.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoSizeW.c`](code/sym.VERSION.dll_GetFileVersionInfoSizeW.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoW.c`](code/sym.VERSION.dll_GetFileVersionInfoW.c)
- [`code/sym.VERSION.dll_VerFindFileA.c`](code/sym.VERSION.dll_VerFindFileA.c)
- [`code/sym.VERSION.dll_VerFindFileW.c`](code/sym.VERSION.dll_VerFindFileW.c)
- [`code/sym.VERSION.dll_VerInstallFileA.c`](code/sym.VERSION.dll_VerInstallFileA.c)
- [`code/sym.VERSION.dll_VerInstallFileW.c`](code/sym.VERSION.dll_VerInstallFileW.c)
- [`code/sym.VERSION.dll_VerLanguageNameA.c`](code/sym.VERSION.dll_VerLanguageNameA.c)

## Behavioral Analysis

Based on the provided disassembly and strings, this binary is a **malware loader (downloader/dropper)** designed to perform several stages of infection: anti-analysis, persistence, payload decryption, and manual mapping of a malicious executable into memory.

### Core Functionality
The primary purpose of this code is to serve as a "stub" or "loader." It establishes a persistent foothold on the system, fetches an encrypted/hidden secondary stage (the actual payload), and injects it into the process space using techniques designed to evade traditional security software.

### Suspicious and Malicious Behaviors

*   **Persistence via Registry Manipulation:**
    *   The code interacts with the Windows Registry key: `Software\Microsoft\Windows\CurrentVersion\Run`.
    *   It specifically targets a value named **"EdgeUpdate"**. 
    *   It checks if this value already exists; if not, it sets the path of its own executable to that key. This ensures the malware executes automatically every time the user starts their computer, masquerading as a legitimate Microsoft Edge update service.

*   **Anti-Analysis & Anti-Debugging:**
    *   The code uses `IsDebuggerPresent` and `CheckRemoteDebuggerPresent`. 
    *   If a debugger is detected, it generates a "dummy" value using `GetTickCount()` (a time-based check) and terminates or enters a stalled loop. This is designed to prevent researchers from analyzing the payload in a debugger.

*   **Manual Mapping & Reflective Loading:**
    *   Rather than using standard Windows APIs like `LoadLibrary` to run the final stage, it performs **manual mapping**. 
    *   It parses a raw "MZ" (0x5A4D) and "PE" header from an internal buffer.
    *   It manually iterates through the PE headers to resolve relocations (`reloc`), map sections into memory via `VirtualProtect`, and resolve imports using `GetProcAddress`. This is a common technique used to bypass EDR (Endpoint Detection and Response) systems that monitor for suspicious API calls during standard DLL loading.

*   **In-Memory Decryption/Deobfuscation:**
    *   The code contains heavy nested loops involving XOR operations and byte manipulation on internal buffers. 
    *   It takes an obfuscated block of data (the "hidden" payload) and transforms it into a runnable executable format in memory before execution begins.

### Notable Techniques & Patterns

*   **WinINet API Wrapping:** The strings suggest the use of `InternetOpen`, `InternetConnect`, and `InternetReadFile`. These are used to reach out to remote servers (the URLs found in the strings, such as those involving `tbox.moe` or `files.ca`) to download the payload.
*   **API Obfuscation:** The code manually resolves several WinINT functions (like those for handling browser-agent headers). It uses a custom mechanism to find these addresses rather than relying on standard naming, which can hide its intent from basic automated scanners.
*   **Evasive Memory Management:** Use of `VirtualProtect` is frequent in the disassembly. This indicates it is changing memory segments from "Read/Write" to "Execute" (RWX), a classic indicator of a loader preparing an injected payload for execution.
*   **Masquerading:** The use of the string "EdgeUpdate" as both the registry key and the context for its operation is a clear attempt to hide among common system processes.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys/Startup Folder | The malware modifies the `\CurrentVersion\Run` registry key to ensure it executes automatically upon system startup. |
| **T1105** | Ingress Tool Transfer | The use of WinINet APIs (`InternetOpen`, `InternetConnect`, etc.) indicates the loader is designed to download a secondary payload from a remote server. |
| **T1106** | Native API | The manual resolution of WinINT functions and avoidance of standard named imports are used to hide the malware's intent from basic security scanners. |
| **T1027** | Obfuscated Files or Information | The use of nested XOR loops and byte manipulation is intended to deobfuscate a "hidden" payload in memory before execution. |
| **T1631** | Manipulation of System Memory | The frequent use of `VirtualProtect` to transition memory segments to RWX (Read/Write/Execute) is a signature of preparing an injected payload for execution. |
| **T1036** | Create Shortcut (Masquerading context) | While not a literal "shortcut," the naming of the registry key as "EdgeUpdate" is a classic masquerading tactic to blend in with legitimate system processes. |

***Note on Defense Evasion:** The "Anti-Analysis & Anti-Debugging" section (using `IsDebuggerPresent` and `CheckRemoteDebuggerPresent`) specifically falls under the broader **Defense Evasion** tactic.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `files.ca`
*   `tbox.moe`

**File paths / Registry keys**
*   **Registry Key:** `Software\Microsoft\Windows\CurrentVersion\Run`
*   **Registry Value:** `EdgeUpdate` (Used for persistence)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **User-Agent Strings:** `Mozilla/`, `AppleWH`, `10.0; Win` (Identified as components of a custom or hardcoded User-Agent used for C2 communication).
*   **C2 Communication Pattern:** The presence of `InternetOpen`, `InternetConnect`, and `InternetReadFile` (obfuscated in strings as `InternetH`, `OpenUrlA`) indicates the use of the WinINet library to fetch remote payloads.
*   **Evasive Behavior:** Use of "Manual Mapping" and "Reflective Loading" to bypass EDR systems by manually resolving imports and mapping the PE header into memory.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
*   **Manual Mapping & Reflection:** The sample avoids standard Windows APIs (like `LoadLibrary`) in favor of manual PE header parsing and `VirtualProtect` manipulation to inject a secondary payload, a signature behavior of advanced loaders designed to bypass EDR systems.
*   **Persistence through Masquerading:** It utilizes the "EdgeUpdate" registry key under the `Run` key, specifically intended to blend in with legitimate system processes while ensuring it remains active across reboots.
*   **Multi-stage Execution Pipeline:** The combination of in-memory XOR deobfuscation, WinINet-based remote downloading (from domains like `tbox.moe`), and anti-debugging checks confirms its role as a "stub" designed to deliver a more complex primary payload.
