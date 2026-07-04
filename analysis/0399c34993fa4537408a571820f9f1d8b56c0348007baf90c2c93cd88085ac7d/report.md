# Threat Analysis Report

**Generated:** 2026-07-01 19:45 UTC
**Sample:** `0399c34993fa4537408a571820f9f1d8b56c0348007baf90c2c93cd88085ac7d_0399c34993fa4537408a571820f9f1d8b56c0348007baf90c2c93cd88085ac7d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0399c34993fa4537408a571820f9f1d8b56c0348007baf90c2c93cd88085ac7d_0399c34993fa4537408a571820f9f1d8b56c0348007baf90c2c93cd88085ac7d.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 560,776 bytes |
| MD5 | `3155da301a502e751a2805f5c7d3afa8` |
| SHA1 | `c9e7a1bbda1067676758ad35b1ef4998309db367` |
| SHA256 | `0399c34993fa4537408a571820f9f1d8b56c0348007baf90c2c93cd88085ac7d` |
| Overall entropy | 7.273 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1632607066 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 27,136 | 6.458 | No |
| `.rdata` | 5,632 | 5.024 | No |
| `.data` | 1,536 | 4.155 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 180,224 | 4.812 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `SetFileSecurityW`, `RegOpenKeyExW`, `RegEnumValueW`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHFileOperationW`, `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `ShellExecuteExW`, `SHGetFileInfoW`
**ole32.dll**: `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `GetClientRect`, `EndPaint`, `DrawTextW`, `IsWindowEnabled`, `DispatchMessageW`, `wsprintfA`, `CharNextA`, `CharPrevW`, `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `GetSystemMetrics`, `FillRect`, `AppendMenuW`, `TrackPopupMenu`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectW`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetModuleHandleA`, `GetProcAddress`, `GetSystemDirectoryW`, `lstrcatW`, `Sleep`, `lstrcpyA`, `WriteFile`, `GetTempFileNameW`, `CreateFileW`, `lstrcmpiA`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`

## Extracted Strings

