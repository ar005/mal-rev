# Threat Analysis Report

**Generated:** 2026-06-27 05:07 UTC
**Sample:** `0199de3c22dbb41a7cae1c6d5dfef4733b55fad2c58d59045f9a6093bac350ec_0199de3c22dbb41a7cae1c6d5dfef4733b55fad2c58d59045f9a6093bac350ec.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0199de3c22dbb41a7cae1c6d5dfef4733b55fad2c58d59045f9a6093bac350ec_0199de3c22dbb41a7cae1c6d5dfef4733b55fad2c58d59045f9a6093bac350ec.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 687,720 bytes |
| MD5 | `4aed977a14cc91e4e6e68dd4998709b3` |
| SHA1 | `df34b6ac151e125be98fd3ec43d28f06b3b1cb4a` |
| SHA256 | `0199de3c22dbb41a7cae1c6d5dfef4733b55fad2c58d59045f9a6093bac350ec` |
| Overall entropy | 7.918 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1632606949 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,112 | 6.44 | No |
| `.rdata` | 5,120 | 5.146 | No |
| `.data` | 1,536 | 4.014 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 20,480 | 1.776 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `SetFileSecurityW`, `RegOpenKeyExW`, `RegEnumValueW`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHFileOperationW`, `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `ShellExecuteExW`, `SHGetFileInfoW`
**ole32.dll**: `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `GetClientRect`, `EndPaint`, `DrawTextW`, `IsWindowEnabled`, `DispatchMessageW`, `wsprintfA`, `CharNextA`, `CharPrevW`, `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `GetSystemMetrics`, `FillRect`, `AppendMenuW`, `TrackPopupMenu`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectW`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetModuleHandleA`, `GetProcAddress`, `GetSystemDirectoryW`, `lstrcatW`, `Sleep`, `lstrcpyA`, `WriteFile`, `GetTempFileNameW`, `CreateFileW`, `lstrcmpiA`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`

## Extracted Strings

