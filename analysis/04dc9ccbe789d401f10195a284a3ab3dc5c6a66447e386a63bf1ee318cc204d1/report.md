# Threat Analysis Report

**Generated:** 2026-07-12 08:18 UTC
**Sample:** `04dc9ccbe789d401f10195a284a3ab3dc5c6a66447e386a63bf1ee318cc204d1_04dc9ccbe789d401f10195a284a3ab3dc5c6a66447e386a63bf1ee318cc204d1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04dc9ccbe789d401f10195a284a3ab3dc5c6a66447e386a63bf1ee318cc204d1_04dc9ccbe789d401f10195a284a3ab3dc5c6a66447e386a63bf1ee318cc204d1.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 86,318,867 bytes |
| MD5 | `608f24c38bba03af4763192ccca11dc3` |
| SHA1 | `01072d230672639e919cd1c94e5cf0f4fc49db82` |
| SHA256 | `04dc9ccbe789d401f10195a284a3ab3dc5c6a66447e386a63bf1ee318cc204d1` |
| Overall entropy | 7.997 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769953248 |
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
| `.rsrc` | 62,976 | 7.555 | ⚠️ Yes |
| `.reloc` | 2,048 | 5.264 | No |

### Imports

**USER32.dll**: `CreateWindowExW`, `ShutdownBlockReasonCreate`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `TranslateMessage`, `PostMessageW`, `GetMessageW`, `MessageBoxW`, `MessageBoxA`, `SystemParametersInfoW`
**COMCTL32.dll**: `ord_380`
**KERNEL32.dll**: `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetFileAttributesExW`, `SetEnvironmentVariableW`, `FlushFileBuffers`, `LCMapStringW`, `CompareStringW`, `VirtualProtect`, `InitializeCriticalSectionEx`, `GetOEMCP`, `GetCPInfo`, `GetLastError`, `FreeLibrary`, `GetProcAddress`
**ADVAPI32.dll**: `OpenProcessToken`, `GetTokenInformation`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `ConvertSidToStringSidW`
**GDI32.dll**: `SelectObject`, `DeleteObject`, `CreateFontIndirectW`

## Extracted Strings

Total strings found: **179931** (showing first 100)

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

This third chunk of disassembly provides definitive evidence regarding the execution model and internal architecture of the binary. It confirms that this is not just a wrapper, but a **sophisticated multi-process environment** typical of high-complexity Python applications bundled with heavy external dependencies (like Tcl/Tk or complex C-extensions).

The following analysis incorporates all previous findings into an updated technical profile.

---

### **Updated Analysis Summary**

#### **1. Execution Architecture & "Hidden" Logic**
The most significant finding in this chunk is the presence of multi-process management:
*   **PyInstaller Multi-Process Handling:** Function `fcn.140009fe0` contains a call to `CreateProcessW` with a specifically named window class: `"PyInstallerOnefileHiddenWindow"`. 
    *   *Significance:* This is a signature of PyInstaller’s "OneFile" mode. It indicates that the original binary may spawn a secondary, "hidden" process to run the actual Python interpreter or logic while the primary process handles the environment setup (like window management or DLL loading).
    *   *Evasion Note:* This architecture allows malicious logic to be decoupled from the initial entry point of the executable, making it harder for basic sandbox analysis to link all actions to a single process.

#### **2. Low-Level Runtime/Interpreter behavior**
The complexity of `fcn.140014e90` and `fcn.140014a20` indicates deep integration with an interpreter's core:
*   **Complex State Dispatch:** These functions feature massive nested conditional blocks based on character comparisons (e.g., checking if a value is less than 'e', 'T', or 'x'). This is characteristic of **command dispatching** in languages like Tcl or the internal evaluation of bytecodes/opcodes in Python.
*   **Heavy Buffer Management:** Function `fcn.140025c60` contains complex bit-shifting and modulo arithmetic to calculate memory offsets. This suggests a sophisticated memory management system for handling large data structures or "object" arrays, common in high-performance C-extensions (e.g., those used by **NumPy**).

#### **3. System Interaction & I/O Management**
The binary interacts with the OS through robust, standard-compliant wrappers:
*   **Environment Manipulation:** `fcn.140023094` performs extensive checks and sets environment variables using `SetEnvironmentVariableW`. This is often used to configure paths for shared libraries or internal configuration settings before jumping into the primary logic.
*   **Robust I/O Handling:** `fcn.14001d810` manages raw reads from the console (`ReadConsoleW`) and files. It includes specific logic to handle different lengths and potential overflow protections, indicating that the application is designed for stable, long-running operations rather than a simple "one-off" script execution.
*   **Data Processing:** `fcn.140005f70` shows high-volume data parsing/scanning across large buffers. This likely corresponds to internal logic for processing datasets or configuration files in memory before they are acted upon.

---

### **Updated Intelligence Profile**

| Feature | Detail | Analysis Impact |
| :--- | :--- | :--- |
| **Wrapper Type** | PyInstaller (OneFile Mode) | The binary is a container. Significant logic resides in the unpacked `.pyc` or bundled DLLs. |
| **Environment** | Hybrid (Python + Tcl + C-extensions) | The presence of Tcl and high-end math support suggests a tool for data analysis, GUI heavy applications, or complex system automation. |
| **Execution Method** | Multi-process/Hidden Window | It likely spawns a secondary process to hide its main activity from the user interface. |
| **Data Handling** | Complex Memory Management | The code is designed to handle large datasets or specialized data structures in memory. |

---

### **Updated Analysis Strategy for Analysts**

**1. Identifying "The Real Threat":**
Because of the `PyInstallerOnefileHiddenWindow` and Tcl-like dispatchers, the core malicious logic (if any) is likely hidden deep within:
*   **Embedded Python Files:** Extract using `pyinstxtractor.py`.
*   **High-Performance Libraries:** The "heavy math" and bitmasking indicate that if there is a payload involving encryption or complex data manipulation, it's likely inside the specialized `.pyd` (Python DLL) files.

**2. Behavior Monitoring:**
Because of the multi-process nature, **standard process-tree monitoring is required.** Analysis must watch for:
*   The launch of child processes from the initial .exe.
*   Changes to environment variables in the session preceding the execution of core logic.
*   High-volume memory allocation or file system crawls occurring in the "hidden" child processes.

**3. Technical Conclusion:**
This is a **sophisticated containerized application.** The complexity suggests that an actor who chose this method did so to blend in with legitimate, high-complexity software (like engineering tools, data processing suites, or specialized networking utilities). The sheer amount of "boilerplate" code for memory management and interpretation makes it a difficult target for manual static analysis of the .exe alone.

**Recommendation:** Proceed immediately with **unpacking the PyInstaller layer**. Focus on the extracted `.pyc` files to determine the actual intent (e.g., data exfiltration, cryptomining, or credential theft).

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036.005** | Masquerading: Other | The use of PyInstaller "OneFile" mode and specific hidden window classes is used to blend the malicious logic with legitimate, complex software characteristics. |
| **T1059.004** | Command and Scripting Interpreter: Python | The analysis identifies a multi-process environment typical of bundled Python applications requiring specialized handling for `.pyc` and `.pyd` components. |
| **T1027** | Obfuscated Files or Information | The use of complex dispatchers, heavy buffer management, and convoluted logic is intended to complicate manual static analysis and hide the true intent of the code. |
| **T1036.003** | Masquerading: Dynamic Link Library (Contextual) | While not strictly a DLL masquerade, the behavior of using a primary process as a wrapper/loader for secondary processes is a technique to decouple malicious actions from initial entry points. |

### Analyst Notes on Findings:
*   **T1036.005 (Masquerading):** The specific mention of `PyInstallerOnefileHiddenWindow` indicates an attempt to evade detection by blending in with common development tools, making it harder for automated systems to flag the process as a standalone malicious threat.
*   **T1059.004 (Python Interpreter):** Because the "real" logic is nested within Python-specific constructs, standard x86/x64 analysis of the `.exe` provides an incomplete picture; the core payload remains hidden until the interpreter environment is fully analyzed.
*   **T1027 (Obfuscation via Complexity):** The complexity noted in `fcn.140014e90` and `fcn.140025c60` serves as a "complexity barrier," forcing analysts to spend more time deciphering standard interpreter behavior before they can see the actual malicious instructions.

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral reports, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Strings" section contained primarily obfuscated data, standard compiler overhead, and internal PE section headers which do not constitute unique indicators of compromise.

### **Indicators of Compromise**

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (Internal PE sections like `.rdata`, `.data`, and `.pdata` were excluded as standard system artifacts).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Window Class:** `PyInstallerOnefileHiddenWindow` 
    *   *Context:* This is a specific artifact used by the PyInstaller "OneFile" bundle to hide the secondary process running the Python interpreter. While not a unique C2 indicator, it confirms the use of a multi-process execution wrapper to mask activity.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: Medium

4. **Key evidence**:
*   **PyInstaller Wrapper Architecture:** The presence of `PyInstallerOnefileHiddenWindow` and multi-process management confirms the binary acts as a container/loader. It is designed to hide the primary payload (likely Python bytecode) within a secondary, hidden process.
*   **Sophisticated Evasion Techniques:** The analysis notes high levels of complexity in memory management (`fcn.140025c60`) and command dispatching, specifically intended to create a "complexity barrier" for analysts and mask the underlying functionality.
*   **Intentional Decoupling:** The use of a script-interpreter environment (Python/Tcl) allows the threat actor to separate the malicious actions from the initial executable's signature, which is a hallmark of sophisticated loaders designed to bypass basic security filters.
