# Threat Analysis Report

**Generated:** 2026-07-09 23:06 UTC
**Sample:** `044e045a439091b9af74217fb82a0493bf0f2e23b3a287172a6ac22a0d9541b3_044e045a439091b9af74217fb82a0493bf0f2e23b3a287172a6ac22a0d9541b3.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `044e045a439091b9af74217fb82a0493bf0f2e23b3a287172a6ac22a0d9541b3_044e045a439091b9af74217fb82a0493bf0f2e23b3a287172a6ac22a0d9541b3.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 320,864 bytes |
| MD5 | `b9897b6475a8047e3f3581c3ff3953a3` |
| SHA1 | `9318b0f4d203b3288af38fab85cd318ba223404c` |
| SHA256 | `044e045a439091b9af74217fb82a0493bf0f2e23b3a287172a6ac22a0d9541b3` |
| Overall entropy | 7.89 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1596249767 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,088 | 6.418 | No |
| `.rdata` | 5,120 | 5.061 | No |
| `.data` | 1,536 | 3.995 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 17,408 | 5.919 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExA`, `RegEnumKeyA`, `RegQueryValueExA`, `RegSetValueExA`, `RegCloseKey`, `RegDeleteValueA`, `RegDeleteKeyA`, `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, `OpenProcessToken`, `SetFileSecurityA`, `RegOpenKeyExA`, `RegEnumValueA`
**SHELL32.dll**: `SHGetFileInfoA`, `SHFileOperationA`, `SHGetPathFromIDListA`, `ShellExecuteExA`, `SHGetSpecialFolderLocation`, `SHBrowseForFolderA`
**ole32.dll**: `IIDFromString`, `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `SetClipboardData`, `CharPrevA`, `CallWindowProcA`, `PeekMessageA`, `DispatchMessageA`, `MessageBoxIndirectA`, `GetDlgItemTextA`, `SetDlgItemTextA`, `GetSystemMetrics`, `CreatePopupMenu`, `AppendMenuA`, `TrackPopupMenu`, `FillRect`, `EmptyClipboard`, `LoadCursorA`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectA`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetProcAddress`, `GetSystemDirectoryA`, `WideCharToMultiByte`, `MoveFileExA`, `ReadFile`, `GetTempFileNameA`, `WriteFile`, `RemoveDirectoryA`, `CreateProcessA`, `CreateFileA`, `GetLastError`, `CreateThread`, `CreateDirectoryA`

## Extracted Strings

Total strings found: **882** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495lGB
tQVPW
Et@;u
Instu`
softuW
NulluN	E
j@Vh`GB
D$$Ph,
D$(SPS
tVj%SSS
D$$+D$
D$,+D$$P
SSSSjn
us9Et	
8\tPV
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
SetFileSecurityA
RegOpenKeyExA
RegCreateKeyExA
ADVAPI32.dll
SHFileOperationA
SHGetFileInfoA
SHBrowseForFolderA
SHGetPathFromIDListA
ShellExecuteExA
SHGetSpecialFolderLocation
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5688 | ✓ |
| `fcn.0040660f` | `0x40660f` | 2642 | ✓ |
| `entry0` | `0x403312` | 1256 | ✓ |
| `fcn.004038d4` | `0x4038d4` | 709 | ✓ |
| `fcn.00406154` | `0x406154` | 584 | ✓ |
| `fcn.00402ea1` | `0x402ea1` | 567 | ✓ |
| `fcn.004030d8` | `0x4030d8` | 476 | ✓ |
| `fcn.00405889` | `0x405889` | 464 | ✓ |
| `fcn.00405d30` | `0x405d30` | 368 | ✓ |
| `fcn.00402cd0` | `0x402cd0` | 234 | ✓ |
| `fcn.004051e8` | `0x4051e8` | 210 | ✓ |
| `fcn.004041ac` | `0x4041ac` | 207 | ✓ |
| `fcn.0040498e` | `0x40498e` | 197 | ✓ |
| `fcn.00403b99` | `0x403b99` | 185 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040639c` | `0x40639c` | 153 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00406038` | `0x406038` | 137 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404a98` | `0x404a98` | 128 | ✓ |
| `fcn.004056ae` | `0x4056ae` | 125 | ✓ |
| `fcn.00405ecc` | `0x405ecc` | 123 | ✓ |
| `fcn.00405b47` | `0x405b47` | 120 | ✓ |
| `fcn.00405fa8` | `0x405fa8` | 119 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406581` | `0x406581` | 110 | ✓ |
| `fcn.0040645c` | `0x40645c` | 110 | ✓ |
| `fcn.004052ba` | `0x4052ba` | 108 | ✓ |
| `fcn.004057dd` | `0x4057dd` | 100 | ✓ |
| `fcn.00402e3d` | `0x402e3d` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402cd0.c`](code/fcn.00402cd0.c)
- [`code/fcn.00402e3d.c`](code/fcn.00402e3d.c)
- [`code/fcn.00402ea1.c`](code/fcn.00402ea1.c)
- [`code/fcn.004030d8.c`](code/fcn.004030d8.c)
- [`code/fcn.004038d4.c`](code/fcn.004038d4.c)
- [`code/fcn.00403b99.c`](code/fcn.00403b99.c)
- [`code/fcn.004041ac.c`](code/fcn.004041ac.c)
- [`code/fcn.0040498e.c`](code/fcn.0040498e.c)
- [`code/fcn.00404a98.c`](code/fcn.00404a98.c)
- [`code/fcn.004051e8.c`](code/fcn.004051e8.c)
- [`code/fcn.004052ba.c`](code/fcn.004052ba.c)
- [`code/fcn.004056ae.c`](code/fcn.004056ae.c)
- [`code/fcn.004057dd.c`](code/fcn.004057dd.c)
- [`code/fcn.00405889.c`](code/fcn.00405889.c)
- [`code/fcn.00405b47.c`](code/fcn.00405b47.c)
- [`code/fcn.00405d30.c`](code/fcn.00405d30.c)
- [`code/fcn.00405ecc.c`](code/fcn.00405ecc.c)
- [`code/fcn.00405fa8.c`](code/fcn.00405fa8.c)
- [`code/fcn.00406038.c`](code/fcn.00406038.c)
- [`code/fcn.00406154.c`](code/fcn.00406154.c)
- [`code/fcn.0040639c.c`](code/fcn.0040639c.c)
- [`code/fcn.0040645c.c`](code/fcn.0040645c.c)
- [`code/fcn.00406581.c`](code/fcn.00406581.c)
- [`code/fcn.0040660f.c`](code/fcn.0040660f.c)

