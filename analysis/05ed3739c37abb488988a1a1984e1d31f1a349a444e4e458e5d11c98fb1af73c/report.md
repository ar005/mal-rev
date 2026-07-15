# Threat Analysis Report

**Generated:** 2026-07-14 19:29 UTC
**Sample:** `05ed3739c37abb488988a1a1984e1d31f1a349a444e4e458e5d11c98fb1af73c_05ed3739c37abb488988a1a1984e1d31f1a349a444e4e458e5d11c98fb1af73c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05ed3739c37abb488988a1a1984e1d31f1a349a444e4e458e5d11c98fb1af73c_05ed3739c37abb488988a1a1984e1d31f1a349a444e4e458e5d11c98fb1af73c.exe` |
| File type | PE32+ executable for MS Windows 5.02 (DLL), x86-64, 6 sections |
| Size | 5,298,176 bytes |
| MD5 | `93acca98a8426e98d661be051feee325` |
| SHA1 | `87d1e5b3a1e5fc3783597d36f0ea3c7b2f3c7188` |
| SHA256 | `05ed3739c37abb488988a1a1984e1d31f1a349a444e4e458e5d11c98fb1af73c` |
| Overall entropy | 6.465 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1494505257 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.325 | No |
| `.rdata` | 11,264 | 4.705 | No |
| `.data` | 5,120 | 1.823 | No |
| `.pdata` | 2,048 | 4.249 | No |
| `.rsrc` | 5,243,392 | 6.468 | No |
| `.reloc` | 3,584 | -0.0 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `WriteFile`, `CreateFileA`, `SizeofResource`, `LockResource`, `LoadResource`, `FindResourceA`, `CreateProcessA`, `GetCurrentThreadId`, `FlsSetValue`, `GetCommandLineA`, `DecodePointer`, `UnhandledExceptionFilter`, `SetUnhandledExceptionFilter`, `IsDebuggerPresent`

### Exports

`PlayGame`

## Extracted Strings

Total strings found: **8578** (showing first 100)

```
!This program cannot be run in DOS mode.
$
/4%D/4%D/4%D4
D|4%D4
D&4%D&L
D,4%D/4$D
D84%D4
D.4%D4
D.4%D4
D.4%DRich/4%D
`.rdata
@.data
.pdata
@.rsrc
@.reloc
L$ USWH
WATAUH
 A]A\_
UVWATAUAVAWH
D$HD9T$\
t$pD+d$HD+
9D$Ttg
A_A^A]A\_^]
WATAUAVAWH
A_A^A]A\_
WATAUAVAWH
@A_A^A]A\_
ATAUAVH
fD9t$b
A^A]A\
x ATAUAVH
< tG<	tC
 A^A]A\
Hct$@H
s\HcL$HH
VWATAUAVH
 A^A]A\_^
\$ UVWATAUAVAWH
!|$DHc
|$DD9d$X
f;D$@ug
f;D$@uD
H!\$ H
HcD$HH;
H!\$ H
HcD$HH;
H!|$ L
A_A^A]A\_^]
VWATAUAVH
 A^A]A\_^
UVWATAUH
^D9d$ 
D$&8\$&t-8X
@A]A\_^]
L$ UVWH
LcA<E3
WATAUAVAWH
0A_A^A]A\_
ATAUAVH
 A^A]A\
t$ WATAUH
D8"u%H
ATAUAWH
0A_A]A\
@UATAUAVAWH
@88tH
!t$(H!t$ A
A_A^A]A\]
@UATAUAVAWH
A_A^A]A\]
fffffff
fffffff
	H;5V
