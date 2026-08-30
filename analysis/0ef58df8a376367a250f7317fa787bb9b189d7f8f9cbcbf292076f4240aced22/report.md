# Threat Analysis Report

**Generated:** 2026-08-15 15:39 UTC
**Sample:** `0ef58df8a376367a250f7317fa787bb9b189d7f8f9cbcbf292076f4240aced22_0ef58df8a376367a250f7317fa787bb9b189d7f8f9cbcbf292076f4240aced22.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ef58df8a376367a250f7317fa787bb9b189d7f8f9cbcbf292076f4240aced22_0ef58df8a376367a250f7317fa787bb9b189d7f8f9cbcbf292076f4240aced22.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 941,000 bytes |
| MD5 | `b67833a72285c5f1232c47ae94ed6ca1` |
| SHA1 | `0dc96f8ab9fb06e6a65712dc405a20b5d0ced471` |
| SHA256 | `0ef58df8a376367a250f7317fa787bb9b189d7f8f9cbcbf292076f4240aced22` |
| Overall entropy | 7.986 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1627165075 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,112 | 6.402 | No |
| `.rdata` | 5,120 | 5.138 | No |
| `.data` | 1,536 | 4.021 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 7,168 | 5.239 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `SetFileSecurityW`, `RegOpenKeyExW`, `RegEnumValueW`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHFileOperationW`, `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `ShellExecuteExW`, `SHGetFileInfoW`
**ole32.dll**: `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `GetClientRect`, `EndPaint`, `DrawTextW`, `IsWindowEnabled`, `DispatchMessageW`, `wsprintfA`, `CharNextA`, `CharPrevW`, `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `GetSystemMetrics`, `FillRect`, `AppendMenuW`, `TrackPopupMenu`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectW`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetModuleHandleA`, `GetProcAddress`, `GetSystemDirectoryW`, `lstrcatW`, `Sleep`, `lstrcpyA`, `WriteFile`, `GetTempFileNameW`, `CreateFileW`, `lstrcmpiA`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`

## Extracted Strings

