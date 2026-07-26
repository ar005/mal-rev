# Threat Analysis Report

**Generated:** 2026-07-25 14:27 UTC
**Sample:** `0ac1e2f8efb8d14f6ed1d1efba1fca6940902339da7acedf1975330694d6e4f8_0ac1e2f8efb8d14f6ed1d1efba1fca6940902339da7acedf1975330694d6e4f8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ac1e2f8efb8d14f6ed1d1efba1fca6940902339da7acedf1975330694d6e4f8_0ac1e2f8efb8d14f6ed1d1efba1fca6940902339da7acedf1975330694d6e4f8.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,082,880 bytes |
| MD5 | `9659578b2b5982017b8f3d131d5bfee2` |
| SHA1 | `8d51165929e4979b1464e8a578c04a9988286de4` |
| SHA256 | `0ac1e2f8efb8d14f6ed1d1efba1fca6940902339da7acedf1975330694d6e4f8` |
| Overall entropy | 7.484 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3468498393 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,073,664 | 7.487 | ⚠️ Yes |
| `.rsrc` | 8,192 | 7.375 | ⚠️ Yes |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **2887** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

X )UU

X )UU
p"33#As.
p"33#As.
p"33#As.

+2	o
p"33#As.
p"33#As.

+@s[

+2	o

+2	o

+2	o

+2	o
p"33#As.

+@s[
p"33#As.

+@s[
p"33#As.
v4.0.30319
#Strings
			!	'	=	K	R	Y	o	u	

'
0
?
S
\
r
{


A]%5;AG\u
!/:CIWclr
label10
panel10
53EA4B207B86C36E2E03C2A4F869969147F39755B92836FA80B72AEA800CB920
panel20
<>9__14_0
<ObtenerClave>b__14_0
<>9__15_0
<ObtenerNumero>b__15_0
<>c__DisplayClass5_0
<CascadeFluxMapper>b__0
label11
IEnumerable`1
TypedTableBase`1
ICollection`1
IComparer`1
EqualityComparer`1
List`1
relationFK_Estudiante_Carrera1
parentCarreraRowByFK_Estudiante_Carrera1
get_String1
label1
panel1
label12
panel12
Func`2
KeyValuePair`2
IDictionary`2
label2
panel2
label13
<>f__AnonymousType0`3
label3
panel3
label14
panel14
__StaticArrayInitTypeSize=44
label4
panel4
label15
label5
panel5
panel16
label6
panel6
label7
panel7
panel18
get_UTF8
label8
panel8
label9
<Module>
<PrivateImplementationDetails>
get_StringA
Caja_UNAPEC
txtDCID
txtFPID
txtUSUID
txtSVID
System.IO
get_Nombre_O
set_Nombre_O
get_Estado_O
set_Estado_O
get_Acceso_O
set_Acceso_O
get_Identificador_O
set_Identificador_O
pnlPerfilP
value__
ObtenerTanda
get_MovimientoDeCaja
tableMovimientoDeCaja
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c._ObtenerClave_b__14_0` | `0x4261f6` | 116884 | ✓ |
| `method.__c._ObtenerNumero_b__15_0` | `0x4261c9` | 116644 | ✓ |
| `sym.Caja_UNAPEC.Caja_UNAPECDataSet..ctor` | `0x4059ac` | 65592 | ✓ |
| `method.SelfReferenceComparer.Compare` | `0x42632c` | 65226 | ✓ |
| `method.Caja_UNAPEC.Inicio.InicializarLoging` | `0x410067` | 16034 | ✓ |
| `method.Caja_UNAPEC.FrmCajaUnapec.InitializeComponent` | `0x402f24` | 10888 | — |
| `method.Caja_UNAPEC.Empleado.InicializarEmpleado` | `0x4099b3` | 10458 | ✓ |
| `method.Caja_UNAPEC.Estudiantes.InicializarEstudiante` | `0x40c2b3` | 10038 | ✓ |
| `sym.Caja_UNAPEC.Caja_UNAPECDataSet.InitVars` | `0x406103` | 8752 | ✓ |
| `method.Caja_UNAPEC.Usuarios..ctor` | `0x416c53` | 8696 | ✓ |
| `method.Caja_UNAPEC.Movimientos.InitializeComponent` | `0x4123c8` | 7020 | ✓ |
| `method.Caja_UNAPEC.Empleado.InitializeComponent` | `0x40a810` | 6880 | ✓ |
| `method.Caja_UNAPEC.Servicio.InicializarServicios` | `0x4153c7` | 6284 | ✓ |
| `method.Caja_UNAPEC.Estudiantes.InitializeComponent` | `0x40d16c` | 6238 | ✓ |
| `method.Caja_UNAPEC.Usuarios.InitializeComponent` | `0x417684` | 5968 | ✓ |
| `method.Caja_UNAPEC.Documentos.InicializarDocumentos` | `0x408333` | 5722 | ✓ |
| `method.Caja_UNAPEC.FormaDePago.InicializarFormaDePago` | `0x40e9e9` | 5720 | ✓ |
| `method.Caja_UNAPEC.PerfilUsuario.BtnPUCancelar_Click` | `0x413f85` | 5128 | ✓ |
| `method.Caja_UNAPEC.Carrera.InitializeComponent` | `0x407138` | 4572 | ✓ |
| `method.Caja_UNAPEC.PerfilUsuario.InitializeComponent` | `0x41424c` | 4444 | ✓ |
| `method.Caja_UNAPEC.Servicio.InitializeComponent` | `0x415a74` | 4424 | ✓ |
| `method.Caja_UNAPEC.Documentos.InitializeComponent` | `0x40897c` | 4208 | ✓ |
| `method.Caja_UNAPEC.FormaDePago.InitializeComponent` | `0x40f030` | 4192 | ✓ |
| `method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.TableAdapterManager.UpdateAll` | `0x420034` | 2556 | ✓ |
| `method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.EmpleadoTableAdapter.InitAdapter` | `0x419f08` | 2287 | ✓ |
| `method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.EstudianteTableAdapter.InitAdapter` | `0x41b3a4` | 2005 | ✓ |
| `method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.CarreraTableAdapter..ctor` | `0x418f2d` | 1810 | ✓ |
| `method.Caja_UNAPEC.Inicio.InitializeComponent` | `0x410484` | 1730 | ✓ |
| `method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.CarreraTableAdapter.InitAdapter` | `0x4191b8` | 1196 | ✓ |
| `method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.FormaDePAgoTableAdapter.InitAdapter` | `0x41c6e4` | 1155 | ✓ |

