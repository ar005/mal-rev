# Threat Analysis Report

**Generated:** 2026-07-26 05:41 UTC
**Sample:** `0b5c1b777491d7f267bdb5b1eb6e687323799f85ea5eac44f3db11a84c7f505c_0b5c1b777491d7f267bdb5b1eb6e687323799f85ea5eac44f3db11a84c7f505c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b5c1b777491d7f267bdb5b1eb6e687323799f85ea5eac44f3db11a84c7f505c_0b5c1b777491d7f267bdb5b1eb6e687323799f85ea5eac44f3db11a84c7f505c.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 974,848 bytes |
| MD5 | `ee78fede5ea55dcce49fefb3c7e13537` |
| SHA1 | `82dc07b2094d8aa1b9a51cf5ccc673c106081904` |
| SHA256 | `0b5c1b777491d7f267bdb5b1eb6e687323799f85ea5eac44f3db11a84c7f505c` |
| Overall entropy | 7.256 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3929709917 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 970,752 | 7.264 | ⚠️ Yes |
| `.rsrc` | 3,072 | 4.59 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **6996** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

k[&	o>

,I	o|

-J+Z 
 KDBM(

-rT5

,.r_H

+Fr}H
p+r)N

	_,d
0A[i+	

+2	o

+*	od

+*	od
&&*.sE

#333333

,	(T

,S	(s

,F	oI
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADP
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADP
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADP
tWwUWWWWW
s)ycgF
w9=	@9
EdRCD%
Dla{WI*s^3
<|1k1~
(,1L#
A(K%	H
qzd?L3o
Jk*q4^
e.rwV_
B{mrg)z@
}!fj}?
4YhguN
*D6FZ[
C28sZaoJ
/yX9&0
hN3
f%n
Qrm|wV
>,,>$<
$XZJ0~
]M9A(y
p/EJZg
km}HV&
vJyCY_
.7UW:5h
J/]@9U
>Nx4y5
B+!cm;!
X!%	3?r
-DxP'b2
DJKTKJ
xIH5LJ
$mS4_T4_R4_V4_
xsDi0%
b8_u	o
8MKbKV
yu:EF!
!hd-v\
$5AEW
VzBV@iJX
8~+8U
7"
T$	
3`cy$t
<a%C\I
xOwOwO
fz@3_r
uR_^'

;o=\)=o
pyJd^N
Mx	Sdx@
QOZ"UjkFoK
QM]trYi
G00AH

