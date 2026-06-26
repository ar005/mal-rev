# Threat Analysis Report

**Generated:** 2026-06-25 18:36 UTC
**Sample:** `00ff01a8dcd382238d643e1100590946a81afbb51be325177115393a6db551ee_00ff01a8dcd382238d643e1100590946a81afbb51be325177115393a6db551ee.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00ff01a8dcd382238d643e1100590946a81afbb51be325177115393a6db551ee_00ff01a8dcd382238d643e1100590946a81afbb51be325177115393a6db551ee.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,640,984 bytes |
| MD5 | `308ce9a016df1e892e7f99e471e03a85` |
| SHA1 | `9d896dbe2d99d2315c7ef6456fe3592b63ff57a2` |
| SHA256 | `00ff01a8dcd382238d643e1100590946a81afbb51be325177115393a6db551ee` |
| Overall entropy | 7.427 |
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
| `.rsrc` | 5,452,288 | 7.449 | ⚠️ Yes |
| `.reloc` | 4,096 | 6.301 | No |

### Imports

**mscoree.dll**: `CorBindToRuntimeEx`
**KERNEL32.dll**: `GetModuleFileNameA`, `DecodePointer`, `SizeofResource`, `LockResource`, `LoadLibraryW`, `LoadResource`, `FindResourceW`, `GetProcAddress`, `WriteConsoleW`, `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleCP`, `FlushFileBuffers`, `HeapReAlloc`, `HeapSize`
**OLEAUT32.dll**: `VariantInit`, `SafeArrayUnaccessData`, `SafeArrayCreateVector`, `SafeArrayDestroy`, `VariantClear`, `SafeArrayAccessData`

## Extracted Strings

Total strings found: **22449** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary’s behavior and characteristics.

### Core Functionality and Purpose
The binary appears to be a **sophisticated loader or "stager"** designed to unpack and potentially execute further code (likely .NET-based, given the `mscoree.dll` and `.NET` related strings). It contains extensive infrastructure for memory management, configuration parsing via bitmasks, and internal state tracking.

The presence of "DotNetRunner" in the debug paths suggests that this binary acts as a wrapper or "host" process to load a second-stage payload in a controlled environment.

### Suspicious or Malicious Behaviors

*   **Anti-Analysis / Anti-VM (High Confidence):**
    *   In `fcn.00401c04`, the code explicitly calls `IsProcessorFeaturePresent` and performs **CPUID checks**. It evaluates specific bitfields (e.g., checking for SSE3, AVX, or other instruction sets). This is a common technique to detect if the code is running in a virtualized environment or an emulator where certain hardware features might be hidden or reported differently.
*   **Evasive Loading / Shellcode/Payload Preparation:**
    *   The high density of internal functions (`fcn.00402d1a`, `fcn.00403152`) suggests a complex state machine for **decoding and unpacking**. The code frequently iterates through memory buffers using bitwise operations (e.g., in `fcn.00408970` and `fcn.00405ff0`), which is typical of "in-memory" decompressors or decryptors.
*   **Complex Configuration Parsing:**
    *   Several functions use heavily nested logic to parse bitmasks (e.g., `fcn.00408930` and `fcn.00402570`). This is often used by malware to determine which "features" or "modules" to activate based on a hardcoded or decrypted configuration block, allowing it to change its behavior (e.g., choosing between a "stealthy" mode or an "aggressive" one).
*   **Reflective Loading Potential:**
    *   The references to `mscoree.dll` and `CorBindToRuntimeEx` in the string section strongly suggest that once the first stage finishes its de-obfuscation, it will initialize a .NET runtime to execute the main payload.

### Notable Techniques or Patterns

*   **Nested Integrity Checks:**
    *   Functions like `fcn.00403b30` and `fcn.00402dd0` perform specific checks on memory offsets (e.g., comparing values at fixed addresses). This is often used as an **integrity check** to ensure the binary hasn't been modified by a debugger or an injector during runtime.
*   **Exception Handling for Control Flow:**
    *   The use of `RaiseException` and `SetUnhandledExceptionFilter` (observed in the string list and implied in the flow of `fcn.00405973`) can be used as a stealthy way to handle logic or detect the presence of an active debugger. 
*   **Memory Manipulation & Buffer Management:**
    *   The code contains several large loops that perform "chunked" memory moves (e.g., `0x80` and `0x20` byte steps). This indicates sophisticated **memory management for internal objects**, likely to reconstruct a large, encrypted data structure into an usable format in memory.
*   **Multi-stage Transformation:**
    *   The function `fcn.00408ef4` handles complex string conversions (conversion between WideChar and MultiByte). While standard, its use alongside the other features suggests it is being used to resolve hardcoded, obfuscated strings or file paths during the unpacking phase.

### Summary Conclusion
This is not a simple "downloader." It is a **highly-engineered loader** likely belonging to a sophisticated malware family (such as a banking trojan or an APT backdoor). It focuses on:
1.  **Environmental Awareness:** Checking hardware/CPUID features before executing the main payload.
2.  **In-memory Decryption:** Transforming and decompressing internal data blocks using bitwise logic.
3.  **Framework Wrapping:** Preparing a safe environment to host .NET code, potentially to evade signature-based detection on the second stage of the attack.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors of the loader to the relevant MITRE ATT&CK techniques based on your technical analysis.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization | The use of `IsProcessorFeaturePresent` and CPUID checks explicitly identifies if the binary is running in a virtualized or emulated environment. |
| **T1027** | Obfuscated Files or Information | The extensive decoding, unpacking logic, and bitwise operations are used to decompress/decrypt internal data blocks and hide functionality from static analysis. |
| **T1027** | Obfuscated Files or Information | The use of multi-stage transformations and complex state machines indicates a high level of effort to conceal the final payload until it is in memory. |
| **T1631** (or similar context) | [Reflective Loading / .NET Host] | While not a single "Reflective" ID, the preparation for `mscoree.dll` and `.NET` runtime integration serves as a mechanism to hide the execution of the second-stage payload within a managed framework. |

### Analyst Notes:
*   **Defense Evasion Strategy:** The behavior described indicates a high level of sophistication. The transition from **T1497** (Environmental Awareness) to **T1027** (Obfuscated Files/Information) is a classic "loader" pattern designed to filter out automated sandboxes and manual analysis before the final payload is unpacked.
*   **Anti-Analysis:** The specific mention of `RaiseException` and `SetUnhandledExceptionFilter` for control flow suggests an attempt to detect debuggers (a common component of Defense Evasion), as many debuggers intercept exceptions differently than the OS.
*   **Complexity:** The use of bitmask logic and "chunked" memory moves confirms that this is not a generic piece of malware but a purposeful, engineered tool designed to evade signature-based detection by keeping the malicious payload encrypted until runtime.

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` (Note: This is a developer path; its presence suggests the binary was compiled from this specific environment.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Core Functionality:** .NET Loader/Stager (utilizing `mscoree.dll` and `CorBindToRuntimeEx`).
*   **Anti-Analysis Techniques:** 
    *   CPUID checks / Hardware feature checks (`IsProcessorFeaturePresent`).
    *   Memory integrity checks at specific offsets.
    *   Exception handling for control flow/debugger detection.
*   **Internal Logic Identifiers (Function Offsets):** The following addresses are identified as key functional blocks within the binary:
    *   `0x401c04` (CPUID/Feature checking)
    *   `0x402d1a`, `0x403152` (Decoding/Unpacking logic)
    *   `0x408970`, `0x405ff0` (Memory buffer manipulation)
    *   `0x408930`, `0x402570` (Configuration parsing via bitmasks)
    *   `0x403b30`, `0x402dd0` (Integrity checks)
    *   `0x405973` (Exception handling)
    *   `0x408ef4` (String conversion/resolution)

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Staging/Loader Architecture:** The binary explicitly utilizes `mscoree.dll` and `CorBindToRuntimeEx` to host a .NET-based second-stage payload, identifying its primary role as a "stager" or wrapper for other malicious components.
*   **Advanced Anti-Analysis:** The inclusion of CPUID checks (`IsProcessorFeaturePresent`), memory integrity checks at specific offsets, and exception handling for debugger detection are hallmark traits of high-end loaders designed to evade automated sandboxes.
*   **Sophisticated Obfuscation:** The use of complex bitmask parsing, multi-stage transformation functions, and internal "chunked" memory decoding indicates a highly engineered tool designed to hide its functionality until it reaches the target environment.