Total strings found: **2192** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495l
tQWPV
v#Vh+/@
Instu`
softuW
NulluN	E
SVWj _3
Aj"A[f
D$ Ph0
D$$SPS
tVj%SSS
D$$+D$
D$,+D$$P
WWWWjn
uv9Et	
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
SetFileSecurityW
RegOpenKeyExW
RegCreateKeyExW
ADVAPI32.dll
SHFileOperationW
SHGetFileInfoW
SHBrowseForFolderW
SHGetPathFromIDListW
ShellExecuteExW
SHGetSpecialFolderLocation
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
| `fcn.00401434` | `0x401434` | 6048 | ✓ |
| `fcn.0040694b` | `0x40694b` | 2642 | ✓ |
| `entry0` | `0x40348f` | 1345 | ✓ |
| `fcn.00403aaa` | `0x403aaa` | 726 | ✓ |
| `fcn.00406418` | `0x406418` | 626 | ✓ |
| `fcn.00403015` | `0x403015` | 567 | ✓ |
| `fcn.0040324c` | `0x40324c` | 485 | ✓ |
| `fcn.00405aed` | `0x405aed` | 451 | ✓ |
| `fcn.00406027` | `0x406027` | 378 | ✓ |
| `fcn.00402e41` | `0x402e41` | 234 | ✓ |
| `fcn.00405443` | `0x405443` | 211 | ✓ |
| `fcn.00404398` | `0x404398` | 207 | ✓ |
| `fcn.00404bde` | `0x404bde` | 201 | ✓ |
| `fcn.00403d80` | `0x403d80` | 185 | ✓ |
| `fcn.0040668a` | `0x40668a` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040633b` | `0x40633b` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404cec` | `0x404cec` | 128 | ✓ |
| `fcn.00405db8` | `0x405db8` | 126 | ✓ |
| `fcn.00405912` | `0x405912` | 125 | ✓ |
| `fcn.004061cd` | `0x4061cd` | 123 | ✓ |
| `fcn.004062a9` | `0x4062a9` | 121 | ✓ |
| `fcn.00405fb2` | `0x405fb2` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406760` | `0x406760` | 112 | ✓ |
| `fcn.004068bd` | `0x4068bd` | 110 | ✓ |
| `fcn.00405516` | `0x405516` | 108 | ✓ |
| `fcn.00405a41` | `0x405a41` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402e41.c`](code/fcn.00402e41.c)
- [`code/fcn.00403015.c`](code/fcn.00403015.c)
- [`code/fcn.0040324c.c`](code/fcn.0040324c.c)
- [`code/fcn.00403aaa.c`](code/fcn.00403aaa.c)
- [`code/fcn.00403d80.c`](code/fcn.00403d80.c)
- [`code/fcn.00404398.c`](code/fcn.00404398.c)
- [`code/fcn.00404bde.c`](code/fcn.00404bde.c)
- [`code/fcn.00404cec.c`](code/fcn.00404cec.c)
- [`code/fcn.00405443.c`](code/fcn.00405443.c)
- [`code/fcn.00405516.c`](code/fcn.00405516.c)
- [`code/fcn.00405912.c`](code/fcn.00405912.c)
- [`code/fcn.00405a41.c`](code/fcn.00405a41.c)
- [`code/fcn.00405aed.c`](code/fcn.00405aed.c)
- [`code/fcn.00405db8.c`](code/fcn.00405db8.c)
- [`code/fcn.00405fb2.c`](code/fcn.00405fb2.c)
- [`code/fcn.00406027.c`](code/fcn.00406027.c)
- [`code/fcn.004061cd.c`](code/fcn.004061cd.c)
- [`code/fcn.004062a9.c`](code/fcn.004062a9.c)
- [`code/fcn.0040633b.c`](code/fcn.0040633b.c)
- [`code/fcn.00406418.c`](code/fcn.00406418.c)
- [`code/fcn.0040668a.c`](code/fcn.0040668a.c)
- [`code/fcn.00406760.c`](code/fcn.00406760.c)
- [`code/fcn.004068bd.c`](code/fcn.004068bd.c)
- [`code/fcn.0040694b.c`](code/fcn.0040694b.c)

## Behavioral Analysis

Based on the analysis of the provided disassembly and strings, here is a summary of the binary's behavior:

### Core Functionality and Purpose
The binary is a **GUI-based installer** or setup utility, likely built using the **NSIS (Nullsoft Script Installer)** framework. 

*   **Script Interpretation:** The large `switch` tables (e.g., in `fcn.00401434`) and the repetitive use of internal resolution functions like `fcn.004067d0()` indicate that this is an interpreter/engine. It processes a script to perform various actions such as creating folders, moving files, and updating registry keys.
*   **Installer Workflow:** The entry point (`entry0`) performs standard setup tasks: initializing Common Controls (COMCTL32), initializing OLE objects, processing command-line arguments, and determining the installation path (often via `GetTempPathW` or a defined directory).

### Suspicious or Malicious Behaviors
While this specific code is characteristic of an installer, in a malware context, such installers are frequently used as **"droppers"** or **"wrappers."** 

*   **Integrity Checks:** The function `fcn.00403015` contains a hardcoded "Installer integrity check" error message (e.g., `nsis_error`). This is common in installers to ensure the payload has not been tampered with before execution.
*   **File System Manipulation:** There are numerous calls to:
    *   `CreateDirectoryW`: Creating installation paths.
    *   `MoveFileW / CopyFileW`: Moving extracted files from a temporary directory (like `%TEMP%`) to their final destination.
    *   `GetTempFileNameW`: Generating temporary filenames for intermediate processing.
*   **Registry Interaction:** The code uses `RegOpenKeyExW`, `RegSetValueExW`, and `RegQueryValueExW`. While standard for installing software, these are also used by malware to achieve persistence or change system configurations.
*   **Privilege Escalation/Security:** Function `fcn.00405912` calls `SetFileSecurityW` after creating a directory. This suggests the installer is attempting to set specific permissions on its folders, ensuring that only the owner (or specific users) can access certain files.

### Notable Techniques and Patterns
*   **NSIS Framework:** The presence of strings like "nsis" and the specific logic used to handle script instructions strongly indicates this is a standard NSIS installer. This means the actual "malicious" payload is likely bundled inside this executable or provided in an accompanying file.
*   **Environment Sensing:** The code queries system information (e.g., `GetSystemDirectoryW`, `GetWindowsDirectoryW`) and handles "UXTHEME" to ensure compatibility with Windows visual styles. 
*   **Standard API Abstraction:** Instead of interacting directly with files, the binary often calls intermediate functions (`fcn.004063db`, etc.) that likely process script variables before calling the underlying Windows APIs like `MoveFileW`.

### Summary for Incident Response
This binary is a **wrapper/installer**. If this was found in an investigation:
1.  It is not necessarily "malicious" on its own, but it acts as the vehicle to deploy and install other components.
2.  The actual payload (the malware) is likely contained within the resources of this file or will be downloaded/extracted by the logic seen in `fcn.00401434`.
3.  **Persistence Check:** Look for registry keys set via `RegSetValueExW` and files moved to `C:\Windows\` or `C:\Program Files\` via `MoveFileW`.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1566.001 | Dropper | The binary acts as a "wrapper" or installer that serves as a vehicle to deploy and install additional malicious components or payloads. |
| T1112 | Modify Registry | The use of `RegSetValueExW` and `RegQueryValueExW` indicates the binary modifies registry keys for configuration, persistence, or system modification. |
| T1036 | Masquerading | By utilizing the standard NSIS framework, the malware disguises its functionality as a legitimate installer to blend in with normal software. |
| T1082 | System Information Discovery | The use of `GetSystemDirectoryW` and `GetWindowsDirectoryW` indicates an attempt to gather information about the host environment for installation or persistence logic. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** Many items in the "Extracted Strings" section were identified as standard Windows API calls or library functions (e.g., `USER32.dll`, `CreateProcessW`, `GetTempPathW`) and have been excluded per your instructions to skip common system artifacts.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The analysis mentions that the binary interacts with registry keys and moves files via `MoveFileW`, but no specific, hardcoded malicious paths or specific keys—e.g., `HKLM\Software\...`—were provided in the text.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Framework:** NSIS (Nullsoft Script Installer) wrapper.
*   **Behavioral Note:** The binary utilizes a standard installer architecture to mask its payload, utilizing `GetTempPathW` and `MoveFileExW` for file deployment.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **NSIS Framework Usage:** The binary utilizes the Nullsoft Script Installer (NSIS) framework, a common technique used by threat actors to mask malicious payloads as legitimate installers and hide their functionality behind standard installation workflows.
*   **Dropper Behavior:** The presence of "wrapper" logic—specifically moving files from temporary directories (`GetTempPathW`, `MoveFileW`) and modifying registry keys for persistence/configuration—indicates the primary purpose is to deploy a secondary payload.
*   **Masquerading & Integrity Checks:** The inclusion of integrity checks (e.g., `nsis_error`) and environment sensing are classic indicators of malware designed to ensure it is running in an intended environment before "dropping" its core malicious components.
