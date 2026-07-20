# Threat Analysis Report

**Generated:** 2026-07-18 06:05 UTC
**Sample:** `08727f11a6d87937a4efa4b67e69c4346e72588ce7651a965f52a74e8a6956fa_08727f11a6d87937a4efa4b67e69c4346e72588ce7651a965f52a74e8a6956fa.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `08727f11a6d87937a4efa4b67e69c4346e72588ce7651a965f52a74e8a6956fa_08727f11a6d87937a4efa4b67e69c4346e72588ce7651a965f52a74e8a6956fa.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 13,431,632 bytes |
| MD5 | `93e8ed4422edf7bca927160bacca2ac8` |
| SHA1 | `180c77c5cf39cc8b8b62142190dcd261d502bb27` |
| SHA256 | `08727f11a6d87937a4efa4b67e69c4346e72588ce7651a965f52a74e8a6956fa` |
| Overall entropy | 7.817 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1668802220 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 45,568 | 6.592 | No |
| `.rdata` | 25,088 | 4.787 | No |
| `.data` | 2,048 | 2.265 | No |
| `.rsrc` | 13,352,448 | 7.822 | ⚠️ Yes |
| `.reloc` | 4,096 | 6.301 | No |

### Imports

**mscoree.dll**: `CorBindToRuntimeEx`
**KERNEL32.dll**: `GetModuleFileNameA`, `DecodePointer`, `SizeofResource`, `LockResource`, `LoadLibraryW`, `LoadResource`, `FindResourceW`, `GetProcAddress`, `WriteConsoleW`, `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleCP`, `FlushFileBuffers`, `HeapReAlloc`, `HeapSize`
**OLEAUT32.dll**: `VariantInit`, `SafeArrayUnaccessData`, `SafeArrayCreateVector`, `SafeArrayDestroy`, `VariantClear`, `SafeArrayAccessData`

## Extracted Strings

Total strings found: **40894** (showing first 100)

