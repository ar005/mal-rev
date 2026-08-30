# Threat Analysis Report

**Generated:** 2026-08-22 06:48 UTC
**Sample:** `110182bcba9055dd0da11daa323974782d601c89645397ab70e8c26cf8b8a573_110182bcba9055dd0da11daa323974782d601c89645397ab70e8c26cf8b8a573.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `110182bcba9055dd0da11daa323974782d601c89645397ab70e8c26cf8b8a573_110182bcba9055dd0da11daa323974782d601c89645397ab70e8c26cf8b8a573.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 14,059,008 bytes |
| MD5 | `efe0ec83c3bfe308c6013fd720ad12ce` |
| SHA1 | `617ef0f4ef992e5220b1523bf7857679e5256840` |
| SHA256 | `110182bcba9055dd0da11daa323974782d601c89645397ab70e8c26cf8b8a573` |
| Overall entropy | 7.996 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1776370330 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 4,096 | 5.838 | No |
| `.rdata` | 4,608 | 4.005 | No |
| `.data` | 14,047,744 | 7.996 | ⚠️ Yes |
| `.pdata` | 512 | 3.168 | No |
| `.rsrc` | 512 | 4.718 | No |
| `.reloc` | 512 | 0.657 | No |

### Imports

**KERNEL32.dll**: `WriteFile`, `TerminateProcess`, `GetTempPathW`, `CreateMutexA`, `CreateFileW`, `OpenProcess`, `CreateToolhelp32Snapshot`, `Sleep`, `GetTickCount64`, `GetLastError`, `Process32NextW`, `Process32FirstW`, `CloseHandle`, `ExitProcess`, `CreateProcessW`
**USER32.dll**: `wsprintfW`
**VCRUNTIME140.dll**: `__C_specific_handler`, `__current_exception`, `__current_exception_context`, `memset`, `memcpy`
**api-ms-win-crt-string-l1-1-0.dll**: `_wcsicmp`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_cexit`, `_exit`, `_seh_filter_exe`, `_initterm`, `_register_thread_local_exe_atexit_callback`, `_register_onexit_function`, `_crt_atexit`, `terminate`, `_set_app_type`, `_initialize_onexit_table`, `_c_exit`, `_configure_wide_argv`, `_initterm_e`, `_get_wide_winmain_command_line`, `_initialize_wide_environment`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__p__commode`, `_set_fmode`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`
**api-ms-win-crt-heap-l1-1-0.dll**: `_set_new_mode`

## Extracted Strings

Total strings found: **31532** (showing first 100)

```
!This program cannot be run in DOS mode.
$
VRichF
`.rdata
@.data
.pdata
@.rsrc
@.reloc
uxHcH
u0HcH<
Global\RunerInstallerSMTPoK_12345
C:\Users\vboxuser\source\repos\Launcher\x64\Release\Launcher.pdb
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
WriteFile
TerminateProcess
GetTempPathW
CreateMutexA
CreateFileW
OpenProcess
CreateToolhelp32Snapshot
GetTickCount64
GetLastError
Process32NextW
Process32FirstW
CloseHandle
ExitProcess
CreateProcessW
KERNEL32.dll
wsprintfW
USER32.dll
__C_specific_handler
__current_exception
__current_exception_context
memset
VCRUNTIME140.dll
_wcsicmp
_seh_filter_exe
_set_app_type
__setusermatherr
_configure_wide_argv
_initialize_wide_environment
_get_wide_winmain_command_line
_initterm
_initterm_e
_set_fmode
_cexit
_c_exit
_register_thread_local_exe_atexit_callback
_configthreadlocale
_set_new_mode
__p__commode
_initialize_onexit_table
_register_onexit_function
_crt_atexit
terminate
api-ms-win-crt-string-l1-1-0.dll
api-ms-win-crt-runtime-l1-1-0.dll
api-ms-win-crt-math-l1-1-0.dll
api-ms-win-crt-stdio-l1-1-0.dll
api-ms-win-crt-locale-l1-1-0.dll
api-ms-win-crt-heap-l1-1-0.dll
QueryPerformanceCounter
GetCurrentProcessId
GetCurrentThreadId
GetSystemTimeAsFileTime
InitializeSListHead
SetUnhandledExceptionFilter
GetStartupInfoW
GetModuleHandleW
memcpy
!This program cannot be run in DOS mode.
$
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140001abc` | `0x140001abc` | 667 | ✓ |
| `fcn.140001340` | `0x140001340` | 660 | ✓ |
| `fcn.140001100` | `0x140001100` | 545 | ✓ |
| `entry0` | `0x1400015b8` | 390 | ✓ |
| `section..text` | `0x140001000` | 251 | ✓ |
| `fcn.140001814` | `0x140001814` | 175 | ✓ |
| `fcn.1400016d8` | `0x1400016d8` | 152 | ✓ |
| `fcn.14000164c` | `0x14000164c` | 139 | ✓ |
| `fcn.140001e28` | `0x140001e28` | 99 | ✓ |
| `fcn.140001984` | `0x140001984` | 82 | ✓ |
| `fcn.140001a44` | `0x140001a44` | 60 | ✓ |
| `fcn.1400017c0` | `0x1400017c0` | 58 | ✓ |
| `fcn.140001610` | `0x140001610` | 58 | ✓ |
| `fcn.140001940` | `0x140001940` | 58 | ✓ |
| `fcn.1400015d4` | `0x1400015d4` | 57 | ✓ |
| `fcn.140001794` | `0x140001794` | 41 | ✓ |
| `fcn.140001770` | `0x140001770` | 36 | ✓ |
| `fcn.140001900` | `0x140001900` | 27 | ✓ |
| `fcn.1400017fc` | `0x1400017fc` | 23 | ✓ |
| `fcn.1400018d8` | `0x1400018d8` | 14 | ✓ |
| `fcn.1400019d8` | `0x1400019d8` | 14 | ✓ |
| `fcn.14000191c` | `0x14000191c` | 12 | ✓ |
| `fcn.140001d58` | `0x140001d58` | 12 | ✓ |
| `fcn.1400018f0` | `0x1400018f0` | 8 | ✓ |
| `fcn.1400018f8` | `0x1400018f8` | 8 | ✓ |
| `fcn.140001928` | `0x140001928` | 8 | ✓ |
| `fcn.140001930` | `0x140001930` | 8 | ✓ |
| `sub.api_ms_win_crt_runtime_l1_1_0.dll__set_app_type` | `0x140001d8e` | 6 | ✓ |
| `fcn.1400018d0` | `0x1400018d0` | 6 | ✓ |
| `sub.api_ms_win_crt_stdio_l1_1_0.dll__set_fmode` | `0x140001dc4` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.140001100.c`](code/fcn.140001100.c)
- [`code/fcn.140001340.c`](code/fcn.140001340.c)
- [`code/fcn.1400015d4.c`](code/fcn.1400015d4.c)
- [`code/fcn.140001610.c`](code/fcn.140001610.c)
- [`code/fcn.14000164c.c`](code/fcn.14000164c.c)
- [`code/fcn.1400016d8.c`](code/fcn.1400016d8.c)
- [`code/fcn.140001770.c`](code/fcn.140001770.c)
- [`code/fcn.140001794.c`](code/fcn.140001794.c)
- [`code/fcn.1400017c0.c`](code/fcn.1400017c0.c)
- [`code/fcn.1400017fc.c`](code/fcn.1400017fc.c)
- [`code/fcn.140001814.c`](code/fcn.140001814.c)
- [`code/fcn.1400018d0.c`](code/fcn.1400018d0.c)
- [`code/fcn.1400018d8.c`](code/fcn.1400018d8.c)
- [`code/fcn.1400018f0.c`](code/fcn.1400018f0.c)
- [`code/fcn.1400018f8.c`](code/fcn.1400018f8.c)
- [`code/fcn.140001900.c`](code/fcn.140001900.c)
- [`code/fcn.14000191c.c`](code/fcn.14000191c.c)
- [`code/fcn.140001928.c`](code/fcn.140001928.c)
- [`code/fcn.140001930.c`](code/fcn.140001930.c)
- [`code/fcn.140001940.c`](code/fcn.140001940.c)
- [`code/fcn.140001984.c`](code/fcn.140001984.c)
- [`code/fcn.1400019d8.c`](code/fcn.1400019d8.c)
- [`code/fcn.140001a44.c`](code/fcn.140001a44.c)
- [`code/fcn.140001abc.c`](code/fcn.140001abc.c)
- [`code/fcn.140001d58.c`](code/fcn.140001d58.c)
- [`code/fcn.140001e28.c`](code/fcn.140001e28.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sub.api_ms_win_crt_runtime_l1_1_0.dll__set_app_type.c`](code/sub.api_ms_win_crt_runtime_l1_1_0.dll__set_app_type.c)
- [`code/sub.api_ms_win_crt_stdio_l1_1_0.dll__set_fmode.c`](code/sub.api_ms_win_crt_stdio_l1_1_0.dll__set_fmode.c)

