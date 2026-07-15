# Threat Analysis Report

**Generated:** 2026-07-12 13:45 UTC
**Sample:** `05264c0d02cba4c2cff50fcc150d710a828ae00da9e68889dbf4c1a95b9ee224_05264c0d02cba4c2cff50fcc150d710a828ae00da9e68889dbf4c1a95b9ee224.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05264c0d02cba4c2cff50fcc150d710a828ae00da9e68889dbf4c1a95b9ee224_05264c0d02cba4c2cff50fcc150d710a828ae00da9e68889dbf4c1a95b9ee224.exe` |
| File type | PE32+ executable for MS Windows 6.01 (DLL), x86-64, 7 sections |
| Size | 3,448,328 bytes |
| MD5 | `f6e2c5c4c8827691e5c3a7716d6a49d2` |
| SHA1 | `24d38175b1f2b7bfad378a75028329344c86113a` |
| SHA256 | `05264c0d02cba4c2cff50fcc150d710a828ae00da9e68889dbf4c1a95b9ee224` |
| Overall entropy | 6.316 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1750633016 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,704,448 | 6.523 | No |
| `.rdata` | 1,565,696 | 5.483 | No |
| `.data` | 104,448 | 3.721 | No |
| `.pdata` | 43,008 | 5.412 | No |
| `.gfids` | 512 | -0.0 | No |
| `.rsrc` | 2,560 | 1.827 | No |
| `.reloc` | 24,064 | 5.434 | No |

### Imports

**KERNEL32.dll**: `AddVectoredContinueHandler`, `AddVectoredExceptionHandler`, `CloseHandle`, `CreateEventA`, `CreateIoCompletionPort`, `CreateThread`, `CreateWaitableTimerExW`, `DeleteCriticalSection`, `DuplicateHandle`, `EnterCriticalSection`, `ExitProcess`, `FreeEnvironmentStringsW`, `GetConsoleMode`, `GetCurrentThreadId`, `GetEnvironmentStringsW`
**api-ms-win-crt-heap-l1-1-0.dll**: `calloc`, `free`, `malloc`
**api-ms-win-crt-private-l1-1-0.dll**: `memcpy`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_execute_onexit_table`, `_exit`, `_initialize_onexit_table`, `_initterm`, `_initterm_e`, `_register_onexit_function`, `abort`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__acrt_iob_func`, `__stdio_common_vfprintf`, `fwrite`
**api-ms-win-crt-string-l1-1-0.dll**: `strlen`, `strncmp`

### Exports

`CfgAllocateResource`, `gGHfPyGrCIfGMcOGl`

## Extracted Strings

Total strings found: **5082** (showing first 100)

