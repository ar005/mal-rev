# Threat Analysis Report

**Generated:** 2026-07-31 15:02 UTC
**Sample:** `0c7a47180973a40c9f704dae07fd91d93f74b90e75a2c6e1cf22677eeb6e0251_0c7a47180973a40c9f704dae07fd91d93f74b90e75a2c6e1cf22677eeb6e0251.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c7a47180973a40c9f704dae07fd91d93f74b90e75a2c6e1cf22677eeb6e0251_0c7a47180973a40c9f704dae07fd91d93f74b90e75a2c6e1cf22677eeb6e0251.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 720,056 bytes |
| MD5 | `cea340eafd9a83022d39f0bc0db7cbc6` |
| SHA1 | `e3ac1b9a23aa4bc8a5fd8123c7ba297aeab94531` |
| SHA256 | `0c7a47180973a40c9f704dae07fd91d93f74b90e75a2c6e1cf22677eeb6e0251` |
| Overall entropy | 7.752 |
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

Total strings found: **1566** (showing first 100)

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

Based on the provided disassembly and decompiled code, here is an analysis of the binary's functionality:

### Core Functionality and Purpose
The binary functions as a **wrapper/stub for a software installer**, specifically utilizing the **NSIS (Nullsoft Script Installer)** framework. The primary purpose of this specific code is to:
1.  **Extract components:** It unpacks internal resources into temporary directories.
2.  **Environment Setup:** It sets up environment variables and checks for system capabilities (e.g., `UXTHEME` support).
3.  **Installer Execution:** It manages the flow of an installation script, handling UI elements, progress bars, and file operations.

### Suspicious or Malicious Behaviors
While the code is characteristic of a legitimate installer (NSIS), certain behaviors are commonly abused by malware to deliver payloads:

*   **Drop and Execute (Dropper behavior):** 
    *   The code uses `GetTempPathW` and `MoveFileW`/`CopyFileW` to move files from internal memory/resources into the system's temporary folder.
    *   It creates and manipulates temporary files (e.g., `.tmp` extensions) in a local directory before execution. This is a standard method for "dropping" a secondary payload that performs the actual malicious actions.
*   **Dynamic Loading of DLLs:** 
    *   The function `fcn.0040671a` uses `GetProcAddress` and `LoadLibraryExW` to dynamically load system libraries (like `UXTHEME`). While often used for visual compatibility, it is also a common technique to hide the true capabilities of a binary from static analysis.
*   **System Interaction:** 
    *   The code interacts heavily with the registry (`RegOpenKeyExW`, `RegSetValueExW`) and uses `ShellExecuteExW` to launch components. This allows it to interact with system settings or execute newly dropped binaries.
*   **Integrity Checking:** 
    *   Function `fcn.00402f14` specifically performs an "Installer integrity check." In a malicious context, this ensures that the dropped payload hasn't been corrupted by security software during extraction.

### Notable Techniques and Patterns
*   **NSIS Framework Identification:** The inclusion of specific error messages (e.g., `http://nsis.sf.net/NSIS_Error`) and logic for handling `.tmp` files confirms this is a standard NSIS installer. Malware authors frequently use NSIS because it provides an easy way to bundle, decrypt, and extract multiple payloads into the system.
*   **Internal Decompression:** The complex bit-shifting and loops in `fcn.0040690b` indicate internal decompression or decoding of data (likely LZMA/LZS algorithms common in NSIS) before the files are written to disk.
*   **Dynamic Execution Path:** The use of `GetTempPathW` combined with `SetCurrentDirectoryW` indicates that the program dynamically builds its execution path at runtime, making it harder to track exactly what is being executed without observing the process during execution.

### Summary for Analysis
This binary is an **installer stub**. While the code itself is primarily used for legitimate installation, its "Dropper" functionality (extracting and moving files into `%TEMP%` before launching them) is a primary delivery mechanism for malware. Any file it extracts or any process it spawns after extraction should be treated as potentially malicious.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of a standard NSIS wrapper and dropping files into the system's temporary directory allows the binary to blend in with legitimate installer behavior. |
| T1027 | Obfuscated Files/Information | The implementation of decompression algorithms, integrity checks (to bypass security tools), and dynamic loading of DLLs are used to hide the program's true capabilities from static analysis. |
| T1112 | Modify Registry | The use of `RegOpenKeyExW` and `RegSetValueExW` indicates interaction with registry keys for system configuration or establishing persistence. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Many items in the "Strings" section were identified as standard Windows API functions or system libraries (e.g., `KERNEL32.dll`, `GetProcAddress`) and have been excluded as false positives per your instructions.

### **IP addresses / URLs / Domains**
*   `http://nsis.sf.net/NSIS_Error` (Identified as a signature of the NSIS framework)

### **File paths / Registry keys**
*   *None identified.* (The analysis mentions generic locations like `%TEMP%` and `.tmp` files, but no specific hardcoded malicious paths were provided.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Framework Identification:** NSIS (Nullsoft Script Installer). The binary is confirmed as an NSIS wrapper/stub.
*   **C2/Payload Behavior:** 
    *   **Dropper Behavior:** The use of `GetTempPathW`, `MoveFileW`, and `CopyFileW` to stage files in the system's temporary directory.
    *   **Obfuscation Technique:** Dynamic loading of `UXTHEME` via `GetProcAddress` and `LoadLibraryExW`.
    *   **Compression Artifacts:** Use of LZMA/LZS decompression algorithms for internal data extraction.
    *   **Integrity Checking:** Implementation of a specific integrity check (`fcn.00402f14`) to verify payload integrity post-extraction.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown (NSIS Wrapper)
2. **Malware type**: Dropper
3. **Confidence**: High

**Key evidence**:
*   **NSIS Framework Identification:** The analysis confirms the binary is an NSIS (Nullsoft Script Installer) wrapper. While often used for legitimate software, it is a very common vehicle used by malware authors to bundle and deliver multiple payloads while masquerading as a standard installer.
*   **Dropper Behavior:** The code exhibits classic "dropper" characteristics, specifically using `GetTempPathW`, `MoveFileW`, and `CopyFileW` to extract internal resources into the `%TEMP%` directory followed by execution via `ShellExecuteExW`.
*   **Evasion/Obfuscation Tactics:** The inclusion of integrity checks (to ensure payloads haven't been tampered with by security software), dynamic loading of DLLs, and decompression algorithms are standard techniques used to hide the final payload from static analysis.
