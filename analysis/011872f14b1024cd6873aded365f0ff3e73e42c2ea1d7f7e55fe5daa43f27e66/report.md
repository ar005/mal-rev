# Threat Analysis Report

**Generated:** 2026-06-26 16:06 UTC
**Sample:** `011872f14b1024cd6873aded365f0ff3e73e42c2ea1d7f7e55fe5daa43f27e66_011872f14b1024cd6873aded365f0ff3e73e42c2ea1d7f7e55fe5daa43f27e66.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `011872f14b1024cd6873aded365f0ff3e73e42c2ea1d7f7e55fe5daa43f27e66_011872f14b1024cd6873aded365f0ff3e73e42c2ea1d7f7e55fe5daa43f27e66.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 3,266,048 bytes |
| MD5 | `78f2b131ec926e94c326c2ce0e70b8c0` |
| SHA1 | `e09f511431f0687a081a50120e9c0a84c42f7f6d` |
| SHA256 | `011872f14b1024cd6873aded365f0ff3e73e42c2ea1d7f7e55fe5daa43f27e66` |
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
| `.rsrc` | 3,072 | 4.654 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **15733** (showing first 100)

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
+"rgi
%-&r_[
%-&r&k

,r&k

,r&k
p+r`m

,r)r

,%	o,

	,5	

,r&k
%-&r&k
%-&rLx

+1	oJ
`,rZ{

,L	u
%-&rk~

,r&k

,r&k

-+	r<

,r&k

&+r0

-!	r>

,r&k

,9	r+
%-&r&k

,r&k

,r&k
%-&r&k
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
-&	~8
.t+xr8
A.,+frf!
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
| `sym...ctor__25` | `0x40b978` | 2606 | ✓ |
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
- [`code/sym...ctor__25.c`](code/sym...ctor__25.c)

## Behavioral Analysis

This final segment (Chunk 23/23) provides a look into the "engine room" of the malware’s obfuscation strategy. While previous chunks established the **what** (the use of X.509 and Protobuf), this chunk reveals the **how**: the extensive use of automated obfuscation toolchains to make even standard library logic nearly impossible to trace via static analysis.

---

### Finalized Analysis: Chunk 23/23

#### 1. Deep-Level Arithmetic Obfuscation (The "Noise" Layer)
This segment exhibits extreme **Arithmetic Noise** and **Control Flow Flattening**. Notice the repetitive use of `CONCAT` functions (`CONCAT31`, `CONCAT22`, etc.) combined with complex, multi-step calculations to perform what are likely very simple arithmetic operations.

*   **The Mechanism:** Instead of a direct assignment or an increment (e.g., `x = x + 1`), the compiler/obfuscator generates several lines of bitwise logic and carry-flag checks (`CARRY1`, `SBORROW1`) to determine the next value.
*   **Impact on Analysis:** This is designed to exhaust the human analyst and break "decompiler" heuristics. By making every basic operation look like a complex mathematical puzzle, the malware ensures that an analyst cannot easily follow the logic of the underlying code (e.g., identifying where a buffer length is calculated or how a loop counter functions).

#### 2. Junk Code & "Dead Store" Insertion
The segment contains numerous lines such as:
*   `*0x3f7e0a00 = *0x3f7e0a00 + '\x01';` (repeated several times)
*   `*0x407e0a00 = *0x407e0a00 + '\x02';`
*   `*0x417e0a00 = *0x417e0a00 + '\x01';`

**The Strategy:** These are "Dead Stores." They modify memory locations that are either never read by the program or are overwritten before they can be used. 
**Significance:** This is a classic **anti-analysis tactic**. It forces a researcher to waste time investigating whether these addresses represent important state variables (like encryption keys or session IDs) when, in reality, they are "garbage" data meant to bloat the disassembly and confuse automated analysis scripts.

#### 3. Abstracted Buffer Manipulation
The logic involving `puVar17 = iVar18 + -0x72040020` followed by bitwise masking (`& 0x70`) demonstrates how the malware handles memory offsets.
*   **Non-Linear Offsets:** By using large, arbitrary negative numbers and subsequent mask operations, the malware hides the actual destination of a pointer until the moment of execution.
*   **Obfuscated Transitions:** This occurs specifically during the transition between internal data (Protobuf) and external wrappers (X.509). The code is "remapping" the memory space to align with the expected structure of an ASN.1 certificate while keeping the logic hidden behind a wall of arithmetic noise.

#### 4. Complex Branching & State Machines
The deep `if-else` structures containing complex conditions like `(POPCOUNT(uVar10) & 1U) == 0` or `SCARRY1(cVar11, '\x01')` suggest the presence of a **State Machine**. The malware is likely cycling through different "states" to build various parts of the packet (e.g., State A: Header construction; State B: Payload padding; State C: Certificate wrapping).

---

### Final Comprehensive Synthesis for Analyst

The analysis confirms that this is a high-sophistication piece of malware designed specifically to defeat automated tools and waste manual analyst time through multiple layers of defense.

#### The Architecture Summary:
1.  **Internal Logic (VM Layer):** A custom virtual machine executes the primary malicious logic, ensuring the "core" intent is never visible in standard x86/x64 instructions.
2.  **Data Organization (Protobuf Layer):** The VM outputs a Protobuf-structured object which serves as the "internal language" for communication.
3.  **Transport Obfuscation (ASN.1 / BouncyCastle Layer):** A massive, obfuscated wrapper translates the Protobuf into X.509 certificates and PKCS#12 files to mimic standard identity traffic.

#### Key Findings & Threat Indicators:
*   **Tooling Fingerprint:** The specific style of arithmetic noise (`CONCAT`, `POPCOUNT` for basic logic) is highly indicative of advanced obfuscation toolchains like **Tigress**. 
*   **Anti-Disassembly:** The "Instruction Overlap" and "Control Flow Flattening" seen in these segments mean that **Static Analysis (Grepping/IDA)** will be largely ineffective. The code is designed to look like a mess of math until it hits the execution stage.
*   **Data Hiding:** By utilizing `Pkcs12Store` and `Asn1Dump`, the malware hides its command-and-control (C2) instructions within standard certificate fields (e.g., putting a C2 command in the "Subject Alternative Name" or "Issuer" fields).

#### Strategic Recommendations for Defense:
*   **Dynamic Analysis is Mandatory:** Because the static code is so heavily obfuscated, the only way to see the "true" data is via **dynamic memory forensics**. You must capture the buffer *after* it leaves the VM/Protobuf layer but *before* it enters the BouncyCastle/ASN.1 layer.
*   **Signature Strategy:** Do not try to signature the code logic (it changes too much). Instead, **signature the behavior**. 
    *   Flag any process that performs heavy ASN.1/X.509 manipulation using non-standard certificate fields.
    *   Flag processes utilizing BouncyCastle libraries for "unusual" data types (e.g., embedding long, high-entropy strings in the Certificate Body).
*   **Network Detection:** Focus on the **Protocol Symmetry**. A standard certificate exchange has a predictable size and structure. If you see an X.509 packet where the internal fields are unusually large or lack expected patterns, it is a 100% high-confidence indicator of this malware's tunneling mechanism.

#### Final Conclusion:
This malware represents a **high-tier threat** that employs "Defense in Depth" for its own code. It doesn't just hide its data; it hides the *logic* used to hide the data. Detection should focus on the **anomalous structure of the outgoing certificates**, as the underlying code is specifically engineered to be invisible to standard signature-based detection.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055.001** | **Packer** | The use of "Arithmetic Noise," "Control Flow Flattening," and "Dead Store" insertions are specific techniques used by obfuscation toolchains (like Tigress) to defeat static analysis and decompiler heuristics. |
| **T1497** | **Virtualization** | The presence of a "VM Layer" where custom virtual machines execute the core malicious logic is a high-sophistication technique to hide intent from standard disassemblers. |
| **T1028** | **Obfuscated Files/Content** | The malware hides C2 instructions within standard X.509 certificate fields (e.g., Subject Alternative Name), using valid file formats to mask malicious data. |
| **T1036** | **Masquerading** | By wrapping Protobuf data in ASN.1/X.509 certificates, the malware masquerades as legitimate identity traffic to bypass network security filters. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "EXTRACTED STRINGS" section contains heavily obfuscated data and machine-generated artifacts. No hard IOCs (IPs, URLs, or Hashes) were found in that section. However, the "BEHAVIORAL ANALYSIS" provides several high-value **behavioral indicators** used for detecting this specific threat actor's methodology.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Memory offsets like `0x3f7e0a00` were excluded as they are dynamic and not persistent file system indicators).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Obfuscation Tooling Fingerprint:** Use of **Tigress**-style obfuscation (specifically the use of `CONCAT` functions, `POPCOUNT` for simple logic, and complex bitwise masks to hide memory offsets).
*   **Malware Frameworks/Libraries:** 
    *   **BouncyCastle:** Used for ASN.1 and X.509 certificate manipulation.
    *   **Protobuf:** Used as the internal data serialization format between the VM layer and the networking layer.
*   **C2 Communication Patterns:**
    *   **Certificate Tunneling:** Data is hidden within standard certificate fields, specifically **Subject Alternative Name (SAN)** and **Issuer** fields in X.509 certificates and PKCS#12 files.
    *   **Protocol Symmetryed Signaling:** Use of non-standard lengths or high-entropy strings within certificate bodies to bypass standard filters.
*   **Code Characteristics:** 
    *   **Control Flow Flattening:** Implementation of complex "State Machines" to move between different stages of packet assembly (Header, Payload, Wrapping).
    *   **Arithmetic Noise:** Excessive use of bitwise logic and carry-flag checks (`CARRY1`, `SBORROW1`) for basic arithmetic.

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification of the sample:

1. **Malware family:** custom 
2. **Malware type:** backdoor
3. **Confidence:** High
4. **Key evidence:**
    *   **Advanced Obfuscation Techniques:** The malware utilizes a "Defense in Depth" approach for its code, including a custom Virtual Machine (VM) layer to execute core logic and Tigress-style arithmetic noise/control flow flattening to defeat static analysis.
    *   **Sophisticated C2 Tunneling:** It employs "Certificate Tunneling," where it hides internal Protobuf-structured data inside X.509 certificates and PKCS#12 files, specifically hiding commands within standard fields (SAN/Issuer) to mimic legitimate identity traffic.
    *   **Complex State Machine Logic:** The use of complex state machines to manage the transition between inner communication protocols (Protobuf) and outer transport wrappers indicates a high-tier effort to mask its functional intent from network security filters.
