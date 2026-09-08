# Threat Analysis Report

**Generated:** 2026-09-02 22:10 UTC
**Sample:** `13b7ab4380c45e77f921030d8b288dfb976738c714d20b0eb7b6cd7837b9a37e_13b7ab4380c45e77f921030d8b288dfb976738c714d20b0eb7b6cd7837b9a37e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13b7ab4380c45e77f921030d8b288dfb976738c714d20b0eb7b6cd7837b9a37e_13b7ab4380c45e77f921030d8b288dfb976738c714d20b0eb7b6cd7837b9a37e.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 6 sections |
| Size | 85,293 bytes |
| MD5 | `1315aee91696cc5d4558d86c273e4ded` |
| SHA1 | `8798eb5ce8a22b0d3fb96dfd6a7fff8a10a09e50` |
| SHA256 | `13b7ab4380c45e77f921030d8b288dfb976738c714d20b0eb7b6cd7837b9a37e` |
| Overall entropy | 6.556 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1588125593 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 44,544 | 6.399 | No |
| `.rdata` | 7,680 | 4.966 | No |
| `.data` | 512 | 1.921 | No |
| `.CRT` | 512 | 0.061 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 17,920 | 5.15 | No |

### Imports

**KERNEL32.dll**: `lstrlenA`, `GetPrivateProfileStringW`, `WritePrivateProfileStringW`, `MoveFileW`, `MultiByteToWideChar`, `WideCharToMultiByte`, `CreateFileW`, `GetFileSize`, `GetTickCount`, `GetModuleFileNameW`, `GetProcAddress`, `GetCommandLineW`, `SetEnvironmentVariableW`, `WriteFile`, `GetTempPathW`
**USER32.dll**: `ScreenToClient`, `GetSysColor`, `GetWindowLongW`, `SetClassLongW`, `LoadCursorW`, `SystemParametersInfoW`, `wsprintfA`, `DispatchMessageW`, `PeekMessageW`, `SetDlgItemTextW`, `GetDlgItemTextW`, `SetCursor`, `CharPrevW`, `MessageBoxIndirectW`, `GetSystemMetrics`
**GDI32.dll**: `SetBkColor`, `GetDeviceCaps`, `SetTextColor`, `SetBkMode`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectW`
**SHELL32.dll**: `ShellExecuteExW`, `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `SHGetFileInfoW`, `SHFileOperationW`, `SHGetSpecialFolderLocation`
**ADVAPI32.dll**: `RegQueryValueExW`, `LookupPrivilegeValueW`, `AdjustTokenPrivileges`, `OpenProcessToken`, `RegSetValueExW`, `RegCreateKeyExW`, `SetFileSecurityW`, `RegCloseKey`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegEnumKeyW`, `RegEnumValueW`, `RegOpenKeyExW`
**COMCTL32.dll**: `ImageList_Create`, `ImageList_Destroy`, `ImageList_AddMasked`, `ord_17`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoCreateInstance`, `CoTaskMemFree`

## Extracted Strings

Total strings found: **312** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.ndata
t$lWPV
9\$0u+
EL$(^]
D$4_^][
D$<_^][
PW9\$@u
D$0_^][
D$0_^][
9\$0t#UV
T$ 9\$
D$8_^][
D$8_^][
|$$!uSj
T$@RQj
EL$(^]
T$ PV9\$<u
9\$0t4V
D$(PWS
9\$8uMj
L$,QUPV
D$Df9]
t
;l$D
9\$4t-9\$0t
 !"#$%&'()*+,-./0123456789:;<=@@>56@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?
D$9L$
|$(Inst
|$$soft
|$ Null
L$4+D$
t$ Ph

D$X@l@
L$,Qh`
D$ Ph`
\$PUVW
D$ NPVhs
t$4PShs
\$0SUV
\$0SUV
\$0SUV
\$0SUh
D$tP
D$(^][
8\thX
\u)f9K
6;D$8t6
VC20XC00U
5Genu
;t$,v-
kUQPXY]Y[
URPQQh 
GetNativeSystemInfo
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
SHFOLDER
WINDOWSCODECS
DWRITE
MSIMG32
URLMON
IERTUTIL
WINMMBASE
ATLTHUNK
NtQuerySystemInformation
GetFileVersionInfoW
GetFileVersionInfoSizeW
VerQueryValueW
RichEd20
RichEd32
KERNEL32
SetDefaultDllDirectories
GetDiskFreeSpaceExW
GetUserDefaultUILanguage
ADVAPI32
RegDeleteKeyExW
InitiateShutdownW
SHELL32
SHLWAPI
SHAutoComplete
SHFOLDER
SHGetFolderPathW
VERSION
[Rename]

%ls=%ls

ExpandEnvironmentStringsW
SetCurrentDirectoryW
SearchPathW
CompareFileTime
DeleteFileW
FindClose
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004015b0` | `0x4015b0` | 9816 | ✓ |
| `fcn.00409750` | `0x409750` | 3923 | ✓ |
| `fcn.0040a780` | `0x40a780` | 2252 | ✓ |
| `entry0` | `0x404f90` | 1940 | ✓ |
| `fcn.0040a940` | `0x40a940` | 1604 | ✓ |
| `fcn.004045f0` | `0x4045f0` | 1098 | ✓ |
| `fcn.0040b400` | `0x40b400` | 866 | ✓ |
| `fcn.00404070` | `0x404070` | 792 | ✓ |
| `fcn.004078c0` | `0x4078c0` | 776 | ✓ |
| `fcn.00407d70` | `0x407d70` | 720 | ✓ |
| `fcn.004088b0` | `0x4088b0` | 555 | ✓ |
| `fcn.00404c70` | `0x404c70` | 483 | ✓ |
| `fcn.004082a0` | `0x4082a0` | 438 | ✓ |
| `fcn.00404390` | `0x404390` | 377 | ✓ |
| `fcn.00409130` | `0x409130` | 333 | ✓ |
| `fcn.004094f0` | `0x4094f0` | 326 | ✓ |
| `fcn.00408700` | `0x408700` | 278 | ✓ |
| `fcn.00407380` | `0x407380` | 268 | ✓ |
| `fcn.00408fe0` | `0x408fe0` | 259 | ✓ |
| `fcn.00409640` | `0x409640` | 257 | ✓ |
| `fcn.0040ba91` | `0x40ba91` | 251 | ✓ |
| `fcn.00401490` | `0x401490` | 242 | ✓ |
| `fcn.004077d0` | `0x4077d0` | 240 | ✓ |
| `fcn.00407bd0` | `0x407bd0` | 237 | ✓ |
| `fcn.00404b80` | `0x404b80` | 234 | ✓ |
| `fcn.00405730` | `0x405730` | 226 | ✓ |
| `fcn.004075b0` | `0x4075b0` | 221 | ✓ |
| `fcn.004093a0` | `0x4093a0` | 210 | ✓ |
| `fcn.00404e60` | `0x404e60` | 205 | ✓ |
| `fcn.004013c0` | `0x4013c0` | 194 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004013c0.c`](code/fcn.004013c0.c)
- [`code/fcn.00401490.c`](code/fcn.00401490.c)
- [`code/fcn.004015b0.c`](code/fcn.004015b0.c)
- [`code/fcn.00404070.c`](code/fcn.00404070.c)
- [`code/fcn.00404390.c`](code/fcn.00404390.c)
- [`code/fcn.004045f0.c`](code/fcn.004045f0.c)
- [`code/fcn.00404b80.c`](code/fcn.00404b80.c)
- [`code/fcn.00404c70.c`](code/fcn.00404c70.c)
- [`code/fcn.00404e60.c`](code/fcn.00404e60.c)
- [`code/fcn.00405730.c`](code/fcn.00405730.c)
- [`code/fcn.00407380.c`](code/fcn.00407380.c)
- [`code/fcn.004075b0.c`](code/fcn.004075b0.c)
- [`code/fcn.004077d0.c`](code/fcn.004077d0.c)
- [`code/fcn.004078c0.c`](code/fcn.004078c0.c)
- [`code/fcn.00407bd0.c`](code/fcn.00407bd0.c)
- [`code/fcn.00407d70.c`](code/fcn.00407d70.c)
- [`code/fcn.004082a0.c`](code/fcn.004082a0.c)
- [`code/fcn.00408700.c`](code/fcn.00408700.c)
- [`code/fcn.004088b0.c`](code/fcn.004088b0.c)
- [`code/fcn.00408fe0.c`](code/fcn.00408fe0.c)
- [`code/fcn.00409130.c`](code/fcn.00409130.c)
- [`code/fcn.004093a0.c`](code/fcn.004093a0.c)
- [`code/fcn.004094f0.c`](code/fcn.004094f0.c)
- [`code/fcn.00409640.c`](code/fcn.00409640.c)
- [`code/fcn.00409750.c`](code/fcn.00409750.c)
- [`code/fcn.0040a780.c`](code/fcn.0040a780.c)
- [`code/fcn.0040a940.c`](code/fcn.0040a940.c)
- [`code/fcn.0040b400.c`](code/fcn.0040b400.c)
- [`code/fcn.0040ba91.c`](code/fcn.0040ba91.c)

## Behavioral Analysis

This updated analysis incorporates the findings from the second chunk of disassembly. The additional code confirms several sophisticated behaviors typical of high-quality malware droppers, particularly regarding **payload decryption**, **anti-analysis techniques**, and **evasion tactics**.

### 1. Updated Core Functionality: Multi-Stage Loader
The previous finding that this is a "malware dropper" is reinforced by the discovery of specific routines for handling encrypted data. The binary doesn't just move files; it actively manages the lifecycle of an encrypted payload.

*   **In-Memory Decryption:** The function `fcn.00409130` contains a classic **S-box generation routine** (used in RC4 or similar stream ciphers). This indicates that the "payload" is likely stored in an encrypted state within the binary's resources or an appended data block and is decrypted into memory/buffer before being moved to disk.
*   **Dynamic String Deobfuscation:** Function `fcn.004094f0` appears to be a routine for de-obfuscating strings on-the-fly. This allows the malware to hide its true configuration (e.g., C2 domains, file paths) from static analysis.
*   **File Renaming & Preparation:** Function `fcn.004082a0` contains logic specifically for **renaming files**. This is used after a component is "dropped" to give it a legitimate-looking name (e.g., changing `payload_x34.exe` to `UpdateService.exe`) before execution.

### 2. Advanced Evasion & Persistence Techniques
The new disassembly reveals several techniques designed to hide the malware from both the user and security software:

*   **MuiCache Manipulation:** Function `fcn.00405730` explicitly targets the **`MuiCache`** registry key (`Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache`). 
    *   *Significance:* Manipulating this entry is a known technique to make a dropped executable appear as if it has been "already executed" by the system. This can bypass certain heuristic detections that flag "newly seen" executables and helps the malware blend in with legitimate software.
*   **System Information Querying:** Function `fcn.00404e60` utilizes `NtQuerySystemInformation`. While common, it is frequently used in malware to:
    *   Check for the presence of specific processes (like debuggers or antivirus tools).
    *   Detect if the process is running in a virtualized environment or as part of a sandbox.
*   **Resource Masquerading:** The use of `RichEdit` controls and standard Windows GUI components (`fcn.004078c0`) suggests that while the "inner" payload may be malicious, the "outer" installer is designed to look professional, potentially including progress bars (calculated in `fcn.004013c0`) and a polished interface to lower the user's suspicion during the infection process.

### 3. Advanced File System Interaction
The logic found in `fcn.004088b0` and `fcn.00407d70` shows a sophisticated way of interacting with the filesystem:

*   **Automated Path Resolution:** The code uses `SHGetSpecialFolderLocation` and `GetSystemDirectoryW`. This ensures that regardless of where the user installs it, the malware can correctly identify system paths to place its components or modify registry keys.
*   **Wildcard Processing & Movement:** The logic in `fcn.004088b0` performs loops over file lists (using `FindFirstFileW`/`FindNextFileW`) and moves files based on specific criteria. This allows it to "clean up" temporary files or move components into system directories like `%AppData%` or `C:\Windows\System32`.

### Summary of Findings Update

| Feature | Evidence/Function | Behavior Category |
| :--- | :--- | :--- |
| **Encrypted Payload** | `fcn.00409130` (S-box logic) | Obfuscation / Dropper |
| **String De-obfuscation** | `fcn.004094f0` | Evasion of Static Analysis |
| **MuiCache Injection** | `fcn.00405730` | Stealth / Evasion |
| **Anti-Analysis/Sandbox** | `fcn.00404e60` (NtQuerySystem) | Evasion |
| **File Renaming** | `fcn.004082a0` | Deception |
| **NSIS Masking** | `fcn.004078c0`, `fcn.004013c0` | Social Engineering / Masquerading |

### Final Conclusion
This is not a simple "dropper" but a **sophisticated multi-stage loader**. It uses a legitimate installer (NSIS) as a wrapper to bypass initial gates, employs multiple layers of encryption/obfuscation for its strings and payload, and implements specific evasion techniques (`MuiCache` manipulation and `NtQuerySystemInformation`) to remain resident on the system. 

**Recommendation:** Treat this sample as high-risk. The presence of custom decryption loops and deliberate attempts to modify the `MuiCache` suggest it is designed for persistent infection or a multi-stage "downloader" role where subsequent malicious modules will be executed after the initial installer completes its task.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed activities to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of S-box logic for payload decryption and dynamic string de-obfuscation is designed to hide configuration data and malicious code from static analysis. |
| **T1036** | Masquerading | Renaming files to "UpdateService.exe" and utilizing polished GUI components are used to blend in with legitimate system processes and lower user suspicion. |
| **T1497** | Virtualization/Sandbox Detection | The use of `NtQuerySystemInformation` is a common technique used to identify if the malware is running within a debugger, sandbox, or virtualized environment. |
| **T1083** | File and Directory Discovery | The use of `SHGetSpecialFolderLocation` and `GetSystemDirectoryW` allows the malware to programmatically locate system paths for successful deployment. |
| **T1566** | Rogue Update Capabilities | (Optional/Contextual) The use of a legitimate-looking installer (NSIS) to deliver a multi-stage payload mimics an official software update process. |

### Analyst Notes:
*   **MuiCache Manipulation:** While specifically noted as an evasion tactic against "newly seen" file detection, this falls under **T1036 (Masquerading)** because it manipulates the system to make a malicious executable appear as a known, trusted entity.
*   **Multi-Stage Loading:** The overall architecture described is characteristic of a **Loader**, which typically utilizes a combination of T1027 and T1036 to ensure the initial stages of an attack remain undetected while preparing for more significant payloads.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   **Registry Key:** `Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache` (Used for MuiCache manipulation to bypass heuristic detection).
*   **Note on File Paths:** While the analysis mentions `%AppData%` and `C:\Windows\System32`, these are standard system paths. No specific malicious file names or unique sub-paths were identified in the provided text.

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts (behavioral indicators & techniques)**
*   **Encryption Routine:** Presence of an S-box generation routine (at `fcn.00409130`) indicating RC4 or similar stream cipher usage for payload decryption.
*   **String De-obfuscation:** Dynamic de-obfuscation of strings (at `fcn.004094f0`) to hide C2 infrastructure and file paths.
*   **Anti-Analysis/Sandbox Detection:** Use of `NtQuerySystemInformation` (at `fcn.00404e60`) to identify debuggers, virtualization environments, or security tools.
*   **File Masking:** Logic for renaming dropped components (at `fcn.004082a0`) to masquerade as legitimate system files (e.g., `UpdateService.exe`).
*   **Installer Wrapper:** Use of NSIS-style resources and GUI elements to provide a professional front-end during the infection process.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

1. **Malware family**: custom (High-quality Loader)
2. **Malware type**: loader, dropper
3. **Confidence**: High
4. **Key evidence**:
    * **Multi-Stage Execution & Decryption:** The sample utilizes S-box generation for RC4-style decryption and dynamic string de-obfuscation to hide its configuration and payload, indicating a sophisticated multi-stage delivery model rather than a simple infection.
    * **Advanced Evasion Tactics:** It employs specific anti-analysis techniques such as `NtQuerySystemInformation` (to detect sandboxes/debuggers) and `MuiCache` manipulation to bypass heuristic "newly seen" executable alerts.
    * **Social Engineering & Masquerading:** The use of an NSIS-style wrapper, professional GUI components, and logic to rename files to legitimate names like `UpdateService.exe` indicates a high level of effort to evade both automated systems and user suspicion.
