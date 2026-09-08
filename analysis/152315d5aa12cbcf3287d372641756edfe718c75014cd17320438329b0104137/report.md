# Threat Analysis Report

**Generated:** 2026-09-06 19:14 UTC
**Sample:** `152315d5aa12cbcf3287d372641756edfe718c75014cd17320438329b0104137_152315d5aa12cbcf3287d372641756edfe718c75014cd17320438329b0104137.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `152315d5aa12cbcf3287d372641756edfe718c75014cd17320438329b0104137_152315d5aa12cbcf3287d372641756edfe718c75014cd17320438329b0104137.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 12 sections |
| Size | 7,768,576 bytes |
| MD5 | `76c32d70bf23178e76ac791cb752acbb` |
| SHA1 | `19544fccdc0acaa0a2fe92aa5f18d66b9a8428ff` |
| SHA256 | `152315d5aa12cbcf3287d372641756edfe718c75014cd17320438329b0104137` |
| Overall entropy | 7.932 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766328495 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 0 | 0.0 | No |
| `.data` | 0 | 0.0 | No |
| `.rdata` | 0 | 0.0 | No |
| `.pdata` | 0 | 0.0 | No |
| `.xdata` | 0 | 0.0 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 0 | 0.0 | No |
| `.CRT` | 0 | 0.0 | No |
| `.tls` | 0 | 0.0 | No |
| `.code0` | 0 | 0.0 | No |
| `.code1` | 7,765,504 | 7.933 | ⚠️ Yes |
| `.rsrc` | 2,048 | 4.591 | No |

### Imports

**ADVAPI32.dll**: `AdjustTokenPrivileges`
**CRYPT32.dll**: `CertCloseStore`
**dbghelp.dll**: `MiniDumpWriteDump`
**IPHLPAPI.DLL**: `ConvertInterfaceIndexToLuid`
**KERNEL32.dll**: `LocalAlloc`, `LocalFree`, `GetModuleFileNameW`, `GetProcessAffinityMask`, `SetProcessAffinityMask`, `SetThreadAffinityMask`, `Sleep`, `ExitProcess`, `FreeLibrary`, `LoadLibraryA`, `GetModuleHandleA`, `GetProcAddress`
**msvcrt.dll**: `___lc_codepage_func`
**ole32.dll**: `CoCreateInstance`
**SHELL32.dll**: `SHGetKnownFolderPath`
**USER32.dll**: `GetProcessWindowStation`, `GetUserObjectInformationW`
**USERENV.dll**: `GetUserProfileDirectoryW`
**WS2_32.dll**: `FreeAddrInfoW`
**WTSAPI32.dll**: `WTSSendMessageW`

## Extracted Strings

