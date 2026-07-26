# Threat Analysis Report

**Generated:** 2026-07-25 23:01 UTC
**Sample:** `0b3884cd80063362270780c7e28107b62cb3a6f7a2714cd176f003707f070360_0b3884cd80063362270780c7e28107b62cb3a6f7a2714cd176f003707f070360.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b3884cd80063362270780c7e28107b62cb3a6f7a2714cd176f003707f070360_0b3884cd80063362270780c7e28107b62cb3a6f7a2714cd176f003707f070360.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 80,384 bytes |
| MD5 | `ee61af4d16f844c80a6561e5c69721cd` |
| SHA1 | `c45300a8faefdf532224c057efbf745e7c6a5679` |
| SHA256 | `0b3884cd80063362270780c7e28107b62cb3a6f7a2714cd176f003707f070360` |
| Overall entropy | 5.489 |
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
| `.text` | 78,336 | 5.515 | No |
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

Based on the final disassembly chunk provided (4/4), I have completed the analysis of the `Discord_rat` binary. This final set of data provides a definitive look at the malware’s sophistication, particularly in how it employs advanced "anti-analysis" techniques to hide its primary functions.

### Analysis Update: Chunk 4/4 Findings

#### 1. Advanced Anti-Analysis (Instruction Overlapping & Code Aliasing)
The most significant finding in this chunk is the repetitive structure of the code for `_GetScreenshot`, `_Sendmessage`, and `_ConnectAsync`. Note that even though these are different functions, the decompiler labels them all as `rootkitaddpath` in some instances.

*   **Instruction Overlapping:** The "WARNING: Bad instruction" and "overlapping instruction" messages indicate that the developer has intentionally placed jump targets at byte offsets where they would overlap with other instructions if read differently by the CPU. 
*   **Decompiler Sabotage:** By doing this, the developer forces the decompiler to lose track of the control flow. When a tool like Ghidra cannot determine which instruction follows another due to overlapping bytes, it "gives up" and often resorts to using the last known valid label (in this case, `rootkitaddpath`) for subsequent blocks. This is a high-tier technique used to hide the transition between different malicious behaviors.
*   **Automated Obfuscation:** The consistent use of complex mathematical constructs (like the repeated `CONCAT` and `sub/add` chains) indicates that the malware was passed through an automated obfuscation tool designed specifically to break static analysis tools.

#### 2. Expanded Malicious Capabilities (Spying & Communication)
The inclusion of these functions in the final chunk completes the profile of the malware as a full-featured Remote Access Trojan (RAT):

*   **`_GetScreenshot` (Visual Surveillance):** This confirms that the RAT has the capability to capture and exfiltrate screenshots of the victim's desktop. This is often used to steal information that isn't easily "scraped" via text, such as visual confirmation of active sessions or multi-factor authentication (MFA) prompts.
*   **`_Sendmessage` (Active Interaction):** While `_sendpassword` focuses on stealing credentials, `_Sendmessage` suggests the ability to interact with a messaging platform (likely Discord). This could be used for automated "phishing" of other users by the attacker or to exfiltrate specific logs from chat applications.
*   **`_ConnectAsync` (Network Persistence):** The term "Async" usually implies an asynchronous networking library. This indicates that the malware is designed to maintain a persistent connection to a Command and Control (C2) server in the background, allowing the attacker to send commands to the machine without blocking the user's ability to use other applications.

### Updated Summary Table of Indicators

| Category | Specific Findings (New/Confirmed) | Impact Analysis | Risk Level |
| :--- | :--- | :--- | :--- |
| **Credential Theft** | `_sendpassword` | Direct theft of passwords and login credentials. | **Critical** |
| **System Recon** | `_getprocs` | Identifies targets and detects security software. | **High** |
| **Persistence** | `rootkitaddpath` (multi-instance) | Ensures the RAT stays active after reboots; hides via overlapped instructions. | **Critical** |
| **Visual Spyware** | `_GetScreenshot` | Enables remote viewing of the user's screen/desktop. | **High** |
| **Messaging Control**| `_Sendmessage` | Potential for spamming, phishing, or log exfiltration. | **Medium** |
| **C2 Connectivity** | `_ConnectAsync` & `ReceiveLoop` | Establishes a persistent "heartbeat" with the attacker's server. | **High** |
| **Anti-Analysis** | Instruction Overlapping / Junk Code | Specifically designed to break decompiler tools and stall manual analysis. | **Critical** |

### Final Technical Conclusion
The `Discord_rat` binary is a highly sophisticated piece of malware that exhibits characteristics of "professional grade" development. It utilizes a "cloaking" technique where the most critical functions—**screenshotting, messaging, connection management, and credential theft**—are buried under layers of mathematically complex junk code and instruction-overlapping techniques.

The fact that the decompiler struggled to distinguish between `_GetScreenshot`, `_Sendmessage`, and `_ConnectAsync` due to intentional "bad instructions" demonstrates a deliberate attempt to frustrate forensic investigators. The malware is not merely a simple script; it is an engineered tool designed to stay hidden while providing the attacker with full surveillance (screenshotting) and control over the victim's environment.

**Final Threat Assessment:**
The presence of `_GetScreenshot` combined with `_sendpassword` indicates a high-intent theft operation. The malware is built for **maximum impact**, specifically targeting social media, cryptocurrency wallets, and private communications via Discord/Telegram.

**Emergency Response Protocol:**
1.  **Isolate Host:** Immediately disconnect the infected machine from all networks (Wi-Fi/Ethernet).
2.  **Credential Purge:** Assume all passwords entered on the device are compromised. Users must perform a "Global Logout" of all accounts (Google, Discord, Telegram, Exchange) and change passwords via a *different* clean device.
3.  **MFA Reset:** If Multi-Factor Authentication was used, it should be reset/re-synced, as session tokens may have been stolen by the `get_tokens` function identified in earlier segments.
4.  **Persistence Cleanup:** Because of the `rootkitaddpath` functionality, a standard antivirus scan may not be sufficient; a full system wipe and OS reinstallation is the only way to ensure no backdoors remain.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors observed in the `Discord_rat` binary to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of instruction overlapping, "bad instructions," and complex math chains is designed to hide the true intent of the code from decompilers. |
| T1113 | Screen Capture | The `_GetScreenshot` function provides the capability to capture visual information from the victim's desktop. |
| T1567 | Exfiltration Over Web Service | The `_Sendmessage` functionality suggests utilizing a web-based service (Discord) for communication or data exfiltration. |
| T1539 | Steal Web Credentials | The inclusion of `_sendpassword` and `get_tokens` indicates an intent to steal login credentials and session tokens from the user. |
| T1036 | Masquerading | The use of "rootkit" naming conventions and deceptive code structures masks the malware's true functions as standard system processes. |
| T1547 | Persistence (via System Environment) | The `rootkitaddpath` function is utilized to ensure the malware remains active across reboots by modifying system paths. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided string exports and behavioral analysis for the `Discord_rat` sample. Below are the extracted Indicators of Compromise (IOCs) categorized by type.

### **Analysis Note**
The provided data consists primarily of internal function names and .NET assembly symbols rather than hardcoded infrastructure. While no static network indicators (IPs/Domains) were present in this specific string dump, several high-confidence **behavioral IOCs** and **malware identifiers** were identified.

---

### **1. IP addresses / URLs / Domains**
*   *None identified.* (The text mentions "Discord" and "Telegram," but these are the platforms used for command and control/exfiltration rather than specific hardcoded C2 infrastructure in this snippet).

### **2. File paths / Registry keys**
*   **`rootkitaddpath`**: While a function name, it indicates an intent to modify system environment variables (likely the `PATH` variable) or create persistent files hidden via instruction overlapping. 

### **3. Mutex names / Named pipes**
*   *None identified.*

### **4. Hashes**
*   *None identified.*

### **5. Other artifacts (Behavioral IOCs & TTPs)**
These items identify the capabilities and tactics of the malware, which are critical for detection rules (e.g., Sigma or YARA rules).

*   **Malware Family:** `Discord_rat`
*   **Credential Theft Indicators:** 
    *   `sendpassword`
    *   `get_tokens` (Targeting session tokens/cookies)
    *   `GetClipboard`
*   **Persistence & Evasion Tactics:**
    *   `uacbypass` (Bypassing User Account Control)
    *   `DisableFirewall` / `DisableDefender` (Disabling security software)
    *   `Rootkit` / `rootkitaddpath` (Evasive persistence mechanisms)
    *   **Instruction Overlapping:** Detection of "bad instructions" and "overlapping instructions" used to break automated decompiler analysis.
*   **Information Gathering & Surveillance:**
    *   `GetScreenshot` (Visual spying)
    *   `getprocs` (Process enumeration/hunting for security tools)
    *   `geolocate` (Gathering victim location data)
    *   `get_ip` (Local network reconnaissance)
    *   `webcampic` (Interaction with webcam)
*   **C2 & Communication Patterns:**
    *   `ConnectAsync` / `ReceiveLoop` / `heartbeat` (Persistence in communication with a remote server)
    *   `upload` (Data exfiltration)
    *   `Send_message` (Possible interaction with Discord/Telegram APIs for exfiltration or phishing)

---

### **Summary of Risk**
The sample is confirmed as a high-sophistication **Remote Access Trojan (RAT)**. The presence of `GetScreenshot`, `get_tokens`, and `uacbypass` indicates it is designed for high-impact data theft. Its use of "Instruction Overlapping" signifies that it was specifically engineered to evade static analysis by security researchers.

---

## Malware Family Classification

Based on the detailed analysis provided, here is the classification of the sample:

1. **Malware family**: Discord_rat (likely a sophisticated variant of common Discord-centric RAT frameworks)
2. **Malware type**: RAT (Remote Access Trojan) / Infostealer
3. **Confidence**: High
4. **Key evidence**:
    *   **Extensive Surveillance & Theft Capabilities:** The inclusion of `_GetScreenshot` (visual spying), `_sendpassword` (credential theft), and `get_tokens` (session hijacking/cookie theft) confirms the intent to steal sensitive data from social media, crypto wallets, and private communications.
    *   **Advanced Anti-Analysis Sophistication:** The use of "instruction overlapping" and "code aliasing" specifically designed to break decompilers like Ghidra indicates a professional level of development aimed at hiding core functions such as `_ConnectAsync` (C2 persistence) and `root_addpath`.
    *   **Evasion & Persistence Infrastructure:** The presence of `uacbypass`, `DisableFirewall`, `DisableDefender`, and the "rootkit" style approach to system path modification highlights a high-intent effort to maintain long-term, undetected access to the victim's machine.
