# Threat Analysis Report

**Generated:** 2026-08-15 09:23 UTC
**Sample:** `0ee1d5d6cd40ca035ae628632e2ccab0733f04d4a0d6c21a705993166c29761f_0ee1d5d6cd40ca035ae628632e2ccab0733f04d4a0d6c21a705993166c29761f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ee1d5d6cd40ca035ae628632e2ccab0733f04d4a0d6c21a705993166c29761f_0ee1d5d6cd40ca035ae628632e2ccab0733f04d4a0d6c21a705993166c29761f.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 1,134,592 bytes |
| MD5 | `9197456b2b82d4b900cdee86fe753d53` |
| SHA1 | `3054fbd7a8309ff5cc30db325e50053eb0377740` |
| SHA256 | `0ee1d5d6cd40ca035ae628632e2ccab0733f04d4a0d6c21a705993166c29761f` |
| Overall entropy | 7.662 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 4141132264 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,132,544 | 7.666 | ⚠️ Yes |
| `.rsrc` | 1,536 | 4.11 | No |

## Extracted Strings

Total strings found: **2792** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
*f )UU

X )UU
4{ )UU

X )UU

X )UU

X )UU

X )UU

X )UU

X )UU

#aTR'
	Y
	(B
lmjABZ
lmjABZ
lmjABZ
lmjABZ~r
lmjABZ
lmjABZ
lmjABZ
lmjABZ~r
lmjABZ#p
lmjABZ
~r
lmjAB[

#fffff
#m`@iGs`@}
)ej\@}
T}{F@}

*BSJB
v4.0.30319
#Strings
	;	S	d	m	t	

B
W
e
k
q

*Hm
EpoqueJ2000
<>9__4_10
<DisassembleImageData>b__4_10
<>9__5_10
<ExtractPixelComponents>b__5_10
<>9__4_20
<DisassembleImageData>b__4_20
<>9__4_30
<DisassembleImageData>b__4_30
<>9__4_0
<DisassembleImageData>b__4_0
<>c__DisplayClass4_0
<>9__15_0
<InitializeComponent>b__15_0
<>9__5_0
<ExtractPixelComponents>b__5_0
<>c__DisplayClass5_0
<>9__5_11
<ExtractPixelComponents>b__5_11
<DisassembleImageData>b__11
<>9__4_21
<DisassembleImageData>b__4_21
<>9__4_31
<DisassembleImageData>b__4_31
<>9__4_1
<DisassembleImageData>b__4_1
<>c__DisplayClass4_1
<>9__15_1
<InitializeComponent>b__15_1
<>9__5_1
<ExtractPixelComponents>b__5_1
<>c__DisplayClass5_1
IEnumerable`1
IOrderedEnumerable`1
IQueryable`1
TypedTableBase`1
Stack`1
EqualityComparer`1
List`1
get_DataTable1
tableDataTable1
ShouldSerializeDataTable1
get_Item1
get_DataColumn1
set_DataColumn1
columnDataColumn1
CS$<>8__locals1
DataSet1
<>9__5_12
<ExtractPixelComponents>b__5_12
<DisassembleImageData>b__12
<>9__4_22
<DisassembleImageData>b__4_22
<>9__4_32
<DisassembleImageData>b__4_32
<>9__4_2
<DisassembleImageData>b__4_2
<>c__DisplayClass4_2
<>9__15_2
<InitializeComponent>b__15_2
<>9__5_2
<ExtractPixelComponents>b__5_2
<>c__DisplayClass5_2
<>f__AnonymousType0`2
<>f__AnonymousType1`2
<>f__AnonymousType4`2
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c__DisplayClass5_5..ctor` | `0x14000ae28` | 66902 | ✓ |
| `method.__c__DisplayClass5_5._ExtractPixelComponents_b__18` | `0x14000ae31` | 52094 | ✓ |
| `method.PlanetCalculator.Form3.InitializeComponent` | `0x1400054f0` | 3853 | ✓ |
| `method.PlanetCalculator.Form2.InitializeComponent` | `0x14000444c` | 3367 | ✓ |
| `method.PlanetCalculator.Form1.InitializeComponent` | `0x140003410` | 3185 | ✓ |
| `sym.DataTable2DataTable.AddDataTable2Row` | `0x1400095ed` | 2766 | ✓ |
| `method.PlanetCalculator.MoteurPlanetaire..cctor` | `0x1400080f0` | 2190 | ✓ |
| `method.PlanetCalculator.Form4.InitializeComponent` | `0x140006988` | 1630 | ✓ |
| `method.PlanetCalculator.MoteurPlanetaire.ObtenirAlignementHistoriques` | `0x140007bec` | 900 | ✓ |
| `method.PlanetCalculator.Form2.boutonRechercher_Click` | `0x140004184` | 656 | ✓ |
| `method.PlanetCalculator.Form4.grilleHistorique_SelectionChanged` | `0x14000652c` | 620 | ✓ |
| `method.DataTable1DataTable.GetTypedTableSchema` | `0x140008fc0` | 596 | ✓ |
| `method.DataTable2DataTable.GetTypedTableSchema` | `0x140009aac` | 596 | ✓ |
| `method.PlanetCalculator.Form1.DisassembleImageData` | `0x140002e6c` | 552 | ✓ |
| `method.PlanetCalculator.MoteurPlanetaire.CalculerPositionPlanete` | `0x140007240` | 492 | ✓ |
| `method.PlanetCalculator.DataSet1..ctor` | `0x140002704` | 468 | ✓ |
| `method.PlanetCalculator.Form4.boutonVerifier_Click` | `0x140006798` | 440 | ✓ |
| `method.DataTable2DataTable.InitClass` | `0x14000977c` | 428 | ✓ |
| `method.PlanetCalculator.DataSet1.GetTypedDataSetSchema` | `0x140002c84` | 408 | ✓ |
| `method.DataTable1RowChangeEvent..ctor` | `0x14000a2d5` | 390 | ✓ |
| `method.PlanetCalculator.Form1.ExtractPixelComponents` | `0x140003094` | 369 | ✓ |
| `method.PlanetCalculator.Form1.ActualiserPositions` | `0x140003210` | 364 | ✓ |
| `method.PlanetCalculator.MoteurPlanetaire.RechercherAlignements` | `0x140007544` | 364 | ✓ |
| `method.PlanetCalculator.MoteurPlanetaire.CalculerForceGravite` | `0x140007790` | 332 | ✓ |
| `method.__c._ExtractPixelComponents_b__5_8` | `0x14000aa65` | 312 | ✓ |
| `method.__c._DisassembleImageData_b__4_19` | `0x14000a869` | 310 | ✓ |
| `method.__c__DisplayClass4_4..ctor` | `0x14000a54b` | 308 | ✓ |
| `method.PlanetCalculator.DataSet1.ReadXmlSerializable` | `0x1400029d0` | 284 | ✓ |
| `method.PlanetCalculator.MoteurPlanetaire.CalculerJourJulien` | `0x14000705c` | 268 | ✓ |
| `method.PlanetCalculator.Form4.RemplirGrilleHistorique` | `0x14000642c` | 256 | ✓ |

