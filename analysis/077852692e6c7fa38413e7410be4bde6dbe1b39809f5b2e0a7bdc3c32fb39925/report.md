# Threat Analysis Report

**Generated:** 2026-07-16 20:07 UTC
**Sample:** `077852692e6c7fa38413e7410be4bde6dbe1b39809f5b2e0a7bdc3c32fb39925_077852692e6c7fa38413e7410be4bde6dbe1b39809f5b2e0a7bdc3c32fb39925.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `077852692e6c7fa38413e7410be4bde6dbe1b39809f5b2e0a7bdc3c32fb39925_077852692e6c7fa38413e7410be4bde6dbe1b39809f5b2e0a7bdc3c32fb39925.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, 6 sections |
| Size | 1,718,688 bytes |
| MD5 | `a4caff90d789bd81b7300299e92e9959` |
| SHA1 | `502b0ac032d09d6e25d2d41078b3a86be998801e` |
| SHA256 | `077852692e6c7fa38413e7410be4bde6dbe1b39809f5b2e0a7bdc3c32fb39925` |
| Overall entropy | 6.532 |
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
| `.text` | 676,864 | 6.192 | No |
| `.rdata` | 784,384 | 5.584 | No |
| `.data` | 215,552 | 7.751 | ⚠️ Yes |
| `.idata` | 1,536 | 3.866 | No |
| `.reloc` | 37,888 | 6.649 | No |
| `.symtab` | 512 | 0.02 | No |

### Imports