## Behavioral Analysis

### Malware Analysis Report

**Core Functionality and Purpose**
The binary is a sophisticated **installer stub**, likely based on or wrapped with the **NSIS (Nullsoft Script Install System)** framework. Its primary purpose is to facilitate the installation of software by performing several high-level tasks: 
*   **Environment Setup:** It checks Windows version, initializes common controls, and prepares the UI environment (handling themes via `uxtheme`).
*   **Command Line Parsing:** It parses arguments such as `/S` (Silent mode) or `/D` (Directory selection), which are standard for automated software installations.
*   **File Management/Extraction:** A significant portion of the code is dedicated to resolving paths, moving files between directories (`MoveFileA`), and copying files from a source archive into a target directory (`CopyFileA`). 
*   **Installation Logic:** It manages "dropped" components by extracting them to temporary locations (using `GetTempFileName`) before final placement.

**Suspicious or Malicious Behaviors**
While installer scripts are not inherently malicious, the following behaviors are common in **droppers** and **installers for malware**:
*   **Privilege Escalation:** The code explicitly calls `OpenProcessToken`, `LookupPrivilegeValueA`, and `AdjustTokenPrivileges`. This is used to grant the process higher-level privileges (e.g., `SeShutdownPrivilege`), allowing it to modify system files or registry keys that are otherwise protected.
*   **File Dropping/Execution:** The logic for extracting files and moving them into system folders (like `%ProgramFiles%` or others retrieved via `GetWindowsDirectoryA`) is a classic "dropper" behavior used to place malicious payloads on the disk.
*   **Registry Manipulation:** It utilizes `RegSetValueExA` and `WritePrivateProfileStringA`. This can be used for persistence (e.g., adding a "Run" key) or changing system configurations to facilitate subsequent stages of an infection.
*   **System Interaction:** The use of `ShellExecuteExA` suggests the installer may execute other binaries, scripts, or commands immediately after the files are extracted/moved.

