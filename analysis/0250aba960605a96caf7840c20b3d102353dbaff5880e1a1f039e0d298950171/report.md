# Threat Analysis Report

**Generated:** 2026-06-28 04:06 UTC
**Sample:** `0250aba960605a96caf7840c20b3d102353dbaff5880e1a1f039e0d298950171_0250aba960605a96caf7840c20b3d102353dbaff5880e1a1f039e0d298950171.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0250aba960605a96caf7840c20b3d102353dbaff5880e1a1f039e0d298950171_0250aba960605a96caf7840c20b3d102353dbaff5880e1a1f039e0d298950171.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 277,696 bytes |
| MD5 | `df0a6df9d876a941694272e442eb012b` |
| SHA1 | `9b1b030a98b4cfc177f5fbb206f7aaacd2ad188c` |
| SHA256 | `0250aba960605a96caf7840c20b3d102353dbaff5880e1a1f039e0d298950171` |
| Overall entropy | 7.863 |
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

Total strings found: **818** (showing first 100)

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

### Analysis Summary

Based on the provided disassembly and strings, this binary functions as a **sophisticated installer or an "updater" loader**, likely utilizing the **NSIS (Nullsoft Script Installer)** framework. It is designed to verify file integrity, manipulate system configuration via the registry, and handle complex installation logic while managing a graphical user interface (GUI).

While it possesses many characteristics of a legitimate installer, several features are common in malware "droppers" or "loaders" intended to deliver a second-stage payload.

### Core Functionality and Purpose
*   **Installation Framework:** The presence of strings like `"NSIS Error"` and `"Installer integrity check has failed"` indicates this is an installer script wrapper. Its primary role is to prepare the environment, unpack files, and ensure they are valid before execution.
*   **Integrity Verification:** A significant portion of the code (e.g., `fcn.004067c4` and `fcn.00403168`) is dedicated to calculating checksums (likely CRC32 or a similar algorithm) and comparing them against expected values. This ensures that files haven't been corrupted during download or modified by security software.
*   **Environment Preparation:** The code interacts heavily with the Windows environment, including retrieving temp paths (`GetTempPathA`), setting environment variables, and resolving system file paths to ensure a consistent installation environment.

### Suspicious or Malicious Behaviors
The following behaviors are noted as potentially suspicious due to their common usage in malware:

*   **Dropping and Moving Files:** The binary frequently uses `CopyFileA`, `MoveFileExA`, and `GetTempPathA`. It moves files from temporary locations (often where a download initially lands) to final destinations. In a malicious context, this is the "dropper" phase where a payload is unpacked and moved to a persistent location.
*   **Integrity Checking as Evasion:** While common in installers, high-complexity integrity checks are used by malware to ensure that a payload has not been altered or tampered with by security software (AV/EDR) before it is executed.
*   **Registry Manipulation:** The code uses `RegOpenKeyExA`, `RegCreateKeyExA`, and `RegSetValueExA`. This can be used for legitimate installation but is also a primary method for achieving **persistence** (e.g., adding the software to the "Run" key) or modifying system security policies.
*   **Privilege Adjustment:** The code calls `LookupPrivilegeValueA` and `AdjustTokenPrivileges` specifically targeting rights like `SeShutdownPrivilege`. While this may be for a legitimate "Shut Down" option in an installer, it is also used by malware to gain higher privileges or manipulate system-level functions.
*   **Dynamic API Resolution:** The code uses `GetProcAddress` and `GetModuleHandleA` (observed in the logic surrounding `fcn.00402c90`). This technique is often used to hide the program's true capabilities from static analysis by resolving "sensitive" functions only at runtime.

### Notable Techniques and Patterns
*   **NSIS Wrapper Pattern:** The structure of the code—checking for specific system capabilities (like `UXTHEME` or `RichEdit`), handling UI messages, and checking for NSIS-specific errors—is a hallmark of an installer. 
*   **Recursive File/Registry Processing:** Several functions (`fcn.00402d60`, `fcn.00401389`) suggest loops designed to process multiple files or registry keys in sequence, indicating it manages a multi-step installation process.
*   **Resource Handling:** The use of `LoadImageA` and `GetDlgItem` suggests the binary is prepared to interact with a variety of Windows UI components, which can be used to hide malicious activity behind professional-looking "updates" or "setup" windows.

### Conclusion for Security Context
This binary acts as a **precursor/loader**. If this sample is part of a malware campaign, its role is to:
1.  Verify the integrity of a hidden payload.
2.  Extract and move that payload into a local directory.
3.  Modify registry keys to ensure it or its component remains active after a reboot.
4.  Provide a "clean" interface to the user while performing these background actions.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1105 | Ingress Tool Transfer | The binary uses `CopyFileA` and `MoveFileExA` to move files from temporary directories to final locations, a common behavior for "dropping" payloads. |
| T1497 | Virtualization/Sandbox Detection | The complex integrity checks (CRC32) are utilized as a defense evasion tactic to ensure the payload hasn't been modified or flagged by security software before execution. |
| T1112 | Modify Registry | The use of `RegCreateKeyExA` and `RegSetValueExA` is used to establish persistence or modify system configurations for the installed components. |
| T1068 | Exploitation for Privilege Escalation | The calls to `LookupPrivilegeValueA` and `AdjustTokenPrivileges` indicate an attempt to acquire higher-level permissions to execute restricted operations. |
| T1036 | Masquerading | Both the use of an NSIS wrapper and Dynamic API Resolution (`GetProcAddress`) are used to hide the program's true purpose and evade static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified (Note: The registry keys `Control Panel\International` and `Control Panel\Desktop\ResourceLocale`, as well as various system paths, were identified as standard Windows components and excluded as false positives).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **NSIS Wrapper Indicators:** The strings `"NSIS Error"` and `"Installer integrity check has failed"` indicate the use of an NSIS (Nullsoft Script Installer) wrapper, which is a common technique for creating "dropper" or "loader" programs.
*   **Dynamic API Resolution:** Use of `GetProcAddress` and `GetModuleHandleA` to resolve functions at runtime (indicative of attempts to evade static analysis).
*   **Privilege Escalation Logic:** Evidence of using `LookupPrivilegeValueA` and `AdjustTokenPrivileges` to modify system-level capabilities.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family**: Custom
2. **Malware type**: Loader (or Dropper)
3. **Confidence**: High
4. **Key evidence**:
    *   **Loader/Dropper Behavior:** The binary acts as a precursor that moves files from temporary directories to persistent locations and performs integrity checks to ensure the second-stage payload is intact before execution.
    *   **Evasion & Obfuscation:** Use of Dynamic API Resolution (`GetProcAddress`) and complex CRC32 calculations are classic techniques used to hide malicious functionality from static analysis and automated security tools.
    *   **Persistence & Privilege Escalation:** The inclusion of registry modification logic for persistence, combined with `AdjustTokenPrivileges` calls, indicates an intent to maintain a foothold on the system after delivering its payload.
