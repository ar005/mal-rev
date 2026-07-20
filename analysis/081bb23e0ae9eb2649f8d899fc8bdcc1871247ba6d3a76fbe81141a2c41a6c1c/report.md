# Threat Analysis Report

**Generated:** 2026-07-18 01:47 UTC
**Sample:** `081bb23e0ae9eb2649f8d899fc8bdcc1871247ba6d3a76fbe81141a2c41a6c1c_081bb23e0ae9eb2649f8d899fc8bdcc1871247ba6d3a76fbe81141a2c41a6c1c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `081bb23e0ae9eb2649f8d899fc8bdcc1871247ba6d3a76fbe81141a2c41a6c1c_081bb23e0ae9eb2649f8d899fc8bdcc1871247ba6d3a76fbe81141a2c41a6c1c.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 898,792 bytes |
| MD5 | `ba5c487f991fd14e82d33e586e88a414` |
| SHA1 | `3e707b0f88958e7570a9c015025753e318c5d29f` |
| SHA256 | `081bb23e0ae9eb2649f8d899fc8bdcc1871247ba6d3a76fbe81141a2c41a6c1c` |
| Overall entropy | 7.953 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1481493055 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,112 | 6.439 | No |
| `.rdata` | 5,632 | 5.034 | No |
| `.data` | 1,536 | 4.033 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 32,768 | 4.785 | No |

### Imports

