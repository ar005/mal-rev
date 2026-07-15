# Threat Analysis Report

**Generated:** 2026-07-13 19:26 UTC
**Sample:** `055bdf30252b8b644c9c97caa5182f51acd7844be4fd4174361b5557a25c64a8_055bdf30252b8b644c9c97caa5182f51acd7844be4fd4174361b5557a25c64a8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `055bdf30252b8b644c9c97caa5182f51acd7844be4fd4174361b5557a25c64a8_055bdf30252b8b644c9c97caa5182f51acd7844be4fd4174361b5557a25c64a8.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 7 sections |
| Size | 4,143,616 bytes |
| MD5 | `eeaff0a4aa941b94435092263ea3d525` |
| SHA1 | `350f00759b4d4f45d1a3d76d7947161d2dc1af15` |
| SHA256 | `055bdf30252b8b644c9c97caa5182f51acd7844be4fd4174361b5557a25c64a8` |
| Overall entropy | 6.008 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1761271860 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,104,384 | 6.602 | No |
| `.rdata` | 2,964,480 | 5.001 | No |
| `.data` | 6,144 | 3.188 | No |
| `.pdata` | 64,512 | 6.015 | No |
| `_RDATA` | 512 | 3.328 | No |
| `.rsrc` | 512 | 2.875 | No |
| `.reloc` | 2,048 | 4.801 | No |

### Imports

**ADVAPI32.dll**: `DeregisterEventSource`, `RegCloseKey`, `RegCreateKeyExW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryValueExW`, `RegSetValueExW`, `RegisterEventSourceW`, `ReportEventW`, `OpenProcessToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`
**bcrypt.dll**: `BCryptOpenAlgorithmProvider`, `BCryptFinishHash`, `BCryptDestroyHash`, `BCryptGenRandom`, `BCryptCreateHash`, `BCryptHashData`, `BCryptGetProperty`, `BCryptCloseAlgorithmProvider`
**KERNEL32.dll**: `TlsFree`, `TlsSetValue`, `TlsGetValue`, `TlsAlloc`, `InitializeCriticalSectionAndSpinCount`, `EncodePointer`, `RaiseException`, `RtlPcToFileHeader`, `InterlockedFlushSList`, `CancelThreadpoolIo`, `CloseHandle`, `CloseThreadpoolIo`, `CreateEventExW`, `CreateFileW`, `CreateProcessA`
**ole32.dll**: `CoCreateGuid`, `CoGetApartmentType`, `CoInitializeEx`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoUninitialize`, `CoWaitForMultipleHandles`
**USER32.dll**: `LoadStringW`
**api-ms-win-crt-math-l1-1-0.dll**: `ceil`, `modf`
**api-ms-win-crt-heap-l1-1-0.dll**: `malloc`, `calloc`, `free`, `_callnewh`
**api-ms-win-crt-string-l1-1-0.dll**: `strcpy_s`, `_stricmp`, `wcsncmp`, `strcmp`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_crt_atexit`, `_cexit`, `_seh_filter_dll`, `_configure_narrow_argv`, `terminate`, `abort`, `_initterm_e`, `_initialize_narrow_environment`, `_execute_onexit_table`, `_register_onexit_function`, `_initialize_onexit_table`, `_initterm`

### Exports

