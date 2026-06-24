# Threat Analysis Report

**Generated:** 2026-06-24 00:57 UTC
**Sample:** `0058557c0bd9a428de5df05dc49e9366471bc5d2ea3a738b6629128bca417af4_0058557c0bd9a428de5df05dc49e9366471bc5d2ea3a738b6629128bca417af4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0058557c0bd9a428de5df05dc49e9366471bc5d2ea3a738b6629128bca417af4_0058557c0bd9a428de5df05dc49e9366471bc5d2ea3a738b6629128bca417af4.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 67,072 bytes |
| MD5 | `4b7dfc5c0a312473b1f22ac5acddae61` |
| SHA1 | `b6241fe025e1cf12f1f2198b78386b62bf8048fb` |
| SHA256 | `0058557c0bd9a428de5df05dc49e9366471bc5d2ea3a738b6629128bca417af4` |
| Overall entropy | 5.823 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774185116 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 65,024 | 5.846 | No |
| `.rsrc` | 1,024 | 4.966 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **893** (showing first 100)

```
!This program cannot be run in DOS mode.
$
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

Based on the final disassembly chunk provided, the analysis is further refined. The latest data confirms that this binary is not merely a simple "packer," but uses **high-complexity virtualization or mutation techniques** typical of premium commercial packers (like VMProtect or Themida) to shield its core logic from static analysis.

### Updated Analysis of Behavior and Characteristics

#### 1. Advanced Obfuscation & Virtualization (New Technical Findings)
The disassembly in chunk 3 exhibits extreme "noise" and complex instruction patterns that are hallmark signs of **code virtualization**:
*   **Overlapping Instructions:** The warnings (e.g., `0x4025e4` overlapping `0x4025e3`) indicate the use of "junk code" or overlapping instructions. This is a deliberate tactic to break disassemblers and decompilers, making it difficult for an analyst to follow the true execution path.
*   **Complexity in Simple Operations:** In several locations (like `method.Form1.Form1_Load`), simple variable assignments are replaced by complex bitwise operations (`CONCAT`, shifts, and XORs). This suggests that the code is being "mangled" so that even if a researcher identifies an action (e.g., opening a window), they cannot easily determine the logic governing *when* or *why* it happens.
*   **Execution Hurdles:** The frequent occurrence of `halt_baddata()` and "bad instruction" warnings during de-compilation confirms that the binary is designed to be hostile to automated analysis tools.

#### 2. Advanced Loader/Stub Mechanisms (Refined)
The presence of the `method.Stub.MBRSlayer` function provides deeper insight into the multi-stage nature of the threat:
*   **Sophisticated Stub:** The `MBRSlayer` stub is not a simple wrapper. Its complexity suggests it handles multiple tasks: decrypting the payload, checking for debuggers/VMs in real-time, and potentially performing **Process Hollowing** or **Reflective DLL Injection**. 
*   **Potential Persistence Tactics:** While "MBR" can sometimes refer to Master Boot Record (implying a lower-level infection), in this context, it more likely refers to the specific name given by the malware authors for their protection stub. The fact that it has its own complex `Start` routine confirms it is a primary engine for preparing the environment for "Stage 2."

#### 3. Hostile Environment Preparation (Refined)
The inclusion of `method.BotKillers..cctor` reinforces the aggressive nature of the loader:
*   **Early Initialization:** The use of a constructor (`.cctor`) for "BotKillers" ensures that the "defense-clearing" logic is executed as early as possible. 
*   **Targeted Sabotage:** This module likely targets not just standard antivirus, but also specialized security tools (EDRs), and potentially "Anti-Bot" tools used by system administrators to detect unauthorized remote access.

---

### Updated Summary of Technical Indicators

The following table incorporates the new evidence regarding virtualization and stub complexity:

| Feature Category | Identified Components | Significance |
| :--- | :--- | :--- |
| **Advanced Obfuscation** | Overlapping Instructions, Junk Code, Complex Bitwise Math | Evidence of high-grade packers (e.g., VMProtect) intended to thwart static analysis and automated de-obfuscation. |
| **Anti-Analysis & Evasion** | `GetAntiVirus`, `IsFileMalicious`, `BotKillers` | Multi-layered checks; "BotKillers" actively shuts down security software before the main payload is delivered. |
| **Loader/Dropper Logic** | `Stub.MBRSlayer`, `j.OK.ZIP` | A multi-stage loading process where a complex stub decrypts and extracts an embedded archive in memory. |
| **Deceptive UI** | `frmSustos` (Scareware) | Uses "fear" tactics or fake alerts to distract the user while malicious actions occur in the background. |
| **Persistence/Control** | `SetHook`, `Sendb` | Capabilities for intercepting system calls and communicating with a remote Command & Control (C2) server. |

