# Threat Analysis Report

**Generated:** 2026-06-27 21:14 UTC
**Sample:** `01f64c61767bc41f039cf2080e61da49c96b14e4d558da6c03128e40ca816799_01f64c61767bc41f039cf2080e61da49c96b14e4d558da6c03128e40ca816799.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01f64c61767bc41f039cf2080e61da49c96b14e4d558da6c03128e40ca816799_01f64c61767bc41f039cf2080e61da49c96b14e4d558da6c03128e40ca816799.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 12,288 bytes |
| MD5 | `07bd5d0edaca14204802b8ff7db346ce` |
| SHA1 | `660784d4aa65c5914978fae86d4f493e26a9b2b1` |
| SHA256 | `01f64c61767bc41f039cf2080e61da49c96b14e4d558da6c03128e40ca816799` |
| Overall entropy | 5.256 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773085969 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 4,608 | 5.649 | No |
| `.rdata` | 4,096 | 4.402 | No |
| `.data` | 512 | 1.035 | No |
| `.rsrc` | 1,024 | 5.188 | No |
| `.reloc` | 1,024 | 4.25 | No |

### Imports

**MSVCR90.dll**: `_controlfp_s`, `_invoke_watson`, `memset`, `_except_handler4_common`, `_decode_pointer`, `_onexit`, `_lock`, `__dllonexit`, `_unlock`, `?terminate@@YAXXZ`, `__set_app_type`, `_encode_pointer`, `__p__fmode`, `__p__commode`, `_adjust_fdiv`
**WININET.dll**: `InternetCloseHandle`, `DeleteUrlCacheEntryW`, `InternetOpenW`, `InternetOpenUrlW`, `InternetReadFile`
**SHLWAPI.dll**: `PathFindFileNameW`, `PathFileExistsW`
**urlmon.dll**: `URLDownloadToFileW`
**KERNEL32.dll**: `InterlockedCompareExchange`, `InterlockedExchange`, `CreateMutexA`, `ExitProcess`, `GetLastError`, `GetModuleFileNameW`, `CopyFileW`, `GetTickCount`, `ExpandEnvironmentStringsW`, `DeleteFileW`, `GetStartupInfoA`, `WriteFile`, `CloseHandle`, `SetFileAttributesW`, `CreateProcessW`
**USER32.dll**: `wsprintfW`
**ADVAPI32.dll**: `RegSetValueExW`, `RegCloseKey`, `RegOpenKeyExW`
**SHELL32.dll**: `ShellExecuteW`

## Extracted Strings

Total strings found: **102** (showing first 100)

```
!This program cannot be run in DOS mode.
$
RichtU
`.rdata
@.data
@.reloc
jXhX7@
j
XPVj
tVVVVV
memset
wcslen
wcscmp
MSVCR90.dll
_amsg_exit
__getmainargs
_cexit
_XcptFilter
_ismbblead
_acmdln
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
DeleteUrlCacheEntryW
WININET.dll
PathFileExistsW
PathFindFileNameW
SHLWAPI.dll
URLDownloadToFileW
urlmon.dll
CreateProcessW
SetFileAttributesW
CloseHandle
WriteFile
CreateFileW
DeleteFileW
ExpandEnvironmentStringsW
GetTickCount
CopyFileW
GetModuleFileNameW
GetLastError
ExitProcess
CreateMutexA
InterlockedExchange
InterlockedCompareExchange
GetStartupInfoA
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
RegCloseKey
RegSetValueExW
RegOpenKeyExW
ADVAPI32.dll
ShellExecuteW
SHELL32.dll
578685884
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
Y0i0|0
1&13191e1
2 202?2j2w2
3,3<3K3
4D4J4V4c4s4|4
5"5J5P5U5a5n5
56,6;6F6K6W6d6}6
7"717>7N7[7n7s7{7
8)8@8\8f8
9 9]9g9m9w9
:g:m:u:|:
:3;9;B;I;T;Z;n;
<<,<1<P<
=-=A=G=
='>,>q>
?(?.?4?D?J?P?V?\?b?i?p?w?~?
01080@0F0
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `main` | `0x4013d0` | 951 | ✓ |
| `entry0` | `0x401ae6` | 714 | ✓ |
| `fcn.004010b0` | `0x4010b0` | 690 | ✓ |
| `fcn.00401cf0` | `0x401cf0` | 189 | ✓ |
| `section..text` | `0x401000` | 172 | ✓ |
| `fcn.00401b46` | `0x401b46` | 156 | ✓ |
| `fcn.00401e68` | `0x401e68` | 150 | ✓ |
| `fcn.00401370` | `0x401370` | 87 | ✓ |
| `fcn.00401dbc` | `0x401dbc` | 69 | ✓ |
| `fcn.00401ca0` | `0x401ca0` | 68 | ✓ |
| `fcn.00401c60` | `0x401c60` | 53 | ✓ |
| `fcn.004017b0` | `0x4017b0` | 43 | ✓ |
| `fcn.00401e3a` | `0x401e3a` | 43 | ✓ |
| `fcn.00401c02` | `0x401c02` | 38 | ✓ |
| `fcn.00401beb` | `0x401beb` | 23 | ✓ |
| `fcn.00401e01` | `0x401e01` | 20 | ✓ |
| `fcn.00401be2` | `0x401be2` | 9 | ✓ |
| `sub.MSVCR90.dll_wcscmp` | `0x4017a0` | 6 | ✓ |
| `sub.MSVCR90.dll_wcslen` | `0x40179a` | 6 | ✓ |
| `sub.MSVCR90.dll_memset` | `0x401788` | 6 | ✓ |
| `sub.MSVCR90.dll_srand` | `0x401794` | 6 | ✓ |
| `sub.MSVCR90.dll_rand` | `0x40178e` | 6 | ✓ |
| `sub.urlmon.dll_URLDownloadToFileW` | `0x402044` | 6 | ✓ |
| `sub.MSVCR90.dll__amsg_exit` | `0x401b40` | 6 | ✓ |
| `sub.MSVCR90.dll__initterm_e` | `0x401db4` | 6 | ✓ |
| `sub.MSVCR90.dll__initterm` | `0x401dae` | 6 | ✓ |
| `sub.MSVCR90.dll__XcptFilter` | `0x401c4e` | 6 | ✓ |
| `sub.MSVCR90.dll__controlfp_s` | `0x401f32` | 6 | ✓ |
| `sub.MSVCR90.dll__invoke_watson` | `0x401f2c` | 6 | ✓ |
| `sub.MSVCR90.dll__terminate__YAXXZ` | `0x401efe` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004010b0.c`](code/fcn.004010b0.c)
- [`code/fcn.00401370.c`](code/fcn.00401370.c)
- [`code/fcn.004017b0.c`](code/fcn.004017b0.c)
- [`code/fcn.00401b46.c`](code/fcn.00401b46.c)
- [`code/fcn.00401be2.c`](code/fcn.00401be2.c)
- [`code/fcn.00401beb.c`](code/fcn.00401beb.c)
- [`code/fcn.00401c02.c`](code/fcn.00401c02.c)
- [`code/fcn.00401c60.c`](code/fcn.00401c60.c)
- [`code/fcn.00401ca0.c`](code/fcn.00401ca0.c)
- [`code/fcn.00401cf0.c`](code/fcn.00401cf0.c)
- [`code/fcn.00401dbc.c`](code/fcn.00401dbc.c)
- [`code/fcn.00401e01.c`](code/fcn.00401e01.c)
- [`code/fcn.00401e3a.c`](code/fcn.00401e3a.c)
- [`code/fcn.00401e68.c`](code/fcn.00401e68.c)
- [`code/main.c`](code/main.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sub.MSVCR90.dll__XcptFilter.c`](code/sub.MSVCR90.dll__XcptFilter.c)
- [`code/sub.MSVCR90.dll__amsg_exit.c`](code/sub.MSVCR90.dll__amsg_exit.c)
- [`code/sub.MSVCR90.dll__controlfp_s.c`](code/sub.MSVCR90.dll__controlfp_s.c)
- [`code/sub.MSVCR90.dll__initterm.c`](code/sub.MSVCR90.dll__initterm.c)
- [`code/sub.MSVCR90.dll__initterm_e.c`](code/sub.MSVCR90.dll__initterm_e.c)
- [`code/sub.MSVCR90.dll__invoke_watson.c`](code/sub.MSVCR90.dll__invoke_watson.c)
- [`code/sub.MSVCR90.dll__terminate__YAXXZ.c`](code/sub.MSVCR90.dll__terminate__YAXXZ.c)
- [`code/sub.MSVCR90.dll_memset.c`](code/sub.MSVCR90.dll_memset.c)
- [`code/sub.MSVCR90.dll_rand.c`](code/sub.MSVCR90.dll_rand.c)
- [`code/sub.MSVCR90.dll_srand.c`](code/sub.MSVCR90.dll_srand.c)
- [`code/sub.MSVCR90.dll_wcscmp.c`](code/sub.MSVCR90.dll_wcscmp.c)
- [`code/sub.MSVCR90.dll_wcslen.c`](code/sub.MSVCR90.dll_wcslen.c)
- [`code/sub.urlmon.dll_URLDownloadToFileW.c`](code/sub.urlmon.dll_URLDownloadToFileW.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is an analysis of the binary's behavior.

### Core Functionality and Purpose
The binary functions as a **downloader and dropper**. Its primary purpose is to reach out to a remote server, download a payload (likely a secondary stage of malware), save it to the local disk, and execute it. The use of generic names like "sysfrodolv.exe" suggests an attempt to masquerade as a legitimate system process.

### Suspicious or Malicious Behaviors
The following behaviors are highly indicative of malicious intent:

*   **Remote Payload Retrieval (Downloader):**
    *   The function `fcn.004010b0` is designed specifically for network communication. It utilizes multiple methods to fetch data: the standard WinInet API suite (`InternetOpenW`, `InternetOpenUrlW`, `InternetReadFile`) and the helper function `URLDownloadToFileW`.
    *   It systematically handles the download, writing the received buffer into a file on disk.

*   **Anti-Analysis & Evasion:**
    *   **Timing/Environment Checks:** Function `fcn.00401e68` performs calculations using `GetTickCount`, `QueryPerformanceCounter`, and `GetSystemTimeAsFileTime`. This is a common technique to detect if the code is running in a debugger or a virtualized environment by checking for timing inconsistencies.
    *   **Stalling/Sleep:** The code calls `Sleep()` multiple times during execution (e.g., before the main logic and after certain operations). This is often used to "outwait" automated sandbox analysis tools that only monitor a sample for a few minutes.
    *   **Mutex Creation:** It uses `CreateMutexA` at the start of `main`. While common in legitimate software, it is frequently used by malware to ensure only one instance of the malicious process is running on the system at a time.

*   **Persistence and System Manipulation:**
    *   **Registry Modification:** The code interacts with `ADVAPI32.dll` functions like `RegOpenKeyExW` and `RegSetValueExW`. It targets registry keys (specifically mentioning "Windows Config") to ensure the payload persists after a system reboot or to modify system settings.
    *   **File Masquerading:** The use of strings like `sysfrodolv.exe` suggests an attempt to hide in plain sight by mimicking a system-level utility.

*   **Execution of Dropped Payload:**
    *   The binary uses `CreateProcessW` and `ShellExecuteW` to launch the file it successfully downloads or moves. This is the final stage of the "dropper" cycle, transitioning from the downloader to the active payload.

### Notable Techniques & Patterns
*   **Dual Download Path:** The code provides two different methods for downloading files (WinInet and URL_Download_to_File). This "fallback" mechanism ensures that even if one network method is blocked by a security product or firewall, the other may succeed.
*   **File Manipulation:** The routine includes calls to `SetFileAttributesW`, which can be used to set file attributes such as "Hidden" or "System," making it harder for a casual user to notice the dropped executable.
*   **Environment Awareness:** The check in `fcn.00401370` specifically looks for "Program Files (x86)". This suggests the malware is designed to identify and potentially move its components into high-privilege directories.

### Summary Table of Indicators
| Feature | Observation | Impact |
| :--- | :--- | :--- |
| **Network Activity** | `InternetOpenW`, `URLDownloadToFileW` | Capability to fetch remote payloads. |
| **Evasion** | `QueryPerformanceCounter`, `GetTickCount` | Detection of debuggers/sandboxes. |
| **Persistence** | `RegSetValueExW` | Ensuring the infection survives a reboot. |
| **Payload Execution**| `ShellExecuteW`, `CreateProcessW` | Activating the final malware stage. |
| **Masquerading** | "sysfrodolv.exe" | Blending in with system processes. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1105 | Ingress Tool Transfer Protocol | The binary uses `InternetOpenW` and `URLDownloadToFileW` to retrieve a remote payload from a web server via standard protocols. |
| T1497 | Virtualization/Sandbox Detection | The use of `GetTickCount` and `QueryPerformanceCounter` is intended to detect timing inconsistencies typical of virtualized environments or debuggers. |
| T1112 | Modify Registry | The code utilizes `RegSetValueExW` to modify registry keys, a common method for achieving persistence or altering system configurations. |
| T1036 | Masquerading | The use of a deceptive filename (`sysfrodolv.exe`) and `SetFileAttributesW` (to set "Hidden" or "System") are used to hide the malicious presence from users and automated tools. |
| T1204 | User Execution | The use of `CreateProcessW` and `ShellExecuteW` is the mechanism by which the dropped payload is executed on the local system. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
* *None identified.* (The text describes the capability to reach out to remote servers but does not provide specific hardcoded URLs or IP addresses.)

**File paths / Registry keys**
* **sysfrodolv.exe** (Suspicious filename used for masquerading as a system process)

**Mutex names / Named pipes**
* *None identified.* (While the behavior notes the use of `CreateMutexA`, no specific mutex string was provided.)

**Hashes**
* *None identified.*

**Other artifacts**
* **C2/Download Patterns:** Dual-method download logic (utilizing both WinInet API suite and `URLDownloadToFileW` as a fallback mechanism).
* **Anti-Analysis Techniques:** Timing-based evasion checks using: 
    * `GetTickCount`
    * `QueryPerformanceCounter`
    * `GetSystemTimeAsFileTime`
* **Persistence/Manipulation Behaviors:** 
    * Use of `SetFileAttributesW` to hide dropped files.
    * Modification of "Windows Config" registry keys for persistence.
    * Target identification of "Program Files (x86)" directory.

---

## Malware Family Classification

1. **Malware family**: Unknown (or "custom")
2. **Malware type**: Dropper / Loader
3. **Confidence**: High (regarding behavior); Medium (regarding specific naming, as no unique identifiers for a known campaign were provided).

4. **Key evidence**:
*   **Multi-stage Execution:** The binary exhibits classic dropper/loader behavior by retrieving an external payload via dual download methods (`InternetOpenW` and `URLDownloadToFileW`) and executing it using `CreateProcessW` and `ShellExecuteW`.
*   **Robust Evasion Tactics:** The use of `GetTickCount`, `QueryPerformanceCounter`, and multiple `Sleep()` calls indicates a high level of intentional evasion to bypass automated sandboxes and timing-based analysis.
*   **Persistence & Stealth Manipulation:** The sample actively attempts to maintain presence via Registry modifications (`RegSetValueExW`), hides its activities using Masquerading (mimicking "sysfrodolv.exe"), and manipulates file attributes to hide the dropped payload from the user.
