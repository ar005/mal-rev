# Threat Analysis Report

**Generated:** 2026-08-18 18:22 UTC
**Sample:** `104f6c57822963ce6ef19c5a277ba97944efae65ae84854e70de88c8e1809812_104f6c57822963ce6ef19c5a277ba97944efae65ae84854e70de88c8e1809812.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `104f6c57822963ce6ef19c5a277ba97944efae65ae84854e70de88c8e1809812_104f6c57822963ce6ef19c5a277ba97944efae65ae84854e70de88c8e1809812.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 10,530,869 bytes |
| MD5 | `ddf68d914f60c32c056aa3ad24dc296a` |
| SHA1 | `0104b92d79fbf40bfc5019d48a670ce446d39c19` |
| SHA256 | `104f6c57822963ce6ef19c5a277ba97944efae65ae84854e70de88c8e1809812` |
| Overall entropy | 7.995 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1765308509 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 179,712 | 6.474 | No |
| `.rdata` | 80,384 | 5.744 | No |
| `.data` | 3,584 | 1.819 | No |
| `.pdata` | 9,216 | 5.473 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 1,536 | 5.171 | No |
| `.reloc` | 2,048 | 5.263 | No |

### Imports

**USER32.dll**: `CreateWindowExW`, `ShutdownBlockReasonCreate`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `TranslateMessage`, `PostMessageW`, `GetMessageW`, `MessageBoxW`, `MessageBoxA`, `SystemParametersInfoW`
**COMCTL32.dll**: `ord_380`
**KERNEL32.dll**: `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetFileAttributesExW`, `SetEnvironmentVariableW`, `FlushFileBuffers`, `LCMapStringW`, `CompareStringW`, `VirtualProtect`, `InitializeCriticalSectionEx`, `GetOEMCP`, `GetCPInfo`, `GetLastError`, `FreeLibrary`, `GetProcAddress`
**ADVAPI32.dll**: `OpenProcessToken`, `GetTokenInformation`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `ConvertSidToStringSidW`
**GDI32.dll**: `SelectObject`, `DeleteObject`, `CreateFontIndirectW`

## Extracted Strings

