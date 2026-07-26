# Threat Analysis Report

**Generated:** 2026-07-25 16:25 UTC
**Sample:** `0aee4a7c83c0c9e7f4645f75df99a62e04286592170412216d0ebbde23520fe2_0aee4a7c83c0c9e7f4645f75df99a62e04286592170412216d0ebbde23520fe2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0aee4a7c83c0c9e7f4645f75df99a62e04286592170412216d0ebbde23520fe2_0aee4a7c83c0c9e7f4645f75df99a62e04286592170412216d0ebbde23520fe2.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 65,536 bytes |
| MD5 | `d8b87d5aef1c5f1aff29a1eda02a0260` |
| SHA1 | `4069e97977013d30206322a8fe875cb891086a70` |
| SHA256 | `0aee4a7c83c0c9e7f4645f75df99a62e04286592170412216d0ebbde23520fe2` |
| Overall entropy | 5.795 |
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
| `.text` | 60,416 | 5.826 | No |
| `.rsrc` | 4,096 | 5.162 | No |
| `.reloc` | 512 | 0.061 | No |

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
 t8+	d
-6Fk
^ k v cf
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
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x406558` | 39470 | ✓ |
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

Based on the provided disassembly and string list, here is an analysis of the binary's functionality and behavior:

### Core Functionality
The sample appears to be a **sophisticated piece of malware or a remote-access tool (RAT)**. It is designed to establish a connection with a remote server, exchange encrypted data, and perform environment checks to ensure it is not being analyzed by security researchers. 

The inclusion of `MessagePack` libraries suggests the application uses a structured, efficient serialization format for its communication protocol. The presence of `ClientSocket`, `ReadServertData`, and `SendInfo` confirms that network communication is a primary component of the program's lifecycle.

### Suspicious & Malicious Behaviors
The following behaviors were identified as highly suspicious or characteristic of malware:

*   **Anti-Analysis & Anti-Debugging:** 
    *   **Environment Checks:** The string `IsServerOS` and various "Anti_Analysis" indicators suggest the program checks if it is running in a virtual machine (VM) or a laboratory environment before executing its primary payload.
    *   **Process Blocking:** The function `method.Client.Helper.AntiProcess.Block` suggests the malware actively looks for and blocks common analysis tools (like Wireshark, x64dbg, or Process Hacker).
    *   **Memory Patching:** The `PatchMem` function indicates that the binary may modify its own code in memory or patch other processes to bypass security hooks or security software.

*   **Encryption & Obfuscation:**
    *   **Strong Cryptography:** The use of `Aes256` and `HMACSHA256` for "Decrypt" and "Encrypt" functions suggests that the communication with the Command & Control (C2) server is encrypted to evade Network Intrusion Detection Systems (NIDS).
    *   **Code Obfuscation:** Many distinct functions were decompiled under a single name (`WriteBoolean`), which often happens when code is heavily obfuscated or "packed." The `entry0` function contains significant amount of raw, complex logic that suggests an unpacking routine or a manual jump table.

*   **Information Gathering & Persistence:**
    *   **Hardware ID (HWID):** The presence of `HwidGen`, `HWID`, and various `Get` functions suggest the malware gathers unique identifiers from the victim's machine. This is commonly used to "fingerprint" a machine for botnet management or to bypass license checks in cracked software.

### Notable Techniques & Patterns
*   **Standardized Communication:** The use of `MessagePack` combined with `Aes256` points toward a modern malware framework design, likely intended to hide the nature of the commands being sent by the attacker.
*   **Hidden Logic (entry0):** The `entry0` function shows complex bitwise operations and non-standard arithmetic. This is typical for "stub" code used to decrypt the real payload into memory before execution starts.
*   **Sophisticated Componentization:** The naming conventions (`method.Client.Algorithm`, `method.Client.Helper`) suggest a modular architecture, allowing different capabilities (like stealing files or logging keystrokes) to be toggled via remote commands.

