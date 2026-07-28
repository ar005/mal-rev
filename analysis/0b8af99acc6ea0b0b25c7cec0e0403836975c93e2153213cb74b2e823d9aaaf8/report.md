# Threat Analysis Report

**Generated:** 2026-07-26 12:14 UTC
**Sample:** `0b8af99acc6ea0b0b25c7cec0e0403836975c93e2153213cb74b2e823d9aaaf8_0b8af99acc6ea0b0b25c7cec0e0403836975c93e2153213cb74b2e823d9aaaf8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b8af99acc6ea0b0b25c7cec0e0403836975c93e2153213cb74b2e823d9aaaf8_0b8af99acc6ea0b0b25c7cec0e0403836975c93e2153213cb74b2e823d9aaaf8.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 8 sections |
| Size | 3,511,808 bytes |
| MD5 | `e4e16af17e49e3c8e70fd9ee88165f25` |
| SHA1 | `bf9f73255bc647f694cb975aab50f49faaaa581c` |
| SHA256 | `0b8af99acc6ea0b0b25c7cec0e0403836975c93e2153213cb74b2e823d9aaaf8` |
| Overall entropy | 7.341 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1765989342 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 466,944 | 6.636 | No |
| `.managed` | 1,077,248 | 6.441 | No |
| `hydrated` | 0 | 0.0 | No |
| `.rdata` | 1,853,952 | 7.632 | ⚠️ Yes |
| `.data` | 8,704 | 3.797 | No |
| `.pdata` | 100,864 | 6.167 | No |
| `.rsrc` | 1,024 | 4.993 | No |
| `.reloc` | 2,048 | 5.099 | No |

### Imports

**ADVAPI32.dll**: `RegCloseKey`, `RegEnumKeyExW`, `RegEnumValueW`, `RegOpenKeyExW`, `RegQueryValueExW`, `OpenProcessToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`
**bcrypt.dll**: `BCryptGenRandom`, `BCryptCreateHash`, `BCryptFinishHash`, `BCryptGetProperty`, `BCryptHashData`, `BCryptOpenAlgorithmProvider`, `BCryptCloseAlgorithmProvider`, `BCryptDestroyHash`
**KERNEL32.dll**: `TlsFree`, `TlsSetValue`, `TlsGetValue`, `TlsAlloc`, `InitializeCriticalSectionAndSpinCount`, `EncodePointer`, `RaiseException`, `RtlPcToFileHeader`, `QueryPerformanceCounter`, `GetStdHandle`, `RaiseFailFastException`, `TzSpecificLocalTimeToSystemTime`, `SystemTimeToFileTime`, `FileTimeToSystemTime`, `GetSystemTime`
**ole32.dll**: `CoGetApartmentType`, `CoCreateGuid`, `CoWaitForMultipleHandles`, `CoUninitialize`, `CoInitializeEx`
**USER32.dll**: `LoadStringW`
**api-ms-win-crt-math-l1-1-0.dll**: `modf`, `__setusermatherr`, `cos`, `tan`, `sin`, `pow`, `ceil`, `floor`
**api-ms-win-crt-heap-l1-1-0.dll**: `calloc`, `free`, `_set_new_mode`, `_callnewh`, `malloc`
**api-ms-win-crt-string-l1-1-0.dll**: `wcsncmp`, `strcpy_s`, `strncpy_s`, `strlen`, `strcmp`, `_stricmp`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_register_thread_local_exe_atexit_callback`, `abort`, `_initterm`, `_c_exit`, `_cexit`, `__p___wargv`, `__p___argc`, `_exit`, `exit`, `_initterm_e`, `_get_initial_wide_environment`, `_initialize_wide_environment`, `_configure_wide_argv`, `terminate`, `_crt_atexit`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__p__commode`, `__stdio_common_vsprintf_s`, `__stdio_common_vfprintf`, `__stdio_common_vsscanf`, `__acrt_iob_func`, `_set_fmode`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

## Extracted Strings

Total strings found: **12303** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.managed
`hydrated 
.rdata
@.data
.pdata
@.rsrc
@.reloc
AQAWAVAUATWVSh
L$XAQL
0]AZAZ[^_A\A]A^A_AZ
0]AZAZ[^_A\A]A^A_AZ
AQAWAVAUATWVSh
L$XAQL
0]AZAZ[^_A\A]A^A_AZ
0]AZAZ[^_A\A]A^A_AZ
fffffff
rfH;}
rfH;z
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
|$ AVH
|$ AVH
WATAUAVAWH
 A_A^A]A\_