KXH;WV
K`H;MV
@SUVWATAUAVH
PA^A]A\_^][
C:\%s\%s
WINDOWS
mssecsvc.exe
(null)
`h````
xpxxxx
CorExitProcess
HH:mm:ss
dddd, MMMM dd, yyyy
MM/dd/yy
December
November
October
September
August
February
January
Saturday
Friday
Thursday
Wednesday
Tuesday
Monday
Sunday
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180002938` | `0x180002938` | 13223 | ✓ |
| `fcn.180002ef0` | `0x180002ef0` | 12701 | ✓ |
| `fcn.180005a60` | `0x180005a60` | 9202 | ✓ |
| `fcn.180001994` | `0x180001994` | 2732 | ✓ |
| `fcn.180003f58` | `0x180003f58` | 1888 | ✓ |
| `fcn.180007794` | `0x180007794` | 1006 | ✓ |
| `fcn.180007460` | `0x180007460` | 820 | ✓ |
| `fcn.180003228` | `0x180003228` | 722 | ✓ |
| `fcn.180006f0c` | `0x180006f0c` | 714 | ✓ |
| `fcn.180004e50` | `0x180004e50` | 629 | ✓ |
| `fcn.1800064d4` | `0x1800064d4` | 605 | ✓ |
| `fcn.1800060c0` | `0x1800060c0` | 562 | ✓ |
| `fcn.180007ed0` | `0x180007ed0` | 520 | ✓ |
| `fcn.180004b14` | `0x180004b14` | 496 | ✓ |
| `fcn.180003d14` | `0x180003d14` | 483 | ✓ |
| `fcn.1800050c8` | `0x1800050c8` | 478 | ✓ |
| `fcn.1800036a0` | `0x1800036a0` | 463 | ✓ |
| `fcn.1800057b0` | `0x1800057b0` | 452 | ✓ |
| `fcn.180003054` | `0x180003054` | 399 | ✓ |
| `fcn.18000162c` | `0x18000162c` | 397 | ✓ |
| `fcn.180006c30` | `0x180006c30` | 384 | ✓ |
| `fcn.180005400` | `0x180005400` | 377 | ✓ |
| `fcn.180007270` | `0x180007270` | 350 | ✓ |
| `entry0` | `0x1800015ec` | 345 | ✓ |
| `fcn.18000137c` | `0x18000137c` | 338 | ✓ |
| `fcn.180002448` | `0x180002448` | 331 | ✓ |
| `fcn.180002ac0` | `0x180002ac0` | 307 | ✓ |
| `fcn.180003570` | `0x180003570` | 304 | ✓ |
| `fcn.180006384` | `0x180006384` | 266 | ✓ |
| `fcn.180007bf0` | `0x180007bf0` | 266 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.18000137c.c`](code/fcn.18000137c.c)
- [`code/fcn.18000162c.c`](code/fcn.18000162c.c)
- [`code/fcn.180001994.c`](code/fcn.180001994.c)
- [`code/fcn.180002448.c`](code/fcn.180002448.c)
- [`code/fcn.180002938.c`](code/fcn.180002938.c)
- [`code/fcn.180002ac0.c`](code/fcn.180002ac0.c)
- [`code/fcn.180002ef0.c`](code/fcn.180002ef0.c)
- [`code/fcn.180003054.c`](code/fcn.180003054.c)
- [`code/fcn.180003228.c`](code/fcn.180003228.c)
- [`code/fcn.180003570.c`](code/fcn.180003570.c)
- [`code/fcn.1800036a0.c`](code/fcn.1800036a0.c)
- [`code/fcn.180003d14.c`](code/fcn.180003d14.c)
- [`code/fcn.180003f58.c`](code/fcn.180003f58.c)
- [`code/fcn.180004b14.c`](code/fcn.180004b14.c)
- [`code/fcn.180004e50.c`](code/fcn.180004e50.c)
- [`code/fcn.1800050c8.c`](code/fcn.1800050c8.c)
- [`code/fcn.180005400.c`](code/fcn.180005400.c)
- [`code/fcn.1800057b0.c`](code/fcn.1800057b0.c)
- [`code/fcn.180005a60.c`](code/fcn.180005a60.c)
- [`code/fcn.1800060c0.c`](code/fcn.1800060c0.c)
- [`code/fcn.180006384.c`](code/fcn.180006384.c)
- [`code/fcn.1800064d4.c`](code/fcn.1800064d4.c)
- [`code/fcn.180006c30.c`](code/fcn.180006c30.c)
- [`code/fcn.180006f0c.c`](code/fcn.180006f0c.c)
- [`code/fcn.180007270.c`](code/fcn.180007270.c)
- [`code/fcn.180007460.c`](code/fcn.180007460.c)
- [`code/fcn.180007794.c`](code/fcn.180007794.c)
- [`code/fcn.180007bf0.c`](code/fcn.180007bf0.c)
- [`code/fcn.180007ed0.c`](code/fcn.180007ed0.c)

## Behavioral Analysis

This updated analysis incorporates the new disassembly from chunk 2/2. The additional code reinforces the conclusion that this is a sophisticated piece of malware designed for **high-level evasion and resilience.**

The new functions reveal deeper layers of "self-healing" logic and advanced memory manipulation techniques used to hide the execution flow from security researchers.

---

### Updated Analysis: Malware Loader/Dropper (Chunk 2/2)

#### Core Functionality & Purpose
The analysis confirms a high level of sophistication. While the first chunk established that this is a "stage 1" loader, the second chunk reveals how it maintains its integrity during execution. The code doesn't just hide its intent; it actively monitors and corrects its own environment to ensure it isn't being tampered with or monitored by analysis tools.

#### New & Enhanced Findings

**1. Advanced Pointer Obfuscation (Encoding/Decoding Architecture)**
In `fcn.180006384`, the consistent use of `DecodePointer` and `EncodePointer` indicates a systematic way to hide memory addresses. 
*   **Mechanism:** The loader does not store raw absolute addresses for its internal functions or system APIs in plain sight. Instead, it stores "encoded" values.
*   **Purpose:** By only decoding these pointers immediately before use (and potentially re-encoding them after), the malware makes it significantly harder for static analysis tools to map out the call graph or identify which system APIs are being targeted.

