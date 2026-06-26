# Threat Analysis Report

**Generated:** 2026-06-26 16:18 UTC
**Sample:** `011fdaa3a7d7f7badc6088eda2a21fa808bcefe2c0cd24b21a89271102c5be60_011fdaa3a7d7f7badc6088eda2a21fa808bcefe2c0cd24b21a89271102c5be60.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `011fdaa3a7d7f7badc6088eda2a21fa808bcefe2c0cd24b21a89271102c5be60_011fdaa3a7d7f7badc6088eda2a21fa808bcefe2c0cd24b21a89271102c5be60.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,788,432 bytes |
| MD5 | `7b3f4d34b8d3518c092d81506df05103` |
| SHA1 | `264e801035f64163ffa7cf05086ce4c7d1396956` |
| SHA256 | `011fdaa3a7d7f7badc6088eda2a21fa808bcefe2c0cd24b21a89271102c5be60` |
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

Based on the disassembly provided, here is a professional analysis of the binary's functionality.

### Core Functionality and Purpose
The binary appears to be a **sophisticated execution wrapper or "loader"** for a managed runtime environment (likely .NET/CLR based, as evidenced by the "NetRunner" strings and `mscoree` related logic). 

Rather than being a simple application, this code acts as an intermediate layer. It performs extensive system checks, prepares memory environments, handles Floating Point Unit (FPU) state consistency, manages character sets (Code Pages), and provides a mechanism for executing bytecode or "managed" instructions within a native container. The presence of specialized JIT-related logic suggests it is designed to host and execute complex code from a secondary source.

### Suspicious and Malicious Behavs
*   **Anti-Analysis & Anti-Debugging:** 
    *   The function `fcn.00405973` explicitly calls **`IsDebuggerPresent`**.
    *   It sets an **`UnhandledExceptionFilter`**, which is often used by malware to intercept and suppress exceptions that would normally alert a user or analyst when the code performs suspicious actions (like memory injection or brute-forcing).
*   **Environment Probing:**
    *   The function `fcn.00401c04` uses **`IsProcessorFeaturePresent`** and various **CPUID** checks to probe for specific hardware capabilities (SSE, AVX instructions, etc.). While common in game engines or high-performance compilers, this is also a hallmark of "droppers" or "stagers" checking if the environment supports the specific encryption or packing techniques intended for the primary payload.
*   **Complex Memory Manipulation:** 
    *   Several functions (e.g., `fcn.00403b30` and `fcn.00407f6f`) contain highly complex, nested loop structures to move or manipulate memory buffers using large offsets. This complexity is common in **obfuscated loaders** designed to hide the preparation of a payload's execution space.
*   **File System Interaction:** 
    *   The code includes logic for reading and writing files (`fcn.00409e92` and `fcn.00408eb4`). It specifically handles **MultiByteToWideChar** conversions, suggesting it can read/write data in various encodings, potentially facilitating the extraction of an embedded payload or communication with a local file system to stage components.

### Notable Techniques and Patterns
*   **JIT-Engine Characteristics:** The code heavily resembles a custom JIT (Just-In-Time) compiler infrastructure. It manages FPU control words (`fcn.00408222`) and handles complex memory mapping for different instruction types. This is typical of "Loader" malware that uses a legitimate or modified .NET/Mono runtime to hide its true intent from signature-based scanners.
*   **Flow Control via Exceptions:** The use of `RaiseException` (found in the logic leading up to `fcn.00408950`) combined with manual assembly "swi(3)" signals suggests that the loader uses system exceptions as a way to pass data or control flow between the native host and the managed guest (a common technique in hybrid-code execution).
*   **High Obfuscation/Complexity:** The presence of many "Switch" statements based on hardcoded hex values (e.g., `fcn.0040add3`) and heavy use of offsets indicates a **tampered or heavily obfuscated instruction set**. This is often used to make static analysis via standard tools difficult, as the core logic is hidden behind a layer of abstraction.
*   **Potential for "Living off the Land":** Because it links against `mscoree.dll` and implements high-level runtime features (like handling Unicode/Wide characters), the malware may attempt to hide its behavior by mimicking legitimate system processes or utilizing common library functions to mask its network or file manipulation routines.

### Summary for Incident Response
This binary is likely a **sophisticated loader component**. While it does not show direct "fire-and-forget" malicious actions (like an immediate call to a known C2 IP), it builds a complex, protected environment designed to execute more advanced code. The inclusion of anti-debugging, CPU feature checks, and heavy obfuscation points toward its use as a **stage-two loader** or a **custom execution engine** for malware that aims to evade automated detection systems by residing within a "safe" runtime environment.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Debugger Detection | The binary explicitly calls `IsDebuggerPresent` to detect and potentially evade analysis by an analyst's debugger. |
| T1497 | Virtualization/Sandbox Detection | The use of `IsProcessorFeaturePresent` and `CPUID` checks is a common method for malware to determine if it is running in a virtualized or sandbox environment. |
| T1055 | Process Injection | The "loader" functionality, characterized by complex memory manipulation and the creation of an execution space for secondary payloads, indicates techniques used to inject or host malicious code. |
| T1106 | Native API | The binary utilizes low-level system interactions (like `RaiseException` and manual assembly signals) to manage control flow outside of standard high-level language constraints. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type:

### **IP addresses / URLs / Domains**
*None identified.*

### **File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` 
    *(Note: While a .pdb file is typically for debugging, this specific path provides intelligence regarding the developer's internal directory structure and naming conventions.)*

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None provided in the source text.*

### **Other artifacts** (TTPs & Behavioral Indicators)
*   **Anti-Debugging:** The binary calls `IsDebuggerPresent` to detect analysis environments.
*   **Environment Probing:** Use of `IsProcessorFeaturePresent` and `CPUID` checks to verify hardware capabilities, common in malware used to fingerprint systems before executing primary payloads.
*   **Exception Handling for Flow Control:** Use of `RaiseException` and `swi(3)` signals to manage control flow between a native host and a managed ( .NET) guest.
*   **Runtime Wrapping/Masking:** Utilization of `mscoree.dll` and high-level .NET features to mask malicious activity within a legitimate runtime environment.
*   **Obfuscated Memory Manipulation:** Use of complex, nested loops for memory buffer manipulation to hide the preparation of payload execution spaces.
*   **Data Transformation:** Use of `MultiByteToWideChar` during file system interactions, potentially used for decoding or staging components in various character sets.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**: 
*   **Sophisticated Execution Wrapper:** The binary functions as a "loader" or "stager" designed to host and execute managed code (via `mscoree.dll`) in a protected environment, effectively masking the final payload's activity from security software.
*   **Anti-Analysis & Evasion:** It implements multiple layers of defense, including explicit debugger checks (`IsDebuggerPresent`), environmental fingerprinting (`CPUID` and `IsProcessorFeaturePresent`), and complex memory manipulation to hide malicious logic.
*   **Advanced Execution Techniques:** The use of JIT-like functionality, exception-based flow control (`RaiseException`), and heavily obfuscated switch statements indicates a professional construction aimed at complicating reverse engineering and dynamic analysis.