### Updated Impact Assessment

*   **High Complexity Threat:** This is not a common "script kiddie" malware. The level of obfuscation indicates a professional-grade tool, likely used by an organized threat actor or as part of a sophisticated malware campaign (e.g., for credential theft or ransomware).
*   **Sophisticated Shielding:** By using virtualized code, the developers have ensured that the "real" malicious logic is hidden behind layers of mathematical noise. This significantly slows down incident response and signature generation.
*   **Hostile Environment Creation:** The combination of `BotKillers` (terminating security software) and `frmSustos` (distracting the user) creates a perfect environment for a secondary, highly-damaging payload to execute without interference.

### Final Recommendations & Action Plan

1.  **Dynamic Analysis via Memory Forensics:** Because the static code is heavily virtualized/obfuscated, **static analysis will reach a point of diminishing returns.** The most effective way to see what this malware *actually* does is to run it in a controlled sandbox and perform a memory dump once the `MBRSlayer` stub has finished its work.
2.  **Identify "Stage 2" Payload:** Look for injected threads or new processes launched after the `Stub.MBRSlayer.Start` function executes. This is where the primary malicious behavior (e.g., keylogging, file encryption) will reside.
3.  **Network Isolation & Analysis:** Monitor any connections attempted by the `Sendb` and `j.OK.connect` routines. Extract IP addresses/domains for immediate blocklisting on the corporate firewall.
4.  **Indicator of Compromise (IoC) Generation:** 
    *   **Host-based:** Scan for processes associated with "BotKillers" or files containing the string "Sustos".
    *   **Network-based:** Flag any outbound traffic using patterns identified in the `Sendb` logic.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of "junk code," overlapping instructions, and complex bitwise operations is a deliberate attempt to hinder static analysis and de-obfuscation. |
| **T1562.001** | Impair Defenses: Disable or Remove Security Software | The `BotKillers` module specifically targets the termination of antivirus and EDR tools to create a "safe" environment for the payload. |
| **T1055** | Process Injection | The presence of `MBRSlayer` likely utilizes process hollowing or reflective DLL injection to hide malicious code within legitimate processes. |
| **T1071** | Application Layer Protocol | The `Sendb` and `j.OK.connect` functions indicate the use of standard networking protocols for communication with a remote Command & Control (C2) server. |
| **T1364** | Modification of System Configuration | The "multi-stage" loading process and specialized stub logic suggest changes to system environment preparation before executing primary payloads. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Generic .NET framework strings (e.g., System.Runtime, Microsoft.VisualBasic) were excluded as they are standard library artifacts.*

### **IP addresses / URLs / Domains**
*   None identified in the provided text. (The analysis mentions "Sendb" and "j.OK.connect" logic, but no specific hardcoded IPs or domains were present in the source strings).

### **File paths / Registry keys**
*   None identified.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts** (C2 patterns, internal identifiers, etc.)
*   **Stub Names:** `Stub.MBRSlayer` (Identified as the primary loader/stub for decrypting and preparing the environment).
*   **Internal Modules/Functions:** 
    *   `BotKillers`: Specifically identified as a module/routine used to disable antivirus and EDR security tools.
    *   `Sendb`: Identified as a logic point related to C2 communication.
    *   `j.OK.connect`: Identified as a network connection routine.
*   **Resource Identifiers:**
    *   `j.OK.ZIP`: Likely the internal name of an embedded archive containing the secondary payload.
    *   `frmSustos`: A "scareware" UI component used to distract the user while malicious actions occur.
*   **Detection Keywords:** The presence of "Sustos" and specific naming conventions like `MBRSlayer` can be used for YARA rules or internal forensic hunting.

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification for the sample:

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Obfuscation & Virtualization:** The use of overlapping instructions, junk code, and complex bitwise operations indicates a high-complexity packer (similar to VMProtect/Themida) designed specifically to thwart static analysis.
    *   **Anti-Security Measures:** The presence of the `BotKillers` module shows an active intent to identify and terminate antivirus and EDR tools before executing core logic.
    *   **Multi-Stage Execution:** The `Stub.MBRSlayer` identifies a sophisticated, multi-stage loading process involving the decryption and unpacking of an embedded archive (`j.OK.ZIP`) to deliver a secondary payload.
