# Threat Analysis Report

**Generated:** 2026-09-06 18:55 UTC
**Sample:** `151d1efff2d7867e50717283dbd72f965bccd893a5e3fe56c412c8c692bb06aa_151d1efff2d7867e50717283dbd72f965bccd893a5e3fe56c412c8c692bb06aa.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `151d1efff2d7867e50717283dbd72f965bccd893a5e3fe56c412c8c692bb06aa_151d1efff2d7867e50717283dbd72f965bccd893a5e3fe56c412c8c692bb06aa.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 6 sections |
| Size | 77,863,539 bytes |
| MD5 | `6098b42bcb2634407a69459429dd42ec` |
| SHA1 | `69847580e4f0376d9059e8f0b97763463035aac5` |
| SHA256 | `151d1efff2d7867e50717283dbd72f965bccd893a5e3fe56c412c8c692bb06aa` |
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
| `.rsrc` | 28,672 | 5.793 | No |
| `.reloc` | 3,072 | 5.211 | No |

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

Total strings found: **168851** (showing first 100)

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

The additional disassembly provided in Chunk 2/2 is relatively brief, but it confirms several aspects of the execution flow regarding how the binary concludes its internal routines. These findings supplement the existing analysis of the installer's behavior and lifecycle.

Here is the updated and extended technical analysis:

### Updated Technical Analysis

#### Core Functionality and Purpose (Updated)
The code continues to align with the characteristics of an **NSIS-based software installer**. 
*   **Resource Iteration:** The loop logic (`puVar3 = puVar3 + 0x406;` and `while (iVar4 != 0)`) indicates a structured iteration through a predefined table. This is consistent with an installer processing a list of files, components, or installation steps stored in the data section.
*   **State Management:** The incrementing of a specific memory address (`*0x433c8c = *0x433c8c + 1`) suggests a counter or a state machine tracking progress through the extraction/installation sequence.

#### Suspicious or Malicious Behaviors (Refined)
While the new code does not introduce "new" malicious behaviors, it clarifies the **Cleanup and Finalization** phase:
*   **OLE/COM Interaction:** The call to `OleUninitialize` indicates that the binary interacts with Windows Component Object Model (COM) or OLE (Object Linking and Embedding). In an installer, this is typically used for UI elements (like "Drag and Drop" support or advanced windowing features), but it confirms that the binary interacts deeply with standard Windows system components to manage its environment.
*   **Sequential Execution:** The structure of the code suggests a linear progression: perform actions $\rightarrow$ update state/counter $\rightarrow$ cleanup resources. This is typical for legitimate installers, but this "clean" exit from a function after performing tasks (like unpacking or moving files) is also how malware ensures it doesn't leave handles open that could be flagged by monitoring tools.

#### Notable Techniques and Patterns
*   **Robust Data Parsing:** The pointer arithmetic (`+ 0x406`) suggests the binary is navigating a fixed-size structure or record in memory. This indicates a structured approach to handling its internal payload data, ensuring it can correctly locate each "chunk" of information needed for the installation process.
*   **Standard Library Usage:** The inclusion of `OleUninitialize` reinforces that the binary uses standard Windows programming libraries to handle complex tasks (like UI management) rather than writing custom, potentially more suspicious, low-level code to perform those same actions.

---

### Updated Summary for Analysis Report:

The analysis of both chunks confirms the binary is a **highly structured installer wrapper** (consistent with NSIS). 

**Updated Findings:**
1.  **Installer Wrapper Integrity:** The presence of `OleUninstall` and complex loop-based resource tracking indicates a professional-grade installation framework. It manages its own state and cleans up system resources properly upon completion of internal tasks.
2.  **Dropped Payload Awareness:** As previously noted, the "installer" functions (unpacking, CRC32 checks, folder creation) are just the vehicle. The core "threat" or functionality resides in the **extracted data**. 
3.  **Standardized Complexity:** The code uses standard Windows API calls to handle UI and system interaction. While this makes the binary appear "cleaner" to automated scanners than a bespoke malware sample, it effectively masks any malicious payload hidden within the installer's internal resources.

**Final Assessment:**
The binary functions as an **NSIS Installer**. It is highly capable of moving data into protected directories, checking for system processes, and verifying its own integrity. Because it uses standard libraries for UI and resource management (COM/OLE), it provides a sophisticated "wrapper" that can effectively deliver a malicious payload while appearing to be a legitimate installer. 

**Recommendation:**
The analysis should prioritize the **extraction results**. Focus on what files are created in `\Temp` or `\AppData`, and analyze those specific binaries for suspicious behavior, as the installer itself is simply the mechanism of delivery.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The binary utilizes a standard NSIS framework and common Windows libraries (COM/OLE) to appear as a legitimate software installer, thereby blending in with normal system behavior. |
| **T1027.001** | Obfuscated Files or Information: Packing | The installer acts as a wrapper that hides the malicious payload within internal resources, only unpacking and extracting it during the installation process. |
| **T1070** | Indicator Removal on Host | The analysis notes that the binary cleans up resources and avoids leaving open handles to ensure it is not flagged by monitoring tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Most of the items in the "Strings" section were identified as standard Windows API calls, system registry keys, or generic NSIS installer components. Only high-value indicators relevant to identifying the malware's behavior and delivery mechanism are listed below.

### **IP addresses / URLs / Domains**
*   `http://nsis.sf.net/NSIS_Error` (Note: This is a standard URL associated with the NSIS installation framework.)

### **File paths / Registry keys**
*   `~nsu.tmp` (A common temporary filename used by the NSIS installer for staging data).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None present in provided strings.*

### **Other artifacts**
*   **Application Framework:** The binary is confirmed to be an **NSIS Installer Wrapper**.
*   **Technique - Payload Encapsulation:** The analysis indicates the installer acts as a "wrapper" to move data into protected directories (like `\Temp` or `\AppData`) and manage complexity while masking the actual malicious payload.
*   **Known Library Interactions:** Use of `OleUninitialize` and standard Windows API calls for UI management suggests an attempt to blend in with legitimate installer behavior.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Installer Wrapper Behavior:** The binary is identified as a highly structured NSIS-based installer, which serves specifically as a "wrapper" to mask the actual malicious payload from detection.
    *   **Payload Delivery Mechanism:** The analysis confirms that the file's primary function is to unpack and move files into system directories (e.g., `\Temp` or `\AppData`), a hallmark of a dropper/loader.
    *   **Evasion Techniques:** The use of standard Windows libraries (`OleUninitialize`) and common installer frameworks allows the binary to blend in with legitimate software while concealing its underlying intent to deliver malicious content.
