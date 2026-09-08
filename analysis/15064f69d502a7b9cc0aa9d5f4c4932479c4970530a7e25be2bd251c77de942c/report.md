# Threat Analysis Report

**Generated:** 2026-09-06 15:07 UTC
**Sample:** `15064f69d502a7b9cc0aa9d5f4c4932479c4970530a7e25be2bd251c77de942c_15064f69d502a7b9cc0aa9d5f4c4932479c4970530a7e25be2bd251c77de942c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `15064f69d502a7b9cc0aa9d5f4c4932479c4970530a7e25be2bd251c77de942c_15064f69d502a7b9cc0aa9d5f4c4932479c4970530a7e25be2bd251c77de942c.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 6 sections |
| Size | 17,920 bytes |
| MD5 | `cd4ea7f2616d05b2c74469ba7be4d910` |
| SHA1 | `b1169381916cfc79ebc9efb5a4e9fa68a9852215` |
| SHA256 | `15064f69d502a7b9cc0aa9d5f4c4932479c4970530a7e25be2bd251c77de942c` |
| Overall entropy | 5.39 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1781204558 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 6,656 | 6.012 | No |
| `.rdata` | 7,168 | 4.88 | No |
| `.data` | 512 | 4.371 | No |
| `.pdata` | 1,024 | 2.656 | No |
| `.rsrc` | 1,024 | 4.051 | No |
| `.reloc` | 512 | 0.821 | No |

### Imports

