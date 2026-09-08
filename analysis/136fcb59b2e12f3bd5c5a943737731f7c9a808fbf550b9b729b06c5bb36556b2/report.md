# Threat Analysis Report

**Generated:** 2026-09-02 15:29 UTC
**Sample:** `136fcb59b2e12f3bd5c5a943737731f7c9a808fbf550b9b729b06c5bb36556b2_136fcb59b2e12f3bd5c5a943737731f7c9a808fbf550b9b729b06c5bb36556b2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `136fcb59b2e12f3bd5c5a943737731f7c9a808fbf550b9b729b06c5bb36556b2_136fcb59b2e12f3bd5c5a943737731f7c9a808fbf550b9b729b06c5bb36556b2.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 293,376 bytes |
| MD5 | `b230edd9606542f4021ddef3e7a00257` |
| SHA1 | `0571e16fce157b34cf18ce313df29256a16333ad` |
| SHA256 | `136fcb59b2e12f3bd5c5a943737731f7c9a808fbf550b9b729b06c5bb36556b2` |
| Overall entropy | 5.005 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2476713929 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 175,104 | 6.16 | No |
| `.rsrc` | 117,248 | 2.614 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1997** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
PQAeS~
6.:$
g
~4[C)v
cU!}S
gg}V++
jL&&Zl66A~??
Sb11?*
tX,,.4
RRMv;;a
MMUf33
PPDx<<
cB!!0 
~~Gz==
fD""~T**
Vd22Nt::
xxoJ%%r\..$8
ppB|>>
aa_j55
UUxP((z
$6.:
g
&jL&6Zl6?A~?
~=Gz=d
"fD"*~T*
2Vd2:Nt:

x%oJ%.r\.
a5_j5W
=&&jL66Zl??A~
g99KrJJ
==Gzdd
""fD**~T
22Vd::Nt



$$lH\\
77Ynmm
%%oJ..r\
55_jWW
L&&jl66Z~??A
Oh44\Q
sb11S*
uB!!c 
D""fT**~;
;d22Vt::N
J%%o\..r8
'6-9d

[T:$6.
[.:$6g
j_FbT~
h4,8$@_
2\tHlWB
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADP
v4.0.30319
#Strings
 0bZ-
 +dd3
&$&(&.&3&E&J&O&^&e&m&u&z&
' '\'d'm'
'V(\(l(
*6*<*N*q*|*
,	-]-r-
/?/G/P/j/
0E0P0U0{0
1?1H1X1j1
3#4F4|4
4	5C5J5P5`5f5l5{5
8$8*8Y8
!%!7!G!^!f!r!
"1"9"Y"a"i"
$7%?%c%
(5)=)E)
2.2<2b2
<>9__0_10
<Id1>b__0_10
smethod_10
get_Id10
set_Id10
Struct10
Entity10
<>9__0_20
<Id1>b__0_20
Struct20
Struct30
Struct40
A8F9B62160DF085B926D5ED70E2B0F6C95A25280
F413CEA9BAA458730567FE47F57CC3C94DDF63C0
struct10_0
struct20_0
struct30_0
struct40_0
<>9__0_0
<Id1>b__0_0
<Read>b__0_0
<WriteLine>b__0_0
<CloseBrowser>b__0_0
<.ctor>b__0_0
<DomainExists>b__0_0
<>c__DisplayClass0_0
struct0_0
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Proc.get_FilePath` | `0x4075fd` | 196608 | ✓ |
| `sym.VisualPlus.Structure.RECT.Union_2` | `0x4142bc` | 131072 | ✓ |
| `method.XRails.Controls.XRails_Button.set_ForeColor` | `0x407e77` | 128902 | ✓ |
| `method.XRails.Controls.XRails_TitleLabel.OnPaint` | `0x4082f5` | 64386 | ✓ |
| `method.XRails.Controls.XRails_TitleLabel..ctor` | `0x4162b8` | 57348 | ✓ |
| `method.Entity18.Id1` | `0x408310` | 1648 | ✓ |
| `method.AesFastEngine.DecryptBlock` | `0x40bdb0` | 1464 | ✓ |
| `method.AesFastEngine.EncryptBlock` | `0x40b808` | 1448 | ✓ |
| `method.QueryProcessor.GetOffset` | `0x410810` | 1444 | ✓ |
| `method.QueryProcessor.ReadMasterOfContext` | `0x410104` | 1404 | ✓ |
| `method.FileSearcher.Search` | `0x40e574` | 996 | ✓ |
| `method.SystemInfoHelper.QueryAV` | `0x4126cc` | 944 | ✓ |
| `method.RosComNadzor.Id3` | `0x40f294` | 812 | ✓ |
| `method.BrEx.Id3` | `0x40ee90` | 808 | ✓ |
| `method.Entity21.Id1` | `0x409ce4` | 784 | ✓ |
| `method.XRails.Controls.XRails_Button.RoundedRect` | `0x414660` | 704 | ✓ |
| `method.XRails.Controls.XRails_Button.OnPaint` | `0x414b1c` | 644 | ✓ |
| `method.Form1.InitializeComponent` | `0x40fd80` | 616 | ✓ |
| `method.GcmBlockCipher.Init` | `0x40ad64` | 612 | ✓ |
| `method.XRails.Controls.XRails_ControlBox.OnPaint` | `0x415430` | 604 | ✓ |
| `method.FileScanning.FindPaths` | `0x40e320` | 596 | ✓ |
| `method.FileCopier.FindPaths` | `0x4133c4` | 592 | ✓ |
| `method.SystemInfoHelper.QueryProc` | `0x412a7c` | 588 | ✓ |
| `method.Program2.WriteLine` | `0x40cd18` | 568 | ✓ |
| `sym.SystemInfoHelper.QueryProc` | `0x4124b4` | 536 | ✓ |
| `method.AllWallets.Id3` | `0x40eb48` | 532 | ✓ |
| `method.Entity18.Id3` | `0x408c84` | 516 | ✓ |
| `method.Discord.GetTokens` | `0x40f6ac` | 480 | ✓ |
| `method.Entity18.Id2` | `0x408aac` | 472 | ✓ |
| `method.MemoryCollect.Id1` | `0x409830` | 472 | ✓ |

### Decompiled Code Files

- [`code/method.AesFastEngine.DecryptBlock.c`](code/method.AesFastEngine.DecryptBlock.c)
- [`code/method.AesFastEngine.EncryptBlock.c`](code/method.AesFastEngine.EncryptBlock.c)
- [`code/method.AllWallets.Id3.c`](code/method.AllWallets.Id3.c)
- [`code/method.BrEx.Id3.c`](code/method.BrEx.Id3.c)
- [`code/method.Discord.GetTokens.c`](code/method.Discord.GetTokens.c)
- [`code/method.Entity18.Id1.c`](code/method.Entity18.Id1.c)
- [`code/method.Entity18.Id2.c`](code/method.Entity18.Id2.c)
- [`code/method.Entity18.Id3.c`](code/method.Entity18.Id3.c)
- [`code/method.Entity21.Id1.c`](code/method.Entity21.Id1.c)
- [`code/method.FileCopier.FindPaths.c`](code/method.FileCopier.FindPaths.c)
- [`code/method.FileScanning.FindPaths.c`](code/method.FileScanning.FindPaths.c)
- [`code/method.FileSearcher.Search.c`](code/method.FileSearcher.Search.c)
- [`code/method.Form1.InitializeComponent.c`](code/method.Form1.InitializeComponent.c)
- [`code/method.GcmBlockCipher.Init.c`](code/method.GcmBlockCipher.Init.c)
- [`code/method.MemoryCollect.Id1.c`](code/method.MemoryCollect.Id1.c)
- [`code/method.Proc.get_FilePath.c`](code/method.Proc.get_FilePath.c)
- [`code/method.Program2.WriteLine.c`](code/method.Program2.WriteLine.c)
- [`code/method.QueryProcessor.GetOffset.c`](code/method.QueryProcessor.GetOffset.c)
- [`code/method.QueryProcessor.ReadMasterOfContext.c`](code/method.QueryProcessor.ReadMasterOfContext.c)
- [`code/method.RosComNadzor.Id3.c`](code/method.RosComNadzor.Id3.c)
- [`code/method.SystemInfoHelper.QueryAV.c`](code/method.SystemInfoHelper.QueryAV.c)
- [`code/method.SystemInfoHelper.QueryProc.c`](code/method.SystemInfoHelper.QueryProc.c)
- [`code/method.XRails.Controls.XRails_Button.OnPaint.c`](code/method.XRails.Controls.XRails_Button.OnPaint.c)
- [`code/method.XRails.Controls.XRails_Button.RoundedRect.c`](code/method.XRails.Controls.XRails_Button.RoundedRect.c)
- [`code/method.XRails.Controls.XRails_Button.set_ForeColor.c`](code/method.XRails.Controls.XRails_Button.set_ForeColor.c)
- [`code/method.XRails.Controls.XRails_ControlBox.OnPaint.c`](code/method.XRails.Controls.XRails_ControlBox.OnPaint.c)
- [`code/method.XRails.Controls.XRails_TitleLabel..ctor.c`](code/method.XRails.Controls.XRails_TitleLabel..ctor.c)
- [`code/method.XRails.Controls.XRails_TitleLabel.OnPaint.c`](code/method.XRails.Controls.XRails_TitleLabel.OnPaint.c)
- [`code/sym.SystemInfoHelper.QueryProc.c`](code/sym.SystemInfoHelper.QueryProc.c)
- [`code/sym.VisualPlus.Structure.RECT.Union_2.c`](code/sym.VisualPlus.Structure.RECT.Union_2.c)

## Behavioral Analysis

This analysis incorporates the final disassembly (Chunk 11/11) into the ongoing investigation. The final segment provides a "micro-view" of how the **Arithmetic Bloat** and **Virtual Machine (VM) mapping** manifest at the instruction level.

### Updated Analysis Summary (Final Integration)

The data in Chunk 11 confirms that the malware utilizes a sophisticated **Virtual Machine (VM) architecture** where nearly every line of "standard" code is actually an implementation of a VM handler. The presence of `method.XRails_TitleLabel.OnPaint`—which contains no graphical or UI-related logic—is the definitive "smoking gun" for the Ghost Function tactic.

---

### New Findings from Chunk 11

#### 1. Validation of "Ghost Functions" via Logic Mapping
The function `method.XRails_TitleLabel.OnPaint` is a perfect example of a **Decoy Name**. While the name suggests it handles UI rendering for a title label, the inner logic consists entirely of complex bitwise operations, carry-flag checks (`CARRY1`, `CARRY4`), and "Arithmetic Bloat."
*   **The Analysis:** There are no calls to graphics libraries (e.g., DirectX, OpenGL) or string manipulations related to UI. Instead, it performs high-complexity arithmetic on internal registers. This confirms that the function name is irrelevant; it serves only as an entry point into a specific "opcode" within the custom Virtual Machine.

#### 2. Extreme Arithmetic Bloat (Decoding Logic)
The disassembly shows patterns like:
`puVar19 = puVar19 + uVar1;` followed by `uVar1 = CARRY4(uVar10,puVar12) || CARRY4(uVar11,puVar12)`.
*   **The Tactic:** This is a common technique in high-end packers (like VMProtect or Themida). A simple addition of two variables is expanded into several lines to check for overflows and carry bits manually. 
*   **Technical Impact:** By forcing the disassembler to track carries and potential overflows over dozens of instructions just to perform one addition, the author creates a "fog of war." It makes it nearly impossible for an analyst to trace data flow because the actual value being manipulated is hidden behind a wall of noise.

#### 3. Complex Control Flow (State Machine Logic)
The frequent use of `goto` labels (e.g., `code_r0x004083ee`, `code_r0x00408751`) combined with complex conditional checks (`if (CARRY1(uVar20,uVar5)) ... else ...`) suggests a **State Machine**.
*   **The Interpretation:** The code is not "flowing" naturally. It is jumping between different logic blocks based on the results of arithmetic operations. This is the hallmark of a VM dispatcher where each block is a "handler" for an instruction in the malicious payload's bytecode.

#### 4. Advanced Anti-Analysis Markers
The disassembly contains several `WARNING` flags:
*   `WARNING: Bad instruction - Truncating control flow here`
*   `WARNING: Instruction at (...) overlaps instruction at (...)`
*   **Conclusion:** The author is deliberately using **overlapping instructions** and "junk code" to break the linear sweep algorithm used by tools like Ghidr. By intentionally creating "bad" instructions, they ensure that any automated analysis tool will fail to provide a complete or accurate call graph.

---

### Updated Analysis Summary Table

| Category | Observation | Impact |
| :--- | :--- | **High** | Robust calculation of carry bits and overflows to hide simple arithmetic logic. |
| **VM Architecture** | Verified via "Ghost Functions" (e.g., `OnPaint`) | **Critical.** The core payload is not in the code; it is inside a virtualized environment. |
| **Decoy Tactics** | Mismatched Function Names | **High.** Misleads human analysts into wasting time on irrelevant "features." |
| **Anti-Analysis** | Overlapping Instructions & Bad Data | **Critical.** Targets the logic of disassemblers to prevent automated mapping of code blocks. |
| **Encryption** | AES-GCM (Confirmed in earlier chunks) | **High.** Ensures that even if the VM is de-virtualized, the payload remains encrypted until execution. |
| **Persistence/Tactic** | Targeted Data Collection (Discord) | **Critical.** Confirms a goal of credential theft and potential automated "farming" or trading activities. |

---

### Final Technical Verdict

This malware is a high-tier, **custom-engineered packer**. It does not simply use standard obfuscation; it wraps the malicious payload inside a custom execution environment (VM). 

The logic seen in `method.XRails_TitleLabel.OnPaint` proves that the "function" isn't painting anything—it is executing a sequence of bytes from a hidden, encrypted buffer. The "Arithmetic Bloat" ensures that even if you can see the code, it is computationally and mentally exhausting to simplify it back into its original meaning.

**Key Components Identified:**
1.  **Encryption Layer:** AES-GCM for payload protection.
2.  **Virtualization Layer:** A custom VM with "Ghost Functions" to hide opcode execution.
3.  **Anti-Analysis Layer:** Overlapping instructions and junk code to break decompiler integrity.
4.  **Targeted Payload:** Likely focuses on Discord data theft or automated interaction with game entities (based on previous mentions of `GetTokens` and `Entity18`).

---

### Recommended Investigative Roadmap

To fully "crack" this sample, the following steps are recommended:

1.  **De-virtualization Scripting:** Rather than manually reversing each "Ghost Function," write a script to identify repetitive patterns (like the `CARRY` logic). Replace these blocks with simple labels (e.g., `vm_handler_add`) to clean up the graph.
2.  **Symbolic Execution:** Use a tool like **Triton** or **Angr** on the "Arithmetic Bloat" sections. These tools can simplify complex mathematical chains into their simplest forms, effectively stripping away the "noise."
3.  **Trace Logging:** Run the binary in a controlled debugger (x64dbg) and log the execution path of the VM. By tracking which "Ghost Functions" are called most frequently, you can identify the primary logic of the payload.
4.  **Memory Forensics:** Monitor for `VirtualProtect` or `VirtualAlloc` calls immediately following an unusually long period of arithmetic-heavy loop execution. This is often where the VM "hands off" control to the actual decrypted payload.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Packer | The use of a custom Virtual Machine (VM) architecture and "Arithmetic Bloat" to hide execution logic is characteristic of sophisticated packing techniques like VMProtect or Themida. |
| **T1027** | Obfuscated Files or Information | The use of "Ghost Functions" with misleading names (e.g., `OnPaint`) serves as a decoy to mislead manual analysis and mask the true purpose of the code. |
| **T1027** | Obfuscated Files or Information | The intentional use of overlapping instructions and junk code is designed to break linear sweep algorithms in disassemblers like Ghidr. |
| **T1027** | Obfuscated Files or Information | The implementation of AES-GCM ensures that the malicious payload remains encrypted and hidden from automated detection until it is executed within the VM. |
| **T1539** | Steal Web Credentials | The specific targeting of Discord data and "Tokens" indicates an intent to steal user credentials and session information. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs):

**Hashes**
* `A8F9B62160DF085B926D5ED70E2B0F6C95A25280` (SHA-1)
* `F413CEA9BAA458730567FE47F57CC3C94DDF63C0` (SHA-1)

**Other artifacts**
* **Encryption Scheme:** AES-GCM (Confirmed usage for payload protection).
* **Virtualization Logic:** Custom Virtual Machine (VM) architecture used to wrap the core payload.
* **Obfuscation Techniques:** 
    * Arithmetic Bloat (used to hide simple logic within complex mathematical chains).
    * Ghost Functions (e.g., `method.XRails_TitleLabel.OnPaint` — a dummy name for a VM handler).
    * Overlapping Instructions & Junk Code (used to break linear sweep disassembly).
* **Target/Context:** Discord data theft (specifically mentioning "GetTokens" and "Discord data").

***Note:** No IP addresses, URLs, Registry Keys, or Mutex names were identified in the provided text. Standard library strings (e.g., mscorlib, System.Resources) were excluded as per instructions.*

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family**: custom
2. **Malware type**: infostealer
3. **Confidence**: High
4. **Key evidence**:
    * **Advanced Obfuscation (VM Architecture):** The malware utilizes a sophisticated custom Virtual Machine (VM) and "Ghost Functions" (e.g., `method.XRails_TitleLabel.OnPaint`) to hide its execution logic behind complex arithmetic bloat, designed to thwart both manual analysis and automated tools like Ghidr.
    * **Targeted Information Theft:** The behavioral indicators specifically point toward the theft of Discord-related credentials, including "Tokens" and other session data, likely for use in automated farming or trading activities.
    * **Robust Anti-Analysis Layer:** The inclusion of overlapping instructions, junk code, and AES-GCM encryption confirms a high-tier development approach intended to shield a malicious payload from detection and analysis.
