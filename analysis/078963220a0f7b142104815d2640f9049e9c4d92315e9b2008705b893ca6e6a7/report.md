# Threat Analysis Report

**Generated:** 2026-07-16 21:03 UTC
**Sample:** `078963220a0f7b142104815d2640f9049e9c4d92315e9b2008705b893ca6e6a7_078963220a0f7b142104815d2640f9049e9c4d92315e9b2008705b893ca6e6a7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `078963220a0f7b142104815d2640f9049e9c4d92315e9b2008705b893ca6e6a7_078963220a0f7b142104815d2640f9049e9c4d92315e9b2008705b893ca6e6a7.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 276,480 bytes |
| MD5 | `5fa4d3a8dd96a9d7300788ac2ec902c3` |
| SHA1 | `2c2deba1eaa10de40c55326cf9615b593d2f1f11` |
| SHA256 | `078963220a0f7b142104815d2640f9049e9c4d92315e9b2008705b893ca6e6a7` |
| Overall entropy | 6.99 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3094332148 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 187,392 | 6.958 | No |
| `.rsrc` | 88,064 | 6.895 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1009** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
l^1"09
bD`zh4
/9cCaE
:9puX/8G
6j~wZ50
yz+`p"
a4>3H?
A]X@2:
-s/|R
Fm)sA\
-x;_?*NP
s[
;g&
j7<ofJ
z}jJ5k
jMQD 
&$};]w
3	pTtBv
u)$cz

