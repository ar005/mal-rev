# Threat Analysis Report

**Generated:** 2026-09-05 15:33 UTC
**Sample:** `148071e2c945617372ee205c023b223b40519d546d991bd3c4dbcfdf60ab70ee_148071e2c945617372ee205c023b223b40519d546d991bd3c4dbcfdf60ab70ee.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `148071e2c945617372ee205c023b223b40519d546d991bd3c4dbcfdf60ab70ee_148071e2c945617372ee205c023b223b40519d546d991bd3c4dbcfdf60ab70ee.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 1,230,336 bytes |
| MD5 | `91f73b7f9d664c04e794b2bf62de0428` |
| SHA1 | `f85fd59e09835fee3f08c786345cd6c7a01b0a08` |
| SHA256 | `148071e2c945617372ee205c023b223b40519d546d991bd3c4dbcfdf60ab70ee` |
| Overall entropy | 7.83 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1579886405 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.096 | No |
| `.rdata` | 9,216 | 4.728 | No |
| `.data` | 1,024 | 3.189 | No |
| `.pdata` | 1,536 | 3.156 | No |
| `.rsrc` | 1,185,280 | 7.865 | ⚠️ Yes |
| `.reloc` | 512 | 0.407 | No |

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

Total strings found: **2727** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
L$ SVWH
@8+tjH
UVWATAUAVAWH
}P"uH
t"D8)H
tmD8.thL
A_A^A]A\_^]
u#!D$(E3
UAUAVH
L!t$0H
D!t$ H
L!t$ E3
uY!D$(E3
UVWAVAWH
A_A^_^]
USVWATAUAVAWH
HA_A^A]A\_^[]
\$ VWAWH
<EuBH;
u-!|$(E3
u!|$(E3
!|$(E3
|$ AWH
u>!D$(E3
x UATAUAVAWH
u-A9]|
A_A^A]A\]
u0!D$(E3
u=!D$(E3
UATAUAVAWH
A_A^A]A\]
u !D$(E3
WATAUAVAWH
A_A^A]A\_
UVWATAUAVAWH
pA_A^A]A\_^]
@USVWATAVAWH
A_A^A\_^[]
u*!D$(E3
u4!D$(E3
x AUAVAWH
@A_A^A]
x UAVAWH
9D$Pu5
!\$(E3
u !D$(E3
u.!D$(E3
u9!D$(E3
` UAVAWH
tK<\u8
uA!D$(E3
x UATAUAVAWH
A_A^A]A\]
|$ UATAUAVAWH
< t`,	<
<"u.A8F
<AtG<Dt:<It-<Nt <Pt
<At	<Ut
A_A^A]A\]
;t$@t
8\u6H;
,0<	w
u*9Q<|%
LcA<E3
u HcA<H
 H3E H3E
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400040c4` | `0x1400040c4` | 1648 | ✓ |
| `fcn.1400070a8` | `0x1400070a8` | 1615 | ✓ |
| `fcn.140001684` | `0x140001684` | 1408 | ✓ |
| `fcn.1400066c4` | `0x1400066c4` | 1187 | ✓ |
| `fcn.140003bf4` | `0x140003bf4` | 887 | ✓ |
| `fcn.140006ca4` | `0x140006ca4` | 887 | ✓ |
| `fcn.140002db4` | `0x140002db4` | 816 | ✓ |
| `fcn.140001d28` | `0x140001d28` | 797 | ✓ |
| `fcn.1400030ec` | `0x1400030ec` | 678 | ✓ |
| `fcn.140004dcc` | `0x140004dcc` | 635 | ✓ |
| `entry0` | `0x140008200` | 602 | ✓ |
| `fcn.140005380` | `0x140005380` | 597 | ✓ |
| `fcn.140005d90` | `0x140005d90` | 588 | ✓ |
| `fcn.140002834` | `0x140002834` | 560 | ✓ |
| `fcn.14000261c` | `0x14000261c` | 527 | ✓ |
| `fcn.1400012ec` | `0x1400012ec` | 523 | ✓ |
| `fcn.14000473c` | `0x14000473c` | 518 | ✓ |
| `fcn.140004a60` | `0x140004a60` | 511 | ✓ |
| `fcn.14000204c` | `0x14000204c` | 494 | ✓ |
| `fcn.140002a6c` | `0x140002a6c` | 479 | ✓ |
| `fcn.1400064e4` | `0x1400064e4` | 473 | ✓ |
| `fcn.140008470` | `0x140008470` | 465 | ✓ |
| `fcn.1400061ec` | `0x1400061ec` | 451 | ✓ |
| `fcn.140007f04` | `0x140007f04` | 447 | ✓ |
| `fcn.140004c68` | `0x140004c68` | 346 | ✓ |
| `fcn.140002c54` | `0x140002c54` | 345 | ✓ |
| `fcn.140003f74` | `0x140003f74` | 329 | ✓ |
| `fcn.140002318` | `0x140002318` | 326 | ✓ |
| `fcn.140005b18` | `0x140005b18` | 321 | ✓ |
| `fcn.1400060a4` | `0x1400060a4` | 318 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.1400012ec.c`](code/fcn.1400012ec.c)
- [`code/fcn.140001684.c`](code/fcn.140001684.c)
- [`code/fcn.140001d28.c`](code/fcn.140001d28.c)
- [`code/fcn.14000204c.c`](code/fcn.14000204c.c)
- [`code/fcn.140002318.c`](code/fcn.140002318.c)
- [`code/fcn.14000261c.c`](code/fcn.14000261c.c)
- [`code/fcn.140002834.c`](code/fcn.140002834.c)
- [`code/fcn.140002a6c.c`](code/fcn.140002a6c.c)
- [`code/fcn.140002c54.c`](code/fcn.140002c54.c)
- [`code/fcn.140002db4.c`](code/fcn.140002db4.c)
- [`code/fcn.1400030ec.c`](code/fcn.1400030ec.c)
- [`code/fcn.140003bf4.c`](code/fcn.140003bf4.c)
- [`code/fcn.140003f74.c`](code/fcn.140003f74.c)
- [`code/fcn.1400040c4.c`](code/fcn.1400040c4.c)
- [`code/fcn.14000473c.c`](code/fcn.14000473c.c)
- [`code/fcn.140004a60.c`](code/fcn.140004a60.c)
- [`code/fcn.140004c68.c`](code/fcn.140004c68.c)
- [`code/fcn.140004dcc.c`](code/fcn.140004dcc.c)
- [`code/fcn.140005380.c`](code/fcn.140005380.c)
- [`code/fcn.140005b18.c`](code/fcn.140005b18.c)
- [`code/fcn.140005d90.c`](code/fcn.140005d90.c)
- [`code/fcn.1400060a4.c`](code/fcn.1400060a4.c)
- [`code/fcn.1400061ec.c`](code/fcn.1400061ec.c)
- [`code/fcn.1400064e4.c`](code/fcn.1400064e4.c)
- [`code/fcn.1400066c4.c`](code/fcn.1400066c4.c)
- [`code/fcn.140006ca4.c`](code/fcn.140006ca4.c)
- [`code/fcn.1400070a8.c`](code/fcn.1400070a8.c)
- [`code/fcn.140007f04.c`](code/fcn.140007f04.c)
- [`code/fcn.140008470.c`](code/fcn.140008470.c)

## Behavioral Analysis

This is an analysis of the provided binary disassembly and decompiled C code.

### Core Functionality
The binary functions as a **sophisticated installer or "dropper" component**. Its primary purpose is to prepare an environment, verify system capabilities, perform complex path/string normalization, and ensure persistence on the host system. It performs several stages of internal configuration before executing tasks that likely involve installing additional components or payloads.

### Suspicious or Malicious Behaviors

*   **Persistence via Registry Manipulation:**
    *   The code specifically interacts with `Software\Microsoft\Windows\CurrentVersion\RunOnce`. This is a common technique used by both legitimate installers and malware to ensure a command or program is executed automatically the next time a user logs in.
    *   It utilizes `RegSetValueExA` to write paths into this key, suggesting it is scheduling its own restart or a secondary payload for execution.

*   **Privileged System Manipulation:**
    *   The function `fcn.140002318` accesses high-privilege registry keys:
        *   `Session Manager\FileRenameOperations`
        *   `Session Manager\PendingFileRenameOperations`
    *   These keys are used by the Windows boot process to handle file moves/renames (common during system updates or driver installations). Malware often leverages these specific keys to perform "file shadowing" or to ensure that a malicious file is moved into a protected location during a reboot.

*   **Environment & Capability Checking:**
    *   The code performs extensive checks on the OS version, hardware architecture (x86 vs. x64), and system capabilities (e.g., `DoInfInstall`). 
    *   It checks for available disk space (`GetDiskFreeSpaceA`) and validates volume information before proceeding with file operations.

*   **Recursive File System Processing:**
    *   The function `fcn.14000204c` implements a loop to find, rename, or delete files in the local directory based on specific string comparisons (e.g., checking for filenames ending in `.bat`, `.inf`, or those matching internal constants). This is common "cleanup" behavior in installers but is also used by droppers to remove evidence of other tools or their own previous execution stages.

*   **String/Path Normalization:**
    *   The function `fcn.1400070a8` contains a complex loop to parse and normalize file paths, handling environment variables (like `%SystemRoot%`), drive letters (`C:\`), and quoted paths. This ensures the binary can operate correctly regardless of where it is executed or how its path is typed in the command line.

### Notable Techniques & Patterns

*   **Dynamic API Resolution:** The code frequently uses `GetProcAddress` and `GetModule_HandleA` to find functions (like `DelNodeRunDLL32`) at runtime, which helps evade simple static analysis of the Import Address Table (IAT).
*   **Standard Installer Logic (Wrapper):** Much of the logic appears designed to mimic a standard Windows installer. It uses `Cabinet.dll` (`FDICreate`, `FDICopy`), which is a legacy but common way to extract and copy files from an embedded resource into the file system.
*   **Anti-Analysis/Robustness:** The repeated use of "fallbacks" (e.g., if one method for finding a path fails, it tries another) suggests the code is designed to be highly robust, ensuring that even in restricted environments, it can still successfully locate and install its components.

### Summary of Key Indicators
*   **Persistence:** Manipulation of `RunOnce` registry keys.
*   **Privileged Action:** Engagement with `PendingFileRenameOperations`.
*   **System Manipulation:** Use of `DelNodeRunDLL32` to manipulate system-level execution items.
*   **Advanced File Management:** Complex logic for directory creation, file deletion, and path normalization.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | The binary explicitly modifies the `RunOnce` registry key to ensure execution of a payload upon the next user login. |
| **T1543** | Create or Modify System Process | By interacting with `PendingFileRenameOperations`, the malware seeks to manipulate system-level file replacement to gain persistence at a high privilege level during boot. |
| **T1106** | Native API | The use of `GetProcAddress` and `GetModule_HandleA` for dynamic API resolution is used to hide the intended functionality from static analysis of the Import Address Table (IAT). |
| **T1488** | System Information Discovery | The extensive checks for OS version, hardware architecture, and disk space are performed to profile the target system before executing potentially malicious payloads. |
| **T1070** | Indicator Removal on Host | The routine that identifies and deletes specific file types (e.g., .bat, .inf) suggests an attempt to clean up evidence or artifacts left during the installation process. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Used for persistence)
*   `Session Manager\FileRenameOperations` (Utilized for "file shadowing" and privileged manipulation)
*   `Session Manager\PendingFileRenameOperations` (Utilized for "file shadowing" and privileged manipulation)
*   `wininit.ini` (Specific configuration file identifier)
*   `IXP%03d.TMP`, `msdownld.tmp`, `TMP4351$.TMP` (Potential dropped files or staging artifacts)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **DelNodeRunDLL32**: A specific utility/method used to manipulate system-level execution items and registry keys.
*   **Dropped File Patterns**: The presence of multiple `.TMP` files with varying prefixes suggests a multi-stage dropper or installer mechanism.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Persistence and System Manipulation:** The binary utilizes `RunOnce` registry keys and `PendingFileRenameOperations` to ensure execution across reboots and perform "file shadowing" (replacing system-level files), which are hallmarks of sophisticated droppers seeking persistence.
    *   **Evasion Tactics:** The use of dynamic API resolution (`GetProcAddress`, `GetModule_HandleA`) to hide functionality from static analysis, combined with a self-cleaning routine that deletes `.bat` and `.inf` files, indicates an intentional effort to hide the malware's footprint.
    *   **Staged Execution Architecture:** The reliance on `Cabinet.dll` for resource extraction and the creation of multiple `.TMP` staged files indicate it is designed to unpack and install secondary payloads in a multi-stage process.