`0or4dvfZSvJ83SZ7Rv`, `0ztE8pnryXDn`, `1E8YGtCSV9y2Fmxgc2evPaww`, `1EkeuVX7G`, `1ImRmXAikdZ5Mdstx2OZJ`, `1RLfWYzHw25OTnX7iNIPhWEjGBA`, `1TcXblU4rUfcV`, `2QpDlZNsQImXspx`, `2RiMstXT7l51n3JWqefuIPWxSaW`, `2aJW35yJ82daB5fq8cCPohLc6xLiw20`, `36J0Qgc`, `3I09DevKT6T`, `3cXmRjK5hnOdRHAUYBPc`, `3fvV3hdoPg`, `3genvczw705nq9mMD4TMzccVySE`, `3lhAEcyZmoBHJJ`, `40s4JX9Y75zix`, `4FGFAydpwPO`, `4RfQrpM0kz3DHZ0BhPI142IHCw`, `4potzMuYSvuKAdQPl9iJNaElffK`, `4zlDqTUswa6MGucmA6A`, `5jw5fbA8DWQbakWGyzj5`, `5tKCqp4mgS`, `6jZ9HG6psZdXYzAvT9vWaHyUG8n0I7`, `6xVXPiA4`, `7BOWC7fviRAqFxq`, `7VfLPUAtbl75R`, `7kjcaDw84cl0H`, `8NpcYmun7kho4hNuhyGFcWeoRMMX`, `8Sy8qmGcHwGneErKs6SDFSSIg`, `8hShviSllyFCMGvbdbLngCeMFKPAx30U`, `8xj98tc`, `93TqPDw6dkgssbiy6WXnkB8`, `9A8jrM3fSE6wO1Pyhpu9n`, `9FMkq5UZoZX`, `9NuL7NlmlFKqTzWovyatQda7DABOp`, `9SRgyqJ`, `9nFhwFSc8wJ0B8w6XYHwH2`, `ABtzVIMrOTLCLhrskG9aj`, `ASgAONpOzTQvslKTjfvNIsvYGLwUXG`, `B8s3AmUVuKaGbuz2VtOc`, `BXtfYuMW6hC3omYAr5qSCXaPHl6EZ`, `Ci5Dt82j1ls2zvERNQxwQF81XDP`, `CoJ3LvDh18a3`, `CrashForExceptionInNonABICompliantCodeRange`, `D01uEJ0URW05`, `D4uVuLy90mRwwHFzQb18eEM9yzfvgVH`, `EFia9X2JtMUW`, `EoYfr9s17pz2RuVhu`, `F0Y3keUS8SRd5MI8NZyDuk1P9G0frDok`

## Extracted Strings

Total strings found: **8977** (showing first 100)

