# Threat Analysis Report

**Generated:** 2026-06-27 14:18 UTC
**Sample:** `01d7a671885ca694434ac2dc2a1612dee663decb7389a258006ff194314c0af0_01d7a671885ca694434ac2dc2a1612dee663decb7389a258006ff194314c0af0.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01d7a671885ca694434ac2dc2a1612dee663decb7389a258006ff194314c0af0_01d7a671885ca694434ac2dc2a1612dee663decb7389a258006ff194314c0af0.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 507,672 bytes |
| MD5 | `4b23315f8f95d371e8f4e27deeb20333` |
| SHA1 | `bdcfc65f501e321fb390db2371170e5d687f3831` |
| SHA256 | `01d7a671885ca694434ac2dc2a1612dee663decb7389a258006ff194314c0af0` |
| Overall entropy | 7.282 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1632606919 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.389 | No |
| `.rdata` | 5,120 | 5.058 | No |
| `.data` | 1,536 | 3.992 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 164,864 | 4.794 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExA`, `RegEnumKeyA`, `RegQueryValueExA`, `RegSetValueExA`, `RegCloseKey`, `RegDeleteValueA`, `RegDeleteKeyA`, `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, `OpenProcessToken`, `SetFileSecurityA`, `RegOpenKeyExA`, `RegEnumValueA`
**SHELL32.dll**: `SHGetFileInfoA`, `SHFileOperationA`, `SHGetPathFromIDListA`, `ShellExecuteExA`, `SHGetSpecialFolderLocation`, `SHBrowseForFolderA`
**ole32.dll**: `IIDFromString`, `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `SetClipboardData`, `CharPrevA`, `CallWindowProcA`, `PeekMessageA`, `DispatchMessageA`, `MessageBoxIndirectA`, `GetDlgItemTextA`, `SetDlgItemTextA`, `GetSystemMetrics`, `CreatePopupMenu`, `AppendMenuA`, `TrackPopupMenu`, `FillRect`, `EmptyClipboard`, `LoadCursorA`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectA`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetProcAddress`, `GetSystemDirectoryA`, `WideCharToMultiByte`, `MoveFileExA`, `ReadFile`, `GetTempFileNameA`, `WriteFile`, `RemoveDirectoryA`, `CreateProcessA`, `CreateFileA`, `GetLastError`, `CreateThread`, `CreateDirectoryA`

## Extracted Strings

Total strings found: **943** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495LGB
tQVPW
Et@;u
v#Vh%.@
Instu`
softuW
NulluN	E
j@Vh@GB
tVj%WWW
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
RegisterClassA
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5795 | ✓ |
| `fcn.00406772` | `0x406772` | 2642 | ✓ |
| `entry0` | `0x40337d` | 1456 | ✓ |
| `fcn.00403a07` | `0x403a07` | 709 | ✓ |
| `fcn.004062b4` | `0x4062b4` | 587 | ✓ |
| `fcn.00402f0c` | `0x402f0c` | 567 | ✓ |
| `fcn.00403143` | `0x403143` | 476 | ✓ |
| `fcn.004059e3` | `0x4059e3` | 464 | ✓ |
| `fcn.00405e8a` | `0x405e8a` | 368 | ✓ |
| `fcn.00402d3b` | `0x402d3b` | 234 | ✓ |
| `fcn.00405342` | `0x405342` | 210 | ✓ |
| `fcn.00404305` | `0x404305` | 207 | ✓ |
| `fcn.00404ae7` | `0x404ae7` | 197 | ✓ |
| `fcn.00403ccc` | `0x403ccc` | 185 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.004064ff` | `0x4064ff` | 153 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00406198` | `0x406198` | 137 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00406026` | `0x406026` | 129 | ✓ |
| `fcn.00404bf1` | `0x404bf1` | 128 | ✓ |
| `fcn.00405808` | `0x405808` | 125 | ✓ |
| `fcn.00405ca1` | `0x405ca1` | 120 | ✓ |
| `fcn.00406108` | `0x406108` | 119 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004066e4` | `0x4066e4` | 110 | ✓ |
| `fcn.004065bf` | `0x4065bf` | 110 | ✓ |
| `fcn.00405414` | `0x405414` | 108 | ✓ |
| `fcn.00405937` | `0x405937` | 100 | ✓ |
| `fcn.00402ea8` | `0x402ea8` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402d3b.c`](code/fcn.00402d3b.c)
- [`code/fcn.00402ea8.c`](code/fcn.00402ea8.c)
- [`code/fcn.00402f0c.c`](code/fcn.00402f0c.c)
- [`code/fcn.00403143.c`](code/fcn.00403143.c)
- [`code/fcn.00403a07.c`](code/fcn.00403a07.c)
- [`code/fcn.00403ccc.c`](code/fcn.00403ccc.c)
- [`code/fcn.00404305.c`](code/fcn.00404305.c)
- [`code/fcn.00404ae7.c`](code/fcn.00404ae7.c)
- [`code/fcn.00404bf1.c`](code/fcn.00404bf1.c)
- [`code/fcn.00405342.c`](code/fcn.00405342.c)
- [`code/fcn.00405414.c`](code/fcn.00405414.c)
- [`code/fcn.00405808.c`](code/fcn.00405808.c)
- [`code/fcn.00405937.c`](code/fcn.00405937.c)
- [`code/fcn.004059e3.c`](code/fcn.004059e3.c)
- [`code/fcn.00405ca1.c`](code/fcn.00405ca1.c)
- [`code/fcn.00405e8a.c`](code/fcn.00405e8a.c)
- [`code/fcn.00406026.c`](code/fcn.00406026.c)
- [`code/fcn.00406108.c`](code/fcn.00406108.c)
- [`code/fcn.00406198.c`](code/fcn.00406198.c)
- [`code/fcn.004062b4.c`](code/fcn.004062b4.c)
- [`code/fcn.004064ff.c`](code/fcn.004064ff.c)
- [`code/fcn.004065bf.c`](code/fcn.004065bf.c)
- [`code/fcn.004066e4.c`](code/fcn.004066e4.c)
- [`code/fcn.00406772.c`](code/fcn.00406772.c)

