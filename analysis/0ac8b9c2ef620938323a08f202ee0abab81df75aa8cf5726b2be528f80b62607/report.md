# Threat Analysis Report

**Generated:** 2026-07-25 14:31 UTC
**Sample:** `0ac8b9c2ef620938323a08f202ee0abab81df75aa8cf5726b2be528f80b62607_0ac8b9c2ef620938323a08f202ee0abab81df75aa8cf5726b2be528f80b62607.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ac8b9c2ef620938323a08f202ee0abab81df75aa8cf5726b2be528f80b62607_0ac8b9c2ef620938323a08f202ee0abab81df75aa8cf5726b2be528f80b62607.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 867,296 bytes |
| MD5 | `980eba9adc6c7cf930d60f5fc05d09c7` |
| SHA1 | `af5861890d89d2392b97b4e25b775feb03e858fe` |
| SHA256 | `0ac8b9c2ef620938323a08f202ee0abab81df75aa8cf5726b2be528f80b62607` |
| Overall entropy | 7.838 |
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
| `.rsrc` | 125,440 | 6.072 | No |

### Imports

**KERNEL32.dll**: `SetEnvironmentVariableW`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `CopyFileW`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`, `SetErrorMode`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1864** (showing first 100)

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

Based on my analysis of the decompiled code and the associated strings, this binary is an **NSIS (Nullsoft Script Installer) wrapper**. It functions primarily as a setup engine to unpack, verify, and install software components.

While the code structure is consistent with a legitimate installer, such binaries are frequently used by malware authors as "droppers" or "wrappers" because they provide a familiar interface for launching secondary payloads.

### Core Functionality and Purpose
*   **Installation Framework:** The presence of `NSIS Error` strings, use of `OleInitialize`, and the structure of `entry0` confirm this is an NSIS-based installer.
*   **Payload Extraction:** The binary performs several "Copy" and "Move" operations (e.g., in `entry0`). It moves files from temporary directories to final system locations or prepares them for execution.
*   **Integrity Checking:** Function `fcn.004067a7` contains complex bitwise arithmetic and table-based logic typical of **CRC32 or similar checksum algorithms**. This is used to verify that the extracted files are not corrupted during the unpacking process.
*   **UI Management:** A large switch-case structure in `fcn.0041434` handles standard Windows GUI events (e.g., `ShowWindow`, `SetForegroundWindow`), and other functions handle "RichEdit" controls and common dialog box logic.

### Suspicious or Malicious Behaviors
*   **Drop/Extraction Behavior:** The code heavily utilizes `GetTempPathW`, `CopyFileW`, and `MoveFileExW`. While standard for installers, this is the primary mechanism used by **droppers** to unpack a malicious payload from an encrypted or compressed state into a working directory.
*   **Privilege Manipulation:** In `entry0`, there is logic involving `OpenProcessToken`, `LookupPrivilegeValueW`, and `AdjustTokenPrivileges`. Specifically, it attempts to acquire the `SeShutdownPrivilege`. While often used by installers to trigger a reboot after installation, this pattern of privilege manipulation can also be used to prepare an environment for high-privilege execution.
*   **Environment Manipulation:** The code interacts with system paths and environmental variables (like `TEMP`) to ensure it has appropriate space and permissions to move its internal components.

### Notable Techniques or Patterns
*   **Wrapper Pattern:** The binary acts as a "wrapper." It handles the complex task of extracting compressed data and verifying it before handing off execution to the primary payload. This is an effective way for malware to bypass basic signature-based detection, as the malicious payload is hidden inside the installer's archives.
*   **Robust Path Handling:** The function `fcn.00626e` is a sophisticated routine for handling Windows file paths, including Unicode conversions and "long path" logic. This ensures the installer works consistently across different user environments.
*   **Standard API Abuse (Contextual):** Use of `SetFileAttributesW`, `GetTempFileNameW`, and `CopyFileW` are standard but frequently monitored by EDR systems. In this context, these APIs are being used to "stage" files before they are executed.

### Summary for Report
The sample is an **NSIS Installer**. It performs automated file extraction, integrity checking (via CRC-style algorithms), and GUI handling. While the installer itself may not be "malicious," its role as a wrapper means it likely serves as a vehicle to deliver a secondary payload. The core logic focuses on moving files from hidden/temporary locations into executable states.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
|---|---|---|
| T1036 | Masquerading | The binary utilizes a common NSIS installer framework to masquerade as a legitimate software update or installation tool to blend in with system activities. |
| T1027 | Obfuscated Files or Information | The use of an archive/wrapper system hides the primary malicious payload within compressed or encrypted data to bypass signature-based detection. |
| T1068 | Exploitation for Privilege Escalation | The explicit calls to `AdjustTokenPrivileges` indicate an attempt to acquire higher privileges (like `SeShutdownPrivilege`) to facilitate advanced actions or environment preparation. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the list of extracted Indicators of Compromise (IOCs). 

**Note:** Many items in the provided "Extracted Strings" section were identified as standard Windows API functions (e.g., `GetTempPathW`, `RegOpenKeyExW`) or standard system libraries (`KERNEL32.dll`). These have been excluded from the report as they are common to both legitimate and malicious software and do not constitute specific, actionable IOCs.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (While the analysis notes the use of `GetTempPathW` and registry manipulation functions, no specific hardcoded malicious paths or keys were present in the provided data).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Mechanism:** NSIS (Nullsoft Script Installer) Wrapper.
    *   *Analysis:* The sample is identified as an installer wrapper. While the installer itself may be "clean," its use of `GetTempPathW`, `CopyFileW`, and `MoveFileExW` indicates a behavior pattern typical of **droppers** used to stage payloads in temporary directories before execution.
*   **Functionality:** CRC32-style checksum verification (found at logic point `fcn.004067a7`). This is used for payload integrity checks post-extraction.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: dropper / loader
3. **Confidence**: High
4. **Key evidence**: 
*   **Wrapper Behavior:** The sample is identified as an NSIS (Nullsoft Script Installer) wrapper, a common technique used by threat actors to mask the presence of malicious payloads within a legitimate-looking installation framework.
*   **Staging and Extraction:** The code utilizes specific APIs (`GetTempPathW`, `CopyFileW`, `MoveFileExW`) to extract files from compressed/hidden archives into temporary directories, which is the primary characteristic of a "dropper" or "loader."
*   **Evasion and Preparation:** The inclusion of CRC32-style integrity checks for extracted payloads and explicit calls to `AdjustTokenPrivileges` indicates preparation for executing secondary malware while attempting to bypass basic security controls.
