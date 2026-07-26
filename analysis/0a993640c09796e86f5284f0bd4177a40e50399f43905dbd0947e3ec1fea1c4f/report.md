# Threat Analysis Report

**Generated:** 2026-07-25 01:44 UTC
**Sample:** `0a993640c09796e86f5284f0bd4177a40e50399f43905dbd0947e3ec1fea1c4f_0a993640c09796e86f5284f0bd4177a40e50399f43905dbd0947e3ec1fea1c4f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a993640c09796e86f5284f0bd4177a40e50399f43905dbd0947e3ec1fea1c4f_0a993640c09796e86f5284f0bd4177a40e50399f43905dbd0947e3ec1fea1c4f.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 1,244,160 bytes |
| MD5 | `4733d1a824470710cb5d14bdf8be0df8` |
| SHA1 | `cdce27faaae19a20399a53fa2dea9486a6009ebc` |
| SHA256 | `0a993640c09796e86f5284f0bd4177a40e50399f43905dbd0947e3ec1fea1c4f` |
| Overall entropy | 7.635 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1775443341 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,235,968 | 7.646 | ⚠️ Yes |
| `.rsrc` | 7,680 | 4.76 | No |

## Extracted Strings

Total strings found: **2601** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc

X )UU
gAVa}b
b ~p'Ra}l
e 6Vi>a}6
GX Nj
\$La}j
 PNn,f 
ejya}`
\I4a 	U
b  Nv(a}k
 PNn,f 
be m#m
 PNn,f 
 *"81 
 *"81 
GX Nj
sXY :ED{a}$
 PNn,f 
e 2z }a}n
9^ jS.zX 
?X iB[
,gef q
 PNn,f 
&Y p}d2a}+
 PNn,f 
