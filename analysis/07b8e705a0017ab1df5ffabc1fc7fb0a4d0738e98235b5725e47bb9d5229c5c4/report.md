# Threat Analysis Report

**Generated:** 2026-07-17 18:12 UTC
**Sample:** `07b8e705a0017ab1df5ffabc1fc7fb0a4d0738e98235b5725e47bb9d5229c5c4_07b8e705a0017ab1df5ffabc1fc7fb0a4d0738e98235b5725e47bb9d5229c5c4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07b8e705a0017ab1df5ffabc1fc7fb0a4d0738e98235b5725e47bb9d5229c5c4_07b8e705a0017ab1df5ffabc1fc7fb0a4d0738e98235b5725e47bb9d5229c5c4.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 5 sections |
| Size | 31,720,900 bytes |
| MD5 | `600e1b59222ec1bf5d83f62a7cc0b9cc` |
| SHA1 | `9497cb3a673c53c4c45db85818326e675e9d928f` |
| SHA256 | `07b8e705a0017ab1df5ffabc1fc7fb0a4d0738e98235b5725e47bb9d5229c5c4` |
| Overall entropy | 6.739 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1469423715 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.302 | No |
| `.data` | 512 | 4.971 | No |
| `.idata` | 4,608 | 5.022 | No |
| `.rsrc` | 1,275,904 | 7.942 | ⚠️ Yes |
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

Total strings found: **93798** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The sample appears to be a **dropper or an installer-style packer**. Its primary role is to prepare the system environment for the execution of secondary components, manage resources (likely extracting them from its own binary), and ensure that subsequent "cleanup" or "initialization" tasks are scheduled.

### Suspicious and Malicious Behaviors
The following behaviors are highly indicative of malicious intent or functionality common in high-risk software:

*   **Persistence via `RunOnce` Registry Keys:** 
    *   Functions `fcn.00402033` and `fcn.0040226e` both target the `Software\Microsoft\Windows\CurrentVersion\RunOnce` key. 
    *   The binary writes entries using `rundll32.exe` to call functions in a DLL (e.g., `advpack.dll,DelNodeRunDLL32`). While common in installers, this is frequently used by malware to ensure that "cleanup" scripts or subsequent stages of an infection run automatically upon the next login or reboot.
*   **Privilege and Token Analysis:** 
    *   Function `fcn.004018c1` uses `OpenProcessToken`, `GetTokenInformation`, and `AllocateAndInitializeSid`. It iterates through SIDs to check for specific privileges. This suggests the malware is checking if it has administrative rights or high-level system permissions before attempting more intrusive actions.
*   **Dynamic Execution and Loading:** 
    *   The code frequently uses `GetProcAddress` and `LoadLibraryA`. It also uses `CreateProcessA` (fcn.00403fdb) to spawn new processes with specific flags. This technique is used to execute payloads hidden within the binary or to transition execution to a different process to evade detection.
*   **Resource Extraction:** 
    *   The use of `Cabinet.dll` (Shell) functions like `FDICreate` and `FDICopy` (fcn.00404fa0, fcn.00404ecb) suggests the binary is designed to unpack or extract resources from its internal data section. This is a standard technique for "packing" malware to hide its primary payload.
*   **Environment and Anti-Analysis Checks:** 
    *   Function `fcn.004036dc` performs detailed checks on Windows Versioning (`GetVersionExA`) and system capabilities. This may be used as a primitive "anti-sandbox" or "compatibility" check to ensure the malware is running on a target victim's machine rather than an analysis environment.
    *   Function `fcn.00405933` checks disk space via `GetDiskFreeSpaceA`, likely to ensure enough room exists for dropped files/payloads.

### Notable Techniques and Patterns
*   **Use of System Binaries:** The code heavily utilizes `rundll32.exe` and known system DLLs (`advpack.dll`, `shell32.dll`) to perform actions, which helps the malware blend in with standard OS behavior.
*   **Path Obfuscation/Normalization:** Function `fcn.00405c50` contains logic to parse and normalize file paths (handling quotes, backslashes, and different drive letters). This is common when a tool needs to handle inputs from the user or system environment reliably.
*   **Delayed Execution/Persistence:** By setting up tasks in `RunOnce`, the malware can delay its most "noisy" activities until after a reboot, making it harder for real-time analysis tools to catch the full chain of execution.
*   **Decoupled Logic:** The presence of various "cleanup" functions (e.g., `fcn.00402395` which deletes files and removes directories) suggests the binary is designed to clean up its traces or prepare a directory for more permanent installation.

### Summary Table
| Behavior Category | Specific Observation | Potential Risk |
| :--- | :--- | :--- |
| **Persistence** | Writing to `RunOnce` Registry keys via `rundll32.exe`. | Ensures execution of components after reboot/login. |
| **Privilege Escalation** | Analyzing process tokens and SIDs (fcn.004018c1). | Checking for admin rights before performing malicious acts. |
| **Payload Delivery** | Extraction via Cabinet APIs and `CreateProcessA`. | Hiding the primary malware payload inside an encrypted/packed file. |
| **Evasion** | Version checks and environmental queries (fcn.004036dc). | Avoiding execution in automated sandboxes or non-target systems. |

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Registry Run Keys / Startup Folder | The binary writes to the `RunOnce` registry key to ensure that secondary components or "cleanup" tasks execute automatically upon the next login/reboot. |
| T1106 | Dynamic Resolution | The frequent use of `GetProcAddress` and `LoadLibraryA` indicates a technique to resolve API addresses at runtime to evade static analysis. |
| T1218 | System Binary Proxy Execution | The heavy reliance on `rundll32.exe` and standard system DLLs (e.g., `shell32.dll`) is used to mask malicious activity as legitimate OS behavior. |
| T1036 | System Information Discovery | The analysis of SIDs, Windows versions, and disk space is performed to identify the environment and detect if it is an analysis sandbox. |
| T1027 | Obfuscated Files | The use of `Cabinet.dll` (Shell) functions like `FDICreate` and `FDICopy` indicates a method for extracting hidden payloads from within the binary's internal data section. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   (None identified)

**File paths / Registry keys**
*   `Software\Microsoft\RunOnce` (Identified as a mechanism for persistence via `rundll32.exe`)
*   `System\CurrentControlSet\Control\Session Manager\FileRenameOperations`
*   `wininit.ini` (Potential configuration file)

**Mutex names / Named pipes**
*   (None identified)

**Hashes**
*   (None provided in the source text)

**Other artifacts**
*   **Dropped/Temporary Files:**
    *   `msdownld.tmp`
    *   `TMP4351$.TMP`
    *   `IXP%03d.TMP`
    *   `wextract_cleanup%d` (Dynamic filename used for cleanup)
*   **Function Calls/Specific Commands:**
    *   `DelNodeRunDLL32` (Called via `advpack.dll`)
    *   `InstallHinfSection` (Used with `rundll32.exe`)
*   **Suspicious Behavior Patterns:**
    *   Use of `rundll32.exe` to execute functions within `advpack.dll`.
    *   Execution of `Cabinet.dll` functions (`FDICreate`, `FDICopy`) for resource extraction/unpacking.

---

## Malware Family Classification

1. **Malware family**: Unknown (Generic Loader)
2. **Malware type**: Dropper / Loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Resource Extraction & Unpacking:** The use of `Cabinet.dll` functions (`FDICreate`, `FDICopy`) combined with dynamic execution via `CreateProcessA` indicates the primary purpose is to extract and execute a hidden payload from its own binary.
    *   **Persistence and Obfuscation:** The malware utilizes `RunOnce` registry keys, dynamic API resolution (`GetProcAddress`), and system binary proxying (`rundll32.exe`) to maintain persistence while masking its activity as standard OS behavior.
    *   **Evasion Tactics:** The inclusion of environment-aware checks (Windows Versioning, Disk Space) and privilege verification suggests a deliberate attempt to detect sandboxes or non-target systems before deploying the final payload.
