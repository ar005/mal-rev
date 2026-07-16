# Threat Analysis Report

**Generated:** 2026-07-16 14:22 UTC
**Sample:** `072d6dfc5ad637c6220f86c169e62deeb8fcac13a3e5eeb9d548c4bda3c5cbc3_072d6dfc5ad637c6220f86c169e62deeb8fcac13a3e5eeb9d548c4bda3c5cbc3.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `072d6dfc5ad637c6220f86c169e62deeb8fcac13a3e5eeb9d548c4bda3c5cbc3_072d6dfc5ad637c6220f86c169e62deeb8fcac13a3e5eeb9d548c4bda3c5cbc3.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 456,400 bytes |
| MD5 | `c6dd27911d268408966e7e9e954fcf75` |
| SHA1 | `e98e3b7e14eaa1ab374c8dc936c8180a66c34978` |
| SHA256 | `072d6dfc5ad637c6220f86c169e62deeb8fcac13a3e5eeb9d548c4bda3c5cbc3` |
| Overall entropy | 7.333 |
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
| `.text` | 26,112 | 6.385 | No |
| `.rdata` | 5,120 | 5.027 | No |
| `.data` | 1,536 | 4.11 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 166,912 | 5.511 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueA`, `RegEnumKeyA`, `RegQueryValueExA`, `RegSetValueExA`, `RegCloseKey`, `RegDeleteValueA`, `RegDeleteKeyA`, `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, `OpenProcessToken`, `RegOpenKeyExA`, `RegCreateKeyExA`
**SHELL32.dll**: `SHGetPathFromIDListA`, `SHBrowseForFolderA`, `SHGetFileInfoA`, `SHFileOperationA`, `ShellExecuteExA`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoCreateInstance`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `SetDlgItemTextA`, `GetSystemMetrics`, `CreatePopupMenu`, `AppendMenuA`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcA`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorA`, `SetCursor`, `GetSysColor`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectA`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `CreateProcessA`, `RemoveDirectoryA`, `GetTempFileNameA`, `CreateDirectoryA`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceA`, `lstrcpynA`, `SetErrorMode`, `GetVersionExA`, `lstrlenA`, `GetCommandLineA`, `GetTempPathA`, `GetWindowsDirectoryA`

## Extracted Strings

Total strings found: **853** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQVPW
Et@;u
vX95hCB
#VhQ.@
Instuj
softua
NulluX	E
tVj%WWW
D$$+D$
D$,+D$$P
u9=H	B
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
| `fcn.00401434` | `0x401434` | 5839 | ✓ |
| `fcn.00406965` | `0x406965` | 2642 | ✓ |
| `entry0` | `0x40352b` | 1508 | ✓ |
| `fcn.00402f88` | `0x402f88` | 724 | ✓ |
| `fcn.00403c01` | `0x403c01` | 709 | ✓ |
| `fcn.0040648b` | `0x40648b` | 615 | ✓ |
| `fcn.00405bba` | `0x405bba` | 464 | ✓ |
| `fcn.00406061` | `0x406061` | 368 | ✓ |
| `fcn.00403364` | `0x403364` | 361 | ✓ |
| `fcn.0040325c` | `0x40325c` | 264 | ✓ |
| `fcn.00402d67` | `0x402d67` | 234 | ✓ |
| `fcn.0040553c` | `0x40553c` | 210 | ✓ |
| `fcn.004044ff` | `0x4044ff` | 207 | ✓ |
| `fcn.00404ce1` | `0x404ce1` | 197 | ✓ |
| `fcn.00403ec6` | `0x403ec6` | 185 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00402ee9` | `0x402ee9` | 159 | ✓ |
| `fcn.004066f2` | `0x4066f2` | 153 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.0040636f` | `0x40636f` | 137 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.004061fd` | `0x4061fd` | 129 | ✓ |
| `fcn.00404deb` | `0x404deb` | 128 | ✓ |
| `fcn.00405e78` | `0x405e78` | 120 | ✓ |
| `fcn.004062df` | `0x4062df` | 119 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004068d7` | `0x4068d7` | 110 | ✓ |
| `fcn.004067b2` | `0x4067b2` | 110 | ✓ |
| `fcn.0040560e` | `0x40560e` | 108 | ✓ |
| `fcn.00405b0e` | `0x405b0e` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402d67.c`](code/fcn.00402d67.c)
- [`code/fcn.00402ee9.c`](code/fcn.00402ee9.c)
- [`code/fcn.00402f88.c`](code/fcn.00402f88.c)
- [`code/fcn.0040325c.c`](code/fcn.0040325c.c)
- [`code/fcn.00403364.c`](code/fcn.00403364.c)
- [`code/fcn.00403c01.c`](code/fcn.00403c01.c)
- [`code/fcn.00403ec6.c`](code/fcn.00403ec6.c)
- [`code/fcn.004044ff.c`](code/fcn.004044ff.c)
- [`code/fcn.00404ce1.c`](code/fcn.00404ce1.c)
- [`code/fcn.00404deb.c`](code/fcn.00404deb.c)
- [`code/fcn.0040553c.c`](code/fcn.0040553c.c)
- [`code/fcn.0040560e.c`](code/fcn.0040560e.c)
- [`code/fcn.00405b0e.c`](code/fcn.00405b0e.c)
- [`code/fcn.00405bba.c`](code/fcn.00405bba.c)
- [`code/fcn.00405e78.c`](code/fcn.00405e78.c)
- [`code/fcn.00406061.c`](code/fcn.00406061.c)
- [`code/fcn.004061fd.c`](code/fcn.004061fd.c)
- [`code/fcn.004062df.c`](code/fcn.004062df.c)
- [`code/fcn.0040636f.c`](code/fcn.0040636f.c)
- [`code/fcn.0040648b.c`](code/fcn.0040648b.c)
- [`code/fcn.004066f2.c`](code/fcn.004066f2.c)
- [`code/fcn.004067b2.c`](code/fcn.004067b2.c)
- [`code/fcn.004068d7.c`](code/fcn.004068d7.c)
- [`code/fcn.00406965.c`](code/fcn.00406965.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is a professional analysis of the binary's behavior:

### Core Functionality and Purpose
The binary appears to be a **downloader/installer wrapper**, specifically one utilizing or mimicking the **NSIS (Nullsoft Script Install System)** framework. Its primary purpose is to extract, verify, and launch an underlying application or "payload" from a bundled data archive.

It functions as a "stub": it prepares the environment (checking OS versions, setting up temporary folders), unpacks encrypted or compressed resources, validates them using checksums, and then executes the main components.

### Suspicious or Malicious Behaviors
While many of these behaviors are common in legitimate installers, they are also standard techniques used by **droppers** and **loaders**:

*   **Payload Extraction & File Manipulation:** The code frequently uses `CreateFileA`, `GetFileSize`, `MoveFileA`, and `CopyFileA`. It specifically handles the creation of temporary files (e.g., in `entry0`) to house decompressed data before execution.
*   **Integrity Verification:** Function `fcn.004068d7` implements a **CRC-32 checksum algorithm**. This is used to verify that the extracted files have not been corrupted or tampered with, which ensures the "correct" payload is delivered.
*   **Dynamic API Resolution & Loading:** The code uses `GetProcAddress` and `LoadLibraryExA` (within `fcn.00403c01`) to resolve function addresses at runtime rather than linking them at compile time. This is often used to hide the intended functionality of the program from static analysis.
*   **Environment Manipulation:** The code interacts with System Environment Variables and Registry keys (`RegOpenKeyExA`, `RegSetValueExA`). While common in installers, these are frequently used by malware to ensure persistence or modify system configurations.
*   **Argument Parsing (Hidden Behavior):** In `entry0`, the code parses command-line arguments looking for specific flags (like `/S` or `/D`). This is typical of silent installers but also allows a loader to switch between "manual" and "automated/hidden" execution modes.

### Notable Techniques & Patterns
*   **NSIS Artifacts:** The presence of strings like `"NSIS Error"` and the handling of `UXTHEME` suggest the binary was built using the NSIS installer toolkit or a similar wrapper that targets Windows' visual themes.
*   **Resource Management:** Function `fcn.00406965` contains complex logic involving bitwise shifts and rotations used to calculate offsets within large data blocks, indicating it is handling highly compressed or packed resources.
*   **Standardized Error Handling:** The code includes a dedicated error-handling routine (`fcn.00403c01`) that provides specific feedback if the "Installer integrity check" fails, which is a hallmark of professional installer design.

### Summary for Security Context
This binary is a **loader/installer stub**. In a security context, it should be treated as a "delivery vehicle." While the loader itself may not perform direct malicious actions (like stealing data), its role is to facilitate the deployment of another component. 

**Recommendation:** If this sample was found in an unexpected location, investigate the files it extracts/moves into the `TEMP` directory or any calls made shortly after the integrity check (`fcn.004068d7`) passes.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The binary utilizes NSIS artifacts and standard installer behaviors (like silent flags) to masquerade as a legitimate software installer/wrapper. |
| T1112 | Modify Registry | The use of `RegOpenKeyExA` and `RegSetValueExA` indicates the modification of registry keys for configuration or potential persistence. |
| T1027 | Obfuscated Files or Information | The use of CRC-32 checks, bitwise shift/rotation logic for resource offsets, and dynamic API resolution (`GetProcAddress`) are techniques used to hide the payload's true characteristics from static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted list of Indicators of Compromise (IOCs). 

Note: The "Strings" section contains a significant amount of standard Windows API calls and system registry keys; per your instructions, these have been filtered out as they do not constitute unique indicators of malicious activity.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified (all listed registry paths—e.g., `Control Panel\Desktop\ResourceLocale` and `Software\Microsoft\Windows\CurrentVersion`—are standard Windows system locations).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified (The analysis mentions a CRC-32 checksum algorithm at `fcn.004068d7`, but no specific hash value or string was provided in the text).

### **Other artifacts**
*   **NSIS Framework Indicators:** The presence of "NSIS" related strings and `UXTHEME` support suggests an installer-style wrapper.
*   **Dynamic API Resolution:** Use of `GetProcAddress` and `LoadLibraryExA` at `fcn.00403c01` for hidden functionality.
*   **Integrity Check Routine:** CRC-32 checksum calculation located at `fcn.004068d7`.
*   **Command-Line Arguments:** Support for `/S` (Silent) and `/D` (Directory) flags in the `entry0` logic, typical of automated loader deployment.

---
**Analyst Note:** This binary functions as a **loader/stub**. While it does not contain immediate network IOCs (IPs/Domains), its behavior indicates it is designed to unpack and verify a secondary payload into the system's temporary folders before execution. Investigation should focus on the files generated after `fcn.004068d7` completes successfully.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**: 
*   **Stub/Wrapper Functionality:** The binary acts as a "delivery vehicle" using NSIS-like artifacts, specifically designed to unpack, verify via CRC-32 checksums (`fcn.004068d7`), and execute a secondary payload from embedded resources.
*   **Evasion & Obfuscation Techniques:** The use of dynamic API resolution (`GetProcAddress`/`LoadLibraryExA`) and bitwise shift/rotation logic to calculate resource offsets are classic indicators of a loader intended to hide its primary functionality from static analysis.
*   **Automation for Deployment:** The inclusion of silent installation flags (e.g., `/S`, `/D`) and the automated movement of files into `TEMP` directories indicate it is designed for programmatic deployment in a malware lifecycle.
