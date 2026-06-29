# Threat Analysis Report

**Generated:** 2026-06-28 10:25 UTC
**Sample:** `02aa8cabeea2a0120a31adbf0886f821d10953fc6d4d9cd1959568093c48b04d_02aa8cabeea2a0120a31adbf0886f821d10953fc6d4d9cd1959568093c48b04d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `02aa8cabeea2a0120a31adbf0886f821d10953fc6d4d9cd1959568093c48b04d_02aa8cabeea2a0120a31adbf0886f821d10953fc6d4d9cd1959568093c48b04d.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 50,176 bytes |
| MD5 | `74bb3514f737d1386b7ced741ec1e098` |
| SHA1 | `25de16039754b3870676911b146a956d30b2e8fa` |
| SHA256 | `02aa8cabeea2a0120a31adbf0886f821d10953fc6d4d9cd1959568093c48b04d` |
| Overall entropy | 5.636 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1697492453 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 43,008 | 5.506 | No |
| `.rsrc` | 6,144 | 6.552 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **503** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v4.0.30319
#Strings
Action`10
<>p__0
IEnumerable`1
CallSite`1
List`1
__StaticArrayInitTypeSize=32
Microsoft.Win32
ToUInt32
ToInt32
SwapInt32
<>o__2
X509Certificate2
WriteUInt64
ToUInt64
GetAsUInt64
SetAsUInt64
ToInt64
SwapInt64
ToUInt16
ToInt16
SwapInt16
HMACSHA256
Sha256
Aes256
aes256
__StaticArrayInitTypeSize=6
get_UTF8
<Module>
MessagePackLib.<PrivateImplementationDetails>
1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B
ES_SYSTEM_REQUIRED
ES_DISPLAY_REQUIRED
MapNameToOID
get_FormatID
EXECUTION_STATE
87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F
get_ASCII
System.IO
ES_CONTINUOUS
get_IV
set_IV
GenerateIV
value__
ReadServertData
mscorlib
System.Collections.Generic
Microsoft.VisualBasic
get_SendSync
EndRead
BeginRead
Thread
InnerAdd
SHA256Managed
get_Connected
get_IsConnected
set_IsConnected
Received
get_Guid
<SendSync>k__BackingField
<IsConnected>k__BackingField
<KeepAlive>k__BackingField
<HeaderSize>k__BackingField
<Ping>k__BackingField
<ActivatePong>k__BackingField
<Interval>k__BackingField
<Buffer>k__BackingField
<Offset>k__BackingField
<SslClient>k__BackingField
<TcpClient>k__BackingField
InnerAddMapChild
InnerAddArrayChild
Append
RegistryValueKind
Replace
CreateInstance
set_Mode
FileMode
PaddingMode
EnterDebugMode
CryptoStreamMode
CompressionMode
CipherMode
SelectMode
utf8Encode
DeleteSubKeyTree
get_Message
DetectSandboxie
Invoke
IEnumerable
IDisposable
ToDouble
SwapDouble
get_Handle
RuntimeFieldHandle
GetModuleHandle
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x40596c` | 50836 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.DecodeFromStream` | `0x404d48` | 1556 | ✓ |
| `method.Client.Connection.ClientSocket.InitializeClient` | `0x40296c` | 844 | ✓ |
| `method.Client.Install.NormalStartup.Install` | `0x403110` | 744 | ✓ |
| `method.Client.Handle_Packet.Packet.Read` | `0x403da0` | 564 | ✓ |
| `method.Client.Connection.ClientSocket.ReadServertData` | `0x402d40` | 484 | ✓ |
| `method.Client.Algorithm.Aes256.Decrypt` | `0x4042c4` | 448 | ✓ |
| `method.Client.Helper.IdSender.SendInfo` | `0x40375c` | 444 | ✓ |
| `method.Client.Settings.InitializeSettings` | `0x4026f8` | 344 | ✓ |
| `method.Client.Algorithm.Aes256.Encrypt` | `0x40416c` | 344 | ✓ |
| `method.MessagePackLib.MessagePack.WriteTools.WriteInteger` | `0x40579c` | 324 | ✓ |
| `method.Client.Helper.Anti_Analysis.DetectManufacturer` | `0x4034a0` | 316 | ✓ |
| `method.Client.Connection.ClientSocket.Send` | `0x402f24` | 312 | ✓ |
| `method.Client.Handle_Packet.Packet.Invoke` | `0x403fd4` | 288 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.Encode2Stream` | `0x4053c8` | 248 | ✓ |
| `entry0` | `0x402608` | 240 | ✓ |
| `method.Client.Helper.Methods.Antivirus` | `0x403990` | 236 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.WriteMap` | `0x40475c` | 200 | ✓ |
| `method.MessagePackLib.MessagePack.WriteTools.WriteString` | `0x405604` | 200 | ✓ |
| `method.MessagePackLib.MessagePack.ReadTools.ReadString` | `0x405544` | 192 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.ForcePathObject` | `0x404c10` | 188 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.WirteArray` | `0x404824` | 180 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.GetAsBytes` | `0x404abc` | 176 | ✓ |
| `method.Client.Settings..cctor` | `0x4028c0` | 172 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.GetAsUInt64` | `0x4048d8` | 168 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.GetAsInteger` | `0x404980` | 168 | ✓ |
| `method.MessagePackLib.MessagePack.WriteTools.WriteBinary` | `0x4056cc` | 160 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.GetAsFloat` | `0x404a28` | 148 | ✓ |
| `sym.Client.Algorithm.Sha256.ComputeHash` | `0x4044b4` | 140 | ✓ |
| `method.MessagePackLib.MessagePack.Zip.Decompress` | `0x4058e0` | 140 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Client.Algorithm.Aes256.Decrypt.c`](code/method.Client.Algorithm.Aes256.Decrypt.c)
- [`code/method.Client.Algorithm.Aes256.Encrypt.c`](code/method.Client.Algorithm.Aes256.Encrypt.c)
- [`code/method.Client.Connection.ClientSocket.InitializeClient.c`](code/method.Client.Connection.ClientSocket.InitializeClient.c)
- [`code/method.Client.Connection.ClientSocket.ReadServertData.c`](code/method.Client.Connection.ClientSocket.ReadServertData.c)
- [`code/method.Client.Connection.ClientSocket.Send.c`](code/method.Client.Connection.ClientSocket.Send.c)
- [`code/method.Client.Handle_Packet.Packet.Invoke.c`](code/method.Client.Handle_Packet.Packet.Invoke.c)
- [`code/method.Client.Handle_Packet.Packet.Read.c`](code/method.Client.Handle_Packet.Packet.Read.c)
- [`code/method.Client.Helper.Anti_Analysis.DetectManufacturer.c`](code/method.Client.Helper.Anti_Analysis.DetectManufacturer.c)
- [`code/method.Client.Helper.IdSender.SendInfo.c`](code/method.Client.Helper.IdSender.SendInfo.c)
- [`code/method.Client.Helper.Methods.Antivirus.c`](code/method.Client.Helper.Methods.Antivirus.c)
- [`code/method.Client.Install.NormalStartup.Install.c`](code/method.Client.Install.NormalStartup.Install.c)
- [`code/method.Client.Settings..cctor.c`](code/method.Client.Settings..cctor.c)
- [`code/method.Client.Settings.InitializeSettings.c`](code/method.Client.Settings.InitializeSettings.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.DecodeFromStream.c`](code/method.MessagePackLib.MessagePack.MsgPack.DecodeFromStream.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.Encode2Stream.c`](code/method.MessagePackLib.MessagePack.MsgPack.Encode2Stream.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.ForcePathObject.c`](code/method.MessagePackLib.MessagePack.MsgPack.ForcePathObject.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.GetAsBytes.c`](code/method.MessagePackLib.MessagePack.MsgPack.GetAsBytes.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.GetAsFloat.c`](code/method.MessagePackLib.MessagePack.MsgPack.GetAsFloat.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.GetAsInteger.c`](code/method.MessagePackLib.MessagePack.MsgPack.GetAsInteger.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.GetAsUInt64.c`](code/method.MessagePackLib.MessagePack.MsgPack.GetAsUInt64.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.WirteArray.c`](code/method.MessagePackLib.MessagePack.MsgPack.WirteArray.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.WriteMap.c`](code/method.MessagePackLib.MessagePack.MsgPack.WriteMap.c)
- [`code/method.MessagePackLib.MessagePack.ReadTools.ReadString.c`](code/method.MessagePackLib.MessagePack.ReadTools.ReadString.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteBinary.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteBinary.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteInteger.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteInteger.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteString.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteString.c)
- [`code/method.MessagePackLib.MessagePack.Zip.Compress.c`](code/method.MessagePackLib.MessagePack.Zip.Compress.c)
- [`code/method.MessagePackLib.MessagePack.Zip.Decompress.c`](code/method.MessagePackLib.MessagePack.Zip.Decompress.c)
- [`code/sym.Client.Algorithm.Sha256.ComputeHash.c`](code/sym.Client.Algorithm.Sha256.ComputeHash.c)

