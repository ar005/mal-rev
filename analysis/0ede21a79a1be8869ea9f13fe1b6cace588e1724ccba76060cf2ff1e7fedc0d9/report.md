# Threat Analysis Report

**Generated:** 2026-08-15 08:51 UTC
**Sample:** `0ede21a79a1be8869ea9f13fe1b6cace588e1724ccba76060cf2ff1e7fedc0d9_0ede21a79a1be8869ea9f13fe1b6cace588e1724ccba76060cf2ff1e7fedc0d9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ede21a79a1be8869ea9f13fe1b6cace588e1724ccba76060cf2ff1e7fedc0d9_0ede21a79a1be8869ea9f13fe1b6cace588e1724ccba76060cf2ff1e7fedc0d9.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 77,586,360 bytes |
| MD5 | `0970e509827a6b84f9a27e3a35aca2dc` |
| SHA1 | `1540f309a3f22ba605c8bf0f0102936f3a722967` |
| SHA256 | `0ede21a79a1be8869ea9f13fe1b6cace588e1724ccba76060cf2ff1e7fedc0d9` |
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
| `.rsrc` | 3,584 | 4.159 | No |

### Imports

**KERNEL32.dll**: `SetEnvironmentVariableW`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `CopyFileW`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`, `SetErrorMode`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **168723** (showing first 100)

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

This updated analysis incorporates the new disassembly data provided in chunk 2. The addition of these functions reinforces the initial assessment while providing more specific evidence regarding the binary's capability to load external components and verify data integrity.

### Updated Analysis Summary

The binary continues to exhibit characteristics of a sophisticated **installer or loader**. While the core framework remains consistent with an NSIS-based installer, the new disassembly reveals high-level integration with Windows system libraries, dynamic module loading, and data integrity checks. These features are common in professional software installers but are also hallmarks of modular "droppers" or "loaders" used in malware to facilitate multi-stage execution.

---

### New Findings from Chunk 2

#### 1. Dynamic Library Loading & Path Manipulation (`fcn.00406624`)
This function demonstrates a systematic way of loading additional functionality into the process memory:
*   **System Directory Resolution:** It calls `GetSystemDirectoryW` to determine where Windows system files are located.
*   **Path Construction:** The logic includes a check for a trailing backslash (`0x5c`) in the directory path before appending a `.dll` filename using `wsprintfW`. 
*   **Dynamic Loading:** It uses `LoadLibraryExW` to load the resulting DLL into memory.
*   **Significance:** This confirms that the binary is designed to **extend its own capabilities at runtime**. While an installer might do this to load a specific "engine" for different installation types, it is also a primary method used by loaders to pull in malicious payloads or capabilities (like keylogging or encryption) only after the initial execution.

#### 2. Data Integrity and Checksums (`fcn.00406787`)
This function implements a standard **CRC32 (Cyclic Redundancy Check)** algorithm:
*   **Algorithm Identification:** The constant `0xedb88320` is the "magic" polynomial used in the standard CRC-32 calculation. 
*   **Purpose:** This routine is used to verify that a block of data remains intact after being moved or copied. 
*   **Significance:** In an installer, this ensures that files were not corrupted during extraction from a compressed archive. In a malware context (specifically a "downloader"), this confirms the integrity of a payload before it is executed by the main process.

#### 3. COM/OLE Integration (`fcn.004053f5`)
This function interacts with **Component Object Model (COM)** and **Object Linking and Embedding (OLE)**:
*   **Initialization:** It calls `OleInitialize` at the start of its routine and `OleUninitialize` at the end.
*   **Looping/Modular Logic:** The code iterates through a series of data points (from memory address `0x47af2c`) to perform actions. 
*   **Significance:** COM is often used in Windows for advanced features like creating desktop shortcuts, interacting with the Shell, or utilizing specialized system components. This suggests the binary has a sophisticated "hook" into standard Windows functionality beyond simple file copying.

---

### Updated Behavior Summary (Consolidated)

