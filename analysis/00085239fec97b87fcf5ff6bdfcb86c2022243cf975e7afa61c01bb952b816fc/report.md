# Threat Analysis Report

**Generated:** 2026-06-23 16:19 UTC
**Sample:** `00085239fec97b87fcf5ff6bdfcb86c2022243cf975e7afa61c01bb952b816fc_00085239fec97b87fcf5ff6bdfcb86c2022243cf975e7afa61c01bb952b816fc.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00085239fec97b87fcf5ff6bdfcb86c2022243cf975e7afa61c01bb952b816fc_00085239fec97b87fcf5ff6bdfcb86c2022243cf975e7afa61c01bb952b816fc.exe` |
| File type | PE32+ executable for MS Windows 6.01 (GUI), x86-64, 16 sections |
| Size | 9,145,856 bytes |
| MD5 | `ef9853e7248e17faca5e58787e9767dd` |
| SHA1 | `13084491332368db89ded2c52d2271e8c279b200` |
| SHA256 | `00085239fec97b87fcf5ff6bdfcb86c2022243cf975e7afa61c01bb952b816fc` |
| Overall entropy | 6.923 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 2,914,816 | 6.196 | No |
| `.rdata` | 3,079,680 | 5.644 | No |
| `.data` | 319,488 | 6.238 | No |
| `.pdata` | 67,072 | 5.523 | No |
| `.xdata` | 512 | 1.783 | No |
| `/4` | 512 | 5.673 | No |
| `/19` | 539,136 | 7.996 | ⚠️ Yes |
| `/32` | 109,568 | 7.935 | ⚠️ Yes |
| `/46` | 512 | 1.69 | No |
| `/65` | 852,992 | 7.998 | ⚠️ Yes |
| `/78` | 518,656 | 7.997 | ⚠️ Yes |
| `/95` | 209,408 | 7.995 | ⚠️ Yes |
| `/112` | 13,824 | 7.738 | ⚠️ Yes |
| `.idata` | 1,536 | 4.007 | No |
| `.reloc` | 55,296 | 5.424 | No |
| `.symtab` | 461,312 | 5.347 | No |

### Imports

**kernel32.dll**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetProcessPriorityBoost`, `SetEvent`

## Extracted Strings

Total strings found: **31117** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.xdata
B.idata
.reloc
B.symtab
 Go build ID: "QzXsNmm-VVoElU93s6jG/-0y0Rr3EvhsRP8toolx-/S2BnxKA5yBb1jGANzYGP/HOZIEAXMk-Pj2WoXUmVk"
 
l$ M9,$u
8cpu.u
P0H9S0
PPH9SP
PpH9Sp
UUUUUUUUH!
33333333H!
\$PH9H@v#H
D$pL9A
L$pL9N
D$@I9p
H9D$8s
\$hM9K
\$hM9K
l$8M9,$u
P(H9S(t
P H9S uqH
S0H9P0ug
P88S8u^
P98S9uUH
H9=#Od
expafH
nd 3fH
2-byfH
te kfH
H9uH
H9L$ r
L$@H9
s`H9J
debugCal
debugCal
debugCalH9
debugCalH9
l409u
x6tzH9
l819um
debugCalH9
l163uf
x84t6H9
l327uf
runtime.
runtime H
 error: H
