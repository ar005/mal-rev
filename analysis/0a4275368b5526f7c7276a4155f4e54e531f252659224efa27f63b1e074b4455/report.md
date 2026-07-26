# Threat Analysis Report

**Generated:** 2026-07-24 19:19 UTC
**Sample:** `0a4275368b5526f7c7276a4155f4e54e531f252659224efa27f63b1e074b4455_0a4275368b5526f7c7276a4155f4e54e531f252659224efa27f63b1e074b4455.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a4275368b5526f7c7276a4155f4e54e531f252659224efa27f63b1e074b4455_0a4275368b5526f7c7276a4155f4e54e531f252659224efa27f63b1e074b4455.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 66,560 bytes |
| MD5 | `39e482557ab2669b2789217288ac511f` |
| SHA1 | `4c108186e40396aa7b3187d931b19206900fb966` |
| SHA256 | `0a4275368b5526f7c7276a4155f4e54e531f252659224efa27f63b1e074b4455` |
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
| `.text` | 60,416 | 5.841 | No |
| `.rsrc` | 5,120 | 5.082 | No |
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
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x406558` | 39666 | ✓ |
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

Based on the provided disassembly and string data, here is an analysis of the binary's functionality and characteristics:

### Core Functionality
The binary appears to be a **sophisticated client-side application**, likely designed with features commonly found in **game cheats** or **malware (such as a Trojan or Information Stealer)**. It uses the **MessagePack** serialization library for data handling, which is often used to package data into a compact format for network communication.

### Suspicious and Malicious Behaviors
The following behaviors are highly indicative of malicious intent or evasion:

*   **Anti-Analysis & Anti-Debugging:**
    *   The presence of `AntiProcess`, `Block`, and `Antivirus` functions suggests the program actively checks for, and potentially blocks, analysis tools (e.g., debuggers, sandboxes, or antivirus software).
    *   `IsServerOS` and `Ensure_NOT_Debugger` style checks are commonly used to detect if the code is running in a virtualized environment or under a researcher's observation.
*   **Evasive Techniques:**
    *   The entry point (`entry0`) shows signs of **heavy obfuscation**. The decompilation contains significant "junk code," complex pointer arithmetic, and overlapping instructions (e.g., `warning: instruction at ... overlaps...`). This is a deliberate technique to hinder automated analysis and manual disassembly by analysts.
    *   Many functions appear with identical names in the decompiler (`WriteBoolean`), suggesting that the original symbol table was stripped or that the code is **packed/encrypted** and unpacked only during execution.
*   **Data Exfiltration & Surveillance:**
    *   The inclusion of `Camera` and `havecamera` suggests the program may check for, or attempt to access, the system's webcam.
    *   The use of `HwidGen` (Hardware ID Generation) is common in "loader" programs to lock a license to a specific machine but can also be used by malware to track unique victims.
*   **Encryption & Communication:**
    *   The code explicitly references **AES256** for both encryption and decryption. This indicates that any data sent over the network or stored on disk is intentionally encrypted, likely to hide its contents from Network Intrusion Detection Systems (NIDS).
    *   `ClientSocket`, `Send`, and `Receive` functions indicate standard but encapsulated networking capabilities.

### Notable Techniques & Patterns
*   **MessagePack Integration:** The use of MessagePack suggests the developer wanted a structured way to handle complex data structures while keeping the payload small for rapid transmission.
*   **Memory Manipulation:** The inclusion of `PatchMem` suggests the binary might perform **process injection** or modify the memory space of other running applications (common in game cheats to inject code into the game process).
*   **Obfuscated Logic:** The "messy" nature of the `WriteFloat` and `entry0` functions indicates a high level of effort to hide the program's logic from static analysis tools.

### Summary for Incident Response
This sample is highly suspicious. It contains classic "loader" characteristics: it attempts to hide its presence (Anti-Analysis), communicates over encrypted channels, and possesses capabilities to query hardware info and interact with system peripherals (Camera). The high level of obfuscation suggests a professional authoring of the binary, typical of modern malware or sophisticated game-related cheats.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtualized Environment | The presence of `Antivirus`, `IsServerOS`, and `Ensure_NOT_Debugger` functions indicates the binary is attempting to detect if it is running in a sandbox or analysis environment. |
| T1027 | Obfuscated Files or Information | The use of junk code, complex pointer arithmetic, and stripped symbols is a deliberate attempt to hinder manual and automated static analysis. |
| T1082 | System Information Discovery | The `HwidGen` functionality suggests the binary gathers unique hardware identifiers to profile the victim's machine. |
| T1132 | Data Encoding | The explicit use of AES256 encryption for data handling is intended to mask communications and bypass network-based detection systems. |
| T1055 | Process Injection | The inclusion of `PatchMem` indicates a capability to modify the memory space of other processes, typically used to inject malicious code or scripts. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   *(None identified - Note: While "System.IO" and "Microsoft.Win32" appear in strings, these are standard .NET framework libraries and do not constitute specific file paths or registry keys.)*

**Mutex names / Named pipes**
*   *(None identified - Note: "PipeConnected" and "PipeDisconnected" are status flags, not specific pipe names.)*

**Hashes**
*   `D84F4C12005F1837DC65C04181F3DA9466B123FC369C359A301BABC12061570`
*   `E123F60E9FC6E974D1381F2F15FB19E7960628CC8925D65E344C2F2BDC64F424`
*   `CABAFE20CFEA6C92D3377C14650461E190857D4813934B5562233C314AAFBB5`
*   `0C50C67E839472CD612D6033109F5E032987E48E367247F29C0EB30A1D3EB5FC`

**Other artifacts**
*   **Encryption Protocol:** `AES256` (Used for securing data in transit/on disk)
*   **Data Serialization:** `MessagePack` (Used for compact network communication)
*   **Potential Capabilities:** 
    *   `HwidGen` (Hardware ID Generation for licensing or tracking)
    *   `PatchMem` (Memory manipulation/injection capability)
    *   `havecamera` / `Camera` (Inquiry/access to system peripherals)
    *   **Evasion Techniques:** Anti-debugging, Anti-analysis, and "junk code" obfuscation.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / trojan
3. **Confidence**: High

4. **Key evidence**:
*   **Robust Evasion & Obfuscation:** The sample employs advanced anti-analysis techniques, including `Antivirus` and `Ensure_NOT_Debugger` checks, alongside "junk code" and complex pointer arithmetic designed to thwart both automated sandboxes and manual reverse engineering.
*   **Malicious Payload Delivery Traits:** The inclusion of `PatchMem` (suggesting process injection), `HwidGen` (for victim tracking or licensing locks), and the use of `MessagePack` with `AES256` encryption indicates a professional-grade infrastructure for delivering and communicating with malicious components.
*   **Surveillance & Persistence Capabilities:** The presence of functions related to camera access (`havecamera`) and hardware identification, combined with a high degree of obfuscation, suggests the binary is intended to provide persistent access or steal information from the victim's machine.
