# Threat Analysis Report

**Generated:** 2026-07-09 17:58 UTC
**Sample:** `041214997b5ba9f3b344f660d1ab8542b76473538ebc593f78abfd8cee72b7a5_041214997b5ba9f3b344f660d1ab8542b76473538ebc593f78abfd8cee72b7a5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `041214997b5ba9f3b344f660d1ab8542b76473538ebc593f78abfd8cee72b7a5_041214997b5ba9f3b344f660d1ab8542b76473538ebc593f78abfd8cee72b7a5.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 2,966,144 bytes |
| MD5 | `30ce1e4b80da8ded9cdde1be65c2fbd3` |
| SHA1 | `5c0a732f1ae17ba470e049689ddb63424aa5f6bf` |
| SHA256 | `041214997b5ba9f3b344f660d1ab8542b76473538ebc593f78abfd8cee72b7a5` |
| Overall entropy | 6.746 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1412548675 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.096 | No |
| `.rdata` | 9,216 | 4.728 | No |
| `.data` | 1,024 | 3.189 | No |
| `.pdata` | 1,536 | 3.156 | No |
| `.rsrc` | 2,920,448 | 6.742 | No |
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

Total strings found: **4807** (showing first 100)

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

### **Malware Analysis Report**

#### **Core Functionality and Purpose**
The binary appears to be a sophisticated **installer or dropper**. It is designed to prepare the host system for the installation of additional components by performing environment checks, escalating/verifying privileges, and extracting files from an embedded payload.

It utilizes standard Windows installer-related APIs (like `Cabinet.dll` and `SetupAPI.dll`), which is a common technique used by malware to blend in with legitimate software setup routines.

---

#### **Suspicious or Malicious Behaviors**

*   **Persistence Mechanisms:**
    *   **RunOnce Registry Key:** The code explicitly interacts with `Software\Microsoft\Windows\CurrentVersion\RunOnce`. While commonly used by installers, it is a primary method for malware to ensure its components are executed immediately after the next user login.
    *   **File Rename Operations:** Function `fcn.140002318` specifically targets `PendingFileRenameOperations`. This is a highly significant indicator; it is used by the system to move/replace files during a reboot. Malware uses this to replace system files or ensure persistence after a reboot.
    *   **DelNodeRunDLL32:** The inclusion of logic to interact with "Delete Node" routines suggests an attempt to clean up local traces or modify execution paths.

*   **Privilege Escalation/Check:**
    *   **Token Analysis:** Function `fcn.1400012ec` calls `OpenProcessToken` and `GetTokenInformation` followed by `EqualSid`. This is used to check if the process has specific privileges (likely Administrator or SYSTEM) before proceeding with potentially disruptive actions like modifying System keys.

*   **Payload Extraction:**
    *   **Cabinet API Usage:** The code uses `FDICreate` and `FDICopy` from `Cabinet.dll` in function `fcn.14000518`. This indicates the binary contains a compressed or encapsulated "cabinet" file (or similar structure) that it extracts into the local file system during execution.

*   **Environment Preparation:**
    *   **Path Construction/Validation:** Functions like `fcn.1400070a8` and `fcn.1400064e4` perform extensive checks on directory paths (handling temp folders, checking for "T" or "S" indicators). This ensures the malware has a valid path to unpack its components.
    *   **Automatic Directory Creation:** The code iterates through strings to build file paths and automatically creates missing parent directories using `CreateDirectoryA`.

---

#### **Notable Techniques & Patterns**

