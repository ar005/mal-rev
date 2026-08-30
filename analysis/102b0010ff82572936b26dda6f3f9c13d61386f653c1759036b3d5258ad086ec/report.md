# Threat Analysis Report

**Generated:** 2026-08-18 01:04 UTC
**Sample:** `102b0010ff82572936b26dda6f3f9c13d61386f653c1759036b3d5258ad086ec_102b0010ff82572936b26dda6f3f9c13d61386f653c1759036b3d5258ad086ec.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `102b0010ff82572936b26dda6f3f9c13d61386f653c1759036b3d5258ad086ec_102b0010ff82572936b26dda6f3f9c13d61386f653c1759036b3d5258ad086ec.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 646,656 bytes |
| MD5 | `e835e628e0f8377badfed5cb7fc3e6b3` |
| SHA1 | `c8b29f38ac1a121ef79b4eebd120ff76185eb04a` |
| SHA256 | `102b0010ff82572936b26dda6f3f9c13d61386f653c1759036b3d5258ad086ec` |
| Overall entropy | 7.842 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1738618503 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 643,072 | 7.85 | ⚠️ Yes |
| `.rsrc` | 2,560 | 5.003 | No |
| `.reloc` | 512 | 0.098 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **2144** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

-J+Z 

,.r


+Fr+

