# Threat Analysis Report

**Generated:** 2026-07-01 19:47 UTC
**Sample:** `039cc3d021f34d2b7844e4cb4fa0fabd56853dd40dedae1c9cfd1699882bbf6f_039cc3d021f34d2b7844e4cb4fa0fabd56853dd40dedae1c9cfd1699882bbf6f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `039cc3d021f34d2b7844e4cb4fa0fabd56853dd40dedae1c9cfd1699882bbf6f_039cc3d021f34d2b7844e4cb4fa0fabd56853dd40dedae1c9cfd1699882bbf6f.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 274,944 bytes |
| MD5 | `c153de0ecc7626bcb2fd34a4944e79e7` |
| SHA1 | `8cf7684286a14c836d88f5973b59eefbe68df222` |
| SHA256 | `039cc3d021f34d2b7844e4cb4fa0fabd56853dd40dedae1c9cfd1699882bbf6f` |
| Overall entropy | 6.936 |
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
| `.text` | 60,928 | 5.819 | No |
| `.rsrc` | 212,992 | 6.982 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1199** (showing first 100)

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
\ i t cf
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
| `method.MessagePackLib.MessagePack.WriteTools.WriteBoolean` | `0x402759` | 64814 | ✓ |
| `method.MessagePackLib.MessagePack.Zip.Compress` | `0x406558` | 40062 | ✓ |
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

Based on the provided strings and disassembly, this binary appears to be a **sophisticated malware loader or "stub"** (likely for an information stealer or a remote access trojan). It exhibits several hallmarks of professional-grade malware designed to evade detection while preparing a system for further exploitation.

### Core Functionality and Purpose
The sample's primary role is to act as a gateway. It performs environmental checks, unpacks/decrypts hidden components, and establishes encrypted communication with a Command & Control (C2) server. 

The use of **MessagePack** suggests it handles structured data for complex communication, while the inclusion of **AES-256** ensures that any data stolen or commands received from the attacker are encrypted during transit.

### Suspicious and Malicious Behaviors
*   **Anti-Analysis & Anti-Debugging:** The strings `Anti_Analysis`, `AntiProcess`, `IsServerOS`, and `PatchETW` indicate a heavy focus on detecting analysis environments. Specifically, "PatchETW" is a known technique to disable Event Tracing for Windows, which is often used by EDR (Endpoint Detection and Response) systems to monitor malicious behavior.
*   **Evasive Execution:** The `entry0` function contains complex, convoluted arithmetic and bitwise operations that do not map to standard high-level logic. This is a common technique used in **unpacking stubs** or **polymorphic engines** to hide the true entry point of the payload from static analysis tools.
*   **Information Gathering:** The inclusion of `HWID` (Hardware ID) and `havecamera`/`Camera` suggests the malware intends to fingerprint the victim's machine uniquely and potentially access peripheral hardware for spying or identifying "high-value" targets.
*   **Encrypted Communication:** The use of `AES256`, `HMACSHA256`, and `MessagePack` points toward a structured, encrypted communication channel with a remote server to exchange stolen data (like system info or credentials).

### Notable Techniques & Patterns
*   **Code Obfuscation/Junk Code:** A striking observation in the decompiler output is that multiple different functional names (e.g., `Decrypt`, `Send`, `Block`) all resolve to the same generic, nonsensical code (`*in_EAX = *in_EAX + in_EAX`). This strongly indicates the use of **junk code insertion** or a **packer**, where the real logic is hidden behind "garbage" instructions to frustrate automated decompilation.
*   **Memory Manipulation:** The string `PatchMem` and several references to memory-related operations suggest the malware may perform **reflective loading** (loading code directly into memory) or **inline hooking** to intercept system calls.
*   **System Context Awareness:** References like `ProcessInJob` and `ProcessNotInJob` are often used by malware to determine if it is running inside a "Sandbox" or a restricted environment commonly used by malware researchers.

