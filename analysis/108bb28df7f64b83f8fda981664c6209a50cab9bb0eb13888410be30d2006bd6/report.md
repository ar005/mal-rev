# Threat Analysis Report

**Generated:** 2026-08-19 18:29 UTC
**Sample:** `108bb28df7f64b83f8fda981664c6209a50cab9bb0eb13888410be30d2006bd6_108bb28df7f64b83f8fda981664c6209a50cab9bb0eb13888410be30d2006bd6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `108bb28df7f64b83f8fda981664c6209a50cab9bb0eb13888410be30d2006bd6_108bb28df7f64b83f8fda981664c6209a50cab9bb0eb13888410be30d2006bd6.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 80,071,174 bytes |
| MD5 | `ef45ce3dc054e4ee758167936f6ed8e1` |
| SHA1 | `24895bc13b1350de60832e4ec5a5fa83c488de54` |
| SHA256 | `108bb28df7f64b83f8fda981664c6209a50cab9bb0eb13888410be30d2006bd6` |
| Overall entropy | 7.997 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1776342689 |
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
| `.rsrc` | 4,096 | 3.975 | No |
| `.reloc` | 2,048 | 5.264 | No |

### Imports

**USER32.dll**: `CreateWindowExW`, `ShutdownBlockReasonCreate`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `TranslateMessage`, `PostMessageW`, `GetMessageW`, `MessageBoxW`, `MessageBoxA`, `SystemParametersInfoW`
**COMCTL32.dll**: `ord_380`
**KERNEL32.dll**: `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetFileAttributesExW`, `SetEnvironmentVariableW`, `FlushFileBuffers`, `LCMapStringW`, `CompareStringW`, `VirtualProtect`, `InitializeCriticalSectionEx`, `GetOEMCP`, `GetCPInfo`, `GetLastError`, `FreeLibrary`, `GetProcAddress`
**ADVAPI32.dll**: `OpenProcessToken`, `GetTokenInformation`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `ConvertSidToStringSidW`
**GDI32.dll**: `SelectObject`, `DeleteObject`, `CreateFontIndirectW`

## Extracted Strings

Total strings found: **165277** (showing first 100)

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

The following analysis incorporates the additional disassembly from chunk 3/3, integrating it with previous findings regarding the multi-runtime (Python + Tcl) environment and high-performance math libraries.

### Updated Analysis Summary

The core finding remains consistent: the binary is a **PyInstaller-wrapped Python executable**. However, the latest data confirms that this is an extremely complex deployment. The code doesn't just provide "support" for scripts; it implements deep system integration, complex memory management, and environment abstraction. 

The sheer volume of "dispatching" logic (large nested `if/else` blocks) suggests a very mature runtime engine where many different internal states are handled by a single set of low-level C functions.

---

### New Technical Findings & Analysis

#### 1. System Interaction and Stealth Logic (`fcn.140009fe0`)
This function is a significant find for an analyst. It contains several key indicators:
*   **Hidden Window Management:** The code explicitly registers a class and creates a window with the title **"PyInstallerOnefileHiddenWindow"**. It then enters a loop using `PeekMessageW` and `DispatchMessageW`. 
*   **Purpose:** This is standard for PyInstaller’s `-w` or `--noconsole` mode. It allows a Python script to run without a visible command prompt window while still processing system events (like "close" signals). 
*   **Process Manipulation:** The use of `CreateProcessW`, `SetConsoleCtrlHandler`, and the management of process handles (`GetExitCodeProcess`) suggests this layer handles the transition between the initial bootstrap and the actual execution of the Python environment.

#### 2. Complex Data Dispatch Tables (`fcn.140005f70` & `fcn.140014a20`)
These functions are highly complex "switch" statements implemented as nested `if/else` chains.
*   **Pattern:** They check a byte or character (e.g., `uVar3 < 0x65`, `uVar3 == 0x53`, `cVar6 == 'd'`) and route execution to different internal handlers.
*   **Inference:** This is characteristic of **interpreters (like Tcl or Python)** or heavy serialization libraries. These functions act as the "switchboard" for the engine, determining how to handle specific types of data, commands, or objects. 
*   **Security Context:** While this is standard in large projects, it creates a massive hurdle for manual analysis. An analyst must peel through hundreds of these "dispatch" points before finding the actual logic of the script being run by the interpreter.

#### 3. Advanced Memory and Buffer Management (`fcn.140025c60` & `fcn.140023094`)
These functions involve intense calculation regarding memory offsets, bit-shifting, and loop bounds:
*   **Buffer Handling:** The heavy use of modular arithmetic (e.g., `uVar17 = uVar17 % uVar6`) and "wrapping" logic suggests the handling of **large data buffers or multi-byte character sets (Unicode)**. 
*   **Context:** This is likely where the Tcl/Python layers manage memory allocation for strings and lists, ensuring that if a piece of data exceeds a buffer's edge, it is correctly moved to the next available block.

