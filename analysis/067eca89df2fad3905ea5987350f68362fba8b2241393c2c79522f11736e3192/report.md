# Threat Analysis Report

**Generated:** 2026-07-15 04:47 UTC
**Sample:** `067eca89df2fad3905ea5987350f68362fba8b2241393c2c79522f11736e3192_067eca89df2fad3905ea5987350f68362fba8b2241393c2c79522f11736e3192.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `067eca89df2fad3905ea5987350f68362fba8b2241393c2c79522f11736e3192_067eca89df2fad3905ea5987350f68362fba8b2241393c2c79522f11736e3192.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 10,240 bytes |
| MD5 | `8e678b61fb0dab4f332e26cd18b4aee3` |
| SHA1 | `197c4251c2347785ee3ae1afe6cbe6cfbeb38ac7` |
| SHA256 | `067eca89df2fad3905ea5987350f68362fba8b2241393c2c79522f11736e3192` |
| Overall entropy | 5.407 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1775159597 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 3,584 | 6.113 | No |
| `.rdata` | 3,072 | 4.602 | No |
| `.data` | 512 | 0.353 | No |
| `.rsrc` | 1,024 | 5.194 | No |
| `.reloc` | 1,024 | 3.632 | No |

### Imports

**MSVCR90.dll**: `__dllonexit`, `_lock`, `_onexit`, `_unlock`, `_except_handler4_common`, `_invoke_watson`, `_controlfp_s`, `_crt_debugger_hook`, `?terminate@@YAXXZ`, `__set_app_type`, `_encode_pointer`, `__p__fmode`, `__p__commode`, `_adjust_fdiv`, `__setusermatherr`
**WININET.dll**: `InternetOpenW`, `InternetReadFile`, `InternetCloseHandle`, `InternetOpenUrlW`
**SHLWAPI.dll**: `PathCombineW`, `PathFileExistsW`
**urlmon.dll**: `URLDownloadToFileW`
**KERNEL32.dll**: `QueryPerformanceCounter`, `InterlockedExchange`, `GetModuleHandleW`, `GetProcAddress`, `GetTickCount`, `ExpandEnvironmentStringsW`, `CreateFileW`, `WriteFile`, `DeleteFileW`, `CreateProcessW`, `Sleep`, `CloseHandle`, `GetCurrentThreadId`, `GetCurrentProcessId`, `GetSystemTimeAsFileTime`
**USER32.dll**: `wsprintfW`
**SHELL32.dll**: `ShellExecuteW`

## Extracted Strings

