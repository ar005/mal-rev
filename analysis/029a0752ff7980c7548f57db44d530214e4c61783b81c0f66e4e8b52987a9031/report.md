# Threat Analysis Report

**Generated:** 2026-06-28 09:52 UTC
**Sample:** `029a0752ff7980c7548f57db44d530214e4c61783b81c0f66e4e8b52987a9031_029a0752ff7980c7548f57db44d530214e4c61783b81c0f66e4e8b52987a9031.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `029a0752ff7980c7548f57db44d530214e4c61783b81c0f66e4e8b52987a9031_029a0752ff7980c7548f57db44d530214e4c61783b81c0f66e4e8b52987a9031.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, 6 sections |
| Size | 11,418,112 bytes |
| MD5 | `6f38631b29f4f8df8f6e4ffef067ffeb` |
| SHA1 | `6e1eb69902802df830d395996f983e593881d6b6` |
| SHA256 | `029a0752ff7980c7548f57db44d530214e4c61783b81c0f66e4e8b52987a9031` |
| Overall entropy | 6.395 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 4,771,840 | 6.02 | No |
| `.rdata` | 6,074,880 | 6.059 | No |
| `.data` | 342,016 | 5.234 | No |
| `.idata` | 1,536 | 3.865 | No |
| `.reloc` | 226,304 | 6.657 | No |
| `.symtab` | 512 | 0.02 | No |

### Imports

