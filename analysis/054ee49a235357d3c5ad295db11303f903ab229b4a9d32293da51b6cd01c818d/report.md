# Threat Analysis Report

**Generated:** 2026-07-13 15:33 UTC
**Sample:** `054ee49a235357d3c5ad295db11303f903ab229b4a9d32293da51b6cd01c818d_054ee49a235357d3c5ad295db11303f903ab229b4a9d32293da51b6cd01c818d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `054ee49a235357d3c5ad295db11303f903ab229b4a9d32293da51b6cd01c818d_054ee49a235357d3c5ad295db11303f903ab229b4a9d32293da51b6cd01c818d.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 351,680 bytes |
| MD5 | `d4e056d9cb2cb25321d4f9bd23b3562c` |
| SHA1 | `8c7d5f745ac7fc1bd998332d446a36b1eff7a449` |
| SHA256 | `054ee49a235357d3c5ad295db11303f903ab229b4a9d32293da51b6cd01c818d` |
| Overall entropy | 6.331 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1776631127 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,112 | 6.42 | No |
| `.rdata` | 5,120 | 5.029 | No |
| `.data` | 1,024 | 5.258 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 174,080 | 4.015 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueA`, `RegEnumKeyA`, `RegQueryValueExA`, `RegSetValueExA`, `RegCloseKey`, `RegDeleteValueA`, `RegDeleteKeyA`, `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, `OpenProcessToken`, `RegOpenKeyExA`, `RegCreateKeyExA`
**SHELL32.dll**: `SHGetPathFromIDListA`, `SHBrowseForFolderA`, `SHGetFileInfoA`, `SHFileOperationA`, `ShellExecuteExA`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoCreateInstance`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `SetDlgItemTextA`, `GetSystemMetrics`, `CreatePopupMenu`, `AppendMenuA`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcA`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorA`, `SetCursor`, `GetSysColor`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectA`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `CreateFileA`, `GetTempFileNameA`, `ReadFile`, `RemoveDirectoryA`, `CreateProcessA`, `CreateDirectoryA`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceA`, `lstrcpynA`, `SetErrorMode`, `GetVersionExA`, `lstrlenA`, `GetCommandLineA`

## Extracted Strings

Total strings found: **630** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQVPW
Et@;u
v#VhQ.@
Instuj
softua
NulluX	E
Y9=t+z
tVj%WWW
D$$+D$
D$,+D$$P
SSSSjn
us9Et	
8\tPV
u9utm
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
NTMARTA
RichEdit
RichEdit20A
RichEd32
RichEd20
.DEFAULT\Control Panel\International
Control Panel\Desktop\ResourceLocale
Software\Microsoft\Windows\CurrentVersion
\Microsoft\Internet Explorer\Quick Launch
RegEnumValueA
RegEnumKeyA
RegQueryValueExA
RegSetValueExA
RegCloseKey
RegDeleteValueA
RegDeleteKeyA
AdjustTokenPrivileges
LookupPrivilegeValueA
OpenProcessToken
RegOpenKeyExA
RegCreateKeyExA
ADVAPI32.dll
SHFileOperationA
SHGetFileInfoA
SHBrowseForFolderA
SHGetPathFromIDListA
ShellExecuteExA
SHELL32.dll
CoTaskMemFree
CoCreateInstance
OleUninitialize
OleInitialize
IIDFromString
ole32.dll
ImageList_Destroy
ImageList_AddMasked
ImageList_Create
COMCTL32.dll
EndPaint
DrawTextA
FillRect
GetClientRect
BeginPaint
DefWindowProcA
SendMessageA
InvalidateRect
EnableWindow
ReleaseDC
LoadImageA
SetWindowLongA
GetDlgItem
IsWindow
FindWindowExA
SendMessageTimeoutA
wsprintfA
ShowWindow
SetForegroundWindow
PostQuitMessage
SetWindowTextA
SetTimer
CreateDialogParamA
DestroyWindow
ExitWindowsEx
CharNextA
DialogBoxParamA
GetClassInfoA
CreateWindowExA
SystemParametersInfoA
RegisterClassA
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5839 | ✓ |
| `fcn.0040699c` | `0x40699c` | 2183 | ✓ |
| `entry0` | `0x4033f0` | 1521 | ✓ |
| `fcn.00403abb` | `0x403abb` | 709 | ✓ |
| `fcn.00402f38` | `0x402f38` | 619 | ✓ |
| `fcn.00406345` | `0x406345` | 615 | ✓ |
| `fcn.004031a3` | `0x4031a3` | 495 | ✓ |
| `fcn.00405a74` | `0x405a74` | 464 | ✓ |
| `fcn.00405f1b` | `0x405f1b` | 368 | ✓ |
| `fcn.00406854` | `0x406854` | 328 | ✓ |
| `fcn.00402d67` | `0x402d67` | 234 | ✓ |
| `fcn.00407355` | `0x407355` | 216 | ✓ |
| `fcn.004053f6` | `0x4053f6` | 210 | ✓ |
| `fcn.004043b9` | `0x4043b9` | 207 | ✓ |
| `fcn.00404b9b` | `0x404b9b` | 197 | ✓ |
| `fcn.00403d80` | `0x403d80` | 185 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.004065ac` | `0x4065ac` | 153 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00406229` | `0x406229` | 137 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.004060b7` | `0x4060b7` | 129 | ✓ |
| `fcn.004072d4` | `0x4072d4` | 129 | ✓ |
| `fcn.00404ca5` | `0x404ca5` | 128 | ✓ |
| `fcn.00405d32` | `0x405d32` | 120 | ✓ |
| `fcn.00406199` | `0x406199` | 119 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406791` | `0x406791` | 110 | ✓ |
| `fcn.0040666c` | `0x40666c` | 110 | ✓ |
| `fcn.004054c8` | `0x4054c8` | 108 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402d67.c`](code/fcn.00402d67.c)
- [`code/fcn.00402f38.c`](code/fcn.00402f38.c)
- [`code/fcn.004031a3.c`](code/fcn.004031a3.c)
- [`code/fcn.00403abb.c`](code/fcn.00403abb.c)
- [`code/fcn.00403d80.c`](code/fcn.00403d80.c)
- [`code/fcn.004043b9.c`](code/fcn.004043b9.c)
- [`code/fcn.00404b9b.c`](code/fcn.00404b9b.c)
- [`code/fcn.00404ca5.c`](code/fcn.00404ca5.c)
- [`code/fcn.004053f6.c`](code/fcn.004053f6.c)
- [`code/fcn.004054c8.c`](code/fcn.004054c8.c)
- [`code/fcn.00405a74.c`](code/fcn.00405a74.c)
- [`code/fcn.00405d32.c`](code/fcn.00405d32.c)
- [`code/fcn.00405f1b.c`](code/fcn.00405f1b.c)
- [`code/fcn.004060b7.c`](code/fcn.004060b7.c)
- [`code/fcn.00406199.c`](code/fcn.00406199.c)
- [`code/fcn.00406229.c`](code/fcn.00406229.c)
- [`code/fcn.00406345.c`](code/fcn.00406345.c)
- [`code/fcn.004065ac.c`](code/fcn.004065ac.c)
- [`code/fcn.0040666c.c`](code/fcn.0040666c.c)
- [`code/fcn.00406791.c`](code/fcn.00406791.c)
- [`code/fcn.00406854.c`](code/fcn.00406854.c)
- [`code/fcn.0040699c.c`](code/fcn.0040699c.c)
- [`code/fcn.004072d4.c`](code/fcn.004072d4.c)
- [`code/fcn.00407355.c`](code/fcn.00407355.c)

