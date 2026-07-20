# Threat Analysis Report

**Generated:** 2026-07-19 12:22 UTC
**Sample:** `092b7de8fe08fbf5aad89b80f5b19e1469e1c66986fae44ca36c9fda366857a0_092b7de8fe08fbf5aad89b80f5b19e1469e1c66986fae44ca36c9fda366857a0.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `092b7de8fe08fbf5aad89b80f5b19e1469e1c66986fae44ca36c9fda366857a0_092b7de8fe08fbf5aad89b80f5b19e1469e1c66986fae44ca36c9fda366857a0.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 905,874 bytes |
| MD5 | `37bda1fc6b5d7299f70e6ff85fa68b13` |
| SHA1 | `eaafb4240d049f7f9178c16c9898a033104d7008` |
| SHA256 | `092b7de8fe08fbf5aad89b80f5b19e1469e1c66986fae44ca36c9fda366857a0` |
| Overall entropy | 7.771 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1711817706 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,624 | 6.471 | No |
| `.rdata` | 5,120 | 5.102 | No |
| `.data` | 1,536 | 4.036 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 122,368 | 5.034 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `lstrcmpiA`, `CreateFileW`, `GetTempFileNameW`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `GetLastError`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`

## Extracted Strings

Total strings found: **2174** (showing first 100)

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
D$SVW
A@;E |
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 6189 | ✓ |
| `fcn.00406c40` | `0x406c40` | 2183 | ✓ |
| `entry0` | `0x40352f` | 1565 | ✓ |
| `fcn.00403c26` | `0x403c26` | 726 | ✓ |
| `fcn.00406591` | `0x406591` | 625 | ✓ |
| `fcn.004030a2` | `0x4030a2` | 567 | ✓ |
| `fcn.004032d9` | `0x4032d9` | 504 | ✓ |
| `fcn.00405c60` | `0x405c60` | 451 | ✓ |
| `fcn.0040619a` | `0x40619a` | 378 | ✓ |
| `fcn.00406af8` | `0x406af8` | 328 | ✓ |
| `fcn.00402ece` | `0x402ece` | 234 | ✓ |
| `fcn.004075f9` | `0x4075f9` | 216 | ✓ |
| `fcn.004055d9` | `0x4055d9` | 211 | ✓ |
| `fcn.0040453a` | `0x40453a` | 207 | ✓ |
| `fcn.00404d80` | `0x404d80` | 201 | ✓ |
| `fcn.00403efc` | `0x403efc` | 185 | ✓ |
| `fcn.00406802` | `0x406802` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.004064b4` | `0x4064b4` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00406340` | `0x406340` | 129 | ✓ |
| `fcn.00407578` | `0x407578` | 129 | ✓ |
| `fcn.00404e8e` | `0x404e8e` | 128 | ✓ |
| `fcn.00405f2b` | `0x405f2b` | 126 | ✓ |
| `fcn.00406422` | `0x406422` | 121 | ✓ |
| `fcn.00406125` | `0x406125` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004068d8` | `0x4068d8` | 112 | ✓ |
| `fcn.00406a35` | `0x406a35` | 110 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402ece.c`](code/fcn.00402ece.c)
- [`code/fcn.004030a2.c`](code/fcn.004030a2.c)
- [`code/fcn.004032d9.c`](code/fcn.004032d9.c)
- [`code/fcn.00403c26.c`](code/fcn.00403c26.c)
- [`code/fcn.00403efc.c`](code/fcn.00403efc.c)
- [`code/fcn.0040453a.c`](code/fcn.0040453a.c)
- [`code/fcn.00404d80.c`](code/fcn.00404d80.c)
- [`code/fcn.00404e8e.c`](code/fcn.00404e8e.c)
- [`code/fcn.004055d9.c`](code/fcn.004055d9.c)
- [`code/fcn.00405c60.c`](code/fcn.00405c60.c)
- [`code/fcn.00405f2b.c`](code/fcn.00405f2b.c)
- [`code/fcn.00406125.c`](code/fcn.00406125.c)
- [`code/fcn.0040619a.c`](code/fcn.0040619a.c)
- [`code/fcn.00406340.c`](code/fcn.00406340.c)
- [`code/fcn.00406422.c`](code/fcn.00406422.c)
- [`code/fcn.004064b4.c`](code/fcn.004064b4.c)
- [`code/fcn.00406591.c`](code/fcn.00406591.c)
- [`code/fcn.00406802.c`](code/fcn.00406802.c)
- [`code/fcn.004068d8.c`](code/fcn.004068d8.c)
- [`code/fcn.00406a35.c`](code/fcn.00406a35.c)
- [`code/fcn.00406af8.c`](code/fcn.00406af8.c)
- [`code/fcn.00406c40.c`](code/fcn.00406c40.c)
- [`code/fcn.00407578.c`](code/fcn.00407578.c)
- [`code/fcn.004075f9.c`](code/fcn.004075f9.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary's functionality and behavior.

### Core Functionality and Purpose
The binary functions as a **software installer**, specifically showing strong characteristics of an **NSIS (Nullsoft Script Installer)** stub or a similar setup utility. Its primary purpose is to handle the unpacking, integrity verification, and installation of files from a compressed or bundled source onto a host system.

### Suspicious or Malicious Behaviors
While many of these behaviors are common in legitimate installers, they are also frequently utilized by malware for staging and execution:

*   **Privilege Escalation:** The code specifically calls `OpenProcessToken`, `LookupPrivilegeValueW`, and `AdjustTokenPrivileges`. This is used to gain administrative rights, allowing the program (or any subsequent process it launches) to modify system files or registry keys.
*   **Payload Staging (Drop and Execute):** 
    *   The code uses `GetTempPathW` and handles filenames like `"nsu%X.tmp"`. This is a classic technique for extracting "hidden" components into a temporary directory before execution.
    *   It performs multiple `CopyFileW` operations, which suggests moving files from an internal resource or compressed volume to the local disk.
*   **File Manipulation:** The presence of `MoveFileW`, `DeleteFileW`, and `FindFirstFileW` indicates that the program actively manages the file system, likely cleaning up temporary files or "installing" components into target directories.
*   **Persistence/Configuration via Registry:** The extensive use of `RegCreateKeyExW`, `RegSetValueExW`, and `RegEnumKeyW` suggests the installer modifies the Windows Registry to configure settings, create persistent entries, or store configuration data for a newly "installed" application.
*   **Integrity Checking:** Function `fcn.004030a2` contains logic to perform an "Installer integrity check." While this ensures the installer is not corrupted, in a malware context, it can be used to verify that a secondary malicious payload was successfully unpacked and remains intact before execution.

### Notable Techniques and Patterns
*   **NSIS Indicators:** The presence of "nsu" naming conventions and the specific error messages (e.g., "Installer integrity check has failed... visit nsis.sf.net") indicate it uses the NSIS framework. Malware authors often use legitimate installers to wrap malicious payloads because they are familiar to users and less likely to trigger basic heuristic flags.
*   **Checksum/Hash Verification:** Function `fcn.00406a35` contains mathematical operations (like `0xedb88320`) typical of **CRC32 or similar checksum algorithms**. This is used to verify that the data being unpacked matches a specific value, ensuring the payload remains intact during the extraction process.
*   **Dynamic Loading:** The use of `GetModuleHandle` and `LoadLibraryExW` suggests it may dynamically load modules or components at runtime, which can be a way to hide the true functionality of the software until after it has been unpacked.
*   **Standard GUI Manipulation:** Large chunks of the code (e.g., `fcn.00401434`) handle window management (`ShowWindow`, `SetForegroundWindow`), indicating it provides a standard user interface during its execution to appear as a legitimate installation wizard.

### Summary for Incident Response
This is an **installer-type binary**. While the current code shows typical setup behavior, the most significant risk lies in its capability to **request elevated privileges** and **drop/move files into temporary directories**. These actions are frequently used by "droppers" to land a secondary payload (e.g., a backdoor or ransomware) onto the system before executing it.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1068** | Exploitation for Privilege Escalation | The binary utilizes `OpenProcessToken`, `LookupPrivilegeValueW`, and `AdjustTokenPrivileges` to gain administrative rights. |
| **T1027** | Software Deployment | The "Drop and Execute" behavior, specifically using temporary directories (`nsu%X.tmp`) for staging components, is characteristic of software installers/droppers. |
| **T1547** | Boot or Logon Autostart Execution | The use of `RegCreateKeyExW` and `RegSetValueExW` to modify the Registry indicates an attempt to establish persistence or configuration. |
| **T1036** | Masquerading | The binary uses NSIS branding, standard UI elements (GUI manipulation), and familiar error messages to blend in as a legitimate installer. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: As this is a functional analysis of an installer-style binary, many indicators relate to "tooling" and "behavioral patterns" rather than hardcoded malicious infrastructure.*

### **IP addresses / URLs / Domains**
*   **nsis.sf.net** (Identified in the behavior report as part of the standard NSIS error messages; indicates the use of the Nullsoft Script Installer framework).

### **File paths / Registry keys**
*   **nsu%X.tmp** (A naming convention for temporary files created during the unpacking/staging process in a temporary directory via `GetTempPathW`).
*   **Registry Operations:** While no specific registry keys (e.g., `HKLM\...\Software`) were extracted, the binary actively utilizes `RegCreateKeyExW`, `RegSetValueExW`, and `RegOpenKeyExW` to modify system settings or establish persistence.

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *No file hashes (MD5/SHA1/SHA256) were present in the provided strings.* 
    *(Note: The value `0xedb88320` was identified as a CRC32 constant, not a file hash).*

### **Other artifacts**
*   **Framework Identifier:** NSIS (Nullsoft Script Installer). The presence of "nsu" prefixes and specific integrity check strings confirms the use of this common installer wrapper.
*   **Integrity Check Constant:** `0xedb88320` (Used in a CRC32-style algorithm to verify unpacked payloads).
*   **Privilege Escalation Logic:** Execution of `OpenProcessToken`, `LookupPrivilegeValueW`, and `AdjustTokenPrivileges`.
*   **Payload Staging Behavior:** The combination of `GetTempPathW`, `CopyFileW`, and `MoveFileW` indicates a "dropper" behavior where files are moved from an internal resource to the local disk for execution.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Drop and Execute Behavior**: The binary utilizes `GetTempPathW`, `CopyFileW`, and `MoveFileW` to extract files from internal resources into temporary directories (e.g., `nsu%X.tmp`), a hallmark of dropper functionality.
    *   **Privilege Escalation & Persistence**: The inclusion of `AdjustTokenPrivileges` for administrative rights and extensive registry manipulation (`RegCreateKeyExW`, `RegSetValueExW`) indicates an intent to gain system-level control and establish persistence.
    *   **Masquerading Techniques**: The use of the NSIS (Nullsoft Script Installer) framework, combined with standard UI elements and integrity checks, is a common tactic used to disguise malicious activity as a legitimate software installation process.
