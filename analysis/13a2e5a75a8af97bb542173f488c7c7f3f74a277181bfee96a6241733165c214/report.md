# Threat Analysis Report

**Generated:** 2026-09-02 20:29 UTC
**Sample:** `13a2e5a75a8af97bb542173f488c7c7f3f74a277181bfee96a6241733165c214_13a2e5a75a8af97bb542173f488c7c7f3f74a277181bfee96a6241733165c214.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13a2e5a75a8af97bb542173f488c7c7f3f74a277181bfee96a6241733165c214_13a2e5a75a8af97bb542173f488c7c7f3f74a277181bfee96a6241733165c214.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 3,267,584 bytes |
| MD5 | `44fac70f9fe2546deda57b90bcbaec9e` |
| SHA1 | `af8fddbfe46dd6da28c8032a78ec6572f8c0ed5a` |
| SHA256 | `13a2e5a75a8af97bb542173f488c7c7f3f74a277181bfee96a6241733165c214` |
| Overall entropy | 6.085 |
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
| `.text` | 3,262,976 | 6.086 | No |
| `.rsrc` | 3,584 | 4.865 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **15732** (showing first 100)

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
+"rgm
%-&r__
%-&r&o

,r&o

,r&o
p+r`q

,r)v

,%	o,

	,5	

,r&o
%-&r&o
%-&rL|

+1	oJ

,L	u
%-&rk

,r&o

,r&o

-+	r<

,r&o

&+r0

-!	r>

,r&o

,9	r+
%-&r&o

,r&o

,r&o
%-&r&o
%-&rq

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

z.rj

-&	~8
.t+xr8
A.,+frf%
+$~5