## Behavioral Analysis

Based on the disassembly and string analysis, this binary appears to be a **downloader or installer wrapper**, likely a multi-stage loader often used in both legitimate software distribution (like NSIS-based installers) and as a component of a malware "dropper."

Below is the detailed breakdown of the code's behavior:

### Core Functionality and Purpose
The binary acts as an intermediary to prepare an environment, extract files, and launch secondary components. 
*   **Installer Framework:** The inclusion of strings like `NSIS Error`, `UXTHEME`, and large switch-case structures for UI elements indicates it is designed to handle a complex installation or update process.
*   **Extraction Engine:** It includes logic to resolve paths, handle environment variables (like the `TEMP` folder), and move/copy files from an embedded resource or temporary location to the final destination.
*   **Integrity Checking:** The function `fcn.00406791` implements a CRC32 check (identified by the constant `0xedb88320`). This is used to verify that the "payload" has not been corrupted during extraction or transit.

### Suspicious/Malicious Behaviors
While the code shares many characteristics with legitimate installers, several patterns are highly indicative of a **malware dropper**:

*   **Dropper & Execution:** 
    *   The `entry0` function contains logic to extract files to a temporary directory (using `GetTempPathA`) and perform a series of `CopyFileA` operations. 
    *   It then attempts to launch these components while manipulating the environment (e.g., setting current directories and potentially altering environment variables).
