# Threat Analysis Report

**Generated:** 2026-08-20 23:06 UTC
**Sample:** `10d6f24410931b5dd5ad38c3aa410026693d55a904d3dbcebd0ffe608d186044_10d6f24410931b5dd5ad38c3aa410026693d55a904d3dbcebd0ffe608d186044.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10d6f24410931b5dd5ad38c3aa410026693d55a904d3dbcebd0ffe608d186044_10d6f24410931b5dd5ad38c3aa410026693d55a904d3dbcebd0ffe608d186044.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 5 sections |
| Size | 31,992 bytes |
| MD5 | `d81167bf42a4c1048567cf8dc4fed5c5` |
| SHA1 | `a9553a0318e15dc7c58b8bfb0febcf59bbdff3d9` |
| SHA256 | `10d6f24410931b5dd5ad38c3aa410026693d55a904d3dbcebd0ffe608d186044` |
| Overall entropy | 7.083 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1754990036 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 3,584 | 5.906 | No |
| `.rdata` | 3,072 | 4.48 | No |
| `.data` | 512 | 0.28 | No |
| `.rsrc` | 2,048 | 3.689 | No |
| `.reloc` | 512 | 4.836 | No |

### Imports

**dsp_bridge.dll**: `HostMainLoop`
**VCRUNTIME140.dll**: `__current_exception`, `__current_exception_context`, `memset`, `_except_handler4_common`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_initialize_onexit_table`, `_c_exit`, `_crt_atexit`, `_controlfp_s`, `terminate`, `_register_thread_local_exe_atexit_callback`, `_configure_wide_argv`, `_set_app_type`, `_initialize_wide_environment`, `_register_onexit_function`, `_seh_filter_exe`, `_cexit`, `_exit`, `exit`, `_initterm_e`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__p__commode`, `_set_fmode`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`
**api-ms-win-crt-heap-l1-1-0.dll**: `_set_new_mode`
**KERNEL32.dll**: `IsDebuggerPresent`, `GetModuleHandleW`, `GetCurrentProcessId`, `QueryPerformanceCounter`, `IsProcessorFeaturePresent`, `TerminateProcess`, `GetCurrentProcess`, `SetUnhandledExceptionFilter`, `UnhandledExceptionFilter`, `GetSystemTimeAsFileTime`, `InitializeSListHead`, `GetCurrentThreadId`, `GetStartupInfoW`

## Extracted Strings

Total strings found: **261** (showing first 100)

```
!This program cannot be run in DOS mode.
$
V]Rich
`.rdata
@.data
@.reloc
M;Jr

