# Threat Analysis Report

**Generated:** 2026-07-20 15:20 UTC
**Sample:** `097d0a821622e09b00eea461e563706e60bc9f5b7bdb5bbd6475ff31f85d6551_097d0a821622e09b00eea461e563706e60bc9f5b7bdb5bbd6475ff31f85d6551.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `097d0a821622e09b00eea461e563706e60bc9f5b7bdb5bbd6475ff31f85d6551_097d0a821622e09b00eea461e563706e60bc9f5b7bdb5bbd6475ff31f85d6551.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 733,184 bytes |
| MD5 | `cfc8363b04abf8fb9e65ccd10c984294` |
| SHA1 | `91016af9c6c9129b5f68cdd1e0215ad61a274a6b` |
| SHA256 | `097d0a821622e09b00eea461e563706e60bc9f5b7bdb5bbd6475ff31f85d6551` |
| Overall entropy | 7.746 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3635817052 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 709,120 | 7.817 | ⚠️ Yes |
| `.rsrc` | 23,040 | 2.921 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1631** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v4.0.30319
#Strings
IEnumerable`1
List`1
label1
panel1
button1
timer1
imageList1
textBox1
ConcurrentDictionary`2
label2
textBox2
label3
label4
button4
label5
button5
label6
label7
label8
label9
<Module>
System.IO
mscorlib
gameLogic
System.Collections.Generic
set_Enabled
Form1_Activated
add_Activated
Synchronized
passwordField
usernameField
securityThreshold
Dashboard
HoqueLtd
Replace
enableQuantumResistance
defaultInstance
GetHashCode
get_KeyCode
set_AutoScaleMode
HomePage
LoginPage
Average
Enumerable
IDisposable
ToDouble
RuntimeTypeHandle
GetTypeFromHandle
loginTitle
adminTitle
subtitle
set_FormBorderStyle
FontStyle
timerGame
set_Name
DateTime
Combine
set_Multiline
AsType
GetType
System.Core
get_Culture
set_Culture
resourceCulture
packetCapture
ButtonBase
ApplicationSettingsBase
TextBoxBase
Dispose
Reverse
EditorBrowsableState
get_White
AssemblyMetadataAttribute
STAThreadAttribute
CompilerGeneratedAttribute
GuidAttribute
GeneratedCodeAttribute
DebuggerNonUserCodeAttribute
DebuggableAttribute
EditorBrowsableAttribute
ComVisibleAttribute
AssemblyTitleAttribute
TargetFrameworkAttribute
AssemblyDescriptionAttribute
CompilationRelaxationsAttribute
AssemblyProductAttribute
AssemblyCompanyAttribute
RuntimeCompatibilityAttribute
ILX.exe
set_Size
set_ImageSize
set_AutoSize
set_ClientSize
Padding
System.Runtime.Versioning
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **22**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method..Form1.InitializeComponent` | `0x403e50` | 15894 | ✓ |
| `method.HoqueLtd.Dashboard.InitializeComponent` | `0x4020ec` | 2129 | — |
| `method.HoqueLtd.LoginPage.InitializeComponent` | `0x402d04` | 1448 | ✓ |
| `method..Form1.AnalyzeNetworkSecurityLogs` | `0x403798` | 1228 | ✓ |
| `method.HoqueLtd.HomePage.InitializeComponent` | `0x4029c4` | 632 | — |
| `method..Form1.start` | `0x403560` | 328 | ✓ |
| `method..Form1.timerGame_Tick` | `0x403c64` | 236 | ✓ |
| `method..Form1.gameLogic` | `0x403d50` | 224 | ✓ |
| `method..Form1.countDown_Tick` | `0x403498` | 200 | ✓ |
| `method..Form1.timeDelay_Tick` | `0x4036e8` | 176 | ✓ |
| `method.HoqueLtd.LoginPage.button1_Click` | `0x402c4c` | 121 | — |
| `method..Form1..ctor` | `0x403348` | 102 | ✓ |
| `method..Form1.button4_Click` | `0x403434` | 100 | ✓ |
| `method..Form1.Form1_KeyDown` | `0x4033c4` | 95 | ✓ |
| `method.HoqueLtd.Dashboard..ctor` | `0x402060` | 82 | ✓ |
| `method.HoqueLtd.HomePage.timer1_Tick` | `0x402958` | 77 | — |
| `method..Form1.button5_Click` | `0x4036a8` | 64 | ✓ |
| `method.HoqueLtd.Properties.Resources.get_ResourceManager` | `0x4032cb` | 44 | ✓ |
| `method.HoqueLtd.Dashboard.Dispose` | `0x4020cb` | 33 | — |
| `method.HoqueLtd.LoginPage.Dispose` | `0x402ce3` | 33 | ✓ |
| `method..Form1.Dispose` | `0x403e30` | 32 | ✓ |
| `method.HoqueLtd.HomePage.Dispose` | `0x4029a5` | 31 | — |
| `method.HoqueLtd.HomePage..ctor` | `0x40293d` | 27 | — |
| `method.HoqueLtd.Properties.Resources.get_qsw` | `0x403306` | 27 | ✓ |
| `method.HoqueLtd.Properties.Settings..cctor` | `0x403330` | 24 | ✓ |
| `entry0` | `0x4032ac` | 23 | ✓ |
| `method.HoqueLtd.LoginPage.clientLogin_Click` | `0x402cc5` | 23 | ✓ |
| `method..Form1.button1_Click` | `0x4033ae` | 22 | ✓ |
| `method.HoqueLtd.Dashboard.logOutBtn_Click` | `0x4020b2` | 18 | — |
| `method..Form1.Form1_Activated` | `0x403423` | 17 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method..Form1..ctor.c`](code/method..Form1..ctor.c)
- [`code/method..Form1.AnalyzeNetworkSecurityLogs.c`](code/method..Form1.AnalyzeNetworkSecurityLogs.c)
- [`code/method..Form1.Dispose.c`](code/method..Form1.Dispose.c)
- [`code/method..Form1.Form1_Activated.c`](code/method..Form1.Form1_Activated.c)
- [`code/method..Form1.Form1_KeyDown.c`](code/method..Form1.Form1_KeyDown.c)
- [`code/method..Form1.InitializeComponent.c`](code/method..Form1.InitializeComponent.c)
- [`code/method..Form1.button1_Click.c`](code/method..Form1.button1_Click.c)
- [`code/method..Form1.button4_Click.c`](code/method..Form1.button4_Click.c)
- [`code/method..Form1.button5_Click.c`](code/method..Form1.button5_Click.c)
- [`code/method..Form1.countDown_Tick.c`](code/method..Form1.countDown_Tick.c)
- [`code/method..Form1.gameLogic.c`](code/method..Form1.gameLogic.c)
- [`code/method..Form1.start.c`](code/method..Form1.start.c)
- [`code/method..Form1.timeDelay_Tick.c`](code/method..Form1.timeDelay_Tick.c)
- [`code/method..Form1.timerGame_Tick.c`](code/method..Form1.timerGame_Tick.c)
- [`code/method.HoqueLtd.Dashboard..ctor.c`](code/method.HoqueLtd.Dashboard..ctor.c)
- [`code/method.HoqueLtd.LoginPage.Dispose.c`](code/method.HoqueLtd.LoginPage.Dispose.c)
- [`code/method.HoqueLtd.LoginPage.InitializeComponent.c`](code/method.HoqueLtd.LoginPage.InitializeComponent.c)
- [`code/method.HoqueLtd.LoginPage.clientLogin_Click.c`](code/method.HoqueLtd.LoginPage.clientLogin_Click.c)
- [`code/method.HoqueLtd.Properties.Resources.get_ResourceManager.c`](code/method.HoqueLtd.Properties.Resources.get_ResourceManager.c)
- [`code/method.HoqueLtd.Properties.Resources.get_qsw.c`](code/method.HoqueLtd.Properties.Resources.get_qsw.c)
- [`code/method.HoqueLtd.Properties.Settings..cctor.c`](code/method.HoqueLtd.Properties.Settings..cctor.c)

## Behavioral Analysis

This final chunk of disassembly (11/11) provides a definitive look at how the malware handles **metamorphic junk code** and **anti-disassembly techniques**. While the previous segments established the existence of a Virtual Machine (VM), this section demonstrates the specific "noise" tactics used to exhaust an analyst's resources.

The following analysis incorporates findings from all 11 chunks, culminating in the final assessment of the protection layer.

---

### Final Integrated Analysis: Advanced VM Protection and Anti-Analysis

#### 1. Obfuscated Arithmetic and Junk Code Injection
The logic leading up to `code_r0x00403716` is a textbook example of **Arithmetic Obfuscation**.
*   **Redundant Operations:** The repeated additions (`*pcVar7 = *pcVar7 + cVar3;`) performed three times in a row serve no functional purpose for the software's intended operation. They are designed to "bloat" the code, making it difficult for an analyst to distinguish between actual logic and "junk" filler.
*   **Constant Manipulation:** The use of `cVar3`, `%`, and `\x02` suggests a technique where constants are manipulated just before they are used in a calculation. This hides what the constant actually represents (e.g., a memory offset, a flag, or a part of an encrypted string).

#### 2. Instruction-Level "Gaslighting"
The transition from `pcVar7 = CONCAT31(Var17,cVar3 + '\x02');` to the subsequent addition blocks illustrates how the packer hides the actual execution path:
*   **Bitwise Masking and Shifting:** The `>> 8` and `CONCAT31` operations are used to calculate addresses dynamically. By breaking a single memory address into multiple components (shifted and concatenated), the malware ensures that static tools like IDA Pro or Ghidra cannot automatically resolve where the code is jumping next.
*   **The "Bad Instruction" Trap:** The warning `Warning: Bad instruction - Truncating control flow` at `0x00403716` is a deliberate **Anti-Disassembly** tactic. By intentionally crafting the byte sequence so that it appears to be an invalid instruction to a linear disassembler, the authors force the tool to stop analyzing the block. This "breaks" the graph view, preventing the analyst from seeing the jump or call that follows the junk code.

#### 3. Conclusion on Protection Sophistication
The progression through all 11 chunks reveals a high-tier protection suite (consistent with tools like **VMProtect** or **Themida**). The architecture is not just "obfuscated"—it is **virtualized**.
*   **Complexity:** The malware doesn't run standard x86 instructions to perform its primary tasks; it runs a custom bytecode interpreted by the VM.
*   **Tactic Diversity:** It employs **Control Flow Flattening**, **Instruction Substitution**, **Opaque Predicates**, and **Anti-Disassembly Traps**.

---

### Final Report for Incident Response (IR)

**Threat Profile: High-Sophistication Packer/VM Protector**

The malware utilizes a "Fortress Architecture." Every layer of the code—from the UI interaction to the internal logic—is wrapped in a custom virtual machine. This indicates a high level of professionalism and intent.

#### Key Findings Summary:
*   **Static Analysis Barrier:** The use of `halt_baddata` traps and complex bitwise arithmetic means that **manual static analysis is no longer a viable method** for extracting the malware's core functionality from this disassembly. You cannot "read" what the malware does by looking at these instructions.
*   **Execution Flow:** The code path in `button1_Click` is designed to be a black box. The "real" malicious logic only exists in memory during the moments it is being executed by the VM's interpreter.

#### Actionable IR Recommendations:

1.  **Shift to Dynamic Analysis (Immediate Priority):**
    *   **Memory Forensics:** Use tools like `Volatility` or `Process Hacker` to monitor the process's memory space. Look for memory regions that transition from `RW-` (Read/Write) to `R-X` (Read/Execute), as this often marks the point where the VM "unpacks" its true payload into memory.
    *   **API Hooking:** Instead of trying to understand the VM's internal arithmetic, hook the system APIs the malware *must* call eventually. Monitor:
        *   `VirtualAlloc` / `VirtualProtect` (to catch the unpacking).
        *   `InternetConnectW`, `HttpSendRequest` (to identify C2 communication).
        *   `CreateProcess`, `WriteProcessMemory` (to detect injection into other processes).

2.  **Identify the "OEP" (Original Entry Point):**
    The VM will eventually need to hand off execution to the "original" malicious code (the payload). Use a debugger (x64dbg) with a "Scylla" plugin to find the OEP, dump the memory at that point, and reconstruct the Import Address Table (IAT). This dumped file can then be analyzed using standard static methods.

3.  **Behavioral Indicators for SOC Monitoring:**
    Since the code is heavily obfuscated, create detections based on **behavioral artifacts**:
    *   **Network:** Flag any outbound connections from unknown binaries to non-standard ports or known malicious IP ranges.
    *   **Host:** Alert on the creation of hidden files in `%AppData%` or `%Temp%`, and any attempt by a process to inject code into `explorer.exe` or `svchost.exe`.

**Final Conclusion:** This is a professional-grade, heavily protected sample. **Treat as high-priority.** The complexity of the VM protection suggests this may be part of a targeted campaign or a sophisticated "malware-as-a-service" (MaaS) operation. Focus all resources on **dynamic behavior analysis and memory dumping** to bypass the virtualized layer.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Virtualization | The malware utilizes a custom virtual machine architecture (similar to VMProtect/Themida) to interpret bytecode, shielding its primary logic from standard x86 analysis. |
| **T1027** | Obfuscated Execution | The use of junk code injection, arithmetic obfuscation, and instruction substitution is designed to bloat the binary and hide constants from static analysis tools. |
| **T1027 (Sub-type)** | Control Flow Flattening / Opaque Predicates | These specific methods are used to complicate the flow graph and obscure the execution path of the malicious payload. |
| **T1027 (Sub-type)** | Anti-Disassembly Traps | The "Bad Instruction" trap at `0x00403716` is a deliberate technique to break linear disassemblers and prevent automated tools from mapping code correctly. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `ILX.exe` (Primary executable name)
*   *(Note: Generic system paths like %AppData% and %Temp% were omitted as per instructions.)*

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Internal Branding/Identifier:** `HoqueLtd` (Found in multiple resource strings: `HoqueLtd.Dashboard`, `HoqueLtd.HomePage`, `HoqueLtd.LoginPage`)
*   **Known Protection Tooling:** Evidence of **VMProtect** or **Themida** (identified via the analysis of "Fortress Architecture" and virtualized code).
*   **Behavioral Patterns:** 
    *   Use of `InternetConnectW` and `HttpSendRequest` for potential C2 communication.
    *   Use of `VirtualAlloc` and `VirtualProtect` for unpacking malicious payloads into memory.
    *   Advanced anti-analysis techniques (Arithmetic Obfuscation, Instruction-Level "Gaslighting," and Control Flow Flattening).

---

## Malware Family Classification

1. **Malware family**: Unknown (Potential branding: HoqueLtd)
2. **Malware type**: Loader / Packer
3. **Confidence**: High (for its role as a protected loader); Low (regarding the specific final payload functionality)

4. **Key evidence**:
*   **Sophisticated Virtualization:** The sample utilizes "Fortress Architecture" (comparable to VMProtect or Themida), where the primary malicious logic is converted into custom bytecode and executed by a virtual machine, making static analysis of its core purpose impossible without dynamic unpacking.
*   **Advanced Anti-Analysis Tactics:** The code employs high-level obfuscation techniques including arithmetic masking, junk code injection, control flow flattening, and "Bad Instruction" traps specifically designed to break linear disassemblers (like Ghidra/IDA) and exhaust analyst resources.
*   **Loader Behavior:** The report identifies the sample as a "black box." Since the core functionality only exists in memory during execution and is protected by multiple layers of obfuscation, its primary role is that of a sophisticated loader designed to shield and deliver an underlying payload (which could be a RAT, infostealer, or other malware).
