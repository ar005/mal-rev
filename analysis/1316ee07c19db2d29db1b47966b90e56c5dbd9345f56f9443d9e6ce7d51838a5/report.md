# Threat Analysis Report

**Generated:** 2026-09-02 09:00 UTC
**Sample:** `1316ee07c19db2d29db1b47966b90e56c5dbd9345f56f9443d9e6ce7d51838a5_1316ee07c19db2d29db1b47966b90e56c5dbd9345f56f9443d9e6ce7d51838a5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1316ee07c19db2d29db1b47966b90e56c5dbd9345f56f9443d9e6ce7d51838a5_1316ee07c19db2d29db1b47966b90e56c5dbd9345f56f9443d9e6ce7d51838a5.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 10 sections |
| Size | 7,887,408 bytes |
| MD5 | `0c153d2ef4cb0565df75b0dc649dcbfb` |
| SHA1 | `718d2f8c625d248ee8aee5682f7a1dcda4c1fc86` |
| SHA256 | `1316ee07c19db2d29db1b47966b90e56c5dbd9345f56f9443d9e6ce7d51838a5` |
| Overall entropy | 7.985 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 583443149 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 0 | 0.0 | No |
| `.rdata` | 0 | 0.0 | No |
| `.data` | 0 | 0.0 | No |
| `.pdata` | 0 | 0.0 | No |
| `_RDATA` | 0 | 0.0 | No |
| `.hg@` | 0 | 0.0 | No |
| `.wMu` | 12,800 | 0.05 | No |
| `.CoN` | 7,793,152 | 7.991 | ⚠️ Yes |
| `.reloc` | 5,632 | 5.465 | No |
| `.rsrc` | 63,488 | 6.842 | No |

### Imports

**KERNEL32.dll**: `HeapAlloc`, `HeapFree`, `ExitProcess`, `LoadLibraryA`, `GetModuleHandleA`, `GetProcAddress`
**USER32.dll**: `PostMessageA`
**ADVAPI32.dll**: `RegCloseKey`
**SHELL32.dll**: `SHGetFolderPathA`
**SHLWAPI.dll**: `PathCombineW`
**WTSAPI32.dll**: `WTSQuerySessionInformationA`
**WININET.dll**: `InternetOpenA`

## Extracted Strings

Total strings found: **16364** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@_RDATA
h.reloc
@.rsrc
sb;El'
Wb:VPT
%<=Nql
f.dBX}
5Nv'Pr
<-P%2&
PnR"MJ
zC7~g
p\`Gca
mdJ>A
Ak&UQ_
tt%%]'
"m?XI)
<ma2&85W{!I
'@yeHJ
,NmyeHJzW
*vxeHJ
CUqi,k
o+[I8[
OC#O%'
fE"\=!]QI.4&
rGRF}o
8h
ET.
6WXO1`
W2eSi
	tx?Ik