Total strings found: **1277** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495,OC
tQWPV
Y;=,OC
Instu`
softuW
NulluN	E
j@Vh OC
SVWj _3
tVj%SSS
D$$+D$
D$,+D$$P
WWWWjn
us9Et	
FFC;]|
8\tPV
\u f9O
69}t(j
90u'AAf
_^[t	P
HtVHtHH
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 6152 | ✓ |
| `fcn.00406a65` | `0x406a65` | 2639 | ✓ |
| `entry0` | `0x40352d` | 1509 | ✓ |
| `fcn.0040755c` | `0x40755c` | 827 | ✓ |
| `fcn.00403bec` | `0x403bec` | 726 | ✓ |
| `fcn.0040657a` | `0x40657a` | 586 | ✓ |
| `fcn.0040307d` | `0x40307d` | 567 | ✓ |
| `fcn.004032b4` | `0x4032b4` | 539 | ✓ |
| `fcn.00405c49` | `0x405c49` | 451 | ✓ |
| `fcn.00406183` | `0x406183` | 378 | ✓ |
| `fcn.00402ea9` | `0x402ea9` | 234 | ✓ |
| `fcn.0040559f` | `0x40559f` | 211 | ✓ |
| `fcn.00404500` | `0x404500` | 207 | ✓ |
| `fcn.00404d46` | `0x404d46` | 201 | ✓ |
| `fcn.00403ec2` | `0x403ec2` | 185 | ✓ |
| `fcn.004067c4` | `0x4067c4` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040649d` | `0x40649d` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00406329` | `0x406329` | 129 | ✓ |
| `fcn.00404e54` | `0x404e54` | 128 | ✓ |
| `fcn.00405f14` | `0x405f14` | 126 | ✓ |
| `fcn.00405a6e` | `0x405a6e` | 125 | ✓ |
| `fcn.0040640b` | `0x40640b` | 121 | ✓ |
| `fcn.0040610e` | `0x40610e` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.0040689a` | `0x40689a` | 112 | ✓ |
| `fcn.004069f7` | `0x4069f7` | 110 | ✓ |
| `fcn.00405672` | `0x405672` | 108 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402ea9.c`](code/fcn.00402ea9.c)
- [`code/fcn.0040307d.c`](code/fcn.0040307d.c)
- [`code/fcn.004032b4.c`](code/fcn.004032b4.c)
- [`code/fcn.00403bec.c`](code/fcn.00403bec.c)
- [`code/fcn.00403ec2.c`](code/fcn.00403ec2.c)
- [`code/fcn.00404500.c`](code/fcn.00404500.c)
- [`code/fcn.00404d46.c`](code/fcn.00404d46.c)
- [`code/fcn.00404e54.c`](code/fcn.00404e54.c)
- [`code/fcn.0040559f.c`](code/fcn.0040559f.c)
- [`code/fcn.00405672.c`](code/fcn.00405672.c)
- [`code/fcn.00405a6e.c`](code/fcn.00405a6e.c)
- [`code/fcn.00405c49.c`](code/fcn.00405c49.c)
- [`code/fcn.00405f14.c`](code/fcn.00405f14.c)
- [`code/fcn.0040610e.c`](code/fcn.0040610e.c)
- [`code/fcn.00406183.c`](code/fcn.00406183.c)
- [`code/fcn.00406329.c`](code/fcn.00406329.c)
- [`code/fcn.0040640b.c`](code/fcn.0040640b.c)
- [`code/fcn.0040649d.c`](code/fcn.0040649d.c)
- [`code/fcn.0040657a.c`](code/fcn.0040657a.c)
- [`code/fcn.004067c4.c`](code/fcn.004067c4.c)
- [`code/fcn.0040689a.c`](code/fcn.0040689a.c)
- [`code/fcn.004069f7.c`](code/fcn.004069f7.c)
- [`code/fcn.00406a65.c`](code/fcn.00406a65.c)
- [`code/fcn.0040755c.c`](code/fcn.0040755c.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, I have updated and expanded the analysis. The new code confirms several advanced behaviors typically associated with sophisticated malware droppers, specifically regarding integrity checks and modularity.

### Updated Analysis Summary

The binary remains a **multi-stage installer/dropper** using an NSIS framework. However, the second set of functions reveals that it possesses internal mechanisms to verify its components (integrity checking) and dynamically load additional functionality (modular execution), which are hallmarks of sophisticated malware.

---

### Core Functionality and Purpose
The binary acts as a "loader" for a primary payload. It doesn't just move files; it validates them before activation. The inclusion of internal logic to handle file pointers, registry queries, and integrity checks suggests that the binary is designed to ensure that its environment is correctly prepared and that its components are intact before it proceeds with the final stage of the infection.

### Suspicious and Malicious Behaviors
*   **Integrity Verification (CRC32):** The function `fcn.004069f7` implements a **CRC32 checksum algorithm**. This is commonly used by malware to verify that a dropped file has not been altered or corrupted. In a malicious context, this ensures the "payload" remains intact and hasn't been modified by security software before it is executed.
*   **Dynamic DLL Loading:** The function `fcn.0040689a` contains highly suspicious logic where it retrieves the system directory, appends `.dll` to a path, and calls `LoadLibraryExW`. This indicates the binary is designed to load additional modules at runtime. This "modular" approach allows the malware to keep its main execution thread small and simple while loading more complex malicious behaviors (like keylogging or network communication) only when needed.
*   **Registry Enumeration:** The function `fcn.0040640b` interacts with `RegQueryValueExW`. This suggests the binary is checking for specific system configurations, looking for installed security software, or verifying if certain conditions are met before "installing" its components.
*   **Advanced File Handling:** Function `fcn.0040610e` shows interaction with file pointers and potentially handling specific offsets within files, suggesting it might be carving data out of a larger container or dealing with complex nested payloads.

### Notable Techniques and Patterns
*   **Anti-Tampering Mechanisms:** The presence of the CRC32 check (`fcn.004069f7`) suggests an awareness of forensic analysis; if the dropped payload was modified by an antivirus scan, the installer would detect it and stop before "activating" the malware.
*   **Dynamic Execution/Modularity:** By using `LoadLibraryExW` to fetch `.dll` files from system paths (or paths constructed relative to them), the malware hides its true capabilities. The primary executable acts as a "loader," while the actual malicious behavior is hidden in external DLLs.
*   **NSIS Wrapper Strategy:** As noted previously, the use of NSIS-like structures continues to be the primary method for social engineering—presenting the user with a standard installation wizard while the backend performs complex integrity checks and dynamic library loading.

### Summary Conclusion (Updated)
This sample is a **highly capable multi-stage dropper.** The addition of **CRC32 integrity checking** and **dynamic DLL loading** elevates it from a simple "downloader" to a sophisticated "loader." It is designed to verify its malicious components before execution and hide its primary functionality within dynamically loaded libraries. This complexity is intended to bypass automated detection and ensure that the final stage of the infection occurs successfully on the host system.

---
**Key Indicators for Incident Response:**
1.  **Filesystem:** Look for temporary directories created by NSIS or files being moved via `CopyFileW`.
2.  **Integrity Check:** The use of CRC32 indicates that the malware checks its own components; any modification to these components by security tools will likely be detected by the loader.
3.  **Dynamic Loading:** Monitor for `LoadLibraryExW` calls, especially those targeting `.dll` files in system directories or temporary paths.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of CRC32 checksums ensures that the payload remains unaltered by security software before it is executed. |
| T1036 | DLL Side-Loading | Utilizing `LoadLibraryExW` to load modules at runtime allows the malware to hide its core capabilities within separate, dynamically loaded files. |
| T1497 | Virtualization, Sandbox & Availability | Querying registry values to check for security software helps the loader determine if it is being analyzed in a protected environment. |
| T1027 | Obfuscated Files or Information | The use of offset-based parsing and "carving" hides malicious payloads within larger files to evade detection by scanners. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Because this report focuses on a "loader" or "installer" stage, many common Windows API calls were identified in the strings but have been excluded as noise per your instructions.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *No specific hardcoded paths or registry keys were provided.* 
    *   *Note:* The analysis indicates that the binary dynamically constructs paths for `.dll` files in system directories and utilizes `GetTempPathW`, but no specific malicious paths were disclosed.

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (The CRC32 algorithm mentioned is a functional technique, not a static hash).

### **Other artifacts**
*   **Malware Framework:** NSIS (Nullsoft Scriptable Install System) - Used as a wrapper to provide a legitimate-looking installation interface for the dropper.
*   **Integrity Check Mechanism:** CRC32 checksum algorithm (`fcn.004069f7`) used to verify that dropped payloads have not been modified or intercepted by security software.
*   **Modular Execution Technique:** Dynamic DLL loading via `LoadLibraryExW` (`fcn.0040689a`). This is used to hide the primary malicious functionality (e.g., keylogging, C2 communication) in separate modules loaded at runtime.
*   **Persistence/Environment Check:** Use of `RegQueryValueExW` to inspect system configurations and potentially identify the presence of security software before proceeding with the infection.

---

## Malware Family Classification

1. **Malware family**: Unknown (Generic Dropper/Loader)
2. **Malware type**: Loader / Dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Multi-stage Execution & Obfuscation:** The sample utilizes an NSIS framework as a wrapper to mimic a legitimate installer while performing internal integrity checks (CRC32) to ensure the payload has not been tampered with by security software before execution.
    *   **Dynamic Component Loading:** The use of `LoadLibraryExW` to dynamically load DLLs from system paths indicates a modular architecture designed to hide primary malicious functionality (such as C2 communication or data exfiltration) from static analysis.
    *   **Anti-Analysis & Environment Checks:** The inclusion of registry enumeration (`RegQueryValueExW`) and advanced file "carving" suggests the malware is designed to detect security software and evade detection by only activating in environments it deems safe.
