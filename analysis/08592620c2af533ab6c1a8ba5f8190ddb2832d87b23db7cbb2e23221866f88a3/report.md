# Threat Analysis Report

**Generated:** 2026-07-18 04:53 UTC
**Sample:** `08592620c2af533ab6c1a8ba5f8190ddb2832d87b23db7cbb2e23221866f88a3_08592620c2af533ab6c1a8ba5f8190ddb2832d87b23db7cbb2e23221866f88a3.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `08592620c2af533ab6c1a8ba5f8190ddb2832d87b23db7cbb2e23221866f88a3_08592620c2af533ab6c1a8ba5f8190ddb2832d87b23db7cbb2e23221866f88a3.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 90,792,252 bytes |
| MD5 | `0b2b67908943e69f026a59447cd9dac9` |
| SHA1 | `04c3c784a9fa11775ab4a4b9a7913e3664d98127` |
| SHA256 | `08592620c2af533ab6c1a8ba5f8190ddb2832d87b23db7cbb2e23221866f88a3` |
| Overall entropy | 8.0 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1117309320 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 23,552 | 6.455 | No |
| `.rdata` | 4,608 | 5.233 | No |
| `.data` | 1,024 | 5.207 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 1,112,064 | 7.72 | ⚠️ Yes |

### Imports

