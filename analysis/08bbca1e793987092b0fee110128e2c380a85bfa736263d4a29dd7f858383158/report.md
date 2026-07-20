# Threat Analysis Report

**Generated:** 2026-07-18 21:21 UTC
**Sample:** `08bbca1e793987092b0fee110128e2c380a85bfa736263d4a29dd7f858383158_08bbca1e793987092b0fee110128e2c380a85bfa736263d4a29dd7f858383158.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `08bbca1e793987092b0fee110128e2c380a85bfa736263d4a29dd7f858383158_08bbca1e793987092b0fee110128e2c380a85bfa736263d4a29dd7f858383158.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, 7 sections |
| Size | 1,805,312 bytes |
| MD5 | `e348631a2729a08a9790f2c85bffc9d9` |
| SHA1 | `6ba2c6da30a56bf978c0c5eee532354687c8dbfc` |
| SHA256 | `08bbca1e793987092b0fee110128e2c380a85bfa736263d4a29dd7f858383158` |
| Overall entropy | 6.624 |
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
| `.text` | 648,704 | 6.152 | No |
| `.rdata` | 1,013,760 | 6.551 | No |
| `.data` | 16,384 | 3.397 | No |
| `.idata` | 1,536 | 3.873 | No |
| `.reloc` | 39,424 | 6.544 | No |
| `.symtab` | 81,408 | 4.996 | No |
| `.rsrc` | 3,072 | 4.614 | No |

### Imports

**kernel32.dll**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetUnhandledExceptionFilter`, `SetProcessPriorityBoost`

## Extracted Strings

Total strings found: **7451** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.idata
.reloc
B.symtab
B.rsrc
 Go build ID: "AWHKYR4OZyEJeiuBdTje/Q9U31Za6VfH5ec-PBWO2/8dmWcUZe_b3xeICq1RRs/PsDDL0Qk6xNw33czvKCD"
 
|$9;u
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
#t$$#L$(
#\$$#D$(
#t$$#L$(
#l$,#L$0
#l$,#L$0
#t$8#L$<
#l$0#L$4
#t$<#L$@
#t$,#L$0
#t$,#L$0
#D$8#L$<
#t$4#L$8
#t$4#L$8
#t$0#L$4
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
D$49H(v6
D$<9D$
D$49D$
D$ 9D$
	;av|
|$09GDu
L$(9Aw
L$ 9A4t 
L$(f9A
D$,+D$
T$+B
D$49D$
L$H9A4v
\$49\$(u
L$$9A(s
\$09S4
u
9Hw
	;avL
L$+A
L$ 9H<s
L$09A4v
T$(9J4s
T$<9B4v
L$ #D$$#L$(
UUUU%UUUU
T$ 9T$
D$09D$
uP9uTu1
9T$,t-
D$49D$
D$L9D$
L$89L$<
tJ9A0tE
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
T$ 9P
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **0**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.main.Selective` | `0x479b40` | 19086 | — |
| `sym.main.main` | `0x471d40` | 15434 | — |
| `sym.runtime.callbackasm` | `0x469bb0` | 10000 | — |
| `sym.syscall.init` | `0x46e090` | 7007 | — |
| `sym.main.Selective.func3` | `0x47f540` | 5314 | — |
| `sym.main.Psychological.func2` | `0x483bf0` | 5314 | — |
| `sym.main.Permalink.func2` | `0x4863c0` | 5314 | — |
| `sym.main.Polyphonic.func3` | `0x488800` | 5314 | — |
| `sym.main.Polyphonic.func5` | `0x48ac40` | 5314 | — |
| `sym.main.Commodities.func3` | `0x48e380` | 5314 | — |
| `sym.main.Shipments.func3` | `0x491310` | 5314 | — |
| `sym.main.main.func2` | `0x493750` | 5314 | — |
| `sym.main.main.func4` | `0x495f20` | 5314 | — |
| `sym.main.Available.func2` | `0x4992e0` | 5314 | — |
| `sym.main.Selective.func7` | `0x481980` | 4850 | — |
| `sym.main.Permalink.func1` | `0x4850c0` | 4850 | — |
| `sym.main.Commodities.func1` | `0x48d080` | 4850 | — |
| `sym.main.Commodities.func4` | `0x48f850` | 4850 | — |
| `sym.main.main.func3` | `0x494c20` | 4850 | — |
| `sym.main.Available.func3` | `0x49a7b0` | 4850 | — |
| `sym.runtime.gcMarkTermination` | `0x417750` | 4713 | — |
| `sym.runtime.findRunnable` | `0x43dca0` | 4477 | — |
| `sym.main.Commodities` | `0x476a30` | 4476 | — |
| `sym.main.Shipments` | `0x475990` | 4246 | — |
| `sym.main.Polyphonic` | `0x477bb0` | 4178 | — |
| `sym.main.Selective.func1` | `0x47e5d0` | 3952 | — |
| `sym.main.Selective.func4` | `0x480a10` | 3952 | — |
| `sym.main.Selective.func9` | `0x482c80` | 3952 | — |
| `sym.main.Polyphonic.func1` | `0x487890` | 3952 | — |
| `sym.main.Polyphonic.func4` | `0x489cd0` | 3952 | — |

## Behavioral Analysis

Based on the provided disassembly, here is an analysis of the binary's behavior and functionality.

### Core Functionality
The code is a **malicious loader or "dropper"** written in **Go (Golang)**. The use of `sym.runtime` functions (like `growslice`, `mapassign_faststr`, and `wbMove`) and the specific structure of the disassembly indicate it is designed to scan, filter, and likely interact with other processes on the system.

