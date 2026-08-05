# Threat Analysis Report

**Generated:** 2026-08-04 21:09 UTC
**Sample:** `0d26f7dbf57f5046777613ba4b28856e2375a31971a9d5ff789d9d265d88eb9a_0d26f7dbf57f5046777613ba4b28856e2375a31971a9d5ff789d9d265d88eb9a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d26f7dbf57f5046777613ba4b28856e2375a31971a9d5ff789d9d265d88eb9a_0d26f7dbf57f5046777613ba4b28856e2375a31971a9d5ff789d9d265d88eb9a.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 1,055,616 bytes |
| MD5 | `1f3db92afe323ae80d5f24bd5691d09e` |
| SHA1 | `b658a98dad7fad3bdf174b3fa34994dedef37bad` |
| SHA256 | `0d26f7dbf57f5046777613ba4b28856e2375a31971a9d5ff789d9d265d88eb9a` |
| Overall entropy | 7.969 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1596249828 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.403 | No |
| `.rdata` | 5,120 | 5.057 | No |
| `.data` | 1,536 | 4.09 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 30,720 | 5.326 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExA`, `RegEnumKeyA`, `RegQueryValueExA`, `RegSetValueExA`, `RegCloseKey`, `RegDeleteValueA`, `RegDeleteKeyA`, `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, `OpenProcessToken`, `SetFileSecurityA`, `RegOpenKeyExA`, `RegEnumValueA`
**SHELL32.dll**: `SHGetFileInfoA`, `SHFileOperationA`, `SHGetPathFromIDListA`, `ShellExecuteExA`, `SHGetSpecialFolderLocation`, `SHBrowseForFolderA`
**ole32.dll**: `IIDFromString`, `OleInitialize`, `OleUninitialize`, `CoCreateInstance`, `CoTaskMemFree`
**COMCTL32.dll**: `ord_17`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`
**USER32.dll**: `SetClipboardData`, `CharPrevA`, `CallWindowProcA`, `PeekMessageA`, `DispatchMessageA`, `MessageBoxIndirectA`, `GetDlgItemTextA`, `SetDlgItemTextA`, `GetSystemMetrics`, `CreatePopupMenu`, `AppendMenuA`, `TrackPopupMenu`, `FillRect`, `EmptyClipboard`, `LoadCursorA`
**GDI32.dll**: `SetBkMode`, `SetBkColor`, `GetDeviceCaps`, `CreateFontIndirectA`, `CreateBrushIndirect`, `DeleteObject`, `SetTextColor`, `SelectObject`
**KERNEL32.dll**: `GetExitCodeProcess`, `WaitForSingleObject`, `GetProcAddress`, `GetSystemDirectoryA`, `WideCharToMultiByte`, `MoveFileExA`, `GetTempFileNameA`, `RemoveDirectoryA`, `WriteFile`, `CreateDirectoryA`, `GetLastError`, `CreateProcessA`, `GlobalLock`, `GlobalUnlock`, `CreateThread`

## Extracted Strings

