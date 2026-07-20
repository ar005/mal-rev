# Threat Analysis Report

**Generated:** 2026-07-19 05:25 UTC
**Sample:** `08d201dc0b7c8479b991ed7c8de98eacb3091cf71ba2ed5fd3d27c34a9bfd7b2_08d201dc0b7c8479b991ed7c8de98eacb3091cf71ba2ed5fd3d27c34a9bfd7b2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `08d201dc0b7c8479b991ed7c8de98eacb3091cf71ba2ed5fd3d27c34a9bfd7b2_08d201dc0b7c8479b991ed7c8de98eacb3091cf71ba2ed5fd3d27c34a9bfd7b2.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 8 sections |
| Size | 8,187,904 bytes |
| MD5 | `3ae6dc048a209b661ede685458707e60` |
| SHA1 | `d38f76aabd4cd7f10259c2cb69236117fb239312` |
| SHA256 | `08d201dc0b7c8479b991ed7c8de98eacb3091cf71ba2ed5fd3d27c34a9bfd7b2` |
| Overall entropy | 5.992 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1760143008 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 427,008 | 6.643 | No |
| `.managed` | 1,220,608 | 6.413 | No |
| `.rdata` | 6,197,248 | 5.258 | No |
| `.data` | 159,744 | 3.701 | No |
| `.pdata` | 116,736 | 6.272 | No |
| `_RDATA` | 512 | 3.322 | No |
| `.rsrc` | 2,560 | 3.933 | No |
| `.reloc` | 62,464 | 5.492 | No |

### Imports

