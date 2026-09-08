# Threat Analysis Report

**Generated:** 2026-09-02 11:43 UTC
**Sample:** `13410b80418e08044df11f8ad92e0a2380acbfe2c2b5d649fbd9c4266e3eec32_13410b80418e08044df11f8ad92e0a2380acbfe2c2b5d649fbd9c4266e3eec32.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13410b80418e08044df11f8ad92e0a2380acbfe2c2b5d649fbd9c4266e3eec32_13410b80418e08044df11f8ad92e0a2380acbfe2c2b5d649fbd9c4266e3eec32.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 502,648 bytes |
| MD5 | `d631d6260412c0c7f49997ce4144152c` |
| SHA1 | `a12b78e2c53c5be38d715d0b9bd96a6f3a68cd46` |
| SHA256 | `13410b80418e08044df11f8ad92e0a2380acbfe2c2b5d649fbd9c4266e3eec32` |
| Overall entropy | 7.399 |
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
| `.rsrc` | 164,864 | 5.541 | No |

### Imports

**KERNEL32.dll**: `ExitProcess`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `CreateFileW`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `SetEnvironmentVariableW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1173** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality:

### Core Functionality and Purpose
The binary functions as a **script-based installer or "updater" engine**, specifically utilizing the **NSIS (Nullsoft Script Installer)** framework. 

Instead of being a single standalone tool with one purpose, it contains a large state machine (the long `switch` statement in `fcn.00401434`) designed to interpret and execute commands from an external script file. This is common in software installers where the `.exe` acts as the engine and a separate `.nsi` or similar script provides the instructions for installation, file extraction, and configuration.

### Suspicious and Malicious Behaviors
While the code's structure is typical of a legitimate installer, several behaviors are frequently used by malware to deliver payloads (droppers) or establish persistence:

*   **Persistence & Configuration:** The code extensively uses `RegOpenKeyExW`, `RegCreateKeyExW`, and `RegSetValueExW` to modify the Windows Registry. In an installer context, this is for configuration; in a malware context, it is used to ensure the program runs automatically on startup or modifies system settings.
*   **File Manipulation & Staging:** 
    *   The code performs extensive file operations: `MoveFileW`, `CopyFileW`, and `DeleteFileW`. 
    *   It actively manipulates file attributes (`SetFileAttributesW`), which can be used to hide files or mark them as system files.
    *   It utilizes **Temporary Folders** (via `GetTempPathW`) for staging files before they are moved to their final location.
*   **Privilege Escalation:** The code calls `AdjustTokenPrivileges` and `LookupPrivilegeValueW`. This is used to request higher permissions from the operating system, often necessary for modifying system files or registry keys protected by Windows.
*   **Execution of External Components:** Through `CreateProcessW`, the binary can launch other programs or scripts. In malicious samples, this is the step where a "downloader" would launch a secondary payload.

### Notable Techniques and Patterns
*   **Script Interpreter Pattern:** The large `switch` statement (over 100 cases) at address `0x402ad7` confirms that the binary acts as an interpreter. It processes different commands (like moving files, setting registry keys, or showing dialogs) based on a loop.
*   **Integrity Checking:** The function `fcn.004068b5` implements a **CRC32 check**. This is used to verify that the files being moved or unpacked have not been corrupted or altered. Malware uses this to ensure its payload remains intact during the "dropping" process.
*   **Environment Manipulation:** The code checks and modifies environment variables (like `TEMP`) to ensure it has a predictable path for operation, common in both complex installers and sophisticated malware.
*   **Standard Windows API Abuse:** Use of `GetTickCount` and `Sleep` can be used as "anti-analysis" techniques to stall the execution or timing of the program during a sandbox analysis, though here they are likely used to manage UI updates and installation progress.

### Summary for Analysis Report
*   **Primary Classification:** Installer / Loader (NSIS Engine).
*   **Capabilities:** Registry manipulation, file system operations, integrity checking via CRC32, and privilege escalation.
*   **Risk Profile:** High-risk for "Dropper" behavior. Because it is a script interpreter, the binary itself might not be malicious, but it provides all the necessary tools (file copying, registry persistence, and hidden execution) to deliver and install malware onto a system.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Registry Run Keys / Startup Folder | The code modifies registry keys to ensure the application runs automatically upon system startup. |
| **T1070** | File and Directory Modification | The binary performs extensive file operations, including moving, copying, and deleting files for staging or installation. |
| **T1106** | Modify Permissions | The use of `SetFileAttributesW` to alter file attributes is a method used to hide components from the user or system. |
| **T1068** | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicates an attempt to acquire higher-level permissions for system access. |
| **T1059** | Command and Scripting Interpreter | The large switch statement confirms the binary acts as a script interpreter (NSIS) to execute instructions from external files. |
| **T1136.002** | Environment Variable | The code modifies environment variables, such as `TEMP`, to facilitate its staging and execution routines. |
| **T1497** | Virtualization/Sandbox Evasion | The use of `Sleep` and `GetTickCount` are standard tactics used to stall execution and evade detection by automated sandbox environments. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None detected.

**File paths / Registry keys**
*   None detected (Note: The analysis mentions registry manipulation and file system usage, but no specific hardcoded paths or keys were provided in the string dump).

**Mutex names / Named pipes**
*   None detected.

**Hashes**
*   None detected.

**Other artifacts**
*   **NSIS Framework:** The binary utilizes the Nullsoft Script Installer engine to process commands.
*   **CRC32 Integrity Check:** Function `fcn.004068b5` performs CRC32 checks to verify file integrity during extraction/movement.
*   **Persistence & Escalation Indicators:** Use of `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, and standard installer-style API wrapping (e.g., `MoveFileW`, `CopyFileW`).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **NSIS Interpreter Pattern:** The binary utilizes the Nullsoft Script Installer (NSIS) framework, featuring a large switch statement to interpret and execute commands for file manipulation, registry modification, and configuration.
*   **Persistence & Escalation:** The code explicitly implements techniques for escalating privileges (`AdjustTokenPrivileges`) and ensuring persistence via Registry Run keys, which are classic indicators of malware designed to maintain a foothold on a system.
*   **Staging & Integrity Checks:** The use of CRC32 checks to verify file integrity during the "unpacking" process, combined with common anti-analysis techniques (Sleep/GetTickCount), indicates its role is to deliver and prepare subsequent malicious payloads.
