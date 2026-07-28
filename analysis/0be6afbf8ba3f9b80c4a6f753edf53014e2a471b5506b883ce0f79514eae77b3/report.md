# Threat Analysis Report

**Generated:** 2026-07-27 22:49 UTC
**Sample:** `0be6afbf8ba3f9b80c4a6f753edf53014e2a471b5506b883ce0f79514eae77b3_0be6afbf8ba3f9b80c4a6f753edf53014e2a471b5506b883ce0f79514eae77b3.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0be6afbf8ba3f9b80c4a6f753edf53014e2a471b5506b883ce0f79514eae77b3_0be6afbf8ba3f9b80c4a6f753edf53014e2a471b5506b883ce0f79514eae77b3.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 1,797,712 bytes |
| MD5 | `781626e73981679ba86af1ccd26a7a46` |
| SHA1 | `376c185fb4cda44f96948671f57555a66cf9dccf` |
| SHA256 | `0be6afbf8ba3f9b80c4a6f753edf53014e2a471b5506b883ce0f79514eae77b3` |
| Overall entropy | 7.754 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1453275839 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.096 | No |
| `.rdata` | 9,216 | 4.728 | No |
| `.data` | 1,024 | 3.189 | No |
| `.pdata` | 1,536 | 3.156 | No |
| `.rsrc` | 1,742,336 | 7.775 | ⚠️ Yes |
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

Total strings found: **4079** (showing first 100)

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

Based on the provided disassembly and decompiled code, here is a technical analysis of the binary's behavior.

### Core Functionality and Purpose
The binary functions as a **sophisticated "installer" or "downloader" (dropper)**. It is designed to extract content from an internal package (likely a Cabinet/CAB file), install components on the system, manage process execution, and ensure persistence. The code structure indicates it handles common installer tasks like checking disk space, validating paths, and managing system resources, but it does so using techniques frequently seen in malware loaders.

### Suspoded or Malicious Behaviors

*   **Persistence via Registry Manipulation:**
    *   The function `fcn.1400061ec` specifically interacts with the `Software\Microsoft\Windows\CurrentVersion\RunOnce` registry key. 
    *   It also references and checks `PendingFileRenameOperations`. This is a common technique for malware to ensure that a payload is executed with high privileges or at a specific time during/after system reboot.
*   **Automated File Manipulation & Cleanup:**
    *   In several functions (notably `fcn.1400061ec` and `fcn.14000204c`), the code iterates through files, changes their attributes to **hidden/system** (`SetFileAttributesA(..., 0x80)`), and then calls `DeleteFileA`.
    *   This behavior is characteristic of a "cleaner" routine used by droppers to remove evidence of installation or to replace legitimate files with malicious ones.
*   **Payload Extraction (Cabinet/Drop Logic):**
    *   The use of `Cabinet.dll` and functions like `FDICreate` and `FDICopy` suggest the binary extracts a payload from an internal archive. 
    *   A specific internal reference, `*MEMCAB`, suggests it handles a memory-resident or compressed "cabinet" to drop additional components onto the system.
*   **System/Environment Surveying:**
    *   The code performs detailed checks on the operating system's version (`GetVersionExA`), system locale (via `fcn.140007f04`), and disk space availability. 
    *   While common in installers, these are often used by malware to fingerprint the environment or ensure it is not running in a sandbox/vm with limited resources.

### Notable Techniques & Patterns

*   **Process Orchestration:** The use of `CreateProcessA` followed by `WaitForSingleObject` and `GetExitCodeProcess` (in `fcn.14000473c`) indicates it manages the lifecycle of child processes, likely ensuring a payload is successfully launched before continuing or exiting.
*   **Resource & Registry Abuse:** It utilizes standard Windows utilities like `RunOnce` and `PendingFileRenameOperations` not just for installation, but as reliable methods to trigger actions outside the immediate context of the initial execution.
*   **Advanced Path Handling:** Functions like `fcn.1400070a8` show complex logic for handling quoted paths, drive letters, and network shares, ensuring it can successfully navigate various file system structures to place its components.
*   **Self-Deletion/Cleanup Trait:** The routine of "hiding" a file before deleting it is a classic technique used by malware to ensure that even if the deletion fails or the system warns the user, the files remain hidden from standard view.

### Summary Table of Indicators
| Feature | Evidence / Function | Risk Level |
| :--- | :--- | :--- |
| **Persistence** | `RunOnce` key manipulation in `fcn.1400061ec` | High |
| **File Manipulation** | Hidden attribute setting & deletion in `fcn.14000204c` | Medium/High |
| **Payload Drop** | `Cabinet.dll` usage and `FDICopy` for extraction | High |
| **Environment Check** | Versioning, locale, and disk space checks | Low (Common) |
| **Process Management** | Wait-for-exit on child processes in `fcn.14000473c` | Medium |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1546 | Persistence | The use of the `RunOnce` registry key and `PendingFileRenameOperations` ensures that the payload is executed automatically upon system reboot or at a specific time. |
| T1564 | Hide Files and Directories | The application explicitly sets file attributes to "hidden" and "system" (`0x80`) before deletion to conceal its activities from standard user view. |
| T1036 | Masquerading | The binary uses common installer behaviors, such as Cabinet (CAB) extraction and environment checks, to blend in with legitimate software installation processes. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Registry Key used for persistence)
*   `PendingFileRenameOperations` (Registry key/mechanism used for high-privilege execution)
*   `wininit.ini` (Potential dropped file name)
*   `IXP%03d.TMP`, `msdownld.tmp`, `TMP4351$.TMP` (Temporary file names used during unpacking/extraction)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Internal Identifiers:** `MEMCAB` (Associated with internal cabinet handling and payload extraction).
*   **File Naming Patterns:** `UPDFILE%lu` (Pattern used to generate temporary file names).
*   **Extraction Logic:** Use of `Cabinet.dll`, `FDICreate`, and `FDICopy` for extracting payloads from embedded resources.
*   **Persistence/Stealth Behavior:** Utilization of the `0x80` attribute (Hidden/System) via `SetFileAttributesA` before performing deletion to obscure file presence during the dropping process.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Payload Extraction Mechanics:** The use of `Cabinet.dll` (specifically `FDICreate` and `FDICopy`) combined with the internal identifier `MEMCAB` confirms the binary's primary role is to unpack and extract additional components from a hidden archive into the filesystem.
*   **Persistence and Privilege Escalation:** The interaction with `RunOnce` registry keys and `PendingFileRenameOperations` are classic techniques used by loaders to ensure that the secondary payload executes with high privileges or survives system reboots.
*   **Evasion and Stealth Tactics:** The routine of setting file attributes to "Hidden/System" (`0x80`) before performing deletions indicates a deliberate attempt to hide its tracks from both the user and standard system monitoring tools during the installation process.
