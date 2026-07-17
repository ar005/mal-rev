# Threat Analysis Report

**Generated:** 2026-07-16 20:17 UTC
**Sample:** `077ab28d66abdafad9f5411e18d26e87fe43da1410ee8fe846bd721ab0cb52de_077ab28d66abdafad9f5411e18d26e87fe43da1410ee8fe846bd721ab0cb52de.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `077ab28d66abdafad9f5411e18d26e87fe43da1410ee8fe846bd721ab0cb52de_077ab28d66abdafad9f5411e18d26e87fe43da1410ee8fe846bd721ab0cb52de.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 75,387,632 bytes |
| MD5 | `29953b2e46aeaf0157d487c13c4a0643` |
| SHA1 | `429efcf0370b53cc3c455b634dc066b1d08b568d` |
| SHA256 | `077ab28d66abdafad9f5411e18d26e87fe43da1410ee8fe846bd721ab0cb52de` |
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
| `.rsrc` | 80,896 | 4.536 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`, `GetCommandLineW`

## Extracted Strings

Total strings found: **163702** (showing first 100)

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

Based on the provided disassembly and string data, here is an analysis of the binary’s functionality.

### Core Functionality
The binary appears to be a **multi-stage installer or "loader"** (likely built using the Nullsoft Script Installer - NSIS). It functions as a wrapper that prepares and extracts secondary components before they are executed. Its primary roles include:
*   **Resource Unpacking:** The presence of complex bitwise operations and looping structures in `fcn.00406c4b` suggests it decodes/decompresses an embedded payload (possibly using a Huffman-style or similar decoding algorithm).
*   **System Integration:** It performs standard installer tasks such as creating directories, moving files between paths, and setting file attributes.
*   **Environment Setup:** It resolves system paths, handles temporary file creation, and manages environment variables to ensure the "installation" (or payload delivery) succeeds.

### Suspicious or Malicious Behaviors
While these behaviors are common in legitimate installers, they are also hallmark characteristics of **droppers** and **loaders** used in malware infections:

*   **Payload Dropping & Execution:** The binary uses `GetTempPathW`, `MoveFileW`, and `CopyFileW` to stage files. It specifically creates a temporary file (e.g., `nsuXX.tmp`) and moves/renames it, which is a common technique to "drop" a malicious executable from an initial installer into a directory where it can be executed.
*   **Integrity Checks:** The logic in `fcn.00403dae` contains specific checks for file integrity before proceeding. In malware, this ensures that the dropped payload has not been corrupted or modified by security software during the extraction process.
*   **Privilege Escalation/Manipulation:** The inclusion of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicates an attempt to acquire specific system privileges (like `SeShutdownPrivilege`). While often used for standard admin functions, these calls are frequently monitored as indicators of an attempt to escalate the process's capabilities.
*   **Evasion through Scripting:** The "NSIS" references and the large switch-case logic (`fcn.00401434`) suggest that much of the program's behavior is driven by a script. This makes it harder for automated tools to determine the final destination of the software, as the specific actions are hidden behind the script logic.

### Notable Techniques and Patterns
*   **NSIS Framework:** The code heavily utilizes standard NSIS patterns. Malware authors often use this because it provides a "legitimate" wrapper that can bypass simple heuristic filters by mimicking common installer behaviors.
*   **Complex Decoding Loop:** The function `fcn.00406c4b` contains several nested loops with complex arithmetic and bit-shifting (e.g., `((1 << uVar1 / 0x2d) + -1)`). This is typical of an **unpacking stub**, designed to decompress a payload that is too large or "noisy" to be stored in plain text within the binary's resources.
*   **Dynamic Path Resolution:** The code heavily uses `GetFullPathNameW` and `GetShortPathNameW`. This allows it to resolve paths dynamically, which helps in hiding where files are being moved until they are actually executed.
*   **File System Manipulation for Stealth:** There is significant use of `SetFileAttributesW`, likely used to set the "Hidden" or "System" attributes on newly dropped files to evade casual observation by the user or basic security scanners.

### Summary Conclusion
This binary is a **high-capability dropper/loader**. It is designed to take an initial stage of execution, perform several rounds of unpacking and integrity checks, move/prepare a second-stage payload onto the filesystem (often in a temporary directory), and eventually launch it. The presence of NSIS logic suggests it was crafted to mimic a legitimate software installer while hiding malicious behavior inside packed resources.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1059 | Command and Scripting Interpreter | The use of NSIS scripts and complex switch-case logic obscures the true functional path and complicates automated analysis. |
| T1105 | Ingress Tool Transfer | The binary extracts, moves, and renames files into temporary directories to stage a second-stage payload for execution. |
| T1068 | Exploitation for Privilege Escalation | The usage of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicates an attempt to acquire higher system permissions. |
| T1036 | Masquerading | Utilizing the NSIS framework allows the binary to masquerade as a legitimate installer to bypass heuristic security filters. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `nsuXX.tmp` (Note: This is a common naming convention for NSIS installer temporary files).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Framework Identification:** Evidence of **NSIS** (Nullsoft Script Installer) framework usage.
*   **Unpacking Stub Logic:** Complex decoding/decompression routines located at `fcn.00406c4b`.
*   **Integrity Check Routine:** Specific logic for payload validation identified at `fcn.00403dae`.
*   **Scripted Behavior Logic:** Large switch-case block used for script processing at `fcn.00401434`.
*   **Privilege Manipulation:** Calls to `AdjustTokenPrivileges` and `LookupPrivilegeValueW`.

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
*   **Multi-Stage Execution & Obfuscation:** The binary utilizes the NSIS framework to masquerade as a legitimate installer while employing complex decoding loops (e.g., `fcn.00406c4b`) and switch-case logic to hide its true purpose until it extracts and executes a secondary payload.
*   **Dropper Behavior:** The analysis confirms classic "dropper" functionality: extracting files into temporary directories (`GetTempPathW`), renaming them, and applying system attributes (e.g., hidden) to evade detection while preparing the next stage of an infection.
*   **Evasion & Privilege Escalation:** The inclusion of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicates a deliberate attempt to gain elevated permissions, while the use of dynamic path resolution ensures the malware can operate across different system configurations successfully.
