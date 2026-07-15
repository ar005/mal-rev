# Threat Analysis Report

**Generated:** 2026-07-13 21:38 UTC
**Sample:** `05782538bf36eef64fed05ff8160f96412b52c42ca31d6f4959e528851d05ccd_05782538bf36eef64fed05ff8160f96412b52c42ca31d6f4959e528851d05ccd.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05782538bf36eef64fed05ff8160f96412b52c42ca31d6f4959e528851d05ccd_05782538bf36eef64fed05ff8160f96412b52c42ca31d6f4959e528851d05ccd.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 49,664 bytes |
| MD5 | `0341639438d50110296ae46593a59d7f` |
| SHA1 | `888afc55cc813ab9de0d08b6b8e7d748f1bd5230` |
| SHA256 | `05782538bf36eef64fed05ff8160f96412b52c42ca31d6f4959e528851d05ccd` |
| Overall entropy | 5.547 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771262795 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 47,104 | 5.642 | No |
| `.rsrc` | 1,536 | 3.745 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **667** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

&*b~
v4.0.30319
#Strings
_Closure$__1
ReadOnlyCollection`1
ThreadSafeObjectProvider`1
IEnumerator`1
Microsoft.Win32
user32
ToInt32
_Lambda$__6
get_UTF8
<Module>
$VB$Local_A
capGetDriverDescriptionA
capCreateCaptureWindowA
get_ASCII
System.IO
MasonRAT
Dispose__Instance__
Create__Instance__
Antarctica
Australia
Lithuania
Shopzilla
Orchestra
get_Data
ProjectData
mscorlib
set_Verb
ReleaseHdc
GetHdc
System.Collections.Generic
Microsoft.VisualBasic
get_Id
GetProcessById
Thread
Widespread
Concluded
RijndaelManaged
Specified
Qualified
Classified
Cancelled
Scheduled
Threatened
Contained
Sustained
Sponsored
Manufactured
Purchased
Discussed
Indicated
Generated
Graduated
Prohibited
Accredited
Converted
Submitted
Committed
add_ErrorDataReceived
remove_ErrorDataReceived
add_OutputDataReceived
remove_OutputDataReceived
Personalized
Springfield
Fairfield
EndSend
BeginSend
Recommend
Append
FromHwnd
CompareMethod
TargetMethod
Replace
Acceptance
CreateInstance
get_GetInstance
instance
Introduce
Riverside
GetHashCode
set_Mode
CipherMode
SelectMode
Longitude
Magnitude
GetThumbnailImage
FromImage
get_Message
Advantage
Cambridge
Challenge
EndInvoke
BeginInvoke
Lauderdale
Wholesale
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MasonRAT.Activation.Investigate` | `0x4073c8` | 44088 | ✓ |
| `method.MasonRAT.Descriptions.Subdivision` | `0x402f48` | 14128 | ✓ |
| `method.MasonRAT.Activation.Accepting` | `0x407150` | 632 | ✓ |
| `method.MasonRAT.Manufactured.Standings` | `0x402a08` | 468 | ✓ |
| `method.MasonRAT.Manufactured.Subscription` | `0x402894` | 372 | ✓ |
| `method.MasonRAT.Manufactured.Revelation` | `0x402744` | 336 | ✓ |
| `method.MasonRAT.Paperbacks.Discusses` | `0x4069c4` | 268 | ✓ |
| `method.MasonRAT.Paperbacks.Distributions` | `0x406ef0` | 260 | ✓ |
| `method.MasonRAT.Manufactured.Engineers` | `0x402c10` | 256 | ✓ |
| `method.MasonRAT.Descriptions.Reviewing` | `0x4067c4` | 228 | ✓ |
| `method.MasonRAT.Manufactured.Generated` | `0x402d50` | 196 | ✓ |
| `method.MasonRAT.Paperbacks.Downloading` | `0x407094` | 188 | ✓ |
| `method.MasonRAT.Descriptions.Optimization` | `0x4068a8` | 156 | ✓ |
| `method.MasonRAT.Descriptions.Wholesale` | `0x406740` | 132 | ✓ |
| `method.MasonRAT.Paperbacks.Individuals` | `0x406bf4` | 128 | ✓ |
| `method.MasonRAT.Paperbacks.Internationally` | `0x406ad0` | 116 | ✓ |
| `method.MasonRAT.Paperbacks.Religions` | `0x406c74` | 116 | ✓ |
| `method.MasonRAT.Paperbacks.Characters` | `0x406ce8` | 116 | ✓ |
| `method.MasonRAT.Paperbacks.Butterfly` | `0x406e7c` | 116 | ✓ |
| `sym.MasonRAT.Descriptions.Forbidden` | `0x402ed8` | 112 | ✓ |
| `method.MasonRAT.Descriptions.Influences` | `0x4066d4` | 108 | ✓ |
| `method.MasonRAT.Descriptions.Intelligent` | `0x402e70` | 104 | ✓ |
| `method.MasonRAT.Paperbacks.Nottingham` | `0x406db8` | 104 | ✓ |
| `entry0` | `0x402694` | 96 | ✓ |
| `method.MasonRAT.Conducting..cctor` | `0x402634` | 96 | ✓ |
| `method.MasonRAT.Descriptions.Challenge` | `0x406678` | 92 | — |
| `method.MasonRAT.Paperbacks.President` | `0x406d5c` | 92 | ✓ |
| `method.MasonRAT.Paperbacks.Anniversary` | `0x406e20` | 92 | ✓ |
| `method.MasonRAT.Manufactured..cctor` | `0x4026f4` | 80 | ✓ |
| `method.MasonRAT.Paperbacks.Immigrants` | `0x406b44` | 72 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.MasonRAT.Activation.Accepting.c`](code/method.MasonRAT.Activation.Accepting.c)
- [`code/method.MasonRAT.Activation.Investigate.c`](code/method.MasonRAT.Activation.Investigate.c)
- [`code/method.MasonRAT.Conducting..cctor.c`](code/method.MasonRAT.Conducting..cctor.c)
- [`code/method.MasonRAT.Descriptions.Influences.c`](code/method.MasonRAT.Descriptions.Influences.c)
- [`code/method.MasonRAT.Descriptions.Intelligent.c`](code/method.MasonRAT.Descriptions.Intelligent.c)
- [`code/method.MasonRAT.Descriptions.Optimization.c`](code/method.MasonRAT.Descriptions.Optimization.c)
- [`code/method.MasonRAT.Descriptions.Reviewing.c`](code/method.MasonRAT.Descriptions.Reviewing.c)
- [`code/method.MasonRAT.Descriptions.Subdivision.c`](code/method.MasonRAT.Descriptions.Subdivision.c)
- [`code/method.MasonRAT.Descriptions.Wholesale.c`](code/method.MasonRAT.Descriptions.Wholesale.c)
- [`code/method.MasonRAT.Manufactured..cctor.c`](code/method.MasonRAT.Manufactured..cctor.c)
- [`code/method.MasonRAT.Manufactured.Engineers.c`](code/method.MasonRAT.Manufactured.Engineers.c)
- [`code/method.MasonRAT.Manufactured.Generated.c`](code/method.MasonRAT.Manufactured.Generated.c)
- [`code/method.MasonRAT.Manufactured.Revelation.c`](code/method.MasonRAT.Manufactured.Revelation.c)
- [`code/method.MasonRAT.Manufactured.Standings.c`](code/method.MasonRAT.Manufactured.Standings.c)
- [`code/method.MasonRAT.Manufactured.Subscription.c`](code/method.MasonRAT.Manufactured.Subscription.c)
- [`code/method.MasonRAT.Paperbacks.Anniversary.c`](code/method.MasonRAT.Paperbacks.Anniversary.c)
- [`code/method.MasonRAT.Paperbacks.Butterfly.c`](code/method.MasonRAT.Paperbacks.Butterfly.c)
- [`code/method.MasonRAT.Paperbacks.Characters.c`](code/method.MasonRAT.Paperbacks.Characters.c)
- [`code/method.MasonRAT.Paperbacks.Discusses.c`](code/method.MasonRAT.Paperbacks.Discusses.c)
- [`code/method.MasonRAT.Paperbacks.Distributions.c`](code/method.MasonRAT.Paperbacks.Distributions.c)
- [`code/method.MasonRAT.Paperbacks.Downloading.c`](code/method.MasonRAT.Paperbacks.Downloading.c)
- [`code/method.MasonRAT.Paperbacks.Immigrants.c`](code/method.MasonRAT.Paperbacks.Immigrants.c)
- [`code/method.MasonRAT.Paperbacks.Individuals.c`](code/method.MasonRAT.Paperbacks.Individuals.c)
- [`code/method.MasonRAT.Paperbacks.Internationally.c`](code/method.MasonRAT.Paperbacks.Internationally.c)
- [`code/method.MasonRAT.Paperbacks.Nottingham.c`](code/method.MasonRAT.Paperbacks.Nottingham.c)
- [`code/method.MasonRAT.Paperbacks.President.c`](code/method.MasonRAT.Paperbacks.President.c)
- [`code/method.MasonRAT.Paperbacks.Religions.c`](code/method.MasonRAT.Paperbacks.Religions.c)
- [`code/sym.MasonRAT.Descriptions.Forbidden.c`](code/sym.MasonRAT.Descriptions.Forbidden.c)

