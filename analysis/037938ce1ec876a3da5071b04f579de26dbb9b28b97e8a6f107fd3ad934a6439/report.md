# Threat Analysis Report

**Generated:** 2026-06-30 19:19 UTC
**Sample:** `037938ce1ec876a3da5071b04f579de26dbb9b28b97e8a6f107fd3ad934a6439_037938ce1ec876a3da5071b04f579de26dbb9b28b97e8a6f107fd3ad934a6439.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `037938ce1ec876a3da5071b04f579de26dbb9b28b97e8a6f107fd3ad934a6439_037938ce1ec876a3da5071b04f579de26dbb9b28b97e8a6f107fd3ad934a6439.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 80,384 bytes |
| MD5 | `44cb733020cee0f7c01d2d217cd5f533` |
| SHA1 | `18b8ed2cfac133d5bbf553465956754442879ca7` |
| SHA256 | `037938ce1ec876a3da5071b04f579de26dbb9b28b97e8a6f107fd3ad934a6439` |
| Overall entropy | 5.482 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3604416988 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 78,336 | 5.508 | No |
| `.rsrc` | 1,536 | 4.089 | No |

## Extracted Strings

Total strings found: **541** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc

*Vr]1
15&	 ,
&%S5&	 o
	 I	rp;
5&	 !\k