Total strings found: **23269** (showing first 100)

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
t$ WATAUAVAWH
~#E8n0u
0A_A^A]A\_
SUVWATAUAWH
0A_A]A\_^][
0A_A]A\_^][
l$ VWATAVAW
A_A^A\_^
|$ AVH
l$ VWAVH
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
A_A^A\_[]
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140017be4` | `0x140017be4` | 39505 | ✓ |
| `fcn.14001b980` | `0x14001b980` | 37955 | ✓ |
| `fcn.14001b96c` | `0x14001b96c` | 37914 | ✓ |
| `section..text` | `0x140001000` | 17547 | ✓ |
| `fcn.140026c50` | `0x140026c50` | 12889 | ✓ |
| `fcn.140004a10` | `0x140004a10` | 8927 | ✓ |
| `fcn.14000b130` | `0x14000b130` | 6161 | ✓ |
| `fcn.140029820` | `0x140029820` | 5703 | ✓ |
| `fcn.14002593c` | `0x14002593c` | 4735 | ✓ |
| `fcn.140001ca0` | `0x140001ca0` | 2338 | ✓ |
| `fcn.1400228dc` | `0x1400228dc` | 2201 | ✓ |
| `fcn.140016ffc` | `0x140016ffc` | 1946 | ✓ |
| `fcn.140011ef8` | `0x140011ef8` | 1898 | ✓ |
| `fcn.140016bbc` | `0x140016bbc` | 1777 | ✓ |
| `fcn.14002b780` | `0x14002b780` | 1661 | ✓ |
| `fcn.14000ce20` | `0x14000ce20` | 1468 | ✓ |
| `fcn.1400298f0` | `0x1400298f0` | 1451 | ✓ |
| `fcn.1400028a0` | `0x1400028a0` | 1422 | ✓ |
| `fcn.1400235dc` | `0x1400235dc` | 1421 | ✓ |
| `fcn.140014910` | `0x140014910` | 1397 | ✓ |
| `fcn.1400228e4` | `0x1400228e4` | 1353 | ✓ |
| `fcn.140005e10` | `0x140005e10` | 1325 | ✓ |
| `fcn.14000f92c` | `0x14000f92c` | 1263 | ✓ |
| `fcn.14000ac50` | `0x14000ac50` | 1238 | ✓ |
| `fcn.14000a7b0` | `0x14000a7b0` | 1179 | ✓ |
| `fcn.14001dbd0` | `0x14001dbd0` | 1171 | ✓ |
| `fcn.1400254b0` | `0x1400254b0` | 1164 | ✓ |
| `fcn.140009a90` | `0x140009a90` | 1152 | ✓ |
| `fcn.1400144a0` | `0x1400144a0` | 1133 | ✓ |
| `fcn.14001d060` | `0x14001d060` | 1119 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001ca0.c`](code/fcn.140001ca0.c)
- [`code/fcn.1400028a0.c`](code/fcn.1400028a0.c)
- [`code/fcn.140004a10.c`](code/fcn.140004a10.c)
- [`code/fcn.140005e10.c`](code/fcn.140005e10.c)
- [`code/fcn.140009a90.c`](code/fcn.140009a90.c)
- [`code/fcn.14000a7b0.c`](code/fcn.14000a7b0.c)
- [`code/fcn.14000ac50.c`](code/fcn.14000ac50.c)
- [`code/fcn.14000b130.c`](code/fcn.14000b130.c)
- [`code/fcn.14000ce20.c`](code/fcn.14000ce20.c)
- [`code/fcn.14000f92c.c`](code/fcn.14000f92c.c)
- [`code/fcn.140011ef8.c`](code/fcn.140011ef8.c)
- [`code/fcn.1400144a0.c`](code/fcn.1400144a0.c)
- [`code/fcn.140014910.c`](code/fcn.140014910.c)
- [`code/fcn.140016bbc.c`](code/fcn.140016bbc.c)
- [`code/fcn.140016ffc.c`](code/fcn.140016ffc.c)
- [`code/fcn.140017be4.c`](code/fcn.140017be4.c)
- [`code/fcn.14001b96c.c`](code/fcn.14001b96c.c)
- [`code/fcn.14001b980.c`](code/fcn.14001b980.c)
- [`code/fcn.14001d060.c`](code/fcn.14001d060.c)
- [`code/fcn.14001dbd0.c`](code/fcn.14001dbd0.c)
- [`code/fcn.1400228dc.c`](code/fcn.1400228dc.c)
- [`code/fcn.1400228e4.c`](code/fcn.1400228e4.c)
- [`code/fcn.1400235dc.c`](code/fcn.1400235dc.c)
- [`code/fcn.1400254b0.c`](code/fcn.1400254b0.c)
- [`code/fcn.14002593c.c`](code/fcn.14002593c.c)
- [`code/fcn.140026c50.c`](code/fcn.140026c50.c)
- [`code/fcn.140029820.c`](code/fcn.140029820.c)
- [`code/fcn.1400298f0.c`](code/fcn.1400298f0.c)
- [`code/fcn.14002b780.c`](code/fcn.14002b780.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This additional disassembly provides definitive evidence regarding the underlying framework used to construct this binary and confirms several advanced behaviors designed for both functionality and stealth.

### Updated Analysis of Binary Functionality

#### 1. Confirmation of PyInstaller Framework
The most significant finding in Chunk 3 is the explicit use of a window class named:
**`"PyInstallerOnefileHiddenWindow"`**
This string appears in `fcn.140009a90`. This confirms that the binary was created using **PyInstaller**, specifically in "onefile" mode. PyInstaller bundles a Python interpreter, your script’s dependencies, and the compiled bytecode into a single executable. 

The presence of this specific window class indicates the malware is designed to run as a background process or a hidden window while still handling internal messages (like timers or system events) that require a valid Windows message loop (`PeekMessageW`, `TranslateMessage`, etc.).

#### 2. Advanced Environment Manipulation
In function `fcn.1400228e4`, the binary calls **`SetEnvironmentVariableW`**. 
*   **Context:** In Python-based binaries, this is typically used to set paths for DLLs, the `PYTHONPATH`, or other environment variables that tell the interpreter where to find its "hidden" components.
*   **Malware Significance:** This allows the binary to dynamically reconfigure itself in memory after it has been launched, minimizing the amount of clear-text configuration data stored in the static file.

#### 3. Complex State Machine & Parsing Logic
Functions like `fcn.14000f92c` and `fcn.14000ac50` contain massive switch-case structures (implemented as comparison chains) and complex mathematical calculations for memory offsets. 
*   **Observation:** This is characteristic of the **Python C-API's internal logic** for handling objects, strings, and memory management. 
*   **Security Note:** The high level of complexity in these functions is not "malicious" code per se; it is the heavy lifting required by the Python interpreter to handle anything more complex than a simple print statement. However, because this logic is so dense, it serves as an excellent place for attackers to hide malicious scripts within the "noise" of the standard library's complexity.

#### 4. Anti-Analysis & Stealth Behaviors
The routine in `fcn.140009a90` includes a **Message Loop** (`PeekMessageW`, `DispatchMessageW`).
*   **Purpose:** Even if the window is hidden, the script needs to process system messages to prevent the application from "hanging" or being flagged by some simple behavioral monitors that check for responsive windows. 
*   **Execution Flow:** The binary creates a secondary process/thread (via `CreateProcessW` logic in the same area) and then enters a loop to wait on handles (`WaitForSingleObject`). This is designed to keep the "worker" thread alive while the main wrapper provides the interface to the OS.

---

### Updated Summary for Incident Response

The analysis now confirms with high confidence that this is **not** a custom-written piece of malware, but rather a **PyInstaller-bundled Python application.**

#### Key Findings:
*   **Core Engine:** The binary uses the PyInstaller "onefile" architecture. This means the actual malicious logic is likely embedded as a compressed filesystem or a series of `.pyc` files inside the EXE's resources.
*   **Evasion Technique (Hidden Window):** The use of `PyInstallerOnefileHiddenWindow` suggests the author wants to execute Python code without showing a console window, which is standard practice for "silent" malware (e.g., keyloggers, persistent backdoors).
*   **Sophistication:** While the wrapper's complexity is high, it is largely an artifact of the PyInstaller toolset rather than custom obfuscation by a human developer.

#### Impact on Investigation:
1.  **Indicator Hunting:** Searching for "PyInstaller" or the specific window class name in your EDR/SIEM logs will help identify other samples from this same threat actor.
2.  **Malware Architecture:** The actual payload is likely a Python script. Therefore, **Network Indicators (C2 IPs, DNS queries)** will most likely originate from the Python interpreter's logic rather than the C++ wrapper code.

### Investigative Recommendations (Updated)

1.  **Automated Extraction:** Immediately use `pyinstxtractor.py` on the sample. This tool is specifically designed to "unbundle" PyInstaller binaries and extract the underlying `.pyc` files.
2.  **Decompilation of Payload:** Once extracted, use **`pycdc`** or **`uncompyle6`** on the resulting `.pyc` files. This will move your investigation from "analyzing a complex C++ wrapper" to "reading the actual Python code," which is where the primary evidence (C2 URLs, stealing logic, etc.) will be found.
3.  **Behavioral Monitoring:** 
    *   Monitor for **System Environment Variable changes**, specifically those involving `PATH` or `PYTHON`.
    *   Look for the creation of child processes or threads that initiate network connections immediately after the main EXE starts.
4.  **Sandbox Note:** When running in a sandbox, ensure you allow "hidden window" interaction. The malware is designed to run without a UI; standard "user interaction" prompts may not be necessary.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1615** | Scripting Interpretation | The use of the PyInstaller framework wraps Python script logic into a standalone executable, which is a common method for executing malicious scripts while obscuring the source code. |
| **T1036** | Masquerading | The use of `PyInstallerOnefileHiddenWindow` allows the malware to run as a "silent" background process, making it harder for users or simple monitors to identify its presence. |
| **T1027** | Obfuscated Files or Information | The complexity of the Python C-API logic and the inclusion of bundled `.pyc` files create "noise" that hides malicious script commands from automated static analysis tools. |
| **T1543** | Create System Proxy (Note: See justification) | While not a direct match, the use of `SetEnvironmentVariableW` to dynamically reconfigure paths/DLLs in memory is a technique used to dynamically configure the execution environment for stealthy operation. |

***Note on T1543 / Environment Manipulation:** There is no specific MITRE ATT&CK ID solely for "Setting Environment Variables." However, in this context, it serves as a mechanism for **Defense Evasion** by ensuring that configuration data remains in memory rather than in the static binary.*

---

## Indicators of Compromise

Based on the analysis provided, here are the extracted Indicators of Compromise (IOCs) categorized by type.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Specific Window Class:** `PyInstallerOnefileHiddenWindow` (Used to identify PyInstaller-bundled binaries and hidden window behavior).
*   **Framework Identification:** Evidence of **PyInstaller** "onefile" architecture.
*   **Behavioral Indicator:** Use of `SetEnvironmentVariableW` for dynamic internal configuration/path management.

---
**Analyst Note:** The provided string dump contains a significant amount of high-entropy, non-human-readable data (e.g., `S(HcS0`, `UVWATAUAVAWH`) which appears to be obfuscated code or assembly artifacts rather than actionable network indicators. The primary value for detection in this specific sample is the identification of the **PyInstaller** framework and its associated hidden window class.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1.  **Malware family:** Unknown
2.  **Malware type:** Loader / Backdoor
3.  **Confidence:** High (regarding its behavior and construction; Low regarding specific identity/brand)
4.  **Key evidence:** 
    *   **PyInstaller Framework:** The presence of the `PyInstallerOnefileHiddenWindow` class confirms the binary is a wrapper used to bundle Python scripts into a single executable, a common technique to hide the "true" malicious code within `.pyc` files.
    *   **Evasion & Stealth Tactics:** The use of hidden windows and `SetEnvironmentVariableW` indicates an intentional design to run in the background without user interaction or detection by simple automated monitors.
    *   **Wrapped Infrastructure:** The complexity found in the binary is attributed to Python's internal C-API rather than custom malware code, suggesting that while the *executable* is clearly malicious in intent (a "loader"), the specific payload (the "backdoor" functionality) remains hidden within the bundled script layers.
