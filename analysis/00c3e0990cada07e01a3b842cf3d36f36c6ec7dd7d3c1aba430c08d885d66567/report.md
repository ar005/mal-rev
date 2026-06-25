# Threat Analysis Report

**Generated:** 2026-06-24 20:18 UTC
**Sample:** `00c3e0990cada07e01a3b842cf3d36f36c6ec7dd7d3c1aba430c08d885d66567_00c3e0990cada07e01a3b842cf3d36f36c6ec7dd7d3c1aba430c08d885d66567.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00c3e0990cada07e01a3b842cf3d36f36c6ec7dd7d3c1aba430c08d885d66567_00c3e0990cada07e01a3b842cf3d36f36c6ec7dd7d3c1aba430c08d885d66567.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 910,048 bytes |
| MD5 | `00d1386ab7bc8a72d075813480cfb082` |
| SHA1 | `35eb4ad99745ab2bdbac0553f71cdaa0f584d827` |
| SHA256 | `00c3e0990cada07e01a3b842cf3d36f36c6ec7dd7d3c1aba430c08d885d66567` |
| Overall entropy | 7.953 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1596238135 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,088 | 6.418 | No |
| `.rdata` | 5,120 | 5.061 | No |
| `.data` | 1,536 | 3.995 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 30,208 | 5.028 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExA`, `RegEnumKeyA`, `RegQueryValueExA`, `RegSetValueExA`, `RegCloseKey`, `RegDeleteValueA`, `RegDeleteKeyA`, `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, `OpenProcessToken`, `SetFileSecurityA`, `RegOpenKeyExA`, `RegEnumValueA`
**SHELL32.dll**: `SHGetFileInfoA`, `SHFileOperationA`, `SHGetPathFromIDListA`, `ShellExecuteExA`, `SHGetSpecialFolderLocation`, `SHBrowseForFolderA`
**ole32.dll**: `IIDFromString`, `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `SetClipboardData`, `CharPrevA`, `CallWindowProcA`, `PeekMessageA`, `DispatchMessageA`, `MessageBoxIndirectA`, `GetDlgItemTextA`, `SetDlgItemTextA`, `GetSystemMetrics`, `CreatePopupMenu`, `AppendMenuA`, `TrackPopupMenu`, `FillRect`, `EmptyClipboard`, `LoadCursorA`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectA`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetProcAddress`, `GetSystemDirectoryA`, `WideCharToMultiByte`, `MoveFileExA`, `ReadFile`, `GetTempFileNameA`, `WriteFile`, `RemoveDirectoryA`, `CreateProcessA`, `CreateFileA`, `GetLastError`, `CreateThread`, `CreateDirectoryA`

## Extracted Strings

Total strings found: **2075** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's behavior.

### Core Functionality and Purpose
The binary appears to be a **software installer or a packer/loader** (specifically, it exhibits characteristics of the **NSIS (Nullsoft Script Installer)** framework). Its primary purpose is to manage the installation process, which includes extracting files from a compressed archive, moving them to their final destination, and performing system configuration.

### Suspicious or Malicious Behaviors
While this code reflects standard installer behavior, these actions are frequently used by malware to "drop" and execute malicious payloads:

*   **File System Manipulation:** 
    *   The code performs extensive file movement (`MoveFileA`, `CopyFileA`) and deletion (`DeleteFileA`). It specifically handles moving files from temporary paths (retrieved via `GetTempPathA`) to final locations.
    *   It programmatically creates directories and attempts to set specific security attributes/permissions for those folders (`fcn.004056ae`).
*   **Registry Interaction:** 
    *   The code frequently interacts with the Windows Registry using `RegOpenKeyExA`, `RegSetValueExA`, and `RegQueryValueExA`. In an installer context, this is used for creating shortcuts or configuration; in a malware context, it is often used to establish **persistence** (e.g., "Run" keys) or modify system behavior.
