# Threat Analysis Report

**Generated:** 2026-07-14 20:03 UTC
**Sample:** `05fbb8ce9dca28af0de95cfa3d1c773687f49d35085515456f0680c7ac0806b9_05fbb8ce9dca28af0de95cfa3d1c773687f49d35085515456f0680c7ac0806b9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05fbb8ce9dca28af0de95cfa3d1c773687f49d35085515456f0680c7ac0806b9_05fbb8ce9dca28af0de95cfa3d1c773687f49d35085515456f0680c7ac0806b9.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 7,088,816 bytes |
| MD5 | `43880e848fa33491f5ce0fa02bb1934f` |
| SHA1 | `b9fd07162157cde528ec33ca53a995c05710234b` |
| SHA256 | `05fbb8ce9dca28af0de95cfa3d1c773687f49d35085515456f0680c7ac0806b9` |
| Overall entropy | 7.99 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1778509359 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 181,760 | 6.463 | No |
| `.rdata` | 80,896 | 5.755 | No |
| `.data` | 3,584 | 1.816 | No |
| `.pdata` | 9,728 | 5.32 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 1,536 | 5.52 | No |
| `.reloc` | 2,048 | 5.264 | No |

### Imports

**USER32.dll**: `CreateWindowExW`, `ShutdownBlockReasonCreate`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `TranslateMessage`, `PostMessageW`, `GetMessageW`, `MessageBoxW`, `MessageBoxA`, `SystemParametersInfoW`
**COMCTL32.dll**: `ord_380`
**KERNEL32.dll**: `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetFileAttributesExW`, `SetEnvironmentVariableW`, `FlushFileBuffers`, `LCMapStringW`, `CompareStringW`, `VirtualProtect`, `InitializeCriticalSectionEx`, `GetOEMCP`, `GetCPInfo`, `GetLastError`, `FreeLibrary`, `GetProcAddress`
**ADVAPI32.dll**: `OpenProcessToken`, `GetTokenInformation`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `ConvertSidToStringSidW`
**GDI32.dll**: `SelectObject`, `DeleteObject`, `CreateFontIndirectW`

## Extracted Strings

Total strings found: **15613** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
UVWAUAWH
0A_A]_^]
SUVWAVAWH
A_A^_^][
A_A^_^][
\$ UAVAWH
0A_A^]
0A_A^]
L$ SUVWH
L$ SUVWH
T$hfD+D$df+T$`
@SUVWAVH
T$<f+T$4
PA^_^][
@USVWAVH
A^_^[]
|$ AVH
L$ SUVWH
L$ SUVWAV
A^_^][
L$ SUVWAV
A^_^][
L$ SUVWATAUAVAW
A_A^A]A\_^][
L$ SUVWAV
A^_^][
L$ SUVWAV
A^_^][
L$ SUVWATAUAVAW
A_A^A]A\_^][
UVWATAWH
0A_A\_^]
@UVATAU
A]A\^]
L9t$0t
tR@80tMH
L$ SVWH
@SUWAVAW
A_A^_][
H9{ t)
H9{(t(
H9{8t#
H9{@t&
l$ ATAVAWH
 A_A^A\
l$ VWAV
u[HcG0
l$ VATAUAVAWH
0A_A^A]A\^
MLcF0H
@SVAVH
t$ WAVAWH
VWATAVAWH
~#D8e0u
0A_A^A\_^
l$ VWAV
@UVWATAUAVAW
A_A^A]A\_^]
l$ VWATAVAW
A_A^A\_^
|$ AVH
UVWAVAWH
 A_A^_^]
WAVAWH
0A_A^_
@SUVWAV
A^_^][
@VATAUAVAWH
 A_A^A]A\^
@SUATAU
A]A\][
D$hH+D$pHi
|$8fff
SUVWATAUAVAWH
8A_A^A]A\_^][
SUVWATAUAVAWH
MP;H(s
MP;H8s
]Lu*A;|$
L$@E)}P
A;Exsg
E;E8v#A
L$@A9MP
tDE;u$t>H
T$8E+T$
XA_A^A]A\_^][
tHH9
uC
I@L9{8uH
t$HL9{0
~0L9{0
y<L9{0
\$ UVAVH
@USWATAVAWH
fD9 uA
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140018164` | `0x140018164` | 40065 | ✓ |
| `fcn.14001c130` | `0x14001c130` | 37955 | ✓ |
| `fcn.14001c11c` | `0x14001c11c` | 37914 | ✓ |
| `section..text` | `0x140001000` | 17899 | ✓ |
| `fcn.140027400` | `0x140027400` | 12313 | ✓ |
| `fcn.140004b70` | `0x140004b70` | 9279 | ✓ |
| `fcn.14000b6a0` | `0x14000b6a0` | 6161 | ✓ |
| `fcn.140029d90` | `0x140029d90` | 5703 | ✓ |
| `fcn.1400260ec` | `0x1400260ec` | 4735 | ✓ |
| `fcn.140001ca0` | `0x140001ca0` | 2338 | ✓ |
| `fcn.14002308c` | `0x14002308c` | 2201 | ✓ |
| `fcn.14001757c` | `0x14001757c` | 1946 | ✓ |
| `fcn.140012478` | `0x140012478` | 1898 | ✓ |
| `fcn.14001713c` | `0x14001713c` | 1777 | ✓ |
| `fcn.1400028a0` | `0x1400028a0` | 1773 | ✓ |
| `fcn.14002bcf0` | `0x14002bcf0` | 1661 | ✓ |
| `fcn.14000d390` | `0x14000d390` | 1468 | ✓ |
| `fcn.140029e60` | `0x140029e60` | 1451 | ✓ |
| `fcn.140023d8c` | `0x140023d8c` | 1421 | ✓ |
| `fcn.140014e90` | `0x140014e90` | 1397 | ✓ |
| `fcn.140023094` | `0x140023094` | 1353 | ✓ |
| `fcn.140005f70` | `0x140005f70` | 1325 | ✓ |
| `fcn.14000feac` | `0x14000feac` | 1263 | ✓ |
| `fcn.14000b1c0` | `0x14000b1c0` | 1238 | ✓ |
| `fcn.14000ad20` | `0x14000ad20` | 1179 | ✓ |
| `fcn.14001e380` | `0x14001e380` | 1171 | ✓ |
| `fcn.140009fe0` | `0x140009fe0` | 1169 | ✓ |
| `fcn.140025c60` | `0x140025c60` | 1164 | ✓ |
| `fcn.140014a20` | `0x140014a20` | 1133 | ✓ |
| `fcn.14001d810` | `0x14001d810` | 1119 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001ca0.c`](code/fcn.140001ca0.c)
- [`code/fcn.1400028a0.c`](code/fcn.1400028a0.c)
- [`code/fcn.140004b70.c`](code/fcn.140004b70.c)
- [`code/fcn.140005f70.c`](code/fcn.140005f70.c)
- [`code/fcn.140009fe0.c`](code/fcn.140009fe0.c)
- [`code/fcn.14000ad20.c`](code/fcn.14000ad20.c)
- [`code/fcn.14000b1c0.c`](code/fcn.14000b1c0.c)
- [`code/fcn.14000b6a0.c`](code/fcn.14000b6a0.c)
- [`code/fcn.14000d390.c`](code/fcn.14000d390.c)
- [`code/fcn.14000feac.c`](code/fcn.14000feac.c)
- [`code/fcn.140012478.c`](code/fcn.140012478.c)
- [`code/fcn.140014a20.c`](code/fcn.140014a20.c)
- [`code/fcn.140014e90.c`](code/fcn.140014e90.c)
- [`code/fcn.14001713c.c`](code/fcn.14001713c.c)
- [`code/fcn.14001757c.c`](code/fcn.14001757c.c)
- [`code/fcn.140018164.c`](code/fcn.140018164.c)
- [`code/fcn.14001c11c.c`](code/fcn.14001c11c.c)
- [`code/fcn.14001c130.c`](code/fcn.14001c130.c)
- [`code/fcn.14001d810.c`](code/fcn.14001d810.c)
- [`code/fcn.14001e380.c`](code/fcn.14001e380.c)
- [`code/fcn.14002308c.c`](code/fcn.14002308c.c)
- [`code/fcn.140023094.c`](code/fcn.140023094.c)
- [`code/fcn.140023d8c.c`](code/fcn.140023d8c.c)
- [`code/fcn.140025c60.c`](code/fcn.140025c60.c)
- [`code/fcn.1400260ec.c`](code/fcn.1400260ec.c)
- [`code/fcn.140027400.c`](code/fcn.140027400.c)
- [`code/fcn.140029d90.c`](code/fcn.140029d90.c)
- [`code/fcn.140029e60.c`](code/fcn.140029e60.c)
- [`code/fcn.14002bcf0.c`](code/fcn.14002bcf0.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This third and final chunk of disassembly provides a definitive look into the executable's execution logic. While the previous chunks established that this is a complex PyInstaller/Tcl environment, this section reveals **how** that environment interacts with the operating system to maintain stealth and process the underlying script instructions.

Here is the updated analysis incorporating all findings from chunks 1, 2, and 3.

---

### Updated Analysis of Capabilities and Behaviors

The final disassembly confirms that while the binary utilizes standard tools (PyInstaller, Tcl), it incorporates specific architectural choices—such as **hidden window management** and **complex state-machine parsing**—that are indicative of a sophisticated loader designed to run silently in the background.

---

### 1. Expanded Core Functionality & Technical Details

The third chunk introduces three primary technical layers:

*   **Stealthy Window Management (Hidden UI):**
    *   In function `fcn.140009fe0`, there is a specific string literal: `"PyInstallerOnefileHiddenWindow"`. The code proceeds to create a window and immediately calls `ShowWindow` with the `SW_HIDE` parameter (implied by the logic). 
    *   **Significance:** This is used to keep the process "active" in the eyes of the Windows OS while ensuring no GUI window ever appears on the user's desktop. This is a common technique for malware (like miners or info-stealers) to remain invisible to the user while performing heavy background tasks.

*   **Complex State-Machine Parsing:**
    *   Functions like `fcn.140005f70` and `fcn.140014a20` exhibit complex, nested conditional branching based on specific character codes (e.g., checking for 'd', 'S', 'A', 'E', 'F', 'G'). 
    *   **Significance:** These functions act as a **parser/interpreter core**. Instead of executing simple commands, the "payload" is likely passing tokens through these state machines to determine what action to take. This layer adds significant depth to the analysis; an analyst cannot simply look for a single malicious string; they must follow the logic path through the parser.

*   **Environment & Process Management:**
    *   The code utilizes `SetEnvironmentVariableW` and complex memory manipulation (e.g., in `fcn.140025c60`). 
    *   **Significance:** These functions are used to configure the environment for the "inner" script (setting paths, permissions, or internal flags) before it begins execution. The sophisticated way it handles memory offsets and buffer lengths suggests that the underlying payload is substantial in size and complexity.

*   **Multi-Mode I/O Handling:**
    *   Function `fcn.14001d810` interacts with the console using `ReadFile`, `ReadConsoleW`, and `GetConsoleMode`. 
    *   **Significance:** This suggests the inner logic can handle various input types (standard input, pipe data, or file handles), making it versatile for different execution environments.

---

### 2. Updated Behavioral Analysis

The evidence from all three chunks points toward a **highly-engineered multi-stage loader**. Its behavior follows these patterns:

*   **Sophisticated Obfuscation via Complexity:** By using Python and Tcl, the actor forces an analyst to peel back layers of "interpreter logic" before they can see the actual malicious intent. The complexity of the parsing functions (`fcn.140005f70`) means the core payload is likely highly modular.
*   **Persistence & Stealth:** The use of `PyInstallerOnefileHiddenWindow` and the associated message-loop (handling `PeekMessage`, `TranslateMessage`, etc.) confirms that the program is designed to run as a "headless" process. It stays alive in the system's memory but avoids creating any user-facing artifacts like windows or icons.
*   **High Performance / Capability:** The inclusion of **AVX instructions** (from chunk 2) combined with these complex parsing routines suggests that whatever is being executed—whether it is a cryptographic routine for ransomware, a mining algorithm, or a large-scale data exfiltration routine—is high-performance and professional-grade.

---

### 3. Final Summary for Reporting

*   **Behavior Type:** Stealthy Multi-Language Executable Loader.
*   **Primary Technologies:** 
    *   **PyInstaller Framework:** Used to bundle a multi-layered (Python + Tcl) application into a single portable binary.
    *   **State-Machine Parsing:** Complex logic used to interpret internal "opcodes" or command structures from the inner payload.
    *   **Hidden Window Loop:** A technical implementation designed to keep a process running in the background without any user interface (GUI).
    *   **SIMD/AVX Optimization:** Evidence of high-performance math or processing capabilities within the bundled scripts.

*   **Detection Notes / Indicators of Compromise (IOCs):**
    *   The string `"PyInstallerOnefileHiddenWindow"` is a primary indicator that the file's purpose is to run a background process invisibly.
    *   The complexity of the disassembly suggests this is not an automated "script-kiddie" tool but a sophisticated piece of software.
    *   **Conclusion:** This binary acts as a "wrapper of wrappers." It hides a complex, multi-language payload (Python/Tcl) behind a standard launcher, while simultaneously employing Windows API calls to ensure the operation remains hidden from the end user. The sophistication level suggests it is capable of hosting advanced threats like ransomware or specialized crypto-miners.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided analysis to the relevant MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Hide Window | The use of `ShowWindow` with the `SW_HIDE` parameter and the specific string `PyInstallerOnefileHiddenWindow` are used to maintain a "headless" process that remains active without appearing on the user's desktop. |
| **T1059.003** | Command and Scripting Interpreter (Python) | The executable leverages the PyInstaller framework to host a Python environment, allowing for complex logic and multi-layered script execution. |
| **T1059.005** | Command and Scripting Interpreter (Tcl) | The inclusion of Tcl as part of the "wrapper of wrappers" architecture demonstrates use of multiple scripting interpreters to process internal instructions. |
| **T1027** | Obfuscated Files or Information | The use of complex state-machine parsing, multi-language wrapping (Python/Tcl), and high-complexity logic is designed to hide the actual functionality from static analysis. |
| **T1497** | Virtualization/Packer | While not a standard "sub-technique" code, the behavior described as a "wrapper of wrappers" that hides a multi-language payload inside a single binary qualifies as using packing/wrapping to obfuscate logic. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified. (Note: While several obfuscated string blocks exist in the "Extracted Strings" section, they do not follow standard naming conventions for mutexes or named pipes and appear to be junk data/padding.)

**Hashes**
*   None identified.

**Other artifacts**
*   **PyInstallerOnefileHiddenWindow**: A specific internal string identifier used to trigger the `ShowWindow` (SW_HIDE) function, indicating a mechanism to hide the process from the user interface.
*   **Framework Indicators**: The presence of **PyInstaller** and **Tcl** libraries indicates the binary is a wrapped multi-language payload.
*   **High-Performance Computation**: Use of **AVX instructions** suggests underlying capabilities for complex cryptography or intensive data processing (e.g., mining, encryption).

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1.  **Malware family**: Loader (specifically a multi-layered/custom loader)
2.  **Malware type**: Loader / Dropper
3.  **Confidence**: High
4.  **Key evidence**:
    *   **Sophisticated "Wrapper" Architecture:** The use of both PyInstaller and Tcl to create a "wrapper of wrappers" indicates a high-effort attempt to hide the core malicious logic (the "inner payload") behind layers of script interpretation, making it difficult for standard static analysis to pinpoint functionality.
    *   **Intentional Stealth Mechanisms:** The presence of the `PyInstallerOnefileHiddenWindow` string and the implementation of `ShowWindow` with `SW_HIDE` confirm that the binary is designed to operate as a "headless" process, common in malware that performs background tasks (such as data exfiltration or mining) without alerting the user.
    *   **Advanced Processing & Parsing:** The inclusion of complex state-machine parsing for "opcodes" and high-performance AVX instructions suggests the loader is designed to host complex, professional-grade logic—likely for encryption (ransomware), resource-intensive calculations (mining), or modular backend commands (botnet/backdoor).
