# Threat Analysis Report

**Generated:** 2026-06-28 05:28 UTC
**Sample:** `025f57988953e3d23e1657a9af5610887e57c5390a82f73b4b2b99c30eef3b70_025f57988953e3d23e1657a9af5610887e57c5390a82f73b4b2b99c30eef3b70.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `025f57988953e3d23e1657a9af5610887e57c5390a82f73b4b2b99c30eef3b70_025f57988953e3d23e1657a9af5610887e57c5390a82f73b4b2b99c30eef3b70.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 10,240 bytes |
| MD5 | `1f675e91f2099fc2a582e7ae2539f326` |
| SHA1 | `5bda9b339036f712f48a69fc867c299c22bad885` |
| SHA256 | `025f57988953e3d23e1657a9af5610887e57c5390a82f73b4b2b99c30eef3b70` |
| Overall entropy | 5.36 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779455171 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 3,584 | 6.082 | No |
| `.rdata` | 3,072 | 4.544 | No |
| `.data` | 512 | 0.353 | No |
| `.rsrc` | 1,024 | 5.194 | No |
| `.reloc` | 1,024 | 3.598 | No |

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
t`h #@
thD#@
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
5"5(5.545l5v5}5
606:6?6D6Z6_6h6m6z6
7J7R7[7a7i7u7
8$8*81888H8P8V8b8m8
969L9Y9
:@;F;M;j;
<$<1<=<E<M<Y<}<
=#=+=3=;=G=P=U=[=e=n=y=
1 1$1t4x4
55(5D5H5
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

### Analysis Summary
The provided code belongs to a **downloader/dropper** malware sample. Its primary purpose is to verify that the environment is not being analyzed, download a payload from a remote server using multiple methods, and execute that payload on the local machine.

### Core Functionality
*   **Multi-Method Downloader:** The binary implements two different ways to fetch files from the internet: a manual loop using `WinINet` functions (`InternetOpenW`, `InternetReadFile`) for fine-grained control, and a fallback method using the Windows `urlmon` library (`URLDownloadToFileW`).
*   **Staged Execution:** The program performs several checks on the local filesystem (e.g., looking for specific files in `%appdata%` and checking for "Program Files (x86)") before proceeding to the next stages of infection.
*   **Payload Execution:** Once a file is successfully downloaded, the code utilizes `CreateProcessW` or `ShellExecuteW` to execute the downloaded content.

### Suspicious & Malicious Behaviors
*   **Network Communication:** 
    *   The sample reaches out to external URLs (the specific URLs are likely obfuscated in the data section not shown here) to retrieve remote payloads.
*   **Anti-Analysis/Evasion:**
    *   **Environment Validation:** The function `fcn.00401bf8` is a classic anti-analysis routine. It collects various system parameters (`GetTickCount`, `GetSystemTimeAsFileTime`, `GetCurrentProcessId`, `QueryPerformanceCounter`) and performs arithmetic operations to see if they match a specific hardcoded constant (`0xbb40e64e`). This is intended to detect if the binary is running in a debugger, sandbox, or virtual machine.
*   **File Manipulation:**
    *   The code creates temporary files (with random-looking names like `d333333333333333333.txt`) during the download process and calls `DeleteFileW` to remove traces of these local artifacts after the payload is staged or executed.
*   **Process Execution:**
    *   The use of `ShellExecuteW` as a fallback for `CreateProcessW` is a common technique to ensure that the malicious payload is launched regardless of specific execution environment restrictions.

### Notable Techniques & Patterns
*   **Redundancy in Networking:** By implementing both manual `WinINet` logic and the higher-level `urlmon` API, the malware increases its chances of successfully downloading the payload even if one method is blocked by security software.
*   **Environment Context Checking:** The code checks for specific directory paths (e.g., `Program Files (x86)`) to verify it is running on a standard Windows installation rather than an analysis environment.
*   **Decryption/De-obfuscation Logic:** The functions involving `_decode_pointer` and `_encode_pointer` suggest that the binary may have its internal data or API pointers obfuscated to hinder static analysis.
*   **Self-Cleaning:** The explicit use of `DeleteFileW` on temporary files is a common indicator of a "dropper" designed to minimize the forensic footprint left on the local disk.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1105** | Ingress Tool Transfer | The malware employs multiple methods (`WinINet` and `urlmon`) to retrieve remote payloads, ensuring redundancy in its delivery mechanism. |
| **T1497** | Virtualization/Sandbox Evasion | The use of system parameters like `GetTickCount` and `QueryPerformanceCounter` is a classic technique used to detect if the malware is running in an analysis environment. |
| **T1027** | Obfuscated Files or Information | The inclusion of `_decode_pointer` logic for internal data and the deletion of temporary files are used to hinder static analysis and minimize the forensic footprint. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified (Note: The analysis indicates that URLs are present but are obfuscated in the data section and not visible in the provided strings).

**File paths / Registry keys**
*   None (The mentioned file `d333333333333333333.txt` is identified as a dynamically named temporary file and does not constitute a fixed path).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified (Note: The value `0xbb40e64e` is an internal memory constant used for anti-analysis, not a file hash).

**Other artifacts**
*   **Anti-Analysis Constant:** `0xbb40e64e` (Used in function `fcn.00401bf8` to determine if the environment is being monitored/debugged).
*   **Dropper Pattern:** Use of repeated digit naming convention for temporary files (e.g., `d333333333333333333.txt`).
*   **Dual-Path Networking Logic:** The malware utilizes a fallback mechanism where it alternates between `WinINet` functions (`InternetOpenW`, `InternetReadFile`) and the `urlmon` library (`URLDownloadToFileW`).

---

## Malware Family Classification

Based on the analysis provided, here is the classification for this sample:

1. **Malware family:** Unknown
2. **Malware type:** Downloader / Dropper
3. **Confidence:** High (for Type) / Low (for Family)
4. **Key evidence:**
    *   **Multi-Stage Payload Delivery:** The sample utilizes redundant networking methods (`WinINet` and `urlmon`) to ensure the successful acquisition of a remote payload, which is characteristic of a robust dropper.
    *   **Evasion & Anti-Analysis:** The presence of specific environmental checks (e.g., `GetTickCount`, `QueryPerformanceCounter`), anti-debugging logic (`0xbb40e64e` constant), and obfuscated internal pointers indicates an intent to bypass security software and automated sandboxes.
    *   **Artifact Concealment:** The use of "self-cleaning" tactics (deleting temporary files like `d333...txt`) and the deployment of fallback execution methods (`ShellExecuteW`) are classic indicators of a downloader designed to minimize the forensic footprint of the primary infection stage.