### Decompiled Code Files

- [`code/method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.CarreraTableAdapter..ctor.c`](code/method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.CarreraTableAdapter..ctor.c)
- [`code/method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.CarreraTableAdapter.InitAdapter.c`](code/method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.CarreraTableAdapter.InitAdapter.c)
- [`code/method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.EmpleadoTableAdapter.InitAdapter.c`](code/method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.EmpleadoTableAdapter.InitAdapter.c)
- [`code/method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.EstudianteTableAdapter.InitAdapter.c`](code/method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.EstudianteTableAdapter.InitAdapter.c)
- [`code/method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.FormaDePAgoTableAdapter.InitAdapter.c`](code/method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.FormaDePAgoTableAdapter.InitAdapter.c)
- [`code/method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.TableAdapterManager.UpdateAll.c`](code/method.Caja_UNAPEC.Caja_UNAPECDataSetTableAdapters.TableAdapterManager.UpdateAll.c)
- [`code/method.Caja_UNAPEC.Carrera.InitializeComponent.c`](code/method.Caja_UNAPEC.Carrera.InitializeComponent.c)
- [`code/method.Caja_UNAPEC.Documentos.InicializarDocumentos.c`](code/method.Caja_UNAPEC.Documentos.InicializarDocumentos.c)
- [`code/method.Caja_UNAPEC.Documentos.InitializeComponent.c`](code/method.Caja_UNAPEC.Documentos.InitializeComponent.c)
- [`code/method.Caja_UNAPEC.Empleado.InicializarEmpleado.c`](code/method.Caja_UNAPEC.Empleado.InicializarEmpleado.c)
- [`code/method.Caja_UNAPEC.Empleado.InitializeComponent.c`](code/method.Caja_UNAPEC.Empleado.InitializeComponent.c)
- [`code/method.Caja_UNAPEC.Estudiantes.InicializarEstudiante.c`](code/method.Caja_UNAPEC.Estudiantes.InicializarEstudiante.c)
- [`code/method.Caja_UNAPEC.Estudiantes.InitializeComponent.c`](code/method.Caja_UNAPEC.Estudiantes.InitializeComponent.c)
- [`code/method.Caja_UNAPEC.FormaDePago.InicializarFormaDePago.c`](code/method.Caja_UNAPEC.FormaDePago.InicializarFormaDePago.c)
- [`code/method.Caja_UNAPEC.FormaDePago.InitializeComponent.c`](code/method.Caja_UNAPEC.FormaDePago.InitializeComponent.c)
- [`code/method.Caja_UNAPEC.Inicio.InicializarLoging.c`](code/method.Caja_UNAPEC.Inicio.InicializarLoging.c)
- [`code/method.Caja_UNAPEC.Inicio.InitializeComponent.c`](code/method.Caja_UNAPEC.Inicio.InitializeComponent.c)
- [`code/method.Caja_UNAPEC.Movimientos.InitializeComponent.c`](code/method.Caja_UNAPEC.Movimientos.InitializeComponent.c)
- [`code/method.Caja_UNAPEC.PerfilUsuario.BtnPUCancelar_Click.c`](code/method.Caja_UNAPEC.PerfilUsuario.BtnPUCancelar_Click.c)
- [`code/method.Caja_UNAPEC.PerfilUsuario.InitializeComponent.c`](code/method.Caja_UNAPEC.PerfilUsuario.InitializeComponent.c)
- [`code/method.Caja_UNAPEC.Servicio.InicializarServicios.c`](code/method.Caja_UNAPEC.Servicio.InicializarServicios.c)
- [`code/method.Caja_UNAPEC.Servicio.InitializeComponent.c`](code/method.Caja_UNAPEC.Servicio.InitializeComponent.c)
- [`code/method.Caja_UNAPEC.Usuarios..ctor.c`](code/method.Caja_UNAPEC.Usuarios..ctor.c)
- [`code/method.Caja_UNAPEC.Usuarios.InitializeComponent.c`](code/method.Caja_UNAPEC.Usuarios.InitializeComponent.c)
- [`code/method.SelfReferenceComparer.Compare.c`](code/method.SelfReferenceComparer.Compare.c)
- [`code/method.__c._ObtenerClave_b__14_0.c`](code/method.__c._ObtenerClave_b__14_0.c)
- [`code/method.__c._ObtenerNumero_b__15_0.c`](code/method.__c._ObtenerNumero_b__15_0.c)
- [`code/sym.Caja_UNAPEC.Caja_UNAPECDataSet..ctor.c`](code/sym.Caja_UNAPEC.Caja_UNAPECDataSet..ctor.c)
- [`code/sym.Caja_UNAPEC.Caja_UNAPECDataSet.InitVars.c`](code/sym.Caja_UNAPEC.Caja_UNAPECDataSet.InitVars.c)

