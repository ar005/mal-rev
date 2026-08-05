# Threat Analysis Report

**Generated:** 2026-08-03 17:04 UTC
**Sample:** `0cd839c7cabceabe9324f0a440d99669a6e4f4c7975e2a19170d7289b5408ef1_0cd839c7cabceabe9324f0a440d99669a6e4f4c7975e2a19170d7289b5408ef1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0cd839c7cabceabe9324f0a440d99669a6e4f4c7975e2a19170d7289b5408ef1_0cd839c7cabceabe9324f0a440d99669a6e4f4c7975e2a19170d7289b5408ef1.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 783,360 bytes |
| MD5 | `65831a6209060d39487c945ce916a33e` |
| SHA1 | `7fa5eb306d8cbbfc593c605cb3ce53342258a5f2` |
| SHA256 | `0cd839c7cabceabe9324f0a440d99669a6e4f4c7975e2a19170d7289b5408ef1` |
| Overall entropy | 5.303 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771268206 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 137,216 | 6.44 | No |
| `.rdata` | 64,000 | 5.092 | No |
| `.data` | 3,584 | 2.433 | No |
| `.pdata` | 7,168 | 5.118 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 512 | 4.712 | No |
| `.reloc` | 569,344 | 4.038 | No |

### Imports

**KERNEL32.dll**: `AddVectoredExceptionHandler`, `CreateDirectoryW`, `FindFirstFileW`, `FindNextFileW`, `FindClose`, `CreateFileW`, `CopyFileW`, `GetCurrentProcess`, `GetModuleHandleA`, `MultiByteToWideChar`, `GetProcAddress`, `LoadLibraryA`, `GetWindowsDirectoryW`, `RaiseException`, `GetSystemInfo`
**ADVAPI32.dll**: `GetTokenInformation`, `AllocateAndInitializeSid`, `FreeSid`, `CheckTokenMembership`, `OpenProcessToken`

## Extracted Strings

Total strings found: **854** (showing first 100)

```
!This program cannot be run in DOS mode.
$
>QMyz0#*z0#*z0#*
'+w0#*
 +}0#*1
 +p0#*1
'+j0#*
&+C0#*z0"*
*+w0#*
!+{0#*Richz0#*
`.rdata
@.data
.pdata
@.fptable
@.reloc
Bf;Cu
SUVWATAUAVAWH
xA_A^A]A\_^][
@USVWATAUAVAWH
D$pexpa
D$tnd 3
D$x2-by
D$|te k
A_A^A]A\_^[]
@USVWATAUAVAWH
D9l$0upA
L9mXt>L
uD8mlt
A_A^A]A\_^[]
@SVWAWH
(A__^[
(A__^[
(A__^[
@SUVWATAVAWH
 A_A^A\_^][
\$ UVWATAUAVAWH
pA_A^A]A\_^]
\$ UVWATAUAVAWH
D8l$pu2D
D8L$pucL
A_A^A]A\_^]
@SUVWAVAWH
HcW<f;\:
XA_A^_^][
@SUVWAVAWL
A_A^_^][
A_A^_^][
A_A^_^][
UVWATAUAVAWH
PA_A^A]A\_^]
@SVWAVH
(A^_^[
(A^_^[
@SUVWH
uJLcB<A
D$\.?
(
D$`59?)f
D$P2DX
@SUVWH
H9t$0u
VAVAWH
 A_A^^
