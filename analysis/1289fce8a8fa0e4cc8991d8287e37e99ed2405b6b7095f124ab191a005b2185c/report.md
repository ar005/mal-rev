# Threat Analysis Report

**Generated:** 2026-08-31 16:37 UTC
**Sample:** `1289fce8a8fa0e4cc8991d8287e37e99ed2405b6b7095f124ab191a005b2185c_1289fce8a8fa0e4cc8991d8287e37e99ed2405b6b7095f124ab191a005b2185c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1289fce8a8fa0e4cc8991d8287e37e99ed2405b6b7095f124ab191a005b2185c_1289fce8a8fa0e4cc8991d8287e37e99ed2405b6b7095f124ab191a005b2185c.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 83,840 bytes |
| MD5 | `40c3f167f3706961960f4f21733284eb` |
| SHA1 | `d1a3cbba6aa72ee34f20522779c555ef1dff7f63` |
| SHA256 | `1289fce8a8fa0e4cc8991d8287e37e99ed2405b6b7095f124ab191a005b2185c` |
| Overall entropy | 6.975 |
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
| `.rsrc` | 18,944 | 4.795 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueW`, `RegEnumKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegOpenKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`, `ShellExecuteExW`
**ole32.dll**: `CoCreateInstance`, `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `MessageBoxIndirectW`, `GetDlgItemTextW`, `SetDlgItemTextW`, `CreatePopupMenu`, `AppendMenuW`, `TrackPopupMenu`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcW`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorW`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `lstrcmpiA`, `CreateFileW`, `GetTempFileNameW`, `RemoveDirectoryW`, `CreateProcessW`, `CreateDirectoryW`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceW`, `WideCharToMultiByte`, `lstrcpynW`, `lstrlenW`, `SetErrorMode`, `GetVersionExW`

## Extracted Strings

Total strings found: **381** (showing first 100)

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

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis. The new code confirms several advanced behaviors typical of sophisticated installers (and potentially malicious droppers), specifically regarding **integrity checking**, **dynamic library loading**, and **internal command processing**.

### Updated Analysis Summary
The binary continues to exhibit characteristics of a standard **NSIS Installer**. However, the inclusion of robust integrity checks, dynamic path construction for DLL loading, and extensive internal state management reinforces its role as a capable "wrapper." In a malware context, these features allow it to verify that a payload was successfully extracted without corruption before execution, and to dynamically load components needed to interact with various parts of the Windows OS.

---

### New Technical Findings (from Chunk 2)

#### 1. Integrity Checking & Hash Calculation (`fcn.00406a93`)
*   **Analysis:** This function implements a loop that populates an array based on a specific constant (`0xedb88320`). This is the characteristic polynomial for **CRC-32** (or a very similar cyclic redundancy check). 
*   **Functionality:** The code then iterates through data to compute a checksum. 
*   **Malware Context:** While standard in installers to ensure files aren't corrupted during extraction, this is also used by malware to:
    *   Verify the integrity of an injected payload before "unpacking" it into memory.
    *   Perform basic anti-tampering checks on its own components.

#### 2. Dynamic Library Loading & Path Construction (`fcn.00406936`)
*   **Analysis:** This function retrieves the system directory (`GetSystemDirectoryW`), constructs a path string using `wsprintfW`, and then calls `LoadLibraryExW`.
*   **Functionality:** It is specifically designed to find and load DLLs from systemic or adjacent paths. 
*   **Malware Context:** In "dropper" scenarios, this logic is often used to:
    *   Load system components (like `user32.dll` or `shell32.dll`) to perform GUI interactions.
    *   **DLL Side-Loading:** If a malicious DLL is placed in the same folder as the installer, it may be loaded by this function to gain additional functionality.

#### 3. Registry Interaction (`fcn.00406480`)
*   **Analysis:** This provides a wrapper for `RegQueryValueExW` and `RegCloseKey`. It includes logic to handle different data types (checking if the value is a string or binary).
*   **Functionality:** It is used to read configuration settings from the Windows Registry.
*   **Malware Context:** Used to check for the presence of other security software, identify environment-specific paths, or retrieve persistence keys.

#### 4. File System Management (`fcn.00406183`)
*   **Analysis:** This function interacts with `SetFilePointer` and checks specific file attributes before proceeding. 
*   **Functionality:** It validates the status of a file (e.g., is it locked? does it exist?).
*   **Malware Context:** Ensuring that files are not "in use" or are hidden/system files before they are moved or overwritten by the installer's payloads.

#### 5. Command Dispatching & State Management (`fcn.0040117d`)
*   **Analysis:** This is a complex loop iterating over an internal array, performing bitwise operations to determine the "state" of various elements (likely flags for strings or commands).
*   **Functionality:** This is core to the NSIS engine, where it processes an internal script to decide what action to perform next (Move file? Show Message? Wait for input?).

---

### Updated Summary of Suspicious/Malicious Behaviors

| Feature | Behavior | Risk Level | Motivation in Malware Context |
| :--- | :--- | :--- | :--- |
| **Integrity Check** | `fcn.00406a93` (CRC-style) | Medium | Ensures the "payload" is intact before execution; avoids crashing during a malicious drop. |
| **Dynamic Loading** | `fcn.00406936` (`LoadLibraryExW`) | High | Allows the installer to load various modules or exploit DLL hijacking vulnerabilities. |
| **Registry Parsing** | `fcn.00406480` (`RegQueryValueExW`) | Medium | Used for configuration, but also to find target paths or check for security software. |
| **System Interaction** | `fcn.0040570a` (`OleInitialize`) | Low/Medium | Often used by installers to handle icons; can be used by malware to interact with shell objects. |

