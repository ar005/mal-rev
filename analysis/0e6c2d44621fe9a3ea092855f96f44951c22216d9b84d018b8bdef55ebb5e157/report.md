# Threat Analysis Report

**Generated:** 2026-08-12 02:01 UTC
**Sample:** `0e6c2d44621fe9a3ea092855f96f44951c22216d9b84d018b8bdef55ebb5e157_0e6c2d44621fe9a3ea092855f96f44951c22216d9b84d018b8bdef55ebb5e157.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e6c2d44621fe9a3ea092855f96f44951c22216d9b84d018b8bdef55ebb5e157_0e6c2d44621fe9a3ea092855f96f44951c22216d9b84d018b8bdef55ebb5e157.exe` |
| File type | PE32+ executable for MS Windows 4.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 2,454,016 bytes |
| MD5 | `45b623639ae1eb7cb6b617e6eba041d9` |
| SHA1 | `40bc1be9ea197a6de29ff426b0fef8e96d1c7e72` |
| SHA256 | `0e6c2d44621fe9a3ea092855f96f44951c22216d9b84d018b8bdef55ebb5e157` |
| Overall entropy | 5.025 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3700126959 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 2,451,968 | 5.024 | No |
| `.rsrc` | 1,536 | 3.47 | No |

## Extracted Strings

Total strings found: **62756** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
 BC<&+
Vaa*^ 
 7=b& 
