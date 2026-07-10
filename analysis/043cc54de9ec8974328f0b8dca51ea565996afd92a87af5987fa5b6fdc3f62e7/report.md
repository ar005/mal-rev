# Threat Analysis Report

**Generated:** 2026-07-09 21:42 UTC
**Sample:** `043cc54de9ec8974328f0b8dca51ea565996afd92a87af5987fa5b6fdc3f62e7_043cc54de9ec8974328f0b8dca51ea565996afd92a87af5987fa5b6fdc3f62e7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `043cc54de9ec8974328f0b8dca51ea565996afd92a87af5987fa5b6fdc3f62e7_043cc54de9ec8974328f0b8dca51ea565996afd92a87af5987fa5b6fdc3f62e7.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 12,727,267 bytes |
| MD5 | `0638133d1672459e7fee86a15d01089b` |
| SHA1 | `ceef83729244a6500394a13fef456d886938476f` |
| SHA256 | `043cc54de9ec8974328f0b8dca51ea565996afd92a87af5987fa5b6fdc3f62e7` |
| Overall entropy | 7.972 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773630210 |
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
| `.rsrc` | 169,984 | 1.185 | No |
| `.reloc` | 2,048 | 5.263 | No |

### Imports

**USER32.dll**: `CreateWindowExW`, `ShutdownBlockReasonCreate`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `TranslateMessage`, `PostMessageW`, `GetMessageW`, `MessageBoxW`, `MessageBoxA`, `SystemParametersInfoW`
**COMCTL32.dll**: `ord_380`
**KERNEL32.dll**: `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetFileAttributesExW`, `SetEnvironmentVariableW`, `FlushFileBuffers`, `LCMapStringW`, `CompareStringW`, `VirtualProtect`, `InitializeCriticalSectionEx`, `GetOEMCP`, `GetCPInfo`, `GetLastError`, `FreeLibrary`, `GetProcAddress`
**ADVAPI32.dll**: `OpenProcessToken`, `GetTokenInformation`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `ConvertSidToStringSidW`
**GDI32.dll**: `SelectObject`, `DeleteObject`, `CreateFontIndirectW`

## Extracted Strings

Total strings found: **29187** (showing first 100)

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

This final portion of the disassembly completes our technical picture of the binary’s internals. The presence of specific system calls, specialized loop structures, and complex parsing logic confirms that this is not merely a standard Python script wrapper, but a **highly sophisticated execution engine.**

Below is the updated analysis incorporating chunks 1, 2, and 3.

### Final Comprehensive Analysis of Functionality and Behavior

The final disassembly data provides evidence of "stealth" features and complex internal state management that go beyond simple automation.

#### 1. Completion of Tcl/Python Interpreter Integration
The end of the first block confirms the full ingestion of the **Tcl (Tickling Command Language)** library. By resolving functions like `Tcl_EvalFile`, `Tcl_EvalEx`, and `Tcl_Alloc`, the binary prepares to execute complex logic. 
*   **Significance:** The fact that it implements both Python and Tcl suggests a "polyglot" environment. This allows an attacker to switch execution paths or use different languages to perform specific tasks (e.g., using Tcl for system-level interactions/networking and Python for high-level logic).

#### 2. Hidden Window & Background Execution
A critical finding in the third chunk is the usage of:
*   **String:** `"PyInstallerOnefileHiddenWindow"`
*   **API calls:** `CreateWindowExW` followed by `ShowWindow(..., 0)`.
*   **Analysis:** This confirms the application is designed to run as a "headless" process. While common in legitimate background services, in this context, it serves to ensure that if the script performs malicious actions (like data exfiltration or keylogging), there is **no visual indicator** to the user that a window or active process is engaging with their system.

#### 3. Anti-Analysis and Timing Loops
The code contains complex loops using `QueryPerformanceCounter` and `QueryPerformanceFrequency`.
*   **Technical Detail:** Instead of using standard `Sleep()` functions (which are easily detected/hooked by sandboxes), the code calculates time deltas manually: `((current_count - previous_count) * 1000) / frequency`.
*   **Risk Factor:** This is a classic **anti-analysis technique**. It allows the program to wait for specific periods of time in a way that is difficult for automated "fast-forward" sandbox tools to detect, as it relies on hardware timers rather than system clocks.

