# Threat Analysis Report

**Generated:** 2026-06-28 05:18 UTC
**Sample:** `025c8513b71051fa81c1e6f12bdae897b90aa74c75dda2d21304824f7320a47a_025c8513b71051fa81c1e6f12bdae897b90aa74c75dda2d21304824f7320a47a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `025c8513b71051fa81c1e6f12bdae897b90aa74c75dda2d21304824f7320a47a_025c8513b71051fa81c1e6f12bdae897b90aa74c75dda2d21304824f7320a47a.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 495,968 bytes |
| MD5 | `82b7abcee9beffe217a23d2d74ea821f` |
| SHA1 | `f33f09ef17d3f26059ff6b979359db76c7582637` |
| SHA256 | `025c8513b71051fa81c1e6f12bdae897b90aa74c75dda2d21304824f7320a47a` |
| Overall entropy | 7.961 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1632607007 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,624 | 6.417 | No |
| `.rdata` | 5,120 | 5.141 | No |
| `.data` | 1,536 | 4.111 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 46,592 | 7.809 | ⚠️ Yes |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `SetFileSecurityW`, `RegOpenKeyExW`, `RegEnumValueW`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHFileOperationW`, `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `ShellExecuteExW`, `SHGetFileInfoW`
**ole32.dll**: `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `GetClientRect`, `EndPaint`, `DrawTextW`, `IsWindowEnabled`, `DispatchMessageW`, `wsprintfA`, `CharNextA`, `CharPrevW`, `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `GetSystemMetrics`, `FillRect`, `AppendMenuW`, `TrackPopupMenu`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectW`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetModuleHandleA`, `GetProcAddress`, `GetSystemDirectoryW`, `lstrcatW`, `Sleep`, `lstrcpyA`, `WriteFile`, `GetTempFileNameW`, `lstrcmpiA`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `GetLastError`

## Extracted Strings

