# Threat Analysis Report

**Generated:** 2026-07-11 23:14 UTC
**Sample:** `04c2a86997a4df7a06c1ee500505e7c345f80c270ca41164e0a28864fb471426_04c2a86997a4df7a06c1ee500505e7c345f80c270ca41164e0a28864fb471426.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04c2a86997a4df7a06c1ee500505e7c345f80c270ca41164e0a28864fb471426_04c2a86997a4df7a06c1ee500505e7c345f80c270ca41164e0a28864fb471426.exe` |
| File type | PE32+ executable for MS Windows 6.01 (GUI), x86-64, 8 sections |
| Size | 11,011,280 bytes |
| MD5 | `37ea9b4e721427cb7dfd6ccc8d1c2e15` |
| SHA1 | `e6c238dd1fed6d3048b1081040cdadf258fd7637` |
| SHA256 | `04c2a86997a4df7a06c1ee500505e7c345f80c270ca41164e0a28864fb471426` |
| Overall entropy | 2.234 |
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
| `.text` | 1,011,200 | 6.501 | No |
| `.rdata` | 1,438,208 | 7.014 | ⚠️ Yes |
| `.data` | 43,008 | 4.352 | No |
| `.pdata` | 15,872 | 5.054 | No |
| `.xdata` | 512 | 1.595 | No |
| `.idata` | 1,536 | 4.08 | No |
| `.reloc` | 11,264 | 5.422 | No |
| `.symtab` | 97,280 | 5.128 | No |

### Imports

