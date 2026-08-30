# Threat Analysis Report

**Generated:** 2026-08-18 01:08 UTC
**Sample:** `102b27de67452f77077070719d446c9e7565afd5bdaee828017e15dbb19b9be3_102b27de67452f77077070719d446c9e7565afd5bdaee828017e15dbb19b9be3.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `102b27de67452f77077070719d446c9e7565afd5bdaee828017e15dbb19b9be3_102b27de67452f77077070719d446c9e7565afd5bdaee828017e15dbb19b9be3.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 678,552 bytes |
| MD5 | `1b852653fd6000dbb87608cb4a72b3ca` |
| SHA1 | `55439f6cb3f970615524268f92c1f0228f8b81ed` |
| SHA256 | `102b27de67452f77077070719d446c9e7565afd5bdaee828017e15dbb19b9be3` |
| Overall entropy | 7.731 |
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

Total strings found: **1499** (showing first 100)

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

Based on the analysis of the provided disassembly and decompiled code, here is a summary of the binary's behavior:

### Core Functionality and Purpose
The binary functions as an **installer wrapper or packer**. It is designed to bundle compressed/encrypted data (likely for a software application) and "unpack" it into a working state before execution. Several indicators point specifically toward this being a modified or wrapped version of a Nullsoft Script Installer (NSIS) package:
*   The presence of specific error messages referencing `nsis.sf.net`.
*   Heavy use of standard installer routines for file copying, path resolution, and environment checking.

### Suspicious or Malicious Behaviors
While the primary purpose is "installation," the following behaviors are characteristic of malware droppers and packers:

*   **File Dropping & Extraction:** The code identifies a source payload, creates a temporary file (often in `\AppData\Local\Temp\`), and extracts data into it. Specifically, the routine involving `fcn.004032c2` performs chunked reads/writes to move data from an internal buffer to a destination file.
*   **Privilege Escalation/Manipulation:** The binary explicitly calls `OpenProcessToken`, `LookupPrivilegeValueW`, and `AdjustTokenPrivileges`. It specifically requests the `SeShutdownPrivilege`. In a malware context, this is often used to ensure the installer has enough permissions to modify system files or registry keys.
*   **Environment Manipulation:** The code includes logic to check and potentially overwrite the `TEMP` environment variable path (`fcn.00403458`). This ensures that the subsequent "payload" always finds a writable directory, regardless of local configuration.
*   **Payload Execution:** After extracting files to the temporary directory, it utilizes internal routines to launch the resulting executables.

### Notable Techniques and Patterns
*   **NSIS Characteristics:** The code contains several logic gates that are common in NSIS scripts (e.g., checking for "UXTHEME" support, handling `GetFileAttributesW` results, and complex nested switch statements for GUI interaction).
*   **Integrity Checking:** There is a specific routine (`fcn.004031ba`) involved in an integrity check. This ensures the payload was not corrupted during the "wrapping" process before it is allowed to run.
*   **Complex Data Parsing:** The function `fcn.0040690b` contains complex memory management and arithmetic logic, suggesting that the data being unpacked is not just raw files but a structured (potentially encrypted or compressed) format that must be parsed before use.
*   **Dynamic File Path Resolution:** It uses multiple methods (`GetShortPathNameW`, `GetFullPathNameW`) to resolve file locations, ensuring it can navigate both relative and absolute paths commonly used in installers.

### Summary for Incident Response
This binary is a **dropper**. Its primary role is to bypass basic detection by wrapping the final malicious payload inside a legitimate-looking installer framework. It handles the "heavy lifting" of unpacking the malware, resolving system paths, escalating privileges, and ensuring the hidden component is correctly placed in a temporary directory before launching it.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1028 | Packer | The binary functions as a wrapper/packer to bundle, compress, and extract a payload into a workable state before execution. |
| T1548 | Privilege Escalation | The binary explicitly calls `AdjustTokenPrivileges` and `LookupPrivilegeValueW` to acquire the `SeShutdownPrivilege`. |
| T1036 | Masquerading | The binary utilizes common NSIS installer routines and standard installation behaviors to hide its malicious purpose behind a legitimate-looking framework. |
| T1027 | Obfuscated Files or Information | The complex parsing of structured, potentially encrypted/compressed data indicates that the payload is not in its raw form before being unpacked. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `nsis.sf.net` (Note: Associated with the NSIS installer framework used as a wrapper/packer)

**File paths / Registry keys**
*   None (The path `\AppData\Local\Temp\` was identified in the analysis but is excluded as it is a standard Windows system path).

**Mutex names / Named pipes**
*   None

**Hashes**
*   None

**Other artifacts**
*   **Technique:** NSIS Installer Wrapper (used to bundle and obfuscate malicious payloads).
*   **Privilege Request:** `SeShutdownPrivilege` (Requested via `AdjustTokenPrivileges`).
*   **Function Offsets of Interest:** 
    *   `fcn.004032c2` (Payload extraction routine)
    *   `fcn.00403458` (Environment variable manipulation)
    *   `fcn.004031ba` (Integrity check/Verification)
    *   `fcn.0040690b` (Complex data parsing/Decryption logic)

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
    *   **Installer Wrapping:** The binary utilizes Nullsoft Script Installer (NSIS) logic to masquerade as a legitimate software installer while wrapping and concealing the primary malicious payload.
    *   **Payload Deployment:** It exhibits classic dropper behavior by extracting, integrity-checking, and executing files from a temporary directory (`\AppData\Local\Temp\`) after performing environment variable manipulation.
    *   **Privilege Escalation:** The inclusion of `AdjustTokenPrivileges` to acquire the `SeShutdownPrivilege` is a common technique used by droppers to ensure the installer can bypass restrictions to modify system settings or file permissions for the upcoming payload.
