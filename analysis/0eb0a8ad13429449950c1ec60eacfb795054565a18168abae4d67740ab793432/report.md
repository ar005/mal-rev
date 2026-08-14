# Threat Analysis Report

**Generated:** 2026-08-13 19:44 UTC
**Sample:** `0eb0a8ad13429449950c1ec60eacfb795054565a18168abae4d67740ab793432_0eb0a8ad13429449950c1ec60eacfb795054565a18168abae4d67740ab793432.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0eb0a8ad13429449950c1ec60eacfb795054565a18168abae4d67740ab793432_0eb0a8ad13429449950c1ec60eacfb795054565a18168abae4d67740ab793432.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 7 sections |
| Size | 9,557,457 bytes |
| MD5 | `5a064bd100c58f7f9bd4fb1830118524` |
| SHA1 | `9d2a14d473c1e8564cf43f4d7701990b26716509` |
| SHA256 | `0eb0a8ad13429449950c1ec60eacfb795054565a18168abae4d67740ab793432` |
| Overall entropy | 7.99 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1776356664 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 186,880 | 6.477 | No |
| `.rdata` | 80,384 | 5.764 | No |
| `.data` | 3,584 | 1.821 | No |
| `.pdata` | 9,728 | 5.383 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 268,288 | 7.324 | ⚠️ Yes |
| `.reloc` | 2,048 | 5.271 | No |

### Imports

**USER32.dll**: `TranslateMessage`, `ShutdownBlockReasonCreate`, `GetWindowThreadProcessId`, `SetWindowLongPtrW`, `GetWindowLongPtrW`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `CreateWindowExW`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `GetMessageW`
**KERNEL32.dll**: `GetTimeZoneInformation`, `GetProcessHeap`, `FreeEnvironmentStringsW`, `GetEnvironmentStringsW`, `GetCPInfo`, `GetOEMCP`, `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetLastError`, `FreeLibrary`, `GetProcAddress`, `LoadLibraryExW`, `FormatMessageW`, `GetModuleFileNameW`
**ADVAPI32.dll**: `ConvertSidToStringSidW`, `GetTokenInformation`, `OpenProcessToken`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`

## Extracted Strings

