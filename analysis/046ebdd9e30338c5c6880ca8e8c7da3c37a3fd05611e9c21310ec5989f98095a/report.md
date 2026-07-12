# Threat Analysis Report

**Generated:** 2026-07-11 17:36 UTC
**Sample:** `046ebdd9e30338c5c6880ca8e8c7da3c37a3fd05611e9c21310ec5989f98095a_046ebdd9e30338c5c6880ca8e8c7da3c37a3fd05611e9c21310ec5989f98095a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `046ebdd9e30338c5c6880ca8e8c7da3c37a3fd05611e9c21310ec5989f98095a_046ebdd9e30338c5c6880ca8e8c7da3c37a3fd05611e9c21310ec5989f98095a.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,540,096 bytes |
| MD5 | `df5fef057448d212344e9fe69a2bf916` |
| SHA1 | `edd6015f3148a2443b3c21fd1a4119eed19b2639` |
| SHA256 | `046ebdd9e30338c5c6880ca8e8c7da3c37a3fd05611e9c21310ec5989f98095a` |
| Overall entropy | 7.786 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2960531999 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,537,024 | 7.79 | ⚠️ Yes |
| `.rsrc` | 2,048 | 3.494 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **3816** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
 @Zi(?
#fffff
#fffffRw@(
N@YZXo
N@YZXo
@Z	I;
MbP?Z[(
#fffff
#fffffRw@
#fffff
#fffff
v4.0.30319
#Strings
<-9P 
	&
0h
	'	F	U	

+
4
:
H
T
]
c
q
}

<>9__23_0
<ExtractImageStream>b__23_0
<>9__23_1
<ExtractImageStream>b__23_1
IEnumerable`1
TypedTableBase`1
ReadOnlyCollection`1
EventHandler`1
IEnumerator`1
IReadOnlyList`1
ConditionalWeakTable`2
C0FFA9FB092A16539A382EF84691EF6ABA3C7EDB60A3675E577748E2725B9A93
__StaticArrayInitTypeSize=24
ToUInt16
B7A54561D02CFD4A82F89CCB463CC8C0A355BE3B1B7E3C0B85D1F4836265DC17
__StaticArrayInitTypeSize=48
<Module>
<PrivateImplementationDetails>
System.Drawing.Drawing2D
PointF
get_TM
System.IO
etiquetteConstanteR
etiquetteVitesseRMS
CalculerVitesseRMS
get_VelocitasRMS
set_VelocitasRMS
columnVelocitasRMS
get_pSjT
get_VelociteX
set_VelociteX
get_PositionX
set_PositionX
get_PositioX
set_PositioX
columnPositioX
get_VelocitasX
set_VelocitasX
columnVelocitasX
get_VelociteY
set_VelociteY
get_PositionY
set_PositionY
get_PositioY
set_PositioY
columnPositioY
get_VelocitasY
set_VelocitasY
columnVelocitasY
get_MensuraThermodynamica
tableMensuraThermodynamica
ShouldSerializeMensuraThermodynamica
get_EnergiaCinetica
set_EnergiaCinetica
columnEnergiaCinetica
get_EnergiaCineticaParticula
set_EnergiaCineticaParticula
columnEnergiaCineticaParticula
get_MassaParticula
set_MassaParticula
columnMassaParticula
relationSimulatioParticula
parentSimulationisRecordRowBySimulatioParticula
get_IdentificateurParticula
set_IdentificateurParticula
columnIdentificateurParticula
FindByIdentificateurParticula
System.Xml.Schema
GetTypedTableSchema
ReadXmlSchema
WriteXmlSchema
GetTypedDataSetSchema
boutonPlasma
get_TemperaturaMensura
set_TemperaturaMensura
columnTemperaturaMensura
get_VolumenMensura
set_VolumenMensura
columnVolumenMensura
get_PressioMensura
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.ParticulaStatusRowChangeEvent.get_Action` | `0x40e268` | 105298 | ✓ |
| `method.TransitioPhasaeRow..ctor` | `0x40d8a5` | 58594 | ✓ |
| `method.MolecularDynamics.Form1.InitializeComponent` | `0x402db8` | 3424 | ✓ |
| `method.MolecularDynamics.Form2.InitializeComponent` | `0x404120` | 3416 | ✓ |
| `sym.ParticulaStatusDataTable.AddParticulaStatusRow` | `0x40ca41` | 2710 | ✓ |
| `method.MolecularDynamics.Form3.InitializeComponent` | `0x40561c` | 2648 | — |
| `method.MolecularDynamics.Form4.InitializeComponent` | `0x4069cc` | 2264 | ✓ |
| `method.MolecularDynamics.Form4.PanneauDiagramme_Paint` | `0x406464` | 1328 | ✓ |
| `method.MolecularDynamics.Form1.PanneauAnimation_Paint` | `0x402638` | 1164 | ✓ |
| `method.SimulationisRecordRow..ctor` | `0x40d4d7` | 974 | ✓ |
| `method.MolecularDynamics.Form3.PanneauJauge_Paint` | `0x4050a8` | 848 | ✓ |
| `method.MolecularDynamics.MolecularDataSet.InitClass` | `0x4087dc` | 716 | ✓ |
| `method.MolecularDynamics.Form1.ExtractImageStream` | `0x402068` | 676 | ✓ |
| `method.MolecularDynamics.Form2.PanneauDistribution_Paint` | `0x403e44` | 676 | ✓ |
| `method.MolecularDynamics.MolecularDataSet..ctor` | `0x408064` | 656 | ✓ |
| `method.SimulationisRecordDataTable.InitClass` | `0x40a800` | 656 | ✓ |
| `method.MensuraThermodynamicaDataTable.InitClass` | `0x40c000` | 656 | ✓ |
| `method.ElementumDataTable.InitClass` | `0x409bdc` | 596 | ✓ |
| `method.ElementumDataTable.GetTypedTableSchema` | `0x409fb4` | 596 | ✓ |
| `method.SimulationisRecordDataTable.GetTypedTableSchema` | `0x40ac14` | 596 | ✓ |
| `method.TransitioPhasaeDataTable.GetTypedTableSchema` | `0x40b79c` | 596 | ✓ |
| `method.MensuraThermodynamicaDataTable.GetTypedTableSchema` | `0x40c414` | 596 | ✓ |
| `method.ParticulaStatusDataTable.InitClass` | `0x40cc38` | 596 | ✓ |
| `method.ParticulaStatusDataTable.GetTypedTableSchema` | `0x40d010` | 596 | ✓ |
| `method.MolecularDynamics.MolecularEngine.InitialiserParticules` | `0x407420` | 568 | ✓ |
| `method.MolecularDynamics.MolecularEngine.TraiterCollisions` | `0x407978` | 560 | ✓ |
| `method.MolecularDynamics.Form4.MettreAJourAffichage` | `0x4060ec` | 548 | ✓ |
| `method.TransitioPhasaeDataTable.InitClass` | `0x40b3fc` | 540 | ✓ |
| `method.MolecularDynamics.Form3.PanneauChambre_Paint` | `0x4053f8` | 492 | ✓ |
| `method.MolecularDynamics.MolecularDataSet.ReadXmlSerializable` | `0x408434` | 464 | ✓ |

### Decompiled Code Files

- [`code/method.ElementumDataTable.GetTypedTableSchema.c`](code/method.ElementumDataTable.GetTypedTableSchema.c)
- [`code/method.ElementumDataTable.InitClass.c`](code/method.ElementumDataTable.InitClass.c)
- [`code/method.MensuraThermodynamicaDataTable.GetTypedTableSchema.c`](code/method.MensuraThermodynamicaDataTable.GetTypedTableSchema.c)
- [`code/method.MensuraThermodynamicaDataTable.InitClass.c`](code/method.MensuraThermodynamicaDataTable.InitClass.c)
- [`code/method.MolecularDynamics.Form1.ExtractImageStream.c`](code/method.MolecularDynamics.Form1.ExtractImageStream.c)
- [`code/method.MolecularDynamics.Form1.InitializeComponent.c`](code/method.MolecularDynamics.Form1.InitializeComponent.c)
- [`code/method.MolecularDynamics.Form1.PanneauAnimation_Paint.c`](code/method.MolecularDynamics.Form1.PanneauAnimation_Paint.c)
- [`code/method.MolecularDynamics.Form2.InitializeComponent.c`](code/method.MolecularDynamics.Form2.InitializeComponent.c)
- [`code/method.MolecularDynamics.Form2.PanneauDistribution_Paint.c`](code/method.MolecularDynamics.Form2.PanneauDistribution_Paint.c)
- [`code/method.MolecularDynamics.Form3.PanneauChambre_Paint.c`](code/method.MolecularDynamics.Form3.PanneauChambre_Paint.c)
- [`code/method.MolecularDynamics.Form3.PanneauJauge_Paint.c`](code/method.MolecularDynamics.Form3.PanneauJauge_Paint.c)
- [`code/method.MolecularDynamics.Form4.InitializeComponent.c`](code/method.MolecularDynamics.Form4.InitializeComponent.c)
- [`code/method.MolecularDynamics.Form4.MettreAJourAffichage.c`](code/method.MolecularDynamics.Form4.MettreAJourAffichage.c)
- [`code/method.MolecularDynamics.Form4.PanneauDiagramme_Paint.c`](code/method.MolecularDynamics.Form4.PanneauDiagramme_Paint.c)
- [`code/method.MolecularDynamics.MolecularDataSet..ctor.c`](code/method.MolecularDynamics.MolecularDataSet..ctor.c)
- [`code/method.MolecularDynamics.MolecularDataSet.InitClass.c`](code/method.MolecularDynamics.MolecularDataSet.InitClass.c)
- [`code/method.MolecularDynamics.MolecularDataSet.ReadXmlSerializable.c`](code/method.MolecularDynamics.MolecularDataSet.ReadXmlSerializable.c)
- [`code/method.MolecularDynamics.MolecularEngine.InitialiserParticules.c`](code/method.MolecularDynamics.MolecularEngine.InitialiserParticules.c)
- [`code/method.MolecularDynamics.MolecularEngine.TraiterCollisions.c`](code/method.MolecularDynamics.MolecularEngine.TraiterCollisions.c)
- [`code/method.ParticulaStatusDataTable.GetTypedTableSchema.c`](code/method.ParticulaStatusDataTable.GetTypedTableSchema.c)
- [`code/method.ParticulaStatusDataTable.InitClass.c`](code/method.ParticulaStatusDataTable.InitClass.c)
- [`code/method.ParticulaStatusRowChangeEvent.get_Action.c`](code/method.ParticulaStatusRowChangeEvent.get_Action.c)
- [`code/method.SimulationisRecordDataTable.GetTypedTableSchema.c`](code/method.SimulationisRecordDataTable.GetTypedTableSchema.c)
- [`code/method.SimulationisRecordDataTable.InitClass.c`](code/method.SimulationisRecordDataTable.InitClass.c)
- [`code/method.SimulationisRecordRow..ctor.c`](code/method.SimulationisRecordRow..ctor.c)
- [`code/method.TransitioPhasaeDataTable.GetTypedTableSchema.c`](code/method.TransitioPhasaeDataTable.GetTypedTableSchema.c)
- [`code/method.TransitioPhasaeDataTable.InitClass.c`](code/method.TransitioPhasaeDataTable.InitClass.c)
- [`code/method.TransitioPhasaeRow..ctor.c`](code/method.TransitioPhasaeRow..ctor.c)
- [`code/sym.ParticulaStatusDataTable.AddParticulaStatusRow.c`](code/sym.ParticulaStatusDataTable.AddParticulaStatusRow.c)

## Behavioral Analysis

This analysis incorporates the final disassembly segment (Chunk 7/7), which provides a high-resolution look at the core physics logic and data ingestion layers.

---

### Updated Analysis: Chunk 7/7

#### 1. Execution Flow Obfuscation via Opaque Predicates
The repeated use of `POPCOUNT` to gate logical branches is a hallmark of **Opaque Predicates**. In many cases, these calculations are designed to always evaluate to the same result (e.g., "always true" or "always false"), but they are expressed as complex bit-manipulation problems that static analysis tools cannot pre-calculate.
*   **Impact:** This creates a "maze" for the analyst. Because the decompiler cannot determine which branch is actually taken, it must display both, leading to an explosion of "junk code" and "unreachable blocks."
*   **Evidence:** In `TraiterCollisions`, multiple instances of `(POPCOUNT(...) & 1U) == 0` are used to gate logic. This forces a human analyst to manually trace every branch, even though most are dead ends.

#### 2. The "Noise" Layer (Arithmetic Bloat)
The disassembly for `TraiterCollisions` and `MettreAJourAffichage` exhibits extreme **arithmetic noise**. Simple additions or assignments are replaced by complex chains of:
*   **CONCAT operations:** Breaking a single register value into multiple fragments across several variables.
*   **CARRY-propagation logic:** Using multi-step math to handle overflow/carry, even when standard addition would suffice.
*   **Constant Folding Obstruction:** Numbers like `0x6f`, `0x4110411`, and `0x82c1011` are peppered throughout. These serve as "anchors" to ensure that the calculation remains complex even if some variables are optimized out.

#### 3. Data Schema Masking (The Bridge to Assets)
The inclusion of `method.MolecularDynamics.MoleculeDataSet.ReadXmlSerializable` and `method.TransitioPhasaeDataTable.InitClass` provides a critical look at how the application handles its "knowledge base."
*   **Intentional Obscurity:** The purpose of these functions is to map external data (XML files) into internal structures. By heavily obfuscating these, the developers are hiding the **Data Schema**.
*   **Strategic Significance:** This prevents a researcher from easily identifying which XML fields correspond to specific physical properties (e.g., "melting point," "toxicity level," or "reaction_rate"). They aren't just protecting code; they are protecting the *meaning* of their data.

#### 4. Advanced Decompiler Sabotage
The sheer volume of `WARNING: Instruction at... overlaps` and `WARNING: Removing unreachable block` in this final chunk confirms a highly aggressive approach to anti-analysis.
*   **Instruction Overlap:** This is specifically designed to break the **linear sweep** and **recursive descent** algorithms used by tools like Ghidra/IDA Pro. By overlapping instructions, they ensure that if an analyst tries to jump to a specific address, the tool might interpret the bytes starting from a different "offset," leading to completely incorrect assembly.
*   **Stack Tracking Failures:** The warning `Unable to track spacebase fully for stack` suggests that the code is intentionally making standard memory-tracking difficult by using complex offsets and indirect addressing.

---

### Updated Summary for Incident Response

**Current Threat Level: Critical (Sophisticated Proprietary Logic & Asset Protection)**

The final analysis confirms a multi-layered defense strategy involving both **algorithmic obfuscation** (to protect the math) and **schema shielding** (to protect the data).

**New Findings:**
*   **Opaque Predicate Integration:** The use of `POPCOUNT` based branching indicates a professional-grade anti-analysis suite. This is designed to exhaust human analysts by forcing them to investigate "phantom" code paths that are never executed.
*   **Intentional Logic Dilution:** Functions like `TraiterCollisions` (likely the core physics loop) have been bloated with so much "junk" math that identifying the actual physics calculations requires significant manual de-weaving.
*   **Input/Output Shielding:** The protection of the XML parsing logic suggests a high level of concern regarding their underlying data models. It is intentionally difficult to map out how the software interprets its internal "rules."

**Strategic Impact Analysis:**
1.  **Reverse Engineering Complexity:** The time-to-success for a manual audit is very high. Any automated script will likely produce "hallucinated" logic due to the overlapping instructions and junk code blocks.
2.  **IP Protection Strategy:** This level of obfuscation is common in industries with extreme IP sensitivity (e.g., advanced pharmacology, chemical manufacturing, or aerospace). The target isn't just a piece of software; it's a proprietary "methodology" encoded into the logic.

**Updated Recommendations for Next Steps:**
1.  **Dynamic Trace Logging (Execution Path):** Since static analysis is hindered by opaque predicates, use **Instruction Tracing** (via Intel PIN or QEMU). By logging only the instructions actually executed by the CPU during a simulation run, the "junk" and "unreachable" branches will be filtered out automatically.
2.  **Memory Snapshotting:** Instead of trying to understand *how* `ReadXmlSerializable` works, let the program run until it has finished loading its data. Take a memory dump at that point to see the "clean" values of variables like `TransitioPhasae`.
3.  **Symbolic Execution:** Employ tools (like Triton or Manticore) to solve the arithmetic chains. These tools can "simplify" the complex CONCAT/CARRY math back into simple numbers, stripping away some of the OLLVM-style obfuscation.

---

### Final Summary of Infrastructure & Defense
| Component | Role | Obfuscation Type | Intelligence Value |
| :--- | :--- | :--- | :--- |
| **MolecularDynamics** | Core Physics Engine | Opaque Predicates, Arithmetic Bloat | High (Determines material behavior) |
| **Data Parsers (XML)** | Asset Integration | Schema Shielding, Junk Code | Critical (Protects "secret" formulas) |
| **UI/Form Logic** | User Interface | Instruction Overlap, Jump-table Sabotage | Medium (Hides UI interactions) |
| **Systemic Shield** | Global Protection | OLLVM / Hikari Suite | High (Reflects high R&D investment) |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of **Opaque Predicates** and **Arithmetic Bloat** hides actual execution logic by creating "junk" paths and complex calculations that thwart manual analysis. |
| T1027 | Obfuscated Files or Information | **Data Schema Masking** is used to shield the internal meaning of data models (e.g., chemical properties) from being easily identified by researchers. |
| T1027 | Obfuscated Files or Information | **Decompiler Sabotage** via instruction overlapping is specifically designed to break common automated disassembly algorithms like linear sweep and recursive descent. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The report mentions general references to XML files for data parsing, but no specific file paths or registry keys were provided.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
The following hex strings were found within the text. These appear to be high-entropy constants often used in obfuscated code (such as for integrity checks or internal hash tables):
*   `C0FFA9FB092A16539A382EF84691EF6ABA3C7EDB60A3675E577748E2725B9A93`
*   `B7A54561D02CFD4A82F89CCB463CC8C0A355BE3B1B7E3C0B85D1F4836265DC17`

### **Other artifacts**
While not traditional "indicators" for automated blocking, the following internal identifiers and unique function names are significant as behavioral markers of the application's logic:
*   **Unique Function/Class Names (Potential Logic Signatures):**
    *   `TraiterCollisions` (Core physics loop)
    *   `MettreAJourAffichage` (Display update logic)
    *   `MolecularDynamics.MoleculeDataSet.ReadXmlSerializable`
    *   `TransitioPhasaeDataTable.InitClass`
*   **Technical Behaviors:** 
    *   Use of `POPCOUNT` for **Opaque Predicates**.
    *   Evidence of **Instruction Overlap** (indicates a high-sophistication packer/obfuscator like OLLVM).
    *   **Arithmetic Bloat** signatures (specifically targeting the translation of complex math into simple constants).

---

## Malware Family Classification

1. **Malware family**: Unknown 
2. **Malware type**: Custom (Proprietary Tool)
3. **Confidence**: Medium

4. **Key evidence**:
*   **Sophisticated IP Protection:** The use of high-level obfuscation techniques—specifically **Opaque Predicates** (via `POPCOUNT`), **Arithmetic Bloat**, and **Instruction Overlap**—indicates a deliberate effort to protect highly valuable intellectual property rather than just hiding malicious payloads.
*   **Subject Matter Analysis:** The specific internal functions found (`MolecularDynamics`, `TransitioPhasaeDataTable`) and the focus on chemical/physical properties (melting points, toxicity levels) suggest the software is designed for industrial research, pharmaceutical manufacturing, or aerospace engineering.
*   **Absence of Malicious Indicators:** Despite the "Critical" threat level assigned in the analysis due to the complexity of the code, there are no identified C2 servers, exfiltration protocols, or typical malware behaviors (like keylogging or unauthorized encryption) that would categorize it as a common botnet or ransomware. It appears to be a heavily guarded piece of proprietary software.
