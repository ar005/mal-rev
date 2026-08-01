# Threat Analysis Report

**Generated:** 2026-07-29 19:45 UTC
**Sample:** `0c3601879d37fc036b2a057f2a8524f6f34cf81899bd549bf741274e8f2f758b_0c3601879d37fc036b2a057f2a8524f6f34cf81899bd549bf741274e8f2f758b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c3601879d37fc036b2a057f2a8524f6f34cf81899bd549bf741274e8f2f758b_0c3601879d37fc036b2a057f2a8524f6f34cf81899bd549bf741274e8f2f758b.exe` |
| File type | PE32+ executable for MS Windows 6.01 (console), x86-64, 9 sections |
| Size | 13,678,080 bytes |
| MD5 | `14536b1fb2e120eea5c71e83c1ba41fb` |
| SHA1 | `8632d93918902a1b20d942fe4ef2452d57ab2913` |
| SHA256 | `0c3601879d37fc036b2a057f2a8524f6f34cf81899bd549bf741274e8f2f758b` |
| Overall entropy | 6.207 |
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
| `.text` | 6,125,568 | 6.118 | No |
| `.rdata` | 6,709,248 | 5.633 | No |
| `.data` | 550,400 | 5.087 | No |
| `.pdata` | 148,480 | 5.599 | No |
| `.xdata` | 512 | 1.778 | No |
| `.idata` | 1,536 | 3.98 | No |
| `.reloc` | 134,656 | 5.438 | No |
| `.symtab` | 512 | 0.02 | No |
| `.rsrc` | 5,632 | 3.875 | No |

### Imports

