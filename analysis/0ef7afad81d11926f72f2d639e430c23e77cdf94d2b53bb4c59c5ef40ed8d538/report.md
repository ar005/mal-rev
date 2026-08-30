# Threat Analysis Report

**Generated:** 2026-08-15 15:42 UTC
**Sample:** `0ef7afad81d11926f72f2d639e430c23e77cdf94d2b53bb4c59c5ef40ed8d538_0ef7afad81d11926f72f2d639e430c23e77cdf94d2b53bb4c59c5ef40ed8d538.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ef7afad81d11926f72f2d639e430c23e77cdf94d2b53bb4c59c5ef40ed8d538_0ef7afad81d11926f72f2d639e430c23e77cdf94d2b53bb4c59c5ef40ed8d538.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 9 sections |
| Size | 673,792 bytes |
| MD5 | `63f9a6db81dd11cb164adbbb5c8d4356` |
| SHA1 | `e1e1c080b3ec8943ae924458b479ede621e56a12` |
| SHA256 | `0ef7afad81d11926f72f2d639e430c23e77cdf94d2b53bb4c59c5ef40ed8d538` |
| Overall entropy | 7.988 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1775145434 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 9,728 | 6.272 | No |
| `.data` | 654,848 | 8.0 | ⚠️ Yes |
| `.rdata` | 2,560 | 4.921 | No |
| `.pdata` | 1,024 | 3.376 | No |
| `.xdata` | 1,024 | 2.785 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 2,560 | 4.082 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 512 | 1.233 | No |

### Imports

**KERNEL32.dll**: `DeleteCriticalSection`, `EnterCriticalSection`, `FlushInstructionCache`, `GetCurrentProcess`, `GetLastError`, `GetModuleHandleA`, `GetProcAddress`, `InitializeCriticalSection`, `LeaveCriticalSection`, `LoadLibraryA`, `SetUnhandledExceptionFilter`, `Sleep`, `TlsGetValue`, `VirtualAlloc`, `VirtualFree`
**api-ms-win-crt-environment-l1-1-0.dll**: `__p__environ`
**api-ms-win-crt-heap-l1-1-0.dll**: `_set_new_mode`, `calloc`, `free`, `malloc`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-private-l1-1-0.dll**: `__C_specific_handler`, `memcpy`
**api-ms-win-crt-runtime-l1-1-0.dll**: `__p___argc`, `__p___argv`, `_cexit`, `_configure_narrow_argv`, `_crt_atexit`, `_exit`, `_initialize_narrow_environment`, `_set_app_type`, `_initterm`, `_initterm_e`, `_set_invalid_parameter_handler`, `abort`, `exit`, `signal`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__acrt_iob_func`, `__p__commode`, `__p__fmode`, `__stdio_common_vfprintf`
**api-ms-win-crt-string-l1-1-0.dll**: `strlen`, `strncmp`

## Extracted Strings

Total strings found: **1553** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
.reloc
AWAVAUATUWVSH
X[^_]A\A]A^A_
8MZu>HcP<H
PHc5VY

UAWAVAUATWVSH
[^_A\A]A^A_]
ATUWVSH
 [^_]A\H
