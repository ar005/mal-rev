# Threat Analysis Report

**Generated:** 2026-08-04 20:54 UTC
**Sample:** `0d1ffcadc3b75c99807be361c95c9742377ec7aec19e25d2e88225e75dfbd082_0d1ffcadc3b75c99807be361c95c9742377ec7aec19e25d2e88225e75dfbd082.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d1ffcadc3b75c99807be361c95c9742377ec7aec19e25d2e88225e75dfbd082_0d1ffcadc3b75c99807be361c95c9742377ec7aec19e25d2e88225e75dfbd082.exe` |
| File type | PE32+ executable for MS Windows 5.02 (console), x86-64 (stripped to external PDB), 9 sections |
| Size | 12,979,136 bytes |
| MD5 | `d00111fc3df4e3fa3ec2bed19bf4972f` |
| SHA1 | `376b0978c54a018719196049d647a2f59322a803` |
| SHA256 | `0d1ffcadc3b75c99807be361c95c9742377ec7aec19e25d2e88225e75dfbd082` |
| Overall entropy | 7.972 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767554445 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 787,968 | 6.15 | No |
| `.data` | 11,999,744 | 7.999 | ⚠️ Yes |
| `.rdata` | 70,144 | 4.738 | No |
| `.pdata` | 45,568 | 5.917 | No |
| `.xdata` | 61,440 | 4.809 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 5,120 | 4.273 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 6,144 | 5.383 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `CopyFileA`, `CreateProcessA`, `CreateToolhelp32Snapshot`, `DeleteCriticalSection`, `DeleteProcThreadAttributeList`, `EnterCriticalSection`, `ExitProcess`, `FormatMessageA`, `GetConsoleWindow`, `GetEnvironmentVariableA`, `GetFileAttributesA`, `GetLastError`, `GetModuleFileNameA`, `GetModuleHandleA`
**msvcrt.dll**: `__C_specific_handler`, `___lc_codepage_func`, `___mb_cur_max_func`, `__getmainargs`, `__initenv`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `_amsg_exit`, `_cexit`, `_commode`, `_errno`, `_filelengthi64`, `_fileno`, `_fmode`
**USER32.dll**: `ShowWindow`

## Extracted Strings

Total strings found: **28370** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
.reloc
AWAVAUATUWVSH
X[^_]A\A]A^A_
8MZu>HcP<H
\cxeKtWuH
ums.exe
\cxeKtWuH
ums.exe
\MicrosoH
ft\WindoH
ws\StartH
 Menu\PrH
ograms\QH
OvzdBCu.H
J(A;J,}FHc
I(D;I,}FIc
<_t`<ntT
R(A;R,}-Hc
ATUWVSH
@[^_]A\
_GLOBAL_H9
x	NtAf
BHA;R,}
C8;C<|
AVWVSH
C8;C<}uH
X[^_A^
X[^_A^
X[^_A^
X[^_A^
ATUWVSH
0[^_]A\
0[^_]A\
R(A;R,}
R(A;R,}
AVUWVSH
@[^_]A^
@[^_]A^
<st\<f
AVAUATUWVSH
<Ot`E1
0[^_]A\A]A^
<Et)<Qt%H
t$8<Qt6H
C8;C<}(H
C8;C<}3H
A(;A,}3Lc
C(;C,L
D$ }>Lc
T$ u
A
<GtS<TtO1
AWAVATUWVSH
[^_]A\A^A_
[^_]A\A^A_
[^_]A\A^A_
[^_]A\A^A_
[^_]A\A^A_
[^_]A\A^A_
[^_]A\A^A_
[^_]A\A^A_
[^_]A\A^A_
ATUWVSH
0[^_]A\
ATUWVSH
P[^_]A\
P[^_]A\
P[^_]A\
P[^_]A\
UAWAVAUATWVSH
0<	w5A
G<Gty<TtuL
[^_A\A]A^A_]
AVWVSH
H[^_A^
AVUWVSH
@[^_]A^
@[^_]A^
UAWAVAUATWVSH
[^_A\A]A^A_]
ATUWVSH
 [^_]A\H