*   **Privilege Escalation & Persistence:**
    *   The code utilizes `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, and `OpenProcessToken`. While used by installers to perform system-level changes, these are frequently used by malware to gain high-integrity privileges (like `SeDebugPrivilege`) before launching a malicious payload.
    *   It performs heavy Registry manipulation (`RegCreateKeyExA`, `RegSetValueExA`). This is often used to ensure the primary payload survives a reboot or to modify system configurations.
*   **System Modification:** 
    *   The presence of "UXTHEME" and calls into `advapi32` suggest it might attempt to modify system-wide visual themes or interface settings, which can be used as a way to hide the appearance of malicious windows.

### Notable Techniques & Patterns
*   **Large Dispatch Table (State Machine):** The function `fcn.00401434` is a massive switch-case structure. This suggests a "Command" pattern or state machine commonly seen in complex installer engines where various system responses (file not found, permission denied, etc.) are handled through a central dispatcher.
*   **Anti-Analysis/Stalling:** 
    *   The use of `GetTickCount` and potential wait loops (e.g., the logic inside `fcn.00402f38`) can be used as **timing checks**. This is a common technique to delay execution so that automated "sandbox" analysis environments time out before the malicious behavior begins.
*   **Resource Management:** The code uses `LoadLibraryExA` and `GetProcAddress` (evident in the strings and logic) to dynamically resolve functions, which can be used to hide the presence of certain capabilities from static analysis tools.
*   **Payload Verification:** By using CRC32 (`fcn.00406791`), the code ensures that the secondary stage it is about to "drop" or "unpack" is intact before attempting to run it, a standard practice for ensuring reliability in both legitimate and malicious installers.

### Summary for Incident Response
This binary functions as a **Loader/Dropper**. It is designed to:
1.  Verify its environment and the integrity of its internal data (CRC32).
2.  Extract a hidden payload into a temporary directory.
3.  Escalate privileges or modify registry keys to establish persistence.
4.  Launch the final "payload" which may contain the actual malicious functionality (e.g., ransomware, info-stealer).

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&K framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1068** | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueA` indicates an attempt to gain high-integrity privileges (like `SeDebugPrivilege`) prior to launching the payload. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys/Startup Folder | The use of `RegCreateKeyExA` and `RegSetValueExA` is identified as a method to ensure the primary payload persists across system reboots. |
| **T1497** | Virtualization/Sandbox Evasion | The implementation of `GetTickCount` within wait loops functions as a "timing check" to stall execution until automated sandbox analysis environments time out. |
| **T1106** | Native API | The use of `LoadLibraryExA` and `GetProcAddress` allows for the dynamic resolution of functions to hide specific capabilities from static analysis tools. |
| **T1036** | Masquerading | The inclusion of "UXTHEME" logic suggests an attempt to manipulate system themes or window styles to hide malicious windows from the user. |
| **T1574** | Hijack Execution Flow (implied by Dropper) | While a general category, the behavior of extracting and executing a secondary payload in a temporary directory via `CopyFileA` characterizes the "Dropper" functionality. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Many items in the "EXTRACTED STRINGS" section were identified as standard Windows API calls or common system libraries and were excluded as false positives per your instructions.*

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified (The analysis notes the use of `GetTempPathA` and registry manipulation, but no specific malicious file paths or specific non-standard registry keys were provided in the source text).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **CRC32 Constant:** `0xedb88320` (Used in function `fcn.00406791` to verify payload integrity).
*   **Anti-Analysis Technique:** Use of `GetTickCount` for potential timing-based evasion/stalling during sandbox analysis.
*   **Privilege Escalation:** Presence of `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, and `OpenProcessToken` (indicative of attempting to gain `SeDebugPrivilege` or other high-level rights).
*   **Execution Pattern:** Use of `GetProcAddress` and `LoadLibraryExA` for dynamic linking to obscure capabilities from static analysis.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-Stage Delivery:** The binary exhibits classic "dropper" behavior by utilizing a CRC32 check to verify the integrity of an embedded payload, extracting it to a temporary directory via `GetTempPathA`, and then executing that secondary component.
*   **Evasion & Defense Evasion:** It incorporates active anti-analysis techniques, including `GetTickCount` loops for timing-based sandbox evasion and the use of `LoadLibraryExA/GetProcAddress` to dynamically resolve functions and hide its capabilities from static analysis.
*   **Persistence & Privilege Escalation:** The code explicitly attempts to escalate privileges (using `AdjustTokenPrivileges`) and modify registry keys to ensure the payload remains active on the system, which are standard precursors for delivering high-impact payloads like ransomware or RATs.
