# Threat Analysis Report

**Generated:** 2026-06-24 17:48 UTC
**Sample:** `00ad2d7a4e9bec38ac628326a53c196c7f8d396588a1235d9d5c3921c6d9ecfe_00ad2d7a4e9bec38ac628326a53c196c7f8d396588a1235d9d5c3921c6d9ecfe.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00ad2d7a4e9bec38ac628326a53c196c7f8d396588a1235d9d5c3921c6d9ecfe_00ad2d7a4e9bec38ac628326a53c196c7f8d396588a1235d9d5c3921c6d9ecfe.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 11,264 bytes |
| MD5 | `e58a4a8bed24df371f7bc7f4267ce687` |
| SHA1 | `66862757fe6c0bc55ffb8f2a98356a709c118649` |
| SHA256 | `00ad2d7a4e9bec38ac628326a53c196c7f8d396588a1235d9d5c3921c6d9ecfe` |
| Overall entropy | 5.449 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1776804281 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 3,584 | 6.08 | No |
| `.rdata` | 3,072 | 4.558 | No |
| `.data` | 1,536 | 1.305 | No |
| `.rsrc` | 1,024 | 5.194 | No |
| `.reloc` | 1,024 | 3.599 | No |

### Imports

**MSVCR90.dll**: `__dllonexit`, `_lock`, `_onexit`, `_unlock`, `_except_handler4_common`, `_invoke_watson`, `_controlfp_s`, `_crt_debugger_hook`, `?terminate@@YAXXZ`, `__set_app_type`, `_encode_pointer`, `__p__fmode`, `__p__commode`, `_adjust_fdiv`, `__setusermatherr`
**WININET.dll**: `InternetOpenW`, `InternetReadFile`, `InternetCloseHandle`, `InternetOpenUrlW`
**SHLWAPI.dll**: `PathCombineW`, `PathFileExistsW`
**urlmon.dll**: `URLDownloadToFileW`
**KERNEL32.dll**: `QueryPerformanceCounter`, `InterlockedExchange`, `GetModuleHandleW`, `GetProcAddress`, `GetTickCount`, `ExpandEnvironmentStringsW`, `CreateFileW`, `WriteFile`, `DeleteFileW`, `CreateProcessW`, `Sleep`, `CloseHandle`, `GetCurrentThreadId`, `GetCurrentProcessId`, `GetSystemTimeAsFileTime`
**USER32.dll**: `wsprintfW`
**SHELL32.dll**: `ShellExecuteW`

## Extracted Strings

Total strings found: **96** (showing first 100)

```
!This program cannot be run in DOS mode.
$
]%
R]%
R]%
Rz
qRQ%
RT]
R^%
R]%R`%
RT]
R_%
RT]
RH%
RT]
R^%
RT]
R\%
RRich]%
R
`.rdata
@.data
@.reloc
PVVj VVV
RPhH"@
RPhH"@
t`h4#@
j
YQPSh
tVVVVV
RtlGetVersion
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
PathFileExistsW
PathCombineW
SHLWAPI.dll
URLDownloadToFileW
urlmon.dll
CloseHandle
CreateProcessW
DeleteFileW
WriteFile
CreateFileW
ExpandEnvironmentStringsW
GetTickCount
GetProcAddress
GetModuleHandleW
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
wsprintfW
USER32.dll
ShellExecuteW
SHELL32.dll
3338383883838383833383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838333838388383838383338383883838383833383838838383838
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
3$323?3\3h3
4*4@4F4O4V4
5"5(5.545l5v5}5
606:6?6D6Z6_6h6m6z6
7J7R7[7a7i7u7
8$8*81888H8P8V8b8m8
969L9Y9
:@;F;M;j;
<$<1<=<E<M<Y<}<
=#=+=3=;=G=P=U=[=e=n=y=
5 5(5,5H5d5h5
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x401875` | 713 | ✓ |
| `fcn.004010a8` | `0x4010a8` | 595 | ✓ |
| `fcn.00401a80` | `0x401a80` | 189 | ✓ |
| `section..text` | `0x401000` | 168 | ✓ |
| `fcn.004018d6` | `0x4018d6` | 156 | ✓ |
| `fcn.00401bf8` | `0x401bf8` | 150 | ✓ |
| `fcn.00401435` | `0x401435` | 126 | ✓ |
| `fcn.004012fb` | `0x4012fb` | 117 | ✓ |
| `fcn.00401370` | `0x401370` | 117 | ✓ |
| `main` | `0x4014b3` | 108 | ✓ |
| `fcn.004013e5` | `0x4013e5` | 80 | ✓ |
| `fcn.00401b4c` | `0x401b4c` | 69 | ✓ |
| `fcn.00401a30` | `0x401a30` | 68 | ✓ |
| `fcn.004019f0` | `0x4019f0` | 53 | ✓ |
| `fcn.00401540` | `0x401540` | 43 | ✓ |
| `fcn.00401bca` | `0x401bca` | 43 | ✓ |
| `fcn.00401992` | `0x401992` | 38 | ✓ |
| `fcn.0040197b` | `0x40197b` | 23 | ✓ |
| `fcn.00401b91` | `0x401b91` | 20 | ✓ |
| `fcn.00401972` | `0x401972` | 9 | ✓ |
| `sub.MSVCR90.dll_memset` | `0x401520` | 6 | ✓ |
| `sub.MSVCR90.dll_srand` | `0x401532` | 6 | ✓ |
| `sub.MSVCR90.dll_rand` | `0x40152c` | 6 | ✓ |
| `sub.MSVCR90.dll__snwprintf` | `0x401526` | 6 | ✓ |
| `sub.urlmon.dll_URLDownloadToFileW` | `0x401dd4` | 6 | ✓ |
| `sub.MSVCR90.dll__amsg_exit` | `0x4018d0` | 6 | ✓ |
| `sub.MSVCR90.dll__initterm_e` | `0x401b44` | 6 | ✓ |
| `sub.MSVCR90.dll__initterm` | `0x401b3e` | 6 | ✓ |
| `sub.MSVCR90.dll__XcptFilter` | `0x4019de` | 6 | ✓ |
| `sub.MSVCR90.dll__controlfp_s` | `0x401cc2` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004010a8.c`](code/fcn.004010a8.c)
- [`code/fcn.004012fb.c`](code/fcn.004012fb.c)
- [`code/fcn.00401370.c`](code/fcn.00401370.c)
- [`code/fcn.004013e5.c`](code/fcn.004013e5.c)
- [`code/fcn.00401435.c`](code/fcn.00401435.c)
- [`code/fcn.00401540.c`](code/fcn.00401540.c)
- [`code/fcn.004018d6.c`](code/fcn.004018d6.c)
- [`code/fcn.00401972.c`](code/fcn.00401972.c)
- [`code/fcn.0040197b.c`](code/fcn.0040197b.c)
- [`code/fcn.00401992.c`](code/fcn.00401992.c)
- [`code/fcn.004019f0.c`](code/fcn.004019f0.c)
- [`code/fcn.00401a30.c`](code/fcn.00401a30.c)
- [`code/fcn.00401a80.c`](code/fcn.00401a80.c)
- [`code/fcn.00401b4c.c`](code/fcn.00401b4c.c)
- [`code/fcn.00401b91.c`](code/fcn.00401b91.c)
- [`code/fcn.00401bca.c`](code/fcn.00401bca.c)
- [`code/fcn.00401bf8.c`](code/fcn.00401bf8.c)
- [`code/main.c`](code/main.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sub.MSVCR90.dll__XcptFilter.c`](code/sub.MSVCR90.dll__XcptFilter.c)
- [`code/sub.MSVCR90.dll__amsg_exit.c`](code/sub.MSVCR90.dll__amsg_exit.c)
- [`code/sub.MSVCR90.dll__controlfp_s.c`](code/sub.MSVCR90.dll__controlfp_s.c)
- [`code/sub.MSVCR90.dll__initterm.c`](code/sub.MSVCR90.dll__initterm.c)
- [`code/sub.MSVCR90.dll__initterm_e.c`](code/sub.MSVCR90.dll__initterm_e.c)
- [`code/sub.MSVCR90.dll__snwprintf.c`](code/sub.MSVCR90.dll__snwprintf.c)
- [`code/sub.MSVCR90.dll_memset.c`](code/sub.MSVCR90.dll_memset.c)
- [`code/sub.MSVCR90.dll_rand.c`](code/sub.MSVCR90.dll_rand.c)
- [`code/sub.MSVCR90.dll_srand.c`](code/sub.MSVCR90.dll_srand.c)
- [`code/sub.urlmon.dll_URLDownloadToFileW.c`](code/sub.urlmon.dll_URLDownloadToFileW.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C code, here is an analysis of the binary's functionality.

### Core Functionality and Purpose
The binary functions primarily as a **Downloader** or **Dropper**. Its main role is to establish a connection to a remote server, download a payload (such as a malicious executable or script), save it to the local file system, and subsequently execute it.

### Suspicious or Malicious Behaviors
*   **Network Communication & Payload Download:** 
    *   The code utilizes `WININET.dll` (`InternetOpenW`, `InternetOpenUrlW`) and `urlmon.dll` (`URLDownloadToFileW`). This is a classic pattern for reaching out to a Command & Control (C2) server or a hosting site to fetch remote content.
    *   It implements a fallback mechanism: it first attempts to manually download data using `InternetReadFile` into a buffer, and if that fails, it falls back to the higher-level `URLDownloadToFileW` function.
*   **File Manipulation (Dropping):** 
    *   The code uses `ExpandEnvironmentStringsW` to locate the `%appdata%` directory. This is a common technique to find a "safe" location where the malware can hide its payload without requiring administrative privileges.
    *   It creates files with randomized/obfuscated names (e.g., `d33333333...txt`) in the user's data folders. 
*   **Execution of Payload:** 
    *   The function `section..text` contains logic to execute a command. It uses both `CreateProcessW` and `ShellExecuteW`. This indicates that once a file is downloaded, the malware will launch it on the system.
*   **Persistence/Staging:**
    *   The logic in `main` shows a sequential execution flow: check for environment conditions $\rightarrow$ download payload $\rightarrow$ verify system paths $\rightarrow$ execute.

### Notable Techniques & Patterns
*   **Anti-Analysis / Environment Checking:** 
    *   **Environment Key Generation:** In function `fcn.00401bf8`, the code gathers multiple system metrics (`GetSystemTimeAsFileTime`, `GetCurrentProcessId`, `GetTickCount`, and `QueryPerformanceCounter`) and XORs/combines them to check against a hardcoded value (`0xbb40e64e`). This is often used to detect if the program is running in a sandbox or virtual machine by checking for inconsistencies in timing or hardware IDs.
    *   **Version Checking:** The use of `RtlGetVersion` (in `fcn.00401435`) is frequently used to determine if the OS is a specific build or if it's running within an emulator/VM.
*   **Evasion via Multiple Download Methods:** By implementing both manual WinINet calls and the Windows URLMon API, the malware increases its chances of successfully "calling home" even if one specific method is flagged or blocked by local security software.
*   **Obfuscated File Paths:** The use of long numeric strings for filenames in the `%appdata%` path suggests an attempt to blend in with temporary files or make analysis harder by avoiding obviously malicious names.

### Summary Table of Indicators
| Behavior | Function(s) | Risk Level |
| :--- | :--- | :--- |
| **Downloader** | `fcn.004010a8`, `urlmon.dll` | High |
| **File Drop** | `fcn.004012fb`, `fcn.00401370` | High |
| **Execution** | `section..text` | High |
| **Anti-Analysis** | `fcn.00401bf8`, `fcn.00401435` | Medium/High |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1105 | Ingress Tool Transfer | The malware utilizes `WININET` and `URLMon` APIs (`InternetOpenW`, `URLDownloadToFileW`) to fetch remote content from a C2 server or hosting site. |
| T1497 | Virtualization, Sandbox, and Debugger Detection | The use of timing-based functions like `GetTickCount` and `QueryPerformanceCounter`, along with `RtlGetVersion`, indicates an attempt to detect analysis environments. |
| T1036 | Masquerading | The creation of files with randomized numeric names in the `%appdata%` directory is intended to hide the payload by making it appear as a common system or application file. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.* (The report mentions "remote servers" and "C2," but no specific IP addresses or domain names were included in the provided text.)

**File paths / Registry keys**
*   **%appdata%**: Used as the primary directory for dropping payloads.
*   **d3333333...txt**: A pattern of files with long numeric/obfuscated filenames located within user data folders.

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.* (Note: The value `0xbb40e64e` is a hardcoded comparison constant, not a file hash.)

**Other artifacts**
*   **Hardcoded Value:** `0xbb40e64e` (Used in anti-analysis/environment checking logic).
*   **C2 Methodology:** Dual-method download approach using both `WININET.dll` (`InternetOpenW`, `InternetOpenUrlW`) and `urlmon.dll` (`URLDownloadToFileW`).
*   **Anti-Analysis Technique:** Compilation of system metrics (GetSystemTimeAsFileTime, GetCurrentProcessId, GetTickCount, QueryPerformanceCounter) to generate an environment key for sandbox/VM detection.
*   **Persistence/Execution Strategy:** Use of both `CreateProcessW` and `ShellExecuteW` to launch payloads after successful download.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: downloader
3. **Confidence**: High

4. **Key evidence**:
*   **Primary Functionality:** The sample exhibits a classic "Downloader" workflow: it retrieves remote content using multiple APIs (`WININET` and `URLMon`), saves the payload to a local directory (`%appdata%`) with an obfuscated filename, and executes it via `CreateProcessW` or `ShellExecuteW`.
*   **Anti-Analysis Measures:** The inclusion of environment key generation (using `GetTickCount`, `QueryPerformanceCounter`, and `RtlGetVersion`) indicates a deliberate effort to detect virtual machines, sandboxes, or debuggers before executing the main payload.
*   **Evasion Tactics:** The use of dual-method download logic ensures that if one network path is blocked by security software, it can fall back to another, increasing the likelihood of successfully "calling home."
