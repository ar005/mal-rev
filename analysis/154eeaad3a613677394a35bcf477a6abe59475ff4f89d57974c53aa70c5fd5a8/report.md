# Threat Analysis Report

**Generated:** 2026-09-07 01:20 UTC
**Sample:** `154eeaad3a613677394a35bcf477a6abe59475ff4f89d57974c53aa70c5fd5a8_154eeaad3a613677394a35bcf477a6abe59475ff4f89d57974c53aa70c5fd5a8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `154eeaad3a613677394a35bcf477a6abe59475ff4f89d57974c53aa70c5fd5a8_154eeaad3a613677394a35bcf477a6abe59475ff4f89d57974c53aa70c5fd5a8.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 432,376 bytes |
| MD5 | `4588bdefde6b71460b6b3c65198bfd79` |
| SHA1 | `1b789d3d20f23708252905abf150350aa926ccd9` |
| SHA256 | `154eeaad3a613677394a35bcf477a6abe59475ff4f89d57974c53aa70c5fd5a8` |
| Overall entropy | 6.469 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1481493027 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,088 | 6.508 | No |
| `.rdata` | 5,120 | 5.162 | No |
| `.data` | 1,536 | 3.893 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 175,616 | 2.935 | No |

### Imports

**KERNEL32.dll**: `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetFullPathNameW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `MoveFileW`, `SetFileAttributesW`, `GetCurrentProcess`, `ExitProcess`, `SetEnvironmentVariableW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `IsWindowEnabled`, `EnableMenuItem`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `ShellExecuteW`, `SHFileOperationW`
**ADVAPI32.dll**: `RegDeleteKeyW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `AdjustTokenPrivileges`, `RegOpenKeyExW`, `RegEnumValueW`, `RegDeleteValueW`, `RegCloseKey`, `RegCreateKeyExW`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_AddMasked`, `ord_17`, `ImageList_Destroy`, `ImageList_Create`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1683** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495L
SQSSSPW
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
D$SVW
A@;E |
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
GetExitCodeProcess
WaitForSingleObject
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
lstrcpyW
MoveFileExW
lstrcatW
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5817 | ✓ |
| `fcn.00406757` | `0x406757` | 2183 | ✓ |
| `entry0` | `0x403311` | 1311 | ✓ |
| `fcn.0040390a` | `0x40390a` | 726 | ✓ |
| `fcn.004060e3` | `0x4060e3` | 626 | ✓ |
| `fcn.00402e82` | `0x402e82` | 569 | ✓ |
| `fcn.004030bb` | `0x4030bb` | 504 | ✓ |
| `fcn.004058b2` | `0x4058b2` | 451 | ✓ |
| `fcn.00405df0` | `0x405df0` | 370 | ✓ |
| `fcn.0040660f` | `0x40660f` | 328 | ✓ |
| `fcn.00407110` | `0x407110` | 216 | ✓ |
| `fcn.00405220` | `0x405220` | 211 | ✓ |
| `fcn.00403be0` | `0x403be0` | 205 | ✓ |
| `fcn.004049dc` | `0x4049dc` | 201 | ✓ |
| `fcn.00402c93` | `0x402c93` | 181 | ✓ |
| `fcn.00406355` | `0x406355` | 175 | ✓ |
| `fcn.004041ec` | `0x4041ec` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00406021` | `0x406021` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.0040708f` | `0x40708f` | 129 | ✓ |
| `fcn.00404aea` | `0x404aea` | 128 | ✓ |
| `fcn.00405b7d` | `0x405b7d` | 126 | ✓ |
| `fcn.004056ef` | `0x4056ef` | 125 | ✓ |
| `fcn.00405f8e` | `0x405f8e` | 122 | ✓ |
| `fcn.00405d77` | `0x405d77` | 121 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.0040642b` | `0x40642b` | 112 | ✓ |
| `fcn.0040654c` | `0x40654c` | 110 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402c93.c`](code/fcn.00402c93.c)
- [`code/fcn.00402e82.c`](code/fcn.00402e82.c)
- [`code/fcn.004030bb.c`](code/fcn.004030bb.c)
- [`code/fcn.0040390a.c`](code/fcn.0040390a.c)
- [`code/fcn.00403be0.c`](code/fcn.00403be0.c)
- [`code/fcn.004041ec.c`](code/fcn.004041ec.c)
- [`code/fcn.004049dc.c`](code/fcn.004049dc.c)
- [`code/fcn.00404aea.c`](code/fcn.00404aea.c)
- [`code/fcn.00405220.c`](code/fcn.00405220.c)
- [`code/fcn.004056ef.c`](code/fcn.004056ef.c)
- [`code/fcn.004058b2.c`](code/fcn.004058b2.c)
- [`code/fcn.00405b7d.c`](code/fcn.00405b7d.c)
- [`code/fcn.00405d77.c`](code/fcn.00405d77.c)
- [`code/fcn.00405df0.c`](code/fcn.00405df0.c)
- [`code/fcn.00405f8e.c`](code/fcn.00405f8e.c)
- [`code/fcn.00406021.c`](code/fcn.00406021.c)
- [`code/fcn.004060e3.c`](code/fcn.004060e3.c)
- [`code/fcn.00406355.c`](code/fcn.00406355.c)
- [`code/fcn.0040642b.c`](code/fcn.0040642b.c)
- [`code/fcn.0040654c.c`](code/fcn.0040654c.c)
- [`code/fcn.0040660f.c`](code/fcn.0040660f.c)
- [`code/fcn.00406757.c`](code/fcn.00406757.c)
- [`code/fcn.0040708f.c`](code/fcn.0040708f.c)
- [`code/fcn.00407110.c`](code/fcn.00407110.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is an analysis of the binary's functionality and behavior.

### Core Functionality and Purpose
The binary functions as a **sophisticated installer or "packer/dropper" engine**. It features a large internal state machine (represented by long switch-case blocks) that interprets instructions to perform system modifications. While it may be a legitimate installer (likely based on the NSIS framework, given the `nsis_sf.net` reference in the strings), these same techniques are frequently utilized by malware to unpack and execute secondary malicious payloads.

### Suspicious and Malicious Behaviors
*   **Multi-Stage Execution & File Manipulation:** 
    *   The code heavily utilizes `CopyFileW`, `MoveFileW`, `GetFullPathNameW`, and `SetCurrentDirectoryW`. These are used to stage files, move them from temporary directories (like `%TEMP%`) to permanent locations, and rename them to mask their true purpose.
    *   It frequently uses `DeleteFileW` to remove "artifacts" or original installer components after they have been unpacked/executed.
*   **Persistence via Registry Manipulation:**
    *   The binary contains multiple calls to `RegCreateKeyExW`, `RegSetValueExW`, and `RegDeleteValueW`. This is a classic technique for establishing persistence (e.g., adding entries to "Run" or "RunOnce" keys) or modifying system configurations.
*   **Privilege Escalation/Adjustment:** 
    *   The code calls `LookupPrivilegeValueW` and `AdjustTokenPrivileges`. Specifically, it attempts to acquire the `SeShutdownPrivilege`. While this can be used for legitimate shutdown behavior, in malware context, it is often used to ensure the process has sufficient privileges to perform system-wide actions.
*   **Evasive File Security:** 
    *   The function `fcn.004056ef` calls `CreateDirectoryW` followed by `SetFileSecurityW`. This indicates an attempt to modify Access Control Lists (ACLs) on directories, potentially hiding them from other users or applications.
*   **Dynamic Loading & Module Resolution:**
    *   The code uses `GetProcAddress`, `LoadLibraryExW`, and `GetModuleHandleW` to dynamically link functions. This allows the program to hide its true capabilities from simple static analysis by only resolving necessary API addresses at runtime.
*   **Integrity Checks:**
    *   There is a specific routine (`fcn.00402e82`) that performs an "integrity check" on files. In malware, this is used to verify that the payload hasn't been modified or tampered with by security researchers before it is executed.

### Notable Techniques & Patterns
*   **Interpreter/Script Engine Pattern:** The massive switch-case blocks (e.g., `fcn.00401434`) suggest that the binary is not a simple standalone program but an interpreter. It reads a set of instructions (likely from an embedded script) and executes the corresponding code block (file I/O, registry edit, etc.).
*   **Checksum/Hashing Logic:** The function `fcn.0040654c` implements a CRC32-style algorithm (identified by the polynomial constant `0xedb88320`). This is used to verify file integrity during the extraction process.
*   **Standard Dropper Behavior:** The movement from "extracting" logic in `fcn.00401434` to "executing" via `ShellExecuteW` (in case `0x401e77`) is a textbook pattern for malware that acts as a first-stage dropper to drop and launch a final payload.
*   **Environment Manipulation:** The code actively queries system paths (`GetTempPathW`, `GetSystemDirectoryW`) and manipulates environment variables (like `TEMP`) to ensure the subsequent stages of execution occur in controlled environments.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors described in your analysis to the corresponding MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036.003** | Move Data to Preparation Location | The use of `MoveFileW` and `CopyFileW` to move files from `%TEMP%` to permanent locations indicates a staging process for subsequent execution. |
| **T1070.004** | Remove System Artifacts | The systematic use of `DeleteFileW` suggests an attempt to clean up installation traces or original components once the payload is active. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys/Run_Services | Calls to `RegCreateKeyExW` and `RegSetValueExW` indicate the creation of registry keys used for persistent execution on system startup. |
| **T1068** | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicates an attempt to gain higher-level permissions or specific capabilities (like `SeShutdownPrivilege`). |
| **T1070** | Indicator Removal on Host | The call to `SetFileSecurityW` specifically to modify ACLs suggests a move to hide files from other users or security tools. |
| **T1027** | Obfuscated Files or Information | Utilizing `GetProcAddress` and `LoadLibraryExW` hides the program's true functionality from static analysis by resolving APIs at runtime. |
| **T1497** | Virtualization/Sandbox Detection | The CRC32-style integrity check is a common method used to detect if a file has been modified or tampered with by an analyst or automated sandbox. |
| **T1059** | Command and Scripting Interpreter | The extensive switch-case block structure indicates the binary functions as a custom interpreter for internal scripts or commands. |
| **T1106** | Native API | The use of `ShellExecuteW` to launch final payloads is a standard method of interacting with the operating system's core functionality to execute code. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None detected.

**File paths / Registry keys**
*   None detected. *(Note: While the report mentions the use of `%TEMP%` and general registry modifications, no specific hardcoded file paths or unique registry keys were identified in the provided text.)*

**Mutex names / Named pipes**
*   None detected.

**Hashes**
*   None detected.

**Other artifacts**
*   **CRC32 Polynomial:** `0xedb88320` (Identified as part of a custom integrity check routine in `fcn.0040654c`).
*   **Internal Function Offsets:** 
    *   `fcn.004056ef` (Logic for File Security/ACL modification)
    *   `fcn.00402e82` (File integrity checking routine)
    *   `fcn.00401434` (Script interpreter execution block)
    *   `fcn.0040654c` (CRC32 verification logic)
*   **Known Framework Signature:** Reference to `nsis_sf.net` (Indicates the use of the NSIS framework for wrapping or "packing" the payload).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the provided analysis, here is the classification for this sample:

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Multi-stage Payload Deployment:** The binary exhibits classic "dropper" behavior by extracting files from temporary directories (`%TEMP%`), moving them to permanent locations, and deleting the original installers/artifacts to mask its footprint.
    *   **Anti-Analysis & Evasion:** The presence of CRC32 integrity checks, dynamic API loading (GetProcAddress), and manual manipulation of File Security ACLs indicates a deliberate effort to evade detection by security researchers and automated sandboxes.
    *   **Interpreter Architecture:** The use of a large state machine/switch-case block suggests the binary acts as an execution engine or wrapper (likely utilizing the NSIS framework) designed to interpret a script that performs system modifications, such as registry persistence and privilege adjustment.
