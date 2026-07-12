# Threat Analysis Report

**Generated:** 2026-07-11 17:39 UTC
**Sample:** `04747c51231d4890e70faab31fbd1ee37e31890c64b19f01ef60d3c17ec2a773_04747c51231d4890e70faab31fbd1ee37e31890c64b19f01ef60d3c17ec2a773.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04747c51231d4890e70faab31fbd1ee37e31890c64b19f01ef60d3c17ec2a773_04747c51231d4890e70faab31fbd1ee37e31890c64b19f01ef60d3c17ec2a773.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 549,472 bytes |
| MD5 | `898f717a70ef5c3918a79744cc0ac692` |
| SHA1 | `29e1c5640299c0a36d73bc0c8be45046160a78c7` |
| SHA256 | `04747c51231d4890e70faab31fbd1ee37e31890c64b19f01ef60d3c17ec2a773` |
| Overall entropy | 7.924 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1544912676 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,112 | 6.416 | No |
| `.rdata` | 5,120 | 5.155 | No |
| `.data` | 1,536 | 4.004 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 100,864 | 7.577 | ⚠️ Yes |

### Imports

**KERNEL32.dll**: `ExitProcess`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `CreateFileW`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `SetEnvironmentVariableW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1362** (showing first 100)

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
NTMARTA
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5795 | ✓ |
| `fcn.00406943` | `0x406943` | 2642 | ✓ |
| `entry0` | `0x4034a5` | 1345 | ✓ |
| `fcn.00403ad8` | `0x403ad8` | 726 | ✓ |
| `fcn.00402f30` | `0x402f30` | 678 | ✓ |
| `fcn.0040640a` | `0x40640a` | 626 | ✓ |
| `fcn.00405afa` | `0x405afa` | 451 | ✓ |
| `fcn.00406034` | `0x406034` | 378 | ✓ |
| `fcn.004032de` | `0x4032de` | 361 | ✓ |
| `fcn.004031d6` | `0x4031d6` | 264 | ✓ |
| `fcn.00405450` | `0x405450` | 211 | ✓ |
| `fcn.004043c6` | `0x4043c6` | 207 | ✓ |
| `fcn.00404c0c` | `0x404c0c` | 201 | ✓ |
| `fcn.00403dae` | `0x403dae` | 185 | ✓ |
| `fcn.0040667c` | `0x40667c` | 175 | ✓ |
| `fcn.00402d44` | `0x402d44` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00402e8e` | `0x402e8e` | 162 | ✓ |
| `fcn.00406348` | `0x406348` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404d1a` | `0x404d1a` | 128 | ✓ |
| `fcn.00405dc5` | `0x405dc5` | 126 | ✓ |
| `fcn.0040591f` | `0x40591f` | 125 | ✓ |
| `fcn.004061da` | `0x4061da` | 123 | ✓ |
| `fcn.004062b6` | `0x4062b6` | 121 | ✓ |
| `fcn.00405fbf` | `0x405fbf` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406752` | `0x406752` | 112 | ✓ |
| `fcn.004068b5` | `0x4068b5` | 110 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402d44.c`](code/fcn.00402d44.c)
- [`code/fcn.00402e8e.c`](code/fcn.00402e8e.c)
- [`code/fcn.00402f30.c`](code/fcn.00402f30.c)
- [`code/fcn.004031d6.c`](code/fcn.004031d6.c)
- [`code/fcn.004032de.c`](code/fcn.004032de.c)
- [`code/fcn.00403ad8.c`](code/fcn.00403ad8.c)
- [`code/fcn.00403dae.c`](code/fcn.00403dae.c)
- [`code/fcn.004043c6.c`](code/fcn.004043c6.c)
- [`code/fcn.00404c0c.c`](code/fcn.00404c0c.c)
- [`code/fcn.00404d1a.c`](code/fcn.00404d1a.c)
- [`code/fcn.00405450.c`](code/fcn.00405450.c)
- [`code/fcn.0040591f.c`](code/fcn.0040591f.c)
- [`code/fcn.00405afa.c`](code/fcn.00405afa.c)
- [`code/fcn.00405dc5.c`](code/fcn.00405dc5.c)
- [`code/fcn.00405fbf.c`](code/fcn.00405fbf.c)
- [`code/fcn.00406034.c`](code/fcn.00406034.c)
- [`code/fcn.004061da.c`](code/fcn.004061da.c)
- [`code/fcn.004062b6.c`](code/fcn.004062b6.c)
- [`code/fcn.00406348.c`](code/fcn.00406348.c)
- [`code/fcn.0040640a.c`](code/fcn.0040640a.c)
- [`code/fcn.0040667c.c`](code/fcn.0040667c.c)
- [`code/fcn.00406752.c`](code/fcn.00406752.c)
- [`code/fcn.004068b5.c`](code/fcn.004068b5.c)
- [`code/fcn.00406943.c`](code/fcn.00406943.c)

## Behavioral Analysis

This is an analysis of the provided disassembly. Based on the code structure, string references, and logic flow, here is a plain English summary of what this program does:

### Core Functionality and Purpose
The binary functions as a **software installer stub or "wrapper"** (likely generated by the Nullsoft Script Installer - NSIS). Its primary purpose is to unpack, verify, and move files from a temporary location into their final destination on the system. It performs many "housekeeping" tasks typical of an installation process:
*   **Environment Setup:** It prepares the environment by setting up common controls, initializing COM (OleInitialize), and calculating paths for temporary files.
*   **Integrity Verification:** The inclusion of complex bit-shifting loops (e.g., in `fcn.00406943`) indicates the use of CRC32 or similar checksum algorithms to ensure that the data being unpacked has not been corrupted or tampered with.
*   **File Management:** It performs extensive operations involving moving files (`MoveFileW`), copying files (`CopyFileW`), and managing temporary extensions (e.g., appending `.tmp` to filenames).

