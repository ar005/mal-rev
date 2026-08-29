# Threat Analysis Report

**Generated:** 2026-08-19 00:00 UTC
**Sample:** `1079c14f69f1dac1d28b8aea2d9700d699058a6b5005f2b0c609d758549bb74b_1079c14f69f1dac1d28b8aea2d9700d699058a6b5005f2b0c609d758549bb74b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1079c14f69f1dac1d28b8aea2d9700d699058a6b5005f2b0c609d758549bb74b_1079c14f69f1dac1d28b8aea2d9700d699058a6b5005f2b0c609d758549bb74b.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 987,136 bytes |
| MD5 | `a4a77cc699f8e155d93fb4d35696ea78` |
| SHA1 | `783577520daa2bd986dbcab821013abe527dd9c5` |
| SHA256 | `1079c14f69f1dac1d28b8aea2d9700d699058a6b5005f2b0c609d758549bb74b` |
| Overall entropy | 7.785 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774330094 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 984,576 | 7.79 | ⚠️ Yes |
| `.rsrc` | 1,536 | 4.159 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **2932** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
4{ )UU

X )UU

X )UU
]^ )UU

X )UU

X )UU

X )UU

	rA	
	#fff]]
Y5D@}r
XlZi#aTR'
XlZiXl
@X	#fffff
Y#aTR'
Y#aTR'
BAYZX#
#es-8R
#es-8R
#es-8R
#es-8R
#es-8R

lZX#]m

j]*.s
v4.0.30319
#Strings
 DJU_dkz

%8l
EpocaJ2000
SiglosDesdeJ2000
<ConfigurarEventos>b__11_10
<DisassembleImageData>b__10
<ExtractPixelComponents>b__10
<>9__7_20
<ExtractPixelComponents>b__7_20
<DisassembleImageData>b__20
<ConfigurarEventos>b__11_0
<>c__DisplayClass53_0
<>9__6_0
<DisassembleImageData>b__6_0
<ConfigurarEventos>b__6_0
<>c__DisplayClass6_0
<>9__7_0
<ConfigurarEventos>b__7_0
<ExtractPixelComponents>b__7_0
<>c__DisplayClass7_0
<RenderizarTrayectoriaEfemerides>b__0
<ConfigurarEventos>b__11_11
<>9__6_11
<DisassembleImageData>b__6_11
<ExtractPixelComponents>b__11
<>9__7_21
<ExtractPixelComponents>b__7_21
<DisassembleImageData>b__21
<ConfigurarEventos>b__11_1
<>9__6_1
<DisassembleImageData>b__6_1
<ConfigurarEventos>b__6_1
<>c__DisplayClass6_1
<>9__7_1
<ConfigurarEventos>b__7_1
<ExtractPixelComponents>b__7_1
<>c__DisplayClass7_1
Nullable`1
IEnumerable`1
IOrderedEnumerable`1
TypedTableBase`1
EqualityComparer`1
List`1
get_EfemeridesHistorial1
tableEfemeridesHistorial1
ShouldSerializeEfemeridesHistorial1
get_Panel1
panelSeparador1
<ConfigurarEventos>b__11_12
<>9__6_12
<DisassembleImageData>b__6_12
<ExtractPixelComponents>b__12
<DisassembleImageData>b__22
<ConfigurarEventos>b__11_2
<>9__6_2
<DisassembleImageData>b__6_2
<ConfigurarEventos>b__6_2
<>c__DisplayClass6_2
<>9__7_2
<ConfigurarEventos>b__7_2
<ExtractPixelComponents>b__7_2
<>c__DisplayClass7_2
<>f__AnonymousType0`2
<>f__AnonymousType1`2
<>f__AnonymousType2`2
<>f__AnonymousType3`2
<>f__AnonymousType4`2
Func`2
IGrouping`2
get_Panel2
panelSeparador2
<ConfigurarEventos>b__11_13
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **28**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.ConstelacionesRow..ctor` | `0x4113cf` | 68876 | ✓ |
| `method.__c__DisplayClass53_0._RenderizarTrayectoriaEfemerides_b__0` | `0x411f84` | 65008 | ✓ |
| `method.EstrellasRowChangeEvent..ctor` | `0x411dd3` | 62972 | ✓ |
| `method.Planetarium.CieloDomoForm.InitializeComponent` | `0x4031f0` | 6716 | ✓ |
| `method.Planetarium.MovimientoPlanetaForm.InitializeComponent` | `0x407608` | 4808 | — |
| `method.Planetarium.ConstelacionGuiaForm.InitializeComponent` | `0x405878` | 4380 | ✓ |
| `method.Planetarium.Engine.PlanetariumEngine.RenderizarTrayectoriaEfemerides` | `0x40ad08` | 2168 | ✓ |
| `method.Planetarium.Engine.PlanetariumEngine.RenderizarConstelacionDetalle` | `0x40a260` | 1400 | ✓ |
| `method.Planetarium.Engine.PlanetariumEngine.RenderizarSistemaSolar` | `0x40a7d8` | 1328 | ✓ |
| `method.Planetarium.Engine.ProyeccionDomo.DibujarRejillaDomo` | `0x40c17c` | 868 | ✓ |
| `method.PlanetasRow..ctor` | `0x4116df` | 772 | ✓ |
| `method.Planetarium.Engine.PlanetariumEngine.DibujarEstrellas` | `0x4099c0` | 720 | ✓ |
| `method.Planetarium.DatosCelestes..ctor` | `0x408a40` | 716 | ✓ |
| `method.PlanetasDataTable.InitClass` | `0x40f56c` | 716 | ✓ |
| `method.Planetarium.ConstelacionGuiaForm.ListaConstelaciones_DrawItem` | `0x405460` | 692 | ✓ |
| `method.Planetarium.CieloDomoForm.DisassembleImageData` | `0x402688` | 668 | ✓ |
| `method.Planetarium.Engine.ProyeccionDomo.DibujarRejillaEstereografica` | `0x40c4e0` | 664 | ✓ |
| `method.Planetarium.ConstelacionGuiaForm.ConfigurarTablaEstrellas` | `0x405038` | 636 | ✓ |
| `method.Planetarium.MovimientoPlanetaForm.ConfigurarTablaEfemerides` | `0x406d40` | 620 | ✓ |
| `method.Planetarium.MovimientoPlanetaForm.CalcularEfemeridesTabla` | `0x406fac` | 608 | — |
| `method.Planetarium.Engine.PlanetariumEngine.DibujarPlanetasEnDomo` | `0x40a00c` | 596 | ✓ |
| `method.EstrellasDataTable.GetTypedTableSchema` | `0x40d884` | 596 | ✓ |
| `method.ConstelacionesDataTable.GetTypedTableSchema` | `0x40e35c` | 596 | ✓ |
| `method.LineasConstelacionDataTable.GetTypedTableSchema` | `0x40ecf4` | 596 | ✓ |
| `method.PlanetasDataTable.GetTypedTableSchema` | `0x40f9ac` | 596 | ✓ |
| `method.EfemeridesHistorialDataTable.GetTypedTableSchema` | `0x41049c` | 596 | ✓ |
| `method.EfemeridesHistorial1DataTable.GetTypedTableSchema` | `0x410f8c` | 596 | ✓ |
| `method.Planetarium.DatosCelestes.ReadXmlSerializable` | `0x408e64` | 524 | ✓ |
| `method.EfemeridesHistorialRow..ctor` | `0x4119e3` | 504 | ✓ |
| `method.EfemeridesHistorial1Row..ctor` | `0x411bdb` | 504 | ✓ |

### Decompiled Code Files

- [`code/method.ConstelacionesDataTable.GetTypedTableSchema.c`](code/method.ConstelacionesDataTable.GetTypedTableSchema.c)
- [`code/method.ConstelacionesRow..ctor.c`](code/method.ConstelacionesRow..ctor.c)
- [`code/method.EfemeridesHistorial1DataTable.GetTypedTableSchema.c`](code/method.EfemeridesHistorial1DataTable.GetTypedTableSchema.c)
- [`code/method.EfemeridesHistorial1Row..ctor.c`](code/method.EfemeridesHistorial1Row..ctor.c)
- [`code/method.EfemeridesHistorialDataTable.GetTypedTableSchema.c`](code/method.EfemeridesHistorialDataTable.GetTypedTableSchema.c)
- [`code/method.EfemeridesHistorialRow..ctor.c`](code/method.EfemeridesHistorialRow..ctor.c)
- [`code/method.EstrellasDataTable.GetTypedTableSchema.c`](code/method.EstrellasDataTable.GetTypedTableSchema.c)
- [`code/method.EstrellasRowChangeEvent..ctor.c`](code/method.EstrellasRowChangeEvent..ctor.c)
- [`code/method.LineasConstelacionDataTable.GetTypedTableSchema.c`](code/method.LineasConstelacionDataTable.GetTypedTableSchema.c)
- [`code/method.Planetarium.CieloDomoForm.DisassembleImageData.c`](code/method.Planetarium.CieloDomoForm.DisassembleImageData.c)
- [`code/method.Planetarium.CieloDomoForm.InitializeComponent.c`](code/method.Planetarium.CieloDomoForm.InitializeComponent.c)
- [`code/method.Planetarium.ConstelacionGuiaForm.ConfigurarTablaEstrellas.c`](code/method.Planetarium.ConstelacionGuiaForm.ConfigurarTablaEstrellas.c)
- [`code/method.Planetarium.ConstelacionGuiaForm.InitializeComponent.c`](code/method.Planetarium.ConstelacionGuiaForm.InitializeComponent.c)
- [`code/method.Planetarium.ConstelacionGuiaForm.ListaConstelaciones_DrawItem.c`](code/method.Planetarium.ConstelacionGuiaForm.ListaConstelaciones_DrawItem.c)
- [`code/method.Planetarium.DatosCelestes..ctor.c`](code/method.Planetarium.DatosCelestes..ctor.c)
- [`code/method.Planetarium.DatosCelestes.ReadXmlSerializable.c`](code/method.Planetarium.DatosCelestes.ReadXmlSerializable.c)
- [`code/method.Planetarium.Engine.PlanetariumEngine.DibujarEstrellas.c`](code/method.Planetarium.Engine.PlanetariumEngine.DibujarEstrellas.c)
- [`code/method.Planetarium.Engine.PlanetariumEngine.DibujarPlanetasEnDomo.c`](code/method.Planetarium.Engine.PlanetariumEngine.DibujarPlanetasEnDomo.c)
- [`code/method.Planetarium.Engine.PlanetariumEngine.RenderizarConstelacionDetalle.c`](code/method.Planetarium.Engine.PlanetariumEngine.RenderizarConstelacionDetalle.c)
- [`code/method.Planetarium.Engine.PlanetariumEngine.RenderizarSistemaSolar.c`](code/method.Planetarium.Engine.PlanetariumEngine.RenderizarSistemaSolar.c)
- [`code/method.Planetarium.Engine.PlanetariumEngine.RenderizarTrayectoriaEfemerides.c`](code/method.Planetarium.Engine.PlanetariumEngine.RenderizarTrayectoriaEfemerides.c)
- [`code/method.Planetarium.Engine.ProyeccionDomo.DibujarRejillaDomo.c`](code/method.Planetarium.Engine.ProyeccionDomo.DibujarRejillaDomo.c)
- [`code/method.Planetarium.Engine.ProyeccionDomo.DibujarRejillaEstereografica.c`](code/method.Planetarium.Engine.ProyeccionDomo.DibujarRejillaEstereografica.c)
- [`code/method.Planetarium.MovimientoPlanetaForm.ConfigurarTablaEfemerides.c`](code/method.Planetarium.MovimientoPlanetaForm.ConfigurarTablaEfemerides.c)
- [`code/method.PlanetasDataTable.GetTypedTableSchema.c`](code/method.PlanetasDataTable.GetTypedTableSchema.c)
- [`code/method.PlanetasDataTable.InitClass.c`](code/method.PlanetasDataTable.InitClass.c)
- [`code/method.PlanetasRow..ctor.c`](code/method.PlanetasRow..ctor.c)
- [`code/method.__c__DisplayClass53_0._RenderizarTrayectoriaEfemerides_b__0.c`](code/method.__c__DisplayClass53_0._RenderizarTrayectoriaEfemerides_b__0.c)

## Behavioral Analysis

This final segment of disassembly (Chunk 8/8) provides the ultimate confirmation of the technical capabilities and sophistication of the protection layer. It moves our observation from "highly obfuscated" to **"computationally opaque."**

The inclusion of this final chunk completes the picture of a professional-grade, industrial-strength security implementation designed to make manual code auditing virtually impossible for anyone without specialized tools.

### Updated Analysis Summary (Chunk 8/8)

The analysis of the final chunk confirms that the software utilizes **Virtual Machine (VM) Protection** as its primary defense mechanism. The assembly is no longer "standard" x86_64; it has been transformed into a custom bytecode format interpreted by a virtual machine engine embedded within the binary.

---

### New Technical Observations

#### 1. Confirmation of VM-based Execution
The sheer density of `CONCAT`, `POPCOUNT`, and complex bitwise arithmetic in functions like `method.PlanetasRow.set_ColorARGB` is characteristic of a **VM Dispatcher**.
*   **Mechanism:** Instead of the CPU executing "Set Color," it is executing an instruction that says "Interpret Byte X." The long chains of math you see are the VM's internal logic for decoding, de-obfuscating, and executing that single byte of custom code.
*   **Impact:** This means the "actual" logic for how colors or coordinates are handled doesn't exist in a readable format anywhere in the binary. It only exists in the state of the virtual machine as it runs in memory.

#### 2. Intentional "Decompiler Poisoning"
The decompiler warnings—`halt_baddata`, `overlapping instruction`, and `cannot track spacebase`—are not bugs in Ghidra; they are **features of the protection.**
*   **Analysis:** The protector intentionally inserts "junk bytes" or overlapping instructions. When a standard disassembler tries to process these, it loses its place (the "broken" logic seen in your logs). 
*   **Impact:** This is designed to frustrate automated analysis tools and human reverse-engineers alike by creating a "minefield" of invalid paths that lead to the `halt_baddata` state.

#### 3. Control Flow Flattening (CFF)
In both `method.PlanetasRow.set_ColorARGB` and `method.EfemeridesHistorial1Row..ctor`, the logic flow is "flattened." Rather than a logical progression of steps, the code appears as a massive web of similar-looking blocks.
*   **Analysis:** By flattening the control flow, the developer has removed the "story" of the code. You can no longer see where an `if` statement leads or what a `loop` is doing because every branch looks like a complex mathematical transformation leading to the next potential jump.

#### 4. Just-In-Time (JIT) Logic Decryption
Several sections show data being manipulated by large, arbitrary constants (e.g., `0x28010000`, `0x3060001`).
*   **Analysis:** This suggests that the real values (like specific coordinates or color values) are encrypted in memory and only "unpacked" into a usable state at the exact micro-second they are needed by the engine.
*   **Impact:** Even if you dump the memory of the program while it is running, much of the "plain text" data will be hidden behind these mathematical transformations until the moment of use.

---

### Updated Summary Table (Final)

| Feature | Observation | Risk Level |
| :--- | :--- | :--- |
| **Primary Purpose** | Astronomy / Planetarium Engine | Low (Contextual) |
| **Obfuscation Technique** | **VM-Protection**, Control Flow Flattening, Instruction Overlapping. | **Extreme** |
| **Anti-Analysis Indicators** | "Bad instructions," forced overflows, and repetitive "math maze" patterns. | **Critical** |
| **Engineering Quality** | Top-tier, professional protection (likely a modified commercial engine). | **High** |
| **Intellectual Property** | The core physics/mathematics of the celestial model are fully shielded. | **Critical** |

---

### Final Synthesis & Conclusion

The analysis across all 8 chunks reveals a sophisticated defense strategy designed to protect high-value intellectual property (specifically, the proprietary astronomical algorithms and data structures).

1.  **Unified Defense:** The protection is applied globally. There is no "weak" path; whether you are looking at planet orbits (`Planetas`), history logs (`Efemerides`), or simple UI colors, the code has been processed by the same heavy-duty obfuscation engine.
2.  **The "VM" Barrier:** The most significant finding is that the software utilizes a **Virtual Machine**. This means the logic you are attempting to read in Ghidra is not "the code"—it is the *interpreter* of the code. To find the real math, one would have to reverse-engineer the virtual machine's instruction set (a task that can take months of specialized effort).
3.  **Active Deterrence:** The inclusion of "junk" instructions and overlapping bytes purposefully targets tools like Ghidra/IDA. It creates a situation where automated de-compilation yields nonsensical results, forcing the analyst to spend thousands of man-hours manually tracing a single logic path.

### Strategic Recommendation:
**Stop Static Analysis.** 
At this stage, further analysis using static disassembly will yield diminishing returns. The "math maze" is too dense to solve by hand. 

**Switch to Dynamic Instrumentation:**
To proceed, the investigation should move to **dynamic tracing**:
*   **Hardware Breakpoints/Tracing:** Use a debugger (like x64dbg) to watch how values change in memory *after* they pass through the "maze." 
*   **Memory Dumping:** Capture the state of memory at specific moments to see the "plain" data after the VM has decoded it.
*   **API Hooking:** Use a tool like Frida to intercept the final results (e.g., coordinates, colors) as they are passed to the rendering engine, effectively bypassing the obfuscation layer entirely.

**Final Conclusion:** This is a highly professional piece of software protected by an industrial-grade security suite. It is designed to ensure that its proprietary formulas for celestial movement and data parsing remain inaccessible to competitors or third parties.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your technical analysis to the corresponding MITRE ATT&CK techniques. 

Because these are all methods designed to hide logic, obfuscate code, and frustrate reverse engineering, they primarily fall under the **Obfuscated Files or Information** category. However, each represents a distinct tactical application of that technique.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1028 | Obfuscated Files or Information | The use of a custom Virtual Machine (VM) to execute bytecode hides the original logic behind an opaque "interpretation" layer. |
| T1028 | Obfuscated Files or Information | The insertion of junk bytes and overlapping instructions is specifically designed to cause "Decompiler Poisoning" in tools like Ghidra/IDA. |
| T1028 | Obfuscated Files or Information | Control Flow Flattening (CFF) removes the logical progression of the code, replacing clear branching with a mathematically complex web of equivalent blocks. |
| T1028 | Obfuscated Files or Information | Just-In-Time (JIT) Logic Decryption ensures that sensitive data and instructions are only decrypted in memory at the moment of execution to avoid detection by static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   `D4622EBE266BDF6D7FB7759D8BB42A37644D8F22462641F1E79C12CF2F50BEB5` (Note: This 64-character hex string appears in the code; while its exact function is obscured by the VM protection, it serves as a unique identifier or key within the binary).

**Other artifacts**
*   **Obfuscation Techniques:** Virtual Machine (VM) Protection, Control Flow Flattening (CFF), and Instruction Overlapping.
*   **Anti-Analysis Measures:** Use of "junk" bytes to trigger `halt_baddata` and `overlapping instruction` errors in disassemblers like Ghidra/IDA.
*   **JIT Decryption:** Use of large constants (e.g., `0x28010000`, `0x3060001`) to decrypt data at runtime.

---
**Analyst Note:** The sample exhibits high-sophistication defensive layers characteristic of commercial-grade protection or advanced malware. While traditional network IOCs (IPs/URLs) were not present in the provided text, the presence of a **VM-based execution engine** indicates that any malicious behavior is likely hidden within a custom bytecode layer, making static analysis ineffective.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family:** Unknown (Likely a commercial software protection layer)
2. **Malware type:** Loader / Packer 
3. **Confidence:** Medium
4. **Key evidence:**
    *   **Advanced Obfuscation Techniques:** The sample utilizes professional-grade "VM Protection," Control Flow Flattening (CFF), and instruction overlapping to create a "computationally opaque" environment, which are hallmark techniques for both high-end commercial software protection and sophisticated malware loaders.
    *   **Anti-Analysis Intent:** The presence of deliberate "decompiler poisoning" (junk bytes/overlapping instructions) indicates an intentional effort to thwart automated analysis tools like Ghidra or IDA Pro.
    *   **Ambiguous Context:** While the internal strings refer to a "Planetarium Engine" and astronomical math, the lack of traditional malicious indicators (C2 IPs, file system tampering, etc.) suggests the sample is currently categorized as a highly-protected piece of software; however, the technical methods used are indistinguishable from those found in advanced malware infrastructure.
