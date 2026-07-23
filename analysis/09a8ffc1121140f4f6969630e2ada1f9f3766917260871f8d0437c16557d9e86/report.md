# Threat Analysis Report

**Generated:** 2026-07-22 16:54 UTC
**Sample:** `09a8ffc1121140f4f6969630e2ada1f9f3766917260871f8d0437c16557d9e86_09a8ffc1121140f4f6969630e2ada1f9f3766917260871f8d0437c16557d9e86.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `09a8ffc1121140f4f6969630e2ada1f9f3766917260871f8d0437c16557d9e86_09a8ffc1121140f4f6969630e2ada1f9f3766917260871f8d0437c16557d9e86.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 138,752 bytes |
| MD5 | `a58990bf71a1eb82a13d3b2df860f944` |
| SHA1 | `ae06f05a21152f01fd10de266b168e2f83b5f91f` |
| SHA256 | `09a8ffc1121140f4f6969630e2ada1f9f3766917260871f8d0437c16557d9e86` |
| Overall entropy | 7.032 |
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
| `.rsrc` | 77,312 | 7.594 | ⚠️ Yes |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1142** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
pjX	(
pjX	(
v4.0.30319
#Strings
 p8+	d
-6Fk
R _ j cf
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
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x406558` | 39826 | ✓ |
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

### Overview
The provided binary is a **highly obfuscated .NET-based client application**. Based on the strings and decompiled code, it appears to be a "trainer," "cheat," or similar utility that communicates with a remote server using encrypted protocols. The code contains numerous indicators of professional-grade obfuscation intended to hinder reverse engineering.

### Core Functionality
*   **Secure Communication:** The application utilizes **AES-256**, **SHA-256**, and **HMAC-SHA256** for encrypting data sent between the client and a remote server. It uses the `MessagePack` format (a binary serialization library) to package data, which is common in game development and high-performance networking.
*   **Data Processing:** The presence of methods like `ReadServertData`, `WriteTools`, and `UpdateSettings` suggests it processes configuration files or server-side commands to modify its own behavior or the environment it runs in.
*   **Hardware Identification:** The inclusion of `HWID` (Hardware ID) and `havecamera` suggests the application identifies specific hardware components to generate a unique fingerprint for the user, likely to manage "licenses" or prevent multiple accounts on one machine.

### Suspicious & Malicious Behaviors
The binary exhibits several hallmarks of malware or sophisticated gray-ware:

*   **Anti-Analysis / Anti-Debugging:** 
    *   **PatchETW:** The presence of `PatchETW` suggests it attempts to disable **Event Tracing for Windows**, a technique used to hide activities from EDR (Endpoint Detection and Response) systems.
    *   **Antivirus/Anti_Analysis Checks:** Explicitly named methods like `method.Client.Helper.Methods.Antivirus` and `method.Client.Helper.Anti_Analysis.IsServerOS` indicate the program actively checks if it is being analyzed or run in a virtualized environment (VM).
    *   **Process Scanning:** The use of `PROCESSENTRY32` suggests the application scans running processes, likely searching for debuggers, antivirus software, or cheat-detection tools.
*   **Aggressive Obfuscation/Packing:** 
    *   The disassembly shows a massive amount of repetitive, non-functional code in **entry0**. This is a common "junk code" technique used to overwhelm automated decompiler engines and slow down human analysts.
    *   Many distinct functions have been renamed to an identical placeholder (`WriteBoolean`). This is a signature of a packer or obfuscator (like VMProtect, Themida, or a custom .NET protector) that replaces the original metadata with generic names to hide the true logic flow.
*   **Memory Manipulation:** The `PatchMem` function suggests the binary modifies its own memory space or the memory of other processes to hook functions or change values dynamically.

### Notable Techniques & Patterns
*   **MessagePack Integration:** Using `MessagePackLib` is a specific choice to move away from standard JSON/XML, making network traffic harder to read without the correct schemas and keys.
*   **Polymorphism Indicators:** The repetitive nature of the "WriteBoolean" functions suggests that while the disassembly looks identical for many functions, they originally served different roles in the codebase before being mangled by an obfuscator.
*   **Information Gathering:** The collection of system information (Hardware IDs) is a common tactic used both by legitimate DRM (Digital Rights Management) and by malware to track "infected" machines or identify unique users.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the relevant MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of junk code, renamed functions (e.g., `WriteBoolean`), and the MessagePack format are used to hinder reverse engineering and hide program logic. |
| **T1497** | Virtualized Environment | The presence of "Antivirus" and "IsServerOS" checks indicates an intent to detect and avoid analysis in virtual machines or sandboxes. |
| **T1055** | Process Injection | The `PatchMem` function suggests the ability to modify memory space, likely for hooking functions or altering data in other processes. |
| **T1036** | Masquerading | The application mimics a legitimate "trainer" or "cheat" utility to blend in with common gray-ware while performing malicious operations. |
| **T1542** | Exfiltration Over C2 Channel | (Implied) The use of AES-256, SHA-256, and HMAC-SHA256 indicates a structured system for secure communication with a remote command-and-control server. |

***

**Analyst Note:** 
While the analysis describes "PatchETW," this is specifically an evasion technique to blind EDR (Endpoint Detection and Response) systems by tampering with Windows Event Tracing. While there isn't a specific sub-technique for ETW alone, it falls under the broader **Defense Evasion** tactic, similar to the behavior mapped to T1497.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*None identified.*

### **File paths / Registry keys**
*None identified.* (Note: `System.IO` is a standard .NET namespace and not a specific file path.)

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
The following 64-character hex strings were identified in the source. These likely represent hardcoded encryption keys, unique identifiers for the client's communication protocol, or hash values used for data integrity:
*   `D84F4C120005F1837DC65C04181F3DA9466B123FC369C359A301BABC12061570`
*   `E123F60E9FC6E974D1381F2F15FB19E7960628CC8925D65E344C2F2BDC64F424`
*   `CABAFE20CFEA6C92D3377C14650461E190857D48D13934B5562233C314AAFBB5`
*   `0C50C67E839472CD612D6033109F5E032987E48E367247F29C0EB30A1D3EB5FC`

### **Other artifacts**
*   **C2/Communication Patterns:** 
    *   Use of `MessagePackLib`: Indicates a non-standard, binary serialization format for network communication to evade simple string-based traffic analysis.
    *   Encryption Suite: Use of `AES-256`, `SHA-256`, and `HMAC-SHA256` for payload encryption.
*   **Evasion Techniques:**
    *   `PatchETW`: Specifically identified as a technique to disable Event Tracing for Windows to evade EDR (Endpoint Detection and Response) systems.
    *   Anti-Analysis Checks: Functions including `Antivirus`, `IsServerOS`, and `Anti_Analysis` are used to detect virtualized environments or security software.
*   **Persistence/Tracking:** 
    *   `HWID`: Collection of Hardware IDs for device fingerprinting (common in "trainer" malware and gray-ware to prevent multi-account usage).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / trojan
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Evasion & Anti-Analysis:** The binary employs high-level evasion techniques, specifically `PatchETW` to blind Endpoint Detection and Response (EDR) systems, alongside explicit checks for antivirus software, virtualized environments (`IsServerOS`), and process scanning to detect debuggers.
*   **Advanced Obfuscation & Communication:** The use of a "junk code" injection strategy, mass renaming of functions to generic names (e.g., `WriteBoolean`), and the implementation of a complex communication stack (AES-256, HMAC-SHA256, and MessagePack) indicates an effort to hide command-and-control (C2) logic and bypass network security filters.
*   **Intentional Masquerading:** The "trainer/cheat" profile is a common vector for gray-ware; however, the inclusion of hardware fingerprinting (`HWID`) and memory manipulation (`PatchMem`) suggests the application is designed to establish a persistent, unique identity for each infected machine while evading detection.
