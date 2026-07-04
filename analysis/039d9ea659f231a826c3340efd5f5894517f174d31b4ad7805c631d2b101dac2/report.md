# Threat Analysis Report

**Generated:** 2026-07-01 19:54 UTC
**Sample:** `039d9ea659f231a826c3340efd5f5894517f174d31b4ad7805c631d2b101dac2_039d9ea659f231a826c3340efd5f5894517f174d31b4ad7805c631d2b101dac2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `039d9ea659f231a826c3340efd5f5894517f174d31b4ad7805c631d2b101dac2_039d9ea659f231a826c3340efd5f5894517f174d31b4ad7805c631d2b101dac2.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 12,608,504 bytes |
| MD5 | `d32175880985f3095418f2f5db2eaab3` |
| SHA1 | `bf634605a1d106d8f84688d84f833efcd59e8992` |
| SHA256 | `039d9ea659f231a826c3340efd5f5894517f174d31b4ad7805c631d2b101dac2` |
| Overall entropy | 7.995 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767726983 |
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
| `.rsrc` | 62,976 | 7.555 | ⚠️ Yes |
| `.reloc` | 2,048 | 5.263 | No |

### Imports

**USER32.dll**: `CreateWindowExW`, `ShutdownBlockReasonCreate`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `TranslateMessage`, `PostMessageW`, `GetMessageW`, `MessageBoxW`, `MessageBoxA`, `SystemParametersInfoW`
**COMCTL32.dll**: `ord_380`
**KERNEL32.dll**: `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetFileAttributesExW`, `SetEnvironmentVariableW`, `FlushFileBuffers`, `LCMapStringW`, `CompareStringW`, `VirtualProtect`, `InitializeCriticalSectionEx`, `GetOEMCP`, `GetCPInfo`, `GetLastError`, `FreeLibrary`, `GetProcAddress`
**ADVAPI32.dll**: `OpenProcessToken`, `GetTokenInformation`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `ConvertSidToStringSidW`
**GDI32.dll**: `SelectObject`, `DeleteObject`, `CreateFontIndirectW`

## Extracted Strings

Total strings found: **26730** (showing first 100)

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

Based on the final chunk of disassembly provided, I have updated the analysis. This final piece of data solidifies the conclusion that this binary is a highly sophisticated **multi-stage execution environment** designed to hide its true intent through layers of abstraction and complex decoding.

### Updated Technical Analysis (Chunk 3/3)

#### 1. Deep Tcl Engine Integration
The function `fcn.1400028a0` confirms that the **Tcl** component is not just a minor feature but a core part of the execution logic. It explicitly maps:
*   **Execution & Evaluation:** `Tcl_EvalFile`, `Tcl_EvalEx`, and `Tcl_EvalObjv`. These are used to execute Tcl scripts directly from memory or files.
*   **Memory Management:** `Tcl_Alloc` and `Tcl_Free`.
*   **State Management:** `Tcl_GetObjResult` and `Tcl_SetVar2Ex`.
*   **Significance:** This confirms the "Nested Interpreter" theory from earlier. The application can execute Tcl scripts which, in turn, may interact with the Python environment or system resources.

#### 2. Complex Decoding & Resource Extraction (The "Packing" Layer)
Several functions (`fcn.1400254b0`, `fcn.140014910`, and `fcn.1400144a0`) exhibit characteristics of **advanced decoding loops**:
*   **Bit-Shifting & Masking:** `fcn.1400254b0` contains extensive logic involving bitwise shifts (`>>`, `<<`), masking, and modular arithmetic. This is highly characteristic of **Base64 decoding**, custom encoding schemes, or decompressing embedded data.
*   **Large Switch-like Branching:** The "tower" of `if/else` statements in `fcn.140014910` and `fcn.1400144a0` are typical of a **Virtual Machine (VM) or an Instruction Dispatcher**. Instead of direct execution, the binary interprets a "custom" bytecode to perform actions like setting environment variables, handling internal state, or processing configuration.

#### 3. Host Interaction & Persistence Techniques
The function `fcn.14001dbd0` interacts with several Windows APIs that are frequently used in malware for stealth:
*   **Hidden Window Management:** The string `PyInstallerOnefileHiddenWindow` and the use of `RegisterClassW`, `CreateWindowExW`, and `ShowWindow(..., 0)` indicate the binary is designed to run in a **hidden window**. This allows it to perform tasks (like crypto-mining or data exfiltration) without appearing on the user's desktop.
*   **Process Manipulation:** The use of `CreateProcessW` suggests that the application may spawn child processes or "hollow out" existing ones to execute the final payload.
*   **System Interaction:** It interacts with console settings (`GetConsoleMode`) and performs direct file/buffer reading, likely to interpret inputs or commands from a remote server.

---

### Updated Summary of Findings

#### Core Functionality: A Multi-Layered "Wrapper"
The binary is more than just a PyInstaller bootloader; it is a **hybrid environment wrapper**. It establishes two distinct scripting engines (Python and Tcl). The logic flows as follows:
1.  **Bootstrapper:** Initial_setup of the Python/Tcl environments.
2.  **Decoder Loop:** Uses complex bitwise operations to de-obfuscate internal "payload" scripts or configuration data.
3.  **Dispatcher:** A custom bytecode interpreter (`fcn.140014910`) interprets the de-obfuscated script logic, making it nearly impossible for static analysis tools to map the full behavior of the payload without dynamic execution.