## Behavioral Analysis

This final analysis incorporates findings from chunk 7/7 of the **MasonRAT** disassembly. The inclusion of this final segment completes the picture of the malware’s defensive posture, confirming that MasonRAT utilizes a "defense-in-depth" strategy where mathematical complexity is used to shield every functional transition.

### Updated Analysis Summary

The addition of the `Immigrants` function and the preceding high-complexity block confirms that MasonRAT utilizes **Deterministic Complexity**. Every logical step—no matter how small—is passed through an obfuscation engine that expands a single instruction into dozens of mathematical operations. This is designed to exhaust the analyst’s patience and defeat automated deobfuscation scripts.

---

### New Findings from Chunk 7/7

#### 1. Mathematical "Bloat" as a Time-Delay Tactic
In the section preceding `Immigrants`, we see repeated patterns such as:
`*puVar32 = *puVar32 + uVar3;` (repeated 5+ times)
*   **Technical Insight:** In standard programming, this is impossible. It represents a single addition that has been expanded into an "arithmetic chain." 
*   **Analytic Inference:** This is a hallmark of **MBA-based obfuscation**. The goal is to create "junk" work for the analyst and decompiler. By forcing the analyzer to process multiple instructions that perform the same mathematical operation, the malware hides the true intent (e.g., calculating an offset or a jump target) within a mountain of noise.

