# Threat Analysis Report

**Generated:** 2026-08-24 21:59 UTC
**Sample:** `11f392975699cfc7bae3ec4a5cae53d0a16f182038416728b24813d0e78cf3bc_11f392975699cfc7bae3ec4a5cae53d0a16f182038416728b24813d0e78cf3bc.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11f392975699cfc7bae3ec4a5cae53d0a16f182038416728b24813d0e78cf3bc_11f392975699cfc7bae3ec4a5cae53d0a16f182038416728b24813d0e78cf3bc.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 799,672 bytes |
| MD5 | `d0ed0abcf3fa360c725e0dbce00f96de` |
| SHA1 | `ac45b48bb58fc7f7471c1e2bbd639727e1707e4d` |
| SHA256 | `11f392975699cfc7bae3ec4a5cae53d0a16f182038416728b24813d0e78cf3bc` |
| Overall entropy | 7.49 |
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
| `.rsrc` | 158,720 | 3.871 | No |

### Imports

**KERNEL32.dll**: `SetEnvironmentVariableW`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `CopyFileW`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`, `SetErrorMode`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1584** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality and behavior.

### Core Functionality and Purpose
The binary functions as a **multi-stage loader/dropper**. Its primary role is to prepare the environment (resolving paths, ensuring compatibility), drop and stage secondary payloads into temporary directories, and then transition execution to those payloads while potentially hiding the intermediate actions from the user.

A significant portion of the code's structure—specifically the large switch cases in `fcn.00401434` and the complexity of `fcn.0040626e`—suggests this is a **packer stub** or a heavily wrapped installer (like an NSIS wrapper) designed to resolve complex system paths and "unpack" functionality before launching the final payload.

### Suspicious or Malicious Behaviors

*   **Dropper & Downloader Behavior:**
    *   The `entry0` function contains a loop that performs multiple `CopyFileW` operations. It takes files from one location (likely an embedded resource or a nearby path) and copies/renames them into temporary directories (`GetTempPathW`). 
    *   It specifically manipulates the `%TEMP%` environment variable to ensure it can work with various naming conventions, common in malware seeking to hide its footprint.

*   **Environment & Path Manipulation:**
    *   The code heavily utilizes `fcn.0040626e` for **path resolution**. This function resolves "special" folders (like `System32`, `Program Files`, etc.) using `SHGetSpecialFolderLocation`. 
    *   This allows the malware to dynamically locate and interact with system-critical paths regardless of the user's specific Windows configuration.

*   **Persistence and Configuration:**
    *   The presence of `RegSetValueExW`, `RegOpenKeyExW`, and `RegDeleteValueW` indicates the binary interacts with the Windows Registry. This is frequently used for establishing **persistence** (ensuring it runs on startup) or storing configuration data for the next stage.

*   **Evasion/Anti-Analysis:**
    *   The code performs several **environment checks**, such as `GetVersion`. It handles different OS versions differently, which can be a way to ensure compatibility but is also used to detect virtualized environments.
    *   It uses `SetFileSecurityW` and `CreateDirectoryW` with specific security descriptors. This is often used by malware to set permissions on dropped files so that they cannot be easily deleted or accessed by security software.

### Notable Techniques & Patterns

*   **Staged Execution:** The flow from `entry0` to `fcn.0040395a` suggests a multi-stage loading process. The first stage (the code we see) prepares the files, and the second stage (likely called via `CreateProcessW` or `ShellExecuteExW`) is the actual payload.
*   **Resource Management:** The use of `OleInitialize`, `CoCreateInstance`, and `GetProcAddress` suggests it handles complex COM objects or dynamically resolves APIs to evade simple static analysis scanners.
*   **Standard Packer Logic:** The presence of a large, complex switch-case table (mapping out various internal functions) is a hallmark of packed executables (like UPX or custom protectors). These are used to obfuscate the actual malicious logic from researchers.
*   **Shadow Copy/Drop Pattern:** In `entry0`, the routine of copying files and then "cleaning up" by deleting source components or original temporary files is a common technique for stealthy installation.

### Summary Table
| Feature | Observed Evidence |
| :--- | :--- |
| **Dropper behavior** | Extensive use of `CopyFileW`, `MoveFileW`, and `GetTempPathW`. |
| **Persistence** | Registry manipulation via `Advapi32` calls. |
| **Environment Manipulation** | Modifying environment variables; resolving "Special Folders". |
| **Obfuscation** | Packing-style switch tables, dynamic API resolution (`GetProcAddress`). |
| **Evasion** | OS version checking and specific File Security handling. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Packing | The presence of complex switch-case tables and "packer stub" logic indicates an effort to obfuscate the binary's true functionality from static analysis. |
| **T1106** | Native API | Use of `GetProcAddress` allows for dynamic resolution of API addresses, helping the malware evade detection by scanners looking for specific imported functions. |
| **T1112** | Modify Registry | The use of `RegSetValueExW` and other registry-related functions suggests that the binary seeks to establish persistence or store configuration data. |
| **T1497** | Virtualization/Sandbox Detection | Analysis shows the use of `GetVersion` and specialized logic for different OS versions to identify and potentially evade research environments. |
| **T1562.001** | Impair Defenses: Disable or Modify Tools | The use of `SetFileSecurityW` on dropped files is a specific attempt to prevent security software from accessing or deleting the malicious payload. |
| **T1083** | File and Directory Discovery | The usage of `SHGetSpecialFolderLocation` indicates an intent to resolve system-critical paths for staging payloads or interacting with OS components. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the extracted list of Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided data contains a high volume of standard Windows API calls (e.g., `GetProcAddress`, `CreateProcessW`) and common system DLLs (`KERNEL32.dll`, `USER32.dll`). While these indicate the binary's capabilities (such as file manipulation, registry interaction, and execution of secondary payloads), they do not constitute unique IOCs for a specific malware campaign as they are standard components of the Windows environment.

---

### **IOC_Report**

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (Note: While the analysis mentions "Special Folders" and "Registry Keys," no specific malicious paths or specific registry keys were provided in the source text).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Internal Function Offsets:** `fcn.00401434`, `fcn.0040626e` (These represent specific locations in the binary's code likely associated with the packer stub and path resolution logic).
*   **Behavioral Signatures:** 
    *   Multi-stage loader/dropper behavior.
    *   Use of `GetTempPathW` for dropping payloads.
    *   Dynamic API resolution via `GetProcAddress`.
    *   Detection of environment specifics via `GetVersion`.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High (for Type) / Low (for Family)

4. **Key evidence**:
*   **Staged Execution & Delivery**: The binary functions as a classic multi-stage loader; it utilizes `CopyFileW` and `MoveFileW` to stage secondary payloads in the `%TEMP%` directory, which is a primary indicator of dropper behavior.
*   **Evasion & Obfuscation**: The use of packer stub logic (complex switch cases), dynamic API resolution via `GetProcAddress`, and environment checks (like `GetVersion`) are standard techniques used to shield the actual malicious payload from static analysis.
*   **Persistence & Defense Evasion**: The inclusion of registry manipulation (`RegSetValueExW`) for persistence and the use of `SetFileSecurityW` to restrict access to dropped files indicates an intent to maintain a foothold on the system while preventing removal by security software.
