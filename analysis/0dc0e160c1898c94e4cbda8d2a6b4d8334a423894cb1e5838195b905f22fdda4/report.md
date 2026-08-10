# Threat Analysis Report

**Generated:** 2026-08-10 15:27 UTC
**Sample:** `0dc0e160c1898c94e4cbda8d2a6b4d8334a423894cb1e5838195b905f22fdda4_0dc0e160c1898c94e4cbda8d2a6b4d8334a423894cb1e5838195b905f22fdda4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0dc0e160c1898c94e4cbda8d2a6b4d8334a423894cb1e5838195b905f22fdda4_0dc0e160c1898c94e4cbda8d2a6b4d8334a423894cb1e5838195b905f22fdda4.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 65,690,592 bytes |
| MD5 | `67c37850e3e6a5863d305206fc854326` |
| SHA1 | `9c4301f8965250b5f3aedaef58aecd7d190d3ab4` |
| SHA256 | `0dc0e160c1898c94e4cbda8d2a6b4d8334a423894cb1e5838195b905f22fdda4` |
| Overall entropy | 8.0 |
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
| `.rsrc` | 17,408 | 2.984 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `lstrcmpiA`, `CreateFileW`, `GetTempFileNameW`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`

## Extracted Strings

Total strings found: **141595** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's behavior:

### Core Functionality
The binary is an **installer application**, specifically utilizing the **NSIS (Nullsoft Script Installer)** framework. Its primary purpose is to guide a user through a setup process, manage file extractions, and ensure that the files being installed are valid. 

Key standard installer behaviors include:
*   **Installer Logic:** The code contains large switch-case blocks (e.g., `fcn.00401434`) used to interpret and execute a series of commands (likely from an `.nsi` script).
*   **UI Management:** Extensive use of `USER32.dll` and `GDI32.dll` for creating dialogs, rendering text, and handling button/window interactions.
*   **File Manipulation:** The code frequently uses `CopyFileW`, `MoveFileW`, and `GetTempPathW` to move installer components into their final destinations or temporary directories during the installation process.
*   **Resource Handling:** It utilizes standard Windows shell features (via `SHELL32.dll`) to handle file paths and icons.

### Suspicious or Malicious Behaviors
While this specific code is characteristic of a legitimate installer, several behaviors are common in "droppers" or "wrappers" used by malware to deliver a payload:

*   **Integrity Checks:** Function `fcn.00403c4e` contains an explicit integrity check. It validates the files being handled against expected values. While standard for installers, this same logic is frequently used by malware to ensure its "payload" hasn't been modified or replaced by security software during the unpacking process.
*   **Temporary Directory Usage:** The code heavily utilizes `%TEMP%` folders (e.g., `fcn.00403045`, `fcn.004065b9`). Malware often uses these locations to stage and execute malicious payloads because they typically have relaxed permissions.
*   **System Information Gathering:** The binary checks system details using `GetVersionExW` and queries environment variables. While common in installers, this is also a prerequisite for "anti-VM" or "anti-sandbox" checks used by malware to determine if it's being analyzed.
*   **Automatic Execution/Unpacking:** The logic involving `CopyFileW` followed by internal calls suggests that the binary acts as a "loader." It extracts a second stage and then executes it, which is a common technique for evading static analysis.

### Notable Techniques or Patterns
*   **NSIS Framework Signatures:** The presence of strings like `nsis.sf.net`, `NSIS Error`, and specific error messages confirms the use of the NSIS engine. 
*   **Firmware/File Verification:** The logic in `fcn.00403c4e` compares file sizes and contents, which is a standard way to ensure an installer isn't "corrupt," but it also masks the fact that it is validating its own internal components before launching them.
*   **Shell Integration:** The use of `SHGetFileInfoW` and `lGetPathName` suggests the program interacts heavily with the Windows Explorer environment to resolve paths for files it intends to move or execute.

### Summary Conclusion
This binary is a **standard NSIS installer**. However, because such installers are commonly used as "wrappers" by threat actors to install malware (by wrapping the malicious payload in a legitimate-looking setup UI), it should be treated as a potential **dropper** until the specific files it extracts and executes are identified.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtualization/Sandbox Detection | The use of `GetVersionExW` and environment variable queries are identified as methods to detect if the binary is running in a virtualized or sandbox environment. |
| T1036 | Masquerading | The utilization of the NSIS framework allows the malicious payload to be hidden within a legitimate-looking installer interface. |
| T1027 | Obfuscated Files or Information | The "wrapping" of the payload and the internal unpacking logic are used to conceal the true nature of the secondary stage from static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `nsis.sf.net` (Note: Identified as an NSIS framework component; while a legitimate domain for the installer tool, it is the only network-related string identified.)

**File paths / Registry keys**
*   *None detected.* (The strings provided contain various Windows API functions for registry interaction—e.g., `RegOpenKeyExW`, `RegSetValueExW`—but no specific malicious hardcoded paths or registry keys were identified.)

**Mutex names / Named pipes**
*   *None detected.*

**Hashes**
*   *None provided in the source text.*

**Other artifacts**
*   **Framework Identification:** NSIS (Nullsoft Script Installer) signature detected.
*   **Execution Patterns:** The binary exhibits "Dropper" or "Wrapper" behavior, specifically utilizing `%TEMP%` directories to stage and execute additional components.
*   **Integrity Checks:** Function `fcn.00403c4e` performs internal integrity/validation checks on its payload files.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: Medium

4. **Key evidence**:
* **Wrapper Behavior:** The binary utilizes the NSIS (Nullsoft Script Installer) framework, which is a common technique for masquerading malicious payloads behind legitimate-looking installation interfaces (T1036).
* **Staging and Execution:** The analysis identifies classic "dropper" behaviors, specifically the use of `%TEMP%` directories to stage files and the inclusion of integrity checks (fcn.00403c4e) to ensure payloads are not altered before execution.
* **Evasion Tactics:** The presence of `GetVersionExW` calls and environment variable queries suggests anti-analysis capabilities designed to detect if the binary is running in a virtualized or sandbox environment (T1497).
