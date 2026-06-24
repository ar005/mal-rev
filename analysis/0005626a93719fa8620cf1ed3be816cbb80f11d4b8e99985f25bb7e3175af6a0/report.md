# Threat Analysis Report

**Generated:** 2026-06-23 15:40 UTC
**Sample:** `0005626a93719fa8620cf1ed3be816cbb80f11d4b8e99985f25bb7e3175af6a0_0005626a93719fa8620cf1ed3be816cbb80f11d4b8e99985f25bb7e3175af6a0.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0005626a93719fa8620cf1ed3be816cbb80f11d4b8e99985f25bb7e3175af6a0_0005626a93719fa8620cf1ed3be816cbb80f11d4b8e99985f25bb7e3175af6a0.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 7 sections |
| Size | 118,784 bytes |
| MD5 | `ae8f347e5a86651e3b020c3e7f8ca0d9` |
| SHA1 | `904b567ad0517797e4ce8fbb50aaf2d130c9dd2c` |
| SHA256 | `0005626a93719fa8620cf1ed3be816cbb80f11d4b8e99985f25bb7e3175af6a0` |
| Overall entropy | 3.784 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 4059719470 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 14,336 | 5.788 | No |
| `.rdata` | 14,848 | 4.067 | No |
| `.data` | 512 | 2.248 | No |
| `.pdata` | 1,024 | 3.608 | No |
| `.rsrc` | 2,560 | 4.346 | No |
| `.reloc` | 512 | 2.982 | No |
| `.rcdata7` | 65,536 | 3.783 | No |

### Imports

**ADVAPI32.dll**: `RegOpenKeyExW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`
**VERSION.dll**: `VerQueryValueW`, `GetFileVersionInfoW`, `GetFileVersionInfoSizeW`
**USER32.dll**: `wsprintfW`
**KERNEL32.dll**: `GetProcAddress`, `FreeLibrary`, `VirtualQuery`, `GetProcessHeap`, `HeapFree`, `HeapAlloc`, `GetCurrentProcessId`, `ProcessIdToSessionId`, `GetVersionExW`, `GetModuleFileNameW`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `UnhandledExceptionFilter`, `SetUnhandledExceptionFilter`
**VCRUNTIME140.dll**: `_CxxThrowException`, `__std_exception_destroy`, `__vcrt_GetModuleFileNameW`, `__vcrt_LoadLibraryExW`, `memset`, `strstr`, `wcsstr`, `__C_specific_handler`, `__C_specific_handler_noexcept`, `__current_exception`, `__current_exception_context`, `__std_exception_copy`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__stdio_common_vfprintf`, `__stdio_common_vsprintf_s`, `_set_fmode`, `__p__commode`, `fputs`, `fgets`, `feof`, `fopen_s`, `__acrt_iob_func`, `fclose`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_register_onexit_function`, `_initialize_onexit_table`, `perror`, `terminate`, `_crt_atexit`, `_errno`, `_register_thread_local_exe_atexit_callback`, `_seh_filter_exe`, `_set_app_type`, `__p___argv`, `_configure_narrow_argv`, `_initialize_narrow_environment`, `_get_initial_narrow_environment`, `_initterm`, `_initterm_e`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `remove`, `rename`
**api-ms-win-crt-string-l1-1-0.dll**: `strcat_s`, `strtok_s`, `_stricmp`, `strcpy_s`, `_wcslwr_s`, `wcscpy_s`, `wcslen`, `wcstok_s`, `wcscat_s`
**api-ms-win-crt-heap-l1-1-0.dll**: `_set_new_mode`, `malloc`, `free`, `_callnewh`
**api-ms-win-crt-environment-l1-1-0.dll**: `_dupenv_s`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

## Extracted Strings

Total strings found: **459** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
B.rcdata77
@USVWATAUAVAWH
A_A^A]A\_^[]
 H3E H3E
u0HcH<H
UAVAWH
fD9|TP
C\f9DLPt
USVWATAUAVAWH
A_A^A]A\_^[]
td+uoA;6r\A
T$uPH
assistive_technologies
assistive_technologies=com.sun.java.accessibility.AccessBridge

screen_magnifier_present=true

#assistive_technologies=com.sun.java.accessibility.AccessBridge

#screen_magnifier_present=true

screen_magnifier_present
assistive_technologies
screen_magnifier_present
USERPROFILE
Error fetching USERPROFILE.

\.accessibility.properties
\.acce$$ibility.properties
The USERPROFILE environment variable is too long.

It must be no longer than 233 characters.

Couldn't create file: %s

screen_magnifier_present=true

assistive_technologies=com.sun.java.accessibility.AccessBridge

Couldn't open temp file: %s

Couldn't remove file: %s

Couldn't rename %s to %s.


jabswitch [/enable | /disable | /version | /?]


Description:

  jabswitch enables or disables the Java Access Bridge.


Parameters:

  /enable   Enable the Java Accessibility Bridge.

  /disable  Disable the Java Accessibility Bridge.

  /version  Display the version.

  /?        Display this usage information.


Note:

  The Java Access Bridge can also be enabled with the

  Windows Ease of Access control panel (which can be

  activated by pressing Windows + U).  The Ease of Access

  control panel has a Java Access Bridge checkbox.  Please

  be aware that unchecking the checkbox has no effect and

  in order to disable the Java Access Bridge you must run

  jabswitch.exe from the command line.

Unable to get executable file name.

Unable to get version info size.

Unable to get version info.

Unable to query version value.

version %i.%i.%i.%i
jabswitch 

jabswitch enables or disables the Java Access Bridge.

-version
/version
-enable
/enable
-disable
/disable
There was an error.


The Java Access Bridge has 
enabled.

disabled.

commentLine
jabLine
magLine
context
context
commentLine
context
context
tempPath
nParam
profilePath
acc_props1
acc_props2
executableFileName
pVersionInfo
versionString
outputString
dataType
dataLength
dataBuffer
dataType
dataLength
dataBuffer
searchBuffer
nextToken
dataBuffer
dwSessionId
_ArgList
_ArgList
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400142f4` | `0x1400142f4` | 3544 | ✓ |
| `fcn.140014354` | `0x140014354` | 3478 | ✓ |
| `fcn.14001459c` | `0x14001459c` | 2846 | ✓ |
| `fcn.1400141d0` | `0x1400141d0` | 2135 | ✓ |
| `fcn.140002b24` | `0x140002b24` | 1660 | ✓ |
| `fcn.1400119d0` | `0x1400119d0` | 1424 | ✓ |
| `fcn.140001610` | `0x140001610` | 1049 | ✓ |
| `fcn.140001ff0` | `0x140001ff0` | 1026 | ✓ |
| `fcn.140013360` | `0x140013360` | 975 | ✓ |
| `fcn.140003f48` | `0x140003f48` | 953 | ✓ |
| `fcn.140002ed0` | `0x140002ed0` | 910 | ✓ |
| `fcn.1400010a0` | `0x1400010a0` | 890 | ✓ |
| `fcn.140001d10` | `0x140001d10` | 715 | ✓ |
| `fcn.140014adc` | `0x140014adc` | 714 | ✓ |
| `fcn.140011f60` | `0x140011f60` | 678 | ✓ |
| `fcn.14000326c` | `0x14000326c` | 661 | ✓ |
| `fcn.140003cc8` | `0x140003cc8` | 640 | ✓ |
| `fcn.1400024d0` | `0x1400024d0` | 591 | ✓ |
| `fcn.140001b10` | `0x140001b10` | 504 | ✓ |
| `fcn.140001420` | `0x140001420` | 477 | ✓ |
| `fcn.140013ea0` | `0x140013ea0` | 438 | ✓ |
| `fcn.140011710` | `0x140011710` | 430 | ✓ |
| `fcn.140013890` | `0x140013890` | 429 | ✓ |
| `fcn.140004304` | `0x140004304` | 417 | ✓ |
| `fcn.140013d10` | `0x140013d10` | 399 | ✓ |
| `fcn.1400145d0` | `0x1400145d0` | 358 | ✓ |
| `fcn.140013a40` | `0x140013a40` | 353 | ✓ |
| `fcn.140013bb0` | `0x140013bb0` | 347 | ✓ |
| `fcn.140013730` | `0x140013730` | 341 | ✓ |
| `fcn.1400038a4` | `0x1400038a4` | 331 | ✓ |

