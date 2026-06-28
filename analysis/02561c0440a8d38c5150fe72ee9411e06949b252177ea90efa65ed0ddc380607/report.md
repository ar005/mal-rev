# Threat Analysis Report

**Generated:** 2026-06-28 04:25 UTC
**Sample:** `02561c0440a8d38c5150fe72ee9411e06949b252177ea90efa65ed0ddc380607_02561c0440a8d38c5150fe72ee9411e06949b252177ea90efa65ed0ddc380607.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `02561c0440a8d38c5150fe72ee9411e06949b252177ea90efa65ed0ddc380607_02561c0440a8d38c5150fe72ee9411e06949b252177ea90efa65ed0ddc380607.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 1,604,648 bytes |
| MD5 | `675c06a636209d1b19fb02eaa70132cb` |
| SHA1 | `fdc2d22d9d2d9962cb30ac8b4227b782975c5618` |
| SHA256 | `02561c0440a8d38c5150fe72ee9411e06949b252177ea90efa65ed0ddc380607` |
| Overall entropy | 7.863 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1485125896 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.096 | No |
| `.rdata` | 9,216 | 4.728 | No |
| `.data` | 1,024 | 3.189 | No |
| `.pdata` | 1,536 | 3.156 | No |
| `.rsrc` | 1,549,824 | 7.888 | ⚠️ Yes |
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

Total strings found: **3640** (showing first 100)

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

Based on the provided disassembly and strings, here is a technical analysis of the binary's behavior:

### Core Functionality and Purpose
The code exhibits characteristics of a **malware dropper or installer wrapper**. While it mimics the behavior of a standard software installation utility (using resource loading, "Setup" logic, and directory checks), it incorporates several high-level techniques used by malware to ensure persistence, escalate privileges, and execute secondary payloads.

### Suspicious and Malicious Behaviors

*   **Privilege Escalation:**
    *   The code utilizes `OpenProcessToken`, `LookupPrivilegeValueA`, and `AdjustTokenPrivileges`. These are classic indicators of a program attempting to gain higher system privileges (e.g., `SeDebugPrivilege`) to interact with protected processes or system resources. 
    *   **Function Reference:** `fcn.1400012ec` specifically handles token manipulation to escalate the process's capabilities.

*   **Persistence Mechanisms:**
    *   **RunOnce Registry Key:** The code interacts with the `Software\Microsoft\Windows\CurrentVersion\RunOnce` registry key (seen in `fcn.140001d28`). While "RunOnce" is a legitimate Windows feature, it is frequently used by malware to ensure that additional components or payloads execute automatically upon the next user login/reboot.
    *   **PendingFileRenameOperations:** The code specifically checks for and interacts with `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\PendingFileRenameOperations` (via `fcn.140002318`). This is a sophisticated technique used by both legitimate installers and malware to "stage" files for execution or replacement during the next system boot, often bypassing some real-time security monitors.

*   **Environment/Privilege Probing:**
    *   The code performs extensive checks on its environment, including querying system information (`GetVersionExA`), checking for specific capabilities via `fcn.140003f74`, and navigating "App Paths." This is often used to determine if the sample is running in a restricted sandbox or an analysis environment.

*   **File System Manipulation:**
    *   The function `fcn.14000204c` implements logic to find, rename (or move), and delete files/directories. 
    *   The use of `DeleteFileA` and `RemoveDirectoryA` in a loop is often used by "droppers" to clean up temporary files or artifacts left behind during the infection process.

### Notable Techniques and Patterns

