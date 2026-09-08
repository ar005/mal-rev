# Threat Analysis Report

**Generated:** 2026-09-05 17:49 UTC
**Sample:** `1486ea9dac80ac5155e8ba011e577834043118f2079e586dca7ae3d7e5b738fd_1486ea9dac80ac5155e8ba011e577834043118f2079e586dca7ae3d7e5b738fd.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1486ea9dac80ac5155e8ba011e577834043118f2079e586dca7ae3d7e5b738fd_1486ea9dac80ac5155e8ba011e577834043118f2079e586dca7ae3d7e5b738fd.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 18 sections |
| Size | 11,325,456 bytes |
| MD5 | `01737d88581d76b0332104ad7f07a66b` |
| SHA1 | `13419ec18bf363ab6ee39774707af42dbc32549f` |
| SHA256 | `1486ea9dac80ac5155e8ba011e577834043118f2079e586dca7ae3d7e5b738fd` |
| Overall entropy | 7.96 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774564725 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `        ` | 1,358,336 | 7.984 | ⚠️ Yes |
| `        ` | 6,144 | 7.889 | ⚠️ Yes |
| `        ` | 40,448 | 7.933 | ⚠️ Yes |
| `.bss` | 0 | 0.0 | No |
| `        ` | 1,536 | 6.331 | No |
| `        ` | 1,536 | 7.603 | ⚠️ Yes |
| `        ` | 512 | 1.632 | No |
| `.tls` | 0 | 0.0 | No |
| `        ` | 512 | 1.744 | No |
| `        ` | 214,528 | 7.954 | ⚠️ Yes |
| `        ` | 31,232 | 7.969 | ⚠️ Yes |
| `.edata` | 512 | 1.329 | No |
| `.idata` | 1,024 | 4.104 | No |
| `.tls` | 512 | 0.144 | No |
| `.rsrc` | 12,800 | 4.458 | No |
| `.themida` | 0 | 0.0 | No |
| `.boot` | 9,654,272 | 7.95 | ⚠️ Yes |
| `.reloc` | 16 | 2.475 | No |

### Imports

**kernel32.dll**: `GetModuleHandleA`
**winspool.drv**: `DocumentPropertiesW`
**comctl32.dll**: `ImageList_GetImageInfo`
**shell32.dll**: `Shell_NotifyIconW`
**user32.dll**: `CopyImage`
**version.dll**: `GetFileVersionInfoSizeW`
**oleaut32.dll**: `SafeArrayPutElement`
**WTSAPI32.DLL**: `WTSUnRegisterSessionNotification`
**advapi32.dll**: `RegSetValueExW`
**msvcrt.dll**: `isupper`
**winhttp.dll**: `WinHttpGetIEProxyConfigForCurrentUser`
**SHFolder.dll**: `SHGetFolderPathW`
**wsock32.dll**: `WSAStartup`
**ole32.dll**: `IsEqualGUID`
**shcore.dll**: `SetProcessDpiAwareness`
**gdi32.dll**: `Pie`

### Exports

`__dbk_fcall_wrapper`, `dbkFCallWrapperAddr`

## Extracted Strings

Total strings found: **24282** (showing first 100)

```
This program must be run under Win32
$7
        4f9
`        
`        
        
        
        s
        ]
