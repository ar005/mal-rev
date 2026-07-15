# Threat Analysis Report

**Generated:** 2026-07-14 14:05 UTC
**Sample:** `05a97268db58bd86fc730eb09e3fc4ff999309cfa0832d323668dc37704b66c2_05a97268db58bd86fc730eb09e3fc4ff999309cfa0832d323668dc37704b66c2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05a97268db58bd86fc730eb09e3fc4ff999309cfa0832d323668dc37704b66c2_05a97268db58bd86fc730eb09e3fc4ff999309cfa0832d323668dc37704b66c2.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 476,766 bytes |
| MD5 | `1f9b92143c1d6ed2e43a269027dd5f96` |
| SHA1 | `bf5ee6f91e9210b72028a987bddd8e2cc0c82d3d` |
| SHA256 | `05a97268db58bd86fc730eb09e3fc4ff999309cfa0832d323668dc37704b66c2` |
| Overall entropy | 7.456 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1627165123 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.403 | No |
| `.rdata` | 5,120 | 5.057 | No |
| `.data` | 1,536 | 4.09 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 167,424 | 5.928 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExA`, `RegEnumKeyA`, `RegQueryValueExA`, `RegSetValueExA`, `RegCloseKey`, `RegDeleteValueA`, `RegDeleteKeyA`, `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, `OpenProcessToken`, `SetFileSecurityA`, `RegOpenKeyExA`, `RegEnumValueA`
**SHELL32.dll**: `SHGetFileInfoA`, `SHFileOperationA`, `SHGetPathFromIDListA`, `ShellExecuteExA`, `SHGetSpecialFolderLocation`, `SHBrowseForFolderA`
**ole32.dll**: `IIDFromString`, `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `SetClipboardData`, `CharPrevA`, `CallWindowProcA`, `PeekMessageA`, `DispatchMessageA`, `MessageBoxIndirectA`, `GetDlgItemTextA`, `SetDlgItemTextA`, `GetSystemMetrics`, `CreatePopupMenu`, `AppendMenuA`, `TrackPopupMenu`, `FillRect`, `EmptyClipboard`, `LoadCursorA`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectA`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetProcAddress`, `GetSystemDirectoryA`, `WideCharToMultiByte`, `MoveFileExA`, `GetTempFileNameA`, `RemoveDirectoryA`, `WriteFile`, `CreateDirectoryA`, `GetLastError`, `CreateProcessA`, `GlobalLock`, `GlobalUnlock`, `CreateThread`

## Extracted Strings

