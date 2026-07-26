# Threat Analysis Report

**Generated:** 2026-07-25 13:09 UTC
**Sample:** `0ab348e15caa97c08f7803915216cc410b4bd608058fcf01ba3fbb152da0d84d_0ab348e15caa97c08f7803915216cc410b4bd608058fcf01ba3fbb152da0d84d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ab348e15caa97c08f7803915216cc410b4bd608058fcf01ba3fbb152da0d84d_0ab348e15caa97c08f7803915216cc410b4bd608058fcf01ba3fbb152da0d84d.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 6 sections |
| Size | 101,298,170 bytes |
| MD5 | `6332c9e3c530e951159901ae63561a4b` |
| SHA1 | `68af89b953fb8692c15383ca1436d225253135b7` |
| SHA256 | `0ab348e15caa97c08f7803915216cc410b4bd608058fcf01ba3fbb152da0d84d` |
| Overall entropy | 8.0 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1408549256 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,112 | 6.448 | No |
| `.rdata` | 5,632 | 5.364 | No |
| `.data` | 512 | 1.405 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 217,088 | 7.06 | ⚠️ Yes |
| `.reloc` | 3,072 | 4.948 | No |

### Imports

**KERNEL32.dll**: `SearchPathA`, `GetShortPathNameA`, `GetFullPathNameA`, `MoveFileA`, `SetCurrentDirectoryA`, `GetFileAttributesA`, `GetLastError`, `CreateDirectoryA`, `SetFileAttributesA`, `Sleep`, `GetTickCount`, `CreateFileA`, `GetFileSize`, `GetModuleFileNameA`, `GetCurrentProcess`
**USER32.dll**: `ScreenToClient`, `GetMessagePos`, `CallWindowProcA`, `IsWindowVisible`, `LoadBitmapA`, `CloseClipboard`, `SetClipboardData`, `EmptyClipboard`, `OpenClipboard`, `TrackPopupMenu`, `GetWindowRect`, `AppendMenuA`, `CreatePopupMenu`, `GetSystemMetrics`, `EndDialog`
**GDI32.dll**: `SetBkColor`, `GetDeviceCaps`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectA`, `SetBkMode`, `SetTextColor`, `SelectObject`
**SHELL32.dll**: `SHBrowseForFolderA`, `SHGetPathFromIDListA`, `SHGetFileInfoA`, `ShellExecuteA`, `SHFileOperationA`, `SHGetSpecialFolderLocation`
**ADVAPI32.dll**: `RegEnumKeyA`, `RegOpenKeyExA`, `RegCloseKey`, `RegDeleteKeyA`, `RegDeleteValueA`, `RegCreateKeyExA`, `RegSetValueExA`, `RegQueryValueExA`, `RegEnumValueA`
**COMCTL32.dll**: `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`, `ImageList_Create`
**ole32.dll**: `CoTaskMemFree`, `OleInitialize`, `OleUninitialize`, `CoCreateInstance`
**VERSION.dll**: `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`, `VerQueryValueA`

## Extracted Strings

Total strings found: **218977** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
@.reloc
t9Mt
QSSSPW
tQVPW
#Vh%,@
t
9uu
D$<PSho
D$ Pj(
D$(Ph 
9uu;9
uy9Et	
D$ +D$
D$0+D$(P
PPPPPP
8\tPV
QSUVWh$
Ed+EL;E
u$9Mls
)Mh)Mlf
u$9Mls
)Mh)Mlf
u$9Mls
)Mh)Mlf
Ed+EL;E
]4;Mhr+Mh
E89E0}s
u$9Uls
-)Uh)Ul3
Ed+EL;E
)Mh)Mlf
u$9Mls
)Mh)Mlf
verifying installer: %d%%
unpacking data: %d%%
... %d%%
Installer integrity check has failed. Common causes include
incomplete download and damaged media. Contact the
installer's author to obtain a new copy.