PAWAVAUATWVSQRUH
8]XX[^_A\A]A^A_XX
8]XX[^_A\A]A^A_XXH
QAWAVAUATWVSh
0]AZAZ[^_A\A]A^A_AZ
L+A L;
A(H+Q H;
|$ AVH
UVWATAUAVAWH
A_A^A]A\_^]
|$ AVH
SATAUAWH
hA_A]A\[
@WAUAVAWH
(A_A^A]_
(A_A^A]_
|$ ATAVAWH
0A_A^A\
VWATAUAVAWH
A_A^A]A\_^
|$ AVH
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
SUVWATAUAVH
{H9|$ t
@A^A]A\_^][
SWAUAVH
8A^A]_[
|$ AVL
|$ AVL
|$ AVH
VAVAWH
 A_A^^
\$Dt
A
d$P9AXs7
T$Hu:A
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140001d7a` | `0x140001d7a` | 972529 | ✓ |
| `fcn.140144cd0` | `0x140144cd0` | 830721 | ✓ |
| `fcn.1400b04e0` | `0x1400b04e0` | 608545 | ✓ |
| `fcn.14000da70` | `0x14000da70` | 387556 | ✓ |
| `fcn.1400ef990` | `0x1400ef990` | 277919 | ✓ |
| `fcn.1400c9150` | `0x1400c9150` | 275959 | ✓ |
| `fcn.140167620` | `0x140167620` | 243048 | ✓ |
| `fcn.140045f10` | `0x140045f10` | 227717 | ✓ |
| `fcn.140045f20` | `0x140045f20` | 226198 | ✓ |
| `fcn.140045d30` | `0x140045d30` | 225233 | ✓ |
| `fcn.140045ef0` | `0x140045ef0` | 224714 | ✓ |
| `fcn.140045f90` | `0x140045f90` | 222869 | ✓ |
| `fcn.1400c68c0` | `0x1400c68c0` | 217301 | ✓ |
| `fcn.140045ee0` | `0x140045ee0` | 203173 | ✓ |
| `fcn.14010c350` | `0x14010c350` | 189295 | ✓ |
| `fcn.1400fc9f0` | `0x1400fc9f0` | 186889 | ✓ |
| `fcn.1400fc8c0` | `0x1400fc8c0` | 186485 | ✓ |
| `fcn.14003fe10` | `0x14003fe10` | 115591 | ✓ |
| `fcn.1400d9cc0` | `0x1400d9cc0` | 94274 | ✓ |
| `fcn.14004aa90` | `0x14004aa90` | 91887 | ✓ |
| `fcn.140027920` | `0x140027920` | 86671 | ✓ |
| `fcn.1400dd100` | `0x1400dd100` | 82058 | ✓ |
| `fcn.140014410` | `0x140014410` | 56165 | ✓ |
| `fcn.140048250` | `0x140048250` | 52747 | ✓ |
| `fcn.140003a40` | `0x140003a40` | 40923 | ✓ |
| `fcn.140003be0` | `0x140003be0` | 40150 | ✓ |
| `fcn.1400046a0` | `0x1400046a0` | 38359 | ✓ |
| `fcn.140004730` | `0x140004730` | 37623 | ✓ |
| `fcn.140004810` | `0x140004810` | 35771 | ✓ |
| `fcn.140004b60` | `0x140004b60` | 34093 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001d7a.c`](code/fcn.140001d7a.c)
- [`code/fcn.140003a40.c`](code/fcn.140003a40.c)
- [`code/fcn.140003be0.c`](code/fcn.140003be0.c)
- [`code/fcn.1400046a0.c`](code/fcn.1400046a0.c)
- [`code/fcn.140004730.c`](code/fcn.140004730.c)
- [`code/fcn.140004810.c`](code/fcn.140004810.c)
- [`code/fcn.140004b60.c`](code/fcn.140004b60.c)
- [`code/fcn.14000da70.c`](code/fcn.14000da70.c)
- [`code/fcn.140014410.c`](code/fcn.140014410.c)
- [`code/fcn.140027920.c`](code/fcn.140027920.c)
- [`code/fcn.14003fe10.c`](code/fcn.14003fe10.c)
- [`code/fcn.140045d30.c`](code/fcn.140045d30.c)
- [`code/fcn.140045ee0.c`](code/fcn.140045ee0.c)
- [`code/fcn.140045ef0.c`](code/fcn.140045ef0.c)
- [`code/fcn.140045f10.c`](code/fcn.140045f10.c)
- [`code/fcn.140045f20.c`](code/fcn.140045f20.c)
- [`code/fcn.140045f90.c`](code/fcn.140045f90.c)
- [`code/fcn.140048250.c`](code/fcn.140048250.c)
- [`code/fcn.14004aa90.c`](code/fcn.14004aa90.c)
- [`code/fcn.1400b04e0.c`](code/fcn.1400b04e0.c)
- [`code/fcn.1400c68c0.c`](code/fcn.1400c68c0.c)
- [`code/fcn.1400c9150.c`](code/fcn.1400c9150.c)
- [`code/fcn.1400d9cc0.c`](code/fcn.1400d9cc0.c)
- [`code/fcn.1400dd100.c`](code/fcn.1400dd100.c)
- [`code/fcn.1400ef990.c`](code/fcn.1400ef990.c)
- [`code/fcn.1400fc8c0.c`](code/fcn.1400fc8c0.c)
- [`code/fcn.1400fc9f0.c`](code/fcn.1400fc9f0.c)
- [`code/fcn.14010c350.c`](code/fcn.14010c350.c)
- [`code/fcn.140144cd0.c`](code/fcn.140144cd0.c)
- [`code/fcn.140167620.c`](code/fcn.140167620.c)

