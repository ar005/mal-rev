# Threat Analysis Report

**Generated:** 2026-07-24 16:04 UTC
**Sample:** `0a2a9d9e37b867ac0305afeea3c098cc5138c6bcb840ab0bb795b17bff93e345_0a2a9d9e37b867ac0305afeea3c098cc5138c6bcb840ab0bb795b17bff93e345.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a2a9d9e37b867ac0305afeea3c098cc5138c6bcb840ab0bb795b17bff93e345_0a2a9d9e37b867ac0305afeea3c098cc5138c6bcb840ab0bb795b17bff93e345.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 713,056 bytes |
| MD5 | `c04c87243c1adc87a2d919d63abd4cfc` |
| SHA1 | `14ef2931dcf0a686653e36c0665826a84ef1d6e6` |
| SHA256 | `0a2a9d9e37b867ac0305afeea3c098cc5138c6bcb840ab0bb795b17bff93e345` |
| Overall entropy | 7.875 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1576457453 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,112 | 6.427 | No |
| `.rdata` | 5,120 | 5.136 | No |
| `.data` | 1,536 | 4.006 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 28,160 | 4.978 | No |

### Imports

**KERNEL32.dll**: `ExitProcess`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `CreateFileW`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `SetEnvironmentVariableW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`
**USER32.dll**: `GetWindowRect`, `GetSystemMenu`, `SetClassLongW`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`, `SetClipboardData`
**GDI32.dll**: `SelectObject`, `SetTextColor`, `SetBkMode`, `CreateFontIndirectW`, `CreateBrushIndirect`, `DeleteObject`, `GetDeviceCaps`, `SetBkColor`
**SHELL32.dll**: `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHGetSpecialFolderLocation`, `SHGetFileInfoW`, `SHFileOperationW`, `SHBrowseForFolderW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ord_17`, `ImageList_Destroy`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1631** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQVPW
#Vh`.@
Instu`
softuW
NulluN	E
SVWj _3
Aj"A[f
D$$SPS
tVj%SSS
f9=(7B
D$$+D$
D$,+D$$P
WWWWjn
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5904 | ✓ |
| `fcn.004069b5` | `0x4069b5` | 2642 | ✓ |
| `entry0` | `0x40350d` | 1345 | ✓ |
| `fcn.00403b40` | `0x403b40` | 726 | ✓ |
| `fcn.00402f9d` | `0x402f9d` | 673 | ✓ |
| `fcn.0040647c` | `0x40647c` | 626 | ✓ |
| `fcn.00405b6c` | `0x405b6c` | 451 | ✓ |
| `fcn.004060a6` | `0x4060a6` | 378 | ✓ |
| `fcn.00403346` | `0x403346` | 361 | ✓ |
| `fcn.0040323e` | `0x40323e` | 264 | ✓ |
| `fcn.004054c2` | `0x4054c2` | 211 | ✓ |
| `fcn.0040442e` | `0x40442e` | 207 | ✓ |
| `fcn.00404c74` | `0x404c74` | 201 | ✓ |
| `fcn.00403e16` | `0x403e16` | 185 | ✓ |
| `fcn.004066ee` | `0x4066ee` | 175 | ✓ |
| `fcn.00402db1` | `0x402db1` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00402efb` | `0x402efb` | 162 | ✓ |
| `fcn.004063ba` | `0x4063ba` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404d82` | `0x404d82` | 128 | ✓ |
| `fcn.00405e37` | `0x405e37` | 126 | ✓ |
| `fcn.00405991` | `0x405991` | 125 | ✓ |
| `fcn.0040624c` | `0x40624c` | 123 | ✓ |
| `fcn.00406328` | `0x406328` | 121 | ✓ |
| `fcn.00406031` | `0x406031` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004067c4` | `0x4067c4` | 112 | ✓ |
| `fcn.00406927` | `0x406927` | 110 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402db1.c`](code/fcn.00402db1.c)
- [`code/fcn.00402efb.c`](code/fcn.00402efb.c)
- [`code/fcn.00402f9d.c`](code/fcn.00402f9d.c)
- [`code/fcn.0040323e.c`](code/fcn.0040323e.c)
- [`code/fcn.00403346.c`](code/fcn.00403346.c)
- [`code/fcn.00403b40.c`](code/fcn.00403b40.c)
- [`code/fcn.00403e16.c`](code/fcn.00403e16.c)
- [`code/fcn.0040442e.c`](code/fcn.0040442e.c)
- [`code/fcn.00404c74.c`](code/fcn.00404c74.c)
- [`code/fcn.00404d82.c`](code/fcn.00404d82.c)
- [`code/fcn.004054c2.c`](code/fcn.004054c2.c)
- [`code/fcn.00405991.c`](code/fcn.00405991.c)
- [`code/fcn.00405b6c.c`](code/fcn.00405b6c.c)
- [`code/fcn.00405e37.c`](code/fcn.00405e37.c)
- [`code/fcn.00406031.c`](code/fcn.00406031.c)
- [`code/fcn.004060a6.c`](code/fcn.004060a6.c)
- [`code/fcn.0040624c.c`](code/fcn.0040624c.c)
- [`code/fcn.00406328.c`](code/fcn.00406328.c)
- [`code/fcn.004063ba.c`](code/fcn.004063ba.c)
- [`code/fcn.0040647c.c`](code/fcn.0040647c.c)
- [`code/fcn.004066ee.c`](code/fcn.004066ee.c)
- [`code/fcn.004067c4.c`](code/fcn.004067c4.c)
- [`code/fcn.00406927.c`](code/fcn.00406927.c)
- [`code/fcn.004069b5.c`](code/fcn.004069b5.c)

## Behavioral Analysis

### Analysis Summary
The provided code describes a **multi-stage dropper or installer** with features typical of both legitimate software distribution (via the NSIS framework) and malicious delivery mechanisms. The primary purpose is to unpack, verify, and relocate a secondary payload while performing environment preparation and potential persistence setup.

---

### Core Functionality and Purpose
The binary acts as a wrapper for an installation process. It performs several high-level tasks:
*   **Payload Extraction:** It extracts data (potentially compressed or encrypted) from its own resources into temporary directories.
*   **Integrity Verification:** It uses a custom checksum routine to ensure the extracted files have not been tampered with or altered by security software before execution.
*   **File System Manipulation:** It moves and renames these files from "temporary" locations to their final destination, often involving the conversion of absolute paths.
*   **Environment Preparation:** It adjusts system settings, modifies registry keys for configuration, and handles UI interactions (likely via a custom-built installer wizard).

---

### Suspicious or Malicious Behaviors
The following behaviors are indicative of malware, specifically at the "Dropper" stage:

*   **Payload Dropping & Movement:** The code explicitly looks for temporary files and moves them to different locations (`MoveFileW`, `GetTempPathW`). This is a classic technique to move an infection from a "hidden" folder into a more permanent location.
*   **Integrity Checking (Anti-Tamper):** The use of a CRC/Hash loop (`fcn.004069b5`) and the specific error string `"Installer integrity check has failed"` suggest the code is designed to detect if antivirus software has modified the secondary payload.
*   **Privilege Escalation:** The routine involving `OpenProcessToken`, `LookupPrivilegeValueW`, and `AdjustTokenPrivileges` indicates the program is attempting to gain elevated privileges or specific system permissions (like `SeShutdownPrivilege`) to ensure it can modify protected system files/registry keys.
*   **Registry Manipulation:** Extensive use of `RegOpenKeyExW` and `RegSetValueExW` suggests the establishment of persistence or the configuration of malicious settings after a successful infection.
*   **Hidden File Operations:** The code performs complex calculations to determine file paths and attributes before moving files, often used to hide the true nature of the target path from the user.

---

### Notable Techniques & Patterns
*   **NSIS-like Framework:** The structure (specifically looking at `entry0` and the usage of "S" or "--" flags) suggests the binary was built using **NSIS (Nullsoft Script Installer)**. While a legitimate tool, it is frequently used by threat actors to create sophisticated installers for malware.
*   **Dynamic API Resolution:** The presence of `GetProcAddress` and `GetModuleHandleW` in the string list/code implies that many functions are resolved at runtime rather than being imported directly. This is a common anti-analysis technique used to hide the program's true capabilities from static analysis tools.
*   **Resource Extraction Loop:** The repeated calls to internal logic for "unpacking" and then calling `MoveFileW` indicates that the primary malicious payload is hidden inside this binary as an embedded resource or compressed blob.
*   **Polymorphic/Custom String Obfuscation (Potential):** While many strings are clear, several functions (`fcn.004062c7`, `fcn.00406328`) appear to perform logic-heavy processing on strings before they are used in API calls, which may be a way to evade simple string-based detection.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Software Packing | The binary utilizes a multi-stage "dropper" approach where payloads are hidden in resources and extractions involve custom string obfuscation to evade detection. |
| **T1036** | Dynamic Resolution | The use of `GetProcAddress` and `GetModuleHandleW` indicates the program resolves API calls at runtime to hide its functionality from static analysis tools. |
| **T1112** | Modify Registry | The frequent use of `RegOpenKeyExW` and `RegSetValueExW` is used to establish persistence or configure malicious settings on the host system. |
| **T1068** | Exploitation for Privilege Escalation | The implementation of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` shows an attempt to gain elevated permissions to bypass security restrictions. |
| **T1547** | (Contextual: Dropper behavior) | While "Dropping" is a stage rather than a single technique, the movement of files from temporary directories to final locations aligns with standard malware delivery tactics. |

