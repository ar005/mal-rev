# Threat Analysis Report

**Generated:** 2026-06-27 14:10 UTC
**Sample:** `01d43a963b470c78d91382de1f0b6d76c278f9e70a4e0057b636217fd7f3de87_01d43a963b470c78d91382de1f0b6d76c278f9e70a4e0057b636217fd7f3de87.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01d43a963b470c78d91382de1f0b6d76c278f9e70a4e0057b636217fd7f3de87_01d43a963b470c78d91382de1f0b6d76c278f9e70a4e0057b636217fd7f3de87.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 4 sections |
| Size | 14,782,000 bytes |
| MD5 | `cd5dbbc7e14897ccd1fad1b4d21a0b9f` |
| SHA1 | `59d1cd7f5c0db4e198925d9f892f9d09ce6bf6b8` |
| SHA256 | `01d43a963b470c78d91382de1f0b6d76c278f9e70a4e0057b636217fd7f3de87` |
| Overall entropy | 7.999 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1185071589 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 74,752 | 6.469 | No |
| `.rdata` | 13,824 | 4.511 | No |
| `.data` | 4,608 | 4.8 | No |
| `.rsrc` | 3,072 | 4.883 | No |

### Imports

**KERNEL32.dll**: `Sleep`, `MultiByteToWideChar`, `WideCharToMultiByte`, `CompareFileTime`, `FindClose`, `FindFirstFileW`, `GetFileAttributesW`, `GetLastError`, `CreateDirectoryW`, `ExpandEnvironmentStringsW`, `lstrlenA`, `WriteFile`, `GetStdHandle`, `lstrcmpW`, `GetSystemTimeAsFileTime`
**USER32.dll**: `CharUpperW`, `GetWindowLongW`, `wsprintfW`, `wsprintfA`, `MessageBoxA`, `GetKeyState`, `SendMessageW`, `wvsprintfW`, `KillTimer`, `GetSystemMenu`, `EnableMenuItem`, `SetTimer`, `GetWindowTextW`, `DefWindowProcW`, `CallWindowProcW`
**GDI32.dll**: `DeleteObject`, `SelectObject`, `GetDeviceCaps`, `GetObjectW`, `CreateFontIndirectW`
**SHELL32.dll**: `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `SHGetMalloc`, `ShellExecuteW`, `ShellExecuteExW`, `SHGetSpecialFolderPathW`, `SHGetFileInfoW`
**ole32.dll**: `CoCreateInstance`, `CoInitialize`
**OLEAUT32.dll**: `SysAllocString`, `VariantClear`
**MSVCRT.dll**: `__set_app_type`, `__p__fmode`, `__p__commode`, `_adjust_fdiv`, `__setusermatherr`, `_initterm`, `__getmainargs`, `_acmdln`, `exit`, `_XcptFilter`, `_exit`, `??1type_info@@UAE@XZ`, `_onexit`, `__dllonexit`, `_except_handler3`

## Extracted Strings

