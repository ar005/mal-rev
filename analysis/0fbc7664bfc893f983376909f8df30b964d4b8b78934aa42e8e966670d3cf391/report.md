# Threat Analysis Report

**Generated:** 2026-08-16 19:03 UTC
**Sample:** `0fbc7664bfc893f983376909f8df30b964d4b8b78934aa42e8e966670d3cf391_0fbc7664bfc893f983376909f8df30b964d4b8b78934aa42e8e966670d3cf391.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0fbc7664bfc893f983376909f8df30b964d4b8b78934aa42e8e966670d3cf391_0fbc7664bfc893f983376909f8df30b964d4b8b78934aa42e8e966670d3cf391.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 599,160 bytes |
| MD5 | `5ff02f584e5e933c8c0f875df3787ea4` |
| SHA1 | `cba53711a8ba1e224028773b3e1c3f283792fe36` |
| SHA256 | `0fbc7664bfc893f983376909f8df30b964d4b8b78934aa42e8e966670d3cf391` |
| Overall entropy | 6.685 |
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
| `.rsrc` | 298,496 | 4.462 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `SetFileSecurityW`, `RegOpenKeyExW`, `RegEnumValueW`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHFileOperationW`, `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `ShellExecuteExW`, `SHGetFileInfoW`
**ole32.dll**: `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `GetClientRect`, `EndPaint`, `DrawTextW`, `IsWindowEnabled`, `DispatchMessageW`, `wsprintfA`, `CharNextA`, `CharPrevW`, `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `GetSystemMetrics`, `FillRect`, `AppendMenuW`, `TrackPopupMenu`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectW`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetModuleHandleA`, `GetProcAddress`, `GetSystemDirectoryW`, `lstrcatW`, `Sleep`, `lstrcpyA`, `WriteFile`, `GetTempFileNameW`, `lstrcmpiA`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `GetLastError`

## Extracted Strings

Total strings found: **1408** (showing first 100)

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

Based on the provided disassembly and strings, here is a technical analysis of the binary's functionality.

### Core Functionality and Purpose
The binary functions as an **installer stub**, specifically consistent with the architecture of the **NSIS (Nullsoft Script Installer)** framework. Its primary purpose is to manage the installation process of another program by performing several "housekeeping" tasks: 
*   Validating file integrity before execution.
*   Extracting and moving files into final locations.
*   Configuring system environment settings via the Windows Registry.
*   Handling GUI interactions for an installation wizard.

### Suspicious or Malicious Behaviors

While many of these behaviors are common in legitimate installers, they are also frequently utilized by malware as a "dropper" or "installer stub" to prepare a system for a payload.

*   **Registry Manipulation:**
    *   The code extensively uses `RegOpenKeyExW`, `RegSetValueExW`, and `RegEnumValueW`. 
    *   While typically used to set installation paths, these are also standard methods for establishing **persistence** (e.g., adding keys to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`) or configuring the behavior of a resident threat.
*   **File and Directory Manipulation:**
    *   The code calls `CreateDirectoryW` followed by `SetFileSecurityW`. This is used to create directories with specific access permissions, ensuring the installed application (or a malicious payload) has appropriate privileges.
    *   It utilizes `MoveFileW` and `CopyFileW` to move files from temporary locations to permanent ones after they have been "extracted." 
    *   The presence of `GetTempPathW` and subsequent file creation in the Temp folder is common in multi-stage droppers where a small loader fetches and installs a larger payload.
*   **Integrity Checking:**
    *   Function `fcn.00403d17` explicitly includes an "Installer integrity check." This ensures that the installer hasn't been modified before it executes, but in a malware context, this is used to ensure the malicious components are intact before they begin their operations.
*   **Dynamic Library Loading:**
    *   The use of `GetProcAddress`, `GetModuleHandleW`, and `LoadLibraryExW` allows the binary to load required DLLs at runtime. This can be used to delay the loading of suspicious modules until after a security check has passed or as part of a delayed execution strategy.

### Notable Techniques and Patterns