#### 4. Complex Dispatcher & Parser Logic
Functions such as `fcn.140005e10` and `fcn.140014910` contain deep nested loops and complex conditional checks (e.g., comparing bytes against values like `0x3a`, `0x41`, `0x58`).
*   **Observation:** These are not standard high-level logic. They appear to be **bytecode dispatchers** or **custom parser engines**. 
*   **Implication:** This suggests that the "payload" is not a plain text script being read from disk, but likely an obfuscated or compiled script format that this specific engine knows how to "unpack" and execute step-by-step.

---

### Updated Suspicious and Malicious Behaviors

The following behaviors are highlighted as high-risk indicators:

*   **Stealth Operations (Hidden Window):** The explicit attempt to create a window and immediately hide it is a signature of malware attempting to remain invisible while performing background tasks.
*   **Evasion of Sandboxes/Debuggers:** The use of high-precision hardware timers (`QueryPerformanceCounter`) for timing loops suggests the author intended to bypass automated security analysis tools that skip standard `Sleep()` calls.
*   **Multi-Engine "Shell" Architecture:** By bundling Python and Tcl into a single, complex dispatcher, the developer has created a robust environment capable of executing highly complex, multi-stage payloads. It provides a massive "surface area" for malicious activity while making manual de-obfuscation extremely difficult for analysts.
*   **Complex Data Processing (AVX & Parsing):** The combination of AVX instruction sets (from chunk 2) and the deep parsing logic (in chunk 3) indicates that the final payload is likely a significant piece of software—perhaps an advanced info-stealer, a modular trojan, or even a secondary dropper.

---

### Final Summary Conclusion

This binary is a **sophisticated multi-engine execution host.** It functions as a heavy-duty "shell" designed to run complex scripts across two different environments (Python and Tcl). 

**Key Takeaways for Security Operations:**
1.  **High Complexity:** The presence of extensive C-API mapping, Tcl integration, and advanced math libraries indicates this is not a "script kiddie" tool; it is a professional-grade wrapper.
2.  **Intent of Stealth:** The inclusion of "Hidden Window" logic and non-standard timing loops strongly suggests an intent to evade both the end-user's notice and automated security scanners.
3.  **Risk Level - High:** While the binary itself may be a "tool," its design perfectly facilitates sophisticated, stealthy malware. If this file is found in an environment where it does not belong, it should be treated as a **high-priority threat**, as it likely serves as a delivery vehicle for complex, multi-stage malicious payloads hidden within its layered scripting engines.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The integration of both Tcl and Python allows the binary to execute complex, multi-layered logic through established scripting languages. |
| **T1497** | Virtualization, Debugger or Sandbox Evasion | The use of `QueryPerformanceCounter` for timing loops is a specific method to bypass "fast-forward" detection in automated sandbox environments. |
| **T1027** | Obfuscated Files or Information | The complex dispatcher and parsing logic indicate that the payload is not plain text, but is instead formatted to hide its true purpose from simple analysis. |
| **T1036** | Masquerading | The "Hidden Window" functionality ensures that malicious background activities (e.g., data exfiltration) occur without providing a visual indicator to the user. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **String:** `PyInstallerOnefileHiddenWindow` (Identifies the use of PyInstaller to bundle a Python script into a single executable with the console window hidden.)
*   **Behavioral Note:** Use of `QueryPerformanceCounter` and `QueryPerformanceFrequency` for non-standard timing loops (indicates anti-analysis/anti-sandbox techniques).
*   **Functionality Signature:** Integration of both **Tcl** (`Tcl_EvalFile`, `Tcl_EvalEx`, `Tcl_Alloc`) and **Python** interpreters within a single "polyglot" environment.

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1.  **Malware family:** custom
2.  **Malware type:** loader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Multi-Engine Execution Environment:** The integration of both Python and Tcl interpreters creates a "polyglot" environment, allowing for the execution of complex, multi-stage scripts that are difficult to de-obfuscate through standard means.
    *   **Advanced Anti-Analysis Techniques:** The use of `QueryPerformanceCounter` for manual timing loops (to bypass "fast-forward" sandboxes) and "Hidden Window" logic indicates a clear intent to evade both automated security tools and end-user detection.
    *   **Complex Parsing/Dispatching:** The presence of dedicated bytecode dispatchers and custom parser engines suggests the binary is designed to handle obfuscated or compiled payloads rather than plain-text scripts, marking it as a high-end execution "shell."