AW!/q\ddB
DLvw! |
9U=&XU
JYN:
3'[hQd
w?JF8FH
E @G3]
L
W+th
;o!hCj 
!IYx6D
39LZ sc
`EZiAu
4[;NM
U_ywJT^
mhg%R	
@d!e[
s>l,W
SISF~7L
	3aFF=m
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **2**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.Costura.AssemblyLoader.LoadStream` | `0x42b300` | 822528 | ✓ |
| `sym.__c..cctor_15` | `0x428647` | 790538 | ✓ |
| `method.Costura.AssemblyLoader.Attach` | `0x42b614` | 64748 | — |
| `method.DarkModeForms.DarkModeCS.ThemeControl` | `0x402d90` | 3456 | — |
| `method.vgrggolkjgzainxyznvegiro.CUXnUOBJ8TqRd6lkLiGFnHU3GwKj..ctor` | `0x41ac48` | 2606 | — |
| `method.iqibuibqvbggzv.uTFs8puBmOmExdhw4FnsQFlstEoMt.lZIcAz9HxbqW18tSB7RGyAVvC` | `0x42a923` | 2262 | — |
| `method.yqhsbznvrofccsqmfm.7ys9j7qVluORD1TZebsa9YN.48OYiuG1RufWuDMq6nLK` | `0x40d1f0` | 2076 | — |
| `method.zikhqnojrzu.ivVbrOCQdtgFH2vyVAw6jz56CMW.gjCZx5QciLvfcqSs0YYe17SJUPblS` | `0x4062e3` | 1953 | — |
| `method._ExecuteAsync_d__26.MoveNext` | `0x41365c` | 1944 | — |
| `method.rsfsinkufgcrpqlkc.lea7pfHY9HzYMKW1JApNUMQTviGXw.OnLoad` | `0x405b57` | 1932 | — |
| `method.fqgxzlahcoxicuxzlpurk.xanm02xsrm.uV5RreBRx1TAdW6xMn` | `0x4295f4` | 1724 | — |
| `method.yqhsbznvrofccsqmfm.7ys9j7qVluORD1TZebsa9YN.2LGM6pKjzR0CP` | `0x40db44` | 1695 | — |
| `method.qkmgfpvrysacnq.uyn96jOjk6q0iqKjwtaE4m80.uDDivsXrClfJcTJhEZaJIo` | `0x42a0cb` | 1512 | — |
| `method.zikhqnojrzu.aQNaQxxt6b1.PYcHo3T0ix5uBKktBS` | `0x408228` | 1472 | — |
| `method.infoddvcev.BN3sKegLTXqYrK3I.SIZi6rsrjnm5Pzbx61` | `0x41779c` | 1228 | — |
| `method._StartBrowserAsync_d__21.MoveNext` | `0x423acc` | 1208 | — |
| `method._StartFirefoxAsync_d__14.MoveNext` | `0x42449c` | 1200 | — |
| `method._StartGenericChromiumAsync_d__28.MoveNext` | `0x42495c` | 1188 | — |
| `method.zikhqnojrzu.aQNaQxxt6b1.lWDjfiJRKWivCdP` | `0x40748c` | 1116 | — |
| `method.zikhqnojrzu.aQNaQxxt6b1.MtRDJW3AFur8UYh` | `0x407bf4` | 1068 | — |
| `method.dqvtgxdyowfzqsfednhles.LFMPYb5WabqHMFRd47Do.PvMy0MIk4S7M7XEP3LZDWwykg` | `0x425d00` | 1048 | — |
| `method.wotqrbevjcyhp.YxvUmn7ogmzaV4tEm.0fjIIylthPsjOXcKLF0HfgO4l5` | `0x420494` | 996 | — |
| `method.infoddvcev.fZy6BFQy0xCrd8nt1ARHV.tSix8omVvodUBIJzUpZjj` | `0x4158a4` | 992 | — |
| `method._CloneBrowserProfileAsync_d__25.MoveNext` | `0x4234bc` | 940 | — |
| `method.jclrgphyyfgapelhbhbegaflvzsll.SGXUEp7SfumXVwiiRU3LbW8q.h5T16ya4HlENTq8nV37Y6C30Zd7` | `0x4279f8` | 912 | — |
| `method.infoddvcev.m9omYlgO72F.GsdtZMTJ7azFDAuGzvaaqXsxktR` | `0x4106a4` | 868 | — |
| `method.wotqrbevjcyhp.e1LonzkIAs1jBGKKD8kQb4Of.KyiXoKxkTn2bzynP4` | `0x421ad4` | 856 | — |
| `method.jclrgphyyfgapelhbhbegaflvzsll.SGXUEp7SfumXVwiiRU3LbW8q.7fCccd0osm3Wwsb2ps4Eio5EMC` | `0x427f40` | 828 | — |
| `method.nxmlnokqmkb.WIoRwKYIKOoOhJ2.5hGgomRo2DOV77YIwVcmunzJlHCqc` | `0x40e308` | 800 | — |
| `method.zikhqnojrzu.aQNaQxxt6b1.evgZpB6q0YEmUDi3` | `0x4078e8` | 780 | — |

### Decompiled Code Files

- [`code/sym.Costura.AssemblyLoader.LoadStream.c`](code/sym.Costura.AssemblyLoader.LoadStream.c)
- [`code/sym.__c..cctor_15.c`](code/sym.__c..cctor_15.c)

## Behavioral Analysis

Based on the provided disassembly and metadata, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The code belongs to a **.NET application** that has been bundled using the **Costura.Fodery** tool. 
*   **Assembly Loading:** The function `sym.Costura.AssemblyLoader.LoadStream` is part of a mechanism designed to load, extract, and execute additional .NET DLLs (assemblies) that are embedded inside the main executable file rather than being stored as separate files on disk.
*   **Payload Delivery:** This technique is commonly used by developers to simplify distribution, but in a malware context, it is frequently used to "hide" the primary malicious components of the code from basic static analysis.

