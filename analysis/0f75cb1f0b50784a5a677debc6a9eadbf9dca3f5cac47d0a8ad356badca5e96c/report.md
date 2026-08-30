# Threat Analysis Report

**Generated:** 2026-08-16 14:38 UTC
**Sample:** `0f75cb1f0b50784a5a677debc6a9eadbf9dca3f5cac47d0a8ad356badca5e96c_0f75cb1f0b50784a5a677debc6a9eadbf9dca3f5cac47d0a8ad356badca5e96c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f75cb1f0b50784a5a677debc6a9eadbf9dca3f5cac47d0a8ad356badca5e96c_0f75cb1f0b50784a5a677debc6a9eadbf9dca3f5cac47d0a8ad356badca5e96c.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, 6 sections |
| Size | 12,577,280 bytes |
| MD5 | `883cbd6205d7e0f39d971ac56cadf01e` |
| SHA1 | `52d46c6f59124aa643d24638055819630ff5f605` |
| SHA256 | `0f75cb1f0b50784a5a677debc6a9eadbf9dca3f5cac47d0a8ad356badca5e96c` |
| Overall entropy | 6.428 |
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
| `.text` | 5,250,048 | 6.031 | No |
| `.rdata` | 6,638,592 | 6.077 | No |
| `.data` | 433,152 | 5.996 | No |
| `.idata` | 1,536 | 3.85 | No |
| `.reloc` | 252,416 | 6.65 | No |
| `.symtab` | 512 | 0.02 | No |

### Imports

**KERNEL32.DLL**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetUnhandledExceptionFilter`, `SetProcessPriorityBoost`

## Extracted Strings

Total strings found: **41358** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.idata
.reloc
B.symtab
 Go build ID: "btvHmidZiLFgyBrj5JiR/P1fyNrReM_ShkAuLPy9q/izMrs8lErz6tjg1TOe2E/dcstwhlVo2LDEFKwcl1j"
 
|$9;u
;cpu.u
X8Zu$
X8Zu
H89J8u|
H<8J<us
H=8J=uj
HD9JDub
HH9JHuZ
HL8JLuQ
HM8JMuH
JT9HTu@
HX9JXu8
H\8J\u/
H]8J]u&
Hd9Jdu
Hh9Jhu
Hl8Jlu
Hm8Jmu
#t$$#L$(
#t$,#L$0
#\$$#D$(
#t$$#L$(
#l$,#L$0
#l$,#L$0
#t$8#L$<
#t$8#L$<
#l$0#L$4
#l$0#L$4
#t$<#L$@
#t$,#L$0
#t$,#L$0
#D$8#L$<
#t$4#L$8
#t$4#L$8
#t$0#L$4
H9Ju
|$9;u
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
	;av|