## Behavioral Analysis

The additional disassembly from chunk 3/3 provides critical insights into the malware's **data handling, payload management, and delivery infrastructure.** These findings significantly elevate the threat profile from a standard Remote Access Trojan (RAT) to a **multi-functional loader and data exfiltration engine.**

Below is the updated analysis incorporating these new findings.

---

### Updated Analysis of Malware Sample

#### 1. Advanced Data Packaging & Exfiltration Capabilities
The inclusion of `WriteBinary`, `GetAsBytes`, and `WriteArray` within the MessagePack library confirms that the malware is designed to handle complex, non-text data structures:
*   **Binary Data Handling:** The existence of `WriteBinary` and `GetAsBytes` indicates that the bot can transmit "blobs" of data. In a RAT context, this means it can exfiltrate raw files (e.g., PDFs, images), system logs, or even full memory dumps without converting them to text first.
*   **Complex Data Mapping:** The `WriteArray` and `ForcePathObject` functions suggest the malware can organize these data pieces into structured arrays. This allows it to send complex "packets" (e.g., a zip file consisting of multiple segments, or a folder structure being exfiltrated).

#### 2. Evidence of a Multi-Stage Payload Loader
The discovery of `method.MessagePackLib.MessagePack.Zip.Decompress` is a critical finding for incident responders:
*   **Compressed Delivery:** The malware likely receives compressed data from its Command & Control (C2) server to save bandwidth and evade Network Intrusion Detection Systems (NIDS). Because the payload is "packed" or zipped, traditional security appliances may not recognize the signature of the malicious code until it is decompressed in memory.
*   **In-Memory Execution:** This suggests that the primary malicious functionality might be "hidden" inside a compressed blob, which this loader unpacks and executes on the victim's machine.

