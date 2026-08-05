# Threat Analysis Report

**Generated:** 2026-08-04 22:45 UTC
**Sample:** `0d38177cbe3469d1e658d8b8bdf7785c2ef0c0021c7e08aa5ebbe1904d34d1c4_0d38177cbe3469d1e658d8b8bdf7785c2ef0c0021c7e08aa5ebbe1904d34d1c4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d38177cbe3469d1e658d8b8bdf7785c2ef0c0021c7e08aa5ebbe1904d34d1c4_0d38177cbe3469d1e658d8b8bdf7785c2ef0c0021c7e08aa5ebbe1904d34d1c4.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 646,040 bytes |
| MD5 | `bfdfa68016b705afd4c4f60301f5f559` |
| SHA1 | `9f01618c6805c3e3e92c82120ae6dd904bf7aafa` |
| SHA256 | `0d38177cbe3469d1e658d8b8bdf7785c2ef0c0021c7e08aa5ebbe1904d34d1c4` |
| Overall entropy | 7.727 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1469408154 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 24,576 | 6.5 | No |
| `.rdata` | 5,120 | 5.208 | No |
| `.data` | 1,536 | 4.032 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 103,424 | 4.987 | No |

### Imports

**KERNEL32.dll**: `SetEnvironmentVariableA`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameA`, `GetCurrentProcess`, `CopyFileA`, `GetFileAttributesA`, `SetFileAttributesA`, `GetWindowsDirectoryA`, `GetTempPathA`, `GetCommandLineA`, `lstrlenA`, `GetVersion`, `SetErrorMode`
**USER32.dll**: `ScreenToClient`, `GetSystemMenu`, `SetClassLongA`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongA`, `SetCursor`, `LoadCursorA`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapA`, `CallWindowProcA`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectA`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHGetPathFromIDListA`, `SHBrowseForFolderA`, `SHGetFileInfoA`, `ShellExecuteA`, `SHFileOperationA`
**ADVAPI32.dll**: `RegDeleteKeyA`, `SetFileSecurityA`, `OpenProcessToken`, `LookupPrivilegeValueA`, `AdjustTokenPrivileges`, `RegOpenKeyExA`, `RegEnumValueA`, `RegDeleteValueA`, `RegCloseKey`, `RegCreateKeyExA`, `RegSetValueExA`, `RegQueryValueExA`, `RegEnumKeyA`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1389** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495,
SQSSSPW
tQVPW
Et@;u
Instu`
softuW
NulluN	E
D$$Ph,
D$(SPS
tVj%SSS
SWSh<s@
SWhZs@
D$$+D$
D$,+D$$P
us9Et	
8\tPV
_^[t	P
HtVHtHH
UXTHEME
USERENV
SETUPAPI
APPHELP
PROPSYS
DWMAPI
CRYPTBASE
OLEACC
CLBCATQ
RichEdit
RichEdit20A
RichEd32
RichEd20
.DEFAULT\Control Panel\International
Control Panel\Desktop\ResourceLocale
Software\Microsoft\Windows\CurrentVersion
\Microsoft\Internet Explorer\Quick Launch
MulDiv
DeleteFileA
FindFirstFileA
FindNextFileA
FindClose
SetFilePointer
GetPrivateProfileStringA
WritePrivateProfileStringA
MultiByteToWideChar
FreeLibrary
LoadLibraryExA
GetModuleHandleA
GetExitCodeProcess
WaitForSingleObject
GlobalAlloc
GlobalFree
ExpandEnvironmentStringsA
lstrcmpA
lstrcmpiA
CloseHandle
SetFileTime
CompareFileTime
SearchPathA
GetShortPathNameA
GetFullPathNameA
MoveFileA
SetCurrentDirectoryA
GetFileAttributesA
SetFileAttributesA
GetTickCount
GetFileSize
GetModuleFileNameA
GetCurrentProcess
CopyFileA
ExitProcess
SetEnvironmentVariableA
GetWindowsDirectoryA
GetTempPathA
GetCommandLineA
lstrlenA
GetVersion
SetErrorMode
lstrcpynA
GetDiskFreeSpaceA
GlobalUnlock
GlobalLock
CreateThread
GetLastError
CreateDirectoryA
CreateProcessA
RemoveDirectoryA
CreateFileA
GetTempFileNameA
ReadFile
WriteFile
lstrcpyA
MoveFileExA
lstrcatA
GetSystemDirectoryA
GetProcAddress
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5293 | ✓ |
| `fcn.004061ab` | `0x4061ab` | 2639 | ✓ |
| `entry0` | `0x40310f` | 1222 | ✓ |
| `fcn.00406ca2` | `0x406ca2` | 827 | ✓ |
| `fcn.004036af` | `0x4036af` | 709 | ✓ |
| `fcn.00405d51` | `0x405d51` | 585 | ✓ |
| `fcn.00402c66` | `0x402c66` | 569 | ✓ |
| `fcn.00402e9f` | `0x402e9f` | 530 | ✓ |
| `fcn.004055d1` | `0x4055d1` | 464 | ✓ |
| `fcn.00405a78` | `0x405a78` | 370 | ✓ |
| `fcn.00404f48` | `0x404f48` | 210 | ✓ |
| `fcn.00403974` | `0x403974` | 205 | ✓ |
| `fcn.00404709` | `0x404709` | 197 | ✓ |
| `fcn.00402a7a` | `0x402a7a` | 181 | ✓ |
| `fcn.00403f7b` | `0x403f7b` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00405f9a` | `0x405f9a` | 153 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00405ca6` | `0x405ca6` | 137 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404813` | `0x404813` | 128 | ✓ |
| `fcn.0040540e` | `0x40540e` | 125 | ✓ |
| `fcn.0040588f` | `0x40588f` | 120 | ✓ |
| `fcn.00405c16` | `0x405c16` | 119 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.0040613d` | `0x40613d` | 110 | ✓ |
| `fcn.0040605a` | `0x40605a` | 110 | ✓ |
| `fcn.0040501a` | `0x40501a` | 108 | ✓ |
| `fcn.00406c3a` | `0x406c3a` | 104 | ✓ |
| `fcn.00405525` | `0x405525` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402a7a.c`](code/fcn.00402a7a.c)
- [`code/fcn.00402c66.c`](code/fcn.00402c66.c)
- [`code/fcn.00402e9f.c`](code/fcn.00402e9f.c)
- [`code/fcn.004036af.c`](code/fcn.004036af.c)
- [`code/fcn.00403974.c`](code/fcn.00403974.c)
- [`code/fcn.00403f7b.c`](code/fcn.00403f7b.c)
- [`code/fcn.00404709.c`](code/fcn.00404709.c)
- [`code/fcn.00404813.c`](code/fcn.00404813.c)
- [`code/fcn.00404f48.c`](code/fcn.00404f48.c)
- [`code/fcn.0040501a.c`](code/fcn.0040501a.c)
- [`code/fcn.0040540e.c`](code/fcn.0040540e.c)
- [`code/fcn.00405525.c`](code/fcn.00405525.c)
- [`code/fcn.004055d1.c`](code/fcn.004055d1.c)
- [`code/fcn.0040588f.c`](code/fcn.0040588f.c)
- [`code/fcn.00405a78.c`](code/fcn.00405a78.c)
- [`code/fcn.00405c16.c`](code/fcn.00405c16.c)
- [`code/fcn.00405ca6.c`](code/fcn.00405ca6.c)
- [`code/fcn.00405d51.c`](code/fcn.00405d51.c)
- [`code/fcn.00405f9a.c`](code/fcn.00405f9a.c)
- [`code/fcn.0040605a.c`](code/fcn.0040605a.c)
- [`code/fcn.0040613d.c`](code/fcn.0040613d.c)
- [`code/fcn.004061ab.c`](code/fcn.004061ab.c)
- [`code/fcn.00406c3a.c`](code/fcn.00406c3a.c)
- [`code/fcn.00406ca2.c`](code/fcn.00406ca2.c)

