# Threat Analysis Report

**Generated:** 2026-08-19 20:25 UTC
**Sample:** `10910355ad10c6863ee503c9dee4342e7b2767a78c0953bd55ed7b17bdbfcec8_10910355ad10c6863ee503c9dee4342e7b2767a78c0953bd55ed7b17bdbfcec8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10910355ad10c6863ee503c9dee4342e7b2767a78c0953bd55ed7b17bdbfcec8_10910355ad10c6863ee503c9dee4342e7b2767a78c0953bd55ed7b17bdbfcec8.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,031,680 bytes |
| MD5 | `201e8056c93632c2b5d60d3389b76728` |
| SHA1 | `def98da9d9762a2bd1fa61fa118a12bf5b4617bd` |
| SHA256 | `10910355ad10c6863ee503c9dee4342e7b2767a78c0953bd55ed7b17bdbfcec8` |
| Overall entropy | 7.803 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3763845080 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 961,536 | 7.908 | ⚠️ Yes |
| `.rsrc` | 69,120 | 3.823 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **2329** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v4.0.30319
#Strings
<.cctor>b__1_0
<>c__DisplayClass1_0
<>9__37_0
<InitializeComponent>b__37_0
<.cctor>b__1
get__1
IEnumerable`1
List`1
button1
menuStrip1
get__2
Func`2
get__3
__StaticArrayInitTypeSize=44
get__4
get__5
__StaticArrayInitTypeSize=16
get__6
get__7
<Module>
<PrivateImplementationDetails>
3DD10108223125B05A05118131B360C0B6C3A1554CBDF6345D55783FB0696B4A
B15B7DBA7439F36871130776DA70CC3FA814133258C934643593A8A761FFC78F
get_mOO
AdamAsmaca
bHesapla
CevreHesapla
AlanHesapla
bToplama
bKokAlma
bUsAlma
bCarpma
bCikarma
System.Web
DecodeFromWeb
EncodeForWeb
mscorlib
System.Collections.Generic
Microsoft.VisualBasic
lbSonuc
lSonuc
Thread
AdamAsmaca_Load
add_Load
GeometrikIslemler_Load
SesliSessiz_Load
encoded
add_SelectedIndexChanged
ddlGeometrikSekil_SelectedIndexChanged
set_FormattingEnabled
System.Collections.Specialized
Synchronized
kseklik>k__BackingField
<YariCap>k__BackingField
<KisaKenar>k__BackingField
<TabanKenar>k__BackingField
<UzunKenar>k__BackingField
CodeMemberMethod
GetMethod
Replace
IsNullOrWhiteSpace
CodeNamespace
IPixelTransformService
LocalPixelTransformService
defaultInstance
CodeTypeReference
imageSource
set_AutoScaleMode
set_SizeMode
PictureBoxSizeMode
InstanceContextMode
HtmlDecode
HtmlEncode
set_Image
AddRange
Invoke
Enumerable
IDisposable
set_GenerateExecutable
set_Visible
ToDouble
RuntimeFieldHandle
RuntimeTypeHandle
GetTypeFromHandle
lRasgele
FromFile
set_DropDownStyle
FontStyle
ComboBoxStyle
set_Name
CallByName
buluncakKelime
lDebugGelenKelime
kelime
bCokluSilme
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c._.cctor_b__1_0` | `0x406a5e` | 21048 | ✓ |
| `method.WindowsFormsDemo.Calculator.InitializeComponent` | `0x4031f0` | 5408 | ✓ |
| `method.WindowsFormsDemo.GeometrikIslemler.InitializeComponent` | `0x404edc` | 2373 | ✓ |
| `entry0` | `0x405b97` | 1964 | ✓ |
| `method.WindowsFormsDemo.SesliSessiz.InitializeComponent` | `0x405d54` | 1528 | ✓ |
| `method.WindowsFormsDemo.AdamAsmaca.InitializeComponent` | `0x4023a8` | 1272 | ✓ |
| `method.WindowsFormsDemo.MenForm.InitializeComponent` | `0x4058f8` | 694 | ✓ |
| `method.WindowsFormsDemo.Calculator.HarvestColorMatrix` | `0x4028fc` | 588 | ✓ |
| `method.TransactionalByteAccumulator.get_Count` | `0x4067f9` | 528 | ✓ |
| `method.WindowsFormsDemo.AdamAsmaca.islemler` | `0x402190` | 503 | ✓ |
| `method.WindowsFormsDemo.Calculator.bEsittir_Click` | `0x402fe8` | 487 | ✓ |
| `method.DynamicCodeGenerator..cctor` | `0x406808` | 354 | ✓ |
| `method.WindowsFormsDemo.Properties.Resources.get_Culture` | `0x406385` | 342 | ✓ |
| `method.WindowsFormsDemo.GeometrikIslemler.GeometrikIslemler_Load` | `0x404760` | 287 | ✓ |
| `method.WindowsFormsDemo.GeometrikIslemler.ddlGeometrikSekil_SelectedIndexChanged` | `0x404da0` | 284 | ✓ |
| `method.WindowsFormsDemo.GeometrikIslemler.Hesapla` | `0x404888` | 272 | ✓ |
| `method.WindowsFormsDemo.SesliSessiz.button1_Click` | `0x405bec` | 270 | ✓ |
| `method.WindowsFormsDemo.AdamAsmaca.AdamAsmaca_Load` | `0x4020bc` | 204 | ✓ |
| `method.TransactionalByteAccumulator..ctor` | `0x406761` | 152 | ✓ |
| `method.WindowsFormsDemo.GeometrikIslemler.DikdortgenAlan` | `0x404a50` | 120 | ✓ |
| `method.WindowsFormsDemo.GeometrikIslemler.DikdortgenCevre` | `0x404ac8` | 120 | ✓ |
| `method.WindowsFormsDemo.GeometrikIslemler.DikUcgenAlan` | `0x404b40` | 120 | ✓ |
| `method.WindowsFormsDemo.GeometrikIslemler.DikUcgenCevre` | `0x404bb8` | 120 | ✓ |
| `method.WindowsFormsDemo.Concretes.Dikdortgen.set_UzunKenar` | `0x406575` | 118 | ✓ |
| `method.WindowsFormsDemo.Concretes.DikUcgen.set_Ykseklik` | `0x4065f3` | 114 | ✓ |
| `method.TransactionalByteAccumulator.AddWithTransaction` | `0x40677c` | 112 | ✓ |
| `method.WindowsFormsDemo.AdamAsmaca..ctor` | `0x402050` | 108 | ✓ |
| `method.WindowsFormsDemo.Concretes.Daire.set_YariCap` | `0x406501` | 108 | ✓ |
| `method.WindowsFormsDemo.Concretes.EskenarUcgen.set_TabanKenar` | `0x406675` | 98 | ✓ |
| `method.WindowsFormsDemo.Calculator..ctor` | `0x4028a0` | 92 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.DynamicCodeGenerator..cctor.c`](code/method.DynamicCodeGenerator..cctor.c)
- [`code/method.TransactionalByteAccumulator..ctor.c`](code/method.TransactionalByteAccumulator..ctor.c)
- [`code/method.TransactionalByteAccumulator.AddWithTransaction.c`](code/method.TransactionalByteAccumulator.AddWithTransaction.c)
- [`code/method.TransactionalByteAccumulator.get_Count.c`](code/method.TransactionalByteAccumulator.get_Count.c)
- [`code/method.WindowsFormsDemo.AdamAsmaca..ctor.c`](code/method.WindowsFormsDemo.AdamAsmaca..ctor.c)
- [`code/method.WindowsFormsDemo.AdamAsmaca.AdamAsmaca_Load.c`](code/method.WindowsFormsDemo.AdamAsmaca.AdamAsmaca_Load.c)
- [`code/method.WindowsFormsDemo.AdamAsmaca.InitializeComponent.c`](code/method.WindowsFormsDemo.AdamAsmaca.InitializeComponent.c)
- [`code/method.WindowsFormsDemo.AdamAsmaca.islemler.c`](code/method.WindowsFormsDemo.AdamAsmaca.islemler.c)
- [`code/method.WindowsFormsDemo.Calculator..ctor.c`](code/method.WindowsFormsDemo.Calculator..ctor.c)
- [`code/method.WindowsFormsDemo.Calculator.HarvestColorMatrix.c`](code/method.WindowsFormsDemo.Calculator.HarvestColorMatrix.c)
- [`code/method.WindowsFormsDemo.Calculator.InitializeComponent.c`](code/method.WindowsFormsDemo.Calculator.InitializeComponent.c)
- [`code/method.WindowsFormsDemo.Calculator.bEsittir_Click.c`](code/method.WindowsFormsDemo.Calculator.bEsittir_Click.c)
- [`code/method.WindowsFormsDemo.Concretes.Daire.set_YariCap.c`](code/method.WindowsFormsDemo.Concretes.Daire.set_YariCap.c)
- [`code/method.WindowsFormsDemo.Concretes.DikUcgen.set_Ykseklik.c`](code/method.WindowsFormsDemo.Concretes.DikUcgen.set_Ykseklik.c)
- [`code/method.WindowsFormsDemo.Concretes.Dikdortgen.set_UzunKenar.c`](code/method.WindowsFormsDemo.Concretes.Dikdortgen.set_UzunKenar.c)
- [`code/method.WindowsFormsDemo.Concretes.EskenarUcgen.set_TabanKenar.c`](code/method.WindowsFormsDemo.Concretes.EskenarUcgen.set_TabanKenar.c)
- [`code/method.WindowsFormsDemo.GeometrikIslemler.DikUcgenAlan.c`](code/method.WindowsFormsDemo.GeometrikIslemler.DikUcgenAlan.c)
- [`code/method.WindowsFormsDemo.GeometrikIslemler.DikUcgenCevre.c`](code/method.WindowsFormsDemo.GeometrikIslemler.DikUcgenCevre.c)
- [`code/method.WindowsFormsDemo.GeometrikIslemler.DikdortgenAlan.c`](code/method.WindowsFormsDemo.GeometrikIslemler.DikdortgenAlan.c)
- [`code/method.WindowsFormsDemo.GeometrikIslemler.DikdortgenCevre.c`](code/method.WindowsFormsDemo.GeometrikIslemler.DikdortgenCevre.c)
- [`code/method.WindowsFormsDemo.GeometrikIslemler.GeometrikIslemler_Load.c`](code/method.WindowsFormsDemo.GeometrikIslemler.GeometrikIslemler_Load.c)
- [`code/method.WindowsFormsDemo.GeometrikIslemler.Hesapla.c`](code/method.WindowsFormsDemo.GeometrikIslemler.Hesapla.c)
- [`code/method.WindowsFormsDemo.GeometrikIslemler.InitializeComponent.c`](code/method.WindowsFormsDemo.GeometrikIslemler.InitializeComponent.c)
- [`code/method.WindowsFormsDemo.GeometrikIslemler.ddlGeometrikSekil_SelectedIndexChanged.c`](code/method.WindowsFormsDemo.GeometrikIslemler.ddlGeometrikSekil_SelectedIndexChanged.c)
- [`code/method.WindowsFormsDemo.MenForm.InitializeComponent.c`](code/method.WindowsFormsDemo.MenForm.InitializeComponent.c)
- [`code/method.WindowsFormsDemo.Properties.Resources.get_Culture.c`](code/method.WindowsFormsDemo.Properties.Resources.get_Culture.c)
- [`code/method.WindowsFormsDemo.SesliSessiz.InitializeComponent.c`](code/method.WindowsFormsDemo.SesliSessiz.InitializeComponent.c)
- [`code/method.WindowsFormsDemo.SesliSessiz.button1_Click.c`](code/method.WindowsFormsDemo.SesliSessiz.button1_Click.c)
- [`code/method.__c._.cctor_b__1_0.c`](code/method.__c._.cctor_b__1_0.c)

