# Threat Analysis Report

**Generated:** 2026-07-12 06:56 UTC
**Sample:** `04cf839bff11a9a7dbc73062fa35588a69c8dc2fa768e1083dd5a39d193c1285_04cf839bff11a9a7dbc73062fa35588a69c8dc2fa768e1083dd5a39d193c1285.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04cf839bff11a9a7dbc73062fa35588a69c8dc2fa768e1083dd5a39d193c1285_04cf839bff11a9a7dbc73062fa35588a69c8dc2fa768e1083dd5a39d193c1285.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 12 sections |
| Size | 7,780,352 bytes |
| MD5 | `1e93aa53d3a51120b702ba2b17b0745b` |
| SHA1 | `398aee5f0f1cd4a321f4d03f605664ef668f541a` |
| SHA256 | `04cf839bff11a9a7dbc73062fa35588a69c8dc2fa768e1083dd5a39d193c1285` |
| Overall entropy | 7.933 |
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
| `.code1` | 7,777,280 | 7.933 | ⚠️ Yes |
| `.rsrc` | 2,048 | 4.593 | No |

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

Total strings found: **15330** (showing first 100)

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
2y>S8h
E.f7xQ
p:P!K
_R501/2
]:HkBf
KE$[x]2
LoadLibraryA
.H	t7ys
tP.%71
u/C -3
~
}f&-Y	
VNvtD{
'7L.4f
v
9D"
3MD@+1:k
Ejm3lKt
Eh[^Kq
'0=z)
:h^prl
>q,oeCJ[
ito?OM6
Y>5+vdEq
}1.:hoM
pq5xy>
3L1Ej
(o?$\i*N
81wGG{~'
TW kyKX
Ww1A(g
p9jM"{
A0:y?,
@2HTDT4
-]gg?
U	3=Nu
qq2E@8%
xX
8K3tg
Odcl_j
NM{yk1
Nu#ed1

1pShI
m1d4tf
{vp[dQ8.
G5#m=g8!

&d"XzW
6?*0A7
TG9u]ep
3MO{^)
s
_:X6iZ
q`}G6
%e*d@'
}INvzD
+\@Y<)
FreeAddrInfoW
c1^kGa
T!9l14
r,YF.OX
*1<Z6+
xl'	*o
.I,@^1
B>dD#I'w
R2Np@
RQ61iZ
d@F2.w
teS,j6
u~D*2u
WS2_32.dll
dBcw'w
3tw!MV
dOH	.wR^
GRuU5m
:k95"Q
#{"Hdw@
@!wbx^U
#UNfM|O
i[p".4
5<$@yu
.ID!O n
X9twZW\
VDvJQU>)C
LFb;w	
	)E]rx
=.,	ZX,
q61wX
___lc_codepage_func
Pr	*/?
#T^=wr
w%XN9-l
5@1,0Kh!
8l	),W
j`i;z&
c'ww}S
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1413372cc` | `0x1413372cc` | 2826619 | ✓ |
| `fcn.1413d0228` | `0x1413d0228` | 1346668 | ✓ |
| `fcn.14146a01f` | `0x14146a01f` | 1252793 | ✓ |
| `fcn.1414486bb` | `0x1414486bb` | 1098278 | ✓ |
| `fcn.1413b1e54` | `0x1413b1e54` | 979123 | ✓ |
| `fcn.1413aa9d8` | `0x1413aa9d8` | 965771 | ✓ |
| `fcn.141396825` | `0x141396825` | 741493 | ✓ |
| `fcn.141442c35` | `0x141442c35` | 724824 | ✓ |
| `fcn.1413f5f87` | `0x1413f5f87` | 528449 | ✓ |
| `fcn.1413f5952` | `0x1413f5952` | 484015 | ✓ |
| `fcn.14139f908` | `0x14139f908` | 390236 | ✓ |
| `fcn.141373c87` | `0x141373c87` | 369683 | ✓ |
| `fcn.1414ac985` | `0x1414ac985` | 1063 | ✓ |
| `fcn.1414b1d5d` | `0x1414b1d5d` | 456 | ✓ |
| `fcn.1411dace0` | `0x1411dace0` | 349 | ✓ |
| `int.140dfa4a8` | `0x140dfa4a8` | 225 | ✓ |
| `fcn.141495b15` | `0x141495b15` | 216 | ✓ |
| `fcn.140eec006` | `0x140eec006` | 213 | ✓ |
| `fcn.140f02b8a` | `0x140f02b8a` | 187 | ✓ |
| `fcn.1414a2985` | `0x1414a2985` | 173 | ✓ |
| `fcn.141279b4b` | `0x141279b4b` | 166 | ✓ |
| `fcn.140f3f880` | `0x140f3f880` | 148 | ✓ |
| `fcn.141144dd8` | `0x141144dd8` | 129 | ✓ |
| `fcn.14112fe48` | `0x14112fe48` | 124 | ✓ |
| `entry1` | `0x1410a7425` | 113 | ✓ |
| `fcn.1414a5183` | `0x1414a5183` | 75 | ✓ |
| `fcn.140d60c99` | `0x140d60c99` | 70 | ✓ |
| `fcn.1412d4a4d` | `0x1412d4a4d` | 59 | ✓ |
| `sym.imp.IPHLPAPI.DLL_ConvertInterfaceIndexToLuid` | `0x140db0030` | 40 | ✓ |
| `fcn.140fed9f1` | `0x140fed9f1` | 18 | ✓ |

