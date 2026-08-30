# Threat Analysis Report

**Generated:** 2026-08-24 22:38 UTC
**Sample:** `11f7d56dc27f17aa6cb8951934c6f9bc3b9c8033c3d411995c61e349845e8905_11f7d56dc27f17aa6cb8951934c6f9bc3b9c8033c3d411995c61e349845e8905.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11f7d56dc27f17aa6cb8951934c6f9bc3b9c8033c3d411995c61e349845e8905_11f7d56dc27f17aa6cb8951934c6f9bc3b9c8033c3d411995c61e349845e8905.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 80,896 bytes |
| MD5 | `6b58a030b69a9e19760cfc030c3af25c` |
| SHA1 | `3f60b8ae077b4c1fbd721088481cd028ee3eda78` |
| SHA256 | `11f7d56dc27f17aa6cb8951934c6f9bc3b9c8033c3d411995c61e349845e8905` |
| Overall entropy | 5.526 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2532681047 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 78,848 | 5.552 | No |
| `.rsrc` | 1,536 | 4.094 | No |

## Extracted Strings

Total strings found: **543** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc

&+`~
v4.0.30319
#Strings
	u	J
~

<SendMessageAsync>d__10
<CreateHostingChannel>d__30
<BytesToWallpaper>d__40
<DisableDefender>d__50
<getip>d__60
<webcampic>d__70
<>c__DisplayClass41_0
<>c__DisplayClass74_0
<>c__DisplayClass9_0
<GetClipboard>b__0
<ReceiveLoop>b__0
<CommandHandler>b__0
<>p__0
<handler>d__31
<GetClipboard>d__41
<DisableFirewall>d__51
<getprocs>d__61
<select_cam>d__71
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
<Send_message>d__32
Microsoft.Win32
UInt32
ToInt32
<PlayAudio>d__52
<LoadDll>d__62
<get_cams>d__72
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
<Send_attachment>d__33
<password>d__63
<>o__63
<get_tokens>d__73
<buffer>5__3
<httpClient>5__3
<multipartFormContent>5__3
<>p__3
<>u__3
Func`3
<GetScreenshot>d__44
<sendpassword>d__64
<CommandHandler>d__74
<new_channel_id>5__4
<httpClient>5__4
<>p__4
<>u__4
<>7__wrap4
<Responsehandler>d__25
<ShellCommand>d__35
<Delete>d__45
<>u__5
Func`5
<Speak>d__36
<Kill>d__46
<WaitUtillDead>d__6
<MainAsync>d__27
<dir>d__37
<uacbypass>d__47
<Rootkit>d__67
<ConnectAsync>d__7
<heartbeat>d__28
<upload>d__38
<UnRootkit>d__68
get_UTF8
<DisconnectAsync>d__8
<login>d__29
<LinkToBytes>d__39
<ProcKill>d__49
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Discord_rat.WsClient.Dispose` | `0x1400021bf` | 89666 | ✓ |
| `entry0` | `0x1400022a8` | 89432 | ✓ |
| `method.__c__DisplayClass9_0._ReceiveLoop_b__0` | `0x140003059` | 61798 | ✓ |
| `method._webcampic_d__70.SetStateMachine` | `0x14000bda8` | 25856 | ✓ |
| `method._CommandHandler_d__74.MoveNext` | `0x140003b8c` | 11136 | ✓ |
| `method.Discord_rat.Program.StringToBytes` | `0x1400024bb` | 1476 | ✓ |
| `method._upload_d__38.MoveNext` | `0x14000b2d8` | 1408 | ✓ |
| `method._handler_d__31.MoveNext` | `0x140009c20` | 1380 | ✓ |
| `method._webcampic_d__70.MoveNext` | `0x14000b868` | 1344 | ✓ |
| `method._get_cams_d__72.MoveNext` | `0x140008f60` | 1264 | ✓ |
| `method._CreateHostingChannel_d__30.MoveNext` | `0x14000671c` | 1128 | ✓ |
| `method._select_cam_d__71.MoveNext` | `0x14000a9e4` | 1032 | ✓ |
| `method._get_tokens_d__73.MoveNext` | `0x140009460` | 960 | ✓ |
| `method._GetClipboard_d__41.MoveNext` | `0x140006f00` | 924 | ✓ |
| `method._UnRootkit_d__68.MoveNext` | `0x140008850` | 788 | ✓ |
| `method._password_d__63.MoveNext` | `0x14000a6cc` | 776 | ✓ |
| `method._ReceiveLoop_d__9.MoveNext` | `0x140003400` | 720 | ✓ |
| `method._Rootkit_d__67.MoveNext` | `0x140007d9c` | 708 | ✓ |
| `method._ShellCommand_d__35.MoveNext` | `0x140008488` | 692 | ✓ |
| `method._sendpassword_d__64.MoveNext` | `0x14000adfc` | 680 | ✓ |
| `method._getprocs_d__61.MoveNext` | `0x14000997c` | 660 | ✓ |
| `method._BytesToWallpaper_d__40.MoveNext` | `0x1400038f0` | 652 | ✓ |
| `method.Discord_rat.Program.JsonToDictionary` | `0x140002247` | 628 | ✓ |
| `method.Discord_rat.Program.addstartupnonadmin` | `0x140002a7f` | 612 | ✓ |
| `method._Kill_d__46.MoveNext` | `0x1400074d8` | 612 | ✓ |
| `method._dir_d__37.MoveNext` | `0x140008b74` | 612 | ✓ |
| `method.Discord_rat.Program.rootkitaddpath` | `0x140002d0b` | 596 | ✓ |
| `method._helpmenu_d__69.MoveNext` | `0x14000a310` | 588 | ✓ |
| `method._GetScreenshot_d__44.MoveNext` | `0x1400072ac` | 540 | ✓ |
| `method._uacbypass_d__47.MoveNext` | `0x14000b0b4` | 532 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Discord_rat.Program.JsonToDictionary.c`](code/method.Discord_rat.Program.JsonToDictionary.c)
- [`code/method.Discord_rat.Program.StringToBytes.c`](code/method.Discord_rat.Program.StringToBytes.c)
- [`code/method.Discord_rat.Program.addstartupnonadmin.c`](code/method.Discord_rat.Program.addstartupnonadmin.c)
- [`code/method.Discord_rat.Program.rootkitaddpath.c`](code/method.Discord_rat.Program.rootkitaddpath.c)
- [`code/method.Discord_rat.WsClient.Dispose.c`](code/method.Discord_rat.WsClient.Dispose.c)
- [`code/method._BytesToWallpaper_d__40.MoveNext.c`](code/method._BytesToWallpaper_d__40.MoveNext.c)
- [`code/method._CommandHandler_d__74.MoveNext.c`](code/method._CommandHandler_d__74.MoveNext.c)
- [`code/method._CreateHostingChannel_d__30.MoveNext.c`](code/method._CreateHostingChannel_d__30.MoveNext.c)
- [`code/method._GetClipboard_d__41.MoveNext.c`](code/method._GetClipboard_d__41.MoveNext.c)
- [`code/method._GetScreenshot_d__44.MoveNext.c`](code/method._GetScreenshot_d__44.MoveNext.c)
- [`code/method._Kill_d__46.MoveNext.c`](code/method._Kill_d__46.MoveNext.c)
- [`code/method._ReceiveLoop_d__9.MoveNext.c`](code/method._ReceiveLoop_d__9.MoveNext.c)
- [`code/method._Rootkit_d__67.MoveNext.c`](code/method._Rootkit_d__67.MoveNext.c)
- [`code/method._ShellCommand_d__35.MoveNext.c`](code/method._ShellCommand_d__35.MoveNext.c)
- [`code/method._UnRootkit_d__68.MoveNext.c`](code/method._UnRootkit_d__68.MoveNext.c)
- [`code/method.__c__DisplayClass9_0._ReceiveLoop_b__0.c`](code/method.__c__DisplayClass9_0._ReceiveLoop_b__0.c)
- [`code/method._dir_d__37.MoveNext.c`](code/method._dir_d__37.MoveNext.c)
- [`code/method._get_cams_d__72.MoveNext.c`](code/method._get_cams_d__72.MoveNext.c)
- [`code/method._get_tokens_d__73.MoveNext.c`](code/method._get_tokens_d__73.MoveNext.c)
- [`code/method._getprocs_d__61.MoveNext.c`](code/method._getprocs_d__61.MoveNext.c)
- [`code/method._handler_d__31.MoveNext.c`](code/method._handler_d__31.MoveNext.c)
- [`code/method._helpmenu_d__69.MoveNext.c`](code/method._helpmenu_d__69.MoveNext.c)
- [`code/method._password_d__63.MoveNext.c`](code/method._password_d__63.MoveNext.c)
- [`code/method._select_cam_d__71.MoveNext.c`](code/method._select_cam_d__71.MoveNext.c)
- [`code/method._sendpassword_d__64.MoveNext.c`](code/method._sendpassword_d__64.MoveNext.c)
- [`code/method._uacbypass_d__47.MoveNext.c`](code/method._uacbypass_d__47.MoveNext.c)
- [`code/method._upload_d__38.MoveNext.c`](code/method._upload_d__38.MoveNext.c)
- [`code/method._webcampic_d__70.MoveNext.c`](code/method._webcampic_d__70.MoveNext.c)
- [`code/method._webcampic_d__70.SetStateMachine.c`](code/method._webcampic_d__70.SetStateMachine.c)

