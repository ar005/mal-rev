# Threat Analysis Report

**Generated:** 2026-07-15 06:08 UTC
**Sample:** `06840a4bac62abfd410be15bd45ae47a9516682515baa9c981058428815c5fe7_06840a4bac62abfd410be15bd45ae47a9516682515baa9c981058428815c5fe7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `06840a4bac62abfd410be15bd45ae47a9516682515baa9c981058428815c5fe7_06840a4bac62abfd410be15bd45ae47a9516682515baa9c981058428815c5fe7.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,046,016 bytes |
| MD5 | `29add908fa403a89387ab9636e41b012` |
| SHA1 | `d8eb52d0702715bd69f5e028441bec638a55275d` |
| SHA256 | `06840a4bac62abfd410be15bd45ae47a9516682515baa9c981058428815c5fe7` |
| Overall entropy | 7.893 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779161996 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,026,048 | 7.896 | ⚠️ Yes |
| `.rsrc` | 18,944 | 7.823 | ⚠️ Yes |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **2685** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
AjZ 90
?_b`U8
?_b`U8
@mR Z?
W;Y kHp
 'T.af 
f |A6oa 
P]CXf I
ef dY;
 'T.af 
 'T.af 
 'T.af 
 'T.af (
 v(Ap 
@mR Z?
v4.0.30319
#Strings
CompilationRelaxationsAttribute
System.Runtime.CompilerServices
mscorlib
System
Boolean
RuntimeCompatibilityAttribute
DebuggableAttribute
System.Diagnostics
DebuggingModes
ComVisibleAttribute
System.Runtime.InteropServices
GuidAttribute
String
AssemblyFileVersionAttribute
System.Reflection
TargetFrameworkAttribute
System.Runtime.Versioning
SuppressIldasmAttribute
9cc4e7bb-2653-4127-ac3f-3a222fb53e08
udEl.exe
<Module>
Object
<>c__DisplayClass0_0
<>c__DisplayClass3_0
<>c__DisplayClass4_0
<>c__DisplayClass4_1
Resources
PharmacyApp.Properties
System.Windows.Forms
<>c__DisplayClass16_0
<>c__DisplayClass16_1
<PrivateImplementationDetails>
ValueType
<Module>{A98004DC-8E4D-4B05-A3EB-DA913A7C90B9}
MulticastDelegate
<PrivateImplementationDetails>{E2843A1D-A9B5-45A7-B01F-C9D84CAA79B4}
<Module>{68347fae-2d6a-4ccc-9ced-3d10548d74e6}
m8DEB57173BD9E6D
.cctor
Func`1
Application
EnableVisualStyles
AppDomain
get_CurrentDomain
get_BaseDirectory
System.IO
Combine
SetCompatibleTextRenderingDefault
IntPtr
EventHandler
EventArgs
Invoke
IsNullOrWhiteSpace
DateTime
get_Today
List`1
System.Collections.Generic
Func`2
Enumerable
System.Linq
System.Core
FirstOrDefault
IEnumerable`1
IsNullOrEmpty
ToList
Select
op_Equality
AddDays
Double
op_LessThanOrEqual
DataSet
System.Data
Exists
ReadXml
XmlReadMode
DataTable
get_Columns
DataColumnCollection
GetTypeFromHandle
RuntimeTypeHandle
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method._Module_68347fae_2d6a_4ccc_9ced_3d10548d74e6.xNa` | `0x407b54` | 32484 | ✓ |
| `method._Module_68347fae_2d6a_4ccc_9ced_3d10548d74e6.gc75f6e61e90f4e3888c5eb96fc03708d` | `0x406a40` | 4360 | ✓ |
| `method.I3P.F31.w3v` | `0x403e4c` | 1964 | ✓ |
| `method.gFn.JFw.EFM` | `0x404afc` | 1148 | ✓ |
| `method.MF2.FF5.jFA` | `0x405260` | 1036 | ✓ |
| `method.I3P.F31.c3O` | `0x403b0c` | 832 | ✓ |
| `method.dI.vL.ld` | `0x402bd4` | 684 | ✓ |
| `method.U1.Qq.FY` | `0x402724` | 612 | ✓ |
| `method.qFY.sF1.MFP` | `0x4058ec` | 516 | ✓ |
| `method.nFB.LFr.iFL` | `0x405bcc` | 440 | ✓ |
| `method.dI.vL.DKM` | `0x4032cc` | 360 | ✓ |
| `method.Bh.Sa.P7` | `0x402518` | 340 | ✓ |
| `method.Ti.pk.UJ` | `0x402328` | 336 | ✓ |
| `method.__c__DisplayClass16_1.Gm5` | `0x40676c` | 328 | ✓ |
| `method.dI.vL.kKw` | `0x403198` | 308 | ✓ |
| `method.__c__DisplayClass16_0.Tmn` | `0x406410` | 292 | ✓ |
| `method.dI.vL.lKQ` | `0x402e80` | 288 | ✓ |
| `entry0` | `0x40205c` | 280 | ✓ |
| `method.dI.vL.aKR` | `0x402fa0` | 280 | ✓ |
| `method.__c__DisplayClass16_0.jmM` | `0x406534` | 244 | ✓ |
| `method.dI.vL.xKC` | `0x4030b8` | 224 | ✓ |
| `method.jm7.umh.yNh` | `0x4068c8` | 216 | ✓ |
| `method.__c.CmG` | `0x406234` | 208 | ✓ |
| `method.I3P.F31.ShowView` | `0x404680` | 204 | ✓ |
| `method.dI.vL..ctor` | `0x402b0c` | 200 | ✓ |
| `method.__c.jmV` | `0x406304` | 192 | ✓ |
| `method.bf.OE..ctor` | `0x402a3c` | 188 | ✓ |
| `method.__c__DisplayClass4_0.smK` | `0x40604c` | 180 | ✓ |
| `method.gQ.pp..ctor` | `0x402188` | 160 | ✓ |
| `method.U1.Qq.GP` | `0x402988` | 160 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Bh.Sa.P7.c`](code/method.Bh.Sa.P7.c)
- [`code/method.I3P.F31.ShowView.c`](code/method.I3P.F31.ShowView.c)
- [`code/method.I3P.F31.c3O.c`](code/method.I3P.F31.c3O.c)
- [`code/method.I3P.F31.w3v.c`](code/method.I3P.F31.w3v.c)
- [`code/method.MF2.FF5.jFA.c`](code/method.MF2.FF5.jFA.c)
- [`code/method.Ti.pk.UJ.c`](code/method.Ti.pk.UJ.c)
- [`code/method.U1.Qq.FY.c`](code/method.U1.Qq.FY.c)
- [`code/method.U1.Qq.GP.c`](code/method.U1.Qq.GP.c)
- [`code/method._Module_68347fae_2d6a_4ccc_9ced_3d10548d74e6.gc75f6e61e90f4e3888c5eb96fc03708d.c`](code/method._Module_68347fae_2d6a_4ccc_9ced_3d10548d74e6.gc75f6e61e90f4e3888c5eb96fc03708d.c)
- [`code/method._Module_68347fae_2d6a_4ccc_9ced_3d10548d74e6.xNa.c`](code/method._Module_68347fae_2d6a_4ccc_9ced_3d10548d74e6.xNa.c)
- [`code/method.__c.CmG.c`](code/method.__c.CmG.c)
- [`code/method.__c.jmV.c`](code/method.__c.jmV.c)
- [`code/method.__c__DisplayClass16_0.Tmn.c`](code/method.__c__DisplayClass16_0.Tmn.c)
- [`code/method.__c__DisplayClass16_0.jmM.c`](code/method.__c__DisplayClass16_0.jmM.c)
- [`code/method.__c__DisplayClass16_1.Gm5.c`](code/method.__c__DisplayClass16_1.Gm5.c)
- [`code/method.__c__DisplayClass4_0.smK.c`](code/method.__c__DisplayClass4_0.smK.c)
- [`code/method.bf.OE..ctor.c`](code/method.bf.OE..ctor.c)
- [`code/method.dI.vL..ctor.c`](code/method.dI.vL..ctor.c)
- [`code/method.dI.vL.DKM.c`](code/method.dI.vL.DKM.c)
- [`code/method.dI.vL.aKR.c`](code/method.dI.vL.aKR.c)
- [`code/method.dI.vL.kKw.c`](code/method.dI.vL.kKw.c)
- [`code/method.dI.vL.lKQ.c`](code/method.dI.vL.lKQ.c)
- [`code/method.dI.vL.ld.c`](code/method.dI.vL.ld.c)
- [`code/method.dI.vL.xKC.c`](code/method.dI.vL.xKC.c)
- [`code/method.gFn.JFw.EFM.c`](code/method.gFn.JFw.EFM.c)
- [`code/method.gQ.pp..ctor.c`](code/method.gQ.pp..ctor.c)
- [`code/method.jm7.umh.yNh.c`](code/method.jm7.umh.yNh.c)
- [`code/method.nFB.LFr.iFL.c`](code/method.nFB.LFr.iFL.c)
- [`code/method.qFY.sF1.MFP.c`](code/method.qFY.sF1.MFP.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis. The new data reinforces the initial findings while providing more specific evidence regarding the nature of the protection layer used.

### Updated Analysis Report

#### 1. Core Functionality and Context
The presence of pharmacy-related strings (`PharmacyApp`, `Amoxicillin`) remains the primary indicator of the original application's intent. However, as established in the first analysis, the **core logic is no longer directly accessible** to human or automated analysis due to a heavy transformation layer.

#### 2. Advanced Protection Techniques (New Observations)
The second chunk provides clear evidence of a **Virtual Machine (VM) based protection system** (such as VMProtect or a custom equivalent). The following techniques are specifically visible:

*   **Instruction Virtualization:** Functions such as `method.dI.vL.aKR`, `method.dI.vL.xKC`, and `method.I3P.F31.ShowView` appear to be **VM Handlers**. In a VM-protected binary, the original code is translated into a custom bytecode; these functions are then responsible for interpreting that bytecode. The complexity of the math (e.g., `CONCAT31`, `CARRY4` checks) suggests they are handling state transitions and memory access within a virtualized environment.
*   **Data Obfuscation/Packing:** The frequent use of `CONCAT` macros (e.g., `CONCAT22`, `CONCAT31`) indicates that data structures—potentially the pharmacy database or internal variables—are "packed" into single, complex memory addresses. This prevents researchers from using standard tools to find and extract plain-text values or logic paths.
*   **Aggressive Anti-Analysis (De-compilation/Disassembly):** 
    *   **Overlap Errors:** The repeated warnings about "overlapping instructions" (e.g., `0x403072` vs `0x403071`) are a signature of **instruction overlapping**. This is designed to confuse disassemblers by creating ambiguous code paths that are difficult for tools like IDA or Ghidra to resolve correctly.
    *   **Dead-End/Trap Code:** The recurring `halt_baddata()` calls indicate "junk code" insertions. These are used to steer the analyst’s focus toward invalid memory regions or non-executable code, effectively creating a maze that hides the true execution path of the program.
*   **Obfuscated .NET Wrapper:** The presence of `.ctor` (constructor) signatures in names like `method.gQ.pp..ctor` and `method.bf.OE..ctor` confirms this is likely a **.NET assembly** that has been processed by a high-end native protector. The packer "wraps" the .NET logic inside a proprietary, virtually executed shell.

#### 3. Structural Analysis of Code Bloat
The second chunk highlights significant **Code Bloat**. For example, in `method.dI.vL.aKR`, we see nearly 100 lines of assembly translated into what is likely only a few high-level instructions (e.g., a simple variable assignment or an "if" check). This expansion is a hallmark of **Metamorphic/Polymorphic** obfuscation, where the goal is to make the code volume so large that manual auditing becomes economically and practically impossible for an analyst.

#### 4. Summary of Technical Indicators
| Feature | Observed Pattern | Interpretation |
| :--- | :--- | :--- |
| **VM-Handler Logic** | `method.dI...`, `method.xKC` | Presence of a custom Virtual Machine to hide code logic. |
| **Instruction Overlaps** | `0x403072` overlaps `0x403071` | Intentional "traps" for disassemblers/static analysis tools. |
| **Data Packing** | Frequent `CONCAT` and bitwise shifts | Obfuscation of variables to prevent discovery of logic flow. |
| **Junk Code** | `halt_baddata()` calls | Creation of dead-ends to hinder human reverse engineers. |
| **Hybrid Engine** | `.ctor` inside complex wrappers | A .NET application protected by a professional grade packer. |

### Updated Conclusion for Analysis Report
The sample utilizes an **advanced, multi-layered protection scheme**. While the high-level "Pharmacy" functionality is present in the metadata/strings, it is effectively "hidden" behind a proprietary Virtual Machine. 

The code's primary purpose currently appears to be **intentional obfuscation of intent.** Because the real logic (potential data exfiltration, backdoor commands, or malicious behavior) resides within the virtualized layer, it cannot be confirmed through static analysis alone. The presence of professional-grade protection techniques such as instruction overlapping and junk-code insertion suggests a high level of sophistication, common in both **sophisticated malware** and **highly protected commercial software.**

**Recommendation:** Due to the complexity of the VM layer, dynamic analysis (monitoring network traffic and file system changes while the "VM" is running) would be required to determine if the application performs malicious actions.

---

## MITRE ATT&CK Mapping

Based on the behavior analysis provided, here is the mapping of observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Obfuscated Files or Packers | The use of a Virtual Machine (VM) protection system and Instruction Virtualization hides the original code logic behind a proprietary bytecode translation layer. |
| **T1029** | Obfuscated Files or Packers (Data Masking) | The frequent use of `CONCAT` macros and bitwise shifts masks data structures to prevent researchers from extracting plain-text values. |
| **T1029** | Obfuscated Files or Packers (Junk Code) | The insertion of "dead-end" code and `halt_baddata()` calls is used to create a maze that hides the true execution path from human analysts. |
| **T1029** | Obfuscated Files or Packers (Instruction Overlap) | Intentional instruction overlapping is utilized to create ambiguous paths, specifically designed to confuse disassembler tools like IDA or Ghidra. |
| **T1027** | Encrypt/Pack_Execute | The use of an "Obfuscated .NET Wrapper" indicates the original logic is packed inside a protection shell to hinder static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `udEl.exe` (Executable filename)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *No standard MD5, SHA-1, or SHA-256 file hashes were present in the strings.*

**Other artifacts**
*   **Internal Identifiers/GUIDs:** 
    *   `9cc4e7bb-2653-4127-ac3f-3a222fb53e08`
    *   `A98004DC-8E4D-4B05-A3EB-DA913A7C90B9`
    *   `E2843A1D-A9B5-45A7-B01F-C9D84CAA79B4`
    *   `68347fae-2d6a-4ccc-9ced-3d10548d74e6`
*   **VM Handler Method Names (Obfuscation Layer):** 
    *   `method.dI.vL.aKR`
    *   `method.dI.vL.xKC`
    *   `method.I3P.F31.ShowView`
*   **Anti-Analysis/Junk Code Indicators:**
    *   `halt_baddata()` (Function call used to trap disassemblers)
*   **Overlay Signature Offsets:**
    *   `0x403072` / `0x403071` (Identified as overlapping instruction points for anti-analysis)

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: Medium

4. **Key evidence**:
*   **Advanced Obfuscation Layer:** The use of a Virtual Machine (VM) based protection system, including instruction virtualization and `.NET` wrapping, is a hallmark of sophisticated loaders designed to hide the execution path from automated sandboxes and static analysis tools.
*   **Anti-Analysis Techniques:** The presence of "instruction overlapping," junk code (`halt_baddata()` calls), and complex `CONCAT` macro data packing indicates a deliberate attempt to hinder manual reverse engineering and frustrate disassemblers like IDA or Ghidra.
*   **Deceptive Front (Masquerading):** The discrepancy between the plain-text "Pharmacy" strings and the high-level, professional-grade protection techniques suggests the file is intended to serve as a delivery vehicle (loader) for secondary malicious payloads while hiding its true intent from researchers.
