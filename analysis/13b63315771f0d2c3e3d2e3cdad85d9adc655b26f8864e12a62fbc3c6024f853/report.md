# Threat Analysis Report

**Generated:** 2026-09-02 22:02 UTC
**Sample:** `13b63315771f0d2c3e3d2e3cdad85d9adc655b26f8864e12a62fbc3c6024f853_13b63315771f0d2c3e3d2e3cdad85d9adc655b26f8864e12a62fbc3c6024f853.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13b63315771f0d2c3e3d2e3cdad85d9adc655b26f8864e12a62fbc3c6024f853_13b63315771f0d2c3e3d2e3cdad85d9adc655b26f8864e12a62fbc3c6024f853.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 11,264 bytes |
| MD5 | `0c7fc9536762e91f9cb3a571f3551f21` |
| SHA1 | `18652abbff22abbeaf68becb27967482b83a91ec` |
| SHA256 | `13b63315771f0d2c3e3d2e3cdad85d9adc655b26f8864e12a62fbc3c6024f853` |
| Overall entropy | 5.09 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1781267567 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 4,096 | 5.662 | No |
| `.rdata` | 3,584 | 4.235 | No |
| `.data` | 512 | 0.353 | No |
| `.rsrc` | 1,024 | 5.194 | No |
| `.reloc` | 1,024 | 3.682 | No |

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
t`h$#@
thH#@
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
5,5@5R5X5^5d5
6(6C6M6`6j6o6t6
6-777=7F7z7
7&8,848;8@8F8L8T8Z8a8h8x8
9.9C9N9f9|9
;p;v;};
;1<T<a<m<u<}<
="=)=0=7=>=E=L=S=[=c=k=w=
1 1$1\5`5
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x4018a5` | 713 | ✓ |
| `fcn.004010a8` | `0x4010a8` | 595 | ✓ |
| `fcn.00401ab0` | `0x401ab0` | 189 | ✓ |
| `section..text` | `0x401000` | 168 | ✓ |
| `main` | `0x4014b3` | 156 | ✓ |
| `fcn.00401906` | `0x401906` | 156 | ✓ |
| `fcn.00401c28` | `0x401c28` | 150 | ✓ |
| `fcn.00401435` | `0x401435` | 126 | ✓ |
| `fcn.004012fb` | `0x4012fb` | 117 | ✓ |
| `fcn.00401370` | `0x401370` | 117 | ✓ |
| `fcn.004013e5` | `0x4013e5` | 80 | ✓ |
| `fcn.00401b7c` | `0x401b7c` | 69 | ✓ |
| `fcn.00401a60` | `0x401a60` | 68 | ✓ |
| `fcn.00401a20` | `0x401a20` | 53 | ✓ |
| `fcn.00401570` | `0x401570` | 43 | ✓ |
| `fcn.00401bfa` | `0x401bfa` | 43 | ✓ |
| `fcn.004019c2` | `0x4019c2` | 38 | ✓ |
| `fcn.004019ab` | `0x4019ab` | 23 | ✓ |
| `fcn.00401bc1` | `0x401bc1` | 20 | ✓ |
| `fcn.004019a2` | `0x4019a2` | 9 | ✓ |
| `sub.MSVCR90.dll_memset` | `0x401550` | 6 | ✓ |
| `sub.MSVCR90.dll_srand` | `0x401562` | 6 | ✓ |
| `sub.MSVCR90.dll_rand` | `0x40155c` | 6 | ✓ |
| `sub.MSVCR90.dll__snwprintf` | `0x401556` | 6 | ✓ |
| `sub.urlmon.dll_URLDownloadToFileW` | `0x401e04` | 6 | ✓ |
| `sub.MSVCR90.dll__amsg_exit` | `0x401900` | 6 | ✓ |
| `sub.MSVCR90.dll__initterm_e` | `0x401b74` | 6 | ✓ |
| `sub.MSVCR90.dll__initterm` | `0x401b6e` | 6 | ✓ |
| `sub.MSVCR90.dll__XcptFilter` | `0x401a0e` | 6 | ✓ |
| `sub.MSVCR90.dll__controlfp_s` | `0x401cf2` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004010a8.c`](code/fcn.004010a8.c)
- [`code/fcn.004012fb.c`](code/fcn.004012fb.c)
- [`code/fcn.00401370.c`](code/fcn.00401370.c)
- [`code/fcn.004013e5.c`](code/fcn.004013e5.c)
- [`code/fcn.00401435.c`](code/fcn.00401435.c)
- [`code/fcn.00401570.c`](code/fcn.00401570.c)
- [`code/fcn.00401906.c`](code/fcn.00401906.c)
- [`code/fcn.004019a2.c`](code/fcn.004019a2.c)
- [`code/fcn.004019ab.c`](code/fcn.004019ab.c)
- [`code/fcn.004019c2.c`](code/fcn.004019c2.c)
- [`code/fcn.00401a20.c`](code/fcn.00401a20.c)
- [`code/fcn.00401a60.c`](code/fcn.00401a60.c)
- [`code/fcn.00401ab0.c`](code/fcn.00401ab0.c)
- [`code/fcn.00401b7c.c`](code/fcn.00401b7c.c)
- [`code/fcn.00401bc1.c`](code/fcn.00401bc1.c)
- [`code/fcn.00401bfa.c`](code/fcn.00401bfa.c)
- [`code/fcn.00401c28.c`](code/fcn.00401c28.c)
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

