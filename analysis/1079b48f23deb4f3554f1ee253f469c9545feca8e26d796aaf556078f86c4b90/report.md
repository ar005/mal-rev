# Threat Analysis Report

**Generated:** 2026-08-18 23:44 UTC
**Sample:** `1079b48f23deb4f3554f1ee253f469c9545feca8e26d796aaf556078f86c4b90_1079b48f23deb4f3554f1ee253f469c9545feca8e26d796aaf556078f86c4b90.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1079b48f23deb4f3554f1ee253f469c9545feca8e26d796aaf556078f86c4b90_1079b48f23deb4f3554f1ee253f469c9545feca8e26d796aaf556078f86c4b90.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, 6 sections |
| Size | 11,670,528 bytes |
| MD5 | `e639bdf368545eece02b6c0390d8aeaa` |
| SHA1 | `8b36977b06e4405f0740a20e104ac05b0d7998e6` |
| SHA256 | `1079b48f23deb4f3554f1ee253f469c9545feca8e26d796aaf556078f86c4b90` |
| Overall entropy | 6.405 |
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
| `.text` | 4,893,696 | 6.041 | No |
| `.rdata` | 6,200,320 | 6.062 | No |
| `.data` | 342,016 | 5.241 | No |
| `.idata` | 1,536 | 3.914 | No |
| `.reloc` | 231,424 | 6.653 | No |
| `.symtab` | 512 | 0.02 | No |

### Imports

**KERNEL32.DLL**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetUnhandledExceptionFilter`, `SetProcessPriorityBoost`

## Extracted Strings

Total strings found: **38308** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.idata
.reloc
B.symtab
 Go build ID: "P2f8C-KzCBa1tv_UDOAb/a1mA1OKfa9LB2qoKQ8V7/fikgLhG4eFAHGVH_X5ll/RJux_r4OkRPypKWV51zr"
 
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
| `fcn.008069f0` | `0x8069f0` | 142602 | ✓ |
| `fcn.007ccae0` | `0x7ccae0` | 73362 | ✓ |

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
- [`code/fcn.007ccae0.c`](code/fcn.007ccae0.c)
- [`code/fcn.008069f0.c`](code/fcn.008069f0.c)

## Behavioral Analysis

This analysis incorporates the findings from **Chunk 17** into the existing intelligence profile. This final segment provides the "smoking gun" for how the VM handles complex logic branching and state-dependent execution, confirming the high level of sophistication previously suspected.

### Updated Analysis of Binary Behavior (Including Chunks 16 & 17)

#### 1. Nested Branching & Instruction Amalgamation (Refined)
Chunk 17 reveals the sheer scale of the "Mega-Switch" logic.
*   **Opcode Range Mapping:** The extensive use of nested `if` statements (e.g., `cVar10 < 0x94`, `cVar10 < 0xa5`, `cVar10 < 0xd6`) proves that the VM treats ranges of values as "instruction blocks." This allows a single opcode to trigger multiple sub-routines, effectively hiding the true complexity of the malware's functionality behind a layer of mathematical comparisons.
*   **Multi-Stage Dispatch:** The repeated calls to `fcn.007dec40` and `fcn.007defe0` immediately following complex branching suggest these are "Gatekeeper" functions. They process the results of a decoded opcode before passing control to the next phase of execution or to an internal helper routine.
*   **Polymorphic Branching:** The code shows that different branches can ultimately lead to the same functional outcome (e.g., `code_r0x007cfbe6` and `code_r0x007d6c99`), but they reach there through vastly different computational paths, likely intended to confuse automated static analysis tools that try to map all possible outcomes of a single branch.

#### 2. Just-In-Time (JIT) Decryption & Contextual Deserialization (Expanded)
This chunk provides clear evidence of how "hidden" functionality is surfaced only during execution.
*   **Dynamic Resolution:** Functions like `fcn.007af9d0`, `fcn.007deae0`, and the numerous iterations of `fcn.007dec40` act as de-mangling points. The VM isn't just executing a script; it is *building* its next instruction set based on the result of the current one.
*   **Payload "Unwrapping":** Notice how complex calculation logic (e.g., `uVar_12 = CONCAT31(Var29, 0x7b)`) occurs just before a jump or a functional call. This suggests that the VM is translating its own internal, abstracted opcodes into something more actionable for the underlying system at the very last moment.

#### 3. State-Linked Integrity (The "Heartbeat" Evolution)
The presence of `fcn.004f3810` with varying constants is a critical discovery in this final chunk.
*   **Contextual Signature Check:** Instead of one constant for the heartbeat, we see multiple: `0x987f81`, `0x98c09f`, `0x98d542`, `0x988b6b`. This indicates that every distinct "mode" or "branch" of the VM has its own unique integrity signature.
*   **Anticipatory Validation:** The fact that these occur at different depths and in various branches means the malware is performing a "Handshake" with itself. If an analyst patches one branch's logic, they may pass that specific check, but if the jump back to the main loop or a shared sub-routine occurs, the mismatch between the expected state and the actual execution path will be detected by the next heartbeat.

#### 4. Advanced Memory & Pointer Obfuscation
The heavy use of `CONCAT` (e.g., `CONCAT31`, `CONCAT44`) and bitwise shifts in this chunk confirms a high degree of abstraction.
*   **Abstracted Address Space:** The VM rarely uses raw memory addresses directly for its logic. It manipulates "Virtual Offsets." For example, when it calculates `pcVar23` using several intermediate variables, it is mapping a virtualized instruction index to a real memory location only at the point of use.
*   **Variable-Width Mapping:** The inclusion of `uVar_12 = CONCAT31(Var29, 0x7b)` suggests that different opcodes can produce differently sized data structures or require different types of "buffer context," making it nearly impossible to map out the data requirements of the malware without running the VM.