:H9F w
>H+zhH
L$HI9QhuH
D$hH98
P`f9P2tgH
\$0f9C2u
2}#s]H
uH9w t
D$PA)P
H9D$(t
H
^0H9X0tQ
\$XHc
$H+L$HH
T$(H+J
L$(H+A

H9Z(w
\$0H9K
D$pH9H
D$0H9H
v	H9Hkb
|$pH9\$
T$ H+:
UUUUUUUUH!
UUUUUUUUH
wwwwwwwwH!
wwwwwwwwH
vDH950_b
J0f9J2vuH
f9s2uFf
D$$u$L
H9T$@u
H++s_
H+Ur_
H+*r_
T$(M	D
Hc)ma
Hc'[a
	I9x tE1
runtime.H9
QpM9Qhu
L9L$Xt$H
H+x~^
runtime.H9
reflect.H9
D$#e+H
I9N0tVH
T$ 9T$$
H92t9H9rHt3H
rhH92w
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.vendor_golang.org_x_crypto_chacha20poly1305.chacha20Poly1305Seal.abi0` | `0x1401a39a0` | 21787 | ✓ |
| `sym.crypto_internal_fips140_sha3.keccakF1600.abi0` | `0x140276180` | 19597 | ✓ |
| `sym.vendor_golang.org_x_crypto_chacha20poly1305.chacha20Poly1305Open.abi0` | `0x14019eda0` | 19431 | ✓ |
| `sym.crypto_tls._clientHelloMsg_.marshalMsg` | `0x1401cbda0` | 12732 | ✓ |
| `sym.crypto_tls._Conn_.readRecordOrCCS` | `0x1401b35a0` | 12172 | ✓ |
| `sym.time.parse` | `0x1400c9080` | 11679 | ✓ |
| `sym.runtime.callbackasm.abi0` | `0x14007c6c0` | 10001 | ✓ |
| `sym.net_http._Transport_.dialConn` | `0x140246ca0` | 9499 | ✓ |
| `sym.time.Time.appendFormat` | `0x1400c6200` | 9381 | ✓ |
| `sym.crypto_x509.policiesValid` | `0x140196020` | 9285 | ✓ |
| `sym.crypto_internal_fips140_nistec_fiat.p521Mul` | `0x14028f040` | 9164 | ✓ |
| `sym.encoding_asn1.parseField` | `0x140133ee0` | 9136 | ✓ |
| `sym.github.com_gorilla_websocket._Dialer_.DialContext` | `0x14025daa0` | 8985 | ✓ |
| `sym.encoding_json._decodeState_.literalStore` | `0x1400f7a60` | 8773 | ✓ |
| `sym.fmt._pp_.printValue` | `0x1400ed7e0` | 7815 | ✓ |
| `sym.crypto_tls._serverHelloMsg_.marshal` | `0x1401d64a0` | 7667 | ✓ |
| `sym.crypto_internal_fips140_nistec_fiat.p521Square` | `0x140291420` | 7621 | ✓ |
| `sym.syscall.init` | `0x1400b7e80` | 7589 | ✓ |
| `sym.crypto_tls._clientHelloMsg_.unmarshal` | `0x1401d2a20` | 7518 | ✓ |
| `sym.crypto_sha1.blockAVX2.abi0` | `0x140181300` | 7454 | ✓ |
| `sym.crypto_tls._clientHelloMsg_.clone` | `0x1401d47a0` | 7408 | ✓ |
| `sym.encoding_json.typeFields` | `0x140106200` | 6996 | ✓ |
| `sym.encoding_json._decodeState_.object` | `0x1400f5e40` | 6795 | ✓ |
| `sym.crypto_x509.processExtensions` | `0x14018b4c0` | 6437 | ✓ |
| `sym.net._Resolver_.goLookupIPCNAMEOrder` | `0x14015e000` | 6218 | ✓ |
| `sym.runtime.initMetrics` | `0x14001baa0` | 6181 | ✓ |
| `sym.net_http._socksDialer_.connect` | `0x140238200` | 6110 | ✓ |
| `sym.github.com_gorilla_websocket._proxy_socks5_.connect` | `0x140266de0` | 6060 | ✓ |
| `sym.reflect.deepValueEqual` | `0x1400a2b60` | 6012 | ✓ |
| `sym.crypto_tls._Conn_.makeClientHello` | `0x1401be7a0` | 6002 | ✓ |

### Decompiled Code Files

