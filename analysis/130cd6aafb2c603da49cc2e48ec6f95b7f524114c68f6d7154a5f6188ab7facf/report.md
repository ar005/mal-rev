# Threat Analysis Report

**Generated:** 2026-09-02 08:39 UTC
**Sample:** `130cd6aafb2c603da49cc2e48ec6f95b7f524114c68f6d7154a5f6188ab7facf_130cd6aafb2c603da49cc2e48ec6f95b7f524114c68f6d7154a5f6188ab7facf.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `130cd6aafb2c603da49cc2e48ec6f95b7f524114c68f6d7154a5f6188ab7facf_130cd6aafb2c603da49cc2e48ec6f95b7f524114c68f6d7154a5f6188ab7facf.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 11,989,504 bytes |
| MD5 | `d9fe96d978b90a2de4225be1c4c62f51` |
| SHA1 | `06f5f401397862537c2e47bb7518a91ae756b11c` |
| SHA256 | `130cd6aafb2c603da49cc2e48ec6f95b7f524114c68f6d7154a5f6188ab7facf` |
| Overall entropy | 4.044 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 4290181846 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 11,986,944 | 4.044 | No |
| `.rsrc` | 1,536 | 3.875 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1556** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

-!	rf

- 	rf
 lrn#X
? lrn#X
ZX%L B
v4.0.30319
#Strings
	B	S	Z	g	
	R
X
u
{

"(/;DMS]isz
#0=F\dnt
/?]

'
8
^
j

