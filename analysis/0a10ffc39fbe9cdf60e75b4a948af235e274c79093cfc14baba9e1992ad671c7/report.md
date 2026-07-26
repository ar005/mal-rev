# Threat Analysis Report

**Generated:** 2026-07-24 14:51 UTC
**Sample:** `0a10ffc39fbe9cdf60e75b4a948af235e274c79093cfc14baba9e1992ad671c7_0a10ffc39fbe9cdf60e75b4a948af235e274c79093cfc14baba9e1992ad671c7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a10ffc39fbe9cdf60e75b4a948af235e274c79093cfc14baba9e1992ad671c7_0a10ffc39fbe9cdf60e75b4a948af235e274c79093cfc14baba9e1992ad671c7.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 (stripped to external PDB), 10 sections |
| Size | 132,096 bytes |
| MD5 | `db1829dcecb2f498ae47e2848412c124` |
| SHA1 | `fee19bf3586d811789fdeccfe30adf99f8a77359` |
| SHA256 | `0a10ffc39fbe9cdf60e75b4a948af235e274c79093cfc14baba9e1992ad671c7` |
| Overall entropy | 6.195 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773878271 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 105,984 | 6.068 | No |
| `.data` | 2,048 | 0.129 | No |
| `.rdata` | 7,680 | 5.528 | No |
| `.eh_fram` | 5,120 | 4.876 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 4,608 | 5.323 | No |
| `.CRT` | 512 | 0.269 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 1,024 | 2.258 | No |
| `.reloc` | 3,584 | 6.346 | No |

### Imports

**ADVAPI32.dll**: `RegCloseKey`, `RegCreateKeyExW`, `RegDeleteKeyValueW`, `RegSetValueExW`, `SystemFunction036`
**CRYPT32.dll**: `CryptProtectData`, `CryptUnprotectData`
**IPHLPAPI.DLL**: `GetAdaptersAddresses`
**KERNEL32.dll**: `AssignProcessToJobObject`, `CloseHandle`, `CopyFileW`, `CreateDirectoryW`, `CreateFileW`, `CreateJobObjectA`, `CreateMutexA`, `CreatePipe`, `CreateProcessA`, `CreateProcessW`, `CreateThread`, `DeleteCriticalSection`, `DeleteFileW`, `EnterCriticalSection`, `FindClose`
**msvcrt.dll**: `__getmainargs`, `__initenv`, `__lconv_init`, `__mb_cur_max`, `__p__acmdln`, `__p__commode`, `__p__fmode`, `__set_app_type`, `__setusermatherr`, `_amsg_exit`, `_cexit`, `_errno`, `_initterm`, `_iob`, `_lock`
**SHELL32.dll**: `CommandLineToArgvW`
**WS2_32.dll**: `WSACleanup`, `WSAStartup`, `closesocket`, `connect`, `freeaddrinfo`, `getaddrinfo`, `recv`, `send`, `socket`

## Extracted Strings

Total strings found: **506** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.eh_framH
.idata
.reloc
R 9S$~
=UUUUw
D$ 9|$8s
9D$Ds<
s)+T$p
D$$)D$D
D$(D$L
D$|;D$
D$D+D$
|$$9t0
D$<zu
9|$(vv
\$P+L$P
\$(9\$0vV
;|$hs
9|$Xvq
s+D$
tS<t/
0<	wm1
libgcc_s_dw2-1.dll
__register_frame_info
__deregister_frame_info
%s (%s): %s (%lu)
%s (%s) (%lu)
%s: %s (%lu)
%s (%lu)
FCFGTRL1
open failed
read failed
seek failed
write failed
path not found
remove dir failed
delete file failed
path conversion failed
file too large
%s:cfg
--server
FC_AGENT_WORKERS
--workers
ADNEAgent
%sUser
cmd /C schtasks /Create /TN 
 /SC ONLOGON /RL LIMITED /TR 
 /F /IT
$ErrorActionPreference='Stop';
$action=New-ScheduledTaskAction -Execute 
;$trigger=New-ScheduledTaskTrigger -AtLogOn;
$principal=New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType InteractiveToken -RunLevel LeastPrivilege;
Register-ScheduledTask -TaskName '
' -Action $action -Trigger $trigger -Principal $principal -Force
 -Argument 
@echo off

start "" %s

expand 32-byte k
{"command_id":"
","ok":
,"output_b64":"
","error_b64":"
","partial":
,"seq":
--autostart
--apply-update-helper
--helper-parent-pid
--helper-source
--helper-target
--helper-agent-home
FC_AGENT_HOME
 --server 
 --id 
 --workers 
cmd.exe /C ping 127.0.0.1 -n 3 >nul & del /f /q 
FC_AGENT_ID
%s\plugins\*.dll
%s\plugins\%s
windows-host
RtlGetVersion
%lu.%lu
windows
Local\ADNEAgent_%08X
"id":"
"os":"windows",
"plugin_mode":"tiny",
"persistence":
"hostname":"
,"os_version":"
,"os_build":"
,"version":"
,"arch":"
,"lang":"
,"token":"
cpu_percent
max_concurrency
bandwidth_kbps
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **3**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00408488` | `0x408488` | 27181 | ✓ |
| `fcn.00401cf0` | `0x401cf0` | 22790 | ✓ |
| `fcn.00412364` | `0x412364` | 14735 | ✓ |
| `fcn.004181d8` | `0x4181d8` | 11112 | — |
| `fcn.00404f90` | `0x404f90` | 5932 | — |
| `fcn.0040fce4` | `0x40fce4` | 2722 | — |
| `fcn.004043f0` | `0x4043f0` | 2229 | — |
| `fcn.0041103c` | `0x41103c` | 1523 | — |
| `fcn.00403e30` | `0x403e30` | 1471 | — |
| `fcn.00403920` | `0x403920` | 1285 | — |
| `fcn.00411630` | `0x411630` | 1225 | — |
| `fcn.0041663c` | `0x41663c` | 973 | — |
| `fcn.00411f80` | `0x411f80` | 946 | — |
| `fcn.00402df0` | `0x402df0` | 944 | — |
| `fcn.00403270` | `0x403270` | 904 | — |
| `fcn.00417e18` | `0x417e18` | 892 | — |
| `entry0` | `0x4014b0` | 847 | — |
| `fcn.00416188` | `0x416188` | 725 | — |
| `fcn.00401a10` | `0x401a10` | 722 | — |
| `fcn.004024f0` | `0x4024f0` | 705 | — |
| `fcn.0040eeb8` | `0x40eeb8` | 612 | — |
| `fcn.0040f610` | `0x40f610` | 599 | — |
| `fcn.00417078` | `0x417078` | 575 | — |
| `fcn.00407030` | `0x407030` | 562 | — |
| `fcn.00415f08` | `0x415f08` | 544 | — |
| `fcn.00404d90` | `0x404d90` | 506 | — |
| `fcn.00411afc` | `0x411afc` | 465 | — |
| `fcn.0040f868` | `0x40f868` | 443 | — |
| `fcn.00415d58` | `0x415d58` | 429 | — |
| `fcn.00407620` | `0x407620` | 406 | — |