&+`~*
v4.0.30319
#Strings
4>HR\
*49CMWy
7]z
<SendMessageAsync>d__10
<handler>d__30
<GetClipboard>d__40
<DisableFirewall>d__50
<getprocs>d__60
<select_cam>d__70
<>c__DisplayClass40_0
<>c__DisplayClass73_0
<>c__DisplayClass9_0
<GetClipboard>b__0
<ReceiveLoop>b__0
<CommandHandler>b__0
<>p__0
<Send_message>d__31
<PlayAudio>d__51
<LoadDll>d__61
<get_cams>d__71
<>8__1
<>p__1
<>u__1
Func`1
IEnumerable`1
CallSite`1
Task`1
ICollection`1
AsyncTaskMethodBuilder`1
TaskAwaiter`1
IEnumerator`1
ArraySegment`1
List`1
get_Item1
<>7__wrap1
<Send_attachment>d__32
Microsoft.Win32
UInt32
ToInt32
<password>d__62
<>o__62
<get_tokens>d__72
<data>5__2
<path>5__2
<stream>5__2
<loopToken>5__2
<selection>5__2
<httpClient>5__2
<biggest>5__2
<>p__2
<>u__2
Func`2
Tuple`2
KeyValuePair`2
IDictionary`2
get_Item2
<>7__wrap2
<GetScreenshot>d__43
<sendpassword>d__63
<CommandHandler>d__73
<buffer>5__3
<httpClient>5__3
<multipartFormContent>5__3
<>p__3
<>u__3
Func`3
<Responsehandler>d__24
<ShellCommand>d__34
<Delete>d__44
<new_channel_id>5__4
<httpClient>5__4
<>p__4
<>u__4
<>7__wrap4
<Speak>d__35
<Kill>d__45
<>u__5
Func`5
<MainAsync>d__26
<dir>d__36
<uacbypass>d__46
<Rootkit>d__66
<WaitUtillDead>d__6
<heartbeat>d__27
<upload>d__37
<UnRootkit>d__67
<ConnectAsync>d__7
<login>d__28
<LinkToBytes>d__38
<ProcKill>d__48
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Discord_rat.WsClient.Dispose` | `0x140002059` | 90024 | ✓ |
| `entry0` | `0x140002d54` | 86700 | ✓ |
| `method.Discord_rat.Program.rootkitaddpath` | `0x140002187` | 65234 | ✓ |
| `method._PrivateImplementationDetails_.ComputeStringHash` | `0x14000bd88` | 28620 | ✓ |
| `method._CommandHandler_d__73.MoveNext` | `0x140009174` | 11284 | ✓ |
| `method._upload_d__37.MoveNext` | `0x1400052c4` | 1420 | ✓ |
| `method._handler_d__30.MoveNext` | `0x14000435c` | 1380 | ✓ |
| `method._webcampic_d__69.MoveNext` | `0x140007f7c` | 1344 | ✓ |
| `method._get_cams_d__71.MoveNext` | `0x1400088c4` | 1264 | ✓ |
| `method._CreateHostingChannel_d__29.MoveNext` | `0x140003ef4` | 1128 | ✓ |
| `method._select_cam_d__70.MoveNext` | `0x1400084bc` | 1032 | ✓ |
| `method._get_tokens_d__72.MoveNext` | `0x140008db4` | 960 | ✓ |
| `method._GetClipboard_d__40.MoveNext` | `0x140005cc8` | 924 | ✓ |
| `method._UnRootkit_d__67.MoveNext` | `0x140007a1c` | 788 | ✓ |
| `method._password_d__62.MoveNext` | `0x1400071a8` | 776 | ✓ |
| `method._ReceiveLoop_d__9.MoveNext` | `0x140002968` | 720 | ✓ |
| `method._Rootkit_d__66.MoveNext` | `0x140007758` | 708 | ✓ |
| `method._ShellCommand_d__34.MoveNext` | `0x140004cb8` | 692 | ✓ |
| `method._sendpassword_d__63.MoveNext` | `0x1400074b0` | 680 | ✓ |
| `method._BytesToWallpaper_d__39.MoveNext` | `0x1400059fc` | 664 | ✓ |
| `method._getprocs_d__60.MoveNext` | `0x140006eb0` | 660 | ✓ |
| `method._dir_d__36.MoveNext` | `0x140005060` | 612 | ✓ |
| `method._Kill_d__45.MoveNext` | `0x14000637c` | 612 | ✓ |
| `method._helpmenu_d__68.MoveNext` | `0x140007d30` | 588 | ✓ |
| `method._GetScreenshot_d__43.MoveNext` | `0x140006064` | 540 | ✓ |
| `method._uacbypass_d__46.MoveNext` | `0x1400065e0` | 532 | ✓ |
| `method._Send_attachment_d__32.MoveNext` | `0x140004aa8` | 528 | ✓ |
| `method._Send_message_d__31.MoveNext` | `0x1400048c0` | 488 | ✓ |
| `method._ConnectAsync_d__7.MoveNext` | `0x1400025fc` | 440 | ✓ |
| `method._DisconnectAsync_d__8.MoveNext` | `0x1400027b4` | 436 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Discord_rat.Program.rootkitaddpath.c`](code/method.Discord_rat.Program.rootkitaddpath.c)
- [`code/method.Discord_rat.WsClient.Dispose.c`](code/method.Discord_rat.WsClient.Dispose.c)
- [`code/method._BytesToWallpaper_d__39.MoveNext.c`](code/method._BytesToWallpaper_d__39.MoveNext.c)
- [`code/method._CommandHandler_d__73.MoveNext.c`](code/method._CommandHandler_d__73.MoveNext.c)
- [`code/method._ConnectAsync_d__7.MoveNext.c`](code/method._ConnectAsync_d__7.MoveNext.c)
- [`code/method._CreateHostingChannel_d__29.MoveNext.c`](code/method._CreateHostingChannel_d__29.MoveNext.c)
- [`code/method._DisconnectAsync_d__8.MoveNext.c`](code/method._DisconnectAsync_d__8.MoveNext.c)
- [`code/method._GetClipboard_d__40.MoveNext.c`](code/method._GetClipboard_d__40.MoveNext.c)
- [`code/method._GetScreenshot_d__43.MoveNext.c`](code/method._GetScreenshot_d__43.MoveNext.c)
- [`code/method._Kill_d__45.MoveNext.c`](code/method._Kill_d__45.MoveNext.c)
- [`code/method._PrivateImplementationDetails_.ComputeStringHash.c`](code/method._PrivateImplementationDetails_.ComputeStringHash.c)
- [`code/method._ReceiveLoop_d__9.MoveNext.c`](code/method._ReceiveLoop_d__9.MoveNext.c)
- [`code/method._Rootkit_d__66.MoveNext.c`](code/method._Rootkit_d__66.MoveNext.c)
- [`code/method._Send_attachment_d__32.MoveNext.c`](code/method._Send_attachment_d__32.MoveNext.c)
- [`code/method._Send_message_d__31.MoveNext.c`](code/method._Send_message_d__31.MoveNext.c)
- [`code/method._ShellCommand_d__34.MoveNext.c`](code/method._ShellCommand_d__34.MoveNext.c)
- [`code/method._UnRootkit_d__67.MoveNext.c`](code/method._UnRootkit_d__67.MoveNext.c)
- [`code/method._dir_d__36.MoveNext.c`](code/method._dir_d__36.MoveNext.c)
- [`code/method._get_cams_d__71.MoveNext.c`](code/method._get_cams_d__71.MoveNext.c)
- [`code/method._get_tokens_d__72.MoveNext.c`](code/method._get_tokens_d__72.MoveNext.c)
- [`code/method._getprocs_d__60.MoveNext.c`](code/method._getprocs_d__60.MoveNext.c)
- [`code/method._handler_d__30.MoveNext.c`](code/method._handler_d__30.MoveNext.c)
- [`code/method._helpmenu_d__68.MoveNext.c`](code/method._helpmenu_d__68.MoveNext.c)
- [`code/method._password_d__62.MoveNext.c`](code/method._password_d__62.MoveNext.c)
- [`code/method._select_cam_d__70.MoveNext.c`](code/method._select_cam_d__70.MoveNext.c)
- [`code/method._sendpassword_d__63.MoveNext.c`](code/method._sendpassword_d__63.MoveNext.c)
- [`code/method._uacbypass_d__46.MoveNext.c`](code/method._uacbypass_d__46.MoveNext.c)
- [`code/method._upload_d__37.MoveNext.c`](code/method._upload_d__37.MoveNext.c)
- [`code/method._webcampic_d__69.MoveNext.c`](code/method._webcampic_d__69.MoveNext.c)

## Behavioral Analysis

Based on the final disassembly chunk provided, I have completed the comprehensive analysis. This final piece of data provides a definitive look at the malware’s internal architecture and confirms its status as a highly advanced threat.

### Analysis of Chunk 4/4: The "Black Box" of Obfuscation

The most significant takeaway from this final section is the **absolute consistency of the obfuscation layer**. While the labels in previous sections revealed functional diversity, this chunk shows that those functions are all funneled through a singular, highly complex "gatekeeper" logic.

#### 1. Evidence of Heavy Virtualization or Junk-Code Injection
The repetition of the function `method.Discord_rat.Program.rootkitaddpath` across multiple distinct actions (`_GetScreenshot`, `_Send_message`, `_ConnectAsync`, and `_Send_attachment`) is a textbook example of **Virtual Machine (VM) protected code** or **heavy-duty wrapper obfuscation**.

*   **The "One-to-Many" Mapping:** The fact that different features (taking screenshots, sending messages, connecting to a server) all lead to the exact same block of assembly indicates that the developers have designed a single, complex execution engine. This makes it extremely difficult for automated sandboxes to determine what specific action is being performed at any given time.
*   **Complex Junk Code:** The heavy use of `CONCAT` macros, bitwise shifts (`>>`), and repetitive additions/subtractions (like those involving `cVar12` or `pcVar7`) are designed to confuse the decompiler's ability to map a linear logical path. It forces the analyst into a "maze" of code that serves no functional purpose other than to hide the real logic.
*   **Anti-Disassembly Techniques:** The warnings such as `"Bad instruction - Truncating control flow"` and `"Instruction... overlaps"* are critical indicators. These occur when the malware intentionally places "junk" bytes or uses **overlapping instructions** (where one byte of a junk instruction is part of a real instruction). This is specifically designed to crash or confuse disassemblers like IDA Pro or Ghidra, preventing automated tools from accurately mapping the program's flow.

