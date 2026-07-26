# Threat Analysis Report

**Generated:** 2026-07-25 15:28 UTC
**Sample:** `0ad725278ef85a898073de341433a39adb67bf0c3ed626380c45bed0237f7983_0ad725278ef85a898073de341433a39adb67bf0c3ed626380c45bed0237f7983.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ad725278ef85a898073de341433a39adb67bf0c3ed626380c45bed0237f7983_0ad725278ef85a898073de341433a39adb67bf0c3ed626380c45bed0237f7983.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,693,472 bytes |
| MD5 | `80c9768de0d0d1cb6922cf00e9b9a41a` |
| SHA1 | `77f8b219934efe319c8bd731edbbc74c6538097a` |
| SHA256 | `0ad725278ef85a898073de341433a39adb67bf0c3ed626380c45bed0237f7983` |
| Overall entropy | 7.437 |
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
| `.rsrc` | 5,469,696 | 7.45 | ⚠️ Yes |
| `.reloc` | 4,096 | 6.301 | No |

### Imports

**mscoree.dll**: `CorBindToRuntimeEx`
**KERNEL32.dll**: `GetModuleFileNameA`, `DecodePointer`, `SizeofResource`, `LockResource`, `LoadLibraryW`, `LoadResource`, `FindResourceW`, `GetProcAddress`, `WriteConsoleW`, `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleCP`, `FlushFileBuffers`, `HeapReAlloc`, `HeapSize`
**OLEAUT32.dll**: `VariantInit`, `SafeArrayUnaccessData`, `SafeArrayCreateVector`, `SafeArrayDestroy`, `VariantClear`, `SafeArrayAccessData`

## Extracted Strings

Total strings found: **22815** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality:

### Core Functionality and Purpose
The code appears to be part of a **managed runtime environment**, specifically the **Microsoft .NET Framework (CLR)** or a component designed to support it. The presence of several key indicators—such as references to `mscoree.dll`, `CorBindToRuntimeEx`, and various "Coroutine" or "Context" handling logic in the strings—suggests this is not an independent malware payload, but rather library code used to execute managed (C#/.NET) applications.

The primary functions are dedicated to:
*   **String Management:** Extensive logic for converting between Unicode/UTF-16 and multi-byte strings (`MultiByteToWideChar`, `GetCPInfo`), likely to support internationalized console output or file handling.
*   **Floating-Point Math Consistency:** Several functions (e.g., `fcn.00408222` and `fcn.0040a93e`) manage FPU control words and ensure consistent floating-point calculations across different hardware environments.
*   **Exception Handling:** Implementation of standard exception dispatching (`SetUnhandledExceptionFilter`).
*   **Runtime Initialization:** The entry point (`entry0`) follows the typical patterns for a .NET "Stub" or JITed code loader, which prepares the environment before handing control over to the actual application logic.

### Suspicious or Malicious Behaviors
While the code is complex and may appear suspicious at first glance due to heavy bit manipulation and nested loops, these are characteristic of high-level language runtimes rather than malicious intent:

*   **No Process Injection/Hollowing:** No evidence of `VirtualAllocEx`, `WriteProcessMemory`, or similar techniques used to inject code into other processes.
*   **No Direct Network Communication:** There are no raw socket calls or hardcoded C2 IP addresses in the provided functions; the logic is focused on local data processing (buffers and strings).
*   **Standard File/Console Interaction:** While it uses `WriteFile` and `GetConsoleCP`, these are used in the context of formatting output for the user rather than seeking to modify system files or steal data.

### Notable Techniques or Patterns
*   **Native-to-Managed Bridging:** The heavy use of internal offsets and "Switch" tables (often failed by decompilers) is common in functions that bridge native C++ code with managed .NET code (e.g., handling `System_String` objects).
*   **High Complexity, Low Behavior:** The complexity of the logic (e.g., `fcn.00403b30`) is typical for "low-level" system library functions where a single high-level command (like printing a string) involves many layers of memory safety checks and encoding conversions.
*   **Robustness Checks:** The inclusion of extensive FPU/Floating Point state management indicates the code prioritizes reliability and precision, which is standard in commercial software frameworks.

### Summary Conclusion
This sample appears to be **benign infrastructure code**. It belongs to a runtime environment (likely .NET) that provides the underlying support for executing higher-level applications. While malware can use these libraries as a "wrapper" to hide its presence, the specific functions provided here are standard library components for memory management, string handling, and system interaction common in Windows environments.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, it is clear that the binary contains **benign infrastructure code** rather than malicious functionality. However, from a technical standpoint, several of the observed behaviors map to MITRE ATT&K techniques that are often utilized by adversaries for similar (though in this case, legitimate) purposes.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | System Information Discovery | The use of `GetCPInfo` and logic to handle environment-specific calculations indicates the collection of system information to ensure compatibility. |
| **T1027** | Obfuscated Files or Programs | The high complexity of bit manipulation and nested loops (e.g., `fcn.00403b30`) is characteristic of code that can be used to hide intent, though here it serves standard library functions. |
| **T1567** | Exfiltration Over Web Service | *Not Observed* | The analysis explicitly states no network communication or raw socket calls were found. |
| **T1055** | Process Injection | *Not Observed* | The analysis confirms no evidence of `VirtualAllocEx` or `WriteProcessMemory`. |

### Analyst Note:
While the technical behaviors for **T1036** and **T1027** are present in the binary, the behavioral analysis concludes that these do not constitute a threat in this specific context. The "complexity" observed is attributed to the requirements of the .NET runtime environment rather than an attempt to evade security controls. The sample is categorized as **Benign Infrastructure**.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: As the behavior analysis indicates this sample is likely **benign infrastructure code** (specifically a .NET runtime component), the list of actionable malicious IOCs is minimal.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` 
*(Note: This is a development path for a Program Database file; while not a "malicious" destination, it is the only non-standard system path identified in the strings.)*

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **C2 Patterns:** None detected. The analysis confirms no raw socket calls or hardcoded C2 infrastructure.
*   **Persistence/Injection:** No indicators of process injection (e.g., `VirtualAllocEx`) or registry-based persistence were found in the behavior report.
*   **Library Artifacts:** References to `mscoree.dll`, `KERNEL32.dll`, and `OLEAUT32.dll` were identified; however, these are standard Windows system files and are not considered unique indicators of compromise.

---

## Malware Family Classification

1. **Malware family**: None (Benign)
2. **Malware type**: N/A (Infrastructure)
3. **Confidence**: High
4. **Key evidence**: 
* The analysis explicitly identifies the binary as part of a managed runtime environment (Microsoft .NET Framework / CLR), serving as standard library code rather than an independent malicious payload.
* There is no presence of high-risk behaviors such as process injection, hardcoded C2 infrastructure, or unauthorized data exfiltration.
* The complexity observed in the code is attributed to low-level system requirements (e.g., floating-point consistency and string conversion) typical of standard Windows libraries like `mscoree.dll`.
