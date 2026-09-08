# Threat Analysis Report

**Generated:** 2026-09-05 13:40 UTC
**Sample:** `145f510530196c995cbf79bd7d778560c5e24fd2d15a73d17506e94a480b23bf_145f510530196c995cbf79bd7d778560c5e24fd2d15a73d17506e94a480b23bf.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `145f510530196c995cbf79bd7d778560c5e24fd2d15a73d17506e94a480b23bf_145f510530196c995cbf79bd7d778560c5e24fd2d15a73d17506e94a480b23bf.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 238,080 bytes |
| MD5 | `6799a792d2300b35bfc489147492df29` |
| SHA1 | `4a23d48dee34fc58b0494b777f877205b77fa7f0` |
| SHA256 | `145f510530196c995cbf79bd7d778560c5e24fd2d15a73d17506e94a480b23bf` |
| Overall entropy | 7.249 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779493332 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 71,168 | 6.469 | No |
| `.rdata` | 43,008 | 4.88 | No |
| `.data` | 114,688 | 7.962 | ⚠️ Yes |
| `.pdata` | 4,608 | 4.628 | No |
| `_RDATA` | 512 | 1.952 | No |
| `.rsrc` | 1,024 | 3.852 | No |
| `.reloc` | 2,048 | 4.949 | No |

### Imports

**USER32.dll**: `wsprintfA`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `RegOpenKeyExA`, `OpenProcessToken`, `RegCloseKey`, `LookupPrivilegeValueA`, `RegSetValueExA`
**KERNEL32.dll**: `RaiseException`, `WriteConsoleW`, `GetConsoleOutputCP`, `FlushFileBuffers`, `GetModuleFileNameA`, `Process32First`, `WriteProcessMemory`, `GetCurrentProcess`, `WriteFile`, `SetFileTime`, `GetEnvironmentVariableA`, `CreateMutexA`, `WaitForSingleObject`, `GetCurrentThreadId`, `GetModuleHandleA`
**ntdll.dll**: `RtlUnwindEx`, `RtlPcToFileHeader`

## Extracted Strings

Total strings found: **669** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@_RDATA
@.rsrc
@.reloc
L$ SUVWH
@SUVWAVH
A^_^][
UVATAUAVH
A^A]A\^]
 H3E H3E
u0HcH<H
T$uPH
fA;8unI
fA;(t(fA98t
WATAUAVAWH
A_A^A]A\_
WATAUAVAWH
 A_A^A]A\_
ffffff
fffffff
@USVWATAVAWH
D8d$XtH
A_A^A\_^[]
D$@H;G
 t(<#t
<-t
<0uC
<htl<jt\<lt4<tt$<wt
t$ WAVAWH
<Ct-<D
<StW@:
<g~{<itd<ntY<ot7<pt
<utT@:
D<P0@:
k(+sPL
0A_A^_
t98tH
x ATAVAWH
< t=<	t9
 A_A^A\
UVWAVAWH
H9:tH
0A_A^_^]
WAVAWH
0A_A^_
u3HcH<H
t$ WAVAWH
 A_A^_
WAVAWH
 A_A^_
x AUAVAWH
@A_A^A]
@8l$HtH
L$ UVWH
f9
t	H

fA9	t	I
f9
t	H
f9
t	H
WATAUAVAWH
gfffffffH
D8t$htH
A_A^A]A\_
x ATAVAWH
 A_A^A\
