# Threat Analysis Report

**Generated:** 2026-09-04 18:41 UTC
**Sample:** `1424940ec6af15c735a6a67737d7c7c5851a905c2e98f06646d6564b9bf55d34_1424940ec6af15c735a6a67737d7c7c5851a905c2e98f06646d6564b9bf55d34.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1424940ec6af15c735a6a67737d7c7c5851a905c2e98f06646d6564b9bf55d34_1424940ec6af15c735a6a67737d7c7c5851a905c2e98f06646d6564b9bf55d34.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 46,592 bytes |
| MD5 | `f0ce6a5d7ea6f393e4eb7679b7e06d28` |
| SHA1 | `51c8ef6b21cc3e2181be0c65a88d6b23eb906bac` |
| SHA256 | `1424940ec6af15c735a6a67737d7c7c5851a905c2e98f06646d6564b9bf55d34` |
| Overall entropy | 5.447 |
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
| `.text` | 43,008 | 5.51 | No |
| `.rsrc` | 2,560 | 4.807 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **499** (showing first 100)

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

Based on the third chunk of disassembly, I have finalized and further refined the analysis. The addition of decompression routines and specific evidence of deliberate anti-decompiler techniques confirms this is a highly sophisticated piece of malware with multiple layers of protection.

### Finalized Analysis Update

#### 1. Core Functionality (Finalized)
*   **Multi-Layered Data Processing:** The final chunk reveals the full pipeline for data handling:
    *   **Compression (`Zip.Decompress`):** The malware includes a decompression routine. This allows the attacker to send compressed modules, scripts, or configuration updates over the network, reducing the size of the traffic and making it harder for security analysts to spot "strings" or signatures in transit.
    *   **Serialization (MessagePack):** The comprehensive set of functions (`GetAsUInt64`, `GetAsInteger`, `GetAsFloat`) confirms that the malware handles complex, structured data. It isn't just sending simple commands; it is likely receiving entire "objects" or "scripts" from the C2 server.
    *   **Data Integrity (SHA-256):** The inclusion of `Sha256.ComputeHash` indicates a strict protocol for integrity. This ensures that files exfiltrated are intact and, more importantly, that any modules downloaded by the malware have not been tampered with or corrupted during transit.
*   **Modular Payload Execution:** The combination of **Decompression + MessagePack** suggests a "Plug-in" architecture. The malware can be updated remotely with new capabilities without changing the primary executable's footprint.

#### 2. Advanced Evasion & Anti-Analysis (Finalized)
The final disassembly provides definitive proof of high-effort anti-analysis measures:
*   **Anti-Decompiler/Anti-Disassembly:** Every major block in this chunk—including standard library functions like `GetAsInteger` and `GetAsFloat`—contains "overlapping instructions" and "bad instruction data."
    *   **Intent:** This is a classic technique to break the analysis flow of tools like IDA Pro or Gh1dra. By creating overlapping code, the developer ensures that an automated decompiler cannot produce a clean control-flow graph (CFG), forcing human analysts into hours of manual, tedious reconstruction of the logic.
*   **Complexity as Obfuscation:** The extremely "messy" look of the assembly (e.g., in `method.Client.Settings..cctor`) indicates that the code was passed through a specialized obfuscator designed to turn clean logic into a "spaghetti" of jumps and redundant instructions, making reverse engineering significantly more time-consuming.

#### 3. Network & Communication Infrastructure
*   **Sophisticated Pipeline:** The confirmed data flow is now: 
    **[Action] $\rightarrow$ [MessagePack Serialization] $\rightarrow$ [Zlib/Gzip Decompression (on receipt)] $\rightarrow$ [AES-256 Encryption] $\rightarrow$ [TCP/SSL_Transport]**.
*   **Sophisticated Command & Control:** The use of `GetAsFloat` and other typed data types suggests a high level of interaction. This malware is likely used for complex tasks, potentially including automated trading, advanced surveillance, or widespread botnet orchestration.

---

### Final Threat Intelligence Summary

| Feature | Finding | Risk Level |
| :--- | :--- | :--- |
| **Malware Type** | Advanced Remote Access Trojan (RAT) / Modular Botnet Agent | **Critical** |
| **Encryption** | AES-256 (Standard and robust) | **High** |
| **Serialization** | MessagePack (Supports complex data structures) | **High** |
| **Compression** | Integrated Decompression (`Zip.Decompress`) | **High** |
| **Data Integrity** | SHA-256 Hashing | **Medium** |
| **Anti-Analysis** | DetectManufacturer, Anti-AV, and Advanced Obfuscation | **Critical** |
| **Obfuscation** | Overlapping instructions & Junk Code (Anti-Decompiler) | **High** |

**Final Conclusion:**
This binary is a professional-grade piece of malware. The combination of **AES-256**, **MessagePack serialization**, and **built-in decompression** indicates that the threat actor is well-resourced and capable of maintaining long-term, stable access to infected hosts. The high level of anti-decompiler obfuscation suggests they are specifically targeting environments with active security monitoring and a desire to delay manual analysis by researchers.

**Recommendation:**
1.  **Network Level:** Implement SSL/TLS inspection to look for non-standard protocols wrapped in standard ports (e.g., 443). Identify and block IP addresses associated with high-frequency MessagePack traffic.
2.  **Endpoint Level:** Deploy EDR solutions capable of monitoring for "unusual" child processes or scripts being unpacked into memory, as the `Zip.Decompress` function suggests a dynamic execution model.
3.  **Incident Response:** Because of the **DetectManufacturer** and **Antivirus** checks, any host showing signs of this malware should be treated as having been targeted by a sophisticated actor; conduct a full sweep for other hidden persistence mechanisms (e.g., scheduled tasks or WMI event consumers).

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the relevant MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of Zip decompression, MessagePack serialization, and "spaghetti" code/overlapping instructions are all methods to hide strings, data structures, and control flow from static analysis. |
| **T1573** | Encrypted Channel | The implementation of AES-256 encryption over a TCP/SSL transport layer ensures that the communication between the malware and the C2 server remains opaque to network security monitoring. |
| **T1036** | Masquerading | (Contextual) The "Modular Payload" approach allows the malware to maintain a consistent footprint while dynamically changing capabilities, effectively masquerading as a single stable application while hiding its true functionality. |

### Analyst Notes:
*   **Regarding T1027:** This is the primary technique for the anti-analysis findings. By using overlapping instructions and "bad instruction data," the threat actor is specifically targeting the limitations of automated disassemblers (like IDA Pro or Ghidra), forcing a manual—and therefore much slower—reconstruction of the logic by human researchers.
*   **Regarding Modular Architecture:** While not a single specific MITRE technique, the modular nature described (using MessagePack and Decompression) is a hallmark of sophisticated RATs. It allows for "feature-on-demand" updates, which helps evade signature-based detection since the primary binary remains unchanged while payloads are updated over the wire.
*   **Regarding Network Infrastructure:** The combination of AES-256 and SSL/TCP (T1573) indicates a high level of operational security (OPSEC) by the threat actor, designed to bypass basic deep packet inspection (DPI).

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.* (The report mentions network protocols but does not provide specific infrastructure.)

**File paths / Registry keys**
*   `AF88.exe` (Malware executable filename)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   `1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B` (SHA-256)
*   `87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F` (SHA-256)

**Other artifacts**
*   **Anti-Analysis Techniques:** `DetectSandboxie` (specific check for Sandboxie environment).
*   **Communication Patterns:** 
    *   Use of **MessagePack** serialization for complex data structures.
    *   **AES-256** encryption for command/data traffic.
    *   **Zip.Decompress** (Zlib/Gzip) routine used for unpacking modules or scripts in memory.
    *   Non-standard protocols wrapped within standard ports (e.g., 443).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1.  **Malware family**: custom (Advanced Modular RAT)
2.  **Malware type**: RAT (Remote Access Trojan) / Botnet Agent
3.  **Confidence**: High
4.  **Key evidence**:
    *   **Modular Architecture:** The integration of **MessagePack serialization** and **Zip decompression** routines indicates a sophisticated "plug-in" model, allowing the attacker to push updates and new capabilities to the malware without altering the primary executable's signature.
    *   **Advanced Anti-Analysis:** The use of **overlapping instructions** and "bad instruction data" specifically designed to break automated decompilers (like IDA Pro/Ghidra) identifies this as a professional-grade tool intended to frustrate manual reverse engineering.
    *   **Robust Communication Pipeline:** The combination of **AES-256 encryption**, SHA-256 integrity checks, and complex data types suggests a highly stable, long-term infrastructure for remote access and command execution.