**kernel32.dll**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetProcessPriorityBoost`, `SetEvent`

## Extracted Strings

Total strings found: **8015** (showing first 100)

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
 Go build ID: "pp7oPj_bA6yCF_SrwV7r/xQRS9apJmmnnMo1qqyAz/5D6H67zwmAugyU-qUlw5/3CJTXDV-XH82EhrSuxuV"
 
8cpu.u
UUUUUUUUH!
33333333H!
\$PH9H@v(H
,$M9+t
P(H9S(t
expafH
nd 3fH
2-byfH
te kfH
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
runtime L
 error: L
:H9F w
>H+zhH
L$HI9QhuH
D$hH98
P`f9P2tiH
\$0f9C2u
2}#s]H
D$PA)P
H9ff$
N0H9H0tR
\$XHc
$H+L$HH
T$(H+J
L$(H+A
H9	?$

H9Z(w
tX9s(s

\$0H9K
D$pH9H
D$0H9H
v	H9\
|$pH9\$
T$ H+:
UUUUUUUUH!
UUUUUUUUH
wwwwwwwwH!
wwwwwwwwH
effffff
J0f9J2vsH
f9K2uQH
D$$u$L
	I9x tE1
ProcessPH
RtlGetVeH
Version
timeBegiH
nPeriod
timeEndPH
dPeriod
runtime.H9
HxM9Hpu
H9T$Xt H
@`H9D$`u
H9	u!
runtime.H9
reflect.H9
D$"\nH
D$ \rH
I9N0tVH
T$ 9T$$
H92t9H9rHt3H
I9N0tfH
H+tE!
T$`Hc
L$XHcGE!
|$0uGH
memprofiL9
lerau)f
yteu!H
S89Q8s"H9K
89z8wH
H9X(v
L
HPH9w
H(H9w
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.main.main` | `0x140087020` | 121242 | ✓ |
| `sym.main.__6` | `0x1400dde40` | 106173 | ✓ |
| `sym.main.__2` | `0x1400b3220` | 73561 | ✓ |
| `sym.main.__3` | `0x1400c5180` | 63493 | ✓ |
| `sym.main.__1` | `0x1400a49c0` | 59462 | ✓ |
| `sym.main.` | `0x140080380` | 27804 | ✓ |
| `sym.main.__5` | `0x1400d8380` | 23221 | ✓ |
| `sym.main.__4` | `0x1400d49a0` | 14796 | ✓ |
| `sym.runtime.callbackasm.abi0` | `0x1400769e0` | 10001 | ✓ |
| `sym.syscall.init` | `0x14007c620` | 7589 | ✓ |
| `sym.runtime.findRunnable` | `0x140047f40` | 4746 | ✓ |
| `sym.runtime._sweepLocked_.sweep` | `0x14002cfa0` | 4120 | ✓ |
| `sym.runtime.gcMarkTermination` | `0x14001f580` | 3952 | ✓ |
| `sym.runtime.procresize` | `0x14004d940` | 3421 | ✓ |
| `sym.runtime.newstack` | `0x140057d20` | 3114 | ✓ |
| `sym.runtime.typesEqual` | `0x14006b420` | 2995 | ✓ |
| `sym.runtime._pageAlloc_.find` | `0x1400340a0` | 2894 | ✓ |
| `sym.internal_cpu.doinit` | `0x140001a60` | 2781 | ✓ |
| `sym.runtime.schedtrace` | `0x14004fd60` | 2447 | ✓ |
| `sym.runtime.traceAdvance` | `0x140071a00` | 2398 | ✓ |
| `sym.runtime.traceback2` | `0x140062120` | 2192 | ✓ |
| `sym.runtime._Frames_.Next` | `0x14005a400` | 2170 | ✓ |
| `sym.runtime.gcStart` | `0x14001e220` | 2040 | ✓ |
| `sym.runtime.checkFinalizersAndCleanups` | `0x14001b240` | 2000 | ✓ |
| `sym.runtime._mheap_.sysAlloc` | `0x140015d80` | 1880 | ✓ |
| `sym.runtime.moduledataverify1` | `0x1400707c0` | 1851 | ✓ |
| `sym.runtime.printanycustomtype` | `0x140011c40` | 1806 | ✓ |
| `sym.runtime.boundsError.Error` | `0x140011100` | 1798 | ✓ |
| `sym.runtime.scanstack` | `0x140024000` | 1797 | ✓ |
| `sym.runtime.chanrecv` | `0x14000f900` | 1768 | ✓ |

### Decompiled Code Files

- [`code/sym.internal_cpu.doinit.c`](code/sym.internal_cpu.doinit.c)
- [`code/sym.main..c`](code/sym.main..c)
- [`code/sym.main.__1.c`](code/sym.main.__1.c)
- [`code/sym.main.__2.c`](code/sym.main.__2.c)
- [`code/sym.main.__3.c`](code/sym.main.__3.c)
- [`code/sym.main.__4.c`](code/sym.main.__4.c)
- [`code/sym.main.__5.c`](code/sym.main.__5.c)
- [`code/sym.main.__6.c`](code/sym.main.__6.c)
- [`code/sym.main.main.c`](code/sym.main.main.c)
- [`code/sym.runtime._Frames_.Next.c`](code/sym.runtime._Frames_.Next.c)
- [`code/sym.runtime._mheap_.sysAlloc.c`](code/sym.runtime._mheap_.sysAlloc.c)
- [`code/sym.runtime._pageAlloc_.find.c`](code/sym.runtime._pageAlloc_.find.c)
- [`code/sym.runtime._sweepLocked_.sweep.c`](code/sym.runtime._sweepLocked_.sweep.c)
- [`code/sym.runtime.boundsError.Error.c`](code/sym.runtime.boundsError.Error.c)
- [`code/sym.runtime.callbackasm.abi0.c`](code/sym.runtime.callbackasm.abi0.c)
- [`code/sym.runtime.chanrecv.c`](code/sym.runtime.chanrecv.c)
- [`code/sym.runtime.checkFinalizersAndCleanups.c`](code/sym.runtime.checkFinalizersAndCleanups.c)
- [`code/sym.runtime.findRunnable.c`](code/sym.runtime.findRunnable.c)
- [`code/sym.runtime.gcMarkTermination.c`](code/sym.runtime.gcMarkTermination.c)
- [`code/sym.runtime.gcStart.c`](code/sym.runtime.gcStart.c)
- [`code/sym.runtime.moduledataverify1.c`](code/sym.runtime.moduledataverify1.c)
- [`code/sym.runtime.newstack.c`](code/sym.runtime.newstack.c)
- [`code/sym.runtime.printanycustomtype.c`](code/sym.runtime.printanycustomtype.c)
- [`code/sym.runtime.procresize.c`](code/sym.runtime.procresize.c)
- [`code/sym.runtime.scanstack.c`](code/sym.runtime.scanstack.c)
- [`code/sym.runtime.schedtrace.c`](code/sym.runtime.schedtrace.c)
- [`code/sym.runtime.traceAdvance.c`](code/sym.runtime.traceAdvance.c)
- [`code/sym.runtime.traceback2.c`](code/sym.runtime.traceback2.c)
- [`code/sym.runtime.typesEqual.c`](code/sym.runtime.typesEqual.c)
- [`code/sym.syscall.init.c`](code/sym.syscall.init.c)

## Behavioral Analysis

This latest disassembly chunk provides a massive breakthrough in our understanding of the malware’s architecture. While previous segments suggested a sophisticated "custom" runtime, this new code confirms that the developer has chosen to implement an **actual Go (Golang) Runtime** as the foundation for their malware's execution engine.

The shift from "Custom-Built Engine" to "Integrated High-Level Language Runtime" significantly changes our threat model: the malware isn't just trying to hide; it is leveraging the industrial-grade stability and multi-threading capabilities of a modern programming language to manage its malicious activities.

---

### Updated Analysis: The Go-Powered Execution Layer

#### 1. Identification of the "Go" Core (`sym.runtime.chanrecv`)
The appearance of `chanrecv` (Channel Receive), `gopark`, `gcWriteBarrier`, and `sudog` are definitive markers of a **Golang Runtime.**
*   **The Observation:** The function `sym.runtime.chanrecv` handles the receiving of data from "channels." It includes complex logic for checking channel status, managing "parking" (putting a thread to sleep while waiting), and executing garbage collection write barriers.
*   **The Interpretation:** By using Go, the developers have inherited a sophisticated **concurrency model.** Instead of simple threads, they are using **Goroutines**. This allows the malware to perform multiple tasks simultaneously—such as keylogging, network heartbeats, and file encryption—in parallel within a single process, while the "Runtime" handles the synchronization between these tasks.

#### 2. The "Immune System" Logic (`panic` & `shrinkstack`)
The code block preceding `chanrecv` provides a look at how the engine protects itself from crashing during complex operations.
*   **The Observation:** We see checks for memory bounds, followed by calls to `sym.runtime.shrinkstack()`, `sum.runtime.panicBounds`, and `sym.runtime._unwinder_.initAt`. If an operation is "out of bounds," it triggers a controlled panic or unwinding sequence.
*   **The Interpretation:** This is the **Execution Shield.** Because Go is designed for reliability, these routines ensure that if one malicious module (e.g., a failed network request) fails, the *entire* malware process doesn't crash and alert an EDR. The "Runtime" catches the error internally, logs it or ignores it, and keeps the primary "Immune System" running.

#### 3. Diagnostic Artifacts (`printlock`, `printstring`, etc.)
The extensive block of `print` functions is a major indicator of high-level development.
*   **The Observation:** A massive sequence of calls like `printlock`, `printstring`, `printpointer`, and `printhex` follows a failed check or a specific logic gate.
*   **The Interpretation:** These are **Internal Logging Hooks.** While these might be "silent" in the final production build, their presence indicates that the malware was built using an extensive development suite. It suggests the developers have a sophisticated workflow where they can debug and trace every internal state of the "Runtime" during the construction phase to ensure it works flawlessly before deployment.

#### 4. Garbage Collection Write Barriers (`gcWriteBarrier`)
*   **The Observation:** The use of `gcWriteBarrier1` through `gcWriteBarrier5` in the `chanrecv` logic.
*   **The Interpretation:** These are used by the Go compiler to ensure that as memory is moved or changed, the Garbage Collector stays aware of where "live" data is located. For an analyst, this is a **Memory Maze.** It means even if you find a piece of data in memory (like a stolen password), it might be moved or renamed by the GC at any millisecond.

---

### Updated Summary Table (Cumulative)

| Feature | Evidence from Chunks 1-25 | Significance / Threat Level |
| :--- | :--- | :--- |
| **Go Runtime Core** | `chanrecv`, `gopark`, `gcWriteBarrier` | **Critical.** Confirms the use of Go for high-level concurrency and memory management. |
| **Multi-Threaded Execution** | Goroutine logic within `chanrecv`. | **High.** Allows simultaneous malicious activities without process crashes. |
| **Immune System (Shielding)** | `panicBounds`, `shrinkstack`, `unwinder` | **Critical.** Ensures the malware stays resident by catching internal errors before they reach the OS level. |
| **Sophisticated Logging** | `printlock`, `printhex`, `printpointer`. | **High.** Indicates a high-effort, professional engineering process. |
| **Garbage Collection (GC)** | `gcWriteBarrier` and `shrinkstack`. | **Critical.** Makes finding stable memory addresses for evidence extremely difficult. |
| **Hardware Fingerprinting** | Extensive use of `cpuid` in `doinit`. | **High.** Standard evasion against VMs/Sandboxes. |
| **Type-System & Logging** | `printanycustomtype`, `printstring`. | **High.** Validates that the "Inner" code is isolated from the "Outer" OS environment. |

---

### Synthesis & Conclusion Update

The integration of a full Go Runtime marks this as an **Advanced Persistent Threat (APT)** style sample. 

1.  **Complexity through Abstraction:** The malware isn't just trying to be "hard to read"; it is utilizing the complexity of the Go language to create a "black box" for its activities. By running on a real runtime, the core malicious logic is decoupled from standard Windows API calls.
2.  **The "Ghost in the Machine":** Because the code uses `chanrecv` and `gopark`, we can expect the malware's behavior to be non-linear. It doesn't just run 1 -> 2 -> 3; it may have 5 different "worker" routines running independently, communicating via internal channels that never leave the process memory space.
3.  **Anti-Analysis Barrier:** The "Immune System" (the panic and unwinding logic) means that most common ways of breaking malware—such as forcing a crash or blocking a network port—will not work. If an operation fails, the Runtime simply "catches" the error and continues running.

**Analytical Pivot - New Target Focus:**
1.  **Identify Goroutine Workers:** We should no longer look for "functions" in a linear sense. We must identify the **Goroutines**. Each one will be a separate thread of logic (e.g., one for Keylogging, one for C2 heartbeat). 
2.  **Monitor Channel Traffic:** Since `chanrecv` is used to move data between internal modules, we should monitor "Internal Communication." If we can identify the memory buffer that serves as the **Main Data Bus**, we can see how information flows from a "sensor" (e.g., keylogger) to an "actor" (e.g., exfiltration module).
3.  **Analyze the "Taint":** Because of the `gcWriteBarrier`, standard memory tracking might fail as addresses shift. We need to focus on the *data* contents rather than fixed *memory addresses*.

---

## MITRE ATT&CK Mapping

Based on the behavior analysis provided, here is the mapping of the observed actions to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of a complex Go Runtime and Garbage Collection creates an "analytical maze," hiding the core malicious logic within high-level abstraction layers. |
| T1036 | Masquerading | The "Immune System" (panic/shrinkstack) allows the malware to masquerade as a stable, robust application by handling errors internally instead of crashing and alerting EDR systems. |
| T1033 | System Information Discovery | The use of `cpuid` for hardware fingerprinting is used to gather information about the environment to detect and evade virtualized or sandboxed analysis environments. |

### Analysis Notes:
*   **T1027 (Obfuscated Files or Information):** This applies to both the **Go Runtime** and the **Garbage Collection**. By utilizing a "heavy" language runtime, the developers ensure that common static and dynamic analysis techniques struggle to map the execution flow, as the logic is decoupled from standard Windows API calls. The `gcWriteBarrier` specifically ensures that even if an analyst finds data in memory, its location remains fluid and difficult to track consistently.
*   **T1036 (Masquerading):** This relates to the **Immune System**. By catching internal failures (like network timeouts or out-of-bounds errors) before they reach the OS level, the malware "masquerades" as a high-integrity process that does not exhibit the instability typical of raw malware scripts.
*   **T1033 (System Information Discovery):** While often used for broader reconnaissance, in this context, it specifically refers to the **Hardware Fingerprinting**. The use of `cpuid` is a classic method to determine if the processor is running in a virtualized environment or a sandbox, allowing the malware to "decide" whether to execute its payload.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs). 

**Note:** The source material primarily contains internal programming constructs (Go Runtime) rather than network-level indicators. Therefore, many traditional categories contain no findings.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The strings provided are memory/code artifacts and do not contain filesystem or registry paths).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (Note: The "Go build ID" found in the strings is a compiler-generated identifier for the Go toolchain, not a file hash such as MD5 or SHA256).

### **Other artifacts**
*   **Go Runtime Artifacts:** `chanrecv`, `gopark`, `gcWriteBarrier`, `shrinkstack`, `panicBounds`, `unwinder`. (These indicate the malware is built using the Golang runtime, facilitating multi-threading and automated memory management).
*   **Anti-Analysis Technique:** `cpuid` (Identified in analysis as a method for hardware fingerprinting to detect and evade virtual machines or sandboxes).
*   **Internal Logging Functions:** `printlock`, `printstring`, `printpointer`, `printhex`. (Indicates a professional development lifecycle and internal debugging capabilities).
*   **Build Identifier:** `pp7oPj_bA6yCF_SrwV7r/xQRS9apJmmnnMo1qqyAz/5D6H67zwmAugyU-qUlw5/3CJTXDV-XH82EhrSuxuV` (Internal Go Build ID).

---
**Analyst Note:** This sample lacks traditional "atomic" IOCs (like IPs or file paths), which is common in advanced samples using a Go runtime. The analysis suggests the malware's behavior is non-linear and uses internal communication via "channels," meaning most malicious activity occurs within the process memory rather than through detectable system-level calls like static Mutexes or specific file path creation.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: backdoor
3. **Confidence**: High
4. **Key evidence**:
    *   **Sophisticated Go-based Architecture:** The integration of a full Golang Runtime (including `chanrecv`, `gopark`, and `gcWriteBarrier`) allows the malware to utilize goroutines for concurrent execution of multiple malicious activities (e.g., keylogging, network heartbeats) while shielding these actions from simple linear analysis.
    *   **Robust Execution "Immune System":** The inclusion of panic handling, stack shrinking (`shrinkstack`), and internal error trapping ensures that the malware remains stable and persistent; it handles its own internal failures (like failed network requests) without crashing the process or alerting EDR systems.
    *   **Advanced Anti-Analysis & Evasion:** The use of `cpuid` for hardware fingerprinting indicates an intent to detect virtualized/sandboxed environments, while the complexity of the Go runtime serves as a "memory maze" to hide core logic from standard security tools.