### Decompiled Code Files

- [`code/method.DataTable1DataTable.GetTypedTableSchema.c`](code/method.DataTable1DataTable.GetTypedTableSchema.c)
- [`code/method.DataTable1RowChangeEvent..ctor.c`](code/method.DataTable1RowChangeEvent..ctor.c)
- [`code/method.DataTable2DataTable.GetTypedTableSchema.c`](code/method.DataTable2DataTable.GetTypedTableSchema.c)
- [`code/method.DataTable2DataTable.InitClass.c`](code/method.DataTable2DataTable.InitClass.c)
- [`code/method.PlanetCalculator.DataSet1..ctor.c`](code/method.PlanetCalculator.DataSet1..ctor.c)
- [`code/method.PlanetCalculator.DataSet1.GetTypedDataSetSchema.c`](code/method.PlanetCalculator.DataSet1.GetTypedDataSetSchema.c)
- [`code/method.PlanetCalculator.DataSet1.ReadXmlSerializable.c`](code/method.PlanetCalculator.DataSet1.ReadXmlSerializable.c)
- [`code/method.PlanetCalculator.Form1.ActualiserPositions.c`](code/method.PlanetCalculator.Form1.ActualiserPositions.c)
- [`code/method.PlanetCalculator.Form1.DisassembleImageData.c`](code/method.PlanetCalculator.Form1.DisassembleImageData.c)
- [`code/method.PlanetCalculator.Form1.ExtractPixelComponents.c`](code/method.PlanetCalculator.Form1.ExtractPixelComponents.c)
- [`code/method.PlanetCalculator.Form1.InitializeComponent.c`](code/method.PlanetCalculator.Form1.InitializeComponent.c)
- [`code/method.PlanetCalculator.Form2.InitializeComponent.c`](code/method.PlanetCalculator.Form2.InitializeComponent.c)
- [`code/method.PlanetCalculator.Form2.boutonRechercher_Click.c`](code/method.PlanetCalculator.Form2.boutonRechercher_Click.c)
- [`code/method.PlanetCalculator.Form3.InitializeComponent.c`](code/method.PlanetCalculator.Form3.InitializeComponent.c)
- [`code/method.PlanetCalculator.Form4.InitializeComponent.c`](code/method.PlanetCalculator.Form4.InitializeComponent.c)
- [`code/method.PlanetCalculator.Form4.RemplirGrilleHistorique.c`](code/method.PlanetCalculator.Form4.RemplirGrilleHistorique.c)
- [`code/method.PlanetCalculator.Form4.boutonVerifier_Click.c`](code/method.PlanetCalculator.Form4.boutonVerifier_Click.c)
- [`code/method.PlanetCalculator.Form4.grilleHistorique_SelectionChanged.c`](code/method.PlanetCalculator.Form4.grilleHistorique_SelectionChanged.c)
- [`code/method.PlanetCalculator.MoteurPlanetaire..cctor.c`](code/method.PlanetCalculator.MoteurPlanetaire..cctor.c)
- [`code/method.PlanetCalculator.MoteurPlanetaire.CalculerForceGravite.c`](code/method.PlanetCalculator.MoteurPlanetaire.CalculerForceGravite.c)
- [`code/method.PlanetCalculator.MoteurPlanetaire.CalculerJourJulien.c`](code/method.PlanetCalculator.MoteurPlanetaire.CalculerJourJulien.c)
- [`code/method.PlanetCalculator.MoteurPlanetaire.CalculerPositionPlanete.c`](code/method.PlanetCalculator.MoteurPlanetaire.CalculerPositionPlanete.c)
- [`code/method.PlanetCalculator.MoteurPlanetaire.ObtenirAlignementHistoriques.c`](code/method.PlanetCalculator.MoteurPlanetaire.ObtenirAlignementHistoriques.c)
- [`code/method.PlanetCalculator.MoteurPlanetaire.RechercherAlignements.c`](code/method.PlanetCalculator.MoteurPlanetaire.RechercherAlignements.c)
- [`code/method.__c._DisassembleImageData_b__4_19.c`](code/method.__c._DisassembleImageData_b__4_19.c)
- [`code/method.__c._ExtractPixelComponents_b__5_8.c`](code/method.__c._ExtractPixelComponents_b__5_8.c)
- [`code/method.__c__DisplayClass4_4..ctor.c`](code/method.__c__DisplayClass4_4..ctor.c)
- [`code/method.__c__DisplayClass5_5..ctor.c`](code/method.__c__DisplayClass5_5..ctor.c)
- [`code/method.__c__DisplayClass5_5._ExtractPixelComponents_b__18.c`](code/method.__c__DisplayClass5_5._ExtractPixelComponents_b__18.c)
- [`code/sym.DataTable2DataTable.AddDataTable2Row.c`](code/sym.DataTable2DataTable.AddDataTable2Row.c)

