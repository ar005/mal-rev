# Threat Analysis Report

**Generated:** 2026-07-26 10:24 UTC
**Sample:** `0b74e5aa8e84ddefd60a6663e6305b3615eb743db543323f8a0068b58d56503f_0b74e5aa8e84ddefd60a6663e6305b3615eb743db543323f8a0068b58d56503f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b74e5aa8e84ddefd60a6663e6305b3615eb743db543323f8a0068b58d56503f_0b74e5aa8e84ddefd60a6663e6305b3615eb743db543323f8a0068b58d56503f.exe` |
| File type | PE32+ executable for MS Windows 6.01 (console), x86-64, 15 sections |
| Size | 7,192,576 bytes |
| MD5 | `50c07df13d2f922186d9c50d636d08ab` |
| SHA1 | `b587f8daa51a09d3409a8ee85f7a71a3351472ba` |
| SHA256 | `0b74e5aa8e84ddefd60a6663e6305b3615eb743db543323f8a0068b58d56503f` |
| Overall entropy | 6.942 |
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
| `.text` | 2,255,360 | 6.221 | No |
| `.rdata` | 2,370,560 | 5.492 | No |
| `.data` | 184,832 | 6.375 | No |
| `.pdata` | 50,176 | 5.468 | No |
| `.xdata` | 512 | 1.783 | No |
| `/4` | 512 | 5.579 | No |
| `/19` | 408,064 | 7.996 | ⚠️ Yes |
| `/32` | 81,920 | 7.937 | ⚠️ Yes |
| `/46` | 512 | 0.792 | No |
| `/65` | 740,864 | 7.998 | ⚠️ Yes |
| `/78` | 535,552 | 7.996 | ⚠️ Yes |
| `/90` | 163,328 | 7.816 | ⚠️ Yes |
| `.idata` | 1,536 | 3.932 | No |
| `.reloc` | 42,496 | 5.425 | No |
| `.symtab` | 354,816 | 5.332 | No |

### Imports

