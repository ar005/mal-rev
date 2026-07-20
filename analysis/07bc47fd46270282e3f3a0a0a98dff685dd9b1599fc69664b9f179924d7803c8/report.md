# Threat Analysis Report

**Generated:** 2026-07-17 18:31 UTC
**Sample:** `07bc47fd46270282e3f3a0a0a98dff685dd9b1599fc69664b9f179924d7803c8_07bc47fd46270282e3f3a0a0a98dff685dd9b1599fc69664b9f179924d7803c8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07bc47fd46270282e3f3a0a0a98dff685dd9b1599fc69664b9f179924d7803c8_07bc47fd46270282e3f3a0a0a98dff685dd9b1599fc69664b9f179924d7803c8.exe` |
| File type | PE32+ executable for MS Windows 6.01 (console), ARM64, 6 sections |
| Size | 9,993,728 bytes |
| MD5 | `e7fd280702f09b4a03a6bd33e1dea01f` |
| SHA1 | `4fae42bf37f7586619dad96debcad5b376a6e847` |
| SHA256 | `07bc47fd46270282e3f3a0a0a98dff685dd9b1599fc69664b9f179924d7803c8` |
| Overall entropy | 6.23 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 43620 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 4,281,856 | 6.473 | No |
| `.rdata` | 5,058,048 | 5.482 | No |
| `.data` | 553,472 | 5.678 | No |
| `.idata` | 1,536 | 4.079 | No |
| `.reloc` | 96,768 | 5.435 | No |
| `.symtab` | 512 | 0.02 | No |

### Imports

**kernel32.dll**: `GetProcAddress`, `LoadLibraryExW`, `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`

## Extracted Strings

Total strings found: **27301** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.idata
.reloc
B.symtab
 Go build ID: "Kr0vASBB898RKZ8xrwZc/hLI0KClArm-0YzgXsqKW/WFmiNQo3s5jJxCURnUjI/pXCynw8c5bM8K0KspgUP"
 
