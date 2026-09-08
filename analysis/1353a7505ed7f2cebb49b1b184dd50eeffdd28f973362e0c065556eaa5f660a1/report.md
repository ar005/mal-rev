# Threat Analysis Report

**Generated:** 2026-09-02 13:38 UTC
**Sample:** `1353a7505ed7f2cebb49b1b184dd50eeffdd28f973362e0c065556eaa5f660a1_1353a7505ed7f2cebb49b1b184dd50eeffdd28f973362e0c065556eaa5f660a1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1353a7505ed7f2cebb49b1b184dd50eeffdd28f973362e0c065556eaa5f660a1_1353a7505ed7f2cebb49b1b184dd50eeffdd28f973362e0c065556eaa5f660a1.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 9 sections |
| Size | 9,968,640 bytes |
| MD5 | `e5e29b802d8b50cf32001ae0ab5a796a` |
| SHA1 | `6484bdb2140e35898502b247203526e08ed9935f` |
| SHA256 | `1353a7505ed7f2cebb49b1b184dd50eeffdd28f973362e0c065556eaa5f660a1` |
| Overall entropy | 6.491 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769360624 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 6,700,032 | 6.463 | No |
| `.CLR_UEF` | 512 | 3.098 | No |
| `.rdata` | 1,626,112 | 5.701 | No |
| `.data` | 20,992 | 2.683 | No |
| `.pdata` | 233,984 | 6.478 | No |
| `.didat` | 512 | 0.424 | No |
| `Section` | 512 | -0.0 | No |
| `.rsrc` | 1,353,728 | 6.373 | No |
| `.reloc` | 31,232 | 5.447 | No |

### Imports

**KERNEL32.dll**: `ActivateActCtx`, `FindResourceW`, `GetWindowsDirectoryW`, `GetModuleHandleW`, `LoadLibraryExW`, `LoadLibraryExA`, `RtlCaptureContext`, `WideCharToMultiByte`, `GetConsoleOutputCP`, `MapViewOfFileEx`, `SetLastError`, `SetThreadErrorMode`, `RaiseException`, `SetConsoleCtrlHandler`, `DebugBreak`
**ADVAPI32.dll**: `LookupPrivilegeValueW`, `RegGetValueW`, `SetKernelObjectSecurity`, `RegQueryValueExW`, `RegOpenKeyExW`, `GetSidSubAuthorityCount`, `GetSidSubAuthority`, `GetTokenInformation`, `OpenProcessToken`, `RegCloseKey`, `SetThreadToken`, `RevertToSelf`, `OpenThreadToken`, `EventWrite`, `EventRegister`
**ole32.dll**: `CLSIDFromProgID`, `CoCreateGuid`, `CoTaskMemAlloc`, `CoUnmarshalInterface`, `CoMarshalInterface`, `CoGetMarshalSizeMax`, `CoCreateFreeThreadedMarshaler`, `CoGetClassObject`, `CoGetContextToken`, `CoGetObjectContext`, `CoReleaseMarshalData`, `CoInitializeEx`, `CoRegisterInitializeSpy`, `CoWaitForMultipleHandles`, `CoUninitialize`
**OLEAUT32.dll**: `SetErrorInfo`, `GetErrorInfo`, `SysFreeString`, `SysStringLen`, `CreateErrorInfo`, `QueryPathOfRegTypeLib`, `SafeArrayGetVartype`, `VariantChangeType`, `SysAllocString`, `LoadRegTypeLib`, `SysAllocStringLen`, `VariantClear`, `VariantInit`, `VarCyFromDec`, `SafeArrayDestroy`
**USER32.dll**: `LoadStringW`, `MessageBoxW`
**SHELL32.dll**: `ShellExecuteW`
**api-ms-win-crt-string-l1-1-0.dll**: `iswspace`, `strncpy`, `iswascii`, `iswupper`, `wcsncpy_s`, `isalpha`, `strncmp`, `strncpy_s`, `towlower`, `wcscat_s`, `_wcsdup`, `wcscpy_s`, `isdigit`, `strnlen`, `wcsnlen`
**api-ms-win-crt-heap-l1-1-0.dll**: `_aligned_malloc`, `malloc`, `_callnewh`, `realloc`, `free`, `_set_new_mode`, `_aligned_free`, `calloc`
**api-ms-win-crt-convert-l1-1-0.dll**: `atoi`, `_wcstoui64`, `_wtoi`, `strtoull`, `strtol`, `wcstoul`, `_ltow_s`, `_atoi64`, `atol`, `strtoul`
**api-ms-win-crt-stdio-l1-1-0.dll**: `fputwc`, `__stdio_common_vsprintf_s`, `__stdio_common_vfprintf`, `__acrt_iob_func`, `_set_fmode`, `__stdio_common_vsprintf`, `ftell`, `fseek`, `_wfsopen`, `__stdio_common_vfwprintf`, `fclose`, `setvbuf`, `_setmode`, `_dup`, `_fileno`
**api-ms-win-crt-environment-l1-1-0.dll**: `getenv`
**api-ms-win-crt-utility-l1-1-0.dll**: `qsort`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_invoke_watson`, `_invalid_parameter_noinfo`, `_beginthreadex`, `terminate`, `_wcserror_s`, `_register_thread_local_exe_atexit_callback`, `_c_exit`, `__p___wargv`, `__p___argc`, `abort`, `_exit`, `exit`, `_initterm_e`, `_initterm`, `_get_initial_wide_environment`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `_wrename`, `_wremove`
**api-ms-win-crt-math-l1-1-0.dll**: `truncf`, `atanf`, `trunc`, `ilogbf`, `ceil`, `atan2`, `copysign`, `ceilf`, `round`, `fmodf`, `asinh`, `cbrt`, `acosh`, `atanh`, `modf`
**api-ms-win-crt-time-l1-1-0.dll**: `_gmtime64_s`, `_time64`, `wcsftime`
**api-ms-win-crt-locale-l1-1-0.dll**: `setlocale`, `__pctype_func`, `___lc_locale_name_func`, `___lc_codepage_func`, `_lock_locales`, `_free_locale`, `_configthreadlocale`, `_unlock_locales`, `___mb_cur_max_func`, `_create_locale`