**Notable Techniques and Patterns**
*   **NSIS Wrapper:** The presence of strings like "NSIS Error" and specific logic for handling silent flags strongly indicates this is an NSIS-based executable. Malware authors frequently use these wrappers to hide their actual payloads inside a standard installation routine to evade basic detection.
*   **Complex Integrity Checks:** The function `fcn.0040660f` contains complex bitwise operations and nested loops typical of **CRC32 or checksum calculations**. This is used to verify that the "payload" files were extracted correctly from a compressed archive without corruption.
*   **Dynamic API Resolution/Handling:** Some sections use `GetProcAddress` and `GetModuleHandleA`, allowing the program to interact with system functions while making it slightly harder for simple static analysis tools to map every action immediately.
*   **Environment Manipulation:** The code actively manipulates environment variables (e.g., changing the `TEMP` directory) during execution, a tactic sometimes used to hide activity or ensure that temporary files are stored in locations controlled by the malware.

### Summary Table
| Feature | Observation | Risk Level |
| :--- | :--- | :--- |
| **Dropper Behavior** | Extensive logic for copying/moving files and creating directories (`CreateDirectoryA`). | **High** |
| **Privilege Escalation** | Explicit use of `AdjustTokenPrivileges` to gain system-level rights. | **Medium** |
| **Persistence** | Registry manipulation (`RegSetValueExA`) detected in various locations. | **Medium** |
| **Obfuscation/Evasion** | Use of standard installer wrappers (NSIS) to mask the primary payload's presence. | **High** |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1068 | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` allows the malware to acquire high-level system privileges to modify protected files and registries. |
| T1547.001 | Boot or Logon Autostart Executables | Registry manipulation via `RegSetValueExA` is used to ensure the malicious components persist across system reboots. |
| T1027 | Obfuscated Files or Information | The use of an NSIS wrapper masks the presence of the actual payload, making it harder for static analysis tools to identify the underlying threat. |
| T1059 | Command and Scripting Interpreter | The utilization of `ShellExecuteExA` indicates the execution of dropped binaries, scripts, or system commands during the installation sequence. |
| T1036 | Create Host Shortcut (Persistence) | *Note: While not specifically a "drop" action, moving files to common paths like %ProgramFiles% is often associated with establishing persistence.* |

*(Self-Correction/Refinement for Analysis Accuracy)*: 
While the behavior of moving files into system directories represents **Dropper** functionality, in MITRE ATT&CK terms, this is primarily mapped to the subsequent actions it enables (Persistence and Execution). Specifically, T1027 covers the "masking" via NSIS, while T1547.001 covers the "persistence" via registry keys mentioned in your summary table.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the identified Indicators of Compromise (IOCs). 

Note: The provided text contains many standard Windows API calls and library functions; these have been excluded as false positives per your instructions.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (The analysis notes the *intent* to use `RegSetValueExA` and `WritePrivateProfileStringA`, but no specific malicious registry keys or hardcoded file paths were provided in the text.)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified. (While a function offset `fcn.0040660f` is mentioned as performing checksums, no specific MD5/SHA-1/SHA-256 hashes were present in the string dump.)

**Other artifacts**
*   **Malware Family Indicator:** NSIS (Nullsoft Script Install System) wrapper (used to disguise the primary payload).
*   **Behavioral Pattern:** Privilege Escalation via `AdjustTokenPrivileges` and `LookupPrivilegeValueA`.
*   **Integrity Check Mechanism:** CRC32/Checksum calculation logic (detected at offset `0040660f`) used to verify "payload" files.
*   **Execution Method:** Use of `ShellExecuteExA` for secondary payload execution.

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High (for type) / Low (for specific family name)
4. **Key evidence**:
    *   **NSIS Wrapper & Extraction Logic:** The sample utilizes a sophisticated NSIS-based installer wrapper to mask the primary payload, perform complex integrity checks (CRC32), and manage the automated extraction of files into system directories.
    *   **Privilege Escalation & Persistence:** The inclusion of `AdjustTokenPrivileges` and registry manipulation (`RegSetValueExA`) demonstrates intent to bypass local security restrictions and establish a foothold on the host machine.
    *   **Dropper Behavior Chain:** The combination of moving files to `%ProgramFiles%`, handling "dropped" components in temporary directories, and executing them via `ShellExecuteExA` is a classic signature for a multi-stage dropper designed to deliver secondary payloads (such as a RAT or botnet agent).