### Decompiled Code Files

- [`code/fcn.00401cf0.c`](code/fcn.00401cf0.c)
- [`code/fcn.00408488.c`](code/fcn.00408488.c)
- [`code/fcn.00412364.c`](code/fcn.00412364.c)

## Behavioral Analysis

This final analysis incorporates the disassembly from the third chunk, which provides deep insight into the **internal execution logic**, **multi-process communication**, and **robust error handling** of the "ADNEAgent" malware.

### Updated Technical Analysis: ADNEAgent (Final Synthesis)

The completion of the code analysis confirms that AD1NEAgent is a high-tier, production-grade Remote Access Trojan (RAT). The final chunk reveals how the agent manages its internal threads, handles plugin-specific instructions, and utilizes Inter-Process Communication (IPC) to maintain stability.

---

### 1. Advanced Plugin Execution & Validation
The third chunk of code details the logic used once a command is routed to a specific plugin. It isn't just "running" a DLL; it is managing an internal state for each module:

*   **Dynamic Instruction Parsing:** The use of `strtol` to process "plugin op" indicates that even after a plugin is loaded, the attacker sends numerical codes (op-codes) to specify actions. This allows a single plugin to perform multiple functions (e.g., a "Keylogger" plugin might have different op-codes for 'start', 'stop', and 'clear').
*   **Payload Handling:** The code explicitly checks for "invalid plugin payload." This suggests that the data received from the C2 is parsed into specific packets before being passed to the plugin, ensuring the agent doesn't crash when handling malformed instructions.
*   **Robust Error Logging:** Every stage of the plugin lifecycle includes safety checks. If a file is missing or an op-code is incorrect, the code generates internal error strings (e.g., "invalid plugin name," "plugin load failed"). This ensures the primary agent stays alive even if a sub-component fails.

