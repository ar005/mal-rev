# Threat Analysis Report

**Generated:** 2026-07-30 11:14 UTC
**Sample:** `0c6f4a6a439dd4573ebcd755099b2466ddc531fe8bb0912f09afb66d10664ac7_0c6f4a6a439dd4573ebcd755099b2466ddc531fe8bb0912f09afb66d10664ac7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c6f4a6a439dd4573ebcd755099b2466ddc531fe8bb0912f09afb66d10664ac7_0c6f4a6a439dd4573ebcd755099b2466ddc531fe8bb0912f09afb66d10664ac7.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 9 sections |
| Size | 12,896,768 bytes |
| MD5 | `16230f3d314c0665fa585793677f2a52` |
| SHA1 | `f5bc9070f981b0b1623dfbf8998f6849b41c1181` |
| SHA256 | `0c6f4a6a439dd4573ebcd755099b2466ddc531fe8bb0912f09afb66d10664ac7` |
| Overall entropy | 7.822 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767779732 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 0 | 0.0 | No |
| `.data` | 0 | 0.0 | No |
| `.rdata` | 0 | 0.0 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 0 | 0.0 | No |
| `.fMN` | 0 | 0.0 | No |
| `.+)p` | 512 | 0.244 | No |
| `."^O` | 12,769,280 | 7.82 | ⚠️ Yes |
| `.rsrc` | 125,952 | 7.965 | ⚠️ Yes |

### Imports

**ADVAPI32.dll**: `CloseServiceHandle`
**KERNEL32.dll**: `CheckRemoteDebuggerPresent`
**USER32.dll**: `GetSystemMetrics`

## Extracted Strings

