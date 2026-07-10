# Threat Analysis Report

**Generated:** 2026-07-09 21:20 UTC
**Sample:** `04349e82927bd45cab42e0943dccc81a04c94baea252a1dc678ccdf4ee58b061_04349e82927bd45cab42e0943dccc81a04c94baea252a1dc678ccdf4ee58b061.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04349e82927bd45cab42e0943dccc81a04c94baea252a1dc678ccdf4ee58b061_04349e82927bd45cab42e0943dccc81a04c94baea252a1dc678ccdf4ee58b061.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 30,720 bytes |
| MD5 | `5c7a8e944d88e82c09612fd70d767ceb` |
| SHA1 | `e9d8091fa12d10eafc4cc6ae171c34467023e2d4` |
| SHA256 | `04349e82927bd45cab42e0943dccc81a04c94baea252a1dc678ccdf4ee58b061` |
| Overall entropy | 5.595 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2319525606 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 27,648 | 5.696 | No |
| `.rsrc` | 2,048 | 4.837 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **443** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v4.0.30319
#Strings
Action`10
<>p__0
IEnumerable`1
CallSite`1
Task`1
HttpHeaderValueCollection`1
List`1
__StaticArrayInitTypeSize=32
Microsoft.Win32
ToInt32
<>o__2
X509Certificate2
HMACSHA256
Sha256
Aes256
aes256
get_UTF8
<Module>
<PrivateImplementationDetails>
1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B
ES_SYSTEM_REQUIRED
ES_DISPLAY_REQUIRED
MapNameToOID
get_FormatID
EXECUTION_STATE
get_ASCII
System.IO
ES_CONTINUOUS
AsyncRAT
get_IV
set_IV
GenerateIV
value__
ReadServertData
MessagePackLib
mscorlib
System.Collections.Generic
Microsoft.VisualBasic
get_SendSync
ReadAsStringAsync
GetAsync
EndRead
BeginRead
Thread
ParseAdd
SHA256Managed
get_Connected
get_IsConnected
set_IsConnected
Received
get_Guid
<SendSync>k__BackingField
<IsConnected>k__BackingField
<KeepAlive>k__BackingField
<HeaderSize>k__BackingField
<Ping>k__BackingField
<ActivatePong>k__BackingField
<Interval>k__BackingField
<Buffer>k__BackingField
<Offset>k__BackingField
<SslClient>k__BackingField
<TcpClient>k__BackingField
Append
RegistryValueKind
Replace
CreateInstance
get_StatusCode
HttpStatusCode
get_IsSuccessStatusCode
set_Mode
FileMode
PaddingMode
EnterDebugMode
CryptoStreamMode
CipherMode
SelectMode
DeleteSubKeyTree
get_Message
HttpResponseMessage
get_AcceptLanguage
DetectSandboxie
Invoke
Enumerable
IDisposable
get_Handle
RuntimeFieldHandle
GetModuleHandle
RuntimeTypeHandle
GetTypeFromHandle
WaitHandle
InstallFile
IsInRole
WindowsBuiltInRole
Console
GetActiveWindowTitle
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Client.Algorithm.Sha256.ComputeHash` | `0x4045a8` | 39512 | ✓ |
| `method.Client.Connection.ClientSocket.InitializeClient` | `0x402610` | 888 | ✓ |
| `method.Client.Install.NormalStartup.Install` | `0x402ec8` | 796 | ✓ |
| `method.Client.Settings.InitializeSettings` | `0x402168` | 736 | ✓ |
| `method.Client.Handle_Packet.Packet.Read` | `0x403ca4` | 616 | ✓ |
| `method.Client.Connection.ClientSocket.ReadServertData` | `0x402a2c` | 584 | ✓ |
| `method.Client.Helper.IdSender.SendInfo` | `0x403594` | 464 | ✓ |
| `method.Client.Algorithm.Aes256.Decrypt` | `0x4042fc` | 456 | ✓ |
| `method.Client.Connection.ClientSocket.Send` | `0x402c74` | 392 | ✓ |
| `method.Client.Algorithm.Aes256.Encrypt` | `0x40416c` | 360 | ✓ |
| `method.Client.Helper.Anti_Analysis.DetectManufacturer` | `0x4032d8` | 304 | ✓ |
| `method.Client.Handle_Packet.Packet.Invoke` | `0x403f0c` | 296 | ✓ |
| `entry0` | `0x402050` | 268 | ✓ |
| `method.Client.Helper.Methods.Antivirus` | `0x4037fc` | 232 | ✓ |
| `method.Client.Settings..cctor` | `0x4024b4` | 188 | ✓ |
| `sym.Client.Algorithm.Sha256.ComputeHash` | `0x40451c` | 140 | ✓ |
| `method.Client.Helper.HwidGen.HWID` | `0x40349c` | 128 | ✓ |
| `method.Client.Helper.HwidGen.GetHash` | `0x40351c` | 120 | ✓ |
| `method.Client.Algorithm.Aes256..ctor` | `0x4040cc` | 120 | ✓ |
| `method.Client.Connection.ClientSocket.Reconnect` | `0x4029b8` | 116 | ✓ |
| `method.Client.Connection.ClientSocket.KeepAlivePacket` | `0x402dfc` | 116 | ✓ |
| `method.Client.Helper.Methods.ClientOnExit` | `0x40378c` | 112 | ✓ |
| `method.Client.Helper.SetRegistry.GetValue` | `0x403b40` | 112 | ✓ |
| `method.Client.Helper.SetRegistry.DeleteSubKey` | `0x403c1c` | 112 | ✓ |
| `method.Client.Settings.VerifyHash` | `0x402448` | 108 | ✓ |
| `method.Client.Helper.SetRegistry.SetValue` | `0x403ad4` | 108 | ✓ |
| `method.Client.Helper.SetRegistry.DeleteValue` | `0x403bb0` | 108 | ✓ |
| `method.Client.Helper.Methods.GetActiveWindowTitle` | `0x403968` | 96 | ✓ |
| `method.Client.Helper.Anti_Analysis.IsSmallDisk` | `0x403230` | 88 | ✓ |
| `method.Client.Helper.Anti_Analysis.IsXP` | `0x403288` | 80 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Client.Algorithm.Aes256..ctor.c`](code/method.Client.Algorithm.Aes256..ctor.c)
- [`code/method.Client.Algorithm.Aes256.Decrypt.c`](code/method.Client.Algorithm.Aes256.Decrypt.c)
- [`code/method.Client.Algorithm.Aes256.Encrypt.c`](code/method.Client.Algorithm.Aes256.Encrypt.c)
- [`code/method.Client.Algorithm.Sha256.ComputeHash.c`](code/method.Client.Algorithm.Sha256.ComputeHash.c)
- [`code/method.Client.Connection.ClientSocket.InitializeClient.c`](code/method.Client.Connection.ClientSocket.InitializeClient.c)
- [`code/method.Client.Connection.ClientSocket.KeepAlivePacket.c`](code/method.Client.Connection.ClientSocket.KeepAlivePacket.c)
- [`code/method.Client.Connection.ClientSocket.ReadServertData.c`](code/method.Client.Connection.ClientSocket.ReadServertData.c)
- [`code/method.Client.Connection.ClientSocket.Reconnect.c`](code/method.Client.Connection.ClientSocket.Reconnect.c)
- [`code/method.Client.Connection.ClientSocket.Send.c`](code/method.Client.Connection.ClientSocket.Send.c)
- [`code/method.Client.Handle_Packet.Packet.Invoke.c`](code/method.Client.Handle_Packet.Packet.Invoke.c)
- [`code/method.Client.Handle_Packet.Packet.Read.c`](code/method.Client.Handle_Packet.Packet.Read.c)
- [`code/method.Client.Helper.Anti_Analysis.DetectManufacturer.c`](code/method.Client.Helper.Anti_Analysis.DetectManufacturer.c)
- [`code/method.Client.Helper.Anti_Analysis.IsSmallDisk.c`](code/method.Client.Helper.Anti_Analysis.IsSmallDisk.c)
- [`code/method.Client.Helper.Anti_Analysis.IsXP.c`](code/method.Client.Helper.Anti_Analysis.IsXP.c)
- [`code/method.Client.Helper.HwidGen.GetHash.c`](code/method.Client.Helper.HwidGen.GetHash.c)
- [`code/method.Client.Helper.HwidGen.HWID.c`](code/method.Client.Helper.HwidGen.HWID.c)
- [`code/method.Client.Helper.IdSender.SendInfo.c`](code/method.Client.Helper.IdSender.SendInfo.c)
- [`code/method.Client.Helper.Methods.Antivirus.c`](code/method.Client.Helper.Methods.Antivirus.c)
- [`code/method.Client.Helper.Methods.ClientOnExit.c`](code/method.Client.Helper.Methods.ClientOnExit.c)
- [`code/method.Client.Helper.Methods.GetActiveWindowTitle.c`](code/method.Client.Helper.Methods.GetActiveWindowTitle.c)
- [`code/method.Client.Helper.SetRegistry.DeleteSubKey.c`](code/method.Client.Helper.SetRegistry.DeleteSubKey.c)
- [`code/method.Client.Helper.SetRegistry.DeleteValue.c`](code/method.Client.Helper.SetRegistry.DeleteValue.c)
- [`code/method.Client.Helper.SetRegistry.GetValue.c`](code/method.Client.Helper.SetRegistry.GetValue.c)
- [`code/method.Client.Helper.SetRegistry.SetValue.c`](code/method.Client.Helper.SetRegistry.SetValue.c)
- [`code/method.Client.Install.NormalStartup.Install.c`](code/method.Client.Install.NormalStartup.Install.c)
- [`code/method.Client.Settings..cctor.c`](code/method.Client.Settings..cctor.c)
- [`code/method.Client.Settings.InitializeSettings.c`](code/method.Client.Settings.InitializeSettings.c)
- [`code/method.Client.Settings.VerifyHash.c`](code/method.Client.Settings.VerifyHash.c)
- [`code/sym.Client.Algorithm.Sha256.ComputeHash.c`](code/sym.Client.Algorithm.Sha256.ComputeHash.c)

## Behavioral Analysis

The final analysis of **AsyncRAT** has been updated following the review of disassembly chunk 5/5. This concluding segment reinforces the malware’s sophisticated profile, specifically focusing on environmental awareness (anti-analysis) and context-aware monitoring.

### Updated Analysis Summary: AsyncRAT (Chunk 5/5)

This final section of the disassembly reveals how the malware attempts to identify its execution environment and gather specific information about user activity.

#### 1. Advanced Anti-Analysis Techniques
The inclusion of the `method.Client.Helper.Anti_Analysis` namespace confirms a dedicated module for detecting analysis environments:
*   **`IsSmallDisk`**: This function is a classic anti-VM/anti-sandbox technique. Virtual machines (VMs) and automated sandboxes often present smaller or non-standard disk sizes compared to physical workstations. If the malware detects a "small" disk, it may cease malicious activity to avoid being flagged by automated security systems.
*   **`IsXP`**: This checks for legacy operating system versions. While potentially a compatibility check, in malware analysis, this is often used to detect specific sandbox configurations or to ensure the RAT behaves consistently across different environments while evading newer, more stringent sandboxing detections.

#### 2. Contextual Awareness & Reconnaissance
The function **`GetActiveWindowTitle`** (despite being buried under significant obfuscation) points toward a capability for targeted information gathering:
*   **Target Tracking**: By identifying the title of the window currently in focus, the attacker can determine what applications the victim is using at any given moment. 
*   **Strategic Timing:** This allows the threat actor to know if the user is interacting with high-value targets (e.g., banking websites, corporate email clients, or cryptocurrency wallets), enabling them to time their actions or additional payloads more effectively.

#### 3. Extreme "Noise" Injection as a Defensive Layer
The disassembly in this chunk continues to show an extreme level of **instructional noise**. The compiler/packer has inserted:
*   **Complex Arithmetic Chains**: Using `CONCAT`, `CARRY` checks, and large constant offsets (e.g., `0x21ffffda`) for operations that essentially boil down to simple logical checks or movements.
*   **Stack Manipulation & Overlaps**: The "overlapping instruction" warnings in both the anti-analysis functions and the window title functions indicate a high-level effort to break the decompiler's ability to generate clean, readable code. This forces human analysts to spend significantly more time manually cleaning up the assembly to find the actual logic.

---

### Final Technical Summary for Incident Response

The final set of data completes the profile of AsyncRAT as a highly professional, sophisticated Remote Access Trojan (RAT).

*   **Advanced Anti-Analysis Suite:** The presence of `IsSmallDisk` and `IsXP` confirms that the malware is "sandbox-aware." It actively tries to determine if it is being analyzed by security professionals before fully deploying its features.
*   **Contextual Data Harvesting:** The ability to monitor active window titles suggests the attacker aims for more than just remote control; they want to know exactly what the user is doing in real-time, allowing for targeted data theft or social engineering.
*   **High Barrier to Entry (Analysis):** The deliberate use of "junk code" and overlapping instructions isn't just a technical byproduct—it’s a defensive strategy to maximize **Time-to-Analyze**. This ensures the malware remains effective in the wild longer by frustrating automated tools and slowing down human researchers.

**Final Recommendation:**
1.  **Advanced Detection:** Because of the robust anti-analysis features, standard "off-the-shelf" sandboxes may produce false negatives (the malware staying dormant when it detects a virtual environment). **Hardware-assisted analysis or custom-hardened VMs are recommended.**
2.  **Full System Remediation:** Given the sophistication of the persistence and obfuscation mechanisms, any infection should be treated as high-severity. Removal must include thorough scanning for Registry keys (identified in Chunk 4) and a check for additional hidden scripts that might be triggered by changes in active window focus.
3.  **Intel Gathering:** Indicators of Compromise (IOCs) should include not just the primary executable, but also any behavior related to "active window" monitoring or environmental checks as part of the behavioral signature.

---

### Final Consolidated Findings (Chunks 1-5):
1.  **Encryption & Integrity:** Uses AES-256 and SHA-256 for secure communication and integrity verification.
2.  **Unique Fingerprinting:** Uses HWID generation to uniquely identify each infected machine for the attacker.
3.  **Resilient Connectivity:** Implements robust logic to ensure it remains connected to the C2 server despite network fluctuations.
4.  **Sophisticated Obfuscation:** Employs extreme "junk" code, bitwise complexities, and intentional disassembly errors (overlapping instructions) to frustrate automated tools and human analysts.
5.  **Persistence & Configuration:** Uses Windows Registry keys for storing configuration data and maintaining its presence on the system.
6.  **Anti-Analysis/Evasion:** Specifically includes checks for virtualized environments (`IsSmallDisk`) and older OS versions (`IsXP`).
7.  **Contextual Monitoring:** Actively monitors user activity through functions like `GetActiveWindowTitle` to provide the attacker with real-time context on what the victim is currently doing.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided for **AsyncRAT**, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of "instructional noise," complex arithmetic chains, and overlapping instructions is specifically designed to frustrate decompilers and delay human analysis. |
| **T1573** | Encrypted Channel | The implementation of AES-256 for communication ensures that the data exchanged between the RAT and the C2 server remains hidden from network inspection. |
| **T1547.001** | Registry Run Keys / Command Execution | The use of Windows Registry keys (identified in Chunk 4) to maintain persistence is a standard method for ensuring the malware survives a reboot. |
| **T1112** | System Information Discovery* | The `GetActiveWindowTitle` function provides context-aware tracking, allowing the attacker to identify high-value targets like banking or crypto applications. |
| **T1036** | Masquerading / Defense Evasion | The inclusion of `IsSmallDisk` and `IsXP` functions demonstrates an attempt to detect virtualization/sandboxes to evade detection by security researchers. |

*\*Note: While "Contextual Awareness" is a broad behavior, it falls under the **Discovery** tactic or specifically identifies high-value targets for subsequent actions.*

---

## Indicators of Compromise

As a threat intelligence analyst, I have processed the provided strings and behavioral analysis to extract the following Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **AsyncRAT.exe** (Malware executable filename)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   **1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B** (Identified as a potential unique identifier or signature hash within the binary).

### **Other artifacts**
*   **Malware Family:** AsyncRAT
*   **Anti-Analysis Functions:** 
    *   `IsSmallDisk` (Used to detect virtualized/sandbox environments)
    *   `IsXP` (Used for environment checking and potential evasion)
*   **Contextual Tracking:** `GetActiveWindowTitle` (Used to monitor user activity and identify high-value targets like banking or crypto apps).
*   **Cryptographic Protocols:** 
    *   AES-256
    *   SHA-256
    *   HMACSHA256
*   **Obfuscation Techniques:** 
    *   Instructional noise (Complex arithmetic chains)
    *   Overlapping instructions (Designed to break decompiler output)

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: AsyncRAT
2. **Malware type**: RAT (Remote Access Trojan)
3. **Confidence**: High
4. **Key evidence**:
    * **Explicit Identification:** The report explicitly identifies the malware as "AsyncRAT" and describes it as a "sophisticated Remote Access Trojan."
    * **Remote Administration & Surveillance:** The inclusion of `GetActiveWindowTitle` indicates intent to monitor user activity in real-time (e.g., banking or crypto) for targeted data theft.
    * **Advanced Evasion Tactics:** The malware employs sophisticated anti-analysis features (`IsSmallDisk`, `IsXP`) and "instructional noise" (overlapping instructions, complex arithmetic) specifically designed to bypass automated sandboxes and frustrate human reverse engineers.