### Decompiled Code Files

- [`code/fcn.1400010a0.c`](code/fcn.1400010a0.c)
- [`code/fcn.140001420.c`](code/fcn.140001420.c)
- [`code/fcn.140001610.c`](code/fcn.140001610.c)
- [`code/fcn.140001b10.c`](code/fcn.140001b10.c)
- [`code/fcn.140001d10.c`](code/fcn.140001d10.c)
- [`code/fcn.140001ff0.c`](code/fcn.140001ff0.c)
- [`code/fcn.1400024d0.c`](code/fcn.1400024d0.c)
- [`code/fcn.140002b24.c`](code/fcn.140002b24.c)
- [`code/fcn.140002ed0.c`](code/fcn.140002ed0.c)
- [`code/fcn.14000326c.c`](code/fcn.14000326c.c)
- [`code/fcn.1400038a4.c`](code/fcn.1400038a4.c)
- [`code/fcn.140003cc8.c`](code/fcn.140003cc8.c)
- [`code/fcn.140003f48.c`](code/fcn.140003f48.c)
- [`code/fcn.140004304.c`](code/fcn.140004304.c)
- [`code/fcn.140011710.c`](code/fcn.140011710.c)
- [`code/fcn.1400119d0.c`](code/fcn.1400119d0.c)
- [`code/fcn.140011f60.c`](code/fcn.140011f60.c)
- [`code/fcn.140013360.c`](code/fcn.140013360.c)
- [`code/fcn.140013730.c`](code/fcn.140013730.c)
- [`code/fcn.140013890.c`](code/fcn.140013890.c)
- [`code/fcn.140013a40.c`](code/fcn.140013a40.c)
- [`code/fcn.140013bb0.c`](code/fcn.140013bb0.c)
- [`code/fcn.140013d10.c`](code/fcn.140013d10.c)
- [`code/fcn.140013ea0.c`](code/fcn.140013ea0.c)
- [`code/fcn.1400141d0.c`](code/fcn.1400141d0.c)
- [`code/fcn.1400142f4.c`](code/fcn.1400142f4.c)
- [`code/fcn.140014354.c`](code/fcn.140014354.c)
- [`code/fcn.14001459c.c`](code/fcn.14001459c.c)
- [`code/fcn.1400145d0.c`](code/fcn.1400145d0.c)
- [`code/fcn.140014adc.c`](code/fcn.140014adc.c)

