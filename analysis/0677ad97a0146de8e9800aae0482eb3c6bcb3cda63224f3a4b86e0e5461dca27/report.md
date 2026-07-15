# Threat Analysis Report

**Generated:** 2026-07-15 03:38 UTC
**Sample:** `0677ad97a0146de8e9800aae0482eb3c6bcb3cda63224f3a4b86e0e5461dca27_0677ad97a0146de8e9800aae0482eb3c6bcb3cda63224f3a4b86e0e5461dca27.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0677ad97a0146de8e9800aae0482eb3c6bcb3cda63224f3a4b86e0e5461dca27_0677ad97a0146de8e9800aae0482eb3c6bcb3cda63224f3a4b86e0e5461dca27.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 68,608 bytes |
| MD5 | `05f916a0eb213cfe8dad37a240b2428d` |
| SHA1 | `4c2e147f08f0e4fbd11ee8e007f75d9b292d3f67` |
| SHA256 | `0677ad97a0146de8e9800aae0482eb3c6bcb3cda63224f3a4b86e0e5461dca27` |
| Overall entropy | 5.777 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3724057605 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 66,048 | 5.848 | No |
| `.rsrc` | 1,536 | 3.951 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **776** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU
	o )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU
..b+hr$
p+fr2

+Vr>
p+NrN
p+Fr\
p+>rh
p+6rv
p+.rz
v4.0.30319
#Strings
"	-	6	Y	{	
<Start>b__12_0
<Main>d__1
<>u__1
<>f__AnonymousType3`1
Func`1
Task`1
AsyncTaskMethodBuilder`1
EqualityComparer`1
TaskAwaiter`1
IEnumerator`1
List`1
<>7__wrap1
<ProcessAsync>d__12
Microsoft.Win32
ToInt32
<info>5__2
<http>5__2
<logger>5__2
<SendStartupAsync>d__2
<>u__2
<>f__AnonymousType2`2
Dictionary`2
<>7__wrap2
<HandleScreenshotAsync>d__13
<ip>5__3
<apiClient>5__3
<GetPublicIpAsync>d__3
<>f__AnonymousType10`3
<>f__AnonymousType0`3
<HandleMouseAsync>d__14
get_WorkingSet64
ToUInt64
<response>5__4
<success>5__4
<SendHeartbeatAsync>d__4
<GetCountryAsync>d__4
<>f__AnonymousType11`4
<>f__AnonymousType1`4
<>f__AnonymousType5`4
<>f__AnonymousType7`4
<>7__wrap4
<HandleKeyboardAsync>d__15
<RunAsync>d__15
<RunAsync>d__5
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MemoryInfo.set_freePhysical` | `0x408027` | 47594 | ✓ |
| `method._SendTelegramAsync_d__7.SetStateMachine` | `0x408a9c` | 47026 | ✓ |
| `method.RemoteClient.Models.SystemInfo.set_RegistrationKey` | `0x4060e7` | 7808 | ✓ |
| `method.__f__AnonymousType3_1.GetHashCode` | `0x402539` | 3680 | ✓ |
| `method.RemoteClient.Utils.Persistence.get_AppDataPath` | `0x40426f` | 3050 | ✓ |
| `method.RemoteClient.Services.ProcessService..ctor` | `0x405519` | 2782 | ✓ |
| `method._ProcessAsync_d__12.MoveNext` | `0x406d10` | 2748 | ✓ |
| `method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor` | `0x403a11` | 2142 | ✓ |
| `method.RemoteClient.Services.InputService.TranslateKey` | `0x404888` | 1600 | ✓ |
| `method.__f__AnonymousType9_6..ctor` | `0x4033c9` | 1569 | ✓ |
| `method.RemoteClient.Services.KeyloggerService._Start_b__12_0` | `0x405143` | 952 | ✓ |
| `method._RunAsync_d__5.MoveNext` | `0x4079ac` | 896 | ✓ |
| `method.RemoteClient.Services.SystemInfoService.GetSystemInfoAsync` | `0x405a40` | 884 | ✓ |
| `method._GetCountryAsync_d__4.MoveNext` | `0x408038` | 724 | ✓ |
| `method.RemoteClient.Services.KeyloggerService.Start` | `0x404e91` | 690 | ✓ |
| `method._SendStartupAsync_d__2.MoveNext` | `0x408660` | 628 | ✓ |
| `method.RemoteClient.Services.SystemInfoService.GetNetworkInfoAsync` | `0x405db4` | 560 | ✓ |
| `method.RemoteClient.Services.ScreenCaptureService.CaptureAsync` | `0x40567c` | 524 | ✓ |
| `method._RunAsync_d__15.MoveNext` | `0x407d3c` | 524 | ✓ |
| `method._SendHeartbeatAsync_d__4.MoveNext` | `0x406258` | 464 | ✓ |
| `method._Main_d__1.MoveNext` | `0x4077dc` | 448 | ✓ |
| `method._SendTelegramAsync_d__7.MoveNext` | `0x4088e4` | 440 | ✓ |
| `method.__f__AnonymousType8_7.ToString` | `0x403260` | 416 | ✓ |
| `method._SendDiscordAsync_d__8.MoveNext` | `0x4084bc` | 404 | ✓ |
| `method._GetPublicIpAsync_d__3.MoveNext` | `0x40831c` | 400 | ✓ |
| `method.__f__AnonymousType6_9.ToString` | `0x402ce4` | 396 | ✓ |
| `method.RemoteClient.Services.InputService.HandleMouseAsync` | `0x4046c4` | 396 | ✓ |
| `method.RemoteClient.Services.NotificationService.BuildMessage` | `0x40522c` | 388 | ✓ |
| `method._HandleProcessKillAsync_d__17.MoveNext` | `0x406a54` | 380 | ✓ |
| `method._HandleMouseAsync_d__14.MoveNext` | `0x406900` | 324 | ✓ |

