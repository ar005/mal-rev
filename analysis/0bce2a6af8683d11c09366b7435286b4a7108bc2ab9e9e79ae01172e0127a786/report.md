# Threat Analysis Report

**Generated:** 2026-07-27 18:09 UTC
**Sample:** `0bce2a6af8683d11c09366b7435286b4a7108bc2ab9e9e79ae01172e0127a786_0bce2a6af8683d11c09366b7435286b4a7108bc2ab9e9e79ae01172e0127a786.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0bce2a6af8683d11c09366b7435286b4a7108bc2ab9e9e79ae01172e0127a786_0bce2a6af8683d11c09366b7435286b4a7108bc2ab9e9e79ae01172e0127a786.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 1,069,592 bytes |
| MD5 | `f0f2b3b0e64e02eca6bf0de056dba547` |
| SHA1 | `7407cec998748c986c903a4b25daad9bceeb9497` |
| SHA256 | `0bce2a6af8683d11c09366b7435286b4a7108bc2ab9e9e79ae01172e0127a786` |
| Overall entropy | 7.485 |
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
| `.text` | 27,136 | 6.489 | No |
| `.rdata` | 5,632 | 4.971 | No |
| `.data` | 1,536 | 4.174 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 297,984 | 4.741 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `lstrcmpiA`, `CreateFileW`, `GetTempFileNameW`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`

## Extracted Strings

Total strings found: **2865** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495,GC
tQWPV
Y;=,GC
Instuj
softua
NulluX	E
j@Vh GC
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 6196 | ✓ |
| `fcn.00406b01` | `0x406b01` | 2639 | ✓ |
| `entry0` | `0x40358d` | 1565 | ✓ |
| `fcn.004075f8` | `0x4075f8` | 827 | ✓ |
| `fcn.00403c84` | `0x403c84` | 726 | ✓ |
| `fcn.004065ef` | `0x4065ef` | 625 | ✓ |
| `fcn.004030a9` | `0x4030a9` | 619 | ✓ |
| `fcn.00403314` | `0x403314` | 539 | ✓ |
| `fcn.00405cbe` | `0x405cbe` | 451 | ✓ |
| `fcn.004061f8` | `0x4061f8` | 378 | ✓ |
| `fcn.00402ed5` | `0x402ed5` | 234 | ✓ |
| `fcn.00405637` | `0x405637` | 211 | ✓ |
| `fcn.00404598` | `0x404598` | 207 | ✓ |
| `fcn.00404dde` | `0x404dde` | 201 | ✓ |
| `fcn.00403f5a` | `0x403f5a` | 185 | ✓ |
| `fcn.00406860` | `0x406860` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00406512` | `0x406512` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.0040639e` | `0x40639e` | 129 | ✓ |
| `fcn.00404eec` | `0x404eec` | 128 | ✓ |
| `fcn.00405f89` | `0x405f89` | 126 | ✓ |
| `fcn.00406480` | `0x406480` | 121 | ✓ |
| `fcn.00406183` | `0x406183` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406936` | `0x406936` | 112 | ✓ |
| `fcn.00406a93` | `0x406a93` | 110 | ✓ |
| `fcn.0040570a` | `0x40570a` | 108 | ✓ |
| `fcn.00407590` | `0x407590` | 104 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402ed5.c`](code/fcn.00402ed5.c)
- [`code/fcn.004030a9.c`](code/fcn.004030a9.c)
- [`code/fcn.00403314.c`](code/fcn.00403314.c)
- [`code/fcn.00403c84.c`](code/fcn.00403c84.c)
- [`code/fcn.00403f5a.c`](code/fcn.00403f5a.c)
- [`code/fcn.00404598.c`](code/fcn.00404598.c)
- [`code/fcn.00404dde.c`](code/fcn.00404dde.c)
- [`code/fcn.00404eec.c`](code/fcn.00404eec.c)
- [`code/fcn.00405637.c`](code/fcn.00405637.c)
- [`code/fcn.0040570a.c`](code/fcn.0040570a.c)
- [`code/fcn.00405cbe.c`](code/fcn.00405cbe.c)
- [`code/fcn.00405f89.c`](code/fcn.00405f89.c)
- [`code/fcn.00406183.c`](code/fcn.00406183.c)
- [`code/fcn.004061f8.c`](code/fcn.004061f8.c)
- [`code/fcn.0040639e.c`](code/fcn.0040639e.c)
- [`code/fcn.00406480.c`](code/fcn.00406480.c)
- [`code/fcn.00406512.c`](code/fcn.00406512.c)
- [`code/fcn.004065ef.c`](code/fcn.004065ef.c)
- [`code/fcn.00406860.c`](code/fcn.00406860.c)
- [`code/fcn.00406936.c`](code/fcn.00406936.c)
- [`code/fcn.00406a93.c`](code/fcn.00406a93.c)
- [`code/fcn.00406b01.c`](code/fcn.00406b01.c)
- [`code/fcn.00407590.c`](code/fcn.00407590.c)
- [`code/fcn.004075f8.c`](code/fcn.004075f8.c)

