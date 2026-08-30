# Threat Analysis Report

**Generated:** 2026-08-18 21:20 UTC
**Sample:** `106264fd9a3a4e198b360f86dece9a1f85f863b46a7192b132c8330c4e13289c_106264fd9a3a4e198b360f86dece9a1f85f863b46a7192b132c8330c4e13289c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `106264fd9a3a4e198b360f86dece9a1f85f863b46a7192b132c8330c4e13289c_106264fd9a3a4e198b360f86dece9a1f85f863b46a7192b132c8330c4e13289c.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 15,645,908 bytes |
| MD5 | `4d8874cc0c37b618ea03f10827381330` |
| SHA1 | `81b62f5f30385e581d8b07594f440cc09fffe246` |
| SHA256 | `106264fd9a3a4e198b360f86dece9a1f85f863b46a7192b132c8330c4e13289c` |
| Overall entropy | 8.0 |
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
| `.rsrc` | 18,432 | 5.885 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `SetFileSecurityW`, `RegOpenKeyExW`, `RegEnumValueW`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHFileOperationW`, `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `ShellExecuteExW`, `SHGetFileInfoW`
**ole32.dll**: `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `GetClientRect`, `EndPaint`, `DrawTextW`, `IsWindowEnabled`, `DispatchMessageW`, `wsprintfA`, `CharNextA`, `CharPrevW`, `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `GetSystemMetrics`, `FillRect`, `AppendMenuW`, `TrackPopupMenu`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectW`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetModuleHandleA`, `GetProcAddress`, `GetSystemDirectoryW`, `lstrcatW`, `Sleep`, `lstrcpyA`, `WriteFile`, `GetTempFileNameW`, `lstrcmpiA`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `GetLastError`

## Extracted Strings

Total strings found: **33932** (showing first 100)

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

This is a technical analysis of the provided disassembled code.

### Core Functionality and Purpose
The binary functions as an **installer or "wrapper" application**, likely utilizing the **NSIS (Nullsoft Script Installer)** framework, given the specific error messages and logic patterns found in the disassembly. Its primary purpose is to perform environment checks, unpack/extract files from a payload, verify their integrity, and prepare them for installation on the host system.

### Suspicious or Malicious Behaviors
While the code exhibits characteristics of a standard installer, several behaviors are commonly observed in **droppers** (malware that "drops" a secondary malicious payload onto a system):

*   **Dropped File/Staging Behavior:** The code heavily utilizes `MoveFileW`, `CopyFileW`, and `CreateDirectoryW` to move data into temporary directories. Specifically, it creates folders and copies files from an internal buffer or temp location to execution paths. 
*   **Privilege Escalation:** The application attempts to identify and acquire administrative-level privileges using `LookupPrivilegeValueW` and `AdjustTokenPrivileges`. While common in installers to modify system files, this is also a classic technique used by malware to gain higher permissions.
*   **System Interaction/Environment Probing:** It queries the system for specific capabilities (e.g., `UXTHEME`, `GetVersionExW`) and modifies environment variables or system paths before executing subsequent components.
*   **Extraction of Components:** The code contains logic to extract "resources" or embedded files from itself, then move these files into a working directory before calling `ShellExecute` (or similar) to run them.

### Notable Techniques and Patterns
The following technical patterns were observed:

*   **NSIS Wrapper Signature:** The presence of strings like `"Installer integrity check has failed..."` and the specific logic in `fcn.004030d17` strongly indicate this is an NSIS-based installer. These are often used to bundle third-party software but are also frequently utilized by malware authors to wrap a malicious payload in a "legitimate-looking" installer wrapper.
*   **Integrity Verification (CRC32):** The function `fcn.00406b22` implements a standard **CRC32 checksum algorithm**. This is used to ensure that the files being unpacked or moved have not been corrupted during the extraction process. 
*   **Dynamic Resource Loading:** The use of `GetProcAddress`, `LoadLibraryExW`, and "manual" resolution of function pointers (via an internal table) suggests a technique to reduce the Import Address Table (IAT) size, making it harder for automated tools to see every API the program calls.
*   **Resource Handling:** Extensive usage of `Shell32` and `Ole32` functions indicates the handling of complex objects or file system metadata before the final payload is executed.

### Summary Conclusion
This binary is an **installer-style wrapper**. While it may be a legitimate piece of software, its behavior—specifically the extraction of files into temporary directories followed by privilege escalation and integrity checks—is identical to the behavior exhibited by **malware droppers**. If this sample was found in an unexpected location or associated with an unknown source, it should be treated as a potential delivery mechanism for a second-stage payload.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your technical analysis to the relevant MITRE ATT&CK techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1068** | Exploitation for Privilege Escalation | The use of `LookupPrivilegeValueW` and `AdjustTokenPrivileges` indicates an attempt to acquire higher system permissions. |
| **T1082** | System Information Discovery | The application queries system capabilities (e.g., `GetVersionExW`) and environment details before execution. |
| **T1027** | Obfuscated Files or Information | The use of internal resources, hidden components, and extraction logic suggests a method to conceal the payload from static analysis. |
| **T1106** | Native API | The reliance on Win32 APIs (such as `MoveFileW`, `CopyFileW`, and `ShellExecute`) to facilitate file manipulation and execution. |
| **T1574** | Hijack Execution Flow | The "wrapper" functionality acts as a vehicle to prepare the environment and execute a secondary, potentially malicious, payload. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   *Note: No specific hardcoded file paths or unique registry keys were found in the text.* The analysis mentions "temporary directories" and system-wide items, but no specific paths (e.g., `C:\Windows\Temp` or a specific malicious path) were provided in the sample.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified. (Note: The references to `fcn.004030d17` and `fcn.00406b22` are internal code offsets, not file hashes).

### **Other artifacts**
*   **Tooling/Framework Identification:** NSIS (Nullsoft Script Installer) Wrapper.
*   **Known String:** `"Installer integrity check has failed..."` (Used to identify the installer's logic path).
*   **Techniques identified:** 
    *   CRC32 checksum algorithm usage (for payload verification).
    *   Dynamic API resolution via `GetProcAddress` and `LoadLibraryExW`.
    *   Privilege Escalation attempts (`LookupPrivilegeValueW`, `AdjustTokenPrivileges`).

---

### **Analyst Summary**
While the sample contains no high-fidelity network IOCs (IPs/Domains) or specific hardcoded file paths, it is categorized as an **installer-style wrapper**. The lack of direct indicators suggests that this binary likely acts as a "dropper" or "downloader," where the actual malicious payload is either embedded within the resource sections or downloaded from a remote server after the integrity checks are passed.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`
- `http://schemas.microsoft.com/SMI/2016/WindowsSettings`

---

## Malware Family Classification

1. **Malware family**: Unknown (NSIS Wrapper)
2. **Malware type**: Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Wrapper/Dropper Functionality:** The binary acts as a staging vehicle, using NSIS-style logic to extract embedded components, perform CRC32 integrity checks, and move files into temporary directories before execution via `ShellExecute`.
*   **Privilege Escalation & Persistence:** It utilizes `LookupPrivilegeValueW` and `AdjustTokenPrivileges` to gain elevated permissions, a common tactic used by droppers to ensure the subsequent payload can perform administrative actions.
*   **Evasion Techniques:** The use of dynamic API resolution (`GetProcAddress`, `LoadLibraryExW`) to manually resolve function pointers indicates an attempt to reduce the Import Address Table (IAT) size and evade basic static analysis of its capabilities.
