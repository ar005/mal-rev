# Threat Analysis Report

**Generated:** 2026-07-09 20:39 UTC
**Sample:** `043411ec48a610695668589c877e96b333b1a7b2ba07304ab0776339edf61cc1_043411ec48a610695668589c877e96b333b1a7b2ba07304ab0776339edf61cc1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `043411ec48a610695668589c877e96b333b1a7b2ba07304ab0776339edf61cc1_043411ec48a610695668589c877e96b333b1a7b2ba07304ab0776339edf61cc1.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 5 sections |
| Size | 496,128 bytes |
| MD5 | `5dc395bdeed0ac727586defc61a6b8d2` |
| SHA1 | `51dc56f5c78ccac565abf297ebbec24e27b97c3e` |
| SHA256 | `043411ec48a610695668589c877e96b333b1a7b2ba07304ab0776339edf61cc1` |
| Overall entropy | 7.829 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1653432546 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.314 | No |
| `.data` | 512 | 4.971 | No |
| `.idata` | 4,608 | 5.026 | No |
| `.rsrc` | 461,824 | 7.877 | ⚠️ Yes |
| `.reloc` | 2,560 | 6.223 | No |

### Imports

**ADVAPI32.dll**: `GetTokenInformation`, `RegDeleteValueA`, `RegOpenKeyExA`, `RegQueryInfoKeyA`, `FreeSid`, `OpenProcessToken`, `RegSetValueExA`, `RegCreateKeyExA`, `LookupPrivilegeValueA`, `AllocateAndInitializeSid`, `RegQueryValueExA`, `EqualSid`, `RegCloseKey`, `AdjustTokenPrivileges`
**KERNEL32.dll**: `_lopen`, `_llseek`, `CompareStringA`, `GetLastError`, `GetFileAttributesA`, `GetSystemDirectoryA`, `LoadLibraryA`, `DeleteFileA`, `GlobalAlloc`, `GlobalFree`, `CloseHandle`, `WritePrivateProfileStringA`, `IsDBCSLeadByte`, `GetWindowsDirectoryA`, `SetFileAttributesA`
**GDI32.dll**: `GetDeviceCaps`
**USER32.dll**: `SetWindowLongA`, `GetDlgItemTextA`, `DialogBoxIndirectParamA`, `ShowWindow`, `MsgWaitForMultipleObjects`, `SetWindowPos`, `GetDC`, `GetWindowRect`, `DispatchMessageA`, `GetDesktopWindow`, `CharUpperA`, `SetDlgItemTextA`, `ExitWindowsEx`, `MessageBeep`, `EndDialog`
**msvcrt.dll**: `_controlfp`, `?terminate@@YAXXZ`, `_acmdln`, `_initterm`, `__setusermatherr`, `_except_handler4_common`, `memcpy`, `_ismbblead`, `__p__fmode`, `_cexit`, `_exit`, `exit`, `__set_app_type`, `__getmainargs`, `_amsg_exit`
**COMCTL32.dll**: `ord_17`
**Cabinet.dll**: `ord_22`, `ord_23`, `ord_21`, `ord_20`
**VERSION.dll**: `GetFileVersionInfoA`, `VerQueryValueA`, `GetFileVersionInfoSizeA`

## Extracted Strings