**ADVAPI32.dll**: `RegOpenKeyExW`, `RegSetValueExW`, `RegCloseKey`, `RegEnumKeyExW`, `RegQueryValueExW`, `EventWrite`, `EventRegister`, `EventEnabled`, `OpenProcessToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`
**bcrypt.dll**: `BCryptGenRandom`
**KERNEL32.dll**: `RtlUnwind`, `TlsFree`, `SetLastError`, `CreateDirectoryW`, `GetLastError`, `CopyFileW`, `CreateFileW`, `WriteFile`, `CloseHandle`, `GetModuleHandleW`, `OpenProcess`, `ReadProcessMemory`, `VirtualProtectEx`, `WriteProcessMemory`, `LocalFree`
**ole32.dll**: `CoTaskMemAlloc`, `CoInitializeEx`, `CoWaitForMultipleHandles`, `CoGetApartmentType`, `CoTaskMemFree`, `CoCreateGuid`, `CoUninitialize`
**USER32.dll**: `LoadStringW`
**api-ms-win-crt-heap-l1-1-0.dll**: `calloc`, `_callnewh`, `free`, `malloc`
**api-ms-win-crt-math-l1-1-0.dll**: `modf`, `pow`, `ceil`
**api-ms-win-crt-string-l1-1-0.dll**: `strcpy_s`, `strcmp`, `_wcsicmp`, `wcsncmp`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_initialize_narrow_environment`, `abort`, `terminate`, `_cexit`, `_configure_narrow_argv`, `_crt_atexit`, `_execute_onexit_table`, `_initialize_onexit_table`, `_register_onexit_function`, `_initterm`, `_initterm_e`, `_seh_filter_dll`

### Exports

`00I7HEUrJ9BNI`, `0SpmIMeSeL9ZVPvYue2`, `0aByVFiME7DM4vl3kUOz7`, `16c49RTs0oG0RaKTHSYNHfs`, `1f6fJrAjhq3oy1M8dukffC0A`, `2B2oR3IEGJWTmUH1KsUxpC7uf2FbSRWk`, `3vu3MN2hl`, `4BAIZSrWjmYgmB`, `557iow4HBFE8Qpy`, `5AjoyEHfjDK0Olm76`, `5SHN90E46X5LZOG81w3dUY8ao2`, `5iF2ByQlM4HcgRiBwnjeH9P8mg4`, `6UwuSRjpeA`, `6lziG8IM25W9wQ`, `8E2ATkpv2wCEv6qAqHXrAFFpH61qs`, `8gBYBwot4`, `95R8oSjTZMOe7rVC8`, `9GC27s2AAZlbXWRw`, `9crFAwDfCE0sRnjsGrmcZORhJZvRvq`, `9nE3L6B51DaD6QirsoBircsgQ93Nv`, `AneTz7JbXCKkMXoZIuaD`, `BWoYJhlXgKEJpN19f`, `BY1onLgHYZNKxbfr`, `C3SENJqEhXg7E5fYsuo5kK`, `D2NzpGPEU`, `D7GUbm37gY49rc9YV0QyaKpfiRrhVs`, `ERihmdkrLuHcXx4zNj0je0vVqtiNL0u`, `FslaMLGnTwI8QQnXS2IdiT`, `G2LXgRoYpIiBTDp6xg3rBfkj`, `GNMcskdmCjL`, `GjVscgQUJ9Q15GKKTsuywsAX`, `HKynQYo6pZ99D`, `IfTXRR58OgM3`, `ImqjSxFE6`, `J79kVH3iik3N`, `J7LA9kgB`, `JwGT6c86TnHZ4AHcfrlq4h70fRRX5o`, `K8MB0SRJ5fWsB`, `KZp9veU4p51`, `LUo7i7fEl6WjQrZtbQQn3F`, `LzOxdDBhDy9mAaq`, `M2X5eXjv6mIbn8IVEfQ7pB`, `M5plGd53LIYdlSNI5AsUdriyxPaX6`, `Mp6kixBytvcBq`, `N32e6alfPoLh6jrpk8hlkM1xXrzr7qA`, `N3LA7g3j4eypAIYsMdMtH`, `N9v5x4L4`, `O9eaVZrtztXC`, `OJLjxgEWnPPhDHll8oNLVgYiIs1`, `PpMKZDlOGV1dmcSw93GZRKDKjT57UQ61`

## Extracted Strings

Total strings found: **13055** (showing first 100)

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
H;ftz
r+H;etz
fffffff
|$ AVH
|$ AVH
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
L+A0L;
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
H;ynr
H;*gr
tTH;)gr
tKH;@_r
t<H;/_r
t3H;6_r
t*H;5_r
H;4_r
H;,_r
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1800ed0c0` | `0x1800ed0c0` | 570353 | ✓ |
| `fcn.1800108f0` | `0x1800108f0` | 334434 | ✓ |
| `fcn.180139e30` | `0x180139e30` | 226351 | ✓ |
| `fcn.1800472a0` | `0x1800472a0` | 217317 | ✓ |
| `fcn.1800472b0` | `0x1800472b0` | 216022 | ✓ |
| `fcn.1800470c0` | `0x1800470c0` | 215137 | ✓ |
| `fcn.180047280` | `0x180047280` | 214730 | ✓ |
| `fcn.180047320` | `0x180047320` | 212581 | ✓ |
| `fcn.180047270` | `0x180047270` | 204837 | ✓ |
| `fcn.18004b8f0` | `0x18004b8f0` | 91567 | ✓ |
| `fcn.18002b190` | `0x18002b190` | 79774 | ✓ |
| `fcn.1800301f0` | `0x1800301f0` | 66134 | ✓ |
| `fcn.180020f20` | `0x180020f20` | 60978 | ✓ |
| `fcn.180018790` | `0x180018790` | 57482 | ✓ |
| `fcn.180097000` | `0x180097000` | 53653 | ✓ |
| `fcn.1800491d0` | `0x1800491d0` | 52139 | ✓ |
| `fcn.180015120` | `0x180015120` | 50725 | ✓ |
| `fcn.180085f60` | `0x180085f60` | 49253 | ✓ |
| `fcn.180004310` | `0x180004310` | 47371 | ✓ |
| `fcn.180004480` | `0x180004480` | 46694 | ✓ |
| `fcn.180005280` | `0x180005280` | 44372 | ✓ |
| `fcn.18000a750` | `0x18000a750` | 43642 | ✓ |
| `fcn.18000a7e0` | `0x18000a7e0` | 43617 | ✓ |
| `fcn.180005cb0` | `0x180005cb0` | 38929 | ✓ |
| `fcn.180006970` | `0x180006970` | 37575 | ✓ |
| `fcn.18000a4a0` | `0x18000a4a0` | 30636 | ✓ |
| `fcn.1801115b0` | `0x1801115b0` | 28718 | ✓ |
| `fcn.18000b0c0` | `0x18000b0c0` | 27752 | ✓ |
| `fcn.180095da0` | `0x180095da0` | 26313 | ✓ |
| `fcn.1800136a0` | `0x1800136a0` | 24828 | ✓ |

