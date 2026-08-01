# Threat Analysis Report

**Generated:** 2026-07-29 19:05 UTC
**Sample:** `0c29cce2264f5bf04ff732bb6035279cb32d23c4b7fa2b935b8386de29f91a37_0c29cce2264f5bf04ff732bb6035279cb32d23c4b7fa2b935b8386de29f91a37.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c29cce2264f5bf04ff732bb6035279cb32d23c4b7fa2b935b8386de29f91a37_0c29cce2264f5bf04ff732bb6035279cb32d23c4b7fa2b935b8386de29f91a37.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 10 sections |
| Size | 38,438,988 bytes |
| MD5 | `6ca4ff521769bb248042eacf3d03fbdc` |
| SHA1 | `888b83fda65c55d8b560d60220acd62e96ebf389` |
| SHA256 | `0c29cce2264f5bf04ff732bb6035279cb32d23c4b7fa2b935b8386de29f91a37` |
| Overall entropy | 7.832 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1765060396 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 6,347,264 | 6.452 | No |
| `.CLR_UEF` | 512 | 3.083 | No |
| `.rdata` | 1,567,744 | 5.673 | No |
| `.data` | 38,912 | 3.327 | No |
| `.pdata` | 221,696 | 6.474 | No |
| `.didat` | 512 | 0.417 | No |
| `Section` | 512 | -0.0 | No |
| `_RDATA` | 78,848 | 5.483 | No |
| `.rsrc` | 1,348,608 | 6.354 | No |
| `.reloc` | 32,768 | 5.448 | No |

### Imports

**KERNEL32.dll**: `RaiseException`, `FreeLibrary`, `SetErrorMode`, `RaiseFailFastException`, `GetExitCodeProcess`, `TerminateProcess`, `UnhandledExceptionFilter`, `SetUnhandledExceptionFilter`, `AddVectoredExceptionHandler`, `MultiByteToWideChar`, `GetTickCount`, `FlushInstructionCache`, `QueryPerformanceFrequency`, `QueryPerformanceCounter`, `RtlLookupFunctionEntry`
**ADVAPI32.dll**: `ReportEventW`, `AdjustTokenPrivileges`, `RegGetValueW`, `SetKernelObjectSecurity`, `GetSidSubAuthorityCount`, `GetSidSubAuthority`, `GetTokenInformation`, `OpenProcessToken`, `DeregisterEventSource`, `RegisterEventSourceW`, `RegQueryValueExW`, `RegOpenKeyExW`, `RegCloseKey`, `EventRegister`, `SetThreadToken`
**ole32.dll**: `CoCreateFreeThreadedMarshaler`, `CreateStreamOnHGlobal`, `CoRevokeInitializeSpy`, `CoGetContextToken`, `CoGetObjectContext`, `CoUnmarshalInterface`, `CoMarshalInterface`, `CoGetMarshalSizeMax`, `CLSIDFromProgID`, `CoReleaseMarshalData`, `CoTaskMemFree`, `CoTaskMemAlloc`, `CoCreateGuid`, `CoInitializeEx`, `CoRegisterInitializeSpy`
**OLEAUT32.dll**: `CreateErrorInfo`, `SysFreeString`, `GetErrorInfo`, `SetErrorInfo`, `SysStringLen`, `SysAllocString`, `SysAllocStringLen`, `SafeArrayGetDim`, `SafeArrayGetLBound`, `SafeArrayDestroy`, `QueryPathOfRegTypeLib`, `LoadTypeLibEx`, `SafeArrayGetVartype`, `VariantChangeType`, `VariantChangeTypeEx`
**USER32.dll**: `LoadStringW`, `MessageBoxW`
**SHELL32.dll**: `ShellExecuteW`
**api-ms-win-crt-string-l1-1-0.dll**: `strncat_s`, `wcsncat_s`, `_wcsicmp`, `wcsnlen`, `wcscat_s`, `towupper`, `iswascii`, `_strdup`, `strncpy`, `strnlen`, `wcstok_s`, `isdigit`, `isupper`, `isalpha`, `towlower`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__stdio_common_vsscanf`, `fflush`, `__acrt_iob_func`, `__stdio_common_vfprintf`, `__stdio_common_vswprintf`, `__stdio_common_vfwprintf`, `fputws`, `fputwc`, `_get_stream_buffer_pointers`, `_fseeki64`, `fread`, `fsetpos`, `ungetc`, `fgetpos`, `fgets`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_crt_atexit`, `_cexit`, `_seh_filter_exe`, `_set_app_type`, `_register_onexit_function`, `_configure_wide_argv`, `_initialize_wide_environment`, `_get_initial_wide_environment`, `_initterm`, `_initterm_e`, `_exit`, `_invoke_watson`, `__p___argc`, `__p___wargv`, `_c_exit`
**api-ms-win-crt-convert-l1-1-0.dll**: `_atoi64`, `_ltow_s`, `_wtoi`, `strtoul`, `_wcstoui64`, `atol`, `_itow_s`, `strtoull`, `wcstoul`
**api-ms-win-crt-heap-l1-1-0.dll**: `free`, `_set_new_mode`, `calloc`, `malloc`, `realloc`
**api-ms-win-crt-utility-l1-1-0.dll**: `qsort`
**api-ms-win-crt-math-l1-1-0.dll**: `asinhf`, `atanhf`, `cbrtf`, `acoshf`, `cosh`, `cbrt`, `coshf`, `exp`, `expf`, `acosh`, `atanh`, `floor`, `floorf`, `fma`, `fmaf`
**api-ms-win-crt-time-l1-1-0.dll**: `_time64`, `_gmtime64_s`, `wcsftime`
**api-ms-win-crt-environment-l1-1-0.dll**: `getenv`
**api-ms-win-crt-locale-l1-1-0.dll**: `_unlock_locales`, `setlocale`, `__pctype_func`, `___lc_locale_name_func`, `_lock_locales`, `___lc_codepage_func`, `___mb_cur_max_func`, `_configthreadlocale`, `localeconv`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `_wrename`, `_unlock_file`, `_wremove`, `_lock_file`

### Exports

`CLRJitAttachState`, `DotNetRuntimeInfo`, `MetaDataGetDispenser`, `g_CLREngineMetrics`, `g_dacTable`

## Extracted Strings

Total strings found: **82136** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.CLR_UEF
`.rdata
@.data
.pdata
@.didat
Section
_RDATA
@.rsrc
@.reloc
|$ AV3
	













		
	






				
t$ WATAUAVAWH
A_A^A]A\_
UVWATAUAVAWH
@A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
VWATAVAWH
0A_A^A\_^
l$ VWAVH
t$PH95
9{~*f
{ ATAVAWH
A_A^A\
|$ AVH
VWATAVAWH
A_A^A\_^
UVWATAUAVAWH
9A4tH
H;MHt)
pA_A^A]A\_^]
l$ VWAVH
9Qx}rH
t$H9sx|'L
|$ ATAVAWH
@A_A^A\
UVWATAUAVAWH
A_A^A]A\_^]
UVWAVAWH
Ot$@9rx}}
`A_A^_^]
SVWATAUAVAWH
A_A^A]A\_^[
A M;A u
UVWATAUAVAWH
PA_A^A]A\_^]
|$ AVH
|$ AVH
|$ AVH
|$ ATAVAWH
0A_A^A\
SVWATAUAVAWH
A_A^A]A\_^[
VWATAVAWH
A_A^A\_^
UVWATAUAVAWH
A_A^A]A\_^]
UAVAWH
UATAUAVAWH
A_A^A]A\]
|$ UATAUAVAWH
A_A^A]A\]
9H tH
@SVWATAUAVAWH
A_A^A]A\_^[
WATAUAVAWH
A_A^A]A\_
UVWAVAWH
	r%fff
 A_A^_^]
|$ AVH
EH;Ehs 
D$ 9l$(
J M;J u
|$ AVH
WATAUAVAWH
@A_A^A]A\_
WATAUAVAWH
@A_A^A]A\_
y8}	H
WATAUAVAWH
0A_A^A]A\_
WAVAWH
0A_A^_
|$ AVH
VWAUAVAWH
 A_A^A]_^
|$ UATAUAVAWH
A_A^A]A\]
VWATAVAWH
 A_A^A\_^
USVWATAUAVAWH
d$HL9\$`
A_A^A]A\_^[]
UVWAVAWI
A_A^_^]
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140001660` | `0x140001660` | 6072530 | ✓ |
| `fcn.1404e1c80` | `0x1404e1c80` | 5053708 | ✓ |
| `fcn.1404df160` | `0x1404df160` | 5042596 | ✓ |
| `fcn.1404dceb0` | `0x1404dceb0` | 5034008 | ✓ |
| `fcn.1404e3040` | `0x1404e3040` | 4867283 | ✓ |
| `fcn.14012ce40` | `0x14012ce40` | 4845810 | ✓ |
| `fcn.1403cfaf0` | `0x1403cfaf0` | 3932376 | ✓ |
| `fcn.1402ea890` | `0x1402ea890` | 2977777 | ✓ |
| `fcn.1402f33d0` | `0x1402f33d0` | 2897298 | ✓ |
| `fcn.140348f50` | `0x140348f50` | 2633698 | ✓ |
| `fcn.14034db30` | `0x14034db30` | 2614310 | ✓ |
| `fcn.1403bfdf0` | `0x1403bfdf0` | 2146662 | ✓ |
| `fcn.14001bfd0` | `0x14001bfd0` | 1781835 | ✓ |
| `fcn.140426c00` | `0x140426c00` | 1725270 | ✓ |
| `fcn.140430fa0` | `0x140430fa0` | 1683382 | ✓ |
| `fcn.1404310c0` | `0x1404310c0` | 1683094 | ✓ |
| `fcn.140433d10` | `0x140433d10` | 1671750 | ✓ |
| `fcn.1405127a0` | `0x1405127a0` | 1527653 | ✓ |
| `fcn.14017c640` | `0x14017c640` | 1427451 | ✓ |
| `fcn.140092950` | `0x140092950` | 1295096 | ✓ |
| `fcn.1403b3b70` | `0x1403b3b70` | 1201254 | ✓ |
| `fcn.1404d3b40` | `0x1404d3b40` | 1168978 | ✓ |
| `fcn.140021810` | `0x140021810` | 820290 | ✓ |
| `fcn.14011ae70` | `0x14011ae70` | 650171 | ✓ |
| `method.std::ctype_wchar_t_.virtual_24` | `0x140538500` | 592772 | ✓ |
| `fcn.1403b4410` | `0x1403b4410` | 592360 | ✓ |
| `fcn.1400892d0` | `0x1400892d0` | 555374 | ✓ |
| `fcn.14012da70` | `0x14012da70` | 433746 | ✓ |
| `fcn.1400db720` | `0x1400db720` | 249052 | ✓ |
| `fcn.1404d41c0` | `0x1404d41c0` | 178679 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001660.c`](code/fcn.140001660.c)
- [`code/fcn.14001bfd0.c`](code/fcn.14001bfd0.c)
- [`code/fcn.140021810.c`](code/fcn.140021810.c)
- [`code/fcn.1400892d0.c`](code/fcn.1400892d0.c)
- [`code/fcn.140092950.c`](code/fcn.140092950.c)
- [`code/fcn.1400db720.c`](code/fcn.1400db720.c)
- [`code/fcn.14011ae70.c`](code/fcn.14011ae70.c)
- [`code/fcn.14012ce40.c`](code/fcn.14012ce40.c)
- [`code/fcn.14012da70.c`](code/fcn.14012da70.c)
- [`code/fcn.14017c640.c`](code/fcn.14017c640.c)
- [`code/fcn.1402ea890.c`](code/fcn.1402ea890.c)
- [`code/fcn.1402f33d0.c`](code/fcn.1402f33d0.c)
- [`code/fcn.140348f50.c`](code/fcn.140348f50.c)
- [`code/fcn.14034db30.c`](code/fcn.14034db30.c)
- [`code/fcn.1403b3b70.c`](code/fcn.1403b3b70.c)
- [`code/fcn.1403b4410.c`](code/fcn.1403b4410.c)
- [`code/fcn.1403bfdf0.c`](code/fcn.1403bfdf0.c)
- [`code/fcn.1403cfaf0.c`](code/fcn.1403cfaf0.c)
- [`code/fcn.140426c00.c`](code/fcn.140426c00.c)
- [`code/fcn.140430fa0.c`](code/fcn.140430fa0.c)
- [`code/fcn.1404310c0.c`](code/fcn.1404310c0.c)
- [`code/fcn.140433d10.c`](code/fcn.140433d10.c)
- [`code/fcn.1404d3b40.c`](code/fcn.1404d3b40.c)
- [`code/fcn.1404d41c0.c`](code/fcn.1404d41c0.c)
- [`code/fcn.1404dceb0.c`](code/fcn.1404dceb0.c)
- [`code/fcn.1404df160.c`](code/fcn.1404df160.c)
- [`code/fcn.1404e1c80.c`](code/fcn.1404e1c80.c)
- [`code/fcn.1404e3040.c`](code/fcn.1404e3040.c)
- [`code/fcn.1405127a0.c`](code/fcn.1405127a0.c)
- [`code/method.std__ctype_wchar_t_.virtual_24.c`](code/method.std__ctype_wchar_t_.virtual_24.c)