## Behavioral Analysis

Based on my analysis of the provided strings and disassembly, this binary is a **Remote Access Trojan (RAT)** designed for surveillance, credential theft, and unauthorized remote control. The name `Discord_rat` in the code structure strongly suggests it uses Discord’s infrastructure or protocol for Command and Control (C2) communication.

### Core Functionality and Purpose
The primary purpose of this malware is to provide an attacker with a persistent "backdoor" into a victim's system. It is designed to:
*   **Exfiltrate sensitive information:** Specifically targeting credentials, location data, and personal environment details.
*   **Provide remote command execution:** Allowing the attacker to run arbitrary commands on the target machine via a shell.
*   **Conduct spying activities:** Monitoring what the user sees (screenshots) and doing (clipboard monitoring).

### Suspicious and Malicious Behaviors
The following malicious behaviors were identified:

*   **Information Theft & Surveillance:**
    *   **Clipboard Stealing (`GetClipboard`):** Likely used to capture passwords, cryptocurrency wallet addresses, or session tokens copied by the user.
    *   **Visual Spying (`GetScreenshot`, `get_cams`, `select_cam`):** The malware attempts to take screenshots of the desktop and interact with/activate the system's webcam.
    *   **Geolocation & Network Tracking (`getip`, `geolocate`):** Used to identify the victim's physical location and network environment.
    *   **Credential Exfiltration (`sendpassword`):** Explicitly attempts to send harvested passwords to a remote server.

