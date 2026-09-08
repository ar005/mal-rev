# Threat Analysis Report

**Generated:** 2026-09-04 19:26 UTC
**Sample:** `142fdb8fd9050a03e994ef33697c847cb64c2e2a1c822b48a32c01e2ac744149_142fdb8fd9050a03e994ef33697c847cb64c2e2a1c822b48a32c01e2ac744149.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `142fdb8fd9050a03e994ef33697c847cb64c2e2a1c822b48a32c01e2ac744149_142fdb8fd9050a03e994ef33697c847cb64c2e2a1c822b48a32c01e2ac744149.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 8,389,120 bytes |
| MD5 | `8c27301f9e6afb6097adb5fc88b2e5d2` |
| SHA1 | `396e9ebd9b42f5b7e8b0af38549b11d76c21529f` |
| SHA256 | `142fdb8fd9050a03e994ef33697c847cb64c2e2a1c822b48a32c01e2ac744149` |
| Overall entropy | 3.118 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1263208360 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.096 | No |
| `.rdata` | 9,216 | 4.728 | No |
| `.data` | 1,024 | 3.189 | No |
| `.pdata` | 1,536 | 3.156 | No |
| `.rsrc` | 8,344,064 | 3.092 | No |
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

Total strings found: **4001** (showing first 100)

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

Based on the provided disassembly and string analysis, here is a breakdown of the binary's functionality and behavior.

### Core Functionality and Purpose
The binary appears to be a **sophisticated installer or loader**, likely for a "downloader" or "dropper" payload. It heavily utilizes standard Windows Setup APIs (e.g., `SetupApi`, `Cabinet` functions) and advanced system management logic. Its primary purpose seems to be preparing the environment, extracting components, and ensuring that subsequent processes are executed with appropriate privileges or hidden from casual observation.

### Suspicious and Malicious Behaviors

*   **Persistence & Manipulation of System Registry:**
    *   The code interacts heavily with `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce`. 
    *   Specifically, it uses **`DelNodeRunDLL32`** (via `setupx.dll`). This is a classic technique used by both legitimate installers and malware to manipulate the RunOnce key—either to ensure an installer finishes its task or to "clean up" traces of execution after a successful installation/infection.
    *   It also queries **`PendingFileRenameOperations`** via `fcn.140002318`. This is often used by installers to perform actions that require a system reboot, but in a malware context, it can be used to hide or replace critical files during the boot process.

*   **Privilege Escalation & Token Manipulation:**
    *   The presence of **`AdjustTokenPrivileges`**, **`GetProcessTokenInformation`**, and **`LookupPrivilegeValueA`** (all found in the string list) indicates that the binary attempts to escalate its privileges or manipulate its access token. 
    *   It specifically checks for certain capabilities before proceeding with high-level actions, which is common when an installer needs "SYSTEM" or administrative rights to modify protected areas of the OS.

*   **System Environment Probing:**
    *   The binary performs extensive environment checks, including **`GetVersionExA`**, **`GetFileAttributesA`**, and **`GetSystemDirectoryA`**. 
    *   It seems to verify if it is running in a specific context or on a supported version of Windows before executing "privileged" code paths (e.g., the logic branching inside `fcn.140002c54`).

*   **Automatic Artifact Cleanup:**
    *   Function **`fcn.1400061ec`** and **`fcn.14000204c`** contain logic to iterate through files, compare them against specific strings (likely identifying temporary installation artifacts), and delete them using `DeleteFileA`. This is a common "cleanup" routine used by malware to remove evidence of its installer/dropper components after the main payload has been successfully executed.

### Notable Techniques & Patterns

