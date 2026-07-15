# Threat Analysis Report

**Generated:** 2026-07-15 06:48 UTC
**Sample:** `068e34ef7cb67e5a8d34b4d6977cd69be00d52b12d119413fb00d9b68dbc63b6_068e34ef7cb67e5a8d34b4d6977cd69be00d52b12d119413fb00d9b68dbc63b6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `068e34ef7cb67e5a8d34b4d6977cd69be00d52b12d119413fb00d9b68dbc63b6_068e34ef7cb67e5a8d34b4d6977cd69be00d52b12d119413fb00d9b68dbc63b6.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 72,377,544 bytes |
| MD5 | `0086c6861a813fee078304f28845bde8` |
| SHA1 | `251593eddce2ccb8aefd51ea02898f54a9882715` |
| SHA256 | `068e34ef7cb67e5a8d34b4d6977cd69be00d52b12d119413fb00d9b68dbc63b6` |
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
| `.rsrc` | 30,208 | 4.205 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`, `GetCommandLineW`

## Extracted Strings

Total strings found: **156704** (showing first 100)

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

This analysis is based on the provided disassembly and strings of a binary sample. Based on the code structure and included strings, here is an assessment of the program's behavior.

### Core Functionality and Purpose
The binary appears to be a **multi-stage installer or "loader"** designed to extract, verify, and execute additional components. The presence of specific error messages (e.g., `"NSIS Error"`), references to `GetTempPathW`, and the logic for copying files into temporary directories indicate it is likely built using the Nullsoft Script Installer (NSIS) or a similar custom installer framework.

Its primary roles are:
*   **Environment Preparation:** It checks system versions, locates temporary folders, and initializes standard Windows components (COM/OLE and common controls).
*   **Data Extraction:** The code includes logic to unpack and move files from internal resources into the filesystem (specifically looking for a staging area to extract "modules").
*   **UI Interaction:** A large portion of the code (`fcn.00401434`) handles standard Windows UI elements, such as rendering buttons, progress bars, and dialog boxes.

### Suspicious or Malicious Behaviors
While the binary functions primarily as an installer, it contains several behaviors common in malware "droppers" and "loaders":

*   **Privilege Escalation/Manipulation:** The code calls `LookupPrivilegeValueW` for `"SeShutdownPrivilege"` and uses `AdjustTokenPrivileges`. While sometimes used by legitimate installers to perform system-level tasks (like restarting the PC), this is a common technique in malware to gain higher permissions for subsequent actions.
*   **File Manipulation & Staging:** The code actively moves files, copies them into temporary directories (e.g., `nsu%X.tmp`), and manipulates file attributes (`SetFileAttributesW`). This "staging" behavior is often used by malware to unpack a hidden payload before executing it.
*   **Dynamic Loading/Execution:** It uses `LoadLibraryExW` and `GetModuleHandleW`. In this context, these are likely used to load the "payload" that was extracted during the installation process. 
*   **Integrity Checking:** The complexity of functions like `fcn.00403dae` suggests a need to validate data before it is unpacked. This ensures that any embedded payload has not been tampered with or altered by security software.

### Notable Techniques and Patterns
*   **NSIS Framework Pattern:** The inclusion of `"NSIS Error"` and the specific way it handles temporary file paths identifies this as an NSIS-based installer. These are frequently used in "Trojanized" installers where a legitimate application is bundled with malicious code.
*   **Large Switch/Dispatch Table:** Function `fcn.00401434` uses a large switch table to handle various internal states and UI commands. This is a common way to manage complex, multi-stage logic (like an installation wizard) while keeping the core logic somewhat obscured from simple linear analysis.
*   **Custom Data Parsing:** Functions like `fcn.00406c4b` suggest the use of custom data structures or a proprietary format for managing internal resources/scripts, which is common in sophisticated installers to hide the true nature of the files being extracted.
*   **System Interaction (Registry & Files):** Extensive calls to `ADVAPI32` (for registry manipulation) and `SHELL32` (for file operations) indicate that the program interacts deeply with the OS environment to ensure its components are installed or "hidden" properly.

### Summary for Security Operations
This sample is likely a **malware dropper/loader**. It uses standard installer techniques—such as creating temporary files, unpacking resources, and escalating privileges—to deliver and execute a primary payload. Because it relies on heavy file manipulation and dynamic loading, the final malicious behavior (e.g., credential theft, ransomware, or persistence) is likely contained in a separate module that this binary extracts and executes.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1068 | Exploitation for Privilege Escalation | The use of `LookupPrivilegeValueW` and `AdjustTokenPrivileges` indicates an attempt to obtain higher system permissions for subsequent actions. |
| T1036 | Masquerading | The use of the NSIS framework and naming conventions like `nsu%X.tmp` allows the malware to hide its activity by mimicking a standard installer. |
| T1112 | Modify Registry | Extensive calls to `ADVAPI32` indicate registry manipulation to ensure components are installed or hidden from the user/system. |
| T1564 | Hide Escape (Defense Evasion) | The inclusion of integrity checks (`fcn.00403dae`) suggests an attempt to detect and evade detection by security software before unpacking the payload. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Many items in the "Extracted Strings" section were identified as standard Windows API calls or library functions; these have been excluded from the final list to filter out false positives.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **`nsu%X.tmp`**: (Pattern) Used for staging files in temporary directories during the installation/unpacking process.

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Framework Identification:** **NSIS (Nullsoft Script Installer)** - The inclusion of `"NSIS Error"` and specific temporary file handling confirms the use of this installer framework.
*   **Privilege Manipulation:** `SeShutdownPrivilege` - Identified via `LookupPrivilegeValueW`; used to elevate privileges for system-level tasks.
*   **Behavioral Patterns:** 
    *   **Staging Behavior:** Active movement and copying of files into temporary directories before execution.
    *   **Dynamic Loading:** Use of `LoadLibraryExW` and `GetModuleHandleW` to load unpacked payloads.
    *   **Integrity Checking:** Complexity in the unpacking routine suggests a check for tampering before final payload execution.
*   **Internal Function Offsets (Analyst Notes):** 
    *   `fcn.00401434` (UI/State Management)
    *   `fcn.00403dae` (Integrity Check)
    *   `fcn.00406c4b` (Custom Data Parsing)

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High (regarding its functional role)

4. **Key evidence**:
*   **Staging and Execution:** The binary exhibits classic dropper behavior by extracting resources into temporary directories (`nsu%X.tmp`) and using `LoadLibraryExW` to execute a secondary payload, indicating it is a vehicle for other malware.
*   **Masquerading via NSIS:** The use of the Nullsoft Script Installer (NSIS) framework is a common technique to disguise malicious installation processes as legitimate software updates or installers.
*   **Evasion and Privilege Escalation:** The inclusion of integrity checks (`fcn.00403dae`) and the specific calls to `LookupPrivilegeValueW` for system-level permissions indicate intent to bypass security controls and ensure the successful deployment of its components.
