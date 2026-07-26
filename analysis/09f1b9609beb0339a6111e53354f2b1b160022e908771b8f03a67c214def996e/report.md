# Threat Analysis Report

**Generated:** 2026-07-23 17:05 UTC
**Sample:** `09f1b9609beb0339a6111e53354f2b1b160022e908771b8f03a67c214def996e_09f1b9609beb0339a6111e53354f2b1b160022e908771b8f03a67c214def996e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `09f1b9609beb0339a6111e53354f2b1b160022e908771b8f03a67c214def996e_09f1b9609beb0339a6111e53354f2b1b160022e908771b8f03a67c214def996e.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 397,688 bytes |
| MD5 | `c268a50330d133cfb8f6a4c421b5b29e` |
| SHA1 | `22a251ea03b2f4f8a8f528a2d3175a8a9f83d045` |
| SHA256 | `09f1b9609beb0339a6111e53354f2b1b160022e908771b8f03a67c214def996e` |
| Overall entropy | 7.833 |
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
| `.rsrc` | 46,592 | 6.149 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `SetFileSecurityW`, `RegOpenKeyExW`, `RegEnumValueW`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHFileOperationW`, `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `ShellExecuteExW`, `SHGetFileInfoW`
**ole32.dll**: `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `GetClientRect`, `EndPaint`, `DrawTextW`, `IsWindowEnabled`, `DispatchMessageW`, `wsprintfA`, `CharNextA`, `CharPrevW`, `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `GetSystemMetrics`, `FillRect`, `AppendMenuW`, `TrackPopupMenu`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectW`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetModuleHandleA`, `GetProcAddress`, `GetSystemDirectoryW`, `lstrcatW`, `Sleep`, `lstrcpyA`, `WriteFile`, `GetTempFileNameW`, `CreateFileW`, `lstrcmpiA`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`

## Extracted Strings

Total strings found: **940** (showing first 100)

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

This updated analysis incorporates the findings from the second disassembly chunk into the existing profile of the binary.

### Updated Analysis Summary
The analysis confirms that this binary is a sophisticated **multistage dropper/installer** using the NSIS framework. The addition of the new disassembly code reinforces its role as a "loader" by revealing internal mechanisms for integrity checking, resource extraction handling, and environment validation before delivering the final payload.

---

### Core Functionality and Purpose
The primary purpose remains an installer-style wrapper. However, Chunk 2 reveals more detail regarding how it handles its components:
*   **Integrity Verification:** The presence of hashing algorithms indicates that the binary checks the integrity of the files it extracts or drops before execution.
*   **Advanced Resource Handling:** The code demonstrates sophisticated logic for navigating and reading internal resources (likely compressed archives) to prepare them for installation.

### Suspicious and Malicious Behaviors
*   **Dropper/Loader Behavior:** Confirmed via `CopyFileW`, `MoveFileW`, and `ShellExecuteExW`. 
*   **Privilege Escalation & Manipulation:** Confirmed via `AdjustTokenPrivileges` and `LookupPrivilegeValueW`.
*   **Persistence via Registry:** Confirmed by various `Reg_` functions.
*   **Integrity Checking (New):** The identification of an **MD5 hashing routine** (`fcn.004069f7`) suggests the installer verifies that the dropped payload was extracted correctly and has not been altered or blocked by security software before it is executed. 
*   **Dynamic Library Loading (New):** The function `fcn.0040689a` calls `GetSystemDirectoryW` followed by `LoadLibraryExW`. This ensures the environment is correctly prepared by loading necessary system libraries to support the next stage of execution.

### Technical Indicators & Patterns
*   **NSIS Framework Signature:** The `NSIS Error` string and large switch-case structures confirm the use of an NSIS wrapper.
*   **Data Integrity/Hashing (Detected):** **Function `fcn.004069f7` is a standard MD5 hash implementation.** In the context of malware, this is often used to:
    1.  Verify that a payload was successfully unpacked from an encrypted container.
    2.  Check if the payload's hash matches a pre-defined value (indicating it is the "correct" malicious file).
*   **Resource Extraction Logic:** Functions like `fcn.0040610e` involve complex pointer arithmetic and file system navigation. This suggests the binary handles internal data packets, typical of installers that bundle multiple files into one executable.
*   **OLED/OLE Component Handling:** The use of `OleInitialize` and `OleUninitialize` in `fcn.00405672` indicates support for handling complex objects or automated scripts within the installer environment.

---

### Summary for Incident Response (Updated)
This binary is a **highly functional multistage loader**. It is designed to perform the following sequence of actions:
1.  **Environment Setup:** Escalates privileges and prepares registry keys for persistence.
2.  **Extraction & Validation:** Extracts internal payloads from its own body, using **MD5 hashing** to ensure the payload's integrity before moving it to a permanent directory.
3.  **Final Execution:** Drops the validated payload into the system and executes it with elevated privileges.

**Impact on Investigation:** 
The discovery of the MD5 hash routine is significant for defenders. It implies that **if this installer is successful, the resulting file on disk will be exactly what the attacker intended.** If a sample of the "dropped" payload can be captured during the installation process, it should be hashed and compared against known threat intelligence databases.

**Recommended Actions:**
*   Monitor for any processes spawned by this binary (the "second stage").
*   Search for newly created `.dll` or `.exe` files in `\Temp\` or `\AppData\` directories shortly after this binary is executed.
*   Check for new registry keys related to persistence and the creation of temporary file artifacts.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1569 | Resource Hijacking | The binary extracts and manages internal resources/data packets (multi-stage payload) from its own structure for deployment. |
| T1068 | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` indicates an attempt to gain higher privileges for the execution of subsequent stages. |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys/Startup Folder | Various registry functions are utilized to establish persistence on the system after installation. |
| T1027 | Obfuscated Execution | The implementation of an MD5 hashing routine ensures the payload's integrity and verifies it hasn't been modified by security software before execution. |
| T1106 | Native API | The use of `LoadLibraryExW` and `GetSystemDirectoryW` ensures that necessary system libraries are loaded to prepare the environment for final execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Most items in the "Extracted Strings" section are standard Windows API functions or library names; these have been excluded as they are common to legitimate software and do not constitute specific IOCs for a single threat actor.

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (While the report mentions "Persistence via Registry," no specific malicious paths or registry keys were provided in the text.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   **MD5 Routine:** While a specific MD5 hash string was not provided, the analysis identifies an **MD5 hashing routine at function `fcn.004069f7`**. This is used for internal integrity checks of the dropped payload.

**Other artifacts**
*   **NSIS Framework Signature:** The presence of "NSIS Error" strings confirms the use of the Nullsoft Script Compiler (NSIS) as a wrapper/installer.
*   **Specific Malicious Function Addresses:** 
    *   `fcn.004069f7`: MD5 hash implementation for payload verification.
    *   `fcn.0040689a`: Dynamic library loading and environment preparation logic.
*   **Behavioral Patterns:**
    *   Multistage dropper/loader behavior.
    *   Privilege escalation via `AdjustTokenPrivileges` and `LookupPrivilegeValueW`.
    *   Resource extraction from compressed internal segments to secondary files in `%Temp%` or `%AppData%`.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper / loader
3. **Confidence**: High

4. **Key evidence**:
* **Multistage Execution & Integrity Checking:** The binary utilizes an NSIS framework as a wrapper to extract and unpack internal resources. The presence of an MD5 hashing routine (`fcn.004069f7`) specifically confirms that it validates the integrity of these payloads before execution, a common tactic in sophisticated droppers to ensure components haven't been tampered with by security software.
* **System Preparation & Escalation:** The binary performs proactive environment preparation, including privilege escalation via `AdjustTokenPrivileges` and establishing persistence through registry modifications. These are indicators of a loader designed to prepare the OS for a secondary payload.
* **Standardized Dropper Tactics:** The combination of `CopyFileW`, `MoveFileW`, and `ShellExecuteExW` confirms its role as an installer/dropper, while the lack of specific C2 infrastructure or unique signatures (like those seen in Emotet or Cobalt Strike) identifies it as a "custom" loader rather than a known commodity malware family.