**KERNEL32.dll**: `CompareFileTime`, `SearchPathA`, `GetShortPathNameA`, `GetFullPathNameA`, `MoveFileA`, `lstrcatA`, `SetCurrentDirectoryA`, `GetFileAttributesA`, `GetLastError`, `CreateDirectoryA`, `SetFileAttributesA`, `Sleep`, `GetFileSize`, `GetModuleFileNameA`, `GetTickCount`
**USER32.dll**: `SystemParametersInfoA`, `RegisterClassA`, `EndDialog`, `ScreenToClient`, `GetWindowRect`, `SetClassLongA`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongA`, `LoadCursorA`, `SetCursor`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapA`
**GDI32.dll**: `SetBkColor`, `GetDeviceCaps`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectA`, `SetBkMode`, `SetTextColor`, `SelectObject`
**SHELL32.dll**: `SHGetMalloc`, `SHGetPathFromIDListA`, `SHBrowseForFolderA`, `ShellExecuteA`, `SHFileOperationA`, `SHGetSpecialFolderLocation`
**ADVAPI32.dll**: `RegQueryValueExA`, `RegSetValueExA`, `RegEnumKeyA`, `RegEnumValueA`, `RegOpenKeyExA`, `RegDeleteKeyA`, `RegDeleteValueA`, `RegCloseKey`, `RegCreateKeyExA`
**COMCTL32.dll**: `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`, `ImageList_Create`
**ole32.dll**: `OleInitialize`, `OleUninitialize`, `CoCreateInstance`
**VERSION.dll**: `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`, `VerQueryValueA`

## Extracted Strings

Total strings found: **195637** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9uu
 s495L
tQVPW
Et@;u
Instu|
softus
Nulluj
t
9uu
8NCRCu
> _?=t
D$(VPV
D$(+D$ SSP
D$0+D$(P
9uu;9=
SVSPQh

FFC;]
uQQQQQ
8\th
8\tPV
<a|
<z
D.
PWj
tWWWWj
&u)WhD
HtVHtHH
MulDiv
DeleteFileA
FindFirstFileA
FindNextFileA
FindClose
SetFilePointer
ReadFile
WriteFile
GetPrivateProfileStringA
WritePrivateProfileStringA
MultiByteToWideChar
FreeLibrary
GetProcAddress
LoadLibraryA
GetModuleHandleA
SetErrorMode
GetExitCodeProcess
WaitForSingleObject
GlobalFree
ExpandEnvironmentStringsA
GetEnvironmentVariableA
lstrcmpiA
CloseHandle
SetFileTime
CompareFileTime
SearchPathA
GetShortPathNameA
GetFullPathNameA
MoveFileA
lstrcatA
SetCurrentDirectoryA
GetFileAttributesA
GetLastError
CreateDirectoryA
SetFileAttributesA
GetFileSize
GetModuleFileNameA
GetTickCount
GetCurrentProcess
CopyFileA
ExitProcess
lstrcpynA
GetCommandLineA
GetWindowsDirectoryA
GetTempPathA
GetUserDefaultLangID
GetDiskFreeSpaceA
GlobalUnlock
GlobalLock
GlobalAlloc
CreateThread
CreateProcessA
RemoveDirectoryA
CreateFileA
GetTempFileNameA
SetEndOfFile
UnmapViewOfFile
MapViewOfFile
CreateFileMappingA
lstrcpyA
lstrlenA
GetSystemDirectoryA
KERNEL32.dll
EndPaint
DrawTextA
FillRect
GetClientRect
BeginPaint
DefWindowProcA
SendMessageA
InvalidateRect
DispatchMessageA
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401444` | `0x401444` | 5405 | ✓ |
| `fcn.00405d11` | `0x405d11` | 2639 | ✓ |
| `entry0` | `0x40319e` | 928 | ✓ |
| `fcn.00406808` | `0x406808` | 827 | ✓ |
| `fcn.00402c57` | `0x402c57` | 670 | ✓ |
| `fcn.00403563` | `0x403563` | 607 | ✓ |
| `fcn.0040598f` | `0x40598f` | 564 | ✓ |
| `fcn.00402ef5` | `0x402ef5` | 556 | ✓ |
| `fcn.004056c0` | `0x4056c0` | 439 | ✓ |
| `fcn.004052e5` | `0x4052e5` | 420 | ✓ |
| `fcn.004037c2` | `0x4037c2` | 229 | ✓ |
| `fcn.00404d3b` | `0x404d3b` | 215 | ✓ |
| `fcn.00403df6` | `0x403df6` | 173 | ✓ |
| `fcn.004011f9` | `0x4011f9` | 171 | ✓ |
| `fcn.00401378` | `0x401378` | 163 | ✓ |
| `fcn.00405bc3` | `0x405bc3` | 162 | ✓ |
| `fcn.0040452b` | `0x40452b` | 152 | ✓ |
| `fcn.004012ed` | `0x4012ed` | 139 | ✓ |
| `fcn.004058fa` | `0x4058fa` | 137 | ✓ |
| `fcn.00402afa` | `0x402afa` | 135 | ✓ |
| `fcn.0040556a` | `0x40556a` | 115 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00405ca3` | `0x405ca3` | 110 | ✓ |
| `fcn.00405877` | `0x405877` | 106 | ✓ |
| `fcn.004067a0` | `0x4067a0` | 104 | ✓ |
| `fcn.00404e12` | `0x404e12` | 101 | ✓ |
| `fcn.0040521c` | `0x40521c` | 86 | ✓ |
| `fcn.0040551d` | `0x40551d` | 77 | ✓ |
| `fcn.004045f0` | `0x4045f0` | 76 | ✓ |
| `fcn.004055dd` | `0x4055dd` | 76 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011f9.c`](code/fcn.004011f9.c)
- [`code/fcn.004012ed.c`](code/fcn.004012ed.c)
- [`code/fcn.00401378.c`](code/fcn.00401378.c)
- [`code/fcn.00401444.c`](code/fcn.00401444.c)
- [`code/fcn.00402afa.c`](code/fcn.00402afa.c)
- [`code/fcn.00402c57.c`](code/fcn.00402c57.c)
- [`code/fcn.00402ef5.c`](code/fcn.00402ef5.c)
- [`code/fcn.00403563.c`](code/fcn.00403563.c)
- [`code/fcn.004037c2.c`](code/fcn.004037c2.c)
- [`code/fcn.00403df6.c`](code/fcn.00403df6.c)
- [`code/fcn.0040452b.c`](code/fcn.0040452b.c)
- [`code/fcn.004045f0.c`](code/fcn.004045f0.c)
- [`code/fcn.00404d3b.c`](code/fcn.00404d3b.c)
- [`code/fcn.00404e12.c`](code/fcn.00404e12.c)
- [`code/fcn.0040521c.c`](code/fcn.0040521c.c)
- [`code/fcn.004052e5.c`](code/fcn.004052e5.c)
- [`code/fcn.0040551d.c`](code/fcn.0040551d.c)
- [`code/fcn.0040556a.c`](code/fcn.0040556a.c)
- [`code/fcn.004055dd.c`](code/fcn.004055dd.c)
- [`code/fcn.004056c0.c`](code/fcn.004056c0.c)
- [`code/fcn.00405877.c`](code/fcn.00405877.c)
- [`code/fcn.004058fa.c`](code/fcn.004058fa.c)
- [`code/fcn.0040598f.c`](code/fcn.0040598f.c)
- [`code/fcn.00405bc3.c`](code/fcn.00405bc3.c)
- [`code/fcn.00405ca3.c`](code/fcn.00405ca3.c)
- [`code/fcn.00405d11.c`](code/fcn.00405d11.c)
- [`code/fcn.004067a0.c`](code/fcn.004067a0.c)
- [`code/fcn.00406808.c`](code/fcn.00406808.c)

## Behavioral Analysis

Based on my analysis of the provided disassembly and strings, here is a summary of the code's functionality and behaviors.

### Core Functionality and Purpose
The binary functions primarily as an **installer executable**, specifically appearing to be based on or heavily utilizing the **NSIS (Nullsoft Script Installer)** framework. 

Its primary role is to:
*   **Verify Integrity:** It performs checks to ensure that files are not "corrupted or incomplete" before installation (as evidenced by the `verifying installer` and `CRC-related` logic).
*   **File System Management:** It handles complex file operations including creating directories, moving files (`MoveFileA`), setting file attributes, and resolving system paths for special folders (e.g., Start Menu, Desktop) using Shell32 APIs.
*   **Registry Manipulation:** It reads from and writes to the Windows Registry to configure settings or ensure persistence for its components.

