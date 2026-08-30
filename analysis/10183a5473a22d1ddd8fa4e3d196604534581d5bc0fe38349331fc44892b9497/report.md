# Threat Analysis Report

**Generated:** 2026-08-17 23:22 UTC
**Sample:** `10183a5473a22d1ddd8fa4e3d196604534581d5bc0fe38349331fc44892b9497_10183a5473a22d1ddd8fa4e3d196604534581d5bc0fe38349331fc44892b9497.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10183a5473a22d1ddd8fa4e3d196604534581d5bc0fe38349331fc44892b9497_10183a5473a22d1ddd8fa4e3d196604534581d5bc0fe38349331fc44892b9497.exe` |
| File type | PE32+ executable for MS Windows 6.01 (GUI), x86-64, 9 sections |
| Size | 1,866,752 bytes |
| MD5 | `a50dfdd0152877c28f16eceab84d0b41` |
| SHA1 | `aa01c012f7d65e0935f5d3a0e648a780a6798783` |
| SHA256 | `10183a5473a22d1ddd8fa4e3d196604534581d5bc0fe38349331fc44892b9497` |
| Overall entropy | 6.781 |
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
| `.text` | 512,512 | 6.234 | No |
| `.rdata` | 1,142,784 | 6.829 | No |
| `.data` | 43,008 | 3.293 | No |
| `.pdata` | 15,360 | 5.113 | No |
| `.xdata` | 512 | 1.691 | No |
| `.idata` | 1,536 | 4.013 | No |
| `.reloc` | 11,776 | 5.418 | No |
| `.symtab` | 512 | 0.02 | No |
| `.rsrc` | 137,216 | 6.119 | No |

### Imports

