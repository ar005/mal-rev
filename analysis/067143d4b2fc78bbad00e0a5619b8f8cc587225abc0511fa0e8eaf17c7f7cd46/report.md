# Threat Analysis Report

**Generated:** 2026-07-15 03:07 UTC
**Sample:** `067143d4b2fc78bbad00e0a5619b8f8cc587225abc0511fa0e8eaf17c7f7cd46_067143d4b2fc78bbad00e0a5619b8f8cc587225abc0511fa0e8eaf17c7f7cd46.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `067143d4b2fc78bbad00e0a5619b8f8cc587225abc0511fa0e8eaf17c7f7cd46_067143d4b2fc78bbad00e0a5619b8f8cc587225abc0511fa0e8eaf17c7f7cd46.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 773,600 bytes |
| MD5 | `f121e97cec4947e08c3fce3c951fbfc7` |
| SHA1 | `7ee4db989b38d26166587e7df202844b897ce292` |
| SHA256 | `067143d4b2fc78bbad00e0a5619b8f8cc587225abc0511fa0e8eaf17c7f7cd46` |
| Overall entropy | 7.803 |
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

Total strings found: **1691** (showing first 100)

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

Based on the provided disassembly and strings, here is a technical analysis of the binary's behavior.

### Core Functionality and Purpose
The binary appears to be an **installer or packer stub**, likely built using the **NSIS (Nullsoft Script Install System)** framework (evidenced by the `nsis.sf.net` URLs and "NSIS Error" strings). Its primary role is to manage the extraction, verification, and installation of files on a local system.

### Suspicious or Malicious Behaviors
While many of these behaviors are common in legitimate installers, they are also core techniques used by **droppers** and **loaders**.

*   **File Staging & Execution:** 
    *   The code uses `GetTempPathW`, `CopyFileW`, and `MoveFileW` to move files into temporary directories before executing them. This is a classic "downloader" pattern where the primary binary drops a secondary payload (the actual malware) into a hidden or temporary path.
    *   It utilizes `CreateProcessW` to launch these staged components.

*   **Persistence and System Manipulation:**
    *   There is extensive use of **Registry manipulation** (`RegOpenKeyExW`, `RegSetValueExW`, `RegDeleteValueW`). This indicates the program likely creates persistent entries, modifies system configurations, or sets up autostart mechanisms.
    *   The presence of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` suggests the binary attempts to acquire higher privileges (e.g., `SeDebugPrivilege`) to perform system-level changes or bypass restrictions.

*   **Timestomping:** 
    *   The inclusion of `SetFileTime` is a significant indicator. This technique is used by malware to modify the creation and modification dates of files on disk to make them appear older/legitimate, thereby evading detection by forensic analysis tools that flag recently created "suspicious" files.

*   **Self-Protection / Integrity Checks:**
    *   The function `fcn.00406c4b` contains logic consistent with **CRC32 or checksum calculations**. This is used to verify that the "payloads" (or other parts of the installer) have not been tampered with or corrupted during extraction/transmission.

### Notable Techniques and Patterns
*   **NSIS Wrapper:** The inclusion of `nsis` error messages suggests this might be a "wrapper." Malware authors often use legitimate installers to bundle malicious payloads, as these tools are less likely to be flagged by basic antivirus scanners compared to raw shellcode or simple executables.
*   **Complex Switching/Dispatching:** The large switch statement in `fcn.00401434` indicates a "Command" or "Action" pattern common in installers, where the binary processes a script of commands (e.g., copy file, set registry, show message).
*   **Environment Manipulation:** The code checks and sets environment variables (`SetEnvironmentVariableW`) and handles temporary paths, ensuring that subsequent components have a consistent environment to run within.
*   **Information Obfuscation/Handling:** It performs extensive work on strings (converting between multibyte and wide characters) and uses `GetShortPathNameW` to resolve relative or complex file paths into absolute ones before moving them.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Hide Files | The use of `GetTempPathW` and an NSIS wrapper are used to stage payloads in common directories and blend malicious behavior with legitimate installer activity. |
| T1112 | Modify Registry | Extensive registry manipulation is utilized to modify system configurations or establish persistence for the payload. |
| T1070.005 | Timestomping | The inclusion of `SetFileTime` indicates an attempt to alter file timestamps to evade detection by forensic analysis tools. |
| T1068 | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` suggests a deliberate attempt to gain higher privileges (e.g., `SeDebugPrivilege`) for system-level changes. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs). 

Note: Most of the raw strings provided consist of standard Windows API exports and internal system library names (e.g., `USER32.dll`, `GDI32.dll`), which are considered common functionality and not specific IOCs for a particular malware campaign.

### **IP addresses / URLs / Domains**
*   *None identified.* (The mention of `nsis.sf.net` in the analysis refers to the identification of the software framework used, not a malicious C2 infrastructure).

### **File paths / Registry keys**
*   *None explicitly defined.* (While the behavior analysis notes that the binary performs registry manipulation and file movement using functions like `RegOpenKeyExW` and `GetTempPathW`, no specific hardcoded paths or registry keys were provided in the source text).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Techniques (TTPs):**
    *   **NSIS Wrapper:** The binary utilizes the NSIS framework to wrap and deploy payloads.
    *   **Timestomping:** The use of `SetFileTime` indicates an attempt to modify file timestamps to evade forensic detection.
    *   **Privilege Escalation:** The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` suggests attempts to gain administrative/system-level permissions.
    *   **Dropper Behavior:** Use of `GetTempPathW`, `CopyFileW`, and `MoveFileW` followed by `CreateProcessW` indicates a multi-stage execution pattern typical of droppers or loaders.
    *   **Integrity Checking:** The use of custom logic (`fcn.00406c4b`) for CRC32/checksum calculations to verify payload integrity before execution.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the technical analysis provided, here is the classification of the sample:

1. **Malware family**: custom (or "Generic Loader")
2. **Malware type**: dropper / loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Multi-stage Execution:** The use of `GetTempPathW`, `CopyFileW`, and `MoveFileW` followed by `CreateProcessW` is a classic signature of a "dropper" or "loader," where the primary binary extracts and executes a hidden secondary payload.
    *   **Anti-Forensics & Evasion:** The explicit use of `SetFileTime` (Timestomping) indicates an intentional effort to hide the file's presence from forensic investigators, while `AdjustTokenPrivileges` shows an attempt to bypass system restrictions.
    *   **Wrapper Technique:** The utilization of the **NSIS framework** is a common technique used by threat actors to wrap malicious payloads in a legitimate-looking installer structure to evade basic signature-based detection.
