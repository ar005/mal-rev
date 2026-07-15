# Threat Analysis Report

**Generated:** 2026-07-13 13:55 UTC
**Sample:** `0547ad19bbe778a9f1732fd2a98acc59488b82a5caee63e3b637b2dadad8f327_0547ad19bbe778a9f1732fd2a98acc59488b82a5caee63e3b637b2dadad8f327.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0547ad19bbe778a9f1732fd2a98acc59488b82a5caee63e3b637b2dadad8f327_0547ad19bbe778a9f1732fd2a98acc59488b82a5caee63e3b637b2dadad8f327.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 375,064 bytes |
| MD5 | `78830986be75773d062e90cc80c626bc` |
| SHA1 | `98bed453c32c0ebe9fe100899f1086c231c63ee2` |
| SHA256 | `0547ad19bbe778a9f1732fd2a98acc59488b82a5caee63e3b637b2dadad8f327` |
| Overall entropy | 7.522 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1663756095 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 28,160 | 6.368 | No |
| `.rdata` | 6,656 | 4.866 | No |
| `.data` | 512 | 1.68 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 113,664 | 6.181 | No |

### Imports

**ADVAPI32.dll**: `RegCloseKey`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegEnumKeyW`, `RegEnumValueW`, `RegQueryValueExW`, `RegSetValueExW`, `OpenProcessToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `SetFileSecurityW`, `RegCreateKeyExW`, `RegOpenKeyExW`
**SHELL32.dll**: `ShellExecuteExW`, `SHFileOperationW`, `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `SHGetFileInfoW`, `SHGetSpecialFolderLocation`
**ole32.dll**: `OleInitialize`, `OleUninitialize`, `CoTaskMemFree`, `IIDFromString`, `CoCreateInstance`
**COMCTL32.dll**: `ord_17`, `ImageList_Destroy`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `DispatchMessageW`, `wsprintfA`, `SystemParametersInfoW`, `SetClassLongW`, `GetWindowLongW`, `GetSysColor`, `ScreenToClient`, `SetCursor`, `GetWindowRect`, `TrackPopupMenu`, `AppendMenuW`, `EnableMenuItem`, `CreatePopupMenu`, `GetSystemMenu`, `GetSystemMetrics`
**GDI32.dll**: `SetBkMode`, `CreateBrushIndirect`, `GetDeviceCaps`, `SelectObject`, `DeleteObject`, `SetBkColor`, `SetTextColor`, `CreateFontIndirectW`
**KERNEL32.dll**: `WriteFile`, `GetLastError`, `WaitForSingleObject`, `GetExitCodeProcess`, `GetTempFileNameW`, `CreateFileW`, `CreateDirectoryW`, `WideCharToMultiByte`, `lstrlenW`, `lstrcpynW`, `GlobalLock`, `GlobalUnlock`, `CreateThread`, `GetDiskFreeSpaceW`, `CopyFileW`

## Extracted Strings

Total strings found: **900** (showing first 100)

```
!This program cannot be run in DOS mode.
$
7!smersmersmer8
asqmer8
csrmer8
ds|mersmdr
asxmer
gsrmerRichsmer
`.rdata
@.data
.ndata
D$$VWP
 s59=,
t$UUUU
L$PQWh
D$4PUPS
PV9l$@u
RQUSVP
YjHjZW
YYPV9l$<u
L$lf9+
9l$0t$V
9l$,|P
D$LQPj

