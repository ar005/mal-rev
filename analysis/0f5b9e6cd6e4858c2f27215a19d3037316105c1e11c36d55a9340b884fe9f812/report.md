# Threat Analysis Report

**Generated:** 2026-08-15 22:35 UTC
**Sample:** `0f5b9e6cd6e4858c2f27215a19d3037316105c1e11c36d55a9340b884fe9f812_0f5b9e6cd6e4858c2f27215a19d3037316105c1e11c36d55a9340b884fe9f812.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f5b9e6cd6e4858c2f27215a19d3037316105c1e11c36d55a9340b884fe9f812_0f5b9e6cd6e4858c2f27215a19d3037316105c1e11c36d55a9340b884fe9f812.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 1,906,176 bytes |
| MD5 | `489410003345faf4f67503fca615e8cb` |
| SHA1 | `213f9b2ebcb300f7742fad36fef0ade71f53abc4` |
| SHA256 | `0f5b9e6cd6e4858c2f27215a19d3037316105c1e11c36d55a9340b884fe9f812` |
| Overall entropy | 7.711 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1436959553 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.096 | No |
| `.rdata` | 9,216 | 4.728 | No |
| `.data` | 1,024 | 3.189 | No |
| `.pdata` | 1,536 | 3.156 | No |
| `.rsrc` | 1,861,120 | 7.733 | ⚠️ Yes |
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

Total strings found: **4003** (showing first 100)

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

The provided disassembly and decompiled code describe the functionality of a **software installer or uninstaller component**. While many of these behaviors are common in legitimate installation software, they are also frequently observed in "droppers" or malware that masquerides as installers to establish persistence and clean up traces.

### Core Functionality
The code appears to manage the lifecycle of an application by interacting with system configuration, managing file paths, and performing cleanup operations. It uses several standard Windows API calls to ensure that files are correctly moved or deleted and that "installation" states are updated in the registry.

### Suspicious & Notable Behaviors

*   **Persistence via Registry (RunOnce):**
    *   The function `fcn.140001d28` specifically targets the registry key: `Software\Microsoft\Windows\CurrentVersion\RunOnce`. 
    *   It attempts to read and set values within this key, which is a common technique to ensure that an action (like completing a setup or running a cleanup) happens automatically after the next user login.

*   **System-Level File Operations:**
    *   The code interacts with `Session Manager\FileRenameOperations` and `PendingFileRenameOperations`. These are typically used by Windows installers to handle file renames that require a system reboot (e.g., replacing system files). 
    *   In a malware context, these keys are often manipulated to replace legitimate system files with malicious ones during the next boot cycle.

*   **Evasive File Manipulation:**
    *   In `fcn.1400061ec` and `fcn.14000204c`, the code iterates through a list of files or paths, applies attributes (like `FILE_ATTRIBUTE_HIDDEN` / 0x80) before performing deletion (`DeleteFileA`).
    *   The use of `SetFileAttributesA` to hide a file immediately before deleting it is a common technique to avoid detection by the user during a "clean-up" or "uninstallation" phase.

*   **Environment Awareness & Context Gathering:**
    *   Several functions (`fcn.1400064e4`, `fcn.140007f04`) perform checks on system architecture, current directory paths, and system metrics (e.g., `GetSystemMetrics`). 
    *   The code also dynamically loads libraries like `advapi32.dll` and searches for specific functions (like `DelNodeRunDLL32`), which is common in complex installers to determine environment capabilities.

*   **Execution of External Processes:**
    *   Function `fcn.14000473c` uses `CreateProcessA` to launch other components or secondary processes, and then waits for them to complete (`WaitForSingleObject`). This is typical in "dropper" behavior where a first-stage executable launches the main malicious payload.

### Summary of Indicators
| Category | Observation | Technical Detail |
| :--- | :--- | :--- |
| **Persistence** | `RunOnce` Registry Key | Manipulation of `Software\Microsoft\Windows\CurrentVersion\RunOnce`. |
| **Stealth** | Attribute Manipulation | Setting file attributes to "Hidden" before deletion. |
| **System Interaction** | Pending Operations | Accessing `PendingFileRenameOperations` and `FileRenameOperations`. |
| **File/Dir Cleanup** | Iterative Deletion | Searching for files in specific paths and removing them recursively. |
| **Deployment** | Process Spawning | Usage of `CreateProcessA` to execute child processes from a command line. |

### Conclusion
The binary exhibits behaviors consistent with an **installer or uninstaller suite**. The primary indicators of concern are the manipulation of "Pending" operations and the use of `RunOnce`. While these are standard in `.msi` or `.exe` installers, they are also classic maneuvers for malware to facilitate file replacement and maintain presence on a system.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | The utilization of the `RunOnce` registry key is a direct method to ensure execution during the subsequent login session. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | Manipulation of `PendingFileRenameOperations` ensures that file replacements are committed during the boot cycle, providing persistence for modified system files. |
| **(Defense Evasion)** | Defense Evasion | Applying the `FILE_ATTRIBUTE_HIDDEN` attribute before deletion is used to conceal file activity from users and automated security tools. |
| **T1610** | System Information Discovery | The collection of system architecture, metrics, and directory paths provides context for the application (or malware) to determine its behavior. |
| **T1059** | Command and Scripting Interpreter | The use of `CreateProcessA` to launch secondary processes is a standard mechanism for "droppers" to transition from initial execution to payload deployment. |

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None found)*

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Persistence mechanism)
*   `Session Manager\FileRenameOperations` (System file manipulation/bypass)
*   `PendingFileRenameOperations` (System file manipulation/bypass)

**Mutex names / Named pipes**
*   *(None found)*

**Hashes**
*   *(None found)*

**Other artifacts**
*   **Behavioral - Evasion:** Use of `SetFileAttributesA` with the `FILE_ATTRIBUTE_HIDDEN` (0x80) attribute prior to file deletion.
*   **Behavioral - Dropper Activity:** Execution of child processes via `CreateProcessA` followed by a wait state (`WaitForSingleObject`), typical of first-stage malware loaders.
*   **Potential Temporary Files:** 
    *   `IXP%03d.TMP` (Pattern for temporary installation files)
    *   `msdownld.tmp`

---

## Malware Family Classification

1. **Malware family:** Unknown
2. **Malware type:** Dropper / Loader
3. **Confidence:** High (for Type) / Low (for Family)

4. **Key evidence:**
*   **Staged Execution & Persistence:** The use of `CreateProcessA` to launch subsequent components and the manipulation of the `RunOnce` registry key are classic hallmarks of a first-stage loader or dropper intended to establish a foothold.
*   **Evasive File Manipulation:** The deliberate application of the `FILE_ATTRIBUTE_HIDDEN` flag prior to deletion and the use of `PendingFileRenameOperations` indicate an attempt to hide malicious activity and replace system files during the boot cycle—tactics commonly used by installers to bypass detection or ensure persistence.
*   **Masquerading Behavior:** The analysis highlights that while the behavior mimics a standard installer suite, these specific techniques (hiding files, staged execution, and registry manipulation) are primary indicators of malicious "dropper" functionality designed to deliver a secondary payload.
