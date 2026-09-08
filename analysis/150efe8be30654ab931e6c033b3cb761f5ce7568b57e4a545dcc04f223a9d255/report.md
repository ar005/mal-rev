# Threat Analysis Report

**Generated:** 2026-09-06 18:36 UTC
**Sample:** `150efe8be30654ab931e6c033b3cb761f5ce7568b57e4a545dcc04f223a9d255_150efe8be30654ab931e6c033b3cb761f5ce7568b57e4a545dcc04f223a9d255.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `150efe8be30654ab931e6c033b3cb761f5ce7568b57e4a545dcc04f223a9d255_150efe8be30654ab931e6c033b3cb761f5ce7568b57e4a545dcc04f223a9d255.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 94,720 bytes |
| MD5 | `74da44472379b4f7d0b0f0ab568f5bb6` |
| SHA1 | `0036f6ce07ca2d09e1a1972ea07ce2934b920af8` |
| SHA256 | `150efe8be30654ab931e6c033b3cb761f5ce7568b57e4a545dcc04f223a9d255` |
| Overall entropy | 5.896 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2921055480 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.096 | No |
| `.rdata` | 9,216 | 4.728 | No |
| `.data` | 1,024 | 3.189 | No |
| `.pdata` | 1,536 | 3.156 | No |
| `.rsrc` | 49,664 | 5.643 | No |
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

Total strings found: **348** (showing first 100)

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

This code appears to be part of a **sophisticated downloader or "dropper"** masquerading as a legitimate software installer/updater. While the heavy use of UI-related functions and setup routines suggests an installer, several specific techniques are hallmarks of malware designed for persistence and bypassing system protections.

### Core Functionality
The code is structured to perform environment checks and preparation tasks common in installation wizards:
*   **System & Environment Validation:** It checks for Windows versions, available disk space (`GetDisk102`), and system information before proceeding with its main task.
*   **Resource Handling:** It manages various resource files (e.g., `.INF` or `.BAT` style logic) and handles directory creation/navigation to set up a workspace for subsequent components.
*   **UI Management:** Functions like `fcn.140004c68` manage window positioning and sizes, likely used to maintain the appearance of a standard installation wizard while it executes background tasks.

### Suspicious or Malicious Behaviors
The binary exhibits several behaviors highly indicative of malware, specifically for **persistence** and **evading security controls**:

*   **Persistence via Registry Manipulation:** 
    *   The code actively interacts with `Software\Microsoft\Windows\CurrentVersion\RunOnce` (in `fcn.140001d28`). This is used to ensure that a command or file runs automatically on the next login.
    *   It queries and modifies registry keys related to **PendingFileRenameOperations** (`fcn.140005380` & `fcn.140002318`). This technique is commonly used by malware to rename or replace system files that are currently "locked" by the OS, waiting for the next reboot to finalize the swap.
*   **Anti-Analysis / File Locking Bypass:** 
    *   The inclusion of and interaction with `DelNodeRunDLL32` (via `setupx.dll`) is a classic technique used to delete or modify files that would otherwise be blocked by Windows, often used during the "drop" phase of an infection.
*   **Privilege Management:** 
    *   The use of `GetTokenInformation`, `LookupPrivilegeValueA`, and `AdjustTokenPrivileges` (evident in the strings) suggests it is attempting to identify or elevate its own permissions, likely to gain access to system-level resources or network configurations.
*   **Sophisticated "Setup" Wrapper:** 
    *   The behavior of checking for `"RunOnce"` keys and performing `GetSystemDirectoryA` inside multiple nested logic loops indicates the code is designed to act as a "loader." It stays "quiet" while it prepares the environment (setting permissions, moving files) before launching a secondary payload.

### Notable Techniques & Patterns
*   **Dual-Purpose Logic:** The code blends legitimate installer features (GUI updates, directory creation, disk checks) with malicious techniques. This is a common tactic to evade detection by heuristic scanners that look for "malicious" actions in isolation.
*   **Fallback/Multi-stage Execution:** The logic in `fcn.140001d28` and `fcn.140005380` shows multiple paths for execution. If one method of establishing persistence or privilege fails, it attempts an alternative (e.g., checking different types of Session Manager keys).
*   **Path Sanitization:** The complex logic in `fcn.1400070a8` to handle quotes and backslashes while evaluating system paths suggests the code is designed to be robust across various environment configurations, ensuring it can find its components even if moved or renamed.

### Summary for Incident Response
This sample is likely a **loader/dropper**. It uses "installer-style" behavior as a front to perform **persistence** (via `RunOnce` and `PendingFileRenameOperations`) and **privilege elevation**, while employing specific Windows API tricks (`DelNodeRunDLL32`) to bypass standard file system locks. It is likely intended to deliver another payload or establish a foothold on the system.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The malware uses "installer-style" logic (UI management, directory creation) to blend in with legitimate software and evade detection by security analysts. |
| T1547.001 | Registry Run Keys / Startup Folder | The use of the `RunOnce` registry key is a direct method to ensure the malware or its components execute automatically upon user login/reboot. |
| T1546.010 | Windows Installer | Manipulation of `PendingFileRenameOperations` mimics legitimate installer behavior to bypass system locks on files that are currently in use by the OS. |
| T1564 | Hide Technique | The inclusion of `DelNodeRunDLL32` is used to circumvent standard file system restrictions and bypass security controls when modifying or deleting protected files. |
| T1068 | Exploitation for Privilege Escalation | Use of `GetTokenInformation`, `LookupPrivilegeValueA`, and `AdjustTokenPrivileges` indicates an attempt to elevate the process's authority to access restricted resources. |
| T1574 | Hijack Execution Flow | The "loader" behavior, where the code prepares an environment before launching a secondary payload, points to a multi-stage execution chain common in drop/loader scenarios. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*None identified.*

### **File paths / Registry keys**
*   **Registry Key:** `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Used for persistence)
*   **Registry Key:** `PendingFileRenameOperations` (Identified as a mechanism to bypass file locks and replace system files during reboot)
*   **File Name:** `IXP%03d.TMP` (Potential temporary file pattern used by the dropper)
*   **File Name:** `msdownld.tmp` (Temporary file likely associated with the delivery/drop phase)
*   **File Name:** `TMP4351$.TMP` (Specific temporary filename)
*   **File Name:** `wextract.pdb` (Debug symbols left by the developer)

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None identified in the provided text.*

### **Other artifacts**
*   **Technique/DLL usage:** `DelNodeRunDLL32` via `setupx.dll` (Used to delete or modify files that are otherwise blocked by the OS).
*   **Behavioral Pattern:** The sample utilizes "Installer-style" UI behavior and standard system utility calls as a wrapper to mask its primary function as a **loader/dropper**.
*   **Persistence Logic:** The code includes multi-stage checks for `RunOnce` and `PendingFileRenameOperations`, indicating high-confidence intent to establish persistence.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Persistence & Bypass Tactics:** The sample utilizes `RunOnce` registry keys and manipulates `PendingFileRenameOperations`. These are classic techniques used by malware to ensure persistence across reboots and to bypass system locks on files currently in use by the OS.
*   **Masquerading as Installer:** The code intentionally blends legitimate installer behaviors (UI management, disk space checks, and resource handling) with malicious "loader" functions to evade heuristic detection while preparing for a secondary payload.
*   **Privilege Elevation & Security Bypass:** The inclusion of `AdjustTokenPrivileges` for privilege escalation and the use of `DelNodeRunDLL32` (via `setupx.dll`) indicate a sophisticated attempt to bypass standard Windows security controls and gain higher-level system access.