Laa*2 
a*: l8
Aff c8
X 4-Vs 
XEnaY*
 (hop&+
*^ [1&
\aa*2 
C.aaf(
hF AK
hF AK
!8aY*J ?S
aZ YIO
&aX*^ 
d&a Ow
f BbwXaf(
 TzPB 
*N Lpz`f jpz`af(
j -z>} 
a -z>} 
g"8aa*^ 9
 o<_&&+
:ff |g
 7D!h 
Faaf*N T
 AIDS&+
 r#b& 
Waa*J 
 g(9v 
<lA @<lAY(
 h%7M&+
Bwaa*: e
 JH g WI g 
?b+aZ r
 -Rjj 
tia >1@
+aY*N 
 ]k82&+
," JB+
," @`L
^R,aa*
 X!Boa 
)1	aY*
P#na P_gq 0
a P_gq 0
|e =
5	; %91gaa(
#{Oa 
FaX r-
Aa mN$
|e @?bNaa(
R 	gK
a 
7zF "?tgaZ 
-_ D0F2a 
ZEaaf(
 sH14 "A04a
04 "A04a
 /h14 "A04a

 /h14 "A04a
 Ib%p&+
 h|pl&+
_X|a A
{aZ h`
Xaff 0
Z-j !u97aaf(
xaaf.)
uaa.+
VRaaf(
kff 
;HSaX 
X rNm# 
-#aY;_
^ D Ia 
J[f ,$]@ 
X Vk U 
!Uaa 

->+Bs
}|a &0
 ig&V 

%-<&~
Z ;6K L~Kaa(
YbDaY3
x' > lnaafjXo!
 \o>G ]o=Ga 
haYf x
naa_ Y	
haaf(>
saf_
(
 n.6Naf ]v
=@Mae 
D'I \+'IaX 
saa jH
{af T
 3af}
 MdK1 q
4MaZ #
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x4058b8` | 2451272 | ✓ |
| `method.A.cfd1396f04d57f33e124a8a8366a5dea8.c2a50f21eeb703e761faf244541f931dc` | `0x405a04` | 65204 | ✓ |
| `method.c31ef09b904334e7b28b8cd3ed0ca76f5.cd50ead0f6093de9dae588f3686052a13` | `0x404a18` | 1004 | ✓ |
| `method.SM4_DEC_1.SM4Decrypt.DecryptCbc` | `0x402618` | 904 | ✓ |
| `method.A.c9aece3acb518bd72d9dde553a1ff8c89.c22ee1f107b8e7582f0a782a602fccc7b` | `0x403634` | 900 | ✓ |
| `method.A.c3479d560663cb7eda9f184cbf63b5218.cba7a9d4a7b36c3eca2efd99a5bf25328` | `0x403a28` | 716 | ✓ |
| `method.A.c32bdda81623d38ce51e33c674de21cf8.cba7a9d4a7b36c3eca2efd99a5bf25328` | `0x404004` | 608 | ✓ |
| `method.A.cb197467ed5a2e313431bec3da397e7bb.cba7a9d4a7b36c3eca2efd99a5bf25328` | `0x403d54` | 592 | ✓ |
| `method.SM4_DEC_1.SM4Decrypt.DecryptBlob` | `0x402a18` | 572 | ✓ |
| `method.SM4_DEC_1.SM4Decrypt.ChineseHexToBytes` | `0x402c54` | 456 | ✓ |
| `method.SM4_DEC_1.SM4Core.ExpandKey` | `0x4022c4` | 420 | ✓ |
| `method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.ce5490282e1af0324328ec4498826ef28` | `0x4043a8` | 400 | ✓ |
| `method.SM4_DEC_1.SM4Core.DecryptBlock` | `0x402468` | 364 | ✓ |
| `method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e..cctor` | `0x404264` | 304 | ✓ |
| `method.SM4_DEC_1.SM4Decrypt.FromHex` | `0x402e1c` | 252 | ✓ |
| `method.A.ce274703d228b4531afd8558bf02d0160.c941b020448f08c10cf4a2bd534f13b10` | `0x40332c` | 244 | ✓ |
| `method.c31ef09b904334e7b28b8cd3ed0ca76f5..cctor` | `0x404848` | 244 | ✓ |
| `method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.cc4135be38e9892eecdfd772f73c74947` | `0x40463c` | 240 | ✓ |
| `method.A.c9aece3acb518bd72d9dde553a1ff8c89.ca6d078d734e5768d8787004642a6f5a5` | `0x4034d4` | 232 | ✓ |
| `method.A.c5f43ed01f49a5b16ec4a82616beee37f.ce3b25dfa6061506c172701e7e9b01812` | `0x4031cc` | 224 | ✓ |
| `method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.c582c0aa5e53db3b2f8422ebd955c2bf1` | `0x404774` | 212 | ✓ |
| `method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.c06ce978bad074c9caecd1ad2aace8235` | `0x4045a4` | 152 | ✓ |
| `method.c31ef09b904334e7b28b8cd3ed0ca76f5..ctor` | `0x40493c` | 152 | ✓ |
| `method.SM4_DEC_1.SM4Core.Tau` | `0x4020d8` | 132 | ✓ |
| `method.A.c459a2d15a7dd3beb6fc7448ff8902c44.c7c55e32b0ee59c83888d633a66e8d43d` | `0x403058` | 132 | ✓ |
| `method.SM4_DEC_1.SM4Decrypt.DeriveKey` | `0x4029a0` | 120 | ✓ |
| `method.A.c5f43ed01f49a5b16ec4a82616beee37f..cctor` | `0x4030dc` | 108 | ✓ |
| `method.A.ce274703d228b4531afd8558bf02d0160..cctor` | `0x4032ac` | 108 | ✓ |
| `method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.c4c63b901fce5d226b50eb8cce9bc1e3a` | `0x404538` | 108 | ✓ |
| `method.A.c459a2d15a7dd3beb6fc7448ff8902c44.cbb17542cfae0680a02d62af104df12bf` | `0x402f98` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.A.c32bdda81623d38ce51e33c674de21cf8.cba7a9d4a7b36c3eca2efd99a5bf25328.c`](code/method.A.c32bdda81623d38ce51e33c674de21cf8.cba7a9d4a7b36c3eca2efd99a5bf25328.c)
- [`code/method.A.c3479d560663cb7eda9f184cbf63b5218.cba7a9d4a7b36c3eca2efd99a5bf25328.c`](code/method.A.c3479d560663cb7eda9f184cbf63b5218.cba7a9d4a7b36c3eca2efd99a5bf25328.c)
- [`code/method.A.c459a2d15a7dd3beb6fc7448ff8902c44.c7c55e32b0ee59c83888d633a66e8d43d.c`](code/method.A.c459a2d15a7dd3beb6fc7448ff8902c44.c7c55e32b0ee59c83888d633a66e8d43d.c)
- [`code/method.A.c459a2d15a7dd3beb6fc7448ff8902c44.cbb17542cfae0680a02d62af104df12bf.c`](code/method.A.c459a2d15a7dd3beb6fc7448ff8902c44.cbb17542cfae0680a02d62af104df12bf.c)
- [`code/method.A.c5f43ed01f49a5b16ec4a82616beee37f..cctor.c`](code/method.A.c5f43ed01f49a5b16ec4a82616beee37f..cctor.c)
- [`code/method.A.c5f43ed01f49a5b16ec4a82616beee37f.ce3b25dfa6061506c172701e7e9b01812.c`](code/method.A.c5f43ed01f49a5b16ec4a82616beee37f.ce3b25dfa6061506c172701e7e9b01812.c)
- [`code/method.A.c9aece3acb518bd72d9dde553a1ff8c89.c22ee1f107b8e7582f0a782a602fccc7b.c`](code/method.A.c9aece3acb518bd72d9dde553a1ff8c89.c22ee1f107b8e7582f0a782a602fccc7b.c)
- [`code/method.A.c9aece3acb518bd72d9dde553a1ff8c89.ca6d078d734e5768d8787004642a6f5a5.c`](code/method.A.c9aece3acb518bd72d9dde553a1ff8c89.ca6d078d734e5768d8787004642a6f5a5.c)
- [`code/method.A.cb197467ed5a2e313431bec3da397e7bb.cba7a9d4a7b36c3eca2efd99a5bf25328.c`](code/method.A.cb197467ed5a2e313431bec3da397e7bb.cba7a9d4a7b36c3eca2efd99a5bf25328.c)
- [`code/method.A.ce274703d228b4531afd8558bf02d0160..cctor.c`](code/method.A.ce274703d228b4531afd8558bf02d0160..cctor.c)
- [`code/method.A.ce274703d228b4531afd8558bf02d0160.c941b020448f08c10cf4a2bd534f13b10.c`](code/method.A.ce274703d228b4531afd8558bf02d0160.c941b020448f08c10cf4a2bd534f13b10.c)
- [`code/method.A.cfd1396f04d57f33e124a8a8366a5dea8.c2a50f21eeb703e761faf244541f931dc.c`](code/method.A.cfd1396f04d57f33e124a8a8366a5dea8.c2a50f21eeb703e761faf244541f931dc.c)
- [`code/method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e..cctor.c`](code/method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e..cctor.c)
- [`code/method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.c06ce978bad074c9caecd1ad2aace8235.c`](code/method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.c06ce978bad074c9caecd1ad2aace8235.c)
- [`code/method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.c4c63b901fce5d226b50eb8cce9bc1e3a.c`](code/method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.c4c63b901fce5d226b50eb8cce9bc1e3a.c)
- [`code/method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.c582c0aa5e53db3b2f8422ebd955c2bf1.c`](code/method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.c582c0aa5e53db3b2f8422ebd955c2bf1.c)
- [`code/method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.cc4135be38e9892eecdfd772f73c74947.c`](code/method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.cc4135be38e9892eecdfd772f73c74947.c)
- [`code/method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.ce5490282e1af0324328ec4498826ef28.c`](code/method.A.cfdf32c3fb873de95e9c9ac99da8d2b9e.ce5490282e1af0324328ec4498826ef28.c)
- [`code/method.SM4_DEC_1.SM4Core.DecryptBlock.c`](code/method.SM4_DEC_1.SM4Core.DecryptBlock.c)
- [`code/method.SM4_DEC_1.SM4Core.ExpandKey.c`](code/method.SM4_DEC_1.SM4Core.ExpandKey.c)
- [`code/method.SM4_DEC_1.SM4Core.Tau.c`](code/method.SM4_DEC_1.SM4Core.Tau.c)
- [`code/method.SM4_DEC_1.SM4Decrypt.ChineseHexToBytes.c`](code/method.SM4_DEC_1.SM4Decrypt.ChineseHexToBytes.c)
- [`code/method.SM4_DEC_1.SM4Decrypt.DecryptBlob.c`](code/method.SM4_DEC_1.SM4Decrypt.DecryptBlob.c)
- [`code/method.SM4_DEC_1.SM4Decrypt.DecryptCbc.c`](code/method.SM4_DEC_1.SM4Decrypt.DecryptCbc.c)
- [`code/method.SM4_DEC_1.SM4Decrypt.DeriveKey.c`](code/method.SM4_DEC_1.SM4Decrypt.DeriveKey.c)
- [`code/method.SM4_DEC_1.SM4Decrypt.FromHex.c`](code/method.SM4_DEC_1.SM4Decrypt.FromHex.c)
- [`code/method.c31ef09b904334e7b28b8cd3ed0ca76f5..cctor.c`](code/method.c31ef09b904334e7b28b8cd3ed0ca76f5..cctor.c)
- [`code/method.c31ef09b904334e7b28b8cd3ed0ca76f5..ctor.c`](code/method.c31ef09b904334e7b28b8cd3ed0ca76f5..ctor.c)
- [`code/method.c31ef09b904334e7b28b8cd3ed0ca76f5.cd50ead0f6093de9dae588f3686052a13.c`](code/method.c31ef09b904334e7b28b8cd3ed0ca76f5.cd50ead0f6093de9dae588f3686052a13.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary sample:

### Core Functionality and Purpose
The primary purpose of this code appears to be a **loader/decryptor** (likely part of a "packer" or "dropper"). The core logic revolves around decrypting embedded data. 

*   **Encryption Implementation:** The presence of multiple functions starting with `method.SM4_DEC_1...` indicates the use of the **SM4 block cipher**. SM4 is a symmetric key algorithm widely used in China; its presence in malware often suggests high-sophistication or specific regional threat actor origin.
*   **Decryption Pipeline:** The naming convention (`DecryptCbc`, `DecryptBlob`, `DeriveKey`, `ExpandKey`) indicates a standard cryptographic implementation used to unpack an internal payload, configuration file, or further stages of the malware.

### Suspicious and Malicious Behaviors
While this specific snippet does not show direct "actions" like downloading files or injecting into processes (likely because it occurs in the unpacking stage), several indicators point to malicious intent:

*   **Payload Concealment:** The transition from a decryption routine (`DecryptBlob`) to subsequent functionality suggests that the actual malicious payload is encrypted and hidden within the file until it can be decrypted in memory.
*   **Obfuscated Control Flow:** The decompiler notes (e.g., `WARNING: Control flow encountered bad instruction data` and `halt_baddata()`) are clear indicators of **anti-analysis techniques**. These typically occur when a compiler/packer uses "junk code," "opaque predicates," or "self-modifying code" to break linear disassemblers (like IDA Pro or Ghidra).
*   **Garbage Strings:** The extracted strings contain mostly non-printable characters and high-entropy data. This is a hallmark of **packing**, where the original string table of the malicious payload is compressed or encrypted until execution.

### Notable Techniques & Patterns
*   **SM4 Cryptography:** As noted, SM4 is frequently used by advanced persistent threat (APT) groups to encrypt Command & Control (C2) communications and internal payloads.
*   **Anti-Disassembly/Decompilation:** 
    *   The "Bad instruction" warnings suggest the use of **junk code insertion**. This confuses disassemblers into interpreting data as code, leading to the "broken" C pseudocode seen in `entry0`.
    *   The complex arithmetic and bitwise operations in `entry0` (e.g., `CONCAT`, `ROUND`, `POPCOUNT`) are often used by protectors to calculate jump targets dynamically, preventing static analysis tools from mapping out the execution flow.
*   **Import/Symbol Mangling:** The long, alphanumeric method names (e.g., `method.A.cfd1396...`) indicate that the binary has been processed by a protector or packer that strips original symbols and replaces them with generated identifiers to hinder human analysis.

### Summary Table
| Feature | Observation | Risk Level |
| :--- | :--- | :--- |
| **Encryption** | SM4 Algorithm (DecryptCbc, ExpandKey) | High |
| **Obfuscation** | Junk code / Broken control flow | High |
| **Packing** | Encrypted strings and "bad instruction" artifacts | High |
| **Tactic** | Likely a Stage-1 Loader or Packer | High |

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the relevant MITRE ATT&CK techniques. The primary behavior identified in this sample—the use of encryption, junk code, and packing to hinder analysis—falls under the **Defense Evasion** tactic.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The implementation of the SM4 block cipher (DecryptCbc, ExpandKey) is used to encrypt and hide the primary payload/configuration from static analysis. |
| T1027 | Obfuscated Files or Information | The use of "junk code" and "broken control flow" specifically targets disassemblers to hinder manual and automated reverse engineering. |
| T1027 | Obfuscated Files or Information | High-entropy strings and "garbage" data indicate the use of packing/encryption to conceal the true functionality of the binary's string table. |

### Analyst Notes:
*   **Tactic:** Defense Evasion (TA0006).
*   **Contextual Insight:** While all behaviors map to **T1027**, they represent three different layers of obfuscation: 1) **Cryptographic Obfuscation** (SM4), 2) **Structural Obfuscation** (Junk code/Broken flow), and 3) **Packing** (Garbage strings).
*   **Indicator of Sophistication:** The specific choice of the **SM4 algorithm** is a high-confidence indicator often associated with actors targeting infrastructure or using specialized proprietary tools to evade standard signature-based detection.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, the following Indicators of Compromise (IOCs) have been extracted:

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Encryption Algorithms:** `SM4_DEC` (specifically functions: `DecryptCbc`, `DecryptBlob`, `DeriveKey`, `ExpandKey`). This indicates the use of the SM4 block cipher for payload decryption.
*   **Ant-Analysis Markers:** "bad instruction" warnings and `halt_baddata()` calls, indicating the presence of junk code/opaque predicates intended to break disassemblers.
*   **Symbol Mangling:** Use of non-standard, mangled function names (e.g., `method.A.cfd1396...`) characteristic of professional packers or protectors.

***

**Analyst Note:** The lack of network-based IOCs (IPs/URLs) and file-system IOCs is consistent with the behavioral analysis provided. This sample appears to be a **Stage 1 Loader**; the malicious infrastructure and payloads are likely encrypted within the binary and only decrypted in memory during execution, meaning most "hard" IOCs would not be visible in a static string analysis of this specific component.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Cryptographic Implementation:** The use of the SM4 block cipher (specifically `DecryptCbc`, `ExpandKey`, and `DeriveKey`) indicates a sophisticated multi-stage decryption process used to hide payloads or configuration data from static analysis.
*   **Anti-Analysis & Obfuscation:** The presence of "bad instruction" warnings, junk code, and broken control flow confirms the use of professional-grade protectors intended to thwart automated sandboxes and manual disassembly (e.g., IDA Pro/Ghidra).
*   **Staged Execution Behavior:** The lack of hard indicators (IPs, URLs) combined with high-entropy "garbage" strings is characteristic of a Stage 1 loader; its primary role is to decrypt and execute the next stage of malware in memory rather than performing the final malicious action itself.