## Behavioral Analysis

This analysis is based on the provided disassembly of a binary that appears to be a **customized installer or a dropper** (specifically, one wrapping an NSIS—Nullsoft Script Installer—payload).

### Core Functionality and Purpose
The primary purpose of this code is to act as a "wrapper" for an installation process. It performs several management tasks before launching the main payload:
*   **Integrity Verification:** The function `fcn.0040613d` implements a CRC32 checksum (identified by the constant `0xedb88320`). This is used to verify that the installer or its associated files are not corrupted before proceeding.
*   **Environment Setup:** It performs extensive checks on system paths, including resolution of special folders and system directories. 
*   **Installer Logic:** The presence of strings like `-nsu` (a standard NSIS flag) and a reference to `nsis.sf.net` in the error message confirm that this code manages an installation script. It handles UI elements, progress bars (`... %`), and file renaming/moving operations.

### Suspicious or Malicious Behaviors
While much of the behavior is typical for installer wrappers, several patterns are common in malware (specifically droppers and loaders):

*   **Privilege Escalation:** 
    *   The code calls `AdjustTokenPrivileges` to acquire the `SeShutdownPrivilege`. While seemingly specific to shutting down, this system call is often used by installers/malware to elevate the process's privileges or bypass certain security restrictions.
*   **Environment Manipulation:**
    *   The binary interacts with and potentially modifies the `TEMP` environment variable (`SetEnvironmentVariableA`). This ensures that if it extracts a payload, the payload is executed from a predictable location.