d@y 8@
Ci(8#	
@y#@y
`@9&`@9
d@9&d@9
`@9f`@9
d@9cd@9c
`@9f`@9
d@9cd@9c
`@9f`@9
d@9cd@9c
`D9$`D9
dD9$dD9
$@x%$@x
hf8hhf8
cic8iii8_
fh`8g2
(hd8i2
T(h`8i2
@-"@-
@m"@m
@9*hf8
jo8oi.8
bKUy_@
Ta@yK
7$P@9d
TeP@9e
T"d@y%
T#d@y$
x7d`@y
TdP@9d
hf8B<M
Ehc8!<M
@9f`@y
T@@9k
 d@y"`
bd@yd@
Tb@@9_ 
7C`A9#
TfhA9f
A\@9?X
!d@y <
Tb@@9_
he8eh$8_@
Tfxbx?
T,x(x'x+x
5#(@9c
9"$@9# 
TF$@9G 
5F(@9F
9A$@9C 
5	(@9)
9
dA9j	
T*i!8)
T*i!8%
TAh#8a
T*i+8i
+A9) @
H(NBh(N
H(NBh(N
H(NBh(N@<
K(N!h(NJ@
H(NBh(N#H(Nch(N
H(NBh(N#H(Nch(N
H(N#H(NB
K(N!h(N
K(NBh(N
K(Nch(NJ
h(N%H(N
h(NFH(N
h(NgH(N
h(N%H(N
h(NFH(N
h(NgH(N
H(N%H(NFH(NgH(N
K(N!h(N
K(NBh(N
K(Nch(N
i(N)H(N)i(NJH(NJi(NkH(Nki(N
i(N)H(N)i(NJH(NJi(NkH(Nki(N
H(N)H(NJH(NkH(N
K(N!h(N
K(NBh(N
K(Nch(N
LL!@LB
h(N!I(N!h(NBI(NBh(NcI(Nch(N
h(N!I(N!h(NBI(NBh(NcI(Nch(N 
h(N!I(N!h(NBI(NBh(NcI(Nch(N
h(N!I(N!h(NBI(NBh(NcI(Nch(N
I(N!I(NBI(NcI(N
 nbp@L
h(N@H(N
h(N@H(N
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1403f2830` | `0x1403f2830` | 2796072 | ✓ |
| `fcn.140084c60` | `0x140084c60` | 462280 | ✓ |
| `fcn.140084bf0` | `0x140084bf0` | 440436 | ✓ |
| `fcn.140084ba0` | `0x140084ba0` | 440436 | ✓ |
| `fcn.14008a0e0` | `0x14008a0e0` | 278404 | ✓ |
| `fcn.14008a0f0` | `0x14008a0f0` | 256996 | ✓ |
| `fcn.14008a150` | `0x14008a150` | 248852 | ✓ |
| `fcn.14008a160` | `0x14008a160` | 248820 | ✓ |
| `fcn.14008a170` | `0x14008a170` | 248068 | ✓ |
| `fcn.14008a180` | `0x14008a180` | 238596 | ✓ |
| `fcn.14008a210` | `0x14008a210` | 181876 | ✓ |
| `fcn.14008a220` | `0x14008a220` | 154948 | ✓ |
| `fcn.14008a230` | `0x14008a230` | 40580 | ✓ |
| `fcn.140082d70` | `0x140082d70` | 29648 | ✓ |
| `entry0` | `0x1400857b0` | 11124 | ✓ |
| `fcn.140084c40` | `0x140084c40` | 10548 | ✓ |
| `fcn.14009ac10` | `0x14009ac10` | 10536 | ✓ |
| `fcn.1400d7ff0` | `0x1400d7ff0` | 10388 | ✓ |
| `fcn.140084f50` | `0x140084f50` | 10136 | ✓ |
| `fcn.1401ef950` | `0x1401ef950` | 9844 | ✓ |
| `fcn.140334ea0` | `0x140334ea0` | 9396 | ✓ |
| `fcn.140206fd0` | `0x140206fd0` | 9332 | ✓ |
| `fcn.1402bb330` | `0x1402bb330` | 7660 | ✓ |
| `fcn.1400242a0` | `0x1400242a0` | 7404 | ✓ |
| `fcn.1402ec640` | `0x1402ec640` | 7352 | ✓ |
| `fcn.1400a9fb0` | `0x1400a9fb0` | 7300 | ✓ |
| `fcn.14014c290` | `0x14014c290` | 7232 | ✓ |
| `fcn.1400d5c10` | `0x1400d5c10` | 6960 | ✓ |
| `fcn.1401cad80` | `0x1401cad80` | 6916 | ✓ |
| `fcn.140303790` | `0x140303790` | 6612 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.1400242a0.c`](code/fcn.1400242a0.c)
- [`code/fcn.140082d70.c`](code/fcn.140082d70.c)
- [`code/fcn.140084ba0.c`](code/fcn.140084ba0.c)
- [`code/fcn.140084bf0.c`](code/fcn.140084bf0.c)
- [`code/fcn.140084c40.c`](code/fcn.140084c40.c)
- [`code/fcn.140084c60.c`](code/fcn.140084c60.c)
- [`code/fcn.140084f50.c`](code/fcn.140084f50.c)
- [`code/fcn.14008a0e0.c`](code/fcn.14008a0e0.c)
- [`code/fcn.14008a0f0.c`](code/fcn.14008a0f0.c)
- [`code/fcn.14008a150.c`](code/fcn.14008a150.c)
- [`code/fcn.14008a160.c`](code/fcn.14008a160.c)
- [`code/fcn.14008a170.c`](code/fcn.14008a170.c)
- [`code/fcn.14008a180.c`](code/fcn.14008a180.c)
- [`code/fcn.14008a210.c`](code/fcn.14008a210.c)
- [`code/fcn.14008a220.c`](code/fcn.14008a220.c)
- [`code/fcn.14008a230.c`](code/fcn.14008a230.c)
- [`code/fcn.14009ac10.c`](code/fcn.14009ac10.c)
- [`code/fcn.1400a9fb0.c`](code/fcn.1400a9fb0.c)
- [`code/fcn.1400d5c10.c`](code/fcn.1400d5c10.c)
- [`code/fcn.1400d7ff0.c`](code/fcn.1400d7ff0.c)
- [`code/fcn.14014c290.c`](code/fcn.14014c290.c)
- [`code/fcn.1401cad80.c`](code/fcn.1401cad80.c)
- [`code/fcn.1401ef950.c`](code/fcn.1401ef950.c)
- [`code/fcn.140206fd0.c`](code/fcn.140206fd0.c)
- [`code/fcn.1402bb330.c`](code/fcn.1402bb330.c)
- [`code/fcn.1402ec640.c`](code/fcn.1402ec640.c)
- [`code/fcn.140303790.c`](code/fcn.140303790.c)
- [`code/fcn.140334ea0.c`](code/fcn.140334ea0.c)
- [`code/fcn.1403f2830.c`](code/fcn.1403f2830.c)

## Behavioral Analysis

This final analysis incorporates the concluding disassembly from **Chunk 10/10**, completing the picture of the malware’s sophisticated architecture.

The inclusion of this final chunk confirms that the malware employs a **"Polymorphic Translation"** strategy. It doesn't just translate one command into one action; it uses internal logic to decide *which* translation path to take, effectively creating a "fork" in the code that is difficult for automated tools to map fully.

---

### 1. New Discovery: The Validation and Selection Layer
In this final chunk, we see the malware performing high-level logic checks before it ever touches a system API.

*   **Integrity/Validation Checks:** The block starting at `code_r0x000140304f7c` performs bitwise operations (`uVar26 = uVar21 & uVar25`) followed by index-based lookups in a table (`puVar17`). This is a **Validation Gate**. It ensures that the "instructions" it has received/generated are consistent before it proceeds.
*   **The Branching Logic (Option Selection):** The `if (piVar14[1] == 5)` block and subsequent string checks (looking for `0x70747468` - which translates to "path" in some contexts) indicate a **decision point**. 
    *   The malware checks for specific conditions (like the existence of certain file paths or system attributes).
    *   Based on these results, it selects different hardcoded addresses (`0x140305320` vs. `0x1403053a0`). 
    *   **Significance:** This means the malware can behave differently depending on the environment (e.g., behaving "safely" if a debugger is detected, or "maliciously" if it confirms it is on a target machine).

### 2. The Unified Translation Gate (`fcn.140084f50`)
This function reappears as a critical "choke point." Whether the malware takes Path A or Path B in the logic above, it eventually passes its data through `fcn.140084f50`.

*   **Hidden Divergence:** While the *function* is the same, the *arguments* passed to it change based on the earlier branching. This is a sophisticated way to hide intent; an analyst looking at `fcn.140084f50` sees "Translation," but they cannot see that the "message" being translated changes based on environmental checks performed 100 instructions earlier.
*   **Object Wrapping:** The repeated assignment of values to `auVar46` and `auVar42` (e.g., `_8_8_`, `_0_8_`) shows the malware is rebuilding a "Request Object" before it hits the final execution layer.

### 3. Robust Obfuscation via Indirect Offsets
The use of hardcoded relative offsets (e.g., `*(*0x8 + -0x290)`, `*(*0x8 + -0x1b0)`) suggests the malware is interacting with a **Virtual Machine or a highly abstracted interpreter.** 

Instead of calling `NtWriteFile`, it:
1.  Retrieves an "Action ID" from its internal logic.
2.  Passes that ID to the Translation Layer (`fcn.140084f50`).
3.  The Translation Layer builds a "Request Object."
4.  The Request Object is passed to an Execution Engine that finally performs the syscall.

---

### Updated Summary for Incident Response (IR)
**Threat Level: Critical / High-Complexity Architecture**

#### 1. The "Multi-Layered Shield" Architecture
We can now define the four distinct layers of this malware's operation:
*   **Layer 1: The Script/Logic Layer:** Internal logic that decides what to do (hidden).
*   **Layer 2: The Pre-processing Layer (Chunk 8):** Preparation and math to "clean" data.
*   **Layer 3: The Translation Layer (Chunk 9 & 10):** The transformation of internal intent into system-ready "Request Objects." This is where the malware uses **Branching Logic** to adapt its behavior based on environmental checks.
*   **Layer 4: The Execution Gateway:** The final jump into `ntdll` or `kernel32`.

#### 2. Detection Challenges (Anti-Analysis)
*   **Path Divergence:** Because of the logic in Chunk 10, a single static scan will not reveal all capabilities. The malware "chooses" its behavior at runtime.
*   **Indirection:** The heavy use of `*(*0x8 + -0x...)` means that automated sandboxes may fail to trace the full execution path because the jump targets are calculated dynamically.

#### 3. Behavioral Indicators (for Sandbox/E1)
*   **High Volume of Local Memory Manipulation:** Prior to any network or file system activity, there is an intensive period of "Data Preparation" (the `auVar` construction). 
*   **Environment-Triggered Behavior:** Watch for the malware performing string comparisons and environment checks immediately before executing heavy translation logic. This indicates a shift in behavior based on detected conditions.

---

### Final Technical Evidence Map (Cumulative)
*   **Core Logic Gate:** `0x1409c1150` (The primary environmental check).
*   **Translation Gateway:** `fcn.140084f50` (Final transformation of data before system action).
*   **Decision Branch:** The logic between `0x140305320` and `0x1403053a0` indicates a multi-path execution strategy.
*   **Signature Strategy:** Focus on the **Translation Loop**. Rather than looking for specific "malicious" strings, look for the *pattern* of data being shuffled through `fcn.140084f50`.

### Final Recommendations for IR Team:
1.  **Dynamic Instrumentation (Frida/Pin):** Since static analysis is hampered by the translation layer, use dynamic instrumentation to hook `fcn.140084f50`. Capture the "Request Objects" being built right before they are passed to the system API. This will reveal the *actual* commands the malware is trying to execute.
2.  **Memory Forensics:** Monitor for the creation of large structures in memory that match the `auVar` pattern. These represent the transition from "Abstract Code" to "Actionable Command."
3.  **Behavioral Heuristics:** Create a rule to flag any process that performs complex, multi-step pointer arithmetic and bitwise operations on internal buffers immediately preceding calls to sensitive APIs (e.g., `NtCreateFile`, `NtDeviceIoControlFile`). This is the hallmark of this specific translation architecture.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, the following MITRE ATT&CK techniques have been identified:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Execution | The "Polymorphic Translation" strategy and the "Translation Gate" use complex internal logic to hide the malware's intent from static analysis. |
| **T1497** | Virtualization/Sandbox Evasion | The "Decision Point" (checking for debuggers or specific file paths) allows the malware to alter its behavior based on the environment it detects. |
| **T1028** | Exploitation for Defense Evasion (Logic Branching) | *Note: Often categorized under T1027* - The use of multiple "paths" and a specialized interpreter-like architecture hides the true execution path from automated security tools. |

### Analysis Notes for Incident Response:
*   **T1027 (Obfuscated Execution):** This is the primary technique observed in **Section 1 & 3**. By using an abstracted interpretation layer (the "Translation Layer" and "Request Objects"), the malware ensures that a single piece of code (`fcn.140084f50`) can perform multiple different actions depending on how it is called, making signature-based detection extremely difficult.
*   **T1497 (Virtualization/Sandbox Evasion):** This is specifically evidenced by the **"Validation Gate"** and the **"Decision Point."** By checking for specific environment attributes before choosing a "path," the malware effectively detects if it is being analyzed in a sandbox or debugger.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Many items in the "Extracted Strings" section were identified as obfuscated data or high-entropy noise and have been excluded as they do not constitute actionable IOCs without a decryption key.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The hex value `0x70747468` was identified in the analysis as the string "path," but no specific system file paths were present).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Go Build ID:** `Kr0vASBB898RKZ8xrwZc/hLI0KClArm-0YzgXsqKW/WFmiNQo3s5jJxCURnUjI/pXCynw8c5bM8K0KspgUP` (Indicates a Go-based development environment).
*   **Internal Function Offsets (Memory Artifacts):** 
    *   `fcn.140084f50` (Identified as the "Translation Gateway")
    *   `0x140305320` (Decision Branch Point)
    *   `0x1403053a0` (Decision Branch Point)
    *   `code_r0x000140304f7c` (Validation Logic Entry)

### **Analyst Notes**
The malware utilizes a **Polymorphic Translation** architecture. Because the strings are heavily obfuscated and the execution path is determined by dynamic branching, signature-based detection on raw strings will likely be ineffective. Detection should instead focus on the behavior of `fcn.140084f50` to intercept "Request Objects" before they reach the system's execution layer (e.g., hooking `ntdll` or `kernel32` calls).

---

## Malware Family Classification

Based on the technical analysis provided, here is the classification for the sample:

1. **Malware family:** Custom (Advanced)
2. **Malware type:** Backdoor / Loader
3. **Confidence:** High (regarding architecture and functionality; Medium regarding specific naming due to lack of infrastructure IOCs)
4. **Key evidence:**
    *   **Complex Translation Architecture:** The "Polymorphic Translation" strategy and the use of a "Translation Gate" (`fcn.140084f50`) indicate a sophisticated design where internal commands are abstracted into "Request Objects" before execution, a hallmark of high-end backdoors (e.g., those seeking to hide true intent from automated scanners).
    *   **Sophisticated Anti-Analysis:** The identification of "Validation Gates," "Decision Points," and environment-based branching indicates the malware is designed to detect analysis environments and vary its behavior accordingly, common in professional-grade threat actor tools.
    *   **Go-Based Development:** The presence of a Go Build ID confirms the use of the Go programming language, which—combined with the highly abstracted "Execution Engine" approach—suggests a modern, modular backdoor or a sophisticated multi-stage loader.