Total strings found: **2460** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
tQVPW
Et@;u
vX95HGB
Instu`
softuW
NulluN	E
D$(SPS
tVj%SSS
D$$+D$
D$,+D$$P
u9=@B
SSSSjn
us9Et	
8\tPV
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
RichEdit
RichEdit20A
RichEd32
RichEd20
.DEFAULT\Control Panel\International
Control Panel\Desktop\ResourceLocale
Software\Microsoft\Windows\CurrentVersion
\Microsoft\Internet Explorer\Quick Launch
RegEnumValueA
RegEnumKeyA
RegQueryValueExA
RegSetValueExA
RegCloseKey
RegDeleteValueA
RegDeleteKeyA
AdjustTokenPrivileges
LookupPrivilegeValueA
OpenProcessToken
SetFileSecurityA
RegOpenKeyExA
RegCreateKeyExA
ADVAPI32.dll
SHFileOperationA
SHGetFileInfoA
SHBrowseForFolderA
SHGetPathFromIDListA
ShellExecuteExA
SHGetSpecialFolderLocation
SHELL32.dll
CoTaskMemFree
CoCreateInstance
OleUninitialize
OleInitialize
IIDFromString
ole32.dll
ImageList_Destroy
ImageList_AddMasked
ImageList_Create
COMCTL32.dll
EndPaint
DrawTextA
FillRect
GetClientRect
BeginPaint
DefWindowProcA
SendMessageA
InvalidateRect
EnableWindow
ReleaseDC
LoadImageA
SetWindowLongA
GetDlgItem
IsWindow
FindWindowExA
SendMessageTimeoutA
wsprintfA
ShowWindow
SetForegroundWindow
PostQuitMessage
SetWindowTextA
SetTimer
CreateDialogParamA
DestroyWindow
ExitWindowsEx
CharNextA
DialogBoxParamA
GetClassInfoA
CreateWindowExA
SystemParametersInfoA
RegisterClassA
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5688 | ✓ |
| `fcn.00406776` | `0x406776` | 2642 | ✓ |
| `entry0` | `0x403461` | 1256 | ✓ |
| `fcn.00403a3b` | `0x403a3b` | 709 | ✓ |
| `fcn.00402ef1` | `0x402ef1` | 673 | ✓ |
| `fcn.004062bb` | `0x4062bb` | 584 | ✓ |
| `fcn.004059f0` | `0x4059f0` | 464 | ✓ |
| `fcn.00405e97` | `0x405e97` | 368 | ✓ |
| `fcn.0040329a` | `0x40329a` | 361 | ✓ |
| `fcn.00403192` | `0x403192` | 264 | ✓ |
| `fcn.00402cd0` | `0x402cd0` | 234 | ✓ |
| `fcn.0040534f` | `0x40534f` | 210 | ✓ |
| `fcn.00404313` | `0x404313` | 207 | ✓ |
| `fcn.00404af5` | `0x404af5` | 197 | ✓ |
| `fcn.00403d00` | `0x403d00` | 185 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.00402e52` | `0x402e52` | 159 | ✓ |
| `fcn.00406503` | `0x406503` | 153 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.0040619f` | `0x40619f` | 137 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.00404bff` | `0x404bff` | 128 | ✓ |
| `fcn.00405815` | `0x405815` | 125 | ✓ |
| `fcn.00406033` | `0x406033` | 123 | ✓ |
| `fcn.00405cae` | `0x405cae` | 120 | ✓ |
| `fcn.0040610f` | `0x40610f` | 119 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004066e8` | `0x4066e8` | 110 | ✓ |
| `fcn.004065c3` | `0x4065c3` | 110 | ✓ |
| `fcn.00405421` | `0x405421` | 108 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402cd0.c`](code/fcn.00402cd0.c)
- [`code/fcn.00402e52.c`](code/fcn.00402e52.c)
- [`code/fcn.00402ef1.c`](code/fcn.00402ef1.c)
- [`code/fcn.00403192.c`](code/fcn.00403192.c)
- [`code/fcn.0040329a.c`](code/fcn.0040329a.c)
- [`code/fcn.00403a3b.c`](code/fcn.00403a3b.c)
- [`code/fcn.00403d00.c`](code/fcn.00403d00.c)
- [`code/fcn.00404313.c`](code/fcn.00404313.c)
- [`code/fcn.00404af5.c`](code/fcn.00404af5.c)
- [`code/fcn.00404bff.c`](code/fcn.00404bff.c)
- [`code/fcn.0040534f.c`](code/fcn.0040534f.c)
- [`code/fcn.00405421.c`](code/fcn.00405421.c)
- [`code/fcn.00405815.c`](code/fcn.00405815.c)
- [`code/fcn.004059f0.c`](code/fcn.004059f0.c)
- [`code/fcn.00405cae.c`](code/fcn.00405cae.c)
- [`code/fcn.00405e97.c`](code/fcn.00405e97.c)
- [`code/fcn.00406033.c`](code/fcn.00406033.c)
- [`code/fcn.0040610f.c`](code/fcn.0040610f.c)
- [`code/fcn.0040619f.c`](code/fcn.0040619f.c)
- [`code/fcn.004062bb.c`](code/fcn.004062bb.c)
- [`code/fcn.00406503.c`](code/fcn.00406503.c)
- [`code/fcn.004065c3.c`](code/fcn.004065c3.c)
- [`code/fcn.004066e8.c`](code/fcn.004066e8.c)
- [`code/fcn.00406776.c`](code/fcn.00406776.c)

## Behavioral Analysis

Based on the provided disassembly and strings, this binary functions as a **multi-stage installer or dropper**, likely utilizing the **NSIS (Nullsoft Script Installer)** framework.

The code is designed to unpack resources from an archive, verify their integrity, and "drop" them onto the system for execution. While these are standard behaviors for legitimate software installers, they are also common techniques used by malware to deliver payloads while masking the final malicious action behind a legitimate-looking installation process.

### Core Functionality
*   **Installer Logic:** The presence of strings like `NSIS Error`, the manipulation of temporary paths (`GetTempPathA`), and the use of standard UI libraries (GDI, COMCTL32) indicate this is an installer wrapper. 
*   **File Extraction & Handling:** The code contains logic to extract files from a compressed or wrapped package. It creates temporary files in the system's temp directory, moves them, and prepares them for execution.
*   **Integrity Verification:** A specific function (`fcn.004066e8`) implements a **CRC32-like checksum algorithm** (identified by the constant `0xedb88320`). This is used to ensure that the files being unpacked are not corrupted or tampered with.
*   **Environment Preparation:** The code checks for system privileges and sets environment variables, ensuring the installer has the necessary "context" to modify the system.