@        
@        
@.edata
@.idata
@.themida
`.reloc
~!7a9$
K>9^[A
I=P/`C
O`II:\E
f{A]CNPY
d@H=(
4-^`p|
suF@nb	
^HVC]`
9N}TQ5
Yp\0wdC
+>hiW.%
4+6FNy
`0PD!K
L(G_	"
#yKXP\<
;S=uO[
6I1I^`
sIA8k!
Ou*h{>
Dv!F[#X
ZSrc{j
W~A!]I
+NVB~cK|
E0i%|!
RjXy;%b
*;103+
@zbAS{%c
}9a5(&
:9BtHf
Bs<^^c5
:H_7A

qE_?U/
\zL0)=
sAcjtU
5`	:s!{
y~)q@\
4L<P	]T
el_M}og
tE3 }s)
 q|:,|
}<2:~A
l/Ol!`

Q6K:r
4OLmE4
St)=#

7JzLRM
g]cf8@
E|p]"z
I\uJ{G
2JU(;
KOD[3 zW@o
)mA HA	V
aW*'gN
Eb('-0Z
B#Wu9_0
 -3(i}
+"	kv[H
Um.s9J
o05|r
ZBZ@OnY
,mR&|J
	9>0f{5
JN=Y.;
 ]
8ip
?d/()
5C` 0o
el+@er.
A4	ZP
9L>~ id.
5`h1{0
Hqcp8^9
8U*K`
&e;,OE
5<1oJDv
D@YV/R
tecT)J
f	,hJN
KOeI 
8{Kq0A-
D#OM`	
*bK#Nx
AzMGq	
M{f UBX
Dg<:5

Xth]/
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **28**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.01ef1625` | `0x1ef1625` | 716 | ✓ |
| `fcn.01715ea3` | `0x1715ea3` | 662 | ✓ |
| `fcn.01db9fb8` | `0x1db9fb8` | 622 | ✓ |
| `int.019d157e` | `0x19d157e` | 548 | ✓ |
| `int.01ac8591` | `0x1ac8591` | 525 | ✓ |
| `fcn.0042d389` | `0x42d389` | 514 | ✓ |
| `fcn.01ebac55` | `0x1ebac55` | 507 | ✓ |
| `fcn.01e3128b` | `0x1e3128b` | 477 | ✓ |
| `fcn.01b830d1` | `0x1b830d1` | 462 | ✓ |
| `fcn.01af6fea` | `0x1af6fea` | 438 | ✓ |
| `fcn.0051983f` | `0x51983f` | 436 | ✓ |
| `fcn.01c59551` | `0x1c59551` | 422 | ✓ |
| `fcn.004cea25` | `0x4cea25` | 402 | ✓ |
| `fcn.01eb5361` | `0x1eb5361` | 400 | — |
| `fcn.017f0830` | `0x17f0830` | 369 | ✓ |
| `fcn.01aa0974` | `0x1aa0974` | 365 | ✓ |
| `fcn.01c2ae62` | `0x1c2ae62` | 362 | ✓ |
| `int.01c985fc` | `0x1c985fc` | 360 | ✓ |
| `fcn.01ebdc59` | `0x1ebdc59` | 343 | — |
| `fcn.01dc84bf` | `0x1dc84bf` | 343 | ✓ |
| `entry0` | `0x15da058` | 336 | ✓ |
| `fcn.01da0a5a` | `0x1da0a5a` | 333 | ✓ |
| `fcn.01c4ec77` | `0x1c4ec77` | 331 | ✓ |
| `fcn.016999eb` | `0x16999eb` | 323 | ✓ |
| `fcn.01ca7f25` | `0x1ca7f25` | 321 | ✓ |
| `int.019e4a7c` | `0x19e4a7c` | 318 | ✓ |
| `fcn.00447318` | `0x447318` | 317 | ✓ |
| `fcn.01e2ebc0` | `0x1e2ebc0` | 314 | ✓ |
| `fcn.01632afc` | `0x1632afc` | 302 | ✓ |
| `int.01b435f1` | `0x1b435f1` | 287 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0042d389.c`](code/fcn.0042d389.c)
- [`code/fcn.00447318.c`](code/fcn.00447318.c)
- [`code/fcn.004cea25.c`](code/fcn.004cea25.c)
- [`code/fcn.0051983f.c`](code/fcn.0051983f.c)
- [`code/fcn.01632afc.c`](code/fcn.01632afc.c)
- [`code/fcn.016999eb.c`](code/fcn.016999eb.c)
- [`code/fcn.01715ea3.c`](code/fcn.01715ea3.c)
- [`code/fcn.017f0830.c`](code/fcn.017f0830.c)
- [`code/fcn.01aa0974.c`](code/fcn.01aa0974.c)
- [`code/fcn.01af6fea.c`](code/fcn.01af6fea.c)
- [`code/fcn.01b830d1.c`](code/fcn.01b830d1.c)
- [`code/fcn.01c2ae62.c`](code/fcn.01c2ae62.c)
- [`code/fcn.01c4ec77.c`](code/fcn.01c4ec77.c)
- [`code/fcn.01c59551.c`](code/fcn.01c59551.c)
- [`code/fcn.01ca7f25.c`](code/fcn.01ca7f25.c)
- [`code/fcn.01da0a5a.c`](code/fcn.01da0a5a.c)
- [`code/fcn.01db9fb8.c`](code/fcn.01db9fb8.c)
- [`code/fcn.01dc84bf.c`](code/fcn.01dc84bf.c)
- [`code/fcn.01e2ebc0.c`](code/fcn.01e2ebc0.c)
- [`code/fcn.01e3128b.c`](code/fcn.01e3128b.c)
- [`code/fcn.01ebac55.c`](code/fcn.01ebac55.c)
- [`code/fcn.01ef1625.c`](code/fcn.01ef1625.c)
- [`code/int.019d157e.c`](code/int.019d157e.c)
- [`code/int.019e4a7c.c`](code/int.019e4a7c.c)
- [`code/int.01ac8591.c`](code/int.01ac8591.c)
- [`code/int.01b435f1.c`](code/int.01b435f1.c)
- [`code/int.01c985fc.c`](code/int.01c985fc.c)

