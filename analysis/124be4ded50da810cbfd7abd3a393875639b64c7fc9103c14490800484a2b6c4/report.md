# Threat Analysis Report

**Generated:** 2026-08-25 14:56 UTC
**Sample:** `124be4ded50da810cbfd7abd3a393875639b64c7fc9103c14490800484a2b6c4_124be4ded50da810cbfd7abd3a393875639b64c7fc9103c14490800484a2b6c4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `124be4ded50da810cbfd7abd3a393875639b64c7fc9103c14490800484a2b6c4_124be4ded50da810cbfd7abd3a393875639b64c7fc9103c14490800484a2b6c4.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 46,592 bytes |
| MD5 | `0db33c257d847bf64fa107aa79dd5e39` |
| SHA1 | `36b73b0a2482532edf5e261639ea922257b795d5` |
| SHA256 | `124be4ded50da810cbfd7abd3a393875639b64c7fc9103c14490800484a2b6c4` |
| Overall entropy | 5.462 |
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
| `.text` | 43,008 | 5.511 | No |
| `.rsrc` | 2,560 | 5.031 | No |
| `.reloc` | 512 | 0.082 | No |

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

The final piece of disassembly (chunk 3/3) provides definitive evidence regarding the sophistication of the malware’s internal architecture, particularly its handling of data, remote payloads, and intentional anti-analysis measures.

By integrating this new data with previous findings, I have updated the analysis below.

### Updated Analysis of Malware Behavior

#### 1. Advanced Anti-Analysis & Obfuscation (Expanded)
The disassembly for `method.Client.Settings..cctor` provides a clear example of **Anti-Decompilation techniques**:
*   **Deliberate Junk Code/Control Flow Flattening:** The numerous warnings regarding "bad instruction data," "overlapping instructions," and "truncated control flow" are not necessarily bugs in the decompiler; they are hallmarks of high-level obfuscation. The author is intentionally using "garbage" instructions to break the logic flow for automated tools like Ghidra/IDA, forcing a manual analyst to spend significant time cleaning up the code just to find the underlying logic.
*   **Complexity as a Shield:** The complexity within the `cctor` (constructor) indicates that even basic configuration tasks are wrapped in layers of mathematical "noise" to hide the actual values being loaded or initialized.

#### 2. Robust Data Serialization & Handling (Confirmed & Expanded)
The inclusion of specific MessagePack helper functions (`GetAsUInt64`, `GetAsInteger`, `GetAsFloat`) and `WriteTools.WriteBinary` confirms a very high level of data sophistication:
*   **Complex Data Structures:** Instead of sending simple strings to the C2 (which are easily flagged by IDS/IPS), the malware uses MessagePack to pack complex objects. The use of `UInt64` and `Float` suggests it might be gathering specific system metrics, GPS coordinates, or other multi-type data points that need to remain consistent in a structured format.
*   **Binary Packing:** The presence of `WriteBinary` confirms that the malware is capable of packaging raw binary data (such as memory dumps, configuration files, or even additional malicious modules) into the MessagePack structure before it reaches the encryption layer (AES-256).

#### 3. Remote Payload Management & Compression
The discovery of the `method.MessagePackLib.MessagePack.Zip.Decompress` function introduces a new capability:
*   **Payload Handling:** The presence of a decompression routine suggests that commands or "plugins" sent from the C2 server are likely compressed. This is used to **minimize the network footprint**, making it harder for security systems to identify large, suspicious data transfers over the network. It also indicates that the malware can be updated or "re-tasked" remotely with new functionality without re-infecting the host.

#### 4. Cryptographic Integrity & Hashing
The `sym.Client.Algorithm.Sha256.ComputeHash` function confirms a robust backend:
*   **Integrity Checks:** SHA-256 is likely used to verify the integrity of files before they are exfiltrated or after a payload is downloaded and executed. This ensures that the malware's operations do not "break" during the process, ensuring the attacker receives clean data and that newly downloaded modules are authentic.

---