### Decompiled Code Files

- [`code/entry1.c`](code/entry1.c)
- [`code/fcn.140d60c99.c`](code/fcn.140d60c99.c)
- [`code/fcn.140eec006.c`](code/fcn.140eec006.c)
- [`code/fcn.140f02b8a.c`](code/fcn.140f02b8a.c)
- [`code/fcn.140f3f880.c`](code/fcn.140f3f880.c)
- [`code/fcn.140fed9f1.c`](code/fcn.140fed9f1.c)
- [`code/fcn.14112fe48.c`](code/fcn.14112fe48.c)
- [`code/fcn.141144dd8.c`](code/fcn.141144dd8.c)
- [`code/fcn.1411dace0.c`](code/fcn.1411dace0.c)
- [`code/fcn.141279b4b.c`](code/fcn.141279b4b.c)
- [`code/fcn.1412d4a4d.c`](code/fcn.1412d4a4d.c)
- [`code/fcn.1413372cc.c`](code/fcn.1413372cc.c)
- [`code/fcn.141373c87.c`](code/fcn.141373c87.c)
- [`code/fcn.141396825.c`](code/fcn.141396825.c)
- [`code/fcn.14139f908.c`](code/fcn.14139f908.c)
- [`code/fcn.1413aa9d8.c`](code/fcn.1413aa9d8.c)
- [`code/fcn.1413b1e54.c`](code/fcn.1413b1e54.c)
- [`code/fcn.1413d0228.c`](code/fcn.1413d0228.c)
- [`code/fcn.1413f5952.c`](code/fcn.1413f5952.c)
- [`code/fcn.1413f5f87.c`](code/fcn.1413f5f87.c)
- [`code/fcn.141442c35.c`](code/fcn.141442c35.c)
- [`code/fcn.1414486bb.c`](code/fcn.1414486bb.c)
- [`code/fcn.14146a01f.c`](code/fcn.14146a01f.c)
- [`code/fcn.141495b15.c`](code/fcn.141495b15.c)
- [`code/fcn.1414a2985.c`](code/fcn.1414a2985.c)
- [`code/fcn.1414a5183.c`](code/fcn.1414a5183.c)
- [`code/fcn.1414ac985.c`](code/fcn.1414ac985.c)
- [`code/fcn.1414b1d5d.c`](code/fcn.1414b1d5d.c)
- [`code/int.140dfa4a8.c`](code/int.140dfa4a8.c)
- [`code/sym.imp.IPHLPAPI.DLL_ConvertInterfaceIndexToLuid.c`](code/sym.imp.IPHLPAPI.DLL_ConvertInterfaceIndexToLuid.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The primary purpose of the code visible in this sample is **evasion and stealth**. The code does not perform high-level logic (like file manipulation or network communication) directly; instead, it focuses on "preparing" the environment by hiding its own functionality from security tools.

### Suspicious and Malicious Behaviors
*   **Dynamic API Resolution:** Function `fcn.1413372cc` is a sophisticated custom implementation of `GetProcAddress`. 
    *   It manually parses the Export Directory of loaded modules (checking for "MZ" and "PE" headers).
    *   Instead of using standard strings, it uses an **alphanumeric/hash-based lookup** (the loop involving `0x2f185dac`). This allows the malware to call system functions without those function names appearing in the Import Address Table (IAT), making static analysis significantly harder.
*   **Anti-Analysis/Anti-Debugging:** 
    *   The inclusion of `rdtsc()` in `fcn.1396825` is a classic timing check. It measures the time elapsed between two points; if the gap is too large (as would occur if a researcher is stepping through code with a debugger), the malware may alter its behavior or exit.
    *   The presence of multiple "bad instruction" and "overlap" warnings in functions like `fcn.1414ac985` suggests the use of **junk code** or **metamorphic engines** to confuse disassemblers.
*   **Control Flow Obfuscation:** Several functions (e.g., `fcn.1413aa9d8`, `fcn.1414ac985`) exhibit complex, non-linear logic and "junk" instructions. This is a technique used to exhaust the analyst's time by creating a labyrinthine execution path that is difficult to follow manually.

### Notable Techniques & Patterns
*   **API Hiding:** By resolving functions at runtime using hashes rather than strings, the author ensures that automated tools cannot easily determine what capabilities (e.g., "InternetOpen", "WriteProcessMemory") the malware possesses until it is actually running.
*   **Packed/Obfuscated Structure:** The high volume of "broken" decompilation and complex math for simple operations suggests a heavy reliance on an obfuscation framework (like LLVM-based protectors) to shield the actual malicious payload.
*   **Self-Checking Logic:** The check `if (*piVar12 != 0x5a4d)` in the first function is a way to verify if a loaded module's header is valid before attempting to walk its exports, ensuring the malware doesn't crash when trying to find hidden functions.

### Summary Table
| Feature | Detection | Risk Level | Purpose |
| :--- | :--- | :--- | :--- |
| **Dynamic Resolution** | `fcn.1413372cc` (Manual Export Walk) | High | Evade static analysis by hiding API imports. |
| **Time-Based Anti-Debug** | `rdtsc()` | Medium | Detect and bypass debuggers/sandboxes. |
| **Code Obfuscation** | "Bad instruction" / Junk loops | High | Frustrate manual reverse engineering. |
| **Hash-based Lookup** | XOR loop in `fcn.1413372cc` | Medium | Hide intent by avoiding hardcoded strings. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of junk code, complex non-linear logic, and hash-based API lookups (instead of strings) is designed to hide the malware's capabilities from static analysis tools. |
| T1497 | Virtualized Environment Detection | The implementation of `rdtsc()` timing checks is used to detect if the binary is being executed in a debugger or an automated analysis sandbox. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the categorized list of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: `WS2_32.dll` and `GetUserProfileDirectoryW` were identified in the strings but are excluded as they are standard Windows system files/APIs).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (Note: The value `0x5a4d` appears in the text, but it is a standard "MZ" header signature used for identifying valid PE files, not a file hash).

