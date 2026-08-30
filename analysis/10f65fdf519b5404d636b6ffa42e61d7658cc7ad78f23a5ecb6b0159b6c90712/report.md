# Threat Analysis Report

**Generated:** 2026-08-21 20:19 UTC
**Sample:** `10f65fdf519b5404d636b6ffa42e61d7658cc7ad78f23a5ecb6b0159b6c90712_10f65fdf519b5404d636b6ffa42e61d7658cc7ad78f23a5ecb6b0159b6c90712.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10f65fdf519b5404d636b6ffa42e61d7658cc7ad78f23a5ecb6b0159b6c90712_10f65fdf519b5404d636b6ffa42e61d7658cc7ad78f23a5ecb6b0159b6c90712.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 9 sections |
| Size | 24,746,016 bytes |
| MD5 | `716c1da8c517654504cb974a6373da31` |
| SHA1 | `6505f1f0629899e20e7c02ffa2560ed001173f69` |
| SHA256 | `10f65fdf519b5404d636b6ffa42e61d7658cc7ad78f23a5ecb6b0159b6c90712` |
| Overall entropy | 7.869 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1764094580 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 0 | 0.0 | No |
| `.rdata` | 0 | 0.0 | No |
| `.data` | 0 | 0.0 | No |
| `.pdata` | 0 | 0.0 | No |
| `.fptable` | 0 | 0.0 | No |
| `.(Wb` | 0 | 0.0 | No |
| `.xOt` | 4,608 | 0.239 | No |
| `.a?M` | 24,739,840 | 7.869 | ⚠️ Yes |
| `.rsrc` | 512 | 4.788 | No |

### Imports

**KERNEL32.dll**: `HeapAlloc`, `HeapFree`, `ExitProcess`, `GetModuleHandleA`, `LoadLibraryA`, `GetProcAddress`
**USER32.dll**: `ExitWindowsEx`
**GDI32.dll**: `GetCurrentObject`
**ADVAPI32.dll**: `LookupPrivilegeValueW`
**SHELL32.dll**: `ShellExecuteExA`
**ole32.dll**: `CLSIDFromString`
**gdiplus.dll**: `GdipSaveImageToFile`
**WINHTTP.dll**: `WinHttpOpen`
**USERENV.dll**: `UnloadUserProfile`
**WININET.dll**: `InternetCloseHandle`
**urlmon.dll**: `URLDownloadToFileA`
**ntdll.dll**: `NtShutdownSystem`
**WS2_32.dll**: `setsockopt`
**Normaliz.dll**: `IdnToAscii`
**WLDAP32.dll**: `ord_33`
**CRYPT32.dll**: `CertFreeCertificateContext`

## Extracted Strings

Total strings found: **37791** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
h.rsrc
vFjFgg
lW:uz
6s/04-
t&6$P3
>?-)IV
6!K`=!
jf6g2uE
`@ R36
:S7"B/S
)'#;BQ
*JG;+
J&WSAv<*
Z[R:r
'AOO2%
ef<Uj<
H<(}HY8
Beo-`kH+
'3LAP@f8r8
!3.3/3
)BZ	@ 
{
Y}Gj#-
~Ad,gYNJ
];/n*R
eSAEp
#kBEp
/aBEpqO
m8#P3<
_RWmz0
)td,&w
f$I+0%
<Mk@e
7,YdsP
-}RMYR
s@f!SW>
#qr-3d
zvm) o
5Nd	(J
nCH
FO
iE&qX"
V~7 ;K
O(w15+
Ls@`oL
or8d?L
(A5H;w
xC+%b(n>f&
WeB$p>3-b
"Pg-:?
Yb{,*X
$so4VyX
-rz=IE;
Fu*Rg?
;:aM-R
o9tP}9
&(?5]:
;)ELkb
g3vdgf>9
kR-:'Qb
d(YR4j
YwzzF"
0SXc3A8
Ybv+N~
bj3j-K
F80S <H
"9wtu}
:m@88]
FX{E\9lt
ole32.dll
Nef{#
JC
OJV
Nj#2+o
R
x^d=
XqvdnB
?;\Ou	~
(Ry4|M
lCHj8
Pr2EY4
\)K!b]\
VNl7ZP
CreateThread
9AM%c
AQWv{5b
f-M.>p

y|XWQ
4+RQ\N
q*olO*d
fB8:{
|A-]Q>
vo3H;U3{1
$
rWpQ
!^+jAR
,U#qG4
5(ow
M.ZE)	
c~ouU
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **17**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14295039f` | `0x14295039f` | 24337771 | — |
| `fcn.1429bef02` | `0x1429bef02` | 24231487 | ✓ |
| `fcn.1429116f5` | `0x1429116f5` | 24211379 | — |
| `fcn.14299fe92` | `0x14299fe92` | 23893246 | — |
| `fcn.142607d93` | `0x142607d93` | 23871935 | — |
| `fcn.142572e5a` | `0x142572e5a` | 23661176 | — |
| `fcn.14260506e` | `0x14260506e` | 23619068 | ✓ |
| `fcn.1423b2c69` | `0x1423b2c69` | 23466590 | ✓ |
| `fcn.1429ee78e` | `0x1429ee78e` | 22413638 | ✓ |
| `fcn.1428136de` | `0x1428136de` | 22380792 | ✓ |
| `fcn.142708fe7` | `0x142708fe7` | 22296422 | ✓ |
| `fcn.1427e0ed6` | `0x1427e0ed6` | 22238674 | ✓ |
| `fcn.142990b9e` | `0x142990b9e` | 22023308 | ✓ |
| `loc.14279cf9e` | `0x14279cf9e` | 21852361 | ✓ |
| `fcn.14285b313` | `0x14285b313` | 21597343 | — |
| `fcn.14266fede` | `0x14266fede` | 21289004 | ✓ |
| `fcn.1426efb87` | `0x1426efb87` | 21092963 | ✓ |
| `fcn.1423e5488` | `0x1423e5488` | 20610099 | ✓ |
| `fcn.1425c2618` | `0x1425c2618` | 20556367 | — |
| `fcn.1426ebc26` | `0x1426ebc26` | 20538225 | — |
| `fcn.142603818` | `0x142603818` | 20305357 | ✓ |
| `fcn.1425bde08` | `0x1425bde08` | 20233001 | ✓ |
| `fcn.1425b6756` | `0x1425b6756` | 19828901 | ✓ |
| `fcn.14291ab01` | `0x14291ab01` | 19598673 | — |
| `fcn.1429f49a4` | `0x1429f49a4` | 19150060 | ✓ |
| `fcn.14265b2b5` | `0x14265b2b5` | 19112129 | — |
| `fcn.14248cc9d` | `0x14248cc9d` | 19049195 | — |
| `fcn.1426b5528` | `0x1426b5528` | 19033912 | ✓ |
| `fcn.142499fdf` | `0x142499fdf` | 18756564 | — |
| `fcn.142753751` | `0x142753751` | 18702097 | — |

### Decompiled Code Files

- [`code/fcn.1423b2c69.c`](code/fcn.1423b2c69.c)
- [`code/fcn.1423e5488.c`](code/fcn.1423e5488.c)
- [`code/fcn.1425b6756.c`](code/fcn.1425b6756.c)
- [`code/fcn.1425bde08.c`](code/fcn.1425bde08.c)
- [`code/fcn.142603818.c`](code/fcn.142603818.c)
- [`code/fcn.14260506e.c`](code/fcn.14260506e.c)
- [`code/fcn.14266fede.c`](code/fcn.14266fede.c)
- [`code/fcn.1426b5528.c`](code/fcn.1426b5528.c)
- [`code/fcn.1426efb87.c`](code/fcn.1426efb87.c)
- [`code/fcn.142708fe7.c`](code/fcn.142708fe7.c)
- [`code/fcn.1427e0ed6.c`](code/fcn.1427e0ed6.c)
- [`code/fcn.1428136de.c`](code/fcn.1428136de.c)
- [`code/fcn.142990b9e.c`](code/fcn.142990b9e.c)
- [`code/fcn.1429bef02.c`](code/fcn.1429bef02.c)
- [`code/fcn.1429ee78e.c`](code/fcn.1429ee78e.c)
- [`code/fcn.1429f49a4.c`](code/fcn.1429f49a4.c)
- [`code/loc.14279cf9e.c`](code/loc.14279cf9e.c)

## Behavioral Analysis

Based on the provided disassembly, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The sample appears to be a **highly obfuscated packer or loader**, likely designed to deliver a secondary malicious payload. The code does not perform high-level "business logic" (like searching for files or communicating over standard protocols) in these specific functions; instead, it focuses on:
*   **De-obfuscation:** Extensive use of complex arithmetic, bitwise operations, and jump tables to resolve execution paths.
*   **Stage Transitioning:** Using interrupts and indirect jumps to move between different layers of the loader.
*   **Environment Preparation:** Preparing for a "payload" by decrypting or unpacking subsequent stages in memory.

### Suspicious and Malicious Behaviors
The following behaviors are characteristic of malware loaders intended to evade detection:

*   **Anti-Analysis/Anti-Debugging:** 
    *   The use of `swi(1)` (Software Interrupt) in `fcn.1429bef02` is a common technique used to trigger exceptions that the malware's own exception handler catches to redirect execution flow, making it difficult for standard debuggers to follow.
    *   **Control Flow Obfuscation:** The frequent `halt_baddata()` warnings and "bad instruction" notes indicate the use of junk code or overlapping instructions meant to confuse decompilers and automated analysis tools.

*   **Evasion Techniques:**
    *   **Direct System Calls (`syscall`):** In `fcn.1429f49a4`, an explicit `syscall` is present. This is a common technique used by advanced malware to bypass EDR (Endpoint Detection and Response) hooks on standard Windows APIs by communicating directly with the kernel.
    *   **Instruction Overlapping/Junk Code:** Functions like `fcn.142708fe7` contain extremely complex mathematical calculations that appear to have no practical purpose other than to "mess up" a static analyzer's ability to understand what the code is doing before it reaches the next jump.
    *   **Decoy Strings:** The inclusion of nonsensical strings like `"1§m"` and `\"IIA\x01\"` in `fcn.14266fede` suggests the use of "junk" data to fill memory or confuse analysts looking for embedded indicators of compromise (IOCs).

*   **Potential Process Injection:**
    *   The complexity of the calculations in `fcn.1429f49a4` and its use of indirect calls (e.g., `*(...)(0xd329d283...)`) suggests that it is resolving memory addresses for a payload to be injected or executed as a separate thread/process.

### Notable Techniques and Patterns
*   **VM-Style Obfuscation:** The presence of large jump tables and very complex arithmetic to determine the "next" instruction (as seen in `fcn.142708fe7`) is indicative of **Virtual Machine Protection (VMP)** or similar techniques where the original code is translated into a custom bytecode interpreted by the loader.
*   **Position Independent Code (PIC):** The use of relative addressing and hard-to-follow offsets (e.g., `unaff_RSI + -0x4cde6e27`) suggests the binary is designed to be position-independent, allowing it to execute from various memory locations once unpacked.
*   **Register Pressure/Manipulation:** The code frequently performs operations on multiple registers simultaneously or treats segments of registers as single values (the `CONCAT` macros), which is a hallmark of automated obfuscation tools like **LLVM-based obfuscators** or **Tigress**.

### Summary Conclusion
This sample is not "functional" malware in the sense of a downloader or ransomware yet; it is a **sophisticated loader component.** Its primary goal is to hide its true intent and the presence of the actual payload by employing heavy obfuscation, anti-debugging tricks, and direct system calls to evade security software.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The sample employs junk code, decoy strings, and VM-style obfuscation (complex arithmetic/jump tables) to hinder analysis and hide its true purpose. |
| **T1497** | Virtualization/Sandbox Detection | The use of `swi(1)` exception handling is a classic anti-analysis technique designed to detect the presence of debuggers or virtualized environments. |
| **T1055** | Process Injection | The resolution of specific memory addresses and complex calculations for a "payload" indicate preparation to inject code into another process/thread. |

---

## Indicators of Compromise

Based on the provided data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: `ole32.dll` was identified in strings but is a standard Windows system library and was excluded as a false positive.)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **API Calls:** `CreateThread` (Note: While common, its usage in the context of "Potential Process Injection" is noted in behavioral analysis).
*   **Techniques Detected:** 
    *   Use of `swi(1)` for exception-based control flow.
    *   Direct System Calls (`syscall`) to bypass EDR.
    *   VM-style obfuscation (Tigress/LLVM-based).

---
**Analyst Note:** The provided sample is a sophisticated loader/packer. It does not contain hardcoded network indicators or specific file paths, as it is designed to hide the secondary payload's details through heavy encryption and anti-analysis techniques. Detection should focus on behavioral heuristics (e.g., suspicious `swi` instructions and direct system calls) rather than static indicators.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
* **Sophisticated Evasion Techniques**: The sample utilizes direct system calls (`syscall`) to bypass EDR hooks and `swi(1)` exception handling to complicate debugger analysis, which are hallmarks of professional-grade loaders.
* **Heavy Obfuscation:** The presence of VM-style obfuscation (likely Tigress or LLVM-based), junk code, and complex mathematical transformations indicates the primary goal is to hide the execution logic and transition between stages.
* **Functional Indicators**: The absence of "business logic" (like file encryption or data exfiltration) combined with evidence of process injection and memory resolution confirms its role as a "loader"—a wrapper designed to unpack and execute a secondary, more functional payload in memory.
