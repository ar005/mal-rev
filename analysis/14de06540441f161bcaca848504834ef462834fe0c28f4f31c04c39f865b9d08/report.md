# Threat Analysis Report

**Generated:** 2026-09-06 09:54 UTC
**Sample:** `14de06540441f161bcaca848504834ef462834fe0c28f4f31c04c39f865b9d08_14de06540441f161bcaca848504834ef462834fe0c28f4f31c04c39f865b9d08.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14de06540441f161bcaca848504834ef462834fe0c28f4f31c04c39f865b9d08_14de06540441f161bcaca848504834ef462834fe0c28f4f31c04c39f865b9d08.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 2,678,784 bytes |
| MD5 | `8e3e9d6ee1971daad075a5c477ef9959` |
| SHA1 | `2a8aeb15bc596d295b7cc25dc55775999b3eb1e3` |
| SHA256 | `14de06540441f161bcaca848504834ef462834fe0c28f4f31c04c39f865b9d08` |
| Overall entropy | 7.099 |
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
| `.rsrc` | 1,806,336 | 7.483 | ⚠️ Yes |
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

Total strings found: **3976** (showing first 100)

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

### Overview
The provided code describes a sophisticated **installer or loader (dropper)**. It is designed to manage complex installation routines, handle various file system scenarios (such as network shares and different drive types), and execute secondary components while monitoring their execution status.

The presence of heavy path-parsing logic, environment variable expansion, and the use of standard installer-related libraries suggests it is intended to unpack or install a software package (which could be legitimate or malicious).

### Core Functionality
*   **Complex Path Resolution:** The code contains extensive logic (`fcn.140006768`, `fcn.1400041ec`) to parse file paths, handle quoted strings, expand environment variables (like `%SystemRoot%`), and determine if a path is a local drive or a network share (UNC).
*   **Environment Awareness:** It checks for specific system versions (`GetVersionExA`), hardware architecture, and regional settings via the Registry. 
*   **Secondary Process Execution:** It uses `CreateProcessA` to launch other components (`fcn.140007010`) and waits for them to finish before proceeding based on their exit codes.
*   **Resource Management:** The code utilizes `LoadResource` and `LockResource` (associated with the "CABINET" string) to load internal data or configuration files used during the setup process.

### Suspicious or Malicious Behaviors
*   **Persistence Mechanism:** 
    *   The code specifically interacts with the `RunOnce` registry key (`Software\Microsoft\Windows\CurrentVersion\RunOnce`). This is a classic technique for installers to ensure that actions (like further unpacking or system modifications) are performed automatically after a reboot.
*   **Process Orchestration:** 
    *   The logic of launching a process and immediately waiting for its exit code suggests it may be "chaining" different pieces of malware together (e.g., dropping one component, ensuring it runs successfully, then moving to the next).
*   **File System Manipulation:** 
    *   It performs automated directory creation and permission checking (`fcn.14000521c`, `fcn.140005810`). If a folder doesn't exist or is not accessible, it attempts to create the path or change its attributes to ensure subsequent files can be dropped.
    *   The routine in `fcn.1400026b8` iterates through directories and deletes temporary files/folders after use, which is common for "cleaning up" traces of a drop sequence.

### Notable Techniques & Patterns
*   **Robust Path Handling:** The implementation of path parsing (handling quotes, backslashes, and nested variables) is quite robust. While common in legitimate installers (like those using InstallShield), this level of detail is also utilized by high-quality malware to ensure it can run correctly across different user environments.
*   **Dynamic Linking/Resolution:** The use of `GetProcAddress` and `LoadLibraryA` for core functions suggests an attempt to delay the binding of certain capabilities or to hide specific API calls from simple static analysis.
*   **User Interaction via Shell:** It uses `SHELL32.dll` (via `SHBrowseForFolder`) to allow the user to select a destination directory, which is typical in "interactive" installers.
*   **Error Handling & Feedback:** The code includes extensive error handling and uses `MessageBoxA` to notify the user or log errors during the installation/extraction process.

### Summary of Findings
The sample appears to be an **installer-style loader**. It is designed to navigate complex system environments, manage files across different drives (including network paths), and execute secondary components in a controlled sequence. 

**Primary concerns for further investigation:**
1.  Identify the payload launched via `CreateProcessA` in `fcn.140007010`.
2.  Inspect the data being read from the "CABINET" resource to determine what is being unpacked.
3.  Monitor the specific files and registry keys modified during the `RunOnce` logic.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys | The analysis identifies the use of the `RunOnce` registry key as a persistence mechanism to ensure tasks are performed after a restart or login. |
| **T1137** | Dynamic Resolution | The use of `GetProcAddress` and `LoadLibraryA` is used to resolve functions at runtime, which can hide API calls from static analysis. |
| **T1070.004** | Indicator Removal: File Deletion | The code includes specific logic to delete temporary files and folders after use to "clean up" traces of the activity. |
| **T1520** | Software Packing | The use of `LoadResource` and the "CABINET" string indicates the inclusion/unpacking of data or additional components within a single executable. |
| **T1059** | Command and Scripting Interpreter | (Implicit) The creation of a process chain via `CreateProcessA` to execute orchestrated commands is characteristic of installer-style loaders and droppers. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Identified as a persistence mechanism in the analysis)
*   `wininit.ini` (Potential configuration file/artifact)
*   `msdownld.tmp` (Temporary file artifact)
*   `TMP4351$.TMP` (Specific temporary filename)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Resource Identifier:** `CABINET` (Used as a resource type for loading internal data/payloads).
*   **Execution Pattern:** Use of "chained" process execution via `CreateProcessA` to sequence different components.
*   **Technique Identification:** Intentional use of `GetProcAddress` and `LoadLibraryA` to dynamically resolve functions (Potential evasion of static analysis).

---
**Analyst Note:** The sample functions as a sophisticated loader/installer. While many of the strings provided are standard Windows API calls or common library names (e.g., `advapi32.dll`, `GetProcAddress`), the most significant indicators for tracking this specific threat are the usage of the **RunOnce** registry key for persistence and the specific naming conventions of the temporary files (**msdownld.tmp**, **TMP4351$.TMP**) used during the unpacking sequence.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Sophisticated Staging Behavior:** The sample exhibits classic "dropper" characteristics by utilizing `LoadResource` (with the "CABINET" identifier) and a chained execution model via `CreateProcessA`, designed to unpack, install, and manage secondary components in a controlled sequence.
    *   **Evasion and Persistence Techniques:** The use of dynamic API resolution (`GetProcAddress`/`LoadLibraryA`) to hide functionality from static analysis, combined with the exploitation of the `RunOnce` registry key for persistence, indicates an intent to establish a foothold while hiding its true payload.
    *   **Automated Environment Management:** Extensive logic for path parsing, directory creation, and temporary file cleanup (e.g., `msdownld.tmp`) highlights a professional-grade installer framework designed to ensure the "payload" executes successfully across various system configurations.
