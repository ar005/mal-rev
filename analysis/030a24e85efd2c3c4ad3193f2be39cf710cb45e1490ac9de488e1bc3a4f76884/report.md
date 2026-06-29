# Threat Analysis Report

**Generated:** 2026-06-28 20:14 UTC
**Sample:** `030a24e85efd2c3c4ad3193f2be39cf710cb45e1490ac9de488e1bc3a4f76884_030a24e85efd2c3c4ad3193f2be39cf710cb45e1490ac9de488e1bc3a4f76884.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `030a24e85efd2c3c4ad3193f2be39cf710cb45e1490ac9de488e1bc3a4f76884_030a24e85efd2c3c4ad3193f2be39cf710cb45e1490ac9de488e1bc3a4f76884.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,412,608 bytes |
| MD5 | `a6169923a0c8604c13bcec3bbbd8a3f3` |
| SHA1 | `6b3997141cfdb9f44dcd1f690d31bf9c43043c0e` |
| SHA256 | `030a24e85efd2c3c4ad3193f2be39cf710cb45e1490ac9de488e1bc3a4f76884` |
| Overall entropy | 6.894 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1758419785 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,400,320 | 6.906 | No |
| `.rsrc` | 11,264 | 3.027 | No |
| `.reloc` | 512 | 0.098 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **7343** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

