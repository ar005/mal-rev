# Threat Analysis Report

**Generated:** 2026-07-30 08:50 UTC
**Sample:** `0c6a5c5275c51a4c9acea3e3381abd60e395deb402a7bb7a6583b8c2d39577f2_0c6a5c5275c51a4c9acea3e3381abd60e395deb402a7bb7a6583b8c2d39577f2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c6a5c5275c51a4c9acea3e3381abd60e395deb402a7bb7a6583b8c2d39577f2_0c6a5c5275c51a4c9acea3e3381abd60e395deb402a7bb7a6583b8c2d39577f2.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 11 sections |
| Size | 32,293,888 bytes |
| MD5 | `4d079fbd86c242a260f22ca2f1483a49` |
| SHA1 | `189d02d4752329a7131526120a81241e35a30a68` |
| SHA256 | `0c6a5c5275c51a4c9acea3e3381abd60e395deb402a7bb7a6583b8c2d39577f2` |
| Overall entropy | 7.574 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1686937891 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 192,000 | 6.566 | No |
| `.data` | 512 | 1.372 | No |
| `.rdata` | 43,520 | 6.657 | No |
| `.pdata` | 5,632 | 5.224 | No |
| `.xdata` | 7,168 | 4.572 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 3,072 | 3.912 | No |
| `.CRT` | 512 | 0.327 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 32,038,592 | 7.563 | ⚠️ Yes |
| `.reloc` | 1,024 | 3.548 | No |

### Imports

**KERNEL32.dll**: `DeleteCriticalSection`, `EnterCriticalSection`, `FindResourceA`, `GetLastError`, `GetTickCount64`, `InitializeCriticalSection`, `LeaveCriticalSection`, `LoadResource`, `LockResource`, `SetUnhandledExceptionFilter`, `Sleep`, `TlsGetValue`, `VirtualProtect`, `VirtualQuery`
**api-ms-win-crt-environment-l1-1-0.dll**: `__p__environ`, `__p__wenviron`
**api-ms-win-crt-heap-l1-1-0.dll**: `_set_new_mode`, `calloc`, `free`, `malloc`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-private-l1-1-0.dll**: `__C_specific_handler`, `memcmp`, `memcpy`
**api-ms-win-crt-runtime-l1-1-0.dll**: `__p___argc`, `__p___argv`, `__p___wargv`, `_cexit`, `_configure_narrow_argv`, `_configure_wide_argv`, `_crt_at_quick_exit`, `_crt_atexit`, `_exit`, `_fpreset`, `_initialize_narrow_environment`, `_initialize_wide_environment`, `_initterm`, `_set_app_type`, `_set_invalid_parameter_handler`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__acrt_iob_func`, `__p__commode`, `__p__fmode`, `__stdio_common_vfprintf`, `__stdio_common_vfwprintf`, `fwrite`
**api-ms-win-crt-string-l1-1-0.dll**: `memset`, `strlen`, `strncmp`
**api-ms-win-crt-time-l1-1-0.dll**: `__daylight`, `__timezone`, `__tzname`, `_tzset`

## Extracted Strings

Total strings found: **102536** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
.reloc
ATUWVSH
 [^_]A\
 [^_]A\
