# Threat Analysis Report

**Generated:** 2026-08-15 21:54 UTC
**Sample:** `0f523040c10857d5e03c5f0f88eefee85518ee22505f3a1f5850dcb12a70c94f_0f523040c10857d5e03c5f0f88eefee85518ee22505f3a1f5850dcb12a70c94f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f523040c10857d5e03c5f0f88eefee85518ee22505f3a1f5850dcb12a70c94f_0f523040c10857d5e03c5f0f88eefee85518ee22505f3a1f5850dcb12a70c94f.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 65,536 bytes |
| MD5 | `4069d21bfd62950a43ec54cd74893761` |
| SHA1 | `a0bec3c91c450d05d48030e44e806b36968e136e` |
| SHA256 | `0f523040c10857d5e03c5f0f88eefee85518ee22505f3a1f5850dcb12a70c94f` |
| Overall entropy | 5.8 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1641959262 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 60,416 | 5.828 | No |
| `.rsrc` | 4,096 | 5.218 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **970** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
pjX	(
pjX	(
v4.0.30319
#Strings
 |8+	d
-6Fk
X e p cf
Action`10
InvalidParameter10
D84F4C120005F1837DC65C04181F3DA9466B123FC369C359A301BABC12061570
<>c__DisplayClass5_0
<>c__DisplayClass6_0
<PatchMem>b__0
<GetFiltes>b__0
<>p__0
AbandonedWait0
InvalidParameter11
IEnumerable`1
CallSite`1
List`1
InvalidParameter1
AbandonedWait1
InvalidParameter12
PROCESSENTRY32
Microsoft.Win32
ToUInt32
ReadInt32
ToInt32
SwapInt32
Func`2
X509Certificate2
InvalidParameter2
AbandonedWait2
<>o__53
AbandonedWait63
Func`3
InvalidParameter3
AbandonedWait3
E123F60E9FC6E974D1381F2F15FB19E7960628CC8925D65E344C2F2BDC64F424
WriteUInt64
ToUInt64
GetAsUInt64
SetAsUInt64
ToInt64
SwapInt64
InvalidParameter4
__StaticArrayInitTypeSize=5
CABAFE20CFEA6C92D3377C14650461E190857D48D13934B5562233C314AAFBB5
InvalidParameter5
InvalidImageWin16
ToUInt16
ReadInt16
ToInt16
SwapInt16
HMACSHA256
Aes256
aes256
__StaticArrayInitTypeSize=6
InvalidParameter6
InvalidParameter7
get_UTF8
InvalidParameter8
InvalidParameter9
<Module>
MessagePackLib.<PrivateImplementationDetails>
0C50C67E839472CD612D6033109F5E032987E48E367247F29C0EB30A1D3EB5FC
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
IsServerOS
ES_CONTINUOUS
NTSTATUS
get_IV
set_IV
GenerateIV
PatchETW
value__
Camera
havecamera
NotMappedData
ReadServertData
PropertyData
NoTxfMetadata
PagefileQuota
mscorlib
ProcessInJob
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MessagePackLib.MessagePack.WriteTools.WriteBoolean` | `0x402759` | 65464 | ✓ |
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x406558` | 39590 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.DecodeFromStream` | `0x405934` | 1556 | ✓ |
| `method.Client.Connection.ClientSocket.InitializeClient` | `0x402bb4` | 844 | ✓ |
| `method.Client.Install.NormalStartup.Install` | `0x4036ac` | 760 | ✓ |
| `method.Client.Connection.ClientSocket.Read` | `0x403358` | 564 | ✓ |
| `method.Client.Helper.DInvokeCore.GetExportAddress` | `0x4044a8` | 544 | ✓ |
| `method.Client.Helper.A.GetExportAddress` | `0x40474c` | 544 | ✓ |
| `method.Client.Connection.ClientSocket.ReadServertData` | `0x402f88` | 484 | ✓ |
| `method.Client.Helper.IdSender.SendInfo` | `0x403f28` | 484 | ✓ |
| `method.Client.Algorithm.Aes256.Decrypt` | `0x404f7c` | 448 | ✓ |
| `entry0` | `0x402778` | 396 | ✓ |
| `method.Client.Settings.InitializeSettings` | `0x402904` | 364 | ✓ |
| `method.Client.Algorithm.Aes256.Encrypt` | `0x404e24` | 344 | ✓ |
| `method.Client.Helper.AntiProcess.Block` | `0x4039f4` | 336 | ✓ |
| `method.MessagePackLib.MessagePack.WriteTools.WriteInteger` | `0x406388` | 324 | ✓ |
| `method.Client.Connection.ClientSocket.Send` | `0x40316c` | 312 | ✓ |
| `method.Client.Connection.ClientSocket.Invoke` | `0x40358c` | 288 | ✓ |
| `method.Client.Helper.Anti_Analysis.IsServerOS` | `0x403b44` | 280 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.Encode2Stream` | `0x405fb4` | 248 | ✓ |
| `method.Client.Helper.Camera.EnumMonikers` | `0x403d1c` | 244 | ✓ |
| `method.Client.Helper.Methods.Antivirus` | `0x404184` | 244 | ✓ |
| `method.Client.Helper.HwidGen.HWID` | `0x403e44` | 228 | ✓ |
| `method.Client.Helper.Methods.ClearSetting` | `0x404350` | 212 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.WriteMap` | `0x405348` | 200 | ✓ |
| `method.MessagePackLib.MessagePack.WriteTools.WriteString` | `0x4061f0` | 200 | ✓ |
| `method.MessagePackLib.MessagePack.ReadTools.ReadString` | `0x406130` | 192 | ✓ |
| `method.MessagePackLib.MessagePack.MsgPack.ForcePathObject` | `0x4057fc` | 188 | ✓ |
| `method.Client.Settings..cctor` | `0x402b00` | 180 | ✓ |
| `method.Client.Helper.A.PatchMem` | `0x40496c` | 180 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Client.Algorithm.Aes256.Decrypt.c`](code/method.Client.Algorithm.Aes256.Decrypt.c)
- [`code/method.Client.Algorithm.Aes256.Encrypt.c`](code/method.Client.Algorithm.Aes256.Encrypt.c)
- [`code/method.Client.Connection.ClientSocket.InitializeClient.c`](code/method.Client.Connection.ClientSocket.InitializeClient.c)
- [`code/method.Client.Connection.ClientSocket.Invoke.c`](code/method.Client.Connection.ClientSocket.Invoke.c)
- [`code/method.Client.Connection.ClientSocket.Read.c`](code/method.Client.Connection.ClientSocket.Read.c)
- [`code/method.Client.Connection.ClientSocket.ReadServertData.c`](code/method.Client.Connection.ClientSocket.ReadServertData.c)
- [`code/method.Client.Connection.ClientSocket.Send.c`](code/method.Client.Connection.ClientSocket.Send.c)
- [`code/method.Client.Helper.A.GetExportAddress.c`](code/method.Client.Helper.A.GetExportAddress.c)
- [`code/method.Client.Helper.A.PatchMem.c`](code/method.Client.Helper.A.PatchMem.c)
- [`code/method.Client.Helper.AntiProcess.Block.c`](code/method.Client.Helper.AntiProcess.Block.c)
- [`code/method.Client.Helper.Anti_Analysis.IsServerOS.c`](code/method.Client.Helper.Anti_Analysis.IsServerOS.c)
- [`code/method.Client.Helper.Camera.EnumMonikers.c`](code/method.Client.Helper.Camera.EnumMonikers.c)
- [`code/method.Client.Helper.DInvokeCore.GetExportAddress.c`](code/method.Client.Helper.DInvokeCore.GetExportAddress.c)
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
- [`code/method.MessagePackLib.MessagePack.MsgPack.WriteMap.c`](code/method.MessagePackLib.MessagePack.MsgPack.WriteMap.c)
- [`code/method.MessagePackLib.MessagePack.ReadTools.ReadString.c`](code/method.MessagePackLib.MessagePack.ReadTools.ReadString.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteBoolean.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteBoolean.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteInteger.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteInteger.c)
- [`code/method.MessagePackLib.MessagePack.WriteTools.WriteString.c`](code/method.MessagePackLib.MessagePack.WriteTools.WriteString.c)
- [`code/method.MessagePackLib.MessagePack.Zip.Compress.c`](code/method.MessagePackLib.MessagePack.Zip.Compress.c)

## Behavioral Analysis

Based on the provided disassembly and strings, this binary is highly characteristic of a **malicious loader or a Remote Access Trojan (RAT)**, likely designed for information theft or as part of a botnet. The presence of several high-level .NET components suggests it is an obfuscated .NET assembly.

### Core Functionality
The primary purpose of this code appears to be establishing a controlled communication channel between a local client and a remote server. 
*   **Communication & Data Handling:** It uses **MessagePack**, a compact serialization format, to package data before transmission. This is often used in malware to minimize the size of packets sent to Command & Control (C2) servers.
*   **Encryption:** The code explicitly references **AES-256** and **HMAC-SHA256**. This indicates that all traffic between the victim and the attacker's server is encrypted, likely to bypass Network Intrusion Detection Systems (NIDS).
*   **Client/Server Architecture:** The internal naming conventions (e.g., `Client.Connection`, `ReadServertData`) confirm it is designed as a "client" that receives instructions from a remote handler.

### Suspicious and Malicious Behaviors
The sample contains several indicators of malicious intent:

*   **Anti-Analysis & Anti-Debugging:** 
    *   The inclusion of functions like `Antivirus`, `Block` (under `AntiProcess`), and `IsServerOS` indicates the malware checks if it is being run in a sandbox, a virtual machine, or under the observation of security software before "unpacking" its full capabilities.
    *   `PatchMem` suggests the ability to modify memory in real-time, often used to hook system APIs or patch out security protections.
*   **Information Gathering (Spyware/Tracking):**
    *   The inclusion of `hwid`, `HwidGen`, and references to `Camera` and `havecamera` strongly suggest the malware attempts to identify unique hardware characteristics (to create a "fingerprint" for the victim) and potentially access webcams.
*   **Data Exfiltration:**
    *   The usage of `SendSync` and `ReadServertData` combined with encryption suggests that gathered data (system info, credentials, or files) is sent to a remote IP.

### Notable Techniques and Patterns
*   **Heavy Obfuscation/Packing:** 
    *   A significant red flag is the repetitive decompilation of multiple different functions as `WriteBoolean`. This is a classic sign of **Control Flow Flattening** or symbol stripping by an obfuscator (like ConfuserEX). The decompiler cannot resolve the actual logic because the code has been intentionally mangled to hinder analysis.
*   **Complex Data Serialization:** 
    *   The use of `MessagePack` is a common choice for modern malware developers who want to transmit complex data structures (like system configurations or logs) more efficiently than standard JSON or XML.
*   **Cryptographic Implementation:** 
    *   The presence of high-grade encryption (`AES256`, `HMACSHA256`) suggests the developer intended to hide the "heart" of the malware's communication from security researchers.

### Summary for Incident Response
This binary is **highly suspicious**. It contains clear markers of a multi-stage loader or RAT designed to:
1.  Evade automated sandboxes and manual analysis.
2.  Identify and fingerprint the victim’s hardware.
3.  Communicate with an external server using encrypted, serialized packets. 

**Recommendation:** Treat any host infected by this binary as compromised. Look for persistent network connections over non-standard ports or hidden processes utilizing MessagePack/AES protocols.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files | The use of .NET obfuscation and Control Flow Flattening is designed to hinder reverse engineering and hide the code's actual logic. |
| T1497 | Virtualization/Sandbox Escape | Checks for "Antivirus," "IsServerOS," and specific blocking functions indicate an attempt to detect and evade analysis environments. |
| T1573 | Encrypted Traffic | The implementation of AES-256 and HMAC-SHA256 is used to encrypt communication with the C2 server to bypass network security monitoring. |
| T1082 | System Information Discovery | The collection of "hwid" and hardware fingerprints allows the attacker to uniquely identify and track the victim's machine. |
| T1041 | Exfiltration Over C2 Channel | The use of `SendSync` and `ReadServertData` indicates that gathered information is being transmitted to a remote server via an established channel. |
| T1055 | Process Injection | The "PatchMem" functionality suggests the malware can modify memory in real-time to hook APIs or bypass security protections. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None specific; however, internal logic mentions `PipeConnected` and `PipeDisconnected`, indicating the use of named pipes for inter-process communication or networking.

**Hashes**
The following hex strings were identified in the raw data. These are likely used as unique identifiers, encryption keys, or integrity checks:
*   `D84F4C120005F1837DC65C04181F3DA9466B123FC369C359A301BABC12061570`
*   `E123F60E9FC6E974D1381F2F15FB19E7960628CC8925D65E344C2F2BDC64F424`
*   `CABAFE20CFEA6C92D3377C14650461E190857D48D13934B5562233C314AAFBB5`
*   `0C50C67E839472CD612D6033109F5E032987E48E367247F29C0EB30A1D3EB5FC`
*   `87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F`

**Other artifacts**
*   **C2 Protocols/Serialization:** MessagePack (Used for compact, structured data transmission).
*   **Encryption Schemes:** AES-256, HMAC-SHA256.
*   **Malicious Functions/Capabilities:** 
    *   `PatchMem`: Indicates memory manipulation to bypass security or hook functions.
    *   `hwid`, `HwidGen`: Used for unique victim fingerprinting.
    *   `Camera`, `havecamera`: Evidence of webcam access capabilities.
    *   `SendSync`, `ReadServertData`: Core communication logic between the agent and C2.
*   **Obfuscation Indicators:** 
    *   Presence of common obfuscator artifacts (e.g., repeated `WriteBoolean` mappings suggesting Control Flow Flattening).

---

## Malware Family Classification

1. **Malware family**: custom 
2. **Malware type**: RAT
3. **Confidence**: High
4. **Key evidence**:
    *   **Robust C2 Infrastructure:** The use of MessagePack serialization combined with AES-256 and HMAC-SHA256 encryption indicates a sophisticated, structured communication channel for receiving commands and exfiltrating data.
    *   **Spyware & Surveillance Capabilities:** Specific functions for "hwid" fingerprinting and "camera" access are hallmark features of Remote Access Trojans (RATs) designed for long-term surveillance.
    *   **Advanced Evasion Techniques:** The sample employs both technical obfuscation (Control Flow Flattening) and environmental checks (Antivirus/ServerOS detection) to bypass security software and automated analysis environments.
