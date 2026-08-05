# Threat Analysis Report

**Generated:** 2026-08-03 12:01 UTC
**Sample:** `0cae65f8aaaa688fefaf835c28ffe775e63e7feee8baa55213dd5663a13794d9_0cae65f8aaaa688fefaf835c28ffe775e63e7feee8baa55213dd5663a13794d9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0cae65f8aaaa688fefaf835c28ffe775e63e7feee8baa55213dd5663a13794d9_0cae65f8aaaa688fefaf835c28ffe775e63e7feee8baa55213dd5663a13794d9.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 478,416 bytes |
| MD5 | `61e0ba6e41c6bea45dfd4bb64db0f08c` |
| SHA1 | `084d93c86e21bef93dfae010d231a6156e06e924` |
| SHA256 | `0cae65f8aaaa688fefaf835c28ffe775e63e7feee8baa55213dd5663a13794d9` |
| Overall entropy | 7.907 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1501547618 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.504 | No |
| `.rdata` | 5,120 | 5.146 | No |
| `.data` | 1,536 | 3.907 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 26,624 | 5.581 | No |

### Imports

**KERNEL32.dll**: `SetEnvironmentVariableW`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `CopyFileW`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`, `SetErrorMode`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1230** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495l
tQVPW
Instu`
softuW
NulluN	E
SVWj _3
Aj"A[f
D$ Ph0
D$$SPS
tVj%SSS
D$$+D$
D$,+D$$P
us9Et	
FFC;]|
8\tPV
\u f9O
69}t(j
90u'AAf
_^[t	P
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
CreateFileW
GetTempFileNameW
WriteFile
lstrcpyA
MoveFileExW
lstrcatW
GetSystemDirectoryW
GetProcAddress
GetModuleHandleA
GetExitCodeProcess
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5789 | ✓ |
| `fcn.00406937` | `0x406937` | 2183 | ✓ |
| `entry0` | `0x403350` | 1347 | ✓ |
| `fcn.0040396d` | `0x40396d` | 726 | ✓ |
| `fcn.00406281` | `0x406281` | 626 | ✓ |
| `fcn.00402ec1` | `0x402ec1` | 569 | ✓ |
| `fcn.004030fa` | `0x4030fa` | 504 | ✓ |
| `fcn.0040596d` | `0x40596d` | 451 | ✓ |
| `fcn.00405eab` | `0x405eab` | 378 | ✓ |
| `fcn.004067ef` | `0x4067ef` | 328 | ✓ |
| `fcn.004072f0` | `0x4072f0` | 216 | ✓ |
| `fcn.004052c3` | `0x4052c3` | 211 | ✓ |
| `fcn.00404a7f` | `0x404a7f` | 201 | ✓ |
| `fcn.00403c43` | `0x403c43` | 185 | ✓ |
| `fcn.004064f3` | `0x4064f3` | 175 | ✓ |
| `fcn.00402d2a` | `0x402d2a` | 173 | ✓ |
| `fcn.0040425b` | `0x40425b` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.004061bf` | `0x4061bf` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.0040726f` | `0x40726f` | 129 | ✓ |
| `fcn.00404b8d` | `0x404b8d` | 128 | ✓ |
| `fcn.00405c38` | `0x405c38` | 126 | ✓ |
| `fcn.00405792` | `0x405792` | 125 | ✓ |
| `fcn.00406051` | `0x406051` | 123 | ✓ |
| `fcn.00405e32` | `0x405e32` | 121 | ✓ |
| `fcn.0040612d` | `0x40612d` | 121 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004065c9` | `0x4065c9` | 112 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402d2a.c`](code/fcn.00402d2a.c)
- [`code/fcn.00402ec1.c`](code/fcn.00402ec1.c)
- [`code/fcn.004030fa.c`](code/fcn.004030fa.c)
- [`code/fcn.0040396d.c`](code/fcn.0040396d.c)
- [`code/fcn.00403c43.c`](code/fcn.00403c43.c)
- [`code/fcn.0040425b.c`](code/fcn.0040425b.c)
- [`code/fcn.00404a7f.c`](code/fcn.00404a7f.c)
- [`code/fcn.00404b8d.c`](code/fcn.00404b8d.c)
- [`code/fcn.004052c3.c`](code/fcn.004052c3.c)
- [`code/fcn.00405792.c`](code/fcn.00405792.c)
- [`code/fcn.0040596d.c`](code/fcn.0040596d.c)
- [`code/fcn.00405c38.c`](code/fcn.00405c38.c)
- [`code/fcn.00405e32.c`](code/fcn.00405e32.c)
- [`code/fcn.00405eab.c`](code/fcn.00405eab.c)
- [`code/fcn.00406051.c`](code/fcn.00406051.c)
- [`code/fcn.0040612d.c`](code/fcn.0040612d.c)
- [`code/fcn.004061bf.c`](code/fcn.004061bf.c)
- [`code/fcn.00406281.c`](code/fcn.00406281.c)
- [`code/fcn.004064f3.c`](code/fcn.004064f3.c)
- [`code/fcn.004065c9.c`](code/fcn.004065c9.c)
- [`code/fcn.004067ef.c`](code/fcn.004067ef.c)
- [`code/fcn.00406937.c`](code/fcn.00406937.c)
- [`code/fcn.0040726f.c`](code/fcn.0040726f.c)
- [`code/fcn.004072f0.c`](code/fcn.004072f0.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C pseudocode, here is an analysis of the binary's functionality and behavior.

### Core Functionality and Purpose
The binary functions as a **dropper or installer wrapper**. It is designed to perform "staging" activities—preparing the system environment, moving files into temporary locations, and ultimately launching a secondary payload. The presence of strings like `"NSIS Error"` and `"Installer integrity check"* suggests it is likely based on the NSIS (Nullsoft Script Installer) framework but has been modified or bundled with additional logic.

