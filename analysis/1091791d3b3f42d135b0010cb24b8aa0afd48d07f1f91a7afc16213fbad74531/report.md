# Threat Analysis Report

**Generated:** 2026-08-19 20:28 UTC
**Sample:** `1091791d3b3f42d135b0010cb24b8aa0afd48d07f1f91a7afc16213fbad74531_1091791d3b3f42d135b0010cb24b8aa0afd48d07f1f91a7afc16213fbad74531.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1091791d3b3f42d135b0010cb24b8aa0afd48d07f1f91a7afc16213fbad74531_1091791d3b3f42d135b0010cb24b8aa0afd48d07f1f91a7afc16213fbad74531.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 12 sections |
| Size | 7,760,384 bytes |
| MD5 | `f1cb1f593bf5a7156ba7e182f32897ab` |
| SHA1 | `5cc9903f8e4cc8d3564cbe5e1cce82f74f06423e` |
| SHA256 | `1091791d3b3f42d135b0010cb24b8aa0afd48d07f1f91a7afc16213fbad74531` |
| Overall entropy | 7.929 |
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
| `.code1` | 7,757,312 | 7.93 | ⚠️ Yes |
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

Total strings found: **16140** (showing first 100)

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
i~}EJv-	/or
LocalAlloc
Dz
/A6i>
tc5 1B1
cM*$%X
CRYPT32.dll
N3N:mYfa
!Q+#:m]
N8@/,U
H*\!*7[R
}hBK~0
ri1m/2
T5ITNO-I!f/
5IrJBw
9I'WU?I
/R7Ip?T
0Izs9I3
jrDz&4
AivH&=4
k'Cr^tV
_;1DH-^=
c5IR$0
s<6:IY4
0FB;IA

dHt,k
4fQ&geJd
l5IIA1
``wa0Q
?IrCU6Ir
9Ia46I
n\e;Ick8
D/U
h
tU9ry
,+2qV
7^5Ng 
0xLPP3

?ezII
4Lc;
%b
GetVersionExA
il^SWeUE
1R3s<5
P~~$) a
-6 N5=
<v)/(w
5HJzFLx
$PIwYG
Z5^In0
ohk]O!
PU#z+K
1gI	_.
wQrn"
QEFsB[
:u'lKz
i$d1jcN
rIljih 
x+Ouy$3/yi
Ht\u92
HeB{]
kThBZA
5gc+zv
o
LE!
|:B+XM
quJ$=og
z#I:`a;I
mTNx_~
[e27J6I
uf'eU7O
?<|?A
tAp==D
#YP&A\
fkT/CL
/$l-7U
USER32.dll
dx
+Ea
eHuznVW\
&3tE"'3M
o$o@ >
!C^Rt!C@7
Z2C2?"
1	C89}
 2#X
 
