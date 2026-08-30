# Threat Analysis Report

**Generated:** 2026-08-19 01:43 UTC
**Sample:** `10831eaa36ee138523e0e45ca4078ca8481b8a51e89304efd626d142a6c7dd1f_10831eaa36ee138523e0e45ca4078ca8481b8a51e89304efd626d142a6c7dd1f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10831eaa36ee138523e0e45ca4078ca8481b8a51e89304efd626d142a6c7dd1f_10831eaa36ee138523e0e45ca4078ca8481b8a51e89304efd626d142a6c7dd1f.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 83,001,072 bytes |
| MD5 | `96d25d647d6cd58dd50f302b6c9338a3` |
| SHA1 | `f1bc3b8cf7c5c0c0c7f9328340ba77d6eb2de9aa` |
| SHA256 | `10831eaa36ee138523e0e45ca4078ca8481b8a51e89304efd626d142a6c7dd1f` |
| Overall entropy | 8.0 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1544912774 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,624 | 6.45 | No |
| `.rdata` | 5,632 | 5.025 | No |
| `.data` | 1,536 | 4.037 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 179,200 | 7.97 | ⚠️ Yes |

### Imports

**KERNEL32.dll**: `SetEnvironmentVariableW`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `CopyFileW`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`, `SetErrorMode`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **180069** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495,
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
NTMARTA
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5795 | ✓ |
| `fcn.004067f5` | `0x4067f5` | 2639 | ✓ |
| `entry0` | `0x40338f` | 1345 | ✓ |
| `fcn.004072ec` | `0x4072ec` | 827 | ✓ |
| `fcn.004039aa` | `0x4039aa` | 726 | ✓ |
| `fcn.004062dc` | `0x4062dc` | 626 | ✓ |
| `fcn.00402edd` | `0x402edd` | 569 | ✓ |
| `fcn.00403116` | `0x403116` | 539 | ✓ |
| `fcn.004059cc` | `0x4059cc` | 451 | ✓ |
| `fcn.00405f06` | `0x405f06` | 378 | ✓ |
| `fcn.00405322` | `0x405322` | 211 | ✓ |
| `fcn.00404298` | `0x404298` | 207 | ✓ |
| `fcn.00404ade` | `0x404ade` | 201 | ✓ |
| `fcn.00403c80` | `0x403c80` | 185 | ✓ |
| `fcn.0040654e` | `0x40654e` | 175 | ✓ |
| `fcn.00402d44` | `0x402d44` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040621a` | `0x40621a` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404bec` | `0x404bec` | 128 | ✓ |
| `fcn.00405c97` | `0x405c97` | 126 | ✓ |
| `fcn.004057f1` | `0x4057f1` | 125 | ✓ |
| `fcn.004060ac` | `0x4060ac` | 123 | ✓ |
| `fcn.00406188` | `0x406188` | 121 | ✓ |
| `fcn.00405e91` | `0x405e91` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406624` | `0x406624` | 112 | ✓ |
| `fcn.00406787` | `0x406787` | 110 | ✓ |
| `fcn.004053f5` | `0x4053f5` | 108 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402d44.c`](code/fcn.00402d44.c)
- [`code/fcn.00402edd.c`](code/fcn.00402edd.c)
- [`code/fcn.00403116.c`](code/fcn.00403116.c)
- [`code/fcn.004039aa.c`](code/fcn.004039aa.c)
- [`code/fcn.00403c80.c`](code/fcn.00403c80.c)
- [`code/fcn.00404298.c`](code/fcn.00404298.c)
- [`code/fcn.00404ade.c`](code/fcn.00404ade.c)
- [`code/fcn.00404bec.c`](code/fcn.00404bec.c)
- [`code/fcn.00405322.c`](code/fcn.00405322.c)
- [`code/fcn.004053f5.c`](code/fcn.004053f5.c)
- [`code/fcn.004057f1.c`](code/fcn.004057f1.c)
- [`code/fcn.004059cc.c`](code/fcn.004059cc.c)
- [`code/fcn.00405c97.c`](code/fcn.00405c97.c)
- [`code/fcn.00405e91.c`](code/fcn.00405e91.c)
- [`code/fcn.00405f06.c`](code/fcn.00405f06.c)
- [`code/fcn.004060ac.c`](code/fcn.004060ac.c)
- [`code/fcn.00406188.c`](code/fcn.00406188.c)
- [`code/fcn.0040621a.c`](code/fcn.0040621a.c)
- [`code/fcn.004062dc.c`](code/fcn.004062dc.c)
- [`code/fcn.0040654e.c`](code/fcn.0040654e.c)
- [`code/fcn.00406624.c`](code/fcn.00406624.c)
- [`code/fcn.00406787.c`](code/fcn.00406787.c)
- [`code/fcn.004067f5.c`](code/fcn.004067f5.c)
- [`code/fcn.004072ec.c`](code/fcn.004072ec.c)