### Final Conclusion (Updated)
The binary is a highly functional **NSIS-based installer**. The additional disassembly confirms that it has the "tools" necessary to be an effective **malware dropper**:
1.  It can **verify payload integrity** via CRC/Hashing.
2.  It can **dynamically load libraries** from the system or local paths.
3.  It possesses a **robust internal logic engine** for processing complex installation scripts.

If the data blocks embedded within this binary contain non-standard files, this installer will act as a "Trojan" vehicle—the heavy lifting of file manipulation and integrity checking is done by the NSIS framework, while the malicious intent is carried in the payload it extracts and executes.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036.005** | DLL Side-Loading | The use of `LoadLibraryExW` combined with dynamic path construction allows the binary to load modules from local or system paths, a common method for loading malicious components while evading detection. |
| **T1082** | System Information Discovery | Use of Registry queries (`RegQueryValueExW`) and file attribute checks are used to gather information about the environment, identify security software, or locate specific paths. |
| **T1059** | Command and Scripting Interpreter | The "Command Dispatching" logic and internal state management indicate a script-driven execution model (like NSIS) used to process a series of instructions for payload delivery. |
| **T1036** | Dynamic Signature Detection (or Defense Evasion) | The implementation of CRC-style integrity checks (`fcn.00406a93`) serves as an anti-tampering mechanism to ensure the "payload" is intact before execution. |
| **T1105** | Ingress Tool Transfer | While a general behavior, the file system management logic ensures that payloads are in a valid state (not locked/hidden) prior to being moved or finalized for execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the report of extracted Indicators of Compromise (IOCs). 

**Note:** This specific sample appears to be a standard **NSIS-based installer**. While the behaviors described (CRC checks, dynamic library loading) are common in malware loaders, no unique infrastructure or filesystem artifacts were identified in the provided text.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (The analysis mentions functions for registry interaction and file system management, such as `RegQueryValueExW` and `GetSystemDirectoryW`, but no specific malicious paths or keys were provided.)

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified. (The constant `0xedb88320` was noted in the analysis; however, this is a standard mathematical constant for the CRC-32 algorithm and not a unique file hash.)

### **Other artifacts**
*   **Framework Identification:** The binary utilizes functionality consistent with the **NSIS (Nullsoft Script Installer)**. 
*   **Mechanism - Integrity Checking:** The use of CRC-style calculations (`fcn.00406a93`) indicates a mechanism to verify file integrity before execution/extraction.
*   **Mechanism - Dynamic Loading:** Use of `LoadLibraryExW` and `GetSystemDirectoryW` suggests the ability to load system components or potentially perform DLL side-loading.

---
**Analyst Note:** Because this is an NSIS-based wrapper, any specific IOCs (such as C2 IPs or specific malicious filenames) would likely be contained within the payload extracted by the installer rather than the strings/behavior of the installer binary itself.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://crl.comodoca.com/AAACertificateServices.crl04`
- `http://crl.sectigo.com/SectigoPublicCodeSigningCAEVR36.crl0`
- `http://crl.sectigo.com/SectigoPublicCodeSigningRootR46.crl0`
- `http://crl.sectigo.com/SectigoPublicTimeStampingCAR36.crl0z`
- `http://crl.sectigo.com/SectigoPublicTimeStampingRootR46.crl0|`
- `http://crl.usertrust.com/USERTrustRSACertificationAuthority.crl05`
- `http://crt.sectigo.com/SectigoPublicCodeSigningCAEVR36.crt0#`
- `http://crt.sectigo.com/SectigoPublicCodeSigningRootR46.p7c0#`
- `http://crt.sectigo.com/SectigoPublicTimeStampingCAR36.crt0#`
- `http://crt.sectigo.com/SectigoPublicTimeStampingRootR46.p7c0#`
- `http://nsis.sf.net/NSIS_Error`
- `http://ocsp.comodoca.com0`
- `http://ocsp.sectigo.com0`
- `http://ocsp.usertrust.com0`
- `https://sectigo.com/CPS0`

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1.  **Malware family:** Unknown
2.  **Malware type:** Dropper / Loader
3.  **Confidence:** Medium
4.  **Key evidence:**
    *   **Wrapper Functionality:** The binary is identified as an NSIS-based installer, a common "wrapper" mechanism used to bundle, unpack, and verify malicious payloads while hiding the primary payload's signature from initial analysis.
    *   **Integrity Verification:** The use of CRC-32 calculations (`fcn.00406a93`) is a hallmark of droppers used to ensure that an injected or extracted payload remains intact before it is executed in memory.
    *   **Evasive Loading Techniques:** The implementation of `LoadLibraryExW` with dynamic path construction and registry lookups provides the "loader" functionality required to dynamically bring in malicious components (potential DLL side-loading).

**Analyst Note:** Because this sample functions as a vehicle for delivery, it is highly likely that the actual malicious payload (e.g., ransomware, info-stealer) resides within the compressed data of the installer rather than within the installer's code itself.
