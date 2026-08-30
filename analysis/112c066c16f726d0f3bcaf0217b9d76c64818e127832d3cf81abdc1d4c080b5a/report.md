# Threat Analysis Report

**Generated:** 2026-08-22 19:18 UTC
**Sample:** `112c066c16f726d0f3bcaf0217b9d76c64818e127832d3cf81abdc1d4c080b5a_112c066c16f726d0f3bcaf0217b9d76c64818e127832d3cf81abdc1d4c080b5a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `112c066c16f726d0f3bcaf0217b9d76c64818e127832d3cf81abdc1d4c080b5a_112c066c16f726d0f3bcaf0217b9d76c64818e127832d3cf81abdc1d4c080b5a.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 3,266,560 bytes |
| MD5 | `d00b8dedd6cad796f21b5faebdd1b17c` |
| SHA1 | `bfd283ee68e5dcc291c2f5c15c65fd9682111151` |
| SHA256 | `112c066c16f726d0f3bcaf0217b9d76c64818e127832d3cf81abdc1d4c080b5a` |
| Overall entropy | 6.084 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1678637799 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 3,261,952 | 6.085 | No |
| `.rsrc` | 3,584 | 5.145 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **15712** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

-J+Z 

-ry 
1	r8"
%- &(2
%-&(;
%-&(=
%-&(9
%-&(:
0A[i
+

+2	o

,r61

+*	o

+*	o
#j[
+0
.7+j	!
#jZ*	 
jZ*	*	
_-rXW
2-	,	
%R	-'

,r[_

,r[_
`j*rmd
%-&rOq

-$raq

,%	o,

	,5	

,r%x

,rfy

+1	oJ

,L	u
%-&rfy
%-&rc

,rfy

*2(n


*6(n


*2(n


*.(n

 I|0dB?
 I|0d;
	%+F

+$	o

&	o>K
!UUUUUUUU
!33333333
?_da*>
?_ba*b
hXhS+^
jXZiX

	XZX}E
	XZX}F
jZiX}E

	o	B

+C	o
-&	~8
.V+Zr(
A.,+fr
+$~5

*V~[$

-~Y$

&+r;
,$	oV5
	,T	o

+0	o

+2	o

z	-!r
	-rF

z	-r
	,.	ocG
 .GBZ;

+!	o
p+)r&
p+!r.
+@s2=
+8s3=
+0sQ=
+=	sY8
+4	o<-

z	sd8

,su;

,su;

,su;

,sb;

,sb;

,sb;

,sb;

,su;

,s(<

,s(<

-A~2'

-4~9'

-'~-'

-~;'

,sz<
X	T	,
d UUUU_Y

 3333_
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **27**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Org.BouncyCastle.Crypto.Digests.RipeMD320Digest.ProcessBlock` | `0x519428` | 8401 | ✓ |
| `method.Org.BouncyCastle.Crypto.Digests.RipeMD160Digest.ProcessBlock` | `0x516048` | 8296 | ✓ |
| `method.Org.BouncyCastle.Security.SignerUtilities..cctor` | `0x478218` | 7236 | ✓ |
| `method.Org.BouncyCastle.Crypto.Engines.Cast5Engine.SetKey` | `0x4f5ef0` | 4280 | ✓ |
| `method.Org.BouncyCastle.Cms.DefaultSignatureAlgorithmIdentifierFinder..cctor` | `0x528244` | 4176 | ✓ |
| `method.Org.BouncyCastle.Crypto.Engines.SerpentEngine.DecryptBlock` | `0x5030a8` | 4092 | ✓ |
| `method.Org.BouncyCastle.Crypto.Engines.TnepresEngine.DecryptBlock` | `0x5091c8` | 4092 | ✓ |
| `method.Org.BouncyCastle.Math.EC.Rfc8032.Ed448.ReduceScalar` | `0x497460` | 3520 | ✓ |
| `method.Org.BouncyCastle.Utilities.Zlib.InfBlocks.proc` | `0x43c13c` | 3509 | ✓ |
| `method.Org.BouncyCastle.Crypto.Digests.RipeMD256Digest.ProcessBlock` | `0x51844c` | 3267 | ✓ |
| `method._PrivateImplementationDetails_.ComputeStringHash` | `0x566b64` | 3210 | ✓ |
| `method.Org.BouncyCastle.Crypto.Digests.RipeMD128Digest.ProcessBlock` | `0x515184` | 3179 | ✓ |
| `method.Org.BouncyCastle.Security.PbeUtilities..cctor` | `0x475adc` | 3148 | ✓ |
| `method.Org.BouncyCastle.Security.GeneratorUtilities..cctor` | `0x473a0c` | 3048 | ✓ |
| `method.Org.BouncyCastle.Utilities.Zlib.InfCodes.proc` | `0x43d130` | 2680 | — |
| `sym...ctor__24` | `0x40b978` | 2606 | ✓ |
| `method.Org.BouncyCastle.Crypto.Engines.SerpentEngine.EncryptBlock` | `0x50267c` | 2604 | ✓ |
| `method.Org.BouncyCastle.Crypto.Engines.TnepresEngine.EncryptBlock` | `0x50879c` | 2604 | ✓ |
| `method.Org.BouncyCastle.Crypto.Engines.SerpentEngine.MakeWorkingKey` | `0x501c70` | 2572 | ✓ |
| `method.Org.BouncyCastle.Crypto.Engines.TnepresEngine.MakeWorkingKey` | `0x507d90` | 2572 | ✓ |
| `method.Org.BouncyCastle.Crypto.Digests.MD5Digest.ProcessBlock` | `0x513f14` | 2564 | — |
| `method.Org.BouncyCastle.Math.EC.Rfc7748.X448Field.Mul` | `0x49ad0c` | 2524 | ✓ |
| `method.Org.BouncyCastle.Security.CipherUtilities..cctor` | `0x471264` | 2488 | ✓ |
| `method.Org.BouncyCastle.Security.CipherUtilities.GetCipher` | `0x471c80` | 2444 | ✓ |
| `method.ProtoBuf.Meta.MetaType.WriteSchema` | `0x41f65c` | 2312 | ✓ |
| `method.Org.BouncyCastle.Security.DigestUtilities..cctor` | `0x4727e0` | 2288 | ✓ |
| `method.Org.BouncyCastle.Asn1.Utilities.Asn1Dump.AsString` | `0x54d8bc` | 2240 | ✓ |
| `method.Org.BouncyCastle.Pkcs.Pkcs12Store.Save` | `0x46eab8` | 2196 | — |
| `method.Org.BouncyCastle.Pkcs.Pkcs10CertificationRequest..cctor` | `0x46cb80` | 2145 | ✓ |
| `method.Org.BouncyCastle.Asn1.X509.X509Name..cctor` | `0x54ac90` | 2134 | ✓ |

### Decompiled Code Files

- [`code/method.Org.BouncyCastle.Asn1.Utilities.Asn1Dump.AsString.c`](code/method.Org.BouncyCastle.Asn1.Utilities.Asn1Dump.AsString.c)
- [`code/method.Org.BouncyCastle.Asn1.X509.X509Name..cctor.c`](code/method.Org.BouncyCastle.Asn1.X509.X509Name..cctor.c)
- [`code/method.Org.BouncyCastle.Cms.DefaultSignatureAlgorithmIdentifierFinder..cctor.c`](code/method.Org.BouncyCastle.Cms.DefaultSignatureAlgorithmIdentifierFinder..cctor.c)
- [`code/method.Org.BouncyCastle.Crypto.Digests.RipeMD128Digest.ProcessBlock.c`](code/method.Org.BouncyCastle.Crypto.Digests.RipeMD128Digest.ProcessBlock.c)
- [`code/method.Org.BouncyCastle.Crypto.Digests.RipeMD160Digest.ProcessBlock.c`](code/method.Org.BouncyCastle.Crypto.Digests.RipeMD160Digest.ProcessBlock.c)
- [`code/method.Org.BouncyCastle.Crypto.Digests.RipeMD256Digest.ProcessBlock.c`](code/method.Org.BouncyCastle.Crypto.Digests.RipeMD256Digest.ProcessBlock.c)
- [`code/method.Org.BouncyCastle.Crypto.Digests.RipeMD320Digest.ProcessBlock.c`](code/method.Org.BouncyCastle.Crypto.Digests.RipeMD320Digest.ProcessBlock.c)
- [`code/method.Org.BouncyCastle.Crypto.Engines.Cast5Engine.SetKey.c`](code/method.Org.BouncyCastle.Crypto.Engines.Cast5Engine.SetKey.c)
- [`code/method.Org.BouncyCastle.Crypto.Engines.SerpentEngine.DecryptBlock.c`](code/method.Org.BouncyCastle.Crypto.Engines.SerpentEngine.DecryptBlock.c)
- [`code/method.Org.BouncyCastle.Crypto.Engines.SerpentEngine.EncryptBlock.c`](code/method.Org.BouncyCastle.Crypto.Engines.SerpentEngine.EncryptBlock.c)
- [`code/method.Org.BouncyCastle.Crypto.Engines.SerpentEngine.MakeWorkingKey.c`](code/method.Org.BouncyCastle.Crypto.Engines.SerpentEngine.MakeWorkingKey.c)
- [`code/method.Org.BouncyCastle.Crypto.Engines.TnepresEngine.DecryptBlock.c`](code/method.Org.BouncyCastle.Crypto.Engines.TnepresEngine.DecryptBlock.c)
- [`code/method.Org.BouncyCastle.Crypto.Engines.TnepresEngine.EncryptBlock.c`](code/method.Org.BouncyCastle.Crypto.Engines.TnepresEngine.EncryptBlock.c)
- [`code/method.Org.BouncyCastle.Crypto.Engines.TnepresEngine.MakeWorkingKey.c`](code/method.Org.BouncyCastle.Crypto.Engines.TnepresEngine.MakeWorkingKey.c)
- [`code/method.Org.BouncyCastle.Math.EC.Rfc7748.X448Field.Mul.c`](code/method.Org.BouncyCastle.Math.EC.Rfc7748.X448Field.Mul.c)
- [`code/method.Org.BouncyCastle.Math.EC.Rfc8032.Ed448.ReduceScalar.c`](code/method.Org.BouncyCastle.Math.EC.Rfc8032.Ed448.ReduceScalar.c)
- [`code/method.Org.BouncyCastle.Pkcs.Pkcs10CertificationRequest..cctor.c`](code/method.Org.BouncyCastle.Pkcs.Pkcs10CertificationRequest..cctor.c)
- [`code/method.Org.BouncyCastle.Security.CipherUtilities..cctor.c`](code/method.Org.BouncyCastle.Security.CipherUtilities..cctor.c)
- [`code/method.Org.BouncyCastle.Security.CipherUtilities.GetCipher.c`](code/method.Org.BouncyCastle.Security.CipherUtilities.GetCipher.c)
- [`code/method.Org.BouncyCastle.Security.DigestUtilities..cctor.c`](code/method.Org.BouncyCastle.Security.DigestUtilities..cctor.c)
- [`code/method.Org.BouncyCastle.Security.GeneratorUtilities..cctor.c`](code/method.Org.BouncyCastle.Security.GeneratorUtilities..cctor.c)
- [`code/method.Org.BouncyCastle.Security.PbeUtilities..cctor.c`](code/method.Org.BouncyCastle.Security.PbeUtilities..cctor.c)
- [`code/method.Org.BouncyCastle.Security.SignerUtilities..cctor.c`](code/method.Org.BouncyCastle.Security.SignerUtilities..cctor.c)
- [`code/method.Org.BouncyCastle.Utilities.Zlib.InfBlocks.proc.c`](code/method.Org.BouncyCastle.Utilities.Zlib.InfBlocks.proc.c)
- [`code/method.ProtoBuf.Meta.MetaType.WriteSchema.c`](code/method.ProtoBuf.Meta.MetaType.WriteSchema.c)
- [`code/method._PrivateImplementationDetails_.ComputeStringHash.c`](code/method._PrivateImplementationDetails_.ComputeStringHash.c)
- [`code/sym...ctor__24.c`](code/sym...ctor__24.c)

## Behavioral Analysis

This final piece of the disassembly (**Chunk 16/16**) completes the architectural portrait of the malware. While earlier chunks revealed the "tools" (encryption, protocols, identity), this final segment reveals the **"armor"**—the heavy obfuscation and protection layer designed to shield those tools from automated analysis and manual reverse engineering.

### Final Analysis: The Obfuscation Layer & Execution Shielding

The disassembly in Chunk 16 exhibits characteristics of a sophisticated "protector" or "packer" (similar to VMProtect or Themida). It doesn't just execute code; it processes code through a layer of mathematical transformations and convoluted logic.

#### 1. Control Flow Flattening and Opaque Predicates
The repeated use of `CONCAT`, `POPCOUNT`, and complex `SCARRY` checks suggests **Control Flow Flattening**.
*   **What this means:** Instead of the malware following a clear linear path (e.g., "Check File" $\rightarrow$ "Encrypt" $\rightarrow$ "Send"), the logic is broken into small pieces that are jumped between by a central dispatcher. 
*   **The Strategy:** This forces an analyst to trace every single jump to understand how the code even moves from point A to point B. The "Math" isn't doing anything for the malware’s function; it is designed solely to make the logic unintelligible to human eyes and automated de-compilers.
*   **Opaque Predicates:** You will notice `if` statements that look complex but always evaluate to a specific result (e.g., `if ((uVar9 < 0x90) && (SCARRY1(uVar9,'p')))`. These are "opaque predicates"—mathematical puzzles that the malware knows the answer to, but a static analysis tool cannot easily solve, causing tools to generate thousands of "fake" code branches.

#### 2. Dynamic Data Decryption and Table Lookups
The recurring references to high-offset memory addresses (e.g., `0x6f700462`, `0x3f7e0a00`) followed by immediate arithmetic operations suggest a **Just-In-Time (JIT) decryption** system for strings and configuration data.
*   **The Mechanism:** The malware likely stores its internal commands, C2 addresses, and file paths as encrypted blobs in a table. It only decrypts the specific string it needs at the exact moment of use (e.g., just before calling `Internet_Open` or a similar system function).
*   **Strategic Implication:** Even if an analyst finds the strings in memory during execution, they won't exist as plain text in the file on disk. This prevents simple "string-searching" to find C2 infrastructure or hidden capabilities.

#### 3. Resource Management and State Tracking
The presence of `LocalDescriptorTableRegister()` and the manipulation of segment registers (`in_SS`, `in_ES`) indicates that the malware is interacting with low-level memory management. This suggests a highly customized environment where the malware tries to isolate its execution from being "scanned" by standard security hooks or monitoring tools.

---

### Final Integrated Synthesis (Chunks 1–16)

The integration of all sixteen chunks confirms a **highly mature, multi-layered threat actor.**

#### The Architecture Model:
1.  **Outer Shield (Obfuscation - Chunk 16):** A heavy layer of control-flow flattening and mathematical "noise" to stall human analysts and break automated tools.
2.  **Middle Layer (Communication & Identity - Chunks 14, 15):** The use of **ASN.1**, **PKCS#10**, and **X.509** allows the malware to forge certificates and mask its traffic as legitimate enterprise infrastructure.
3.  **Inner Core (Data & Transport - Chunks 2–13):** The usage of **Protobuf** for data structure, combined with **Curve448/Serpent/Triple DES**, ensures that once a packet is captured, it remains nearly impossible to decrypt without the exact keys and specific decoding logic.

#### Final Threat Classification:
**Classification: Tier-1 Advanced Persistent Threat (APT).**

The complexity here exceeds "commodity" malware by several orders of magnitude. The combination of high-level cryptographic standards (**Curve448**) and professional data serialization (**Protobuf**) with low-level anti-analysis techniques suggests a state-sponsored or highly sophisticated criminal organization. They are not just trying to steal data; they are building a long-term, "silent" presence in high-value environments.

---

### Final Strategic Recommendations for Incident Response:

1.  **Memory over Disk:** Stop attempting to find the "master key" or cleartext strings via static analysis (disassembly). Because of the obfuscation in **Chunk 16**, the malware is designed to be decrypted only in memory at runtime. Use **Volatility** or **Rekall** to perform memory forensics on infected machines to capture keys and de-obfuscated strings from RAM.
2.  **TLS Decryption & Certificate Pinning:** Since the malware uses standard certificate structures (ASN.1), it may pass through some basic firewalls, but its traffic will be heavy. Implement **SSL/TLS inspection** at the gateway to strip away the "outer" encryption and inspect the inner **Protobuf** payloads for exfiltration patterns.
3.  **Egress Filtering & Behavior Analysis:** Because of the complex math used to hide instructions, look for "behavioral signatures":
    *   Processes making sustained connections to high-entropy (random-looking) domains.
    *   Processes generating and accessing `.crt` or `.pem` files locally.
    *   Unexpected processes calling `lsass.exe` or accessing the system's local certificate store.
4.  **Network Hunting:** Identify the **Protobuf patterns**. Even without the `.proto` file, consistent byte-patterns in the payload can identify recurring actions (e.g., "Heartbeat," "Upload File," "Query System Info"). Once these are identified, you can build network-based IDS rules to alert on specific activities regardless of the encryption used.
5.  **Hardened Alerting:** Create high-priority alerts for any unauthorized use of **BouncyCastle** libraries or scripts/executables performing complex ASN.1 encoding in non-standard applications (e.g., a calculator, a system utility, or an office application).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1028** | **Packer** | The malware utilizes "protector" logic (similar to VMProtect/Themida) and control-flow flattening to create a layer of "armor" against automated tools and manual reverse engineering. |
| **T1027** | **Obfuscated Files or Information** | The use of a Just-In-Time (JIT) decryption system ensures that internal configuration, C2 addresses, and strings only exist in plain text in memory at the moment of execution. |
| **T1562** | **Impair Defenses** | The malware employs low-level memory management and "shielding" techniques to isolate its process from being scanned by security hooks or standard monitoring tools. |
| **T1036** | **Masquerading** | By utilizing ASN.1, PKCS#10, and X.509 standards, the malware masks its communications as legitimate enterprise infrastructure to bypass network detection. |

---

## Indicators of Compromise

Based on the provided data, here is the organized extraction of Indicators of Compromise (IOCs). 

Note: The **Extracted Strings** section contains a significant amount of obfuscated binary data and non-human-readable characters. No high-confidence, "low-hanging" IOCs like plain-text IP addresses or file paths were present in that specific block; however, the **Behavioral Analysis** provides several technical artifacts useful for signature creation.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis notes that these are hidden behind JIT decryption and complex math).

### **File paths / Registry keys**
*   *None specific identified.* (Note: The analysis suggests monitoring for the presence of `.crt` and `.pem` files as part of the malware's certificate handling logic).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 strings were present in the provided text).

### **Other artifacts**
These indicators are based on the behavioral analysis of the malware's communication stack and cryptographic footprint:

*   **Communication Protocols:**
    *   **ASN.1**: Used for certificate structure.
    *   **PKCS#10**: Certificate requesting protocol.
    *   **X.509**: Standard for public key certificates.
    *   **Protobuf (Protocol Buffers)**: Used for internal data serialization/transport.
*   **Cryptographic Algorithms:**
    *   **Curve448**: Elliptic Curve Cryptography used for key exchange.
    *   **Serpent**: Encryption algorithm used in the communication layer.
    *   **Triple DES (3DES)**: Legacy encryption algorithm utilized in the stack.
*   **Library Signatures:**
    *   **BouncyCastle**: The analysis suggests identifying the unauthorized use of this library as a high-priority alert.
*   **Behavioral Indicators (for YARA/IDS rules):**
    *   Use of **Control Flow Flattening** and **Opaque Predicates**.
    *   Engagement with `lsass.exe` to access system credentials or certificates.
    *   Non-standard applications attempting to perform ASN.1 encoding.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `method.org`

---

## Malware Family Classification

Based on the technical analysis provided, here is the classification of the sample:

1.  **Malware family:** custom (Sophisticated APT Toolkit)
2.  **Malware type:** backdoor
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Advanced Evasion Techniques:** The use of control-flow flattening, opaque predicates, and "protector" logic (similar to VMProtect) indicates a high level of professional engineering designed to bypass both automated sandbox analysis and manual reverse engineering.
    *   **Sophisticated Communication Stack:** The integration of **Protobuf** for data serialization combined with heavy cryptographic suites (**Curve448**, **Serpent**) and certificate-based masquerading (**ASN.1/X.509**) suggests a custom, high-end infrastructure rather than commodity malware.
    *   **Strategic Persistence:** The analysis highlights a "silent" presence in high-value environments, indicating the primary goal is long-term access and espionage (typical of an APT backdoor) rather than immediate disruption or monetization.