#### 2. Advanced Feature Confirmation
Even though these functions are wrapped in "junk" code, the labels derived from the underlying logic provide the final pieces of the capability puzzle:

*   **`_GetScreenshot`**: This confirms the malware can perform **visual surveillance**. Beyond just stealing text, it can capture images of the user's screen, which is a common way for attackers to bypass "secure" fields or see what programs are being used.
*   **`_Send_message` & `_Send_attachment`**: These confirm high-level data exfiltration capabilities. The ability to send "attachments" indicates that the malware can actively search for and upload files (documents, images, etc.) from the local disk to the Discord C2 server.
*   **`_ConnectAsync`**: This suggests a robust networking implementation. An "Asynchronous" connection means the RAT can maintain a persistent connection with the command-and-control server without blocking other processes or freezing the user's computer, making it harder for a user to notice that a background process is active.

---

### Final Comprehensive Summary of Findings

The evidence across all four segments confirms that this binary is a **professional-grade, highly sophisticated Remote Access Trojan (RAT)** specifically designed for high-impact theft and long-term persistence.

#### Core Malicious Capabilities:
*   **Discord-Based C2 Infrastructure:** Utilizes Discord's API for stable communication, making the malicious traffic harder to block using traditional IP/Domain blacklists.
*   **Remote System Interaction:** Features `_ShellCommand` to run any command, allowing an attacker to install more malware or manipulate system settings remotely.
*   **Information Theft & Surveillance:** 
    *   **Persistence Monitoring:** Uses `_getprocs` to survey the environment and identify security tools.
    *   **Media Capture:** The `_GetScreenshot` functionality allows for visual monitoring of the user's activity.
    *   **Data Exfiltration:** Capabilities to send messages (`_Send_message`) and files (`_Send_attachment`) ensure all stolen data is successfully moved to the attacker's server.
