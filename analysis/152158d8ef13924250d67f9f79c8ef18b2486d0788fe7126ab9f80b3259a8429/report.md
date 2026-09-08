# Threat Analysis Report

**Generated:** 2026-09-06 19:11 UTC
**Sample:** `152158d8ef13924250d67f9f79c8ef18b2486d0788fe7126ab9f80b3259a8429_152158d8ef13924250d67f9f79c8ef18b2486d0788fe7126ab9f80b3259a8429.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `152158d8ef13924250d67f9f79c8ef18b2486d0788fe7126ab9f80b3259a8429_152158d8ef13924250d67f9f79c8ef18b2486d0788fe7126ab9f80b3259a8429.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 5 sections |
| Size | 9,453,608 bytes |
| MD5 | `0d51eae91a22764674c0ab32616bb832` |
| SHA1 | `7ea2f1d0b9396698e654eedaecd5db34ee59ac72` |
| SHA256 | `152158d8ef13924250d67f9f79c8ef18b2486d0788fe7126ab9f80b3259a8429` |
| Overall entropy | 2.703 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1605256119 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.302 | No |
| `.data` | 512 | 4.971 | No |
| `.idata` | 4,608 | 5.022 | No |
| `.rsrc` | 9,403,392 | 2.668 | No |
| `.reloc` | 2,560 | 6.274 | No |

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

Total strings found: **3699** (showing first 100)

