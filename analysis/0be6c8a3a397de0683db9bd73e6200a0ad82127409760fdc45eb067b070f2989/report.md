# Threat Analysis Report

**Generated:** 2026-07-27 22:54 UTC
**Sample:** `0be6c8a3a397de0683db9bd73e6200a0ad82127409760fdc45eb067b070f2989_0be6c8a3a397de0683db9bd73e6200a0ad82127409760fdc45eb067b070f2989.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0be6c8a3a397de0683db9bd73e6200a0ad82127409760fdc45eb067b070f2989_0be6c8a3a397de0683db9bd73e6200a0ad82127409760fdc45eb067b070f2989.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 400,778 bytes |
| MD5 | `1a159b4ccd494e83bbca41ea99a3a64a` |
| SHA1 | `9ff1658e0a3443a18c44ca63ea9df04f1c24290b` |
| SHA256 | `0be6c8a3a397de0683db9bd73e6200a0ad82127409760fdc45eb067b070f2989` |
| Overall entropy | 7.245 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1711817715 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,112 | 6.461 | No |
| `.rdata` | 5,120 | 5.102 | No |
| `.data` | 1,536 | 4.044 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 138,752 | 5.29 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `lstrcmpiA`, `CreateFileW`, `GetTempFileNameW`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `GetLastError`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`

## Extracted Strings

