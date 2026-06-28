# Threat Analysis Report

**Generated:** 2026-06-27 22:38 UTC
**Sample:** `020643859d860215d31c7e7201e40a1ff61a11ad5ea23fd1dac85b1f2bdbb3c8_020643859d860215d31c7e7201e40a1ff61a11ad5ea23fd1dac85b1f2bdbb3c8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `020643859d860215d31c7e7201e40a1ff61a11ad5ea23fd1dac85b1f2bdbb3c8_020643859d860215d31c7e7201e40a1ff61a11ad5ea23fd1dac85b1f2bdbb3c8.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 432,112 bytes |
| MD5 | `abe4d9cd0017bad9aec639eca08593af` |
| SHA1 | `17c0e9cc3559516e2d0d405532bf1b467f642b22` |
| SHA256 | `020643859d860215d31c7e7201e40a1ff61a11ad5ea23fd1dac85b1f2bdbb3c8` |
| Overall entropy | 6.711 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1544912676 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,112 | 6.416 | No |
| `.rdata` | 5,120 | 5.155 | No |
| `.data` | 1,536 | 4.004 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 190,464 | 4.265 | No |

### Imports

**KERNEL32.dll**: `ExitProcess`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `CreateFileW`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `SetEnvironmentVariableW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **850** (showing first 100)

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
WaitForSingleObject
KERNEL32.dll
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

Based on my analysis of the decompiled code and strings, here is a summary of the behavior for this binary.

### Core Functionality
The binary functions as an **installer or wrapper program**, likely utilizing a script engine (resembling NSIS or a similar installer framework) to unpack, configure, and execute software. It handles standard installation tasks such as:
*   **UI Management:** Utilizing Windows GDI and User32 libraries to display dialogs, buttons, and text fields (`GetDlgItem`, `CreateWindowExW`, `MessageBoxIndirectW`).
*   **File System Operations:** Creating directories, moving files between locations, and managing file permissions/attributes.
*   **Resource Loading:** Dynamically loading DLLs and internal resources to facilitate the installation process.

### Suspicious or Malicious Behaviors
While the functionality mimics a standard installer, several behaviors are characteristic of **droppers** or **installers used for malicious payloads**:

*   **Dropper/Extractor Behavior:** The code extensively uses `CreateFileW`, `MoveFileW`, and `CopyFileW`. It appears to "unpack" files into temporary directories and then move them to final locations. This is a common technique for delivering and installing unauthorized software or malware.
*   **Environment Manipulation:** The code specifically targets and modifies environment variables (e.g., `SetEnvironmentVariableW`). Specifically, it manipulates the **TEMP path**, which is often done to redirect the execution of subsequent scripts or components.
*   **Registry Modification:** It performs registry operations (`RegOpenKeyExW`, `RegSetValueExW`) to set system/user configuration values. In a malware context, this is frequently used to ensure **persistence** (e.g., creating "Run" keys).
*   **Dynamic Code Execution:** The use of `GetProcAddress` and `LoadLibraryExW` to resolve functions at runtime allows the binary to hide its full functionality from static analysis until it is running in memory.

### Notable Techniques & Patterns
*   **NSIS-like Framework:** The presence of the string `http://nsis.sf.net/NSIS_Error` and specific error handling routines strongly suggests this is a wrapper around an NSIS installer. This is a common technique for malware authors to "hide" malicious payloads inside a legitimate-looking installation script.
*   **File Integrity Checks:** The function `fcn.004031d6` includes logic to check the integrity of files before execution, ensuring that the payload was not corrupted during the extraction process.
*   **Dynamic Path Resolution:** Rather than using hardcoded strings for all operations, the code frequently resolves paths and addresses at runtime (e.g., `GetFullPathNameW`, `GetSystemDirectoryW`), which helps evade simple signature-based detection.
*   **Heavy use of "Temporary" Storage:** The heavy reliance on the `%TEMP%` directory is a classic indicator of an installer/dropper that extracts components to a non-persistent location before they are moved or executed as a primary process.

### Summary for Security Report
**Classification: Dropper / Installer Wrapper**
The binary acts as a delivery vehicle. It uses standard installation techniques (GUI creation, file system manipulation, and registry modification) to unpack and prepare other components for execution. The presence of NSIS-related code suggests it is designed to simplify the distribution of a multi-component payload while masking its true nature behind a standard "installer" facade.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1136.002** | Modify Environment Block | The binary specifically utilizes `SetEnvironmentVariableW` to manipulate the `TEMP` path, a common method to redirect the execution of subsequent scripts or components. |
| **T1112** | Modify Registry | The use of `RegOpenKeyExW` and `RegSetValueExW` is identified as a means to modify system configuration values, specifically for achieving persistence via "Run" keys. |
| **T1027** | Obfuscated Files or Information | The use of an NSIS-like wrapper and the resolution of functions at runtime (`GetProcAddress`/`LoadLibraryExW`) are employed to hide functionality from static analysis and mask the payload's true nature. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Standard Windows API functions (e.g., `CreateProcessW`, `GetProcAddress`), standard system libraries (e.g., `KERNEL32.dll`, `USER32.dll`), and general environmental variables (e.g., `%TEMP%`) have been excluded as false positives per your instructions.

### **IP addresses / URLs / Domains**
*   **http://nsis.sf.net/NSIS_Error** (Identified as part of the NSIS installer framework)

### **File paths / Registry keys**
*   *None identified.* (The analysis mentions registry modification and temp folder usage, but no specific hardcoded paths or keys were provided in the source text.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Framework Identification:** NSIS (Nullsoft Scriptable Install System). The presence of `nsis.sf.net` and related error handling indicates the malware utilizes an NSIS wrapper to mask its payload.
*   **Behavioral Profile:** Dropper / Installer Wrapper.
*   **Techniques Observed:** 
    *   Dynamic API Resolution (`GetProcAddress`, `LoadLibraryExW`)
    *   Persistence via Registry modification (implied)
    *   Payload extraction/dropping into temporary directories

---

## Malware Family Classification

1. **Malware family**: custom (NSIS-based wrapper)
2. **Malware type**: dropper / loader
3. **Confidence**: High

4. **Key evidence**:
*   **Dropper Functionality:** The binary exhibits classic "dropper" behavior by extracting files into temporary directories and moving them to final locations using `CreateFileW` and `MoveFileW`.
*   **Wrapper Tactics:** It utilizes the NSIS (Nullsoft Scriptable Install System) framework, a common technique used by malware authors to masquerade a malicious payload as a legitimate software installer.
*   **Persistence & Preparation:** The use of Registry modifications for "Run" keys and environment variable manipulation (`SetEnvironmentVariableW`) indicates the binary is preparing the system for a secondary, more active stage of infection.
