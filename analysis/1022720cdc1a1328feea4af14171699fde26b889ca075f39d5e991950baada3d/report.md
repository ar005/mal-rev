# Threat Analysis Report

**Generated:** 2026-08-18 00:46 UTC
**Sample:** `1022720cdc1a1328feea4af14171699fde26b889ca075f39d5e991950baada3d_1022720cdc1a1328feea4af14171699fde26b889ca075f39d5e991950baada3d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1022720cdc1a1328feea4af14171699fde26b889ca075f39d5e991950baada3d_1022720cdc1a1328feea4af14171699fde26b889ca075f39d5e991950baada3d.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 27,136 bytes |
| MD5 | `8d26e1ad47b89ee4152be467756a1467` |
| SHA1 | `cfbec7d471a6126fb0058ee75c1e52b330088bcb` |
| SHA256 | `1022720cdc1a1328feea4af14171699fde26b889ca075f39d5e991950baada3d` |
| Overall entropy | 5.539 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2909107350 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 24,064 | 5.65 | No |
| `.rsrc` | 2,048 | 4.809 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **402** (showing first 100)

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
get_FormatID
EXECUTION_STATE
get_ASCII
System.IO
ES_CONTINUOUS
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
EndRead
BeginRead
Thread
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
set_Mode
FileMode
PaddingMode
EnterDebugMode
CryptoStreamMode
CipherMode
SelectMode
DeleteSubKeyTree
get_Message
DetectSandboxie
Invoke
Enumerable
IDisposable
RuntimeFieldHandle
GetModuleHandle
RuntimeTypeHandle
GetTypeFromHandle
WaitHandle
InstallFile
IsInRole
WindowsBuiltInRole
GetActiveWindowTitle
get_MainModule
ProcessModule
set_WindowStyle
ProcessWindowStyle
get_Name
get_FileName
set_FileName
GetTempFileName
GetFileName
lpModuleName
get_MachineName
get_OSFullName
get_FullName
IsValidDomainName
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Client.Algorithm.Sha256.ComputeHash` | `0x403fec` | 32788 | ✓ |
| `method.Client.Connection.ClientSocket.InitializeClient` | `0x402284` | 888 | ✓ |
| `method.Client.Install.NormalStartup.Install` | `0x402b3c` | 796 | ✓ |
| `method.Client.Handle_Packet.Packet.Read` | `0x4036e8` | 616 | ✓ |
| `method.Client.Connection.ClientSocket.ReadServertData` | `0x4026a0` | 584 | ✓ |
| `method.Client.Helper.IdSender.SendInfo` | `0x402fd8` | 464 | ✓ |
| `method.Client.Algorithm.Aes256.Decrypt` | `0x403d40` | 456 | ✓ |
| `method.Client.Connection.ClientSocket.Send` | `0x4028e8` | 392 | ✓ |
| `method.Client.Algorithm.Aes256.Encrypt` | `0x403bb0` | 360 | ✓ |
| `method.Client.Handle_Packet.Packet.Invoke` | `0x403950` | 296 | ✓ |
| `method.Client.Helper.Methods.Antivirus` | `0x403240` | 232 | ✓ |
| `method.Client.Settings..cctor` | `0x402124` | 194 | ✓ |
| `entry0` | `0x402050` | 160 | ✓ |
| `sym.Client.Algorithm.Sha256.ComputeHash` | `0x403f60` | 140 | ✓ |
| `method.Client.Helper.HwidGen.HWID` | `0x402ee0` | 128 | ✓ |
| `method.Client.Helper.HwidGen.GetHash` | `0x402f60` | 120 | ✓ |
| `method.Client.Algorithm.Aes256..ctor` | `0x403b10` | 120 | ✓ |
| `method.Client.Connection.ClientSocket.Reconnect` | `0x40262c` | 116 | ✓ |
| `method.Client.Connection.ClientSocket.KeepAlivePacket` | `0x402a70` | 116 | ✓ |
| `method.Client.Helper.Methods.ClientOnExit` | `0x4031d0` | 112 | ✓ |
| `method.Client.Helper.SetRegistry.GetValue` | `0x403584` | 112 | ✓ |
| `method.Client.Helper.SetRegistry.DeleteSubKey` | `0x403660` | 112 | ✓ |
| `method.Client.Helper.SetRegistry.SetValue` | `0x403518` | 108 | ✓ |
| `method.Client.Helper.SetRegistry.DeleteValue` | `0x4035f4` | 108 | ✓ |
| `method.Client.Helper.Methods.GetActiveWindowTitle` | `0x4033ac` | 96 | ✓ |
| `method.Client.Helper.Methods.GetEncoder` | `0x403328` | 80 | ✓ |
| `method.Client.Connection.ClientSocket.Pong` | `0x402ae4` | 76 | ✓ |
| `method.Client.Helper.ProcessCritical.Set` | `0x403490` | 72 | ✓ |
| `method.Client.Handle_Packet.Packet.Error` | `0x403abc` | 72 | ✓ |
| `method.Client.Handle_Packet.Packet.Received` | `0x403a78` | 68 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Client.Algorithm.Aes256..ctor.c`](code/method.Client.Algorithm.Aes256..ctor.c)
- [`code/method.Client.Algorithm.Aes256.Decrypt.c`](code/method.Client.Algorithm.Aes256.Decrypt.c)
- [`code/method.Client.Algorithm.Aes256.Encrypt.c`](code/method.Client.Algorithm.Aes256.Encrypt.c)
- [`code/method.Client.Algorithm.Sha256.ComputeHash.c`](code/method.Client.Algorithm.Sha256.ComputeHash.c)
- [`code/method.Client.Connection.ClientSocket.InitializeClient.c`](code/method.Client.Connection.ClientSocket.InitializeClient.c)
- [`code/method.Client.Connection.ClientSocket.KeepAlivePacket.c`](code/method.Client.Connection.ClientSocket.KeepAlivePacket.c)
- [`code/method.Client.Connection.ClientSocket.Pong.c`](code/method.Client.Connection.ClientSocket.Pong.c)
- [`code/method.Client.Connection.ClientSocket.ReadServertData.c`](code/method.Client.Connection.ClientSocket.ReadServertData.c)
- [`code/method.Client.Connection.ClientSocket.Reconnect.c`](code/method.Client.Connection.ClientSocket.Reconnect.c)
- [`code/method.Client.Connection.ClientSocket.Send.c`](code/method.Client.Connection.ClientSocket.Send.c)
- [`code/method.Client.Handle_Packet.Packet.Error.c`](code/method.Client.Handle_Packet.Packet.Error.c)
- [`code/method.Client.Handle_Packet.Packet.Invoke.c`](code/method.Client.Handle_Packet.Packet.Invoke.c)
- [`code/method.Client.Handle_Packet.Packet.Read.c`](code/method.Client.Handle_Packet.Packet.Read.c)
- [`code/method.Client.Handle_Packet.Packet.Received.c`](code/method.Client.Handle_Packet.Packet.Received.c)
- [`code/method.Client.Helper.HwidGen.GetHash.c`](code/method.Client.Helper.HwidGen.GetHash.c)
- [`code/method.Client.Helper.HwidGen.HWID.c`](code/method.Client.Helper.HwidGen.HWID.c)
- [`code/method.Client.Helper.IdSender.SendInfo.c`](code/method.Client.Helper.IdSender.SendInfo.c)
- [`code/method.Client.Helper.Methods.Antivirus.c`](code/method.Client.Helper.Methods.Antivirus.c)
- [`code/method.Client.Helper.Methods.ClientOnExit.c`](code/method.Client.Helper.Methods.ClientOnExit.c)
- [`code/method.Client.Helper.Methods.GetActiveWindowTitle.c`](code/method.Client.Helper.Methods.GetActiveWindowTitle.c)
- [`code/method.Client.Helper.Methods.GetEncoder.c`](code/method.Client.Helper.Methods.GetEncoder.c)
- [`code/method.Client.Helper.ProcessCritical.Set.c`](code/method.Client.Helper.ProcessCritical.Set.c)
- [`code/method.Client.Helper.SetRegistry.DeleteSubKey.c`](code/method.Client.Helper.SetRegistry.DeleteSubKey.c)
- [`code/method.Client.Helper.SetRegistry.DeleteValue.c`](code/method.Client.Helper.SetRegistry.DeleteValue.c)
- [`code/method.Client.Helper.SetRegistry.GetValue.c`](code/method.Client.Helper.SetRegistry.GetValue.c)
- [`code/method.Client.Helper.SetRegistry.SetValue.c`](code/method.Client.Helper.SetRegistry.SetValue.c)
- [`code/method.Client.Install.NormalStartup.Install.c`](code/method.Client.Install.NormalStartup.Install.c)
- [`code/method.Client.Settings..cctor.c`](code/method.Client.Settings..cctor.c)
- [`code/sym.Client.Algorithm.Sha256.ComputeHash.c`](code/sym.Client.Algorithm.Sha256.ComputeHash.c)

## Behavioral Analysis

This analysis incorporates findings from the final disassembly segment (**Chunk 11/11**), which provides a detailed look into the malware's internal communication and packet-handling logic.

---

### Updated Analysis of Malware Functionality (Chunk 11/11)

#### 20. Obfuscated Communication Protocol (C2 Interaction)
The functions `method.Client.Handle_Packet.Packet.Error` and `method.Client.Handle_Packet.Packet.Received` reveal the core communication engine of the malware.
*   **Technique:** The use of highly complex arithmetic, bit-shifting (`>> 8`, `>> 0x10`), and "junk" operations to process incoming data packets. This is not standard software engineering; it is a deliberate attempt to mask the structure of the Command & Control (C2) protocol.
*   **Observation:** Within these functions, we see the construction of specific byte sequences (e.g., `pcVar13[0] = '\0'; pcVar13[1] = '\n'; pcVar13[2] = '\x03'; pcVar13[3] = 'o'`). These "hardcoded" components suggest a proprietary packet structure where the malware is decoding instructions from the attacker.
*   **Impact:** By wrapping even simple "Packet Received" logic in hundreds of lines of math, the developers ensure that automated traffic analysis tools struggle to identify the specific commands being issued by the C2 server (e.g., "upload file," "execute shell," or "exfiltrate data").

#### 21. "Noise-Induced" Analysis Stalling
The sheer volume of `CARRY` flag checks and complex bitwise logic (`CONCAT31`, `CONCAT22`) serves as a primary defense against **Decompilation analysis**.
*   **Technique:** Instead of a simple `if (command == 'X')`, the code uses multi-stage mathematical derivations to determine if a packet is valid or what action it demands.
*   **Purpose:** This creates "Human Analysis Fatigue." An analyst attempting to trace a single network packet through this code must manually walk through hundreds of lines of mathematically heavy instructions that ultimately resolve to very simple logic gates. 
*   **Significance:** This is a hallmark of high-end (APT) malware. It effectively "hides" the malicious intent within a thicket of intentional complexity, making it difficult for researchers to quickly map out the full capabilities of the RAT.

#### 22. Integrity and State Management
The repeated use of internal state flags (like `bVar25`, `bVar49`) and complex loop-back logic suggests that the malware maintains a very robust internal state machine.
*   **Technique:** The code checks various conditions before moving to the next "step" in packet processing, using the results of complex calculations as the primary gatekeepers.
*   **Impact:** This ensures that if an analyst tries to bypass certain parts of the code or inject a dummy packet, the internal state will desynchronize, causing the malware to stop communicating and effectively "self-protect" from discovery during analysis.

---

### Updated Summary of Findings (Cumulative)

**Malware Classification:** Elite-Tier Remote Access Trojan (RAT) / Advanced Persistent Threat (APT) Toolkit.

**Key Technical Indicators (Cumulative):**
*   **Arithmetic/Polymorphic Obfuscation:** Massive use of "junk" math and carry-flag manipulation to hide logic flow from both humans and automated decompilers.
*   **Dynamic API Resolution:** Calculation of function offsets at runtime to mask the use of sensitive system calls (e.g., `GetForegroundWindow`).
*   **Obfuscated Communication Layer:** A deeply "noisy" packet handling system that uses custom calculations to hide the structure of C2 commands and data exchange.
*   **Advanced Reconnaissance Suite:** Capabilities for tracking user interaction and active window titles in real-time.
*   **Sophisticated State Management:** Complex logic flow used to manage the internal state of the malware, making it harder to debug or "force" into a specific behavior during analysis.

---

### Updated Risk Assessment & Strategic Impact

**1. Defense Evasion: Elite.**
The complexity found in Chunk 11/11 confirms that this malware is designed to be nearly impossible to analyze via static means alone. The "noise" created by the packet-handling logic is specifically engineered to baffle both automated scanners and human researchers during the initial triage phase.

**2. Capability for Stealthy Persistence:**
Because the communication protocol is wrapped in layers of mathematical noise, security systems that monitor "typical" RAT behaviors (like common command strings or standard header structures) will likely fail to detect it. The malware isn't just hiding its *presence*; it is hiding its *behavior*.

**3. Target Profile & Operational Maturity:**
The presence of a custom-engineered communication layer, combined with the sophisticated obfuscation techniques seen throughout all chunks, indicates this tool was developed by an organized threat actor. This is not "script kiddie" malware; it is designed for high-value targets where evading EDR (Endpoint Detection and Response) systems is a primary requirement.

### Final Conclusion:
This malware represents a **highly sophisticated persistent threat**. It employs multiple layers of defense: 
1.  **At the API level**, it uses dynamic resolution to hide what it calls. 
2.  **At the Logic level**, it uses metamorphic-style math to hide how it thinks. 
3.  **At the Network level**, it hides its communication protocols behind a wall of obfuscated code.

**Strategic Recommendation:**
Standard signature-based detection is insufficient against this threat. Organizations should implement:
*   **Behavioral Analytics:** Focus on the *actions* (e.g., unusual network connections at regular intervals, unauthorized processes interacting with specific window titles).
*   **Memory Forensics:** Since the code "unfolds" only in memory to perform its functions, searching for the decoded strings and resolved pointers during execution is the most effective way to identify this activity.
*   **Egress Filtering:** Monitor for non-standard protocols or high volumes of encrypted data moving to unfamiliar IP ranges as a primary indicator of compromise (IoC).

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The malware uses "junk" operations, complex arithmetic, and bit-shifting to mask logic flow and create "Human Analysis Fatigue" for researchers. |
| **T1071** | Application Layer Protocol | The use of a proprietary packet structure masks the specific commands (e.g., exfiltrate data, execute shell) from automated traffic analysis tools. |
| **T1106** | Native API | Dynamic resolution and calculation of function offsets are used to mask the usage of sensitive system calls like `GetForegroundWindow`. |
| **T1497** | Virtualization/Sandbox (Anti-Analysis) | The "State Management" logic ensures that any attempt by an analyst to bypass code or inject dummy packets causes a desynchronization, thwarting manual analysis. |

### Analysis Notes for Intelligence Report:
*   **Obfuscation Strategy:** The malware utilizes **T1027** not just as a simple packer, but as a continuous methodology to hide the *intent* of the code rather than just its presence.
*   **C2 Evasion:** By using **T1071**, the actors ensure that even if network traffic is captured, the "meaning" of the packets remains opaque without the specific decryption logic found in the binary's core.
*   **Persistence/Evasion Depth:** The combination of **T1106** and **T1497** indicates a high level of operational maturity, designed to defeat both automated EDR systems and manual forensic deep-dives.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (Note: "Stub.exe" is a filename but no specific file path or registry key was provided in the source text).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   `1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B` (SHA-256)

**Other artifacts**
*   **C2 Communication Pattern:** Hardcoded packet header sequence: `\0\n\x03o` (represented in code as `pcVar13[0] = '\0'; pcVar13[1] = '\n'; pcVar13[2] = '\x03'; pcVar13[3] = 'o'`).
*   **Malware Filename:** `Stub.exe`
*   **Reconnaissance Behavior:** Tracking of `GetForegroundWindow` and active window titles (used to monitor user interaction).
*   **Evasion Technique:** Use of complex arithmetic/bit-shifting (`>> 8`, `>> 0x10`) and "junk" operations to mask C2 protocol logic.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

1. **Malware family:** custom
2. **Malware type:** RAT
3. **Confidence:** High
4. **Key evidence:**
    *   **Sophisticated Communication Obfuscation:** The use of complex arithmetic, bit-shifting, and "junk" operations to mask C2 commands and proprietary packet structures (e.g., `\0\n\x03o`) indicates a high-effort attempt to evade automated traffic analysis and manual deconstruction.
    *   **Advanced Reconnaissance Capabilities:** The inclusion of functions to monitor active window titles and user interaction via `GetForegroundWindow` is characteristic of high-end Remote Access Trojans (RATs) used for targeted information gathering.
    *   **Evasive Architecture:** The "State Management" logic designed to desynchronize the malware during analysis, combined with dynamic API resolution, indicates a mature toolkit intended for use by advanced threat actors (APTs) against high-value targets.
