# Threat Analysis Report

**Generated:** 2026-08-18 17:24 UTC
**Sample:** `103bf7cda93749567f7e16e48cd205fd059fdda7f7396a781c6e4a096a3b47d7_103bf7cda93749567f7e16e48cd205fd059fdda7f7396a781c6e4a096a3b47d7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `103bf7cda93749567f7e16e48cd205fd059fdda7f7396a781c6e4a096a3b47d7_103bf7cda93749567f7e16e48cd205fd059fdda7f7396a781c6e4a096a3b47d7.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 114,688 bytes |
| MD5 | `b669f2d36b0b71f614751ed3c4486c0b` |
| SHA1 | `d93d360643cd95ca8b2f2bbcf61b2fec5dc208f0` |
| SHA256 | `103bf7cda93749567f7e16e48cd205fd059fdda7f7396a781c6e4a096a3b47d7` |
| Overall entropy | 5.671 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1778247384 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 43,520 | 5.48 | No |
| `.rsrc` | 70,144 | 5.047 | No |
| `.reloc` | 512 | 0.061 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **500** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v4.0.30319
#Strings
Telegram (1)
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x40596c` | 49964 | ✓ |
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
| `method.MessagePackLib.MessagePack.Zip.Decompress` | `0x4058e0` | 140 | — |

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
- [`code/sym.Client.Algorithm.Sha256.ComputeHash.c`](code/sym.Client.Algorithm.Sha256.ComputeHash.c)

## Behavioral Analysis

This update incorporates the third and final disassembly chunk into the existing analysis. The new data provides significant evidence regarding the malware's internal data processing capabilities, its commitment to anti-analysis techniques, and the robustness of its communication infrastructure.

### Updated Analysis Summary

The sample is confirmed as a **high-tier, sophisticated network-based client/backdoor**. The latest disassembly highlights a "defense-in-depth" approach to development: using standard high-level libraries (MessagePack) for data handling, industry-standard cryptography (AES-256, SHA-256) for security, and aggressive anti-disassembly techniques to frustrate manual analysis.

---

### 1. Enhanced Obfuscation & Anti-Analysis
The most striking feature of this chunk is the consistent presence of **Anti-Disassembly** tactics across almost all functions (e.g., `cctor`, `GetAsUInt64`, `GetAsFloat`).

*   **Instruction Overlapping:** The "overlap" warnings indicate that the code is designed to be interpreted differently by a human/disassembler than by the CPU. By overlapping instructions, the developer creates "dead zones" and ambiguous jumps that can cause automated tools (like IDA Pro or Ghidra) to generate incorrect control flow graphs (CFG).
*   **Polymorphic-style Junk Code:** The complex arithmetic involving `POPCOUNT`, `CARRY` flags, and `CONCAT` operations in the `GetAs...` functions suggests a "mutation" of standard logic. This is designed to make it extremely tedious for an analyst to determine what a simple operation (like reading an integer) actually does.
*   **Hardened Initialization:** The obfuscation in `method.Client.Settings..cctor` is critical. Since this function typically loads the malware's configuration (C2 addresses, port numbers, and activity intervals), its protection suggests the developers want to hide the "heart" of the malware’s operations from initial triage.

### 2. Advanced Data Handling & Serialization
The disassembly for the `MessagePackLib` confirms a highly sophisticated approach to data management:

*   **Multi-Type Support:** The inclusion of specific handlers for `GetAsUInt64`, `GetAsInteger`, and `GetAsFloat` indicates that the malware is prepared to transport a wide variety of data types. This allows it to transmit complex objects (e.g., system metrics, file metadata, or geolocation coordinates) in a compact binary format.
*   **Efficient Transport:** By utilizing **MessagePack**, the malware achieves "compactness." Unlike JSON or XML, MessagePack minimizes the packet size, making the traffic less conspicuous to Network Intrusion Detection Systems (NIDS) that look for large, plain-text data headers.

### 3. Cryptographic Integrity & Validation
The inclusion of `sym.Client.Algorithm.Sha256.ComputeHash` provides a new layer of evidence regarding its sophistication:

*   **Integrity Checks:** While AES-256 (from previous chunks) ensures **secrecy**, SHA-256 is used for **integrity**. The malware likely uses this to verify that the instructions received from the C2 have not been tampered with by security middleboxes or automated "man-in-the-middle" (MITM) proxies.
*   **Payload Verification:** It may also be used to verify the integrity of any secondary payloads or modules downloaded from the server before they are executed on the victim's machine.

---

### Updated Technical Overview Table

| Feature | Implementation Detail | Significance |
| :--- | :--- | :--- |
| **Encryption** | `Aes256.Encrypt` | Ensures high-grade privacy for data exfiltration; bypasses NIDS/DPI. |
| **Integrity** | `Sha256.ComputeHash` | Validates the authenticity of C2 commands and ensures payload integrity. |
| **Serialization** | `MessagePackLib` (UInt, Int, Float) | Enables compact, multi-type data packaging to minimize network footprint. |
| **C2 Interaction** | `Packet.Invoke` / `ClientSocket.Send` | Provides a robust, two-way communication channel for remote commands. |
| **Anti-Analysis** | `DetectManufacturer`, `DetectSandboxie` | Identifies analysis environments and modifies behavior to evade detection. |
| **Anti-Disassembly**| Instruction Overlaps / Junk Code | Deliberately breaks the logic flow in tools like IDA Pro to slow down human analysts. |

---

### Final Conclusion
The final data confirms that this malware is not a simple "script-kiddie" tool; it is an **enterprise-grade malware suite**. 

By combining **MessagePack** (to hide data types), **AES-256 & SHA-256** (to secure the communication tunnel), and **Anti-Disassembly** techniques (to hinder reverse engineering), the threat actor has built a resilient platform designed for longevity. The sophistication of the code indicates a high level of investment in both the functionality of the backdoor and the difficulty of its analysis, making it highly effective at evading automated and manual security scrutiny.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the corresponding MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of instruction overlapping and junk code is specifically designed to hinder manual analysis and break automated disassembly tools like IDA Pro. |
| **T1562** | Impair Defenses | The inclusion of `DetectSandboxie` and `DetectManufacturer` indicates an attempt to detect, and therefore evade, security analysis environments. |
| **T1573** | Encrypted Channel | The implementation of AES-256 for secrecy and SHA-256 for integrity ensures the communication channel is protected from inspection and tampering. |
| **T1027** | Obfuscated Files or Information | MessagePack is utilized to provide a compact binary format, masking data structures and reducing the network footprint to evade NIDS detection. |
| **T1071** | Application Layer Protocol | The use of `Packet_Invoke` and `ClientSocket_Send` indicates the implementation of a structured protocol for command-and-control communication. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided string data and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*   *None identified in the provided text.*

### **File paths / Registry keys**
*   *None specific to system paths or registry hives were identified.* (Note: `DetectSandboxie` implies interaction with sandbox software, but no specific path was provided.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
The following 64-character hex strings were identified. Given their length and format, these are likely SHA-256 hashes or hardcoded cryptographic keys/identifiers:
*   `1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B`
*   `87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F`

### **Other artifacts**
*   **File Names:** 
    *   `Telegram (1).exe`
*   **C2 & Network Communication Patterns:**
    *   **Serialization Method:** Use of `MessagePackLib` to package multi-type data (UInt, Int, Float) into compact binary formats to evade NIDS/DPI.
    *   **Heartbeat Mechanism:** Logic for `<KeepAlive>`, `<Ping>`, and `<Interval>` indicates a persistent heartbeating communication channel.
    *   **Encryption Standards:** Utilization of `AES-256` for payload confidentiality and `SHA-256` for integrity checks on C2 commands.
*   **Anti-Analysis & Evasion Techniques:**
    *   **Sandbox Detection:** Implementation of `DetectSandboxie` and `GetActiveWindowTitle`.
    *   **Anti-Disassembly:** Use of "Instruction Overlapping" and "Junk Code" (specifically within the `GetAs...` functions) to break linear disassembly in tools like IDA Pro or Ghidra.
    *   **Environment Checks:** Usage of `get_MachineName`, `get_OSFullName`, and `get_Manufacturer`.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1.  **Malware family:** custom
2.  **Malware type:** backdoor
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Sophisticated Communication Infrastructure:** The use of MessagePack for serialization, combined with AES-256 and SHA-256 encryption/integrity checks, indicates a high-tier backdoor designed to bypass NIDS/DPI while maintaining a persistent connection (via Heartbeat/Ping mechanisms).
    *   **Advanced Anti-Analysis & Evasion:** The implementation of "Instruction Overlapping" and "Junk Code" specifically targets the failure of disassemblers like IDA Pro/Ghidra, while `DetectSandboxie` and `DetectManufacturer` checks indicate a deliberate effort to evade automated sandbox analysis.
    *   **Social Engineering Tactics:** The use of the filename `Telegram (1).exe` indicates an intent to masquerade as a legitimate communication application to deceive users into executing the malware.
