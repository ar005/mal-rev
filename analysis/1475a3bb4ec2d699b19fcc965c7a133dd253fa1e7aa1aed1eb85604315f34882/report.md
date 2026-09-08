# Threat Analysis Report

**Generated:** 2026-09-05 14:55 UTC
**Sample:** `1475a3bb4ec2d699b19fcc965c7a133dd253fa1e7aa1aed1eb85604315f34882_1475a3bb4ec2d699b19fcc965c7a133dd253fa1e7aa1aed1eb85604315f34882.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1475a3bb4ec2d699b19fcc965c7a133dd253fa1e7aa1aed1eb85604315f34882_1475a3bb4ec2d699b19fcc965c7a133dd253fa1e7aa1aed1eb85604315f34882.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 5 sections |
| Size | 496,128 bytes |
| MD5 | `735af08a6a65e4efc3f6d2c70427c0e5` |
| SHA1 | `30aa9a92e8be58fdbf3b077d3fd3a6c8cbe890a0` |
| SHA256 | `1475a3bb4ec2d699b19fcc965c7a133dd253fa1e7aa1aed1eb85604315f34882` |
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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality:

### Core Functionality and Purpose
The binary functions primarily as an **installer or a self-extracting archive (SFX) wrapper**. It contains several hallmarks of a setup utility designed to unpack resources, configure system environment variables, and execute post-installation tasks. 

Key indicators include the use of `advpack.dll`, `setupapi.dll`, and the presence of "Setup" related strings like `RUNPROGRAM`, `FINISHMSG`, and `INSTALLHINFSECTION`.

### Suspicious or Malicious Behaviors
While many of these behaviors are common in legitimate installers, they are also frequently utilized by malware (specifically droppers) to execute malicious payloads.

*   **Persistence/Delayed Execution:** 
    *   The code interacts with the `RunOnce` registry key (`Software\Microsoft\Windows\CurrentVersion\RunOnce`).
    *   It dynamically constructs commands involving `rundll32.exe` and a custom DLL (`advpack.dll`) to perform tasks like `DelNodeRunDLL32`. This is often used by installers to perform cleanup after a reboot or by malware to ensure a payload runs once the system restarts.
*   **Resource Extraction & Hidden Loading:** 
    *   The code uses `FindResourceA` and `LoadResource` to pull data from its own binary. It then iterates through these resources to process them. This suggests the main "payload" is hidden inside this wrapper.
    *   It utilizes `GetProcAddress` to resolve functions dynamically, a common technique to evade simple static analysis of the Import Address Table (IAT).
*   **Privilege Escalation/Check:** 
    *   The function `fcn.004018a3` uses `OpenProcessToken`, `GetTokenInformation`, and `AllocateAndInitializeSid`. This is used to check if the process has administrative privileges or specific system tokens, common in both legitimate installers (to install drivers) and malware (to gain higher permissions).
*   **File Manipulation & Cleanup:** 
    *   The function `fcn.00402390` iterates through a directory (`FindFirstFileA`/`FindNextFileA`), changes file attributes to "Hidden" or "System," and deletes them via `DeleteFileA`. This is typical for cleaning up temporary files after extraction, but it can also be used to remove traces of an installation.
*   **Environment Manipulation:** 
    *   The code extensively uses `GetTempPathA`, `CreateDirectoryA`, and `SetCurrentDirectoryA` to manage where data is staged before execution.

### Notable Techniques or Patterns
*   **Installer-Style Wrapper:** The complexity of the logic (handling `Installation` flags, `Firmware` checks, etc.) suggests a sophisticated installation routine.
*   **Dynamic Execution:** The use of `CreateProcessA` combined with `WaitForSingleObject` and `GetExitCodeProcess` indicates that this program is designed to launch other executables or scripts as part of its workflow.
*   **Anti-Analysis/Obfuscation Signs:** 
    *   While not a high-level "packer," the heavy use of `LoadResource` and dynamic API resolution indicates an attempt to keep the actual functionality hidden from simple scanners.
    *   The use of `SetFileAttributesA(..., 0x80)` specifically targets making files invisible to the average user, which can be a "grey" technique used for both legitimate software deployment and hiding malware components.

### Summary Table
| Feature | Observation | Significance |
| :--- | :--- | :--- |
| **Persistence** | `RunOnce` Registry Keys | Used for delayed/post-reboot execution (Common in Installers/Droppers). |
| **Injection** | `rundll32.exe ... advpack.dll` | Execution of arbitrary DLL functions via system host. |
| **Evasion** | `GetProcAddress` & `LoadResource` | Hides the primary functionality within a wrapper. |
| **Privilege Check** | `OpenProcessToken` / `GetTokenInformation` | Verifies if the process has "Elevated" rights. |
| **File Manipulation**| `DeleteFileA` + `SetFileAttributes` | Cleans up temporary artifacts or hides files on disk. |

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided analysis to the relevant MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1546.003** | Registry Run Keys / Startup Folder | The binary interacts with the `RunOnce` registry key to ensure execution of commands (like `rundll32`) after a system restart. |
| **T1218** | System Binary Proxy Execution | The use of `rundll32.exe` to load and execute a custom DLL (`advpack.dll`) is a common method to masquerade malicious actions as legitimate system processes. |
| **T1027** | Obfuscated Files or Information | The use of `FindResource` and `LoadResource` indicates that the primary payload is hidden within the resources of the wrapper binary. |
| **T1106** | Native API | The use of `GetProcAddress` to resolve functions dynamically helps the binary evade static analysis by hiding its intended capabilities from the Import Address Table (IAT). |
| **T1068** | Exploitation for Privilege Escalation | The check for administrative privileges using `OpenProcessToken` and `GetTokenInformation` is a precursor to escalating privileges or performing system-level changes. |
| **T1070** | Indicator Removal on Host | The use of `SetFileAttributes` (Hidden/System) and `DeleteFileA` is used to hide artifacts from the user and remove evidence of its operation after completion. |
| **T1059** | Command and Scripting Interpreter | The use of `CreateProcessA` to execute external components or scripts as part of a multi-stage execution chain. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Registry Key used for persistence)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Command Execution Pattern:** `rundll32.exe %sadvpack.dll,DelNodeRunDLL32 "%s"` (Used to execute a specific function within a DLL via the system host).
*   **Suspicious Module Name:** `advpack.dll` (Specifically associated with the execution of the `DelNodeRunDLL32` function).
*   **Temporary File Naming Patterns:** 
    *   `IXP%03d.TMP`
    *   `msdownld.tmp`
    *   `TMP4351$.TMP`
*   **Evasion Techniques:**
    *   Use of `GetProcAddress` for dynamic API resolution (hiding the Import Address Table).
    *   Use of `SetFileAttributesA(..., 0x80)` to modify file attributes to "Hidden" or "System" status.
*   **Persistence/Staging:** Use of `GetTempPathA`, `CreateDirectoryA`, and `SetCurrentDirectoryA` for staging data before execution.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**:
* **Wrapper Functionality:** The binary exhibits all characteristics of a "wrapper" or "stub," using `FindResource`, `LoadResource`, and dynamic API resolution (`GetProcAddress`) to conceal the primary payload within its own resources, a classic indicator of a dropper/loader.
* **Evasive Execution Techniques:** The use of `rundll32.exe` to call functions in a custom DLL (`advpack.dll`), combined with `RunOnce` registry keys and attribute manipulation (setting files to "Hidden" or "System"), indicates an intent to execute hidden payloads while minimizing the footprint left on the system.
* **Artifact Cleanup:** The presence of automated routines to delete temporary files and hide artifacts immediately after execution is a hallmark of malicious droppers designed to facilitate multi-stage infections.