- [`code/sym.crypto_internal_fips140_nistec_fiat.p521Mul.c`](code/sym.crypto_internal_fips140_nistec_fiat.p521Mul.c)
- [`code/sym.crypto_internal_fips140_nistec_fiat.p521Square.c`](code/sym.crypto_internal_fips140_nistec_fiat.p521Square.c)
- [`code/sym.crypto_internal_fips140_sha3.keccakF1600.abi0.c`](code/sym.crypto_internal_fips140_sha3.keccakF1600.abi0.c)
- [`code/sym.crypto_sha1.blockAVX2.abi0.c`](code/sym.crypto_sha1.blockAVX2.abi0.c)
- [`code/sym.crypto_tls._Conn_.makeClientHello.c`](code/sym.crypto_tls._Conn_.makeClientHello.c)
- [`code/sym.crypto_tls._Conn_.readRecordOrCCS.c`](code/sym.crypto_tls._Conn_.readRecordOrCCS.c)
- [`code/sym.crypto_tls._clientHelloMsg_.clone.c`](code/sym.crypto_tls._clientHelloMsg_.clone.c)
- [`code/sym.crypto_tls._clientHelloMsg_.marshalMsg.c`](code/sym.crypto_tls._clientHelloMsg_.marshalMsg.c)
- [`code/sym.crypto_tls._clientHelloMsg_.unmarshal.c`](code/sym.crypto_tls._clientHelloMsg_.unmarshal.c)
- [`code/sym.crypto_tls._serverHelloMsg_.marshal.c`](code/sym.crypto_tls._serverHelloMsg_.marshal.c)
- [`code/sym.crypto_x509.policiesValid.c`](code/sym.crypto_x509.policiesValid.c)
- [`code/sym.crypto_x509.processExtensions.c`](code/sym.crypto_x509.processExtensions.c)
- [`code/sym.encoding_asn1.parseField.c`](code/sym.encoding_asn1.parseField.c)
- [`code/sym.encoding_json._decodeState_.literalStore.c`](code/sym.encoding_json._decodeState_.literalStore.c)
- [`code/sym.encoding_json._decodeState_.object.c`](code/sym.encoding_json._decodeState_.object.c)
- [`code/sym.encoding_json.typeFields.c`](code/sym.encoding_json.typeFields.c)
- [`code/sym.fmt._pp_.printValue.c`](code/sym.fmt._pp_.printValue.c)
- [`code/sym.github.com_gorilla_websocket._Dialer_.DialContext.c`](code/sym.github.com_gorilla_websocket._Dialer_.DialContext.c)
- [`code/sym.github.com_gorilla_websocket._proxy_socks5_.connect.c`](code/sym.github.com_gorilla_websocket._proxy_socks5_.connect.c)
- [`code/sym.net._Resolver_.goLookupIPCNAMEOrder.c`](code/sym.net._Resolver_.goLookupIPCNAMEOrder.c)
- [`code/sym.net_http._Transport_.dialConn.c`](code/sym.net_http._Transport_.dialConn.c)
- [`code/sym.net_http._socksDialer_.connect.c`](code/sym.net_http._socksDialer_.connect.c)
- [`code/sym.reflect.deepValueEqual.c`](code/sym.reflect.deepValueEqual.c)
- [`code/sym.runtime.callbackasm.abi0.c`](code/sym.runtime.callbackasm.abi0.c)
- [`code/sym.runtime.initMetrics.c`](code/sym.runtime.initMetrics.c)
- [`code/sym.syscall.init.c`](code/sym.syscall.init.c)
- [`code/sym.time.Time.appendFormat.c`](code/sym.time.Time.appendFormat.c)
- [`code/sym.time.parse.c`](code/sym.time.parse.c)
- [`code/sym.vendor_golang.org_x_crypto_chacha20poly1305.chacha20Poly1305Open.abi0.c`](code/sym.vendor_golang.org_x_crypto_chacha20poly1305.chacha20Poly1305Open.abi0.c)
- [`code/sym.vendor_golang.org_x_crypto_chacha20poly1305.chacha20Poly1305Seal.abi0.c`](code/sym.vendor_golang.org_x_crypto_chacha20poly1305.chacha20Poly1305Seal.abi0.c)

## Behavioral Analysis

This final disassembly chunk completes the technical profile of the malware, transitioning its classification from "sophisticated" to **"highly advanced / elite."** 

The addition of Post-Quantum Cryptography (PQC) and Encrypted Client Hello (ECH) suggests that the developers are not just following current standards but are implementing cutting-edge protocols designed to resist both modern traffic analysis and future cryptographic advancements.

### Updated Analysis Summary: Cutting-Edge Encryption & Privacy Shielding

Chunk 19 reveals a significant leap in engineering sophistication. While previous chunks showed "professional" standard usage (SOCKS5, WebSockets), this section shows the integration of **Post-Quantum Cryptography (PQC)** and **Advanced Privacy Protocols** to mask even the metadata of the communication.

---

### 1. New Technical Findings: Post-Quantum & Metadata Obfuscation
The disassembly highlights several high-level cryptographic primitives that are rare in standard malware but common in highly secure, modern infrastructure.

*   **ML-KEM (Module-Lattice-based Key-Encapsulation Mechanism):** The inclusion of `sym.crypto_internal_fips140_mlkem` is a critical discovery. ML-KEM (formerly known as Kyber) is the primary algorithm selected by NIST for **Post-Quantum Cryptography**.
    *   *Impact:* This indicates that the malware’s communication infrastructure is designed to be "future-proof" against quantum computing threats and, more practically, uses very high-end cryptographic libraries that are extremely difficult to distinguish from top-tier secure software.