Q~fLL9
b:Sc&8)
|EgT&K
V_{4?7
$4QZ9
AGb:*9W
94v{55d
?/T		n
/w5<:@
-90T!2
m+.gKQ
	Qq
h	_vFdE-3
(	cU:2T
!cubN8
J?fQ:&
(Tw&4d
(Tw&9	
5TYe"
AuUYeLQ
sC)r[Fp
sC)r[F9|
(r[F4)

WCPDXb
Q+?,8~
(r[F^C
Q)r[F+
(r[FZ+
(r[F|a
\]wcpd
$Wmyjo
n])r[F
aeWIIH
GiI.rE
%"'fD
WTSQuerySessionInformationA
9@<tTF
;brO:<^
E1bt:H`8
m&_1rm
Fc
_3P{s;m
E~sWB]2
zIoC]2
Bs8C]2
f <YW
s8]gj[
+?c]@yP
,z{Nbx
yQefyU0
L:P/-G
@a\/=r
IS^"Vy
=5	0usf
I_{xv')@e)K&
k.(`I9
vDRTF-
Yb:LJ
8Zt89
8wb!|*
@E@zor
)&7/.`/:
6T2u-)g
#_V|
0
NW]X^h'n
,kb&bY
-
ZG%0
,"=rk
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `int.1406be73b` | `0x1406be73b` | 7012611 | ✓ |
| `fcn.1406ab1c0` | `0x1406ab1c0` | 5126847 | ✓ |
| `fcn.140b148f8` | `0x140b148f8` | 4602072 | ✓ |
| `fcn.140dca16c` | `0x140dca16c` | 3209664 | ✓ |
| `fcn.140dbf9af` | `0x140dbf9af` | 3186928 | ✓ |
| `fcn.140da0cb1` | `0x140da0cb1` | 3179521 | ✓ |
| `fcn.140dbbdf7` | `0x140dbbdf7` | 3039836 | ✓ |
| `fcn.140dd5ac5` | `0x140dd5ac5` | 2933674 | ✓ |
| `fcn.140dbbbff` | `0x140dbbbff` | 2928995 | ✓ |
| `fcn.140dbc7ac` | `0x140dbc7ac` | 2901666 | ✓ |
| `fcn.140ddae6a` | `0x140ddae6a` | 2897794 | ✓ |
| `fcn.140af33ea` | `0x140af33ea` | 2790417 | ✓ |
| `fcn.140db92b1` | `0x140db92b1` | 2707344 | ✓ |
| `fcn.140dbbf09` | `0x140dbbf09` | 2659911 | ✓ |
| `fcn.140dd04cc` | `0x140dd04cc` | 2592922 | ✓ |
| `fcn.140daf16e` | `0x140daf16e` | 2549390 | ✓ |
| `fcn.140dbb9cf` | `0x140dbb9cf` | 2481827 | ✓ |
| `fcn.140da2be0` | `0x140da2be0` | 2296566 | ✓ |
| `fcn.140d9dee6` | `0x140d9dee6` | 2224288 | ✓ |
| `fcn.140b987ca` | `0x140b987ca` | 2014591 | ✓ |
| `fcn.140af3c39` | `0x140af3c39` | 612129 | ✓ |
| `fcn.140b247e6` | `0x140b247e6` | 495488 | ✓ |
| `fcn.140dde42a` | `0x140dde42a` | 394100 | ✓ |
| `fcn.140dd347d` | `0x140dd347d` | 325520 | ✓ |
| `fcn.140db2678` | `0x140db2678` | 278291 | ✓ |
| `fcn.140dc4eca` | `0x140dc4eca` | 278087 | ✓ |
| `fcn.140dbb4d1` | `0x140dbb4d1` | 277139 | ✓ |
| `fcn.140dd0616` | `0x140dd0616` | 276653 | ✓ |
| `fcn.140de0981` | `0x140de0981` | 276122 | ✓ |
| `fcn.140da28ee` | `0x140da28ee` | 275647 | ✓ |

### Decompiled Code Files

- [`code/fcn.1406ab1c0.c`](code/fcn.1406ab1c0.c)
- [`code/fcn.140af33ea.c`](code/fcn.140af33ea.c)
- [`code/fcn.140af3c39.c`](code/fcn.140af3c39.c)
- [`code/fcn.140b148f8.c`](code/fcn.140b148f8.c)
- [`code/fcn.140b247e6.c`](code/fcn.140b247e6.c)
- [`code/fcn.140b987ca.c`](code/fcn.140b987ca.c)
- [`code/fcn.140d9dee6.c`](code/fcn.140d9dee6.c)
- [`code/fcn.140da0cb1.c`](code/fcn.140da0cb1.c)
- [`code/fcn.140da28ee.c`](code/fcn.140da28ee.c)
- [`code/fcn.140da2be0.c`](code/fcn.140da2be0.c)
- [`code/fcn.140daf16e.c`](code/fcn.140daf16e.c)
- [`code/fcn.140db2678.c`](code/fcn.140db2678.c)
- [`code/fcn.140db92b1.c`](code/fcn.140db92b1.c)
- [`code/fcn.140dbb4d1.c`](code/fcn.140dbb4d1.c)
- [`code/fcn.140dbb9cf.c`](code/fcn.140dbb9cf.c)
- [`code/fcn.140dbbbff.c`](code/fcn.140dbbbff.c)
- [`code/fcn.140dbbdf7.c`](code/fcn.140dbbdf7.c)
- [`code/fcn.140dbbf09.c`](code/fcn.140dbbf09.c)
- [`code/fcn.140dbc7ac.c`](code/fcn.140dbc7ac.c)
- [`code/fcn.140dbf9af.c`](code/fcn.140dbf9af.c)
- [`code/fcn.140dc4eca.c`](code/fcn.140dc4eca.c)
- [`code/fcn.140dca16c.c`](code/fcn.140dca16c.c)
- [`code/fcn.140dd04cc.c`](code/fcn.140dd04cc.c)
- [`code/fcn.140dd0616.c`](code/fcn.140dd0616.c)
- [`code/fcn.140dd347d.c`](code/fcn.140dd347d.c)
- [`code/fcn.140dd5ac5.c`](code/fcn.140dd5ac5.c)
- [`code/fcn.140ddae6a.c`](code/fcn.140ddae6a.c)
- [`code/fcn.140dde42a.c`](code/fcn.140dde42a.c)
- [`code/fcn.140de0981.c`](code/fcn.140de0981.c)
- [`code/int.1406be73b.c`](code/int.1406be73b.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, here is the updated and expanded analysis of the binary.

### Updated Analysis Report

#### Core Functionality and Purpose
The binary remains confirmed as a **highly sophisticated packer or protector**, likely utilizing a custom Virtual Machine (VM) architecture or a complex state-machine dispatcher. The second set of disassembly confirms that the code does not execute standard logic linearly; instead, it spends significant resources on "preparing" execution paths, decrypting internal constants, and navigating a heavily obfuscated control flow graph.

#### Suspicious and Malicious Behaviors
*   **Anti-Analysis Techniques (Expanded):**
    *   **Time-Based Detection:** The use of `rdtsc` is confirmed in the logic flow. Notably, the result of the `rdtsc` call is processed through a bit-shifting/folding operation (`param_2 = CONCAT44(uVar4 >> 0x20, uVar13)`). This suggests the malware isn't just checking if a timer "jumps" (indicating a debugger), but is potentially using the timestamp as a seed or key for subsequent decryption steps.
    *   **Direct System Calls & Obfuscation:** The reliance on manual address calculations and indirect jumps (e.g., `UNRECOVERED_JUMPTABLE`) indicates an attempt to hide the actual API calls from static analysis tools by resolving them at runtime only when specific conditions are met.
*   **Information Gathering / Environment Checks:**
    *   The complexity of the state-packing logic (the large block of bitwise `OR` and `AND` operations) suggests it is evaluating multiple environment variables (potential flags for debugger presence, admin privileges, or specific system artifacts) to decide which "branch" of the packer to execute.

#### Notable Techniques and Patterns
*   **Control Flow Flattening (CFF) & State Machine Dispatcher:**
    The code at `code_r0x000140da5552` reveals a sophisticated **State Machine**. The calculation involving `(in_NT & 1) * 0x4000 | ...` is a technique where multiple Boolean conditions are packed into a single integer. This resulting value then dictates the next "jump" in the flow. To a decompiler, this looks like a mess of math; to the CPU, it is selecting the next instruction's location based on environmental checks.
*   **Virtual Machine (VM) Execution:**
    The pattern of updating `puVar31` with specific offsets followed by function calls and indirect jumps strongly suggests a **VM-dispatcher**. The binary is likely interpreting a custom bytecode. The "hidden" logic is not in the standard x86 instructions we see, but in the way the dispatcher interprets those values.
*   **Multi-Stage Decryption Loops:**
    The `do { ... } while(true)` loop at the end of the segment (around `code_r0x000140dde8a7`) is a classic **decryption/deobfuscation loop**. It processes data using fixed constants (like `0x259e379c`). This indicates that a "Stage 2" payload is being decrypted in memory just before it is executed.
*   **Opaque Predicates & Junk Code:**
    The logic involving `uVar33 = (~(((*puVar27 ^ uVar3) + 1 ^ 0x6337) + 1) ^ 0xb90a) + 0x6c19` is a classic **Opaque Predicate**. The math is unnecessarily complex to calculate a value that ultimately leads to a known path, but it serves to break the "decompiler's" ability to create a clean flow graph.

---

### Updated Summary for Incident Response
The binary is a professional-grade **multi-stage packer/loader** designed to shield a high-value payload (e.g., a RAT, ransomware, or info-stealer). It utilizes "VM-style" protection where the primary malicious logic is hidden behind a custom instruction set and a state-machine dispatcher.

**New Technical Observations for Forensics:**
1.  **Memory Residency:** The binary likely decrypts its secondary stage entirely in memory (Fileless behavior) after passing through several layers of mathematical de-obfuscation.
2.  **Timing Sensitivity:** Because `rdtsc` is integrated into the decryption logic, standard "slow" debuggers or step-through debugging will likely cause the payload to fail to decrypt correctly, as the calculated key would be incorrect.
3.  **Anti-Analysis Sophistication:** The use of packed state machines means that simply looking at the code won't reveal the "intent." Analysis should focus on **memory dumping** at the point where the final loop finishes its execution.

**Updated Indicators of Compromise (IoCs):**
*   **Behavioral:** High-frequency calculation of bitwise masks to determine jump targets; use of `rdtsc` as a functional component of a decryption algorithm.
*   **Static:** Presence of "junk" math blocks that result in no net change to variables but significantly complicate the disassembly.
*   **Dynamic:** Look for evidence of **in-memory decryption loops** and jumps into newly allocated/modified memory regions (RWX segments).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Software Packing | The use of a custom VM architecture, Control Flow Flattening (CFF), and Opaque Predicates are primary methods to obfuscate the code's logic from static analysis. |
| **T1497** | Virtualization/Sandbox Evasion | The integration of `rdtsc` into the decryption logic indicates an attempt to detect timing inconsistencies common in debuggers or virtualized environments. |
| **T1055** | Process Injection | The "memory-resident" behavior and multi-stage execution suggest that payloads are decrypted and executed directly in memory to avoid detection by file-based scanners. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The "Strings" section contains heavily obfuscated data and standard system library references; no actionable infrastructure-based IOCs (like specific C2 domains or IPs) were found within that specific block.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: Memory offsets such as `r0x000140da5552` are internal to the binary's execution and do not constitute file system or registry IOCs).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified. (Note: Hexadecimal values such as `0x259e379c` are used in internal decryption logic rather than representing standard MD5/SHA hashes).

### **Other artifacts**
*   **Anti-Analysis Techniques:** 
    *   Use of `rdtsc` instruction for timing checks and as a seed/key for decryption routines.
    *   Presence of "Opaque Predicates" (complex math logic intended to confuse decompilers).
*   **Evasion Tactics:**
    *   Control Flow Flattening (CFF) implemented via state-machine dispatchers.
    *   In-memory decryption loops (likely indicating a multi-stage "fileless" loader behavior).
*   **Known Internal Logic:** 
    *   Bitwise mask calculations for jump target determination.
    *   Use of `WTSQuerySessionInformationA` (typically used to determine if the session is interactive, often a precursor to environmental checks).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
*   **Sophisticated Obfuscation & Virtualization:** The binary utilizes a custom Virtual Machine (VM) architecture and a state-machine dispatcher to hide its true logic from static analysis, a hallmark of professional-grade loaders used to protect high-value payloads.
*   **Multi-Stage In-Memory Execution:** The presence of multi-stage decryption loops and the "fileless" behavior (decrypting secondary stages directly into memory) indicates its primary purpose is to unpack and inject a hidden payload (such as a RAT or info-stealer).
*   **Advanced Anti-Analysis Suite:** The use of `rdtsc` for both timing checks and decryption seeds, combined with Control Flow Flattening (CFF) and Opaque Predicates, demonstrates a high level of sophistication intended to bypass automated sandboxes and manual reverse engineering.