### Decompiled Code Files

- [`code/fcn.180004310.c`](code/fcn.180004310.c)
- [`code/fcn.180004480.c`](code/fcn.180004480.c)
- [`code/fcn.180005280.c`](code/fcn.180005280.c)
- [`code/fcn.180005cb0.c`](code/fcn.180005cb0.c)
- [`code/fcn.180006970.c`](code/fcn.180006970.c)
- [`code/fcn.18000a4a0.c`](code/fcn.18000a4a0.c)
- [`code/fcn.18000a750.c`](code/fcn.18000a750.c)
- [`code/fcn.18000a7e0.c`](code/fcn.18000a7e0.c)
- [`code/fcn.18000b0c0.c`](code/fcn.18000b0c0.c)
- [`code/fcn.1800108f0.c`](code/fcn.1800108f0.c)
- [`code/fcn.1800136a0.c`](code/fcn.1800136a0.c)
- [`code/fcn.180015120.c`](code/fcn.180015120.c)
- [`code/fcn.180018790.c`](code/fcn.180018790.c)
- [`code/fcn.180020f20.c`](code/fcn.180020f20.c)
- [`code/fcn.18002b190.c`](code/fcn.18002b190.c)
- [`code/fcn.1800301f0.c`](code/fcn.1800301f0.c)
- [`code/fcn.1800470c0.c`](code/fcn.1800470c0.c)
- [`code/fcn.180047270.c`](code/fcn.180047270.c)
- [`code/fcn.180047280.c`](code/fcn.180047280.c)
- [`code/fcn.1800472a0.c`](code/fcn.1800472a0.c)
- [`code/fcn.1800472b0.c`](code/fcn.1800472b0.c)
- [`code/fcn.180047320.c`](code/fcn.180047320.c)
- [`code/fcn.1800491d0.c`](code/fcn.1800491d0.c)
- [`code/fcn.18004b8f0.c`](code/fcn.18004b8f0.c)
- [`code/fcn.180085f60.c`](code/fcn.180085f60.c)
- [`code/fcn.180095da0.c`](code/fcn.180095da0.c)
- [`code/fcn.180097000.c`](code/fcn.180097000.c)
- [`code/fcn.1800ed0c0.c`](code/fcn.1800ed0c0.c)
- [`code/fcn.1801115b0.c`](code/fcn.1801115b0.c)
- [`code/fcn.180139e30.c`](code/fcn.180139e30.c)

## Behavioral Analysis

This latest disassembly confirms and significantly deepens our understanding of the protection's architecture. We are no longer looking at "complex code"—we are looking at a **highly engineered Virtual Machine (VM) execution pipeline** that utilizes specific mathematical primitives to flatten control flow.

Here is the updated analysis incorporating the new data from chunk 7/7.

---

### Updated Analysis Report: The VM Architecture & State Mapping

#### 1. The "Register Map" Discovery (`arg2` as a Virtual Register File)
In this chunk, we see a massive block of assignments to `arg2`. This is no longer just a buffer; it is the **VM's Register File.**

*   **The Observation:** After a series of intense SIMD calculations (like those in case `0x1800510c3`), the code performs a "dump" into `arg2`:
    *   `*(arg2 + 0x40) = auStack_180._0_8_;`
    *   `*(arg2 + 0x60) = auStack_160._0_8_;`
    *   `*(arg2 + 0x80) = auStack_140._0_8_;`
*   **The Significance:** Every offset in `arg2` represents a **logical state** or a **virtual register**. When the VM's "Instruction Pointer" moves, it calculates new values for these specific slots. The fact that they are updated via high-complexity SIMD math means that even the calculation of a *single* internal flag is hidden behind layers of arithmetic.
*   **Analytical Conclusion:** To understand what the program is doing, we must ignore the "math" and instead map which offsets in `arg2` change during specific stages. For example, if `arg2 + 0x40` consistently changes only when a network packet is processed, then `0x40` corresponds to a "Network State" register.

