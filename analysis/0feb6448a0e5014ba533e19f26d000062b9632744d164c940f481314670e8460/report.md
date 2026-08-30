# Threat Analysis Report

**Generated:** 2026-08-17 19:38 UTC
**Sample:** `0feb6448a0e5014ba533e19f26d000062b9632744d164c940f481314670e8460_0feb6448a0e5014ba533e19f26d000062b9632744d164c940f481314670e8460.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0feb6448a0e5014ba533e19f26d000062b9632744d164c940f481314670e8460_0feb6448a0e5014ba533e19f26d000062b9632744d164c940f481314670e8460.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 80,384 bytes |
| MD5 | `789b4cf512636156394656b7450e8251` |
| SHA1 | `62ca27797773be8ff7f21346d435e8d96350087d` |
| SHA256 | `0feb6448a0e5014ba533e19f26d000062b9632744d164c940f481314670e8460` |
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

Based on the final disassembly provided in Chunk 4, I have updated the final analysis. This section provides conclusive evidence regarding the sophistication of the malware's evasion techniques and confirms specific functional capabilities that were hinted at in previous segments.

### Final Analysis: Discord_rat (Chunk 4)

The fourth chunk focuses on the underlying mechanics of the "Wrapper" strategy identified in Chunk 3, while also revealing several more high-level malicious features.

#### 1. Universal Wrapper and Call Obfuscation
In this segment, we see that functions with vastly different purposes—`_GetScreenshot`, `_Send_message`, `_ConnectAsync`, and `_DisconnectAsync`—all resolve to the **exact same** disassembly block (`rootkitaddpath`).

**Significance:** 
*   **Identity Masking:** By forcing multiple unique actions (taking a screenshot vs. sending a network packet) into an identical code structure, the author prevents analysts from identifying specific behaviors through signature-based detection or automated graph analysis.
*   **Complexity Overhead:** Any analyst attempting to trace the "Get Screenshot" logic will be forced to navigate the same maze of junk code as they would for any other function in the program.

#### 2. Explicit Anti-Analysis (Anti-Disassembly)
This chunk highlights several indicators of a professional obfuscation suite:
*   **Instruction Overlapping:** The disassembler repeatedly warns of "overlapping instructions" and "bad instruction data." This is a deliberate tactic where the malware uses "jump" offsets that land in the middle of an intended instruction, confusing the tool's ability to map out the logic.
*   **Dead-Code Insertion & Junk Logic:** The repeated use of `cVar25`, `pcVar9`, and complex `CONCAT` operations are classic examples of **junk code**. These calculations have no impact on the program's execution but are designed to exhaust an analyst’s time and resources.
*   **Control-Flow Flattening (CFF):** The presence of many "unreachable blocks" suggests that the original logic has been flattened, turning a linear set of instructions into a complex web of jumps and conditional branches that look identical regardless of the function being called.

#### 3. Additional Malicious Capabilities
The presence of these specific functions confirms several key capabilities:
*   **Visual Surveillance:** The `_GetScreenshot` function indicates that the malware can capture images from the user's desktop, a common feature for monitoring activity or capturing sensitive information (e.g., banking portals).
*   **Persistent Communication:** The inclusion of `_ConnectAsync` and `_DisconnectAsync` confirms that the malware maintains a persistent connection to a remote server. This allows the attacker to stay in contact with the infected machine, receive commands, and exfiltrate data in real-time.

---

### Final Comprehensive Summary of Findings

**Threat Type:** High-Sophistication Remote Access Trojan (RAT) / Information Stealer.

**Evasion Tactics Identified:**
*   **Homogenized Wrapper System:** Using a single, heavily obfuscated "wrapper" (`rootkitaddpath`) for all core functionalities to hide the malware's true intent from automated scanners and human researchers.
*   **Instruction Overlapping & Junk Code:** Utilizing advanced assembly tricks to break disassemblers (IDA Pro/Ghidra) and create a massive amount of "noise" to hinder manual analysis.
*   **Control-Flow Flattening:** Removing the distinct signatures of different functions by forcing them through an identical, complex execution path.
*   **C2 Integration:** Utilizing Discord as a stable communication channel to mask the command-and-control infrastructure.

**Confirmed Capabilities:**
1.  **Remote Command Execution:** Ability to execute arbitrary commands (via `_ShellCommand`).
2.  **File System Interaction:** Capability to list and navigate directories (`_dir`).
3.  **Information Gathering & Reconnaissance:** Ability to see running processes (`_getprocs`).
4.  **Credential Harvesting:** Targeted theft of passwords (`_sendpassword`).
5.  **Visual Surveillance:** Capturing screenshots of the victim’s machine (`_GetScreenshot`).
6.  **Continuous Connectivity:** Stable, asynchronous connection management for ongoing access to the victim's device (`_ConnectAsync`).

### Final Conclusion
The analysis of all four chunks reveals that **Discord_rat** is a highly sophisticated piece of malware produced by a professional developer or organized group. The primary hallmark of this threat is its **evasion-first design**. By layering advanced assembly-level obfuscation (junk code, instruction overlapping, and function wrapping) over standard RAT features, the developers have created a tool that is intentionally difficult to analyze, reverse engineer, and signature_scan. 

The inclusion of screenshot capabilities, credential theft, and persistent networking confirms its purpose: it is designed for long-term surveillance and data exfiltration from infected targets.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of "Wrapper" logic, junk code, and control-flow flattening is designed to hide the malware's true intent from analysts. |
| T1113 | Screen Capture | The `_GetScreenshot` function allows the threat actor to perform visual surveillance on the victim's machine. |
| T1059 | Command and Scripting Interpreter | The `_ShellCommand` capability enables the execution of arbitrary commands via a command shell. |
| T1083 | File and Directory Discovery | The `_dir` function is utilized to list and navigate the file system to identify targets for collection. |
| T1082 | System Information Discovery | The `_getprocs` function identifies running processes, assisting in reconnaissance of the environment. |
| T1071 | Application Layer Protocol | Utilizing Discord as a communication channel hides C2 traffic within standard application layer protocols. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized as requested:

**IP addresses / URLs / Domains**
*   **Discord Infrastructure:** The analysis confirms that the malware utilizes Discord's infrastructure to mask its Command & Control (C2) communications. *(Note: No specific URLs or IP addresses were present in the raw strings, but "Discord" is the primary C2 channel identifier).*

**File paths / Registry keys**
*   *None identified.* (The string `Microsoft.Win32` refers to a standard .NET library and does not constitute a specific malicious registry key.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts (user agents, C2 patterns, etc.)**
*   **Malware Family Name:** `Discord_rat`
*   **Detection Evasion Techniques:** 
    *   `rootkitaddpath`: Used as a universal wrapper to mask distinct functions (e.g., `GetScreenshot`, `Send_message`).
    *   **Control-Flow Flattening (CFF):** Implementation of "unreachable blocks" and junk code logic.
    *   **Instruction Overlapping:** Use of overlapping instructions to defeat disassemblers like IDA Pro or Ghidra.
*   **Malicious Function Indicators (Behavioral IOCs):**
    *   `uacbypass` (Privilege escalation)
    *   `DisableFirewall` / `DisableDefender` (Security software evasion)
    *   `ShellCommand` (Remote command execution)
    *   `GetScreenshot` (Visual surveillance/spyware)
    *   `sendpassword` / `getprocs` (Credential harvesting and reconnaissance)
    *   `Rootkit` / `ProcKill` (Persistence and process manipulation)
    *   `webcampic` (Potential web-based interaction or activity logging)
    *   `geolocate` (Target tracking)
    *   `heartbeat` (C2 check-in mechanism)

---

## Malware Family Classification

1. **Malware family**: custom (specifically identified as a "Discord-based" RAT)
2. **Malware type**: RAT
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Evasion Techniques:** The sample employs sophisticated anti-analysis methods including Control-Flow Flattening (CFF), instruction overlapping, and the use of a "Wrapper" system (`rootkitaddpath`) to mask distinct functions like screenshotting and network communication.
    *   **Extensive Remote Access Capabilities:** The analysis confirms a suite of features typical of high-end RATs, including remote command execution (`_ShellCommand`), credential harvesting (`_sendpassword`), file system navigation, and process monitoring.
    *   **Sophisticated C2 Infrastructure:** It utilizes Discord as a primary communication channel to mask its traffic, combined with persistent asynchronous connections (`_ConnectAsync`) to maintain long-term access to the infected host.