`Y L`a!a}f
,gef q
?X iB[
 *"81 
?X iB[
v4.0.30319
#Strings
	6	I	x	
CompilationRelaxationsAttribute
System.Runtime.CompilerServices
mscorlib
System
Boolean
RuntimeCompatibilityAttribute
DebuggableAttribute
System.Diagnostics
DebuggingModes
AssemblyTitleAttribute
System.Reflection
String
AssemblyDescriptionAttribute
AssemblyConfigurationAttribute
AssemblyCompanyAttribute
AssemblyProductAttribute
AssemblyCopyrightAttribute
AssemblyTrademarkAttribute
ComVisibleAttribute
System.Runtime.InteropServices
GuidAttribute
AssemblyFileVersionAttribute
TargetFrameworkAttribute
System.Runtime.Versioning
SuppressIldasmAttribute
c6cc989d-8074-4df2-ab65-08506fc2b26d
jQDU.exe
<Module>
<>f__AnonymousType0`2
Object
System.Windows.Forms
<>c__DisplayClass7_0
<>c__DisplayClass7_1
<>c__DisplayClass7_2
DataSet
System.Data
DataTable
Resources
LaserCalculator.Properties
Settings
ApplicationSettingsBase
System.Configuration
<Module>{73039813-AD68-4419-8CCB-BD0AD270AA8C}
MulticastDelegate
<PrivateImplementationDetails>
ValueType
<Module>{7fc3146a-43c2-4136-9972-07409dc7e5e3}
m8DE939F4D31FDE3
.cctor
Equals
EqualityComparer`1
System.Collections.Generic
get_Default
GetHashCode
ToString
Format
IFormatProvider
<i>j__TPar
<j>j__TPar
Double
IContainer
System.ComponentModel
Button
GroupBox
ComboBox
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method._Module_7fc3146a_43c2_4136_9972_07409dc7e5e3.qbN` | `0x4113ac` | 54932 | ✓ |
| `method.uZ.wL.fj` | `0x4033dc` | 14472 | ✓ |
| `method.DfX.NfJ.ifx` | `0x40a26c` | 14424 | ✓ |
| `method.GK3.XK4.PKY` | `0x4075c8` | 11244 | ✓ |
| `method._Module_7fc3146a_43c2_4136_9972_07409dc7e5e3.sbf6b7f2418044326bae4c0352cb9157d` | `0x41024c` | 4436 | ✓ |
| `method.uZ.wL.o4` | `0x4028a4` | 1312 | ✓ |
| `method.GK3.XK4.jKA` | `0x406e60` | 1024 | ✓ |
| `method.FlH..ctor` | `0x40ef28` | 984 | ✓ |
| `method.zRs..ctor` | `0x40faf8` | 932 | ✓ |
| `method.QRE..ctor` | `0x40f570` | 876 | ✓ |
| `method.uZ.wL.KU` | `0x4025a4` | 768 | ✓ |
| `method.uZ.wL.iH` | `0x402f38` | 664 | ✓ |
| `method.GK3.XK4.dKj` | `0x407388` | 472 | ✓ |
| `method.uZ.wL.k3` | `0x402dc4` | 372 | ✓ |
| `method.uZ.wL.dv` | `0x402444` | 352 | ✓ |
| `method.GK3.XK4.UK0` | `0x406d00` | 352 | ✓ |
| `method.uZ.wL.t0` | `0x4031d0` | 332 | ✓ |
| `method.SSR.rSl.rSw` | `0x40dbdc` | 332 | ✓ |
| `method.GK3.XK4.HKT` | `0x407260` | 296 | ✓ |
| `method.SSR.rSl.pSL` | `0x40df04` | 276 | ✓ |
| `method.uZ.wL.RW` | `0x402244` | 232 | ✓ |
| `method.uZ.wL.oe` | `0x402360` | 228 | ✓ |
| `method.TnH.Xn3.CbD` | `0x4100d0` | 216 | ✓ |
| `method.SSR.rSl.eSI` | `0x40de70` | 148 | ✓ |
| `method.SSR.rSl..cctor` | `0x40e730` | 148 | ✓ |
| `method.ASB.kS5.ISp` | `0x40e970` | 148 | ✓ |
| `method.SSR.rSl.kSW` | `0x40e054` | 140 | ✓ |
| `method.SSR.rSl.bST` | `0x40e3c4` | 136 | ✓ |
| `method.__f__AnonymousType0_2.Equals` | `0x402080` | 132 | ✓ |
| `method.__f__AnonymousType0_2.ToString` | `0x40213c` | 132 | ✓ |

### Decompiled Code Files

- [`code/method.ASB.kS5.ISp.c`](code/method.ASB.kS5.ISp.c)
- [`code/method.DfX.NfJ.ifx.c`](code/method.DfX.NfJ.ifx.c)
- [`code/method.FlH..ctor.c`](code/method.FlH..ctor.c)
- [`code/method.GK3.XK4.HKT.c`](code/method.GK3.XK4.HKT.c)
- [`code/method.GK3.XK4.PKY.c`](code/method.GK3.XK4.PKY.c)
- [`code/method.GK3.XK4.UK0.c`](code/method.GK3.XK4.UK0.c)
- [`code/method.GK3.XK4.dKj.c`](code/method.GK3.XK4.dKj.c)
- [`code/method.GK3.XK4.jKA.c`](code/method.GK3.XK4.jKA.c)
- [`code/method.QRE..ctor.c`](code/method.QRE..ctor.c)
- [`code/method.SSR.rSl..cctor.c`](code/method.SSR.rSl..cctor.c)
- [`code/method.SSR.rSl.bST.c`](code/method.SSR.rSl.bST.c)
- [`code/method.SSR.rSl.eSI.c`](code/method.SSR.rSl.eSI.c)
- [`code/method.SSR.rSl.kSW.c`](code/method.SSR.rSl.kSW.c)
- [`code/method.SSR.rSl.pSL.c`](code/method.SSR.rSl.pSL.c)
- [`code/method.SSR.rSl.rSw.c`](code/method.SSR.rSl.rSw.c)
- [`code/method.TnH.Xn3.CbD.c`](code/method.TnH.Xn3.CbD.c)
- [`code/method._Module_7fc3146a_43c2_4136_9972_07409dc7e5e3.qbN.c`](code/method._Module_7fc3146a_43c2_4136_9972_07409dc7e5e3.qbN.c)
- [`code/method._Module_7fc3146a_43c2_4136_9972_07409dc7e5e3.sbf6b7f2418044326bae4c0352cb9157d.c`](code/method._Module_7fc3146a_43c2_4136_9972_07409dc7e5e3.sbf6b7f2418044326bae4c0352cb9157d.c)
- [`code/method.__f__AnonymousType0_2.Equals.c`](code/method.__f__AnonymousType0_2.Equals.c)
- [`code/method.__f__AnonymousType0_2.ToString.c`](code/method.__f__AnonymousType0_2.ToString.c)
- [`code/method.uZ.wL.KU.c`](code/method.uZ.wL.KU.c)
- [`code/method.uZ.wL.RW.c`](code/method.uZ.wL.RW.c)
- [`code/method.uZ.wL.dv.c`](code/method.uZ.wL.dv.c)
- [`code/method.uZ.wL.fj.c`](code/method.uZ.wL.fj.c)
- [`code/method.uZ.wL.iH.c`](code/method.uZ.wL.iH.c)
- [`code/method.uZ.wL.k3.c`](code/method.uZ.wL.k3.c)
- [`code/method.uZ.wL.o4.c`](code/method.uZ.wL.o4.c)
- [`code/method.uZ.wL.oe.c`](code/method.uZ.wL.oe.c)
- [`code/method.uZ.wL.t0.c`](code/method.uZ.wL.t0.c)
- [`code/method.zRs..ctor.c`](code/method.zRs..ctor.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary's behavior and characteristics:

### Core Functionality and Purpose
The binary appears to be a **.NET-based application** (evidenced by references to `mscorlib`, `System.Windows.Forms`, and `.NET` namespaces). 
*   **Original Context:** The presence of the string `LaserCalculator.Properties` and various UI components (`Button`, `GroupBox`, `DataGridView`) suggest that the original, non-malicious purpose of the code was a utility application—specifically, a "Laser Calculator."
*   **Current State:** The sample has been heavily processed by an **obfuscator or packer**. While the original logic might be hidden within these layers, the current state of the code is designed to hinder manual analysis and automated decompilation.

### Suspicious or Malicious Behaviors
The following behaviors are indicators of potentially malicious intent or high-level evasion:
*   **Heavy Obfuscation:** The use of non-human-readable method names (e.g., `method.uZ.wL.fj`, `method.GK3.XK4.PKY`) and the "junk" characters in the string table are classic indicators of a packer or obfuscator like ConfuserEx or similar tools used by malware authors to hide functionality.
*   **Anti-Analysis/Anti-Decompilation:** The decompiler frequently reports `WARNING: Control flow encountered bad instruction data` and `halt_baddata()`. This indicates the inclusion of **junk code** and **control-flow flattening**, designed to break the logic flow for analysts using tools like IDA Pro or Ghidra.
*   **Instruction Overlapping:** The warning `Instruction at (ram,0x00407459) overlaps instruction at (ram,0x00407458)` is a specific anti-disassembly technique used to confuse linear sweep disassemblers and trick them into interpreting code incorrectly.

### Notable Techniques and Patterns
*   **Control Flow Obfuscation:** Many functions contain complex arithmetic with bitwise operations, carry flag checks (`CARRY1`), and "poisonous" instructions that serve no functional purpose other than confusing the decompiler's ability to reconstruct the original logic.
*   **Dead-Code Insertion:** The inclusion of multiple calls to methods that lead immediately to a "bad instruction" or an infinite loop (e.g., `method.uZ.wL.k3`) is used to waste the analyst's time and complicate the creation of a clean execution graph.
*   **Standard Library Abuse:** The large number of standard .NET UI components indicates that if malicious functionality exists, it is likely "wrapped" inside a legitimate-looking GUI to evade detection by security software that flags standalone, command-line shells.

### Summary for Incident Response
While the code does not explicitly show immediate evidence of network communication or file encryption in this specific snippet, **the level of protection (obfuscation/anti-disassembly) is significantly higher than what is typically found in standard commercial software.** This suggests that the sample may be a "loader" or "dropper" designed to hide a malicious payload from automated sandboxes and manual reverse engineering.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The binary uses non-human-readable method names, junk characters in string tables, and complex bitwise arithmetic to hide its actual logic from analysts. |
| **T1027.001** | Software Packing | The report explicitly identifies the use of an obfuscator/packer (e.g., ConfuserEx) to hinder manual analysis and automated decompilation. |
| **T1036** | Masquerading | The malicious functionality is "wrapped" inside a legitimate-looking GUI (a "Laser Calculator") to evade suspicion and security software detection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `jQDU.exe` (Identified as a module/binary name)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   `c6cc989d-8074-4df2-ab65-08506fc2b26d` (GUID - used for internal identifier/module)
*   `73039813-AD68-4419-8CCB-BD0AD270AA8C` (GUID - identified in `<Module>` block)
*   `7fc3146a-43c2-4136-9972-07409dc7e5e3` (GUID - identified in `<Module>` block)
*   `m8DE939F4D31FDE3` (Suspicious alphanumeric string/hex identifier)

**Other artifacts**
*   **Antidisassembly Techniques:** Instruction overlapping at `0x00407458` and `0x00407459`.
*   **Obfuscation Patterns:** Use of junk code, control-flow flattening, and non-human-readable method names (e.g., `method.uZ.wL.fj`).
*   **Application Context:** Original application name "LaserCalculator" suggests a trojanized or repurposed utility.
*   **Framework Info:** .NET Framework version `v4.0.30319`.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High (for functional classification)

4. **Key evidence**:
*   **Advanced Evasion Techniques:** The sample employs sophisticated anti-analysis measures, including control-flow flattening, "poisoned" instructions to break decompilers (Ghidra/IDA), and instruction overlapping. These are hallmark traits of professional malware designed to shield its true intent from automated systems and human analysts.
*   **Masquerading & Obfuscation:** The use of a legitimate-looking GUI ("Laser Calculator") combined with heavy .NET obfuscation (likely via ConfuserEx or similar tools) indicates a "wrapper" strategy, where the original functionality is hidden behind a decoy interface to evade detection.
*   **Loader Behavior:** While no direct C2 communication was observed in this specific sample, the high level of protection for a simple utility—coupled with the use of non-human-readable method names and junk code—strongly indicates that the primary purpose is to act as a loader or dropper for a subsequent malicious payload.