### Suspicious or Malicious Behaviors
While the primary purpose is an installer, several elements are common in "droppers" or installers used to deliver malware:

*   **Privilege Escalation Attempt:** The code explicitly uses `LookupPrivilegeValueA`, `OpenProcessToken`, and `AdjustTokenPrivileges` to request `SeShutdownPrivilege`. While this can be legitimate for system-wide installations, it is a classic technique used by malware to gain higher privileges from the current user session.
*   **Persistence/System File Manipulation:** There is specific logic involving the creation of or writing to **`wininit.ini`**. In modern Windows versions, modifying `wininit.ini` or interacting with files in that context can be a technique used to influence system boot behavior or persistence.
*   **Detection Evasion / Obfuscation:** The use of generic error messages (e.g., "The installer you are trying to use is corrupted... This could be the result of... a virus") serves as a fallback. If certain anti-analysis checks or missing file dependencies occur, it presents a plausible excuse for failure rather than crashing or showing technical errors that would alert a user or researcher.
*   **Complex Path Resolution:** The extensive usage of `SHGetSpecialFolderLocation` and subsequent manipulation suggests the installer is designed to "find" where it should hide or reside on the system automatically.

### Notable Techniques & Patterns
*   **NSIS Framework Signature:** The string `A~NSISu_.exe`, the specific error message regarding "corrupted" installers, and the logic for "verifying installer" are standard indicators of an NSIS-based setup. 
*   **Robust Error Handling:** The code uses a large switch/jump table (seen in `fcn.00401444`) to manage various state transitions during the installation process, ensuring that even if one method of file movement fails, it attempts others.
*   **API Wrapping:** It heavily utilizes standard Windows APIs (`kernel32`, `user32`, `advapi32`) but hides them behind internal wrapper functions (e.g., `fcn.004052e5` and `fcn.00401378`), which is common in both legitimate installers and malware to manage complex logic more cleanly.
*   **"Decoy" Logic:** The heavy presence of UI-related functions (`GetDlgItem`, `SetWindowTextA`) suggests the installer interacts with a GUI, but it also performs "under-the-hood" system modifications (Registry/Privileges) that don't require user interaction.

### Summary for Investigation
This binary is likely an **installer or dropper**. While the presence of NSIS indicates it is designed to deploy software, the inclusion of **privilege escalation** and **system-level file manipulation** makes it highly suspicious. It should be treated as a potential delivery vehicle (dropper) for a secondary payload.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1548** | Abuse Elevation Control Mechanism | The binary explicitly uses `LookupPrivilegeValueA` and `AdjustTokenPrivileges` to acquire system-level privileges (e.g., `SeShutdownPrivilege`). |
| **T1546** | Persistence | The manipulation of the Registry and modification of system files like `wininit.ini` are indicators of attempts to maintain a presence on the host. |
| **T1036** | Masquerading | The use of the NSIS framework and standard installer logic allows the binary to hide its malicious intent by appearing as a legitimate software installer. |
| **T1083** | File and Directory Discovery | The extensive use of `SHGetSpecialFolderLocation` indicates automated logic to find specific system paths for installation or concealment. |
| **T1027** | Obfuscated Files or Information | The use of generic error messages instead of technical alerts serves to mislead researchers during anti-analysis checks. |
| **T1105** | Ingress Tool Transfer (Note: Contextual) | While the binary is a "dropper," its role in moving files and preparing the environment fulfills the delivery aspect of malicious payloads. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `wininit.ini` (Identified as a target for potential persistence/system behavior manipulation)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None provided in the source text)*

**Other artifacts**
*   **NSIS Framework Indicators:** 
    *   `A~NSISu_.exe` (Indicates use of Nullsoft Script Installer)
    *   "The installer you are trying to use is corrupted or incomplete." (Standard NSIS error message)
    *   "verifying installer: %d%%" (Internal NSIS verification string)
*   **Privilege Escalation Indicators:** 
    *   `SeShutdownPrivilege` (Specifically sought via `LookupPrivilegeValueA` and `AdjustTokenPrivileges`)
*   **Behavioral Note:** The binary exhibits "dropper" characteristics by using legitimate installer frameworks to mask the execution of privilege escalation and system-level file manipulation.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**:
    * **Masquerading as a legitimate installer:** The binary utilizes the NSIS framework to hide its actions behind common installation logic, including standard "corrupted file" error messages to deflect suspicion during analysis.
    * **Privilege Escalation and Persistence:** The sample actively attempts to gain elevated privileges (`SeShutdownPrivilege`) and targets system files like `wininit.ini` to ensure it can maintain a presence on the host.
    * **Environment Preparation:** The extensive use of `Shell32` APIs for path resolution and registry manipulation indicates the file is designed to "prime" the system for a secondary malicious payload.
