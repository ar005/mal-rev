# Threat Analysis Report

**Generated:** 2026-08-14 00:22 UTC
**Sample:** `0ec8881736114b83e3282ac546703a0a2f9d2a00d532e2a501e8c33437252f27_0ec8881736114b83e3282ac546703a0a2f9d2a00d532e2a501e8c33437252f27.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ec8881736114b83e3282ac546703a0a2f9d2a00d532e2a501e8c33437252f27_0ec8881736114b83e3282ac546703a0a2f9d2a00d532e2a501e8c33437252f27.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 699,128 bytes |
| MD5 | `81e4e8805aca09cd540e35bcead0490b` |
| SHA1 | `5a9d015e967928b538b89e005696704e0037b3d7` |
| SHA256 | `0ec8881736114b83e3282ac546703a0a2f9d2a00d532e2a501e8c33437252f27` |
| Overall entropy | 7.937 |
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
| `.text` | 26,112 | 6.467 | No |
| `.rdata` | 5,120 | 5.104 | No |
| `.data` | 1,536 | 4.03 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 23,552 | 4.373 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `lstrcmpiA`, `CreateFileW`, `GetTempFileNameW`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`

## Extracted Strings

Total strings found: **1626** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495L
tQWPV
Instuj
softua
NulluX	E
UVWj _3
L$bf-S
D$ Pj(
D$(Ph0
D$,UPU
tVj%UUU
D$$+D$
D$,+D$$P
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
| `fcn.00406aeb` | `0x406aeb` | 2642 | ✓ |
| `entry0` | `0x403557` | 1565 | ✓ |
| `fcn.00403c4e` | `0x403c4e` | 726 | ✓ |
| `fcn.004065b9` | `0x4065b9` | 625 | ✓ |
| `fcn.004030a9` | `0x4030a9` | 619 | ✓ |
| `fcn.00403314` | `0x403314` | 485 | ✓ |
| `fcn.00405c88` | `0x405c88` | 451 | ✓ |
| `fcn.004061c2` | `0x4061c2` | 378 | ✓ |
| `fcn.00402ed5` | `0x402ed5` | 234 | ✓ |
| `fcn.00405601` | `0x405601` | 211 | ✓ |
| `fcn.00404562` | `0x404562` | 207 | ✓ |
| `fcn.00404da8` | `0x404da8` | 201 | ✓ |
| `fcn.00403f24` | `0x403f24` | 185 | ✓ |
| `fcn.0040682a` | `0x40682a` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.004064dc` | `0x4064dc` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00406368` | `0x406368` | 129 | ✓ |
| `fcn.00404eb6` | `0x404eb6` | 128 | ✓ |
| `fcn.00405f53` | `0x405f53` | 126 | ✓ |
| `fcn.0040644a` | `0x40644a` | 121 | ✓ |
| `fcn.0040614d` | `0x40614d` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406900` | `0x406900` | 112 | ✓ |
| `fcn.00406a5d` | `0x406a5d` | 110 | ✓ |
| `fcn.004056d4` | `0x4056d4` | 108 | ✓ |
| `fcn.00405bdc` | `0x405bdc` | 100 | ✓ |
| `fcn.00403045` | `0x403045` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402ed5.c`](code/fcn.00402ed5.c)
- [`code/fcn.00403045.c`](code/fcn.00403045.c)
- [`code/fcn.004030a9.c`](code/fcn.004030a9.c)
- [`code/fcn.00403314.c`](code/fcn.00403314.c)
- [`code/fcn.00403c4e.c`](code/fcn.00403c4e.c)
- [`code/fcn.00403f24.c`](code/fcn.00403f24.c)
- [`code/fcn.00404562.c`](code/fcn.00404562.c)
- [`code/fcn.00404da8.c`](code/fcn.00404da8.c)
- [`code/fcn.00404eb6.c`](code/fcn.00404eb6.c)
- [`code/fcn.00405601.c`](code/fcn.00405601.c)
- [`code/fcn.004056d4.c`](code/fcn.004056d4.c)
- [`code/fcn.00405bdc.c`](code/fcn.00405bdc.c)
- [`code/fcn.00405c88.c`](code/fcn.00405c88.c)
- [`code/fcn.00405f53.c`](code/fcn.00405f53.c)
- [`code/fcn.0040614d.c`](code/fcn.0040614d.c)
- [`code/fcn.004061c2.c`](code/fcn.004061c2.c)
- [`code/fcn.00406368.c`](code/fcn.00406368.c)
- [`code/fcn.0040644a.c`](code/fcn.0040644a.c)
- [`code/fcn.004064dc.c`](code/fcn.004064dc.c)
- [`code/fcn.004065b9.c`](code/fcn.004065b9.c)
- [`code/fcn.0040682a.c`](code/fcn.0040682a.c)
- [`code/fcn.00406900.c`](code/fcn.00406900.c)
- [`code/fcn.00406a5d.c`](code/fcn.00406a5d.c)
- [`code/fcn.00406aeb.c`](code/fcn.00406aeb.c)

## Behavioral Analysis

Based on the disassembly provided, this binary is a complex **installer or packer**—likely built using the **NSIS (Nullsoft Script Installer)** framework, as evidenced by the "NSIS" error strings and common installer behaviors.

While many of these actions are standard for installation software, they are also techniques used by malware to unpack payloads, gain privileges, and establish persistence.

### Core Functionality and Purpose
The primary purpose of this code is to manage the **installation or unpacking** of a software package. It handles complex UI logic, file system extraction/renaming, registry modification, and environment preparation. 

It manages a "staging" area by:
1.  Moving files from an initial location (potentially a self-extracting archive).
2.  Renaming those files as they are "unpacked."
3.  Setting up local environment variables or system paths.

### Suspicious or Malicious Behaviors
While the code appears to be a standard installer, several segments exhibit behaviors commonly associated with **droppers** or **loaders**:

*   **Privilege Escalation/Manipulation:** The use of `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, and `OpenProcessToken` (seen in `entry0`) indicates the program is attempting to gain higher system privileges. While common for installers (to install drivers/system services), this is a frequent precursor to malware seeking full administrative control.
*   **File Extraction & Renaming:** The function `fcn.004061c2` specifically includes logic for renaming files and updating their metadata. In a malicious context, this is indicative of a "packer" unpacking a hidden payload (e.g., a Trojan or Ransomware) from an encrypted container into the filesystem.
*   **Process/System Interaction:** The use of `LoadImageW`, `CreateProcessW`, and `ShellExecuteW` indicates that the program can execute other binaries or load modules into its own memory space.
*   **Registry Modification:** Extensive use of `RegOpenKeyExW`, `RegSetValueExW`, and `RegEnumKeyW` shows the program interacts heavily with the Windows Registry, likely to create software shortcuts or modify system configuration keys (persistence).

### Notable Techniques and Patterns
*   **NSIS Framework Characteristics:** The presence of "NSIS" strings and specific string-handling routines suggests this is a standard installer. If this was found in a malware sample, it often means the malicious payload is "wrapped" inside a legitimate-looking installer to bypass basic security filters.
*   **Dynamic Resource Loading/Mapping:** Function `fcn.00403c4e` utilizes `LoadImageW`. This suggests the binary might be loading additional resources or modules into memory that are not part of the primary executable's initial image.
*   **Fallback Paths & Temp Files:** The code extensively uses `GetTempPathW`, `GetWindowsDirectoryW`, and `GetCurrentProcess`. It actively moves files to temporary directories before processing them, a common tactic to bypass some simple file-system monitors that only watch the original execution directory.
*   **Complexity of UI/Interaction:** The large switch case in `fcn.00401434` and the interaction with `COMCTL32.dll` indicate a sophisticated graphical user interface (GUI), which is often used to mask malicious activity behind "busy" progress bars or standard setup dialogs.

### Summary for Analyst
This sample is likely a **wrapper/installer**. While it performs many actions common in malware (privilege elevation, file unpacking, and persistence via registry), those behaviors are currently consistent with an installer designed by the NSIS framework. You should treat it as a potential "dropper" if it's found alongside suspicious payloads or if the files it extracts have unusual names/extensions.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1564.001 | Packing | The binary demonstrates packer behavior by extracting, renaming, and preparing hidden payloads from a "staging" area. |
| T1068 | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` and `OpenProcessToken` indicates an attempt to gain higher system privileges common in malware seeking administrative control. |
| T1112 | Modify Registry | Extensive interaction with registry keys is used to modify system configurations or establish persistence for the payload. |
| T1036.005 | Masquerading (User-Specified Software) | The use of the NSIS framework and a complex GUI masks malicious activities behind legitimate installer behaviors and "busy" progress indicators. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted intelligence. 

**Note:** As per your instructions, standard Windows API functions (e.g., `CreateProcessW`), system DLLs (e.g., `USER32.dll`), and generic installer behaviors have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. *(Note: While the analysis confirms the binary performs registry modifications and file movements, no specific hardcoded paths or registry keys were provided in the source text.)*

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Framework Identification:** The binary utilizes the **NSIS (Nullsoft Script Installer)** framework.
*   **Function Indicators:** 
    *   `fcn.004061c2`: Logic for file renaming and metadata updates (indicative of a packer/dropper).
    *   `fcn.00403c4e`: Utilizes `LoadImageW` for dynamic resource loading/mapping.
    *   `fcn.00401434`: Large switch case with `COMCTL32.dll` interaction (sophisticated GUI construction).

---
**Analyst Note:** 
The provided data contains **no actionable network or file-system IOCs**. The sample exhibits "high-signal" behavior for a **dropper** or **wrapper**, but the specific indicators (IPs, specific paths) are likely obfuscated or dynamically generated. This sample should be treated as suspicious due to its capability to escalate privileges and unpack payloads via the NSIS wrapper.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: Medium

**Key evidence**:
*   **Wrapper/Packer Behavior:** The sample utilizes the NSIS framework and exhibits classic "packer" traits, such as extracting files from a staging area, renaming them, and utilizing dynamic resource loading (`LoadImageW`) to hide the final payload.
*   **Privilege Escalation & Persistence:** The inclusion of `AdjustTokenPrivileges` (privilege escalation) combined with heavy registry manipulation indicates an intent to gain administrative control and establish persistence for a secondary payload.
*   **Masquerading as Legit Software:** The use of complex GUI components (`COMCTL32.dll`) and standard installer behaviors is designed to mask malicious activity behind a common "setup" interface, a hallmark of droppers meant to bypass initial security scrutiny.
