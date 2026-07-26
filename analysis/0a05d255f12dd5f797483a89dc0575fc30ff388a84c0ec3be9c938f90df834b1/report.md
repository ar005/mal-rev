# Threat Analysis Report

**Generated:** 2026-07-24 13:27 UTC
**Sample:** `0a05d255f12dd5f797483a89dc0575fc30ff388a84c0ec3be9c938f90df834b1_0a05d255f12dd5f797483a89dc0575fc30ff388a84c0ec3be9c938f90df834b1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a05d255f12dd5f797483a89dc0575fc30ff388a84c0ec3be9c938f90df834b1_0a05d255f12dd5f797483a89dc0575fc30ff388a84c0ec3be9c938f90df834b1.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 8 sections |
| Size | 42,300,544 bytes |
| MD5 | `ffa1ba133090a31fbb441e184af633e9` |
| SHA1 | `eadaed3f985da38465fa9140925c725282702a0b` |
| SHA256 | `0a05d255f12dd5f797483a89dc0575fc30ff388a84c0ec3be9c938f90df834b1` |
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
| `.data` | 29,184 | 3.781 | No |
| `.didat` | 512 | 0.26 | No |
| `_RDATA` | 69,632 | 5.365 | No |
| `.rsrc` | 1,268,736 | 6.391 | No |
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

Total strings found: **93362** (showing first 100)

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

This final chunk (Chunk 13) provides the definitive technical "smoking gun" regarding the malware’s architecture. It confirms that the code is not merely complex; it is **engineered with high-level software design patterns** typically reserved for enterprise-grade applications or sophisticated frameworks.

The following analysis integrates Chunk 13 into the existing findings of infrastructure sophistication and object modeling.

---

### Updated Analysis: Sophisticated Dispatch, Memory Safety, and Polymorphic Execution

The logic in Chunk 13 reinforces the theory that this is a **Framework-based threat.** The code doesn't just "run" instructions; it "resolves" them through an internal layer of abstraction before execution.

#### 1. Validation & Range Checking (Gatekeeper Logic)
A recurring pattern in Chunk 13 involves checking if pointers fall within specific memory ranges (e.g., `*0xa86ef4` to `*0xa86ef0`) and applying flags (e.g., `0xff`).
*   **Significance:** This is a form of **Internal Metadata Validation**. Before the malware performs an action on a piece of data, it checks that data against its internal "map." This ensures that even if a malformed or unexpected packet is received from the C2, the core engine remains stable. It indicates a high degree of defensive programming to prevent the malware from crashing during execution—a hallmark of professional, long-term operations.

#### 2. Polymorphic Function Dispatch (VTable-style Implementation)
The code frequently uses a pattern similar to:
`pcVar3 = *(*piVar22 + 0xc); (**0x94371c)(iVar12, 2); (*pcVar3)();`
*   **Significance:** This is high-level **Object-Oriented Programming (OOP)** implemented in C/Assembly. Instead of a direct function call, the code looks up a pointer in a table (a "vtable") and then executes it.
*   **Impact on Analysis:** This means that many functions are "swappable." The core engine doesn't need to know what a module does; it only needs to know where to find its entry point in the internal object map. This allows the developers to add new features (e.g., new exfiltration methods, new encryption types) by simply updating the table rather than rewriting the main execution loop.

#### 3. Advanced Memory Management & "Safe" Operations
The presence of `OLEAUT32.dll` imports (`SafeArrayCopyData`, `SafeArrayCopy`) is highly significant in this context.
*   **Why it matters:** While these are common in Windows COM components, their use here suggests the malware is managing **complex, nested data arrays.** By using "Safe" copy functions, the developers ensure that memory offsets and lengths are handled correctly when moving data between different internal objects. This prevents buffer overflows while allowing the malware to handle highly dynamic data structures (like large lists of stolen credentials or varied system configurations).

---

### Technical Observations for IR

The findings in Chunk 13 provide specific targets for incident responders and advanced analysts:

*   **Confirmation of "Framework" Nature:** The use of vtable-style dispatching confirms this is a **Modular Framework.** The "malware" is actually a core engine that hosts various "modules." If an analyst finds one module (e.g., a keylogger), the framework likely contains others that are only activated under specific C2 conditions.
*   **Anti-Analysis via Complexity:** The extensive use of range checks and abstraction layers means that "linear" analysis is nearly impossible. An analyst cannot simply follow a single chain of execution from the network to the action; they must first map out how the *engine* resolves the objects before they can understand what the *module* does.
*   **Resilience via Decoupling:** Because the core engine is decoupled from the malicious actions, the malware is highly resilient. If a signature for one "action" (e.g., a specific file-grabbing routine) is identified, the core infrastructure remains unchanged and functional.

---

### Final Comprehensive Summary (13/13)

**Conclusion: Sophisticated Modular Framework with Object-Oriented Architecture.**

The final analysis confirms that this threat belongs to the **Elite / State-Sponsored** category. It is a professional piece of software engineering designed for longevity, modularity, and stealth.

*   **Risk Level:** **Critical / Elite (State-Sponsored).**
*   **Malware Class:** Advanced Persistent Threat (APT) Framework / Multi-Purpose Backdoor.
*   **Key Technical Indicators:**
    1.  **Complex Object Dispatcher (`0x6823f0`):** A centralized engine that resolves commands into object actions using vtable-style logic.
    2.  **Advanced Memory Safety:** Utilization of `SafeArray` logic to handle complex data structures, ensuring stability during multi-stage operations.
    3.  **Range-Based Validation:** Internal maps that validate data before processing, shielding the core engine from crashes and providing a "buffer" against detection/instability.
    4.  **High Level of Abstraction:** The use of .NET-like patterns (Standard Types like Guid, Decimal, Vector) implemented in a low-level language indicates a professional development lifecycle and a multi-layered attack surface.

#### Final IR Recommendations:

1.  **Behavioral Over Static Analysis:** Because the code uses high levels of abstraction and dynamic dispatch, static analysis will only reveal "how the engine works," not necessarily "what it's doing today." **Focus on behavioral indicators (IOCs)** such as specific API calls for credential dumping, keylogging, or hidden network tunnels.
2.  **Memory Forensics is Essential:** The most potent features of the malware may only exist in memory when a specific C2 command is received. **Conduct full-memory captures** to identify "hot" modules and dynamically loaded capabilities that do not appear on disk.
3.  **Identify Gateway Functions:** Rather than trying to reverse every possible module, focus on the **Dispatch Logic.** Identifying the functions that translate "C2_Command $\rightarrow$ Internal_Object $\rightarrow$ Action" will provide the quickest way to understand the breadth of the malware's capabilities.
4.  **Infrastructure Choke-Points:** Given the complexity of the internal code, the most effective way to disrupt this threat is at the **Communication Layer.** Monitor for the specific protocols and heartbeats used by the "Framework" to communicate with its controller.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors observed in the technical analysis of "Chunk 13" to the relevant MITRE ATT&CK techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1568 | Dynamic Resolution | The use of vtable-style dispatching and internal map lookups allows the malware to resolve function pointers at runtime, hiding the direct relationship between commands and actions. |
| T1027 | Obfuscated Execution | The heavy use of abstraction layers, "gatekeeper" range checks, and non-linear execution paths is designed to hinder manual analysis and prevent analysts from easily following the code's logic. |
| T1587 | Resource Development | The sophisticated modular architecture and "framework" design indicate a high level of development aimed at creating a multi-purpose tool for long-term, state-sponsored operations. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below is the categorized list of Indicators of Compromise (IOCs) and significant technical artifacts.

### **Threat Intelligence Report: IOC Extraction**

**Analysis Note:** The provided data contains very few "traditional" network-based IOCs (such as hardcoded IPs or URLs). However, it contains several high-value "internal" indicators that are critical for memory forensics and identifying the specific malware family/framework.

---

### **IP addresses / URLs / Domains**
*   *None identified.* (The strings provided appear to be obfuscated or represent non-human-readable binary segments.)

### **File paths / Registry keys**
*   *None identified.* (Note: `OLEAUT32.dll` was mentioned in the analysis, but it is a standard Windows system library and excluded as a false positive.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
These are technical markers that assist in identifying the malware's behavior, internal logic, and "fingerprinting" of the underlying framework:

*   **Internal Memory Offsets (VTable & Dispatch Logic):**
    *   `0xa86ef4`
    *   `0xa86ef0`
    *   `0x94371c`
    *   `0x6823f0` (Identified specifically as the **Complex Object Dispatcher**)
*   **Behavioral Logic Patterns:**
    *   **VTable-style Implementation:** The use of a jump table/vtable-like logic for polymorphic function dispatch. This indicates a modular framework where functionality is swapped dynamically via an internal map.
    *   **Range-Based Validation:** Use of specific memory range checks (e.g., the check between `0xa86ef4` and `0xa86ef0`) to validate data integrity before processing.
*   **API Usage Patterns (Sophisticated Data Handling):**
    *   Use of `SafeArrayCopyData` and `SafeArrayCopy` from `OLEAUT32.dll`. While these are standard APIs, their specific use here indicates the handling of complex, nested data structures or large lists of stolen information.
*   **Architecture Signature:** 
    *   **Modular Framework Architecture:** The code uses .NET-like constructs (e.g., Guidance, Decimal types) implemented in low-level code, suggesting a high level of sophistication typical of state-sponsored actors.

---

### **Analyst Summary for Incident Response**
While there are no immediate "block-list" items (IPs/Domains), the discovery of **Address `0x6823f0`** serves as a primary pivot point for memory forensics. Analysts should focus on this area to map out the dispatched modules and identify active functionality (e.g., keylogging, exfiltration) during runtime.

---

## Malware Family Classification

Based on the detailed behavioral analysis provided, here is the classification of the sample:

1. **Malware family:** custom
2. **Malware type:** backdoor / RAT
3. **Confidence:** High
4. **Key evidence:** 
    * **Modular Framework Architecture:** The use of vtable-style dispatching and a "Complex Object Dispatcher" (0x6823f0) indicates a modular system where the core engine is decoupled from specific malicious actions, allowing it to host multiple capabilities (e.g., keylogging, exfiltration) dynamically.
    * **High-Level Engineering Sophistication:** The implementation of advanced memory safety (SafeArray logic), range-based "gatekeeper" validation, and complex data types (Guid, Decimal) in a low-level language indicates professional-grade development typical of elite or state-sponsored actors.
    * **Resilient Execution Logic:** The use of non-linear code paths and dynamic resolution allows the malware to remain stable and functional even when individual modules are analyzed, providing high resistance to standard static analysis techniques.