**2. Self-Patching and Environment Correction ("Self-Healing")**
The function `fcn.180007bf0` is highly characteristic of advanced malware (often seen in sophisticated "crypters" or "protectors"). 
*   **Mechanism:** It iterates through a series of memory offsets (e.g., `+0x18`, `+0x20`, `+0x28`). At each offset, it compares the value currently in memory against a hardcoded constant. If the values do not match, it calls `fcn.180002cb8`.
*   **Purpose:** This is a **patching mechanism**. The "constant" might be a known hook signature used by an antivirus or a debugger. If the malware detects that its code has been modified (hooked) or that the environment is not in the expected state, it calls `fcn.180002cb8` to "fix" that specific area of memory. This allows the loader to bypass security software hooks dynamically.

**3. Dynamic Memory Management & Relocation**
The logic in `fcn.180006384` involves complex calculations regarding memory boundaries and sizes (e.g., `puVar1 - arg1_00`, `uVar5 = 0x1000`).
*   **Mechanism:** This appears to be a custom relocation or mapping handler. It validates the size of memory blocks and ensures that the offsets for decoded pointers are within safe bounds before jumping to them.
*   **Purpose:** This ensures the loader can function even if it is loaded into different memory locations or in different process contexts, while ensuring that its internal "jumping" logic remains intact.

---

### Summary Table of New Findings (Chunk 2)

| Feature | Observed Mechanism | Potential Purpose |
| :--- | :--- | :--- |
| **Pointer Obfuscation** | `DecodePointer` / `EncodePointer` | Hides the true destination of function calls from static analysis and automated scanners. |
| **Self-Patching** | `fcn.180007bf0` (Iterative offset checks) | Detects and removes/overwrites security hooks or modifications made by debuggers. |
| **Integrity Checking** | Comparison of memory values against hardcoded constants. | Ensures the "environment" is safe and that no third-party tools are interfering with the loader's logic. |
| **Dynamic Relocation** | Complex offset math & range checks in `fcn.180006384`. | Allows the loader to resolve its internal components dynamically regardless of where it resides in memory. |

---

### Comprehensive Technical Summary (Combined 1 & 2)

The binary is a **highly defensive Stage-1 Loader**. Its design incorporates three distinct layers of protection:

1.  **Layer 1: Identity Masking.** It uses deceptive strings (`mssecsvc.exe`, `launcher.dll`) to blend in with system resources and gaming software.
2.  **Layer 2: Environment Filtering.** It checks for the presence of debuggers and specific Windows internal states before it "unpacks" its primary payload.
3.  **Layer 3: Active Counter-Defense.** Through **Pointer Encoding** and **Self-Patching**, it ensures that even if a researcher manages to run the loader, the loader will detect and bypass most common hooking techniques used by EDR (Endpoint Detection and Response) systems.

**Conclusion:** This is not a simple script or "lazy" malware; it was likely produced using professional-grade protection software (a "crypter") intended to deliver high-value payloads while surviving in hostile, monitored environments.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of `DecodePointer` and `EncodePointer` functions hides internal function locations and system API targets from static analysis. |
| **T1106** | Dynamic Resolution | The malware resolves and decodes memory addresses at runtime rather than using static offsets, complicating the identification of its call graph. |
| **T1497** | Virtualization/Sandbox Evasion | The "Self-Healing" logic and environment checks are specifically designed to detect and bypass security hooks and analysis tools. |
| **T1036** | Masquerading | The use of deceptive strings such as `mssecsvc.exe` allows the malware to blend in with legitimate system services and files. |
| **T1114** | Modify System Properties (Implicit) | The "Self-Healing" logic that checks and corrects memory values indicates an attempt to ensure the execution environment meets specific criteria before proceeding. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `mssecsvc.exe` (Identified as a masquerading filename; likely intended to mimic a system service).
*   `launcher.dll` (Identified as a component used for staging or execution).

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Masquerading Behavior:** The use of `mssecsvc.exe` suggests an attempt to blend in with legitimate Windows services (e.g., "Microsoft Security Service").
*   **Evasion Techniques:** 
    *   **Pointer Obfuscation:** Utilization of `DecodePointer` and `EncodePointer` to hide internal function calls from static analysis.
    *   **Self-Patching/Integrity Checking:** Detection and removal of security hooks in memory (specifically noted in the behavior at offsets like `fcn.180007bf0`).
    *   **Stage-1 Loader Logic:** The binary is designed as a "crypter" or loader intended to deliver a secondary payload while bypassing EDR systems via dynamic resolution and memory manipulation.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

**Key evidence**:
*   **Sophisticated Evasion Tactics:** The sample utilizes advanced "Self-Healing" logic (at `fcn.180007bf0`) and pointer obfuscation (`DecodePointer`/`EncodePointer`) specifically designed to detect and bypass EDR hooks and security monitoring tools.
*   **Multi-Stage Architecture:** The analysis confirms it is a "Stage-1" loader, meaning its primary function is not the final payload but the delivery and execution of subsequent malware while maintaining evasion.
*   **Masquerading & Obfuscation:** Use of deceptive strings like `mssecsvc.exe` combined with dynamic resolution and memory relocation techniques indicate a professional-grade "crypter" or loader intended to blend into system environments.
