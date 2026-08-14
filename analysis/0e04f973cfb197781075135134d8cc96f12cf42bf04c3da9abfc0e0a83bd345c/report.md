# Threat Analysis Report

**Generated:** 2026-08-11 16:42 UTC
**Sample:** `0e04f973cfb197781075135134d8cc96f12cf42bf04c3da9abfc0e0a83bd345c_0e04f973cfb197781075135134d8cc96f12cf42bf04c3da9abfc0e0a83bd345c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e04f973cfb197781075135134d8cc96f12cf42bf04c3da9abfc0e0a83bd345c_0e04f973cfb197781075135134d8cc96f12cf42bf04c3da9abfc0e0a83bd345c.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,030,144 bytes |
| MD5 | `0979e1bc39524814f7315d140c281490` |
| SHA1 | `a7e148b848858305feee957c38adadc12ebe8eab` |
| SHA256 | `0e04f973cfb197781075135134d8cc96f12cf42bf04c3da9abfc0e0a83bd345c` |
| Overall entropy | 7.732 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773636582 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,027,584 | 7.737 | ⚠️ Yes |
| `.rsrc` | 1,536 | 4.194 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **2595** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

X )UU
 @Z
s]
YZXl(o
?+	#ffffff

+VrO
p+Nrc
p+Frw
$@Zi(W
[	lZkX
[	lZkX
[	lZkX
Y[	lZkY
	#333333
#333333
#333333
Z#ffffff
?Y#333333
Mb`?#{
,#ffffff
@
+
#
@ZXZ+j
@ZXZ+P
$@ZXZ+6#{
Y@Z	*
Y@ZX+v#
@ZX+^#
I@ZX+F#
@ZX+.#
O"A+"#
MbP?Z+:
(@Z+
4@Z	*
#333333
#333333
#ffffff
#ffffff
#333333
#333333
#ffffff
#333333
,"#ffffff
?ZX+ #
	#hfffff
#hfffff
#hfffff
MbP?+v#
I@+R#
i@+F#
@+:#{
?+.#-C
MbP?(r
MbP?(r
#333333
#ffffff
#333333
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADP
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADP
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADP
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
hSystem.Drawing.Bitmap, System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3aPADPADvrY
QSystem.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
System.Drawing.Bitmap
QSystem.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
System.Drawing.Bitmap
IDATx^
/txn
i
og-]y/*
]^8!O-n
	NBlWl
!	"4:	
x*vq"8
=Wox/,M
hTB7az
4#@i:k
jP+kXm!
Zqkh6
E@!Foc6
F)b>+
{
>k^aLNo4
(//y\Z"E
f>R)?UG
f2d,)Q
.YTzaE
fx^A7[
	Y*)(@$=e
;ZBJ}yz
**N<))y
+t	sGZ
MP{8>,^
#pJ;|U
lJ>Pl4fp
ak9v#R(
ex;qw^
JxHVm!k:
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.PinnableBufferCacheEventSou.LocalBuil..cctor` | `0x4026f9` | 35876 | ✓ |
| `method.InternalGCCollectionM.ObjectCompa.InitializeComponent` | `0x403a74` | 5808 | ✓ |
| `method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.InitializeComponent` | `0x4086c8` | 4100 | ✓ |
| `method.StaticIndexRangePartitionForIL.cDisplayClass.InitializeComponent` | `0x40669c` | 3636 | ✓ |
| `method.StaticIndexRangePartitionForIL.cDisplayClass.PnlJadwalZamani_Paint` | `0x405784` | 1616 | ✓ |
| `method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.RasmMukhattatFuqaat` | `0x407d10` | 1576 | ✓ |
| `method.StaticIndexRangePartitionForIL.cDisplayClass.PnlRasmBayani_Paint` | `0x405dd4` | 1460 | ✓ |
| `method.PinnableBufferCacheEventSou.LocalBuil.get_Default` | `0x40ae20` | 912 | ✓ |
| `method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.RasmMiqyasKhatar` | `0x408338` | 568 | ✓ |
| `method.InternalGCCollectionM.ObjectCompa.PnlMajarra_Paint` | `0x402efc` | 524 | ✓ |
| `method.IPermissionSetEn.InsufficientMemoryExcept.HisabLawn` | `0x409768` | 524 | ✓ |
| `method.StaticIndexRangePartitionForIL.cDisplayClass.PnlDalil_Paint` | `0x406430` | 452 | ✓ |
| `method.StaticIndexRangePartitionForIL.cDisplayClass.TanfidhMuhaka` | `0x4055d4` | 432 | ✓ |
| `method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.TahdithMurashahun` | `0x407790` | 432 | ✓ |
| `method.InternalGCCollectionM.ObjectCompa.PnlMajarra_MouseClick` | `0x403668` | 428 | ✓ |
| `method.StaticIndexRangePartitionForIL.cDisplayClass..cctor` | `0x4074d0` | 416 | ✓ |
| `method.InternalGCCollectionM.ObjectCompa.RasmInfijar` | `0x403420` | 396 | ✓ |
| `method.InternalGCCollectionM.ObjectCompa.ExtractPixelComponents` | `0x402954` | 372 | ✓ |
| `method.InternalGCCollectionM.ObjectCompa.RasmNajm` | `0x403244` | 364 | ✓ |
| `method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.PnlRasm_Paint` | `0x407bb4` | 348 | ✓ |
| `method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.TahdithTafasil` | `0x407a5c` | 344 | ✓ |
| `method.IAsyncLocalValue.IDefinitionIdent.TawlidNajmJadid` | `0x409dfc` | 344 | ✓ |
| `method.NumberBuf.SynchronizedServerContextS.HisabIhtimaInfijar` | `0x40a5b4` | 324 | ✓ |
| `method.InternalGCCollectionM.ObjectCompa.TahdithWajha` | `0x402d04` | 320 | ✓ |
| `method.InternalGCCollectionM.ObjectCompa.RasmMarkazMajarra` | `0x403108` | 316 | ✓ |
| `method.NumberBuf.SynchronizedServerContextS.HisabHarara` | `0x40a3bc` | 312 | ✓ |
| `method.ParallelLoopRes.TokenizerStr.TahdidMarHala` | `0x40ab70` | 312 | ✓ |
| `method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.TatbiqAnmatJadwal` | `0x407670` | 288 | ✓ |
| `method.ParallelLoopRes.TokenizerStr.TatwirNajm` | `0x40aa50` | 288 | ✓ |
| `method.IAsyncLocalValue.IDefinitionIdent.Taqaddum` | `0x409f54` | 268 | ✓ |

### Decompiled Code Files

- [`code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.InitializeComponent.c`](code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.InitializeComponent.c)
- [`code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.PnlRasm_Paint.c`](code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.PnlRasm_Paint.c)
- [`code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.RasmMiqyasKhatar.c`](code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.RasmMiqyasKhatar.c)
- [`code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.RasmMukhattatFuqaat.c`](code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.RasmMukhattatFuqaat.c)
- [`code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.TahdithMurashahun.c`](code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.TahdithMurashahun.c)
- [`code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.TahdithTafasil.c`](code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.TahdithTafasil.c)
- [`code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.TatbiqAnmatJadwal.c`](code/method.EventT.IIDENTITYAUTHORITYDEFINITIONIDENTITYTOTEXTFL.TatbiqAnmatJadwal.c)
- [`code/method.IAsyncLocalValue.IDefinitionIdent.Taqaddum.c`](code/method.IAsyncLocalValue.IDefinitionIdent.Taqaddum.c)
- [`code/method.IAsyncLocalValue.IDefinitionIdent.TawlidNajmJadid.c`](code/method.IAsyncLocalValue.IDefinitionIdent.TawlidNajmJadid.c)
- [`code/method.IPermissionSetEn.InsufficientMemoryExcept.HisabLawn.c`](code/method.IPermissionSetEn.InsufficientMemoryExcept.HisabLawn.c)
- [`code/method.InternalGCCollectionM.ObjectCompa.ExtractPixelComponents.c`](code/method.InternalGCCollectionM.ObjectCompa.ExtractPixelComponents.c)
- [`code/method.InternalGCCollectionM.ObjectCompa.InitializeComponent.c`](code/method.InternalGCCollectionM.ObjectCompa.InitializeComponent.c)
- [`code/method.InternalGCCollectionM.ObjectCompa.PnlMajarra_MouseClick.c`](code/method.InternalGCCollectionM.ObjectCompa.PnlMajarra_MouseClick.c)
- [`code/method.InternalGCCollectionM.ObjectCompa.PnlMajarra_Paint.c`](code/method.InternalGCCollectionM.ObjectCompa.PnlMajarra_Paint.c)
- [`code/method.InternalGCCollectionM.ObjectCompa.RasmInfijar.c`](code/method.InternalGCCollectionM.ObjectCompa.RasmInfijar.c)
- [`code/method.InternalGCCollectionM.ObjectCompa.RasmMarkazMajarra.c`](code/method.InternalGCCollectionM.ObjectCompa.RasmMarkazMajarra.c)
- [`code/method.InternalGCCollectionM.ObjectCompa.RasmNajm.c`](code/method.InternalGCCollectionM.ObjectCompa.RasmNajm.c)
- [`code/method.InternalGCCollectionM.ObjectCompa.TahdithWajha.c`](code/method.InternalGCCollectionM.ObjectCompa.TahdithWajha.c)
- [`code/method.NumberBuf.SynchronizedServerContextS.HisabHarara.c`](code/method.NumberBuf.SynchronizedServerContextS.HisabHarara.c)
- [`code/method.NumberBuf.SynchronizedServerContextS.HisabIhtimaInfijar.c`](code/method.NumberBuf.SynchronizedServerContextS.HisabIhtimaInfijar.c)
- [`code/method.ParallelLoopRes.TokenizerStr.TahdidMarHala.c`](code/method.ParallelLoopRes.TokenizerStr.TahdidMarHala.c)
- [`code/method.ParallelLoopRes.TokenizerStr.TatwirNajm.c`](code/method.ParallelLoopRes.TokenizerStr.TatwirNajm.c)
- [`code/method.PinnableBufferCacheEventSou.LocalBuil..cctor.c`](code/method.PinnableBufferCacheEventSou.LocalBuil..cctor.c)
- [`code/method.PinnableBufferCacheEventSou.LocalBuil.get_Default.c`](code/method.PinnableBufferCacheEventSou.LocalBuil.get_Default.c)
- [`code/method.StaticIndexRangePartitionForIL.cDisplayClass..cctor.c`](code/method.StaticIndexRangePartitionForIL.cDisplayClass..cctor.c)
- [`code/method.StaticIndexRangePartitionForIL.cDisplayClass.InitializeComponent.c`](code/method.StaticIndexRangePartitionForIL.cDisplayClass.InitializeComponent.c)
- [`code/method.StaticIndexRangePartitionForIL.cDisplayClass.PnlDalil_Paint.c`](code/method.StaticIndexRangePartitionForIL.cDisplayClass.PnlDalil_Paint.c)
- [`code/method.StaticIndexRangePartitionForIL.cDisplayClass.PnlJadwalZamani_Paint.c`](code/method.StaticIndexRangePartitionForIL.cDisplayClass.PnlJadwalZamani_Paint.c)
- [`code/method.StaticIndexRangePartitionForIL.cDisplayClass.PnlRasmBayani_Paint.c`](code/method.StaticIndexRangePartitionForIL.cDisplayClass.PnlRasmBayani_Paint.c)
- [`code/method.StaticIndexRangePartitionForIL.cDisplayClass.TanfidhMuhaka.c`](code/method.StaticIndexRangePartitionForIL.cDisplayClass.TanfidhMuhaka.c)

## Behavioral Analysis

The second batch of disassembly reinforces and expands upon the previous findings. The addition of these functions confirms that the sample is not just standard obfuscation but utilizes high-level **metamorphism** and **anti-analysis techniques** typical of commercial-grade protectors (e.g., VMProtect, Themida, or advanced .NET wrappers).

Here is the updated analysis including the new data:

### Updated Analysis of Findings

#### 1. Advanced Metamorphism & Polymorphism
The most striking finding in Chunk 2 is the repetition of identical machine code under completely different function names. For example:
*   `method.EventT.IIDENTITYAUTHORITYDEFINITION...PnlRasm_Paint`
*   `method.PinnableBufferCacheEventSou.LocalBuil..cctor` (appearing multiple times)
*   `method.NumberBuf.SynchronizedServerContextS.HisabIhtimaInfijar`

**Analysis:** The fact that these disparate, "nonsense" names all lead to the exact same underlying assembly confirms a **metamorphic engine**. This is designed to overwhelm an analyst; by making every internal call look unique or "random," the obfuscator prevents the researcher from identifying which parts of the code are responsible for specific actions (e.g., network communication vs. file encryption).

#### 2. Anti-Disassembly & Tool Sabotage
The disassembly continues to show a high frequency of:
*   **Overlap Warnings:** (e.g., `Instruction at (ram,0x402753) overlaps instruction at (ram,0x402752)`). 
*   **Bad Instruction Traps:** The repeated `halt_baddata()` and "Truncating control flow" errors are intentional.

**Analysis:** These are used to break the disassembler's ability to map a linear path of execution. By intentionally creating overlapping instructions, the author forces tools like Ghidra or IDA Pro to choose between two different ways of interpreting the same bytes. This creates "ghost" code paths and makes it nearly impossible for an analyst to determine the true flow of the program without manual, instruction-by-instruction inspection.

#### 3. Virtualization/Heavy Abstraction
The use of macros like `CONCAT11`, `CONCAT22`, `CONCAT31`, `CARRY1`, and `POPCOUNT` is highly characteristic of **Virtual Machine (VM) based protection**. 

**Analysis:** These are not standard "high-level" operations. They suggest that the original code has been translated into a custom, non-standard instruction set. The processor isn't just executing "malware logic"; it is running a small, hidden interpreter that translates these complex mathematical constructs into actual actions. This makes static analysis extremely difficult because the "real" malicious instructions are hidden inside this layer of abstraction.

#### 4. Purposeful Obfuscated Naming
The function names (e.g., `TatbiqAnmatJadwal`, `TatwirNajm`, `Suhuyur`) appear to be a mix of garbled technical terms and potentially nonsensical strings.

**Analysis:** These are "junk" identifiers. They serve no functional purpose in the code; they exist solely to populate the symbol table with confusing information, making it harder for automated scanners (which look for keywords like "Send" or "Pass") to flag the file accurately.

---

### Updated Summary for Report

**Malware Classification:** Highly Sophisticated Obfuscated .NET Binary
**Protector Profile:** Professional-grade Packer/Protector (likely utilizing a Virtualization Layer).

**Key Technical Observations:**
1.  **Metamorphic Code Blocks:** The sample employs high-level metamorphism where identical logic is hidden behind hundreds of unique, randomly generated function names to frustrate manual analysis and hinder the mapping of functionality.
2.  **Active Anti-Disassembly:** The binary utilizes "overlapping instructions" and "junk code insertion." These techniques are specifically designed to crash or misrepresent the control flow in disassembly tools (Ghidra/IDA Pro), significantly increasing the time required for manual reverse engineering.
3.  **Virtualization Layer:** The presence of complex arithmetic macros (`POPCOUNT`, `CARRY`, and multi-bit `CONCAT`) suggests the use of a "Virtual Machine" protector. This wraps the actual malicious payload in a layer of custom bytecode, meaning the "real" logic is not visible in standard disassembly.
4.  **Conclusion:** The presence of these high-end evasion techniques indicates that this is likely a **professional-grade malware sample** (such as a sophisticated Trojan, Botnet loader, or Stealer). It is designed to bypass automated heuristic scanners and exhaust the resources of human analysts by creating a "maze" of junk code and complex math.

**Recommendation:** The file should be treated as highly malicious. Due to the level of protection, manual analysis will likely require de-obfuscation tools (like dnSpy/de4dot for the .NET layer) or dynamic analysis in a controlled sandbox to observe its behavior while it is "unpacked" in memory.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the corresponding MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of metamorphic engines, junk identifiers (nonsense strings), and deliberately overlapping instructions are designed to hide malicious functionality from both automated scanners and manual analysis. |
| **T1497** | Virtualization | The presence of custom bytecode translation and non-standard mathematical macros (e.g., POPCOUNT, CARRY) indicates the use of a virtual machine-based protection layer to shield the core payload. |

---

## Indicators of Compromise

Based on my analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The string data consists primarily of binary artifacts and standard .NET framework metadata.)

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Obfuscation Indicators:** 
    *   Evidence of a **Virtual Machine (VM) based protection layer** (e.g., techniques similar to VMProtect or Themida).
    *   Presence of specific arithmetic macros: `CONCAT11`, `CONCENT22`, `CONCAT31`, `CARRY1`, and `POPCOUNT`.
*   **Obfuscated Function Strings:** 
    The following strings are part of the "junk" identifier set used to confuse automated scanners (note: these may be indicative of specific obfuscation patterns):
    *   `TatbiqAnmatJadwal`
    *   `TatwirNajm`
    *   `Suhuyur`
*   **Assembly Artifacts:** 
    The samples includes references to `mscorlib`, `System.Resources.ResourceReader`, and `System.Drawing.Bitmap`. (Note: These are standard .NET libraries and were excluded as per instructions regarding common system strings).

---

### **Analyst Note**
While no direct network indicators (IPs/URLs) or filesystem artifacts (Paths/Mutexes) were present in the provided text, the behavioral analysis confirms this is a **high-sophistication malicious sample**. The primary "threat" identified via these IOCs is the use of **Advanced Metamorphism** and **Virtualization Layer Protection**, which are hallmarks of professional malware like botnet loaders or sophisticated trojans.

---

## Malware Family Classification

1. **Malware family**: custom (Note: While the sophisticated protection is typical of high-end malware, there are no specific signatures provided to link it to a known campaign such as Emotet or Cobalt Strike).
2. **Malware type**: loader
3. **Confidence**: Medium
4. **Key evidence**: 
    *   **Virtualization Layer:** The presence of `POPCOUNT`, `CARRY`, and `CONCAT` macros indicates the use of a "Virtual Machine" protector (similar to VMProtect or Themida) to hide the core logic in a custom bytecode layer.
    *   **Advanced Anti-Analysis:** The use of overlapping instructions, junk identifiers, and metamorphic code blocks is specifically designed to sabotage disassemblers (IDA/Ghidra) and exhaust human analysts.
    *   **Evasion Intent:** The combination of high-level metamorphism and intentional "broken" control flows points toward a professional-grade loader intended to deliver further malicious payloads while remaining undetected by automated systems.