4:[@dN
^?HfG
3H?kZB
vg1&nA
s;' n"
==46
p
&dl@FfLs*
qsq?6BM[x
4h~2.u]XY
i
}pXh
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry1` | `0x1412a6c0d` | 6111900 | ✓ |
| `fcn.141331409` | `0x141331409` | 3777758 | ✓ |
| `fcn.14147bc48` | `0x14147bc48` | 1340202 | ✓ |
| `fcn.141375f92` | `0x141375f92` | 1142689 | ✓ |
| `fcn.1413aa49e` | `0x1413aa49e` | 1126157 | ✓ |
| `fcn.14134f753` | `0x14134f753` | 1090582 | ✓ |
| `fcn.1414059c6` | `0x1414059c6` | 1070990 | ✓ |
| `fcn.1413b9297` | `0x1413b9297` | 1016406 | ✓ |
| `fcn.1413caa12` | `0x1413caa12` | 953752 | ✓ |
| `fcn.1413f7143` | `0x1413f7143` | 911731 | ✓ |
| `fcn.14144bf28` | `0x14144bf28` | 872947 | ✓ |
| `fcn.1413831c8` | `0x1413831c8` | 610858 | ✓ |
| `fcn.14140ec8a` | `0x14140ec8a` | 577230 | ✓ |
| `fcn.14144739d` | `0x14144739d` | 246207 | ✓ |
| `fcn.1414a7c25` | `0x1414a7c25` | 1063 | ✓ |
| `fcn.141490db5` | `0x141490db5` | 216 | ✓ |
| `fcn.14149dc25` | `0x14149dc25` | 173 | ✓ |
| `fcn.1414b54dc` | `0x1414b54dc` | 142 | ✓ |
| `entry0` | `0x1412d1171` | 137 | ✓ |
| `fcn.140f670ab` | `0x140f670ab` | 126 | ✓ |
| `fcn.140d6890f` | `0x140d6890f` | 124 | ✓ |
| `fcn.140f7adfd` | `0x140f7adfd` | 93 | ✓ |
| `fcn.1414a0423` | `0x1414a0423` | 75 | ✓ |
| `fcn.140f63120` | `0x140f63120` | 56 | ✓ |
| `fcn.140ec437e` | `0x140ec437e` | 41 | ✓ |
| `fcn.140daabf9` | `0x140daabf9` | 38 | ✓ |
| `fcn.14127dadd` | `0x14127dadd` | 37 | ✓ |
| `fcn.140fe2390` | `0x140fe2390` | 18 | ✓ |
| `sym.imp.IPHLPAPI.DLL_ConvertInterfaceIndexToLuid` | `0x141292030` | 16 | ✓ |
| `int.140e4da49` | `0x140e4da49` | 12 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/entry1.c`](code/entry1.c)
- [`code/fcn.140d6890f.c`](code/fcn.140d6890f.c)
- [`code/fcn.140daabf9.c`](code/fcn.140daabf9.c)
- [`code/fcn.140ec437e.c`](code/fcn.140ec437e.c)
- [`code/fcn.140f63120.c`](code/fcn.140f63120.c)
- [`code/fcn.140f670ab.c`](code/fcn.140f670ab.c)
- [`code/fcn.140f7adfd.c`](code/fcn.140f7adfd.c)
- [`code/fcn.140fe2390.c`](code/fcn.140fe2390.c)
- [`code/fcn.14127dadd.c`](code/fcn.14127dadd.c)
- [`code/fcn.141331409.c`](code/fcn.141331409.c)
- [`code/fcn.14134f753.c`](code/fcn.14134f753.c)
- [`code/fcn.141375f92.c`](code/fcn.141375f92.c)
- [`code/fcn.1413831c8.c`](code/fcn.1413831c8.c)
- [`code/fcn.1413aa49e.c`](code/fcn.1413aa49e.c)
- [`code/fcn.1413b9297.c`](code/fcn.1413b9297.c)
- [`code/fcn.1413caa12.c`](code/fcn.1413caa12.c)
- [`code/fcn.1413f7143.c`](code/fcn.1413f7143.c)
- [`code/fcn.1414059c6.c`](code/fcn.1414059c6.c)
- [`code/fcn.14140ec8a.c`](code/fcn.14140ec8a.c)
- [`code/fcn.14144739d.c`](code/fcn.14144739d.c)
- [`code/fcn.14144bf28.c`](code/fcn.14144bf28.c)
- [`code/fcn.14147bc48.c`](code/fcn.14147bc48.c)
- [`code/fcn.141490db5.c`](code/fcn.141490db5.c)
- [`code/fcn.14149dc25.c`](code/fcn.14149dc25.c)
- [`code/fcn.1414a0423.c`](code/fcn.1414a0423.c)
- [`code/fcn.1414a7c25.c`](code/fcn.1414a7c25.c)
- [`code/fcn.1414b54dc.c`](code/fcn.1414b54dc.c)
- [`code/int.140e4da49.c`](code/int.140e4da49.c)
- [`code/sym.imp.IPHLPAPI.DLL_ConvertInterfaceIndexToLuid.c`](code/sym.imp.IPHLPAPI.DLL_ConvertInterfaceIndexToLuid.c)

## Behavioral Analysis

Based on my analysis of the provided disassembly and decompiled code, here is a summary of the findings:

### Core Functionality and Purpose
The binary appears to be a sophisticated **malware loader or "packer."** Rather than performing its primary malicious actions directly (like stealing files or encrypting data), it spends most of its logic on anti-analysis, hiding its true functionality from security researchers, and preparing an environment to execute a secondary payload.

### Suspicious or Malicious Behaviors
*   **Anti-VM / Anti-Sandbox Detection:** 
    *   The function `entry1` contains explicit checks for common virtualization technologies. It searches for strings such as **"VirtualBox"**, **"VMware"**, and **"Parallels."** This is a classic technique used to detect if the malware is being analyzed in a virtual environment or by automated sandbox systems.
*   **Timing Attacks:**
    *   The inclusion of the `rdtsc` (Read Time-Stamp Counter) instruction indicates that the code likely measures how long specific instructions take to execute. This is often used to detect the presence of a debugger; if a process is slowed down significantly, it assumes a human analyst is stepping through the code and may shut itself down or change its behavior.
