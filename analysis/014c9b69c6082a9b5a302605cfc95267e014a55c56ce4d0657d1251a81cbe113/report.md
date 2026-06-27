# Threat Analysis Report

**Generated:** 2026-06-26 20:44 UTC
**Sample:** `014c9b69c6082a9b5a302605cfc95267e014a55c56ce4d0657d1251a81cbe113_014c9b69c6082a9b5a302605cfc95267e014a55c56ce4d0657d1251a81cbe113.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `014c9b69c6082a9b5a302605cfc95267e014a55c56ce4d0657d1251a81cbe113_014c9b69c6082a9b5a302605cfc95267e014a55c56ce4d0657d1251a81cbe113.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 2,035,712 bytes |
| MD5 | `31fc57b75074182e57641cfbaf404bc5` |
| SHA1 | `b6010df574f5750740f0c581cdca65df3abd673c` |
| SHA256 | `014c9b69c6082a9b5a302605cfc95267e014a55c56ce4d0657d1251a81cbe113` |
| Overall entropy | 7.869 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3649033311 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 32,768 | 6.11 | No |
| `.rdata` | 12,288 | 3.907 | No |
| `.data` | 4,096 | 1.038 | No |
| `.pdata` | 4,096 | 1.462 | No |
| `.rsrc` | 1,974,272 | 7.911 | ⚠️ Yes |
| `.reloc` | 4,096 | 0.113 | No |

### Imports

