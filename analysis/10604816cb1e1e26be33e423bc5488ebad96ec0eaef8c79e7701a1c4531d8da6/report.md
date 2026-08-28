# Threat Analysis Report

**Generated:** 2026-08-18 21:05 UTC
**Sample:** `10604816cb1e1e26be33e423bc5488ebad96ec0eaef8c79e7701a1c4531d8da6_10604816cb1e1e26be33e423bc5488ebad96ec0eaef8c79e7701a1c4531d8da6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10604816cb1e1e26be33e423bc5488ebad96ec0eaef8c79e7701a1c4531d8da6_10604816cb1e1e26be33e423bc5488ebad96ec0eaef8c79e7701a1c4531d8da6.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 1,207,808 bytes |
| MD5 | `af24ceac3e510aa1d2922d77effd3401` |
| SHA1 | `829aa08c24d1c35c42258eca3b05d2abb621737a` |
| SHA256 | `10604816cb1e1e26be33e423bc5488ebad96ec0eaef8c79e7701a1c4531d8da6` |
| Overall entropy | 7.668 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1775197635 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,199,616 | 7.68 | ⚠️ Yes |
| `.rsrc` | 7,680 | 4.298 | No |

## Extracted Strings

Total strings found: **2572** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc

X )UU
MbP?Z
+
v4.0.30319
#Strings
<>9__7_10
<HarvestImageData>b__7_10
lblUnidadW0
<>9__7_0
<HarvestImageData>b__7_0
<>c__DisplayClass7_0
columnParametroG1
parametroG1
lblResG1
txtResG1
lblUnidadR1
<>c__DisplayClass7_1
<HarvestImageData>b__1
IEnumerable`1
EqualityComparer`1
List`1
_vRadioCurvatura1
toolStripStatusLabel1
lblRadioEspejo1
txtRadioEspejo1
statusStrip1
CS$<>8__locals1
columnParametroG2
parametroG2
lblResG2
txtResG2
_vFactorCalidadM2
lblFactorM2
columnFactorM2
txtFactorM2
factorM2
lblUnidadR2
<>c__DisplayClass7_2
<HarvestImageData>b__2
<>f__AnonymousType0`2
Func`2
_vRadioCurvatura2
irradiancia_Wm2
densidadPotencia_Wm2
columnDensidadPotenciaMedia_Wm2
columnDensidadPotenciaPico_Wm2
columnFluencia_Jcm2
CalcularFluencia_Jcm2
ConvertirAIrradiancia_Wcm2
columnIrradiancia_Wcm2
lblRadioEspejo2
txtRadioEspejo2
<HarvestImageData>b__3
Func`3
<>9__7_4
<HarvestImageData>b__7_4
<>9__7_5
<HarvestImageData>b__7_5
<>9__7_6
<HarvestImageData>b__7_6
<HarvestImageData>b__7
<>9__8
<HarvestImageData>b__8
<HarvestImageData>b__9
<Module>
lblUnidadLC
CalcularParametroG
columnProductoG
lblResProductoG
txtResProductoG
columnEnergiaPulso_J
energiaPulso_J
lblUnidadLO
CalcularBPP
lblResBPP
txtResBPP
columnParametroHazBPP
CalcularFactorQ
lblResFSR
txtResFSR
btnCalcularCW
potencia_W
columnPotenciaPico_W
columnPotenciaLaser_W
lblResRadioEnZ
txtResRadioEnZ
_vCinturaOptica
lblUnidadLambda
FrecuenciaALongitudOnda
lblLongitudOnda
txtLongitudOnda
CalcularNumeroOnda
lblResIrradiancia
txtResIrradiancia
lblDistancia
CalcularRadioHazEnDistancia
txtDistancia
CalcularMediaDivergencia
btnDivergencia
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__f__AnonymousType0_2.get_i` | `0x140002048` | 106096 | ✓ |
| `method.__c__DisplayClass7_0._HarvestImageData_b__8` | `0x14000b213` | 33336 | ✓ |
| `method.DensidadPotenciaDataTable.get_FechaCalculoColumn` | `0x14000becc` | 24956 | ✓ |
| `method.__f__AnonymousType0_2.GetHashCode` | `0x1400020bf` | 13942 | ✓ |
| `method.LaserCalculator.Form3..ctor` | `0x140007d73` | 13028 | ✓ |
| `method.LaserCalculator.Form1.InitializeComponent` | `0x140002e00` | 10624 | ✓ |
| `method.LaserCalculator.Form3.InitializeComponent` | `0x140007dc4` | 10608 | ✓ |
| `method.LaserCalculator.Form2.InicializarMotorDatos` | `0x14000575b` | 9752 | ✓ |
| `method.LaserCalculator.Form2.InitializeComponent` | `0x140005d84` | 8200 | ✓ |
| `method.LaserCalculator.Form1.btnCalcular_Click` | `0x14000264c` | 912 | ✓ |
| `method.LaserCalculator.Form2.btnCalcular_Click` | `0x140005884` | 740 | ✓ |
| `method.CavidadLaserDataTable..ctor` | `0x14000b350` | 720 | ✓ |
| `method.DensidadPotenciaDataTable..ctor` | `0x14000bb08` | 676 | ✓ |
| `method.DivergenciaHazDataTable..ctor` | `0x14000b770` | 632 | ✓ |
| `method.LaserCalculator.Form1.cboPresetLaser_SelectedIndexChanged` | `0x140002458` | 500 | ✓ |
| `method.LaserCalculator.Form1.btnGuardar_Click` | `0x140002ad0` | 480 | ✓ |
| `method.LaserCalculator.Form2.btnGuardar_Click` | `0x140005c18` | 308 | ✓ |
| `method.LaserCalculator.Form1.ConfigurarEstiloGrilla` | `0x140002354` | 260 | ✓ |
| `method.LaserCalculator.Form2.ConfigurarEstiloGrilla` | `0x140005780` | 260 | ✓ |
| `method.LaserCalculator.Form1.btnLimpiar_Click` | `0x1400029dc` | 244 | ✓ |
| `method.LaserCalculator.Form1.btnExportarXml_Click` | `0x140002cb0` | 224 | ✓ |
| `method.LaserCalculator.Form1.HarvestImageData` | `0x14000219c` | 218 | ✓ |
| `method.LaserCalculator.Form1.CargarPresetsLaser` | `0x14000229c` | 184 | ✓ |
| `method.LaserCalculator.Form2.btnLimpiar_Click` | `0x140005b68` | 176 | ✓ |
| `method.LaserCalculator.LaserEngine.CalcularCinturaHaz` | `0x14000a7c4` | 172 | ✓ |
| `entry0` | `0x14000b057` | 132 | ✓ |
| `method.__f__AnonymousType0_2.Equals` | `0x140002070` | 132 | ✓ |
| `method.LaserCalculator.LaserEngine.CalcularMediaDivergencia` | `0x14000a9a8` | 132 | ✓ |
| `method.LaserCalculator.Properties.Resources.set_Culture` | `0x14000b0db` | 128 | ✓ |
| `method.__c__DisplayClass7_0._HarvestImageData_b__2` | `0x14000b19d` | 118 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.CavidadLaserDataTable..ctor.c`](code/method.CavidadLaserDataTable..ctor.c)
- [`code/method.DensidadPotenciaDataTable..ctor.c`](code/method.DensidadPotenciaDataTable..ctor.c)
- [`code/method.DensidadPotenciaDataTable.get_FechaCalculoColumn.c`](code/method.DensidadPotenciaDataTable.get_FechaCalculoColumn.c)
- [`code/method.DivergenciaHazDataTable..ctor.c`](code/method.DivergenciaHazDataTable..ctor.c)
- [`code/method.LaserCalculator.Form1.CargarPresetsLaser.c`](code/method.LaserCalculator.Form1.CargarPresetsLaser.c)
- [`code/method.LaserCalculator.Form1.ConfigurarEstiloGrilla.c`](code/method.LaserCalculator.Form1.ConfigurarEstiloGrilla.c)
- [`code/method.LaserCalculator.Form1.HarvestImageData.c`](code/method.LaserCalculator.Form1.HarvestImageData.c)
- [`code/method.LaserCalculator.Form1.InitializeComponent.c`](code/method.LaserCalculator.Form1.InitializeComponent.c)
- [`code/method.LaserCalculator.Form1.btnCalcular_Click.c`](code/method.LaserCalculator.Form1.btnCalcular_Click.c)
- [`code/method.LaserCalculator.Form1.btnExportarXml_Click.c`](code/method.LaserCalculator.Form1.btnExportarXml_Click.c)
- [`code/method.LaserCalculator.Form1.btnGuardar_Click.c`](code/method.LaserCalculator.Form1.btnGuardar_Click.c)
- [`code/method.LaserCalculator.Form1.btnLimpiar_Click.c`](code/method.LaserCalculator.Form1.btnLimpiar_Click.c)
- [`code/method.LaserCalculator.Form1.cboPresetLaser_SelectedIndexChanged.c`](code/method.LaserCalculator.Form1.cboPresetLaser_SelectedIndexChanged.c)
- [`code/method.LaserCalculator.Form2.ConfigurarEstiloGrilla.c`](code/method.LaserCalculator.Form2.ConfigurarEstiloGrilla.c)
- [`code/method.LaserCalculator.Form2.InicializarMotorDatos.c`](code/method.LaserCalculator.Form2.InicializarMotorDatos.c)
- [`code/method.LaserCalculator.Form2.InitializeComponent.c`](code/method.LaserCalculator.Form2.InitializeComponent.c)
- [`code/method.LaserCalculator.Form2.btnCalcular_Click.c`](code/method.LaserCalculator.Form2.btnCalcular_Click.c)
- [`code/method.LaserCalculator.Form2.btnGuardar_Click.c`](code/method.LaserCalculator.Form2.btnGuardar_Click.c)
- [`code/method.LaserCalculator.Form2.btnLimpiar_Click.c`](code/method.LaserCalculator.Form2.btnLimpiar_Click.c)
- [`code/method.LaserCalculator.Form3..ctor.c`](code/method.LaserCalculator.Form3..ctor.c)
- [`code/method.LaserCalculator.Form3.InitializeComponent.c`](code/method.LaserCalculator.Form3.InitializeComponent.c)
- [`code/method.LaserCalculator.LaserEngine.CalcularCinturaHaz.c`](code/method.LaserCalculator.LaserEngine.CalcularCinturaHaz.c)
- [`code/method.LaserCalculator.LaserEngine.CalcularMediaDivergencia.c`](code/method.LaserCalculator.LaserEngine.CalcularMediaDivergencia.c)
- [`code/method.LaserCalculator.Properties.Resources.set_Culture.c`](code/method.LaserCalculator.Properties.Resources.set_Culture.c)
- [`code/method.__c__DisplayClass7_0._HarvestImageData_b__2.c`](code/method.__c__DisplayClass7_0._HarvestImageData_b__2.c)
- [`code/method.__c__DisplayClass7_0._HarvestImageData_b__8.c`](code/method.__c__DisplayClass7_0._HarvestImageData_b__8.c)
- [`code/method.__f__AnonymousType0_2.Equals.c`](code/method.__f__AnonymousType0_2.Equals.c)
- [`code/method.__f__AnonymousType0_2.GetHashCode.c`](code/method.__f__AnonymousType0_2.GetHashCode.c)
- [`code/method.__f__AnonymousType0_2.get_i.c`](code/method.__f__AnonymousType0_2.get_i.c)

## Behavioral Analysis

Based on the disassembly and string analysis of the provided binary sample, here is a technical breakdown of its functionality:

### Core Functionality and Purpose
The code appears to be an **engineering tool for laser physics and optics calculations**. The heavy concentration of mathematical terms and scientific units suggests it is designed to calculate properties related to laser beams.

*   **Laser Metrics:** It calculates various metrics such as `irradiancia_Wm2` (irradiance), `densidadPotencia_Wm2` (power density), `Fluencia_Jcm2` (fluence), and `EnergiaPulso_J` (pulse energy).
*   **Optical Physics Calculation:** The presence of functions like `CalcularRadioCurvatura` (calculate radius of curvature), `CalcularMediaDivergencia` (mean divergence), and `FrecuenciaALongitudOnda` (frequency to wavelength conversion) indicates it is used for beam profiling.
*   **Data Management:** It utilizes `.NET` standard libraries (`System.Xml`, `System.Data`) to handle structured data, specifically using "DataTables" for fields like `CavidadLaserDataTable` and `DivergenciaHazDataTable`.

### Suspicious or Malicious Behaviors
From the provided sample, there are **no overt malicious behaviors** typical of malware (such as process injection, unauthorized file modification, or network communication). 

*   **No Network Activity:** No IP addresses, domain names, or hardcoded URLs were found in the string list.
*   **No Persistence Mechanisms:** There is no evidence of registry modification or scheduled task creation.
*   **No Obvious Stealers:** The "Harvest" terminology (e.g., `HarvestImageData`) refers to collecting data within the application's UI/form logic, not harvesting credentials from the OS.

### Notable Techniques and Observations
*   **Decompilation Artifacts:** A significant number of functions are flagged with `WARNING: Control flow encountered bad instruction data` or `halt_baddata()`. In a malware context, this sometimes indicates **anti-analysis techniques** (like junk code insertion or overlapping instructions). However, in the context of a .NET application being decompiled from a mixed intermediate language (MSIL) state via a decompiler like r2ghidra, this is often just an artifact of the tool struggling to map complex C# compiler optimizations into clean C pseudocode.
*   **Localization:** The use of Spanish labels (`lblUnidad`, `txtResG1`) suggests the application was developed for or used in a Spanish-speaking region as a specialized professional tool.
*   **Framework Usage:** The inclusion of `mscorlib` and `System.Xml` indicates this is a .NET-based application, which provides high-level abstraction for calculations and GUI rendering.

### Summary
The sample appears to be **benign**. It is likely a specialized scientific calculator used by laser technicians or researchers to determine the physics of laser propagation and intensity. The "messy" appearance of the assembly/pseudocode is most likely an artifact of the decompiler's interaction with .NET-specific metadata rather than intentional obfuscation for malicious purposes.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed technical characteristics to the MITRE ATT&CK framework. 

Note: As the analysis concludes the sample is **benign**, most behaviors identified do not map to malicious tactics; however, certain indicators (like those related to disassembly difficulties) have been mapped as they represent techniques often used in malware to hinder analysis.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The identification of "halt_baddata" and "bad instruction data" can be indicative of efforts to complicate de-obfuscation and disassembly, though the analyst notes these may be artifacts of a .NET decompiler. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, no malicious Indicators of Compromise (IOCs) were identified. The sample appears to be a benign engineering tool for laser physics calculations.

**IP addresses / URLs / Domains**
*   None

**File paths / Registry keys**
*   None

**Mutex names / Named pipes**
*   None

**Hashes**
*   None

**Other artifacts**
*   None (Note: While the term "Harvest" appeared in strings such as `HarvestImageData`, the behavioral analysis confirms this refers to internal UI data collection rather than credential harvesting or malicious activity.)

---

## Malware Family Classification

1. **Malware family**: None (Benign)
2. **Malware type**: None (Benign)
3. **Confidence**: High
4. **Key evidence**:
    * **Lack of Malicious Behavior:** The analysis confirms the absence of common malware indicators, such as C2 communication (no IPs/URLs), persistence mechanisms (no registry or scheduled task changes), and unauthorized data harvesting.
    * **Clear Purpose:** The code's logic is consistently tied to scientific calculations for laser physics and optics (e.g., calculating irradiance, beam divergence, and pulse energy).
    * **Artifact Clarification:** Indicators that might suggest evasion (like "halt_baddata") were identified as artifacts of the decompiler struggling with .NET metadata rather than intentional obfuscation techniques.