Total strings found: **19633** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
.idata
h.rsrc
O^$lO
D$4;D1T$8H
hVdOla
rS34&n
lJe"F>J
cD0tV-
[iz@82
xiW+{).
*"hW+L
;n=hW+L
AX$R'y
sy\~id	
!p{]#`
QAYAYAZZZZAY
}+JbF%W
#\-~3c
(!*J+$
h{,D\0H,g
 &$'z/+
[_EAc,
`K@o[G
 (T$
A
LLhSfF
>fvO2>
~{Wmsa
}k
~WK
YAZY^X
o[=F59
_10ivb
[c\z/0
0D1L$
AQf-	
#
m^^ZAYX

=4w@z
 
_	$`
Y>Tq{[!>Tq
@NH&9L>
4m4T	m
1Gn4FK
YYXAZ]Z
![	;8[~
u:E=8L
sv%9*i
2,GfA
5	r"Yh2H
jfI?}5
^rjvG[
^%;kU3
xQ`>HA
A[]Z_A
AZAZAZ[
'Rj)|L
#3CC:T
5g;9t1
ASF1L\
_ zb5
%
vaQO	?T
WT(2Td
!ry43[
L0\!ry4
\a=ZD:9
YAYZA[ZY
^Z^YXH
0fB)D	H
e8
<J.P	
4"Y@gWB
RcW3)Yh
5Mr-Yz
o"^w$D8
oyF0Gm
f@b7/Z
+c2xT,
ic2x^z
Ax{! =#|${:2
skDSR
"lQB_k
jb# tb
qmn6hk
F4+%~%4|
HMmN<|
%eR,,6$
h"/)Z-

e-%V+
_RhB,QH
750za. 
}O\mKE
P]2'Qo
9]zGx61]zG
n	]zG0	
ZAZZAZ
Yy`Ui~
t}$&DzS
c:Hkw8
+vg2w	
+ !K>6
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **1**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00b13ece` | `0xb13ece` | 12696991 | — |
| `fcn.00b13116` | `0xb13116` | 12650553 | — |
| `fcn.012a5517` | `0x12a5517` | 12646884 | — |
| `fcn.01507082` | `0x1507082` | 12625055 | — |
| `fcn.016b3e97` | `0x16b3e97` | 12601328 | — |
| `fcn.016c03ac` | `0x16c03ac` | 12595771 | — |
| `fcn.01705768` | `0x1705768` | 12591719 | — |
| `fcn.011766b0` | `0x11766b0` | 12589023 | — |
| `fcn.01718207` | `0x1718207` | 12584748 | — |
| `fcn.00b122ca` | `0xb122ca` | 12573056 | ✓ |
| `fcn.0167462c` | `0x167462c` | 12571795 | — |
| `fcn.00b19c32` | `0xb19c32` | 12569469 | — |
| `fcn.01395ce9` | `0x1395ce9` | 12559948 | — |
| `fcn.0171ca4f` | `0x171ca4f` | 12558450 | — |
| `fcn.01704f21` | `0x1704f21` | 12554924 | — |
| `fcn.0170ab13` | `0x170ab13` | 12551341 | — |
| `fcn.011e5282` | `0x11e5282` | 12550451 | — |
| `fcn.01714702` | `0x1714702` | 12548041 | — |
| `fcn.0165229f` | `0x165229f` | 12541497 | — |
| `fcn.01714bbe` | `0x1714bbe` | 12536153 | — |
| `fcn.017118e6` | `0x17118e6` | 12531762 | — |
| `fcn.014dba73` | `0x14dba73` | 12531378 | — |
| `fcn.012fe5d8` | `0x12fe5d8` | 12529665 | — |
| `fcn.015219f9` | `0x15219f9` | 12529108 | — |
| `fcn.0110a225` | `0x110a225` | 12525645 | — |
| `fcn.01706212` | `0x1706212` | 12521825 | — |
| `fcn.01548ed6` | `0x1548ed6` | 12517505 | — |
| `fcn.010d5632` | `0x10d5632` | 12511760 | — |
| `fcn.00b2eef7` | `0xb2eef7` | 12508486 | — |
| `fcn.01175ba4` | `0x1175ba4` | 12498381 | — |

### Decompiled Code Files

- [`code/fcn.00b122ca.c`](code/fcn.00b122ca.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C code, here is an analysis of the sample:

### Core Functionality and Purpose
The primary purpose of this specific function (`fcn.00b122ca`) is **code obfuscation and control-flow flattening**. 

The code does not perform high-level logic (like file I/O or network requests) in a readable way. Instead, it serves as a "dispatcher" or a heavily mangled internal routine. It uses complex mathematical transformations to determine the next block of code to execute. This is common in malware that utilizes commercial packers or custom protectors to hide its true intent from static analysis tools.

### Suspicious and Malicious Behaviors
*   **Control-Flow Flattening (CFF):** The presence of `UNRECOVERED_JUMPTABLE` and the complex calculations used to determine offsets (e.g., `uVar13 = uVar13 >> uVar18 | uVar13 << 0x40 - uVar18`) indicate that the original logic has been "flattened." Instead of a standard `if/else` or `switch` structure, every block of code returns to a central dispatcher which calculates the next destination using an obfuscated index.
*   **Anti-Analysis via Complexity:** The use of **Mixed Boolean-Arithmetic (MBA)** is evident in the calculations for variables like `iVar27` and `uVar13`. These are mathematically complex ways to perform very simple operations (like adding 1 or comparing a value). This makes it extremely difficult for a human analyst or an automated tool to determine what the "real" logic is.
*   **Opaque Predicates:** Several segments of the code appear to be "opaque predicates"—calculations that always result in a specific value but are written in a complex way so that a disassembler cannot easily skip them as "dead code."

### Notable Techniques & Patterns
*   **Jump Table Obfuscation:** The `UNRECOVERED_JUMPTABLE` warning is a hallmark of advanced obfuscation. It indicates the compiler/protector has intentionally broken the linear flow, forcing the analyst to trace every jump manually.
*   **Bitwise Rotations and Shifting:** The code uses extensive bit-shifting and rotation (e.g., `uVar13 >> uVar18 | uVar13 << 0x40 - uVar18`) to manipulate values. In this context, these are usually used to calculate the "next" state of a virtual machine or a flattened dispatcher.
*   **Constant Mangling:** Instead of using recognizable constants (like `0x55` for printing), the code uses hex-heavy calculations (`- 0x4cce7be6`, `- 0x70e68379`) to mask basic arithmetic.

### Summary for Analysts
This is not a "functional" piece of malware in isolation (like a downloader or an injector); rather, it is a **protection layer**. The heavy use of control-flow flattening and MBA suggests this sample is intended to thwart automated scanning and manual reverse engineering. 

**Recommendation:** This code confirms the presence of a sophisticated packer or protector. To analyze the actual payload, you will likely need to perform dynamic analysis (debugging) to observe the "unpacked" state in memory or use symbolic execution tools (like Triton or Miasm) to simplify the arithmetic expressions.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027.001** | Packing | The report explicitly identifies the code as a "protection layer" and a "sophisticated packer or protector" intended to hide the true payload from analysis. |
| **T1027** | Obfuscated Files or Information | The use of Control-Flow Flattening (CFF), Mixed Boolean-Arithmetic (MBA), and Opaque Predicates are primary methods used to obfuscate code logic and hinder automated/manual reverse engineering. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided data indicates a highly obfuscated binary. The "Strings" section contains mostly non-human-readable, mangled character sets typical of packed or protected code. The "Behavioral Analysis" confirms that this sample utilizes advanced evasion techniques like Control-Flow Flattening (CFF) and Mixed Boolean-Arithmetic (MBA).

---

### **Indicators of Compromise**

**IP addresses / URLs / Domains**
*   *None identified.* (The raw strings do not contain plain-text network indicators.)

**File paths / Registry keys**
*   *None identified.*

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Function Offset:** `00b122ca` (Identified as the primary obfuscation/dispatcher routine).
*   **Obfuscation Techniques:** 
    *   Control-Flow Flattening (CFF)
    *   Mixed Boolean-Arithmetic (MBA)
    *   Jump Table Obfuscation
    *   Constant Mangling (e.g., `0x4cce7be6`, `0x70e68379`)

---

### **Analyst Notes**
While no traditional "network" IOCs (IPs/Domains) were extracted from the raw strings, the behavioral analysis confirms this is a sophisticated **protection layer**. The presence of MBA and CFF suggests that any further malicious functionality (such as Command & Control communication or data exfiltration) is currently hidden behind multiple layers of obfuscation. 

**Recommendation:** Proceed with dynamic analysis in a sandboxed environment to capture "in-memory" indicators, such as decrypted strings or active network connections, once the dispatcher routine executes.

---

## Malware Family Classification

1. **Malware family:** Unknown
2. **Malware type:** Loader (specifically a Packer/Protector)
3. **Confidence:** High
4. **Key evidence:**
*   **Advanced Obfuscation Techniques:** The sample utilizes high-level obfuscation methods, specifically Control-Flow Flattening (CFF) and Mixed Boolean-Arithmetic (MBA), which are hallmark indicators of sophisticated protection layers.
*   **Protective Packaging:** Analysis indicates the code serves as a "dispatcher" or "protection layer" rather than a functional piece of malware like a RAT or wiper; its primary goal is to hinder analysis and hide a secondary, currently hidden payload.
*   **Anti-Analysis Design:** The presence of complex jump tables, constant mangling, and opaque predicates demonstrates a deliberate attempt to thwart both automated scanning and manual reverse engineering by security researchers.