### 2. Multi-Process Architecture & IPC
The most significant finding in this final chunk relates to how the malware handles data movement between its own components:

*   **Named Pipe Communication:** The heavy presence of `hReadPipe`, `hProcess` (a handle to another process), and `lpNumberOfBytesRead` confirms a **dual-process architecture**. 
    *   The "Agent" likely acts as the listener, while a secondary, hidden "worker" process performs intensive tasks like file encryption, large data reading, or screen scraping.
    *   **Why this is used:** By splitting the tasks, if a security tool detects and kills the worker process for "suspicious activity," the main communication thread (the Agent) can stay alive to report back to the attacker or try to restart the worker.
*   **Synchronization via Critical Sections:** The use of `EnterCriticalSection` and `LeaveCriticalSection` confirms that the malware is **multi-threaded**. This allows it to handle incoming C2 heartbeats while simultaneously processing heavy data from the "worker" process over the named pipe without causing a race condition or crashing.

### 3. File System Interaction Logic
The code includes a dedicated loop for scanning and loading files:
*   **Iterative Scanning:** Using `FindFirstFileW` and `FindNextFileW` in a loop, it iterates through files to find matching modules. 
*   **Memory Management:** The extensive use of `malloc`, `free`, and `strdup` specifically for handling directory paths and plugin names indicates that the malware is designed to handle dynamic system information without leaving static strings in memory that could be easily flagged by simple signature scanners.

---

### Final Summary Table of Indicators (Final Version)

| Category | Specific Technical Findings | Risk / Significance |
| :--- | :--- | :--- |
| **C2 Command Suite** | `read`, `write_chunk`, `mkdir`, `reboot`, `switch_endpoint` | **High**: Enables full file theft, remote control, and persistence. |
| **Plugin Architecture** | Support for `.fcp` & `.dll`; op-code processing; "payload" validation. | **High**: Allows the attacker to update capabilities without re-infecting host. |
| **Multi-Process (IPC)** | Named Pipes (`hReadPipe`), Process Handles, and Pipe reading logic. | **Critical**: Evades detection by isolating data-heavy tasks in a secondary process. |
| **Threading & Stability** | `CriticalSection` usage; robust error handling for "invalid" inputs/paths. | **High**: Ensures the malware remains active even if specific modules fail. |
| **Persistence Prep** | `uninstall`, `disable_autostart` (Registry/Task manipulation). | **High**: Directly facilitates long-term, hidden residency on the host. |

---

### Final Conclusion: Threat Profile
The **ADNEAgent** is a sophisticated, modular backdoor designed for high-value targets where persistence and reliability are paramount. 

Unlike "script-kiddy" malware that performs all actions in one process, ADNEAgent employs professional-grade techniques:
1.  **Modularity:** It can be updated with new capabilities via its plugin system.
2.  **Resilience:** It uses multi-threading and critical sections to ensure stability.
3.  **Evasion:** It uses a dual-process architecture (via Named Pipes) to separate the "network" face from the "action" face of the malware, making it significantly harder for standard EDR solutions to flag the primary communication thread as malicious.