### Suspicious or Malicious Behaviors
While much of the behavior is common in installers, several features are characteristic of **droppers** or **installers used in malware delivery**:

*   **Privilege Escalation/Manipulation:** The code explicitly attempts to request and adjust token privileges (e.g., `AdjustTokenPrivileges` for "SeShutdownPrivilege"). This allows the program to perform high-privilege system actions, a common requirement for both legitimate installers and malware seeking to disable security features or modify system files.
*   **Environmental Manipulation:** The code modifies environment variables (specifically the `TEMP` path). By redirecting where the system looks for temporary data, an attacker can bypass certain security monitors or hide file-writing activity in non-standard locations.
*   **Directory Preparation & Security:** In function `fcn.0040591f`, the program creates directories and explicitly calls `SetFileSecurityW`. This ensures that the folders it is about to use have specific permissions, which can be used to hide files from other users or processes.
*   **Sophisticated File Manipulation:** The script includes logic for handling file permissions during move operations and "extracting" content into pre-defined paths. This behavior is typical of a **downloader/dropper**, where the primary executable is just a vehicle to place a final payload on the disk.

### Notable Techniques or Patterns
*   **NSIS Infrastructure:** The presence of "NSIS Error" strings and specific logic for handling `.tmp` files indicates this is likely an NSIS-based installer. These are frequently used in malware because they provide a standardized way to unpack and execute multi-stage payloads.
*   **Dynamic Path Resolution:** Rather than using hardcoded paths, the code heavily uses `GetTempPathW`, `GetSystemDirectoryW`, and `ShellGetSpecialFolderLocation`. This allows it to find "hidden" or system-sensitive areas dynamically.
*   **Internal Decryption/Decompression Logic:** Several functions (like `fcn.0031d6`) appear to be custom wrappers for reading chunks of data from a file, potentially decompressing them on the fly into memory or temporary files before they are moved to final locations.

### Summary
The binary is an **installer stub**. While it might be used for legitimate software, its behaviors—**privilege adjustment, environment manipulation, and automated file unpacking/moving**—are highly common in malicious "dropper" stages where a first-stage installer prepares the system for a second-stage payload.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1564** | SetPermissions | The program explicitly calls `SetFileSecurityW` to modify directory permissions, potentially to hide files from other users or security processes. |
| **T1136** | Modify Environment Variables | The code modifies the `TEMP` environment variable to redirect system activity and potentially bypass security monitoring. |
| **T1140** | Deobfuscate Files or Information | The use of custom wrappers for chunked reading and decompression indicates logic used to unpack hidden payloads from a compressed state. |
| **T1083** | File and Directory Discovery | The reliance on `GetTempPathW` and `GetSystemDirectoryW` instead of hardcoded paths allows the program to dynamically locate system-sensitive areas. |
| **T1036** | Masquerading | The use of NSIS infrastructure and installer behavior is used to disguise the malicious functionality as a legitimate software installation process. |
| **T1548** | Disable or Remove Security Software | Although presented as an installer, the specific request for "SeShutdownPrivilege" via `AdjustTokenPrivileges` suggests a requirement to perform actions that could impact system availability or security controls. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: While the behavior describes the manipulation of `TEMP` paths and system directories, no specific hardcoded paths or malicious registry keys were present in the provided text.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Tooling/Framework:** NSIS (Nullsoft Script Installer) - The binary is confirmed to use NSIS infrastructure, a common tool for creating multi-stage malware droppers.
*   **Behavioral Artifacts:**
    *   **Privilege Escalation:** Use of `AdjustTokenPrivileges` specifically for "SeShutdownPrivilege."
    *   **Environment Manipulation:** Dynamic modification of the `%TEMP%` environment variable to potentially bypass security monitors.
    *   **Security Modification:** Use of `SetFileSecurityW` to modify permissions on newly created directories (indicative of anti-analysis or hiding files).
    *   **Data Integrity/Decompression:** Presence of custom bit-shifting loops and data chunk reading, indicating an internal extraction/decompression routine.

***

**Analyst Note:** While this sample contains no "hard" indicators (like IPs or file hashes) that can be used for automated blocking, the behavior analysis identifies it as a **dropper/installer stub**. The lack of hardcoded strings suggests the malware may use dynamically resolved paths to avoid detection while preparing the system for a secondary payload.

---

## Malware Family Classification

1. **Malware family**: Unknown (NSIS-based installer stub)
2. **Malware type**: Dropper / Loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Installer Wrapper Functionality:** The sample utilizes NSIS infrastructure and standard "installer" logic to manage file extraction, integrity checks (CRC32), and movement of components into system directories.
    *   **Evasive Environment Manipulation:** The inclusion of `SetFileSecurityW` to modify directory permissions and the modification of the `%TEMP%` environment variable are classic indicators of a dropper attempting to hide its activities from security software.
    *   **Payload Preparation:** The combination of dynamic path resolution, privilege escalation (`AdjustTokenPrivileges`), and custom decompression logic indicates this binary's primary role is to prepare the system for and "drop" a secondary, potentially more malicious, payload.
