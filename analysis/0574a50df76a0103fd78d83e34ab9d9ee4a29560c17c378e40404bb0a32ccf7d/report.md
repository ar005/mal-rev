# Threat Analysis Report

**Generated:** 2026-07-13 21:13 UTC
**Sample:** `0574a50df76a0103fd78d83e34ab9d9ee4a29560c17c378e40404bb0a32ccf7d_0574a50df76a0103fd78d83e34ab9d9ee4a29560c17c378e40404bb0a32ccf7d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0574a50df76a0103fd78d83e34ab9d9ee4a29560c17c378e40404bb0a32ccf7d_0574a50df76a0103fd78d83e34ab9d9ee4a29560c17c378e40404bb0a32ccf7d.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 71,773,480 bytes |
| MD5 | `b42a2a644178b106952394cc89628e45` |
| SHA1 | `4e90d156dd64b26dbfb17036cc65a4551aed9991` |
| SHA256 | `0574a50df76a0103fd78d83e34ab9d9ee4a29560c17c378e40404bb0a32ccf7d` |
| Overall entropy | 8.0 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1741475120 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,624 | 6.454 | No |
| `.rdata` | 5,120 | 5.1 | No |
| `.data` | 1,536 | 4.123 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 80,896 | 4.54 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`, `GetCommandLineW`

## Extracted Strings

