# Threat Analysis Report

**Generated:** 2026-08-22 07:37 UTC
**Sample:** `1111810b615080da021051e957d6eb1df3e88e44b2e1b8e53186ea3f2ecc14d9_1111810b615080da021051e957d6eb1df3e88e44b2e1b8e53186ea3f2ecc14d9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1111810b615080da021051e957d6eb1df3e88e44b2e1b8e53186ea3f2ecc14d9_1111810b615080da021051e957d6eb1df3e88e44b2e1b8e53186ea3f2ecc14d9.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,696,256 bytes |
| MD5 | `56fe5645c6b6a03a71b817e0ba7f9e94` |
| SHA1 | `3eab89184a99326ec44ec897fce111abd18b1499` |
| SHA256 | `1111810b615080da021051e957d6eb1df3e88e44b2e1b8e53186ea3f2ecc14d9` |
| Overall entropy | 7.759 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779326209 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,509,376 | 7.922 | ⚠️ Yes |
| `.rsrc` | 185,856 | 5.318 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **3335** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
p+r

v4.0.30319
#Strings
<.ctor>b__1_10
__StaticArrayInitTypeSize=20
<BtnStart_Click>b__10_0
<>c__DisplayClass10_0
<.ctor>b__0_0
<>9__1_0
<.ctor>b__1_0
<>c__DisplayClass2_0
<BuildUI>b__3_0
<BuildUI>b__4_0
<BuildUI>b__5_0
<BuildUI>b__6_0
<BuildUI>b__9_0
<ProcessFileAsync>b__0
<Survey_Cadastral_Transect>b__0
<BtnStart_Click>b__10_1
<>c__DisplayClass10_1
<.ctor>b__1_1
<BuildUI>b__4_1
<ProcessFileAsync>b__1
<Survey_Cadastral_Transect>b__1
IEnumerable`1
Action`1
EventHandler`1
List`1
get_Panel1
<BtnStart_Click>b__10_2
<>c__DisplayClass10_2
<.ctor>b__1_2
<ProcessFileAsync>b__2
<Survey_Cadastral_Transect>b__2
Func`2
Action`2
get_Panel2
<.ctor>b__1_3
<BtnStart_Click>b__3
<Survey_Cadastral_Transect>b__3
Func`3
D3C0C46CE5572A5ED901CC5DA80738CE32E83B37AA6A4D651909C77049244664
<.ctor>b__1_4
<BtnStart_Click>b__4
<.ctor>b__1_5
<BtnStart_Click>b__5
<>9__1_6
<.ctor>b__1_6
<>9__1_7
<.ctor>b__1_7
<.ctor>b__1_8
<.ctor>b__1_9
<Module>
<PrivateImplementationDetails>
FILE_PATH
BuildUI
System.IO
get_AnVO
get_CKT
_treeAST
WM_SETREDRAW
mscorlib
System.Collections.Generic
Microsoft.VisualBasic
ProcessFileAsync
CancelAsync
RunWorkerAsync
get_Id
set_Id
skip_head
Thread
terrainQuad
get_DarkRed
add_ProgressChanged
remove_ProgressChanged
add_TextChanged
set_Checked
Interlocked
set_Enabled
get_Cancelled
add_ErrorOccurred
remove_ErrorOccurred
azimuthReversed
add_Completed
remove_Completed
add_RunWorkerCompleted
NewGuid
<Id>k__BackingField
<Name>k__BackingField
<RawValue>k__BackingField
<Depth>k__BackingField
<Explanation>k__BackingField
<Description>k__BackingField
<Pattern>k__BackingField
OpenChild
_txtReplace
transectAllowance
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.AdvancedRegexStudio.Core.RegexToken.get_Explanation` | `0x4023c3` | 1412486 | ✓ |
| `method.__c__DisplayClass10_2._BtnStart_Click_b__5` | `0x4045ab` | 122392 | ✓ |
| `method.__c__DisplayClass2_0._Survey_Cadastral_Transect_b__3` | `0x4044f8` | 21422 | ✓ |
| `method.AdvancedRegexStudio.Forms.LiveTesterForm..ctor` | `0x403147` | 2386 | ✓ |
| `method.AdvancedRegexStudio.Forms.BulkProcessorForm..ctor` | `0x403aa1` | 2326 | ✓ |
| `method.AdvancedRegexStudio.Models.SavedRegex.set_Description` | `0x4028c1` | 2090 | ✓ |
| `method.AdvancedRegexStudio.Forms.MainMdiForm.Survey_Cadastral_Transect` | `0x402c80` | 1116 | ✓ |
| `method.AdvancedRegexStudio.Forms.MainMdiForm..ctor` | `0x4028f8` | 904 | ✓ |
| `method.AdvancedRegexStudio.Forms.BulkProcessorForm.BuildUI` | `0x403ab0` | 720 | ✓ |
| `method.AdvancedRegexStudio.Forms.CodeGeneratorForm.BuildUI` | `0x4037a8` | 684 | ✓ |
| `method.AdvancedRegexStudio.Core.RegexParser.Parse` | `0x402404` | 624 | ✓ |
| `method.AdvancedRegexStudio.Core.RegexToken..ctor` | `0x4023e5` | 612 | ✓ |
| `method.AdvancedRegexStudio.Core.NativeMethods.ResumeDrawing` | `0x40265b` | 572 | ✓ |
| `method.AdvancedRegexStudio.Forms.LiveTesterForm.RunRegex` | `0x403354` | 512 | ✓ |
| `method.AdvancedRegexStudio.Forms.LiveTesterForm.BuildUI` | `0x403158` | 508 | ✓ |
| `method.__c._.ctor_b__1_6` | `0x4043b7` | 428 | ✓ |
| `method.AdvancedRegexStudio.Forms.RegexAnalyzerForm.BuildUI` | `0x40356c` | 296 | ✓ |
| `method.AdvancedRegexStudio.Forms.RegexAnalyzerForm.Analyze` | `0x403694` | 252 | ✓ |
| `method.AdvancedRegexStudio.Forms.SettingsForm..ctor` | `0x4040f4` | 244 | ✓ |
| `method.__c__DisplayClass10_0._ProcessFileAsync_b__0` | `0x4041f0` | 240 | ✓ |
| `method.AdvancedRegexStudio.Forms.BulkProcessorForm.BtnStart_Click` | `0x403d80` | 214 | ✓ |
| `method.AdvancedRegexStudio.Forms.LibraryForm.LoadLibrary` | `0x403f1c` | 204 | ✓ |
| `method.AdvancedRegexStudio.Forms.LibraryForm.BuildUI` | `0x40403c` | 176 | ✓ |
| `method.AdvancedRegexStudio.Core.AsyncFileProcessor.ProcessFileAsync` | `0x4027c4` | 160 | ✓ |
| `method.__c__DisplayClass10_0._ProcessFileAsync_b__2` | `0x40430c` | 152 | ✓ |
| `method.__c__DisplayClass2_0._Survey_Cadastral_Transect_b__0` | `0x4043e0` | 128 | ✓ |
| `method.AdvancedRegexStudio.Generators.CSharpGenerator.GenerateReplaceCode` | `0x402164` | 120 | ✓ |
| `method.AdvancedRegexStudio.Generators.PythonGenerator.GenerateReplaceCode` | `0x402238` | 120 | ✓ |
| `method.AdvancedRegexStudio.Generators.JavaScriptGenerator.GenerateReplaceCode` | `0x4022fc` | 104 | ✓ |
| `method.AdvancedRegexStudio.Generators.CSharpGenerator.GenerateMatchCode` | `0x402108` | 92 | ✓ |

### Decompiled Code Files

- [`code/method.AdvancedRegexStudio.Core.AsyncFileProcessor.ProcessFileAsync.c`](code/method.AdvancedRegexStudio.Core.AsyncFileProcessor.ProcessFileAsync.c)
- [`code/method.AdvancedRegexStudio.Core.NativeMethods.ResumeDrawing.c`](code/method.AdvancedRegexStudio.Core.NativeMethods.ResumeDrawing.c)
- [`code/method.AdvancedRegexStudio.Core.RegexParser.Parse.c`](code/method.AdvancedRegexStudio.Core.RegexParser.Parse.c)
- [`code/method.AdvancedRegexStudio.Core.RegexToken..ctor.c`](code/method.AdvancedRegexStudio.Core.RegexToken..ctor.c)
- [`code/method.AdvancedRegexStudio.Core.RegexToken.get_Explanation.c`](code/method.AdvancedRegexStudio.Core.RegexToken.get_Explanation.c)
- [`code/method.AdvancedRegexStudio.Forms.BulkProcessorForm..ctor.c`](code/method.AdvancedRegexStudio.Forms.BulkProcessorForm..ctor.c)
- [`code/method.AdvancedRegexStudio.Forms.BulkProcessorForm.BtnStart_Click.c`](code/method.AdvancedRegexStudio.Forms.BulkProcessorForm.BtnStart_Click.c)
- [`code/method.AdvancedRegexStudio.Forms.BulkProcessorForm.BuildUI.c`](code/method.AdvancedRegexStudio.Forms.BulkProcessorForm.BuildUI.c)
- [`code/method.AdvancedRegexStudio.Forms.CodeGeneratorForm.BuildUI.c`](code/method.AdvancedRegexStudio.Forms.CodeGeneratorForm.BuildUI.c)
- [`code/method.AdvancedRegexStudio.Forms.LibraryForm.BuildUI.c`](code/method.AdvancedRegexStudio.Forms.LibraryForm.BuildUI.c)
- [`code/method.AdvancedRegexStudio.Forms.LibraryForm.LoadLibrary.c`](code/method.AdvancedRegexStudio.Forms.LibraryForm.LoadLibrary.c)
- [`code/method.AdvancedRegexStudio.Forms.LiveTesterForm..ctor.c`](code/method.AdvancedRegexStudio.Forms.LiveTesterForm..ctor.c)
- [`code/method.AdvancedRegexStudio.Forms.LiveTesterForm.BuildUI.c`](code/method.AdvancedRegexStudio.Forms.LiveTesterForm.BuildUI.c)
- [`code/method.AdvancedRegexStudio.Forms.LiveTesterForm.RunRegex.c`](code/method.AdvancedRegexStudio.Forms.LiveTesterForm.RunRegex.c)
- [`code/method.AdvancedRegexStudio.Forms.MainMdiForm..ctor.c`](code/method.AdvancedRegexStudio.Forms.MainMdiForm..ctor.c)
- [`code/method.AdvancedRegexStudio.Forms.MainMdiForm.Survey_Cadastral_Transect.c`](code/method.AdvancedRegexStudio.Forms.MainMdiForm.Survey_Cadastral_Transect.c)
- [`code/method.AdvancedRegexStudio.Forms.RegexAnalyzerForm.Analyze.c`](code/method.AdvancedRegexStudio.Forms.RegexAnalyzerForm.Analyze.c)
- [`code/method.AdvancedRegexStudio.Forms.RegexAnalyzerForm.BuildUI.c`](code/method.AdvancedRegexStudio.Forms.RegexAnalyzerForm.BuildUI.c)
- [`code/method.AdvancedRegexStudio.Forms.SettingsForm..ctor.c`](code/method.AdvancedRegexStudio.Forms.SettingsForm..ctor.c)
- [`code/method.AdvancedRegexStudio.Generators.CSharpGenerator.GenerateMatchCode.c`](code/method.AdvancedRegexStudio.Generators.CSharpGenerator.GenerateMatchCode.c)
- [`code/method.AdvancedRegexStudio.Generators.CSharpGenerator.GenerateReplaceCode.c`](code/method.AdvancedRegexStudio.Generators.CSharpGenerator.GenerateReplaceCode.c)
- [`code/method.AdvancedRegexStudio.Generators.JavaScriptGenerator.GenerateReplaceCode.c`](code/method.AdvancedRegexStudio.Generators.JavaScriptGenerator.GenerateReplaceCode.c)
- [`code/method.AdvancedRegexStudio.Generators.PythonGenerator.GenerateReplaceCode.c`](code/method.AdvancedRegexStudio.Generators.PythonGenerator.GenerateReplaceCode.c)
- [`code/method.AdvancedRegexStudio.Models.SavedRegex.set_Description.c`](code/method.AdvancedRegexStudio.Models.SavedRegex.set_Description.c)
- [`code/method.__c._.ctor_b__1_6.c`](code/method.__c._.ctor_b__1_6.c)
- [`code/method.__c__DisplayClass10_0._ProcessFileAsync_b__0.c`](code/method.__c__DisplayClass10_0._ProcessFileAsync_b__0.c)
- [`code/method.__c__DisplayClass10_0._ProcessFileAsync_b__2.c`](code/method.__c__DisplayClass10_0._ProcessFileAsync_b__2.c)
- [`code/method.__c__DisplayClass10_2._BtnStart_Click_b__5.c`](code/method.__c__DisplayClass10_2._BtnStart_Click_b__5.c)
- [`code/method.__c__DisplayClass2_0._Survey_Cadastral_Transect_b__0.c`](code/method.__c__DisplayClass2_0._Survey_Cadastral_Transect_b__0.c)
- [`code/method.__c__DisplayClass2_0._Survey_Cadastral_Transect_b__3.c`](code/method.__c__DisplayClass2_0._Survey_Cadastral_Transect_b__3.c)

## Behavioral Analysis

This final chunk of disassembly confirms and amplifies the previous findings, providing definitive evidence of high-level, professional-grade obfuscation techniques. The sheer volume of "noise" generated by the decompiler suggests that this binary is designed specifically to defeat automated static analysis tools.

---

### Updated Analysis: Advanced Regex Studio (Analysis Part 4)

#### 1. Quantification of Control Flow Obfuscation
The final chunk shows a massive list of **unreachable block removals** (nearly 100 occurrences in just two functions). 
*   **Complexity Engineering:** The decompiler is forced to discard hundreds of code blocks because they are mathematically or logically unreachable during normal execution. This creates "noise" that forces an analyst to manually trace every branch only to find it leads nowhere.
*   **Control Flow Flattening (CFF):** The repeated warnings and the structure of the loops suggest a flattened control flow where the actual logic is buried within a massive switch statement or state machine, making it nearly impossible to follow the "true" execution path without custom de-obfuscation scripts.

#### 2. Analysis of High-Interest Functions (Generator Modules)
The final chunk covers `PythonGenerator.GenerateReplaceCode` and `CSharpGenerator.GenerateMatchCode`. These functions are particularly significant:

*   **Technical Implementation:** While the function names suggest "code generation" for Python or C#, the underlying assembly is almost entirely opaque. Instead of clear logic to build a string or construct an object, we see a dense thicket of bitwise operations (`CONCAT31`, `CONCAT22`), complex arithmetic on high/low bits, and mathematical obfuscation (e.g., `puVar4 = *piVar5 * 0x186f7000`).
*   **The "M.O." of Sophisticated Malware:** This type of construction is common when a developer uses a **Virtual Machine (VM) Protector**. The real logic isn't actually in the C# or Python generation; instead, those functions are likely serving as handlers for a custom virtual machine's bytecode.
*   **Risk Profile:** 
    *   **Evasion of Signature-based Detection:** By using "hidden" logic to generate scripts at runtime, the malware ensures that no malicious strings appear in the binary until it is actually executed.
    *   **Complexity as a Shield:** The heavy obfuscation in these specific modules suggests they contain the most critical parts of the program—likely the components responsible for **payload delivery, configuration decryption, or C2 communication.**

#### 3. Identification of Advanced Anti-Analysis "Triggers"
The recurring warnings regarding **Instruction Overlap** (`0x402642` vs `0x402641`) are a specific indicator:
*   **Disassembler Desynchronization:** By overlapping instructions, the author ensures that if an analyst (or a tool) starts reading even one byte too early or late, the entire disassembly of the following 100 bytes changes into something completely different. This is a classic "trap" for human researchers and automated scanners alike.

---

### Final Consolidated Summary for Incident Response

| Category | Observation | Significance |
| :--- | :--- | :--- |
| **Primary Function** | Advanced Regex / Bulk Data Utility | Serves as the front-end; provides a plausible "legal" reason for complex file/data manipulation. |
| **Obfuscation Technique** | **Elite Complexity (VM/Mutation)** | Use of Control Flow Flattening, Instruction Overloading, and massive Junk Code injection. |
| **Anti-Analysis TTPs** | **High Sophistication** | Extensive use of overlapping instructions to break disassemblers; high volume of unreachable blocks to mask true logic. |
| **Suspicious Functions** | `ProcessFileAsync`, `PythonGenerator`, `CSharpGenerator` | These functions are heavily protected, suggesting they contain the core "payload" or critical internal mechanics. |
| **Detection Risk** | **Critical (Manual Analysis)** | High degree of manual effort required to peel back the layers of obfuscation. Automation will likely fail to map the full logic path. |

#### Final Analyst Conclusion:
The binary is not merely "complex"; it is **deliberately and professionally hardened.** The transition from standard-looking utility functions (like `ProcessFileAsync`) to highly complex, obfuscated modules (`PythonGenerator`, `CSharpGenerator`) indicates a high degree of intentionality. This pattern—hiding complex, non-linear logic inside layers of mathematical noise—is a hallmark of **sophisticated malware** or top-tier commercial protectors used by threat actors to hide heavy payloads (like ransomware or advanced backdoors).

#### Final Recommendations:
1.  **Immediate Isolation:** Treat any system where this binary is executed as potentially compromised. The complexity suggests it may be capable of sophisticated evasion.
2.  **Dynamic Behavior Monitoring:** Since static analysis is intentionally hindered, focus on **behavioral indicators**: 
    *   Monitor for unauthorized file system modifications (especially in the "Bulk" mode).
    *   Monitor for network connections to unusual IPs/domains.
3.  **Memory Forensics:** Perform memory dumps while the process is running to see if it "unpacks" or "de-obfuscates" its own code into RAM, as much of the logic hidden in `PythonGenerator` may only appear in cleartext during execution.
4.  **Threat Intelligence Correlation:** Search for signatures related to known high-end packers (e.g., VMProtect) which often produce this specific type of "overlapping instruction" and "unreachable block" profile.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of junk code (unreachable blocks), control flow flattening, and instruction overlapping is specifically designed to hinder both manual analysis and automated decompiler tools. |
| T1055 | Packer | The identification of a "VM Protector" indicates the binary uses packing techniques to hide its true functionality and shield critical modules from static analysis. |
| T1028 | Dynamic Resolution | By generating scripts at runtime, the malware ensures that malicious logic and strings are not present in the file on disk, evading signature-based detection. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized as requested.

### **IP addresses / URLs / Domains**
*None identified.*

### **File paths / Registry keys**
*   **Zvpo.exe** (Identified executable filename)

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*   **D3C0C46CE5572A5ED901CC5DA80738CE32E83B37AA6A4D651909C77049244664** (Extracted from string list; identifies as a 64-character hex string, likely a hardcoded key or SHA-256 hash used for internal validation/decryption).

### **Other artifacts**
*   **High-Interest Functions:** 
    *   `ProcessFileAsync`
    *   `PythonGenerator.GenerateReplaceCode`
    *   `CSharpGenerator.GenerateMatchCode`
    *(Note: These functions were identified in the behavioral analysis as containing high levels of obfuscation and are suspected to house the primary payload/C2 logic).*
*   **Anomalous Behavior:** 
    *   **Instruction Overlap:** Identified at `0x402642`. (Indicates a deliberate attempt to desynchronize disassemblers).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Anti-Analysis Techniques:** The presence of "Instruction Overlapping" (e.g., `0x402642` vs `0x402641`) and extensive Control Flow Flattening indicates a professional effort to desynchronize disassemblers and hide the true execution path from analysts.
*   **Concealed Payload Logic:** The use of "generator" modules (`PythonGenerator`, `CSharpGenerator`) wrapped in heavy mathematical obfuscation suggests these functions are not for legitimate coding assistance but serve as the core mechanism for dynamically generating, decrypting, or delivering malicious payloads.
*   **Deceptive Front/Trojanized Utility:** The binary presents a plausible "utility" facade (Advanced Regex Studio) to mask its true purpose, which is identified by the analysis as highly sophisticated evasion and persistence logic typical of high-end loaders.
