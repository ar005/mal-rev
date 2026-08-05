# Threat Analysis Report

**Generated:** 2026-08-03 17:35 UTC
**Sample:** `0ce76e80399b4b281aba1687b761aaaf3f90dc3caf5a1aba8129968b618a7d22_0ce76e80399b4b281aba1687b761aaaf3f90dc3caf5a1aba8129968b618a7d22.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ce76e80399b4b281aba1687b761aaaf3f90dc3caf5a1aba8129968b618a7d22_0ce76e80399b4b281aba1687b761aaaf3f90dc3caf5a1aba8129968b618a7d22.exe` |
| File type | PE32+ executable for MS Windows 5.02 (DLL), x86-64 (stripped to external PDB), 11 sections |
| Size | 270,848 bytes |
| MD5 | `07379b75d389ae2d3cb03494955b1443` |
| SHA1 | `14d84cbd7cbe86c3fba60197d9f1668f3feb28e0` |
| SHA256 | `0ce76e80399b4b281aba1687b761aaaf3f90dc3caf5a1aba8129968b618a7d22` |
| Overall entropy | 6.99 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1775850836 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 58,368 | 6.009 | No |
| `.data` | 512 | 0.372 | No |
| `.rdata` | 12,288 | 6.17 | No |
| `.pdata` | 2,048 | 4.691 | No |
| `.xdata` | 3,584 | 5.264 | No |
| `.bss` | 0 | 0.0 | No |
| `.edata` | 512 | 3.902 | No |
| `.idata` | 5,120 | 4.542 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 186,368 | 7.169 | ⚠️ Yes |
| `.reloc` | 512 | 0.93 | No |

### Imports

**bcrypt.dll**: `BCryptGenRandom`
**CFGMGR32.dll**: `CM_Get_DevNode_PropertyW`, `CM_MapCrToWin32Err`
**d2d1.dll**: `D2D1CreateFactory`
**libgcc_s_seh-1.dll**: `_Unwind_Resume`
**GDI32.dll**: `BitBlt`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `CreateDIBSection`, `DeleteDC`, `DeleteObject`, `GetDIBits`, `SelectObject`
**KERNEL32.dll**: `DeleteCriticalSection`, `DisableThreadLibraryCalls`, `EnterCriticalSection`, `EnumSystemCodePagesW`, `GetLastError`, `InitializeCriticalSection`, `LeaveCriticalSection`, `Sleep`, `TlsGetValue`, `VirtualAlloc`, `VirtualProtect`, `VirtualQuery`
**api-ms-win-crt-heap-l1-1-0.dll**: `calloc`, `free`
**api-ms-win-crt-math-l1-1-0.dll**: `ceilf`, `cosf`, `expf`, `sinf`, `sqrtf`
**api-ms-win-crt-private-l1-1-0.dll**: `memcpy`, `memmove`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_execute_onexit_table`, `_exit`, `_initialize_onexit_table`, `_initterm`, `_initterm_e`, `_register_onexit_function`, `abort`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__acrt_iob_func`, `__stdio_common_vfprintf`
**api-ms-win-crt-string-l1-1-0.dll**: `strlen`, `strncmp`, `wcslen`, `wcsncpy_s`
**ole32.dll**: `CoTaskMemAlloc`
**SETUPAPI.dll**: `CM_Get_DevNode_Status`, `CM_Locate_DevNodeW`, `SetupDiDestroyDeviceInfoList`, `SetupDiEnumDeviceInterfaces`, `SetupDiGetClassDevsW`, `SetupDiGetDeviceInterfaceDetailW`, `SetupDiGetDeviceRegistryPropertyW`
**libstdc++-6.dll**: `_ZNKSt8__detail20_Prime_rehash_policy14_M_need_rehashEyyy`, `_ZNSt7__cxx1112basic_stringIwSt11char_traitsIwESaIwEE10_M_disposeEv`, `_ZNSt7__cxx1112basic_stringIwSt11char_traitsIwESaIwEE10_M_replaceEyyPKwy`, `_ZNSt7__cxx1112basic_stringIwSt11char_traitsIwESaIwEE13_M_set_lengthEy`, `_ZNSt7__cxx1112basic_stringIwSt11char_traitsIwESaIwEE7_S_copyEPwPKwy`, `_ZNSt7__cxx1112basic_stringIwSt11char_traitsIwESaIwEE9_M_createERyy`, `_ZNSt7__cxx1112basic_stringIwSt11char_traitsIwESaIwEEC1EOS4_`, `_ZNSt7__cxx1112basic_stringIwSt11char_traitsIwESaIwEEC1ERKS4_`, `_ZNSt8__detail15_List_node_base11_M_transferEPS0_S1_`, `_ZNSt8__detail15_List_node_base4swapERS0_S1_`, `_ZNSt8__detail15_List_node_base7_M_hookEPS0_`, `_ZSt17__throw_bad_allocv`, `_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base`, `_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base`, `_ZSt19__throw_logic_errorPKc`
**USER32.dll**: `GetClientRect`