#### 2. Evolution of "SIMD-as-Logic": The Decision Tree Erasure
The repeated patterns of `vpminsd_avx2`, `vpmaxsd__avx2`, and `vpblendd_avx2` are used to construct **Branchless Logic Trees.**

*   **The Technique:** Standard code uses: `if (a > b) { x = a; } else { x = b; }`. This creates a branch in the Control Flow Graph (CFG).
*   **The Obfuscation:** They use: `x = vpmaxsd_avx2(a, b)`. This performs the same logic but produces a **straight line** in the CFG. 
*   **Complexity Multiplier:** By chaining these together with `vpshufd` (shuffling data) and `vpermpd` (permuting), they can create complex nested "if-else" structures that appear to a decompiler as hundreds of lines of SIMD math. They are effectively **simulating a CPU's branch predictor with mathematical gates.**

#### 3. Micro-Handler Orchestration
The calls to `fcn.180052380`, `fcn.180053360`, and `fcn.180052200` represent **Micro-Handlers**.

*   **Observation:** These functions are called between the heavy SIMD blocks. 
*   **The Role:** While the "Main Switch" (`fcn.1800491d0`) handles the standard logic of the VM, these Micro-Handlers handle "Edge Cases" or "System Interfacing." When the VM reaches a point where it needs to perform an operation that isn't just pure math (like a memory swap, a stack adjustment, or a complex multi-step derivation), it jumps into one of these handlers.
*   **The Strategy:** This separates the **Obfuscation Layer** (the SIMD mess) from the **Functional Layer** (the micro-handlers). The logic inside the micro-handlers is likely much simpler but is "hidden" by the fact that its input and output are always processed through the "SIMD Filter."

#### 4. Decoupling of Logic and Timing
The appearance of `fcn.180006970` calling `GetTickCount64` and `fcn.180052380` suggests that the VM is performing **internal timing checks.**

*   **Analysis:** The VM likely measures how long certain "blocks" take to execute. If a debugger is attached, or if the "SIMD Logic Gate" takes too many cycles (due to stepping), the VM detects this and alters its internal state (`arg2`).
*   **Technical Insight:** This indicates that the protection isn't just trying to hide *what* it does; it’s trying to hide *how fast* it is doing it.

---

### Summary for Analyst: Strategic Synthesis

We have moved from "Deciphering Code" to "Decoding a Protocol." The core logic of this program is no longer visible in the disassembly because it has been **translated into a state machine.**

#### Key Technical Findings (Consolidated):
1.  **The Instruction Dispatcher:** `fcn.1800491d0` is the heart of the VM. Every case in that switch is an "Instruction" in the custom bytecode.
2.  **Branchless State Transformation:** The use of SIMD (`vpminsd`/`vpmaxsd`) means the program's logic flow is **linearized**. There are no "branches" for a decompiler to follow; there is only a mountain of math that eventually results in a new state.
3.  **State Map (arg2):** `arg2` is the primary vehicle for data. We should focus on tracking how values at specific offsets (`0x40`, `0x80`, `0x100`) change over time. **These are the "true" variables of the program.**
4.  **Micro-Handler Isolation:** Functions like `fcn.180052380` handle complex state transitions that aren't easily expressed in simple SIMD math.

#### Recommended Strategy for De-obfuscation:
*   **State Logging (The "North Star"):** Instead of trying to simplify the SIMD math manually, use a debugger/tracer to log the contents of `arg2` every time `fcn.1800491d0` is called. 
    *   By comparing the state of `arg2` before and after various "Cases," you can reconstruct the logic flow (e.g., "When Case X is hit, the value at 0x40 always flips from 0 to 1").
*   **Identify State Changes:** Focus on finding which "Case" in the switch corresponds to critical events (authentication checks, decryption keys, etc.). Each time a jump occurs in the original logic, it will manifest as a specific sequence of "Cases" being hit and `arg2` being updated.
*   **Filter the Noise:** Treat everything between the assignments to `arg2` as **Computational Noise.** It is designed to waste your time; only the change in state (the values in `arg2`) matters for understanding the program's functionality.

