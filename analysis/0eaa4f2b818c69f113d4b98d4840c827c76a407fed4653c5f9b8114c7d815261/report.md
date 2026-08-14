# Threat Analysis Report

**Generated:** 2026-08-13 19:21 UTC
**Sample:** `0eaa4f2b818c69f113d4b98d4840c827c76a407fed4653c5f9b8114c7d815261_0eaa4f2b818c69f113d4b98d4840c827c76a407fed4653c5f9b8114c7d815261.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0eaa4f2b818c69f113d4b98d4840c827c76a407fed4653c5f9b8114c7d815261_0eaa4f2b818c69f113d4b98d4840c827c76a407fed4653c5f9b8114c7d815261.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 1,128,880 bytes |
| MD5 | `9ca004788dfd2fb17416ec00d5414148` |
| SHA1 | `36a59ee95b339f46a5a511faf3b487ca927fa985` |
| SHA256 | `0eaa4f2b818c69f113d4b98d4840c827c76a407fed4653c5f9b8114c7d815261` |
| Overall entropy | 7.976 |
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
| `.text` | 26,112 | 6.385 | No |
| `.rdata` | 5,120 | 5.027 | No |
| `.data` | 1,536 | 4.11 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 66,048 | 7.212 | ⚠️ Yes |

### Imports

**ADVAPI32.dll**: `RegEnumValueA`, `RegEnumKeyA`, `RegQueryValueExA`, `RegSetValueExA`, `RegCloseKey`, `RegDeleteValueA`, `RegDeleteKeyA`, `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, `OpenProcessToken`, `RegOpenKeyExA`, `RegCreateKeyExA`
**SHELL32.dll**: `SHGetPathFromIDListA`, `SHBrowseForFolderA`, `SHGetFileInfoA`, `SHFileOperationA`, `ShellExecuteExA`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoCreateInstance`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `SetDlgItemTextA`, `GetSystemMetrics`, `CreatePopupMenu`, `AppendMenuA`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcA`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorA`, `SetCursor`, `GetSysColor`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectA`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `CreateProcessA`, `RemoveDirectoryA`, `GetTempFileNameA`, `CreateDirectoryA`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceA`, `lstrcpynA`, `SetErrorMode`, `GetVersionExA`, `lstrlenA`, `GetCommandLineA`, `GetTempPathA`, `GetWindowsDirectoryA`

## Extracted Strings

Total strings found: **2728** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQVPW
Et@;u
vX95hCB
#VhQ.@
Instuj
softua
NulluX	E
tVj%WWW
D$$+D$
D$,+D$$P
u9=H	B
SSSSjn
us9Et	
8\tPV
u9utm
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
RegOpenKeyExA
RegCreateKeyExA
ADVAPI32.dll
SHFileOperationA
SHGetFileInfoA
SHBrowseForFolderA
SHGetPathFromIDListA
ShellExecuteExA
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
EndDialog
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5839 | ✓ |
| `fcn.00406965` | `0x406965` | 2642 | ✓ |
| `entry0` | `0x40352b` | 1508 | ✓ |
| `fcn.00402f88` | `0x402f88` | 724 | ✓ |
| `fcn.00403c01` | `0x403c01` | 709 | ✓ |
| `fcn.0040648b` | `0x40648b` | 615 | ✓ |
| `fcn.00405bba` | `0x405bba` | 464 | ✓ |
| `fcn.00406061` | `0x406061` | 368 | ✓ |
| `fcn.00403364` | `0x403364` | 361 | ✓ |
| `fcn.0040325c` | `0x40325c` | 264 | ✓ |
| `fcn.00402d67` | `0x402d67` | 234 | ✓ |
| `fcn.0040553c` | `0x40553c` | 210 | ✓ |
| `fcn.004044ff` | `0x4044ff` | 207 | ✓ |
| `fcn.00404ce1` | `0x404ce1` | 197 | ✓ |
| `fcn.00403ec6` | `0x403ec6` | 185 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00402ee9` | `0x402ee9` | 159 | ✓ |
| `fcn.004066f2` | `0x4066f2` | 153 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.0040636f` | `0x40636f` | 137 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.004061fd` | `0x4061fd` | 129 | ✓ |
| `fcn.00404deb` | `0x404deb` | 128 | ✓ |
| `fcn.00405e78` | `0x405e78` | 120 | ✓ |
| `fcn.004062df` | `0x4062df` | 119 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004068d7` | `0x4068d7` | 110 | ✓ |
| `fcn.004067b2` | `0x4067b2` | 110 | ✓ |
| `fcn.0040560e` | `0x40560e` | 108 | ✓ |
| `fcn.00405b0e` | `0x405b0e` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402d67.c`](code/fcn.00402d67.c)
- [`code/fcn.00402ee9.c`](code/fcn.00402ee9.c)
- [`code/fcn.00402f88.c`](code/fcn.00402f88.c)
- [`code/fcn.0040325c.c`](code/fcn.0040325c.c)
- [`code/fcn.00403364.c`](code/fcn.00403364.c)
- [`code/fcn.00403c01.c`](code/fcn.00403c01.c)
- [`code/fcn.00403ec6.c`](code/fcn.00403ec6.c)
- [`code/fcn.004044ff.c`](code/fcn.004044ff.c)
- [`code/fcn.00404ce1.c`](code/fcn.00404ce1.c)
- [`code/fcn.00404deb.c`](code/fcn.00404deb.c)
- [`code/fcn.0040553c.c`](code/fcn.0040553c.c)
- [`code/fcn.0040560e.c`](code/fcn.0040560e.c)
- [`code/fcn.00405b0e.c`](code/fcn.00405b0e.c)
- [`code/fcn.00405bba.c`](code/fcn.00405bba.c)
- [`code/fcn.00405e78.c`](code/fcn.00405e78.c)
- [`code/fcn.00406061.c`](code/fcn.00406061.c)
- [`code/fcn.004061fd.c`](code/fcn.004061fd.c)
- [`code/fcn.004062df.c`](code/fcn.004062df.c)
- [`code/fcn.0040636f.c`](code/fcn.0040636f.c)
- [`code/fcn.0040648b.c`](code/fcn.0040648b.c)
- [`code/fcn.004066f2.c`](code/fcn.004066f2.c)
- [`code/fcn.004067b2.c`](code/fcn.004067b2.c)
- [`code/fcn.004068d7.c`](code/fcn.004068d7.c)
- [`code/fcn.00406965.c`](code/fcn.00406965.c)

