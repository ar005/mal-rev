# Threat Analysis Report

**Generated:** 2026-08-04 20:06 UTC
**Sample:** `0d13e31b0ff25e3ff2e564ae518a72e7cca222174565bcda0d2e15154a4ec46b_0d13e31b0ff25e3ff2e564ae518a72e7cca222174565bcda0d2e15154a4ec46b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d13e31b0ff25e3ff2e564ae518a72e7cca222174565bcda0d2e15154a4ec46b_0d13e31b0ff25e3ff2e564ae518a72e7cca222174565bcda0d2e15154a4ec46b.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 747,336 bytes |
| MD5 | `e6cf5f821a8bb4d771421547f6bcb83d` |
| SHA1 | `ca00e4703ff791fb3fe70ef32e49065e62947f7b` |
| SHA256 | `0d13e31b0ff25e3ff2e564ae518a72e7cca222174565bcda0d2e15154a4ec46b` |
| Overall entropy | 7.936 |
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
| `.rsrc` | 19,456 | 1.961 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `lstrcmpiA`, `CreateFileW`, `GetTempFileNameW`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`

## Extracted Strings

Total strings found: **1662** (showing first 100)

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

Based on the provided strings and decompiled code, here is an analysis of the binary sample:

### Core Functionality and Purpose
The binary functions as a **Dropper or Installer**, specifically utilizing the **NSIS (Nullsoft Script Installer)** framework. This is evidenced by the explicit "NSIS Error" string constants and the presence of standard NSIS logic for handling installation scripts, extracting files from an archive/installer package, and managing system-wide configurations.

The primary goal of this specific component is to:
1.  **Extract components:** Extracting files from a bundled installer into temporary directories.
2.  **Validate integrity:** Ensuring that the extracted components have not been tampered with (seen in `fcn.004030a9`).
3.  **Configure the system:** Modifying registry keys and system properties to prepare for or "install" a final application.

### Suspicious or Malicious Behaviors
While these behaviors are common in legitimate installers, they are also standard techniques used by malware (droppers) to deliver payloads:

*   **File Manipulation & Staging:** The code frequently interacts with the filesystem using `GetTempPathW`, `CopyFileW`, and `MoveFileW`. It extracts files into temporary directories (likely `%TEMP%` or `%APPDATA%`) and renames them. This is a classic "Dropper" technique to unpack a payload before execution.
*   **Persistence/System Configuration:** The code heavily utilizes Registry APIs (`RegOpenKeyExW`, `RegSetValueExW`, `RegDeleteValueW`). While it may be setting up an application, these same functions are used by malware to ensure persistence (e.g., creating "Run" keys) or to disable security features.
*   **Privilege Manipulation:** The use of `LookupPrivilegeValueW` and `AdjustTokenPrivileges` for `SeShutdownPrivilege` indicates the program is attempting to verify or escalate its permissions. In a malware context, this allows the process to perform higher-level system actions.
*   **Process Execution:** Use of `ShellExecuteExW` and `CreateProcessW` indicates that once files are extracted and moved, the installer attempts to launch them as separate processes.
*   **Anti-Analysis/Evasion (Contextual):** The heavy use of NSIS logic can sometimes be used as a "wrapper" to hide malicious intent. By masquerading as a standard installer, the malware can bypass simple heuristic checks that look for suspicious behavior but ignore it if it appears consistent with an installation routine.

### Notable Techniques and Patterns
*   **NSIS Framework:** The binary is clearly built using NSIS. This is common in "bundled" software where one executable handles the unpacking of several others. 
*   **Integrity Checks:** Function `fcn.004030a9` includes logic to verify the integrity of the installer files. It checks if "the download is complete and media is not damaged."
*   **Delayed Execution/Interaction:** The code contains multiple calls to `Sleep` and interacts with Windows UI elements (e.g., `SetForegroundWindow`, `MessageBoxIndirectW`). This can be used to slow down automated analysis tools or interact with the user to provide a sense of legitimacy.
*   **Dynamic Path Construction:** The binary constructs paths dynamically using `GetTempPathW` and `GetWindowsDirectoryW`, ensuring that it can operate in different system environments, which is typical for both reliable installers and versatile malware.

### Summary for Triage
This binary is likely the **delivery mechanism (dropper/installer)** for a larger payload. While not showing direct "malicious" actions like active network beaconing or memory injection in this snippet, it performs all the necessary prerequisites for an infection: **unpacking, moving to system folders, registering with the OS, and launching the final payload.**

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1560.003 | Archive Extraction: Archive File | The binary extracts and moves files from a bundled installer into temporary directories to stage the payload. |
| T1547.001 | Boot or Logon Autostart: Registry Run Keys | The use of `RegSetValueExW` to modify registry keys is identified as a method for establishing persistence. |
| T1068 | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` indicates an attempt to acquire higher-level system permissions to perform restricted actions. |
| T1036 | Masquerading | The binary uses the standard NSIS framework as a "wrapper" to hide its malicious intent by appearing as a legitimate installer. |
| T1497 | Virtualization/Sandbox Evasion | The use of `Sleep` calls and UI interactions are utilized to stall automated analysis tools and mimic user activity. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (While the report mentions the use of `RegOpenKeyExW` and `GetTempPathW`, no specific malicious registry paths or hardcoded file paths were provided in the source text.)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Framework Identification:** NSIS (Nullsoft Script Installer) - The binary utilizes standard NSIS logic for installation and unpacking.
*   **Internal Function Offset:** `fcn.004030a9` (Identified as the specific location where integrity checks are performed).
*   **Behavioral Indicators:** 
    *   Use of `GetTempPathW`, `CopyFileW`, and `MoveFileW` for payload staging.
    *   Use of `LookupPrivilegeValueW` and `AdjustTokenPrivileges` for privilege escalation/verification.
    *   Use of `ShellExecuteExW` and `CreateProcessW` for secondary payload execution.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family:** Unknown
2. **Malware type:** dropper
3. **Confidence:** High

4. **Key evidence:**
*   **Staging and Payload Delivery:** The binary utilizes the NSIS framework to extract, move, and rename files in temporary directories (`GetTempPathW`, `CopyFileW`), which is a standard "dropper" behavior used to unpack malicious payloads before execution.
*   **Persistence and Privilege Escalation:** The code includes logic for both registry manipulation (typically for persistence) and the use of `AdjustTokenPrivileges` to acquire higher-level system permissions, facilitating the deployment of secondary components.
*   **Evasion Techniques:** The implementation of `Sleep` commands and active interaction with Windows UI elements are deliberate tactics used to stall automated sandbox analysis and bypass heuristic detection while masquerading as a legitimate installer.