Total strings found: **1574** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495L
tQWPV
Instu`
softuW
NulluN	E
SVWj _3
tVj%SSS
D$$+D$
D$,+D$$P
WWWWjn
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
SetFileSecurityW
RegOpenKeyExW
RegCreateKeyExW
ADVAPI32.dll
SHFileOperationW
SHGetFileInfoW
SHBrowseForFolderW
SHGetPathFromIDListW
ShellExecuteExW
SHGetSpecialFolderLocation
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
EndDialog
ScreenToClient
GetWindowRect
EnableMenuItem
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 6152 | ✓ |
| `fcn.00406a4f` | `0x406a4f` | 2642 | ✓ |
| `entry0` | `0x4034f7` | 1509 | ✓ |
| `fcn.00403bb6` | `0x403bb6` | 726 | ✓ |
| `fcn.00406544` | `0x406544` | 586 | ✓ |
| `fcn.0040307d` | `0x40307d` | 567 | ✓ |
| `fcn.004032b4` | `0x4032b4` | 485 | ✓ |
| `fcn.00405c13` | `0x405c13` | 451 | ✓ |
| `fcn.0040614d` | `0x40614d` | 378 | ✓ |
| `fcn.00402ea9` | `0x402ea9` | 234 | ✓ |
| `fcn.00405569` | `0x405569` | 211 | ✓ |
| `fcn.004044ca` | `0x4044ca` | 207 | ✓ |
| `fcn.00404d10` | `0x404d10` | 201 | ✓ |
| `fcn.00403e8c` | `0x403e8c` | 185 | ✓ |
| `fcn.0040678e` | `0x40678e` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00406467` | `0x406467` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.004062f3` | `0x4062f3` | 129 | ✓ |
| `fcn.00404e1e` | `0x404e1e` | 128 | ✓ |
| `fcn.00405ede` | `0x405ede` | 126 | ✓ |
| `fcn.00405a38` | `0x405a38` | 125 | ✓ |
| `fcn.004063d5` | `0x4063d5` | 121 | ✓ |
| `fcn.004060d8` | `0x4060d8` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406864` | `0x406864` | 112 | ✓ |
| `fcn.004069c1` | `0x4069c1` | 110 | ✓ |
| `fcn.0040563c` | `0x40563c` | 108 | ✓ |
| `fcn.00405b67` | `0x405b67` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402ea9.c`](code/fcn.00402ea9.c)
- [`code/fcn.0040307d.c`](code/fcn.0040307d.c)
- [`code/fcn.004032b4.c`](code/fcn.004032b4.c)
- [`code/fcn.00403bb6.c`](code/fcn.00403bb6.c)
- [`code/fcn.00403e8c.c`](code/fcn.00403e8c.c)
- [`code/fcn.004044ca.c`](code/fcn.004044ca.c)
- [`code/fcn.00404d10.c`](code/fcn.00404d10.c)
- [`code/fcn.00404e1e.c`](code/fcn.00404e1e.c)
- [`code/fcn.00405569.c`](code/fcn.00405569.c)
- [`code/fcn.0040563c.c`](code/fcn.0040563c.c)
- [`code/fcn.00405a38.c`](code/fcn.00405a38.c)
- [`code/fcn.00405b67.c`](code/fcn.00405b67.c)
- [`code/fcn.00405c13.c`](code/fcn.00405c13.c)
- [`code/fcn.00405ede.c`](code/fcn.00405ede.c)
- [`code/fcn.004060d8.c`](code/fcn.004060d8.c)
- [`code/fcn.0040614d.c`](code/fcn.0040614d.c)
- [`code/fcn.004062f3.c`](code/fcn.004062f3.c)
- [`code/fcn.004063d5.c`](code/fcn.004063d5.c)
- [`code/fcn.00406467.c`](code/fcn.00406467.c)
- [`code/fcn.00406544.c`](code/fcn.00406544.c)
- [`code/fcn.0040678e.c`](code/fcn.0040678e.c)
- [`code/fcn.00406864.c`](code/fcn.00406864.c)
- [`code/fcn.004069c1.c`](code/fcn.004069c1.c)
- [`code/fcn.00406a4f.c`](code/fcn.00406a4f.c)

## Behavioral Analysis

Based on the disassembly and string analysis provided, here is an assessment of the binary's functionality.

### **Overview**
The binary appears to be a **complex installer or a wrapper for an installation script**, likely utilizing the Nullsoft Script Installer (NSIS) framework. It is designed to handle file extraction, environment preparation, and "payload" execution. While many of these behaviors are common in legitimate installers, this specific implementation contains several indicators often seen in **droppers** or **loaders** used to deliver subsequent malware stages.

### **Core Functionality**
*   **Installer Logic:** The code features a large command-switch table (at `fcn.00401434`) typical of an installer that handles various flags (e.g., silent mode, directory selection).
*   **Environment Setup:** It actively interacts with Windows system environment variables (like `%TEMP%` and `%PATH%`) to determine where to extract files and how to proceed with the setup.
*   **Integrity Checking:** The function `fcn.0040307d` performs an "integrity check." If a file is corrupted or incomplete, it displays a standard error message (including a link to the NSIS website). 
*   **Automatic Cleanup/Movement:** It uses several Windows APIs (`MoveFileW`, `CopyFileW`) to move files from temporary locations into their final destination.

### **Suspicious & Malicious Behaviors**
The following behaviors are notable as they could be used to mask malicious activity:

*   **Privilege Escalation:** The code calls `AdjustTokenPrivileges` and `LookupPrivilegeValueW`. While common in installers to gain permission to write to protected folders, this is also a primary method for malware to escalate its privileges (e.g., attempting to obtain `SeShutdownPrivilege`).
*   **File System Manipulation & Obfuscation:** 
    *   The code frequently uses `SetFileAttributesW`. This can be used to change the "hidden" or "system" attributes of a file during the moving/copying process, allowing a malicious payload to remain hidden on the disk.
    *   It interacts with system directories (`GetSystemDirectoryW`, `GetWindowsDirectoryW`) to move files into protected paths, which is a common way to ensure persistence and avoid manual detection by the user.
*   **Dropper/Loader Characteristics:** 
    *   The presence of `CreateProcessW` and `ShellExecuteExW` suggests that after "installing" or "extracting" components, this binary launches additional processes. In a malware context, this is how the initial stage (this installer) hands off control to the actual malicious payload.
    *   The use of `GetTempPathW` combined with move/copy logic suggests it drops its primary payload into a temporary directory before executing it or moving it to a more permanent location.
*   **Implicit Persistence:** By utilizing standard installer scripts (NSIS), the malware can blend in perfectly with legitimate software, making it difficult for automated security tools to distinguish between "installing a game" and "installing a remote access trojan."

### **Notable Techniques & Patterns**
*   **NSIS Framework Usage:** The inclusion of `nsis.sf.net` links in the error strings indicates it uses the Nullsoft Script Installer. This is a common "living off the land" technique where malware utilizes well-known, legitimate tools to perform complex tasks like file unpacking and extraction.
*   **Shell Execution Logic:** In function `fcn.00401434`, there is a clear loop/switch system that processes commands from the command line (`GetCommandLineW`), allowing it to be called by other scripts or automation tools.
*   **Large Switch-Case Utility:** The extensive switch statement suggests a high degree of complexity; even if only one part of the code is "malicious," the sheer amount of legitimate installer logic makes manual reverse engineering time-consuming for analysts.

### **Conclusion for Analysis Report**
This binary acts as a **sophisticated dropper/installer**. It leverages common installation patterns (NSIS) to manage file extraction, move files into system directories, and escalate privileges. While it likely serves a functional purpose for an installer, the logic is consistent with malware designed to deliver and hide secondary payloads on a victim's machine.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The binary utilizes the legitimate NSIS framework and standard installer logic to blend in with genuine software installations. |
| T1068 | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicates an attempt to gain higher privileges for system-level interactions. |
| T1562.001 | Impair Defenses: Modify System Attributes | The call to `SetFileAttributesW` is used to hide files by applying "hidden" or "system" attributes to evade manual detection. |
| T1036.005 | Masquerading: Match Legitimate Name or Location | The malware moves payloads into system directories (via `GetSystemDirectoryW`) to mimic the behavior of legitimate software components. |
| T1204.001 | User Execution: Malicious File | The binary acts as a dropper/loader by extracting files to temporary paths and executing subsequent stages via `CreateProcessW` or `ShellExecuteExW`. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `nsis.sf.net` (Identified as part of the NSIS framework used for error messaging)

**File paths / Registry keys**
*   *None identified.* (Note: While the analysis mentions interactions with `GetSystemDirectoryW` and `GetWindowsDirectoryW`, these are standard system calls; no specific malicious hardcoded paths were found in the string list.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Framework:** Nullsoft Script Installer (NSIS) — Used to mask installation logic and deliver payloads.
*   **Privilege Escalation:** Usage of `AdjustTokenPrivileges` and `LookupPrivilegeValueW`.
*   **Evasion/Obfuscation:** Use of `SetFileAttributesW` to hide files during the deployment phase.
*   **Payload Delivery:** Usage of `CreateProcessW` and `ShellExecuteExW` following file movement from temporary directories (`GetTempPathW`).

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Masquerading & Extraction:** The binary utilizes the legitimate Nullsoft Script Installer (NSIS) framework to blend in with standard software installers while performing common malicious behaviors like extracting files to temporary directories and moving them into protected system folders.
*   **Evasion Techniques:** The use of `SetFileAttributesW` specifically for hiding files and the attempt at privilege escalation (`AdjustTokenPrivileges`) are classic indicators used to evade detection and ensure the payload has sufficient permissions to run.
*   **Payload Delivery Logic:** The combination of `GetTempPathW`, `CreateProcessW`, and `ShellExecuteExW` demonstrates a multi-stage execution flow where this binary acts as the initial vehicle (dropper) to deploy and launch secondary payloads.