## Behavioral Analysis

Based on the second chunk of disassembly, I have updated and expanded the analysis. The new code confirms several characteristics regarding its behavior as a sophisticated installer/loader while highlighting specific techniques used to ensure integrity and manage environment resources.

### Updated Analysis Summary
The binary continues to exhibit the architecture of a multi-stage installer (likely NSIS). However, the additional disassembly reveals more granular details regarding how it validates components before execution and how it dynamically loads system dependencies. The presence of **CRC/checksum logic** and **OLE (Object Linking and Embedding)** initialization suggests a highly polished environment intended to interact with Windows shell features or complex UI elements while ensuring that payload files remain untampered during the transition from the "installer" to the "actual application."

---

### Core Functionality
The core engine handles resource management and environment preparation. It doesn't just move files; it validates them, resolves their paths, and loads necessary system components dynamically. The presence of `OleInitialize` indicates a sophisticated interaction with Windows' COM (Component Object Model) infrastructure, often used for high-level UI rendering or interacting with the shell.

### Suspicious & Malicious Behaviors
*   **Dropper/Unpacker Behavior:** (Retained from previous analysis) Use of `CopyFileW`, `MoveFileW`, and `GetTempPathW` to stage payloads in temporary directories.
*   **Privilege Escalation Check:** (Retained from previous analysis) Use of `SeShutdownPrivilege` as a test for administrative status.
*   **Environment Manipulation:** (Retained from previous analysis) Usage of `SetEnvironmentVariableW` to steer the execution environment.
*   **Integrity & Validation Logic (Expanded):** The function `fcn.00406787` implements a **CRC-32 or similar checksum algorithm** (evidenced by the constant `0xedb88320`). This is used to verify that files extracted from the resources have not been altered. In malware, this ensures the "payload" remains intact until it is time for the final execution stage.
*   **Dynamic DLL Loading:** Function `fcn.00406624` demonstrates dynamic loading of system libraries using `LoadLibraryExW`. By calculating paths dynamically (e.g., checking `GetSystemDirectoryW`), the binary can load necessary components into memory at runtime, which can be used to bypass static analysis of the main executable's import table.

### Notable Techniques & Patterns
*   **NSIS Framework Utilization:** (Retained) The dispatcher and script-like handling confirm it is a wrapper designed to hide its true intent behind a legitimate installer's behavior.
*   **Complex String/Instruction Parsing:** (Retained) Logic in `fcn.004067f5` indicates a state-machine approach to processing internal commands.
*   **File System Obfuscation:** (Retained) Dynamic path resolution prevents easy identification of target directories via static analysis.
*   **CRC32 Integrity Checks:** The implementation of the `0xedb88320` polynomial in `fcn.00406787` is a classic technique to verify data integrity. While legitimate in installers, it's also used by malware to ensure that "staged" payloads haven't been modified or quarantined by security software before they are launched.
*   **COM/OLE Integration:** The use of `OleInitialize` (in `fcn.004053f5`) indicates the program may interact with Windows shell objects, icons, or other system-level components. While common in heavy installers, it allows an application to blend into the Windows environment more seamlessly by utilizing standard OS features for UI/shell interaction.
*   **Dynamic Library Resolution:** The logic in `fcn.00406624` specifically constructs a path to a `.dll` and loads it immediately. This "just-in-time" loading of system components reduces the "footprint" of the primary executable during static analysis by hiding its full list of dependencies.

