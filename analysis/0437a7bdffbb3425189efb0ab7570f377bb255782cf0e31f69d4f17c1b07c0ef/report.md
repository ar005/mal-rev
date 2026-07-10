# Threat Analysis Report

**Generated:** 2026-07-09 21:28 UTC
**Sample:** `0437a7bdffbb3425189efb0ab7570f377bb255782cf0e31f69d4f17c1b07c0ef_0437a7bdffbb3425189efb0ab7570f377bb255782cf0e31f69d4f17c1b07c0ef.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0437a7bdffbb3425189efb0ab7570f377bb255782cf0e31f69d4f17c1b07c0ef_0437a7bdffbb3425189efb0ab7570f377bb255782cf0e31f69d4f17c1b07c0ef.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 1,059,664 bytes |
| MD5 | `586fd4df94683f5177e9ae00a926372f` |
| SHA1 | `e386b0795b60734bf7393ccee5f306058c247111` |
| SHA256 | `0437a7bdffbb3425189efb0ab7570f377bb255782cf0e31f69d4f17c1b07c0ef` |
| Overall entropy | 7.963 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1517284661 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,112 | 6.416 | No |
| `.rdata` | 5,120 | 5.144 | No |
| `.data` | 1,536 | 4.004 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 17,920 | 1.815 | No |

### Imports

**KERNEL32.dll**: `ExitProcess`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `CreateFileW`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `SetEnvironmentVariableW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **2469** (showing first 100)

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

Based on the provided disassembly and strings, here is a summary of the behavior of this binary:

### **Core Functionality and Purpose**
The binary functions as a **multi-stage installer or dropper**, likely using the **NSIS (Nullsoft Script Installer)** framework. Its primary purpose is to validate its own integrity, unpack/extract components into temporary directories, and configure system settings before executing the final payload.

### **Suspicious or Malicious Behaviors**
While much of the code resembles standard installation behavior, several patterns are common in malware droppers:

*   **Dropper/Extractor Behavior:** The binary heavily utilizes `GetTempPathW` to identify a working directory and uses `MoveFileExW`, `CopyFileW`, and `CreateFileW` to move or create files within the `%TEMP%` folder. This is a classic technique for "staging" a payload before execution.
*   **Integrity Verification:** The function `fcn.00406943` contains complex bit-shifting logic and look-up tables, which are characteristic of **CRC32 or custom hashing algorithms**. It ensures the installer's files haven't been tampered with before proceeding to extraction.
*   **Registry Manipulation:** The code frequently uses `RegOpenKeyExW`, `RegSetValueExW`, and `RegQueryValueExW`. These are used to create persistent configuration settings or modify system behavior upon installation.
*   **Privilege Escalation/Manipulation:** In the `entry0` function, there is a specific routine that calls `OpenProcessToken`, `LookupPrivilegeValueW` (specifically seeking `"SeShutdownPrivilege"`), and `AdjustTokenPrivileges`. This indicates an attempt to elevate privileges or modify token permissions.
*   **System Interaction:** The use of `ShellExecuteExW` and `CreateProcessW` suggests that after the files are moved/extracted, the binary launches the next stage of the application (or payload).

### **Notable Techniques & Patterns**
*   **NSIS Framework Indicators:** The presence of "NSIS Error" messages and specific logic for handling `.tmp` files confirms it is built using NSIS. This framework is frequently used by both legitimate software and malware because it provides a powerful way to bundle and execute installers.
*   **File System Navigation:** Extensive use of `GetShortPathNameW`, `GetFullPathNameW`, and `SearchPathW` allows the binary to resolve relative paths and "hide" its actual file locations during the extraction process.
*   **Dynamic Library Loading:** The function `fcn.00406752` implements a routine for loading DLLs dynamically by constructing strings, which can be used to delay-load functionality or evade static analysis of common API imports.
*   **Environment Manipulation:** The binary checks and potentially updates the `TEMP` environment variable using `SetEnvironmentVariableW`, ensuring it has a controlled environment to perform its file operations.

### **Summary for Analyst**
This is likely an **installer/downloader**. While the code contains many "noisy" UI-related functions (typical of installers), the specific pattern of **validating local files via CRC, staging items in `%TEMP%`, and requesting higher privileges** are significant indicators that this binary is designed to prepare a system for another execution. It should be treated as a potential dropper; the final payload being "unpacked" or "moved" by this installer is likely the primary threat.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1562 | Impair Defenses | The use of complex hashing/CRC32 checks ensures that files have not been tampered with or modified by security tools before execution. |
| T1036 | Masquerading | Utilizing the `%TEMP%` folder for staging and moving files allows the binary to blend in with legitimate system activity. |
| T1112 | Modify Registry | The use of `RegSetValueExW` indicates an attempt to modify registry keys for configuration or persistence purposes. |
| T1068 | Exploitation for Privilege Escalation | The specific request for "SeShutdownPrivilege" via `AdjustTokenPrivileges` indicates a deliberate attempt to obtain higher system privileges. |
| T1204 | User Execution | The use of `CreateProcessW` and `ShellExecuteExW` marks the final stage where the unpacked payload is executed. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the identified Indicators of Compromise (IOCs). 

Note: Because the provided text contains a high volume of standard Windows API imports (e.g., `GetTempPathW`, `CreateFileW`) and general descriptive analysis rather than specific hardcoded values (like unique IP addresses or specific file paths), many "strings" were excluded as they are common to thousands of legitimate applications.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   **%TEMP%** (Note: Identified as the primary staging area for payloads, though this is a standard system variable).
*   **"SeShutdownPrivilege"** (Identified as a specific privilege requested via `LookupPrivilegeValueW` during the escalation phase).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **NSIS Framework:** The binary utilizes the Nullsoft Script Installer (NSIS) framework, commonly used to wrap and deploy payloads.
*   **Function Offsets/Logic:** 
    *   `fcn.00406943`: Identified as a non-standard implementation of CRC32 or custom hashing for integrity checks.
    *   `fcn.00406752`: Identified as a dynamic library loading routine used to hide the primary imports from static analysis.
*   **Behavioral Pattern:** The sequence of `GetTempPathW` $\rightarrow$ `MoveFileExW` $\rightarrow$ `CreateProcessW` indicates a multi-stage dropper behavior intended to move an executable into a temporary directory before execution.

---

## Malware Family Classification

1. **Malware family**: Unknown (NSIS-wrapped)
2. **Malware type**: Dropper
3. **Confidence**: High

**Key evidence**:
*   **Staging Behavior:** The binary exhibits classic dropper characteristics by utilizing `GetTempPathW`, `MoveFileExW`, and `CopyFileW` to move components into the `%TEMP%` directory before execution, a common technique for "hiding" payloads in plain sight.
*   **Evasion & Integrity Checks:** The inclusion of custom CRC32/hashing logic (`fcn.00406943`) and dynamic library loading (`fcn.00406752`) indicates an intentional effort to verify that the payload hasn't been modified by security software and to hide imports from static analysis.
*   **Privilege Escalation:** The specific request for `SeShutdownPrivilege` via `AdjustTokenPrivileges` suggests the loader is attempting to gain higher system permissions to ensure the final stage of the attack can execute successfully.
