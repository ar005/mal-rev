# Threat Analysis Report

**Generated:** 2026-08-21 20:23 UTC
**Sample:** `10f7f483512029d6a7ceecc154c9cb8bda6d34fa65dfbd2c67a49c12e763449a_10f7f483512029d6a7ceecc154c9cb8bda6d34fa65dfbd2c67a49c12e763449a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10f7f483512029d6a7ceecc154c9cb8bda6d34fa65dfbd2c67a49c12e763449a_10f7f483512029d6a7ceecc154c9cb8bda6d34fa65dfbd2c67a49c12e763449a.exe` |
| File type | PE32+ executable for MS Windows 5.02 (DLL), x86-64 (stripped to external PDB), 12 sections |
| Size | 59,392 bytes |
| MD5 | `95f347900d08f9e80602e6f545105984` |
| SHA1 | `e64409b33b4f864400a96ffff6b36af80a588f32` |
| SHA256 | `10f7f483512029d6a7ceecc154c9cb8bda6d34fa65dfbd2c67a49c12e763449a` |
| Overall entropy | 7.337 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1651856023 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 10,240 | 6.046 | No |
| `.data` | 512 | 2.933 | No |
| `.rdata` | 39,936 | 7.962 | ⚠️ Yes |
| `.pdata` | 1,024 | 3.308 | No |
| `.xdata` | 1,024 | 2.664 | No |
| `.bss` | 0 | 0.0 | No |
| `.edata` | 1,024 | 3.314 | No |
| `.idata` | 2,048 | 3.605 | No |
| `.CRT` | 512 | 0.249 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 1,024 | 2.906 | No |
| `.reloc` | 512 | 1.092 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `CreateFileA`, `DeleteCriticalSection`, `DeleteFileA`, `EnterCriticalSection`, `FlushInstructionCache`, `GetCurrentProcess`, `GetFileSize`, `GetLastError`, `GetModuleFileNameA`, `GetModuleHandleExA`, `GetTickCount`, `InitializeCriticalSection`, `LeaveCriticalSection`, `QueryPerformanceCounter`
**msvcrt.dll**: `__iob_func`, `_amsg_exit`, `_initterm`, `_lock`, `_unlock`, `abort`, `calloc`, `free`, `fwrite`, `memcpy`, `memset`, `realloc`, `strcpy`, `strlen`, `strncmp`
**USER32.dll**: `DispatchMessageA`, `GetMessageA`, `TranslateMessage`

### Exports

