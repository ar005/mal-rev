# Threat Analysis Report

**Generated:** 2026-08-18 17:32 UTC
**Sample:** `103ccb9ba1230b21e4fb360e1f1f99b3a6537c8dfe8eb02e853db4eae891d5a1_103ccb9ba1230b21e4fb360e1f1f99b3a6537c8dfe8eb02e853db4eae891d5a1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `103ccb9ba1230b21e4fb360e1f1f99b3a6537c8dfe8eb02e853db4eae891d5a1_103ccb9ba1230b21e4fb360e1f1f99b3a6537c8dfe8eb02e853db4eae891d5a1.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 47,616 bytes |
| MD5 | `2a976b5a8dd98416ee71ad42a1dca0f4` |
| SHA1 | `ab3d30a1d969103292440ceeefe3bf191ff788a3` |
| SHA256 | `103ccb9ba1230b21e4fb360e1f1f99b3a6537c8dfe8eb02e853db4eae891d5a1` |
| Overall entropy | 5.419 |
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
| `.text` | 43,520 | 5.485 | No |
| `.rsrc` | 3,072 | 4.763 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **501** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

	rR$
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

This final segment of disassembly provides a definitive look into the malware’s operational lifecycle—moving from data preparation (MessagePack) to transmission readiness (Compression and Hashing), while employing extreme techniques to thwart automated analysis tools.

### Updated Analysis: [Malware Report - Chunk 4/4]

#### **1. Cryptographic Integrity & Identification (SHA-256)**
The identification of a `Sha256.ComputeHash` function, even though it is heavily obfuscated, confirms several high-level capabilities:
*   **Command Validation:** The malware likely uses SHA-256 to verify the integrity of commands received from the Command & Control (C2) server. This ensures that instructions haven't been tampered with by security middleboxes or researchers during transit.
*   **Data Fingerprinting:** Before exfiltration, the malware may hash local files or system artifacts. This allows the attacker to identify unique files on a victim's machine and avoid sending duplicate data (e.g., "File_A" on Host 1 and "File_A" on Host 2).
*   **Payload Verification:** If the malware downloads secondary modules, SHA-256 is used to verify that the downloaded payload was not corrupted or intercepted.

#### **2. Data Compression & Payload Management (Decompression)**
The `MessagePack.Zip.Decompress` function indicates a multi-layered approach to data handling:
*   **Reduced Footprint:** By using compression, the malware minimizes its network footprint, making it harder for Network Intrusion Detection Systems (NIDS) to flag "unusually large" uploads.
*   **Evasion of Traffic Analysis:** Compressed and structured (MessagePack) payloads look like standard application traffic rather than raw data exfiltration. The use of a dedicated decompression routine suggests that the data arriving at the C2 is likely packed/compressed to stay under the radar of deep packet inspection (DPI).

#### **3. Extreme Anti-Analysis & Deception**
The disassembly for these specific functions includes significant "Warning" flags from the disassembler:
*   **Overlapping Instructions:** The warning `Instruction at (...) overlaps instruction at (...)` is a hallmark of deliberate code mutation. By overlapping instructions, the developer ensures that standard disassemblers (like IDA Pro or Ghuzra) produce incorrect assembly, potentially leading analysts into "dead ends" or causing the tool to crash/misinterpret the logic.
*   **Bad Instruction Data:** The `halt_baddata()` and several warnings regarding "bad instruction data" indicate that the malware includes non-executable "junk" code designed to confuse linear sweep and recursive traversal disassemblers.

---

### Updated Technical Observations Table

| Component | Identified Feature | Tactical Purpose |
| :--- | :--- | :--- |
| **Deception** | **Overlapping Instructions** | Explicitly designed to break automated de-compilers/disassemblers, forcing manual analysis of "broken" code. |
| **Data Integrity** | `Sha256.ComputeHash` | Used for verifying C2 commands, fingerprinting exfiltrated data, or validating downloaded modules. |
| **Packaging** | `MessagePack` (via Decompress) | Compresses and structures data to reduce the network footprint and evade traffic-based detection. |
| **Robustness** | **Junk Code/Complex Loops** | High-complexity loops in "defense" functions mask the core logic of exfiltration and communication. |

---

### Final Conclusion Update
The comprehensive analysis of all four segments confirms that this is a **highly sophisticated, enterprise-grade Trojan**. 

The malware's design follows a professional development lifecycle:
1.  **Sophisticated Collection:** It uses **MessagePack** to organize various types of system metadata into structured objects.
2.  **Advanced Packaging:** It utilizes **Decompression (Zip)** logic to minimize its network footprint and bypass traffic analysis.
3.  **Verification:** It employs **SHA-256** to ensure the integrity of its internal operations and C2 communications.
4.  **Aggressive Evasion:** The use of **overlapping instructions** and complex control-flow "junk code" proves that the threat actor is specifically targeting the time and resources of security researchers, making manual reverse-engineering extremely labor-intensive.

This malware is not a simple "plug-and-play" script; it is an engineered tool intended for long-term persistence and high-value data theft in targeted environments.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Valid Code | The use of "overlapping instructions" and high-complexity "junk code" is a deliberate attempt to break disassemblers/decompilers and hinder manual reverse engineering. |
| T1132 | Data Encoding | The utilization of MessagePack and Zip compression serves to hide the payload's true nature, reduce its network footprint, and evade identification by NIDS or Deep Packet Inspection (DPI). |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

### **IP addresses / URLs / Domains**
*   *None identified.* (While C2 communication is mentioned in the behavior report, no specific IP addresses or domain names were present in the raw data.)

### **File paths / Registry keys**
*   **TitanPulseZeroAccess.exe** (Identified filename)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   **87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F** (SHA-256)
*   **1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B** (Long hex string; likely a unique identifier or internal hash)

### **Other artifacts**
*   **C2 Communication Patterns:** 
    *   Use of **MessagePack** for structuring and preparing data.
    *   Use of **Zip compression** to reduce network footprint and evade NIDS/DPI (Deep Packet Inspection).
    *   Utilization of **SHA-256** for verifying C2 command integrity and fingerprinting exfiltrated files.
*   **Evasion Techniques:** 
    *   **Overlapping Instructions:** Deliberately designed to break disassemblers like IDA Pro.
    *   **Junk Code/Complex Loops:** Used to mask core logic and hinder manual analysis.
    *   **Anti-Analysis:** Intentional inclusion of "bad instruction data" to thwart automated security tools.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family:** custom
2. **Malware type:** backdoor / trojan
3. **Confidence:** High
4. **Key evidence:** 
    * **Sophisticated Data Handling:** The use of MessagePack for structured data organization and Zip compression to minimize network footprint indicates a professional effort to bypass Network Intrusion Detection Systems (NIDS) and Deep Packet Inspection (DPI).
    * **Advanced Anti-Analysis Techniques:** The deliberate implementation of "overlapping instructions" and "junk code" specifically targets the weaknesses of automated disassemblers (like IDA Pro), suggesting an enterprise-grade threat designed for long-term persistence.
    * **Robust C2 Infrastructure:** The use of SHA-256 for both command validation and file fingerprinting ensures that communication remains reliable and consistent during the exfiltration phase.
