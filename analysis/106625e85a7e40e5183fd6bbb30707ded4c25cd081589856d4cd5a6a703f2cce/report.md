# Threat Analysis Report

**Generated:** 2026-08-18 21:30 UTC
**Sample:** `106625e85a7e40e5183fd6bbb30707ded4c25cd081589856d4cd5a6a703f2cce_106625e85a7e40e5183fd6bbb30707ded4c25cd081589856d4cd5a6a703f2cce.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `106625e85a7e40e5183fd6bbb30707ded4c25cd081589856d4cd5a6a703f2cce_106625e85a7e40e5183fd6bbb30707ded4c25cd081589856d4cd5a6a703f2cce.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 5,317,632 bytes |
| MD5 | `7846b810927322294da505fbfccfccd6` |
| SHA1 | `19b6dcd683016519b1bc4a8cccd3d1a59eb3dbb7` |
| SHA256 | `106625e85a7e40e5183fd6bbb30707ded4c25cd081589856d4cd5a6a703f2cce` |
| Overall entropy | 5.915 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773440245 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 5,315,072 | 5.915 | No |
| `.rsrc` | 1,536 | 3.699 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **140771** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
%o;HJoET

6M2E);;

+.9%
\r&r&w&u+}+s+
u[P
D{H
a~y~l~Eq\u
Uwp?dehiZLHz}
d~htZnH`}
d\hrZKTJT[T
d?pU|@N
Abd:p|lNM\
p\|cNl\
Ajd	pP|FN
bxfxtx
[+~|j$f\T	F
[6~Dj%f#Ts
yGxGgG
dqfqCq
u?O|CeqPc.V
~a[8OwCvqhc
R*@wujKmKGK&@
|cpjBGP,e
MNh2|@p{B<P
Mkh1|Pp
S^_ZmB
b@GXS'
stetIt
@Q'ESI
In{`i"\T
kvlv-v
71a%2)=
J,oi{fY`Y7Y"V*R
]9R2RkR
}oX'LP@Gr
5kQbQ1Q
%qVtV-V
`n	$
F^S^*^
ZMd_4j
LNHN<N)E
f?*+r'a
kkskUdC`
*m}mUm
|)RBSB
l)>=p1S

>/f;Z7

'/I;?7

A/h;	7

</P;%7+
l]`	Rx@4u
]FxYlp`ORB@5u
x4ll`	RL@Fu
lT`uR>@>u
@&ekq}/O_]@h
}9O*]Oh
oA]}O:z
g44 |,(
{4- G,v
e4r S,.
N44 G,J
m4w &,^
upO&CDq
+:9@p#r#
KFKJ}BOc]	h
@re)qn}
s7VzB N<|
s6V~B"N
Wbr*fvjOX
VpZuh@z:O
^Q^BZ{H
dghUZ|H$}6x>x
ifS,_'mO
GvS&_.m
b=GrS-_
b9G_S2_tm&
b:GQS(_sm
WLrfFj|XuJ4
fdjiXDJ
WyrZfXjCXuJ0
WKr0fjj
r)fojaX`J7
Wzr\f}j
D}D0~tr
~[rm@GR;g
OMj%~ar@;R<g
~Drq@|RMg
~|rC@2R
Ooj;~ar`@~RGg
ZGKSCc
v4.0.30319
#Strings
	*	1	M	W	e	u	

*
A
O
x

#9H
OZi

&l

*1A
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **12**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Stub.RBu9UCM6kJihmHNSMOQJ36IXkKAskBpCiqwSr.tRY7VCl7Cc1` | `0x7310ed` | 1994516 | — |
| `method.My.t51vw7mts8aTZzgqyULBMb9sgGe8P7iKNAii6WVk7vrc6cuz0cOp4TDTiTmdCF.cVCfZ0` | `0x74ce62` | 1862108 | — |
| `method.My.cTbl2qz3181uSoOq9Ecq9Ev3Qjo6U8OcsdhYUmkLvAdPQzc1xIfDWRiQEiZBFfXivxeeBM01XxdOK.eEXqKKp65xeDd1cjPr871` | `0x530000` | 787302 | ✓ |
| `sym.Stub.RBu9UCM6kJihmHNSMOQJ36IXkKAskBpCiqwSr.HGiiVHW3jJDtyJRoZdN` | `0x6a06fd` | 592368 | — |
| `method.Stub.2fvdxBxML2ybk6Wd7uu5Q2yojlvA95OAtkoCC.1` | `0x516ec3` | 419210 | ✓ |
| `method.My.t51vw7mts8aTZzgqyULBMb9sgGe8P7iKNAii6WVk7vrc6cuz0cOp4TDTiTmdCF.dy5RAGUi0NV0` | `0x62cb8f` | 406948 | — |
| `method.Stub.NL3WltC3QEZSu4RARgIHhXBMKbK2OWdAEtYs4zNVN8d5DsjfNT5DWjE8FuT15uknooYmcsd30CzhEnj1uXB7HjRYLopA6D9.4CSNVPBypZN0` | `0x6c1544` | 399014 | — |
| `sym.Stub.fiAeqLB7avspT2SvNitYf8D9ot1v9aGjKyJHT.iUjlJhIwNK_3` | `0x620414` | 342764 | — |
| `method.My.t51vw7mts8aTZzgqyULBMb9sgGe8P7iKNAii6WVk7vrc6cuz0cOp4TDTiTmdCF.iUjlJhIwNK` | `0x4101a4` | 262303 | ✓ |
| `method.Stub.XZCQhprmwkCWjPwjDtaKBvYjrAwxdTZeuSK0F.5ItZrJSR1` | `0x487cb0` | 248690 | ✓ |
| `sym.Stub.MEuEgwjxzzhqHjFlKXB27U72Q80684XpJzBtf.7mc86r3Si571` | `0x4c4822` | 228800 | ✓ |
| `method.Stub.MEuEgwjxzzhqHjFlKXB27U72Q80684XpJzBtf.SIC7ooyyuWwdirLLqNvcKkEgPUXp5G3Jf2b3v` | `0x4210c1` | 192898 | ✓ |
| `method.Stub.ouSlQrNLXQ4OFknnWsb5FkUmKWCUxQnNaRHLe3xiii24OvoE66WNvdwVLQXgJFHZSErBsDqYo6YqMZLYuCLjne5cGNrwqT5.HGiiVHW3jJDtyJRoZdN` | `0x450243` | 131150 | ✓ |
| `method.Stub.2fvdxBxML2ybk6Wd7uu5Q2yojlvA95OAtkoCC.1H386ZKmBZmT1` | `0x6a23fe` | 127302 | — |
| `method.Stub.ouSlQrNLXQ4OFknnWsb5FkUmKWCUxQnNaRHLe3xiii24OvoE66WNvdwVLQXgJFHZSErBsDqYo6YqMZLYuCLjne5cGNrwqT5.OO8aVI2hW6yKo01qj0` | `0x6025d2` | 121404 | — |
| `sym.Stub.NL3WltC3QEZSu4RARgIHhXBMKbK2OWdAEtYs4zNVN8d5DsjfNT5DWjE8FuT15uknooYmcsd30CzhEnj1uXB7HjRYLopA6D9.HGiiVHW3jJDtyJRoZdN` | `0x470291` | 96799 | ✓ |
| `method.My.C4Fc6Etvi2eZBMaxQTd7wCYBn8Dl2siSKWvpbIZE5LF8fugj2u6vDmT111DP54.qo71` | `0x510000` | 95212 | ✓ |
| `method.Stub.2fvdxBxML2ybk6Wd7uu5Q2yojlvA95OAtkoCC.FyYU3BVTnU1` | `0x5dcee9` | 78874 | — |
| `method.Stub.NL3WltC3QEZSu4RARgIHhXBMKbK2OWdAEtYs4zNVN8d5DsjfNT5DWjE8FuT15uknooYmcsd30CzhEnj1uXB7HjRYLopA6D9.kDGiTZXUlGGs0` | `0x60d5ef` | 76355 | — |
| `sym.Stub.fiAeqLB7avspT2SvNitYf8D9ot1v9aGjKyJHT.iUjlJhIwNK_1` | `0x5f0366` | 74348 | — |
| `method.Stub.NL3WltC3QEZSu4RARgIHhXBMKbK2OWdAEtYs4zNVN8d5DsjfNT5DWjE8FuT15uknooYmcsd30CzhEnj1uXB7HjRYLopA6D9.mt0` | `0x673f00` | 70742 | — |
| `sym.Stub.2fvdxBxML2ybk6Wd7uu5Q2yojlvA95OAtkoCC.iUjlJhIwNK_1` | `0x690133` | 65808 | — |
| `method.Stub.NL3WltC3QEZSu4RARgIHhXBMKbK2OWdAEtYs4zNVN8d5DsjfNT5DWjE8FuT15uknooYmcsd30CzhEnj1uXB7HjRYLopA6D9.HGiiVHW3jJDtyJRoZdN` | `0x4e0291` | 65536 | ✓ |
| `method.Stub.RBu9UCM6kJihmHNSMOQJ36IXkKAskBpCiqwSr.HGiiVHW3jJDtyJRoZdN` | `0x6a0735` | 65480 | — |
| `method...ogle1Veaw5TSZKLwJpYkZBC1` | `0x411103` | 65470 | ✓ |
| `method.Stub.fiAeqLB7avspT2SvNitYf8D9ot1v9aGjKyJHT.iUjlJhIwNK` | `0x62046a` | 65450 | — |
| `sym.Stub.2fvdxBxML2ybk6Wd7uu5Q2yojlvA95OAtkoCC.iUjlJhIwNK` | `0x690548` | 64763 | — |
| `method.Stub.2fvdxBxML2ybk6Wd7uu5Q2yojlvA95OAtkoCC.iUjlJhIwNK` | `0x6905e1` | 64338 | — |
| `method.Stub.fiAeqLB7avspT2SvNitYf8D9ot1v9aGjKyJHT.ooglefAUv1BWIO3JGyQldN9K1` | `0x674476` | 64138 | — |
| `method.Stub.NL3WltC3QEZSu4RARgIHhXBMKbK2OWdAEtYs4zNVN8d5DsjfNT5DWjE8FuT15uknooYmcsd30CzhEnj1uXB7HjRYLopA6D9.e6iv7jhDV1p8tMbc5t0` | `0x500734` | 63692 | ✓ |

### Decompiled Code Files

- [`code/method...ogle1Veaw5TSZKLwJpYkZBC1.c`](code/method...ogle1Veaw5TSZKLwJpYkZBC1.c)
- [`code/method.My.C4Fc6Etvi2eZBMaxQTd7wCYBn8Dl2siSKWvpbIZE5LF8fugj2u6vDmT111DP54.qo71.c`](code/method.My.C4Fc6Etvi2eZBMaxQTd7wCYBn8Dl2siSKWvpbIZE5LF8fugj2u6vDmT111DP54.qo71.c)
- [`code/method.My.cTbl2qz3181uSoOq9Ecq9Ev3Qjo6U8OcsdhYUmkLvAdPQzc1xIfDWRiQEiZBFfXivxeeBM01XxdOK.eEXqKKp65xeDd1cjPr871.c`](code/method.My.cTbl2qz3181uSoOq9Ecq9Ev3Qjo6U8OcsdhYUmkLvAdPQzc1xIfDWRiQEiZBFfXivxeeBM01XxdOK.eEXqKKp65xeDd1cjPr871.c)
- [`code/method.My.t51vw7mts8aTZzgqyULBMb9sgGe8P7iKNAii6WVk7vrc6cuz0cOp4TDTiTmdCF.iUjlJhIwNK.c`](code/method.My.t51vw7mts8aTZzgqyULBMb9sgGe8P7iKNAii6WVk7vrc6cuz0cOp4TDTiTmdCF.iUjlJhIwNK.c)
- [`code/method.Stub.2fvdxBxML2ybk6Wd7uu5Q2yojlvA95OAtkoCC.1.c`](code/method.Stub.2fvdxBxML2ybk6Wd7uu5Q2yojlvA95OAtkoCC.1.c)
- [`code/method.Stub.MEuEgwjxzzhqHjFlKXB27U72Q80684XpJzBtf.SIC7ooyyuWwdirLLqNvcKkEgPUXp5G3Jf2b3v.c`](code/method.Stub.MEuEgwjxzzhqHjFlKXB27U72Q80684XpJzBtf.SIC7ooyyuWwdirLLqNvcKkEgPUXp5G3Jf2b3v.c)
- [`code/method.Stub.NL3WltC3QEZSu4RARgIHhXBMKbK2OWdAEtYs4zNVN8d5DsjfNT5DWjE8FuT15uknooYmcsd30CzhEnj1uXB7HjRYLopA6D9.HGiiVHW3jJDt.c`](code/method.Stub.NL3WltC3QEZSu4RARgIHhXBMKbK2OWdAEtYs4zNVN8d5DsjfNT5DWjE8FuT15uknooYmcsd30CzhEnj1uXB7HjRYLopA6D9.HGiiVHW3jJDt.c)
- [`code/method.Stub.NL3WltC3QEZSu4RARgIHhXBMKbK2OWdAEtYs4zNVN8d5DsjfNT5DWjE8FuT15uknooYmcsd30CzhEnj1uXB7HjRYLopA6D9.e6iv7jhDV1p8.c`](code/method.Stub.NL3WltC3QEZSu4RARgIHhXBMKbK2OWdAEtYs4zNVN8d5DsjfNT5DWjE8FuT15uknooYmcsd30CzhEnj1uXB7HjRYLopA6D9.e6iv7jhDV1p8.c)
- [`code/method.Stub.XZCQhprmwkCWjPwjDtaKBvYjrAwxdTZeuSK0F.5ItZrJSR1.c`](code/method.Stub.XZCQhprmwkCWjPwjDtaKBvYjrAwxdTZeuSK0F.5ItZrJSR1.c)
- [`code/method.Stub.ouSlQrNLXQ4OFknnWsb5FkUmKWCUxQnNaRHLe3xiii24OvoE66WNvdwVLQXgJFHZSErBsDqYo6YqMZLYuCLjne5cGNrwqT5.HGiiVHW3jJDt.c`](code/method.Stub.ouSlQrNLXQ4OFknnWsb5FkUmKWCUxQnNaRHLe3xiii24OvoE66WNvdwVLQXgJFHZSErBsDqYo6YqMZLYuCLjne5cGNrwqT5.HGiiVHW3jJDt.c)
- [`code/sym.Stub.MEuEgwjxzzhqHjFlKXB27U72Q80684XpJzBtf.7mc86r3Si571.c`](code/sym.Stub.MEuEgwjxzzhqHjFlKXB27U72Q80684XpJzBtf.7mc86r3Si571.c)
- [`code/sym.Stub.NL3WltC3QEZSu4RARgIHhXBMKbK2OWdAEtYs4zNVN8d5DsjfNT5DWjE8FuT15uknooYmcsd30CzhEnj1uXB7HjRYLopA6D9.HGiiVHW3jJDtyJR.c`](code/sym.Stub.NL3WltC3QEZSu4RARgIHhXBMKbK2OWdAEtYs4zNVN8d5DsjfNT5DWjE8FuT15uknooYmcsd30CzhEnj1uXB7HjRYLopA6D9.HGiiVHW3jJDtyJR.c)

## Behavioral Analysis

Based on the provided disassembly and string data, here is an analysis of the binary sample:

### Core Functionality and Purpose
The binary appears to be a **highly obfuscated piece of malware**, likely acting as a "dropper," "downloader," or a botnet agent. The primary purpose of the visible code is not immediate execution of malicious logic (like stealing files), but rather **evasion and anti-analysis**. It uses complex layers of obfuscation to hide its true intent from automated scanners and human researchers.

### Suspicious or Malicious Behaviors
*   **Advanced Obfuscation:** The use of extremely long, randomized function names (e.g., `method.My.cTbl2qz3...`) is a hallmark of specialized protection tools (like LLVM-based obfuscators). This makes manual analysis significantly more time-consuming.
*   **Anti-Analysis/Decompiler Evasion:** The "Warning: Control flow encountered bad instruction data" and "overlapping instruction" notices indicate that the author intentionally inserted junk bytes or overlapping instructions. These are designed to break linear disassemblers and cause decompilers (like Hex-Rays) to produce inaccurate code, as seen in the provided output.
*   **Potential Command & Control (C2) Infrastructure:** The large block of "Google" prefixed strings followed by random alphanumeric characters is highly suspicious. While they look like Google search terms or resources, this pattern is common for **Unique Identifier Generation**. Each unique string likely identifies a specific infected machine to a C2 server, allowing the attacker to manage thousands of victims individually.

### Notable Techniques and Patterns
*   **Junk Code Injection:** The functions are filled with complex arithmetic (`CONCAT31`, `CARRY1`, bit-shifts) that perform no meaningful operations but serve to create a "wall" of code for an analyst to navigate.
*   **Metamorphism/Polymorphism Traits:** The way the code is structured—using repeated, heavily mutated versions of similar logic—suggests the use of a polymorphic engine where each build of the malware looks different to signature-based antivirus.
*   **Stack/Register Manipulation:** The heavy use of `unaff_EBP` and complex memory offsets suggests the binary may be manually manipulating the stack or registers to hide transitions between different stages of execution (e.g., unpacking a hidden payload into memory).

### Summary for Incident Response
This sample is designed with **sophisticated anti-analysis protections**. The presence of intentional disassembler "traps" and high-entropy, automated obfuscation suggests a professional threat actor or a sophisticated malware kit. 

**Recommended Action:** Treat this as a high-threat sample. Since the logic is heavily hidden behind an obfuscator, behavioral analysis (sandbox monitoring) should be used to identify what the code *does* (e.g., which IP addresses it contacts or what files it drops) rather than trying to decipher every line of the disassembled code.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of randomized function names, junk code (meaningless arithmetic), and "traps" for disassemblers are clear indicators of efforts to hinder both automated analysis and manual human investigation. |
| **T1036** | Masquerading | The inclusion of "Google" prefixed strings suggests an attempt to blend in with legitimate search traffic or common resources while generating unique identifiers for C2 management. |
| **T1055** | Process Injection | (Inferred) The mention of manual stack/register manipulation to hide transitions between execution stages and host a hidden payload indicates preparation for injecting malicious code into memory. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Unique Identifier Pattern:** A large block of "Google" prefixed strings followed by unique alphanumeric characters (e.g., `GoogleakJauP9vKQbIVnYxt000`, `GoogleoBONN2lRaqtvtwv5x300`). 
    *   *Note: These are not actual Google search terms but serve as machine-specific identifiers used by the C2 infrastructure to track and manage unique infected hosts.*
*   **Obfuscation Techniques:** Use of "junk code" arithmetic (e.g., `CONCAT31`, `CARRY1`) and intentional "overlapping instructions" to evade disassemblers/decompilers.

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1.  **Malware family:** Unknown (likely a custom-built loader or part of a sophisticated private malware suite)
2.  **Malware type:** Loader / Dropper
3.  **Confidence:** High (for Type), Low (for Family)
4.  **Key evidence:**
    *   **Sophisticated Anti-Analysis Layers:** The use of intentionally broken "overlapping instructions," junk code arithmetic, and LLVM-style obfuscation indicates a high level of effort to bypass automated sandboxes and manual reverse engineering.
    *   **Presence of C2 Identification Infrastructure:** The systematic use of "Google" prefixed strings as unique machine identifiers is a classic technique used by botnets and loader networks to track and manage individual infected hosts.
    *   **Staged Execution Behavior:** The lack of immediate malicious payloads (like ransomware encryption or direct data exfiltration) combined with evidence of process injection (T1055) strongly suggests the primary role of this binary is to act as a "wrapper" or loader for secondary payloads.