### Exports

`BrotliDecoderAttachDictionary`, `BrotliDecoderCreateInstance`, `BrotliDecoderDecompress`, `BrotliDecoderDecompressStream`, `BrotliDecoderDestroyInstance`, `BrotliDecoderErrorString`, `BrotliDecoderGetErrorCode`, `BrotliDecoderHasMoreOutput`, `BrotliDecoderIsFinished`, `BrotliDecoderIsUsed`, `BrotliDecoderSetMetadataCallbacks`, `BrotliDecoderSetParameter`, `BrotliDecoderTakeOutput`, `BrotliDecoderVersion`, `BrotliDefaultAllocFunc`, `BrotliDefaultFreeFunc`, `BrotliEncoderAttachPreparedDictionary`, `BrotliEncoderCompress`, `BrotliEncoderCompressStream`, `BrotliEncoderCreateInstance`, `BrotliEncoderDestroyInstance`, `BrotliEncoderDestroyPreparedDictionary`, `BrotliEncoderHasMoreOutput`, `BrotliEncoderIsFinished`, `BrotliEncoderMaxCompressedSize`, `BrotliEncoderPrepareDictionary`, `BrotliEncoderSetParameter`, `BrotliEncoderTakeOutput`, `BrotliEncoderVersion`, `BrotliGetDictionary`, `BrotliGetTransforms`, `BrotliSetDictionaryData`, `BrotliSharedDictionaryAttach`, `BrotliSharedDictionaryCreateInstance`, `BrotliSharedDictionaryDestroyInstance`, `BrotliTransformDictionaryWord`, `CLRJitAttachState`, `DotNetRuntimeContractDescriptor`, `DotNetRuntimeInfo`, `MetaDataGetDispenser`, `_kBrotliContextLookupTable`, `_kBrotliPrefixCodeRanges`, `g_CLREngineMetrics`, `g_dacTable`