## Behavioral Analysis

Based on the analysis of the second chunk of disassembly and integration with your previous findings, here is the updated report.

---

### Updated Analysis Report: Project "PlanetCalculator" (Obfuscated .NET)

The addition of the second code segment confirms several high-level technical concerns regarding the construction of this binary. While the **functional intent** remains rooted in astronomical calculations, the **implementation method** strongly suggests a sophisticated attempt to thwart static analysis and reverse engineering.

#### 1. Core Functionality and Purpose (Updated)
The core functionality remains consistent with your previous finding: it is an astronomy-themed application.
*   **Astronomical Logic:** The function `CalculerJourJulien` (Calculate Julian Day) is a standard fundamental calculation in orbital mechanics to convert dates into a continuous count of days. 
*   **User Interface (UI):** The function `RemplirGrilleHistorique` ("Fill History Grid") confirms the application populates data into visual UI elements (likely tables or grids).
*   **Internal Consistency:** Despite the heavy obfuscation, the naming convention remains in French, and the organization of classes (`MoteurPlanetaire`, `Form4`) suggests a cohesive, structured project.

#### 2. Enhanced Analysis of Suspicious Behaviors
The second chunk provides more evidence regarding how the application protects its logic:

*   **Instruction Overlapping/Junk Code:** The disassembly for `CalculerJourJulien` is filled with nonsensical operations such as `*CONCAT44(in_register_00000004,in_EAX)`. These are not standard C# or even standard high-level assembly constructs. They represent **junk instructions**—code designed to be executed by the CPU but misinterpreted by a disassembler (like Ghidra or IDA Pro).
*   **Anti-Disassembly Traps:** The repeated `WARNING: Bad instruction - Truncating control flow here` and `halt_baddata()` warnings are critical indicators. This happens when the developer uses "overlapping instructions," where a jump is designed to land in the middle of what looks like another instruction. This confuses the linear sweep or recursive traversal used by decompilers, effectively "breaking" the tool's ability to map the logic accurately.
*   **Opaque Predicates:** The complex bitwise operations (e.g., `in_EAX >> 8`, `CONCAT31`) may be part of **opaque predicates**. These are mathematical calculations that always evaluate to a known result but are too complex for a static analysis tool to simplify, forcing the tool to generate "spaghetti" code during decompression/de-obfuscation.