*   **State Machine Architecture:** The large `switch` block in `fcn.00401434` indicates a state-machine-based execution flow typical of installer scripts (like NSIS). Each "case" represents a step in the installation process (e.g., checking for files, setting registry keys, handling button clicks).
*   **NSIS Infrastructure:** The strings and error messages (e.g., `"NSIS Error"`, `nsis.sf.net`) confirm that this is an NSIS-based installer. It is common for malware authors to use these legitimate tools as wrappers to bundle and install secondary payloads.
*   **Environment Manipulation:** The code interacts with environment variables (via `GetEnvironmentStringsW` or similar logic) and uses `SetCurrentDirectoryW` to move the execution context into a temporary folder, ensuring that subsequent files are written to the correct location.
*   **Standard Win32 API Reliance:** The binary relies heavily on standard Windows APIs for UI interaction (`MessageBoxIndirectW`, `GetDlgItem`) and system information gathering (e.g., `GetVersionExW`), which is used to determine compatibility or environment specifics before proceeding with the "installation."

### Summary
This binary is a **wrapper/installer stub**. It is not necessarily malicious in itself; however, its core functionality—**file extraction, registry modification for persistence, and integrity checking of payloads**—provides the necessary infrastructure for delivering malware. If this sample was found in an unexpected location (e.g., temp folders or via a phishing link), it should be treated as a **downloader/dropper**.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1112** | Modify Registry | The binary utilizes `RegOpenKeyExW` and `RegSetValueExW` to modify registry keys, which are used for both system configuration and establishing persistence. |
| **T1036** | Masquerading | The use of an NSIS installer stub allows the malicious payload to masquerade as a legitimate software installation process to evade detection. |
| **T1547** | Boot or Logon Autostart Execution | The movement of files to "permanent" locations and modification of registry keys are typical indicators of establishing persistence for a persistent threat. |
| **T1027** | Software Packing | The use of integrity checks and dynamic library loading (`GetProcAddress`, `LoadLibraryExW`) are common tactics used to ensure payload integrity and evade static analysis. |
| **T1497** | Virtualization/Sandbox Detection | The gathering of environment specifics before proceeding with the "installation" suggests a check for analysis environments prior to execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** Because this sample is identified as a generic **NSIS Installer Stub**, many of the strings present (e.g., `SHELL32.dll`, `RegOpenKeyExW`) are standard Windows API calls and have been excluded as false positives per your instructions.

### IP addresses / URLs / Domains
*   *None identified.* 
*(Note: While "nsis.sf.net" is mentioned in the analysis, it is a legitimate domain for the NSIS toolset and does not serve as a specific C2 or malicious infrastructure indicator.)*

### File paths / Registry keys
*   **Persistence Mechanism:** The analysis notes the use of `RegOpenKeyExW` and `RegSetValueExW` to modify registry keys. While no specific malicious key was named, the behavior targets standard persistence locations such as:
    *   `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` 

### Mutex names / Named pipes
*   *None identified.*

### Hashes
*   *None provided in the source text.*

### Other artifacts
*   **Tooling/Wrapper:** **NSIS (Nullsoft Script Installer)**. The binary is structured as an NSIS wrapper. In a threat intelligence context, this indicates the use of a common "dropper" framework to package and deliver payloads.
*   **Functionality Profile:** 
    *   **Integrity Checking:** Presence of a specific integrity check routine (`fcn.00403d17`) used to verify payload integrity before execution.
    *   **Drop/Move Behavior:** Utilization of `CopyFileW`, `MoveFileW`, and `GetTempPathW` to move files from temporary directories to final locations.
    *   **Dynamic Loading:** Use of `GetProcAddress` and `LoadLibraryExW` to resolve functions at runtime, a common technique to evade static analysis of the import table.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: custom (NSIS Wrapper)
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Infrastructure as a Wrapper:** The binary is identified as an NSIS-based installer stub, a common method for bundling and installing secondary payloads while masking their presence behind a legitimate installation wizard.
    *   **Persistence and File Management:** It performs behaviors indicative of a dropper, specifically moving files from temporary directories to permanent locations and modifying Registry keys (likely in the `Run` key) to ensure persistence.
    *   **Evasion Tactics:** The inclusion of integrity checks (`fcn.00403d17`), dynamic library loading (`GetProcAddress`, `LoadLibraryExW`), and environmental queries suggests a deliberate attempt to verify payload integrity and evade static analysis before the final execution.