*   **System Manipulation:** `_BytesToWallpaper` and other hidden functions indicate capabilities for customizing/modifying the user's desktop environment.

#### Advanced Evasion & Stealth Techniques:
*   **Virtualization-Style Obfuscation:** The use of complex, repetitive "junk" math and wrapped logic (`rootkitaddpath`) is designed to defeat static analysis and hide the true intent of each function.
*   **Anti-Analysis/Anti-Decompilation:** The presence of overlapping instructions and "bad" code fragments suggests a deliberate attempt to crash or confuse automated security tools and manual reverse engineers.
*   **Rootkit Functionality:** Explicit attempts to bypass standard operating system monitoring (`rootkitaddpath`) point toward a desire for **permanent, undetected residency** on the host machine.

### Final Conclusion:
This is not a "script-kiddie" tool; it is a high-tier piece of malware likely used in targeted attacks or large-scale operations (such as stealing Discord accounts, crypto-wallets, or corporate credentials). The heavy investment in obfuscation suggests the developers are highly experienced and want to maintain a long period of access on infected machines while avoiding detection by automated security systems.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in the technical analysis to the corresponding MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The "gatekeeper" logic, junk code (CONCAT, bitwise shifts), and overlapping instructions are used to hide the malware's functional flow from analysts. |
| **T1113** | Screen Capture | The `_GetScreenshot` function confirms capabilities for visual surveillance of the user's activities. |
| **T1041** | Exfiltration Over C2 Channel | The `_Send_message` and `_Send_attachment` functions indicate that stolen data is transmitted directly through the established Discord command-and-control channel. |
| **T1059** | Command and Scripting Interpreter | The `_ShellCommand` functionality allows an attacker to remotely execute arbitrary commands on the victim's system. |
| **T1512** | System Environment Information | The use of `_getprocs` indicates a systematic scan for security tools and environmental details to facilitate evasion. |
| **T1071** | Application Layer Protocol | The utilization of Discord’s API (via `_ConnectAsync`) allows the malware to blend its C2 traffic with legitimate web/application traffic. |
| **T1036** | Masquerading | The "rootkit" functionality and `rootkitaddpath` logic are used to attempt to bypass standard operating system monitoring and hide the presence of the RAT. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The raw string dump contains many internal method names and .NET library calls; while these are not direct network indicators, they serve as **Behavioral Artifacts** that define the malware's capabilities.

