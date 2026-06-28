# Threat Analysis Report

**Generated:** 2026-06-28 02:44 UTC
**Sample:** `023280288a154681b1652c24289acc49e44beb65e1f12948aee25dad981b3e0e_023280288a154681b1652c24289acc49e44beb65e1f12948aee25dad981b3e0e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `023280288a154681b1652c24289acc49e44beb65e1f12948aee25dad981b3e0e_023280288a154681b1652c24289acc49e44beb65e1f12948aee25dad981b3e0e.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 6 sections |
| Size | 149,504 bytes |
| MD5 | `3aec3b9525dcbac3e7d6f83980c93d18` |
| SHA1 | `5a924ce418c0f91c7b31deea4aed49824af62c73` |
| SHA256 | `023280288a154681b1652c24289acc49e44beb65e1f12948aee25dad981b3e0e` |
| Overall entropy | 7.202 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1662686821 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 97,792 | 6.634 | No |
| `.itext` | 1,536 | 2.934 | No |
| `.rdata` | 1,536 | 3.537 | No |
| `.data` | 40,960 | 7.988 | ⚠️ Yes |
| `.pdata` | 2,560 | 7.286 | ⚠️ Yes |
| `.reloc` | 4,096 | 6.739 | No |

### Imports

**gdi32.dll**: `SetPixel`, `SetDCBrushColor`, `SelectPalette`, `GetTextColor`, `GetDeviceCaps`, `CreateSolidBrush`
**USER32.dll**: `DefWindowProcW`, `CreateMenu`, `EndDialog`, `GetDlgItem`, `GetKeyNameTextW`, `GetMessageW`, `GetWindowTextW`, `IsDlgButtonChecked`, `LoadImageW`, `LoadMenuW`, `DialogBoxParamW`
**KERNEL32.dll**: `SetLastError`, `LoadLibraryW`, `GetTickCount`, `GetLastError`, `GetCommandLineW`, `GetCommandLineA`, `FreeLibrary`

## Extracted Strings