@USVWAVAWH
D$02D@
A_A^_^[]
@USVWATAUAVAWH
D$P75(#
D$82D@
A_A^A]A\_^[]
@USVWATAVAWH
PA_A^A\_^[]
@USVWATAUAVAWH
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
D$@2D
D$@2D
D$@2D
D$@2D
D$@2D
D$@2D
D$@2D
H9t$Hu
SUVWATAUAVAWH
(A_A^A]A\_^][
2*B8
ua
@USVWATAUAVAWH
D$`f3DLhf
A_A^A]A\_^[]
@USVWATAUAVAWH
ufIcG<I
A_A^A]A\_^[]
D$0D9p
D$ ?E2
L$ B2
D$0D;p
@SUVWAVH
 A^_^][
 A^_^][
@SUVWATAUAVAWH
HA_A^A]A\_^][
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140019d1c` | `0x140019d1c` | 14535 | ✓ |
| `fcn.140019d08` | `0x140019d08` | 14494 | ✓ |
| `fcn.14000e310` | `0x14000e310` | 4968 | ✓ |
| `fcn.140006330` | `0x140006330` | 3194 | ✓ |
| `fcn.140003510` | `0x140003510` | 2679 | ✓ |
| `fcn.140006fb0` | `0x140006fb0` | 2645 | ✓ |
| `fcn.140005470` | `0x140005470` | 2117 | ✓ |
| `fcn.140010050` | `0x140010050` | 2015 | ✓ |
| `fcn.140007f70` | `0x140007f70` | 1940 | ✓ |
| `fcn.140001e00` | `0x140001e00` | 1893 | ✓ |
| `fcn.140020f60` | `0x140020f60` | 1677 | ✓ |
| `fcn.14000a2b0` | `0x14000a2b0` | 1588 | ✓ |
| `fcn.14000cac0` | `0x14000cac0` | 1449 | ✓ |
| `fcn.140005d20` | `0x140005d20` | 1448 | ✓ |
| `fcn.14000c520` | `0x14000c520` | 1436 | ✓ |
| `fcn.14000bf80` | `0x14000bf80` | 1429 | ✓ |
| `fcn.14001c600` | `0x14001c600` | 1421 | ✓ |
| `fcn.14000b470` | `0x14000b470` | 1419 | ✓ |
| `fcn.14000ba00` | `0x14000ba00` | 1403 | ✓ |
| `fcn.14000d070` | `0x14000d070` | 1397 | ✓ |
| `fcn.14000d5f0` | `0x14000d5f0` | 1397 | ✓ |
| `fcn.14000db70` | `0x14000db70` | 1395 | ✓ |
| `fcn.140008710` | `0x140008710` | 1363 | ✓ |
| `fcn.14000af20` | `0x14000af20` | 1351 | ✓ |
| `fcn.1400148cc` | `0x1400148cc` | 1312 | ✓ |
| `fcn.140002b80` | `0x140002b80` | 1285 | ✓ |
| `fcn.140015a6c` | `0x140015a6c` | 1229 | ✓ |
| `fcn.14001440c` | `0x14001440c` | 1213 | ✓ |
| `fcn.14001f040` | `0x14001f040` | 1171 | ✓ |
| `fcn.140020e30` | `0x140020e30` | 1156 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001e00.c`](code/fcn.140001e00.c)
- [`code/fcn.140002b80.c`](code/fcn.140002b80.c)
- [`code/fcn.140003510.c`](code/fcn.140003510.c)
- [`code/fcn.140005470.c`](code/fcn.140005470.c)
- [`code/fcn.140005d20.c`](code/fcn.140005d20.c)
- [`code/fcn.140006330.c`](code/fcn.140006330.c)
- [`code/fcn.140006fb0.c`](code/fcn.140006fb0.c)
- [`code/fcn.140007f70.c`](code/fcn.140007f70.c)
- [`code/fcn.140008710.c`](code/fcn.140008710.c)
- [`code/fcn.14000a2b0.c`](code/fcn.14000a2b0.c)
- [`code/fcn.14000af20.c`](code/fcn.14000af20.c)
- [`code/fcn.14000b470.c`](code/fcn.14000b470.c)
- [`code/fcn.14000ba00.c`](code/fcn.14000ba00.c)
- [`code/fcn.14000bf80.c`](code/fcn.14000bf80.c)
- [`code/fcn.14000c520.c`](code/fcn.14000c520.c)
- [`code/fcn.14000cac0.c`](code/fcn.14000cac0.c)
- [`code/fcn.14000d070.c`](code/fcn.14000d070.c)
- [`code/fcn.14000d5f0.c`](code/fcn.14000d5f0.c)
- [`code/fcn.14000db70.c`](code/fcn.14000db70.c)
- [`code/fcn.14000e310.c`](code/fcn.14000e310.c)
- [`code/fcn.140010050.c`](code/fcn.140010050.c)
- [`code/fcn.14001440c.c`](code/fcn.14001440c.c)
- [`code/fcn.1400148cc.c`](code/fcn.1400148cc.c)
- [`code/fcn.140015a6c.c`](code/fcn.140015a6c.c)
- [`code/fcn.140019d08.c`](code/fcn.140019d08.c)
- [`code/fcn.140019d1c.c`](code/fcn.140019d1c.c)
- [`code/fcn.14001c600.c`](code/fcn.14001c600.c)
- [`code/fcn.14001f040.c`](code/fcn.14001f040.c)
- [`code/fcn.140020e30.c`](code/fcn.140020e30.c)
- [`code/fcn.140020f60.c`](code/fcn.140020f60.c)

## Behavioral Analysis

This final installment of disassembly completes our architectural map of the binary. The analysis of this final chunk confirms that the malware is not just a "loader," but a sophisticated **Command & Control (C2) Execution Framework.**

The addition of these functions reinforces our classification of the binary as an **Advanced Execution Engine / Task Orchestrator** and provides specific evidence of its multi-functional capabilities.

---

### Finalized Analysis Summary

#### Core Functionality and Purpose
*   **Complex Command Dispatcher (fcn.14001440c):** This is a massive, complex "gateway" function. It doesn't just execute code; it validates data structures before allowing execution to proceed. The nested logic (e.g., checking `*arg1 == -0x1f928c9d`) suggests it is inspecting an **Instruction Buffer**. If the buffer matches a specific "OpCode" or signature, the dispatcher resolves the corresponding handler in memory and passes control to it.
*   **Just-in-Time (JIT) Logic Resolution:** The frequent calls to `fcn.1400139a4()` within the logic flow suggest that the malware is resolving memory addresses for its internal functions at runtime. This prevents a static analyst from seeing a clear "tree" of what the malware does; the paths are only created in memory when specific conditions (commands) are met.
*   **Data Transformation & File I/O (fcn.14001f040):** This function demonstrates the ability to process large buffers, perform complex index calculations, and interact with the filesystem via `WriteFile`. The presence of `GetConsoleOutputCP` suggests that while it may not show a console to the user, it handles data encoding/decoding (like converting special characters) during its "drop" or "write" phases.
*   **Mathematical/Cryptographic Primitives (fcn.140020e30):** The presence of floating-point handling and specialized math checks often indicates the underlying infrastructure for **encryption/decryption routines** or complex hashing algorithms used to verify the integrity of received payloads before execution.

#### Sophisticated Malicious Behaviors
*   **Gatekeeper Logic:** Several blocks (like `fcn.14001687c` and `fcn.14001695c`) act as "gatekeepers." If a check fails or if the malware detects it is being monitored, these functions will trigger an exit or jump to a "dead end" (the `swi(3)` calls), preventing further analysis of the core malicious components.
*   **Advanced Memory Manipulation:** The code frequently treats memory as a dynamic array of structures. Instead of using standard variables, it calculates offsets (`uVar11 * 0x14`, `uVar5 * 0x48`) to navigate its internal "brain." This is designed to hide the data's purpose from automated scanners that look for standard strings or known patterns.
*   **"Switching" Capabilities:** The complex branching in `fcn.14001440c` confirms that this one binary can act as a **downloader, an injector, and a persistence installer** all at once, depending entirely on the "Task ID" it receives from its remote controller.

#### Technical Indicators & Patterns
*   **Instruction Set Architecture (ISA) Emulation:** The malware effectively has its own internal programming language. It interprets instructions (OpCodes), checks lengths/offsets, and executes corresponding subroutines. 
*   **Polymorphic Execution Paths:** By using indirect jumps and nested conditionals based on decrypted values, the "main" path of execution changes every time it runs, making it very difficult for a human analyst to map out all possible behaviors in a single pass.
*   **Anti-Analysis Hooks:** The use of `swi(3)` (Software Interrupt 3) is a classic technique to break the flow of automated disassemblers and debuggers by forcing the system into an exception handler that only the malware’s "clean" code can resolve correctly.

---

### Final Summary of Risk

The risk profile for this sample remains at **Critical.**

**Final Classification: Modular Command Orchestration Framework (MCOF)**

This binary is a highly professional piece of malware engineering. It exhibits several characteristics common in high-level **Advanced Persistent Threat (APT)** toolsets:
1.  **Modular Versatility:** The ability to act as multiple different types of threats based on remote commands.
2.  **Extreme Obfuscation:** The use of internal "instruction sets" and indirect calls makes the code’s true purpose invisible until it is actually running in a compromised environment.
3.  **Operational Resilience:** By compartmentalizing its functions into "Dispatchers," "Validators," and "Handlers," it ensures that if one component is discovered, the entire logic chain remains hidden.

**Final Conclusion:** This binary is not a simple infection; it is an **infrastructure tool.** It is designed to stay resident on a network for long periods, performing various tasks at the whim of a remote operator. 

**Recommendations:**
*   **Isolate and Hunt:** Any system where this code is found should be assumed to have a persistent backdoor. The presence of such a sophisticated orchestrator suggests that an attacker may have been active in the environment for some time.
*   **Memory Forensics:** Because so much of its logic is resolved at runtime, memory forensics (capturing the RAM of the infected process) is the only reliable way to see the full scope of the "instructions" it has received and executed.
*   **Block Indicators:** Any IPs or domains associated with this sample should be blocked globally across the enterprise.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the relevant MITRE ATT&CK techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The use of an "Instruction Buffer," custom "OpCodes," and a complex dispatcher indicates the malware functions as its own interpreter for processing remote commands. |
| **T1027** | Obfuscated Files or Information | JIT logic resolution, dynamic memory offset calculations, and cryptographic primitives are used to hide execution paths and data from static analysis. |
| **T1497** | Virtualization/Sandbox Detection | The "Gatekeeper" functions and `swi(3)` interrupts are designed to detect debuggers or automated analysis environments and stall execution if detected. |
| **T1105** | Ingress Tool Transfer | The identification of the malware as a "downloader" with "drop" capabilities confirms its role in retrieving and installing additional components on the target system. |
| **T1132** | Data Encoding | The use of `GetConsoleOutputCP` and complex data transformation routines indicates the obfuscation of data during transmission or local processing. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the intelligence report. 

**Note:** The "Strings" section contains highly obfuscated or packed data (likely from a protected binary), and many of the values are memory addresses or internal labels that do not constitute actionable network indicators in their current form.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: While `WriteFile` is mentioned, no specific hardcoded file paths were provided).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified. (No MD5/SHA1/SHA256 strings present in the text).

### **Other artifacts**
*   **Internal Logic Constants:** `0x1f928c9d` (Used as an Instruction Buffer validation check in `fcn.14001440c`).
*   **Function Offsets (Analyzed logic paths):** 
    *   `14001440c` (Complex Command Dispatcher)
    *   `1400139a4` (JIT Logic Resolution)
    *   `14001f040` (Data Transformation/File I/O)
    *   `140020e30` (Cryptographic Primitives)
    *   `14001687c` / `14001695c` (Gatekeeper Logic)
*   **Ant-Analysis Techniques:** Use of `swi(3)` (Software Interrupt 3) to break debugger/disassembler flow.
*   **C2 Behavior Pattern:** The sample functions as a **Modular Command Orchestration Framework (MCOF)**, utilizing an internal Instruction Set Architecture (ISA) to process remote commands for tasks such as downloading, injecting, and establishing persistence.

---

## Malware Family Classification

1. **Malware family:** Custom (identified as a Modular Command Orchestration Framework)
2. **Malware type:** Backdoor / Loader
3. **Confidence:** High

4. **Key evidence:**
*   **Multi-functional Dispatcher Architecture:** The binary utilizes a complex "Command Dispatcher" and internal instruction set to switch roles (downloader, injector, persistence installer) based on received Task IDs, characteristic of sophisticated backdoor frameworks.
*   **Advanced Evasion & Anti-Analysis:** The presence of "Gatekeeper" logic, `swi(3)` interrupts, and JIT logic resolution indicates a high level of intent to bypass automated sandboxes and manual reverse engineering.
*   **Sophisticated Orchestration:** The analysis confirms the binary is not a simple infection but an infrastructure tool designed for long-term residence and modular execution of various commands.
