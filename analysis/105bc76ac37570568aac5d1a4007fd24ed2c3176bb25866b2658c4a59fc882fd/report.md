# Threat Analysis Report

**Generated:** 2026-08-18 20:07 UTC
**Sample:** `105bc76ac37570568aac5d1a4007fd24ed2c3176bb25866b2658c4a59fc882fd_105bc76ac37570568aac5d1a4007fd24ed2c3176bb25866b2658c4a59fc882fd.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `105bc76ac37570568aac5d1a4007fd24ed2c3176bb25866b2658c4a59fc882fd_105bc76ac37570568aac5d1a4007fd24ed2c3176bb25866b2658c4a59fc882fd.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 5,733,888 bytes |
| MD5 | `62446320089113b10b86c0e78c71507a` |
| SHA1 | `b8e01b0f938529ad6bfe3ffabd55c96a883470ca` |
| SHA256 | `105bc76ac37570568aac5d1a4007fd24ed2c3176bb25866b2658c4a59fc882fd` |
| Overall entropy | 7.998 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1576457453 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,112 | 6.427 | No |
| `.rdata` | 5,120 | 5.136 | No |
| `.data` | 1,536 | 4.006 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 37,376 | 5.356 | No |

### Imports

**KERNEL32.dll**: `ExitProcess`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `CreateFileW`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `SetEnvironmentVariableW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`
**USER32.dll**: `GetWindowRect`, `GetSystemMenu`, `SetClassLongW`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`, `SetClipboardData`
**GDI32.dll**: `SelectObject`, `SetTextColor`, `SetBkMode`, `CreateFontIndirectW`, `CreateBrushIndirect`, `DeleteObject`, `GetDeviceCaps`, `SetBkColor`
**SHELL32.dll**: `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHGetSpecialFolderLocation`, `SHGetFileInfoW`, `SHFileOperationW`, `SHBrowseForFolderW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ord_17`, `ImageList_Destroy`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **12956** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQVPW
#Vh`.@
Instu`
softuW
NulluN	E
SVWj _3
Aj"A[f
D$$SPS
tVj%SSS
f9=(7B
D$$+D$
D$,+D$$P
WWWWjn
us9Et	
FFC;]|
8\tPV
\u f9O
69}t(j
90u'AAf
_^[t	P
UXTHEME
USERENV
SETUPAPI
APPHELP
PROPSYS
DWMAPI
CRYPTBASE
OLEACC
CLBCATQ
NTMARTA
RichEd32
RichEd20
MulDiv
DeleteFileW
FindFirstFileW
FindNextFileW
FindClose
SetFilePointer
ReadFile
MultiByteToWideChar
lstrlenA
WideCharToMultiByte
GetPrivateProfileStringW
WritePrivateProfileStringW
FreeLibrary
LoadLibraryExW
GetModuleHandleW
GlobalAlloc
GlobalFree
ExpandEnvironmentStringsW
lstrcmpW
lstrcmpiW
CloseHandle
SetFileTime
CompareFileTime
SearchPathW
GetShortPathNameW
GetFullPathNameW
MoveFileW
SetCurrentDirectoryW
GetFileAttributesW
SetFileAttributesW
GetTickCount
CreateFileW
GetFileSize
GetModuleFileNameW
GetCurrentProcess
CopyFileW
ExitProcess
SetEnvironmentVariableW
GetWindowsDirectoryW
GetTempPathW
GetCommandLineW
GetVersion
SetErrorMode
lstrlenW
lstrcpynW
GetDiskFreeSpaceW
GlobalUnlock
GlobalLock
CreateThread
GetLastError
CreateDirectoryW
CreateProcessW
RemoveDirectoryW
lstrcmpiA
GetTempFileNameW
WriteFile
lstrcpyA
MoveFileExW
lstrcatW
GetSystemDirectoryW
GetProcAddress
GetModuleHandleA
GetExitCodeProcess
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5904 | ✓ |
| `fcn.004069b5` | `0x4069b5` | 2642 | ✓ |
| `entry0` | `0x40350d` | 1345 | ✓ |
| `fcn.00403b40` | `0x403b40` | 726 | ✓ |
| `fcn.00402f9d` | `0x402f9d` | 673 | ✓ |
| `fcn.0040647c` | `0x40647c` | 626 | ✓ |
| `fcn.00405b6c` | `0x405b6c` | 451 | ✓ |
| `fcn.004060a6` | `0x4060a6` | 378 | ✓ |
| `fcn.00403346` | `0x403346` | 361 | ✓ |
| `fcn.0040323e` | `0x40323e` | 264 | ✓ |
| `fcn.004054c2` | `0x4054c2` | 211 | ✓ |
| `fcn.0040442e` | `0x40442e` | 207 | ✓ |
| `fcn.00404c74` | `0x404c74` | 201 | ✓ |
| `fcn.00403e16` | `0x403e16` | 185 | ✓ |
| `fcn.004066ee` | `0x4066ee` | 175 | ✓ |
| `fcn.00402db1` | `0x402db1` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00402efb` | `0x402efb` | 162 | ✓ |
| `fcn.004063ba` | `0x4063ba` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404d82` | `0x404d82` | 128 | ✓ |
| `fcn.00405e37` | `0x405e37` | 126 | ✓ |
| `fcn.00405991` | `0x405991` | 125 | ✓ |
| `fcn.0040624c` | `0x40624c` | 123 | ✓ |
| `fcn.00406328` | `0x406328` | 121 | ✓ |
| `fcn.00406031` | `0x406031` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004067c4` | `0x4067c4` | 112 | ✓ |
| `fcn.00406927` | `0x406927` | 110 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402db1.c`](code/fcn.00402db1.c)
- [`code/fcn.00402efb.c`](code/fcn.00402efb.c)
- [`code/fcn.00402f9d.c`](code/fcn.00402f9d.c)
- [`code/fcn.0040323e.c`](code/fcn.0040323e.c)
- [`code/fcn.00403346.c`](code/fcn.00403346.c)
- [`code/fcn.00403b40.c`](code/fcn.00403b40.c)
- [`code/fcn.00403e16.c`](code/fcn.00403e16.c)
- [`code/fcn.0040442e.c`](code/fcn.0040442e.c)
- [`code/fcn.00404c74.c`](code/fcn.00404c74.c)
- [`code/fcn.00404d82.c`](code/fcn.00404d82.c)
- [`code/fcn.004054c2.c`](code/fcn.004054c2.c)
- [`code/fcn.00405991.c`](code/fcn.00405991.c)
- [`code/fcn.00405b6c.c`](code/fcn.00405b6c.c)
- [`code/fcn.00405e37.c`](code/fcn.00405e37.c)
- [`code/fcn.00406031.c`](code/fcn.00406031.c)
- [`code/fcn.004060a6.c`](code/fcn.004060a6.c)
- [`code/fcn.0040624c.c`](code/fcn.0040624c.c)
- [`code/fcn.00406328.c`](code/fcn.00406328.c)
- [`code/fcn.004063ba.c`](code/fcn.004063ba.c)
- [`code/fcn.0040647c.c`](code/fcn.0040647c.c)
- [`code/fcn.004066ee.c`](code/fcn.004066ee.c)
- [`code/fcn.004067c4.c`](code/fcn.004067c4.c)
- [`code/fcn.00406927.c`](code/fcn.00406927.c)
- [`code/fcn.004069b5.c`](code/fcn.004069b5.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is an analysis of the binary's behavior.

### Core Functionality and Purpose
The binary appears to be a **custom installer or a "dropper"** using functionality similar to the **NSIS (Nullsoft Script Installer)** framework. Its primary purpose is to act as a wrapper that prepares the environment, verifies integrity, and installs/extracts files onto the local system.

Instead of performing a single action, it contains a large dispatch table (the `switch` statement in `fcn.00401434`) which indicates it interprets an internal script or set of commands to perform various operations like moving files, creating directories, and handling UI elements.

### Suspicious or Malicious Behaviors
While the code contains patterns common in legitimate installers, several features are frequently observed in malware "droppers" used to deliver secondary payloads:

*   **File Manipulation & Deployment:** 
    *   The code makes extensive use of `CopyFileW` and `MoveFileExW`. It specifically looks for files in temporary directories and moves them to final locations.
    *   It implements logic to handle "hidden" or system-level file attributes (via `SetFileAttributesW`) and can change directory paths dynamically during the execution flow.
*   **Privilege Escalation / Manipulation:**
    *   The code explicitly calls `OpenProcessToken`, `LookupPrivilegeValueW`, and `AdjustTokenPrivileges`. 
    *   It specifically targets **`SeShutdownPrivilege`**. While often used by installers to trigger a reboot, this is also a common step in malware to ensure the process has sufficient privileges to interact with system services or modify protected files.
*   **Environment Manipulation:**
    *   The code interacts with environment variables (e.g., setting/checking `TEMP`) and modifies path strings before executing secondary components. This is used both by installers to find assets and by malware to bypass certain security checks or ensure the environment is prepared for a payload.
*   **Integrity Checking:** 
    *   The function `fcn.00402f9d` performs an "integrity check" on files before they are launched. While this ensures a valid installation, in a malware context, it is used to ensure the secondary payload hasn't been tampered with or flagged by security software.

### Notable Techniques and Patterns
*   **Scripted Execution:** The massive switch-case structure (`fcn.00401434`) indicates that the binary isn't just a simple script; it is an engine designed to interpret a list of commands (likely an internal configuration or a compiled script) to perform complex tasks sequentially.
*   **Dynamic Resource Handling:** The use of `GetProcAddress`, `LoadLibraryExW`, and `GetModuleHandleW` suggests that the program loads functionality dynamically. This is often used to delay the loading of potentially sensitive APIs (like networking or injection) until they are actually needed, a common anti-analysis technique.
*   **NSIS-Style Logic:** The presence of strings like `"NSIS Error"`, `"No valid installer"`, and specific ways of handling "hidden" files suggests the author leveraged existing installation frameworks to wrap the payload, which can help it evade detection as a standalone malicious binary.
*   **Process Obfuscation:** By using an installer-like structure, the malware may attempt to appear as a legitimate piece of software (e.g., a game patch or update) during initial analysis.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The large switch-case structure indicates a dispatcher designed to interpret an internal script or command list to perform sequential operations. |
| **T1036** | Masquerading | The use of NSIS-style strings and installer logic allows the binary to appear as legitimate software (e.g., a game patch) to evade detection. |
| **T1548** | Privilege Escalation | The explicit calls to `OpenProcessToken` and `AdjustTokenPrivileges` are used to obtain the necessary permissions for system-level interactions. |
| **T1027** | Obfuscated Files or Packing | While not explicitly "packed," the use of integrity checks and hidden file attributes is a common method to ensure payload viability while avoiding security scrutiny. |
| **T1136** | Search Order Hijacking | The manipulation of environment variables (like `TEMP`) can be used to redirect execution paths or bypass specific security controls. |

***Note on Dynamic Resolution:** The use of `GetProcAddress` and `LoadLibraryExW` is a common technique for "Dynamic Resolution." While it doesn't have a single unique ID in MITRE, it is frequently associated with **Defense Evasion** to bypass static analysis by hiding API imports from the Import Address Table (IAT).*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Many items in the "Extracted Strings" section were identified as standard Windows API functions or common system library calls and were excluded to filter out noise.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified (Note: While the analysis mentions the use of `GetTempPathW` and `RegOpenKeyExW`, no specific hardcoded paths or registry keys were provided in the strings).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Framework Identification:** NSIS (Nullsoft Script Installer) patterns/logic.
*   **Internal Function Offsets:** 
    *   `fcn.00401434` (Identified as a large dispatch table for script interpretation).
    *   `fcn.00402f9d` (Identified as the integrity check routine).
*   **Behavioral Signatures:**
    *   Use of `SetFileAttributesW` to manipulate "hidden" system files.
    *   Privilege Escalation attempt via `SeShutdownPrivilege`.
    *   Dynamic API loading (`GetProcAddress`, `LoadLibraryExW`) for potential anti-analysis/evasion.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**:
    * **Installer-Wrapper Logic:** The binary utilizes NSIS-style installer patterns and a large dispatch table to interpret commands for moving files from temporary directories, and setting "hidden" attributes, which is typical behavior for a wrapper designed to deliver secondary payloads while masquerading as legitimate software.
    * **Evasion & Integrity Checks:** The use of dynamic API resolution (`GetProcAddress`/`LoadLibraryExW`) and specific integrity check routines indicates an intent to hide the program's true capabilities from static analysis and ensure that subsequent components have not been tampered with or flagged by security tools.
    * **Privilege Escalation & Environment Prep:** The explicit attempt to acquire `SeShutdownPrivilege` and the manipulation of environment variables suggest the binary is designed to prepare the system environment and elevate permissions to facilitate the installation of a more significant malicious component.