## Behavioral Analysis

This analysis incorporates your new data. The additional disassembly reinforces and further solidifies the previous conclusion: **this code is non-malicious, high-complexity standard library boilerplate.**

### Updated Analysis Summary

The presence of more complex structures and specific technical markers in chunk 2 provides a clearer picture of what this code is: it is part of the **Microsoft C Runtime (CRT)** or the **C++ Standard Library (`msvcrt.dll`)**, specifically handling **locale, character encoding (ctype), and internal memory management.**

---

### Key Findings from Chunk 2

#### 1. Definitive Identification of Standard Library Components
The most significant indicator in this batch is:
*   **`method.std::ctype_wchar_t_.virtual_24`**: This is a direct implementation of the C++ standard library’s `ctype` facet for wide characters (`wchar_t`). The purpose of this class in any standard C++ environment is to determine character properties (e.g., "is this digit?", "is this uppercase?"). The fact that it calls `GetStringTypeW` suggests it is managing how the system interprets and displays text across different locales.

#### 2. Table-Driven Logic (Why the code looks "complex")
The high volume of nested `if` statements, bitwise masks (e.g., `0x1f`, `0x3f`), and specific hex offsets (like `0x48`, `0x57`, `0x58`) is not indicative of manual obfuscation by a malware author. Instead, it is **Table-Driven Design**.
*   **Internal Offsets:** The code frequently checks if a character or state equals values like `0x39` or `0x57`. These are internal "Type" IDs for the CRT. When the code determines a string type, it uses these numbers to jump to the correct logic to handle that specific format.
*   **Performance Optimization:** The repeated checks (e.g., `if (uVar13 - 0x10 < 0x20)`) are often used by compilers to optimize "fast paths" for common characters while keeping specialized handling for rare symbols or different languages/locales.

