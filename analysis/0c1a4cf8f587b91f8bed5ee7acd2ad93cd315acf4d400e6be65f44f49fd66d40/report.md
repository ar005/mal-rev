# Threat Analysis Report

**Generated:** 2026-07-29 18:50 UTC
**Sample:** `0c1a4cf8f587b91f8bed5ee7acd2ad93cd315acf4d400e6be65f44f49fd66d40_0c1a4cf8f587b91f8bed5ee7acd2ad93cd315acf4d400e6be65f44f49fd66d40.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c1a4cf8f587b91f8bed5ee7acd2ad93cd315acf4d400e6be65f44f49fd66d40_0c1a4cf8f587b91f8bed5ee7acd2ad93cd315acf4d400e6be65f44f49fd66d40.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 87,172,376 bytes |
| MD5 | `167538ca94ab799b6ae3b17fcd62d8a4` |
| SHA1 | `cb2ad44fe4779ae5aefb6ad6600d78448827d789` |
| SHA256 | `0c1a4cf8f587b91f8bed5ee7acd2ad93cd315acf4d400e6be65f44f49fd66d40` |
| Overall entropy | 7.998 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1741475120 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 27,136 | 6.466 | No |
| `.rdata` | 5,120 | 5.1 | No |
| `.data` | 1,536 | 4.111 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 23,040 | 3.08 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`, `GetCommandLineW`

## Extracted Strings

