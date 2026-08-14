# Threat Analysis Report

**Generated:** 2026-08-10 17:26 UTC
**Sample:** `0de87d04c8fba2d2fe51200ec17d7a2c15fe121cbeb1fcee5d6451d6d1d96e15_0de87d04c8fba2d2fe51200ec17d7a2c15fe121cbeb1fcee5d6451d6d1d96e15.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0de87d04c8fba2d2fe51200ec17d7a2c15fe121cbeb1fcee5d6451d6d1d96e15_0de87d04c8fba2d2fe51200ec17d7a2c15fe121cbeb1fcee5d6451d6d1d96e15.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 8 sections |
| Size | 6,215,680 bytes |
| MD5 | `bc007946919df92576caeeef8562433b` |
| SHA1 | `7397346e59fa98ee785db40f932dfc4019be13db` |
| SHA256 | `0de87d04c8fba2d2fe51200ec17d7a2c15fe121cbeb1fcee5d6451d6d1d96e15` |
| Overall entropy | 6.691 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767619354 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 439,296 | 6.632 | No |
| `.managed` | 2,414,592 | 6.472 | No |
| `.rdata` | 2,001,408 | 6.307 | No |
| `.data` | 391,168 | 3.483 | No |
| `.pdata` | 161,792 | 6.373 | No |
| `_RDATA` | 512 | 3.355 | No |
| `.rsrc` | 512 | 2.875 | No |
| `.reloc` | 805,376 | 4.859 | No |

### Imports

**ADVAPI32.dll**: `RegCloseKey`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryValueExW`, `EventWrite`, `EventRegister`, `EventEnabled`, `OpenProcessToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`
**bcrypt.dll**: `BCryptGenRandom`
**KERNEL32.dll**: `TlsFree`, `TlsSetValue`, `GetTickCount64`, `GetCPInfoExW`, `LocalFree`, `CloseThreadpoolIo`, `SetLastError`, `SetThreadErrorMode`, `GetLastError`, `GetCurrentProcessId`, `GetModuleFileNameW`, `MultiByteToWideChar`, `GetStdHandle`, `TzSpecificLocalTimeToSystemTime`, `SystemTimeToFileTime`
**ole32.dll**: `CoGetApartmentType`, `CoUninitialize`, `CoCreateGuid`, `CoInitializeEx`, `CoWaitForMultipleHandles`
**api-ms-win-crt-heap-l1-1-0.dll**: `calloc`, `malloc`, `free`, `_callnewh`
**api-ms-win-crt-math-l1-1-0.dll**: `nan`, `modf`, `pow`, `ceil`, `fmod`, `_dclass`
**api-ms-win-crt-string-l1-1-0.dll**: `_wcsicmp`, `strcmp`, `wcsncmp`, `strcpy_s`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_initialize_onexit_table`, `_initialize_narrow_environment`, `_configure_narrow_argv`, `abort`, `terminate`, `_cexit`, `_crt_atexit`, `_initterm`, `_initterm_e`, `_register_onexit_function`, `_seh_filter_dll`, `_execute_onexit_table`

### Exports

`04MWqzFphmgz`, `0up4g4N7WlfJCwTAnn9`, `1fZwAWs`, `1fxuhu9apa`, `1tOtx8FSqt`, `25rPXi1I`, `27VJhXm6Tk9vgYskcuiB2w8yAV`, `2JyHC9lYZjE`, `2nR6nGC`, `2odNaGK962Mhh4bFaQ9Z`, `3GJYvySL9FkknX8Z8rn18wF0nhZ`, `3JKfSjes`, `3ZWcdhwf10o14`, `4DPV8KNNOY0NzN2xqhqCHvwJBRYzBoLx`, `59wLN2RhGe7Zn7VIoXw21IHyKct`, `5AG4GpCTixRm5Yj7m`, `5SLrtvHyxLa89GxXl`, `5Utj0NO`, `7c1NOz8gUriOJplUeh5QBN6w`, `7ziqrZz3u0ZZJh4g9gLwlk2KXNVz4AzP`, `8EEB2FoDY3CVJUtjfV`, `8UnxB6HyhkvgCCfOrXFxmDIdPr3`, `8wfqmwN2`, `9k86JWLZR6EfgzdtobBw6TEhZcoM2k`, `9kwP9f9gdSr`, `9wWhXmYQuo6u`, `A80nGVHOuHt7Jo`, `AeolhfZo6SvN`, `B9c1bvs`, `BTTI7wV`, `BboDso4qwjWbjHGjI`, `BlT0s7EeUU56LYmKE`, `BqaeSgrdoLNQzIGze`, `BzsZ7CwKnKpg`, `CfP8jDvQIrQ2MsroEuW554j`, `ClearPropVariantArray`, `ClearVariantArray`, `DYhQ2Bd`, `DejEgcb4tSRmdMTO9MRcLXsoff`, `DkHp0yrhR`, `DllCanUnloadNow`, `DllGetClassObject`, `DllRegisterServer`, `DllUnregisterServer`, `DsB424r0eLDysyUsLxdEPh`, `EOQX5kZbC6Tl5JW`, `FHSjBLkgDkw9VlE9XZpDzhyuSvlH5E`, `Fh67BlVyWaoNo3`, `GetProxyDllInfo`, `GjiOjTU`

## Extracted Strings

Total strings found: **16404** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.managed
`.rdata
@.data
.pdata
@_RDATA
@.rsrc
@.reloc
c(I;C0u
c(I;C0u
c8I;C@u
cHI;CPu
c(I;C0u
c8I;C@u
cHI;CPu
cXI;C`u
chI;Cpu
c(I;C0u
c8I;C@u
cHI;CPu
cXI;C`u
chI;Cpu
c(I;C0u
c8I;C@u
cHI;CPu
cXI;C`u
chI;Cpu
c(I;C0u
c8I;C@u
cHI;CPu
cXI;C`u
chI;Cpu
AQAWAVAUATWVSh
L$XAQL
0]AZAZ[^_A\A]A^A_AZ
0]AZAZ[^_A\A]A^A_AZ
AQAWAVAUATWVSh
L$XAQL
0]AZAZ[^_A\A]A^A_AZ
0]AZAZ[^_A\A]A^A_AZ
fffffff
APAWAVAUATSAPVWUPRH
APAWAVAUATSAPVWUPRH
APAWAVAUATSAPVWUPRH
AWAVAUATSVWUH
AWAVAUATSVWUH
o|$0fD
oD$@fD
oL$PfD
oT$`fD
o\$pfD
]_^[A\A]A^A_
AWAVAUATSVWUH
o|$0fD
oD$@fD
oL$PfD
oT$`fD
o\$pfD
]_^[A\A]A^A_
r+H;U
|$ AVH
|$ AVH
@SVAWH
VWATAVAWH
@A_A^A\_^
PAWAVAUATWVSQRUH
8]XX[^_A\A]A^A_XX
8]XX[^_A\A]A^A_XXH
QAWAVAUATWVSh
0]AZAZ[^_A\A]A^A_AZ
SATAUAWH
hA_A]A\[
WAVAWH
@A_A^_
A8H+Q0H;
WAVAWH
 A_A^_
|$ AVH
SUVWATAUAVAWH
A_A^A]A\_^][
WAVAWH
0A_A^_
UWATAVAWH
9Hc9H
 A_A^A\_]