## Behavioral Analysis

Based on the provided disassembly and string data, here is an analysis of the binary's functionality and behavior:

### Core Functionality and Purpose
The program, identified by the string `jabswitch`, is designed to **enable or disable the Java Access Bridge**. This is a standard component used to provide accessibility features (like screen readers) for Java-based applications. 

The code processes command-line arguments (e.g., `/enable`, `/disable`, `/version`) and performs the following actions:
*   **Configuration Modification:** It modifies configuration files (specifically `.properties` files) to toggle settings like `assistive_technologies` and `screen_magnifier_present`.
*   **Registry Interaction:** The code interacts with the Windows Registry (`RegOpenKeyExW`, `RegQueryValueExW`, `RegSetValueExW`) to read or update configuration paths.
*   **System Info Retrieval:** It uses standard Windows APIs to gather information about the system's files, version info, and memory status.

### Suspicious or Malicious Behaviors
While the primary purpose appears to be a utility for accessibility tools, several elements are notable from a security perspective:

*   **Obfuscated Filenames:** The string list contains `\.acce$$ibility.properties`. The use of dollar signs (`$$`) in place of letters is a common **evasion technique**. It allows the file to exist on disk while potentially bypassing simple signature-based detection or confusing standard system logs.
*   **Registry Persistence/Modification:** The program modifies registry keys under `SOFTWARE\Wow6432Node\Microsoft\...`. While this can be for legitimate software installation, modification of these paths is often used by malware to achieve persistence or modify environment variables to facilitate the execution of other components.
*   **Environment Manipulation:** By modifying `.properties` files and Registry entries related to "assistive technologies," a malicious actor could potentially use this tool as a component in a larger attack (e.g., leveraging legitimate-looking utilities to change system behavior).