More information at:
http://nsis.sf.net/NSIS_Error
Error writing temporary file. Make sure your temp folder is valid.
Error launching installer
SeShutdownPrivilege
~nsu.tmp
NSIS Error
%u.%u%s%s
RichEdit
RichEdit20A
RichEd32
RichEd20
.DEFAULT\Control Panel\International
Control Panel\Desktop\ResourceLocale
SHGetFolderPathA
SHFOLDER
SHAutoComplete
SHLWAPI
GetUserDefaultUILanguage
AdjustTokenPrivileges
LookupPrivilegeValueA
OpenProcessToken
RegDeleteKeyExA
ADVAPI32
MoveFileExA
GetDiskFreeSpaceExA
KERNEL32
[Rename]

Software\Microsoft\Windows\CurrentVersion
\Microsoft\Internet Explorer\Quick Launch
*?|<>/":
Module32Next
Module32First
Process32Next
Process32First
CreateToolhelp32Snapshot
Kernel32.DLL
Unknown
GetModuleBaseNameA
EnumProcessModules
EnumProcesses
PSAPI.DLL
%s=%s

Version 
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
LoadLibraryExA
GetModuleHandleA
GlobalFree
GetExitCodeProcess
WaitForSingleObject
GlobalAlloc
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401599` | `0x401599` | 5397 | ✓ |
| `fcn.0040699f` | `0x40699f` | 2533 | ✓ |
| `entry0` | `0x403391` | 974 | ✓ |
| `fcn.00405b3d` | `0x405b3d` | 875 | ✓ |
| `fcn.00406566` | `0x406566` | 805 | ✓ |
| `fcn.004052e6` | `0x4052e6` | 718 | ✓ |
| `fcn.00403030` | `0x403030` | 667 | ✓ |
| `fcn.00405f7e` | `0x405f7e` | 600 | ✓ |
| `fcn.0040639b` | `0x40639b` | 459 | ✓ |
| `fcn.004061d6` | `0x4061d6` | 402 | ✓ |
| `fcn.00402d89` | `0x402d89` | 382 | ✓ |
| `fcn.00402f07` | `0x402f07` | 297 | ✓ |
| `fcn.00404975` | `0x404975` | 210 | ✓ |
| `fcn.0040396b` | `0x40396b` | 207 | ✓ |
| `fcn.00403e2d` | `0x403e2d` | 190 | ✓ |
| `fcn.00401497` | `0x401497` | 182 | ✓ |
| `fcn.004011f8` | `0x4011f8` | 174 | ✓ |
| `fcn.004038c1` | `0x4038c1` | 170 | ✓ |
| `fcn.00402ca1` | `0x402ca1` | 159 | ✓ |
| `fcn.0040596d` | `0x40596d` | 155 | ✓ |
| `fcn.004012f1` | `0x4012f1` | 141 | ✓ |
| `fcn.004058b7` | `0x4058b7` | 135 | ✓ |
| `fcn.00405efc` | `0x405efc` | 130 | ✓ |
| `fcn.0040139a` | `0x40139a` | 128 | ✓ |
| `fcn.00404252` | `0x404252` | 126 | ✓ |
| `fcn.00405827` | `0x405827` | 119 | ✓ |
| `fcn.00401186` | `0x401186` | 114 | ✓ |
| `fcn.0040690e` | `0x40690e` | 113 | ✓ |
| `fcn.0040688b` | `0x40688b` | 108 | ✓ |
| `fcn.00404a47` | `0x404a47` | 108 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401186.c`](code/fcn.00401186.c)
- [`code/fcn.004011f8.c`](code/fcn.004011f8.c)
- [`code/fcn.004012f1.c`](code/fcn.004012f1.c)
- [`code/fcn.0040139a.c`](code/fcn.0040139a.c)
- [`code/fcn.00401497.c`](code/fcn.00401497.c)
- [`code/fcn.00401599.c`](code/fcn.00401599.c)
- [`code/fcn.00402ca1.c`](code/fcn.00402ca1.c)
- [`code/fcn.00402d89.c`](code/fcn.00402d89.c)
- [`code/fcn.00402f07.c`](code/fcn.00402f07.c)
- [`code/fcn.00403030.c`](code/fcn.00403030.c)
- [`code/fcn.004038c1.c`](code/fcn.004038c1.c)
- [`code/fcn.0040396b.c`](code/fcn.0040396b.c)
- [`code/fcn.00403e2d.c`](code/fcn.00403e2d.c)
- [`code/fcn.00404252.c`](code/fcn.00404252.c)
- [`code/fcn.00404975.c`](code/fcn.00404975.c)
- [`code/fcn.00404a47.c`](code/fcn.00404a47.c)
- [`code/fcn.004052e6.c`](code/fcn.004052e6.c)
- [`code/fcn.00405827.c`](code/fcn.00405827.c)
- [`code/fcn.004058b7.c`](code/fcn.004058b7.c)
- [`code/fcn.0040596d.c`](code/fcn.0040596d.c)
- [`code/fcn.00405b3d.c`](code/fcn.00405b3d.c)
- [`code/fcn.00405efc.c`](code/fcn.00405efc.c)
- [`code/fcn.00405f7e.c`](code/fcn.00405f7e.c)
- [`code/fcn.004061d6.c`](code/fcn.004061d6.c)
- [`code/fcn.0040639b.c`](code/fcn.0040639b.c)
- [`code/fcn.00406566.c`](code/fcn.00406566.c)
- [`code/fcn.0040688b.c`](code/fcn.0040688b.c)
- [`code/fcn.0040690e.c`](code/fcn.0040690e.c)
- [`code/fcn.0040699f.c`](code/fcn.0040699f.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated the analysis. The new code snippet reveals details regarding the finalization of an execution routine and interaction with Windows system libraries.

### Updated Malware Analysis Report

#### Core Functionality and Purpose
The binary remains identified as a **sophisticated installer or "loader" wrapper**, likely utilizing or mimicking the NSIS (Nullsoft Script Installer) framework. Its primary role is to manage the transition from an initial "dropper" state to an active payload by handling environment checks, file extraction, integrity verification, and system configuration.

#### Suspicious or Malicious Behaviors
The following behaviors are indicative of potential malicious intent or common characteristics found in "droppers":

*   **Anti-Analysis / Process Enumeration:** 
    *   Function `fcn.00405b3d` uses the `PSAPI` library to scan running processes against a known list (e.g., debuggers, security tools) before proceeding. This is a classic evasion technique to prevent analysis by security researchers.
*   **Persistence and Configuration via Registry:** 
    *   Multiple calls to `RegCreateKeyExA` and `RegSetValueExA` indicate the installer modifies system registry keys. In malware contexts, this is frequently used to ensure the infection survives a reboot (e.g., "Run" keys).
*   **Temporary File Manipulation & Dropping:** 
    *   The code manages temporary files (like `~nsu.tmp`) and uses custom string expansion (`fcn.00405f7e`) to move components into non-obvious locations, such as the Quick Launch folder or system directories.
*   **Integrity Verification (Packer/Crypter behavior):** 
    *   The CRC-style calculation loop in `fcn.0040699f` confirms that the payload is being checked for integrity after decompression/decryption, a hallmark of multi-stage malware.
*   **File System Cleanup:** 
    *   Routine `fcn.0040639b` utilizes wildcards (`*.*`) to find and delete files, likely intended to remove the "loader" components or evidence of intermediate execution steps after the primary payload is successfully launched.
*   **COM Component Interaction (New Evidence):** 
    *   The call to `OleUninitialize()` indicates that the binary interacts with **Object Linking and Embedding (OLE)** or COM objects. While common in complex installers for UI elements, it is also used by malware to interact with shell components or system services more deeply than standard API calls.

#### Notable Techniques or Patterns
*   **NSIS Framework Signature:** The `nsis.sf.net` strings confirm the use of an NSIS-based infrastructure, a common choice for both legitimate software and sophisticated malware due to its robust file manipulation capabilities.
*   **Execution State Management:** The incrementing of the value at `0x433c8c` suggests a "success/failure" tracking mechanism throughout the execution flow, ensuring that the final stage only occurs if all previous checks (decompress, integrity check, registry modification) pass successfully.
*   **Multi-Stage Logic Flow:** The analysis confirms a clear lifecycle: 
    1.  Environment Check $\rightarrow$ 2. Payload Extraction $\rightarrow$ 3. Integrity Verification $\rightarrow$ 4. Registry/System Modification $\rightarrow$ 5. Cleanup & Exit (where `OleUninitialize` is called).

---

### Updated Summary Table for Quick Reference

| Feature | Observation | Risk Level | Detail / Context |
| :--- | :--- | :--- | :--- |
| **Anti-Analysis** | Process Enumeration (`PSAPI`) | **High** | Checks for debuggers and security software. |
| **Persistence** | Registry Manipulation | **Medium** | Likely creates "Run" keys or modifies system behavior. |
| **Payload Dropping**| Temp Files & Path Expansion | **High** | Moves components to hidden/system folders. |
| **Integrity Check** | CRC/Checksum Loops | **Low** | Ensures the payload is intact post-decryption. |
| **File Cleanup** | Wildcard Search & Delete | **Medium** | Deletes artifacts of the installation process. |
| **COM Interaction**| `OleUninitialize` call | **Medium** | Indicates interaction with OLE/Shell objects. |

### Conclusion
The inclusion of `OleUninitialize` and the final cleanup loop confirms that this is not a simple script, but a **multi-stage installer designed to operate cleanly**. It performs its "dirty work" (unpacking, checking for security software, moving files) and then attempts to clean up its artifacts before completing the execution. The presence of anti-analysis checks combined with these installation features strongly suggests it is a **malicious loader** intended to deploy a second-stage payload while evading detection.

---

## MITRE ATT&CK Mapping

Based on your behavioral analysis, here is the mapping of the observed activities to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Detection | The use of `PSAPI` to identify and filter out debuggers or security tools is a primary method for evading analysis environments. |
| **T1136.001** | Registry Run Keys / Startup Folder | Modification of registry keys via `RegCreateKeyExA` and `RegSetValueExA` is used to ensure the malware automatically executes on system boot. |
| **T1036** | Masquerading | Deploying components into "non-obvious" locations and using custom string expansion helps the malware blend in with legitimate system files. |
| **T1027** | Encrypt/Pack | The CRC-style calculation loop identifies a multi-stage payload that has been unpacked or decrypted, typical of complex loader behaviors. |
| **T1070.004** | Indicator Removal on Host | The use of wildcards to delete temporary files and "loader" components is an attempt to remove traces of the infection chain. |
| **T1564** | Proxy Execution (or related COM interaction) | Interaction with OLE/COM objects via `OleUninitialize` suggests a more sophisticated method of interacting with system components or shell environments. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `nsis.sf.net` (Domain associated with NSIS infrastructure)

**File paths / Registry keys**
*   `~nsu.tmp` (Temporary file artifact used during installation/unpacking)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified in the provided text.*

**Other artifacts**
*   **Framework:** NSIS (Nullsoft Script Installer) - Identified via `nsis.sf.net` and standard NSIS error strings.
*   **Persistence/Evasion Tactics:** 
    *   Process Enumeration via `PSAPI` library (`EnumProcesses`, `GetModuleBaseNameA`) to detect debuggers or security tools.
    *   CRC-style integrity check loop (indicative of a packer or crypter).
*   **System Interaction:** 
    *   Use of `OleUninitialize` for COM component interaction.
    *   Wildcard file deletion (`*.*`) used as a cleanup mechanism to remove artifacts/loaders.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1.  **Malware family:** Unknown
2.  **Malware type:** Loader / Dropper
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Anti-Analysis & Evasion:** The use of `PSAPI` to enumerate processes and check for debuggers/security tools is a definitive indicator of malicious intent aimed at evading detection.
    *   **Multi-Stage Execution Logic:** The combination of CRC integrity checks, file extraction into non-obvious paths, and automatic "cleanup" routines indicates the sample's primary purpose is to deliver and hide a secondary payload.
    *   **Persistence & Obfuscation:** Use of registry modifications for persistence and the leveraging of the NSIS framework to mask its activity as a standard installer are common tactics used by sophisticated loaders.
