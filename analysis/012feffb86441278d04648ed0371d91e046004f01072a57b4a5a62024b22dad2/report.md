# Threat Analysis Report

**Generated:** 2026-06-26 18:56 UTC
**Sample:** `012feffb86441278d04648ed0371d91e046004f01072a57b4a5a62024b22dad2_012feffb86441278d04648ed0371d91e046004f01072a57b4a5a62024b22dad2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `012feffb86441278d04648ed0371d91e046004f01072a57b4a5a62024b22dad2_012feffb86441278d04648ed0371d91e046004f01072a57b4a5a62024b22dad2.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 158,629 bytes |
| MD5 | `1f941ccbf50d80370c99acff3593cb02` |
| SHA1 | `6098c7053eff8e8004b108599c42ed757c926732` |
| SHA256 | `012feffb86441278d04648ed0371d91e046004f01072a57b4a5a62024b22dad2` |
| Overall entropy | 7.704 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1501547642 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.434 | No |
| `.rdata` | 5,120 | 5.236 | No |
| `.data` | 1,536 | 4.045 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 16,384 | 6.033 | No |

### Imports

**KERNEL32.dll**: `GetTempPathA`, `GetFileSize`, `GetModuleFileNameA`, `GetCurrentProcess`, `CopyFileA`, `ExitProcess`, `SetEnvironmentVariableA`, `Sleep`, `GetTickCount`, `GetCommandLineA`, `lstrlenA`, `GetVersion`, `SetErrorMode`, `lstrcpynA`, `GetDiskFreeSpaceA`
**USER32.dll**: `ScreenToClient`, `GetSystemMenu`, `SetClassLongA`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongA`, `SetCursor`, `LoadCursorA`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapA`, `CallWindowProcA`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectA`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExA`, `SHGetPathFromIDListA`, `SHBrowseForFolderA`, `SHGetFileInfoA`, `SHFileOperationA`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExA`, `RegOpenKeyExA`, `SetFileSecurityA`, `OpenProcessToken`, `LookupPrivilegeValueA`, `RegEnumValueA`, `RegDeleteKeyA`, `RegDeleteValueA`, `RegCloseKey`, `RegSetValueExA`, `RegQueryValueExA`, `RegEnumKeyA`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **523** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495L
tQVPW
Et@;u
v#Vha,@
Instu`
softuW
NulluN	E
D$$Ph,
D$(SPS
tVj%SSS
D$$+D$
D$,+D$$P
us9Et	
8\tPV
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
RichEdit
RichEdit20A
RichEd32
RichEd20
.DEFAULT\Control Panel\International
Control Panel\Desktop\ResourceLocale
Software\Microsoft\Windows\CurrentVersion
\Microsoft\Internet Explorer\Quick Launch
MulDiv
DeleteFileA
FindFirstFileA
FindNextFileA
FindClose
SetFilePointer
GetPrivateProfileStringA
WritePrivateProfileStringA
MultiByteToWideChar
FreeLibrary
LoadLibraryExA
GetModuleHandleA
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
GetFileSize
GetModuleFileNameA
GetCurrentProcess
CopyFileA
ExitProcess
SetEnvironmentVariableA
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
CreateDirectoryA
CreateProcessA
RemoveDirectoryA
CreateFileA
GetTempFileNameA
ReadFile
WriteFile
lstrcpyA
MoveFileExA
lstrcatA
GetSystemDirectoryA
GetProcAddress
GetExitCodeProcess
WaitForSingleObject
KERNEL32.dll
EndPaint
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5423 | ✓ |
| `fcn.00406422` | `0x406422` | 2639 | ✓ |
| `entry0` | `0x4031f1` | 1258 | ✓ |
| `fcn.00406f19` | `0x406f19` | 827 | ✓ |
| `fcn.004037b5` | `0x4037b5` | 709 | ✓ |
| `fcn.00405f87` | `0x405f87` | 584 | ✓ |
| `fcn.00402d48` | `0x402d48` | 569 | ✓ |
| `fcn.00402f81` | `0x402f81` | 530 | ✓ |
| `fcn.0040572d` | `0x40572d` | 464 | ✓ |
| `fcn.00405bd4` | `0x405bd4` | 368 | ✓ |
| `fcn.0040508c` | `0x40508c` | 210 | ✓ |
| `fcn.0040484d` | `0x40484d` | 197 | ✓ |
| `fcn.00403a7a` | `0x403a7a` | 185 | ✓ |
| `fcn.00402bb4` | `0x402bb4` | 173 | ✓ |
| `fcn.0040408d` | `0x40408d` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.004061cf` | `0x4061cf` | 153 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00405edc` | `0x405edc` | 137 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404957` | `0x404957` | 128 | ✓ |
| `fcn.00405552` | `0x405552` | 125 | ✓ |
| `fcn.00405d70` | `0x405d70` | 123 | ✓ |
| `fcn.004059eb` | `0x4059eb` | 120 | ✓ |
| `fcn.00405e4c` | `0x405e4c` | 119 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004063b4` | `0x4063b4` | 110 | ✓ |
| `fcn.0040628f` | `0x40628f` | 110 | ✓ |
| `fcn.0040515e` | `0x40515e` | 108 | ✓ |
| `fcn.00406eb1` | `0x406eb1` | 104 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402bb4.c`](code/fcn.00402bb4.c)
- [`code/fcn.00402d48.c`](code/fcn.00402d48.c)
- [`code/fcn.00402f81.c`](code/fcn.00402f81.c)
- [`code/fcn.004037b5.c`](code/fcn.004037b5.c)
- [`code/fcn.00403a7a.c`](code/fcn.00403a7a.c)
- [`code/fcn.0040408d.c`](code/fcn.0040408d.c)
- [`code/fcn.0040484d.c`](code/fcn.0040484d.c)
- [`code/fcn.00404957.c`](code/fcn.00404957.c)
- [`code/fcn.0040508c.c`](code/fcn.0040508c.c)
- [`code/fcn.0040515e.c`](code/fcn.0040515e.c)
- [`code/fcn.00405552.c`](code/fcn.00405552.c)
- [`code/fcn.0040572d.c`](code/fcn.0040572d.c)
- [`code/fcn.004059eb.c`](code/fcn.004059eb.c)
- [`code/fcn.00405bd4.c`](code/fcn.00405bd4.c)
- [`code/fcn.00405d70.c`](code/fcn.00405d70.c)
- [`code/fcn.00405e4c.c`](code/fcn.00405e4c.c)
- [`code/fcn.00405edc.c`](code/fcn.00405edc.c)
- [`code/fcn.00405f87.c`](code/fcn.00405f87.c)
- [`code/fcn.004061cf.c`](code/fcn.004061cf.c)
- [`code/fcn.0040628f.c`](code/fcn.0040628f.c)
- [`code/fcn.004063b4.c`](code/fcn.004063b4.c)
- [`code/fcn.00406422.c`](code/fcn.00406422.c)
- [`code/fcn.00406eb1.c`](code/fcn.00406eb1.c)
- [`code/fcn.00406f19.c`](code/fcn.00406f19.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis. The new code provides further insight into how the binary handles internal data processing, specifically regarding buffer management and potential payload preparation.

### Updated Analysis Summary

The sample remains classified as a **Dropper** or **Custom Installer**. The addition of the newly analyzed function (`fcn.00406eb1`) reinforces the conclusion that this is a sophisticated installer (likely using NSIS) designed to unpack, decrypt, or prepare secondary components for execution.

---

### Core Functionality and Purpose
The sample functions as a **Dropper** or a **Custom Installer**. The presence of specific error strings (e.g., "Installer integrity check has failed," "NSIS_Error") and the overall structure indicate that this is an installer designed to deploy, install, or unpack additional components onto a target system.

### Suspicious and Malicious Behaviors
The binary exhibits several behaviors typical of malware droppers and installers:

*   **File Manipulation & Extraction:** 
    *   The code extensively uses `CopyFileA`, `MoveFileA`, and `DeleteFileA`. It specifically handles moving files from temporary directories (via `GetTempPathA`) to permanent locations. This is a primary indicator of "unpacking" behavior, where the initial executable drops a secondary payload onto the disk.
    *   It validates its own integrity by checking file sizes and content before proceeding with installation steps.

*   **Privilege Escalation:** 
    *   The code calls `AdjustTokenPrivileges` to request higher-level privileges (such as `SeShutdownPrivilege`). While common in legitimate installers, this is also a standard technique for malware to gain the permissions necessary to modify system files or registry keys protected by Windows.

*   **Persistence and System Modification:**
    *   The sample contains extensive logic for interacting with the Windows Registry (`RegOpenKeyExA`, `RegSetValueExA`, `RegEnumKeyA`). It iterates through keys to set values, which are often used to ensure a program (or malware) restarts automatically upon reboot.
    *   It interacts with "Special Folders" via `SHGetSpecialFolderLocation` and `ShellExecuteExA` to find common locations for installation and execution.

*   **Environment Manipulation:**
    *   The code actively manipulates environment variables, such as changing or verifying the `TEMP` path. This can be used to ensure that temporary files are handled in a way that favors the malware's persistence.

### New Findings from Chunk 2/2 (Data Processing & Buffer Management)

The addition of function `fcn.00406eb1` reveals more about how the binary handles data internally:

*   **Robust Memory Copying / Data Decryption:**
    *   Function `fcn.00406eb1` contains a complex loop that performs arithmetic on memory offsets (`0x9bb0`, `0x9bb4`, `0x9bb8`). The logic calculates the "distance" between pointers and adjusts them incrementally (e.g., `uVar3 = uVar2 - uVar4`).
    *   This type of logic is typical of **advanced memory copying or string processing routines** that must handle overlapping regions or specific buffer limits. In the context of a dropper, this is often where the binary handles the **decryption or decompression of its payload** before writing it to disk.

*   **Resource Handling:**
    *   The use of large offsets from the base pointer suggests the code is interacting with complex internal structures (likely part of the NSIS engine or a custom wrapper). This indicates that the program manages multiple "blocks" of data, potentially handling different components of the installation simultaneously or preparing them in memory to avoid detection by simple string-searching scanners.

*   **Automatic Logic Execution:**
    *   The call to `fcn.00405ab9()` inside the loop suggests a modular approach where the "work" (the actual copying/processing) is delegated to a sub-function while the outer loop manages the state and boundaries of the memory blocks.

### Notable Techniques & Patterns
*   **NSIS Framework usage:** The error strings and logic flow suggest it uses the Nullsoft Script Installer (NSIS). Malware authors frequently use legitimate installer frameworks to wrap and deploy malicious payloads, as these tools are less likely to be flagged by simple signature-based antivirus.
*   **Dynamic API Loading/Resolution:** The code makes frequent calls to `GetProcAddress` and `GetModuleHandleA`. This is often used to dynamically resolve function addresses at runtime, making static analysis slightly more difficult for automated systems.
*   **GUI "Decoy" Behavior:** The inclusion of extensive UI-related logic (via `user32.dll` and `gdi32.dll`), such as `MessageBoxIndirectA`, `SetWindowTextA`, and even font creation, suggests it creates a functional user interface to appear like a legitimate installer to the end-user while performing background malicious actions.
*   **Search & Path Resolution:** It uses `GetFullPathNameA` and `GetShortPathNameA` extensively to resolve relative paths, ensuring that its installation routine works regardless of how the installer is launched or where it is currently residing.

### Conclusion Update
The inclusion of advanced memory management logic in chunk 2/2 suggests a high level of sophistication in the way the payload is handled. The binary does not simply move files; it manages internal data buffers meticulously. This strongly indicates that the payload may be encrypted or packed, and the utility functions identified are responsible for unpacking that payload into its final form before the installer "finishes" its routine.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1560.003** | Archive Extraction: Other | The use of `CopyFileA`, `MoveFileA`, and complex memory management loops indicates the binary is unpacking or preparing secondary payloads from an initial installer file. |
| **T1068** | Exploitation for Privilege Escalation | Calling `AdjustTokenPrivileges` to acquire elevated rights (like `SeShutdownPrivilege`) allows the malware to bypass standard limitations and modify protected system files. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys | The interaction with `RegSetValueExA` for various keys indicates an attempt to ensure persistence by automatically launching the payload upon system reboot. |
| **T1546** | Modification of Environment Variables | The active manipulation of the `TEMP` path is a technique used to influence how subsequent processes or scripts handle temporary files and system paths. |
| **T1027** | Obfuscated Files or Information | The sophisticated arithmetic loops on memory offsets suggest that internal data (payloads) are being decrypted or decompressed before being written to disk. |
| **T1036** | Masquerading | Using the NSIS framework and creating a functional GUI with `user32.dll` elements serves as a "decoy" to blend in with legitimate installation processes. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs). 

**Note:** Following your instructions, standard Windows system paths, common API calls, and generic library files have been excluded as they are not unique to a specific malicious threat.

### **IP addresses / URLs / Domains**
*None identified.*

### **File paths / Registry keys**
*None identified.* (The paths provided in the strings—such as `Control Panel\Desktop\ResourceLocale` and `Software\Microsoft\Windows\CurrentVersion`—are standard Windows system paths.)

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None identified.*

### **Other artifacts**
*   **Framework/Tooling:** NSIS (Nullsoft Script Installer). The analysis identifies the use of "NSIS_Error" strings and standard NSIS logic, indicating the malware uses this legitimate installer framework to wrap or unpack its payload.
*   **Behavioral Note:** The binary utilizes heavy **Dynamic API Loading** (`GetProcAddress`, `GetModuleHandleA`) and specific memory management routines (likely for decryption/decompression of the primary payload).

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family**: Unknown
2. **Malware type**: Dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Payload Preparation & Unpacking:** The binary utilizes sophisticated memory management routines and arithmetic loops (as seen in `fcn.00406eb1`) to decrypt, decompress, or unpack secondary components before they are written to disk.
    *   **Masquerading Tactics:** It employs the NSIS framework and includes legitimate-looking GUI elements/dialogs to hide its malicious activity behind a "standard" installer interface.
    *   **Malicious Persistence & Escalation:** The sample actively attempts to gain elevated privileges (`AdjustTokenPrivileges`), modify environment variables, and establish persistence via Windows Registry keys, all of which are characteristic behaviors of a dropper.
