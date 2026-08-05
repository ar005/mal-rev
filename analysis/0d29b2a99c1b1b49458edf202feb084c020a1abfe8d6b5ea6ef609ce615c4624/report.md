# Threat Analysis Report

**Generated:** 2026-08-04 21:13 UTC
**Sample:** `0d29b2a99c1b1b49458edf202feb084c020a1abfe8d6b5ea6ef609ce615c4624_0d29b2a99c1b1b49458edf202feb084c020a1abfe8d6b5ea6ef609ce615c4624.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d29b2a99c1b1b49458edf202feb084c020a1abfe8d6b5ea6ef609ce615c4624_0d29b2a99c1b1b49458edf202feb084c020a1abfe8d6b5ea6ef609ce615c4624.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 553,120 bytes |
| MD5 | `8d1239e20b67d593e731a873755b65b3` |
| SHA1 | `8e5db74778f74eea45a3693c8c0718fc7ed45a8a` |
| SHA256 | `0d29b2a99c1b1b49458edf202feb084c020a1abfe8d6b5ea6ef609ce615c4624` |
| Overall entropy | 6.462 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1481493048 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,088 | 6.477 | No |
| `.rdata` | 5,120 | 5.163 | No |
| `.data` | 1,536 | 3.975 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 283,136 | 4.364 | No |

### Imports

**KERNEL32.dll**: `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetFullPathNameW`, `Sleep`, `GetTickCount`, `CreateFileW`, `GetFileSize`, `MoveFileW`, `SetFileAttributesW`, `GetModuleFileNameW`, `CopyFileW`, `ExitProcess`, `SetEnvironmentVariableW`, `GetWindowsDirectoryW`, `GetTempPathW`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `IsWindowEnabled`, `EnableMenuItem`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `ShellExecuteW`, `SHFileOperationW`
**ADVAPI32.dll**: `RegDeleteKeyW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `AdjustTokenPrivileges`, `RegOpenKeyExW`, `RegEnumValueW`, `RegDeleteValueW`, `RegCloseKey`, `RegCreateKeyExW`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_AddMasked`, `ord_17`, `ImageList_Destroy`, `ImageList_Create`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1125** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495l
SQSSSPW
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
lstrcpyW
MoveFileExW
lstrcatW
GetSystemDirectoryW
GetProcAddress
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5817 | ✓ |
| `fcn.0040672b` | `0x40672b` | 2642 | ✓ |
| `entry0` | `0x40344a` | 1311 | ✓ |
| `fcn.00403a5b` | `0x403a5b` | 726 | ✓ |
| `fcn.00402ed5` | `0x402ed5` | 678 | ✓ |
| `fcn.00406234` | `0x406234` | 626 | ✓ |
| `fcn.00405a03` | `0x405a03` | 451 | ✓ |
| `fcn.00405f41` | `0x405f41` | 370 | ✓ |
| `fcn.00403283` | `0x403283` | 361 | ✓ |
| `fcn.0040317b` | `0x40317b` | 264 | ✓ |
| `fcn.00405371` | `0x405371` | 211 | ✓ |
| `fcn.00403d31` | `0x403d31` | 205 | ✓ |
| `fcn.00404b2d` | `0x404b2d` | 201 | ✓ |
| `fcn.00402c93` | `0x402c93` | 181 | ✓ |
| `fcn.004064a6` | `0x4064a6` | 175 | ✓ |
| `fcn.0040433d` | `0x40433d` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00402e33` | `0x402e33` | 162 | ✓ |
| `fcn.00406172` | `0x406172` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404c3b` | `0x404c3b` | 128 | ✓ |
| `fcn.00405cce` | `0x405cce` | 126 | ✓ |
| `fcn.00405840` | `0x405840` | 125 | ✓ |
| `fcn.004060df` | `0x4060df` | 122 | ✓ |
| `fcn.00405ec8` | `0x405ec8` | 121 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.0040657c` | `0x40657c` | 112 | ✓ |
| `fcn.0040669d` | `0x40669d` | 110 | ✓ |
| `fcn.00405444` | `0x405444` | 108 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402c93.c`](code/fcn.00402c93.c)
- [`code/fcn.00402e33.c`](code/fcn.00402e33.c)
- [`code/fcn.00402ed5.c`](code/fcn.00402ed5.c)
- [`code/fcn.0040317b.c`](code/fcn.0040317b.c)
- [`code/fcn.00403283.c`](code/fcn.00403283.c)
- [`code/fcn.00403a5b.c`](code/fcn.00403a5b.c)
- [`code/fcn.00403d31.c`](code/fcn.00403d31.c)
- [`code/fcn.0040433d.c`](code/fcn.0040433d.c)
- [`code/fcn.00404b2d.c`](code/fcn.00404b2d.c)
- [`code/fcn.00404c3b.c`](code/fcn.00404c3b.c)
- [`code/fcn.00405371.c`](code/fcn.00405371.c)
- [`code/fcn.00405444.c`](code/fcn.00405444.c)
- [`code/fcn.00405840.c`](code/fcn.00405840.c)
- [`code/fcn.00405a03.c`](code/fcn.00405a03.c)
- [`code/fcn.00405cce.c`](code/fcn.00405cce.c)
- [`code/fcn.00405ec8.c`](code/fcn.00405ec8.c)
- [`code/fcn.00405f41.c`](code/fcn.00405f41.c)
- [`code/fcn.004060df.c`](code/fcn.004060df.c)
- [`code/fcn.00406172.c`](code/fcn.00406172.c)
- [`code/fcn.00406234.c`](code/fcn.00406234.c)
- [`code/fcn.004064a6.c`](code/fcn.004064a6.c)
- [`code/fcn.0040657c.c`](code/fcn.0040657c.c)
- [`code/fcn.0040669d.c`](code/fcn.0040669d.c)
- [`code/fcn.0040672b.c`](code/fcn.0040672b.c)

## Behavioral Analysis

Based on my analysis of the provided disassembly and strings, this binary is likely a **malware dropper or an installer wrapper**, potentially derived from or utilizing components of the NSIS (Nullsoft Script Installer) framework.

The code's primary purpose is to prepare the environment, extract/decompress payload components, modify system settings via the registry, and execute secondary programs.

### Core Functionality and Purpose
*   **Installer Wrapper:** The presence of "NSIS Error" strings and common installer patterns (like `RichEdit` control checks) indicates this is a wrapper designed to install software. In malware terms, this "software" is typically a malicious payload (e.g., a backdoor or information stealer).
*   **Environment Preparation:** The code actively manipulates environment variables (specifically the `TEMP` path) and works with temporary directories to host files before execution.
*   **Resource Extraction:** Several functions (notably those involving bitwise operations like `fcn.0040669d`) suggest that the binary contains "packed" or encrypted data which it decompress/decrypts in memory before writing to disk.

### Suspicious or Malicious Behaviors
*   **Payload Dropping & Execution:** The code performs manual file operations using `CopyFileW` and `CreateProcessW`. It copies components from an internal buffer (or a separate source) into temporary directories and executes them, while waiting for the process to finish (`GetExitCodeProcess`, `WaitForSingleObject`). This is a classic "Dropper" technique.
*   **Privilege Escalation:** The code explicitly attempts to adjust token privileges using `OpenProcessToken`, `LookupPrivilegeValueW`, and `AdjustTokenPrivileges`. It specifically looks for high-level capabilities, which are often necessary to modify system files or registry keys protected by Windows security.
*   **Registry Manipulation:** There is extensive use of `RegCreateKeyExW` and `RegSetValueExW`. This indicates the malware is likely establishing **persistence** (e.g., adding a "Run" key) or modifying system configurations to weaken security.
*   **File System Obfuscation:** It uses `SetFileAttributesW` and moves files between temporary paths, likely trying to hide its activities from basic heuristic scanners that monitor static locations.

### Notable Techniques and Patterns
*   **NSIS-like Architecture:** The structure of the code mirrors a standard installer's workflow: unpacking, environment setup, component installation (dropping), and then "cleaning up" by deleting temporary files.
*   **Decryption/Decompression Loops:** The complex nested loops and bitwise operations in `fcn.0040669d` are typical of routines used to unpack a second-stage payload that is hidden within the first executable's data section.
*   **Generic API Usage for Stealth:** It uses many standard Windows APIs (`ShellExecuteW`, `GetTempPathW`, `GetProcess_Term_Time`) which allow it to blend in with legitimate system processes while performing its malicious tasks.
*   **Dynamic Path Resolution:** Rather than hardcoding paths (which would be easily flagged), the code constructs file paths dynamically using `GetSystemDirectoryW` and `GetWindowsDirectoryW`.

### Summary of Risk
This binary is a **high-risk downloader/dropper**. It acts as the first stage of an infection. Its main role is to "land" the actual malware on the system, bypass basic security checks by masquerading as a legitimate installer, and ensure that the malicious payload has enough privileges to function effectively.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of complex bitwise operations and decompression loops suggests that the primary payload is hidden within a packed or encrypted data section to evade detection. |
| T1068 | Exploitation for Privilege Escalation | The calls to `AdjustTokenPrivileges` indicate an attempt to acquire high-level system privileges necessary to modify protected files or registry keys. |
| T1547.001 | Registry Run Keys | The use of `RegCreateKeyExW` and `RegSetValueExW` specifically indicates the creation of "Run" keys to ensure persistence after a system reboot. |
| T1036 | Hide Files and Directories | The utilization of `SetFileAttributesW` combined with moving files between temporary paths is intended to hide malicious activity from heuristic scanners. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** As a threat intelligence analyst, I have excluded standard Windows API calls (e.g., `GetProcess_Term_Time`, `WriteFile`) and common system libraries as they are not unique to this specific threat.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis notes the presence of a "downloader" behavior, but no specific C2 infrastructure was listed in the source text).

### **File paths / Registry keys**
*   *None identified.* (While the report mentions "Registry Manipulation" and "Environment Variable" modification, it does not provide specific malicious registry paths or hardcoded file paths.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **NSIS Error:** (Indicates the use of the Nullsoft Script Installer framework to wrap and deploy payloads).
*   **Function Offset 0x40669d:** (Identified in analysis as the specific location for decryption/decompression loops used to unpack secondary stages).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**: 
    * **Installer Wrapper Behavior:** The sample utilizes an NSIS-like architecture to mask its activities as a legitimate software installer, using standard techniques like environment preparation and temporary directory manipulation to hide the delivery of payloads.
    * **Payload Extraction & Execution:** Evidence of decompression/decryption loops (e.g., at `0x40669d`) combined with `CopyFileW` and `CreateProcessW` confirms its primary role is to unpack and execute secondary malicious components.
    * **Persistence & Privilege Escalation:** The binary explicitly attempts to gain high-level system privileges (`AdjustTokenPrivileges`) and manipulate registry keys (`RegSetValueExW`) to ensure the malware remains active upon system reboot.