```
!This program cannot be run in DOS mode.$
`.rdata
@.data
.pdata
@.gfids
@.reloc
l$ M9,$u
8cpu.u
P0H9S0
PPH9SP
PpH9Sp
UUUUUUUUH!
33333333H!
\$PH9H@v#H
D$pL9A
L$pL9N
D$@I9p
\$hM9K
\$hM9K
l$8M9,$u
P(H9S(t
P H9S uqH
S0H9P0ug
P88S8u^
P98S9uUH
expafH
nd 3fH
2-byfH
te kfH
H9uH
H9L$ r
L$@H9
s`H9J
debugCal
debugCal
debugCalH9
debugCalH9
l409u
x6tzH9
l819um
debugCalH9
l163uf
x84t6H9
l327uf
runtime.
runtime H
 error: H
f9A2vA
q`f9q2r
:H9F w
>H+zhH
L$HI9QhuH
P`f9P2tgH
\$0f9C2u
2}#s]H
D$PA)P
H9D$(t
^0H9X0tQ
\$XHc
$H+L$HH
T$(H+J
L$(H+A

H9Z(w
\$0H9K
D$pH9H
D$0H9H
|$pH9\$
T$ H+:
UUUUUUUUH!
UUUUUUUUH
wwwwwwwwH!
wwwwwwwwH
J0f9J2vsL
f9s2u:H=
D$$u$L
H9T$@u
T$(M	D
runtime.H9
QpM9Qhu
L9L$Xt$H
H9>wHH9~
runtime.H9
reflect.H9
I9N0tVH
T$ 9T$$
H92t9H9rHt3H
rhH92w
H+5h+2
tRI9N0tLH
|$0uMH
memprofi
lerau*f
yteu"H
9q0s&H9J
09z0w
H
H9X(v
L
HPH9w
H(H9w
H95GH-
L$HH9A
Q8H+Q(
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1801a0070` | `0x1801a0070` | 1701446 | ✓ |
| `fcn.180067c60` | `0x180067c60` | 382394 | ✓ |
| `fcn.180067cc0` | `0x180067cc0` | 362459 | ✓ |
| `fcn.180067c80` | `0x180067c80` | 362458 | ✓ |
| `fcn.18006c7e0` | `0x18006c7e0` | 232663 | ✓ |
| `fcn.180068140` | `0x180068140` | 205992 | ✓ |
| `fcn.180068160` | `0x180068160` | 205864 | ✓ |
| `fcn.180068180` | `0x180068180` | 205739 | ✓ |
| `fcn.1800681a0` | `0x1800681a0` | 205611 | ✓ |
| `fcn.18006c940` | `0x18006c940` | 205591 | ✓ |
| `fcn.1800681c0` | `0x1800681c0` | 205483 | ✓ |
| `fcn.1800681e0` | `0x1800681e0` | 205355 | ✓ |
| `fcn.180068200` | `0x180068200` | 205224 | ✓ |
| `fcn.180068220` | `0x180068220` | 205096 | ✓ |
| `fcn.180068240` | `0x180068240` | 204968 | ✓ |
| `fcn.180068260` | `0x180068260` | 204840 | ✓ |
| `fcn.180068280` | `0x180068280` | 204712 | ✓ |
| `fcn.1800682a0` | `0x1800682a0` | 204584 | ✓ |
| `fcn.18006c9a0` | `0x18006c9a0` | 176439 | ✓ |
| `fcn.18006ca40` | `0x18006ca40` | 149207 | ✓ |
| `fcn.18006caa0` | `0x18006caa0` | 132119 | ✓ |
| `fcn.1800abea0` | `0x1800abea0` | 22777 | ✓ |
| `fcn.180115ba0` | `0x180115ba0` | 19597 | ✓ |
| `fcn.180067c40` | `0x180067c40` | 11731 | ✓ |
| `fcn.18014f220` | `0x18014f220` | 11438 | ✓ |
| `fcn.1801980c0` | `0x1801980c0` | 10953 | ✓ |
| `fcn.1800b28c0` | `0x1800b28c0` | 9477 | ✓ |
| `fcn.180102b40` | `0x180102b40` | 8695 | ✓ |
| `fcn.180191ea0` | `0x180191ea0` | 7454 | ✓ |
| `fcn.1800184e0` | `0x1800184e0` | 6181 | ✓ |

### Decompiled Code Files

- [`code/fcn.1800184e0.c`](code/fcn.1800184e0.c)
- [`code/fcn.180067c40.c`](code/fcn.180067c40.c)
- [`code/fcn.180067c60.c`](code/fcn.180067c60.c)
- [`code/fcn.180067c80.c`](code/fcn.180067c80.c)
- [`code/fcn.180067cc0.c`](code/fcn.180067cc0.c)
- [`code/fcn.180068140.c`](code/fcn.180068140.c)
- [`code/fcn.180068160.c`](code/fcn.180068160.c)
- [`code/fcn.180068180.c`](code/fcn.180068180.c)
- [`code/fcn.1800681a0.c`](code/fcn.1800681a0.c)
- [`code/fcn.1800681c0.c`](code/fcn.1800681c0.c)
- [`code/fcn.1800681e0.c`](code/fcn.1800681e0.c)
- [`code/fcn.180068200.c`](code/fcn.180068200.c)
- [`code/fcn.180068220.c`](code/fcn.180068220.c)
- [`code/fcn.180068240.c`](code/fcn.180068240.c)
- [`code/fcn.180068260.c`](code/fcn.180068260.c)
- [`code/fcn.180068280.c`](code/fcn.180068280.c)
- [`code/fcn.1800682a0.c`](code/fcn.1800682a0.c)
- [`code/fcn.18006c7e0.c`](code/fcn.18006c7e0.c)
- [`code/fcn.18006c940.c`](code/fcn.18006c940.c)
- [`code/fcn.18006c9a0.c`](code/fcn.18006c9a0.c)
- [`code/fcn.18006ca40.c`](code/fcn.18006ca40.c)
- [`code/fcn.18006caa0.c`](code/fcn.18006caa0.c)
- [`code/fcn.1800abea0.c`](code/fcn.1800abea0.c)
- [`code/fcn.1800b28c0.c`](code/fcn.1800b28c0.c)
- [`code/fcn.180102b40.c`](code/fcn.180102b40.c)
- [`code/fcn.180115ba0.c`](code/fcn.180115ba0.c)
- [`code/fcn.18014f220.c`](code/fcn.18014f220.c)
- [`code/fcn.180191ea0.c`](code/fcn.180191ea0.c)
- [`code/fcn.1801980c0.c`](code/fcn.1801980c0.c)
- [`code/fcn.1801a0070.c`](code/fcn.1801a0070.c)

## Behavioral Analysis

This final piece of disassembly (Chunk 5/5) provides the "missing link" between the high-level VM architecture and the low-level execution. While Chunk 4 showed us the **Engine** (the SIMD crypto and the Dispatcher), Chunk 5 reveals the **Data Processing Layer**.

The code in this chunk is characteristic of a **complex state machine** used to parse internal data structures, likely those required to manage memory segments or decode "internal" instructions that are even further nested.

### New Findings from Chunk 5/5

#### 1. Bitwise Page-Mapping Logic (Index Calculation)
The most significant technical finding in this chunk is the logic involving `>> 6` and `& 0x3f`.
*   **Code Context:** `if (*(*0x20 + iVar5 * 8 + -0x68) >> 6 != 0)` and `uVar3 = uVar3 | 1LL << (*(*0x20 + iVar5 * 8 + -0x68) & 0x3f);`
*   **Technical Meaning:** Shifting right by 6 is mathematically equivalent to dividing by 64. Masking with `0x3F` (decimal 63) isolates the remainder of a division by 64. This is the standard way to calculate an **offset within a page**.
*   **Significance:** This suggests that the malware is managing its own internal memory map. It isn't just looking at an address; it is calculating where a piece of data sits relative to a specific base, likely to facilitate "in-memory" execution of multiple modules or to navigate a custom virtual address space created by the packer.

#### 2. Decoupled Execution (The Gatekeeper Pattern)
The repeated calls to `fcn.180067d80()` and `fcn.180067dc0()` are now clearly identified as **Execution Gates**.
*   **How it works:** Notice how the code sets a value (`puVar2 = ...`), then immediately performs a check, and calls `fcn.180067d80()`. 
*   **Significance:** This is a "Proxy" pattern. The VM logic doesn't know what `fcn.180067d80()` does; it only knows that it must call it to perform the next action (e.g., allocating memory, changing protection, or creating a thread). This prevents an analyst from seeing a direct link between "Action A" and "System Call B."

#### 3. Structured Data Deserialization
The loop starting at `for (iVar6 = *0x18032a628; 0 < iVar6; iVar6 = iVar6 - 1)` is a **Deserialization Loop**.
*   **Observation:** It iterates through an array of structures (`puVar2`) and extracts multiple fields (e.g., `puVar2[3]`, `puVar2[5]`, `puVar2[7]`).
*   **Significance:** This confirms that the malware has a highly organized internal database or "recipe" for how it unpacks its components. It is likely iterating through a list of objects, where each object represents a different stage of the infection or a different malicious capability (e.g., Module 1 = Keylogger; Module 2 = Backdoor).

---

### Updated Analysis Summary (Cumulative)

The malware utilizes a **Multi-Tiered Obfuscation Architecture** that combines several advanced techniques to evade both automated and manual analysis:

| Feature | Technical Observation | Threat Significance |
| :--- | :--- | :--- |
| **Virtual Machine (VM)** | Extensive use of `case` blocks as an instruction dispatcher. | **Critical:** Disconnects the "intent" from the "action," making it nearly impossible to map logic via static analysis. |
| **SIMD/AVX2 Crypto** | Usage of `vpshufb`, `vpaddd` in `fcn.180191ea0`. | **High:** Indicates a high-performance, custom-built decryption engine for large payloads. |
| **Page-Aware Mapping** | Shift/Mask logic (`>> 6`, `& 0x3f`). | **High:** Suggests sophisticated memory management and the ability to house multiple modules in one process. |
| **Gatekeeper Wrappers** | Heavy use of internal calls like `fcn.180067d80`. | **Critical:** Shields the malware's interaction with the Windows API from analysis tools. |

---

### Technical Interpretation & Synthesis

By combining all five chunks, we can now construct a complete map of how this malware operates:

1.  **The Outer Shell (The VM):** The malware is wrapped in a custom Virtual Machine. When you look at the code, you aren't seeing "Malware Code"; you are seeing "Interpreter Code."
2.  **The Data Management:** Within that VM, there is a sophisticated system for managing memory and data structures. The bitwise logic we found in Chunk 5 shows it manages its own internal "pages," allowing it to hide several different modules within one memory space.
3.  **The Transformation (SIMD):** When the VM decides it is time to "unpack" a module, it calls into the high-performance SIMD blocks discovered in Chunk 4. This quickly decrypts large amounts of data that are no longer hidden by the obfuscated shell.
4.  **The Execution Gate:** Once decrypted, the "Gatekeeper" functions (the `fcn.180...` series) are used to execute the payload's final actions, and because these functions are heavily wrapped, it is very difficult for an analyst to see what they actually do until the moment of execution.

---

### Finalized Action Plan:

Based on the total evidence across all 5 chunks:

1.  **Identify the "Payload Transition":** The most critical point in memory is where the code transitions from **VM-land** (the dispatcher) to **Native-land** (the decrypted payload).
    *   *Action:* Set a breakpoint on `fcn.180191ea0` (The SIMD/AVX block). Monitor the memory buffer it processes. The moment that calculation finishes, the next jump is likely into the "real" malware code.

2.  **Memory Dumping:** Because of the heavy use of VM-based obfuscation and internal state tracking, static analysis of this file will yield diminishing returns.
    *   *Action:* Run the sample in a controlled environment (e.g., FlareVM). Use **Scylla** or similar tools to dump memory regions just after the SIMD processing is completed but before the final "Gatekeeper" functions are executed.

3.  **Trace the Gatekeepers:** 
    *   *Action:* Log all calls to `fcn.180067d80` and its variants. Even if you don't know what they do immediately, observing *when* they are called will tell you exactly when the malware is attempting networking, file system changes, or process injection.

**Final Conclusion:** This is a **highly sophisticated, professional-grade packer/loader**. It uses a combination of Virtual Machine architecture to hide logic, SIMD instructions for high-performance decryption, and "Gatekeeper" wrappers to shield API calls. It is designed specifically to defeat standard automated sandboxes and frustrate manual reverse engineering by forcing the analyst to deconstruct an entire virtualized CPU state just to see one simple command.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, the following MITRE ATT&K techniques have been identified:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtual Machine System Firmware | The malware uses a custom instruction dispatcher and "Gatekeeper" wrappers to decouple internal logic from system calls, making it difficult to map the intent of the code. |
| **T1027** | Obfuscated Files | The use of SIMD/AVX2 instructions for high-performance decryption and bitwise logic to mask memory mapping hides the true nature of the payload. |
| **T1106** | Dynamic Resolution | (Optional Mapping) While not explicitly shown as a dynamic API call, the "Gatekeeper" pattern is a common architecture used to hide the resolution and calling of system functions from automated analysis tools. |

### Analysis Notes:
*   **T1497 (Virtual Machine System Firmware):** This is the primary technique for the malware's core infrastructure. By creating a custom VM, it ensures that any standard signature-based or heuristic scan only sees "interpreter" logic rather than the actual malicious instructions (the "logic gate" mentioned in your analysis).
*   **T1027 (Obfuscated Files):** This covers both the SIMD decryption layer and the complex state machine. It addresses the intent to hide strings, capabilities (the "recipe"), and functionality from static analysis.
*   **Gatekeeper Pattern:** In many cases, these wrappers are used to facilitate **T1027**, specifically to ensure that there is no direct jump or call between a malicious action (like creating a process) and the Windows API call required to execute it.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted intelligence.

### **IOC Analysis Report**

**IP addresses / URLs / Domains**
*   *None identified.* (The string "www" appears multiple times but is not associated with a domain or TLD).

**File paths / Registry keys**
*   *None identified.* (Strings like `.rdata`, `.data`, and `.pdata` are standard linker sections and do not constitute actionable file paths).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.* (While several hex-like values appear in the analysis, e.g., `180067d80`, these are internal memory addresses/offsets, not file hashes).

**Other artifacts**
*   **Internal Function Offsets (Gatekeepers):** 
    *   `180067d80`
    *   `180067dc0`
    *   `180191ea0` (Identified as the SIMD/AVX2 decryption block)
*   **Internal Memory Address:** `0x18032a628` (Used in the deserialization loop).
*   **Behavioral Patterns:**
    *   **VM-based Obfuscation:** Use of a custom interpreter with a "case" block instruction dispatcher.
    *   **SIMD/AVX2 Cryptography:** Utilization of `vpshufb` and `vpaddd` instructions for high-speed payload decryption.
    *   **Page-Mapping Logic:** Bitwise manipulation (`>> 6`, `& 0x3f`) used to manage a custom internal memory map to hide multiple modules.
    *   **Gatekeeper Pattern:** Use of wrapped function calls to shield standard Windows API interactions from static analysis.

---
**Analyst Note:** This sample is a sophisticated, multi-layered loader/packer rather than a simple "dropper." The lack of explicit network IOCs in the current data suggests that the primary purpose of this specific module is to provide an obfuscated environment (VM) and high-performance decryption (SIMD) for an internal payload. Further dynamic analysis is required to capture memory dumps at the transition point from the "VM-land" to "Native-land."

---

## Malware Family Classification

1. **Malware family**: Custom (Advanced Packer/Loader)
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
* **Virtual Machine (VM) Architecture:** The sample employs a complex instruction dispatcher and "Gatekeeper" wrappers to decouple its internal logic from Windows API calls, making it extremely difficult for static analysis tools to map the code's intent.
* **Sophisticated Decryption Layer:** The use of SIMD/AVX2 instructions (`vpshufb`, `vpaddd`) indicates a professional-grade decryption engine designed to rapidly process and unpack large amounts of data (payload modules).
* **Modular Memory Management:** The presence of bitwise page-mapping logic and deserialization loops suggests the loader is designed to host, manage, and transition between multiple internal modules (e.g., keyloggers or backdoors) within a single protected memory space.
