# Threat Analysis Report

**Generated:** 2026-09-06 09:34 UTC
**Sample:** `14d8b15c4be76ef562899bab4de96509e3c8d168de0e4a0043b30191239fedee_14d8b15c4be76ef562899bab4de96509e3c8d168de0e4a0043b30191239fedee.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14d8b15c4be76ef562899bab4de96509e3c8d168de0e4a0043b30191239fedee_14d8b15c4be76ef562899bab4de96509e3c8d168de0e4a0043b30191239fedee.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 1,917,952 bytes |
| MD5 | `a6f91fa0879ebba68c0cce12aa4b0043` |
| SHA1 | `7a16e486f73f191e3fd9a63f69fe6012b154f067` |
| SHA256 | `14d8b15c4be76ef562899bab4de96509e3c8d168de0e4a0043b30191239fedee` |
| Overall entropy | 7.956 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1765541745 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,915,392 | 7.957 | ⚠️ Yes |
| `.rsrc` | 2,048 | 3.447 | No |

## Extracted Strings

Total strings found: **4467** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc

X )UU
"33s?Z}

ZiXsI
v4.0.30319
#Strings
<>c__DisplayClass8_0
<DecodeMatrix>b__0
<>9__8_1
<DecodeMatrix>b__8_1
IEnumerable`1
EqualityComparer`1
List`1
<>f__AnonymousType0`2
Func`2
get_V6
<Module>
System.Drawing.Drawing2D
get_uLHW
mittelpunktX
mittelpunktY
get_DarkMagenta
FromArgb
mscorlib
System.Collections.Generic
Microsoft.VisualBasic
Thread
get_Red
get_OrangeRed
get_DarkRed
set_Enabled
<Plane>i__Field
<Limit>i__Field
get_Gold
get_Hand
get_DarkGoldenrod
CreateInstance
GetHashCode
set_SmoothingMode
LinearGradientMode
get_FlascheModeeee
get_Orange
get_DarkOrange
ZeichneFlasche
Invoke
Enumerable
IDisposable
RuntimeTypeHandle
GetTypeFromHandle
FillRectangle
get_ClientRectangle
DrawRectangle
set_BorderStyle
set_FormBorderStyle
set_FlatStyle
FontStyle
txtSpielerName
spielerName
CallByName
get_Plane
fluxPlane
CallType
System.Core
Restore
get_Culture
set_Culture
resourceCulture
ButtonBase
TextBoxBase
Dispose
FillEllipse
DrawEllipse
Invalidate
DebuggerBrowsableState
EditorBrowsableState
GraphicsState
get_White
spielerListe
AktualisiereSpielerliste
STAThreadAttribute
CompilerGeneratedAttribute
GuidAttribute
GeneratedCodeAttribute
DebuggerNonUserCodeAttribute
DebuggableAttribute
DebuggerBrowsableAttribute
EditorBrowsableAttribute
ComVisibleAttribute
AssemblyTitleAttribute
AssemblyTrademarkAttribute
TargetFrameworkAttribute
DebuggerHiddenAttribute
AssemblyFileVersionAttribute
AssemblyConfigurationAttribute
AssemblyDescriptionAttribute
CompilationRelaxationsAttribute
AssemblyProductAttribute
AssemblyCopyrightAttribute
DebuggerDisplayAttribute
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x140002162` | 115188 | ✓ |
| `method.__c__DisplayClass8_0._DecodeMatrix_b__0` | `0x14000416c` | 57334 | ✓ |
| `method.__c._DecodeMatrix_b__8_1` | `0x1400041b1` | 12288 | ✓ |
| `method.FlaschenDrehen.SpielerListeForm.btnZurueck_Click` | `0x140003079` | 2712 | ✓ |
| `method.FlaschenDrehen.HauptForm..ctor` | `0x14000217d` | 2052 | ✓ |
| `method.FlaschenDrehen.SpielerListeForm..ctor` | `0x140002981` | 1784 | ✓ |
| `method.FlaschenDrehen.SpielerListeForm.InitialisiereKomponenten` | `0x14000299c` | 1352 | ✓ |
| `method.FlaschenDrehen.ErgebnisForm..ctor` | `0x140003b11` | 1338 | ✓ |
| `method.FlaschenDrehen.HauptForm.InitialisiereKomponenten` | `0x140002450` | 1152 | ✓ |
| `method.FlaschenDrehen.FlascheSpielForm.InitialisiereKomponenten` | `0x1400031d4` | 984 | ✓ |
| `method.FlaschenDrehen.ErgebnisForm.InitialisiereKomponenten` | `0x140003b30` | 924 | ✓ |
| `method.FlaschenDrehen.HauptForm.DecodeMatrix` | `0x1400021a0` | 688 | ✓ |
| `method.FlaschenDrehen.FlascheSpielForm.spielBereich_Paint` | `0x140003674` | 364 | ✓ |
| `method.FlaschenDrehen.FlascheSpielForm.ZeichneFlasche` | `0x1400037e0` | 288 | ✓ |
| `method.FlaschenDrehen.FlascheSpielForm.animationsTimer_Tick` | `0x1400039bc` | 288 | ✓ |
| `method.FlaschenDrehen.ErgebnisForm.bildBox_Paint` | `0x140003ecc` | 260 | ✓ |
| `method.FlaschenDrehen.SpielerListeForm.btnHinzufuegen_Click` | `0x140002ee4` | 240 | ✓ |
| `method.FlaschenDrehen.SpielerListeForm.AktualisiereSpielerliste` | `0x140003084` | 240 | ✓ |
| `method.FlaschenDrehen.FlascheSpielForm.InitialisiereSpiel` | `0x1400035ac` | 200 | ✓ |
| `method.__f__AnonymousType0_2.GetHashCode` | `0x1400020bf` | 190 | ✓ |
| `method.FlaschenDrehen.FlascheSpielForm.btnDrehen_Click` | `0x140003900` | 188 | ✓ |
| `method.FlaschenDrehen.SpielerListeForm.btnEntfernen_Click` | `0x140002fd4` | 176 | ✓ |
| `method.FlaschenDrehen.ErgebnisForm.farbTimer_Tick` | `0x140003fd0` | 156 | ✓ |
| `method.FlaschenDrehen.Properties.Resources.set_Culture` | `0x1400040cb` | 150 | ✓ |
| `method.__f__AnonymousType0_2.ToString` | `0x1400020f4` | 110 | ✓ |
| `method.FlaschenDrehen.Properties.Resources..ctor` | `0x140004061` | 106 | ✓ |
| `method.FlaschenDrehen.FlascheSpielForm..ctor` | `0x140003180` | 84 | ✓ |
| `method.FlaschenDrehen.FlascheSpielForm.btnZurueck_Click` | `0x140003adc` | 84 | ✓ |
| `method.__f__AnonymousType0_2.Equals` | `0x140002070` | 79 | ✓ |
| `method.FlaschenDrehen.HauptForm.btnBeenden_Click` | `0x140002950` | 76 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.FlaschenDrehen.ErgebnisForm..ctor.c`](code/method.FlaschenDrehen.ErgebnisForm..ctor.c)
- [`code/method.FlaschenDrehen.ErgebnisForm.InitialisiereKomponenten.c`](code/method.FlaschenDrehen.ErgebnisForm.InitialisiereKomponenten.c)
- [`code/method.FlaschenDrehen.ErgebnisForm.bildBox_Paint.c`](code/method.FlaschenDrehen.ErgebnisForm.bildBox_Paint.c)
- [`code/method.FlaschenDrehen.ErgebnisForm.farbTimer_Tick.c`](code/method.FlaschenDrehen.ErgebnisForm.farbTimer_Tick.c)
- [`code/method.FlaschenDrehen.FlascheSpielForm..ctor.c`](code/method.FlaschenDrehen.FlascheSpielForm..ctor.c)
- [`code/method.FlaschenDrehen.FlascheSpielForm.InitialisiereKomponenten.c`](code/method.FlaschenDrehen.FlascheSpielForm.InitialisiereKomponenten.c)
- [`code/method.FlaschenDrehen.FlascheSpielForm.InitialisiereSpiel.c`](code/method.FlaschenDrehen.FlascheSpielForm.InitialisiereSpiel.c)
- [`code/method.FlaschenDrehen.FlascheSpielForm.ZeichneFlasche.c`](code/method.FlaschenDrehen.FlascheSpielForm.ZeichneFlasche.c)
- [`code/method.FlaschenDrehen.FlascheSpielForm.animationsTimer_Tick.c`](code/method.FlaschenDrehen.FlascheSpielForm.animationsTimer_Tick.c)
- [`code/method.FlaschenDrehen.FlascheSpielForm.btnDrehen_Click.c`](code/method.FlaschenDrehen.FlascheSpielForm.btnDrehen_Click.c)
- [`code/method.FlaschenDrehen.FlascheSpielForm.btnZurueck_Click.c`](code/method.FlaschenDrehen.FlascheSpielForm.btnZurueck_Click.c)
- [`code/method.FlaschenDrehen.FlascheSpielForm.spielBereich_Paint.c`](code/method.FlaschenDrehen.FlascheSpielForm.spielBereich_Paint.c)
- [`code/method.FlaschenDrehen.HauptForm..ctor.c`](code/method.FlaschenDrehen.HauptForm..ctor.c)
- [`code/method.FlaschenDrehen.HauptForm.DecodeMatrix.c`](code/method.FlaschenDrehen.HauptForm.DecodeMatrix.c)
- [`code/method.FlaschenDrehen.HauptForm.InitialisiereKomponenten.c`](code/method.FlaschenDrehen.HauptForm.InitialisiereKomponenten.c)
- [`code/method.FlaschenDrehen.HauptForm.btnBeenden_Click.c`](code/method.FlaschenDrehen.HauptForm.btnBeenden_Click.c)
- [`code/method.FlaschenDrehen.Properties.Resources..ctor.c`](code/method.FlaschenDrehen.Properties.Resources..ctor.c)
- [`code/method.FlaschenDrehen.Properties.Resources.set_Culture.c`](code/method.FlaschenDrehen.Properties.Resources.set_Culture.c)
- [`code/method.FlaschenDrehen.SpielerListeForm..ctor.c`](code/method.FlaschenDrehen.SpielerListeForm..ctor.c)
- [`code/method.FlaschenDrehen.SpielerListeForm.AktualisiereSpielerliste.c`](code/method.FlaschenDrehen.SpielerListeForm.AktualisiereSpielerliste.c)
- [`code/method.FlaschenDrehen.SpielerListeForm.InitialisiereKomponenten.c`](code/method.FlaschenDrehen.SpielerListeForm.InitialisiereKomponenten.c)
- [`code/method.FlaschenDrehen.SpielerListeForm.btnEntfernen_Click.c`](code/method.FlaschenDrehen.SpielerListeForm.btnEntfernen_Click.c)
- [`code/method.FlaschenDrehen.SpielerListeForm.btnHinzufuegen_Click.c`](code/method.FlaschenDrehen.SpielerListeForm.btnHinzufuegen_Click.c)
- [`code/method.FlaschenDrehen.SpielerListeForm.btnZurueck_Click.c`](code/method.FlaschenDrehen.SpielerListeForm.btnZurueck_Click.c)
- [`code/method.__c._DecodeMatrix_b__8_1.c`](code/method.__c._DecodeMatrix_b__8_1.c)
- [`code/method.__c__DisplayClass8_0._DecodeMatrix_b__0.c`](code/method.__c__DisplayClass8_0._DecodeMatrix_b__0.c)
- [`code/method.__f__AnonymousType0_2.Equals.c`](code/method.__f__AnonymousType0_2.Equals.c)
- [`code/method.__f__AnonymousType0_2.GetHashCode.c`](code/method.__f__AnonymousType0_2.GetHashCode.c)
- [`code/method.__f__AnonymousType0_2.ToString.c`](code/method.__f__AnonymousType0_2.ToString.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary:

### Core Functionality
The binary appears to be a **graphical user interface (GUI) application**, likely a game or interactive tool, written in .NET (C# or VB.NET). The German labels and naming conventions suggest it is titled "FlaschenDrehen" (Bottle Turning), which typically refers to a game where a bottle is spun to select a player (common in social settings).

The code includes:
*   **User Interface Management:** Several forms are defined, including `HauptForm` (Main Form), `SpielerListeForm` (Player List Form), and `ErgebnisForm` (Result Form).
*   **Game Logic/Graphics:** Functions like `ZeichneFlasche` (Draw Bottle) and `spielBereich_Paint` indicate the program renders graphics and handles animations.
*   **Interaction Handling:** There are standard UI button interactions for "Back" (`btnZurueck`), "Add" (`btnHinzufuegen`), "Turn/Spin" (`btnDrehen`), and "Exit" (`btnBeenden`).
*   **Timer Events:** The `farbTimer_Tick` suggests a timed event, likely for visual effects or state changes in the game.

### Suspicious or Malicious Behaviors
While no overt malicious actions (such as file encryption, credential stealing, or command execution) are present in this specific snippet, there are several indicators of **obfuscation**:

*   **Decompilation Noise:** The high frequency of `halt_baddata()` and "Bad instruction" warnings indicates that the binary has been processed by an **obfuscator** or a packer. This is used to confuse disassemblers (like IDA or Ghidra) and automated analysis tools.
*   **Overlapping Instructions:** Errors like `Instruction at (ram,0x0001400030b1) overlaps instruction at (ram,0x0001400030b0)` are a common technique used in "junk code" insertion to break the linear flow of disassembly, making it harder for an analyst to follow.
*   **Obfuscated Logic Blocks:** Functions like `DecodeMatrix` and those containing complex bitwise operations/conversions (e.g., `CONCAT`, `POPCNT`) that do not seem directly related to "drawing a bottle" may be used to hide underlying logic or represent packed code being unpacked into memory.

### Notable Techniques
*   **Standard .NET Framework Usage:** The presence of many `System.*` and `Microsoft.VisualBasic` namespaces indicates the use of standard libraries for window management, graphics, and internationalization.
*   **Obfuscation Layers:** The "messy" nature of the decompiled C code (repetitive logic in different functions like `btnZurueck_Click`) suggests that the original source was modified to hide its structure. This is a common tactic used by both game developers to protect IP and malware authors to hide malicious functionality behind a layer of "junk" code.

### Summary for Analyst
The sample presents as a **seemingly harmless German-language game** about spinning a bottle. However, the **heavy use of obfuscation techniques** (junk instructions, overlapping memory addresses, and complex bitwise operations) suggests that it was designed to resist analysis. 

In a professional triage context, this sample would be flagged for further dynamic analysis to determine if the "obfuscated" sections are simply protecting game logic or hiding a malicious payload.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of junk instructions, "bad data" indicators, and complex bitwise operations is intended to hinder disassembly and hide the true logic of the code. |
| T1055 | Packing | The report specifically notes that the binary appears to have been processed by an obfuscator or packer to evade automated analysis tools. |
| T1036 | Masquerading | The application presents as a harmless social game ("FlaschenDrehen") to blend in with legitimate software and avoid suspicion during initial triage. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The analysis identifies several behaviors highly indicative of malicious intent (e.g., use of junk code, overlapping instructions, and obfuscation), but these are **behavioral indicators** rather than static IOCs like specific IPs or hashes.

### **IP addresses / URLs / Domains**
*   None detected.

### **File paths / Registry keys**
*   `Desp.exe` (Note: This is the filename of the binary; no specific directory path was provided).

### **Mutex names / Named pipes**
*   None detected.

### **Hashes**
*   None detected.

### **Other artifacts**
*   **Suspicious Function/Module:** `DecodeMatrix` (Identified in analysis as a potential component for unpacking or hiding logic via bitwise operations).
*   **Obfuscation Technique:** Use of "junk code" and overlapping instructions to bypass linear disassembly tools.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / dropper
3. **Confidence**: Medium

4. **Key evidence**:
*   **Masquerading and Obfuscation:** The binary presents a benign front (a German social game, "FlaschenDrehen") while employing advanced anti-analysis techniques, including junk code, overlapping instructions, and `halt_baddata` markers to hide its true logic.
*   **Suspicious Payload Decryption:** The presence of the `DecodeMatrix` function combined with complex bitwise operations suggests that the "game" UI is a wrapper used to conceal a secondary payload being unpacked in memory.
*   **Atypical Implementation:** The discrepancy between a simple game's requirements and the high level of deliberate obfuscation (T1027, T1055) strongly indicates it is designed as a loader or dropper rather than a standalone legitimate application.