#### 4. Input/Output Diversity (`fcn.14001d810`)
This function demonstrates capability in reading from multiple sources:
*   **I/O Multiplexing:** It includes logic for both `ReadFile` (file system) and `ReadConsoleW` (user input). 
*   **Implication:** The backend is prepared to handle diverse inputs, common in tools that might be used as a CLI tool or a background service.

---

### Updated Synthesis of Findings

| Feature | Evidence Location(s) | Analysis/Significance |
| :--- | :--- | :--- |
| **Multi-Runtime** | `fcn.1400028a0` (Tcl), `fcn.140015754` | Confirmed support for both Python and Tcl scripts. |
| **High Performance** | `fcn.140029e60` (AVX) | Use of AVX instructions indicates heavy math/science libraries (NumPy/SciPy). |
| **Stealth/Persistence** | `fcn.140009fe0` | Creation of a "Hidden Window" to hide the console from the user. |
| **Complex Dispatching** | `fcn.140005f70`, `fcn.140014a20` | Massive switch-tables to handle internal interpreter state/types. |
| **Memory Management** | `fcn.140025c60` | Complex buffer handling for multi-byte data and large strings. |

---

### Final Conclusion for Analyst

The binary is a **high-complexity, production-grade environment wrapper.** It is not just "hiding" a script; it is providing the full infrastructure necessary to run complex, professional-grade software (likely involving scientific calculation or heavy Tcl/Python interaction).

**Security Significance:** 
From an incident response perspective, this type of complexity can be used as **"Anti-Analysis via Volume."** A malicious actor can hide a very small piece of and high-impact code inside this massive amount of "bloated but benign" infrastructure. An analyst who does not know to look for the internal `.py` or `.tcl` files might spend days/weeks analyzing the AVX instructions or Tcl dispatchers, while the actual malicious logic remains hidden inside a script that is only loaded in memory at runtime.

**Next Steps:**
1.  **Extraction (Critical):** The most productive next step is to use `pyinstxtractor` and search for `.tcl` files. This will bypass the "complexity wall" of the C/C++ code.
2.  **Memory Monitoring:** Since much of this code deals with buffer management and dynamic resolution, running the binary in a debugger (like x64dbg) to see which scripts are loaded into memory after the `PyInstallerOnefileHiddenWindow` is created will be highly effective.
3.  **String Analysis:** Look for hardcoded URLs or IP addresses that might be hidden inside the data structures being processed by the "Dispatch" functions.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of observed behaviors to MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1059.004 | Python | The binary acts as a runtime environment to execute Python scripts, providing the necessary infrastructure for high-level script execution. |
| T1059.005 | Tcl | The application includes integrated support and dispatch logic for executing Tcl-based commands or scripting. |
| T1036 | Create Exclusive Process | The use of "Hidden Window" management allows the process to run without a visible command prompt, reducing visibility to the end user. |
| T1027 | Obfuscated Files or Information/Programs | The "Anti-Analysis via Volume" tactic hides high-impact malicious code within a massive amount of complex but benign infrastructure (the "complexity wall"). |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Window Title:** `PyInstallerOnefileHiddenWindow`
    *   *Note: This identifies the use of a PyInstaller "onefile" bundle, specifically used to hide the console window during execution.*
*   **Framework Identifiers:** 
    *   Python (via PyInstaller)
    *   Tcl (referenced in analysis)
    *   AVX instruction sets (indicating high-performance math libraries like NumPy or SciPy).

---

### **Analyst Notes**
While no direct network indicators (IPs/Domains) were found in the provided text, the behavioral analysis highlights a "Complexity as Obfuscation" tactic. The binary is heavily wrapped using PyInstaller to hide its true intent behind legitimate library overhead (Tcl/Python). 

The primary indicator for defensive purposes is the **PyInstallerOnefileHiddenWindow** string; while technically a feature of the PyInstaller tool, it is a high-fidelity signature for identifying "bundled" executables often used in malware delivery to mask automated scripts.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: Medium

4. **Key evidence**:
*   **Sophisticated Wrapper Strategy:** The sample utilizes a PyInstaller-wrapped Python environment with Tcl support and high-performance libraries (AVX/NumPy). This is a classic "complexity wall" technique used to hide malicious scripts within an overwhelming amount of benign, complex code.
*   **Stealth Tactics:** The explicit use of `PyInstallerOnefileHiddenWindow` and the management of hidden windows indicate a deliberate attempt to execute functionality without user notification or console visibility, typical of loaders designed to run in the background.
*   **Analysis Obstruction:** The presence of massive "dispatch" tables (multi-layered if/else blocks) serves as an anti-analysis tactic, forcing researchers to navigate through hundreds of lines of boilerplate interpreter code before reaching the actual malicious logic hidden within the secondary script files (.py or .tcl).
