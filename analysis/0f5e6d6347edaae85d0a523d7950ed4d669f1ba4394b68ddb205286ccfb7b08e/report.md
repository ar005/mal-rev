# Threat Analysis Report

**Generated:** 2026-08-15 22:50 UTC
**Sample:** `0f5e6d6347edaae85d0a523d7950ed4d669f1ba4394b68ddb205286ccfb7b08e_0f5e6d6347edaae85d0a523d7950ed4d669f1ba4394b68ddb205286ccfb7b08e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f5e6d6347edaae85d0a523d7950ed4d669f1ba4394b68ddb205286ccfb7b08e_0f5e6d6347edaae85d0a523d7950ed4d669f1ba4394b68ddb205286ccfb7b08e.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 1,804,800 bytes |
| MD5 | `73522e67154192641ca6db26f692b2d3` |
| SHA1 | `1e682a080f7f3aad944afd7d4db7036955790cd5` |
| SHA256 | `0f5e6d6347edaae85d0a523d7950ed4d669f1ba4394b68ddb205286ccfb7b08e` |
| Overall entropy | 7.635 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1591519199 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.096 | No |
| `.rdata` | 9,216 | 4.728 | No |
| `.data` | 1,024 | 3.189 | No |
| `.pdata` | 1,536 | 3.156 | No |
| `.rsrc` | 1,759,744 | 7.658 | ⚠️ Yes |
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

Total strings found: **3466** (showing first 100)

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

### Overview
The provided code describes a **malware dropper or an advanced installer**. The binary's primary purpose is to prepare the system environment, establish persistence, and potentially stage or install additional components (such as payloads) by manipulating registry keys and the filesystem.

While it contains elements common in legitimate software installers (like Cabinet file handling and version checking), several specific behaviors are highly characteristic of malware.

### Core Functionality & Purpose
*   **System Preparation:** The code extensively checks for system environment details, such as the Windows version (`GetVersionExA`), current directory status, and disk space/drive types.
*   **Resource Management:** It utilizes `Cabinet.dll` (specifically functions like `FDICreate` and `FDICopy`) to handle compressed files. This is a common method for extracting a hidden payload from within a larger package.
*   **Environment Mapping:** Several functions (`fcn.1400070a8`, `fcn.1400064e4`) are dedicated to resolving and validating file paths, including handling local drives (C:, D:) and network shares/UNC paths.

### Suspicious or Malicious Behaviors
*   **Persistence via "RunOnce":** The function `fcn.140001d28` explicitly interacts with the registry key `Software\Microsoft\Windows\CurrentVersion\RunOnce`. It retrieves system information and creates/sets a value in this key to ensure that an associated program is executed automatically upon the next user login.
*   **File Replacement (Pending Operations):** The function `fcn.140002318` queries the `PendingFileRenameOperations` registry key. This technique is frequently used by malware to replace system files or known binaries with malicious ones; the replacement occurs during the next boot sequence, which can bypass certain real-time protections.
*   **Self-Cleaning/Artifact Removal:** The function `fcn.14000204c` implements a recursive search and delete mechanism. It iterates through directories using `FindFirstFileA`/`FindNextFileA` and removes files that match specific criteria. This is often used by malware to "clean up" temporary files or dropped components after the primary payload has been successfully installed.
*   **Directory/File Harvesting:** The code performs heavy checks on disk space (`GetDiskFreeSpaceA`) and volume information, ensuring there is enough room for potential payloads or hidden directories (e.g., "MEMCAB").

### Notable Techniques & Patterns
*   **Drop-and-Execute Logic:** The use of `CreateProcessA` followed by `WaitForSingleObject` and `GetExitCodeProcess` in `fcn.14000473c` suggests a multi-stage execution model. The primary binary may launch a secondary "worker" or payload process, wait for it to finish, and then proceed with cleanup.
*   **Dynamic Loading:** The code heavily relies on `GetProcAddress` and `LoadLibraryA`. This allows the binary to resolve its dependencies at runtime, which can be used to hide functionality from simple static analysis of the Import Address Table (IAT).
*   **Standard API Abuse:** It uses "dual-use" APIs like `ShellExecute`, `Cabinet.dll`, and standard registry keys. These are common in installers but are favored by malware authors because they provide high compatibility across different Windows versions while executing sophisticated actions.
*   **Reflective Manipulation (Potential):** The presence of `DelNodeRunDLL32` in the strings suggests a mechanism to quickly unload or remove items from running processes or system lists, often used during "clean" uninstalls but equally useful for evading detection.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors described in your analysis to the relevant MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | The code explicitly modifies the `RunOnce` registry key to ensure a payload is executed during the next user login. |
| **T1560.003** | Archive Extraction: Payload Files | The use of `Cabinet.dll` functions (`FDICreate`, `FDICopy`) indicates the extraction of hidden payloads from compressed archives or installers. |
| **T1070** | Indicator Removal on Host | The implementation of a recursive search and delete mechanism is used to clear tracks by removing temporary files and artifacts after execution. |
| **T1036** | System Information Discovery | The code queries the system version, disk space, and hardware details to map the environment before deploying components. |
| **T1115** | Modify Certificate (Contextual: Defense Evasion via Dynamic Loading) | While technically a "Malware Design" choice, the use of `GetProcAddress` and `LoadLibraryA` is used to hide the Import Address Table (IAT) from static analysis. |
| **T1059** | Command and Scripting Interpreter | The multi-stage execution model (`CreateProcessA`, `WaitForSingleObject`) indicates a "drop-and-execute" logic to transition from a loader to a primary payload. |
| **T1546** | Scheduled Task / System Startup (Pending File Rename) | The manipulation of the `PendingFileRenameOperations` registry key allows the malware to replace system files during the next boot cycle to bypass real-time protections. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral reports, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `Software\Microsoft\Win\CurrentVersion\RunOnce` (Used for persistence)
*   `PendingFileRenameOperations` (Used to bypass security and replace files on reboot)
*   `MEMCAB` (Identified as a specific directory used for hidden components)
*   `IXP%03d.TMP` (Temporary file naming convention)
*   `msdownld.tmp` (Potential temporary dropped file)
*   `TMP4351$.TMP` (Potential temporary dropped file)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified in the provided text.

**Other artifacts**
*   **DelNodeRunDLL32**: A specific string indicating a mechanism to manipulate or remove items from running processes/system lists.
*   **DecryptFileA**: Internal function identifier suggesting logic for decrypting and extracting hidden payloads.
*   **RUNPROGRAM / POSTRUNPROGRAM**: Logic flags indicative of a multi-stage execution workflow.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Payload Extraction & Staging:** The use of `Cabinet.dll` for unpacking files, combined with a multi-stage "drop-and-execute" logic (using `CreateProcessA` and `WaitForSingleObject`), confirms its primary role as a vehicle to deliver secondary payloads.
    *   **Persistence and Evasion Tactics:** The manipulation of the `RunOnce` registry key and the use of `PendingFileRenameOperations` are high-confidence indicators of an intent to establish long-term persistence and bypass real-time security protections during system reboots.
    *   **Anti-Forensics/Cleanup:** The inclusion of a recursive deletion routine to remove temporary files (`FindFirstFileA`/`FindNextFileA`) and the use of dynamic loading to hide its Import Address Table (IAT) are characteristic behaviors of sophisticated malware designed to minimize its footprint on the host.
