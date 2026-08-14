# Threat Analysis Report

**Generated:** 2026-08-10 17:02 UTC
**Sample:** `0dda9bf0db4fb70ac42763b5ac834d6f916b2f2c97fb5c7489075a482d6a1d4a_0dda9bf0db4fb70ac42763b5ac834d6f916b2f2c97fb5c7489075a482d6a1d4a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0dda9bf0db4fb70ac42763b5ac834d6f916b2f2c97fb5c7489075a482d6a1d4a_0dda9bf0db4fb70ac42763b5ac834d6f916b2f2c97fb5c7489075a482d6a1d4a.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 133,120 bytes |
| MD5 | `84907d4e415001f7b4ab022c76fc8354` |
| SHA1 | `a0ba383462566c614e76eb551349e55b47054c89` |
| SHA256 | `0dda9bf0db4fb70ac42763b5ac834d6f916b2f2c97fb5c7489075a482d6a1d4a` |
| Overall entropy | 5.452 |
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
| `.rsrc` | 71,680 | 4.484 | No |
| `.reloc` | 512 | 0.061 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1011** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
pjX	(
pjX	(
v4.0.30319
#Strings
 l8+	d
-6Fk
P ] h cf
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
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x406558` | 39474 | ✓ |
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

Based on the provided disassembly and string symbols, here is an analysis of the binary's functionality and behavior:

### Core Functionality and Purpose
The sample appears to be a **sophisticated malware agent**, likely a **Remote Access Trojan (RAT)** or a **botnet client**. It is designed to establish a persistent connection with a Command and Control (C2) server, receive commands from the attacker, and perform various actions on the infected host.

### Suspicious or Malicious Behaviors
*   **Anti-Analysis & Evasion:** 
    *   The binary contains explicit components for anti-analysis: `method.Client.Helper.Anti_Analysis.IsServerOS` (used to detect if the code is running in a virtualized/server environment common in malware labs) and `method.Client.Helper.AntiProcess.Block`.
    *   **Code Obfuscation:** A high number of functions share the identical name `method.MessagePackLib.MessagePack.WriteTools.WriteBoolean` despite being associated with vastly different tasks (Encryption, Camera usage, Network Sending). This is a classic technique to hinder decompilation and confuse analysts by stripping or mangling original metadata.
*   **Command & Control (C2) Communication:**
    *   The use of **MessagePack** indicates the use of an efficient binary serialization format for network communication. This helps hide the structure of the data being sent to/from the server compared to plain JSON or XML.
    *   It includes components for standard C2 operations: `ClientSocket.Send`, `ReadServertData`, and `SendInfo`.
*   **Cryptographic Operations:** 
    *   The inclusion of `Aes256` and `HMACSHA256` indicates that the communication between the malware and its server is likely encrypted to evade Network Intrusion Detection Systems (NIDS).
*   **Information Gathering & Spyware Capabilities:**
    *   **HWID Generation:** The `HwidGen.HWID` routine suggests it identifies unique machines (common for botnet management or "locking" a license to a specific victim).
    *   **Spying:** The inclusion of `Camera` and `havecamera` symbols strongly indicates functionality to activate the device's webcam.
*   **Memory Manipulation:** 
    *   The `PatchMem` function suggests it may perform in-memory patching of other processes or itself to hide its presence or bypass security software hooks.

### Notable Techniques or Patterns
*   **Obfuscated Entry Point (`entry0`):** The decompiled code for `entry0` is heavily cluttered with "junk" arithmetic and complex bitwise operations (e.g., `CONCAT31`, `CARRY1`). This is a common technique to break the decompiler's ability to generate clean C code, making it harder for humans to follow the logic.
*   **Packed/Stripped Metadata:** The repetition of `WriteBoolean` across unrelated functions suggests that the original .NET metadata was intentionally stripped or modified before compilation to hinder static analysis tools.
*   **Standard Malware Toolkit:** The naming conventions (e.g., `Client.Algorithm`, `Client.Helper`) suggest this might be based on a known malware framework or "builder" that provides various modules for an attacker to toggle.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The repetition of `WriteBoolean` across different functions and the use of "junk" arithmetic in `entry0` are designed to hinder manual analysis and de-compilation. |
| T1573 | Encrypted Channel | The implementation of AES-256 and HMAC-SHA256 is used to encrypt C2 communications, making it harder for NIDS to detect malicious traffic. |
| T1112 | Modify Host Memory | The `PatchMem` function indicates the malware modifies memory (either its own or other processes) to bypass security hooks or hide its presence. |
| T1082 | System Information Discovery | The use of `HwidGen` and `IsServerOS` checks suggests the malware gathers system-specific details to fingerprint the environment or identify unique victims. |
| T1071 | Application Layer Protocol | The utilization of MessagePack as a binary serialization format allows the malware to communicate with its C2 server using a structured, non-plain-text protocol. |

---

## Indicators of Compromise

Based on the provided string dump and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

**File paths / Registry keys**
*   *(None identified; standard .NET libraries like `System.IO` and `Microsoft.Win32` were excluded as common system components.)*

**Mutex names / Named pipes**
*   *(No specific named mutexes or pipe strings were identified; only generic status flags such as `PipeConnected` and `PipeDisconnected` were present.)*

**Hashes**
The following 192-bit (48-character) hex strings were identified. These likely represent cryptographic keys, salts, or unique identifiers used within the malware's logic:
*   `D84F4C120005F1837DC65C04181F3DA9466B123FC369C359A301BABC12061570`
*   `E123F60E9FC6E974D1381F2F15FB19E7960628CC8925D65E344C2F2BDC64F424`
*   `CABAFE20CFEA6C92D3377C14650461E190857D4813934B5562233C314AAFBB5`

**Other artifacts**
*   **C2 Communication Pattern:** Utilization of **MessagePack** for binary serialization to mask data structures.
*   **Encryption Standards:** Usage of `Aes256` and `HMACSHA256` for C2 communication.
*   **Anti-Analysis / Evasion:** 
    *   `method.Client.Helper.Anti_Analysis.IsServerOS` (Environment checking)
    *   `method.Client.Helper.AntiProcess.Block` (Process blocking/evasion)
    *   Decompiler evasion via "junk" instructions in `entry0` (e.g., `CONCAT31`, `CARRY1`).
*   **Spyware Capabilities:** Detection of hardware for camera access (`Camera`, `havecamera`).
*   **Obfuscation Technique:** Intentional metadata stripping/mangling where multiple unrelated functions share the same name: `method.MessagePackLib.MessagePack.WriteTools.WriteBoolean`.
*   **Memory Manipulation:** Presence of a `PatchMem` function, likely used for in-memory patching or injection.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: RAT
3. **Confidence**: High
4. **Key evidence**:
    *   **Spyware & Remote Control Capabilities:** The presence of `Camera` and `havecamera` symbols, alongside `PatchMem` functionality and a structured C2 communication system (MessagePack), are primary indicators of a Remote Access Trojan designed for surveillance and remote command execution.
    *   **Sophisticated Evasion Techniques:** The malware employs advanced anti-analysis measures, including environment checks (`IsServerOS`), deliberate decompiler obfuscation via "junk" instructions in `entry0`, and stripped metadata to hide its true functionality from automated tools.
    *   **Robust C2 Infrastructure:** The use of industry-standard encryption (AES-256, HMAC-SHA256) combined with binary serialization (MessagePack) indicates a high level of sophistication intended to bypass Network Intrusion Detection Systems (NIDS).