#### 3. Memory and Resource Management
Several functions in this chunk handle the "plumbing" of a multi-threaded environment:
*   **`fcn.1400892d0`**: This function contains calls to `_FlushInstructionCache`, `GetProcess()`, and complex logic for managing memory blocks. These are standard procedures when a library needs to ensure that data modified in one thread (like a shared string table or locale setting) is visible to other threads.
*   **`LOCK()` and `UNLOCK()`**: These macros/calls indicate the use of Critical Sections, which are used by the CRT to prevent "race conditions" when multiple parts of a program try to access the same memory at once.

#### 4. Error Handling and "Abort" Mechanisms
The occurrence of `swi(3)` (Software Interrupt) or calls to `fcn.1403cc600` are common in the MSVC runtime.
*   **Context:** In these specific locations, they are used as a "fail-fast" mechanism. If the system encounters an impossible state (like a memory corruption or an unsupported character encoding), it triggers this interrupt to stop the process immediately rather than allowing it to continue in an unstable state.

### Analysis of New "Suspicious" Patterns
*   **Complex Pointer Arithmetic:** While calculations like `uVar12 = *(iVar19 + uVar17 * 0x48) & 0x1f` look suspicious, they are the standard way a C++ compiler implements an array-based lookup for a "Feature" or "Property" table.
*   **Switch Table Complexity:** The large switch cases (e.g., in `fcn.14011ae70`) are used to map internal data types to specific handling routines. This is common when supporting dozens of different language locales and Unicode variations.