```
!This program cannot be run in DOS mode.
$
Hq
WHtr
`.rdata
@.data
.pdata
@_RDATA
@.rsrc
@.reloc
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVWVSH
x[^_A^A_]
UAWAVWVSH
H[^_A^A_]
UAWAVWVSH
H[^_A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAVWVSH
[^_A^]
UAVWVSH
0[^_A^]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
([^_A\A]A^A_]
UAWAVAUATWVSH
([^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
8[^_A\A]A^A_]
UAWAVAUATWVSH
8[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
([^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
8[^_A\A]A^A_]
UAWAVAUATWVSH
8[^_A\A]A^A_]
UAVWVSH
[^_A^]
[^_A^]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAVWVSH
[^_A^]
AWAVWVUSH
L$H;L$X
[]^_A^A_
[]^_A^A_
[]^_A^A_
[]^_A^A_
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
([^_A\A]A^A_]
UAWAVAUWVSH
 [^_A]A^A_]
AWAVAUATWVUSH
([]^_A\A]A^A_
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180019920` | `0x180019920` | 979603 | ✓ |
| `fcn.1800197f0` | `0x1800197f0` | 587892 | ✓ |
| `fcn.180020ff0` | `0x180020ff0` | 584897 | ✓ |
| `fcn.180019be0` | `0x180019be0` | 584833 | ✓ |
| `fcn.180019dc0` | `0x180019dc0` | 584289 | ✓ |
| `fcn.180019ec0` | `0x180019ec0` | 583985 | ✓ |
| `fcn.180019f80` | `0x180019f80` | 583809 | ✓ |
| `fcn.18001a060` | `0x18001a060` | 583561 | ✓ |
| `fcn.18001a340` | `0x18001a340` | 583129 | ✓ |
| `fcn.18001a400` | `0x18001a400` | 582665 | ✓ |
| `fcn.1800a8598` | `0x1800a8598` | 560907 | ✓ |
| `fcn.1800a8418` | `0x1800a8418` | 560692 | ✓ |
| `fcn.18003eb30` | `0x18003eb30` | 441320 | ✓ |
| `fcn.180041c50` | `0x180041c50` | 421465 | ✓ |
| `fcn.180093060` | `0x180093060` | 416208 | ✓ |
| `fcn.180045cb0` | `0x180045cb0` | 404233 | ✓ |
| `fcn.1800aa770` | `0x1800aa770` | 373369 | ✓ |
| `fcn.1800377a0` | `0x1800377a0` | 345218 | ✓ |
| `fcn.1800b4fc0` | `0x1800b4fc0` | 342405 | ✓ |
| `fcn.1800a8b85` | `0x1800a8b85` | 337913 | ✓ |
| `fcn.1800b8520` | `0x1800b8520` | 329309 | ✓ |
| `fcn.1800ed5f0` | `0x1800ed5f0` | 232677 | ✓ |
| `fcn.1800ed620` | `0x1800ed620` | 223589 | ✓ |
| `fcn.1800ed630` | `0x1800ed630` | 222166 | ✓ |
| `fcn.1800ed430` | `0x1800ed430` | 221185 | ✓ |
| `fcn.1800ed600` | `0x1800ed600` | 220698 | ✓ |
| `fcn.1800ed6a0` | `0x1800ed6a0` | 218725 | ✓ |
| `fcn.18009e420` | `0x18009e420` | 127331 | ✓ |
| `fcn.1800a6b30` | `0x1800a6b30` | 115225 | ✓ |
| `fcn.1800616e0` | `0x1800616e0` | 114046 | ✓ |

### Decompiled Code Files

- [`code/fcn.1800197f0.c`](code/fcn.1800197f0.c)
- [`code/fcn.180019920.c`](code/fcn.180019920.c)
- [`code/fcn.180019be0.c`](code/fcn.180019be0.c)
- [`code/fcn.180019dc0.c`](code/fcn.180019dc0.c)
- [`code/fcn.180019ec0.c`](code/fcn.180019ec0.c)
- [`code/fcn.180019f80.c`](code/fcn.180019f80.c)
- [`code/fcn.18001a060.c`](code/fcn.18001a060.c)
- [`code/fcn.18001a340.c`](code/fcn.18001a340.c)
- [`code/fcn.18001a400.c`](code/fcn.18001a400.c)
- [`code/fcn.180020ff0.c`](code/fcn.180020ff0.c)
- [`code/fcn.1800377a0.c`](code/fcn.1800377a0.c)
- [`code/fcn.18003eb30.c`](code/fcn.18003eb30.c)
- [`code/fcn.180041c50.c`](code/fcn.180041c50.c)
- [`code/fcn.180045cb0.c`](code/fcn.180045cb0.c)
- [`code/fcn.1800616e0.c`](code/fcn.1800616e0.c)
- [`code/fcn.180093060.c`](code/fcn.180093060.c)
- [`code/fcn.18009e420.c`](code/fcn.18009e420.c)
- [`code/fcn.1800a6b30.c`](code/fcn.1800a6b30.c)
- [`code/fcn.1800a8418.c`](code/fcn.1800a8418.c)
- [`code/fcn.1800a8598.c`](code/fcn.1800a8598.c)
- [`code/fcn.1800a8b85.c`](code/fcn.1800a8b85.c)
- [`code/fcn.1800aa770.c`](code/fcn.1800aa770.c)
- [`code/fcn.1800b4fc0.c`](code/fcn.1800b4fc0.c)
- [`code/fcn.1800b8520.c`](code/fcn.1800b8520.c)
- [`code/fcn.1800ed430.c`](code/fcn.1800ed430.c)
- [`code/fcn.1800ed5f0.c`](code/fcn.1800ed5f0.c)
- [`code/fcn.1800ed600.c`](code/fcn.1800ed600.c)
- [`code/fcn.1800ed620.c`](code/fcn.1800ed620.c)
- [`code/fcn.1800ed630.c`](code/fcn.1800ed630.c)
- [`code/fcn.1800ed6a0.c`](code/fcn.1800ed6a0.c)

## Behavioral Analysis

Based on the provided disassembly and string data, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The code appears to be part of a **highly obfuscated packer or loader** that utilizes **Virtual Machine (VM)-based protection**. 

Instead of straightforward execution, the code functions as a "dispatcher" for a custom bytecode interpreter. The presence of numerous similar-looking functions (`fcn.180019dc0`, `fcn.180019ec0`, etc.) that perform complex checks before jumping to internal handlers is a hallmark of VM protection (such as VMProtect or Themida). Its primary role is likely to decrypt and decompress a hidden "payload" in memory while making the analysis of that payload significantly harder for researchers.

### Suspicious/Malicious Behaviors
While these specific functions do not show direct high-level actions like "sending an email" or "encrypting files," they exhibit several behaviors typical of advanced malware:

*   **Virtual Machine (VM) Obfuscation:** The heavy use of indirect jumps (`(**0x1803e9b00 + 0xb0)`) and nested pointer dereferencing indicates that the actual logic is hidden behind a custom instruction set.
*   **Control Flow Flattening / Complexity:** Many functions (like `fcn.180019ec0`) use complex bitmask checks (`& 0x30000`) to determine the next jump or operation, designed to confuse automated analysis tools and human analysts.
*   **Encryption/Unpacking Evidence:** The "garbled" string list suggests heavily encrypted or compressed resources. These strings are likely not intended for use as-is but are part of an obfuscated data segment.
*   **Manual Memory Manipulation:** Function `fcn.180093060` performs manual loop-based pointer arithmetic and "shuffling" of memory, which is commonly used in custom decryption routines to unpack the final stage of a multi-stage loader.
*   **Concurrency Control:** The use of the `LOCK` instruction (found in `fcn.180041c50`) suggests the malware may be multi-threaded or uses atomic operations to synchronize threads during the unpacking process.

### Notable Techniques and Patterns
*   **Instruction Handler Pattern:** Many functions follow a pattern: Check internal flags $\rightarrow$ Verify memory integrity $\rightarrow$ Jump to an offset. This indicates a "handler" architecture where the code is essentially running its own mini-operating system to hide its true intent.
*   **Indirect Branching:** The frequent use of `swi(3)` (software interrupts) or calls into offsets calculated at runtime is used to break the visibility of the execution path in disassemblers like IDA Pro.
*   **State Management:** Functions like `fcn.1800a8598` and `fcn.1800a8418` are updating specific offsets (e.g., `0x1800913c0`). This is typical of a "Context" structure in VM-protected code, where the internal state of the virtual machine is updated after every "instruction."
*   **Anti-Analysis through Complexity:** The sheer amount of boilerplate logic required to perform simple tasks (like the math/ceiling call at the start) suggests the author prioritized making the code difficult to reverse-engineer over performance.

### Summary
This is likely a **stub for a multi-stage malware loader**. It uses advanced VM-based protection techniques to hide its true purpose. The presence of this much sophisticated obfuscation usually points toward high-end malware (such as a Trojan, Ransomware, or Spyware) where the actual malicious payload is only "unpacked" in memory after passing several layers of integrity and anti-debugging checks.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | **Obfuscated Files or Information** | The use of VM-based protection, control flow flattening, and "garbled" (encrypted) strings are classic methods to hide code logic and evade automated analysis. |

### Analyst Notes:
While all observed behaviors fall under the primary technique of **T1027**, they represent several specific sub-behaviors typical of advanced malware loaders:
*   **VM-based Protection:** The use of a custom bytecode interpreter (dispatcher) to hide execution logic is a high-complexity form of obfuscation.
*   **Control Flow Flattening:** The "complex bitmask checks" and indirect jumps are designed specifically to defeat static analysis tools (like IDA Pro).
*   **Multi-stage Loading:** The use of manual memory manipulation for decryption/decompression indicates the binary is a packer or loader intended to hide a final malicious payload in memory.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** The "Extracted Strings" section contains highly obfuscated data and standard PE header symbols. No actionable network indicators or clear-text file paths were present in that specific segment.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified (Standard system strings like `.rdata` and `.pdata` were excluded as false positives).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Behavioral Signature:** VM-based protection (likely a packer/loader utilizing techniques similar to VMProtect or Themida).
*   **Technical Indicators (Internal Offsets):** The following memory offsets were identified in the disassembly, which can be used for behavioral signature matching:
    *   `0x1800913c0` (Context structure update)
    *   `fcn.180019dc0`
    *   `fcn.180019ec0`
    *   `fcn.180093060`
    *   `fcn.180041c50`
    *   `fcn.1800a8598`
    *   `fcn.1800a8418`
*   **Techniques Observed:** 
    *   Control Flow Flattening
    *   Manual Memory Manipulation/Shuffling (indicative of a multi-stage loader)
    *   Instruction Handler Pattern (VM-based protection)
    *   Use of `LOCK` instructions for synchronization during decryption.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High

4. **Key evidence**:
*   **VM-Based Protection:** The analysis identifies a custom bytecode interpreter and a "dispatcher" architecture with complex bitmask checks, which are signature behaviors of advanced packers (like VMProtect or Themida) used to hide the actual payload.
*   **Multi-Stage Loading Indicators:** The presence of manual memory manipulation ("shuffling"), lack of immediate high-level malicious actions (like C2 communication or encryption), and heavy use of control flow flattening strongly indicate a "stub" designed to unpack/decrypt a secondary stage.
*   **Obfuscation as Primary Function:** The primary complexity of the code is dedicated to hiding execution logic through indirect jumps and instruction handler patterns, a hallmark of high-sophistication loaders used in advanced persistent threats (APTs) or large-scale malware campaigns.
