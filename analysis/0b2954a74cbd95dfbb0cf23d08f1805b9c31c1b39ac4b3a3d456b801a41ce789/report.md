# Threat Analysis Report

**Generated:** 2026-07-25 21:14 UTC
**Sample:** `0b2954a74cbd95dfbb0cf23d08f1805b9c31c1b39ac4b3a3d456b801a41ce789_0b2954a74cbd95dfbb0cf23d08f1805b9c31c1b39ac4b3a3d456b801a41ce789.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b2954a74cbd95dfbb0cf23d08f1805b9c31c1b39ac4b3a3d456b801a41ce789_0b2954a74cbd95dfbb0cf23d08f1805b9c31c1b39ac4b3a3d456b801a41ce789.exe` |
| File type | PE32+ executable for EFI (ROM), x86-64, 3 sections |
| Size | 866,688 bytes |
| MD5 | `3afd4380cd177b86825654fed6d6ad30` |
| SHA1 | `d4d26bc799e6e129702183c029c11b4789d05c8c` |
| SHA256 | `0b2954a74cbd95dfbb0cf23d08f1805b9c31c1b39ac4b3a3d456b801a41ce789` |
| Overall entropy | 6.79 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 717,824 | 6.394 | No |
| `.data` | 126,976 | 7.675 | ⚠️ Yes |
| `.mrdata` | 11,264 | 5.882 | No |

### Exports

`D1DAssemble`, `D1DCompile`, `D1DCompile2`, `D1DCompileFromFile`, `D1DCompressShaders`, `D1DCreateBlob`, `D1DCreateFunctionLinkingGraph`, `D1DCreateLinker`, `D1DDecompressShaders`, `D1DDisassemble`, `D1DDisassemble10Effect`, `D1DDisassemble11Trace`, `D1DDisassembleRegion`, `D1DGetBlobPart`, `D1DGetDebugInfo`, `D1DGetInputAndOutputSignatureBlob`, `D1DGetInputSignatureBlob`, `D1DGetOutputSignatureBlob`, `D1DGetTraceInstructionOffsets`, `D1DLoadModule`, `D1DPreprocess`, `D1DReadFileToBlob`, `D1DReflect`, `D1DReflectLibrary`, `D1DReturnFailure1`, `D1DSetBlobPart`, `D1DStripShader`, `D1DWriteBlobToFile`, `D2DAssemble`, `D2DCompile`, `D2DCompile2`, `D2DCompileFromFile`, `D2DCompressShaders`, `D2DCreateBlob`, `D2DCreateFunctionLinkingGraph`, `D2DCreateLinker`, `D2DDecompressShaders`, `D2DDisassemble`, `D2DDisassemble10Effect`, `D2DDisassemble11Trace`, `D2DDisassembleRegion`, `D2DGetBlobPart`, `D2DGetDebugInfo`, `D2DGetInputAndOutputSignatureBlob`, `D2DGetInputSignatureBlob`, `D2DGetOutputSignatureBlob`, `D2DGetTraceInstructionOffsets`, `D2DLoadModule`, `D2DPreprocess`, `D2DReadFileToBlob`

## Extracted Strings

Total strings found: **797** (showing first 100)

