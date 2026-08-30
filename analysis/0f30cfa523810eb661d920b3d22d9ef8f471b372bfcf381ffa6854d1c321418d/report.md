# Threat Analysis Report

**Generated:** 2026-08-15 20:00 UTC
**Sample:** `0f30cfa523810eb661d920b3d22d9ef8f471b372bfcf381ffa6854d1c321418d_0f30cfa523810eb661d920b3d22d9ef8f471b372bfcf381ffa6854d1c321418d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f30cfa523810eb661d920b3d22d9ef8f471b372bfcf381ffa6854d1c321418d_0f30cfa523810eb661d920b3d22d9ef8f471b372bfcf381ffa6854d1c321418d.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 81,882,808 bytes |
| MD5 | `4769843079dcf2b56af56882ac8763f5` |
| SHA1 | `7a5447a4393a7c33b21288b9c034ad31e9329919` |
| SHA256 | `0f30cfa523810eb661d920b3d22d9ef8f471b372bfcf381ffa6854d1c321418d` |
| Overall entropy | 7.998 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1632607007 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,624 | 6.417 | No |
| `.rdata` | 5,120 | 5.141 | No |
| `.data` | 1,536 | 4.111 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 424,960 | 1.695 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `SetFileSecurityW`, `RegOpenKeyExW`, `RegEnumValueW`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHFileOperationW`, `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `ShellExecuteExW`, `SHGetFileInfoW`
**ole32.dll**: `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `GetClientRect`, `EndPaint`, `DrawTextW`, `IsWindowEnabled`, `DispatchMessageW`, `wsprintfA`, `CharNextA`, `CharPrevW`, `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `GetSystemMetrics`, `FillRect`, `AppendMenuW`, `TrackPopupMenu`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectW`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetModuleHandleA`, `GetProcAddress`, `GetSystemDirectoryW`, `lstrcatW`, `Sleep`, `lstrcpyA`, `WriteFile`, `GetTempFileNameW`, `lstrcmpiA`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `GetLastError`

## Extracted Strings

Total strings found: **176233** (showing first 100)

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
SVWj _3
tVj%SSS
f9=H7B
D$$+D$
D$,+D$$P
u9=87B
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
EndDialog
ScreenToClient
GetWindowRect
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 6152 | ✓ |
| `fcn.00406bb0` | `0x406bb0` | 2642 | ✓ |
| `entry0` | `0x403640` | 1509 | ✓ |
| `fcn.00403d17` | `0x403d17` | 726 | ✓ |
| `fcn.004030d0` | `0x4030d0` | 673 | ✓ |
| `fcn.004066a5` | `0x4066a5` | 586 | ✓ |
| `fcn.00405d74` | `0x405d74` | 451 | ✓ |
| `fcn.004062ae` | `0x4062ae` | 378 | ✓ |
| `fcn.00403479` | `0x403479` | 361 | ✓ |
| `fcn.00403371` | `0x403371` | 264 | ✓ |
| `fcn.00402ea9` | `0x402ea9` | 234 | ✓ |
| `fcn.004056ca` | `0x4056ca` | 211 | ✓ |
| `fcn.0040462b` | `0x40462b` | 207 | ✓ |
| `fcn.00404e71` | `0x404e71` | 201 | ✓ |
| `fcn.00403fed` | `0x403fed` | 185 | ✓ |
| `fcn.004068ef` | `0x4068ef` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040302e` | `0x40302e` | 162 | ✓ |
| `fcn.004065c8` | `0x4065c8` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00406454` | `0x406454` | 129 | ✓ |
| `fcn.00404f7f` | `0x404f7f` | 128 | ✓ |
| `fcn.0040603f` | `0x40603f` | 126 | ✓ |
| `fcn.00405b99` | `0x405b99` | 125 | ✓ |
| `fcn.00406536` | `0x406536` | 121 | ✓ |
| `fcn.00406239` | `0x406239` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004069c5` | `0x4069c5` | 112 | ✓ |
| `fcn.00406b22` | `0x406b22` | 110 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402ea9.c`](code/fcn.00402ea9.c)
- [`code/fcn.0040302e.c`](code/fcn.0040302e.c)
- [`code/fcn.004030d0.c`](code/fcn.004030d0.c)
- [`code/fcn.00403371.c`](code/fcn.00403371.c)
- [`code/fcn.00403479.c`](code/fcn.00403479.c)
- [`code/fcn.00403d17.c`](code/fcn.00403d17.c)
- [`code/fcn.00403fed.c`](code/fcn.00403fed.c)
- [`code/fcn.0040462b.c`](code/fcn.0040462b.c)
- [`code/fcn.00404e71.c`](code/fcn.00404e71.c)
- [`code/fcn.00404f7f.c`](code/fcn.00404f7f.c)
- [`code/fcn.004056ca.c`](code/fcn.004056ca.c)
- [`code/fcn.00405b99.c`](code/fcn.00405b99.c)
- [`code/fcn.00405d74.c`](code/fcn.00405d74.c)
- [`code/fcn.0040603f.c`](code/fcn.0040603f.c)
- [`code/fcn.00406239.c`](code/fcn.00406239.c)
- [`code/fcn.004062ae.c`](code/fcn.004062ae.c)
- [`code/fcn.00406454.c`](code/fcn.00406454.c)
- [`code/fcn.00406536.c`](code/fcn.00406536.c)
- [`code/fcn.004065c8.c`](code/fcn.004065c8.c)
- [`code/fcn.004066a5.c`](code/fcn.004066a5.c)
- [`code/fcn.004068ef.c`](code/fcn.004068ef.c)
- [`code/fcn.004069c5.c`](code/fcn.004069c5.c)
- [`code/fcn.00406b22.c`](code/fcn.00406b22.c)
- [`code/fcn.00406bb0.c`](code/fcn.00406bb0.c)

## Behavioral Analysis

### Analysis Summary

The provided code is part of a **custom installer or loader wrapper**, specifically utilizing the **NSIS (Nullsoft Script Installer)** framework. Its primary purpose is to manage the extraction, verification, and execution of an application payload while handling standard installation tasks like environment configuration and UI interaction.

While the core functionality is typical for an installer, it employs techniques commonly seen in "droppers" or "wrappers," where a first-stage executable handles the complex logic of unpacking and staging files before launching the final payload.

### Core Functionality & Purpose
*   **Installer Framework Integration:** The code contains numerous references to NSIS (e.g., `nsis.sf.net`, "NSIS Error"). It acts as a wrapper to handle file system operations, directory creation, and user interface management during an installation process.
*   **File Extraction & Staging:** A significant portion of the logic involves identifying files in a source directory, moving or copying them into temporary locations (`GetTempPathW`), and setting the current working directory before execution.
*   **Integrity Verification:** Function `fcn.00406bb0` contains logic characteristic of **CRC32 or similar checksum calculations**. This is used to ensure that the files being moved/unpacked haven't been corrupted during the process.
*   **UI Management:** The code handles standard Windows GUI interactions, including progress reporting (via `SetWindowTextW`), dialog boxes (`DialogBoxParamW`), and handling system-level messages.

### Suspicious or Malicious Behaviors
*   **Staging of Executables:** The use of `CopyFileW` to move files into temporary directories followed by `GetProcAddress` and potential execution suggests the program is "dropping" a second-stage executable. This is a common technique for both legitimate installers and malware (droppers) to hide the final payload from simple static scanners.
*   **Privilege Escalation:** The code explicitly attempts to acquire high-level privileges (e.g., `SeShutdownPrivilege`) via `AdjustTokenPrivileges`. While often used by installers to perform system reboots after updates, it is also a common step for malware seeking to bypass local security restrictions or force system changes.
*   **Environment Manipulation:** The code includes logic to manually check and set the `TEMP` environment variable if the standard Windows query fails or provides an inaccessible path. This ensures the installer can proceed even in restricted environments—a behavior used by both legitimate installers and malware attempting to find a "safe" spot for file extraction.

### Notable Techniques & Patterns
*   **Multi-Stage Execution:** The structure of `entry0` suggests it acts as a "loader." It performs several checks (integrity, paths) before ultimately handing off control or launching the main application logic.
*   **Resource Obfuscation/Packing Style:** The use of many nested calls to internal functions (`fcn.004...`) and the large switch statement in `fcn.00401434` indicate a highly modularized installer engine designed to handle various configuration flags without exposing all logic at once.
*   **Dynamic Path Resolution:** The code performs extensive string manipulation to construct paths dynamically, ensuring that the "real" path of the payload is only resolved in memory during execution.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1105 | Ingress Tool Transfer | The "Staging of Executables" behavior, involving moving files to temporary directories before execution, is a common method for staging payloads for later use. |
| T1036 | Masquerading | Utilizing the NSIS (Nullsoft Script Installer) framework allows the malicious code to hide its true purpose behind the facade of a standard installer. |
| T1027 | Obfuscated Files or Information | The use of modular logic, nested internal functions, and dynamic path resolution is designed to hide the core functionality from static analysis. |
| T1068 | Exploitation for Privilege Escalation | The explicit call to `AdjustTokenPrivileges` to acquire high-level system privileges (e.g., `SeShutdownPrivilege`) indicates an attempt to escalate authority. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: The "Extracted Strings" section consists primarily of standard Windows API calls and library imports. These are not unique IOCs for a specific threat actor, but they characterize the capabilities of the sample.*

**IP addresses / URLs / Domains**
*   None (Note: `nsis.sf.net` is mentioned in the analysis as part of the NSIS framework, but it is not presented as an active C2 or malicious link).

**File paths / Registry keys**
*   None (The strings provided are standard API functions such as `GetTempPathW`, `GetSystemDirectoryW`, and `RegOpenKeyExW` rather than hardcoded malicious paths/keys).

**Mutex names / Named pipes**
*   None.

**Hashes**
*   None.

**Other artifacts**
*   **Framework Identification:** NSIS (Nullsoft Script Installer) — The sample utilizes the NSIS framework to act as a wrapper or installer.
*   **Malware Type/Technique:** Dropper/Loader functionality (Stage 1 executable designed to unpack and stage a Stage 2 payload).
*   **Persistence/Escalation Technique:** Use of `AdjustTokenPrivileges` to attempt to gain elevated system privileges.
*   **Evasion Technique:** Dynamic path resolution and staging files in temporary directories (`GetTempPathW`) to hide the final payload from static analysis.
*   **Integrity Check:** Presence of a CRC32 or similar checksum calculation routine (identified as `fcn.00406bb0`).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`
- `http://schemas.microsoft.com/SMI/2016/WindowsSettings`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High

**Key evidence**:
*   **Staging and Execution:** The sample functions as a wrapper that extracts, moves to temporary directories (`GetTempPathW`), and verifies the integrity (CRC32) of a secondary payload before execution—a classic "dropper" workflow designed to bypass static analysis.
*   **Masquerading via Frameworks:** It utilizes the NSIS (Nullsoft Script Installer) framework to hide its malicious intent behind a familiar, legitimate installer interface.
*   **Evasive Techniques:** The inclusion of `AdjustTokenPrivileges` for potential privilege escalation and dynamic path resolution indicates an intentional effort to bypass security restrictions and conceal the final payload's location during the initial infection stage.
