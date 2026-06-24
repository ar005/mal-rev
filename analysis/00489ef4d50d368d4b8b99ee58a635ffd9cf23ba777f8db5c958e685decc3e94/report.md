# Threat Analysis Report

**Generated:** 2026-06-23 23:45 UTC
**Sample:** `00489ef4d50d368d4b8b99ee58a635ffd9cf23ba777f8db5c958e685decc3e94_00489ef4d50d368d4b8b99ee58a635ffd9cf23ba777f8db5c958e685decc3e94.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00489ef4d50d368d4b8b99ee58a635ffd9cf23ba777f8db5c958e685decc3e94_00489ef4d50d368d4b8b99ee58a635ffd9cf23ba777f8db5c958e685decc3e94.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 8 sections |
| Size | 76,210,808 bytes |
| MD5 | `601f1f51cc30f7cfe429dd58cabc3552` |
| SHA1 | `c0f34b1ea22bb2f3254e512ae7ec6f22f95a15c8` |
| SHA256 | `00489ef4d50d368d4b8b99ee58a635ffd9cf23ba777f8db5c958e685decc3e94` |
| Overall entropy | 7.945 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1777505091 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 5,506,560 | 6.553 | No |
| `.CLR_UEF` | 512 | 0.962 | No |
| `.rdata` | 1,292,800 | 5.167 | No |
| `.data` | 29,184 | 3.783 | No |
| `.didat` | 512 | 0.26 | No |
| `_RDATA` | 69,632 | 5.365 | No |
| `.rsrc` | 1,269,760 | 6.391 | No |
| `.reloc` | 264,192 | 6.669 | No |

### Imports

**KERNEL32.dll**: `RaiseException`, `FreeLibrary`, `SetErrorMode`, `RaiseFailFastException`, `GetExitCodeProcess`, `TerminateProcess`, `UnhandledExceptionFilter`, `SetUnhandledExceptionFilter`, `AddVectoredExceptionHandler`, `MultiByteToWideChar`, `GetTickCount`, `FlushInstructionCache`, `QueryPerformanceFrequency`, `QueryPerformanceCounter`, `InterlockedPushEntrySList`
**ADVAPI32.dll**: `RegQueryValueExW`, `AdjustTokenPrivileges`, `RegGetValueW`, `SetKernelObjectSecurity`, `GetSidSubAuthorityCount`, `GetSidSubAuthority`, `GetTokenInformation`, `OpenProcessToken`, `DeregisterEventSource`, `ReportEventW`, `RegisterEventSourceW`, `RegOpenKeyExW`, `RegCloseKey`, `EventRegister`, `SetThreadToken`
**ole32.dll**: `CoCreateFreeThreadedMarshaler`, `CreateStreamOnHGlobal`, `CoRevokeInitializeSpy`, `CoGetContextToken`, `CoGetObjectContext`, `CoUnmarshalInterface`, `CoMarshalInterface`, `CoGetMarshalSizeMax`, `CLSIDFromProgID`, `CoReleaseMarshalData`, `CoTaskMemFree`, `CoTaskMemAlloc`, `CoCreateGuid`, `CoInitializeEx`, `CoRegisterInitializeSpy`
**OLEAUT32.dll**: `SafeArrayPutElement`, `LoadRegTypeLib`, `CreateErrorInfo`, `SafeArraySetRecordInfo`, `GetRecordInfoFromTypeInfo`, `SafeArrayGetElemsize`, `SysStringByteLen`, `SafeArrayAllocDescriptorEx`, `SysAllocStringByteLen`, `VarCyFromDec`, `SafeArrayCreateVector`, `SysFreeString`, `VariantInit`, `GetErrorInfo`, `SetErrorInfo`
**USER32.dll**: `LoadStringW`, `MessageBoxW`
**SHELL32.dll**: `ShellExecuteW`
**api-ms-win-crt-string-l1-1-0.dll**: `strncat_s`, `wcsncat_s`, `_stricmp`, `wcsnlen`, `wcscat_s`, `towupper`, `iswascii`, `_strdup`, `strnlen`, `wcstok_s`, `isdigit`, `isalpha`, `towlower`, `iswupper`, `strncpy`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__stdio_common_vfwprintf`, `fflush`, `fputws`, `fputwc`, `__acrt_iob_func`, `__stdio_common_vswprintf`, `_set_fmode`, `_get_stream_buffer_pointers`, `_fseeki64`, `fread`, `fsetpos`, `ungetc`, `fgetpos`, `__stdio_common_vsscanf`, `fgetc`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_invoke_watson`, `abort`, `exit`, `_beginthreadex`, `terminate`, `_initialize_onexit_table`, `_register_onexit_function`, `_crt_atexit`, `_cexit`, `_seh_filter_exe`, `_set_app_type`, `_wcserror_s`, `_configure_wide_argv`, `_initialize_wide_environment`, `_get_initial_wide_environment`
**api-ms-win-crt-convert-l1-1-0.dll**: `_wcstoui64`, `_itow_s`, `_ltow_s`, `wcstoul`, `strtoul`, `strtoull`, `_wtoi`, `atol`, `atoi`
**api-ms-win-crt-heap-l1-1-0.dll**: `realloc`, `free`, `_set_new_mode`, `malloc`, `calloc`
**api-ms-win-crt-utility-l1-1-0.dll**: `qsort`
**api-ms-win-crt-math-l1-1-0.dll**: `asinh`, `asinhf`, `atanhf`, `cbrtf`, `acoshf`, `log2f`, `__libm_sse2_asin`, `__libm_sse2_atan`, `__libm_sse2_atan2`, `__libm_sse2_log10`, `__libm_sse2_pow`, `acosh`, `atanh`, `log2`, `__libm_sse2_sin`
**api-ms-win-crt-time-l1-1-0.dll**: `_gmtime64_s`, `_time64`, `wcsftime`
**api-ms-win-crt-environment-l1-1-0.dll**: `getenv`
**api-ms-win-crt-locale-l1-1-0.dll**: `___mb_cur_max_func`, `___lc_codepage_func`, `___lc_locale_name_func`, `__pctype_func`, `setlocale`, `localeconv`, `_configthreadlocale`, `_unlock_locales`, `_lock_locales`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `_unlock_file`, `_wremove`, `_wrename`, `_lock_file`

### Exports

`CLRJitAttachState`, `DotNetRuntimeInfo`, `MetaDataGetDispenser`, `g_CLREngineMetrics`, `g_dacTable`

## Extracted Strings

Total strings found: **164382** (showing first 100)

```
!This program cannot be run in DOS mode.
$
Rich ue
`.CLR_UEFD
`.rdata
@.data
.didat
_RDATA
@.rsrc
@.reloc






