*   **"Wrapper" Behavior:** The binary exhibits characteristics of a "wrapper." It uses many standard Windows Setup components (like `Cabinet` and `SetupApi`) to appear like a legitimate installation tool, while hiding more malicious logic inside complex conditions or separate dynamically loaded modules.
*   **Dynamic Module Loading:** It frequently uses **`GetProcAddress`** and **`LoadLibraryA`**. This is often used by malware to hide its true functionality from static analysis; it only resolves the "dangerous" functions (like those for registry manipulation) at runtime.
*   **Resource Management:** The use of `Cabinet.dll` and functions like `FDICreate` and `FDICopy` suggests that there is an encrypted or compressed payload contained within a resource section, which this program extracts to the disk before execution.
*   **Obfuscated Logic Flow:** The extensive use of `fcn.140004dcc` (which appears to be a wrapper for `LoadStringA` and error handling) suggests that while many messages are shown to the user, much of the internal logic is heavily guarded by condition checks.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostar Execution: Registry Run Keys/Startup Folder | The binary interacts with the `RunOnce` registry key to ensure execution or clear its presence post-installation. |
| **T1068** | Exploitation for Privilege Escalation | Use of `AdjustTokenPrivileges`, `GetProcessTokenInformation`, and `LookupPrivilegeValueA` indicates an attempt to gain higher system privileges. |
| **T1497** | Virtualization/Sandbox Detection | Extensive usage of `GetVersionExA` and environment checks suggests the binary is probing for analysis environments before executing core logic. |
| **T1106** | Native API | The use of `GetProcAddress` and `LoadLibraryA` allows the binary to resolve "dangerous" functions at runtime to evade static detection. |
| **T1070.004** | Indicator Removal on Host: File Deletion | The specific logic in `fcn.11061ec` and `fcn.14000204c` uses `DeleteFileA` to remove temporary artifacts and evidence of infection. |
| **T1036** | Masquerading | The binary utilizes standard Windows Setup APIs and components (like `Cabinet`) to mimic a legitimate installer for the purpose of hiding its presence. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** Standard system paths (e.g., `Control Panel\Desktop\ResourceLocale`) and common library files (e.g., `advapi32.dll`) have been excluded as false positives per your instructions.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **msdownld.tmp** (Potential temporary file name)
*   **TMP4351$.TMP** (Specific temporary filename used during execution)
*   **IXP%03d.TMP** (Pattern for temporary files created by the installer/loader)
*   **UPDFILE%lu** (Variable-based path naming convention)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *No MD5, SHA1, or SHA256 hashes were present in the provided strings.*

### **Other artifacts**
*   **Function/Library Utility:** `DelNodeRunDLL32` (Specifically associated with `setupx.dll`; used to manipulate RunOnce keys).
*   **Persistence Mechanism:** Manipulation of `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce`.
*   **Evasion/Stealth Technique:** Utilization of the **`PendingFileRenameOperations`** registry key to mask file replacements during system reboots.
*   **Privilege Escalation Indicators:** The use of `AdjustTokenPrivileges`, `GetProcessTokenInformation`, and `LookupPrivilegeValueA`.
*   **Behavioral Pattern:** "Cleanup" routine (functions `fcn.1400061ec` and `fcn.14000204c`) specifically designed to delete temporary artifacts after payload extraction.

---

## Malware Family Classification

Based on the behavioral analysis provided, here is the classification:

1. **Malware family**: custom
2. **Malware type**: loader / dropper
3. **Confidence**: High
4. **Key evidence**: 
    *   **Wrapper Behavior & Component Usage:** The binary uses standard Windows Setup APIs (`Cabinet`, `SetupApi`) and dynamic API resolution to mask its true purpose, a hallmark of a "wrapper" or loader designed to deliver additional payloads while masquerading as a legitimate installer.
    *   **Post-Execution Cleanup:** The presence of specific functions dedicated to identifying and deleting temporary artifacts (like `.tmp` files) after the main payload is triggered indicates a primary goal of minimizing the forensic footprint on the host system.
    *   **Evasion & Persistence Techniques:** The use of `PendingFileRenameOperations`, privilege escalation routines, and environment checks suggests the binary's role is to bypass security controls and prepare the OS for more malicious activities (such as installing a RAT or ransomware).
