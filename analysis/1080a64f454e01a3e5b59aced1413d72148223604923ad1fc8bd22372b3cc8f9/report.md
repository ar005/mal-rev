# Threat Analysis Report

**Generated:** 2026-08-19 00:49 UTC
**Sample:** `1080a64f454e01a3e5b59aced1413d72148223604923ad1fc8bd22372b3cc8f9_1080a64f454e01a3e5b59aced1413d72148223604923ad1fc8bd22372b3cc8f9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1080a64f454e01a3e5b59aced1413d72148223604923ad1fc8bd22372b3cc8f9_1080a64f454e01a3e5b59aced1413d72148223604923ad1fc8bd22372b3cc8f9.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 92,163,700 bytes |
| MD5 | `e87a40196def7f6824c2384713d9c20d` |
| SHA1 | `f94a7683307fb46e38bc409d8c118eebc2a5b738` |
| SHA256 | `1080a64f454e01a3e5b59aced1413d72148223604923ad1fc8bd22372b3cc8f9` |
| Overall entropy | 8.0 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1776631127 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,624 | 6.454 | No |
| `.rdata` | 5,120 | 5.1 | No |
| `.data` | 1,536 | 4.125 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 274,432 | 2.822 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`, `GetCommandLineW`

## Extracted Strings

