# Threat Analysis Report

**Generated:** 2026-06-25 18:42 UTC
**Sample:** `0104e0b13130dfa08e3b021b85ed80399ce15afbcbcf00d672750b3fe5465795_0104e0b13130dfa08e3b021b85ed80399ce15afbcbcf00d672750b3fe5465795.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0104e0b13130dfa08e3b021b85ed80399ce15afbcbcf00d672750b3fe5465795_0104e0b13130dfa08e3b021b85ed80399ce15afbcbcf00d672750b3fe5465795.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 53,248 bytes |
| MD5 | `4737c6899345a8f5cd555c7366f88526` |
| SHA1 | `0bf08b7c682880563739f5cef31124fa6146250d` |
| SHA256 | `0104e0b13130dfa08e3b021b85ed80399ce15afbcbcf00d672750b3fe5465795` |
| Overall entropy | 4.612 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771272326 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 5,632 | 5.858 | No |
| `.rdata` | 31,744 | 2.957 | No |
| `.data` | 8,704 | 4.814 | No |
| `.rsrc` | 1,024 | 5.194 | No |
| `.reloc` | 5,120 | 5.944 | No |

### Imports

**MSVCR90.dll**: `_except_handler4_common`, `_invoke_watson`, `_decode_pointer`, `_crt_debugger_hook`, `_onexit`, `_lock`, `__dllonexit`, `_unlock`, `?terminate@@YAXXZ`, `iswspace`, `__set_app_type`, `_encode_pointer`, `__p__fmode`, `__p__commode`, `_adjust_fdiv`
**WININET.dll**: `InternetOpenUrlW`, `InternetCloseHandle`, `InternetOpenW`
**SHLWAPI.dll**: `StrCmpNW`, `PathMatchSpecW`, `PathFileExistsW`, `PathCombineW`
**KERNEL32.dll**: `QueryPerformanceCounter`, `SetUnhandledExceptionFilter`, `GetStartupInfoW`, `InterlockedCompareExchange`, `InterlockedExchange`, `Sleep`, `CreateMutexA`, `GetLastError`, `ExitProcess`, `CreateThread`, `ExitThread`, `GetLogicalDrives`, `GetDriveTypeW`, `GetTickCount`, `lstrcpyW`
**USER32.dll**: `wsprintfW`, `CharLowerW`
**ADVAPI32.dll**: `RegQueryValueExW`, `RegCloseKey`, `RegOpenKeyExW`

## Extracted Strings

Total strings found: **138** (showing first 100)

```
!This program cannot be run in DOS mode.
$
Richw1
`.rdata
@.data
@.reloc
j
YQPSh
uhE"@
tVVVVV
bad allocation
586484847
iswspace
wcslen
wcscmp
fclose
wcscat
wcstok
fgetws
_wfopen
memset
wcsstr
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
InternetOpenUrlW
InternetOpenW
WININET.dll
PathFileExistsW
PathCombineW
PathMatchSpecW
StrCmpNW
SHLWAPI.dll
CloseHandle
CreateFileW
ExpandEnvironmentStringsW
FindNextFileW
lstrcmpW
FindFirstFileW
lstrcpyW
QueryDosDeviceW
GetDriveTypeW
GetLogicalDrives
ExitThread
CreateThread
ExitProcess
GetLastError
CreateMutexA
InterlockedExchange
InterlockedCompareExchange
GetStartupInfoW
SetUnhandledExceptionFilter
QueryPerformanceCounter
GetTickCount
GetCurrentThreadId
GetCurrentProcessId
GetSystemTimeAsFileTime
TerminateProcess
GetCurrentProcess
UnhandledExceptionFilter
IsDebuggerPresent
KERNEL32.dll
wsprintfW
CharLowerW
USER32.dll
RegCloseKey
RegQueryValueExW
RegOpenKeyExW
ADVAPI32.dll
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
0)0=0J0p0
3454n4
4<5C5J5Q5X5_5
7"7/7<7I7V7c7p7}7
8'848=8J8S8`8|8
:9:C:`:
;";9;C;N;\;b;h;n;t;z;
<-<L<U<p<z<
=Z=d=j=s=
>
>S>Y>a>h>m>s>y>
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401530` | `0x401530` | 908 | ✓ |
| `entry0` | `0x401ed2` | 713 | ✓ |
| `fcn.00401300` | `0x401300` | 545 | ✓ |
| `fcn.004011b0` | `0x4011b0` | 202 | ✓ |
| `fcn.004020d0` | `0x4020d0` | 189 | ✓ |
| `fcn.004019c0` | `0x4019c0` | 178 | ✓ |
| `fcn.00401f32` | `0x401f32` | 156 | ✓ |
| `section..text` | `0x401000` | 150 | ✓ |
| `fcn.00402248` | `0x402248` | 150 | ✓ |
| `fcn.00401120` | `0x401120` | 137 | ✓ |
| `fcn.004010a0` | `0x4010a0` | 126 | ✓ |
| `fcn.00401280` | `0x401280` | 124 | ✓ |
| `fcn.00401940` | `0x401940` | 124 | ✓ |
| `main` | `0x401af0` | 106 | ✓ |
| `fcn.004018e0` | `0x4018e0` | 96 | ✓ |
| `fcn.0040219c` | `0x40219c` | 69 | ✓ |
| `fcn.00402080` | `0x402080` | 68 | ✓ |
| `fcn.00402040` | `0x402040` | 53 | ✓ |
| `fcn.00401b90` | `0x401b90` | 43 | ✓ |
| `fcn.0040221a` | `0x40221a` | 43 | ✓ |
| `fcn.00401fee` | `0x401fee` | 38 | ✓ |
| `fcn.00401fd7` | `0x401fd7` | 23 | ✓ |
| `fcn.004018c0` | `0x4018c0` | 21 | ✓ |
| `fcn.004021e1` | `0x4021e1` | 20 | ✓ |
| `fcn.00401fce` | `0x401fce` | 9 | ✓ |
| `sub.MSVCR90.dll_iswspace` | `0x401b5a` | 6 | ✓ |
| `sub.MSVCR90.dll_wcslen` | `0x401b60` | 6 | ✓ |
| `sub.MSVCR90.dll_wcscmp` | `0x401b66` | 6 | ✓ |
| `sub.MSVCR90.dll__wfopen` | `0x401b84` | 6 | ✓ |
| `sub.MSVCR90.dll_fgetws` | `0x401b7e` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004010a0.c`](code/fcn.004010a0.c)
- [`code/fcn.00401120.c`](code/fcn.00401120.c)
- [`code/fcn.004011b0.c`](code/fcn.004011b0.c)
- [`code/fcn.00401280.c`](code/fcn.00401280.c)
- [`code/fcn.00401300.c`](code/fcn.00401300.c)
- [`code/fcn.00401530.c`](code/fcn.00401530.c)
- [`code/fcn.004018c0.c`](code/fcn.004018c0.c)
- [`code/fcn.004018e0.c`](code/fcn.004018e0.c)
- [`code/fcn.00401940.c`](code/fcn.00401940.c)
- [`code/fcn.004019c0.c`](code/fcn.004019c0.c)
- [`code/fcn.00401b90.c`](code/fcn.00401b90.c)
- [`code/fcn.00401f32.c`](code/fcn.00401f32.c)
- [`code/fcn.00401fce.c`](code/fcn.00401fce.c)
- [`code/fcn.00401fd7.c`](code/fcn.00401fd7.c)
- [`code/fcn.00401fee.c`](code/fcn.00401fee.c)
- [`code/fcn.00402040.c`](code/fcn.00402040.c)
- [`code/fcn.00402080.c`](code/fcn.00402080.c)
- [`code/fcn.004020d0.c`](code/fcn.004020d0.c)
- [`code/fcn.0040219c.c`](code/fcn.0040219c.c)
- [`code/fcn.004021e1.c`](code/fcn.004021e1.c)
- [`code/fcn.0040221a.c`](code/fcn.0040221a.c)
- [`code/fcn.00402248.c`](code/fcn.00402248.c)
- [`code/main.c`](code/main.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sub.MSVCR90.dll__wfopen.c`](code/sub.MSVCR90.dll__wfopen.c)
- [`code/sub.MSVCR90.dll_fgetws.c`](code/sub.MSVCR90.dll_fgetws.c)
- [`code/sub.MSVCR90.dll_iswspace.c`](code/sub.MSVCR90.dll_iswspace.c)
- [`code/sub.MSVCR90.dll_wcscmp.c`](code/sub.MSVCR90.dll_wcscmp.c)
- [`code/sub.MSVCR90.dll_wcslen.c`](code/sub.MSVCR90.dll_wcslen.c)