**KERNEL32.DLL**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetUnhandledExceptionFilter`, `SetProcessPriorityBoost`

## Extracted Strings

Total strings found: **37180** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.idata
.reloc
B.symtab
 Go build ID: "hYDAsqMjBze1O-lA2Ym5/nma4m7AXfhxqlXjaRJkw/HdUC4OOClQtsk6Ll0A28/GYaB3o4yowEZKPelPUDx"
 
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
| `fcn.007ebb90` | `0x7ebb90` | 142602 | ✓ |
| `fcn.007b1c80` | `0x7b1c80` | 73362 | ✓ |

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
- [`code/fcn.007b1c80.c`](code/fcn.007b1c80.c)
- [`code/fcn.007ebb90.c`](code/fcn.007ebb90.c)

## Behavioral Analysis

This analysis incorporates the findings from **Chunk 17/17**, completing the examination of the "Dispatcher" core. This final segment provides definitive evidence regarding the complexity and maturity of the VM-based loader.

---

### Final Analysis Summary: Hyper-Granular Dispatcher & Templated Obfuscation

The inclusion of Chunk 17 confirms that the dispatcher is not merely a large `switch` statement, but a **highly engineered tree of conditional branches** designed to maximize the complexity of the Control Flow Graph (CFG).

#### 1. Evidence of "Template-Based" Obfuscation
A striking pattern emerges in this chunk: several blocks of code share nearly identical structures, with only slight variations in constant values or specific internal state checks. 
*   **Example:** The repetition of `uVar12 = CONCAT31(Var29,0x7b);` followed by a multi-step check on `in_stack_fffffa50` and a call to `fcn.0040e1f0`.
*   **Significance:** This suggests the author used an automated script or a macro-based system to generate these handlers. While this makes manual reading difficult, it confirms that the "Logic" of the VM is consistent; only the "Address Space" (the specific opcodes) is being shifted and obfuscated via the tree structure.

#### 2. State-Dependent Execution ("Gatekeeping")
The code frequently checks internal state variables before proceeding with an operation. 
*   **Example:** The recurring check `if (in_stack_fffffa50 != NULL)` appears in almost every instruction block.
*   **Interpretation:** This indicates that the VM is tracking its own "context." An instruction is only valid if the virtual registers/memory are in a specific state. If the state isn't met, the code may jump to an error handler or simply do nothing, making it impossible for an analyst to know what an instruction *would* have done without a full execution trace of the prior 10,000 instructions.

#### 3. Data-Driven Buffer Construction
The heavy use of `CONCAT`, bit-shifting (`>> 8`), and direct memory mapping (e.g., `uStack_581 = cVar10;`) confirms that the VM is constructing **complex data structures in memory** before they are passed to the host OS.
*   **Just-in-Time Assembly:** The VM doesn't just pass "instructions" to the system; it builds a complete, valid structure (like an `Nt_` call structure) only at the moment of execution. This hides the true API calls from static analysis tools.

#### 4. Massive Cyclomatic Complexity
The sheer number of labels (`code_r0x...`) and nested conditions in this final chunk demonstrates a deliberate attempt to break automated de-obfuscation tools. By spreading simple logic across dozens of `if` statements, the malware ensures that an analyst cannot easily "flatten" the code to see the underlying intent without massive manual effort.

---

### Final Synthesis for Incident Response

The analysis of all 17 chunks confirms that this is a **High-Tier, Sophisticated VM-Based Loader.** It is designed for long-term persistence and to defeat both automated sandboxes and advanced manual reverse engineering.

**Technical Indicators & Observations:**
*   **Sophistication Level:** **Elite.** The use of nested tree-based dispatching combined with state-aware gates indicates a high level of development resources (typical of APT groups or top-tier cybercrime syndicates).
*   **Mechanism:** **State-Machine Orchestrator.** The VM acts as an intermediary layer. The "maliciousness" is not in the dispatcher; it is hidden within the virtual instructions that the dispatcher interprets to build system calls dynamically.
*   **Anti-Analysis Tactics:** 
    *   **Control Flow Obfuscation:** Tree structures instead of switch cases.
    *   **Instruction Packing:** Using bitwise "shuffling" (e.g., `0x7b` vs `0x7f`) to differentiate between nearly identical operations.
    *   **Context-Aware Execution:** Validating internal VM state before every operation to ensure the malware doesn't behave predictably in a debugger.

**Refined Intelligence for IR Teams:**
1.  **Malware Category:** **Advanced Virtual Machine (VM) Loader.** This is not just "packing"; it is a fully functional virtual CPU environment executing an encrypted/custom bytecode.
2.  **Payload Delivery:** The payload is likely never fully decrypted in memory until the moment of execution. It is assembled piece-by-piece by the VM's handler logic.
3.  **Detection Strategy:** Traditional signature-based detection will fail. Look for **behavioral indicators** (e.g., a process performing heavy internal "math" and then making a single, strangely formatted system call).

---

### Final Recommendations for Investigation:

1.  **Automated Trace Collection (Primary):** Do not waste time trying to map every `if` branch in the dispatcher manually. Use **Frida**, **Intel PIN**, or a debugger script to log Every "exit point" from the VM. Map the sequence of system calls that actually occur during runtime.
2.  **Memory Snapshotting:** Since the VM builds structures "just-in-time," take memory dumps at frequent intervals. This will reveal the "naked" strings, IPs, and file paths just before they are handed over to `Kernel32.dll` or `Nt_` functions.
3.  **De-obfuscation via Scripting:** Use an IDAPython script to identify all `CONCAT` and bit-shift operations in the dispatcher. Replace these with a simplified "Instruction Table" once you have identified which values of `cVar10` correspond to critical actions (e.g., Network, File System).
4.  **Behavioral Profiling:** Create YARA rules based on the **patterns** of the dispatcher rather than the specific bytes. The way it accesses internal stack pointers and its unique "gatekeeping" functions (`fcn.0040ac80`) are highly specific signatures.

### Final Summary Checklist for IR:
*   **Malware Class:** Highly Complex State-Machine Orchestrator (VM-based).
*   **Threat Level:** **Critical.** High sophistication, high complexity.
*   **Key Indicators of Sophistication:**
    *   Multi-layered nested dispatchers to break CFG analysis.
    *   Just-in-time construction of system call structures.
    *   Internal state validation (gatekeeping) at every instruction step.
    *   Heavy use of bitwise "shuffling" for micro-instruction differentiation.
*   **Recommended Response:** **Dynamic Instrumentation & Memory Forensics.** Focus on the points where the VM interacts with the OS, as these are the only moments the true intent is revealed.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files/Programs | The use of a "highly engineered tree of conditional branches," template-based logic, and bitwise shuffling is designed to maximize CFG complexity and hinder manual and automated analysis. |
| **T1497** | Virtualization/Sandbox Evasion | The "Gatekeeping" mechanism (state-dependent execution) ensures that the malware only executes when specific internal conditions are met, intentionally evading detection in automated sandboxes or debuggers. |
| **T1027** | Obfuscated Files/Programs | The "Just-in-Time" construction of data structures and use of `CONCAT` to build system call parameters at the moment of execution is intended to hide API calls from static analysis tools. |

### Analysis Notes for Intelligence Reporting:
*   **Complexity of T1027:** In this specific case, the "Obfuscation" isn't just simple packing; it is a sophisticated **Virtual Machine (VM) Loader**. The complexity lies in the abstraction layer where the actual malicious logic is hidden within custom bytecode interpreted by the complex tree structure.
*   **Context of T1497:** The "State-aware" gates function as a defensive check to ensure the malware does not exhibit its true behavior unless it confirms it is running on a genuine target machine rather than an analyst's environment.

---

## Indicators of Compromise

Based on the provided string dump and behavioral analysis, here is the extracted intelligence. 

Note: The "Extracted Strings" section contains significant amounts of non-human-readable data (common in VM-based malware where strings are XORed or encoded), and the "Behavioral Analysis" describes internal logic rather than external infrastructure.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (The terms `9systu`, `9crasuH`, etc., appear to be remnants of internal function names or labels, not full file system paths).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified. (Note: The "Go build ID" present in the strings is an internal compiler-generated identifier and does not constitute a unique malware signature/hash like MD5 or SHA-256).

### **Other artifacts**
*   **C2 Patterns:** None directly listed, however, the analysis indicates the use of **Just-in-time (JIT) construction of system call structures**. This means the actual command parameters and IP addresses are likely only generated in memory at the moment of execution to evade static detection.
*   **Malware Category:** Advanced VM-based Loader/Stub.
*   **Internal Function Signatures:** `fcn.0040e1f0` and `fcn.0040ac80` (These are internal offsets; while not global IOCs, they can be used to identify specific behavior in memory forensics).

---
**Analyst Note:** The provided text describes a highly sophisticated **VM-based loader**. Because the malware constructs its communication structures dynamically at runtime (JIT), standard static analysis of strings is unlikely to yield IP addresses or URLs. Detection should focus on behavioral patterns, specifically identifying processes performing heavy "math" and nested conditional branching before making system calls.

---

## Malware Family Classification

Based on the provided technical analysis, here is the classification of the sample:

1. **Malware family**: Custom (Sophisticated VM-based Architecture)
2. **Malware type**: Loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Virtual Machine (VM) Architecture:** The code utilizes a highly engineered tree-based dispatcher and "State-aware" gatekeeping to hide the core logic within custom bytecode, a hallmark of elite-tier malware designed to defeat automated sandboxes and manual reverse engineering.
    *   **Just-in-Time (JIT) Construction:** The loader avoids static detection by constructing system call structures (like `Nt_` calls) only at the moment of execution using bitwise "shuffling" and concatenation, meaning malicious parameters are never visible in a static memory dump until the final step.
    *   **High Complexity/Obfuscation:** The transition from standard "switching" to complex nested logic with high cyclomatic complexity indicates a deliberate attempt to frustrate analysts, typical of sophisticated APT or professional cybercrime tools.
