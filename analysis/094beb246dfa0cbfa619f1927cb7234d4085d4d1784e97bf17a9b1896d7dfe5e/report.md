# Threat Analysis Report

**Generated:** 2026-07-19 14:39 UTC
**Sample:** `094beb246dfa0cbfa619f1927cb7234d4085d4d1784e97bf17a9b1896d7dfe5e_094beb246dfa0cbfa619f1927cb7234d4085d4d1784e97bf17a9b1896d7dfe5e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `094beb246dfa0cbfa619f1927cb7234d4085d4d1784e97bf17a9b1896d7dfe5e_094beb246dfa0cbfa619f1927cb7234d4085d4d1784e97bf17a9b1896d7dfe5e.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 755,632 bytes |
| MD5 | `7b9a8f1cf5251938c330ea07d5a0e692` |
| SHA1 | `decccbc58a8c3ef736891897d3a7d86e5bcf5d70` |
| SHA256 | `094beb246dfa0cbfa619f1927cb7234d4085d4d1784e97bf17a9b1896d7dfe5e` |
| Overall entropy | 7.77 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1501547639 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.479 | No |
| `.rdata` | 5,120 | 5.144 | No |
| `.data` | 1,536 | 4.001 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 91,136 | 4.253 | No |

### Imports

**KERNEL32.dll**: `ExitProcess`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `CreateFileW`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `SetEnvironmentVariableW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1723** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQVPW
Instu_
softuV
NulluM	E
SVWj _3
Aj"A[f
D$$SPS
tVj%SSS
f9=(7B
D$$+D$
D$,+D$$P
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
RichEd32
RichEd20
MulDiv
DeleteFileW
FindFirstFileW
FindNextFileW
FindClose
SetFilePointer
ReadFile
MultiByteToWideChar
lstrlenA
WideCharToMultiByte
GetPrivateProfileStringW
WritePrivateProfileStringW
FreeLibrary
LoadLibraryExW
GetModuleHandleW
GlobalAlloc
GlobalFree
ExpandEnvironmentStringsW
lstrcmpW
lstrcmpiW
CloseHandle
SetFileTime
CompareFileTime
SearchPathW
GetShortPathNameW
GetFullPathNameW
MoveFileW
SetCurrentDirectoryW
GetFileAttributesW
SetFileAttributesW
GetTickCount
CreateFileW
GetFileSize
GetModuleFileNameW
GetCurrentProcess
CopyFileW
ExitProcess
SetEnvironmentVariableW
GetWindowsDirectoryW
GetTempPathW
GetCommandLineW
GetVersion
SetErrorMode
lstrlenW
lstrcpynW
GetDiskFreeSpaceW
GlobalUnlock
GlobalLock
CreateThread
GetLastError
CreateDirectoryW
CreateProcessW
RemoveDirectoryW
lstrcmpiA
GetTempFileNameW
WriteFile
lstrcpyA
MoveFileExW
lstrcatW
GetSystemDirectoryW
GetProcAddress
GetModuleHandleA
GetExitCodeProcess
WaitForSingleObject
KERNEL32.dll
EndPaint
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5789 | ✓ |
| `fcn.0040690b` | `0x40690b` | 2642 | ✓ |
| `entry0` | `0x403489` | 1347 | ✓ |
| `fcn.00403abe` | `0x403abe` | 726 | ✓ |
| `fcn.00402f14` | `0x402f14` | 678 | ✓ |
| `fcn.004063d2` | `0x4063d2` | 626 | ✓ |
| `fcn.00405abe` | `0x405abe` | 451 | ✓ |
| `fcn.00405ffc` | `0x405ffc` | 378 | ✓ |
| `fcn.004032c2` | `0x4032c2` | 361 | ✓ |
| `fcn.004031ba` | `0x4031ba` | 264 | ✓ |
| `fcn.00405414` | `0x405414` | 211 | ✓ |
| `fcn.00404bd0` | `0x404bd0` | 201 | ✓ |
| `fcn.00403d94` | `0x403d94` | 185 | ✓ |
| `fcn.00406644` | `0x406644` | 175 | ✓ |
| `fcn.00402d2a` | `0x402d2a` | 173 | ✓ |
| `fcn.004043ac` | `0x4043ac` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00402e72` | `0x402e72` | 162 | ✓ |
| `fcn.00406310` | `0x406310` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404cde` | `0x404cde` | 128 | ✓ |
| `fcn.00405d89` | `0x405d89` | 126 | ✓ |
| `fcn.004058e3` | `0x4058e3` | 125 | ✓ |
| `fcn.004061a2` | `0x4061a2` | 123 | ✓ |
| `fcn.00405f83` | `0x405f83` | 121 | ✓ |
| `fcn.0040627e` | `0x40627e` | 121 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.0040671a` | `0x40671a` | 112 | ✓ |
| `fcn.0040687d` | `0x40687d` | 110 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402d2a.c`](code/fcn.00402d2a.c)
- [`code/fcn.00402e72.c`](code/fcn.00402e72.c)
- [`code/fcn.00402f14.c`](code/fcn.00402f14.c)
- [`code/fcn.004031ba.c`](code/fcn.004031ba.c)
- [`code/fcn.004032c2.c`](code/fcn.004032c2.c)
- [`code/fcn.00403abe.c`](code/fcn.00403abe.c)
- [`code/fcn.00403d94.c`](code/fcn.00403d94.c)
- [`code/fcn.004043ac.c`](code/fcn.004043ac.c)
- [`code/fcn.00404bd0.c`](code/fcn.00404bd0.c)
- [`code/fcn.00404cde.c`](code/fcn.00404cde.c)
- [`code/fcn.00405414.c`](code/fcn.00405414.c)
- [`code/fcn.004058e3.c`](code/fcn.004058e3.c)
- [`code/fcn.00405abe.c`](code/fcn.00405abe.c)
- [`code/fcn.00405d89.c`](code/fcn.00405d89.c)
- [`code/fcn.00405f83.c`](code/fcn.00405f83.c)
- [`code/fcn.00405ffc.c`](code/fcn.00405ffc.c)
- [`code/fcn.004061a2.c`](code/fcn.004061a2.c)
- [`code/fcn.0040627e.c`](code/fcn.0040627e.c)
- [`code/fcn.00406310.c`](code/fcn.00406310.c)
- [`code/fcn.004063d2.c`](code/fcn.004063d2.c)
- [`code/fcn.00406644.c`](code/fcn.00406644.c)
- [`code/fcn.0040671a.c`](code/fcn.0040671a.c)
- [`code/fcn.0040687d.c`](code/fcn.0040687d.c)
- [`code/fcn.0040690b.c`](code/fcn.0040690b.c)

## Behavioral Analysis

Based on the analysis of the decompiled code and accompanying metadata, here is a technical summary of the binary's behavior.

### Core Functionality and Purpose
The binary functions as a **software installer or setup wizard**, likely utilizing the NSIS (Nullsoft Script Installer) framework or a similar installation engine. The code is designed to manage the complexities of installing software on Windows, including file extraction, integrity verification, registry configuration, and UI state management.

### Key Behaviors & Observed Techniques

*   **File Integrity Verification:**
    *   The function `fcn.00402f14` performs a detailed integrity check on files before they are "installed." 
    *   It utilizes an internal routine (`fcn.0040687d`), which is a standard **CRC32 checksum** implementation (identified by the polynomial `0xedb88320`).
    *   If the check fails, it displays a specific error message regarding "incomplete download" or "damaged media," which is characteristic of an installer routine.

*   **File System and Path Manipulation:**
    *   The code extensively interacts with the file system to manage temporary files (e.g., appending `.tmp` extensions).
    *   It dynamically resolves and manages paths using `GetTempPathW`, `GetSystemDirectoryW`, and `GetWindowsDirectoryW`.
    *   It handles complex path logic, including resolving relative paths and environment variables via `ExpandEnvironmentStringsW`.

*   **Registry Interaction:**
    *   The code contains numerous calls to `RegSetValueExW`, `RegQueryValueExW`, and `RegDeleteValueW`. 
    *   These are used for configuring software preferences or system integrations during the installation process.

*   **User Interface (UI) Management:**
    *   A significant portion of `fcn.00401434` is a large switch-case block handling UI updates, such as updating progress bars, changing window text, and managing dialog box states.
    *   It uses `SendMessageW` and `SendMessageTimeoutW` to communicate with UI elements (e.g., showing "Cancel" or "Retry" options).

*   **Environment Configuration:**
    *   The entry point (`entry0`) includes logic to set environment variables (e.g., the `TEMP` variable) to ensure the installation environment is consistent across different systems.

### Summary of Risk Profile
*   **Malicious Intent:** The code itself exhibits behavior typical of a **legitimate installer**. It does not contain direct evidence of process injection, unauthorized network communication, or common anti-debugging "packer" tricks.
*   **Dual-Use Potential:** While the functionality is consistent with an installer, this type of "installer engine" can be used as a wrapper for malware (a "dropper"). The integrity checks and file-moving routines are standard for installers but also serve to ensure that malicious payloads are unpacked and moved correctly.
*   **Technical Note:** The presence of `NSIS_Error` strings and the specific manner in which it handles `.tmp` files strongly suggest this is a compiled NSIS script.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The extensive UI management (progress bars, dialog boxes) and the use of standard installer routines allow the binary to blend in with legitimate software installation processes. |
| T1112 | Modify Registry | The presence of `RegSetValueExW`, `RegQueryValueExW`, and `RegDeleteValueW` indicates the binary modifies registry settings for configuration or integration. |
| T1134 | Modify Environment Variables | The entry point includes specific logic to modify environment variables, such as the `TEMP` path, to ensure a consistent execution environment. |
| T1083 | File and Directory Discovery | The usage of `GetSystemDirectoryW`, `GetWindowsDirectoryW`, and `ExpandEnvironmentStringsW` indicates the binary is programmatically discovering system paths for file operations. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, there are **no specific, high-fidelity Indicators of Compromise (IOCs)** such as hardcoded IP addresses, malicious domains, or unique file hashes in the data provided.

The findings suggest a generic installer tool rather than a specific piece of active malware infrastructure. Below is the categorization based on your requirements:

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   **None.** (The report mentions "Registry Interaction" and "Path Manipulation," but it refers to standard Windows API calls—e.g., `GetTempPathW`, `RegSetValueExW`—rather than specific, hardcoded malicious paths or keys).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified. (The string "0xedb88320" is a standard CRC32 polynomial constant and not a file hash).

### **Other artifacts**
*   **Framework/Tooling:** NSIS (Nullsoft Script Installer) - The report notes the presence of `NSIS_Error` strings and common behavior consistent with an NSIS-based installer. 
    *   *Note: While this identifies the "wrapper" used, it is not a specific IOC for a particular threat actor without a unique script signature.*
*   **Common API Imports:** A large list of standard Win32 API functions (e.g., `CreateProcessW`, `ShellExecuteExW`, `WriteFile`) was identified. These are common to both legitimate software and malware and do not serve as specific IOCs in this context.

---
**Analyst Note:** The behavior description indicates a "Dual-Use" scenario. While the binary functions as an installer, it lacks unique identifiers (like C2 addresses or unique Mutexes) that would allow for pinpointing a specific campaign. It is likely part of a generic toolkit or a standard software deployment script.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper
3. **Confidence**: Medium

**Key evidence**:
*   **Wrapper Functionality:** The sample exhibits the characteristics of a standard NSIS installer, which is commonly used by threat actors as a "wrapper" to unpack and execute secondary payloads while masquerading as legitimate software installation.
*   **Lack of Specific Indicators:** There are no hardcoded C2 domains, IP addresses, or unique mutexes provided in the report, making it impossible to attribute the sample to a specific known campaign (e.g., Emotet).
*   **Dual-Use Behavior:** The analysis identifies classic "dropper" behaviors—such as file integrity checks (CRC32), environment variable manipulation, and multi-stage file handling—which are standard for both legitimate software installers and malicious first-stage loaders.
