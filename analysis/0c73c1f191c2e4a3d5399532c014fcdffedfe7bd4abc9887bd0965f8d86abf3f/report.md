# Threat Analysis Report

**Generated:** 2026-07-30 11:25 UTC
**Sample:** `0c73c1f191c2e4a3d5399532c014fcdffedfe7bd4abc9887bd0965f8d86abf3f_0c73c1f191c2e4a3d5399532c014fcdffedfe7bd4abc9887bd0965f8d86abf3f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c73c1f191c2e4a3d5399532c014fcdffedfe7bd4abc9887bd0965f8d86abf3f_0c73c1f191c2e4a3d5399532c014fcdffedfe7bd4abc9887bd0965f8d86abf3f.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 66,048 bytes |
| MD5 | `85700f51c13481313d4c10c292969b1b` |
| SHA1 | `bdf21e46eea363c2dad4e939a3ef9d5519437989` |
| SHA256 | `0c73c1f191c2e4a3d5399532c014fcdffedfe7bd4abc9887bd0965f8d86abf3f` |
| Overall entropy | 5.79 |
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
| `.text` | 60,416 | 5.836 | No |
| `.rsrc` | 4,608 | 5.033 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **969** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
pjX	(
pjX	(
v4.0.30319
#Strings
-6Fk
a n y cf
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
ProcessNotInJob
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MessagePackLib.MessagePack.WriteTools.WriteBoolean` | `0x402759` | 65464 | ✓ |
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x406558` | 39630 | ✓ |
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

Based on the provided disassembly and string analysis, this binary appears to be a **malicious client application**, likely a "cheat" or "bot" for an online game or a piece of malware designed for remote communication. It incorporates significant anti-analysis techniques and utilizes advanced encryption/serialization for its communication.

### Core Functionality and Purpose
*   **Encrypted Networking:** The presence of `Aes256`, `HMACSHA256`, `GetIV`, and `MessagePack` indicates the application is designed to send and receive data from a remote server while encrypting that data to evade network security inspection.
*   **Data Serialization:** Use of the **MessagePack** library suggests it handles complex, structured data packets, which is common in high-performance game protocols or botnets to minimize bandwidth usage while maintaining complex instructions.
*   **Client Architecture:** The presence of `Client.Connection`, `Client.Install`, and `ReadServertData` (sic) confirms this is a "client" application designed to interact with a backend server.

### Suspicious or Malicious Behaviors
*   **Anti-Analysis & Anti-Debugging:** 
    *   The code contains specific functions like `AntiProcess.Block`, `Anti_Analysis.IsServerOS`, and `PatchMem`. These are used to detect if the sample is running in a virtual machine, debugger, or analysis sandbox.
    *   `PatchMem` suggests it may attempt to modify its own memory or the memory of other processes to hide its behavior or inject code.
*   **Hardware Identification (HWID):** 
    *   The inclusion of `HwidGen.HWID` is a common tactic in "cheats" and malware to uniquely identify a victim's machine, ensuring that a compromised account/license cannot be used on multiple machines.
*   **Information Gathering:**
    *   The string `havecamera` suggests the binary may check for available peripherals or capabilities of the host system, which can be a precursor to unauthorized data collection or surveillance.

### Notable Techniques and Patterns
*   **Heavy Obfuscation:** Most functions (e.g., `WriteBoolean`, `Decrypt`, `Send`) resulted in "broken" C pseudocode consisting only of basic additions. This is a hallmark of **compiler-level obfuscation** (such as OLLVM) or high-level packing, designed to break the decompiler's ability to analyze logic flow.
*   **Complex Logic Hiding:** The `entry0` function contains "junk" instructions and overlapping code segments (`WARNING: Instruction at ... overlaps`). This is a deliberate tactic to confuse automated analysis tools and human analysts.
*   **Custom Communication Layer:** By wrapping `MessagePack` inside its own `WriteTools` class, the author creates a custom layer of abstraction that makes it harder to map out exactly what information (e.g., keystrokes, coordinates, personal info) is being exfiltrated.

### Summary for Incident Response
This binary should be treated as **highly suspicious**. It contains hallmarks of modern "cheat" software or sophisticated malware:
1.  **Evasion:** Actively checks for analysis environments.
2.  **Encryption:** Uses high-grade encryption (AES-256) for command-and-control (C2) traffic.
3.  **Obfuscation:** Heavily utilizes techniques to hinder reverse engineering.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of OLLVM, junk instructions, and overlapping code segments is designed to hinder reverse engineering and automated analysis. |
| T1497 | Virtualization/Sandbox Detection | Functions like `AntiProcess.Block` and `IsServerOS` are used to detect if the binary is running in a research environment. |
| T1505.003 | Debugger Detection | The inclusion of specific anti-debugging routines aims to prevent analysts from attaching debuggers to inspect execution flow. |
| T1573 | Encrypted Channel | The use of AES-256 and HMACSHA256 ensures that communication between the client and the server remains encrypted to evade detection. |
| T1082 | System Information Discovery | The inclusion of `HwidGen` and `havecamera` checks indicates the gathering of specific hardware identifiers and peripheral capabilities. |
| T1020 | Protocol Tunneling | The use of a custom communication layer wrapping MessagePack suggests an attempt to mask the nature of the data being transmitted over the network. |

---

## Indicators of Compromise

Based on the strings provided and the accompanying behavioral analysis, here is the extracted list of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: While `Microsoft.Win32` was present in strings, it refers to a .NET namespace rather than a specific registry path.)

### **Mutex names / Named pipes**
*   *None identified.* (Note: The term `PipeConnected` appears as a status flag/constant but does not provide a specific named pipe path.)

### **Hashes**
The following strings are identified as 40-character hexadecimal values, likely used for internal identification or as unique signatures within the binary logic:
*   `D84F4C120005F1837DC65C04181F3DA9466B123FC369C359A301BABC12061570`
*   `E123F60E9FC6E974D1381F2F15FB19E7960628CC8925D65E344C2F2BDC64F424`
*   `CABAFE20CFEA6C92D3377C14650461E190857D48D13934B5562233C314AAFBB5`

### **Other artifacts**
*   **Encryption/Communication Protocols:** 
    *   `Aes256` (Used for data encryption)
    *   `HMACSHA256` (Used for integrity checking)
    *   `MessagePack` (Used for serialization of complex data structures)
*   **Anti-Analysis Indicators:**
    *   `PatchMem` (Potential code injection or self-patching)
    *   `AntiProcess.Block` / `Anti_Analysis.IsServerOS` (Evasion techniques against VMs and sandboxes)
*   **Information Gathering/Persistence:**
    *   `havecamera` (Hardware/capability scanning)
    *   `HwidGen.HWID` (Hardened unique machine identification)
*   **Capabilities:**
    *   `ReadServertData` (Client-server communication structure)
    *   `GetIV`, `set_IV`, `GenerateIV` (Cryptographic initialization vectors)

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1. **Malware family:** custom
2. **Malware type:** RAT (Remote Access Trojan) / Backdoor
3. **Confidence:** High
4. **Key evidence:**
    *   **Advanced Evasion & Obfuscation:** The use of OLLVM-style obfuscation, "junk" instructions, and specific anti-debugging/anti-VM functions (`AntiProcess.Block`, `IsServerOS`) indicates a high level of intent to bypass security analysts.
    *   **Encrypted Command & Control (C2):** The combination of AES-256 encryption, HMAC signatures, and MessagePack serialization suggests a sophisticated infrastructure designed to hide data exfiltration and remote instructions from network monitoring.
    *   **Information Gathering Capabilities:** The presence of `HwidGen` for unique device identification and `havecamera` checks are classic indicators of a Remote Access Trojan (RAT) intended to identify victims and gather system intelligence.
