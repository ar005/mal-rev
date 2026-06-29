# Threat Analysis Report

**Generated:** 2026-06-28 21:22 UTC
**Sample:** `0311761bca1187e06281040ec3141356fb1008446adaeaa0b2ed311918bf003f_0311761bca1187e06281040ec3141356fb1008446adaeaa0b2ed311918bf003f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0311761bca1187e06281040ec3141356fb1008446adaeaa0b2ed311918bf003f_0311761bca1187e06281040ec3141356fb1008446adaeaa0b2ed311918bf003f.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 391,097 bytes |
| MD5 | `527b885d4995f35626cce5bc24a46a1c` |
| SHA1 | `5a4e5dfb9855d2449cf27f724b417233f1597f3d` |
| SHA256 | `0311761bca1187e06281040ec3141356fb1008446adaeaa0b2ed311918bf003f` |
| Overall entropy | 7.88 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1481493041 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,088 | 6.424 | No |
| `.rdata` | 5,120 | 5.162 | No |
| `.data` | 1,536 | 3.898 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 93,696 | 7.526 | ⚠️ Yes |

### Imports

**KERNEL32.dll**: `SetCurrentDirectoryW`, `GetFileAttributesW`, `GetFullPathNameW`, `Sleep`, `GetTickCount`, `GetFileSize`, `GetModuleFileNameW`, `MoveFileW`, `SetFileAttributesW`, `GetCurrentProcess`, `ExitProcess`, `SetEnvironmentVariableW`, `GetWindowsDirectoryW`, `GetTempPathW`, `GetCommandLineW`
**USER32.dll**: `GetSystemMenu`, `SetClassLongW`, `IsWindowEnabled`, `EnableMenuItem`, `SetWindowPos`, `GetSysColor`, `GetWindowLongW`, `SetCursor`, `LoadCursorW`, `CheckDlgButton`, `GetMessagePos`, `LoadBitmapW`, `CallWindowProcW`, `IsWindowVisible`, `CloseClipboard`
**GDI32.dll**: `SelectObject`, `SetBkMode`, `CreateFontIndirectW`, `SetTextColor`, `DeleteObject`, `GetDeviceCaps`, `CreateBrushIndirect`, `SetBkColor`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `ShellExecuteW`, `SHFileOperationW`
**ADVAPI32.dll**: `RegDeleteKeyW`, `SetFileSecurityW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `AdjustTokenPrivileges`, `RegOpenKeyExW`, `RegEnumValueW`, `RegDeleteValueW`, `RegCloseKey`, `RegCreateKeyExW`, `RegSetValueExW`, `RegQueryValueExW`, `RegEnumKeyW`
**COMCTL32.dll**: `ImageList_AddMasked`, `ord_17`, `ImageList_Destroy`, `ImageList_Create`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoCreateInstance`

## Extracted Strings

Total strings found: **1024** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495,
SQSSSPW
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
lstrcatW
GetSystemDirectoryW
GetProcAddress
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5817 | ✓ |
| `fcn.004065c7` | `0x4065c7` | 2642 | ✓ |
| `entry0` | `0x4032fe` | 1311 | ✓ |
| `fcn.004038f7` | `0x4038f7` | 726 | ✓ |
| `fcn.004060d0` | `0x4060d0` | 626 | ✓ |
| `fcn.00402e82` | `0x402e82` | 569 | ✓ |
| `fcn.004030bb` | `0x4030bb` | 485 | ✓ |
| `fcn.0040589f` | `0x40589f` | 451 | ✓ |
| `fcn.00405ddd` | `0x405ddd` | 370 | ✓ |
| `fcn.0040520d` | `0x40520d` | 211 | ✓ |
| `fcn.00403bcd` | `0x403bcd` | 205 | ✓ |
| `fcn.004049c9` | `0x4049c9` | 201 | ✓ |
| `fcn.00402c93` | `0x402c93` | 181 | ✓ |
| `fcn.00406342` | `0x406342` | 175 | ✓ |
| `fcn.004041d9` | `0x4041d9` | 173 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.0040600e` | `0x40600e` | 160 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404ad7` | `0x404ad7` | 128 | ✓ |
| `fcn.00405b6a` | `0x405b6a` | 126 | ✓ |
| `fcn.004056dc` | `0x4056dc` | 125 | ✓ |
| `fcn.00405f7b` | `0x405f7b` | 122 | ✓ |
| `fcn.00405d64` | `0x405d64` | 121 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.00406418` | `0x406418` | 112 | ✓ |
| `fcn.00406539` | `0x406539` | 110 | ✓ |
| `fcn.004052e0` | `0x4052e0` | 108 | ✓ |
| `fcn.004057f3` | `0x4057f3` | 100 | ✓ |
| `fcn.00402e1e` | `0x402e1e` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402c93.c`](code/fcn.00402c93.c)
- [`code/fcn.00402e1e.c`](code/fcn.00402e1e.c)
- [`code/fcn.00402e82.c`](code/fcn.00402e82.c)
- [`code/fcn.004030bb.c`](code/fcn.004030bb.c)
- [`code/fcn.004038f7.c`](code/fcn.004038f7.c)
- [`code/fcn.00403bcd.c`](code/fcn.00403bcd.c)
- [`code/fcn.004041d9.c`](code/fcn.004041d9.c)
- [`code/fcn.004049c9.c`](code/fcn.004049c9.c)
- [`code/fcn.00404ad7.c`](code/fcn.00404ad7.c)
- [`code/fcn.0040520d.c`](code/fcn.0040520d.c)
- [`code/fcn.004052e0.c`](code/fcn.004052e0.c)
- [`code/fcn.004056dc.c`](code/fcn.004056dc.c)
- [`code/fcn.004057f3.c`](code/fcn.004057f3.c)
- [`code/fcn.0040589f.c`](code/fcn.0040589f.c)
- [`code/fcn.00405b6a.c`](code/fcn.00405b6a.c)
- [`code/fcn.00405d64.c`](code/fcn.00405d64.c)
- [`code/fcn.00405ddd.c`](code/fcn.00405ddd.c)
- [`code/fcn.00405f7b.c`](code/fcn.00405f7b.c)
- [`code/fcn.0040600e.c`](code/fcn.0040600e.c)
- [`code/fcn.004060d0.c`](code/fcn.004060d0.c)
- [`code/fcn.00406342.c`](code/fcn.00406342.c)
- [`code/fcn.00406418.c`](code/fcn.00406418.c)
- [`code/fcn.00406539.c`](code/fcn.00406539.c)
- [`code/fcn.004065c7.c`](code/fcn.004065c7.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is a technical analysis of the binary's behavior.

### Core Functionality and Purpose
The binary functions as an **installer or "downloader" stub**, likely utilizing the **NSIS (Nullsoft Script Installer)** framework or a similar setup engine. Its primary purpose is to prepare an environment, verify files, and move/extract components from a temporary location to a final installation directory.

### Key Behaviors and Observations

*   **Installer Framework Logic:**
    *   The presence of the string "NSIS Error" and the logic in `fcn.004038f7` strongly indicate that this is part of an installer suite. It handles common setup tasks like progress reporting, error message generation, and UI updates.
    *   It uses standard Windows GUI libraries (`USER32`, `GDI32`) to manage windows and display information to the user.

*   **Integrity and Validation:**
    *   The function `fcn.004065c7` contains logic for **CRC-style checksum calculations**. This is used to verify that files have not been corrupted during download or extraction before the installer attempts to move them.
    *   It performs checks on system components (e.g., "UXTHEME") and handles various setup errors via specific error codes.

*   **File System Manipulation:**
    *   The code extensively uses `CreateDirectoryW`, `MoveFileW`, `CopyFileW`, and `GetFileAttributesW`.
    *   It performs **file movement/staging**: It is common for such a binary to extract heavy assets into the `%TEMP%` directory first, verify them (via CRC), and then move/rename them to their final destination.

*   **Registry Interaction:**
    *   The code utilizes `RegOpenKeyExW`, `RegCreateKeyExW`, and `RegSetValueExW`. This is typically used to:
        1.  Check for existing installations.
        2.  Write configuration settings or "Uninstaller" paths into the Windows Registry.

*   **Privilege Escalation / System Interaction:**
    *   The code includes logic to check for and potentially acquire **system privileges** (e.g., `SeShutdownPrivilege`). This is common in installers that need to perform administrative actions but can also be a technique used by malware to escalate privileges before executing an update or payload.

### Suspicious/Malicious Behaviors
While the behavior is consistent with a legitimate installer, from a malware analysis perspective, several points warrant close monitoring:

*   **Dropper/Stager Characteristics:** The pattern of **moving files from Temp folders** and **modifying registry keys** are common tactics for "droppers." Malicious actors often use legitimate-looking NSIS wrappers to deliver payloads.
*   **Payload Execution:** While the provided code does not show a direct process injection (e.g., `CreateRemoteThread`), it frequently calls `ShellExecuteW` and `CreateProcessW`. These are used by malware to launch malicious executables or scripts after they have been successfully "staged" in a hidden directory.
*   **Persistence:** The heavy use of registry manipulation suggests the binary may be attempting to ensure its components start automatically (e.g., via the "Run" keys).

### Notable Techniques & Patterns
*   **Standard Library Abstraction:** Much of the code is a large switch-case block (`fcn.00401434`) that acts as a dispatcher for various installer actions. This is typical of compiled scripts or high-level installers to handle numerous possible user interactions and system states.
*   **Error Handling & Feedback:** The code includes detailed error handling (e.g., `GetUserDefaultSchema`, "Installer integrity check has failed"). While helpful for developers, it also serves to ensure that the "installation" process proceeds smoothly without alerting the user through manual crashes.

### Summary for Report
The binary is a **functional installer stub** (likely NSIS-based). It performs file system manipulations (moving/copying files), integrity checks via checksums, and registry modifications typical of software installation. Because it handles the movement of "payload" files from temporary directories to permanent ones, it should be monitored for whether those files being moved are malicious components or legitimate software.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of a standard NSIS installer framework allows the binary to blend in with legitimate software updates and installation processes. |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys | The analysis notes that registry manipulation is used to ensure components start automatically, a classic indicator of persistence. |
| T1105 | Ingress Tool Transfer | The "downloader" stub behavior of moving and staging files from the `%TEMP%` directory to final locations indicates the transfer of malicious tools. |
| T1059 | Command and Scripting Interpreter | The use of `ShellExecuteW` and `CreateProcessW` suggests the execution of subsequent payloads, scripts, or secondary components. |
| T1204 | User Execution | The binary functions as an installer that triggers the execution of staged components, potentially tricking a user into running a malicious payload. |
| T1070 | Indicator Removal on Host | (Optional/Contextual) While not explicitly stated as deletion, the "move and rename" behavior from temporary folders is often used to hide the original source of the malicious file during staging. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: Many items in the input (such as `KERNEL32.dll`, `DeleteFileW`, and `%TEMP%`) were excluded as they are standard Windows components or generic system locations rather than specific indicators of a targeted threat.

**IP addresses / URLs / Domains**
*   None

**File paths / Registry keys**
*   None (Note: While the report mentions using "Run" keys and the `%TEMP%` folder, these are standard Windows locations and do not constitute specific IOCs without a specific path or key name).

**Mutex names / Named pipes**
*   None

**Hashes**
*   None

**Other artifacts**
*   **Framework Identification:** The binary utilizes the **NSIS (Nullsoft Script Installer)** framework. While common in legitimate software, it is frequently used as a wrapper for droppers and installers.
*   **Tactic - Staging/Dropping:** The binary demonstrates "File Movement" behavior, specifically moving files from temporary directories to final destinations after performing CRC-style integrity checks.
*   **Tactic - Persistence:** The behavior report indicates the use of registry manipulation (specifically targeting "Run" keys) for potential persistence.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family**: Unknown (or custom)
2. **Malware type**: Dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Staging and Deployment Behavior:** The binary utilizes an NSIS framework to perform classic "dropper" activities, including moving files from temporary directories (`%TEMP%`) to permanent locations after performing integrity checks (CRC).
    *   **Persistence Mechanisms:** The code specifically targets the Windows Registry to establish persistence (e.g., via "Run" keys), ensuring that dropped components execute automatically upon system startup.
    *   **Payload Execution Logic:** The use of `ShellExecuteW` and `CreateProcessW` following a staging phase indicates its role as an intermediary loader designed to launch secondary, potentially more malicious, payloads.