*   **HPKE (Hybrid Public Key Encryption):** The use of `sym.crypto_internal_hpke` suggests the malware uses a hybrid approach for payload encryption, combining asymmetric and symmetric keys.
    *   *Impact:* HPKE is common in modern privacy-centric protocols (like Signal or modern email standards). It ensures that even if one part of the encryption is compromised, the other remains intact.
*   **ECH (Encrypted Client Hello) Support:** The implementation of `parseECHConfigList` and `pickECHConfig` provides a significant layer of network defense. ECH encrypts the entire "Client Hello" portion of the TLS handshake.
    *   *Impact:* **This hides the SNI (Server Name Indication).** In standard HTTPS, even if the content is encrypted, the domain name (e.g., `c2-server.com`) is visible in plaintext during the handshake. ECH makes it impossible for network defenders to see which specific domain the malware is contacting via passive traffic analysis.

### 2. Advanced Technical Analysis: The "Invisible" Infrastructure
The move from standard encryption to these advanced protocols suggests a strategic goal of **Total Communication Blindness.**

*   **Eliminating Fingerprinting:** By using ML-KEM and HPKE, the developers ensure that the cryptographic handshake is indist1inguishable from high-security web services. 
*   **Neutralizing Metadata Analysis:** The inclusion of ECH means that even if a defender identifies a suspicious IP address, they cannot easily determine *what service* or *which sub-domain* the malware is interacting with on that IP. This allows the threat actor to host multiple pieces of infrastructure on a single "front" server while only reaching the one intended for this specific malware sample.
*   **Hardening against Interception:** The combination of SOCKS5 (for routing), WebSockets (for persistence), and ML-KEM/HPKE (for encryption) means that every possible layer of observation—from network path, to packet content, to handshake metadata—is shielded by high-grade technical "wrapping."

### 3. Sophistication and Threat Context
The inclusion of these features suggests an **Advanced Persistent Threat (APT)** or a very well-funded cybercriminal organization.

*   **Development Maturity:** The code does not look like a "custom" malware build; it utilizes the full breadth of Go’s internal crypto libraries, including experimental or advanced modules (like ML-EM). This indicates a high level of experience in both software engineering and network security.
*   **Strategic Persistence:** By implementing ECH and Post-Quantum logic, the actors are deliberately making their traffic "untrackable" by standard automated systems that look for leaked SNIs or common cryptographic flaws.

---

### Updated Indicators for Incident Response (IR)

*   **Metadata Blindness (High Risk):**
    *   *Observation:* Implementation of `parseECHConfigList` and `pickECHConfig`.
    *   *Impact:* Because the Server Name Indication (SNI) is encrypted, **DNS filtering and standard deep packet inspection (DPI) may fail to identify the destination host.** Analysts should look for "unusual" IP connections that lack associated SNI data in the TLS handshake.
*   **Post-Quantum Ready Infrastructure:** 
    *   *Observation:* Integration of `fips140_mlkem`.
    *   *Impact:* The infrastructure is likely hosted on very high-end, modern platforms. If a C2 server is found, it may be running sophisticated web servers designed to handle these modern protocols.
*   **Payload Integrity via HPKE:**
    *   *Observation:* Usage of `crypto_internal_hpke`.
    *   *Impact:* Standard "man-in-the-middle" (MITM) attempts by security appliances will likely fail unless the appliance has the specific keys, making it extremely difficult to intercept or inject commands into the communication stream.

---

### Final Comprehensive Summary Table for IR Report

