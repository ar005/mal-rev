# Threat Analysis Report

**Generated:** 2026-07-14 18:07 UTC
**Sample:** `05d2d06143d363c1e41546f14c1d99b082402460ba4e8598667614de996d2fbc_05d2d06143d363c1e41546f14c1d99b082402460ba4e8598667614de996d2fbc.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05d2d06143d363c1e41546f14c1d99b082402460ba4e8598667614de996d2fbc_05d2d06143d363c1e41546f14c1d99b082402460ba4e8598667614de996d2fbc.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 28,579,888 bytes |
| MD5 | `c711bc35a88de291dcab885ddb2e7373` |
| SHA1 | `0bf7e9c5929aad4e33cd1cd469c12ce52b443047` |
| SHA256 | `05d2d06143d363c1e41546f14c1d99b082402460ba4e8598667614de996d2fbc` |
| Overall entropy | 8.0 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1711817719 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,624 | 6.442 | No |
| `.rdata` | 5,120 | 5.103 | No |
| `.data` | 1,536 | 4.123 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 29,184 | 5.199 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `GetLastError`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`

## Extracted Strings

Total strings found: **62109** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQWPV
Instu`
softuW
NulluN	E
UVWj _3
L$bf-S
D$ Pj(
D$,UPU
tVj%UUU
f9=H/B
D$$+D$
D$,+D$$P
u9=8/B
WWWWjn
us9Et	
FFC;]|
8\tPV
\u f9O
69}t(j
90u'AAf
l$(9l$(tr
+D$(PV
_^][t
P
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
RegisterClassW
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 6189 | ✓ |
| `fcn.00406c11` | `0x406c11` | 2642 | ✓ |
| `entry0` | `0x403665` | 1565 | ✓ |
| `fcn.00403d74` | `0x403d74` | 726 | ✓ |
| `fcn.004030f5` | `0x4030f5` | 673 | ✓ |
| `fcn.004066df` | `0x4066df` | 625 | ✓ |
| `fcn.00405dae` | `0x405dae` | 451 | ✓ |
| `fcn.004062e8` | `0x4062e8` | 378 | ✓ |
| `fcn.0040349e` | `0x40349e` | 361 | ✓ |
| `fcn.00403396` | `0x403396` | 264 | ✓ |
| `fcn.00402ece` | `0x402ece` | 234 | ✓ |
| `fcn.00405727` | `0x405727` | 211 | ✓ |
| `fcn.00404688` | `0x404688` | 207 | ✓ |
| `fcn.00404ece` | `0x404ece` | 201 | ✓ |
| `fcn.0040404a` | `0x40404a` | 185 | ✓ |
| `fcn.00406950` | `0x406950` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00403053` | `0x403053` | 162 | ✓ |
| `fcn.00406602` | `0x406602` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.0040648e` | `0x40648e` | 129 | ✓ |
| `fcn.00404fdc` | `0x404fdc` | 128 | ✓ |
| `fcn.00406079` | `0x406079` | 126 | ✓ |
| `fcn.00406570` | `0x406570` | 121 | ✓ |
| `fcn.00406273` | `0x406273` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406a26` | `0x406a26` | 112 | ✓ |
| `fcn.00406b83` | `0x406b83` | 110 | ✓ |
| `fcn.004057fa` | `0x4057fa` | 108 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402ece.c`](code/fcn.00402ece.c)
- [`code/fcn.00403053.c`](code/fcn.00403053.c)
- [`code/fcn.004030f5.c`](code/fcn.004030f5.c)
- [`code/fcn.00403396.c`](code/fcn.00403396.c)
- [`code/fcn.0040349e.c`](code/fcn.0040349e.c)
- [`code/fcn.00403d74.c`](code/fcn.00403d74.c)
- [`code/fcn.0040404a.c`](code/fcn.0040404a.c)
- [`code/fcn.00404688.c`](code/fcn.00404688.c)
- [`code/fcn.00404ece.c`](code/fcn.00404ece.c)
- [`code/fcn.00404fdc.c`](code/fcn.00404fdc.c)
- [`code/fcn.00405727.c`](code/fcn.00405727.c)
- [`code/fcn.004057fa.c`](code/fcn.004057fa.c)
- [`code/fcn.00405dae.c`](code/fcn.00405dae.c)
- [`code/fcn.00406079.c`](code/fcn.00406079.c)
- [`code/fcn.00406273.c`](code/fcn.00406273.c)
- [`code/fcn.004062e8.c`](code/fcn.004062e8.c)
- [`code/fcn.0040648e.c`](code/fcn.0040648e.c)
- [`code/fcn.00406570.c`](code/fcn.00406570.c)
- [`code/fcn.00406602.c`](code/fcn.00406602.c)
- [`code/fcn.004066df.c`](code/fcn.004066df.c)
- [`code/fcn.00406950.c`](code/fcn.00406950.c)
- [`code/fcn.00406a26.c`](code/fcn.00406a26.c)
- [`code/fcn.00406b83.c`](code/fcn.00406b83.c)
- [`code/fcn.00406c11.c`](code/fcn.00406c11.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C code, here is a technical analysis of the binary’s functionality.

### Core Functionality
The binary functions as an **installer wrapper/stub**, specifically appearing to be based on or mimicking the **Nullsoft Script Installer (NSIS)** framework. Its primary purpose is to serve as a "loader" or "wrapper" that handles the following:
*   **Resource Extraction:** It extracts and unpacks data (likely compressed executables, scripts, or configuration files) from its own internal resources into the system's temporary directory.
*   **Installation Management:** It manages standard installation tasks such as creating registry keys for uninstallation paths, handling file movements, and updating UI elements during a multi-step setup process.
*   **Environment Preparation:** It checks system capabilities (via `GetVersionExW`), prepares the environment for OLE/COM objects, and ensures necessary directory permissions are available.

### Suspicious or Malicious Behaviors
While many of these behaviors are common in legitimate installers, several characteristics are indicative of a **dropper** or **packer** often used in malware distribution:

*   **Self-Extraction & Dropping:** The code identifies and extracts files into the `%TEMP%` directory using a specific naming convention (`nsu%X.tmp`). This is a classic technique to drop a "hidden" payload (the actual malware) that is then executed by the stub.
*   **Privilege Escalation:** The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` specifically targets high-level privileges (e.g., `SeShutdownPrivilege`). While sometimes used in legitimate system tools, it is frequently used by malware to gain the permissions necessary to modify system files or registry keys protected by the OS.
*   **Integrity Checks:** The code includes extensive logic to verify the integrity of the data being extracted/processed (e.g., checking file sizes and potential CRC checks). This ensures that the malicious payload is not corrupted during the extraction process before it is launched.
*   **File Manipulation & Renaming:** Function `fcn.004062e8` explicitly handles "Renaming" logic, where files are read into memory, manipulated, and written to new paths. This can be used to rename a generic malicious file to something that looks legitimate (e.g., `svchost.exe`) after it is dropped.

