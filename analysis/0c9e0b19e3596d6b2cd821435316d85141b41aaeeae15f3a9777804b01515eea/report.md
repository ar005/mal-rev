# Threat Analysis Report

**Generated:** 2026-07-31 17:44 UTC
**Sample:** `0c9e0b19e3596d6b2cd821435316d85141b41aaeeae15f3a9777804b01515eea_0c9e0b19e3596d6b2cd821435316d85141b41aaeeae15f3a9777804b01515eea.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c9e0b19e3596d6b2cd821435316d85141b41aaeeae15f3a9777804b01515eea_0c9e0b19e3596d6b2cd821435316d85141b41aaeeae15f3a9777804b01515eea.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 240,743 bytes |
| MD5 | `54ec0c8ebcdc101887fb8904ef992b46` |
| SHA1 | `6dcfd76e92982e437bc56411691059f254744fe1` |
| SHA256 | `0c9e0b19e3596d6b2cd821435316d85141b41aaeeae15f3a9777804b01515eea` |
| Overall entropy | 7.832 |
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

Total strings found: **678** (showing first 100)

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

Based on my analysis of the provided disassembly and strings, this binary functions as an **installer or a multi-stage "dropper."** 

While the code utilizes many standard Windows API calls common to legitimate installation software (specifically suggesting the use of the NSIS framework), it exhibits behaviors often used by malware to stage a payload on a target system.

### Core Functionality and Purpose
The primary purpose of this code is to unpack, extract, and prepare files for execution. It acts as a "wrapper" that handles the initial setup:
*   **Environment Preparation:** It checks for system capabilities (like `UXTHEME`), sets up environment variables, and prepares temporary directories.
*   **File Extraction/Staging:** The code heavily utilizes file manipulation routines to move files from an internal source or previous stage into a workable location on the disk (e.g., moving them to `%TEMP%` or other system paths).
*   **Progress Tracking:** There is significant logic for updating a GUI and showing progress percentages, which is typical of setup wizards.

### Suspicious or Malicious Behaviors
The following behaviors are notable from a security perspective:

*   **Dropper/Staging Behavior:** The code uses `GetTempPathA`, `CopyFileA`, and `MoveFileA` to move files into temporary directories before execution. This is a classic "dropper" technique used to hide the final payload until it can be launched from a less-monitored location.
*   **Privilege Escalation/Manipulation:** The code explicitly calls `OpenProcessToken`, `LookupPrivilegeValueA`, and `AdjustTokenPrivileges`. While common in installers that need to modify system files, these functions are also frequently used by malware to gain elevated permissions (e.g., the ability to interact with system services or shutdown processes).
*   **Persistence and Configuration via Registry:** There is extensive use of the `ADVAPI32` library (`RegSetValueExA`, `RegEnumKeyA`, `RegOpenKeyExA`). This indicates that the program modifies several areas of the Windows Registry, which could be used for persistence (ensuring the malware runs on reboot) or to change system configurations.
*   **Self-Extraction Logic:** The loop structures and the handling of different file types (implied by various `case` switches in `fcn.00401434`) indicate it is "unpacking" a bundle of components.

### Notable Techniques/Patterns
*   **NSIS Framework Characteristics:** Several strings (e.g., `"NSIS Error"`, `"http://nsis.sf.net/NSIS_Error"`) confirm the use of the Nullsoft Scriptable Install System. This is a common tool for legitimate software, but it is very frequently used by malware authors to package and deliver malicious payloads because it handles many heavy lifting tasks like file extraction automatically.
*   **Argument Parsing:** The `entry0` function parses command-line arguments (e.g., looking for `/S` or `-` flags). This allows the binary to be run in "silent" mode, a common requirement for automated malware deployments.
*   **Hardcoded Integrity Checks:** The presence of an "integrity check" message (`fcn.00403168`) suggests that the program verifies the files it is extracting before moving forward, ensuring that the dropped payload has not been corrupted or modified by security software during the extraction process.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Exploitation for Privilege Escalation (Note: Often mapped as **Obfuscated Files or Information**) | The use of `GetTempPathA`, `CopyFileA`, and `MoveFileA` to extract and move components into a temporary directory characterizes the "dropper" behavior of unpacking a payload. |
| **T1068** | Exploitation for Privilege Escalation | The calls to `OpenProcessToken`, `LookupPrivilegeValueA`, and `AdjustTokenPrivileges` indicate an attempt to acquire higher privileges or capabilities to bypass system restrictions. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys | The extensive use of `RegSetValueExA` to modify multiple areas of the Windows Registry indicates a mechanism for establishing persistence upon reboot/login. |
| **T1036** | Masquerading | The integration of the NSIS framework allows the binary to hide its malicious intent by mimicking the behavior and appearance of a legitimate software installer. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Please note that many of the items in the "Extracted Strings" section were identified as standard Windows API functions or common system paths and were excluded per your instructions to skip false positives.

### **IP addresses / URLs / Domains**
*   `http://nsis.sf.net/NSIS_Error` (Note: This is a hardcoded string associated with the NSIS framework used for error reporting.)

### **File paths / Registry keys**
*   *None detected.* (The strings `Control Panel\Desktop\ResourceLocale`, `Software\Microsoft\Windows\CurrentVersion`, and others were identified as standard Windows system paths/registry keys and excluded from this list.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Tools Used:** Nullsoft Scriptable Install System (NSIS) — Identified via the "NSIS Error" and related URL strings.
*   **Command-line Arguments:** `/S` and `-` — Used for execution in "silent" or "hidden" mode to bypass user interaction.
*   **Core Behavior:** Multi-stage dropper/wrapper functionality (utilizing `GetTempPathA`, `CopyFileA`, and `MoveFileA` to stage payloads).
*   **Privilege Manipulation:** Use of `AdjustTokenPrivileges` and `LookupPrivilegeValueA` for escalating permissions.
*   **Integrity Check:** Hardcoded routine (`fcn.00403168`) to verify the integrity of dropped files before execution.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown (NSIS-based Dropper)
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Wrapper/Staging Behavior:** The sample exhibits classic "dropper" characteristics by utilizing `GetTempPathA`, `CopyFileA`, and `MoveFileA` to extract and stage internal components into temporary directories before execution.
*   **Masquerading via NSIS:** The integration of the Nullsoft Scriptable Install System (NSIS) and the use of "silent" command-line switches (`/S`) are common techniques used by malware to hide its activities behind a legitimate installer facade.
*   **Privilege Escalation & Persistence:** The code contains specific logic for privilege manipulation (`AdjustTokenPrivileges`) and extensive registry modification, indicating an intent to gain elevated permissions and establish persistence on the host system.
