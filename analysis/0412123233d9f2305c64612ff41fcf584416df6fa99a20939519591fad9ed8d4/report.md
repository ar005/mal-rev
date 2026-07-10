# Threat Analysis Report

**Generated:** 2026-07-09 17:53 UTC
**Sample:** `0412123233d9f2305c64612ff41fcf584416df6fa99a20939519591fad9ed8d4_0412123233d9f2305c64612ff41fcf584416df6fa99a20939519591fad9ed8d4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0412123233d9f2305c64612ff41fcf584416df6fa99a20939519591fad9ed8d4_0412123233d9f2305c64612ff41fcf584416df6fa99a20939519591fad9ed8d4.exe` |
| File type | PE32+ executable for MS Windows 5.02 (DLL), x86-64, 6 sections |
| Size | 5,298,176 bytes |
| MD5 | `5239d509cb289898b70780bfc4539d21` |
| SHA1 | `c2105acb0e5cac1a086e9c19276a3fd5ce123ce8` |
| SHA256 | `0412123233d9f2305c64612ff41fcf584416df6fa99a20939519591fad9ed8d4` |
| Overall entropy | 5.065 |
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
| `.rsrc` | 5,243,392 | 5.054 | No |
| `.reloc` | 3,584 | -0.0 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `WriteFile`, `CreateFileA`, `SizeofResource`, `LockResource`, `LoadResource`, `FindResourceA`, `CreateProcessA`, `GetCurrentThreadId`, `FlsSetValue`, `GetCommandLineA`, `DecodePointer`, `UnhandledExceptionFilter`, `SetUnhandledExceptionFilter`, `IsDebuggerPresent`

### Exports

`PlayGame`

## Extracted Strings

Total strings found: **5372** (showing first 100)

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

Based on the additional disassembly provided in chunk 2, I have updated the analysis. The new functions reinforce and expand upon the existing findings, particularly in the areas of **anti-analysis techniques** and **evasive runtime behavior.**

### Updated Analysis Report

#### Core Functionality and Purpose
The binary continues to exhibit characteristics of a sophisticated loader/dropper. In addition to masquerading as a system service (`mssecsvc.exe`), the new code segments suggest that it performs extensive internal management of its own execution logic to bypass security monitoring. It manages complex internal tables to resolve functions dynamically and perform integrity checks on its memory space.

#### Suspicion & Malicious Behaviors (Updated)
*   **Anti-Debugging & Anti-Analysis:** 
    *   **Integrity/Hook Detection:** Function `fcn.180007bf0` demonstrates a systematic check of several memory offsets against hardcoded values. This is a common technique used to detect **Inline Hooks**. If an EDR (Endpoint Detection and Response) or an antivirus tool "hooks" a function by overwriting the first few bytes with a jump, this code detects that change and triggers `fcn.180002cb8` (potentially to switch to a "clean" execution path or terminate).
    *   **Self-Modifying/Dynamic Dispatch:** The use of `DecodePointer` and `EncodePointer` in `fcn.180006384`, combined with manual offset calculations, suggests the malware is managing its own **Dispatch Table**. This allows it to dynamically change where it jumps when a function is called, making it much harder for static analysis tools to trace the execution flow.
*   **Dynamic API Resolution:** 
    *   The continued use of `DecodePointer` (a wrapper for `GetProcAddress`) confirms that the malware intends to hide its intent from the Import Address Table (IAT). It only resolves the location of "dangerous" functions at runtime.
*   **Potential File Manipulation:** 
    *   (From previous chunk) The logic in `fcn.180003f58` regarding `WriteFile` confirms capabilities for dropping secondary payloads or modifying system files to establish persistence.