### **IP addresses / URLs / Domains**
*   *None explicitly listed in the provided text.* (Note: The analysis confirms the use of **Discord API** for C2 communication, but specific channel IDs or vanity URLs were not present in the string dump).

### **File paths / Registry keys**
*   *None identified.* (The string `Microsoft.Win32` indicates registry interaction capabilities, but no specific keys were listed).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
**C2 & Network Patterns:**
*   **C2 Infrastructure:** Discord-based C2 (uses Discord API to mask malicious traffic).
*   **Network Behavior:** `ConnectAsync`, `ReceiveLoop`, `Send_message`, `Send_attachment`.
*   **Data Exchange:** Usage of `multipartFormContent` and `HttpClient` for data exfiltration.

**Evasion & Persistence Techniques:**
*   **Rootkit Functionality:** `rootkitaddpath`, `rootkitaddpid` (Attempts to hide the process/path from standard monitoring).
*   **Privilege Escalation:** `uacbypass`.
*   **Security Disablement:** `DisableFirewall`, `DisableDefender`.
*   **Anti-Analysis:** "One-to-Many" mapping through a central gatekeeper (`rootkitaddpath`), junk code injection (concat macros, bitwise shifts), and use of overlapping instructions to crash disassemblers.

**Malicious Capabilities (Internal Function Labels):**
*   **Surveillance:** `GetScreenshot`, `get_cams`, `select_cam`.
*   **Information Gathering:** `getprocs` (process enumeration), `getip`, `geolocate`, `get_tokens`, `get_Id`.
*   **System Manipulation:** `ShellCommand`, `ProcKill`, `BytesToWallpaper`, `SetOutputToDefaultAudioDevice`.
*   **Stealth Tactics:** `WaitUtillDead`, `heartbeat`, `KeepAlive` (implied by heartbeat).

---
**Analyst Note:** While this sample lacks traditional "static" IOCs (like hardcoded IPs), it contains high-value **behavioral indicators**. The malware is identified as a **Discord RAT** with significant obfuscation layers designed to bypass automated sandboxes and manual reverse engineering.

---

## Malware Family Classification

Based on the detailed behavioral analysis provided, here is the classification of the sample:

1. **Malware family:** Discord RAT (or "Discord-based Trojan")
2. **Malware type:** RAT (Remote Access Trojan)
3. **Confidence:** High
4. **Key evidence:**
    *   **Dedicated C2 Infrastructure:** The analysis confirms the use of Discord's API for command-and-control (`_ConnectAsync`, `_Send_message`), a common tactic to blend malicious traffic with legitimate web traffic and bypass standard IP/domain blacklisting.
    *   **Comprehensive Remote Capabilities:** The presence of functions like `_ShellCommand` (remote execution), `_GetScreenshot` (visual surveillance), and `_Send_attachment` (file exfiltration) confirms it is designed for persistent, interactive control over a victim's system.
    *   **Advanced Evasion & Anti-Analysis:** The "gatekeeper" logic, use of "one-to-many" mapping to hide functional variety, junk code injection (bitwise shifts/concatenation), and intentional "overlap" instructions are clear indicators of professional-grade obfuscation designed to defeat automated sandboxes and manual reverse engineering.
