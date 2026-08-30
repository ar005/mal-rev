# Threat Analysis Report

**Generated:** 2026-08-23 17:22 UTC
**Sample:** `1159467031d7e6422cc1dbb955b2bdd50a0552dc433364caeffb5e2204f042aa_1159467031d7e6422cc1dbb955b2bdd50a0552dc433364caeffb5e2204f042aa.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1159467031d7e6422cc1dbb955b2bdd50a0552dc433364caeffb5e2204f042aa_1159467031d7e6422cc1dbb955b2bdd50a0552dc433364caeffb5e2204f042aa.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 38,400 bytes |
| MD5 | `03bb9f2d582790ce584c3f85800a5af0` |
| SHA1 | `5a83ed4ed8a35651a8a2b01ce1c540381dbd160d` |
| SHA256 | `1159467031d7e6422cc1dbb955b2bdd50a0552dc433364caeffb5e2204f042aa` |
| Overall entropy | 5.562 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774971410 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 35,840 | 5.689 | No |
| `.rsrc` | 1,536 | 3.755 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **528** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
	,	tC
	,	tC
v4.0.30319
#Strings
E	K	m	~	
<Module>
mscorlib
Microsoft.VisualBasic
MyApplication
MyComputer
MyProject
MyWebServices
ThreadSafeObjectProvider`1
Settings
ClientSocket
Messages
Uninstaller
ProcessCritical
AlgorithmAES
Helper
LASTINPUTINFO
EXECUTION_STATE
Microsoft.VisualBasic.ApplicationServices
ApplicationBase
Microsoft.VisualBasic.Devices
Computer
System
Object
.cctor
get_Computer
m_ComputerObjectProvider
get_Application
m_AppObjectProvider
get_User
m_UserObjectProvider
get_WebServices
m_MyWebServicesObjectProvider
Application
WebServices
Equals
GetHashCode
GetType
ToString
Create__Instance__
instance
Dispose__Instance__
get_GetInstance
m_ThreadStaticValue
GetInstance
InstallDir
InstallStr
Exclusion
RunAntiAnalysis
anyrun
DetectManufacturer
DetectDebugger
DetectSandboxie
GetModuleHandle
lpModuleName
CheckRemoteDebuggerPresent
hProcess
isDebuggerPresent
isConnected
System.Net.Sockets
Socket
BufferLength
Buffer
System.IO
MemoryStream
System.Threading
ManualResetEvent
allDone
SendSync
Interval
ActivatePong
BeginConnect
ConnectServer
INDATE
Spread
Antivirus
IAsyncResult
BeginReceive
BeginRead
EndSend
isDisconnected
Plugin
SendMSG
SendError
Thread
ReportWindow
Monitoring
OpenUrl
Hidden
capCreateCaptureWindowA
lpszWindowName
dwStyle
nWidth
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Stub.Helper.CloseMutex` | `0x40578c` | 43124 | ✓ |
| `method.Stub.Messages.Read` | `0x4037c8` | 2196 | ✓ |
| `method.Stub.Messages.Plugin` | `0x40405c` | 1244 | ✓ |
| `entry0` | `0x40226c` | 848 | ✓ |
| `method.Stub.Uninstaller.UNS` | `0x404b04` | 680 | ✓ |
| `method.Stub.ClientSocket.BeginReceive` | `0x403284` | 496 | ✓ |
| `method.Stub.Main.DetectManufacturer` | `0x4027a8` | 440 | ✓ |
| `method.Stub.Helper.Decompress` | `0x405350` | 416 | ✓ |
| `method.Stub.Helper.Compress` | `0x4054f0` | 400 | ✓ |
| `method.Stub.ClientSocket.ConnectServer` | `0x402b5c` | 368 | ✓ |
| `method.Stub.ClientSocket.Info` | `0x402ccc` | 356 | ✓ |
| `method.Stub.Main.Exclusion` | `0x4025bc` | 280 | ✓ |
| `method.Stub.ClientSocket.Antivirus` | `0x402f50` | 260 | ✓ |
| `method.Stub.ClientSocket.Send` | `0x4034a8` | 256 | ✓ |
| `method.Stub.ClientSocket.isDisconnected` | `0x4035e8` | 248 | ✓ |
| `method.Stub.Messages.TD` | `0x4045c0` | 240 | ✓ |
| `method.Stub.Messages.Monitoring` | `0x4046b0` | 240 | ✓ |
| `method.Stub.ClientSocket.RAM` | `0x4031ac` | 216 | ✓ |
| `method.Stub.ClientSocket.BeginConnect` | `0x402a88` | 212 | ✓ |
| `method.Stub.Messages.RunDisk` | `0x4048bc` | 212 | ✓ |
| `method._Closure___1._Lambda___7` | `0x404a2c` | 200 | ✓ |
| `method.Stub.Messages.OpenUrl` | `0x4047a0` | 192 | ✓ |
| `method.Stub.ClientSocket.GPU` | `0x403054` | 184 | ✓ |
| `method.Stub.ClientSocket.CPU` | `0x40310c` | 160 | ✓ |
| `method.Stub.Helper.ID` | `0x405174` | 144 | ✓ |
| `method.Stub.AlgorithmAES.Decrypt` | `0x404e48` | 140 | ✓ |
| `method.Stub.Helper..cctor` | `0x404ed4` | 132 | ✓ |
| `method.Stub.ClientSocket.Ping` | `0x403728` | 124 | ✓ |
| `method.Stub.Messages.Memory` | `0x404990` | 124 | ✓ |
| `method.Stub.Helper.GetLastInputTime` | `0x404fcc` | 124 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Stub.AlgorithmAES.Decrypt.c`](code/method.Stub.AlgorithmAES.Decrypt.c)
- [`code/method.Stub.ClientSocket.Antivirus.c`](code/method.Stub.ClientSocket.Antivirus.c)
- [`code/method.Stub.ClientSocket.BeginConnect.c`](code/method.Stub.ClientSocket.BeginConnect.c)
- [`code/method.Stub.ClientSocket.BeginReceive.c`](code/method.Stub.ClientSocket.BeginReceive.c)
- [`code/method.Stub.ClientSocket.CPU.c`](code/method.Stub.ClientSocket.CPU.c)
- [`code/method.Stub.ClientSocket.ConnectServer.c`](code/method.Stub.ClientSocket.ConnectServer.c)
- [`code/method.Stub.ClientSocket.GPU.c`](code/method.Stub.ClientSocket.GPU.c)
- [`code/method.Stub.ClientSocket.Info.c`](code/method.Stub.ClientSocket.Info.c)
- [`code/method.Stub.ClientSocket.Ping.c`](code/method.Stub.ClientSocket.Ping.c)
- [`code/method.Stub.ClientSocket.RAM.c`](code/method.Stub.ClientSocket.RAM.c)
- [`code/method.Stub.ClientSocket.Send.c`](code/method.Stub.ClientSocket.Send.c)
- [`code/method.Stub.ClientSocket.isDisconnected.c`](code/method.Stub.ClientSocket.isDisconnected.c)
- [`code/method.Stub.Helper..cctor.c`](code/method.Stub.Helper..cctor.c)
- [`code/method.Stub.Helper.CloseMutex.c`](code/method.Stub.Helper.CloseMutex.c)
- [`code/method.Stub.Helper.Compress.c`](code/method.Stub.Helper.Compress.c)
- [`code/method.Stub.Helper.Decompress.c`](code/method.Stub.Helper.Decompress.c)
- [`code/method.Stub.Helper.GetLastInputTime.c`](code/method.Stub.Helper.GetLastInputTime.c)
- [`code/method.Stub.Helper.ID.c`](code/method.Stub.Helper.ID.c)
- [`code/method.Stub.Main.DetectManufacturer.c`](code/method.Stub.Main.DetectManufacturer.c)
- [`code/method.Stub.Main.Exclusion.c`](code/method.Stub.Main.Exclusion.c)
- [`code/method.Stub.Messages.Memory.c`](code/method.Stub.Messages.Memory.c)
- [`code/method.Stub.Messages.Monitoring.c`](code/method.Stub.Messages.Monitoring.c)
- [`code/method.Stub.Messages.OpenUrl.c`](code/method.Stub.Messages.OpenUrl.c)
- [`code/method.Stub.Messages.Plugin.c`](code/method.Stub.Messages.Plugin.c)
- [`code/method.Stub.Messages.Read.c`](code/method.Stub.Messages.Read.c)
- [`code/method.Stub.Messages.RunDisk.c`](code/method.Stub.Messages.RunDisk.c)
- [`code/method.Stub.Messages.TD.c`](code/method.Stub.Messages.TD.c)
- [`code/method.Stub.Uninstaller.UNS.c`](code/method.Stub.Uninstaller.UNS.c)
- [`code/method._Closure___1._Lambda___7.c`](code/method._Closure___1._Lambda___7.c)

