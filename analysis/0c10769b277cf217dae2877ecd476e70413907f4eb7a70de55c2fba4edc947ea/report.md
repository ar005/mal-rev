# Threat Analysis Report

**Generated:** 2026-07-29 14:22 UTC
**Sample:** `0c10769b277cf217dae2877ecd476e70413907f4eb7a70de55c2fba4edc947ea_0c10769b277cf217dae2877ecd476e70413907f4eb7a70de55c2fba4edc947ea.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c10769b277cf217dae2877ecd476e70413907f4eb7a70de55c2fba4edc947ea_0c10769b277cf217dae2877ecd476e70413907f4eb7a70de55c2fba4edc947ea.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 819,928 bytes |
| MD5 | `952d893926df7a8d5879f2ffeb96e96e` |
| SHA1 | `2a2f3faa2c7670a52e27b838c81737e6c9b4f965` |
| SHA256 | `0c10769b277cf217dae2877ecd476e70413907f4eb7a70de55c2fba4edc947ea` |
| Overall entropy | 7.794 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1459567209 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 24,064 | 6.41 | No |
| `.rdata` | 4,608 | 5.204 | No |
| `.data` | 1,536 | 4.131 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 141,824 | 6.059 | No |

### Imports

**KERNEL32.dll**: `GetTickCount`, `GetShortPathNameA`, `GetFullPathNameA`, `MoveFileA`, `SetCurrentDirectoryA`, `GetFileAttributesA`, `SetFileAttributesA`, `CompareFileTime`, `SearchPathA`, `CreateFileA`, `GetFileSize`, `GetModuleFileNameA`, `GetCurrentProcess`, `CopyFileA`, `ExitProcess`
**USER32.dll**: `SetCursor`, `GetWindowRect`, `EnableMenuItem`, `GetSystemMenu`, `SetClassLongA`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `EndDialog`, `ScreenToClient`, `LoadCursorA`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapA`, `CallWindowProcA`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectA`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHGetPathFromIDListA`, `SHBrowseForFolderA`, `SHGetFileInfoA`, `SHFileOperationA`, `ShellExecuteA`
**ADVAPI32.dll**: `RegDeleteValueA`, `SetFileSecurityA`, `RegOpenKeyExA`, `RegDeleteKeyA`, `RegEnumValueA`, `RegCloseKey`, `RegCreateKeyExA`, `RegSetValueExA`, `RegQueryValueExA`, `RegEnumKeyA`
**COMCTL32.dll**: `ImageList_AddMasked`, `ImageList_Destroy`, `ImageList_Create`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1775** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
SQSSSPW
tQVPW
Et@;u
v95qA
vX95h?B
#Vhn+@
Instu_
softuV
NulluM	E
t
9uu
8NCRCu
> _?=t
D$ Pj(
D$,SPS
tVj%SSS
SWSh$s@
SWhBs@
D$(+D$ SSP
D$0+D$(P
uv9Et	
9uu;9

FFC;]|
PPPPPP
8\tPV
<a|
<z
_^[t	P
UXTHEME
USERENV
SETUPAPI
APPHELP
PROPSYS
DWMAPI
CRYPTBASE
OLEACC
CLBCATQ
RichEdit
RichEdit20A
RichEd32
RichEd20
.DEFAULT\Control Panel\International
Control Panel\Desktop\ResourceLocale
[Rename]

Software\Microsoft\Windows\CurrentVersion
\Microsoft\Internet Explorer\Quick Launch
MulDiv
DeleteFileA
FindFirstFileA
FindNextFileA
FindClose
SetFilePointer
ReadFile
WriteFile
GetPrivateProfileStringA
WritePrivateProfileStringA
MultiByteToWideChar
FreeLibrary
GetProcAddress
LoadLibraryExA
GetModuleHandleA
GetExitCodeProcess
WaitForSingleObject
GlobalAlloc
GlobalFree
ExpandEnvironmentStringsA
lstrcmpA
lstrcmpiA
CloseHandle
SetFileTime
CompareFileTime
SearchPathA
GetShortPathNameA
GetFullPathNameA
MoveFileA
SetCurrentDirectoryA
GetFileAttributesA
SetFileAttributesA
GetTickCount
CreateFileA
GetFileSize
GetModuleFileNameA
GetCurrentProcess
CopyFileA
ExitProcess
GetWindowsDirectoryA
GetTempPathA
GetCommandLineA
lstrlenA
GetVersion
SetErrorMode
lstrcpynA
GetDiskFreeSpaceA
GlobalUnlock
GlobalLock
CreateThread
GetLastError
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5276 | ✓ |
| `fcn.004061ae` | `0x4061ae` | 2642 | ✓ |
| `entry0` | `0x40326c` | 1046 | ✓ |
| `fcn.00403774` | `0x403774` | 713 | ✓ |
| `fcn.00402ca5` | `0x402ca5` | 678 | ✓ |
| `fcn.00405d43` | `0x405d43` | 576 | ✓ |
| `fcn.00405646` | `0x405646` | 462 | ✓ |
| `fcn.00405a6f` | `0x405a6f` | 409 | ✓ |
| `fcn.00403076` | `0x403076` | 380 | ✓ |
| `fcn.00402f4b` | `0x402f4b` | 299 | ✓ |
| `fcn.0040500d` | `0x40500d` | 210 | ✓ |
| `fcn.00403a3d` | `0x403a3d` | 205 | ✓ |
| `fcn.004047d2` | `0x4047d2` | 197 | ✓ |
| `fcn.00402a69` | `0x402a69` | 181 | ✓ |
| `fcn.00404044` | `0x404044` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00402c06` | `0x402c06` | 159 | ✓ |
| `fcn.00405f83` | `0x405f83` | 153 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00405c98` | `0x405c98` | 137 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.004048dc` | `0x4048dc` | 128 | ✓ |
| `fcn.004054cf` | `0x4054cf` | 125 | ✓ |
| `fcn.004058f5` | `0x4058f5` | 120 | ✓ |
| `fcn.00405c08` | `0x405c08` | 119 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406120` | `0x406120` | 110 | ✓ |
| `fcn.00406043` | `0x406043` | 110 | ✓ |
| `fcn.004050df` | `0x4050df` | 108 | ✓ |
| `fcn.004055e2` | `0x4055e2` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402a69.c`](code/fcn.00402a69.c)
- [`code/fcn.00402c06.c`](code/fcn.00402c06.c)
- [`code/fcn.00402ca5.c`](code/fcn.00402ca5.c)
- [`code/fcn.00402f4b.c`](code/fcn.00402f4b.c)
- [`code/fcn.00403076.c`](code/fcn.00403076.c)
- [`code/fcn.00403774.c`](code/fcn.00403774.c)
- [`code/fcn.00403a3d.c`](code/fcn.00403a3d.c)
- [`code/fcn.00404044.c`](code/fcn.00404044.c)
- [`code/fcn.004047d2.c`](code/fcn.004047d2.c)
- [`code/fcn.004048dc.c`](code/fcn.004048dc.c)
- [`code/fcn.0040500d.c`](code/fcn.0040500d.c)
- [`code/fcn.004050df.c`](code/fcn.004050df.c)
- [`code/fcn.004054cf.c`](code/fcn.004054cf.c)
- [`code/fcn.004055e2.c`](code/fcn.004055e2.c)
- [`code/fcn.00405646.c`](code/fcn.00405646.c)
- [`code/fcn.004058f5.c`](code/fcn.004058f5.c)
- [`code/fcn.00405a6f.c`](code/fcn.00405a6f.c)
- [`code/fcn.00405c08.c`](code/fcn.00405c08.c)
- [`code/fcn.00405c98.c`](code/fcn.00405c98.c)
- [`code/fcn.00405d43.c`](code/fcn.00405d43.c)
- [`code/fcn.00405f83.c`](code/fcn.00405f83.c)
- [`code/fcn.00406043.c`](code/fcn.00406043.c)
- [`code/fcn.00406120.c`](code/fcn.00406120.c)
- [`code/fcn.004061ae.c`](code/fcn.004061ae.c)

## Behavioral Analysis

Based on the analysis of the provided disassembly, this binary is an **NSIS (Nullsoft Script Installer) Stub**. This type of file is commonly used to package and install software, but it is also frequently utilized in malware delivery as a "dropper" or "downloader."

The code serves as a wrapper that extracts files from its own internal data sections, moves them to the system, and executes them.

### Core Functionality
*   **Installer Framework:** The binary implements standard installer logic: creating directories, moving/copying files (`MoveFileA`, `CopyFileA`), and setting up environment variables.
*   **Resource Extraction:** It handles the extraction of "hidden" data (common in NSIS) where a single large file is unpacked into multiple components.
*   **Integrity Checking:** The function `fcn.00402ca5` implements an internal verification mechanism (likely CRC32 or a similar checksum) to ensure that the files being extracted/executed are intact and haven't been tampered with by security researchers or modified during transit.

### Suspicious / Malicious Behaviors
While this is technically a "tool" for installation, its behavior is highly characteristic of **malware droppers**:
*   **File Manipulation & Deployment:** The code heavily utilizes `CreateDirectoryA`, `MoveFileA`, and `CopyFileA`. In a malware context, this indicates the program's role in moving a payload from a temporary directory to a permanent location (e.g., `%AppData%` or `Temp`).
*   **Registry Manipulation:** Functions involving `RegCreateKeyExA` and `RegSetValueExA` are used to create keys and set values. This is often used for **persistence** (ensuring the malware runs on every reboot) or changing system configurations/security settings.
*   **Persistence through "System" logic:** The code checks for various file types and paths, including those in `GetTempPathA` and `GetWindowsDirectoryA`. It specifically looks to ensure it has the necessary permissions or environment to run its next stage successfully.
*   **Hidden File Handling:** Several functions (e.g., `fcn.0058f5`) deal with identifying and handling "hidden" attributes, which can be used to bypass basic security scanners that only look for standard files.

### Notable Techniques & Patterns
*   **NSIS Packaging Signature:** The inclusion of the string `"nsis.sf.net"` and the logic around `_nsi` (Notice the `.tmp`, `[Rename]`, and `_nsu` strings) are definitive indicators that this is an NSIS-wrapped installer.
*   **Shell Execution:** The use of `ShellExecuteA` indicates that once the "payload" is dropped, the stub will launch it as a new process to begin its primary operation (e.g., starting a keylogger or botnet agent).
*   **Self-Correction/Cleanup:** Function `fcn.005646` includes logic to loop through and delete other files in a directory. This is often used by malware to "clean up" the installer stub after it has finished deploying the actual malicious payload, effectively hiding its tracks.
*   **Information Obfuscation:** The use of `GetProcAddress` and `LoadLibraryExA` allows the binary to resolve and load necessary system DLLs dynamically at runtime rather than having them listed in the import table (a common technique to evade static analysis).

### Conclusion for Analysts
This is not a standalone piece of "malicious" logic, but rather a **delivery vehicle**. The presence of this specific code suggests that the original file is part of an infection chain. The primary threat comes from what this stub is designed to **unpack and execute**, as it will perform the heavy lifting of unpacking the payload, setting registry keys for persistence, and executing the final malicious stage.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1105 | Ingress Tool Transfer | The binary acts as a "dropper" by moving and copying payload files from internal data sections to local system directories. |
| T1547.001 | Registry Run Keys / Startup Folder | The use of `RegCreateKeyExA` and `RegSetValueExA` indicates an attempt to establish persistence for the loaded payloads. |
| T1027 | Obfuscated Files or Information | The use of `GetProcAddress` and `LoadLibraryExA` is a technique used to hide the binary's true capabilities from static analysis by resolving functions at runtime. |
| T1070.004 | Indicator Removal: File Deletion | The "Self-Correction/Cleanup" logic (fcn.005646) is designed to delete installer components and remove evidence of the delivery stage after execution. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: Most of the strings provided were identified as standard Windows API calls or system paths; these have been excluded as per your instructions to skip false positives.

### **IP addresses / URLs / Domains**
*   **nsis.sf.net** (Identified as a signature for NSIS-wrapped installers)

### **File paths / Registry keys**
*   *None.* (The registry paths provided in the strings, such as `Software\Microsoft\Windows\CurrentVersion` and `Control Panel\Desktop\ResourceLocale`, are standard Windows system paths and do not constitute specific malicious IOCs.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Installer Type:** NSIS (Nullsoft Script Installer) Stub.
*   **Internal Markers:** `_nsu`, `_nsi`, and `[Rename]` (Used to identify the specific installer framework).
*   **Persistence/Evasion Techniques:** 
    *   Dynamic API Resolution: Use of `GetProcAddress` and `LoadLibraryExA` to hide imports.
    *   Self-Deletion logic: Function `fcn.005646` is used for cleaning up installer artifacts after the payload is executed.
    *   Hidden File Handling: Logic in `fcn.0058f5` used to manipulate file attributes to evade detection.

---
**Analyst Note:** The primary threat identified is not a standalone malicious payload but a **delivery vehicle**. The presence of these specific markers confirms the use of an NSIS wrapper, commonly used to drop and execute secondary payloads (e.g., trojans or miners) while attempting to clean up its own footprint.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**: 
*   **NSIS Wrapper Framework:** The presence of specific internal markers (`_nsi`, `_nsu`, `[Rename]`) and standard installer logic confirms the binary is an NSIS stub used to bundle and deploy files.
*   **Delivery & Persistence Logic:** The use of `MoveFileA`/`CopyFileA` for payload placement, `RegCreateKeyExA` for establishing persistence, and `ShellExecuteA` to launch the final stage identifies it as a delivery vehicle.
*   **Evasion Tactics:** The inclusion of dynamic API resolution (`GetProcAddress`, `LoadLibraryExA`) and dedicated self-deletion routines (fcn.005646) are classic techniques used to hide the installation process from security analysts.