*   **Dynamic API Resolution:**
    *   The function `fcn.141331409` is a complex custom implementation for resolving Windows APIs at runtime. Instead of listing its functions in the standard Import Address Table (IAT), it uses **GetModuleHandleA** and **GetProcAddress**. 
    *   Crucially, it performs mathematical operations (XORing, bit-shifting) on function names before looking them up. This hides the malware's true capabilities from static analysis tools that look for "suspicious" API imports like `CreateRemoteThread` or `WriteProcessMemory`.

### Notable Techniques & Patterns
*   **Control Flow Obfuscation:** 
    *   Multiple functions (e.g., `fcn.141375f92`, `fcn.1413aa49e`) are flagged by the decompiler as having "too many branches" or "bad instruction data." This indicates the use of **junk code** and **overlapping instructions**. These are designed to break disassemblers (like IDA Pro or Ghidra) and make it extremely difficult for a human analyst to follow the logic.
*   **Arithmetic Obfuscation:** 
    *   The code frequently uses complex, multi-step arithmetic calculations to determine jump destinations rather than using direct jumps or standard labels. This is intended to hide the "roadmap" of the program's execution.
*   **String Manipulation/Encryption:** 
    *   While some strings are visible (like `CRYPT32.dll`), many segments appear as garbled text or are processed through loops before use, suggesting that most configuration data or commands are encrypted in memory and only decrypted when needed.

### Summary Conclusion
This is a **highly evasive piece of malware**. It utilizes professional-grade evasion techniques including:
1.  **Anti-Analysis:** Active detection of VirtualBox/VMware.
2.  **De-obfuscation Resistance:** Using "junk" instructions and complex math to break automated analysis tools.
3.  **Stealthy API Loading:** Hiding its intent by dynamically resolving and obfuscating the names of the Windows functions it calls.

The primary goal of this specific module is likely to bypass local security defenses and environmental checks before "unpacking" or "injecting" a second stage payload that performs the actual malicious activity.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtualization/Sandbox Evasion | The malware checks for environment-specific strings (VirtualBox, VMware) to detect and evade analysis environments. |
| T1497 | Virtualization/Sandbox Evasion | The use of the `rdtsc` instruction is a timing attack used to detect the presence of debuggers or emulators by measuring execution speed. |
| T1027 | Obfuscated Execution | The use of junk code and overlapping instructions is designed to break disassemblers and hinder manual analysis of the control flow. |
| T1027 | Obfuscated Execution | Dynamic API resolution with XOR/bit-shifting obscures the program's actual functionality from static analysis tools. |
| T1027 | Obfuscated Execution | The use of complex arithmetic to calculate jump destinations conceals the execution path from analysts. |
| T1027 | Obfuscated Execution | Encrypting strings and configuration data ensures that malicious behavior is only revealed in memory during runtime. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Many items in the "Extracted Strings" section were identified as standard system libraries (e.g., `CRYPT32.dll`, `USER32.dll`) or obfuscated junk data and have been excluded as false positives per your instructions.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: While DLL names like `CRYPT32.dll` and `USER32.dll` were present in the strings, these are standard Windows system files and do not constitute unique malicious artifacts.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (Behavioral IOCs)**
The following are behavioral indicators derived from the analysis of the malware's evasion techniques:

*   **Anti-VM/Sandbox Strings:** The binary actively searches for and checks against the following environment markers:
    *   `VirtualBox`
    *   `VMware`
    *   `Parallels`
*   **Timing Attack Indicator:** Use of the `rdtsc` instruction to detect the presence of debuggers or high-latency analysis environments.
*   **Dynamic API Resolution Patterns:** 
    *   Use of `GetModuleHandleA` and `GetProcAddress` combined with arithmetic obfuscation (XORing/bit-shifting) to hide the import of sensitive functions like `CreateRemoteThread` and `WriteProcessMemory`.
*   **Code Obfuscation Techniques:**
    *   **Junk Code/Overlapping Instructions:** Specifically noted in segments `fcn.141375f92` and `fcn.1413aa49e`.
    *   **Arithmetic Obfuscation:** Complex multi-step calculations used to determine jump destinations rather than direct labels.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Evasion Techniques:** The sample employs sophisticated anti-analysis methods, including specific checks for virtualization software (VirtualBox, VMware, Parallels) and the use of `rdtsc` timing attacks to detect debuggers.
*   **Heavy Obfuscation:** The code utilizes advanced techniques to hinder static analysis, such as junk code/overlapping instructions, complex arithmetic for jump destinations, and dynamic API resolution where function names are XORed/bit-shifted.
*   **Loader Functionality:** The primary purpose of the sample is identified as a loader or packer; it is designed to hide its presence and bypass security controls specifically to prepare an environment for a second-stage payload.
