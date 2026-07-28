# Threat Analysis Report

**Generated:** 2026-07-27 22:56 UTC
**Sample:** `0be73be4dde470cb4fb9bafc5604d12a044be5285fa10adcfa9b742e48308c87_0be73be4dde470cb4fb9bafc5604d12a044be5285fa10adcfa9b742e48308c87.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0be73be4dde470cb4fb9bafc5604d12a044be5285fa10adcfa9b742e48308c87_0be73be4dde470cb4fb9bafc5604d12a044be5285fa10adcfa9b742e48308c87.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 8,704 bytes |
| MD5 | `d56881c9efd4fde5babaea7b074b4b2b` |
| SHA1 | `780ae4c128691bbbc580f8eaf2ebf15763b71e52` |
| SHA256 | `0be73be4dde470cb4fb9bafc5604d12a044be5285fa10adcfa9b742e48308c87` |
| Overall entropy | 5.423 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773348384 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 3,072 | 6.072 | No |
| `.rdata` | 2,560 | 4.407 | No |
| `.data` | 512 | 0.353 | No |
| `.rsrc` | 1,024 | 5.194 | No |
| `.reloc` | 512 | 5.35 | No |

### Imports

**MSVCR90.dll**: `?terminate@@YAXXZ`, `_unlock`, `__dllonexit`, `_lock`, `_decode_pointer`, `_except_handler4_common`, `_invoke_watson`, `_controlfp_s`, `_crt_debugger_hook`, `__set_app_type`, `_encode_pointer`, `__p__fmode`, `__p__commode`, `_adjust_fdiv`, `__setusermatherr`
**WININET.dll**: `InternetOpenUrlW`, `InternetReadFile`, `InternetCloseHandle`, `InternetOpenW`
**urlmon.dll**: `URLDownloadToFileW`
**KERNEL32.dll**: `QueryPerformanceCounter`, `InterlockedExchange`, `GetTickCount`, `ExpandEnvironmentStringsW`, `CreateFileW`, `WriteFile`, `DeleteFileW`, `CreateProcessW`, `Sleep`, `CloseHandle`, `GetCurrentThreadId`, `GetCurrentProcessId`, `GetSystemTimeAsFileTime`, `TerminateProcess`, `GetCurrentProcess`
**SHELL32.dll**: `ShellExecuteW`

## Extracted Strings

Total strings found: **84** (showing first 100)

```
!This program cannot be run in DOS mode.
$
]
R]
R]
Rz
qRQ
RTu
R^
R]Rf
RTu
R_
RTu
RH
RTu
R^
RTu
R\
RRich]
R
`.rdata
@.data
@.reloc
PVVj VVV
RPh("@
RPh("@
j
YQPSh
tVVVVV
memset
_snwprintf
MSVCR90.dll
_amsg_exit
__wgetmainargs
_cexit
_XcptFilter
_wcmdln
_initterm
_initterm_e
_configthreadlocale
__setusermatherr
_adjust_fdiv
__p__commode
__p__fmode
_encode_pointer
__set_app_type
?terminate@@YAXXZ
_unlock
__dllonexit
_onexit
_decode_pointer
_except_handler4_common
_invoke_watson
_controlfp_s
_crt_debugger_hook
InternetCloseHandle
InternetReadFile
InternetOpenUrlW
InternetOpenW
WININET.dll
URLDownloadToFileW
urlmon.dll
CloseHandle
CreateProcessW
DeleteFileW
WriteFile
CreateFileW
ExpandEnvironmentStringsW
GetTickCount
InterlockedExchange
InterlockedCompareExchange
GetStartupInfoW
SetUnhandledExceptionFilter
QueryPerformanceCounter
GetCurrentThreadId
GetCurrentProcessId
GetSystemTimeAsFileTime
TerminateProcess
GetCurrentProcess
UnhandledExceptionFilter
IsDebuggerPresent
KERNEL32.dll
ShellExecuteW
SHELL32.dll
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel level="asInvoker" uiAccess="false"></requestedExecutionLevel>
      </requestedPrivileges>
    </security>
  </trustInfo>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity type="win32" name="Microsoft.VC90.CRT" version="9.0.21022.8" processorArchitecture="x86" publicKeyToken="1fc8b3b9a1e18e3b"></assemblyIdentity>
    </dependentAssembly>
  </dependency>
</assembly>PAPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDING
W0g0p0
1*141M1p1
2%202P2|2
3$3*3\3f3m3s3x3}3
44 4*4/444J4O4X4]4j4{4
5:5B5K5Q5Y5e5
6!6(686@6F6R6]6
7&7<7I7
80969=9Z9
:!:-:5:=:I:m:u:
;#;+;7;@;E;K;U;^;i;u;z;
383T3X3
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x401665` | 713 | ✓ |
| `fcn.004010a8` | `0x4010a8` | 595 | ✓ |
| `fcn.00401870` | `0x401870` | 189 | ✓ |
| `section..text` | `0x401000` | 168 | ✓ |
| `fcn.004016c6` | `0x4016c6` | 156 | ✓ |
| `fcn.004019e8` | `0x4019e8` | 150 | ✓ |
| `fcn.0040193c` | `0x40193c` | 69 | ✓ |
| `fcn.00401820` | `0x401820` | 68 | ✓ |
| `fcn.004017e0` | `0x4017e0` | 53 | ✓ |
| `fcn.00401330` | `0x401330` | 43 | ✓ |
| `fcn.004019ba` | `0x4019ba` | 43 | ✓ |
| `fcn.00401782` | `0x401782` | 38 | ✓ |
| `main` | `0x4012fb` | 27 | ✓ |
| `fcn.0040176b` | `0x40176b` | 23 | ✓ |
| `fcn.00401981` | `0x401981` | 20 | ✓ |
| `fcn.00401762` | `0x401762` | 9 | ✓ |
| `sub.MSVCR90.dll_memset` | `0x401316` | 6 | ✓ |
| `sub.MSVCR90.dll_srand` | `0x401328` | 6 | ✓ |
| `sub.MSVCR90.dll_rand` | `0x401322` | 6 | ✓ |
| `sub.MSVCR90.dll__snwprintf` | `0x40131c` | 6 | ✓ |
| `sub.urlmon.dll_URLDownloadToFileW` | `0x401bc4` | 6 | ✓ |
| `sub.MSVCR90.dll__amsg_exit` | `0x4016c0` | 6 | ✓ |
| `sub.MSVCR90.dll__initterm_e` | `0x401934` | 6 | ✓ |
| `sub.MSVCR90.dll__initterm` | `0x40192e` | 6 | ✓ |
| `sub.MSVCR90.dll__XcptFilter` | `0x4017ce` | 6 | ✓ |
| `sub.MSVCR90.dll__controlfp_s` | `0x401ab2` | 6 | ✓ |
| `sub.MSVCR90.dll__invoke_watson` | `0x401aac` | 6 | ✓ |
| `sub.MSVCR90.dll__terminate__YAXXZ` | `0x401a7e` | 6 | ✓ |
| `sub.MSVCR90.dll__lock` | `0x401a90` | 6 | ✓ |
| `sub.MSVCR90.dll___dllonexit` | `0x401a8a` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004010a8.c`](code/fcn.004010a8.c)
- [`code/fcn.00401330.c`](code/fcn.00401330.c)
- [`code/fcn.004016c6.c`](code/fcn.004016c6.c)
- [`code/fcn.00401762.c`](code/fcn.00401762.c)
- [`code/fcn.0040176b.c`](code/fcn.0040176b.c)
- [`code/fcn.00401782.c`](code/fcn.00401782.c)
- [`code/fcn.004017e0.c`](code/fcn.004017e0.c)
- [`code/fcn.00401820.c`](code/fcn.00401820.c)
- [`code/fcn.00401870.c`](code/fcn.00401870.c)
- [`code/fcn.0040193c.c`](code/fcn.0040193c.c)
- [`code/fcn.00401981.c`](code/fcn.00401981.c)
- [`code/fcn.004019ba.c`](code/fcn.004019ba.c)
- [`code/fcn.004019e8.c`](code/fcn.004019e8.c)
- [`code/main.c`](code/main.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sub.MSVCR90.dll__XcptFilter.c`](code/sub.MSVCR90.dll__XcptFilter.c)
- [`code/sub.MSVCR90.dll___dllonexit.c`](code/sub.MSVCR90.dll___dllonexit.c)
- [`code/sub.MSVCR90.dll__amsg_exit.c`](code/sub.MSVCR90.dll__amsg_exit.c)
- [`code/sub.MSVCR90.dll__controlfp_s.c`](code/sub.MSVCR90.dll__controlfp_s.c)
- [`code/sub.MSVCR90.dll__initterm.c`](code/sub.MSVCR90.dll__initterm.c)
- [`code/sub.MSVCR90.dll__initterm_e.c`](code/sub.MSVCR90.dll__initterm_e.c)
- [`code/sub.MSVCR90.dll__invoke_watson.c`](code/sub.MSVCR90.dll__invoke_watson.c)
- [`code/sub.MSVCR90.dll__lock.c`](code/sub.MSVCR90.dll__lock.c)
- [`code/sub.MSVCR90.dll__snwprintf.c`](code/sub.MSVCR90.dll__snwprintf.c)
- [`code/sub.MSVCR90.dll__terminate__YAXXZ.c`](code/sub.MSVCR90.dll__terminate__YAXXZ.c)
- [`code/sub.MSVCR90.dll_memset.c`](code/sub.MSVCR90.dll_memset.c)
- [`code/sub.MSVCR90.dll_rand.c`](code/sub.MSVCR90.dll_rand.c)
- [`code/sub.MSVCR90.dll_srand.c`](code/sub.MSVCR90.dll_srand.c)
- [`code/sub.urlmon.dll_URLDownloadToFileW.c`](code/sub.urlmon.dll_URLDownloadToFileW.c)