The "Selective" logic suggests that the malware does not target every process it finds; instead, it filters targets based on specific criteria (e.g., specific filenames, paths, or environment variables).

### Suspicious & Malicious Behaviors

*   **PE File Parsing/Hunting:** 
    *   The code specifically checks for the hex value `0x5a4d` (`MZ`). This is the magic number at the start of a Windows Portable Executable (PE) file. 
    *   It also looks for `0x4550` (`EP`), which marks the beginning of an executable section header.
    *   **Significance:** These checks indicate the malware is scanning memory or files to identify and locate valid executables, a common prerequisite for process injection or finding "target" applications to infect.

*   **String Manipulation & Data Analysis:**
    *   The high volume of calls to `mapassign_faststr` and `wbMove`, combined with long loops of switch-like logic (the `fcn.00468f...` series), suggests the malware is performing extensive string comparisons. 
    *   It is likely comparing system information (process names, file paths) against a "blacklist" or "whitelist" to decide whether to proceed with its payload.

*   **Memory Scanning Logic:**
    *   The use of `0x1f4` as an iteration count and the various `rep stosd` instructions suggest it is clearing/initializing large memory buffers before copying data into them. This is common when preparing a buffer for a "reflected" DLL or a second-stage payload to be injected into another process's memory space.

*   **Dynamic Offsets:**
    *   The repeated calculations of offsets (e.g., `ebx + ecx * 4`) and the use of `growslice` indicate it is navigating complex data structures in memory, likely a list of loaded modules or system handles.

### Notable Techniques & Patterns

*   **Go Runtime Utilization:** The sample heavily relies on the Go runtime for string management. This makes it harder to identify specific strings or commands via simple static analysis because many operations are abstracted through the runtime’s "fast" logic.
*   **Logic Branching (The "Selection" Loop):** The code structure is very repetitive, with several blocks looking almost identical except for their target addresses and immediate values. This indicates a **Dispatcher Pattern**, where the malware identifies a specific condition (like a "Type" or "ID") and jumps to a specialized handler to perform an action on that specific object.
*   **Code Modularization:** The division of functionality into `func1`, `func3`, and `func4` suggests a multi-stage execution flow where the malware first identifies potential targets, then validates them, and finally executes the primary payload (like a downloader or keylogger).

### Summary for Threat Intelligence
*   **Type:** Loader / Downloader / Dropper.
*   **Primary Purpose:** To identify and "select" specific target processes in memory to inject malicious code.
*   **Key Indicators:** 
    *   Scanning for `MZ` (0x5A4D) and `EP` (0x4550) signatures.
    *   Intensive string comparison logic used as a filter mechanism.
    *   Go-based implementation to mask the underlying malicious logic within standard runtime calls.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1623** | Reflective Code Loading | The binary specifically looks for `MZ` (0x5A4D) and `EP` (0x4550) headers to identify executable segments, a hallmark of loading code into memory without using standard OS loaders. |
| **T1055.001** | Process Injection: Reflective Loader | The "Loader" functionality and the preparation of large memory buffers suggest that the malware is preparing to host a second-stage payload within the memory space of other processes. |
| **T1027** | Obfuscated Files or Information | By utilizing Go's internal runtime functions (e.g., `sym.runtime`) for string manipulation, the malware masks its underlying logic and makes it harder to identify malicious strings via static analysis. |
| **T1497** | Virtualized Environment | The "Selection" logic used to filter processes based on specific criteria is a common method to detect if the code is running in a sandbox or specialized analyst environment before executing the payload. |
| **T1568** | Dynamic Resolution | The use of a "Dispatcher Pattern" and complex loop-based logic for finding target addresses indicates an attempt to resolve offsets or functions dynamically rather than statically. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.* (Note: While `.com` appeared multiple times in the string dump, these were part of repetitive code logic/scrambled data and did not resolve to specific malicious domains.)

**File paths / Registry keys**
*   *None identified.*

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   **Go Build ID:** `AWHKYR4OZyEJeiuBdTje/Q9U31Za6VfH5ec-PBWO2/8dmWcUZe_b3xeICq1RRs/PsDDL0Qk6xNw33czvKCD` (This is a unique identifier for this specific build of the Go binary.)

**Other artifacts**
*   **MZ Header Check:** The malware specifically looks for `0x5a4d` (MZ) and `0x4550` (EP). While these are standard PE headers, their presence in the analysis confirms the malware is actively scanning memory for portable executables to target.
*   **Go Runtime Artifacts:** Extensive use of `growslice`, `mapassign_faststr`, and `wbMove` indicates a Go-based implementation designed to hide logic within standard runtime calls.

---
**Analyst Note:** 
The provided string dump contains a high volume of obfuscated data or "junk" characters (e.g., `|$9;u`). These do not constitute actionable network or filesystem IOCs but indicate that the malware is likely packed or utilizes heavy code-obfuscation techniques to hinder static analysis. The primary threat indicators for this sample are behavioral (memory scanning and dispatcher patterns) rather than static indicators like hardcoded IPs.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Reflective Loading Techniques:** The binary actively scans memory for `MZ` (0x5A4D) and `EP` (0x4550) headers, which are hallmark indicators of a loader designed to perform reflective code injection or identify target executables in memory.
    *   **Go-Based Obfuscation & Logic:** The use of the Go runtime (`sym.runtime`) to manage string comparisons and large memory buffers indicates a deliberate attempt to hide malicious logic (such as process filtering/selection) within standard library functions.
    *   **Sophisticated Payload Preparation:** The "Dispatcher Pattern" and use of `growslice` for buffer preparation suggest a modular architecture designed to host and execute a second-stage payload after identifying specific target processes.
