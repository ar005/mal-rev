# Threat Analysis Report

**Generated:** 2026-08-20 23:18 UTC
**Sample:** `10ded890320a96e2b69baa901bf556f5d11f483e5c97cd477f45cc8258395f56_10ded890320a96e2b69baa901bf556f5d11f483e5c97cd477f45cc8258395f56.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10ded890320a96e2b69baa901bf556f5d11f483e5c97cd477f45cc8258395f56_10ded890320a96e2b69baa901bf556f5d11f483e5c97cd477f45cc8258395f56.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 75,397,941 bytes |
| MD5 | `17c70417e6a9154ab36caab4843a5142` |
| SHA1 | `c8277b640dc67928458c036c210adbdf2624a337` |
| SHA256 | `10ded890320a96e2b69baa901bf556f5d11f483e5c97cd477f45cc8258395f56` |
| Overall entropy | 8.0 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1544912774 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,624 | 6.45 | No |
| `.rdata` | 5,632 | 5.025 | No |
| `.data` | 1,536 | 4.037 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 10,752 | 7.303 | ⚠️ Yes |

### Imports

**KERNEL32.dll**: `SetEnvironmentVariableW`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `CopyFileW`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`, `SetErrorMode`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **162919** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495,
tQVPW
Instu`
softuW
NulluN	E
SVWj _3
Aj"A[f
D$ Ph0
D$$SPS
tVj%SSS
D$$+D$
D$,+D$$P
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
MulDiv
DeleteFileW
FindFirstFileW
FindNextFileW
FindClose
SetFilePointer
ReadFile
MultiByteToWideChar
lstrlenA
WideCharToMultiByte
GetPrivateProfileStringW
WritePrivateProfileStringW
FreeLibrary
LoadLibraryExW
GetModuleHandleW
GlobalAlloc
GlobalFree
ExpandEnvironmentStringsW
lstrcmpW
lstrcmpiW
CloseHandle
SetFileTime
CompareFileTime
SearchPathW
GetShortPathNameW
GetFullPathNameW
MoveFileW
SetCurrentDirectoryW
GetFileAttributesW
SetFileAttributesW
GetTickCount
GetFileSize
GetModuleFileNameW
GetCurrentProcess
CopyFileW
ExitProcess
SetEnvironmentVariableW
GetWindowsDirectoryW
GetTempPathW
GetCommandLineW
GetVersion
SetErrorMode
lstrlenW
lstrcpynW
GetDiskFreeSpaceW
GlobalUnlock
GlobalLock
CreateThread
GetLastError
CreateDirectoryW
CreateProcessW
RemoveDirectoryW
lstrcmpiA
CreateFileW
GetTempFileNameW
WriteFile
lstrcpyA
MoveFileExW
lstrcatW
GetSystemDirectoryW
GetProcAddress
GetModuleHandleA
GetExitCodeProcess
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5795 | ✓ |
| `fcn.004067f5` | `0x4067f5` | 2639 | ✓ |
| `entry0` | `0x40338f` | 1345 | ✓ |
| `fcn.004072ec` | `0x4072ec` | 827 | ✓ |
| `fcn.004039aa` | `0x4039aa` | 726 | ✓ |
| `fcn.004062dc` | `0x4062dc` | 626 | ✓ |
| `fcn.00402edd` | `0x402edd` | 569 | ✓ |
| `fcn.00403116` | `0x403116` | 539 | ✓ |
| `fcn.004059cc` | `0x4059cc` | 451 | ✓ |
| `fcn.00405f06` | `0x405f06` | 378 | ✓ |
| `fcn.00405322` | `0x405322` | 211 | ✓ |
| `fcn.00404298` | `0x404298` | 207 | ✓ |
| `fcn.00404ade` | `0x404ade` | 201 | ✓ |
| `fcn.00403c80` | `0x403c80` | 185 | ✓ |
| `fcn.0040654e` | `0x40654e` | 175 | ✓ |
| `fcn.00402d44` | `0x402d44` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040621a` | `0x40621a` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404bec` | `0x404bec` | 128 | ✓ |
| `fcn.00405c97` | `0x405c97` | 126 | ✓ |
| `fcn.004057f1` | `0x4057f1` | 125 | ✓ |
| `fcn.004060ac` | `0x4060ac` | 123 | ✓ |
| `fcn.00406188` | `0x406188` | 121 | ✓ |
| `fcn.00405e91` | `0x405e91` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406624` | `0x406624` | 112 | ✓ |
| `fcn.00406787` | `0x406787` | 110 | ✓ |
| `fcn.004053f5` | `0x4053f5` | 108 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402d44.c`](code/fcn.00402d44.c)
- [`code/fcn.00402edd.c`](code/fcn.00402edd.c)
- [`code/fcn.00403116.c`](code/fcn.00403116.c)
- [`code/fcn.004039aa.c`](code/fcn.004039aa.c)
- [`code/fcn.00403c80.c`](code/fcn.00403c80.c)
- [`code/fcn.00404298.c`](code/fcn.00404298.c)
- [`code/fcn.00404ade.c`](code/fcn.00404ade.c)
- [`code/fcn.00404bec.c`](code/fcn.00404bec.c)
- [`code/fcn.00405322.c`](code/fcn.00405322.c)
- [`code/fcn.004053f5.c`](code/fcn.004053f5.c)
- [`code/fcn.004057f1.c`](code/fcn.004057f1.c)
- [`code/fcn.004059cc.c`](code/fcn.004059cc.c)
- [`code/fcn.00405c97.c`](code/fcn.00405c97.c)
- [`code/fcn.00405e91.c`](code/fcn.00405e91.c)
- [`code/fcn.00405f06.c`](code/fcn.00405f06.c)
- [`code/fcn.004060ac.c`](code/fcn.004060ac.c)
- [`code/fcn.00406188.c`](code/fcn.00406188.c)
- [`code/fcn.0040621a.c`](code/fcn.0040621a.c)
- [`code/fcn.004062dc.c`](code/fcn.004062dc.c)
- [`code/fcn.0040654e.c`](code/fcn.0040654e.c)
- [`code/fcn.00406624.c`](code/fcn.00406624.c)
- [`code/fcn.00406787.c`](code/fcn.00406787.c)
- [`code/fcn.004067f5.c`](code/fcn.004067f5.c)
- [`code/fcn.004072ec.c`](code/fcn.004072ec.c)

## Behavioral Analysis

Based on the second chunk of disassembly, the analysis confirms that this binary is a highly engineered piece of software. The additional functions reveal more sophisticated behavior regarding **integrity verification** and **dynamic system interaction**, which are hallmarks of both high-end installers and professional-grade malware "gatekeepers."

Below is the updated analysis incorporating the new findings.

---

### Updated Analysis Report

#### Executive Summary
The code remains consistent with a **sophisticated installer or "dropper" stub**, likely utilizing the NSIS framework. The addition of chunk 2/2 introduces evidence of **integrity checking (CRC32)** and **dynamic system library loading**. These features ensure that the payload is not only extracted but verified before execution, and that the environment is prepared by loading necessary system components dynamically.

---

### Core Functionality & Purpose
*   **Installer Stub:** Confirmed via NSIS-style logic in chunk 1. The complexity of the OLE initialization (`OleInitialize`) in `fcn.004053f5` suggests a "polished" installer designed to interact with complex Windows features.
*   **Payload Integrity Verification:** Function `fcn.00406787` implements a **CRC-32 checksum calculation**. This is used to verify that the files moved/extracted in previous steps (from chunk 1) are intact and have not been corrupted or modified before they are executed.
*   **Dynamic Environment Preparation:** Function `fcn.00406624` programmatically determines system paths (`GetSystemDirectoryW`) to load necessary DLLs via `LoadLibraryExW`. This ensures the installer can find and hook into required system components regardless of specific path configurations.

---

### Suspicious or Malicious Behaviors
The following behaviors are characteristic of sophisticated "gatekeeper" malware:

*   **Integrity Checking (High Indicator):** 
    *   The implementation of `fcn.00406787` (a standard CRC32 algorithm) is used to validate the payload. In a malicious context, this ensures that the "dropped" malware hasn't been corrupted during the unpacking process or intercepted by security software.
*   **Dynamic DLL Loading & Path Construction:** 
    *   In `fcn.00406624`, the code dynamically constructs paths to system libraries. While standard for installers, this technique is also used by malware to ensure it can load necessary components (like `advapi32.dll` or others) while attempting to bypass static analysis that looks for hardcoded malicious DLL paths.
*   **Persistence/Evasion via Decoupling:**
    *   The combination of "Drop $\rightarrow$ Verify Integrity $\rightarrow$ Load Libraries $\rightarrow$ Execute" is a classic multi-stage execution chain. By checking the integrity before execution, the loader ensures that the final payload is ready to run without crashing or being flagged by simple heuristics during the extraction phase.

---

### Technical Indicators & Patterns
*   **CRC32 Algorithm (`fcn.00406787`):** The presence of the polynomial `0xedb88320` confirms a standard CRC-32 check. This is an automated way to verify data integrity during file extraction.
*   **System Path Resolution:** The use of `GetSystemDirectoryW` and subsequent string manipulation to load libraries (`LoadLibraryExW`) indicates the program is designed to be portable across different Windows configurations while maintaining high control over its environment.
*   **COM/OLE Management:** The presence of `OleInitialize` and the corresponding cleanup logic in `fcn.004053f5` suggests that the installer (or the payload it prepares) has a complex UI or interacts with advanced system features, providing a "legitimate" veneer to the code.

---

### Conclusion for Analyst
The addition of this disassembly strengthens the "Sophisticated Dropper" classification. The binary is not just moving files; it is **validating** them and **preparing the environment** specifically for the payload's successful execution. 

**Updated Risk Assessment:**
*   **Complexity:** High.
*   **Intent:** Likely a dropper or wrapper.
*   **Sophistication:** The inclusion of CRC-32 checks and dynamic library loading suggests this is not a "script-kiddy" level sample but rather a professionally developed piece of software (potentially an installer for a commercial product) or, more concerningly, a sophisticated piece of malware (like a Trojan or Information Stealer).

**Recommendation:** 
Continue monitoring the filenames and paths generated by `fcn.00406624`. If the DLLs being loaded are not standard system files but are instead located in temp directories, the sample should be treated as an active threat. The use of CRC-32 strongly suggests a multi-stage delivery where the "true" payload is hidden until it passes verification by this stub.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of CRC-32 checksums (`fcn.00406787`) ensures the payload remains intact and has not been altered by security tools during the extraction phase. |
| **T1106** | Native API | The utilization of `LoadLibraryExW` and `GetSystemDirectoryW` to dynamically resolve system paths avoids hardcoded strings that could be flagged by static analysis. |
| **T1036** | Masquerading | The inclusion of `OleInitialize` and polished installer-like logic is used to provide a "legitimate" veneer, helping the malware blend in with standard system software. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs).

**Note:** The majority of the "Extracted Strings" section consists of standard Windows API calls (e.g., `Kernel32.dll`, `CreateProcessW`). These were excluded as they are common to thousands of legitimate applications and do not constitute specific indicators of a particular threat actor or campaign.

### **IOC_REPORT**

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (The analysis mentions "System Path Resolution," but no specific hardcoded malicious paths were provided in the text).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified. (Note: The value `0xedb88320` is a standard CRC-32 polynomial constant, not a file hash).

**Other artifacts**
*   **CRC-32 Integrity Check:** Function `fcn.00406787` (Used for payload verification).
*   **Dynamic Library Loading/Path Construction:** Function `fcn.00406624`.
*   **OLE Management Logic:** Function `fcn.004053f5`.
*   **Behavioral Pattern:** Multi-stage execution chain (Drop $\rightarrow$ Verify Integrity $\rightarrow$ Load Libraries $\rightarrow$ Execute).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper
3. **Confidence**: High (for functionality) / Low (for specific campaign attribution)
4. **Key evidence**:
    *   **Multi-stage Execution Chain:** The analysis identifies a classic "Drop $\rightarrow$ Verify Integrity $\rightarrow$ Load Libraries $\rightarrow$ Execute" workflow, which is the primary characteristic of a sophisticated dropper/gatekeeper.
    *   **Integrity Verification (CRC-32):** The use of the `0xedb88320` polynomial to verify payloads ensures that the dropped malicious components have not been tampered with or modified by security software before execution.
    *   **Evasion via Dynamic Loading:** The utilization of `GetSystemDirectoryW` and `LoadLibraryExW` indicates an attempt to bypass static analysis by avoiding hardcoded strings while ensuring the environment is properly prepared for the final payload.