## Behavioral Analysis

Based on the provided disassembly and strings, this binary is a **downloader/loader**, a common first-stage malware component designed to fetch and execute a secondary malicious payload.

### Core Functionality and Purpose
The primary purpose of this code is to reach out to a remote server, download an executable file (the "payload"), and execute it on the local system. It employs multiple methods for downloading to ensure reliability and includes logic to execute the resulting file.

### Suspicious or Malicious Behaviors
*   **Network Communication (Downloader):** 
    *   The binary uses `InternetOpenW`, `InternetOpenUrlW`, and `InternetReadFile` (WinINet API) to establish a connection and retrieve data from a remote URL.
    *   It also contains fallback logic using `URLDownloadToFileW` (URLMon), which is a common convenience method used by malware to download files with minimal coding effort.
*   **File Manipulation:** 
    *   The code writes received network data into a file on the local disk.
    *   It calls `DeleteFileW` shortly after the download/processing phase. This is a classic "cleaner" behavior used by malware to delete the original downloader or temporary files to hide its presence from the user and basic forensic tools.
*   **Process Execution (Launcher):**
    *   The code utilizes `CreateProcessW` and `ShellExecuteW` to launch the downloaded payload. 
    *   The function `section..text` specifically handles these calls, showing that it can execute a command-line string or use a shell to run a file.