## Behavioral Analysis

### Malware Analysis Report

The provided code is characteristic of a **dropper**—a type of malware designed to install and execute a secondary payload while attempting to evade detection.

#### Core Functionality
The primary purpose of this binary is to "drop" an embedded executable into a temporary directory, launch it, and then remain active in the background for several minutes to ensure the launched process has sufficient time to perform its tasks (such as establishing network connections or persisting on the system).

#### Suspicious and Malicious Behaviors
*   **Payload Extraction (File Dropping):** 
    The code uses `GetTempPathW` to locate the system's temporary directory and then creates a file named **"updater.exe"**. It proceeds to write a large blob of data (approx. 13MB) from its own memory space into this new file using `WriteFile`. This is a classic indicator that the primary malicious payload is hidden within this initial "loader."
*   **Process Execution:** 
    Immediately after writing "updater.exe," the code calls `CreateProcessW` to execute it. This transition from a loader to a functional malware component is typical in multi-stage infections.
*   **Process Termination (Targeted Activity):** 
    The function `section..text` contains a loop that enumerates all running system processes using `CreateToolhelp32Snapshot`. It specifically looks for **"Telegram.exe"**. If found, the code attempts to open the process and terminate it via `TerminateProcess`. This suggests an intent to disrupt communication or security measures on the victim's machine.