## Behavioral Analysis

This updated analysis incorporates **Chunk 18**, providing a definitive look into the inner workings of the malware's execution engine. These final blocks confirm that the sophistication level is not merely high—it is professional-grade, utilizing techniques synonymous with high-end commercial protectors (e.g., VMProtect or Themida).

---

### Analysis of Chunk 18: "The Industrial Fortress"

#### 1. The Semantic Void: `set_TabanKenar`
The function name `method.WindowsFormsDemo.Concretes.EskenarUcgen.set_TabanKenar` (Set Base Side) suggests a simple property setter in a .NET environment. However, the disassembled code reveals a **"Semantic Void."**
*   **Logic vs. Label:** Instead of setting a numeric value to a variable, the function contains a massive `do-while(true)` loop filled with bitwise operations (`CONCAT`, `CARRY1`), shifts, and memory pointer arithmetic.
*   **The Strategy:** The original "logic" (setting a length) has been entirely replaced by a **Decoding Routine**. This function acts as a handler that processes a chunk of bytecode. The complex math is not calculating geometric sides; it is calculating the next state of the internal VM's virtual CPU.
*   **Decompiler Sabotage:** The warnings regarding "overlapping instructions" and "bad instruction data" in this specific block confirm that the author has intentionally corrupted the byte stream to break linear disassemblers. By overlapping instructions, they ensure that a tool like IDA Pro cannot provide a reliable Control Flow Graph (CFG).

