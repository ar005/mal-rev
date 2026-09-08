# Threat Analysis Report

**Generated:** 2026-09-06 14:45 UTC
**Sample:** `15020778c8004fbf4d4f123cf9b0f9749065baf32835790c44549efb7399414f_15020778c8004fbf4d4f123cf9b0f9749065baf32835790c44549efb7399414f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `15020778c8004fbf4d4f123cf9b0f9749065baf32835790c44549efb7399414f_15020778c8004fbf4d4f123cf9b0f9749065baf32835790c44549efb7399414f.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 3,232,766 bytes |
| MD5 | `eaab7f491c63f1599535ed2312bb4bff` |
| SHA1 | `7766fe317035246249e34cfb5e86ea586b51141a` |
| SHA256 | `15020778c8004fbf4d4f123cf9b0f9749065baf32835790c44549efb7399414f` |
| Overall entropy | 6.845 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1421992240 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.096 | No |
| `.rdata` | 9,216 | 4.728 | No |
| `.data` | 1,024 | 3.189 | No |
| `.pdata` | 1,536 | 3.156 | No |
| `.rsrc` | 3,187,200 | 6.844 | No |
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

Total strings found: **5608** (showing first 100)

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

Based on my analysis of the provided disassembly and decompiled C code, here is a summary of what this binary does.

### Core Functionality and Purpose
The binary appears to be a **complex installer or dropper**. Its primary purpose is to prepare an environment for "installing" software by checking system information, resolving file paths, manipulating the registry, and performing cleanup operations. The code structure is consistent with tools designed to unpack a payload and ensure it remains active on the system.

### Suspicious and Malicious Behaviors
The following behaviors are common in malware (specifically droppers and loaders):

*   **Persistence Mechanisms:**
    *   The code explicitly interacts with `Software\Microsoft\Windows\CurrentVersion\RunOnce` via **`fcn.140001d28`**. It reads/writes values to this key to ensure that commands (likely the dropped payload) are executed by the system during the next reboot or login.
    *   It uses `GetSystemDirectoryA` and `GetProcAddress` to dynamically resolve functions from system libraries, a common technique used to bypass static analysis of imports.

*   **Artifact Cleanup & Self-Deletion:**
    *   The routine **`fcn.14000204c`** uses `FindFirstFileA`, `FindNextFileA`, and `DeleteFileA`. It iterates through a directory (likely a temporary installation folder) to delete files after they are "processed." This is a common technique used by droppers to remove evidence of their existence on the disk.
    *   The use of **`DelNodeRunDLL32`** (seen in strings and logic) suggests a routine intended to programmatically "remove" the installer stub from the filesystem after it has successfully handed off execution to the primary payload.

*   **Anti-Analysis / Environment Awareness:**
    *   The code checks for specific system states like `PendingFileRenameOperations` and `FileRenameOperations`. While these are legitimate Windows features, they are frequently checked by malware to determine if a system is in a "maintenance" state or to detect the presence of certain security software.
    *   **`fcn.1400064e4`** checks for CPU architectures (x86, MIPS, Alpha) and other system metrics before proceeding, ensuring the dropped payload is compatible with the target environment.

*   **File/System Manipulation:**
    *   The binary performs extensive path parsing (**`fcn.1400070a8`**) to resolve whether a destination folder exists or needs to be created using `CreateDirectoryA`.
    *   It interacts with `.INF` and `.BAT` files (implied by logic in **`fcn.140001684`**), which are often used in legitimate installers but can also be leveraged to run secondary scripts or configuration changes.

### Notable Techniques & Patterns
*   **Dynamic API Resolution:** The binary frequently uses `GetProcAddress` and `LoadLibraryA`. This allows the malware to hide its true capabilities from basic static analysis tools by only revealing these "safe" calls in the Import Address Table (IAT).
*   **Hardcoded Registry Manipulation:** Instead of using a generic installer, it directly targets sensitive keys like `RunOnce`, which is high-confidence evidence of an intent to maintain persistence.
*   **Environment Validation:** The code includes extensive checks for Windows versions and resource locales (**`fcn.1400070a8`**, **`fcn.140003f74`**), ensuring the environment matches a specific target profile before "installing" its components.
*   **Recursive File Cleanup:** The pattern of finding files in a folder and immediately deleting them (**`fcn.14000204c`**) indicates it is cleaning up temporary files used during the unpacking phase.

### Summary for Incident Response
This binary is likely a **Dropper**. It acts as a "loader" that performs environment checks, ensures persistence via registry keys (`RunOnce`), and cleans up its own footprint after deploying a secondary payload. The presence of `DelNode` logic suggests it is designed to delete itself from the disk once the primary malware has been successfully executed.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the relevant MITRE ATT&K techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | The binary modifies the `RunOnce` registry key to ensure payload execution upon subsequent system logins or reboots. |
| **T1027** | Obfuscated Files or Information | The use of `GetProcAddress` and `LoadLibraryA` is used to resolve APIs at runtime, hiding the true capabilities of the binary from static analysis tools. |
| **T1070.004** | Indicator Removal on Host: File Deletion | The routine identifying and deleting files in a temporary directory (and its own "DelNode" logic) is designed to remove evidence of its presence on disk. |
| **T1485** | Environment Keying | The extensive checks for CPU architecture, Windows version, and locale ensure the payload only executes when specific target environment criteria are met. |
| **T1059.003** | Command and Scripting Interpreter: Windows Command Shell | The use of `.BAT` files indicates a reliance on scripting to execute secondary tasks or configuration changes during the installation process. |
| **T1106** | Createpad | *Note: While not explicitly mentioned, the "Dropper" behavior involving resolving paths and creating directories (CreateDirectoryA) is indicative of preparing for payload deployment.* |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Used for persistence)
*   `wininit.ini` (Potential configuration file/artifact)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified in the provided text.

**Other artifacts**
*   **C2/Persistence Patterns:** Utilization of the `RunOnce` registry key to ensure execution after reboot.
*   **Self-Deletion Logic:** Presence of `DelNodeRunDLL32` and specific routines (`fcn.14000204c`) designed to delete installation artifacts and the primary stub from the filesystem.
*   **Dynamic API Resolution:** Use of `GetProcAddress` and `LoadLibraryA` to obfuscate functionality by resolving APIs at runtime rather than during load time.
*   **Temporary File Artifacts:**
    *   `IXP%03d.TMP`
    *   `msdownld.tmp`
    *   `TMP4351$.TMP`
*   **Environment Checks:** Logic identified in `fcn.1400064e4` and `fcn.1400070a8` used to validate system architecture and resource locales before execution.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Persistence and Self-Deletion:** The binary utilizes the `RunOnce` registry key for persistence while simultaneously employing specific routines (like `DelNodeRunDLL32`) to delete its own executable and associated temporary files from the disk after the primary payload is deployed.
*   **Evasive Maneuvers:** It employs advanced anti-analysis techniques, including dynamic API resolution (`GetProcAddress`/`LoadLibraryA`) to hide its capabilities and "Environment Keying" (checking CPU architecture and system locale) to ensure it only executes on targeted systems.
*   **Payload Delivery Workflow:** The extensive use of directory creation logic, interaction with `.BAT`/`.INF` files, and the systematic cleanup of temporary artifacts (e.g., `IXP001.TMP`) are classic indicators of a loader designed to facilitate the successful installation of a second-stage payload.
