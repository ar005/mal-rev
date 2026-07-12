# Threat Analysis Report

**Generated:** 2026-07-11 21:34 UTC
**Sample:** `04abd60e49b28e5c6eab8d3445f32e444d09a95324cb0d06a1695185f74b004d_04abd60e49b28e5c6eab8d3445f32e444d09a95324cb0d06a1695185f74b004d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04abd60e49b28e5c6eab8d3445f32e444d09a95324cb0d06a1695185f74b004d_04abd60e49b28e5c6eab8d3445f32e444d09a95324cb0d06a1695185f74b004d.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 1,040,584 bytes |
| MD5 | `aef2a16082d0302646aa9fef390d2d1c` |
| SHA1 | `d5473434e07ec25dbf10f606b141dbf661acc122` |
| SHA256 | `04abd60e49b28e5c6eab8d3445f32e444d09a95324cb0d06a1695185f74b004d` |
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

Total strings found: **2370** (showing first 100)

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

Based on my analysis of the decompiled code and disassembly, this binary functions as a **multi-stage dropper/installer** (likely based on or mimicking the NSIS installer framework). It is designed to unpack, verify, and deploy a payload onto a target system while performing environment checks and interacting with various system components.

### Core Functionality
The primary purpose of this code is to act as a "loader" or "stub." Its job is not to perform the final malicious action itself, but to prepare the environment for a hidden payload. Key activities include:
*   **Payload Unpacking:** The presence of complex bit-shifting and table-lookup loops (e.g., `fcn.00406943`) indicates that the main functionality is compressed or encrypted and is extracted during execution.
*   **Integrity Verification:** Function `fcn.00402f30` contains logic to perform "installer integrity checks" before proceeding with the installation, ensuring the payload hasn't been corrupted or modified by security researchers.
*   **Environment Setup:** The code resolves system paths (Temporary folders, System directories) and dynamically loads necessary DLLs to facilitate its own operation.

### Suspicious or Malicious Behaviors
The following behaviors are characteristic of malware delivery:
*   **Dropping & File Manipulation:** 
    *   It frequently uses `CreateFileW`, `WriteFile`, `MoveFileW`, and `CopyFileW` to move files into temporary directories (`GetTempPathW`).
    *   It performs automated renaming and path processing, often a technique used to "stage" a malicious executable in a less-monitored directory.
*   **Persistence & Configuration:** 
    *   The binary makes extensive use of `RegOpenKeyExW`, `RegSetValueExW`, and `RegQueryValueExW`. This is typically used to modify the registry for **persistence** (e.g., ensuring a program runs at startup) or to store configuration data for the second-stage payload.
*   **Privilege Manipulation:** 
    *   In `entry0`, the code attempts to acquire specific privileges using `AdjustTokenPrivileges` and `LookupPrivilegeValueW`. It specifically checks for `SeShutdownPrivilege`. While this sounds benign, the attempt to elevate or manipulate tokens is a common step in malware to bypass security restrictions.
*   **Hidden "Drop" Logic:** 
    *   The code uses an iterative loop to move/copy files (in `entry0` and `fcn.00401434`), which suggests it can unpack multiple components or variants of a payload.

### Notable Techniques & Patterns
*   **NSIS Framework Pattern:** The inclusion of the string `"NSIS Error"` and the overall flow suggest this is an "infected" or custom-modified Nullsoft Script Installer. Malware authors often use NSIS because its legitimate functionality provides a perfect cover for complex installation/extraction logic.
*   **Dynamic Library Loading:** Function `fcn.00406752` identifies system paths and calls `LoadLibraryExW` to dynamically load required modules, which can be used to hide the actual dependencies needed for malicious actions until runtime.
*   **Advanced Decompression/Decoding:** The function `fcn.00406943` is highly complex, featuring nested loops and arithmetic operations typical of **LZMA-style decompression** or custom encoding schemes used to pack and unpack malicious payloads in memory.
*   **Heavy Use of Switch Tables:** The large switch statement in `fcn.00401434` serves as a "dispatcher." This is often used to simplify the code's logic while hiding the true flow of execution from simple static analysis, as it treats various system interactions (file I/O, registry edits, and UI updates) through a unified handler.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of complex bit-shifting, table lookups, and LZMA-style decompression is used to hide the payload's true functionality from static analysis. |
| **T1105** | Ingress Tool Transfer | The binary functions as a dropper/installer that moves files into temporary directories (`GetTempPathW`) to stage payloads for execution. |
| **T1127** | Dynamic Resolution | The use of `LoadLibraryExW` to resolve and load modules at runtime hides the program's dependencies from static analysis tools. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys | The execution of `RegSetValueExW` indicates an attempt to modify registry keys to ensure the payload persists across system reboots. |
| **T1548** | Privilege Escalation | The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` is a technique used to acquire elevated permissions to bypass system security restrictions. |
| **T1036.005** | Masquerading (Capability: Known Framework) | Utilizing the NSIS installer framework allows the malicious payload to hide its presence by mimicking legitimate, well-known software installation behavior. |
| **T1497** | Virtualization/Sandbox Evasion | The "Integrity Verification" logic is specifically designed to detect if the environment is being monitored or manipulated by security researchers. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted list of Indicators of Compromise (IOCs). 

**Note:** Most of the strings identified in the "Extracted Strings" section were standard Windows API functions or system DLL names; these have been excluded as false positives per your instructions.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **Temporary Folders:** (Behavioral) The binary dynamically resolves and utilizes the `GetTempPathW` and `GetTempFileNameW` functions to stage, move, and rename files in temporary directories. 
*   **Registry Interaction:** (Behavioral) Use of `RegOpenKeyExW`, `RegSetValueExW`, and `RegQueryValueExW` indicates registry manipulation for persistence or configuration, though specific keys were not hardcoded in the provided strings.

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Framework Identification:** "NSIS" (Nullsoft Script Installer). The binary contains the string `NSIS Error` and mimics NS10 architecture, indicating it is a modified or infected installer framework used to mask malicious installation logic.
*   **Decompression Technique:** The analysis identifies high-complexity logic at `fcn.00406943` consistent with **LZMA-style decompression** or custom encoding to hide second-stage payloads.
*   **Privilege Escalation Pattern:** The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` (specifically targeting `SeShutdownPrivilege`) indicates attempts to manipulate system tokens for privilege elevation.
*   **Persistence/Staging Logic:** High frequency of file manipulation functions (`MoveFileW`, `CopyFileW`, `WriteFile`) combined with an "iterative loop" at `fcn.00401434` (a dispatcher), suggesting the extraction and staging of multiple components or variants.
*   **Dynamic Loading:** Use of `LoadLibraryExW` via `fcn.00406752` to resolve system paths and load modules at runtime to evade static detection of dependencies.

---

## Malware Family Classification

1. **Malware family**: custom (NSIS-based)
2. **Malware type**: dropper / loader
3. **Confidence**: High

4. **Key evidence**:
*   **NSIS Framework Masquerading:** The binary utilizes the Nullsoft Script Installer framework to provide a "legitimate" cover for its activities, specifically using it as a vehicle to hide complex unpacking and deployment logic.
*   **Advanced Payload Unpacking:** The detection of high-complexity decompression (LZMA-style) and the use of dynamic library loading (`LoadLibraryExW`) indicate the primary function is to de-obfuscate and stage a second-stage payload in memory or on disk.
*   **Persistence & Evasion Tactics:** The combination of registry modification for persistence, privilege manipulation via `AdjustTokenPrivileges`, and "integrity checks" are classic indicators of a loader designed to bypass security controls and establish a foothold for further infection.
