# Threat Analysis Report

**Generated:** 2026-08-11 19:56 UTC
**Sample:** `0e2da089bb44fd77506e5a4219dc27a33727f059d3fac8687e58a4e42bd6f562_0e2da089bb44fd77506e5a4219dc27a33727f059d3fac8687e58a4e42bd6f562.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e2da089bb44fd77506e5a4219dc27a33727f059d3fac8687e58a4e42bd6f562_0e2da089bb44fd77506e5a4219dc27a33727f059d3fac8687e58a4e42bd6f562.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 9 sections |
| Size | 13,617,152 bytes |
| MD5 | `6d7686cc98ade67bc3d2a2816db91a92` |
| SHA1 | `e97dcb7217617d43a3e7459e0a80c4d016ea2b83` |
| SHA256 | `0e2da089bb44fd77506e5a4219dc27a33727f059d3fac8687e58a4e42bd6f562` |
| Overall entropy | 7.919 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1780364667 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 0 | 0.0 | No |
| `.rdata` | 0 | 0.0 | No |
| `.data` | 0 | 0.0 | No |
| `.pdata` | 0 | 0.0 | No |
| `.CRT` | 0 | 0.0 | No |
| `.ess0` | 0 | 0.0 | No |
| `.ess1` | 512 | 0.763 | No |
| `.ess2` | 13,614,592 | 7.919 | ⚠️ Yes |
| `.rsrc` | 1,024 | 3.416 | No |

### Imports

**d3d9.dll**: `Direct3DCreate9`
**WS2_32.dll**: `WSACleanup`
**bcrypt.dll**: `BCryptCloseAlgorithmProvider`
**CRYPT32.dll**: `CryptProtectData`
**ntdll.dll**: `RtlAllocateHeap`
**ucrtbase.dll**: `__stdio_common_vsprintf`
**KERNEL32.dll**: `AssignProcessToJobObject`
**USER32.dll**: `AdjustWindowRectEx`
**GDI32.dll**: `GetDeviceCaps`
**SHELL32.dll**: `SHBrowseForFolderA`
**ole32.dll**: `OleInitialize`
**ADVAPI32.dll**: `LookupAccountSidW`

## Extracted Strings

Total strings found: **24299** (showing first 100)

```
!This program cannot be run in DOS mode.$
`.rdata
@.data
.pdata
@.ess0
`.ess1
h.rsrc
\
t$(E
P98K
\rL=XG
_E3`zV
AWSAQJ
K
<t_fE
AYZ]A[
APAXf3
f59;f3
AXYYAYAX
AYAYAYAYAY
APAS]A
3Yy=L

/Yy=N
+4{kE3
QXXAX]
dI4$E3
AYXA[X
f	D$H
W]]XX
,:XAXX
AQL	L$
#K#.D3
4%7AQD
t$@h<8 
D,!Lt+V
i(e?Y/
yA)M(H
r@8=BGO
_D|NoC
)&BfE3
XYX^]Y
DtRfD
RXZAYZZAY
4|B1TL	
5u-wL3
,M;vQ
AQAQA3
xpb	_fB
PAYYZA[A[AY
h/U
^H
b`
=3i
De_>tb(
dKq(c<
t\
fA3
*XAXZZZA[[
54x(#3
4Es>:
]>S WM
\R/rEI
AXZ^AX
A[ASfF
EAZ_]QJ
\D]"[3
x1IcH6>
9&)"LfA
AYAYAX
	#/qfD
AYAXfA
AYZRD2
2AY]YAYAY
"]AY]ZX[
("1%Hc
5] }:
174 }H
AYX]AY
=V	*A3
3e8U]I
L$+Hc
n"~]g
}krB,b
!jfpc
vjc2Fm
[n'AkiP|F
Q	#	0I
J)D$#f!
APAQ4A2
XA[AYXY
A[YAYY]
kA[YAX
=DAYH3
XXAXYAY
rA[YAY
ASA[Hc
AYAYA[
f+,fD
5<6)M3
2o=;E3
f5i~fA3
f5ZVfA3
Z]YA[Y]
A[A[AYAX
MW;5A
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140b69b30` | `0x140b69b30` | 12863470 | ✓ |
| `fcn.140c02531` | `0x140c02531` | 12231999 | ✓ |
| `fcn.140c4bf5d` | `0x140c4bf5d` | 11942860 | ✓ |
| `fcn.140c4c065` | `0x140c4c065` | 11923100 | ✓ |
| `fcn.140c93d92` | `0x140c93d92` | 11651805 | ✓ |
| `fcn.140c94052` | `0x140c94052` | 11641517 | ✓ |
| `fcn.140bb864e` | `0x140bb864e` | 3861737 | ✓ |
| `fcn.140bb8597` | `0x140bb8597` | 3836823 | ✓ |
| `fcn.140bb86ff` | `0x140bb86ff` | 3788727 | ✓ |
| `fcn.140bb855d` | `0x140bb855d` | 3784001 | ✓ |
| `fcn.140bb889b` | `0x140bb889b` | 3715186 | ✓ |
| `fcn.140c026e8` | `0x140c026e8` | 3552846 | ✓ |
| `fcn.140b71340` | `0x140b71340` | 3481414 | ✓ |
| `fcn.140bb87f5` | `0x140bb87f5` | 3354645 | ✓ |
| `fcn.140bb84c0` | `0x140bb84c0` | 3232303 | ✓ |
| `fcn.140bb8839` | `0x140bb8839` | 3229177 | ✓ |
| `fcn.140c02229` | `0x140c02229` | 3163488 | ✓ |
| `fcn.140c024b3` | `0x140c024b3` | 3158737 | ✓ |
| `fcn.140c4c0fc` | `0x140c4c0fc` | 3157897 | ✓ |
| `fcn.140c023b7` | `0x140c023b7` | 3024754 | ✓ |
| `fcn.140c02421` | `0x140c02421` | 2946495 | ✓ |
| `fcn.140c4bcfe` | `0x140c4bcfe` | 2777275 | ✓ |
| `fcn.140c4c1a0` | `0x140c4c1a0` | 2659256 | ✓ |
| `fcn.140b5a83f` | `0x140b5a83f` | 2595499 | ✓ |
| `fcn.140c4be63` | `0x140c4be63` | 2585610 | ✓ |
| `fcn.140bb0058` | `0x140bb0058` | 2505103 | ✓ |
| `fcn.140c93ea9` | `0x140c93ea9` | 2461811 | ✓ |
| `fcn.140c93f16` | `0x140c93f16` | 2433785 | ✓ |
| `fcn.140d77252` | `0x140d77252` | 2244433 | ✓ |
| `fcn.140d806a0` | `0x140d806a0` | 2192420 | ✓ |

### Decompiled Code Files

- [`code/fcn.140b5a83f.c`](code/fcn.140b5a83f.c)
- [`code/fcn.140b69b30.c`](code/fcn.140b69b30.c)
- [`code/fcn.140b71340.c`](code/fcn.140b71340.c)
- [`code/fcn.140bb0058.c`](code/fcn.140bb0058.c)
- [`code/fcn.140bb84c0.c`](code/fcn.140bb84c0.c)
- [`code/fcn.140bb855d.c`](code/fcn.140bb855d.c)
- [`code/fcn.140bb8597.c`](code/fcn.140bb8597.c)
- [`code/fcn.140bb864e.c`](code/fcn.140bb864e.c)
- [`code/fcn.140bb86ff.c`](code/fcn.140bb86ff.c)
- [`code/fcn.140bb87f5.c`](code/fcn.140bb87f5.c)
- [`code/fcn.140bb8839.c`](code/fcn.140bb8839.c)
- [`code/fcn.140bb889b.c`](code/fcn.140bb889b.c)
- [`code/fcn.140c02229.c`](code/fcn.140c02229.c)
- [`code/fcn.140c023b7.c`](code/fcn.140c023b7.c)
- [`code/fcn.140c02421.c`](code/fcn.140c02421.c)
- [`code/fcn.140c024b3.c`](code/fcn.140c024b3.c)
- [`code/fcn.140c02531.c`](code/fcn.140c02531.c)
- [`code/fcn.140c026e8.c`](code/fcn.140c026e8.c)
- [`code/fcn.140c4bcfe.c`](code/fcn.140c4bcfe.c)
- [`code/fcn.140c4be63.c`](code/fcn.140c4be63.c)
- [`code/fcn.140c4bf5d.c`](code/fcn.140c4bf5d.c)
- [`code/fcn.140c4c065.c`](code/fcn.140c4c065.c)
- [`code/fcn.140c4c0fc.c`](code/fcn.140c4c0fc.c)
- [`code/fcn.140c4c1a0.c`](code/fcn.140c4c1a0.c)
- [`code/fcn.140c93d92.c`](code/fcn.140c93d92.c)
- [`code/fcn.140c93ea9.c`](code/fcn.140c93ea9.c)
- [`code/fcn.140c93f16.c`](code/fcn.140c93f16.c)
- [`code/fcn.140c94052.c`](code/fcn.140c94052.c)
- [`code/fcn.140d77252.c`](code/fcn.140d77252.c)
- [`code/fcn.140d806a0.c`](code/fcn.140d806a0.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C pseudocode, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The code appears to be a **highly obfuscated packer or protector** (e.g., similar in nature to VMProtect or Themida). The primary purpose of this specific section of the code is not "payload" execution but rather the **unpacking, decryption, and de-obfuscation** of the actual malicious payload.

The frequent calls to shared utility functions (like `fcn.140b533b8`) suggest a modular design where one layer of protection decodes another. The code is designed to hinder static analysis by making it difficult for a researcher to follow the logical flow or identify the underlying commands.

### Suspicious and Malicious Behavs
*   **Heavy Obfuscation & Anti-Analysis:**
    *   The presence of many **"Bad instruction - Truncating"** warnings indicates the use of junk code, opaque predicates, or "overlapping instructions" (where a jump targets the middle of an instruction) to break disassemblers and decompilers.
    *   Functions like `fcn.140c93d92` and `fcn.140c026e8` use complex bitwise logic and arithmetic just to calculate the next memory address for a jump, which is a common way to hide the program's true control flow.
*   **Indirect Branching/Jump Tables:**
    *   Several functions end in "indirect jumps" or have "unrecovered jump tables." This technique prevents linear analysis because the "next" instruction is determined at runtime based on calculations, making it difficult to trace the execution path statically.
*   **Software Interrupts (SWI):** 
    *   The presence of `swi(0x9b)` in `fcn.140c026e8` is highly suspicious for standard Windows applications; this is often used as a custom exception handler to redirect execution flow or detect the presence of debuggers/emulators.

### Notable Techniques and Patterns
*   **Arithmetic Obfuscation:** Functions like `fcn.140c4c065` and `fcn.140c4bcfe` contain complex math (e.g., `((uVar1 & 1) != 0) << 0x1f`) to calculate offsets or keys. This is likely used for decrypting data in memory or decoding the next stage of the packer.
*   **Bit-Swapping/Shuffling:** Function `fcn.140c94052` uses a series of bitwise shifts and ORs (`uVar3 = ~((uVar1 | uVar2 * 0x20000000) >> 0x18 ...`). This is a common technique to hide constants or modify instruction bytes in memory so that they do not appear as recognizable signatures.
*   **Virtualization-like Behavior:** The complexity of `fcn.140d77252` (with large arrays and jump tables) suggests the use of a **VM-based protection engine**. This technique converts x86 instructions into a custom "bytecode" that is executed by an internal virtual machine, making reverse engineering extremely difficult.
*   **Control Flow Flattening:** The constant jumping to common logic blocks (like `fcn.140b533b8`) suggests the code has been flattened, meaning all logical branches are collapsed into a single loop with a switch-like dispatcher.

### Summary for Analyst
This sample contains highly sophisticated anti-analysis protections characteristic of **advanced malware packers**. The binary is likely wrapping a malicious payload (such as a Trojan or Ransomware). Because of the heavy obfuscation and VM-style protection, manual analysis will require significant effort to reach the "OEP" (Original Entry Point) where the actual malicious functionality begins.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of junk code, opaque predicates, and complex arithmetic to hide logic/instructions is a classic implementation of this technique. |
| **T1027** | Obfuscated Files or Information | Control flow flattening and the use of indirect jumps are specific methods used to complicate static analysis and hide the execution path. |
| **T1027** | Obfuscated Files or Information | The "Virtualization-like" behavior (custom bytecode/VM protection) is a high-level obfuscation method to hide the original instructions. |
| **T1027** | Obfuscated Files or Information | The use of bit-swapping and arithmetic for decryption and de-obfuscation of the payload indicates efforts to mask malicious functionality before execution. |
| **T1027** | Obfuscated Files or Information | The use of specific software interrupts (SWI) to detect debuggers/emulators is a form of obfuscation used to hinder analysis tools. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The "Extracted Strings" section contains highly obfuscated/encrypted data typical of a packer. Because the payload is currently packed/encrypted, no standard network indicators (IPs, URLs) or filesystem artifacts were revealed in the raw strings.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: Strings like `.rdata` and `.data` are standard PE section headers and are excluded as false positives).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Anti-Debugging Signature:** `swi(0x9b)` (Software Interrupt used to detect debuggers or redirect flow).
*   **Internal Function Offsets (Packer Signatures):** 
    *   `fcn.140b533b8`
    *   `fcn.140c93d92`
    *   `fcn.140c026e8`
    *   `fcn.140c4c065`
    *   `fcn.140c4bcfe`
    *   `fcn.140c94052`
    *   `fcn.140d77252`
*   **Behavioral Patterns:** 
    *   Control Flow Flattening.
    *   VM-based protection engine (indicative of VMProtect or Themida).
    *   Instruction overlapping/junk code usage.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**: 
    * **Protector/Packer Behavior:** The analysis explicitly identifies the sample as a highly obfuscated packer or protector (similar to VMProtect), where the primary function is to decrypt and de-obfuscate a hidden payload rather than executing malicious actions itself.
    * **Advanced Anti-Analysis:** The presence of "Virtualization-like" behavior, control flow flattening, and junk code/opaque predicates are hallmark indicators of a loader designed to shield an underlying payload from automated analysis.
    * **Lack of Direct Malicious Payload:** No specific network indicators or file system modifications were found in the initial stage because the core malicious functionality is still wrapped within multiple layers of protection.