### Notable Techniques & Patterns
*   **NSIS Framework Indicators:** The presence of the string `"NSIS Error"` and references to `nsis.sf.net` confirms the use of an NSIS-based wrapper. Malware authors frequently use these because they provide a convenient way to bundle and hide malicious payloads.
*   **Heavy Use of Windows API for File/Registry Management:** The code heavily utilizes:
    *   `CreateFileW`, `WriteFile`, `MoveFileW`: For manipulating the underlying filesystem.
    *   `RegOpenKeyExW`, `RegSetValueExW`: To ensure persistence or record installation data.
    *   `GetTempPathW`: Specifically to find a location where it can drop files with lower-level scrutiny than standard folders like `Program Files`.
*   **Dynamic Path Construction:** The code constructs paths dynamically using `GetSystemDirectoryW`, `GetWindowsDirectoryW`, and `ExpandEnvironmentStringsW`. This allows the binary to be portable and work across different user configurations.
*   **Complex Control Flow for GUI Interaction:** Function `fcn.00401434` contains a large switch-case table (nearly 70 cases) used to handle various UI interactions, button clicks, and window messages. This indicates the installer has a fully functional (though likely automated/scripted) graphical interface.

### Summary for Incident Response
The binary is an **installer stub**. It acts as a "carrier" that unpacks and executes a secondary payload in the `%TEMP%` folder. The presence of privilege escalation logic and automated file-hiding behaviors suggests it is highly likely used to deliver malicious software (Dropper behavior).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of an NSIS-based wrapper to bundle, hide, and later extract a secondary payload from internal resources is characteristic of a packer/dropper. |
| **T1036** | Masquerading | The specific logic to rename files to common system names (e.g., `svchost.exe`) after extraction is intended to hide malicious activity in plain sight. |
| **T1068** | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` demonstrates an attempt to acquire high-level system privileges beyond the standard user level. |
| **T1112** | Modify Registry | The usage of `RegOpenKeyExW` and `RegSetValueExW` to manage installation paths and data can be used for persistent storage or ensuring the malware remains active. |
| **T1036.005** | Masquerading (Dynamic Link Library) | While a broader masquerade exists, the use of a wrapper to disguise the presence of an executable "installer" is a common method to blend in with legitimate system tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `nsis.sf.net` (Identified via framework analysis; indicates use of Nullsoft Script Installer)

**File paths / Registry keys**
*   `%TEMP%` (Used as a primary drop location for unpacked payloads)
*   `nsu%X.tmp` (Specific naming convention for temporary files used during the extraction process)
*   *Note: Standard Windows system paths and DLLs identified in the strings (e.g., `SYSTEM32`, `USER32.dll`) are excluded as false positives.*

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Internal Strings/Patterns:** `"NSIS Error"` (Confirms the use of an NSIS-based wrapper).
*   **Behavioral Patterns:** 
    *   **Dropper Behavior:** Extraction and execution of a secondary payload from internal resources into the `%TEMP%` directory.
    *   **Privilege Escalation:** Use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` to gain high-level system permissions.
    *   **Masquerading:** Logic identified in function `fcn.004062e8` for renaming files to legitimate names (e.g., `svchost.exe`).
    *   **Automated GUI:** Complex switch-case table at `fcn.00401434` indicating a scripted installation/interaction flow.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown (NSIS-based Dropper)
2. **Malware type**: dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Dropper/Wrapper Functionality:** The binary acts as a standard NSIS installer wrapper, specifically designed to extract and unpack hidden payloads from internal resources into the `%TEMP%` directory before execution.
*   **Evasion & Masquerading:** The analysis identifies explicit logic for renaming files to common system names (e.g., `svchost.exe`) and utilizing a complex automated GUI to hide the transition between the installer and the malicious payload.
*   **Privilege Escalation:** The presence of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicates an attempt to gain elevated permissions, typically required for a secondary payload to modify system files or achieve persistence.