**Recommendation:** This sample should be treated as a high-priority threat. Analysts should monitor for unauthorized `Named Pipe` creation and look for suspicious `.fcp` files in hidden directories or common application folders.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors observed in the **ADNEAgent** analysis to the following MITRE ATT&K techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The use of "op-codes" (via `strtol`) for instruction parsing allows the malware to execute various functions through a modular plugin system. |
| **T1601** | Reflective Code Loading | The utilization of `.fcp` and `.dll` modules allows the agent to dynamically load and update capabilities without altering the primary executable's core logic. |
| **T1133** | External Communication | The "switch_endpoint" command and variety of C2 instructions (read, write, mkdir) indicate a robust infrastructure for remote data exfiltration and control. |
| **T1547** | Boot or Logon Autostart Execution | The inclusion of `disable_autostart` and registry manipulation confirms the malware's intent to establish persistent residency on the host. |
| **T1027** | Encrypted/Packed_Data (Contextual) | The use of dynamic memory allocation (`malloc`, `strdup`) to handle file paths instead of static strings is a common technique used to evade simple string-based detection. |

***

### Analyst Notes on Advanced Behaviors:
*   **Multi-Process Architecture & IPC:** While "Named Pipes" doesn't have a dedicated unique ID in the primary MITRE ATT&CK matrix, it represents a sophisticated implementation of **Defense Evasion**. By splitting tasks (network communication vs. data processing) between two processes, the malware ensures that if one process is flagged or terminated by an EDR, the other remains active to maintain the connection to the C2 server.
*   **Modular Plugin System:** The use of op-codes suggests a high level of sophistication similar to commercial RATs (like Cobalt Strike), where the core "loader" remains relatively static while the malicious actions are offloaded to dynamically loaded modules.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

### **IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

### **File paths / Registry keys**
*   `Local\ADNEAgent_%08X` (Indicates a Registry key or Service name pattern)
*   `%s\plugins\` (Directory path used for malicious module storage)
*   `.fcp` (Malicious file extension used for plugins)

### **Mutex names / Named pipes**
*   `hReadPipe` (Indicates the use of Named Pipes for inter-process communication)

### **Hashes**
*   *(None identified in the provided strings)*

### **Other artifacts**
*   **Malware Name:** `ADNEAgent`
*   **C2 Command Set / Commands:** 
    *   `read_chunk`
    *   `write_chunk`
    *   `mkdir`
    *   `reboot`
    *   `switch_endpoint`
    *   `plugin_install`
    *   `plugin_call`
    *   `plugin_remove`
*   **Internal Configuration Identifiers:** 
    *   `FCFGTRL1`
    *   `FC_AGENT_WORKERS`
    *   `FC_AGENT_HOME`
    *   `FC_AGENT_ID`
*   **Persistence Mechanisms:**
    *   Use of `schtasks` (Scheduled Tasks) for persistence.
    *   Automated registry modification via PowerShell (`Remove-ItemProperty -Path 'HKCU:\...'`).
*   **Configuration/Status Indicators:** 
    *   `offline_mode`
    *   `plugin_mode: "tiny"`
    *   `inventory_type` (implied by internal logic)

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification of the sample:

1. **Malware family**: custom (ADNEAgent)
2. **Malware type**: RAT / Backdoor
3. **Confidence**: High
4. **Key evidence**:
    * **Advanced Evasion via Multi-Process Architecture:** The use of Named Pipes (`hReadPipe`) and critical sections to separate the "communication" process from the "worker" process is a high-tier technique used to ensure that if one component is flagged by security software, the other remains active.
    * **Modular Plugin System:** The inclusion of `.fcp` files and a robust op-code interpretation system (using `strtol`) allows the attacker to dynamically inject new capabilities (e.g., file manipulation, data exfiltration) without altering the primary malware's core code.
    * **Extensive C2 Command Suite:** The presence of commands like `read_chunk`, `write_chunk`, `mkdir`, and `switch_endpoint` confirms that the tool is designed for persistent remote access, file system interaction, and administrative control over the infected host.
