# Threat Analysis Report

**Generated:** 2026-06-29 20:59 UTC
**Sample:** `034c0e259f7f829e7c5476f4492769b1ffa8656e10da1fa372a4d5d49cc2b48c_034c0e259f7f829e7c5476f4492769b1ffa8656e10da1fa372a4d5d49cc2b48c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `034c0e259f7f829e7c5476f4492769b1ffa8656e10da1fa372a4d5d49cc2b48c_034c0e259f7f829e7c5476f4492769b1ffa8656e10da1fa372a4d5d49cc2b48c.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 114,688 bytes |
| MD5 | `b020f0428000a9424297260c46593648` |
| SHA1 | `3b6b2fe05ecb1a4c4aee3202ca9b9c637cd93608` |
| SHA256 | `034c0e259f7f829e7c5476f4492769b1ffa8656e10da1fa372a4d5d49cc2b48c` |
| Overall entropy | 4.078 |
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
| `.text` | 43,008 | 5.522 | No |
| `.rsrc` | 70,656 | 2.618 | No |
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

	r:&
v4.0.30319
#Strings
Action`10
<>p__0
Window11
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MessagePackLib.MessagePack.WriteTools.WriteFloat` | `0x4025ab` | 65508 | ✓ |
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x40596c` | 64436 | ✓ |
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
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteFloat.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteFloat.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteInteger.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteInteger.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteString.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteString.c)
- [`code/method.MessagePackLib.MessagePack.Zip.Compress.c`](code/method.MessagePackLib.MessagePack.Zip.Compress.c)
- [`code/sym.Client.Algorithm.Sha256.ComputeHash.c`](code/sym.Client.Algorithm.Sha256.ComputeHash.c)

## Behavioral Analysis

Based on the provided strings and disassembled code, here is an analysis of the binary's behavior.

### Core Functionality and Purpose
The sample appears to be a **malicious .NET-based client** (likely a bot, trojan, or backdoor) designed to communicate with a remote server using encrypted protocols. The presence of `MessagePack` indicates it uses a compact serialization format, which is common in modern malware to package data for transmission efficiently.

### Suspicious and Malicious Behaviors
The following behaviors are highly indicative of malicious intent:

*   **Anti-Analysis & Evasion:** 
    *   The inclusion of `DetectSandboxie` suggests the binary checks if it is running inside a common analysis sandbox/wrapper to evade detection.
    *   The presence of an `Anti_Analysis` module and `DetectManufacturer` indicates the code actively attempts to identify if it is being run in a laboratory environment or on a virtual machine before proceeding with its primary payload.
*   **Encrypted Communication:** 
    *   The code utilizes **AES-256** for both encryption (`Encrypt`) and decryption (`Decrypt`).
    *   It implements standard network protocols including `SslClient`, `TcpClient`, and `Heartbeat` mechanisms, suggesting it maintains a persistent connection with a Command & Control (C2) server.
*   **Information Gathering:** 
    *   Strings such as `get_MachineName`, `get_UserName`, and `GetActiveWindowTitle` suggest the malware profiles the victim's machine to identify target details or potentially gather intelligence before exfiltrating data.
*   **File & Registry Manipulation:** 
    *   Functions like `InstallFile`, `SaveBytesToFile`, and `DeleteSubKeyTree` indicate the ability to drop additional components onto the system, modify configuration files, or clean up artifacts (or registry keys) during its operation.

### Notable Techniques & Patterns
*   **Data Serialization:** The use of **MessagePackLib** indicates a sophisticated approach to data handling, allowing for complex objects and structures to be sent over the wire in a compressed format.
*   **Network "Heartbeats":** The presence of `KeepAlive` and `Ping` suggest a persistent "heartbeat" system typical of botnets or remote access trojans (RATs) to keep a connection open with the C2 server.
*   **Obfuscation/Decompilation Artifacts:** While several functions are displayed as "WriteFloat" in the disassembly, these appear to be artifacts of the decompiler failing to resolve complex .NET metadata after obfuscation; however, the original function names (e.g., `ReadServertData`, `Decrypt`, `Send`) remain visible and indicate the actual logic intended by the developer.
*   **System Profiling:** The combination of `GetHostName`, `get_OSFullName`, and `ValidateServerCertificate` suggests a robust connection logic that validates its remote infrastructure while gathering enough local information to "fingerprint" the infected machine.

### Summary of Indicators
*   **Malware Class:** Likely a RAT or Trojan.
*   **Primary Threat:** Persistent, encrypted communication with a C2 server.
*   **Detection Surface:** Anti-analysis checks (Sandboxie), AES encryption, and information harvesting.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1562** | Impair Defenses | The inclusion of `DetectSandboxie`, `Anti_Analysis`, and `DetectManufacturer` indicates an attempt to evade detection by identifying analysis environments. |
| **T1573** | Encrypted Channel | The use of AES-256 for data encryption and the implementation of `SslClient` indicate a desire to mask communication between the malware and the C2 server. |
| **T1082** | System Information Discovery | Functions like `get_MachineName`, `get_UserName`, and `GetHostName` are used to profile and fingerprint the victim's machine. |
| **T1105** | Ingress Tool Transfer | The use of `InstallFile` and `SaveBytesToFile` suggests the delivery and installation of additional malicious components or modules onto the host. |
| **T1070** | Indicator Removal on Host | The `DeleteSubKeyTree` function indicates an attempt to remove registry keys or other artifacts to hide the malware's presence from investigators. |
| **T1027** | Obfuscated Files or Information | The use of `MessagePackLib` provides a compact, non-standard serialization format that helps mask and package data before it is sent over the wire. |
| **T1071** | Application Layer Protocol | The use of standard protocols (TCP/SSL) and "Heartbeat" mechanisms indicates a structured communication method for maintaining contact with C2 infrastructure. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral documentation, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `Window11.exe` (Identified as a primary executable/filename)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   `1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B` (Potential hardcoded key or hash)
*   `87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F` (Potential hardcoded key or hash)

**Other artifacts**
*   **Anti-Analysis:** `DetectSandboxie` (Detection of analysis environments).
*   **C2 Communication Pattern:** Use of **AES-256** for encryption and a heartbeat mechanism (**KeepAlive**, **Ping**) to maintain persistent connections.
*   **Data Serialization:** Usage of **MessagePackLib** for compact data packaging/transmission.
*   **Information Gathering Functions:** `get_MachineName`, `get_UserName`, `GetActiveWindowTitle`, `get_OSFullName`.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: RAT (Remote Access Trojan) / Backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **Robust Command & Control (C2) Infrastructure:** The use of AES-256 encryption, MessagePack serialization for efficient data packaging, and "Heartbeat" mechanisms (`KeepAlive`, `Ping`) are hallmark characteristics of a RAT designed to maintain a persistent, stealthy connection to a remote server.
*   **Advanced Evasion Techniques:** The inclusion of specific modules like `DetectSandboxie`, `Anti_Analysis`, and `DetectManufacturer` indicates the malware is engineered to detect and bypass automated analysis environments and security research tools.
*   **System Profiling & Payload Delivery:** The combination of gathering system information (Machine Name, User, OS details) with capabilities to drop files (`InstallFile`) and clear registry traces (`DeleteSubKeyTree`) points toward a persistent backdoor designed to gather intelligence and execute further malicious actions on the host.