```
!This program cannot be run in DOS mode.$
`.data
.mrdata
UAWAVATVWSH
[_^A\A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVVWSH
[_^A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
E(Hc0H
E(Hc0H
eX[_^A\A]A^A_]
UAWAVAUATVWSPH
H5	B-hH
H5	B-hH
H	B-hH)
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAVVWSH
[_^A^]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAVVWSH
[_^A^]
UAWAVVWSH
[_^A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVATVWSH
[_^A\A^A_]
UAWAVAUATVWSH
1Anl5g
[_^A\A]A^A_]
UAWAVVWSH
[_^A^A_]
UAWAVATVWSH
[_^A\A^A_]
UAWAVVWSH
[_^A^A_]
UAWAVAUATVWSH
lH%<1`
HhipUH
[_^A\A]A^A_]
UAWAVVWSH
ecE~V=Q]
[_^A^A_]
UAWAVATVWSH
[_^A\A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVATVWSH
[_^A\A^A_]
UAWAVVWSH
[_^A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVATVWSH
[_^A\A^A_]
UAVVWSH
[_^A^]
UAWAVVWSH
[_^A^A_]
UAWAVVWSH
[_^A^A_]
UAWAVVWSH
[_^A^A_]
UAVVWSH
[_^A^]
UAVVWSH
[_^A^]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
~n=f$f
	HcI<H
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAVVWSH
[_^A^]
UAVVWSH
[_^A^]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVATVWSH
[_^A\A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVATVWSH
e [_^A\A^A_]
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.18007b6c0` | `0x18007b6c0` | 38272 | ✓ |
| `fcn.18005bca0` | `0x18005bca0` | 25391 | ✓ |
| `fcn.180085e50` | `0x180085e50` | 25017 | ✓ |
| `fcn.18006c430` | `0x18006c430` | 21115 | ✓ |
| `fcn.180042130` | `0x180042130` | 17764 | ✓ |
| `fcn.1800a2b50` | `0x1800a2b50` | 15452 | ✓ |
| `fcn.1800516e0` | `0x1800516e0` | 14326 | ✓ |
| `fcn.18003f260` | `0x18003f260` | 11982 | ✓ |
| `fcn.1800904f0` | `0x1800904f0` | 11753 | ✓ |
| `fcn.180067730` | `0x180067730` | 10565 | ✓ |
| `fcn.18004d370` | `0x18004d370` | 10511 | ✓ |
| `fcn.180006190` | `0x180006190` | 8690 | ✓ |
| `fcn.18004b290` | `0x18004b290` | 8402 | ✓ |
| `fcn.180002170` | `0x180002170` | 8223 | ✓ |
| `fcn.1800951c0` | `0x1800951c0` | 7744 | ✓ |
| `fcn.1800478e0` | `0x1800478e0` | 7686 | ✓ |
| `fcn.180074cb0` | `0x180074cb0` | 6740 | ✓ |
| `fcn.18002c4c0` | `0x18002c4c0` | 6498 | ✓ |
| `fcn.180004bb0` | `0x180004bb0` | 5594 | ✓ |
| `fcn.18006a330` | `0x18006a330` | 5561 | ✓ |
| `fcn.180055c50` | `0x180055c50` | 5498 | ✓ |
| `fcn.180036320` | `0x180036320` | 5490 | ✓ |
| `fcn.18003de00` | `0x18003de00` | 5202 | ✓ |
| `fcn.18001cbd0` | `0x18001cbd0` | 5177 | ✓ |
| `fcn.18008db10` | `0x18008db10` | 4997 | ✓ |
| `fcn.1800652c0` | `0x1800652c0` | 4856 | ✓ |
| `fcn.180024a80` | `0x180024a80` | 4750 | ✓ |
| `fcn.1800466a0` | `0x1800466a0` | 4670 | ✓ |
| `fcn.1800a1220` | `0x1800a1220` | 4664 | ✓ |
| `fcn.18003a750` | `0x18003a750` | 4590 | ✓ |

### Decompiled Code Files

- [`code/fcn.180002170.c`](code/fcn.180002170.c)
- [`code/fcn.180004bb0.c`](code/fcn.180004bb0.c)
- [`code/fcn.180006190.c`](code/fcn.180006190.c)
- [`code/fcn.18001cbd0.c`](code/fcn.18001cbd0.c)
- [`code/fcn.180024a80.c`](code/fcn.180024a80.c)
- [`code/fcn.18002c4c0.c`](code/fcn.18002c4c0.c)
- [`code/fcn.180036320.c`](code/fcn.180036320.c)
- [`code/fcn.18003a750.c`](code/fcn.18003a750.c)
- [`code/fcn.18003de00.c`](code/fcn.18003de00.c)
- [`code/fcn.18003f260.c`](code/fcn.18003f260.c)
- [`code/fcn.180042130.c`](code/fcn.180042130.c)
- [`code/fcn.1800466a0.c`](code/fcn.1800466a0.c)
- [`code/fcn.1800478e0.c`](code/fcn.1800478e0.c)
- [`code/fcn.18004b290.c`](code/fcn.18004b290.c)
- [`code/fcn.18004d370.c`](code/fcn.18004d370.c)
- [`code/fcn.1800516e0.c`](code/fcn.1800516e0.c)
- [`code/fcn.180055c50.c`](code/fcn.180055c50.c)
- [`code/fcn.18005bca0.c`](code/fcn.18005bca0.c)
- [`code/fcn.1800652c0.c`](code/fcn.1800652c0.c)
- [`code/fcn.180067730.c`](code/fcn.180067730.c)
- [`code/fcn.18006a330.c`](code/fcn.18006a330.c)
- [`code/fcn.18006c430.c`](code/fcn.18006c430.c)
- [`code/fcn.180074cb0.c`](code/fcn.180074cb0.c)
- [`code/fcn.18007b6c0.c`](code/fcn.18007b6c0.c)
- [`code/fcn.180085e50.c`](code/fcn.180085e50.c)
- [`code/fcn.18008db10.c`](code/fcn.18008db10.c)
- [`code/fcn.1800904f0.c`](code/fcn.1800904f0.c)
- [`code/fcn.1800951c0.c`](code/fcn.1800951c0.c)
- [`code/fcn.1800a1220.c`](code/fcn.1800a1220.c)
- [`code/fcn.1800a2b50.c`](code/fcn.1800a2b50.c)

## Behavioral Analysis

This analysis incorporates your prior findings and integrates the final set of logic uncovered in **Chunk 31**.

The evidence from this final section confirms that the packer is utilizing a highly sophisticated **Virtualized Execution Environment** where the "real" logic is stripped away, replaced by a massive dispatcher tree designed to exhaust human patience and automated analysis tools.

---

### Updated Analysis of Code Behavior (Chunks 30 & 31)

#### 1. Massive Dispatcher Expansion (The "Switch-Case" Forest)
In Chunk 31, we see the full realization of the `iVar17` comparison tree. Instead of a standard jump table or a simple switch statement, the packer uses a massive chain of nested `if/else` blocks to handle different "instructions."
*   **Observation:** The sequence of comparisons (`iVar17 == 0x909631b`, `iVar17 == 0x78bde943`, `iVar17 == 0x72ed416b`, etc.) indicates that each unique constant is a distinct **opcode** within the custom VM.
*   **The Intent:** By using nested if-statements instead of a jump table, the compiler/obfuscator forces an analyst to step through every single possibility or manually map out dozens of branch points just to find the logic for a single operation.

#### 2. Complex Branch Protection (Advanced Opaque Predicates)
Chunk 31 contains some of the most aggressive "mathematical noise" seen in the entire disassembly.
*   **Observation:** Look at expressions like: `(((*0x1800d9bd0 + 1U + *0x1800d9bd0) - (*0x1800d9bd0 + 1U & 1)) * 3 + 0x8) * *0x1800d9bd0 & 1`.
*   **The Intent:** This is a masterclass in **Opaque Predicates**. To an automated tool (like a symbolic executor), this looks like a complex mathematical problem that needs solving. To a human, it's a nightmare to calculate manually. In reality, these expressions almost always resolve to a constant (0 or 1) based on the properties of even/odd numbers, but they are designed to make "simplification" by a tool nearly impossible without a specialized solver.

#### 3. State-Machine Context Update
Several blocks in Chunk 31 (specifically those involving `puStack_70` and `puStack_80`) show the packer updating its internal state machine.
*   **Observation:** The constant `0x32` appears repeatedly as a result of complex calculations or direct assignments within different "handler" branches. This value likely represents an internal pointer or status flag that tells the VM how to interpret the *next* piece of data it reads.
*   **The Intent:** By breaking a single logical operation (e.g., "add two numbers") into multiple state transitions across different handler blocks, the packer ensures that no single chunk of code contains enough information for an analyst to understand the full operation.

#### 4. Junk Loop Injection (Tarpits)
The `do...while` loops in Chunk 31 contain very little meaningful logic but are heavily decorated with "junk" calculations.
*   **Observation:** The loop conditions, such as `((9 < *0x1800d9f24) || ...)` combined with complex bitwise arithmetic, serve no purpose other than to stall the analyst.
*   **The Intent:** These are **Tarpits**. They force a debugger to hit multiple "check" points and force an automated tracer to record thousands of unnecessary instructions, making it incredibly difficult to isolate the actual execution path.

---

### Updated Summary for Incident Response (IR)

The final chunks confirm that this is not just a packer; it is a **Hardened Virtual Machine Environment**. The logic is "flattened," and the control flow is intentionally obscured by a massive, nested dispatcher tree.

**New Technical Insights:**
*   **Opcode Mapping:** Every large constant (e.g., `0x909631b`, `0x7cf993cf`) represents an internal instruction. If you find these in the code, they are the "key" to identifying different behaviors of the packer.
*   **Execution Flattening:** The code uses a technique where all "real" logic is moved into small blocks that are called by a central dispatcher. This makes it nearly impossible to see the "big picture" through static analysis.
*   **Symbolic Execution Resistance:** The use of complex bitwise/arithmetic gates in jump conditions (e.g., `(uVar14 ^ 0x80eea36) & uVar14`) is specifically designed to break tools like Triton or Manticore by forcing them to explore "phantom" paths that never actually execute.

**Actionable Intelligence for IR Team:**
1.  **Identify the Dispatcher Hub:** Focus on the location of `iVar17`. This variable acts as the "Instruction Pointer" for the VM. Mapping out the values it can take will reveal the full scope of the packer's capabilities.
2.  **Trace State Changes:** Instead of trying to understand the math in `do...while` loops, let the code run and log the changes to the **Stack/Context Block** (the memory referenced by `puStack_`). The "real" data is what flows through those buffers.
3.  **Use Constant Folding for De-obfuscation:** If using a tool like IDAPython or Ghidra Scripts, create a pass that identifies and simplifies the bitwise/arithmetic junk (e.g., `((x+1)*2) & 1` becomes `x % 2`). This can "prune" the tarpits from the disassembly.
4.  **Hook Instruction Fetches:** Since the VM is based on a central dispatcher, set a breakpoint at the beginning of the `if(iVar17 == ...)` chain. Every time it hits, log the value of `iVar17`. This will give you a "map" of which instructions are actually being used by the malware during execution.

---

### Updated Technical Indicators
*   **Technique: Control Flow Flattening (CFF).** (Breaking up logic into a series of branches controlled by a central dispatcher.)
*   **Technique: Custom Virtual Machine (VM) Execution.** (Translating original x86 instructions into a custom, nested set of opcodes.)
*   **Technique: Advanced Opaque Predicates.** (Using complex bitwise/arithmetic math to hide simple jump conditions from automated tools.)
*   **Technique: Instruction Handler Fragmentation.** (Splitting one logical operation into multiple handler calls that update a shared "Context" block.)

---

### Final Consolidated Summary of Evidence (Chains 1–31)
The packer is a **High-Complexity Virtual Machine Environment** designed for maximum resilience. Its architecture can be summarized as follows:
1.  **Nested Gatekeeper Dispatcher:** A massive, multi-layered "if-tree" that translates raw data into machine actions while hiding the transition logic in layers of math.
2.  **Execution Shadowing:** The real malicious intent is hidden inside a "shadow" logic—the analyst sees the VM's mechanics, but rarely the actual payload until it is unpacked into memory at the final stage.
3.  **Context-Driven State Machine:** The "state" of the packer is maintained in separate buffer structures (like `puStack`), ensuring that no single function contains enough information to be easily reverse-engineered.
4.  **Automated Tool Immunity:** By using complex, non-linear arithmetic for jump logic, it creates a "combinatorial explosion" for symbolic execution engines, forcing the analyst to perform manual, labor-intensive work.

**Final Recommendation for IR:** 
Do not attempt to statically de-obfuscate the math. The packer is designed to make that path impossible. Instead, **dynamically instrument the Dispatcher**. By capturing the values of `iVar17` and the contents of the `puStack_` buffers during execution, you can bypass the "Tarpits" and see exactly what the malware is doing in real-time.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Execution (Control Flow Flattening) | The use of a massive "switch-case" forest and nested `if/else` blocks hides the true logic path from analysts. |
| T1027 | Obfuscated Execution (Opaque Predicates) | Complex mathematical expressions are used to mask simple jump conditions, making it difficult for automated tools to resolve code paths. |
| T1027 | Obfuscated Execution (Custom Virtual Machine) | The packer utilizes a custom instruction set and opcode mapping (e.g., `iVar17` constants) to hide the actual payload execution logic. |
| T1027 | Obfuscated Execution (Junk Code/Tarpits) | Meaningless loops and heavy arithmetic are injected specifically to stall human analysts and force automated tools to process redundant data. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** The "EXTRACTED STRINGS" section consists primarily of obfuscated data and junk noise characteristic of a virtualized execution environment; no actionable infrastructure IOCs (such as IPs or URLs) were present in those raw strings.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified (The hex values found in the analysis are internal VM opcodes, not file hashes).

### **Other artifacts**
*   **VM Opcode Constants:** The following constants were identified as specific "opcodes" within the custom virtual machine's dispatcher:
    *   `0x909631b`
    *   `0x78bde943`
    *   `0x72ed416b`
    *   `0x7cf993cf`
*   **Internal State/Flag Constants:** 
    *   `0x32` (Identified as a repeated state-machine transition value).
*   **Tactic/Technique Identifiers (for YARA/Sigma rules):**
    *   **Control Flow Flattening (CFF):** Implementation of a "Switch-Case" forest to hide logic.
    *   **Custom VM Execution:** Translation of x86 instructions into a proprietary, nested instruction set.
    *   **Opaque Predicates:** Use of complex bitwise/arithmetic math (e.g., `(uVar14 ^ 0x80eea36) & uVar14`) to break symbolic execution and automated analysis.
    *   **Instruction Handler Fragmentation:** Breaking single logical operations into multiple state-update steps.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for this sample:

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High (Regarding its functionality and construction)
4. **Key evidence**:
    *   **Virtualized Execution Environment:** The sample utilizes a sophisticated custom VM architecture where core logic is replaced by a "switch-case" forest of opcodes (e.g., `0x909631b`). This is a hallmark of high-end, custom-built protectors designed to shield the primary payload from static analysis.
    *   **Advanced Anti-Analysis Defenses:** The presence of "Tarpits" (junk loops), complex opaque predicates to thwart symbolic execution (Triton/Manticore), and instruction fragmentation indicates a professional level of obfuscation intended to exhaust both human researchers and automated tools.
    *   **Control Flow Flattening:** By using a central dispatcher to manage state-machine updates, the malware ensures that no single code block contains enough information to reveal its true purpose without dynamic instrumentation, which is characteristic of advanced loaders used to deliver secondary payloads (such as ransomware or RATs).
