# Threat Analysis Report

**Generated:** 2026-06-23 18:28 UTC
**Sample:** `001a10b946d41f8794c110f97cd46b961fea0c0d50c92efaef1d166adaffe8b8_001a10b946d41f8794c110f97cd46b961fea0c0d50c92efaef1d166adaffe8b8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `001a10b946d41f8794c110f97cd46b961fea0c0d50c92efaef1d166adaffe8b8_001a10b946d41f8794c110f97cd46b961fea0c0d50c92efaef1d166adaffe8b8.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 79,386,456 bytes |
| MD5 | `c7a1c5c0c8b403a79f658f5247b025f4` |
| SHA1 | `4742d8622786354fb8f67180270e6c08f5de711e` |
| SHA256 | `001a10b946d41f8794c110f97cd46b961fea0c0d50c92efaef1d166adaffe8b8` |
| Overall entropy | 7.999 |
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
| `.rsrc` | 385,024 | 2.268 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `RemoveDirectoryW`, `lstrcmpiA`, `GetTempFileNameW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`, `GetCommandLineW`

## Extracted Strings

Total strings found: **171470** (showing first 100)

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

Based on the provided disassembly and decompiled code, here is a technical analysis of the binary's behavior:

### Core Functionality and Purpose
The binary functions as a **multi-stage loader and installer**. It exhibits characteristics typical of an "installer" wrapper (similar to those created by NSIS), but it contains several sophisticated techniques common in malware for hiding malicious payloads. Its primary purpose is to unpack, verify, and execute additional components while attempting to evade detection and forensic analysis.

### Suspicious or Malicious Behaviors
*   **Payload Decryption/Decompression:** The function `fcn.00406c4b` contains a complex loop involving heavy bitwise operations, shifts, and arithmetic. This is a signature of a **custom decryption or decompression routine**. It likely takes an encrypted resource within the binary and decodes it into a usable executable format in memory.
*   **Anti-Forensics (File Masquerading):** The code at `0x40179b` specifically uses `SetFileTime` and `GetFileAttributes`. By retrieving the attributes of an existing file and applying them to its own files, it attempts to hide the "freshness" of a dropped file, making a newly installed component appear as if it has existed on the system for a long time (mimicking original system files).
*   **Dynamic Payload Execution:** In `fcn.00402103`, the code uses `GetModuleHandleW` and `LoadLibraryExW` to load modules into the process memory. It then attempts to find and execute functions from these loaded modules. This is a standard technique for "hiding" the primary malicious logic behind a legitimate-looking installer stub.
*   **Integrity Checks & Error Handling:** The function `fcn.00403dae` performs what appears to be an integrity check of the payload before execution. If the check fails (which could happen if an analyst modifies the file), it falls back to a generic "Installer integrity check has failed" message rather than crashing or exhibiting unusual behavior, helping to hide its true functionality from researchers.
*   **Temporary File Manipulation:** The `entry0` function follows patterns often seen in malware droppers: extracting files into `%TEMP%`, renaming them (e.g., `nsu%X.tmp`), and moving/executing them from temporary locations to bypass simple file system monitors.

### Notable Techniques & Patterns
*   **Installer Mimicry:** The presence of "NSIS Error" strings, the use of `SetCurrentDirectoryW`, and logic involving `GetTempPathW` suggest it is designed to look like a standard software installer to evade suspicion during manual review.
*   **Manual Memory Management:** There are several instances where `GlobalAlloc` and `GlobalFree` are used to manage buffers for decoded data, suggesting the application handles its own memory management rather than relying purely on high-level system APIs.
*   **Reflective Loading Behavior:** The way it resolves functions from newly loaded libraries (checking if `piVar1 != 0` before execution) suggests a "Loader" architecture where the main binary is just a vehicle for the actual payload.

### Summary of Risk
The sample's behavior is highly consistent with a **dropper/loader**. It uses significant effort to hide its primary payload through custom decryption and anti-forensic file tampering (timestamp manipulation). The high level of abstraction in the dispatching logic (`fcn.00401434`) suggests it is designed to handle many different tasks, likely for different types of payloads or across different environment conditions.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of complex bitwise operations and arithmetic in `fcn.00406c4b` indicates a custom decryption routine to hide the payload from static analysis. |
| T1036 | Masquerading | The malware manipulates file timestamps via `SetFileTime` and utilizes installer-like strings/logic to blend in with legitimate system files. |
| T1562 | Predictive Analysis Evasion | Integrity checks are designed to detect analyst intervention, ensuring the core functionality remains hidden if the binary is modified during research. |
| T1083 | File and Directory Execution | The malware utilizes standard temporary directories (`%TEMP%`) and common file extensions (e.g., `.tmp`) to hide its execution from basic monitoring. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `nsu%X.tmp` (Identified as a naming convention for dropped files in the `%TEMP%` directory).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Decryption Routine:** Custom decryption/decompression logic located at `0x406c4b`.
*   **Anti-Forensics Technique:** Use of `SetFileTime` and `GetFileAttributes` to masquerade the "freshness" of dropped files (timestamp manipulation).
*   **Persistence/Execution Pattern:** Dropping and executing payloads from `%TEMP%` directory.
*   **Loader Behavior:** Manual memory management (`GlobalAlloc`/`GlobalFree`) for handling decoded payloads.

---

## Malware Family Classification

1. **Malware family:** Unknown
2. **Malware type:** Loader / Dropper
3. **Confidence:** High

**Key evidence:**
*   **Multi-Stage Payload Delivery:** The analysis describes a clear "loader" architecture where the primary binary serves as a wrapper to decrypt, decompress, and dynamically load secondary payloads into memory using `LoadLibraryExW` and `GetModuleHandleW`.
*   **Advanced Anti-Forensics & Evasion:** The sample employs specific techniques to hinder analysis, including timestamp manipulation (`SetFileTime`) to mask the "freshness" of dropped files and integrity checks specifically designed to detect if a researcher is tampering with the binary.
*   **Malicious Wrapper Techniques:** It utilizes "Installer Mimicry" (imitating NSIS installers) and hides its activities in common directories like `%TEMP%` using `.tmp` extensions, which are classic indicators of a dropper intended to evade both automated systems and manual inspection.
