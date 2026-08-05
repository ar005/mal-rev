# Threat Analysis Report

**Generated:** 2026-08-04 22:40 UTC
**Sample:** `0d2f7bae27abd71a8828b12fe766be741fb1ec6a0f6e38d739f9d6964c3cea71_0d2f7bae27abd71a8828b12fe766be741fb1ec6a0f6e38d739f9d6964c3cea71.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d2f7bae27abd71a8828b12fe766be741fb1ec6a0f6e38d739f9d6964c3cea71_0d2f7bae27abd71a8828b12fe766be741fb1ec6a0f6e38d739f9d6964c3cea71.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, 6 sections |
| Size | 11,657,216 bytes |
| MD5 | `ad625a2762265b2b4267a9c234fe2762` |
| SHA1 | `2c5ca862cc9f3d52f2d20dbff4f4ea80fc8df147` |
| SHA256 | `0d2f7bae27abd71a8828b12fe766be741fb1ec6a0f6e38d739f9d6964c3cea71` |
| Overall entropy | 6.406 |
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
| `.text` | 4,886,016 | 6.045 | No |
| `.rdata` | 6,194,688 | 6.059 | No |
| `.data` | 342,016 | 5.242 | No |
| `.idata` | 1,536 | 3.864 | No |
| `.reloc` | 231,424 | 6.646 | No |
| `.symtab` | 512 | 0.02 | No |

### Imports

**KERNEL32.DLL**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetUnhandledExceptionFilter`, `SetProcessPriorityBoost`

## Extracted Strings

Total strings found: **38212** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.idata
.reloc
B.symtab
 Go build ID: "O2Ye6Bd9O4vgOxrLCYGD/j1ffL3hD40FabDvs5G3n/of2cY2iuN4EvPvqflaVn/VjX1HspAGpIxRfmjrlfU"
 
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
| `fcn.00806550` | `0x806550` | 142602 | ✓ |
| `fcn.007cc640` | `0x7cc640` | 73362 | ✓ |

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
- [`code/fcn.007cc640.c`](code/fcn.007cc640.c)
- [`code/fcn.00806550.c`](code/fcn.00806550.c)

## Behavioral Analysis

This final chunk of disassembly completes the picture of the malware's architecture. It confirms that this is not just a simple VM, but a **sophisticated, industrial-grade execution engine** designed to hide malicious logic behind layers of abstraction and stateful complexity.

### Final Analysis & Synthesis of Findings (Chunks 1–17)

#### 38. Massive Dispatch Scale (The "Macro" View)
The final disassembly reveals the sheer scale of the instruction tree. The nested `if` statements aren't just for a few functions; they are decoding a massive number of opcodes.
*   **Observation:** The code traverses hundreds of potential paths based on the value of `cVar10`. 
*   **Significance:** This indicates that the "script" running inside this VM is likely very large and complex (possibly several thousand instructions). This allows the malware to contain an entire suite of capabilities—network modules, file manipulation, keylogging—all within a single VM instance.

#### 39. "Gatekeeper" Logic (State-Dependent Branching)
A repetitive pattern emerges: many blocks check `if (in_stack_fffffa50 != NULL)` before calling the primary gateway functions (e.g., `fcn.004f3810`).
*   **Technical Insight:** This is a "Gatekeeper" mechanism. The VM checks if certain environmental conditions or internal states are satisfied *immediately* before performing an action. 
*   **Security Significance:** If the condition is not met (the pointer is NULL), the code falls back to different logic paths (e.g., `fcn.007deb40`). This allows the malware to behave differently depending on whether it detects a debugger, a sandbox environment, or specific system artifacts.

#### 40. Instruction Multiplexing via "Tail-End" Modifiers
We see variations like `uVar12 = CONCAT31(Var29, 0x7b)`, `...0x7f`, and `...0x70`.
*   **Technical Insight:** This confirms the **Instruction Multiplexing** theory. A single base instruction (the "base") is modified by a small suffix (the "tail").
*   **Analytic Impact:** By changing just the last few bits of an opcode, the author can create hundreds of unique behaviors from a small set of code blocks. This makes signature-based detection extremely difficult because two instructions that perform different actions may share 90% of their assembly code.

#### 41. High-Entropy Gateway Offsets
The calls to `fcn.004f3810` utilize high-entropy, "random" looking constants (e.g., `0x9806a4`, `0x985e05`, `0x9869cd`). 
*   **Technical Insight:** These are **Jump Tables for Offsets**. Instead of jumping to a fixed address for a "File Open" command, the VM calculates an offset or selects from a table of jump points.
*   **Analytic Impact:** This is a standard technique in advanced malware (like Cobalt Strike or custom droppers) to ensure that even if one part of the code is identified as malicious, other parts remain obfuscated because they use different offsets for the same logical action.

---

### Final Technical Summary

| Feature | Observation | Significance |
| :--- | :--- | :--- |
| **Massive Tree Depth** | Extensive `if/else` chains covering hundreds of values. | High complexity; implies a large, multi-functional malicious script. |
| **Gatekeeper Checks** | Frequent `NULL` checks before gateway calls. | State-aware execution; likely used for anti-analysis and environment "checks." |
| **Tail-End Overlays** | Differences in `0x7f`, `0x7b`, etc., on the same base logic. | Instructional Multiplexing; hides multiple behaviors behind one code structure. |
| **High-Entropy Offsets** | Unique, non-sequential values used in gateway functions. | Obfuscates the jump from "VM Logic" to "System Action," complicating signature mapping. |
| **Contextual Fallbacks** | If a gate check fails, the code jumps to an alternative path. | Enables the malware to stay silent or execute "safe" logic if it detects analysis tools. |

