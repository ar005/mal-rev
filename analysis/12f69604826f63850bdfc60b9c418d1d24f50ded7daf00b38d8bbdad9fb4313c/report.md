# Threat Analysis Report

**Generated:** 2026-09-01 19:45 UTC
**Sample:** `12f69604826f63850bdfc60b9c418d1d24f50ded7daf00b38d8bbdad9fb4313c_12f69604826f63850bdfc60b9c418d1d24f50ded7daf00b38d8bbdad9fb4313c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12f69604826f63850bdfc60b9c418d1d24f50ded7daf00b38d8bbdad9fb4313c_12f69604826f63850bdfc60b9c418d1d24f50ded7daf00b38d8bbdad9fb4313c.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 47,104 bytes |
| MD5 | `48f06391d305a2e105d0de83bbcb5787` |
| SHA1 | `59bd67f3841f8e87c71e0838fd385173d69a92d5` |
| SHA256 | `12f69604826f63850bdfc60b9c418d1d24f50ded7daf00b38d8bbdad9fb4313c` |
| Overall entropy | 5.453 |
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
| `.text` | 43,008 | 5.502 | No |
| `.rsrc` | 3,072 | 4.952 | No |
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

This third chunk of disassembly provides a final layer of confirmation regarding the malware's complexity, specifically focusing on **data versatility**, **hidden functionality**, and **modular architecture**.

The inclusion of advanced compression routines and high-precision data handling confirms that this is not just a simple "grabber," but a highly engineered tool designed for maximum utility.

### Updated Analysis: Sophisticated Information Stealer / Trojan
*Integration of Chunk 3 findings into the existing intelligence.*

---

### New Key Findings from Chunk 3

#### 1. Robust Data Handling (Type-Rich Serialization)
The disassembly reveals specific methods within `MessagePackLib` for handling various data types, such as `GetAsUInt64`, `GetAsInteger`, and `GetAsFloat`.
*   **Why this matters:** This indicates that the malware isn't just looking for "text" (like passwords or usernames). It is designed to capture a wide array of system information. For example:
    *   `GetAsUInt64`: Used for high-precision values like timestamps, large file sizes, or specific hardware identifiers.
    *   `GetAsFloat`: Likely used for network metrics or telemetry data provided by the local environment.
    *   **Impact:** It allows the malware to build a comprehensive profile of the victim's machine, not just steal stolen credentials.

#### 2. Support for "Raw" Data (WriteBinary)
The `WriteTools.WriteBinary` function confirms that the malware is capable of handling and packaging **raw binary data**.
*   **Why this matters:** This is a strong indicator of a **RAT (Remote Access Trojan)** or a **Multi-Purpose Stealer**. It means the malware can package files, images (such as screenshots), or even raw memory dumps for exfiltration. It doesn't need to convert things to text; it can move "blobs" of data directly.

#### 3. Payload Extraction & Modular Capability (Zip.Decompress)
The inclusion of `MessagePackLib.MessagePack.Zip.Decompress` is a critical discovery regarding the malware’s lifecycle.
*   **Why this matters:** This suggests that the malware can **decompress and execute additional components**. Instead of carrying all its malicious features in one large file (which would be easily flagged), it likely downloads "modules" or configuration files in compressed form. It then decompresses them locally to perform different actions, such as starting a keylogger or opening a remote shell.

#### 4. Integrity and Identity Verification (Sha256)
The `sym.Client.Algorithm.Sha256.ComputeHash` function indicates the use of standard cryptographic hashing for two primary purposes:
*   **Unique Hardware Fingerprinting:** Generating a unique ID based on system hardware to identify specific victims for the attackers.
*   **Integrity Checks:** Ensuring that the data received from the Command & Control (C2) server is untampered with before the malware executes those instructions.

---

### Updated Summary of Malicious Behaviors
*   **Versatile Data Harvesting:** Uses **MessagePack** to handle a wide range of data types (Large Integers, Floats, and Binary Blobs), allowing for comprehensive information theft.
*   **Modular Architecture:** The `Decompress` function indicates the ability to unpack additional payloads or modules locally, suggesting it can change its "behavior" over time based on what the attacker sends.
*   **Robust Identity & Integrity:** Uses **SHA-256** to create unique machine fingerprints and verify the integrity of instructions received from the C2 infrastructure.
*   **Proactive Evasion:** (Carried from previous analysis) Continues to use `DetectManufacturer` and `Antivirus` checks to stay hidden in high-value environments.

---

### Final Risk Assessment Table (Consolidated)

| Feature | Evidence Observed | Analysis / Impact | Risk Level |
| :--- | :--- | :--- | :--- |
| **Complex Serialization** | `MessagePackLib`, `GetAsUInt64`, `GetAsFloat` | Allows the capture of complex, non-textual data (timestamps, system metrics). | High |
| **Raw Data Support** | `WriteTools.WriteBinary` | Indicates capability to exfiltrate files, screenshots, or raw memory dumps. | High |
| **Payload Decompression** | `Zip.Decompress` | Suggests a modular design where the malware can "unpack" more tools after infection. | Critical |
| **Encryption & Hashing** | `Aes256.Encrypt`, `Sha256.ComputeHash` | Shields exfiltrated data from network filters and ensures C2 instructions are valid. | High |
| **Environment Awareness** | `DetectManufacturer`, `Antivirus` | Active measures to evade sandboxes and security software during the initial infection phase. | High |
| **C2 Infrastructure** | `ClientSocket.Send`, `Packet.Invoke` | Confirms an active, bidirectional communication channel with a remote server. | High |

---

### Final Conclusion (Final Update)
This malware is a high-tier threat characterized by its **multipurpose capabilities**. It is not merely a "script-kiddy" tool; the presence of **MessagePack** for sophisticated data handling, **SHA-256** for identity verification, and **Zip Decompression** for modular payload execution indicates a professional level of development. 

The malware is designed to be **persistent and versatile**: it can act as a high-volume information stealer (gathering complex system data) while simultaneously serving as a "loader" or "dropper" capable of bringing in new functionalities as instructed by the remote operator. The deliberate inclusion of anti-analysis features confirms it is intended for targets where security posture is significant, making it an ideal tool for **corporate espionage** or **targeted ransomware preparation.**

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the relevant MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1082** | System Information Discovery | The use of `MessagePack` for diverse data types (UInt64, Float) indicates the collection of specific system metrics and hardware identifiers. |
| **T1011** | Exfiltration | The inclusion of `WriteBinary` confirms the capability to package and move raw "blobs" such as files, images, or memory dumps. |
| **T1105** | Ingress Tool Transfer | The `Zip.Decompress` function points to a modular architecture designed to download and execute additional capabilities post-infection. |
| **T1027** | Obfuscated Files or Information | The use of complex serialization and compression masks the underlying data structure and the specific functions being performed by the modules. |
| **T1497** | Virtualization/Sandbox Detection | Checks for `Manufacturer` and `Antivirus` presence are classic indicators of attempts to detect and evade security analysis environments. |
| **T1036** | Masquerading | (Optional/Implicit) The use of modularity and complex serialization allows the malware to blend in as a legitimate, multi-purpose tool rather than a simple script. |

### Analyst Notes:
*   **Modular Architecture:** The identification of `Zip.Decompress` combined with `MessagePack` suggests a sophisticated "Loader" functionality. This is common in advanced persistent threats (APTs) where the initial payload is small to avoid detection, but can pull down heavier modules (keyloggers, remote shells) upon confirmation of a valid environment.
*   **Data Sophistication:** The shift from simple string-grabbing to `UInt64` and `Float` support indicates that the threat actor is targeting high-value environments where system telemetry and complex data are more valuable than just plain-text credentials.
*   **Evasion Strategy:** The use of **SHA-256** for integrity checks ensures that the malware only executes commands from a trusted C2 source, preventing researchers from easily hijacking the bot or injecting unauthorized instructions during an analysis phase.

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*   *None identified.* (The behavior analysis mentions C2 infrastructure, but no specific IP addresses or domains were provided in the raw data.)

### **File paths / Registry keys**
*   `meta_update.exe` (Identified filename)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   `1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B` (SHA-256)

### **Other artifacts**
*   **Malware Library/Framework:** `MessagePackLib` (Used for complex data serialization and handling non-textual data like binary blobs).
*   **Cryptographic Functions:** `Aes256`, `Sha256Managed`, `HMACSHA256`.
*   **Execution Patterns:** 
    *   `Zip.Decompress`: Indicates a multi-stage/modular execution behavior where the malware unpacks additional payloads or configuration files.
    *   `WriteTools.WriteBinary`: Capability to handle and exfiltrate raw binary data (e.g., screenshots, documents).
    *   **Anti-Analysis:** `DetectSandboxie`, `Antivirus` checks (as noted in behavior analysis), and use of hardware fingerprinting via `Sha256`.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1.  **Malware family:** custom
2.  **Malware type:** loader / info-stealer (modular)
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Modular Architecture & Payload Delivery:** The presence of `Zip.Decompress` and `MessagePackLib` indicates the malware is designed to function as a multi-stage loader, capable of unpacking additional modules (such as keyloggers or remote shells) to expand its functionality post-infection.
    *   **Advanced Data Exfiltration:** Unlike basic "grabbers," this sample supports raw binary data (`WriteBinary`) and complex data types (`UInt64`, `Float`), allowing it to exfiltrate system telemetry, files, and images rather than just plain-text credentials.
    *   **Sophisticated Evasion & Integrity:** The use of SHA-256 for unique hardware fingerprinting and C2 integrity checks, combined with active anti-analysis routines (Antivirus/Sandbox detection), identifies this as a professional-grade tool designed for high-value targets and corporate espionage.