**KERNEL32.dll**: `AddVectoredExceptionHandler`, `IsDebuggerPresent`, `CreateToolhelp32Snapshot`, `Process32NextW`, `CreateThreadpoolWait`, `Process32FirstW`, `WriteProcessMemory`, `GetHandleInformation`, `CreateMutexW`, `CreateEventW`, `SetEvent`, `VirtualAllocEx`, `VirtualFreeEx`, `GetModuleHandleA`, `GetProcAddress`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `OpenProcessToken`, `LookupPrivilegeValueW`
**VCRUNTIME140.dll**: `__C_specific_handler`, `__current_exception`, `__current_exception_context`, `memset`, `memcpy`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__acrt_iob_func`, `__p__commode`, `__stdio_common_vfprintf`, `getchar`, `_set_fmode`, `__stdio_common_vfwprintf`
**api-ms-win-crt-runtime-l1-1-0.dll**: `exit`, `_exit`, `system`, `__p___argc`, `__p___argv`, `_cexit`, `_configure_narrow_argv`, `_register_thread_local_exe_atexit_callback`, `_initterm_e`, `_initterm`, `_seh_filter_exe`, `_initialize_onexit_table`, `_register_onexit_function`, `_crt_atexit`, `terminate`
**api-ms-win-crt-string-l1-1-0.dll**: `_wcsnicmp`, `_wcsicmp`
**api-ms-win-crt-heap-l1-1-0.dll**: `free`, `_set_new_mode`, `malloc`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

## Extracted Strings

Total strings found: **170** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
L$ SWH
L$ SWH
@SVWATAUH
`A]A\_^[
uqHcp
L$HH1D$ 
D$ H3L$ H3
u3HcH<
@VWAVH
$?< u{
OpenProcessToken failed. Error: %d

LookupPrivilegeValue failed. Error: %d

AdjustTokenPrivileges failed. Error: %d

The token does not have the specified privilege. (
Privilege adjusted successfully.

Error

chcp 65001
?IoCompletion

CreateThreadpoolWait failed. Error: %d

IoCompletion 
pRemoteTpWait
pRemoteTpWait

pRemoteTpDirect
pRemoteTpDirect

WaitPkt valid=%d gle=%lu

IoCompletion valid=%d gle=%lu

Event valid=%d gle=%lu

ZwAssociateWaitCompletionPacket status: 0x%08X

SetEvent=%d gle=%lu

done!

ntdll.dll
NtQueryInformationProcess
?NtQueryInformationProcess, 
? 0x%08X

malloc
? 0x%08X

NtDuplicateObject
NtDuplicateObject
: 0x%08X

: 0x%p

NtQueryObject
NtQueryObject
Object
? 0x%08X

malloc
(NtQueryObject)

: 0x%08X

ZwAssociateWaitCompletionPacket
ZwAssociateWaitCompletionPacket
Go fuck your self and the Debugger

.text$mn
.text$mn$00
.text$x
.idata$5
.00cfg
.CRT$XCA
.CRT$XCAA
.CRT$XCZ
.CRT$XIA
.CRT$XIAA
.CRT$XIAC
.CRT$XIZ
.CRT$XLA
.CRT$XLB
.CRT$XLZ
.CRT$XPA
.CRT$XPZ
.CRT$XTA
.CRT$XTZ
.rdata
.rdata$T
.rdata$voltmd
.rdata$zzzdbg
.rtc$IAA
.rtc$IZZ
.rtc$TAA
.rtc$TZZ
.tls$ZZZ
.xdata
.idata$2
.idata$3
.idata$4
.idata$6
.pdata
.rsrc$01
.rsrc$02
GetCurrentProcess
GetLastError
CloseHandle
CreateMutexW
AddVectoredExceptionHandler
IsDebuggerPresent
CreateToolhelp32Snapshot
Process32NextW
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140001670` | `0x140001670` | 1291 | ✓ |
| `fcn.1400012f0` | `0x1400012f0` | 893 | ✓ |
| `fcn.140002400` | `0x140002400` | 680 | ✓ |
| `main` | `0x140001100` | 485 | ✓ |
| `entry0` | `0x140001e50` | 402 | ✓ |
| `fcn.140002780` | `0x140002780` | 399 | ✓ |
| `fcn.1400020f0` | `0x1400020f0` | 191 | ✓ |
| `fcn.140001f10` | `0x140001f10` | 147 | ✓ |
| `fcn.140001fb0` | `0x140001fb0` | 145 | ✓ |
| `fcn.140002290` | `0x140002290` | 85 | ✓ |
| `fcn.140001070` | `0x140001070` | 82 | ✓ |
| `fcn.140001010` | `0x140001010` | 82 | ✓ |
| `fcn.140001e80` | `0x140001e80` | 71 | ✓ |
| `fcn.140002360` | `0x140002360` | 66 | ✓ |
| `fcn.1400020b0` | `0x1400020b0` | 64 | ✓ |
| `fcn.140001ed0` | `0x140001ed0` | 59 | ✓ |
| `fcn.140002080` | `0x140002080` | 43 | ✓ |
| `fcn.140002050` | `0x140002050` | 37 | ✓ |
| `entry1` | `0x1400010d0` | 34 | ✓ |
| `fcn.140001bc0` | `0x140001bc0` | 30 | ✓ |
| `fcn.140002220` | `0x140002220` | 27 | ✓ |
| `fcn.1400021e0` | `0x1400021e0` | 14 | ✓ |
| `fcn.1400022f0` | `0x1400022f0` | 14 | ✓ |
| `fcn.140002240` | `0x140002240` | 12 | ✓ |
| `fcn.1400026b0` | `0x1400026b0` | 12 | ✓ |
| `fcn.140001000` | `0x140001000` | 8 | ✓ |
| `fcn.140002210` | `0x140002210` | 8 | ✓ |
| `fcn.140002250` | `0x140002250` | 8 | ✓ |
| `fcn.140002260` | `0x140002260` | 8 | ✓ |
| `fcn.140001e70` | `0x140001e70` | 8 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/entry1.c`](code/entry1.c)
- [`code/fcn.140001000.c`](code/fcn.140001000.c)
- [`code/fcn.140001010.c`](code/fcn.140001010.c)
- [`code/fcn.140001070.c`](code/fcn.140001070.c)
- [`code/fcn.1400012f0.c`](code/fcn.1400012f0.c)
- [`code/fcn.140001670.c`](code/fcn.140001670.c)
- [`code/fcn.140001bc0.c`](code/fcn.140001bc0.c)
- [`code/fcn.140001e70.c`](code/fcn.140001e70.c)
- [`code/fcn.140001e80.c`](code/fcn.140001e80.c)
- [`code/fcn.140001ed0.c`](code/fcn.140001ed0.c)
- [`code/fcn.140001f10.c`](code/fcn.140001f10.c)
- [`code/fcn.140001fb0.c`](code/fcn.140001fb0.c)
- [`code/fcn.140002050.c`](code/fcn.140002050.c)
- [`code/fcn.140002080.c`](code/fcn.140002080.c)
- [`code/fcn.1400020b0.c`](code/fcn.1400020b0.c)
- [`code/fcn.1400020f0.c`](code/fcn.1400020f0.c)
- [`code/fcn.1400021e0.c`](code/fcn.1400021e0.c)
- [`code/fcn.140002210.c`](code/fcn.140002210.c)
- [`code/fcn.140002220.c`](code/fcn.140002220.c)
- [`code/fcn.140002240.c`](code/fcn.140002240.c)
- [`code/fcn.140002250.c`](code/fcn.140002250.c)
- [`code/fcn.140002260.c`](code/fcn.140002260.c)
- [`code/fcn.140002290.c`](code/fcn.140002290.c)
- [`code/fcn.1400022f0.c`](code/fcn.1400022f0.c)
- [`code/fcn.140002360.c`](code/fcn.140002360.c)
- [`code/fcn.140002400.c`](code/fcn.140002400.c)
- [`code/fcn.1400026b0.c`](code/fcn.1400026b0.c)
- [`code/fcn.140002780.c`](code/fcn.140002780.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

### Analysis Summary
The binary is a sophisticated **malware loader/injector**. Its primary purpose is to elevate its own privileges and inject malicious code into legitimate system processes (specifically `svchost.exe`) using advanced techniques involving I/O Completion Ports (IOCP) to facilitate stealthy execution or network communication.

### Core Functionality
*   **Privilege Escalation:** The program starts by attempting to acquire high-level system privileges (`AdjustTokenPrivileges`). This is necessary for the malware to interact with and "touch" protected system processes like `svchost.exe`.
*   **Targeted Process Injection:** The code iterates through all running processes using `CreateToolhelp32Snapshot` and `Process32NextW`. It specifically looks for **`svchost.exe`**.
*   **Advanced Memory Manipulation:** Once a target process is found, it uses `VirtualAllocEx` and `WriteProcessMemory` to allocate space and copy "payload" data into the target's memory space.
*   **IOCP Exploitation/Technique:** The code specifically seeks out **IoCompletion ports** using `NtQueryInformationProcess`, `NtDuplicateObject`, and `NtQueryObject`. It then resolves and calls `ZwAssociateWaitCompletionPacket` from `ntdll.dll`. This is a sophisticated technique often used to associate the injected code with system-level I/O completions, which can help hide malicious network traffic or asynchronous operations from basic security monitors.

### Suspicious & Malicious Behaviors
*   **Process Injection:** The primary behavior is injecting code into `svchost.exe`. This is a classic technique used to hide malicious activity under the guise of a legitimate Windows service host.
*   **Privilege Escalation:** The use of `OpenProcessToken` and `LookupPrivilegeValueW` indicates an attempt to gain administrative/system-level permissions to perform actions that standard users cannot.
*   **Anti-Analysis / Anti-Debugging:**
    *   **IsDebuggerPresent:** Checks if the code is running under a debugger.
    *   **Vectored Exception Handling (VEH):** The use of `AddVectoredExceptionHandler` can be used to intercept exceptions and bypass certain debugger checks or "trap" debuggers.
    *   **Hardcoded Hostility:** The presence of strings like `"Go fuck your self and the Debugger"` suggests a deliberate attempt to frustrate reverse engineers.
    *   **Environment Fingerprinting:** Function `fcn.140002400` contains heavy CPUID-related checks (e.g., checking for specific instruction set features). This is commonly used to detect if the code is running in a virtual machine or an automated sandbox.
*   **Mutex Creation:** The use of a unique "Global" mutex (`Global\{FUCKYOUA...}`) ensures that only one instance of the malware runs at a time, preventing multiple copies from interfering with each other's injection logic.

### Notable Techniques & Patterns
*   **Native API Usage:** Instead of relying solely on standard Win32 APIs, the code frequently calls `ntdll.dll` functions (e.g., `NtQueryInformationProcess`, `ZwAssociateWaitCompletionPacket`). This is a common tactic to bypass basic security hooks and evade EDR (Endpoint Detection and Response) systems.
*   **Payload Staging:** The repetitive use of `VirtualAllocEx` with different sizes suggests the malware may be injecting multiple "stages" or components into the target process.
*   **Execution via Thread Pools:** The call to `CreateThreadpoolWait` inside the injected memory suggests it is preparing the code for execution in a way that mimics standard system behavior.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1068** | Exploitation for Privilege Escalation | The malware uses `AdjustTokenPrivileges` and `LookupPrivilegeValueW` to obtain the necessary permissions to interact with protected system processes. |
| **T1036** | Masquerading | By specifically targeting `svchost.exe`, the malware attempts to hide its presence among legitimate Windows services. |
| **T1055.001** | Process Injection | The use of `VirtualAllocEx` and `WriteProcessMemory` to insert payload data into a target process is a classic injection technique. |
| **T1435** | Anti-Debugging | The inclusion of `IsDebuggerPresent` and Vectored Exception Handling (VEH) is designed to detect and hinder the efforts of security researchers. |
| **T1497** | Virtualization/Sandbox Detection | Extensive CPUID-related checks are used to determine if the malware is running in a virtual machine or an automated analysis environment. |
| **T1027** | Software Packing (Payload Staging) | The use of multiple `VirtualAllocEx` calls for different sizes suggests a multi-stage loading process common in packed or modular malware. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `C:\Windows\mydll.dll` (Suspicious local DLL path)

**Mutex names / Named pipes**
*   `Global\{FUCKYOUA...` (Note: The full string appears to be a "hardcoded hostility" identifier used as a unique mutex to prevent multiple instances).

**Hashes**
*   None identified.

**Other artifacts**
*   **Target Process:** `svchost.exe` (Specifically targeted for code injection).
*   **Evasive API Sequences:** 
    *   `NtQueryInformationProcess`
    *   `ZwAssociateWaitCompletionPacket`
    *   `NtDuplicateObject`
    *   `NtQueryObject`
*   **Anti-Analysis/Debugging Signals:**
    *   Internal string: `"Go fuck your self and the Debugger"`
    *   Function `fcn.140002400` (Identified as a CPUID-based environment fingerprinting routine).
*   **Injection Techniques:** Use of `VirtualAllocEx`, `WriteProcessMemory`, and `CreateThreadpoolWait`.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2020/WindowsSettings`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
* **Sophisticated Injection & Evasion:** The sample employs advanced techniques to bypass security monitors, specifically using `ntdll.dll` functions (like `ZwAssociateWaitCompletionPacket`) and I/O Completion Ports (IOCP) to hide its activity within the `svchost.exe` process.
* **Advanced Anti-Analysis Suite:** It features multiple layers of defense against researchers, including environment fingerprinting via CPUID checks (to detect VMs/sandboxes), Vectored Exception Handling (VEH) to bypass debugger checks, and explicit "hardcoded" anti-debugging messages.
* **Multi-stage Loading Behavior:** The use of multiple `VirtualAllocEx` calls and the transition from a loader's role—elevating privileges and injecting code into system processes—indicates it is designed to deliver and execute a more complex primary payload (such as a RAT or botnet agent) in a stealthy manner.
