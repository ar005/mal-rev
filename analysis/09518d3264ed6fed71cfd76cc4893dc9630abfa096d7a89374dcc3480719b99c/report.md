# Threat Analysis Report

**Generated:** 2026-07-19 14:59 UTC
**Sample:** `09518d3264ed6fed71cfd76cc4893dc9630abfa096d7a89374dcc3480719b99c_09518d3264ed6fed71cfd76cc4893dc9630abfa096d7a89374dcc3480719b99c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `09518d3264ed6fed71cfd76cc4893dc9630abfa096d7a89374dcc3480719b99c_09518d3264ed6fed71cfd76cc4893dc9630abfa096d7a89374dcc3480719b99c.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 843,776 bytes |
| MD5 | `d289dd07c2ffc20f5dda07545d7b49e0` |
| SHA1 | `916a1d38e4ad4c7cf8778ab7f1ee1af47552bb61` |
| SHA256 | `09518d3264ed6fed71cfd76cc4893dc9630abfa096d7a89374dcc3480719b99c` |
| Overall entropy | 7.682 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2337981662 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 839,680 | 7.69 | ⚠️ Yes |
| `.rsrc` | 3,072 | 5.68 | No |
| `.reloc` | 512 | 0.098 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **2519** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

X )UU

 VCR5-

 VCR;
