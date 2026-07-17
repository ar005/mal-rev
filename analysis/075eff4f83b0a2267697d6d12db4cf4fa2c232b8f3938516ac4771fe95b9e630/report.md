# Threat Analysis Report

**Generated:** 2026-07-16 18:34 UTC
**Sample:** `075eff4f83b0a2267697d6d12db4cf4fa2c232b8f3938516ac4771fe95b9e630_075eff4f83b0a2267697d6d12db4cf4fa2c232b8f3938516ac4771fe95b9e630.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `075eff4f83b0a2267697d6d12db4cf4fa2c232b8f3938516ac4771fe95b9e630_075eff4f83b0a2267697d6d12db4cf4fa2c232b8f3938516ac4771fe95b9e630.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 8 sections |
| Size | 10,098,176 bytes |
| MD5 | `b7e646c690fc4866430db8c74a1bb6a6` |
| SHA1 | `3abe326b31c5f75a49cabf314e4c22a6983d9e83` |
| SHA256 | `075eff4f83b0a2267697d6d12db4cf4fa2c232b8f3938516ac4771fe95b9e630` |
| Overall entropy | 7.965 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1772363915 |
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
| `.vmp0` | 0 | 0.0 | No |
| `.vmp1` | 10,096,640 | 7.965 | ⚠️ Yes |
| `.rsrc` | 512 | 4.721 | No |

### Imports

**d3d11.dll**: `D3D11CreateDeviceAndSwapChain`
**D3DCOMPILER_47.dll**: `D3DCompile`
**KERNEL32.dll**: `LocalAlloc`, `LocalFree`, `GetModuleFileNameW`, `GetProcessAffinityMask`, `SetProcessAffinityMask`, `SetThreadAffinityMask`, `Sleep`, `ExitProcess`, `FreeLibrary`, `LoadLibraryA`, `GetModuleHandleA`, `GetProcAddress`
**USER32.dll**: `GetProcessWindowStation`, `GetUserObjectInformationW`
**GDI32.dll**: `GetDeviceCaps`
**ADVAPI32.dll**: `CryptReleaseContext`
**SHELL32.dll**: `ShellExecuteW`
**ole32.dll**: `CoInitializeEx`
**OLEAUT32.dll**: `VariantClear`
**dwmapi.dll**: `DwmExtendFrameIntoClientArea`
**IMM32.dll**: `ImmReleaseContext`
**IPHLPAPI.DLL**: `GetAdaptersInfo`
**WINHTTP.dll**: `WinHttpReceiveResponse`
**WS2_32.dll**: `WSACleanup`
**WTSAPI32.dll**: `WTSSendMessageW`

## Extracted Strings

Total strings found: **21188** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
h.vmp1
h.rsrc
<}ZD+]}#
~fI_'l_McH
.Vc#!P?p
&x#9~m
&"s'#vkvS
<Q `>t*

J_v&'N
0.X\I#
VvE]soi
%1VA`n
ouRA#*,RA
auRAfsN"
$l5\pM
ex"}}/U
QCA\m]
,1kY:

)u]U88
OYS~mz
=$lh8V
qk!Up
=52-$1
aj]36!
)?9cG
Fo
bIk,y%
t~V{#Bt
GetUserObjectInformationW
OQAi@W
Gg1l%u%K
%]A! 