u"h@3@
D:\buildbot\build1\dsp_bridge\build\bin\Release\bridge_plugin_host.pdb
.text$mn
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
.rdata$sxdata
.rdata$voltmd
.rdata$zzzdbg
.rtc$IAA
.rtc$IZZ
.rtc$TAA
.rtc$TZZ
.xdata$x
.idata$2
.idata$3
.idata$4
.idata$6
.rsrc$01
.rsrc$02
HostMainLoop
dsp_bridge.dll
__current_exception
__current_exception_context
memset
_except_handler4_common
VCRUNTIME140.dll
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
_controlfp_s
terminate
api-ms-win-crt-runtime-l1-1-0.dll
api-ms-win-crt-math-l1-1-0.dll
api-ms-win-crt-stdio-l1-1-0.dll
api-ms-win-crt-locale-l1-1-0.dll
api-ms-win-crt-heap-l1-1-0.dll
UnhandledExceptionFilter
SetUnhandledExceptionFilter
GetCurrentProcess
TerminateProcess
IsProcessorFeaturePresent
QueryPerformanceCounter
GetCurrentProcessId
GetCurrentThreadId
GetSystemTimeAsFileTime
InitializeSListHead
IsDebuggerPresent
GetStartupInfoW
GetModuleHandleW
KERNEL32.dll
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0"><trustInfo xmlns="urn:schemas-microsoft-com:asm.v3"><security><requestedPrivileges><requestedExecutionLevel level="asInvoker" uiAccess="false"></requestedExecutionLevel></requestedPrivileges></security></trustInfo><application xmlns="urn:schemas-microsoft-com:asm.v3"><windowsSettings><dpiAware xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">True/PM</dpiAware></windowsSettings></application></assembly>
1'1,111R1W1d1
3 3)3.343>3H3X3h3x3
34@4f4u4
6,6f6o6
9"9'9:9Q9n9
;;;;D;M;[;d;
<$<*<0<6<<<F<
0<1@1H1
0e10	
DigiCert Inc1
www.digicert.com1$0"
DigiCert Assured ID Root CA0
220801000000Z
311109235959Z0b10	
DigiCert Inc1
www.digicert.com1!0
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004019c4` | `0x4019c4` | 468 | ✓ |
| `entry0` | `0x401260` | 390 | ✓ |
| `fcn.004016f6` | `0x4016f6` | 283 | ✓ |
| `fcn.004014c2` | `0x4014c2` | 148 | ✓ |
| `fcn.0040143b` | `0x40143b` | 135 | ✓ |
| `fcn.00401c40` | `0x401c40` | 120 | ✓ |
| `fcn.004015dd` | `0x4015dd` | 77 | ✓ |
| `fcn.0040162a` | `0x40162a` | 75 | ✓ |
| `fcn.00401950` | `0x401950` | 69 | ✓ |
| `fcn.0040138c` | `0x40138c` | 68 | ✓ |
| `fcn.00401847` | `0x401847` | 66 | ✓ |
| `fcn.00401402` | `0x401402` | 57 | ✓ |
| `fcn.004013d0` | `0x4013d0` | 50 | ✓ |
| `fcn.00401811` | `0x401811` | 49 | ✓ |
| `fcn.0040159b` | `0x40159b` | 45 | ✓ |
| `fcn.004018f3` | `0x4018f3` | 44 | ✓ |
| `fcn.00401573` | `0x401573` | 40 | ✓ |
| `fcn.0040126a` | `0x40126a` | 40 | ✓ |
| `fcn.00401691` | `0x401691` | 33 | ✓ |
| `fcn.004016c1` | `0x4016c1` | 29 | ✓ |
| `fcn.00401556` | `0x401556` | 29 | ✓ |
| `fcn.004015c8` | `0x4015c8` | 21 | ✓ |
| `main` | `0x401000` | 17 | ✓ |
| `fcn.00401b98` | `0x401b98` | 12 | ✓ |
| `fcn.00401682` | `0x401682` | 12 | ✓ |
| `fcn.004016de` | `0x4016de` | 12 | ✓ |
| `fcn.00401889` | `0x401889` | 12 | ✓ |
| `fcn.004018eb` | `0x4018eb` | 8 | ✓ |
| `sub.api_ms_win_crt_runtime_l1_1_0.dll__set_app_type` | `0x401bc2` | 6 | ✓ |
| `fcn.0040167c` | `0x40167c` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040126a.c`](code/fcn.0040126a.c)
- [`code/fcn.0040138c.c`](code/fcn.0040138c.c)
- [`code/fcn.004013d0.c`](code/fcn.004013d0.c)
- [`code/fcn.00401402.c`](code/fcn.00401402.c)
- [`code/fcn.0040143b.c`](code/fcn.0040143b.c)
- [`code/fcn.004014c2.c`](code/fcn.004014c2.c)
- [`code/fcn.00401556.c`](code/fcn.00401556.c)
- [`code/fcn.00401573.c`](code/fcn.00401573.c)
- [`code/fcn.0040159b.c`](code/fcn.0040159b.c)
- [`code/fcn.004015c8.c`](code/fcn.004015c8.c)
- [`code/fcn.004015dd.c`](code/fcn.004015dd.c)
- [`code/fcn.0040162a.c`](code/fcn.0040162a.c)
- [`code/fcn.0040167c.c`](code/fcn.0040167c.c)
- [`code/fcn.00401682.c`](code/fcn.00401682.c)
- [`code/fcn.00401691.c`](code/fcn.00401691.c)
- [`code/fcn.004016c1.c`](code/fcn.004016c1.c)
- [`code/fcn.004016de.c`](code/fcn.004016de.c)
- [`code/fcn.004016f6.c`](code/fcn.004016f6.c)
- [`code/fcn.00401811.c`](code/fcn.00401811.c)
- [`code/fcn.00401847.c`](code/fcn.00401847.c)
- [`code/fcn.00401889.c`](code/fcn.00401889.c)
- [`code/fcn.004018eb.c`](code/fcn.004018eb.c)
- [`code/fcn.004018f3.c`](code/fcn.004018f3.c)
- [`code/fcn.00401950.c`](code/fcn.00401950.c)
- [`code/fcn.004019c4.c`](code/fcn.004019c4.c)
- [`code/fcn.00401b98.c`](code/fcn.00401b98.c)
- [`code/fcn.00401c40.c`](code/fcn.00401c40.c)
- [`code/main.c`](code/main.c)
- [`code/sub.api_ms_win_crt_runtime_l1_1_0.dll__set_app_type.c`](code/sub.api_ms_win_crt_runtime_l1_1_0.dll__set_app_type.c)

