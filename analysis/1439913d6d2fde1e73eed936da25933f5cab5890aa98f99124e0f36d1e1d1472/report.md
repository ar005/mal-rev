# Threat Analysis Report

**Generated:** 2026-09-04 20:09 UTC
**Sample:** `1439913d6d2fde1e73eed936da25933f5cab5890aa98f99124e0f36d1e1d1472_1439913d6d2fde1e73eed936da25933f5cab5890aa98f99124e0f36d1e1d1472.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1439913d6d2fde1e73eed936da25933f5cab5890aa98f99124e0f36d1e1d1472_1439913d6d2fde1e73eed936da25933f5cab5890aa98f99124e0f36d1e1d1472.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 80,371,082 bytes |
| MD5 | `fb1795ea7bfda7999ed318c9fe1bbce7` |
| SHA1 | `2bafa3004e6cfdd00a807db6b6f035bca0ec3271` |
| SHA256 | `1439913d6d2fde1e73eed936da25933f5cab5890aa98f99124e0f36d1e1d1472` |
| Overall entropy | 7.997 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1778367982 |
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

Total strings found: **162272** (showing first 100)

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

This final segment of disassembly confirms the previous theories regarding the binary's nature as a high-complexity "wrapper" while providing specific evidence of how it handles its internal payload.

The addition of Chunk 3 introduces several key technical indicators that define exactly how this binary functions as a container for complex, potentially multi-layered logic.

### 1. Updated Technical Analysis of New Functions

#### A. PyInstaller "OneFile" Bootloader Characteristics
In **fcn.140009fe0**, we see a critical sequence of Windows API calls:
*   **Key Strings:** `PyInstallerOnefileHiddenWindow` and `PyInstaller Onefile Hidden Window`.
*   **Functions:** `RegisterClassW`, `CreateWindowExW`, `ShowWindow(..., 0)`, and `CreateProcessW`.
*   **Analysis:** This is a definitive signature of the **PyInstaller "OneFile" bootloader**. The purpose of this code is to unpack the embedded Python files into a temporary directory (or memory) and then spawn a secondary process (the actual interpreter) while hiding the window.
*   **Implication:** The primary work—the logic that actually performs tasks, handles data, or interacts with the user—is not contained in these functions. They are "scaffolding" designed to provide a seamless execution environment for the bundled Python scripts.

#### B. Complex Data Parsing and Extraction
Functions like **fcn.140005f70** and **fcn.140025c60** exhibit high complexity in data manipulation:
*   **Behavior:** These functions iterate through large memory buffers, checking for specific byte patterns (like `'o'`, `'='`, or spaces) and performing complex bitwise shifts (`<<`) and arithmetic to determine lengths of subsequent segments.
*   **Analysis:** This is the internal logic used to **parse Python's bundled archives**. When a PyInstaller executable runs, it must "unpack" its contents. These functions are the engine that interprets the internal metadata of the embedded `.pyz` or similar files to find and load modules and scripts correctly.

#### C. Environment Setup and Management
Function **fcn.140023094** involves:
*   **Behavior:** Mapping out memory, performing length checks on buffers, and interacting with `SetEnvironmentVariableW`.
*   **Analysis:** This is the "plumbing" required to configure the environment for a Python interpreter. It ensures that internal paths, library locations (like those for **NumPy/SciPy** identified in Chunk 2), and system variables are set correctly before the main script is executed.

#### D. I/O and Result Handling
Function **fcn.14000feac** involves:
*   **Behavior:** Extensive loops involving `WriteFile` and standard input/output (STDIN/STDOUT) checks. 
*   **Analysis:** This function appears to manage the bridge between the "inner" script and the "outer" system. It handles how data is actually output or written to files, potentially handling multiple lines or different types of buffer reads.

---

### Final Consolidated Analysis (All Chunks Combined)

#### 1. Core Architecture: The "Swiss Army Knife" Wrapper
The binary is not a standalone application in the traditional sense; it is a **highly sophisticated bootloader**. It utilizes a multi-layered approach to execute code:
*   **Layer 1 (The Stub):** The EXE we have analyzed. Its job is to unpack the environment, set variables, and host the interpreter.
*   **Layer 2 (The Interpreter):** A bundled Python/Tcl environment that provides the "logic."
*   **Layer 3 (The Payload):** The actual scripts (potentially involving heavy mathematics via AVX instructions) and GUI elements (via Tcl/Tk).

#### 2. Technical Complexity Indicators
*   **Hybrid Environment:** The presence of **Python + Tcl/Tk** suggests a capability for complex logic combined with potentially graphical user interfaces or interactive elements.
*   **High-Performance Processing:** The inclusion of specialized CPU instructions (AVX) and the specific "heavy" math libraries suggest that the payload is capable of intensive data processing, cryptography, or advanced engineering calculations.
*   **Robust Packaging:** By using PyInstaller's "OneFile" mode with a hidden window, the author ensures that the complex dependencies are bundled into a single file that can be distributed easily while hiding the "clutter" of the initialization process from the user.

### Summary for Analysts

This binary is a **sophisticated wrapper/launcher**. It is engineered to hide the complexity and size of its internal payload by bundling everything—interpreter, libraries, and scripts—into a single executable. 

**Key Intelligence Points:**
1.  **Hidden Intentions:** The use of "HiddenWindow" and `CreateProcessW` indicates that while the first process (the one analyzed) is mostly management-oriented, it prepares the ground for a secondary process to perform the primary work in the background.
2.  **Complexity Warning:** The amount of "plumbing" code required just to *start* the environment (parsed from these three chunks) suggests that the actual payload script(s) are likely large and feature-rich.
3.  **Extraction Requirement:** Because the core logic is nested within a PyInstaller structure, **static analysis of this EXE's disassembly alone will not reveal the full malicious or functional intent.** 

**Recommended Action Plan:**
*   **Step 1: Extraction.** Use `pyinstxtractor` (or similar tools) to unpack the `.pyz` files and extract any `.pyc` (compiled Python) or `.tcl` scripts.
*   **Step 2: Decompilation.** Once extracted, decompile the `.pyc` files into readable `.py` source code using `uncompyle6` or `pycdc`.
*   **Step 3: Payload Analysis.** Analyze the resulting Python/Tcl code to identify the actual core functionality (e.g., data exfiltration, mining algorithms, encryption routines).

**Risk Level:** **Moderate-High**. While this structure is common in legitimate specialized engineering software, it is equally used by advanced malware actors to bundle complex behaviors into a single, easily distributable file while evading simple detection of the "raw" script.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors observed in the provided technical analysis to the relevant MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a PyInstaller "OneFile" wrapper and multi-layered architecture is designed to mask the complexity, size, and ultimate intent of the internal payload. |
| **T1136** | Modify Environment Variables | Function `fcn.140023094` specifically utilizes `SetEnvironmentVariableW` to configure paths and system variables for the Python interpreter. |
| **T1059.003** | Command and Scripting Interpreter: Python | The analysis confirms that the core "logic" of the application resides within a bundled Python environment, which is then executed via the wrapper. |
| **T1059.004** | Command and Scripting Interpreter: Tcl | The analysis identifies the inclusion of Tcl/Tk as part of the core logic layer for potential interactive elements or GUI functionality. |

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contains heavily obfuscated or non-standard character sets that do not resolve into clear IP addresses, URLs, or file paths. However, the Behavioral Analysis identifies specific strings used by the underlying framework.

**IP addresses / URLs / Domains**
*   (None)

**File paths / Registry keys**
*   (None - Note: While the analysis mentions internal Python library locations and temporary directory usage, no specific malicious hardcoded paths or registry keys were identified.)

**Mutex names / Named pipes**
*   (None)

**Hashes**
*   (None)

**Other artifacts**
*   **PyInstaller Artifacts:** 
    *   `PyInstallerOnefileHiddenWindow`
    *   `PyInstaller Onefile Hidden Window`
*   **Behavioral Indicators:**
    *   **Execution Pattern:** Use of `CreateProcessW` to spawn a secondary process while suppressing the window (`ShowWindow(..., 0)`).
    *   **Tooling/Frameworks:** Identified usage of **PyInstaller "OneFile"** bootloader, **Tcl/Tk** graphical elements, and high-performance math libraries (**NumPy/SciPy**).
    *   **Extraction Requirements:** The presence of a `.pyz` or similar internal structure typical of PyInstaller.

---

## Malware Family Classification

1. **Malware family**: Unknown (PyInstaller-based wrapper)
2. **Malware type**: Loader
3. **Confidence**: Medium

4. **Key evidence**:
*   **PyInstaller Bootloader Signature:** The presence of `PyInstallerOnefileHiddenWindow` strings and the sequence of `RegisterClassW`, `CreateWindowExW`, and `CreateProcessW` confirms the binary functions as a "one-file" wrapper to hide its true payload.
*   **Multi-layered Obfuscation:** The analysis highlights that the core malicious logic is not contained within the executable's disassembly but is hidden within bundled Python (.pyz) or Tcl scripts, designed specifically to evade basic static analysis.
*   **Sophisticated Payload Environment:** The inclusion of high-performance libraries (NumPy/SciPy), AVX instructions, and Tcl/Tk indicates that the underlying payload is complex—likely involving heavy computation, data processing, or custom encryption—rather than a simple script.