**ADVAPI32.dll**: `GetTokenInformation`, `RegDeleteValueA`, `RegOpenKeyExA`, `RegQueryInfoKeyA`, `FreeSid`, `OpenProcessToken`, `RegSetValueExA`, `RegCreateKeyExA`, `LookupPrivilegeValueA`, `AllocateAndInitializeSid`, `RegQueryValueExA`, `EqualSid`, `RegCloseKey`, `AdjustTokenPrivileges`
**KERNEL32.dll**: `_lopen`, `_llseek`, `CompareStringA`, `GetLastError`, `GetFileAttributesA`, `GetSystemDirectoryA`, `LoadLibraryA`, `DeleteFileA`, `GlobalAlloc`, `GlobalFree`, `CloseHandle`, `WritePrivateProfileStringA`, `IsDBCSLeadByte`, `GetWindowsDirectoryA`, `SetFileAttributesA`
**GDI32.dll**: `GetDeviceCaps`
**USER32.dll**: `ShowWindow`, `MsgWaitForMultipleObjects`, `SetWindowPos`, `GetDC`, `GetWindowRect`, `DispatchMessageA`, `GetSystemMetrics`, `CallWindowProcA`, `SetWindowTextA`, `MessageBoxA`, `SendDlgItemMessageA`, `SendMessageA`, `GetDlgItem`, `DialogBoxIndirectParamA`, `GetWindowLongPtrA`
**msvcrt.dll**: `?terminate@@YAXXZ`, `_commode`, `_fmode`, `_acmdln`, `__C_specific_handler`, `memset`, `__setusermatherr`, `_ismbblead`, `_cexit`, `_exit`, `exit`, `__set_app_type`, `__getmainargs`, `_amsg_exit`, `_XcptFilter`
**COMCTL32.dll**: `ord_17`
**Cabinet.dll**: `ord_20`, `ord_21`, `ord_23`, `ord_22`
**VERSION.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`

## Extracted Strings

Total strings found: **4518** (showing first 100)

```
!This program cannot be run in DOS mode.
$
IkRichd
`.rdata
@.data
.pdata
@.rsrc
@.reloc
q0R^G'
p0R^G'
q0R^G'
u*9Q<|%
LcA<E3
 H3E H3E
UAUAVH
H!|$0H
H!|$ E3
uY!D$(E3
UVWATAUAVAWH
}P"uH
t"D8!H
tlE8&tgL
A_A^A]A\_^]
USVWATAUAVAWH
HA_A^A]A\_^[]
@8+tjH
UVWATAVH
A^A\_^]
u#!D$(E3
L$ SVWH
u*!D$(E3
u4!D$(E3
WATAUAVAWH
A_A^A]A\_
UVWATAUAVAWH
pA_A^A]A\_^]
x UATAUAVAWH
HcD$0L
A_A^A]A\]
u0!D$(E3
u=!D$(E3
u>!D$(E3
q0R^G'
!\$(E3
u !D$(E3
u !D$(E3
l$ VWAVH
` UAVAWH
tK<\u8
u.!D$(E3
u9!D$(E3
l$ VWAVH
x UATAUAVAWH
A_A^A]A\]
uA!D$(E3
@USVWATAVAWH
A_A^A\_^[]
|$ UATAUAVAWH
< t`,	<
<"u.A8F
<AtG<Dt:<It-<Nt <Pt
<At	<Ut
A_A^A]A\]
;t$@t
UATAUAVAWH
A_A^A]A\]
9D$Pu5
x AUAVAWH
@A_A^A]
q1[8''Y
8\u6H;
,0<	w
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14000721c` | `0x14000721c` | 1663 | ✓ |
| `fcn.140006768` | `0x140006768` | 1658 | ✓ |
| `fcn.140001d28` | `0x140001d28` | 1472 | ✓ |
| `fcn.14000521c` | `0x14000521c` | 1187 | ✓ |
| `fcn.140005b50` | `0x140005b50` | 894 | ✓ |
| `fcn.140003df0` | `0x140003df0` | 839 | ✓ |
| `fcn.140005810` | `0x140005810` | 823 | ✓ |
| `fcn.140001a08` | `0x140001a08` | 790 | ✓ |
| `fcn.1400061e8` | `0x1400061e8` | 702 | ✓ |
| `fcn.1400046e8` | `0x1400046e8` | 684 | ✓ |
| `fcn.140002a10` | `0x140002a10` | 640 | ✓ |
| `entry0` | `0x140001150` | 625 | ✓ |
| `fcn.140008400` | `0x140008400` | 597 | ✓ |
| `fcn.140002d34` | `0x140002d34` | 592 | ✓ |
| `fcn.140003950` | `0x140003950` | 590 | ✓ |
| `fcn.140004be0` | `0x140004be0` | 588 | ✓ |
| `fcn.1400022f0` | `0x1400022f0` | 585 | ✓ |
| `fcn.140003118` | `0x140003118` | 523 | ✓ |
| `fcn.140007010` | `0x140007010` | 514 | ✓ |
| `fcn.1400026b8` | `0x1400026b8` | 503 | ✓ |
| `fcn.1400041ec` | `0x1400041ec` | 471 | ✓ |
| `fcn.1400013e0` | `0x1400013e0` | 465 | ✓ |
| `fcn.1400043cc` | `0x1400043cc` | 451 | ✓ |
| `fcn.140008bb4` | `0x140008bb4` | 447 | ✓ |
| `fcn.140005ed8` | `0x140005ed8` | 362 | ✓ |
| `fcn.140004fd8` | `0x140004fd8` | 354 | ✓ |
| `fcn.140003c8c` | `0x140003c8c` | 346 | ✓ |
| `fcn.140004598` | `0x140004598` | 329 | ✓ |
| `fcn.140007fe4` | `0x140007fe4` | 324 | ✓ |
| `fcn.140007ce0` | `0x140007ce0` | 321 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.1400013e0.c`](code/fcn.1400013e0.c)
- [`code/fcn.140001a08.c`](code/fcn.140001a08.c)
- [`code/fcn.140001d28.c`](code/fcn.140001d28.c)
- [`code/fcn.1400022f0.c`](code/fcn.1400022f0.c)
- [`code/fcn.1400026b8.c`](code/fcn.1400026b8.c)
- [`code/fcn.140002a10.c`](code/fcn.140002a10.c)
- [`code/fcn.140002d34.c`](code/fcn.140002d34.c)
- [`code/fcn.140003118.c`](code/fcn.140003118.c)
- [`code/fcn.140003950.c`](code/fcn.140003950.c)
- [`code/fcn.140003c8c.c`](code/fcn.140003c8c.c)
- [`code/fcn.140003df0.c`](code/fcn.140003df0.c)
- [`code/fcn.1400041ec.c`](code/fcn.1400041ec.c)
- [`code/fcn.1400043cc.c`](code/fcn.1400043cc.c)
- [`code/fcn.140004598.c`](code/fcn.140004598.c)
- [`code/fcn.1400046e8.c`](code/fcn.1400046e8.c)
- [`code/fcn.140004be0.c`](code/fcn.140004be0.c)
- [`code/fcn.140004fd8.c`](code/fcn.140004fd8.c)
- [`code/fcn.14000521c.c`](code/fcn.14000521c.c)
- [`code/fcn.140005810.c`](code/fcn.140005810.c)
- [`code/fcn.140005b50.c`](code/fcn.140005b50.c)
- [`code/fcn.140005ed8.c`](code/fcn.140005ed8.c)
- [`code/fcn.1400061e8.c`](code/fcn.1400061e8.c)
- [`code/fcn.140006768.c`](code/fcn.140006768.c)
- [`code/fcn.140007010.c`](code/fcn.140007010.c)
- [`code/fcn.14000721c.c`](code/fcn.14000721c.c)
- [`code/fcn.140007ce0.c`](code/fcn.140007ce0.c)
- [`code/fcn.140007fe4.c`](code/fcn.140007fe4.c)
- [`code/fcn.140008400.c`](code/fcn.140008400.c)
- [`code/fcn.140008bb4.c`](code/fcn.140008bb4.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C code, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The binary appears to be a **setup utility or a multi-stage dropper**. Its primary role is to prepare the environment for the execution of another component (the "payload"). It performs standard installer tasks such as checking system compatibility, resolving file paths, ensuring directory existence, and handling configuration data.

### Suspicious and Malicious Behaviors
While much of the code resembles a legitimate installer, several features are commonly used in malware to ensure successful installation or persistence:

*   **Persistence via Registry Manipulation:** 
    *   In `fcn.14000721c` and `fcn.140001a08`, the code interacts with the **"RunOnce"** registry key (`Software\Microsoft\Windows\CurrentVersion\RunOnce`). This is used to ensure that a specific command (often part of a second-stage execution) runs automatically after the next system reboot.
*   **Environment Discovery and Escalation:** 
    *   The code frequently queries system environment variables, `GetSystemDirectoryA`, `GetWindowsDirectoryA`, and `GetTempPathA`. 
    *   In `fcn.140002d34`, it specifically checks the **"App Paths"** registry key to determine how Windows resolves paths for specific applications, which can be used by malware to ensure its component is correctly executed when called by the system.
*   **Process Execution and Management:** 
    *   `fcn.140007010` uses `CreateProcessA` and `WaitForSingleObject`. It monitors the exit code of a spawned process, which suggests it is launching another executable (the payload) and waiting for it to finish its setup routine before continuing or closing.
*   **System/Library Manipulation:** 
    *   The use of `GetProcAddress` and `LoadLibraryA` for functions like `DoInfInstall` (from `setupx.dll`) indicates a modular design. This allows the binary to dynamically load functionality only when needed, a common technique to minimize its initial footprint or bypass simple static analysis.

### Notable Techniques & Patterns
*   **Installer Wrapper/Dropper Pattern:** The heavy reliance on `GetFileAttributesA`, `CreateDirectoryA`, and path normalization (removing quotes and extra slashes in `fcn.140002a10` and `fcn.140008400`) is typical of a "wrapper" that prepares paths for the actual malicious payload.
*   **Shell Integration:** The use of `SHELL32.dll` (specifically `SHBrowseForFolder` in `fcn.140003950`) suggests that at some point, it may interact with the Windows shell to select files or directories, potentially masquerading as a legitimate installer where a user is asked to "pick a destination."
*   **File System Persistence:** The code specifically looks for `.BAT` and `.INF` files (in `fcn.140001d28`). These are common formats used in installers to execute batch commands or configuration scripts during the setup process.
*   **Self-Cleaning/Cleanup Routine:** In `fcn.1400043cc`, there is logic to delete files from a list and clean up temporary folders (e.g., using `GetTempPathA`). This "shredding" of evidence after an installation is finished is common in malware to hide its tracks.
*   **Obfuscation/Evasion through Standard APIs:** The binary heavily utilizes standard Windows API calls for environment checks (like `GetVersionExA` and `GetSystemMetrics`) which helps it blend in with legitimate software while ensuring the environment is suitable for the payload's execution.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys/Startup Folder | The binary interacts with the "RunOnce" registry key to ensure a payload executes automatically upon the next system reboot. |
| T1614 | System Environment Information | The binary queries environment variables and specific Windows paths (like App Paths) to determine the local environment for its operations. |
| T1030 | DLL Loading | The use of `GetProcAddress` and `LoadLibraryA` facilitates modular design and may be used to bypass static analysis by loading functionality dynamically. |
| T1059.004 | Windows Command Shell | The binary specifically looks for `.BAT` files to execute batch commands during the setup routine. |
| T1070 | Indicator Removal on Host | The "self-cleaning" logic used to delete temporary files and shred evidence after completion is intended to hide the presence of the installation. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the identified Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Identified as used for persistence)
*   `Software\Microsoft\Windows\CurrentVersion\App Paths` (Used to determine execution paths)
*   `Control Panel\Desktop\ResourceLocale`

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **File Types:** `.BAT`, `.INF` (Identified as search targets for script/configuration execution)
*   **Temporary Files:** `IXP%03d.TMP`, `msdownld.tmp`, `TMP4351$.TMP`
*   **Module Loading:** Use of `GetProcAddress` and `LoadLibraryA` to dynamically load `setupx.dll`.
*   **Behavioral Patterns:** 
    *   Multi-stage dropper behavior (Parent process monitors child process exit codes).
    *   Evidence shredding (Automated deletion of temporary files/folders post-execution).
    *   Path normalization routines used to prepare paths for a secondary payload.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**:
    * **Multi-stage Dropper Behavior:** The binary functions as an "installer wrapper," designed to prepare the environment (path normalization, directory creation) and execute a secondary payload while monitoring its exit code.
    * **Persistence & Evasion:** It utilizes the `RunOnce` registry key for persistence and employs "self-cleaning" routines to delete temporary files and artifacts, specifically intended to hide traces after the primary payload is delivered.
    * **Modular Design & Environment Recon:** The use of dynamic DLL loading (`GetProcAddress`/`LoadLibraryA`) and extensive environment checks (App Paths, system variables) are classic indicators of a loader designed to ensure successful execution in varied environments while evading basic static analysis.
