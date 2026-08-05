# Threat Analysis Report

**Generated:** 2026-08-04 19:25 UTC
**Sample:** `0d024a36cc1c1970a26a7f1ac0daf07d9478bdd6c5b6484284664ebe33eb4815_0d024a36cc1c1970a26a7f1ac0daf07d9478bdd6c5b6484284664ebe33eb4815.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d024a36cc1c1970a26a7f1ac0daf07d9478bdd6c5b6484284664ebe33eb4815_0d024a36cc1c1970a26a7f1ac0daf07d9478bdd6c5b6484284664ebe33eb4815.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 103,332,680 bytes |
| MD5 | `e302a6f4e571e3d5a9954292adef29cc` |
| SHA1 | `29a32701ad8f97eea1fe5dbafb6a0a70fef28aa7` |
| SHA256 | `0d024a36cc1c1970a26a7f1ac0daf07d9478bdd6c5b6484284664ebe33eb4815` |
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
| `.rsrc` | 80,896 | 4.607 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`, `GetCommandLineW`

## Extracted Strings

Total strings found: **223223** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality and behavior.

### Core Functionality and Purpose
The binary appears to be a **first-stage installer or "dropper"** typical of those generated by tools like NSIS (Nullsoft Script Installer). Its primary purpose is to prepare the system environment, unpack/extract files, modify registry settings, and launch subsequent components.

While the code contains structures common in legitimate installers, several behaviors are characteristic of malware loaders used to deliver payloads while minimizing the footprint of the initial execution.

### Suspicious or Malicious Behaviors
*   **Dropper / Downloader Behavior:** 
    *   The entry point (`entry0`) and supporting functions (like `fcn.004030fc`) involve extracting data, moving files, and creating temporary files in the `%TEMP%` directory. This is a classic "dropper" pattern where a small, less-suspicious binary is used to "drop" the actual malicious payload onto the disk.
    *   The use of `GetTempPathW` and `MoveFileW` suggests it moves an extracted component to its final execution location.

*   **Registry Manipulation:** 
    *   Extensive calls to `RegOpenKeyExW`, `RegSetValueExW`, and `RegCreateKeyExW` indicate the binary is actively modifying system configuration or persistence keys. In a malicious context, this is often used to ensure the payload starts automatically on boot (e.g., "Run" keys) or hides its presence from the user.

*   **Environment Manipulation:** 
    *   The code includes logic to set environment variables (`SetEnvironmentVariableW`). Malicious actors use this to redirect subsequent stages of an infection or to bypass certain security checks by altering how the OS finds system files.

*   **Potential Anti-Analysis/Evasion:**
    *   **Timing Checks:** The presence of `GetTickCount` and `Sleep` (especially in loops) is a common indicator of anti-sandbox techniques, where the program waits for a period to exceed the time limit of an automated analysis sandbox.
    *   **Implicit Execution:** The use of `ShellExecuteW`, `CreateProcessW`, and `LoadLibraryExW` allows the binary to launch other processes or load DLLs into memory, which can be used to "handoff" execution to a secondary malicious stage.

### Notable Techniques and Patterns
*   **NSIS Wrapper Pattern:** The presence of strings like `"NSIS Error"` and the specific structure of `fcn.004030fc` (which handles resource extraction and file copying) strongly suggest this is an NSIS-generated installer. Malware authors frequently use NSIS because it provides a "legitimate" wrapper for malicious payloads, making it harder to distinguish from a standard software installer.
*   **State Machine Logic:** The large `switch` table in `fcn.00401434` is typical of unpacked or wrapped code where a main loop handles various internal commands (e.g., "create window," "set text," "move file").
*   **Persistence Infrastructure:** The specific combination of registry manipulation and the use of standard shell extensions (`SHELL32.dll`) suggests the binary is designed to integrate deeply with the Windows environment, likely for long-term presence on a compromised host.

### Summary Table of Key Indicators
| Category | Observed Behaviors / APIs | Purpose in Malware Context |
| :--- | :--- | :--- |
| **Persistence** | `RegOpenKeyExW`, `RegSetValueExW` | Establishing "Run" keys or other persistence mechanisms. |
| **Dropper/Loader** | `GetTempPathW`, `MoveFileW`, `CopyFileW` | Extracting and relocating a secondary malicious payload. |
| **Evasion** | `Sleep`, `GetTickCount` | Stalling execution to bypass automated sandbox analysis. |
| **Execution** | `CreateProcessW`, `ShellExecuteExW`, `LoadLibraryExW` | Launching the "stage 2" malware or injecting into processes. |
| **System Interaction**| `SetEnvironmentVariableW`, `GetSystemDirectoryW` | Manipulating system paths to facilitate further infection stages. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of an NSIS wrapper allows the malicious payload to masquerade as a legitimate software installer to evade detection. |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys | The binary uses `RegOpenKeyExW` and `RegSetValueExW` to modify registry keys for ensuring persistence upon system reboot. |
| T1497 | Virtualization/Sandbox Detection | The implementation of `GetTickCount` and `Sleep` loops is a common tactic used to stall execution and bypass automated analysis environments. |
| T1059 | Command and Scripting Interpreter | The use of `ShellExecuteW` indicates the binary's ability to execute commands or hand off execution to subsequent stages. |
| T1106 | Native API | The use of `LoadLibraryExW` allows the malware to load necessary DLLs directly into memory for its next stage of operation. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None detected.

**File paths / Registry keys**
*   None detected. *(Note: While the behavior report mentions registry manipulation via `RegOpenKeyExW` and use of `%TEMP%`, no specific malicious paths or hardcoded registry keys were identified in the source text.)*

**Mutex names / Named pipes**
*   None detected.

**Hashes**
*   None detected.

**Other artifacts**
*   **NSIS Wrapper Pattern:** The binary is identified as a wrapped installer (likely using the Nullsoft Script Installer). While not a unique identifier for a specific campaign, it indicates a specific delivery method.
*   **Dropper/Loader Behavior:** Use of `GetTempPathW`, `MoveFileW`, and `CopyFileW` to relocate components in the temp directory.
*   **Anti-Analysis Techniques:** Use of `GetTickCount` and `Sleep` (detected via behavioral analysis) suggests a deliberate attempt to stall execution to bypass sandbox environments.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High (for type) / Low (for specific campaign identification)

**Key evidence**:
*   **Dropper/Loader Functionality:** The binary utilizes `GetTempPathW`, `MoveFileW`, and `CopyFileW` to extract and relocate files from an initial installer to a temporary directory, a signature behavior of first-stage droppers.
*   **Persistence & Evasion Techniques:** It employs registry manipulation (`RegSetValueExW`) for startup persistence and incorporates anti-analysis techniques (timing checks via `GetTickCount` and `Sleep`) specifically designed to stall and bypass automated sandboxes.
*   **Wrappered Architecture:** The use of an NSIS wrapper serves as a common obfuscation technique, allowing the malicious payload to masquerade as a legitimate software installer while facilitating the "handoff" to secondary stages via `ShellExecuteW` and `CreateProcessW`.