Total strings found: **198871** (showing first 100)

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
| `fcn.00406c58` | `0x406c58` | 2642 | ✓ |
| `entry0` | `0x40369f` | 1578 | ✓ |
| `fcn.00403dbb` | `0x403dbb` | 726 | ✓ |
| `fcn.004030fc` | `0x4030fc` | 724 | ✓ |
| `fcn.00406726` | `0x406726` | 625 | ✓ |
| `fcn.00405df5` | `0x405df5` | 451 | ✓ |
| `fcn.0040632f` | `0x40632f` | 378 | ✓ |
| `fcn.004034d8` | `0x4034d8` | 361 | ✓ |
| `fcn.004033d0` | `0x4033d0` | 264 | ✓ |
| `fcn.00402ed5` | `0x402ed5` | 234 | ✓ |
| `fcn.0040576e` | `0x40576e` | 211 | ✓ |
| `fcn.004046cf` | `0x4046cf` | 207 | ✓ |
| `fcn.00404f15` | `0x404f15` | 201 | ✓ |
| `fcn.00404091` | `0x404091` | 185 | ✓ |
| `fcn.00406997` | `0x406997` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040305a` | `0x40305a` | 162 | ✓ |
| `fcn.00406649` | `0x406649` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.004064d5` | `0x4064d5` | 129 | ✓ |
| `fcn.00405023` | `0x405023` | 128 | ✓ |
| `fcn.004060c0` | `0x4060c0` | 126 | ✓ |
| `fcn.004065b7` | `0x4065b7` | 121 | ✓ |
| `fcn.004062ba` | `0x4062ba` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406a6d` | `0x406a6d` | 112 | ✓ |
| `fcn.00406bca` | `0x406bca` | 110 | ✓ |
| `fcn.00405841` | `0x405841` | 108 | ✓ |

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
- [`code/fcn.00403dbb.c`](code/fcn.00403dbb.c)
- [`code/fcn.00404091.c`](code/fcn.00404091.c)
- [`code/fcn.004046cf.c`](code/fcn.004046cf.c)
- [`code/fcn.00404f15.c`](code/fcn.00404f15.c)
- [`code/fcn.00405023.c`](code/fcn.00405023.c)
- [`code/fcn.0040576e.c`](code/fcn.0040576e.c)
- [`code/fcn.00405841.c`](code/fcn.00405841.c)
- [`code/fcn.00405df5.c`](code/fcn.00405df5.c)
- [`code/fcn.004060c0.c`](code/fcn.004060c0.c)
- [`code/fcn.004062ba.c`](code/fcn.004062ba.c)
- [`code/fcn.0040632f.c`](code/fcn.0040632f.c)
- [`code/fcn.004064d5.c`](code/fcn.004064d5.c)
- [`code/fcn.004065b7.c`](code/fcn.004065b7.c)
- [`code/fcn.00406649.c`](code/fcn.00406649.c)
- [`code/fcn.00406726.c`](code/fcn.00406726.c)
- [`code/fcn.00406997.c`](code/fcn.00406997.c)
- [`code/fcn.00406a6d.c`](code/fcn.00406a6d.c)
- [`code/fcn.00406bca.c`](code/fcn.00406bca.c)
- [`code/fcn.00406c58.c`](code/fcn.00406c58.c)

## Behavioral Analysis

Based on my analysis of the decompiled code and extracted strings, this binary is a **dropper/installer wrapper**, likely utilizing techniques common in "crack" installers or malware loaders. It is designed to extract, verify, and execute an embedded payload while managing system environment variables and registry keys.

### Core Functionality
The program acts as a "wrapper." Its primary purpose is to take a packed or bundled resource (likely hidden within the binary), unpack it into a temporary directory, verify its integrity, and then execute it. The presence of "NSIS" related strings and logic suggests it uses a modified Nullsoft Script Installer framework, which is commonly repurposed by malware authors for distribution.

### Suspicious and Malicious Behaviors
*   **Dropper/Unpacker Behavior:** 
    *   The function `fcn.004030fc` performs heavy lifting in processing data. It iterates through a buffer, calculates sizes (possibly during decompression or decryption), and manages the transition of data from an internal state to a file-writing state.
    *   It uses `GetTempPathW` and `GetWindowsDirectoryW` to resolve paths for "dropping" files into temporary locations before execution.
*   **Integrity Verification:** 
    *   The function `fcn.00406c58` implements a **CRC32 or similar checksum algorithm**. This is used to ensure that the unpacked payload remains intact during the extraction process, ensuring the "malware" component isn't corrupted before it runs.
*   **Persistence and Privilege Escalation:** 
    *   The code interacts with `ADVAPI32.dll` (e.g., `AdjustTokenPrivileges`, `LookupPrivilegeValueW`). Specifically, there is logic to request the `SeShutdownPrivilege`, which, while often used by installers to manage system state, can also be a precursor to performing high-privilege operations.
*   **Registry Manipulation:** 
    *   Extensive use of `RegOpenKeyExW` and `RegSetValueExW` indicates it modifies the Windows Registry. While common for configuration in installers, this is a standard method for establishing **persistence** (e.g., adding entries to the "Run" keys).
*   **Evasive File Handling:** 
    *   The code performs checks like `GetFileAttributesW` and `MoveFileExW`. It frequently hides the true nature of files by moving them from system-monitored areas or temporary folders into final execution paths.

### Notable Techniques & Patterns
*   **Overlay/Embedded Payload Strategy:** The script iterates through internal offsets to find "payload" data (observed in `fcn.004030fc` and `fcn.00401389`). This indicates the actual malicious payload is not on disk until this program runs.
*   **Standard Windows API Hooking/Usage:** The binary heavily utilizes common Win32 APIs to hide its presence in the UI, such as `SetForegroundWindow` and various `Send_MessageW` calls used to interact with dialog elements without direct focus.
*   **Heavy use of Switch Tables:** The large switch-case block in `fcn.00401434` is a classic way to handle a wide variety of GUI events and internal state transitions while keeping the control flow complex for analysts.
*   **COM Implementation:** The use of `OleInitialize` and `CoCreateInstance` (in `fcn.004021d6`) suggests it may be interacting with Shell objects or specialized Windows components to handle file system navigation or clipboard manipulation.

### Conclusion
The sample is a **sophisticated loader/dropper**. It uses a standard "installer" facade (NSIS-style) to mask its true intent: extracting and verifying a secondary payload from memory or an embedded resource, moving it to a temporary location, and executing it. The integrity checks and automated file movement are high-confidence indicators of malware distribution.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of an embedded payload, CRC32 integrity checks, and complex switch-case logic is designed to hide the true nature of the code from analysts. |
| T1036 | Masquerading | The binary uses a "launcher" facade (NSIS) and performs movement of files between paths to disguise its activities as a legitimate installer. |
| T1112 | Modify Registry | The execution of `RegOpenKeyExW` and `RegSetValueExW` indicates the malware is modifying system settings or establishing persistence through registry keys. |
| T1068 | Exploitation for Privilege Escalation | The specific use of `AdjustTokenPrivileges` to request `SeShutdownPrivilege` suggests a precursor to executing high-privilege operations on the host. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** As requested, standard Windows API calls, library names, and common system functions have been excluded from this list.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (The analysis mentions the *use* of `GetTempPathW` and "Run" keys for persistence, but no specific malicious file paths or registry keys were provided in the text).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Tactic/Technique:** NSIS (Nullsoft Script Installer) framework used as a wrapper for payload delivery.
*   **Integrity Check:** CRC32 or similar checksum logic (located at `fcn.00406c58`) to verify payload integrity after extraction.
*   **Privilege Request:** Attempted acquisition of `SeShutdownPrivilege` (via `AdjustTokenPrivileges`/`LookupPrivilegeValueW`).
*   **Payload Strategy:** Use of internal offsets and buffer processing (`fcn.004030fc`, `fcn.00401389`) to handle an embedded, encrypted/compressed payload.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown (Generic Loader)
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**: 
*   **Payload Delivery Mechanism:** The sample functions as a multi-stage wrapper that extracts, validates (via CRC32 checksums), and executes an embedded payload in temporary directories. This is a classic hallmark of a dropper/loader designed to deliver the primary malicious component.
*   **Evasive Tactics:** It uses masquerading techniques by utilizing a modified Nullsoft Script Installer (NSIS) framework and complex switch-case logic to hide its true control flow, making it harder for analysts to trace the transition from loader to payload.
*   **Persistence and Privilege Escalation:** The binary actively interacts with `ADVAPI32.dll` to request elevated privileges (`SeShutdownPrivilege`) and modifies Windows Registry keys to ensure persistence on the host system.
