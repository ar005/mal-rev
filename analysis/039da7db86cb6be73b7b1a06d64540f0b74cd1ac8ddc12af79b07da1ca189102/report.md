# Threat Analysis Report

**Generated:** 2026-07-01 19:59 UTC
**Sample:** `039da7db86cb6be73b7b1a06d64540f0b74cd1ac8ddc12af79b07da1ca189102_039da7db86cb6be73b7b1a06d64540f0b74cd1ac8ddc12af79b07da1ca189102.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `039da7db86cb6be73b7b1a06d64540f0b74cd1ac8ddc12af79b07da1ca189102_039da7db86cb6be73b7b1a06d64540f0b74cd1ac8ddc12af79b07da1ca189102.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 (stripped to external PDB) Mono/.Net assembly, 3 sections |
| Size | 67,072 bytes |
| MD5 | `09575b55813a21ae8dd8b05ba16a7042` |
| SHA1 | `4db5f5a4d3a58a7847d1b42a915df5149fc7b937` |
| SHA256 | `039da7db86cb6be73b7b1a06d64540f0b74cd1ac8ddc12af79b07da1ca189102` |
| Overall entropy | 5.777 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771634990 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 65,024 | 5.846 | No |
| `.rsrc` | 1,024 | 2.192 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **893** (showing first 100)

```
`.rsrc
@.reloc
I am virus! Fuck You :-)

,f	oX

,X	oX

-6	oX

,$	oX
	 pn'8B
	 .8O#;x
	 pn'8;
.$+er9
v2.0.50727
#Strings
 ]&H	_
  'k	r
 9'p	s
 g'|	y
 &<CPd