#### 3. Integrity Verification & Validation
The `sym.Client.Algorithm.Sha256.ComputeHash` function serves as a security check for the attacker:
*   **Payload Validation:** The malware likely uses SHA-256 to verify that a downloaded module or tool has not been corrupted during transit or tampered with by a security researcher.
*   **Communication Integrity:** It may also be used to generate "handshake" hashes to ensure the communication between the victim and the C2 is stable and consistent.

#### 4. Sophisticated Code Obfuscation (Anti-Analysis)
The disassembly for common types (e.g., `GetAsInteger`, `GetAsFloat`, `ReadString`) shows an extremely high level of "noisy" code:
*   **Instruction Substitution:** The repetitive use of `CONCAT`, `POPCOUNT`, and complex bitwise operations to perform simple additions or assignments is a classic technique used to break **automated decompilation**. 
*   **Intentional Complexity:** By making standard library functions appear complex and convoluted, the developers force an analyst to spend significantly more time manually reversing "boilerplate" code before they can reach the actual malicious logic.

---

### Updated Summary of Tactics & Techniques

The integration of these final components confirms that this is a **high-sophistication, multi-functional malware framework**. 

**New Technical Capabilities Identified:**
*   **Payload Loader Functionality:** Through `Zip.Decompress`, it can act as a "dropper" or "loader," pulling in and unpacking additional malicious modules.
*   **High-Volume Data Exfiltration:** By using `WriteBinary` within the MessagePack framework, it is optimized for moving large amounts of data (files/blobs) rather than just simple chat commands.
*   **Validation & Integrity Checks:** Using `Sha256` ensures that only "approved" payloads are executed by the bot, allowing the attacker to manage a fleet of bots with high reliability.
*   **Anti-Decompilation Tactics:** The deliberate obfuscation of standard data types indicates a developer who is intentionally trying to stall and frustrate security researchers.

