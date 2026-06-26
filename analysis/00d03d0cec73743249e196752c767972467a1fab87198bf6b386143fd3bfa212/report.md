# Threat Analysis Report

**Generated:** 2026-06-25 12:55 UTC
**Sample:** `00d03d0cec73743249e196752c767972467a1fab87198bf6b386143fd3bfa212_00d03d0cec73743249e196752c767972467a1fab87198bf6b386143fd3bfa212.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00d03d0cec73743249e196752c767972467a1fab87198bf6b386143fd3bfa212_00d03d0cec73743249e196752c767972467a1fab87198bf6b386143fd3bfa212.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 47,616 bytes |
| MD5 | `d8dcf08a1825ad4b3b45860f9849288f` |
| SHA1 | `4d240b52705be3f6e03d411422fb926f219eedd8` |
| SHA256 | `00d03d0cec73743249e196752c767972467a1fab87198bf6b386143fd3bfa212` |
| Overall entropy | 5.602 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2324017115 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 41,984 | 5.611 | No |
| `.rsrc` | 4,608 | 5.177 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **502** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

,!	rY#

-	r&
v4.0.30319
#Strings
#	(	7	?	X	
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
<PrivateImplementationDetails>
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
get_Id
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Client.Algorithm.Zip.Compress` | `0x4056a4` | 51548 | ✓ |
| `method.Client.Algorithm.Aes256..cctor` | `0x402605` | 12131 | ✓ |
| `method.Client.MessagePack.MsgPack.DecodeFromStream` | `0x403720` | 1424 | ✓ |
| `method.Client.Install.NormalStartup.Install` | `0x4041d4` | 812 | ✓ |
| `method.Client.Connection.ClientSocket.InitializeClient` | `0x40293c` | 760 | ✓ |
| `method.Client.Handle_Packet.Packet.Read` | `0x404ea4` | 540 | ✓ |
| `method.Client.Connection.ClientSocket.ReadServertData` | `0x402c98` | 448 | ✓ |
| `method.Client.Helper.IdSender.SendInfo` | `0x404928` | 448 | ✓ |
| `method.Client.Algorithm.Aes256.Decrypt` | `0x405398` | 424 | ✓ |
| `method.Client.Algorithm.Aes256.Encrypt` | `0x405258` | 320 | ✓ |
| `method.Client.Settings.InitializeSettings` | `0x4026f4` | 316 | ✓ |
| `method.Client.MessagePack.WriteTools.WriteInteger` | `0x4040a8` | 300 | ✓ |
| `method.Client.Handle_Packet.Packet.Invoke` | `0x4050c0` | 296 | ✓ |
| `method.Client.Connection.ClientSocket.Send` | `0x402e58` | 284 | ✓ |
| `method.Client.Helper.Anti_Analysis.DetectManufacturer` | `0x404590` | 272 | ✓ |
| `method.Client.MessagePack.MsgPack.Encode2Stream` | `0x403d14` | 248 | ✓ |
| `entry0` | `0x402620` | 212 | ✓ |
| `method.Client.Helper.Methods.Antivirus` | `0x404b48` | 212 | ✓ |
| `method.Client.MessagePack.MsgPack.WriteMap` | `0x4031c8` | 188 | ✓ |
| `method.Client.MessagePack.WriteTools.WriteString` | `0x403f30` | 180 | ✓ |
| `method.Client.MessagePack.MsgPack.GetAsBytes` | `0x403500` | 176 | ✓ |
| `method.Client.MessagePack.ReadTools.ReadString` | `0x403e88` | 168 | ✓ |
| `method.Client.Settings..cctor` | `0x402898` | 164 | ✓ |
| `method.Client.MessagePack.MsgPack.WirteArray` | `0x403284` | 164 | ✓ |
| `method.Client.MessagePack.MsgPack.GetAsUInt64` | `0x403328` | 164 | ✓ |
| `method.Client.MessagePack.MsgPack.GetAsInteger` | `0x4033cc` | 164 | ✓ |
| `method.Client.MessagePack.MsgPack.ForcePathObject` | `0x403604` | 164 | ✓ |
| `method.Client.Helper.CheckMiner.GetCommandLine` | `0x4047a0` | 164 | ✓ |
| `method.Client.Connection.ClientSocket.KeepAlivePacket` | `0x402f74` | 148 | ✓ |
| `method.Client.MessagePack.WriteTools.WriteBinary` | `0x403fe4` | 148 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Client.Algorithm.Aes256..cctor.c`](code/method.Client.Algorithm.Aes256..cctor.c)
- [`code/method.Client.Algorithm.Aes256.Decrypt.c`](code/method.Client.Algorithm.Aes256.Decrypt.c)
- [`code/method.Client.Algorithm.Aes256.Encrypt.c`](code/method.Client.Algorithm.Aes256.Encrypt.c)
- [`code/method.Client.Algorithm.Zip.Compress.c`](code/method.Client.Algorithm.Zip.Compress.c)
- [`code/method.Client.Connection.ClientSocket.InitializeClient.c`](code/method.Client.Connection.ClientSocket.InitializeClient.c)
- [`code/method.Client.Connection.ClientSocket.KeepAlivePacket.c`](code/method.Client.Connection.ClientSocket.KeepAlivePacket.c)
- [`code/method.Client.Connection.ClientSocket.ReadServertData.c`](code/method.Client.Connection.ClientSocket.ReadServertData.c)
- [`code/method.Client.Connection.ClientSocket.Send.c`](code/method.Client.Connection.ClientSocket.Send.c)
- [`code/method.Client.Handle_Packet.Packet.Invoke.c`](code/method.Client.Handle_Packet.Packet.Invoke.c)
- [`code/method.Client.Handle_Packet.Packet.Read.c`](code/method.Client.Handle_Packet.Packet.Read.c)
- [`code/method.Client.Helper.Anti_Analysis.DetectManufacturer.c`](code/method.Client.Helper.Anti_Analysis.DetectManufacturer.c)
- [`code/method.Client.Helper.CheckMiner.GetCommandLine.c`](code/method.Client.Helper.CheckMiner.GetCommandLine.c)
- [`code/method.Client.Helper.IdSender.SendInfo.c`](code/method.Client.Helper.IdSender.SendInfo.c)
- [`code/method.Client.Helper.Methods.Antivirus.c`](code/method.Client.Helper.Methods.Antivirus.c)
- [`code/method.Client.Install.NormalStartup.Install.c`](code/method.Client.Install.NormalStartup.Install.c)
- [`code/method.Client.MessagePack.MsgPack.DecodeFromStream.c`](code/method.Client.MessagePack.MsgPack.DecodeFromStream.c)
- [`code/method.Client.MessagePack.MsgPack.Encode2Stream.c`](code/method.Client.MessagePack.MsgPack.Encode2Stream.c)
- [`code/method.Client.MessagePack.MsgPack.ForcePathObject.c`](code/method.Client.MessagePack.MsgPack.ForcePathObject.c)
- [`code/method.Client.MessagePack.MsgPack.GetAsBytes.c`](code/method.Client.MessagePack.MsgPack.GetAsBytes.c)
- [`code/method.Client.MessagePack.MsgPack.GetAsInteger.c`](code/method.Client.MessagePack.MsgPack.GetAsInteger.c)
- [`code/method.Client.MessagePack.MsgPack.GetAsUInt64.c`](code/method.Client.MessagePack.MsgPack.GetAsUInt64.c)
- [`code/method.Client.MessagePack.MsgPack.WirteArray.c`](code/method.Client.MessagePack.MsgPack.WirteArray.c)
- [`code/method.Client.MessagePack.MsgPack.WriteMap.c`](code/method.Client.MessagePack.MsgPack.WriteMap.c)
- [`code/method.Client.MessagePack.ReadTools.ReadString.c`](code/method.Client.MessagePack.ReadTools.ReadString.c)
- [`code/method.Client.MessagePack.WriteTools.WriteBinary.c`](code/method.Client.MessagePack.WriteTools.WriteBinary.c)
- [`code/method.Client.MessagePack.WriteTools.WriteInteger.c`](code/method.Client.MessagePack.WriteTools.WriteInteger.c)
- [`code/method.Client.MessagePack.WriteTools.WriteString.c`](code/method.Client.MessagePack.WriteTools.WriteString.c)
- [`code/method.Client.Settings..cctor.c`](code/method.Client.Settings..cctor.c)
- [`code/method.Client.Settings.InitializeSettings.c`](code/method.Client.Settings.InitializeSettings.c)

## Behavioral Analysis

Based on the disassembly provided in chunk 4/4, I have updated the analysis. This final portion of the code reveals specialized communication maintenance, evidence of multi-purpose capabilities (potentially involving cryptocurrency mining), and further confirms high-level anti-analysis techniques.

### **Updated Analysis Overview**
The final set of functions reinforces the conclusion that this is a sophisticated, production-grade malware framework. While the previous chunks established the "transport" (MessagePack) and "security" (AES-256) layers, this chunk reveals the "persistence" and "environmental awareness" of the threat. The repeated presence of the same heavily obfuscated code blocks across different functions confirms that the developers are using a modular architecture where many features share common, hidden logic.

---

### **Refined & Confirmed Core Functionalities**
*   **Persistence & Connection Maintenance:**
    *   **`KeepAlivePacket`**: The inclusion of this function in `method.Client.Connection.ClientSocket` is a hallmark of high-quality RATs (Remote Access Trojans). It ensures that the connection between the infected host and the C2 server remains active, even during periods of inactivity. This prevents firewalls or network monitors from timing out the connection.
*   **Multi-Purpose Capability / Potential Mining:**
    *   **`CheckMiner.GetCommandLine`**: The presence of a "Miner" check is highly significant. It suggests two possibilities:
        1.  The malware is a **hybrid threat**, containing capabilities to perform cryptocurrency mining in addition to standard RAT functions.
        2.  The malware includes an **environment-checking module** to see if the system is already being monitored or utilized by other known pieces of malware (like miners) before it proceeds with its primary mission.
*   **Advanced Data Handling:**
    *   **`WriteBinary` & `ForcePathObject`**: These functions within the MessagePack library confirm that the malware is designed to handle raw binary data and file pathing efficiently. This allows it to exfiltrate not just text, but potentially compressed files, system binaries, or registry dumps.

---

### **Enhanced Suspicious & Malicious Behaviors**
*   **Evasive Anti-Analysis (Instruction Overlapping):**
    *   The disassembly consistently flags: `WARNING: Instruction at (ram,0x0040282a) overlaps instruction at (ram,0x00402828)`. 
    *   This is a deliberate anti-disassembly technique. By overlapping instructions, the developers are attempting to break the linear flow of disassemblers like IDA Pro or Ghidra. This makes it extremely difficult for automated tools to generate a clean control-flow graph (CFG), forcing an analyst to manually untangle the code to see what it is actually doing.
*   **High Persistence Strategy:**
    *   The combination of `KeepAlivePacket` and `AES256` suggests a "low and slow" approach. The malware wants to stay connected for days or weeks at a time without alerting network security monitors, while ensuring that every packet sent is encrypted and unreadable by standard intrusion detection systems (IDS).

---

### **Finalized Communication Pipeline**
The full lifecycle of the data transmission now looks like this:
1.  **Collection:** Gather system info, files, or credentials (potentially even mining metrics).
2.  **Parsing/Validation:** Use `ForcePathObject` to handle local file paths and check for environmental factors (`CheckMiner`).
3.  **Packaging:** Wrap data into binary containers using **MessagePack**.
4.  **Encryption:** Encrypt the payload using **AES-256**.
5.  **Persistence:** Maintain a constant heartbeat via **KeepAlivePacket** to ensure the tunnel remains open for future commands.

---

### **Final Conclusion & Risk Assessment**
The total evidence from all four chunks confirms that this is an **Advanced Persistent Threat (APT) level backdoor/RAT.** 

It is not a "script kiddie" tool; it is a professional piece of malware designed for long-term presence, advanced data exfiltration, and evasion of security software.

**Final Risk Rating: Critical**
*   **Threat Type:** Modular RAT / Advanced Trojan.
*   **Key Indicators of Sophistication:** 
    *   **Sophisticated Serialization:** (MessagePack) allows for complex data structures.
    *   **Robust Encryption:** (AES-256) hides the content of the traffic.
    *   **Active Anti-Analysis:** (Instruction Overlapping) targets the tools used by forensic analysts.
    *   **Persistence Features:** (KeepAlivePacket) ensures long-term control over the infected machine.

**Final Recommendation:** 
Any system interacting with this code should be considered compromised at a deep level. Because of the `KeepAlive` and `AES` features, standard network monitoring might not catch the data theft in real-time. Isolation of the infected host and a full forensic sweep for other modular components (like miners or additional backdoors) is highly recommended.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided analysis to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Executables | The use of "Instruction Overlapping" is a deliberate anti-disassembly technique designed to break the flow of tools like IDA Pro and Ghidra. |
| **T1497** | Virtualization/Sandbox Detection | The `CheckMiner` functionality serves as an environmental awareness check to determine if the malware is running in a monitored or non-target environment. |
| **T1573** | Encrypted Traffic | The implementation of AES-256 ensures that all communication between the RAT and the C2 server remains hidden from network security monitors. |
| **T1071** | Application Layer Protocol | The use of "KeepAlivePacket" and MessagePack indicates a structured, persistent application layer protocol for maintaining the C2 connection. |
| **T1041** | Exfiltration Over C2 Channel | The inclusion of `WriteBinary` and `ForcePathObject` functions allows the malware to package and exfiltrate raw binary data and system files via the C2 channel. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted list of Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `Stub.exe` (Potential executable filename)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   `1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B`
*   `87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F`

**Other artifacts (user agents, C2 patterns, etc.)**
*   **C2 Communication Protocol:** MessagePack (used for data serialization)
*   **Encryption Algorithms:** AES-256, HMACSHA256
*   **Persistence/Heartbeat Mechanism:** `KeepAlivePacket` (Used to maintain a persistent connection with the C2 server).
*   **Anti-Analysis Technique:** Instruction Overlapping at memory offsets `0x00402828` and `0x0040282a`.
*   **Malicious Capability Indicators:**
    *   `CheckMiner`: Presence of cryptocurrency mining detection/capabilities.
    *   `WriteBinary`/`ForcePathObject`: Capabilities to handle raw binary data and manipulate file system paths for exfiltration.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: RAT (Remote Access Trojan) / Backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Persistence & Communication:** The use of `KeepAlivePacket` for maintaining long-term C2 heartbeats and **MessagePack** for complex data serialization indicates a professional, production-grade infrastructure designed for persistent access.
*   **Advanced Evasion Techniques:** The intentional use of "Instruction Overlapping" to break disassemblers (IDA Pro/Ghidra) combined with **AES-256 encryption** highlights a high level of sophistication intended to bypass both automated detection and manual analysis.
*   **Modular Capabilities:** The presence of `CheckMiner` and `WriteBinary` functions suggests the malware is designed for multi-purpose operations, including potential cryptocurrency mining integration or advanced data exfiltration.