### Suspicious and Malicious Behaviors
While the assembly loader itself is a legitimate library function, its presence and the way the surrounding code is structured indicate several suspicious behaviors:

*   **Obfuscation/Anti-Analysis:** The decompiler produced numerous warnings (e.g., `Control flow encountered bad instruction data`, `overlapping instruction`, `Removing unreachable block`). This is a strong indicator of **heavy obfuscation**. Malware authors use these techniques to break automated analysis tools, confuse human researchers, and hide the true logic of the program.
*   **Hidden Logic:** By using Costura, the "true" malicious logic (e.g., stealing credentials, keylogging, or communicating with a C2 server) is likely contained within one of the internal assemblies being loaded by this function rather than in the main executable's visible code.
*   **Junk Code Injection:** The complex arithmetic, `CONCAT` operations, and large hex offsets (e.g., `0x72c0a00`, `0x2cf8ec04`) within the decompiled C code are typical of "junk code" or "dead code" insertion designed to make it difficult for an analyst to determine the actual flow of execution.

### Notable Techniques & Patterns
*   **Packer/Loader Pattern:** The combination of a .NET runtime, Costura-style embedding, and broken disassembly is a hallmark of sophisticated malware (such as info-stealers or loaders). 
*   **Code Complexity:** The extremely high number of "unreachable blocks" suggests the use of a **control-flow obfuscator**. These tools create a "spaghetti" of jumps and branches that make manual reverse engineering significantly more time-consuming.
*   **Signature Overlap:** The strings provided show standard .NET libraries (`System.Resources`), but notice the large block of non-human-readable characters. This suggests either encrypted data or an obfuscated resource section containing the internal DLLs mentioned above.

### Summary for Incident Response
The binary is likely a **loader**. It uses legitimate bundling tools (Costura) to hide its secondary modules and employs significant obfuscation to hinder analysis. 
*   **Risk Level:** High/Suspicious.
*   **Recommendation:** The sample should be executed in a controlled, isolated sandbox. Monitoring should focus on the memory space of the process after it initializes; the "real" malicious behavior will likely manifest only after `LoadStream` has successfully decrypted and loaded the embedded payloads into memory.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of junk code, complex arithmetic, and "spaghetti" control-flow logic is designed to hinder manual reverse engineering and defeat automated analysis tools. |
| **T1548** | Abuseers of System Tools | The utilization of a legitimate library (Costura) to bundle and hide malicious components within a single executable allows the malware to evade basic static detection. |
| **T1637** | Reflective Code Loading | The identification of the binary as a "loader" that extracts and executes internal assemblies into memory suggests it is designed to execute payload code without standard file-on-disk artifacts. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The analysis indicates that this binary is a heavily obfuscated loader; therefore, many traditional network indicators (IPs/URLs) are likely hidden within encrypted payloads not visible in the raw string dump.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The analysis notes that the "true" logic is hidden within embedded assemblies, meaning file paths are likely generated dynamically or exist only in memory.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Loader Framework:** `Costura.Fodery` (Used to bundle and hide secondary malicious DLLs).
*   **Assembly Loading Method:** `sym.Costura.AssemblyLoader.LoadStream` (Identified as the primary mechanism for injecting payload into memory).
*   **Obfuscation Techniques:** 
    *   Control-flow obfuscation (High volume of "unreachable blocks").
    *   Junk code injection (Complex arithmetic and `CONCAT` operations used to confuse analysis).
    *   Encrypted resource sections (Identified by large blocks of non-human-readable characters in the string dump).
*   **Internal Metadata:** `.NET Framework 4.0.0.0` references (Standard library, but confirms the environment for the loader).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
* **Execution of Hidden Payloads:** The use of `Costura.Fodery` and the `LoadStream` method confirms the primary function is to bundle and execute secondary, hidden .NET assemblies within the same process memory.
* **Advanced Obfuscation Techniques:** The presence of extensive junk code, "spaghetti" control flow (unreachable blocks), and non-human-readable character strings indicates a deliberate attempt to mask malicious intent from both automated systems and human analysts.
* **Reflective Loading Capabilities:** By utilizing techniques mapped to MITRE T1637, the sample is designed to operate without leaving traditional artifacts on disk, which is a hallmark of sophisticated first-stage loaders used to deliver high-impact payloads like info-stealers or ransomware.