### Exports

`ApplyUnsharpMaskFilter`, `CreateImageMosaic`, `DrawConcentricRings`, `DrawSankeyDiagram`, `EnumerateDeviceInterfaces`, `ObjectCode`, `QueryDeviceInstanceProperties`, `RenderNetworkGraph`, `RenderStackedAreaChart`, `image`

## Extracted Strings

Total strings found: **624** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.edata
@.idata
@.reloc
9x s1
9x s1
9x s1
9x s1
9x }1
9x s1
9x s1
AWAVAUATUWVSH
H+D$xH
T$hH+T$XH
|$XH9|$p
H9D$0t
H+T$8H
T$XH+T$xH
L9d$0tVH
[^_]A\A]A^A_
AWAVAUATUWVSH
L+l$8H
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
H+L$HH
H+\$hH
t
D;p 
[^_]A\A]A^A_
AWAVAUATUWVSH
t
D9g 
xD9g ~0L
D9` }CL
D9D$x~W1
D9D$x~e1
H9\$Xt_H
\$`H9\$Xt
[^_]A\A]A^A_
AWAVAUATUWVSH
D9h sGH
D;h sI
H+|$XH
H+T$XH
H9t$pthH
H9t$pt
[^_]A\A]A^A_
AWAVAUATUWVSH
L9d$Xu
L;d$`u>
L;d$`u~
H+D$HH
[^_]A\A]A^A_
AWAVAUATUWVSH
>333?H
?333?H
fff?333?H
L?333?H
333?333?H
W$H9\$`
|$XH9|$`
|$8H9|$Pt_H
t$8H9t$0t
[^_]A\A]A^A_
AWAVAUATUWVSH
H9D$@H
t
D;` 
L9t$ptQL9t$8t
[^_]A\A]A^A_
UAWAVAUATWVSH
[^_A\A]A^A_]
([^_]H
@' t	H
AUATUWVSH
H[^_]A\A]
AUATUWVSH
H[^_]A\A]
AUATUWVSH
H[^_]A\A]
AUATUWVSH
H[^_]A\A]
ATUWVSH
 [^_]A\
ATUWVSH
 [^_]A\
ATUWVSH
 [^_]A\
AUATUWVSH
D;n r
G E9h 
D9h s?H
D;h sI
8[^_]A\A]
AUATUWVSH
D;n r
G E9h 
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.391eab1f0` | `0x391eab1f0` | 44494 | ✓ |
| `sym.dopuslib.dll_CreateImageMosaic` | `0x391ea5fcb` | 6008 | ✓ |
| `sym.dopuslib.dll_DrawSankeyDiagram` | `0x391ea77e6` | 4966 | ✓ |
| `sym.dopuslib.dll_RenderNetworkGraph` | `0x391ea9d23` | 4786 | ✓ |
| `sym.dopuslib.dll_ApplyUnsharpMaskFilter` | `0x391ea4db2` | 4633 | ✓ |
| `sym.dopuslib.dll_RenderStackedAreaChart` | `0x391ea8b4c` | 4567 | ✓ |
| `sym.dopuslib.dll_EnumerateDeviceInterfaces` | `0x391ea3d9c` | 4118 | ✓ |
| `sym.dopuslib.dll_DrawConcentricRings` | `0x391ea26c7` | 3570 | ✓ |
| `sym.dopuslib.dll_ObjectCode` | `0x391ea1cc7` | 2560 | ✓ |
| `sym.dopuslib.dll_QueryDeviceInstanceProperties` | `0x391ea34b9` | 2275 | ✓ |
| `fcn.391eab510` | `0x391eab510` | 912 | ✓ |
| `section..text` | `0x391ea1000` | 496 | ✓ |
| `fcn.391eadcf0` | `0x391eadcf0` | 485 | ✓ |
| `fcn.391eadee0` | `0x391eadee0` | 477 | ✓ |
| `fcn.391eae2f0` | `0x391eae2f0` | 473 | ✓ |
| `fcn.391eae890` | `0x391eae890` | 452 | ✓ |
| `fcn.391eae620` | `0x391eae620` | 378 | ✓ |
| `fcn.391eadcc0` | `0x391eadcc0` | 378 | ✓ |
| `fcn.391eae210` | `0x391eae210` | 378 | ✓ |
| `fcn.391ead9f0` | `0x391ead9f0` | 373 | ✓ |
| `fcn.391ead5a0` | `0x391ead5a0` | 373 | ✓ |
| `fcn.391eab3a0` | `0x391eab3a0` | 368 | ✓ |
| `fcn.391ead720` | `0x391ead720` | 367 | ✓ |
| `fcn.391ead890` | `0x391ead890` | 351 | ✓ |
| `fcn.391eac500` | `0x391eac500` | 345 | ✓ |
| `fcn.391eac340` | `0x391eac340` | 345 | ✓ |
| `fcn.391eac6c0` | `0x391eac6c0` | 345 | ✓ |
| `fcn.391eac890` | `0x391eac890` | 345 | ✓ |
| `fcn.391eaead0` | `0x391eaead0` | 337 | ✓ |
| `fcn.391eaed10` | `0x391eaed10` | 337 | ✓ |