## Behavioral Analysis

Based on the disassembly and the associated strings, here is an analysis of the binary's functionality:

### Core Functionality and Purpose
The code appears to be a **multi-stage installer or an automated setup script/wrapper**. It exhibits many characteristics common in installers created with tools like NSIS (Nullsoft Script Installer). Its primary purpose is to verify the system environment, extract files to temporary locations, perform integrity checks on those files, and register configurations in the Windows Registry.

### Suspicious or Malicious Behaviors
While much of the behavior is consistent with a legitimate installer, several patterns are notable from a security perspective:

*   **Environment Manipulation & Persistence:** 
    *   The code actively queries and potentially modifies environment variables (e.g., "TEMP") to ensure it has a valid location for file operations.
    *   It performs extensive Registry interaction (`Advapi32.dll`). It reads, creates, and sets values in various registry keys, which is a common method for ensuring software persists or remains configured after a reboot.
*   **File Manipulation & Dropping:** 
    *   The code performs "Move," "Copy," and "Delete" operations on files (e.g., `fcn.00405bba`). In an installer context, this is for extracting payload components; in malware, this is used to drop malicious executables or clear "tracks."
    *   It uses temporary directories as a staging area for these files before they are moved to their final locations.
*   **Integrity Checks:** 
    *   The function `fcn.004068d7` implements a checksum/CRC algorithm (visible through the bit-shifting and XORing logic). This is used to ensure that the data being extracted hasn't been tampered with or corrupted, which is standard for installers but also used by malware to verify its own components.
