# Threat Analysis Report

**Generated:** 2026-06-26 15:25 UTC
**Sample:** `01139818cc4f023f50dfa34b471e6440f097d05a767d72e7f5cf129cc1b7f3b1_01139818cc4f023f50dfa34b471e6440f097d05a767d72e7f5cf129cc1b7f3b1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01139818cc4f023f50dfa34b471e6440f097d05a767d72e7f5cf129cc1b7f3b1_01139818cc4f023f50dfa34b471e6440f097d05a767d72e7f5cf129cc1b7f3b1.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 66,048 bytes |
| MD5 | `f51d0f8922881aa603d5503ca8b56ebb` |
| SHA1 | `70710b60a027f78f4f36bf6a839c71cef08c97a9` |
| SHA256 | `01139818cc4f023f50dfa34b471e6440f097d05a767d72e7f5cf129cc1b7f3b1` |
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
| `.text` | 60,416 | 5.854 | No |
| `.rsrc` | 4,608 | 4.919 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **968** (showing first 100)

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
DifferenceAtDc
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MessagePackLib.MessagePack.WriteTools.WriteBoolean` | `0x402759` | 65464 | ✓ |
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x406558` | 39966 | ✓ |
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

Based on the provided disassembly and string metadata, here is an analysis of the binary's functionality and behavior.

### Core Functionality
The binary appears to be a **network-oriented client** (potentially for a game or a specialized application) that utilizes the **MessagePack** serialization library for data exchange. However, it contains significant indicators of malicious intent or high-level protection mechanisms typically found in "cheat" software or sophisticated malware.

### Suspicious and Malicious Behaviors
*   **Anti-Analysis & Anti-Debugging:** 
    *   The strings `Anti_Analysis`, `IsServerOS`, and `AntiProcess` strongly suggest the program checks if it is being run in a virtual machine (VM), inside a sandbox, or by an analyst. It likely shuts down or changes its behavior if these conditions are met.
    *   The `Block` function under the `AntiProcess` path suggests it may actively prevent debuggers or analysis tools from attaching to it.
*   **Memory Manipulation:** 
    *   The presence of `PatchMem` indicates the binary likely modifies its own code in memory (self-patching) or patches other processes. This is a common technique for bypassing security checks or hiding activities.
*   **Encryption and Secure Communication:** 
    *   The use of `Aes256`, `HMACSHA256`, and functions like `Decrypt` and `Encrypt` indicate that the binary communicates with a remote server using strong encryption, likely to mask Command & Control (C2) traffic or exfiltrated data.
*   **Hardware Identification:** 
    *   The `HWID` string suggests the program generates or checks a unique hardware identifier, often used by malware for "campaign tracking" or by cheats to prevent multiple users from using one account.

### Notable Techniques and Patterns
*   **Heavy Obfuscation:**
    *   The decompiler produced dozens of different functions with the exact same name (`WriteBoolean`). This is a hallmark of **function flattening** or code obfuscation, designed to confuse automated analysis tools and humans by hiding the actual logic behind generic symbols.
    *   The `entry0` function contains "junk" control flow (e.g., `WARNING: Control flow encountered bad instruction data`), complex arithmetic with carry flags, and bitwise operations that perform simple actions in an intentionally convoluted way to hinder static analysis.
*   **Symbol Overloading/Packing:** 
    *   The presence of a wide variety of strings ranging from standard libraries (MessagePack) to high-level security checks suggests the binary might be "packed" or uses a commercial protector to hide its true capabilities.
*   **Data Serialization:** 
    *   The integration of `MessagePack` suggests that while the underlying logic is obscured, the data it sends/receives is structured and likely contains complex objects (e.g., user profiles, telemetry, or game state).

### Summary Verdict
The binary exhibits characteristics consistent with **sophisticated malware** or a **highly protected "cheat" tool**. It uses heavy obfuscation to hide its true logic, employs active anti-analysis checks to evade researchers, and uses standard high-strength encryption for network communication.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Detection | The inclusion of `Anti_Analysis`, `IsServerOS`, and `AntiProcess` indicates checks intended to identify if the code is running in a researcher's sandbox or virtual machine. |
| **T1573** | Encrypted Channel for Command and Control | The use of `Aes256` and `HMACSHA256` confirms that the binary encrypts its network traffic to hide communication with remote infrastructure. |
| **T1027** | Obfuscated Executables | The presence of "junk" control flow, function flattening (multiple `WriteBoolean` instances), and complex arithmetic is designed to hinder static analysis and automated tools. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs). 

Note: Standard .NET libraries (e.g., `System.IO`, `mscorlib`), common Windows environmental flags (e.g., `ES_SYSTEM_REQUIRED`), and internal method names have been excluded as they do not constitute specific indicators for a unique threat actor or campaign.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified.

### **Mutex names / Named pipes**
*   None identified (Note: while `PipeConnected` appears in strings, it is a generic state indicator and not a specific named pipe path).

### **Hashes**
*(The following are unique hex strings found in the data; they may represent cryptographic keys or custom internal identifiers.)*
*   `D84F4C120005F1837DC65C04181F3DA9466B123FC369C359A301BABC12061570`
*   `E123F60E9FC6E974D1381F2F15FB19E7960628CC8925D65E344C2F2BDC64F424`
*   `CABAFE20CFEA6C92D3377C14650461E190857D4813934B5562233C314AAFBB5`

### **Other artifacts**
*   **Encryption/Hashing Algorithms:** `Aes256`, `HMACSHA256` (Indicates secure C2 communication or data exfiltration).
*   **Data Serialization:** `MessagePack` (Used for structured data exchange).
*   **Anti-Analysis Triggers:** 
    *   `Anti_Analysis`
    *   `IsServerOS` (Check to see if running in a server environment/VM)
    *   `AntiProcess` (Attempting to detect or block analysis tools)
*   **Malicious Behavior Indicators:**
    *   `PatchMem`: Indicates memory patching of self or other processes.
    *   `HWID`: Generation or checking of unique hardware IDs for tracking/licensing.
    *   `WriteBoolean` (Multi-instance): Evidence of function flattening/obfuscation.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for this sample:

1.  **Malware family:** custom
2.  **Malware type:** loader / backdoor
3.  **Confidence:** Medium
4.  **Key evidence:**
    *   **Advanced Evasion & Obfuscation:** The use of function flattening (multiple `WriteBoolean` instances), junk control flow, and specific anti-analysis checks (`Anti_Analysis`, `IsServerOS`, `AntiProcess`) indicates a high level of effort to evade automated analysis and manual inspection.
    *   **Secure C2 Communication:** The integration of `Aes256` and `HMACSHA256` for encrypted communication via the `MessagePack` serialization library suggests a sophisticated infrastructure for Command & Control (C2) or data exfiltration.
    *   **Memory Manipulation & Identification:** The presence of `PatchMem` (suggesting self-modification or process tampering) and `HWID` (hardware fingerprinting) are classic indicators of either high-end malware seeking to maintain a persistent, stealthy presence or highly protected "cheat" software.