### Decompiled Code Files

- [`code/fcn.391eab1f0.c`](code/fcn.391eab1f0.c)
- [`code/fcn.391eab3a0.c`](code/fcn.391eab3a0.c)
- [`code/fcn.391eab510.c`](code/fcn.391eab510.c)
- [`code/fcn.391eac340.c`](code/fcn.391eac340.c)
- [`code/fcn.391eac500.c`](code/fcn.391eac500.c)
- [`code/fcn.391eac6c0.c`](code/fcn.391eac6c0.c)
- [`code/fcn.391eac890.c`](code/fcn.391eac890.c)
- [`code/fcn.391ead5a0.c`](code/fcn.391ead5a0.c)
- [`code/fcn.391ead720.c`](code/fcn.391ead720.c)
- [`code/fcn.391ead890.c`](code/fcn.391ead890.c)
- [`code/fcn.391ead9f0.c`](code/fcn.391ead9f0.c)
- [`code/fcn.391eadcc0.c`](code/fcn.391eadcc0.c)
- [`code/fcn.391eadcf0.c`](code/fcn.391eadcf0.c)
- [`code/fcn.391eadee0.c`](code/fcn.391eadee0.c)
- [`code/fcn.391eae210.c`](code/fcn.391eae210.c)
- [`code/fcn.391eae2f0.c`](code/fcn.391eae2f0.c)
- [`code/fcn.391eae620.c`](code/fcn.391eae620.c)
- [`code/fcn.391eae890.c`](code/fcn.391eae890.c)
- [`code/fcn.391eaead0.c`](code/fcn.391eaead0.c)
- [`code/fcn.391eaed10.c`](code/fcn.391eaed10.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sym.dopuslib.dll_ApplyUnsharpMaskFilter.c`](code/sym.dopuslib.dll_ApplyUnsharpMaskFilter.c)
- [`code/sym.dopuslib.dll_CreateImageMosaic.c`](code/sym.dopuslib.dll_CreateImageMosaic.c)
- [`code/sym.dopuslib.dll_DrawConcentricRings.c`](code/sym.dopuslib.dll_DrawConcentricRings.c)
- [`code/sym.dopuslib.dll_DrawSankeyDiagram.c`](code/sym.dopuslib.dll_DrawSankeyDiagram.c)
- [`code/sym.dopuslib.dll_EnumerateDeviceInterfaces.c`](code/sym.dopuslib.dll_EnumerateDeviceInterfaces.c)
- [`code/sym.dopuslib.dll_ObjectCode.c`](code/sym.dopuslib.dll_ObjectCode.c)
- [`code/sym.dopuslib.dll_QueryDeviceInstanceProperties.c`](code/sym.dopuslib.dll_QueryDeviceInstanceProperties.c)
- [`code/sym.dopuslib.dll_RenderNetworkGraph.c`](code/sym.dopuslib.dll_RenderNetworkGraph.c)
- [`code/sym.dopuslib.dll_RenderStackedAreaChart.c`](code/sym.dopuslib.dll_RenderStackedAreaChart.c)

## Behavioral Analysis

Based on the final chunk of disassembly provided (chunk 3/3), here is the updated and extended analysis of `dopuslib.dll`.

### Updated Analysis Summary

The addition of this final segment confirms the initial assessment: **`dopuslib.dll` is a professionally developed library using standard C++ compilation practices.** The code in this section is quintessential "boilerplate" generated by the C++ Standard Template Library (STL) to handle dynamic memory management for containers like `std::vector`.

---

### 1. Core Functionality & Infrastructure
The analysis of the previous chunks remains consistent regarding its purpose:
*   **Hardware-Aware Visualization:** The use of `SETUPAPI` and complex trigonometric calculations (`DrawConcentricRings`) continues to indicate a tool designed to process hardware data for graphical display.
*   **Robust Data Handling:** The library is built to handle varying amounts of data, requiring dynamic memory resizing (as seen in the new disassembly).

### 2. Technical Observations & Patterns
The latest disassembly provides high-confidence evidence regarding the development environment:

*   **Explicit STL Signature:** The presence of `fcn.391eab120("vector::_M_default_append")` is a "smoking gun" for standard C++ compilation. This isn't just any function; it is an internal name used by the GCC/libstdc++ libraries. It confirms that the developers used high-level languages and standard libraries rather than writing raw, low-level assembly or manually managed memory buffers often seen in custom malware.
*   **Standardized Memory Management:** The functions provided (`fcn.391eaed10` and its preceding sibling) are implementation details for **dynamic array resizing**. 
    *   The code checks if the current buffer is large enough to hold new data (`uVar6 <= uVar4`).
    *   If not, it calculates a new required size, allocates a larger block of memory using `operator_new`, copies the old data into the new space via a loop, and deletes the old buffer.
*   **Predictable Logic:** The logic is highly repetitive. These functions are virtually identical to one another in their logic flow (calculating offsets, checking bounds, reallocating). This level of consistency is typical of auto-generated compiler code for template classes.

### 3. Security Analysis Updates
*   **No Malicious "Tells":** While these functions involve memory allocation and copying—actions that *could* be abused in an exploit (like a buffer overflow)—the way they are implemented here is standard and safe. There is no evidence of manual pointer arithmetic intended to bypass security boundaries or hide malicious payloads.
*   **Lack of Obfuscation:** The names used within the code (even if prefixed by `fcn.`) clearly correspond to standard library operations. Malicious actors typically attempt to strip these references or rename them to make the logic harder to follow. The "honesty" of this code suggests a professional engineering tool.
*   **Resource Management:** The use of `operator_new` and `operator_delete` within the context of vector growth shows that the library is designed for stability and longevity, ensuring that memory leaks are minimized during heavy data processing.

---

### Updated Conclusion
The analysis remains unchanged: **The library is highly likely to be benign.**

The final chunk provides definitive proof of the development stack: it is a C++ application utilizing standard libraries to handle complex data structures. The complexity found in the disassembly is not "malicious complexity" (obfuscation), but rather "**architectural complexity**"—the necessary overhead of using modern, high-level programming languages to create stable software.

The module serves as a backend for an application that interacts with hardware and provides sophisticated visual feedback. It does not exhibit any characteristics of malware, trojans, or unauthorized system modification tools.

**Final Verdict: Benign / Functional.**

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have reviewed the provided behavioral analysis of `dopuslib.dll`. The analysis concludes that the library is **benign** and serves as a professional tool for hardware interaction and visualization. 

Because the file is determined to be benign, it does not exhibit malicious maneuvers; however, the technical capabilities observed (specifically how the code interacts with system resources) can be mapped to the MITRE ATT&CK framework as follows:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1400** | **Resource Development** | The use of `SETUPAPI` and trigonometry for hardware-aware visualization indicates interaction with system resources/hardware components. |
| **N/A** | **None (Lack of Obfuscation)** | The clear usage of Standard Template Library (STL) structures (`std::vector`) and standard naming conventions confirms a lack of "Defense Evasion" techniques (e.g., T1027, T1036). |

### Analyst Note:
While the code utilizes functions like `operator_new` and `operator_delete`, these are identified as legitimate memory management for dynamic arrays and do not constitute evidence of **Exploitation Techniques** or **Defense Evasion**, as they lack the non-standard logic typically associated with malicious buffer manipulation.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: While `dopuslib.dll` is mentioned in the text, it is identified as a standard library file and does not constitute a specific malicious path or registry key.)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Compiler/Tooling Signatures:** The strings confirm the use of the **GCC (Rev11, Built by MSYS2 project) 15.2.0** compiler and standard C++ libraries (libstdc++). These are characteristic of a development environment rather than malicious indicators.
*   **Internal Function Offsets:** References to `fcn.391eab120` and `fcn.391eaed10` appear to be internal memory addresses or symbols from the analysis tool, not external C2 patterns or network artifacts.

---
**Analyst Note:** 
The provided text contains no actionable IOCs. The "Extracted Strings" consist of standard compiler error messages (e.g., `basic_string`, `vector::_M_realloc_append`), standard Windows system messages, and high-entropy/obfuscated data that does not resolve to identifiable malicious infrastructure. The Behavioral Analysis concludes that the file is a **benign** professional library using standard C++ implementation practices.

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1. **Malware family**: None (Benign)
2. **Malware type**: N/A
3. **Confidence**: High
4. **Key evidence**:
    *   **Explicit Benign Determination:** The behavioral analysis explicitly concludes that `dopuslib.dll` is a "professionally developed" and "benign" library designed for hardware interaction and visualization, rather than a malicious tool.
    *   **Standard Development Practices:** The presence of standard C++ STL signatures (e.g., `std::vector`) and the absence of obfuscation indicate professional software engineering rather than malicious coding techniques.
    *   **Lack of Malicious Indicators:** No indicators of compromise (IOCs), such as hardcoded C2 domains, malicious IP addresses, or evasion tactics, were identified during the analysis.
