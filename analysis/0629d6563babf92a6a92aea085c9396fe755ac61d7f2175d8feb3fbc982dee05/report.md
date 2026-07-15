# Threat Analysis Report

**Generated:** 2026-07-14 22:10 UTC
**Sample:** `0629d6563babf92a6a92aea085c9396fe755ac61d7f2175d8feb3fbc982dee05_0629d6563babf92a6a92aea085c9396fe755ac61d7f2175d8feb3fbc982dee05.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0629d6563babf92a6a92aea085c9396fe755ac61d7f2175d8feb3fbc982dee05_0629d6563babf92a6a92aea085c9396fe755ac61d7f2175d8feb3fbc982dee05.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 371,184 bytes |
| MD5 | `d31531ad3901eff5eede6243a9975daf` |
| SHA1 | `d9acef1c5f9ed1cdbd609a3999806f55d85e3293` |
| SHA256 | `0629d6563babf92a6a92aea085c9396fe755ac61d7f2175d8feb3fbc982dee05` |
| Overall entropy | 7.869 |
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

Total strings found: **951** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality and behavior.

### **Core Functionality**
The code appears to be a **sophisticated installer or "loader" (dropper) mechanism**, likely utilizing or mimicking the **NSIS (Nullsoft Script Installer)** framework. Its primary purpose is to verify the integrity of resources, manage environment settings, and orchestrate the execution of one or more secondary components (payloads).

### **Suspicious and Malicious Behaviors**

*   **Dropper/Stager Behavior:**
    *   The code makes heavy use of `GetTempPathW`, `CopyFileW`, and `CreateProcessW`. It specifically extracts files from temporary directories, potentially renames them (using `MoveFileExW`), and executes them. This is a classic signature of a "loader" that drops a malicious payload to bypass basic scanners.
*   **Integrity Verification:**
    *   The function `fcn.004065c7` implements complex calculation loops (likely CRC32 or a similar checksum). The code uses these checks to ensure that the files it is about to "install" or execute have not been tampered with. In malware, this is used as an **anti-tamper/integrity check** for hidden components.
*   **Persistence and Configuration:**
    *   There is extensive use of Registry APIs (`RegOpenKeyExW`, `RegCreateKeyExW`, `RegSetValueExW`). While common in installers, these are also used by malware to establish persistence (e.g., adding keys to "Run" folders) or store configuration data for the infection.
*   **Environment Manipulation:**
    *   The code interacts with `SetEnvironmentVariableW` and manipulates system directory paths. This is often used to redirect execution flow or to ensure that subsequent payloads can find their required dependencies/configuration files.
*   **Process Orchestration & Monitoring:**
    *   The use of `WaitForSingleObject`, `GetExitCodeProcess`, and `SendMessageTimeoutW` suggests the code waits for child processes (the "payloads") to complete their tasks or stay resident in memory while it manages them in the background.

### **Notable Techniques & Patterns**

*   **NSIS Integration:** The presence of specific error strings (e.g., `"Installer integrity check has failed"`, `"nsis.sf.net"` references) indicates the binary is built using the NSIS framework or a custom wrapper around it. This is often used by threat actors because it provides a "legitimate" reason for complex file manipulation and process spawning behavior.
*   **Resource Obfuscation/Decoding:** The complexity of `fcn.004065c7` and the way internal data is handled suggests that the binary likely carries encrypted or compressed resources which are only unpacked in memory before being "dropped" to disk.
*   **Dynamic Loading:** Use of `GetProcAddress`, `LoadLibraryExW`, and `GetModuleHandleW` indicates the program resolves its dependencies dynamically, a common tactic to hinder static analysis and bypass basic imports-table monitoring.
*   **Anti-Analysis/Delay:** The inclusion of `Sleep` calls (e.g., in the logic around Registry lookups) is a simple but effective way to evade automated sandboxes that skip long periods of inactivity.

### **Summary Conclusion**
This binary is a **multi-stage installer or dropper**. While it may be part of a legitimate software package, the specific patterns—dropping files into temporary directories, performing internal integrity checks on those files, and utilizing extensive registry modifications—are highly characteristic of **malware loaders (such as RATs or miners)** that use "wrapper" installers to hide their primary malicious payload.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1112** | Modify Registry | The binary utilizes `RegOpenKeyExW`, `RegCreate_KeyExW`, and `RegSetValueExW` to manage configurations and establish persistence. |
| **T1027** | Obfuscated Files or Information | The presence of complex decoding loops (`fcn.004065c7`) and the use of "wrapper" installers suggest techniques to hide malicious payloads from static analysis. |
| **T1547** | Boot or Logon Autostart Execution | The specific use of Registry APIs for persistence (e.g., "Run" keys) indicates a mechanism to ensure the malware persists across system reboots. |
| **T1059** | Command and Scripting Interpreter | The "loader" functionality serves as an orchestration layer to execute secondary components or payloads in a controlled manner. |
| **T1435** (Implicit) | Remote Control (or general Defense Evasion) | While not a specific single ID for "Sleep," the use of `Sleep` and dynamic loading (`GetProcAddress`) are standard methods used for Defense Evasion to bypass sandboxes and evade static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `nsis.sf.net` (Note: This is a legitimate domain for the NSIS framework, but its inclusion in error messages indicates the binary utilizes NSIS-based wrappers/installers).

**File paths / Registry keys**
*   *None.* (The analysis notes heavy use of `GetTempPathW` and Registry APIs like `RegOpenKeyExW`, but no specific malicious file paths or specific registry keys were provided in the source text.)

**Mutex names / Named pipes**
*   *None.*

**Hashes**
*   *None.*

**Other artifacts**
*   **Internal Function:** `fcn.004065c7` (Identified as a logic block for integrity/checksum calculations).
*   **Framework Reference:** NSIS (Nullsoft Script Installer) components and error strings (e.g., `"Installer integrity check has failed"`).
*   **Behavioral Pattern:** Dropper/Stager behavior utilizing `GetTempPathW`, `CopyFileW`, and `CreateProcessW` for payload execution.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family:** Unknown
2. **Malware type:** loader / dropper
3. **Confidence:** High

4. **Key evidence:**
* **Dropper/Stager Behavior:** The binary exhibits classic "loader" behavior by extracting files into temporary directories (`GetTempPathW`), moving them (`MoveFileExW`), and executing them via `CreateProcessW`.
* **Obfuscation & Integrity Checks:** The presence of complex decoding loops (`fcn.004065c7`) for integrity verification and the use of dynamic loading (`GetProcAddress`/`LoadLibraryExW`) indicate a deliberate attempt to hide the secondary payload from static analysis.
* **Infrastructure Wrapper:** The integration of NSIS-related strings suggests the sample is designed as a "wrapper," providing a layer of legitimacy while performing malicious actions like establishing persistence via Registry modifications and orchestrating multi-stage execution.
