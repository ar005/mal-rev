# Threat Analysis Report

**Generated:** 2026-09-07 01:16 UTC
**Sample:** `154ebc207e7463ba7a1aa994236f83246625bb13fa365a5825715b3b56a39caf_154ebc207e7463ba7a1aa994236f83246625bb13fa365a5825715b3b56a39caf.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `154ebc207e7463ba7a1aa994236f83246625bb13fa365a5825715b3b56a39caf_154ebc207e7463ba7a1aa994236f83246625bb13fa365a5825715b3b56a39caf.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 787,376 bytes |
| MD5 | `85cd5c77764bf1a765dbf64aaa831c9b` |
| SHA1 | `a42c18666aeb1bfcf7d192b9d2f8052fa0563c14` |
| SHA256 | `154ebc207e7463ba7a1aa994236f83246625bb13fa365a5825715b3b56a39caf` |
| Overall entropy | 7.808 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1741475120 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,624 | 6.454 | No |
| `.rdata` | 5,120 | 5.1 | No |
| `.data` | 1,536 | 4.123 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 90,624 | 4.477 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`, `GetCommandLineW`

## Extracted Strings

Total strings found: **1657** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQWPV
Instuj
softua
NulluX	E
UVWj _3
L$bf-S
D$ Pj(
D$,UPU
tVj%UUU
f9=P/B
D$$+D$
D$,+D$$P
u9=@/B
WWWWjn
us9Et	
FFC;]|
8\tPV
\u f9O
69}t(j
90u'AAf
l$(9l$(tr
+D$(PV
_^][t
P
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
RegOpenKeyExW
RegCreateKeyExW
ADVAPI32.dll
SHFileOperationW
SHGetFileInfoW
SHBrowseForFolderW
SHGetPathFromIDListW
ShellExecuteExW
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
| `fcn.00401434` | `0x401434` | 6196 | ✓ |
| `fcn.00406c4b` | `0x406c4b` | 2642 | ✓ |
| `entry0` | `0x40369f` | 1565 | ✓ |
| `fcn.00403dae` | `0x403dae` | 726 | ✓ |
| `fcn.004030fc` | `0x4030fc` | 724 | ✓ |
| `fcn.00406719` | `0x406719` | 625 | ✓ |
| `fcn.00405de8` | `0x405de8` | 451 | ✓ |
| `fcn.00406322` | `0x406322` | 378 | ✓ |
| `fcn.004034d8` | `0x4034d8` | 361 | ✓ |
| `fcn.004033d0` | `0x4033d0` | 264 | ✓ |
| `fcn.00402ed5` | `0x402ed5` | 234 | ✓ |
| `fcn.00405761` | `0x405761` | 211 | ✓ |
| `fcn.004046c2` | `0x4046c2` | 207 | ✓ |
| `fcn.00404f08` | `0x404f08` | 201 | ✓ |
| `fcn.00404084` | `0x404084` | 185 | ✓ |
| `fcn.0040698a` | `0x40698a` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040305a` | `0x40305a` | 162 | ✓ |
| `fcn.0040663c` | `0x40663c` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.004064c8` | `0x4064c8` | 129 | ✓ |
| `fcn.00405016` | `0x405016` | 128 | ✓ |
| `fcn.004060b3` | `0x4060b3` | 126 | ✓ |
| `fcn.004065aa` | `0x4065aa` | 121 | ✓ |
| `fcn.004062ad` | `0x4062ad` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406a60` | `0x406a60` | 112 | ✓ |
| `fcn.00406bbd` | `0x406bbd` | 110 | ✓ |
| `fcn.00405834` | `0x405834` | 108 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402ed5.c`](code/fcn.00402ed5.c)
- [`code/fcn.0040305a.c`](code/fcn.0040305a.c)
- [`code/fcn.004030fc.c`](code/fcn.004030fc.c)
- [`code/fcn.004033d0.c`](code/fcn.004033d0.c)
- [`code/fcn.004034d8.c`](code/fcn.004034d8.c)
- [`code/fcn.00403dae.c`](code/fcn.00403dae.c)
- [`code/fcn.00404084.c`](code/fcn.00404084.c)
- [`code/fcn.004046c2.c`](code/fcn.004046c2.c)
- [`code/fcn.00404f08.c`](code/fcn.00404f08.c)
- [`code/fcn.00405016.c`](code/fcn.00405016.c)
- [`code/fcn.00405761.c`](code/fcn.00405761.c)
- [`code/fcn.00405834.c`](code/fcn.00405834.c)
- [`code/fcn.00405de8.c`](code/fcn.00405de8.c)
- [`code/fcn.004060b3.c`](code/fcn.004060b3.c)
- [`code/fcn.004062ad.c`](code/fcn.004062ad.c)
- [`code/fcn.00406322.c`](code/fcn.00406322.c)
- [`code/fcn.004064c8.c`](code/fcn.004064c8.c)
- [`code/fcn.004065aa.c`](code/fcn.004065aa.c)
- [`code/fcn.0040663c.c`](code/fcn.0040663c.c)
- [`code/fcn.00406719.c`](code/fcn.00406719.c)
- [`code/fcn.0040698a.c`](code/fcn.0040698a.c)
- [`code/fcn.00406a60.c`](code/fcn.00406a60.c)
- [`code/fcn.00406bbd.c`](code/fcn.00406bbd.c)
- [`code/fcn.00406c4b.c`](code/fcn.00406c4b.c)

## Behavioral Analysis

Based on the provided disassembly and string data, here is a technical analysis of the binary's behavior.

### Core Functionality
The binary functions as a **dropper/installer stub**. Its primary purpose is to act as an initial "loader" for a secondary payload. It performs environmental checks, extracts or decrypts an embedded component (likely a malicious executable), moves it to a temporary directory, and executes it.

### Suspicious and Malicious Behaviors

*   **Dropper/Downloader Behavior:**
    *   The code extensively uses `GetTempPathW` and `GetTempFileNameW` to identify paths in the Windows Temp folder. 
    *   It utilizes `CopyFileW`, `MoveFileExW`, and `CreateFileW` to move files from its internal resources (or a nearby directory) into the system's temporary folders. This is a classic technique used by malware to "stage" an infection, where the actual malicious payload remains hidden in the original file until it is unpacked/moved during execution.
    *   The presence of `NSIS Error` strings suggests it may be leveraging or mimicking the **Nullsoft Script Installer (NSIS)** framework, which is commonly used by both legitimate installers and malware to wrap an initial "downloader" stage.

*   **Decryption and Deobfuscation:**
    *   **Function `fcn.004030fc`** contains a complex loop involving multiple logic branches and mathematical operations on data buffers (seen in the switch table at `0x40769d`). This is indicative of a **custom decryption or unpacking routine**. The purpose of this routine is to decrypt the main payload's code/data before it is executed.

*   **Privilege Escalation & Adjustment:**
    *   The binary calls `AdjustTokenPrivileges` and `LookupPrivilegeValueW`. This is often used by malware to attempt to gain administrative rights or specific system privileges (like `SeDebugPrivilege`) necessary for deeper persistence or interacting with protected system processes.

*   **Persistence and Configuration:**
    *   There is heavy interaction with the Windows Registry using `RegSetValueExW`, `RegOpenKeyExW`, and `RegEnumKeyW`. While common in installers, this is also a primary method for establishing **persistence** (e.g., adding an entry to "Run" keys) or modifying system behavior.

*   **Defense Evasion:**
    *   The use of `GetTickCount` and several `Sleep` calls throughout the code are often used as primitive **anti-analysis/anti-debugging** techniques. They can be used to time out simple sandboxes or bypass certain automated analysis scripts that look for immediate, high-activity behavior.

### Notable Techniques & Patterns

*   **Multi-Stage Execution:** The separation between `entry0` (the loader) and the complex logic in `fcn.004030fc` (the unpacker) indicates a multi-stage execution chain. This is designed to bypass static file scanners, as the "main" malicious code does not exist on disk until this binary runs.
*   **Environment Preparation:** The inclusion of several standard Windows libraries (`ADVAPI32`, `SHELL32`, `USER32`) and the specific handling of registry keys suggest a highly organized installer intended to ensure it has the necessary permissions to modify the host system successfully.
*   **Resource Extraction:** The logic in `fcn.00406187` and related functions suggests the binary is capable of reading resources from its own data section/files and reconstructing them into an executable format in memory or on disk.

### Summary for Incident Response
This sample is likely a **first-stage dropper**. It is designed to:
1.  **Hide the main payload** via decryption (found in `fcn.004030fc`).
2.  **Extract and stage** that payload into a temporary directory (`%TEMP%`) where it can be executed without raising immediate suspicion from simple file-system monitors.
3.  **Escalate privileges** to ensure the final payload has sufficient permissions to carry out its ultimate objective (e.g., credential theft, ransomware encryption, or establishing a backdoor).

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The presence of a custom decryption and deobfuscation routine in `fcn.004030fc` is used to hide the main payload's code/data from static analysis. |
| **T1543.003** | Windows Token Manipulation (for Privilege Escalation) | The calls to `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicate an attempt to gain specific system privileges (like `SeDebugPrivilege`) for broader access. |
| **T1547.001** | Registry Run Keys / Startup Folder | The interaction with registry keys via `RegSetValueExW` specifically targeting "Run" keys is a classic method for establishing persistence. |
| **T1497** | Virtualization/Sandbox Detection | The use of `GetTickCount` and multiple `Sleep` calls is designed to bypass automated sandboxes by delaying execution or detecting timing inconsistencies. |
| **T1036** | Masquerading | The inclusion of "NSIS Error" strings suggests the malware mimics a legitimate installer framework (Nullsoft Script Installer) to blend in with standard system software. |
| **T1105** | Ingress Tool Transfer | The movement of files into a `%TEMP%` directory via `CopyFileW` and `MoveFileExW` represents the "staging" phase where a primary payload is prepared for execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Because this is a "dropper" sample, many specific network indicators (IPs/URLs) are likely obfuscated or hidden until the second stage is executed.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **%TEMP%**: The analysis notes the use of `GetTempPathW` and `GetTempFileNameW` to stage and execute payloads in the Windows temporary directory.
*   **Registry Run Keys**: The report notes activity related to "Run" keys (implied by the mention of persistence), though specific keys were not explicitly listed in the string dump.

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **NSIS Framework**: The binary exhibits characteristics/strings associated with the **Nullsoft Script Installer (NSIS)**, which it may be leveraging or mimicking to wrap the initial loader.
*   **Decryption Routine**: A specific decryption routine is identified at function offset `fcn.004030fc` (and related data at `0x40769d`). 
*   **Privilege Escalation**: The binary utilizes `AdjustTokenPrivileges` and `LookupPrivilegeValueW`, indicating an attempt to escalate privileges for the final payload.
*   **Staging Behavior**: Use of `CopyFileW` and `MoveFileExW` to move internal resources into system-accessible folders before execution.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-Stage Execution & Obfuscation:** The binary contains a custom decryption routine (`fcn.004030fc`) and resource extraction logic designed to unpack a secondary payload into the `%TEMP%` directory, which is characteristic of a first-stage loader.
*   **Persistence & Privilege Escalation:** The use of `AdjustTokenPrivileges` and modifications to Windows "Run" keys indicate a clear intent to gain elevated permissions and ensure the final payload remains active on the host system.
*   **Evasion & Masquerading:** The inclusion of anti-analysis techniques (timing checks/sleeps) and the use of NSIS framework strings to mimic legitimate installer software are classic indicators of malware designed to bypass security controls and hide in plain sight.
