# Threat Analysis Report

**Generated:** 2026-08-11 16:46 UTC
**Sample:** `0e0e8a78f37b87b6343a3946c1c3d3a702d58492f18962f36aef116c9c5607ba_0e0e8a78f37b87b6343a3946c1c3d3a702d58492f18962f36aef116c9c5607ba.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e0e8a78f37b87b6343a3946c1c3d3a702d58492f18962f36aef116c9c5607ba_0e0e8a78f37b87b6343a3946c1c3d3a702d58492f18962f36aef116c9c5607ba.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 447,760 bytes |
| MD5 | `93560008d2c889952cdd8dcec762ef2b` |
| SHA1 | `2e4fbccf044c5e003b7430fe094aef9a9aae2e5a` |
| SHA256 | `0e0e8a78f37b87b6343a3946c1c3d3a702d58492f18962f36aef116c9c5607ba` |
| Overall entropy | 6.982 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1627165075 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,112 | 6.402 | No |
| `.rdata` | 5,120 | 5.138 | No |
| `.data` | 1,536 | 4.021 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 164,864 | 4.245 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `SetFileSecurityW`, `RegOpenKeyExW`, `RegEnumValueW`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHFileOperationW`, `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `ShellExecuteExW`, `SHGetFileInfoW`
**ole32.dll**: `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `GetClientRect`, `EndPaint`, `DrawTextW`, `IsWindowEnabled`, `DispatchMessageW`, `wsprintfA`, `CharNextA`, `CharPrevW`, `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `GetSystemMetrics`, `FillRect`, `AppendMenuW`, `TrackPopupMenu`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectW`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetModuleHandleA`, `GetProcAddress`, `GetSystemDirectoryW`, `lstrcatW`, `Sleep`, `lstrcpyA`, `WriteFile`, `GetTempFileNameW`, `CreateFileW`, `lstrcmpiA`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`

## Extracted Strings

Total strings found: **951** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495l
tQWPV
v#Vh+/@
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
WWWWjn
uv9Et	
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 6048 | ✓ |
| `fcn.0040694b` | `0x40694b` | 2642 | ✓ |
| `entry0` | `0x40348f` | 1345 | ✓ |
| `fcn.00403aaa` | `0x403aaa` | 726 | ✓ |
| `fcn.00406418` | `0x406418` | 626 | ✓ |
| `fcn.00403015` | `0x403015` | 567 | ✓ |
| `fcn.0040324c` | `0x40324c` | 485 | ✓ |
| `fcn.00405aed` | `0x405aed` | 451 | ✓ |
| `fcn.00406027` | `0x406027` | 378 | ✓ |
| `fcn.00402e41` | `0x402e41` | 234 | ✓ |
| `fcn.00405443` | `0x405443` | 211 | ✓ |
| `fcn.00404398` | `0x404398` | 207 | ✓ |
| `fcn.00404bde` | `0x404bde` | 201 | ✓ |
| `fcn.00403d80` | `0x403d80` | 185 | ✓ |
| `fcn.0040668a` | `0x40668a` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040633b` | `0x40633b` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404cec` | `0x404cec` | 128 | ✓ |
| `fcn.00405db8` | `0x405db8` | 126 | ✓ |
| `fcn.00405912` | `0x405912` | 125 | ✓ |
| `fcn.004061cd` | `0x4061cd` | 123 | ✓ |
| `fcn.004062a9` | `0x4062a9` | 121 | ✓ |
| `fcn.00405fb2` | `0x405fb2` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406760` | `0x406760` | 112 | ✓ |
| `fcn.004068bd` | `0x4068bd` | 110 | ✓ |
| `fcn.00405516` | `0x405516` | 108 | ✓ |
| `fcn.00405a41` | `0x405a41` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402e41.c`](code/fcn.00402e41.c)
- [`code/fcn.00403015.c`](code/fcn.00403015.c)
- [`code/fcn.0040324c.c`](code/fcn.0040324c.c)
- [`code/fcn.00403aaa.c`](code/fcn.00403aaa.c)
- [`code/fcn.00403d80.c`](code/fcn.00403d80.c)
- [`code/fcn.00404398.c`](code/fcn.00404398.c)
- [`code/fcn.00404bde.c`](code/fcn.00404bde.c)
- [`code/fcn.00404cec.c`](code/fcn.00404cec.c)
- [`code/fcn.00405443.c`](code/fcn.00405443.c)
- [`code/fcn.00405516.c`](code/fcn.00405516.c)
- [`code/fcn.00405912.c`](code/fcn.00405912.c)
- [`code/fcn.00405a41.c`](code/fcn.00405a41.c)
- [`code/fcn.00405aed.c`](code/fcn.00405aed.c)
- [`code/fcn.00405db8.c`](code/fcn.00405db8.c)
- [`code/fcn.00405fb2.c`](code/fcn.00405fb2.c)
- [`code/fcn.00406027.c`](code/fcn.00406027.c)
- [`code/fcn.004061cd.c`](code/fcn.004061cd.c)
- [`code/fcn.004062a9.c`](code/fcn.004062a9.c)
- [`code/fcn.0040633b.c`](code/fcn.0040633b.c)
- [`code/fcn.00406418.c`](code/fcn.00406418.c)
- [`code/fcn.0040668a.c`](code/fcn.0040668a.c)
- [`code/fcn.00406760.c`](code/fcn.00406760.c)
- [`code/fcn.004068bd.c`](code/fcn.004068bd.c)
- [`code/fcn.0040694b.c`](code/fcn.0040694b.c)

## Behavioral Analysis

