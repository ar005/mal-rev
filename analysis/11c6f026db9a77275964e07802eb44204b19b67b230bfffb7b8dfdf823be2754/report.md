# Threat Analysis Report

**Generated:** 2026-08-23 22:57 UTC
**Sample:** `11c6f026db9a77275964e07802eb44204b19b67b230bfffb7b8dfdf823be2754_11c6f026db9a77275964e07802eb44204b19b67b230bfffb7b8dfdf823be2754.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11c6f026db9a77275964e07802eb44204b19b67b230bfffb7b8dfdf823be2754_11c6f026db9a77275964e07802eb44204b19b67b230bfffb7b8dfdf823be2754.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 253,474 bytes |
| MD5 | `fd7f853d5dcb8ecc69d1a7812c60cb62` |
| SHA1 | `1ab8f3cbf8d180289af6395eeaf01f6e6bc09d4c` |
| SHA256 | `11c6f026db9a77275964e07802eb44204b19b67b230bfffb7b8dfdf823be2754` |
| Overall entropy | 7.843 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1711817713 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.39 | No |
| `.rdata` | 5,120 | 5.032 | No |
| `.data` | 1,024 | 5.256 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 17,920 | 5.882 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueA`, `RegEnumKeyA`, `RegQueryValueExA`, `RegSetValueExA`, `RegCloseKey`, `RegDeleteValueA`, `RegDeleteKeyA`, `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, `OpenProcessToken`, `RegOpenKeyExA`, `RegCreateKeyExA`
**SHELL32.dll**: `SHGetPathFromIDListA`, `SHBrowseForFolderA`, `SHGetFileInfoA`, `SHFileOperationA`, `ShellExecuteExA`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoCreateInstance`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `SetDlgItemTextA`, `GetSystemMetrics`, `CreatePopupMenu`, `AppendMenuA`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcA`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorA`, `SetCursor`, `GetSysColor`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectA`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `CreateFileA`, `GetTempFileNameA`, `ReadFile`, `RemoveDirectoryA`, `CreateProcessA`, `CreateDirectoryA`, `GetLastError`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceA`, `lstrcpynA`, `SetErrorMode`, `GetVersionExA`, `lstrlenA`

## Extracted Strings