*   **Persistence & Stealth:**
    *   **Rootkit Capabilities (`Rootkit`, `UnRootkit`):** Indicates features meant to hide files, processes, or network connections from the user and standard monitoring tools.
    *   **UAC Bypass (`uacbypass`):** A common technique used to gain administrative privileges without triggering a Windows User Account Control prompt.
    *   **Disabling Security Software:** Explicit functions for `DisableDefender` and `DisableFirewall` indicate an intent to neutralize system protections immediately upon infection.

*   **Command & Control (C2) Communication:**
    *   **Discord Integration:** The inclusion of Discord-related classes and methods suggests the malware communicates with a Discord server or uses Discord's API/WebSockets for relaying commands.
    *   **Remote Shell Execution (`ShellCommand`):** Allows the attacker to execute arbitrary system commands remotely.

### Notable Techniques & Patterns
*   **Anti-Analysis / Obfuscation:** The decompiler flagged numerous "bad instructions," "overlapping instructions," and "junk data" (e.g., `halt_baddata()`). This suggests the binary uses **control-flow flattening** or **junk code insertion** to hinder reverse engineering by automated tools.
*   **Evasion via Common Utilities:** By using Discord as a C2 channel, the malware may attempt to bypass network filters that only block "unknown" or non-standard IP addresses/ports, as it appears to be communicating with legitimate Discord infrastructure.
*   **Data Packaging:** The use of `JsonToDictionary` and `StringToBytes` suggests it organizes stolen data into structured formats (like JSON) before exfiltrating them via web requests (`httpClient`).

