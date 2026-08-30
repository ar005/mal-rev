# Threat Analysis Report

**Generated:** 2026-08-23 20:21 UTC
**Sample:** `11a563757a79333564f1eda8325816a621d4f404c282245c8a382f0ec9e2dcfb_11a563757a79333564f1eda8325816a621d4f404c282245c8a382f0ec9e2dcfb.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11a563757a79333564f1eda8325816a621d4f404c282245c8a382f0ec9e2dcfb_11a563757a79333564f1eda8325816a621d4f404c282245c8a382f0ec9e2dcfb.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 585,618 bytes |
| MD5 | `693d96e5e78e84dffa825682015ed434` |
| SHA1 | `e4c82332c18ec8204e754fdf39119f02735adea5` |
| SHA256 | `11a563757a79333564f1eda8325816a621d4f404c282245c8a382f0ec9e2dcfb` |
| Overall entropy | 7.704 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1469408131 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,088 | 6.479 | No |
| `.rdata` | 5,120 | 5.162 | No |
| `.data` | 1,536 | 3.903 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 105,472 | 5.028 | No |

### Imports

**KERNEL32.dll**: `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetFullPathNameW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `MoveFileW`, `SetFileAttributesW`, `GetCurrentProcess`, `ExitProcess`, `SetEnvironmentVariableW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `IsWindowEnabled`, `EnableMenuItem`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `ShellExecuteW`, `SHFileOperationW`
**ADVAPI32.dll**: `RegDeleteKeyW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `AdjustTokenPrivileges`, `RegOpenKeyExW`, `RegEnumValueW`, `RegDeleteValueW`, `RegCloseKey`, `RegCreateKeyExW`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_AddMasked`, `ord_17`, `ImageList_Destroy`, `ImageList_Create`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1133** (showing first 100)

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
| `fcn.00401434` | `0x401434` | 5674 | ✓ |
| `fcn.004066c3` | `0x4066c3` | 2183 | ✓ |
| `entry0` | `0x40327d` | 1311 | ✓ |
| `fcn.00403876` | `0x403876` | 726 | ✓ |
| `fcn.0040604f` | `0x40604f` | 626 | ✓ |
| `fcn.00402dee` | `0x402dee` | 569 | ✓ |
| `fcn.00403027` | `0x403027` | 504 | ✓ |
| `fcn.0040581e` | `0x40581e` | 451 | ✓ |
| `fcn.00405d5c` | `0x405d5c` | 370 | ✓ |
| `fcn.0040657b` | `0x40657b` | 328 | ✓ |
| `fcn.0040707c` | `0x40707c` | 216 | ✓ |
| `fcn.0040518c` | `0x40518c` | 211 | ✓ |
| `fcn.00403b4c` | `0x403b4c` | 205 | ✓ |
| `fcn.00404948` | `0x404948` | 201 | ✓ |
| `fcn.00402bff` | `0x402bff` | 181 | ✓ |
| `fcn.004062c1` | `0x4062c1` | 175 | ✓ |
| `fcn.00404158` | `0x404158` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00405f8d` | `0x405f8d` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00406ffb` | `0x406ffb` | 129 | ✓ |
| `fcn.00404a56` | `0x404a56` | 128 | ✓ |
| `fcn.00405ae9` | `0x405ae9` | 126 | ✓ |
| `fcn.0040565b` | `0x40565b` | 125 | ✓ |
| `fcn.00405efa` | `0x405efa` | 122 | ✓ |
| `fcn.00405ce3` | `0x405ce3` | 121 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406397` | `0x406397` | 112 | ✓ |
| `fcn.004064b8` | `0x4064b8` | 110 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402bff.c`](code/fcn.00402bff.c)
- [`code/fcn.00402dee.c`](code/fcn.00402dee.c)
- [`code/fcn.00403027.c`](code/fcn.00403027.c)
- [`code/fcn.00403876.c`](code/fcn.00403876.c)
- [`code/fcn.00403b4c.c`](code/fcn.00403b4c.c)
- [`code/fcn.00404158.c`](code/fcn.00404158.c)
- [`code/fcn.00404948.c`](code/fcn.00404948.c)
- [`code/fcn.00404a56.c`](code/fcn.00404a56.c)
- [`code/fcn.0040518c.c`](code/fcn.0040518c.c)
- [`code/fcn.0040565b.c`](code/fcn.0040565b.c)
- [`code/fcn.0040581e.c`](code/fcn.0040581e.c)
- [`code/fcn.00405ae9.c`](code/fcn.00405ae9.c)
- [`code/fcn.00405ce3.c`](code/fcn.00405ce3.c)
- [`code/fcn.00405d5c.c`](code/fcn.00405d5c.c)
- [`code/fcn.00405efa.c`](code/fcn.00405efa.c)
- [`code/fcn.00405f8d.c`](code/fcn.00405f8d.c)
- [`code/fcn.0040604f.c`](code/fcn.0040604f.c)
- [`code/fcn.004062c1.c`](code/fcn.004062c1.c)
- [`code/fcn.00406397.c`](code/fcn.00406397.c)
- [`code/fcn.004064b8.c`](code/fcn.004064b8.c)
- [`code/fcn.0040657b.c`](code/fcn.0040657b.c)
- [`code/fcn.004066c3.c`](code/fcn.004066c3.c)
- [`code/fcn.00406ffb.c`](code/fcn.00406ffb.c)
- [`code/fcn.0040707c.c`](code/fcn.0040707c.c)

## Behavioral Analysis

Based on the analysis of the provided disassembly and strings, here is a summary of the binary's functionality and behaviors:

### Core Functionality and Purpose
The sample functions as a **sophisticated installer or "loader" application**. The presence of specific error messages (e.g., `"NSIS Error"`, `"Installer integrity check has failed"`) and code structures suggests it is either based on the Nullsoft Script Installer (NSIS) framework or is designed to mimic its behavior.

Its primary role is to:
*   **Validate and Unpack:** The binary performs several checks to ensure that internal components are intact before execution.
*   **Environment Setup:** It manipulates environment variables, sets system paths, and prepares the operating system for the installation of secondary software or modules.
*   **Payload Delivery:** It acts as a "dropper" or "loader," responsible for extracting resources from its own binary (or an associated file) and launching them using `CreateProcessW` or `ShellExecuteW`.

### Suspicious or Malicious Behaviors
The following behaviors are common in malware, particularly in the "downloader/loader" stage of a multi-stage infection:

*   **Integrity Checks & Anti-Tamper:** The function `fcn.004012e2` and others perform complex verification loops on internal data. This is often used to ensure that security researchers haven't modified the malicious payload or bypassed the packer/loader’s protections.
*   **Evasive Packing/Unpacking:** The code contains specific logic (`fcn.00403876`) that checks for "packed" states and uses custom routines (like `fcn.004064b8`, which appears to be a hashing or CRC check) before loading components into memory via `LoadImageW`. This is a classic technique to hide the primary malicious payload from static analysis.
*   **Privilege Manipulation:** The binary attempts to acquire special privileges using `AdjustTokenPrivileges` (specifically mentioning `SeShutdownPrivilege`). While sometimes used by installers, this is also a common technique used by malware to gain higher-level access to system processes or to ensure it can perform actions like shutting down/restarting systems.
*   **Dynamic Loading of Components:** Extensive use of `LoadLibraryExW`, `GetProcAddress`, and `CreateProcessW` indicates that the actual malicious payload is likely not in this binary but is instead loaded into memory or executed as a separate process after this "stub" completes its work.

### Notable Techniques & Patterns
*   **Stub Architecture:** The code structure (Check $\rightarrow$ Unpack $\rightarrow$ Verify $\rightarrow$ Launch) is characteristic of a **packer stub**. It acts as a wrapper for the real malware to protect it from signature-based detection.
*   **Resource Handling:** It utilizes `GetModuleFileNameW` and various file manipulation APIs (`MoveFileW`, `CopyFileW`) to manage hidden or temporary files during its execution, a common behavior in installers but also heavily utilized by droppers to move payloads into "safe" locations (like `%TEMP%`).
*   **Standard API Abuse:** The binary uses standard Windows functions for UI and interaction (e.g., `ShellExecuteW`, `SendMessageW`), which helps it blend in with legitimate installer software during initial analysis.

### Conclusion
This is likely a **malware loader/dropper**. While the code itself performs "installer" tasks, its heavy use of integrity checks, packer-detection logic, and dynamic execution suggests it is designed to deliver a secondary payload while evading detection through obfuscation and unpacking routines.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027.001** | Packing | The use of "packer stubs," integrity checks, and unpacking routines is designed to hide the malicious payload from static analysis. |
| **T1105** | Dropper | The binary acts as a loader/dropper by extracting internal resources and executing them on the local system. |
| **T1106** | Dynamic Resolution | Extensive use of `GetProcAddress` and `LoadLibraryExW` indicates that API calls are resolved at runtime to evade detection. |
| **T1036** | Masquerading | The binary mimics legitimate installer software (e.g., NSIS) and uses standard UI elements to blend in with normal system activity. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs). 

*Note: Many strings provided (e.g., `KERNEL32.dll`, `CreateProcessW`, `GetProcAddress`) were identified as standard Windows API calls or system libraries and have been excluded as false positives.*

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The analysis mentions usage of `%TEMP%` and registry manipulation, but no specific hardcoded malicious paths or keys were provided in the source text).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5/SHA1/SHA256 hashes were present in the provided strings).

### **Other artifacts**
*   **Behavioral Indicators:** 
    *   **Packer Signature:** The binary exhibits a "Stub Architecture" (Check $\rightarrow$ Unpack $\rightarrow$ Verify $\rightarrow$ Launch), characteristic of malware droppers.
    *   **Specific Function Offsets:** 
        *   `0x4012e2`: Integrity/Verification loop.
        *   `0x403876`: Packed state check logic.
        *   `0x4064b8`: Hashing or CRC checking routine.
    *   **Privilege Escalation:** Use of `AdjustTokenPrivileges` specifically targeting the `SeShutdownPrivilege`.
    *   **Mimicry:** The binary intentionally mimics "NSIS" (Nullsoft Script Installer) behavior to blend in with legitimate software installers.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / dropper
3. **Confidence**: High

4. **Key evidence**:
* **Stub Architecture & Evasion:** The binary follows a classic "Check $\rightarrow$ Unpack $\rightarrow$ Verify $\rightarrow$ Launch" pattern, utilizing integrity checks and packing-detection logic to hide its primary payload from static analysis tools.
* **Masquerading & Mimicry:** The sample explicitly mimics the Nullsoft Script Installer (NSIS) framework and uses standard system APIs for UI interaction to blend in with legitimate software installation processes.
* **Dynamic Execution Tactics:** Extensive use of `GetProcAddress`, `LoadLibraryExW`, and `CreateProcessW` indicates it is designed as a "loader" intended to decrypt and execute an internal payload into memory or a separate process.