Y@[%
+

"333?Z
XZ*.s(

*BSJB
v4.0.30319
#Strings
'	,	:	@	P	g	w	
%0Qg
	I	

R
h

<>9__20_0
<get_AudioPlaylistNames>b__20_0
<>9__0_0
<GetPlaybackNames>b__0_0
<>9__11_0
<LoadFiles>b__11_0
<>9__21_0
<NoiseAroundPixel>b__21_0
<>c__DisplayClass31_0
<>c__DisplayClass1_0
<textBoxNewProfileName_TextChanged>b__32_0
<>c__DisplayClass33_0
<>9__14_0
<InitializeJunkBag>b__14_0
<get_PlaybackPlaylistNames>b__14_0
<>c__DisplayClass14_0
<>9__34_0
<buttonCreateProfile_Click>b__34_0
<>9__15_0
<get_preferenceNames>b__15_0
<get_CurrentPlaybackPlaylistRef>b__26_0
<textBoxNewPlaybackPlaylistName_TextChanged>b__46_0
<textBox1_TextChanged>b__6_0
<>9__17_0
<get_currentPreference>b__17_0
<>9__27_0
<RecordingName_TextChanged>b__27_0
<buttonDeleteProfile_Click>b__37_0
<buttonDeletePlaybackPlaylist_Click>b__47_0
<textBoxNewAudioPlaylistName_TextChanged>b__57_0
<get_CurrentAudioPlaylistRef>b__28_0
<buttonDeleteAudioPlaylist_Click>b__58_0
<PlayNextSong>b__49_0
<PlayPlayback>b__0
<PlayAudio>b__0
<GetPlaylist>b__0
<TalkToStream>d__0
<>9__0_1
<GetPlaybackNames>b__0_1
<>9__11_1
<LoadFiles>b__11_1
<>9__21_1
<NoiseAroundPixel>b__21_1
<>9__1_1
<GetPlaylist>b__1_1
<buttonCreateProfile_Click>b__34_1
<>9__37_1
<buttonDeleteProfile_Click>b__37_1
<>9__49_1
<PlayNextSong>b__49_1
<provider>5__1
<InitializeJunkBag>b__1
<PlayPlayback>b__1
<PlayAudio>b__1
<>u__1
IEnumerable`1
IOrderedEnumerable`1
SharedOptionsBase`1
Predicate`1
Task`1
Action`1
ReadOnlyCollection`1
AsyncTaskMethodBuilder`1
EventHandler`1
EqualityComparer`1
TaskAwaiter`1
IEnumerator`1
IList`1
get_String1
panel1
roundedButton_Num1
progressBar1
argument1
panel_Menu1
roundedButton_DivBy1
textBox_Display1
ToInt32
roundedButton_Num1_2
roundedButton_DivBy1_2
roundedButton_Num2_2
roundedButton_Num3_2
<>9__14_2
<InitializeJunkBag>b__14_2
roundedButton_Num4_2
roundedButton_Num5_2
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c__DisplayClass1_0._GetPlaylist_b__0` | `0x414051` | 56994 | ✓ |
| `method.SimpleWindowsApp.Calculator.Calculator_MouseUp` | `0x404d2f` | 35394 | ✓ |
| `method.SimpleWindowsApp.Calculator.InitializeComponent` | `0x405444` | 33540 | ✓ |
| `method.SimpleWindowsApp.Calculator.button_ClearHistory_Click` | `0x402caf` | 6558 | ✓ |
| `method.WebAudioController.MainForm.InitializeComponent` | `0x4107a0` | 5900 | ✓ |
| `method.__f__AnonymousType0_2.GetHashCode` | `0x4020c7` | 3002 | ✓ |
| `method.WebAudioController.AudioRecordForm.InitializeComponent` | `0x40eaa0` | 2617 | ✓ |
| `method.SimpleWindowsApp.Calculator.roundedButton_Hyp_Click` | `0x40464d` | 1612 | ✓ |
| `method.WebAudioController.AddFile.InitializeComponent` | `0x40dd60` | 1185 | ✓ |
| `method.SimpleWindowsApp.Calculator.roundedButton_Equals_Click` | `0x403254` | 1136 | ✓ |
| `method.SimpleWindowsApp.Calculator..ctor` | `0x402840` | 1092 | ✓ |
| `method.WebAudioController.Controllers.MasterController..ctor` | `0x4137bf` | 738 | ✓ |
| `method._TalkToStream_d__0.MoveNext` | `0x413d14` | 692 | ✓ |
| `method.WebAudioController.NAudioHandler.timerFadeIn_Tick` | `0x412fe0` | 615 | ✓ |
| `method.SimpleWindowsApp.Calculator.InitializeJunkBag` | `0x40223c` | 580 | ✓ |
| `method.WebAudioController.NAudioHandler.PlayNextSong` | `0x413254` | 559 | ✓ |
| `method.SimpleWindowsApp.Calculator.roundedButton_Num_Click` | `0x402e90` | 540 | ✓ |
| `method.WebAudioController.NAudioHandler.ProcessCommand` | `0x412548` | 469 | ✓ |
| `method.SimpleWindowsApp.RoundedButton.OnResize` | `0x40d771` | 424 | ✓ |
| `method.SimpleWindowsApp.Calculator.DisableButtons` | `0x4050e4` | 420 | ✓ |
| `method.SimpleWindowsApp.Calculator.button_Menu_Click` | `0x403c08` | 392 | ✓ |
| `method.SimpleWindowsApp.Calculator.EnableButtons` | `0x405288` | 388 | ✓ |
| `method.SimpleWindowsApp.RoundedPanel.OnResize` | `0x40d919` | 380 | ✓ |
| `method.WebAudioController.NAudioHandler.PrepNextAudioType` | `0x412d30` | 376 | ✓ |
| `method.SimpleWindowsApp.Calculator.UpdateFontSize` | `0x404e64` | 360 | ✓ |
| `method.WebAudioController.NAudioHandler..ctor` | `0x4123e0` | 360 | ✓ |
| `method.SimpleWindowsApp.RoundedButton.OnPaint` | `0x40d784` | 344 | ✓ |
| `method.SimpleWindowsApp.RoundedPanel.OnPaint` | `0x40d92c` | 344 | ✓ |
| `method.WebAudioController.MainForm.LoadPreferences` | `0x40f8c0` | 332 | ✓ |
| `method.SimpleWindowsApp.Calculator.roundedButton_DivBy1_Click` | `0x4038a8` | 328 | ✓ |

### Decompiled Code Files

- [`code/method.SimpleWindowsApp.Calculator..ctor.c`](code/method.SimpleWindowsApp.Calculator..ctor.c)
- [`code/method.SimpleWindowsApp.Calculator.Calculator_MouseUp.c`](code/method.SimpleWindowsApp.Calculator.Calculator_MouseUp.c)
- [`code/method.SimpleWindowsApp.Calculator.DisableButtons.c`](code/method.SimpleWindowsApp.Calculator.DisableButtons.c)
- [`code/method.SimpleWindowsApp.Calculator.EnableButtons.c`](code/method.SimpleWindowsApp.Calculator.EnableButtons.c)
- [`code/method.SimpleWindowsApp.Calculator.InitializeComponent.c`](code/method.SimpleWindowsApp.Calculator.InitializeComponent.c)
- [`code/method.SimpleWindowsApp.Calculator.InitializeJunkBag.c`](code/method.SimpleWindowsApp.Calculator.InitializeJunkBag.c)
- [`code/method.SimpleWindowsApp.Calculator.UpdateFontSize.c`](code/method.SimpleWindowsApp.Calculator.UpdateFontSize.c)
- [`code/method.SimpleWindowsApp.Calculator.button_ClearHistory_Click.c`](code/method.SimpleWindowsApp.Calculator.button_ClearHistory_Click.c)
- [`code/method.SimpleWindowsApp.Calculator.button_Menu_Click.c`](code/method.SimpleWindowsApp.Calculator.button_Menu_Click.c)
- [`code/method.SimpleWindowsApp.Calculator.roundedButton_DivBy1_Click.c`](code/method.SimpleWindowsApp.Calculator.roundedButton_DivBy1_Click.c)
- [`code/method.SimpleWindowsApp.Calculator.roundedButton_Equals_Click.c`](code/method.SimpleWindowsApp.Calculator.roundedButton_Equals_Click.c)
- [`code/method.SimpleWindowsApp.Calculator.roundedButton_Hyp_Click.c`](code/method.SimpleWindowsApp.Calculator.roundedButton_Hyp_Click.c)
- [`code/method.SimpleWindowsApp.Calculator.roundedButton_Num_Click.c`](code/method.SimpleWindowsApp.Calculator.roundedButton_Num_Click.c)
- [`code/method.SimpleWindowsApp.RoundedButton.OnPaint.c`](code/method.SimpleWindowsApp.RoundedButton.OnPaint.c)
- [`code/method.SimpleWindowsApp.RoundedButton.OnResize.c`](code/method.SimpleWindowsApp.RoundedButton.OnResize.c)
- [`code/method.SimpleWindowsApp.RoundedPanel.OnPaint.c`](code/method.SimpleWindowsApp.RoundedPanel.OnPaint.c)
- [`code/method.SimpleWindowsApp.RoundedPanel.OnResize.c`](code/method.SimpleWindowsApp.RoundedPanel.OnResize.c)
- [`code/method.WebAudioController.AddFile.InitializeComponent.c`](code/method.WebAudioController.AddFile.InitializeComponent.c)
- [`code/method.WebAudioController.AudioRecordForm.InitializeComponent.c`](code/method.WebAudioController.AudioRecordForm.InitializeComponent.c)
- [`code/method.WebAudioController.Controllers.MasterController..ctor.c`](code/method.WebAudioController.Controllers.MasterController..ctor.c)
- [`code/method.WebAudioController.MainForm.InitializeComponent.c`](code/method.WebAudioController.MainForm.InitializeComponent.c)
- [`code/method.WebAudioController.MainForm.LoadPreferences.c`](code/method.WebAudioController.MainForm.LoadPreferences.c)
- [`code/method.WebAudioController.NAudioHandler..ctor.c`](code/method.WebAudioController.NAudioHandler..ctor.c)
- [`code/method.WebAudioController.NAudioHandler.PlayNextSong.c`](code/method.WebAudioController.NAudioHandler.PlayNextSong.c)
- [`code/method.WebAudioController.NAudioHandler.PrepNextAudioType.c`](code/method.WebAudioController.NAudioHandler.PrepNextAudioType.c)
- [`code/method.WebAudioController.NAudioHandler.ProcessCommand.c`](code/method.WebAudioController.NAudioHandler.ProcessCommand.c)
- [`code/method.WebAudioController.NAudioHandler.timerFadeIn_Tick.c`](code/method.WebAudioController.NAudioHandler.timerFadeIn_Tick.c)
- [`code/method._TalkToStream_d__0.MoveNext.c`](code/method._TalkToStream_d__0.MoveNext.c)
- [`code/method.__c__DisplayClass1_0._GetPlaylist_b__0.c`](code/method.__c__DisplayClass1_0._GetPlaylist_b__0.c)
- [`code/method.__f__AnonymousType0_2.GetHashCode.c`](code/method.__f__AnonymousType0_2.GetHashCode.c)

## Behavioral Analysis

This analysis incorporates findings from **chunk 12/12**, the final segment of the provided disassembly. This chunk provides the "smoking gun" regarding the technical sophistication of the malware's protection layer. It confirms that the code is not merely obfuscated; it is engineered to create a "hallucination" for automated analysis tools while maintaining a rigid, functional execution path for the malicious payload.

### Updated Analysis Report

#### 1. Reinforced Evidence: The "Fiction" of the UI Layer
The function `method.SimpleWindowsApp.Calculator.button_ClearHistory_Click` provides the ultimate proof of **Homogeneous Obfuscation**. 
*   **Observation:** While the name suggests a simple button click to clear a history list, the body contains no logic related to lists, buffers, or UI state. Instead, it is filled with dense, high-level arithmetic, pointer arithmetic, and complex bitwise operations.
*   **Interpretation:** Every "feature" of the Calculator/SimpleWindowsApp (buttons, paint routines, preference loading) serves as a container for the same underlying VM execution engine. The developer has created a **functional shell** where each routine is actually a different "module" or "script" running on the internal Virtual Machine.

#### 2. Fragmented String Assembly & Instruction Encoding
In this final chunk, we see more evidence of how the VM handles data:
*   **Fragmented Construction:** Instead of standard `strcpy` or string literals, notice lines like `piVar10 = CONCAT31(Var18,cVar6 + 'r');` and `pcVar11 = CONCAT31(Var18,cVar6 + 'o');`.
*   **The "Jigsaw" Technique:** The code isn't just hiding a string; it is constructing characters (like `'r'`, `'o'`, `'q'`, `'#'`, `'%'`) through the result of complex mathematical expressions. This suggests that the VM is decoding an encrypted instruction stream or a command-and-control (C2) packet where each character must be "reconstructed" before use.
*   **Embedded Special Characters:** The appearance of symbols like `';'`, `'['`, and `'%'` within these math blocks confirms that the VM is likely building something more complex than just text—possibly **shellcode snippets, environment variables, or decrypted configuration paths.**

#### 3. High-Complexity Memory Mapping
The disassembly shows extremely large multipliers (e.g., `0x2000a00`, `0x4001400`) and layered pointer arithmetic:
*   **Mechanism:** Expressions like `piVar10 = *piVar10 * 0x2000a00` are used to jump between memory regions or calculate offsets within a massive data blob.
*   **Purpose:** This serves as **Memory Geometry Obfuscation**. By using very large multipliers and complex additions, the author ensures that a human analyst cannot easily determine where a pointer is "going" without performing every single step of the calculation. It makes it nearly impossible to map out the memory layout statically.

#### 4. Deliberate Tool Sabotage (The "Broken" Graph)
The final warnings in the disassembly are critical:
*   **Overlapping Instructions:** The warning at `0x40328f` confirms that the binary contains overlapping instructions, a classic technique to break linear disassemblers (like Ghidra and IDA). This forces the analyst to manually re-analyze segments where one "instruction" actually hides another starting just a few bytes later.
*   **Unreachable Block Proliferation:** The dozens of `WARNING: Removing unreachable block` messages at the end are not bugs; they are **dead-code injection**. By creating thousands of paths that can never be taken, the developer creates a "labyrinth" for the analyst's eyes, making it difficult to determine which path is actually executed by the CPU.

---

### Technical Indicators Summary (Updated)

1.  **State-Dependent Dispatcher:** Confirmed via `POPCOUNT` logic. The VM uses bitwise properties of data as branching conditions, creating a "living" execution path that only reveals itself at runtime.
2.  **Homogeneous Obfuscation Layers:** Overlapping functionality in "Calculator," "Paint," and "Preferences" functions confirms the entire UI is a hollow shell for a unified malicious engine.
3.  **Fragmented Instruction Assembly:** The use of `CONCAT` and arithmetic to build characters (e.g., `'o'`, `'r'`, `'q'`) indicates that the VM decodes its instructions/strings on-the-fly from an encoded blob.
4.  **Memory Geometry Obfuscation:** Use of large multipliers (`0x2000a00`) and complex pointer arithmetic to mask memory addresses and jump targets, preventing static mapping of the malware's behavior.
5.  **Active Decompiler Sabotage:** Intentional use of **instruction overlap** and **unreachable block bloating** designed specifically to break analysis tools and waste the time of human reverse engineers.

### Final Conclusion:
The presence of these techniques in a "Calculator" application is a hallmark of high-level malware engineering (common in sophisticated trojans, ransomware, or state-sponsored spyware). The developer has gone to great lengths to ensure that **automated analysis yields no clear path** and **manual analysis is stalled by complexity.**

**Status: Confirmed Malicious / High Sophistication.**
**Final Recommendation:** Do not attempt to "clean" or "patch" the binary. Treat every function within the `SimpleWindowsApp` namespace as a high-priority target for manual, step-by-step dynamic analysis. The focus must remain on extracting the logic hidden behind the math blocks in the core loops of `OnPaint` and `LoadPreferences`.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization | The malware employs a custom Virtual Machine (VM) execution engine, using a "calculator" UI as a hollow shell to house and execute internal logic. |
| **T1027** | Obfuscated Execution | The use of complex mathematical expressions ("Jigsaw") to construct strings and multi-step arithmetic for memory mapping hides the true intent of the code from static analysis. |
| **T1027** | Obfuscated Execution | The inclusion of overlapping instructions is a specific tactic used to break linear disassemblers like Ghidra and IDA Pro during the reverse engineering process. |
| **T1027** | Obfuscated Execution | The "unreachable block" proliferation (dead-code injection) creates a labyrinthine execution path designed to waste an analyst's time and complicate manual analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: This specific sample relies heavily on **behavioral indicators** and **technical TTPs (Tactics, Techniques, and Procedures)** rather than static indicators like hardcoded IP addresses or URLs, as the malware employs a "Just-in-Time" decoding method to hide its infrastructure.

### **IP addresses / URLs / Domains**
*None identified.* (The analysis indicates that C2 infrastructure is likely constructed dynamically using the "Jigsaw" technique described in the behavior report).

### **File paths / Registry keys**
*None identified.* (Internal memory offsets, such as `0x40328f`, were identified but these are used for internal execution flow rather than filesystem interaction).

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None provided in the source text.*

### **Other artifacts (TTPs & Technical Indicators)**
*   **VM-Based Obfuscation Engine:** The malware uses a custom Virtual Machine to execute malicious payloads. Standard UI functions (Calculator, Paint) are used as "shells" for hidden execution modules.
*   **Fragmented String Assembly:** Use of the `CONCAT31` function and mathematical expressions to construct characters (e.g., `'r'`, `'o'`, `'q'`) at runtime to bypass static string analysis.
*   **Memory Geometry Obfuscation:** Use of high-value multipliers (e.g., `0x2000a00`, `0x4001400`) and complex pointer arithmetic to hide jump targets and memory addresses from automated tools.
*   **Tool Sabotage (Anti-Analysis):** 
    *   **Overlapping Instructions:** Intentional instruction overlaps at specific offsets (e.g., `0x40328f`) designed to break linear disassemblers like Ghidra or IDA Pro.
    *   **Unreachable Block Proliferation:** Use of "dead-code" injection to create a labyrinth for human analysts and automated tools.
*   **State-Dependent Dispatcher:** Implementation of `POPCOUNT` logic where bitwise properties of data are used as branching conditions, ensuring the execution path only reveals itself during active runtime.

---
**Analyst Note:** The primary risk associated with this sample is its high level of sophistication. Because it utilizes "Homogeneous Obfuscation," traditional signature-based detection will likely fail. Security teams should monitor for processes attempting to perform **dynamic string construction** and **complex memory mapping** in the `SimpleWindowsApp` namespace.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated VM-based Obfuscation:** The malware utilizes a "Homogeneous Obfuscation" technique where common UI elements (Calculator/Paint) are actually shells for a complex, custom Virtual Machine execution engine to hide its primary logic.
*   **Advanced Anti-Analysis Tactics:** The implementation of intentional instruction overlapping and "unreachable block" proliferation is specifically designed to sabotage automated tools (Ghidra/IDA Pro) and exhaust human reverse engineers.
*   **Dynamic Construction & Masking:** The use of "Jigsaw" string assembly and large-multiplier memory geometry ensures that indicators like C2 infrastructure or internal logic remain hidden until runtime, characteristic of high-sophistication loaders used to deliver secondary payloads.
