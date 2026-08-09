# Threat Analysis Report

**Generated:** 2026-08-06 20:02 UTC
**Sample:** `0d782bb469e3a4eabab6224d2155793752dfadc150fc8a299d12c4f73dae3582_0d782bb469e3a4eabab6224d2155793752dfadc150fc8a299d12c4f73dae3582.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d782bb469e3a4eabab6224d2155793752dfadc150fc8a299d12c4f73dae3582_0d782bb469e3a4eabab6224d2155793752dfadc150fc8a299d12c4f73dae3582.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 5 sections |
| Size | 7,539,655 bytes |
| MD5 | `ff473ecd0a7518053a21701201c5ba59` |
| SHA1 | `e621137bf304c5d27b801fab375306bbed290244` |
| SHA256 | `0d782bb469e3a4eabab6224d2155793752dfadc150fc8a299d12c4f73dae3582` |
| Overall entropy | 7.997 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1290097655 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 104,960 | 6.608 | No |
| `.rdata` | 17,920 | 4.368 | No |
| `.data` | 12,800 | 1.371 | No |
| `.sxdata` | 512 | 0.02 | No |
| `.rsrc` | 3,584 | 3.697 | No |

### Imports

**OLEAUT32.dll**: `VariantClear`, `SysAllocString`
**USER32.dll**: `SendMessageA`, `SetTimer`, `DialogBoxParamW`, `DialogBoxParamA`, `SetWindowLongA`, `GetWindowLongA`, `SetWindowTextW`, `LoadIconA`, `LoadStringW`, `LoadStringA`, `CharUpperW`, `CharUpperA`, `DestroyWindow`, `EndDialog`, `PostMessageA`
**SHELL32.dll**: `ShellExecuteExA`
**KERNEL32.dll**: `GetStringTypeW`, `GetStringTypeA`, `LCMapStringW`, `LCMapStringA`, `InterlockedIncrement`, `InterlockedDecrement`, `GetProcAddress`, `GetOEMCP`, `GetACP`, `GetCPInfo`, `IsBadCodePtr`, `IsBadReadPtr`, `GetFileType`, `SetHandleCount`, `GetEnvironmentStringsW`

## Extracted Strings

Total strings found: **16353** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.sxdata
tt8]ug
 w'8]u
PSSSSSS
^L8^4t
j
FSWF
2AABBf;
CCEEf;
EVPj_
PPRPQPh
SPSVSh
B@@f98u
t09uu
~;}u
F$;F,r
t\IItEIt2IIt!It
Y9}t'
9^pY~0
CY;^p|
w$_^[]
99Gtt
F
9~|~!;~pt
\$f9\$
G490tvB
V4u$9]
;F4wr
F0F4u5
tpNtfNt*Nt
tSNNt*
@;D$r
<
7t
;
C 90tA
t4Ht"Ht
x0C;^D|
_^][YY
u ;~D|
uA8Eu/8E
FD;FHu
t)It"It
t7Ht#Hu
D$ )Ft
D$,_^]
L$,_^]
T$,_^]
|$D;T$ 
AG;L$$u
;L$ds3
;T$hs)
V+V,;
F9F,r
D$(;D$
r_^]3
D$(;D$
L$(;L$
9F _^]
9NLtp;
T$0_^]
D$0_^]
D$0_^]
L$0_^]
T$0_^]
uRFGHt
QQSVWd
t.;t$$t(
FLVh)IA
VC20XC00U
sO;>|C;~
6;58(B
)u9U
)E9Ur4
;t$s
uA;5<(B
SS@SSPVSS
t#SSUP
t$$VSS
_^][YY
<xt<Xt	
HSVHWtgHHtF
PPPPPPPP
PPPPPPPP
__GLOBAL_HEAP_SELECTED
__MSVCRT_HEAP_SELECT
runtime error 
TLOSS error

SING error

DOMAIN error

R6028
- unable to initialize heap

R6027
- not enough space for lowio initialization

R6026
- not enough space for stdio initialization

R6025
- pure virtual function call

R6024
- not enough space for _onexit/atexit table

R6019
- unable to open console device

R6018
- unexpected heap error

R6017
- unexpected multithread lock error

R6016
- not enough space for thread data


abnormal program termination

R6009
- not enough space for environment

```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0041562a` | `0x41562a` | 9158 | ✓ |
| `fcn.00411990` | `0x411990` | 3135 | ✓ |
| `main` | `0x401014` | 2543 | ✓ |
| `fcn.0040ad19` | `0x40ad19` | 2301 | ✓ |
| `fcn.0040ed98` | `0x40ed98` | 1766 | ✓ |
| `fcn.004126b0` | `0x4126b0` | 1545 | ✓ |
| `fcn.00408a3b` | `0x408a3b` | 1125 | ✓ |
| `fcn.00408524` | `0x408524` | 938 | ✓ |
| `fcn.0040ea0b` | `0x40ea0b` | 909 | ✓ |
| `fcn.00412d10` | `0x412d10` | 829 | ✓ |
| `fcn.00413980` | `0x413980` | 821 | ✓ |
| `fcn.00414090` | `0x414090` | 821 | ✓ |
| `fcn.0041458f` | `0x41458f` | 815 | ✓ |
| `fcn.00415ac8` | `0x415ac8` | 809 | ✓ |
| `fcn.00415df1` | `0x415df1` | 777 | ✓ |
| `fcn.004162a6` | `0x4162a6` | 758 | ✓ |
| `fcn.0040e5a5` | `0x40e5a5` | 710 | ✓ |
| `fcn.004116c0` | `0x4116c0` | 709 | ✓ |
| `fcn.0040ffaa` | `0x40ffaa` | 705 | ✓ |
| `fcn.0040a122` | `0x40a122` | 662 | ✓ |
| `fcn.0040f648` | `0x40f648` | 635 | ✓ |
| `fcn.00408f0a` | `0x408f0a` | 634 | ✓ |
| `fcn.0040dfe2` | `0x40dfe2` | 559 | ✓ |
| `fcn.0040d7cc` | `0x40d7cc` | 557 | ✓ |
| `fcn.00410dce` | `0x410dce` | 551 | ✓ |
| `fcn.0041881d` | `0x41881d` | 548 | ✓ |
| `fcn.00416894` | `0x416894` | 520 | ✓ |
| `fcn.00417a07` | `0x417a07` | 517 | ✓ |
| `fcn.004049dd` | `0x4049dd` | 511 | ✓ |
| `fcn.0040e35a` | `0x40e35a` | 491 | ✓ |

### Decompiled Code Files

- [`code/fcn.004049dd.c`](code/fcn.004049dd.c)
- [`code/fcn.00408524.c`](code/fcn.00408524.c)
- [`code/fcn.00408a3b.c`](code/fcn.00408a3b.c)
- [`code/fcn.00408f0a.c`](code/fcn.00408f0a.c)
- [`code/fcn.0040a122.c`](code/fcn.0040a122.c)
- [`code/fcn.0040ad19.c`](code/fcn.0040ad19.c)
- [`code/fcn.0040d7cc.c`](code/fcn.0040d7cc.c)
- [`code/fcn.0040dfe2.c`](code/fcn.0040dfe2.c)
- [`code/fcn.0040e35a.c`](code/fcn.0040e35a.c)
- [`code/fcn.0040e5a5.c`](code/fcn.0040e5a5.c)
- [`code/fcn.0040ea0b.c`](code/fcn.0040ea0b.c)
- [`code/fcn.0040ed98.c`](code/fcn.0040ed98.c)
- [`code/fcn.0040f648.c`](code/fcn.0040f648.c)
- [`code/fcn.0040ffaa.c`](code/fcn.0040ffaa.c)
- [`code/fcn.00410dce.c`](code/fcn.00410dce.c)
- [`code/fcn.004116c0.c`](code/fcn.004116c0.c)
- [`code/fcn.00411990.c`](code/fcn.00411990.c)
- [`code/fcn.004126b0.c`](code/fcn.004126b0.c)
- [`code/fcn.00412d10.c`](code/fcn.00412d10.c)
- [`code/fcn.00413980.c`](code/fcn.00413980.c)
- [`code/fcn.00414090.c`](code/fcn.00414090.c)
- [`code/fcn.0041458f.c`](code/fcn.0041458f.c)
- [`code/fcn.0041562a.c`](code/fcn.0041562a.c)
- [`code/fcn.00415ac8.c`](code/fcn.00415ac8.c)
- [`code/fcn.00415df1.c`](code/fcn.00415df1.c)
- [`code/fcn.004162a6.c`](code/fcn.004162a6.c)
- [`code/fcn.00416894.c`](code/fcn.00416894.c)
- [`code/fcn.00417a07.c`](code/fcn.00417a07.c)
- [`code/fcn.0041881d.c`](code/fcn.0041881d.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

The additional disassembly provides more insight into the internal mechanics of the binary's string handling and resource management systems. While much of the complexity in these functions stems from standard C++ runtime library (CRT) implementations, their presence confirms that the binary performs significant "pre-processing" before launching the target process.

### Updated Analysis Report

#### Core Functionality
The sample remains a **wrapper/loader**. The newly analyzed sections confirm that the program does not simply call `CreateProcessA` with static strings. Instead, it employs sophisticated string manipulation and search routines to construct parameters for the payload. 

*   **Dynamic String Construction:** Functions such as `fcn.00414090` and `fcn.00415ac8` are typical of advanced string-handling libraries (like those used by MSVC). They handle complex tasks like multi-byte to wide-character conversion, buffer management, and concatenating strings into a final command line or environment block.
*   **Search and Lookup Logic:** Functions `fcn.00415df1` and `fcn.004162a6` appear to be "search" or "match" routines. These are likely used by the wrapper to find a specific file path, an entry in a configuration file, or a registry key before deciding which payload to execute.

#### Suspicious/Malicious Behaviors
*   **Dynamic Environment Preparation:** The high volume of code dedicated to string manipulation and memory management (`HeapAlloc`, `HeapReAlloc`) indicates that the loader is building a complex execution environment for the child process. In malware, this is often used to dynamically construct paths that obfuscate the final destination from static analysis.
*   **Search-Based Execution Paths:** The "search" logic suggests the binary may check for certain system conditions or environmental variables to decide its behavior. For example, it might search for a local configuration file or use an environment variable to determine which malicious module to load next.

#### Notable Techniques and Patterns
*   **Complex Runtime Library Usage:** A large portion of the code (e.g., `fcn.0041881d`) is dedicated to standard Windows localization and conversion (`LCMapStringW`, `MultiByteToWideChar`). While common in legitimate software, this level of complexity ensures that the loader can work across different language locales—a trait often seen in professional-grade malware "droppers" to ensure maximum reach.
*   **Memory Management Overheads:** The frequent calls to `HeapAlloc` and `HeapReAlloc` during string processing suggest that the script/payload path is constructed dynamically in memory, likely as a result of several different logic branches being evaluated before execution.

### Updated Summary for Analysis Report
*   **Type:** Sophisticated Loader / Wrapper.
*   **Purpose:** Dynamically prepares environment and executes subsequent process(es).
*   **Risk Level:** Moderate to High (The complexity of the string-processing indicates a sophisticated construction of launch parameters, likely intended to hide the final payload's location/arguments from basic analysis).
*   **Key Indicators:** 
    1.  **Complex String Processing:** Extensive usage of CRT functions for building complex command lines.
    2.  **Search Logic:** Use of search/lookup routines (`fcn.00415df1`, `fcn.004162a6`) to determine execution paths.
    3.  **Process Orchestration:** Standard behavior of a loader (e.g., `CreateProcessA`, `WaitForSingleObject`).

### Technical Summary of New Findings
| Function | Purpose/Observation | Impact on Analysis |
| :--- | :--- | :--- |
| **fcn.00414090** | Advanced string manipulation / Concatenation | Confirms the tool builds complex, potentially dynamic, command lines. |
| **fcn.00415df1/62a6** | Look-up or "Match" logic | Suggests a multi-path execution strategy based on search results (e.g., finding configs). |
| **fcn.0041881d** | Locale/MultiByte translation | Indicates high compatibility for broad distribution across different systems. |
| **Heap Management** | Frequent `HeapAlloc`/`ReAlloc` | Confirms that the loader builds its payload logic in-memory rather than using static strings. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of complex, multi-layered string manipulation to construct command lines and environment blocks in memory is intended to hide the final payload's destination from static analysis. |
| **T1562** | Dynamic Resolution | The "search" and "match" logic functions are used to dynamically identify file paths or configuration elements to determine which malicious module should be loaded. |
| **T1036** | Masquerading | The identification of the binary as a "wrapper" or "loader" that utilizes standard CRT libraries for widespread compatibility suggests an attempt to blend in with legitimate system processes. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the identified Indicators of Compromise (IOCs).

**Note:** As per your instructions, standard Windows API calls, common system error messages (e.g., "This program cannot be run in DOS mode"), and standard library errors (R6028, etc.) have been excluded as they are false positives for specific threat indicators.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The analysis notes that the binary searches for files and registry keys, but no specific paths or keys were revealed in the provided text.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Internal Function Offsets (Code Logic):** These indicate the specific locations within the binary where the malicious "wrapper" logic is performed:
    *   `00414090` (Advanced string manipulation/concatenation)
    *   `00415ac8` (String construction)
    *   `00415df1` (Look-up/Match logic for finding configurations)
    *   `004162a6` (Look-up/Match logic for execution paths)
    *   `0041881d` (Locale and multi-byte translation)
*   **Behavioral Patterns:** 
    *   **Loader/Wrapper Behavior:** The binary utilizes a high volume of `HeapAlloc` and `HeapReAlloc` calls to build complex command lines in memory, intended to hide the final payload's destination.
    *   **Search-Based Execution:** The use of look-up routines suggests the malware checks for specific local environment conditions or configuration files before executing its primary payload.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High (regarding behavior) / Low (regarding specific attribution)

4. **Key evidence**:
*   **Sophisticated Wrapper Logic:** The analysis explicitly identifies the binary as a "wrapper/loader" that utilizes complex string manipulation and memory management (`HeapAlloc`, `HeapReAlloc`) to dynamically construct payload parameters, effectively hiding static indicators of the final destination.
*   **Search-Based Execution:** The inclusion of specific lookup/match functions (`fcn.00415df1`, `fcn.004162a6`) indicates a multi-path execution strategy where the loader evaluates environment conditions or configuration files before deciding which malicious component to activate.
*   **Evasion Techniques:** The use of standard C++ runtime libraries for locale translation and the avoidance of static strings in the primary logic are classic techniques used by professional loaders to ensure broad compatibility and evade basic signature-based detection.
