# Threat Analysis Report

**Generated:** 2026-07-16 17:55 UTC
**Sample:** `07506b483a2fe1276fe390fcd462b4ed91ebc28b7be39830b03771e998e2a6f1_07506b483a2fe1276fe390fcd462b4ed91ebc28b7be39830b03771e998e2a6f1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07506b483a2fe1276fe390fcd462b4ed91ebc28b7be39830b03771e998e2a6f1_07506b483a2fe1276fe390fcd462b4ed91ebc28b7be39830b03771e998e2a6f1.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 46,080 bytes |
| MD5 | `95d1f3f551726758afefd7d77374ad68` |
| SHA1 | `a292bcefc8f37a360ad7704077f8ecfa8a634300` |
| SHA256 | `07506b483a2fe1276fe390fcd462b4ed91ebc28b7be39830b03771e998e2a6f1` |
| Overall entropy | 5.442 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1776002921 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 43,008 | 5.5 | No |
| `.rsrc` | 2,048 | 4.806 | No |
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

	r #
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

This final chunk of disassembly provides the concluding pieces of evidence needed to build a comprehensive profile of this threat. The presence of these specific functions confirms that the malware uses a highly sophisticated "triple-threat" communication pipeline: **Encryption, Compression, and Serialization.**

Here is the updated analysis incorporating all three segments of the disassembly.

---

### Updated Analysis of Binary Sample (Final Review)

The inclusion of the third chunk solidifies the classification of this sample as a **high-end, professionally developed Trojan or sophisticated Loader.** The complexity of the code suggests it was designed to operate in environments where high-level security monitoring is present.

#### 1. Advanced Technical Infrastructure
*   **Multi-Layered Data Pipeline:** This segment confirms a very robust way of handling data from the C2 server:
    *   **Encryption (AES-256):** As seen in earlier chunks, all traffic is encrypted to prevent network inspection.
    *   **Compression (Decompress/Zip):** The `method.MessagePackLib.MessagePack.Zip.Decompress` function indicates that the payload or instructions sent by the C2 are compressed before transmission. This minimizes the "noise" on the wire and allows more commands to be packed into single packets.
    *   **Serialization (MessagePack):** Using `WriteMap`, `WriteString`, `GetAsUInt64`, and `WriteBinary` shows that the malware handles complex, nested data structures. It isn't just receiving "commands"; it is likely receiving entire configuration files or even secondary payloads in a structured format.
*   **Cryptographic Integrity (SHA-256):** The inclusion of `Sha256.ComputeHash` suggests the malware performs integrity checks. This is typically used to:
    1.  Verify that a downloaded "plugin" or second-stage payload hasn't been corrupted or modified by security software.
    2.  Generate unique machine fingerprints (HWIDs) for a specific victim.

#### 2. Aggressive Anti-Analysis & Obfuscation (Final Confirmation)
The final chunk provides the clearest evidence of **intentional anti-reverse engineering**:
*   **"Antivirus" Function as an Obfuscation Shield:** The function `method.Client.Helper.Methods.Antivirus` is surrounded by a massive amount of "junk" code, leading to dozens of warnings about "bad instruction data," "overlapping instructions," and "unreachable blocks." 
    *   This isn't just a simple check for an antivirus program; it is a **sophisticated obfuscation technique** designed to break the disassembler’s ability to map out the logic. It forces human analysts and automated tools to waste time on thousands of lines of meaningless code that never execute but confuse the software analyzing them.
*   **Control-Flow Obfuscation:** The repeated "Instruction Overlap" warnings suggest the use of techniques like **instruction substitution** or **overlapping instructions**, where one set of bytes can be interpreted as multiple different instructions depending on the entry point, a hallmark of professional malware protection (e.g., VMProtect or Themida-style protections).

#### 3. Operational Logic & Workflow
Based on all three segments of disassembly, we can now map the complete lifecycle:
1.  **Environment Check:** The malware executes `Antivirus` and `DetectManufacturer` to determine if it is in a sandbox/VM.
2.  **Initialization & Integrity:** It initializes settings and may use `Sha256` to verify its own configuration or environment stability.
3.  **Heartbeat/Registration:** It uses `SendInfo` (wrapped in MessagePack) to send the victim’s hardware details to the C2 server.
4.  **C2 Interaction Loop:** 
    *   The malware enters a loop reading data from the network.
    *   The data is **decrypted via AES-256**.
    *   The data is then **decompressed** (via the `Zip.Decompress` logic).
    *   Finally, it is **parsed as MessagePack objects**, allowing the malware to execute complex tasks like downloading more files, changing system settings, or starting additional processes based on the decrypted commands.

---

### Final Summary of Findings

| Category | Technical Details | Risk Level | Impact |
| :--- | :--- | :--- | :--- |
| **Payload Type** | Sophisticated Loader / Modular Trojan | **Critical** | Potential for multi-stage infections and persistent access. |
| **Encryption** | AES-256 (Symmetric) | **Critical** | High resistance to standard network traffic analysis. |
| **Data Handling** | MessagePack Serialization & Zip Decompression | **High** | Indicates complex, structured data/commands from C2. |
| **Anti-Analysis** | Massive "Junk" Code, Instruction Overlap, Anti-VM | **Critical** | Designed to frustrate and delay security research. |
| **Integrity** | SHA-256 Hashing | **Medium** | Used for validating payloads or unique device identification. |

### Conclusion for Incident Response
This is a top-tier piece of malware. The complexity of the **MessagePack + AES + Decompression** pipeline indicates that the actors behind this are not amateurs; they are likely part of a professional cybercrime organization or a sophisticated threat actor group.

**Key Takeaways for Defenders:**
1.  **Network Monitoring:** Standard NIDS/IPS will struggle to see what the malware is "doing" because it is hidden inside an encrypted, compressed packet. Look for persistent connections to suspicious IPs/domains over non-standard ports.
2.  **Endpoint Detection (EDR):** Because of the heavy obfuscation and "junk code," traditional signature-based detection will likely fail. EDR solutions should focus on **behavioral analysis** (e.g., a process suddenly launching `powershell.exe` or making repeated outbound connections after a period of dormancy).
3.  **Triage:** If this binary is found on a host, it should be treated as an indicator of a targeted attack rather than a random infection. The presence of "Antivirus" obfuscation suggests the threat actors are aware of professional security measures and will actively work to evade them.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1020** | Obfuscated Files or Information | The use of AES-256 encryption and MessagePack serialization is designed to hide command structures and data content from network security tools. |
| **T1027** | Obfuscated Executables | The heavy use of "junk" code and overlapping instructions is a deliberate tactic to frustrate reverse engineering efforts and bypass automated disassembly analysis. |
| **T1497** | Virtualized Environment | The `DetectManufacturer` and `Antivirus` functions are used to detect if the sample is running in a sandbox or analysis environment before executing malicious actions. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `AsyncClient.exe` (Identified as a component/binary name)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   `1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B` (Potential identifier/hash)
*   `87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F` (Potential identifier/hash)

**Other artifacts**
*   **C2 Communication Patterns:** Use of **MessagePack** for serialization, combined with **AES-256** encryption and **Zip decompression** to mask C2 traffic.
*   **Obfuscation Techniques:** Use of "junk code," "instruction overlap," and "unreachable blocks" specifically within the `Antivirus` check function to evade automated analysis tools.
*   **Anti-Analysis Functions:** Presence of `DetectManufacturer`, `GetActiveWindowTitle`, and `DetermineSandbox` logic (implied via the behavior description of `Antivirus` and `DetectManufacturer`).
*   **Detection for Logic Labels:** `SendInfo` (used for initial victim check/heartbeat).

---

## Malware Family Classification

Based on the analysis provided, here is the classification for this sample:

1. **Malware family:** custom (sophisticated loader)
2. **Malware type:** loader / backdoor
3. **Confidence:** High (for functionality/type), Medium (for specific naming)
4. **Key evidence:** 
    *   **Advanced Communication Pipeline:** The use of a triple-layer system (**AES-256 encryption, MessagePack serialization, and Zip compression**) indicates a professional-grade infrastructure designed to mask complex commands and payloads from network security tools.
    *   **Sophisticated Anti-Analysis:** The presence of "junk" code, instruction overlapping, and specific anti-VM/anti-debugging checks (e.g., `Antivirus` and `DetectManufacturer`) confirms the malware is engineered to evade both automated sandboxes and manual reverse engineering.
    *   **Modular Capability:** The combination of heartbeat functionality (`SendInfo`), integrity checking (`Sha256`), and the ability to process structured data suggests the primary purpose is to serve as a persistent beachhead (backdoor) or a delivery vehicle for secondary payloads (loader).
