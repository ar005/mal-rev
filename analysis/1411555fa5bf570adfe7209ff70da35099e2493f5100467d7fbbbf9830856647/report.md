# Threat Analysis Report

**Generated:** 2026-09-03 22:31 UTC
**Sample:** `1411555fa5bf570adfe7209ff70da35099e2493f5100467d7fbbbf9830856647_1411555fa5bf570adfe7209ff70da35099e2493f5100467d7fbbbf9830856647.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1411555fa5bf570adfe7209ff70da35099e2493f5100467d7fbbbf9830856647_1411555fa5bf570adfe7209ff70da35099e2493f5100467d7fbbbf9830856647.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 46,592 bytes |
| MD5 | `9fc64c104c16b6c61f8ab98366fc1bff` |
| SHA1 | `585fef3bf3ec2657a7e20092b99ebf9e73475fe2` |
| SHA256 | `1411555fa5bf570adfe7209ff70da35099e2493f5100467d7fbbbf9830856647` |
| Overall entropy | 5.459 |
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
| `.rsrc` | 2,560 | 5.014 | No |
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

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x40596c` | 50836 | — |
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
- [`code/method.MessagePackLib.MessagePack.Zip.Decompress.c`](code/method.MessagePackLib.MessagePack.Zip.Decompress.c)
- [`code/sym.Client.Algorithm.Sha256.ComputeHash.c`](code/sym.Client.Algorithm.Sha256.ComputeHash.c)

## Behavioral Analysis

This final portion of the disassembly provides a comprehensive look into the "back-end" utility suite of the malware. The inclusion of these specific libraries confirms that this is not just a simple remote access tool, but a **highly modular and extensible platform.**

The following updated analysis incorporates findings from all three segments of the provided code.

---

### Final Integrated Analysis Report

#### 1. Core Functionality & Infrastructure (Consolidated)
The binary's architecture confirms it as a high-tier, professional-grade malware (likely a RAT or Botnet agent). The core infrastructure is built on three pillars:

*   **Advanced Data Serialization (MessagePack):** The extensive suite of functions (`WriteMap`, `WriteString`, `GetAsInteger`, `GetAsFloat`, etc.) confirms the use of **MessagePack**. Unlike simpler formats, MessagePack allows the malware to package complex, nested data structures into a compact binary format. This means the command-and-control (C2) interaction is highly structured and efficient.
*   **Multi-Layered Encryption & Integrity:** The confirmation of `AES-256` for payload protection, combined with `Sha256.ComputeHash`, indicates a professional security posture. SHA-256 is likely used to verify the integrity of received commands or modules before execution, ensuring that an intercepted and tampered packet does not cause the malware to crash (which would alert defenders).
*   **Dynamic Payload Execution (Zip.Decompress):** The discovery of a `Decompress` routine is a critical finding. It strongly suggests **modular functionality.** This allows the threat actor to send "plug-ins" or new capabilities (e.g., a specific credential scraper, a different keylogger module, or even a secondary stage payload) in a compressed and encrypted state, which the malware then unpacks and executes in memory.

#### 2. Advanced Evasion & Anti-Analysis (Refined)
The analysis of `entry0`, `InitializeSettings`, and the various "Warning" blocks in the disassembly confirms several advanced techniques:

*   **Anti-Sandbox/Environment Fingerprinting:** The use of `DetectManufacturer` and checks for specific hardware IDs indicates the malware is programmed to recognize and potentially "go dormant" if it detects a virtual machine (VM), debugger, or analysis laboratory.
*   **Instruction Obfuscation:** Several functions contain **overlapping instructions** and complex jump logic. This is a deliberate tactic designed to break the linear disassembly process in tools like IDA Pro or Ghidra, forcing a human analyst to spend significantly more time "de-obfuscating" the code just to understand its basic flow.
*   **Behavioral Obfuscation:** By using `GetForegroundWindow`, the malware can detect when it is actively being observed by an analyst or if it should only perform actions (like keylogging) when a specific window is in focus, helping it blend in with legitimate user activity.

#### 3. Technical Indicators (IOC Potential)
*   **Encryption/Hashing:** AES-256, SHA256, HMACSHA256.
*   **Data Protocol:** MessagePack (High probability of use over TCP port 443 or non-standard ports).
*   **Decompression Algorithms:** Likely Zlib or Gzip-based decompression (referenced via the `Zip` namespace).
*   **Evasive Behavior Patterns:**
    *   Requesting hardware/BIOS information.
    *   Monitoring for foreground window changes.
    *   High volume of "no-op" or overlapping instruction blocks designed to confuse signature-based detection and automated analysis.