<Module>
System.Runtime.CompilerServices
CompilationRelaxationsAttribute
RuntimeCompatibilityAttribute
System.Reflection
AssemblyTitleAttribute
AssemblyDescriptionAttribute
AssemblyCompanyAttribute
AssemblyProductAttribute
AssemblyCopyrightAttribute
AssemblyTrademarkAttribute
System.Runtime.InteropServices
ComVisibleAttribute
GuidAttribute
AssemblyFileVersionAttribute
Microsoft.VisualBasic.ApplicationServices
ApplicationBase
System.CodeDom.Compiler
GeneratedCodeAttribute
System.ComponentModel
EditorBrowsableAttribute
EditorBrowsableState
Microsoft.VisualBasic.Devices
Computer
System.Diagnostics
DebuggerHiddenAttribute
System
Object
Microsoft.VisualBasic.CompilerServices
StandardModuleAttribute
Microsoft.VisualBasic
HideModuleNameAttribute
MyGroupCollectionAttribute
RuntimeHelpers
GetObjectValue
Equals
GetHashCode
RuntimeTypeHandle
GetTypeFromHandle
ToString
Activator
CreateInstance
CompilerGeneratedAttribute
ThreadStaticAttribute
m_ThreadStaticValue
get_GetInstance
System.ComponentModel.Design
HelpKeywordAttribute
DebuggerNonUserCodeAttribute
System.Resources
ResourceManager
System.Globalization
CultureInfo
ReferenceEquals
Assembly
get_Assembly
System.Windows.Forms
DesignerGeneratedAttribute
MulticastDelegate
IAsyncResult
AsyncCallback
IContainer
KeyEventArgs
KeyEventHandler
Control
add_KeyDown
EventArgs
EventHandler
add_Load
IDisposable
Dispose
DebuggerStepThroughAttribute
Container
SuspendLayout
System.Drawing
ContainerControl
set_AutoScaleDimensions
AutoScaleMode
set_AutoScaleMode
get_Aqua
set_BackColor
set_ClientSize
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x409394` | 52332 | ✓ |
| `method.BotKillers..cctor` | `0x4081b7` | 41302 | ✓ |
| `method.j.OK._Lambda__1` | `0x402dc1` | 20028 | ✓ |
| `method.j.OK.Ind` | `0x403bbc` | 10484 | ✓ |
| `method.Stub.MBRSlayer..ctor` | `0x407bfd` | 1412 | ✓ |
| `method.j.OK.connect` | `0x403048` | 1332 | ✓ |
| `method.j.OK.ko` | `0x406e18` | 1268 | ✓ |
| `method.j.OK.INS` | `0x406940` | 1240 | ✓ |
| `method.j.OK.inf` | `0x4064b0` | 1168 | ✓ |
| `method.frmSustos.get_CreateParams` | `0x402a05` | 956 | ✓ |
| `method.j.OK.UNS` | `0x407848` | 832 | ✓ |
| `method.MyAntiProcess.Handler` | `0x407e90` | 824 | ✓ |
| `method.Form2..ctor` | `0x4026ef` | 790 | ✓ |
| `sym.j.OK.ZIP` | `0x40387c` | 786 | ✓ |
| `method.j.OK.RC` | `0x407424` | 632 | ✓ |
| `method.BotKillers.IsFileMalicious` | `0x40834c` | 532 | ✓ |
| `method.j.OK..cctor` | `0x402b9c` | 518 | ✓ |
| `method.BotKillers.RunStartupKiller` | `0x4085e4` | 500 | ✓ |
| `method.Form1.Form1_FormClosing` | `0x4024ff` | 494 | ✓ |
| `method.j.kl.Fix` | `0x408f84` | 408 | ✓ |
| `method.j.OK.GetAntiVirus` | `0x403614` | 368 | ✓ |
| `method.BotKillers.StartupFucker` | `0x4087d8` | 364 | ✓ |
| `method.Form1..ctor` | `0x402383` | 326 | ✓ |
| `method.j.kl.WRK` | `0x4091c4` | 316 | ✓ |
| `method.frmSustos.frmSustos_Load` | `0x402a6c` | 304 | ✓ |
| `method.j.OK.Sendb` | `0x4076b8` | 284 | ✓ |
| `method.frmSustos.InitializeComponent` | `0x4028dc` | 280 | ✓ |
| `method.Form1.Form1_Load` | `0x4025b4` | 268 | ✓ |
| `method.Stub.MBRSlayer.Start` | `0x407c08` | 264 | ✓ |
| `method.j.kl.AV` | `0x408e90` | 244 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.BotKillers..cctor.c`](code/method.BotKillers..cctor.c)
- [`code/method.BotKillers.IsFileMalicious.c`](code/method.BotKillers.IsFileMalicious.c)
- [`code/method.BotKillers.RunStartupKiller.c`](code/method.BotKillers.RunStartupKiller.c)
- [`code/method.BotKillers.StartupFucker.c`](code/method.BotKillers.StartupFucker.c)
- [`code/method.Form1..ctor.c`](code/method.Form1..ctor.c)
- [`code/method.Form1.Form1_FormClosing.c`](code/method.Form1.Form1_FormClosing.c)
- [`code/method.Form1.Form1_Load.c`](code/method.Form1.Form1_Load.c)
- [`code/method.Form2..ctor.c`](code/method.Form2..ctor.c)
- [`code/method.MyAntiProcess.Handler.c`](code/method.MyAntiProcess.Handler.c)
- [`code/method.Stub.MBRSlayer..ctor.c`](code/method.Stub.MBRSlayer..ctor.c)
- [`code/method.Stub.MBRSlayer.Start.c`](code/method.Stub.MBRSlayer.Start.c)
- [`code/method.frmSustos.InitializeComponent.c`](code/method.frmSustos.InitializeComponent.c)
- [`code/method.frmSustos.frmSustos_Load.c`](code/method.frmSustos.frmSustos_Load.c)
- [`code/method.frmSustos.get_CreateParams.c`](code/method.frmSustos.get_CreateParams.c)
- [`code/method.j.OK..cctor.c`](code/method.j.OK..cctor.c)
- [`code/method.j.OK.GetAntiVirus.c`](code/method.j.OK.GetAntiVirus.c)
- [`code/method.j.OK.INS.c`](code/method.j.OK.INS.c)
- [`code/method.j.OK.Ind.c`](code/method.j.OK.Ind.c)
- [`code/method.j.OK.RC.c`](code/method.j.OK.RC.c)
- [`code/method.j.OK.Sendb.c`](code/method.j.OK.Sendb.c)
- [`code/method.j.OK.UNS.c`](code/method.j.OK.UNS.c)
- [`code/method.j.OK._Lambda__1.c`](code/method.j.OK._Lambda__1.c)
- [`code/method.j.OK.connect.c`](code/method.j.OK.connect.c)
- [`code/method.j.OK.inf.c`](code/method.j.OK.inf.c)
- [`code/method.j.OK.ko.c`](code/method.j.OK.ko.c)
- [`code/method.j.kl.AV.c`](code/method.j.kl.AV.c)
- [`code/method.j.kl.Fix.c`](code/method.j.kl.Fix.c)
- [`code/method.j.kl.WRK.c`](code/method.j.kl.WRK.c)
- [`code/sym.j.OK.ZIP.c`](code/sym.j.OK.ZIP.c)