### Decompiled Code Files

- [`code/method.MemoryInfo.set_freePhysical.c`](code/method.MemoryInfo.set_freePhysical.c)
- [`code/method.RemoteClient.Models.SystemInfo.set_RegistrationKey.c`](code/method.RemoteClient.Models.SystemInfo.set_RegistrationKey.c)
- [`code/method.RemoteClient.Services.InputService.HandleMouseAsync.c`](code/method.RemoteClient.Services.InputService.HandleMouseAsync.c)
- [`code/method.RemoteClient.Services.InputService.TranslateKey.c`](code/method.RemoteClient.Services.InputService.TranslateKey.c)
- [`code/method.RemoteClient.Services.KeyloggerService.Start.c`](code/method.RemoteClient.Services.KeyloggerService.Start.c)
- [`code/method.RemoteClient.Services.KeyloggerService._Start_b__12_0.c`](code/method.RemoteClient.Services.KeyloggerService._Start_b__12_0.c)
- [`code/method.RemoteClient.Services.NotificationService.BuildMessage.c`](code/method.RemoteClient.Services.NotificationService.BuildMessage.c)
- [`code/method.RemoteClient.Services.ProcessService..ctor.c`](code/method.RemoteClient.Services.ProcessService..ctor.c)
- [`code/method.RemoteClient.Services.ScreenCaptureService.CaptureAsync.c`](code/method.RemoteClient.Services.ScreenCaptureService.CaptureAsync.c)
- [`code/method.RemoteClient.Services.SystemInfoService.GetNetworkInfoAsync.c`](code/method.RemoteClient.Services.SystemInfoService.GetNetworkInfoAsync.c)
- [`code/method.RemoteClient.Services.SystemInfoService.GetSystemInfoAsync.c`](code/method.RemoteClient.Services.SystemInfoService.GetSystemInfoAsync.c)
- [`code/method.RemoteClient.Utils.Persistence.get_AppDataPath.c`](code/method.RemoteClient.Utils.Persistence.get_AppDataPath.c)
- [`code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor.c`](code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor.c)
- [`code/method._GetCountryAsync_d__4.MoveNext.c`](code/method._GetCountryAsync_d__4.MoveNext.c)
- [`code/method._GetPublicIpAsync_d__3.MoveNext.c`](code/method._GetPublicIpAsync_d__3.MoveNext.c)
- [`code/method._HandleMouseAsync_d__14.MoveNext.c`](code/method._HandleMouseAsync_d__14.MoveNext.c)
- [`code/method._HandleProcessKillAsync_d__17.MoveNext.c`](code/method._HandleProcessKillAsync_d__17.MoveNext.c)
- [`code/method._Main_d__1.MoveNext.c`](code/method._Main_d__1.MoveNext.c)
- [`code/method._ProcessAsync_d__12.MoveNext.c`](code/method._ProcessAsync_d__12.MoveNext.c)
- [`code/method._RunAsync_d__15.MoveNext.c`](code/method._RunAsync_d__15.MoveNext.c)
- [`code/method._RunAsync_d__5.MoveNext.c`](code/method._RunAsync_d__5.MoveNext.c)
- [`code/method._SendDiscordAsync_d__8.MoveNext.c`](code/method._SendDiscordAsync_d__8.MoveNext.c)
- [`code/method._SendHeartbeatAsync_d__4.MoveNext.c`](code/method._SendHeartbeatAsync_d__4.MoveNext.c)
- [`code/method._SendStartupAsync_d__2.MoveNext.c`](code/method._SendStartupAsync_d__2.MoveNext.c)
- [`code/method._SendTelegramAsync_d__7.MoveNext.c`](code/method._SendTelegramAsync_d__7.MoveNext.c)
- [`code/method._SendTelegramAsync_d__7.SetStateMachine.c`](code/method._SendTelegramAsync_d__7.SetStateMachine.c)
- [`code/method.__f__AnonymousType3_1.GetHashCode.c`](code/method.__f__AnonymousType3_1.GetHashCode.c)
- [`code/method.__f__AnonymousType6_9.ToString.c`](code/method.__f__AnonymousType6_9.ToString.c)
- [`code/method.__f__AnonymousType8_7.ToString.c`](code/method.__f__AnonymousType8_7.ToString.c)
- [`code/method.__f__AnonymousType9_6..ctor.c`](code/method.__f__AnonymousType9_6..ctor.c)

