# Threat Analysis Report

**Generated:** 2026-07-11 14:21 UTC
**Sample:** `045c7c5443695ecd98e2633f005acd9f2c9a84bd1e446472c32a17e710fdaaa2_045c7c5443695ecd98e2633f005acd9f2c9a84bd1e446472c32a17e710fdaaa2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `045c7c5443695ecd98e2633f005acd9f2c9a84bd1e446472c32a17e710fdaaa2_045c7c5443695ecd98e2633f005acd9f2c9a84bd1e446472c32a17e710fdaaa2.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 64,512 bytes |
| MD5 | `0508c6d95c8fee8702499a57b64d642f` |
| SHA1 | `914634976a4051125d67f560032842a158292cb7` |
| SHA256 | `045c7c5443695ecd98e2633f005acd9f2c9a84bd1e446472c32a17e710fdaaa2` |
| Overall entropy | 5.398 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1681166197 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 61,440 | 5.435 | No |
| `.rsrc` | 2,048 | 4.885 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **599** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v4.0.30319
#Strings
	>	f	u	

%
;
G
M
S

Action`10
<>c__DisplayClass2_0
<Read>b__0
<>p__0
<>9__2_1
<Read>b__2_1
IEnumerable`1
CallSite`1
List`1
__StaticArrayInitTypeSize=32
Microsoft.Win32
user32
ToUInt32
ReadInt32
ToInt32
SwapInt32
X509Certificate2
<>o__3
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
CHROME8
get_UTF8
<Module>
MessagePackLib.<PrivateImplementationDetails>
SystemParametersInfoA
1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B
ES_SYSTEM_REQUIRED
ES_DISPLAY_REQUIRED
MapNameToOID
_hookID
get_FormatID
EXECUTION_STATE
87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F
get_ASCII
offlineKL
WHKEYBOARDLL
AppdataL
WM_KEYDOWN
LASTINPUTINFO
System.IO
AppdataR
uptimeToDHMS
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
LowLevelKeyboardProc
dwThreadId
GetWindowThreadProcessId
lpdwProcessId
GetProcessById
EndRead
BeginRead
idThread
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MessagePackLib.MessagePack.WriteTools.WriteBoolean` | `0x4026b9` | 65464 | ✓ |
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x4079a4` | 58972 | ✓ |
| `method.Client.Handle_Packet.Packet.Read` | `0x404e68` | 4064 | ✓ |
| `method.Client.Helper.IdSender.SendInfo` | `0x403898` | 2568 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.DecodeFromStream` | `0x406d80` | 1556 | ✓ |
| `method.Client.Helper.LimeLogger.HookCallback` | `0x404394` | 936 | ✓ |
| `method.Client.Connection.ClientSocket.InitializeClient` | `0x402a90` | 844 | ✓ |
| `method.Client.Install.NormalStartup.Install` | `0x40324c` | 744 | ✓ |
| `method.Client.Connection.ClientSocket.ReadServertData` | `0x402e64` | 484 | ✓ |
| `method.Client.Algorithm.Aes256.Decrypt` | `0x4062bc` | 448 | ✓ |
| `method.Client.Settings.InitializeSettings` | `0x402800` | 364 | ✓ |
| `method.Client.Algorithm.Aes256.Encrypt` | `0x406164` | 344 | ✓ |
| `method.MessagePackLib.MessagePack.WriteTools.WriteInteger` | `0x4077d4` | 324 | ✓ |
| `method.Client.Helper.Anti_Analysis.DetectManufacturer` | `0x4035dc` | 316 | ✓ |
| `method.Client.Connection.ClientSocket.Send` | `0x403048` | 312 | ✓ |
| `entry0` | `0x4026d8` | 296 | ✓ |
| `method.Client.Handle_Packet.Packet.Invoke` | `0x405e48` | 288 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.Encode2Stream` | `0x407400` | 248 | ✓ |
| `method.Client.Helper.Methods.Antivirus` | `0x404a58` | 236 | ✓ |
| `method.Client.Helper.Methods.uptimeToDHMS` | `0x404904` | 220 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.WriteMap` | `0x406794` | 200 | ✓ |
| `method.MessagePackLib.MessagePack.WriteTools.WriteString` | `0x40763c` | 200 | ✓ |
| `method.MessagePackLib.MessagePack.ReadTools.ReadString` | `0x40757c` | 192 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.ForcePathObject` | `0x406c48` | 188 | ✓ |
| `method.Client.Settings..cctor` | `0x4029dc` | 180 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.WirteArray` | `0x40685c` | 180 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.GetAsBytes` | `0x406af4` | 176 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.GetAsUInt64` | `0x406910` | 168 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.GetAsInteger` | `0x4069b8` | 168 | ✓ |
| `method.Client.Helper.IdSender.Firefox` | `0x4042a0` | 164 | ✓ |

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
- [`code/method.Client.Helper.IdSender.Firefox.c`](code/method.Client.Helper.IdSender.Firefox.c)
- [`code/method.Client.Helper.IdSender.SendInfo.c`](code/method.Client.Helper.IdSender.SendInfo.c)
- [`code/method.Client.Helper.LimeLogger.HookCallback.c`](code/method.Client.Helper.LimeLogger.HookCallback.c)
- [`code/method.Client.Helper.Methods.Antivirus.c`](code/method.Client.Helper.Methods.Antivirus.c)
- [`code/method.Client.Helper.Methods.uptimeToDHMS.c`](code/method.Client.Helper.Methods.uptimeToDHMS.c)
- [`code/method.Client.Install.NormalStartup.Install.c`](code/method.Client.Install.NormalStartup.Install.c)
- [`code/method.Client.Settings..cctor.c`](code/method.Client.Settings..cctor.c)
- [`code/method.Client.Settings.InitializeSettings.c`](code/method.Client.Settings.InitializeSettings.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.DecodeFromStream.c`](code/method.MessagePackLib.MessagePack.MsgPack.DecodeFromStream.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.Encode2Stream.c`](code/method.MessagePackLib.MessagePack.MsgPack.Encode2Stream.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.ForcePathObject.c`](code/method.MessagePackLib.MessagePack.MsgPack.ForcePathObject.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.GetAsBytes.c`](code/method.MessagePackLib.MessagePack.MsgPack.GetAsBytes.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.GetAsInteger.c`](code/method.MessagePackLib.MessagePack.MsgPack.GetAsInteger.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.GetAsUInt64.c`](code/method.MessagePackLib.MessagePack.MsgPack.GetAsUInt64.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.WirteArray.c`](code/method.MessagePackLib.MessagePack.MsgPack.WirteArray.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.WriteMap.c`](code/method.MessagePackLib.MessagePack.MsgPack.WriteMap.c)
- [`code/method.MessagePackLib.MessagePack.ReadTools.ReadString.c`](code/method.MessagePackLib.MessagePack.ReadTools.ReadString.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteBoolean.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteBoolean.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteInteger.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteInteger.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteString.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteString.c)
- [`code/method.MessagePackLib.MessagePack.Zip.Compress.c`](code/method.MessagePackLib.MessagePack.Zip.Compress.c)

