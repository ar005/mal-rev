# Threat Analysis Report

**Generated:** 2026-08-15 22:08 UTC
**Sample:** `0f55011a79a851db19afd2e1863867d861dd9c823c1c58e135b6904c9ea634f7_0f55011a79a851db19afd2e1863867d861dd9c823c1c58e135b6904c9ea634f7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f55011a79a851db19afd2e1863867d861dd9c823c1c58e135b6904c9ea634f7_0f55011a79a851db19afd2e1863867d861dd9c823c1c58e135b6904c9ea634f7.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 104,448 bytes |
| MD5 | `4529f0e9f250c647ea638bd3cd72edfa` |
| SHA1 | `bff71ae77154c29de1d49b6b40e56f4c6c086591` |
| SHA256 | `0f55011a79a851db19afd2e1863867d861dd9c823c1c58e135b6904c9ea634f7` |
| Overall entropy | 5.906 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767198531 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 53,760 | 6.434 | No |
| `.rdata` | 39,936 | 4.707 | No |
| `.data` | 3,072 | 2.095 | No |
| `.pdata` | 4,096 | 4.782 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.845 | No |

### Imports

**WININET.dll**: `InternetOpenA`, `InternetReadFile`, `InternetOpenUrlA`, `InternetCloseHandle`
**USER32.dll**: `DispatchMessageA`, `TranslateMessage`, `GetMessageA`
**ADVAPI32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`, `RegSetValueExA`
**KERNEL32.dll**: `GetConsoleMode`, `CreateFileW`, `WriteConsoleW`, `SetFilePointerEx`, `FreeLibrary`, `IsDebuggerPresent`, `CheckRemoteDebuggerPresent`, `CloseHandle`, `Sleep`, `GetCurrentProcess`, `CreateThread`, `FlushInstructionCache`, `GetTickCount`, `VirtualAlloc`, `DisableThreadLibraryCalls`

### Exports

`get_hostfxr_path`

## Extracted Strings

Total strings found: **395** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
.reloc
\$ ATAVAWH
A9OTv 
I+_0t~A
0A_A^A\
0A_A^A\
UVWAVAWH
A_A^_^]
|$ AVH
WATAUAVAWH
A_A^A]A\_
t$ WATAUAVAWH
 A_A^A]A\_
WATAUAVAWH
0A_A^A]A\_
H;XXs
H;xXu5
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
t98t H
u3HcH<H
x ATAVAWH
< t;<	t7
 A_A^A\
UVWAVAWH
H9:tH
0A_A^_^]
WAVAWH
L3
H3B
 A_A^_