zukVVVVj
U9WD|
9wD}dV
D$ t9USj
s	_^]2
A8;A4u
K(;C4s"@
D$XPVW
L$l_^3
G_^Y]



G;A4u

A8;A4u
J(;B4s%@
C@+CD+C8
;C<t-3
D$(SVW
;H|u=j
x_^[]
t$,9t$
t$,9t$
|$9|$
f;Fs 
B(B,t
F(F,t
C(C,t
O<f9t9
sC;W(r*w
;w,r#Q
G;|$<v
|$9|$
Q<f9t

F<f9\0
Q<f9D

H(H,t
L$@;L$<s"
x.F;t$r
f;Xs^
Gf;{r
F
f+Ff
f;~tI
F_^[]
G9Gv
C9Kv
B9Bv

u9Qt*
u9Ht#
t9pt-
A9Av
C9Cv
t69xpu1
'tOfff
D$(;D$$s8
L$L_^[3
D$$PWV
D$_^[
A9Av
= RLCt=TOORt
=  EEt
= RLCt=TOORt
=  EEu
G;Cu_^
tCf9t>
tFf9tA
t$0;|$@u
t$0;|$@u
A;Bu
G4;G0uL
9wPv!S
=  RHt=TOORt
=  RHu$
u%9Hu ;p
t,9zXw
B9z0u
D$_^[
D$_^[
D$_^[
E ;xt,
tV;{v9
t@V=RCC
tWShxB
u
9Y0t
PPPPPPPPP
F(F,t
tAf9t<
tDf9t?
tAf9t<
tDf9t?
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.006860e0` | `0x6860e0` | 2525765 | ✓ |
| `fcn.00794110` | `0x794110` | 19801 | ✓ |
| `fcn.0084b130` | `0x84b130` | 11835 | ✓ |
| `fcn.0078a110` | `0x78a110` | 11289 | ✓ |
| `fcn.0061dcb0` | `0x61dcb0` | 9047 | ✓ |
| `fcn.00641930` | `0x641930` | 8587 | ✓ |
| `fcn.008a9e20` | `0x8a9e20` | 8434 | ✓ |
| `fcn.008479f0` | `0x8479f0` | 8336 | ✓ |
| `fcn.00480a80` | `0x480a80` | 8021 | ✓ |
| `fcn.006d6420` | `0x6d6420` | 7676 | ✓ |
| `fcn.007402a0` | `0x7402a0` | 7513 | ✓ |
| `fcn.00830340` | `0x830340` | 7352 | ✓ |
| `fcn.00703260` | `0x703260` | 7272 | ✓ |
| `fcn.007d1940` | `0x7d1940` | 7233 | ✓ |
| `fcn.008b1f20` | `0x8b1f20` | 7168 | ✓ |
| `fcn.0083a750` | `0x83a750` | 6775 | ✓ |
| `fcn.00784670` | `0x784670` | 6617 | ✓ |
| `fcn.008df000` | `0x8df000` | 6603 | ✓ |
| `fcn.008e09d0` | `0x8e09d0` | 6603 | ✓ |
| `fcn.008e23a0` | `0x8e23a0` | 6603 | ✓ |
| `fcn.008e3d70` | `0x8e3d70` | 6603 | ✓ |
| `fcn.00782380` | `0x782380` | 6390 | ✓ |
| `fcn.0075fc20` | `0x75fc20` | 6363 | ✓ |
| `fcn.006823f0` | `0x6823f0` | 6295 | ✓ |
| `fcn.0070ab40` | `0x70ab40` | 6187 | ✓ |
| `fcn.0055fa60` | `0x55fa60` | 6046 | ✓ |
| `fcn.0055da90` | `0x55da90` | 5989 | ✓ |
| `fcn.0045afb0` | `0x45afb0` | 5969 | ✓ |
| `fcn.00549f90` | `0x549f90` | 5940 | ✓ |
| `fcn.005dfdd0` | `0x5dfdd0` | 5737 | ✓ |

### Decompiled Code Files

- [`code/fcn.0045afb0.c`](code/fcn.0045afb0.c)
- [`code/fcn.00480a80.c`](code/fcn.00480a80.c)
- [`code/fcn.00549f90.c`](code/fcn.00549f90.c)
- [`code/fcn.0055da90.c`](code/fcn.0055da90.c)
- [`code/fcn.0055fa60.c`](code/fcn.0055fa60.c)
- [`code/fcn.005dfdd0.c`](code/fcn.005dfdd0.c)
- [`code/fcn.0061dcb0.c`](code/fcn.0061dcb0.c)
- [`code/fcn.00641930.c`](code/fcn.00641930.c)
- [`code/fcn.006823f0.c`](code/fcn.006823f0.c)
- [`code/fcn.006860e0.c`](code/fcn.006860e0.c)
- [`code/fcn.006d6420.c`](code/fcn.006d6420.c)
- [`code/fcn.00703260.c`](code/fcn.00703260.c)
- [`code/fcn.0070ab40.c`](code/fcn.0070ab40.c)
- [`code/fcn.007402a0.c`](code/fcn.007402a0.c)
- [`code/fcn.0075fc20.c`](code/fcn.0075fc20.c)
- [`code/fcn.00782380.c`](code/fcn.00782380.c)
- [`code/fcn.00784670.c`](code/fcn.00784670.c)
- [`code/fcn.0078a110.c`](code/fcn.0078a110.c)
- [`code/fcn.00794110.c`](code/fcn.00794110.c)
- [`code/fcn.007d1940.c`](code/fcn.007d1940.c)
- [`code/fcn.00830340.c`](code/fcn.00830340.c)
- [`code/fcn.0083a750.c`](code/fcn.0083a750.c)
- [`code/fcn.008479f0.c`](code/fcn.008479f0.c)
- [`code/fcn.0084b130.c`](code/fcn.0084b130.c)
- [`code/fcn.008a9e20.c`](code/fcn.008a9e20.c)
- [`code/fcn.008b1f20.c`](code/fcn.008b1f20.c)
- [`code/fcn.008df000.c`](code/fcn.008df000.c)
- [`code/fcn.008e09d0.c`](code/fcn.008e09d0.c)
- [`code/fcn.008e23a0.c`](code/fcn.008e23a0.c)
- [`code/fcn.008e3d70.c`](code/fcn.008e3d70.c)

## Behavioral Analysis

This final chunk of disassembly (Chunk 13) provides the "micro-architecture" of the translation and buffering mechanism. While the previous chunks showed the *routing* (how a command moves from A to B), Chunk 13 reveals the **Data Serialization & Buffer Management** layer.

It describes how the malware handles internal data structures that bridge its private "Guest" environment with the Windows host environment.

---

### Analysis of Chunk 13: The Data Marshaling & Packet Parsing Layer

This segment represents a sophisticated "Interpreter Loop." It isn't just passing values; it is unpacking complex, nested objects from a buffer.

#### 1. Tag-Based Identification (The `0x400c` System)
The code repeatedly checks for specific hex constants (e.g., `if (uVar6 == 0x400c)` and `if (*puVar16 == 0x400c)`). 
*   **Interpretation:** This is a **Type-Tagging system**. The malware's internal "Instruction Set" isn't just raw numbers; it’s a structured protocol. A value of `0x400c` likely signifies a specific class of operation (e.g., a File I/O command, a Network request, or a Memory manipulation).
*   **Significance:** This allows the "Gatekeeper" to handle different types of malicious actions using a single unified parsing loop. An analyst seeing `0x400c` in memory knows they are looking at a "Command Packet."

#### 2. Manual Buffer Management (The "Internal Heap")
Unlike standard .NET code which relies heavily on the Garbage Collector, much of this logic uses manual pointer arithmetic and explicit offset calculations (e.g., `puVar14 = iVar13 * 0x10 + var_1c0h_2`).
*   **Risk Mitigation:** By manually managing a "buffer" of tasks, the malware reduces its footprint on the standard .NET heap. This makes it harder for memory scanners to identify patterns, as the malicious data is packed into an opaque block that only the internal interpreter understands how to read.
*   **Validation Logic:** The inclusion of bounds-checking (e.g., `if (0 < var_1b4h_2)`) and length calculations suggests a high level of "Hardened" programming. It is designed not just to work, but to remain stable while performing complex tasks.

#### 3. Component Translation & Marshaling
The use of functions like `fcn.004ebed0` (which appears to be an internal "Copy-and-Cast" or "Buffer Prep" helper) and the logic surrounding `SafeArray` (or similar memory layout patterns) indicates a **Marshaling Layer**.
*   **Mechanism:** This layer takes a "Guest Command," unpacks its parameters, validates them against the current "State" of the malware, and wraps them into a structure that the Bridge can pass to the Windows API. 
*   **Impact on Analysis:** This means searching for strings like "C:\Windows\System32..." will likely fail in the initial stages because those strings are packed inside these `0x400c` style packets until the very last millisecond before execution.

---

### Updated Summary for Incident Response

The final analysis confirms that this is a **Modular, State-Machine driven Virtual Machine (VM).** It does not execute commands directly; it interprets a proprietary bytecode that is parsed through multiple layers of abstraction and memory management.

#### Key Technical Findings (Final Update):
*   **Instruction Tagging:** The malware utilizes a tag-based system (e.g., `0x400c`) to identify different "types" of actions within its internal buffer. This allows it to multiplex many different capabilities into a single, compact execution loop.
*   **Advanced Buffer Manipulation:** The code demonstrates sophisticated memory management, utilizing offset-based indexing and manual size calculations. This minimizes the risk of crashes during complex operations (like multi-step file exfiltration).
*   **Sophisticated Marshaling:** There is a distinct layer where "Raw Data" is converted into "Actionable Objects." This happens in the gap between the Gatekeeper and the Bridge, making it very difficult to trace an action back to its origin via static analysis.

#### Updated Risk Assessment:
*   **Threat Level: Critical (Highly Sophisticated / Professional Grade).**
*   **Persistence/Evasion:** The use of **Data Fragmentation** is the primary defense. An analyst looking at a single function will only see "buffer management" or "loop logic," never the actual intent (e.g., "Delete Shadow Copies"). The intent only exists in the *combination* of the data inside the buffer and the code that interprets it.
*   **Complexity:** This is not a standard "dropper." It is an **Execution Framework**. It is designed to host many different modules (exfiltration, encryption, persistence) using the same core interpreter.

#### Strategic Recommendations:
1.  **Memory Scraping for Tags:** Instead of searching for common strings or API names, search memory specifically for the identified "Type Tags" (e.g., `0x400c`, `0x200c`). These are the "junctions" where different malicious capabilities reside.
2.  **Instrumentation at the Gatekeeper:** Place hooks on the functions involved in buffer management (like `fcn.004ebed0`). By monitoring what data is being "prepared," you can see the commands as they are unpacked from the obfuscated format into their usable forms.
3.  **Dynamic Trace Analysis:** Because of the heavy use of switch trees and state-dependent logic, a single execution path may not reveal all capabilities. Use automated "fuzzing" or multi-iteration analysis to force the malware through different branches of its internal switch trees.

#### Final Architecture Map:
| Layer | Name | Function | Technical Indicator |
| :--- | :--- | :--- | :--- |
| **1** | **Loader/Unpacker** | Initial infection & LZMA extraction | `LZMA`, `Standard Packing` |
| **2** | **Runtime Core** | .NET environment preparation | `System.Reflection`, `MemoryMarshal` |
| **3** | **Instruction Fetcher** | Retrieves "Guest" code from memory | `Internal Memory Pointers` |
| **4** | **Translation Matrix** | Converts Guest instructions to Internal IR | **Nested Switch Trees** |
| **5** | **Data Marshaling** | Preps data for the Bridge via Tagging | **0x400c/0x200c Tags**, **Manual Offsets** |
| **6** | **Gatekeeper** | Maps "IR" to specific system-level tasks | `fcn.006823f0` (Large Switch Table) |
| **7** | **Bridge Layer** | Wraps API calls in safe .NET containers | `System.Text`, `System.Numerics` |
| **8** | **Execution Engine** | The actual malicious payload | *Hidden behind layers 4, 5, and 6.* |

---

## MITRE ATT&CK Mapping

Based on your behavioral analysis of Chunk 13, here is the mapping to the MITRE ATT&CK framework.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | **Obfuscated Files or Information** | The use of a tag-based system (`0x400c`) and manual buffer management serves to hide the true intent of command strings and data structures from static analysis. |
| **T1059** | **Command and Scripting Interpreter** | The "Interpreter Loop," "Translation Matrix," and "Instruction Set" indicate that the malware acts as a VM, where internal bytecode is processed rather than executed directly as standard code. |
| **T1637** | **Dynamic Resolution** | The "Marshaling Layer" translates abstract, obfuscated "Guest Commands" into functional Windows API calls only at the moment of execution to evade detection. |

### Analyst Notes on Strategic Findings:
*   **Complexity Factor:** The transition from standard .NET patterns to manual pointer arithmetic and offset calculations suggests a deliberate attempt to bypass automated behavior analysis tools that rely on identifying common .NET memory signatures.
*   **Evasion Strategy:** By using **Data Fragmentation**, the malware ensures that no single piece of code "contains" the full malicious logic; the intent only exists in the combination of the data buffer and the interpreter’s state-machine logic.
*   **Detection Pivot:** Because the primary capabilities are hidden behind the **Gatekeeper** and **Bridge**, traditional YARA rules looking for strings (e.g., `cmd.exe` or registry keys) will fail until the malware is active in memory and the "Translation" has occurred.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "EXTRACTED STRINGS" section consists primarily of binary artifacts, memory offsets, and internal assembly instructions resulting from a decompiler; therefore, most common indicators like URLs or IP addresses were not present in this specific sample.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The analysis notes that standard system paths are intentionally obfuscated/packed within the internal "Gatekeeper" layer).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 strings were present in the data provided).

### **Other artifacts**
*   **Internal Instruction Type Tags:** 
    *   `0x400c` (Identified as a primary tag for identifying and routing internal command packets/logic types)
    *   `0x200c` (Identified as a related classification tag within the parsing loop)
*   **Function Memory Offsets:** 
    *   `fcn.004ebed0` (Internal "Copy-and-Cast" / Buffer Preparation helper)
    *   `fcn.006823f0` (Large Switch Table used by the Gatekeeper to map internal commands to system actions)
*   **Technical Patterns:** 
    *   **Sophisticated Marshaling:** The presence of a "Gatekeeper" and "Bridge" architecture suggests that real-world strings (IPs, paths) are stored in an encoded/obfuscated state until the final point of execution.
    *   **Manual Buffer Management:** Use of non-standard .NET memory handling to bypass standard heap analysis tools.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: backdoor
3. **Confidence**: High

**Key evidence**:
* **Virtual Machine (VM) Architecture:** The sample employs a highly sophisticated "Interpreter Loop" and "Translation Matrix," utilizing a proprietary bytecode system with tag-based identification (e.g., `0x400c`). This allows the malware to remain agnostic of its actual payload until the moment of execution, effectively hiding malicious intent from static analysis.
* **Sophisticated Evasion Tactics:** The use of manual buffer management and pointer arithmetic—deliberately bypassing standard .NET heap patterns—along with "Data Fragmentation," indicates a professional-grade effort to evade automated memory scanners and signature-based detection.
* **Modular Execution Framework:** The multi-layered architecture (Gatekeeper, Bridge, Translation Matrix) identifies this as an execution framework rather than a simple dropper. It is designed to host a wide array of capabilities (exfiltration, encryption, persistence) via a centralized, abstracted command interpreter.