### Final Conclusion
This sample is characteristic of **professional cybercrime operations (e.g., Ransomware gangs or specialized Spyware groups).** It is designed for:
1.  **Stealthy persistence** via its advanced anti-analysis checks.
2.  **Robust communication** through AES and MessagePack.
3.  **Extensive functionality** by serving as a gateway (loader) for other, more specialized pieces of malware delivered over an encrypted channel.

---

### Updated Recommendations for Defense & Response

*   **Deep Packet Inspection (DPI):** Since the malware uses **MessagePack**, standard "plain-text" filters will fail. Security teams should look for high volumes of outbound traffic to unusual ports using the MessagePack structure if possible.
*   **Memory Forensics:** Because the `Zip.Decompress` function implies that the most dangerous actions might occur only *after* decompression in memory, standard disk-based scanning may miss subsequent stages of the attack. Perform memory dumps on suspected infected machines.
*   **Payload Identification:** Identify and block the specific compressed payloads being delivered via the loader to prevent the "second stage" of the infection from occurring.
*   **C2 Infrastructure Takedown:** The complexity of this code suggests a stable, high-value infrastructure. Reporting the C2 IP addresses/domains associated with these specific `MessagePack` and `Sha256` routines is highly recommended for community-wide defense.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1041 | Exfiltration Over C2 Channel | The use of `WriteBinary` and `GetAsBytes` indicates the capability to exfiltrate non-text "blobs" (files, images, or memory dumps) directly through the communication channel. |
| T1027 | Obfuscated Files or Programs | The inclusion of `Zip.Decompress` suggests that malicious payloads are packaged in compressed archives to bypass signature-based detection and hide functionality until execution. |
| T1105 | Ingress Tool Transfer | The multi-stage loader functionality indicates the malware is designed to fetch and "drop" additional, more specialized tools or modules from the C2 server. |
| T1027 | Obfuscated Files or Programs | The use of instruction substitution (e.g., using complex bitwise logic for simple additions) is a deliberate attempt to hinder automated decompilation and manual analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   **Google Keep.exe** (Note: Likely used as a masquerading filename for the primary executable or a dropped component).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   `1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B` (SHA-256)
*   `87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F` (SHA-256)

**Other artifacts**
*   **C2 Communication Protocol:** Use of **MessagePack** for data serialization/deserialization.
*   **Anti-Analysis Techniques:** 
    *   `DetectSandboxie` (Detection of sandbox environments).
    *   Use of `Sha256Managed` for integrity checks on remote payloads.
*   **Payload Delivery:** Use of `Zip.Decompress` to unpack hidden/compressed modules in memory.
*   **Encryption:** Usage of **AES-256** and `CryptoStream`.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1.  **Malware family**: **custom** (likely a modular framework used by a professional cybercrime group)
2.  **Malware type**: **loader / RAT**
3.  **Confidence**: **High**
4.  **Key evidence**:
    *   **Multi-Stage Loader Capabilities:** The presence of `Zip.Decompress` and `Sha256` verification confirms the malware is designed to fetch, decompress, and verify additional malicious modules in memory, which is characteristic of a sophisticated loader used to deliver secondary payloads.
    *   **Advanced Data Exfiltration:** The integration of the MessagePack library with `WriteBinary` and `GetAsBytes` indicates it is built for high-volume data exfiltration (e.g., files, images, or system dumps) rather than simple text-based command execution.
    *   **Professional Anti-Analysis/Evasion:** The use of "noisy" instruction substitution to thwart decompilers, combined with masquerading as a legitimate application ("Google Keep.exe") and the use of AES encryption, points toward a professional development cycle aimed at high-value targets.