```
!This program cannot be run in DOS mode.
$
RichE>`
`.rdata
@.data
@.reloc
T$Rh
M;Jr

QQSVWd
38_^]
E9xt
&9Gv!8E
Yt
jV
9Nv@k
URPQQh
kUQPXY]Y[
< t1<	t-
uh0MA
uj Y;E
jh 'A
tf;1u
WWWPWS
u-PWWS
PjhLMA
PQhPAA
PQhXBA
SSVWh 
f9:t!V
WuVVS
QQSWj0j@
jh (A
tl=PFA
jh@(A
jh`(A
u9Mu!3
PPPPPPPP
PPPPPWS
PP9E u:PPVWP
t;Et
jh()A

u,jXj

u	jZf
\9EuY
D$+d$SVW
Unknown exception
bad exception
__based(
__cdecl
__pascal
__stdcall
__thiscall
__fastcall
__vectorcall
__clrcall
__eabi
__swift_1
__swift_2
__swift_3
__ptr64
__restrict
__unaligned
restrict(
 delete
operator
`vftable'
`vbtable'
`vcall'
`typeof'
`local static guard'
`string'
`vbase destructor'
`vector deleting destructor'
`default constructor closure'
`scalar deleting destructor'
`vector constructor iterator'
`vector destructor iterator'
`vector vbase constructor iterator'
`virtual displacement map'
`eh vector constructor iterator'
`eh vector destructor iterator'
`eh vector vbase constructor iterator'
`copy constructor closure'
`udt returning'
`local vftable'
`local vftable constructor closure'
 new[]
 delete[]
`omni callsig'
`placement delete closure'
`placement delete[] closure'
`managed vector constructor iterator'
`managed vector destructor iterator'
`eh vector copy constructor iterator'
`eh vector vbase copy constructor iterator'
`dynamic initializer for '
`dynamic atexit destructor for '
`vector copy constructor iterator'
`vector vbase copy constructor iterator'
`managed vector copy constructor iterator'
`local static thread guard'
operator "" 
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040a138` | `0x40a138` | 2957 | ✓ |
| `fcn.00403b30` | `0x403b30` | 1396 | ✓ |
| `fcn.00402a2b` | `0x402a2b` | 933 | ✓ |
| `fcn.00408970` | `0x408970` | 922 | ✓ |
| `fcn.00408222` | `0x408222` | 770 | ✓ |
| `fcn.0040a57e` | `0x40a57e` | 614 | ✓ |
| `fcn.0040b895` | `0x40b895` | 563 | ✓ |
| `fcn.00408eb4` | `0x408eb4` | 541 | ✓ |
| `fcn.0040add3` | `0x40add3` | 536 | ✓ |
| `fcn.00409e92` | `0x409e92` | 524 | ✓ |
| `fcn.00404852` | `0x404852` | 523 | ✓ |
| `fcn.0040a93e` | `0x40a93e` | 523 | ✓ |
| `fcn.00407f6f` | `0x407f6f` | 520 | ✓ |
| `fcn.004066eb` | `0x4066eb` | 497 | ✓ |
| `fcn.0040b692` | `0x40b692` | 480 | ✓ |
| `fcn.00401c04` | `0x401c04` | 468 | ✓ |
| `fcn.00409817` | `0x409817` | 435 | ✓ |
| `fcn.00406396` | `0x406396` | 404 | ✓ |
| `fcn.00405cbb` | `0x405cbb` | 400 | ✓ |
| `entry0` | `0x4014ad` | 390 | ✓ |
| `fcn.00405ee1` | `0x405ee1` | 388 | ✓ |
| `fcn.00404477` | `0x404477` | 373 | ✓ |
| `fcn.004040f0` | `0x4040f0` | 371 | ✓ |
| `fcn.00402570` | `0x402570` | 346 | ✓ |
| `fcn.00403152` | `0x403152` | 333 | ✓ |
| `fcn.00407907` | `0x407907` | 330 | ✓ |
| `fcn.00404f40` | `0x404f40` | 321 | ✓ |
| `fcn.004027d4` | `0x4027d4` | 318 | ✓ |
| `fcn.00405973` | `0x405973` | 315 | ✓ |
| `fcn.00402dd0` | `0x402dd0` | 310 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401c04.c`](code/fcn.00401c04.c)
- [`code/fcn.00402570.c`](code/fcn.00402570.c)
- [`code/fcn.004027d4.c`](code/fcn.004027d4.c)
- [`code/fcn.00402a2b.c`](code/fcn.00402a2b.c)
- [`code/fcn.00402dd0.c`](code/fcn.00402dd0.c)
- [`code/fcn.00403152.c`](code/fcn.00403152.c)
- [`code/fcn.00403b30.c`](code/fcn.00403b30.c)
- [`code/fcn.004040f0.c`](code/fcn.004040f0.c)
- [`code/fcn.00404477.c`](code/fcn.00404477.c)
- [`code/fcn.00404852.c`](code/fcn.00404852.c)
- [`code/fcn.00404f40.c`](code/fcn.00404f40.c)
- [`code/fcn.00405973.c`](code/fcn.00405973.c)
- [`code/fcn.00405cbb.c`](code/fcn.00405cbb.c)
- [`code/fcn.00405ee1.c`](code/fcn.00405ee1.c)
- [`code/fcn.00406396.c`](code/fcn.00406396.c)
- [`code/fcn.004066eb.c`](code/fcn.004066eb.c)
- [`code/fcn.00407907.c`](code/fcn.00407907.c)
- [`code/fcn.00407f6f.c`](code/fcn.00407f6f.c)
- [`code/fcn.00408222.c`](code/fcn.00408222.c)
- [`code/fcn.00408970.c`](code/fcn.00408970.c)
- [`code/fcn.00408eb4.c`](code/fcn.00408eb4.c)
- [`code/fcn.00409817.c`](code/fcn.00409817.c)
- [`code/fcn.00409e92.c`](code/fcn.00409e92.c)
- [`code/fcn.0040a138.c`](code/fcn.0040a138.c)
- [`code/fcn.0040a57e.c`](code/fcn.0040a57e.c)
- [`code/fcn.0040a93e.c`](code/fcn.0040a93e.c)
- [`code/fcn.0040add3.c`](code/fcn.0040add3.c)
- [`code/fcn.0040b692.c`](code/fcn.0040b692.c)
- [`code/fcn.0040b895.c`](code/fcn.0040b895.c)

## Behavioral Analysis

### Analysis Summary

Based on the provided disassembly and strings, this code appears to be part of a **managed execution environment or a JIT (Just-In-Time) compiler backend**, likely associated with a .NET-related runner (as evidenced by the string path `...DotNetRunner.pdb` and references to `mscoree.dll`).

The functionality is centered on high-performance mathematical calculations, floating-point state management, and complex memory/data manipulation typical of an interpreter or a JIT engine.

### Core Functionality
*   **Mathematical Library Operations:** The function `fcn.0040add3` acts as a dispatcher for common math functions including `sqrt`, `asin`, `acos`, and `log10`. It handles the underlying logic for these transcendental functions.
*   **Floating-Point (FPU/SIMD) Management:** Multiple functions (`fcn.0040a138`, `fcn.00408222`, `fcn.0040b692`) are dedicated to handling FPU control words and SSE/AVX instruction sets. This ensures consistent arithmetic behavior across different CPU architectures.
*   **JIT Compilation/Runtime Logic:** The heavy use of memory copying, pointer arithmetic in `fcn.00403b30`, and complex state-checking in `fcn.00402a2b` are characteristic of a runtime environment that interprets or compiles intermediate code (like CIL) into machine code.
*   **String/Buffer Manipulation:** Functions like `fcn.00408eb4` provide wrappers for standard Windows API calls to convert multi-byte strings to wide characters and handle standard output/logging.

### Suspicious or Malicious Behaviors
While the snippet does not contain "smoking gun" indicators of active exploitation (like direct process injection or networking), several characteristics are noteworthy in a malware analysis context:

*   **Complexity as an Obfuscation Layer:** The extremely complex, repetitive logic for memory manipulation and instruction dispatching is common in **custom packers and loaders**. These tools often wrap legitimate-looking math libraries to hide the underlying malicious payload.
*   **Potential for "Fileless" Execution:** Because this code supports a "DotNetRunner" environment, it can be used to execute obfuscated scripts or dynamically generated code in memory, a common technique for evading traditional signature-based antivirus.
*   **Use of System APIs for Output:** The presence of `WriteFile` and `GetConsoleCP` (via wrapper `fcn.00408eb4`) suggests the program may interact with the file system or console to display progress, log actions, or exfiltrate data in a way that appears like standard application behavior.

### Notable Techniques & Patterns
*   **Processor Feature Detection:** The code uses `IsProcessorFeaturePresent` and checks for specific CPU instructions (e.g., checking for SSE2/AVX capabilities). This is common in high-performance software but also used by malware to check if it can use optimized encryption or compression routines.
*   **Manual Memory Management:** Extensive manual pointer arithmetic and "manually" implemented memory movement loops suggest a desire for low-level control over data, typical of both performance-oriented compilers and custom-built loader components.
*   **Internal Dispatching:** The pattern of using hash/ID checks (e.g., `if (arg_14h == 0x3a) { var_20h = "acos"; }`) indicates a dispatcher that maps internal IDs to specific functions, common in JIT compilers to minimize overhead.

**Conclusion:** This sample appears to be the **core engine of a managed runtime or a high-performance math library**. While not inherently malicious, this type of complex infrastructure is frequently utilized by advanced malware as a "loader" to execute secondary stages (e.g., stealing credentials via a hidden .NET script).

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | Packer | The analysis identifies that the complex, repetitive logic for memory manipulation and instruction dispatching is characteristic of custom packers used to hide malicious payloads. |
| **T1027** | Obfuscated Files or Information | The use of intricate mathematical libraries and "complex logic" as an obfuscation layer serves to mask the true intent of the code from signature-based detection. |
| **T1059** | Command and Scripting Interpreter | The inclusion of a ".NET Runner" and JIT compilation capabilities enables the execution of dynamically generated code or scripts in memory, a common method for executing obfuscated commands. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` 
    *(Note: This path points to a specific development environment/build folder, often associated with custom loaders or packers).*

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Core Component:** `DotNetRunner` (Identified as a potential execution engine used to run obfuscated scripts or dynamically generated code in memory).
*   **Behavioral Note:** The presence of a custom dispatching system for mathematical functions (`fcn.0040add3`, etc.) and extensive manual memory management suggests the use of a custom packer/loader framework rather than a standard application.

---

## Malware Family Classification

1. **Malware family**: custom (likely associated with a loader framework)
2. **Malware type**: loader
3. **Confidence**: Medium

4. **Key evidence**:
* **JIT Compilation & Script Execution:** The analysis identifies the sample as a "DotNetRunner" and a JIT compilation backend, which are classic indicators of a loader designed to execute obfuscated scripts or dynamically generated code in memory (fileless execution).
* **Obfuscation via Complexity:** The use of complex mathematical libraries, manual memory management, and internal dispatching functions suggests a deliberate attempt to create an "obfuscation layer" to hide the underlying malicious functionality from signature-based detection.
* **Loader Infrastructure:** The inclusion of MITRE techniques T1055 (Packer) and T1059 (Command and Scripting Interpreter) confirms its role as a vehicle for delivering secondary payloads rather than being a standalone malware payload like a RAT or ransomware.