Total strings found: **20801** (showing first 100)

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
L$ SUVWH
L$ SVWH
L$ SVWH
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
@UVWAT
L9t$0t
tM@8(tHH
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
t);\$8u#3
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
A_A^A\_[]
uxHc\*
u0HcH<
WATAUAVAWH
A_A^A]A\_
WATAUAVAWH
 A_A^A]A\_
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400191dc` | `0x1400191dc` | 41017 | ✓ |
| `fcn.14001d1f0` | `0x14001d1f0` | 38835 | ✓ |
| `fcn.14001d1dc` | `0x14001d1dc` | 38794 | ✓ |
| `main` | `0x140001000` | 14863 | ✓ |
| `fcn.140028830` | `0x140028830` | 12313 | ✓ |
| `fcn.140003fa0` | `0x140003fa0` | 6287 | ✓ |
| `fcn.14000ab90` | `0x14000ab90` | 6161 | ✓ |
| `fcn.14002b1c0` | `0x14002b1c0` | 5703 | ✓ |
| `fcn.14002751c` | `0x14002751c` | 4735 | ✓ |
| `fcn.140001c80` | `0x140001c80` | 2338 | ✓ |
| `fcn.1400244bc` | `0x1400244bc` | 2201 | ✓ |
| `fcn.1400187ac` | `0x1400187ac` | 1946 | ✓ |
| `fcn.140011980` | `0x140011980` | 1898 | ✓ |
| `fcn.1400181bc` | `0x1400181bc` | 1777 | ✓ |
| `fcn.140002880` | `0x140002880` | 1773 | ✓ |
| `fcn.14002d120` | `0x14002d120` | 1661 | ✓ |
| `fcn.140015484` | `0x140015484` | 1532 | ✓ |
| `fcn.14000c880` | `0x14000c880` | 1468 | ✓ |
| `fcn.14002b290` | `0x14002b290` | 1451 | ✓ |
| `fcn.1400251bc` | `0x1400251bc` | 1421 | ✓ |
| `fcn.140015a80` | `0x140015a80` | 1397 | ✓ |
| `fcn.1400244c4` | `0x1400244c4` | 1353 | ✓ |
| `fcn.140014adc` | `0x140014adc` | 1336 | ✓ |
| `fcn.140005390` | `0x140005390` | 1325 | ✓ |
| `fcn.14000f36c` | `0x14000f36c` | 1263 | ✓ |
| `fcn.14000a6b0` | `0x14000a6b0` | 1238 | ✓ |
| `fcn.14000a210` | `0x14000a210` | 1179 | ✓ |
| `fcn.14001f440` | `0x14001f440` | 1171 | ✓ |
| `fcn.140009430` | `0x140009430` | 1169 | ✓ |
| `fcn.140027090` | `0x140027090` | 1164 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001c80.c`](code/fcn.140001c80.c)
- [`code/fcn.140002880.c`](code/fcn.140002880.c)
- [`code/fcn.140003fa0.c`](code/fcn.140003fa0.c)
- [`code/fcn.140005390.c`](code/fcn.140005390.c)
- [`code/fcn.140009430.c`](code/fcn.140009430.c)
- [`code/fcn.14000a210.c`](code/fcn.14000a210.c)
- [`code/fcn.14000a6b0.c`](code/fcn.14000a6b0.c)
- [`code/fcn.14000ab90.c`](code/fcn.14000ab90.c)
- [`code/fcn.14000c880.c`](code/fcn.14000c880.c)
- [`code/fcn.14000f36c.c`](code/fcn.14000f36c.c)
- [`code/fcn.140011980.c`](code/fcn.140011980.c)
- [`code/fcn.140014adc.c`](code/fcn.140014adc.c)
- [`code/fcn.140015484.c`](code/fcn.140015484.c)
- [`code/fcn.140015a80.c`](code/fcn.140015a80.c)
- [`code/fcn.1400181bc.c`](code/fcn.1400181bc.c)
- [`code/fcn.1400187ac.c`](code/fcn.1400187ac.c)
- [`code/fcn.1400191dc.c`](code/fcn.1400191dc.c)
- [`code/fcn.14001d1dc.c`](code/fcn.14001d1dc.c)
- [`code/fcn.14001d1f0.c`](code/fcn.14001d1f0.c)
- [`code/fcn.14001f440.c`](code/fcn.14001f440.c)
- [`code/fcn.1400244bc.c`](code/fcn.1400244bc.c)
- [`code/fcn.1400244c4.c`](code/fcn.1400244c4.c)
- [`code/fcn.1400251bc.c`](code/fcn.1400251bc.c)
- [`code/fcn.140027090.c`](code/fcn.140027090.c)
- [`code/fcn.14002751c.c`](code/fcn.14002751c.c)
- [`code/fcn.140028830.c`](code/fcn.140028830.c)
- [`code/fcn.14002b1c0.c`](code/fcn.14002b1c0.c)
- [`code/fcn.14002b290.c`](code/fcn.14002b290.c)
- [`code/fcn.14002d120.c`](code/fcn.14002d120.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

This final chunk of disassembly provides the "smoking gun" regarding how this binary operates as a launcher, while also confirming the high level of complexity within its internal environment.

The new data solidifies the conclusion that this is a **highly professional, bundled Python runtime** (consistent with tools like PyInstaller or Nuitka), but it also reveals specific techniques used to manage and hide the execution process from the end-user.

---

### 1. New Key Findings (from Chunk 3/3)

#### A. Evidence of a "Hidden Window" Execution Model
The function `fcn.140009430` contains very specific Windows API calls that are hallmarks of "silent" execution:
*   **Windows Setup:** It uses `RegisterClassW`, `CreateWindowExW`, and `ShowWindow(..., 0)`. The inclusion of the string **"PyInstallerOnefileHiddenWindow"** in the window class name is a definitive indicator.
*   **Purpose:** This allows a Python script that normally requires a console to run in the background without popping up a command prompt window—a standard feature for GUI-based Python applications, but also a technique used by malware to hide its presence during execution.

#### B. Process Management and Handoff
In the same area (`fcn.140009430`), the binary uses `CreateProcessW` combined with `GetCommandLineW`. 
*   **Behavior:** The loader is designed to spawn a child process (the actual Python interpreter) while passing the original command-line arguments to it. It then enters a message loop (`PeekMessageW`, `DispatchMessageW`) to keep that "hidden" window alive so the script can continue running in the background.
*   **Significance:** This confirms the multi-stage nature of the loader; the file you are analyzing is the "wrapper," which sets up the environment and then hands off the heavy lifting to a second, internal process.

#### C. High-Performance Math & SIMD Optimization
The function `fcn.14002b290` contains complex logic involving **AVX (Advanced Vector Extensions)** instructions (`vfmadd`, `vpsrlq_avx`). 
*   **Analysis:** This is not "junk" code or standard obfuscation; it is highly optimized floating-point math.
*   **Context:** This suggests that the environment supports heavy computational tasks, potentially including libraries like **NumPy**, which require high-performance linear algebra and are commonly bundled into large Python applications (like 3D engines or data analysis tools).

#### D. Sophisticated Unicode/String Parsing
The functions `fcn.140015a80` and `fcn.140014adc` contain massive "switch-table" style logic to handle different character types.
*   **Analysis:** These are used to ensure the software can correctly interpret various international characters (Unicode/UTF-8). 
*   **Significance:** This confirms that the environment is built for production use, designed to work in multiple languages and locales without crashing on special characters.

---

### 2. Updated Risk Profile

The addition of these technical details provides a clearer picture of how this "container" functions:

*   **Stealth Capability (Standard but Notable):** The use of `ShowWindow(..., 0)` and the specific **"HiddenWindow"** strings indicate that the application is designed to run without showing a command prompt. While standard for professional GUI software, it is also the primary way "droppers" or "infostealers" hide their execution from the user's view.
*   **Self-Contained Complexity:** The presence of SIMD/AVX math and extensive Unicode handling suggests that this is not a simple script; it is part of a **heavy, professional-grade application**.
*   **Multi-Process Architecture:** Because it spawns a second process to run the actual Python logic, identifying "malicious" behavior solely in the first binary can be difficult. The initial loader prepares the ground (the "environment"), and the second process executes the payload.

---

### 3. Final Summary Table (Consolidated)

| Feature | Technical Observation | Inference / Context |
| :--- | :--- | :--- |
| **Core Purpose** | PyInstaller/Python Bootloader | A wrapper designed to execute a Python script by bundling all dependencies into one executable. |
| **Tcl/Tk Support** | `Tcl_Init`, `Tcl_EvalEx` | The environment supports GUIs and complex internal scripting via the Tkinter library. |
| **Hide-Window Logic** | `CreateWindowExW` & "PyInstallerOne1fileHiddenWindow" | Ensures that the Python process runs in the background without a command prompt window popping up. |
| **Process Management**| `CreateProcessW` + `GetCommandLineW` | The loader sets up an environment and launches a separate child process to run the actual script. |
| **High Performance** | AVX/SIMD math instructions (`vfmadd`) | Supports heavy computational libraries (like NumPy) or advanced graphics processing. |
| **Robustness** | Massive Unicode dispatch tables | High-quality, multi-language support for international characters and memory safety. |
| **Status** | **No inherent malice detected.** | This is a highly complex, standard "heavy" launcher. Malicious intent would be found in the *inner* script/payload, not this loader. |

---

### Final Analytical Conclusion
The binary is a **sophisticated multi-stage bootloader**. It is designed to create an extensive environment that supports:
1.  **Graphical Interfaces** (via Tcl/Tk)
2.  **Heavy Computation** (via AVX optimized math)
3.  **Internationalization** (via robust Unicode handling)
4.  **Stealth Execution** (by spawning a hidden child process to run the core logic).

**Security Recommendation:** 
Because this loader is designed to be "heavy" and "hidden," it provides an ideal vehicle for complex software (like games or tools) but can also be used by attackers to hide malicious activity. **The most effective way to determine intent is to inspect what is being loaded into the second process.** If you run this in a sandbox, monitor:
1.  **File System:** Look for hidden files/folders created in `%TEMP%` or `%APPDATA%`.
2.  **Network:** Watch for any connections made immediately after the "Hidden Window" process is spawned.
3.  **Processes:** Check if it spawns `python.exe` or another binary that performs unexpected network tasks.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059.004** | Command and Scripting Interpreter: Python | The analysis confirms a bundled Python runtime (PyInstaller/Nuitka) used to execute script logic within the application. |
| **T1218** | System Binary Proxy Execution | The use of a "loader" wrapper that spawns a child process (the Python interpreter) to perform the primary execution can be used to mask activity behind a common runtime. |
| **T1036** | Hide Window* | *Note: While not a specific sub-technique in MITRE, the use of `ShowWindow(..., 0)` and "PyInstallerOnefileHiddenWindow" is specifically utilized to hide execution from the user.* |

***Note for the analyst:** In standard MITRE ATT&CK mapping, if you are strictly limited to official IDs where a specific "Hide Window" ID does not exist in the current framework, T1059.004 remains the primary identification for the behavior described.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contains largely obfuscated data or internal assembly artifacts (e.g., `L$ SUVWAV`) that do not resolve to standard network indicators like IP addresses or file paths. The behaviorals confirm a multi-stage execution model common in PyInstaller/Nuitka environments.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The analysis mentions standard Windows API calls like `GetCommandLineW`, but no specific malicious paths were provided.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA-1, or SHA-256 hashes were present in the strings.)