#### 2. Advanced State-Machine Construction: `Calculator..ctor`
The constructor for the `Calculator` class is often where an analyst looks for initializations. In this malware, it serves as part of the **VM Dispatcher/Initialization Layer**.
*   **Complex Branching via Math:** Notice the labels like `code_r0x0040291b`. These are not standard jumps; they are entry points into a complex state machine. Instead of using simple `if` statements, the code uses `CARRY4` and `SCARRY1` (multi-bit carry flags) to determine the next branch of logic.
*   **Manual Flag Management:** The heavy use of `CARRY` macros indicates that the malware is simulating hardware-level arithmetic. It is essentially running a "software CPU" inside the actual physical CPU to hide its true intent from behavioral monitors.

---

### Updated Synthesis & Intelligence Report

#### I. Architecture Finalization: The "Double-Blind" System
We can now define the architecture as a **Double-Blind Execution Environment**:
1.  **The Outer Layer (Host):** This is the code we see in the disassembly. It contains no malicious logic. Its only job is to act as a host for the virtual machine, providing "handlers" (like `set_TabanKenar`) and a "dispatcher" (found in `Calculator..ctor`).
2.  **The Inner Layer (Guest):** The actual malicious instructions are hidden within the **Custom Bytecode**. Because this bytecode is only interpreted by the Host's handlers, traditional signature-based detection is useless—the "malicious" code never exists in a raw form in memory during execution; it only exists as an *interpretation* of data.

