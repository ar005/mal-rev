# Threat Analysis Report

**Generated:** 2026-08-19 00:45 UTC
**Sample:** `1080826aacb388d5163487f739c15a438307d6ed2f4b1c753eba12ec4850ba92_1080826aacb388d5163487f739c15a438307d6ed2f4b1c753eba12ec4850ba92.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1080826aacb388d5163487f739c15a438307d6ed2f4b1c753eba12ec4850ba92_1080826aacb388d5163487f739c15a438307d6ed2f4b1c753eba12ec4850ba92.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 66,048 bytes |
| MD5 | `1687803de9269d78f982bdaa53ea053f` |
| SHA1 | `4dab0d5eb212c3167e1825f4d98c7f1661365791` |
| SHA256 | `1080826aacb388d5163487f739c15a438307d6ed2f4b1c753eba12ec4850ba92` |
| Overall entropy | 5.788 |
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
| `.text` | 60,416 | 5.833 | No |
| `.rsrc` | 4,608 | 5.041 | No |
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
 n8+	d
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
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x406558` | 39586 | ✓ |
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

Based on the provided disassembly and string analysis, here is an analysis of the binary's behavior:

### Core Functionality
The binary appears to be a **malware loader or bot agent** (e.g., a remote access trojan/RAT component or a malicious "downloader"). It is designed to communicate with a Command & Control (C2) server, receive instructions, and perform actions on the host machine while actively attempting to evade detection.

The presence of **MessagePack** libraries suggests that the program uses this format for structured data serialization when communicating over the network, which helps it mimic legitimate traffic or obscure its internal commands.

### Suspicious & Malicious Behaviors
*   **Anti-Analysis & Anti-Debugging:** The string list explicitly includes terms like `Antivirus`, `Anti_Analysis`, and `AntiProcess`. These indicate the program checks for the presence of security software, sandboxes, or analysis tools before executing its primary payload.
*   **Environment Validation:** Features like `IsServerOS` suggest the malware checks if it is running on a cloud/virtualized server (common in analysis labs) versus a physical "target" machine.
*   **Payload Protection & Encryption:** The inclusion of `AES256`, `HMACSHA256`, and specific routines for `Encrypt` and `Decrypt` suggests that communication with the C2 server is encrypted, and local configuration files may be protected against inspection.
*   **Machine Fingerprinting:** The presence of `HwidGen` (Hardware ID Generation) indicates the malware identifies unique characteristics of the infected machine to track victims or manage "licenses" for an infection.
*   **Memory Manipulation:** The function `PatchMem` suggests the code may modify its own memory space at runtime, likely to decrypt further stages of a payload or to clear traces of malicious behavior.
*   **Evidence of Sophisticated Evasion:** The `entry0` function exhibits signs of **anti-disassembly**. The warnings regarding "bad instruction data" and "overlapping instructions," combined with complex math and bitwise operations on hardcoded offsets, suggest the use of a packer or an obfuscator to hinder static analysis.

### Notable Techniques & Patterns
*   **Symbol Obfuscation:** A significant number of functions are labeled as `method...WriteBoolean`. This is a hallmark of **code stripping/obfuscation**, where original function names (like `Decrypt`, `Send`, and `GetHWID`) have been replaced with generic names or consolidated into common stubs to confuse analysts.
*   **Custom Serialization:** By using **MessagePack** instead of standard JSON or XML, the author attempts to hide the structure of the packets being sent to and from the C2 server.
*   **Evasive Networking:** The use of `ClientSocket` and `SendInfo` combined with `AES256` indicates a high level of effort to maintain a stealthy connection to the remote infrastructure.

### Summary for Incident Response
This is a sophisticated piece of malware. It contains multiple layers of protection, including:
1.  **Active Evasion:** Checks for debuggers and antivirus.
2.  **Obfuscation:** Hidden functionality through symbol mangling.
3.  **Encrypted Communication:** Use of AES-256 to secure C2 traffic.
4.  **Anti-Analysis Packaging:** Using anti-disassembly tricks in the entry point to hide the primary payload's logic.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox | The "Anti_Analysis," "Antivirus," and "IsServerOS" checks indicate efforts to detect if the malware is running in a lab environment. |
| **T1027** | Software Packing | The use of `PatchMem` for de-obfuscation, along with anti-disassembly tricks (overlapping instructions), indicates a packed or obfuscated binary. |
| **T1569.001** | Obfuscated Files or Information | The use of MessagePack and "method...WriteBoolean" symbol stripping masks the program's internal logic and data structures. |
| **T1573** | Encrypted Channel | The implementation of AES256 and HMACSHA256 indicates that the malware uses encrypted communication to interact with its C2 server. |
| **T1036** | Masquerading | Using generic function names (symbol obfuscation) and potentially mimicking legitimate traffic via MessagePack helps the malware blend in. |
| **T1030** | Data Manipulation | The use of `HwidGen` to identify unique machine characteristics allows the attacker to track victims and manage specific infection profiles. |

### Summary of Mapping Notes:
*   **Evasion Focus:** The majority of the behaviors (T1497, T1027, T1569.001) fall under the **Defense Evasion** tactic, specifically aimed at preventing a security analyst from successfully deconstructing the malware's capabilities.
*   **Command and Control Focus:** The use of encryption (T1573) and custom serialization (MessagePack) falls under the **Command and Control** tactic to ensure the communication remains covert and resilient against network-based inspection.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: `Microsoft.Win32` is a standard .NET namespace and not a specific registry path).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   `D84F4C120005F1837DC65C04181F3DA9466B123FC369C359A301BABC12061570` (SHA-256)
*   `E123F60E9FC6E974D1381F2F15FB19E7960628CC8925D65E344C2F2BDC64F424` (SHA-256)
*   `CABAFE20CFEA6C92D3377C14650461E190857D48D13934B5562233C314AAFBB5` (SHA-256)

**Other artifacts**
*   **Communication Protocol:** MessagePack (used for serialized C2 communication).
*   **Encryption Algorithms:** AES256, HMACSHA256.
*   **Evasion Strings/Behaviors:** `Anti_Analysis`, `Antivirus`, `AntiProcess` (identified via behavior analysis as indicators of anti-analysis routines).

---

## Malware Family Classification

1. **Malware family**: Unknown (Potential custom loader/bot agent)
2. **Malware type**: Loader / Backdoor
3. **Confidence**: Medium

**Key evidence**:
*   **Sophisticated Evasion & Obfuscation:** The sample utilizes advanced anti-analysis techniques, including `Antivirus` and `IsServerOS` checks, alongside complex "anti-disassembly" tactics (overlapping instructions/complex math) to hinder manual analysis.
*   **Secure C2 Architecture:** The use of **MessagePack** for serialization combined with **AES-256** and **HMAC-SHA256** encryption indicates a professional level of development aimed at masking communication between the bot and its command infrastructure.
*   **Infrastructure Management:** The inclusion of `HwidGen` (Hardware ID Generation) and `PatchMem` functionality suggests the sample is designed to manage unique infection profiles and dynamically decrypt/patch payloads in memory, typical of a multi-stage loader or a persistent backdoor.