## Behavioral Analysis

This final analysis incorporates the findings from **Chunk 18/18**, completing the overview of the provided disassembly segments. This final segment confirms that the malware's architecture is designed not just to hide its intent, but to actively sabotage the tools and techniques used by security researchers.

---

### Executive Summary Update
Analysis of Chunk 18/18 reinforces the conclusion that this malware utilizes a **highly sophisticated Virtual Machine (VM) architecture**. The final segments demonstrate an extreme level of "control-flow flattening" and "opaque predicate" injection. 

The code is structured as a state machine where logic is not expressed through standard `if/else` or `switch` statements, but through a series of complex, mathematically derived transitions. This ensures that even if a researcher identifies a piece of malicious functionality (like the screen capture routine), they cannot easily trace how it is triggered or how it communicates with the Command and Control (C2) infrastructure.

---

### New Findings & Technical Deep Dive

#### 1. State-Machine Complexity via Nested Loop Obfuscation
The final disassembly shows a high density of `do { ... } while (true)` loops involving complex bitwise operations (`CONCAT`, `CARRY1`, `SHIFT`).
*   **Technical Detail:** These are not standard programming constructs for simple logic. In a VM-based packer, these "loops" often represent the **dispatcher loop**. Every time the "virtual instruction pointer" moves, the malware executes a block of math to determine the next destination. 
*   **Analysis:** The sheer number of jumps (`goto code_r0x00406c35`, `goto code_r0x00406cd7`) combined with these loops creates a "spaghetti" effect. This makes it nearly impossible for a human to follow the logic linearly. The malware is essentially "re-calculating" its path at every step of execution.

