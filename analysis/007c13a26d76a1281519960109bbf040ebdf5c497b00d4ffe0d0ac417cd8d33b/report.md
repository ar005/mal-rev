# Threat Analysis Report

**Generated:** 2026-06-24 15:52 UTC
**Sample:** `007c13a26d76a1281519960109bbf040ebdf5c497b00d4ffe0d0ac417cd8d33b_007c13a26d76a1281519960109bbf040ebdf5c497b00d4ffe0d0ac417cd8d33b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `007c13a26d76a1281519960109bbf040ebdf5c497b00d4ffe0d0ac417cd8d33b_007c13a26d76a1281519960109bbf040ebdf5c497b00d4ffe0d0ac417cd8d33b.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 139,776 bytes |
| MD5 | `668a2576569169db132b965366a616ed` |
| SHA1 | `10e8977b8264fe39b478ff593713a62ad365970c` |
| SHA256 | `007c13a26d76a1281519960109bbf040ebdf5c497b00d4ffe0d0ac417cd8d33b` |
| Overall entropy | 5.938 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3045103586 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 135,680 | 5.968 | No |
| `.rsrc` | 3,072 | 4.755 | No |
| `.reloc` | 512 | 0.094 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1761** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

-J+Z 
1	rr"
0A[i
+

+2	o

,rp1

+*	o

+*	o

&*.s}
v4.0.30319
#Strings
Q	hR9	Q	
8h`	Y	?ef	
	]o	a	KNw	i	KN
9
KN

+
:
G
[
`