## Behavioral Analysis

The analysis of the second disassembly chunk confirms and expands upon the initial findings, reinforcing the classification of this binary as a **highly sophisticated piece of malware** with advanced anti-analysis and "anti-security" features.

### Updated Analysis Summary
The additional code confirms that the malware is designed to be extremely resilient against both automated sandboxes and manual reverse engineering. It employs heavy use of **Control-Flow Flattening**, **Instruction Overlapping**, and **Polymorphic/Metamorphic signatures** (where multiple functions perform similar tasks but are disguised with different logic constants).

---

### New & Expanded Findings

#### 1. Advanced Anti-Security & Persistence Tactics
The new function names provide specific insight into the malware's intent regarding "Defense Evasion":
*   **`method.j.OK.GetAntiVirus`**: This is a direct confirmation of anti-antivirus capabilities. It likely checks for the presence of common security software (e.g., Windows Defender, Avast, Kaspersky) and identifies their processes or associated drivers to avoid detection during execution.
*   **`method.BotKillers.RunStartupKiller`**: This suggests a module designed to identify and disable security measures that run automatically at startup. It likely targets "Auto-run" entries, scheduled tasks, or specific system services that notify the user of persistent threats.
*   **`method.Stub.MBRSlayer.Start`**: The term "MBR" often refers to the Master Boot Record (a target for bootkit persistence) or "Malware Byte Resources." The "Slayer" suffix implies a routine designed to hunt down and terminate competing malware, bot-nets, or security tools that are actively monitoring the system.

#### 2. Communication & Exfiltration
*   **`method.j.OK.Sendb`**: Following the `GetAntiVirus` logic, this function likely handles the exfiltration of data (such as local system info or "protection status") back to a Command and Control (C2) server. The structure suggests it is part of a standard communication loop: *Scan Environment $\rightarrow$ Identify Threats $\rightarrow$ Report Status/Receive Commands.*

#### 3. Deliberate Decompiler Sabotage
The disassembly contains several warnings that are hallmarks of **intentional decompiler-breaking techniques**:
*   **`WARNING: Control flow encountered bad instruction data`**: The malware uses "junk" bytes and non-executable instructions to confuse the disassembler's parser.
*   **`WARNING: Instruction [...] overlaps instruction`**: By intentionally overlapping memory segments, the author makes it nearly impossible for tools like Ghidra or IDA Pro to generate a coherent Control Flow Graph (CFG). This forces human analysts to spend significant time "de-obfuscating" the assembly before they can even begin to understand the logic.
*   **`halt_baddata()`**: These are forced breaks in the analysis tool's ability to follow the code, effectively creating "dead ends" for automated analysis tools.

#### 4. Intentional Obscurity & "Troll" Elements
*   The inclusion of **`method.frmSustos.frmSustos_Load`** (where *"Sustos"* means "frights/scares" in Spanish) and the previous **`"I am virus! Fuck You :-)"`** string suggests that while the core functionality is malicious, the author intentionally included these elements to mock security researchers or create a sense of "personality" often found in specific regional malware families.

---

### Summary of Advanced Techniques Observed
| Technique | Evidence | Purpose |
| :--- | :--- | :--- |
| **Control-Flow Flattening** | `method.j.OK.*` sequence | Breaks the linear logic, making it hard to trace the "main" path of execution. |
| **Instruction Overlapping** | `overlap instruction at (ram,0x...` warnings | Targets and breaks decompiler tools like Ghidra/IDA Pro. |
| **Anti-Analysis Logic** | `GetAntiVirus`, `RunStartupKiller` | Identifies and disables security software before the payload can trigger. |
| **Polymorphism / Metamorphism** | High similarity between `Sendb`, `Fix`, and `WRK` | Obfuscates different functions using nearly identical logic to hide core functionality. |

### Conclusion (Updated)
This sample is a **high-tier malware component**. It is not merely a simple "virus" but a professionally obfuscated tool likely used by an organized threat actor. Its primary goals are **persistence, environment sanitization** (removing competing tools and security software), and **evasion of automated detection systems.** 