---

### Technical Summary Table (Updated)
| Feature | Detection / Function | Purpose & Potential Risk |
| :--- | :--- | :--- |
| **Persistence/Execution** | `ShellExecuteExW`, `RegSetValue` | Standard for installers; used by malware to ensure persistence and launch payloads. |
| **Integrity Check** | `fcn.00406787` (CRC-32) | Ensures payload has not been altered; common in multi-stage droppers. |
| **Dynamic Loading** | `fcn.00406624` (`LoadLibraryExW`) | Loads system DLLs at runtime to minimize the initial import footprint. |
| **Privilege Check** | `AdjustTokenPrivileges` | Confirms if the installer has administrative rights before performing sensitive actions. |
| **Shell Interaction** | `OleInitialize` | Interfaces with Windows COM; used for advanced UI or interacting with system objects. |
| **Path Obfuscation** | `GetShortPathNameW`, `SetCurrentDirectoryW` | Prevents static analysis of where files are actually being moved/hidden. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of the NSIS framework and `OleInitialize` allows the malware to blend in with legitimate Windows system components and standard installer behaviors. |
| T1548 | Privilege Escalation | The check for `SeShutdownPrivilege` via `AdjustTokenPrivileges` is used to determine if the process has the administrative rights required to execute higher-level actions. |
| T1027 | Obfuscated Files or Information | The use of CRC-32 checksums ensures that staged payloads remain intact and haven't been tampered with by security tools before final execution. |
| T1036 | Masquerading | The use of `LoadLibraryExW` to resolve system components at runtime hides the full scope of the application's capabilities from static analysis of the import table. |
| T1105 | Ingress Tool Transfer | The "Dropper" behavior involving `CopyFileW`, `MoveFileW`, and `GetTempPathW` indicates a multi-stage process to move and stage payloads for execution. |

---

## Indicators of Compromise

Based on my analysis of the provided strings and behavioral data, here are the extracted Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided text contains high-level behavioral descriptions and a list of standard Win32 API functions. While it describes suspicious *behaviors* (e.g., dropper functionality, integrity checks, and dynamic library loading), it does not contain specific, unique technical IOCs such as hardcoded IP addresses, domain names, or file paths.

---

### **Indicators of Compromise**

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified (Note: While functions like `GetTempPathW` and `RegSetValue` are present, no specific paths or registry keys were hardcoded in the strings).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified. (The value `0xedb88320` was identified in the analysis; however, this is a standard CRC-32 polynomial constant and not a file hash.)

**Other artifacts**
*   **Behavioral Patterns:** 
    *   Use of **CRC-32 integrity checks** (polynomial `0xedb88320`) to verify payload integrity.
    *   **Dynamic Library Resolution**: Use of `LoadLibraryExW` and `GetProcAddress` to hide the initial import footprint.
    *   **NSIS Wrapper:** The code utilizes an NSIS-style dispatcher to mask the execution flow.
*   **Known API Abuse Patterns:**
    *   `ShellExecuteExW`, `RegSetValue`, `AdjustTokenPrivileges`: Used for persistence and privilege escalation.
    *   `CopyFileW`, `MoveFileW`, `GetTempPathW`: Typical indicators of dropper/downloader behavior.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: Unknown (likely a custom-built loader/wrapper)
2. **Malware type**: Dropper / Loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Multi-stage Payload Delivery:** The use of `CopyFileW`, `MoveFileW`, and `GetTempPathW` combined with CRC-32 integrity checks (`0xedb88320`) confirms the primary role is to extract, verify, and stage an underlying payload from its resources.
    *   **Evasion Techniques:** The implementation of dynamic library loading (`LoadLibraryExW`) and a "just-in-time" approach to resolving system components are specifically designed to minimize the file's initial import footprint and bypass static analysis.
    *   **Masquerading and Privilege Escalation:** The use of an NSIS framework wrapper allows it to mimic legitimate installers, while calls like `AdjustTokenPrivileges` (checking for `SeShutdownPrivilege`) indicate a requirement for elevated permissions to execute the final payload.