*   **API Obfuscation/Resolution:** The code makes frequent use of `GetProcAddress` and `GetModuleHandle` (often wrapped in internal functions) to resolve symbols at runtime. This is a standard technique to hide the program's true capabilities from static analysis.
*   **String Manipulation & Parsing:** Function `fcn.1400070a8` contains complex logic for parsing paths and strings. The code appears to manually process path segments (e.g., checking for `:` or `\`), which is a common way to handle file operations without relying on high-level, easily-hookable APIs.
*   **Resource Loading:** The presence of "CABINET," "INST," and various setup-related strings suggests the binary may be looking for and unpacking additional resources/modules from an embedded stream (like a `.cab` or `.zip` file).
*   **Error Handling via Message Box:** Many functions conclude with calls to `fcn.140004dcc`, which triggers a `MessageBoxA`. This is typical of installers, but in malware, it can be used to provide "decoy" messages to the user while malicious actions occur in the background.

### Summary Table of Malicious Indicators
| Behavior | Observed Evidence / Function | Risk Level |
| :--- | :--- | :--- |
| **Privilege Escalation** | `AdjustTokenPrivileges`, `LookupPrivilegeValueA` (`fcn.1400012ec`) | High |
| **Persistence** | `RunOnce` Registry Key, `PendingFileRenameOperations` | High |
| **Evasion/Defense Evasion** | Dynamic API resolution via `GetProcAddress` | Medium |
| **Installer Behavior** | Resource loading, "Setup" logic (indicative of a dropper) | Informational |

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the following MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1068** | Exploitation for Privilege Escalation | The use of `AdjustTokenPrivileges` and `LookupPrivilegeValueA` indicates an intentional effort to gain higher system privileges. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys | The interaction with the `RunOnce` registry key is a common method used to ensure execution during subsequent user logins. |
| **T1497** | Virtualization/Sandbox Evasion | The use of `GetVersionExA` and capabilities checking suggests an attempt to identify if the malware is running in an analysis environment. |
| **T1070** | Indicator Removal on Host | The use of `DeleteFileA` and `RemoveDirectoryA` in a loop indicates an effort to remove artifacts or temporary files left during the infection process. |
| **T1036** | Masquerading | The binary mimics "Setup" logic and installation behavior to blend in with legitimate software and evade detection by users or basic security tools. |

***Note on Supplemental Observations:***
*   **Persistence via `PendingFileRenameOperations`**: While specifically listed in your analysis, this is also categorized under **T1547** (Boot or Logon Autostart Execution) as it ensures the execution/replacement of files during the system boot sequence. 
*   **API Obfuscation (`GetProcAddress`)**: This behavior falls under the broader **Defense Evasion** tactic; while not always mapped to a specific sub-technique, it is a core methodology for hiding program capabilities from static analysis tools.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Registry Key - Persistence)
*   `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\PendingFileRenameOperations` (Registry Key - Persistence/Staging)
*   `wininit.ini` (File)
*   `msdownld.tmp` (Temporary File)
*   `TMP4351$.TMP` (Temporary File)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified - Note: The non-alphanumeric strings in the "Extracted Strings" section appear to be obfuscated data or junk code and do not constitute standard MD5/SHA hashes.)*

**Other artifacts**
*   `IXP%03d.TMP` (File naming pattern)
*   `UPDFILE%lu` (File naming pattern)
*   `wextract.pdb` (PDB reference; indicates the internal project name or developer environment)
*   **Note on API behavior:** The analysis confirms the use of `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, and `GetProcAddress`. While these are standard Windows APIs, their specific implementation in this context is used for privilege escalation and evasion.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Privilege Escalation & Persistence**: The sample utilizes `AdjustTokenPrivileges` to gain higher system permissions and employs both `RunOnce` registry keys and `PendingFileRenameOperations` to ensure its persistence or the execution of subsequent payloads across reboots.
    *   **Evasive Characteristics**: The binary includes specific environmental checks (e.g., `GetVersionExA`) to detect sandboxes/analysis environments and uses "Setup" masquerading to blend in with legitimate installation processes.
    *   **Staging Behavior**: The use of self-contained resources, temporary file manipulation (e.g., `.tmp` files), and the cleanup of artifacts via `DeleteFileA` are classic indicators of a dropper designed to deliver and hide subsequent components.