## Behavioral Analysis

Based on the analysis of chunk 4/4, I have finalized the profile of **[Malicious_Loader_Stub]**. This final segment provides definitive evidence of highly aggressive anti-analysis techniques designed specifically to defeat static analysis tools and hinder manual reverse engineering.

### Finalized Analysis: [Malicious_Loader_Stub] (v4)

#### 1. Core Functionality and Purpose
The analysis of the final chunk reveals that the loader's "infrastructure" is designed not just to deliver a payload, but to actively defend its own logic from being analyzed by security researchers.

*   **Aggressive Anti-Automation & Interaction Checks:** The inclusion of `method.Stub.Helper.GetLastInputTime` is a classic indicator used to detect if the malware is running in an automated sandbox. By checking how long it has been since the last mouse click or keyboard input, the malware can determine if it is being "interacted with" by a human or if it is sitting in a headless analysis environment.
*   **Complex Networking Management:** While `method.Stub.ClientSocket.Ping` appears to be a simple network check, the massive amount of obfuscated code surrounding it suggests that even basic communication protocols are wrapped in "noise." This prevents analysts from easily identifying the heartbeat logic or any data being exchanged during the handshake.
*   **Potential Execution Flow Manipulation:** The presence of `swi(1)` (Software Interrupt) and references to `unaff_retaddr` suggest the malware may use custom exception handling. By intentionally triggering an interrupt, the loader can jump to a specific handler, effectively "hiding" its next move from standard linear disassembly.

