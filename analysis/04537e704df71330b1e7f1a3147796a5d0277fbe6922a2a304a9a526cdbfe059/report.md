# Threat Analysis Report

**Generated:** 2026-07-10 00:26 UTC
**Sample:** `04537e704df71330b1e7f1a3147796a5d0277fbe6922a2a304a9a526cdbfe059_04537e704df71330b1e7f1a3147796a5d0277fbe6922a2a304a9a526cdbfe059.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04537e704df71330b1e7f1a3147796a5d0277fbe6922a2a304a9a526cdbfe059_04537e704df71330b1e7f1a3147796a5d0277fbe6922a2a304a9a526cdbfe059.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 54,784 bytes |
| MD5 | `e709114b3c9b593f245f9168c998752d` |
| SHA1 | `3d08793eaac7c0feeba676bb1bf24f10e0159667` |
| SHA256 | `04537e704df71330b1e7f1a3147796a5d0277fbe6922a2a304a9a526cdbfe059` |
| Overall entropy | 4.698 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767476648 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 6,656 | 6.036 | No |
| `.rdata` | 32,256 | 2.953 | No |
| `.data` | 8,704 | 4.811 | No |
| `.rsrc` | 1,024 | 5.194 | No |
| `.reloc` | 5,120 | 5.977 | No |

### Imports

**MSVCR90.dll**: `_except_handler4_common`, `_invoke_watson`, `_decode_pointer`, `_crt_debugger_hook`, `_onexit`, `_lock`, `__dllonexit`, `_unlock`, `?terminate@@YAXXZ`, `iswspace`, `__set_app_type`, `_encode_pointer`, `__p__fmode`, `__p__commode`, `_adjust_fdiv`
**WININET.dll**: `InternetOpenUrlW`, `InternetCloseHandle`, `InternetOpenW`
**SHLWAPI.dll**: `StrCmpNW`, `PathCombineW`, `PathFileExistsW`, `PathMatchSpecW`
**KERNEL32.dll**: `QueryPerformanceCounter`, `SetUnhandledExceptionFilter`, `GetStartupInfoW`, `InterlockedCompareExchange`, `InterlockedExchange`, `Sleep`, `CreateMutexA`, `GetLastError`, `ExitProcess`, `CreateThread`, `ExitThread`, `GetLogicalDrives`, `GetDriveTypeW`, `GetTickCount`, `lstrcpyW`
**USER32.dll**: `wsprintfW`, `CloseClipboard`, `OpenClipboard`, `CharLowerW`, `GetClipboardData`
**ADVAPI32.dll**: `RegQueryValueExW`, `RegCloseKey`, `RegOpenKeyExW`

## Extracted Strings

Total strings found: **150** (showing first 100)

```
!This program cannot be run in DOS mode.
$
Richw1
`.rdata
@.data
@.reloc
j
YQPSh
uhe'@
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
wcscat_s
wcsncat_s
wcschr
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
PathMatchSpecW
PathCombineW
StrCmpNW
SHLWAPI.dll
CloseHandle
CreateFileW
ExpandEnvironmentStringsW
GlobalUnlock
GlobalLock
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
CloseClipboard
GetClipboardData
OpenClipboard
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
0(050E0k0
3454n4
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401530` | `0x401530` | 1225 | ✓ |
| `fcn.00401a20` | `0x401a20` | 908 | ✓ |
| `entry0` | `0x4023e4` | 713 | ✓ |
| `fcn.00401300` | `0x401300` | 545 | ✓ |
| `fcn.004011b0` | `0x4011b0` | 202 | ✓ |
| `fcn.004025f0` | `0x4025f0` | 189 | ✓ |
| `fcn.00401eb0` | `0x401eb0` | 178 | ✓ |
| `fcn.00402444` | `0x402444` | 156 | ✓ |
| `fcn.00402768` | `0x402768` | 150 | ✓ |
| `section..text` | `0x401000` | 145 | ✓ |
| `fcn.00401120` | `0x401120` | 137 | ✓ |
| `fcn.004010a0` | `0x4010a0` | 126 | ✓ |
| `fcn.00401280` | `0x401280` | 124 | ✓ |
| `fcn.00401e30` | `0x401e30` | 124 | ✓ |
| `main` | `0x401fe0` | 105 | ✓ |
| `fcn.00401dd0` | `0x401dd0` | 96 | ✓ |
| `fcn.004026bc` | `0x4026bc` | 69 | ✓ |
| `fcn.004025a0` | `0x4025a0` | 68 | ✓ |
| `fcn.00402560` | `0x402560` | 53 | ✓ |
| `fcn.00402090` | `0x402090` | 43 | ✓ |
| `fcn.0040273a` | `0x40273a` | 43 | ✓ |
| `fcn.00402500` | `0x402500` | 38 | ✓ |
| `fcn.004024e9` | `0x4024e9` | 23 | ✓ |
| `fcn.00401a00` | `0x401a00` | 22 | ✓ |
| `fcn.00401db0` | `0x401db0` | 21 | ✓ |
| `fcn.00402701` | `0x402701` | 20 | ✓ |
| `fcn.004024e0` | `0x4024e0` | 9 | ✓ |
| `sub.MSVCR90.dll_iswspace` | `0x40205c` | 6 | ✓ |
| `sub.MSVCR90.dll_wcslen` | `0x402062` | 6 | ✓ |
| `sub.MSVCR90.dll_wcscmp` | `0x402068` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004010a0.c`](code/fcn.004010a0.c)
- [`code/fcn.00401120.c`](code/fcn.00401120.c)
- [`code/fcn.004011b0.c`](code/fcn.004011b0.c)
- [`code/fcn.00401280.c`](code/fcn.00401280.c)
- [`code/fcn.00401300.c`](code/fcn.00401300.c)
- [`code/fcn.00401530.c`](code/fcn.00401530.c)
- [`code/fcn.00401a00.c`](code/fcn.00401a00.c)
- [`code/fcn.00401a20.c`](code/fcn.00401a20.c)
- [`code/fcn.00401db0.c`](code/fcn.00401db0.c)
- [`code/fcn.00401dd0.c`](code/fcn.00401dd0.c)
- [`code/fcn.00401e30.c`](code/fcn.00401e30.c)
- [`code/fcn.00401eb0.c`](code/fcn.00401eb0.c)
- [`code/fcn.00402090.c`](code/fcn.00402090.c)
- [`code/fcn.00402444.c`](code/fcn.00402444.c)
- [`code/fcn.004024e0.c`](code/fcn.004024e0.c)
- [`code/fcn.004024e9.c`](code/fcn.004024e9.c)
- [`code/fcn.00402500.c`](code/fcn.00402500.c)
- [`code/fcn.00402560.c`](code/fcn.00402560.c)
- [`code/fcn.004025a0.c`](code/fcn.004025a0.c)
- [`code/fcn.004025f0.c`](code/fcn.004025f0.c)
- [`code/fcn.004026bc.c`](code/fcn.004026bc.c)
- [`code/fcn.00402701.c`](code/fcn.00402701.c)
- [`code/fcn.0040273a.c`](code/fcn.0040273a.c)
- [`code/fcn.00402768.c`](code/fcn.00402768.c)
- [`code/main.c`](code/main.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sub.MSVCR90.dll_iswspace.c`](code/sub.MSVCR90.dll_iswspace.c)
- [`code/sub.MSVCR90.dll_wcscmp.c`](code/sub.MSVCR90.dll_wcscmp.c)
- [`code/sub.MSVCR90.dll_wcslen.c`](code/sub.MSVCR90.dll_wcslen.c)