#### 2. Advanced Control Flow Graph (CFG) Destruction
The repeated use of `POPCOUNT` and overlapping instructions in this final section serves a specific purpose: **breaking the decompiler's ability to represent the code as a tree.**
*   **Technical Detail:** By using `POPCOUNT(uVar6) & 1U`, the author creates conditions that are always true or always false, but cannot be determined by a static analyzer without executing the code.
*   **Analysis:** This is **Anti-Decompilation**. Tools like Ghidra and IDA Pro rely on identifying "basic blocks" of code. By intentionally creating overlaps and ambiguous branches, the author forces these tools to produce broken or incomplete output, making it much harder for a human to analyze the core logic.

#### 3. Obfuscated Pointer Arithmetic & Constant Masking
Notice terms like `pcVar12 = CONCAT31(Var22,uVar6 + 0x15)` and large constants like `0x1f2802` or `0x4b000000`.
*   **Technical Detail:** These are not "standard" numbers. They are typically used to calculate memory offsets for the VM’s internal handler table. 
*   **Analysis:** The malware is using a **Table-Driven Architecture**. Instead of having distinct functions for different tasks, it has one large blob of code (the VM) that takes a command and looks up what to do in a hidden table. This prevents an analyst from finding a single "Keylogger" function; instead, they find only the "VM Interpreter" which handles the keylogging commands on the fly.

---

### Final Consolidated Risk Assessment Table

| Feature | Evidence Found | Risk Level | Analysis Note |
| :--- | :--- | :--- | :--- |
| **Virtual Machine (VM)** | `POPCOUNT` gates, custom bit-shifts, complex state loops | **Extreme** | The primary defense; hides the true logic of the malware from static analysis. |
| **Keylogging** | `KeyloggerService` / VM-obfuscated handlers | **Critical** | Captured via a hidden "instruction" within the VM's lifecycle. |
| **Screen Capture** | `ScreenCaptureService` | **Critical** | Captures full visual context of the victim's desktop. |
| **Machine Fingerprinting** | `set_RegisterKey`, complex math loops | **High** | Creates a unique ID (HWID) for tracking specific victims. |
| **C2 / Exfiltration** | `SendTelegramAsync` | **Critical** | Uses Telegram API as a robust, disguised channel for data theft. |
| **Control Flow Obfuscation** | Overlapping instructions at `0x406c3d`, etc. | **High** | Designed to break Ghidra/IDA's ability to map the program flow. |
| **Opaque Predicates** | Frequent `POPCOUNT` logic checks | **High** | Creates "ghost" paths to waste analyst time and break automation. |
| **Arithmetic Noise** | Heavy use of `CONCAT`, `CARRY1`, and large constants | **Medium** | Masks simple operations behind a wall of complex math. |

---

### Final Analysis Conclusion & Strategic Recommendations

The analysis of all 18 chunks confirms that this is a **sophisticated, high-tier piece of malware**. The authors have intentionally implemented several "layers" of protection:
1.  **Layer 1 (Network):** Telegram as a C2 makes the traffic look like standard social media usage.
2.  **Layer 2 (Logic):** A custom Virtual Machine ensures that even if the binary is captured, the core logic is not immediately visible.
3.  **Layer 3 (Anti-Analysis):** Overlapping instructions and `POPCOUNT` predicates make it a manual labor nightmare for human reverse engineers.

#### **Recommended Defense & Investigation Strategy:**

1.  **Dynamic Analysis over Static Analysis:** 
    Because the "VM" makes static analysis of this code almost impossible, focus on **behavioral monitoring**. Use tools like **Process Monitor (ProcMon)** to watch for file system changes and **Wireshark/Fiddler** to capture outgoing packets to Telegram.
2.  **Memory Forensics:** 
    Instead of trying to "crack" the math in the disassembly, wait for the malware to run. At some point, the VM must decrypt its instructions into memory to execute them. Capture a **memory dump** at this point to find cleartext strings (IP addresses, file paths, and stolen data).
3.  **API Hooking with Frida:** 
    Since the "VM" eventually has to call standard Windows APIs for keylogging (`SetWindowsHookEx`) or networking, use **Frida** to intercept those specific calls. By hooking the API at the system level, you bypass all the "math-noise" of the VM.
4.  **Egress Filtering:** 
    Implement strict outbound firewall rules. Block unknown processes from reaching `api.telegram.org` or other common C2 ports/domains.