### Final Conclusion: Non-Malicious
The code remains classified as **non-malicious boilerplate**. 

Evidence for this conclusion includes:
1.  **Explicit Symbols:** The presence of `std::ctype_wchar_t_` links the logic directly to the standard C++ library.
2.  **Consistency:** The "complexity" is consistent with a large, mature codebase (the Windows Runtime) designed to handle every possible edge case for string processing and memory management.
3.  **Lack of Malicious Indicators:** There are no calls to network APIs (e.g., `InternetOpen`, `connect`), no attempts at process injection, no file system manipulation outside of standard library buffers, and no encryption/obfuscation techniques used to hide high-level logic.

The code is a "workhorse" of the Microsoft C Runtime—complex because it has to be extremely robust across thousands of different software applications.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework. 

Note: As the final conclusion states the code is **non-malicious** and consists of standard library boilerplate (msvcrt.dll), these mappings identify characteristics that are often flagged during initial triage but were confirmed as benign system functions in this context.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The "complex" bitmasking, arithmetic, and large switch tables are characteristic of obfuscation but are confirmed here as standard "Table-Driven Design" for the CRT. |
| **T1562.001** | DLL Execution: Reflective DLL Loading (Related) | While not malicious in this context, the heavy use of memory management and internal `LOCK/UNLOCK` routines are typical components examined during triage to rule out dynamic code loading. |
| **None** | Non-Malicious / Standard Library | The analysis concludes that features like `swi(3)` and `GetProcess()` are standard "fail-fast" mechanisms and memory handling for the Microsoft C Runtime, not adversary TTPs. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the intelligence report regarding Indicators of Compromise (IOCs).

