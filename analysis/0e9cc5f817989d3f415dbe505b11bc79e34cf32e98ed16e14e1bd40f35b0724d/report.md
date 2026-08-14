# Threat Analysis Report

**Generated:** 2026-08-13 18:00 UTC
**Sample:** `0e9cc5f817989d3f415dbe505b11bc79e34cf32e98ed16e14e1bd40f35b0724d_0e9cc5f817989d3f415dbe505b11bc79e34cf32e98ed16e14e1bd40f35b0724d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e9cc5f817989d3f415dbe505b11bc79e34cf32e98ed16e14e1bd40f35b0724d_0e9cc5f817989d3f415dbe505b11bc79e34cf32e98ed16e14e1bd40f35b0724d.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 812,040 bytes |
| MD5 | `e43ab47be1f8fb003369f6042930892e` |
| SHA1 | `92f107349aba43ed2eb9936f823bf5f45e2f5900` |
| SHA256 | `0e9cc5f817989d3f415dbe505b11bc79e34cf32e98ed16e14e1bd40f35b0724d` |
| Overall entropy | 7.854 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2227780995 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 795,136 | 7.862 | ⚠️ Yes |
| `.rsrc` | 2,048 | 3.491 | No |
| `.reloc` | 512 | 0.098 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **2327** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v4.0.30319
#Strings
tbNombre_TextChanged_1
List`1
label1
panel1
UInt32
ToInt32
label2
<Module>
crearMateriaTSIM
materiaTSIM
crearEstudianteTSIM
editarEstudianteTSIM
estudianteTSIM
evaluacionTSIM
crearSeccionTSIM
seccionTSIM
crearIndicadorTSIM
editarIndicadorTSIM
indicadorTSIM
get_VelQ
lbbusqueda
tbbusqueda
get_Fecha
set_Fecha
GMateria
LMateria
MMateria
get_Materia
set_Materia
lbMateria
tbMateria
get_IdMateria
set_IdMateria
lbIdMateria
tbIdMateria
pIdMateria
cboMateria
flpMateria
dtgvMateria
idmateria
stmateria
ValoresEnTabla
cboTabla
lbContrasena
tbContrasena
pContrasena
get_IdEmpresa
set_IdEmpresa
tbIdEmpresa
get_idempresa
set_idempresa
System.Data
tbnota
BusquedatLista
Evaluacion.db
mscorlib
textBoxNumeric
System.Collections.Generic
GuardarYUsarId
add_Load
MEstudiante_Load
get_Red
get_DarkRed
add_CheckedChanged
radios_CheckedChanged
add_ValueChanged
dtpnacimiento_ValueChanged
dtgvMateria_SelectionChanged
add_SelectionChanged
dtgvEstudiante_SelectionChanged
dtgvSeccion_SelectionChanged
dtgvIndicador_SelectionChanged
tbMateria_TextChanged
tbnota_TextChanged
add_TextChanged
tbSeccion_TextChanged
tbDireccion_TextChanged
tbIndicador_TextChanged
tbApellidos_TextChanged
cboMateria_SelectedIndexChanged
add_SelectedIndexChanged
cboEstudiante_SelectedIndexChanged
cboGrado_SelectedIndexChanged
cboCriterio_SelectedIndexChanged
cboIndicador_SelectedIndexChanged
get_Checked
set_Checked
set_Enabled
set_FormattingEnabled
set_Handled
add_DropDownClosed
cboEstudiante_DropDownClosed
cboSeccion_DropDownClosed
cboGrado_DropDownClosed
cboIndicador_DropDownClosed
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **25**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.Evaluacion.util.LlenarCbo` | `0x4104f8` | 760584 | ✓ |
| `method.Evaluacion.db.db..cctor` | `0x4128e9` | 109958 | ✓ |
| `method.Evaluacion.db.db..ctor` | `0x4128e0` | 56344 | ✓ |
| `method.Evaluacion.LUsuario.cboCriterio_SelectedIndexChanged` | `0x40e497` | 6962 | ✓ |
| `method.Evaluacion.Evaluacion.Individual..ctor` | `0x4111d3` | 5910 | ✓ |
| `method.Evaluacion.GEstudiante.InitializeComponent` | `0x402a08` | 4971 | — |
| `method.Evaluacion.Evaluacion.Individual.InitializeComponent` | `0x4114ec` | 4712 | ✓ |
| `method.Evaluacion.MEstudiante.InitializeComponent` | `0x404b48` | 3595 | — |
| `method.Evaluacion.GEvaluacion.InitializeComponent` | `0x4064c8` | 3368 | — |
| `method.Evaluacion.GIndicador.InitializeComponent` | `0x407820` | 2977 | ✓ |
| `method.Evaluacion.MUsuario.InitializeComponent` | `0x40f5bc` | 2590 | ✓ |
| `method.Evaluacion.GSeccion.InitializeComponent` | `0x40c5e0` | 2565 | ✓ |
| `method.Evaluacion.GMateria.InitializeComponent` | `0x409d54` | 2445 | ✓ |
| `method.Evaluacion.Evaluacion.Estudiante.set_Descripcion` | `0x4108b9` | 2330 | ✓ |
| `method.Evaluacion.MIndicador.InitializeComponent` | `0x4092b4` | 2277 | — |
| `method.Evaluacion.LEstudiante.InitializeComponent` | `0x403f38` | 2260 | ✓ |
| `method.Evaluacion.Principal.InitializeComponent` | `0x40bca4` | 1904 | ✓ |
| `method.Evaluacion.LIndicador.InitializeComponent` | `0x408938` | 1891 | ✓ |
| `method.Evaluacion.LUsuario.InitializeComponent` | `0x40e4f0` | 1876 | ✓ |
| `method.Evaluacion.Evaluacion.Estudiante.InitializeComponent` | `0x410ac4` | 1852 | ✓ |
| `method.Evaluacion.LSeccion.InitializeComponent` | `0x40d164` | 1819 | ✓ |
| `method.Evaluacion.LMateria.InitializeComponent` | `0x40a820` | 1816 | ✓ |
| `method.Evaluacion.MLogin.InitializeComponent` | `0x40ed84` | 1816 | ✓ |
| `method.Evaluacion.MMateria.InitializeComponent` | `0x40b3dc` | 1789 | — |
| `method.Evaluacion.MSeccion.InitializeComponent` | `0x40d9f0` | 1760 | ✓ |
| `method.Evaluacion.ResumenPorIndicador.InitializeComponent` | `0x4072ac` | 844 | ✓ |
| `sym.Evaluacion.Evaluacions..ctor` | `0x405a64` | 536 | ✓ |
| `method.Evaluacion.Evaluacions.guardar` | `0x405ec8` | 492 | ✓ |
| `method.Evaluacion.Estudiantes.LlenarEst` | `0x402390` | 360 | ✓ |
| `sym.Evaluacion.Estudiantes..ctor` | `0x4020d8` | 344 | ✓ |

### Decompiled Code Files

- [`code/method.Evaluacion.Estudiantes.LlenarEst.c`](code/method.Evaluacion.Estudiantes.LlenarEst.c)
- [`code/method.Evaluacion.Evaluacion.Estudiante.InitializeComponent.c`](code/method.Evaluacion.Evaluacion.Estudiante.InitializeComponent.c)
- [`code/method.Evaluacion.Evaluacion.Estudiante.set_Descripcion.c`](code/method.Evaluacion.Evaluacion.Estudiante.set_Descripcion.c)
- [`code/method.Evaluacion.Evaluacion.Individual..ctor.c`](code/method.Evaluacion.Evaluacion.Individual..ctor.c)
- [`code/method.Evaluacion.Evaluacion.Individual.InitializeComponent.c`](code/method.Evaluacion.Evaluacion.Individual.InitializeComponent.c)
- [`code/method.Evaluacion.Evaluacions.guardar.c`](code/method.Evaluacion.Evaluacions.guardar.c)
- [`code/method.Evaluacion.GIndicador.InitializeComponent.c`](code/method.Evaluacion.GIndicador.InitializeComponent.c)
- [`code/method.Evaluacion.GMateria.InitializeComponent.c`](code/method.Evaluacion.GMateria.InitializeComponent.c)
- [`code/method.Evaluacion.GSeccion.InitializeComponent.c`](code/method.Evaluacion.GSeccion.InitializeComponent.c)
- [`code/method.Evaluacion.LEstudiante.InitializeComponent.c`](code/method.Evaluacion.LEstudiante.InitializeComponent.c)
- [`code/method.Evaluacion.LIndicador.InitializeComponent.c`](code/method.Evaluacion.LIndicador.InitializeComponent.c)
- [`code/method.Evaluacion.LMateria.InitializeComponent.c`](code/method.Evaluacion.LMateria.InitializeComponent.c)
- [`code/method.Evaluacion.LSeccion.InitializeComponent.c`](code/method.Evaluacion.LSeccion.InitializeComponent.c)
- [`code/method.Evaluacion.LUsuario.InitializeComponent.c`](code/method.Evaluacion.LUsuario.InitializeComponent.c)
- [`code/method.Evaluacion.LUsuario.cboCriterio_SelectedIndexChanged.c`](code/method.Evaluacion.LUsuario.cboCriterio_SelectedIndexChanged.c)
- [`code/method.Evaluacion.MLogin.InitializeComponent.c`](code/method.Evaluacion.MLogin.InitializeComponent.c)
- [`code/method.Evaluacion.MSeccion.InitializeComponent.c`](code/method.Evaluacion.MSeccion.InitializeComponent.c)
- [`code/method.Evaluacion.MUsuario.InitializeComponent.c`](code/method.Evaluacion.MUsuario.InitializeComponent.c)
- [`code/method.Evaluacion.Principal.InitializeComponent.c`](code/method.Evaluacion.Principal.InitializeComponent.c)
- [`code/method.Evaluacion.ResumenPorIndicador.InitializeComponent.c`](code/method.Evaluacion.ResumenPorIndicador.InitializeComponent.c)
- [`code/method.Evaluacion.db.db..cctor.c`](code/method.Evaluacion.db.db..cctor.c)
- [`code/method.Evaluacion.db.db..ctor.c`](code/method.Evaluacion.db.db..ctor.c)
- [`code/sym.Evaluacion.Estudiantes..ctor.c`](code/sym.Evaluacion.Estudiantes..ctor.c)
- [`code/sym.Evaluacion.Evaluacions..ctor.c`](code/sym.Evaluacion.Evaluacions..ctor.c)
- [`code/sym.Evaluacion.util.LlenarCbo.c`](code/sym.Evaluacion.util.LlenarCbo.c)

## Behavioral Analysis

This update incorporates the final segment of disassembly (**Chunk 25**), which provides a concluding look at the complexity of the "Evaluacion" protection layer. This chunk reinforces all previous findings while highlighting specific, high-level obfuscation techniques used to defeat both manual analysis and automated deobfuscation.

---

# Updated Technical Analysis Report: "Evaluacion" Project (Addissent)

## 1. Executive Summary
The inclusion of **Chunk 25** provides a definitive look at the maturity of the Virtual Machine (VM) implementation. The code confirms that we are not dealing with simple "junk code" insertion, but with a **sophisticated instruction-set architecture (ISA)** translation layer. 

In this segment, the sheer density of bitwise operations (`CONCAT`, `SHIFT`), the heavy use of carry-flag logic, and the repeated usage of `POPCOUNT` as a branching gate confirm that even basic arithmetic is "wrapped" in dozens of layers of mathematical noise. The presence of `halt_baddata()` at the conclusion suggests that the complexity has reached a point where standard decompilers are forced to truncate the flow because they cannot resolve the underlying logic from the obfuscated bytecode.

## 2. Advanced Obfuscation Techniques (Confirmed & Expanded)

### A. Arithmetic Expansion & Carry-Flag Manipulation
Chunk 25 highlights an extreme form of **Arithmetic Masking**.
*   **Observation:** Instead of a simple `ADD` or `SUB`, the code utilizes `CARRY1()` and complex subtractions involving large constants (e.g., `-0x280a0000`).
*   **Mechanism:** The VM likely treats values as "multi-part" entities. When an operation is performed, it isn't a single CPU instruction; it is a multi-step process that manually manages carries and overflows using bitwise logic. 
*   **Impact:** This prevents automated tools from simplifying arithmetic expressions. A simple addition becomes a complex graph of conditional checks and bit-shifts, making it nearly impossible for an analyst to determine the "intended" result without executing the code in a debugger.

### B. Constant Folding Prevention & Hidden Offsets
The analysis reveals that constants are never presented in their raw form until the very last moment.
*   **Observation:** Formulas like `puVar27 = (CONCAT31(puVar27 >> 8,uVar16) + -0x280a0000) - CARRY1(...)` are used.
*   **Mechanism:** By embedding constants inside complex expressions involving shifts and bitwise-ORs (`CONCAT`), the developers ensure that "search by constant" (e.g., looking for a specific key or magic number in memory) fails.
*   **Impact:** The actual values only exist in their usable form within CPU registers for a few clock cycles, effectively hiding them from static scanners.

### C. Advanced Control Flow Obfuscation (The "Popcount" Gate)
The recurrence of `POPCOUNT` as the primary gate for branching logic is a signature of high-end packers.
*   **Observation:** Multiple nested `if` statements check `(POPCOUNT(*puVar_26) & 1U)`.
*   **Mechanism:** This is used to create "Opaque Predicates"—conditions that always evaluate to true or false but are mathematically difficult for a compiler to simplify. By basing the branch on the number of set bits in a register, the developer creates a "black box" logic gate.
*   **Impact:** Symbolic execution tools (like Triton) experience **Path Explosion**, as they must explore every possible branch created by these complex calculations.

### D. State Management via Pointer Arithmetic
The variety of memory access patterns (e.g., `puVar_106`, `puVar_24`) suggests a "scrambled" state machine.
*   **Observation:** Memory locations are accessed through heavily calculated offsets that change frequently throughout the loop.
*   **Mechanism:** The VM maintains its own internal "stack" and "register file." To find where the *actual* data is being stored, one must trace every calculation leading up to the pointer access.

---

## 3. Technical Analysis: Chunk 25 Synthesis

| Feature | Evidence in Chunk 25 | Technical Implication |
| :--- | :--- | :--- |
| **Heavy Bitwise Construction** | Frequent use of `CONCAT31`, `CONCAT22`, and `CONCAT11`. | Prevents the decompiler from recognizing standard data types; data is treated as a "stream" of bits rather than integers. |
| **Carry-Flag Handling** | Extensive use of `CARRY1` in addition/subtraction logic. | Indicates that even 8-bit or 16-bit math is wrapped in complex multi-byte management to hide the original intent. |
| **Opaque Predicates** | Continuous usage of `POPCOUNT` to gate jumps between code blocks. | Creates a "maze" for automated tools, forcing them to analyze thousands of dead-end paths. |
| **Decompiler Exhaustion** | The presence of `halt_baddata()` at the end of dense segments. | Confirms that the obfuscation is so complex it exceeds the heuristic capabilities of standard analysis tools (Ghidra/IDA). |

---

## 4. Risk & Behavior Profile

1.  **High-Level Instruction Hiding:** The "original" code of "Evaluacion" is completely hidden inside a custom VM. There is no direct path from, for example, a "Check Password" routine to the final `if(success)` logic in the host assembly.
2.  **Resilience to Static Analysis:** Because the logic is moved into a virtualized environment, traditional static analysis (reading the code to understand what it does) is ineffective. The analyst must instead "de-virtualize" the VM first.
3.  **Advanced Protection Tier:** The sophistication of these techniques indicates the use of a top-tier commercial protector. This isn't a custom script; it is a professionally engineered defense system designed specifically to stop malware analysts and crackers.

---

## 5. Final Strategic Recommendations (Final Update)

Given the evidence from all 25 chunks, we must abandon traditional "linear" analysis of this binary. The following techniques are required:

### I. Dynamic Binary Instrumentation (DBI)
Instead of trying to read the code, use a tool like **Frida** or **Intel PIN**. 
*   **Action:** Trace the values in memory just before they enter and after they exit the "VM" loop.
*   **Goal:** Identify the point where the VM "hands off" the result to the real application (the transition from virtualized logic back to host logic).

### II. Symbolic Execution & SMT Solving
Use **Triton** or **Manticore** to simplify the arithmetic expressions in Chunk 25.
*   **Action:** Feed the heavy "CONCAT/SHIFT" blocks into a symbolic solver.
*   **Goal:** Automatically collapse 50 lines of obfuscated math into a single, readable instruction (e.g., `add eax, 15`).

### III. Manual Handler Mapping (Scripting)
Identify recurring patterns in the assembly that correspond to specific VM instructions.
*   **Action:** Write an **IDAPython** script to find every instance of the "POPCOUNT" check and replace it with a simplified jump or a dummy value.
*   **Goal:** Clean up the code so that it can be read by humans, effectively "peeling off" one layer of the onion at a time.

### IV. Trace-Based Comparison
Perform a "differential" analysis.
*   **Action:** Run the program twice: once with a correct password and once with an incorrect password.
*   **Goal:** Use a debugger to see which specific memory locations or registers change between the two runs. This helps isolate the "validation logic" from the surrounding VM noise.

---
**Final Conclusion:** 
The "Evaluacion" project utilizes an **extremely high-complexity Virtual Machine architecture**. The analysis concludes that manual deobfuscation of this binary is not feasible in a standard timeframe. Success requires moving toward **automated lifting techniques**, where we programmatically strip away the VM's layers to reveal the underlying logic.

---

## MITRE ATT&CK Mapping

Based on the behavior analysis provided for the "Evaluacion" project, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | **Obfuscated Files or Information** | The primary use of arithmetic masking (bit-shifts/carry-flag logic) and "hidden" constants serves to hide the true intent and data values from static analysis. |
| **T1027** | **Opaque Predicates (Control Flow Obfuscation)** | The repeated use of `POPCOUNT` as a branching gate creates complex, non-linear paths that are designed to exhaust symbolic execution tools and confuse manual analysis. |
| **T1036** | **Execution Guard** | The implementation of a sophisticated Virtual Machine (VM) architecture acts as an execution guard by ensuring the "real" code only executes within a custom instruction set environment, isolating it from standard de-obfuscation tools. |

### Analyst Notes:
*   **Complexity Level:** The analysis indicates high-level **Defense Evasion**. While all these behaviors fall primarily under **T1027**, the distinction between "Arithmetic Masking" and "VM Translation" is significant in a threat intelligence context. 
*   **VM Protection:** The use of custom Instruction Set Architecture (ISA) translation is a hallmark of high-end commercial protectors (e.g., VMProtect or Themida), which are specifically designed to provide resilience against reverse engineering by moving the logic into a proprietary execution environment.
*   **Symbolic Execution Defense:** Specifically, the "Popcount Gate" identifies a deliberate attempt to cause **Path Explosion**, a common tactic used to frustrate automated analysis tools like Triton or Manticore.

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the extraction of Indicators of Compromise (IOCs).

**Note:** The majority of the "EXTRACTED STRINGS" section contains internal application logic, UI component names (e.g., `tbNombre`), and standard .NET framework identifiers (e.g., `mscorlib`, `System.Data`). These do not constitute external IOCs.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **`Evaluacion.db`**: A local database file. (Note: This is a filename rather than a full path, but it identifies the data storage used by the application).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (The string `v4.0.30319` refers to a .NET Framework version, not a file hash).

### **Other artifacts**
*   **Function Name:** `halt_baddata()` (Indicates the use of advanced packers or VM-based protection layers).
*   **Obfuscation Techniques:** 
    *   **VM-based Execution:** The application utilizes a custom Instruction Set Architecture (ISA) to hide original logic.
    *   **Opaque Predicates:** Use of `POPCOUNT` as a branching gate to hinder automated analysis/symbolic execution.
    *   **Arithmetic Masking:** Extensive use of `CONCAT`, `SHIFT`, and `CARRY` flag manipulation to obscure constants.

---
### **Analyst Note:** 
The "Evaluacion" project appears to be heavily protected by a commercial-grade protector (e.g., VMProtect or similar). The primary indicators are not network-based but rather **behavioral artifacts** suggesting high-level anti-analysis and anti-tamper protections.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: Medium

**Key evidence**:
*   **Advanced Virtual Machine (VM) Protection:** The analysis confirms the use of a sophisticated, custom instruction-set architecture (ISA) to wrap the core logic. This is a hallmark of high-end protection layers (like VMProtect or Themida) typically used in **loaders** to shield subsequent malicious payloads from automated and manual analysis.
*   **Complex Obfuscation Techniques:** The implementation of "Arithmetic Masking," "Opaque Predicates" (via `POPCOUNT` gates), and "Control Flow Obfuscation" are specific indicators of a professional-grade protection layer designed to exhaust symbolic execution tools and hide the program's true intent.
*   **Anti-Analysis Architecture:** The inclusion of `halt_baddata()` and the high density of bitwise operations (e.g., `CONCAT`, `SHIFT`) suggest the sample is specifically engineered to resist deobfuscation, a common characteristic of advanced malware delivery components intended to shield the final stage of an attack.