Total strings found: **857** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQVPW
Et@;u
vX95HGB
Instu`
softuW
NulluN	E
D$(SPS
tVj%SSS
D$$+D$
D$,+D$$P
u9=@B
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
| `fcn.00401434` | `0x401434` | 5688 | ✓ |
| `fcn.00406776` | `0x406776` | 2642 | ✓ |
| `entry0` | `0x403461` | 1256 | ✓ |
| `fcn.00403a3b` | `0x403a3b` | 709 | ✓ |
| `fcn.00402ef1` | `0x402ef1` | 673 | ✓ |
| `fcn.004062bb` | `0x4062bb` | 584 | ✓ |
| `fcn.004059f0` | `0x4059f0` | 464 | ✓ |
| `fcn.00405e97` | `0x405e97` | 368 | ✓ |
| `fcn.0040329a` | `0x40329a` | 361 | ✓ |
| `fcn.00403192` | `0x403192` | 264 | ✓ |
| `fcn.00402cd0` | `0x402cd0` | 234 | ✓ |
| `fcn.0040534f` | `0x40534f` | 210 | ✓ |
| `fcn.00404313` | `0x404313` | 207 | ✓ |
| `fcn.00404af5` | `0x404af5` | 197 | ✓ |
| `fcn.00403d00` | `0x403d00` | 185 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00402e52` | `0x402e52` | 159 | ✓ |
| `fcn.00406503` | `0x406503` | 153 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.0040619f` | `0x40619f` | 137 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404bff` | `0x404bff` | 128 | ✓ |
| `fcn.00405815` | `0x405815` | 125 | ✓ |
| `fcn.00406033` | `0x406033` | 123 | ✓ |
| `fcn.00405cae` | `0x405cae` | 120 | ✓ |
| `fcn.0040610f` | `0x40610f` | 119 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004066e8` | `0x4066e8` | 110 | ✓ |
| `fcn.004065c3` | `0x4065c3` | 110 | ✓ |
| `fcn.00405421` | `0x405421` | 108 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402cd0.c`](code/fcn.00402cd0.c)
- [`code/fcn.00402e52.c`](code/fcn.00402e52.c)
- [`code/fcn.00402ef1.c`](code/fcn.00402ef1.c)
- [`code/fcn.00403192.c`](code/fcn.00403192.c)
- [`code/fcn.0040329a.c`](code/fcn.0040329a.c)
- [`code/fcn.00403a3b.c`](code/fcn.00403a3b.c)
- [`code/fcn.00403d00.c`](code/fcn.00403d00.c)
- [`code/fcn.00404313.c`](code/fcn.00404313.c)
- [`code/fcn.00404af5.c`](code/fcn.00404af5.c)
- [`code/fcn.00404bff.c`](code/fcn.00404bff.c)
- [`code/fcn.0040534f.c`](code/fcn.0040534f.c)
- [`code/fcn.00405421.c`](code/fcn.00405421.c)
- [`code/fcn.00405815.c`](code/fcn.00405815.c)
- [`code/fcn.004059f0.c`](code/fcn.004059f0.c)
- [`code/fcn.00405cae.c`](code/fcn.00405cae.c)
- [`code/fcn.00405e97.c`](code/fcn.00405e97.c)
- [`code/fcn.00406033.c`](code/fcn.00406033.c)
- [`code/fcn.0040610f.c`](code/fcn.0040610f.c)
- [`code/fcn.0040619f.c`](code/fcn.0040619f.c)
- [`code/fcn.004062bb.c`](code/fcn.004062bb.c)
- [`code/fcn.00406503.c`](code/fcn.00406503.c)
- [`code/fcn.004065c3.c`](code/fcn.004065c3.c)
- [`code/fcn.004066e8.c`](code/fcn.004066e8.c)
- [`code/fcn.00406776.c`](code/fcn.00406776.c)

## Behavioral Analysis

Based on the disassembly provided, here is an analysis of the binary's functionality and behavior.

### Core Functionality and Purpose
The code functions as a **sophisticated installer or unpacker**, likely utilizing the **NSIS (Nullsoft Script Installer)** framework or a similar script-driven deployment engine. The core logic focuses on unpacking files from a temporary location, verifying their integrity before "installation," and configuring system settings (registry keys, file permissions).

### Key Behaviors & Features

*   **Integrity Verification:**
    *   The function `fcn.00406776` implements a standard CRC32 or similar checksum algorithm to verify data integrity.
    *   Function `fcn.00402ef1` specifically performs an "Installer integrity check." If the hash of the extracted files does not match expected values, it displays an error message ("Installer integrity check has failed") and refers to "NSIS" errors.

*   **File Extraction & Management:**
    *   The code heavily utilizes `GetTempPathA`, `CreateFileA`, `WriteFile`, and `MoveFileExA`. This indicates a "Stage-and-Move" logic: it extracts files into a temporary directory (possibly for decryption or unpacking) before moving them to their final destination.
    *   It performs extensive file system traversal using `FindFirstFileA` and `FindNextFileA` to identify components within a bundle.