*   **Dynamic API Loading:** 
    *   The binary uses `GetProcAddress` and `LoadLibraryExA` to dynamically resolve and load functions at runtime. This technique is commonly used to hide functionality from static analysis or to delay the loading of malicious capabilities until necessary.
*   **System Integration:**
    *   The presence of `UXTHEME`, `ShellExecuteExA`, and various GDI/User32 calls indicates that it interacts with the Windows shell and GUI, potentially to present a "friendly" installer interface or a fake error message.

### Notable Techniques and Patterns
*   **Integrity Checking:** The function `fcn.006581` implements a **CRC32-style checksum algorithm**. This is typically used during the unpacking process to ensure that the files extracted from the internal archive were not corrupted.
*   **Environment/Path Resolution:** The code contains heavy logic for resolving system paths (e.g., handling `%ProgramFiles%`, `%SystemRoot%`). It uses `GetShortPathNameA` and `ExpandEnvironmentStringsA` to normalize paths before performing file operations.
*   **Resource Loading:** The usage of `LoadImageA` suggests the binary may be loading sections or resources into memory in a manner that could facilitate "reflective" loading if the binary were repurposed as a loader for malicious components.
*   **Installer Metadata:** The presence of strings like `"NSIS Error"` and specific logic to check for `system32` and other environment variables confirms the use of known installer scripting engines.

### Summary Conclusion
This sample is likely an **installer stub**. While it exhibits behaviors common to legitimate software installers (moving files, registry modification, checksumming), these same capabilities are used by malware "droppers" to unpack and install a malicious payload on a host system. The presence of advanced file resolution and integrity checking suggests a multi-stage execution flow.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Installation | The binary acts as a loader/installer to move files from temporary directories to final locations, a behavior common in dropping malicious payloads. |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys | The interaction with registry keys (e.g., "Run" keys) is specifically identified as a method for establishing persistence. |
| T1027 | Obfuscated Files or Information | Dynamic API loading via `GetProcAddress` and `LoadLibraryExA` is used to hide functionality from static analysis tools. |
| T1213 | System Information Discovery | The use of `GetShortPathNameA` and `ExpandEnvironmentStringsA` demonstrates the gathering of system paths and environment details. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: In accordance with your instructions, standard Windows API calls, system-wide registry paths (e.g., `Software\Microsoft\Windows\CurrentVersion`), and common library names have been excluded as they are considered false positives/environment defaults.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. *(Note: All registry paths identified in the text—such as `Control Panel\Desktop` and `.DEFAULT\Control Panel`—are standard Windows system paths.)*

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Malware Framework/Tooling:** NSIS (Nullsoft Script Installer) - The binary exhibits behaviors consistent with an NSIS installer, commonly used as a wrapper or dropper for payloads.
*   **Execution Techniques:** 
    *   **Dynamic API Loading:** Use of `GetProcAddress` and `LoadLibraryExA` to resolve functions at runtime.
    *   **Integrity Checking:** Implementation of a CRC32-style checksum algorithm (at offset `fcn.006581`).
    *   **Persistence/Configuration Logic:** Usage of `RegOpenKeyExA`, `RegSetValueExA`, and `RegQueryValueExA` to modify system configuration or persistence.
    *   **Environment Manipulation:** Use of `GetTempPathA` and `ExpandEnvironmentStringsA` for path resolution.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: Medium

4. **Key evidence**:
* **Installer Stub Behavior:** The binary is identified as an NSIS (Nullsoft Script Installer) stub, a common technique used by threat actors to wrap and deliver malicious payloads in a "friendly" installation interface.
* **Deployment Techniques:** The analysis highlights behaviors typical of a dropper: moving files from temporary paths to final locations (`GetTempPathA`, `MoveFileA`), performing registry modifications for persistence (T1547.001), and using CRC32 integrity checks to verify the unpacked payload.
* **Evasion Tactics:** The use of dynamic API loading (`GetProcAddress` and `LoadLibraryExA`) suggests a deliberate attempt to hide functionality from static analysis, a common characteristic in multi-stage malware loaders.