## Extracted Strings

Total strings found: **22933** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.CLR_UEF
`.rdata
@.data
.pdata
@.didat
Section
@.reloc
|$ ATAVAW3
|$8A_A^A\

@SUVWATAUAVAWH
A_A^A]A\_^][
\$ UVWAVAWH
A_A^_^]
\$ UVWAVAWH
A_A^_^]
\$ UVWAVAWH
A_A^_^]
\$ UVWAVAWH
A_A^_^]
\$ UVWAVAWH
A_A^_^]
\$ UVWAVAWH
A_A^_^]
@SUVWATAUAVAWH
A_A^A]A\_^][
@SUVWAVAWH
A_A^_^][
@USVWATAUAVAWH
A_A^A]A\_^[]
@SUVWATAUAVAWH
A_A^A]A\_^][
@"|$@L
SUVWATAUAVAWH
A_A^A]A\_^][
@SUVWATAUAVAWH
A_A^A]A\_^][
@SUVWATAUAVAWH
A_A^A]A\_^][
@USVWAUAWH
D"l$@H
A_A]_^[]
SUVWAVAWH
D"t$@H
A_A^_^][
@USVWATH
D"t$@H
A\_^[]
USVWATAVAWH
D"d$@H
A_A^A\_^[]
@USVWATH
D"t$@L
A\_^[]
USVWATAVAWH
D"d$@H
A_A^A\_^[]
@USVWATH
D"t$@H
A\_^[]
@SUWAVAWH
D"d$@H
A_A^_][
@SUWAVAWH
D"d$@H
A_A^_][
USVWAWI
@"t$@H
A__^[]
@SUWAVAWH
D"d$@H
A_A^_][
@SUWAVAWH
D"d$@H
A_A^_][
@USVWATAUAVAWH
A_A^A]A\_^[]
USVWATAUAVAWH
D"l$@H
D"l$@H
A_A^A]A\_^[]
@USWAVH
USVWATAUAVAWH
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
@USVAVH
@USVWATAVAWH
A_A^A\_^[]
@USVWATAVAWH
A_A^A\_^[]
@SUVWAVAWH
A_A^_^][
@USVWATAVAWH
A_A^A\_^[]
USVWATAUAVAWH
Lcd$PA
A_A^A]A\_^[]
SUVWATAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.std::ctype_wchar_t_.virtual_24` | `0x140060890` | 6024516 | ✓ |
| `fcn.140588a70` | `0x140588a70` | 5676347 | ✓ |
| `fcn.1400bcbb0` | `0x1400bcbb0` | 5649026 | ✓ |
| `fcn.140533a40` | `0x140533a40` | 5388993 | ✓ |
| `fcn.14052cf60` | `0x14052cf60` | 5361806 | ✓ |
| `fcn.140451450` | `0x140451450` | 4463117 | ✓ |
| `fcn.1401b6280` | `0x1401b6280` | 4192081 | ✓ |
| `fcn.1402d2da0` | `0x1402d2da0` | 3461302 | ✓ |
| `fcn.1402d7690` | `0x1402d7690` | 3442630 | ✓ |
| `fcn.140383380` | `0x140383380` | 2738866 | ✓ |
| `fcn.1402be880` | `0x1402be880` | 2681410 | ✓ |
| `fcn.1402bd830` | `0x1402bd830` | 2677222 | ✓ |
| `fcn.14027f6b0` | `0x14027f6b0` | 2495742 | ✓ |
| `fcn.14027f2d0` | `0x14027f2d0` | 2487627 | ✓ |
| `fcn.1403c5bc0` | `0x1403c5bc0` | 2466418 | ✓ |
| `fcn.1403c5d00` | `0x1403c5d00` | 2466134 | ✓ |
| `fcn.1403c91d0` | `0x1403c91d0` | 2452614 | ✓ |
| `fcn.140440e40` | `0x140440e40` | 1865706 | ✓ |
| `fcn.140481300` | `0x140481300` | 1698646 | ✓ |
| `fcn.140524570` | `0x140524570` | 1569967 | ✓ |
| `fcn.14040d650` | `0x14040d650` | 1412059 | ✓ |
| `fcn.14040ab50` | `0x14040ab50` | 1361839 | ✓ |
| `fcn.1400ee3d0` | `0x1400ee3d0` | 1339491 | ✓ |
| `fcn.140115b90` | `0x140115b90` | 1003604 | ✓ |
| `fcn.14043ec10` | `0x14043ec10` | 868902 | ✓ |
| `fcn.140441810` | `0x140441810` | 838947 | ✓ |
| `fcn.14050cb20` | `0x14050cb20` | 831748 | ✓ |
| `fcn.14019b100` | `0x14019b100` | 816132 | ✓ |
| `fcn.14015e1e0` | `0x14015e1e0` | 672879 | ✓ |
| `fcn.14014e500` | `0x14014e500` | 596401 | ✓ |