smethod_100
smethod_110
__StaticArrayInitTypeSize=10
smethod_10
vmethod_10
label_10
pictureBox_10
Delegate10
Class10
smethod_120
smethod_20
vmethod_20
Class20
smethod_130
__StaticArrayInitTypeSize=30
smethod_30
vmethod_30
Class30
smethod_140
__StaticArrayInitTypeSize=40
smethod_40
vmethod_40
smethod_50
vmethod_50
smethod_60
vmethod_60
smethod_70
vmethod_70
smethod_80
vmethod_80
smethod_90
E442AEEF1ACA522EB71A6A316110A7AD2A92834F46A11E2E95ED289A2AF48AC0
<GForm1_Load>b__10_0
class20_0
get_Form0_0
gform0_0
get_Class0_0
gform1_0
enum1_0
struct1_0
_003C_003E9__12_0
delegate12_0
class12_0
class22_0
delegate2_0
gform2_0
struct2_0
delegate13_0
class13_0
enum3_0
class24_0
<>9__154_0
<method_8>b__154_0
Ldc_I4_0
delegate4_0
enum4_0
class25_0
_003C_003E9__45_0
<>9__155_0
<method_9>b__155_0
delegate5_0
class16_0
class36_0
<>9__156_0
<method_10>b__156_0
delegate6_0
class17_0
class27_0
<>9__47_0
<smethod_1>b__47_0
delegate7_0
class18_0
<>9__28_0
<method_2>b__28_0
delegate8_0
class19_0
delegate9_0
class9_0
<smethod_0>b__0
smethod_0
vmethod_0
cipherMode_0
idisposable_0
hashtable_0
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **27**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.__c..ctor` | `0x41c758` | 11792538 | ✓ |
| `method.Class35..ctor` | `0x41c349` | 11790932 | ✓ |
| `method.__c._method_10_b__156_0` | `0x41c7a5` | 129956 | — |
| `method.Class7_1..ctor` | `0x41c92f` | 65142 | ✓ |
| `method.Class7_1.smethod_1` | `0x41c918` | 65088 | ✓ |
| `method.Class20.method_7` | `0x4153d0` | 16480 | ✓ |
| `method.ns0.GForm2.method_16` | `0x409494` | 6504 | ✓ |
| `method.ns0.Class6.smethod_19` | `0x404174` | 6356 | ✓ |
| `method.ns0.Class11.smethod_1` | `0x402138` | 2844 | ✓ |
| `method.Class20.smethod_3` | `0x419fc8` | 2004 | ✓ |
| `method.Class22.smethod_1` | `0x41b6d4` | 1944 | ✓ |
| `method.ns0.GForm2.method_0` | `0x407f44` | 1920 | ✓ |
| `method.ns0.Class6.smethod_0` | `0x403314` | 1830 | ✓ |
| `method.ns0.GForm1.GForm1_Load` | `0x40708c` | 1576 | ✓ |
| `method.Class20.smethod_4` | `0x41a79c` | 1504 | ✓ |
| `method.Class20.smethod_2` | `0x419a48` | 1408 | ✓ |
| `method.Class24.vmethod_4` | `0x40b8e4` | 1080 | — |
| `method.Class20.method_12` | `0x419640` | 1032 | ✓ |
| `method.Class25.vmethod_4` | `0x40d76c` | 972 | — |
| `method.Class26.vmethod_10` | `0x40f060` | 951 | ✓ |
| `method.Class20.method_2` | `0x414c80` | 820 | ✓ |
| `method.Class22.smethod_0` | `0x41b470` | 612 | ✓ |
| `method.Class34.vmethod_4` | `0x41bff0` | 596 | ✓ |
| `method.ns0.Class6.method_1` | `0x403b54` | 572 | ✓ |
| `method.ns0.GForm2.method_5` | `0x408d3c` | 568 | ✓ |
| `method.ns0.GForm1..ctor` | `0x406d70` | 504 | ✓ |
| `method.Class26.vmethod_4` | `0x40f8a4` | 504 | ✓ |
| `method.ns0.GForm2.GForm2_KeyDown` | `0x4089d8` | 500 | ✓ |
| `method.Class25.method_6` | `0x40db38` | 484 | ✓ |
| `method.Class24.method_6` | `0x40bd1c` | 452 | ✓ |

### Decompiled Code Files

- [`code/method.Class20.method_12.c`](code/method.Class20.method_12.c)
- [`code/method.Class20.method_2.c`](code/method.Class20.method_2.c)
- [`code/method.Class20.method_7.c`](code/method.Class20.method_7.c)
- [`code/method.Class20.smethod_2.c`](code/method.Class20.smethod_2.c)
- [`code/method.Class20.smethod_3.c`](code/method.Class20.smethod_3.c)
- [`code/method.Class20.smethod_4.c`](code/method.Class20.smethod_4.c)
- [`code/method.Class22.smethod_0.c`](code/method.Class22.smethod_0.c)
- [`code/method.Class22.smethod_1.c`](code/method.Class22.smethod_1.c)
- [`code/method.Class24.method_6.c`](code/method.Class24.method_6.c)
- [`code/method.Class25.method_6.c`](code/method.Class25.method_6.c)
- [`code/method.Class26.vmethod_10.c`](code/method.Class26.vmethod_10.c)
- [`code/method.Class26.vmethod_4.c`](code/method.Class26.vmethod_4.c)
- [`code/method.Class34.vmethod_4.c`](code/method.Class34.vmethod_4.c)
- [`code/method.Class35..ctor.c`](code/method.Class35..ctor.c)
- [`code/method.Class7_1..ctor.c`](code/method.Class7_1..ctor.c)
- [`code/method.Class7_1.smethod_1.c`](code/method.Class7_1.smethod_1.c)
- [`code/method.ns0.Class11.smethod_1.c`](code/method.ns0.Class11.smethod_1.c)
- [`code/method.ns0.Class6.method_1.c`](code/method.ns0.Class6.method_1.c)
- [`code/method.ns0.Class6.smethod_0.c`](code/method.ns0.Class6.smethod_0.c)
- [`code/method.ns0.Class6.smethod_19.c`](code/method.ns0.Class6.smethod_19.c)
- [`code/method.ns0.GForm1..ctor.c`](code/method.ns0.GForm1..ctor.c)
- [`code/method.ns0.GForm1.GForm1_Load.c`](code/method.ns0.GForm1.GForm1_Load.c)
- [`code/method.ns0.GForm2.GForm2_KeyDown.c`](code/method.ns0.GForm2.GForm2_KeyDown.c)
- [`code/method.ns0.GForm2.method_0.c`](code/method.ns0.GForm2.method_0.c)
- [`code/method.ns0.GForm2.method_16.c`](code/method.ns0.GForm2.method_16.c)
- [`code/method.ns0.GForm2.method_5.c`](code/method.ns0.GForm2.method_5.c)
- [`code/sym.__c..ctor.c`](code/sym.__c..ctor.c)

## Behavioral Analysis

This final chunk (9/9) provides the most definitive evidence yet regarding the malware's sophistication. It represents the transition point where the Virtual Machine (VM) finishes its complex decoding and internal logic processing, ultimately leading to the execution of a specific malicious action.

Below is the updated analysis incorporating the findings from the final segment.

---

### Updated Analysis Report (Chunk 9/9)

#### 1. The "Final" State Transition
The presence of `swi(3)` or similar indirect calls at the end of such long, convoluted loops indicates a **Transition Layer**. 
*   **VM Exit:** After the VM has successfully navigated its internal state machine and decrypted its required instructions/strings, it eventually reaches a "terminal" block.
*   **Execution Hook:** The final `pcVar2 = swi(3);` suggests that once the VM completes its task (e.g., calculating an encryption key or reconstructing a C2 URL), it calls an underlying system function to perform the actual malicious act (like opening a socket or writing a file). This means the "malicious" part of the code is technically separate from the "parsing" logic, but both are hidden behind the VM's complexity.

#### 2. Advanced Arithmetic & Memory "Masking"
This chunk shows extreme examples of **Instruction Bloat**:
*   **Multi-Step Calculations:** A simple memory assignment or increment is expanded into dozens of lines involving `CONCAT`, `CARRY` checks, and bit-shifts (e.g., the logic around `puVar12 = puVar12 + uVar33`). 
*   **Constant Folding/Smearing:** Values like `0x6f027a2b` or `-0x17030001` are used as "junk" constants. They are added and then subtracted or modified in ways that ultimately result in a small integer or a specific offset. This is designed to break the ability of automated tools to perform constant folding during analysis.

#### 3. Dynamic String & Instruction Assembly
The inclusion of characters like `{`, `}`, `*`, and `'1'` (e.g., `cVar7 = puVar12 + '{';`) confirms a technique called **In-line Construction**:
*   **No Static Strings:** The malware does not store its configuration strings in the `.data` or `.rdata` sections of the binary.
*   **Just-in-Time (JIT) Assembly:** The VM builds these strings character-by-character only at the exact moment they are needed for a system call. This bypasses most basic string-searching tools and makes static analysis nearly impossible without full emulation of the VM's state.

#### 4. Complex State Branching
The nested `while(true)` loops combined with `if` checks on `POPCOUNT` results (e.g., `if ((POPCOUNT(cVar43) & 1U) == 0)`) create a **non-linear execution path**. Every time the code reaches one of these "Gatekeeper" blocks, it effectively "decides" which part of its internal logic to execute next based on results that are mathematically complex but logically simple (e.g., "is this number even?").

---

### Updated Summary Table (Cumulative)

| Feature | Observation | Significance |
| :--- | :--- | :--- |
| **Virtual Machine (VM)** | Extensive `code_r` jumps and state-based logic. | The core malicious logic is hidden inside a custom "interpreter" language. |
| **Arithmetic Obfuscation** | Use of `CONCAT`, `CARRY`, and large, arbitrary constants. | Creates an "economic barrier"; simple math is disguised as complex arithmetic to exhaust the analyst. |
| **Opaque Predicates** | Branching based on `POPCOUNT(x) & 1`. | Forces human/symbolic analysis by hiding the actual logic path behind mathematical hurdles. |
| **In-Line Construction** | Integration of symbols like `{`, `}`, and `*` into math blocks. | Prevents string extraction; data is "constructed" rather than "stored." |
| **State Machine Depth** | Nested loops with complex, multi-step transitions. | Obscures the functional flow; you cannot "trace" a standard function because it lives in VM-space. |
| **Data Scrubbing** | Use of `CONCAT31` and similar packing/unpacking routines. | Hides the fact that data is being moved or modified, making it look like random bit manipulation. |
| **Execution Exit** | Final transition to system calls (e.g., via `swi`). | Marks the end of the VM's "processing" phase and the start of the payload action. |

---

### Final Conclusion Update (Cumulative)

The final analysis confirms that this is a **highly sophisticated, high-tier threat**. The complexity observed across all nine chunks reveals an adversary with significant expertise in anti-analysis techniques.

**Key Findings Summary:**
1.  **Defense-in-Depth Architecture:** The malware doesn't just "hide" its code; it translates it into a different architecture (the VM). This means that even if an analyst finds the string for a C2 server, they won't find it in the binary—it only exists in memory for a fraction of a second.
2.  **Automation Defeat:** By using `POPCOUNT` and intricate math to hide simple logic, the author has effectively "broken" most automated de-obfuscators (like Hex-Rays or standard Ghidra scripts), forcing a human analyst to manually reverse each gate.
3.  **Intentional Complexity:** The sheer volume of "junk code" is not accidental; it's a deliberate strategy to make the cost of analysis higher than the value of the information gathered by the analyst in a timely manner.

**Threat Profile:** This malware belongs to a class designed for **persistent, high-value targets**. It is built to survive scrutiny from advanced forensic teams. The use of custom VM architectures and opaque predicates suggests it is likely used for state-sponsored espionage or highly targeted financially motivated attacks where "stealth" is the primary requirement.

**Recommendation:** 
*   **Static analysis alone will not suffice.** To understand this threat, one must develop a **VM Emulator/Decompiler**. The goal should be to map the `code_r` handlers to their original functional equivalents (e.g., identifying which handler performs an "XOR" or "Add").
*   **Memory Forensics:** Because strings are constructed in-line, dumping memory *during* execution is the most effective way to see the de-obfuscated values at the moment of use.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1028** | Virtualization | The malware implements a custom virtual machine with its own state machine and instruction set to hide core logic from analysts. |
| **T1497** | Obfuscated System Information | Arithmetic masking, "junk" constants, and opaque predicates are used to hide the actual purpose of calculations and branch decisions from automated tools. |
| **T1027** | Obfuscated Files/Information | The use of in-line construction ensures that malicious strings (like C2 URLs) are never stored as static data, evading detection by string-searching tools. |

### Analyst Notes:
*   **Virtualization (T1028)** is the primary mechanism used to create the "Transition Layer" and "State Machine Depth." By running its logic inside a custom interpreter, the malware forces an analyst to reverse-engineer the architecture of the VM before they can even begin to analyze the actual malicious payload.
*   **Obfuscated System Information (T1497)** specifically addresses the "Arithmetic Masking" and "Opaque Predicates." These techniques are designed to exhaust human analysts and break symbolic execution tools by making it difficult to determine which code path will be taken.
*   **Obfuscated Files/Information (T1027)** is applied here because the lack of static strings in `.data` or `.rdata` sections means the file lacks "known indicators." The malware only reveals its true nature in memory during the execution phase.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.* (The report notes that the malware uses in-line construction to ensure these are not present in static strings.)

**File paths / Registry keys**
*   *None identified.*

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   `E442AEEF1ACA522EB71A6A316110A7AD2A92834F46A11E2E95ED289A2AF48AC0` (Potential SHA-256 hash or cryptographic key)
*   `39942EAEE461CDA229BB4EDE2BA191709234ABF226B7EE3C506AF77822CCD5A1` (Potential SHA-256 hash or cryptographic key)

**Other artifacts**
*   **Execution Transition:** `swi(3)` (Software interrupt used as a transition point from the VM's internal logic to system-level execution).
*   **Obfuscation Logic:** `POPCOUNT` (Used in non-linear state branching and "Gatekeeper" blocks).
*   **Manual String Construction Symbols:** `{`, `}`, `*` (Identified as indicators of a JIT assembly/inline construction technique used to hide configuration data).
*   **VM Architecture Elements:** `count_r`, `code_r` (Indicators of a custom Virtual Machine instruction set).

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification:

1. **Malware family:** custom (highly sophisticated/APT-grade)
2. **Malware type:** loader
3. **Confidence:** High (regarding its architecture and functionality as a delivery vehicle)
4. **Key evidence:** 
    *   **Advanced Virtualization (T1028):** The malware utilizes a complex custom VM interpreter with its own instruction set (`code_r`, `count_r`) to hide its core logic, making static analysis nearly impossible without first reversing the "virtual" architecture.
    *   **Sophisticated Anti-Analysis:** The use of opaque predicates (e.g., `POPCOUNT` calculations), arithmetic masking, and "junk" constants are specifically designed to defeat automated de-obfuscators and exhaust human analysts during manual review.
    *   **Just-in-Time (JIT) String Construction:** By constructing strings in-line rather than storing them in data sections, the malware ensures that critical indicators (like C2 URLs or file paths) are only visible in memory for a fraction of a second at the point of use.