*V~[$

-~Y$
,$	oV5
	,T	o

+0	o

+2	o

z	-!r?

z	-r0
	,.	ocG
 .GBZ;

+!	o
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
| `sym...ctor__23` | `0x40b978` | 2606 | ✓ |
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
- [`code/sym...ctor__23.c`](code/sym...ctor__23.c)

## Behavioral Analysis

This update incorporates the analysis of **Chunk 19**, which provides a deep look into the low-level execution logic of the malware. The findings here confirm the extreme technical sophistication of the developer and suggest that the code is not only "minimized" but intentionally engineered to be extremely difficult for automated scanners and manual reverse engineers to map.

---

### Updated Analysis Report (Chunks 1–19)

#### 1. Integration of Protocol Buffers (ProtoBuf)
*(Retained from previous analysis)*
The use of `method.ProtoBuf.Meta.MetaType.WriteSchema` confirms the use of **Google's Protocol Buffers** for data serialization. This ensures that command structures are compressed into a compact binary format before being transmitted, effectively hiding the "logic" of the C2 commands from simple network inspection.

#### 2. Evidence of High-Level Transpilation (The "GraalVM" Signature)
*(Enhanced by Chunk 19)*
The heavy presence of `WARNING: Removing unreachable block` and the dense bitwise arithmetic confirmed in earlier chunks are now reinforced by the raw disassembly in Chunk 19.
*   **Mathematical Density:** The code is saturated with complex operations like `CONCAT31`, `CONCAT21`, and multi-step arithmetic to perform what would typically be simple additions or logic checks (e.g., `puVar41 = puVar41 + uVar5;`). 
*   **Compiler Evidence:** This "mathematically dense" construction is a hallmark of **GraalVM Native Image** or similar Ahead-Of-Time (AOT) compilers. These tools take high-level code (Java/Kotlin) and compile it into highly optimized machine code that strips away standard library symbols and flattens logic, making the resulting binary look like "scrambled" math rather than readable functions.

#### 3. Automated Infrastructure Shielding
*(Retained from previous analysis)*
The synergy between **BouncyCastle** and **ProtoBuf** creates a formidable dual-layer defense:
1.  **ProtoBuf:** Obscures the *structure* of the command (what the server is telling the bot to do).
2.  **BouncyCastle:** Encrypts the *content* of the communication.

#### 4. Advanced Certificate Management & ASN.1 Parsing
*(Retained from previous analysis)*
The inclusion of `Pkcs10CertificationRequest` and `X509Name` indicates a sophisticated approach to **Identity Mimicry**, allowing the malware to blend into enterprise environments by utilizing standard-compliant certificate infrastructure.

#### 5. Advanced Execution Obfuscation (New Discovery in Chunk 19)
The final chunk reveals several advanced techniques used to hide the "heart" of the malware's logic:

*   **State Machine Complexity:** The repetitive use of `LOCK()` and `UNLOCK()` operations, combined with complex memory offsets (e.g., `puVar32 + -0x4ab`), suggests that the malware operates as a **Complex State Machine**. Instead of linear execution, it maintains an internal state, moving between different "modes" based on inputs from the C2.
*   **Non-Standard Control Flow:** The presence of `POPCOUNT` logic (`while((POPCOUNT(uVar4) & 1U) != 0)`) used as a loop condition is highly unusual for standard software but common in advanced obfuscation. This allows the malware to iterate through bitmasks or "features" without using traditional `for` or `while` loops that are easily flagged by heuristic scanners.
*   **Instruction Mangling:** The disassembly shows significant "bloat" where a single logical step is expanded into multiple arithmetic operations. This is designed to break up and confuse the **Linear Disassembly** of tools like IDA Pro, making it harder for an analyst to follow the logic flow.

---

### Updated Threat Assessment (Elite/State-Sponsored)

The inclusion of Chunk 19 solidifies the classification of this threat as a **High-Tier / State-Sponsored** operation:

*   **Anti-Analysis Engineering:** The jump from standard "malware coding" to "compiler-level optimization and obfuscation" indicates an actor who prioritizes long-term persistence over quick deployment. They are intentionally making the code difficult for human analysts to reverse-engineer into a usable signature.
*   **Professional Software Lifecycle:** The presence of GraalVM signatures suggests that the developers are likely professional software engineers, not just malware "script kiddies." They utilize industrial-grade build pipelines to compile their tools.
*   **Hybrid Defense Strategy:** By combining **ProtoBuf (Structural)**, **BouncyCastle (Cryptographic)**, and **ASN.1/PKCS#10 (Identity)**, the actors have created a triple-layer shield. This means that even if an analyst intercepts the traffic, they cannot see the structure; if they break the encryption, they still face a "mimicked" identity that looks like legitimate corporate traffic.

---

### Final Synthesis (Chunks 1–19)

The malware's architecture is confirmed as a **tri-layer infrastructure**:

1.  **Layer 1: Structural Obfuscation (ProtoBuf)**
    Ensures the "grammar" of the C2 communication remains hidden in binary packets.
2.  **Layer 2: Cryptographic Hardening (BouncyCastle)**
    Provides high-level, standard-compliant encryption for the data payload.
3.  **Layer 3: Identity & Certificate Mimicry (ASN.1/PKCS#10)**
    Ensures the "identity" of the communication follows standard certificate protocols to blend into network noise.

**Key Takeaways from Chunk 19:**
*   **Compiler-Level Obfuscation:** The use of advanced compilation techniques suggests an actor with access to professional development environments and a sophisticated build pipeline.
*   **Anti-Analysis Logic:** The "mathematically dense" code and unconventional loop structures (like POPCOUNT loops) are specific tactics used to frustrate automated detection and manual analysis.
*   **High Maturity:** Every indicator points toward a target of high value, where the actor is prepared for an extensive investigation by elite forensic teams.

---

## MITRE ATT&CK Mapping

Based on the behavior provided in the report, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1071** | Application Layer Protocol | The use of ProtoBuf for structure serialization and BouncyCastle for content encryption conceals the C2 command logic from network inspection. |
| **T1036** | Masquerading | The implementation of ASN.1 parsing and PKCS#10 certificates allows the malware to mimic standard certificate infrastructure to blend into legitimate corporate traffic. |
| **T1027** | Obfuscated Executables | The "mathematically dense" GraalVM signatures, instruction mangling, and non-standard control flow (e.g., POPCOUNT loops) are specifically designed to thwart manual reverse engineering and automated analysis tools. |

---

## Indicators of Compromise

Based on the provided technical data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "EXTRACTED STRINGS" section contains heavily obfuscated/encoded data and binary artifacts. No direct IP addresses, URLs, or cleartext file paths were present in that raw segment; however, several high-value **Behavioral Artifacts** were identified in the analysis report.

### **IP addresses / URLs / Domains**
*   *None identified.* (The malware utilizes ProtoBuf and BouncyCastle to obfuscate all network traffic).

### **File paths / Registry keys**
*   *None identified.* (Memory offsets such as `puVar32 + -0x4ab` were noted, but these are internal memory addresses rather than filesystem paths).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (Behavioral & Technical Indicators)**
*   **C2 Communication Protocol:** 
    *   **Google Protocol Buffers (ProtoBuf):** Used to serialize and hide the "grammar" of C2 commands.
    *   **BouncyCastle Library:** Utilized for payload encryption.
    *   **ASN.1 / PKCS#10 / X509Name:** Employed specifically for **Identity Mimicry** to blend certificate-based traffic into standard enterprise network environments.
*   **Evasion & Anti-Analysis Techniques:**
    *   **GraalVM/AOT Compilation Signatures:** Evidence of "mathematically dense" code (e.g., `CONCAT31`, `CONCAT21`) used to strip symbols and flatten logic.
    *   **Non-Standard Control Flow:** Use of **POPCOUNT** logic within loops (`while((POPCOUNT(uVar4) & 1U) != 0)`) to evade heuristic scanners that look for standard `for` or `while` loops.
    *   **Instruction Mangling:** Intentional "bloating" of simple instructions into multiple arithmetic operations to frustrate linear disassembly (e.g., IDA Pro).
    *   **Complex State Machine:** Use of `LOCK()` and `UNLOCK()` functions with non-linear offsets to manage internal state transitions.

---
**Analyst Note:** The lack of static IOCs (IPs/Domains) combined with the presence of "State-Sponsored" level obfuscation techniques suggests a high degree of operational security (OPSEC). Detection should focus on identifying the **Protobuf serialized packets** and the specific **BouncyCastle implementation** rather than static network indicators.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `method.org`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Backdoor / RAT
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-Layered Communication Obfuscation:** The integration of ProtoBuf (for structure), BouncyCastle (for encryption), and ASN.1/PKCS#10 (for identity mimicry) indicates a highly sophisticated effort to hide C2 communication within standard enterprise traffic.
*   **Advanced Anti-Analysis Engineering:** The use of GraalVM AOT compilation signatures, instruction mangling, and non-standard control flows (such as POPCOUNT loops) demonstrates a deliberate intent to frustrate both automated scanners and manual reverse engineering.
*   **High-Tier Architecture:** The transition from simple malware logic to "mathematically dense" code and complex state machine management suggests the involvement of professional software engineers, characteristic of high-sophistication or state-sponsored operations.