---

### Final Risk Assessment & Synthesis

This malware is a **Professional Grade Multi-Stage Threat.** 

The transition from simple remote commands to a full **MessagePack suite** and a **Decompression engine** indicates that the threat actor intends for this malware to be long-lived. By using these components, they achieve:
1.  **Adaptability:** They can update what the "bot" does without changing the main binary's signature (by sending new compressed modules).
2.  **Evasion:** The use of complex serialization and layered encryption makes it very difficult for Network Intrusion Detection Systems (NIDS) to identify the specific commands being sent by the C2.
3.  **Stealth:** The advanced obfuscation techniques suggest a "pro" developer cycle, where the primary goal is to remain undetected on a high-value target for as long as possible.

### Recommended Incident Response Actions:

*   **Network Hunting (L7):** Monitor for traffic using binary protocols that don't conform to standard HTTP/HTTPS structures. Look specifically for MessagePack headers or repeated patterns of AES-encrypted packets followed by "heartbeat" pings.
*   **Host Monitoring:** Deploy EDR rules to alert on processes attempting to access BIOS information, hardware serial numbers, or performing high-frequency calls to `GetForegroundWindow` in a loop (typical of keylogging logic).
*   **Payload Analysis:** Since the malware has `Decompress` capabilities, any "blob" of data received from the C2 should be treated as potentially executable. If a suspicious blob is captured, it should be extracted and analyzed separately for secondary stages.
*   **Internal Scanning:** Identify machines where internal processes are attempting to connect to external IPs using high-entropy ports or repeated connections that stay open for long periods (persistence).

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your report to the corresponding MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1071** | Application Layer Protocol | The use of MessagePack for structured, compact data serialization indicates a sophisticated method for organizing C2 communications. |
| **T1573** | Encrypted Channel | The implementation of AES-256 and SHA-256 ensures that the communication channel remains encrypted and verifies the integrity of received commands. |
| **T1105** | Ingress Tool Transfer | The inclusion of a `Zip.Decompress` routine enables the malware to receive and execute additional modules or "plug-ins" from a remote server. |
| **T1497** | Virtualization/Sandbox Evasion | The use of hardware ID checks and manufacturer detection is designed to identify and avoid execution within analysis environments or VMs. |
| **T1027** | Obfuscated Files or System API | The use of overlapping instructions and complex jump logic is a deliberate tactic intended to break linear disassembly and hinder manual analysis in tools like IDA Pro. |
| **T1497** | Virtualization/Sandbox Evasion | The utilization of `GetForegroundWindow` allows the malware to detect if it is being actively observed by an analyst before performing sensitive actions. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `AzureNetwork.exe` (Identified as a specific executable filename within the malware's structure).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   `1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B` (Hex string/Potential MD5)
*   `87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F` (SHA-256)

**Other artifacts**
*   **C2 Protocol:** MessagePack (Used for structured, compact binary data serialization).
*   **Encryption/Hashing Algorithms:** AES-256, Sha256, HMACSHA256.
*   **Decompression Engines:** Zlib / Gzip (referenced via `Zip` namespace and `Decompress` routines).
*   **Evasion Techniques:** 
    *   Use of `GetForegroundWindow` to detect analyst interaction or specific user activity.
    *   Hardware/BIOS information gathering for environment fingerprinting.
    *   Instruction Obfuscation (overlapping instructions and complex jump logic).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the malware sample:

1.  **Malware family:** custom (Sophisticated Backdoor)
2.  **Malware type:** RAT / Loader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Modular Architecture:** The integration of a **MessagePack serialization suite** and **Zip decompression routines** indicates the malware is designed to act as a persistent "host" for various modules (e.g., keyloggers, credential stealers) that can be updated remotely without modifying the primary binary's signature.
    *   **Advanced Evasion Tactics:** The use of **overlapping instructions** and **hardware/manufacturer fingerprinting** demonstrates a high-tier development cycle intended to bypass automated sandboxes and frustrate manual reverse engineering.
    *   **Sophisticated Communication Protocol:** The reliance on **AES-256 encryption** combined with structured data packaging suggests a professional-grade C2 infrastructure designed for long-term persistence rather than a simple, one-off infection.