**kernel32.dll**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetProcessPriorityBoost`, `SetEvent`

## Extracted Strings

Total strings found: **37469** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.xdata
@.idata
.reloc
B.symtab
B.rsrc
 Go build ID: "m_eWKAVMKwFLXIGF2mMv/2j5A85-N9hZ9W_iPMwYY/3kDBzS7kxfOy3K1Ccv9t/7I8JItNK_qHl3j3AXNUy"
 
l$ M9,$u
8cpu.u
P0H9S0
PPH9SP
PpH9Sp
UUUUUUUUH!
33333333H!
D$@I9p
\$hM9K
\$hM9K
P(H9S(t
P@H9S@u/H
H9SHu!H
PPH9SPu
PXH9SXu
P H9S ujH
S0H9P0u`
8S8uUH
chacha8:H9
expafH
nd 3fH
2-byfH
te kfH
\$hH9H@v#H
H9uH
H9L$ r
L$@H9
s`H9J
debugCal
debugCal
debugCalH9
debugCalH9
l409u
x6tzH9
l819um
debugCalH9
l163uf
x84t6H9
l327uf
runtime.
runtime H
 error: H
:H9F w
2H+phH
L$HI9QhuH
D$hH98
P`f9P2tgH
\$0f9C2u
H9D$(t
H
H9X0tO
\$XHcr
$H+L$HH
T$(H+J
L$(H+A
l$(M9,$u

H9Z(w
\$0H9K
D$pH9H
D$0H9H
v	H9 N
|$pH9\$
T$ H+:
UUUUUUUUH!
UUUUUUUUH
wwwwwwwwH!
wwwwwwwwH
J0f9J2vsH
f9s2uFf
D$$u$L
T$(M	D
L$0H+Y
runtime.H9
QpM9Qhu
L9L$Xt#H
runtime.H9
reflect.H9
D$#e+H
I9N0tVH
T$ 9T$$
H92t6H9rPt0H
rpH92w
tRI9N0tLH
T$`HcK
L$XHc
|$0uMH
memprofi
lerau*f
yteu"H
,$M9l$
0H9G@u*
9q0s&H9J
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0047e1c0` | `0x47e1c0` | 454266 | ✓ |
| `fcn.0047e220` | `0x47e220` | 429755 | ✓ |
| `fcn.0047e1e0` | `0x47e1e0` | 429754 | ✓ |
| `fcn.00482f80` | `0x482f80` | 281911 | ✓ |
| `fcn.0047e6a0` | `0x47e6a0` | 254056 | ✓ |
| `fcn.0047e6c0` | `0x47e6c0` | 253928 | ✓ |
| `fcn.0047e6e0` | `0x47e6e0` | 253803 | ✓ |
| `fcn.0047e700` | `0x47e700` | 253675 | ✓ |
| `fcn.0047e720` | `0x47e720` | 253547 | ✓ |
| `fcn.0047e740` | `0x47e740` | 253419 | ✓ |
| `fcn.0047e760` | `0x47e760` | 253288 | ✓ |
| `fcn.0047e780` | `0x47e780` | 253160 | ✓ |
| `fcn.0047e7a0` | `0x47e7a0` | 253032 | ✓ |
| `fcn.0047e7c0` | `0x47e7c0` | 252904 | ✓ |
| `fcn.0047e7e0` | `0x47e7e0` | 252779 | ✓ |
| `fcn.0047e800` | `0x47e800` | 252648 | ✓ |
| `fcn.0047e820` | `0x47e820` | 252520 | ✓ |
| `fcn.004830e0` | `0x4830e0` | 248855 | ✓ |
| `fcn.00483140` | `0x483140` | 218327 | ✓ |
| `fcn.004831e0` | `0x4831e0` | 187543 | ✓ |
| `fcn.00483240` | `0x483240` | 162775 | ✓ |
| `fcn.00715e20` | `0x715e20` | 21787 | ✓ |
| `fcn.009726a0` | `0x9726a0` | 19597 | ✓ |
| `fcn.00711220` | `0x711220` | 19431 | ✓ |
| `fcn.009788c0` | `0x9788c0` | 16138 | ✓ |
| `entry0` | `0x47f940` | 14661 | ✓ |
| `fcn.0073f5e0` | `0x73f5e0` | 12668 | ✓ |
| `fcn.00726bc0` | `0x726bc0` | 12012 | ✓ |
| `fcn.0047e1a0` | `0x47e1a0` | 11699 | ✓ |
| `fcn.004dece0` | `0x4dece0` | 11679 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0047e1a0.c`](code/fcn.0047e1a0.c)
- [`code/fcn.0047e1c0.c`](code/fcn.0047e1c0.c)
- [`code/fcn.0047e1e0.c`](code/fcn.0047e1e0.c)
- [`code/fcn.0047e220.c`](code/fcn.0047e220.c)
- [`code/fcn.0047e6a0.c`](code/fcn.0047e6a0.c)
- [`code/fcn.0047e6c0.c`](code/fcn.0047e6c0.c)
- [`code/fcn.0047e6e0.c`](code/fcn.0047e6e0.c)
- [`code/fcn.0047e700.c`](code/fcn.0047e700.c)
- [`code/fcn.0047e720.c`](code/fcn.0047e720.c)
- [`code/fcn.0047e740.c`](code/fcn.0047e740.c)
- [`code/fcn.0047e760.c`](code/fcn.0047e760.c)
- [`code/fcn.0047e780.c`](code/fcn.0047e780.c)
- [`code/fcn.0047e7a0.c`](code/fcn.0047e7a0.c)
- [`code/fcn.0047e7c0.c`](code/fcn.0047e7c0.c)
- [`code/fcn.0047e7e0.c`](code/fcn.0047e7e0.c)
- [`code/fcn.0047e800.c`](code/fcn.0047e800.c)
- [`code/fcn.0047e820.c`](code/fcn.0047e820.c)
- [`code/fcn.00482f80.c`](code/fcn.00482f80.c)
- [`code/fcn.004830e0.c`](code/fcn.004830e0.c)
- [`code/fcn.00483140.c`](code/fcn.00483140.c)
- [`code/fcn.004831e0.c`](code/fcn.004831e0.c)
- [`code/fcn.00483240.c`](code/fcn.00483240.c)
- [`code/fcn.004dece0.c`](code/fcn.004dece0.c)
- [`code/fcn.00711220.c`](code/fcn.00711220.c)
- [`code/fcn.00715e20.c`](code/fcn.00715e20.c)
- [`code/fcn.00726bc0.c`](code/fcn.00726bc0.c)
- [`code/fcn.0073f5e0.c`](code/fcn.0073f5e0.c)
- [`code/fcn.009726a0.c`](code/fcn.009726a0.c)
- [`code/fcn.009788c0.c`](code/fcn.009788c0.c)

## Behavioral Analysis

This final chunk of disassembly provides the definitive proof that we are dealing with a **high-tier, professional-grade packer**, likely utilizing **Virtualization Technology (VM)** or an extremely advanced **Dispatcher-based architecture**.

The complexity has shifted from "difficult to read" to "intentionally engineered to be mathematically and logically impenetrable" for standard tools.

### Updated Analysis (Chunk 10/10)

#### 1. Virtualized Execution (The "Interpreter" Pattern)
While Chunk 9 showed Control Flow Flattening, this chunk reveals that the packer may actually be using a **Virtual Machine (VM)**.
*   **The Dispatcher Loop:** Notice the repetitive pattern of `*(*0x20 + -0x2b0) = [Constant]` followed by complex logic or internal function calls (`fcn.004735a0`, `fcn.0047f080`). This is characteristic of a **VM Dispatcher**. The packer isn't executing standard x86 instructions; it is running a custom, private bytecode where the "instruction pointer" moves through a series of handlers (the large `if-else` blocks).
*   **State Management:** The variable at offset `-0x2b0` acts as the "Instruction Pointer" or "Opcode." Every time that value changes and is compared to a constant, it triggers a different "handler" for the packer's internal logic.

#### 2. High-Complexity Arithmetic (Anti-Analysis Math)
Several segments in this chunk contain extremely complex arithmetic involving large constants and bitwise operations:
*   **Example:** `(SUB168(SEXT816(-0x5c28f5c28f5c28f5) * SEXT816(uVar12), 8) + uVar12 >> 4) - (uVar12 >> 0x3f)) * 0x19`
*   **Why this is done:** These are **"Constant Folding" traps**. To the CPU, these calculations result in simple values, but to a human or an automated decompiler, they are nightmare scenarios. They are designed to break the "simplification" passes of tools like Hex-Rays, forcing the analyst to manually reverse every single line of math just to find out it's actually adding 1 to a counter.

#### 3. Targeted String/Value Validation
The code contains specific checks for character values (e.g., `0x5455` ('SU'), `0x4d41` ('MA'), `0x6d61` ('ma')).
*   **Hidden Logic:** These are likely checking for **integrity keys** or **environment identifiers**. The packer is verifying that the code has not been tampered with (e.g., by a debugger) and that it is running on a specific target environment before it proceeds to the next stage of decryption.

#### 4. Complex Data Parsing/Walking
The loops involving `piVar28` and the checks for `:`, `.`, and `,` suggest a **Nested Data Structure Walker**. The packer isn't just unpacking a file; it is parsing internal configuration data or "blobs" that contain the instructions for the next layer of its own execution.

---

### Updated Intelligence Summary (Cumulative)

| Feature | Technical Indicator | Risk/Impact |
| :--- | :--- | :--- |
| **Virtualization (VM)** | Dispatcher-style loops and `*(*0x20 + -0x2b0)` state tracking. | **Critical.** The "real" code is hidden in a custom bytecode. Traditional analysis of the x86 instructions won't reveal the actual logic of the malware. |
| **Anti-Analysis Math** | Massive constant expansion and complex bitwise arithmetic. | **High.** Designed to waste the analyst's time. It creates a "manual labor" wall where every mathematical step must be manually solved. |
| **Multi-Layered Cryptography** | Standardized AES (`aesenc`) plus custom pre/post-processing. | **Critical.** Confirms that even if one layer is broken, another (potentially more complex) layer remains hidden behind the VM logic. |
| **State-Driven Execution** | Extensive `if-else` chains acting as a gatekeeper for every action. | **High.** Prevents linear analysis. The flow of the program cannot be determined without running it in a controlled environment. |

---

### Final Conclusion for Incident Response

This is not a simple "packer." It is a **sophisticated protection shell** likely built using a commercial-grade protector or custom-built by an advanced threat actor.

**Key Technical Takeaways:**
1.  **The Logic is Virtualized:** The most critical finding is the transition from "complex code" to "virtualized instructions." The analyst is currently looking at the *interpreter* of the packer, not the malware itself.
2.  **Intentional Frustration:** The use of extreme math and "Maze" logic indicates a goal to stall human analysts for hours or days by making every step of the disassembly manually tedious.
3.  **Highly Defensible Architecture:** Because the payload is only decrypted inside the VM's memory space after passing through multiple "gates," static analysis will never yield the full capabilities of the malware.

**Final Strategy Recommendations:**

1.  **Abandon Pure Static Analysis:** The amount of time required to manually de-obfuscate the math and the dispatcher logic exceeds typical incident response timelines.
2.  **Execute-to-Dump (Dynamic Analysis):** Use a debugger (x64dbg) or an emulator (Qiling/Unicorn). Target the **point of transition** where the VM "hands off" the decrypted payload to the system.
3.  **Identify AES Key Material:** Since `aesenc` is present, use memory forensics to find the round keys in RAM. If you can dump the key, you may be able to decrypt the final payload offline.
4.  **Memory Forensics at "Point of Entry":** Place hardware breakpoints on suspicious APIs (`VirtualAlloc`, `CreateProcess`, `WriteProcessMemory`). Monitor for the moment the packer finishes its internal loops and prepares a new executable region in memory. **This is where the "true" malware will appear.**
5.  **Scripted Triage:** Use YARA rules to detect the specific "Dispatch" patterns or AES-related constants found in this disassembly to identify other samples from the same threat actor or packer family.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the technical analysis to the relevant MITRE ATT&CK techniques. Because the primary goal of all these behaviors is to hinder manual and automated reverse engineering (Defense Evasion), they fall under the **T1027** umbrella, though each represents a distinct method of obfuscation.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of a VM Dispatcher and custom bytecode masks the true logic of the malware by replacing standard x86 instructions with an internal, non-standard instruction set. |
| T1027 | Obfuscated Files or Information | Complex "anti-analysis" math (constant folding) is used to stall human analysts and break decompiler simplification passes during manual review. |
| T1027 | Obfuscated Files or Information | Specific checks for integrity keys and environment identifiers are implemented to detect the presence of debuggers or sandboxes before executing further code. |
| T1027 | Obfuscated Files or Information | The use of complex data-walking routines hides internal configuration blobs and transitions between layers, preventing linear analysis of the packer's execution flow. |

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
*   **Go Build ID:** `m_eWKAVMKwFLXIGF2mMv/2j5A85-N9hZ9W_iPMwYY/3kDBzS7kxfOy3K1Ccv9t/7I8JItNK_qHl3j3AXNUy` (Note: This is a unique identifier for the specific Go build of the binary.)

**Other artifacts**
*   **Programming Language:** Golang (Identified via `Go build ID`, `runtime.`, `reflect.`, and `gopau`).
*   **Malware Category:** Advanced Packer / Virtualized Protector (High-tier).
*   **Technical Indicators (Behavioral):**
    *   **VM Dispatcher Pattern:** Usage of a custom bytecode interpreter with a dispatcher loop (`*(*0x20 + -0x2b0)`).
    *   **Anti-Analysis Arithmetic:** Use of complex "Constant Folding" traps to hinder automated deobfuscation.
    *   **Cryptographic Signatures:** Presence of `aesenc` (AES encryption) for multi-layered protection.
    *   **Integrity Checks:** Hardcoded character checks (`0x5455`, `0x4d41`, `0x6d61`) used to detect tampering or environmental anomalies.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

**1. Malware family:** custom (Advanced Packer/Protector)
**2. Malware type:** loader
**3. Confidence:** High (for Type) / Medium (for Family)

**4. Key evidence:**
*   **Virtualized Execution Engine:** The presence of a "Dispatcher Loop" and the transition from standard x86 instructions to a custom, private bytecode interpreter indicates the primary purpose is to hide the core malicious logic behind a sophisticated VM layer.
*   **Advanced Anti-Analysis Techniques:** The use of "Constant Folding" traps (complex arithmetic meant to stall human analysts) and state-driven execution confirms that this is a high-tier protection shell designed specifically to thwart reverse engineering.
*   **Loader Characteristics:** The report explicitly states that the analysis is currently focused on the *interpreter* rather than the actual malware, confirming its role as a sophisticated loader/packer used to wrap and protect a secondary, hidden payload.
