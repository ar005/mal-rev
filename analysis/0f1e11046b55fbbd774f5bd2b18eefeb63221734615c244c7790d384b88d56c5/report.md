# Threat Analysis Report

**Generated:** 2026-08-15 19:32 UTC
**Sample:** `0f1e11046b55fbbd774f5bd2b18eefeb63221734615c244c7790d384b88d56c5_0f1e11046b55fbbd774f5bd2b18eefeb63221734615c244c7790d384b88d56c5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f1e11046b55fbbd774f5bd2b18eefeb63221734615c244c7790d384b88d56c5_0f1e11046b55fbbd774f5bd2b18eefeb63221734615c244c7790d384b88d56c5.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 6 sections |
| Size | 24,064 bytes |
| MD5 | `24052d0865d5db6f9943f7430df550fd` |
| SHA1 | `0c74ae1ed95eab50897d2801b31e9ec95d1713d8` |
| SHA256 | `0f1e11046b55fbbd774f5bd2b18eefeb63221734615c244c7790d384b88d56c5` |
| Overall entropy | 4.767 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768936658 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 7,680 | 5.809 | No |
| `.rdata` | 13,312 | 3.833 | No |
| `.data` | 512 | 0.532 | No |
| `.pdata` | 512 | 3.721 | No |
| `.rsrc` | 512 | 4.702 | No |
| `.reloc` | 512 | 0.745 | No |

### Imports

**WTSAPI32.dll**: `WTSQueryUserToken`, `WTSEnumerateSessionsW`, `WTSFreeMemory`
**USERENV.dll**: `CreateEnvironmentBlock`, `DestroyEnvironmentBlock`
**KERNEL32.dll**: `GetModuleFileNameW`, `GetFileAttributesW`, `GetVersionExW`, `GetCurrentProcess`, `CloseHandle`, `GetSystemTimeAsFileTime`, `GetCurrentThreadId`, `GetCurrentProcessId`, `QueryPerformanceCounter`, `GetModuleHandleW`, `RtlVirtualUnwind`, `RtlLookupFunctionEntry`, `RtlCaptureContext`, `GetLastError`, `UnhandledExceptionFilter`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `CreateProcessAsUserW`, `DuplicateTokenEx`, `OpenProcessToken`, `LookupAccountSidW`, `GetTokenInformation`, `LookupPrivilegeValueW`
**VCRUNTIME140.dll**: `__current_exception`, `memset`, `wcsrchr`, `__C_specific_handler`, `__current_exception_context`, `memcpy`
**api-ms-win-crt-stdio-l1-1-0.dll**: `_set_fmode`, `__stdio_common_vswprintf_s`, `__p__commode`, `setvbuf`, `__acrt_iob_func`, `__stdio_common_vfwprintf`
**api-ms-win-crt-string-l1-1-0.dll**: `wcslen`, `wcscat_s`, `_wcsicmp`
**api-ms-win-crt-heap-l1-1-0.dll**: `malloc`, `free`, `_set_new_mode`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_register_thread_local_exe_atexit_callback`, `_cexit`, `__p___wargv`, `__p___argc`, `_exit`, `_initialize_onexit_table`, `_register_onexit_function`, `_crt_atexit`, `terminate`, `_initialize_wide_environment`, `exit`, `_initterm_e`, `_seh_filter_exe`, `_c_exit`, `_get_initial_wide_environment`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

## Extracted Strings

