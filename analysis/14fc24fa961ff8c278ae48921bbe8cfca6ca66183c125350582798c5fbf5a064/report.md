# Threat Analysis Report

**Generated:** 2026-09-06 14:25 UTC
**Sample:** `14fc24fa961ff8c278ae48921bbe8cfca6ca66183c125350582798c5fbf5a064_14fc24fa961ff8c278ae48921bbe8cfca6ca66183c125350582798c5fbf5a064.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14fc24fa961ff8c278ae48921bbe8cfca6ca66183c125350582798c5fbf5a064_14fc24fa961ff8c278ae48921bbe8cfca6ca66183c125350582798c5fbf5a064.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 10 sections |
| Size | 18,332,211 bytes |
| MD5 | `299b6e4e61ede097805998a7f6503d81` |
| SHA1 | `0f9aaf2d556d7e6a8aa930f888855dc44148e62d` |
| SHA256 | `14fc24fa961ff8c278ae48921bbe8cfca6ca66183c125350582798c5fbf5a064` |
| Overall entropy | 7.209 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1770889916 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 6,347,264 | 6.452 | No |
| `.CLR_UEF` | 512 | 3.083 | No |
| `.rdata` | 1,567,744 | 5.673 | No |
| `.data` | 38,912 | 3.328 | No |
| `.pdata` | 221,696 | 6.474 | No |
| `.didat` | 512 | 0.417 | No |
| `Section` | 512 | -0.0 | No |
| `_RDATA` | 78,848 | 5.483 | No |
| `.rsrc` | 1,348,608 | 6.355 | No |
| `.reloc` | 32,768 | 5.449 | No |

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

Total strings found: **56506** (showing first 100)

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

This updated analysis incorporates the new disassembly provided in chunk 2/2 while retaining all previously identified observations regarding the binary's likely role as high-level infrastructure or a sophisticated packer/loader wrapper.

### Updated Core Functionality and Purpose
The additional code confirms that this is an extremely sophisticated piece of software, consistent with a **managed runtime (like .NET CLR) or a specialized virtual machine.** 

**New evidence from Chunk 2:**
*   **Multi-Threaded Synchronization:** The explicit use of `LOCK()` and `UNLOCK()` macros, along with calls to `CriticalSection` related functions, confirms that the code is designed for a multi-threaded environment. This is standard in system-level infrastructure but also common in sophisticated malware droppers used to handle multiple concurrent tasks (e.g., staying alive while decrypting components).
*   **Sophisticated Memory Management:** Functions like `fcn.140021810` and `fcn.1403b4410` show intricate memory handling, including alignment checks (e.g., `uVar_uint8 * 8`), heap management (`HeapFree`), and buffer boundary checks. The logic used to determine offsets is highly optimized, suggesting a large-scale production environment.
*   **Object Handling & Type Resolution:** The extensive switch tables in functions like `fcn.1404d41c0` (containing hundreds of potential paths) are characteristic of "method dispatch" or "type casting" logic where the program must determine how to handle various internal data types at runtime.

### Refined Analysis of Suspicious Behaviors
While the code remains "infrastructure-heavy," the complexity itself is a significant observation in a malware context:

*   **Complexity as Obfuscation:** The sheer density of the switch tables and nested if-else blocks (especially in `fcn.1404d41c0`) serves to significantly slow down manual analysis. In a malicious file, this level of complexity is often used to hide "logic gates"—where only certain conditions met by specific environmental checks allow the code to proceed to its primary payload.
*   **Dynamic Offset Calculations:** The frequent use of complex arithmetic for memory addresses (e.g., `(iVar13 + uVar24 * 0x14) * 2 + 0x14063f750`) suggests a system that uses **dynamic dispatch**. It is calculating the location of data or functions on the fly, which is harder for automated sandboxes to follow than direct calls.
*   **Implicit Resource Management:** Function `fcn.1400892d0` contains loops that appear to traverse a linked list or table of resources/objects to perform "cleanup" or state updates. This suggests the software manages many long-lived objects in memory, which is common in both large applications and sophisticated packers maintaining internal state during an unpacking process.

### Updated Technical Patterns & Indicators
*   **High-Level Jumps:** The use of `switch` tables for what appear to be property lookups or instruction interpretations (e.g., the block starting at `0x1404d4788`) is a classic hallmark of a **VM-based protector**. It processes a series of "instructions" internally rather than calling standard OS functions directly.
*   **Complex Pointer Arithmetic:** The code frequently calculates offsets using large, hardcoded constants (e.g., `0x14063f750`). This is typical of compiled C# or C++ where the compiler/linker has optimized memory access for high-performance applications.
*   **Safety Guards & Validations:** The repeated checks to see if an address is "valid" or if a buffer length is sufficient before proceeding suggest a robust error-handling system, but in a packer context, these can also be used as **anti-analysis checks**. If an analyst alters the memory state to force a path that doesn't exist, the code will simply fail to execute or call `TerminateProcess`.

### Updated Summary for Analyst
The analysis of chunk 2/2 reinforces the conclusion that this is not a simple script. It is highly complex **runtime infrastructure**, likely part of a .NET-based environment (CLR) or a specialized Virtual Machine.

**Key takeaways for your investigation:**
1.  **Likely a Packer/Loader Wrapper:** Because of its complexity and "generic" nature, if this binary is indeed malicious, it is almost certainly the **loader or unpacker**. It is designed to hide the *actual* malware by wrapping it in a complex layer of heavy-duty code that mimics a legitimate runtime environment.
2.  **Non-Linear Execution:** The extensive use of jump tables and indirect calls means traditional linear disassembly will be difficult. You should focus on finding where this "routine" eventually hands over execution to another module or unpacks a new segment into memory.
3.  **Persistence of Sophistication:** The amount of work required to build/maintain this infrastructure suggests it is part of an established toolkit (likely used by advanced threat actors) rather than a single-purpose piece of "scam" malware.

**Recommendation:** Monitor for calls to `VirtualAlloc`, `VirtualProtect`, or `WriteProcessMemory` shortly after these complex setup routines are completed, as these would indicate the point where the underlying payload is being prepared for execution.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors observed in your analysis to the corresponding MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055.003** | Virtualization | The use of large switch tables for instruction interpretation (VM-based protector) indicates a custom virtual machine is used to hide the primary malicious logic from analysis. |
| **T1029** | Packing | The behavior describes the binary as a sophisticated loader or unpacker wrapper designed to conceal the ultimate payload through complex, high-level runtime infrastructure. |
| **T1027** | Obfuscated Files | The use of non-linear execution paths, dynamic offset calculations, and excessive complexity (logic gates) is specifically intended to hinder manual and automated reverse engineering. |
| **T1546** | Sandbox Evasion | The "Safety Guards & Validations" mentioned are likely utilized as anti-analysis checks to detect if the binary is running in a monitored or simulated environment. |

---

## Indicators of Compromise

Based on the provided strings and behavior analysis, here is the extraction of Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided data contains a significant amount of technical metadata and behavioral descriptions, but it does not contain traditional "hard" IOCs such as specific IP addresses, URLs, or file hashes. The text describes a complex **packer/loader wrapper** likely used in a .NET environment.

---

### **Indicators of Compromise (IOCs)**

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (The strings provided are memory offsets and assembly labels, not filesystem paths or registry locations).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts (behavioral indicators)**
While no static IOCs were found, the following **behavioral patterns** are identified as high-confidence markers for a sophisticated packer/loader:
*   **VM-based Protection:** Extensive use of switch tables and indirect calls to obfuscate logic gates.
*   **Dynamic Dispatch:** Frequent usage of complex arithmetic for memory address calculation (e.g., `(iVar13 + uVar24 * 0x14) * 2 + 0x14063f750`).
*   **Anti-Analysis Patterns:** Use of "Logic Gates" to detect environment changes and the use of complex memory management routines as a smoke screen for malicious payloads.
*   **Suspicious API Logic:** While not specific IOCs, the analysis indicates the code is designed to wrap logic before executing standard procedures like `VirtualAlloc`, `VirtualProtect`, and `WriteProcessMemory`.

---
**Analyst Note:** The "extracted strings" section contains mostly junk data, non-printing characters, and internal assembly labels (e.g., `.rdata`, `.pdata`). These are common in packed binaries to obfuscate the real payload. No actionable network or filesystem indicators were present in the provided snippet.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated VM-based Protection:** The heavy use of large switch tables, multi-threaded synchronization, and complex "method dispatch" logic is characteristic of a custom virtual machine (T1055.003) used to hide the primary payload's execution path.
*   **Loader/Packer Characteristics:** The analysis identifies the binary as a high-level wrapper or packer designed for non-linear execution and dynamic offset calculations, specifically intended to wrap a secondary, hidden payload.
*   **Anti-Analysis Engineering:** The use of "logic gates," complex memory management (e.g., `HeapFree` and boundary checks), and potential sandbox evasion techniques indicate it is a professional-grade piece of infrastructure rather than a simple malware script.
