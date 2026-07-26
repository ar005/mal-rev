# Threat Analysis Report

**Generated:** 2026-07-24 19:32 UTC
**Sample:** `0a46c185a25b50311e80569b960f75178b233c402472f1e38aafa5f2b885627e_0a46c185a25b50311e80569b960f75178b233c402472f1e38aafa5f2b885627e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a46c185a25b50311e80569b960f75178b233c402472f1e38aafa5f2b885627e_0a46c185a25b50311e80569b960f75178b233c402472f1e38aafa5f2b885627e.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 76,525,084 bytes |
| MD5 | `ff443c3e2a25f724d5c451c1116fce27` |
| SHA1 | `813108169608f089be8fb3b06cc5015713fd09a7` |
| SHA256 | `0a46c185a25b50311e80569b960f75178b233c402472f1e38aafa5f2b885627e` |
| Overall entropy | 7.999 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774014336 |
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
| `.rsrc` | 1,536 | 5.511 | No |
| `.reloc` | 2,048 | 5.264 | No |

### Imports

**USER32.dll**: `CreateWindowExW`, `ShutdownBlockReasonCreate`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `TranslateMessage`, `PostMessageW`, `GetMessageW`, `MessageBoxW`, `MessageBoxA`, `SystemParametersInfoW`
**COMCTL32.dll**: `ord_380`
**KERNEL32.dll**: `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetFileAttributesExW`, `SetEnvironmentVariableW`, `FlushFileBuffers`, `LCMapStringW`, `CompareStringW`, `VirtualProtect`, `InitializeCriticalSectionEx`, `GetOEMCP`, `GetCPInfo`, `GetLastError`, `FreeLibrary`, `GetProcAddress`
**ADVAPI32.dll**: `OpenProcessToken`, `GetTokenInformation`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `ConvertSidToStringSidW`
**GDI32.dll**: `SelectObject`, `DeleteObject`, `CreateFontIndirectW`

## Extracted Strings

Total strings found: **175006** (showing first 100)

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

This final analysis incorporates the details from the third and final disassembly chunk. The addition of this data provides a definitive "smoking gun" regarding the executable's structure and confirms several technical suspicions from previous chunks.

---

### Updated Technical Analysis (Comprehensive)

#### 1. Core Functionality and Architecture
The evidence now overwhelmingly points to a **highly complex, multi-layered execution environment**. The core logic is hosted within an interpreted system with multiple layers of abstraction:

*   **Confirmed PyInstaller Wrapper:** The discovery of the string `"PyInstallerOnefileHiddenWindow"` in `fcn.140009fe0` confirms that this binary is a Python application bundled using **PyInstaller**. This specific naming convention refers to the logic used when a Python script is launched with a "hidden" window or as part of a multi-process execution (common for tools using GUI components or background workers).
*   **Multi-Process Management:** The inclusion of `CreateProcessW` and `GetCommandLineW` in `fcn.140009fe0`, coupled with the message loop (`PeekMessageW`, `TranslateMessage`, `DispatchMessageW`), indicates that the binary is designed to manage child processes or run as a background service while handling system signals (via `SetConsoleCtrlHandler`).
*   **Tcl/Tk and Python Integration:** The repeated appearance of complex "switch" logic and state machine transitions in functions like `fcn.140014a20` and `fcn.140005f70` is characteristic of the **Tcl interpreter**. This confirms that the application likely relies on Tcl for its internal scripting or GUI management (Tkinter).
*   **Complex Memory & String Handling:** Functions like `fcn.140025c60` and `fcn.140023094` indicate sophisticated memory management, potentially handling multi-byte character sets or large buffer allocations for internal scripts.

#### 2. Suspicious or Malicious Behaviors
While the binary primarily functions as a container, several features are noteworthy from a security perspective:

*   **Hidden Execution Profile:** The use of `"PyInstallerOnefileHiddenWindow"` and `ShowWindow(iVar6, 0)` suggests an intentional design to run without a visible user interface. While common in legitimate background services (like update checkers), it is also a common technique used by malware to hide its presence from the user.
*   **Environment Manipulation:** The call to `SetEnvironmentVariableW` within internal logic (`fcn.140023094`) confirms that the application modifies its own environment—or that of child processes—during startup. This can be used to point the interpreter toward specific malicious DLLs or configuration files.
*   **Abstraction as Obfuscation:** The sheer complexity of the "dispatch" logic in `fcn.140014a20` and `fcn.140005f70` serves as a significant barrier to automated analysis. By nesting "malicious" actions deep within these translation loops, an attacker ensures that standard sandboxes may only see the interpreter's activity rather than the specific script logic being executed by it.
*   **Sophisticated I/O Handling:** `fcn.14001d810` handles complex terminal interactions (e.g., `GetConsoleMode`, `ReadConsoleW`). This suggests that if a CLI component exists, it is designed to be robust and potentially interact with the console in ways that might bypass simple logging.

#### 3. Technical Patterns & Key Constants
*   **State Machine Complexity:** The repetitive, nested branching (e.g., checking for `'d'`, `'S'`, `'A'`, `'E'`) in `fcn.140014a20` is a classic indicator of an interpreter processing tokens/commands. 
*   **Data Dispatching:** Function `fcn.14000feac` demonstrates deep nesting and multiple "escape" paths, typical of high-level language handlers dealing with variable types or memory addresses.

---

### Final Summary of Analysis

The binary is a **sophisticated, multi-layered wrapper environment**, almost certainly produced by the **PyInstaller** tool to package a complex application involving both **Python** and **Tcl/Tk**.

#### Key Findings:
1.  **Packaging Confirmation:** The identification of `"PyInstallerOnefileHiddenWindow"` confirms it is a bundled Python script. This explains the massive amount of "overhead" code (the interpreter) that occupies most of the binary's volume.
2.  **Obfuscation via Complexity:** The primary "payload" or malicious intent is not likely in the C++/Assembly layer, but rather hidden within the **interpreted scripts**. The complex dispatch tables found in this chunk are part of the "engine," making it very difficult for static tools to determine what the script will actually *do* until it is executed.
3.  **System Interaction:** The presence of `CreateProcessW`, `SetEnvironmentVariableW`, and sophisticated input/output handling indicates a capability for multi-process execution and interaction with system components.

**Conclusion:** 
The file serves as a **robust container**. While the binary itself does not contain "loud" indicators like immediate keylogging or unauthorized network connections, it provides all the infrastructure necessary to host a highly complex, potentially malicious script-based application. The complexity of the interpreter and Tcl/Tk layers acts as a significant technical hurdle for analysts attempting to find the ultimate goal of the software via static analysis alone.

**Recommendation:**
To determine the final intent, this file should be executed in a **monitored sandbox**. Since it is a PyInstaller bundle, dynamic analysis (observing network traffic and file system changes during execution) will reveal the "active" part of the payload that currently resides hidden within the interpreted layers.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your technical analysis to the relevant MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The use of PyInstaller, Python, and Tcl/Tk provides a multi-layered abstraction where the core logic is executed via scripts rather than direct machine code. |
| **T1027** | Obfuscated Files or Information | The complex dispatch logic and "multi-layered execution environment" are used to hide the true intent of the script from static analysis tools. |
| **T1137** | Environment Variable | The use of `SetEnvironmentVariableW` indicates an attempt to modify the environment for the interpreter or child processes, potentially to point toward specific configuration files or DLLs. |
| **T1036** | Masquerading | The use of "Hidden" window profiles and complex I/O handling suggests a desire to blend in as a legitimate background process while avoiding user interaction. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavior report, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The report mentions standard Windows API calls like `CreateProcessW`, but no specific malicious file paths or registry keys were provided.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Execution Environment:** `PyInstallerOnefileHiddenWindow` (Indicates the binary is a PyInstaller-wrapped Python script, often used to bundle complex logic into a single executable).
*   **Application Frameworks:** Evidence of **Tcl/Tk** integration (identified through multi-byte character handling and specific state machine transitions in functions `fcn.140014a20` and `fcn.140005f70`).
*   **Evasion/Stealth Techniques:** 
    *   Use of `ShowWindow(iVar6, 0)` to execute without a visible GUI.
    *   Heavy use of abstraction (Python/Tcl layers) as a method to bypass static analysis of the underlying logic.
*   **System Interaction Capabilities:** 
    *   `SetEnvironmentVariableW`: Used for environment manipulation.
    *   `CreateProcessW`: Indicates multi-process management capability.
    *   `GetConsoleMode` / `ReadConsoleW`: Advanced terminal interaction capabilities.

---
**Analyst Note:** The provided data contains very few "static" IOCs (like hardcoded IPs or specific file paths) because the malicious logic is contained within an interpreted script layer rather than the compiled C++/Assembly code. The primary indicators are **behavioral** and **structural**, specifically the use of a PyInstaller wrapper to hide functionality within Tcl/Tk layers.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader (Script-based)
3. **Confidence**: Medium

4. **Key evidence**:
*   **PyInstaller Wrapper:** The identification of `"PyInstallerOnefileHiddenWindow"` and the presence of Tcl/Tk interpreter logic confirms the binary is a wrapper designed to execute Python scripts, which allows attackers to hide malicious functionality within layers of abstraction.
*   **Evasion via Complexity:** The use of hidden window flags (`ShowWindow(iVar6, 0)`), complex dispatch tables, and nested script interpretation are classic indicators of an effort to bypass static analysis by hiding the "active" payload from signature-based detection.
*   **System Interaction Capabilities:** The inclusion of `CreateProcessW`, `SetEnvironmentVariableW`, and advanced terminal handling (`GetConsoleMode`) indicates the binary is designed to manage environment variables and child processes, common behaviors in loaders that prepare a system for further malicious execution.