### **Other artifacts**
*   **Anti-Analysis Patterns:**
    *   **Timing Check:** Use of the `rdtsc()` instruction to detect the presence of debuggers or sandboxes.
    *   **Custom GetProcAddress:** Implementation of a manual export directory walk (function `fcn.1413372cc`) to hide API calls from the Import Address Table (IAT).
*   **Obfuscation Constants:**
    *   **Hash/XOR Constant:** The value `0x2f185dac` is used in a loop for hash-based lookups of system functions.
    *   **Junk Code:** Presence of "bad instructions" and non-linear logic designed to frustrate automated decompilers and manual analysis.

---

## Malware Family Classification

1. **Malware family**: unknown
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
*   **Advanced Evasion Techniques:** The use of custom `GetProcAddress` implementations (manual export directory walking) and hash-based lookup tables indicates a sophisticated attempt to hide functionality from static analysis and automated tools.
*   **Anti-Analysis Measures:** The inclusion of `rdtsc()` timing checks and the deliberate insertion of "junk" code/bad instructions are classic indicators of a sample designed to detect debuggers and frustrate reverse engineers.
*   **Loader Characteristics:** The lack of immediate malicious actions (no hardcoded C2 infrastructure, file encryption logic, or direct data exfiltration) combined with heavy obfuscation suggests this binary serves as a "loader" or "dropper," intended to unpack and execute the actual malicious payload in memory.