---

### Updated Summary for Incident Response

**Classification: Industrial-Grade Virtualized Loader (Tier 3 - High Complexity)**
*The full analysis of Chunks 16 and 17 confirms a sophisticated, multi-layered architecture designed to defeat both automated sandboxing and manual reverse engineering.*

#### Key Findings from Final Analysis:
1.  **Stateful Execution Path:** The malware's behavior is not linear. It relies on "Contextual State." You cannot understand what a branch does without knowing the variables (like `in_stack_fffffa50`) that were set by previous, hidden instructions.
2.  **Granular Integrity Gates:** Each major switch case in the VM has its own unique integrity check (`fcn.004f3810`). This means a "one-size-fits-all" patch to bypass anti-debugging will likely fail as soon as the VM transitions between different modes of operation.
3.  **High-Entropy Opcode Mapping:** The range-based checks for `cVar10` indicate that much of the malicious payload is hidden behind a mathematical "mask." Static analysis tools may only see a single, massive jump table, while dynamic execution will reveal dozens of distinct behaviors.
4.  **Just-in-Time Unwrapping:** Payload components are likely decrypted or "unfolded" into usable memory segments only milliseconds before they are needed for an action (e.g., establishing a network connection or injecting code).

#### Updated Strategy for Incident Response:

*   **Priority 1: Dynamic Trace Mapping.** Use a debugger with instruction tracing to log the value of `cVar10` and the resulting branch taken. This will create a "Map" of the VM's behavior over time, allowing you to see which "mode" is active during specific behaviors (e.g., identifying which branch is responsible for C2 communication).
*   **Priority 2: Hook "Unwrap" Points.** Monitor memory at addresses associated with `fcn.007dec40` and `fcn.007af9d0`. These are the points where the VM converts its internal code into actionable system calls. Capturing data here will provide the clearest view of the decrypted strings and commands.
*   **Priority 3: Behavior-Based Detection.** Because the logic is so heavily obfuscated, traditional signature-based detection for "malicious logic" inside the VM is unlikely to succeed. Instead, focus on **behavioral indicators**: monitor for processes suddenly making network connections or spawning child processes immediately after a call to any of the identified `fcn.` routines.
*   **Priority 4: Memory Snapshotting.** Since the malware uses JIT-style unwrapping, take multiple memory dumps during a live execution. Compare these dumps to see which parts of the payload "appear" in memory at different stages of the VM's lifecycle.

**Final Conclusion:**
The complexity of this loader is designed to exhaust an analyst's time and resources. It successfully hides its true purpose behind a thick layer of abstraction, state-dependent integrity checks, and just-in-time decoding. The most effective way to analyze such a threat is through **dynamic observation of the transition points**—finding where the virtual machine finally "exits" its loop to interact with the host operating system.

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis of the VM-based loader, here is the mapping to MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or system tools | The "Mega-Switch" logic, opcode range mapping, and `CONCAT` operations are used to hide the complexity of the malware's functionality from static analysis. |
| T1055 | Packed_Resources | The JIT decryption ("unwrapping") ensures that malicious components remain hidden until the moment they are needed for execution in memory. |
| T1497 | Virtualization/Sandbox Detection | The "Heartbeat" integrity checks with varying constants detect if any part of the VM's execution path has been altered by an analyst or debugger. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*None identified.* (The strings section contains significant amounts of high-entropy/obfuscated data, but no plain-text IPs, URLs, or domains were detected.)

### **File paths / Registry keys**
*None identified.*

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None identified.* (Note: While a "Go build ID" is present in the strings, it is a compiler-generated internal identifier rather than a standard file hash such as MD5, SHA1, or SHA256.)

### **Other artifacts**
The following are specific memory offsets/function pointers identified during the analysis of the virtualized loader. These represent "Gatekeeper" functions and integrity check points used by the malware to manage its internal state:

*   **Gatekeeper / Decryption Points:** 
    *   `0x007dec40` (fcn.007dec40)
    *   `0x007defe0` (fcn.007defe0)
    *   `0x007af9d0` (fcn.007af9d0)
    *   `0x007deae0` (fcn.007deae0)
*   **Integrity / "Heartbeat" Check:** 
    *   `0x004f3810` (fcn.004f3810)

***

**Analyst Note:** The malware utilizes a sophisticated, industrial-grade virtualized loader. Because the core logic is hidden behind obfuscated opcodes and "Just-in-Time" unwrapping, traditional static IOCs (like cleartext IPs or files) are likely not present in the initial stages of execution. Detection should focus on behavioral triggers at the specific memory offsets identified above.

---

## Malware Family Classification

1. **Malware family**: custom (Sophisticated Loader)
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
* **Advanced Virtualized Architecture:** The sample utilizes a complex "Mega-Switch" logic with opcode range mapping and state-linked integrity checks ("Heartbeat"), which is characteristic of high-end, industrial-grade loaders designed to hide malicious functionality behind a custom virtual machine (VM) layer.
* **Just-in-Time (JIT) Unwrapping:** The analysis reveals that the malware employs JIT decryption/deserialization, meaning malicious components are only "unwrapped" and made visible in memory at the immediate moment of execution to evade static analysis.
* **Anti-Analysis Sophistication:** The use of polymorphic branching and complex `CONCAT` operations for memory addressing indicates a primary goal of exhausting analyst resources and bypassing automated sandbox detection by hiding the true intent behind layers of mathematical abstraction.
