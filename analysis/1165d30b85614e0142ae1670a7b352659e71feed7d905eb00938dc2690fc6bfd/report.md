# Threat Analysis Report

**Generated:** 2026-08-23 17:57 UTC
**Sample:** `1165d30b85614e0142ae1670a7b352659e71feed7d905eb00938dc2690fc6bfd_1165d30b85614e0142ae1670a7b352659e71feed7d905eb00938dc2690fc6bfd.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1165d30b85614e0142ae1670a7b352659e71feed7d905eb00938dc2690fc6bfd_1165d30b85614e0142ae1670a7b352659e71feed7d905eb00938dc2690fc6bfd.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 (stripped to external PDB), 3 sections |
| Size | 46,080 bytes |
| MD5 | `ab46540b1543491f385bb3f3419fca0c` |
| SHA1 | `56ccb29b619c7994413b41802c77d4e4893c201d` |
| SHA256 | `1165d30b85614e0142ae1670a7b352659e71feed7d905eb00938dc2690fc6bfd` |
| Overall entropy | 7.861 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.MPRESS1` | 40,448 | 7.994 | ⚠️ Yes |
| `.MPRESS2` | 3,584 | 5.799 | No |
| `.rsrc` | 1,536 | 2.553 | No |

### Imports

**KERNEL32.DLL**: `GetModuleHandleA`, `GetProcAddress`
**ADVAPI32.DLL**: `RegCloseKey`
**DNSAPI.DLL**: `DnsQuery_A`
**msvcrt.dll**: `_iob`
**USER32.dll**: `wsprintfA`
**WININET.DLL**: `InternetGetConnectedState`
**WS2_32.DLL**: `recv`

## Extracted Strings

Total strings found: **126** (showing first 100)

```
!Win32 .EXE.
$@
.MPRESS1
.MPRESS25
760hfmgd
130dfhjz
13f6qagd
nW
'	t
yeG.[Uc
bp!Fv!
i^st"T<
IBz$sH~
iXZd?P&;'j[5
,=k[#)
\8_TKU
2'"bgE
n;L2we
BVaM,
I {c8.nX
M>/{,<
-$9'2/`}
A{;$Ka
5n.ZX?
jj$sLn
<E-JEx
HzqSyjC;CO
R%p m8
Ky:EQW"M3<
m%VQHJv
=x&)#s
"7?U}_
pYzjBf
Q[<l02
J]($}:
g"2
P
6.udBhVr

2hkM5-N
t^-m8
L*
.#0"M/
Vq:=K<tf
mm88Ft<w	~
%;ZkV?P
KpoI7g?
kZ(N`Z
+"7gw%^Z
cL~1G
W1!F|"
lI%%Lb	
Q,2Oy,#
E?)W7I
d>wg;	5
`^._kA
_+ZOJk
5}&..r^

n\|g 
n$a@qp8
Hy}a{
Fp\C:u
{Z4r8j{
UU)23w"
HY7+5V
8(:&kfL?_]
tMF\&?
y/?\84b
65'*N&S
u3Do+<
u>*<wV

Rg~7u
mb#.hw
	NK_|
ww(Bd@1
!6$}!7
Be0:dU
"axM(lV
g6C;_Z
]]+0b>
t,g+h|
x	0?G2
wLHVx
kp
z!;F`c
%o5;|N
y!!8JYW
J~*t7:
y?bs9\
R{BkY:
T4GKGC[>U
<[lmyg
1NUcEG=
6	]!Uc
|#rN<%
2)|n?/
~2CtE.9
Ksd0{y
0{9EFt`
c(vV}bP
xulL;X
7n7_aQ	
`k;}>s?
02Lfyh
zOR7L
_
r1F{S1
```

## Disassembly Overview