## Behavioral Analysis

This is a classic example of an **Information Stealer (Infostealer)**. The binary is designed to scan the local file system for sensitive information—specifically credentials, configuration files, and cryptocurrency-related data—and exfiltrate that data to a remote server.

### Core Functionality
The primary purpose of this code is to perform **automated reconnaissance and data theft**. It crawls through directories looking for specific file extensions associated with high-value information (passwords, emails, wallet seeds). Once it finds matching files, it parses the content for relevant strings and sends them to a hardcoded Command & Control (C2) IP address.

### Malicious Behaviors
*   **Information Stealing (Targeted Data Mining):** 
    The function `fcn.00401530` implements a heavy-duty filter for sensitive data. It specifically looks for the following file types:
    *   **Credentials/Config:** `.txt`, `.doc`, `.sql`, `.ini`, `.rtf`, `.json`, `.log`.
    *   **Databases/Spreadsheets:** `.csv`, `.xls`, `.xlsx`.
    *   **Email Data:** `.eml`, `.msg`, `.mbox`.
    *   **Cryptocurrency Wallets:** The inclusion of **`.mnemonic`** and **`.seed`** extensions is a high-confidence indicator of intent to steal cryptocurrency assets.

*   **Data Exfiltration:** 
    The function `fcn.004010a0` handles the communication with the attacker's infrastructure:
    *   It uses the **WININET library** to perform network requests.
    *   It constructs a URL pointing to a specific IP address and a PHP script: `http://178.16.54.109/tcoin.php?s=[stolen_data]`. 
    *   The use of the "tcoin" naming convention strongly suggests an intent to steal cryptocurrency-related information.