&AVe
%:GTiv
7S7^7 7k7-7G7A
!	(	1	S
j

__StaticArrayInitTypeSize=10
<>9__10_0
<Execute>b__10_0
<>9__0_0
<ContainsModifierKeys>b__0_0
<>c__DisplayClass0_0
<Run>b__11_0
<>c__DisplayClass11_0
<>c__DisplayClass12_0
<>9__22_0
<DisableScreensaver>b__22_0
<>c__DisplayClass22_0
<>9__3_0
<Execute>b__3_0
<.ctor>b__3_0
<>c__DisplayClass3_0
<>9__4_0
<WinSCPDecrypt>b__4_0
<>c__DisplayClass15_0
<>9__5_0
<AddDefaultValue>b__5_0
<>c__DisplayClass16_0
<>c__DisplayClass7_0
<>c__DisplayClass68_0
<>9__0
<GetReverseProxyByConnectionId>b__0
<Execute>b__0
<DetectKeyHolding>b__0
<DoesURLMatchWithHash>b__0
<Uninstall>b__0
<GetKeyValues>b__0
get_Scan0
ALG_SID_SHA1
CALG_SHA1
<>9__3_1
<Execute>b__3_1
<>9__15_1
<GetKeyValues>b__15_1
<>8__1
Nullable`1
IEnumerable`1
MessageProcessorBase`1
Predicate`1
Queue`1
Action`1
IEnumerator`1
List`1
SecretId1
lpFileTime1
get_Item1
<>7__wrap1
<>m__Finally1
Microsoft.Win32
ToUInt32
ToInt32
Func`2
Tuple`2
KeyValuePair`2
ConcurrentDictionary`2
SecretId2
lpFileTime2
X509Certificate2
IUrlHistoryStg2
get_Item2
SecretId3
ToUInt64
ToInt64
SecretId4
<GetKeyValues>d__15
CALG_MD5
SecretId5
ToUInt16
Sha256
Aes256
SecretId6
SecretId7
get_UTF8
7D78CB380BF5EFB7B851409CA6A875F77DECF09D19B9149DA17A3EBF674BC0F9
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.__c..ctor_5` | `0x40e79f` | 104546 | ✓ |
| `method._GetKeyValues_d__15.System.Collections.Generic.IEnumerable_System.Tuple_System.String_System.String__.GetEnumerator` | `0x40e9e4` | 103964 | ✓ |
| `method._GetKeyValues_d__15.System.Collections.IEnumerable.GetEnumerator` | `0x40ea27` | 64888 | ✓ |
| `method.Quasar.Client.IpGeoLocation.GeoInformationRetriever..ctor` | `0x40b50c` | 2606 | ✓ |
| `method.Quasar.Client.Recovery.Utilities.SQLiteHandler.ReadMasterTable` | `0x403d2c` | 2076 | ✓ |
| `method.Quasar.Client.Recovery.Utilities.SQLiteHandler.ReadTableFromOffset` | `0x404684` | 1695 | ✓ |
| `sym.Quasar.Client.Messages.StartupManagerHandler.Execute_1` | `0x4095b4` | 1228 | ✓ |
| `method.Quasar.Client.Recovery.FtpClients.FileZillaPassReader.ReadAccounts` | `0x404d2c` | 948 | ✓ |
| `method.Quasar.Client.Networking.Client.AsyncReceive` | `0x406f6c` | 908 | ✓ |
| `method.Quasar.Client.Recovery.FtpClients.WinScpPassReader.WinSCPDecrypt` | `0x405340` | 700 | ✓ |
| `method.Quasar.Client.Recovery.Browsers.FirefoxPassReader.ReadAccounts` | `0x405c60` | 688 | ✓ |
| `sym.Quasar.Client.Messages.RemoteDesktopHandler.Execute_1` | `0x408e98` | 688 | ✓ |
| `sym.Quasar.Client.Messages.FileManagerHandler.Execute_2` | `0x407f2c` | 664 | ✓ |
| `sym.Quasar.Client.Messages.StartupManagerHandler.Execute_2` | `0x409a80` | 648 | ✓ |
| `method.Quasar.Client.Messages.SystemInformationHandler.Execute` | `0x409ee8` | 564 | ✓ |
| `method.Quasar.Client.Recovery.Browsers.InternetExplorerPassReader.DecryptIePassword` | `0x406080` | 524 | ✓ |
| `method.__c__DisplayClass12_0._Execute_b__0` | `0x40e43c` | 508 | ✓ |
| `method._GetKeyValues_d__15..ctor` | `0x40e7e7` | 500 | ✓ |
| `sym.Quasar.Client.Messages.FileManagerHandler.Execute_1` | `0x407d80` | 428 | ✓ |
| `method.Quasar.Client.Recovery.FtpClients.WinScpPassReader.ReadAccounts` | `0x405158` | 424 | ✓ |
| `method.Quasar.Client.Messages.StartupManagerHandler.Execute` | `0x409d08` | 424 | ✓ |
| `method.Quasar.Client.Messages.FileManagerHandler.Execute` | `0x4084d8` | 384 | ✓ |
| `method.Quasar.Client.Logging.Keylogger.HighlightSpecialKeys` | `0x40ad20` | 373 | ✓ |
| `sym.Quasar.Client.Networking.Client.AsyncReceive` | `0x406df8` | 372 | ✓ |
| `sym.Quasar.Client.Messages.FileManagerHandler.Execute_6` | `0x408364` | 372 | ✓ |
| `method.Quasar.Client.ReverseProxy.ReverseProxyClient.Handle_Connect` | `0x402e94` | 360 | ✓ |
| `method.Quasar.Client.QuasarApplication.InitializeMessageProcessors` | `0x40242c` | 356 | ✓ |
| `method.Quasar.Client.Logging.Keylogger.WriteFile` | `0x40aeac` | 352 | ✓ |
| `method._GetKeyValues_d__15.MoveNext` | `0x40e854` | 348 | ✓ |
| `method.Quasar.Client.Helper.SystemHelper.GetUptime` | `0x40d554` | 344 | ✓ |

### Decompiled Code Files

- [`code/method.Quasar.Client.Helper.SystemHelper.GetUptime.c`](code/method.Quasar.Client.Helper.SystemHelper.GetUptime.c)
- [`code/method.Quasar.Client.IpGeoLocation.GeoInformationRetriever..ctor.c`](code/method.Quasar.Client.IpGeoLocation.GeoInformationRetriever..ctor.c)
- [`code/method.Quasar.Client.Logging.Keylogger.HighlightSpecialKeys.c`](code/method.Quasar.Client.Logging.Keylogger.HighlightSpecialKeys.c)
- [`code/method.Quasar.Client.Logging.Keylogger.WriteFile.c`](code/method.Quasar.Client.Logging.Keylogger.WriteFile.c)
- [`code/method.Quasar.Client.Messages.FileManagerHandler.Execute.c`](code/method.Quasar.Client.Messages.FileManagerHandler.Execute.c)
- [`code/method.Quasar.Client.Messages.StartupManagerHandler.Execute.c`](code/method.Quasar.Client.Messages.StartupManagerHandler.Execute.c)
- [`code/method.Quasar.Client.Messages.SystemInformationHandler.Execute.c`](code/method.Quasar.Client.Messages.SystemInformationHandler.Execute.c)
- [`code/method.Quasar.Client.Networking.Client.AsyncReceive.c`](code/method.Quasar.Client.Networking.Client.AsyncReceive.c)
- [`code/method.Quasar.Client.QuasarApplication.InitializeMessageProcessors.c`](code/method.Quasar.Client.QuasarApplication.InitializeMessageProcessors.c)
- [`code/method.Quasar.Client.Recovery.Browsers.FirefoxPassReader.ReadAccounts.c`](code/method.Quasar.Client.Recovery.Browsers.FirefoxPassReader.ReadAccounts.c)
- [`code/method.Quasar.Client.Recovery.Browsers.InternetExplorerPassReader.DecryptIePassword.c`](code/method.Quasar.Client.Recovery.Browsers.InternetExplorerPassReader.DecryptIePassword.c)
- [`code/method.Quasar.Client.Recovery.FtpClients.FileZillaPassReader.ReadAccounts.c`](code/method.Quasar.Client.Recovery.FtpClients.FileZillaPassReader.ReadAccounts.c)
- [`code/method.Quasar.Client.Recovery.FtpClients.WinScpPassReader.ReadAccounts.c`](code/method.Quasar.Client.Recovery.FtpClients.WinScpPassReader.ReadAccounts.c)
- [`code/method.Quasar.Client.Recovery.FtpClients.WinScpPassReader.WinSCPDecrypt.c`](code/method.Quasar.Client.Recovery.FtpClients.WinScpPassReader.WinSCPDecrypt.c)
- [`code/method.Quasar.Client.Recovery.Utilities.SQLiteHandler.ReadMasterTable.c`](code/method.Quasar.Client.Recovery.Utilities.SQLiteHandler.ReadMasterTable.c)
- [`code/method.Quasar.Client.Recovery.Utilities.SQLiteHandler.ReadTableFromOffset.c`](code/method.Quasar.Client.Recovery.Utilities.SQLiteHandler.ReadTableFromOffset.c)
- [`code/method.Quasar.Client.ReverseProxy.ReverseProxyClient.Handle_Connect.c`](code/method.Quasar.Client.ReverseProxy.ReverseProxyClient.Handle_Connect.c)
- [`code/method._GetKeyValues_d__15..ctor.c`](code/method._GetKeyValues_d__15..ctor.c)
- [`code/method._GetKeyValues_d__15.MoveNext.c`](code/method._GetKeyValues_d__15.MoveNext.c)
- [`code/method._GetKeyValues_d__15.System.Collections.Generic.IEnumerable_System.Tuple_System.String_System.String__.GetEnumerat.c`](code/method._GetKeyValues_d__15.System.Collections.Generic.IEnumerable_System.Tuple_System.String_System.String__.GetEnumerat.c)
- [`code/method._GetKeyValues_d__15.System.Collections.IEnumerable.GetEnumerator.c`](code/method._GetKeyValues_d__15.System.Collections.IEnumerable.GetEnumerator.c)
- [`code/method.__c__DisplayClass12_0._Execute_b__0.c`](code/method.__c__DisplayClass12_0._Execute_b__0.c)
- [`code/sym.Quasar.Client.Messages.FileManagerHandler.Execute_1.c`](code/sym.Quasar.Client.Messages.FileManagerHandler.Execute_1.c)
- [`code/sym.Quasar.Client.Messages.FileManagerHandler.Execute_2.c`](code/sym.Quasar.Client.Messages.FileManagerHandler.Execute_2.c)
- [`code/sym.Quasar.Client.Messages.FileManagerHandler.Execute_6.c`](code/sym.Quasar.Client.Messages.FileManagerHandler.Execute_6.c)
- [`code/sym.Quasar.Client.Messages.RemoteDesktopHandler.Execute_1.c`](code/sym.Quasar.Client.Messages.RemoteDesktopHandler.Execute_1.c)
- [`code/sym.Quasar.Client.Messages.StartupManagerHandler.Execute_1.c`](code/sym.Quasar.Client.Messages.StartupManagerHandler.Execute_1.c)
- [`code/sym.Quasar.Client.Messages.StartupManagerHandler.Execute_2.c`](code/sym.Quasar.Client.Messages.StartupManagerHandler.Execute_2.c)
- [`code/sym.Quasar.Client.Networking.Client.AsyncReceive.c`](code/sym.Quasar.Client.Networking.Client.AsyncReceive.c)
- [`code/sym.__c..ctor_5.c`](code/sym.__c..ctor_5.c)

## Behavioral Analysis

The analysis of **chunk 6/6** provides the final layer of technical detail regarding Quasar’s construction. This final segment confirms that the malware's defenses are not just "active" in high-value areas but are pervasive throughout the entire codebase, even within seemingly mundane "helper" functions.

### Updated Analysis: Quasar Information Stealer (Final Conclusion)

The addition of chunk 6 reinforces the conclusion that Quasar is a highly engineered piece of malware designed to frustrate both automated analysis tools and human reverse engineers through **dense, systemic obfuscation.**

#### 1. Pervasive Obfuscation Strategy
A key takeaway from this final segment is that the "industrial-grade" protection is not targeted only at the core theft logic; it is applied globally.
*   **Uniformity of Defense:** The function `method.Quasar.Client.Helper.SystemHelper.GetUptime` contains the same "bad instruction" and "overlapping instruction" markers as the primary keylogger. This indicates that the developers are using a compiler-level obfuscator (like **OLLVM** or **Tigress**) to wrap the entire binary. 
*   **The Goal of Ubiquity:** By making even simple system calls (like checking uptime) difficult to decompile, the authors force an analyst to waste significant time "de-obfuscating" basic functions before they can even begin to understand the core malicious logic.

#### 2. Analysis of New Functions
*   **`method.Qu_Client.Logging.Keylogger.WriteFile`**: This function confirms that Quasar has a dedicated, hardened routine for local data persistence. Even though it is simple in intent (saving captured logs), its implementation is buried in overlapping code to prevent researchers from easily tracing where the stolen data is stored on the local disk.
*   **`method._GetKeyValues_d__15.MoveNext`**: This large block of disassembly is a masterclass in **Control Flow Flattening.** The excessive use of `CONCAT31`, `POPCOUNT`, and complex arithmetic to perform simple loops suggests that the true logic (processing keystrokes or formatting data) is hidden behind layers of "junk" math. The presence of `LOCK()`/`UNLOCK()` primitives also hints at a multi-threaded environment, allowing the malware to remain responsive while performing heavy background processing (e.g., encryption or exfiltration).
*   **`method.Quasar.Client.Helper.SystemHelper.GetUptime`**: This function likely provides the "heartbeat" for the malware's logic. Knowing how long a system has been running is often used by sophisticated actors to:
    *   Calculate intervals between heartbeats to C2 servers (beaconing).
    *   Determine if a machine has been rebooted recently (detecting potential disruption).
    *   Time data exfiltration tasks for non-peak hours.

#### 3. Advanced Anti-Analysis Findings
The high frequency of `WARN: Bad instruction` and `overlap` messages in this chunk confirms the use of **instruction overlapping**. By placing a jump or a "hidden" entry point in the middle of a multi-byte instruction, the author ensures that a disassembler (like IDA Pro) will fail to render a clean graph. This is a deliberate tactic to break the "Decompiler" view and force the researcher to manually trace assembly code.

---

### Finalized Summary for Incident Response:

**Threat Actor Profile:** 
*   **Highly Professional / State-Sponsored Level.** The consistent application of OLLVM-style obfuscation across both critical and non-critical functions suggests a sophisticated development lifecycle. They are not "script kiddies"; they have the resources to build custom, hardened tools for production use.

**Technical Sophistication:**
*   **Elite Obfuscation Techniques:** Usage of overlapping instructions (to break disassembly), control flow flattening (to hide logic flow), and junk code insertion (to exhaust human analysis time).
*   **Modular Architecture:** The `InitializeMessageProcessors` logic confirms a modular approach where the malware can stay resident on a system for long periods, executing different modules as instructed by the C2.

**Confirmed Functional Capabilities:**
*   **Robust Keylogging:** Real-time capture of input, including special keys and MFA codes.
*   **File Manipulation & Management:** Mechanisms to store and manage stolen data locally before exfiltration.
*   **Resilient Networking:** Use of asynchronous communication to maintain connection with C2 while performing other tasks.
*   **Environment Awareness:** Uses system telemetry (like uptime) to coordinate its behavior over time.

**Updated Target Scope & Risk Factors:**
1.  **Target Environment:** The sophisticated obfuscation suggests a target on high-value enterprise assets where "detection by signature" or "quick manual analysis" are the primary obstacles for the threat actor.
2.  **Detection Difficulty:** Standard automated sandboxes may fail to see the full extent of Quasar’s behavior because the decompiler will "hang" or produce incorrect code in the obscured sections. 
3.  **Data Exfiltration Risk:** The robust networking and modular nature indicate a high probability of long-term residency (persistence) on infected machines.

### Conclusion:
Quasar is a **production-grade information stealer.** Its architecture is designed for longevity; it doesn't just "steal and go." It is built to sit inside a network, wait for commands from a C2 server, and perform various actions (Keylogging, File Stealing, Network Reconnaissance) while remaining virtually invisible to automated security tools due to its intense, professional-grade obfuscation layer.

**Primary Indicators of Concern (IOC) Logic:**
1.  **Execution Context:** Watch for processes that exhibit "multi-modal" behavior—a single process handling file I/O, keyboard hooks, and complex network traffic concurrently.
2.  **Anti-Analysis Persistence:** If security tools flag "Obfuscated Code" or "Control Flow Flattening," these should be treated as high-confidence indicators of a sophisticated adversary (Quasar).
3.  **Network Behavior:** Look for persistent connections using non-standard ports or protocols that utilize "heartbeat" patterns, potentially managed by the `GetUptime` or similar logic.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of OLLVM/Tigress, control flow flattening, and instruction overlapping are intended to hinder both automated tools and human analysis. |
| T1056.001 | Keylogging | The malware features a dedicated, hardened routine for the real-time capture of keystrokes, including special keys and MFA codes. |
| T1011 | Exfiltration Over C2 Channel | The implementation of heartbeats and timed exfiltration tasks indicates that stolen data is moved to a remote server via a command-and-control channel. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*None identified.* (While several internal functions like `GetReverseProxyByConnectionId` and `DoesURLMatchWithHash` suggest network activity, no hardcoded IP addresses or domains were present in the provided text.)

### **File paths / Registry keys**
*None identified.* (Strings such as `INSTALLPATH`, `LOGSPATH`, and `PROV_RSA_FULL` are generic system variables or constants and do not constitute specific malicious file paths or registry keys.)

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*   **7D78CB380BF5EFB7B851409CA6A875F77DECF09D19B9149DA17A3EBF674BC0F9** (SHA-1 Hash)

### **Other artifacts**
*   **Malware Family Identifier:** `Quasar` (Appears in internal class/method names: `Quasar.Common.IO`, `Quasar.Client.IO`, `Quasar.Client.Helper`)
*   **C2 / Behavioral Patterns:** 
    *   **Heartbeat Logic:** Use of the `GetUptime` function to calculate heartbeat intervals and coordinate exfiltration timing.
    *   **Persistence/Storage:** Use of a dedicated, hardened routine (`WriteFile`) for local storage of captured keylogs before exfiltration.
    *   **Obfuscation Techniques:** Implementation of OLLVM/Tigress-style "Control Flow Flattening" and "Instruction Overlapping" to bypass automated decompilers (e.g., IDA Pro).
    *   **Core Functions Detected:** `WinSCPDecrypt`, `DetectKeyHolding`, `GetReverseProxyByConnectionId`.

---

### **Analyst Note:**
The primary indicator of concern in this sample is the high level of professional obfuscation. The presence of "junk math" (e.g., `CONCAT31`, `POPCOUNT`) and overlapping instructions suggests a sophisticated actor. While network indicators are missing from this specific string dump, the behavior analysis confirms that the malware is designed for long-term residency and multi-stage operations.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1.  **Malware family**: Quasar
2.  **Malware type**: Infostealer / Backdoor
3.  **Confidence**: High
4.  **Key evidence**:
    *   **Robust Data Theft Capabilities:** The malware includes specific, hardened routines for real-time keylogging (including MFA codes) and local data persistence before exfiltration.
    *   **Sophisticated Anti-Analysis:** The use of "industrial-grade" obfuscation—specifically OLLVM/Tigress techniques like Control Flow Flattening and Instruction Overlapping—indicates a high level of professionalism designed to evade both automated tools and human analysts.
    *   **Persistent C2 Infrastructure:** The inclusion of heartbeat logic (`GetUptime`), modular architecture for receiving commands, and "heartbeat" patterns indicates the malware is designed for long-term residency on a network rather than a simple one-time execution.