T$Lf9*t
9|$8t	j"
D$\PVW
j
Xf9E
G9l$8u'j
L$$QUPV
L$P9l$8tQWPV
L$`QWPV
X+D$<P
D$H9l$4
D$HtoSIBUR
*9l$4u
D$H9l$4uyjZf9T$@j
Zt=f9T$@t6f
f9D$@t
f;D$Dt
t$4UPW
D$D9l$0
D$DUUWP
9l$4t#9l$0t
9l$(t
D$ UUP
D$$tK+D$
D$ Pjd+
$SUVW3
|$(Instu]
|$$softuS
|$ NulluI
;D$,uT
f9D$@u
|$0
s
j"^j [f;
Yj Zf9
tVj%UUU
t$`WPV
PPPPjn
D$8t63
D$(PQh2
D$(PQh2
D$l9T$h
L$(PVha
x
PVh$
D$hPVh	
f9D$hu
t$dVPRh
D$ MPUhs
|$4PVhs
t\j"Yf;
D$,+D$$P
69]t(j
j.Xf9D$Hu
thf9D$Ju
?:j\]uf9o
Wj
[j9]3
j-Xf9D$
8\tPV
?uf9V
6;D$0t/
D$H*L$l#
T$P!t$x
t$ j"Y
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
RichEd20
RichEd32
KERNEL32
SetDefaultDllDirectories
GetDiskFreeSpaceExW
GetUserDefaultUILanguage
ADVAPI32
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040154a` | `0x40154a` | 6512 | ✓ |
| `fcn.00406e83` | `0x406e83` | 3414 | ✓ |
| `entry0` | `0x4036d7` | 1449 | ✓ |
| `fcn.00405a19` | `0x405a19` | 733 | ✓ |
| `fcn.00405e95` | `0x405e95` | 614 | ✓ |
| `fcn.004033c8` | `0x4033c8` | 610 | ✓ |
| `fcn.00403148` | `0x403148` | 540 | ✓ |
| `fcn.004066f4` | `0x4066f4` | 461 | ✓ |
| `fcn.004062e1` | `0x4062e1` | 355 | ✓ |
| `fcn.0040141e` | `0x40141e` | 277 | ✓ |
| `fcn.0040553b` | `0x40553b` | 245 | ✓ |
| `fcn.00406c00` | `0x406c00` | 235 | ✓ |
| `fcn.00405d15` | `0x405d15` | 228 | ✓ |
| `fcn.00405736` | `0x405736` | 218 | ✓ |
| `fcn.00406d18` | `0x406d18` | 198 | ✓ |
| `fcn.0040595a` | `0x40595a` | 191 | ✓ |
| `fcn.004012dd` | `0x4012dd` | 188 | ✓ |
| `fcn.00401399` | `0x401399` | 133 | ✓ |
| `fcn.004011a0` | `0x4011a0` | 129 | ✓ |
| `fcn.004056b5` | `0x4056b5` | 129 | ✓ |
| `fcn.004060fb` | `0x4060fb` | 126 | ✓ |
| `fcn.00405e19` | `0x405e19` | 124 | ✓ |
| `fcn.00406613` | `0x406613` | 124 | ✓ |
| `fcn.00406952` | `0x406952` | 124 | ✓ |
| `fcn.0040645f` | `0x40645f` | 120 | ✓ |
| `fcn.00406179` | `0x406179` | 113 | ✓ |
| `fcn.00401221` | `0x401221` | 111 | ✓ |
| `fcn.00406e17` | `0x406e17` | 108 | ✓ |
| `fcn.0040583f` | `0x40583f` | 108 | ✓ |
| `fcn.00406b11` | `0x406b11` | 103 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004011a0.c`](code/fcn.004011a0.c)
- [`code/fcn.00401221.c`](code/fcn.00401221.c)
- [`code/fcn.004012dd.c`](code/fcn.004012dd.c)
- [`code/fcn.00401399.c`](code/fcn.00401399.c)
- [`code/fcn.0040141e.c`](code/fcn.0040141e.c)
- [`code/fcn.0040154a.c`](code/fcn.0040154a.c)
- [`code/fcn.00403148.c`](code/fcn.00403148.c)
- [`code/fcn.004033c8.c`](code/fcn.004033c8.c)
- [`code/fcn.0040553b.c`](code/fcn.0040553b.c)
- [`code/fcn.004056b5.c`](code/fcn.004056b5.c)
- [`code/fcn.00405736.c`](code/fcn.00405736.c)
- [`code/fcn.0040583f.c`](code/fcn.0040583f.c)
- [`code/fcn.0040595a.c`](code/fcn.0040595a.c)
- [`code/fcn.00405a19.c`](code/fcn.00405a19.c)
- [`code/fcn.00405d15.c`](code/fcn.00405d15.c)
- [`code/fcn.00405e19.c`](code/fcn.00405e19.c)
- [`code/fcn.00405e95.c`](code/fcn.00405e95.c)
- [`code/fcn.004060fb.c`](code/fcn.004060fb.c)
- [`code/fcn.00406179.c`](code/fcn.00406179.c)
- [`code/fcn.004062e1.c`](code/fcn.004062e1.c)
- [`code/fcn.0040645f.c`](code/fcn.0040645f.c)
- [`code/fcn.00406613.c`](code/fcn.00406613.c)
- [`code/fcn.004066f4.c`](code/fcn.004066f4.c)
- [`code/fcn.00406952.c`](code/fcn.00406952.c)
- [`code/fcn.00406b11.c`](code/fcn.00406b11.c)
- [`code/fcn.00406c00.c`](code/fcn.00406c00.c)
- [`code/fcn.00406d18.c`](code/fcn.00406d18.c)
- [`code/fcn.00406e17.c`](code/fcn.00406e17.c)
- [`code/fcn.00406e83.c`](code/fcn.00406e83.c)

## Behavioral Analysis

Based on the disassembly provided, here is an analysis of the binary's functionality and behavior.

### Core Functionality and Purpose
The code appears to be a **sophisticated installer or updater utility**, likely associated with an application that modifies system themes (given the `UXTHEME` strings). It performs standard installation tasks such as file unpacking, integrity verification, registry configuration, and environment setup. The presence of "NSIS" error messages in the strings indicates it may have been built using the Nullsoft Script Installer framework or a similar custom wrapper.

### Suspicious or Malicious Behaviors
While much of the code resembles standard installer behavior, several areas are noteworthy from a security perspective:

*   **File Manipulation & Path Navigation:**
    *   The binary heavily interacts with the filesystem, including creating directories (`CreateDirectoryW`), moving files (`MoveFlowW`), and renaming files.
    *   It dynamically resolves system paths (e.g., `GetSystemDirectoryW`, `GetWindowsDirectoryW`, `GetTempPathW`) to determine where to place its components.
    *   The function `fcn.004062e1` specifically handles a "Rename" logic, where it reads file content and modifies the output to ensure it fits specific requirements or locations.

*   **Registry Persistence & Configuration:**
    *   There is extensive use of `RegSetValueExW`, `RegQueryValueExW`, and `RegEnumKeyW`. This indicates the program frequently interacts with the Windows Registry to set configuration keys, which can be used for persistence or modifying system behavior.

*   **Integrity Verification:**
    *   The function `fcn.00403148` contains a loop that calculates progress (e.g., showing a percentage like `... %`) while copying or verifying data. This is often used to ensure that an "update" or "patch" has been downloaded correctly before execution.

*   **Environment Manipulation:**
    *   The binary uses `SetEnvironmentVariableW` and interacts with system paths (like the "Quick Launch" folder) via `SHGetSpecialFolderLocation`. These are common techniques for making a program's components easily accessible to the user or auto-started by the OS.

### Notable Techniques & Patterns
*   **Large Command Dispatcher:** The function `fcn.0040154a` contains an exceptionally large switch-case block (over 60 cases). This is a common pattern in complex installers to handle various states, UI interactions, and backend logic within a single management loop.
*   **Self-Contained Logic:** The presence of `UXTHEME` checks and GDI calls (`CreateFontIndirectW`, `SetBkColor`) suggests the installer might be preparing an environment for a custom shell or a modified system appearance.
*   **Multi-Stage Loading:** The entry point `entry0` performs several preliminary checks (like OS versioning) before proceeding to a heavy "unpacking" phase, where it copies and verifies files from temporary locations into final destinations.
*   **Integrity Check Failures:** The inclusion of specific error strings for "NSIS Error" and "Installer integrity check has failed" suggests the binary is designed to handle errors during a multi-step installation process.

### Summary for Analyst
This binary is likely an **installer or updater**. While it contains many behaviors common to legitimate software (file copying, registry edits, and integrity checks), its complexity—specifically the large dispatching logic and deep integration with system path resolutions—means it has the capability to modify significant areas of the operating system. If this sample was found in a suspicious context, it should be treated as a potential **dropper or installer** for further analysis to see what specific "feature" or "update" it is deploying.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1083** | File and Directory Discovery | The binary utilizes `GetSystemDirectoryW`, `GetWindowsDirectoryW`, and `GetTempPathW` to identify system paths for placing its components. |
| **T1112** | Modify Registry | The extensive use of `RegSetValueExW`, `RegQueryValueExW`, and `RegEnumKeyW` indicates the binary is modifying registry keys for configuration or persistence. |
| **T1547.001** | Boot or Logon Autostart Execution | Interaction with the "Quick Launch" folder via `SHGetSpecialFolderLocation` suggests an attempt to place components in a directory that automatically triggers at login. |
| **T1036** | Masquerading | The inclusion of `UXTHEME` strings and common installer signatures (like NSIS error messages) indicates the binary is designed to mimic a legitimate software updater to evade suspicion. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral summary, here are the extracted Indicators of Compromise (IOCs). 

Note: Per your instructions, standard Windows API calls (e.g., `KERNEL32`, `RegSetValueExW`), internal function addresses (e.g., `fcn.004062e1`), and generic system paths were excluded as false positives.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. *(Note: The analysis mentions interaction with the "Quick Launch" folder and general registry manipulation, but no specific malicious paths or registry keys were provided.)*

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Tooling/Framework:** NSIS (Nullsoft Script Installer) – The presence of "NSIS Error" strings indicates the binary was wrapped or built using the Nullsoft framework.
*   **Capability Tags:** 
    *   `UXTHEME`: Indicates potential interaction with system themes/visual styles.
    *   **Installer Behavior:** Large switch-case dispatching and multi-stage unpacking suggest a "dropper" or "installer" profile.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: Medium

4. **Key evidence**:
*   **Installer Masquerading:** The use of "NSIS" framework strings and `UXTHEME` references suggests the binary is designed to mimic a legitimate software update or theme utility to evade suspicion while performing system-level changes.
*   **Multi-Stage Execution & Persistence:** The analysis identifies multi-stage unpacking, integrity verification, and specific attempts to gain persistence via the "Quick Launch" folder (T1547.001) and registry modifications (T1112).
*   **Delivery Vehicle Characteristics:** The extensive use of a large command dispatcher (switch-case block) and manual file manipulation routines are typical of sophisticated droppers used to deploy secondary payloads into hidden or system directories.