### **Core Functionality**
The binary functions as a **multi-stage downloader and dropper**. Its primary purpose is to reach out to remote servers (likely via HTTP/HTTPS) to download malicious payloads or components and then execute them on the local system. It uses multiple methods for downloading to ensure reliability and attempts to hide its tracks by using randomized file names and temporary files.

### **Suspicious & Malicious Behaviors**

*   **Multi-Method Downloader:**
    *   The function `fcn.004010a8` implements two distinct ways to retrieve remote content: one via the **WinINET** API (`InternetOpenW`, `InternetOpenUrlW`, `InternetReadFile`) and a fallback/alternative using the **URLMon** library (`URLDownloadToFileW`).
    *   The use of both methods is a common technique in malware to ensure that if one method is blocked or fails, the other can still successfully download the payload.

*   **Staging and File Manipulation:**
    *   The binary checks for (and creates) files with "randomized" names in the `%appdata%` directory (e.g., `d333333333333333333.txt`, `3969592695.txt`). 
    *   It uses these files as staging areas. After a file is downloaded, the code often deletes the temporary local copy or prepares it for execution.

*   **Execution of Payloads:**
    *   The function `section..text` implements the final execution stage. It takes a path (likely the path to one of the downloaded items) and executes it using either `CreateProcessW` or `ShellExecuteW`. This is the point where the secondary, more specialized malicious code (e.g., ransomware, spyware, or a remote access trojan) is launched.

*   **Anti-Analysis & Evasion:**
    *   **Time Delays:** The binary frequently calls `Sleep()` (e.g., 2000ms at start and multiple times during the download loop). This is used to stall automated sandbox analysis tools that only monitor a process for a few seconds.
    *   **Environment Checks:** It uses `RtlGetVersion` (via `ntdll`) and checks for specific hardware/OS characteristics to determine if it is running in a supported or "target" environment, potentially avoiding execution on known security researcher machines.
    *   **Entropy/Randomization:** The heavy use of `srand()` and `rand()` suggests an attempt to make the behavior non-deterministic, making it harder for automated systems to create consistent signatures.

### **Notable Techniques & Patterns**

*   **Dynamic API Resolution:** Use of `GetProcAddress` and `GetModuleHandleW` (seen in the inclusion list) indicates the binary may resolve certain functions at runtime to hide its true capabilities from basic static analysis.
*   **Fallback Logic:** The structure of `fcn.004010a8` contains an `if (!bVar1)` block, which effectively acts as a fallback mechanism for downloading if the primary network method fails.
*   **Persistence/Stealth via AppData:** By using `%appdata%`, the malware targets a directory that usually has write permissions for standard users and is frequently ignored by casual users, making it an ideal place to hide dropped components.

### **Summary of Risk**
This is a highly suspicious binary characteristic of a **Downloader/Dropper**. It contains significant indicators of malicious intent:
1.  **Network activity** to fetch remote files.
2.  **Payload execution** via `ShellExecuteW`.
3.  **Evasion techniques** (Sleep, environment checking).
4.  **Obfuscated file paths** in user-writable directories.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1105 | Ingress Tool Transfer | The binary employs multiple methods (WinINET and URLMon) to download remote payloads, ensuring successful acquisition despite potential network blocks. |
| T1497 | Virtualized/Sandbox Evasion | The use of `RtlGetVersion` and specific hardware checks indicates an attempt to detect and bypass analysis environments. |
| T1036 | Masquerading | The utilization of randomized filenames and the `%appdata%` directory is designed to hide dropped components among legitimate system files. |
| T1415 | System Interference | The implementation of `Sleep()` calls serves as a "time-out" tactic to stall automated sandbox analysis tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.* (The report notes that remote servers are used, but no specific hardcoded IPs or domains were present in the provided text.)

**File paths / Registry keys**
*   `%appdata%` (Targeted directory for staging dropped payloads)
*   `d333333333333333333.txt` (Example of randomized filename used for staging)
*   `3969592695.txt` (Example of randomized filename used for staging)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **C2/Download Methodology:** Dual-method download approach using both **WinINET** (`InternetOpenW`, `InternetOpenUrlW`, `InternetReadFile`) and **URLMon** (`URLDownloadToFileW`).
*   **Evasion Techniques:** 
    *   Use of `Sleep()` (e.g., 2000ms) to bypass automated sandbox analysis.
    *   Environment checks via `RtlGetVersion` to detect non-target systems or analysis environments.
*   **Execution Method:** Use of `ShellExecuteW` and `CreateProcessW` for launching secondary payloads.
*   **Persistence/Stealth:** Intentional use of randomized filenames and common user directories (`%appdata%`) to mask malicious files.

---

## Malware Family Classification

1. **Malware family:** Unknown
2. **Malware type:** Downloader / Loader
3. **Confidence:** High

**Key evidence:**
*   **Multi-Stage Delivery:** The binary employs a dual-method download approach (WinINET and URLMon) to retrieve remote payloads, which is a classic signature of a downloader designed to ensure successful payload acquisition despite network restrictions.
*   **Anti-Analysis Techniques:** The presence of `Sleep()` calls and environment checks via `RtlGetVersion` specifically indicates an intent to bypass automated sandbox analysis and detect security researchers' environments.
*   **Staging & Execution:** The use of randomized filenames within the `%appdata%` directory for staging, followed by execution via `ShellExecuteW`, confirms its primary role as a vehicle for delivering subsequent, more specialized malicious payloads (such as RATs or ransomware).