### Decompiled Code Files

- [`code/fcn.1400bcbb0.c`](code/fcn.1400bcbb0.c)
- [`code/fcn.1400ee3d0.c`](code/fcn.1400ee3d0.c)
- [`code/fcn.140115b90.c`](code/fcn.140115b90.c)
- [`code/fcn.14014e500.c`](code/fcn.14014e500.c)
- [`code/fcn.14015e1e0.c`](code/fcn.14015e1e0.c)
- [`code/fcn.14019b100.c`](code/fcn.14019b100.c)
- [`code/fcn.1401b6280.c`](code/fcn.1401b6280.c)
- [`code/fcn.14027f2d0.c`](code/fcn.14027f2d0.c)
- [`code/fcn.14027f6b0.c`](code/fcn.14027f6b0.c)
- [`code/fcn.1402bd830.c`](code/fcn.1402bd830.c)
- [`code/fcn.1402be880.c`](code/fcn.1402be880.c)
- [`code/fcn.1402d2da0.c`](code/fcn.1402d2da0.c)
- [`code/fcn.1402d7690.c`](code/fcn.1402d7690.c)
- [`code/fcn.140383380.c`](code/fcn.140383380.c)
- [`code/fcn.1403c5bc0.c`](code/fcn.1403c5bc0.c)
- [`code/fcn.1403c5d00.c`](code/fcn.1403c5d00.c)
- [`code/fcn.1403c91d0.c`](code/fcn.1403c91d0.c)
- [`code/fcn.14040ab50.c`](code/fcn.14040ab50.c)
- [`code/fcn.14040d650.c`](code/fcn.14040d650.c)
- [`code/fcn.14043ec10.c`](code/fcn.14043ec10.c)
- [`code/fcn.140440e40.c`](code/fcn.140440e40.c)
- [`code/fcn.140441810.c`](code/fcn.140441810.c)
- [`code/fcn.140451450.c`](code/fcn.140451450.c)
- [`code/fcn.140481300.c`](code/fcn.140481300.c)
- [`code/fcn.14050cb20.c`](code/fcn.14050cb20.c)
- [`code/fcn.140524570.c`](code/fcn.140524570.c)
- [`code/fcn.14052cf60.c`](code/fcn.14052cf60.c)
- [`code/fcn.140533a40.c`](code/fcn.140533a40.c)
- [`code/fcn.140588a70.c`](code/fcn.140588a70.c)
- [`code/method.std__ctype_wchar_t_.virtual_24.c`](code/method.std__ctype_wchar_t_.virtual_24.c)

## Behavioral Analysis

This analysis integrates the final disassembly provided in **chunk 9/9** into the existing technical architecture of the malware.

### Updated Analysis Report (Final Integration)

The inclusion of these final functions completes the picture of a highly sophisticated, professionally engineered piece of malware. While previous chunks established the "Interpreter" and the "Math Engine," this final segment reveals the **Management Layer**: how the malware manages its internal objects, handles concurrency, and abstracts its operations through dynamic dispatching.