Total strings found: **1311** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.idata
@.rsrc
@.reloc
advapi32.dll
CheckTokenMembership
Reboot
AdvancedINF
Version
setupx.dll
setupapi.dll
SeShutdownPrivilege
advpack.dll
DelNodeRunDLL32
wininit.ini
Software\Microsoft\Windows\CurrentVersion\App Paths
HeapSetInformation
EXTRACTOPT
INSTANCECHECK
VERCHECK
DecryptFileA
LICENSE
<None>
REBOOT
SHOWWINDOW
ADMQCMD
USRQCMD
RUNPROGRAM
POSTRUNPROGRAM
FINISHMSG
LoadString() Error.  Could not load string resource.
CABINET
FILESIZES
PACKINSTSPACE
UPROMPT
IXP%03d.TMP
msdownld.tmp
TMP4351$.TMP
RegServer
UPDFILE%lu
Control Panel\Desktop\ResourceLocale
wextract.pdb
.rdata$brc
.CRT$XCA
.CRT$XCAA
.CRT$XCZ
.CRT$XIA
.CRT$XIAA
.CRT$XIY
.CRT$XIZ
.gfids
.rdata
.rdata$sxdata
.rdata$zzzdbg
.text$mn
.xdata$x
.idata$5
.00cfg
.idata$2
.idata$3
.idata$4
.idata$6
.rsrc$01
.rsrc$02
PQQQQQQh 
PSSSSSSh 
D$<tXh
PVVVVVV
w;Urw
|$$95(
D$HjDj
D$@t	
WWj WWWSW
t;j
Wj
t;<\u
8
<At <Bt
<t<
t
<t<
t
<t<
t
<
t}<ty<tu
<At	<Ut
Sj@Sh@
j
XPVSh
DSystem\CurrentControlSet\Control\Session Manager
rundll32.exe %sadvpack.dll,DelNodeRunDLL32 "%s"
Software\Microsoft\Windows\CurrentVersion\RunOnce
wextract_cleanup%d
rundll32.exe %s,InstallHinfSection %s 128 %s
PendingFileRenameOperations
DefaultInstall
Command.com /c %s
%s /D:%s
System\CurrentControlSet\Control\Session Manager\FileRenameOperations
SHELL32.DLL
DoInfInstall
SHBrowseForFolder
SHGetPathFromIDList
*MEMCAB
GetTokenInformation
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00405c9e` | `0x405c9e` | 1408 | ✓ |
| `fcn.00403ba2` | `0x403ba2` | 1101 | ✓ |
| `fcn.00401ae8` | `0x401ae8` | 959 | ✓ |
| `fcn.004036ee` | `0x4036ee` | 849 | ✓ |
| `fcn.004055a0` | `0x4055a0` | 808 | ✓ |
| `fcn.0040597d` | `0x40597d` | 666 | ✓ |
| `fcn.00402caa` | `0x402caa` | 625 | ✓ |
| `fcn.0040202a` | `0x40202a` | 573 | ✓ |
| `entry0` | `0x406a60` | 479 | ✓ |
| `fcn.004044b9` | `0x4044b9` | 470 | ✓ |
| `fcn.00404224` | `0x404224` | 428 | ✓ |
| `fcn.004028e8` | `0x4028e8` | 417 | ✓ |
| `fcn.00402f1d` | `0x402f1d` | 412 | ✓ |
| `fcn.00404fe0` | `0x404fe0` | 388 | ✓ |
| `fcn.00402773` | `0x402773` | 373 | ✓ |
| `fcn.00402390` | `0x402390` | 336 | ✓ |
| `fcn.00402aac` | `0x402aac` | 335 | ✓ |
| `fcn.00405467` | `0x405467` | 313 | ✓ |
| `fcn.004018a3` | `0x4018a3` | 310 | ✓ |
| `fcn.0040681f` | `0x40681f` | 307 | ✓ |
| `fcn.00403fef` | `0x403fef` | 300 | ✓ |
| `fcn.00402267` | `0x402267` | 297 | ✓ |
| `fcn.00406d1a` | `0x406d1a` | 272 | ✓ |
| `fcn.004052b6` | `0x4052b6` | 235 | ✓ |
| `fcn.004043d0` | `0x4043d0` | 233 | ✓ |
| `fcn.0040268b` | `0x40268b` | 232 | ✓ |
| `fcn.00403a3f` | `0x403a3f` | 231 | ✓ |
| `fcn.00406298` | `0x406298` | 230 | ✓ |
| `fcn.004051e5` | `0x4051e5` | 209 | ✓ |
| `fcn.00404efd` | `0x404efd` | 205 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004018a3.c`](code/fcn.004018a3.c)
- [`code/fcn.00401ae8.c`](code/fcn.00401ae8.c)
- [`code/fcn.0040202a.c`](code/fcn.0040202a.c)
- [`code/fcn.00402267.c`](code/fcn.00402267.c)
- [`code/fcn.00402390.c`](code/fcn.00402390.c)
- [`code/fcn.0040268b.c`](code/fcn.0040268b.c)
- [`code/fcn.00402773.c`](code/fcn.00402773.c)
- [`code/fcn.004028e8.c`](code/fcn.004028e8.c)
- [`code/fcn.00402aac.c`](code/fcn.00402aac.c)
- [`code/fcn.00402caa.c`](code/fcn.00402caa.c)
- [`code/fcn.00402f1d.c`](code/fcn.00402f1d.c)
- [`code/fcn.004036ee.c`](code/fcn.004036ee.c)
- [`code/fcn.00403a3f.c`](code/fcn.00403a3f.c)
- [`code/fcn.00403ba2.c`](code/fcn.00403ba2.c)
- [`code/fcn.00403fef.c`](code/fcn.00403fef.c)
- [`code/fcn.00404224.c`](code/fcn.00404224.c)
- [`code/fcn.004043d0.c`](code/fcn.004043d0.c)
- [`code/fcn.004044b9.c`](code/fcn.004044b9.c)
- [`code/fcn.00404efd.c`](code/fcn.00404efd.c)
- [`code/fcn.00404fe0.c`](code/fcn.00404fe0.c)
- [`code/fcn.004051e5.c`](code/fcn.004051e5.c)
- [`code/fcn.004052b6.c`](code/fcn.004052b6.c)
- [`code/fcn.00405467.c`](code/fcn.00405467.c)
- [`code/fcn.004055a0.c`](code/fcn.004055a0.c)
- [`code/fcn.0040597d.c`](code/fcn.0040597d.c)
- [`code/fcn.00405c9e.c`](code/fcn.00405c9e.c)
- [`code/fcn.00406298.c`](code/fcn.00406298.c)
- [`code/fcn.0040681f.c`](code/fcn.0040681f.c)
- [`code/fcn.00406d1a.c`](code/fcn.00406d1a.c)