*   **Execution Delay (Evasion):** 
    After launching the "updater.exe," the binary enters a loop where it calls `Sleep(500)` repeatedly, checking `GetTickCount64` until approximately 360,000 ticks have passed (roughly 10 minutes). This is designed to keep the dropper alive long enough for the payload to complete its initialization or connect to a Command and Control (C2) server.
*   **Anti-Analysis/Evasion:** 
    The function `fcn.140001abc` performs extensive CPU instruction checks (CPUID). While this can be for legitimate performance reasons, in malware, it is frequently used to detect virtualized environments or specialized debugging tools.

#### Notable Techniques & Patterns
*   **Mutex Creation:** The use of a unique mutex (`Global\RunerInstallerSMTPoK_12345`) ensures that only one instance of the "updater" logic runs at a time, preventing multiple instances from competing for resources or alerting the user with multiple windows.
*   **Use of System Temp Folders:** Dropping files into `GetTempPathW` is a common tactic because these folders often have loose permissions and are rarely checked by casual users.
*   **Staged Execution:** By using a small loader to drop a larger "updater" file, the malware can bypass initial security scans that might only scan the first executable launched by the user.

### Summary Table of Indicators
| Behavior | Technique | Purpose |
| :--- | :--- | :--- |
| **Dropping** | `CreateFileW` / `WriteFile` to "updater.exe" | Extracting the main payload from memory to disk. |
| **Termination** | `Process32NextW` / `TerminateProcess` on "Telegram.exe" | Disabling communication apps or security tools. |
| **Delay** | `Sleep()` loop for ~10 minutes | Ensuring the payload has time to establish persistence/C2. |
| **Evasion** | Complex CPU feature (CPUID) checks | Detecting and avoiding analysis environments (VMs/Emulators). |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The malware names the dropped file "updater.exe" and places it in a common temporary directory to blend in with legitimate system processes. |
| **T1562.001** | Impair Defenses: Disable or Remove Security Software | Terminating "Telegram.exe" is an attempt to disable communication tools that could alert the user or provide a channel for security response. |
| **T1497** | Virtualization/Sandbox Detection | The use of CPUID instructions (fcn.140001abc) is a standard method used to detect if the code is running in a virtualized environment. |
| **T1568** | Dynamic Resolution | While not explicitly listed as an ID for "Sleep," the 10-minute delay and the use of various system calls are part of broader defense evasion tactics to stall automated analysis. |

*(Note: For "Execution Delay" specifically, while it is a primary component of **Defense Evasion**, it does not always have a unique sub-technique identifier in every version of the framework; however, it is consistently categorized under the overarching Defense Evasion tactic.)*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `updater.exe` (Dropped payload filename)

**Mutex names / Named pipes**
*   `Global\RunerInstallerSMTPoK_12345`

**Hashes**
*   None identified.

**Other artifacts**
*   **Targeted Process:** `Telegram.exe` (The malware specifically seeks out and terminates this process).
*   **Execution Delay Pattern:** A sleep loop of approximately 360,000 ticks (approx. 10 minutes) following the drop to provide time for C2 establishment.
*   **Evasion Technique:** Use of `CPUID` instruction checks to detect virtualized/debugged environments.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family**: custom
2. **Malware type**: dropper / loader
3. **Confidence**: High (for type) / Medium (for family)
4. **Key evidence**:
    *   **Payload Delivery:** The sample performs classic "dropper" behavior by extracting a large, hidden executable (`updater.exe`) from its own memory and executing it in a temporary directory to facilitate multi-stage infection.
    *   **Specific Target Interference:** The intentional termination of `Telegram.exe` indicates a targeted effort to disrupt the victim's communication channels or disable specific applications used for reporting/security.
    *   **Evasion Tactics:** The use of `CPUID` instructions to detect virtualized environments and a 10-minute sleep loop are standard techniques used to bypass automated sandbox analysis and delay detection during execution.