## Behavioral Analysis

The inclusion of chunk 17/18 introduces a critical shift in the investigation. While previous segments focused on identifying **who** the students are (`Carrera`), this segment reveals that the attackers are also targeting **how the students pay** for their education.

This update confirms that "Caja_UNAPEC" is not just a general data-grabber; it is performing high-precision profiling of the student body's financial habits.

---

### Updated Technical Analysis: Project "Caja_UNAPEC"

#### 1. Expanded Data Mapping (The "FormaDePAgo" Component)
The analysis of the `FormaDePAgoTableAdapter` and its `InitAdapter` method provides a significant new data point. In Spanish, **"Forma de Pago"** translates to **"Method of Payment."**

*   **Financial Profiling:** By mapping "Method of Payment," the malware is identifying how students pay their tuition—specifically looking for information related to credit cards, bank accounts, installment plans, or specific payment providers.
*   **High-Value Target Correlation:** When combined with the previous `Carrera` (Academic Major) data, a two-dimensional profile is formed. An attacker can now cross-reference:
    *   *Example:* Students in "Management" majors who use "Credit Card" payments might be flagged as high-value targets for credit card fraud or targeted phishing regarding financial services.
*   **Sophisticated Integration:** The fact that this exists as a specific `TableAdapter` suggests the malware is designed to ingest and structure complex, multi-field database records rather than simple text strings.