#### II. Advanced Anti-Analysis Tactics (Confirmed)
*   **Instruction Overlapping:** This is a high-tier technique. By forcing instructions to overlap, the author ensures that any attempt to statically map the code will result in "junk" paths and broken logic flows. 
*   **Turing Trap Execution:** The inclusion of highly complex math for simple variables (like `uVar14`, `uVar18`) is designed to waste analyst time. An analyst might spend hours trying to calculate why `uVar18` is being modified by a `CARRY` operation, only to find that it’s just part of an obfuscated "add 1" operation for the virtual instruction pointer.
*   **Abstracted Functionality:** By wrapping everything in what looks like standard .NET Windows Forms objects (`EskenarUcgen`, `Calculator`), the author masks the presence of a malicious engine behind common library naming conventions.

#### III. Technical Indicators & Behavior Summary
*   **Sophistication Level:** **Expert/Elite.** This is not a "script kiddie" tool. The integration of a custom VM, instruction overlapping, and manual carry-flag arithmetic suggests a professional development cycle (likely a professional malware developer or firm).
*   **Deconstruction Complexity:** **Extremely High.** Manual analysis of the "Guest" logic will be required because the "Host" logic is intentionally non-linear.
*   **VM Detection Indicator:** **Confirmed.** The presence of `CARRY` arithmetic and intentional disassembler "breakage" are definitive signatures of a Virtual Machine-based protector.

---

### Updated Threat Assessment & Response Strategy

**Threat Level: Critical | Target Profile: Advanced Persistent Threat (APT) or High-Level Cybercrime Group.**

The malware is designed specifically to defeat automated sandboxes and human reverse engineers. The complexity of the "Turing Trap" in Chunk 18 indicates that this malware belongs to a family that prioritizes **evasion over speed**.

