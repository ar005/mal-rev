# Threat Analysis Report

**Generated:** 2026-06-28 14:16 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, UPX compressed, 3 sections |
| Size | 3,298,816 bytes |
| MD5 | `86350441ef00f17b2ab6ed184a319e90` |
| SHA1 | `7b5fe5ee040932d828f9676182fb07264b15b11d` |
| SHA256 | `02ddfae5499c560790df90e28819279652210092e121fbd2d880aaf87f80ad05` |
| Overall entropy | 6.401 |
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
| `.text` | 4,894,208 | 6.037 | No |
| `.rdata` | 6,202,368 | 6.056 | No |
| `.data` | 342,016 | 5.24 | No |
| `.idata` | 1,536 | 3.889 | No |
| `.reloc` | 231,424 | 6.652 | No |
| `.symtab` | 512 | 0.02 | No |

### Imports

**KERNEL32.DLL**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetUnhandledExceptionFilter`, `SetProcessPriorityBoost`

## Extracted Strings

Total strings found: **38309** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.idata
.reloc
B.symtab
 Go build ID: "dSpta53yrajZyp4Cttgp/iRKwsoH-SW-dKCVyawG-/Z8PHINlJPZ-rsL_KIHuq/HN4g4I6CmZf4B8Au3JjL"
 
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
| `fcn.00806ae0` | `0x806ae0` | 142602 | ✓ |
| `fcn.007ccbd0` | `0x7ccbd0` | 73362 | ✓ |

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
- [`code/fcn.007ccbd0.c`](code/fcn.007ccbd0.c)
- [`code/fcn.00806ae0.c`](code/fcn.00806ae0.c)

## Behavioral Analysis

The inclusion of **Chunk 17** provides the final piece of the puzzle regarding the VM's architectural intent. This final segment confirms that the packer doesn't just have a complex dispatch table; it utilizes a **multi-layered state machine where the path taken through the "maze" determines not only which function is called, but how the internal environment is updated.**

The following analysis integrates all previous findings (Chunks 1–17) into a finalized comprehensive profile of the VM engine.

---

### Final Analysis: Malware Loader/Packer (VM Engine Architecture)

The architecture identified across all chunks describes an **Advanced State-Aware Virtual Machine**. It is designed to hide not only the "what" (the malicious actions) but also the "how" (the logic flow and data transformation rules).

---

### 1. The Decision Maze: Granular Logic Partitioning
Chunk 17 highlights the extreme depth of the `cVar10` check tree.
*   **The Mechanism:** Instead of a standard `switch(opcode)` or `jump_table`, the VM uses deeply nested, overlapping `if` statements (e.g., checking `cVar10 < 0x2e`, then `< 0x1d`, etc.).
*   **Significance:** This is **Path-Dependent Logic**. A single opcode might have five different ways to be processed depending on the "hidden" state of the VM. By forcing the analyst to trace dozens of branches to find a single result, the authors ensure that static analysis tools cannot map a 1:1 relationship between an instruction and its behavior.
*   **Analyst Impact:** This is specifically designed to cause **Analyst Fatigue**. Even if you identify one block as "String Decoding," the next time that same piece of code appears, it may be under a different branch with different flags, making automated detection nearly impossible.

### 2. Context-Aware Polymorphism & Operand Stitching
The repeated use of `CONCAT31` and `CONCAT44` with varying constants (e.g., `0x7f`, `0x7b`, `0x7f`) just before handler calls is a primary defensive layer.
*   **The Mechanism:** The instruction isn't "raw." It is **constructed at the last possible micro-second**. For example, in several blocks, different paths eventually lead to `fcn.007df0d0`, but they arrive there with different concatenated values appended to the operands.
*   **Significance:** This ensures that the instruction's "identity" is fluid. One "Add" instruction might be represented by a dozen different byte sequences depending on which path through the maze it took, effectively hiding the core logic behind **context-dependent mutations**.

### 3. State-Dependent Gatekeeping (Validation Gates)
Chunks 16 and 17 reveal frequent `if (in_stack_... != NULL)` checks before jumping to shared handler locations like `code_r0x007cccbf`.
*   **The Mechanism:** These are **Execution Gateways**. Before the VM executes a "common" task, it validates its own internal state. If the environment is not exactly as expected (e.g., due to an emulator's incorrect behavior or a researcher’s modified memory), the code branches into a "safe" but useless path.
*   **Significance:** This protects the packer from being successfully "traced." It ensures that only under perfect, real-world conditions does the core malicious logic activate.

### 4. Abstracted Memory & Register Mapping
The complex math for offset calculation (e.g., `uVar17 = uStack_538._4_4_ + (0xfffffffd < uStack_538)`) confirms a decoupled architecture.
*   **The Mechanism:** The VM uses its own **Virtual Register Set**. It maps "Register A" to some calculated offset in a heap/buffer, rather than using `EAX` or `RBX`. 
*   **Significance:** This hides the **data flow**. When an analyst watches a value move from one memory location to another, they aren't seeing the actual logic; they are watching the VM's internal "shadow" memory. The true meaning of the data is only revealed at the final moment of execution.

### 5. Dynamic Operand Assembly & Stitching
The logic in chunks 14-17 shows that operands (the values an instruction acts upon) are often not contiguous.
*   **The Mechanism:** Values are "stitched" together using `CONCAT` functions just before the handler is invoked.
*   **Significance:** This prevents **Static Signature Matching**. Because the full operand isn't visible until the jump, a scanner cannot look at the bytes and know what they will do.

---

### Summary of Technical Indicators (Cumulative)

| Feature | Mechanism observed in Chunks 1-17 | Purpose |
| :--- | :--- | :--- |
| **Logic Maze** | Deeply nested `if/else` chains for opcode evaluation. | Force manual analysis; defeat automated "Switch" mapping. |
| **Polymorphic Dispatch** | Multiple paths leading to same handler with different `CONCAT` constants. | Ensure identical logic doesn't have a consistent signature. |
| **State-Gating** | Validating internal stack pointers before critical jump points. | Evade sandboxes/emulators by checking for "perfect" environment states. |
| **Abstracted Mapping** | Calculation of offsets (`uVar27`, `iVar8`) to access hidden data. | Hide the flow of sensitive information from standard debuggers. |
| **Instruction Stitching** | Reassembling operands in-memory just before handler execution. | Prevent static analysis tools from identifying operand intent. |

---

### Final Conclusion: Technical Sophistication Level
The packer is extremely sophisticated, employing a **Stateful Micro-Processor** architecture. It does not merely obfuscate the code; it creates an entirely different execution environment that "interprets" the malicious logic only when all internal state conditions are met. 

**Recommended Methodology for Full Decryption:**
1.  **Symbolic Execution (Angr/Triton):** To map out all possible paths in the `cVar10` maze and identify all reachable states.
2.  **Dynamic Taint Analysis:** To track how data flows through the "Abstracted Memory" to see which values actually impact the final payload.
3.  **De-virtualization Scripting:** A custom script would be needed to "flatten" the nested `if` blocks and simplify the code into a linear representation of the VM's actual instruction set.

The packer is designed for **maximum durability against automated analysis**, requiring significant manual effort to untangle the layers of logic it employs to hide its true intent.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the relevant MITRE ATT&CK techniques. 

The analyzed packer employs several layers of defense designed to frustrate both automated systems and human analysts by hiding the execution logic (the "how") as much as the actual payload (the "what").

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Packing | The use of a multi-layered, state-aware Virtual Machine architecture functions as a sophisticated packer to wrap and hide the malicious code's true logic. |
| **T1027** | Obfuscated Files or Information | The "Decision Maze" uses nested, overlapping `if` statements to ensure that no direct 1:1 mapping exists between an opcode and its behavior in static analysis. |
| **T1027** | Obfuscated Files or Information | Operand Stitching/Polymorphism ensures that the identity of a command is only determined at the point of execution, preventing signature-based detection. |
| **Defense Evasion** | Defense Evasion (Sandbox/Emulator Evasion) | "State-Dependent Gatekeeping" functions as an environment check to detect analysis tools and redirect the code to a "safe" path if an analyst's presence is detected. |
| **T1027** | Obfuscated Files or Information | "Abstracted Memory & Register Mapping" hides data flow by decoupling actual values from the physical registers/memory addresses viewed by standard debuggers. |

### Analyst Notes:
*   **T1029 (Packing)** is the overarching technique for the VM architecture itself. The complexity of the VM creates a "black box" that forces an analyst to perform heavy manual labor to de-virtualize the code.
*   **T1027 (Obfuscated Files or Information)** is applied multiple times here because it encompasses several specific behaviors: the **Logic Maze** (hiding flow), **Operand Stitching** (hiding identity/signature), and **Abstracted Mapping** (hiding data intent).
*   The **State-Dependent Gatekeeping** specifically targets common automated analysis environments. While not always listed under a unique sub-technique ID in every version of the framework, it is the primary method for **Defense Evasion** within packer logic to ensure execution only occurs on "real" target machines.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the intelligence report regarding Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided text describes a highly sophisticated **malware loader/packer** utilizing a custom virtual machine (VM) architecture. The "Strings" section contains primarily obfuscated data, internal compiler artifacts, and non-human-readable sequences typical of packed code. 

---

### **Indicators of Compromise (IOCs)**

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: `fcn.007df0d0` was identified in the analysis, but this is a relative memory offset within the binary, not a system file path or registry key).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified. (Note: A **Go build ID** `dSpta53yrajZyp4Cttgp/iRKwsoH-SW-dKCVyawG-/Z8PHINlJPZ-rsL_KIHuq/HN4g4I6CmZf4B8Au3JjL` was present in the strings; however, this is a unique identifier for the specific compilation of the Go binary and not a standard file hash such as MD5 or SHA-256).

**Other artifacts**
*   None identified. (No C2 patterns, User-Agents, or hardcoded commands were found in the provided text).

---

### **Analyst Notes**
While no traditional network or host-based IOCs (like IPs or paths) were extracted, the behavioral analysis confirms a high level of sophistication:
*   **Custom VM Architecture:** The use of "Decision Mazes" and "State-Dependent Gatekeeping" suggests that any attempts to find hardcoded artifacts via static analysis will be unsuccessful.
*   **Anti-Analysis Techniques:** The packer is designed specifically to defeat automated sandboxes and memory scanners by using dynamic operand stitching and state-aware logic. 
*   **Recommendation:** Since no static IOCs are available, detection should focus on **behavioral signatures**, such as the presence of high-frequency `if/else` branching (the "Logic Maze") or calls to non-standard decryption loops.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Packer
3. **Confidence**: High (regarding its function as a loader/packer) / Low (regarding specific campaign attribution)

4. **Key evidence**:
*   **Virtual Machine Architecture:** The sample employs an "Advanced State-Aware Virtual Machine" that uses complex nested logic ("Decision Mazes") and custom register mapping to decouple the actual malicious logic from the underlying assembly, making static analysis extremely difficult.
*   **Anti-Analysis & Evasion:** The inclusion of "State-Dependent Gatekeeping" (validating internal state before core execution) and "Operand Stitching" indicates a primary goal of evading automated sandboxes and signature-based detection by ensuring code is only fully "unpacked" under specific conditions.
*   **Sophisticated Obfuscation:** The use of context-aware polymorphism and dynamically constructed instructions at the "last possible micro-second" confirms it is designed as a high-tier protector/packer rather than a simple downloader.