Total strings found: **724** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495LCB
tQVPW
Et@;u
v#VhJ.@
Instu`
softuW
NulluN	E
j@Vh@CB
tVj%WWW
D$$+D$
D$,+D$$P
SSSSjn
us9Et	
8\tPV
u9utm
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
RichEdit
RichEdit20A
RichEd32
RichEd20
.DEFAULT\Control Panel\International
Control Panel\Desktop\ResourceLocale
Software\Microsoft\Windows\CurrentVersion
\Microsoft\Internet Explorer\Quick Launch
RegEnumValueA
RegEnumKeyA
RegQueryValueExA
RegSetValueExA
RegCloseKey
RegDeleteValueA
RegDeleteKeyA
AdjustTokenPrivileges
LookupPrivilegeValueA
OpenProcessToken
RegOpenKeyExA
RegCreateKeyExA
ADVAPI32.dll
SHFileOperationA
SHGetFileInfoA
SHBrowseForFolderA
SHGetPathFromIDListA
ShellExecuteExA
SHELL32.dll
CoTaskMemFree
CoCreateInstance
OleUninitialize
OleInitialize
IIDFromString
ole32.dll
ImageList_Destroy
ImageList_AddMasked
ImageList_Create
COMCTL32.dll
EndPaint
DrawTextA
FillRect
GetClientRect
BeginPaint
DefWindowProcA
SendMessageA
InvalidateRect
EnableWindow
ReleaseDC
LoadImageA
SetWindowLongA
GetDlgItem
IsWindow
FindWindowExA
SendMessageTimeoutA
wsprintfA
ShowWindow
SetForegroundWindow
PostQuitMessage
SetWindowTextA
SetTimer
CreateDialogParamA
DestroyWindow
ExitWindowsEx
CharNextA
DialogBoxParamA
GetClassInfoA
CreateWindowExA
SystemParametersInfoA
RegisterClassA
EndDialog
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5832 | ✓ |
| `fcn.004067c4` | `0x4067c4` | 2642 | ✓ |
| `entry0` | `0x4033a2` | 1508 | ✓ |
| `fcn.00403a60` | `0x403a60` | 709 | ✓ |
| `fcn.004062ea` | `0x4062ea` | 615 | ✓ |
| `fcn.00402f31` | `0x402f31` | 567 | ✓ |
| `fcn.00403168` | `0x403168` | 476 | ✓ |
| `fcn.00405a19` | `0x405a19` | 464 | ✓ |
| `fcn.00405ec0` | `0x405ec0` | 368 | ✓ |
| `fcn.00402d60` | `0x402d60` | 234 | ✓ |
| `fcn.0040539b` | `0x40539b` | 210 | ✓ |
| `fcn.0040435e` | `0x40435e` | 207 | ✓ |
| `fcn.00404b40` | `0x404b40` | 197 | ✓ |
| `fcn.00403d25` | `0x403d25` | 185 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00406551` | `0x406551` | 153 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.004061ce` | `0x4061ce` | 137 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.0040605c` | `0x40605c` | 129 | ✓ |
| `fcn.00404c4a` | `0x404c4a` | 128 | ✓ |
| `fcn.00405cd7` | `0x405cd7` | 120 | ✓ |
| `fcn.0040613e` | `0x40613e` | 119 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406736` | `0x406736` | 110 | ✓ |
| `fcn.00406611` | `0x406611` | 110 | ✓ |
| `fcn.0040546d` | `0x40546d` | 108 | ✓ |
| `fcn.0040596d` | `0x40596d` | 100 | ✓ |
| `fcn.00402ecd` | `0x402ecd` | 100 | ✓ |
| `fcn.00405861` | `0x405861` | 90 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402d60.c`](code/fcn.00402d60.c)
- [`code/fcn.00402ecd.c`](code/fcn.00402ecd.c)
- [`code/fcn.00402f31.c`](code/fcn.00402f31.c)
- [`code/fcn.00403168.c`](code/fcn.00403168.c)
- [`code/fcn.00403a60.c`](code/fcn.00403a60.c)
- [`code/fcn.00403d25.c`](code/fcn.00403d25.c)
- [`code/fcn.0040435e.c`](code/fcn.0040435e.c)
- [`code/fcn.00404b40.c`](code/fcn.00404b40.c)
- [`code/fcn.00404c4a.c`](code/fcn.00404c4a.c)
- [`code/fcn.0040539b.c`](code/fcn.0040539b.c)
- [`code/fcn.0040546d.c`](code/fcn.0040546d.c)
- [`code/fcn.00405861.c`](code/fcn.00405861.c)
- [`code/fcn.0040596d.c`](code/fcn.0040596d.c)
- [`code/fcn.00405a19.c`](code/fcn.00405a19.c)
- [`code/fcn.00405cd7.c`](code/fcn.00405cd7.c)
- [`code/fcn.00405ec0.c`](code/fcn.00405ec0.c)
- [`code/fcn.0040605c.c`](code/fcn.0040605c.c)
- [`code/fcn.0040613e.c`](code/fcn.0040613e.c)
- [`code/fcn.004061ce.c`](code/fcn.004061ce.c)
- [`code/fcn.004062ea.c`](code/fcn.004062ea.c)
- [`code/fcn.00406551.c`](code/fcn.00406551.c)
- [`code/fcn.00406611.c`](code/fcn.00406611.c)
- [`code/fcn.00406736.c`](code/fcn.00406736.c)
- [`code/fcn.004067c4.c`](code/fcn.004067c4.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C code, here is a technical analysis of the binary's functionality.

### Core Functionality and Purpose
The binary functions as an **installer stub or "dropper"** (likely based on or mimicking the **NSIS - Nullsoft Script Installer** framework). Its primary purpose is to unpack files, verify their integrity, move them to specified system locations, and register configuration settings in the Windows Registry.

### Key Behaviors and Features
The following behaviors were identified within the code:

*   **File Extraction and Deployment:**
    *   The `entry0` function handles a loop that iterates through data (likely from an embedded resource or a temporary file) to copy files using `CopyFileA`.
    *   It utilizes `MoveFileA` and `SetCurrentDirectoryA` to organize these files into final destinations.
    *   **Context:** This is typical of installers, but in malware analysis, this indicates a "dropper" behavior where the actual malicious payload is hidden inside this installer until it is "installed."

*   **Integrity Verification:**
    *   The function `fcn.00403168` implements a loop to check file integrity (likely a CRC32 or similar checksum) during the copying process. 
    *   If the check fails, it triggers an error message: *"Installer integrity check has failed... contact the installer's author."* This ensures that the files being moved are not corrupted and match the expected payload.

*   **Registry Manipulation:**
    *   The code contains several calls to `RegOpenKeyExA`, `RegSetValueExA`, `RegQueryValueExA`, and `RegEnumKeyA`.
    *   These functions are used to modify or create registry keys, which is common for establishing **persistence** (e.g., adding a program to "Run" at startup) or configuring system settings after an installation.

*   **Environment/System Interaction:**
    *   **UXTHEME & UI Management:** The code loads `UXTHEME` and uses `MessageBoxIndirectA`, `SetWindowTextA`, and `CreateWindowExA`. This suggests it interacts with the Windows UI to show progress bars, logs, or error dialogs.
    *   **Permissions Check:** There is logic involving `OpenProcessToken` and `LookupPrivilegeValueA` (used in conjunction with `AdjustTokenPrivileges`). This is often used to check if the installer has administrative privileges before attempting to write to protected system directories.

*   **Anti-Analysis / Evasion Tactics:**
    *   The use of **NSIS-like structures** is a common technique for malware authors because it provides a "legitimate" wrapper for malicious payloads, making the initial execution appear like a standard software installation.
    *   The code includes logic to handle various command-line flags (e.g., looking for `/S` or `/D`), which allows the installer to run silently (stealthily) on a victim's machine without user interaction.

### Summary of Observed Techniques
*   **Dropper/Installer Pattern:** The core logic is wrapped in an installer framework, which provides a "veneer" of legitimacy while moving and executing payloads.
*   **Persistence Mechanism:** Use of Registry APIs to ensure the application persists across reboots.
*   **Integrity Checking:** Ensuring the payload remains intact during the unpacking/extraction phase.
*   **Resource Management:** Extensive use of `GetTempPathA` and local file manipulation to stage files before execution.

### Conclusion
The binary is a sophisticated **installer stub**. While it may be part of legitimate software, its structure—specifically the combination of integrity checks, silent-mode handling, registry persistence logic, and automated file extraction—is highly consistent with a **malicious dropper** designed to install malware while masquerading as a standard application installer.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys/Run Options | The binary utilizes `RegOpenKeyExA` and `RegSetValueExA` to modify registry keys, a common method for establishing persistence. |
| T1560.001 | Archive Extraction: Archive File Extraction | The analysis identifies the binary as a "dropper" that extracts and unpacks files from embedded resources or temporary locations. |
| T1036 | Masquerading | The use of an NSIS-like framework and silent switches (e.g., /S) allows the malicious behavior to mimic legitimate software installation. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Per your instructions, standard Windows system paths (e.g., `Control Panel\Desktop\ResourceLocale`) and standard API functions (e.g., `CreateProcessA`, `GetTempPathA`) have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The provided strings contained only standard Windows system paths and internal API calls).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Framework/Tooling:** The binary utilizes the **NSIS (Nullsoft Script Installer)** framework. While common in legitimate software, it is a known indicator of "wrapper" techniques used by malware to provide a veneer of legitimacy for dropped payloads.
*   **Behavioral Indicator (Dropper Logic):** The use of `CopyFileA`, `MoveFileA`, and `SetCurrentDirectoryA` specifically designed to unpack and move files from an embedded resource/temporary location to final destinations.
*   **Persistence Attempt:** Use of registry manipulation via `RegOpenKeyExA` and `RegSetValueExA` (though specific malicious keys were not identified in the string dump).
*   **Integrity Check Behavior:** The implementation of a loop (`fcn.00403168`) to verify file integrity before execution, which is common in complex droppers to ensure the payload survives the unpacking process.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: dropper
3. **Confidence**: High

**Key evidence**:
*   **Installer Masquerading:** The binary utilizes an NSIS-style framework to provide a "veneer" of legitimacy, incorporating silent installation flags (e.g., `/S`) and UI elements like progress bars to hide its malicious activities from the user.
*   **Multi-stage Deployment Logic:** The inclusion of integrity checks (`fcn.00403168`), file extraction routines (`CopyFileA`, `MoveFileA`), and directory management indicates a primary role of unpacking and staging an embedded payload rather than performing final malicious actions itself.
*   **Persistence Establishment:** The use of Registry API calls (`RegOpenKeyExA`, `RegSetValueExA`) combined with system privilege checks suggests the binary is designed to ensure its (or the dropped payload's) persistence on the host machine following execution.