## Behavioral Analysis

This final chunk of disassembly completes the picture, transitioning our understanding from "advanced packer" to a **sophisticated, multi-stage architectural obfuscator.**

The final data confirms that the "Arithmetic Maze" isn't just a series of random calculations; it is a highly structured system for building the internal components of a custom Virtual Machine (VM) or an Execution Engine.

---

### **Final Technical Analysis**

#### **1. The "Transformation Gateways" (The Switch Case Logic)**
The large `switch` block (containing cases like `0x140050370`, `0x140050375`, and `0x140050384`) acts as the **core processing engine** of the packer.
*   **SIMD-Driven Mutation:** Each case is a "gateway." Instead of using standard XOR/ADD loops, it uses complex SIMD chains (`vpshufd`, `vpmaxsd`, `vpminsd`, and `vpblendd`). 
*   **Logic Synthesis:** These aren't just "decoding" the payload; they are performing **mathematical synthesis**. The packer is using the hardware’s vector processing capabilities to calculate complex state values that will eventually define the behavior of the VM. The repeated use of `vpblendd` with different constants (e.g., `0xaa`, `0xcc`, `0xf0`) suggests a way to perform multi-way branching or conditional logic without using a single jump instruction—further evading heuristic analysis.

#### **2. State Machine Construction (`arg2` population)**
The repeated assignments into the `arg2` buffer (e.g., `*(arg2 + 0x100)`, `*(arg2 + 0x120)`) are now confirmed as the construction of a **Control Block (CB)** or a **Virtual Instruction Set Architecture (V-ISA)** table.
*   **Buffer Mapping:** Each offset in `arg2` likely corresponds to a specific component: one block for the opcode handler, another for the stack pointer/frame manager, and another for the jump-table of the VM's "virtual" instructions.
*   **Intermediate Transformation:** The code doesn't just decrypt data into `arg2`; it passes raw data through several SIMD stages before placing it in its final home in `arg2`. This ensures that even if an analyst captures a piece of memory, they are looking at a *transformed state*, not the original malicious payload.