## Behavioral Analysis

### Executive Summary
The analyzed binary is a **dropper/installer** typically used in the initial stages of a multi-stage malware infection. Its primary purpose is to unpack hidden resources, verify system privileges, and install secondary components (DLLs or executables) onto the host system while ensuring they can run automatically. It employs several common "packer" techniques, such as resource extraction, persistence via registry keys, and privilege checking.

---

### Key Behaviors & Malicious Characteristics

#### 1. Persistence Mechanism
*   **Registry Manipulation:** The code specifically targets the `Software\Microsoft\Windows\CurrentVersion\RunOnce` key (seen in functions `fcn.0040202a` and `fcn.00402267`).
*   **Delayed Execution/Cleanup:** It creates entries like `"rundll32.exe %sadvpack.dll,DelNodeRunDLL32 \"%s\""`. This is a common technique to ensure that follow-up actions (like deleting the original dropper or performing "cleanup") occur automatically upon restart or login.

#### 2. Resource Extraction & Payload Loading
*   **Embedded Resources:** The function `fcn.00406298` iterates through the binary's resource section (`FindResourceA`, `LoadResource`). It extracts multiple items, suggesting it carries a suite of tools or "plug-ins" inside its own body.
*   **Cabinet/Archive Handling:** Use of `Cabinet.dll_FDICreate` and `FDICopy` (in `fcn.00404efd`) indicates the binary is capable of decompressing files. This is a classic indicator of a "packer" or "dropper" that wraps encrypted or compressed payloads to evade basic signature-based detection.

#### 3. Privilege & Environment Validation
*   **Privilege Escalation Checks:** Function `fcn.004018a3` uses `OpenProcessToken`, `GetTokenInformation`, and `EqualSid`. It is checking if the current process has specific high-level privileges (likely Administrator or System rights) before attempting to perform system-level modifications.
*   **System Geometry/Check:** Function `fcn.0040597d` calculates available disk space (`GetDiskFreeSpaceA`) and volume information, ensuring there is enough room for the extracted payload.

#### 4. Process Execution & Interaction
*   **Process Spawning:** The function `fcn.00403fef` wraps `CreateProcessA`. It spawns a child process, waits for it to complete (`WaitForSingleObject`), and then checks the exit code. This "fire-and-forget" or "wait-for-completion" logic is typical when the dropper is installing a driver or a persistent service.
*   **Injected/Loaded Modules:** The use of `LoadLibraryA` and `GetProcAddress` (in `fcn.00402264`) to load modules dynamically suggests it may be loading specific functions from system DLLs to perform tasks like installing INF files or interacting with the Windows Installer service.