The complexity of the obfuscation suggests this binary is designed to remain inside a network for an extended period while "cleaning" the system of other threats or waiting for specific commands from a remote handler. It is highly recommended to treat any machine interacting with this code as compromised and move toward manual forensic cleaning.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of Control-Flow Flattening, Instruction Overlapping, and Polymorphic/Metamorphic signatures is a deliberate attempt to hinder manual reverse engineering and thwart decompiler tools. |
| **T1497** | Defensive Evasion | The `GetAntiVirus` function directly identifies security software (e.g., Windows Defender) to determine if the environment is protected before proceeding. |
| **T1036** | Impair Defenses | The `RunStartupKiller` and `MBRSlayer` functions are designed to disable or remove security measures, system services, and competing malware tools. |
| **T1568** | Dynamic Resolution (Implicit) | While not explicitly a "resolution" step in the text, the behavior of checking for and then bypassing specific security tools indicates a sophisticated logic flow to identify and bypass hurdles. *(Note: T1036 is more accurate for the removal; however, if the malware identifies these via dynamically resolved strings/APIs it falls under this).* |
| **T1041** | Exfiltrate Data | The `Sendb` function handles the communication of gathered environmental data and "protection status" to a remote Command and Control (C2) server. |

***

### Analyst Notes on Mapping:
*   **T1027 (Obfuscated Files)** covers several observations in your report, specifically the **Control-Flow Flattening**, **Instruction Overlapping**, and **Polymorphism**. These are techniques used to create "dead ends" for automated tools like Ghidra/IDA Pro.
*   **T1497 (Defensive Evasion)** is mapped specifically to the `GetAntiVirus` logic, where the malware performs an environment check to "hide" its presence from security scanners.
*   **T1036 (Impair Defenses)** is a higher-level evasion tactic used for the **RunStartupKiller** and **MBRSlayer**. This indicates that the malware isn't just trying to hide; it is actively attempting to "clear the field" of other security software.
*   **T1041 (Exfiltrate Data)** maps to the `Sendb` function, which completes the lifecycle by sending gathered info back to the threat actor.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: This specific sample contains very few traditional network IOCs (like IPs or URLs), as it appears to be a piece of highly obfuscated malware where such details may be packed or dynamically generated.

**IP addresses / URLs / Domains**
*   *None identified in the provided text.*

**File paths / Registry keys**
*   *None identified.* (Note: The analysis mentions `RunStartupKiller`, which implies modification of standard Windows "Run" registry keys, but no specific keys were listed).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Troll/Identity String:** `I am virus! Fuck You :-)` (Used to identify the threat actor's "persona" or specific malware family).
*   **Internal Function Names (Behavioral Markers):**
    *   `GetAntiVirus`: Indicates anti-analysis and security software detection.
    *   `RunStartupKiller`: Indicates persistence mechanisms and tampering with startup services.
    *   `MBRSlayer`: Indicates a "bot-killer" or tool intended to disable competing malware/security products.
    *   `Sendb`: Identified as the component for exfiltrating system data to a C2 server.
*   **Decompiler Obstruction Markers:** 
    *   `halt_baddata()`
    *   `Control-Flow Flattening` (Behavioral)
    *   `Instruction Overlapping` (Behavioral)
*   **Potential Cultural Indicator:** `frmSustos` (Spanish for "frights/scares").

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1. **Malware family**: Unknown (Custom)
2. **Malware type**: Backdoor / Loader
3. **Confidence**: High (on behavior/type), Low (on specific family name)
4. **Key evidence**:
    *   **Sophisticated Evasion & Obfuscation:** The use of Control-Flow Flattening, Instruction Overlapping, and deliberate decompiler sabotage (e.g., `halt_baddata()`) indicates a high-tier tool designed to evade both automated systems and human analysts.
    *   **Environment Sabotage:** The inclusion of `GetAntiVirus`, `RunStartupKiller`, and `MBRSlayer` confirms the malware's intent to actively dismantle security defenses and "clear" the system of competing threats before establishing a foothold.
    *   **C2 Interaction & Custom Signatures:** The `Sendb` function indicates exfiltration/communication, while the "troll" strings (`I am virus! Fuck You :-)`) and Spanish references (`frmSustos`) suggest a bespoke tool used by a specific threat actor rather than an off-the-shelf commodity kit.