%- &(9
%-&(B
%-&(D
%-&(@
%-&(A
0A[i
+

+2	oj

+:	o]

+*	o]

+*	o]
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADP
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADP
Q#y:oJ~

lP5s:
Zv9VBS
7Jtoef
w(.q0.
%O']L
@b*J0Y
z!+ws)8v
 dy
r3
\Q~>K4
BA8Uf
*X0h>^wt
Pz(7'7
W<t~Fm
Uk-Zki
Pb!&FK
o.UZ!WG
F,%QC&
fh=%5q
,NQ!\St{
$eB!ug

Z\zh?
8)t*'!R#
WPnzohR
vwaPi/
g
]3R7@
Z%rNgm
>D*7Y3
 UhR?^
?"UlRo
O'$[4
/lr7Ag
|Bq7s}
\70%}
=h?=iY
e^/SCpm00
1GQo!5U
&Y^{Zy
RL{YQC
4>	O.JBo
oY&>JC
"1?P$<
a.,g|;K~
NC|a	q
"\&v l
BVc::PL
Astaob
RhuWoGT%P!
I#1\;6)
hclIWo
^cJHbI
oc,><s]
VEb48R
yHHk{w4
LyG'M
&)4&oj
rYA8
4
Jv"vY-
iAm0K
jI=_Ff	
+E#pM]>=-
nx;\$E
1jgwa
H~f
aV 
0t}sgW<
?ecoccb
1O"r&"'
E,gEZp
)(B<(
fk<R#B
vvnoK1
YP/NMG
G`M47J
*gtOQw
A[-5z/
8Q"NAw
"n6QFL
=R b;zvu<
2Rwy/P
+r\Km@
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.__c..cctor_3` | `0x4097b9` | 632904 | ✓ |
| `sym.Costura.AssemblyLoader.LoadStream` | `0x40aae8` | 510600 | ✓ |
| `method.__c__DisplayClass15_0._GetKeyValues_b__0` | `0x40a567` | 127570 | ✓ |
| `method.Costura.AssemblyLoader.Attach` | `0x40ae10` | 64728 | — |
| `sym...ctor__18` | `0x407818` | 2606 | ✓ |
| `sym..__78` | `0x40553c` | 1228 | ✓ |
| `sym..__81` | `0x405ec8` | 748 | ✓ |
| `sym..__53` | `0x403ef8` | 664 | ✓ |
| `sym..__79` | `0x405a08` | 648 | ✓ |
| `sym..__82` | `0x4061b4` | 564 | ✓ |
| `method._GetKeyValues_d__15..ctor` | `0x40a58f` | 544 | ✓ |
| `method.__c__DisplayClass12_0._Execute_b__0` | `0x404738` | 508 | ✓ |
| `sym..__52` | `0x403d4c` | 428 | ✓ |
| `sym..__80` | `0x405c90` | 424 | ✓ |
| `method..IsNameOrValueNull` | `0x40a0eb` | 413 | ✓ |
| `sym..__58` | `0x4044b0` | 384 | ✓ |
| `sym..__98` | `0x407028` | 373 | ✓ |
| `sym..__57` | `0x40433c` | 372 | ✓ |
| `sym..__100` | `0x4071b4` | 352 | ✓ |
| `method._GetKeyValues_d__15.MoveNext` | `0x40a5e4` | 348 | ✓ |
| `sym..__158` | `0x409b5c` | 344 | ✓ |
| `sym..__3` | `0x402218` | 340 | ✓ |
| `method..L` | `0x4074b8` | 328 | ✓ |
| `sym..__1` | `0x4020b8` | 312 | ✓ |
| `sym..__56` | `0x404214` | 296 | ✓ |
| `sym..__62` | `0x404b4c` | 284 | ✓ |
| `sym..__17` | `0x402a98` | 276 | ✓ |
| `sym..__85` | `0x406574` | 276 | ✓ |
| `sym..__124` | `0x408a38` | 276 | ✓ |
| `sym..__152` | `0x4097e0` | 272 | ✓ |

### Decompiled Code Files

- [`code/method..IsNameOrValueNull.c`](code/method..IsNameOrValueNull.c)
- [`code/method..L.c`](code/method..L.c)
- [`code/method._GetKeyValues_d__15..ctor.c`](code/method._GetKeyValues_d__15..ctor.c)
- [`code/method._GetKeyValues_d__15.MoveNext.c`](code/method._GetKeyValues_d__15.MoveNext.c)
- [`code/method.__c__DisplayClass12_0._Execute_b__0.c`](code/method.__c__DisplayClass12_0._Execute_b__0.c)
- [`code/method.__c__DisplayClass15_0._GetKeyValues_b__0.c`](code/method.__c__DisplayClass15_0._GetKeyValues_b__0.c)
- [`code/sym...ctor__18.c`](code/sym...ctor__18.c)
- [`code/sym..__1.c`](code/sym..__1.c)
- [`code/sym..__100.c`](code/sym..__100.c)
- [`code/sym..__124.c`](code/sym..__124.c)
- [`code/sym..__152.c`](code/sym..__152.c)
- [`code/sym..__158.c`](code/sym..__158.c)
- [`code/sym..__17.c`](code/sym..__17.c)
- [`code/sym..__3.c`](code/sym..__3.c)
- [`code/sym..__52.c`](code/sym..__52.c)
- [`code/sym..__53.c`](code/sym..__53.c)
- [`code/sym..__56.c`](code/sym..__56.c)
- [`code/sym..__57.c`](code/sym..__57.c)
- [`code/sym..__58.c`](code/sym..__58.c)
- [`code/sym..__62.c`](code/sym..__62.c)
- [`code/sym..__78.c`](code/sym..__78.c)
- [`code/sym..__79.c`](code/sym..__79.c)
- [`code/sym..__80.c`](code/sym..__80.c)
- [`code/sym..__81.c`](code/sym..__81.c)
- [`code/sym..__82.c`](code/sym..__82.c)
- [`code/sym..__85.c`](code/sym..__85.c)
- [`code/sym..__98.c`](code/sym..__98.c)
- [`code/sym.Costura.AssemblyLoader.LoadStream.c`](code/sym.Costura.AssemblyLoader.LoadStream.c)
- [`code/sym.__c..cctor_3.c`](code/sym.__c..cctor_3.c)

## Behavioral Analysis

This final update incorporates findings from **Chunk 7/7**. The concluding segment of the disassembly provides a definitive look at the "end-game" tactics used by the developers: sophisticated anti-disassembly techniques designed to sabotage the very tools (like IDA Pro or Ghidra) that analysts use to study the malware.

---

### Updated Analysis Report (Chunk 7 Additions)

The final section of the disassembly (`sym..__17`, `sym..__85`, and `sym..__124`) confirms a transition from "complex logic" to **Active Tool Sabotage**.

#### New Technical Findings from Chunk 7:

*   **Intentional Anti-Disassembly (Overlap Tactics):**
    The decompiler issues multiple warnings for "bad instruction data" and "overlapping instructions" (e.g., at `0x402db9`, `0x406631`, and `0x408c83`).
    *   **Analysis:** This is a classic high-tier anti-disassembly technique. By jumping into the *middle* of a multi-byte instruction, the malware creates "chameleon" code. A linear disassembler will see one set of instructions, while the CPU (executing the jump) will interpret a completely different set.
    *   **Impact:** This forces an analyst to manually fix every "broken" block in the disassembly to understand how the code actually executes. It is a deliberate "landmine" for human researchers and automated scripts.

*   **Extreme Mathematical Obfuscation (MBA-Style):**
    In `sym..__17` and `_85`, very simple operations are wrapped in massive amounts of bitwise logic, carries (`CARRY1`), and multi-step arithmetic (e.g., the way characters like `'o'`, `'s'`, or offsets like `0x6f` are calculated).
    *   **Analysis:** This is a form of **Mixed Boolean-Arithmetic (MBA)**. It transforms a simple constant into a complex mathematical expression that evaluates to that constant only at runtime. 
    *   **Impact:** Automated tools cannot "simplify" these expressions. The logic remains "opaque," making it nearly impossible for an analyst to determine what a value represents (e.g., is it a port number, a memory offset, or a command?) without executing the code in a debugger.

*   **Control Flow Complexity & Branch Obscurity:**
    The repeated use of `while(true)` loops containing heavy math before any actual logic is performed suggests the presence of **decryption/de-obfuscation stubs**. 
    *   **Analysis:** These blocks are likely "cleaning" data or unpacking the next stage. The fact that these look like a "wall of math" is intentional; it hides the transition between different stages of the malware's execution.

*   **System Interaction Concealment:**
    The inclusion of `swi(3)` (in `sym..__152`) and various calls to `out()` functions within heavily obfuscated blocks suggests that even standard Windows API interactions are being "wrapped" or modified by the packer.

---

### Cumulative Summary of Findings (Chunks 1–7)

The analysis confirms that this malware is a high-sophistication example of **defensive programming**. It does not just hide its purpose; it actively fights back against the tools used to uncover it.

**1. Packaging & Distribution:**
*   Uses **Costura.Fody** for heavy bundling, hiding internal dependencies and shrinking the "surface area" available for easy scanning.

**2. Advanced Obfuscation Suite:**
*   **Control Flow Flattening (CFF):** Fragments logic into a "Dispatcher" model, making it impossible to follow the flow via static graphing.
*   **Mixed Boolean-Arithmetic (MBA):** Replaces simple constants and operations with complex mathematical equivalents that only resolve at runtime.
*   **Instruction Overlap:** A sophisticated tactic that exploits how disassemblers process bytes, creating "trap zones" for the human analyst.
*   **Data Obfuscation:** Construction of strings/commands in memory via layered math (Chunk 1 & 5) ensures no plaintext indicators exist on disk.

**3. Anti-Analysis & Evasion Tactics:**
*   **Tool Sabotage:** Deliberate use of "bad instructions" and overlapping bytes to break the linear flow of automated tools like Ghidr/IDA.
*   **Complexity as a Shield:** By creating an enormous amount of "noise" (junk code, math-heavy loops), the malware forces the analyst into a time-consuming manual process of de-obfuscation.

**4. Technical Sophistication Indicators:**
*   The combination of **Costura bundling**, **CFF**, and **Instruction Overlap** strongly suggests either a sophisticated **APT (Advanced Persistent Threat)** or a professional, high-end **Malware-as-a-Service (MaaS)** operation.

---

### Final Assessment & Updated Recommendation:

**Confidence Level: High (Sophisticated Malware/APT)**

The analysis of all 7 chunks confirms that this is not "entry-level" malware. The presence of **Instruction Overlapping** and **MBA logic** are hallmark traits of professional-grade evasion. The author's primary goal is to exhaust the analyst’s time and resources through "Analytical Friction."

**Strategic Recommendations:**

1.  **Abandon Traditional Static Analysis Paths:**
    The complexity of the "Dispatcher" (CFF) and the "Math Walls" means that manually de-obfuscating this code will take weeks or months of work with low information yield. **Do not attempt to untangle every jump in `sym..__17`.**

2.  **Prioritize Memory Forensics (The "Wait for it" approach):**
    Since the malware is designed to "unfold" itself at runtime, use a debugger (**x64dbg**) or an emulator. Allow the malware to run until it has performed its internal de-obfuscation loops. Once it has unpacked its strings and configuration into memory, take a **memory dump**. This bypasses all of the mathematical complexity found in Chunks 1–7.

3.  **Execute Behavioral Sandboxing:**
    Because the code is so well hidden, observe what it *does* rather than how it's *written*. Focus on:
    *   Network connections (C2 activity).
    *   File system changes or registry keys created.
    *   Process injection behavior.

4.  **Dynamic Instrumentation (Frida/API Hooking):**
    Use **Frida** to hook higher-level Windows APIs (e.g., `InternetConnect`, `WriteProcessMemory`). This allows you to capture the "final results" of all the complex calculations in a single moment, bypassing the layers of math and jumps used by the malware.

5.  **Indicator Generation:**
    Instead of looking for code-based signatures (which are heavily obfuscated), create **behavioral YARA rules** based on specific memory artifacts or sequences of API calls that occur immediately after its de-obfuscation loops finish.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors observed in the provided report to the relevant MITRE ATT&CK techniques. The malware demonstrates high-tier sophistication by utilizing multiple layers of obfuscation to hinder both manual and automated analysis.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | **Obfuscated/Packed_Code** | The use of Instruction Overlapping, Control Flow Flattening (CFF), and "Math Walls" are deliberate techniques to break disassemblers like IDA Pro/Ghidra and hide the logic from automated analysis. |
| **T1564** | **Data Encoding** | Mixed Boolean-Arithmetic (MBA) is used to transform simple constants and strings into complex mathematical expressions, ensuring no plaintext indicators exist on disk for signature-based detection. |
| **T1036** | **Masquerading** | The "wrapping" or modification of standard Windows API calls (e.g., `swi(3)`) suggests an attempt to hide the true intent of system interactions from security monitoring tools. |

### Analyst Notes:
*   **Instruction Overlap & CFF:** These are classic examples of **anti-analysis**. By forcing a "human-in-the-loop" requirement (manually fixing every broken block), the authors significantly increase the time and cost associated with reverse engineering.
*   **MBA Selection:** While MBA is often viewed as an obfuscation method, in the MITRE framework, it maps effectively to **Data Encoding (T1564)** because it encodes the "true" value of a variable through mathematical complexity rather than standard encoding (like Base64), making it harder for automated tools to resolve.
*   **Costura Bundling:** While not a standalone technique in MITRE, this is a common implementation of **T1027**, as it bundles dependencies into a single executable to reduce the surface area available for static analysis.

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs). 

Note: Many of the strings in the "EXTRACTED STRINGS" section appear to be obfuscated data or "junk code" designed to confuse automated scanners; therefore, only those with clear technical significance or specific identifiers have been included.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: While memory offsets are provided in the analysis, they do not constitute file paths or registry keys.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Bundling/Packaging Tools:** `Costura.Fody` (Indicates the use of a specific framework to bundle dependencies and hide the attack surface).
*   **Instruction Overlap Offsets:** `0x402db9`, `0x406631`, `0x408c83` (Specific locations used for anti-disassembly "trap" zones).
*   **Obfuscated Logic Identifiers:** `sym..__17`, `_85`, `__124`, `__152` (Specific code blocks identified as containing MBA math or system interaction concealment).
*   **System Library References:** `mscorlib`, `System.Resources.ResourceReader` (Standard .NET libraries; used here to identify the sample's environment).

---

## Malware Family Classification

1. **Malware family:** custom
2. **Malware type:** loader
3. **Confidence:** High

4. **Key evidence:**
*   **Advanced Anti-Analysis Suite:** The use of Instruction Overlapping (to break disassemblers like IDA/Ghidr), Control Flow Flattening (CFF), and Mixed Boolean-Arithmetic (MBA) indicates a high-tier, professional-grade construction designed to create "analytical friction."
*   **Sophisticated Obfuscation as a Shield:** The presence of "Math Walls" and the wrapping of system interactions suggest a primary purpose of acting as a **Loader**; it is designed to hide its core functionality/payload through layers of mathematical complexity that only resolve at runtime.
*   **Intentional Tool Sabotage:** Unlike basic malware, this sample specifically targets the tools used by human researchers, aiming to exhaust their time and resources during the de-obfuscation process.