## Behavioral Analysis

The following is an updated and expanded analysis based on the second chunk of disassembly provided.

### Updated Analysis of Binary Sample (Chunk 2/2)

#### Core Functionality and Purpose
The analysis confirms that this binary is protected by a **sophisticated, high-end packer or protector** (likely similar to VMProtect or Themida). The complexity of the code in Chunk 2 reinforces the conclusion that the primary objective of this section is not application logic, but rather:
*   **Multi-stage Decryption:** Complex loops and arithmetic are used to peel away layers of encryption from the actual payload.
*   **Execution Flow Obfuscation:** Extensive use of "junk code," overlapping instructions, and opaque predicates are designed to break automated analysis tools (like IDA’s Hex-Rays decompiler).
*   **Anti-Debugging/Analysis Triggers:** The presence of `swi` (Software Interrupt) calls suggests the packer may trigger intentional exceptions to redirect execution or detect the presence of a debugger.

#### Suspicious or Malicious Behaviors
*   **Advanced Instruction Overlapping & "Bad Instructions":** The repeated warnings about overlapping instructions (e.g., at `0x1dc85c0` and `0x1da0a5d`) are a deliberate technique to mislead disassemblers. By placing valid jump targets inside what the tool thinks is the middle of an instruction, the packer ensures that only the correct runtime path is executable, while the "junk" paths remain undecipherable.
*   **Opaque Predicates & Junk Logic:** Functions like `fcn.01632afc` and `fcn.01e2ebc0` contain complex mathematical operations (using things like `POPCOUNT`, `SCARRY4`, and large hex constants) that ultimately resolve to simple booleans or constants. These are used to create "fake" branches, forcing an analyst to manually trace hundreds of lines of code that have no impact on the final result.
*   **Sophisticated Decoding Loops:** The sheer size and complexity of `fcn.01632afc` and `fcn.01e2ebc0` suggest these are primary "unpacking" loops. They likely process data in blocks, using multi-layered logic to decrypt the next stage of the code into memory.
*   **Anti-Analysis Tactics (Soft/Hard):** 
    *   **Swi Triggers:** The `swi(1)`, `swi(4)` instructions are often used as "hooks" for custom exception handlers that bypass standard debugger protections or jump to different, hidden code paths.
    *   **Do-Nothing Loops:** The presence of loops that appear to do nothing (or have very simple iterations) at the end of functions is a common way to waste an analyst's time during manual stepping.

#### Notable Techniques and Patterns
*   **Advanced Instruction Set Utilization:** The use of **AVX instructions** (`vpsrld_avx` in `fcn.01c4ec77`) indicates that the packer is designed for modern hardware and can perform high-speed, parallelized decryption or transformation of data blocks.
*   **Arithmetic Complexity as Obfuscation:** Simple increments are replaced with complex arithmetic involving multiple constants (e.g., `uVar2 = uVar1 & 0x8ce864b9` followed by calculations that ultimately only affect a single bit). This is intended to make the "math" of the decryption look like a proprietary or complex algorithm.
*   **Control-Flow Flattening:** The logic in many functions appears highly non-linear, with multiple jumps and indirect calls (like `swi(3)` followed by an immediate call), characteristic of modern protectors that flatten the original code's control flow into a "hub-and-spoke" model.
*   **Stack Management Manipulation:** Some functions show complex stack management that appears to be obfuscated, making it harder for a researcher to track where variables are being stored or how the stack frame is changing.

---

### Summary for Analysis Report (Updated)