&]AT[	
']AH->
\AZSp]A
yCF\5G{I4
&suzp)
X;@HX{\
n1@hXMV
XjxN*0
Avt(<S0
YMUK<T
%}&w5A
CylY(xG)
.KgSABK
[ANey_
UAEftS
vXAI,T
d-T<9/
x/?VAX
8/9U^v/n
&;bqI+P
K$[[AC
D<qqha*54
\AqxV]A|
8V3WLe
s+RAjC3
mskqU^
=mG"I$wX/
8Ub,:g
JM/,W-
lkj.^
m09TT]0S_
4VhXhHM
s+ItGZ
xBuG-n
NrciP2
Z[Af(_
x{];M<
Z:'3u>t
;9
s\{
5'~pqJ
L;`&H
'vg+0~
V	y1Op;
l=8jOw
6W|tRc
Zqfnjy
(0P<&)
,*@^q"
@rR%<sv#N
\mtn3/IDIOm
)rM
YZc].a&
m79RJ9
		n)N
]Ak"G]An
NpUA_vh
-H9Nkb
.5{Vb
\^>='

6{#pK9
AVAeY
1QPVorm
#"IeY
k
$E,"r%
954]DG
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14154a6c1` | `0x14154a6c1` | 6057394 | ✓ |
| `fcn.141632c2e` | `0x141632c2e` | 1256077 | ✓ |
| `fcn.1415a4db9` | `0x1415a4db9` | 1121282 | ✓ |
| `fcn.14154f543` | `0x14154f543` | 1117792 | ✓ |
| `fcn.141670fac` | `0x141670fac` | 1062906 | ✓ |
| `fcn.1415d02cc` | `0x1415d02cc` | 963206 | ✓ |
| `fcn.14169424c` | `0x14169424c` | 959891 | ✓ |
| `fcn.141565b2a` | `0x141565b2a` | 940170 | ✓ |
| `fcn.14163a792` | `0x14163a792` | 878574 | ✓ |
| `fcn.141662812` | `0x141662812` | 808735 | ✓ |
| `fcn.14160657a` | `0x14160657a` | 440274 | ✓ |
| `fcn.1415adac7` | `0x1415adac7` | 312636 | ✓ |
| `fcn.1415ba3f8` | `0x1415ba3f8` | 287480 | ✓ |
| `fcn.141585451` | `0x141585451` | 165749 | ✓ |
| `fcn.141639246` | `0x141639246` | 61524 | ✓ |
| `fcn.1416a72a7` | `0x1416a72a7` | 279 | ✓ |
| `fcn.1412487b2` | `0x1412487b2` | 220 | ✓ |
| `fcn.1416a57cf` | `0x1416a57cf` | 192 | ✓ |
| `fcn.140ee2700` | `0x140ee2700` | 125 | ✓ |
| `entry0` | `0x140f81dab` | 111 | ✓ |
| `fcn.14117622f` | `0x14117622f` | 97 | ✓ |
| `fcn.141464507` | `0x141464507` | 90 | ✓ |
| `fcn.1412d51c8` | `0x1412d51c8` | 85 | ✓ |
| `fcn.1414cb445` | `0x1414cb445` | 46 | ✓ |
| `fcn.14146bc19` | `0x14146bc19` | 35 | ✓ |
| `fcn.141656eb0` | `0x141656eb0` | 34 | ✓ |
| `fcn.140da2b87` | `0x140da2b87` | 33 | ✓ |
| `fcn.14135568f` | `0x14135568f` | 31 | ✓ |
| `fcn.1416a7023` | `0x1416a7023` | 25 | ✓ |
| `fcn.140d65420` | `0x140d65420` | 24 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.140d65420.c`](code/fcn.140d65420.c)
- [`code/fcn.140da2b87.c`](code/fcn.140da2b87.c)
- [`code/fcn.140ee2700.c`](code/fcn.140ee2700.c)
- [`code/fcn.14117622f.c`](code/fcn.14117622f.c)
- [`code/fcn.1412487b2.c`](code/fcn.1412487b2.c)
- [`code/fcn.1412d51c8.c`](code/fcn.1412d51c8.c)
- [`code/fcn.14135568f.c`](code/fcn.14135568f.c)
- [`code/fcn.141464507.c`](code/fcn.141464507.c)
- [`code/fcn.14146bc19.c`](code/fcn.14146bc19.c)
- [`code/fcn.1414cb445.c`](code/fcn.1414cb445.c)
- [`code/fcn.14154a6c1.c`](code/fcn.14154a6c1.c)
- [`code/fcn.14154f543.c`](code/fcn.14154f543.c)
- [`code/fcn.141565b2a.c`](code/fcn.141565b2a.c)
- [`code/fcn.141585451.c`](code/fcn.141585451.c)
- [`code/fcn.1415a4db9.c`](code/fcn.1415a4db9.c)
- [`code/fcn.1415adac7.c`](code/fcn.1415adac7.c)
- [`code/fcn.1415ba3f8.c`](code/fcn.1415ba3f8.c)
- [`code/fcn.1415d02cc.c`](code/fcn.1415d02cc.c)
- [`code/fcn.14160657a.c`](code/fcn.14160657a.c)
- [`code/fcn.141632c2e.c`](code/fcn.141632c2e.c)
- [`code/fcn.141639246.c`](code/fcn.141639246.c)
- [`code/fcn.14163a792.c`](code/fcn.14163a792.c)
- [`code/fcn.141656eb0.c`](code/fcn.141656eb0.c)
- [`code/fcn.141662812.c`](code/fcn.141662812.c)
- [`code/fcn.141670fac.c`](code/fcn.141670fac.c)
- [`code/fcn.14169424c.c`](code/fcn.14169424c.c)
- [`code/fcn.1416a57cf.c`](code/fcn.1416a57cf.c)
- [`code/fcn.1416a7023.c`](code/fcn.1416a7023.c)
- [`code/fcn.1416a72a7.c`](code/fcn.1416a72a7.c)

## Behavioral Analysis

### Analysis Summary
Based on the provided disassembly, the binary exhibits characteristics of a highly obfuscated piece of malware. The code contains significant layers of protection designed to hinder static analysis and manual reverse engineering.

#### Core Functionality and Purpose
The primary purpose of this specific section of the code is **protection and evasion**. Rather than performing overt actions (like file deletion or network communication) in these functions, the code focuses on:
*   **Dynamic API Resolution:** Hiding the actual Windows system calls it intends to make.
*   **Anti-Analysis/Anti-Debugging:** Detecting if the malware is being run in a controlled environment (debugger/emulator).
*   **Control Flow Obfuscation:** Using "junk code" and complex arithmetic to break the logic flow for automated tools like Decompilers or Disassemblers.

#### Suspicious and Malicious Behaviors
*   **Dynamic API Resolution & String Obfuscation (`fcn.14154a6c1`):** 
    *   The code iterates through a buffer, checking for "MZ" and "PE" headers (typical of parsing the Process Environment Block or exported tables).
    *   It uses an **XOR-based decryption routine** to deobfuscate strings in memory. These strings likely represent hidden Windows API names (e.g., `NtCreateThread` or `InternetOpen`).
    *   After decrypting a string, it dynamically finds the address of the function using `GetModuleHandleA` and `GetProcAddress`. This is used to hide the malware's true capabilities from static analysis.
*   **Anti-Analysis Timing Checks (`fcn.14169424c`, `fcn.141585451`):**
    *   Both functions utilize the **`rdtsc` (Read Time Stamp Counter)** instruction twice in close proximity. 
    *   This is a common technique to detect the presence of a debugger or an emulator; if the time difference between two `rdtsc` calls is too large, it indicates the code is being "stepped through" by an analyst or slowed down by virtualization.
*   **Code Obfuscation / Junk Code Insertion:** 
    *   Several functions (e.g., `fcn.141632c2e`, `fcn.141670fac`) contain complex, repetitive arithmetic operations and bitwise shifts that do not affect the program's output but serve to confuse the analyst and "break" the decompiler's ability to produce clean C code.
*   **Control Flow Flattening/Complex Jumps:** 
    *   The use of "unrecovered jump tables" and arithmetic-based jumps (e.g., `fcn.14154f543`) indicates the use of a **packer or protector**. This makes it extremely difficult to follow the execution path linearly, as the next instruction's location is calculated at runtime.

#### Notable Techniques/Patterns
*   **Custom Loader Pattern:** The presence of manual PE parsing (searching for `0x5a4d` and `0x4550`) suggests a "packer" or "loader" stub is being used to decrypt the main payload into memory.
*   **Instruction Overlap / Junk Data:** Several functions are flagged with "broken" logic or "bad instruction data," which is often a byproduct of **polymorphic engines** or tools designed to trick disassemblers into showing incorrect instructions for subsequent blocks.
*   **API Hooking Evasion:** By resolving APIs like `GetProcAddress` and `LoadLibraryA` at runtime from obfuscated strings, the malware avoids having "suspicious" names in its Import Address Table (IAT).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of "junk code," instruction overlapping, and complex arithmetic is designed to hide the logic from disassemblers and complicate manual analysis. |
| **T1027.003** | Obfuscated Files or Information: Packing | The presence of a custom loader stub with manual PE header parsing (MZ/PE) indicates the sample uses packing to deobfuscate its primary payload in memory. |
| **T1496** | Debugger Evasion | The use of the `rdtsc` instruction to measure timing discrepancies is a common method to detect if a debugger is being used to step through the code. |
| **T1497** | Virtualization/Sandbox Evasion | Multiple `rdtsc` checks are frequently utilized to detect execution within virtualized environments or sandboxes where processing speeds may differ from physical hardware. |
| **T1027** | Obfuscated Files or Information (Dynamic Resolution) | The use of XOR-based decryption for API strings combined with `GetProcAddress` hides the malicious intent by ensuring suspicious functions do not appear in the Import Address Table (IAT). |

---

## Indicators of Compromise

Based on the provided string set and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Because the malware utilizes heavy obfuscation and encryption (XOR), most of the raw strings provided do not resolve to human-readable IP addresses or file paths in their current state. The "indicators" in this case are primarily behavioral patterns.

**IP addresses / URLs / Domains**
*   None identified (Strings appear to be encrypted/obfuscated).

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Anti-Analysis Technique:** `rdtsc` (Read Time Stamp Counter) – Used to detect the presence of debuggers or virtualized environments via timing checks.
*   **Evasion Technique:** XOR-based string decryption — Used to deobfuscate hidden Windows API calls in memory.
*   **Evasion Technique:** Manual PE Parsing — The code explicitly searches for `0x5a4d` (MZ) and `0x4550` (PE) headers to resolve functions dynamically, bypassing the Import Address Table (IAT).
*   **Obfuscation Method:** Control Flow Flattening / Junk Code Insertion — Used to hinder automated de-compilation and manual analysis.
*   **Dynamic API Resolution:** Use of `GetModuleHandleA` and `GetProcAddress` on obfuscated strings to hide the malware's functional capabilities.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High (regarding the functional type; Low regarding a specific named family)
4. **Key evidence**:
    *   **Advanced Evasion Techniques:** The presence of `rdtsc` timing checks, XOR-based string decryption, and control flow flattening indicates a sophisticated attempt to bypass both automated sandboxes and manual reverse engineering.
    *   **Loader Characteristics:** The use of manual PE header parsing (`MZ`/`PE` signatures) combined with dynamic API resolution via `GetProcAddress` is highly characteristic of a loader/packer designed to unpack or inject a secondary, malicious payload into memory while hiding its functionality from the Import Address Table (IAT).
