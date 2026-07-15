# Threat Analysis Report

**Generated:** 2026-07-12 09:45 UTC
**Sample:** `04fae87ad99118b414439853eb0950d62a0b37bb7ef62c9bfe40fbe70c5dc00e_04fae87ad99118b414439853eb0950d62a0b37bb7ef62c9bfe40fbe70c5dc00e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04fae87ad99118b414439853eb0950d62a0b37bb7ef62c9bfe40fbe70c5dc00e_04fae87ad99118b414439853eb0950d62a0b37bb7ef62c9bfe40fbe70c5dc00e.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 2,334,720 bytes |
| MD5 | `b8aa3afaa82d3475f95bd5e6408f5ba2` |
| SHA1 | `09cb3b39bd1bc0b2e224d18728594cfae3d0c3b0` |
| SHA256 | `04fae87ad99118b414439853eb0950d62a0b37bb7ef62c9bfe40fbe70c5dc00e` |
| Overall entropy | 7.704 |
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
| `.rsrc` | 2,273,280 | 7.747 | ⚠️ Yes |
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

Total strings found: **4166** (showing first 100)

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

Based on the provided disassembly and strings, this binary is a **sophisticated installer/dropper** designed to deploy and manage additional components or payloads on a Windows system. It exhibits several behaviors typical of "packer" or "loader" malware that acts as an initial stage for a larger infection.

### Core Functionality and Purpose
The code functions as a wrapper and installation engine. It handles:
*   **Installation Logic:** Using internal routines to parse settings, check hardware/OS compatibility (via `GetSystemInfo` and `GetVersion`), and manage the "installation" flow (referencing strings like `REBOOT`, `FINISHMSG`, and `INSTALL`).
*   **Resource Extraction:** The presence of "Cabinet" related logic suggests it extracts embedded resources or files from its own binary to a temporary location for execution.
*   **Environment Validation:** It checks system environment variables, directory permissions (via `GetFileAttributesA`), and disk space before attempting to unpack or move files.

### Suspicious and Malicious Behaviors
The following behaviors are highly indicative of malware:

*   **Persistence via Registry Manipulation:** 
    *   Functions like `fcn.140001a08` specifically target the **"RunOnce"** registry key (`Software\Microsoft\Windows\CurrentVersion\RunOnce`). This is a classic technique to ensure that a payload is executed during the next reboot or shortly after the current process finishes, allowing the malware to "stay" on the system.
*   **Persistence/Installer-like Behavior:** 
    *   The code includes logic for `DelNodeRunDLL32` and interacts with common setup APIs (e.g., `setupapi.dll`, `advapi32.dll`). While common in legitimate installers, it is frequently used by malware to provide a "clean" installation of malicious drivers or services.
*   **Anti-Analysis & Anti-Debugging:** 
    *   **Mutex Creation:** The use of `CreateMutexA` (e.g., in `fcn.140005810`) is commonly used by malware to ensure only one instance of the loader/dropper is running at a time, preventing multiple processes from alerting security software or interfering with each other.
    *   **Heap Protection:** The call to `HeapSetInformation` (via related internals) can be used to influence how memory behaves during analysis or to bypass certain integrity checks.
*   **File Manipulation and Cleanup:** 
    *   Function `fcn.1400026b8` iterates through files, potentially checking for script files (`.BAT`) or system files (`.INF`). It specifically manipulates file attributes (e.g., setting them to "hidden" or "system") before deleting or moving them—a common tactic to hide evidence of the installation process.
*   **System Information Gathering:** 
    *   The binary gathers high-level details about the environment (`GetSystemDirectoryA`, `GetWindowsDirectoryA`). This is often performed by malware to determine if it's running in a virtual machine or on a specific target (e.g., looking for "System32" to inject DLLs).

### Notable Techniques & Patterns
*   **Multi-Stage Execution:** The code structure suggests the first binary (this one) only prepares the ground, while subsequent files are extracted and executed using standard Windows tools like `ShellExecute` or by being dropped into the `RunOnce` path.
*   **Polymorphic/Dynamic Path Handling:** Functions like `fcn.140002d34` and `fcn.140006768` perform complex string parsing to handle environment variables and relative paths, ensuring the malware can operate correctly regardless of where it is unpacked on the disk.
*   **Use of Internal APIs:** The heavy use of internal-looking names (e.g., `fcn.14000...`) and custom mapping for WinAPI calls suggest that the original source was heavily modified or wrapped to obscure its intent from automated scanners.

### Summary Table for Report
| Behavior | Identified Code/Evidence | Threat Level |
| :--- | :--- | :--- |
| **Persistence** | `RunOnce` Registry keys, `advapi32` manipulation | High |
| **Installation Logic** | Cabinet support, Setup API usage, Reboot handling | Medium (Wrapper) |
| **Anti-Analysis** | Mutex creation, Heap info adjustment | Medium |
| **File Manipulation** | `.bat`/`.inf` detection, attribute modification | Medium |
| **Environment Check** | `GetSystemDirectoryA`, Version checking | Low/Medium |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys | The binary specifically targets the "RunOnce" registry key to ensure that payloads are executed upon reboot or after the installer completes. |
| T1059 | Command and Scripting Interpreter | The inclusion of logic to detect and prepare `.bat` files indicates a multi-stage execution model using script interpreters. |
| T1106 | Native API | The heavy use of WinAPI (e.g., `GetSystemInfo`, `GetVersion`, `GetFileAttributesA`) for environment profiling and attribute manipulation is a hallmark of this technique. |
| T1547 | Persistence | The overall behavior of the "installer/dropper" to establish a foothold via registry keys and multi-stage execution confirms this tactic. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Standard Windows system calls (e.g., `GetSystemDirectoryA`, `LoadLibraryA`) and generic paths have been omitted as they are considered common environment artifacts rather than specific indicators of malicious intent.

### **IP addresses / URLs / Domains**
*   *(None identified)*

### **File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Used for persistence)
*   `IXP%03d.TMP` (Temporary file creation pattern)
*   `msdownld.tmp` (Temporary file name)
*   `TMP4351$.TMP` (Temporary file name)

### **Mutex names / Named pipes**
*   *(None identified - only the API `CreateMutexA` was referenced in behavior, but no specific mutex string was provided.)*

### **Hashes**
*   *(No hashes were present in the provided strings.)*

### **Other artifacts**
*   **Persistence Mechanism:** Usage of `RunOnce` registry key to execute payloads during subsequent reboots.
*   **Anti-Analysis / Evasion:** Use of `CreateMutexA` and `HeapSetInformation` to control execution flow and mitigate analysis impacts.
*   **File Manipulation:** Detection and modification of file attributes (e.g., hiding them) for `.bat` and `.inf` files prior to movement or deletion.
*   **Loader Behavior:** 
    *   Utilization of `advapi32.dll`, `setupapi.dll`, and `advpack.dll` to mimic legitimate installer behavior.
    *   "Cabinet" (CAB) logic used for extracting embedded resources/payloads from the primary binary.
*   **Tactic - Persistence via Installer:** Use of `DelNodeRunDLL32` to manipulate system services or drivers during the installation phase.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family:** custom
2. **Malware type:** dropper / loader
3. **Confidence:** High
4. **Key evidence:**
    *   **Multistage Deployment Logic:** The binary functions as a wrapper/installer that utilizes "Cabinet" extraction logic and multi-stage execution to deploy secondary payloads while hiding their presence by modifying file attributes (e.g., `.bat` and `.inf` files).
    *   **Persistence Mechanisms:** It actively manipulates the `RunOnce` registry key and utilizes standard installation APIs (`setupapi.dll`, `advapi32.dll`) to ensure its components persist across reboots.
    *   **Evasion Tactics:** The use of `CreateMutexA` for instance control, `HeapSetInformation` to evade analysis tools, and internal API mapping suggests a sophisticated attempt to bypass security software while preparing the environment for subsequent malware stages.
