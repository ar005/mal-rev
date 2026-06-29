# Threat Analysis Report

**Generated:** 2026-06-28 11:33 UTC
**Sample:** `02b93705ddbc4c6c5b293cd48623ef3289bcc5815706a6d693665176918dfe1b_02b93705ddbc4c6c5b293cd48623ef3289bcc5815706a6d693665176918dfe1b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `02b93705ddbc4c6c5b293cd48623ef3289bcc5815706a6d693665176918dfe1b_02b93705ddbc4c6c5b293cd48623ef3289bcc5815706a6d693665176918dfe1b.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 476,672 bytes |
| MD5 | `348bd812c6ddb53774cc41259d39dbcd` |
| SHA1 | `8cb2a9b5ee5ee3e09e4e9058bb1de1b1a2dbc5b7` |
| SHA256 | `02b93705ddbc4c6c5b293cd48623ef3289bcc5815706a6d693665176918dfe1b` |
| Overall entropy | 2.646 |
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
| `.text` | 60,416 | 5.822 | No |
| `.rsrc` | 415,232 | 1.823 | No |
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
| `method.MessagePackLib.MessagePack.WriteTools.WriteBoolean` | `0x402759` | 64488 | ✓ |
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x406558` | 39546 | ✓ |
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

Based on the provided strings and disassembly, this binary appears to be a **highly obfuscated game cheat or a sophisticated piece of malware (such as a loader/trojan)**. The naming conventions and features suggest it is designed to communicate with a remote server while evading security software and identifying specific hardware signatures.

### Core Functionality
*   **Remote Communication & Serialization:** The extensive use of `MessagePackLib` indicates the application serializes data into a compact format for transmission. The presence of `ClientSocket`, `SendSync`, and `ReadServertData` confirms it establishes network connections to exchange information with a remote server.
*   **Encryption:** The inclusion of `Aes256` and `HMACSHA256` indicates that the communication between the client and the server is encrypted, likely to hide its activities from network defenders.
*   **Hardware Identification (HWID):** The `HwidGen` and `HWID` strings suggest a mechanism to uniquely identify a user's machine. This is common in both "licensed" game cheats and malware that wants to track specific infected machines.

### Suspicious and Malicious Behaviors
*   **Anti-Analysis & Anti-Debugging:** 
    *   The code contains explicit references to `AntiProcess`, `Anti_Analysis`, and `IsServerOS`. These are used to detect if the program is being run in a virtual machine, a debugger, or a controlled environment.
    *   `PatchMem` suggests the application modifies memory (potentially its own or another process's) to bypass security hooks or patches game code.
*   **Evasion Techniques:** 
    *   The `entry0` function is heavily obfuscated with "junk code" (complex arithmetic, overlapping instructions, and unusual stack manipulations). This is designed to break decompilers and confuse manual analysis.
    *   **Hidden Functionality:** The decompiler failed to provide clean logic for many functions (showing only `WriteBoolean`), which often happens when the code uses indirect jumps or sophisticated "opaque predicates" to hide the real execution flow.
*   **System/Hardware Probing:** 
    *   The use of `Camera` and `havecamera` are non-standard in typical applications but common in game cheats (to check for peripheral support) or malware trying to assess a target's hardware capabilities.

### Notable Techniques & Patterns
*   **"Cheat Engine" Architecture:** The naming convention (`method.Client.Helper...`) is very common in the "cheat" industry, where developers create modular frameworks for interacting with online games.
*   **Dynamic Loading/Execution:** The mention of `DInvokeCore` and `GetExportAddress` suggests the program dynamically resolves function addresses to hide its imports from the Windows Import Address Table (IAT).
*   **Advanced Obfuscation:** The repeated use of complex math in `entry0` to perform simple operations is a classic "packer" or "protector" technique to hinder static analysis.

### Summary of Indicators
| Category | Findings |
| :--- | :--- |
| **Network** | AES-256 Encryption, MessagePack Serialization, Socket Communication |
| **Evasion** | Anti-Process, Anti-Analysis, IsServerOS checks, Junk code in entry point |
| **Manipulation** | PatchMem (Memory patching), DInvokeCore (Dynamic calls) |
| **Identity** | HWID Generation (Hardware fingerprinting) |

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the corresponding MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1573** | Encrypted Channel | The use of `Aes256` and `HMACSHA256` indicates the application encrypts its communication to hide content from network defenders. |
| **T1071** | Application Layer Protocol | The presence of `MessagePackLib`, `ClientSocket`, and `SendSync` indicates the use of specific protocols to transmit data to a remote server. |
| **T1497** | Virtualization/Sandbox Detection | The inclusion of `Anti_Analysis`, `AntiProcess`, and `IsServerOS` suggests attempts to detect if the sample is running in a controlled environment. |
| **T1027** | Obfuscated Files or Information | The use of "junk code," complex arithmetic, and opaque predicates in the entry point is designed to hinder static analysis and decompilation. |
| **T1106** | Native API | The use of `DInvokeCore` and `GetExportAddress` indicates dynamic resolution of function addresses to hide the program's dependencies from the Import Address Table (IAT). |
| **T1082** | System Information Discovery | The gathering of hardware signatures (`HwidGen`, `HWID`) and probing for hardware features like cameras are used to fingerprint or profile the target system. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

### **File paths / Registry keys**
*   *(None identified in the provided text)*

### **Mutex names / Named pipes**
*   *(None explicitly listed, though "PipeConnected" and "PipeDisconnected" appear as status checks in strings.)*

### **Hashes**
The following high-entropy hex strings were identified within the code. These likely represent file hashes (SHA-256), internal encryption keys, or hardcoded identifiers:
*   `D84F4C120005F1837DC65C04181F3DA9466B123FC369C359A301BABC12061570`
*   `E123F60E9FC6E974D1381F2F15FB19E7960628CC8925D65E344C2F2BDC64F424`
*   `CABAFE20CFEA6C92D3377C14650461E190857D48D13934B5562233C314AAFBB5`
*   `0C50C67E839472CD612D6109F5E032987E48E367247F29C0EB30A1D3EB5FC`

### **Other artifacts**
*   **Encryption/Integrity:** `Aes256`, `HMACSHA256` (Indicates encrypted C2 communication).
*   **Data Serialization:** `MessagePackLib` (Used for compact, structured data transmission to a remote server).
*   **Evasion Techniques:** 
    *   `PatchMem` (Memory patching to bypass security hooks).
    *   `DInvokeCore` / `GetExportAddress` (Dynamic function resolution to hide API imports).
    *   `Anti_Analysis`, `AntiProcess`, `IsServerOS` (Checks designed to detect debuggers, sandboxes, or virtual environments).
*   **Identification Patterns:** `HwidGen`, `HWID` (Hardware ID generation used for tracking unique machines or license enforcement).

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family:** custom 
2. **Malware type:** loader
3. **Confidence:** Medium
4. **Key evidence:**
    * **Advanced Evasion & Obfuscation:** The presence of "junk code," sophisticated anti-analysis checks (Anti_Analysis, AntiProcess, IsServerOS), and dynamic API resolution (`DInvokeCore`) are hallmarks of a professional loader designed to evade automated and manual analysis.
    * **Encrypted C2 Communication:** The use of `Aes256`, `HMACSHA256`, and `MessagePackLib` indicates a structured, encrypted communication channel with a remote server, typical of botnets or loaders used to deliver secondary payloads.
    * **Hybrid Characteristics:** While the "Cheat Engine" architecture suggests it may originate from the gaming cheat scene, these same features (HWID fingerprinting, memory patching, and high-level obfuscation) are frequently co-opted by malware authors to create persistent backdoors or modular loaders.