## Behavioral Analysis

Based on the additional disassembly provided, I have updated and extended the analysis of the binary. The new code segments provide more insight into how the program handles data integrity, system resources, and dynamic library loading.

### Updated Analysis Report

#### Core Functionality and Purpose
The binary continues to exhibit characteristics of a **software installer or setup utility**, specifically one utilizing the **Nullsoft Script Installer (NSIS)** framework. The underlying logic confirms that it manages complex internal states, handles file system navigation, and interacts with Windows system components to facilitate an installation process.

#### Suspicious or Malicious Behaviors
In addition to the previously identified behaviors (File Manipulation, Registry Modification, Privilege Escalation, and Environment Modification), the new disassembly reveals the following:

*   **Dynamic Library Loading:** Function `fcn.00406936` specifically targets the system directory to construct a path for a `.dll` file and then calls `LoadLibraryExW`. 
    *   *Malicious Context:* While installers use this to load plugin components, it is also a primary method used by malware to load "payload" DLLs into memory after they have been dropped. The specific way the path is constructed suggests the program can dynamically determine which library to load based on its environment.
*   **Data Integrity Verification:** Function `fcn.00406a93` implements a mathematical algorithm (specifically, it appears to be a **CRC-32 or similar checksum calculation** using the polynomial `0xedb88320`). 
    *   *Malicious Context:* In an installer, this is used to ensure that files were not corrupted during the copy process. In malware, this is frequently used to verify that a dropped payload has been successfully written to disk or to verify the integrity of data received from a Command and Control (C2) server.
*   **OLE Initialization:** The use of `OleInitialize` and `OleUninitialize` (in `fcn.0040570a`) indicates the program interacts with Windows' Object Linking and Embedding libraries. While standard for complex UI components, it is also used by malware to interact with certain system objects or host applications.

#### Notable Techniques and Patterns
*   **Complex Buffer/State Management:** Functions like `fcn.0040117d` and `fcn.00407590` contain complex pointer arithmetic and loop structures. These are typical of the "back-end" logic of a script-based installer, where it must track multiple states (e.g., UI elements, installation steps, or progress percentages).
*   **File Navigation & Seek:** Function `fcn.00406183` utilizes `SetFilePointer` with specific offsets. This indicates the binary is capable of "seeking" within files to find specific data chunks, common when handling packed or compressed installer resources.
*   **Registry Value Retrieval:** The update confirms the use of `RegQueryValueExW` in `fcn.00406480`, which allows the program to pull configuration data directly from the Windows Registry.

### Updated Summary Conclusion
The binary remains consistent with a **sophisticated installer utility**. However, the inclusion of **CRC-style integrity checks** and **dynamic DLL loading via constructed paths** increases its "capability profile." 

While these features are standard for high-quality installers to ensure a smooth user experience, they are also significant indicators in malware analysis. The binary is effectively designed to:
1.  Verify that data (files or code) remains intact after being moved/copied.
2.  Dynamically load additional functionality from the system or local folders.
3.  Perform complex state management to handle a multi-step installation process.

**Updated Recommendation:** The file should be treated as **potentially suspicious**. While it is likely a legitimate installer, its ability to perform integrity checks and dynamically load libraries means it possesses the necessary "building blocks" for a dropper or downloader. It should be executed in a controlled sandbox environment where network traffic and file system changes are monitored.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1601** | Reflective Code Loading | The use of `LoadLibraryExW` to load DLLs from dynamically constructed paths is a primary method for injecting and executing "payload" components. |
| **T1611** | Dynamic Resolution | The report notes the program's ability to determine which library to load based on its environment, indicating dynamic resolution of resources or capabilities. |
| **T1036** | Masquerading | Registry queries (`RegQueryExW`) are commonly used by installers (and malware) to gather system information and tailor their behavior to blend in with legitimate software. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: While the analysis mentions the *capability* to construct file paths and query registry values using `RegQueryValueExW`, no specific hardcoded paths or registry keys were provided in the text.)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **CRC-32 Polynomial:** `0xedb88320` (Used for data integrity verification).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: Medium

**Key evidence**:
*   **Dual-Use Functionality:** The binary employs `LoadLibraryExW` for dynamic library loading and CRC-32 checksums (`0xedb88320`) for data integrity. While common in legitimate installers, these are primary technical "building blocks" for droppers to verify and execute malicious payloads.
*   **Potential as a Wrapper:** The analysis identifies the binary as an NSIS-based installer. In malware campaigns, such sophisticated installers are frequently used as wrappers or loaders to hide subsequent malicious components from signature-based detection.
*   **Ambiguous Intent:** No specific Command and Control (C2) infrastructure or known malware signatures were identified; however, its ability to manipulate files, modify the registry, and dynamically resolve resources confirms it has the necessary capabilities to serve as a delivery vehicle in a multi-stage attack.