## Behavioral Analysis

Based on the analysis of the provided disassembly and strings, here is a summary of the findings:

### Core Functionality
The binary appears to be a **bridge or host application** for a library/plugin named `dsp_bridge`. The main logic resides in `dsp_bridge.dll`, which suggests this specific executable acts as a wrapper or host process to execute functions related to Digital Signal Processing (DSP). 

### Suspicious or Malicious Behaviors
While the code does not show direct "malware" actions such as active file encryption or network communication, it contains several techniques common in both high-end commercial software (e.g., games with anti-cheat) and sophisticated malware:

*   **Anti-Analysis / Anti-Debugging:** 
    *   **Exception Handling Manipulation:** The function `fcn.004016f6` interacts heavily with `SetUnhandledExceptionFilter`. While standard for stability, it is a common technique to intercept exceptions that a debugger would normally catch, potentially hiding the program's true behavior from an analyst.
    *   **Environment Check:** The inclusion of `IsDebuggerPresent` and manual checks in the exception handling routines suggest the code is designed to detect if it is being run within a debugger or analysis environment.
*   **Hardware & Instruction Set Profiling:**
    *   The function `fcn.004019c4` performs extensive checks using `IsProcessorFeaturePresent` and a series of bitwise comparisons on values derived from CPUID instructions (e.g., checking for specific feature flags like `0x106c0`, `0x20660`). 
    *   While this is often used to determine if the CPU supports advanced instructions (like AVX), it is also a common method used by malware to detect virtual machines or emulators.

### Notable Techniques & Patterns
*   **Complex Hardware Probing:** The logic in `fcn.004019c4` is quite granular. It doesn't just check for one feature but builds an internal map of capabilities (reflected in the modifications to memory addresses like `0x403378`). 
*   **C Runtime (CRT) Wrappers:** The code heavily utilizes standard C runtime libraries (`api_ms_win_crt_runtime_l1_1_0.dll`), indicating it is a compiled high-level language application rather than raw, hand-crafted assembly malware.
*   **Certificate Context:** The certificates in the metadata belong to **DigiCert** and mention "Guangzhou Kugou Technology Co., Ltd." This indicates the code was likely signed by a legitimate entity, which may suggest it is part of a commercial suite (like media software) that employs heavy protection to prevent tampering or reverse engineering.

