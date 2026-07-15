# Threat Analysis Report

**Generated:** 2026-07-14 15:41 UTC
**Sample:** `05c1c274fab9c2dbc679e70b67d748599a1fe6e05f49729ba10af76424460f30_05c1c274fab9c2dbc679e70b67d748599a1fe6e05f49729ba10af76424460f30.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05c1c274fab9c2dbc679e70b67d748599a1fe6e05f49729ba10af76424460f30_05c1c274fab9c2dbc679e70b67d748599a1fe6e05f49729ba10af76424460f30.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 531,584 bytes |
| MD5 | `d8aded9889166f9a7e241ea5a11e2018` |
| SHA1 | `40a41825019e850f4fb38738e90c8501c7169cca` |
| SHA256 | `05c1c274fab9c2dbc679e70b67d748599a1fe6e05f49729ba10af76424460f30` |
| Overall entropy | 7.496 |
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
| `.rsrc` | 233,472 | 6.658 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`, `GetCommandLineW`

## Extracted Strings

Total strings found: **960** (showing first 100)

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

Based on the provided disassembly and decompiled C code, here is an analysis of the binary's functionality and behavior.

### Core Functionality
The binary functions as a **software installer**, specifically one utilizing the **NSIS (Nullsoft Script Installer)** framework. Its primary purpose is to extract components, verify their integrity, move them to final locations, and potentially register system entries or registry keys associated with an application's installation.

### Suspicious or Malicious Behaviors
While many of these behaviors are standard for installers, they are also commonly utilized by malware (especially "droppers" or "loaders") to deliver malicious payloads:

*   **Integrity Verification:** The code contains complex mathematical loops (e.g., in `fcn.00406c4b`) that appear to perform CRC32 or similar checksum calculations. This ensures the files being moved or executed have not been corrupted, a common step before an installer executes a secondary payload.
*   **Privilege Escalation:** The presence of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicates the program seeks to escalate its privileges (e.g., seeking "SeShutdownPrivilege" or similar). While used by installers to modify system files, this is a high-risk technique for gaining administrative control.
*   **File Manipulation & Staging:** The code extensively uses `MoveFileW`, `CopyFileW`, and `DeleteFileW`. It specifically identifies temporary paths (e.g., `%TEMP%`) to stage files, rename them (referenced as `.tmp` or `nsu` prefixed files), and move them to final destinations.
*   **Registry Manipulation:** The code interacts with the Windows Registry via `RegOpenKeyExW`, `RegCreateKeyExW`, and `RegSetValueExW`. This is used to persist application settings, but in a malware context, this is used to ensure persistence or modify system configurations.
*   **Execution of External Components:** Use of `ShellExecuteW` and `CreateProcessW` suggests the installer's final step is to launch another executable or a script after successful deployment.

### Notable Techniques & Patterns
*   **NSIS Framework Pattern:** The structure of the code (specifically the massive switch-case logic in `fcn.00401434`, the "NSIS Error" strings, and the specific handling of file paths) is a hallmark of the NSIS installer suite. 
*   **Environment Awareness:** The code includes logic to detect if it is running in a 32-bit or 64-bit environment (checking for `SysWow64` and `System32` in path strings). This ensures compatibility but also helps malware tailor its behavior based on the target OS architecture.
*   **Dropper Logic:** The way the code handles temporary files (creating a file, copying data into it, then moving/renaming it) is characteristic of a "dropper" mechanism where an initial stub delivers and prepares the actual malicious payload for execution.

### Summary Table of Key Indicators
| Feature | Observation | Potential Risk |
| :--- | :--- | :--- |
| **Tooling** | NSIS Installer Framework | Common vehicle for malware distribution. |
| **Privileges** | `AdjustTokenPrivileges` | Escalation to administrative/system levels. |
| **File Ops** | Stage in `%TEMP%`, Rename, Move | Dropper behavior; preparing payload for execution. |
| **Integrity** | Checksum loops (CRC32-like) | Verification of a secondary stage component. |
| **Persistence**| Registry Key Creation/Modification | Establishing persistence on the local machine. |

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your report to the relevant MITRE ATT&K techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1068** | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicates an attempt to gain higher-level system permissions. |
| **T1112** | Modify Registry | Use of `RegOpenKeyExW`, `RegCreateKeyExW`, and `RegSetValueExW` is used to modify configuration or establish persistence. |
| **T1036** | Masquerading | Moving files to `%TEMP%` and renaming them (e.g., `.tmp` or `nsu`) is a common tactic to hide the presence of malicious payloads. |
| **T1204** | User Execution | The use of `ShellExecuteW` and `CreateProcessW` signals the final step of delivering and running a secondary payload for the user. |
| **T1548** | Privilege Abuse | Utilizing legitimate installer tools (like NSIS) to carry out malicious actions allows attackers to blend in with normal system activity. |
| **T1489** | System Host Execution | The logic used to detect 32-bit/64-bit environments and specific system paths is often used to tailor behavior based on the target environment. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** As per your instructions, standard Windows API calls (e.g., `RegOpenKeyExW`, `CreateProcessW`) and generic system paths (e.g., `%TEMP%`) have been excluded as they are common to both legitimate software and malware.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (The analysis mentions registry manipulation and file staging, but no specific malicious keys or hardcoded paths were provided in the source text).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Framework Identification:** NSIS (Nullsoft Script Installer) — The binary utilizes the NSIS framework for installation, a common method for both legitimate software and malware distribution.
*   **Integrity Checks:** Presence of CRC32-like checksum loops in `fcn.00406c4b` to verify secondary payloads.
*   **Privilege Escalation Logic:** Use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` to request administrative/system privileges.
*   **Dropper Behavior:** Execution of "Staging" logic (Copying, Renaming with `.tmp` or `nsu` prefixes, and Moving files) typical of malware droppers.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: custom (NSIS Wrapper)
2. **Malware type**: dropper
3. **Confidence**: Medium

4. **Key evidence**:
*   **Dropper Architecture:** The binary exhibits classic "dropper" behavior by staging files in `%TEMP%` directories, renaming them, and performing CRC32-style integrity checks to verify payload components before execution.
*   **Wrapper Tactics:** It utilizes the NSIS (Nullsoft Script Installer) framework, a common technique used to mask malicious activity as legitimate software installation while providing an easy method for distributing hidden payloads.
*   **Persistence & Privilege Escalation:** The use of `AdjustTokenPrivileges` and registry manipulation indicates that the installer's role is to prepare the environment and gain high-level permissions for a secondary, potentially more malicious, payload.