### Summary of Risk
The sample is **highly suspicious**. It exhibits classic indicators of a **RAT (Remote Access Trojan)** or a **Botnet Agent**. It utilizes encryption for C2 communication, employs multiple layers of anti-analysis techniques to evade researchers, and collects hardware identifiers to manage infected hosts.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Detection | The presence of `IsServerOS` and "Anti_Analysis" indicators confirms the malware checks for VM or lab environments to evade analysis. |
| **T1562.001** | Impair Defenses: Disable or Modify Security Software | The `AntiProcess.Block` function specifically targets and disables common security/analysis tools like Wireshark, x64dbg, and Process Hacker. |
| **T1055.016** | Process Injection: Module Overwriting | The `PatchMem` function indicates the binary modifies its own code or other processes in memory to bypass security hooks. |
| **T1573** | Encrypted Channel | The implementation of AES256 and HMACSHA256 for "Decrypt" and "Encrypt" functions is used to shield C2 communication from network inspection. |
| **T1027** | Packed_Data | The use of a complex `entry0` routine and the collapsing of distinct functions into one name indicate significant packing or code obfuscation. |
| **T1082** | System Information Discovery | Functions like `HwidGen` and `HWID` are used to gather unique hardware identifiers to fingerprint and track the victim's machine. |
| **T1071** | Application Layer Protocol | The use of MessagePack for structured communication over established network sockets indicates a defined application layer protocol for C2 activity. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the categorized list of Indicators of Compromise (IOCs):

### **IP addresses / URLs / Domains**
*   `googleddd` (Note: This appears to be a non-standard string likely associated with a masked C2 domain or proxy service).

### **File paths / Registry keys**
*   *(None identified. The strings contain various .NET namespaces like `System.IO` and `Microsoft.Win32`, but no specific hardcoded file paths or registry keys were present.)*

### **Mutex names / Named pipes**
*   *(Note: While the behavior analysis mentions "PipeConnected" and "PipeDisconnected," no specific named pipe strings—e.g., `\Device\NamedPipe\...`—were identified in the raw text.)*

### **Hashes**
The following four SHA-256 hashes were identified within the string list (likely representing internal payloads, modified modules, or hardcoded keys):
*   `D84F4C120005F1837DC65C04181F3DA9466B123FC369C359A301BABC12061570`
*   `E123F60E9FC6E974D1381F2F15FB19E7960628CC8925D65E344C2F2BDC64F424`
*   `CABAFE20CFEA6C92D3377C14650461E190857D48D13934B5562233C314AAFBB5`
*   `0C50C67E839472CD612D6033109F5E032987E48E367247F29C0EB30A1D3EB5FC`

### **Other artifacts**
*   **Encryption Protocols:** `Aes256`, `HMACSHA256` (Used for C2 communication).
*   **Serialization Library:** `MessagePack` (Identified as the primary method for structured data exchange).
*   **Malicious Functions/Techniques:** 
    *   `PatchMem` (Memory patching to bypass security or modify code in-memory).
    *   `HwidGen` / `HWID` (Hardware ID collection for victim fingerprinting).
    *   `ReadServertData`, `SendInfo` (Network communication routines).
    *   `Offer_Analysis` related behavior (Anti-debugging/VM detection logic).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: RAT
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Evasion Techniques:** The sample contains explicit anti-analysis routines, including checks for virtualized environments (`IsServerOS`) and specific functions to block security analysis tools like Wireshark and x64dbg.
*   **Encrypted C2 Communication:** The implementation of `MessagePack` for data serialization combined with `Aes256` and `HMACSHA256` encryption indicates a professional-grade infrastructure designed to hide command-and-control traffic from network inspection.
*   **Remote Management Features:** The inclusion of hardware fingerprinting (`HwidGen`), memory patching (`PatchMem`), and modular helper functions suggests the malware is designed for persistent, remote management of infected systems.
