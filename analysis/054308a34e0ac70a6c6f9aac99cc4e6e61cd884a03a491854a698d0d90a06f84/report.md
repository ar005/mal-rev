# Threat Analysis Report

**Generated:** 2026-07-13 13:52 UTC
**Sample:** `054308a34e0ac70a6c6f9aac99cc4e6e61cd884a03a491854a698d0d90a06f84_054308a34e0ac70a6c6f9aac99cc4e6e61cd884a03a491854a698d0d90a06f84.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `054308a34e0ac70a6c6f9aac99cc4e6e61cd884a03a491854a698d0d90a06f84_054308a34e0ac70a6c6f9aac99cc4e6e61cd884a03a491854a698d0d90a06f84.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 5 sections |
| Size | 2,292,224 bytes |
| MD5 | `1ec0f7a930ac0c3a8f983bca474042e0` |
| SHA1 | `d140f73b4be36fe9a5007de443efb20821243115` |
| SHA256 | `054308a34e0ac70a6c6f9aac99cc4e6e61cd884a03a491854a698d0d90a06f84` |
| Overall entropy | 4.83 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1605472930 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.302 | No |
| `.data` | 512 | 4.971 | No |
| `.idata` | 4,608 | 5.022 | No |
| `.rsrc` | 1,104,384 | 7.947 | ⚠️ Yes |
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

Total strings found: **2827** (showing first 100)

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

### **Malware Analysis Report**

#### **Core Functionality and Purpose**
Based on the decompiled code and string analysis, this binary appears to be a **downloader or an installer stub**. Its primary role is to prepare the system environment, verify resources, and orchestrate the execution of secondary components (specifically referencing "advpack.dll"). It handles directory creation, disk space verification, and registry manipulation to facilitate the installation of additional features or modules.

#### **Suspicious and Malicious Behaviors**
The following behaviors are noteworthy from a security perspective:

*   **Persistence/Execution via Registry:** 
    *   The code interacts with the `Software\Microsoft\Windows\CurrentVersion\RunOnce` registry key (see `fcn.00402033`). This is a common technique used by both installers and malware to ensure that specific commands (like `rundll32.exe advpack.dll,DelNodeRunDLL32`) are executed automatically during the next system login.
*   **Evasion/Stealth Tactics:** 
    *   The code explicitly sets file attributes to **Hidden** (`0x80`) before performing actions or deleting files (see `fcn.00402395`). This is a common technique used by malware to hide its "footprints" (temporary files, dropped executables) from the user and basic security monitoring tools.
*   **Automated Cleanup of Artifacts:** 
    *   The function `fcn.00402395` iterates through files in a directory using `FindFirstFileA/FindNextFileA`. If it matches specific criteria, it marks them as hidden and deletes them. This is indicative of "anti-forensics" behavior intended to scrub the system of evidence after a payload has been delivered or installed.
*   **System Environment Probing:** 
    *   The binary performs extensive checks on system versions (`GetVersionExA`), disk space, and directory availability before proceeding (see `fcn.00405933` and `fcn.00405423`). While common in legitimate installers, this is also used by malware to ensure the target environment supports its capabilities (e.g., checking for a specific Windows version).
*   **Execution of External Modules:** 
    *   The code utilizes `GetProcAddress` and `LoadLibraryA` to dynamically resolve and load functionality from external DLLs, and uses `CreateProcessA` to execute commands or secondary payloads via `rundll32.exe`.

#### **Notable Techniques & Patterns**
*   **Resource Loading:** The binary actively parses and loads resources (e.g., `fcn.00406246`). This often indicates a multi-stage loader where the initial binary is just a "wrapper" for several internal components.
*   **System Path Manipulation:** Extensive use of `GetSystemDirectoryA`, `GetTempPathA`, and `GetModuleFileNameA` suggests that the program moves, creates, or hides files in standard Windows locations to blend in with system processes.
*   **Standard DLL Hijacking/Usage Patterns:** The reliance on `rundll32.exe` to call functions inside a `.dll` (specifically via `advpack.dll`) is a common technique for malware to execute code while the process name remains a trusted Windows system utility in the task manager.

### **Summary of Key Indicators**
*   **Persistence:** `RunOnce` registry key manipulation.
*   **Stealth:** Manipulation of `FILE_ATTRIBUTE_HIDDEN` (0x80) on local files.
*   **Evasion:** Automated deletion/cleanup of "temporary" files.
*   **Potential Dropper:** Use of `CreateProcessA` and `GetProcAddress` to launch remote components.

---

## MITRE ATT&CK Mapping

Based on the behavior analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1546.003** | Registry Run Keys / Startup Folder | The malware manipulates the `RunOnce` registry key to ensure that a specific DLL is executed automatically upon the next login. |
| **T1564.001** | Hide Files and Directories | The code explicitly sets the `FILE_ATTRIBUTE_HIDDEN` attribute on files to evade detection by users and basic security monitoring tools. |
| **T1070.004** | Indicator Removal on Host: File Deletion | The malware performs automated cleanup of its own artifacts (deleting temporary files) to remove evidence of activity from the system. |
| **T1481** | System Information Discovery | The binary probes system versions and disk space to confirm that the target environment supports its requirements before proceeding. |
| **T1106** | Native API | The use of `GetProcAddress` and `LoadLibraryA` to resolve functions dynamically is used to evade static analysis and hide the true capabilities of the code. |
| **T1059.003** | Windows Command Shell / Command Interpreter | The execution of commands via `rundll32.exe` allows the malware to execute malicious code while masking its activity under a trusted system process name. |

---

## Indicators of Compromise

Based on the provided strings and behavior analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `advpack.dll` (Specifically utilized via `rundll32.exe`)
*   `msdownld.tmp` (Potential masqueraded temporary file)
*   `TMP4351$.TMP` (Specific staged filename)
*   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Used for persistence of the `advpack.dll` component)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None provided in source text)*

**Other artifacts**
*   **Execution Command Pattern:** `rundll32.exe %sadvpack.dll,DelNodeRunDLL32 "%s"` (Used to execute the specific `DelNodeRunDLL32` function).
*   **Function Name:** `DelNodeRunDLL32` (Specific routine identified in the logic for file/artifact manipulation).
*   **Anti-Forensics Behavior:** Manual setting of file attributes to `0x80` (Hidden) during the cleanup phase (`fcn.00402395`).
*   **System Manipulation:** Use of `GetProcAddress` and `LoadLibraryA` to dynamically load components, typical of multi-stage loaders.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family**: custom
2. **Malware type**: loader / dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Orchestration of Secondary Payloads:** The binary functions as an intermediary (loader/installer stub) that validates system environment variables and utilizes `rundll32.exe` to execute secondary components like `advpack.dll`.
    *   **Anti-Forensics and Evasion:** The sample exhibits clear evasion tactics, including the manual setting of file attributes to "Hidden" (`0x80`) and automated cleanup/deletion of temporary artifacts (e.g., `msdownld.tmp`) to hide its presence from investigators.
    *   **Persistence & Obfuscation:** It employs common malware persistence techniques via the `RunOnce` registry key and uses dynamic API resolution (`GetProcAddress`/`LoadLibraryA`) to mask its true capabilities during initial analysis.
