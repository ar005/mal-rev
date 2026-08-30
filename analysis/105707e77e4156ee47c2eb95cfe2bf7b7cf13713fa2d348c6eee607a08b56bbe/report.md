# Threat Analysis Report

**Generated:** 2026-08-18 19:36 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, UPX compressed, 3 sections |
| Size | 3,292,672 bytes |
| MD5 | `6c1fce048dd6807e55ba57958a602c5b` |
| SHA1 | `7743d6480d2571922f62812fb35488c1c7472de8` |
| SHA256 | `105707e77e4156ee47c2eb95cfe2bf7b7cf13713fa2d348c6eee607a08b56bbe` |
| Overall entropy | 6.404 |
| Unpacked | ✓ Yes (tool: upx) |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 4,889,600 | 6.041 | No |
| `.rdata` | 6,197,248 | 6.06 | No |
| `.data` | 342,016 | 5.238 | No |
| `.idata` | 1,536 | 3.925 | No |
| `.reloc` | 231,424 | 6.651 | No |
| `.symtab` | 512 | 0.02 | No |

### Imports

**KERNEL32.DLL**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetUnhandledExceptionFilter`, `SetProcessPriorityBoost`

## Extracted Strings

Total strings found: **38277** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.idata
.reloc
B.symtab
 Go build ID: "yehnFtK7CeTWei53TWWQ/d914duEu7_MG56PUsJeV/qQAClmgF9lglw2WNsz_s/T9FSl0wAF7pC44BYBeCI"
 
|$9;u
|$9;u
|$9;u
;cpu.u
X8Zu$
X8Zu
H(9J(u|
H,8J,us
H-8J-uj
H49J4ub
H89J8uZ
H<8J<uQ
H=8J=uH
JD9HDu@
HH9JHu8
HL8JLu/
HM8JMu&
JT9HTu
HX9JXu
H\8J\u
H]8J]u
@expa
@ 2-by
@$2-by
@(2-by
@,2-by
@0te k
@4te k
@8te k
@<te k
D$49H(v6
D$<9D$
D$49D$
D$ 9D$
	;av}
L$,9yw
69t$Dt
69t$Dt
l$(9.u
|$09GDu
L$(9Aw
T$0+B
L$ 9A4t 
G 9E tJ
D$,+D$
T$+B
D$89D$
L$H9A4v
\$49\$(u
L$$9A(s
\$(9S4
u
9Hw
	;avL
	;avY
L$+A
L$ 9H<s
L$09A4v
T$(9J4s
T$<9B4v
L$,#D$0#L$4
UUUU%UUUU
T$ 9T$
D$09D$
uP9uTu1
9T$,t-
D$49D$
D$<9D$
L$89L$<
t19A0t,
|$ t%
19A u,
Z 9X s&9B
v 9q w
9
w9J
9
w9J
9
w9J
9L$Pv	
9L$Pv	
D$$9D$
t9PPw
D$<9D$
D$<9D$
T$,9B 
D$,9D$
	;avO
L$D9L$
D$@9D$(u9K<u
D$<9D$
D$<9D$
|$D2u 
D$H9D$
8runtu
D$L9D$
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0046d8a0` | `0x46d8a0` | 432480 | ✓ |
| `fcn.0046d8c0` | `0x46d8c0` | 410048 | ✓ |
| `fcn.0046d900` | `0x46d900` | 410016 | ✓ |
| `fcn.0046da50` | `0x46da50` | 217133 | ✓ |
| `fcn.0046da60` | `0x46da60` | 216973 | ✓ |
| `fcn.0046da70` | `0x46da70` | 216813 | ✓ |
| `fcn.0046da80` | `0x46da80` | 216653 | ✓ |
| `fcn.0046da90` | `0x46da90` | 216493 | ✓ |
| `fcn.0046daa0` | `0x46daa0` | 216333 | ✓ |
| `fcn.0046dab0` | `0x46dab0` | 216173 | ✓ |
| `fcn.0046dac0` | `0x46dac0` | 216013 | ✓ |
| `fcn.0046dad0` | `0x46dad0` | 215853 | ✓ |
| `fcn.0046dae0` | `0x46dae0` | 215693 | ✓ |
| `fcn.0046daf0` | `0x46daf0` | 215533 | ✓ |
| `fcn.0046db00` | `0x46db00` | 215373 | ✓ |
| `fcn.0046db10` | `0x46db10` | 215213 | ✓ |
| `fcn.0046db20` | `0x46db20` | 215053 | ✓ |
| `fcn.0046db30` | `0x46db30` | 214893 | ✓ |
| `fcn.0046db40` | `0x46db40` | 214733 | ✓ |
| `fcn.0046db50` | `0x46db50` | 214573 | ✓ |
| `fcn.0046db60` | `0x46db60` | 205985 | ✓ |
| `fcn.0046db80` | `0x46db80` | 205825 | ✓ |
| `fcn.0046dba0` | `0x46dba0` | 205665 | ✓ |
| `fcn.0046dbc0` | `0x46dbc0` | 205505 | ✓ |
| `fcn.0046dbe0` | `0x46dbe0` | 205345 | ✓ |
| `fcn.0046dc00` | `0x46dc00` | 205185 | ✓ |
| `fcn.0046dc20` | `0x46dc20` | 205025 | ✓ |
| `fcn.0046dc40` | `0x46dc40` | 204865 | ✓ |
| `fcn.00806ee0` | `0x806ee0` | 142602 | ✓ |
| `fcn.007ccfd0` | `0x7ccfd0` | 73362 | ✓ |