### Summary Table of Indicators
| Category | Observed Features / Strings | Severity |
| :--- | :--- | :--- |
| **Spying** | `GetScreenshot`, `get_cams`, `select_cam` | High |
| **Data Theft** | `GetClipboard`, `sendpassword`, `geolocate` | High |
| **Evasion** | `DisableDefender`, `DisableFirewall`, `uacbypass` | Critical |
| **Stealth** | `Rootkit`, `un_Risk`, `halt_baddata` (obfuscation) | High |
| **C2** | `Discord_rat`, `WebSocket`, `SendAsync` | High |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1056** | Input Capture | The use of `GetClipboard` indicates an intent to capture sensitive information like passwords or tokens from the system clipboard. |
| **T1114** | Screen Capture | Functions like `GetScreenshot`, `get_cams`, and `select_cam` are used for visual spying and monitoring user activity. |
| **T1082** | System Information Discovery | The `getip` and `geolocate` functions are used to gather environmental data about the victim's location and network. |
| **T1016** | System Network Configuration Discovery | The `getip` functionality specifically identifies the internal/external network configurations of the host. |
| **T1041** | Exfiltration Over C2 Channel | The `sendpassword` function indicates that stolen credentials are sent to a remote server via a command-and-control channel. |
| **T1014** | Rootkit | The presence of `Rootkit` and `UnRootkit` functions suggests the malware attempts to hide its files, processes, or network connections. |
| **T1548.002** | Bypass User Account Control | The `uacbypass` functionality is used to gain administrative privileges without triggering a Windows UAC prompt. |
| **T1562.001** | Impair Defenses: Disable or Remove Security Software | The `DisableDefender` and `DisableFirewall` functions are designed to neutralize system protections immediately upon infection. |
| **T1105** | Data Encoding | The use of `JsonToDictionary` and `StringToBytes` suggests a methodology for structuring/encoding data before transmission to evade detection. |
| **T1059** | Command and Scripting Interpreter | The `ShellCommand` functionality allows the attacker to execute arbitrary commands on the host via a remote shell. |
| **T1027** | Obfuscated Files or Information | The use of junk data, control-flow flattening, and "bad instructions" is intended to hinder reverse engineering and automated analysis. |

---

## Indicators of Compromise

Based on the strings provided and the accompanying behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Please note that because this analysis focuses on the **behavioral logic** and **function names** rather than specific configuration files or hardcoded infrastructure, there are no "hard" static IOCs (like specific IP addresses or MD5 hashes) present in the provided text.

### **IP addresses / URLs / Domains**
*   None found. (The analysis notes use of Discord infrastructure, but no specific malicious domains were listed).

### **File paths / Registry keys**
*   None found. (While functions like `Get_FileName` and `Get_Query` exist, no specific malicious paths or registry keys were identified).

### **Mutex names / Named pipes**
*   None found.

### **Hashes**
*   None found.

### **Other artifacts**
*   **C2 Infrastructure Patterns:** 
    *   Discord Infrastructure/WebSockets: The malware is identified as a "Discord_rat," utilizing Discord's API and WebSockets for C2 communication to bypass standard network filters.
    *   `SendAsync`, `ReceiveAsync`: Indicators of asynchronous networking for data exfiltration.
*   **Malware Identity:**
    *   `Discord_rat`: Identified as the core project/malware name within the code structure.
*   **Behavioral Signatures (TTPs):** 
    *   `uacbypass`: Technique used to escalate privileges.
    *   `DisableDefender` / `DisableFirewall`: Actions taken to neutralize endpoint security.
    *   `Rootkit` / `un_Risk` / `halt_baddata`: Indicators of anti-analysis and evasion techniques.
    *   `Get_Clipboard`, `GetScreenshot`, `get_cams`: Features indicating active spying and data theft capabilities.

---

## Malware Family Classification

1. **Malware family**: Discord_rat
2. **Malware type**: RAT (Remote Access Trojan)
3. **Confidence**: High

**Key evidence**:
*   **Explicit Functionality:** The malware contains numerous indicators of a Remote Access Trojan, including remote shell execution (`ShellCommand`), camera access (`get_cams`, `select_cam`), and screen capturing (`GetScreenshot`).
*   **Data Exfiltration & Stealing:** It features dedicated modules for stealing sensitive information, such as clipboard contents (`GetClipboard`) and credentials (`sendpassword`), combined with geolocation tracking.
*   **Advanced Evasion Tactics:** The sample incorporates multiple layers of defense evasion, including `uacbypass` to gain administrative privileges, functions to disable Windows Defender and Firewalls, and rootkit-like capabilities to hide its presence from the user.