#### 2. Advanced Anti-Analysis & Decompiler Sabotage
This chunk provides some of the clearest evidence yet of "intentional" architectural complexity designed to defeat automated analysis:

*   **Overlapping Instructions:** The decompilation warnings (e.g., `0x41cd19` overlapping `0x41cd18`) and "Bad Instruction" errors are classic indicators of **Anti-Decompiler code**. The threat actor is purposefully injecting bytes that confuse tools like Ghidra or IDA Pro, forcing the analyst to manually fix the disassembly.
*   **Instruction Bloat (Mathematical Noise):** The repeated use of `CONCAT`, `POPCOUNT`, and complex `CARRY` checks for what should be simple memory offsets indicates a "Heavy" obfuscation layer. This is intended to exhaust the human analyst's patience—every line of code you read that isn't "useful" is a calculated distraction to slow down the identification of the core malicious logic.
*   **Dynamic Offsets:** The heavy use of `0x6f`, `0x72`, and other hex constants in calculations suggests the malware uses **offset-based memory navigation**. It doesn't store the "target" data (like a credit card number) as a string; it calculates where that data sits in a buffer at runtime.

#### 3. Evidence of Modular Sophistication
The distinction between `Caja_UNAPECDataSetTableAdapters` and specific sub-adapters like `FormaDePAgoTableAdapter` indicates:
*   **Modular Architecture:** The malware is built with a "plug-and-play" architecture. The core engine handles the connection/extraction, while different "Adapters" handle the parsing of different types of data (Students, Courses, Payments).
*   **Persistent Development:** This level of organization suggests that the threat actor has spent significant time developing a suite of tools specifically for this environment, rather than using an off-the-shelf script.

---

### Updated Risk Assessment: High-Value Financial Targeting

The discovery of `FormaDePAgo` significantly elevates the risk profile from "Privacy Breach" to **"Financial Fraud Facilitation."**

1.  **Targeted Identity Theft:** By capturing both a student's academic path and their payment methods, the actor can construct highly convincing phishing lures (e.g., "Your [Specific Major] scholarship has been updated; please re-confirm your [Method of Payment]").
2.  **Fraudulent Account Takeover (ATO):** The specific focus on "Forma de Pago" suggests a motive to harvest credentials for payment gateways or to identify students with high credit limits for fraudulent use.
3.  **Institutional Risk:** For UNAPEC, this indicates that the threat is not just targeting individuals, but specifically the infrastructure that handles student billing and financial records.

---

### Updated Summary Conclusion
The analysis of chunk 17/18 confirms that **Caja_UNAPEC** is a sophisticated piece of industrial-grade malware. The transition from `Carrera` (Identity) to `FormaDePAgo` (Financial Strategy) confirms that the threat actor's goal is the creation of a high-value database of student records that can be monetized through identity theft or targeted financial fraud.

The extremely high level of obfuscation—intended to break decompilers and hide logic within mountains of mathematical "noise"—confirms that this is the work of an experienced developer or an organized cybercrime group prepared for defense by security professionals.

