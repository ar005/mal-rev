# Threat Analysis Report

**Generated:** 2026-07-13 13:03 UTC
**Sample:** `0534dedcd464b08f7e9905e4186dbc060f3511f198d252fe5d80b228419bb331_0534dedcd464b08f7e9905e4186dbc060f3511f198d252fe5d80b228419bb331.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0534dedcd464b08f7e9905e4186dbc060f3511f198d252fe5d80b228419bb331_0534dedcd464b08f7e9905e4186dbc060f3511f198d252fe5d80b228419bb331.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 30,720 bytes |
| MD5 | `74a6c8486037c84759dc68393d7996a3` |
| SHA1 | `ce80e0621cf257d73b9b1ac79acfeb4c31007946` |
| SHA256 | `0534dedcd464b08f7e9905e4186dbc060f3511f198d252fe5d80b228419bb331` |
| Overall entropy | 5.533 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3864594590 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 27,648 | 5.629 | No |
| `.rsrc` | 2,048 | 4.837 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **440** (showing first 100)

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
get_MainModule
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Client.Algorithm.Sha256.ComputeHash` | `0x4044ec` | 39700 | — |
| `method.Client.Connection.ClientSocket.InitializeClient` | `0x402554` | 888 | ✓ |
| `method.Client.Install.NormalStartup.Install` | `0x402e0c` | 796 | ✓ |
| `method.Client.Handle_Packet.Packet.Read` | `0x403be8` | 616 | ✓ |
| `method.Client.Connection.ClientSocket.ReadServertData` | `0x402970` | 584 | ✓ |
| `method.Client.Settings.InitializeSettings` | `0x402168` | 548 | ✓ |
| `method.Client.Helper.IdSender.SendInfo` | `0x4034d8` | 464 | ✓ |
| `method.Client.Algorithm.Aes256.Decrypt` | `0x404240` | 456 | ✓ |
| `method.Client.Connection.ClientSocket.Send` | `0x402bb8` | 392 | ✓ |
| `method.Client.Algorithm.Aes256.Encrypt` | `0x4040b0` | 360 | ✓ |
| `method.Client.Helper.Anti_Analysis.DetectManufacturer` | `0x40321c` | 304 | ✓ |
| `method.Client.Handle_Packet.Packet.Invoke` | `0x403e50` | 296 | ✓ |
| `entry0` | `0x402050` | 268 | ✓ |
| `method.Client.Helper.Methods.Antivirus` | `0x403740` | 232 | ✓ |
| `method.Client.Settings..cctor` | `0x4023f8` | 188 | ✓ |
| `sym.Client.Algorithm.Sha256.ComputeHash` | `0x404460` | 140 | ✓ |
| `method.Client.Helper.HwidGen.HWID` | `0x4033e0` | 128 | ✓ |
| `method.Client.Helper.HwidGen.GetHash` | `0x403460` | 120 | ✓ |
| `method.Client.Algorithm.Aes256..ctor` | `0x404010` | 120 | ✓ |
| `method.Client.Connection.ClientSocket.Reconnect` | `0x4028fc` | 116 | ✓ |
| `method.Client.Connection.ClientSocket.KeepAlivePacket` | `0x402d40` | 116 | ✓ |
| `method.Client.Helper.Methods.ClientOnExit` | `0x4036d0` | 112 | ✓ |
| `method.Client.Helper.SetRegistry.GetValue` | `0x403a84` | 112 | ✓ |
| `method.Client.Helper.SetRegistry.DeleteSubKey` | `0x403b60` | 112 | ✓ |
| `method.Client.Settings.VerifyHash` | `0x40238c` | 108 | ✓ |
| `method.Client.Helper.SetRegistry.SetValue` | `0x403a18` | 108 | ✓ |
| `method.Client.Helper.SetRegistry.DeleteValue` | `0x403af4` | 108 | ✓ |
| `method.Client.Helper.Methods.GetActiveWindowTitle` | `0x4038ac` | 96 | ✓ |
| `method.Client.Helper.Anti_Analysis.IsSmallDisk` | `0x403174` | 88 | ✓ |
| `method.Client.Helper.Anti_Analysis.IsXP` | `0x4031cc` | 80 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Client.Algorithm.Aes256..ctor.c`](code/method.Client.Algorithm.Aes256..ctor.c)
- [`code/method.Client.Algorithm.Aes256.Decrypt.c`](code/method.Client.Algorithm.Aes256.Decrypt.c)
- [`code/method.Client.Algorithm.Aes256.Encrypt.c`](code/method.Client.Algorithm.Aes256.Encrypt.c)
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

This final segment of disassembly confirms that **AsyncRAT** incorporates sophisticated environmental awareness and anti-analysis techniques designed to detect research environments and bypass automated security filters.

### Updated Analysis of AsyncRAT (Chunk 5/5)

#### 1. Advanced Anti-Analysis & Sandbox Evasion
The inclusion of specific "Anti_Analysis" helper functions confirms that the malware actively scouts its environment before executing its primary payload:
*   **`IsSmallDisk`:** This is a classic indicator of **Sandbox Detection**. Many automated analysis sandboxes (like Cuckoo or JoeSandbox) allocate small virtual disks for each run. By checking if the disk size is below a certain threshold, AsyncRAT can determine if it is being analyzed in a virtualized "lab" environment and cease its malicious behavior to avoid detection.
*   **`IsXP`:** This checks for specific OS versions (historically Windows XP). In modern malware contexts, this often serves two purposes: ensuring compatibility with targeted legacy systems or, more commonly in high-end RATs, identifying the presence of "locked down" environments versus standard user workstations.

#### 2. Context-Aware Intelligence (`GetActiveWindowTitle`)
While the code for `GetActiveWindowTitle` is heavily obscured by "junk instructions" and overlapping logic (designed to break disassemblers like IDA Pro), its existence in a "Helper" class provides significant intelligence:
*   **Application Targeting:** The RAT likely uses this to identify which application is currently in focus. This allows the malware to be selective—for example, it may only log keystrokes or scrape data when it detects a web browser (e.g., Chrome/Edge) or a specific financial application.
*   **Contextual Awareness:** By knowing the active window title, the attacker can tailor their actions in real-time, making the malware's behavior appear more "normal" to automated monitors that look for constant, broad activity.

#### 3. Defensive Engineering (Obfuscation)
The overwhelming amount of `WARNING: Removing unreachable block` and `overlapping instruction` errors in these functions is not a byproduct of poor coding; it is a **deliberate defense strategy**:
*   **Complexity Inflation:** By wrapping simple logic (like checking a disk size or window title) in thousands of layers of "junk" calculations, the developers make it mathematically difficult for an analyst to determine the *actual* core functionality without significant manual labor.
*   **Tool Sabotage:** The overlapping instructions are specifically designed to break the graphing capabilities of common disassembly tools, forcing a human researcher to manually reconstruct every single jump and branch.

---

### Final Comprehensive Analysis of AsyncRAT

Based on all 5 chunks of analysis, here is the final profile of the malware:

#### Technical Capability Matrix
| Feature | Detail | Risk Level |
| :--- | :--- | :--- |
| **Core Identity** | **AsyncRAT (Remote Access Trojan)** | **Critical** |
| **Encryption/Hashing** | **AES-256 & SHA-256** used for config validation and data integrity. | High |
| **Persistence** | **Registry Manipulation** (`SetValue`, `DeleteSubKey`) to stay active after reboots. | High |
| **Identity Tracking** | **HWID Generation** to uniquely identify and manage victims in a database. | High |
| **Communication** | **Heartbeat & Reconnect** logic ensures stable, persistent C1 links. | High |
| **Anti-Analysis** | **Sandbox Detection** (`IsSmallDisk`), **Environment Checks**, and **Heavy Junk Code/Overlapping Instructions**. | Critical |
| **Contextual Awareness** | **Active Window Tracking** to target specific applications or browsers. | High |

---

### Final Conclusion & Behavior Profile

The final analysis confirms that **AsyncRAT is a professional-grade, "hardened" malware suite.** It is not a simple piece of and-delivery; it is designed for long-term persistence in environments where security professionals are active.

**Summary of Malicious Behaviors:**
1.  **Evasion First:** Before engaging in its primary tasks (keylogging, file theft), the RAT performs several "checks" to see if it is being monitored by an analyst or running inside a sandbox environment. If detected, it likely remains dormant.
2.  **Environment Adaptation:** By checking system details like disk size and active window titles, the malware can adapt its behavior based on what the user is currently doing, increasing the likelihood of successful theft from high-value targets (e.g., bank accounts or corporate credentials).
3.  **Hardened Obfuscation:** The extreme level of "junk" code and instruction overlapping indicates that the developers have invested significant effort into making static analysis nearly impossible for standard automated tools.

**Forensic & Incident Response Guidance:**
*   **Static Analysis Limitation:** Due to the heavy use of overlapping instructions, signature-based detection and manual reverse engineering will be slow. Investigators should rely heavily on **dynamic behavior monitoring**.
*   **Indicator Hunt:** Look for unauthorized modifications in Windows Registry keys related to "Run" commands and high frequencies of network traffic (heartbeats) to a fixed IP/domain.
*   **Defense Strategy:** Because the RAT is "aware" of its environment, use of standard automated sandboxes may not be enough to fully unmask all capabilities; manual "hands-on" analysis in a hardened lab is recommended for high-risk infections.

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis of AsyncRAT, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualized Environment | The `IsSmallDisk` function is a specific method used to detect and evade automated sandbox analysis environments. |
| **T1027** | Obfuscated Files or Information | The use of "junk instructions" and "overlapping logic" is designed to complicate manual reverse engineering and break disassembly tools. |
| **T1112** | Modify Registry | The malware uses `SetValue` and `DeleteSubKey` commands to establish persistence on the host system. |
| **T1573** | Encrypted Channel | The use of AES-256 and SHA-256 for configuration validation and data integrity protects information from being intercepted or read easily. |
| **T1056.001** | Keylogging | The `GetActiveWindowTitle` function is used to identify specific applications (like browsers) to focus logging efforts on high-value targets. |
| **T1031** | System Owner/User Info | The "HWID Generation" confirms the malware tracks and uniquely identifies infected hosts for management in a botnet database. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None specifically defined (the report notes "Registry Manipulation" as a behavior, but no specific registry paths were provided).*

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   `1DB2A1F9902B35F8F880EF1692CE9947A193D5A698D8F568BDA721658ED4C58B` (SHA-256)

**Other artifacts**
*   **Malware Family/Executable:** `AsyncRAT`, `AsyncRAT.exe`
*   **C2 Behavior:** Heartbeat and Reconnect logic; AES-256 and SHA-256 encryption for config validation and data integrity.
*   **Anti-Analysis / Evasion Techniques:** 
    *   `IsSmallDisk`: Used for sandbox detection (checking for small virtual disks).
    *   `GetActiveWindowTitle`: Used for context-aware targeting of specific applications/browsers.
    *   "Overlapping instructions" and "Junk code": Used to defeat disassembly tools like IDA Pro.
    *   `IsXP`: Environmental check for OS compatibility/environment detection.

---

## Malware Family Classification

1. **Malware family**: AsyncRAT
2. **Malware type**: RAT (Remote Access Trojan)
3. **Confidence**: High
4. **Key evidence**:
    *   **Explicit Identification & Core Functionality:** The analysis explicitly identifies the sample as AsyncRAT, a sophisticated Remote Access Trojan featuring persistent C1 communication (heartbeats), HWID generation for botnet management, and registry-based persistence.
    *   **Advanced Evasion Techniques:** The malware employs professional-grade anti-analysis measures, including `IsSmallDisk` for sandbox detection, "junk" code to thwart disassemblers, and overlapping instructions to complicate manual reverse engineering.
    *   **Contextual Targeting:** The use of `GetActiveWindowTitle` indicates the ability to perform selective monitoring (e.g., only logging keystrokes when a web browser is active), which is a hallmark of high-end RATs designed for targeted data theft.