**kernel32.dll**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetUnhandledExceptionFilter`, `SetProcessPriorityBoost`

## Extracted Strings

Total strings found: **6344** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.idata
.reloc
B.symtab
 Go build ID: "XbiKSpS5S3pJube62PS2/YsTR8AbHK1CEFaYVQq8X/mYXUFR0cs51Y322z46qO/ioqtIobyY6YaJyjzc2H5"
 
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
|$9;u
D$(9H(v6
#t$$#L$(
#\$$#D$(
#\$,#|$0
#l$(#L$,
#l$(#L$,
#t$8#L$<
#t$8#L$<
#l$,#L$0
#t$<#L$@
#t$,#L$0
#t$,#L$0
#D$8#L$<
#t$4#L$8
#t$0#L$4
|$ 9;u
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
D$<9D$
D$49D$
D$ 9D$
	;av|
|$09GDu
L$(9Aw
L$ 9A4t 
L$(f9A
D$$+D$
u 9r tL
D$,+D$
T$+B
D$49D$
L$H9A4v
L$$9A(s
\$09S4
u
9Hw
	;avL
L$+A
L$ 9H<s
L$09A4v
T$(9J4s
T$89B4v
L$ #D$$#L$(
UUUU%UUUU
T$ 9T$
D$09D$
uP9uTu1
9T$,t-
D$49D$
D$L9D$
L$<9L$@
tC9A(t>
L$49L$
|$ u	1
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
D$89D$
D$89D$
D$,9D$
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00473c60` | `0x473c60` | 431600 | ✓ |
| `fcn.00473c80` | `0x473c80` | 411024 | ✓ |
| `fcn.00473cc0` | `0x473cc0` | 410992 | ✓ |
| `fcn.00473e00` | `0x473e00` | 229469 | ✓ |
| `fcn.00473e10` | `0x473e10` | 229341 | ✓ |
| `fcn.00473e20` | `0x473e20` | 229213 | ✓ |
| `fcn.00473e30` | `0x473e30` | 229085 | ✓ |
| `fcn.00473e40` | `0x473e40` | 228957 | ✓ |
| `fcn.00473e50` | `0x473e50` | 228829 | ✓ |
| `fcn.00473e60` | `0x473e60` | 228701 | ✓ |
| `fcn.00473e70` | `0x473e70` | 228573 | ✓ |
| `fcn.00473e80` | `0x473e80` | 228445 | ✓ |
| `fcn.00473e90` | `0x473e90` | 228317 | ✓ |
| `fcn.00473ea0` | `0x473ea0` | 228189 | ✓ |
| `fcn.00473eb0` | `0x473eb0` | 220977 | ✓ |
| `fcn.00473ed0` | `0x473ed0` | 220849 | ✓ |
| `entry0` | `0x4748a0` | 8757 | ✓ |
| `fcn.004a0290` | `0x4a0290` | 7950 | ✓ |
| `fcn.00419250` | `0x419250` | 7080 | ✓ |
| `fcn.00473c40` | `0x473c40` | 6351 | ✓ |
| `fcn.00473d90` | `0x473d90` | 6042 | ✓ |
| `fcn.0041d3c0` | `0x41d3c0` | 5456 | ✓ |
| `fcn.004452b0` | `0x4452b0` | 5016 | ✓ |
| `fcn.004a28d0` | `0x4a28d0` | 4302 | ✓ |
| `fcn.0047ced0` | `0x47ced0` | 3834 | ✓ |
| `fcn.0042b360` | `0x42b360` | 3466 | ✓ |
| `fcn.00498b40` | `0x498b40` | 3349 | ✓ |
| `fcn.00468870` | `0x468870` | 3331 | ✓ |
| `fcn.0048ff80` | `0x48ff80` | 3204 | ✓ |
| `fcn.00454b10` | `0x454b10` | 3171 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00419250.c`](code/fcn.00419250.c)
- [`code/fcn.0041d3c0.c`](code/fcn.0041d3c0.c)
- [`code/fcn.0042b360.c`](code/fcn.0042b360.c)
- [`code/fcn.004452b0.c`](code/fcn.004452b0.c)
- [`code/fcn.00454b10.c`](code/fcn.00454b10.c)
- [`code/fcn.00468870.c`](code/fcn.00468870.c)
- [`code/fcn.00473c40.c`](code/fcn.00473c40.c)
- [`code/fcn.00473c60.c`](code/fcn.00473c60.c)
- [`code/fcn.00473c80.c`](code/fcn.00473c80.c)
- [`code/fcn.00473cc0.c`](code/fcn.00473cc0.c)
- [`code/fcn.00473d90.c`](code/fcn.00473d90.c)
- [`code/fcn.00473e00.c`](code/fcn.00473e00.c)
- [`code/fcn.00473e10.c`](code/fcn.00473e10.c)
- [`code/fcn.00473e20.c`](code/fcn.00473e20.c)
- [`code/fcn.00473e30.c`](code/fcn.00473e30.c)
- [`code/fcn.00473e40.c`](code/fcn.00473e40.c)
- [`code/fcn.00473e50.c`](code/fcn.00473e50.c)
- [`code/fcn.00473e60.c`](code/fcn.00473e60.c)
- [`code/fcn.00473e70.c`](code/fcn.00473e70.c)
- [`code/fcn.00473e80.c`](code/fcn.00473e80.c)
- [`code/fcn.00473e90.c`](code/fcn.00473e90.c)
- [`code/fcn.00473ea0.c`](code/fcn.00473ea0.c)
- [`code/fcn.00473eb0.c`](code/fcn.00473eb0.c)
- [`code/fcn.00473ed0.c`](code/fcn.00473ed0.c)
- [`code/fcn.0047ced0.c`](code/fcn.0047ced0.c)
- [`code/fcn.0048ff80.c`](code/fcn.0048ff80.c)
- [`code/fcn.00498b40.c`](code/fcn.00498b40.c)
- [`code/fcn.004a0290.c`](code/fcn.004a0290.c)
- [`code/fcn.004a28d0.c`](code/fcn.004a28d0.c)

## Behavioral Analysis

This final chunk of disassembly completes the picture of an extremely sophisticated, high-tier malware loader. The addition of `fcn.0048ff80` and `fcn.00454b10` reveals that the malware employs **Opaque Predicates**, **Internal Integrity Checks**, and **Automated State Management** to protect its transition into the primary payload.

Here is the updated analysis incorporating all three chunks of data.

---

### Updated Analysis & Findings

#### 1. Advanced Decryption Dispatcher (`fcn.0047ced0`)
*(Retained from previous analysis)*
This function acts as a **multi-stage decryption engine**. It uses "magic" constants (e.g., `0x16d806e3`) to route different data blocks through specific arithmetic permutations. The use of bitwise logic combined with multipliers (`* 0x1b3`) ensures that the payload remains encrypted until the exact moment it is needed by the execution flow.

#### 2. Mathematical Obfuscation & Opaque Predicates (`fcn.0048ff80`)
This function represents a high level of engineering in anti-analysis:
*   **Complex Arithmetic for Simple Constants:** The use of values like `0x33333333` in multi-step arithmetic (e.g., `uVar12 * 0x33333333 + ...`) is a classic technique to hide simple integers or offsets from static analysis tools. A human looks at the code and sees complex math; the CPU executes it as a simple constant.
*   **Opaque Predicates:** The nested, convoluted "if" statements (e.g., `if (param_2 == (-(uVar12 < 0x20) & 1 << (uVar12 & 0x1f)))`) are likely "opaque predicates." These are conditions that always evaluate to true or false but are structured so complex that automated de-obfuscators cannot simplify them, effectively creating a "maze" for the analyst.
*   **High Entropy Logic:** The sheer amount of bit-shifting and masking suggests that even the internal logic used to calculate memory offsets is intentionally obscured to prevent researchers from finding fixed jump targets.

#### 3. Internal Integrity & "Passport" Validation (`fcn.00454b10`)
This function appears to be a **self-check or environment validation routine**.
*   **Identity Verification:** The checks like `if (piVar12[2] != -0x4d2)` and comparisons between `piVar12` and `piVar14` suggest the loader is verifying its own integrity. It is checking if it has been tampered with or if certain "keys" are present in memory before proceeding.
*   **Hidden Resource Mapping:** The repetition of calls to `fcn.0043f600`, `fcn.0043f580`, and `fcn.0043f2f0` suggests the loader is traversing a table of resources or capabilities. It only "unlocks" certain features if it passes the internal checks, ensuring that basic sandboxes only see a fraction of the malware's true functionality.

#### 4. Complex Data Structure Parsing & Dynamic Offsets (`fcn.004a28d0`, `fcn.00468870`)
*(Retained from previous analysis)*
These functions handle the "Map" of the decrypted payload. By using custom offsets and complex loops to parse internal headers, the loader ensures that even if a researcher finds a piece of the payload in memory, they won't know what it does because its "map" (the instructions on how to call its functions) is hidden within this complex parsing logic.

---

### Updated Summary of Risk Indicators

| Feature | Observation | Severity | Purpose |
| :--- | :--- | :--- | :--- |
| **Multi-Stage Decryption** | Multi-branch logic (`fcn.0047ced0`) using distinct keys for different data segments. | **Critical** | Prevents "dumping" the entire payload in one go; only parts are decrypted as needed. |
| **Opaque Predicates** | Complex bitwise/math logic to hide simple truth values (`fcn.0048ff80`). | **High** | Confuses both human analysts and automated de-obfuscation tools. |
| **Internal Integrity Checks** | Conditional jumps based on internal "magic" values (`fcn.00454b10`). | **High** | Prevents the loader from executing if it detects a debugger or an altered memory state. |
| **Floating-Point Obfuscation** | Use of `float8` to hide integer constants/addresses. | **High** | Bypasses standard "string" and "constant" scans in automated sandboxes. |
| **Just-in-Time (JIT) Gating** | Repeated calls to "gatekeeper" functions (`fcn.00472990`) before critical jumps. | **Medium** | Ensures the environment is still "safe" at every step of the unpacking process. |

---

### Final Conclusion
The analysis of all three segments confirms that this is a **highly sophisticated, multi-layered malware loader**. It does not rely on a single trick; rather, it uses a "defense-in-depth" strategy:
1.  **Layer 1 (Storage):** Uses complex math and floating-point arithmetic to hide constants from static scanners.
2.  **Layer 2 (Decryption):** Employs a multi-key dispatcher to ensure only the necessary components of the payload are in plaintext at any given time.
3.  **Layer 3 (Execution Gatekeeping):** Uses opaque predicates and internal integrity checks to "test" the environment at every step, ensuring that if an analyst tries to jump ahead or force execution, the loader will fail or divert into a harmless path.

**Conclusion:** This is likely a high-end professional threat actor's tool (e.g., for a state-sponsored group or advanced ransomware operator). The level of effort required to implement this specific type of mathematical obfuscation and multi-stage decryption suggests a highly developed development cycle.

---

## MITRE ATT&CK Mapping

Based on your behavioral analysis of the malware loader, here are the corresponding MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of multi-stage decryption, complex mathematical transformations for simple constants, and floating-point obfuscation are primary methods to hide the payload's true purpose from static analysis. |
| **T1497** | Virtualization/Sandbox Detection | Internal integrity checks ("Passport" validation) and "Just-in-Time (JIT) Gating" are used to detect if the loader is running in a sandbox or a researcher’s environment to limit its functionality. |
| **T1028** | Modify System Configuration | *(Not applicable - Note: While the malware checks system state, it does not appear to be modifying configurations based on this analysis.)* |

### Analysis Breakdown for Mapping:
*   **Obfuscated Files or Information (T1027):** This covers your observations of **Opaque Predicates**, **Mathematical Obfuscation**, and **Multi-Stage Decryption**. These techniques are specifically designed to defeat automated tools (like disassemblers) and human analysts by making the control flow and data structures difficult to interpret.
*   **Virtualization/Sandbox Detection (T1497):** This maps to your observations of **Internal Integrity Checks** and **JIT Gating**. These behaviors are intended to detect "artificial" environments; if a sandbox is detected, the malware provides only limited functionality or fails to execute, preventing the full payload from being analyzed.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Please note: The majority of the "EXTRACTED STRINGS" section consists of obfuscated data or internal code labels rather than actionable IOCs. 

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: While strings like `8fileu` and `8pipeu` appear, they are internal markers/labels for "file" and "pipe" logic rather than specific system paths).

**Mutex names / Named pipes**
*   None identified. 

**Hashes**
*   None identified. (A **Go build ID** was found: `XbiKSpS5S3pJube62PS2/YsTR8AbHK1CEFaYVQq8X/mYXUFR0cs51Y322z46qO/ioqtIobyY6YaJyjzc2H5`. While not a standard file hash like MD5/SHA256, it is a unique identifier used to distinguish specific builds of the binary).

**Other artifacts**
*   **Magic Constant:** `0x16d806e3` (Used as a routing constant for multi-stage decryption logic).
*   **Internal Functions/Offests (Behavioral Markers):** 
    *   `fcn.0047ced0` (Decryption Dispatcher)
    *   `fcn.0048ff80` (Opaque Predicate handler)
    *   `fcn.00454b10` (Integrity/Passport validation)
    *   `fcn.0043f600`, `fcn.0043f580`, `fcn.0043f2f0` (Resource mapping routine)

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High
4. **Key evidence**: 
*   **Sophisticated Evasion Techniques:** The use of "Opaque Predicates" (`fcn.0048ff80`), complex mathematical obfuscation, and floating-point tricks indicates a high-tier effort to bypass automated sandbox analysis and manual de-obfuscation.
*   **Multi-Stage Decryption Architecture:** The loader utilizes a multi-key "decryption dispatcher" (`fcn.0047ced0`) to ensure that the primary payload remains encrypted in memory until the moment of execution, preventing simple "dumping" by researchers.
*   **Environment Validation (Anti-Analysis):** The presence of "Passport" validation and "Just-in-Time (JIT) Gating" confirms the malware is designed to detect and evade analysis environments before it proceeds with its primary mission.