#### **3. The Transition Zone (Sorting and Linking)**
The logic following the switch cases (specifically the block involving `uVar35` and the `do...while` loops) represents the **transition from packer to loader.**
*   **Complexity Hidden in Standard Logic:** These loops appear to be an implementation of a **sorting algorithm** (like Insertion Sort or Shell Sort). 
*   **Why is this here?** In high-end packers, these are often used to sort memory addresses of resolved APIs, align pointers for the jump table, or order sections of code that were intentionally scrambled in memory. This is where the packer "organizes" its findings before handing off control to the payload.

#### **4. The Final Hand-off (Linked List Navigation)**
The function `fcn.140003a40` shows a classic **linked list traversal** (`while ((puVar1[4] != arg1 ...))`).
*   **Internal Mapping:** This suggests the packer is traversing a linked list of "hooks" or "functions" within its own internal structure to find a safe point to jump. It’s essentially looking for the "front door" into the malicious code that has just been reconstructed in memory.

---

### **Finalized Suspicious Behavior Assessment**

*   **SIMD Logic Masking:** The packer uses `vpmax/vpmins` logic gates. This is a high-level evasion technique where the *intent* of the code (e.g., "If X, then do Y") is hidden inside a set of mathematical instructions that perform the exact same operation but are invisible to traditional "branch" detection tools.
*   **Multi-Stage State Construction:** By building the `arg2` structure incrementally, the packer ensures that no single part of the payload exists in its runnable form until the very last moment. It builds a *machine* (the VM) and then feeds it the *instructions*.
*   **Sophisticated Transition Mechanics:** The use of sorting algorithms and linked-list traversals to find jump points indicates that the packer is designed to frustrate automated "unpacking" tools that look for simple JMP or CALL instructions to the payload.

---

### **Final Summary for Incident Response**

The complexity of this packer puts it in the top tier of modern malware protection techniques (comparable to packers like *Themida* or custom-built protectors used by APT groups).

**Critical Indicators for Analysts:**
1.  **SIMD Logic Gates:** Any sequence involving `vpshufd`, `vpmaxsd`, and `vpblendd` in a loop without a clear branching jump should be flagged as **logic obfuscation.** It is being used to calculate internal state or keys.
2.  **The `arg2` Buffer:** This is the "brain." If you can identify the structure of this buffer, you can find where the VM's handlers and instruction tables are hidden. 
3.  **Transition Points:** The area involving sorting loops (the `do...while` blocks) is a critical transition zone. Analyzing the values being sorted may reveal the "ground truth" of what functions or addresses the malware intends to call.

**Recommended Tactics for Investigation:**
1.  **Dynamic Instrumentation (Triton/Frida):** Because the logic is so heavily obfuscated by SIMD math, manual de-obfuscation of these blocks is inefficient. Use a symbolic execution engine like **Triton** to "fold" the arithmetic and see what the final values in `arg2` actually represent.
2.  **Memory Snapshots:** Take memory dumps immediately before and after the `switch` block. Compare the contents of `arg2`. This will show you how the state table is built.
3.  **Hardware Breakpoints on `arg2`:** Set a hardware breakpoint on the memory region of `arg2`. Track which parts are being modified first; this often reveals the "boot" sequence of the internal VM.

