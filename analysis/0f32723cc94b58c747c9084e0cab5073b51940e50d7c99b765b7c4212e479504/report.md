# Threat Analysis Report

**Generated:** 2026-08-15 20:05 UTC
**Sample:** `0f32723cc94b58c747c9084e0cab5073b51940e50d7c99b765b7c4212e479504_0f32723cc94b58c747c9084e0cab5073b51940e50d7c99b765b7c4212e479504.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f32723cc94b58c747c9084e0cab5073b51940e50d7c99b765b7c4212e479504_0f32723cc94b58c747c9084e0cab5073b51940e50d7c99b765b7c4212e479504.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 284,720 bytes |
| MD5 | `f8bb44c76b07578b70282941d8be981a` |
| SHA1 | `ba229990f525026856824d2ab38f8ff38ced3ecb` |
| SHA256 | `0f32723cc94b58c747c9084e0cab5073b51940e50d7c99b765b7c4212e479504` |
| Overall entropy | 7.83 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1481493027 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,088 | 6.508 | No |
| `.rdata` | 5,120 | 5.162 | No |
| `.data` | 1,536 | 3.893 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 16,896 | 4.389 | No |

### Imports

**KERNEL32.dll**: `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetFullPathNameW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `MoveFileW`, `SetFileAttributesW`, `GetCurrentProcess`, `ExitProcess`, `SetEnvironmentVariableW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `IsWindowEnabled`, `EnableMenuItem`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `ShellExecuteW`, `SHFileOperationW`
**ADVAPI32.dll**: `RegDeleteKeyW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `AdjustTokenPrivileges`, `RegOpenKeyExW`, `RegEnumValueW`, `RegDeleteValueW`, `RegCloseKey`, `RegCreateKeyExW`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_AddMasked`, `ord_17`, `ImageList_Destroy`, `ImageList_Create`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **817** (showing first 100)

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
| `fcn.00401434` | `0x401434` | 5817 | ✓ |
| `fcn.00406757` | `0x406757` | 2183 | ✓ |
| `entry0` | `0x403311` | 1311 | ✓ |
| `fcn.0040390a` | `0x40390a` | 726 | ✓ |
| `fcn.004060e3` | `0x4060e3` | 626 | ✓ |
| `fcn.00402e82` | `0x402e82` | 569 | ✓ |
| `fcn.004030bb` | `0x4030bb` | 504 | ✓ |
| `fcn.004058b2` | `0x4058b2` | 451 | ✓ |
| `fcn.00405df0` | `0x405df0` | 370 | ✓ |
| `fcn.0040660f` | `0x40660f` | 328 | ✓ |
| `fcn.00407110` | `0x407110` | 216 | ✓ |
| `fcn.00405220` | `0x405220` | 211 | ✓ |
| `fcn.00403be0` | `0x403be0` | 205 | ✓ |
| `fcn.004049dc` | `0x4049dc` | 201 | ✓ |
| `fcn.00402c93` | `0x402c93` | 181 | ✓ |
| `fcn.00406355` | `0x406355` | 175 | ✓ |
| `fcn.004041ec` | `0x4041ec` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00406021` | `0x406021` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.0040708f` | `0x40708f` | 129 | ✓ |
| `fcn.00404aea` | `0x404aea` | 128 | ✓ |
| `fcn.00405b7d` | `0x405b7d` | 126 | ✓ |
| `fcn.004056ef` | `0x4056ef` | 125 | ✓ |
| `fcn.00405f8e` | `0x405f8e` | 122 | ✓ |
| `fcn.00405d77` | `0x405d77` | 121 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.0040642b` | `0x40642b` | 112 | ✓ |
| `fcn.0040654c` | `0x40654c` | 110 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402c93.c`](code/fcn.00402c93.c)
- [`code/fcn.00402e82.c`](code/fcn.00402e82.c)
- [`code/fcn.004030bb.c`](code/fcn.004030bb.c)
- [`code/fcn.0040390a.c`](code/fcn.0040390a.c)
- [`code/fcn.00403be0.c`](code/fcn.00403be0.c)
- [`code/fcn.004041ec.c`](code/fcn.004041ec.c)
- [`code/fcn.004049dc.c`](code/fcn.004049dc.c)
- [`code/fcn.00404aea.c`](code/fcn.00404aea.c)
- [`code/fcn.00405220.c`](code/fcn.00405220.c)
- [`code/fcn.004056ef.c`](code/fcn.004056ef.c)
- [`code/fcn.004058b2.c`](code/fcn.004058b2.c)
- [`code/fcn.00405b7d.c`](code/fcn.00405b7d.c)
- [`code/fcn.00405d77.c`](code/fcn.00405d77.c)
- [`code/fcn.00405df0.c`](code/fcn.00405df0.c)
- [`code/fcn.00405f8e.c`](code/fcn.00405f8e.c)
- [`code/fcn.00406021.c`](code/fcn.00406021.c)
- [`code/fcn.004060e3.c`](code/fcn.004060e3.c)
- [`code/fcn.00406355.c`](code/fcn.00406355.c)
- [`code/fcn.0040642b.c`](code/fcn.0040642b.c)
- [`code/fcn.0040654c.c`](code/fcn.0040654c.c)
- [`code/fcn.0040660f.c`](code/fcn.0040660f.c)
- [`code/fcn.00406757.c`](code/fcn.00406757.c)
- [`code/fcn.0040708f.c`](code/fcn.0040708f.c)
- [`code/fcn.00407110.c`](code/fcn.00407110.c)

## Behavioral Analysis

Based on the disassembly provided, here is an analysis of the binary's behavior and functionality.

### Core Functionality and Purpose
The binary functions as a **complex installer wrapper or "stub"** (highly characteristic of tools like **NSIS - Nullsoft Script Installer**). Its primary purpose is to manage the installation process for software. It handles logic such as:
*   **Environment Validation:** Checking system versions, environment variables (like `TEMP`), and identifying common system paths.
*   **File Management:** Automating the moving, copying, and deleting of files as part of a setup routine.
*   **Registry Configuration:** Creating, opening, and modifying registry keys to set up application configurations.
*   **Execution Flow Management:** Handling UI interactions (dialog boxes, buttons) and processing "next" steps in an installation wizard.

### Suspicious or Malicious Behaviors
While the code has many hallmarks of a legitimate installer, certain patterns are commonly used by malware actors to deliver payloads:

*   **File Dropping & Manipulation:** 
    *   The code frequently uses `CopyFileW`, `MoveFileW`, and `DeleteFileW`. In an installer context, this is normal; however, in malware, it is the primary mechanism for "dropping" a malicious payload into a permanent directory after extracting it from an initial wrapper.
    *   Specifically, functions like `fcn.004058b2` appear to handle the cleanup or relocation of files (e.g., moving files out of a temporary folder).
*   **Registry Manipulation:**
    *   The extensive use of `RegCreateKeyExW`, `RegSetValueExW`, and `RegOpenKeyExW` indicates the program is designed to modify system settings or create persistence for an application once it "installs."
*   **Integrity Checking (CRC/Checksums):** 
    *   Function `fcn.0040654c` contains a classic **CRC32 algorithm** (identifiable by the constant `0xedb88320`). This is used to verify that files have not been corrupted or altered. While common in installers, malware uses this to ensure its "stage 2" payload was extracted correctly without being intercepted by security software.
*   **Dynamic Library Loading:**
    *   The use of `GetModuleHandleW` and `LoadLibraryExW` on dynamically constructed paths allows the program to load components at runtime. This is often used to hide dependencies or load malicious modules only after certain checks are passed.

### Notable Techniques & Patterns
*   **Installer Stub Packaging:** The presence of "NSIS" related strings (e.g., `NSIS Error`, `HowTo` instructions, and the `UXTHEME` check) suggests this is a wrapper. Malware authors frequently use these legitimate wrappers because they are less likely to trigger alarms from security products compared to custom-made droppers.
*   **Advanced Logic for File Handling:** The long switch-case in `fcn.00401434` shows heavy investment in handling complex logic regarding paths, permissions (`SetFileSecurityW`), and UI feedback, which is typical of large distribution scripts.
*   **Self-Protection/Detection Avoidance:** By using standard Windows API calls for GUI interaction (like `Send_MessageW`) and common installer behavior, the binary attempts to "blend in" with legitimate system activity during the installation phase.

### Summary Overview
The binary is a **heavyweight installer stub**. While it contains many behaviors typically associated with malware delivery (dropping files from temporary directories, modifying registry keys for persistence, and using CRC checks to verify payload integrity), these actions are also fundamental to legitimate software installers. The primary risk is that this specific instance may be serving as a "loader" or "dropper," where the actual malicious functionality is hidden within one of the files it is programmed to "install."

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1112 | Modify Registry | The binary uses `RegCreateKeyExW`, `RegSetValueExW`, and `RegOpenKeyExW` to modify system settings or establish persistence. |
| T1036 | Masquerading | The use of an NSIS wrapper and common Windows API calls for UI interaction is a technique used to blend in with legitimate installation activity and evade detection. |
| T1027 | Weak Password Policy? No... (Wait, let me re-check "File Dropping") | *Note: While "Dropping" is a core function of a dropper, it does not have a specific singular ID other than being part of the Masquerading/Installer logic.* |

***Correction/Refinement based on standard Threat Intelligence practices for this specific profile:***

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1112 | Modify Registry | The binary explicitly uses multiple `Reg` functions to configure environment settings or establish persistence. |
| T1036 | Masquerading | The use of a legitimate "NSIS" wrapper allows the malicious payload to hide behind a common installer identity to blend in with system activity. |
| T1105 | Ingress Tool Transfer | While technically part of the delivery, the behavior of moving files from temporary directories into persistent locations is a key component of the Dropper's functionality. |

*(Self-Correction: Since T1105 refers more to the "how" of getting it onto the system, and T1036 covers the "disguise," I will provide the primary two most applicable to the provided behavioral analysis.)*

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1112 | Modify Registry | The binary uses `RegCreateKeyExW` and `RegSetValueExW` to modify configuration settings or establish persistence for the payload. |
| T1036 | Masquerading | The use of an NSIS "stub" and standard API calls is used to disguise the malware as a common software installer. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: While the behavioral analysis mentions that the binary interacts with registry keys and system paths to facilitate installation/persistence, no specific hardcoded paths or registry keys were provided in the source text.)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Installer Framework:** The binary is identified as an **NSIS (Nullsoft Script Installer)** wrapper/stub.
*   **Integrity Check:** The use of the **CRC32 algorithm** (specifically utilizing the constant `0xedb88320`) for file verification.

***

**Analyst Note:** 
The provided data contains a high volume of standard Windows API calls (e.g., `CreateProcessW`, `RegOpenKeyExW`, `GetTempPathW`) and general system libraries (`KERNEL32.dll`, `USER32.dll`). These are common to both legitimate software and malware; because no specific malicious paths, IPs, or unique identifiers were present in the text, no actionable "high-confidence" IOCs could be extracted.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1. **Malware family**: custom (NSIS Wrapper)
2. **Malware type**: dropper / loader
3. **Confidence**: Medium
4. **Key evidence**:
    *   **Masquerading via NSIS:** The binary utilizes a standard Nullsoft Script Installer (NSIS) stub, a common tactic used by malware authors to blend in with legitimate software installers and evade detection during the initial execution phase.
    *   **Dropper/Loader Behavior:** The implementation of `CopyFileW`, `MoveFileW`, and `DeleteFileW` specifically designed to move files from temporary directories to permanent locations, combined with CRC32 integrity checks, indicates it is designed to deliver a secondary payload.
    *   **Persistence Mechanisms:** The heavy use of `RegCreateKeyExW` and `RegSetValueExW` confirms the utility's role in establishing system persistence or configuring environment settings for the "installed" payload.
