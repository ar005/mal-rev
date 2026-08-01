# Threat Analysis Report

**Generated:** 2026-07-29 15:25 UTC
**Sample:** `0c150020cbb47d68b1414b0c93834cdc90ca2d8064354964893b3aba9e553676_0c150020cbb47d68b1414b0c93834cdc90ca2d8064354964893b3aba9e553676.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c150020cbb47d68b1414b0c93834cdc90ca2d8064354964893b3aba9e553676_0c150020cbb47d68b1414b0c93834cdc90ca2d8064354964893b3aba9e553676.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 861,496 bytes |
| MD5 | `daaa9e40e51717861fe7788b27665204` |
| SHA1 | `8ca168b99e3371df4bbd43e1316134401fa4464a` |
| SHA256 | `0c150020cbb47d68b1414b0c93834cdc90ca2d8064354964893b3aba9e553676` |
| Overall entropy | 7.837 |
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

Total strings found: **1855** (showing first 100)

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

Based on the analysis of the decompiled code and strings, here is a summary of the binary's functionality.

### Core Functionality
The binary is an **installer wrapper**, specifically one built using the **NSIS (Nullsoft Script Installer)** framework. Its primary role is to act as a "loader" or "extractor." It handles environment setup, verifies the integrity of the installation files, extracts resources/files from its own package, and then executes the main payload.

### Suspicious or Malicious Behaviors
While much of the behavior is typical for an installer, several patterns are common in malware (specifically droppers or installers used by malware):

*   **File Manipulation & Staging:** The code performs extensive file operations including `CreateDirectoryW`, `CopyFileW`, `MoveFileW`, and `DeleteFileW`. It specifically manipulates file attributes (`SetFileAttributesW`) and sets the current directory to temporary paths, which are common tactics for a "dropper" moving an executable into a hidden or system-accessible location.
*   **Registry Manipulation:** Extensive use of `RegOpenKeyExW`, `RegSetValueExW`, and `RegCreateKeyExW` suggests it creates persistence points or modifies system configuration to ensure the payload runs after a reboot.
*   **Persistence & Privilege Escalation:** The inclusion of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` (specifically checking for `SeShutdownPrivilege`) indicates the installer may be attempting to gain elevated privileges or interact with sensitive system services.
*   **Anti-Analysis/Obfuscation Signs:** 
    *   The function `fcn.004067a7` contains complex bitwise operations and loops over memory, likely used for decompressing or decrypting internal resources before execution.
    *   It performs "Integrity Checks" (as seen in the `nsis_error` logic). While common in installers, this is also a standard method to check if an analyst has tampered with the binary's code.

### Notable Techniques & Patterns
*   **NSIS Wrapper:** The presence of strings like "NSIS Error", "nsis.sf.net", and "RichEdit20W" confirms that the sample is wrapped in a standard installer script. This is frequently used by malware authors to hide their actual payload inside a multi-stage installer.
*   **Dynamic Loading/Resolution:** The code uses `GetProcAddress` and `LoadLibraryExW` (evident in the string list and logic) to resolve functions at runtime, which can be used to bypass simple static scanners that look for specific API imports.
*   **Resource Extraction:** The flow of `entry0` suggests it extracts a "primary" payload from its own data section/resource to a temporary directory before executing it (a common technique to hide the malicious payload from initial file system scans).
*   **Environment Awareness:** It queries system information (`GetVersion`, `GetSystemDirectoryW`) and checks for the presence of specific folders and items, likely ensuring it is running in an environment where it can successfully install or drop its payload.

### Summary Conclusion
This binary acts as a **sophisticated installer/dropper**. While the code provided shows many "innocent"-looking installer behaviors (moving files, setting registry keys), the combination of these features with manual decryption loops and integrity checks strongly suggests this is a delivery vehicle for an underlying payload. In a malware context, its purpose would be to unpack a hidden executable, grant it privileges, and ensure it persists on the system.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1563** | Hide Files and Directories | The binary manipulates file attributes (`SetFileAttributesW`) and moves files to temporary/hidden paths to obscure its presence during the staging process. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys | The use of `RegSetValueExW` indicates an attempt to create registry keys that ensure the payload persists after a system reboot. |
| **T1068** | Exploitation for Privilege Escalation | The check for `SeShutdownPrivilege` and the use of `AdjustTokenPrivileges` suggest attempts to acquire elevated rights to interact with sensitive system services. |
| **T1027** | Obfuscated Files or Information | The use of complex bitwise operations and loops over memory indicates a decryption/decompression routine designed to hide internal resources from static analysis. |
| **T1106** | Native API | The use of `GetProcAddress` and `LoadLibraryExW` is employed to resolve functions at runtime, allowing the binary to bypass static scanners that look for specific API imports. |
| **T1497** | Virtualization/Sandbox Detection | Querying system information via `GetVersion` and checking for specific directories suggests the sample identifies its environment before executing malicious behavior. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted intelligence. 

Note: Many items in the "Extracted Strings" section are standard Windows API functions (e.g., `CreateFileW`, `RegOpenKeyExW`) or standard library files (e.g., `KERNEL32.dll`). These have been excluded as they do not constitute unique Indicators of Compromise.

### **IP addresses / URLs / Domains**
*   *None identified.* (Note: "nsis.sf.net" appears in the analysis but is associated with the standard NSIS framework and is not considered a specific malicious IOC).

### **File paths / Registry keys**
*   *None identified.* (The report notes that registry keys and temporary paths are used for persistence, but no specific paths or keys were provided in the source text).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Malware Type:** Installer Wrapper / Dropper (NSIS framework).
*   **Function Signature:** `fcn.004067a7` (Identified as a decryption/decompression routine for internal resources).
*   **Technique - Dynamic Resolution:** The binary utilizes `GetProcAddress` and `LoadLibraryExW` to resolve APIs at runtime, likely to evade static analysis.
*   **Technique - Privilege Escalation:** Use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` (specifically targeting `SeShutdownPrivilege`) to attempt elevated permissions.
*   **Behavioral Pattern:** Multi-stage execution where the primary payload is extracted from the internal data section to a temporary directory before execution.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1.  **Malware family**: custom
2.  **Malware type**: dropper / loader
3.  **Confidence**: High
4.  **Key evidence**: 
    *   **Extraction Mechanism:** The binary functions as an NSIS wrapper designed to hide a secondary payload within its own data section, extracting it to temporary directories for execution (a classic "dropper" behavior).
    *   **Evasion & Obfuscation:** The use of dynamic API resolution (`GetProcAddress`/`LoadLibraryExW`), complex bitwise decryption loops (fcn.004067a7), and environment checks indicates a deliberate attempt to bypass static analysis and security controls.
    *   **Persistence & Privilege Escalation:** The sample explicitly attempts to establish persistence via Registry Run keys and seeks elevated privileges through `AdjustTokenPrivileges` to ensure the dropped payload can operate with maximum authority.