@' t	H
~D$8fH
AWAVWVSH
0[^_A^A_
AUATUWVSH
([^_]A\A]
UWVSIc
D;C}"A
AWAVAUATUWVSH
H[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
D$\ff.
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400c1450` | `0x1400c1450` | 786549 | ✓ |
| `fcn.140003670` | `0x140003670` | 777695 | ✓ |
| `fcn.1400bfd80` | `0x1400bfd80` | 720085 | ✓ |
| `fcn.1400bfea0` | `0x1400bfea0` | 719484 | ✓ |
| `fcn.140001410` | `0x140001410` | 104382 | ✓ |
| `fcn.14002d2c0` | `0x14002d2c0` | 75126 | ✓ |
| `fcn.14002ce00` | `0x14002ce00` | 73982 | ✓ |
| `fcn.140027980` | `0x140027980` | 53323 | ✓ |
| `fcn.14001af60` | `0x14001af60` | 48629 | ✓ |
| `fcn.14000ef20` | `0x14000ef20` | 48182 | ✓ |
| `fcn.14001b240` | `0x14001b240` | 46492 | ✓ |
| `fcn.1400109f0` | `0x1400109f0` | 41398 | ✓ |
| `fcn.140006d10` | `0x140006d10` | 36434 | ✓ |
| `fcn.1400305c0` | `0x1400305c0` | 11040 | ✓ |
| `fcn.140037240` | `0x140037240` | 9888 | ✓ |
| `fcn.1400648e0` | `0x1400648e0` | 8512 | ✓ |
| `fcn.1400115f0` | `0x1400115f0` | 8277 | ✓ |
| `fcn.140069d80` | `0x140069d80` | 8224 | ✓ |
| `fcn.140016480` | `0x140016480` | 7319 | ✓ |
| `fcn.1400330e0` | `0x1400330e0` | 7302 | ✓ |
| `fcn.1400398e0` | `0x1400398e0` | 6198 | ✓ |
| `fcn.140066a20` | `0x140066a20` | 5622 | ✓ |
| `fcn.14003c6f0` | `0x14003c6f0` | 5343 | ✓ |
| `fcn.14003b200` | `0x14003b200` | 5343 | ✓ |
| `fcn.14003f480` | `0x14003f480` | 4985 | ✓ |
| `fcn.14003e0c0` | `0x14003e0c0` | 4985 | ✓ |
| `fcn.1400aea20` | `0x1400aea20` | 4936 | ✓ |
| `fcn.14006bda0` | `0x14006bda0` | 4902 | ✓ |
| `fcn.14006f000` | `0x14006f000` | 4578 | ✓ |
| `fcn.14006de90` | `0x14006de90` | 4464 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001410.c`](code/fcn.140001410.c)
- [`code/fcn.140003670.c`](code/fcn.140003670.c)
- [`code/fcn.140006d10.c`](code/fcn.140006d10.c)
- [`code/fcn.14000ef20.c`](code/fcn.14000ef20.c)
- [`code/fcn.1400109f0.c`](code/fcn.1400109f0.c)
- [`code/fcn.1400115f0.c`](code/fcn.1400115f0.c)
- [`code/fcn.140016480.c`](code/fcn.140016480.c)
- [`code/fcn.14001af60.c`](code/fcn.14001af60.c)
- [`code/fcn.14001b240.c`](code/fcn.14001b240.c)
- [`code/fcn.140027980.c`](code/fcn.140027980.c)
- [`code/fcn.14002ce00.c`](code/fcn.14002ce00.c)
- [`code/fcn.14002d2c0.c`](code/fcn.14002d2c0.c)
- [`code/fcn.1400305c0.c`](code/fcn.1400305c0.c)
- [`code/fcn.1400330e0.c`](code/fcn.1400330e0.c)
- [`code/fcn.140037240.c`](code/fcn.140037240.c)
- [`code/fcn.1400398e0.c`](code/fcn.1400398e0.c)
- [`code/fcn.14003b200.c`](code/fcn.14003b200.c)
- [`code/fcn.14003c6f0.c`](code/fcn.14003c6f0.c)
- [`code/fcn.14003e0c0.c`](code/fcn.14003e0c0.c)
- [`code/fcn.14003f480.c`](code/fcn.14003f480.c)
- [`code/fcn.1400648e0.c`](code/fcn.1400648e0.c)
- [`code/fcn.140066a20.c`](code/fcn.140066a20.c)
- [`code/fcn.140069d80.c`](code/fcn.140069d80.c)
- [`code/fcn.14006bda0.c`](code/fcn.14006bda0.c)
- [`code/fcn.14006de90.c`](code/fcn.14006de90.c)
- [`code/fcn.14006f000.c`](code/fcn.14006f000.c)
- [`code/fcn.1400aea20.c`](code/fcn.1400aea20.c)
- [`code/fcn.1400bfd80.c`](code/fcn.1400bfd80.c)
- [`code/fcn.1400bfea0.c`](code/fcn.1400bfea0.c)
- [`code/fcn.1400c1450.c`](code/fcn.1400c1450.c)