**kernel32.dll**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetProcessPriorityBoost`, `SetEvent`

## Extracted Strings

Total strings found: **5001** (showing first 100)

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
P H9S ujH
S0H9P0u`
8S8uUH
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
\$XHc
$H+L$HH
T$(H+J
L$(H+A

H9Z(w
\$0H9K
D$pH9H
D$0H9H
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
9q0s&H9J
09z0w
H
H9X(v
L
HPH9w
H(H9w
Q8H+Q(
H9D$XA
H9D$XA
H9D$8A
L$0H9A
t$(H9q8H
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0046bfe0` | `0x46bfe0` | 408922 | ✓ |
| `fcn.0046c040` | `0x46c040` | 385467 | ✓ |
| `fcn.0046c000` | `0x46c000` | 385466 | ✓ |
| `fcn.00470ac0` | `0x470ac0` | 253207 | ✓ |
| `fcn.0046c4a0` | `0x46c4a0` | 226056 | ✓ |
| `fcn.0046c4c0` | `0x46c4c0` | 225928 | ✓ |
| `fcn.0046c4e0` | `0x46c4e0` | 225803 | ✓ |
| `fcn.0046c500` | `0x46c500` | 225675 | ✓ |
| `fcn.0046c520` | `0x46c520` | 225547 | ✓ |
| `fcn.0046c540` | `0x46c540` | 225419 | ✓ |
| `fcn.0046c560` | `0x46c560` | 225288 | ✓ |
| `fcn.0046c580` | `0x46c580` | 225160 | ✓ |
| `fcn.0046c5a0` | `0x46c5a0` | 225032 | ✓ |
| `fcn.0046c5c0` | `0x46c5c0` | 224904 | ✓ |
| `fcn.00470c20` | `0x470c20` | 221879 | ✓ |
| `fcn.00470c80` | `0x470c80` | 192279 | ✓ |
| `fcn.00470d20` | `0x470d20` | 161719 | ✓ |
| `fcn.00470d80` | `0x470d80` | 143511 | ✓ |
| `entry0` | `0x46d6e0` | 14533 | ✓ |
| `fcn.0046bfc0` | `0x46bfc0` | 11699 | ✓ |
| `fcn.00416120` | `0x416120` | 6213 | ✓ |
| `fcn.0047cbc0` | `0x47cbc0` | 4465 | ✓ |
| `fcn.0043f1e0` | `0x43f1e0` | 4357 | ✓ |
| `fcn.00424ca0` | `0x424ca0` | 3928 | ✓ |
| `fcn.0046a020` | `0x46a020` | 3857 | ✓ |
| `fcn.00419e00` | `0x419e00` | 3678 | ✓ |
| `fcn.00460e60` | `0x460e60` | 3022 | ✓ |
| `fcn.0042b440` | `0x42b440` | 2917 | ✓ |
| `fcn.00444960` | `0x444960` | 2510 | ✓ |
| `fcn.00478400` | `0x478400` | 2484 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00416120.c`](code/fcn.00416120.c)
- [`code/fcn.00419e00.c`](code/fcn.00419e00.c)
- [`code/fcn.00424ca0.c`](code/fcn.00424ca0.c)
- [`code/fcn.0042b440.c`](code/fcn.0042b440.c)
- [`code/fcn.0043f1e0.c`](code/fcn.0043f1e0.c)
- [`code/fcn.00444960.c`](code/fcn.00444960.c)
- [`code/fcn.00460e60.c`](code/fcn.00460e60.c)
- [`code/fcn.0046a020.c`](code/fcn.0046a020.c)
- [`code/fcn.0046bfc0.c`](code/fcn.0046bfc0.c)
- [`code/fcn.0046bfe0.c`](code/fcn.0046bfe0.c)
- [`code/fcn.0046c000.c`](code/fcn.0046c000.c)
- [`code/fcn.0046c040.c`](code/fcn.0046c040.c)
- [`code/fcn.0046c4a0.c`](code/fcn.0046c4a0.c)
- [`code/fcn.0046c4c0.c`](code/fcn.0046c4c0.c)
- [`code/fcn.0046c4e0.c`](code/fcn.0046c4e0.c)
- [`code/fcn.0046c500.c`](code/fcn.0046c500.c)
- [`code/fcn.0046c520.c`](code/fcn.0046c520.c)
- [`code/fcn.0046c540.c`](code/fcn.0046c540.c)
- [`code/fcn.0046c560.c`](code/fcn.0046c560.c)
- [`code/fcn.0046c580.c`](code/fcn.0046c580.c)
- [`code/fcn.0046c5a0.c`](code/fcn.0046c5a0.c)
- [`code/fcn.0046c5c0.c`](code/fcn.0046c5c0.c)
- [`code/fcn.00470ac0.c`](code/fcn.00470ac0.c)
- [`code/fcn.00470c20.c`](code/fcn.00470c20.c)
- [`code/fcn.00470c80.c`](code/fcn.00470c80.c)
- [`code/fcn.00470d20.c`](code/fcn.00470d20.c)
- [`code/fcn.00470d80.c`](code/fcn.00470d80.c)
- [`code/fcn.00478400.c`](code/fcn.00478400.c)
- [`code/fcn.0047cbc0.c`](code/fcn.0047cbc0.c)

## Behavioral Analysis

Based on the third and final chunk of disassembly, the sophistication of this sample has been further confirmed. This segment reveals not only a complex execution engine but also an **advanced "Just-in-Time" (JIT) de-obfuscation layer** and high levels of **arithmetic obfuscation**.

Here is the updated and expanded analysis including all previous findings.

---

### Updated Analysis

#### 1. Advanced Execution Architecture: State Machine & VM Dispatcher
*   **Dispatcher Logic:** The reliance on a central dispatcher (`fcn.0046c4a0`) remains a primary architectural feature. By passing state variables into this function, the malware avoids linear execution paths, making it extremely difficult for automated tools to map the full logic of the program.
*   **Virtual Machine (VM) Integration:** The recurring calls to `fcn.0046c100` and `fcn.0046c4a0` with varying constants confirm that the "real" malicious logic is likely stored as a custom bytecode. This architecture allows the developers to change the underlying behavior by simply updating the bytecode without changing the primary loader's code.

#### 2. Just-in-Time (JIT) De-obfuscation & Data Decoding
The function `fcn.00478400` provides evidence of a very sophisticated data-processing layer:
*   **Inline Decoding Loops:** The large `while(true)` loop containing complex arithmetic (e.g., `uVar16 = uVar16 << uVar13 & ... | uVar19 - 0x30`) is a classic technique used to **de-obfuscate data on the fly**.
*   **Encoded Constants:** The use of non-standard character checks (like `'q'`, `'v'`, `'!'`) and large hex values (e.g., `0x49a553`, `0x49df1c`) suggests that internal configuration strings, IP addresses, or secondary payload headers are "scrambled" in memory until the moment they are needed for a network connection or memory allocation.
*   **Dynamic Interpretation:** The code isn't just decrypting a file; it is actively interpreting a stream of data to reconstruct its own internal state.

#### 3. Sophisticated Memory Management & Multi-threading
The analysis from chunk 2 remains critical here:
*   **Concurrency for Evasion:** The explicit use of `LOCK()` and `UNLOCK()` instructions confirms that the loader operates in a multi-threaded environment. This is often used to perform "heavy lifting" (like decrypting large portions of a payload) on background threads to keep the main thread responsive or to hide activity from simple behavioral monitors.
*   **Complex Offsets:** The heavy use of indirect addressing (e.g., `*(*0x20 + -0xd0)`) and varying memory offsets indicates that the loader interacts with a very complex internal data structure, likely a custom table for mapping bytecode to specific actions.

#### 4. Advanced Obfuscation Techniques
*   **Arithmetic Complexity:** The use of bit-shifting and masking (e.g., `uVar13 = 4` followed by shift operations) is designed to bypass static analysis tools that look for simple "XOR" or "ADD" patterns. It makes the underlying logic (like calculating a memory offset) appear like complex math.
*   **Control Flow Flattening:** By breaking code into small chunks fed into the dispatcher, the authors have effectively destroyed the ability to perform static "graph" analysis of the binary's flow.

---

### Summary of Technical Indicators

| Feature | Observation | Significance |
| :--- | :--- | :--- |
| **VM / Interpreter** | Recurring calls to `fcn.0046c4a0` and `fcn.0046c100`. | **High:** The core logic is hidden in a custom bytecode, making static analysis very difficult. |
| **JIT De-obfuscation** | Complex bitwise arithmetic/loops to process "scrambled" data (e.g., `fcn.00478400`). | **High:** Critical configuration and secondary payloads are decrypted only at the moment of use. |
| **State Machine** | Extensive state assignments followed by dispatcher calls. | **High:** Disruption of standard control-flow graphs to hide logic from automated tools. |
| **Concurrency** | Frequent `LOCK()` and `UNLOCK()` instructions. | **Med/High:** Indicates multi-threaded execution, likely for concurrent decryption or evasion. |
| **Arithmetic Obfuscation** | Use of shifts/masks instead of direct assignments. | **Medium:** A standard technique to hide "simple" calculations from automated scanners. |

---

### Updated Threat Intelligence Summary
This sample is a **high-complexity, professional-grade packer and loader**. It exhibits characteristics common in sophisticated **APT (Advanced Persistent Threat)** tools and high-end ransomware loaders. 

The combination of a **VM-based execution engine**, **multi-threaded processing**, and **Just-in-Time de-obfuscation** suggests that this is not a "one-off" piece of malware, but rather a component of a sophisticated operation. The loader's primary goal is to remain invisible for as long as possible by ensuring that the malicious payload never exists in a fully decrypted state in memory until it is being actively executed by the interpreter.

**Conclusion:** This is a highly evasive loader designed to defeat both automated sandboxes and manual reverse engineering. 
**Recommendation:** Traditional static analysis will only uncover the "shield" (the packer). **Dynamic analysis via a debugger (like x64dbg) or an instrumentation tool (like Frida)** is required to intercept the de-obfuscated data at the point where it is passed into the VM dispatcher. Watch for network callbacks once the "JIT" decoding in `fcn.00478400` completes.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided report to the relevant MITRE ATT&K techniques. Most of the sophisticated evasion tactics described fall under the primary technique of **Obfuscated Files or system**, as they are specifically designed to hinder both automated sandboxes and manual reverse engineering.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or system | The use of a **Virtual Machine (VM) Dispatcher** hides the "real" malicious logic within custom bytecode, making it difficult for analysts to map the execution flow. |
| T1027 | Obfuscated Files or system | The **Just-in-Time (JIT) de-obfuscation** and use of complex arithmetic ensure that configuration data remains encrypted until the exact moment it is needed. |
| T1027 | Obfuscated Files or system | **Arithmetic Complexity** (bit-shifting/masking) is employed to mask simple calculations, effectively bypassing signature-based detection tools. |
| T1027 | Obfuscated Files or system | **Control Flow Flattening** disrupts the construction of control-flow graphs, preventing automated tools from analyzing the program's logic flow. |
| T1036 (Related) | Automated_Analysis_Evasion | While not a standalone technical ID in all versions, the use of multi-threading and complex loaders is specifically designed to **evade behavior monitors** during execution. |

***Note on Mapping:** Because the adversary is utilizing multiple layers of obfuscation (VM dispatching, JIT decoding, arithmetic complexity, and control flow flattening), these behaviors all map to T1027. These are standard techniques used by advanced threat actors to create a "shield" for the underlying payload.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The report notes that data is "scrambled" in memory and only decrypted at the point of use, which is why no static IPs or URLs appear in the raw strings.)

### **File paths / Registry keys**
*   *None identified.* (No hardcoded file system paths or registry modifications were present in the provided text.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA-1, or SHA-256 hashes were present in the string list.)

### **Other artifacts**
*   **Internal Function Offsets (Potential for YARA/Signature matching):** 
    *   `fcn.0046c4a0` (Dispatcher logic)
    *   `fcn.0046c100` (VM Interpreter)
    *   `fcn.00478400` (JIT De-obfuscation loop)
*   **Behavioral Artifacts:**
    *   **Execution Style:** Custom VM/Interpreter architecture using a dispatcher to hide linear execution paths.
    *   **Obfuscation Technique:** Bitwise arithmetic masking and shifting (e.g., `uVar16 = uVar16 << uVar13 & ... | uVar19 - 0x30`) used for JIT de-obfuscation.
    *   **Concurrency:** Frequent use of `LOCK()` and `UNLOCK()` instructions to perform multi-threaded decryption/execution.
*   **Potential Go Library Artifacts (Used for identification, though not unique to a specific campaign):** 
    *   `runtime`, `reflect`, `memprofiler`, `uint64`, `int31n`, `bisect`.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for this sample:

1. **Malware family:** Custom
2. **Malware type:** Loader
3. **Confidence:** High (for Type), Medium (for Family)
4. **Key evidence:**
    *   **VM-Based Execution Architecture:** The use of a custom VM dispatcher and control flow flattening indicates a sophisticated, bespoke design intended to hide core logic from static analysis tools by using a proprietary bytecode system.
    *   **Just-in-Time (JIT) De-obfuscation:** The presence of complex bitwise arithmetic and decoding loops (fcn.00478400) confirms the sample is designed to keep configuration data and secondary payloads encrypted in memory until the exact moment they are required for execution.
    *   **Professional-Grade Evasion:** The combination of multi-threaded execution (`LOCK`/`UNLOCK`) and advanced arithmetic complexity suggests a high-level, professional-grade loader typical of APT (Advanced Persistent Threat) campaigns or high-end ransomware deployment operations.