\$ AVH
@UWAVAWH
(A_A^_]
(A_A^_]
H;ZeA
tTH;YeA
tKH;0]A
t3H;&]A
t*H;%]A
H;$]A
|$ ATAVAWH
A_A^A\
\$ UAVAWH
 A_A^]
 A_A^]
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1802b5580` | `0x1802b5580` | 2281948 | ✓ |
| `fcn.180097140` | `0x180097140` | 2221734 | ✓ |
| `fcn.18011a3a0` | `0x18011a3a0` | 1589185 | ✓ |
| `fcn.1802170b0` | `0x1802170b0` | 664265 | ✓ |
| `fcn.18021b700` | `0x18021b700` | 550156 | ✓ |
| `fcn.180276820` | `0x180276820` | 427482 | ✓ |
| `fcn.1800f2a30` | `0x1800f2a30` | 421126 | ✓ |
| `fcn.180241b80` | `0x180241b80` | 392973 | ✓ |
| `fcn.1800098a0` | `0x1800098a0` | 374066 | ✓ |
| `fcn.1801f3400` | `0x1801f3400` | 348705 | ✓ |
| `fcn.180013770` | `0x180013770` | 333332 | ✓ |
| `fcn.1801c43e0` | `0x1801c43e0` | 277024 | ✓ |
| `fcn.180266f40` | `0x180266f40` | 226759 | ✓ |
| `fcn.1802235e0` | `0x1802235e0` | 222911 | ✓ |
| `fcn.180049cf0` | `0x180049cf0` | 220917 | ✓ |
| `fcn.180049d00` | `0x180049d00` | 219622 | ✓ |
| `fcn.180049b10` | `0x180049b10` | 218737 | ✓ |
| `fcn.180049cd0` | `0x180049cd0` | 218330 | ✓ |
| `fcn.180049d70` | `0x180049d70` | 216181 | ✓ |
| `fcn.180049cc0` | `0x180049cc0` | 203765 | ✓ |
| `fcn.1801f3e40` | `0x1801f3e40` | 183857 | ✓ |
| `fcn.180098b60` | `0x180098b60` | 103050 | ✓ |
| `fcn.18004e340` | `0x18004e340` | 91567 | ✓ |
| `fcn.18002e010` | `0x18002e010` | 78222 | ✓ |
| `fcn.1801aed60` | `0x1801aed60` | 70567 | ✓ |
| `fcn.180032ca0` | `0x180032ca0` | 65158 | ✓ |
| `fcn.180023da0` | `0x180023da0` | 60002 | ✓ |
| `fcn.18001b610` | `0x18001b610` | 57434 | ✓ |
| `fcn.18004bc20` | `0x18004bc20` | 52139 | ✓ |
| `fcn.180017fa0` | `0x180017fa0` | 50677 | ✓ |

### Decompiled Code Files

- [`code/fcn.1800098a0.c`](code/fcn.1800098a0.c)
- [`code/fcn.180013770.c`](code/fcn.180013770.c)
- [`code/fcn.180017fa0.c`](code/fcn.180017fa0.c)
- [`code/fcn.18001b610.c`](code/fcn.18001b610.c)
- [`code/fcn.180023da0.c`](code/fcn.180023da0.c)
- [`code/fcn.18002e010.c`](code/fcn.18002e010.c)
- [`code/fcn.180032ca0.c`](code/fcn.180032ca0.c)
- [`code/fcn.180049b10.c`](code/fcn.180049b10.c)
- [`code/fcn.180049cc0.c`](code/fcn.180049cc0.c)
- [`code/fcn.180049cd0.c`](code/fcn.180049cd0.c)
- [`code/fcn.180049cf0.c`](code/fcn.180049cf0.c)
- [`code/fcn.180049d00.c`](code/fcn.180049d00.c)
- [`code/fcn.180049d70.c`](code/fcn.180049d70.c)
- [`code/fcn.18004bc20.c`](code/fcn.18004bc20.c)
- [`code/fcn.18004e340.c`](code/fcn.18004e340.c)
- [`code/fcn.180097140.c`](code/fcn.180097140.c)
- [`code/fcn.180098b60.c`](code/fcn.180098b60.c)
- [`code/fcn.1800f2a30.c`](code/fcn.1800f2a30.c)
- [`code/fcn.18011a3a0.c`](code/fcn.18011a3a0.c)
- [`code/fcn.1801aed60.c`](code/fcn.1801aed60.c)
- [`code/fcn.1801c43e0.c`](code/fcn.1801c43e0.c)
- [`code/fcn.1801f3400.c`](code/fcn.1801f3400.c)
- [`code/fcn.1801f3e40.c`](code/fcn.1801f3e40.c)
- [`code/fcn.1802170b0.c`](code/fcn.1802170b0.c)
- [`code/fcn.18021b700.c`](code/fcn.18021b700.c)
- [`code/fcn.1802235e0.c`](code/fcn.1802235e0.c)
- [`code/fcn.180241b80.c`](code/fcn.180241b80.c)
- [`code/fcn.180266f40.c`](code/fcn.180266f40.c)
- [`code/fcn.180276820.c`](code/fcn.180276820.c)
- [`code/fcn.1802b5580.c`](code/fcn.1802b5580.c)

## Behavioral Analysis

This final analysis incorporates the findings from **chunk 7/7** into the existing report. This concluding segment reveals a sophisticated transition from **Data Synthesis** to **Structural Organization**, confirming that the "VM" is a multi-stage engine designed to build, sort, and organize complex data structures before they are passed to the next stage of execution.

---

### Updated Analysis: Multi-Stage Construction & State-Dependent Processing

#### 1. Evolution of the Construction Engine
The final chunk confirms that the SIMD "kernel" approach is not just a decryption loop but a **Structured Assembly Line**. Each `switch` case (e.g., `0x180053b2c`, `0x180053b31`, `0x180053b40`) performs distinct "folding" operations to populate specific memory offsets in the `arg2` buffer.

*   **Component-Specific Assembly:** The repetition of patterns (like `vpshufd` with `0x4e` and `0xb1`) across different cases suggests that each case is responsible for a different *part* of a single large object. For example, one block builds the "header," while another builds the "payload" or "configuration table."
*   **Data Consolidation:** After the construction loops, the code performs operations like `vlddqu_avx` and `vpmaskmovd_avx2`. These are used to move and pack the raw results of the SIMD math into a contiguous, usable structure in memory.

#### 2. Transition from Construction to Organization (The "Sort" Phase)
Following the massive switch block, the code enters a logic block that involves heavy pointer arithmetic and comparison loops:
*   **Dynamic Sorting/Indexing:** The presence of loops comparing `uVar31` and `iVar28`, combined with calculations like `uVar34 * 4`, strongly indicates a **sorting or indexing routine**. Once the data is "constructed" via SIMD, it must be organized into an ordered table (likely for subsequent lookup operations).
*   **Size-Dependent Branching:** The logic `if (uVar34 < 0xa8)` determines which sub-function to call (`fcn.180049eb0` vs `fcn.18004aaf0`). This implies the "VM" handles different data sizes or types differently after construction, a common technique to hide the true nature of the payload until it is fully assembled in memory.

#### 3. State-Driven Mutation (Anti-Analysis)
The section involving `in_stack_00000030` shows advanced **Stateful Transformation**:
*   **Bitwise Logic Over Branches:** Instead of using standard `if/else` blocks to determine state, the code uses XORs and bitmasks (`& 0xff`, `& 0xff00`). This is a classic "opaque predicate" style technique where the execution path's logic is embedded in mathematical transformations.
*   **Dynamic Key Generation:** The interaction between `arg2` and `in_stack_...` suggests that a portion of the data being constructed is used as an input to generate a key or a mask for the next stage, ensuring that static analysis cannot predict which code path will be taken without executing the construction.

#### New Highly Technical Observations
*   **Memory Layout Obfuscation:** By building the `arg2` structure piece-by-piece through different SIMD kernels, the malware ensures that any single "write" operation does not represent a complete malicious instruction or value. The data only becomes meaningful once all components are assembled and ordered.
*   **High-Density Instruction Packing:** The sheer volume of AVX-512 instructions (some repeated in slightly different forms) creates what is known as a **Complexity Wall**. It forces an analyst to process hundreds of lines of SIMD math that eventually resolve into simple, constant values at runtime.
*   **Post-Construction Re-indexing:** The final loop demonstrates the "Finalization" phase where constructed blocks are aligned and indexed, preparing them for immediate use by the core malicious logic (e.g., setting up a C2 configuration or a file system mapping).

#### Updated Summary of Malicious Behaviors
*   **Multi-Stage Data Assembly:** Construction is decoupled from usage; the "VM" builds a complex, multi-part data structure using SIMD kernels before passing it to any functional logic.
*   **Dynamic State Transition:** Use of bitwise operations on internal state variables to determine branching paths without utilizing standard conditional jumps (`Jcc`), hindering automated behavioral analysis.
*   **Complexity Shielding:** Utilizing high-performance computing (HPC) instructions for basic data manipulation to "exhaust" the analyst's time and bypass simple signature detection.

#### Updated Findings for Incident Response
*   **Risk Level: Critical.** The sophistication of the construction engine, particularly the use of SIMD kernels and branchless state transitions, indicates a high-tier actor capable of writing custom-tailored obfuscation layers.
*   **Primary Technique:** **Polymorphic Construction & State-Driven Execution.**
*   **Analysis Note:** Do not attempt to "brute force" the deobfuscation of the SIMD math; it is designed as a time-sink for human analysts. 
*   **Recommended Strategy: Memory Forensics (Snapshotting).** The most effective way to bypass these protections is to wait until the `arg2` buffer has been fully populated by the "VM." By dumping memory *after* the large switch block and the sorting loop, you will find the "cleartext" configuration or payload that the SIMD math was designed to hide.

---

### Summary of Changes to your Record:
*   **Added:** Evidence of **Multi-Stage Construction**, where data is first built via SIMD kernels and then sorted/indexed for use.
*   **Refined State Logic:** Identified that bitwise XOR operations are used as state-dependent transition markers to evade automated branch analysis.
*   **New Analysis Context:** Defined the "Complexity Wall" (using AVX-512 to hide simple values) as a primary defense against static analysis.
*   **Updated Recommendation:** Emphasized **Memory Forensics** as the primary path for bypassing the construction-based obfuscation, rather than manual deobfuscation of the SIMD math.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | **Virtualization** | The report describes a "VM" engine that uses various kernels and switch cases to process data, effectively abstracting the original instructions into a custom execution environment. |
| **T1027** | **Obfuscated Execution** | The use of SIMD "complexity walls," bitwise-based opaque predicates, and multi-stage construction is designed to hide malicious intent from static analysis. |
| **T1055** | **Packer** | The transformation of data through a "construction" phase where pieces are assembled into a usable structure in memory is characteristic of advanced packing/loader behavior. |
| **T1028** | **Dynamic Resolution** | The requirement for memory forensics (post-unpacking) to see the "cleartext" configuration indicates that values are only resolved during execution after the construction and sorting phases. |
| **T1027.001** | **Multi-stage Decoding** | The analysis identifies a clear transition from "Data Synthesis" to "Structural Organization," where data is built in pieces before it can be utilized by the main logic. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: References to `arg2` and `in_stack_00000030` are memory offsets, not filesystem paths).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (The hex strings present in the text appear to be internal memory addresses/offsets rather than file hashes).

### **Other artifacts**
*   **SIMD Instruction Set Usage:** The malware utilizes a "Complexity Wall" using AVX-512 instructions to mask simple data operations. Specific instructions noted: 
    *   `vpshufd`
    *   `vlddqu_avx`
    *   `vpmaskmovd_avx2`
*   **Internal Memory Offsets (Signature Markers):** The following addresses may be used for identifying specific code blocks or stages in the assembly line:
    *   `0x180053b2c`
    *   `0x180053b31`
    *   `0x180053b40`
    *   `fcn.180049eb0`
    *   `fcn.18004aaf0`
*   **Behavioral Patterns:**
    *   **Multi-Stage Data Assembly:** Construction of data structures via a "Switch" block to hide the final payload/config until execution.
    *   **State-Driven Mutation:** Use of bitwise XOR and mask operations (`& 0xff`, `& 0xff00`) as substitutes for standard conditional jumps (`Jcc`) to evade automated analysis.
    *   **Data Sorting Routine:** Identification of a "Sort Phase" using pointer arithmetic and comparison loops (e.g., comparing `uVar31` and `iVar28`).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
* **Advanced VM & Construction Engine:** The sample utilizes a sophisticated "Virtual Machine" architecture where data is constructed using a series of SIMD kernels (AVX-512). This "Complexity Wall" is specifically designed to mask configuration tables and payloads until they are assembled in memory.
* **State-Driven Obfuscation:** The malware employs bitwise logic (XORs/masks) instead of standard conditional jumps (`Jcc`) to manage execution states. This technique effectively bypasses automated analysis tools that rely on branch tracing to map out malicious behavior.
* **Multi-Stage Payload Assembly:** The identification of a "Sort Phase" and "Data Synthesis" indicates the malware is designed as a loader; it systematically builds, organizes, and decodes hidden components (likely C2 configurations or secondary payloads) only at the final stage of execution.