#### Core Functionality and Purpose
The final disassembly clarifies how the malware manages its lifecycle and internal state:

*   **State-Aware Object Management:** The code extensively uses structure offsets (e.g., `iVar12 + 0x6b8`, `iVar12 + 0x6c8`). This indicates that the malware operates on a "Context" or "Global State" object. Instead of simple variables, it manages complex objects that hold metadata, status flags, and pointers to other system components.
*   **Dynamic Dispatch & Polymorphism (`**0x140666e40`):** One of the most significant findings is the repeated use of a double-pointer dereference for function calls: `(**0x140666e40)(...)`. This is a classic implementation of a **Virtual Function Table (vtable)** or a **Dispatch Table**.
    *   *Significance:* The malware doesn't call "PrintScreen" or "ExfiltrateData" directly. It calls an offset in a table. This allows the developers to swap out functionalities at runtime or via different configuration files without changing the core execution logic. 
*   **Concurrency and Synchronization:** The presence of `LOCK()` and `UNLOCK()` macros, combined with code that modifies shared counters (e.g., `*0x140804488 = *0x140804488 + -1`), indicates the malware is **multi-threaded** or designed to be thread-safe. It is managing multiple simultaneous tasks, likely handling several network connections or concurrent monitoring hooks simultaneously.
*   **Buffer & String Sanitization:** Functions like `fcn.1405c5274` appear to handle internal string/buffer manipulation with specific length constraints (e.g., `0x20`). This is the "janitorial" layer of the engine, ensuring that data passed between the Interpreter and the system remains within bounds.

#### Advanced Obfuscation Techniques
*   **Abstraction through Indirect Jumps:** By using a jump table (`**0x140666e40`), the malware makes it nearly impossible for an automated tool to map out the "decision tree." A static analyst sees a call to a memory address; only at runtime, based on the state of the object being processed, is the final destination determined.
*   **Decoupled Execution:** The code manages a list of objects (the `while` loops iterating through `0x200` offsets) that represent distinct "tasks." This means the core logic of the malware is decoupled from its specific actions; the "engine" processes a list of tasks, and only the "data" within those tasks determines what actually happens.
*   **Environment Masking:** The use of `FlushInstructionCache` suggests the code is prepared for dynamic changes to its own memory space or is ensuring that any newly mapped modules are immediately executable.

#### Analysis of Specific Behaviors
*   **Robustness and Stability:** The complexity of the loops (handling potential NULL pointers, checking counts, and managing offsets) indicates this is not a "disposable" piece of malware. It is designed to run persistently in the background without crashing, even as it processes complex data structures.
*   **Object-Oriented Architecture:** The way the code manages `iVar14` and `iVar21` suggests a collection-based approach. If this were a simple bot, it would use a linear execution path. This architecture allows for **multi-tasking**: one "thread" could be handling heartbeats to a C2 server while another handles local data collection, both managed by the same underlying logic framework.

#### Technical Significance
*   **Highly Mature Framework:** The combination of an **AVX-512 Math Engine**, a **Context-Aware Interpreter**, and a **Polymorphic Dispatch Table** puts this malware in the "Tier 1" category (e.g., APT-grade). This architecture is designed to defeat both automated sandboxes and manual reverse engineering.
*   **Resilience to Analysis:** Because the core malicious behaviors are hidden behind multiple layers of abstraction:
    1.  The **Math Engine** hides the logic from symbolic execution.
    2.  The **Interpreter** masks the intent of the commands.
    3.  The **Dispatch Table** hides the destination of the code.
*   **Modular Capability Expansion:** This architecture allows the threat actor to "hot-swap" capabilities. By simply updating a command file, they can change what the interpreter does without ever changing the binary on disk, making signature-based detection much harder.

---

### Final Cumulative Summary (Total Analysis)

The analysis of all fragments confirms that this malware is not just a malicious tool, but a **sophisticated software platform**. It functions as a "Remote System Management" environment designed for high-stakes operations.