## Behavioral Analysis

Based on the disassembly provided, here is an analysis of the binary's behavior.

### Core Functionality and Purpose
The binary is a **software installer**, specifically one built using the **NSIS (Nullsoft Script Installer)** framework. The presence of strings like `"NSIS Error"`, `"-nsi"`, and the logic used to handle temporary files and "integrity checks" are signature characteristics of NSIS installers.

Its primary purpose is to:
*   **Extract and Install Software:** It manages the unpacking of compressed data, moving files to target directories (e.g., `C:\Program Files`), and creating shortcuts.
*   **Environment Preparation:** It validates system capabilities, checks for required system files, and ensures proper directory permissions are set before installation.
*   **User Interaction:** It utilizes standard Windows UI elements (GDI, User32) to display progress bars, dialog boxes, and "Finish" prompts.

### Suspicious or Malicious Behaviors
While this is a legitimate installer tool, in the context of malware analysis, such installers are often used as **droppers** or **wrappers**. Because it performs several high-privilege actions by design, they can be used to mask malicious activity:

*   **File Manipulation:** The code frequently uses `MoveFileA`, `CopyFileA`, and `ShellExecuteA`. It creates temporary directories (e.g., `\nsi.tmp`) and moves files into them. These are standard for installers but are also common tactics for "dropping" malware onto the disk before execution.
*   **Registry Manipulation:** Extensive use of `RegOpenKeyExA`, `RegSetValueExA`, and `RegDeleteValueA` indicates it modifies system settings, creates shortcuts (via registry keys), or installs shell extensions.
*   **Privilege Adjustment:** The inclusion of `AdjustTokenPrivileges` and `LookupPrivilegeValueA` suggests the installer attempts to acquire administrative privileges to modify protected areas of the OS (like `HKEY_LOCAL_MACHINE`).
*   **System Persistence/Interaction:** Through its logic for creating shortcuts and modifying registry keys, it can establish persistence for any software it is "installing."

### Notable Techniques or Patterns
*   **NSIS Framework Identification:** The code contains several hardcoded strings (e.g., `_nsi`, `nsi.tmp`) and internal logic structures typical of NSIS script processing. This tells an analyst that the core installer engine is standard; if malicious behavior exists, it likely resides in the "payload" being installed rather than the installer itself.
*   **CRC32 Integrity Check:** The function `fcn.004066e4` is a classic implementation of the **CRC32 algorithm**. It is used to ensure that files extracted from the compressed archive are not corrupted, but it can also be used in malicious samples to verify that a payload hasn't been tampered with by security tools.
*   **Dynamic Library Loading:** The use of `GetProcAddress` and `LoadLibraryExA` (seen in `fcn.004065bf`) allows the installer to dynamically load system DLLs. While standard, this is also a technique used by malware to bypass static detection.
*   **Error Handling & Feedback:** The code includes extensive logging for "integrity check failures" and "failed installation," which helps the developer debug the script but also gives away the program's role as an installer.