Total strings found: **388** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.itext
`.rdata
@.data
.pdata
.reloc
r;Ew
X_^ZY[
=j&&LZ66lA??~
}{))R>
f""D~**T
V22dN::t
o%%Jr..\$
&&Lj66lZ??~A
99rKJJ
==zGdd
""Df**T~
;22dV::tN



$$Hl\\
C77nYmm
%%Jo..\r
55j_WW
&Lj&6lZ6?~A?
~=zG=d
"Df"*T~*
2dV2:tN:

x%Jo%.\r.
a5j_5W
ggV}++
Lj&&lZ66~A??
bS11*?
Xt,,4.
RRvM;;
MMfU33
PPxD<<%
Bc!! 0
~~zG==
Df""T~**;
dV22tN::
xxJo%%\r..8$
pp|B>>q
aaj_55
UUPx((
cccc||||wwww{{{{
kkkkoooo
gggg++++
YYYYGGGG
&&&&6666????
uuuu				
nnnnZZZZ
RRRR;;;;
[[[[jjjj
9999JJJJLLLLXXXX
CCCCMMMM3333
PPPP<<<<
~~~~====dddd]]]]
ssss````
""""****
^^^^
2222::::



IIII
$$$$\\\\
7777mmmm
llllVVVV
eeeezzzz
xxxx%%%%....
pppp>>>>
ffffHHHH
aaaa5555WWWW
UUUU((((
BBBBhhhhAAAA
='9-6d
_jbF~T
11#?*0
,4$8_@
t\lHBW
QPeA~S
.6$:g

>4$8,@
p\lHtW
+HpXhE
T6$:.

6'9-
d
T[$:.6
RRRR				jjjj
00006666
CCCCDDDD
TTTT{{{{
####====
BBBB
ffff((((
vvvv[[[[
IIIImmmm
%%%%rrrr
]]]]eeee
llllppppHHHHPPPP
FFFFWWWW
kkkk::::
AAAAOOOOgggg
tttt""""
nnnnGGGG
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00419479` | `0x419479` | 2951 | ✓ |
| `fcn.00418496` | `0x418496` | 1870 | ✓ |
| `fcn.00408230` | `0x408230` | 1838 | ✓ |
| `fcn.004150e0` | `0x4150e0` | 1748 | ✓ |
| `fcn.00401a9c` | `0x401a9c` | 1552 | ✓ |
| `fcn.00416688` | `0x416688` | 1332 | ✓ |
| `fcn.00404d08` | `0x404d08` | 1295 | ✓ |
| `fcn.0040cfcc` | `0x40cfcc` | 1251 | ✓ |
| `fcn.004104b4` | `0x4104b4` | 1199 | ✓ |
| `fcn.00405218` | `0x405218` | 1141 | ✓ |
| `fcn.004091c8` | `0x4091c8` | 1120 | ✓ |
| `fcn.0040f82c` | `0x40f82c` | 1113 | ✓ |
| `fcn.004020ac` | `0x4020ac` | 1073 | ✓ |
| `fcn.00409c64` | `0x409c64` | 1070 | ✓ |
| `fcn.004139c4` | `0x4139c4` | 979 | ✓ |
| `fcn.0041205c` | `0x41205c` | 971 | ✓ |
| `fcn.00415d28` | `0x415d28` | 894 | ✓ |
| `fcn.0040fc88` | `0x40fc88` | 888 | ✓ |
| `fcn.00417034` | `0x417034` | 886 | ✓ |
| `fcn.00416124` | `0x416124` | 875 | ✓ |
| `fcn.00410000` | `0x410000` | 821 | ✓ |
| `fcn.0040e8ac` | `0x40e8ac` | 812 | ✓ |
| `fcn.0040ae74` | `0x40ae74` | 775 | ✓ |
| `fcn.00406f48` | `0x406f48` | 758 | ✓ |
| `fcn.00417458` | `0x417458` | 735 | ✓ |
| `fcn.004157b4` | `0x4157b4` | 717 | ✓ |
| `fcn.0040a68c` | `0x40a68c` | 714 | ✓ |
| `fcn.00418083` | `0x418083` | 711 | ✓ |
| `fcn.00415a84` | `0x415a84` | 675 | ✓ |
| `fcn.00417db6` | `0x417db6` | 669 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401a9c.c`](code/fcn.00401a9c.c)
- [`code/fcn.004020ac.c`](code/fcn.004020ac.c)
- [`code/fcn.00404d08.c`](code/fcn.00404d08.c)
- [`code/fcn.00405218.c`](code/fcn.00405218.c)
- [`code/fcn.00406f48.c`](code/fcn.00406f48.c)
- [`code/fcn.00408230.c`](code/fcn.00408230.c)
- [`code/fcn.004091c8.c`](code/fcn.004091c8.c)
- [`code/fcn.00409c64.c`](code/fcn.00409c64.c)
- [`code/fcn.0040a68c.c`](code/fcn.0040a68c.c)
- [`code/fcn.0040ae74.c`](code/fcn.0040ae74.c)
- [`code/fcn.0040cfcc.c`](code/fcn.0040cfcc.c)
- [`code/fcn.0040e8ac.c`](code/fcn.0040e8ac.c)
- [`code/fcn.0040f82c.c`](code/fcn.0040f82c.c)
- [`code/fcn.0040fc88.c`](code/fcn.0040fc88.c)
- [`code/fcn.00410000.c`](code/fcn.00410000.c)
- [`code/fcn.004104b4.c`](code/fcn.004104b4.c)
- [`code/fcn.0041205c.c`](code/fcn.0041205c.c)
- [`code/fcn.004139c4.c`](code/fcn.004139c4.c)
- [`code/fcn.004150e0.c`](code/fcn.004150e0.c)
- [`code/fcn.004157b4.c`](code/fcn.004157b4.c)
- [`code/fcn.00415a84.c`](code/fcn.00415a84.c)
- [`code/fcn.00415d28.c`](code/fcn.00415d28.c)
- [`code/fcn.00416124.c`](code/fcn.00416124.c)
- [`code/fcn.00416688.c`](code/fcn.00416688.c)
- [`code/fcn.00417034.c`](code/fcn.00417034.c)
- [`code/fcn.00417458.c`](code/fcn.00417458.c)
- [`code/fcn.00417db6.c`](code/fcn.00417db6.c)
- [`code/fcn.00418083.c`](code/fcn.00418083.c)
- [`code/fcn.00418496.c`](code/fcn.00418496.c)
- [`code/fcn.00419479.c`](code/fcn.00419479.c)

## Behavioral Analysis

This final chunk of disassembly provides the definitive evidence needed to conclude that this binary is protected by a **highly sophisticated Virtual Machine (VM)-based packer/protector.** 

The code provided in Chunk 4 moves from "suspicious behavior" into "explicit architecture." We are no longer just looking at obfuscated code; we are looking at the **execution engine** of a custom virtual machine.

### Updated Analysis Summary (Chunk 4/4)

#### 1. Explicit Instruction Dispatching (The "VM Heart")
In `fcn.00417458`, we see one of the most tell-tale signs of a VM protector: **the Switch-Table dispatch.**
*   **Observation:** The code uses a series of `if/else if` blocks to compare specific, large hexadecimal constants (e.g., `0x45471d17`, `0x459f1cd7`, `0x452f4997`) against the result of an internal decode function.
*   **Analysis:** These are not "data" values; these are **Virtual Opcodes**. The VM is reading a byte from its own custom bytecode, passing it through a decoder (`fcn.004011c4`), and then using that result to decide which "handler" (the code that actually performs the action) to execute. This allows the attacker to hide the actual logic of the malware inside these "magic" numbers, making standard static analysis almost impossible.

#### 2. Decoupled Handler Logic
Functions like `fcn.00406f48` and `fcn.00415a84` act as **Handler Routines**. 
*   **Observation:** These functions contain repetitive patterns of checking offsets (e.g., `uVar4 + 0xbc`, `uVar4 + 0xc0`) followed by calls to shared utility functions like `fcn.00406844` and `fcn.0040686c`.
*   **Analysis:** This is the "backend" of the VM. The interpreter loop (the dispatcher) identifies an opcode; it then jumps here to perform a specific task—such as moving a value, adding two numbers, or performing a string operation. By breaking every common x86 instruction into multiple VM instructions, the protector ensures that no single piece of "malicious" code exists in plain sight.

#### 3. Integrity Check & State Validation
The function `fcn.0040a68c` demonstrates **Anti-Tamper Logic** within the VM loop.
*   **Observation:** It checks a series of values against "magic constants" (e.g., `0x5c005c`, `0xc12a7328`) and compares multiple stack variables simultaneously before proceeding.
*   **Analysis:** This is likely a **Validation Gate**. If an analyst tries to patch the binary or if a debugger changes the state of the virtual registers, these specific "magic" checks will fail. The complexity of the comparisons (e.g., `(var_58ch != 0xc12a7328) || (iStack_58c != 0x11d2f81f)`) is designed to ensure that even if a researcher finds one "gate," they cannot easily bypass the entire sequence of checks.

#### 4. Abstracted Data Handling
Functions like `fcn.00418083` and `fcn.00417db6` appear to be **Internal VM Utilities**.
*   **Observation:** They involve complex pointer arithmetic, boundary checking (`0x16800`), and "wrapping" logic. 
*   **Analysis:** These are the functions that handle things like buffer copies, string manipulations, or memory management *inside* the virtual environment. The fact that these are so heavily abstracted means the malware's real strings (e.g., C2 URLs, file paths) are likely encrypted and only "materialize" inside the VM's private memory space during execution.

---

### Final Summary of Technical Indicators

| Feature | Evidence Location | Significance |
| :--- | :--- | :--- |
| **VM Dispatcher** | `fcn.00417458` | Confirms a custom architecture where "instructions" are decoded from non-standard opcodes. |
| **Handler Mapping** | `fcn.00406f48`, `fcn.00415a84` | Shows how different "virtual instructions" are mapped to specific chunks of code. |
| **Magic Number Gates**| `fcn.0040a68c` | Identifies anti-debugging and anti-tamper checks designed to break tools like x64dbg or IDA Pro. |
| **Instruction Shredding** | Across all functions | The use of complex offsets (e.g., `uVar4 + 0xbc`) ensures that standard cross-references cannot be easily mapped by automated tools. |

### Final Conclusion
This is a **high-sophistication, professional-grade malware sample.** It utilizes a **Custom Virtual Machine (VM) protection layer** to shield the primary malicious payload (the "Guest" code). 

The true behavior of the malware—whether it's exfiltrating data, encrypting files, or establishing a backdoor—is currently hidden inside the VM's bytecode. To uncover the actual functionality, an analyst would need to:
1.  **Map the Opcodes:** Identify what each "magic" constant in `fcn.00417458` does.
2.  **Trace the Dispatcher:** Use a debugger to log the flow of execution through the handlers.
3.  **Dump the Guest Memory:** Identify the point where the VM decodes enough data to perform its primary malicious action (e.g., opening a socket or writing a file).

**Risk Assessment: High.** The complexity of this protection suggests that the authors are experienced in bypassing standard security measures and intend for the malware to remain undetected by automated scanners and manual analysis for an extended period.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1029 | Virtualization | The malware utilizes a custom virtual machine architecture with its own instruction set (opcodes) and handlers to hide the underlying malicious logic. |
| T1027 | Obfuscated Files or Information | "Instruction shredding" and the use of complex offsets are employed to obscure code flow and prevent static analysis from identifying key operations. |
| T1497 | Virtualization/Sandbox Evasion | The "Validation Gates" and magic constant checks function as anti-tamper mechanisms designed to detect and hinder analysis in debugger environments like x64dbg. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted list of Indicators of Compromise (IOCs). 

Note: Because this sample utilizes a **Virtual Machine (VM)-based packer**, traditional indicators like plaintext IP addresses or file paths are currently obfuscated within the "guest" code and do not appear in the raw string dump.

### **IP addresses / URLs / Domains**
*   *None identified.* (Note: These are likely encrypted/hidden within the VM's proprietary bytecode).

### **File paths / Registry keys**
*   *None identified.* (Standard system libraries like `gdi32.dll`, `user32.dll`, and `kernel32.dll` were excluded as per instructions).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *No file hashes (MD5/SHA1/SHA256) were present in the provided text.* 
*(Note: The hex values below are internal VM opcodes, not file hashes).*

### **Other artifacts**
**VM Dispatcher & Handler Logic (Internal Indicators):**
These identify the specific architecture of the custom packer.
*   **VM Opcode Constants:** `0x45471d17`, `0x459f1cd7`, `0x452f4997` (Used in `fcn.00417458`)
*   **Anti-Tamper Magic Gates:** `0x5c005c`, `0xc12a7328` (Used in `fcn.0040a68c`)

**Internal Function Offsets (Analysis Markers):**
These identify the core components of the protection layer:
*   **Dispatcher:** `fcn.00417458`
*   **Handler Routines:** `fcn.00406f48`, `fcn.00415a84`
*   **Internal VM Utilities:** `fcn.00418083`, `fcn.00417db6`

**Behavioral Signature:**
*   **Technique:** Custom Virtual Machine (VM) Execution Environment.
*   **Mechanism:** Instruction Shredding via complex offset calculations (e.g., `uVar4 + 0xbc`).

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: Unknown (Sophisticated Custom Packer)
2. **Malware type**: Loader / Dropper
3. **Confidence**: Medium
4. **Key evidence**:
    *   **VM-Based Protection:** The sample utilizes a highly sophisticated custom virtual machine architecture, replacing standard x86 instructions with a proprietary bytecode and "instruction shredding" to hide the core logic.
    *   **Anti-Analysis Mechanisms:** The presence of "Validation Gates" (magic constant checks) specifically designed to detect and thwart debuggers and manual analysis tools.
    *   **Payload Obfuscation:** The primary malicious functionality is currently hidden within the "guest" code of the VM, which is a hallmark of advanced loaders used to deliver further stages of malware (like RATs or Ransomware).
