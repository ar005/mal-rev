# Threat Analysis Report

**Generated:** 2026-07-30 05:42 UTC
**Sample:** `0c5d83d8f55e9cfc9f2f2d70f11212b74a4550e8fe9d3a557243c1d31a97e13e_0c5d83d8f55e9cfc9f2f2d70f11212b74a4550e8fe9d3a557243c1d31a97e13e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c5d83d8f55e9cfc9f2f2d70f11212b74a4550e8fe9d3a557243c1d31a97e13e_0c5d83d8f55e9cfc9f2f2d70f11212b74a4550e8fe9d3a557243c1d31a97e13e.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 47,616 bytes |
| MD5 | `2bf85f342cd0b34fe34b309253484d7f` |
| SHA1 | `cdc62191a059670680add08fe91d54ce20771131` |
| SHA256 | `0c5d83d8f55e9cfc9f2f2d70f11212b74a4550e8fe9d3a557243c1d31a97e13e` |
| Overall entropy | 5.435 |
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
| `.text` | 43,520 | 5.498 | No |
| `.rsrc` | 3,072 | 4.803 | No |
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

	rj'
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

Functions analyzed: **30** | Decompiled to C: **29**

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

This is the final update to your analysis based on **chunk 3/3** of the disassembly. This final segment provides significant details regarding the depth of the malware's communication protocol, its internal configuration handling, and the advanced evasion techniques used to frustrate researchers.

### Updated Analysis of Capabilities

#### 1. Granular Data Serialization (MessagePack)
The third chunk reveals that the use of **MessagePack** is not just for basic "packaging," but for a very robust and flexible data exchange format:
*   **Multi-type Handling:** The presence of `WriteMap`, `WriteString`, `GetAsUInt64`, `GetAsInteger`, and `GetAsFloat` confirms that the malware can transport complex, structured objects. 
    *   *Implication:* Instead of just sending raw text, it can send a "dictionary" of information (e.g., `{ "user_id": 12345, "ip_address": "xxx.xxx.xxx.x", "system_status": "active"}`).
*   **Versatility:** Supporting floats and long integers suggests the malware may be capable of reporting complex telemetry or coordinates (if it's part of a multi-user environment).

#### 2. Advanced Anti-Analysis & Obfuscation
This chunk provides some of the strongest evidence yet of intentional "anti-research" measures:
*   **Overlapping Instructions/Junk Code:** The disassembly contains multiple warnings regarding **"Control flow encountered bad instruction data"** and **"instruction... overlaps."** 
    *   *Significance:* These are common tactics used by malware authors to break disassemblers (like IDA Pro or Ghidra). By overlapping instructions, the author forces the tool to misinterpret the code's logic, making it much harder for a human researcher to follow the execution flow.
*   **Sophisticated Execution Path:** The repeated "bad instruction" flags in the MessagePack routines suggest that even the data-handling portion of the code is intentionally obfuscated to hide what specific types of data are being collected and sent.

#### 3. Internal Configuration & Local Interaction
The `method.Client.Settings..cctor` (constructor) section reveals how the bot initializes itself:
*   **Configuration Loading:** The constructor indicates a process for loading "settings." This usually involves reading a hardcoded or encrypted configuration file that contains C2 server addresses, port numbers, and specific command instructions.
*   **Targeted Activity:** The inclusion of `GetForegroundWindow` in the `NativeMethods` suggests that the malware might have logic to check what the user is currently doing. 
    *   *Potential Use:* A "smart" RAT might only activate certain features (like keylogging or screen scraping) if a specific application (like a banking site or an internal corporate tool) is in the foreground.

#### 4. Integrity and Verification (SHA-256)
The inclusion of `method.Client.Algorithm.Sha256.ComputeHash` confirms a high level of cryptographic awareness:
*   **Payload Integrity:** The malware likely uses SHA-256 to verify that any secondary payloads downloaded from the C2 server are "correct" (not tampered with by security researchers).
*   **Duplicate Prevention:** It may be used to hash files on the local system before exfiltration; if a file's hash has already been sent, the malware won't waste bandwidth sending it again.

---

### Final Summary of Findings

This binary is highly indicative of a **professional-grade Remote Access Trojan (RAT) or sophisticated Command & Control (C2) agent.** 

The evidence for this conclusion is summarized below:

1.  **Robust Communication Suite:** The combination of **AES-256**, **MessagePack**, and **SHA-256** ensures that all communications are encrypted, structured for easy parsing by the attacker, and verified to prevent tampering.
2.  **Intentional Anti-Analysis Layer:** The presence of "overlapping instructions" is a high-level obfuscation technique specifically designed to hinder automated tools and human reverse engineers. This suggests an author who understands the standard techniques used by security professionals.
3.  **Sophisticated Persistence & Configuration:** The existence of a `Settings` constructor implies a modular design where the bot’s behavior can be updated or changed remotely via an encrypted configuration file without needing to re-infect the machine.
4.  **Context-Aware Execution:** Features like `GetForegroundWindow` suggest the malware is designed for high-value targets, potentially only performing malicious actions when certain conditions are met (e.g., during a specific work hour or while a specific app is open).

### Final Conclusion
The binary is **highly malicious.** It is not a simple "script kiddie" tool; it was developed with a focus on durability and evasion. Its design allows an attacker to maintain a persistent, stealthy presence on a compromised machine, provide complex remote instructions, and exfiltrate high volumes of structured data while actively evading detection by both automated tools and manual analysis.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1131** | Data Encoding | The use of MessagePack for multi-type data serialization and SHA-256 for integrity checks indicates a concerted effort to structure, package, and verify data before transmission. |
| **T1027** | Obfuscated Files | The inclusion of overlapping instructions and "junk" code is a specific technique designed to break disassemblers and hinder human reverse engineering. |
| **T1611** | System Information Discovery | The use of `GetForegroundWindow` indicates the malware is gathering environmental context to determine when it is appropriate to activate its features. |
| **T1071** | Application Layer Protocol | The sophisticated combination of AES-256, MessagePack, and custom "Settings" handling suggests a robust, structured communication protocol for C2 operations. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided string extractions and behavioral analysis. Below are the identified Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **AGTApexPrime.exe** (Identified as the primary malicious binary/module name)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
The following hex strings were identified in the code; these may represent internal identifiers, specific hardcoded keys, or SHA-256 hashes of components:
*   `1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B`
*   `87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F`

### **Other artifacts**
*   **C2/Communication Protocols:** 
    *   **MessagePack:** Used for structured, multi-type data serialization (highly indicative of complex C2 instructions).
    *   **AES-256:** Used for encrypting communication.
    *   **SHA-256:** Utilized for payload integrity verification and potential duplicate detection.
*   **Evasion Techniques:** 
    *   **Overlapping Instructions / Junk Code:** Intentionally used to break disassembler tools (e.g., IDA Pro, Ghidra).
*   **Behavioral Artifacts:**
    *   **GetForegroundWindow:** Used for context-aware execution (triggering actions only when specific applications are in focus).
    *   **Dynamic Configuration:** The presence of `method.Client.Settings..cctor` suggests the malware loads its operational parameters from an encrypted/hidden configuration file.

---

## Malware Family Classification

1. **Malware family:** custom
2. **Malware type:** RAT (Remote Access Trojan) / Backdoor
3. **Confidence:** High

4. **Key evidence:**
*   **Sophisticated C2 Infrastructure:** The combination of AES-256 encryption, MessagePack serialization for complex data structures, and SHA-256 integrity checks indicates a professional-grade communication protocol designed for robust, multi-function remote commands.
*   **Advanced Anti-Analysis Techniques:** The use of "overlapping instructions" and junk code is a deliberate tactic to break automated disassemblers (like IDA Pro/Ghidra), demonstrating an intent to frustrate manual reverse engineering by skilled researchers.
*   **Context-Aware Execution:** The inclusion of `GetForegroundWindow` suggests the malware performs "smart" logic, potentially only activating malicious modules (such as keylogging or screen scraping) when a specific target application is in focus, typical of high-end RATs targeting corporate environments.
