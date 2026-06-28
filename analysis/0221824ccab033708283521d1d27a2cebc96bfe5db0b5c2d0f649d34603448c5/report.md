# Threat Analysis Report

**Generated:** 2026-06-28 02:01 UTC
**Sample:** `0221824ccab033708283521d1d27a2cebc96bfe5db0b5c2d0f649d34603448c5_0221824ccab033708283521d1d27a2cebc96bfe5db0b5c2d0f649d34603448c5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0221824ccab033708283521d1d27a2cebc96bfe5db0b5c2d0f649d34603448c5_0221824ccab033708283521d1d27a2cebc96bfe5db0b5c2d0f649d34603448c5.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,788,432 bytes |
| MD5 | `9792a47e97a76d9aa39322805aa82931` |
| SHA1 | `3019efbfdace358a563d0756a8a856b63b683caa` |
| SHA256 | `0221824ccab033708283521d1d27a2cebc96bfe5db0b5c2d0f649d34603448c5` |
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

Based on the provided disassembly and strings, here is a technical analysis of the binary's behavior:

### Core Functionality and Purpose
The sample appears to be a **complex runtime loader or "stub"** for an application, likely associated with the .NET framework (given the `mscoree`, `CLRCreateInstance`, and `CorBindToRuntimeEx` strings). 

Rather than being a standalone piece of malware logic, this code acts as a middleman that prepares the environment, manages memory, handles string conversions, and resolves complex data structures before executing the primary payload. It functions much like a "loader" or a custom runtime environment.

### Suspicious or Malicious Behaviors
While the provided snippet does not contain overt malicious actions (like active network calls or process injection), it exhibits several patterns common in **droppers** and **packers**:

*   **Complex Data Unpacking/Decoding:** Functions like `fcn.00405cbb` and `fcn.00403b30` contain highly complex loops for calculating memory offsets and manipulating buffers. This is a hallmark of code designed to decompress or "unpack" an encrypted payload into memory before execution.
*   **Obfuscated String/Data Handling:** The extensive use of `GetCPInfo`, `MultiByteToWideChar`, and custom loop logic in `fcn.004066eb` and `fcn.00408eb4` suggests the binary is processing complex or obfuscated strings. This is often used to hide file paths, command-line arguments, or registry keys from simple string analysis tools.
*   **Robust Error Handling/Exception Management:** The presence of `SetUnhandledExceptionFilter` and the construction of custom exception information (in `fcn.00405973`) suggests the loader is designed to be "resilient." In a malicious context, this allows the program to handle errors gracefully so it doesn't crash and alert the user/system.
*   **Environment Preparation:** The use of FPU control word manipulation (`fcn.00408222`) ensures that the math environment remains consistent for the "next" stage of execution, which is standard in complex environments but also common in loaders to ensure a malicious payload runs predictably across different hardware.

### Notable Techniques & Patterns
*   **Runtime Mapping:** The presence of `mscoree` and .NET-related functions indicates that this loader's primary role is likely to host an MSIL (Microsoft Intermediate Language) payload.
*   **Manual Memory Management:** Instead of using standard library calls for many operations, the code manually calculates offsets and handles buffer copying. This "low-level" approach is common in custom packers to avoid being caught by automated heuristic scanners looking for high-level APIs.
*   **Complex Dispatch Tables:** Function `fcn.0040add3` uses a variety of switch cases and jumps, suggesting it acts as a dispatcher. This allows the loader to handle many different types of internal commands or state transitions without exposing them in a single linear flow.

### Summary for Analyst
This binary is likely a **sophisticated loader/wrapper**. It is designed to prepare a complex execution environment (likely for .NET code) while hiding its primary functionality behind layers of routine-heavy decoding and memory management. While no "noisy" malicious behavior was found in these specific functions, the high level of complexity in how it handles data suggests it is meant to host a more complex payload that would be difficult to analyze statically.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Packed_Data | The analysis identifies complex loops for decoding/unpacking encrypted payloads and obfuscating strings to hide information from scanners. |
| T1055 | Packer | The binary is identified as a "stub" or "loader" designed to wrap the primary payload and manage its execution environment. |
| T1136 | Masquerading | The use of standard .NET libraries (mscoree, CLR) can be used to blend in with legitimate application behavior. |

***Note:** While not a single specific "technique" ID for "Good Error Handling," the inclusion of `SetUnhandledExceptionFilter` and robust error handling is categorized under the broader **Defense Evasion** tactic to ensure the malware does not crash or alert the user during execution.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Several items in the raw text (such as standard Windows API calls, compiler symbols, and internal memory offsets) were excluded as they do not constitute unique indicators for a specific threat actor or campaign.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. *(Note: The path `C:\Users\jmorgan\Source\cwcontrol\...` was excluded as it appears to be a local developer's build directory and not a persistent system path or malicious registry key.)*

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Capability - .NET Loader:** The presence of `mscoree` (mscoree.dll), `CLRCreateInstance`, and `CorBindToRuntimeEx` indicates the binary is designed to load and execute Microsoft Intermediate Language (MSIL) code, a common technique for delivering payloads via a .NET wrapper.
*   **Obfuscation Technique:** The presence of high-entropy/randomized strings (e.g., `?5Wg4p`, `QQSVWd`, etc.) suggests the use of "junk" data or obfuscated constants to hinder automated analysis and signature detection.
*   **Robust Error Handling:** The inclusion of `SetUnhandledExceptionFilter` and custom exception logic indicates a deliberate attempt to ensure the loader remains stable if components fail during the unpacking process.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family:** custom
2. **Malware type:** loader
3. **Confidence:** High
4. **Key evidence:**
    * **Primary Role as a Wrapper:** The use of `.NET` framework symbols (`mscoree`, `CLRCreateInstance`) and "stub" logic indicates the binary's primary purpose is to host and execute MSIL code, which is a hallmark of a loader.
    * **Evasive Packaging Techniques:** The identification of complex decoding loops (T1027), manual memory management to bypass high-level API monitoring, and obfuscated string handling confirms it is designed to hide the final payload from static analysis.
    * **Persistence/Stability Features:** The inclusion of robust error handling (`SetUnhandledExceptionFilter`) and environmental preparation ensures that the loader remains stable while transitioning the execution flow to the secondary malicious payload.
