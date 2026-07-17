# Threat Analysis Report

**Generated:** 2026-07-17 00:54 UTC
**Sample:** `079e99c669428e7b65656f2cb0eefc9a31e22dd720cad20c1d1490fc9c1a9d22_079e99c669428e7b65656f2cb0eefc9a31e22dd720cad20c1d1490fc9c1a9d22.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `079e99c669428e7b65656f2cb0eefc9a31e22dd720cad20c1d1490fc9c1a9d22_079e99c669428e7b65656f2cb0eefc9a31e22dd720cad20c1d1490fc9c1a9d22.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 49,152 bytes |
| MD5 | `ce6730669f0fb5af7238c20d6b73d30c` |
| SHA1 | `fe2851e365025d66aaf886d7a72acf1d9893c8cc` |
| SHA256 | `079e99c669428e7b65656f2cb0eefc9a31e22dd720cad20c1d1490fc9c1a9d22` |
| Overall entropy | 5.586 |
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
| `.text` | 44,544 | 5.608 | No |
| `.rsrc` | 3,584 | 5.111 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **598** (showing first 100)

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

Based on the provided disassembly and string analysis, this binary appears to be a sophisticated piece of software—likely a **game cheat or a high-end malware sample** (such as a "loader" for remote access)—designed with heavy emphasis on anti-analysis and evasion.

### Core Functionality and Purpose
The code's primary purpose is to establish a secure, encrypted communication channel between the local machine and a remote server while actively bypassing security software. 

*   **Encrypted Communication:** The use of `Aes256`, `SHA256Managed`, `SslClient`, and `MessagePack` indicates that all data exchanged with the server is encrypted and serialized into a compact format (MessagePack).
*   **Environment Identification:** Features like `HwidGen` (Hardware ID Generation) suggest the software identifies unique characteristics of the machine, common in cheat systems to manage "bans" or in malware to track unique infections.
*   **Information Gathering:** The use of `GetActiveWindowTitle`, `GetSystemInfo`, and `GetActiveProcess` suggests the program is interested in what else is running on the system (likely looking for specific games or analysis tools).

### Suspicious/Malicious Behaviors
The sample exhibits several behaviors typical of malware or advanced cheat "loaders":

*   **Antimalware Evasion:** The presence of `Amsi.PatchA` is a high-severity indicator. Patching the **AMSI (Antimalware Scan Interface)** is a specific technique used to disable Windows Defender and other antivirus products' ability to scan script content in memory.
*   **Anti-Analysis/Obfuscation:** The `entry0` function shows clear evidence of "junk code" or anti-disassembly techniques. 
    *   The warnings regarding **overlapping instructions** (e.g., `instruction at ... overlaps instruction at ...`) and **bad instruction data** are intentional tactics used to break the linear sweep and recursive descent disassembly processes of tools like IDA Pro and Ghidra.
*   **Security Feature Disabling:** The presence of `AntiProcess` and `Antivirus` strings suggests logic specifically designed to detect, close, or bypass security software.
*   **Network Activity:** The inclusion of `TcpClient`, `SslClient`, and `ReadServertData` indicates the program functions as a "client" that communicates with a remote Command & Control (C2) server.

### Notable Techniques & Patterns
*   **Code Obfuscation:** The failure of the decompiler to produce meaningful C code for almost all functions (reverting them to `WriteBoolean`) is a primary indicator of heavy obfuscation or "garbage" instructions injected between real instructions.
*   **Packing/Protection:** The mangled disassembly in `entry0` suggests the binary may be packed or contains an "unpacker" stub designed to frustrate manual reverse engineering.
*   **Standard Tooling for Persistence:** The use of `System.IO`, `Microsoft.Win32`, and `RegistryValueKind` indicates the ability to interact with the file system and Windows Registry, potentially for establishing persistence or modifying system configurations.

### Summary Conclusion
This binary is **highly suspicious**. It contains specific indicators used in modern "cheat" software (HWID generation, AMSI patching, anti-debug logic). The complexity of the obfuscation suggests it was designed to remain hidden from both automated security scanners and manual human analysis.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1562.001** | Disable or Notify Running Antivirus | The use of `Amsi.PatchA` specifically targets and disables the Antimalware Scan Interface to bypass Windows Defender's memory scanning. |
| **T1027** | Obfuscated Files or Information | The presence of "junk code," overlapping instructions, and bad instruction data are used to hinder manual analysis and break disassembly tools. |
| **T1027.001** | Packing | The mangled disassembly in the entry point suggests the binary is packed or uses an unpacker stub to hide its true functionality from static analysis. |
| **T1573** | Encrypted Traffic | The implementation of `Aes256`, `SslClient`, and `MessagePack` ensures that communication with the remote server is encrypted to evade detection. |
| **T1082** | System Information Discovery | The use of `GetSystemInfo` and `GetActiveProcess` allows the malware to identify the environment and look for specific target applications or security tools. |
| **T1112** | Modify Registry | Interaction with `Microsoft.Win32` and `RegistryValueKind` suggests the ability to modify system configurations or establish persistence via the Windows Registry. |
| **T1071.001** | Application Layer Protocol | The use of `TcpClient` and `SslClient` indicates the establishment of a communication channel over standard network protocols for C2 interaction. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

**File paths / Registry keys**
*   *(None identified; while .NET libraries like `Microsoft.Win32` and `System.IO` are mentioned, no specific malicious paths or registry keys were listed.)*

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   **SHA-256:** `87639126EA77B358F26532367DBA67C5310EF50A8D9888ED070CD40E1F605A8F`

**Other artifacts (user agents, C2 patterns, etc.)**
*   **Antimalware Evasion Technique:** `Amsi.PatchA` (Specific indicator of an attempt to patch and disable the Antimalware Scan Interface).
*   **Encryption/Communication Protocols:** 
    *   `Aes256` / `aes256` (Symmetric encryption)
    *   `SHA256Managed` (Hashing)
    *   `MessagePack` (Data serialization format for C2 communication)
*   **Network Components:** `SslClient`, `TcpClient`, `ReadServertData` (Indicates a client-server architecture).
*   **Evasion/Obfuscation Tactics:** 
    *   "Junk code" / "Overlapping instructions" in `entry0`.
    *   **HWID Generation:** (`HwidGen`) used for identifying unique hardware signatures.
*   **Information Gathering:** `GetActiveWindowTitle`, `GetSystemInfo`, `GetActiveProcess` (Used to identify the environment or target applications).

---

## Malware Family Classification

1. **Malware family**: Custom (Loader)
2. **Malware type**: Loader / Trojan
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Evasion Tactics:** The use of `Amsi.PatchA` is a high-confidence indicator of malicious intent, specifically designed to disable the Antimalware Scan Interface (AMSI) to bypass Windows Defender and other security products. Furthermore, "junk code" and overlapping instructions are intentional techniques to hinder manual analysis in tools like IDA Pro.
*   **Robust C2 Infrastructure:** The implementation of `Aes256`, `SslClient`, and `MessagePack` suggests a highly developed communication layer designed to encrypt and serialize data for secure transmission to a command-and-control (C2) server.
*   **Environment Profiling & Fingerprinting:** The inclusion of `HwidGen` (Hardware ID Generation) and system information gathering (`GetSystemInfo`, `GetActiveProcess`) is characteristic of both high-end game cheats and sophisticated malware used to track unique infections and manage "bans" or access levels.