#### 3. Technical Patterns and Advanced Techniques
The specific techniques observed in this chunk indicate high-level protection:

*   **Anti-Analysis via Obfuscated .NET:** While the .NET framework is usually easy to decompile (using tools like dnSpy), this binary has been processed by a protector that targets both the **IL (Intermediate Language)** and the **native machine code**.
*   **Logic Hiding through "Mangled" Code:** In `CalculerJourJulien`, what should be a simple mathematical formula is wrapped in dozens of lines of noise. This is a common tactic to hide sensitive algorithms—such as proprietary orbital models or, if repurposed for malware, encryption keys or command-and-control (C2) logic.
*   **Targeted Obstruction:** The fact that the disassembler fails *immediately* at certain points (`halt_baddata()`) suggests a "trap" system. If an analyst tries to step through the code in a debugger, these junk instructions may be skipped or correctly executed by the CPU, but they appear as "broken" to any tool attempting to visualize the flow beforehand.

#### 4. Updated Conclusion
The sample remains a **highly obfuscated .NET application**. 

**Risk Assessment:**
While the "astronomy" theme is clearly present in the metadata and naming conventions, the **method of protection is characteristic of high-end malware or strictly protected commercial software.** The use of instruction overlapping and junk code to break disassemblers indicates a developer who specifically intends to prevent others from analyzing the code. 

**Recommendation:**
Because the disassembly is so heavily mangled by "bad instruction" traps, **static analysis alone is insufficient.** To determine if there is a hidden malicious payload (such as an injected dropper or secondary payload), dynamic analysis in a controlled sandbox—specifically monitoring network activity and file system changes while the app runs—is required. The "astronomy" features may serve as a legitimate front for potentially unauthorized background activities.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of junk instructions, overlapping code (to break disassemblers), and opaque predicates is designed to hide logic from static analysis. |
| T1036 | Masquerading | The "astronomy" theme and consistent naming conventions may serve as a front to conceal the true purpose or hidden functionality of the software. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. 

Based on the content provided, there are **no conventional infrastructure IOCs** (such as hardcoded IP addresses, URLs, or file paths) present in this specific data set. The report describes an obfuscated sample where much of the true malicious behavior is hidden behind anti-analysis techniques.

However, for the purposes of signature generation and threat actor tracking, the following internal identifiers and behavioral patterns have been extracted:

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *No cryptographic hashes (MD5/SHA1/SHA256) were present in the provided strings.*

### **Other artifacts**
**Internal Identifiers & Signature Potential:**
The following terms are unique to this specific binary's compilation and can be used for creating YARA rules or identifying related variants:
*   **Project Name:** `PlanetCalculator` (Used as a primary identifier for the internal project/module).
*   **Specific Function Names:** 
    *   `CalculerJourJulien` (Calculation of Julian Day)
    *   `RemplirGrilleHistorique` (Populating history grids)
    *   `MoteurPlanetaire` (Planetary engine module)
*   **Obfuscation Indicators (TTPs):** 
    *   Usage of **Instruction Overlapping** and **Junk Code** (e.g., `*CONCAT44`, `CONCAT31`).
    *   Presence of **Opaque Predicates**.
    *   Implementation of **Anti-Disassembly Traps** intended to break linear sweep and recursive traversal in tools like Ghidra or IDA Pro.

---
**Analyst Note:** The absence of network indicators suggests that this sample may be a "loader" or its communication logic is heavily obfuscated/encrypted, requiring dynamic analysis (sandbox execution) to extract real-time C2 infrastructure.

---

## Malware Family Classification

Based on the provided analysis report, here is the classification for the sample:

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: Medium-High
4. **Key evidence**:
    *   **Advanced Anti-Analysis Techniques:** The use of instruction overlapping, junk code (`*CONCAT44`), and opaque predicates is a deliberate attempt to "break" disassemblers (like Ghidra/IDA Pro), which is characteristic of high-end malware designed to hide its true logic from security researchers.
    *   **Masquerading (T1036):** The application uses a coherent "astronomy" theme and consistent naming conventions (`MoteurPlanetaire`) as a front, a classic tactic used to provide a plausible reason for the software's existence while hiding malicious background activities or secondary payloads.
    *   **Obfuscated Execution Flow:** The analyst notes that the lack of clear network indicators combined with extreme obfuscation suggests the binary is designed to hide its communication logic (C2) and likely serves as a vehicle to deliver other components.