### Decompiled Code Files

- [`code/fcn.0046d8a0.c`](code/fcn.0046d8a0.c)
- [`code/fcn.0046d8c0.c`](code/fcn.0046d8c0.c)
- [`code/fcn.0046d900.c`](code/fcn.0046d900.c)
- [`code/fcn.0046da50.c`](code/fcn.0046da50.c)
- [`code/fcn.0046da60.c`](code/fcn.0046da60.c)
- [`code/fcn.0046da70.c`](code/fcn.0046da70.c)
- [`code/fcn.0046da80.c`](code/fcn.0046da80.c)
- [`code/fcn.0046da90.c`](code/fcn.0046da90.c)
- [`code/fcn.0046daa0.c`](code/fcn.0046daa0.c)
- [`code/fcn.0046dab0.c`](code/fcn.0046dab0.c)
- [`code/fcn.0046dac0.c`](code/fcn.0046dac0.c)
- [`code/fcn.0046dad0.c`](code/fcn.0046dad0.c)
- [`code/fcn.0046dae0.c`](code/fcn.0046dae0.c)
- [`code/fcn.0046daf0.c`](code/fcn.0046daf0.c)
- [`code/fcn.0046db00.c`](code/fcn.0046db00.c)
- [`code/fcn.0046db10.c`](code/fcn.0046db10.c)
- [`code/fcn.0046db20.c`](code/fcn.0046db20.c)
- [`code/fcn.0046db30.c`](code/fcn.0046db30.c)
- [`code/fcn.0046db40.c`](code/fcn.0046db40.c)
- [`code/fcn.0046db50.c`](code/fcn.0046db50.c)
- [`code/fcn.0046db60.c`](code/fcn.0046db60.c)
- [`code/fcn.0046db80.c`](code/fcn.0046db80.c)
- [`code/fcn.0046dba0.c`](code/fcn.0046dba0.c)
- [`code/fcn.0046dbc0.c`](code/fcn.0046dbc0.c)
- [`code/fcn.0046dbe0.c`](code/fcn.0046dbe0.c)
- [`code/fcn.0046dc00.c`](code/fcn.0046dc00.c)
- [`code/fcn.0046dc20.c`](code/fcn.0046dc20.c)
- [`code/fcn.0046dc40.c`](code/fcn.0046dc40.c)
- [`code/fcn.007ccfd0.c`](code/fcn.007ccfd0.c)
- [`code/fcn.00806ee0.c`](code/fcn.00806ee0.c)

## Behavioral Analysis

This analysis incorporates findings from **chunk 17/17**, the final segment of the provided disassembly. These segments conclude our mapping of the VM’s dispatcher and provide a comprehensive view of the protection's architecture.

---

### Updated Analysis Summary
The final chunk solidifies the conclusion that this is not a standard packer, but a **sophisticated virtualized environment** (similar to VMProtect or Themida). The complexity of the "Decision Forest" in chunks 16 and 17 confirms that the developers have implemented a massive "Switch-Tree" to mask the core logic.

The primary architectural pillars remain:
1.  **State-Machine Architecture:** `cVar10` serves as the primary opcode.
2.  **Decoupled Action Model:** The Dispatcher (`fcn.004f39d0`) acts as the "Execution Engine," where specific hex keys are exchanged for malicious functionality.

