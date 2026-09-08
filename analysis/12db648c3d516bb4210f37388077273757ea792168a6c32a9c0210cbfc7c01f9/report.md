# Threat Analysis Report

**Generated:** 2026-08-31 21:43 UTC
**Sample:** `12db648c3d516bb4210f37388077273757ea792168a6c32a9c0210cbfc7c01f9_12db648c3d516bb4210f37388077273757ea792168a6c32a9c0210cbfc7c01f9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12db648c3d516bb4210f37388077273757ea792168a6c32a9c0210cbfc7c01f9_12db648c3d516bb4210f37388077273757ea792168a6c32a9c0210cbfc7c01f9.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 266,647 bytes |
| MD5 | `c0214c5ac40753c905e4ecf9c4a8b48e` |
| SHA1 | `8cbb0796cce9e55c5ad359ec5a9628a06908d627` |
| SHA256 | `12db648c3d516bb4210f37388077273757ea792168a6c32a9c0210cbfc7c01f9` |
| Overall entropy | 7.856 |
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

Total strings found: **748** (showing first 100)

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

Based on the provided disassembly and string data, here is an analysis of the binary's functionality.

### Core Functionality and Purpose
The binary functions primarily as a **downloader/installer stub**, likely wrapped with or utilizing the **NSIS (Nullsoft Script Installer)** framework. Its main purpose is to serve as a "loader" for another executable. It performs several preliminary tasks before launching its primary payload:

*   **Environment Validation:** It checks system versions and verifies that necessary components (like common controls and OLE) are initialized.
*   **Command-Line Parsing:** It analyzes the command line looking for specific flags (e.g., `/S` for silent mode or `/K` to keep keys). This is a hallmark of automated installers where an attacker or script might want to execute the dropper without user interaction.
*   **Payload Extraction:** The code identifies, extracts, and moves files into a temporary directory (often using "randomized" naming conventions like `~nsu%X.tmp`).
*   **Integrity Verification:** It includes routines (specifically in `fcn.004067c4`) to perform **CRC32 checksum calculations** on the payload before execution. This ensures that the file hasn't been corrupted or tampered with during the unpacking/extraction process.

### Suspicious or Malicious Behaviors
While many legitimate installers use these techniques, in a malware context, these behaviors are characteristic of a "Dropper" or "Downloader." Specific suspicious activities include:

*   **Staged Execution:** By extracting the payload to a temporary directory and then executing it, the binary creates a gap between the initial infection (the installer) and the final malicious action (the executed payload). This is used to evade basic antivirus detection that only scans the initial file.
*   **Silent/Hidden Installation:** The presence of logic to handle "Silent" flags (`/S`) indicates an intent to run the installation process without showing any UI or prompts to the user, common in automated malware deployment.
*   **Anti-Analysis Logic (Ambiguous):** While not a heavy anti-debugging suite, the reliance on `MessageBoxIndirectA` and complex state checks suggests it tries to handle errors gracefully while hiding its operation from the average user.
*   **Integrity Checking:** The CRC32 check ensures that the "payload" being delivered is exactly what the attacker intended, preventing security software from injecting code into the payload or detecting an altered version of the malware.

### Notable Techniques and Patterns
*   **NSIS Framework Indicators:** The presence of strings like `"NSIS Error"` and `http://nsis.sf.net/NSIS_Error` strongly suggests this is a custom script wrapped in an NSIS installer. This is very common in "Game Cracks," "Warez," and Trojaned software.
*   **Temporary File Manipulation:** The use of `GetTempPathA`, `CopyFileA`, and `MoveFileA` to move files into the system's temp folders (e.g., `%TEMP%`) is a standard way for malware to drop and execute payload components.
*   **Dynamic API Resolution/Loading:** The code uses `GetProcAddress` and `GetModuleHandleA` in certain blocks, which allows it to resolve functions at runtime rather than at compile time, potentially hiding its capabilities from static analysis tools.
*   **Resource Management:** The use of `ShellExecuteExA` for launching the final stage is a common way to execute the unpacked payload as a separate process, detaching the malicious activity from the initial dropper's process tree.

### Summary Conclusion
This binary is a **Loader/Dropper**. It is designed to take an embedded or nearby file (the "payload"), verify its integrity via CRC32, move it into a temporary folder, and execute it—potentially in a silent mode. Its presence indicates that this binary is likely just one stage of a multi-stage infection chain.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1204.002 | Dropper | The binary acts as a loader that extracts, moves to a temporary directory, and executes a payload to facilitate a multi-stage infection. |
| T1036 | Masquerading | The use of NSIS framework strings and identifiers allows the malicious installer to blend in with legitimate "game crack" or software installation tools. |
| T1027 | Obfuscated Files or Information | CRC32 checksum calculations are used to ensure the payload remains intact and has not been tampered with by security software before execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `http://nsis.sf.net/NSIS_Error` (Note: This is a standard NSIS error page; its presence confirms the use of the Nullsoft Script Installer framework).

**File paths / Registry keys**
*   `~nsu%X.tmp` (Specific naming convention used for temporary payload extraction).
*   `%TEMP%` (Target directory for dropped components, identified via `GetTempPathA`).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Framework Identification:** NSIS (Nullsoft Script Installer).
*   **Integrity Check:** CRC32 checksum calculation used to verify payload integrity before execution.
*   **Execution Method:** `ShellExecuteExA` used for staged, detached execution of the final payload.
*   **Dropper Behavior:** Automated "Silent" mode support (triggered by `/S` or `/K` flags).
*   **File Manipulation:** Use of `MoveFileA`, `CopyFileA`, and `GetTempPathA` to move files from the installer to a system temp folder.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: custom (NSIS-wrapped)
2. **Malware type**: dropper / loader
3. **Confidence**: High
4. **Key evidence**:
    * **Staged Execution & Payload Delivery:** The binary utilizes a classic "dropper" workflow by extracting an embedded payload to a temporary directory (`%TEMP%`) and executing it via `ShellExecuteExA`, which allows the malicious payload to run as a separate process from the initial installer.
    * **Integrity Verification:** The use of CRC32 checksums indicates a deliberate effort to ensure that the secondary payload is not modified or intercepted by security software before execution.
    * **Masquerading via Frameworks:** The integration of the NSIS (Nullsoft Script Installer) framework and support for silent installation flags (`/S`, `/K`) are hallmarks of malware designed to hide its activities from the user during the initial infection phase.