Total strings found: **97** (showing first 100)

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
t`h#@
thP$@
j\h8%@
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
5%515B5H5N5T5
636=6P6Z6_6d6z6
7'7-767j7r7{7
8$8+80868<8D8J8Q8X8h8p8v8
939>9V9l9y9
:`;f;m;
;!<D<Q<]<e<m<y<
= ='=.=5=<=C=K=S=[=g=p=u={=
5L5P5X5\5x5
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x401895` | 713 | ✓ |
| `fcn.004010a8` | `0x4010a8` | 595 | ✓ |
| `fcn.00401aa0` | `0x401aa0` | 189 | ✓ |
| `section..text` | `0x401000` | 168 | ✓ |
| `fcn.004018f6` | `0x4018f6` | 156 | ✓ |
| `fcn.00401c18` | `0x401c18` | 150 | ✓ |
| `main` | `0x4014b3` | 141 | ✓ |
| `fcn.00401435` | `0x401435` | 126 | ✓ |
| `fcn.004012fb` | `0x4012fb` | 117 | ✓ |
| `fcn.00401370` | `0x401370` | 117 | ✓ |
| `fcn.004013e5` | `0x4013e5` | 80 | ✓ |
| `fcn.00401b6c` | `0x401b6c` | 69 | ✓ |
| `fcn.00401a50` | `0x401a50` | 68 | ✓ |
| `fcn.00401a10` | `0x401a10` | 53 | ✓ |
| `fcn.00401560` | `0x401560` | 43 | ✓ |
| `fcn.00401bea` | `0x401bea` | 43 | ✓ |
| `fcn.004019b2` | `0x4019b2` | 38 | ✓ |
| `fcn.0040199b` | `0x40199b` | 23 | ✓ |
| `fcn.00401bb1` | `0x401bb1` | 20 | ✓ |
| `fcn.00401992` | `0x401992` | 9 | ✓ |
| `sub.MSVCR90.dll_memset` | `0x401540` | 6 | ✓ |
| `sub.MSVCR90.dll_srand` | `0x401552` | 6 | ✓ |
| `sub.MSVCR90.dll_rand` | `0x40154c` | 6 | ✓ |
| `sub.MSVCR90.dll__snwprintf` | `0x401546` | 6 | ✓ |
| `sub.urlmon.dll_URLDownloadToFileW` | `0x401df4` | 6 | ✓ |
| `sub.MSVCR90.dll__amsg_exit` | `0x4018f0` | 6 | ✓ |
| `sub.MSVCR90.dll__initterm_e` | `0x401b64` | 6 | ✓ |
| `sub.MSVCR90.dll__initterm` | `0x401b5e` | 6 | ✓ |
| `sub.MSVCR90.dll__XcptFilter` | `0x4019fe` | 6 | ✓ |
| `sub.MSVCR90.dll__controlfp_s` | `0x401ce2` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004010a8.c`](code/fcn.004010a8.c)
- [`code/fcn.004012fb.c`](code/fcn.004012fb.c)
- [`code/fcn.00401370.c`](code/fcn.00401370.c)
- [`code/fcn.004013e5.c`](code/fcn.004013e5.c)
- [`code/fcn.00401435.c`](code/fcn.00401435.c)
- [`code/fcn.00401560.c`](code/fcn.00401560.c)
- [`code/fcn.004018f6.c`](code/fcn.004018f6.c)
- [`code/fcn.00401992.c`](code/fcn.00401992.c)
- [`code/fcn.0040199b.c`](code/fcn.0040199b.c)
- [`code/fcn.004019b2.c`](code/fcn.004019b2.c)
- [`code/fcn.00401a10.c`](code/fcn.00401a10.c)
- [`code/fcn.00401a50.c`](code/fcn.00401a50.c)
- [`code/fcn.00401aa0.c`](code/fcn.00401aa0.c)
- [`code/fcn.00401b6c.c`](code/fcn.00401b6c.c)
- [`code/fcn.00401bb1.c`](code/fcn.00401bb1.c)
- [`code/fcn.00401bea.c`](code/fcn.00401bea.c)
- [`code/fcn.00401c18.c`](code/fcn.00401c18.c)
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

### Malware Analysis Report

#### **Core Functionality and Purpose**
The binary functions as a **Downloader/Dropper**. Its primary purpose is to verify that it is running on a "valid" target (not in a sandbox or debugger), download a remote payload from the internet, and execute subsequent components or staged files.

#### **Suspicious and Malicious Behaved Observed**
The code exhibits several behaviors characteristic of malware:

*   **Multi-Stage Downloader:** 
    *   The function `fcn.004010a8` contains logic to connect to a remote URL (`InternetOpenW`, `InternetOpenUrlW`). 
    *   It downloads content and writes it to a local file via `WriteFile`.
    *   **Fallback Mechanism:** If the primary download method fails (the `!bVar1` branch), it uses the `urlmon.dll` library (`URLDownloadToFileW`) as a fallback, which is common in malware to bypass simple network monitoring or ensure the payload is successfully retrieved.

*   **Anti-Analysis & Anti-Debugging:**
    *   **Timing/Environmental Checks:** Function `fcn.00401c18` aggregates several system values (System Time, Process ID, Thread ID, Tick Count, and Performance Counter) and compares them against a hardcoded constant (`0xbb40e64e`). This is used to detect if the execution environment is being tampered with or monitored.
    *   **OS Version Verification:** Function `fcn.00401435` specifically calls `RtlGetVersion` and checks specific byte values (likely checking for a modern Windows version like Windows 10). This ensures it doesn't run on outdated systems or certain specialized VM environments.

*   **File Manipulation & Staging:**
    *   The binary checks for the existence of specific, seemingly random filenames in the `%appdata%` directory (e.g., `7d7d6d66d.txt` and `s77s7s7s7s7.txt`). 
    *   If these files do not exist, it creates them. These act as "markers" or configuration flags to determine the state of the infection on a specific machine.
    *   The downloader deletes local files immediately after an action (seen in `fcn.004010a8`), which is often used to remove evidence of the downloaded payload before it is executed/loaded into memory.