D$0u3
\$8t	H
D$0@8{
u$D8r(tH
D81u`L9r
uPD8r(tH
vWD8s(tH
u$D8r(tH
fD91u_L9r
uPD8r(tH
vVD8s(tH
UVWATAUAVAWH
PA_A^A]A\_^]
WATAUAVAWH
0A_A^A]A\_
H9>u+A
@USVWATAUAVH
,/<-w
H
D8t$ht
H
D8t$ht
H
A^A]A\_^[]
f9)u4H9j
u%@8j(t
v@8k(t
8D$@tH
l$ VWATAVAWH
L$&8\$&t,8Y
A_A^A\_^
t$ WATAUAVAWH
 A_A^A]A\_
fD9t$b
t$ WATAUAVAWH
D!|$xA
A_A^A]A\_
L$ VWAVH
fD94H}aD
@SUVWATAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1800057e8` | `0x1800057e8` | 13503 | ✓ |
| `fcn.1800057b0` | `0x1800057b0` | 13498 | ✓ |
| `fcn.180001fac` | `0x180001fac` | 11399 | ✓ |
| `fcn.180001eac` | `0x180001eac` | 2302 | ✓ |
| `fcn.18000203c` | `0x18000203c` | 2024 | ✓ |
| `fcn.1800072e4` | `0x1800072e4` | 1985 | ✓ |
| `fcn.18000d550` | `0x18000d550` | 1677 | ✓ |
| `fcn.18000369c` | `0x18000369c` | 1213 | ✓ |
| `fcn.18000b690` | `0x18000b690` | 1171 | ✓ |
| `fcn.1800012b0` | `0x1800012b0` | 968 | ✓ |
| `fcn.18000a6d0` | `0x18000a6d0` | 922 | ✓ |
| `fcn.18000d190` | `0x18000d190` | 920 | ✓ |
| `fcn.18000a160` | `0x18000a160` | 920 | ✓ |
| `fcn.180001a70` | `0x180001a70` | 892 | ✓ |
| `fcn.180006ee8` | `0x180006ee8` | 862 | ✓ |
| `fcn.18000acb4` | `0x18000acb4` | 817 | ✓ |
| `fcn.18000bfdc` | `0x18000bfdc` | 815 | ✓ |
| `fcn.180007db0` | `0x180007db0` | 712 | ✓ |
| `fcn.180001680` | `0x180001680` | 689 | ✓ |
| `section..text` | `0x180001000` | 681 | ✓ |
| `fcn.180002298` | `0x180002298` | 667 | ✓ |
| `fcn.180007a0c` | `0x180007a0c` | 623 | ✓ |
| `fcn.180008e44` | `0x180008e44` | 604 | ✓ |
| `fcn.1800054b8` | `0x1800054b8` | 589 | ✓ |
| `fcn.180003b5c` | `0x180003b5c` | 584 | ✓ |
| `fcn.1800040fc` | `0x1800040fc` | 557 | ✓ |
| `fcn.180009d0c` | `0x180009d0c` | 555 | ✓ |
| `fcn.180002550` | `0x180002550` | 517 | ✓ |
| `fcn.180007814` | `0x180007814` | 501 | ✓ |
| `fcn.180003310` | `0x180003310` | 499 | ✓ |

### Decompiled Code Files

- [`code/fcn.1800012b0.c`](code/fcn.1800012b0.c)
- [`code/fcn.180001680.c`](code/fcn.180001680.c)
- [`code/fcn.180001a70.c`](code/fcn.180001a70.c)
- [`code/fcn.180001eac.c`](code/fcn.180001eac.c)
- [`code/fcn.180001fac.c`](code/fcn.180001fac.c)
- [`code/fcn.18000203c.c`](code/fcn.18000203c.c)
- [`code/fcn.180002298.c`](code/fcn.180002298.c)
- [`code/fcn.180002550.c`](code/fcn.180002550.c)
- [`code/fcn.180003310.c`](code/fcn.180003310.c)
- [`code/fcn.18000369c.c`](code/fcn.18000369c.c)
- [`code/fcn.180003b5c.c`](code/fcn.180003b5c.c)
- [`code/fcn.1800040fc.c`](code/fcn.1800040fc.c)
- [`code/fcn.1800054b8.c`](code/fcn.1800054b8.c)
- [`code/fcn.1800057b0.c`](code/fcn.1800057b0.c)
- [`code/fcn.1800057e8.c`](code/fcn.1800057e8.c)
- [`code/fcn.180006ee8.c`](code/fcn.180006ee8.c)
- [`code/fcn.1800072e4.c`](code/fcn.1800072e4.c)
- [`code/fcn.180007814.c`](code/fcn.180007814.c)
- [`code/fcn.180007a0c.c`](code/fcn.180007a0c.c)
- [`code/fcn.180007db0.c`](code/fcn.180007db0.c)
- [`code/fcn.180008e44.c`](code/fcn.180008e44.c)
- [`code/fcn.180009d0c.c`](code/fcn.180009d0c.c)
- [`code/fcn.18000a160.c`](code/fcn.18000a160.c)
- [`code/fcn.18000a6d0.c`](code/fcn.18000a6d0.c)
- [`code/fcn.18000acb4.c`](code/fcn.18000acb4.c)
- [`code/fcn.18000b690.c`](code/fcn.18000b690.c)
- [`code/fcn.18000bfdc.c`](code/fcn.18000bfdc.c)
- [`code/fcn.18000d190.c`](code/fcn.18000d190.c)
- [`code/fcn.18000d550.c`](code/fcn.18000d550.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis. The complexity of the code indicates that this is not a "simple" downloader; it contains sophisticated components typically found in advanced **multi-stage loaders** or **modular malware frameworks**.

### Updated Analysis Summary
The binary remains a **downloader/dropper**, but the additional disassembly reveals a high level of technical sophistication. It includes complex decryption loops, environmental fingerprinting (anti-analysis), and evidence of a "loader engine" capable of managing complex memory states and potentially executing modular components after the initial payload is fetched.

---

### Core Functionality (Updated)
*   **Persistence Mechanism:** Remains consistent—utilizes `Run` registry keys masked as `"EdgeUpdate"`.
*   **Remote Payload Retrieval:** Uses WinINet to fetch data from a remote server (`tbox.moe`).
*   **Complex In-Memory Decoding:** The new disassembly shows that the "decryption" phase is not a simple XOR; it involves complex arithmetic, multi-stage transformations (seen in `fcn.180001680` and `fcn.180007814`), and likely a rolling key or stream cipher approach to unpack the final payload.
*   **Advanced Loader Engine:** The presence of functions like `fcn.180009d0c` (handling reference counting/locks) and `fcn.180002550` suggests the binary manages a complex internal state, common in malware that supports multiple "plug-ins" or modules (e.g., different types of stealers or backdoors).

---

### New & Enhanced Technical Findings

#### 1. Advanced Obfuscation and Decryption Logic
The functions `fcn.180001680` and `fcn.180007814` are significant for their complexity:
*   **Multi-Pass Transformation:** These functions use nested loops and large, hardcoded data tables to transform data in memory. This is indicative of a "packer" or "loader" designed to hide the true nature of the payload until it is fully unpacked in memory.
*   **Stateful Decoding:** The use of modulo arithmetic (`uVar13 % arg4 + arg3`) and bitwise shifts suggests that the decryption key changes as the code progresses, making static analysis of the payload much harder for automated tools.

#### 2. Environmental Fingerprinting (Anti-Analysis)
The function **`fcn.180002298`** is highly significant:
*   **CPUID Analysis:** This function performs extensive checks on CPU features via `cpuid`. It looks for specific instruction sets and processor capabilities. 
*   **Evasion Purpose:** In malware, these checks are often used to detect virtual machine (VM) environments, debuggers, or hardware profiles. If the "wrong" environment is detected, the malware may behave differently or exit to avoid analysis by researchers.

#### 3. Sophisticated Memory Management
The function **`fcn.180009d0c`** provides insight into how the malware manages its lifecycle:
*   **Reference Counting & Thread Safety:** The use of `LOCK()` and `UNLOCK()` blocks combined with incrementing counters suggests that the binary is managing "objects" in memory. This implies a modular architecture where different components can be loaded or unloaded dynamically, ensuring that only the necessary code for a specific task is active at any given time.

#### 4. Complex Logic Branching (Execution Dispatcher)
The function **`fcn.1800040fc`** contains large amounts of conditional logic and nested checks:
*   **Dispatcher Behavior:** This appears to be an internal "switch" or dispatcher. It checks various states before deciding which piece of code to execute next. This is a hallmark of sophisticated malware (like those used by APT groups) where the primary binary acts as a host for multiple different functionalities.

---

### Updated Malicious Behaviors & Techniques

| Technique | Description | Code Evidence |
| :--- | :--- | :--- |
| **Persistence** | Creates "EdgeUpdate" in Registry `Run` key. | `fcn.1800012b0` (previous) |
| **Network Fetching** | Uses WinINet to pull payloads from malicious URLs. | WinINet API calls |
| **Anti-Analysis** | Performs CPUID checks to detect VMs/Sandboxes. | `fcn.180002298` |
| **Polymorphic/Complex Decoding** | Multi-stage decryption with rolling keys and bitwise math. | `fcn.180001680`, `fcn.180007814` |
| **Memory-Only Execution** | Payload exists only in memory after decoding; no file on disk. | Use of `VirtualAlloc` & heavy transformation loops |
| **Modular Architecture** | Uses reference counting and lock primitives to manage modules. | `fcn.180009d0c`, `fcn.180002550` |

---

### Conclusion / Threat Actor Profile
The complexity of the decoding logic, combined with specific CPUID fingerprinting and a robust internal management system (reference counting/locking), suggests that this binary belongs to a **sophisticated threat actor**. 

This is not just a "one-off" downloader; it is a professional-grade loader. It is designed to bypass automated sandbox detection, evade signature-based antivirus by using complex multi-stage decryption, and provide a stable environment for the final payload (which could be an information stealer, a remote access trojan (RAT), or part of a larger infection chain).

**Recommendation:** This binary should be treated as a high-priority threat. Because it uses in-memory execution and sophisticated evasion, traditional disk-scanning antivirus may fail to detect the secondary stages of the attack.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys/Startup Folder | The malware establishes persistence by creating a registry key named "EdgeUpdate" within the `Run` key. |
| **T1105** | Ingress Tool Transfer Protocol | The binary uses WinINet to fetch and download additional payloads from a remote server (`tbox.moe`). |
| **T1497** | Virtualization/Sandbox Detection | The use of `cpuid` instructions in function `fcn.180002298` indicates an attempt to detect and evade virtualized or analysis environments. |
| **T1027** | Packed_Data | The multi-pass transformation, rolling keys, and bitwise math used to de-obfuscate the payload are characteristic of packed data. |
| **T1055** | Packer | The "loader engine" architecture (handling reference counts and state) indicates a sophisticated packer designed to host multiple modular components. |
| **T1631** | Manipulation of System Configuration | Note: While not explicitly in your list, the complex dispatcher logic (`fcn.1800040fc`) suggests the loader acts as a gatekeeper for various internal system-altering modules. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, I have extracted the following Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `tbox.moe`
*   `files.ca`
*   (Note: The string `tbox.moe/ro64b5.https://files.ca` indicates these domains are used for payload retrieval.)

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\Run` (Registry Key)
*   `EdgeUpdate` (Registry Value used for persistence)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified in the provided text.

**Other artifacts**
*   **User-Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36`
*   **C2 Communication Method:** Utilization of the `WinINet` library for fetching remote payloads.
*   **Anti-Analysis Technique:** Implementation of `cpuid` instruction checks (at function offset `fcn.180002298`) to detect virtualized environments or sandboxes.
*   **Payload Obfuscation:** Use of multi-stage transformations involving modulo arithmetic and bitwise shifts (`fcn.180001680`, `fcn.180007814`) with rolling keys/key streams.
*   **Modular Architecture:** Presence of reference counting and lock primitives (`fcn.180009d0c`, `fcn.180002550`) indicating a multi-functionality loader (e.g., capable of hosting multiple modules like stealers or RATs).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `https://files.ca`

---

## Malware Family Classification

1. **Malware family**: custom (sophisticated loader framework)
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
* **Sophisticated Multi-Stage Decoding:** The presence of complex arithmetic, rolling keys, and multi-pass transformations (`fcn.180001680`, `fcn.180007814`) indicates a professional loader designed to hide the final payload from signature-based detection.
* **Modular Architecture & Dispatcher:** The use of reference counting, locking primitives, and a complex execution dispatcher (`fcn.1800040fc`) suggests the binary acts as a "loader engine" capable of hosting multiple functional modules (e.g., RATs or stealers) rather than being a single-purpose piece of malware.
* **Advanced Evasion Techniques:** The implementation of `cpuid` checks for environment fingerprinting (`fcn.180002298`) specifically targets the detection and evasion of virtual machines and sandboxes, typical of high-level threat actors.