## Behavioral Analysis

Based on the analysis of the provided disassembly and decompiled C code, here is a summary of the malware's functionality:

### Core Functionality and Purpose
The binary is an **Information Stealer (Infostealer)**. Its primary purpose is to scan the local system for sensitive information—specifically targeting data that might be associated with cryptocurrency wallets, passwords, and configuration files—and exfiltrate that data to a remote server.

### Suspicious and Malicious Behaviors
*   **Clipboard Scraping:** The function `fcn.00401530` repeatedly accesses the system clipboard (`OpenClipboard`, `GetClipboardData`). It processes the content, removes whitespace, and checks it against internal lists to identify potentially valuable information (e.g., credentials or keys).
*   **Automated File System Crawling:** The function `fcn.00401a20` implements a "scavenger" routine. It recursively searches the file system for specific high-value extensions, including:
    *   **.mnemonic / .seed:** Highly indicative of cryptocurrency wallet recovery phrases.
    *   **.sql / .db:** Database files containing potential user data or credentials.
    *   **.json / .ini / .config:** Configuration files often containing API keys or passwords.
    *   **.msg / .eml:** Email files that may contain sensitive communications.
    *   **Other common formats:** `.txt`, `.doc`, `.rtf`, `.csv`, `.xls`, `.xlsx`, `.pdf`, `.log`.
*   **Data Exfiltration:** The function `fcn.004010a0` constructs a hardcoded URL (`http://178.16.54.109/tcoin.php?s=[DATA]`) and uses the WinINet library (`InternetOpenW`, `InternetOpenUrlW`) to send stolen data via an HTTP GET request to a remote server.
*   **Sensitive Data Mining:** The code specifically parses content from files it finds on disk (in `fcn.00401300`), looking for specific patterns before exfiltrating them, suggesting a targeted attempt to find and steal "high-value" secrets rather than just stealing raw files.