Total strings found: **31925** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@BBf92u
WSSSSP
SVWujz
9w@@f
Yu(j
S
tHHt)S
twHtPHt H
9^0tXj
SSjjh
F(@Pj
jh
EHHtW
@PQSjh
G490tsB
EhPSA
8_>u8_=u
u/!F0!F4
tsNthNt,Nt
uN8XDtI
08X?t+
u#9ut
C 90tA
E9ur
tNHt)H
x0C;^D|
_^][YY
EhPSA
9^|~!;~pt
YG;~||
9CttsG
~;}u
_WhXEA
8WhxEA
F$;F,r
\$f9\$
v#SVW3
+|$O9D$r
9D$s4
UWh(EA
j
XPVSS
							
SetFileAttributesW
SystemTimeToFileTime
GetLocalTime
GetExitCodeThread
WaitForSingleObject
CreateThread
MultiByteToWideChar
WideCharToMultiByte
CompareFileTime
FindClose
FindFirstFileW
GetFileAttributesW
GetLastError
CreateDirectoryW
ExpandEnvironmentStringsW
lstrlenA
WriteFile
GetStdHandle
lstrcmpW
GetSystemTimeAsFileTime
lstrlenW
RemoveDirectoryW
FindNextFileW
DeleteFileW
VirtualAlloc
VirtualFree
GetACP
GetOEMCP
GetUserDefaultUILanguage
GetUserDefaultLCID
GetTempPathW
SetEnvironmentVariableW
SetCurrentDirectoryW
CloseHandle
lstrcmpiW
GetModuleFileNameW
GetCommandLineW
GetVersionExW
CreateFileW
GetDriveTypeW
GetModuleHandleW
GetProcAddress
LoadLibraryA
MulDiv
GetSystemDirectoryW
TerminateThread
ResumeThread
SuspendThread
LocalFree
lstrcpyW
FormatMessageW
DeleteCriticalSection
GetFileSize
SetFilePointer
ReadFile
SetFileTime
SetEndOfFile
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040315e` | `0x40315e` | 9672 | ✓ |
| `main` | `0x40397a` | 6292 | ✓ |
| `fcn.0040be81` | `0x40be81` | 3936 | ✓ |
| `fcn.00407852` | `0x407852` | 2306 | ✓ |
| `fcn.0040b9b3` | `0x40b9b3` | 1230 | ✓ |
| `fcn.0041004e` | `0x41004e` | 1036 | ✓ |
| `fcn.00402451` | `0x402451` | 979 | ✓ |
| `fcn.0040b353` | `0x40b353` | 829 | ✓ |
| `fcn.0040cf9a` | `0x40cf9a` | 779 | ✓ |
| `fcn.0040abe8` | `0x40abe8` | 707 | ✓ |
| `fcn.00401c91` | `0x401c91` | 689 | ✓ |
| `fcn.004113a0` | `0x4113a0` | 685 | ✓ |
| `fcn.00406097` | `0x406097` | 672 | ✓ |
| `fcn.0040b07f` | `0x40b07f` | 628 | ✓ |
| `fcn.00407430` | `0x407430` | 591 | ✓ |
| `fcn.00405506` | `0x405506` | 517 | ✓ |
| `fcn.00405d28` | `0x405d28` | 477 | ✓ |
| `fcn.0040dc90` | `0x40dc90` | 476 | ✓ |
| `fcn.0040a890` | `0x40a890` | 455 | ✓ |
| `fcn.004020f1` | `0x4020f1` | 356 | ✓ |
| `fcn.0041060d` | `0x41060d` | 346 | ✓ |
| `entry0` | `0x411de6` | 338 | ✓ |
| `fcn.004118e7` | `0x4118e7` | 336 | ✓ |
| `fcn.00403698` | `0x403698` | 332 | ✓ |
| `fcn.00401a5e` | `0x401a5e` | 327 | ✓ |
| `fcn.0040b86c` | `0x40b86c` | 327 | ✓ |
| `fcn.0040317e` | `0x40317e` | 326 | ✓ |
| `fcn.0040d953` | `0x40d953` | 312 | ✓ |
| `fcn.00407249` | `0x407249` | 306 | ✓ |
| `fcn.0040330c` | `0x40330c` | 296 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401a5e.c`](code/fcn.00401a5e.c)
- [`code/fcn.00401c91.c`](code/fcn.00401c91.c)
- [`code/fcn.004020f1.c`](code/fcn.004020f1.c)
- [`code/fcn.00402451.c`](code/fcn.00402451.c)
- [`code/fcn.0040315e.c`](code/fcn.0040315e.c)
- [`code/fcn.0040317e.c`](code/fcn.0040317e.c)
- [`code/fcn.0040330c.c`](code/fcn.0040330c.c)
- [`code/fcn.00403698.c`](code/fcn.00403698.c)
- [`code/fcn.00405506.c`](code/fcn.00405506.c)
- [`code/fcn.00405d28.c`](code/fcn.00405d28.c)
- [`code/fcn.00406097.c`](code/fcn.00406097.c)
- [`code/fcn.00407249.c`](code/fcn.00407249.c)
- [`code/fcn.00407430.c`](code/fcn.00407430.c)
- [`code/fcn.00407852.c`](code/fcn.00407852.c)
- [`code/fcn.0040a890.c`](code/fcn.0040a890.c)
- [`code/fcn.0040abe8.c`](code/fcn.0040abe8.c)
- [`code/fcn.0040b07f.c`](code/fcn.0040b07f.c)
- [`code/fcn.0040b353.c`](code/fcn.0040b353.c)
- [`code/fcn.0040b86c.c`](code/fcn.0040b86c.c)
- [`code/fcn.0040b9b3.c`](code/fcn.0040b9b3.c)
- [`code/fcn.0040be81.c`](code/fcn.0040be81.c)
- [`code/fcn.0040cf9a.c`](code/fcn.0040cf9a.c)
- [`code/fcn.0040d953.c`](code/fcn.0040d953.c)
- [`code/fcn.0040dc90.c`](code/fcn.0040dc90.c)
- [`code/fcn.0041004e.c`](code/fcn.0041004e.c)
- [`code/fcn.0041060d.c`](code/fcn.0041060d.c)
- [`code/fcn.004113a0.c`](code/fcn.004113a0.c)
- [`code/fcn.004118e7.c`](code/fcn.004118e7.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, your analysis is updated to reflect more specific behaviors regarding how the binary handles file system interaction, path resolution, and staged execution.

### Updated Analysis: **Installer Wrapper / Dropper**

The analysis of the second set of functions reinforces the initial assessment that this binary serves as a sophisticated wrapper. However, it also provides concrete evidence of "Dropper" behavior—specifically the ability to extract components from internal resources and execute them in temporary locations.

---

### 1. Refined Core Functionality
*   **Robust Path Resolution & Normalization:** Functions such as `fcn.00402451` demonstrate significant effort in resolving system paths (e.g., via `SHGetSpecialFolderPathW`) and "cleaning" those paths (removing trailing characters/dots). This ensures the installer can find valid locations on various Windows configurations to place its payloads.
*   **Resource Extraction Logic:** The complexity of `fcn.0041060d` suggests a sophisticated parsing engine for embedded data. While common in installers like 7-Zip or Inno Setup, this level of complexity is also used by malware to unpack multiple "modules" or "stages" from a single encrypted resource block within the primary executable.
*   **Dynamic UI Adaptation:** Functions like `fcn.00406097` and `fcn.00407430` show that the binary performs extensive calculations on window sizes, system metrics, and control positions. This indicates a highly polished "front-end" designed to look like professional software.

### 2. New & Enhanced Suspicious Behaviors
The addition of these functions reveals several high-priority indicators common in dropper/loader malware:

*   **Dropping and Executing (The "Drop" Pattern):** `fcn.0040330c` and `fcn.00405506` exhibit a classic dropper sequence:
    1.  Retrieve a temporary directory (`GetTempPathW`).
    2.  Construct/prepare a path for a file.
    3.  Create the file on disk (`CreateFileW`).
    4.  Write data to that file (likely extracted from memory or an internal resource).
    5.  Immediately execute the dropped file using `ShellExecuteW`.
*   **Environment Discovery:** The use of `SHGetSpecialFolderPathW` allows the binary to identify "safe" locations for payload placement, such as the Desktop or common application folders, which are often less scrutinized than deep system directories but still convenient for initial infection.
*   **Error Handling for Extraction/Execution:** Functions like `fcn.00407249` show that the binary handles various failures (e.g., file access errors during writing) and can present formatted error messages to the user or log them internally.

### 3. Advanced Techniques & Patterns
*   **Layered Execution Architecture:** The code doesn't just launch one thing; it manages a multi-step process. It validates the environment, extracts components (possibly using its own internal decompression/decryption logic), writes them to temporary paths, and then hands off execution to those "staged" files.
*   **Standard Library Mimicry:** The binary uses standard Windows API calls (`GetSystemMetrics`, `GetDlgItem`) for its GUI elements. This is a common tactic to blend in with legitimate software by utilizing the same system libraries as popular installers (like InstallShield).
*   **Hardcoded Strings & Constants:** Several functions reference internal constants and lengths that suggest the binary is processing "blocks" of data or records, typical of an installer dealing with multiple files within one bundle.

---

### Updated Summary for Incident Response

This binary remains a high-priority candidate for a **Dropper/Downloader**. The additional code confirms it possesses the capabilities to extract, write, and execute secondary components on the local filesystem.

**Key Indicators of Concern:**
*   **Staged Execution Sequence:** Monitor for a process that calls `GetTempPathW` followed by `CreateFile`/`WriteFile` and then immediately spawns a child process via `ShellExecute`.
*   **In-Memory Extraction:** The complexity of the logic in `0041060d` suggests it may be extracting its "true" payload from an internal, potentially obfuscated resource.
*   **Environment Manipulation:** It actively seeks out user folders (Documents, Desktop) to drop files for execution.

**Detection & Mitigation Strategy:**
*   **Behavioral Rule:** Alert on any process that writes a file to `%TEMP%` or `%APPDATA%` and immediately executes that file using `ShellExecuteW`.
*   **Integrity Check:** Because this is an "installer," it may attempt to bypass security by mimicking standard installation behavior. Focus monitoring on the **files it creates**, rather than just the installer itself.
*   **Persistence Awareness:** If a second-stage payload is launched, it may attempt to establish persistence (Registry keys, Scheduled Tasks) that is distinct from this wrapper’s actions.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1574** | Archive Extraction Capability | The binary utilizes a complex parsing engine to extract multiple components/stages from internal resource blocks within the primary executable. |
| **T1036** | Masquerading | The use of standard Windows APIs and dynamic UI adaptation are intended to mimic legitimate installer software (e.g., InstallShield) to blend in with normal system activity. |
| **T1083** | File and Directory Discovery | The binary utilizes `SHGetSpecialFolderPathW` to identify and resolve "safe" system locations (like the Desktop or AppData) for dropping its payloads. |
| **T1630** | User Execution | The use of `ShellExecuteW` to launch a file immediately after it is written to a temporary directory indicates an execution stage typical of a dropper wrapper. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: As per your instructions, standard Windows API calls (e.g., `GetLocalTime`), system libraries (`KERNEL32.dll`), and common compiler mangled names (e.g., `??2@YAPAXI@Z`) have been excluded as they do not constitute unique indicators of a specific threat actor or campaign.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **%TEMP% Directory:** Targeted via `GetTempPathW` for staged execution.
*   **User Folders (Desktop/Documents):** Targeted via `SHGetSpecialFolderPathW` for payload placement.
*(Note: No specific hardcoded absolute paths were identified in the string dump.)*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (Behavioral Indicators & TTPs)**
*   **Dropper Pattern:** The binary exhibits a high-confidence "Drop and Execute" behavior. Specifically:
    1.  `GetTempPathW`: Identifying the temporary directory.
    2.  `CreateFileW` / `WriteFile`: Writing a payload to disk from internal resources.
    3.  `ShellExecuteW`: Immediately executing the newly created file.
*   **Resource Extraction:** Use of complex parsing logic (identified in the analysis as `fcn.0041060d`) suggests the binary extracts multiple stages or modules from encrypted/embedded internal resource blocks.
*   **Persistence Preparation:** The use of `SHGetSpecialFolderPathW` indicates an intent to place payloads in common user-accessible paths to evade detection while remaining accessible to the user's session.
*   **"Installer" Masking:** The binary deliberately utilizes standard Windows UI and system metrics libraries (`USER32.dll`, `GDI32.dll`) to mimic the behavior of legitimate software installers (e.g., InstallShield).

---
**Analyst Note:** While no static network IOCs (IPs/URLs) were found in this specific sample, the behavioral analysis confirms the binary is a **highly capable Dropper**. Monitoring should focus on the execution chain: any process writing to `%TEMP%` or `%APPDATA%` followed immediately by a `ShellExecute` call should be flagged for investigation.

---

## Malware Family Classification

Based on the detailed behavioral analysis provided, here is the classification for the sample:

1. **Malware family**: Unknown
2. **Malware type**: Dropper
3. **Confidence**: High
4. **Key evidence**:
    * **Drop and Execute Sequence:** The binary exhibits a classic dropper lifecycle by identifying temporary directories via `GetTempPathW`, writing files to disk from internal resources using `CreateFileW`/`WriteFile`, and immediately executing them via `ShellExecuteW`.
    * **Advanced Resource Extraction:** The presence of complex parsing logic for embedded data indicates it is designed to unpack multiple stages or modules hidden within encrypted/obfuscated internal resource blocks.
    * **Installer Masquerading:** The binary intentionally utilizes standard Windows UI libraries and system metrics to mimic the behavior of legitimate software (e.g., InstallShield), a common tactic used by droppers to blend in with normal system activity and evade detection.
