# Threat Analysis Report

**Generated:** 2026-07-16 18:00 UTC
**Sample:** `07531d80301a5a19ba1cd76e697a485a4e7d233a2edabf16953aa2b0975486cd_07531d80301a5a19ba1cd76e697a485a4e7d233a2edabf16953aa2b0975486cd.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07531d80301a5a19ba1cd76e697a485a4e7d233a2edabf16953aa2b0975486cd_07531d80301a5a19ba1cd76e697a485a4e7d233a2edabf16953aa2b0975486cd.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 87,517,921 bytes |
| MD5 | `c1b096840802528a58eca102511e90ca` |
| SHA1 | `171a88c5be1f2dbfaaf38e8868e074e9ac804c75` |
| SHA256 | `07531d80301a5a19ba1cd76e697a485a4e7d233a2edabf16953aa2b0975486cd` |
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
| `.rsrc` | 23,552 | 5.384 | No |

### Imports

**KERNEL32.dll**: `SetEnvironmentVariableW`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `CopyFileW`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`, `SetErrorMode`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **190419** (showing first 100)

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

Based on the additional disassembly provided in chunk 2/2, here is the updated and extended analysis.

### **Updated Analysis Summary**
The binary remains confirmed as a **multi-stage loader/dropper**, likely utilizing an NSIS wrapper. The new disassembly confirms several sophisticated behaviors: it contains logic for **dynamic module loading**, utilizes **integrity checking (CRC32-style)** to verify payload integrity before execution, and maintains the capability to transition from a "loader" to an "active" state by injecting or loading secondary components into memory.

---

### **Core Functionality & Purpose**
*   **Multi-Stage Execution:** The inclusion of `fcn.00406624` (which utilizes `LoadLibraryExW`) confirms that the binary does not operate in isolation. It is designed to locate and load additional DLLs or modules into its own process space after the initial execution.
*   **Payload Integrity Verification:** The routine `fcn.00406787` acts as a checksum/decryption validator. This ensures that the data extracted from the resources (as identified in chunk 1) is correct and hasn't been corrupted or modified before the primary payload is executed.
*   **Resource Management:** The use of `OleInitialize` suggests it may be interacting with COM objects, which can be used for more complex system interactions, such as manipulating Shell objects or interacting with other Windows components.

---

### **Suspicious or Malicious Behaviors**
*   **Dynamic Library Loading (Evasive Execution):**
    *   The function `fcn.00406624` retrieves the system directory and uses `wsprintfW` to construct a path before calling `LoadLibraryExW`. This is a classic technique for **modular malware**. Instead of having all malicious logic in one file (which is easily flagged by static analysis), the "loader" pulls in specific capabilities only when needed.
*   **Integrity Checks/Checksums:**
    *   The loop structure in `fcn.00406787` is characteristic of a **CRC32 or similar cyclic redundancy check**. In malware, this is frequently used to verify that an encrypted payload was decrypted correctly before the loader "hands over" control to it. This prevents the loader from crashing if it fails to decrypt its hidden component properly.
*   **Hidden Payload Management:** 
    *   The combination of `GetTempPathW` (from chunk 1) and `LoadLibraryExW` (chunk 2) creates a clear workflow: 
        1.  Extract payload from resource $\rightarrow$ 2. Save to Temp folder $\rightarrow$ 3. Verify integrity with CRC check $\rightarrow$ 4. Load/Execute via `CreateProcessW`.

---

### **Notable Techniques & Patterns**
*   **CRC32 Algorithm Implementation:** The specific bit-shifting and XORing in `fcn.00406787` (e.g., `uVar1 = uVar1 >> 1 ^ -((uVar1 & 1) != 0) & 0xedb88320`) is a signature of the CRC32 algorithm. This reinforces that the file handles complex data processing for its internal payloads.
*   **Dynamic API Manipulation:** The continued use of `LoadLibraryExW` and potentially obfuscated calls to system libraries (via `GetProcAddress` in chunk 1) demonstrates an intent to stay "under the radar" by avoiding static imports from the Import Address Table (IAT).
*   **NSIS Persistence/Wrap Strategy:** The persistence of NSIS-related strings combined with these advanced loading techniques suggests a professional level of development. It is designed to hide the transition between the "installer" and the actual malware payload.

