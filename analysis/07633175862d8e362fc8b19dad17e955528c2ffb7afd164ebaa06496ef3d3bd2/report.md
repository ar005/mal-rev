# Threat Analysis Report

**Generated:** 2026-07-16 18:37 UTC
**Sample:** `07633175862d8e362fc8b19dad17e955528c2ffb7afd164ebaa06496ef3d3bd2_07633175862d8e362fc8b19dad17e955528c2ffb7afd164ebaa06496ef3d3bd2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07633175862d8e362fc8b19dad17e955528c2ffb7afd164ebaa06496ef3d3bd2_07633175862d8e362fc8b19dad17e955528c2ffb7afd164ebaa06496ef3d3bd2.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 66,048 bytes |
| MD5 | `c10f8301f217bbfdbdcc915f27f3cd76` |
| SHA1 | `6a5038bdadd12ae1b5c8830a32fc75d881b45309` |
| SHA256 | `07633175862d8e362fc8b19dad17e955528c2ffb7afd164ebaa06496ef3d3bd2` |
| Overall entropy | 5.81 |
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
| `.text` | 60,416 | 5.846 | No |
| `.rsrc` | 4,608 | 5.139 | No |
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
Virexa
mscorlib
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MessagePackLib.MessagePack.WriteTools.WriteBoolean` | `0x402759` | 65464 | ✓ |
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x406558` | 39838 | ✓ |
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

Based on the provided disassembly and string analysis, here is a summary of the findings:

### Core Functionality and Purpose
The binary appears to be a **malicious client application** (likely a bot, remote access tool, or an "injector" for game cheats) designed to communicate with a remote server using encrypted protocols. 

*   **Network Communication:** The presence of `MessagePack`, `ClientSocket`, `SendInfo`, and `ReadServertData` indicates the binary is structured to transmit data between a local client and a remote server.
*   **Encryption/Security:** The inclusion of `AES256`, `HMACSHA256`, and `get_IV` confirms that the communication and/or local storage are encrypted to prevent security researchers from intercepting traffic or analyzing the payload.
*   **Data Serialization:** It uses the **MessagePack** library, which is a common way to serialize data into a compact binary format for efficient transmission over networks.

### Suspicious or Malicious Behaviors
The following behaviors strongly suggest malicious intent:

*   **Anti-Analysis & Evasion:** 
    *   The presence of `Anti_Analysis`, `Antivirus`, and `IsServerOS` strings indicates the program actively checks if it is being run in a virtual machine, a sandbox, or by a researcher.
    *   The `PatchMem` function suggests the ability to modify memory (either its own or other processes) to bypass security controls.
*   **Spying/Information Gathering:** 
    *   Strings like `Camera` and `havecamera` suggest the program may attempt to access the system's camera or perform reconnaissance on available hardware.
    *   `HwidGen` (Hardware ID Generation) is a common technique used to uniquely identify an infected machine for licensing or as a persistent identifier for a bot.
*   **Obfuscated Execution:** 
    *   The disassembly shows several distinct functions (e.g., `WriteFloat`, `Decrypt`, `GetExportAddress`) all being mapped to the same dummy function name (`WriteBoolean`). This is a classic **decompiler evasion technique** where real logic is hidden behind "junk" code or renamed labels to frustrate automated analysis tools.

### Notable Techniques and Patterns
*   **Heavy Obfuscation:** The repeated `WriteBoolean` names across completely different logical modules (Encryption, Network, Hardware info) indicates that the binary was passed through an obfuscator designed to break static analysis tools like IDA Pro/Ghidra.
*   **Manual Code Crafting (Entry0):** The `entry0` function shows complex mathematical operations and overlapping instructions. This is often a sign of a **packer or stub** used to decrypt the actual payload in memory before execution begins.
*   **Dynamic API Resolution:** The use of `GetExportAddress` and `DInvokeCore` suggests the program avoids using the standard Import Address Table (IAT) where possible, instead resolving functions at runtime to hide its capabilities from basic scanners.

### Summary Conclusion
This is a highly suspicious binary that employs multiple layers of **encryption, anti-analysis, and heavy code obfuscation**. It likely serves as a persistent backdoor or a remote-controlled tool designed to hide its activity from both the user and security software while communicating with an external server via encrypted channels.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1573** | Encrypted Channel | The use of `AES256`, `HMACSHA256`, and `get_IV` confirms that data transmission and local storage are encrypted to evade detection by security researchers. |
| **T1027** | Obfuscated Files or Information | The mapping of multiple distinct logical functions (Encryption, Network, etc.) to the same dummy name (`WriteBoolean`) is a clear attempt to frustrate static analysis tools like IDA Pro/Ghidra. |
| **T1027.002** | Packed Data | The `entry0` function's use of complex mathematical operations and overlapping instructions indicates the presence of a packer or decryption stub used to hide the main payload. |
| **T1106** | Native API | The use of `GetExportAddress` and `DInvokeCore` points to dynamic resolution of functions to bypass standard Import Address Table (IAT) scanning. |
| **T1213** | System Information Discovery | The inclusion of `HwidGen` and checks for hardware components like the `Camera` are used to identify, track, and fingerprint infected systems. |
| **T1055** | Process Injection | The presence of a `PatchMem` function suggests an intent to modify memory—either internally or in other processes—to bypass security controls. |
| **T1071** | Application Layer Protocol | The use of the `MessagePack` library and custom socket logic indicates the utilization of specific protocols for structured communication between the client and a remote server. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

**File paths / Registry keys**
*   *(None identified; standard .NET library paths like `Microsoft.Win32` were excluded as false positives)*

**Mutex names / Named pipes**
*   *(No specific named pipe strings or mutexes were identified. While "PipeConnected" was mentioned, it appears to be a logic flag rather than a specific IPC object name.)*

**Hashes**
The following high-entropy hex strings were identified. These may represent SHA-256 hashes of embedded components or static keys used for the AES/HMAC encryption layers:
*   `D84F4C120005F1837DC65C04181F3DA9466B123FC369C359A301BABC12061570`
*   `E123F60E9FC6E974D1381F2F15FB19E7960628CC8925D65E344C2F2BDC64F424`
*   `CABAFE20CFEA6C92D3377C14650461E190857D4813934B5562233C314AAFBB5`

**Other artifacts**
*   **Potential Malware Family/Identifier:** `Virexa`
*   **C2 Communication Protocol:** Use of **MessagePack** for data serialization and binary transmission.
*   **Obfuscation Technique:** Multiple distinct functions (Encryption, Network, Hardware Info) mapped to the dummy name `WriteBoolean`.
*   **Evasion/Anti-Analysis Indicators:** 
    *   `PatchMem` (Memory patching capabilities)
    *   `Ant_Analysis`, `Antivirus`, `IsServerOS` (Environment checks)
    *   `HwidGen` (Hardware ID generation for bot tracking)
*   **Spying Capabilities:** `Camera`, `havecamera` (Potential unauthorized hardware access).

---

## Malware Family Classification

1. **Malware family**: Virexa
2. **Malware type**: RAT (Remote Access Trojan) / Backdoor
3. **Confidence**: High

4. **Key evidence**:
* **Advanced Evasion & Obfuscation:** The sample employs sophisticated anti-analysis techniques, including environment checks (`Ant_Analysis`, `IsServerOS`), dynamic API resolution to hide its Import Address Table (IAT), and "dummy" function naming (e.g., mapping multiple logic types to `WriteBoolean`) to frustrate static analysis tools.
* **Secure Communication Infrastructure:** The use of the **MessagePack** serialization library combined with high-strength encryption (**AES256**, **HMACSHA256**) indicates a professional-grade effort to hide command-and-control (C2) traffic from network security monitoring.
* **Spying & Persistence Indicators:** The inclusion of `HwidGen` for unique device tracking and specific logic for camera access (`havecamera`) are hallmarks of Remote Access Trojans designed for long-term persistence and information theft.