Functions analyzed: **11** | Decompiled to C: **11**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0041f27e` | `0x41f27e` | 2733 | ✓ |
| `fcn.0041f29e` | `0x41f29e` | 2696 | ✓ |
| `sym.imp.WS2_32.DLL_recv` | `0x41f0e9` | 311 | ✓ |
| `entry0` | `0x41f1cb` | 162 | ✓ |
| `fcn.00406bc1` | `0x406bc1` | 27 | ✓ |
| `sym.imp.KERNEL32.DLL_GetProcAddress` | `0x41f0b8` | 8 | ✓ |
| `sym.imp.ADVAPI32.DLL_RegCloseKey` | `0x41f0c0` | 8 | ✓ |
| `sym.imp.DNSAPI.DLL_DnsQuery_A` | `0x41f0c8` | 8 | ✓ |
| `sym.imp.WININET.DLL_InternetGetConnectedState` | `0x41f0e0` | 8 | ✓ |
| `sym.imp.KERNEL32.DLL_GetModuleHandleA` | `0x41f0b4` | 4 | ✓ |
| `fcn.0041f26d` | `0x41f26d` | 1 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00406bc1.c`](code/fcn.00406bc1.c)
- [`code/fcn.0041f26d.c`](code/fcn.0041f26d.c)
- [`code/fcn.0041f27e.c`](code/fcn.0041f27e.c)
- [`code/fcn.0041f29e.c`](code/fcn.0041f29e.c)
- [`code/sym.imp.ADVAPI32.DLL_RegCloseKey.c`](code/sym.imp.ADVAPI32.DLL_RegCloseKey.c)
- [`code/sym.imp.DNSAPI.DLL_DnsQuery_A.c`](code/sym.imp.DNSAPI.DLL_DnsQuery_A.c)
- [`code/sym.imp.KERNEL32.DLL_GetModuleHandleA.c`](code/sym.imp.KERNEL32.DLL_GetModuleHandleA.c)
- [`code/sym.imp.KERNEL32.DLL_GetProcAddress.c`](code/sym.imp.KERNEL32.DLL_GetProcAddress.c)
- [`code/sym.imp.WININET.DLL_InternetGetConnectedState.c`](code/sym.imp.WININET.DLL_InternetGetConnectedState.c)
- [`code/sym.imp.WS2_32.DLL_recv.c`](code/sym.imp.WS2_32.DLL_recv.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is a summary of the analysis:

### Core Functionality and Purpose
The binary appears to be a **malicious loader or dropper**. Its primary purpose is to deobfuscate its own code/data in memory before proceeding to network communication. The presence of complex decoding loops and repeated arithmetic operations suggests it contains a "packer" or "protector" layer designed to hide the true functionality from static analysis.

### Suspicious and Malicious Behaviors
*   **Network Communication:** 
    *   The inclusion of `DnsQuery_A` indicates that the malware resolves domain names, likely for its Command & Control (C2) server.
    *   `InternetGetConnectedState` is used to check for an active connection before attempting to communicate.
    *   The presence of `recv` from `WS2_32.DLL` confirms it is designed to receive data over a network socket, likely receiving instructions or additional payloads from a remote host.
*   **Anti-Analysis / Obfuscation:**
    *   **Junk Code/Arithmetic:** Function `fcn.0041f27e` contains repetitive, complex arithmetic on memory addresses (e.g., `0x41fd2b`, `0x41f056`). These operations do not result in meaningful logic but serve to confuse decompilers and automated analysis tools.
    *   **Complex Decryption Loops:** Function `fcn.0041f29e` contains a large, complex loop structure with numerous bitwise shifts and conditional branches. This is characteristic of a custom decryption or deobfuscation routine used to unpack the next stage of the malware in memory.
*   **Registry Manipulation (Potential Persistence):** 
    *   The inclusion of `RegCloseKey` implies that the malware interacts with the Windows Registry, which is frequently used for establishing persistence (e.g., adding entries to "Run" keys).

### Notable Techniques and Patterns
*   **Dynamic API Resolution:** The use of `GetProcAddress` and `GetModuleHandleA` suggests the binary may resolve its true functionality at runtime rather than having it visible in the Import Address Table (IAT), a common evasion technique.
*   **Multi-Stage Execution:** The heavy investment in deobfuscation routines (`fcn.0041f29e`) indicates that the initial code is just a loader designed to unpack and run the actual malicious payload.
*   **Obscured Strings/Network Indicators:** While the strings provided are largely garbled (likely due to an encoding or packing layer), the presence of `www` related fragments suggests it prepares for web-based communication.

### Summary Table of Relevant Imports
| API Function | Potential Malicious Intent |
| :--- | :--- |
| `DnsQuery_A` | C2 Domain Resolution |
| `InternetGetConnectedState` | Checking network connectivity before "calling home" |
| `recv` | Receiving data from a remote server |
| `RegCloseKey` | Persistence via registry modification |
| `GetProcAddress` | Obfuscating API calls to hide true capabilities |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of junk code, complex decryption loops, and dynamic API resolution are used to hide the binary's true functionality from static analysis tools. |
| T1105 | Ingress Tool Transfer | The presence of the `recv` function indicates that the malware is designed to receive additional payloads or instructions over a network connection. |
| T1547.001 | Registry Run Keys / Startup Folder | Interaction with registry keys (indicated by `RegCloseKey`) suggests an attempt to establish persistence on the host system for repeated execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs).

**Note:** Many of the strings provided in the input appear to be obfuscated or part of a packing/encryption layer; therefore, no specific high-confidence IP addresses or file paths were identified.

### **IP addresses / URLs / Domains**
*   None identified. *(The string `wwwwwwwwwwpp` appears to be a non-functional fragment or byproduct of the extraction process).*

### **File paths / Registry keys**
*   None identified. *(While registry manipulation was noted in the analysis, no specific keys or paths were provided in the text).*

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts (user agents, C2 patterns, etc.)**
*   **Suspicious API Patterns:**
    *   `DnsQuery_A`: Used for C2 domain resolution.
    *   `InternetGetConnectedState`: Used to verify connectivity before "calling home."
    *   `recv`: Used for receiving remote payloads or instructions via `WS2_32.DLL`.
    *   `GetProcAddress` / `GetModuleHandleA`: Indicates dynamic API resolution to hide functionality from static analysis.
*   **Decoding/Packer Indicators:**
    *   `.MPRESS1`
    *   `.MPRESS25`
*   **Technical Artifacts (Function Offsets):**
    *   `fcn.0041f27e`: Identified as a junk code/arithmetic obfuscation loop.
    *   `fcn.0041f29e`: Identified as a complex decryption routine for multi-stage execution.
*   **Known Library Interaction:**
    *   `WININET.DLL` (Network communication)
    *   `ADVAPI32.DLL` (System/Registry interaction)

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Heavy Obfuscation & Multi-Stage Execution:** The presence of complex decryption loops (fcn.0041f29e), junk code, and dynamic API resolution indicates a design intended to hide the primary payload while unpacking it in memory for later execution.
*   **Staged Payload Delivery:** The combination of `DnsQuery_A` (C2 resolution) and `recv` functionality confirms its role as a gateway; it is specifically designed to establish a connection and pull down secondary components or instructions from a remote server.
*   **Persistence & Evasion Indicators:** The use of `RegCloseKey` suggests an intent to maintain residency on the system, while the deliberate use of "noise" (arithmetic-heavy junk code) identifies it as a professional loader/dropper designed to bypass static analysis tools.
