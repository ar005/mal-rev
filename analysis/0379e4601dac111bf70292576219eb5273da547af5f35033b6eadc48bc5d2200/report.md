# Threat Analysis Report

**Generated:** 2026-06-30 19:22 UTC
**Sample:** `0379e4601dac111bf70292576219eb5273da547af5f35033b6eadc48bc5d2200_0379e4601dac111bf70292576219eb5273da547af5f35033b6eadc48bc5d2200.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0379e4601dac111bf70292576219eb5273da547af5f35033b6eadc48bc5d2200_0379e4601dac111bf70292576219eb5273da547af5f35033b6eadc48bc5d2200.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 9 sections |
| Size | 11,872,256 bytes |
| MD5 | `f9a01a72fe2377fd4d0b4f81f1a414bc` |
| SHA1 | `654b77bdff56109d11c92457e48471e40dab2a8a` |
| SHA256 | `0379e4601dac111bf70292576219eb5273da547af5f35033b6eadc48bc5d2200` |
| Overall entropy | 7.977 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774968494 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 0 | 0.0 | No |
| `.rdata` | 0 | 0.0 | No |
| `.data` | 0 | 0.0 | No |
| `.pdata` | 0 | 0.0 | No |
| `.00cfg` | 0 | 0.0 | No |
| `.tls` | 0 | 0.0 | No |
| `.vmp0` | 0 | 0.0 | No |
| `.vmp1` | 11,870,720 | 7.977 | ⚠️ Yes |
| `.reloc` | 512 | 2.19 | No |

### Imports

**msvcrt.dll**: `__C_specific_handler`
**KERNEL32.dll**: `LocalAlloc`, `LocalFree`, `GetModuleFileNameW`, `GetProcessAffinityMask`, `SetProcessAffinityMask`, `SetThreadAffinityMask`, `Sleep`, `ExitProcess`, `FreeLibrary`, `LoadLibraryA`, `GetModuleHandleA`, `GetProcAddress`
**WTSAPI32.dll**: `WTSSendMessageW`
**USER32.dll**: `GetProcessWindowStation`, `GetUserObjectInformationW`

## Extracted Strings

Total strings found: **24608** (showing first 100)

```
!This program cannot be run in DOS mode.$
`.rdata
@.data
.pdata
@.00cfg
`.vmp1
h.reloc
PuDEBe
A*4/{2	
sgUmN<
GqP?*V
jtcoH|
5;h<X
 u@{I$
;c4z8E
Vz~G_;
(ZqQY
':dy%K
s@"%Xc
WEgioW
WwK^
z
:+CtA&#
?Sj'ww+
Sxy92l
Z(TQ<s
wzci$?
Bvmxe6
Jpa@,Z
V?CWGCQ
u7DER?l
a5q
nw,gL
ams9
6&
8$&2n(
	


O
_
TLSYz\d(Qz
WuzFkS
??Ys{1
S^e3;|9
qGMiEur
Ik!%rG
[%7IB_(
m5sJBi]
h9%@GC
45:
5
wlW	Q
XzoWpPz
'2X2vk
;R",vd
(Ynbm"
WTSAPI32.dll
l!L%jR
l!Cw!{`
fR,Yd3
ZKz!fL
MOCP q

3_%.*Q
GetSystemTimeAsFileTime
` ''np
/7Dz
s
YB4MiL
,/s=3
`iEOZHC
Zjqz#O
6wg3u|
FBG,+X}
F}# 8$
^FQUz&~*]z
wx^McvjK
>7]Dmv
UY1|Zz`
:"[XzR* Pz
&Gzi}`uz
4,!hq)q
ppmNV];
WdN*=\
aE[*.tt
]zUtUzU
S!zI5g
$
OKz{
nR=
b-E|
muhg{?_
:qs1Lh
 s[VTi
ad?uQy
Pj^Umb

Io)!30
{aAULM
PKrO[q:h
y-* 73
aY_HG[.
tWR2aI
(zbqql
~1~n29
e1W^	>W
<^N~/2

mx7F3
regm
Qe
,mMuQ/e
,qpVOs
?>r0ue
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.141a13339` | `0x141a13339` | 3277259 | ✓ |
| `fcn.141aab72d` | `0x141aab72d` | 1180383 | ✓ |
| `fcn.141b22f7d` | `0x141b22f7d` | 1057179 | ✓ |
| `fcn.141b2559a` | `0x141b2559a` | 1056155 | ✓ |
| `fcn.141af7ff5` | `0x141af7ff5` | 1046430 | ✓ |
| `fcn.141a2c629` | `0x141a2c629` | 840100 | ✓ |
| `fcn.141a8fbc0` | `0x141a8fbc0` | 740577 | ✓ |
| `fcn.141b0a9e9` | `0x141b0a9e9` | 737615 | ✓ |
| `fcn.141aab3c7` | `0x141aab3c7` | 685907 | ✓ |
| `fcn.141af8c04` | `0x141af8c04` | 674980 | ✓ |
| `fcn.141a87089` | `0x141a87089` | 621508 | ✓ |
| `fcn.141ab91ae` | `0x141ab91ae` | 558661 | ✓ |
| `fcn.141a83915` | `0x141a83915` | 442353 | ✓ |
| `fcn.141ac8795` | `0x141ac8795` | 390067 | ✓ |
| `fcn.14115ba49` | `0x14115ba49` | 357 | ✓ |
| `fcn.1415e5b95` | `0x1415e5b95` | 209 | ✓ |
| `fcn.1419d3bfd` | `0x1419d3bfd` | 190 | ✓ |
| `fcn.1418e06f0` | `0x1418e06f0` | 157 | ✓ |
| `fcn.1416b88e8` | `0x1416b88e8` | 132 | ✓ |
| `fcn.141029837` | `0x141029837` | 131 | ✓ |
| `fcn.1418dbe31` | `0x1418dbe31` | 123 | ✓ |
| `fcn.1419c00dd` | `0x1419c00dd` | 103 | ✓ |
| `fcn.1415471d4` | `0x1415471d4` | 92 | ✓ |
| `fcn.141054058` | `0x141054058` | 83 | ✓ |
| `fcn.14108fb50` | `0x14108fb50` | 68 | ✓ |
| `fcn.14189fe06` | `0x14189fe06` | 48 | ✓ |
| `fcn.141573269` | `0x141573269` | 47 | ✓ |
| `fcn.1418e8566` | `0x1418e8566` | 45 | ✓ |
| `fcn.1417ae5bc` | `0x1417ae5bc` | 43 | ✓ |
| `fcn.14130cf70` | `0x14130cf70` | 38 | ✓ |

### Decompiled Code Files

- [`code/fcn.141029837.c`](code/fcn.141029837.c)
- [`code/fcn.141054058.c`](code/fcn.141054058.c)
- [`code/fcn.14108fb50.c`](code/fcn.14108fb50.c)
- [`code/fcn.14115ba49.c`](code/fcn.14115ba49.c)
- [`code/fcn.14130cf70.c`](code/fcn.14130cf70.c)
- [`code/fcn.1415471d4.c`](code/fcn.1415471d4.c)
- [`code/fcn.141573269.c`](code/fcn.141573269.c)
- [`code/fcn.1415e5b95.c`](code/fcn.1415e5b95.c)
- [`code/fcn.1416b88e8.c`](code/fcn.1416b88e8.c)
- [`code/fcn.1417ae5bc.c`](code/fcn.1417ae5bc.c)
- [`code/fcn.14189fe06.c`](code/fcn.14189fe06.c)
- [`code/fcn.1418dbe31.c`](code/fcn.1418dbe31.c)
- [`code/fcn.1418e06f0.c`](code/fcn.1418e06f0.c)
- [`code/fcn.1418e8566.c`](code/fcn.1418e8566.c)
- [`code/fcn.1419c00dd.c`](code/fcn.1419c00dd.c)
- [`code/fcn.1419d3bfd.c`](code/fcn.1419d3bfd.c)
- [`code/fcn.141a13339.c`](code/fcn.141a13339.c)
- [`code/fcn.141a2c629.c`](code/fcn.141a2c629.c)
- [`code/fcn.141a83915.c`](code/fcn.141a83915.c)
- [`code/fcn.141a87089.c`](code/fcn.141a87089.c)
- [`code/fcn.141a8fbc0.c`](code/fcn.141a8fbc0.c)
- [`code/fcn.141aab3c7.c`](code/fcn.141aab3c7.c)
- [`code/fcn.141aab72d.c`](code/fcn.141aab72d.c)
- [`code/fcn.141ab91ae.c`](code/fcn.141ab91ae.c)
- [`code/fcn.141ac8795.c`](code/fcn.141ac8795.c)
- [`code/fcn.141af7ff5.c`](code/fcn.141af7ff5.c)
- [`code/fcn.141af8c04.c`](code/fcn.141af8c04.c)
- [`code/fcn.141b0a9e9.c`](code/fcn.141b0a9e9.c)
- [`code/fcn.141b22f7d.c`](code/fcn.141b22f7d.c)
- [`code/fcn.141b2559a.c`](code/fcn.141b2559a.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The sample appears to be a **malicious loader or a packed component** (e.g., a "packer" or "downloader"). Its primary role is to hide its true functionality from static analysis by decrypting and resolving system functions at runtime rather than importing them directly via the standard Windows Import Address Table (IAT).

### Suspicious and Malicious Behaviors
*   **Dynamic API Resolution:** Function `fcn.141a13339` is a classic "API Resolver." It manually parses through an internal buffer to find function names, resolves their addresses using `GetModuleHandleA` or `LoadLibraryA`, and then retrieves the memory address of specific functions via `GetProcAddress`.
*   **String Obfuscation:** The code includes a custom decryption loop (using a bitwise shift and XOR/addition logic with the key `0x621b7484`). This is used to decrypt system function names (like "GetProcAddress" or "LoadLibrary") only when they are needed in memory.
*   **Anti-Analysis / Obfuscation:** 
    *   The presence of numerous functions that the decompiler could not resolve into clean logic (e.g., `fcn.141aab3c7`, `fcn.141b2559a`) suggests the use of **junk code** or **control-flow flattening**. These are techniques designed to confuse automated analysis tools and human researchers.
    *   The repeated "WARNING: Control flow encountered bad instruction" notes in several functions indicate that the compiler (or a packer) has intentionally introduced overlapping instructions or "dead" code paths to break decompilation.
*   **Processor Affinity Manipulation:** The extracted strings include `GetProcessAffinityMask` and `SetProcessAffinityMask`. These are often used by malware to pin its execution to specific CPU cores, which can be a technique to evade certain hardware-based monitoring or to hide processing spikes from security software.

### Notable Techniques & Patterns
*   **Custom String Decryption:** Instead of standard encryption, the sample uses a rolling XOR/addition mechanism. This ensures that "plain text" strings never appear in the binary's static files.
*   **Decoy Logic:** The decompiler shows several functions (like `fcn.141aab72d`) that perform complex arithmetic on registers but ultimately do nothing meaningful for the program's execution. This is a common "smoke screen" technique to waste an analyst's time.
*   **Manual Parsing of PE Structures:** The logic in `fcn.141a13339` specifically checks for the `MZ` header and the `PE` signature, suggesting it may be looking at other modules or a secondary payload it intends to "unpack" and execute in memory.

### Summary
This sample is likely a **malware dropper or loader**. It uses high-level obfuscation (encryption of strings, junk code insertion, and complex control flow) to hide its intent from security scanners. Its primary goal is to decrypt its true payload and resolve the necessary Windows APIs at runtime to perform subsequent malicious actions (such as establishing network connections, stealing data, or injecting into other processes).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of custom XOR/addition logic, junk code insertion, and control-flow flattening is intended to hide the sample's true functionality from static analysis. |
| T1602 | Reflective Code Loading | The manual parsing of MZ/PE headers and resolution of APIs at runtime indicate a loader designed to execute a payload in memory without traditional file-on-disk mapping. |
| T1497 | Virtualization/Sandbox Evasion | The manipulation of processor affinity is a technique used to bypass certain hardware-based monitoring systems or evade detection in automated analysis environments. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: Strings such as `.rdata` and `.data` are internal PE section headers, not file system paths.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Packer/Protector Identification:** The string `vmp1` (or `.vmp1`) is a known indicator of the use of **VMProtect**, a common commercial packer used to obfuscate malicious code.
*   **Cryptographic/Decryption Keys:** The analysis identifies a specific hardcoded key used for internal string decryption: `0x621b7484`.
*   **Evasion Techniques:** 
    *   Use of **GetProcessAffinityMask** and **SetProcessAffinityMask** (used to hide execution from hardware-based monitoring).
    *   Implementation of **Control-flow flattening** and **Junk code insertion** (specifically in functions `fcn.141aab3c7` and `fcn.141b2559a`).
    *   **Dynamic API Resolution:** Use of `GetModuleHandleA` and `GetProcAddress` to resolve functions hidden by a custom XOR/addition decryption loop.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Protective Packaging & Obfuscation:** The identification of the `.vmp1` string confirms the use of VMProtect, a commercial packer frequently used to wrap and hide malicious code from automated scanners.
*   **Dynamic API Resolution & Decryption:** The sample uses custom XOR/addition logic for string decryption and `GetProcAddress` for dynamic API resolution, which are hallmark behaviors of a "loader" designed to hide its true functionality until runtime.
*   **Reflective Loading Behavior:** The analysis specifically notes the manual parsing of MZ/PE headers (MITRE T1602), indicating that this component is intended to load and execute an additional payload directly in memory rather than interacting with the file system.