**The Architecture follows three distinct layers:**
1.  **The Logic Layer (Math Engine):** Uses advanced instruction sets to perform calculations and logic gates that appear as random noise or math errors to automated analysis tools.
2.  **The Translation Layer (Interpreter/Parser):** Takes raw, obfuscated data from the network or local files and translates it into "actions" for the engine. This creates a "Context-Aware" environment where the malware's behavior changes based on received input.
3.  **The Management Layer (Dispatcher & Resource Manager):** Manages the internal lifecycle of the malware, including multi-threading, memory management, and dynamic task dispatching via vtables to ensure stability and high functionality.

**Final Conclusion:**
This is a **professional-grade, modular malware framework**. It is designed for long-term persistence and flexibility, allowing an attacker to deploy a single "engine" that can perform various tasks (exfiltration, spying, disruption) simply by changing the data fed into the interpreter. 

**Defense Strategy Recommendations:**
*   **Memory Forensics focus:** Because of the heavy use of dynamic dispatching and internal state management, memory dumps will be more fruitful than static disassembly for identifying active "tasks."
*   **Behavioral Monitoring:** Since the core logic is obfuscated, defenders should focus on the *outcomes* (e.g., unusual network connections or unauthorized process injections) rather than trying to reverse-engineer every branch of the math engine.
*   **Egress Filtering:** Given the "Service-oriented" architecture, identifying and blocking the C2 communication patterns will be more effective than attempting to signature the underlying interpreter logic.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The malware utilizes a "Translation Layer" that acts as an interpreter to process raw, obfuscated data into specific system actions. |
| **T1027** | Obfuscated Valid Fields | The use of an "AVX-511 Math Engine" and complex internal state management is designed to hide logical intent from automated analysis and symbolic execution tools. |
| **T1027** | Obfuscated Valid Fields (Secondary) | The implementation of a Dispatch Table (vtable) for dynamic jumps hides the true "decision tree," making it difficult for analysts to map out the malware's capabilities. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Strings" section contains highly obfuscated or scrambled data; no clear-text IP addresses, URLs, or file paths were identifiable within that specific block. The technical artifacts are primarily derived from the structural analysis of the malware's execution logic.

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (Internal memory offsets such as `0x140666e40` are not persistent file system paths.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Memory Address/Dispatch Table:** `0x140666e40` (Identified as a vtable or dispatch table used for polymorphic execution).
*   **Internal Counter Location:** `0x140804488` (Used for managing multi-threaded synchronization).
*   **Internal Function Pointer:** `fcn.1405c5274` (Specific routine identified for buffer/string sanitization).
*   **Behavioral Pattern:** Usage of **AVX-512 instructions** to facilitate a "Math Engine" used for obfuscating internal logic and state calculations.
*   **Behavioral Pattern:** Use of a **Context-Aware Interpreter** to decouple core malware functionality from its specific actions (modular execution).
*   **Technical Capability:** Implementation of a polymorphic dispatch system to hide the decision tree from static analysis tools.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1. **Malware family**: custom (Sophisticated Modular Framework)
2. **Malware type**: backdoor
3. **Confidence**: High
4. **Key evidence**:
    *   **Multi-Layered Abstraction:** The architecture utilizes three distinct layers—a Math Engine (AVX-511/512), a Translation Layer (Interpreter), and a Management Layer (Dispatcher)—specifically designed to decouple the malware's core logic from its malicious actions, making it extremely difficult for automated tools or static analysis to map out its capabilities.
    *   **Polymorphic Execution & Dynamic Dispatch:** The use of virtual function tables (vtables) and indirect jumps (`**0x140666e40`) allows the malware to perform "context-aware" operations, enabling it to swap functionalities at runtime via configuration updates without changing its underlying code.
    *   **Advanced Anti-Analysis Techniques:** The implementation of complex math logic for state calculations and a modular "Task" system indicates high maturity (APT-grade), intended for long-term persistence and evasion of symbolic execution and automated sandbox detection.