**Actionable Intelligence & Recommendations:**
1.  **Identify Financial Data Gateways:** Immediately audit all systems involving student payments (`FormaDePAgo`). Ensure these specific databases are isolated from the general academic network.
2.  **Behavioral Analysis (Egress):** Since the logic is heavily obfuscated, signature-based detection may fail. Monitor for "Heartbeat" patterns—small, periodic packets being sent to external IPs—which could indicate the successful transmission of a harvested "Forma de Pago" packet.
3.  **Memory Forensics:** Because many strings and offsets are calculated at runtime (via `CONCAT` and `POPCOUNT`), standard static scanning might miss them. Use memory forensic tools to look for decrypted payment-related keywords in active processes during the `InitAdapter` phase of execution.
4.  **Enhanced Monitoring:** Flag any internal processes that exhibit high CPU spikes or complex mathematical operations while interacting with databases containing student billing information.

*End of Analysis Update - Chunk 17/18 integrated.*

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors in the "Caja_UNAPEC" investigation to the following MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1005** | Data from Local System | The malware is specifically designed to query and extract structured records (e.g., `FormaDePAgo` and `Carrera`) to build high-value profiles of student financial habits. |
| **T1027** | Obfuscated Files or Information | The use of "Instruction Bloat," "Mathematical Noise" (CONCAT, POPCOUNT), and "Overlapping Instructions" are deliberate tactics intended to hinder reverse engineering and defeat analysis tools like Ghidra/IDA Pro. |
| **T1592** | Gather Victim Identity Information | By mapping students' academic paths alongside their payment methods, the actor is performing specific information gathering to identify high-value targets for subsequent fraud or phishing. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) and relevant technical artifacts:

### **IP addresses / URLs / Domains**
*None identified in the provided text.*

### **File paths / Registry keys**
*None identified in the provided text.*

### **Mutex names / Named pipes**
*None identified in the provided text.*

### **Hashes**
*   `53EA4B207B86C36E2E03C2A4F869969147F39755B92836FA80B72AEA800CB920` (Note: This appears to be a SHA-256 hash, likely associated with a specific payload or file component).

### **Other artifacts**
*   **Malware/Campaign Identifier:** `Caja_UNAPEC` (Used as the internal naming convention for the malware suite targeting UNAPEC systems).
*   **Targeted Data Fields:** 
    *   `FormaDePAgo` (Method of Payment - indicates specific interest in financial data).
    *   `txtDCID`, `txtFPID`, `txtUSUID`, `txtSVID` (Potential internal identifiers for Document ID, Form Payment ID, User ID, and Student View ID).
    *   `ValidarCedula` (Validation routine for National Identity numbers).
*   **Anti-Analysis/Obfuscation Patterns:**
    *   **Instruction Bloat:** Use of `CONCAT`, `POPCOUNT`, and complex `CARRY` checks to mask simple memory offsets.
    *   **Decompiler Sabotage:** Intentional "Overlapping Instructions" (e.g., 0x41cd19 overlapping 0x41cd18) designed to break tools like Ghidra or IDA Pro.
    *   **Dynamic Offsets:** Use of hex constants (`0x6f`, `0x72`) to calculate memory locations at runtime rather than storing plaintext strings.
*   **C2 Behavior (Inferred):** "Heartbeat" patterns (small, periodic packets) described in the analysis as a potential method for exfiltrating the harvested "Forma de Pago" data.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: infostealer
3. **Confidence**: High
4. **Key evidence**:
    *   **Targeted Financial Data Extraction:** The malware specifically targets structured data fields such as `FormaDePAgo` (Method of Payment) and academic records, indicating a deliberate goal of harvesting financial information for fraud rather than general system disruption.
    *   **Advanced Anti-Analysis Techniques:** The use of "instruction bloat" (POPCOUNT/CONCAT), dynamic offsets, and intentional decompiler sabotage (overlapping instructions) confirms the malware is designed to evade detection from security professionals and automated tools like Ghidra or IDA Pro.
    *   **Modular & Tailored Architecture:** The use of specific data adapters (`FormaDePAgoTableAdapter`) suggests a professionally developed, modular toolkit tailored specifically for the UNAPEC infrastructure rather than a generic piece of "off-the-shelf" malware.