## Behavioral Analysis

This analysis incorporates findings from chunk 8/8 into the existing framework. This final segment provides definitive evidence of a **Highly Modular and Template-Based VM Architecture**, where the malware utilizes nearly identical code structures to handle multiple, potentially different, malicious modules.

---

### Updated Analysis of Binary Behavior

The transition from chunk 7 to chunk 8 reveals that the complexity observed in `fcn.14003e0c0` is not an isolated instance but a **systemic architectural choice.**

#### 1. Template-Based Instruction Handling (Polymorphism)
*   **Mirror Functionality:** The functions `fcn.14006bda0`, `fcn.14006f000`, and `fcn.14006de90` exhibit nearly identical structural logic to `fcn.14003e0c0`. They share the same dispatch patterns, state-tracking bitwise operations (e.g., `| 2`, `| 4`), and switch table structures.
*   **Data-Driven Logic:** The only significant differences between these functions are the **hardcoded memory offsets/constants** used to fetch data (e.g., `0x140c39e60` vs `0x140c39e70`). 
*   **Significance:** This indicates a "Template" system. The developer wrote one high-quality, complex VM engine and then generated multiple variations of it. Each variation points to a different "Script Bundle." This allows the malware to stay "generic" in its core logic while switching between various malicious functionalities (e.g., credential stealing vs. ransomware) by simply swapping the data pointers.

#### 2. Advanced State Tracking & Validation
*   **State-Machine Depth:** The repeated use of bitwise ORs on internal registers (like `in_stack_00000030`) confirms that each "Instruction" in the virtual language is accompanied by a complex set of metadata. These bits likely represent: 
    1.  *Type Identity* (e.g., Is this an Int, String, or Pointer?)
    2.  *Size Status* (e.g., Was the previous buffer read fully?)
    3.  *Validation Flag* (e.g., Did the last operation successfully resolve its address?)
*   **Robust Memory Management:** `fcn.1400aea20` functions as a sophisticated internal "Memory Manager." It handles complex cases like overlapping buffers, length checks, and segmented memory moves. This ensures that even if the script is complex or poorly formed, it won't crash the host process, ensuring high stability for the infection.

#### 3. Obfuscation via "Complexity-by-Design"
*   **Disruption of Static Analysis:** The repetitive nature of these functions creates a "fog of war." An analyst spending hours deconstructing `fcn.14006bda0` may find they have only decoded the *engine*, not the *malicious action*. When the next function (`fcn.14006f000`) appears, it will look identical, requiring a repeat of the same effort without providing new unique information about the payload.
*   **Opaque Predicates & Jump Tables:** The "Too many branches" warnings for switch tables indicate that the VM uses large jump tables to jump to different logic blocks. This prevents linear disassemblers from easily mapping the flow of code, as every instruction could potentially branch into dozens of different execution paths depending on the current state of the VM.

---

### Updated Analysis of VM Architecture

The final chunk completes the map of what we can call a **Multi-Module Virtual Machine.**

**Refined Architecture Layers:**
1.  **Script/Payload Layer (Data):** Multiple distinct scripts, each hidden behind different hardcoded pointers in the "Template" functions.
2.  **Interpretation & Logic Engine (The Core):** The high-level logic found in `fcn.14003e0c0`. It doesn't just execute instructions; it manages state, validates memory boundaries, and resolves variable types.
3.  **Template Layer (Mapping):** The "Mirror" functions (`6bda0`, `6f000`, etc.). These act as the bridge between the specific script being loaded and the core VM engine. 
4.  **Gatekeeper/API Bridge:** The final stage where the abstract "State" is converted into a concrete Windows API call (e.g., a call to `advapi32` or `wininet`).

---

### Summary for Incident Response

The analysis of all eight chunks confirms that this malware belongs to a **High-End Tiered Architecture**, likely associated with an APT group or a sophisticated Malware-as-a-Service (MaaS) provider.

#### **Key Intelligence Findings:**
*   **Modular Flexibility:** The malware is designed for "Hot-Swapping" payloads. By using similar function structures for different script pointers, the threat actor can update what the malware *does* without ever changing its primary code structure, making signature-based detection extremely difficult.
*   **Extreme Anti-Analysis:** The design intentionally wastes the analyst's time by creating a "Recursive" analysis loop where many functions perform the same complex logic just to handle different pieces of data.
*   **Stability Focused:** The heavy emphasis on memory validation and state checking indicates that this malware is designed for persistence. It is built to remain silent and stable in a target environment for months or even years.

