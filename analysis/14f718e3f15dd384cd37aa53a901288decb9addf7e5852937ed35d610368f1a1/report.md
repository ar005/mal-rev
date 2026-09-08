# Threat Analysis Report

**Generated:** 2026-09-06 13:50 UTC
**Sample:** `14f718e3f15dd384cd37aa53a901288decb9addf7e5852937ed35d610368f1a1_14f718e3f15dd384cd37aa53a901288decb9addf7e5852937ed35d610368f1a1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14f718e3f15dd384cd37aa53a901288decb9addf7e5852937ed35d610368f1a1_14f718e3f15dd384cd37aa53a901288decb9addf7e5852937ed35d610368f1a1.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 1,327,808 bytes |
| MD5 | `71a470805c9aea2600482d0dce53dc58` |
| SHA1 | `48f56bebd2f68e4102927b0bbd441f0dadc2eca6` |
| SHA256 | `14f718e3f15dd384cd37aa53a901288decb9addf7e5852937ed35d610368f1a1` |
| Overall entropy | 7.201 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1501547632 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.423 | No |
| `.rdata` | 5,120 | 5.146 | No |
| `.data` | 1,536 | 3.907 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 359,936 | 3.392 | No |

### Imports

**KERNEL32.dll**: `SetEnvironmentVariableW`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `CopyFileW`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`, `SetErrorMode`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **2307** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495L
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
WaitForSingleObject
KERNEL32.dll
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5789 | ✓ |
| `fcn.004067a7` | `0x4067a7` | 2642 | ✓ |
| `entry0` | `0x40333d` | 1347 | ✓ |
| `fcn.0040395a` | `0x40395a` | 726 | ✓ |
| `fcn.0040626e` | `0x40626e` | 626 | ✓ |
| `fcn.00402ec1` | `0x402ec1` | 569 | ✓ |
| `fcn.004030fa` | `0x4030fa` | 485 | ✓ |
| `fcn.0040595a` | `0x40595a` | 451 | ✓ |
| `fcn.00405e98` | `0x405e98` | 378 | ✓ |
| `fcn.004052b0` | `0x4052b0` | 211 | ✓ |
| `fcn.00404a6c` | `0x404a6c` | 201 | ✓ |
| `fcn.00403c30` | `0x403c30` | 185 | ✓ |
| `fcn.004064e0` | `0x4064e0` | 175 | ✓ |
| `fcn.00402d2a` | `0x402d2a` | 173 | ✓ |
| `fcn.00404248` | `0x404248` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.004061ac` | `0x4061ac` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404b7a` | `0x404b7a` | 128 | ✓ |
| `fcn.00405c25` | `0x405c25` | 126 | ✓ |
| `fcn.0040577f` | `0x40577f` | 125 | ✓ |
| `fcn.0040603e` | `0x40603e` | 123 | ✓ |
| `fcn.00405e1f` | `0x405e1f` | 121 | ✓ |
| `fcn.0040611a` | `0x40611a` | 121 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004065b6` | `0x4065b6` | 112 | ✓ |
| `fcn.00406719` | `0x406719` | 110 | ✓ |
| `fcn.00405383` | `0x405383` | 108 | ✓ |
| `fcn.004058ae` | `0x4058ae` | 100 | ✓ |

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
- [`code/fcn.0040395a.c`](code/fcn.0040395a.c)
- [`code/fcn.00403c30.c`](code/fcn.00403c30.c)
- [`code/fcn.00404248.c`](code/fcn.00404248.c)
- [`code/fcn.00404a6c.c`](code/fcn.00404a6c.c)
- [`code/fcn.00404b7a.c`](code/fcn.00404b7a.c)
- [`code/fcn.004052b0.c`](code/fcn.004052b0.c)
- [`code/fcn.00405383.c`](code/fcn.00405383.c)
- [`code/fcn.0040577f.c`](code/fcn.0040577f.c)
- [`code/fcn.004058ae.c`](code/fcn.004058ae.c)
- [`code/fcn.0040595a.c`](code/fcn.0040595a.c)
- [`code/fcn.00405c25.c`](code/fcn.00405c25.c)
- [`code/fcn.00405e1f.c`](code/fcn.00405e1f.c)
- [`code/fcn.00405e98.c`](code/fcn.00405e98.c)
- [`code/fcn.0040603e.c`](code/fcn.0040603e.c)
- [`code/fcn.0040611a.c`](code/fcn.0040611a.c)
- [`code/fcn.004061ac.c`](code/fcn.004061ac.c)
- [`code/fcn.0040626e.c`](code/fcn.0040626e.c)
- [`code/fcn.004064e0.c`](code/fcn.004064e0.c)
- [`code/fcn.004065b6.c`](code/fcn.004065b6.c)
- [`code/fcn.00406719.c`](code/fcn.00406719.c)
- [`code/fcn.004067a7.c`](code/fcn.004067a7.c)

## Behavioral Analysis

Based on the disassembly provided, this binary appears to be a **multi-stage installer or a dropper**. While it contains many components common to legitimate software installers (such as those using the NSIS framework), several behaviors are common in malware designed to drop and execute a secondary payload.

### Core Functionality
The primary purpose of this code is to prepare an environment, verify the integrity of files on disk, and orchestrate the installation or execution of subsequent components. It acts as a "wrapper" that handles system interactions like directory creation, registry updates, and file moving before launching the final payload.

### Suspicious & Malicious Behaviors
The following behaviors are characteristic of droppers or installers used in malware campaigns:

*   **Dropping and Moving Files:**
    *   The code extensively uses `GetTempPathW`, `CreateDirectoryW`, `MoveFileW`, and `CopyFileW`. It appears to unpack or move files into temporary directories before execution. 
    *   It specifically performs "cleanup" operations on file names (e.g., removing `.tmp` or other extensions) before launching processes.
*   **Privilege Escalation:**
    *   The code calls `AdjustTokenPrivileges` to request `SeShutdownPrivilege`. While often found in legitimate installers that require a reboot, this is also used by malware to gain higher privileges or prepare the system for state changes.
*   **Registry Manipulation:**
    *   There are numerous calls to `RegOpenKeyExW`, `RegCreateKeyExW`, and `RegSetValueExW`. This indicates the program is attempting to modify system configurations, create persistence, or change software settings during its execution.
*   **Integrity Checking (Self-Protection/Validation):**
    *   The function `fcn.0040395a` performs an "integrity check" on a file before it can be launched. It uses a complex arithmetic routine (`fcn.00406719`) which resembles a CRC or checksum algorithm to ensure the payload hasn't been tampered with (or to verify that the installer is running in a specific environment).
*   **Environment Manipulation:**
    *   The code explicitly manipulates environment variables and system paths via `GetSystemDirectoryW` and `SetEnvironmentVariableW`, which can be used to hijack search paths for DLLs or other binaries.

### Notable Techniques & Patterns
*   **NSIS Framework Indicators:** The presence of the string `nsis.sf.net` and specific logic for handling "Installer integrity check" failures suggests this is based on the **Nullsoft Script Installer (NSIS)**. This is common in both legitimate software distribution and malware where a script-based installer is used to simplify the deployment of secondary payloads.
*   **Dynamic Module Loading:** The use of `LoadLibraryExW` and `GetModuleHandleW` followed by calls to `GetProcAddress` indicates that the binary loads functionality at runtime, often used to hide the true capabilities of the code until execution starts.
*   **Complex Data Processing/Decoding:** Function `fcn.004067a7` contains complex bitwise operations and loops. This is a common pattern for **decompressing or decrypting data** in memory before it is used by the main logic, suggesting that some parts of the payload are not stored in plaintext on disk.
*   **Resource Handling:** The code includes significant logic to manage internal resources (strings/icons), likely using a table-driven approach to build UI messages dynamically.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in the provided analysis to the relevant MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The process of moving files into temporary directories and "cleaning up" names (removing .tmp) is used to hide the true nature or presence of the payload. |
| **T1068** | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` to request `SeShutdownPrivilege` indicates an attempt to gain elevated system privileges. |
| **T1112** | Modify Registry | The repeated calls to `RegOpenKeyExW`, `RegCreateKeyExW`, and `RegSetValueExW` indicate attempts to establish persistence or modify system configuration. |
| **T1497** | Virtualization/Sandbox Detection | The complex integrity check (`fcn.0040395a`) used to verify the environment before execution is a common tactic to evade automated analysis. |
| **T1123** | Modify Operating System Architecture | (Alternatively, part of Defense Evasion) Manipulation of system paths and environment variables via `SetEnvironmentVariableW` can be used to alter how the OS interprets commands or loads binaries. |
| **T1027** | Obfuscated Services | The use of complex bitwise operations for decryption/decompression and dynamic loading (`GetProcAddress`) are techniques used to hide functionality from static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Standard Windows API calls (e.g., `GetProcAddress`, `CreateFileW`) and standard system DLLs have been excluded as they are common to both legitimate and malicious software.

