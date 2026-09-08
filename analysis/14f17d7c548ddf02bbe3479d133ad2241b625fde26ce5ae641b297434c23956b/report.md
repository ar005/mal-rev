# Threat Analysis Report

**Generated:** 2026-09-06 13:42 UTC
**Sample:** `14f17d7c548ddf02bbe3479d133ad2241b625fde26ce5ae641b297434c23956b_14f17d7c548ddf02bbe3479d133ad2241b625fde26ce5ae641b297434c23956b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14f17d7c548ddf02bbe3479d133ad2241b625fde26ce5ae641b297434c23956b_14f17d7c548ddf02bbe3479d133ad2241b625fde26ce5ae641b297434c23956b.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 104,448 bytes |
| MD5 | `e7c3b787c0af52dd102675ac8d398bcb` |
| SHA1 | `89a1abbf6bdd63a927979743dfda314b571a373a` |
| SHA256 | `14f17d7c548ddf02bbe3479d133ad2241b625fde26ce5ae641b297434c23956b` |
| Overall entropy | 5.877 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767628769 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 53,760 | 6.412 | No |
| `.rdata` | 39,936 | 4.68 | No |
| `.data` | 3,072 | 2.105 | No |
| `.pdata` | 4,096 | 4.747 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.848 | No |

### Imports

**WININET.dll**: `InternetOpenA`, `InternetReadFile`, `InternetOpenUrlA`, `InternetCloseHandle`
**USER32.dll**: `DispatchMessageA`, `TranslateMessage`, `GetMessageA`
**KERNEL32.dll**: `IsProcessorFeaturePresent`, `WriteConsoleW`, `CreateFileW`, `SetFilePointerEx`, `GetConsoleMode`, `IsDebuggerPresent`, `CheckRemoteDebuggerPresent`, `CloseHandle`, `Sleep`, `GetCurrentProcess`, `CreateThread`, `FlushInstructionCache`, `GetTickCount`, `VirtualAlloc`, `DisableThreadLibraryCalls`

### Exports

`get_hostfxr_path`

## Extracted Strings

Total strings found: **388** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
.reloc
UVWAVAWH
A_A^_^]
\$ ATAVAWH
A9OTv 
I+_0t~A
0A_A^A\
0A_A^A\
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
| `fcn.180005720` | `0x180005720` | 13511 | ✓ |
| `fcn.1800056e8` | `0x1800056e8` | 13506 | ✓ |
| `fcn.180001eec` | `0x180001eec` | 11391 | ✓ |
| `fcn.180001dec` | `0x180001dec` | 2302 | ✓ |
| `fcn.180001f7c` | `0x180001f7c` | 2024 | ✓ |
| `fcn.180007224` | `0x180007224` | 1985 | ✓ |
| `fcn.18000d490` | `0x18000d490` | 1677 | ✓ |
| `fcn.1800035dc` | `0x1800035dc` | 1213 | ✓ |
| `fcn.18000b5d0` | `0x18000b5d0` | 1171 | ✓ |
| `fcn.18000a610` | `0x18000a610` | 922 | ✓ |
| `fcn.18000d0d0` | `0x18000d0d0` | 920 | ✓ |
| `fcn.18000a0a0` | `0x18000a0a0` | 920 | ✓ |
| `fcn.1800019b0` | `0x1800019b0` | 892 | ✓ |
| `fcn.180006e28` | `0x180006e28` | 862 | ✓ |
| `fcn.18000abf4` | `0x18000abf4` | 817 | ✓ |
| `fcn.18000bf1c` | `0x18000bf1c` | 815 | ✓ |
| `section..text` | `0x180001000` | 777 | ✓ |
| `fcn.180007cf0` | `0x180007cf0` | 712 | ✓ |
| `fcn.180001310` | `0x180001310` | 689 | ✓ |
| `fcn.1800015d0` | `0x1800015d0` | 681 | ✓ |
| `fcn.1800021d8` | `0x1800021d8` | 667 | ✓ |
| `fcn.18000794c` | `0x18000794c` | 623 | ✓ |
| `fcn.180008d84` | `0x180008d84` | 604 | ✓ |
| `fcn.1800053f0` | `0x1800053f0` | 589 | ✓ |
| `fcn.180003a9c` | `0x180003a9c` | 584 | ✓ |
| `fcn.18000403c` | `0x18000403c` | 557 | ✓ |
| `fcn.180009c4c` | `0x180009c4c` | 555 | ✓ |
| `fcn.180002490` | `0x180002490` | 517 | ✓ |
| `fcn.180007754` | `0x180007754` | 501 | ✓ |
| `fcn.180003250` | `0x180003250` | 499 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001310.c`](code/fcn.180001310.c)
- [`code/fcn.1800015d0.c`](code/fcn.1800015d0.c)
- [`code/fcn.1800019b0.c`](code/fcn.1800019b0.c)
- [`code/fcn.180001dec.c`](code/fcn.180001dec.c)
- [`code/fcn.180001eec.c`](code/fcn.180001eec.c)
- [`code/fcn.180001f7c.c`](code/fcn.180001f7c.c)
- [`code/fcn.1800021d8.c`](code/fcn.1800021d8.c)
- [`code/fcn.180002490.c`](code/fcn.180002490.c)
- [`code/fcn.180003250.c`](code/fcn.180003250.c)
- [`code/fcn.1800035dc.c`](code/fcn.1800035dc.c)
- [`code/fcn.180003a9c.c`](code/fcn.180003a9c.c)
- [`code/fcn.18000403c.c`](code/fcn.18000403c.c)
- [`code/fcn.1800053f0.c`](code/fcn.1800053f0.c)
- [`code/fcn.1800056e8.c`](code/fcn.1800056e8.c)
- [`code/fcn.180005720.c`](code/fcn.180005720.c)
- [`code/fcn.180006e28.c`](code/fcn.180006e28.c)
- [`code/fcn.180007224.c`](code/fcn.180007224.c)
- [`code/fcn.180007754.c`](code/fcn.180007754.c)
- [`code/fcn.18000794c.c`](code/fcn.18000794c.c)
- [`code/fcn.180007cf0.c`](code/fcn.180007cf0.c)
- [`code/fcn.180008d84.c`](code/fcn.180008d84.c)
- [`code/fcn.180009c4c.c`](code/fcn.180009c4c.c)
- [`code/fcn.18000a0a0.c`](code/fcn.18000a0a0.c)
- [`code/fcn.18000a610.c`](code/fcn.18000a610.c)
- [`code/fcn.18000abf4.c`](code/fcn.18000abf4.c)
- [`code/fcn.18000b5d0.c`](code/fcn.18000b5d0.c)
- [`code/fcn.18000bf1c.c`](code/fcn.18000bf1c.c)
- [`code/fcn.18000d0d0.c`](code/fcn.18000d0d0.c)
- [`code/fcn.18000d490.c`](code/fcn.18000d490.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

Based on the analysis of the second chunk of disassembly, several critical new capabilities and techniques have been identified. These findings significantly upgrade the threat profile of this binary from a simple downloader to a **sophisticated multi-stage loader**.

The updated summary below integrates your previous findings with the newly discovered behaviors.

### Updated Analysis Summary

#### 1. Core Functionality and Purpose
The binary is a sophisticated **Downloader, Dropper, and Reflective Loader**. 
*   **Primary Role:** It fetches an obfuscated payload from a remote server (as identified in chunk 1).
*   **Advanced Execution:** Unlike simple droppers that simply write a file to disk and execute it, this binary contains logic to **manually map/load PE files into memory** (`fcn.1800015d0`). This suggests the malware can execute the second-stage payload directly in memory or via process injection to evade traditional on-disk scanning.

#### 2. Sophisticated Payload De-obfuscation
The analysis of `fcn.180001310` reveals a complex decryption routine:
*   **Multi-layered XORing:** The code uses a systematic loop to perform bitwise operations (XOR) on the received data. It utilizes internal tables and offset calculations to process the buffer.
*   **In-Memory Processing:** This function is designed to "clean" the payload in memory before it reaches the file system or the loading stage, ensuring that the malicious signature of the final payload remains hidden from simple string/pattern scanners during transit and initial processing.

#### 3. Advanced Loader Characteristics (Reflective Loading)
The function `fcn.1800015d0` is a textbook implementation of a **PE Loader**:
*   **Signature Verification:** It checks for the "MZ" (`0x5A4D`) and "PE" (`0x4550`) headers.
*   **Memory Mapping:** It uses `VirtualAlloc` to reserve memory and then maps segments (headers, sections) into that space.
*   **Import Resolution:** It manually iterates through the Import Address Table (IAT), using `LoadLibraryA` and `GetProcAddress` to resolve required functions for the payload at runtime.
*   **Execution:** It uses `FlushInstructionCache` and `CreateThread` to launch the decoded payload in a new thread, which is a hallmark of **Reflective DLL Injection**.

#### 4. Anti-Analysis & Environment Awareness (Expanded)
In addition to the previously identified `IsDebuggerPresent` and time-based "stalling," the new code reveals:
*   **Hardware/CPU Fingerprinting:** Function `fcn.1800021d8` interacts with `CPUID` instructions to check for specific CPU features (e.g., SSE, AVX). This is often used by malware to detect virtualized environments or specialized "sandbox" hardware that may not support the full range of instruction sets found on physical machines.
*   **System Integrity Checks:** Several internal functions suggest the presence of a custom runtime environment designed to handle heavy lifting (like memory management and thread synchronization) while minimizing the number of direct, suspicious system calls made by the primary payload logic.

#### 5. Summary of Malicious Techniques Found
| Technique | Implementation Detail | Purpose |
| :--- | :--- | :--- |
| **Reflective Loading** | `fcn.1800015d0` (Manual PE Mapping) | Execute payloads in memory to bypass EDR/AV file-scanners. |
| **Complex De-obfuscation** | `fcn.180001310` (Iterative XOR & Table Lookups) | Hide the final payload's signature from detection during transport. |
| **Environment Fingerprinting** | `fcn.1800021d8` (CPUID Analysis) | Detect and evade execution in sandboxes or virtual machines. |
| **Evasion via Delay** | `GetTickCount` & Math-based stalls | Bypass automated "sandbox" timing checks. |
| **Network Communication** | `WinINet` (`InternetReadFile`) | Fetch the malicious payload from a remote C2 server. |

### Final Conclusion (Updated)
This is not a basic downloader; it is a **high-capability loader module**. It is designed to be the "first stage" of a multi-stage attack. Its purpose is to establish a foothold, bypass local security controls using anti-analysis and de-obfuscation routines, and then host/inject a much more powerful secondary payload (such as a RAT or ransomware) directly into memory via reflective loading techniques. 

**Recommendation:** This sample should be treated as part of a sophisticated threat actor's toolkit. Any system where this binary is found should be checked for evidence of "fileless" execution, as the primary malicious payload may never touch the hard drive in its original form.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your report to the corresponding MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1620** | Reflective Loader | The binary performs manual PE mapping, IAT resolution, and memory execution to load a second-stage payload without writing it to disk. |
| **T1027** | Obfuscated Files or Information | Multi-layered XOR loops and custom decryption routines are used to hide the malicious signature of the payload during transmission and initial processing. |
| **T1497** | Virtualization/Sandbox Detection | The use of CPUID instructions to fingerprint hardware and time-based stalls (GetTickCount) indicates an attempt to evade analysis in virtualized environments. |
| **T1105** | Ingress Tool Transfer | The binary utilizes WinINet (`InternetReadFile`) to fetch malicious components from a remote server during the initial infection stage. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `tbox.moe`
*   `2ctvdn` (Potential subdomain/path component)
*   `files.ca`
*   *Note: The string `tbox.moe/2ctvdn.https://files.ca` suggests these domains are used for fetching payloads via the WinINet API.*

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified (The character strings provided appear to be obfuscated data or junk code rather than standard MD5/SHA1/SHA256 hashes).

**Other artifacts**
*   **User Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36` (Used during the network communication phase).
*   **Malicious Function Offsets (Behavioral Indicators):**
    *   `fcn.1800015d0`: Used for manual PE mapping and reflective loading.
    *   `fcn.180001310`: Used for multi-layered XOR decryption of the payload.
    *   `fcn.1800021d8`: Used for CPUID analysis to detect virtualized/sandbox environments.
*   **C2 Communication Pattern:** Use of `WinINet` and `InternetReadFile` to fetch and process payloads in memory.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `https://files.ca`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Reflective Loading:** The binary implements a full manual PE mapping routine (including IAT resolution and `CreateThread`), allowing it to execute secondary payloads directly in memory to bypass disk-based security scans.
    *   **Sophisticated Evasion:** It employs multiple anti-analysis layers, including CPUID fingerprinting for environment detection and time-based stalling to evade automated sandbox analysis.
    *   **Multi-stage Delivery:** The binary functions as a sophisticated "first stage" loader that retrieves, de-obfuscates (via multi-layered XOR), and injects payloads from remote C2 servers.