#### 2. Suspicious and Malicious Behaviors
Chunk 4/4 provides high-confidence evidence of **Advanced Anti-Analysis & De-obfuscation Resistance**:

*   **Control Flow Obfuscation (Overlapping Code & Junk Data):** The numerous "WARNING: Instruction at [...] overlaps" and "Bad instruction" flags in the `Ping` function are critical indicators. This is a deliberate technique where "junk" bytes are inserted to trick disassemblers like Ghidra or IDA into misinterpreting the start/end of instructions.
    *   **Impact:** This creates a "maze" for the analyst, making it nearly impossible to trace the actual logic of the `Ping` function through static analysis alone.
*   **Sandboxing & Automation Detection:** The `GetLastInputTime` function is a high-confidence indicator of **anti-analysis capability**. If no input is detected within a certain timeframe, the loader may terminate or execute "decoy" behavior to mislead researchers.
*   **Heavy Code Bloat (Obfuscation via Complexity):** The sheer amount of mathematical complexity (e.g., `CONCAT31`, `CARRY1` logic) surrounding simple operations indicates that the developer is using **Control Flow Flattening** or similar techniques. This forces an analyst to spend hours reverse-engineering math that has no functional purpose other than to exhaust their time and resources.

#### 3. Technical Summary for Incident Response
The final technical summary for your threat intelligence report should be updated as follows:

*   **Sophistication Level:** **Extreme.** The combination of layered encryption (AES), hardware fingerprinting, and advanced control-flow obfuscation (overlapping instructions/junk code) suggests a high-tier actor or professional malware developer.
*   **New Key Indicators of Concern (IoCs):**
    *   **Anti-Analysis Tactics:** High usage of **Control Flow Obfuscation**. Analysis tools may produce "broken" output due to intentional overlapping instructions at `0x403dcf`.
    *   **Sandboxing Detection:** Use of `GetLastInputTime` indicates a strategy to evade automated security systems and sandboxes.
    *   **Execution Strategy:** The loader is designed to be "hard" to statically analyze. It utilizes **junk-code injection** to shield its core logic from static tools, meaning dynamic analysis (running the code in a controlled environment) will likely be necessary to see the final payload.
*   **Detection Strategy:** 
    1.  **Dynamic Analysis Focus:** Because of the heavy "junk code" and overlapping instructions used to defeat disassemblers, defense teams should prioritize **dynamic memory forensics**. The true intent of the code only becomes clear once it is unpacked and decrypted in RAM.
    2.  **Behavioral Monitoring:** Monitor for processes that perform **Human Interaction Checks** (e.g., querying `GetLastInputTime`) followed by high-privilege actions or network connections to known malicious IPs/domains.
    3.  **Advanced De-obfuscation:** Use symbolic execution tools (like Triton) to "flatten" the control flow and strip away the junk code before attempting manual analysis of the core logic.