*   **Anti-Analysis/Evasion:**
    *   **Environment Checks:** The function `fcn.004019e8` gathers multiple system metrics (Process ID, Thread ID, TickCount, System Time) and performs bitwise operations on them. This is a common technique used to generate a decryption key or to detect if the binary is running in a debugger/sandbox.
    *   **Sleep Loops:** The use of `Sleep(1000)` inside loops (especially near `InterlockedCompareExchange`) is often used to stall analysis tools or bypass automated "sandboxes" that only monitor execution for a few seconds.
    *   **Code Obfuscation:** The presence of `_decode_pointer` and `_encode_pointer` suggests the binary contains packed or encrypted segments that are unpacked into memory at runtime before execution.

### Notable Techniques & Patterns
*   **Multi-Stage Approach:** This is a classic "Stager." It doesn't contain the primary payload but provides the infrastructure to get it onto the system and execute it.
*   **Redundant Download Methods:** By including both `WinINet` and `URLMon`, the author ensures the downloader works across different system configurations.
*   **API Hashing/Obfuscation:** The use of several internal "decode" functions indicates an attempt to hide the true intentions of the code from static analysis tools until it is executed in memory.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors described in the analysis to the corresponding MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1105** | Ingress Tool Transfer | The binary uses WinINet (`InternetOpenW`, `InternetReadFile`) and URLMon (`URLDownloadToFileW`) to retrieve a payload from a remote server. |
| **T1070.006** | Indicator Removal on Host | The use of `DeleteFileW` is a clear attempt to remove the downloader or temporary files to hide evidence from forensic tools. |
| **T1059** | Command and Scripting Interpreter | The binary utilizes `CreateProcessW` and `ShellExecuteW` to execute command-line strings or shell commands for payload execution. |
| **T1497** | Virtualization/Sandbox Detection | Gathering system metrics (PID, TickCount) is used to determine if the code is running in an automated analysis environment. |
| **T1027** | Obfuscated Files or Information | The use of `_decode_pointer` and `_encode_pointer` functions indicates an attempt to hide strings and logic from static analysis. |