### Analyst Notes:
*   **Integrity Checking:** The CRC/Hash loop (`fcn.004069b5`) used to detect anti-tampering is a common defensive evasion tactic often bundled under **T1027 (Software Packing)** or as part of the dropper's logic to ensure the payload remains "clean" before execution.
*   **NSIS Framework:** The use of the NSIS framework is a common indicator of a "wrapper" architecture, which allows threat actors to bundle multiple malicious functionalities into what appears to be a standard installer.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: While the behavior describes "moving files to persistent locations" and "modifying registry keys," no specific malicious paths or keys were explicitly listed in the strings provided.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Anti-Tamper String:** `"Installer integrity check has failed"` (Used to detect if the secondary payload has been modified by security software).
*   **Persistence/Privilege Escalation Indicators:** Use of `AdjustTokenPrivileges`, `OpenProcessToken`, and `LookupPrivilegeValueW` to attempt higher system permissions.
*   **Evasion Techniques:** 
    *   **Dynamic API Resolution:** Usage of `GetProcAddress` and `GetModuleHandleW` to hide capabilities from static analysis.
    *   **Obfuscation:** Potential string manipulation logic found in functions `fcn.004062c7` and `fcn.00406328`.
*   **Payload Mechanism:** Use of the **NSIS (Nullsoft Script Installer)** framework to wrap, unpack, and deploy a hidden secondary payload.
*   **Integrity Check Logic:** Identified at function `fcn.004069b5` (CRC/Hash loop).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High

**Key evidence**:
* **Multi-Stage Payload Delivery:** The binary functions as a wrapper (utilizing the NSIS framework) designed to extract, verify, and relocate a secondary payload from its internal resources, which is a classic "dropper" behavior.
* **Anti-Tampering & Evasion:** The inclusion of specific integrity check loops (CRC/Hash checks) with the message `"Installer integrity check has failed"` indicates a deliberate effort to detect and bypass security software before executing the main malicious payload.
* **Host Preparation & Persistence:** The use of dynamic API resolution (`GetProcAddress`), privilege escalation maneuvers (`AdjustTokenPrivileges`), and registry manipulation suggests the code is designed to bypass system restrictions and establish persistence for the final infection.