### Final Summary Update Table (Internal Note)
| Feature | Initial Observation | Findings (Chunk 4/4) | Impact Level |
| :--- | :--- | :--- | :--- |
| **Payload Processing** | Detection of compression. | Confirmed **AES Decryption** stage following decompression. | **Critical** |
| **Anti-Analysis** | Standard anti-debug/VM. | Advanced hardware profiling & **Sandboxing detection (GetLastInputTime)**. | **High** |
| **Obfuscation Style** | Basic obfuscation. | **Control Flow Obfuscation**, overlapping instructions, and junk code injection. | **Extreme** |
| **Network Logic** | Standard C2 Heartbeat. | Highly obscured "Ping" logic via complex mathematical noise. | **Medium** |

**Final Conclusion:** This loader is a highly sophisticated piece of malware infrastructure designed to resist both automated detection systems and manual professional analysis. It uses every standard high-tier tactic: multi-layered encryption, hardware fingerprinting, sandboxing detection, and heavy control-flow obfuscation. The primary payload is shielded by several layers of complexity that are only "stripped away" in memory during the execution phase.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Detection | The use of `GetLastInputTime` and hardware fingerprinting are specific tactics used to identify if the malware is running in an automated sandbox or a researcher's laboratory. |
| **T1027** | Obfuscated Files or Information | The implementation of junk code, overlapping instructions, and "mathematical noise" is designed to defeat disassemblers and complicate manual reverse engineering of the core logic. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

### **IP addresses / URLs / Domains**
*   *None identified in the provided text.* (The analysis mentions "Ping" logic and "C2 patterns," but no specific hardcoded IPs or domains were included in the raw string dump.)

### **File paths / Registry keys**
*   *None identified.* (While terms like `InstallDir` and `InstallStr` appear, they are generic variables rather than specific file paths.)

### **Mutex names / Named pipes**
*   **_appMutex** (Identified as a potential mutex name used for process synchronization or infection tracking.)

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Anti-Analysis Functions:** 
    *   `GetLastInputTime` (Used to detect sandboxes/automated analysis).
    *   `DetectDebugger`
    *   `DetectSandboxie`
    *   `RunAntiAnalysis`
    *   `GetForegroundWindow`
    *   `GetActiveWindowTitle`
*   **Obfuscation & Evasion Techniques:**
    *   **Control Flow Obfuscation:** Use of overlapping instructions and junk code injection.
    *   **Specific Offset:** `0x403dcf` (Identified as the specific location where "broken" logic/overlapping instructions occur to thwart disassemblers).
    *   **Encryption Standard:** AES (specifically referenced via `AES_Encryptor` and `AES_Decryptor`).
    *   **User Agent Rotation:** Presence of a `userAgents` string list, indicating evasion of network filters.
*   **Technical Indicators:**
    *   **Suspicious Logic:** `SendMSG`, `ReportWindow`, `RunDisk`, `GetHashT`.
    *   **Network Behavior:** "Ping" logic hidden within complex mathematical noise (Control Flow Flattening).

---

### **Summary for Incident Response**
*   **Primary Threat Actor Profile:** Sophisticated/High-tier.
*   **Key Behavioral Indicators:** The sample utilizes a multi-layered approach to evasion: 1) Detection of virtualization/sandboxing via human interaction checks (`GetLastInputTime`), 2) Heavy use of AES encryption for payload protection, and 3) Advanced anti-disassembly techniques (overlapping instructions at `0x403dcf`).
*   **Recommended Defense:** Since static analysis is hindered by "junk code" and "broken" assembly, analysts should prioritize **dynamic memory forensics** to capture the decrypted payloads.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `method.stub.clientsocket.info`

---

## Malware Family Classification

1. **Malware family**: custom (Loader)
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    * **Sophisticated Anti-Analysis Suite:** The sample employs advanced techniques to evade automated sandboxes and manual analysis, specifically using `GetLastInputTime` for human interaction checks, as well as explicit functions like `DetectDebugger`, `DetectSandboxie`, and `RunAntiAnalysis`.
    * **Advanced Obfuscation Techniques:** To thwart static analysis (Ghidra/IDA), the loader utilizes "Control Flow Flattening," heavy mathematical noise in network logic, and intentional code overlap at specific offsets (`0x403dcf`) to break disassemblers.
    * **Multi-Stage Payload Protection:** The report confirms the use of AES encryption and multiple layers of complexity designed to ensure that the primary payload remains encrypted and hidden until it is "stripped away" in memory during execution.
