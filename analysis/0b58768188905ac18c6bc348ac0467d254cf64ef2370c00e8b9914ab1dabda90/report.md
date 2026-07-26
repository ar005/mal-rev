# Threat Analysis Report

**Generated:** 2026-07-26 05:29 UTC
**Sample:** `0b58768188905ac18c6bc348ac0467d254cf64ef2370c00e8b9914ab1dabda90_0b58768188905ac18c6bc348ac0467d254cf64ef2370c00e8b9914ab1dabda90.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b58768188905ac18c6bc348ac0467d254cf64ef2370c00e8b9914ab1dabda90_0b58768188905ac18c6bc348ac0467d254cf64ef2370c00e8b9914ab1dabda90.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 16,009,736 bytes |
| MD5 | `40168a81cfbb1f962288abeaffbc09a4` |
| SHA1 | `82fad79febf46fb9aeebe3b07280453f9558884d` |
| SHA256 | `0b58768188905ac18c6bc348ac0467d254cf64ef2370c00e8b9914ab1dabda90` |
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
| `.rsrc` | 3,072 | 4.203 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`, `GetCommandLineW`

## Extracted Strings

Total strings found: **35027** (showing first 100)

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

Based on the analysis of the provided disassembly and strings, here is a summary of the binary's functionality and behavior.

### Core Functionality and Purpose
The code represents an **installer stub** or a **downloader/dropper**. Specifically, it bears many hallmarks of an installer built with the **NSIS (Nullsoft Script Installer)** framework or a similar custom-built setup engine. 

Its primary role is to act as a "wrapper": it prepares the environment, extracts and decompresses internal resources (the actual payload), and executes them on the system.

### Suspicious and Malicious Behaviors
While much of this behavior is common in legitimate installers, these specific actions are often utilized by malware to deliver a primary malicious payload:

*   **Payload Extraction & Decompression:** 
    *   The function `fcn.00406c4b` contains logic consistent with **LZMA decompression**. This indicates the binary contains compressed data (potentially an executable, DLL, or script) inside its own body.
    *   The code moves and copies files to temporary directories (e.g., using paths involving `GetTempPathW`) and creates temporary filenames like `.nsu%X.tmp`.
*   **File Manipulation & System Interaction:** 
    *   It interacts heavily with the filesystem, performing operations such as `MoveFileW`, `CopyFileW`, and `CreateFileW`.
    *   It modifies file attributes (e.g., setting "Hidden" or "System" attributes) via `SetFileAttributesW` to hide its activities or the files it extracts.
*   **Registry Manipulation:** 
    *   The presence of several `Reg` functions (e.g., `RegOpenKeyExW`, `RegSetValueExW`) suggests the binary modifies the Windows Registry to configure settings, create persistence for a payload, or change system configurations.
*   **Environment Modification:**
    *   The code checks and potentially sets environment variables (`SetEnvironmentVariableW`) and interacts with "System" paths to ensure it has the necessary context to run its internal components.

### Notable Techniques and Patterns
*   **Self-Extraction (Stub Pattern):** The binary is designed to stay small while carrying a large amount of data (the payload) in an encrypted or compressed state. This allows it to bypass simple scanners that only look for known malicious signatures, as the actual "malware" part doesn't exist on disk until after this stub runs.
*   **Standard API Usage for Obfuscation:** By using standard Windows APIs for file management and UI, the code mimics a legitimate installer. This makes it harder for automated analysis tools to flag the binary immediately without dynamic execution.
*   **Late-Stage Execution:** The use of `ShellExecuteExW` (seen in strings) suggests that after the extraction is complete, it may launch an additional process or component.

### Summary for Incident Response
This binary is a **loader/dropper**. If this is from a live sample:
1.  The binary likely contains a hidden payload compressed with LZMA.
2.  It creates temporary files in `%TEMP%` or other system folders.
3.  **Action:** Check the `\Temp\` directories and search for recently created `.exe` or `.dll` files created during the timeframe of infection.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files | The use of LZMA decompression indicates that the primary payload is hidden within a compressed format to evade signature-based detection. |
| T1036 | Masquerading | The use of `SetFileAttributesW` to set "Hidden" or "System" flags is an attempt to conceal the presence of files from the user and system tools. |
| T1112 | Modify Registry | The binary utilizes `RegSetValueExW` to modify registry keys, which can be used to establish persistence or alter system configurations. |
| T1059 | Command and Scripting Interpreter | The use of `ShellExecuteExW` indicates the stub acts as a launcher to execute additional components or commands once the payload is extracted. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (While the analysis mentions `GetTempPathW` and `RegOpenKeyExW`, no specific hardcoded file paths or registry keys were provided in the text).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **LZMA Decompression:** The presence of a specific decompression routine at `fcn.00406c4b` indicates the binary contains compressed payloads (common in droppers).
*   **NSIS Stub Pattern:** The behavior and file naming convention (`.nsu%X.tmp`) identify the binary as an **NSIS (Nullsoft Script Installer)** wrapper, often used to hide malicious payloads within a legitimate-looking installer structure.

***

**Analyst Note:** This sample is characterized by its behavioral traits rather than static indicators. The primary risk factors are the **LZMA decompression logic** and the use of **standard Windows APIs** (`ShellExecuteExW`, `GetTempPathW`) to facilitate "dropped" files in temporary directories, which is typical for a downloader or installer stub.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown (Generic NSIS Stub)
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Payload Extraction:** The presence of LZMA decompression logic and the creation of temporary files in `\Temp\` indicate the binary's primary purpose is to unpack a hidden payload from within its own structure.
*   **Evasive Behaviors:** The use of `SetFileAttributesW` to apply "Hidden" or "System" flags, combined with non-standard file naming (e.g., `.nsu%X.tmp`), are classic techniques used by droppers to hide files from the user and automated scans.
*   **Execution Chain:** The transition from a wrapper's logic to execution via `ShellExecuteExW` confirms its role as a "launcher" or "loader," designed to execute a secondary payload once the initial environment setup is complete.