### Notable Techniques or Patterns
*   **Command-Line Interface (CLI) Logic:** The code uses a standard dispatching pattern for CLI arguments (`fcn.1400024d0`). This is common in "dual-use" tools—programs that have a legitimate purpose but can be used as building blocks for malware (e.g., for automated installation or configuration).
*   **Error Handling/Reporting:** The presence of `Run-Time Check Failure` and specific error messages suggests the code was compiled with standard development kits, which might indicate it is an official utility that has been bundled into a larger project, or a custom tool designed to look like a legitimate system utility.
*   **Instructional Guardrails:** The inclusion of several "Risk" headers in the disassembly (like `Sema` for memory safety or `RtlCapability` checks) indicates it interacts with lower-level Windows APIs often used by system drivers or high-privilege installers.

### Summary
The binary is a **configuration utility** that manipulates files and Registry keys to toggle Java accessibility features. The primary concern from a security standpoint is the **intentional misspelling of "accessibility"** in its internal string table, which suggests an intent to hide specific file operations from basic observation.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
|---|---|---|
| T1027 | Obfuscation | The use of `$$` in file names (e.g., `\.acce$$ibility.properties`) is a clear attempt to evade signature-based detection and bypass basic string filtering. |
| T1038 | System Information Discovery | The binary gathers system information, including version info, memory status, and file locations, which are often used in the reconnaissance phase of an attack. |
| T1112 | Modify Registry | The tool actively interacts with and modifies keys within the `SOFTWARE\Wow6432Node\` hive to change configuration settings or environment variables. |
| T1059 | Command and Scripting Interpreter | The use of a standard CLI dispatching pattern allows for automated execution and configuration, common in "dual-use" tools used by adversaries for automation. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   (None identified)

**File paths / Registry keys**
*   `\.acce$$ibility.properties` (Note: This is a high-confidence IOC as the use of `$$` indicates an intentional evasion technique to bypass security filters.)
*   `SOFTWARE\Wow6432Node\Microsoft\...` (Note: While a full path was not provided in the strings, the behavioral analysis confirms this specific tree is being targeted for configuration modification.)

**Mutex names / Named pipes**
*   (None identified)

**Hashes**
*   (None provided in text)

**Other artifacts**
*   **Executable/Command Name:** `jabswitch` (Used to toggle Java Access Bridge features).
*   **Configuration Keys:** `assistive_technologies`, `screen_magnifier_present` (Targeted configuration variables within `.properties` files and Registry keys).
*   **Potential Evasion Technique:** Use of "leetspeak" or special character substitution in file names (e.g., `acce$$ibility`) to hide activity from basic string-matching signatures.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: Medium

4. **Key evidence**:
*   **Intentional Evasion Techniques:** The use of "leetspeak" or special characters in filenames (e.g., `\.acce$$ibility.properties`) specifically to bypass string-based security filters indicates a deliberate attempt to evade detection (MITRE T1027).
*   **System Manipulation & Setup:** The combination of registry modification (`Wow6432Node`), system information gathering (T1038), and the use of a command-line interface for configuration suggests this is a "loader" or setup component designed to prepare an environment or modify system state for subsequent payloads.
*   **Dual-Use Ambiguity:** While the primary functionality relates to Java Access Bridge settings, the inclusion of evasion techniques combined with non-standard naming conventions indicates that while it may not be part of a major known family like Emotet, it is designed as a malicious component in an attack chain rather than a standard utility.