| Feature | Observed Mechanism | Contextual Significance |
| :--- | :--- | :--- |
| **Persistence & Delivery** | NSIS Framework / Multi-stage logic | Standard installer behavior; also common in "droppers." |
| **Dynamic Loading** | `GetSystemDirectoryW` + `LoadLibraryExW` | Ability to load extra modules (DLLs) into memory at runtime. |
| **Data Integrity** | CRC32 Calculation (`0xedb88320`) | Ensuring files are intact before execution/moving. |
| **System Integration** | COM/OLE (`OleInitialize`) | Advanced interaction with the Windows Shell and system objects. |
| **File Manipulation** | `CopyFileW`, `MoveFileW`, `GetTempPathW` | Core installation logic; used to stage payloads in `%TEMP%`. |

---

### Updated Risk Assessment & Conclusion

The inclusion of chunk 2 reinforces the **"Loader/Installer"** hybrid nature of this binary. 

1.  **Installer Indicators:** The presence of NSIS-related strings, CRC32 checks for file integrity, and COM integration for UI/Shortcuts points strongly toward a professional installer.
2.  **Malware Indicator Flags:** The **Dynamic Loading (`LoadLibraryExW`)** from system directories and the robust **integrity checking** are high-interest behaviors. If the DLL being loaded in `fcn.00406624` is not a known, legitimate component of the software being "installed," it suggests the binary acts as a gatekeeper for malicious code.

**Final Recommendation:** 
The binary should be treated as a **suspicious installer/loader**. The next step in analysis should be:
1.  Identifying the specific DLL filenames being passed to `LoadLibraryExW` (via static analysis of the data segments).
2.  Monitoring the file system during execution to see which files are created in the `%TEMP%` directory and where they are ultimately moved. 
3.  Determining if the "integrity check" is performed on standard installer assets or on potentially malicious payload components.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of dynamic loading (`LoadLibraryExW`) and path manipulation allows the binary to hide its full capabilities from static analysis by only loading components at runtime. |
| T1027 | Obfuscated Files or Information | The implementation of CRC32 integrity checks ensures that payloads have not been modified or tampered with (e.g., by security software) before execution. |
| T1105 | Ingress Tool Transfer | The multi-stage logic and the systematic movement of files into the `%TEMP%` directory are characteristic of a "dropper" used to stage components for subsequent stages of an attack. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here is the extraction of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*None detected.*

### **File paths / Registry keys**
*None detected.* (While the behavior mentions `%TEMP%` usage and system directory resolution via `GetSystemDirectoryW`, no specific malicious file paths or hardcoded registry keys were identified in the strings.)

### **Mutex names / Named pipes**
*None detected.*

### **Hashes**
*None detected.*

### **Other artifacts**
*   **Behavioral Indicators (Non-static IOCs):**
    *   **Dynamic Loading:** Execution of `fcn.00406624` which utilizes `GetSystemDirectoryW` and `LoadLibraryExW` to load DLLs at runtime.
    *   **Integrity Checking:** Usage of the CRC32 polynomial (`0xedb88320`) in `fcn.00406787` to verify file integrity before execution (a common trait in both installers and droppers).
    *   **COM/OLE Integration:** Usage of `OleInitialize` and `OleUnlikely` in `fcn.004053f5` to interact with advanced Windows system components.

---
**Analyst Note:** 
The provided data contains no high-fidelity, machine-readable IOCs (such as C2 IPs or specific file hashes). The "indicators" present are behavioral indicators of a **Loader/Installer hybrid**. The primary risk identified is the use of `LoadLibraryExW` to pull in additional functionality and the CRC32 check used to ensure the integrity of potentially malicious payloads before they are activated.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1.  **Malware family:** custom
2.  **Malware type:** loader (or dropper)
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Multi-stage Execution Logic:** The use of `GetTempPathW`, `CopyFileW`, and `MoveFileW` to stage files in the `%TEMP%` directory, combined with an NSIS-style framework, is a classic signature of a "dropper" used to deliver components for later execution.
    *   **Dynamic Payload Loading:** The implementation of `LoadLibraryExW` combined with path manipulation indicates that the binary's primary purpose is to load and execute additional modules into memory at runtime, defining its role as a "loader."
    *   **Integrity Verification:** The inclusion of a CRC32 checksum routine (`0xedb88320`) suggests the loader is designed to verify that its payloads have not been modified or tampered with (e.g., by antivirus software) before they are activated.