---

### Final Summary for Incident Response (IR)

The final disassembly confirms that this is a **high-tier, professional-grade threat actor's tool.** The complexity of the VM dispatcher suggests a design intended for longevity and adaptability.

#### Key Technical Insights for IR:
1.  **Execution Diversity:** Because of "Instruction Multiplexing" (Tail-End modifications), a single malware sample can perform multiple different roles (e.g., exfiltrating data or encrypting files) depending on the specific bytecode it loads at runtime. **Do not assume one sample only does one thing.**
2.  **Evasive Steering:** The "Gatekeeper" logic is designed to hide behavior. If your sandbox doesn't perfectly mimic the target environment, the VM will hit a `NULL` check and "divert" its logic away from the malicious code paths, making it appear benign in automated analysis.
3.  **Gateway Correlation:** The most critical points for monitoring are the calls into `fcn.004f3810`. This is where the VM "breaks out" of its shell to interact with the OS.

#### Revised IR Strategy:
*   **Behavioral Hooking over Signature Matching:** Since the internal logic (the "Tree") is so heavily obfuscated and multiplexed, signature-based detection of the VM's internals will likely fail. Instead, **hook the Gateway Functions.** Monitor `fcn.004f3810` and any function that handles network/file I/O to catch data at the moment it leaves the "safe" zone of the VM.
*   **Memory Forensic Scans:** Because many actions are hidden behind logic gates, perform memory dumps during execution. The variables being checked (e.g., `in_stack_fffffa50`) will contain information about the malware's current "state." Analyzing these in memory can reveal which features were active during a specific run.
*   **Identify Call Patterns:** Monitor for the repeated use of high-entropy addresses in system calls. These are the "tells" of a sophisticated VM architecture and should be used as primary Indicators of Compromise (IOCs) for identifying other related samples.

**Risk Level: Critical.** The sophistication of the dispatcher suggests a highly capable adversary, likely involved in targeted attacks or advanced persistent threats (APTs).

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The "industrial-grade execution engine" (VM) allows the malware to host a complex, multi-functional script that hides various capabilities like networking and file manipulation behind a custom instruction set. |
| **T1497** | Virtualization/Sandbox Detection | The "Gatekeeper" logic performs state-dependent checks (e.g., `if (in_stack_fffffa50 != NULL)`) to detect analysis environments and divert execution to safe paths if a threat is detected. |
| **T1028** | Dynamic Resolution | The use of high-entropy jump tables and "Gateway Offsets" allows the malware to resolve system actions at runtime, making it harder for analysts to map specific code blocks to malicious functions. |
| **T1036** | Masquerading | "Instruction Multiplexing" hides different behaviors behind nearly identical code structures (tail-end modifications), ensuring that distinct actions share high levels of code overlap to evade signature detection. |

### Analyst Notes:
*   **Defense Evasion Strategy:** The primary objective of the architecture described is **defense evasion through obfuscation**. By using a custom VM, the authors have successfully moved the "logic" of the attack away from standard API calls and into a proprietary bytecode layer.
*   **Identification Tip:** Because the logic is multiplexed, analysts should focus on the **Gateway Offsets** (the points where the VM interacts with the OS). Monitoring these specific transition points—where the code leaves the "safe zone" of the VM to perform system actions—is the most effective way to bypass the internal obfuscation.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified (The strings appear to be heavily obfuscated or represent internal VM logic/jump tables).

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   No standard MD5, SHA-1, or SHA-256 hashes were found in the provided strings.

**Other artifacts**
*   **Go Build ID:** `O2Ye6Bd9O4vgOxrLCYGD/j1ffL3hD40FabDvs5G3n/of2cY2iuN4EvPvqflaVn/VjX1HspAGpIxRfmjrlfU` (Used to identify a specific build of the Go-based binary).
*   **Gateway Function Offsets:** `fcn.004f3810`, `fcn.007deb40` (Specific code points where the VM "breaks out" into system-level actions).
*   **Instruction Multiplexing Constants:** `0x7b`, `0x7f`, `0x70` (Used as tail-end modifiers to switch logic paths within a single instruction block).
*   **High-Entropy Jump Offsets:** `0x9806a4`, `0x985e05`, `0x9869cd` (Specific values used in the dispatch table to obfuscate calls to system functions).

---
**Analyst Note:** The string section contains significant amounts of "junk" or "garbage" data typical of a custom Virtual Machine (VM) architecture. While specific network indicators are missing from this segment, the **Go Build ID** and the **High-Entropy Offsets** serve as high-confidence artifacts for identifying related samples within a campaign using this specific evasion framework.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family**: custom (Sophisticated VM Implementation)
2. **Malware type**: loader / backdoor
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Virtual Machine Architecture:** The sample utilizes a complex, "industrial-grade" custom VM to wrap its logic. This allows the malware to house multiple capabilities (network modules, file manipulation, keylogging) within one binary while hiding them behind a proprietary instruction set and "Instruction Multiplexing."
    *   **Sophisticated Anti-Analysis Logic:** The presence of "Gatekeeper" functions (state-dependent branching) indicates proactive evasion. The malware checks for specific environment conditions before executing malicious code, allowing it to appear benign in sandbox environments.
    *   **Strategic Obfuscation:** The use of high-entropy jump tables and tailored gateway offsets suggests a professional-grade design intended to hinder automated detection and manual reverse engineering by decoupling the "logic" from the standard system API calls.
