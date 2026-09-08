# Threat Analysis Report

**Generated:** 2026-09-07 21:50 UTC
**Sample:** `1586e6f714547d9ec024c9aeff1df7024d37a867d543de418b0af65c530c6738_1586e6f714547d9ec024c9aeff1df7024d37a867d543de418b0af65c530c6738.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1586e6f714547d9ec024c9aeff1df7024d37a867d543de418b0af65c530c6738_1586e6f714547d9ec024c9aeff1df7024d37a867d543de418b0af65c530c6738.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 297,472 bytes |
| MD5 | `1ebf69bec958763e420691a856ba1e3e` |
| SHA1 | `4dd8ade66c5966282097e0c69abe1cbcef12e393` |
| SHA256 | `1586e6f714547d9ec024c9aeff1df7024d37a867d543de418b0af65c530c6738` |
| Overall entropy | 5.987 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766615520 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 43,008 | 6.294 | No |
| `.rdata` | 26,624 | 4.863 | No |
| `.data` | 218,112 | 6.028 | No |
| `.pdata` | 3,584 | 4.386 | No |
| `.rsrc` | 1,024 | 3.85 | No |
| `.reloc` | 4,096 | 2.078 | No |

### Imports

**SHELL32.dll**: `ShellExecuteExW`
**ADVAPI32.dll**: `LookupPrivilegeValueW`, `RegCloseKey`, `OpenProcessToken`, `RegSetValueExA`, `LookupPrivilegeValueA`, `RegOpenKeyExA`, `AdjustTokenPrivileges`
**SHLWAPI.dll**: `PathFindFileNameA`
**KERNEL32.dll**: `WriteConsoleW`, `SetFilePointerEx`, `SetStdHandle`, `lstrlenA`, `HeapAlloc`, `GetCurrentProcess`, `HeapFree`, `Process32First`, `WaitForSingleObject`, `GetProcessHeap`, `OpenProcess`, `Sleep`, `GetExitCodeProcess`, `GetModuleFileNameW`, `CreateFileW`

## Extracted Strings

Total strings found: **1212** (showing first 100)

```
!This program cannot be run in DOS mode.
$
1Rich
`.rdata
@.data
.pdata
@.rsrc
@.reloc
@UWAVH
f9\$0t
SVWAVH
8A^_^[
SVWAVAWH
0A_A^_^[
fffffff
ATAVAWH
 A_A^A\
VWATAVAWH
 A_A^A\_^
x ATAVAWH
 A_A^A\
x UAVAWH
Genuua
ineIuY
nteluQ3
WATAUAVAWH
@A_A^A]A\_
WATAUAVAWH
A_A^A]A\_
t$ WAVAWH
` AUAVAWH
t$HHc0I
\$0D9=
A_A^A]
Hct$PH
seHcD$XH
fD9!u:A
fD93tSH
CfD93u
H3E H3E
9 w
fD9
VWATAVAWH
A_A^A\_^
UVWATAUAVAWH
wL9g0u
O0HcQH
O0HcQ
G0Hc	H
A_A^A]A\_^]
D8eoupH
UVWATAUAVAWH
pA_A^A]A\_^]
WATAUAVAWH
E0LcxI
E0HcH
 A_A^A]A\_