### Suspicious or Malicious Behaviors
*   **Dropper Behavior:** The binary extracts several components (likely a primary executable and its dependencies) into the `%TEMP%` directory before running them. This is a classic "dropper" technique where the initial file (this one) serves only to deliver the actual payload.
*   **Privilege Escalation/Manipulation:** There is specific logic involving `AdjustTokenPrivileges` and `LookupPrivilegeValueA`. While often used by installers to grant permissions for installing drivers or system services, this can also be used by malware to gain administrative rights.
*   **Persistence/System Modification:** The code includes calls to interact with the registry (`RegSetValueExA`, `RegCreateKeyExA`) and file systems to modify system settings or ensure parts of the installer run on startup (though specific persistence keys aren't visible in this snippet, the infrastructure is there).
*   **Silent Execution:** The logic for parsing command-line arguments looks for "silent" switches (e.g., `/S`). While common in installers, malware uses these to install components without alerting the user via GUI prompts.

### Notable Techniques & Patterns
*   **NSIS Wrapper Pattern:** The code structure—specifically the way it handles `GetTempPathA`, creates a `.tmp` file, and then performs a `CopyFile` or `MoveFile` operation—is highly characteristic of an NSIS-built installer. 
*   **Self-Extraction:** The use of many internal functions to "unzip" or unpack data suggests that the original malicious payload is hidden inside this binary's resource section, only being extracted and decrypted at runtime.
*   **Resource Manipulation:** The code uses `GetFileAttributesA` and `SetFileAttributesA`, which can be used to hide files (e.g., making a file "hidden" or "system") immediately after they are dropped onto the disk.
*   **API Abstraction:** The large switch-case structure (`fcn.00401434`) suggests a highly modulared engine that handles various types of UI interactions and system calls, designed to provide a consistent experience regardless of what "content" it is currently installing.

### Summary for Analysis
This binary is likely the **delivery vehicle** for an attack. It acts as an installer wrapper that:
1.  Checks and modifies environment/privileges.
2.  Extracts potentially malicious payloads from its own internal storage.
3.  Verifies those files using CRC checks.
4.  Drops these files into temporary directories to bypass basic security filters that only scan the initial executable.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The binary utilizes an NSIS wrapper and standard installer logic to disguise its role as a "dropper," hiding malicious actions behind a legitimate installation process. |
| **T1548** | Abuse Elevation Control | The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueA` indicates the binary is attempting to gain higher privileges to perform system-level modifications. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | The analysis identifies registry manipulation (`RegCreateKeyExA`, `RegSetValueExA`) intended to ensure that components of the installer run on system startup. |
| **T1027** | Obfuscated Files or Information | The implementation of a CRC32-like checksum algorithm ensures payload integrity, which is a common method used to verify that dropped files haven't been tampered with by security software. |
| **T1490** | [Inferred: Dropper Behavior] | While not a single ID, the "Dropper" behavior described (extracting components from a resource section into a temporary directory) is an orchestration of T1036 and T1548. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs). 

Note: Many entries in the source text were identified as standard Windows APIs or common system components and have been excluded to filter out false positives.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `.DEFAULT\Control Panel\International`
*   `Control Panel\Desktop\ResourceLocale`
*   `Software\Microsoft\Windows\CurrentVersion`
*   `\Microsoft\Internet Explorer\Quick Launch` 
*(Note: These are standard Windows registry locations; their presence indicates the installer interacts with system localization and UI settings.)*

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified. (The value `0xedb88320` mentioned in the analysis is a CRC32 mathematical constant, not a file hash).

**Other artifacts**
*   **Infrastructure/Framework:** NSIS (Nullsoft Script Installer) 
*   **Mechanism:** Dropper/Wrapper behavior (extracting payloads into `%TEMP%` directories).
*   **Logic Constants:** CRC32-style checksum verification (Constant: `0xedb88320`).
*   **Command Line Patterns:** Support for "silent" installation switches (e.g., `/S`).
*   **Privilege Manipulation:** Use of `AdjustTokenPrivileges` and `LookupPrivilegeValueA` to escalate/modify permissions.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: dropper
3. **Confidence**: High (Regarding its role as a delivery mechanism)

**Key evidence**:
*   **NSIS Wrapper Utilization:** The sample utilizes standard Nullsoft Script Installer (NSIS) logic to mask its activity, mimicking a legitimate software installer while performing multi-stage execution.
*   **Payload Extraction and Verification:** It incorporates a CRC32-based verification system (`0xedb88320`) to ensure the integrity of hidden components extracted from its internal resource section into `%TEMP%` directories.
*   **Environment Manipulation:** The binary explicitly utilizes privilege escalation techniques (`AdjustTokenPrivileges`) and registry modifications to prepare the system environment for executing subsequent payloads, characteristic of a sophisticated downloader/dropper.
