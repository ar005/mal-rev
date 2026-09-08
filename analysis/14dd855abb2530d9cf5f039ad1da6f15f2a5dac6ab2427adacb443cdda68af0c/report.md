# Threat Analysis Report

**Generated:** 2026-09-06 09:45 UTC
**Sample:** `14dd855abb2530d9cf5f039ad1da6f15f2a5dac6ab2427adacb443cdda68af0c_14dd855abb2530d9cf5f039ad1da6f15f2a5dac6ab2427adacb443cdda68af0c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14dd855abb2530d9cf5f039ad1da6f15f2a5dac6ab2427adacb443cdda68af0c_14dd855abb2530d9cf5f039ad1da6f15f2a5dac6ab2427adacb443cdda68af0c.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,788,432 bytes |
| MD5 | `39ec34bb5f40716e47c8201703bb2294` |
| SHA1 | `314c2ef3090741f0ee94eb33103da9aef95d22eb` |
| SHA256 | `14dd855abb2530d9cf5f039ad1da6f15f2a5dac6ab2427adacb443cdda68af0c` |
| Overall entropy | 7.445 |
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

Total strings found: **22923** (showing first 100)

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

Based on the provided disassembly and strings, here is a technical analysis of the binary's functionality:

### Core Functionality and Purpose
The sample appears to be a **loader or a custom runtime wrapper** designed to execute .NET-based code. The presence of several internal .NET infrastructure strings (e.g., `mscoree.dll`, `CorBindToRuntimeEx`, `CLRCreateInstance`) indicates that the binary interacts directly with the Common Language Runtime (CLR). 

The code includes a significant amount of low-level "boilerplate" logic typically found in managed-code runners, such as:
*   **Memory Management:** Large blocks of code for managing internal buffers and memory copying.
*   **Floating Point Processing:** Extensive logic to handle FPU control words and complex math operations (e.g., `fcn.00408222`, `fcn.0040b692`).
*   **String Manipulation:** Robust handling of character sets, conversion between MultiByte/Wide characters, and newline normalization.

### Suspicious or Malicious Behaviors
While much of the code resembles standard library functionality for a .NET runner, several specific sections are highly indicative of malicious intent or anti-analysis techniques:

*   **Anti-Debugging / Anti-Analysis:**
    *   The function `fcn.00405973` explicitly calls **`IsDebuggerPresent()`**. This is a classic technique used by malware to detect if it is being analyzed in a debugger and change its behavior (e.g., "gracefully" exiting or executing benign code) if one is detected.
    *   The use of **`SetUnhandledExceptionFilter`** suggests the binary may be attempting to intercept crashes or exceptions, which can be used to hide its tracks or bypass certain monitoring tools.

*   **Environment/Hardware Fingerprinting:**
    *   Function `fcn.00401c04` uses **CPUID instructions** and checks for specific processor features (e.g., hardware support for various instruction sets). 
    *   In a malware context, this is often used to determine if the code is running on a physical machine or in a virtualized/sandboxed environment before "unpacking" more malicious behavior.

*   **Potential Data Exfiltration / File Manipulation:**
    *   `fcn.00409817` interacts with **`WriteFile`** and handles various string encodings. While this can be used for legitimate logging, in a suspicious sample, it may indicate the ability to write configuration files or exfiltrated data to disk/buffers under different encodings to evade simple signature-based detection.

### Notable Techniques & Patterns
*   **Complex String Processing:** The code contains very extensive logic for handling various locales and character sets (seen in `fcn.00406396`). This suggests the binary is designed to handle complex data input, possibly to obfuscate internal commands or strings.
*   **Just-In-Time (JIT) Preparation:** The heavy involvement with .NET runtime calls (`CorBindToRuntimeEx`) and the "DotNetRunner" path in the symbols suggest that this code acts as a **loader**. It likely loads a malicious `.dll` or script into memory and executes it via the .NET framework to hide the actual payload from simple static analysis.
*   **Switch-Table Logic & Large Jump Tables:** The presence of complex jump tables (e.g., `fcn.00403b30`) indicates a large amount of logic is being funneled through a single entry point, which can sometimes be used to complicate manual reverse engineering.

### Summary for Report
The sample is likely a **malicious loader** designed to host and execute .NET-based malware. It utilizes standard .NET runtime components but incorporates **anti-debugging techniques (IsDebuggerPresent)** and **hardware fingerprinting (CPUID checks)** to evade security researchers and automated analysis environments. The core "payload" is likely not in this binary itself, but is loaded into memory by the logic observed here.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Detection | The use of `IsDebuggerPresent()` and `CPUID` instructions is intended to identify if the sample is running in a debugger or a virtualized analysis environment. |
| **T1027** | Obfuscated Files or Information | The extensive string manipulation, multiple character encodings, and "loader" logic are designed to hide malicious indicators from signature-based detection systems. |
| **T1609** | Reference File Execution | The binary acts as a loader that pulls in and executes external .NET components (DLLs or scripts), abstracting the primary payload from initial analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` (Note: While a `.pdb` file is a debug symbol, this path reveals internal project naming and development structures).

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified in the provided strings)*

**Other artifacts**
*   **Loader Identification:** "DotNetRunner" (The binary identifies as a .NET loader used to execute managed code/payloads).
*   **Anti-Analysis Techniques:** 
    *   `IsDebuggerPresent` (Used for anti-debugging checks).
    *   `SetUnhandledExceptionFilter` (Used to intercept and mask exceptions).
    *   `CPUID` instructions (Utilized for hardware fingerprinting/VM detection).
*   **API Hooking/Interaction:** `CorBindToRuntimeEx`, `CLRCreateInstance`, `GetProcAddress`.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Loader Functionality:** The binary explicitly acts as a wrapper for .NET-based code, utilizing `mscoree.dll`, `CorBindToRuntimeEx`, and `CLRCreateInstance` to host managed payloads while shielding the primary malicious logic from static analysis.
*   **Anti-Analysis Techniques:** It incorporates multiple evasion tactics, including `IsDebuggerPresent()` calls and `CPUID` instruction checks (hardware fingerprinting) to detect if it is running in a virtualized environment or a debugger.
*   **Evasion Tactics:** The presence of complex jump tables, extensive string manipulation/encoding, and the use of `SetUnhandledExceptionFilter` indicate a deliberate attempt to complicate reverse engineering and evade automated detection systems.