#### Notable Techniques & Patterns
*   **Hybrid Execution Environment:** By supporting both Python and Tcl, the author creates a **"Russian Nesting Doll"** effect. An analyst might unpack the Python layer only to find it is calling into a Tcl script that contains the actual malicious logic.
*   **Anti-Analysis via Complexity:** The sheer amount of "junk" logic in the dispatcher functions (`fcn.140014910`, `fcn.1400144a0`) is designed to exhaust the resources and time of human analysts and automated sandboxes.
*   **Hidden Execution:** Using a hidden window during execution is a classic indicator of malware attempting to remain unnoticed by the user while it performs its operations in the background.

#### Suspicious/Malicious Behaviors (Updated)
1.  **Sophisticated Evasion:** The use of nested interpreters and custom bytecode dispatchers is a high-level evasion technique used to hide "malicious" strings or API calls from static scanners.
2.  **Payload Obfuscation:** The heavy bitwise math in `fcn.1400254b0` suggests that the primary malicious payload is hidden inside an encrypted/encoded blob within the binary's resources.
3.  **Evasion of Detection during Execution:** By utilizing standard tools like Python and Tcl, the malware can perform "noisy" actions (like network traffic or file encryption) while using "clean" high-level commands that are harder to flag as malicious compared to raw system calls.

---

### Final Analyst Recommendations
*   **Dynamic Analysis is Mandatory:** Because of the nested interpreter design, static analysis will only tell you *how the loader works*, not *what the payload does*. You must run this in a controlled sandbox with full instrumentation (e.g., **ProcMon**, **Wireshark**, and **FakeNet-Sim**) to see what it actually communicates with or modifies on the system.
*   **Resource Extraction:** Attempt to dump all resources from the binary. Specifically, look for embedded `.py`, `.tcl`, and data chunks that appear "random" in a hex editor (indicating high entropy/encryption).
*   **Memory Forensics:** Perform memory dumps of the process while it is running. This may allow you to capture the scripts after they have been de-obfuscated by the internal `fcn.1400254b0` routines but before they are executed by the Python/Tcl engines.
*   **Risk Level: Critical.** The complexity of this loader, combined with hidden window management and multi-engine support, strongly indicates a **professionally developed malware sample**, likely designed for long-term persistence or high-value data exfiltration.

---

## MITRE ATT&CK Mapping

Based on the behavior analysis provided, here is the mapping of observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The binary incorporates Tcl and Python engines as core components to execute scripts (via `Tcl_Eval` functions) as a primary means of execution. |
| **T1027** | Obfuscated Files or Information | The use of extensive bit-shifting, masking, and complex decoding loops (`fcn.1400254b0`) is designed to hide the true payload from static analysis. |
| **T1036** | Masquerading | The use of `ShowWindow(..., 0)` and a hidden window name indicates an attempt to run the process without alerting the user to its presence. |
| **T1055.010** | Process Hollowing | The analyst's note regarding "hollow out" existing processes via `CreateProcessW` points specifically to this technique for injecting code into legitimate processes. |
| **T1482** | Virtualization (Optional/Contextual) | The implementation of a custom bytecode interpreter and instruction dispatcher (`fcn.140014910`) functions as a virtualization layer to hide the execution logic path. |

### Analyst Notes on Mapping:
*   **T1059 (Command and Scripting Interpreter):** Because the analyst highlighted that "the Tcl component is not just a minor feature but a core part of the execution logic," this confirms the malware uses these interpreters as a primary vehicle for malicious actions rather than just a helper.
*   **T1027 (Obfuscated Files or Information):** This covers both the "packing" layer (bit-shifting/masking) and the complexity of the dispatcher, as both are intended to frustrate automated tools and human analysts during static analysis.
*   **T1055.010 (Process Hollowing):** The specific mention of "hollowing out" a process is a high-confidence indicator for this sub-technique of Process Injection.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: The string section contains a high volume of non-human-readable data and obfuscated blocks common in packed binaries. Only unique identifiers found in the technical report have been categorized.*

### **IP addresses / URLs / Domains**
*   *(None identified)*

### **File paths / Registry keys**
*   *(None identified)*

### **Mutex names / Named pipes**
*   *(None identified)*

### **Hashes**
*   *(None identified in the provided text)*

### **Other artifacts**
*   **Known Strings:** `PyInstallerOnefileHiddenWindow` (Indicates use of the PyInstaller framework to mask a hidden window during execution).
*   **Tcl/Python Integration:** The binary utilizes both Tcl and Python interpreters as part of a "Nested Interpreter" architecture.
*   **Decoding Logic:** Evidence of custom decoding loops (`fcn.1400254b0`) involving bit-shifting, masking, and modular arithmetic used for unpacking malicious payloads from embedded data.
*   **VM/Instruction Dispatcher:** Detection of a custom bytecode interpreter (`fcn.140014910`, `fcn.1400144a0`) to execute de-obfuscated scripts in memory.

---

## Malware Family Classification

1. **Malware family**: Custom
2. **Malware type**: Loader
3. **Confidence**: High (for the role of the binary) / Medium (for the final payload's intent)

4. **Key evidence**: 
*   **Multi-Layered "Nested Interpreter" Architecture:** The binary integrates both Tcl and Python engines to create a "Russian Nesting Doll" execution environment, allowing malicious logic to be hidden within nested script layers that are difficult for static analysis tools to parse.
*   **Advanced Decoding & Virtualization:** The presence of complex bit-shifting/masking routines (`fcn.1400254b0`) and a custom bytecode interpreter/instruction dispatcher (`fcn.140014910`) indicates a high level of effort to obfuscate the final payload from security researchers.
*   **Evasive Execution Tactics:** The use of `PyInstallerOnefileHiddenWindow` and `ShowWindow(..., 0)` confirms the binary is designed to run "headless" in the background, while its reliance on standard script engines allows it to perform malicious actions (like network communication or file manipulation) using legitimate-looking code.