**KERNEL32.dll**: `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetFullPathNameW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `MoveFileW`, `SetFileAttributesW`, `GetCurrentProcess`, `ExitProcess`, `SetEnvironmentVariableW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `IsWindowEnabled`, `EnableMenuItem`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `ShellExecuteW`, `SHFileOperationW`
**ADVAPI32.dll**: `RegDeleteKeyW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `AdjustTokenPrivileges`, `RegOpenKeyExW`, `RegEnumValueW`, `RegDeleteValueW`, `RegCloseKey`, `RegCreateKeyExW`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_AddMasked`, `ord_17`, `ImageList_Destroy`, `ImageList_Create`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1935** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495OC
SQSSSPW
tQVPW
Y;=OC
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
u49-lOC
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
GetExitCodeProcess
WaitForSingleObject
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
lstrcpyW
MoveFileExW
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5817 | ✓ |
| `fcn.004065dd` | `0x4065dd` | 2639 | ✓ |
| `entry0` | `0x403334` | 1311 | ✓ |
| `fcn.004070d4` | `0x4070d4` | 827 | ✓ |
| `fcn.0040392d` | `0x40392d` | 726 | ✓ |
| `fcn.00406106` | `0x406106` | 626 | ✓ |
| `fcn.00402e82` | `0x402e82` | 569 | ✓ |
| `fcn.004030bb` | `0x4030bb` | 539 | ✓ |
| `fcn.004058d5` | `0x4058d5` | 451 | ✓ |
| `fcn.00405e13` | `0x405e13` | 370 | ✓ |
| `fcn.00405243` | `0x405243` | 211 | ✓ |
| `fcn.00403c03` | `0x403c03` | 205 | ✓ |
| `fcn.004049ff` | `0x4049ff` | 201 | ✓ |
| `fcn.00402c93` | `0x402c93` | 181 | ✓ |
| `fcn.00406378` | `0x406378` | 175 | ✓ |
| `fcn.0040420f` | `0x40420f` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00406044` | `0x406044` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404b0d` | `0x404b0d` | 128 | ✓ |
| `fcn.00405ba0` | `0x405ba0` | 126 | ✓ |
| `fcn.00405712` | `0x405712` | 125 | ✓ |
| `fcn.00405fb1` | `0x405fb1` | 122 | ✓ |
| `fcn.00405d9a` | `0x405d9a` | 121 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.0040644e` | `0x40644e` | 112 | ✓ |
| `fcn.0040656f` | `0x40656f` | 110 | ✓ |
| `fcn.00405316` | `0x405316` | 108 | ✓ |
| `fcn.0040706c` | `0x40706c` | 104 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402c93.c`](code/fcn.00402c93.c)
- [`code/fcn.00402e82.c`](code/fcn.00402e82.c)
- [`code/fcn.004030bb.c`](code/fcn.004030bb.c)
- [`code/fcn.0040392d.c`](code/fcn.0040392d.c)
- [`code/fcn.00403c03.c`](code/fcn.00403c03.c)
- [`code/fcn.0040420f.c`](code/fcn.0040420f.c)
- [`code/fcn.004049ff.c`](code/fcn.004049ff.c)
- [`code/fcn.00404b0d.c`](code/fcn.00404b0d.c)
- [`code/fcn.00405243.c`](code/fcn.00405243.c)
- [`code/fcn.00405316.c`](code/fcn.00405316.c)
- [`code/fcn.00405712.c`](code/fcn.00405712.c)
- [`code/fcn.004058d5.c`](code/fcn.004058d5.c)
- [`code/fcn.00405ba0.c`](code/fcn.00405ba0.c)
- [`code/fcn.00405d9a.c`](code/fcn.00405d9a.c)
- [`code/fcn.00405e13.c`](code/fcn.00405e13.c)
- [`code/fcn.00405fb1.c`](code/fcn.00405fb1.c)
- [`code/fcn.00406044.c`](code/fcn.00406044.c)
- [`code/fcn.00406106.c`](code/fcn.00406106.c)
- [`code/fcn.00406378.c`](code/fcn.00406378.c)
- [`code/fcn.0040644e.c`](code/fcn.0040644e.c)
- [`code/fcn.0040656f.c`](code/fcn.0040656f.c)
- [`code/fcn.004065dd.c`](code/fcn.004065dd.c)
- [`code/fcn.0040706c.c`](code/fcn.0040706c.c)
- [`code/fcn.004070d4.c`](code/fcn.004070d4.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated the technical analysis. The new code segments provide deeper insight into how the binary validates its components and manages its execution flow.

### Updated Technical Analysis

#### 1. Core Functionality & Infrastructure (Refined)
The presence of the following functions reinforces the conclusion that this is a high-level installer, but adds specifics on how it handles internal tasks:

*   **Execution Engine (Script Parsing):** The function `fcn.00405316` acts as a primary dispatcher. It iterates through a table of "actions" or "components." Each iteration performs a check and calls another routine (`fcn.00401389`). This is characteristic of an engine that reads a script (like an `.nsi` file) and executes predefined commands (e.g., *Install, Register, Copy*) in a loop.
*   **Integrity Verification:** The function `fcn.0040656f` implements a **CRC32-style checksum algorithm** (identifiable by the polynomial constant `0xedb88320`). This is used to verify that files being moved or extracted have not been corrupted or tampered with.
*   **Dynamic Component Loading:** The function `fcn.0040644e` utilizes `GetSystemDirectoryW`, `wsprintfW`, and `LoadLibraryExW`. This suggests the installer dynamically loads DLLs at runtime based on internal logic. While standard for installers needing specific system features, this is also a common tactic used by malware to load "payload" modules only when needed to evade static analysis.

#### 2. Suspicious or Malicious Behaviors (Additional Findings)
The new disassembly highlights several behaviors that overlap with sophisticated malware techniques:

*   **Data Integrity Checking as a Gatekeeper:** The CRC32-style logic (`fcn.0040656f`) can be used by malware to ensure that a "dropped" payload has been successfully unpacked and is not being modified by an automated sandbox or security tool before it is executed.
*   **Context-Aware Library Loading:** In `fcn.0040644e`, the calculation of the DLL name (using an index/offset) combined with `LoadLibraryExW` indicates that the binary doesn't hardcode every dependency. It "finds" its requirements dynamically, which can be used to hide the true functionality of the installer from basic static scanners.
*   **Robust State Management:** The complex arithmetic loop in `fcn.0040706c` suggests a sophisticated way of managing internal states or memory buffers. In an installer, this might manage progress bars; however, in a malicious context, such logic is often used to handle buffer offsets during the unpacking of encrypted data blocks.

#### 3. Technical Indicators & Patterns
*   **Algorithm Recognition:** The identification of the `0xedb88320` constant confirms that the binary includes specialized algorithms for data verification rather than just standard file I/O.
*   **Loop-Based Execution:** The transition from "Raw Instructions" to a "Scripted Loop" (seen in `fcn.00405316`) indicates a professional development framework. This is typical of the **NSIS** or **Inno Setup** engines, but also common in sophisticated malware "droppers" that need to perform many steps (e.g., create folder $\rightarrow$ copy file $\rightarrow$ set permissions $\rightarrow$ modify registry).

### Updated Summary Conclusion
The binary remains identified as a **sophisticated installer wrapper**, likely utilizing the NSIS framework. However, the addition of chunk 2/2 provides evidence of more advanced "under-the-hood" capabilities:

1.  **Validation:** It uses CRC32-style checks to ensure file integrity during the installation process.
2.  **Dynamic Execution:** It is designed to load components dynamically from the system or local environment, allowing it to remain modular.
3.  **Structured Automation:** It employs a robust internal loop to process a list of actions/commands.

**Final Risk Assessment:** The binary exhibits many "dual-use" characteristics. While these features are necessary for a complex software installer (ensuring files aren't corrupted and that the installer can handle various system configurations), they are also the primary building blocks for **droppers** and **downloaders**. The core risk lies in the *payloads* it is designed to move, verify, and launch.

**Recommended Next Steps:**
1.  **Payload Analysis:** Identify and extract any files that `fcn.0040656f` validates or `fcn.0040644e` loads into memory. 
2.  **Registry Monitoring:** Monitor the specific paths being modified during the loop in `fcn.00405316`.
3.  **Network Traffic:** Observe if the "Action" loop initiates any outbound connections to fetch additional components or validation keys.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1059 | Command and Scripting Interpreter | The use of a "script parsing" loop (`fcn.00405316`) to iterate through actions like Install, Register, and Copy indicates the binary functions as a command-driven execution engine. |
| T1106 | Native API | The utilization of `LoadLibraryExW` and `GetSystemDirectoryW` for dynamic component loading allows the binary to resolve dependencies at runtime and potentially hide its full functionality from static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** In accordance with your instructions, standard Windows API calls (e.g., `CreateFileW`, `LoadLibraryExW`) and common system libraries (`KERNEL32.dll`, `USER32.dll`) have been excluded as they do not constitute unique malicious indicators.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (While the analysis mentions registry modification and system directory interaction, no specific hardcoded malicious paths or keys were present in the provided strings).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **CRC32 Integrity Check:** The constant `0xedb88320` was identified as part of a CRC32-style checksum algorithm (used for verifying file integrity/payload unpacking).
*   **Execution Pattern (Script Loop):** The binary utilizes a "dispatch" logic (found at `fcn.00405316`) characteristic of an automated installer or dropper (likely NSIS or Inno Setup).
*   **Dynamic Loading Logic:** Detection of dynamic DLL loading via offset-based calculation (at `fcn.0040644e`) used to resolve and load components at runtime.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: Medium

4. **Key evidence**:
*   **Scripted Execution Framework:** The identification of a "dispatch" loop (`fcn.00405316`) used to iterate through actions like Install, Register, and Copy is characteristic of droppers designed to systematically deploy payloads.
*   **Integrity Verification & Payload Management:** The use of a CRC32-style checksum algorithm (`0xedb88320`) indicates the binary's primary role is to ensure that dropped components are intact before execution. 
*   **Evasive Loading Techniques:** The reliance on `LoadLibraryExW` combined with offset calculations for dynamic DLL loading suggests a modular design intended to hide its full functionality and final payload from static analysis.
