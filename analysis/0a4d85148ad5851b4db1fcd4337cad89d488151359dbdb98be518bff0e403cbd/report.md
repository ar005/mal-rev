# Threat Analysis Report

**Generated:** 2026-07-24 21:07 UTC
**Sample:** `0a4d85148ad5851b4db1fcd4337cad89d488151359dbdb98be518bff0e403cbd_0a4d85148ad5851b4db1fcd4337cad89d488151359dbdb98be518bff0e403cbd.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a4d85148ad5851b4db1fcd4337cad89d488151359dbdb98be518bff0e403cbd_0a4d85148ad5851b4db1fcd4337cad89d488151359dbdb98be518bff0e403cbd.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 391,760 bytes |
| MD5 | `db5d442c2b905a9da0104080935096ed` |
| SHA1 | `24aebf001f3cfcc9baf58e79b308dac674ad857a` |
| SHA256 | `0a4d85148ad5851b4db1fcd4337cad89d488151359dbdb98be518bff0e403cbd` |
| Overall entropy | 6.988 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1544912667 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.431 | No |
| `.rdata` | 5,120 | 5.16 | No |
| `.data` | 1,536 | 3.905 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 165,376 | 5.038 | No |

### Imports

**KERNEL32.dll**: `SetEnvironmentVariableW`, `SetFileAttributesW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `GetCurrentProcess`, `CopyFileW`, `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`, `GetVersion`, `SetErrorMode`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `EnableMenuItem`, `IsWindowEnabled`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ShellExecuteExW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `SHFileOperationW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegCreateKeyExW`, `RegOpenKeyExW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `RegEnumValueW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegCloseKey`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_AddMasked`, `ImageList_Destroy`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **696** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495L
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
WaitForSingleObject
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5795 | ✓ |
| `fcn.004067df` | `0x4067df` | 2642 | ✓ |
| `entry0` | `0x403359` | 1345 | ✓ |
| `fcn.00403974` | `0x403974` | 726 | ✓ |
| `fcn.004062a6` | `0x4062a6` | 626 | ✓ |
| `fcn.00402edd` | `0x402edd` | 569 | ✓ |
| `fcn.00403116` | `0x403116` | 485 | ✓ |
| `fcn.00405996` | `0x405996` | 451 | ✓ |
| `fcn.00405ed0` | `0x405ed0` | 378 | ✓ |
| `fcn.004052ec` | `0x4052ec` | 211 | ✓ |
| `fcn.00404262` | `0x404262` | 207 | ✓ |
| `fcn.00404aa8` | `0x404aa8` | 201 | ✓ |
| `fcn.00403c4a` | `0x403c4a` | 185 | ✓ |
| `fcn.00406518` | `0x406518` | 175 | ✓ |
| `fcn.00402d44` | `0x402d44` | 175 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.004061e4` | `0x4061e4` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404bb6` | `0x404bb6` | 128 | ✓ |
| `fcn.00405c61` | `0x405c61` | 126 | ✓ |
| `fcn.004057bb` | `0x4057bb` | 125 | ✓ |
| `fcn.00406076` | `0x406076` | 123 | ✓ |
| `fcn.00406152` | `0x406152` | 121 | ✓ |
| `fcn.00405e5b` | `0x405e5b` | 117 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004065ee` | `0x4065ee` | 112 | ✓ |
| `fcn.00406751` | `0x406751` | 110 | ✓ |
| `fcn.004053bf` | `0x4053bf` | 108 | ✓ |
| `fcn.004058ea` | `0x4058ea` | 100 | ✓ |

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
- [`code/fcn.00403974.c`](code/fcn.00403974.c)
- [`code/fcn.00403c4a.c`](code/fcn.00403c4a.c)
- [`code/fcn.00404262.c`](code/fcn.00404262.c)
- [`code/fcn.00404aa8.c`](code/fcn.00404aa8.c)
- [`code/fcn.00404bb6.c`](code/fcn.00404bb6.c)
- [`code/fcn.004052ec.c`](code/fcn.004052ec.c)
- [`code/fcn.004053bf.c`](code/fcn.004053bf.c)
- [`code/fcn.004057bb.c`](code/fcn.004057bb.c)
- [`code/fcn.004058ea.c`](code/fcn.004058ea.c)
- [`code/fcn.00405996.c`](code/fcn.00405996.c)
- [`code/fcn.00405c61.c`](code/fcn.00405c61.c)
- [`code/fcn.00405e5b.c`](code/fcn.00405e5b.c)
- [`code/fcn.00405ed0.c`](code/fcn.00405ed0.c)
- [`code/fcn.00406076.c`](code/fcn.00406076.c)
- [`code/fcn.00406152.c`](code/fcn.00406152.c)
- [`code/fcn.004061e4.c`](code/fcn.004061e4.c)
- [`code/fcn.004062a6.c`](code/fcn.004062a6.c)
- [`code/fcn.00406518.c`](code/fcn.00406518.c)
- [`code/fcn.004065ee.c`](code/fcn.004065ee.c)
- [`code/fcn.00406751.c`](code/fcn.00406751.c)
- [`code/fcn.004067df.c`](code/fcn.004067df.c)

## Behavioral Analysis

Based on the analysis of the provided disassembly and strings, here is a breakdown of the binary's functionality.

### Core Functionality and Purpose
The binary functions as a **malware dropper or an "installer" wrapper** (highly likely based on the NSIS—Nullsoft Script Installer—framework). Its primary purpose is to decompress, verify, and stage files for execution on the target system.

Instead of performing its main task directly, it acts as a preliminary stage:
1.  **Environment Setup:** It checks the OS version and initializes common Windows components (COM, Common Controls).
2.  **Payload Extraction:** It identifies temporary paths (`GetTempPathW`) and manipulates environment variables to prepare a location for "unpacking" hidden files.
3.  **Integrity Checking:** It contains complex mathematical loops (likely CRC32 or Adler-32) to ensure that the payload it is extracting has not been corrupted or altered during transmission/extraction.
4.  **Resource Handling:** It uses a large switch-case table (interpreter-style logic) to process a list of commands, which handle file movements, directory creations, and registry updates.

### Suspicious or Malicious Behaviors
While this behavior is common in legitimate installers, it is also the primary signature of "droppers" used by malware to deliver secondary payloads.

*   **Payload Staging:** The use of `GetTempPathW`, `SetEnvironmentVariableW` (for TEMP), and `CopyFileW` suggests the binary is moving "hidden" files from a compressed internal resource into a usable folder on the disk before launching them.
*   **Privilege Escalation/Manipulation:** The code calls `OpenProcessToken`, `LookupPrivilegeValueW`, and `AdjustTokenPrivileges`. Specifically, it attempts to gain privileges (like `SeShutdownPrivilege`) that allow it to perform system-level modifications or interact with protected system files.
*   **Persistence via Registry:** It uses `RegSetValueExW` and `RegDeleteValueW`. In a malicious context, this is used to ensure the "installed" component starts automatically on boot or hides its presence from common tools.
*   **System Persistence/Modification:** The use of `SetFileAttributesW` (to hide files) followed by `MoveFileW` or `CreateDirectoryW` are common tactics for establishing a permanent foothold on the system.

### Notable Techniques and Patterns
*   **Interpreter Loop Strategy:** Function `fcn.00401434` contains a large switch-case block. This is a classic technique used by installers (and some packers) to process an internal "script" or command list, making it harder for simple automated tools to follow the execution flow linearly.
*   **Checksum/Integrity Verification:** Function `fcn.004067df` implements a complex loop with bit-shifting and XOR operations. This is used to verify the integrity of files after they are extracted from the binary's memory or resources.
*   **Shell Interaction:** The inclusion of `SHFileOperationW`, `ShellExecuteExW`, and `GetSpecialFolderLocation` indicates the program interacts heavily with the Windows Shell, likely to execute the final payload automatically after "installation" is complete.
*   **Dynamic Loading:** The code uses `GetProcAddress` logic (implied by the switch table) and `LoadLibraryExW` to load components dynamically, which can be used to delay the detection of malicious imports until the program is actually running.

### Summary for Threat Intelligence
The sample is a **Dropper/Installer**. It is designed to take an obfuscated payload, unpack it into the system's temporary directories or hidden folders, verify its integrity using CRC-style checks, and then potentially escalate privileges to ensure the payload can execute with maximum impact.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of `GetTempPathW` and `SetFileAttributesW` indicates an attempt to blend into the environment and hide files in common system locations. |
| T1068 | Exploitation for Privilege Escalation | The sequence of `OpenProcessToken`, `LookupPrivilegeValueW`, and `AdjustTokenPrivileges` demonstrates a deliberate effort to acquire elevated system privileges. |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys | The use of `RegSetValueExW` suggests the malware is attempting to establish persistence by creating registry keys that trigger at startup. |
| T1059 | Command and Scripting Interpreter | The large switch-case block in `fcn.00401434` functions as a custom interpreter to process internal commands, complicating linear analysis. |
| T1106 | Native API | The use of `GetProcAddress` and `LoadLibraryExW` allows the binary to resolve and load functionality dynamically to evade static detection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: As per your instructions, standard Windows API calls (e.g., `GetTempPathW`, `CreateProcessW`), system DLLs (e.g., `KERNEL32.dll`, `USER32.dll`), and common environment variables were excluded as false positives.*

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (The analysis notes the *use* of registry modification via `RegSetValueExW` and file movement, but no specific target keys or paths were provided in the text.)

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Malware Type:** Dropper / Installer Wrapper.
*   **Technique - Payload Staging:** Use of `GetTempPathW` and `SetEnvironmentVariableW` to stage payloads in temporary directories.
*   **Technique - Privilege Manipulation:** Usage of `AdjustTokenPrivileges` and `LookupPrivilegeValueW` to escalate privileges for system-level modifications.
*   **Technique - Integrity Checking:** Use of custom loops (e.g., `fcn.004067df`) for CRC/checksum verification of unpacked files.
*   **Tactic - Persistence:** Intent to use registry modification to ensure persistent execution.

---
**Analyst Note:** While no static network IOCs (IPs, Domains) or specific local artifacts (Paths, Mutexes) were extracted from the provided data, the behavioral analysis confirms this is a **Dropper/Installer**. The sample relies on standard Windows APIs to perform its actions, likely to blend in with legitimate installer behavior.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family:** Unknown (Generic Installer/Dropper)
2. **Malware type:** dropper
3. **Confidence:** High
4. **Key evidence:**
    * **Payload Staging & Verification:** The binary functions as a wrapper that extracts, moves, and validates the integrity of hidden files using CRC-style loops (`fcn.004067df`) before execution.
    * **Privilege Escalation & Persistence:** It actively attempts to acquire elevated system privileges via `AdjustTokenPrivileges` and establishes persistence through registry modifications (`RegSetValueExW`).
    * **Interpreter Logic:** The use of a large switch-case block (`fcn.00401434`) indicates it is designed as an installer (likely NSIS) to execute a series of scripted commands to deploy the final payload.