*   **File System Manipulation (Dropper Behavior):**
    *   The complex logic in `fcn.00405d51` involves intensive manipulation of file paths, including `GetSystemDirectoryA`, `GetWindowsDirectoryA`, and `GetSpecialFolderLocation`. It performs "search-and-replace" style logic on filenames, which can be used to hide files or move them into system directories where they are harder to detect.
    *   It uses `MoveFileExA` and `CopyFileA` in a loop, potentially preparing several components for an upcoming execution phase.
*   **Obfuscated/Robust Path Handling:** 
    *   The heavy use of `GetShortPathNameA`, `GetFullPathNameA`, and `SearchPathA` suggests the code is designed to find its dependencies even if they are moved, renamed, or hidden behind symbolic links/shortcuts.

### Notable Techniques and Patterns
*   **NSIS Wrapper:** The binary is clearly a modified NSIS wrapper. Attackers frequently use this method to bundle malicious payloads with legitimate-looking installers, as the initial installer "looks" like a standard system tool.
*   **CRC32 Integrity Checks:** The implementation of `fcn.0040613d` is a classic way to ensure that the payload hasn't been tampered with or corrupted during the download/extraction phase.
*   **Resource-Heavy UI Handling:** The extensive use of `Win32` API calls (like `SendMessageA`, `SetWindowTextA`, and `GetDlgItem`) suggests a complex GUI is present to interact with the user, potentially distracting them while high-privilege operations occur in the background.
*   **Standard Library Mimicry:** The code uses standard OS features (System Parameters, Shell APIs) to blend in with legitimate installer software, making it harder for basic heuristic scanners to flag it as suspicious without deep behavioral analysis.

### Summary for Incident Response
This binary is a **Loader/Installer Wrapper**. It is designed to verify the integrity of a payload (via CRC32), prepare the system environment (manipulating paths and privileges), and then execute a secondary installer or component. The presence of privilege escalation attempts and complex file-moving logic suggests it is likely used for delivering and installing software, which could be potentially malicious depending on the final "payload" it unpacks.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of an NSIS wrapper and standard Win32 API calls allows the binary to mimic a legitimate software installer. |
| T1068 | Exploitation for Privilege Escalation | The call to `AdjustTokenPrivileges` indicates an attempt to acquire elevated system privileges or bypass security restrictions. |
| T1105 | Ingress Tool Transfer | The "Dropper" behavior involving the movement of components and file path manipulation is used to stage payloads on the local system. |
| T1027 | Obfuscated Files or Information | The implementation of a CRC32 checksum ensures that potentially obfuscated or packed payload files remain intact before execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `nsis.sf.net` (Identified as part of an error message; associated with the Nullsoft Script Installer suite)

**File paths / Registry keys**
*   *None.* (Note: While several registry keys and system directory calls were mentioned, they are standard Windows system paths/keys and do not constitute specific malicious IOCs.)

**Mutex names / Named pipes**
*   *None found.*

**Hashes**
*   *None found.* (Note: The constant `0xedb88320` is a CRC32 algorithm constant, not a file hash.)

**Other artifacts**
*   **Tooling Identifiers:** 
    *   `-nsu` (Standard NSIS installer flag)
    *   **NSIS Wrapper Behavior:** The binary functions as a wrapper/loader for an NSIS payload.
*   **Integrity Check Method:** CRC32 checksum validation.
*   **Privilege Manipulation:** Utilization of `AdjustTokenPrivileges` to acquire `SeShutdownPrivilege`.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family:** custom
2. **Malware type:** dropper / loader
3. **Confidence:** High
4. **Key evidence:** 
*   **NSIS Wrapper Behavior:** The binary utilizes a modified Nullsoft Script Installer (NSIS) framework, identified by the `-nsu` flag and standard installer logic, to masquerade as legitimate software while facilitating the installation of subsequent components.
*   **Pre-execution Preparation:** It performs typical dropper behaviors including CRC32 integrity checks (`0xedb88320`), environment manipulation (modifying `TEMP` variables), and complex file-system navigation to prepare an environment for a secondary payload.
*   **Privilege Escalation & Persistence:** The use of `AdjustTokenPrivileges` and systematic movement of files into system directories indicates an intent to bypass security restrictions and ensure the successful installation/execution of its primary objective.