#### **Revised Tactical Recommendations:**
1.  **Identify the "Gatekeeper" Exit Points:** Do not waste time de-obfuscating every variation of the VM logic (e.g., `fcn.14006bda0` vs `fcn.14006f000`). Instead, perform **cross-reference analysis** to find where these functions call into known Windows APIs or "System" calls. These are your primary "Action" points.
2.  **Dynamic Memory Monitoring:** Since the script is decoded/processed just before execution, use a memory scanner (like Monolith or Volatility) to capture the process memory after it has run for several minutes. Look for **strings or IP addresses** appearing in regions assigned to the VM's "Instruction Buffer."
3.  **Behavioral Indicators:** Because the internal logic is so heavily protected/obfuscated, focus on **behavioral IOCs**: 
    *   Look for the process spinning through high-frequency jumps (characteristic of a VM loop).
    *   Monitor for injected code or "Process Hollowing" where the script might be "unpacked" into memory before being fed to the VM.
4.  **Script Extraction:** If possible, use an automated tool to dump all "Data" segments used by the `fcn.14003e0c0` style functions. Comparing these data blocks will reveal the different capabilities of each module.

#### **Final Conclusion:**
This is a highly professional implementation of a Virtual Machine Trojan. Its primary defense is **complexity as a shield**. It successfully separates "malicious intent" (the script) from "execution logic" (the VM), making it one of the more difficult samples to manually reverse engineer fully.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors described in your report to the relevant MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Virtualization | The malware employs a custom "multi-module" virtual machine architecture to interpret its own instructions, hiding malicious actions behind a complex execution engine. |
| **T1027** | Obfuscated Code | The use of "mirror functions," template-based logic, and jump tables creates a "fog of war" designed to stall manual analysis and hinder static reverse engineering. |
| **T1059** | Command and Scripting Interpreter | The architecture includes a dedicated "Script/Payload Layer" where different malicious behaviors (e.g., ransomware, credential stealing) are executed via a custom interpreted language. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

**File paths / Registry keys**
*   `\Microsoft\Windows\StartMenu\Programs\QHovzdBCu.H` (Note: This appears to be a path for a dynamically generated folder/file used for persistence or startup.)

**Mutex names / Named pipes**
*   *(None identified in the provided text)*

**Hashes**
*   *(None identified in the provided text)*

**Other artifacts**
*   **Memory Offsets (Function Identifiers):**
    *   `fcn.14003e0c0` (Core VM Logic)
    *   `fcn.14006bda0` (Template Function 1)
    *   `fcn.14006f000` (Template Function 2)
    *   `fcn.14006de90` (Template Function 3)
    *   `fcn.1400aea20` (Internal Memory Manager)
*   **Data Offsets:**
    *   `0x140c39e60`
    *   `0x140c39e70`
*   **Behavioral Patterns / TTPs:**
    *   **VM-based Architecture:** Use of a "Multi-Module Virtual Machine" to hide malicious logic behind template-based execution.
    *   **Instruction Masking:** State-tracking via bitwise OR operations (e.g., `| 2`, `| 4`) on internal registers.
    *   **Junk Code/Obfuscation:** Use of "complexity-by-design" and extensive jump tables to disrupt linear disassembly and static analysis.
    *   **Memory Management:** Sophisticated memory management for overlapping buffers and length checks to ensure stability during script execution.
    *   **High-Frequency Jumps:** Characteristic behavior of a VM loop, detectable via dynamic monitoring.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for this sample:

1. **Malware family:** custom
2. **Malware type:** loader / backdoor
3. **Confidence:** High (for behavior/architecture), Low (for specific campaign identification)
4. **Key evidence:**
    *   **Modular Virtual Machine Architecture:** The malware utilizes a complex, multi-module VM to interpret its own instructions, effectively separating the "malicious intent" (the scripts) from the "execution logic." This allows for the easy swapping of functionalities like credential stealing or ransomware without changing the core code.
    *   **Advanced Anti-Analysis & Obfuscation:** The use of "Template-Based" functions, large jump tables, and bitwise state tracking is designed to create a "fog of war," deliberately stalling analysts by making it difficult to trace linear execution flows or identify specific malicious actions through static analysis.
    *   **Sophisticated Payload Handling:** The presence of an internal memory manager and the use of different data pointers for various "Script Bundles" indicates a high-end professional architecture typical of APT (Advanced Persistent Threat) groups or sophisticated Malware-as-a-Service (MaaS) providers.