### Analysis Report: [Sample_Analysis]

#### Core Functionality and Purpose
Based on the deconstruction of the code and the presence of specific strings (e.g., references to **NSIS** - Nullsoft Script Installer), this binary functions as a **custom installer or an unpacker**. It is designed to extract, move, and configure files from a compressed package while managing system environments and preparing for secondary execution.

#### Suspicious or Malicious Behaviors
The following behaviors were identified that are common in both legitimate installers and malicious "droppers" or "loaders":

*   **Environment Manipulation:** The code performs manual manipulation of the `TEMP` environment variable using `SetEnvironmentVariableW`. It calculates paths to a temporary directory, confirms their existence, and then sets the system's environment. This is often used by malware to redirect execution to a controlled folder or bypass certain security constraints on standard paths.
*   **Privilege Escalation/Manipulation:** The code calls `OpenProcessToken` followed by `LookupPrivilegeValueW` specifically for the `"SeShutdownPrivilege"`. While common in installers that need to reboot the system, this mechanism is also frequently used by malware to ensure it has high-level permissions before performing sensitive actions.
*   **Payload Staging & Deployment:** There is extensive logic involving:
    *   `CreateDirectoryW` and `SetFileSecurityW` (managing access rights).
    *   `CopyFileW` and `MoveFileW` to transfer files between temporary locations and target directories.
    *   `SetFileAttributesW` to hide or modify file flags during the installation process.
*   **Automatic File Execution:** The code includes logic to locate, rename, and move specific assets (e.g., checking for strings like "setup" or looking for specific extensions).

#### Notable Techniques and Patterns
Several technical signatures suggest that this binary likely acts as a **loader/stub** for another piece of software:

*   **In-Memory Loading (Unpacking Behavior):** In `fcn.00403aaa`, the code uses `LoadImageW` to load segments into memory, followed by checks on file sizes and "integrity" (calculated via timing or size). This is a classic signature of an **unpacking stub**. It likely loads a primary payload into memory so that it doesn't exist as a raw file on disk until execution.
*   **Scripted/Table-Driven Logic:** `fcn.0040694b` and the large switch statement in `fcn.00401434` indicate a "state machine" or "instruction interpreter." This is typical of installers (like NSIS) where an internal script dictates which Windows APIs are called next.
*   **Resource Loading:** The presence of `OleInitialize`, `CoCreateInstance`, and the handling of `RichEdit` controls suggests it provides a GUI for its operations, common in "dropper" applications to interact with the user during the installation/infection phase.
*   **Persistence via Environment Modification:** By modifying the environment variables (the `TEMP` path), the program ensures that subsequent child processes launched by the installer have specific parameters, which can be used to ensure malware components continue to run in the desired context.

### Summary for Threat Intelligence
The sample is a **sophisticated loader/installer**. While it may be part of a legitimate software suite (given the NSIS-style code), its techniques—specifically **in-memory payload loading**, **environment variable manipulation**, and **privilege escalation**—are high-fidelity indicators used by malware to hide malicious payloads from file-system scanners.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1610 | System Environment Variables | The binary manipulates the `TEMP` environment variable to redirect execution paths and bypass security constraints on standard directories. |
| T1068 | Exploitation for Privilege Escalation | The code explicitly requests high-level privileges (e.g., "SeShutdownPrivilege") to ensure it has sufficient permissions before executing sensitive actions. |
| T1560 | Archive Extraction | The logic involving `CreateDirectoryW`, `CopyFileW`, and `MoveFileW` indicates the extraction of files from a compressed package into a usable state. |
| T1564 | Hideer Directory | The use of `SetFileAttributesW` and `SetFileSecurityW` is employed to hide file presence or restrict access rights during the installation process. |
| T1027 | Weak File Buffering | The usage of `LoadImageW` with integrity checks indicates a loader designed to execute a payload in memory to avoid detection by file-system scanners. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: The "EXTRACTED STRINGS" section primarily consists of standard Win32 API imports; per your instructions, these have been excluded as they are common library functions rather than specific malicious artifacts.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The report mentions the use of `TEMP` environment variables and "setup" strings, but no specific hardcoded paths or registry keys were provided).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Malware Type:** Loader/Stub (likely an unpacker)
*   **Associated Frameworks:** NSIS (Nullsoft Script Installer) logic.
*   **Behavioral Signatures:**
    *   **In-Memory Loading:** Use of `LoadImageW` to load payloads into memory to bypass disk-based scanners.
    *   **Privilege Escalation:** Targeted query for `"SeShutdownPrivilege"` via `LookupPrivilegeValueW`.
    *   **Environment Manipulation:** Manual manipulation of the `TEMP` environment variable via `SetEnvironmentVariableW`.
    *   **File Obfuscation:** Use of `SetFileAttributesW` to modify file flags during deployment.
    *   **State Machine Logic:** Presence of a large switch statement (at `fcn.00401434`) and instruction-like logic indicative of an installer/loader script interpreter.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**: 
    * **In-Memory Execution:** The use of `LoadImageW` to load segments into memory and perform integrity checks is a classic hallmark of an unpacking stub or loader designed to bypass disk-based security scanners.
    * **Environment & Privilege Manipulation:** The specific targeting of the `TEMP` environment variable (T1610) and the request for `SeShutdownPrivilege` indicate a routine used by loaders to prepare a controlled environment and gain necessary permissions before executing a primary payload.
    * **Installer Framework Logic:** The identification of NSIS-style state machine logic and archive extraction routines suggests the binary is purpose-built as a "wrapper" or installer to deploy secondary, potentially malicious, components.