### **IP addresses / URLs / Domains**
*   **nsis.sf.net** (Identified in the behavioral analysis; associated with the Nullsoft Script Installer framework).

### **File paths / Registry keys**
*   *None identified.* (The analysis notes that registry keys and temporary paths are manipulated, but no specific malicious paths or hardcoded registry keys were provided in the string dump.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None found.*

### **Other artifacts**
*   **Framework Identification:** NSIS (Nullsoft Script Installer)
*   **Techniques Detected:** 
    *   **Integrity Checking:** The binary performs internal integrity checks (`fcn.0040395a`) to verify the payload before execution.
    *   **Dynamic Module Loading:** Utilization of `LoadLibraryExW` and `GetProcAddress` to load functionality at runtime.
    *   **Data Decryption/Decompression:** Presence of complex bitwise operations in `fcn.004067a7` suggesting the use of an "in-memory" unpacking routine.
    *   **Privilege Escalation:** Intentional calls to `AdjustTokenPrivileges` for `SeShutdownPrivilege`.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-stage Delivery Logic:** The sample exhibits classic dropper behavior by utilizing `GetTempPathW`, `MoveFileW`, and `CopyFileW` to move payloads into temporary directories while "cleaning up" filenames (e.g., removing `.tmp` extensions) before execution.
*   **Anti-Analysis & Evasion:** The presence of integrity checks (`fcn.0040395a`), potential sandbox detection, and complex decryption/decompression routines indicates it is designed to shield the actual payload from static analysis.
*   **Infrastructure for Persistence:** The use of `AdjustTokenPrivileges`, numerous registry modifications, and environment variable manipulation are standard techniques used by loaders to ensure the primary malware can establish persistence and maintain elevated privileges.