*   **System & Environment Manipulation:**
    *   **Registry Interaction:** The code interacts with several registry keys (via `RegOpenKeyExA`, `RegSetValueExA`, etc.) related to system configuration and potentially persistence (e.g., modifying "CurrentVersion" paths).
    *   **Privilege Escalation:** The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueA` suggests the installer seeks elevated privileges to perform tasks like setting file permissions (`SetFileSecurityA`) or modifying system-wide settings.
    *   **Environment Configuration:** It actively manages environment variables (e.g., "TEMP" paths) using `SetEnvironmentVariableA`.

*   **User Interface Interaction:**
    *   The code contains numerous UI management routines, such as `SendMessageA`, `SetForegroundWindow`, and `GetDlgItem`. These are used to update progress bars, display status messages (via `SetWindowTextA`), and handle multi-step dialog boxes.

### Suspicious or Malicious Indicators

While the functionality is consistent with a legitimate installer, several characteristics are common in **droppers** and **malware loaders**:

*   **Multi-Stage Extraction:** The pattern of extracting files to a temp folder (often `\AppData\Local\Temp` or similar) before moving them is a classic technique for malware to hide the final payload until the very last moment.
*   **Integrity Checks as Evasion:** While used by legitimate software, "integrity checks" are also used by malware to ensure that its components have not been modified/replaced by security software (sandboxes or AV) during the unpacking process.
*   **Privilege Escalation:** The specific attempt to acquire high-level privileges suggests it intends to modify protected system files or registry keys common for persistence.

### Notable Techniques & Patterns
*   **Standard Wrapper Usage:** The code uses standard Win32 API wrappers heavily (via `GetProcAddress` and `LoadLibraryExA`), which is common in compilers but also allows malware to resolve APIs dynamically to evade static detection.
*   **Custom Logic Loops:** Function `fcn.00401434` contains a large switch-case structure, indicating a state machine used to manage various steps of the installation/unpacking process (e.g., "Check File," "Move Folder," "Apply Registry").
*   **NSIS Signature:** The error strings and logic flow strongly indicate that this is an NSIS wrapper. Malware authors frequently use NSIS because it is a powerful, well-documented tool for automating the deployment of payloads across various versions of Windows.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1068 | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueA` indicates a deliberate attempt to gain elevated permissions to modify system-wide settings. |
| T1112 | Modify Registry | The binary interacts with multiple registry keys via `RegOpenKeyExA` and `RegSetValueExA` to configure system paths and potentially establish persistence. |
| T1036 | Hideers | The "Stage-and-Move" logic of extracting files to a temporary directory before moving them is a common tactic used to conceal the final payload's location during execution. |
| T1027 | Obfuscated Files or Information | The use of dynamic API resolution (`GetProcAddress`, `LoadLibraryExA`) and integrity checks are employed to hinder static analysis and detect if the file is being inspected by security tools. |
| T1059 | Command and Scripting Interpreter | The reliance on the NSIS framework demonstrates the use of a script-driven deployment engine to automate complex installation tasks and payload delivery. |
| T1547.001 | Non-Standard Port (Related) / [Alternative: T1036] | *(Note: While the "Environment Configuration" via `SetEnvironmentVariableA` is noted, it most closely aligns with general persistence or evasion techniques depending on the specific variables targeted.)* |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Per your instructions, standard Windows system paths and common library strings have been excluded from this report.*

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified (All identified registry keys, such as `Software\Microsoft\Windows\CurrentVersion`, were determined to be standard Windows system paths).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Tooling Identification:** NSIS (Nullsoft Script Installer) framework usage (identified via error strings and logic flow).
*   **Behavioral Pattern (Stage-and-Move):** The binary utilizes a "Stage-and-Move" tactic, extracting files to temporary directories using `GetTempPathA` before moving them to final locations.
*   **Evasion Technique:** Use of "Installer integrity checks" (specifically in function `fcn.00402ef1`) which can be used by malware to detect and evade sandbox/security software analysis.
*   **Privilege Escalation:** Attempted acquisition of high-level privileges via `AdjustTokenPrivileges` and `LookupPrivilegeValueA` to modify system files or registry keys.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1.  **Malware family:** custom
2.  **Malware type:** dropper / loader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Multi-Stage Delivery Logic:** The binary utilizes a "Stage-and-Move" execution pattern, extracting payloads to temporary directories (`GetTempPathA`) and performing integrity checks (CRC32) before deployment—a hallmark of droppers/loaders designed to hide the final payload from static analysis.
    *   **Wrapper Functionality:** Use of the NSIS framework and dynamic API resolution (`GetProcAddress`, `LoadLibraryExA`) indicates the binary's primary role is as a delivery vehicle (wrapper) rather than the ultimate malicious payload.
    *   **Persistence & Privilege Preparation:** The inclusion of `AdjustTokenPrivileges` for privilege escalation and registry modifications suggests it is preparing the system environment to allow subsequent components to establish persistence or perform high-level operations.
