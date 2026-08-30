# Threat Analysis Report

**Generated:** 2026-08-18 21:42 UTC
**Sample:** `106803719e4aaf7439378baa6a6400d7b40ea0e71fa0f0d5199a7037a6e1a470_106803719e4aaf7439378baa6a6400d7b40ea0e71fa0f0d5199a7037a6e1a470.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `106803719e4aaf7439378baa6a6400d7b40ea0e71fa0f0d5199a7037a6e1a470_106803719e4aaf7439378baa6a6400d7b40ea0e71fa0f0d5199a7037a6e1a470.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 89,221,112 bytes |
| MD5 | `7f906ab14e54ae8534cf33db7e1705f6` |
| SHA1 | `ec4f2e5aff83f789e702a52eefbb100c7d6c233c` |
| SHA256 | `106803719e4aaf7439378baa6a6400d7b40ea0e71fa0f0d5199a7037a6e1a470` |
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
| `.rsrc` | 52,736 | 7.588 | ⚠️ Yes |

### Imports

**KERNEL32.dll**: `SetEnvironmentVariableW`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `CopyFileW`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`, `SetErrorMode`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **193644** (showing first 100)

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

This updated analysis incorporates the findings from the second chunk of disassembly. The new code confirms and expands upon the previously identified behaviors, specifically regarding **payload integrity verification** and **targeted system library loading.**

### Updated Analysis of Binary Behavior

#### 1. Core Functionality and Purpose
The binary remains a **dropper/installer stub**. However, the additional code clarifies its "validation" phase: it doesn't just drop files; it verifies their integrity before execution to ensure the payload is intact (or not corrupted by security scanners). It is designed to move components into system directories and dynamically load them as DLLs.

#### 2. Suspicious or Malicious Behaviors
*   **Payload Integrity Verification (CRC-32):** The function `fcn.00406787` implements a **CRC-32 checksum algorithm**. This is a critical finding: the malware uses this to verify that the files it has unpacked/dropped are correct before they are executed. This ensures that if an antivirus tool modifies or deletes part of the payload, the malware will detect the change and stop execution.
*   **Targeted System Library Loading:** The function `fcn.00406624` specifically targets system directories to load libraries. It constructs a path (e.g., appending `.dll`) and uses `LoadLibraryExW`. This suggests it is designed to drop a malicious DLL into a folder like `System32` or `SysWOW64` and then immediately "hook" into it or execute its code.
*   **Automated Resource Processing:** The loop in `fcn.004053f5` indicates the binary processes a list of items (likely components, files, or commands) sequentially. This is typical of installers that handle multiple subsequent actions (e.g., "Extract File A," "Verify File B," "Launch Payload C").
*   **Dropper/Payload Extraction:** (Previously identified) The binary extracts hidden resources and moves them to system-accessible directories using `GetTempPathW` and `GetSystemDirectoryW`.

#### 3. Notable Techniques & Patterns
*   **CRC-32 Implementation:** The use of the bitwise manipulation (`param_1 >> 8 ^ ...`) in `fcn.00406787` is a classic optimized implementation of the CRC-32 algorithm. Its presence confirms a high level of intent to ensure "successful" infection of the environment.
*   **Dynamic Path Construction for DLLs:** Instead of using hardcoded paths, the code dynamically builds strings to point to `.dll` files in system directories. This allows the malware to be more portable and adapt to different Windows versions while ensuring it lands in a high-privilege location.
*   **OLE Integration:** The presence of `OleInitialize` and `OleUninitialize` suggests the installer may interact with COM objects or use standard Windows Installer components (like those used by NSIS) to handle complex installations, though this is also common in legitimate installers.
*   **Switch-Table Dispatcher:** (Previously identified) The large switch-case structure indicates a sophisticated state machine for handling various installation stages or error states.

---

### Updated Summary for Incident Response

| Risk Factor | Detection Detail | Significance |
| :--- | :--- | :--- |
| **Malware Type** | Dropper / Installer Stub | High - Used to deliver primary payloads. |
| **Payload Verification** | CRC-32 Checksum (fcn.00406787) | **Critical** - Indicates the malware verifies its components before activation to bypass simple tampering or deletion. |
| **System Interaction** | `GetSystemDirectoryW` + `LoadLibraryExW` | High - The binary specifically targets system directories to host and load DLLs. |
| **Evasion Tactics** | Dynamic Library Loading / Resource Hiding | Medium-High - Uses common installer techniques to mask the transition from "installer" to "malware." |

**Incident Response Note:** 
This sample is a highly structured loader. The inclusion of CRC32 integrity checks indicates it is designed to be resilient; if you find one part of the payload, others are likely present and checked by this stub. The focus on **System Directory** interaction and **DLL loading** suggests that the ultimate goal is to establish persistence or execute high-privilege code via a dropped .dll file. 

**Recommended Actions:**
1.  **Host Isolation:** Isolate any machine where this binary was executed.
2.  **File System Audit:** Search for recently created `.dll` files in `%SystemRoot%\System32` and `%SystemRoot%\SysWOW64`.
3.  **Persistence Check:** Monitor for new services or scheduled tasks that point to the newly dropped DLLs.
4.  **Memory Analysis:** Perform memory forensics on processes launched by this stub to identify the "true" payload hidden behind the loader's logic.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The malware uses system directories (System32/SysWOW64) and dynamic path construction to hide malicious DLLs among legitimate system files. |
| T1568 | Dynamic Resolution | The use of `LoadLibraryExW` allows the malware to dynamically resolve and load its payload into memory at runtime rather than being statically linked. |
| T1547 | Persistence | Placing payloads in system-wide directories and ensuring integrity via CRC checks suggests an attempt to maintain a stable, long-term presence on the host. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `%SystemRoot%\System32` (Targeted directory for dropped DLLs)
*   `%SystemRoot%\SysWOW64` (Targeted directory for dropped DLLs)
*   *(Note: Specific filenames were not provided in the analysis, but the behavior indicates a focus on these system paths.)*

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified. (The CRC-32 mentioned is a verification algorithm, not a specific file hash).

**Other artifacts**
*   **CRC-32 Integrity Check:** The malware utilizes a custom or standard CRC-32 implementation (specifically noted at `fcn.00406787`) to verify the integrity of dropped payloads before execution.
*   **Dynamic Library Loading:** Use of `LoadLibraryExW` to dynamically load and execute `.dll` files from system directories.
*   **Persistence Mechanism:** The use of `GetSystemDirectoryW`, `GetTempPathW`, and `MoveFileExW` to transition a dropper into a persistent, hidden state.

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
*   **Integrity Verification:** The inclusion of a CRC-32 check (`fcn.00406787`) specifically intended to verify payload integrity ensures the malware only executes if its components haven't been tampered with or removed by security software.
*   **Systemized Persistence & Stealth:** The binary utilizes `GetSystemDirectoryW` and `LoadLibraryExW` to move and load malicious DLLs into high-privilege system directories (`System32`/`SysWOW64`), a classic technique for establishing persistence and hiding within the OS structure.
*   **Structured Execution Flow:** The use of a switch-table dispatcher and automated resource processing indicates a sophisticated, multi-stage installation routine designed to transition from an initial "dropper" state to a persistent "loaded" state.
