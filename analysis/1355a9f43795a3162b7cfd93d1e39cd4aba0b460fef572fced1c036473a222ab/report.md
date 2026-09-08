# Threat Analysis Report

**Generated:** 2026-09-02 13:43 UTC
**Sample:** `1355a9f43795a3162b7cfd93d1e39cd4aba0b460fef572fced1c036473a222ab_1355a9f43795a3162b7cfd93d1e39cd4aba0b460fef572fced1c036473a222ab.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1355a9f43795a3162b7cfd93d1e39cd4aba0b460fef572fced1c036473a222ab_1355a9f43795a3162b7cfd93d1e39cd4aba0b460fef572fced1c036473a222ab.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 624,063 bytes |
| MD5 | `17ae700cf861e07d94a5ef0422fca187` |
| SHA1 | `c9f1e8c56848bf06e94788b922b9323f96eda4bd` |
| SHA256 | `1355a9f43795a3162b7cfd93d1e39cd4aba0b460fef572fced1c036473a222ab` |
| Overall entropy | 7.445 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1387947676 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 23,552 | 6.511 | No |
| `.rdata` | 4,608 | 5.236 | No |
| `.data` | 1,024 | 4.875 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 202,240 | 5.555 | No |

### Imports

**KERNEL32.dll**: `GetTickCount`, `GetFullPathNameA`, `MoveFileA`, `SetCurrentDirectoryA`, `GetFileAttributesA`, `GetLastError`, `CreateDirectoryA`, `SetFileAttributesA`, `SearchPathA`, `GetShortPathNameA`, `GetFileSize`, `GetModuleFileNameA`, `GetCurrentProcess`, `CopyFileA`, `ExitProcess`
**USER32.dll**: `CreateWindowExA`, `EndDialog`, `ScreenToClient`, `GetWindowRect`, `EnableMenuItem`, `GetSystemMenu`, `SetClassLongA`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongA`, `SetCursor`, `LoadCursorA`, `CheckDlgButton`, `GetMessagePos`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectA`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHGetPathFromIDListA`, `SHBrowseForFolderA`, `SHGetFileInfoA`, `ShellExecuteA`, `SHFileOperationA`
**ADVAPI32.dll**: `RegCloseKey`, `RegOpenKeyExA`, `RegDeleteKeyA`, `RegDeleteValueA`, `RegEnumValueA`, `RegCreateKeyExA`, `RegSetValueExA`, `RegQueryValueExA`, `RegEnumKeyA`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `CoCreateInstance`, `CoTaskMemFree`, `OleInitialize`, `OleUninitialize`
**VERSION.dll**: `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`, `VerQueryValueA`

## Extracted Strings