Total strings found: **184046** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQWPV
Instui
softu`
NulluW	E
UVWj _3
L$bf-S
D$ Pj(
D$,UPU
tVj%UUU
D$$+D$
D$,+D$$P
WWWWjn
us9Et	
FFC;]|
8\tPV
\u f9O
69}t(j
90u'AAf
L$(9-$
l$(9l$(tr
+D$(PV
_^][t
P
D$SVW
A@;E |
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
RegEnumValueW
RegEnumKeyW
RegQueryValueExW
RegSetValueExW
RegCloseKey
RegDeleteValueW
RegDeleteKeyW
AdjustTokenPrivileges
LookupPrivilegeValueW
OpenProcessToken
RegOpenKeyExW
RegCreateKeyExW
ADVAPI32.dll
SHFileOperationW
SHGetFileInfoW
SHBrowseForFolderW
SHGetPathFromIDListW
ShellExecuteExW
SHELL32.dll
CoTaskMemFree
IIDFromString
CoCreateInstance
OleUninitialize
OleInitialize
ole32.dll
ImageList_Destroy
ImageList_AddMasked
ImageList_Create
COMCTL32.dll
EndPaint
DrawTextW
FillRect
GetClientRect
BeginPaint
DefWindowProcW
SendMessageW
InvalidateRect
EnableWindow
ReleaseDC
LoadImageW
SetWindowLongW
GetDlgItem
IsWindow
FindWindowExW
SendMessageTimeoutW
wsprintfW
ShowWindow
SetForegroundWindow
PostQuitMessage
SetWindowTextW
SetTimer
CreateDialogParamW
DestroyWindow
ExitWindowsEx
CharNextW
DialogBoxParamW
GetClassInfoW
CreateWindowExW
SystemParametersInfoW
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 6196 | ✓ |
| `fcn.00406dce` | `0x406dce` | 2183 | ✓ |
| `entry0` | `0x4036a5` | 1565 | ✓ |
| `fcn.004030fc` | `0x4030fc` | 730 | ✓ |
| `fcn.00403db4` | `0x403db4` | 726 | ✓ |
| `fcn.0040671f` | `0x40671f` | 625 | ✓ |
| `fcn.00405dee` | `0x405dee` | 451 | ✓ |
| `fcn.00406328` | `0x406328` | 378 | ✓ |
| `fcn.004034de` | `0x4034de` | 361 | ✓ |
| `fcn.00406c86` | `0x406c86` | 328 | ✓ |
| `fcn.004033d6` | `0x4033d6` | 264 | ✓ |
| `fcn.00402ed5` | `0x402ed5` | 234 | ✓ |
| `fcn.00407787` | `0x407787` | 216 | ✓ |
| `fcn.00405767` | `0x405767` | 211 | ✓ |
| `fcn.004046c8` | `0x4046c8` | 207 | ✓ |
| `fcn.00404f0e` | `0x404f0e` | 201 | ✓ |
| `fcn.0040408a` | `0x40408a` | 185 | ✓ |
| `fcn.00406990` | `0x406990` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040305a` | `0x40305a` | 162 | ✓ |
| `fcn.00406642` | `0x406642` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.004064ce` | `0x4064ce` | 129 | ✓ |
| `fcn.00407706` | `0x407706` | 129 | ✓ |
| `fcn.0040501c` | `0x40501c` | 128 | ✓ |
| `fcn.004060b9` | `0x4060b9` | 126 | ✓ |
| `fcn.004065b0` | `0x4065b0` | 121 | ✓ |
| `fcn.004062b3` | `0x4062b3` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402ed5.c`](code/fcn.00402ed5.c)
- [`code/fcn.0040305a.c`](code/fcn.0040305a.c)
- [`code/fcn.004030fc.c`](code/fcn.004030fc.c)
- [`code/fcn.004033d6.c`](code/fcn.004033d6.c)
- [`code/fcn.004034de.c`](code/fcn.004034de.c)
- [`code/fcn.00403db4.c`](code/fcn.00403db4.c)
- [`code/fcn.0040408a.c`](code/fcn.0040408a.c)
- [`code/fcn.004046c8.c`](code/fcn.004046c8.c)
- [`code/fcn.00404f0e.c`](code/fcn.00404f0e.c)
- [`code/fcn.0040501c.c`](code/fcn.0040501c.c)
- [`code/fcn.00405767.c`](code/fcn.00405767.c)
- [`code/fcn.00405dee.c`](code/fcn.00405dee.c)
- [`code/fcn.004060b9.c`](code/fcn.004060b9.c)
- [`code/fcn.004062b3.c`](code/fcn.004062b3.c)
- [`code/fcn.00406328.c`](code/fcn.00406328.c)
- [`code/fcn.004064ce.c`](code/fcn.004064ce.c)
- [`code/fcn.004065b0.c`](code/fcn.004065b0.c)
- [`code/fcn.00406642.c`](code/fcn.00406642.c)
- [`code/fcn.0040671f.c`](code/fcn.0040671f.c)
- [`code/fcn.00406990.c`](code/fcn.00406990.c)
- [`code/fcn.00406c86.c`](code/fcn.00406c86.c)
- [`code/fcn.00406dce.c`](code/fcn.00406dce.c)
- [`code/fcn.00407706.c`](code/fcn.00407706.c)
- [`code/fcn.00407787.c`](code/fcn.00407787.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is a technical analysis of the binary's behavior.

### Core Functionality and Purpose
The code functions as an **installer wrapper or "dropper."** It utilizes logic typical of the Nullsoft Script Installer (NSIS) framework to unpack, verify, and execute a secondary payload. The primary goal is to move files from an initial location into a temporary directory, perform integrity checks, and then launch the final executable.

### Suspicious or Malicious Behaviors
The following behaviors are common in malware "stagers" or droppers:

*   **Dropping and Moving Files:** 
    *   The code frequently uses `GetTempPathW`, `MoveFileW`, and `CopyFileW`. It specifically targets the `%TEMP%` directory to extract files (e.g., using filenames like `ns_...tmp`).
    *   It performs manual path manipulations and expansion via `ExpandEnvironmentStringsW` to ensure it can resolve system paths regardless of where the user runs the installer.
*   **Persistence and Configuration:**
    *   The inclusion of a large number of registry-related functions (`RegEnumValueW`, `RegEnumKeyW`, `RegOpenKeyExW`) suggests that the binary is designed to check for, create, or modify system registry keys, likely for configuration of the payload or establishing persistence.
*   **Environment Manipulation:** 
    *   The code explicitly calls `SetEnvironmentVariableW` to manipulate variables like "TEMP." This is a common technique to ensure that subsequent child processes (the actual payload) are executed in controlled directories.
*   **Integrity Checks and Verification:**
    *   Function `fcn.004030fc` appears to be an **integrity check mechanism**. It compares file sizes, calculates offsets, and validates "blocks" of data before allowing the execution to proceed. This is often used by malware to ensure that a downloaded payload was not corrupted or modified by security software during transit.
*   **Privilege Manipulation:** 
    *   The use of `LookupPrivilegeValueW`, `OpenProcessToken`, and `AdjustTokenPrivileges` indicates an attempt to check for or acquire elevated privileges (such as `SeShutdownPrivilege`) before executing the main payload.

### Notable Techniques and Patterns
*   **NSIS Framework Utilization:** The string `"NSIS Error"` and the specific handling of `.nsi` style logic indicate this is likely a modified installer script. Malware authors often use these to hide their primary malicious code inside a legitimate-looking installer.
*   **Dynamic Execution/Loading:** The inclusion of `LoadLibraryExW` and `GetProc_Address` (implied by the way it handles `pcVar14` as a function pointer) suggests that the binary might dynamically load required DLLs or capabilities only at the moment they are needed to evade static analysis.
*   **Complex Dispatch Table:** The large switch-case structure in `fcn.00401434` is typical of an interpreted script engine (like NSIS). This allows the malware's behavior to be changed by simply modifying a configuration file or script embedded within it, rather than changing the binary itself.
*   **Data Obfuscation:** The way `fcn.004030fc` handles data in "blocks" of 0x10 suggests that the payload is stored in an obfuscated or packed format and is only unpacked into memory/temp folders at runtime.

### Summary for Incident Response
This binary is a **Stage-1 Dropper**. It does not perform complex network communication directly, but it prepares the environment by:
1.  **Extracting and validating** a hidden payload in the `%TEMP%` folder.
2.  **Modifying registry keys** for persistence or settings.
3.  **Escalating privileges** to ensure the payload can run with administrative rights.

If this binary is found on a system, it should be treated as an indicator of a multi-stage infection where the primary malware has likely been "dropped" by this loader.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of an NSIS installer wrapper and common system directories (e.g., `%TEMP%`) allows the malware to blend in with legitimate installation processes. |
| T1112 | Modify Registry | The wide range of registry-related functions indicates a clear intent to modify system configuration or establish persistence for the payload. |
| T1059 | Command and Scripting Interpreter | The "complex dispatch table" and "NSI style logic" suggest an interpreted script engine is used to manage execution flow and behavior changes. |
| T1068 | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` indicates a targeted attempt to acquire higher privileges before the final payload is executed. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Standard Windows API calls (e.g., `CreateProcessW`, `GetTempPathW`) and common system libraries have been excluded as per your instructions regarding false positives.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None (The analysis notes the use of `%TEMP%` and registry manipulation, but no specific malicious hardcoded paths or non-standard registry keys were identified in the strings).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **String:** `NSIS Error` (Indicates usage of the Nullsoft Script Installer framework as a wrapper/dropper).
*   **Function Offset:** `fcn.004030fc` (Identified as an integrity check mechanism).
*   **Function Offset:** `fcn.00401434` (Identified as a complex dispatch table for script execution).
*   **File Pattern:** `ns_...tmp` (Used during the extraction/dropping phase in the temporary directory).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

**Key evidence**:
*   **Installer Masquerading:** The binary utilizes the Nullsoft Script Installer (NSIS) framework to hide its activities, using typical installer behaviors (like `GetTempPathW` and `ExpandEnvironmentStringsW`) to blend in with legitimate software installations.
*   **Staging Behavior:** It functions as a Stage-1 component by extracting, renaming (`ns_...tmp`), and validating the integrity of a secondary payload in the `%TEMP%` directory before execution.
*   **Evasion & Persistence:** The presence of an integrity check mechanism (`fcn.004030fc`) suggests it is designed to verify that its payload hasn't been tampered with by security software, while heavy registry activity and privilege escalation calls indicate a preparation for persistent infection.