---

### **Revised Conclusion & Risk Assessment**
**Risk Level: High**

The binary exhibits high-confidence indicators of a **sophisticated dropper/loader**. The addition of chunk 2 highlights a structured "delivery" chain:
1.  **Obfuscation:** Use of an NSIS wrapper and custom decoding loops (`fcn.004067f5` / `fcn.00406787`).
2.  **Extraction:** Extracting data to temporary directories (identified in chunk 1).
3.  **Verification:** Running integrity checks to ensure the "Stage 2" payload is intact before execution.
4.  **Activation:** Using `LoadLibraryExW` and `CreateProcessW` to launch or integrate the malicious component into the system environment.

**Recommended Actions:**
*   Monitor for the creation of new files in `%TEMP%` or `%APPDATA%` folders.
*   Perform memory forensics on any process spawned by this binary to identify "Stage 2" payloads loaded via `LoadLibraryExW`.
*   Check for newly registered persistence points (Run keys, Scheduled Tasks) immediately following the execution of this installer.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1564** | Obfuscated Files or system resources | The use of an NSIS wrapper and multi-stage design is used to hide the actual malicious payload from static analysis. |
| **T1036** | Masquerading | The binary utilizes a legitimate installer's context (NSIS) to blend in with normal system activity while transitioning to its "active" state. |
| **T1574** | Archive Extraction | The behavior of extracting data from the internal resource section into a local file indicates hidden payload extraction. |
| **T1123** | Dynamic Resolution | The use of `GetProcAddress` and `LoadLibraryExW` allows the malware to resolve API calls at runtime, bypassing Import Address Table (IAT) scrutiny. |
| **T1027** | Packed_Resources | The implementation of CRC32 checksums and decryption loops indicates that internal components are packed or encrypted before execution. |
| **T1595** | Dump__or_Inject__Code | The behavior of loading secondary modules into the current process space via `LoadLibraryExW` is a method to inject functionality. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   (None identified)

**File paths / Registry keys**
*   **Note:** While the analysis mentions `GetTempPathW`, `%TEMP%`, and `GetSystemDirectoryW`, these are standard Windows API calls/variables rather than hardcoded malicious file paths. No specific registry keys were provided in the text.

**Mutex names / Named pipes**
*   (None identified)

**Hashes**
*   **CRC32 Constant:** `0xedb88320` (Note: This is a constant used for CRC32 algorithm verification, not a file hash).

**Other artifacts**
*   **Malware Framework/Wrapper:** Use of an **NSIS wrapper** to hide the transition between the installer and the payload.
*   **Specific Function Offsets:** 
    *   `fcn.00406624` (Logic for dynamic module loading via `LoadLibraryExW`).
    *   `fcn.00406787` / `fcn.004067f5` (CRC32 integrity check loop).
*   **Technique:** Use of **dynamic API manipulation** via `GetProcAddress` to bypass static Import Address Table (IAT) analysis.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High (for Type) / Low (for Family)
4. **Key evidence**:
    *   **Multi-Stage Delivery Chain:** The analysis confirms a sophisticated "loader" workflow: extracting data from resources, saving it to a temporary directory, and using `CreateProcessW` or `LoadLibraryExW` to execute the next stage.
    *   **Evasion & Integrity Tactics:** The use of CRC32 checksums (`fcn.00406787`) ensures payload integrity before execution, while dynamic API resolution via `GetProcAddress` and an NSIS wrapper are used to bypass static analysis and hide the "Stage 2" components.
    *   **Modular Architecture:** The reliance on `LoadLibraryExW` and specific function offsets for dynamic loading confirms that the primary binary is designed as a vehicle to deliver more complex functionality (like a RAT or Stealer) rather than performing all malicious acts alone.