### Summary for Report
*   **Purpose:** Host application/bridge for DSP processing functions.
*   **Threat Level:** Low-Medium (Technical indicators of anti-analysis are present, but no active malicious payloads were found in this snippet).
*   **Key Indicators:** 
    *   Extensive CPUID feature mapping.
    *   Custom exception handling to potentially bypass debuggers.
    *   Reference to "dsp_bridge" infrastructure.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Debugger Detection | The binary utilizes `IsDebuggerPresent` and manipulates `SetUnhandledExceptionFilter` to identify and potentially evade analysis by a debugger. |
| T1497 | Virtualized Environment Detection | The granular check of CPUID features via `IsProcessorFeaturePresent` is used to determine if the application is running within a virtual machine or emulator. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Several entries in the raw string data (such as DigiCert URLs) have been excluded as they belong to standard Certificate Authority infrastructure and are considered false positives for malicious activity.*

### **IP addresses / URLs / Domains**
*   None identified (all discovered URLs were verified as standard certificate authority infrastructure).

### **File paths / Registry keys**
*   `D:\buildbot\build1\dsp_bridge\build\bin\Release\bridge_plugin_host.pdb` (Note: This is a debug path, but it identifies the specific build environment and naming convention of the application.)
*   `dsp_bridge.dll` (Primary library/component identifier)

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Module Name:** `dsp_bridge` (Identified as the core functionality and internal naming convention for the bridge components).
*   **Organization Identity:** `Guangzhou Kugou Technology Co., Ltd.` (Associated with the signing certificate; useful for attribution to specific commercial software suites).
*   **Anti-Analysis Behavior:** 
    *   `SetUnhandledExceptionFilter`: Used as a mechanism for anti-debugging/exception handling.
    *   **CPU ID Mapping**: Specific routine (`fcn.004019c4`) used for intensive hardware feature checks (commonly associated with VM detection or anti-analysis).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://cacerts.digicert.com/DigiCertAssuredIDRootCA.crt0E`
- `http://cacerts.digicert.com/DigiCertTrustedG4CodeSigningRSA4096SHA3842021CA1.crt0`
- `http://cacerts.digicert.com/DigiCertTrustedG4TimeStampingRSA4096SHA2562025CA1.crt0_`
- `http://cacerts.digicert.com/DigiCertTrustedRootG4.crt0C`
- `http://crl3.digicert.com/DigiCertAssuredIDRootCA.crl0`
- `http://crl3.digicert.com/DigiCertTrustedG4CodeSigningRSA4096SHA3842021CA1.crl0S`
- `http://crl3.digicert.com/DigiCertTrustedG4TimeStampingRSA4096SHA2562025CA1.crl0`
- `http://crl3.digicert.com/DigiCertTrustedRootG4.crl0`
- `http://crl4.digicert.com/DigiCertTrustedG4CodeSigningRSA4096SHA3842021CA1.crl0`
- `http://ocsp.digicert.com0`
- `http://ocsp.digicert.com0A`
- `http://ocsp.digicert.com0C`
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`
- `http://www.digicert.com/CPS0`

---

## Malware Family Classification

1. **Malware family**: Non-Malicious / Commercial Software (Not a known malware family)
2. **Malware type**: Host Application (None identified as malicious functionality)
3. **Confidence**: High

4. **Key evidence**:
*   **Lack of Malicious Behavior:** The analysis shows no indicators of command-and-control (C2) communication, data exfiltration, file encryption, or unauthorized system modifications typical of RATs, ransomware, or infostealers.
*   **Corporate Attribution & Validity:** The binary is signed by a known entity ("Guangzhou Kugou Technology Co., Ltd.") and contains specific infrastructure references (`dsp_bridge`), suggesting it is a legitimate piece of multimedia/DSP software rather than an ad-hoc malware sample.
*   **Contextual Protective Measures:** While "anti-analysis" techniques (VM detection, exception handling manipulation) were flagged, these are common in high-end commercial software to protect intellectual property via Digital Rights Management (DRM) or anti-tamper mechanisms rather than solely as a means to hide malware activity.