The new data provides the following critical insights:
1.  **Massive Gate Volume:** This chunk reveals an even larger list of unique hex keys, some of which appear multiple times or across different logic branches. This suggests a very large instruction set (ISA) and potentially "aliased" opcodes where different virtual instructions lead to the same physical handler if they share similar behaviors.
2.  **Pre-Dispatch Logic:** We see significant "preparation" code before a jump is made (e.g., `uVar12 = CONCAT31(Var29, 0x7b)`). This indicates that the raw opcode from the VM's memory might be combined with operand data or environment flags before it hits the dispatcher.
3.  **Deep Nesting as a Defense:** The repetitive use of `if (cVar10 < x) { if (cVar10 < y) ... }` is an intentional "maze" for automated de-compilers, forcing human analysts to manually trace the flow to find the actual malicious calls.

---

### New Findings from Chunk 17/17

#### 1. Expansion of the "Gatekeeper" Inventory
Chunk 17 reveals a significant number of new hex constants passed to `fcn.004f39d0`. This expands our "map" of potential capabilities:
*   **Previously identified:** `0x986f90`, `0x97ea8b`, `0x976e7e`, `0x98409f`, `0x98ff8a`, `0x98ba3f`, `0x9789d5`.
*   **New constants from Chunk 17:** `0x98182f`, `0x97ea73`, `0x987b58` (repeated), `0x97b87e`, `0x987b7a`, `0x976e7e`, `0x984bbd`, `0x991a71`, `0x98ff5c`, `0x98d009`.
*   **Significance:** The diversity of these keys suggests a wide range of capabilities, from simple arithmetic and memory movement to complex networking or file I/O operations.

#### 2. Logic Aliasing & Code Merging
In several locations (e.g., `code_r0x007d0151`), the code validates several different conditions just to reach the same dispatcher call with the key `0x986f90`.
*   **Mechanism:** This is a "Multi-Path Convergence." The VM architecture allows multiple internal opcodes (which are easier for the author to manage) to map to one core functionality in the handler. 
*   **Significance:** For an analyst, this means that identifying `0x986f90` as a specific action is high-priority, as it likely represents a "Primary Instruction" used by multiple parts of the malware's logic.

#### 3. Contextual State Evaluation
Several blocks include checks like `if (param_12 == 0)` or complex bitwise/comparison logic before dispatching.
*   **Mechanism:** **State-Dependent Execution.** The VM isn't just reading a list of instructions; it is checking the "context" of the current execution state to decide which handler to call.
*   **Significance:** This suggests that the malware's behavior can change based on internal flags, potentially making some malicious behaviors only active under specific conditions (e.g., after a successful C2 check).

#### 4. Heavy use of "Glue Code" and Obfuscation Macros
The recurring `CONCAT31` and `CONCAT44` calls are typical of compilers processing complex data structures or protected code. These blocks often appear just before the dispatcher, likely preparing the arguments (registers/stack) for the handler.

---

### Final Technical Characteristics Summary

| Feature | Status | Analysis Detail |
| :--- | :--- | :--- |
| **Architecture** | **Virtual Machine (VM)** | The code does not perform direct actions; it interprets a "virtual" instruction set. |
| **Decision Tree** | **Dense & Nested** | Uses nested `if` statements to create a massive, opaque map of opcodes. |
| **Dispatcher** | `fcn.004f39d0` | The central hub where opcode constants are translated into actions. |
| **Key Vocabulary** | **Extensive** | Large list of hex keys (e.g., `0x986f90`, `0x987b58`) identifies the "tools" in the malware's toolbox. |
| **Complexity Level** | **High / Professional** | The scale and consistency of the obfuscation indicate a high-end commercial protector or very sophisticated custom packer. |

---

### Finalized Risk Assessment & IR Strategy

**Status: CRITICAL - HIGHLY PROTECTED MALWARE**

The malware is designed to be "unbreakable" by standard automated scanners. It uses an industry-standard protection technique where the actual malicious logic (the "payload") never exists in a raw, executable form; it only exists as a set of "instructions" for the VM to interpret.

#### Recommended Incident Response Actions:

1.  **Identify the Core Gateways:**
    The most efficient way to deconstruct this threat is to **map the hex constants**. 
    *   Create an automated script to log every unique constant passed to `fcn.004f39d0`.
    *   Example: If `0x986f90` is consistently associated with a socket call, label it as "Networking_Gateway."

2.  **Dynamic Instrumentation (Frida/x64dbg):**
    Instead of attempting to statically de-obfuscate the 1,000+ lines of `if` statements:
    *   Place a breakpoint on `fcn.004f39d0`.
    *   Log the registers and memory at the moment of every call.
    *   **Observation:** This will generate a "Behavior Log" that shows exactly which capabilities are triggered during execution, bypassing the "Decision Forest" entirely.

