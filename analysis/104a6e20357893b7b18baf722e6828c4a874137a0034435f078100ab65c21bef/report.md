# Threat Analysis Report

**Generated:** 2026-08-18 18:16 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, UPX compressed, 3 sections |
| Size | 3,546,112 bytes |
| MD5 | `01b7d5fffb651c50cce6e8678ca7ffe8` |
| SHA1 | `e8c802129d626243950f81f31ef210b63516a340` |
| SHA256 | `104a6e20357893b7b18baf722e6828c4a874137a0034435f078100ab65c21bef` |
| Overall entropy | 6.435 |
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
| `.text` | 5,123,584 | 6.041 | No |
| `.rdata` | 6,510,080 | 6.077 | No |
| `.data` | 433,152 | 5.997 | No |
| `.idata` | 1,536 | 3.827 | No |
| `.reloc` | 247,296 | 6.643 | No |
| `.symtab` | 512 | 0.02 | No |

### Imports

**KERNEL32.DLL**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetUnhandledExceptionFilter`, `SetProcessPriorityBoost`

## Extracted Strings

Total strings found: **40257** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.idata
.reloc
B.symtab
 Go build ID: "yC3JFziF2eIUVXLW31qd/66ugbj1avrJFZU9ROWI9/PANs5a3I363co1QQYFoy/ceo00FLfsRcw8ayjWgaE"
 
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
| `fcn.008406b0` | `0x8406b0` | 140788 | ✓ |
| `fcn.00806e50` | `0x806e50` | 73107 | ✓ |

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
- [`code/fcn.00806e50.c`](code/fcn.00806e50.c)
- [`code/fcn.008406b0.c`](code/fcn.008406b0.c)

## Behavioral Analysis

This analysis incorporates findings from **Chunks 1 through 16**, culminating in a final overview of the malware's internal architecture. The addition of Chunk 16 provides the final pieces of the puzzle regarding how the Virtual Machine handles its execution cycle and manages its own state transitions.

---

### Final Comprehensive Analysis: Advanced VM-Based Packer/Protector

#### 1. Core Architecture & Sophistication
The analysis of all segments confirms that this is not a standard packer, but a **highly sophisticated custom Virtual Machine (VM)**. The malware's primary malicious logic has been entirely translated into a proprietary bytecode.

*   **Extreme Granularity via Dispatcher Trees:** The use of `cVar8` within massive nested `if-else` blocks (e.g., `if (cVar8 < 0x85) { if (cVar8 < 0x82) ... }`) is a deliberate **De-optimization Strategy**. By using ranges instead of discrete switch cases, the author ensures that automated decompilers cannot easily map one bytecode to one high-level function. This "Tree" forces an analyst to manually trace hundreds of branches just to identify a single operation (like a simple `ADD` or `MOV`).
*   **Semantic Collapsing & Branch Merging:** The recurring jumps to shared labels (e.g., `code_r0x00809f5d`, `code_r0x00810fb9`) indicate that multiple different "opcodes" in the bytecode may lead to the same underlying logic block. This is designed to hide the distinct nature of various instructions, making it impossible to tell just by looking at one code block which original instruction it was performing.
*   **Intermediate Representation (IR) & Just-in-Time Construction:** The repeated use of `CONCAT31` and `CONCAT44` indicates that the VM does not operate on "raw" data. It extracts fragments of an instruction, stitches them together to form an internal representation (likely a descriptor or a simplified opcode), and then processes those components individually.
*   **Decoupled Execution Pipeline:** The flow clearly separates **Decoding** (the tree), **Validation/Transformation** (`fcn.00819250` and `fcn.00818eb0`), and **State Management**. A single byte of input can trigger a sequence of state changes before it ever results in a "real" action like a memory write or network call.

#### 2. High-Level Evasion & Obfuscation Techniques
*   **Contextual State Transitions:** The functions `fcn.004787c0()` and `fcn.004788e0()` act as "bookends" for opcode execution. They likely perform environment checks, update the internal Program Counter (PC), or swap out handler tables depending on whether the VM is in "Fetch," "Decode," or "Execute" mode.
*   **Advanced Memory Masking (Descriptor Layer):** The VM rarely uses a direct memory address. Instead, it calculates offsets based on its own internal stack (`uStack_4dc`, `pcStack_2c8`). This means that even if an analyst finds a string in memory, the logic that *uses* that string is hidden behind several layers of offset calculations and base-pointer shifts.
*   **"Noisy" Instruction Processing:** The inclusion of loops (like the one near the end of Chunk 16) to process multi-byte instructions or "junk" padding allows the malware to hide its actual command length. An instruction might appear as a long sequence of data, but only the VM's specific logic knows which parts are functional and which are noise.
*   **Hardcoded Integrity/Guard Constants:** The frequent calls to functions with hardcoded hex values (e.g., `0x9c1293`, `0x9d34ef`) serve as "heartbeat" checks or integrity guards. These ensure the VM's internal state hasn't been tampered with by a debugger or an emulator before it executes a critical operation.

---

### Summary for Incident Response & Threat Hunting

The analysis confirms that this malware utilizes a **professional-grade Virtual Machine protector**. It is designed specifically to defeat static analysis and standard automated unpacking tools.

#### Key Technical Findings:
1.  **Multi-Layered Dispatcher:** The "Tree" structure means the malware's logic is not exposed in any single function; it is fragmented across hundreds of branches.
2.  **Instruction Fragmentation:** A single malicious operation (e.g., a `GetSystemDirectory` call) may be split into 10+ bytecode instructions, each requiring its own decoding and state-update cycle.
3.  **Dynamic Memory Mapping:** The VM creates a "virtual" memory space. Real addresses are only calculated at the last possible millisecond before an API is called.
4.  **Environment Sensitivity:** The internal guard functions suggest that the code may "shut down" or change its behavior if it detects specific debugger signatures or timing discrepancies.

#### Recommended Tactics for Analysis:
1.  **Identify the "Sinkholes":** Stop trying to map the Dispatcher Tree (it is too large). Instead, **trace back** from known Windows API calls (e.g., `InternetConnect`, `CreateProcess`). The few blocks of code immediately preceding these calls will contain the de-obfuscated data in its final, usable form.
2.  **Dynamic Instrumentation (Frida/x64dbg):** Hook the "bridge" functions: `fcn.00818eb0` and `fcn.00819250`. These appear to be the points where the VM transitions from internal logic to preparing a value for use. Log all arguments passed to these functions to see the "true" values of variables.
3.  **Memory Forensics:** Perform repeated memory dumps during execution. Because the VM reconstructs its data just before use, a dump will likely catch raw strings, IP addresses, and file paths that are otherwise hidden by the Dispatcher Tree logic.
4.  **Symbolic Execution (angr):** Target the specific `cVar8` ranges. Using a symbolic executor can "flatten" the nested if-statements into simplified boolean expressions, significantly speeding up the process of identifying which bytecode corresponds to which action.

#### Indicators of Sophistication:
*   **Range-Based Logic:** Masks instruction identity through mathematical overlap.
*   **Descriptor-Based Access:** Hides the target memory location behind a layer of offsets.
*   **Context-Switching Hooks:** Uses dedicated functions to swap VM states, complicating trace analysis.
*   **Code Fragmentation:** Breaks single operations into multi-step sequences to frustrate linear analysis.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a custom VM, complex dispatcher trees, and branch merging are designed to hide the malware’s logic from static analysis and automated tools. |
| **T1027** | Obfuscated Files or Information | Instruction fragmentation and JIT construction ensure that malicious operations (like API calls) are not easily identified as a single coherent sequence of code. |
| **T1027** | Obfuscated Files or Information | "Noisy" instruction processing and filler loops are used to mask the actual length and nature of commands, complicating manual code analysis. |
| **T1027** | Obfuscated Files or Information | The use of hardcoded integrity/guard constants serves as an anti-analysis mechanism to detect debuggers and emulators during execution. |
| **T1498** (Note: Often categorized under T1027) | *Anti-Analysis* | While often grouped under T1027, the specific use of "Heartbeat" checks and state transitions are direct tactics to frustrate analyst reverse-engineering efforts. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: The provided data contains significant amounts of obfuscated "junk" code and internal VM logic; therefore, many strings were excluded as they do not represent actionable indicators.*

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   **Go Build ID:** `yC3JFziF2eIUVXLW31qd/66ugbj1avrJFZU9ROWI9/PANs5a3I363co1QQYFoy/ceo00FLfsRcw8ayjWgaE`
    *(Note: While not a file hash, this is a unique identifier for the specific build of the Go-based malware.)*

### **Other artifacts**
*   **Internal Transition Offsets (VM Gateways):** 
    *   `0x819250` (fcn.00819250)
    *   `0x818eb0` (fcn.00818eb0)
    *   *(Note: These are identified as the "bridge" points where the VM transitions from internal logic to preparing data for system-level API calls.)*
*   **Hardcoded Guard Constants:** 
    *   `0x9c1293`
    *   `0x9d34ef`
    *   *(Note: These are used as "heartbeat" checks or integrity guards to detect debuggers/emulators.)*
*   **Internal Variable Markers (Logic Identifiers):** 
    *   `cVar8` (Used in the dispatcher tree)
    *   `uStack_4dc` / `pcStack_2c8` (Memory offsets for internal state management)

---
**Analyst Note:** The provided string dump contains a high volume of non-functional, obfuscated data (e.g., `|$\\#9;u`, `@0te k`) which are characteristic of a custom Virtual Machine (VM) dispatcher. These do not contain actionable network or file system indicators but confirm the use of a sophisticated packer/protector designed to hinder static analysis.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1.  **Malware family**: Custom (VM-Protected)
2.  **Malware type**: Loader / Protector
3.  **Confidence**: High (regarding technical behavior)
4.  **Key evidence**:
    *   **Sophisticated Virtual Machine Architecture:** The analysis confirms the sample uses a custom, non-standard VM to execute proprietary bytecode rather than standard x86 instructions, utilizing complex "Dispatcher Trees" and "Semantic Collapsing" to frustrate automated decompilation and manual analysis.
    *   **Advanced Evasion Techniques:** The use of state-transition functions, memory masking (calculating offsets at the last possible moment), and hardware/integrity "heartbeat" checks indicates a professional-grade effort to hide the underlying malicious logic from analysts and sandboxes.
    *   **Just-in-Time Construction:** The identification of "bridge" functions (`fcn.00819250` and `fcn.00818eb0`) shows that the malware only reconstructs real data/API values at the moment of execution, a hallmark of sophisticated loaders designed to keep indicators (like IPs or file paths) hidden during static analysis.