### Notable Techniques and Patterns
*   **Anti-Analysis/Evasion:**
    *   **Execution Delay:** The `main` function includes a `Sleep(2000)` call at the start, a common technique to evade basic sandbox analysis that only monitors the first few seconds of execution.
    *   **Mutex Check:** It uses a hardcoded mutex (`586484847`) to ensure only one instance of the malware is running at a time, which helps avoid detection from multiple concurrent processes or duplicate behavior in an environment.
*   **Network Hardcoding:** The use of a hardcoded IP address (`178.16.54.109`) instead of a domain name (FQDN) for C2 communication is a common trait in malware, as it bypasses the need for DNS resolution and can be harder to sinkhole via standard DNS blacklisting.
*   **System Interaction:** The inclusion of `fcn.00401eb0` checks registry keys related to "NoDrives" under Windows Explorer policies, which is often used by malware to determine if it is running in a restricted environment or to map accessible storage devices for scanning.
*   **Persistence/Staging:** The function `section..text` creates a file named `ururrur.txt` in the `%temp%` directory. This may be used as a temporary buffer for collected data before exfiltration or as a "heartbeat" file to check if the malware was successfully executed.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1056** | Collection | The malware accesses and processes system clipboard data (`OpenClipboard`, `GetClipboardData`) to identify credentials or keys. |
| **T1083** | File and Directory Discovery | The "scavenger" routine specifically crawls the file system looking for high-value extensions like `.mnemonic`, `.sql`, and `.config`. |
| **T1497** | Virtualization/Sandbox Evasion | The use of `Sleep(2000)` and checks on "NoDrives" registry keys are designed to detect and evade automated analysis environments. |
| **T1048** | Exfiltration Over Web Service | Stolen data is exfiltrated via HTTP GET requests (using the WinINet library) to a hardcoded remote IP address. |
| **T1567** | Exfiltration (Other) | While T1048 is more specific, the general movement of "high-value" secrets from internal files to an external server confirms exfiltration activity. |

### Analyst Notes:
*   **Data Mining:** The behavior described as "Sensitive Data Mining" (filtering content for specific patterns before sending) is technically a component of **T1056 (Collection)**, where the malware filters out noise to ensure only valuable data is sent to the C2 server.
*   **Network Hardcoding:** The use of a hardcoded IP address (`178.16.54.109`) supports **T1041 (Exfiltration Over C2 Channel)**; however, since it specifically utilizes HTTP and a .php script, **T1048** is the more precise sub-technique for this behavior.
*   **Mutex Check:** While "Mutex" usage isn't a standalone MITRE technique, it is a common standard practice in malware to ensure only one instance runs at a time, which helps prevent detection by alerting security systems to multiple concurrent processes.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   **URL:** `http://178.16.54.109/tcoin.php?s=[DATA]`
*   **IP Address:** `178.16.54.109` (C2 Infrastructure)

**File paths / Registry keys**
*   **File Path:** `%temp%\ururrur.txt` (Used as a staging file or heartbeat)
*   **Registry Key Context:** "NoDrives" (Checked via `fcn.00401eb0` to determine environment restrictions)

**Mutex names / Named pipes**
*   **Mutex Name:** `586484847`

**Hashes**
*   *None identified.*

**Other artifacts**
*   **C2 Pattern:** HTTP GET request to a hardcoded IP containing stolen data appended as a query string (`?s=[DATA]`).
*   **Targeted File Extensions (Data Mining):** `.mnemonic`, `.seed`, `.sql`, `.db`, `.json`, `.ini`, `.config`, `.msg`, `.eml`, `.txt`, `.doc`, `.rtf`, `.csv`, `.xls`, `.xlsx`, `.pdf`, `.log`.
*   **Persistence/Staging Behavior:** Creation of a temporary file in the `%temp%` directory.
*   **Evasion Technique:** Execution delay of 2 seconds (`Sleep(2000)`) to bypass basic sandbox analysis.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: infostealer
3. **Confidence**: High
4. **Key evidence**: 
    *   **Targeted Data Collection:** The malware actively crawls the file system for high-value targets, specifically cryptocurrency recovery phrases (`.mnemonic`, `.seed`) and configuration files containing credentials.
    *   **Data Exfiltration:** It utilizes a hardcoded IP address (`178.16.54.109`) to exfiltrate gathered data via HTTP GET requests to a PHP script.
    *   **Persistence & Evasion:** The use of an execution delay, mutex checks, and registry-based environment checks are classic indicators of malicious intent designed to bypass automated sandboxes and antivirus detection.