#### Conclusion:
The complexity of this system is **structural**, not just mathematical. The authors have built a "black box" where the logic is buried inside a SIMD-processing engine. To break it, we must stop looking at the gears (the SIMD instructions) and start looking at the output of the machine (the changes in the `arg2` state buffer).

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors described in your report to the appropriate MITRE ATT&C techniques. The majority of these behaviors fall under the **Defense Evasion** tactic, specifically utilizing advanced obfuscation and anti-analysis techniques typically found in high-end packers and "protectors."

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1055 | Packer | The use of a custom Virtual Machine (VM) to host the core logic hides the actual functionality from static analysis. |
| T1055 | Packer | The implementation of "Branchless Logic" via SIMD instructions replaces standard conditional jumps with math, flattening the Control Flow Graph (CFG). |
| T1055 | Packer | The use of "Micro-Handlers" segments the logic into smaller, distinct functions to isolate the core functionality from the obfuscation layer. |
| T1036 | Masquerade | *(Note: While often associated with Masquerade)*, the timing checks using `GetTickCount64` are intended to hide the program's behavior by detecting if it is being run in a controlled analysis environment or under a debugger. |

### Analytical Note
While all four behaviors are technically different techniques of "obfuscation," they are often grouped together in report generation as part of **T1055 (Packer)** because they characterize the methodology used by sophisticated protectors to shield malware from reverse engineering. 

The transition from a standard control flow to a "State Map" (the `arg2` register file) is a hallmark of advanced evasion, where the analyst's primary hurdle shifts from reading instructions to decoding a custom protocol.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the categorized list of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*None identified.*

### **File paths / Registry keys**
*None identified.* (Note: Memory offsets like `arg2 + 0x40` are internal to the process and do not constitute file system or registry IOCs.)

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None identified.* (The scrambled strings provided in the "Extracted Strings" section appear to be obfuscated bytecode, encrypted data, or junk data used for de-obfuscation; they do not conform to standard MD5/SHA1/SHA256 formats.)

### **Other artifacts**
*   **Internal Function Offsets (Potential signature of a specific build):** 
    *   `fcn.1800510c3` (SIMD calculation block)
    *   `fcn.180052380` (Micro-handler / Timing check)
    *   `fcn.180053360` (Micro-handler)
    *   `fcn.180052200` (Micro-handler)
    *   `fcn.1800491d0` (Main VM Dispatcher/Switch)
    *   `fcn.180006970` (Timing check logic)
*   **Anti-Analysis Techniques:** 
    *   **Time-based Evasion:** Use of `GetTickCount64` to detect debugger presence or execution delays.
    *   **Branchless Logic:** Extensive use of AVX2 instructions (`vpminsd_avx2`, `vpmaxsd_avx2`, `vpblendd_avx2`) to flatten the control flow graph (CFG) and hide logical branches.
    *   **Virtual Machine (VM) Architecture:** A highly engineered, custom VM execution pipeline used to wrap core functionality.

---
**Analyst Note:** While no traditional network or file system IOCs were identified in this sample, the analysis reveals a high level of sophistication. The malware utilizes a **custom Virtual Machine (VM)** and **SIMD-based obfuscation**, which are characteristics often associated with advanced persistent threats (APTs) or highly sophisticated loaders/protectors to evade static and dynamic analysis.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Virtual Machine (VM) Architecture:** The analysis confirms the sample uses a highly engineered VM execution pipeline where core logic is translated into a state machine, using `arg2` as a "Register File" to mask the actual program flow.
*   **Advanced Branchless Logic:** The use of AVX2 SIMD instructions (`vpminsd`, `vpmaxsd`) to replace standard conditional branches creates a flattened Control Flow Graph (CFG), specifically designed to defeat automated analysis and manual de-obfuscation.
*   **Evasive Anti-Analysis Techniques:** The inclusion of timing checks via `GetTickCount64` and the decoupling of functional "Micro-Handlers" from the obfuscation layer indicate a high level of sophistication intended to hide the payload's true purpose (common in advanced loaders/protectors).
