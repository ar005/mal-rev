# Threat Analysis Report

**Generated:** 2026-07-19 13:25 UTC
**Sample:** `093ede1caec2dfbe8eacaeec091fad7f27b5c206503ca0b645f3c79167121094_093ede1caec2dfbe8eacaeec091fad7f27b5c206503ca0b645f3c79167121094.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `093ede1caec2dfbe8eacaeec091fad7f27b5c206503ca0b645f3c79167121094_093ede1caec2dfbe8eacaeec091fad7f27b5c206503ca0b645f3c79167121094.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 901,960 bytes |
| MD5 | `b8f4df5aedc8eb364ff53c157b94451d` |
| SHA1 | `371e55a7374e005420e8ef6cc5b8c72861f54f05` |
| SHA256 | `093ede1caec2dfbe8eacaeec091fad7f27b5c206503ca0b645f3c79167121094` |
| Overall entropy | 7.914 |
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
| `.rsrc` | 99,328 | 6.32 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `lstrcmpiA`, `CreateFileW`, `GetTempFileNameW`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`

## Extracted Strings

Total strings found: **1932** (showing first 100)

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

Based on the provided disassembly and decompiled code, here is an analysis of the binary's functionality.

### Core Functionality and Purpose
The binary appears to be an **installer stub or wrapper**, specifically exhibiting characteristics common in **NSIS (Nullsoft Script Installer)** based installers. Its primary purpose is to manage the unpacking, verification, and installation of software components.

*   **Installation Logic:** The code contains large switch-case blocks (`fcn.00401434`) that handle standard installer actions such as interacting with dialog boxes, managing window states, and processing user inputs.
*   **Integrity Verification:** A significant portion of the code is dedicated to verifying file integrity. Function `fcn.00406a5d` implements a mathematical algorithm (likely **CRC32 or Adler-32**) to ensure that files have not been corrupted during the unpacking process.
*   **Environment Configuration:** The code checks for the existence of system components (e.g., "UXTHEME") and manages environmental variables, such as paths for temporary files and system directories.

### Suspicious/Malicious Behaviors
While this specific logic is common in legitimate installer programs, it can be used by malware as a **"Dropper"** or **"Loader."** The following behaviors are noted:

*   **File Manipulation & Extraction:**
    *   The code frequently uses `GetTempPathW`, `MoveFileW`, and `CopyFileW` to move files from temporary locations to final destinations.
    *   It performs "search and replace" operations on file paths (e.g., `fcn.004061c2`), which is common when a dropper extracts an embedded payload and prepares it for execution.
*   **Integrity Checks:** The use of checksums (`fcn.00406a5d`) ensures that the "payload" (which could be legitimate software or a malicious component) was successfully unpacked before being executed by the main installer logic.
*   **Registry Interaction:** Functions like `RegOpenKeyExW`, `RegSetValueExW`, and `RegDeleteValueW` indicate the program modifies the Windows Registry, likely to ensure persistence or configure settings for the installed application.
*   **Privilege Management:** The code attempts to adjust token privileges (e.g., `AdjustTokenPrivileges` and `LookupPrivilegeValueW`). While common in installers that need administrative rights to write to `C:\Program Files`, this is also a technique used by malware to elevate its capabilities.

### Notable Techniques & Patterns
*   **NSIS Signatures:** The presence of "NSIS Error" strings and the structure of the state machine in the code indicate it is likely an NSIS-generated wrapper. These are frequently "wrapped" by malicious actors because they provide a layer of abstraction between the raw malware payload and the initial execution.
*   **Dynamic Path Resolution:** The binary uses several helper functions to resolve relative paths into full system paths, ensuring that dropped files can be located even if the installer is run from an arbitrary location.
*   **Self-Correction/Check Loops:** There are loops designed to "wait" or retry actions (e.g., `GetFileAttributes` checks), which are used to handle locked files or late-loading system resources during the installation phase.

### Summary for Security Context
This binary is a **pre-execution installer wrapper**. While the code provided does not show direct network communication (C2) or active process injection, it provides the infrastructure for a **Dropper** scenario: 
1.  It extracts an encrypted/compressed payload from its own resources.
2.  It verifies the integrity of that payload using checksums.
3.  It moves and names the payload in a temporary directory.
4.  It prepares the system environment to run the payload.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of an NSIS wrapper provides a layer of abstraction that allows malicious content to be hidden within a legitimate-looking installer. |
| T1112 | Modify Registry | The use of `RegOpenKeyExW` and `RegSetValueExW` indicates the program modifies system configuration or seeks to establish persistence via the registry. |
| T1548 | Privilege Escalation | The inclusion of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` demonstrates an attempt by the binary to gain higher-level system privileges. |
| T1568 | Dynamic Resolution | The use of helper functions to resolve relative paths into full system paths allows the malware to function across different environments and avoid static analysis of hardcoded paths. |
| T1027 | Software Installer | The behavior characterizes a "Dropper" or "Loader" that automates the installation, unpacking, and preparation of payloads on a host system. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Because the analysis indicates this is a generic installer stub/wrapper, many of the identifiers found in the "Extracted Strings" section are standard Windows API calls or common library names and have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: While the report mentions `C:\Program Files` and temporary directories, these are standard system locations and do not constitute specific malicious IOCs).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Installer Type:** NSIS (Nullsoft Script Installer) 
*   **Verification Algorithm:** CRC32 or Adler-32 (detected via `fcn.00406a5d`)
*   **Persistence/Privilege Tactics:** `AdjustTokenPrivileges`, `LookupPrivilegeValueW` (Used for privilege escalation/modification).

---
**Analyst Note:** 
The sample is identified as a **Dropper/Loader wrapper**. While it does not contain hardcoded C2 infrastructure (IPs/Domains) or specific malicious file paths in the provided text, its primary IOC is its behavior: utilizing an NSIS wrapper to unpack and verify an embedded payload. For proactive defense, security teams should monitor for unauthorized NSIS-based executables performing `MoveFileW` operations in system directories or requesting elevated privileges.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper / loader
3. **Confidence**: High

4. **Key evidence**:
*   **NSIS Wrapper Logic:** The binary functions as an NSIS-based installer stub, a common technique used by malware to wrap and "hide" a primary payload (e.g., ransomware or a RAT) within a legitimate-looking installation process.
*   **Payload Preparation & Verification:** The presence of checksum routines (CRC32/Adler-32), file movement functions (`MoveFileW`, `CopyFileW`), and temporary directory handling indicates its primary role is to unpack, verify, and stage an embedded payload for execution.
*   **Privilege Escalation & Persistence:** The integration of `AdjustTokenPrivileges` and registry modification functions suggests the binary is designed to ensure that once the dropped payload is executed, it has the necessary permissions and persistence to operate on the system.