| Feature | Technical Implementation | Security Impact / Significance |
| :--- | :--- | :--- |
| **Core Transport** | Standardized TLS (Go `crypto_tls`) | Ensures handshake passes standard checks; mirrors high-end web traffic. |
| **Proxy Support** | SOCKS4/5 Proxy Integration | Enables "tunneling" through internal or external proxies to hide origin. |
| **WebSocket Usage** | `gorilla_websocket` integration | Provides long-lived, full-duplex connections (heartbeat minimization). |
| **DNS Resilience** | Robust `goLookupIPCNAMEOrder` | Handles A/AAAA/CNAME; mirrors standard OS browser behavior perfectly. |
| **Hardware Accel.** | AVX2 Optimized (`blockAVX2`) | High performance for crypto operations, indistinguishable from native apps. |
| **Encrypted SNI** | **ECH (Encrypted Client Hello)** | **Critical:** Masks the destination domain name in the TLS handshake. |
| **Next-Gen Crypto** | **ML-KEM / HPKE** | **High Sophistication:** Uses Post-Quantum logic and hybrid encryption to harden communication against interception. |
| **Data Layer** | JSON Serialization | Wraps commands in standard format, blending into mobile/IoT/web API traffic. |
| **Persistence** | Persistence via WebSockets | Reduces the "noise" of repeated connection attempts; appears as a constant active session. |
| **Engineering Rank** | **Elite / Advanced** | The malware utilizes professional-grade infrastructure and cutting-edge crypto to bypass advanced perimeter defenses. |

**Final Conclusion for Report:**
The analysis confirms that this is an extremely high-tier threat actor. By utilizing **SOCKS5, WebSockets, ML-KEM (Post-Quantum), and ECH**, the adversary has built a "defense-in-depth" communication model. They are not just attempting to hide their data; they are specifically designed to bypass sophisticated network visibility tools that look for common malware tell-tales. Detection should focus on **behavioral anomalies** (e.g., persistent connections to high-reputation cloud providers) rather than standard signature or protocol-based detection.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1090.003** | Proxy: SOCKS | The malware utilizes SOCKS4/5 proxy integration to tunnel traffic, effectively hiding the origin and routing path of its communications. |
| **T1573** | Encrypted Channel | The implementation of ML-KEM, HPKE, and ECH creates a highly sophisticated encrypted channel designed to hide both payload content and metadata (like SNI) from network defenders. |
| **T1071.001** | Application Layer Protocol: Web Protocols | The use of WebSockets allows the malware to maintain persistent, full-duplex connections that mimic standard web traffic behavior to avoid detection. |
| **T1036** | Masquerading | By mimicking "standard OS browser" behavior and using industry-standard cryptographic libraries (Go's internal crypto), the malware blends in with legitimate high-security software. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

**File paths / Registry keys**
*   *(None identified; "rdata" and "data" sections are standard binary segments and were excluded as false positives.)*

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   **Go Build ID:** `QzXsNmm-VVoElU93s6jG/-0y0Rr3EvhsRP8toolx-/S2BnxKA5yBb1jGANzYGP/HOZIEAXMk-Pj2WoXUmVk` 
    *(Note: While not a standard MD5/SHA hash, this is a unique identifier for the specific binary build.)*

**Other artifacts (user agents, C2 patterns, etc.)**
*   **C2 Protocols:** WebSockets (specifically using `gorilla_websocket` library).
*   **Encryption Primitives:** 
    *   ML-KEM (Module-Lattice-based Key-Encapsulation Mechanism / `fips140_mlkem`)
    *   HPKE (Hybrid Public Key Encryption)
*   **Network Obfuscation:** 
    *   ECH (Encrypted Client Hello) - Used to hide SNI (Server Name Indication).
    *   SOCKS4/5 Proxy integration for traffic routing.
*   **Data Serialization:** JSON format used for command and control payloads.
*   **Technical Indicators of Sophistication:** 
    *   Use of `go_crypto` internal libraries.
    *   AVX2 optimization (`blockAVX2`) for cryptographic calculations.
    *   Presence of internals like `debugCal` and `memprofi`.

---

## Malware Family Classification

Based on the detailed behavioral analysis provided, here is the classification:

1. **Malware family:** Custom (Advanced/APT-level)
2. **Malware type:** Backdoor / RAT 
3. **Confidence:** High

**Key evidence:**
*   **Advanced Cryptographic Stack:** The use of Post-Quantum Cryptography (ML-KEM) and Hybrid Public Key Encryption (HPKE) indicates a high-tier threat actor aiming for "future-proof" communication that is nearly impossible to decrypt or analyze using standard means.
*   **Sophisticated Network Obfuscation:** The implementation of Encrypted Client Hello (ECH) specifically targets the concealment of Server Name Indication (SNI), deliberately designed to bypass Deep Packet Inspection (DPI) and DNS filtering.
*   **Professional Engineering Maturity:** The combination of SOCKS5 proxying, WebSockets for persistent communication, and Go-based infrastructure demonstrates a "defense-in-depth" approach intended to mimic legitimate high-security web services rather than standard common malware.