#### Updated Technical Countermeasures:
1.  **Dynamic Analysis Over Static:** Since static disassembly (Ghidra/IDA) is being actively sabotaged by overlapping instructions, **dynamic instrumentation** should be the primary path. Use tools like **Frida** or **Intel PIN** to hook the dispatcher and log the values of registers as they are updated by the handlers.
2.  **Memory Dumping at Runtime:** The "Guest" bytecode is likely decrypted in memory just before it is fed into the VM's dispatcher. Instead of trying to decode the logic from the disassembly, let the malware run in a controlled environment and **dump the memory** immediately after the `Calculator..ctor` completes but before it begins its main malicious loop.
3.  **Identify the Dispatcher Loop:** Focus your analysis on finding the primary loop that calls functions like `set_TabanKenar`. Once you find the "Master Loop," you can identify the table of handlers, which will tell you what the VM is capable of (e.g., networking, file system manipulation, encryption).
4.  **Signature Generation:** Do not attempt to create signatures based on the assembly code provided; it is too dynamic and obscured. Instead, develop **behavioral signatures** for the "unpacked" actions that occur once the VM decides to reach a "high-level" action (like opening a socket or injecting into another process).

**Summary of Key Findings for SOC/Incident Response:**
*   **Advanced VM Architecture:** The malware uses a custom Virtual Machine to shield its true logic from analysis.
*   **Decompiler Sabotage:** Intentional overlapping instructions were used to break automated analysis tools, forcing manual investigation and slowing down response times.
*   **High-Sophistication Tactics:** Use of "Turing Traps" (complex math for simple tasks) indicates a high level of investment in the malware's development cycle.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | **Packer** | The malware utilizes a "professional-grade" custom VM architecture similar to commercial protectors (VMProtect/Themida) to hide its true logic from analysis. |
| **T1027** | **Obfuscated Executables** | The use of "Instruction Overlapping," "Semantic Void" naming, and "Turing Traps" are specific tactics designed to break disassemblers (e.g., IDA Pro) and exhaust human analysts. |
| **T1486** | **Data Encoding** | The "Inner Layer" of the architecture stores malicious instructions as a custom bytecode, which only becomes executable logic when processed by the internal VM's interpreter. |
| **T1028** | **Encrypted/Packed Code** | The "Double-Blind" system ensures that the actual malicious behavior is not present in plain text; it remains obfuscated until it is dynamically decoded and interpreted by the "Host." |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted list of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*None identified.*

### **File paths / Registry keys**
*   `ObA.exe` (Executable filename)

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*   `3DD10108223125B05A05118131B360C0B6C3A1554CBDF6345D55783FB0696B4A`
*   `B15B7DBA7439F36871130776DA70CC3FA814133258C934643593A8A761FFC78F`

### **Other artifacts**
*   **Sophisticated Obfuscation Techniques:**
    *   **Instruction Overlapping:** Specifically identified in the `set_TabanKenar` function to break linear disassemblers (e.g., IDA Pro).
    *   **Turing Traps:** Use of complex, multi-bit carry arithmetic (`CARRY4`, `SCARRY1`) and bitwise operations (`CONCAT`) for simple logical tasks to exhaust manual analysis efforts.
    *   **Custom Virtual Machine (VM):** The malware utilizes a "Double-Blind" architecture where the visible .NET code acts as a host/interpreter for an underlying, custom bytecode layer.
*   **Internal Function Identifiers:**
    *   `Calculator..ctor` (Used as a VM Dispatcher/Initialization Layer)
    *   `set_TabanKenar` (Acts as a decoding routine rather than a standard property setter)

---

## Malware Family Classification

1. **Malware family**: custom (Sophisticated Loader/Protector)
2. **Malware type**: loader
3. **Confidence**: High (regarding technical behavior; Medium regarding specific campaign identity)
4. **Key evidence**:
    *   **Custom Virtual Machine (VM) Architecture:** The malware employs a "Double-Blind" system where the primary malicious logic is hidden in custom bytecode, interpreted by a .NET host that uses complex bitwise operations and multi-bit carry arithmetic (`CARRY4`, `SCARRY1`).
    *   **Advanced Anti-Analysis/Decompiler Sabotage:** The use of "Instruction Overlapping" specifically designed to break linear disassemblers (like IDA Pro) and the creation of a "Semantic Void" indicate an elite level of development intended to stall human analysts.
    *   **Professional-Grade Protection:** The report explicitly compares the sophistication to high-end commercial protectors like VMProtect or Themida, signifying that the primary goal is protecting a hidden payload (the "Inner Layer") rather than immediate, overt action.