*   **Execution of External Payloads:**
    *   The function `section..text` handles the execution of components. It uses `CreateProcessW` or `ShellExecuteW` to launch additional programs based on provided arguments or paths. This indicates that this binary might be the first stage (a "loader") that pulls in more sophisticated malware modules.

#### **Notable Techniques and Patterns**
*   **API Obfuscation/Dynamic Loading:** The use of `GetProcAddress` and `GetModuleHandleW` suggest some level of dynamic capability, though much is wrapped in standard libraries.
*   **WinINet & URLMon usage:** Standard Windows APIs used by malware to facilitate easy internet communication without requiring a full browser engine.
*   **Self-Defense/Evasion:** The frequent use of `Sleep()` between critical network or file operations (e.g., in `fcn.004010a8` and during execution calls) is intended to evade automated sandboxes that analyze behavior over short windows of time.

### Summary Table
| Feature | Detection/Observation | Purpose |
| :--- | :--- | :--- |
| **Downloader** | `InternetOpenW`, `URLDownloadToFileW` | Fetching remote malicious payloads. |
| **Anti-Analysis** | `RtlGetVersion`, `QueryPerformanceCounter` | Evading sandboxes and debuggers. |
| **File Operations** | `CreateFileW`, `DeleteFileW` | Staging files in `%appdata%` and cleaning up traces. |
| **Execution** | `ShellExecuteW`, `CreateProcessW` | Launching the final payload or secondary stages. |

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis, here is the mapping of the observed actions to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1105** | Ingress Tool Transfer | The malware uses `InternetOpenW` and `URLDownloadToFileW` to fetch a remote payload and store it locally. |
| **T1497** | Virtualization/Sandbox Detection | The use of `RtlGetVersion` for OS checks and time-based queries (like `QueryPerformanceCounter`) are classic indicators of anti-analysis logic. |
| **T1070.004** | Indicator Removal on Host: File Deletion | The malware deletes local files immediately after use to remove traces of the payload or intermediate files from the system. |
| **T1204** | User Execution | The use of `ShellExecuteW` and `CreateProcessW` indicates a transition from a loader stage to executing the primary malicious payload. |
| **T1106** | Native API | The malware utilizes standard Windows APIs (WinINet, URLMon) to perform its core functions like network communication and file handling. |
| **T1059** | Command and Scripting Interpreter | Use of `ShellExecuteW` often implies the execution of commands or scripts to launch further components or stages. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified. While the behavior describes "Remote URL" functionality, no specific domains or IP addresses were present in the provided text.)*

**File paths / Registry keys**
*   `%appdata%\7d7d6d66d.txt` (Used as a configuration/marker file)
*   `%appdata%\s77s7s7s7s7.txt` (Used as a configuration/marker file)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(No cryptographic file hashes were present in the provided strings.)*

**Other artifacts**
*   **Anti-Analysis Constant:** `0xbb40e64e` (Used in comparison against system values like Tick Count and Performance Counters to detect sandbox/debugger environments).
*   **Specific Filenames:** `7d7d6d66d.txt` and `s77s7s7s7s7.txt` (Non-standard naming conventions used for local staging).
*   **Suspicious API Usage Pattern:** Fallback mechanism utilizing `URLDownloadToFileW` via `urlmon.dll` as a secondary method for payload retrieval.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Downloader / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-Stage Payload Retrieval:** The binary utilizes `InternetOpenW` and a fallback mechanism via `URLDownloadToFileW` to fetch remote components, a classic behavior of a first-stage downloader designed to bring more complex malware into the environment.
*   **Anti-Analysis/Evasion Techniques:** The inclusion of `RtlGetVersion` for OS checking and custom calculations using `QueryPerformanceCounter` against a hardcoded constant indicates deliberate attempts to bypass sandbox analysis and debugger detection.
*   **Staging and Self-Deletion:** The creation of "marker" files in the `%appdata%` directory followed by the immediate deletion of local files after execution demonstrates an intent to minimize its forensic footprint while preparing the environment for subsequent stages.
