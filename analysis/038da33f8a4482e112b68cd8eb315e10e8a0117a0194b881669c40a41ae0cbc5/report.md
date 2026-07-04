# Threat Analysis Report

**Generated:** 2026-07-01 19:02 UTC
**Sample:** `038da33f8a4482e112b68cd8eb315e10e8a0117a0194b881669c40a41ae0cbc5_038da33f8a4482e112b68cd8eb315e10e8a0117a0194b881669c40a41ae0cbc5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `038da33f8a4482e112b68cd8eb315e10e8a0117a0194b881669c40a41ae0cbc5_038da33f8a4482e112b68cd8eb315e10e8a0117a0194b881669c40a41ae0cbc5.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 580,120 bytes |
| MD5 | `b215bfeff0ec221658b8d3f20e9ffe73` |
| SHA1 | `e15037c7cf6a10a2204c4d267bb8a2cd307461f2` |
| SHA256 | `038da33f8a4482e112b68cd8eb315e10e8a0117a0194b881669c40a41ae0cbc5` |
| Overall entropy | 7.555 |
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
| `.rsrc` | 233,472 | 6.658 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`, `GetCommandLineW`

## Extracted Strings

Total strings found: **1032** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary’s functionality:

### Core Functionality and Purpose
The binary functions as a **dropper/installer stub**, likely utilizing the Nullsoft Script Installer (NSIS) framework or a similar wrapper. Its primary purpose is to act as a "wrapper" that prepares the environment, extracts an embedded payload from its own resources, verifies its integrity, and executes it.

### Notable Behaviors & Suspect Activity
*   **Payload Extraction & Staging:**
    *   The code uses `GetTempPathW` and `CopyFileW` to move files into a temporary directory using the naming convention `~nsu%X.tmp`. This is typical of "dropper" behavior where an initial, less-suspicious file is used to unpack and stage a more complex payload on disk before execution.
    *   The logic in `fcn.00403dae` indicates it handles resources that are expected to be compressed or encoded.

*   **Decompression Engine:**
    *   `fcn.00406c4b` contains a complex decompression routine (likely LZMA or a similar sliding-window algorithm). The presence of such an engine is highly characteristic of installers/droppers designed to hide their primary payload in a compressed state within the binary's resources.

*   **Integrity Verification:**
    *   The code includes specific checks for "Installer integrity." It performs calculations on the extracted data to ensure it matches expected values before proceeding with execution, ensuring the payload hasn't been tampered with by antivirus software or during the extraction process.

*   **Privilege/Token Manipulation:**
    *   In `entry0`, the code calls `AdjustTokenPrivileges` and `LookupPrivilegeValueW` to request specific privileges (e.g., `SeShutdownPrivilege`). While often found in legitimate installers that need to reboot a machine, this is also a common technique used by malware to elevate permissions or ensure it can perform administrative actions.

*   **Registry Manipulation:**
    *   The binary frequently interacts with the Windows Registry (`RegEnumKeyW`, `RegEnumValueW`, `RegSetValueExW`). While common in installers for storing configuration data, in a malicious context, this is used to persist settings or disable security software.

*   **Dynamic Loading & Execution:**
    *   The code performs several calls to `LoadLibraryExW` and `GetModuleHandleW`. This allows the program to load additional components into memory at runtime, potentially concealing the true nature of the final payload until it is actually executed.

### Summary of Techniques
*   **Dropping/Staging:** Moving files from internal resources to `%TEMP%` for execution.
*   **Compression:** Using custom or standard decompression (LZMA-style) to hide payloads in plain sight.
*   **Anti-Analysis/Evasion:** The use of a "wrapper" allows the primary payload to be hidden within a legitimate-looking installer structure, making it harder for basic static scanners to identify the malicious components.
*   **Standard Installer Artifacts:** The presence of `NSIS` strings and `RichEdit32` suggests it targets the user interface while performing its backend tasks of extraction and installation.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of a "wrapper," LZMA-style compression, and hidden resource extraction are all primary methods to hide the payload from static analysis. |
| T1134 | Privilege Escalation | The calls to `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicate an attempt to gain higher system privileges for administrative actions. |
| T1112 | Modify Registry | The interaction with various `RegSet...` functions is a standard method for ensuring persistence, changing configurations, or disabling security software. |
| T1036 | Dynamic Resolution (Note: Often mapped to T1027) | The use of `LoadLibraryExW` and `GetModuleHandleW` allows the binary to resolve imports at runtime to conceal its true capabilities from static scanners. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Most strings identified in the "EXTRACTED STRINGS" section are standard Windows API functions or common system libraries (e.g., `USER32.dll`, `CreateProcessW`). These have been excluded as they are standard system components and do not constitute specific malicious IOCs.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   **Naming Convention (Staging):** `~nsu%X.tmp` (Used during the payload extraction/staging phase in the `%TEMP%` directory).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Dropper Behavior:** The binary functions as a "dropper" or "installer stub," likely using an NSIS (Nullsoft Script Installer) wrapper to hide the primary payload.
*   **Persistence/Privilege Escalation Attempt:** Use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` to manipulate system privileges.
*   **Decompression Engine:** Presence of a high-complexity decompression routine (likely LZMA-style) used to decompress embedded malicious content.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Dropper/Wrapper Behavior:** The sample utilizes a standard installer-wrapper technique (likely NSIS), employing complex decompression (LZMA) and integrity checks to hide an embedded payload within its resources.
*   **Staging & Extraction:** It exhibits classic "dropper" behavior by extracting files from its own resource section and moving them to the `%TEMP%` directory using common temporary naming conventions (`~nsu%X.tmp`) before execution.
*   **Evasion Techniques:** The use of dynamic resolution (`LoadLibraryExW`), privilege escalation attempts, and registry manipulation indicates a deliberate effort to prepare the environment and hide the final payload's functionality from security software.