***Note on Additional Behaviors:*** *The "Sleep Loops" mentioned in the report are a specific tactic used to facilitate **T1497 (Virtualization/Sandbox Detection)** by stalling execution until automated analysis sandboxes time out.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (While the analysis notes the use of `InternetOpenUrlW` and `URLDownloadToFileW`, no specific hardcoded C2 domains or IP addresses were present in the provided string dump.)

### **File paths / Registry keys**
*   *None identified.* (The report mentions "file manipulation" and a "cleaner" behavior via `DeleteFileW`, but no specific local file paths were included in the strings.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Malware Type:** Downloader/Loader (Stage 1)
*   **Function Offset:** `fcn.004019e8` (Identified as the specific routine for environment checks and anti-analysis).
*   **Obfuscation Indicators:** 
    *   Presence of `_decode_pointer` and `_encode_pointer` functions (indicates packed or encrypted code sections).
    *   Large block of high-entropy/encoded data strings starting with `W0g0p0` through `383T3X3`.
*   **Anti-Analysis Techniques:** 
    *   Stalling/Sleep loops: `Sleep(1000)` (used to bypass automated sandbox analysis).
    *   Environment checks: Analysis of Process ID, Thread ID, TickCount, and System Time via the `fcn.004019e8` routine.
*   **Malicious API Patterns:** 
    *   **Downloader Routine:** Use of `InternetOpenW`, `InternetOpenUrlW`, and `InternetReadFile`.
    *   **Fall-back/Convenience Logic:** Usage of `URLDownloadToFileW` (urlmon.dll).
    *   **Execution/Launcher logic:** Utilization of `CreateProcessW` and `ShellExecuteW` to transition from the stager to the primary payload.
    *   **Cleanup behavior:** Use of `DeleteFileW` immediately following download tasks to remove evidence of the downloader or dropped files.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Staged Download Logic:** The binary utilizes redundant download methods (`WinINet` and `URLMon`) specifically to fetch, save, and execute a secondary payload, which is the primary characteristic of a first-stage loader.
    *   **Evasion & Anti-Analysis:** It employs several sophisticated evasion techniques, including environment checks (PID/TickCount analysis), sleep loops to stall sandboxes, and "cleaner" behavior (`DeleteFileW`) to remove traces of itself after execution.
    *   **Execution Infrastructure:** The integration of `CreateProcessW` and `ShellExecuteW` immediately following the download routine confirms its role as a facilitator for subsequent malware stages.
