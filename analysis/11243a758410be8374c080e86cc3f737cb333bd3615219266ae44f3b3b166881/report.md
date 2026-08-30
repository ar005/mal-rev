# Threat Analysis Report

**Generated:** 2026-08-22 18:39 UTC
**Sample:** `11243a758410be8374c080e86cc3f737cb333bd3615219266ae44f3b3b166881_11243a758410be8374c080e86cc3f737cb333bd3615219266ae44f3b3b166881.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11243a758410be8374c080e86cc3f737cb333bd3615219266ae44f3b3b166881_11243a758410be8374c080e86cc3f737cb333bd3615219266ae44f3b3b166881.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 1,701,968 bytes |
| MD5 | `6d19860eeacd344b7a262a7575d64ad8` |
| SHA1 | `9df20290d8634e11113dfcf0cf4581bffae2a95b` |
| SHA256 | `11243a758410be8374c080e86cc3f737cb333bd3615219266ae44f3b3b166881` |
| Overall entropy | 7.66 |
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
| `.rsrc` | 1,630,208 | 7.721 | ⚠️ Yes |
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

Total strings found: **3966** (showing first 100)

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

Based on the disassembly provided, this binary functions as a **sophisticated "dropper" or "installer."** It is designed to prepare a system for further payloads by performing environment checks, establishing persistence, and managing the execution of secondary components while attempting to hide its tracks.

### Core Functionality
The code acts as a staging component. Rather than executing a single payload, it performs several high-level tasks:
*   **Configuration Parsing:** It processes internal resources (e.g., `RUNPROGRAM`, `POSTRUNPROGRAM`) and extracts configuration details to determine what should be installed or executed next.
*   **Environment Validation:** The code heavily interacts with system information (`GetSystemDirectoryA`, `GetWindowsDirectoryA`, `GetVersionExA`). This is used to ensure the environment meets specific criteria before proceeding.
*   **Resource Management:** It uses a robust internal infrastructure (e.g., `fcn.1400061e8`) to load strings and handle UI elements like MessageBoxes for error handling or "success" prompts.

### Suspicious & Malicious Behaviors
The following features are indicative of malicious intent, common in high-end malware:

*   **Persistence via Registry Manipulation:** 
    *   In `fcn.140001a08`, the code specifically targets the `...\Microsoft\Windows\CurrentVersion\RunOnce` registry key. It retrieves and updates values here to ensure that specific programs are executed automatically during a subsequent login or reboot—a classic method for maintaining persistence while keeping the "installer"'s presence brief.
*   **Process Execution & Payload Loading:** 
    *   The code uses `CreateProcessA` (in `fcn.14000721c`) to launch secondary binaries and uses `LoadLibraryA` / `GetProcAddress` to dynamically load functionality at runtime. This is a common tactic to hide the final stage of an attack from simple static scanners.
*   **Automated Cleanup & Artifact Removal:** 
    *   In `fcn.1400026b8`, the code contains logic to identify and **delete its own source files or temporary artifacts** (such as `.BAT` scripts or original installer components) after execution. This is used to "clean" the system of evidence.
*   **System Manipulation:** 
    *   The inclusion of `DeleteFileA` and `RemoveDirectoryA` in loops, combined with specific logic for file attributes (e.g., checking if a file has been modified), suggests it is actively purging its tracks during the "installation" process.

### Notable Techniques & Patterns
*   **Delayed Execution/Staging:** By using many internal jump tables and long-form logic to check versions (`VERCHECK`) and directory permissions, the code ensures it only performs high-risk actions on confirmed target systems.
*   **String Obfuscation/Indirect Calls:** The use of `GetProcAddress` for common Windows functions (like `DelNodeRunDLL32` as seen in strings) suggests an attempt to bypass security software that monitors standard Import Address Tables (IAT).
*   **Robust Path Handling:** There is significant logic dedicated to resolving relative paths, handling "quoted" paths, and checking disk space (`GetDiskFreeSpaceA`). This indicates the malware is designed to be robust across different user environments.
*   **Dummy/Decoy Logic:** The presence of heavy "installer" logic (handling `INF` files or system-style UI) is often used as a "wrapper" to make the malicious activity appear like legitimate software installation if monitored by an average user.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys/Startup Folder | The binary modifies the `RunOnce` registry key to ensure subsequent components are executed automatically upon login or reboot. |
| T1027 | Obfuscated Files or Information | The use of internal resources for configuration and dynamic loading via `GetProcAddress` indicates an attempt to hide functionality from static analysis. |
| T1497 | Virtualization/Sandbox Evasion | Extensive system information checks (e.g., `GetVersionExA`) are used to determine if the environment meets specific criteria before proceeding with high-risk actions. |
| T1070.004 | Indicator Removal: File Deletion | The code contains logic to identify and delete its own source files, scripts, and temporary artifacts to remove evidence of its presence. |
| T1059 | Command and Scripting Interpreter | The use of `CreateProcessA` is utilized to execute secondary binaries and transition the infection to subsequent stages. |
| T1036.005 | Masquerading: Match Activity Type | The inclusion of "installer" logic and standard UI elements (MessageBoxes) is designed to blend malicious activity with a legitimate software installation process. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\App Paths` (Registry Path)
*   `Control Panel\Desktop\ResourceLocale` (Registry Key)
*   `...\Microsoft\Windows\CurrentVersion\RunOnce` (Targeted Persistence Registry Key)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Temporary File Patterns:** 
    *   `ixp%03d.TMP`
    *   `msdownld.tmp`
    *   `TMP4351$.TMP`
*   **Development Artifacts:** `wextract.pdb` (Leftover Program Database file)
*   **Suspicious Internal Strings/Commands:** 
    *   `DelNodeRunDLL32` (Indicates a specific method for handling executables)
    *   `RUNPROGRAM`
    *   `POSTRUNPROGRAM`
    *   `VERCHECK`
    *   `DecryptFileA`

---

## Malware Family Classification

1. **Malware family:** custom
2. **Malware type:** dropper
3. **Confidence:** High

4. **Key evidence:**
*   **Staged Execution & Persistence:** The binary utilizes `RunOnce` registry keys for persistence and employs `GetProcAddress`/`CreateProcessA` to load and execute secondary components, characterizing a "dropper" designed to hand off the infection to a main payload.
*   **Sophisticated Evasion/Anti-Analysis:** The inclusion of automatic artifact cleanup (deleting `.BAT` scripts and temporary files), environment validation (`GetVersionExA`), and the use of indirect calls for system functions indicates an intentional effort to bypass security software and hide the malware's footprint.
*   **Masquerading as a Legitimate Installer:** The analysis highlights that the binary mimics legitimate installation behavior—such as handling `INF` files, checking disk space, and using standard UI elements—to blend in with normal system activities while executing malicious functions.