`GetFileVersionInfoA`, `GetFileVersionInfoByHandle`, `GetFileVersionInfoExA`, `GetFileVersionInfoExW`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoSizeExA`, `GetFileVersionInfoSizeExW`, `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`, `VerFindFileA`, `VerFindFileW`, `VerInstallFileA`, `VerInstallFileW`, `VerLanguageNameA`, `VerLanguageNameW`, `VerQueryValueA`, `VerQueryValueW`

## Extracted Strings

Total strings found: **207** (showing first 100)

```
`.data
.rdata
@.pdata
@.xdata
.edata
@.idata
.reloc
AUATUWVSH
([^_]A\A]
([^_]A\A]
([^_]A\A]
AVAUATVSH
 [^A\A]A^
ATVSeH
9MZukHcQ<
AWAVAUATWVSH
[^_A\A]A^A_
AWAVAUATUWVSH
gfffffffL
L+D$xH
[^_]A\A]A^A_
Ic|$<L
ATUWVSH
P[^_]A\
P[^_]A\
UAWAVAUATWVSH
[^_A\A]A^A_]
ATWVSH
([^_A\H
tNHcA<H
tTIcB<L
t	HcA<
tCHcA<H
@' t	M
tKIcA<L
tSIcK<L
}PC0_M'
rOYE|
7QnsTO|~u
!V0NUf
<*x=oN
,,cujM
&.EKw{
^sFZm
@e1/	X}
:{i7e.
]X~s~~[
Ki\B"6
2yu-4V
2j^9)t
c*g#7q
vZ:"" (
f`3fu~
k	xQ5W
Wat;n
/RVyC[<!t>
3Htu/` =
T.M\,d
p<_'*<Wc
%k-?v:
U\Nh1_
[tnEZ'
8+B4Q-Z
6q* Ow
VUv.A%
,6.Q5{
+YxY!+(
*EW[ Zg"F
~xil	C
-@6)|0.
/PERP>
q&v61f@
7@Y,~9r
*%"f>H
1-OpEF
*z{Y%

#GnYzb$[Z
$Ig^twY/
c2-Hpet
CaqPA
%.g-}
~}OdG
!(r
4C
Zmh_pn
yR Why
Qpr$1-
BB-+Z3
q'T2	N
9ML^&he
4Fdy#`-
W,GOLi
ZO
EO[R
XM^z||D&p
uP<g9U
a8?}k 
_#`L*^
U-}Hfe
1<'.0
Mg|RGhO
7)#\6E
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.23c472680` | `0x23c472680` | 8708 | ✓ |
| `fcn.23c471c20` | `0x23c471c20` | 1544 | ✓ |
| `fcn.23c471820` | `0x23c471820` | 804 | ✓ |
| `fcn.23c472a70` | `0x23c472a70` | 752 | ✓ |
| `fcn.23c472850` | `0x23c472850` | 544 | ✓ |
| `fcn.23c471010` | `0x23c471010` | 495 | ✓ |
| `entry0` | `0x23c471350` | 354 | ✓ |
| `fcn.23c471500` | `0x23c471500` | 329 | ✓ |
| `fcn.23c472ee0` | `0x23c472ee0` | 224 | ✓ |
| `fcn.23c471b50` | `0x23c471b50` | 206 | ✓ |
| `fcn.23c4713a0` | `0x23c4713a0` | 171 | ✓ |
| `fcn.23c471450` | `0x23c471450` | 162 | ✓ |
| `fcn.23c471780` | `0x23c471780` | 156 | ✓ |
| `fcn.23c4716e0` | `0x23c4716e0` | 153 | ✓ |
| `fcn.23c471650` | `0x23c471650` | 135 | ✓ |
| `entry1` | `0x23c472740` | 129 | ✓ |
| `fcn.23c4730f0` | `0x23c4730f0` | 129 | ✓ |
| `fcn.23c4725a0` | `0x23c4725a0` | 124 | ✓ |
| `fcn.23c473580` | `0x23c473580` | 113 | ✓ |
| `fcn.23c4727e0` | `0x23c4727e0` | 112 | ✓ |
| `fcn.23c472d60` | `0x23c472d60` | 107 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoSizeA` | `0x23c4722f0` | 57 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoSizeExA` | `0x23c472330` | 57 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoSizeExW` | `0x23c472370` | 57 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoSizeW` | `0x23c4723b0` | 57 | ✓ |
| `fcn.23c4733b0` | `0x23c4733b0` | 50 | ✓ |
| `entry2` | `0x23c472710` | 47 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoA` | `0x23c472230` | 46 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoByHandle` | `0x23c472260` | 46 | ✓ |
| `sym.VERSION.dll_GetFileVersionInfoExA` | `0x23c472290` | 46 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/entry1.c`](code/entry1.c)
- [`code/entry2.c`](code/entry2.c)
- [`code/fcn.23c471010.c`](code/fcn.23c471010.c)
- [`code/fcn.23c4713a0.c`](code/fcn.23c4713a0.c)
- [`code/fcn.23c471450.c`](code/fcn.23c471450.c)
- [`code/fcn.23c471500.c`](code/fcn.23c471500.c)
- [`code/fcn.23c471650.c`](code/fcn.23c471650.c)
- [`code/fcn.23c4716e0.c`](code/fcn.23c4716e0.c)
- [`code/fcn.23c471780.c`](code/fcn.23c471780.c)
- [`code/fcn.23c471820.c`](code/fcn.23c471820.c)
- [`code/fcn.23c471b50.c`](code/fcn.23c471b50.c)
- [`code/fcn.23c471c20.c`](code/fcn.23c471c20.c)
- [`code/fcn.23c4725a0.c`](code/fcn.23c4725a0.c)
- [`code/fcn.23c472680.c`](code/fcn.23c472680.c)
- [`code/fcn.23c4727e0.c`](code/fcn.23c4727e0.c)
- [`code/fcn.23c472850.c`](code/fcn.23c472850.c)
- [`code/fcn.23c472a70.c`](code/fcn.23c472a70.c)
- [`code/fcn.23c472d60.c`](code/fcn.23c472d60.c)
- [`code/fcn.23c472ee0.c`](code/fcn.23c472ee0.c)
- [`code/fcn.23c4730f0.c`](code/fcn.23c4730f0.c)
- [`code/fcn.23c4733b0.c`](code/fcn.23c4733b0.c)
- [`code/fcn.23c473580.c`](code/fcn.23c473580.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoA.c`](code/sym.VERSION.dll_GetFileVersionInfoA.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoByHandle.c`](code/sym.VERSION.dll_GetFileVersionInfoByHandle.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoExA.c`](code/sym.VERSION.dll_GetFileVersionInfoExA.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoSizeA.c`](code/sym.VERSION.dll_GetFileVersionInfoSizeA.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoSizeExA.c`](code/sym.VERSION.dll_GetFileVersionInfoSizeExA.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoSizeExW.c`](code/sym.VERSION.dll_GetFileVersionInfoSizeExW.c)
- [`code/sym.VERSION.dll_GetFileVersionInfoSizeW.c`](code/sym.VERSION.dll_GetFileVersionInfoSizeW.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, this binary is a **malware loader/packer** designed to decrypt and execute a secondary payload. It employs several common evasion and unpacking techniques.

### Core Functionality
The primary purpose of this code is to serve as a "stub." It prepares the environment by decrypting its own internal strings and resources, performing anti-analysis checks, and then locating and loading an encrypted component (likely a DLL or another executable) from the local filesystem to perform the actual malicious activity.

### Suspicious & Malicious Behaviors
*   **Multi-Stage Unpacking:** 
    *   The code uses multiple "entry" points (`entry0`, `entry1`, `entry2`) and internal initialization functions (e.g., `fcn.23c471500`) to decrypt various segments of the binary before they are used.
    *   **`fcn.23c471650`** is a dedicated string decryption routine, using an XOR operation (`^ 0x74`) to de-obfuscate hardcoded strings into plain text.
    *   **`fcn.23c471b50`** performs more complex block decryption on data buffers using a stack-based key.
*   **Memory Manipulation (Unpacking/Injection):** 
    *   The function **`fcn.23c472a70`** heavily utilizes `VirtualProtect`. It iterates through memory regions and changes their protection attributes, which is a signature of a packer transitioning "de-obfuscated" data into "executable" code.
    *   The code references internal pointers (e.g., `*0x23c481060`) that appear to be dynamically resolved functions used for handling the decrypted payload.
*   **Anti-Analysis & Anti-Debugging:** 
    *   In **`fcn.23c471c20`**, the code compares the results of `QueryPerformanceCounter` against a calculated threshold. This is a common **timing check** used to detect if the code is being slowed down by a debugger or an analyst's monitoring tools.
    *   The use of `GetTickCount` and then performing math on the difference between time sources is another method to detect "stepping" through the code in a debugger.
*   **Hidden File Loading:** 
    *   **`fcn.23c471820`** identifies the directory where the current binary resides using `GetModuleFileNameA`, appends a name, and then opens/reads a file from that location. This is typical of a loader looking for an encrypted payload (e.g., `payload.dat` or a secondary DLL).

### Notable Techniques & Patterns
*   **XOR-Based Encryption:** The sample uses basic XOR gates to hide both its internal logic and the strings it uses for communication or file system interaction.
*   **API Obfuscation/Abstraction:** Many calls are made through internal pointers (like `0x23c481088`) rather than directly calling Windows APIs, which helps bypass simple automated scan tools that look for common malicious API imports.
*   **Runtime De-obfuscation:** The heavy presence of memory-scanning loops and `VirtualProtect` calls indicates the binary is "unpacking" itself in real-time to hide its true intent from static analysis.

### Summary for Threat Intelligence
This sample belongs to a **Loader/Dropper** class of malware. It does not perform final actions (like stealing files or contacting C2 servers) directly; instead, it focuses on **evading detection** and **decrypting internal components**. The presence of timing checks and XOR-loop decryption suggests it is designed to bypass automated sandboxes and basic static analysis tools.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027.001 | Obfuscated Files or Information: Packing | The binary uses multi-stage unpacking, XOR-based string decryption, and `VirtualProtect` to hide its payload and true functionality from static analysis. |
| T1497 | Debugger Detection | The use of `QueryPerformanceCounter` and `GetTickCount` are implemented as timing checks to detect if the code is being monitored or "stepped" through by an analyst. |
| T1106 | Dynamic Resolution | Calling functions via internal pointers rather than directly importing them from the Windows API helps bypass automated scanners that look for known malicious imports. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Many of the raw strings provided appear to be obfuscated data or "junk" code designed to hinder static analysis; since they do not resolve to known URLs, IPs, or file paths in the provided text, they have been excluded as per your instructions.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The analysis notes that a local directory is used for payload loading via `GetModuleFileNameA`, but no specific file names or paths were provided in the text.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (Techniques & Patterns)**
*   **XOR Decryption Key:** `0x74` (Used in routine `fcn.23c471650` to de-obfuscate strings).
*   **Memory Manipulation:** Use of `VirtualProtect` to transition "de-obfuscated" data into executable memory segments.
*   **Anti-Analysis/Timing Checks:** 
    *   Usage of `QueryPerformanceCounter` compared against a threshold to detect debugger slowdowns.
    *   Comparison of `GetTickCount` values to identify "stepped" execution.
*   **API Obfuscation:** The use of internal function pointers (e.g., `0x23c481088`) rather than direct API calls to evade automated signature detection.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High (regarding the functionality; Low regarding specific threat actor attribution)
4. **Key evidence**: 
*   **Multi-Stage Unpacking & Decryption:** The binary functions as a "stub" that uses XOR operations and `VirtualProtect` to decrypt internal strings and transition de-obfuscated data into executable memory, which is characteristic of a loader or packer.
*   **Anti-Analysis Mechanisms:** The inclusion of timing checks (using `QueryPerformanceCounter` and `GetTickCount`) specifically designed to detect the presence of debuggers or analysis environments confirms its role in evading security measures.
*   **Evasive Execution:** Use of internal function pointers rather than direct API calls, combined with a routine to resolve local file paths for secondary payloads, indicates a primary goal of masking its final payload until runtime.
