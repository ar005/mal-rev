# Threat Analysis Report

**Generated:** 2026-07-12 09:05 UTC
**Sample:** `04e4ab0b983a9011303db7fb009d3053280297453de5e3f4cd231ef08476b2c4_04e4ab0b983a9011303db7fb009d3053280297453de5e3f4cd231ef08476b2c4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04e4ab0b983a9011303db7fb009d3053280297453de5e3f4cd231ef08476b2c4_04e4ab0b983a9011303db7fb009d3053280297453de5e3f4cd231ef08476b2c4.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, 6 sections |
| Size | 11,669,504 bytes |
| MD5 | `cbd1abb56425b90d45e7a6badf20f31c` |
| SHA1 | `86ed566c45c5209177ff4d174fa27f7f1b605552` |
| SHA256 | `04e4ab0b983a9011303db7fb009d3053280297453de5e3f4cd231ef08476b2c4` |
| Overall entropy | 6.407 |
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
| `.text` | 4,892,672 | 6.045 | No |
| `.rdata` | 6,200,320 | 6.062 | No |
| `.data` | 342,016 | 5.241 | No |
| `.idata` | 1,536 | 3.914 | No |
| `.reloc` | 231,424 | 6.656 | No |
| `.symtab` | 512 | 0.02 | No |

### Imports

**KERNEL32.DLL**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetUnhandledExceptionFilter`, `SetProcessPriorityBoost`

## Extracted Strings

Total strings found: **38303** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.idata
.reloc
B.symtab
 Go build ID: "-Wh7E6puTQNGa2lvG2pk/2-amth_lgwDqF8rniP5p/ZRTrQMmUvuZD_NA2N0nw/qEqFzO7ViXCWvHOsNqQ1"
 
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

This final chunk of disassembly (17/17) completes the picture of a **high-complexity Virtual Machine (VM)** architecture. It provides the most granular look at the "inner workings" of the dispatcher, confirming that this is not merely an obfuscation layer, but a fully realized execution environment designed to frustrate both automated analysis and manual deconstruction.

Below is the updated analysis incorporating the final set of data.

---

### Updated Analysis of Sample Behavior

#### 1. Micro-Instruction Granularity & Fragmented Dispatch
The extensive nested `if` structures (e.g., `cVar10 < 0x2e`, `cVar10 < 0x1d`, etc.) confirm that the VM uses a **dense, multi-byte opcode system**. 
*   **Opcode Fragmentation:** Instead of one instruction equals one action, a single "guest" instruction may be broken into several "micro-ops." The jump logic suggests that a single high-level command is decomposed into dozens of low-level transitions to make tracking the original logic impossible.
*   **Overlapping State Logic:** In several locations (e.g., `0x7f` vs `0x7b`), different values lead to nearly identical handler setups. This suggests that the VM interprets "context" to determine action, meaning a single instruction's behavior can change based on previous instructions executed by the guest.

#### 2. Real-time Instruction Transformation (The "CONCAT" Logic)
A recurring pattern in this chunk is the use of `CONCAT` operations followed immediately by calls like `fcn.007ded30`.
*   **Dynamic Translation:** The VM doesn't just jump to a handler; it often modifies the instruction's value (the `uVar12` variables) before processing. This implies that the "guest" code is in a semi-obfuscated state, and the **VM serves as the decryptor/translator** during the execution cycle.
*   **Implicit Decoding:** By manipulating bit-shifted values (`uVar12 = CONCAT31(Var29, 0x7b)`), the VM ensures that an analyst looking at a memory dump of the "guest" code cannot see the actual parameters being passed to the host functions.

#### 3. Protective Guardrails and Fallback Logic
The repeated check `if (in_stack_fffffa50 != NULL)` before several handler calls is highly significant.
*   **Integrity Checks:** This acts as a "gatekeeper." If the VM's internal state doesn't perfectly match what it expects for that specific opcode, it falls back to alternative logic or stays within the dispatcher loop. 
*   **Anti-Debugging/Tampering:** These checks can also serve as an environment check—if a debugger or tool attempts to skip over certain "junk" bytes, the pointer `in_stack_fffffa50` will fail the null check, and the VM will divert to an incorrect state, likely causing the malware to crash or behave differently.

#### 4. Complex Internal Pointer Arithmetic
The interaction with `uStack_538`, `pcStack_2d4`, and `pcVar11` in the latter half of the chunk shows a **complex internal register system**.
*   **Virtual Register Mapping:** The malware isn't using standard CPU registers for its core logic. It maps "Guest" variables to calculated offsets within its own private memory space. 
*   **Dynamic Offsets:** Calculations like `uVar17 = uStack_538._4_4_ + (0xfffffffd < uStack_538)` suggest the VM is navigating a complex data structure (like a linked list or a heavily fragmented table) to find its next instruction or data source.

---

### Updated Summary for Incident Response

