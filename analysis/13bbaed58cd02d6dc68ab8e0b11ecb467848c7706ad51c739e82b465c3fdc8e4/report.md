# Threat Analysis Report

**Generated:** 2026-09-02 23:38 UTC
**Sample:** `13bbaed58cd02d6dc68ab8e0b11ecb467848c7706ad51c739e82b465c3fdc8e4_13bbaed58cd02d6dc68ab8e0b11ecb467848c7706ad51c739e82b465c3fdc8e4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13bbaed58cd02d6dc68ab8e0b11ecb467848c7706ad51c739e82b465c3fdc8e4_13bbaed58cd02d6dc68ab8e0b11ecb467848c7706ad51c739e82b465c3fdc8e4.exe` |
| File type | PE32+ executable for MS Windows 5.02 (DLL), x86-64, 6 sections |
| Size | 2,406,400 bytes |
| MD5 | `ec2e1ed31515b722d88fa50838ff4d9b` |
| SHA1 | `ebefdb0e01fc703b9127daa5e2675713d53af239` |
| SHA256 | `13bbaed58cd02d6dc68ab8e0b11ecb467848c7706ad51c739e82b465c3fdc8e4` |
| Overall entropy | 7.54 |
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
| `.rsrc` | 5,243,392 | 7.563 | ⚠️ Yes |
| `.reloc` | 3,584 | 0.0 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `WriteFile`, `CreateFileA`, `SizeofResource`, `LockResource`, `LoadResource`, `FindResourceA`, `CreateProcessA`, `GetCurrentThreadId`, `FlsSetValue`, `GetCommandLineA`, `DecodePointer`, `UnhandledExceptionFilter`, `SetUnhandledExceptionFilter`, `IsDebuggerPresent`

### Exports

`PlayGame`

## Extracted Strings

Total strings found: **4704** (showing first 100)

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
mssecsvr.exe
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

Based on the additional disassembly provided, I have updated and expanded the analysis. The new code segments confirm that this binary uses advanced **control-flow obfuscation** and **indirect execution patterns**, typical of high-end packers or sophisticated malware (like state-sponsored trojans).

### Updated Analysis Summary
The provided code remains characteristic of a **sophisticated malware loader/packer**. While the first chunk established the "loader" behaviors (dropping files, anti-debugging, and string decryption), this second chunk reveals complex **internal dispatching mechanisms** used to hide the program's actual logic from static analysis tools.

---

### Core Functionality and Purpose
*   **Loader/Stub Behavior:** The code continues to exhibit heavy infrastructure for environment preparation (memory management, string decoding).
*   **Payload Deployment:** Confirmed via `fcn.1800064d4` (from the first chunk) which handles file writing of the "mssecsvr" payload.
*   **Dynamic API Resolution & Obfuscated Dispatching:** The new code highlights a transition from simple dynamic resolution to **indirect dispatch**. Instead of calling functions directly, the malware uses jump tables and offset checks to determine where to redirect execution at runtime.

### Suspicious and Malicious Behavs
*   **Anti-Debugging & Anti-Analysis:** 
    *   **Debugger Detection/Trap Instructions:** (Previously identified) `swi(3)` and `IsDebuggerPresent` remain key indicators of an evasive environment.
    *   **Instructional Obfuscation:** The use of `DecodePointer` and `EncodePointer` in `fcn.180006384` is a classic technique to hide relative offsets. By encoding jumps, the malware makes it difficult for disassemblers to follow the logic path (Control Flow Graph) during static analysis.
*   **Environment Awareness:** 
    *   The inclusion of `GetActiveWindow` and `GetProcessWindowStation` suggests it is waiting for a "human" interaction or specific UI context before executing its main payload.
*   **Masquerading:** 
    *   Still identified: The use of `mssecsvr.exe`.

---

### New Technical Findings (from Chunk 2)

#### 1. Advanced Control-Flow Obfuscation (`fcn.180006384`)
This function is a high-complexity routine involving **pointer arithmetic and encoding**.
*   **Encoding/Decoding Logic:** The use of `DecodePointer` and `EncodePointer` indicates that the malware is likely using a custom "relocation" system. It calculates distances between modules or internal functions to ensure that even if an analyst changes a memory address, the jump still works—but it also makes the code nearly impossible to trace linearly in tools like IDA Pro without manual de-obfuscation.
*   **Bounds Checking:** The logic checking `uVar5` against `0x1000` and comparing `uVar4 = (*_sym.imp.KERNEL32.dll_EncodePointer)(arg1)` suggests a very rigid, internally consistent way of handling memory addresses to prevent "crashing" while ensuring the code remains hidden from scanners.