*   **System Information Gathering:** 
    *   The binary checks the system version (`GetVersionExA`) and probes for specific system files/folders (like those related to `UXTHEME`). This can be used as an "anti-analysis" or "compatibility check" to see if the OS is a standard consumer installation.

### Notable Techniques & Patterns
*   **NSIS Framework:** The presence of strings like `"NSIS Error"`, `"nsis.sf.net"`, and `"Error writing temporary file"` strongly suggests that this binary was built using the **Nullsoft Script Installer**. This makes it likely to be a "wrapper"—it wraps a payload (which could be legitimate or malicious) in a standard installer interface.
*   **Robust File Handling:** The code contains complex logic for handling paths, including stripping quotes and resolving relative paths. This indicates it is designed to handle complex file system operations reliably.
*   **UI Construction:** Several functions involve `MessageBoxIndirectA` and `SetDlgItemTextA`. These are used to interact with the user or display error messages if a step in the installation/execution process fails.

### Summary for Analyst
This binary is likely an **installer wrapper**. While it possesses "suspicious" traits like registry manipulation and file moving, these are currently standard behaviors of installation scripts. However, because this is often used as a delivery mechanism, you should treat the files it extracts or moves as the primary targets for further analysis.

**Key Indicators:**
*   **Type:** Installer / Wrapper
*   **Techniques:** Registry modification, File system manipulation (Drop/Move), Integrity checking (CRC32-like).
*   **Potential Risk:** High (as a delivery vehicle for other payloads).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547** | Boot or Logon Autostart Execution | The analysis notes that the binary performs extensive registry interactions specifically to ensure the software persists after a reboot. |
| **T1213** | System Information Discovery | The binary uses `GetVersionExA` and probes specific system folders to gather information about the environment and compatibility. |
| **T1070** | Indicator Removal | The analysis identifies delete operations used to "clear tracks," a common method for removing traces of malicious activity or artifacts. |
| **T1036** | Modify Registry | The binary performs various `Advapi32.dll` calls to create and set values in registry keys for configuration purposes. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** As per your instructions, standard Windows system paths and common API library names have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   *None identified.* (The domain `nsis.sf.net` mentioned in the analysis refers to the legitimate Nullsoft Script Installer framework and is not an indicator of a malicious C2 or phishing site).

### **File paths / Registry keys**
*   *None identified.* (All registry keys listed, such as `Software\Microsoft\Windows\CurrentVersion` and `Control Panel\Desktop\ResourceLocale`, are standard Windows system paths).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (The strings `fcn.00405bba` and `fcn.004068d7` appear to be internal function offsets from a disassembler rather than file hashes).

### **Other artifacts**
*   **Framework/Wrapper Identification:** 
    *   **NSIS (Nullsoft Script Installer):** The presence of strings `"NSIS Error"` and `"nsis.sf.net"` identifies the binary as an installer wrapper. While not a direct indicator of a specific malicious campaign, it identifies the delivery mechanism.
*   **Behavioral Patterns:** 
    *   **CRC32-like Integrity Check:** Logic identified at `fcn.004068d7` for verifying payload integrity during extraction.
    *   **Staging Behavior:** Use of temporary directories to move and rename files before final execution.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: Medium

4. **Key evidence**:
*   **NSIS Framework Usage:** The presence of strings like `"NSIS Error"` and `"nsis.sf.net"` confirms the binary is an NSIS installer wrapper, a common method for delivering and installing payloads onto a target system.
*   **Dropper/Loader Behavior:** The analysis highlights typical "wrapper" behaviors, including extracting files to temporary directories (staging), performing integrity checks (CRC32), and modifying registry keys (`T1036`) to establish persistence (`T1547`).
*   **Inconclusive Payload:** While the behavior is consistent with a malicious delivery vehicle, no specific malware payload (e.g., a known RAT or Botnet) was identified in the provided text, necessitating an "Unknown" family classification and "Medium" confidence.
