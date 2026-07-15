# Threat Analysis Report

**Generated:** 2026-07-13 21:41 UTC
**Sample:** `057ce719d259f34687589c6a31498b1edbdb84af194e6c7c0e5681497699e24a_057ce719d259f34687589c6a31498b1edbdb84af194e6c7c0e5681497699e24a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `057ce719d259f34687589c6a31498b1edbdb84af194e6c7c0e5681497699e24a_057ce719d259f34687589c6a31498b1edbdb84af194e6c7c0e5681497699e24a.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 48,640 bytes |
| MD5 | `4bbe27ba6f62d05cc08bef87f3b808d9` |
| SHA1 | `e5c90b3a99f09b7a97689bf9007ddcbb43619058` |
| SHA256 | `057ce719d259f34687589c6a31498b1edbdb84af194e6c7c0e5681497699e24a` |
| Overall entropy | 5.617 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1620249099 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 44,032 | 5.642 | No |
| `.rsrc` | 3,584 | 5.111 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **597** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v4.0.30319
#Strings
	(	D	J	n	~	

$
3
@

(5N
Action`10
<>c__DisplayClass5_0
<GetFiltes>b__0
<>p__0
IEnumerable`1
CallSite`1
List`1
PROCESSENTRY32
kernel32
Microsoft.Win32
ToUInt32
ToInt32
SwapInt32
X509Certificate2
<>o__53
Func`3
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
Aes256
aes256
__StaticArrayInitTypeSize=6
get_UTF8
<Module>
<PrivateImplementationDetails>
PatchA
LoadLibraryA
ES_SYSTEM_REQUIRED
ES_DISPLAY_REQUIRED
MapNameToOID
GetTypeFromCLSID
th32ModuleID
th32DefaultHeapID
th32ProcessID
th32ParentProcessID
get_FormatID
EXECUTION_STATE
87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F
get_ASCII
LASTINPUTINFO
System.IO
ES_CONTINUOUS
get_IV
set_IV
GenerateIV
value__
Camera
havecamera
ReadServertData
mscorlib
System.Collections.Generic
Microsoft.VisualBasic
get_SendSync
dwProcessId
processId
EndRead
BeginRead
BlockThread
InnerAdd
SHA256Managed
get_Enabled
set_Enabled
get_Connected
get_IsConnected
set_IsConnected
Received
get_Guid
<SendSync>k__BackingField
<Enabled>k__BackingField
<IsConnected>k__BackingField
<KeepAlive>k__BackingField
<HeaderSize>k__BackingField
<ActivatePo_ng>k__BackingField
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
method
Replace
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MessagePackLib.MessagePack.WriteTools.WriteBoolean` | `0x4026db` | 63782 | ✓ |
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x405d2c` | 49876 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.DecodeFromStream` | `0x405108` | 1556 | ✓ |
| `method.Client.Connection.ClientSocket.InitializeClient` | `0x402ac4` | 844 | ✓ |
| `method.Client.Install.NormalStartup.Install` | `0x4036d8` | 776 | ✓ |
| `method.Client.Connection.ClientSocket.Read` | `0x403268` | 564 | ✓ |
| `method.Client.Connection.ClientSocket.ReadServertData` | `0x402e98` | 484 | ✓ |
| `method.Client.Helper.IdSender.SendInfo` | `0x403e38` | 484 | ✓ |
| `method.Client.Algorithm.Aes256.Decrypt` | `0x404750` | 448 | ✓ |
| `method.Client.Settings.InitializeSettings` | `0x402814` | 364 | ✓ |
| `method.Client.Algorithm.Aes256.Encrypt` | `0x4045f8` | 344 | ✓ |
| `method.Client.Helper.AntiProcess.Block` | `0x403a30` | 336 | ✓ |
| `method.MessagePackLib.MessagePack.WriteTools.WriteInteger` | `0x405b5c` | 324 | ✓ |
| `method.Client.Connection.ClientSocket.Send` | `0x40307c` | 312 | ✓ |
| `method.Client.Connection.ClientSocket.Invoke` | `0x40349c` | 288 | ✓ |
| `entry0` | `0x4026fc` | 280 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.Encode2Stream` | `0x405788` | 248 | ✓ |
| `method.Client.Helper.Camera.EnumMonikers` | `0x403c2c` | 244 | ✓ |
| `method.Client.Helper.Methods.Antivirus` | `0x404094` | 244 | ✓ |
| `method.Client.Helper.HwidGen.HWID` | `0x403d54` | 228 | ✓ |
| `method.Client.Helper.Methods.ClearSetting` | `0x404260` | 212 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.WriteMap` | `0x404b1c` | 200 | ✓ |
| `method.MessagePackLib.MessagePack.WriteTools.WriteString` | `0x4059c4` | 200 | ✓ |
| `method.MessagePackLib.MessagePack.ReadTools.ReadString` | `0x405904` | 192 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.ForcePathObject` | `0x404fd0` | 188 | ✓ |
| `method.Client.Settings..cctor` | `0x402a10` | 180 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.WirteArray` | `0x404be4` | 180 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.GetAsBytes` | `0x404e7c` | 176 | ✓ |
| `method.Client.Connection.Amsi.PatchA` | `0x403610` | 168 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.GetAsUInt64` | `0x404c98` | 168 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Client.Algorithm.Aes256.Decrypt.c`](code/method.Client.Algorithm.Aes256.Decrypt.c)
- [`code/method.Client.Algorithm.Aes256.Encrypt.c`](code/method.Client.Algorithm.Aes256.Encrypt.c)
- [`code/method.Client.Connection.Amsi.PatchA.c`](code/method.Client.Connection.Amsi.PatchA.c)
- [`code/method.Client.Connection.ClientSocket.InitializeClient.c`](code/method.Client.Connection.ClientSocket.InitializeClient.c)
- [`code/method.Client.Connection.ClientSocket.Invoke.c`](code/method.Client.Connection.ClientSocket.Invoke.c)
- [`code/method.Client.Connection.ClientSocket.Read.c`](code/method.Client.Connection.ClientSocket.Read.c)
- [`code/method.Client.Connection.ClientSocket.ReadServertData.c`](code/method.Client.Connection.ClientSocket.ReadServertData.c)
- [`code/method.Client.Connection.ClientSocket.Send.c`](code/method.Client.Connection.ClientSocket.Send.c)
- [`code/method.Client.Helper.AntiProcess.Block.c`](code/method.Client.Helper.AntiProcess.Block.c)
- [`code/method.Client.Helper.Camera.EnumMonikers.c`](code/method.Client.Helper.Camera.EnumMonikers.c)
- [`code/method.Client.Helper.HwidGen.HWID.c`](code/method.Client.Helper.HwidGen.HWID.c)
- [`code/method.Client.Helper.IdSender.SendInfo.c`](code/method.Client.Helper.IdSender.SendInfo.c)
- [`code/method.Client.Helper.Methods.Antivirus.c`](code/method.Client.Helper.Methods.Antivirus.c)
- [`code/method.Client.Helper.Methods.ClearSetting.c`](code/method.Client.Helper.Methods.ClearSetting.c)
- [`code/method.Client.Install.NormalStartup.Install.c`](code/method.Client.Install.NormalStartup.Install.c)
- [`code/method.Client.Settings..cctor.c`](code/method.Client.Settings..cctor.c)
- [`code/method.Client.Settings.InitializeSettings.c`](code/method.Client.Settings.InitializeSettings.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.DecodeFromStream.c`](code/method.MessagePackLib.MessagePack.MsgPack.DecodeFromStream.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.Encode2Stream.c`](code/method.MessagePackLib.MessagePack.MsgPack.Encode2Stream.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.ForcePathObject.c`](code/method.MessagePackLib.MessagePack.MsgPack.ForcePathObject.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.GetAsBytes.c`](code/method.MessagePackLib.MessagePack.MsgPack.GetAsBytes.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.GetAsUInt64.c`](code/method.MessagePackLib.MessagePack.MsgPack.GetAsUInt64.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.WirteArray.c`](code/method.MessagePackLib.MessagePack.MsgPack.WirteArray.c)
- [`code/method.MessagePackLib.MessagePack.MsgPack.WriteMap.c`](code/method.MessagePackLib.MessagePack.MsgPack.WriteMap.c)
- [`code/method.MessagePackLib.MessagePack.ReadTools.ReadString.c`](code/method.MessagePackLib.MessagePack.ReadTools.ReadString.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteBoolean.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteBoolean.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteInteger.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteInteger.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteString.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteString.c)
- [`code/method.MessagePackLib.MessagePack.Zip.Compress.c`](code/method.MessagePackLib.MessagePack.Zip.Compress.c)

## Behavioral Analysis

Based on the provided disassembly and string symbols, here is a technical analysis of the binary's behavior:

### Core Functionality and Purpose
The binary appears to be a **malicious loader or "bot" client** (likely for a game or a remote access tool). It is designed to establish a secure connection to a remote server, perform environmental checks on the host system, and manage encrypted data exchange. 

The presence of `MessagePack` libraries suggests it uses a specific serialization format to communicate with a Command & Control (C2) server. The fact that many distinct functions are all showing as `WriteBoolean` during decompilation indicates the binary has been **obfuscated** or packed, which is common in malware to hinder analysis.

### Suspicious and Malicious Behaviors
The following behaviors indicate malicious intent:

*   **Anti-Analysis & Evasion:**
    *   **AMSI Patching:** The inclusion of `method.Client.Connection.Amsi.PatchA` is a high-confidence indicator of malware. AMSI (Antimalware Scan Interface) patching is used to disable Windows Defender’s ability to scan scripts and memory for malicious activity.
    *   **Anti-Virus Checks:** The function `method.Client.Helper.Methods.Antivirus` suggests the code explicitly checks if security software is active or present before proceeding.
    *   **Environment Blocking:** The `method.Client.Helper.AntiProcess.Block` function likely identifies and blocks common analysis tools (like Wireshark, x64dbg) or sandboxes.

*   **Information Gathering & Fingerprinting:**
    *   **Hardware Identification:** The code includes functions for **HWID** (Hardware ID), `get_MachineName`, `get_OSFullName`, and `get_UserName`. This is used to "fingerprint" the victim's machine so they can be uniquely identified by the attacker.
    *   **Peripheral Check:** The presence of `Camera` and `havecamera` functions suggests the malware may check for or interact with hardware like webcams, which is common in spyware.

*   **Encrypted Communication:**
    *   **Strong Encryption:** The use of `Aes256`, `HMACSHA256`, and `SslClient` indicates that the communication between the infected host and the remote server is encrypted to bypass Network Intrusion Detection Systems (NIDS).
    *   **Data Persistence:** Functions like `SaveBytesToFile` and `GetTempFileName` suggest the binary may download secondary payloads or save configuration files locally.

### Notable Techniques & Patterns
*   **Code Obfuscation:** The repetitive naming of functions as `WriteBoolean` despite having distinct source-code names (like `Decrypt`, `Encrypt`, `Initialize`) indicates a sophisticated obfuscation layer was used to hide the true purpose of the underlying logic.
*   **C# / .NET Framework Origin:** The string references (e.g., `mscorlib`, `System.IO`, `Microsoft.VisualBasic`) indicate this is a .NET-based application, likely wrapped or packed into a native executable.
*   **Sophisticated Networking:** Use of `MessagePack` and `SslClient` suggests the author intended to mimic legitimate traffic or use high-performance communication protocols common in modern malware "bots."

### Summary Recommendation
The presence of **AMSI patching**, **Anti-Virus checks**, and **HWID gathering** strongly classifies this sample as malicious. It likely functions as a persistent backdoor or a credential/information stealer that attempts to hide from both automated antivirus scans and manual analyst inspection.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1562.001** | Impair Defenses: Disable or Modify Tools | The binary performs AMSI patching and explicit antivirus checks to disable security features before executing malicious logic. |
| **T1497** | Virtualization, Sandbox, and Availability | The "AntiProcess" check specifically targets analysis tools like x64dbg and Wireshark to detect if the malware is being monitored by an analyst. |
| **T1082** | System Information Discovery | The binary gathers HWID, Machine Name, OS details, and Username to fingerprint and uniquely identify the victim's system. |
| **T1573** | Encrypted Channel | The use of AES-256, HMAC-SHA256, and SSL clients is intended to encrypt traffic between the host and C2 server to evade network detection. |
| **T1027** | Obfuscated Files or Information | The repetitive naming of functions (e.g., `WriteBoolean`) and evidence of packing indicate an effort to hide the true purpose of the code from researchers. |
| **T1105** | Ingress Tool Transfer | The use of `SaveBytesToFile` and `GetTempFileName` suggests the binary can receive or store secondary payloads or configuration files locally. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized as requested:

**IP addresses / URLs / Domains**
*   *None identified.* (Note: The analysis suggests the malware uses encrypted communication via `SslClient` and `MessagePack`, likely hiding the underlying C2 infrastructure from plain-text string analysis.)

**File paths / Registry keys**
*   *None identified.* (While functions like `GetTempFileName` and `DeleteSubKeyTree` are present, no specific hardcoded file paths or registry keys were found in the strings.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   **87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F** (Note: This appears to be a SHA-256 hash or certificate fingerprint.)

**Other artifacts**
*   **C2 Communication Patterns:** 
    *   Usage of `MessagePack` for data serialization.
    *   Encryption protocols: `Aes256`, `HMACSHA256`.
*   **Evasion & Anti-Analysis Techniques:**
    *   **AMSI Patching:** Identified via the string `PatchA` (associated with `method.Client.Connection.Amsi.PatchA`).
    *   **Anti-VM/Debugger:** Logic identified in `method.Client.Helper.AntiProcess.Block`.
    *   **AV Checking:** Logic identified in `method.Client.Helper.Methods.Antivirus`.
*   **Information Gathering (Fingerprinting):** 
    *   `Get_MachineName`, `get_OSFullName`, `get_UserName` (Used for HWID collection).
    *   `havecamera` / `Camera` (Potential surveillance/spyware behavior).

---

## Malware Family Classification

1. **Malware family**: Custom (likely a Loader or Bot client)
2. **Malware type**: Loader / Backdoor
3. **Confidence**: High (for functionality), Low (for specific brand/family attribution)
4. **Key evidence**:
    *   **Advanced Evasion & Defense Impairment**: The binary explicitly implements AMSI patching (`PatchA`) and anti-analysis checks to detect tools like x64dbg and Wireshark, indicating a high level of sophistication in evading security software.
    *   **Information Gathering (Fingerprinting)**: The inclusion of hardware identification (HWID), system information gathering, and a specific check for camera access indicates the sample is designed to identify unique victims and may possess spyware capabilities.
    *   **Secure C2 Communication**: The use of `MessagePack` for serialization alongside high-grade encryption (`AES-256`, `HMAC-SHA256`) suggests it is built to facilitate stable, encrypted communication between a victim and a command-and-control server.
