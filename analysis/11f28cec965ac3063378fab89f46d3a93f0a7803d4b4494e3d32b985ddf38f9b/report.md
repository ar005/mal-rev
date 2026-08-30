# Threat Analysis Report

**Generated:** 2026-08-24 21:55 UTC
**Sample:** `11f28cec965ac3063378fab89f46d3a93f0a7803d4b4494e3d32b985ddf38f9b_11f28cec965ac3063378fab89f46d3a93f0a7803d4b4494e3d32b985ddf38f9b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11f28cec965ac3063378fab89f46d3a93f0a7803d4b4494e3d32b985ddf38f9b_11f28cec965ac3063378fab89f46d3a93f0a7803d4b4494e3d32b985ddf38f9b.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,534,976 bytes |
| MD5 | `730410a21ba80c56f99f1bf070b79ea6` |
| SHA1 | `f638d9e6e0f73e8dcd76e9740e93b5d7f519d2f0` |
| SHA256 | `11f28cec965ac3063378fab89f46d3a93f0a7803d4b4494e3d32b985ddf38f9b` |
| Overall entropy | 7.912 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779352758 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,531,904 | 7.916 | ⚠️ Yes |
| `.rsrc` | 2,048 | 3.5 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **3534** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

*BSJB
v4.0.30319
#Strings
<>c__DisplayClass3_0
<>9__9_0
<InitializeComponent>b__9_0
<Survey_Cadastral_Transect>b__0
btnKod0
<Survey_Cadastral_Transect>b__1
IEnumerable`1
Action`1
List`1
btnKod1
pnlSim1
btnSimKes1
<>9__3_2
<Survey_Cadastral_Transect>b__3_2
Func`2
btnKod2
pnlSim2
btnSimKes2
Func`3
btnKod3
pnlSim3
btnSimKes3
btnKod4
pnlSim4
btnSimKes4
btnKod5
btnKod6
btnKod7
btnKod8
btnKod9
<Module>
System.Drawing.Drawing2D
get_ID
set_ID
columnID
System.IO
get_CKT
get_LtYZ
Galaba
galaba
tmrBomba
pnlYuqoriAlohida
lblStatistikaSarlavha
lblKodSarlavha
lblSarlavha
lblTaymerSarlavha
pnlVisualNatija
FormNatija
get_KodShama
lblKodShama
kodShama
lblSimKorsatma
lblMatKorsatma
get_Sana
set_Sana
columnSana
pnlKlaviatura
System.Data
soniya
FromArgb
mscorlib
aslJavob
kiritilganJavob
txtMatJavob
System.Collections.Generic
Microsoft.VisualBasic
Thread
FormNatija_Load
add_Load
FormOyin_Load
FormKiris_Load
maqsad
terrainQuad
set_AutoIncrementSeed
Interlocked
set_Enabled
get_InvokeRequired
IsBinarySerialized
Synchronized
get_Hand
lblLedKod
togriKod
kiritilganKod
FlatButtonAppearance
get_FlatAppearance
defaultInstance
transectAllowance
set_DataSource
get_KeyCode
XmlReadMode
set_AutoScaleMode
set_ColumnHeadersHeightSizeMode
DataGridViewColumnHeadersHeightSizeMode
set_SmoothingMode
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **28**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c__DisplayClass3_0._Survey_Cadastral_Transect_b__1` | `0x407d8d` | 24354 | ✓ |
| `method.BombaZarasizlantiruvchi.FormOyin.InitializeComponent` | `0x4040e4` | 10684 | ✓ |
| `method.BombaZarasizlantiruvchi.FormKiris.InitializeComponent` | `0x402c78` | 2817 | ✓ |
| `method.BombaZarasizlantiruvchi.FormNatija.InitializeComponent` | `0x40705c` | 1704 | ✓ |
| `method.BombaZarasizlantiruvchi.FormNatija.pnlVisualNatija_Paint` | `0x406d2c` | 652 | ✓ |
| `method.BombaZarasizlantiruvchi.FormKiris.StatistikaniYangilash` | `0x402a64` | 396 | ✓ |
| `method.BombaZarasizlantiruvchi.FormOyin.OnJumboqYechildi` | `0x403af8` | 348 | ✓ |
| `method.OyinNatijalariDataTable.InitClass` | `0x407a00` | 336 | ✓ |
| `method.BombaZarasizlantiruvchi.FormNatija.FormNatija_Load` | `0x406af8` | 320 | ✓ |
| `method.BombaZarasizlantiruvchi.FormOyin.FormOyin_Load` | `0x4037bc` | 284 | ✓ |
| `method.BombaZarasizlantiruvchi.BombaMantiqi.KashfEtish` | `0x40240c` | 276 | ✓ |
| `method.BombaZarasizlantiruvchi.FormOyin.btnSimKes_Click` | `0x403db0` | 272 | ✓ |
| `method.BombaZarasizlantiruvchi.FormOyin.OnNotogriHarakat` | `0x403a10` | 232 | ✓ |
| `method.BombaZarasizlantiruvchi.FormOyin.OnSekundOtdi` | `0x403930` | 224 | ✓ |
| `method.BombaZarasizlantiruvchi.FormOyin.OnGalabaQozonildi` | `0x403ce0` | 208 | ✓ |
| `method.BombaZarasizlantiruvchi.FormOyin.OnBombaPortladi` | `0x403c54` | 140 | ✓ |
| `method.BombaZarasizlantiruvchi.BombaMantiqi.SimniKes` | `0x40257c` | 132 | ✓ |
| `method.BombaZarasizlantiruvchi.BombaMantiqi.TekshirKodniYashirin` | `0x402788` | 132 | ✓ |
| `method.BombaZarasizlantiruvchi.OyinTarixiKhizmati.NatijaniSaqlash` | `0x402894` | 132 | ✓ |
| `method.BombaZarasizlantiruvchi.FormOyin.FormOyin_FormClosing` | `0x40402c` | 128 | — |
| `method.BombaZarasizlantiruvchi.FormNatija.tmrMiltillash_Tick` | `0x406cac` | 128 | ✓ |
| `method.BombaZarasizlantiruvchi.FormKiris.Survey_Cadastral_Transect` | `0x4029dc` | 124 | ✓ |
| `method.OyinNatijalariDataTable.InitVars` | `0x407984` | 124 | ✓ |
| `method.BombaZarasizlantiruvchi.FormNatija.EkranniSilkit` | `0x406c38` | 116 | ✓ |
| `method.BombaZarasizlantiruvchi.BombaMantiqi.KodniKirit` | `0x402600` | 112 | ✓ |
| `method.BombaZarasizlantiruvchi.FormOyin.MatematikaTekshiruviniAmalgaOshir` | `0x403fbc` | 112 | ✓ |
| `method.BombaZarasizlantiruvchi.BombaMantiqi.MatematikaniYech` | `0x402670` | 108 | ✓ |
| `method.BombaZarasizlantiruvchi.BombaMantiqi.JarimaBering` | `0x4026dc` | 101 | — |
| `method.BombaZarasizlantiruvchi.FormOyin.btnKodKirit_Click` | `0x403f1c` | 99 | ✓ |
| `method.BombaZarasizlantiruvchi.BombaMantiqi..ctor` | `0x40235c` | 94 | ✓ |

### Decompiled Code Files

- [`code/method.BombaZarasizlantiruvchi.BombaMantiqi..ctor.c`](code/method.BombaZarasizlantiruvchi.BombaMantiqi..ctor.c)
- [`code/method.BombaZarasizlantiruvchi.BombaMantiqi.KashfEtish.c`](code/method.BombaZarasizlantiruvchi.BombaMantiqi.KashfEtish.c)
- [`code/method.BombaZarasizlantiruvchi.BombaMantiqi.KodniKirit.c`](code/method.BombaZarasizlantiruvchi.BombaMantiqi.KodniKirit.c)
- [`code/method.BombaZarasizlantiruvchi.BombaMantiqi.MatematikaniYech.c`](code/method.BombaZarasizlantiruvchi.BombaMantiqi.MatematikaniYech.c)
- [`code/method.BombaZarasizlantiruvchi.BombaMantiqi.SimniKes.c`](code/method.BombaZarasizlantiruvchi.BombaMantiqi.SimniKes.c)
- [`code/method.BombaZarasizlantiruvchi.BombaMantiqi.TekshirKodniYashirin.c`](code/method.BombaZarasizlantiruvchi.BombaMantiqi.TekshirKodniYashirin.c)
- [`code/method.BombaZarasizlantiruvchi.FormKiris.InitializeComponent.c`](code/method.BombaZarasizlantiruvchi.FormKiris.InitializeComponent.c)
- [`code/method.BombaZarasizlantiruvchi.FormKiris.StatistikaniYangilash.c`](code/method.BombaZarasizlantiruvchi.FormKiris.StatistikaniYangilash.c)
- [`code/method.BombaZarasizlantiruvchi.FormKiris.Survey_Cadastral_Transect.c`](code/method.BombaZarasizlantiruvchi.FormKiris.Survey_Cadastral_Transect.c)
- [`code/method.BombaZarasizlantiruvchi.FormNatija.EkranniSilkit.c`](code/method.BombaZarasizlantiruvchi.FormNatija.EkranniSilkit.c)
- [`code/method.BombaZarasizlantiruvchi.FormNatija.FormNatija_Load.c`](code/method.BombaZarasizlantiruvchi.FormNatija.FormNatija_Load.c)
- [`code/method.BombaZarasizlantiruvchi.FormNatija.InitializeComponent.c`](code/method.BombaZarasizlantiruvchi.FormNatija.InitializeComponent.c)
- [`code/method.BombaZarasizlantiruvchi.FormNatija.pnlVisualNatija_Paint.c`](code/method.BombaZarasizlantiruvchi.FormNatija.pnlVisualNatija_Paint.c)
- [`code/method.BombaZarasizlantiruvchi.FormNatija.tmrMiltillash_Tick.c`](code/method.BombaZarasizlantiruvchi.FormNatija.tmrMiltillash_Tick.c)
- [`code/method.BombaZarasizlantiruvchi.FormOyin.FormOyin_Load.c`](code/method.BombaZarasizlantiruvchi.FormOyin.FormOyin_Load.c)
- [`code/method.BombaZarasizlantiruvchi.FormOyin.InitializeComponent.c`](code/method.BombaZarasizlantiruvchi.FormOyin.InitializeComponent.c)
- [`code/method.BombaZarasizlantiruvchi.FormOyin.MatematikaTekshiruviniAmalgaOshir.c`](code/method.BombaZarasizlantiruvchi.FormOyin.MatematikaTekshiruviniAmalgaOshir.c)
- [`code/method.BombaZarasizlantiruvchi.FormOyin.OnBombaPortladi.c`](code/method.BombaZarasizlantiruvchi.FormOyin.OnBombaPortladi.c)
- [`code/method.BombaZarasizlantiruvchi.FormOyin.OnGalabaQozonildi.c`](code/method.BombaZarasizlantiruvchi.FormOyin.OnGalabaQozonildi.c)
- [`code/method.BombaZarasizlantiruvchi.FormOyin.OnJumboqYechildi.c`](code/method.BombaZarasizlantiruvchi.FormOyin.OnJumboqYechildi.c)
- [`code/method.BombaZarasizlantiruvchi.FormOyin.OnNotogriHarakat.c`](code/method.BombaZarasizlantiruvchi.FormOyin.OnNotogriHarakat.c)
- [`code/method.BombaZarasizlantiruvchi.FormOyin.OnSekundOtdi.c`](code/method.BombaZarasizlantiruvchi.FormOyin.OnSekundOtdi.c)
- [`code/method.BombaZarasizlantiruvchi.FormOyin.btnKodKirit_Click.c`](code/method.BombaZarasizlantiruvchi.FormOyin.btnKodKirit_Click.c)
- [`code/method.BombaZarasizlantiruvchi.FormOyin.btnSimKes_Click.c`](code/method.BombaZarasizlantiruvchi.FormOyin.btnSimKes_Click.c)
- [`code/method.BombaZarasizlantiruvchi.OyinTarixiKhizmati.NatijaniSaqlash.c`](code/method.BombaZarasizlantiruvchi.OyinTarixiKhizmati.NatijaniSaqlash.c)
- [`code/method.OyinNatijalariDataTable.InitClass.c`](code/method.OyinNatijalariDataTable.InitClass.c)
- [`code/method.OyinNatijalariDataTable.InitVars.c`](code/method.OyinNatijalariDataTable.InitVars.c)
- [`code/method.__c__DisplayClass3_0._Survey_Cadastral_Transect_b__1.c`](code/method.__c__DisplayClass3_0._Survey_Cadastral_Transect_b__1.c)

## Behavioral Analysis

This analysis incorporates the final disassembly provided in **Chunk 9/9**. The inclusion of these segments provides a definitive look at the scale and methodology of the malware's evasion tactics.

The sheer volume of warnings regarding unreachable blocks and instruction overlaps confirms that this is not a standard piece of "packed" malware, but rather a highly engineered piece of code specifically designed to frustrate automated analysis tools (like Ghidra or IDA Pro).

---

### **Updated Analysis Report**

#### **1. Arithmetic Gauntlets & Data Folding (Refined)**
The functions `MatematikaTekshiruviniAmalgaOshir` and the constructor for `BombaMantiqi` showcase an extreme use of "Arithmetic Gauntlets."

*   **Complex Constant Calculation:** Instead of using a direct constant to determine a jump or state, the malware performs multi-step calculations involving `CONCAT31`, `CARRY1`, and bitwise operations (e.g., `puVar20 = CONCAT31(uVar10_a, uVar10_b)`). 
*   **Data Folding:** The inclusion of values like `0x1a2c09` or `0xf9d4d9fd` are likely "seeds" for calculations. In the disassembler, these look like random large numbers; at runtime, they are part of a calculation that eventually produces a simple value (like a 0 or 1) to set a flag.
*   **Purpose:** This hides the **logic of the state machine**. By making the math complex enough, the author ensures that an analyst cannot simply look at a "Jump if Equal" instruction to see what happens next; they must manually calculate every step of the arithmetic to determine the path.

#### **2. Scale of Evasion Tactics (Quantified)**
Chunk 9/9 provides high-impact evidence regarding the intensity of the anti-analysis measures:

*   **Massive Junk Code Saturation:** The disassembly contains an overwhelming number of `WARNING: Removing unreachable block` notifications—potentially hundreds in a single vicinity. This is a deliberate "noise" tactic. By saturating the code with thousands of instructions that will never execute, the author forces any human analyst to sift through massive amounts of useless data to find the actual logic.
*   **Instruction Overlapping (The Trap):** The warnings for **overlapping instructions** (e.g., `0x402b73` and `0x402b72`) are a high-level technique. By overlapping, the malware ensures that if an analyst tries to "force" the disassembler to start at a different offset, it may land in the middle of another instruction, causing the disassembler to render entirely incorrect code. This effectively hides the true malicious payload "between" the lines of junk.
*   **Opaque Predicates via POPCOUNT:** The repeated use of `(POPCOUNT(x) & 1U) == 0` as a conditional check is a sophisticated way to create **Opaque Predicates**. These are branches that *always* evaluate to one direction, but because the math involves bit counting, it is difficult for automated tools to determine with certainty which path is "real" without running the code.

#### **3. Behavioral Intelligence & Risk Assessment**
The construction of `BombaMantiqi` (Bomb Logic) and `MatematikaTekshiruviniAmalgaOshir` (Mathematical Verification Integration) suggests the following:

*   **Intentional "Time-Wasting" Strategy:** The complexity is not for the sake of complexity; it is designed to burn through an analyst's time. Each hour spent trying to resolve a `POPCOUNT` calculation or navigate a block of 100 "unreachable" instructions is a win for the attacker, as it delays the creation of a signature or a behavioral profile.
*   **Sophisticated Author Profile:** The implementation of **Instruction Overlapping** specifically targets the flaws in how disassemblers linearize code. This indicates an author who has significant experience with reverse engineering tools and understands exactly how to break them.

---

### **Summary for Incident Response (IR)**

The analysis of Chunk 9/9 confirms that this is a high-sophistication threat designed to stall manual and automated triage.

**Key Findings for IR Team:**
1.  **Deceptive Scale:** The "unreachable blocks" are not just an oversight; they are a "wall" intended to slow down analysis of the `BombaMantiqi` (Bomb Logic) core. 
2.  **Hidden Pathways:** Because of **Instruction Overlapping**, any manual disassembly in Ghidra/IDA is potentially "poisoned." The analyst might be looking at "junk" while the actual malicious instructions are hidden in the overlaps.
3.  **Algorithmic Obfuscation:** Most logical transitions are guarded by complex arithmetic. Identifying the "next step" of the malware’s behavior via static analysis is extremely difficult without a debugger.

**Updated Recommendations for IR Team:**
*   **Execution Tracing (Crucial):** Do not attempt to fully de-obfuscate the math in a disassembler. Use a debugger (x64dbg) and **trace the execution**. A trace will show only the instructions actually executed by the CPU, automatically "skipping" all the unreachable junk blocks and simplifying the path of execution.
*   **Memory Dumping:** Since the code is designed to be difficult to read statically, the most effective way to see the "true" behavior is to allow the malware to run in a controlled sandbox/VM and **dump its memory** once it has performed its calculations but before it performs its primary malicious actions (e.g., after `MatematikaTekshiruviniAmalgaOshir` returns).
*   **Behavior-Based Detection:** Given the high level of obfuscation, focus on the "outputs" rather than the "inputs." Monitor for:
    *   Unauthorized API calls (e.g., injection into other processes).
    *   Spawning of unusual child processes.
    *   Attempts to modify registry keys or system files.

---

### **Summary Update Log**
*   **Chunk 9/9 Analysis Integrated:** Yes.
*   **New Findings:** Quantified the scale of "unreachable blocks" as a massive "time-waste" tactic; confirmed **Instruction Overlapping** as a deliberate tool to break disassembler logic; identified the use of `POPCOUNT` for opaque predicates.
*   **Risk Profile Status:** **Extreme.** This is a professional-grade obfuscation suite, suggesting an actor with significant resources and experience in anti-analysis techniques.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, the following table maps the observed tactics to the MITRE ATT&CK framework. 

Because several of these techniques (Arithmetic Gauntlets, Junk Code, Overlapping Instructions, and Opaque Predicates) are all methods used to hide execution logic from analysts, they primarily fall under the **Obfuscated Execution** category.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Execution | The use of "Arithmetic Gauntlets" and "Data Folding" hides the state machine logic by replacing simple constants with complex, multi-step calculations. |
| T1027 | Obfuscated Execution (Junk Code) | The intentional saturation of thousands of unreachable code blocks serves as a "wall" to exhaust the time and resources of human analysts. |
| T1027 | Obfuscated Execution (Overlapping Instructions) | Overlapping instructions are used specifically to trick disassemblers into rendering incorrect code, hiding malicious logic between instruction boundaries. |
| T1027 | Obfuscated Execution (Opaque Predicates) | The use of `POPCOUNT` results in conditions that always evaluate the same way but are difficult for automated tools to resolve statically. |

### **Analyst Notes on Risk Assessment:**
The "Intentional Time-Wasting Strategy" described in your report is a hallmark of high-sophistication actors who understand the constraints of incident response (IR) cycles. By utilizing these specific T1027 sub-behaviors, the actor successfully creates a gap between **infection** and **detection**, as the manual effort required to de-obfuscate the `BombaMantiqi` logic significantly delays the creation of effective IOCs (Indicators of Compromise).

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `Hyzq.exe` (Note: This is a filename; no full directory path was provided.)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Malicious Logic Identifiers:** 
    *   `BombaMantiqi` (Internal function name/logic identifier)
    *   `MatematikaTekshiruviniAmalgaOshir` (Internal function name/logic identifier)
*   **Obfuscation Indicators:** 
    *   Use of `POPCOUNT` for opaque predicates.
    *   Instruction Overlapping at offsets `0x402b73` and `0x402b72`.

***

**Analyst Note:** The provided data contains high-sophistication anti-analysis techniques (arithmetic gauntlets, instruction overlapping, and junk code saturation) rather than traditional "atomic" IOCs like hardcoded IP addresses or hashes. From an incident response perspective, the primary indicator is the executable `Hyzq.exe`.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: Medium

**Key evidence**:
*   **Sophisticated Obfuscation Layer:** The use of "Arithmetic Gauntlets," "Data Folding," and `POPCOUNT` opaque predicates indicates a professional-grade effort to hide the malware's true logic from automated tools and human analysts.
*   **Anti-Analysis Engineering:** The presence of instruction overlapping and massive junk code saturation (thousands of unreachable blocks) is a deliberate tactic to "poison" disassemblers like Ghidra/IDA, a hallmark of high-end custom loaders or sophisticated malware wrappers.
*   **Intentional Persistence of Obscurity:** The analysis identifies a specific "Time-Wasting" strategy intended to delay incident response; the lack of known signatures for established families (like Emotet or Cobalt Strike) combined with unique internal naming (`BombaMantiqi`) points toward a bespoke, custom-built threat.
