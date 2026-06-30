# Threat Analysis Report

**Generated:** 2026-06-30 00:50 UTC
**Sample:** `03738c27c94377feef5f7ef65a9bc09c7ce125af80ab97132a7c6fd257929154_03738c27c94377feef5f7ef65a9bc09c7ce125af80ab97132a7c6fd257929154.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `03738c27c94377feef5f7ef65a9bc09c7ce125af80ab97132a7c6fd257929154_03738c27c94377feef5f7ef65a9bc09c7ce125af80ab97132a7c6fd257929154.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 887,304 bytes |
| MD5 | `008970e24250fd3992ce9dd2ecfe7f5a` |
| SHA1 | `c774cd3b66f3c0905c890ef04b5bcf2221d12b9c` |
| SHA256 | `03738c27c94377feef5f7ef65a9bc09c7ce125af80ab97132a7c6fd257929154` |
| Overall entropy | 7.817 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2935796568 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 723,968 | 7.778 | ⚠️ Yes |
| `.rsrc` | 147,456 | 7.974 | ⚠️ Yes |
| `.reloc` | 1,024 | 0.056 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **2169** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v4.0.30319
#Strings
label10
button10
columnHeader10
<.cctor>b__38_0
<>9__19_0
<NebulousHarbor>b__19_0
BtnOda101
label11
button11
columnHeader11
button4_Click_1
Func`1
IEnumerable`1
ThreadLocal`1
List`1
linkLabel1
label1
button1
LblFaturalar1
columnHeader1
timer1
webBrowser1
axWindowsMediaPlayer1
Pansiyon_kay
listView1
comboBox1
groupBox1
richTextBox1
textBox1
BtnOda102
label12
button12
ToInt32
Func`2
linkLabel2
label2
button2
LblFaturalar2
columnHeader2
veriler2
Btnkaydet2
listView2
groupBox2
BtnOda103
Func`3
linkLabel3
label3
button3
LblFaturalar3
columnHeader3
BtnOda104
label4
button4
columnHeader4
BtnOda105
label5
button5
columnHeader5
BtnOda106
ToInt16
label6
button6
columnHeader6
BtnOda107
label7
button7
columnHeader7
BtnOda108
label8
button8
columnHeader8
BtnOda109
label9
button9
columnHeader9
<Module>
System.IO
get_Fuchsia
nebula
BtnAra
get_sa
System.Data
AxInterop.WMPLib
AxWMPLib
mscorlib
System.Collections.Generic
Lblsonuc
get_CanRead
add_Load
FrmYeniM
steri_Load
FrmAnaForm_Load
FrmOdalar_Load
FrmMesajlar_Load
FrmStoklar_Load
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Pansiyon_kayt1.Properties.Settings.get_Default` | `0x40b8fe` | 43294 | ✓ |
| `method.__c._.cctor_b__38_0` | `0x40b947` | 23460 | ✓ |
| `method.Pansiyon_kayt1.FrmMsteriler.button1_Click` | `0x404589` | 7850 | ✓ |
| `method.Pansiyon_kayt1.FrmYeniMsteri.Dispose` | `0x4090a3` | 6972 | ✓ |
| `method.Pansiyon_kayt1.FrmYeniMsteri.InitializeComponent` | `0x4090c4` | 6078 | ✓ |
| `method.Pansiyon_kayt1.FrmMsteriler.InitializeComponent` | `0x404d84` | 5852 | ✓ |
| `method.Pansiyon_kayt1.FrmAnaForm.button10_Click` | `0x40273d` | 4540 | ✓ |
| `method.Pansiyon_kayt1.FrmAnaForm.InitializeComponent` | `0x402b4c` | 3612 | ✓ |
| `method.Pansiyon_kayt1.FrmStoklar.InitializeComponent` | `0x407720` | 3360 | ✓ |
| `method.Pansiyon_kayt1.FrmStoklar.Dispose` | `0x407701` | 3340 | ✓ |
| `method.Pansiyon_kayt1.FrmGelirGider.Dispose` | `0x40abdf` | 3194 | ✓ |
| `method.Pansiyon_kayt1.FrmGelirGider.InitializeComponent` | `0x40ac00` | 3184 | ✓ |
| `method.Pansiyon_kayt1.FrmMzik.Dispose` | `0x406441` | 2318 | ✓ |
| `method.Pansiyon_kayt1.FrmYeniMsteri.BtnBo_Click` | `0x408905` | 1950 | ✓ |
| `method.Pansiyon_kayt1.FrmOdalar.InitializeComponent` | `0x406d70` | 1768 | ✓ |
| `method.Pansiyon_kayt1.FrmOdalar.Dispose` | `0x406d4f` | 1766 | ✓ |
| `method.Pansiyon_kayt1.FrmMesajlar.Dispose` | `0x403f03` | 1670 | ✓ |
| `method.Pansiyon_kayt1.FrmYeniMsteri.FrmYeniMsteri_Load` | `0x408acc` | 1528 | ✓ |
| `method.Pansiyon_kayt1.FrmOdalar.FrmOdalar_Load` | `0x4067e4` | 1420 | ✓ |
| `method.Pansiyon_kayt1.FrmAdminGiris.InitializeComponent` | `0x402168` | 1271 | ✓ |
| `method.Pansiyon_kayt1.FrmYeniMsteri.BtnDolu_Click` | `0x408433` | 1234 | ✓ |
| `method.Pansiyon_kayt1.FrmMesajlar.InitializeComponent` | `0x403f24` | 1216 | ✓ |
| `method.Pansiyon_kayt1.FrmGazeteler.InitializeComponent` | `0x403968` | 1112 | ✓ |
| `method.Pansiyon_kayt1.FrmGazeteler.Dispose` | `0x403949` | 1110 | ✓ |
| `method.Pansiyon_kayt1.FrmMzik.InitializeComponent` | `0x406460` | 868 | ✓ |
| `method.Pansiyon_kayt1.FrmAnaForm.NebulousHarbor` | `0x4027d0` | 860 | ✓ |
| `method.Pansiyon_kayt1.FrmMsteriler.BtnSil_Click` | `0x4048ac` | 700 | ✓ |
| `method.Pansiyon_kayt1.FrmGelirGider.FrmGelirGider_Load` | `0x40a974` | 652 | ✓ |
| `method.Pansiyon_kayt1.FrmStoklar.listView1_SelectedIndexChanged` | `0x407453` | 526 | ✓ |
| `method.Pansiyon_kayt1.FrmMsteriler.listView1_DoubleClick` | `0x404594` | 456 | ✓ |

### Decompiled Code Files

- [`code/method.Pansiyon_kayt1.FrmAdminGiris.InitializeComponent.c`](code/method.Pansiyon_kayt1.FrmAdminGiris.InitializeComponent.c)
- [`code/method.Pansiyon_kayt1.FrmAnaForm.InitializeComponent.c`](code/method.Pansiyon_kayt1.FrmAnaForm.InitializeComponent.c)
- [`code/method.Pansiyon_kayt1.FrmAnaForm.NebulousHarbor.c`](code/method.Pansiyon_kayt1.FrmAnaForm.NebulousHarbor.c)
- [`code/method.Pansiyon_kayt1.FrmAnaForm.button10_Click.c`](code/method.Pansiyon_kayt1.FrmAnaForm.button10_Click.c)
- [`code/method.Pansiyon_kayt1.FrmGazeteler.Dispose.c`](code/method.Pansiyon_kayt1.FrmGazeteler.Dispose.c)
- [`code/method.Pansiyon_kayt1.FrmGazeteler.InitializeComponent.c`](code/method.Pansiyon_kayt1.FrmGazeteler.InitializeComponent.c)
- [`code/method.Pansiyon_kayt1.FrmGelirGider.Dispose.c`](code/method.Pansiyon_kayt1.FrmGelirGider.Dispose.c)
- [`code/method.Pansiyon_kayt1.FrmGelirGider.FrmGelirGider_Load.c`](code/method.Pansiyon_kayt1.FrmGelirGider.FrmGelirGider_Load.c)
- [`code/method.Pansiyon_kayt1.FrmGelirGider.InitializeComponent.c`](code/method.Pansiyon_kayt1.FrmGelirGider.InitializeComponent.c)
- [`code/method.Pansiyon_kayt1.FrmMesajlar.Dispose.c`](code/method.Pansiyon_kayt1.FrmMesajlar.Dispose.c)
- [`code/method.Pansiyon_kayt1.FrmMesajlar.InitializeComponent.c`](code/method.Pansiyon_kayt1.FrmMesajlar.InitializeComponent.c)
- [`code/method.Pansiyon_kayt1.FrmMsteriler.BtnSil_Click.c`](code/method.Pansiyon_kayt1.FrmMsteriler.BtnSil_Click.c)
- [`code/method.Pansiyon_kayt1.FrmMsteriler.InitializeComponent.c`](code/method.Pansiyon_kayt1.FrmMsteriler.InitializeComponent.c)
- [`code/method.Pansiyon_kayt1.FrmMsteriler.button1_Click.c`](code/method.Pansiyon_kayt1.FrmMsteriler.button1_Click.c)
- [`code/method.Pansiyon_kayt1.FrmMsteriler.listView1_DoubleClick.c`](code/method.Pansiyon_kayt1.FrmMsteriler.listView1_DoubleClick.c)
- [`code/method.Pansiyon_kayt1.FrmMzik.Dispose.c`](code/method.Pansiyon_kayt1.FrmMzik.Dispose.c)
- [`code/method.Pansiyon_kayt1.FrmMzik.InitializeComponent.c`](code/method.Pansiyon_kayt1.FrmMzik.InitializeComponent.c)
- [`code/method.Pansiyon_kayt1.FrmOdalar.Dispose.c`](code/method.Pansiyon_kayt1.FrmOdalar.Dispose.c)
- [`code/method.Pansiyon_kayt1.FrmOdalar.FrmOdalar_Load.c`](code/method.Pansiyon_kayt1.FrmOdalar.FrmOdalar_Load.c)
- [`code/method.Pansiyon_kayt1.FrmOdalar.InitializeComponent.c`](code/method.Pansiyon_kayt1.FrmOdalar.InitializeComponent.c)
- [`code/method.Pansiyon_kayt1.FrmStoklar.Dispose.c`](code/method.Pansiyon_kayt1.FrmStoklar.Dispose.c)
- [`code/method.Pansiyon_kayt1.FrmStoklar.InitializeComponent.c`](code/method.Pansiyon_kayt1.FrmStoklar.InitializeComponent.c)
- [`code/method.Pansiyon_kayt1.FrmStoklar.listView1_SelectedIndexChanged.c`](code/method.Pansiyon_kayt1.FrmStoklar.listView1_SelectedIndexChanged.c)
- [`code/method.Pansiyon_kayt1.FrmYeniMsteri.BtnBo_Click.c`](code/method.Pansiyon_kayt1.FrmYeniMsteri.BtnBo_Click.c)
- [`code/method.Pansiyon_kayt1.FrmYeniMsteri.BtnDolu_Click.c`](code/method.Pansiyon_kayt1.FrmYeniMsteri.BtnDolu_Click.c)
- [`code/method.Pansiyon_kayt1.FrmYeniMsteri.Dispose.c`](code/method.Pansiyon_kayt1.FrmYeniMsteri.Dispose.c)
- [`code/method.Pansiyon_kayt1.FrmYeniMsteri.FrmYeniMsteri_Load.c`](code/method.Pansiyon_kayt1.FrmYeniMsteri.FrmYeniMsteri_Load.c)
- [`code/method.Pansiyon_kayt1.FrmYeniMsteri.InitializeComponent.c`](code/method.Pansiyon_kayt1.FrmYeniMsteri.InitializeComponent.c)
- [`code/method.Pansiyon_kayt1.Properties.Settings.get_Default.c`](code/method.Pansiyon_kayt1.Properties.Settings.get_Default.c)
- [`code/method.__c._.cctor_b__38_0.c`](code/method.__c._.cctor_b__38_0.c)

## Behavioral Analysis

This updated analysis incorporates the final set of disassemblies (**Chunk 23**). This final segment provides a high-resolution look at the execution logic within the `button1_Click` method and confirms that the "Pansiyon" system utilizes an extremely sophisticated, multi-layered protection scheme.

### Updated Analysis Report: [Pansiyon] Management System (Final Analysis)

#### 1. Confirmation of VM Architecture & Handler Logic
Chunk 23 provides a clear view of how the Virtual Machine (VM) processes instructions. The repetition of structures—specifically the `POPCOUNT` checks followed by complex arithmetic shifts—confirms that each "block" is an individual **Handler**.

*   **Instruction Dispatching:** When you see segments like `puVar10 = puVar10 | *puVar10;` or repetitive `CONCAT31` operations, you are seeing the VM's internal logic for decoding and executing a single "virtual" instruction.
*   **State Persistence:** Variables such as `puVar37`, `puVar_16`, and `puVar_23` appear to be registers or state markers within the virtual CPU. They carry values across different logical blocks, meaning the "real" logic of the program is stored in these variables, while the code you see is merely the machine that manipulates them.

#### 2. Advanced Protection Techniques (Refined)
The final chunk highlights several advanced techniques used to thwart both human analysts and automated tools:

*   **Massive Junk Code & "Dead" Branches:** The sheer volume of `WARNING: Removing unreachable block` messages is a deliberate tactic. By littering the binary with thousands of segments that are never executed (or only reached through impossible conditions), the obfuscator forces decompilers to struggle with the layout, making it nearly impossible to map the actual flow of the program.
*   **Instruction Overlapping:** The warning `Instruction at (...) overlaps instruction at (...)` indicates the use of overlapping instructions. This is a high-level technique where a jump lands in the middle of a multi-byte instruction, forcing the processor to interpret bytes differently than a linear scanner would. This effectively breaks many automated decompilation scripts.
*   **Extreme Mixed Boolean-Arithmetic (MBA):** The code uses complex bitwise masks and "concatenation" logic (e.g., `CONCAT31(puVar_13 >> 8, uVar_2 | *puVar_16)`). These are not standard arithmetic; they are designed to perform simple operations (like adding a number or checking a condition) in a way that looks like noise to a human but is executed correctly by the CPU.
*   **Opaque Predicates:** The `POPCOUNT` checks serve as "Opaque Predicates." These are branch conditions where the outcome is always the same, but only the machine can determine it easily. This forces an analyst to manually calculate every single branch just to find out if a piece of code is even reachable.

#### 3. Detection of Proprietary Implementation
The patterns in Chunk 23 strongly suggest the use of a commercial-grade protector like **VMProtect** or **Themida**. These tools don't just "obfuscate" your code; they replace it with their own bytecode and a custom interpreter.

---

### Final Technical Indicator Summary (Final Report)

| Feature | Status | Analysis Detail |
| :--- | :--- | :--- |
| **VM Protection** | **Confirmed** | Core logic is encapsulated in a proprietary VM; standard disassembly is useless for finding "original" logic. |
| **Control-Flow Flattening** | **Extreme** | The logic is flattened into a state-machine style where all paths lead back to a central dispatcher. |
| **MBA Complexity** | **High** | Mathematical operations are masked by complex bitwise/logical chains to defeat symbolic execution. |
| **Junk Code Insertion** | **Massive** | Thousands of "dead" blocks and overlapping instructions are used to exhaust the analyst's time/tools. |
| **Opaque Predicates** | **Confirmed** | Use of `POPCOUNT` and bitwise constants ensures that flow logic is hidden behind deterministic but hard-to-read math. |

---

### Final Risk Assessment: [CRITICAL / HIGHLY SECURE]

The "Pansiyon" system's security posture is designed to be highly resistant to traditional reverse engineering. 

1.  **Anti-Analysis Maturity:** This is not a basic obfuscation script; it is a professional-grade protection layer. It specifically targets the tools used by crackers and malware researchers (Ghidra, IDA Pro, Radare2).
2.  **Effort Multiplier:** Because of the VM architecture, every "step" in the actual logic (e.g., checking a password) might require analyzing 500–1,000 lines of obfuscated assembly code.
3.  **Automatic Tool Failure:** Automated scripts to find strings or patterns will fail because strings are constructed at runtime and logic is hidden behind the VM's dispatcher.

---

### Final Forensic & Mitigation Recommendations

To bypass this security, your team should move away from static "code reading" and adopt a **Dynamic/Behavioral** approach:

1.  **Hardware Breakpoints / Instrumentation:** Instead of analyzing what the code *looks like*, use tools like **x64dbg** or **Frida** to see what it *does*. Trace the execution and only log instructions that touch sensitive areas (like memory addresses involving "passwords," "keys," or "data").
2.  **Memory Scraping:** Do not try to find strings in the `.data` section of the binary. The VM will decrypt them into RAM just before use. Use a tool to dump the process memory during execution to catch plain-text strings.
3.  **API Hooking (The "Black Box" Method):** Since the internal logic is hidden behind a wall of math, watch the boundaries. Use **ProcMon** or Frida to monitor calls to networking APIs (`WinInet`, `ws2_32`), file system calls, and Registry access. This allows you to see *what* the program is doing without needing to understand *how* it did it through the VM.
4.  **Symbolic Execution (Advanced):** If you must understand a specific logic gate, use **angr** or **Triton**. These tools can "simplify" the MBA blocks by mathematically proving that a 50-line bitwise mess is just `x + y`.
5.  **De-virtualization:** Only attempt this if you have significant time/resources. You must identify the VM's instruction set and write a custom script to "lift" the bytecode into a readable intermediate representation (IR).

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors observed in the [Pansiyon] Management System analysis to the relevant MITRE ATT&CK techniques. 

Because many of the identified tactics are specific methods of code obfuscation intended to hinder manual and automated reverse engineering, they primarily fall under the **T1027 (Obfuscated Files or Information)** category.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of a custom Virtual Machine (VM) architecture hides the actual program logic behind a proprietary, complex instruction set. |
| T1027 | Obfuscated Files or Information | "Junk Code" and "Dead Branches" are used to create massive amounts of irrelevant data to exhaust analyst time and confuse decompilers. |
| T1027 | Obfuscated Files or Information | Overlapping instructions are utilized to force scanners to interpret the binary incorrectly, complicating linear analysis. |
| T1027 | Obfuscated Files or Information | Mixed Boolean-Arithmetic (MBA) masks simple operations with complex bitwise logic to defeat symbolic execution tools. |
| T1027 | Obfuscated Files or Information | Opaque Predicates (e.g., `POPCOUNT` checks) create deterministic but hard-to-parse branches to hide the true control flow. |
| T1027 | Obfuscated Files or Information | "Extreme" Control-Flow Flattening obscures the program's logic by directing all paths through a central dispatcher. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   `nzimtu.exe` (Executable filename)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None found in the provided strings.*

### **Other artifacts**
*   **Obfuscation Techniques:** 
    *   **Virtual Machine (VM) Protection:** The analysis confirms the use of a custom VM execution engine (similar to **VMProtect** or **Themida**) to wrap core logic.
    *   **Control-Flow Flattening:** Use of state-machine style logic to obscure the program's flow.
    *   **Mixed Boolean-Arithmetic (MBA):** Complex bitwise/logical chains used to hide simple arithmetic operations.
    *   **Opaque Predicates:** Specifically, the use of `POPCOUNT` instructions as branch conditions that are deterministic but hard for automated tools to analyze.
    *   **Instruction Overlapping:** Intentional overlapping of bytes in assembly to break linear disassemblers (e.g., Ghidra/IDA).
*   **Potential Internal Project Names:** 
    *   `<NebulousHarbor>` (Appears as a class or internal identifier; may relate to the specific packer/obfuscator used).

---
**Analyst Note:** 
While there are no traditional network IOCs (IPs/Domains) in this sample, the "Pansiyon" system exhibits **high-sophistication evasion behaviors**. The presence of VM protection, MBA, and control-flow flattening indicates that this is likely a high-priority target for deeper dynamic analysis to identify potential C2 behavior or secondary payloads that are currently hidden within the virtualized code.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1. **Malware family:** custom
2. **Malware type:** loader
3. **Confidence:** Medium
4. **Key evidence:**
    *   **Sophisticated Obfuscation Architecture:** The use of a custom Virtual Machine (VM) architecture, Mixed Boolean-Arithmetic (MBA), and "Instruction Overlapping" indicates high-level evasion techniques typically found in professional-grade loaders or complex backdoors to shield the core logic from researchers.
    *   **Anti-Analysis Hardening:** The heavy reliance on "Opaque Predicates" (e.g., `POPCOUNT` checks) and "Control-Flow Flattening" demonstrates a deliberate effort to break automated de-compilation tools like Ghidra or IDA Pro.
    *   **Hidden Functionality:** While no direct malicious actions were identified in the text, the presence of internal project identifiers (e.g., `<NebulousHarbor>`) and the "Loader" style infrastructure strongly suggests a protective wrapper designed to deliver or hide further payloads (such as RATs or info-stealers).