## Behavioral Analysis

Based on the provided strings and decompiled code, here is an analysis of the binary's behavior:

### Core Functionality
The sample appears to be a **Remote Access Trojan (RAT)** or a sophisticated **Information Stealer**. It is designed to collect system information, intercept user input, and communicate with a remote server using encrypted channels. The use of "MessagePack" indicates a structured, binary-based protocol for transmitting data between the infected host and the attacker's command-and-control (C2) server.

### Suspicious & Malicious Behaviors
The following behaviors are highly indicative of malicious intent:

*   **Spyware & Keylogging:**
    *   The presence of `WHKEYBOARDLL`, `LowLevelKeyboardProc`, and `GetKeyState` indicates the malware captures keystrokes (keylogging). 
    *   The string `offlineKL` likely refers to an "Offline Keylogger" component.
*   **Information Gathering (Profiling):**
    *   The malware collects extensive system metadata, including:
        *   Machine name and OS details (`get_MachineName`, `get_OSFullName`).
        *   User information (`get_UserName`).
        *   Active window information (`GetActiveWindowTitle`, `GetProcessName`).
        *   Hardware environment checks (e.g., `ES_SYSTEM_REQUIRED`, `ES_DISPLAY_REQUIRED` to ensure it is running on a physical machine rather than a server).
*   **Evasion & Anti-Analysis:**
    *   **Sandbox Detection:** The string `DetectSandboxie` specifically targets a popular tool used by malware analysts.
    *   **Timing/Idle Checks:** Use of `GetLastInputTime` and `uptimeToDHMS` are common techniques to determine if the system is being actively monitored or used by a human, potentially delaying execution if a sandbox environment is suspected.