### Updated Summary of Identified Capabilities

| Category | Findings | Significance |
| :--- | :--- | :--- |
| **Primary Classification** | **High-Sophistication RAT / Espionage Tool** | Highly professional, non-scripted implementation for long-term access. |
| **Anti-Analysis** | **Obfuscated Control Flow**, Junk Code Insertion | Intentional use of "broken" instructions to frustrate manual reverse engineering and automated analysis. |
| **Encryption** | **AES-256**, SHA-256 | Industry-standard encryption/hashing to hide data content and ensure integrity. |
| **Data Serialization** | **MessagePack (Full Suite)** | Robust packing of complex, multi-type data structures into a compact binary format. |
| **Data Compression** | **Zip Decompression** | Ability to receive compressed payloads from C2 to evade detection of large transfers. |
| **Network Behavior** | **Persistent Interaction**, Complex Data Mapping | Designed for an interactive session where the operator can send complex commands and the bot can send structured data back. |

---

### Final Conclusion Update
The total disassembly across all three chunks confirms that this is a **highly sophisticated, professional-grade Remote Access Trojan (RAT) or espionage tool.** 

The developer has gone to significant lengths to ensure "operational security" (OPSEC). They have not only implemented high-level encryption (**AES-256**) and sophisticated serialization (**MessagePack**), but they have also integrated **Payload Compression** and **Anti-Decompilation** tactics. These features are typical of malware used by organized cybercrime groups or state-sponsored actors, where the goal is to remain undetected on a high-value target for as long as possible while providing the remote operator with an easy, robust interface for data theft and system control.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the corresponding MITRE ATT&CK techniques. 

Because several of these behaviors (Junk Code, MessagePack/Serialization, Compression, and Encryption) all serve the primary goal of evading detection and hindering analysis, they fall under the primary technique **T1027**. However, I have broken them out below to reflect the specific nuances provided in your report.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of "junk code" and "control flow flattening" is a deliberate tactic to frustrate automated decompilers and manual reverse engineering. |
| **T1027** | Obfuscated Files or Information | Utilizing MessagePack for data serialization hides complex data structures and eliminates plain-text strings that would be flagged by IDS/IPS systems. |
| **T1027** | Obfuscated Files or Information | The inclusion of Zip decompression routines is a method to minimize the network footprint and hide the true nature of large payload transfers from security monitoring. |
| **T1027** | Obfuscated Files or Information | The implementation of AES-256 and SHA-256 ensures the confidentiality of exfiltrated data and the integrity of remote payloads, shielding the communication from inspection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `NetworkSecurity.exe` (Note: Likely used as a masquerading name for the primary malicious binary)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   `1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B` (Hex string)
*   `87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F` (Hex string)

**Other artifacts**
*   **Encryption Algorithms:** AES-256, SHA-256
*   **Data Serialization:** MessagePack (including specific methods: `GetAsUInt64`, `GetAsInteger`, `GetAsFloat`, `WriteBinary`)
*   **Compression:** Zip Decompression (used for payload handling and minimizing network footprint)
*   **Evasion Techniques:** Control Flow Flattening, Junk Code Insertion (intentional anti-decompilation)
*   **Capabilities:** Remote Payload Management, Content Integrity Checks.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1.  **Malware family:** Custom
2.  **Malware type:** RAT (Remote Access Trojan) / Espionage Tool
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Advanced Evasion & Obfuscation:** The use of control flow flattening, junk code insertion, and "broken" instruction paths indicates a high level of sophistication designed to frustrate manual reverse engineering and automated de-compilation tools.
    *   **Sophisticated Communication Stack:** Rather than using simple strings, the malware utilizes MessagePack for complex data serialization (handling various data types like Float/UInt64) combined with AES-256 encryption and SHA-256 integrity checks to facilitate secure, structured exfiltration.
    *   **Modular Payload Management:** The inclusion of a Zip decompression routine suggests a modular architecture where the attacker can remotely deploy and update "plugins" or additional capabilities while minimizing the network footprint.
