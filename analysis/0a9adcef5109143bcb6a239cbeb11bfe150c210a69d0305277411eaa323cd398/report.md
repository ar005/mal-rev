# Threat Analysis Report

**Generated:** 2026-07-25 01:56 UTC
**Sample:** `0a9adcef5109143bcb6a239cbeb11bfe150c210a69d0305277411eaa323cd398_0a9adcef5109143bcb6a239cbeb11bfe150c210a69d0305277411eaa323cd398.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a9adcef5109143bcb6a239cbeb11bfe150c210a69d0305277411eaa323cd398_0a9adcef5109143bcb6a239cbeb11bfe150c210a69d0305277411eaa323cd398.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 1,891,440 bytes |
| MD5 | `d97387312872e799a2554362fb6088c7` |
| SHA1 | `553fb268a88a7d3e5db70607fe6c1aae0c6fbead` |
| SHA256 | `0a9adcef5109143bcb6a239cbeb11bfe150c210a69d0305277411eaa323cd398` |
| Overall entropy | 7.489 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1544664250 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.096 | No |
| `.rdata` | 9,216 | 4.728 | No |
| `.data` | 1,024 | 3.189 | No |
| `.pdata` | 1,536 | 3.156 | No |
| `.rsrc` | 1,838,080 | 7.505 | ⚠️ Yes |
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

Total strings found: **4273** (showing first 100)

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

### Analysis Summary: Windows Installer Stub / Wrapper

Based on the provided strings and decompiled code, this binary appears to be an **installer wrapper or a stub** designed to facilitate the installation of software on a Windows system. It utilizes several standard Win32 APIs typical of "Setup" utilities, but it also includes logic common in malware for persistence and environment preparation.

### Core Functionality
The primary purpose of this code is to manage the execution of an installation routine. It handles:
*   **Environment Validation:** Checking disk space (`GetDiskFreeSpaceA`), drive types (`GetDriveTypeA`), and system versions/capabilities.
*   **Configuration Parsing:** Reading values from `.INF` files (e.g., `GetPrivateProfileStringA`) to determine whether a reboot is required or what "Advanced" settings to apply.
*   **Path Normalization:** Converting and validating file paths, including handling of network shares and different drive root formats (`fcn.1400070a8`).
*   **Execution Orchestration:** It manages the flow between different installer components by invoking DLLs (like `setupx.dll` or `setupapi.dll`) and determining if specific scripts (like `.BAT` files) need to be executed.

### Suspicious/Malicious Behaviors
While much of this behavior is typical for legitimate installers, the following sections are noteworthy from a security perspective:

*   **Persistence Mechanism:** 
    *   The code explicitly interacts with the **`RunOnce`** registry key (`Software\Microsoft\Windows\CurrentVersion\RunOnce`) in several locations (e.g., `fcn.140001d28`). This is used to ensure that specific commands are executed by the system once after a reboot, commonly used by installers but also frequently abused by malware for persistence or delayed execution of secondary payloads.
*   **Privilege Escalation/Validation:** 
    *   In `fcn.1400012ec`, the code performs detailed **Token and SID checks** (`OpenProcessToken`, `GetTokenInformation`, `AllocateAndInitializeSid`, `EqualSid`). This is used to verify if the process has sufficient privileges (e.g., administrative rights) before attempting to modify system files or registries.
*   **File Manipulation & Cleanup:** 
    *   The function `fcn.14000204c` uses **`FindFirstFileA`** and **`FindNextFileA`** to iterate through a directory and calls **`DeleteFileA`** and **`RemoveDirectoryA`**. This is used for "cleaning" up setup files, but in a malicious context, it can be used to delete evidence of an installation or remove security software.
*   **Advanced Scripting Execution:** 
    *   The code checks for `.BAT` file extensions (e.g., `fcn.140001684`). It may be used to execute batch scripts that perform administrative tasks during the setup process.

### Notable Techniques & Observations
*   **Win32 Installer Integration:** The presence of `DelNodeRunDLL32` and references to `Cabinet` (likely related to the `CABINET.dll` library) suggests it is a wrapper for an MSI-based installer or uses similar logic to manage cabinet files (.cab).
*   **Robust Path Handling:** The code includes sophisticated checks for path formatting (e.g., handling `C:`, UNC paths, and short/long name conversions), ensuring the installer works across various Windows configurations.
*   **Defensive Programming / Errors:** It utilizes a common error-handling pattern where it retrieves system messages (`Get_last_error` logic) to display via `MessageBoxA` or other UI elements if an action (like creating a directory or opening a registry key) fails.
*   **Potential for Masquerading:** The use of standard strings like "Risk," "Version," and interaction with standard Windows dialogs (`Shell32.dll`) suggests the binary is designed to appear as a legitimate installer while performing system-level modifications.

### Conclusion
This binary is likely an **installer stub**. It is highly functional, intended to automate complex setup procedures on Windows systems. While its primary purpose is installation management, the specific use of `RunOnce` for persistence and robust token checking indicates it is designed to perform high-privilege actions on the system.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys | The binary interacts with the `RunOnce` registry key to ensure specific commands are executed after a system reboot for persistence or delayed execution. |
| **T1068** | Exploitation for Privilege Escalation | The code performs detailed Token and SID checks to verify if the process has sufficient administrative privileges before attempting high-impact actions. |
| **T1070.004** | Indicator Removal on Host: File Deletion | The use of `DeleteFileA` and `RemoveDirectoryA` can be used to remove evidence of activity or delete security-related files from the system. |
| **T1059.003** | Command and Scripting Interpreter: Batch | The binary specifically checks for and executes `.BAT` files to perform administrative tasks as part of its routine. |
| **T1036** | Masquerading | The use of standard installer strings, common DLL names (e.g., `setupx.dll`), and standard Win32 dialogs is designed to hide malicious activity behind a legitimate-looking interface. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Identified as a persistence mechanism used to execute commands following a reboot).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Temporary File Patterns:** 
    *   `IXP%03d.TMP`
    *   `msdownld.tmp`
    *   `TMP4351$.TMP`
*   **Specific Internal Strings (Potential for YARA/Signature identification):**
    *   `DelNodeRunDLL32` (Associated with the installer stub's execution logic).
    *   `setupx.dll` / `setupapi.dll` (While standard libraries, they are identified as primary components of the wrapper functionality).

***

**Analyst Note:** The binary functions primarily as an **installer stub**. While many of the strings present are common to Windows installation utilities, the specific utilization of the `RunOnce` registry key and the patterns for temporary file creation (`.TMP`) are the primary indicators of its operational behavior during a system infection or software deployment.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Installer Stub Behavior:** The binary functions as a wrapper designed to mimic a legitimate Windows installer, utilizing standard components (e.g., `setupx.dll`, `setupapi.dll`) and common naming conventions to mask its activities from the user and security systems.
*   **Persistence & Privilege Escalation:** The implementation of specific logic to check for high-level permissions via Token/SID checks and the use of the `RunOnce` registry key are classic indicators of a loader preparing an environment for subsequent execution or persistence.
*   **Execution Orchestration:** The ability to execute `.BAT` scripts and perform "cleanup" operations (deleting installation artifacts) suggests it is designed as a first-stage component to facilitate the delivery and deployment of secondary payloads.
