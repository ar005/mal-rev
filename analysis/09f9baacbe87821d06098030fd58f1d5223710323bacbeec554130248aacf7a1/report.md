# Threat Analysis Report

**Generated:** 2026-07-24 12:57 UTC
**Sample:** `09f9baacbe87821d06098030fd58f1d5223710323bacbeec554130248aacf7a1_09f9baacbe87821d06098030fd58f1d5223710323bacbeec554130248aacf7a1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `09f9baacbe87821d06098030fd58f1d5223710323bacbeec554130248aacf7a1_09f9baacbe87821d06098030fd58f1d5223710323bacbeec554130248aacf7a1.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 8 sections |
| Size | 434,176 bytes |
| MD5 | `6f26c2a3ce76e080fabf6b4201774e8c` |
| SHA1 | `54d1327d42cfbf0fade7b67a9345e4eedd1dbac0` |
| SHA256 | `09f9baacbe87821d06098030fd58f1d5223710323bacbeec554130248aacf7a1` |
| Overall entropy | 7.69 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1581610835 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 78,336 | 6.425 | No |
| `.rdata` | 26,624 | 4.814 | No |
| `.data` | 3,072 | 3.196 | No |
| `.rsrc` | 512 | 4.71 | No |
| `.reloc` | 5,120 | 6.291 | No |
| `.tls` | 288,256 | 7.998 | ⚠️ Yes |
| `lktbwr` | 4,096 | 4.587 | No |
| `dat` | 27,136 | 6.201 | No |

### Imports

**KERNEL32.dll**: `VirtualFree`, `VirtualAlloc`, `VirtualQuery`, `HeapCreate`, `VirtualProtect`, `HeapFree`, `GetCurrentProcess`, `Thread32Next`, `Thread32First`, `GetCurrentThreadId`, `SuspendThread`, `ResumeThread`, `CreateToolhelp32Snapshot`, `Sleep`, `HeapReAlloc`
**USER32.dll**: `MessageBoxA`
**OLEAUT32.dll**: `VariantCopy`, `SafeArrayDestroy`, `VariantInit`, `SafeArrayGetUBound`, `SafeArrayGetLBound`, `SysFreeString`, `SafeArrayPutElement`, `SafeArrayUnaccessData`, `SafeArrayCreate`, `SafeArrayAccessData`, `VariantClear`
**SHLWAPI.dll**: `PathFindFileNameW`
**mscoree.dll**: `CLRCreateInstance`

## Extracted Strings

Total strings found: **1036** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.reloc
@lktbwr
;Ut3j
M;Jr

Yt
jV
QQSVWd
38_^]
E9xt
&9Gv!8E
9Ov:k
URPQQh
kUQPXY]Y[
< t4<	t0
9>tWV
tf;1u
u9~uj
};GvP
u9^uj
};GvP
</t
<\t
u9^u
uSSSSj
};GvP
];3t'
f9:t!V
u|9]t,9
QQSVj8j@
;ut.;
PPPPPPPP
PPPPPWV
PP9E u

u<jXSf

