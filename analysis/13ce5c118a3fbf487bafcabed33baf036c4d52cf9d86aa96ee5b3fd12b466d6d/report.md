# Threat Analysis Report

**Generated:** 2026-09-03 00:45 UTC
**Sample:** `13ce5c118a3fbf487bafcabed33baf036c4d52cf9d86aa96ee5b3fd12b466d6d_13ce5c118a3fbf487bafcabed33baf036c4d52cf9d86aa96ee5b3fd12b466d6d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13ce5c118a3fbf487bafcabed33baf036c4d52cf9d86aa96ee5b3fd12b466d6d_13ce5c118a3fbf487bafcabed33baf036c4d52cf9d86aa96ee5b3fd12b466d6d.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 369,664 bytes |
| MD5 | `c647a40456f98f1912b75cb0e2e7fd28` |
| SHA1 | `8e205668879d806d5211abdcbeb1370f520af2ab` |
| SHA256 | `13ce5c118a3fbf487bafcabed33baf036c4d52cf9d86aa96ee5b3fd12b466d6d` |
| Overall entropy | 6.156 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767097742 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 52,224 | 6.387 | No |
| `.rdata` | 43,520 | 4.866 | No |
| `.data` | 265,216 | 6.22 | No |
| `.pdata` | 4,096 | 4.579 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 1,024 | 3.852 | No |
| `.reloc` | 2,048 | 4.958 | No |

### Imports

**SHELL32.dll**: `ShellExecuteExW`
**ADVAPI32.dll**: `LookupPrivilegeValueW`, `RegOpenKeyExA`, `OpenProcessToken`, `RegSetValueExA`, `AdjustTokenPrivileges`, `RegCloseKey`, `LookupPrivilegeValueA`
**SHLWAPI.dll**: `PathFindFileNameA`
**KERNEL32.dll**: `FlsAlloc`, `WriteConsoleW`, `SetFilePointerEx`, `GetModuleFileNameA`, `Process32First`, `WriteProcessMemory`, `HeapFree`, `GetCurrentProcess`, `lstrlenW`, `GetModuleFileNameW`, `lstrlenA`, `WaitForSingleObject`, `CreateFileW`, `GetModuleHandleA`, `OpenProcess`

## Extracted Strings

Total strings found: **1406** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
@USVWH
@USVWAVAWH
A_A^_^[]
\$ UWAVH
uxHc 
u0HcH<
t$ WATAUAVAWH
 A_A^A]A\_
WATAUAVAWH
0A_A^A]A\_
H;XXs
H;xXu5
WATAUAVAWH
A_A^A]A\_
AUAVAWH
9;|
HcC
u4I9}(
9I9}(tgH
0A_A^A]
UVWATAUAVAWH
`A_A^A]A\_^]
@USVWATAUAVAWH
G0HcX
G0HcX
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
WAVAWH
 A_A^_
WAVAWH
@SVWATAUAVAWH
A_A^A]A\_^[
A9	uaA
B(I9A(u
A9	u3A
SVWATAUAVAWH
|$$Hc^
@A_A^A]A\_^[
UVWATAUAVAWH
G0Lch
G0HcX
D$hIcu
 A_A^A]A\_^]
99~YHc^
D$0u3
\$8t	H
t98t H
tfD9y
UVWAVAWH
H9:tH
0A_A^_^]
WAVAWH
fA9,@u
fA9,vu
0A_A^_
	H;RJ
	H;.J
u3HcH<H
WAVAWH
 A_A^_
WAVAWH
L3
H3B
 A_A^_
D$0@8{
UVWATAUAVAWH
H;\$8u
H;\$8u
fD9$Ju
A_A^A]A\_^]
WATAUAVAWH
0A_A^A]A\_
H9>u+A
l$ VWATAVAWH
L$&8\$&t,8Y
A_A^A\_^
fD9t$b
@UATAUAVAWH
e0A_A^A]A\]
t$ WATAUAVAWH
 A_A^A]A\_