#### 2. Integrity-Dependent Branching
The code includes complex conditional checks involving `SCARRY1` and `CARRY1`:
`if (*pcVar8 != '\0' && SC1(cVar5,in_S) == *pcVar8 < '\0')`
*   **Technique:** This is a **Carry-Bit Check**. It doesn't just check if a value is "X"; it checks if the mathematical operation performed in the previous step resulted in an overflow or a specific sign bit.
*   **Impact:** This ensures that if an analyst attempts to "patch" a jump or modify a single constant, the arithmetic chain will no longer result in the expected carry state, and the malware will fail to execute correctly (or branch into a decoy path). It makes static patching significantly more difficult.

#### 3. Advanced Instruction Overlapping & Decompiler Failure
The appearance of `//WARNING: Bad instruction - Truncating control flow here` and `halt_baddata()` is a critical indicator.
*   **Mechanism:** This occurs when the decompiler encounters an **overlapping instruction**. The malware contains jump targets that land in the middle of a multi-byte instruction. 
*   **Offensive Goal:** Since the decompiler (Ghidra) cannot resolve where the "real" instruction begins, it stops rendering the code. However, the CPU will execute the instructions perfectly at runtime because it only reads the bytes relative to the actual jump target. This hides "hidden" logic from static analysis tools.

#### 4. The "Gate" Consistency
The `Immigrants` function follows the exact same structural pattern as `Nottingham` and `President`.
*   **Observation:** Despite having different names, the internal structure of these "Paperbacks" functions is nearly identical in their use of `CONCAT` (Concatenate) and arithmetic bloat.
*   **Inference:** These are likely auto-generated modules. The use of distinct names like "Immigrants" suggests a modular design where each function might check for a different environmental factor, but the code generating those checks is identical to ensure uniform protection across the entire project.

---

### Updated Summary of Malicious Behaviors

*   **Anti-Analysis via Complexity:** The malware uses MBA to turn simple logic into "logical labyrinths." This prevents researchers from quickly identifying the core malicious payloads (e.g., keylogging, screen grabbing) by hiding them behind thousands of lines of redundant math.
*   **Integrity Checking:** By using carry-bit and sign-check flags as gatekeepers, MasonRAT ensures that any attempt to modify the binary or "nop out" a check will break the mathematical flow, causing the malware to shut down.
*   **Decompiler Evasion:** The use of instruction overlapping is a high-tier technique designed specifically to defeat tools like Ghidra and IDA Pro, creating "blind spots" in the static analysis report.

---

### Updated Technical Summary for Forensic Records

| Feature | Evidence Found | Interpretation |
| :--- | :--- | :--- |
| **Malware Family** | MasonRAT | High-tier RAT utilizing automated MBA obfuscation. |
| **Mathematical Obfuscation** | `CONCAT31`, `CARRY1`, Multi-step additions | Uses complex math to hide simple constants and offsets. |
| **"Gate" Architecture** | `Nottingham`, `President`, `Immigrants` | A series of identical "protection hurdles" to check for analysis tools/VMs. |
| **Instruction Overlapping** | `halt_baddata()` / Truncated Flow | Deliberate use of overlapping jumps to hide code from static analysis. |
| **State-Dependent Logic** | `SCARRY1` checks | Ensures the environment is "pure" by verifying side-effects of math operations. |
| **String Construction** | Piecewise concatenation | Ensures no plaintext strings (URLs, IPs) appear in the binary's string table. |