#### 2. Table-Driven Dispatcher (`fcn.180007bf0`)
This function is highly characteristic of **malware packers** and **VM-based protectors**.
*   **The "Dispatcher" Pattern:** The sequence of checks (comparing `0x18`, `0x20`, `0x28`, etc.) against hardcoded constants followed by a call to `fcn.180002cb8` is a classic **Dispatcher**.
*   **How it works:** Instead of having one function that does many things, the malware has one "dispatcher" (`fcn.180007bf0`) that looks at an offset in a table (the instructions). If the value at that location isn't a "null" or "placeholder," it calls a handler (`fcn.180002cb8`).
*   **Impact on Analysis:** This hides the true intent of the code. An analyst looking at `fcn.180007bf0` only sees a series of checks; they cannot see what the "handler" actually does until it is triggered during runtime. This is often used to implement **Virtual Machine (VM) protected code**, where the malware executes its own custom bytecode rather than standard x86 instructions.

---

### Updated Summary Table of Techniques

| Category | Technique Identified | Purpose/Impact |
| :--- | :--- | :--- |
| **Obfuscation** | **Encoded Pointers** | Hides destination addresses and breaks static Control Flow Graphs (CFG). |
| **Obfuscation** | **Table-Based Dispatching** | Decouples the logic from the execution, making it hard to trace "how" a function reaches its goal. |
| **Evasion** | **Debugger Traps (`swi(3)`)** | Crashes the process if a debugger is attached or tries to divert execution. |
| **Evasion** | **Environment Checking** | Ensures the malware only runs on "real" user machines, not in sandboxes. |
| **Payload** | **Dropped Executable** | The `mssecsvr.exe` file is the final goal of this loader's operations. |

### Conclusion
The addition of Chunk 2 confirms that this is not a simple "script-kiddie" malware. The presence of **manual pointer encoding/decoding** and **multi-offset dispatching** indicates a professional level of engineering aimed at thwarting automated sandbox analysis and manual reverse engineering. It is highly likely this is the first stage of an infection chain where the loader's only job is to "unpack" and "hide" the primary malicious logic.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The malware uses the name `mssecsvr` to mimic a legitimate system service and avoid detection by users or basic security tools. |
| **T1497** | Virtualization/Sandbox Evasion | The use of `swi(3)`, `IsDebuggerPresent`, and environment checks (`GetActiveWindow`) are used to detect analysis environments or automated sandboxes. |
| **T1027** | Obfuscated Files or Information | The implementation of encoded pointers, a custom dispatch table, and packer-style obfuscation hides the execution logic from static analysis tools like IDA Pro. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the identified Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `mssecsvr.exe` (Identified as the primary malicious payload)
*   `launcher.dll` (Component of the loader/packer)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Payload Name:** `mssecsvr` (The specific naming convention used for the dropped executable).
*   **Anti-Debugging Technique:** Use of `swi(3)` (Software Interrupt) to trap and detect debugger presence.
*   **Obfuscation Techniques:** 
    *   **Encoded Pointers:** Use of custom "relocation" logic (`DecodePointer`/`EncodePointer`) to hide control flow.
    *   **Table-Based Dispatching:** A multi-offset dispatcher used to decouple execution logic from analysis tools.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High (regarding functionality), Low (regarding specific brand/campaign)
4. **Key evidence**:
    *   **Sophisticated Obfuscation:** The use of "Table-Based Dispatching" and "Encoded Pointers" indicates a high-level engineering effort designed to bypass static analysis and hide the core logic from tools like IDA Pro.
    *   **Anti-Analysis Techniques:** The presence of `swi(3)` traps, `IsDebuggerPresent` checks, and environment awareness (checking for active windows) are classic hallmarks of a professional loader used to protect a secondary payload.
    *   **Payload Delivery Mechanism:** The analysis identifies the file as a "loader/stub" whose primary purpose is to unpack and drop a masqueraded executable (`mssecsvr.exe`) while evading detection during the transition.