t$ WATAUAVAWH
D!|$xA
A_A^A]A\_
L$ VWAVH
fD94H}aD
@SUVWATAVAWH
@A_A^A\_^][
t$ WATAUAVAWH
0A_A^A]A\_
ATAUAVAWH
L$ |+L;
A_A^A]A\
@UATAUAVAWH
A_A^A]A\]
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140005f98` | `0x140005f98` | 15195 | ✓ |
| `fcn.140005f84` | `0x140005f84` | 15154 | ✓ |
| `fcn.14000cf30` | `0x14000cf30` | 1677 | ✓ |
| `fcn.1400076d4` | `0x1400076d4` | 1421 | ✓ |
| `fcn.14000389c` | `0x14000389c` | 1213 | ✓ |
| `fcn.14000b2dc` | `0x14000b2dc` | 1171 | ✓ |
| `fcn.14000cb70` | `0x14000cb70` | 920 | ✓ |
| `fcn.14000a860` | `0x14000a860` | 920 | ✓ |
| `fcn.1400011c0` | `0x1400011c0` | 824 | ✓ |
| `fcn.14000abf8` | `0x14000abf8` | 817 | ✓ |
| `fcn.14000bc28` | `0x14000bc28` | 815 | ✓ |
| `fcn.140001cd0` | `0x140001cd0` | 780 | ✓ |
| `fcn.140007f60` | `0x140007f60` | 712 | ✓ |
| `fcn.1400017b0` | `0x1400017b0` | 702 | ✓ |
| `fcn.140001500` | `0x140001500` | 681 | ✓ |
| `fcn.1400024f0` | `0x1400024f0` | 667 | ✓ |
| `fcn.140007bbc` | `0x140007bbc` | 623 | ✓ |
| `fcn.140009b8c` | `0x140009b8c` | 604 | ✓ |
| `fcn.1400054f4` | `0x1400054f4` | 597 | ✓ |
| `fcn.140003d5c` | `0x140003d5c` | 584 | ✓ |
| `fcn.1400042fc` | `0x1400042fc` | 557 | ✓ |
| `fcn.1400090b8` | `0x1400090b8` | 555 | ✓ |
| `fcn.140003028` | `0x140003028` | 517 | ✓ |
| `fcn.1400079c4` | `0x1400079c4` | 501 | ✓ |
| `fcn.140003510` | `0x140003510` | 499 | ✓ |
| `fcn.1400076dc` | `0x1400076dc` | 462 | ✓ |
| `fcn.14000a474` | `0x14000a474` | 445 | ✓ |
| `fcn.14000a67c` | `0x14000a67c` | 437 | ✓ |
| `fcn.1400094c4` | `0x1400094c4` | 434 | ✓ |
| `fcn.140005acc` | `0x140005acc` | 430 | ✓ |

### Decompiled Code Files

- [`code/fcn.1400011c0.c`](code/fcn.1400011c0.c)
- [`code/fcn.140001500.c`](code/fcn.140001500.c)
- [`code/fcn.1400017b0.c`](code/fcn.1400017b0.c)
- [`code/fcn.140001cd0.c`](code/fcn.140001cd0.c)
- [`code/fcn.1400024f0.c`](code/fcn.1400024f0.c)
- [`code/fcn.140003028.c`](code/fcn.140003028.c)
- [`code/fcn.140003510.c`](code/fcn.140003510.c)
- [`code/fcn.14000389c.c`](code/fcn.14000389c.c)
- [`code/fcn.140003d5c.c`](code/fcn.140003d5c.c)
- [`code/fcn.1400042fc.c`](code/fcn.1400042fc.c)
- [`code/fcn.1400054f4.c`](code/fcn.1400054f4.c)
- [`code/fcn.140005acc.c`](code/fcn.140005acc.c)
- [`code/fcn.140005f84.c`](code/fcn.140005f84.c)
- [`code/fcn.140005f98.c`](code/fcn.140005f98.c)
- [`code/fcn.1400076d4.c`](code/fcn.1400076d4.c)
- [`code/fcn.1400076dc.c`](code/fcn.1400076dc.c)
- [`code/fcn.1400079c4.c`](code/fcn.1400079c4.c)
- [`code/fcn.140007bbc.c`](code/fcn.140007bbc.c)
- [`code/fcn.140007f60.c`](code/fcn.140007f60.c)
- [`code/fcn.1400090b8.c`](code/fcn.1400090b8.c)
- [`code/fcn.1400094c4.c`](code/fcn.1400094c4.c)
- [`code/fcn.140009b8c.c`](code/fcn.140009b8c.c)
- [`code/fcn.14000a474.c`](code/fcn.14000a474.c)
- [`code/fcn.14000a67c.c`](code/fcn.14000a67c.c)
- [`code/fcn.14000a860.c`](code/fcn.14000a860.c)
- [`code/fcn.14000abf8.c`](code/fcn.14000abf8.c)
- [`code/fcn.14000b2dc.c`](code/fcn.14000b2dc.c)
- [`code/fcn.14000bc28.c`](code/fcn.14000bc28.c)
- [`code/fcn.14000cb70.c`](code/fcn.14000cb70.c)
- [`code/fcn.14000cf30.c`](code/fcn.14000cf30.c)

## Behavioral Analysis

This additional disassembly provides further evidence of sophisticated malware techniques, specifically in the areas of **dynamic code execution**, **memory manipulation**, and **complex data obfuscation**.

The following analysis integrates these new findings with the previously identified behaviors.

### Updated Analysis: New Findings from Chunk 2

#### 1. Dynamic API Resolution & Obfuscated Loading
In `fcn.1400094c4`, the code implements a custom **Dynamic API Resolver**. Instead of relying on a standard Import Address Table (IAT), which is easily audited, it performs the following:
*   **Manual Library Loading:** It iterates through an internal list of function names and attempts to find them using `GetProcAddress` and `LoadLibraryExW`. 
*   **Fallback Mechanisms:** If a library or function is not immediately available, it includes logic to "retry" or re-map the procedure. This allows the malware to resolve its intended functions only at runtime, significantly hiding its capabilities from static analysis tools.
*   **Memory Protection Manipulation:** Before finalizing the resolution of a function, the code calls `VirtualProtect`. Specifically, it alters the permissions of a memory range (`0x14005c000`). This is a classic technique used to make a decrypted "payload" or "stub" executable in memory immediately after it is unpacked.

#### 2. Sophisticated Data Obfuscation (Encryption/Decoding)
The functions `fcn.1400079c4` and `fcn.140005ac` indicate a high level of internal data processing:
*   **Bitwise Rotation & XOR:** In `fcn.140005ac`, the code performs repeated bitwise rotations (e.g., `(val >> shift) | (val << (64-shift))`) combined with XOR operations against a hardcoded/global key (`0x140019000`). This suggests that the malware's configuration, internal strings, or next-stage payloads are heavily obfuscated and only decrypted in memory during execution.
*   **Buffer Management:** The large local arrays and complex indexing in `fcn.1400079c4` suggest it is processing blocks of data (possibly a custom protocol or a compressed configuration file) to prepare it for use by the main logic.

#### 3. Advanced Execution Environment Handling
The presence of `fcn.140003028`, which interacts with **`RtlUnwindEx`**, is significant. This function deals with stack walking and exception handling:
*   **Context Awareness:** By utilizing "unwinding" logic, the malware can determine the state of the call stack. This is often used by advanced threats to find the correct context for injecting code into other processes or to gracefully handle exceptions during complex multi-stage unpacking processes where traditional error handling might crash the process and alert the user/AV.

---

### Updated Synthesis of Malicious Behavior

Based on both parts of the disassembly, here is the updated profile:

| Category | Finding | Impact |
| :--- | :--- | :--- |
| **Persistence** | Registry "Run" keys & Scheduled Tasks ("Windows SystemEnv Core"). | Ensures long-term presence and high privilege execution. |
| **Evasion** | CPU instruction checks (AVX, SSE4.1) & Process Enumeration. | Detects sandboxes/virtual machines and determines if a user is active. |
| **Privilege Escalation** | Explicit request for `SeDebugPrivilege`. | Allows the malware to inject code into high-value targets like `lsass.exe`. |
| **Obfuscation** | Bitwise rotation & XOR; Custom Dynamic API Resolution. | Hinders static analysis and hides intended capabilities from security software. |
| **Anti-Analysis** | Use of `VirtualProtect` for execution redirection. | Indicates a multi-stage "packer" or "loader" behavior where the final payload is decrypted in memory. |

### Summary for Reporting (Updated)

The sample is a sophisticated, multi-stage malware specimen (likely a Trojan/Downloader). It exhibits several hallmarks of advanced persistent threats:

1.  **Multi-Vector Persistence:** Uses both Registry keys and Scheduled Tasks to ensure it remains active on the system even if one method is remediated.
2.  **Advanced Obfuscation Engine:** The binary does not rely on standard imports for its core functionality; instead, it uses a custom loader to resolve APIs at runtime and employs bitwise rotation/XOR logic to hide its internal configuration and strings.
3.  **Environment Awareness:** It actively checks for virtualization features and other system indicators before "unpacking" or proceeding with malicious actions.
4.  **Privilege & Memory Manipulation:** The request for `SeDebugPrivilege` combined with the use of `VirtualProtect` strongly suggests an intent to perform process injection or memory-resident payload execution (fileless techniques).

**Conclusion:** This is a high-confidence malicious sample designed to evade automated detection while establishing deep persistence and preparing the environment for potentially more advanced activities, such as credential theft or data exfiltration.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Registry Run Keys / Startup Folder | The malware utilizes "Run" keys to ensure it persists and executes automatically upon system startup. |
| T1053.005 | Scheduled Task | The creation of the "Windows SystemEnv Core" task provides a secondary mechanism for maintaining long-term persistence. |
| T1497 | Virtualization/Sandbox Detection | The malware checks for specific CPU instructions (AVX, SSE4.1) and performs process enumeration to detect if it is running in an analysis environment. |
| T1027 | Obfuscated Capabilities | The use of a custom Dynamic API Resolver, bitwise rotations, and XOR operations serves to hide the malware's functionality from static analysis tools. |
| T1055 | Process Injection | The combination of `VirtualProtect` for memory permission manipulation and the request for `SeDebugPrivilege` indicates an intent to execute code in-memory or inject it into other processes. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified (Note: The report mentions "Registry 'Run' keys," but no specific registry paths were provided).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Scheduled Task Name:** `Windows SystemEnv Core` (Used for persistence)
*   **Memory Address:** `0x14005c000` (Specifically associated with a `VirtualProtect` call during the Dynamic API Resolution phase).

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification of the sample:

1.  **Malware family:** Custom
2.  **Malware type:** Loader / Downloader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Advanced Evasion & Obfuscation:** The use of a custom Dynamic API Resolver (hiding the IAT), bitwise rotation, and XOR operations indicates a multi-stage design intended to hide core functionality and payloads from static analysis.
    *   **Privilege Escalation for Injection:** The explicit request for `SeDebugPrivilege` combined with `VirtualProtect` manipulation is a classic indicator of "fileless" behavior, where the loader prepares the environment to inject code into high-value processes (like `lsass.exe`) or execute unpacked payloads in memory.
    *   **Robust Persistence & Environment Awareness:** The use of dual persistence mechanisms (Registry Run keys and Scheduled Tasks) alongside specific hardware/instruction checks (AVX, SSE4.1) confirms the sample is designed for long-term residency on a target system while evading automated sandbox detection.
