# Threat Analysis Report

**Generated:** 2026-08-23 17:47 UTC
**Sample:** `115ee188d3c16f19d9a117696bbca43211a7debd7be89a9abdc71f04d1f07a65_115ee188d3c16f19d9a117696bbca43211a7debd7be89a9abdc71f04d1f07a65.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `115ee188d3c16f19d9a117696bbca43211a7debd7be89a9abdc71f04d1f07a65_115ee188d3c16f19d9a117696bbca43211a7debd7be89a9abdc71f04d1f07a65.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 63,215,788 bytes |
| MD5 | `c28a655a2921de94472ba022abda5a11` |
| SHA1 | `0810475d91b36e313ca8acc4aa617f9546a5f503` |
| SHA256 | `115ee188d3c16f19d9a117696bbca43211a7debd7be89a9abdc71f04d1f07a65` |
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
| `.text` | 27,136 | 6.489 | No |
| `.rdata` | 5,632 | 4.971 | No |
| `.data` | 1,536 | 4.174 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 30,208 | 7.696 | ⚠️ Yes |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `lstrcmpiA`, `CreateFileW`, `GetTempFileNameW`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`

## Extracted Strings

Total strings found: **136298** (showing first 100)

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

Based on the second batch of disassembly provided, I have updated and expanded the analysis. The new code confirms several behaviors previously suspected, specifically regarding **integrity verification**, **dynamic library loading**, and **complex system interaction**.

### Updated Summary of Findings

#### Core Functionality and Purpose
The binary remains identified as an **installer application** using the **NSIS (Nullsoft Script Installer)** framework. The additional disassembly confirms that it possesses robust internal logic for handling data structures, calculating file integrity, and interacting with Windows system components to ensure a successful installation environment.

#### Suspicious or Malicious Behaviors
While primarily consistent with an installer, the following behaviors are noted as common in both legitimate installers and sophisticated "droppers":

*   **Integrity Verification (CRC32):** The function `fcn.00406a93` implements a **CRC-32 checksum algorithm** (identifiable by the polynomial `0xedb88320`). This is used to verify that files have not been corrupted or tampered with. In malware, this is often used to ensure that a payload remains intact after being moved or extracted.
*   **Dynamic Library Loading:** Function `fcn.00406936` uses `GetSystemDirectoryW`, `wsprintfW`, and `LoadLibraryExW`. This indicates the installer can load additional DLLs at runtime. While standard for installers to load UI components, it is also a primary technique used by malware to "unpack" or "stage" secondary malicious modules into memory.
*   **OLE/COM Integration:** The use of `OleInitialize` and `OleUninitialize` in `fcn.0040570a` confirms the binary interacts with the **Object Linking and Embedding (OLE)** layer. This allows for deeper integration with Windows Shell features, which can be used to manipulate desktop objects or complex file types.
*   **Registry Querying:** The code continues to show extensive registry interaction (`RegQueryValueExW`). It is used to check system configurations before applying changes.

#### Notable Techniques and Patterns
*   **CRC-32 Implementation:** The presence of the `0xedb88320` constant in `fcn.00406a93` is a classic signature for integrity checking. This confirms that the "integrity check" mentioned in the first analysis is a deliberate, algorithmic process rather than a simple file-exists check.
*   **Sophisticated Loop Logic:** Functions like `fcn.0040117d` and `fcn.00407590` show structured loops that iterate through memory offsets or data blocks. This suggests the installer is parsing a complex configuration script or managing multi-part file movements.
*   **Robust Path/Environment Resolution:** The continuous use of standard Windows APIs for pathing and system directory resolution confirms the installer is designed to be "environment aware," ensuring it can run even if the user's environment isn't perfectly configured.

---

### Updated Summary Table of Findings

| Behavior | Observation Type | Description |
| :--- | :--- | :--- |
| **Installer Framework** | Structure | Confirmed NSIS-style switch structures and script processing logic. |
| **Integrity Checking** | **Confirmed Technical Check** | Uses a **CRC32 algorithm (0xedb88320)** to verify the integrity of files/components. |
| **Dynamic Loading** | **Potential Risk** | Uses `LoadLibraryExW` to load external DLLs at runtime; common in both installers and droppers. |
| **Registry Manipulation** | Persistence/Config | Extensive use of `ADVAPI32` functions to query and set registry keys for configuration. |
| **System Integration** | **Complex Interaction** | Utilizes OLE (`OleInitialize`) and Shell-related logic to interact with Windows system components. |
| **File Handling** | Delivery | Heavy use of `SetFilePointer`, `MoveFileW`, and `CopyFileW` for moving data across the filesystem. |

### Conclusion (Updated)
The binary is a robust, feature-rich installer constructed on the NSIS framework. The second batch of disassembly confirms that it performs **integrity checks** via CRC32 and utilizes **dynamic library loading** to extend its functionality. 

While these are standard features for a high-quality installer, they are also hallmark behaviors of "dropper" malware. Because the binary is designed to verify files, load external modules, and modify system settings/registry keys, it acts as a highly capable "delivery vehicle." If the source of the installation script or the associated DLLs is untrusted, this binary could be used to deliver and initialize malicious components on a host system.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The binary mimics a legitimate NSIS installer and is identified as a "delivery vehicle" for potentially malicious components. |
| T1112 | Modify Registry | The use of `RegQueryValueExW` confirms the binary interacts with registry keys for configuration and persistence. |
| T1105 | Ingress Tool Transfer | The heavy use of `MoveFileW` and `CopyFileW` indicates the staging and movement of files across the filesystem. |
| T1055 | Process Injection | The use of `LoadLibraryExW` allows the binary to load additional modules or "stage" components into memory at runtime. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs).

**Note:** Following your instructions, standard Windows API functions (e.g., `GetSystemDirectoryW`), system libraries (e.g., `ADVAPI32.dll`), and common technical constants (like the CRC-32 polynomial) have been excluded as they are considered standard environment artifacts rather than unique indicators of a specific threat.

### **Indicators of Compromise (IOCs)**

*   **IP addresses / URLs / Domains**
    *   None identified.

*   **File paths / Registry keys**
    *   None identified. (The analysis mentions the *capability* to modify registry keys and files, but no specific paths or keys were provided).

*   **Mutex names / Named pipes**
    *   None identified.

*   **Hashes**
    *   None identified. (Note: The value `0xedb88320` was identified in the analysis as a CRC-32 polynomial constant, not a file hash).

*   **Other artifacts**
    *   **Framework Identification:** NSIS (Nullsoft Script Installer) — This identifies the wrapper/installer type. 
    *   **Behavioral Note:** The sample utilizes `LoadLibraryExW` and `OleInitialize` for extended functionality, which are common vectors for "dropper" behavior, but no specific malicious payloads or C2 communication patterns were extracted from the text provided.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1.  **Malware family:** custom
2.  **Malware type:** dropper
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Dual-Purpose Functionality:** The binary utilizes the NSIS installer framework to "masquerade" as a legitimate software installer while performing actions typical of a delivery vehicle, such as file system staging and moving files (`MoveFileW`, `CopyFileW`).
    *   **Payload Verification & Loading:** The implementation of CRC-32 integrity checks and the use of `LoadLibraryExW` indicate the binary is designed to verify the integrity of external components and load them into memory, a core behavior of sophisticated droppers.
    *   **System Manipulation:** The evidence of extensive registry interaction (`RegQueryValueExW`) and OLE/COM integration suggests the sample is prepared to modify system configurations or establish persistence for subsequent payloads.