u	jZf
PVVVVV
t;Et
\9EuY
D$+d$SVW
D$+d$SVW
bad allocation
bad exception
__based(
__cdecl
__pascal
__stdcall
__thiscall
__fastcall
__vectorcall
__clrcall
__eabi
__swift_1
__swift_2
__ptr64
__restrict
__unaligned
restrict(
 delete
operator
`vftable'
`vbtable'
`vcall'
`typeof'
`local static guard'
`string'
`vbase destructor'
`vector deleting destructor'
`default constructor closure'
`scalar deleting destructor'
`vector constructor iterator'
`vector destructor iterator'
`vector vbase constructor iterator'
`virtual displacement map'
`eh vector constructor iterator'
`eh vector destructor iterator'
`eh vector vbase constructor iterator'
`copy constructor closure'
`udt returning'
`local vftable'
`local vftable constructor closure'
 new[]
 delete[]
`omni callsig'
`placement delete closure'
`placement delete[] closure'
`managed vector constructor iterator'
`managed vector destructor iterator'
`eh vector copy constructor iterator'
`eh vector vbase copy constructor iterator'
`dynamic initializer for '
`dynamic atexit destructor for '
`vector copy constructor iterator'
`vector vbase copy constructor iterator'
`managed vector copy constructor iterator'
`local static thread guard'
operator "" 
operator co_await
operator<=>
 Type Descriptor'
 Base Class Descriptor at (
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.008b1848` | `0x8b1848` | 4301 | ✓ |
| `fcn.0090af10` | `0x90af10` | 3126 | ✓ |
| `fcn.008a1220` | `0x8a1220` | 2575 | ✓ |
| `fcn.008a3440` | `0x8a3440` | 2534 | ✓ |
| `fcn.008a9760` | `0x8a9760` | 1396 | ✓ |
| `fcn.008af5f0` | `0x8af5f0` | 1262 | ✓ |
| `fcn.008a2aa0` | `0x8a2aa0` | 1074 | ✓ |
| `fcn.008a6c3e` | `0x8a6c3e` | 1064 | ✓ |
| `fcn.0090ab10` | `0x90ab10` | 1018 | ✓ |
| `fcn.008b02d7` | `0x8b02d7` | 962 | ✓ |
| `fcn.008a87bb` | `0x8a87bb` | 938 | ✓ |
| `fcn.0090bb50` | `0x90bb50` | 822 | ✓ |
| `fcn.00909a60` | `0x909a60` | 801 | ✓ |
| `fcn.00909d90` | `0x909d90` | 799 | ✓ |
| `fcn.0090cae0` | `0x90cae0` | 774 | ✓ |
| `fcn.008af033` | `0x8af033` | 769 | ✓ |
| `fcn.0090eb70` | `0x90eb70` | 763 | ✓ |
| `fcn.0090e2e0` | `0x90e2e0` | 696 | ✓ |
| `fcn.008b12e3` | `0x8b12e3` | 671 | ✓ |
| `fcn.008ac17b` | `0x8ac17b` | 645 | ✓ |
| `fcn.008b308e` | `0x8b308e` | 640 | ✓ |
| `fcn.0090df10` | `0x90df10` | 622 | ✓ |
| `fcn.008b215e` | `0x8b215e` | 614 | ✓ |
| `fcn.008ad348` | `0x8ad348` | 608 | ✓ |
| `fcn.0090c030` | `0x90c030` | 606 | ✓ |
| `fcn.0090e640` | `0x90e640` | 598 | ✓ |
| `fcn.0090d600` | `0x90d600` | 581 | ✓ |
| `fcn.008b252d` | `0x8b252d` | 576 | ✓ |
| `fcn.008b3331` | `0x8b3331` | 563 | ✓ |
| `fcn.0090d260` | `0x90d260` | 558 | ✓ |

### Decompiled Code Files

- [`code/fcn.008a1220.c`](code/fcn.008a1220.c)
- [`code/fcn.008a2aa0.c`](code/fcn.008a2aa0.c)
- [`code/fcn.008a3440.c`](code/fcn.008a3440.c)
- [`code/fcn.008a6c3e.c`](code/fcn.008a6c3e.c)
- [`code/fcn.008a87bb.c`](code/fcn.008a87bb.c)
- [`code/fcn.008a9760.c`](code/fcn.008a9760.c)
- [`code/fcn.008ac17b.c`](code/fcn.008ac17b.c)
- [`code/fcn.008ad348.c`](code/fcn.008ad348.c)
- [`code/fcn.008af033.c`](code/fcn.008af033.c)
- [`code/fcn.008af5f0.c`](code/fcn.008af5f0.c)
- [`code/fcn.008b02d7.c`](code/fcn.008b02d7.c)
- [`code/fcn.008b12e3.c`](code/fcn.008b12e3.c)
- [`code/fcn.008b1848.c`](code/fcn.008b1848.c)
- [`code/fcn.008b215e.c`](code/fcn.008b215e.c)
- [`code/fcn.008b252d.c`](code/fcn.008b252d.c)
- [`code/fcn.008b308e.c`](code/fcn.008b308e.c)
- [`code/fcn.008b3331.c`](code/fcn.008b3331.c)
- [`code/fcn.00909a60.c`](code/fcn.00909a60.c)
- [`code/fcn.00909d90.c`](code/fcn.00909d90.c)
- [`code/fcn.0090ab10.c`](code/fcn.0090ab10.c)
- [`code/fcn.0090af10.c`](code/fcn.0090af10.c)
- [`code/fcn.0090bb50.c`](code/fcn.0090bb50.c)
- [`code/fcn.0090c030.c`](code/fcn.0090c030.c)
- [`code/fcn.0090cae0.c`](code/fcn.0090cae0.c)
- [`code/fcn.0090d260.c`](code/fcn.0090d260.c)
- [`code/fcn.0090d600.c`](code/fcn.0090d600.c)
- [`code/fcn.0090df10.c`](code/fcn.0090df10.c)
- [`code/fcn.0090e2e0.c`](code/fcn.0090e2e0.c)
- [`code/fcn.0090e640.c`](code/fcn.0090e640.c)
- [`code/fcn.0090eb70.c`](code/fcn.0090eb70.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, I have updated and expanded the analysis. The new code confirms that this binary is not a simple packer; it is a **highly sophisticated loader** featuring advanced environmental checks, multi-stage payload processing, and specialized mathematical routines for decryption.

### Updated Analysis of Capability & Intent

#### 1. Advanced Payload Parsing (Instruction Decoding)
The functions `fcn.0090df10` and `fcn.0090d600` indicate that the binary doesn't just "decrypt" a block of data; it **interprets** it.
*   **Custom Instruction Set:** `fcn.0090df10` contains logic that iterates through memory, checking values against constants (e.g., `>> 0xc == 10`, `== 1`). This is characteristic of a **custom virtual machine (VM) or an instruction dispatcher**. It suggests the payload is "wrapped" in a layer of custom code that the loader must interpret to execute.
*   **Memory Allocation & Mapping:** `fcn.0090d600` involves complex calculations for memory offsets and sizes (e.g., `0x1000`, which is the standard Windows page size). This is used to map different "stages" of the payload into executable memory.

#### 2. File System Discovery & Manipulation
The function `fcn.008ac17b` reveals that the loader actively interacts with the file system in a way that suggests **multi-stage staging**:
*   **Path Normalization:** It contains logic to identify and handle different directory separators (`/`, `\`). 
*   **Automated File Searching:** It utilizes `FindFirstFileExW` and `FindNextFileW` to scan for files. This is often used by malware to locate "sibling" configuration files, hidden payload components, or even to check for the presence of specific security software before proceeding with the final stage.

#### 3. Complex Mathematical/Encryption Routines
The functions `fcn.008b308e` and `fcn.008b215e` contain heavy floating-point math, bitwise manipulations, and even **SIMD-related logic** (indicated by the use of XMM register logic structures).
*   **Non-Standard Cryptography:** While high-level encryption usually uses standard libraries, these routines look like custom, highly-optimized mathematical algorithms. In malware, this is frequently used to derive decryption keys from system environment variables or to perform "heavy" de-obfuscation of the primary payload's core logic.
*   **Anti-Analysis via Complexity:** These functions are intentionally dense and mathematically complex to deter human analysts from reverse-engineering the actual decryption key or algorithm through simple observation.

#### 4. Deep .NET Runtime Interaction
The repeated use of indirect calls (e.g., `(**(*arg_8h + 0x38))(...)`) and "table" lookups suggests the loader is performing **Manual JIT/CLR interaction**. It is navigating internal structures of the .NET runtime to resolve methods and call them directly, bypassing standard high-level APIs that are often monitored by EDR (Endpoint Detection and Response) systems.

---

### Updated Summary of Malicious Indicators

| Indicator | Technical Observation | Threat Context |
| :--- | :--- | :--- |
| **Multi-Stage Staging** | Use of `FindFirstFileExW` and internal buffer management for different "stages." | The loader fetches multiple components from the disk/memory to complete its execution. |
| **Instruction Decoding** | Loops with opcode-style checks (e.g., `>> 0xc == 10`). | Suggests a custom VM or packer that hides the primary payload's true logic. |
| **Advanced Math/SIMD** | Complex floating-point math and XMM-related operations in `fcn.008b308e`. | Likely used for sophisticated, non-standard decryption of core components. |
| **Reflective Loading** | Interaction with `.NET` internals to resolve and call functions manually. | Designed to bypass security hooks that monitor standard API calls (like `GetProcAddress`). |
| **Anti-Analysis Tactics** | Inclusion of `swi(3)` (breakpoints) and heavy "junk" logic/mathematical complexity. | Intentionally designed to break automated sandboxes and frustrate human researchers. |

### Refined Intelligence for Incident Response
This is a high-capability **downloader/loader** typical of advanced persistent threat (APT) groups or sophisticated cybercriminal operations. 

*   **Behavioral Warning:** If this binary is executed, it will likely perform several "silent" actions: searching the local disk for other files, decompressing several layers of code in memory using complex math, and finally starting a .NET-based "worker" process or thread.
*   **Detection Strategy:** Because much of its logic happens in-memory (via reflective loading) and uses custom instruction sets, **signature-based detection will likely fail.** Defenders should look for:
    1.  Processes making frequent calls to `VirtualAlloc` or `VirtualProtect` with `PAGE_EXECUTE_READWRITE` permissions.
    2.  The presence of high-entropy (encrypted) data blocks within the process's memory space.
    3.  Detection of "orphan" threads running in regions of memory not associated with a loaded module.

**Conclusion:** This binary is highly dangerous and indicative of an advanced stage of an intrusion. It is designed to provide a stable, hidden environment for a secondary payload (such as a RAT, info-stealer, or ransomware) to execute.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization | The use of a custom instruction set and a "virtual machine" dispatcher (`fcn.0090df10`) to interpret payload logic is a clear indicator of code virtualization. |
| **T1055** | Packing | The loader uses complex memory mapping, page size calculations, and multi-stage processing to hide the true nature of the primary payload. |
| **T1083** | File and Directory Discovery | The use of `FindFirstFileExW` and `FindNextFileW` to find sibling files or configuration components demonstrates active file system discovery. |
| **T1562** | Data Encoding | The heavy use of non-standard mathematical algorithms, bitwise manipulations, and SIMD logic is used to encode/decrypt payload data into a usable state. |
| **T1620** | Reflective Code Loading | The loader bypasses standard APIs (like `GetProcAddress`) by navigating .NET internal structures to load and execute code directly in memory. |
| **T1416** | System Host Signal Detection | The inclusion of `swi(3)` instructions is a specific anti-debugging technique used to detect breakpoints or interrupt the execution flow during analysis. |
| **T1027** | Obfuscated Files or system information | The high level of mathematical complexity and "junk" logic are specifically designed to frustrate human analysts and automated tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: While `FindFirstFileExW` is used for file searching, no specific malicious paths were disclosed in the provided text).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Internal Function Offsets (Potentially indicative of a specific packer/loader):**
    *   `fcn.0090df10` (Instruction decoding/VM logic)
    *   `fcn.0090d600` (Memory mapping/Stage processing)
    *   `fcn.008ac17b` (File system interaction/staging)
    *   `fcn.008b308e` (Complex math/SIMD-based decryption)
    *   `fcn.008b215e` (Complexity/Decryption routine)
*   **Behavioral Patterns / Techniques:**
    *   **Custom Instruction Decoding:** Usage of loops with opcode-style checks (e.g., `>> 0xc == 10`).
    *   **Manual .NET JIT/CLR Interaction:** Bypassing standard APIs to resolve and call .NET functions directly to evade EDR.
    *   **Memory Manipulation:** Frequent use of `VirtualAlloc` and `VirtualProtect` to create `PAGE_EXECUTE_READWRITE` (RWX) memory regions.
    *   **Multi-Stage Staging:** Use of `FindFirstFileExW` and `FindNextFileW` to locate components for multi-stage loading.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Virtualization/VM:** The use of a custom instruction set and dispatcher (`fcn.0090df10`) indicates the loader is designed to wrap and protect high-value payloads using code virtualization (MITRE T1497).
    *   **Reflective Loading & Evasion:** The binary performs manual .NET JIT/CLR interaction and reflective loading to bypass standard API hooks, combined with complex SIMD math routines to evade detection during the de-obfuscation phase.
    *   **Multi-Stage Staging:** Evidence of automated file system discovery (`FindFirstFileExW`) and dynamic memory mapping confirms its role in fetching and preparing multiple stages for a final payload (e.g., RAT or info-stealer).