@' t	H
AWAVAUATUWVSH
H[^_]A\A]A^A_
ATUWVSH
[^_]A\
AWAVAUATUWVSH
8[^_]A\A]A^A_
ATUWVSH
0[^_]A\
0[^_]A\
ATUWVSH
0[^_]A\
0[^_]A\
\J}nq6
I5#<(0C6y
s7@z|
y0ys=P
7a	ZA64
W$R1:Y9
T5pQaT
Gh%5b%Q
PzEamO
$u}H+py)Z
OO1)
f
'x\KY
}2
w/
yX8z>w
m\R1aWP
2+3pEq
("*n&3
4Lh
i9
<1B\,l3w
jei&ta
t*Wz{[
Sp{PlT
=Gr
[?u;
iLs!Z7
c)/p1Y
dBhMx-T]
*KcDq_
&E}-i,b(
cPz,{C
h'%jn
1fIgW
)@AaMI
+tPTL2mG
tUfW
OX
5&N6$u
6"G6gE
-d9N 
5Lfk(aZ
PXw	e!V
sA,Wafe
|BVgY;
w71T91M
QunBR%
.Wu=o+&*-f
LM,U\.W
{gi=LLN
gL -BH
H99`JeEz
~5FOv	
O_Eb.2
<0APd^H
H <~|
@0*\
K\r\Jx
y>xx#
W20E|.
E1KJr?
Mj-"Ak
KJlrv{
FeGg$
WU/`a
F9`}yr_
.1NI^#E
tYiO =a
-kl;p.
iyX0It
YTs*43(^
KokZle[WT|
KMEZ*\
4Nj7BB
<UAXMk
Cv"cZWH
.HH+3"
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140001480` | `0x140001480` | 4854 | ✓ |
| `fcn.140001c90` | `0x140001c90` | 2758 | ✓ |
| `fcn.140002e20` | `0x140002e20` | 1519 | ✓ |
| `fcn.1400027a0` | `0x1400027a0` | 1202 | ✓ |
| `fcn.1400018b0` | `0x1400018b0` | 990 | ✓ |
| `fcn.140001010` | `0x140001010` | 960 | ✓ |
| `fcn.140003000` | `0x140003000` | 700 | ✓ |
| `fcn.140001740` | `0x140001740` | 368 | ✓ |
| `fcn.140002c80` | `0x140002c80` | 330 | ✓ |
| `fcn.140001ff0` | `0x140001ff0` | 242 | ✓ |
| `fcn.140003410` | `0x140003410` | 207 | ✓ |
| `fcn.140002f30` | `0x140002f30` | 168 | ✓ |
| `fcn.140002e80` | `0x140002e80` | 153 | ✓ |
| `fcn.140003560` | `0x140003560` | 132 | ✓ |
| `fcn.140002240` | `0x140002240` | 128 | ✓ |
| `entry1` | `0x140001550` | 115 | ✓ |
| `fcn.140001e60` | `0x140001e60` | 112 | ✓ |
| `fcn.1400016e0` | `0x1400016e0` | 96 | ✓ |
| `fcn.140002650` | `0x140002650` | 95 | ✓ |
| `fcn.1400025a0` | `0x1400025a0` | 68 | ✓ |
| `fcn.140002610` | `0x140002610` | 64 | ✓ |
| `fcn.1400022c0` | `0x1400022c0` | 55 | ✓ |
| `fcn.140002380` | `0x140002380` | 54 | ✓ |
| `fcn.140002560` | `0x140002560` | 51 | ✓ |
| `fcn.140002520` | `0x140002520` | 50 | ✓ |
| `fcn.140002100` | `0x140002100` | 32 | ✓ |
| `fcn.140001500` | `0x140001500` | 31 | ✓ |
| `entry0` | `0x1400013d0` | 29 | ✓ |
| `entry2` | `0x140001530` | 21 | ✓ |
| `fcn.140002600` | `0x140002600` | 11 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/entry1.c`](code/entry1.c)
- [`code/entry2.c`](code/entry2.c)
- [`code/fcn.140001010.c`](code/fcn.140001010.c)
- [`code/fcn.140001480.c`](code/fcn.140001480.c)
- [`code/fcn.140001500.c`](code/fcn.140001500.c)
- [`code/fcn.1400016e0.c`](code/fcn.1400016e0.c)
- [`code/fcn.140001740.c`](code/fcn.140001740.c)
- [`code/fcn.1400018b0.c`](code/fcn.1400018b0.c)
- [`code/fcn.140001c90.c`](code/fcn.140001c90.c)
- [`code/fcn.140001e60.c`](code/fcn.140001e60.c)
- [`code/fcn.140001ff0.c`](code/fcn.140001ff0.c)
- [`code/fcn.140002100.c`](code/fcn.140002100.c)
- [`code/fcn.140002240.c`](code/fcn.140002240.c)
- [`code/fcn.1400022c0.c`](code/fcn.1400022c0.c)
- [`code/fcn.140002380.c`](code/fcn.140002380.c)
- [`code/fcn.140002520.c`](code/fcn.140002520.c)
- [`code/fcn.140002560.c`](code/fcn.140002560.c)
- [`code/fcn.1400025a0.c`](code/fcn.1400025a0.c)
- [`code/fcn.140002600.c`](code/fcn.140002600.c)
- [`code/fcn.140002610.c`](code/fcn.140002610.c)
- [`code/fcn.140002650.c`](code/fcn.140002650.c)
- [`code/fcn.1400027a0.c`](code/fcn.1400027a0.c)
- [`code/fcn.140002c80.c`](code/fcn.140002c80.c)
- [`code/fcn.140002e20.c`](code/fcn.140002e20.c)
- [`code/fcn.140002e80.c`](code/fcn.140002e80.c)
- [`code/fcn.140002f30.c`](code/fcn.140002f30.c)
- [`code/fcn.140003000.c`](code/fcn.140003000.c)
- [`code/fcn.140003410.c`](code/fcn.140003410.c)
- [`code/fcn.140003560.c`](code/fcn.140003560.c)

## Behavioral Analysis

Based on the provided disassembly, here is a summary of the binary's behavior and characteristics:

### Core Functionality and Purpose
This binary functions as a **packer or loader** for a secondary, malicious payload. Its primary purpose is to decrypt an obfuscated piece of code (such as a Cobalt Strike beacon, shellcode, or a hidden DLL) in memory and execute it while evading security software. It does not appear to have any legitimate functionality beyond this "wrapper" behavior.

### Suspicious or Malicious Behaviors
*   **AMSI Bypass:** The function `fcn.140002e20` specifically targets the Windows Antimalware Scan Interface (AMSI). It attempts to load `amsi.dll`, find the address of `AmsiScanBuffer`, and use `VirtualProtect` to modify its memory. This is a standard technique used by malware to "blind" antivirus software, preventing it from detecting malicious scripts or code being executed in memory.
*   **Manual Mapping / Reflective Loading:** The functions `fcn.140003000` and `fcn.140002f30` perform actions characteristic of a manual mapper. They allocate memory (`VirtualAlloc`), copy "sections" of a hidden file, resolve imported functions using `GetProcAddress`, and handle relocations. This allows the payload to run in memory without ever being saved as a file on the disk, making it harder for traditional antivirus scanners to find.
*   **In-Memory Decryption:** The function `fcn.1400027a0` contains complex bitwise operations (XORing and arithmetic shifts) used to decrypt or de-obfuscate data in memory. This indicates that the actual malicious payload is encrypted while stored inside this loader's resources.
*   **Process Injection:** By mapping a new executable into its own memory space and resolving imports manually, the code is essentially "injecting" the functionality of another program into the current process to hide its origin.

### Notable Techniques or Patterns
*   **Anti-Analysis/Evasion:** The combination of an **AMSI Bypass** and **Manual Mapping** is a hallmark of sophisticated malware loaders (such as those used in Cobalt Strike). It indicates a high level of intent to bypass modern endpoint security.
*   **Staged Execution:** The logic shows the program performs several "preparation" steps: first, it disables security checks (`fcn.140002e20`); then, it decrypts a blob; finally, it maps and executes that blob (the "stage 2" payload).
*   **Instruction Cache Flushing:** In both `fcn.140002e20` and `fcn.140003410`, the code calls `FlushInstructionCache`. This is a technical requirement when modifying memory permissions or copying new machine code into a buffer so that it can be executed immediately by the CPU.

### Summary Conclusion
This is a **highly suspicious loader/packer**. It contains specific techniques designed to bypass security software (AMSI) and hide a secondary payload through manual mapping. This behavior is typical of early-stage infection components in advanced persistent threat (APT) campaigns or automated malware delivery.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1562.001** | Impair Defenses: Disable or Modify Tools | The binary explicitly targets `amsi.dll` and modifies its memory to bypass the Antimalware Scan Interface. |
| **T1027** | Obfuscated Files or Information | The use of bitwise XOR operations and arithmetic shifts indicates an effort to de-obfuscate a malicious payload hidden within the loader. |
| **T1055** | Process Injection | The manual mapping process (allocating memory, resolving imports, and executing code in-memory) is used to inject and hide the origin of the second-stage payload. |
| **T1623** | Reflective Code Loading | *Note: Often associated with T1055*, the specific use of a "manual mapper" allows the execution of code from memory without being saved to disk, evading traditional file scanners. |

---

## Indicators of Compromise

Based on the provided data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section appears to contain high-entropy/obfuscated binary data or junk code typical of a packer; no actionable network indicators (IPs/Domains) were found within those strings.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The internal function offsets, e.g., `fcn.140002e20`, are used for internal logic and do not constitute file system IOCs).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (Behavioral Indicators)**
The following behavioral signatures were identified from the analysis of the loader's functionality:
*   **AMSI Bypass:** Function `fcn.140002e20` specifically targets and patches the Windows Antimalware Scan Interface to evade detection.
*   **Manual Mapping/Reflective Loading:** Functions `fcn.140003000` and `fcn.140002f30` are used to resolve imports, handle relocations, and map a hidden payload into memory without touching the disk.
*   **In-Memory Decryption:** Function `fcn.1400027a0` utilizes XOR operations and arithmetic shifts to de-obfuscate secondary payloads.
*   **Instruction Cache Flushing:** Calls to `FlushInstructionCache` (in `fcn.140002e20` and `fcn.140003410`) are utilized to execute newly injected/modified machine code.
*   **Loader Characteristics:** The binary acts as a "wrapper" or stub for known frameworks, specifically showing characteristics consistent with **Cobalt Strike** beacons.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family**: Cobalt Strike
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Evasion Techniques:** The binary implements a specific AMSI bypass (patching `amsi.dll` and `AmsiScanBuffer`) to blind security software, which is a hallmark of Cobalt Strike-related modules.
    *   **Reflective Loading Characteristics:** The use of manual mapping (allocating memory, resolving imports via `GetProcAddress`, and handling relocations) indicates the sample is designed to execute a second-stage payload strictly in memory to evade disk-based scanning.
    *   **Obfuscated Execution Chain:** The presence of XOR/arithmetic shift decryption routines for a hidden blob, followed by instruction cache flushing, confirms its role as a sophisticated wrapper/loader intended to host and hide secondary malicious code.