*   **Classification:** **Highly Sophisticated Packer/Protector.**
*   **Primary Techniques:** 
    *   **Instruction Overlapping:** Intentional "bad instructions" used to desynchronize disassemblers and hide true jump targets.
    *   **Opaque Predicates:** Complex arithmetic logic used to create fake execution paths.
    *   **Multi-Stage Unpacking:** Large, complex loops designed for iterative decryption of the primary payload.
    *   **Advanced Instruction Usage:** Utilization of AVX sets for high-speed data processing.
*   **Risk Level:** **High.** The complexity suggests a professional-grade protection layer often used by sophisticated threat actors to shield malware from automated and manual analysis.
*   **Note to Analyst:** This binary is intentionally designed to be "un-analyzable" via static means. Manual deconstruction of these functions will yield very little information about the ultimate payload (e.g., command-and-control, data theft). 
    *   **Recommended Action:** Do not attempt to reverse the packer's logic manually. Instead, focus on **dynamic analysis**: run the sample in a controlled environment and use memory forensics/scanners at multiple intervals to identify the point where the "real" payload is decrypted into memory (the Original Entry Point - OEP). Once unpacked, dump the process memory for a secondary analysis of the actual malicious logic.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of complex packing, instruction overlapping, and opaque predicates is specifically designed to hinder static analysis and hide the malicious payload's logic. |
| T1497 | Virtualized Environment Detection | The inclusion of `swi` instructions as anti-analysis triggers suggests a mechanism to detect debuggers or non-standard environments during execution. |
| T1027 | Obfuscated Files or Information | (Note: Covers "Control-Flow Flattening") The transformation of linear code into a non-linear, "hub-and-spoke" model is a signature method used to complicate manual reverse engineering. |

***

**Analyst Notes:**
*   **T1027 (Obfuscated Files or Information)** covers the majority of the observed behaviors: the packer's complexity, the multi-stage decryption loops, and the use of "junk" code/logic to waste an analyst's time.
*   The **`swi`** instructions are a classic indicator of anti-debugging/anti-instrumentation logic; while T1497 specifically targets virtualized environments, it is the standard mapping for automated evasion detection in these contexts.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The provided text contains significant amounts of "noise" and obfuscation techniques typical of advanced packers; therefore, several segments were identified as packer logic rather than direct malicious indicators.

### **IP addresses / URLs / Domains**
*None identified.*

### **File paths / Registry keys**
*None identified.* (Note: Memory addresses such as `0x1dc85c0` and `0x1da0a5d` were noted in the analysis, but these are internal execution offsets and do not constitute standard file system or registry IOCs.)

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None identified.*

### **Other artifacts**
*   **Packer/Protector Identification:** 
    *   **Themida**: Identified via the string `@.themida`. This indicates the use of a high-end protector to obfuscate the actual malicious payload.
    *   **VMProtect**: Mentioned in behavioral analysis as a similar threat actor preference for protection.
*   **Anti-Analysis Techniques:** 
    *   **Instruction Overlapping:** Used to desynchronize disassemblers.
    *   **Opaque Predicates:** Use of complex math (e.g., `POPCOUNT`, `SCARRY4`) to create fake execution branches.
    *   **Control-Flow Flattening:** Non-linear logic used to hide the original program's flow.
    *   **Swi Triggers:** Utilization of `swi(1)`, `swi(3)`, and `swi(4)` as hooks for custom exception handlers to bypass debuggers.
    *   **AVX Instruction Utilization:** Use of `vpsrld_avx` for high-speed data processing/decryption.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: Unknown (Packer-protected)
2. **Malware type**: Loader / Dropper
3. **Confidence**: High (Regarding its role as a protector/loader; Low regarding the ultimate payload's identity)
4. **Key evidence**:
    *   **Advanced Packing & Protection:** The sample is confirmed to use high-end protectors (Themida and potentially VMProtect), which are industry standards for hiding malicious payloads from static analysis.
    *   **Sophisticated Obfuscation Techniques:** The presence of instruction overlapping, opaque predicates, and control-flow flattening indicates a professional effort to bypass both automated tools and manual reverse engineering.
    *   **Anti-Analysis Mechanisms:** The use of `swi` (Software Interrupt) hooks and junk code logic is specifically designed to detect debuggers and hinder the analysis of the "real" payload which only exists in memory after decryption.