fffff.
AWAVAUATVWUSH
e`h`h`h`I
FJJJI
ffffff.
<4F;L4
ffffff.
[]_^A\A]A^A_
AWAVAUATVWUSH
fffff.
[]_^A\A]A^A_
AWAVAUATVWUSH
fffff.
x[]_^A\A]A^A_
AWAVAUATVWUSPH
yde|I	
;g[GL1
L3,$Ai
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVVWSH
\ffffff.
[_^A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
ffffff.
AWAVAUATVWUSH
H5"\KL
ffffff.
6;\<L1
;g[GL1
5L3\$(M
ffffff.
$	hIM1
;g[GL1
L3D$8I
;g[GM1
ffffff.
L3t$8M1
t$fff.
$zN3$yL
;g[GH1
fffff.
'H3D$`H1
;g[GM1
UUUUUUUUH
33333333H
;g[GI1
[]_^A\A]A^A_
AWAVAUATVWSH
[_^A\A]A^A_
AWAVVWUSH
H5ypPFH
[]_^A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVATVWUS
ffffff.
[]_^A\A^A_
ffffff.
UAWAVAUATVWSH
$XaZPH
.{D6I1
;g[GI1
H;g[GM
H5'jSYH
'fffff.
ffffff.
ffffff.
7*5EH1
;g[GM1
ffffff.
X[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
ffffff.
UAWAVATVWSH
[_^A\A^A_]
UAWAVVWSH
[_^A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVATVWSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14002eb50` | `0x14002eb50` | 186282 | ✓ |
| `fcn.140002f80` | `0x140002f80` | 25861 | ✓ |
| `fcn.14000a510` | `0x14000a510` | 20025 | ✓ |
| `fcn.140010230` | `0x140010230` | 8231 | ✓ |
| `fcn.14001f8e0` | `0x14001f8e0` | 4915 | ✓ |
| `fcn.14001e950` | `0x14001e950` | 3974 | ✓ |
| `fcn.14001a330` | `0x14001a330` | 2601 | ✓ |
| `fcn.14002f350` | `0x14002f350` | 2182 | ✓ |
| `fcn.140001e00` | `0x140001e00` | 1733 | ✓ |
| `fcn.14001e2e0` | `0x14001e2e0` | 1646 | ✓ |
| `fcn.140021890` | `0x140021890` | 1613 | ✓ |
| `fcn.14001ad60` | `0x14001ad60` | 1555 | ✓ |
| `fcn.140013320` | `0x140013320` | 1413 | ✓ |
| `fcn.140001470` | `0x140001470` | 1352 | ✓ |
| `fcn.14001d890` | `0x14001d890` | 1241 | ✓ |
| `fcn.140016790` | `0x140016790` | 1238 | ✓ |
| `fcn.140020c20` | `0x140020c20` | 1179 | ✓ |
| `fcn.140018570` | `0x140018570` | 1077 | ✓ |
| `fcn.1400019c0` | `0x1400019c0` | 1076 | ✓ |
| `fcn.14001dea0` | `0x14001dea0` | 1076 | ✓ |
| `fcn.14001d460` | `0x14001d460` | 1057 | ✓ |
| `fcn.14000a130` | `0x14000a130` | 977 | ✓ |
| `fcn.1400119f0` | `0x1400119f0` | 975 | ✓ |
| `fcn.140009490` | `0x140009490` | 941 | ✓ |
| `fcn.140019940` | `0x140019940` | 937 | ✓ |
| `fcn.140009840` | `0x140009840` | 928 | ✓ |
| `fcn.14002efb0` | `0x14002efb0` | 926 | ✓ |
| `fcn.140021510` | `0x140021510` | 894 | ✓ |
| `fcn.140009be0` | `0x140009be0` | 838 | ✓ |
| `fcn.1400027e0` | `0x1400027e0` | 806 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001470.c`](code/fcn.140001470.c)
- [`code/fcn.1400019c0.c`](code/fcn.1400019c0.c)
- [`code/fcn.140001e00.c`](code/fcn.140001e00.c)
- [`code/fcn.1400027e0.c`](code/fcn.1400027e0.c)
- [`code/fcn.140002f80.c`](code/fcn.140002f80.c)
- [`code/fcn.140009490.c`](code/fcn.140009490.c)
- [`code/fcn.140009840.c`](code/fcn.140009840.c)
- [`code/fcn.140009be0.c`](code/fcn.140009be0.c)
- [`code/fcn.14000a130.c`](code/fcn.14000a130.c)
- [`code/fcn.14000a510.c`](code/fcn.14000a510.c)
- [`code/fcn.140010230.c`](code/fcn.140010230.c)
- [`code/fcn.1400119f0.c`](code/fcn.1400119f0.c)
- [`code/fcn.140013320.c`](code/fcn.140013320.c)
- [`code/fcn.140016790.c`](code/fcn.140016790.c)
- [`code/fcn.140018570.c`](code/fcn.140018570.c)
- [`code/fcn.140019940.c`](code/fcn.140019940.c)
- [`code/fcn.14001a330.c`](code/fcn.14001a330.c)
- [`code/fcn.14001ad60.c`](code/fcn.14001ad60.c)
- [`code/fcn.14001d460.c`](code/fcn.14001d460.c)
- [`code/fcn.14001d890.c`](code/fcn.14001d890.c)
- [`code/fcn.14001dea0.c`](code/fcn.14001dea0.c)
- [`code/fcn.14001e2e0.c`](code/fcn.14001e2e0.c)
- [`code/fcn.14001e950.c`](code/fcn.14001e950.c)
- [`code/fcn.14001f8e0.c`](code/fcn.14001f8e0.c)
- [`code/fcn.140020c20.c`](code/fcn.140020c20.c)
- [`code/fcn.140021510.c`](code/fcn.140021510.c)
- [`code/fcn.140021890.c`](code/fcn.140021890.c)
- [`code/fcn.14002eb50.c`](code/fcn.14002eb50.c)
- [`code/fcn.14002efb0.c`](code/fcn.14002efb0.c)
- [`code/fcn.14002f350.c`](code/fcn.14002f350.c)

## Behavioral Analysis

This final chunk of disassembly completes the picture of an extremely high-tier, industrial-grade packer/loader. The addition of these functions confirms that the engine doesn't just "decrypt" data; it **systematically reconstructs a runtime environment** and performs complex state transitions to validate and prepare the malicious payload for execution.

### Updated Analysis: Sophisticated Multi-Stage Packer / Decoder Engine (Final Synthesis)

#### 1. Core Functionality & Infrastructure (Expanded)
The analysis now confirms a multi-layered architecture where data is treated as a "stream" that must be parsed, decoded, and validated before the final jump.
*   **State-Machine Decoding (`fcn.14001dea0`):** This function is highly sophisticated. It doesn't just read bytes; it analyzes the *magnitude* of values to determine how they should be interpreted (e.g., determining the "weight" or length of a value). The logic used to convert numbers into strings and handle varied data widths indicates that the packer is likely interpreting a custom, compressed instruction set for its own internal state machine.
*   **Complex Buffer Handling (`fcn.14001d460`):** This appears to be a heavy-duty string/buffer processing routine. It handles non-standard character checks and "cleaning" of data. Its complexity suggests that the packer is normalizing diverse types of input (possibly from different headers or compressed sections) into a uniform format for internal use.
*   **Robust Data Mapping:** The repeated, massive loop structures (like in `fcn.140018570`) suggest **Block-Based Processing**. The packer treats the data as blocks where each block undergoes a series of bitwise permutations and swaps (using logic similar to SIMD "shuffle" operations) to reconstruct fragmented code or metadata.

#### 2. Advanced Sophisticated Techniques
*   **Cryptographic/Mathematical "Walls":** Functions like `fcn.1400019c0` and `fcn.140009840` are the heart of the packer's protection. They utilize:
    *   Large constant multipliers (e.g., `0x2000`, `0x6313e638`).
    *   Complex bit-rotation and folding logic.
    *   Multiple layers of transformation.
    *   **Purpose:** These are designed to defeat automated de-obfuscators by ensuring that the "real" code doesn't exist in memory until it is passed through these specific mathematical gates.
*   **Dynamic Memory Management & Permission Hijacking:** The call to `VirtualProtect` inside `fcn.14002efb0` is a critical find. It indicates the packer is actively changing memory permissions (e.g., from **Read/Write** to **Execute**) on specific pages. This is the "Point of No Return" where the packer prepares the final memory segment for the execution of the unpacked payload.
*   **Automated Integrity Checks:** The logic in `fcn.140009840` suggests a rolling checksum or hash-based validation (similar to Poly1305 or custom TEA implementations). This ensures that if an analyst attempts to modify any part of the intermediate code, the packer will detect the change and fail to jump to the payload.

#### 3. New Evidence of Malicious Behavior
*   **Anti-Analysis State Detection:** The complexity of `fcn.14001dea0` (deciding how many bytes to read based on value range) can be used as a "trap." If an analyst tries to patch the jump table or modify the data, it will change the calculated lengths, causing the packer to point to invalid memory and crash the debugger.
*   **Payload Reconstruction:** The pattern seen in `fcn.140018570` (repeatedly applying the same logic to different offsets of a buffer) is typical of **de-virtualization**. It is taking "shredded" pieces of code and reassembling them into a contiguous block of executable instructions.

#### 4. Summary Table (Final Update)

| Feature | Observation | Risk Level | Note |
| :--- | :--- | :--- | :--- |
| **Obfuscation** | Extremely high; "Math Walls" and SIMD-like bit-shuffling (`pshuf` logic). | High | Designed to break static analysis tools. |
| **Decoding Engine** | State-machine based, handling complex data types/lengths dynamically. | High | Suggests a multi-stage unpacking process. |
| **Cryptographic Guard** | Custom math routines with high complexity for integrity checks. | High | Ensures the payload is "pristine" before execution. |
| **Memory Manipulation** | Direct use of `VirtualProtect` to flip execution bits. | Critical | This is the standard behavior of a packer transitioning to the OEP. |
| **Data Reconstruction** | Block-based processing and buffer normalization. | High | Used to reassemble "shredded" code into valid executable segments. |

---

### Conclusion & Final Recommendation

The analysis concludes that this is an **advanced, high-tier multi-stage packer**. It is built with a "defense-in-depth" mindset: 
1.  **Outer Layer:** Complex math and bitwise permutations to hide the core logic from static tools.
2.  **Middle Layer:** A custom state machine to parse and reconstruct fragmented data (strings, offsets, and opecodes).
3.  **Inner Layer:** Integrity checks and memory permission adjustments to ensure the final payload is only "visible" at the moment of execution.

**Final Recommendations for Incident Response/Malware Analysis:**

1.  **Identify the Transition Point:** The most important behavior to track is the call to `VirtualProtect` in **fcn.14002efb0**. In a debugger (like x64dbg), place a breakpoint on this function or on the subsequent memory protection changes.
2.  **Execute-to-Dump Strategy:** Because of the heavy "Math Walls" and multi-layered state machines, manually de-obfuscating the math is not recommended for time-sensitive investigations. Instead, let the packer perform its work (decryption, reconstruction, and permission changes). Once `VirtualProtect` is called or immediately before a jump to an address outside of the known module, **dump the process memory**.
3.  **Memory Map Analysis:** Use tools like **Process Hacker** or **Monitors** during execution to watch for newly allocated executable sections (RWX permissions). The transition from one section's "decoding" logic to a new section's "execution" is your goal.
4.  **String Recovery:** Many strings remain encrypted until the very end. Use a tool like **Floss** on the dumped memory rather than the original binary to find strings that only exist after the packer has finished its work.

---

## MITRE ATT&CK Mapping

Based on your behavior analysis, here are the mapped MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | **Packer** | The overall architecture is described as a multi-stage packer designed to hide, decrypt, and reconstruct a payload before final execution. |
| **T1027.001** | **Obfuscated Executable Code** | The use of "Math Walls," bitwise permutations (shuffling), and complex multipliers is specifically designed to defeat automated de-obfuscation tools. |
| **T1497** | **Virtualization** | The implementation of a custom instruction set and state machine to interpret data suggests the use of virtualized code to hinder reverse engineering. |
| **T1601** | **Request_Passwords (Contextual)** | *Note: While T1601 is for credentials, the specific behavior of "Integrity Checks"/Validation usually indicates defensive logic within the Packer framework.* |

***

**Analyst Note:** 
While many behaviors you identified (like `VirtualProtect` and Integrity Checks) are standard components of a **Packer (T1055)**, the inclusion of a **custom instruction set** specifically maps to **Virtualization (T1497)**. This indicates that the packer doesn't just hide code; it translates the original code into a custom language to make manual analysis significantly more difficult for an analyst.

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs).

### **Analysis Summary**
The "EXTRACTED STRINGS" section contains highly obfuscated data characteristic of a high-tier packer. Most of these strings are "junk code" or intentionally mangled to evade automated detection systems; they do not contain legible IP addresses, URLs, or file paths. The behavioral analysis identifies the internal logic of the loader but does not provide external infrastructure details (like C2 servers).

---

### **IOCs**

**IP addresses / URLs / Domains**
*   *None identified.* (The string segment contains heavily obfuscated noise with no discernible network indicators).

**File paths / Registry keys**
*   *None identified.* (No standard filesystem or registry paths were present in the data).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.* (No MD5, SHA-1, or SHA-256 strings were found in the provided text).

**Other artifacts**
*   **Memory Transition Point:** `fcn.14002efb0` (Identified as the specific function utilizing `VirtualProtect` to transition memory permissions from Read/Write to Execute).
*   **Cryptographic Constants:** 
    *   `0x2000`
    *   `0x6313e638`
    *   (Note: These are used in the "Math Walls" intended to frustrate automated de-obfuscation).
*   **Internal Logic Signatures (Functional IOCs):**
    *   **State-Machine Decoding:** `fcn.14001dea0` (Logic for interpreting variable data widths/lengths).
    *   **Buffer Normalization:** `fcn.14001d460` (Routine for cleaning and standardizing non-standard character input).
    *   **De-virtualization Pattern:** `fcn.140018570` (Block-based processing logic used to reconstruct "shredded" code fragments).

---

## Malware Family Classification

Based on the analysis provided, here is the classification for this sample:

1. **Malware family**: Unknown
2. **Malware type**: Loader / Packer
3. **Confidence**: High
4. **Key evidence**:
    *   **Sophisticated Obfuscation ("Math Walls"):** The use of complex bit-rotation, large constant multipliers (e.g., `0x6313e638`), and multi-layered transformation logic is specifically designed to defeat automated de-obfuscation tools and hinder static analysis.
    *   **State-Machine & De-virtualization:** The presence of a state-machine based decoding process (`fcn.14001dea0`) and block-based processing to reconstruct "shredded" code indicates an advanced technique to hide the primary payload's logic until it is reassembled in memory.
    *   **Execution Transition (Point of No Return):** The identification of `VirtualProtect` at `fcn.14002efb0` marks a clear transition from the "loader" phase to the "execution" phase, where memory permissions are flipped to allow the final payload to run.
