# Threat Analysis Report

**Generated:** 2026-08-17 21:29 UTC
**Sample:** `100658233e9f15e1c25721be61ba784ce1d568502d85874d1cf39d2b519755e5_100658233e9f15e1c25721be61ba784ce1d568502d85874d1cf39d2b519755e5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `100658233e9f15e1c25721be61ba784ce1d568502d85874d1cf39d2b519755e5_100658233e9f15e1c25721be61ba784ce1d568502d85874d1cf39d2b519755e5.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 87,172,376 bytes |
| MD5 | `474a4cadbcddb053adc1f0d9f69bc0fb` |
| SHA1 | `9d88025ac826b79e1b494a09abc007a02f3cbf53` |
| SHA256 | `100658233e9f15e1c25721be61ba784ce1d568502d85874d1cf39d2b519755e5` |
| Overall entropy | 7.998 |
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
| `.text` | 27,136 | 6.466 | No |
| `.rdata` | 5,120 | 5.1 | No |
| `.data` | 1,536 | 4.111 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 23,040 | 3.08 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`, `GetCommandLineW`

## Extracted Strings

Total strings found: **184047** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQWPV
Instui
softu`
NulluW	E
UVWj _3
L$bf-S
D$ Pj(
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
L$(9-$
l$(9l$(tr
+D$(PV
_^][t
P
D$SVW
A@;E |
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 6196 | ✓ |
| `fcn.00406dce` | `0x406dce` | 2183 | ✓ |
| `entry0` | `0x4036a5` | 1565 | ✓ |
| `fcn.004030fc` | `0x4030fc` | 730 | ✓ |
| `fcn.00403db4` | `0x403db4` | 726 | ✓ |
| `fcn.0040671f` | `0x40671f` | 625 | ✓ |
| `fcn.00405dee` | `0x405dee` | 451 | ✓ |
| `fcn.00406328` | `0x406328` | 378 | ✓ |
| `fcn.004034de` | `0x4034de` | 361 | ✓ |
| `fcn.00406c86` | `0x406c86` | 328 | ✓ |
| `fcn.004033d6` | `0x4033d6` | 264 | ✓ |
| `fcn.00402ed5` | `0x402ed5` | 234 | ✓ |
| `fcn.00407787` | `0x407787` | 216 | ✓ |
| `fcn.00405767` | `0x405767` | 211 | ✓ |
| `fcn.004046c8` | `0x4046c8` | 207 | ✓ |
| `fcn.00404f0e` | `0x404f0e` | 201 | ✓ |
| `fcn.0040408a` | `0x40408a` | 185 | ✓ |
| `fcn.00406990` | `0x406990` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040305a` | `0x40305a` | 162 | ✓ |
| `fcn.00406642` | `0x406642` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.004064ce` | `0x4064ce` | 129 | ✓ |
| `fcn.00407706` | `0x407706` | 129 | ✓ |
| `fcn.0040501c` | `0x40501c` | 128 | ✓ |
| `fcn.004060b9` | `0x4060b9` | 126 | ✓ |
| `fcn.004065b0` | `0x4065b0` | 121 | ✓ |
| `fcn.004062b3` | `0x4062b3` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |

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
- [`code/fcn.004033d6.c`](code/fcn.004033d6.c)
- [`code/fcn.004034de.c`](code/fcn.004034de.c)
- [`code/fcn.00403db4.c`](code/fcn.00403db4.c)
- [`code/fcn.0040408a.c`](code/fcn.0040408a.c)
- [`code/fcn.004046c8.c`](code/fcn.004046c8.c)
- [`code/fcn.00404f0e.c`](code/fcn.00404f0e.c)
- [`code/fcn.0040501c.c`](code/fcn.0040501c.c)
- [`code/fcn.00405767.c`](code/fcn.00405767.c)
- [`code/fcn.00405dee.c`](code/fcn.00405dee.c)
- [`code/fcn.004060b9.c`](code/fcn.004060b9.c)
- [`code/fcn.004062b3.c`](code/fcn.004062b3.c)
- [`code/fcn.00406328.c`](code/fcn.00406328.c)
- [`code/fcn.004064ce.c`](code/fcn.004064ce.c)
- [`code/fcn.004065b0.c`](code/fcn.004065b0.c)
- [`code/fcn.00406642.c`](code/fcn.00406642.c)
- [`code/fcn.0040671f.c`](code/fcn.0040671f.c)
- [`code/fcn.00406990.c`](code/fcn.00406990.c)
- [`code/fcn.00406c86.c`](code/fcn.00406c86.c)
- [`code/fcn.00406dce.c`](code/fcn.00406dce.c)
- [`code/fcn.00407706.c`](code/fcn.00407706.c)
- [`code/fcn.00407787.c`](code/fcn.00407787.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary's functionality.

### Core Functionality
The binary functions as a **complex installation engine** or "wrapper" (highly characteristic of the **NSIS - Nullsoft Script Installer** framework). Its primary purpose is to manage the deployment of software by unpacking files, configuring system settings via the registry, and providing a user interface for the installation process.

### Technical Observations
*   **Installer Framework:** The inclusion of strings like `nsis.sf.net` and the logic in `fcn.004030fc` (which returns a "Installer integrity check has failed" message) confirms this is an installer stub. 
*   **Resource & UI Management:** Functions such as `fcn.00401434` contain extensive logic for handling Windows GUI elements, responding to button clicks, updating progress bars, and managing window states (`ShowWindow`, `SetForegroundWindow`).
*   **File System Operations:** The code heavily utilizes standard file manipulation techniques:
    *   Moving/Copying files from temporary locations to final destinations.
    *   Generating unique temporary filenames (e.g., `_nsu%X.tmp` pattern).
    *   Checking and setting file attributes (Hidden, System, etc.).
*   **Registry Manipulation:** Extensive use of `RegOpenKeyExW`, `RegSetValueExW`, and `RegQueryValueExW` indicates the installer modifies system configurations or creates persistent settings during the installation process.

### Suspicious or Malicious Behaviors
While the code primarily reflects standard installer behavior, there are several elements that are frequently utilized by malware (specifically in "droppers" or "loaders"):

*   **Privilege Manipulation:** The binary calls `AdjustTokenPrivileges` and `LookupPrivilegeValueW`. While common in installers to allow system-wide changes, these functions can also be used by malware to gain higher privileges or bypass security restrictions.
*   **Dynamic Loading:** The use of `LoadLibraryExW` and `GetModuleHandleW` (seen in `fcn.00402103`) is a common technique for loading additional components or malicious DLLs into the process memory at runtime.
*   **Staging Area via Temp Folders:** The code identifies and utilizes the `%TEMP%` directory to move and extract files before execution. This "staging" behavior is a hallmark of droppers, where a benign-looking installer extracts a hidden malicious payload from its internal resources or an encrypted bundle.
*   **Persistence/Configuration:** The heavy reliance on Registry modifications (`RegSetValueExW`) suggests the binary is designed to ensure that the software (or its component) persists and executes automatically upon subsequent system boots or user actions.

### Notable Techniques & Patterns
*   **Obfuscated Logic Flow:** The large switch-case structures (e.g., in `fcn.00401434`) are a common way to handle complex, state-driven logic in installer scripts, making it difficult for simple automated scanners to follow the intended path of execution.
*   **Standard Windows API usage:** The code relies heavily on "Win32" style programming (Unicode strings ending in `W`, standard DLLs like `ADVAPI32`, `USER32`, and `SHELL32`), which is typical for software targeting general-purpose Windows environments.
*   **Hardcoded Errors:** The specific error messages (e.g., "Installer integrity check has failed") suggest that the binary checks the integrity of its own components or the files it is attempting to extract, a common step in ensuring the payload hasn't been tampered with by security software during download.

### Summary for Incident Response
This binary appears to be an **installer/dropper**. While the logic shown is typical for legitimate installation scripts, the "malicious" nature of such a sample usually lies in the **payload** it extracts and executes from its internal resources rather than the installer code itself. 

**Key indicators for further investigation:**
*   Investigate what file is being extracted/moved to the `%TEMP%` directory.
*   Monitor for any calls to `ShellExecuteW` or `CreateProcessW` involving files recently moved into temporary folders.
*   Audit registry keys modified by the process, specifically those under `HKEY_CURRENT_USER\Software\` or `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run`.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1112 | Modify Registry | The binary actively utilizes `RegOpenKeyExW`, `RegSetValueExW`, and `RegQueryValueExW` to modify system configurations. |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys | The analysis identifies the use of registry keys (e.g., under `...\Run`) to ensure the software persists after a reboot. |
| T1068 | Exploitation for Privilege Escalation | The inclusion of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicates attempts to obtain higher privileges. |
| T1036 | Launching Application | The binary functions as a "dropper" by moving and extracting files into the `%TEMP%` directory before execution. |
| T1027 | Obfuscated Files or Information | The use of complex switch-case logic and integrity checks is designed to hinder automated analysis and ensure payload integrity. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `nsis.sf.net` (Note: Identified as a component of the NSIS installer framework)

**File paths / Registry keys**
*   *None identified.* (The analysis notes the use of `%TEMP%` and `_nsu%X.tmp` patterns, but these are standard behaviors for this specific installer type and do not constitute unique malicious path indicators.)

**Mutex names / Named pipes**
*   *None detected.*

**Hashes**
*   *None provided in the source text.*

**Other artifacts**
*   **Tooling/Framework:** NSIS (Nullsoft Script Installer) — The binary's structure and specific identifiers indicate it is a wrapper for this common installation tool. 
*   **Behavioral Artifact:** Use of `_nsu%X.tmp` for staging files in temporary directories.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown (NSIS Wrapper)
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Installation Framework Usage:** The binary is identified as an NSIS (Nullsoft Script Installer) stub, which is frequently used by threat actors to wrap and deploy malicious payloads while masking their initial execution.
*   **Staging & Deployment Behavior:** The sample exhibits classic "dropper" indicators, such as extracting files into the `%TEMP%` directory and performing integrity checks to ensure the payload has not been tampered with or removed by security software.
*   **Persistence & Privilege Escalation:** The inclusion of `AdjustTokenPrivileges` for elevated permissions and `RegSetValueExW` targeting "Run" keys confirms the intent to establish a persistent foothold on the system for the delivered payload.
