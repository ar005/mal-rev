# Threat Analysis Report

**Generated:** 2026-08-16 15:48 UTC
**Sample:** `0f898d4fcd42e00896c2af2403844dbfdefc56c9bc6f49e07ba2e64fec7f3428_0f898d4fcd42e00896c2af2403844dbfdefc56c9bc6f49e07ba2e64fec7f3428.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f898d4fcd42e00896c2af2403844dbfdefc56c9bc6f49e07ba2e64fec7f3428_0f898d4fcd42e00896c2af2403844dbfdefc56c9bc6f49e07ba2e64fec7f3428.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 2,437,120 bytes |
| MD5 | `2cee5b629187443508ede5a2a1dcef63` |
| SHA1 | `58b643fed3254b5585ea390320101ca96dae5d7a` |
| SHA256 | `0f898d4fcd42e00896c2af2403844dbfdefc56c9bc6f49e07ba2e64fec7f3428` |
| Overall entropy | 7.636 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1411252172 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.096 | No |
| `.rdata` | 9,216 | 4.728 | No |
| `.data` | 1,024 | 3.189 | No |
| `.pdata` | 1,536 | 3.156 | No |
| `.rsrc` | 2,392,064 | 7.653 | ⚠️ Yes |
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

Total strings found: **5287** (showing first 100)

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

Based on the provided disassembly and strings, here is a technical analysis of the binary's behavior:

### Core Functionality
The binary appears to be a **setup wrapper** or an **installer-style dropper**. It contains logic typical of software installation programs, but several components are highly characteristic of malware (specifically droppers) designed to hide malicious payloads and establish persistence.

### Suspicious and Malicious Behaviors

*   **Persistence Mechanism:**
    *   The code frequently interacts with the `RunOnce` registry key (`Software\Microsoft\Windows\CurrentVersion\RunOnce`).
    *   Specifically, functions like `fcn.140001d28` are dedicated to reading from and writing to this key. 
    *   **Why it’s suspicious:** While legitimate installers use "RunOnce" for one-time tasks (like a reboot), malware uses it as a persistence mechanism or to ensure that certain cleanup/installation steps execute automatically upon the next login.

*   **Payload Dropping & Execution:**
    *   Function `fcn.14000473c` utilizes `CreateProcessA`, followed by `WaitForSingleObject` and `GetExitCodeProcess`. 
    *   This pattern is characteristic of a **loader**: the main program launches a secondary process (the actual payload) and waits for it to complete before finishing its own execution.

*   **Resource Extraction & File Manipulation:**
    *   The code utilizes the `Cabinet` API (`Cabinet.dll`) and references "MEMCAB" resources. This is often used to handle compressed internal data or to unpack components from a bundled file.
    *   Function `fcn.140006ca4` performs extensive checks on disk space, directory permissions, and directory creation (using `CreateDirectoryA`). It also handles the construction of file paths for items like `.BAT` and `.INF` files.

*   **Evasive/Anti-Analysis Checks:**
    *   Function `fcn.140007f04` checks system metrics (e.g., `GetSystemMetrics`) and registry values related to regional settings (`ResourceLocale`). 
    *   In a malware context, these checks are often used to determine if the code is running in a "sanitized" environment or a specific target region, or to detect virtual machines/sandboxes.

### Notable Techniques & Patterns

*   **Installer Mimicry:** The binary includes many strings and behaviors typical of an installer (e.g., `setupx.dll`, `advancedinf.dll`, `GetSystemDirectoryA`). This is a common technique used by "droppers" to blend in with legitimate system installers or update tools.
*   **Cleanup Logic:** Function `fcn.1400061ec` performs cleanup of registry keys and files. In malware, this is often used to remove the evidence of other dropped components once they have been successfully executed.
*   **Dynamic Resolution/Internal Handling:** The use of `GetProcAddress` and manual calculation of offsets (e.g., in `fcn.140003f74`) suggests a degree of internal abstraction or an attempt to bypass basic static analysis by not linking everything directly.

### Summary Table
| Feature | Observation | Potential Intent |
| :--- | :--- | :--- |
| **Persistence** | Manipulation of `RunOnce` Registry key | Ensuring the malware/payload runs on restart. |
| **Process Injection**| Use of `CreateProcessA` with a wait loop | Dropping and launching the main payload. |
| **File Management** | Extensive use of Cabinet API & Directory creation | Extracting hidden components from internal resources. |
| **Anti-Analysis** | System metrics and locale validation | Detecting sandboxes or non-target environments. |
| **Stealth/Evasion** | Packaging as a "Setup" tool | Masquerading as a legitimate software installer. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | The binary interacts with the `RunOnce` registry key to ensure that malicious components are executed upon user login or system restart. |
| T1106 | Native API | The use of `CreateProcessA`, `GetProcAddress`, and manual offset calculations indicates an attempt to use native APIs for loader functionality and to bypass basic static analysis. |
| T1497 | Virtualized Environment | The utilization of `GetSystemMetrics` and registry checks for regional settings is a classic method to detect if the code is running in a sandbox or virtual machine. |
| T1036 | Masquerading | The inclusion of installer-specific strings (e.g., `setupx.dll`) allows the malware to blend in with legitimate system installation tools to evade detection. |
| T1070 | Indicator Removal on Host | The specific logic dedicated to cleaning up registry keys and files after execution is intended to remove traces of the intrusion from the local system. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *(None identified in the provided data)*

### **File paths / Registry keys**
*   **Registry Key:** `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Used for persistence)
*   **Registry Key:** `Control Panel\Desktop\ResourceLocale` (Used for environment/anti-analysis checks)
*   **Temporary File Artifacts:**
    *   `msdownld.tmp`
    *   `TMP4351$.TMP`
    *   `IXP%03d.TMP`

### **Mutex names / Named pipes**
*   *(None identified in the provided data)*

### **Hashes**
*   *(None present in the source text)*

### **Other artifacts**
*   **Loader Behavior:** Utilization of `CreateProcessA` followed by `WaitForSingleObject` and `GetExitCodeProcess` to execute a secondary payload.
*   **Extraction Techniques:** Use of the `Cabinet` API and `MEMCAB` resources to unpack/extract internal components (common in droppers).
*   **Installer Mimicry:** The binary uses several "decoy" artifacts to blend with legitimate system installers:
    *   `setupx.dll`
    *   `advancedinf.dll`
    *   `advpack.dll`
    *   `GetSystemDirectoryA` / `GetWindowsDirectoryA` (used for establishing deceptive environment context).
*   **Anti-Analysis Indicators:** Logic specifically targeting regional settings and system metrics to detect sandboxes or non-target environments.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1. **Malware family:** custom
2. **Malware type:** dropper / loader
3. **Confidence:** High
4. **Key evidence:**
    *   **Loader/Dropper Functionality:** The binary utilizes the Cabinet API (`MEMCAB`) to unpack internal components and employs a `CreateProcessA` $\rightarrow$ `WaitForSingleObject` loop, which is a classic signature of a loader designed to execute a secondary payload.
    *   **Installer Mimicry & Evasion:** The sample explicitly uses "decoy" artifacts (e.g., `setupx.dll`, `advancedinf.dll`) to blend in with legitimate software installations, while concurrently using `GetSystemMetrics` and registry checks to detect and evade virtualized or sandboxed analysis environments.
    *   **Persistence Mechanisms:** The intentional manipulation of the `RunOnce` registry key confirms the intent to ensure that components executed by this loader persist across system reboots.