**Final Summary for Stakeholders:**
This is a high-capability threat. The complexity of the code suggests it was developed by an experienced group that values persistence and evasion over simplicity. **Detection should focus on the "symptoms" (Unauthorized Telegram traffic, keyboard hooking) rather than trying to fully deconstruct the inner "VM" mechanics.**

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your technical analysis to the relevant MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1028** | Encoded Script or Payload | The use of a custom VM architecture, control-flow flattening, and opaque predicates are designed to hide the malware's true logic from static analysis. |
| **T1056.001** | Input Capture: Keylogging | The presence of `KeyloggerService` confirms the intent to capture user keystrokes through a hidden VM handler. |
| **T1113** | Screen Capture | The inclusion of `ScreenCaptureService` allows the malware to record visual context from the victim's desktop. |
| **T1583** | Acquire System Information | "Machine Fingerprinting" and hardware ID (HWID) generation are used to collect system information for identifying and tracking unique victims. |
| **T1567** | Exfiltration Over Web Service | The use of `SendTelegramAsync` leverages a legitimate web service (Telegram API) as an evasion-friendly channel for data exfiltration. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided string data and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*   *(No direct IP addresses or URLs were found in the provided strings.)*
*   **Note:** The presence of `SendTelegramAsync` and `SendDiscordAsync` indicates use of these platforms for C2 communication, which may involve reaching out to `api.telegram.org` or Discord API endpoints.

### **File paths / Registry keys**
*   *(No specific file paths or registry keys were identified in the provided data.)*

### **Mutex names / Named pipes**
*   *(None found.)*

### **Hashes**
*   *(No MD5, SHA-1, or SHA-256 hashes were present in the strings.)*

### **Other artifacts**
*   **C2 Communication Patterns:**
    *   `SendTelegramAsync` (Likely Telegram Bot API for data exfiltration/commanding)
    *   `SendDiscordAsync` (Potential Discord integration for notification or C2)
    *   `SendHeartbeatAsync` (Indicates a persistent connection to the C2 server)
    *   `SendStartupAsync` (Initialization check with command infrastructure)

*   **Information Gathering/Spyware Capabilities:**
    *   `GetPublicIpAsync` / `GetCountryAsync` (Geographic and network footprint gathering)
    *   `HandleScreenshotAsync` (Visual data theft)
    *   `HandleKeyboardAsync` / `HandleMouseAsync` (Input logging)
    *   `CaptureAsync` (General environment capture)
    *   `GetNetworkInfoAsync` / `GetSystemInfoAsync` (Host fingerprinting)

*   **Evasion & Obfuscation Techniques:**
    *   **Virtual Machine (VM) Architecture:** The malware uses a custom VM-based packer/interpreter to shield its core logic.
    *   **Control-Flow Flattening:** Used to obscure the program's decision-making path.
    *   **Opaque Predicates:** Specifically using `POPCOUNT` logic to create branches that are difficult for static analysis tools to resolve.
    *   **Instruction Overlapping:** Identified at offsets such as `0x406c3d`, used to break decompiler output (e.g., Ghidra/IDA Pro).

*   **Data Collection Variables:**
    *   `chat_id`, `pid`, `GetPayload`, `WatchdogEnabled`, `DiscordEnabled`, `TelegramEnabled`.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: RAT (Remote Access Trojan) / Infostealer
3. **Confidence**: High

4. **Key evidence**:
*   **Spyware Capabilities:** The analysis explicitly identifies `KeyloggerService`, `ScreenCaptureService`, and various "Handle" functions for keyboard, mouse, and screenshot captures, which are core components of a RAT.
*   **Advanced Obfuscation/Anti-Analysis:** The use of a custom Virtual Machine (VM) architecture, control-flow flattening, and opaque predicates (`POPCOUNT`) indicates a high-tier sophistication designed to hide malicious logic from automated tools and human researchers.
*   **C2 Infrastructure & Exfiltration:** The integration of `SendTelegramAsync` and `SendDiscordAsync` shows a clear mechanism for exfiltrating stolen data (screen captures, keystrokes) while masking the traffic as legitimate social media communications.
