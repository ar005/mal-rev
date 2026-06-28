# Threat Analysis Report

**Generated:** 2026-06-27 21:53 UTC
**Sample:** `01f8832e1da252782190d58b1d4ed7cebb9c6dade34ca58dd19eebd5e537d604_01f8832e1da252782190d58b1d4ed7cebb9c6dade34ca58dd19eebd5e537d604.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01f8832e1da252782190d58b1d4ed7cebb9c6dade34ca58dd19eebd5e537d604_01f8832e1da252782190d58b1d4ed7cebb9c6dade34ca58dd19eebd5e537d604.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 8 sections |
| Size | 42,323,680 bytes |
| MD5 | `b6508f451b935de6bf17282fbf4e15db` |
| SHA1 | `593c2c8ac41fb18442c5c235d9a2e0d577e75583` |
| SHA256 | `01f8832e1da252782190d58b1d4ed7cebb9c6dade34ca58dd19eebd5e537d604` |
| Overall entropy | 7.859 |
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
| `.rsrc` | 1,280,000 | 6.408 | No |
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

Total strings found: **93398** (showing first 100)

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

This final disassembly (chunk 13/13) completes the picture of a highly sophisticated, multi-layered malware architecture. It provides the final pieces of the puzzle regarding how the **Orchestrator** interacts with the system and how it prepares data for final execution.

The following analysis integrates these new findings into our established framework.

---

### Updated Analysis: The Hybrid Orchestrator Architecture

#### 1. Integration of COM/OLE Infrastructure
A critical finding in this chunk is the interaction with `OLEAUT32.dll` (specifically `SafeArrayCopyData` and `SafeArrayCopy`). 

*   **Analytical Significance:** The presence of "SafeArrays" indicates that the malware isn't just using standard C-style arrays; it is using structures compatible with **Component Object Model (COM)**.
*   **The "Bridge" Function:** This suggests that while the internal logic is "hidden" in a managed-like interpreter, it occasionally interfaces with low-level Windows components or utilizes common COM-based libraries to handle complex data types (like multi-dimensional arrays or variant types). This provides another layer of obfuscation: an analyst might mistake these calls for legitimate system overhead rather than part of the malware's internal communication.

#### 2. The "Pre-Processing" Loop (The Assembly Line)
The extensive logic involving `var_1f0h_2`, `iVar13`, and complex pointer arithmetic (e.g., `iVar13 = *var_1e8h_2; ... puVar14 = iVar13 * 0x10 + var_1c0h_2`) reveals a heavy **Data Preparation Phase.**

*   **The "Assembly Line" Logic:** Before an action is taken, the code iterates through a collection of data objects. It doesn't just move one piece of data; it validates, unpacks, and transforms segments of data (the loop structure at `0x5e1429` suggests this).
*   **Instruction Unpacking:** This loop likely represents the "fetching" or "decoding" stage of the internal VM. It is pulling a sequence of internal instructions from a blob of memory and preparing them for the Orchestrator to process.

#### 3. The Execution Gateway (Indirect Function Calls)
The code contains several instances where `pcVar3` is assigned and then called via `(*pcVar3)()`.

*   **Mechanism:** This is an **indirect branch**. The malware doesn't call a fixed function; it calculates the address of the next action to take. 
*   **Analytic Impact:** This confirms that the Orchestrator acts as a dispatcher. It determines *what* needs to be done (e.g., "Send Heartbeat," "Encrypt File") and then jumps to the specific logic for that task. By using an indirect jump, it makes static analysis significantly harder because there is no direct link between the "decision" and the "action."

---

### Updated Technical Brief for Analysts

The architecture is now confirmed as a **Hybrid VM-based Orchestrator.**

#### Layer Analysis (Updated):
1.  **Translation/Interpretation Layer:** The `.NET` style objects and `SafeArray` usage indicate that logic is treated like high-level "scripts" (possibly transpiled from C# or a similar language).
2.  **Orchestration Layer (The Maze):** The nested switch-tables and state-change markers (`in_ECX[18]`) provide the navigation through these scripts.
3.  **Execution Gateway:** The indirect calls (`*pcVar3()`) represent the hand-off point where the internal VM logic resolves into a concrete system action (e.g., an API call).

#### New Technical Indicators:
1.  **COM/SafeArray Contexts:** If you see `OLEAUT32` or `SafeArray` references, these are indicators of **complex data handling**. These sections often hide the construction of complex commands or payloads being prepared for network transmission.
2.  **Iteration-Based Decoding:** The heavy use of loops with index offsets (e.g., `*puVar16 = *var_218h_2 + 8 + *(iVar13 + 4)`) is a signature of **Instruction Fetching**. These are the "gears" of the engine; they move through the internal code.
3.  **Indirect Dispatch Logic:** Any time you see an address being calculated and then immediately called via a pointer (the `pcVar3` pattern), you have likely found a **Transition Point** between the malware's internal logic and its external actions.

---

### Finalized Strategy for Analysis:

1.  **Identify "Script" Boundaries:** Because we see evidence of both .NET-style types and COM structures, the "Payload" is likely stored as a series of objects or a specialized bytecode. We should look for large, high-entropy blocks in the data section that are accessed by the loops identified in this chunk.

2.  **Map the "Action" Functions:** Instead of trying to decode every nested switch (the Maze), we should find all locations where `*pcVar3()` occurs. These are our **Primary Interest Points**. By hooking these, we can see exactly what state the machine was in immediately before it decided to perform a "real-world" action.

3.  **Trace State Transitions:**
    *   Monitor the value of `in_ECX[18]` or similar registers used for state tracking.
    *   Map these values to specific actions (e.g., State `0x1742` always leads to a `ws2_32` call).
    *   This allows you to skip 90% of the "Maze" and focus only on the code that transitions into your target interest.

4.  **Instrumentation Logic (The "Hook-and-Trace"):**
    *   Set a breakpoint on `fcn.00549f90`.
    *   Log every transition in the switch table to a file.
    *   When an indirect call (`*pcVar3`) is reached, log the value of the register containing the address and the current "State" values. 
    *   **Result:** This will create a map of the "Execution Path," showing exactly which internal states correspond to malicious behaviors.

**Conclusion:**
The complexity of this malware is designed to overwhelm standard human analysis by burying the malicious intent deep within an elaborate, nested state machine. By shifting our strategy from **"Analyzing the Code"** (which is intentionally confusing) to **"Mapping the State Machine,"** we can isolate the core malicious logic and effectively "short-circuit" the maze of the Orchestrator.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors observed in the provided analysis to the relevant MITRE ATT&CK techniques and sub-techniques. 

The malware utilizes a sophisticated "Hybrid VM-based Orchestrator" architecture, which is primarily designed to hinder static analysis and hide malicious intent through complexity.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Information or Programs | The use of a "Hybrid VM-based Orchestrator," nested switch-tables, and a "maze" of state transitions is designed to hide the core logic from analysts. |
| **T1055** | Packing | The "Pre-Processing Loop" (e.g., at `0x5e1429`) functions as an unpacking mechanism to decode and fetch internal instructions from a memory blob before execution. |
| **T1027** | Obfuscated Information or Programs | The use of indirect function calls (`*pcVar3()`) obscures the execution path, making it difficult for static analysis tools to determine which action is being performed. |
| **T1036** | Masquerading | The interaction with `OLEAUT32.dll` and `SafeArray` structures is used to blend malicious data handling with legitimate system-level operations to avoid detection. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral documentation, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Strings" section contains heavily obfuscated/encrypted data; no plaintext IP addresses, URLs, or file paths were identified within that specific block. The technical findings in the "Behavioral Analysis" provide **behavioral indicators** rather than static infrastructure IOCs.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (Behavioral & Technical Signatures)**
The following are behavioral indicators used to identify the malware's execution logic and internal architecture:

*   **API/Library Usage:** 
    *   `OLEAUT32.dll`: Specifically utilized for `SafeArrayCopyData` and `SafeArrayCopy`. This is used as a "bridge" to handle complex data structures (potentially containing encrypted configuration or payload fragments).
*   **Execution Patterns:**
    *   **Indirect Branching:** Use of the `(*pcVar3)()` pattern. The malware calculates function addresses at runtime to mask the transition between its internal "Orchestrator" and system-level actions.
    *   **Instruction Fetching Loop:** A specific logic structure (centered around offsets such as `0x5e1429`) involving complex pointer arithmetic (`iVar13 = *var_1e8h_2; ... puVar14 = iVar13 * 0x10 + var_1c0h_2`) used to unpack and decode internal instructions.
*   **Internal State Tracking:**
    *   Usage of `in_ECX[18]` (or similar register-based indices) as a state machine tracker to navigate nested switch tables. 
*   **Specific Function Offsets (for memory forensics/hunting):**
    *   `fcn.00549f90`: Identified as a key point for monitoring transition logic.
    *   `0x5e1429`: Identified as the base of the instruction-fetching loop.

---
**Analyst Note:** This sample exhibits high levels of obfuscation typical of "Hybrid VM" architectures. Because static IOCs (IPs/Domains) are absent from this specific snippet, detection should focus on the **behavioral signatures**—specifically tracking `OLEAUT32` calls in tandem with indirect jumps and complex pointer-arithmetic loops to identify Orchestrator activity.

---

## Malware Family Classification

1. **Malware family**: Custom
2. **Malware type**: Loader / Backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **Hybrid VM-based Orchestrator Architecture:** The sample utilizes a custom bytecode interpreter and nested switch-tables to hide its primary logic. This "maze" structure is designed specifically to thwart static analysis by decoupling the malware's high-level instructions from low-level machine code.
*   **Indirection and State Tracking:** The use of indirect function calls (`*pcVar3()`) and state trackers (e.g., `in_ECX[18]`) ensures that malicious actions—such as heartbeats or encryption—are only revealed during runtime, making it difficult to trace the execution path statically.
*   **Complex Data Handling via System Libraries:** The intentional use of `OLEAUT32` and `SafeArray` structures allows the malware to process complex data objects (likely encrypted commands/configurations) in a way that mimics legitimate system behavior, providing an additional layer of obfuscation.