AUAVAWH
0A_A^A]
@SVWATAUAVAWH
L!|$@L!
D$HHcH
A_A^A]A\_^[
SVWATAUAVAWH
0A_A^A]A\_^[
WATAVH
 t>D9u9M
@A^A\_
LcA<E3
VWATAVAWH
0A_A^A\_^
l$ VWATAVAWH
T$&@8t$&t9@8r
A81t@@8r
A_A^A\_^
@SUVWATAVAWH
tcH95n

PA_A^A\_^][
@UATAUAVAWH
@88tH
!t$(H!t$ I
A_A^A]A\]
@UATAUAVAWH
A_A^A]A\]
AUAVAWH
0A_A^A]
K H;b
K(H;X
K0H;N
K8H;D
K@H;:
KHH;0
KhH;>
KpH;4
KxH;*
KXH;o
K`H;e
VWATAVAWH
 A_A^A\_^
\$ UVWATAUAVAWH
!|$HHc
|$HD9l$X
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140004184` | `0x140004184` | 12745 | ✓ |
| `fcn.14000524c` | `0x14000524c` | 9179 | ✓ |
| `fcn.140003b5c` | `0x140003b5c` | 8775 | ✓ |
| `fcn.140002850` | `0x140002850` | 5161 | ✓ |
| `fcn.14000a0b4` | `0x14000a0b4` | 1908 | ✓ |
| `fcn.140002880` | `0x140002880` | 1252 | ✓ |
| `fcn.140005fc0` | `0x140005fc0` | 1204 | ✓ |
| `fcn.140009a38` | `0x140009a38` | 1018 | ✓ |
| `fcn.140001d50` | `0x140001d50` | 955 | ✓ |
| `fcn.140001e90` | `0x140001e90` | 890 | ✓ |
| `fcn.140001760` | `0x140001760` | 727 | ✓ |
| `fcn.1400090b4` | `0x1400090b4` | 718 | ✓ |
| `fcn.1400081a4` | `0x1400081a4` | 686 | ✓ |
| `fcn.140004808` | `0x140004808` | 623 | ✓ |
| `fcn.140008820` | `0x140008820` | 622 | ✓ |
| `fcn.140006474` | `0x140006474` | 613 | ✓ |
| `fcn.140007f48` | `0x140007f48` | 604 | ✓ |
| `fcn.140001440` | `0x140001440` | 570 | ✓ |
| `fcn.140006e7c` | `0x140006e7c` | 548 | ✓ |
| `fcn.1400078a4` | `0x1400078a4` | 548 | ✓ |
| `fcn.140006890` | `0x140006890` | 509 | ✓ |
| `fcn.140007ca8` | `0x140007ca8` | 481 | ✓ |
| `fcn.140004d68` | `0x140004d68` | 460 | ✓ |
| `fcn.140005728` | `0x140005728` | 408 | ✓ |
| `fcn.140008b54` | `0x140008b54` | 406 | ✓ |
| `fcn.140004254` | `0x140004254` | 405 | ✓ |
| `fcn.140006ce8` | `0x140006ce8` | 402 | ✓ |
| `entry0` | `0x14000314c` | 398 | ✓ |
| `fcn.1400037bc` | `0x1400037bc` | 373 | ✓ |
| `fcn.14000941c` | `0x14000941c` | 357 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.140001440.c`](code/fcn.140001440.c)
- [`code/fcn.140001760.c`](code/fcn.140001760.c)
- [`code/fcn.140001d50.c`](code/fcn.140001d50.c)
- [`code/fcn.140001e90.c`](code/fcn.140001e90.c)
- [`code/fcn.140002850.c`](code/fcn.140002850.c)
- [`code/fcn.140002880.c`](code/fcn.140002880.c)
- [`code/fcn.1400037bc.c`](code/fcn.1400037bc.c)
- [`code/fcn.140003b5c.c`](code/fcn.140003b5c.c)
- [`code/fcn.140004184.c`](code/fcn.140004184.c)
- [`code/fcn.140004254.c`](code/fcn.140004254.c)
- [`code/fcn.140004808.c`](code/fcn.140004808.c)
- [`code/fcn.140004d68.c`](code/fcn.140004d68.c)
- [`code/fcn.14000524c.c`](code/fcn.14000524c.c)
- [`code/fcn.140005728.c`](code/fcn.140005728.c)
- [`code/fcn.140005fc0.c`](code/fcn.140005fc0.c)
- [`code/fcn.140006474.c`](code/fcn.140006474.c)
- [`code/fcn.140006890.c`](code/fcn.140006890.c)
- [`code/fcn.140006ce8.c`](code/fcn.140006ce8.c)
- [`code/fcn.140006e7c.c`](code/fcn.140006e7c.c)
- [`code/fcn.1400078a4.c`](code/fcn.1400078a4.c)
- [`code/fcn.140007ca8.c`](code/fcn.140007ca8.c)
- [`code/fcn.140007f48.c`](code/fcn.140007f48.c)
- [`code/fcn.1400081a4.c`](code/fcn.1400081a4.c)
- [`code/fcn.140008820.c`](code/fcn.140008820.c)
- [`code/fcn.140008b54.c`](code/fcn.140008b54.c)
- [`code/fcn.1400090b4.c`](code/fcn.1400090b4.c)
- [`code/fcn.14000941c.c`](code/fcn.14000941c.c)
- [`code/fcn.140009a38.c`](code/fcn.140009a38.c)
- [`code/fcn.14000a0b4.c`](code/fcn.14000a0b4.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, this binary exhibits several characteristics consistent with a **malicious downloader or Trojan**. The code contains sophisticated techniques for process injection, anti-analysis evasion, and persistence by masquerading as legitimate system processes.

### Core Functionality and Purpose
The primary purpose of this code appears to be establishing a persistent foothold on the system while executing a malicious payload hidden within another process. It uses standard Windows utilities (`schtasks.0`, `ntdll`) to perform its tasks, often using "masquerading" techniques (naming things after "Windows Defender") to hide from the user and basic security tools.

### Suspicious or Malicious Behaviors

*   **Process Injection (High Risk)**
    *   The function `fcn.140001400` is a classic implementation of **Remote Thread Injection**. 
    *   It opens a remote process with high privileges (`PROCESS_ALL_ACCESS`), allocates memory within that process using `VirtualAllocEx`, and copies a payload into that space via `WriteProcessMemory`.
    *   It specifically resolves `RtlCreateUserThread` from `ntdll.dll` to execute the injected code in the context of the hijacked process, which is a common method to evade standard API hooks.

*   **Persistence & Masquerading**
    *   The function `fcn.140001760` interacts with the Windows Task Scheduler (`schtasks.exe`).
    *   It creates a scheduled task specifically named **"Windows Defender Security"**. This is an attempt to blend in with legitimate system services. 
    *   It configures this task to run every minute, ensuring the malware automatically restarts or remains active even if the original process is closed.

*   **Anti-Analysis & Anti-Debugging**
    *   The code uses `IsDebuggerPresent()` (in `fcn.140003c5c`) and `IsProcessorFeaturePresent()` (in `fcn.140002850`) to detect if it is running in a debugger or an analysis environment.
    *   If certain conditions are not met (e.g., if it detects a "clean" environment for the attacker), it calls `TerminateProcess`, effectively stopping its own execution to prevent researchers from observing its behavior.

*   **Dynamic API Resolution & Obfuscation**
    *   The function `fcn.140008820` demonstrates dynamic loading of system libraries and resolution of functions via `GetProcAddress`. 
    *   This technique is commonly used to hide the program's true intentions from static analysis tools, as it avoids hardcoding "suspicious" function names in the Import Address Table (IAT).

### Notable Techniques Observed
*   **Shadowing System Names:** By using the string "Windows Defender Security" for its scheduled tasks, the malware attempts to deceive users and administrators who might overlook a task with that name.
*   **Direct System Calls/Low-Level APIs:** The use of `ntdll` functions (like `RtlCreateUserThread`) instead of higher-level Win32 APIs is a common technique used by advanced malware to bypass security software's monitoring capabilities.
*   **Multi-Stage Execution:** The code structure suggests that the initial binary acts as a "loader" or "dropper," which performs the anti-analysis checks and injects the "payload" into a stable process (like `explorer.exe` or `svchost.exe`) to hide its activity.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1055 | Process Injection | The malware performs remote thread injection using `VirtualAllocEx`, `WriteProcessMemory`, and `RtlCreateUserThread` to execute code in a different process. |
| T1053.005 | Scheduled Task | The binary uses the Windows Task Scheduler (`schtasks`) to establish persistence by creating a recurring task. |
| T1036.005 | Masquerading: Match System Firmware/Software | The malware names its scheduled task "Windows Defender Security" to blend in with and deceive users/tools regarding legitimate system processes. |
| T1497 | Virtualization/Sandbox Detection | The use of `IsDebuggerPresent` and `IsProcessorFeaturePresent` allows the malware to detect and terminate if run in a debugger or analysis environment. |
| T1027 | Obfuscated Import Table | The use of dynamic API resolution via `GetProcAddress` is intended to hide the program's true functionality from static analysis tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Standard system error messages (e.g., "permission denied", "no such file or directory") and standard Windows API names (e.g., `VirtualAllocEx`, `ntdll.dll`) were excluded as they are common across both legitimate and malicious software.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **Scheduled Task Name:** `Windows Defender Security` (Note: This is used as a masquerading name for a scheduled task).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Persistence Mechanism:** Creation of a scheduled task via `schtasks.exe` with the name "Windows Defender Security" configured to run every minute.
*   **Evasion Technique (API Masking):** Use of `RtlCreateUserThread` from `ntdll.dll` to perform remote thread injection.
*   **Anti-Analysis Checks:** Usage of `IsDebuggerPresent()` and `IsProcessorFeaturePresent()` to detect analysis environments.
*   **Injection Method:** Remote Thread Injection using `VirtualAllocEx` and `WriteProcessMemory`.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Injection & Evasion:** The sample employs advanced remote thread injection (using `VirtualAllocEx`, `WriteProcessMemory`, and `RtlCreateUserThread`) to execute a hidden payload within legitimate processes, coupled with dynamic API resolution to bypass static detection.
*   **Masquerading Tactics:** It actively attempts to deceive both users and security tools by naming its persistence mechanism (scheduled task) "Windows Defender Security."
*   **Anti-Analysis Suite:** The inclusion of `IsDebuggerPresent` and `IsProcessorFeaturePresent` checks, combined with automated execution through a 1-minute interval scheduled task, indicates an intentional effort to evade analysis environments and maintain long-term persistence.
