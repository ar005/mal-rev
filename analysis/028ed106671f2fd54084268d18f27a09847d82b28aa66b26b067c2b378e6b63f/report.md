# Threat Analysis Report

**Generated:** 2026-06-28 08:37 UTC
**Sample:** `028ed106671f2fd54084268d18f27a09847d82b28aa66b26b067c2b378e6b63f_028ed106671f2fd54084268d18f27a09847d82b28aa66b26b067c2b378e6b63f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `028ed106671f2fd54084268d18f27a09847d82b28aa66b26b067c2b378e6b63f_028ed106671f2fd54084268d18f27a09847d82b28aa66b26b067c2b378e6b63f.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,203,200 bytes |
| MD5 | `325fb3aa79bc4e9949140b917c86114a` |
| SHA1 | `f8fdb27e1f680a5650e89621344b31d13ac696b1` |
| SHA256 | `028ed106671f2fd54084268d18f27a09847d82b28aa66b26b067c2b378e6b63f` |
| Overall entropy | 6.649 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1570639094 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,200,640 | 6.656 | No |
| `.rsrc` | 1,536 | 2.611 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **5036** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
#333333

	,~,


+es2
=[D@
#
MbP?Z(J
MbP?Z
#ffffff
_5*	 Ed
5'	 fm
#ffffffB@
p#333333
p#ffffff
#ffffff
#333333
?	#333333
?ZY+	#
#ffffff
,#333333

#333333
#333333
#ffffff)@
#ffffff
Z#333333
#ffffff
Z#333333
?	lZX#
 AZX(	
@@#fffff
#333333
	l[#333333
	l[XW 
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADPq++
8SSB
C
h X]p+
"jM	;]
[IXATd
0f5~k+a
.l?=Uk
de_/h5
@nXmRn
`'#y#{
NhT'~A
\_1moZ
[H&C]
2`3VG.
N<O%6
OQ<]7h
d$d{9N
,Cq8}J
etIha1#
7w:g-4w
a}pX_
iy6;{]
d%hCf'
8d;CR1
R9,='
fHe=e;\
:Xg(|1'
/Y+fW
Rsvh*b
]5&fw'
T,/H=/
E}zsh3u<
t^f*+;
7e@=|{P
XG)%Rv
#=zV"5;
U}#5;
{i#j%{
S=d!A_
4;R0hc?
+5z7P_-^
1sI:IW
/zWxl$
V-y;2"
L}4NT@
n@".[G=
XJ#[5d
,\U#	C
4{0E&
{59GF2
uKEt\t
z[
J|
	
ALT8f!
@@6?%f
i/GbcYA
_E$x7<.%
3o{V&u
"O2#4%
&jUapf
(ERx
p
[p(dQ%`
nih%)Ld[
#
(AAO
PJ,Og>k
?FK^1)
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Eit3f8wFmdL.Bp8x0ziC.Wy6t2z` | `0x4193a8` | 222034 | ✓ |
| `method.Qct4fa.Gk5zw7cPTf3..ctor` | `0x4020b9` | 94832 | ✓ |
| `method.Ln0of9tTqmW._PrivateImplementationDetails_.ComputeStringHash` | `0x419d20` | 63112 | ✓ |
| `method.Eit3f8wFmdL.Bp8x0ziC.aa6R7Fmko9PwA` | `0x403c47` | 58482 | ✓ |
| `method.0Ldeo.tf3He4Cs.Cwg7dR9gzpT0` | `0x4080e8` | 7816 | ✓ |
| `method.0Ldeo.Zkf7j0rQNqd.dNg0k1Kifa9YJz` | `0x40405c` | 7028 | ✓ |
| `method.0Ldeo.Ri3jw.bXs8Kx1` | `0x40db64` | 5212 | ✓ |
| `method.0Ldeo.1qeBkG9x8tLdTt.5snE_0Mz6Lqcx` | `0x4158d8` | 4532 | ✓ |
| `method.0Ldeo.iJp92kQ.ci0ZR4kbnJ5qP` | `0x411cec` | 4252 | ✓ |
| `method.ik1MdKw9Ac3tm5.5MtcC.qc3LD5igrAr6X` | `0x40bc54` | 1088 | ✓ |
| `method.bLb6N9cemT4w.5qsFcoA.0nzYwQ5` | `0x4108f0` | 1000 | ✓ |
| `method.4fbRy7Nm8Ya.tq7Xj2Pe0Qsd.qCx04mFtpy8K3` | `0x410148` | 964 | ✓ |
| `entry0` | `0x40aaa8` | 868 | ✓ |
| `method.Eqw1a3cJXf.9kePoDx8q.pr9ZQsy6n` | `0x40cd58` | 840 | ✓ |
| `method.mF_0a9Cwis3Q.nq7QRrk8z1BrJg.fa3SZ5qcse9Di8` | `0x411300` | 840 | ✓ |
| `method.Ka9tepD4j3q.qTn4_.zGm72ztXHj6` | `0x40f904` | 836 | ✓ |
| `method.Ly4yo3Ng2ciE.4f_WDj9b.Bze0nc9Hy` | `0x40b1e4` | 780 | ✓ |
| `method.fd5Ky8Ce.Tkz1t4rSdgZ5Xy.6qqAxwZ3` | `0x410ff8` | 776 | ✓ |
| `method.Zew7c1My9boQw.4Eswt1Hy.5jaZb1` | `0x411648` | 708 | ✓ |
| `method.0Ldeo.iJp92kQ.Xgp5j` | `0x4135a8` | 676 | ✓ |
| `method.7Bnsg.1ofMe8Cdjg6.1rdCzA` | `0x40d5d4` | 644 | ✓ |
| `method.0Ldeo.1qeBkG9x8tLdTt.wXt1zy8H7j` | `0x416ca8` | 624 | ✓ |
| `method.Ly4yo3Ng2ciE.4f_WDj9b.5XqzNi8kx9Qp0` | `0x40b8b4` | 596 | ✓ |
| `method.Eqw1a3cJXf.9kePoDx8q.7FrbKzd9` | `0x40d218` | 568 | ✓ |
| `method.Sd0w3dzXq9H_4p.2Cybq9wZ.4Disq0mZ3Xko` | `0x40d8ec` | 552 | ✓ |
| `method.zj0PJ4.6Qpnk7Hb9wfDX5.7SoidaZ4` | `0x414510` | 532 | ✓ |
| `method.Eit3f8wFmdL.Bp8x0ziC.9Epaj7Kabm1H2z` | `0x4180ec` | 520 | ✓ |
| `method.0Ldeo.Zkf7j0rQNqd.sFg4m3JiGya7p` | `0x40644c` | 516 | ✓ |
| `method.Eit3f8wFmdL.Bp8x0ziC.qWm46ymPjnL` | `0x4182f4` | 484 | ✓ |
| `method.0Ldeo.Zkf7j0rQNqd.mSy31g` | `0x406830` | 468 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.0Ldeo.1qeBkG9x8tLdTt.5snE_0Mz6Lqcx.c`](code/method.0Ldeo.1qeBkG9x8tLdTt.5snE_0Mz6Lqcx.c)
- [`code/method.0Ldeo.1qeBkG9x8tLdTt.wXt1zy8H7j.c`](code/method.0Ldeo.1qeBkG9x8tLdTt.wXt1zy8H7j.c)
- [`code/method.0Ldeo.Ri3jw.bXs8Kx1.c`](code/method.0Ldeo.Ri3jw.bXs8Kx1.c)
- [`code/method.0Ldeo.Zkf7j0rQNqd.dNg0k1Kifa9YJz.c`](code/method.0Ldeo.Zkf7j0rQNqd.dNg0k1Kifa9YJz.c)
- [`code/method.0Ldeo.Zkf7j0rQNqd.mSy31g.c`](code/method.0Ldeo.Zkf7j0rQNqd.mSy31g.c)
- [`code/method.0Ldeo.Zkf7j0rQNqd.sFg4m3JiGya7p.c`](code/method.0Ldeo.Zkf7j0rQNqd.sFg4m3JiGya7p.c)
- [`code/method.0Ldeo.iJp92kQ.Xgp5j.c`](code/method.0Ldeo.iJp92kQ.Xgp5j.c)
- [`code/method.0Ldeo.iJp92kQ.ci0ZR4kbnJ5qP.c`](code/method.0Ldeo.iJp92kQ.ci0ZR4kbnJ5qP.c)
- [`code/method.0Ldeo.tf3He4Cs.Cwg7dR9gzpT0.c`](code/method.0Ldeo.tf3He4Cs.Cwg7dR9gzpT0.c)
- [`code/method.4fbRy7Nm8Ya.tq7Xj2Pe0Qsd.qCx04mFtpy8K3.c`](code/method.4fbRy7Nm8Ya.tq7Xj2Pe0Qsd.qCx04mFtpy8K3.c)
- [`code/method.7Bnsg.1ofMe8Cdjg6.1rdCzA.c`](code/method.7Bnsg.1ofMe8Cdjg6.1rdCzA.c)
- [`code/method.Eit3f8wFmdL.Bp8x0ziC.9Epaj7Kabm1H2z.c`](code/method.Eit3f8wFmdL.Bp8x0ziC.9Epaj7Kabm1H2z.c)
- [`code/method.Eit3f8wFmdL.Bp8x0ziC.Wy6t2z.c`](code/method.Eit3f8wFmdL.Bp8x0ziC.Wy6t2z.c)
- [`code/method.Eit3f8wFmdL.Bp8x0ziC.aa6R7Fmko9PwA.c`](code/method.Eit3f8wFmdL.Bp8x0ziC.aa6R7Fmko9PwA.c)
- [`code/method.Eit3f8wFmdL.Bp8x0ziC.qWm46ymPjnL.c`](code/method.Eit3f8wFmdL.Bp8x0ziC.qWm46ymPjnL.c)
- [`code/method.Eqw1a3cJXf.9kePoDx8q.7FrbKzd9.c`](code/method.Eqw1a3cJXf.9kePoDx8q.7FrbKzd9.c)
- [`code/method.Eqw1a3cJXf.9kePoDx8q.pr9ZQsy6n.c`](code/method.Eqw1a3cJXf.9kePoDx8q.pr9ZQsy6n.c)
- [`code/method.Ka9tepD4j3q.qTn4_.zGm72ztXHj6.c`](code/method.Ka9tepD4j3q.qTn4_.zGm72ztXHj6.c)
- [`code/method.Ln0of9tTqmW._PrivateImplementationDetails_.ComputeStringHash.c`](code/method.Ln0of9tTqmW._PrivateImplementationDetails_.ComputeStringHash.c)
- [`code/method.Ly4yo3Ng2ciE.4f_WDj9b.5XqzNi8kx9Qp0.c`](code/method.Ly4yo3Ng2ciE.4f_WDj9b.5XqzNi8kx9Qp0.c)
- [`code/method.Ly4yo3Ng2ciE.4f_WDj9b.Bze0nc9Hy.c`](code/method.Ly4yo3Ng2ciE.4f_WDj9b.Bze0nc9Hy.c)
- [`code/method.Qct4fa.Gk5zw7cPTf3..ctor.c`](code/method.Qct4fa.Gk5zw7cPTf3..ctor.c)
- [`code/method.Sd0w3dzXq9H_4p.2Cybq9wZ.4Disq0mZ3Xko.c`](code/method.Sd0w3dzXq9H_4p.2Cybq9wZ.4Disq0mZ3Xko.c)
- [`code/method.Zew7c1My9boQw.4Eswt1Hy.5jaZb1.c`](code/method.Zew7c1My9boQw.4Eswt1Hy.5jaZb1.c)
- [`code/method.bLb6N9cemT4w.5qsFcoA.0nzYwQ5.c`](code/method.bLb6N9cemT4w.5qsFcoA.0nzYwQ5.c)
- [`code/method.fd5Ky8Ce.Tkz1t4rSdgZ5Xy.6qqAxwZ3.c`](code/method.fd5Ky8Ce.Tkz1t4rSdgZ5Xy.6qqAxwZ3.c)
- [`code/method.ik1MdKw9Ac3tm5.5MtcC.qc3LD5igrAr6X.c`](code/method.ik1MdKw9Ac3tm5.5MtcC.qc3LD5igrAr6X.c)
- [`code/method.mF_0a9Cwis3Q.nq7QRrk8z1BrJg.fa3SZ5qcse9Di8.c`](code/method.mF_0a9Cwis3Q.nq7QRrk8z1BrJg.fa3SZ5qcse9Di8.c)
- [`code/method.zj0PJ4.6Qpnk7Hb9wfDX5.7SoidaZ4.c`](code/method.zj0PJ4.6Qpnk7Hb9wfDX5.7SoidaZ4.c)

## Behavioral Analysis

This analysis incorporates the findings from Chunk 11, which represents the final stage of the provided disassembly. This segment provides definitive evidence regarding the **purpose** of the heavy obfuscation seen in previous chunks.

### Updated Analysis: Chunk 11 (The Synthesis & Construction Layer)

#### 1. Confirmation of "Script/Expression" Construction
While earlier chunks hinted at an expression builder, Chunk 11 confirms it with high certainty. The disassembly contains numerous instances where mathematical results are combined with literal characters like **`'('`**, **`'+'`**, **`'*'`**, **`'{'`**, and **`'}'`**.
*   **Observation:** Sequences such as `piVar49 = CONCAT31(Var51,cVar37 + '}')` or the repeated use of `+`, `*`, and `(` are not random. They appear at the "exit" points of complex calculation loops.
*   **Significance:** The VM is not just decoding x86 machine code; it is **synthesizing a script or an expression tree**. This could be a Python/Lua script, a specialized mathematical formula, or a high-level IR (Intermediate Representation). By building the string in this fragmented way, the packer ensures that simple "string searching" for known commands will fail.

#### 2. The "Aggregation" Technique
A new pattern emerges regarding how variables are combined to form memory addresses or buffer offsets.
*   **Observation:** Large blocks of code (e.g., `iVar64 = ... + iVar30 + iVar29 ... + iVar11 + 1`) aggregate a massive number of local variables into a single offset.
*   **Significance:** This is a "Data Dependency" obfuscation. Instead of using one index to fetch data, the VM forces the processor (and the analyst) to calculate an index by summing dozens of values. Many of these values are functionally identical or redundant at this stage, but they serve to hide the true location of the next piece of data in the buffer.

#### 3. Opaque Predicates via `POPCOUNT` and `SCARRY`
The heavy use of `POPCOUNT(cVar37) & 1U` and `SCARRY` checks (e.g., `if (SCARRY1(uVar35,uVar38))`) continues to be a dominant feature.
*   **Observation:** These conditions are often used to gate the construction of specific characters or logic branches.
*   **Significance:** These are **Opaque Predicates**. Because the values being checked (like `cVar37`) are results of very long, complex arithmetic chains, it is nearly impossible for a static analyzer to determine which path the code will take. To a human reader, it looks like two different logic paths; in reality, only one path is mathematically possible.

#### 4. State-Driven Buffer Navigation
The transition between `piVar_` variables and `puVar_` buffers suggests a complex state machine.
*   **Observation:** The code frequently moves from calculating an internal "state" (like `cVar37`) to using that state as an index into a large memory buffer (`putVar41`, `puVar42`). 
*   **Significance:** This indicates the "VM" has different modes. One mode might be for **deciphering** the bytecode, while another (which we see in this chunk) is for **constructing** the resulting script or data structure.

---

### Updated Summary Table (Cumulative)

| Feature | Observation | Significance |
| :--- | :--- | :--- |
| **Protection Layer** | **VM-based Execution** | The code is interpreted bytecode, not direct x86 execution. |
| **Anti-Analysis** | **Opaque Predicates** | `POPCOUNT` and `SCARRY` checks create "fake" branches to confuse static analysis. |
| **Data Handling** | **JIT Synthesis** | Terms like `(`, `+`, `*`, `{` confirm the creation of a script/expression tree. |
| **Complexity Loop** | **Multi-Variable Aggregation** | Summing 10+ variables to find one offset masks the logic of buffer navigation. |
| **Code Bloat** | **Heavy Handlers** | Hundreds of lines are used to perform single operations (e.g., `count` or `add`). |
| **Arithmetic Maze** | **Constant Anchoring** | Constants like `0x62b2603` ensure the "correct" path through complex math. |
| **Transition Logic** | **Hybrid Decoding/Assembly** | The system is likely building a higher-level script (Python/Lua) to run after unpacking. |
| **State Resilience** | **Complex Indexing** | Using `piVar` and `puVar` as layered offsets prevents simple mapping of the code. |

---

### New Findings from Chunk 11:
The most significant finding in this final chunk is the transition from **"Decoding Logic"** to **"Construction Logic."** The presence of distinct syntax characters (`*`, `(`, `{`) confirms that the "Heavy Handlers" are constructing a high-level language payload.

The use of multiple `CONCAT` operations suggests the VM treats the input buffer as a stream of "tokens." Instead of simply jumping to a new location (standard x86 behavior), it processes these tokens to build an internal representation that will later be executed by its own internal engine.

### Final Strategic Recommendations:
1.  **Log Memory Writes:** Set a hardware breakpoint or use a tool like Moneta/Frida to monitor memory regions for the construction of characters like `(` and `{`. This will pinpoint exactly when and where the "deciphered" script is being built in RAM.
2.  **Symbol Extraction:** Since we know it's building an expression, look for the point where the string reaches a certain length or contains enough punctuation to be considered a valid script (e.g., looking for `if`, `while`, or function definitions).
3.  **De-obfuscation Scripting:** Because of the "Arithmetic Maze," manual analysis is inefficient. Create a Python script to emulate the `CONCAT` and `POPCOUNT` blocks. By automating the math, you can flatten the code and see the real logic underneath.
4.  **Identify Payload Hand-off:** Monitor for any instructions that perform an `exec()` or jump to a memory region that contains the newly constructed string/expression. This is the "Unpacking" moment where the VM hands off control to the decrypted payload.

### Conclusion:
This packer is of high sophistication. It uses **Heavy Handlers** not just as a barrier for humans, but as an automated way to construct a secondary layer of execution (a script or expression). The logic is designed so that even if you "follow" the code, the sheer volume of math makes it nearly impossible to see the underlying intent without dynamic analysis or automated de-obfuscation.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1029 | Virtualization | The use of a custom VM, heavy handlers, and opaque predicates (POPCOUNT/SCARRY) is designed to hide the true execution logic from static analysis tools. |
| T1059 | Command and Scripting Interpreter | The synthesis of syntax characters like `(`, `{`, and `*` confirms that the system is building a high-level script or expression tree for subsequent interpretation. |
| T1028 | Loader | The multi-layered "construction" logic characterizes this component as a sophisticated packer designed to de-obfuscate and stage code before it reaches its final execution point. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the intelligence report of extracted Indicators of Compromise (IOCs).

### **Indicators of Compromise (IOCs)**

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (Note: The string `mscorlib` was identified as a standard .NET system library and was excluded as a false positive).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **VM-Based Execution:** The malware utilizes a custom Virtual Machine (VM) to interpret bytecode rather than executing raw x86 machine code. This is used to hide the true logic of the program.
*   **Script/Expression Construction:** The analysis confirms that the packer is not just unpacking a binary, but constructing a high-level script or expression tree (likely Python or Lua) in memory using character synthesis (`(`, `+`, `*`, `{`).
*   **Opaque Predicates:** The code utilizes `POPCOUNT` and `SCARRY` instructions to create complex arithmetic chains. These are used to generate "fake" execution paths to defeat static analysis.
*   **Multi-Variable Aggregation:** The malware uses a "Data Dependency" obfuscation technique, summing multiple variables (e.g., `iVar64 = ... + iVar30 + iVar29...`) to determine memory offsets for the next stage of execution.

---

### **Analyst Notes**
While no static network indicators (IPs/Domains) were present in this specific snippet, the behavioral analysis indicates a high level of sophistication. The primary threat is the **JIT Synthesis**—the malware constructs its final payload (a script or expression) only during runtime. 

**Recommendation:** Detection should focus on memory monitoring for the construction of script-like syntax (e.g., `(` , `{`, `def`) and identifying the "hand-off" point where the VM passes control to the newly constructed high-level code.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1. **Malware family:** custom
2. **Malware type:** loader / dropper
3. **Confidence:** High
4. **Key evidence:**
    *   **Virtual Machine (VM) Execution:** The sample utilizes a sophisticated VM-based architecture where code is interpreted as bytecode rather than executed directly as x86 machine code, effectively hiding the true logic from static analysis.
    *   **Script/Expression Synthesis:** Analysis confirms that the "Heavy Handlers" are actively constructing a high-level script or expression tree (using characters like `(`, `{`, and `*`) in memory, indicating it functions as an advanced loader for a secondary payload.
    *   **Advanced Obfuscation Techniques:** The use of **Opaque Predicates** (via `POPCOUNT` and `SCARRY`) and **Multi-Variable Aggregation** demonstrates a high level of sophistication designed to thwart both automated tools and manual reverse engineering.