*   **Network Communication & Encryption:**
    *   The binary employs high-grade encryption for its communications: `Aes256`, `Sha256`, and `HMACSHA256`.
    *   It utilizes `SslClient` and `TcpClient` to establish connections. The use of `MessagePackLib` suggests it packs data into a compact binary format before sending, which can make network traffic harder to inspect via standard packet sniffers compared to plain-text protocols.
*   **File Manipulation & Persistence:**
    *   Functions like `DownloadFile`, `InstallFile`, and `SaveBytesToFile` suggest that the malware can download additional modules (staged payloads) or modify local files to ensure persistence or to exfiltrate stolen data.

### Notable Techniques & Patterns
*   **Obfuscation via Managed Code:** The repetitive decompilation of various functions into the same name (`method.MessagePackLib.MessagePack.WriteTools.WriteBoolean`) suggests this is likely a **.NET executable**. The "messy" disassembly in `entry0` often occurs when decompilers struggle to map JIT (Just-In-Time) compiled code or heavily obfuscated managed code into C structures.
*   **Sophisticated Protocol:** By using **MessagePack**, the author attempts to hide the structure of the commands being sent by the attacker, making it harder for automated network security systems to flag specific "malicious" strings in transit.
*   **Multi-Stage Capability:** The inclusion of `DecodeFromFile` and `InstallFile` indicates a modular design where the initial "loader" may only be responsible for unpacking or downloading the primary malicious payload.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided report to the corresponding MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1056.001** | Keylogging | The use of `WHKEYBOARDLL`, `LowLevelKeyboardProc`, and `GetKeyState` confirms the capability to capture user keystrokes for credential theft. |
| **T1082** | System Information Discovery | The malware collects metadata such as machine name, OS details, and user information to perform host profiling. |
| **T1497** | Virtualization/Sandbox Detection | The specific checks for `DetectSandboxie` and hardware requirements (e.g., `ES_SYSTEM_REQUIRED`) are used to evade analysis environments. |
| **T1573** | Encrypted Channel | The use of `Aes256`, `Sha256`, and `SslClient` indicates the employment of encrypted communication to hide malicious traffic from network defenders. |
| **T1027** | Obfuscated Files or Information | The use of MessagePack is a deliberate attempt to mask data structures and command strings within the network protocol. |
| **T1105** | Ingress Tool Transfer | The `DownloadFile` and `InstallFile` functions indicate that the malware can fetch additional modules/payloads from a remote server. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized as requested.

### **IP addresses / URLs / Domains**
*None identified.* (The behavior report mentions C2 communication, but no specific hardcoded IP addresses or domains were present in the raw string dump.)

### **File paths / Registry keys**
*None identified.* (Strings like `AppdataL` and `AppdataR` appear to be internal variable names for the application logic rather than absolute system paths.)

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
The following hex strings were identified within the code. These likely serve as unique identifiers, encryption keys, or specific signatures used by the malware's communication protocol (MessagePack):
*   `1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B`
*   `87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F`

### **Other artifacts**
*   **Detection/Evasion Markers:**
    *   `DetectSandboxie` (Specific check for common analysis tools)
    *   `offlin_KL` (Likely internal identifier for an "Offline Keylogger" component)
*   **Communication Protocols:**
    *   `MessagePackLib` / `MsgPackType` (Indicates the use of a binary serialization format to obfuscate C2 traffic)
*   **Encryption/Security Contexts:**
    *   `Aes256`
    *   `Sha256`
    *   `HMACSHA256`
    *   `SslClient` / `TcpClient` (Infrastructure components for establishing encrypted tunnels)
*   **Behavioral Indicators:**
    *   `WHKEYBOARDLL` / `LowLevelKeyboardProc` (Indicates a high-level keylogging hook)
    *   `GetActiveWindowTitle` / `get_ProcessName` (Information gathering/Spyware behavior)

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1.  **Malware family:** custom
2.  **Malware type:** RAT / Infostealer
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Spyware & Data Theft Capability:** The inclusion of `WHKEYBOARDLL` and `GetKeyState` confirms active keylogging, while the collection of machine details, active windows, and user information indicates a primary goal of stealing sensitive data from the host.
    *   **Sophisticated Communication & Obfuscation:** Use of **MessagePack** for serialized data transmission combined with **AES-256/HMACSHA256** encryption suggests a professional level of effort to hide C2 traffic and evade detection by traditional network security tools.
    *   **Advanced Evasion Techniques:** The presence of specific anti-analysis checks (e.g., `DetectSandboxie` and hardware environment checks) indicates the malware is designed to detect analysis environments and bypass automated sandboxes before deploying its full capabilities.