Total strings found: **1247** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQWPV
Instu`
softuW
NulluN	E
SVWj _3
tVj%SSS
f9=H7B
D$$+D$
D$,+D$$P
u9=87B
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 6152 | ✓ |
| `fcn.00406bb0` | `0x406bb0` | 2642 | ✓ |
| `entry0` | `0x403640` | 1509 | ✓ |
| `fcn.00403d17` | `0x403d17` | 726 | ✓ |
| `fcn.004030d0` | `0x4030d0` | 673 | ✓ |
| `fcn.004066a5` | `0x4066a5` | 586 | ✓ |
| `fcn.00405d74` | `0x405d74` | 451 | ✓ |
| `fcn.004062ae` | `0x4062ae` | 378 | ✓ |
| `fcn.00403479` | `0x403479` | 361 | ✓ |
| `fcn.00403371` | `0x403371` | 264 | ✓ |
| `fcn.00402ea9` | `0x402ea9` | 234 | ✓ |
| `fcn.004056ca` | `0x4056ca` | 211 | ✓ |
| `fcn.0040462b` | `0x40462b` | 207 | ✓ |
| `fcn.00404e71` | `0x404e71` | 201 | ✓ |
| `fcn.00403fed` | `0x403fed` | 185 | ✓ |
| `fcn.004068ef` | `0x4068ef` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040302e` | `0x40302e` | 162 | ✓ |
| `fcn.004065c8` | `0x4065c8` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00406454` | `0x406454` | 129 | ✓ |
| `fcn.00404f7f` | `0x404f7f` | 128 | ✓ |
| `fcn.0040603f` | `0x40603f` | 126 | ✓ |
| `fcn.00405b99` | `0x405b99` | 125 | ✓ |
| `fcn.00406536` | `0x406536` | 121 | ✓ |
| `fcn.00406239` | `0x406239` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004069c5` | `0x4069c5` | 112 | ✓ |
| `fcn.00406b22` | `0x406b22` | 110 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402ea9.c`](code/fcn.00402ea9.c)
- [`code/fcn.0040302e.c`](code/fcn.0040302e.c)
- [`code/fcn.004030d0.c`](code/fcn.004030d0.c)
- [`code/fcn.00403371.c`](code/fcn.00403371.c)
- [`code/fcn.00403479.c`](code/fcn.00403479.c)
- [`code/fcn.00403d17.c`](code/fcn.00403d17.c)
- [`code/fcn.00403fed.c`](code/fcn.00403fed.c)
- [`code/fcn.0040462b.c`](code/fcn.0040462b.c)
- [`code/fcn.00404e71.c`](code/fcn.00404e71.c)
- [`code/fcn.00404f7f.c`](code/fcn.00404f7f.c)
- [`code/fcn.004056ca.c`](code/fcn.004056ca.c)
- [`code/fcn.00405b99.c`](code/fcn.00405b99.c)
- [`code/fcn.00405d74.c`](code/fcn.00405d74.c)
- [`code/fcn.0040603f.c`](code/fcn.0040603f.c)
- [`code/fcn.00406239.c`](code/fcn.00406239.c)
- [`code/fcn.004062ae.c`](code/fcn.004062ae.c)
- [`code/fcn.00406454.c`](code/fcn.00406454.c)
- [`code/fcn.00406536.c`](code/fcn.00406536.c)
- [`code/fcn.004065c8.c`](code/fcn.004065c8.c)
- [`code/fcn.004066a5.c`](code/fcn.004066a5.c)
- [`code/fcn.004068ef.c`](code/fcn.004068ef.c)
- [`code/fcn.004069c5.c`](code/fcn.004069c5.c)
- [`code/fcn.00406b22.c`](code/fcn.00406b22.c)
- [`code/fcn.00406bb0.c`](code/fcn.00406bb0.c)

## Behavioral Analysis

### Analysis Summary
Based on the provided disassembly and strings, this binary functions as a **multi-stage installer or "packer/dropper."** It utilizes a logic engine common in installation frameworks (specifically resembling the **NSIS - Nullsoft Script Installer** structure) to unpack, move, and execute subsequent components of a program.

While it may be part of a legitimate installer, these same techniques are frequently employed by malware (such as trojans or droppers) to hide their true payload behind an "installer" wrapper.

---

### Core Functionality
*   **Installer Framework:** The large switch-case structure in `fcn.00401434` is indicative of a script interpreter. Instead of the logic being directly written in C, it interprets commands (likely from an embedded script) to handle UI elements, file system operations, and registry edits.
*   **Resource Management:** The code interacts heavily with `COMCTL32.dll`, `SHELL32.dll`, and `Ole32.dll` to render "standard" Windows dialogs and manage icons/images during a setup process.
*   **Path Resolution & Cleanup:** A significant amount of logic is dedicated to resolving relative paths into absolute ones, identifying "Special Folders," and cleaning up temporary files after they are no longer needed.

### Suspicious or Malicious Behaviors
The following behaviors are commonly associated with droppers or installers used in malware campaigns:

*   **Multi-Stage Execution (Dropper Behavior):** 
    *   The binary frequently uses `GetTempPathW` and `CopyFileW`. It creates a temporary file, copies data into it, and then executes/moves that file. This is a classic technique to drop a secondary payload (the actual malware) while keeping the first executable "clean."
    *   **Evidence:** In `fcn.00403d17` and `fcn.004030d0`, the code checks for installer integrity before proceeding, a common hurdle in multi-stage delivery.

*   **Persistence & Configuration:** 
    *   The extensive use of `RegOpenKeyExW`, `RegSetValueExW`, and `RegQueryValueExW` indicates that the binary modifies the Windows Registry to set up the environment or ensure the "installed" application persists across reboots.

*   **Privilege Escalation/Manipulation:**
    *   The inclusion of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` suggests the program attempts to gain elevated privileges (like `SeShutdownPrivilege`) or modify its security token, which is often necessary for malware to interact with system-level files.

*   **Evasive File Manipulation:**
    *   The code uses `SetFileSecurityW` and `MoveFileExW`. This can be used by malware to bypass certain file permissions or hide the actual malicious executable by renaming it several times during the "installation" process.