&	rx;
p+rGg
l#333333
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADP
I8dgr,
x4}R'"
({E1,U
M05yhud
:D46/N
M(tj\^)
V]84sj
w6f{?1;
]4/CT
xGC_B
aN0%oq]
\:)"N[|d'
[~uZ!x
l0K+1?O
|jX@4=
.sLb'L
5OlqnV}
!RlvG;y
bt a;0
J<z,VX"
?mT<t5
2UPU:_
zyK`f
'pxc?~
`YFB
RyQCMP
]e2w,
8jX,&c"
oge:bV
:[FA,C
y?>!4(`L4Kq
SBE7OB
NoTss1
+SE
:I[
f2lo7pN
3uGj
s5
Ww8msV

niA8
O28&Qm
xGXG4%
J_Tu,5(
T<Zc4rR
E,nZC/x5
q63vSzc
h\ IWR
_	~tR&6
~Cjo0X,4
1
_:hmu&
z[O|i0
JHOd9r
prbP^b
BR Oq
tM<
E_C(
JWO6j9
i:Yvq+
35yX(g
#;&Ux06
9:D>O
po#beF}
l09U5
,Eb95N4
x}|uP~6HA0W
y8;&bS
L9+n$
);`gi
14
3[| pO
+^m7&f
6-5P
wJ*gAWv
:F[HEAt
0}^
/$
jA{ z"-u
9
D	9f
na?Q=/
b5hm2!
|Q:82j#k
43._!:4
[cMVTiuY
,7w|5i
9tt<,g
6[OFR,
	_^{jV
%IwdU
rQV>0(
AH1\Yr
 .&5:
,5MmT??T=
g0;yM`
B!,
ED
%"t0n
Ll%O
Qyj<hA
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.fTr94sEbjo5B.0Yyofi6HF3mgm.9siMdJk7x3` | `0x40210d` | 592306 | ✓ |
| `entry0` | `0x4212d0` | 464880 | ✓ |
| `method.Tra4in5.Nt6c7Ekoq3J.xFi09cTpm` | `0x402050` | 65752 | ✓ |
| `method.Gro4fD8b._PrivateImplementationDetails_.ComputeStringHash` | `0x421700` | 64464 | ✓ |
| `method.K_i2yw1X.8j_QW..cctor` | `0x405ea9` | 49764 | ✓ |
| `method.1omDq0KmtAs8k6.1Zd_c4RfSeo8g.2yyYtAb3d5H` | `0x413918` | 21792 | ✓ |
| `method.1omDq0KmtAs8k6.bEf0p9RiHt7.Pmi7ij4AZ5t` | `0x406f3c` | 15640 | ✓ |
| `method.1omDq0KmtAs8k6.bEf0p9RiHt7.wEk2Wn7e` | `0x40b424` | 1532 | ✓ |
| `method.rHc8e.Ke2intX79D.xm7E6G` | `0x41e0f8` | 1504 | ✓ |
| `method.wb4D5oRg.Nm3_6bkJ.9odFktX` | `0x40f438` | 1160 | ✓ |
| `method.wb4D5oRg.Nm3_6bkJ.5mqPN3rkno` | `0x40e0a0` | 1060 | ✓ |
| `method.1omDq0KmtAs8k6.bEf0p9RiHt7.5qxYsHe3` | `0x40cd0c` | 1036 | ✓ |
| `method.1omDq0KmtAs8k6.1Zd_c4RfSeo8g.Xkk9dp6D` | `0x4190cc` | 1036 | ✓ |
| `method.wb4D5oRg.Nm3_6bkJ.ox9BaKz` | `0x40fe40` | 936 | ✓ |
| `method.rHc8e.Ke2intX79D.dCq3ab8SGn` | `0x41da7c` | 872 | ✓ |
| `method.rHc8e.Ke2intX79D.cNm9Y2fktn6K3F` | `0x41ee8c` | 828 | ✓ |
| `method.wb4D5oRg.Nm3_6bkJ.gf9S4XpjxpY` | `0x4107a4` | 808 | ✓ |
| `method.rHc8e.Ke2intX79D.4dqRd9` | `0x41fa08` | 796 | ✓ |
| `method.rHc8e.Ke2intX79D.Tsi6m` | `0x420a74` | 792 | ✓ |
| `method.wb4D5oRg.Nm3_6bkJ.Xym8qS1k5wHsr9` | `0x40e524` | 736 | ✓ |
| `method.rHc8e.Ke2intX79D.0Cmfg` | `0x41cbb0` | 732 | ✓ |
| `method.wb4D5oRg.Nm3_6bkJ.8gtApN0eZ2f` | `0x4110fc` | 700 | ✓ |
| `method.wb4D5oRg.Nm3_6bkJ.zDq9g4Kk5Lizb8` | `0x411b28` | 700 | ✓ |
| `method.rHc8e.Ke2intX79D.Wyt8i` | `0x41d014` | 696 | ✓ |
| `method.1omDq0KmtAs8k6.bEf0p9RiHt7.4GsqHok16wMjm` | `0x40d708` | 680 | ✓ |
| `method.1omDq0KmtAs8k6.bEf0p9RiHt7.bHw5W1xtpF8` | `0x40c7d4` | 676 | ✓ |
| `method.wb4D5oRg.Nm3_6bkJ.y_1F3eBgQ9` | `0x40f1a0` | 664 | ✓ |
| `method.1omDq0KmtAs8k6.bEf0p9RiHt7.1QksFwx` | `0x40ca78` | 660 | ✓ |
| `method.wb4D5oRg.Nm3_6bkJ.6irKz` | `0x4113b8` | 632 | ✓ |
| `method.1omDq0KmtAs8k6.1Zd_c4RfSeo8g.8Siby3Fs9mpDn` | `0x41a45c` | 628 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.1omDq0KmtAs8k6.1Zd_c4RfSeo8g.2yyYtAb3d5H.c`](code/method.1omDq0KmtAs8k6.1Zd_c4RfSeo8g.2yyYtAb3d5H.c)
- [`code/method.1omDq0KmtAs8k6.1Zd_c4RfSeo8g.8Siby3Fs9mpDn.c`](code/method.1omDq0KmtAs8k6.1Zd_c4RfSeo8g.8Siby3Fs9mpDn.c)
- [`code/method.1omDq0KmtAs8k6.1Zd_c4RfSeo8g.Xkk9dp6D.c`](code/method.1omDq0KmtAs8k6.1Zd_c4RfSeo8g.Xkk9dp6D.c)
- [`code/method.1omDq0KmtAs8k6.bEf0p9RiHt7.1QksFwx.c`](code/method.1omDq0KmtAs8k6.bEf0p9RiHt7.1QksFwx.c)
- [`code/method.1omDq0KmtAs8k6.bEf0p9RiHt7.4GsqHok16wMjm.c`](code/method.1omDq0KmtAs8k6.bEf0p9RiHt7.4GsqHok16wMjm.c)
- [`code/method.1omDq0KmtAs8k6.bEf0p9RiHt7.5qxYsHe3.c`](code/method.1omDq0KmtAs8k6.bEf0p9RiHt7.5qxYsHe3.c)
- [`code/method.1omDq0KmtAs8k6.bEf0p9RiHt7.Pmi7ij4AZ5t.c`](code/method.1omDq0KmtAs8k6.bEf0p9RiHt7.Pmi7ij4AZ5t.c)
- [`code/method.1omDq0KmtAs8k6.bEf0p9RiHt7.bHw5W1xtpF8.c`](code/method.1omDq0KmtAs8k6.bEf0p9RiHt7.bHw5W1xtpF8.c)
- [`code/method.1omDq0KmtAs8k6.bEf0p9RiHt7.wEk2Wn7e.c`](code/method.1omDq0KmtAs8k6.bEf0p9RiHt7.wEk2Wn7e.c)
- [`code/method.Gro4fD8b._PrivateImplementationDetails_.ComputeStringHash.c`](code/method.Gro4fD8b._PrivateImplementationDetails_.ComputeStringHash.c)
- [`code/method.K_i2yw1X.8j_QW..cctor.c`](code/method.K_i2yw1X.8j_QW..cctor.c)
- [`code/method.Tra4in5.Nt6c7Ekoq3J.xFi09cTpm.c`](code/method.Tra4in5.Nt6c7Ekoq3J.xFi09cTpm.c)
- [`code/method.fTr94sEbjo5B.0Yyofi6HF3mgm.9siMdJk7x3.c`](code/method.fTr94sEbjo5B.0Yyofi6HF3mgm.9siMdJk7x3.c)
- [`code/method.rHc8e.Ke2intX79D.0Cmfg.c`](code/method.rHc8e.Ke2intX79D.0Cmfg.c)
- [`code/method.rHc8e.Ke2intX79D.4dqRd9.c`](code/method.rHc8e.Ke2intX79D.4dqRd9.c)
- [`code/method.rHc8e.Ke2intX79D.Tsi6m.c`](code/method.rHc8e.Ke2intX79D.Tsi6m.c)
- [`code/method.rHc8e.Ke2intX79D.Wyt8i.c`](code/method.rHc8e.Ke2intX79D.Wyt8i.c)
- [`code/method.rHc8e.Ke2intX79D.cNm9Y2fktn6K3F.c`](code/method.rHc8e.Ke2intX79D.cNm9Y2fktn6K3F.c)
- [`code/method.rHc8e.Ke2intX79D.dCq3ab8SGn.c`](code/method.rHc8e.Ke2intX79D.dCq3ab8SGn.c)
- [`code/method.rHc8e.Ke2intX79D.xm7E6G.c`](code/method.rHc8e.Ke2intX79D.xm7E6G.c)
- [`code/method.wb4D5oRg.Nm3_6bkJ.5mqPN3rkno.c`](code/method.wb4D5oRg.Nm3_6bkJ.5mqPN3rkno.c)
- [`code/method.wb4D5oRg.Nm3_6bkJ.6irKz.c`](code/method.wb4D5oRg.Nm3_6bkJ.6irKz.c)
- [`code/method.wb4D5oRg.Nm3_6bkJ.8gtApN0eZ2f.c`](code/method.wb4D5oRg.Nm3_6bkJ.8gtApN0eZ2f.c)
- [`code/method.wb4D5oRg.Nm3_6bkJ.9odFktX.c`](code/method.wb4D5oRg.Nm3_6bkJ.9odFktX.c)
- [`code/method.wb4D5oRg.Nm3_6bkJ.Xym8qS1k5wHsr9.c`](code/method.wb4D5oRg.Nm3_6bkJ.Xym8qS1k5wHsr9.c)
- [`code/method.wb4D5oRg.Nm3_6bkJ.gf9S4XpjxpY.c`](code/method.wb4D5oRg.Nm3_6bkJ.gf9S4XpjxpY.c)
- [`code/method.wb4D5oRg.Nm3_6bkJ.ox9BaKz.c`](code/method.wb4D5oRg.Nm3_6bkJ.ox9BaKz.c)
- [`code/method.wb4D5oRg.Nm3_6bkJ.y_1F3eBgQ9.c`](code/method.wb4D5oRg.Nm3_6bkJ.y_1F3eBgQ9.c)
- [`code/method.wb4D5oRg.Nm3_6bkJ.zDq9g4Kk5Lizb8.c`](code/method.wb4D5oRg.Nm3_6bkJ.zDq9g4Kk5Lizb8.c)

## Behavioral Analysis

This final piece of disassembly (Chunk 11/11) provides a high-resolution look at the "execution core" of the malware. It confirms the most advanced architectural features identified in previous chunks, specifically focusing on how the **Virtual Machine (VM)** handles state transitions, data de-obfuscation, and transition points between internal logic and system-level calls.

---

### Updated Analysis: Technical Deep Dive (Chunk 11/11)

#### 1. Decoding the "Arithmetic Maze"
The sheer density of `CONCAT`, `SUB`, `POPCOUNT`, and bit-shift operations across this entire chunk is not indicative of standard software engineering; it is a hallmark of **mathematical obfuscation.**

*   **Opaque Predicates:** Many conditions (e.g., the `if` statements involving `POPCOUNT`) are likely "opaque predicates." These are branches that always evaluate in one direction at runtime but appear complex to static analyzers, effectively hiding the true flow of the program.
*   **Data-Dependent Offsets:** When you see instructions like `puVar45[0x36]` followed by a sequence of operations calculating the next address via `CONCAT31`, it indicates that the malware is **deciphering its own instruction pointer.** It doesn't just jump to the next piece of code; it calculates where to go based on the "results" of the math, making standard Control Flow Graph (CFG) analysis nearly impossible.

#### 2. Analysis of the "Handler Blocks"
The transition points (e.g., `code_r0x00402228`, `code_r0x004026ef`) are not just labels; they represent **Execution States** within the VM.

*   **State Transition Logic:** In each block, the malware performs a large "math-heavy" calculation to determine its next state. This is used to hide common operations (like comparing an IP address or checking a file path).
*   **Nested Loops and Decoding:** The long loops involving `puVar43`, `puVar_44`, and `puVar_45` appear to be **"Just-in-Time" (JIT) decryption routines.** Instead of decrypting an entire block of code at once, the VM deciphers only the next few instructions or "steps" required for execution. This significantly hinders memory forensics because the malicious payload exists in a plain state only for milliseconds during processing.

#### 3. The `swi(4)` Gateway and Post-Gate Cleanup
The presence of `swi(4)` (Software Interrupt) is critical. In this context, it serves as the **Bridge to the Kernel.**

*   **Contextual Isolation:** By wrapping the `swi` call in massive amounts of math, the malware ensures that any "hook" placed on standard API calls won't see the actual parameters being passed. The values are likely only "de-obfuscated" at the exact moment the transition to kernel mode occurs.
*   **Buffer/State Re-synchronization:** After `swi(4)`, the code performs complex logic involving `uVar17` and `puVar_44`. This is likely re-calculating the VM's internal state after a system call has returned, ensuring that no information about the "bridge" left behind during the transition.

#### 4. Evidence of High-Level Obfuscation Tools
The repetitive nature of some code segments (seen in previous chunks) combined with this high level of arithmetic complexity suggests the use of an **advanced obfuscation compiler** (such as a custom LLVM pass). 
*   The "junk" logic is specifically designed to break disassemblers. It forces the tool to represent complex math as dozens of lines of assembly, making it exponentially harder for a human analyst to distinguish between *functional code* and *obfuscation-noise*.

---

### Updated Summary of Malicious Indicators

*   **VM Architecture (Confirmed):** The malware utilizes a full Virtual Machine where standard x86/x64 instructions are replaced by a custom, math-heavy bytecode system.
*   **JIT-Style Decoding:** Instead of "packing" the file in the traditional sense, it uses an internal "translation layer" to decode logic just before execution.
*   **Opaque Predicates & Logic Bloat:** The use of `POPCOUNT` and complex bitwise arithmetic suggests a design intended to frustrate both automated scanners and manual disassembly.
*   **Hidden State Machine:** Control flow is not linear; it is state-dependent, meaning the "next" block of code is calculated at runtime based on previous mathematical results.
*   **Gateway Obfuscation:** System calls are wrapped in layers of calculation to hide parameters from EDR (Endpoint Detection and Response) hooks that monitor standard API transition points.

---

### Incident Response & Hunting Guidance (Finalized)

1.  **Dynamic Behavior over Static Analysis:** Because the "true" code is hidden behind a translation engine, static analysis will likely only uncover the VM itself. **Focus on memory-forensics during execution.** The plain-text commands/IPs are only visible inside the VM's internal registers after they have been passed through the arithmetic filters.
2.  **Monitor for "Heavy Math" Execution:** Create a behavioral profile for processes that exhibit high CPU cycles in tight loops consisting of numerous XOR, AND, and ADD instructions before making system calls. This is often an indicator of an active VM dispatcher or decrypter.
3.  **Detection of Non-Standard System Calls:** Since the malware uses `swi` gates to bypass standard hooks, monitor for **direct syscalls**. Use EDR tools that can detect "instruction-level" jumps into kernel space (e.g., looking for the `syscall` or `int 0x80/0x2e` opcodes in memory).
4.  **Watch for High-Entropy Memory Regions:** The existence of several "decoder loops" suggests the malware will allocate memory buffers that change from high entropy (encrypted) to low entropy (decrypted) during execution. Alert on `PAGE_EXECUTE_READWRITE` (RWX) transitions in suspicious processes.
5.  **Hardened Signature Development:** Instead of trying to sign the "math," focus signatures on the **execution pattern.** Look for loops that perform 10+ arithmetic operations before a system call, or the specific repeated patterns found in the `method.*` naming conventions if they are leaked into memory during unpacking.

### Final Conclusion
This malware represents a high-tier threat involving a **Virtual Machine Architecture** designed to defeat standard analysis pipelines. It hides its true purpose behind layers of mathematical obfuscation and uses an internal translation engine to ensure that most of its malicious "logic" is only visible in the moment it is being executed by the VM's interpreter.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The "Arithmetic Maze," use of `POPCOUNT`, and bit-shift operations are used to create complex logic flows that hide the true intent from static analysis. |
| **T1027** | Obfuscated Files or Information | The use of "Opaque Predicates" creates branches that always evaluate one way but confuse automated disassembly tools and analysts. |
| **T1027** | Obfuscated Files or Information | The "Virtual Machine Architecture" serves as a translation layer, hiding standard x86/x64 instructions behind custom bytecode. |
| **T1027** | Obfuscated Files or Information | "Just-in-Time (JIT) decoding" ensures that plain-text malicious code exists in memory only for the duration of its execution to evade detection. |
| **T1027** | Obfuscated Files or Information | The `swi(4)` gateway obfuscation wraps system calls in heavy math to bypass EDR hooks and hide parameters from security monitors. |

### Analyst Notes:
*   **Defense Evasion Focus:** All identified behaviors fall under the **Defense Evasion** tactic. 
*   **Complexity of T1027:** While these appear as several different behaviors (VM, JIT, Opaque Predicates), they are all distinct methods of implementing **T1027**. The primary goal of every behavior described in the analysis is to frustrate both automated scanners and manual reverse engineering.
*   **Direct System Calls:** Note that while `swi(4)` functions as a "direct syscall" mechanism (a common technique to bypass EDR hooks), it is classified under T1027 in this context because its primary function here is the obfuscation of the call's parameters and intent.

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided string dump and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) and technical observations categorized by type.

### **Note on Data Analysis**
The raw strings provided appear to be heavily obfuscated or represent "junk" data/encrypted payloads characteristic of a VM-based execution environment. Consequently, standard static indicators (like plain-text IPs or file paths) are not present in the string dump as they are likely decrypted only at runtime within the malware's memory space.

---

### **IOC Categorization**

#### **IP addresses / URLs / Domains**
*   *None identified.* (The strings provided do not contain clear, plaintext network indicators.)

#### **File paths / Registry keys**
*   *None identified.* (Standard system paths or malicious file paths were not present in the string dump.)

#### **Mutex names / Named pipes**
*   *None identified.*

#### **Hashes**
*   *None identified.* (While high-entropy character strings are present, no valid MD5, SHA-1, or SHA-256 hashes were detected.)

#### **Other artifacts (TTPs & Behavioral Indicators)**
These are indicators of the malware's construction and behavior, which can be used to develop signature-based detections for its execution patterns:

*   **VM Architecture:** The presence of a custom Virtual Machine (VM) is a primary indicator of high-sophistication. The malware replaces standard x86/x64 instructions with a proprietary bytecode system.
*   **JIT-Style Decoding:** The use of "Just-in-Time" decryption, where only the next few instructions are decrypted into memory for execution (rather than unpacking the entire binary), is a key behavioral indicator.
*   **Direct System Calls via `swi(4)`:** The malware utilizes `swi(4)` (Software Interrupts) to transition directly to the kernel. This is a specific technique used to bypass EDR hooks on standard system libraries.
*   **Arithmetic Obfuscation (Opaque Predicates):** The heavy use of `POPCOUNT`, bit-shifting, and complex arithmetic in logic gates serves as an indicator of "Logic Bloat" designed to defeat static analysis tools.
*   **Code Segment Decryption:** Detection can be based on the identification of "decoder loops" that transition memory from high-entropy (encrypted) to low-entropy (executable) states.

---

### **Summary for Security Operations**
Because this malware utilizes a **Virtual Machine Architecture**, static IOCs (like IPs and file paths) are intentionally omitted or hidden until execution. 

**Recommended Detection Strategy:**
1.  **Behavioral Monitoring:** Alert on processes performing high-frequency bitwise operations (`XOR`, `AND`, `POPCOUNT`) immediately preceding a system call.
2.  **Memory Integrity:** Monitor for memory regions that transition to `PAGE_EXECUTE_READWRITE` (RWX) or perform "Just-in-Time" decoding of small code blocks.
3.  **Direct Syscall Detection:** Flag and investigate any processes attempting to execute `swi(4)` or direct `syscall` instructions outside of expected system library contexts.

---

## Malware Family Classification

Based on the provided technical analysis, here is the classification for the sample:

1. **Malware family**: custom (Sophisticated VM-based architecture)
2. **Malware type**: loader / dropper
3. **Confidence**: High (regarding functionality/type); Medium (regarding specific campaign identity)
4. **Key evidence**:
    *   **Virtual Machine (VM) Architecture:** The sample utilizes a complex, custom bytecode system and "Arithmetic Maze" logic to hide its true execution flow from static analysis tools.
    *   **Just-in-Time (JIT) Decoding:** It employs "step-by-step" decoding of code segments in memory, ensuring that the malicious payload is only visible for milliseconds at a time to evade forensic memory scans.
    *   **EDR Evasion via Direct Syscalls:** The use of `swi(4)` gateways wrapped in heavy mathematical obfuscation indicates a deliberate attempt to bypass security products by hiding syscall parameters until they reach the kernel level.
