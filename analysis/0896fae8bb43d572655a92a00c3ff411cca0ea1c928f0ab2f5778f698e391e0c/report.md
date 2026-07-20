# Threat Analysis Report

**Generated:** 2026-07-18 14:52 UTC
**Sample:** `0896fae8bb43d572655a92a00c3ff411cca0ea1c928f0ab2f5778f698e391e0c_0896fae8bb43d572655a92a00c3ff411cca0ea1c928f0ab2f5778f698e391e0c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0896fae8bb43d572655a92a00c3ff411cca0ea1c928f0ab2f5778f698e391e0c_0896fae8bb43d572655a92a00c3ff411cca0ea1c928f0ab2f5778f698e391e0c.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 2,141,696 bytes |
| MD5 | `8624de4818263016a4c33b767b38743d` |
| SHA1 | `70df531bf923e7859dd8c95541ece99bf972b1c3` |
| SHA256 | `0896fae8bb43d572655a92a00c3ff411cca0ea1c928f0ab2f5778f698e391e0c` |
| Overall entropy | 5.295 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1780071554 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 525,312 | 6.414 | No |
| `.rdata` | 141,312 | 5.834 | No |
| `.data` | 6,656 | 1.06 | No |
| `.pdata` | 22,528 | 5.901 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 1,438,208 | 3.971 | No |
| `.reloc` | 6,144 | 5.34 | No |

### Imports

**bcryptprimitives.dll**: `ProcessPrng`
**api-ms-win-core-synch-l1-2-0.dll**: `WaitOnAddress`, `WakeByAddressSingle`, `WakeByAddressAll`
**kernel32.dll**: `GetLastError`, `WaitForSingleObject`, `GetModuleHandleW`, `VirtualProtect`, `CloseHandle`, `WaitForMultipleObjects`, `GetOverlappedResult`, `FlushFileBuffers`, `GetFileInformationByHandleEx`, `GetExitCodeProcess`, `HeapSize`, `GetFileInformationByHandle`, `HeapFree`, `LCMapStringW`, `CreateWaitableTimerExW`
**ntdll.dll**: `NtWriteFile`, `NtOpenFile`, `RtlNtStatusToDosError`, `NtReadFile`, `NtCreateNamedPipeFile`
**ole32.dll**: `CoInitializeEx`, `CoCreateInstance`, `CoUninitialize`
**advapi32.dll**: `RegCloseKey`, `RegQueryValueExW`, `RegSetValueExW`, `RegCreateKeyExW`
**oleaut32.dll**: `GetErrorInfo`, `SysStringLen`, `SysAllocStringLen`, `SysFreeString`
**user32.dll**: `DispatchMessageW`, `GetMessageW`, `TranslateMessage`

## Extracted Strings

Total strings found: **2387** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
UAWAVAUATVWSH
h[_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWS
H9x t*H
L;h@s6H
H9x t*H
[_^A\A]A^A_]
UAWAVAUATVWSH
(D$pfD
oL$`fD
oT$PfD
[_^A\A]A^A_]
UAWAVAUATVWSH
(D$pfD
oL$`fD
oT$PfD
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
(D$pfD
oL$`fD
oT$PfD
[_^A\A]A^A_]
UAWAVAUATVWSH
(D$pfD
oL$`fD
oT$PfD
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
AVVWSH
H[_^A^
AWAVVWSH
 [_^A^A_
 [_^A^A_
AWAVAUATVWUSH
)D$`E1
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVATVWSH
([_^A\A^A_H
([_^A\A^A_
AWAVAUATVWUSH
UUUUUUUUM!
33333333M!
([]_^A\A]A^A_
AWAVAUATVWUSH
L3e(L1
L#L$(M1
H#L$(H
H!D$0L
L#l$`L
H#D$hL
L#D$ L3
p[]_^A\A]A^A_
AWAVAUATVWUSH
UUUUUUUUH!
33333333I!
[]_^A\A]A^A_
AVVWSH
([_^A^
AWAVAUATVWUSH
[]_^A\A]A^A_
UAWAVAUATVWSH
X[_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAVVWSH
 [_^A^]
UAVVWSH
P[_^A^]
UAVVWSH
0[_^A^]
UAVVWSH
 [_^A^]
UAVVWSH
 [_^A^]
UAVVWSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140047900` | `0x140047900` | 230940 | ✓ |
| `case.0x140041d36.256` | `0x1400536b0` | 182946 | ✓ |
| `fcn.140080550` | `0x140080550` | 160419 | ✓ |
| `fcn.140041c10` | `0x140041c10` | 86424 | ✓ |
| `fcn.14001656a` | `0x14001656a` | 44398 | ✓ |
| `fcn.1400214a6` | `0x1400214a6` | 18588 | ✓ |
| `fcn.14005c010` | `0x14005c010` | 18202 | ✓ |
| `fcn.140059d00` | `0x140059d00` | 17846 | ✓ |
| `fcn.14006d278` | `0x14006d278` | 17819 | ✓ |
| `fcn.14006d264` | `0x14006d264` | 17778 | ✓ |
| `fcn.140053150` | `0x140053150` | 16302 | ✓ |
| `case.0x14005322a.45` | `0x140053f80` | 13000 | ✓ |
| `fcn.140064650` | `0x140064650` | 12458 | ✓ |
| `fcn.140049cab` | `0x140049cab` | 9697 | ✓ |
| `fcn.140025d42` | `0x140025d42` | 8140 | ✓ |
| `fcn.14002baa1` | `0x14002baa1` | 5235 | ✓ |
| `fcn.140017ee2` | `0x140017ee2` | 4346 | ✓ |
| `fcn.140061b50` | `0x140061b50` | 4279 | ✓ |
| `fcn.140027d0e` | `0x140027d0e` | 4189 | ✓ |
| `fcn.140010605` | `0x140010605` | 4161 | ✓ |
| `fcn.140028efb` | `0x140028efb` | 4153 | ✓ |
| `fcn.14000ee4c` | `0x14000ee4c` | 3686 | ✓ |
| `fcn.14000ccad` | `0x14000ccad` | 3381 | ✓ |
| `fcn.140046a40` | `0x140046a40` | 3365 | ✓ |
| `fcn.14002cf14` | `0x14002cf14` | 3192 | ✓ |
| `fcn.140045560` | `0x140045560` | 2813 | ✓ |
| `fcn.14004a4ad` | `0x14004a4ad` | 2593 | ✓ |
| `fcn.14000bc8a` | `0x14000bc8a` | 2167 | ✓ |
| `fcn.14006ebf4` | `0x14006ebf4` | 1985 | ✓ |
| `fcn.1400199da` | `0x1400199da` | 1962 | ✓ |

### Decompiled Code Files

- [`code/case.0x140041d36.256.c`](code/case.0x140041d36.256.c)
- [`code/case.0x14005322a.45.c`](code/case.0x14005322a.45.c)
- [`code/fcn.14000bc8a.c`](code/fcn.14000bc8a.c)
- [`code/fcn.14000ccad.c`](code/fcn.14000ccad.c)
- [`code/fcn.14000ee4c.c`](code/fcn.14000ee4c.c)
- [`code/fcn.140010605.c`](code/fcn.140010605.c)
- [`code/fcn.14001656a.c`](code/fcn.14001656a.c)
- [`code/fcn.140017ee2.c`](code/fcn.140017ee2.c)
- [`code/fcn.1400199da.c`](code/fcn.1400199da.c)
- [`code/fcn.1400214a6.c`](code/fcn.1400214a6.c)
- [`code/fcn.140025d42.c`](code/fcn.140025d42.c)
- [`code/fcn.140027d0e.c`](code/fcn.140027d0e.c)
- [`code/fcn.140028efb.c`](code/fcn.140028efb.c)
- [`code/fcn.14002baa1.c`](code/fcn.14002baa1.c)
- [`code/fcn.14002cf14.c`](code/fcn.14002cf14.c)
- [`code/fcn.140041c10.c`](code/fcn.140041c10.c)
- [`code/fcn.140045560.c`](code/fcn.140045560.c)
- [`code/fcn.140046a40.c`](code/fcn.140046a40.c)
- [`code/fcn.140047900.c`](code/fcn.140047900.c)
- [`code/fcn.140049cab.c`](code/fcn.140049cab.c)
- [`code/fcn.14004a4ad.c`](code/fcn.14004a4ad.c)
- [`code/fcn.140053150.c`](code/fcn.140053150.c)
- [`code/fcn.140059d00.c`](code/fcn.140059d00.c)
- [`code/fcn.14005c010.c`](code/fcn.14005c010.c)
- [`code/fcn.140061b50.c`](code/fcn.140061b50.c)
- [`code/fcn.140064650.c`](code/fcn.140064650.c)
- [`code/fcn.14006d264.c`](code/fcn.14006d264.c)
- [`code/fcn.14006d278.c`](code/fcn.14006d278.c)
- [`code/fcn.14006ebf4.c`](code/fcn.14006ebf4.c)
- [`code/fcn.140080550.c`](code/fcn.140080550.c)

## Behavioral Analysis

This update incorporates the findings from **Chunk 8/8** into the ongoing profile of the binary.

### Updated Analysis Summary

#### 1. Core Functionality & Purpose
*   **Sophisticated Data De-serialization:** This final chunk confirms that the software processes complex, potentially compressed or "packed" data structures. The code doesn't just read raw bytes; it interprets them based on tag-based logic and calculates complex offsets to navigate a multi-layered memory space.
*   **Cryptographic Core Inclusion:** A significant finding in this chunk is the presence of **AES (Advanced Encryption Standard)** implementation logic (`aesenc`, `aesenclast`). The code processes data blocks using these primitives, suggesting that internal assets, configuration files, or communication packets are encrypted/decrypted during the "loading" or "initialization" phase.
*   **Highly Optimized Memory Management:** Several functions exhibit patterns consistent with modern compiler backends (like LLVM) or high-performance game engines. These include complex buffer merging logic, overlapping memory calculations, and alignment-aware data copying.

#### 2. New Observations from Chunk 8/8
*   **Cryptographic Processing (`fcn.14000bc8a`):** The inclusion of AES logic indicates a robust security layer for the software's internal data. This is often used in professional software to protect proprietary algorithms, intellectual property (game assets), or secure communication between client and server.
*   **Tag-Based Parsing & State Logic (`fcn.14004a4ad`):** The code uses a "tag" system—checking for specific values like `0x4e5a`, `0x5f5f`, and `'R'`—to determine how to interpret the subsequent bytes. This is characteristic of serialization formats (like Protocol Buffers or custom internal IRs) where the data's type determines the decoding logic.
*   **Advanced Buffer Reconciliation (`fcn.1400199da`):** This function contains highly complex math for calculating indices and offsets (e.g., `uVar_14 * 0x15 * 8`). It handles cases where data might be "shifted" or "packed," adjusting pointers dynamically to ensure correct alignment during memory moves.
*   **Safety-Critical Check Cycles:** The code frequently includes nested loops that validate buffer boundaries before performing any operations. This is a hallmark of high-quality software development (especially in Rust/C++) where the goal is to prevent buffer overflows by pre-validating every jump and copy operation.

#### 3. Risk Assessment Update
*   **Malicious Intent:** **No change.** The complexity remains consistent with "High-End Software Engineering." While the presence of AES encryption *can* be a red flag in low-level malware (used for C2 communication), its implementation here is integrated into what appears to be a very sophisticated, well-architected infrastructure. It is far more likely used for protecting intellectual property or proprietary data structures than for hiding malicious payloads.
*   **Infrastructure Complexity:** This chunk completes the profile of the code as "Infrastructure Heavy." The logic is designed to handle high volumes of complex data efficiently and securely.

---

### Updated Summary for Report (Technical Update)
*   **Verdict: High-Complexity Systems Programming / Compiler Backend Architecture.**
*   **Updated Summary:** Analysis of Chunk 8/8 confirms a highly sophisticated infrastructure characterized by advanced data parsing, cryptographic integration, and high-performance memory management. The inclusion of AES primitives indicates a robust layer for protecting internal assets or communications. The code demonstrates complex state-based decoding (tag-driven) and intricate buffer reconciliation logic typical of compiler backends, virtual machine implementations, or large-scale engine middleware.
*   **Key Technical Indicators:** 
    *   **Cryptographic Primitives:** Explicit implementation of AES block processing for internal data security.
    *   **Tag-Based Serialization:** Implementation of a schema-aware parser that interprets data structures based on embedded type tags.
    *   **Sophisticated Buffer Management:** Multi-pass logic for resolving memory offsets, handling packed structures, and ensuring safe memory alignment during transitions.
    *   **Safety-First Engineering:** Prolific use of bounds checking and state validation, indicating a production-grade environment where stability is prioritized.

---

### Summary Table: Evidence Log (Consolidated)
| Feature | Observation | Interpretation |
| :--- | :--- | :--- |
| **Language/Design** | `rustc`, `thread_local`; complex bitmasking; high usage of safe-guard loops. | Rust or C++ architecture with a focus on safety and memory efficiency. |
| **Cryptographic Logic** | Presence of `aesenc` and `aesenclast` routines in `fcn.14000bc8a`. | Robust encryption for internal assets, configuration, or secure communication. |
| **Tag-Based Parsing** | Checks for specific constants (`0x4e5a`, `'R'`, etc.) to decide decoding paths. | Complex data deserialization (similar to Protobuf/FlatBuffers logic). |
| **Buffer Management** | Deeply nested loops and complex arithmetic for memory offset calculation. | High-performance buffer reconciliation; typical of compiler/engine middleware. |
| **Data Packing** | Use of `pshuflw` type logic, bitmasking, and shifting to decode multi-property fields. | Existence of an Intermediate Representation (IR) or highly optimized packed format. |
| **System Stability** | Extensive pre-calculation of buffer sizes before data movement occurs. | Professional-grade engineering aimed at eliminating memory safety vulnerabilities. |
| **State Management** | Multi-layered jumps based on bitwise flags to navigate internal execution paths. | Implementation of an interpreter, VM, or complex state machine for processing logic. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of AES encryption and tag-based parsing to process internal data structures serves to mask the program's content from static analysis. |
| T1055 | Packer | The multi-layered memory navigation, state machine logic, and complex buffer reconciliation indicate a sophisticated packer designed to hide malicious functionality until runtime. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None detected.

**File paths / Registry keys**
*   None detected.

**Mutex names / Named pipes**
*   None detected.

**Hashes**
*   None detected (the "EXTRACTED STRINGS" section contains obfuscated/randomized data rather than standard MD5, SHA1, or SHA256 hashes).

**Other artifacts**
*   **Internal Memory Offsets:** `fcn.14000bc8a`, `fcn.14004a4ad`, `fcn.1400199da` (Note: These are internal to the binary and serve as behavioral markers rather than network-based IOCs).
*   **Parsing Constants/Tags:** `0x4e5a`, `0x5f5f`, `'R'` (These identify specific logic branches in the data parsing routine).

---
**Analyst Note:** The provided materials appear to describe a high-complexity, legitimate piece of software engineering (likely a game engine or compiler backend written in Rust/C++). While technical artifacts like AES implementations and memory offsets are present, they do not constitute standard malicious IOCs such as C2 infrastructure or known malware filenames.

---

## Malware Family Classification

1. **Malware family**: None (Benign / Not Malicious)
2. **Malware type**: N/A (Potential False Positive)
3. **Confidence**: High
4. **Key evidence**:
    *   **High-End Software Engineering:** The analysis explicitly identifies the code as characteristic of a "compiler backend," "game engine," or "middleware," where complex memory management and tag-based parsing are standard for processing proprietary data structures.
    *   **Lack of Malicious Indicators:** There are no Command & Control (C2) infrastructure markers, known malicious strings, or payload delivery mechanisms typical of malware families like Emotet or Cobalt Strike.
    *   **Purpose of Encryption:** The use of AES is attributed to protecting intellectual property and internal assets rather than concealing malicious functionality; the report notes the code's "sophisticated architecture" aligns with high-quality production software rather than standard malware.
