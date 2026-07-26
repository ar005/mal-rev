# Threat Analysis Report

**Generated:** 2026-07-24 14:54 UTC
**Sample:** `0a11983b15d1fcf62e637cb7c2ad185baf8cb124a7973ce616e25000fe64bb3f_0a11983b15d1fcf62e637cb7c2ad185baf8cb124a7973ce616e25000fe64bb3f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a11983b15d1fcf62e637cb7c2ad185baf8cb124a7973ce616e25000fe64bb3f_0a11983b15d1fcf62e637cb7c2ad185baf8cb124a7973ce616e25000fe64bb3f.exe` |
| File type | PE32+ executable for MS Windows 4.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 388,392 bytes |
| MD5 | `48849d56104dc8bf61e8433321bdd4af` |
| SHA1 | `84472749a9062d6e4483919c056f9d676ed18f1f` |
| SHA256 | `0a11983b15d1fcf62e637cb7c2ad185baf8cb124a7973ce616e25000fe64bb3f` |
| Overall entropy | 7.611 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3514513013 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 358,400 | 7.69 | ⚠️ Yes |
| `.rsrc` | 17,408 | 3.952 | No |

## Extracted Strings

Total strings found: **1817** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc

	,^	

*.rb

	,1	ov
	,rR
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADP_
.*Dc]r%^
#RxC0G
2%E<1$
@J(I\
[IDATx
<wL&*?o
qZd8P<
i}tMl{
ejOm|k
47#&r0
q7cDk[
B-pqt;@3
z:Cs:v$
H`-1(eS
}A3{&N
d)3O=

6~9Ai
5F.c;5	
2SWl*.
S'HRm'I
i]mk0D
hI`($p
spdU"
,IOKg.


0 vR
t,t.D.
e3v;P4
	[j^6sgY
w48S;9
mK9d.
NG?C,q
3ERjJTX
~oNFv(
8Z#]G,
R`8@i
)0,<\&W
>!+e2
oEyBIXhO
P[^3GM
5X7uM3I
82Lt!+}	DvF
6A[DGC
M	3@rP!
Y%]uM~
WK$FG
zh]1u#
!Jk&N<IQ
k]dS*J
,QH`X/
]k}Dw|
;~FB.rk%
YKj!QI$W
(D0g$N
I_/GjJ
S.s]
18{lHi4
XV+e
0
hR>jIj<
(.R^3
\''X{U 
QP`/
eK}y`$3
8_W>rN
vDEw_o
Yg;P#
9*v7GXF
@Z\@G\Y3[
u*:SL#_$
_Kp,S`
i3EAl$
28'0&b
j:'q7	
S;L=@Jk8
QZ`Eof
.6: h
XhewY=x
-9a x#
(hV:i&lL9$
0CvG?C|0
8`	aN$
vNr$J5
ax+^c@
},Omyy
dd_fG
fNSbCU
.M$>0Q
_f6-KQ
'e}O6[5
@&k6`
jS
w>jXv
$*SH"n)Y
PlthNP
```

## Disassembly Overview

Functions analyzed: **11** | Decompiled to C: **11**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Uninstall.App.Application_Startup` | `0x402048` | 282492 | ✓ |
| `entry0` | `0x40213f` | 279488 | ✓ |
| `method.Uninstall.Properties.Settings..cctor` | `0x40215d` | 65506 | ✓ |
| `method.Uninstall.Properties.Settings.get_Default` | `0x40214e` | 65274 | ✓ |
| `method.Uninstall.App.Main` | `0x4020f0` | 86 | ✓ |
| `method.Uninstall.Properties.Resources.get_ResourceManager` | `0x402113` | 44 | ✓ |
| `method.Uninstall.App.InitializeComponent` | `0x4020dc` | 20 | ✓ |
| `method.Uninstall.App..ctor` | `0x402103` | 8 | ✓ |
| `method.Uninstall.Properties.Resources..ctor` | `0x40210b` | 8 | ✓ |
| `method.Uninstall.Properties.Resources.set_Culture` | `0x402146` | 8 | ✓ |
| `method.Uninstall.Properties.Settings..ctor` | `0x402155` | 8 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Uninstall.App..ctor.c`](code/method.Uninstall.App..ctor.c)
- [`code/method.Uninstall.App.Application_Startup.c`](code/method.Uninstall.App.Application_Startup.c)
- [`code/method.Uninstall.App.InitializeComponent.c`](code/method.Uninstall.App.InitializeComponent.c)
- [`code/method.Uninstall.App.Main.c`](code/method.Uninstall.App.Main.c)
- [`code/method.Uninstall.Properties.Resources..ctor.c`](code/method.Uninstall.Properties.Resources..ctor.c)
- [`code/method.Uninstall.Properties.Resources.get_ResourceManager.c`](code/method.Uninstall.Properties.Resources.get_ResourceManager.c)
- [`code/method.Uninstall.Properties.Resources.set_Culture.c`](code/method.Uninstall.Properties.Resources.set_Culture.c)
- [`code/method.Uninstall.Properties.Settings..cctor.c`](code/method.Uninstall.Properties.Settings..cctor.c)
- [`code/method.Uninstall.Properties.Settings..ctor.c`](code/method.Uninstall.Properties.Settings..ctor.c)
- [`code/method.Uninstall.Properties.Settings.get_Default.c`](code/method.Uninstall.Properties.Settings.get_Default.c)

## Behavioral Analysis

Based on my analysis of the provided disassembly and string data, here is the report on the behavior of this binary:

### Core Functionality and Purpose
The binary appears to be a **highly obfuscated .NET assembly**. While the underlying logic is intentionally hidden by an obfuscator (such as ConfuserEx or a similar packer), several indicators suggest its purpose:
*   **Obfuscated Execution:** The decompiler frequently reports "Control flow encountered bad instruction data" and "halt_baddata." This indicates that the actual malicious instructions are wrapped in a layer of junk code, "spaghetti" jumps, or encryption.
*   **Misleading Naming:** Functions like `method.Uninstall.App` suggest the binary may masquerade as an "Uninstaller" to blend in with system processes or to provide a plausible excuse for its presence on a victim's machine.

### Suspicious and Malicious Behaviors
While the raw logic is obscured, the following characteristics are highly indicative of malicious intent:
*   **Anti-Analysis Techniques:** The primary behavior observed is **anti-analysis through obfuscation**. By using complex mathematical loops (seen in `get_Default`) to perform simple arithmetic, the author is attempting to break automated decompilers and frustrate manual reverse engineering.
*   **Evasive Packing/Obfuscation:** The presence of "junk" instructions that cause the decompiler to stop ("halt_baddata") suggests a packer or an obfuscator has been used to hide the true functionality (e.g., command-and-control communication, credential theft, or file encryption).
*   **Encrypted Payload Indicators:** The string dump contains large blocks of high-entropy, non-human-readable data. These are typically indicators of encrypted payloads, configuration files, or additional malicious modules that will be unpacked into memory during execution.

### Notable Techniques and Patterns
*   **Control Flow Flattening / Junk Code Insertion:** The `get_Default` and `entry0` functions show a high volume of bit-shifting (`>> 0x20`) and complex arithmetic using large constants (e.g., `0x8762b70`). This is a common technique to hide the real logic path from analysts by making it difficult for tools to determine what the code actually does.
*   **Standard .NET Framework Usage:** The inclusion of `mscorlib` and `System.Resources.ResourceReader` confirms this is a .NET application, which is commonly used in malware because it allows developers to write complex logic easily, which can then be "packed" to hide the final malicious functionality.
*   **Instruction Overlap/Complexity:** The warning regarding overlapping instructions at specific memory locations (`0x40218d`) and the use of `swi(0)` (software interrupt) suggest that the code is designed to behave inconsistently or crash if a debugger attempts to step through it linearly.

### Summary
This sample is likely a **malicious loader** for a .NET-based threat. It uses professional-grade obfuscation to hide its true intent, which may include secondary payloads. The "Uninstall" naming convention suggests an attempt to evade detection by the user and during initial triage.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of junk code, control flow flattening, "swi(0)" interrupts, and high-entropy data blocks are clear indicators of attempts to hide the payload's true functionality from automated tools and human analysts. |
| **T1036** | Masquerading | The naming of functions like `method.Uninstall.App` is a deliberate attempt to mimic legitimate system behavior (an uninstaller) to evade detection during initial triage. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The high-entropy character strings do not contain recognizable URL patterns or IP addresses.)

### **File paths / Registry keys**
*   *None identified.* (While "method.Uninstall.App" was mentioned in the report, it is a method name within the assembly rather than a file path on a filesystem.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Application Masquerading:** The binary utilizes the naming convention `method.Uninstall.App`, indicating an attempt to masquerade as a system uninstaller to evade detection.
*   **Obfuscation Tooling:** The presence of "junk" instructions and complex mathematical loops (e.g., bit-shifting with constants like `0x8762b70`) indicates the use of a packer or obfuscator such as **ConfuserEx**.
*   **Runtime Environment:** The sample is identified as a **.NET assembly** utilizing `mscorlib` and `System.Resources.ResourceReader`.
*   **High Entropy/Encrypted Payload:** Large blocks of non-human-readable data in the string dump indicate an encrypted payload or configuration file waiting to be unpacked into memory.

---
**Analyst Note:** This sample appears to be a **malicious loader**. Because it is heavily obfuscated and packed, many traditional "static" IOCs (like cleartext IPs and file paths) are hidden within the layers of encryption. Further dynamic analysis (sandbox execution) would be required to extract active C2 infrastructure.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**: 
*   **Sophisticated Obfuscation:** The binary is a .NET assembly utilizing advanced techniques such as control flow flattening, junk code insertion, and "swi(0)" interrupts to hinder de-compilation and analysis.
*   **Intentional Masquerading:** The inclusion of the `method.Uninstall.App` naming convention demonstrates a deliberate attempt to hide in plain sight by mimicking legitimate system components.
*   **Payload Delivery Indicators:** The presence of high-entropy data blocks combined with "loader" behavior suggests the binary's primary purpose is to decrypt and execute a secondary, hidden payload (such as a RAT or infostealer).