### Suspicious and Malicious Behaviors
The following behaviors are characteristic of malware used for initial infection or payload delivery:

*   **File Staging and Dropping:** 
    *   The code frequently interacts with `GetTempPathW` and `GetCurrentDirectoryW`.
    *   It performs "Rename" operations (e.g., in `fcn.00405eab`) where it moves data/files to temporary paths.
    *   In `entry0`, there is logic to identify its own path on disk, copy it (or associated components), and move them into a working directory before execution. This is a classic "dropper" technique used to hide the actual malicious payload from simple signature-based scanners until it is in a temporary folder.
*   **Privilege Escalation/Check:** 
    *   The `entry0` function calls `AdjustTokenPrivilegesW` to request `SeShutdownPrivilege`. While "Shutdown" sounds benign, this is a common method for an application to check if it is running with Administrative privileges before attempting more intrusive operations.
*   **Persistence and Configuration via Registry:** 
    *   The binary contains extensive logic for interacting with the Windows Registry (`RegQueryValueExW`, `RegEnumKeyW`, `RegSetValueExW`). While this could be for a legitimate installer, it is also used by malware to ensure persistence (e.g., "Run" keys) or to store configuration data for the payload.
*   **Environment Manipulation:** 
    *   The use of `SetFileSecurityW` and `CreateDirectoryW` suggests the binary is preparing specific folders and setting permissions to ensure that the dropped payload can execute without being blocked by system permissions.

### Notable Techniques and Patterns
*   **Control Flow Obfuscation (Switch Table):** 
    *   The function `fcn.00401434` utilizes a massive switch-table structure (covering over 68 cases). This is a common obfuscation technique used to "flatten" the control flow, making it difficult for an analyst to follow the logical progression of the code by looking at the assembly alone.
*   **Resource Extraction:** 
    *   The heavy reliance on `OleInitialize`, `SHGetFileInfoW`, and `LoadLibraryExW` suggests that much of the payload's functionality is stored as embedded resources or within encrypted blobs inside the binary, which are then "unpacked" during execution.
*   **Self-Reference Logic:** 
    *   The code retrieves its own path/name (`GetModuleFileNameW`) and compares it against other strings to determine logic branches. This is often used in multi-stage loaders to determine if it is running as a "stub" or the final payload.

### Summary Conclusion
This binary is likely a **malicious downloader/dropper**. It is designed to wrap an installation process, but its heavy use of file moving into temporary directories, privilege checks, and obfuscated control flow indicates that its primary purpose is to prepare a system for a secondary payload while evading basic security detections.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Dropper | The binary moves files to temporary locations and extracts embedded resources to hide and prepare a secondary payload for execution. |
| T1068 | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivilegesW` indicates an attempt to check for or acquire administrative privileges to perform more intrusive operations. |
| T1112 | Modify Registry | The binary utilizes multiple registry functions (`RegQueryValueExW`, `RegEnumKeyW`, `RegSetValueExW`) to store configuration data and potentially establish persistence. |

---

## Indicators of Compromise

Based on the provided string extraction and behavioral analysis, here are the identified Indicators of Compromise (IOCs). 

Note: As per your instructions, standard Windows API functions (e.g., `GetTempPathW`, `CreateProcessW`) and common library filenames have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   **Note:** While the behavioral analysis mentions the use of "temporary folders" and "Registry keys" for persistence, no specific hardcoded paths or registry keys (e.g., `HKLM\...\Run`) were provided in the source text.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Internal Function Offsets:** The following specific offsets are noted as locations of malicious behavior (File staging and Control Flow Obfuscation) and can be used for YARA rules or forensic comparison:
    *   `0x405eab` (Function associated with data/file moving to temporary paths).
    *   `0x401434` (Function utilizing a large switch-table structure for control flow obfuscation).
*   **Suspicious Strings:** The presence of `"NSIS Error"` and `"Installer integrity check"` indicates the binary utilizes or mimics the Nullsoft Script Installer framework.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Staging and Extraction:** The binary exhibits classic "dropper" behavior by moving files to temporary directories (`GetTempPathW`) and extracting embedded resources to hide a secondary payload from signature-based detection.
    *   **Obfuscation Techniques:** The use of a massive switch-table (68+ cases) for control flow flattening indicates an intentional effort to hinder manual analysis and automate detection by security tools.
    *   **System Preparation:** The combination of privilege checks (`AdjustTokenPrivilegesW`) and registry interaction suggests the binary is designed to secure its environment, establish persistence, and ensure the subsequent payload can run with elevated permissions.