*   **Persistence & Execution Logic:**
    *   **Delayed Execution:** The `main` function starts with a `Sleep(2000)` (2 seconds). This is a common tactic used by malware to bypass automated sandbox analysis, where the "malicious" behavior occurs after the initial startup period.
    *   **Multi-Instance Prevention:** It uses `CreateMutexA("586484847")`. While standard in legitimate software, it is also used here to ensure only one instance of the infection runs at a time on the host.

### Notable Techniques & Patterns
*   **Anti-Analysis/Evasion:**
    *   The function `fcn.00402248` implements **timing-based anti-debugging**. It uses `GetSystemTimeAsFileTime`, `GetTickCount`, and `QueryPerformanceCounter`. By comparing these values, the malware can detect if it is being "stepped through" in a debugger or running in an emulated environment.
    *   **Environment Checking:** The code includes calls to `GetLogicalDrives` and checks registry keys regarding "NoDrives," which are used to map out the system's environment and potentially detect security restrictions.

*   **Search Logic:** 
    The malware iterates through files using `FindFirstFileW`. It identifies valid target files by checking against a long list of hardcoded extensions. If a file matches, it is processed; if not (e.g., it’s a directory or an unrelated file), it is skipped.

*   **Hardcoded Infrastructure:** 
    The IP address `178.16.54.109` and the specific query string structure are hard-coded, which is typical for "plug-and-play" malware samples distributed via various infection vectors (like phishing or malicious downloads).

### Summary for Incident Response
*   **Threat Type:** Information Stealer / Spyware.
*   **Primary Indicators:** IP `178.16.54.109`, use of `WININET` for exfiltration, and specific targeting of `.mnemonic` and `.seed` files.
*   **Risk Level:** **High.** The malware targets personal information and financial assets (cryptocurrency).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Evasion | The use of `Sleep(2000)` and timing-based checks (`GetTickCount`, `QueryPerformanceCounter`) is designed to bypass automated analysis environments. |
| **T1083** | File and Directory Discovery | The malware utilizes `FindFirstFileW` to crawl the file system for specific extensions associated with sensitive information. |
| **T1510** | Data from Local System | Specifically targeting `.mnemonic`, `.seed`, and configuration files identifies a clear intent to harvest credentials and assets from the local host. |
| **T1041** | Exfiltration Over C2 Channel | The use of `WININET` to transmit collected data to a hardcoded IP address via a PHP script confirms exfiltration via a Command & Control channel. |

---

## Indicators of Compromise

Based on the analysis provided, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   **IP:** `178.16.54.109`
*   **URL:** `http://178.16.54.109/tcoin.php?s=[stolen_data]`

**File paths / Registry keys**
*   *(None identified; the malware uses dynamic system crawling rather than hardcoded local paths.)*

**Mutex names / Named pipes**
*   **Mutex:** `586484847`

**Hashes**
*   *(None identified in the provided strings.)*

**Other artifacts**
*   **Targeted File Extensions (High-Value):** `.mnemonic`, `.seed`
*   **C2 Script Name:** `tcoin.php`
*   **Anti-Analysis Technique:** Timing-based debugger detection using `GetTickCount`, `QueryPerformanceCounter`, and `GetSystemTimeAsFileTime`.
*   **Evasion Tactic:** Initial execution delay of 2000ms (`Sleep(2000)`) to bypass automated sandbox analysis.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Infostealer
3. **Confidence**: High
4. **Key evidence**:
    *   **Targeted Data Mining:** The malware specifically searches for high-value file extensions, most notably `.mnemonic` and `.seed`, which are definitive indicators of intent to steal cryptocurrency assets.
    *   **Hardcoded Exfiltration:** It utilizes the `WININET` library to exfiltrate stolen data to a hardcoded IP address (`178.16.54.109`) via a specific script (`tcoin.php`).
    *   **Evasion Techniques:** The inclusion of both a sleep timer and complex timing-based anti-debugging checks (using `GetTickCount` and `QueryPerformanceCounter`) demonstrates a deliberate effort to bypass automated sandbox analysis and manual inspection.