Total strings found: **15179** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
.code0
h.code1
h.rsrc
d$W`(^K
$zbt	,
,*q@]*
|p")@(
az2;Ka\F

,e6c!
``W6h\
2xJjS@d
'?zv6L
)"r!&`
D+J_-l
h-z*;4
0'oJ,!
k(_)<q
4;$\+,;'
-;b[|(
3;A/D>;w&
JU<<lJuC
/:eL5j
#+;gKW
7y);|e
eXAZ6
`SANav
2;r(93
e:qx<C
8Sso:"
f	<S53
7>&!h5>#
I55/bIU
239WQ
Bj8is
<K0hyU
nEib.V
Ir]cr.
=hyU.e
R,"t>L
5?c'?
-;|E@CG
3@x"70
)N[lP'q
BYJ7x
E"|ujE
xu735wc
W.& MQ
d*r}qZs
) N	yi{
a}F_^lC
F={Z0xP[
q\P?9[
D?p=4"!
jthu4j
6UhFe
dBjBxx
X{=;Z:#&
UX"Ca|^
GetModuleHandleA
s7Wcz/
K	1k?~
>	13W
eSa[f!
An.$O;
@cv8^y
bv8^wzww
0h}Il2/>'
%x%,7y:9
+L=/'C
a_`ix{Hj
mma{X>Uj;
cd;liU
IPHLPAPI.DLL
=;:T[0;=
j*i4$t/
e\ {lS
S<h`#$
m|A[67s
5>l_B4
NCOZH8
.]D6{
rsVOcu
|-+)U/5
e`s*#ewN
5o.ej>:lh?
u~E{Mw
YQ=CeqM
>`@E\l
9Nm<#?
[I=eZA
v7N)lj
#rDp
\
AzMykA
M/R$SG
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.141333be5` | `0x141333be5` | 5512907 | ✓ |
| `fcn.14133deb9` | `0x14133deb9` | 1305040 | ✓ |
| `fcn.14146b9cf` | `0x14146b9cf` | 1255377 | ✓ |
| `fcn.14143b4c8` | `0x14143b4c8` | 1211538 | ✓ |
| `fcn.14134f399` | `0x14134f399` | 1157504 | ✓ |
| `fcn.141455e7a` | `0x141455e7a` | 1144053 | ✓ |
| `fcn.1413519a1` | `0x1413519a1` | 1142566 | ✓ |
| `fcn.14145200c` | `0x14145200c` | 1044880 | ✓ |
| `fcn.14142f186` | `0x14142f186` | 946171 | ✓ |
| `fcn.14142fea8` | `0x14142fea8` | 939040 | ✓ |
| `fcn.14133d203` | `0x14133d203` | 910801 | ✓ |
| `fcn.1413b0ac7` | `0x1413b0ac7` | 786516 | ✓ |
| `fcn.1413e8f13` | `0x1413e8f13` | 462353 | ✓ |
| `fcn.1414a8c15` | `0x1414a8c15` | 1063 | ✓ |
| `fcn.140e5b63b` | `0x140e5b63b` | 224 | ✓ |
| `fcn.1410d45d1` | `0x1410d45d1` | 222 | ✓ |
| `fcn.141491da5` | `0x141491da5` | 216 | ✓ |
| `fcn.1412014bd` | `0x1412014bd` | 214 | ✓ |
| `fcn.141491887` | `0x141491887` | 174 | ✓ |
| `fcn.14149ec15` | `0x14149ec15` | 173 | ✓ |
| `fcn.140f8e2e3` | `0x140f8e2e3` | 125 | ✓ |
| `int.140f6d8e3` | `0x140f6d8e3` | 117 | ✓ |
| `entry1` | `0x140ddbbfb` | 80 | ✓ |
| `fcn.1414a1413` | `0x1414a1413` | 75 | ✓ |
| `fcn.141379680` | `0x141379680` | 36 | ✓ |
| `entry0` | `0x14100c2c8` | 33 | ✓ |
| `fcn.1412bf727` | `0x1412bf727` | 27 | ✓ |
| `sym.imp.IPHLPAPI.DLL_ConvertInterfaceIndexToLuid` | `0x141036030` | 24 | ✓ |
| `fcn.14101054c` | `0x14101054c` | 10 | ✓ |
| `fcn.140d53d9b` | `0x140d53d9b` | 7 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/entry1.c`](code/entry1.c)
- [`code/fcn.140d53d9b.c`](code/fcn.140d53d9b.c)
- [`code/fcn.140e5b63b.c`](code/fcn.140e5b63b.c)
- [`code/fcn.140f8e2e3.c`](code/fcn.140f8e2e3.c)
- [`code/fcn.14101054c.c`](code/fcn.14101054c.c)
- [`code/fcn.1410d45d1.c`](code/fcn.1410d45d1.c)
- [`code/fcn.1412014bd.c`](code/fcn.1412014bd.c)
- [`code/fcn.1412bf727.c`](code/fcn.1412bf727.c)
- [`code/fcn.141333be5.c`](code/fcn.141333be5.c)
- [`code/fcn.14133d203.c`](code/fcn.14133d203.c)
- [`code/fcn.14133deb9.c`](code/fcn.14133deb9.c)
- [`code/fcn.14134f399.c`](code/fcn.14134f399.c)
- [`code/fcn.1413519a1.c`](code/fcn.1413519a1.c)
- [`code/fcn.141379680.c`](code/fcn.141379680.c)
- [`code/fcn.1413b0ac7.c`](code/fcn.1413b0ac7.c)
- [`code/fcn.1413e8f13.c`](code/fcn.1413e8f13.c)
- [`code/fcn.14142f186.c`](code/fcn.14142f186.c)
- [`code/fcn.14142fea8.c`](code/fcn.14142fea8.c)
- [`code/fcn.14143b4c8.c`](code/fcn.14143b4c8.c)
- [`code/fcn.14145200c.c`](code/fcn.14145200c.c)
- [`code/fcn.141455e7a.c`](code/fcn.141455e7a.c)
- [`code/fcn.14146b9cf.c`](code/fcn.14146b9cf.c)
- [`code/fcn.141491887.c`](code/fcn.141491887.c)
- [`code/fcn.141491da5.c`](code/fcn.141491da5.c)
- [`code/fcn.14149ec15.c`](code/fcn.14149ec15.c)
- [`code/fcn.1414a1413.c`](code/fcn.1414a1413.c)
- [`code/fcn.1414a8c15.c`](code/fcn.1414a8c15.c)
- [`code/int.140f6d8e3.c`](code/int.140f6d8e3.c)
- [`code/sym.imp.IPHLPAPI.DLL_ConvertInterfaceIndexToLuid.c`](code/sym.imp.IPHLPAPI.DLL_ConvertInterfaceIndexToLuid.c)

## Behavioral Analysis

This analysis identifies the sample as a **packer or loader for malicious code**, likely utilizing advanced evasion techniques to hide its true functionality from static and dynamic analysis.

### Core Functionality and Purpose
The primary purpose of this binary is to act as a "stub." It prepares an environment where hidden malicious payloads can be unpacked, decrypted, and executed in memory. Instead of calling standard Windows APIs directly (which would be visible in the Import Address Table), it resolves these functions at runtime using **API Hashing**.

### Suspicious or Malicious Behaviors
*   **API Hashing (Dynamic Resolution):** 
    The function `fcn.141333be5` is a classic implementation of an API hashing resolver. It iterates through the export tables of system DLLs (like `kernel32.dll`) and compares the names of the functions against a pre-calculated hash rather than a plain string. This allows the malware to call sensitive APIs (e.g., for process injection or networking) without those names appearing in the binary's headers.
*   **Anti-Analysis / Junk Code:** 
    Several functions (e.g., `fcn.1413deb9`, `fcn.14146b9cf`, `fcn.14143b4c8`) contain complex, "noisy" arithmetic and bitwise operations that do not contribute to the actual logic but are intended to confuse automated decompilers and human analysts (a technique known as **Code Bloating** or **Metamorphism**).
*   **Indirect Execution:** 
    The use of indirect jumps—calculated via heavy math—to jump into code blocks is a hallmark of packers. It makes it difficult for static analysis tools to map the execution flow of the program.
*   **Network Scouting Indicators:** 
    The presence of `IPHLPAPI.DLL_ConvertInterfaceIndexToLuid` (found in the strings) suggests that if the payload is active, it may be inspecting network configurations or local network topology to facilitate lateral movement or data exfiltration.

### Notable Techniques & Patterns
*   **Custom Hashing Algorithm:** The code uses a specific hash constant (`0x2d794c7f`) during its search for functions. This confirms that the binary is intentionally hiding its "Import" list from simple security scanners.
*   **String Manipulation/De-obfuscation:** The logic within `fcn.141333be5` includes loops to find specific characters (like `.`) and handle `#` marks, which are typically used during the assembly of a custom loader to jump between different decrypted segments of code.
*   **Control Flow Obfuscation:** The "not_enough" warnings in the decompiler output for several functions suggest that the compiler-generated or manually crafted jumps are intentionally non-linear to break the analysis of the execution path.

### Summary Conclusion
This binary is a **sophisticated loader/packer**. It does not appear to perform any high-level malicious actions itself (like file deletion or keylogging); instead, it serves as a "shield" for a payload. Its use of API hashing and junk code indicates an intent to bypass signature-based detection and hinder manual reverse engineering.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of API hashing and dynamic resolution hides the binary's intended functionality from static analysis of the Import Address Table (IAT). |
| T1027 | Obfuscated Files or Information | The inclusion of "junk code" (complex, non-functional arithmetic) is designed to confuse decompilers and exhaust manual reverse engineering efforts. |
| T1027 | Obfuscated Files or Information | The implementation of indirect jumps via complex math creates a non-linear execution path to hinder the mapping of the program's logic. |
| T1590 | Gather Victim Network Information | The inclusion of `IPHLPAPI` functions suggests an intent to map local network topology and infrastructure for potential lateral movement. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `IPHLPAPI.DLL` (Note: While a standard system library, it is flagged in this context as part of the network scouting behavior).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   `0x2d794c7f` (Specific hash constant used by the loader's custom hashing algorithm to resolve API functions).

**Other artifacts**
*   **Function Offsets/Identifiers:** 
    *   `fcn.141333be5` (API Hashing resolver)
    *   `fcn.1413deb9` (Junk code/Obfuscation)
    *   `fcn.14146b9cf` (Junk code/Obfuscation)
    *   `fcn.14143b4c8` (Junk code/Obfuscation)
*   **API Resolution Pattern:** Usage of `GetModuleHandleA` combined with custom hashing to bypass the Import Address Table (IAT).
*   **Behavioral Indicator:** Presence of `IPHLPAPI.DLL_ConvertInterfaceIndexToLuid` signifying potential network reconnaissance or internal network scanning capabilities.
*   **Obfuscation Techniques:** Evidence of "Code Bloating," non-linear control flow, and advanced packers designed to hide the primary malicious payload.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
*   **Stub Behavior:** The analysis explicitly identifies the binary as a "stub" or packer designed to hide, decrypt, and execute a secondary payload in memory rather than performing direct malicious actions like data theft or encryption itself.
*   **Advanced Evasion Techniques:** The use of API Hashing (specifically for `fcn.141333be5`), junk code/metamorphism, and non-linear control flow are classic indicators of a sophisticated loader designed to bypass static analysis and evade signature-based detection.
*   **Network Preparation:** The inclusion of `IPHLPAPI` functions indicates that the loader is prepared to facilitate environment mapping or network scouting for subsequent stages (such as lateral movement) once the payload is active.
