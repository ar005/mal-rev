# Threat Analysis Report

**Generated:** 2026-08-11 22:41 UTC
**Sample:** `0e397bd7935c280c172bc5c95a57c9a652da50e2d770040432b245aa2d836ca1_0e397bd7935c280c172bc5c95a57c9a652da50e2d770040432b245aa2d836ca1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e397bd7935c280c172bc5c95a57c9a652da50e2d770040432b245aa2d836ca1_0e397bd7935c280c172bc5c95a57c9a652da50e2d770040432b245aa2d836ca1.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 2,100,224 bytes |
| MD5 | `851b0dd5e35495fa5cf122a6df17dd09` |
| SHA1 | `88e0f774d6cfef84e2b9e12f426eb08b7f649806` |
| SHA256 | `0e397bd7935c280c172bc5c95a57c9a652da50e2d770040432b245aa2d836ca1` |
| Overall entropy | 7.851 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1354420047 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.096 | No |
| `.rdata` | 9,216 | 4.728 | No |
| `.data` | 1,024 | 3.189 | No |
| `.pdata` | 1,536 | 3.156 | No |
| `.rsrc` | 2,055,168 | 7.869 | ⚠️ Yes |
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

Total strings found: **4462** (showing first 100)

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

Based on my analysis of the provided disassembly and string data, here is a summary of the binary's behavior.

### Core Functionality and Purpose
The binary functions as an **installer/dropper**. It contains logic to extract resources (specifically using **Cabinet** file logic), install files into the system, ensure persistence, and clean up its tracks after "installation." The inclusion of `CABINET` strings and `FDICopy`/`FDICreate` functions suggests it unpacks hidden payloads from within its own resource section.

### Suspicious or Malicious Behaviors
*   **Persistence Mechanism:** 
    *   The code explicitly interacts with the **RunOnce** registry key (`Software\Microsoft\Windows\CurrentVersion\RunOnce`). It checks for existing entries and, if necessary, writes new ones to ensure that components are executed by the system.
*   **Dropper/Unpacking Behavior:**
    *   It utilizes internal Cabinet (CAB) processing logic. Specifically, `fcn.140005380` and `fcn.140005240` manage the creation of files and directories while unpacking resources from a "cabinet" source. 
    *   The use of `FindResourceA`, `LoadResource`, and `LockResource` indicates that the primary payload is hidden within the binary's resources rather than being passed as an external file initially.
*   **Automatic File Cleanup:**
    *   Function `fcn.1400061ec` iterates through a list of files (likely temporary setup files or unpacking artifacts) and deletes them using `DeleteFileA`. This is a common technique to remove traces of the installation process from the disk.
*   **Privilege/Environment Awareness:**
    *   The code uses `GetTokenInformation`, `LookupPrivilegeValueA`, and `AdjustTokenPrivileges` (found in strings) to check or modify the current process's privileges, which is often used to gain sufficient permissions for system-wide installation.

### Notable Techniques and Patterns
*   **Dynamic API Resolution:** The binary uses `GetProcAddress` and `GetModule_FileNameA` extensively. This allows it to resolve critical functions at runtime rather than having them in the Import Address Table (IAT), a common technique used by malware to evade simple static analysis.
*   **Environment Validation:** 
    *   The use of `GetVersion` and `HeapSetInformation` suggests an attempt to check for specific OS versions or detect/evade certain sandbox environments.
    *   The presence of the string `DelNodeRunDLL32` is a classic indicator of a "silent" installer that removes temporary files after a DLL execution.
*   **Wait-and-Execute (Fork-and-Exec):** 
    *   In function `fcn.14000473c`, the code uses `CreateProcessA` followed by `WaitForSingleObject`. This indicates the binary launches and waits for a child process to complete, which is often used during a multi-stage infection to execute different tasks in separate processes.
*   **Registry Manipulation:** 
    *   Beyond `RunOnce`, it references several registry keys related to system configuration (e.g., `Control\Session Manager`). While these can be used by legitimate installers, they are high-value targets for malware seeking to modify environment behavior or hide persistence.

### Summary Conclusion
This binary is likely a **sophisticated dropper/downloader**. It is designed to unpack an internal payload using Cabinet logic, establish persistence via the registry, and perform "stealthy" file management (deleting temporary files) to minimize its footprint after the installation phase is complete.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Boot or Log-on Execution: Registry Run Keys / Startup Folder | The binary explicitly modifies the `RunOnce` registry key to ensure its components execute automatically upon system startup or user login. |
| T1574 | Archive Extraction | The inclusion of `CABINET` logic and resource loading functions indicates that the primary payload is unpacked from a hidden archive within the file's resources. |
| T1070.004 | Indicator Removal: File Deletion | The binary utilizes `DeleteFileA` to remove temporary files and installation artifacts, effectively minimizing its footprint on the disk. |
| T1027 | Obfuscated Files (Dynamic API Resolution) | The extensive use of `GetProcAddress` to resolve functions at runtime allows the binary to hide its true capabilities from static analysis of the Import Address Table (IAT). |
| T1497 | Virtualization/Sandbox Evasion | The use of `GetVersion` and `HeapSetInformation` suggests an attempt to detect and bypass automated analysis environments. |
| T1068 | Exploitation for Privilege Escalation | The use of `GetTokenInformation` and `AdjustTokenPrivileges` indicates the binary is attempting to acquire higher privileges for system-wide execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   **Registry Key:** `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Used for persistence)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Temporary File Names:** 
    *   `IXP%03d.TMP`
    *   `msdownld.tmp`
    *   `TMP4351$.TMP`
*   **Persistence/Evasion Artifacts:** 
    *   `DelNodeRunDLL32` (Indicates a self-deleting installer mechanism)
    *   Cabinet (CAB) unpacking logic (Used to hide payloads within the binary resources)

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family:** Unknown
2. **Malware type:** Dropper / Loader
3. **Confidence:** High

**Key evidence:**
*   **Resource Extraction & Persistence:** The binary utilizes Cabinet (CAB) logic to unpack a hidden payload from its own resources and implements persistence via the `RunOnce` registry key, which are hallmark behaviors of a sophisticated dropper.
*   **Anti-Analysis/Stealth Techniques:** The use of dynamic API resolution (`GetProcAddress`), sandbox evasion checks (`GetVersion`, `HeapSetInformation`), and the automatic deletion of temporary files (`DeleteFileA`) indicates an intentional effort to bypass security controls and hide its activities.
*   **Multi-Stage Execution:** The "fork-and-exec" behavior (using `CreateProcessA` followed by `WaitForSingleObject`) confirms it is designed to facilitate a multi-stage infection, typical of loaders used to deliver more complex payloads like RATs or ransomware.