X&X70C
[d:Dm6)
z={:P4
-tQD_>n_
O(Fr[cBU
vVdJDP"
g2P	/k
d64P5?
:_'0v>
0_@*P+,
+r(pbi
o|@T]ZyJ
KYP`0GL
U(kyd]
Pq+
;}
FllORf
moQjUA[
!!(5j_	
+OdKid
3PnhC$jU
A}32-8
gR|X\
+%V1y?
`=Vb\~Z*
E!y>YZ
 T+{m(
bvN+=2
t@uG%
`a#aB)
b_OY7bw
B]91m
iIRz\
5\hKLq
9rDQ{L?m
-s		)T
m%|w#
22a<4'D
J)P+Z
~{k+B9:
?fLBJ

MQP8Q5
y`bb_h)
(<[eb=
zrd[Z.Wh
N
|'?:H
=pTG1H
FHK#T+}NNsH
AfD!aTC
nzEdEe
FakcX$
=`sqf:
hmNE@[
+'jTU

R*C/
a-kavI
_>)JpU
?3z[Vj
DLm6>Rlv
JtF>4X
Fys	19
155Pnl
	uZ5l
HO#\Rl
9]#a,a
*|d@Gk
X'$-]~
P(J?mz
_&^++[
W^h?Ptqm
d|\^c$
G:F*MM
/<mrs{
slkD=CN
f)+'?FZ
?10!l~
me%-N	
:}KZ=SG$7
?|mz=p
z9>&fe
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x403b14` | 83884 | ✓ |
| `sym.__StaticArrayInitTypeSize32..cctor` | `0x418328` | 76154 | ✓ |
| `method.e5xjuvSKTJDGdhfIKe..cctor` | `0x405328` | 59372 | ✓ |
| `method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.hvro2fIQji` | `0x423448` | 17024 | ✓ |
| `method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.AwBouxn3PB` | `0x41f7ec` | 15408 | ✓ |
| `method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.AtioXb3XNL` | `0x41c0c4` | 14120 | ✓ |
| `method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.UM9o0el5bP` | `0x418cc4` | 13312 | ✓ |
| `method.Taskmgr.yarak.klass.hIiQN0uL9` | `0x402a50` | 2712 | ✓ |
| `method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.X8vogNWOvi` | `0x418424` | 1712 | ✓ |
| `method.__StaticArrayInitTypeSize18..cctor` | `0x427f74` | 948 | ✓ |
| `method.Taskmgr.yarak.klass.CJMUObInE` | `0x402758` | 760 | ✓ |
| `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.N9Ef01R11` | `0x403e00` | 672 | ✓ |
| `method.Taskmgr.yarak.klass.xkNP2vcre` | `0x402554` | 472 | ✓ |
| `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.vKJ9UZUAT` | `0x40491c` | 436 | ✓ |
| `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.pURc09pHG` | `0x404ad0` | 412 | ✓ |
| `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.FAQLZkrZW` | `0x403854` | 376 | ✓ |
| `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.n3eunvmbs` | `0x4041a4` | 332 | ✓ |
| `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.QNpncB7i3` | `0x4039cc` | 328 | ✓ |
| `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.d9dkcdSqq` | `0x4047d4` | 328 | ✓ |
| `method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.r2NoJXwt66` | `0x4276c8` | 308 | ✓ |
| `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.mjY23dxWU` | `0x40447c` | 304 | ✓ |
| `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.XGdjhfIKe` | `0x4046ac` | 296 | ✓ |
| `method.CN0uL9NWkyfZUsXgpc.bPaooD3ZHI` | `0x404da4` | 292 | ✓ |
| `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE..cctor` | `0x403748` | 268 | ✓ |
| `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.qdAX14ofO` | `0x4040a0` | 260 | ✓ |
| `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.YsAEoY0EN` | `0x404378` | 260 | ✓ |
| `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.nxjZuvKTJ` | `0x4045bc` | 240 | ✓ |
| `method.Taskmgr.yarak.klass..cctor` | `0x402438` | 232 | ✓ |
| `method.Taskmgr.yarak.klass.Run` | `0x4034e8` | 228 | ✓ |
| `method.Taskmgr.RegisterScreen.SDZMMs2gj` | `0x40232c` | 224 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.CN0uL9NWkyfZUsXgpc.bPaooD3ZHI.c`](code/method.CN0uL9NWkyfZUsXgpc.bPaooD3ZHI.c)
- [`code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE..cctor.c`](code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE..cctor.c)
- [`code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.FAQLZkrZW.c`](code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.FAQLZkrZW.c)
- [`code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.N9Ef01R11.c`](code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.N9Ef01R11.c)
- [`code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.QNpncB7i3.c`](code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.QNpncB7i3.c)
- [`code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.XGdjhfIKe.c`](code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.XGdjhfIKe.c)
- [`code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.YsAEoY0EN.c`](code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.YsAEoY0EN.c)
- [`code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.d9dkcdSqq.c`](code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.d9dkcdSqq.c)
- [`code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.mjY23dxWU.c`](code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.mjY23dxWU.c)
- [`code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.n3eunvmbs.c`](code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.n3eunvmbs.c)
- [`code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.nxjZuvKTJ.c`](code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.nxjZuvKTJ.c)
- [`code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.pURc09pHG.c`](code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.pURc09pHG.c)
- [`code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.qdAX14ofO.c`](code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.qdAX14ofO.c)
- [`code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.vKJ9UZUAT.c`](code/method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE.vKJ9UZUAT.c)
- [`code/method.Taskmgr.RegisterScreen.SDZMMs2gj.c`](code/method.Taskmgr.RegisterScreen.SDZMMs2gj.c)
- [`code/method.Taskmgr.yarak.klass..cctor.c`](code/method.Taskmgr.yarak.klass..cctor.c)
- [`code/method.Taskmgr.yarak.klass.CJMUObInE.c`](code/method.Taskmgr.yarak.klass.CJMUObInE.c)
- [`code/method.Taskmgr.yarak.klass.Run.c`](code/method.Taskmgr.yarak.klass.Run.c)
- [`code/method.Taskmgr.yarak.klass.hIiQN0uL9.c`](code/method.Taskmgr.yarak.klass.hIiQN0uL9.c)
- [`code/method.Taskmgr.yarak.klass.xkNP2vcre.c`](code/method.Taskmgr.yarak.klass.xkNP2vcre.c)
- [`code/method.__StaticArrayInitTypeSize18..cctor.c`](code/method.__StaticArrayInitTypeSize18..cctor.c)
- [`code/method.e5xjuvSKTJDGdhfIKe..cctor.c`](code/method.e5xjuvSKTJDGdhfIKe..cctor.c)
- [`code/method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.AtioXb3XNL.c`](code/method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.AtioXb3XNL.c)
- [`code/method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.AwBouxn3PB.c`](code/method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.AwBouxn3PB.c)
- [`code/method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.UM9o0el5bP.c`](code/method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.UM9o0el5bP.c)
- [`code/method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.X8vogNWOvi.c`](code/method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.X8vogNWOvi.c)
- [`code/method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.hvro2fIQji.c`](code/method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.hvro2fIQji.c)
- [`code/method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.r2NoJXwt66.c`](code/method.zhCoPa6D3ZHIBD0vqv.yLnJV7RxLUWxi1gOCW.r2NoJXwt66.c)
- [`code/sym.__StaticArrayInitTypeSize32..cctor.c`](code/sym.__StaticArrayInitTypeSize32..cctor.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis. The new data confirms the high level of sophistication in the obfuscation techniques used by this binary.

### Updated Comprehensive Analysis

#### 1. Core Functionality and Purpose (Updated)
The analysis confirms that this is a **highly sophisticated packer or "stub"** for a multi-stage malware infection. The second chunk of code reveals several layers of protection:
*   **Static Constructor Abuse:** The presence of `.cctor` methods (e.g., `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE..cctor`) indicates this is a **.NET binary** that has been processed by a professional obfuscator (such as Dotfuscix or ConfuserEx). These constructors are used to perform heavy "pre-processing" (decryption, integrity checks) before the main logic of the program can begin.
*   **Execution Hand-off:** The detection of an **indirect jump/call** at the end of `qdAX14ofO` (`(**(pcVar5 | 0xffff8a38))();`) is a critical finding. This indicates the point where the "loader" finishes its job and hands execution over to the actual malicious payload, which likely resides in memory in an unpacked state.

#### 2. Advanced Obfuscation & Anti-Analysis Techniques
The second chunk of disassembly highlights several advanced techniques used to hinder both manual and automated analysis:

*   **Dead Code & Junk Instructions:** Many functions (e.g., `mjY23dxWU`, `XGdjhfIKe`) consist of repetitive mathematical operations on registers that are recalculated but never meaningfully used in a way that impacts the program's output. This is designed to "flood" the analyst with noise and make it difficult to identify the core logic.
*   **Anti-Decompiler Logic:** The recurring **"WARNING: Bad instruction - Truncating control flow here"** messages are intentional. By using overlapping instructions or data-as-code, the author forces decompilers like Ghidra to "give up" on accurately reconstructing the logic flow.
*   **Control Flow Flattening/Obfuscation:** The complex `while(true)` loops and nested conditional jumps (like those in the first large block) are typical of **control-flow flattening**, which replaces a simple linear logical path with a massive, complicated loop structure to hide the true order of operations.
*   **Anti-Analysis Loops:** The function `method.Taskmgr.RegisterScreen.SDZMMs2gj` contains an explicit **"Do nothing block with infinite loop."** This is a common tactic used to:
    1.  Stall automated sandboxes by keeping the process "busy" in a harmless loop.
    2.  Confuse debuggers that may struggle to step through or interpret the intent of an empty, infinite cycle.

#### 3. Specific Technical Observations from Chunk 2
*   **Complex Memory Arithmetic:** You can see frequent use of `CONCAT` and bit-shifting (e.g., `pcVar16 = CONCAT31(uVar22,CONCAT11(uVar27,uVar23))`). These are not standard ways to write code; they are artifacts of a **mutation engine** that replaces simple additions/moves with complex bitwise equivalent operations.
*   **Symbolic Obfuscation:** The names like `method.Taskmgr.yarak.klass..cctor` suggest a structure where the malware's real "identity" is hidden behind fake classes and methods, making it difficult to determine what functionality (e.g., networking, file deletion) is actually being performed until the code is unpacked in memory.

### Summary of Findings
| Feature | Analysis Result | Significance |
| :--- | :--- | :--- |
| **Core Type** | **Polymorphic/Metamorphic Loader** | Designed to hide a secondary payload from static scanners. |
| **Obfuscation Engine** | Likely **Dotfuscix or ConfuserEx** | High-level .NET obfuscation is present. |
| **Anti-Analysis** | **High** | Uses junk code, "bad" instructions, and stall loops to defeat debuggers/decompilers. |
| **Payload Transition** | **Detected** | Indirect jumps are used to transition from the loader stub to the active malware. |

### Recommendation for Further Analysis
The static analysis of this binary is reaching a point of diminishing returns because of the heavy obfuscation; it is designed to be "unreadable" in its current form. To progress, I recommend:
1.  **Dynamic Analysis:** Run the sample in a controlled, isolated sandbox.
2.  **Memory Dumping:** Use a tool like Scylla or x64dbg to set a breakpoint at the indirect jump (`(**(pcVar5 | 0xffff8a38))()`). When hit, dump the memory region of the process. This will capture the **de-obfuscated payload**, which will be much easier to analyze.
3.  **Behavioral Monitoring:** Monitor for network connections and file system changes while it runs to see what the "hidden" payload actually does once it is unpacked.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1055 | Packing | The binary functions as a "stub" or packer designed to hide a multi-stage payload and transition execution to an unpacked state in memory. |
| T1027 | Obfuscated Files or Information | Techniques such as dead code, junk instructions, control flow flattening, and mutation are used to frustrate both manual analysis and automated tools. |
| T1497 | Virtualization/Sandbox Evasion | The use of "do nothing" loops is specifically designed to stall automated sandboxes and complicate the work of a debugger. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contains a high volume of obfuscated data and standard .NET library artifacts; these have been filtered out to provide only genuine indicators.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Obfuscation Tools:** Evidence of **Dotfuscix** or **ConfuserEx** (identified via .NET metadata and complex method naming conventions like `method.ESGx3sAliJMObInEwI.WWXkeHwZNbkN2vcreE..cctor`).
*   **Anti-Analysis Logic:** 
    *   **Infinite Loop Stall:** The specific routine `method.Taskmgr.RegisterScreen.SDZMMs2gj` is identified as a "Do nothing" block used to stall automated sandboxes.
    *   **Control Flow Flattening:** Extensive use of junk code and non-standard math (e.g., `CONCAT31`, `CONCAT11`) suggests a highly sophisticated mutation engine.
*   **Malicious Behavior Indicators:** 
    *   **Indirect Jump Point:** A transition to the payload is identified at the end of function/method `qdAX14ofO`. 
    *   **Decompiler Evasion:** Presence of "Warning: Bad instruction" logic intended to break Ghidra/IDA Pro control flow reconstruction.

---

## Malware Family Classification

1. **Malware family**: Unknown (Loader Stub)
2. **Malware type**: Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Obfuscation:** The binary utilizes advanced .NET obfuscation techniques (likely Dotfuscix or ConfuserEx), including control-flow flattening, junk code insertion, and "bad instruction" logic to hinder decompiler analysis.
*   **Anti-Analysis/Sandbox Evasion:** The presence of specific "do nothing" loops is a clear indicator of an attempt to stall automated sandboxes and complicate manual debugging.
*   **Multi-stage Execution:** The identification of an indirect jump point (`qdAX14ofO`) confirms the binary's role as a stub/loader designed to decrypt and hand off execution to a primary payload currently residing in memory.
