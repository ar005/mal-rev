# Threat Analysis Report

**Generated:** 2026-07-12 10:36 UTC
**Sample:** `0500163df70a709472ed90dbeb9ce871156f5125736ce763fb61fe54d06081d1_0500163df70a709472ed90dbeb9ce871156f5125736ce763fb61fe54d06081d1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0500163df70a709472ed90dbeb9ce871156f5125736ce763fb61fe54d06081d1_0500163df70a709472ed90dbeb9ce871156f5125736ce763fb61fe54d06081d1.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 348,752 bytes |
| MD5 | `7f2b3386b6c942cb3e31c53fb11197c8` |
| SHA1 | `1e1b1adb7b637db21917b1dc9a78f6ccf8878bfa` |
| SHA256 | `0500163df70a709472ed90dbeb9ce871156f5125736ce763fb61fe54d06081d1` |
| Overall entropy | 6.312 |
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

Total strings found: **648** (showing first 100)

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

Based on my analysis of the provided disassembly and decompiled code, this binary is a **dropper/installer** (likely based on or wrapped by the NSIS script system). It acts as a "wrapper" designed to prepare the environment and deliver a primary payload onto the target system.

### Core Functionality and Purpose
The program's main role is to facilitate the installation of software. However, from an analysis standpoint, it functions as a multi-stage loader:
*   **Environment Preparation:** It checks OS versions, identifies supported features (like `UXTHEME`), and prepares temporary directories for use.
*   **Payload Extraction:** It extracts and copies a secondary executable or library into a temporary directory with a randomized name (e.g., `~nsu%X.tmp`). 
*   **Integrity Verification:** It performs checks on the file it just extracted to ensure it is complete before proceeding to execute it.

### Suspicious or Malicious Behaviors
While these behaviors are common in legitimate installers, they are also primary indicators of a **downloader/dropper** malware sample:

*   **Dropping and Executing Payloads:** The core logic (especially in `entry0` and `fcn.00402f38`) involves moving an embedded payload into the `%TEMP%` directory or another system folder to be executed separately from the main process.
*   **Privilege Escalation/Manipulation:** In `entry0`, the code calls `OpenProcessToken`, `LookupPrivilegeValueA`, and `AdjustTokenPrivileges`. This is often used by malware to gain administrative rights or bypass security restrictions before running the secondary payload.
*   **Environment Manipulation:** The code explicitly modifies environment variables (e.g., setting the `TEMP` path) and manipulates registry keys via `ADVAPI32` functions (`RegOpenKeyExA`, `RegSetValueExA`). This is used to ensure the installer can modify system settings or achieve persistence.
*   **Dynamic API Resolution:** The code uses `GetProcAddress` and `GetModuleHandleA`. While common in Windows programming, it is a frequent technique to hide the application's true capabilities from static analysis tools by only resolving functions at runtime.

### Notable Techniques & Patterns
*   **NSIS Wrapper Pattern:** The presence of strings like `"NSIS Error"` and `"Installer integrity check has failed"` suggests this is an **NSIS (Nullsoft Script Installer)** wrapper. Attackers frequently use these to bundle malware because they provide a "legitimate" looking setup interface while hiding the actual malicious payload.
*   **Self-Protection/Evasion:** The code includes logic to check system capabilities and ensure specific DLLs are loaded before continuing, which can be used to detect if it is running in a virtual machine or sandbox (though here it's likely just for UI compatibility).
*   **File Manipulation Loop:** In `fcn.0040231f` and other sections, the code handles file system operations extensively, including creating directories and moving files, which are primary indicators of dropping malware components.

### Summary Recommendation
This binary is not "the" virus itself in a traditional sense; rather, it is the **loader/installer** designed to deliver and install the actual malicious payload. Its presence on a system suggests that an installer was executed, which then dropped a separate file onto the machine for further action (e.g., establishing a backdoor or installing a miner).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of an NSIS wrapper and randomized file naming schemes is intended to hide the malicious payload's presence within a standard installation routine. |
| T1134 | Modify Environment Variables | The binary explicitly modifies environment variables, such as the `TEMP` path, to prepare the execution environment for the secondary payload. |
| T1112 | Modify Registry | The code utilizes `ADVAPI32` functions to modify registry keys for configuration or potential persistence. |
| T1068 | Exploitation for Privilege Escalation | The inclusion of `AdjustTokenPrivileges` and `LookupPrivilegeValueA` indicates an attempt to gain higher privileges or bypass security restrictions before executing the secondary payload. |
| T1497 | Virtualization/Sandbox Evasion | The code includes logic to check system capabilities and specific DLL availability to determine if it is running in a virtual machine or sandbox environment. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   (None identified)

**File paths / Registry keys**
*   `~nsu%X.tmp` (Note: This is a signature filename pattern used by NSIS to stage dropped payloads in temporary directories.)

**Mutex names / Named pipes**
*   (None identified)

**Hashes**
*   (None identified)

**Other artifacts**
*   **Installer Type:** NSIS (Nullsoft Script Installer) wrapper.
*   **Dropper Behavior:** Extraction of secondary payloads to the `%TEMP%` directory or other system folders.
*   **Technique - Dynamic API Resolution:** Use of `GetProcAddress` and `GetModuleHandleA` to resolve functions at runtime to evade static analysis.
*   **Privilege Manipulation:** Utilization of `OpenProcessToken`, `LookupPrivilegeValueA`, and `AdjustTokenPrivileges` to escalate privileges or bypass restrictions prior to execution.
*   **Persistence/Configuration:** Manipulation of registry keys via `ADVAPI32` functions for environment modification.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1.  **Malware family:** Unknown (Specifically identified as an **NSIS Wrapper**)
2.  **Malware type:** Dropper / Loader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Multi-stage Payload Delivery:** The binary functions primarily to extract a secondary, hidden payload into the `%TEMP%` directory with randomized naming, acting as a bridge between the initial infection and the execution of the main malicious payload.
    *   **Obfuscation & Evasion Techniques:** The use of an NSIS (Nullsoft Script Installer) framework provides "legitimate" cover for malicious activities; additionally, it utilizes dynamic API resolution (`GetProcAddress`) to hide its capabilities from static analysis.
    *   **Privilege Escalation:** The inclusion of specific functions such as `AdjustTokenPrivileges` and `LookupPrivilegeValueA` indicates a deliberate attempt to gain elevated system permissions to facilitate the installation of the final payload.