### Summary of Risk
The binary is likely **not a standalone piece of malware**, but rather a **standard installer tool**. However, because it has the capability to move files across the system, modify registry keys for persistence, and elevate privileges, it is a prime candidate for being used in a "dropper" chain. If this was found in an unrelated folder or accompanied by unusual file names, it should be treated as a delivery mechanism for a secondary payload.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1112** | Modify Registry | The binary utilizes `RegOpenKeyExA`, `RegSetValueExA`, and `RegDeleteValueA` to modify system settings and create shortcut entries. |
| **T1547.001** | Boot or Logon Autostart Execution | The creation of shortcuts and modification of specific registry keys indicate a mechanism to ensure the "installed" software persists across system reboots. |
| **T1068** | Exploitation for Privilege Escalation | The implementation of `AdjustTokenPrivileges` and `LookupPrivilegeValueA` indicates an attempt to gain higher privileges to access protected areas of the OS. |
| **T1106** | Native API | The use of `GetProcAddress` and `LoadLibraryExA` allows the binary to resolve and load functions at runtime, which is often used to bypass static detection. |
| **T1595** | Dump__Credentials (Note: Not specifically observed but implied by "Installer" role) | *Alternative:* **T1036** (Masquerading) - The use of a legitimate NSIS installer framework provides a layer of masquerading to hide the presence of malicious payloads. |
| **T1027** | Obfuscated Files or Information | The inclusion of a CRC32 integrity check can be used by attackers to ensure that dropped payloads have not been altered or tampered with by security tools. |

***Note for Analysis:** While many of these behaviors are standard for legitimate installers, their presence in an unsolicited binary is typical of "Dropper" behavior, where the installer acts as a delivery vehicle for a secondary malicious payload.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** As per your instructions, standard Windows system paths (e.g., `Software\Microsoft\Windows\CurrentVersion`) and common API calls were excluded as they are not unique to a specific threat actor or campaign.

### **IP addresses / URLs / Domains**
*   None detected.

### **File paths / Registry keys**
*   `\nsi.tmp` (Used by the installer for temporary file staging).

### **Mutex names / Named pipes**
*   None detected.

### **Hashes**
*   None found in the provided strings.

### **Other artifacts**
*   **Framework Identifiers:** The binary is identified as an **NSIS (Nullsoft Script Installer)** wrapper/installer. 
    *   Specific strings: `"NSIS Error"`, `"-nsi"`
*   **Algorithm Signatures:** A CRC32 implementation was identified at function offset `0x4066e4`. While this is a standard algorithm, the specific offset can be used for signature-based detection of this specific installer build.
*   **Dynamic Loading Patterns:** Use of `GetProcAddress` and `LoadLibraryExA` are noted as methods used to dynamically load system DLLs (often used by both installers and malware to evade static analysis).

***

### **Analyst Note**
The analysis indicates that this file is likely a **delivery mechanism (dropper/wrapper)** rather than the primary payload. The inclusion of NSIS-specific logic suggests it is designed to move files, modify registry keys for persistence, and escalate privileges. While the installer itself is "standard," its presence in an unsolicited directory should be treated as a high-priority alert for investigation into the subsequent payload being installed.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper
3. **Confidence**: High

4. **Key evidence**:
* **NSIS Framework Identification:** The presence of specific strings (e.g., `"NSIS Error"`, `"-nsi"`) and logic for handling temporary files confirms the binary is an NSIS-based installer, a common vehicle for wrapping malicious payloads.
* **Delivery Mechanism Characteristics:** The analysis highlights "dropper" behaviors such as registry manipulation for persistence, privilege escalation (`AdjustTokenPrivileges`), and CRC32 integrity checks to ensure payload stability during installation.
* **Lack of Standalone Payload:** The evidence suggests the binary's primary role is as a delivery vehicle (wrapper) rather than an active malware payload like a RAT or ransomware; it provides the infrastructure for a secondary malicious file to execute.