**Final Evaluation:** **Extreme Complexity.** The packer utilizes advanced architectural obfuscation, SIMD-based logic gate substitution, and staged state construction to protect highly complex payloads. This is not a standard "off-the-shelf" packer but a highly customized tool designed to defeat both automated scanners and manual reverse engineering.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the technical analysis to the relevant MITRE ATT&CK techniques. The packer exhibits high-level evasion tactics characterized by complex logic obfuscation and virtualized execution.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of "Arithmetic Mazes," SIMD-driven mutation (e.g., `vpmaxsd`, `vpblendd`), and complex math to mask logic flow is a classic method of hiding the true intent of code from heuristic analysis. |
| **T1027** | Obfuscated Files or Information | The construction of a custom Virtual Machine (VM) and V-ISA structure represents a high-level "Virtualization" of code, ensuring that standard static analysis tools cannot easily follow the logic flow. |
| **T1568** | Dynamic Resolution | The use of link list traversal and jump table assembly to find "safe points" for hand-offs allows the malware to resolve critical function addresses at runtime rather than using direct calls. |

### **Analyst Notes:**
*   **SIMD Logic Masking (T1027):** This is particularly sophisticated because it replaces standard conditional branching (`Jcc` instructions) with mathematical operations, effectively "flattening" the execution path to bypass automated de-obfuscation tools.
*   **VM-based Packing:** The `arg2` buffer serves as the heart of a virtualized environment; this indicates that even if an analyst extracts the payload from memory, they will still face an additional layer of interpretation (the VM) before the actual malicious behavior is revealed.
*   **Transition Logic (T1568/T1027):** The sorting and linking logic in the "Transition Zone" specifically targets tools that look for common entry point indicators, forcing a manual analyst to work through complex data structures to find the original entry point (OEP).

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral reports, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contains highly obfuscated data/junk characters common in sophisticated packers; these did not yield any standard network indicators or clear file paths. The primary actionable intelligence is found within the Behavioral Analysis.

### **IP addresses / URLs / Domains**
*   *(None identified)*

### **File paths / Registry keys**
*   *(None identified)*

### **Mutex names / Named pipes**
*   *(None identified)*

### **Hashes**
*   *(None identified)*

### **Other artifacts (Behavioral & Technical Indicators)**
These indicators are used for signature-based detection (e.g., YARA rules) and identifying specific packer logic:

*   **SIMD Instruction Sequences:** The use of the following instructions in a loop to mask logic gates is a primary indicator of advanced "Arithmetic Maze" obfuscation:
    *   `vpshufd`
    *   `vpmaxsd`
    *   `vpminsd`
    *   `vpblendd` (specifically used with constants `0xaa`, `0xcc`, and `0xf0`)
*   **Specific Code Offsets/Switch Cases:** These identify the "Transformation Gateways" within the binary:
    *   `0x140050370`
    *   `0x140050375`
    *   `0x140050384`
*   **Internal Function Identifiers:** 
    *   `fcn.140003a40` (Identified as the linked list traversal/transition point).
*   **Memory Buffer Logic:** 
    *   `arg2` buffer construction at offsets `0x100` and `0x120`.

---

## Malware Family Classification

1. **Malware family:** custom
2. **Malware type:** loader
3. **Confidence:** High

4. **Key evidence:**
*   **Advanced Virtualization Architecture:** The analysis confirms the sample uses a "multi-stage architectural obfuscator" that builds a custom Virtual Machine (VM) and V-ISA structure (the `arg2` buffer) to execute its payload, effectively isolating the malicious logic from standard analysis tools.
*   **SIMD-based Logic Masking:** The use of complex SIMD instruction chains (`vpshufd`, `vpmaxsd`, `vpblendd`) to perform "mathematical synthesis" instead of traditional branching instructions is a high-level evasion technique designed to bypass heuristic detection and obscure the code's intent.
*   **Sophisticated Transition Mechanics:** The presence of sorting algorithms and linked-list traversal in the "Transition Zone" indicates a deliberate effort to hide the final hand-off point (OEP) from automated unpackers, characterizing it as a high-tier loader/protector comparable to tools like *Themida*.