Total strings found: **155458** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQWPV
Instuj
softua
NulluX	E
UVWj _3
L$bf-S
D$ Pj(
D$,UPU
tVj%UUU
f9=P/B
D$$+D$
D$,+D$$P
u9=@/B
WWWWjn
us9Et	
FFC;]|
8\tPV
\u f9O
69}t(j
90u'AAf
l$(9l$(tr
+D$(PV
_^][t
P
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
RegEnumValueW
RegEnumKeyW
RegQueryValueExW
RegSetValueExW
RegCloseKey
RegDeleteValueW
RegDeleteKeyW
AdjustTokenPrivileges
LookupPrivilegeValueW
OpenProcessToken
RegOpenKeyExW
RegCreateKeyExW
ADVAPI32.dll
SHFileOperationW
SHGetFileInfoW
SHBrowseForFolderW
SHGetPathFromIDListW
ShellExecuteExW
SHELL32.dll
CoTaskMemFree
IIDFromString
CoCreateInstance
OleUninitialize
OleInitialize
ole32.dll
ImageList_Destroy
ImageList_AddMasked
ImageList_Create
COMCTL32.dll
EndPaint
DrawTextW
FillRect
GetClientRect
BeginPaint
DefWindowProcW
SendMessageW
InvalidateRect
EnableWindow
ReleaseDC
LoadImageW
SetWindowLongW
GetDlgItem
IsWindow
FindWindowExW
SendMessageTimeoutW
wsprintfW
ShowWindow
SetForegroundWindow
PostQuitMessage
SetWindowTextW
SetTimer
CreateDialogParamW
DestroyWindow
ExitWindowsEx
CharNextW
DialogBoxParamW
GetClassInfoW
CreateWindowExW
SystemParametersInfoW
RegisterClassW
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 6196 | ✓ |
| `fcn.00406c4b` | `0x406c4b` | 2642 | ✓ |
| `entry0` | `0x40369f` | 1565 | ✓ |
| `fcn.00403dae` | `0x403dae` | 726 | ✓ |
| `fcn.004030fc` | `0x4030fc` | 724 | ✓ |
| `fcn.00406719` | `0x406719` | 625 | ✓ |
| `fcn.00405de8` | `0x405de8` | 451 | ✓ |
| `fcn.00406322` | `0x406322` | 378 | ✓ |
| `fcn.004034d8` | `0x4034d8` | 361 | ✓ |
| `fcn.004033d0` | `0x4033d0` | 264 | ✓ |
| `fcn.00402ed5` | `0x402ed5` | 234 | ✓ |
| `fcn.00405761` | `0x405761` | 211 | ✓ |
| `fcn.004046c2` | `0x4046c2` | 207 | ✓ |
| `fcn.00404f08` | `0x404f08` | 201 | ✓ |
| `fcn.00404084` | `0x404084` | 185 | ✓ |
| `fcn.0040698a` | `0x40698a` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040305a` | `0x40305a` | 162 | ✓ |
| `fcn.0040663c` | `0x40663c` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.004064c8` | `0x4064c8` | 129 | ✓ |
| `fcn.00405016` | `0x405016` | 128 | ✓ |
| `fcn.004060b3` | `0x4060b3` | 126 | ✓ |
| `fcn.004065aa` | `0x4065aa` | 121 | ✓ |
| `fcn.004062ad` | `0x4062ad` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406a60` | `0x406a60` | 112 | ✓ |
| `fcn.00406bbd` | `0x406bbd` | 110 | ✓ |
| `fcn.00405834` | `0x405834` | 108 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402ed5.c`](code/fcn.00402ed5.c)
- [`code/fcn.0040305a.c`](code/fcn.0040305a.c)
- [`code/fcn.004030fc.c`](code/fcn.004030fc.c)
- [`code/fcn.004033d0.c`](code/fcn.004033d0.c)
- [`code/fcn.004034d8.c`](code/fcn.004034d8.c)
- [`code/fcn.00403dae.c`](code/fcn.00403dae.c)
- [`code/fcn.00404084.c`](code/fcn.00404084.c)
- [`code/fcn.004046c2.c`](code/fcn.004046c2.c)
- [`code/fcn.00404f08.c`](code/fcn.00404f08.c)
- [`code/fcn.00405016.c`](code/fcn.00405016.c)
- [`code/fcn.00405761.c`](code/fcn.00405761.c)
- [`code/fcn.00405834.c`](code/fcn.00405834.c)
- [`code/fcn.00405de8.c`](code/fcn.00405de8.c)
- [`code/fcn.004060b3.c`](code/fcn.004060b3.c)
- [`code/fcn.004062ad.c`](code/fcn.004062ad.c)
- [`code/fcn.00406322.c`](code/fcn.00406322.c)
- [`code/fcn.004064c8.c`](code/fcn.004064c8.c)
- [`code/fcn.004065aa.c`](code/fcn.004065aa.c)
- [`code/fcn.0040663c.c`](code/fcn.0040663c.c)
- [`code/fcn.00406719.c`](code/fcn.00406719.c)
- [`code/fcn.0040698a.c`](code/fcn.0040698a.c)
- [`code/fcn.00406a60.c`](code/fcn.00406a60.c)
- [`code/fcn.00406bbd.c`](code/fcn.00406bbd.c)
- [`code/fcn.00406c4b.c`](code/fcn.00406c4b.c)

## Behavioral Analysis

Based on the disassembly and decompiled pseudocode, here is the analysis of the binary's behavior:

### Core Functionality
The code appears to be a **malware dropper or a component of a multi-stage installer**, likely utilizing the **NSIS (Nullsoft Script Installer)** framework. Its primary purpose is to unpack, verify, and stage files for execution on the target system. 

Instead of being a single application, it acts as a "wrapper" that performs several administrative tasks:
*   **Resource Extraction:** It handles the extraction of data from an embedded resource or a compressed archive.
*   **Integrity Verification:** It utilizes heavy calculation loops (e.g., `fcn.00406bbd`, which is a checksum/hash routine) to ensure that files being unpacked have not been tampered with or corrupted.
*   **Environment Preparation:** It checks for and configures system environment variables, specifically targeting the `TEMP` directory to stage data.
*   **UI Management:** It contains extensive logic for creating windows, handling buttons, and providing feedback to the user (e.g., `"NSIS Error"`, `"Installer integrity check has failed"`).

### Suspicious or Malicious Behaviors
While much of this behavior is common in legitimate installers, from a malware analysis perspective, several elements are highly relevant:

*   **Drop & Execute Pattern:** In `fcn.004030fc`, the code retrieves the system's Temp path (`GetTempPathW`), creates/copies files into that directory with temporary names (e.g., `~nsu[ID].tmp`), and potentially sets environment variables to point to them. This is a standard technique for dropping a payload before executing it.
*   **Environment Manipulation:** The use of `SetEnvironmentVariableW` to change paths or "temporary" locations is often used to redirect the execution flow of subsequent components or to bypass security constraints on the original file path.
*   **File System Interaction:** Use of `MoveFileW`, `CopyFileW`, and `GetTempFileNameW` suggests that the binary moves files from a protected area (where it is running) into a more "accessible" location for execution.
*   **Privilege Check/Adjustment:** The code references `AdjustTokenPrivileges` and `LookupPrivilegeValueW`. While common in installers to grant permissions, these are also used by malware to escalate privileges or bypass certain local restrictions.

### Notable Techniques & Patterns
*   **NSIS Framework usage:** The presence of strings like `"NSIS Error"` and the specific structure of the `fcn.00401389` loop suggest this is a standard NSIS stub. Malware authors frequently use legitimate installer wrappers to "bundle" malicious payloads, as these are less likely to be flagged by heuristic engines.
*   **Checksum Verification:** The complexity of `fcn.00406bbd` and the related functions indicates that the binary validates its internal components before execution. This ensures the payload remains intact during the unpacking process.
*   **COM Interface Usage:** The use of `CoCreateInstance` and various COM-related calls suggests it may interact with high-level Windows features, such as creating desktop shortcuts or interacting with the Shell to "install" components.
*   **Anti-Analysis/Detection (Implicit):** By using a well-known installer engine, the malware hides its true intent behind a familiar interface. If this binary is part of an infection chain, it serves as the "downloader/dropper" layer that handles the messy work of file extraction and environment setup.

### Summary Conclusion
This binary is likely a **malware dropper** disguised as (or utilizing) a standard **NSIS installer**. It performs heavy lifting in terms of:
1.  **Extracting and verifying** hidden payloads from its own resources/files.
2.  **Staging those payloads** in the system's temporary directories.
3.  **Configuring environment variables** to ensure the payload runs correctly. 

The presence of standard installer behavior is a common technique used to **evade signature-based detection** by blending into the "noise" of legitimate software installation processes.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1105** | Ingress Tool Transfer | The binary extracts, moves, and stages files in the `TEMP` directory to prepare them for execution as part of a dropper workflow. |
| **T1027** | Obfuscated Files or Information | The use of internal resources, complex integrity checks (checksums), and hidden payloads is used to mask the malicious nature of the contents. |
| **T1036** | Masquerading | By utilizing the well-known NSIS framework, the malware blends in with legitimate installer activity to evade detection. |
| **T1068** | Exploitation for Privilege Escalation | The explicit use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicates an attempt to acquire higher privileges or bypass system restrictions. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral reports, here are the identified Indicators of Compromise (IOCs). 

Note: Most of the "Extracted Strings" section contains standard Windows API calls (e.g., `CreateFileW`, `GetTempPathW`) and standard system DLLs (`SHELL32.dll`, `USER32.dll`). These have been excluded as they are considered false positives in a general context.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **Path Pattern:** `~nsu[ID].tmp` (Identified in behavior analysis; used for staging files in the system's temporary directory).
*   *Note: While specific registry keys were mentioned as API calls, no hardcoded malicious keys were identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Framework Identification:** NSIS (Nullsoft Script Installer). The presence of `"NSIS Error"` strings and specific installer logic indicates the use of this framework to wrap/drop a payload.
*   **Internal Function Offsets (Code Signatures):** 
    *   `fcn.00406bbd`: Identified as the checksum/hash routine for integrity verification.
    *   `fcn.004030fc`: Identified as the core "Drop & Execute" logic for moving files to the temp directory.
*   **UI Strings:** 
    *   `"NSIS Error"`
    *   `"Installer integrity check has failed"` (Indicates a specific verification step in the dropping process).
*   **Behavioral Pattern:** Use of `GetTempPathW`, `MoveFileW`, and `CopyFileW` to stage payloads in temporary directories.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family**: custom (NSIS-based Dropper)
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **NSIS Framework Wrapper:** The binary utilizes the Nullsoft Script Installer (NSIS) framework and associated strings (e.g., "NSIS Error"), a common technique used by malware authors to masquerade malicious payloads as legitimate software installers to evade heuristic detection.
    *   **Dropper/Staging Behavior:** The analysis identifies clear "Drop & Execute" patterns, specifically the use of `GetTempPathW`, `MoveFileW`, and `CopyFileW` to move and stage files in the system's temporary directory (`~nsu[ID].tmp`) for subsequent execution.
    *   **Integrity Verification:** The presence of complex checksum/hash routines (e.g., `fcn.00406bbd`) indicates that the binary is designed to verify and ensure the integrity of a secondary, hidden payload before it is launched on the host system.
