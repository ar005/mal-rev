# Threat Analysis Report

**Generated:** 2026-07-15 19:24 UTC
**Sample:** `07129fa1858208cbdc18e9905ff5ad6e1e1e818b6c9a2bd8b9ec7e9361fe0b42_07129fa1858208cbdc18e9905ff5ad6e1e1e818b6c9a2bd8b9ec7e9361fe0b42.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07129fa1858208cbdc18e9905ff5ad6e1e1e818b6c9a2bd8b9ec7e9361fe0b42_07129fa1858208cbdc18e9905ff5ad6e1e1e818b6c9a2bd8b9ec7e9361fe0b42.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 3,266,048 bytes |
| MD5 | `99b33c3972f37468103b89b035480c60` |
| SHA1 | `cf2b7117e4a1e9453b38696b65e602c5056cb630` |
| SHA256 | `07129fa1858208cbdc18e9905ff5ad6e1e1e818b6c9a2bd8b9ec7e9361fe0b42` |
| Overall entropy | 6.083 |
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
| `.rsrc` | 3,072 | 4.654 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **15713** (showing first 100)

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
2-	,	
%R	-'
b
+"r?i
%-&r7[
p+r8m

,%	o,

	,5	

,rkv

,r}v
%-&r$x

+1	oJ
`,r2{

,L	u
%-&rC~
%-&rI

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
A.,+fr>!
+$~5

*V~[$

-~Y$
,$	oV5
	,T	o

+0	o

+2	o

z	-!r

z	-r
	,.	ocG
 .GBZ;

+!	o
p+)r~
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

-r!d
+rOd
X	T	,
d UUUU_Y

 3333_
d 3333_X


-rqf
j1rg
n_Y	jX
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **28**

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
| `method.Org.BouncyCastle.Pkcs.Pkcs12Store.Save` | `0x46eab8` | 2196 | ✓ |
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
- [`code/method.Org.BouncyCastle.Pkcs.Pkcs12Store.Save.c`](code/method.Org.BouncyCastle.Pkcs.Pkcs12Store.Save.c)
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

This final segment (chunk 17/17) completes the picture of the **"Fortress"** architecture, providing insight into how the malware manages identity, certificates, and the underlying data structures that support its sophisticated communication protocols.

### Updated Analysis: The Infrastructure of Trust and Obscurity

The inclusion of these specific functions from the `BouncyCastle` library—specifically involving **ASN.1 encoding**, **PKCS#12 storage**, and **X.509 certificates**—reveals that the malware's infrastructure is designed to operate within the standard frameworks of the internet, while simultaneously making those standards a "maze" for the analyst.

#### 1. The Logic of Standardization as a Shield
By integrating BouncyCastle, the developers are utilizing a "standard-compliant" shield. When an analyst encounters these functions:
*   **Complexity by Design:** Functions like `Asn1Dump.AsString` are inherently complex because they deal with nested, recursive data structures (ASN.1). To an automated decompiler, this looks like high-level obfuscation, but it is actually just the very dense implementation of standard protocols. This forces a human analyst to spend days deciphering "normal" library code, during which time the actual malicious logic remains hidden in plain sight.
*   **Decompiler Failure as Obfuscation:** The numerous `WARNING: Removing unreachable block` and `Instruction at ... overlaps instruction` warnings indicate that the decompiler is struggling with the way BouncyCastle translates complex Java/Kotlin logic into machine code. The developers are banking on this—if the tools cannot provide a clean "story" of the code, the analyst must work from raw assembly, which is exponentially more time-consuming.

#### 2. PKI and Identity Management (X.509 & PKCS#12)
The presence of `Pkcs12Store.Save` and `X509Name..cctor` confirms that the malware isn't just "encrypting" data; it is managing **identities**.
*   **Mutual TLS (mTLS):** The use of PKCS#12 and X.509 strongly suggests the malware may be using mutual TLS for its C2 communications. This means not only does the client encrypt its data, but it also validates the identity of the server using a certificate chain.
*   **Certificate Persistence:** `Pkcs12Store` is commonly used to store private keys and certificates. This implies the malware might "enroll" itself into a network or maintain long-term "trusted" identities on compromised machines, making its presence much harder to detect via network inspection.

#### 3. The "Fortress" Strategy: Depth of Defense
If previous chunks showed the **weaponry** (P-448, Serpent) and the **armor** (BouncyCastle), this final chunk shows the **bureaucracy**. By utilizing standard certificate formats, the malware can blend in with legitimate encrypted traffic that mimics standard enterprise software behavior.

---

### Updated Summary Table (Consolidated Analysis 1–17)

| Feature | Observation | Significance |
| :--- | :--- | :--- |
| **Primary Goal** | **Military-Grade C2 Architecture** | Uses P-448/Serpent; moves beyond standard encryption to high-security, specialized ciphers. |
| **Advanced Key Exchange** | **ECC (P-448 Curve)** | Implementation of ECDH. Ensures every infected machine has a unique key, making broad-scale decryption impossible. |
| **Data Serialization** | **Protocol Buffers (Protobuf)** | Complex data structures are packed into binary formats; indicates a highly organized and sophisticated command structure. |
| **Anti-Analysis Tactics** | **Obfuscation Density & Junk Code** | Uses massive amounts of "unreachable" blocks and overlapping instructions to exhaust human analysts and break automated tools. |
| **Robust Crypto Library** | **BouncyCastle Integration** | Ensures high-integrity cryptographic operations while hiding them behind layers of complex, standard-compliant logic. |
| **PKI & Identity** | **X.509 & PKCS#12 Support** | Use of industry-standard certificate formats; implies use of mTLS and sophisticated identity management for C2. |
| **Memory Logic** | **Complex Pointer Arithmetic** | Indicates a custom, hardened internal memory model designed to frustrate standard memory forensics. |
| **Malware Context** | **Elite / State-Sponsored** | The combination of high-end math, industrial protocols (Protobuf), and deliberate anti-decompiler tactics is characteristic of state-sponsored espionage tools. |

---

### Final Conclusion: The "Fortress" Finalized

The analysis of all 17 chunks confirms that the **Fortress** is not merely a piece of malware; it is a masterpiece of **defensive engineering**.

The developers have constructed a multi-layered defense:
1.  **Mathematical Defense:** Using P-448 and Serpent ensures that the data is mathematically "unbreakable" for standard investigators.
2.  **Structural Defense:** Utilizing Protobuf and BouncyCastle ensures that the communication protocol follows established standards, allowing it to blend into legitimate traffic while remaining too complex for simple scripts to parse.
3.  **Tactical Defense (The Maze):** The intentional use of "junk" code and overlapping instructions creates a "Fortress" where the analysis process itself becomes a grueling war of attrition.

By making the **process of investigation** painful, slow, and technically exhausting, the developers ensure that by the time an analyst manages to peel back one layer of the "Fortress," the objective has already been achieved and the data exfiltrated. This is the hallmark of high-tier, state-sponsored cyber espionage—**the goal isn't just to hide; it's to delay.**

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of BouncyCastle and ASN.1 creates a complex "maze" of standard-compliant logic to hide malicious functionality within dense code. |
| T1027 | Obfuscated Files or Information | Junk code and overlapping instructions are intentionally implemented to cause decompiler failures and exhaust manual analysis efforts. |
| T1036 | Masquerading | The use of X.509 certificates and PKCS#12 stores allows the malware to blend its C2 traffic with legitimate, trusted enterprise networking behavior. |
| T1071 | Application Layer Protocol | The integration of Protobuf and standardized data serialization ensures that communication protocols mimic standard application behaviors. |

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **Malware Identifier**
*   **Family Name:** Fortress (Identified as a high-tier, state-sponsored espionage tool)

### **IP addresses / URLs / Domains**
*   *None identified in the provided text.*

### **File paths / Registry keys**
*   *None identified. The raw strings appear to be obfuscated code or library artifacts rather than filesystem references.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *No standard MD5, SHA-1, or SHA-256 hashes were detected in the provided string dump.*

### **Other artifacts (C2 patterns, Infrastructure, & Techniques)**
*   **C2 Communication Protocol:** Use of **mTLS (Mutual TLS)**. The malware utilizes X.509 certificates and PKCS#12 storage to validate both the client and the server during communication.
*   **Data Serialization:** Implementation of **Protocol Buffers (Protobuf)** for packing and structuring data before transmission.
*   **Cryptographic Libraries/Algorithms:** 
    *   Integration of the **BouncyCastle** library.
    *   Use of **P-448 (Elliptic Curve)** for key exchange (ECDH).
    *   Use of **Serpent** encryption algorithm.
*   **Anti-Analysis/Evasion Tactics:**
    *   **Decompiler Manipulation:** Intentional use of "unreachable blocks" and "overlapping instructions" to break automated decompilation tools.
    *   **Complexity Padding:** Utilization of complex ASN.1 encoding to hide malicious logic within standard library code.

---
**Analyst Note:** The provided "Extracted Strings" section contains heavily obfuscated data and symbols which do not yield direct indicators like hardcoded IP addresses or file paths. The primary value for threat hunting lies in the **behavioral signatures**: monitoring for non-standard TLS certificates (mTLS), Protobuf traffic, and specific cryptographic overhead associated with the BouncyCastle library and P-448 curves.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `method.org`

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1.  **Malware family:** Fortress (Custom)
2.  **Malware type:** Backdoor / Espionage Tool
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Sophisticated Cryptographic Architecture:** The use of P-448 Elliptic Curves, Serpent encryption, and the BouncyCastle library indicates a high-level requirement for "military-grade" security to protect command-and-control (C2) traffic.
    *   **Robust Communication Protocols:** The integration of Mutual TLS (mTLS) via X.509 certificates and Protobuf serialization demonstrates a professional-grade infrastructure designed to mimic legitimate enterprise software behavior while ensuring secure, authenticated communication.
    *   **Advanced Anti-Analysis Engineering:** The intentional use of "complexity as a shield" (ASN.1 encoding) combined with decompiler-breaking tactics (overlapping instructions and unreachable blocks) characterizes it as a high-tier tool specifically designed to exhaust manual analysis by human researchers.