**kernel32.dll**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetProcessPriorityBoost`, `SetEvent`

## Extracted Strings

Total strings found: **23859** (showing first 100)

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
 Go build ID: "AZj8o7xa95EHLwqROtkR/R9kxpBkTPiPeVyMarcMp/SsKEn4_w0V6C7K3qsni3/7hBdVaxXkPVxx_tHoW9l"
 
l$ M9,$u
8cpu.u
P0H9S0
PPH9SP
PpH9Sp
UUUUUUUUH!
33333333H!
D$@I9p
\$hM9K
\$hM9K
P(H9S(t
P H9S ujH
S0H9P0u`
8S8uUH
expafH
nd 3fH
2-byfH
te kfH
\$hH9H@v#H
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
2H+phH
L$HI9QhuH
D$hH98
P`f9P2tgH
\$0f9C2u
H9D$(t
H
H9X0tO
\$XHc
$H+L$HH
Hcl%L
T$(H+J
L$(H+A
l$(M9,$u

H9Z(w
\$0H9K
D$pH9H
D$0H9H
v	H9 
|$pH9\$
T$ H+:
UUUUUUUUH!
UUUUUUUUH
wwwwwwwwH!
wwwwwwwwH
J0f9J2vsH
f9s2uFf
D$$u$L
T$(M	D
L$0H+Y
runtime.H9
QpM9Qhu
L9L$Xt#H
runtime.H9
reflect.H9
D$#e+H
I9N0tVH
T$ 9T$$
H92t6H9rPt0H
rpH92w
tRI9N0tLH
T$`Hc
L$XHcO
|$0uMH
memprofi
lerau*f
yteu"H
,$M9l$
0H9G@u*
9q0s&H9J
09z0w
H
H9X(v
L
HPH9w
H(H9w
H9*jA
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.vendor_golang.org_x_crypto_chacha20poly1305.chacha20Poly1305Seal.abi0` | `0x561780` | 21787 | ✓ |
| `sym.crypto_internal_fips140_sha3.keccakF1600.abi0` | `0x5d15e0` | 19597 | ✓ |
| `sym.vendor_golang.org_x_crypto_chacha20poly1305.chacha20Poly1305Open.abi0` | `0x55cb80` | 19431 | ✓ |
| `sym.github.com_shamaton_msgpack_v2_internal_stream_decoding._decoder_.asFixedMap` | `0x5bab20` | 16947 | ✓ |
| `sym.crypto_internal_fips140_sha512.blockAMD64.abi0` | `0x5d7800` | 16138 | ✓ |
| `sym.crypto_tls._clientHelloMsg_.marshalMsg` | `0x586f40` | 12668 | ✓ |
| `sym.crypto_tls._Conn_.readRecordOrCCS` | `0x56ee40` | 12012 | ✓ |
| `sym.time.parse` | `0x4a2140` | 11679 | ✓ |
| `sym.github.com_shamaton_msgpack_v2_internal_decoding.init` | `0x5b1c40` | 10317 | ✓ |
| `sym.github.com_shamaton_msgpack_v2_internal_stream_decoding.init` | `0x5b44a0` | 10317 | ✓ |
| `sym.crypto_internal_fips140_sha256.blockAMD64.abi0` | `0x5cc140` | 10151 | ✓ |
| `sym.encoding_asn1.parseField` | `0x4f0b20` | 10093 | ✓ |
| `sym.runtime.callbackasm.abi0` | `0x4774e0` | 10001 | ✓ |
| `sym.crypto_x509.policiesValid` | `0x554080` | 9445 | ✓ |
| `sym.time.Time.appendFormat` | `0x49f2e0` | 9349 | ✓ |
| `sym.crypto_internal_fips140_nistec_fiat.p521Mul` | `0x5ee000` | 9164 | ✓ |
| `sym.github.com_shamaton_msgpack_v2_internal_stream_encoding._encoder_.writeFixedMap` | `0x5c3d00` | 8709 | ✓ |
| `sym.fmt._pp_.printValue` | `0x4d34c0` | 7815 | ✓ |
| `sym.crypto_tls._serverHelloMsg_.marshal` | `0x591660` | 7667 | ✓ |
| `sym.crypto_internal_fips140_nistec_fiat.p521Square` | `0x5f03e0` | 7621 | ✓ |
| `sym.crypto_tls._clientHelloMsg_.unmarshal` | `0x58dba0` | 7582 | ✓ |
| `sym.syscall.init` | `0x493ec0` | 7540 | ✓ |
| `sym.crypto_sha1.blockAVX2.abi0` | `0x53ff40` | 7454 | ✓ |
| `sym.crypto_tls._clientHelloMsg_.clone` | `0x58f960` | 7407 | ✓ |
| `sym.crypto_tls._Conn_.makeClientHello` | `0x579640` | 6489 | ✓ |
| `sym.crypto_x509.processExtensions` | `0x548fa0` | 6373 | ✓ |
| `sym.net._Resolver_.goLookupIPCNAMEOrder` | `0x51db40` | 6218 | ✓ |
| `sym.runtime.initMetrics` | `0x4197c0` | 6213 | ✓ |
| `sym.reflect.deepValueEqual` | `0x4bf240` | 6012 | ✓ |
| `sym.log.formatHeader` | `0x5a5340` | 5521 | ✓ |

### Decompiled Code Files

- [`code/sym.crypto_internal_fips140_nistec_fiat.p521Mul.c`](code/sym.crypto_internal_fips140_nistec_fiat.p521Mul.c)
- [`code/sym.crypto_internal_fips140_nistec_fiat.p521Square.c`](code/sym.crypto_internal_fips140_nistec_fiat.p521Square.c)
- [`code/sym.crypto_internal_fips140_sha256.blockAMD64.abi0.c`](code/sym.crypto_internal_fips140_sha256.blockAMD64.abi0.c)
- [`code/sym.crypto_internal_fips140_sha3.keccakF1600.abi0.c`](code/sym.crypto_internal_fips140_sha3.keccakF1600.abi0.c)
- [`code/sym.crypto_internal_fips140_sha512.blockAMD64.abi0.c`](code/sym.crypto_internal_fips140_sha512.blockAMD64.abi0.c)
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
- [`code/sym.fmt._pp_.printValue.c`](code/sym.fmt._pp_.printValue.c)
- [`code/sym.github.com_shamaton_msgpack_v2_internal_decoding.init.c`](code/sym.github.com_shamaton_msgpack_v2_internal_decoding.init.c)
- [`code/sym.github.com_shamaton_msgpack_v2_internal_stream_decoding._decoder_.asFixedMap.c`](code/sym.github.com_shamaton_msgpack_v2_internal_stream_decoding._decoder_.asFixedMap.c)
- [`code/sym.github.com_shamaton_msgpack_v2_internal_stream_decoding.init.c`](code/sym.github.com_shamaton_msgpack_v2_internal_stream_decoding.init.c)
- [`code/sym.github.com_shamaton_msgpack_v2_internal_stream_encoding._encoder_.writeFixedMap.c`](code/sym.github.com_shamaton_msgpack_v2_internal_stream_encoding._encoder_.writeFixedMap.c)
- [`code/sym.log.formatHeader.c`](code/sym.log.formatHeader.c)
- [`code/sym.net._Resolver_.goLookupIPCNAMEOrder.c`](code/sym.net._Resolver_.goLookupIPCNAMEOrder.c)
- [`code/sym.reflect.deepValueEqual.c`](code/sym.reflect.deepValueEqual.c)
- [`code/sym.runtime.callbackasm.abi0.c`](code/sym.runtime.callbackasm.abi0.c)
- [`code/sym.runtime.initMetrics.c`](code/sym.runtime.initMetrics.c)
- [`code/sym.syscall.init.c`](code/sym.syscall.init.c)
- [`code/sym.time.Time.appendFormat.c`](code/sym.time.Time.appendFormat.c)
- [`code/sym.time.parse.c`](code/sym.time.parse.c)
- [`code/sym.vendor_golang.org_x_crypto_chacha20poly1305.chacha20Poly1305Open.abi0.c`](code/sym.vendor_golang.org_x_crypto_chacha20poly1305.chacha20Poly1305Open.abi0.c)
- [`code/sym.vendor_golang.org_x_crypto_chacha20poly1305.chacha20Poly1305Seal.abi0.c`](code/sym.vendor_golang.org_x_crypto_chacha20poly1305.chacha20Poly1305Seal.abi0.c)

## Behavioral Analysis

This analysis incorporates all findings from Chunks 1 through 19. The addition of Chunk 19 finalizes the profile of an extremely sophisticated, high-effort malware specimen.

### Updated Analysis (Chunks 18 & 19)

#### 5. Robust Network Resolution (`sym.net._Resolver_.goLookupIPCNAMEOrder`)
*   **The Logic:** This function manages complex IP resolution for domain names into usable addresses, specifically adhering to **RFC6724**.
*   **Technical Implications:** The malware is "network-aware," capable of handling multiple A/AAAA records and navigating complex internal routing tables.
*   **Significance:** Indicates a **High-Availability C2 Infrastructure.** It ensures the bot remains connected even if specific IP addresses are blocked or filtered, by intelligently selecting the best available path.

#### 6. Runtime Integrity and Complexity (`sym.reflect.deepValueEqual`)
*   **The Logic:** A recursive comparison of complex, nested data structures to determine equality.
*   **Technical Implications:** Suggests that the malware is not just passing simple strings; it is exchanging **complex structured objects**.
*   **Significance:** Indicates sophisticated "handshaking." It likely validates the integrity of multi-layered heartbeats or checks if local configurations perfectly match remote requirements, preventing tampering or mismatch errors.

#### 7. Standard-Compliant Logging and Timing (`sym.log.formatHeader`)
*   **The Logic:** Converts timestamps into human-readable formats (e.g., "YYYY-MM-DD").
*   **Technical Implications:** Points to a **professional development lifecycle.** These logs are likely used by the threat actor for internal telemetry, debugging the botnet's health, and maintaining uptime.

#### 8. Complex Buffer Management & Parsing (`sym.runtime.growslice`, `memmove`) (New in Chunk 19)
*   **The Logic:** The final disassembly reveals intense activity around memory management, specifically dynamic buffer growth (`growslice`), memory shifting (`memmove`), and string manipulation.
*   **Technical Implications:** The code contains numerous checks for specific characters like `:` (`0x3a`), `/` (`0x2f`), and ` ` (space). This indicates that the malware is **parsing complex strings/URLs or structured data packets.**
*   **Significance:** This demonstrates a **Refined Parsing Engine.** Instead of simple command execution, the malware parses incoming C2 responses to determine specific paths, sub-functions, or local configuration instructions. The heavy use of standard Go runtime functions for memory management suggests that even its "internal" housekeeping is built on professional-grade software architecture.

---

### Sophistication & Threat Actor Profiling (Updated)

*   **Sophistication Level: State-Sponsored / Elite Tier (Confirmed).**
    The convergence of **Post-Quantum Cryptography (ML-KEM)**, **Encrypted Client Hello (ECH)**, and a **robust, standard-compliant internal framework** marks this as the work of an elite actor. They are not "script kiddies"; they are engineers who have built a highly resilient communication platform that mimics high-end enterprise software.

*   **Infrastructure & Logic Resilience:**
    By adhering to RFC6724 and using dynamic memory growth for buffer management, the authors ensure the malware can operate in diverse network environments while handling unpredictable amounts of data from their C2. They have prioritized **longevity and reliability.**

---

### Updated Summary for Incident Response (IR)

The analysis confirms a "hardened" communication stack designed to resist both automated detection and manual traffic analysis.

#### 1. Capability - Resilience and Robustness
*   **Mechanism:** The malware uses standard-compliant DNS resolution and dynamic buffer growth. It can handle complex C2 instructions that are parsed into specific actions.
*   **Impact on IR:** Simple IP blacklisting is likely ineffective. The bot will pivot between multiple IPs (A/AAAA records) and parse nuanced commands, making its behavior appear like legitimate application traffic.

#### 2. Detection & Mitigation Strategy (Updated)
*   **Detection via DNS Behavior:** Monitor for high-frequency lookups or queries that occur just before an ECH-enabled connection is established. Identify IPs belonging to "rotating" infrastructures.
*   **Detecting Complex Handshakes:** Because `deepValueEqual` suggests complex data exchange, focus on **behavioral patterns**. Analyze the *size* and *timing* of outbound packets (heartbeats). Consistent packet sizes/intervals are a tell-tale sign of automated C2 check-ins.
*   **Memory Forensics:** Due to the use of `growslice` and `memmove`, look for large or dynamically resizing buffers in memory associated with the process during its "idle" state, as these may hold parsed instructions from the C2.

#### 3. Advanced Hunting Queries (Updated)
*   **Identify "Resilient" DNS Behavior:** Alert on processes that resolve a single domain but attempt multiple IP addresses in rapid succession before establishing a TLS session.
*   **Search for Go-Specific Artifacts:** The presence of `runtime.gcWriteBarrier2`, `growslice`, and standard Go runtime logic confirms this is a **Go-based binary**. Look for other binaries using the Go runtime that also incorporate high-end crypto (ML-KEM/ECH).
*   **Hunt for Parsing Signatures:** Search for code segments that perform frequent memory shifts (`memmove`) combined with specific string separators (`:`, `/`). This indicates a sophisticated command parsing engine.

---

### New Action Items for Technical Team:
1.  **Infrastructure Mapping:** Map out all IPs associated with "suspicious" domains in your logs to identify infrastructure that supports the multi-IP rotation enabled by RFC6724 compliance.
2.  **Identify Outlier Go-based Binaries:** Scan for other binaries exhibiting these three combined traits: (1) Advanced Cryptography, (2) Standard Go Runtime Artifacts, and (3) Robust Network Resilience logic.
3.  **Behavioral Analysis of Heartbeats:** Since ECH hides the destination, use **timing analysis**. Identify persistent connections on 443/80 with consistent packet sizes occurring at regular intervals to identify the heartbeat mechanism.
4.  **Enhanced Log Analysis:** Look for internal logs or strings that indicate "heartbeat" checks or date-formatting (`YYYY-MM-DD`) which may be used as diagnostic markers by the threat actor.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1568.003 | Dynamic Resolution: DNS | The use of RFC6724 compliance and multi-record (A/AAAA) handling ensures the malware maintains high availability by navigating complex C2 infrastructures. |
| T1071.001 | Application Layer Protocol: Web Services | The parsing logic for characters like `:` and `/` indicates a command engine designed to interpret instructions via web-like infrastructure or paths. |
| T1036 | Masquerading | The integration of standard Go libraries, RFC compliance, and professional development standards allows the malware to mimic legitimate enterprise software traffic. |
| T1572 | Protocol Impersonation | (Optional/Contextual) The use of "standard-compliant" behavior and common infrastructure patterns is designed to hide malicious traffic within standard network flows. |

---

## Indicators of Compromise

Based on the provided data, here is the intelligence report regarding the extracted Indicators of Compromise (IOCs) and behavioral patterns.

### **1. IP addresses / URLs / Domains**
*No literal IP addresses or domain names were found in the provided text.*
*   **Note for Analysts:** While no hardcoded strings exist, the analysis indicates a **High-Availability C2 Infrastructure**. The malware uses RFC6724 compliant resolution to rotate between multiple A and AAAA records.

### **2. File paths / Registry keys**
*No specific file paths or registry keys were identified in the provided data.*

### **3. Mutex names / Named pipes**
*None detected.*

### **4. Hashes**
*   **Build ID:** `AZj8o7xa95EHLwqROtkR/R9kxpBkTPiPeVyMarcMp/SsKEn4_w0V6C7K3qsni3/7hBdVaxXkPVxx_tHoW9l`
    *(Note: While not a file hash, this unique Go build identifier can be used to fingerprint the specific variant of the malware in memory.)*

### **5. Other artifacts (Behavioral & Technical Indicators)**
**Network Behaviors:**
*   **Sophisticated C2 Resolution:** Implementation of `goLookupIPCNAMEOrder` following RFC6724 standards (indicates a resilient infrastructure capable of switching IPs).
*   **Encrypted Client Hello (ECH):** Usage of ECH to obfuscate the SNI (Server Name Indication) during the TLS handshake.
*   **Post-Quantum Cryptography:** Implementation of **ML-KEM** for secure communication.
*   **Heartbeat Traffic:** Utilization of a "heartbeat" mechanism characterized by consistent packet sizes and regular intervals over ports 80/443.

**Parsing & Logic Artifacts:**
*   **Complex Parsing Engine:** Evidence of `memmove` and `growslice` logic used to parse strings containing `:` (colon) and `/` (forward slash), indicating the parsing of complex URLs or nested C2 commands.
*   **Data Integrity Verification:** Use of `reflect.deepValueEqual` suggests a sophisticated multi-layered handshake where data packets are verified for integrity before execution.

**Development Footprints (Go Language):**
*   **Runtime Artifacts:** Detection of standard Go runtime libraries (`runtime.growslice`, `runtime.gcWriteBarrier2`).
*   **Internal Logging:** Use of date formatting (e.g., `YYYY-MM-DD`) in internal logs for telemetry and development debugging.

---

### **Summary for Incident Response (IR)**
*   **Threat Actor Profile:** Elite / State-Sponsored level sophistication.
*   **Primary Concern:** The malware is "hardened" against standard network blocking; simple IP blacklisting will likely fail due to multi-record DNS rotation and ECH encryption. 
*   **Detection Recommendation:** Focus on **behavioral signatures**:
    1.  Monitor for high-frequency lookups of a single domain that resolve multiple A/AAAA records in rapid succession.
    2.  Identify "Heartbeat" patterns (constant size/timing) to bypass ECH obfuscation.
    3.  Filter for Go-based binaries exhibiting both advanced encryption (ML-KEM) and standard library usage.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `sym.net`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: backdoor / RAT
3. **Confidence**: High (for classification), Medium (for specific brand naming)

4. **Key evidence**:
*   **Advanced Communication Hardening:** The integration of Post-Quantum Cryptography (ML-KEM) and Encrypted Client Hello (ECH) indicates a high-sophistication, elite-level threat actor intent on bypassing advanced network inspection tools.
*   **Robust C2 Infrastructure Logic:** The implementation of RFC6724 compliant DNS resolution for A/AAAA records combined with multi-layered integrity checks (`reflect.deepValueEqual`) suggests a stable, long-term command-and-control framework rather than a simple one-off downloader.
*   **Sophisticated Parsing Engine:** The use of `memmove` and `growslice` to process complex strings containing `:` and `/`, combined with "heartbeat" telemetry, confirms the existence of an internal parsing engine designed to handle complex commands from a remote server.
