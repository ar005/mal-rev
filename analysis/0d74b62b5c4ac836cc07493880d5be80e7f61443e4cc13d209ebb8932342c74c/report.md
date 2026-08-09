# Threat Analysis Report

**Generated:** 2026-08-06 19:49 UTC
**Sample:** `0d74b62b5c4ac836cc07493880d5be80e7f61443e4cc13d209ebb8932342c74c_0d74b62b5c4ac836cc07493880d5be80e7f61443e4cc13d209ebb8932342c74c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d74b62b5c4ac836cc07493880d5be80e7f61443e4cc13d209ebb8932342c74c_0d74b62b5c4ac836cc07493880d5be80e7f61443e4cc13d209ebb8932342c74c.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 1,612,800 bytes |
| MD5 | `1ac3a8a20b26cdd31f21272efd830597` |
| SHA1 | `d86a5a283f9cb2a841d16c4ea97924f7e443c45c` |
| SHA256 | `0d74b62b5c4ac836cc07493880d5be80e7f61443e4cc13d209ebb8932342c74c` |
| Overall entropy | 7.734 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1337796189 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.096 | No |
| `.rdata` | 9,216 | 4.728 | No |
| `.data` | 1,024 | 3.189 | No |
| `.pdata` | 1,536 | 3.156 | No |
| `.rsrc` | 1,567,744 | 7.759 | ⚠️ Yes |
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

Total strings found: **3513** (showing first 100)

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

Based on the provided disassembly, here is a technical analysis of the code's behavior.

### Core Functionality and Purpose
The binary appears to be a complex **installer or system updater** component. It performs extensive environment checks (privileges, paths, registry keys) before executing what appears to be an installation sequence. It handles file system manipulation, resource loading, and "cleanup" operations typical of software that modifies system configuration or installs drivers/services.

### Suspicious or Malicious Behaviors
While the code shares patterns with legitimate installers, several specific behaviors are highly characteristic of malware designed for persistence and evasion:

*   **Persistence via Registry Manipulation:** 
    *   The function `fcn.140001d28` specifically targets the `RunOnce` registry key (`Software\Microsoft\Windows\CurrentVersion\RunOnce`). It constructs a path to an executable and sets it in this key, ensuring that a command is executed once after the next system restart or login.
    *   The code also interacts with `PendingFileRenameOperations`, a Windows mechanism often used by installers but also utilized by malware to replace system files during the boot process.

*   **Privilege Escalation & System Awareness:**
    *   The binary includes several calls for privilege management (`AdjustTokenPrivileges` style logic) and token information gathering (`GetTokenInformation`).
    *   It checks for specific "Administrative" capabilities (seen in `fcn.14000261c`) to determine if it has sufficient rights to perform modifications on system-level files or registries.

*   **File System Manipulation & Cleanup:**
    *   `fcn.1400061ec` and `fcn.14000204c` iterate through file lists, change file attributes (e.g., making them hidden/system), and delete files or directories.
    *   There is an automated "cleanup" routine where the program deletes its own temporary components or evidence after use.

*   **Anti-Analysis / Evasion:**
    *   **Heap Hardening Bypass:** The code calls `HeapSetInformation` (via a GetProcAddress loop). In many cases, this is used to disable certain security features in the heap that can interfere with specific types of memory manipulation or shellcode execution.
    *   **Resource Integrity Check:** It uses `GetFileVersionInfoA` and other Versioning API calls (`fcn.140002834`) to validate files before interacting with them, ensuring it is targeting the correct "victim" files.

### Notable Techniques or Patterns
*   **Dynamic API Resolution:** The use of `GetProcAddress` for critical functions (like `HeapSetInformation` and others in the `setupx.dll` / `advapi32.dll` range) suggests a desire to delay binding to sensitive APIs until necessary, potentially to evade basic static analysis.
*   **Environment Probing:** The code checks several specific paths:
    *   `Software\Microsoft\Windows\CurrentVersion\App Paths`: Used to locate system tools or other apps.
    *   `Control Panel\Desktop\ResourceLocale`: Checked via `fcn.140007f04`, likely as part of a localization check or environment fingerprinting.
*   **Delayed Execution/Persistence Logic:** The combination of `RunOnce` and the deletion of its own entry from that key (seen in `fcn.1400061ec`) is a common technique to ensure a persistent task is triggered but leaves minimal traces in the registry after completion.
*   **Standardized "Installer" Logic:** The code heavily uses `setupapi` and `shell32` logic. While these are standard for installers, they provide a legitimate-looking wrapper for actions like driver installation or system file replacement.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | The binary manipulates the `RunOnce` registry key to ensure execution after a system restart or user login. |
| T1136 | Create System Entry | The use of `PendingFileRenameOperations` allows the malware to manipulate or replace files during the boot process. |
| T1548 | Abuse Elevation Function | The binary uses `AdjustTokenPrivileges` and checks for "Administrative" capabilities to obtain higher privileges for system modification. |
| T1036 | Indicator Filtering | The binary modifies file attributes (making them hidden or system) to hide its presence from the user and security software. |
| T1070 | File Deletion | The automated "cleanup" routine deletes temporary files and evidence of execution to hinder forensic analysis. |
| T1562 | Impair Defenses | The use of `HeapSetInformation` is intended to disable memory management protections that could interfere with malicious behavior or shellcode. |
| T1027 | Obfuscated Files or Information | The use of dynamic API resolution (`GetProcAddress`) for critical functions helps the binary evade detection by static analysis tools. |
| T1082 | System Information Discovery | Probing specific paths like `App Paths` and `ResourceLocale` allows the malware to fingerprint the environment and identify target system details. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   **Registry Keys:**
    *   `Software\Microsoft\Windows\CurrentVersion\App Paths` (Used for identifying system tools)
    *   `Control Panel\Desktop\ResourceLocale` (Used for environment fingerprinting)
    *   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Utilized for persistence)
    *   `PendingFileRenameOperations` (Used to bypass security during file replacement/boot)
*   **Temporary File Patterns:**
    *   `IXP%03d.TMP`
    *   `msdownld.tmp`
    *   `TMP4351$.TMP`

**Mutex names / Named pipes**
*   *(None identified; while the `CreateMutexA` API is present, no specific mutex string was provided in the dump.)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Dynamic API Resolution:** Use of `GetProcAddress` loops for `HeapSetInformation` and other sensitive functions to evade static analysis.
*   **Anti-Analysis Techniques:** Explicit call to `HeapSetInformation` (used to bypass heap hardening and facilitate memory manipulation).
*   **Persistence/Cleanup Pattern:** The combination of writing to `RunOnce` followed by an automated cleanup routine to delete the registry entry after execution.
*   **Resource Integrity Checks:** Use of `GetFileVersionInfoA` and related versioning APIs to target specific "victim" files before modification.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Evasive Installation Tactics:** The sample utilizes "installer" logic (such as `PendingFileRenameOperations` and `RunOnce` registry keys) combined with a deliberate cleanup routine to ensure persistence while minimizing the forensic footprint of its execution.
*   **Anti-Analysis & Defense Evasion:** The use of dynamic API resolution (`GetProcAddress`) for sensitive functions and the specific invocation of `HeapSetInformation` indicates a high level of sophistication intended to bypass security measures like heap hardening and static analysis.
*   **Privilege Escalation & System Manipulation:** The binary actively checks for administrative privileges and manipulates file attributes (hiding them) to facilitate system-level changes, characteristic of a loader designed to prepare an environment for subsequent malicious payloads.
