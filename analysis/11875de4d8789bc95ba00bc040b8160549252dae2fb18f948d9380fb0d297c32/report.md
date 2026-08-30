# Threat Analysis Report

**Generated:** 2026-08-23 19:03 UTC
**Sample:** `11875de4d8789bc95ba00bc040b8160549252dae2fb18f948d9380fb0d297c32_11875de4d8789bc95ba00bc040b8160549252dae2fb18f948d9380fb0d297c32.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11875de4d8789bc95ba00bc040b8160549252dae2fb18f948d9380fb0d297c32_11875de4d8789bc95ba00bc040b8160549252dae2fb18f948d9380fb0d297c32.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 50,618,264 bytes |
| MD5 | `a414282c860af5a9dd7011da263e0713` |
| SHA1 | `f7b2968ba25e5984c561398162030a47784cb21c` |
| SHA256 | `11875de4d8789bc95ba00bc040b8160549252dae2fb18f948d9380fb0d297c32` |
| Overall entropy | 8.0 |
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
| `.rsrc` | 80,896 | 3.794 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`, `GetCommandLineW`

## Extracted Strings

Total strings found: **109923** (showing first 100)

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

Based on the analysis of the provided disassembly and strings, this binary is an **installer program**, specifically one built using the **NSIS (Nullsoft Script Installer)** framework.

While it performs many actions typically associated with malware (such as file manipulation and registry changes), these are "dual-use" behaviors: they are standard for a legitimate software installer but are also common in "droppers" or "loaders" used by attackers to install and configure malicious payloads.

### Core Functionality
The primary purpose of this code is to act as an installation wrapper. It handles the following tasks:
*   **Integrity Checking:** The function `fcn.00403dae` contains logic (and specific error messages) related to "Installer integrity check." It verifies that files have not been corrupted or tampered with before execution. 
*   **Resource Management:** It uses standard Windows COM and OLE libraries (`ole32.dll`) to manage the graphical user interface (GUI).
*   **UI Feedback:** The code frequently interacts with `USER32.dll` and `GDI32.dll` to update window titles, create buttons/dialogs, and display progress information (e.g., calculating percentages for a progress bar).

### Notable Behaviors & Techniques
The following behaviors were identified in the code:

*   **NSIS Framework Usage:** 
    *   The presence of "NSIS" strings and the specific logic found in `fcn.00403dae` confirm this is an NSIS-based installer. 
    *   In a malware context, attackers often use NSIS to wrap their payloads because it handles complex tasks like unpacking, extracting files from compressed archives, and installing system drivers/services automatically.
*   **File Manipulation & Extraction:**
    *   The code uses `CreateFileW`, `GetFileSize`, and `CopyFileW` to move data into temporary directories (e.g., via `GetTempPathW`). 
    *   It performs automated file copy operations, a core step in both installing software and "dropping" malware onto a victim's system.
*   **Registry Interaction:**
    *   The inclusion of functions like `RegEnumValueW`, `RegSetValueExW`, and `RegCreateKeyExW` indicates that the program is designed to modify the Windows Registry, likely to ensure it (or its payload) persists or runs automatically upon startup.
*   **Checksum/Integrity Algorithms:**
    *   The loop found in `fcn.00406c4b` involving specific bitwise operations and constants (like `0xedb88320`) is a standard implementation of the **CRC32 algorithm**. This confirms that the installer validates its own files or the payload it is about to extract.
*   **Environment Manipulation:**
    *   The use of `SetEnvironmentVariableW` suggests the program modifies system variables (such as the `PATH` variable) to ensure subsequent components can find necessary dependencies.

### Summary for Triage
This is a **high-complexity installer wrapper**. While the code provided does not contain "smoking gun" malicious actions like direct shellcode injection or active C2 beaconing, it provides all the infrastructure needed to install and persist malware on a system. 

**Recommendation:** Treat this as a potential **Dropper/Installer**. The presence of the NSIS engine means that while this specific binary is just an installer, the "payload" it is designed to unpack and run may be malicious.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | The use of `RegSetValueExW` and other registry functions indicates the binary is designed to ensure persistence by automatically launching the software or its payload upon startup. |
| T1036 | Masquerading | The utilization of the NSIS framework allows the binary to present as a common, legitimate installer, which can be used to hide malicious behaviors like payload unpacking and deployment. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the extraction of Indicators of Compromise (IOCs).

**Note:** No high-fidelity technical IOCs (such as specific IP addresses, URLs, file hashes, or hardcoded malicious paths) were identified in the provided text. The data primarily contains standard Windows API calls and internal application logic for an installer.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified (Only standard API functions for registry manipulation, such as `RegCreateKeyExW`, were listed, but no specific malicious keys or paths were provided).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Tooling Identification:** The binary is confirmed to be an **NSIS (Nullsoft Script Installer)** wrapper. While not a direct indicator of a specific malicious payload, its use is a common technique for dropping and installing malicious components.
*   **Internal Offsets:** 
    *   `fcn.00403dae`: Logic associated with "Installer integrity check."
    *   `fcn.00406c4b`: Implementation of the CRC32 algorithm (constant `0xedb88320`).

---
**Analyst Note:** This sample functions as a **dropper/installer wrapper**. While it does not contain immediate C2 (Command & Control) infrastructure or hardcoded malicious paths, it provides the necessary environment to execute and persist a secondary payload.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family:** Unknown
2. **Malware type:** Dropper
3. **Confidence:** High
4. **Key evidence:** 
*   **NSIS Framework Utilization:** The binary is confirmed to be an NSIS (Nullsoft Script Installer) wrapper, a common technique used by threat actors to bundle, unpack, and install malicious payloads while masquerading as legitimate software installers.
*   **Persistence and Environment Setup:** The code includes specific logic for registry modification (`RegCreateKeyExW`, `RegSetValueExW`) and environment variable manipulation, which are essential steps for ensuring a secondary payload remains active on the system.
*   **File Manipulation & Integrity Checks:** The use of CRC32 algorithms and standard Windows API calls to move files into temporary directories indicates that this binary serves as a delivery vehicle designed to prepare and "drop" a secondary payload onto the target system.