### Notable Techniques & Patterns
*   **NSIS Signature:** The string `NSIS_Error` and the specific logic in `fcn.004030d0` strongly suggest this is an NSIS-based installer. While a legitimate tool, it is frequently used by malware authors because it provides a ready-made way to handle extraction and installation of hidden payloads.
*   **Complex Path Resolution:** The function `fcn.004066a5` implements high-level path resolution (handling wildcards, special folders, etc.). This ensures that the installer can find its components regardless of where it is unpacked by a downloader.
*   **Dynamic Loading & API Obfuscation:** Use of `GetProcAddress`, `LoadLibraryExW`, and `GetModuleHandleW` suggests that some functions are resolved at runtime to avoid static detection by security software.
*   **Anti-Analysis / UI Manipulation:** The code checks for the presence of "UXTHEME" and manages window visibility (`ShowWindow`). This is often done to ensure a professional look but can also be used to hide windows or overlays from the user.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The binary uses a legitimate-looking NSIS installer wrapper and renames files during the installation process to hide its true intent and payload. |
| **T1547.001** | Registry Run Keys / Startup Folder | The use of `RegSetValueExW` indicates an attempt to modify registry keys to ensure the application persists across system reboots. |
| **T1068** | Exploitation for Privilege Escalation | The inclusion of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` suggests an intentional attempt to acquire higher-level privileges (e.g., `SeShutdownPrivilege`) to interact with the system. |
| **T1059** | Command and Scripting Interpreter | The analysis identifies a large switch-case structure acting as a script interpreter for processing NSIS commands to drive installation logic. |
| **T1204** | User Execution | The "Dropper" behavior of copying files to a temporary directory (`GetTempPathW`) before execution is a common method used to stage and execute secondary payloads. |
| **[Defense Evasion]** | Dynamic Loading / API Obfuscation | The use of `GetProcAddress` and `LoadLibraryExW` is specifically employed to resolve functions at runtime, helping the binary evade static analysis by security tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The provided text contains many Windows API calls and standard library references. These have been filtered out as they are common to both legitimate and malicious software and do not constitute unique IOCs for a specific threat actor.

### **IP addresses / URLs / Domains**
*   *None identified.* (The strings provided contain only internal logic, system constants, and API names.)

### **File paths / Registry keys**
*   *None explicitly listed.* 
    *   *Analyst Note:* While the behavioral analysis confirms that the binary performs registry modifications (`RegOpenKeyExW`, `RegSetValueExW`) and file moves/copies to temporary directories (`GetTempPathW`, `MoveFileExW`), no specific malicious keys (e.g., `HKLM\...\Malware`) or specific hardcoded paths were present in the provided text.

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Framework Identifier:** `NSIS` (Nullsoft Script Installer)
    *   **Reasoning:** The behavioral analysis identifies the string `NS1_Error` and specific logic patterns as characteristic of an NSIS-based installer. This is a key artifact for identifying the "wrapper" used to deliver the payload.
*   **Behavioral Signatures (TTPs):**
    *   **Dropper Behavior:** Use of `GetTempPathW` and `CopyFileW` to stage secondary payloads.
    *   **Privilege Escalation:** Execution of `AdjustTokenPrivileges` and `LookupPrivilegeValueW`.
    *   **Dynamic API Resolution:** Utilization of `GetProcAddress` and `LoadLibraryExW` (indicative of attempts to evade static analysis).

---
**Summary for SOC/Incident Response:**
While no high-fidelity network IOCs (IPs/Domains) were extracted, the binary is confirmed as a **multi-stage dropper**. Investigation should focus on identifying the specific file being dropped in the `Temp` directory and the specific registry keys modified during the "installation" phase.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1.  **Malware family:** Unknown
2.  **Malware type:** Dropper (Multi-stage)
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Multi-Stage Execution:** The binary utilizes `GetTempPathW`, `CopyFileW`, and `MoveFileExW` to extract, move, and execute secondary payloads from a temporary directory—a hallmark of dropper behavior designed to distance the initial "wrapper" from the actual malicious payload.
    *   **NSIS Wrapper & Evasion:** The use of an NSIS (Nullsoft Script Installer) framework provides a common method for masquerading as a legitimate installer while employing dynamic API loading (`GetProcAddress`, `LoadLibraryExW`) to evade static detection.
    *   **Persistence & Privilege Escalation:** The sample actively modifies registry keys (`RegSetValueExW`) for persistence and attempts to gain elevated privileges via `AdjustTokenPrivileges` to ensure it can perform system-level actions once the payload is delivered.