### **Other artifacts**
*   **Specific String:** `PyInstallerOnefileHiddenWindow` 
    *   *Context:* This is a window class name used by the PyInstaller bootloader. While not a network IOC, it serves as a signature that the binary is a bundled Python environment (likely using PyInstaller) and is designed to hide its console window from the user.
*   **Behavioral Signature:** **Multi-stage Execution.** 
    *   *Context:* The use of `CreateProcessW` + `GetCommandLineW` combined with a "Hidden Window" indicates a loader/wrapper architecture. This is often used in both legitimate software and malware to separate the launcher from the actual payload logic.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family:** custom
2. **Malware type:** loader
3. **Confidence:** High
4. **Key evidence:**
    *   **Standard Python Wrapper:** The presence of the string `PyInstallerOnefileHiddenWindow`, Tcl/Tk support, and extensive Unicode handling confirms this is a standard PyInstaller (or similar) bootloader designed to wrap Python scripts into a single executable.
    *   **Multi-Stage Execution Architecture:** The use of `CreateProcessW` combined with `GetCommandLineW` and `ShowWindow(..., 0)` indicates its primary function is to "wrap" and launch a second, hidden process (the actual script), which is the hallmark of a loader.
    *   **Lack of Direct Malicious Payload:** The analysis concludes that no inherent malicious behavior was detected within this specific binary; it serves as a sophisticated environment container. Evidence of malicious intent would only be present in the subsequent script executed by the second process.