Total strings found: **124** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
L$ SUVWH
VWATAVAWH
A_A^A\_^
9\$@vUL
H SVWH
uxHc,
u0HcH<
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
.CRT$XPA
.CRT$XPZ
.CRT$XTA
.CRT$XTZ
.rdata
.rdata$voltmd
.rdata$zzzdbg
.rtc$IAA
.rtc$IZZ
.rtc$TAA
.rtc$TZZ
.xdata
.idata$2
.idata$3
.idata$4
.idata$6
.pdata
.rsrc$01
.rsrc$02
p`P0
WTSQueryUserToken
WTSEnumerateSessionsW
WTSFreeMemory
WTSAPI32.dll
DestroyEnvironmentBlock
CreateEnvironmentBlock
USERENV.dll
GetCurrentProcess
GetModuleFileNameW
GetFileAttributesW
GetVersionExW
GetLastError
CloseHandle
KERNEL32.dll
GetTokenInformation
LookupAccountSidW
OpenProcessToken
DuplicateTokenEx
CreateProcessAsUserW
AdjustTokenPrivileges
LookupPrivilegeValueW
ADVAPI32.dll
wcsrchr
__C_specific_handler
__current_exception
__current_exception_context
memset
VCRUNTIME140.dll
__stdio_common_vswprintf_s
__acrt_iob_func
_wcsicmp
__stdio_common_vfwprintf
wcscat_s
setvbuf
wcslen
malloc
_seh_filter_exe
_set_app_type
__setusermatherr
_configure_wide_argv
_initialize_wide_environment
_get_initial_wide_environment
_initterm
_initterm_e
_set_fmode
__p___argc
__p___wargv
_cexit
_c_exit
_register_thread_local_exe_atexit_callback
_configthreadlocale
_set_new_mode
__p__commode
_initialize_onexit_table
_register_onexit_function
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14000179c` | `0x14000179c` | 958 | ✓ |
| `main` | `0x140001324` | 892 | ✓ |
| `fcn.1400027ec` | `0x1400027ec` | 661 | ✓ |
| `fcn.140001174` | `0x140001174` | 432 | ✓ |
| `entry0` | `0x1400021dc` | 398 | ✓ |
| `fcn.140002558` | `0x140002558` | 331 | ✓ |
| `fcn.140001de0` | `0x140001de0` | 295 | ✓ |
| `fcn.140001b5c` | `0x140001b5c` | 295 | ✓ |
| `fcn.1400016a0` | `0x1400016a0` | 251 | ✓ |
| `fcn.140001c84` | `0x140001c84` | 236 | ✓ |
| `fcn.1400010b0` | `0x1400010b0` | 195 | ✓ |
| `fcn.140002430` | `0x140002430` | 175 | ✓ |
| `fcn.1400022f4` | `0x1400022f4` | 152 | ✓ |
| `fcn.140002268` | `0x140002268` | 139 | ✓ |
| `fcn.140001f08` | `0x140001f08` | 116 | ✓ |
| `fcn.140002b54` | `0x140002b54` | 96 | ✓ |
| `fcn.140001d70` | `0x140001d70` | 88 | ✓ |
| `fcn.140001058` | `0x140001058` | 86 | ✓ |
| `fcn.1400026ac` | `0x1400026ac` | 82 | ✓ |
| `fcn.140001008` | `0x140001008` | 80 | ✓ |
| `fcn.140002774` | `0x140002774` | 60 | ✓ |
| `fcn.1400023dc` | `0x1400023dc` | 58 | ✓ |
| `fcn.14000222c` | `0x14000222c` | 58 | ✓ |
| `fcn.1400021f0` | `0x1400021f0` | 57 | ✓ |
| `fcn.140001e00` | `0x140001e00` | 52 | ✓ |
| `fcn.1400023b0` | `0x1400023b0` | 41 | ✓ |
| `fcn.14000238c` | `0x14000238c` | 36 | ✓ |
| `fcn.140002514` | `0x140002514` | 27 | ✓ |
| `fcn.140002418` | `0x140002418` | 23 | ✓ |
| `fcn.1400024f4` | `0x1400024f4` | 14 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.140001008.c`](code/fcn.140001008.c)
- [`code/fcn.140001058.c`](code/fcn.140001058.c)
- [`code/fcn.1400010b0.c`](code/fcn.1400010b0.c)
- [`code/fcn.140001174.c`](code/fcn.140001174.c)
- [`code/fcn.1400016a0.c`](code/fcn.1400016a0.c)
- [`code/fcn.14000179c.c`](code/fcn.14000179c.c)
- [`code/fcn.140001b5c.c`](code/fcn.140001b5c.c)
- [`code/fcn.140001c84.c`](code/fcn.140001c84.c)
- [`code/fcn.140001d70.c`](code/fcn.140001d70.c)
- [`code/fcn.140001de0.c`](code/fcn.140001de0.c)
- [`code/fcn.140001e00.c`](code/fcn.140001e00.c)
- [`code/fcn.140001f08.c`](code/fcn.140001f08.c)
- [`code/fcn.1400021f0.c`](code/fcn.1400021f0.c)
- [`code/fcn.14000222c.c`](code/fcn.14000222c.c)
- [`code/fcn.140002268.c`](code/fcn.140002268.c)
- [`code/fcn.1400022f4.c`](code/fcn.1400022f4.c)
- [`code/fcn.14000238c.c`](code/fcn.14000238c.c)
- [`code/fcn.1400023b0.c`](code/fcn.1400023b0.c)
- [`code/fcn.1400023dc.c`](code/fcn.1400023dc.c)
- [`code/fcn.140002418.c`](code/fcn.140002418.c)
- [`code/fcn.140002430.c`](code/fcn.140002430.c)
- [`code/fcn.1400024f4.c`](code/fcn.1400024f4.c)
- [`code/fcn.140002514.c`](code/fcn.140002514.c)
- [`code/fcn.140002558.c`](code/fcn.140002558.c)
- [`code/fcn.1400026ac.c`](code/fcn.1400026ac.c)
- [`code/fcn.140002774.c`](code/fcn.140002774.c)
- [`code/fcn.1400027ec.c`](code/fcn.1400027ec.c)
- [`code/fcn.140002b54.c`](code/fcn.140002b54.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

This binary appears to be a **malicious loader or "dropper"** designed to perform **cross-session execution and privilege escalation**. Its primary purpose is to move execution from a standard user's session into another session (such as a system-level or administrative session) to bypass security restrictions.

### Core Functionality and Purpose
The core logic revolves around identifying other active user sessions on the machine, stealing their security tokens, and spawning a new process in those sessions. This is a common technique used by malware to "escape" restricted environments or move from a low-privilege context to a high-privilege (SYSTEM) context.

### Suspicious and Malicious Behaviors
*   **Cross-Session Execution:** The code uses `WTSEnumerateSessionsW` to find all active sessions and `WTSQueryUserToken` to retrieve the security token of users in those sessions. 
*   **Privilege Escalation:** The function `fcn.14000179c` explicitly attempts to enable high-level system privileges using `AdjustTokenPrivileges`. Specifically, it seeks:
    *   `SeTcbPrivilege`: A very powerful privilege typically reserved for the SYSTEM account.
    *   `SeAssignPrimaryTokenPrivilege`: Used to assign a new token to a process.
    *   `SeIncreaseQuotaPrivilege`: Often used in conjunction with other system-level operations.
*   **Token Manipulation:** The binary uses `DuplicateTokenEx` and `CreateEnvironmentBlock`. These are standard Windows APIs, but their use together—especially after querying user tokens via `WTSAPI32.dll`—indicates an intent to impersonate another user's identity and environment.
*   **Process Injection/Creation:** The final step of the logic is calling `CreateProcessAsUserW`. This allows the malware to launch a new process (like a payload or a remote-control agent) while masquerading as the user identified in the high-privilege session.

### Notable Techniques and Patterns
*   **Session Hopping:** By leveraging `WTSAPI32.dll`, the malware can jump from a standard "User" desktop to a "System" desktop. This is frequently used to evade User Account Control (UAC) or sandbox restrictions.
*   **Anti-Analysis/Evasion Logic:** 
    *   The inclusion of `IsDebuggerPresent` and several complex initialization routines (e.g., `fcn.1400027ec`) suggests the malware is prepared to detect if it is being analyzed in a sandbox or under a debugger.
    *   The heavy use of "Debug" logs in the disassembly (e.g., `" [DEBUG] Falha ao habilitar SE_TCB_NAME"`) indicates that while the code was likely produced by a developer/threat actor, these strings might be left over from a development phase or used to debug the injection logic before final deployment.
*   **Credential/Token Theft:** Instead of stealing a password, it steals the **token**, which is a much more "silent" way to gain privileges because it doesn't require the user to re-authenticate.

### Summary Table of Key Indicators
| Behavior | Associated API / Function | Threat Significance |
| :--- | :--- | :--- |
| **Session Enumeration** | `WTSEnumerateSessionsW` | Identifying other users/system sessions on the PC. |
| **Token Theft** | `WTSQueryUserToken`, `DuplicateTokenEx` | Stealing a session's credentials to bypass security. |
| **Privilege Escalation** | `AdjustTokenPrivileges` (SeTcbPrivilege) | Attempting to gain system-level authority. |
| **Targeted Execution** | `CreateProcessAsUserW` | Launching the final payload in a privileged context. |
| **Evasion** | `IsDebuggerPresent`, `RtlCaptureContext` | Standard techniques to hide from security researchers. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1134** | Token Manipulation | The malware uses `WTSQueryUserToken` and `DuplicateTokenEx` to steal and replicate security tokens from other sessions to impersonate higher-privileged users. |
| **T1068** | Exploitation for Privilege Escalation | The deliberate attempt to enable high-level system privileges (e.g., `SeTcbPrivilege`) via `AdjustTokenPrivileges` indicates a direct effort to gain administrative authority. |
| **T1562** | Defensive Evasion | The inclusion of `IsDebuggerPresent` and complex initialization routines suggests the malware is designed to detect and bypass security analysis tools. |
| **T1082** | System Information Discovery | The use of `WTSEnumerateSessionsW` allows the threat actor to map out active user sessions on the local system to identify targets for token theft. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Standard Windows libraries (e.g., KERNEL32.dll), common API calls, and assembly offsets have been excluded as they are not unique to this specific threat.*

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: System library names like `WTSAPI32.dll` or `USERENV.dll` were omitted as they are standard Windows components).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Internal Debug String:** `" [DEBUG] Falha ao habilitar SE_TCB_NAME"` (This Portuguese string indicates a specific developer artifact and can be used to identify this specific build/family).
*   **Malicious Behavior Signatures (TTPs):** 
    *   **Session Hopping Pattern:** Use of `WTSEnumerateSessionsW` combined with `WTSQueryUserToken` to facilitate cross-session execution.
    *   **Privilege Escalation Targets:** Specific targeting of `SeTcbPrivilege`, `SeAssignPrimaryTokenPrivilege`, and `SeIncreaseQuotaPrivilege`.
    *   **Credentialless Token Theft:** Use of `DuplicateTokenEx` and `CreateEnvironmentBlock` to impersonate high-privilege tokens without requiring user passwords.
    *   **Evasion Techniques:** Implementation of `IsDebuggerPresent` and `RtlCaptureContext` for anti-analysis purposes.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family:** custom
2. **Malware type:** loader / dropper
3. **Confidence:** High
4. **Key evidence:** 
    * **Cross-Session Token Theft:** The binary utilizes `WTSQueryUserToken` and `DuplicateTokenEx` to perform "session hopping," a technique used to steal security tokens from higher-privileged sessions (like SYSTEM) to bypass UAC restrictions.
    * **Privilege Escalation Logic:** The explicit targeting of high-level system privileges, specifically `SeTcbPrivilege`, indicates an intentional effort to gain administrative control over the operating system.
    * **Evasive Delivery Mechanism:** The use of `CreateProcessAsUserW` following token manipulation confirms its role as a loader designed to execute and "protect" a secondary payload within a high-privilege context.