fD9t$b
u"8Z(tH
uF8Z(tH
vC8_(tH
u"8Z(tH
uF8Z(tH
vB8_(tH
UVWATAUAVAWH
`A_A^A]A\_^]
WATAUAVAWH
0A_A^A]A\_
H97u+A
\$ UVWATAUAVAWH
,/<-w
H
@8|$HtH
@8|$HtH
@8|$HtH
D$XD9xu
@8|$htH
@8|$htH
@8|$htH
A_A^A]A\_^]
u"8Z(t
v
8_(t
8D$8tH
UVWATAUAVAWH
L$&8\$&t,8Y
@A_A^A]A\_^]
fD94Fu
KxH;z4
@UATAUAVAWH
e0A_A^A]A\]
WATAUAVAWH
 A_A^A]A\_
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140007094` | `0x140007094` | 21124 | ✓ |
| `fcn.140007080` | `0x140007080` | 21084 | ✓ |
| `fcn.14000e4f4` | `0x14000e4f4` | 9841 | ✓ |
| `fcn.140005aa0` | `0x140005aa0` | 5349 | ✓ |
| `fcn.14000d22c` | `0x14000d22c` | 4670 | ✓ |
| `fcn.1400104e4` | `0x1400104e4` | 4373 | ✓ |
| `fcn.140001780` | `0x140001780` | 2170 | ✓ |
| `fcn.14000a084` | `0x14000a084` | 1705 | ✓ |
| `fcn.140003dd0` | `0x140003dd0` | 1685 | ✓ |
| `fcn.1400105b0` | `0x1400105b0` | 1451 | ✓ |
| `fcn.14000208c` | `0x14000208c` | 1409 | ✓ |
| `fcn.14000f5a0` | `0x14000f5a0` | 1260 | ✓ |
| `fcn.14000ce00` | `0x14000ce00` | 1065 | ✓ |
| `fcn.140002030` | `0x140002030` | 1026 | ✓ |
| `fcn.14000eaa0` | `0x14000eaa0` | 937 | ✓ |
| `fcn.14000e660` | `0x14000e660` | 925 | ✓ |
| `fcn.140008404` | `0x140008404` | 896 | ✓ |
| `fcn.140008e10` | `0x140008e10` | 828 | ✓ |
| `fcn.14000ef04` | `0x14000ef04` | 789 | ✓ |
| `fcn.140009d74` | `0x140009d74` | 782 | ✓ |
| `fcn.14000714c` | `0x14000714c` | 770 | ✓ |
| `fcn.140001480` | `0x140001480` | 757 | ✓ |
| `fcn.14000ff08` | `0x14000ff08` | 739 | ✓ |
| `fcn.1400110cc` | `0x1400110cc` | 710 | ✓ |
| `fcn.14000aa64` | `0x14000aa64` | 697 | ✓ |
| `fcn.1400011f0` | `0x1400011f0` | 650 | ✓ |
| `fcn.14000c3b0` | `0x14000c3b0` | 618 | ✓ |
| `fcn.1400050b0` | `0x1400050b0` | 614 | ✓ |
| `fcn.140011ad8` | `0x140011ad8` | 614 | ✓ |
| `fcn.1400065c0` | `0x1400065c0` | 557 | ✓ |

### Decompiled Code Files

- [`code/fcn.1400011f0.c`](code/fcn.1400011f0.c)
- [`code/fcn.140001480.c`](code/fcn.140001480.c)
- [`code/fcn.140001780.c`](code/fcn.140001780.c)
- [`code/fcn.140002030.c`](code/fcn.140002030.c)
- [`code/fcn.14000208c.c`](code/fcn.14000208c.c)
- [`code/fcn.140003dd0.c`](code/fcn.140003dd0.c)
- [`code/fcn.1400050b0.c`](code/fcn.1400050b0.c)
- [`code/fcn.140005aa0.c`](code/fcn.140005aa0.c)
- [`code/fcn.1400065c0.c`](code/fcn.1400065c0.c)
- [`code/fcn.140007080.c`](code/fcn.140007080.c)
- [`code/fcn.140007094.c`](code/fcn.140007094.c)
- [`code/fcn.14000714c.c`](code/fcn.14000714c.c)
- [`code/fcn.140008404.c`](code/fcn.140008404.c)
- [`code/fcn.140008e10.c`](code/fcn.140008e10.c)
- [`code/fcn.140009d74.c`](code/fcn.140009d74.c)
- [`code/fcn.14000a084.c`](code/fcn.14000a084.c)
- [`code/fcn.14000aa64.c`](code/fcn.14000aa64.c)
- [`code/fcn.14000c3b0.c`](code/fcn.14000c3b0.c)
- [`code/fcn.14000ce00.c`](code/fcn.14000ce00.c)
- [`code/fcn.14000d22c.c`](code/fcn.14000d22c.c)
- [`code/fcn.14000e4f4.c`](code/fcn.14000e4f4.c)
- [`code/fcn.14000e660.c`](code/fcn.14000e660.c)
- [`code/fcn.14000eaa0.c`](code/fcn.14000eaa0.c)
- [`code/fcn.14000ef04.c`](code/fcn.14000ef04.c)
- [`code/fcn.14000f5a0.c`](code/fcn.14000f5a0.c)
- [`code/fcn.14000ff08.c`](code/fcn.14000ff08.c)
- [`code/fcn.1400104e4.c`](code/fcn.1400104e4.c)
- [`code/fcn.1400105b0.c`](code/fcn.1400105b0.c)
- [`code/fcn.1400110cc.c`](code/fcn.1400110cc.c)
- [`code/fcn.140011ad8.c`](code/fcn.140011ad8.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, I have updated the analysis of the binary's functionality and behavior. The new data confirms several high-risk behaviors, specifically regarding **persistence**, **dropping payloads with masquerading names**, and **sophisticated internal logic** designed to hinder static analysis.

### Updated Core Functionality
The binary is confirmed as a multi-stage **malware dropper/downloader**. It doesn't just inject code; it also performs "staging" by copying itself or its components into hidden directories under legitimate-sounding names to ensure persistence on the system after an initial infection.

### New & Enhanced Malicious Behaviors

*   **Persistence and Staging (High Risk):**
    *   In `fcn.140001480`, the malware performs several classic "dropper" actions:
        *   **Environment Check:** It queries `%LOCALAPPDATA%` and `%TEMP%` environment variables to find a location for its payload.
        *   **Directory Creation:** It creates a new directory based on these paths (likely to hide its presence).
        *   **Payload Masquerading:** It contains an array of deceptive filenames: `"WindowsStore.Update.exe"`, `"MicrosoftEdge.Update.exe"`, `"SecurityHealthSystray.exe"`, and `"OfficeBackgroundTaskHandler.exe"`. 
        *   **File Copying & Hardening:** It copies a component to one of these names, then calls `SetFileAttributes` (likely to hide the file) and potentially `SystemTimeToFileTime` to manipulate timestamps (timestomping), making the file appear older than it is.
    *   **Registry Persistence:** It modifies the **"Run" key** (`Software\Microsoft\Windows\CurrentVersion\Run`) to ensure that one of these masqueraded files executes automatically every time the user logs in.

*   **File System Traversal and Discovery:**
    *   In `fcn.140009d74`, the malware implements logic using `FindFirstFileExW` and `FindNextFileW`. 
    *   **Purpose:** It appears to be scanning for specific files or configuration data on the disk. The inclusion of a string comparison loop suggests it is looking for specific filenames or "magic" signatures before proceeding with its next stage of execution.

*   **Advanced Obfuscation & Anti-Analysis:**
    *   The code contains several very complex functions (e.g., `fcn.14000eaa0`, `fcn.140008e10`) characterized by large jump tables, heavy bitwise operations (`&`, `|`, `^`), and constant shifting.
    *   **Purpose:** These are common in "packer" code or heavily obfuscated malware. They serve to confuse static analysis tools (like IDA Pro/Ghidra) by making the logic flow difficult to follow linearly, often hiding the actual malicious intent behind layers of arithmetic and conditional jumps.

### Updated Summary Table of Indicators

| Feature | Detail | Threat Level |
| :--- | :--- | :--- |
| **Persistence** | Modifies `HKCU\...\Run` key; uses common system paths (AppData/Temp). | High |
| **Masquerading** | Uses names like `MicrosoftEdge.Update.exe` to blend in with OS services. | High |
| **Dropper Behavior** | Copies and hides files on disk for future execution. | High |
| **Injection** | `VirtualAllocEx`, `WriteProcessMemory`, `CreateRemoteThread` (Chrome/Edge). | High |
| **Privilege Escalation**| Attempts to acquire `SeDebugPrivilege`. | High |
| **Evasion/Obfuscation** | Heavy use of jump tables and bit-shifting to hide logic flow. | Medium |
| **Data Collection** | Scans filesystem via `FindFirstFileExW` for specific signatures. | Medium |

### Analysis Conclusion Update
The binary is a sophisticated, multi-stage piece of malware. Its design indicates it is intended for long-term residency on a target machine. 

1.  **Initial Phase:** It validates the environment and gains privileges to interact with system processes.
2.  **Dropping Phase:** It finds a hidden directory and drops "decoy" files that mimic legitimate Windows updates/services (e.g., `MicrosoftEdge.Update.exe`).
3.  **Persistence Phase:** It ensures these decoys start automatically via Registry keys.
4.  **Execution/Injection Phase:** It targets high-value processes (Browsers, Explorer) to inject its primary payload, likely for credential theft or information exfiltration.

The presence of complex obfuscation suggests this is not a simple script but a professionally developed malware sample designed to bypass automated security scanners and frustrate manual reverse engineering.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the corresponding MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys | The malware modifies the `Software\Microsoft\Windows\CurrentVersion\Run` key to ensure persistent execution of masqueraded files upon user login. |
| **T1036.005** | Masquerading: Match System Services or Files | The use of deceptive filenames (e.g., `MicrosoftEdge.Update.exe`) is designed to blend in with legitimate system services and evade detection. |
| **T1070.006** | Indicator Removal on Host: Timestomping | The call to `SystemTimeToFileTime` indicates an attempt to modify file timestamps to make the malicious files appear older than they are, evading forensic analysis. |
| **T1055** | Process Injection | The use of `VirtualAllocEx`, `WriteProcessMemory`, and `CreateRemoteThread` confirms the intent to inject payload into high-value processes like Chrome or Edge. |
| **T1027** | Obfuscated Files or Information | The heavy use of jump tables, bitwise operations, and constant shifting is a deliberate tactic to hinder static analysis and hide logic flow from researchers. |
| **T1083** | File and Directory Discovery | The implementation of `FindFirstFileExW` and `FindNextFileW` indicates the malware is searching for specific files or configurations on the disk before proceeding. |
| **T1068** | Exploitation for Privilege Escalation | The attempt to acquire `SeDebugPrivilege` is a common method used by malware to gain the permissions necessary to interact with and inject code into system processes. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

### **IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

### **File paths / Registry keys**
*   **Registry Keys:**
    *   `Software\Microsoft\Windows\CurrentVersion\Run` (Used for persistence)
*   **Masqueraded File Names (Potential Paths):**
    *   `WindowsStore.Update.exe`
    *   `MicrosoftEdge.Update.exe`
    *   `SecurityHealthSystray.exe`
    *   `OfficeBackgroundTaskHandler.exe`

### **Mutex names / Named pipes**
*   *(None identified in the provided text)*

### **Hashes**
*   *(No MD5/SHA1/SHA256 hashes were present in the provided strings.)*

### **Other artifacts**
*   **Target Processes (Injection Targets):**
    *   `Chrome`
    *   `Edge`
*   **Suspicious File System Activities:**
    *   Use of `SetFileAttributes` to hide files.
    *   Use of `SystemTimeToFileTime` for timestomping (modifying file timestamps).
    *   FileSystem scanning via `FindFirstFileExW` and `FindNextFileW`.
*   **Injection/Malicious API Patterns:**
    *   `VirtualAllocEx`
    *   `WriteProcessMemory`
    *   `CreateRemoteThread`
    *   `SeDebugPrivilege` (Request for elevated privileges).

---
**Analyst Note:** The "Extracted Strings" section contains a high volume of obfuscated or junk data (e.g., `WATAUAVAWH`, `A_A^A]A\_`) which do not translate to actionable technical indicators and were excluded from this report.

---

## Malware Family Classification

1. **Malware family**: Loader
2. **Malware type**: Dropper, Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-stage Persistence & Masquerading:** The binary exhibits classic "dropper" behavior by copying files to hidden directories under deceptive names (e.g., `MicrosoftEdge.Update.exe`, `SecurityHealthSystray.exe`) and establishing persistence via the `HKCU\...\Run` registry key.
*   **Advanced Evasion Techniques:** The sample employs sophisticated techniques to hinder analysis, including "timestomping" (`SystemTimeToFileTime`), high-complexity obfuscation (jump tables and bitwise operations), and attempts to gain `SeDebugPrivilege` for unauthorized system interaction.
*   **Process Injection for Payloads:** The binary specifically targets high-value processes like **Chrome** and **Edge** using `VirtualAllocEx`, `WriteProcessMemory`, and `CreateRemoteThread`, which is a standard tactic for injecting secondary payloads for information theft or remote access.
