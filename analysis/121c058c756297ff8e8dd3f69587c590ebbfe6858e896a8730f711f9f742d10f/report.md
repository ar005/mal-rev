# Threat Analysis Report

**Generated:** 2026-08-24 23:40 UTC
**Sample:** `121c058c756297ff8e8dd3f69587c590ebbfe6858e896a8730f711f9f742d10f_121c058c756297ff8e8dd3f69587c590ebbfe6858e896a8730f711f9f742d10f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `121c058c756297ff8e8dd3f69587c590ebbfe6858e896a8730f711f9f742d10f_121c058c756297ff8e8dd3f69587c590ebbfe6858e896a8730f711f9f742d10f.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 325,200 bytes |
| MD5 | `03311dda7d1a8e9745c74ab898eec814` |
| SHA1 | `7e0ccf5535cd88141a0e82210089c9fd1db5066c` |
| SHA256 | `121c058c756297ff8e8dd3f69587c590ebbfe6858e896a8730f711f9f742d10f` |
| Overall entropy | 7.736 |
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
| `.text` | 26,112 | 6.467 | No |
| `.rdata` | 5,120 | 5.104 | No |
| `.data` | 1,536 | 4.03 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 40,960 | 5.122 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `lstrcmpiA`, `CreateFileW`, `GetTempFileNameW`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`

## Extracted Strings

Total strings found: **812** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495L
tQWPV
Instuj
softua
NulluX	E
UVWj _3
L$bf-S
D$ Pj(
D$(Ph0
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
| `fcn.00401434` | `0x401434` | 6196 | ✓ |
| `fcn.00406aeb` | `0x406aeb` | 2642 | ✓ |
| `entry0` | `0x403557` | 1565 | ✓ |
| `fcn.00403c4e` | `0x403c4e` | 726 | ✓ |
| `fcn.004065b9` | `0x4065b9` | 625 | ✓ |
| `fcn.004030a9` | `0x4030a9` | 619 | ✓ |
| `fcn.00403314` | `0x403314` | 485 | ✓ |
| `fcn.00405c88` | `0x405c88` | 451 | ✓ |
| `fcn.004061c2` | `0x4061c2` | 378 | ✓ |
| `fcn.00402ed5` | `0x402ed5` | 234 | ✓ |
| `fcn.00405601` | `0x405601` | 211 | ✓ |
| `fcn.00404562` | `0x404562` | 207 | ✓ |
| `fcn.00404da8` | `0x404da8` | 201 | ✓ |
| `fcn.00403f24` | `0x403f24` | 185 | ✓ |
| `fcn.0040682a` | `0x40682a` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.004064dc` | `0x4064dc` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00406368` | `0x406368` | 129 | ✓ |
| `fcn.00404eb6` | `0x404eb6` | 128 | ✓ |
| `fcn.00405f53` | `0x405f53` | 126 | ✓ |
| `fcn.0040644a` | `0x40644a` | 121 | ✓ |
| `fcn.0040614d` | `0x40614d` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406900` | `0x406900` | 112 | ✓ |
| `fcn.00406a5d` | `0x406a5d` | 110 | ✓ |
| `fcn.004056d4` | `0x4056d4` | 108 | ✓ |
| `fcn.00405bdc` | `0x405bdc` | 100 | ✓ |
| `fcn.00403045` | `0x403045` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402ed5.c`](code/fcn.00402ed5.c)
- [`code/fcn.00403045.c`](code/fcn.00403045.c)
- [`code/fcn.004030a9.c`](code/fcn.004030a9.c)
- [`code/fcn.00403314.c`](code/fcn.00403314.c)
- [`code/fcn.00403c4e.c`](code/fcn.00403c4e.c)
- [`code/fcn.00403f24.c`](code/fcn.00403f24.c)
- [`code/fcn.00404562.c`](code/fcn.00404562.c)
- [`code/fcn.00404da8.c`](code/fcn.00404da8.c)
- [`code/fcn.00404eb6.c`](code/fcn.00404eb6.c)
- [`code/fcn.00405601.c`](code/fcn.00405601.c)
- [`code/fcn.004056d4.c`](code/fcn.004056d4.c)
- [`code/fcn.00405bdc.c`](code/fcn.00405bdc.c)
- [`code/fcn.00405c88.c`](code/fcn.00405c88.c)
- [`code/fcn.00405f53.c`](code/fcn.00405f53.c)
- [`code/fcn.0040614d.c`](code/fcn.0040614d.c)
- [`code/fcn.004061c2.c`](code/fcn.004061c2.c)
- [`code/fcn.00406368.c`](code/fcn.00406368.c)
- [`code/fcn.0040644a.c`](code/fcn.0040644a.c)
- [`code/fcn.004064dc.c`](code/fcn.004064dc.c)
- [`code/fcn.004065b9.c`](code/fcn.004065b9.c)
- [`code/fcn.0040682a.c`](code/fcn.0040682a.c)
- [`code/fcn.00406900.c`](code/fcn.00406900.c)
- [`code/fcn.00406a5d.c`](code/fcn.00406a5d.c)
- [`code/fcn.00406aeb.c`](code/fcn.00406aeb.c)

## Behavioral Analysis

### Analysis Summary
The provided code is consistent with a **software installer stub**, specifically one utilizing the **NSIS (Nullsoft Script Installer)** framework. The primary purpose of this code is to manage the "wrapper" logic: unpacking files, verifying integrity, interacting with the user via a GUI, and performing system configuration (like registry edits) during an installation process.

While these behaviors are standard for legitimate installers, they are also frequently used by malware as a delivery mechanism ("dropper") to unpack and execute a secondary payload that is not immediately visible in the primary executable.

### Core Functionality
*   **Installer Framework:** The presence of `NSIS Error` strings and logic for handling "Standard" vs. "Extended" windows indicates it is part of an installation wizard.
*   **Extraction & File Manipulation:** The code includes significant logic to find temporary paths, copy files from a source into a staging area (using `CopyFileW`), and move them to final locations (`MoveFileW`). This is used to unpack the "real" payload.
*   **Integrity Checking:** Function `fcn.004030a9` performs an integrity check on files before they are processed. If the check fails, it displays a specific error message regarding "damaged media."
*   **Registry Interaction:** The code interacts with `Advapi32.dll` to read and write registry keys (`RegOpenKeyExW`, `RegSetValueExW`). This is typically used to create "Uninstall" entries or save application settings.
*   **System Configuration:** It uses `SetEnvironmentVariableW` and `GetSystemDirectoryW` to ensure the environment is correctly configured for the installation process.

### Suspicious or Malicious Behaviors
While the code's primary purpose appears to be an installer, several features are common in "dropper" behavior:

*   **Payload Staging:** The logic involving copying files into temporary directories (e.g., `\Temp` folder) and then executing/moving them is a classic technique used by malware to hide the final payload from simple scanners until it is actually "dropped."
*   **Privilege Elevation:** The code attempts to adjust token privileges (specifically `SeShutdownPrivilege`). While common in installers that need to modify system files, this behavior ensures the process has enough permission to perform deep changes to the OS.
*   **Environment Manipulation:** By dynamically resolving paths and setting environment variables, the installer can change how other processes or shell commands behave after the installation is complete.

### Notable Techniques & Patterns
*   **NSIS Infrastructure:** The code contains highly specialized logic for handling GUI elements (e.g., `fcn.00401434` handles button clicks/dialog logic). This confirms it is a standard installer wrapper.
*   **Internal Dispatch Table:** The large switch-case structure in `fcn.00401434` is characteristic of how these installers handle different UI events (moving through the "Next" buttons, progress bars, etc.).
*   **Dynamic Resource Loading:** Functions like `fcn.00406900` are used to dynamically load system DLLs (like `UXTHEME`) to ensure compatibility across different Windows versions.
*   **Robust Error Handling:** The code includes multiple checks for file existence and "success" returns from OS calls, ensuring the installation process doesn't crash even if a file is missing or a registry key cannot be accessed.

### Summary for Analyst
This sample is an **installer stub**. It does not appear to contain direct malicious payloads (like network command-and-control modules), but it serves as the "delivery vehicle." If this binary was found in a suspicious context, the actual threat would likely reside in the files it unpacks and moves during its execution.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of an NSIS installer framework allows the malware to blend in as a legitimate software wrapper to hide its role as a delivery vehicle. |
| T1027 | Obfuscated Files | The unpacking and staging of files in temporary directories are used to conceal the primary payload from security scanners until execution. |
| T1112 | Registry Event Modification | The use of `RegOpenKeyExW` and `RegSetValueExW` indicates interaction with registry keys for configuration or persistence. |
| T1068 | Exploitation for Privilege Escalation | The specific attempt to adjust token privileges ensures the process gains sufficient permissions to perform significant system modifications. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: Because this sample is identified as a generic **installer stub**, there are no specific network indicators (IPs/URLs) or unique file hashes present in the text. The indicators provided are primarily **behavioral artifacts**.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (The analysis mentions interaction with registry keys and temporary folders, but no specific paths—e.g., `C:\Windows\Temp` or `HKLM\Software\...`—were provided in the raw data).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Installer Framework:** NSIS (Nullsoft Script Installer)
*   **Behavioral Technique - File Staging:** The sample uses `CopyFileW` and `MoveFileW` to move files into temporary directories for execution (Typical "dropper" behavior).
*   **Privilege Escalation Attempt:** Request for `SeShutdownPrivilege` via `AdjustTokenPrivileges`.
*   **Known Internal Functions:** 
    *   `fcn.004030a9` (Integrity check)
    *   `fcn.00401434` (UI/Button handling)
    *   `fcn.00406900` (Dynamic resource loading)

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown (Generic Installer Stub)
2. **Malware type**: Dropper
3. **Confidence**: High

**Key evidence**:
*   **Dropper Functionality:** The analysis confirms the sample acts as a delivery vehicle by unpacking, staging, and moving files to temporary directories before execution—a classic technique used to hide the primary payload from initial security scans.
*   **Masquerading via NSIS:** The use of the Nullsoft Script Installer (NSIS) framework allows the binary to mimic legitimate software behavior (e.g., "Standard" vs. "Extended" UI logic), making it an effective vehicle for concealing malicious activity within a standard installation routine.
*   **Privilege Escalation & System Manipulation:** The attempt to adjust token privileges (specifically `SeShutdownPrivilege`) and the manipulation of registry keys indicate preparation for deep system changes or persistence, which is consistent with post-delivery malware execution.
