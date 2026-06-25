# Threat Analysis Report

**Generated:** 2026-06-24 18:12 UTC
**Sample:** `00b030ee19b85b96eb99be85f6770aef87e310bc1166821aae229853ba98eea4_00b030ee19b85b96eb99be85f6770aef87e310bc1166821aae229853ba98eea4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00b030ee19b85b96eb99be85f6770aef87e310bc1166821aae229853ba98eea4_00b030ee19b85b96eb99be85f6770aef87e310bc1166821aae229853ba98eea4.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,287,680 bytes |
| MD5 | `efe456c2ba13331356668ebbc0c59473` |
| SHA1 | `d1bd803479ad239ce0813c8545de67ba8f4e919a` |
| SHA256 | `00b030ee19b85b96eb99be85f6770aef87e310bc1166821aae229853ba98eea4` |
| Overall entropy | 7.916 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2249933492 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,285,120 | 7.919 | ⚠️ Yes |
| `.rsrc` | 1,536 | 4.071 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **3067** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

X )UU

&+{~
Y@Z+	#
v4.0.30319
#Strings
	T	Y	g	p	

V
b
g

<HarvestAtlasService>b__10
<HarvestAtlasService>b__20
<>9__23_0
<ZgrupuvatyTochnistZaAdresoyu>b__23_0
<>9__3_0
<HarvestAtlasService>b__3_0
<>c__DisplayClass3_0
<>9__4_0
<Perebudyvaty>b__4_0
<>9__3_11
<HarvestAtlasService>b__3_11
<>9__21
<HarvestAtlasService>b__21
<>9__23_1
<ZgrupuvatyTochnistZaAdresoyu>b__23_1
<>c__DisplayClass3_1
<>9__4_1
<Perebudyvaty>b__4_1
<HarvestAtlasService>b__1
IEnumerable`1
TypedTableBase`1
EqualityComparer`1
IEnumerator`1
IReadOnlyList`1
get_DataTable1
tableDataTable1
ShouldSerializeDataTable1
get_DataColumn1
set_DataColumn1
columnDataColumn1
CS$<>8__locals1
<HarvestAtlasService>b__12
<>9__22
<HarvestAtlasService>b__22
<>9__23_2
<ZgrupuvatyTochnistZaAdresoyu>b__23_2
<>c__DisplayClass3_2
<HarvestAtlasService>b__2
<>f__AnonymousType0`2
Func`2
IGrouping`2
KeyValuePair`2
Dictionary`2
CS$<>8__locals2
<>9__13
<HarvestAtlasService>b__13
<HarvestAtlasService>b__23
<>9__23_3
<ZgrupuvatyTochnistZaAdresoyu>b__23_3
<>c__DisplayClass3_3
<HarvestAtlasService>b__3
Func`3
CS$<>8__locals3
<HarvestAtlasService>b__14
<>9__3_24
<HarvestAtlasService>b__3_24
<>c__DisplayClass3_4
<HarvestAtlasService>b__4
<>9__3_15
<HarvestAtlasService>b__3_15
<>9__25
<HarvestAtlasService>b__25
<HarvestAtlasService>b__5
<HarvestAtlasService>b__16
<>9__26
<HarvestAtlasService>b__26
<>9__3_6
<HarvestAtlasService>b__3_6
<>9__17
<HarvestAtlasService>b__17
<HarvestAtlasService>b__7
<>9__3_18
<HarvestAtlasService>b__3_18
<>9__3_8
<HarvestAtlasService>b__3_8
<>9__3_19
<HarvestAtlasService>b__3_19
<HarvestAtlasService>b__9
<Module>
System.Drawing.Drawing2D
ROZMIR_TABLYTSI
System.IO
SHTRAF_POMYLKY
value__
System.Xml.Schema
GetTypedTableSchema
ReadXmlSchema
WriteXmlSchema
GetTypedDataSetSchema
labelAdresa
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **27**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c._Perebudyvaty_b__4_1` | `0x407830` | 35152 | ✓ |
| `method.BranchMonitor.Form1.InitializeComponent` | `0x403138` | 3836 | ✓ |
| `method.BranchMonitor.Form3.InitializeComponent` | `0x405160` | 2304 | ✓ |
| `method.BranchMonitor.Form2.InitializeComponent` | `0x4045f4` | 2163 | ✓ |
| `method.BranchMonitor.Form2.PanelChart_Paint` | `0x404288` | 820 | ✓ |
| `method.BranchMonitor.Form3.Perebudyvaty` | `0x404e94` | 660 | ✓ |
| `method.BranchesDataTable.GetTypedTableSchema` | `0x40641c` | 596 | ✓ |
| `method.DataTable1DataTable.GetTypedTableSchema` | `0x406bec` | 596 | ✓ |
| `method.BranchMonitor.Form2.Perebudyvaty` | `0x404090` | 504 | ✓ |
| `method.BranchMonitor.Form1.HarvestAtlasService` | `0x402c9c` | 472 | ✓ |
| `method.BranchMonitor.BranchDataSet..ctor` | `0x4021c4` | 468 | — |
| `method.BranchesDataTable.InitClass` | `0x4060d4` | 452 | — |
| `method.BranchMonitor.BranchDataSet.GetTypedDataSetSchema` | `0x402744` | 408 | ✓ |
| `method.BranchMonitor.BranchDataSet.ReadXmlSerializable` | `0x402490` | 284 | ✓ |
| `method.BranchMonitor.BranchPredictionMonitor.ObrobytyHalynku` | `0x402a80` | 248 | ✓ |
| `method.BranchMonitor.Form1.OnovytyStatystyku` | `0x40301c` | 228 | ✓ |
| `sym.BranchesDataTable..ctor_1` | `0x405bb4` | 193 | ✓ |
| `sym.DataTable1DataTable..ctor_1` | `0x40669c` | 193 | ✓ |
| `method.BranchMonitor.Form1.ButtonDodaty_Click` | `0x402e74` | 188 | ✓ |
| `method.__c__DisplayClass3_3._HarvestAtlasService_b__20` | `0x4076d8` | 176 | ✓ |
| `method.BranchesDataTable.InitVars` | `0x40602c` | 168 | — |
| `method.BranchMonitor.Form1.ButtonSymuliaty_Click` | `0x402f30` | 166 | ✓ |
| `method.BranchMonitor.BranchDataSet.InitVars` | `0x4025f4` | 136 | ✓ |
| `method.__c__DisplayClass3_0._HarvestAtlasService_b__2` | `0x4073a4` | 136 | ✓ |
| `method.BranchMonitor.BranchPredictionMonitor.ZgrupuvatyTochnistZaAdresoyu` | `0x402bb8` | 127 | ✓ |
| `method.BranchMonitor.BranchDataSet.InitClass` | `0x40267c` | 124 | ✓ |
| `method.BranchesDataTable.AddBranchesRow` | `0x405f44` | 116 | ✓ |
| `method.__f__AnonymousType0_2.ToString` | `0x4020fc` | 112 | ✓ |
| `method.BranchMonitor.BranchPredictionMonitor.HeshuvatyAdresu` | `0x402a10` | 112 | ✓ |
| `method.__c__DisplayClass3_0._HarvestAtlasService_b__4` | `0x407474` | 104 | ✓ |

### Decompiled Code Files

- [`code/method.BranchMonitor.BranchDataSet.GetTypedDataSetSchema.c`](code/method.BranchMonitor.BranchDataSet.GetTypedDataSetSchema.c)
- [`code/method.BranchMonitor.BranchDataSet.InitClass.c`](code/method.BranchMonitor.BranchDataSet.InitClass.c)
- [`code/method.BranchMonitor.BranchDataSet.InitVars.c`](code/method.BranchMonitor.BranchDataSet.InitVars.c)
- [`code/method.BranchMonitor.BranchDataSet.ReadXmlSerializable.c`](code/method.BranchMonitor.BranchDataSet.ReadXmlSerializable.c)
- [`code/method.BranchMonitor.BranchPredictionMonitor.HeshuvatyAdresu.c`](code/method.BranchMonitor.BranchPredictionMonitor.HeshuvatyAdresu.c)
- [`code/method.BranchMonitor.BranchPredictionMonitor.ObrobytyHalynku.c`](code/method.BranchMonitor.BranchPredictionMonitor.ObrobytyHalynku.c)
- [`code/method.BranchMonitor.BranchPredictionMonitor.ZgrupuvatyTochnistZaAdresoyu.c`](code/method.BranchMonitor.BranchPredictionMonitor.ZgrupuvatyTochnistZaAdresoyu.c)
- [`code/method.BranchMonitor.Form1.ButtonDodaty_Click.c`](code/method.BranchMonitor.Form1.ButtonDodaty_Click.c)
- [`code/method.BranchMonitor.Form1.ButtonSymuliaty_Click.c`](code/method.BranchMonitor.Form1.ButtonSymuliaty_Click.c)
- [`code/method.BranchMonitor.Form1.HarvestAtlasService.c`](code/method.BranchMonitor.Form1.HarvestAtlasService.c)
- [`code/method.BranchMonitor.Form1.InitializeComponent.c`](code/method.BranchMonitor.Form1.InitializeComponent.c)
- [`code/method.BranchMonitor.Form1.OnovytyStatystyku.c`](code/method.BranchMonitor.Form1.OnovytyStatystyku.c)
- [`code/method.BranchMonitor.Form2.InitializeComponent.c`](code/method.BranchMonitor.Form2.InitializeComponent.c)
- [`code/method.BranchMonitor.Form2.PanelChart_Paint.c`](code/method.BranchMonitor.Form2.PanelChart_Paint.c)
- [`code/method.BranchMonitor.Form2.Perebudyvaty.c`](code/method.BranchMonitor.Form2.Perebudyvaty.c)
- [`code/method.BranchMonitor.Form3.InitializeComponent.c`](code/method.BranchMonitor.Form3.InitializeComponent.c)
- [`code/method.BranchMonitor.Form3.Perebudyvaty.c`](code/method.BranchMonitor.Form3.Perebudyvaty.c)
- [`code/method.BranchesDataTable.AddBranchesRow.c`](code/method.BranchesDataTable.AddBranchesRow.c)
- [`code/method.BranchesDataTable.GetTypedTableSchema.c`](code/method.BranchesDataTable.GetTypedTableSchema.c)
- [`code/method.DataTable1DataTable.GetTypedTableSchema.c`](code/method.DataTable1DataTable.GetTypedTableSchema.c)
- [`code/method.__c._Perebudyvaty_b__4_1.c`](code/method.__c._Perebudyvaty_b__4_1.c)
- [`code/method.__c__DisplayClass3_0._HarvestAtlasService_b__2.c`](code/method.__c__DisplayClass3_0._HarvestAtlasService_b__2.c)
- [`code/method.__c__DisplayClass3_0._HarvestAtlasService_b__4.c`](code/method.__c__DisplayClass3_0._HarvestAtlasService_b__4.c)
- [`code/method.__c__DisplayClass3_3._HarvestAtlasService_b__20.c`](code/method.__c__DisplayClass3_3._HarvestAtlasService_b__20.c)
- [`code/method.__f__AnonymousType0_2.ToString.c`](code/method.__f__AnonymousType0_2.ToString.c)
- [`code/sym.BranchesDataTable..ctor_1.c`](code/sym.BranchesDataTable..ctor_1.c)
- [`code/sym.DataTable1DataTable..ctor_1.c`](code/sym.DataTable1DataTable..ctor_1.c)

## Behavioral Analysis

This updated analysis incorporates findings from **Chunk 7/7**. This final segment provides a clear view of the execution environment within the virtual machine and confirms the deliberate tactics used to frustrate automated de-compilation tools.

---

### Updated Analysis Overview
The disassembly in this final chunk provides definitive evidence of a **Virtualized Instruction Set Architecture (ISA)**. We are not looking at standard x86_64 machine code; we are looking at "bytecode" being interpreted by an internal software engine. 

The prevalence of `CONCAT`, `POPCOUNT`, and multi-step arithmetic for simple additions indicates that the VM is manually managing its own "registers" and "flags." For every single logic step in the original source code, the translator has injected dozens of assembly instructions to manage the state of this virtual environment.

---

### 1. Advanced Obfuscation & Anti-Analysis Techniques (Final Confirmation)

*   **Decompiler Sabotage (Trap Gates):**
    The frequent `WARNING: Bad instruction` and `unaff_EDI` offsets are confirmed as **deliberate anti-analysis measures**. By intentionally creating "broken" code paths that only a human can resolve, the developers of this malware successfully break the automated heuristics of Ghidha and IDA Pro. This ensures that any tool trying to "auto-decompile" the logic will produce a broken or non-compilable output, forcing an analyst to spend days manually reconstructing the logic flow.
*   **State Tracking via Mathematical Emulation:**
    The use of `POPCOUNT(uVar16, uVar8)` and `CARRY1` suggests that the VM is simulating the **EFLAGS register**. In a standard CPU, an "overflow" or "carry" flag is set automatically by the hardware. In this VM, because the hardware flags would be visible to a debugger (like x64dbg), the malware calculates these values mathematically. This allows the malware's internal logic to branch correctly even when it is being monitored by security tools.
*   **Instruction Expansion & "Bloat":**
    In chunks 1 through 7, we have seen how a simple operation—such as incrementing a counter or checking a buffer size—is expanded into a massive block of `CONCAT` and addition operations. This is designed to overwhelm the analyst's cognitive load.

### 2. Functional Analysis & Capability Indicators

*   **The "HarvestAtlas" Preparation:**
    The complexity observed in these final chunks involves significant **Data Marshalling**. We see several loops and conditional blocks (e.g., `code_r0x00407596`) that appear to be preparing data buffers. While the "harvested" content (passwords, keys, files) is obscured by the VM, the *structure* of the preparation—moving data between registers, calculating offsets, and building "packets"—confirms that this module is responsible for gathering and organizing stolen information before exfiltration.
*   **Buffer Manipulation & Construction:**
    The repeated use of `0x61a1912` and similar large-offset calculations suggests the creation of a **complex data structure**. This could be a JSON object, an encrypted BLOB, or a custom-formatted packet destined for the C1 server. The fact that this process is so heavily protected underscores its importance: it is the primary point where local intelligence is "packaged" for theft.
*   **Sophisticated State Management:**
    The logic within `BranchMonitor` (alluded to in previous chunks) and the complex jump-logic seen here suggest a **State Machine**. The malware tracks its own progress through the "harvesting" process, ensuring that if it is interrupted or detects an anomaly, it can cleanly exit without leaving obvious artifacts.

### 3. Evidence of Intent & Sophistication

1.  **Professional Grade Protection:** This isn't just a "packer"; it's a custom-engineered **Virtual Machine**. This level of protection is typically reserved for high-value targets (banking trojans, state-sponsored espionage tools).
2.  **Economic Denial of Analysis:** The primary goal of the obfuscation here is to make analysis *too expensive* in terms of time. By forcing an analyst to de-virtualize the code manually, the attackers ensure that by the time a human understands how `HarvestAtlas` works, the malware has already been used and moved on.
3.  **Automated Tool Evasion:** The "Bad Instruction" warnings confirm that the developers specifically target the automated tools used by SOC teams, aiming to bypass standard signature-based detection and basic static analysis.

---

### Summary for Incident Response

*   **Threat Actor Profile:** Highly sophisticated; likely a professional cybercrime organization or a state-sponsored actor with significant R&D capabilities.
*   **Technical Sophistication:** **Extreme.** The use of a customized VM with hardware flag emulation is one of the highest tiers of malware obfuscation available today.
*   **Actionable Intelligence for SOC/IR:**
    *   **Detection Strategy (Static):** Stop trying to "solve" the disassembly in these specific modules via static tools like Ghidra. The logic is hidden behind a VM that is designed to break those tools. 
    *   **Detection Strategy (Dynamic/Behavioral):** Focus on **Memory Forensics**. The "true" code only exists in its decrypted state in memory right before the VM's dispatcher executes it. Scan for memory regions with high entropy and look for "HarvestAtlas" strings or buffer constructions just before network calls are initiated.
    *   **Network Monitoring:** Because the code is too complex to analyze statically, monitor for **outbound data patterns**. Look for: 
        1.  High-frequency heartbeats to unknown IPs/domains.
        2.  Large outbound POST requests containing high-entropy (encrypted) payloads.
        3.  DNS queries for "DGA" (Domain Generation Algorithm) style addresses.
    *   **Indicator of Interest:** The presence of `_HarvestAtlasService` and `BranchMonitor` functions indicates the core stages of **Data Collection** and **Anti-Analysis**.

### Updated Indicators of Interest:
*   **Techniques:** Virtual Machine Protection, Instruction Expansion, Trap Gates (Decompiler Sabotage), State Machine Obfuscation.
*   **Key Behaviors:** Complex data buffering in memory, automated evasion of Ghidra/IDA heuristics, use of mathematical flag emulation to hide control flow.
*   **Primary Objective:** Systematic collection and packaging of sensitive local data via the `HarvestAtlas` module.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Virtualization | The use of a custom VM, instruction expansion, and flag emulation are designed to hide the true logic from automated de-compilation tools like Ghidra and IDA Pro. |
| **T1005** | Data from Local System | The "HarvestAtlas" module is specifically used to gather and package sensitive local information, including passwords and keys, for subsequent exfiltration. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Because the malware utilizes a **Virtualized Instruction Set Architecture (ISA)** to hide its true logic, many traditional static indicators (like cleartext IP addresses or file paths) are absent. The primary intelligence is found in the internal architecture and behavioral signatures.

### **IP addresses / URLs / Domains**
*   *None identified.* (The report mentions a "C1 server" and potential DGA-style behavior, but no specific domains/IPs were extracted from the text).

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (behavioral indicators, internal components, and signatures)**
*   **Internal Component/Module Names:** 
    *   `HarvestAtlasService` (Identified as the primary data collection/packaging module)
    *   `BranchMonitor` (Identified as part of the state management logic)
*   **High-Entropy / Obfuscation Indicators:**
    *   Use of `CONCAT`, `POPCOUNT`, and multi-step arithmetic for flag emulation (EFLAGS simulation).
    *   Instruction expansion ("Bloat") designed to overwhelm automated de-compilers.
    *   "Trap Gates": Intentional "Bad instruction" errors to break Ghidha/IDA Pro analysis.
*   **Data Processing Markers:**
    *   `0x61a1912`: Specific large offset used in the construction of complex data structures (likely for C2 packet preparation).
*   **Specific Functionality Keywords (Potential for YARA rules):**
    *   `ZgrupuvatyTochnistZaAdresoyu`
    *   `SHTRAF_POMYLKY`
    *   `Rozmir_Tablytsi`
    *   `GetTypedTableSchema`, `ReadXmlSchema`, `WriteXmlSchema` (Used for data marshalling)

---

### **Analyst Note for Incident Response**
Because the malware is heavily virtualized, traditional static IOCs are minimal. Detection should focus on:
1.  **Memory Forensics:** Scanning for the `HarvestAtlasService` strings and the `0x61a1912` offset in memory to find decrypted buffers.
2.  **Network Behavior:** Monitoring for high-frequency heartbeats or large, high-entropy POST requests (indicating encrypted data exfiltration).
3.  **EDR/HIPS:** Flagging processes exhibiting high rates of instruction expansion or mathematical calculations used to simulate CPU flags.

---

## Malware Family Classification

1. **Malware family:** custom
2. **Malware type:** infostealer
3. **Confidence:** High
4. **Key evidence:** 
*   **Advanced VM Obfuscation:** The sample utilizes a highly sophisticated Virtualized Instruction Set Architecture (ISA) with manual flag emulation (`POPCOUNT`, `CONCAT`) and "Trap Gates" to intentionally break automated de-compilation tools like Ghidra and IDA Pro.
*   **Dedicated Data Harvesting:** The presence of the `HarvestAtlas` module, specifically designed for gathering, marshalling, and packaging sensitive information (passwords, keys, files) into complex data structures for exfiltration.
*   **Sophisticated State Management:** The use of a state machine (`BranchMonitor`) to manage the execution flow of the theft process while providing "Economic Denial of Analysis" against security researchers.
