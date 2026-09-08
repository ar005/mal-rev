# Threat Analysis Report

**Generated:** 2026-09-06 23:39 UTC
**Sample:** `1543b9b955e4de15261dff926dbcb21ba40e22fc3be7d2fbad2b3af95b3c93d9_1543b9b955e4de15261dff926dbcb21ba40e22fc3be7d2fbad2b3af95b3c93d9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1543b9b955e4de15261dff926dbcb21ba40e22fc3be7d2fbad2b3af95b3c93d9_1543b9b955e4de15261dff926dbcb21ba40e22fc3be7d2fbad2b3af95b3c93d9.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 8 sections |
| Size | 2,245,120 bytes |
| MD5 | `878d6c6d9338e724c6e6e2d86d93a653` |
| SHA1 | `e0480b6dee4358df22488eb797c1f2fc96d84b06` |
| SHA256 | `1543b9b955e4de15261dff926dbcb21ba40e22fc3be7d2fbad2b3af95b3c93d9` |
| Overall entropy | 6.759 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1731915361 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 416,768 | 6.645 | No |
| `.managed` | 835,072 | 6.435 | No |
| `hydrated` | 0 | 0.0 | No |
| `.rdata` | 740,352 | 6.771 | No |
| `.data` | 8,192 | 3.629 | No |
| `.pdata` | 80,384 | 6.136 | No |
| `.rsrc` | 161,280 | 3.513 | No |
| `.reloc` | 2,048 | 4.899 | No |

### Imports

**ADVAPI32.dll**: `RegQueryValueExW`, `RegCloseKey`, `OpenProcessToken`, `LookupPrivilegeValueW`, `AdjustTokenPrivileges`, `RegEnumKeyExW`, `RegOpenKeyExW`
**bcrypt.dll**: `BCryptDestroyHash`, `BCryptGenRandom`, `BCryptGetProperty`, `BCryptFinishHash`, `BCryptCreateHash`, `BCryptCloseAlgorithmProvider`, `BCryptOpenAlgorithmProvider`, `BCryptHashData`
**KERNEL32.dll**: `TlsFree`, `TlsSetValue`, `TlsGetValue`, `TlsAlloc`, `InitializeCriticalSectionAndSpinCount`, `EncodePointer`, `RaiseException`, `RtlPcToFileHeader`, `SetLastError`, `GetLastError`, `LocalFree`, `GetProcAddress`, `LoadLibraryW`, `FreeLibrary`, `FormatMessageW`
**ole32.dll**: `CoTaskMemFree`, `CoTaskMemAlloc`, `CoUninitialize`, `CoGetApartmentType`, `CoWaitForMultipleHandles`, `CoInitializeEx`
**api-ms-win-crt-heap-l1-1-0.dll**: `malloc`, `_set_new_mode`, `_callnewh`, `free`, `calloc`
**api-ms-win-crt-math-l1-1-0.dll**: `modf`, `ceil`, `__setusermatherr`, `pow`
**api-ms-win-crt-string-l1-1-0.dll**: `wcsncmp`, `strcmp`, `_stricmp`, `strcpy_s`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-runtime-l1-1-0.dll**: `abort`, `_cexit`, `terminate`, `_crt_atexit`, `_register_onexit_function`, `_initialize_onexit_table`, `_register_thread_local_exe_atexit_callback`, `_seh_filter_exe`, `_c_exit`, `_set_app_type`, `_configure_wide_argv`, `_initialize_wide_environment`, `_get_initial_wide_environment`, `_initterm`, `_initterm_e`
**api-ms-win-crt-stdio-l1-1-0.dll**: `_set_fmode`, `__p__commode`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

### Exports

`DotNetRuntimeDebugHeader`

## Extracted Strings

Total strings found: **8904** (showing first 100)

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
uoH;_
rfH;^
riH;=b
r6H;w
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
SUVWATAUAVAWH
A_A^A]A\_^][
|$ AVH
L+A L;
A(H+Q H;
|$0t,J
SATAUAWH
hA_A]A\[
H93t	H
|$ AVH
WATAUAVAWH
 A_A^A]A\_
PAWAVAUATWVSQRUH
8]XX[^_A\A]A^A_XX
8]XX[^_A\A]A^A_XXH
QAWAVAUATWVSh
0]AZAZ[^_A\A]A^A_AZ
@UWAVAWH
(A_A^_]
(A_A^_]
H;9f!
tTH;8f!
|$ ATAVAWH
0A_A^A\
VWATAUAVAWL
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
SUVWATAUAVAWH
{H9|$ t
8A_A^A]A\_^][
SWAUAVH
8A^A]_[
|$ AVL
|$ AVL
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140001f96` | `0x140001f96` | 806325 | ✓ |
| `fcn.140001d70` | `0x140001d70` | 749637 | ✓ |
| `fcn.14010e890` | `0x14010e890` | 620545 | ✓ |
| `fcn.140094420` | `0x140094420` | 501041 | ✓ |
| `fcn.140131060` | `0x140131060` | 486412 | ✓ |
| `fcn.1400c7270` | `0x1400c7270` | 232639 | ✓ |
| `fcn.1400459d0` | `0x1400459d0` | 226485 | ✓ |
| `fcn.1400459e0` | `0x1400459e0` | 224982 | ✓ |
| `fcn.1400457f0` | `0x1400457f0` | 224017 | ✓ |
| `fcn.1400459b0` | `0x1400459b0` | 223498 | ✓ |
| `fcn.140045a50` | `0x140045a50` | 221653 | ✓ |
| `fcn.1400a0700` | `0x1400a0700` | 206197 | ✓ |
| `fcn.1400459a0` | `0x1400459a0` | 202501 | ✓ |
| `fcn.14006be10` | `0x14006be10` | 197469 | ✓ |
| `fcn.1400d3490` | `0x1400d3490` | 167733 | ✓ |
| `fcn.1400e0650` | `0x1400e0650` | 154223 | ✓ |
| `fcn.1400a4410` | `0x1400a4410` | 153687 | ✓ |
| `fcn.14004a540` | `0x14004a540` | 91615 | ✓ |
| `fcn.1400b9d80` | `0x1400b9d80` | 85987 | ✓ |
| `fcn.140027780` | `0x140027780` | 85562 | ✓ |
| `fcn.1400b7ea0` | `0x1400b7ea0` | 67394 | ✓ |
| `fcn.140047d90` | `0x140047d90` | 52331 | ✓ |
| `fcn.14007d800` | `0x14007d800` | 51889 | ✓ |
| `fcn.1400bc800` | `0x1400bc800` | 49322 | ✓ |
| `fcn.140003960` | `0x140003960` | 40554 | ✓ |
| `fcn.140003b00` | `0x140003b00` | 39868 | ✓ |
| `fcn.1400041c0` | `0x1400041c0` | 39442 | ✓ |
| `fcn.140004250` | `0x140004250` | 38329 | ✓ |
| `fcn.140004330` | `0x140004330` | 36530 | ✓ |
| `fcn.140004680` | `0x140004680` | 34855 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001d70.c`](code/fcn.140001d70.c)
- [`code/fcn.140001f96.c`](code/fcn.140001f96.c)
- [`code/fcn.140003960.c`](code/fcn.140003960.c)
- [`code/fcn.140003b00.c`](code/fcn.140003b00.c)
- [`code/fcn.1400041c0.c`](code/fcn.1400041c0.c)
- [`code/fcn.140004250.c`](code/fcn.140004250.c)
- [`code/fcn.140004330.c`](code/fcn.140004330.c)
- [`code/fcn.140004680.c`](code/fcn.140004680.c)
- [`code/fcn.140027780.c`](code/fcn.140027780.c)
- [`code/fcn.1400457f0.c`](code/fcn.1400457f0.c)
- [`code/fcn.1400459a0.c`](code/fcn.1400459a0.c)
- [`code/fcn.1400459b0.c`](code/fcn.1400459b0.c)
- [`code/fcn.1400459d0.c`](code/fcn.1400459d0.c)
- [`code/fcn.1400459e0.c`](code/fcn.1400459e0.c)
- [`code/fcn.140045a50.c`](code/fcn.140045a50.c)
- [`code/fcn.140047d90.c`](code/fcn.140047d90.c)
- [`code/fcn.14004a540.c`](code/fcn.14004a540.c)
- [`code/fcn.14006be10.c`](code/fcn.14006be10.c)
- [`code/fcn.14007d800.c`](code/fcn.14007d800.c)
- [`code/fcn.140094420.c`](code/fcn.140094420.c)
- [`code/fcn.1400a0700.c`](code/fcn.1400a0700.c)
- [`code/fcn.1400a4410.c`](code/fcn.1400a4410.c)
- [`code/fcn.1400b7ea0.c`](code/fcn.1400b7ea0.c)
- [`code/fcn.1400b9d80.c`](code/fcn.1400b9d80.c)
- [`code/fcn.1400bc800.c`](code/fcn.1400bc800.c)
- [`code/fcn.1400c7270.c`](code/fcn.1400c7270.c)
- [`code/fcn.1400d3490.c`](code/fcn.1400d3490.c)
- [`code/fcn.1400e0650.c`](code/fcn.1400e0650.c)
- [`code/fcn.14010e890.c`](code/fcn.14010e890.c)
- [`code/fcn.140131060.c`](code/fcn.140131060.c)

## Behavioral Analysis

This final chunk completes the picture of a highly sophisticated piece of malware utilizing **"Virtual Machine" (VM) protection architecture** combined with **"Branchless Logic"** and **Advanced Vector Extensions (AVX)** to obfuscate its core functionality.

Below is the updated and comprehensive analysis incorporating all 7 chunks of disassembly.

---

### Final Comprehensive Analysis: [Project - Advanced VM-Based Obfuscation]

#### 1. Core Architecture: The Custom Virtual Machine
The large `switch` statement (starting with `uVar35`) is confirmed as a **Dispatch Table**.
*   **How it works:** Instead of standard execution, the malware processes a "bytecode" internally. Each case in the switch represents an instruction.
*   **The Purpose:** This decouples the malicious logic from the underlying x64 assembly. To an automated scanner or human analyst, the code looks like a massive, repetitive loop of math rather than a coherent piece of functional code (like "download file" or "inject into process").

#### 2. The Mathematical Shield (AVX-based Obfuscation)
The heavy use of `vpminsd`, `vpmaxsd`, `vpshufd`, and `vpblendd` is the primary defense mechanism.
*   **Branchless Logic:** By using `vpblendd_avx2(auVar18, auVar24, 0xf0)`, the author is creating a **conditional move (CMOV)** without a branch instruction. In standard code, this would be an `if` statement. Because there is no jump (`Jcc`), automated symbolic execution tools (like Angr/Triton) cannot easily "fork" and explore different paths; they are forced to calculate the math for every possible outcome.
*   **Complexity Overload:** The repetition of these blocks suggests that multiple pieces of data (e.g., a DLL's header, its section table, and its entry point) are being processed through the *same* mathematical filter, just at different iterations of the loop.

#### 3. Decoupled Payload Reconstruction
The repetitive assignment to `*(arg2 + offset)` is highly significant:
*   **Buffer Building:** The buffer `arg2` is being treated as a **template for a raw executable file.** Every `0x10`, `0x20`, etc., represents an offset in a PE (Portable Executable) header or a memory map. 
*   **Just-in-Time Construction:** The payload isn't decrypted into memory all at once. It is being "constructed" piece by piece as it passes through the VM. This makes signature-based detection nearly impossible, as the full malicious payload does not exist in memory until the very final moment of execution.

#### 4. Multi-Stage Decryption & Logic Gates
Following the `switch` block, the code enters a series of "Decision Points" (e.g., `if (uVar35 < 0xa8)`).
*   **Hidden Paths:** The jump between `fcn.140045f10` and `fcn.140046b50` indicates that the malware may have different behaviors or payloads based on environmental checks (e.g., "Is a debugger present?" or "What is the system language?").
*   **Nested Complexity:** Even if an analyst simplifies the AVX math, they are immediately met with another layer of calls (`fcn.140050fd0`, `fcn.140051fc0`). These are likely helper functions to handle "messy" logic that doesn't fit into a clean mathematical model (like string manipulation or system checks).

---

### Updated Incident Response Findings

*   **Sophistication Level:** **High-Tier/State-Sponsered Style.** This is not a common "off the shelf" packer. The custom use of AVX for branchless logic indicates a high level of engineering intent to defeat automated analysis tools and advanced sandboxes.
*   **Anti-Analysis Techniques Identified:**
    1.  **Instruction Obfuscation:** Using AVX to replace standard conditional jumps (prevents static control flow graphing).
    2.  **Data-Stream Transformation:** The "Switch" loop transforms raw, encrypted data into a functional payload structure in memory.
    3.  **Dynamic Branching:** Utilizing conditions at the end of the VM block to choose between different final decryption routines.
*   **Risk Assessment:** Highly likely capable of evading standard EDR (Endpoint Detection and Response) solutions that rely on static signature matching or simple heuristic analysis of common packers.

---

### Advanced Analysis Recommendations

#### 1. Behavioral "Wait-and-See" Approach (Dynamic Analysis)
Because the math is designed to be hard for humans to solve, **do not waste time manually simplifying every AVX instruction.**
*   **Action:** Run the malware in a "sacrificial" sandbox with an instrumentation tool like **Intel PIN** or **x64dbg's trace**. 
*   **Goal:** Find the point where execution leaves the `switch` block and jumps into new memory. That is your **Original Entry Point (OEP)**.

#### 2. Memory Forensics & Dumping
Since the VM is "constructing" a payload in `arg2`, the most effective way to see what the malware actually does is to watch that specific memory region.
*   **Action:** Set a hardware breakpoint on the address of `arg2` (specifically, look for where it starts receiving significant writes).
*   **Goal:** When the VM completes its cycle, dump the contents of `arg2`. This will likely reveal a decrypted PE file or shellcode that can be analyzed in a disassembler like IDA Pro.

#### 3. Automated De-obfuscation Scripting
If you must perform static analysis:
*   **Action:** Write an IDAPython script to identify the pattern of `vpminsd` and `vpblend` sequences within the switch block.
*   **Goal:** Replace these long chains with a single comment or a "NOP" (No-Operation) if they can be proven to result in a constant. This will clean up the disassembly and allow you to see the logic flow more clearly.

#### 4. Identification of Key Logic Branches
Focus your analysis on the calls: `fcn.140045f10`, `fcn.140046b50`, and `fcn.140047d90`.
*   **Action:** These are "High-Value Targets." They occur after the complex math is done and are likely the final stages of unpacking or preparation before the malicious payload executes. Analysis of these functions will yield more information than analyzing 1,000 lines of AVX logic.

### Summary Table for SOC/IR Teams
| Component | Technique Identified | Purpose | Impact on Investigation |
| :--- | :--- | :--- | :--- |
| **Switch Block** | Custom VM Dispatcher | Hides core logic from static analysis | High - Requires dynamic dumping to see full intent. |
| **AVX Logic** | Branchless Math | Defeats Symbolic Execution/Automation | High - Makes manual "math-based" deobfuscation slow. |
| **Arg2 Buffer** | Payload Construction | Evades signature-based detection | Medium - Requires memory dumps at the correct time. |
| **Dual Call Path**| Conditional Decryption | Environment checks / Tailored payload | High - May hide features from sandboxes. |

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&K framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization | The malware employs a custom "Dispatch Table" and bytecode processing via a `switch` statement to hide its core logic from standard x64 disassembly. |
| **T1027** | Obfuscated Execution | The use of AVX-based branchless logic is designed to thwart automated symbolic execution and force manual, time-intensive analysis of the code's flow. |
| **T1028** | Sample Packing | The "just-in-time" construction of the payload in `arg2` ensures that the full malicious PE structure does not exist in memory until the final moment of execution, evading signature-based detection. |

---

## Indicators of Compromise

Based on my analysis of the provided strings and behavioral report, here is the extraction of Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided data contains significant information regarding the **malware's architecture** (Custom VM, AVX-based branchless logic, and multi-stage unpacking), but it does not contain traditional "network" or "host" IOCs such as IP addresses, URLs, or file paths. The strings provided appear to be obfuscated data fragments or internal jump tables rather than cleartext indicators.

---

### **Indicators of Compromise (IOCs)**

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (Note: The "arg2" mentioned in the analysis refers to a memory buffer, not a file path).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.* (The strings provided do not match standard MD5, SHA-1, or SHA-256 hash formats).

**Other artifacts**
*   **Internal Function Signatures:** The following internal function calls were identified as high-value execution points in the disassembly. While these are not network IOCs, they can be used to identify specific versions of this packer:
    *   `fcn.140045f10`
    *   `fcn.140046b50`
    *   `fcn.140047d90`
*   **Behavioral Signature (Logic Pattern):** 
    *   Use of `vpminsd`, `vpmaxsd`, `vpshufd`, and `vpblendd` for branchless logic to evade symbolic execution.
    *   Implementation of a **Custom VM Dispatch Table** using a large `switch` statement (variable `uVar35`).

---

### **Analyst Notes**
The "EXTRACTED STRINGS" section appears to contain high-entropy, obfuscated data or potentially and/or mutated instructions (e.g., `AQAWAVAUATWVSh`, `0]AZAZ[^_A\A]A^A_AZ`). These do not currently map to recognizable infrastructure. 

**Recommendation:** Since no network indicators were found in the static strings, I recommend performing a **dynamic analysis** of the sample while monitoring memory. The behavioral report indicates that the payload is constructed in `arg2` just before execution; capturing this specific moment will likely yield the "true" IOCs (decrypted C2 URLs and file paths) that are currently hidden by the VM layer.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Custom VM Architecture:** The sample utilizes a sophisticated "Dispatch Table" and bytecode interpretation (a large `switch` statement) to decouple malicious logic from standard x64 assembly, making it extremely difficult for automated systems to map its functionality.
*   **Advanced Obfuscation (AVX/Branchless):** The use of AVX instructions (`vpminsd`, `vpmaxsd`, etc.) to implement branchless logic specifically targets the failure of symbolic execution tools and hides decision-making from standard analysis.
*   **Just-in-Time Payload Construction:** The malware constructs a secondary payload in memory (the `arg2` buffer) piece-by-piece rather than decrypting it all at once, which is a hallmark of advanced loaders designed to evade signature-based detection and EDR systems.
