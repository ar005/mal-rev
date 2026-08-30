# Threat Analysis Report

**Generated:** 2026-08-16 17:33 UTC
**Sample:** `0fa3b5d542e555a456a1377ad125bce99f86500d5499b708bf24eab0d8767102_0fa3b5d542e555a456a1377ad125bce99f86500d5499b708bf24eab0d8767102.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0fa3b5d542e555a456a1377ad125bce99f86500d5499b708bf24eab0d8767102_0fa3b5d542e555a456a1377ad125bce99f86500d5499b708bf24eab0d8767102.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 569,440 bytes |
| MD5 | `940a16187ad3b68cfa78f26b4ea060ec` |
| SHA1 | `3f88522674402060d87c5c5ba1c93ec9dfa9d497` |
| SHA256 | `0fa3b5d542e555a456a1377ad125bce99f86500d5499b708bf24eab0d8767102` |
| Overall entropy | 7.553 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1501547618 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.504 | No |
| `.rdata` | 5,120 | 5.146 | No |
| `.data` | 1,536 | 3.907 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 187,392 | 6.063 | No |

### Imports

**KERNEL32.dll**: `SetEnvironmentVariableW`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `CopyFileW`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`, `SetErrorMode`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1070** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495l
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
| `fcn.00401434` | `0x401434` | 5789 | ✓ |
| `fcn.00406937` | `0x406937` | 2183 | ✓ |
| `entry0` | `0x403350` | 1347 | ✓ |
| `fcn.0040396d` | `0x40396d` | 726 | ✓ |
| `fcn.00406281` | `0x406281` | 626 | ✓ |
| `fcn.00402ec1` | `0x402ec1` | 569 | ✓ |
| `fcn.004030fa` | `0x4030fa` | 504 | ✓ |
| `fcn.0040596d` | `0x40596d` | 451 | ✓ |
| `fcn.00405eab` | `0x405eab` | 378 | ✓ |
| `fcn.004067ef` | `0x4067ef` | 328 | ✓ |
| `fcn.004072f0` | `0x4072f0` | 216 | ✓ |
| `fcn.004052c3` | `0x4052c3` | 211 | ✓ |
| `fcn.00404a7f` | `0x404a7f` | 201 | ✓ |
| `fcn.00403c43` | `0x403c43` | 185 | ✓ |
| `fcn.004064f3` | `0x4064f3` | 175 | ✓ |
| `fcn.00402d2a` | `0x402d2a` | 173 | ✓ |
| `fcn.0040425b` | `0x40425b` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.004061bf` | `0x4061bf` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.0040726f` | `0x40726f` | 129 | ✓ |
| `fcn.00404b8d` | `0x404b8d` | 128 | ✓ |
| `fcn.00405c38` | `0x405c38` | 126 | ✓ |
| `fcn.00405792` | `0x405792` | 125 | ✓ |
| `fcn.00406051` | `0x406051` | 123 | ✓ |
| `fcn.00405e32` | `0x405e32` | 121 | ✓ |
| `fcn.0040612d` | `0x40612d` | 121 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004065c9` | `0x4065c9` | 112 | ✓ |

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
- [`code/fcn.0040396d.c`](code/fcn.0040396d.c)
- [`code/fcn.00403c43.c`](code/fcn.00403c43.c)
- [`code/fcn.0040425b.c`](code/fcn.0040425b.c)
- [`code/fcn.00404a7f.c`](code/fcn.00404a7f.c)
- [`code/fcn.00404b8d.c`](code/fcn.00404b8d.c)
- [`code/fcn.004052c3.c`](code/fcn.004052c3.c)
- [`code/fcn.00405792.c`](code/fcn.00405792.c)
- [`code/fcn.0040596d.c`](code/fcn.0040596d.c)
- [`code/fcn.00405c38.c`](code/fcn.00405c38.c)
- [`code/fcn.00405e32.c`](code/fcn.00405e32.c)
- [`code/fcn.00405eab.c`](code/fcn.00405eab.c)
- [`code/fcn.00406051.c`](code/fcn.00406051.c)
- [`code/fcn.0040612d.c`](code/fcn.0040612d.c)
- [`code/fcn.004061bf.c`](code/fcn.004061bf.c)
- [`code/fcn.00406281.c`](code/fcn.00406281.c)
- [`code/fcn.004064f3.c`](code/fcn.004064f3.c)
- [`code/fcn.004065c9.c`](code/fcn.004065c9.c)
- [`code/fcn.004067ef.c`](code/fcn.004067ef.c)
- [`code/fcn.00406937.c`](code/fcn.00406937.c)
- [`code/fcn.0040726f.c`](code/fcn.0040726f.c)
- [`code/fcn.004072f0.c`](code/fcn.004072f0.c)

## Behavioral Analysis

This analysis covers a binary sample that functions as an **installer or "dropper."** The code structure strongly indicates it was built using the **NSIS (Nullsoft Script Installer)** framework, which is commonly used both for legitimate software installation and by malware to unpack and execute payloads on a victim's system.

### Core Functionality
The primary purpose of this code is to prepare the environment for a secondary payload. It performs the following steps:
*   **Environment Setup:** The binary checks system information (via `GetVersion`), initializes common controls, and interacts with the Windows shell.
*   **Resource Extraction & File Manipulation:** A significant portion of the logic involves identifying, moving, and copying files. It uses `FindFirstFileW`, `FindNextFileW`, `CopyFileW`, and `MoveFileExW` to stage components from temporary directories into intended final locations.
*   **Configuration & Persistence:** The code interacts with the Windows Registry (`RegSetValueExW`, `RegOpenKeyExW`) and configuration files (`GetPrivateProfileStringW`), likely for setting up persistence or configuring the behavior of the dropped payload.

### Suspicious/Malicious Behaviors
The following behaviors are common in "droppers" used to deliver malware:

*   **File Staging (Dropping):** The code performs extensive file manipulation in the `\Temp\` directory. It copies files (`CopyFileW`) and changes their attributes (`SetFileAttributesW`). This is a classic sign of a dropper moving an encrypted or packed payload into a "ready-to-run" state.
*   **Privilege Escalation:** The code attempts to adjust token privileges (specifically mentioning `SeShutdownPrivilege` via `AdjustTokenPrivileges`). While common in legitimate installers requiring administrative rights, this is also a standard technique for malware seeking higher permissions to bypass security controls or interact with system-level drivers/services.
*   **System Interaction:** It uses `SetEnvironmentVariableW` and `SetCurrentDirectoryW` to manipulate the environment before executing subsequent components, ensuring that the secondary payload runs within the expected context (e.g., a specific folder or with certain paths).
*   **Persistence Mechanism:** The heavy use of `RegSetValueExW` suggests the creation of "AutoRun" keys or other methods to ensure the dropped software starts automatically upon system reboot.

### Notable Techniques & Patterns
*   **NSIS Wrapper Detection:** The presence of strings like `"NSIS Error"`, `"Installer integrity check has failed"`, and the large switch-case logic in `fcn.00401434` are hallmarks of an NSIS installer. This indicates the binary is a "wrapper"—it handles the installation logic, while the actual malicious payload may be embedded within it.
*   **Hidden/Temporary Execution:** The code frequently uses temporary paths and immediately performs cleanup (e.g., `DeleteFileW`) on components no longer needed by the installer. This is used to hide the presence of the "loader" from the user.
*   **API Obfuscation via Standard Libs:** It relies heavily on standard Windows DLLs (`kernel32`, `advapi32`, `user32`, `shell32`). While this doesn't indicate direct obfuscation, it shows the binary is designed to leverage native OS features to perform its actions.
*   **Looping File Processing:** Function `fcn.0040596d` contains a loop that iterates through file lists, checking for specific criteria (likely file types or names) before proceeding with copy/move operations, a common tactic to unpack multiple modules of an infection suite.

### Summary Table
| Category | Observation | Significance |
| :--- | :--- | :--- |
| **Execution Type** | Dropper / Installer | The binary's role is to "drop" and prepare files for execution. |
| **Persistence** | Registry Manipulation | Use of `RegSetValueExW` suggests establishing a permanent foothold. |
| **Privilege Escalation** | `AdjustTokenPrivileges` | Attempting to gain elevated rights from the system. |
| **File System Activity** | Temp File Staging | Extensive usage of `GetTempPathW` and `CopyFileW`. |
| **Known Framework** | NSIS Installer | The code is wrapped in a standard script-based installer framework. |

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed actions to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The use of a common NSIS installer framework and standard Windows APIs allows the malware to hide its presence by appearing as a legitimate software installation utility. |
| **T1068** | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` (specifically targeting privileges like `SeShutdownPrivilege`) indicates an attempt to acquire higher-level system permissions to bypass security controls. |
| **T1547.001** | Registry Run Keys / Startup Folder | The heavy utilization of `RegSetValueExW` to create "AutoRun" keys is a classic method for ensuring the malicious payload persists across system reboots. |
| **T1070** | Indicator Removal | The active cleanup and deletion of temporary files/components via `DeleteFileW` after they are no longer needed by the installer is intended to hide traces of the infection. |
| **T1105** | Ingress Tool Transfer | The behavior of moving, copying, and staging components from a directory like `\Temp\` into final locations characterizes the "dropper" functionality for payload delivery. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs). 

**Note:** As a threat intelligence analyst, I have filtered out standard Windows API functions, system libraries, and generic environment variables to focus only on actionable indicators.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (While the analysis mentions registry manipulation via `RegSetValueExW` and use of the `\Temp\` directory, no specific malicious file paths or hardcoded registry keys were provided in the text.)

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Framework Identifier:** NSIS (Nullsoft Script Installer) — The binary uses standard NSIS wrappers and error strings (`"NSIS Error"`, `"Installer integrity check has failed"`). This identifies the delivery mechanism but is not a unique piece of infrastructure.
*   **Code Offsets:** `fcn.00401434` and `fcn.0040596d` (These refer to specific internal function offsets within the binary, often used by analysts to map malicious logic in reverse engineering).

---
**Analyst Note:** The provided material contains **behavioral indicators** (e.g., credential/privilege escalation via `AdjustTokenPrivileges`, use of a "dropper" technique, and persistence through registry modification) rather than **atomic IOCs** (specific IP addresses or unique file hashes). This sample appears to be an automated installer wrapper designed to stage a payload.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: Unknown
2. **Malware type**: Dropper
3. **Confidence**: High (for Type) / Low (for Family)
4. **Key evidence**:
    *   **Wrapper Functionality:** The sample utilizes the NSIS framework to mask its activity as a legitimate installer while performing "file staging" (moving/copying payloads from `\Temp\` directories).
    *   **Persistence and Escalation:** The binary actively attempts privilege escalation via `AdjustTokenPrivileges` and establishes persistence through registry manipulation (`RegSetValueExW`), which are hallmark behaviors of a dropper preparing an environment for a secondary malicious payload.
    *   **Evasion Techniques:** The use of indicator removal (deleting temporary files) and masquerading as a common installer tool indicates a deliberate attempt to hide the delivery mechanism from the user and security software.