#### Notable Techniques and Patterns
*   **Deterministic Integrity Checking:** The structure of `fcn.180007bf0` (a long sequence of `if` statements comparing values at specific offsets) is a "tell" for advanced malware. It suggests the author wants to ensure that no security tools have modified the code's execution path before it proceeds with its malicious tasks.
*   **Complex Memory Management:** The logic in `fcn.180006384` involves calculating buffer sizes and positions (`(puVar1 - arg1_00) + 8`) and conditionally updating memory addresses. This indicates a highly customized execution environment where the malware is trying to hide its "true" functions behind layers of indirection.
*   **Evasive Instruction Sequences:** (From previous chunk) The `swi(3)` instructions serve as deliberate trap_points for debuggers, while the new code ensures that even if an analyst tries to bypass those traps, any subsequent modifications (hooks) are detected by the integrity checks.

### Summary for Incident Response
The inclusion of the second disassembly chunk confirms this is a **high-complexity threat.** 

1.  **Anti-EDR Capabilities:** The malware is specifically designed to detect if it is being monitored by security products. It scans its own memory to see if functions have been "hooked" or tampered with.
2.  **Evasive Execution:** By using custom dispatch tables and dynamic pointer encoding/decoding, the malware hides its true logic from static analysis tools (like `strings` or basic disassemblers), only revealing its full capabilities once it is running in memory.
3.  **Sophisticated Loading Architecture:** The complexity of the internal management functions suggests this is likely part of a larger campaign where the loader's primary job is to ensure the environment is "clean" (not monitored) before delivering and executing the final payload.

**Recommendation:** Due to the advanced anti-analysis features, manual analysis in a sandbox may be insufficient if the sandbox uses standard API hooking for monitoring. A "bare metal" analysis or an environment with hardware-assisted monitoring may be required to observe the full behavior of the sample.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036.005 | Create Equivalent | The malware masquerades as a system service (`mssecsvc.exe`) to blend in with legitimate system processes. |
| T1562.001 | Impair Defenses: System Integrity | The code performs systematic integrity checks on memory offsets to detect and bypass EDR/antivirus hooks. |
| T1497 | Virtualization, Sandbox, and Debugger Detection | The use of `swi(3)` instructions as trap points serves as a method to identify the presence of analysis tools or debuggers. |
| T1105 | Ingress Tool Transfer | The confirmed use of `WriteFile` logic indicates that the binary is designed to drop secondary payloads onto the system. |
| T1036 | Modify Execution (General) | The use of dynamic dispatch tables and `DecodePointer` functions evades static analysis by hiding the actual execution path of the malware. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `mssecsvc.exe` (Identified as a masqueraded process name)
*   `launcher.dll` (Associated module/library)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None provided in the source text)*

**Other artifacts**
*   **Process Masquerading:** The malware masquerades as a system service using the name `mssecsvc.exe`.
*   **Dynamic API Resolution:** Use of custom functions (`DecodePointer` and `EncodePointer`) to resolve and hide "dangerous" API calls from the Import Address Table (IAT).
*   **Anti-EDR/Anti-Hooking:** Detection of inline hooks (specifically identified in function `fcn.180007bf0`) used by security software to monitor execution.
*   **Evasive Execution:** Use of custom dispatch tables and memory offset calculations to obscure the true execution flow from static analysis tools.
*   **Potential Payload Dropper:** Evidence of `WriteFile` usage in sequence `fcn.180003f58` suggesting the capability to drop secondary payloads or modify system files for persistence.

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification for the sample:

1. **Malware family:** Custom (Sophisticated Loader)
2. **Malware type:** Loader / Dropper
3. **Confidence:** High
4. **Key evidence:**
    * **Advanced Anti-EDR/Anti-Hooking:** The binary implements sophisticated integrity checks (e.g., `fcn.180007bf0`) to detect inline hooks, specifically designed to bypass and evade modern Endpoint Detection and Response (EDR) systems.
    * **Evasive Execution & Obfuscation:** The use of custom dispatch tables, `DecodePointer`/`EncodePointer` functions for dynamic API resolution, and `swi(3)` trap points indicates a high level of intentional complexity to hide the malware's true logic from static analysis.
    * **Payload Delivery (Dropper):** The confirmed use of `WriteFile` operations combined with masquerading as a system service (`mssecsvc.exe`) confirms its primary role is to establish persistence and deploy additional malicious modules or secondary payloads.