*   **Installer Masking (Living off the Land):** By utilizing `Cabinet.dll`, `SetupAPI.dll`, and `RunOnce` keys, the malware mimics a standard software installer. This is a common evasion tactic to avoid detection by automated heuristic scanners that flag "malicious" behavior like file copying or registry modification when performed via well-known Windows setup APIs.
*   **Heavy String/Path Processing:** The code contains several loops for validating and normalizing paths. This suggests it can handle complex path logic (e.g., environmental variables, different drive letters) to ensure the payload is placed in a consistent location regardless of user configuration.
*   **Resource Loading:** It references `FindResourceA` and `LoadResource` with identifiers like "VERCHECK" and "CABINET," indicating that the core malicious components are embedded within the binary's resource section rather than being downloaded over the network initially (a common anti-network-detection tactic).
*   **Mutex Creation:** The use of `CreateMutexA` is a standard technique to ensure that only one instance of the dropper/installer is running at any given time, preventing race conditions during the extraction process.

### **Summary Summary for Incident Response**
The binary's primary role is as a **dropper**. It performs privilege checks and environment validation before using legitimate Windows "Cabinet" logic to unpack an embedded payload onto the local disk. The presence of `PendingFileRenameOperations` and `RunOnce` keys strongly suggests it intends to establish persistence on the host machine immediately following execution or upon reboot.

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Registry Run Keys / Startup Folder | The use of the `RunOnce` registry key is a standard method for ensuring malicious components execute upon user login. |
| **T1036** | Masquerading | Utilizing common Windows installer APIs (`Cabinet.dll`, `SetupAPI.dll`) and performing privilege checks allows the malware to blend in with legitimate system activities. |
| **T1027** | Obfuscated Files or Information | The use of `Cabinet` structures and internal resource loading hides the payload within the binary, concealing it from basic scanners. |
| **T1070** | Indicator Removal on Host | The "Delete Node" routine indicates an attempt to remove local traces or cleanup evidence of the malware's presence. |

### **Analysis Notes for Incident Response:**
*   **Persistence:** While `PendingFileRenameOperations` does not have a unique sub-technique ID in MITRE, it is a high-confidence indicator of persistence intended to ensure file replacements survive system reboots.
*   **Detection Gap:** The heavy reliance on "Installer Masking" (T1036) suggests that traditional signature-based detection may be bypassed; behavioral monitoring for `Cabinet.dll` calls in non-standard installer paths is recommended.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\App Paths` (Registry Key)
*   `Control Panel\Desktop\ResourceLocale` (Registry Key)
*   `PendingFileRenameOperations` (System/Registry key used for persistence and file replacement)
*   `wininit.ini` (Potential configuration file)
*   `TMP4351$.TMP` (Temporary file artifact)
*   `msdownld.tmp` (Temporary file artifact)
*   `ixp%03d.TMP` (Template for temporary files used during extraction)

**Mutex names / Named pipes**
*   None identified (While `CreateMutexA` is mentioned in behavior, no specific mutex name was provided in the strings).

**Hashes**
*   None identified.

**Other artifacts**
*   **Technique: Installer Masquerading:** The binary utilizes `Cabinet.dll`, `SetupAPI.dll`, and `RunOnce` registry keys to blend in with legitimate software installation routines.
*   **Persistence Strategy:** Use of the `PendingFileRenameOperations` mechanism to ensure persistence or file replacement upon system reboot.
*   **Internal Labels:** "VERCHECK", "CABINET", "REBOOT", "RUNPROGRAM", "POSTRUNPROGRAM" (Used for internal logic control within the dropper).
*   **Evidence of Extraction:** Use of `FDICreate` and `FDICopy` from `Cabinet.dll` indicates an embedded payload is being unpacked to the local file system.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Payload Extraction & Masking:** The binary utilizes `Cabinet.dll` and `SetupAPI.dll` to unpack an embedded "cabinet" payload, a technique specifically designed to hide malicious components within standard Windows installation routines.
*   **Persistence Mechanisms:** The use of `PendingFileRenameOperations` (to ensure execution/file replacement after reboot) and `RunOnce` registry keys indicates a clear intent to establish long-term presence on the host system.
*   **Privilege & Environment Validation:** The code performs explicit checks for high-level permissions (`GetTokenInformation`) and conducts heavy path validation, ensuring it has the necessary environment to successfully deploy its payload.