Total strings found: **1090** (showing first 100)

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
v#VhD+@
Instu`
softuW
NulluN	E
D$(Ph,
D$,SPS
D$$+D$
D$,+D$$P
us9Et	
PPPPPP
8\tPV
uhHs@
_^[t	P
D$SVW
A@;E |
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
WriteFile
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
GetLastError
CreateDirectoryA
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
SetErrorMode
LoadLibraryA
lstrlenA
lstrcpynA
GetDiskFreeSpaceA
GlobalUnlock
GlobalLock
CreateThread
CreateProcessA
RemoveDirectoryA
CreateFileA
GetTempFileNameA
ReadFile
lstrcpyA
lstrcatA
GetSystemDirectoryA
GetVersion
GetProcAddress
KERNEL32.dll
EndPaint
DrawTextA
FillRect
GetClientRect
BeginPaint
DefWindowProcA
SendMessageA
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5234 | ✓ |
| `fcn.00406122` | `0x406122` | 2183 | ✓ |
| `entry0` | `0x4030cb` | 1118 | ✓ |
| `fcn.00403603` | `0x403603` | 709 | ✓ |
| `fcn.00405b9c` | `0x405b9c` | 585 | ✓ |
| `fcn.00402c2b` | `0x402c2b` | 569 | ✓ |
| `fcn.00402e64` | `0x402e64` | 518 | ✓ |
| `fcn.0040543a` | `0x40543a` | 464 | ✓ |
| `fcn.004058b2` | `0x4058b2` | 380 | ✓ |
| `fcn.00405fda` | `0x405fda` | 328 | ✓ |
| `fcn.00406adb` | `0x406adb` | 216 | ✓ |
| `fcn.00404e65` | `0x404e65` | 210 | ✓ |
| `fcn.004038c8` | `0x4038c8` | 205 | ✓ |
| `fcn.00402a3f` | `0x402a3f` | 181 | ✓ |
| `fcn.0040464e` | `0x40464e` | 181 | ✓ |
| `fcn.00403ecf` | `0x403ecf` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00405de5` | `0x405de5` | 153 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00405af1` | `0x405af1` | 137 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00406a5a` | `0x406a5a` | 129 | ✓ |
| `fcn.00404730` | `0x404730` | 128 | ✓ |
| `fcn.004056f8` | `0x4056f8` | 120 | ✓ |
| `fcn.00405a61` | `0x405a61` | 119 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00405f17` | `0x405f17` | 110 | ✓ |
| `fcn.00404f37` | `0x404f37` | 108 | ✓ |
| `fcn.004069f5` | `0x4069f5` | 101 | ✓ |
| `fcn.0040538e` | `0x40538e` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402a3f.c`](code/fcn.00402a3f.c)
- [`code/fcn.00402c2b.c`](code/fcn.00402c2b.c)
- [`code/fcn.00402e64.c`](code/fcn.00402e64.c)
- [`code/fcn.00403603.c`](code/fcn.00403603.c)
- [`code/fcn.004038c8.c`](code/fcn.004038c8.c)
- [`code/fcn.00403ecf.c`](code/fcn.00403ecf.c)
- [`code/fcn.0040464e.c`](code/fcn.0040464e.c)
- [`code/fcn.00404730.c`](code/fcn.00404730.c)
- [`code/fcn.00404e65.c`](code/fcn.00404e65.c)
- [`code/fcn.00404f37.c`](code/fcn.00404f37.c)
- [`code/fcn.0040538e.c`](code/fcn.0040538e.c)
- [`code/fcn.0040543a.c`](code/fcn.0040543a.c)
- [`code/fcn.004056f8.c`](code/fcn.004056f8.c)
- [`code/fcn.004058b2.c`](code/fcn.004058b2.c)
- [`code/fcn.00405a61.c`](code/fcn.00405a61.c)
- [`code/fcn.00405af1.c`](code/fcn.00405af1.c)
- [`code/fcn.00405b9c.c`](code/fcn.00405b9c.c)
- [`code/fcn.00405de5.c`](code/fcn.00405de5.c)
- [`code/fcn.00405f17.c`](code/fcn.00405f17.c)
- [`code/fcn.00405fda.c`](code/fcn.00405fda.c)
- [`code/fcn.00406122.c`](code/fcn.00406122.c)
- [`code/fcn.004069f5.c`](code/fcn.004069f5.c)
- [`code/fcn.00406a5a.c`](code/fcn.00406a5a.c)
- [`code/fcn.00406adb.c`](code/fcn.00406adb.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary's functionality.

### Core Functionality and Purpose
The binary functions as an **installer stub or a "wrapper"** (highly likely based on the Nullsoft Script Installer - NSIS). Its primary role is to act as a middleman: it takes a packed/compressed payload, extracts it into a temporary directory, performs integrity checks, and then executes the resulting files.

The presence of strings like `nsis_error`, `verifying installer`, and the heavy use of "Command" logic (the large switch-case in `fcn.00401434`) suggest that this is a script interpreter or an installer wrapper common in software distribution.

### Suspicious or Malicious Behaviors
While these behaviors are common in legitimate installers, they are also heavily utilized by malware to hide the final "payload" from automated scanners.

*   **Dropper/Downloader Behavior:**
    *   The `entry0` function retrieves temporary paths (`GetTempPathA`) and creates directories to stage files before execution.
    *   It uses `CopyFileA` and `MoveFileA` to transition "dropped" components into their final working locations.
    *   The use of `ShellExecuteA` and `CreateProcessA` indicates it launches the next stage of the program after unpacking it.

*   **Persistence/Configuration via Registry:**
    *   The code contains significant logic for querying, creating, and modifying registry keys (`RegCreateKeyExA`, `RegSetValueExA`). This is often used to store installation paths or to ensure a program starts on boot (persistence).

*   **Dynamic Function Loading:**
    *   Several sections use `GetProcAddress` and `LoadLibraryA`. This allows the binary to load its "real" logic only into memory at runtime, making it harder for static analysis tools to see what the program is capable of doing until after it has been executed.

*   **Integrity/Checksum Verification:**
    *   The function `fcn.00405f17` implements a custom calculation (appearing to be a CRC or polynomial-based check). It is used to verify that the "dropped" files were not corrupted during extraction, a common step in both complex installers and malware unpackers.

### Notable Techniques & Patterns
*   **Command Dispatcher Pattern:** The extremely large switch statement in `fcn.00401434` (handling over 60 cases) is a hallmark of an **interpreter**. Instead of being a single purpose-built program, it is executing a sequence of instructions (likely from an embedded script).
*   **"Stub" Behavior:** The code is designed to be short and generic. It handles the "heavy lifting" of file manipulation so that the actual malicious or useful payload can remain encrypted/compressed until the last possible moment.
*   **UI Interaction:** References to `RichEdit20`, `GetDlgItem`, and `SendMessageA` indicate that while the core is a launcher, it may also interact with Windows UI elements to display progress bars or "Success" messages during its operations.

### Summary for Intelligence
This binary is a **wrapper/installer stub**. While it does not appear to be performing direct network communication (C2) in this specific snippet, it is designed to:
1.  **Extract and Stage:** Unpack files into a hidden or temporary location.
2.  **Verify:** Check the integrity of those files using custom math.
3.  **Execute:** Hand off control to another process (`CreateProcessA`/`ShellExecuteA`).

**Analyst Note:** Because this is a "wrapper," the actual malicious activity (such as stealing data or encrypting files) is likely contained in the *second* file that this program extracts and runs, rather than in this specific binary.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1112** | Modify Registry | The binary utilizes `RegCreateKeyExA` and `RegSetValueExA` to modify registry keys for configuration or establishing persistence. |
| **T1633** | Dynamic Resolution | The use of `GetProcAddress` and `LoadLibraryA` allows the binary to resolve functions at runtime, which is a common method to evade static analysis. |
| **T1059** | Command and Scripting Interpreter | The presence of an extensive switch-case statement indicates the binary acts as an interpreter for executing embedded instructions or scripts. |
| **T1036** | Masquerading | The "installer stub" design allows the binary to masquerade as a legitimate software utility to hide its primary malicious payload from users and automated scanners. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Please note that because this binary is identified as an **installer stub/wrapper**, many indicators point toward the tools used by the author rather than unique malicious infrastructure.

### **IP addresses / URLs / Domains**
*   **http://nsis.sf.net/NSIS_Error** (Note: This is a standard URL for the Nullsoft Script Installer; its presence confirms the use of the NSIS framework to wrap the payload.)

### **File paths / Registry keys**
*   *None.* (All identified paths, such as `Control Panel\Desktop` and `Software\Microsoft\Windows\CurrentVersion`, are standard Windows system paths and have been excluded as false positives.)

### **Mutex names / Named pipes**
*   *None detected.*

### **Hashes**
*   *None found in the provided text.*

### **Other artifacts**
*   **Tooling Identification:** NSIS (Nullsoft Script Installer) framework. 
*   **Function Signatures:** 
    *   `fcn.00401434`: Identified as a large "Command Dispatcher" switch-case block (indicates script interpretation).
    *   `fcn.00405f17`: Identified as a custom integrity/checksum calculation routine used to verify dropped files.
*   **Behavioral Indicators:** 
    *   Dropper/Loader behavior: Use of `GetTempPathA`, `CopyFileA`, and `MoveFileA` to stage components.
    *   Execution logic: Utilization of `ShellExecuteA` and `CreateProcessA` to launch secondary payloads.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

**Key evidence**:
*   **Wrapper/Stub Behavior:** The analysis identifies the binary as an NSIS (Nullsoft Script Installer) wrapper, designed to act as a middleman that extracts, verifies, and executes a secondary payload while masking its presence from static analysis.
*   **Multi-Stage Execution:** The use of `GetTempPathA`, `CopyFileA`, and `MoveFileA` combined with `CreateProcessA`/`ShellExecuteA` confirms the binary's primary role is to stage and launch a subsequent file (the actual malicious payload).
*   **Evasion Techniques:** The implementation of dynamic function resolution (`GetProcAddress`/`LoadLibraryA`) and a large "Command Dispatcher" switch-case indicates an intentional effort to hide functionality from automated security scanners.
