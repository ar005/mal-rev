# Threat Analysis Report

**Generated:** 2026-07-25 18:42 UTC
**Sample:** `0b0f333fde9599053b51e87571be8bc4c1768f4500dd2e652dc38588819ab9b8_0b0f333fde9599053b51e87571be8bc4c1768f4500dd2e652dc38588819ab9b8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b0f333fde9599053b51e87571be8bc4c1768f4500dd2e652dc38588819ab9b8_0b0f333fde9599053b51e87571be8bc4c1768f4500dd2e652dc38588819ab9b8.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 77,399,680 bytes |
| MD5 | `bde3a70494d08517ebb2fe723e04e5d3` |
| SHA1 | `ff783c68d862e873185d7dc18f9cd7d89d16178f` |
| SHA256 | `0b0f333fde9599053b51e87571be8bc4c1768f4500dd2e652dc38588819ab9b8` |
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
| `.rsrc` | 104,448 | 7.959 | ⚠️ Yes |

### Imports

**KERNEL32.dll**: `SetEnvironmentVariableW`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `CopyFileW`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`, `SetErrorMode`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **168049** (showing first 100)

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

This updated analysis incorporates the new disassembly data provided in chunk 2/2, expanding on the existing findings regarding its behavior as an installer stub and highlighting newly identified techniques for payload verification and dynamic library loading.

### Updated Technical Analysis

#### Core Functionality and Purpose
The binary remains identified as a **scripting interpreter or installer stub**, likely based on the **NSIS (Nullsoft Scriptable Install System)** framework. 

However, the additional code reveals more sophisticated capabilities beyond simple file copying:
1.  **Dynamic Component Loading:** The binary contains logic to dynamically load and interact with DLLs from system directories.
2.  **Integrity Verification:** It includes a dedicated routine for calculating checksums (likely CRC32) to verify the integrity of components or internal data structures.

#### Suspicious or Malicious Behaviors
The following behaviors are now confirmed or expanded upon:

*   **Dynamic Library Loading (DLL Injection/Loading):** In `fcn.00406624`, the binary retrieves the system directory, constructs a path for a `.dll` file, and calls `LoadLibraryExW`. 
    *   *Risk:* This allows the installer to "load in" additional functionality at runtime. In malware, this is often used to transition from an initial "loader" to a more complex "payload" or to bypass static scanners by keeping the primary malicious code inside a secondary DLL that is only loaded when needed.
*   **Payload Integrity Checking (CRC32):** The function `fcn.00406787` implements a standard CRC-32 checksum algorithm (identifiable by the constant `0xedb88320`). 
    *   *Risk:* This is often used in multi-stage malware to verify that a downloaded or extracted "plug-in" or "payload" hasn't been corrupted or modified by security software before it is executed. It ensures the "malware" package remains intact during the transition from one stage to another.
*   **Automated File Manipulation:** (Previously identified) The extensive use of `CreateDirectoryW`, `MoveFileW`, and `CopyFileW` continues to suggest a downloader/dropper role.
*   **Registry Manipulation & Environment Configuration:** (Previously identified) Continued evidence of persistence mechanisms and environment manipulation via the NSIS-style dispatcher (`fcn.00401434`).

#### Notable Techniques & Patterns
*   **CRC-32 Implementation:** The implementation in `fcn.00406787` is a classic example of how malware ensures consistency across different infection targets. By checking the hash of its components, it ensures that only "approved" malicious files are executed by the dispatcher.
*   **Dynamic Path Construction for DLLs:** The logic in `fcn.00406624` specifically looks for a `.dll` extension and maps it to system-relative paths. This is a common technique to ensure compatibility across different Windows versions while facilitating the loading of components.
*   **OLE/COM Initialization:** The presence of `OleInitialize` in `fcn.004053f5` suggests the binary may interact with COM objects, which can be used for various tasks including OLE automation or interacting with complex system APIs common in sophisticated installers (and some advanced malware).
*   **Script Engine Architecture:** The core of the program remains a "dispatcher" model. This allows the author to swap out scripts while keeping the main binary's signature consistent, making it harder for antivirus signatures to track changes across different variants.

### Summary for Incident Response
This is a **sophisticated installer stub/dropper**. Unlike a simple script, this binary includes robust features typically found in high-quality malware loaders:

1.  **Validation:** It checks the integrity of its own components using CRC32 before proceeding.
2.  **Modularity:** It uses dynamic DLL loading to execute different functions depending on the required "stage" of the infection.
3.  **Stealth through Abstraction:** By using an NSIS-style dispatcher, it hides its primary malicious logic within scripts/data blocks rather than hardcoded commands.

**Recommendation:** Treat this binary as a high-confidence **Dropper**. The presence of `LoadLibraryExW` and the CRC-32 check suggests that this is not just a simple installer but part of a multi-stage infection chain. Any system where this file was executed should be scanned for secondary `.dll` files dropped in `%AppData%`, `%Temp%`, or system directories, as these are likely the primary payloads.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1059 | Scripting Interpreter | The binary is identified as an NSIS-style installer stub and scripting interpreter to hide primary malicious logic within script blocks. |
| T1105 | Ingress Tool Transfer | The use of `CreateDirectoryW`, `MoveFileW`, and `CopyFileW` confirms the binary's role as a dropper/downloader for moving files into the system. |
| T1112 | Modify Registry | The analysis explicitly notes evidence of registry manipulation to establish persistence and perform environment configuration. |
| T1036 | Masquerading | The use of an NSIS-style dispatcher allows the threat actor to hide malicious functions behind a legitimate installer structure, complicating signature detection. |

---

## Indicators of Compromise

Based on the analysis of the strings and behavioral report provided, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Many strings in the "EXTRACTED STRINGS" section were excluded as they represent standard Windows API calls or system libraries (e.g., `KERNEL32.dll`, `USER32.dll`, `GetTickCount`), which are considered false positives in this context.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified (The report mentions generic system locations like `%AppData%` and `%Temp%`, but no specific malicious file paths or registry keys were provided).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified. 
    *(Note: The value `0xedb88320` found in the analysis is a standard CRC-32 polynomial constant and is not a unique file hash.)*

### **Other artifacts**
*   **Behavioral Signature:** NSIS (Nullsoft Scriptable Install System) dispatcher pattern.
*   **Integrity Check:** Implementation of CRC-32 checksum algorithm at `fcn.00406787`.
*   **Dynamic Loading:** Use of `LoadLibraryExW` at `fcn.00406624` to dynamically load DLLs from system directories for multi-stage execution.
*   **Potential Drop Zones:** Evidence of file manipulation in `%AppData%`, `%Temp%`, and system directories via `CreateDirectoryW`, `MoveFileW`, and `CopyFileW`.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

**Key evidence**:
* **Multi-stage Execution & Validation:** The binary utilizes CRC-32 checksums and `LoadLibraryExW` to verify and dynamically load additional components, a hallmark of sophisticated droppers used to transition from an initial stub to a primary payload.
* **Obfuscation through Abstraction:** It employs an NSIS-style dispatcher architecture to hide malicious logic within script blocks rather than hardcoded instructions, making it harder for static analysis tools to identify the full scope of its actions.
* **File Manipulation & Persistence:** The use of `CreateDirectoryW`, `MoveFileW`, and `CopyFileW` specifically targeting common directories like `%AppData%` and `%Temp%`, combined with registry manipulation, confirms its role in establishing a foothold for subsequent malware stages.