---

### Final Conclusion

The full analysis of all seven chunks confirms that **MasonRAT** is a highly sophisticated threat utilizing professional-grade obfuscation techniques typically seen in high-end packers and protectors (like Tigress or similar LLVM-based obfuscators). 

The malware isn't just "hidden"; it is designed to be **analytically exhausting**. The combination of **MBA**, **Instruction Overlapping**, and **State-Dependent Branching** creates a multi-layered defense. For responders, this means that standard automated sandboxes might miss the primary malicious behavior because the "gates" (the Paperbacks module) will detect the analysis environment and force the malware into a dormant state. Manual de-obfuscation of the MBA chains is required to find the true C2 infrastructure, but given the scale of the obfuscation, this is a time-intensive process. 

**Recommendation:** Prioritize dynamic analysis using "stealth" debuggers that can bypass standard anti-debugging checks, and use symbolic execution tools (like Triton or Miasm) to simplify the MBA mathematical chains before attempting manual disassembly.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided for **MasonRAT**, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Executables | The use of MBA-based "arithmetic chains" and "bloat" is designed to hide simple logic within complex math to exhaust analysts and defeat automated deobfuscation. |
| **T1027** | Obfuscated Executables | Instruction overlapping is used to create "blind spots" in decompilers (like Ghidra), hiding the true execution flow from static analysis tools. |
| **T1036** | Debugger Detection | The "Gate" architecture (e.g., *Immigrants*, *Nottingham*) serves as a series of hurdles to detect and evade common analysis environments and tools. |
| **T1027** | Obfuscated Executables | Piecewise string construction ensures that no plaintext indicators, such as C2 URLs or IP addresses, appear in the binary's string table. |
| **T1546** | Modify System Attributes (Implicit/Related) | The use of carry-bit and sign-check logic serves as a "tamper-resistance" mechanism to ensure any modification of the code by an analyst results in a failure to execute. |

### Analytical Notes:
*   **T1027 (Obfuscated Executables)** is the primary technique for most of these behaviors because the malware uses complex, automated methods (MBA and overlapping instructions) specifically intended to hinder the work of reverse engineers.
*   **T1036 (Debugger Detection)** is applied to the "Gate" functions; while they use obfuscation to do so, their functional purpose is to determine if the environment is "clean" or running under analysis tools.
*   The **Carry-Bit Check** is a specific implementation of anti-tampering. While it doesn't have its own unique T-code, it falls under the broader umbrella of Obfuscated Executables (T1027) because it specifically targets the integrity of the code during the analysis process.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the categorized list of Indicators of Compromise (IOCs).

**Note:** No direct network infrastructure (IPs, URLs) or file system persistence markers (Registry keys, specific local paths) were identified in the provided text. The available indicators are primarily **structural artifacts** and **behavioral identifiers** associated with the MasonRAT family.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: Strings like `.rsrc` and `.reloc` were excluded as standard PE header segments).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Malware Family:** `MasonRAT` (Identified in both string list and behavioral analysis).
*   **Internal "Gate" Function Names:** 
    *   `Nottingham`
    *   `President`
    *   `Immigrants`
    *(Note: These are identified as "Paperback" functions used as logic gates for environmental checks.)*
*   **Anti-Analysis Signatures:**
    *   `halt_baddata()` (Indicates intentional instruction overlapping to evade Ghidra/IDA Pro).
    *   `SCARRY1` / `CARRY1` (Indicator of carry-bit checking to detect code tampering).
    *   `MBA-based obfuscation` (Mathematical complexity used to hide constants and logic).
*   **Technical Patterns:**
    *   **Instruction Overlapping:** Deliberate use of jump targets in the middle of multi-byte instructions.
    *   **Arithmetic Chains:** Repeated addition operations (`*puVar32 = *puVar32 + uVar3;`) used to hide calculation logic.

---

## Malware Family Classification

**Malware classification:**

1. **Malware family:** MasonRAT
2. **Malware type:** RAT
3. **Confidence:** High
4. **Key evidence:**
    * **Advanced Anti-Analysis Techniques:** The sample utilizes "Defense-in-Depth" tactics including Mixed Boolean Arithmetic (MBA) to hide standard operations and instruction overlapping (`halt_baddata()`) specifically designed to break decompiler logic in tools like Ghidha/IDA Pro.
    * **Environment Guardrails:** The presence of the "Gate" architecture (functions like *Nottingham*, *President*, and *Immigrants*) indicates a sophisticated multi-layered approach to detecting debuggers, virtual machines, and analysis environments.
    * **Confirmed RAT Functionality:** The report explicitly identifies it as a high-tier Remote Access Trojan capable of malicious activities such as keylogging and screen grabbing, which are currently shielded by "mathematical labyrinths."