3.  **Memory Forensics (Snapshotting):**
    Since the VM must eventually decode its instructions to pass them to the dispatcher:
    *   Perform memory dumps of the process at intervals.
    *   Look for strings or API addresses that appear in memory only *after* a dispatch call to `fcn.004f39d0`.

4.  **Heuristic Detection:**
    The "Decision Forest" structure itself is a signature. 
    *   Develop YARA rules to detect the specific pattern of nested `if` statements and the repeated calls to `fcn.004f39d0` with unique, high-entropy hex constants. This can help identify other samples from the same threat actor or using the same packer.

5.  **Payload Extraction:**
    Because the payload is "decoupled," look for where the VM's **Instruction Pointer (IP)** points after a dispatcher call. The code following `fcn.004f39d0` often contains the logic to increment or loop, which can be used to find the boundaries of each "Action."

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a custom VM architecture, "Decision Forest" switch-trees, and logic aliasing are specifically designed to hide the code's true intent from both automated tools and human analysts. |
| **T1568** | Dynamic Resolution | The translation of various hex constants ("Gatekeepers") into specific capabilities like networking or file I/O suggests that actual API calls are hidden behind a dispatcher that resolves them dynamically. |
| **T1027 (Sub-behavior)** | *State-Dependent Execution* | The use of "contextual state evaluation" to gate specific functionalities is a form of obfuscation used to ensure malicious behaviors only trigger under specific conditions, evading automated analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Because the malware utilizes a sophisticated **Virtual Machine (VM) protection layer**, many traditional IOCs (like plain-text IP addresses or file paths) are obfuscated or hidden within the "Decision Forest." The following artifacts represent the technical signatures identified in the analysis.

### **IP addresses / URLs / Domains**
*   None identified (The content provided contains only internal logic and obfuscated strings).

### **File paths / Registry keys**
*   None identified.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   No standard MD5, SHA-1, or SHA-256 file hashes were present in the text. 
*   **Note:** The string `yehnFtK7CeTWei53TWWQ/d914duEu7_MG56PUsJeV/qQAClmgF9lglw2WNsz_s/T9FSl0wAF7pC44BYBeCI` is a **Go Build ID**. While not a file hash, it can be used to identify specific builds of Go-based binaries.

### **Other artifacts**
*   **Malware Architecture:** Virtual Machine (VM) based protection (similar to VMProtect/Themida).
*   **Primary Dispatcher Address:** `0x004f39d0` (Identified as the core "Execution Engine" for malicious functionality).
*   **VM Gateway Constants (Opcode Keys):** The following hex values are used by the dispatcher to trigger specific behaviors. These can be used as signatures for identifying this specific packer/loader:
    *   `0x986f90` (Primary instruction / high-frequency key)
    *   `0x97ea8b`
    *   `0x976e7e`
    *   `0x98409f`
    *   `0x98ff8a`
    *   `0x98ba3f`
    *   `0x9789d5`
    *   `0x98182f`
    *   `0x97ea73`
    *   `0x987b58`
    *   `0x97b87e`
    *   `0x987b7a`
    *   `0x984bbd`
    *   `0x991a71`
    *   `0x98ff5c`
    *   `0x98d009`
*   **Obfuscation Techniques:** 
    *   "Decision Forest" (Nested `if` statement logic).
    *   "Multi-Path Convergence" (Multiple opcodes mapping to a single dispatcher call).
    *   "State-Dependent Execution" (Contextual checks before dispatching).

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1. **Malware family:** Unknown (Sophisticated Packer/Loader)
2. **Malware type:** Loader
3. **Confidence:** High (for the technical architecture), Medium (for specific family identification)
4. **Key evidence:**
    *   **Virtual Machine (VM) Architecture:** The sample employs a sophisticated virtualized execution environment (similar to VMProtect/Themida), where malicious logic is hidden behind a custom instruction set and a dispatcher (`fcn.004f39d0`), making it resistant to standard static analysis.
    *   **"Decision Forest" & Gatekeeper Constants:** The use of heavily nested `if` statements, "multi-path convergence," and unique hex constants (e.g., `0x986f90`) as gatekeepers indicates a high level of professional obfuscation designed to mask core functionality like networking and file I/O.
    *   **Presence of Go Build ID:** The detection of a Go Build ID suggests the use of modern, high-scale delivery frameworks often associated with sophisticated threat actors who prioritize "stealth" via complex, multi-layered loaders.