Total strings found: **882** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495L
tQWPV
Instu`
softuW
NulluN	E
UVWj _3
L$bf-S
D$ Pj(
D$(Ph0
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
| `fcn.00401434` | `0x401434` | 6189 | ✓ |
| `fcn.00406ab0` | `0x406ab0` | 2642 | ✓ |
| `entry0` | `0x40351c` | 1565 | ✓ |
| `fcn.00403c13` | `0x403c13` | 726 | ✓ |
| `fcn.0040657e` | `0x40657e` | 625 | ✓ |
| `fcn.004030a2` | `0x4030a2` | 567 | ✓ |
| `fcn.004032d9` | `0x4032d9` | 485 | ✓ |
| `fcn.00405c4d` | `0x405c4d` | 451 | ✓ |
| `fcn.00406187` | `0x406187` | 378 | ✓ |
| `fcn.00402ece` | `0x402ece` | 234 | ✓ |
| `fcn.004055c6` | `0x4055c6` | 211 | ✓ |
| `fcn.00404527` | `0x404527` | 207 | ✓ |
| `fcn.00404d6d` | `0x404d6d` | 201 | ✓ |
| `fcn.00403ee9` | `0x403ee9` | 185 | ✓ |
| `fcn.004067ef` | `0x4067ef` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.004064a1` | `0x4064a1` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.0040632d` | `0x40632d` | 129 | ✓ |
| `fcn.00404e7b` | `0x404e7b` | 128 | ✓ |
| `fcn.00405f18` | `0x405f18` | 126 | ✓ |
| `fcn.0040640f` | `0x40640f` | 121 | ✓ |
| `fcn.00406112` | `0x406112` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004068c5` | `0x4068c5` | 112 | ✓ |
| `fcn.00406a22` | `0x406a22` | 110 | ✓ |
| `fcn.00405699` | `0x405699` | 108 | ✓ |
| `fcn.00405ba1` | `0x405ba1` | 100 | ✓ |
| `fcn.0040303e` | `0x40303e` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402ece.c`](code/fcn.00402ece.c)
- [`code/fcn.0040303e.c`](code/fcn.0040303e.c)
- [`code/fcn.004030a2.c`](code/fcn.004030a2.c)
- [`code/fcn.004032d9.c`](code/fcn.004032d9.c)
- [`code/fcn.00403c13.c`](code/fcn.00403c13.c)
- [`code/fcn.00403ee9.c`](code/fcn.00403ee9.c)
- [`code/fcn.00404527.c`](code/fcn.00404527.c)
- [`code/fcn.00404d6d.c`](code/fcn.00404d6d.c)
- [`code/fcn.00404e7b.c`](code/fcn.00404e7b.c)
- [`code/fcn.004055c6.c`](code/fcn.004055c6.c)
- [`code/fcn.00405699.c`](code/fcn.00405699.c)
- [`code/fcn.00405ba1.c`](code/fcn.00405ba1.c)
- [`code/fcn.00405c4d.c`](code/fcn.00405c4d.c)
- [`code/fcn.00405f18.c`](code/fcn.00405f18.c)
- [`code/fcn.00406112.c`](code/fcn.00406112.c)
- [`code/fcn.00406187.c`](code/fcn.00406187.c)
- [`code/fcn.0040632d.c`](code/fcn.0040632d.c)
- [`code/fcn.0040640f.c`](code/fcn.0040640f.c)
- [`code/fcn.004064a1.c`](code/fcn.004064a1.c)
- [`code/fcn.0040657e.c`](code/fcn.0040657e.c)
- [`code/fcn.004067ef.c`](code/fcn.004067ef.c)
- [`code/fcn.004068c5.c`](code/fcn.004068c5.c)
- [`code/fcn.00406a22.c`](code/fcn.00406a22.c)
- [`code/fcn.00406ab0.c`](code/fcn.00406ab0.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is an analysis of the binary's functionality.

### Core Functionality and Purpose
The binary functions as a **software installer or update stub**, likely based on the **NSIS (Nullsoft Script Installer)** framework or a similar wrapper system. Its primary role is to extract compressed or packed data from its own resources, verify that integrity of those files, and prepare them for execution on the local system.

### Suspicious and Malicious Behaviors
While much of the code follows standard installer patterns, several behaviors are common in "droppers" (malware designed to install a second-stage payload):

*   **Staged File Dropping:** The `entry0` function contains logic to extract files into temporary directories (e.g., using `GetTempPathW`). It generates filenames like `~nsu%X.tmp`, which is a standard installer behavior for unpacking components before they are moved to final destinations or executed.
*   **Integrity Verification:** Function `fcn.004030a2` contains an extensive routine (including the use of a CRC-like check in `fcn.00406a22`) to verify that the "installer" data has not been tampered with or corrupted. In a malicious context, this ensures that a packed malware payload remains intact before being executed.
*   **Privilege Escalation/Acquisition:** The code explicitly attempts to acquire `SeShutdownPrivilege` using `AdjustTokenPrivileges`. While often used by legitimate installers to force a reboot after updates, it provides the process with elevated privileges over system power states.
*   **Self-Terminating on Failure:** There are multiple checks where the program calls `ExitProcess` or `ExitWindowsEx` based on specific conditions (like failed integrity checks). This is used both as an error handler for legitimate software and to exit "gracefully" if a security tool interferes with the unpacking process.
*   **Dynamic Loading of Modules:** Function `fcn.004068c5` uses `GetSystemDirectoryW` and `LoadLibraryExW` to dynamically load DLLs into the process memory, which is often used to load components only when needed or to bypass static analysis of the main executable.

### Notable Techniques and Patterns
*   **Standard Installer Wrapper:** The presence of strings like `"NSIS Error"` and usage of `Shell32.dll` functions (like `SHGetFileInfoW`) indicate this binary is designed to look like a common, legitimate installer to evade suspicion during initial analysis.
*   **Anti-Analysis/Delay Tactics:** The use of `GetTickCount` in several locations (e.g., `fcn.004030a2` and `fcn.004055c6`) is a common technique to introduce delays or ensure that calculations occur over time, which can sometimes be used to bypass automated "sandboxed" analysis environments.
*   **Complex Integrity Logic:** The complexity of the integrity check in `fcn.004030a2` suggests a multi-layered verification process for the internal data structures (likely using several different types of hashes or checksums).
*   **Resource Handling:** The code interacts heavily with standard UI elements (`CreateDialogParamW`, `GetDlgItem`), suggesting it is designed to interact with the user during the "installation" phase.

### Summary Conclusion
This binary is a **multistage installer wrapper**. While its primary purpose appears to be an installation utility, these types of binaries are frequently used as a "first stage" for malware. It prepares the environment by extracting and verifying payload files into temporary locations before launching the main malicious component.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of NSIS-related strings, standard installer behavior, and common temporary filenames (e.g., `~nsu%X.tmp`) is intended to blend in with legitimate system activity. |
| T1560 | Abuse Elevation Functionality | The explicit call to `AdjustTokenPrivileges` to acquire `SeShutdownPrivilege` indicates an attempt to obtain elevated privileges beyond the standard user's scope. |
| T1497 | Virtualization/Sandbox Evasion | The use of `GetTickCount` to implement delays or timing checks is a common method used to bypass automated sandboxes and static analysis environments. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   None detected.

### **File paths / Registry keys**
*   **Note:** While the analysis mentions the use of `GetTempPathW` and the generation of files following the pattern `~nsu%X.tmp`, these are standard NSIS (Nullsoft Script Installer) behaviors and do not constitute unique, specific malicious file paths or registry keys in this context.

### **Mutex names / Named pipes**
*   None detected.

### **Hashes**
*   None detected.

### **Other artifacts**
*   **Anti-Analysis Techniques:** Use of `GetTickCount` (likely for timing checks to detect sandboxed environments).
*   **Privilege Escalation:** Acquisition of `SeShutdownPrivilege` via `AdjustTokenPrivileges`.
*   **Evasion Technique:** Dynamic loading of DLLs using `LoadLibraryExW` and `GetSystemDirectoryW` to potentially bypass static analysis.
*   **Payload Wrapper:** Identification as a multistage "dropper" or installer wrapper (NSIS-based).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper
3. **Confidence**: High
4. **Key evidence**: 
*   **Staged Payload Delivery:** The binary utilizes an NSIS-style installer wrapper to extract, unpack, and verify the integrity of hidden files in temporary directories before execution, a classic hallmark of a first-stage dropper.
*   **Evasion Techniques:** The inclusion of anti-analysis measures (e.g., `GetTickCount` for timing checks) and masquerading as a legitimate software installer are specific tactics used to bypass automated sandboxes and manual scrutiny.
*   **Environment Preparation:** The use of dynamic library loading (`LoadLibraryExW`) and privilege escalation attempts indicates the binary is designed to prepare the system environment and ensure the second-stage payload can run successfully without interference.