#### 5. Defense Evasion / Obfuscation
*   **Dynamic Path Resolution:** The code uses `GetTempPathA` and `GetSystemDirectoryA` to resolve paths at runtime rather than hardcoding them, making it harder for automated tools to predict where files will be dropped.
*   **String Manipulation:** Function `fcn.00405c9e` performs extensive sanitization of strings (removing quotes, handling escape characters). This is often used to "clean" paths before passing them to system APIs to avoid errors during the execution of malicious commands.

---

### Summary Table of Technical Indicators
| Category | Observed Technique/Indicator | Purpose |
| :--- | :--- | :--- |
| **Persistence** | `RunOnce` Registry Key | Ensures components run after a reboot or logoff. |
| **Payload Delivery** | `Cabinet.dll` & Resource Extraction | Unpacks hidden, compressed payloads from inside the binary. |
| **Privilege Check** | `EqualSid`, `GetTokenInformation` | Verifies if it has the rights to perform system changes. |
| **Process Injection** | `CreateProcessA` with `WaitForSingleObject` | Executes and waits for secondary components/droppers. |
| **Anti-Analysis** | Dynamic resolution of API addresses | Hides intent from simple static analysis tools. |

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the following MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys | The binary targets the `RunOnce` registry key to ensure malicious components persist and execute after a reboot or login. |
| **T1564.001** | Archive File Extraction | The use of `Cabinet.dll` (e.g., `FDICreate`, `FDICopy`) indicates that the malware extracts compressed payloads from its own resources. |
| **T1027** | Obfuscated Files or Information | The use of "packer" techniques and extensive string manipulation are used to hide code functionality and payload information from static analysis. |
| **T1484** | System Host Information Discovery | The utilization of `GetTokenInformation` and `EqualSid` allows the malware to check for high-level privileges before attempting system modifications. |
| **T1059** | Command and Scripting Interpreter | The use of `CreateProcessA` followed by a wait loop is used to execute, manage, and verify the completion of secondary payloads or scripts. |
| **T1106** | Native API | Using `LoadLibraryA` and `GetProcAddress` allows the malware to resolve functions at runtime, evading detection from simple static analysis of the Import Address Table (IAT). |
| **T1036** | Masquerading | By using `GetSystemDirectoryA` to resolve paths at runtime, the malware attempts to blend in with legitimate system components and locations. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Persistence mechanism)
*   `wininit.ini` (Configuration file)
*   `advpack.dll,DelNodeRunDLL32` (Specific function call/path used within the `rundll32.exe` command for cleanup routines)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Command Execution Pattern:** `rundll32.exe %sadvpack.dll,DelNodeRunDLL32 "%s"` (Used for automated cleanup/execution)
*   **Temporary File Patterns:** 
    *   `IXP%03d.TMP`
    *   `msdownld.tmp`
    *   `TMP4351$.TMP`
*   **Payload Extraction Logic:** Use of `Cabinet.dll_FDICreate` and `FDICopy` for unpacking embedded resources.
*   **Persistence Strategy:** Automated execution via the `RunOnce` registry key following a primary drop/infection phase.

---

## Malware Family Classification

1. **Malware family**: Unknown (Potential custom dropper)
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

**Key evidence**:
*   **Payload Packaging & Extraction:** The use of `Cabinet.dll`, `FindResourceA`, and `LoadResource` indicates the binary is designed to wrap, decompress, and extract hidden payloads from its own resource section—a hallmark of a dropper or loader.
*   **Staged Execution & Persistence:** The implementation of "Wait-for-Completion" logic (`WaitForSingleObject`) after spawning processes, combined with `RunOnce` registry persistence for automated cleanup/installation routines, confirms it is part of a multi-stage infection chain.
*   **Environment Preparation:** Validating system privileges via `EqualSid` and `GetTokenInformation` ensures the environment is prepared for the subsequent execution of more complex components (e.g., remote access tools or miners).