The final analysis confirms that this malware is protected by a **highly sophisticated, custom-built Virtual Machine.** It is designed specifically to defeat static analysis and "linear" dynamic analysis (where one would simply follow the code's path).

**New Technical Findings:**
1.  **Fragmented Instruction Set:** The guest code doesn't map 1:1 to host actions. One "instruction" may trigger multiple internal state changes, making it difficult to pinpoint exactly when a malicious action (e.g., opening a socket) is being prepared.
2.  **Just-In-Time Transformation:** The VM modifies its own instructions in memory during the dispatch process (`CONCAT` logic). This means **memory dumps of the malware are "incomplete"**; you only see the true intent at the exact moment of execution.
3.  **Sophisticated Fallback Mechanism:** The frequent `NULL` pointer checks suggest a robust error-handling or integrity-checking system. If an analyst tries to "patch" out code or force jumps, the VM will likely detect the inconsistency and change its behavior.

**Refined Recommendations for IR Team:**
1.  **Focus on State Transitions (The "Heartbeat"):** Instead of trying to map every opcode, monitor the **frequency of transitions between `fcn` calls.** Each jump from a `0x7ded30` style handler back into the main loop is a completion of one "micro-op." A cluster of these followed by an unusual system call is your primary indicator.
2.  **Memory Monitoring for Data Reconstruction:** Because of the dynamic transformation (`CONCAT`), watch for **memory regions that change frequently.** If a memory block's value changes significantly just before a jump to a known "danger" function (like `NtCreateThread` or `InternetConnect`), it was likely a decrypted payload.
3.  **Behavioral Signatures over Static Indicators:** Because the code is so heavily virtualized, traditional YARA rules based on byte sequences may fail. Focus on **behavioral patterns**: 
    *   High frequency of short-lived threads/processes.
    *   Rapid, repetitive internal memory copies (indicative of VM processing).
    *   DNS requests made from non-standard processes or with randomized subdomains.

**Final Risk Assessment: CRITICAL.**
This is a "high-effort" threat. The sheer complexity of the dispatcher indicates that the threat actor is well-resourced and intends to maintain persistence while avoiding detection by standard automated sandboxes. 

**Action Item:**
Create behavioral alerts based on **host-side side effects**. Since we cannot easily deconstruct the VM's "Guest" logic in a reasonable timeframe, we must catch the "Fruit" of its labor: unauthorized network connections, file modifications to system directories, and unexpected child process creation.

---

### Final Summary Metrics
*   **VM Complexity:** Extreme (Multi-layered dispatcher + Runtime translation)
*   **Obfuscation Depth:** High (Instruction fragmentation & context-dependent execution)
*   **Anti-Analysis Profile:** Robust (Integrity checks & dynamic memory manipulation)
*   **Primary Strategy:** Wait for the "Escape Point." Monitor where the VM interacts with standard Windows APIs (`WinExec`, `CreateProcess`, `Internet...`). These are the moments when the guest logic manifests as host action.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Programs | The use of a custom Virtual Machine (VM), instruction fragmentation, and complex pointer arithmetic are used to hide the core logic from static analysis. |
| **T1055** | Packed Code | The "CONCAT" logic and real-time instruction transformation indicate that the VM acts as a dynamic decryptor/translator for its internal code. |
| **T1498** | Virtualization/Emulation Detection | The "Guardrails" and integrity checks are specifically designed to detect the presence of debuggers or analysis tools trying to interfere with execution. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided "Extracted Strings" and "Behavioral Analysis." Based on your criteria to exclude noise and standard system components, here is the intelligence report.

### **Indicator of Compromise (IOC) Report**

**1. IP addresses / URLs / Domains**
*   None identified.

**2. File paths / Registry keys**
*   None identified.

**3. Mutex names / Named pipes**
*   None identified.

**4. Hashes**
*   **Note:** While no standard MD5/SHA1/SHA-256 hashes were present in the string dump, the following unique identifier was found:
    *   `Wh7E6puTQNGa2lvG2pk/2-amth_lgwDqF8rniP5p/ZRTrQMmUvuZD_NA2N0nw/qEqFzO7ViXCWvHOsNqQ1` (identified as a **Go build ID**; can be used as a specific fingerprint for this malware variant).

**5. Other artifacts**
*   **Memory Address / Function Pointer:** `0x7ded30` (Identified in the analysis as a primary handler address within the VM dispatcher. While not a network IOC, it serves as a signature for identifying the core dispatcher logic during memory forensics).
*   **Note on Technical Findings:** The "Behavioral Analysis" indicates high-level evidence of a **Virtual Machine (VM) based packer/obfuscator**. This suggests that traditional static indicators (like strings and simple byte sequences) are intentionally hidden.

---

### **Analyst Notes & Observations**
The provided data suggests a highly sophisticated piece of malware utilizing a custom Virtual Machine architecture to hide its core logic. 
*   **Evasion Technique:** The presence of "Instruction Fragmentation" and "Just-in-Time Transformation" (the `CONCAT` logic) indicates the threat actor is attempting to bypass automated sandboxes and static analysis tools.
*   **Detection Strategy:** Because there are no immediate network indicators (IPs/Domains) in this specific sample, detection should focus on **behavioral patterns**, such as high-frequency internal memory transitions or unauthorized calls to system APIs like `NtCreateThread` and `InternetConnect`.

---

## Malware Family Classification

Based on the provided technical analysis, here is the classification for the sample:

1. **Malware family:** Custom
2. **Malware type:** Loader (or Trojan/Backdoor)
3. **Confidence:** Medium-High
4. **Key evidence:**
    *   **Advanced VM Architecture:** The use of a high-complexity, custom Virtual Machine with "instruction fragmentation" and "just-in-time transformation" is a hallmark of sophisticated loaders designed to hide the actual malicious payload from automated systems and manual analysis.
    *   **High Obfuscation & Evasion:** The presence of "Guardrails," integrity checks, and non-linear logic paths indicates a high-effort effort to bypass sandboxes and defeat signature-based detection (evidenced by the lack of plain-text indicators in the initial string dump).
    *   **Go-based Implementation:** The identification of a Go build ID suggests the sample is part of a modern malware ecosystem that leverages advanced languages for cross-platform compatibility or specific obfuscation techniques.