```
!This program cannot be run in DOS mode.
$
(Rich
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
RSDSE>
u@G= 70
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
u@G= 70
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
jXhhr@
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00405c50` | `0x405c50` | 1406 | ✓ |
| `fcn.00403b8e` | `0x403b8e` | 1101 | ✓ |
| `fcn.00401b04` | `0x401b04` | 957 | ✓ |
| `fcn.004036dc` | `0x4036dc` | 847 | ✓ |
| `fcn.0040555a` | `0x40555a` | 806 | ✓ |
| `fcn.00405933` | `0x405933` | 664 | ✓ |
| `fcn.00402ca1` | `0x402ca1` | 623 | ✓ |
| `fcn.00402033` | `0x402033` | 571 | ✓ |
| `entry0` | `0x406a00` | 489 | ✓ |
| `fcn.00404495` | `0x404495` | 468 | ✓ |
| `fcn.00404204` | `0x404204` | 426 | ✓ |
| `fcn.004028e3` | `0x4028e3` | 415 | ✓ |
| `fcn.00402f10` | `0x402f10` | 410 | ✓ |
| `fcn.00404fa0` | `0x404fa0` | 388 | ✓ |
| `fcn.00402770` | `0x402770` | 371 | ✓ |
| `fcn.00402395` | `0x402395` | 336 | ✓ |
| `fcn.00402aa5` | `0x402aa5` | 333 | ✓ |
| `fcn.00405423` | `0x405423` | 311 | ✓ |
| `fcn.004018c1` | `0x4018c1` | 308 | ✓ |
| `fcn.004067cb` | `0x4067cb` | 305 | ✓ |
| `fcn.00403fdb` | `0x403fdb` | 298 | ✓ |
| `fcn.0040226e` | `0x40226e` | 295 | ✓ |
| `fcn.00406cba` | `0x406cba` | 270 | ✓ |
| `fcn.00405276` | `0x405276` | 233 | ✓ |
| `fcn.004043ae` | `0x4043ae` | 231 | ✓ |
| `fcn.00403a2b` | `0x403a2b` | 231 | ✓ |
| `fcn.0040268a` | `0x40268a` | 230 | ✓ |
| `fcn.00406246` | `0x406246` | 228 | ✓ |
| `fcn.004051a5` | `0x4051a5` | 209 | ✓ |
| `fcn.00404ecb` | `0x404ecb` | 203 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004018c1.c`](code/fcn.004018c1.c)
- [`code/fcn.00401b04.c`](code/fcn.00401b04.c)
- [`code/fcn.00402033.c`](code/fcn.00402033.c)
- [`code/fcn.0040226e.c`](code/fcn.0040226e.c)
- [`code/fcn.00402395.c`](code/fcn.00402395.c)
- [`code/fcn.0040268a.c`](code/fcn.0040268a.c)
- [`code/fcn.00402770.c`](code/fcn.00402770.c)
- [`code/fcn.004028e3.c`](code/fcn.004028e3.c)
- [`code/fcn.00402aa5.c`](code/fcn.00402aa5.c)
- [`code/fcn.00402ca1.c`](code/fcn.00402ca1.c)
- [`code/fcn.00402f10.c`](code/fcn.00402f10.c)
- [`code/fcn.004036dc.c`](code/fcn.004036dc.c)
- [`code/fcn.00403a2b.c`](code/fcn.00403a2b.c)
- [`code/fcn.00403b8e.c`](code/fcn.00403b8e.c)
- [`code/fcn.00403fdb.c`](code/fcn.00403fdb.c)
- [`code/fcn.00404204.c`](code/fcn.00404204.c)
- [`code/fcn.004043ae.c`](code/fcn.004043ae.c)
- [`code/fcn.00404495.c`](code/fcn.00404495.c)
- [`code/fcn.00404ecb.c`](code/fcn.00404ecb.c)
- [`code/fcn.00404fa0.c`](code/fcn.00404fa0.c)
- [`code/fcn.004051a5.c`](code/fcn.004051a5.c)
- [`code/fcn.00405276.c`](code/fcn.00405276.c)
- [`code/fcn.00405423.c`](code/fcn.00405423.c)
- [`code/fcn.0040555a.c`](code/fcn.0040555a.c)
- [`code/fcn.00405933.c`](code/fcn.00405933.c)
- [`code/fcn.00405c50.c`](code/fcn.00405c50.c)
- [`code/fcn.00406246.c`](code/fcn.00406246.c)
- [`code/fcn.004067cb.c`](code/fcn.004067cb.c)
- [`code/fcn.00406cba.c`](code/fcn.00406cba.c)

## Behavioral Analysis

Based on the disassembly and strings provided, here is the analysis of the binary's behavior:

### Core Functionality
The binary functions as a **downloader or installer (dropper)**. It utilizes standard Windows installation routines to extract resources, verify system environment requirements, and manage file systems. The presence of "setup" naming conventions in strings (`setupx.dll`, `advpack.dll`) and the usage of Installer-specific APIs suggest it is designed to "set up" a program or payload on the host machine.

### Suspicious/Malicious Behaviors
While many of these behaviors are common in legitimate installers, their combination (particularly the automation of cleanup and staging) is highly characteristic of **malware droppers**.

*   **Persistence via Registry Manipulation:**
    *   The code specifically targets the `RunOnce` registry key: `Software\Microsoft\Windows\CurrentVersion\RunOnce`. 
    *   It checks for and creates keys to run commands automatically during the next boot or login. It specifically looks for a cleanup task (`wextract_cleanup%d`) and uses `rundll32.exe` to execute functions within `advpack.dll` (e.g., `DelNodeRunDLL32`).
*   **Staging and Command Execution:**
    *   The binary frequently constructs and executes commands using `rundll32.exe`. This is a common technique to execute malicious code under the guise of a legitimate system utility.
    *   It uses `CreateProcessA` and `GetExitCodeProcess` (in `fcn.00403fdb`) to launch other processes and wait for them to complete, which is a classic "dropper" behavior where one executable launches another hidden component.
*   **File Manipulation & Cleanup:**
    *   The function `fcn.00402395` iterates through files, changes their attributes (potentially making them hidden or system files using `SetFileAttributesA`), and deletes them (`DeleteFileA`). This is often used by malware to "clean up" the installer components after a malicious payload has been successfully deployed.
    *   It performs extensive path validation and directory creation (e.g., `CreateDirectoryA`) in temporary and system folders.
*   **Resource Loading & Processing:**
    *   The binary spends significant logic extracting and loading internal resources (`FindResourceA`, `LoadResource`). This indicates that the "payload" is likely embedded within this executable as a resource and unpacked during execution.

### Notable Techniques or Patterns
*   **Installer Mimicry:** The code heavily mimics the behavior of an Installer (using `advpack.dll` for "Advanced Package" logic, checking disk space via `GetDiskFreeSpaceA`, and utilizing `Cabinet.dll` logic). This is a common tactic to blend in with legitimate system activity.
*   **Dynamic Execution Path:** The usage of `rundll32.exe %sadvpack.dll,...` indicates a modular approach where the core malicious functionality may reside in an external DLL, while this binary acts as the primary loader/installer.
*   **Environment Validation:** It performs checks on OS version and system information (`GetVersionExA`, `GetSystemInfo`) to ensure the environment is compatible with the payload before proceeding.

### Summary of Risk
This sample exhibits behavior consistent with a **multi-stage dropper**. It manages the "installation" of a secondary component, ensures persistence via the `RunOnce` registry key, and performs automated cleanup of its own files to evade detection after the primary infection occurs.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys | The binary modifies the `RunOnce` registry key to ensure specific commands are automatically executed upon system login. |
| T1218 | Signed Binary Proxy Execution | The use of `rundll32.exe` to execute functions within an external DLL is used to mask malicious actions as legitimate system activity. |
| T1070.004 | File Deletion | The binary uses `DeleteFileA` and `SetFileAttributesA` to remove installer components and delete evidence after the payload has been deployed. |
| T1036 | Masquerading | The binary mimics standard Windows installer behavior and naming conventions (e.g., "advpack", "setup") to blend in with legitimate system processes. |
| T1106 | Native Code Execution | The use of `CreateProcessA` to launch subsequent components identifies the binary's role as a loader or dropper for secondary payloads. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Persistence mechanism)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None provided in the source text)*

**Other artifacts**
*   **Command Line Patterns:** 
    *   `rundll32.exe %sadvpack.dll,DelNodeRunDLL32 "%s"` (Used for cleanup and persistence)
    *   `rundll32.exe %s,InstallHinfSection %s 128 %s`
*   **Specific Filenames/Strings related to execution:**
    *   `wextract_cleanup%d` (Indicates specific cleanup logic used by the dropper)
    *   `wininit.ini` (Potential configuration file)
*   **Temporary File Patterns:** 
    *   `IQX%03d.TMP`
    *   `msdownld.tmp`
    *   `TMP4351$.TMP`
*   **Suspicious Function Calls/Logic:**
    *   `DelNodeRunDLL32` (Identified in behavioral analysis as a component of the cleanup routine)

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**:
    * **Multi-stage Execution and Staging:** The binary utilizes a "loader" architecture where it extracts embedded resources and uses `rundll32.exe` to execute functions within secondary DLLs (like `advpack.dll`), a classic technique for dropping and executing malicious payloads while masquerading as legitimate system processes.
    * **Persistence and Evasion:** The sample employs the `RunOnce` registry key for persistence and performs automated "cleanup" by changing file attributes and deleting installer components via `DeleteFileA` after deployment to minimize its forensic footprint.
    * **Installer Mimicry:** The use of standard installation naming conventions, environmental checks (OS version/system info), and resource management logic is specifically designed to blend in with legitimate Windows software installers to evade detection by both users and basic security tools.