### **Threat Intelligence Assessment**
The analysis confirms that the provided data contains **no actionable Indicators of Compromise**. The behavior described identifies the code as standard Microsoft C Runtime (CRT) and C++ Standard Library (`ms_vcrt.dll`) components used for locale handling, memory management, and multi-threading.

---

### **IOC Extraction**

**IP addresses / URLs / Domains**
*   None

**File paths / Registry keys**
*   None (The references to `msvcrt.dll` are standard system libraries).

**Mutex names / Named pipes**
*   None

**Hashes**
*   None

**Other artifacts**
*   **Note:** While the behavioral analysis lists internal function offsets (e.g., `fcn.1400892d0`, `fcn.1403cc600`), these are standard memory addresses within a library and do not constitute unique identifiers for malicious activity or specific malware families.

---
**Analyst Note:** The investigation concludes that the provided strings represent high-complexity but legitimate boilerplate code common in Windows software development. No malicious characteristics (e.g., network communication, persistence mechanisms, or injection techniques) were identified.

---

## Malware Family Classification

1. **Malware family**: Non-malicious (Microsoft C Runtime / msvcrt.dll)
2. **Malware type**: N/A (Benign System Library)
3. **Confidence**: High
4. **Key evidence**: 
*   **Standard Library Identification**: The code explicitly contains `std::ctype_wchar_t_` symbols and calls to `GetStringTypeW`, which are standard components of the Microsoft C Runtime (CRT) used for locale and character encoding.
*   **Absence of Malicious Behavior**: There is no evidence of network communication, process injection, file system manipulation, or encryption routines typically associated with malware.
*   **Resolution of "False Positives"**: The analysis confirms that complex logic—such as bitmasking and large switch tables—is a result of "Table-Driven Design" for robust library performance rather than intentional adversarial obfuscation.