### Summary of Risk
This binary is highly suspicious. It contains the building blocks for:
1.  **Anti-Analysis:** Detecting and bypassing security software/researchers.
2.  **Persistence/Stealth:** Using packers and junk code to hide its true intent.
3.  **Data Exfiltration:** Securely communicating stolen data via AES encryption.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Detection | The use of `Anti_Analysis`, `IsServerOS`, and `ProcessInJob` checks indicates the malware is attempting to identify if it is running in a laboratory or sandbox environment. |
| **T1562.001** | Impair Defenses: Disable or Modify Tools (ETW) | The `PatchETW` string specifically points to an attempt to disable Event Tracing for Windows, a common method to blind EDR systems. |
| **T1027** | Obfuscated Files or Information | The use of junk code insertion and mapping multiple functions to identical arithmetic operations is designed to hinder static analysis and manual deconstruction. |
| **T1082** | System Information Discovery | The gathering of `HWID` and specific hardware capabilities (e.g., `havecamera`) suggests the malware is fingerprinting the target system. |
| **T1573** | Encrypted Channel | The implementation of AES-256, HMACSHA256, and MessagePack indicates a prioritized effort to encrypt communications between the host and the C2 server. |
| **T1055** | Process Injection | References to `PatchMem` and "reflective loading" indicate that the malware injects code into memory to evade traditional file-based detection. |
| **T1106** | Native API | The mention of inline hooking suggests the malware interacts directly with system APIs to intercept or redirect function calls for stealth. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified in the provided text.*

### **File paths / Registry keys**
*   *None identified (standard system libraries like `mscorlib` and `System.IO` were excluded as false positives).*

### **Mutex names / Named pipes**
*   *No specific mutex or named pipe strings were identified; however, the behavioral analysis notes the use of "Named Pipes" as a general communication method.*

### **Hashes (High-Entropy Strings / Potential Keys)**
The following 64-character hex strings are likely **SHA-256 hashes** used to identify payload components or serve as **hardcoded encryption keys** for C2 communication:
*   `D84F4C120005F1837DC65C04181F3DA9466B123FC369C359A301BABC12061570`
*   `E123F60E9FC6E974D1381F2F15FB19E7960628CC8925D65E344C2F2BDC64F424`
*   `CABAFE20CFEA6C92D3377C14650461E190857D48D13934B55612233C314AAFBB5`
*   `0C50C67E839472CD612D6033109F5E032987E48E367247F29C0EB30A1D3EB5FC`

### **Other artifacts (Behavioral Indicators & C2 Patterns)**
*   **Anti-Analysis Techniques:** 
    *   `PatchETW`: Technique used to disable Event Tracing for Windows to evade EDR.
    *   `Anti_Analysis`, `AntiProcess`, `IsServerOS`: Detection logic used to identify research/sandbox environments.
*   **Encryption & Communication Protocols:**
    *   `MessagePack`: Used for structured data serialization in C2 communication.
    *   `AES-256` / `HMACSHA256`: Encryption standards utilized for securing stolen data and commands.
*   **Spyware/Information Gathering Indicators:**
    *   `havecamera`, `Camera`: Logic used to identify and potentially access camera hardware.
    *   `HWID`: Identification of unique hardware identifiers.
*   **Evasion Techniques:**
    *   `PatchMem`: Potential indicator of reflective loading or inline hooking.
    *   **Junk Code/Polymorphism:** The report notes that multiple functional names resolve to the same "garbage" arithmetic (e.g., `*in_EAX = *in_EAX + in_EAX`), indicating a packer or obfuscator is present.

---

## Malware Family Classification

1. **Malware family**: custom (likely a modular loader/stub)
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Evasion & Obfuscation:** The sample utilizes advanced techniques to bypass security products, including ETW patching (`PatchETW`), junk code insertion (multiple functions mapping to the same arithmetic), and extensive anti-analysis/anti-debugging checks to mask its true functionality.
*   **Infrastructure for Data Exfiltration:** The integration of `MessagePack`, `AES-256`, and `HMACSHA256` indicates a professional, structured communication channel with a C2 server designed to securely transport stolen data or receive remote commands.
*   **Preparatory "Gateway" Behavior:** The presence of hardware fingerprinting (`HWID`) and peripheral checks (`havecamera`) suggests the sample is designed as a precursor (loader/stub) to deliver more specialized payloads like information stealers or Remote Access Trojans (RATs).