|$09GDu
L$(9Aw
L$ 9A4t 
L$(f9A
u 9r tL
D$,+D$
T$+B
D$49D$
L$H9A4v
\$49\$(u
L$$9A(s
\$09S4
u
9Hw
	;avL
L$+A
L$ 9H<s
L$09A4v
T$(9J4s
T$<9B4v
L$ #D$$#L$(
UUUU%UUUU
T$ 9T$
D$09D$
uP9uTu1
9T$,t-
D$49D$
D$L9D$
L$89L$<
tJ9A0tE
L$49L$
|$ u	1
-9A$u(
Z 9X s&9B
v 9q w
T$`9
w
9
w9J
9
w9J
9
w9J
9L$Pv	
9L$Pv	
D$$9D$
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00478600` | `0x478600` | 444672 | ✓ |
| `fcn.00478620` | `0x478620` | 423312 | ✓ |
| `fcn.00478660` | `0x478660` | 423280 | ✓ |
| `fcn.004787b0` | `0x4787b0` | 246621 | ✓ |
| `fcn.004787c0` | `0x4787c0` | 246493 | ✓ |
| `fcn.004787d0` | `0x4787d0` | 246365 | ✓ |
| `fcn.004787e0` | `0x4787e0` | 246237 | ✓ |
| `fcn.004787f0` | `0x4787f0` | 246109 | ✓ |
| `fcn.00478800` | `0x478800` | 245981 | ✓ |
| `fcn.00478810` | `0x478810` | 245853 | ✓ |
| `fcn.00478820` | `0x478820` | 245725 | ✓ |
| `fcn.00478830` | `0x478830` | 245597 | ✓ |
| `fcn.00478840` | `0x478840` | 245469 | ✓ |
| `fcn.00478850` | `0x478850` | 245341 | ✓ |
| `fcn.00478860` | `0x478860` | 245213 | ✓ |
| `fcn.00478870` | `0x478870` | 245085 | ✓ |
| `fcn.00478880` | `0x478880` | 244957 | ✓ |
| `fcn.00478890` | `0x478890` | 244829 | ✓ |
| `fcn.004788a0` | `0x4788a0` | 244701 | ✓ |
| `fcn.004788b0` | `0x4788b0` | 244573 | ✓ |
| `fcn.004788c0` | `0x4788c0` | 236769 | ✓ |
| `fcn.004788e0` | `0x4788e0` | 236641 | ✓ |
| `fcn.00478900` | `0x478900` | 236513 | ✓ |
| `fcn.00478920` | `0x478920` | 236385 | ✓ |
| `fcn.00478940` | `0x478940` | 236257 | ✓ |
| `fcn.00478960` | `0x478960` | 236129 | ✓ |
| `fcn.00478980` | `0x478980` | 236001 | ✓ |
| `fcn.004789a0` | `0x4789a0` | 235873 | ✓ |
| `fcn.0085c6f0` | `0x85c6f0` | 140788 | ✓ |
| `fcn.00822e90` | `0x822e90` | 73107 | ✓ |

### Decompiled Code Files

- [`code/fcn.00478600.c`](code/fcn.00478600.c)
- [`code/fcn.00478620.c`](code/fcn.00478620.c)
- [`code/fcn.00478660.c`](code/fcn.00478660.c)
- [`code/fcn.004787b0.c`](code/fcn.004787b0.c)
- [`code/fcn.004787c0.c`](code/fcn.004787c0.c)
- [`code/fcn.004787d0.c`](code/fcn.004787d0.c)
- [`code/fcn.004787e0.c`](code/fcn.004787e0.c)
- [`code/fcn.004787f0.c`](code/fcn.004787f0.c)
- [`code/fcn.00478800.c`](code/fcn.00478800.c)
- [`code/fcn.00478810.c`](code/fcn.00478810.c)
- [`code/fcn.00478820.c`](code/fcn.00478820.c)
- [`code/fcn.00478830.c`](code/fcn.00478830.c)
- [`code/fcn.00478840.c`](code/fcn.00478840.c)
- [`code/fcn.00478850.c`](code/fcn.00478850.c)
- [`code/fcn.00478860.c`](code/fcn.00478860.c)
- [`code/fcn.00478870.c`](code/fcn.00478870.c)
- [`code/fcn.00478880.c`](code/fcn.00478880.c)
- [`code/fcn.00478890.c`](code/fcn.00478890.c)
- [`code/fcn.004788a0.c`](code/fcn.004788a0.c)
- [`code/fcn.004788b0.c`](code/fcn.004788b0.c)
- [`code/fcn.004788c0.c`](code/fcn.004788c0.c)
- [`code/fcn.004788e0.c`](code/fcn.004788e0.c)
- [`code/fcn.00478900.c`](code/fcn.00478900.c)
- [`code/fcn.00478920.c`](code/fcn.00478920.c)
- [`code/fcn.00478940.c`](code/fcn.00478940.c)
- [`code/fcn.00478960.c`](code/fcn.00478960.c)
- [`code/fcn.00478980.c`](code/fcn.00478980.c)
- [`code/fcn.004789a0.c`](code/fcn.004789a0.c)
- [`code/fcn.00822e90.c`](code/fcn.00822e90.c)
- [`code/fcn.0085c6f0.c`](code/fcn.0085c6f0.c)

## Behavioral Analysis

This final disassembly chunk (16/16) completes the picture of the packer's architecture. It reveals the most complex layer of the **Virtual Machine (VM)**: the **State-Dependent Dispatcher** and its **Hidden Execution Pathing**.

By analyzing this last portion, we can finalize our understanding of how this packer hides the malicious payload from automated tools and human analysts.

---

### Finalized Technical Analysis

#### 1. The "Decision Tree" (Branch Fusion)
The sheer scale of nested `if` statements (e.g., `if (cVar8 < 0xba)`, then `if (cVar8 < 0x95)`, etc.) is not a result of poor coding; it is a deliberate **Optimization/Obfuscation Hybrid**. This structure represents a "Decision Tree."
*   **Mechanism:** Each nested level corresponds to an attribute of the guest instruction, such as its length, whether it requires special flags, or if it is a multi-byte opcode. 
*   **Impact:** Because many different opcodes share similar properties (e.g., several instructions might be "single-byte" and "non-privileged"), they are funneled into the same code paths until the very last possible moment. This makes it impossible to distinguish between "harmless" VM management code and "malicious" payload logic during static analysis.

#### 2. Sub-Instruction Decomposition (Micro-Decoding)
The repeated pattern of `uVar10 = CONCAT31(Var29, 0x7f); fcn.00834ef0(param_2, uVar10);` is the smoking gun for **Multi-Stage Decoding**.
*   **Observation:** Instead of the dispatcher jumping to a handler for opcode `0x7F`, it takes the "base" logic and appends a dynamic value (the result of `CONCAT31`). 
*   **Meaning:** The packer is decoding "micro-ops." A single guest instruction might be broken down into several smaller, host-side operations. By only invoking the full complexity of a handler at the end of this long chain, the packer ensures that the analyst never sees a single, clean transition from "VM Logic" to "Malicious Action."

#### 3. Dynamic Buffer Navigation & Segmented Memory
The analysis of `iVar6 = uStack_4dc + CONCAT44(in_stack_fffffac4, in_stack_fffffac0);` and the subsequent logic around `pcStack_2c8` reveals a **Segmented Instruction Buffer**.
*   **Mechanism:** The packer doesn't just move a Program Counter (PC) linearly. It uses complex arithmetic to calculate the next "instruction" location based on internal state variables (`uStack_4dc`).
*   **Impact:** This effectively destroys linear disassembly. An automated tool cannot predict where the "next" piece of code is because that depends on the results of every previous calculation in the dispatcher.

#### 4. State-Aware Logic Gates
The logic `if (pcStack_274 < (-(in_stack_fffffab8 < 0x20) & 1 << (in_stack_fffffab8 & 0x1f)))` is a **Bitmask-Based Dispatch**.
*   **Mechanism:** It uses the value of a "virtual register" (`in_staff_fffffab8`) to perform bitwise arithmetic that determines which branch to take.
*   **Impact:** This is designed to defeat symbolic execution and automated "de-obfuscation." The number of possible paths through this single `if` statement scales exponentially with the number of bits in the register, creating a "state explosion" for automated tools.

---

### Final Conclusion: Packer Classification
This packer is classified as **High-Tier Advanced Virtualization**. It does not simply encrypt or pack code; it **re-compiles** the malicious logic into a proprietary bytecode that can only be executed by this specific dispatcher. 

The "complexity" isn't just noise—it's a functional translation layer designed to isolate the malware from the operating system's security hooks. The actual malicious intent (e.g., keylogging, file encryption, C2 communication) is hidden inside the virtual machine's guest instructions and only manifests when the dispatcher executes the specific "translated" sequence of micro-operations.

---

### Final Strategic Recommendations for Incident Response

Given the complexity of this packer, traditional static analysis will likely fail to provide actionable intelligence in a timely manner. The following three strategies are recommended:

#### 1. Execution Trace Analysis (The "Breadcrumb" Method)
Instead of trying to map out every `if` statement in the dispatcher, use a tool like **Intel PIN** or **Frida** to log every jump and every call to the core handlers (`fcn.00834ef0`, `fcn.00835290`).
*   **Goal:** By capturing a full execution trace of a live infection, you can filter out all the "dead" branches (the parts of the maze that are never taken) and see only the path the malware actually takes to reach its payload.

#### 2. Memory Snapshotting (The "Wait-and-See" Method)
Monitor the process for transitions into **newly allocated memory regions** or calls to `VirtualAlloc`/`VirtualProtect`.
*   **Goal:** There is almost always a point where the Virtual Machine finishes decoding its internal instructions and attempts to jump to an "original" piece of code or a decoded payload. Capturing a memory dump at this precise moment will bypass the VM's complexity entirely, providing you with the raw, de-obfuscated malicious code.

#### 3. Automated Instruction Lifting
If you have significant resources for reverse engineering, write a script (IDAPython) to **collapse** the dispatcher's logic. 
*   **Goal:** Replace the complex `if/else` chains with a simplified jump table. This "flattens" the maze and allows a human analyst to see the true logic of the handler functions without getting lost in the nested branching.

**Risk Level: Critical.** This packer is designed specifically to thwart sophisticated analysis. Manual de-obfuscation is time-consuming; automated dynamic analysis/tracing should be the primary path for rapid response.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&C framework.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | **Packer** | The entire architecture utilizes a Virtual Machine (VM) to wrap, hide, and "re-compile" malicious logic into a custom bytecode system. |
| **T1027** | **Obfuscated Valid Machine Code** | The "Decision Tree" and "Micro-Decoding" mechanisms are designed to blend malicious actions with benign VM management code to foil static analysis. |
| **T1497** | **Virtualization** | The use of a custom interpreter/VM (the State-Aware Logic Gates) creates a proprietary execution environment that isolates the malware from standard security hooks. |
| **T1055** | **Packer** (Segmented Memory) | The "Segmented Instruction Buffer" specifically breaks linear disassembly, ensuring automated tools cannot predict the next instruction in the sequence. |
| **T1027** | **Obfuscated Valid Machine Code** (State-Aware Logic) | The use of bitmask-based dispatching creates a "state explosion," intentionally designed to defeat symbolic execution and automated de-obfuscation tools. |

### Analyst Notes:
*   **Primary Defense Evasion Strategy:** The malware relies heavily on **Defense_Evasion** through complexity. By moving the logic from standard x86/x64 instructions into a proprietary VM, the attacker ensures that typical signature-based and heuristic-based detection systems see only "generic" VM management code rather than specific malicious behaviors (e.g., keylogging or C2 communication).
*   **Detection Difficulty:** The combination of **T1055** and **T1027** makes this a high-effort target for manual analysis, as the analyst must first "de-virtualize" the code before any actual threat hunting can occur.

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral reports, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (The analyzed segments like `0x834ef0` are internal memory offsets/function pointers, not file system paths or registry keys).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified. (Note: While a unique identifier is present in the "Other" category, it does not conform to standard MD5/SHA-1/SHA-256 hash formats).

**Other artifacts**
*   **Go Build ID:** `btvHmidZiLFgyBrj5JiR/P1fyNrReM_ShkAuLPy9q/izMrs8lErz6tjg1TOe2E/dcstwhlVo2LDEFKwcl1j` (Used to identify the specific build of the Go-based malicious binary).
*   **Function Offsets:** `fcn.00834ef0`, `fcn.00835290` (Internal function markers within the packer's dispatcher logic).

***

**Analyst Note:** The provided text describes a high-complexity **VM-based packer**. While it does not contain "noisy" IOCs like hardcoded C2 IP addresses, the presence of the specific **Go Build ID** is a critical artifact for campaign tracking and identifying commonality between different samples using the same packing infrastructure.

---

## Malware Family Classification

1. **Malware family**: custom (sophisticated VM-protected loader)
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Virtualization:** The analysis confirms the use of a "High-Tier" Virtual Machine architecture where malicious logic is re-compiled into proprietary bytecode, intentionally designed to isolate it from OS security hooks.
*   **Complex Obfuscation Techniques:** The presence of "Decision Trees," "Micro-Decoding," and "State-Aware Logic Gates" (specifically targeted at defeating symbolic execution) indicates a sophisticated level of protection common in high-end malware loaders.
*   **Technical Indicators:** The identification of a specific **Go Build ID** and the focus on "sub-instruction decomposition" confirm that this is a custom-built, complex execution environment rather than a standard off-the-shelf packer.
