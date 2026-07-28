# Threat Analysis Report

**Generated:** 2026-07-26 11:17 UTC
**Sample:** `0b834be7c5b7197451ff729390f6c4048d9108738b015bd7dbccdb39e3c9432c_0b834be7c5b7197451ff729390f6c4048d9108738b015bd7dbccdb39e3c9432c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b834be7c5b7197451ff729390f6c4048d9108738b015bd7dbccdb39e3c9432c_0b834be7c5b7197451ff729390f6c4048d9108738b015bd7dbccdb39e3c9432c.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 108,544 bytes |
| MD5 | `2c6e2b0754086b25f22e5885f4a5a4c0` |
| SHA1 | `afd60d7bfa46986c3d85dd62ca66b2dda2ffbbf5` |
| SHA256 | `0b834be7c5b7197451ff729390f6c4048d9108738b015bd7dbccdb39e3c9432c` |
| Overall entropy | 5.925 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768014800 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 57,344 | 6.435 | No |
| `.rdata` | 40,448 | 4.728 | No |
| `.data` | 3,072 | 2.088 | No |
| `.pdata` | 4,096 | 4.696 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.849 | No |

### Imports

**OLEAUT32.dll**: `SafeArrayDestroy`, `SafeArrayGetUBound`, `SafeArrayAccessData`, `SafeArrayUnaccessData`, `SafeArrayPutElement`, `VariantClear`, `VariantInit`, `SafeArrayCreateVector`, `SafeArrayCreate`
**USER32.dll**: `DispatchMessageA`, `TranslateMessage`, `GetMessageA`
**ADVAPI32.dll**: `GetUserNameA`
**KERNEL32.dll**: `CreateFileW`, `SetFilePointerEx`, `WriteConsoleW`, `GetConsoleOutputCP`, `WriteFile`, `FlushFileBuffers`, `SetStdHandle`, `HeapReAlloc`, `HeapSize`, `GetConsoleMode`, `InitializeCriticalSectionEx`, `CreateFileA`, `GetDiskFreeSpaceExA`, `GetFileSize`, `ReadFile`

### Exports

`get_hostfxr_path`

## Extracted Strings

Total strings found: **414** (showing first 100)

```
!This program cannot be run in DOS mode.
$
RichSg
`.rdata
@.data
.pdata
@.fptable
.reloc
t}HcH<E3
@USVWATAUAVAWH
PPD9|$p
A_A^A]A\_^[]
D$Hnpwp
D$Lw|m7
D$P}uu
D$`4~vv
D$h}BY_
D$l^JGj
D$pGGDH
D$xcD^Of
D$|XDO^
D$Hbin
UVWAVAWH
A_A^_^]
D$H.<{M
D$ Q(N
H9D$Xr
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1800066f0` | `0x1800066f0` | 13511 | ✓ |
| `fcn.1800066b8` | `0x1800066b8` | 13506 | ✓ |
| `fcn.180002eac` | `0x180002eac` | 11407 | ✓ |
| `fcn.1800011c0` | `0x1800011c0` | 2500 | ✓ |
| `fcn.180002dac` | `0x180002dac` | 2318 | ✓ |
| `fcn.180002f3c` | `0x180002f3c` | 2040 | ✓ |
| `fcn.1800081f4` | `0x1800081f4` | 1985 | ✓ |
| `fcn.18000e0a0` | `0x18000e0a0` | 1677 | ✓ |
| `fcn.1800045a8` | `0x1800045a8` | 1213 | ✓ |
| `fcn.18000c5a0` | `0x18000c5a0` | 1171 | ✓ |
| `fcn.1800023e0` | `0x1800023e0` | 1120 | ✓ |
| `fcn.180001bf0` | `0x180001bf0` | 1022 | ✓ |
| `fcn.18000b5e0` | `0x18000b5e0` | 922 | ✓ |
| `fcn.18000e750` | `0x18000e750` | 920 | ✓ |
| `fcn.18000b070` | `0x18000b070` | 920 | ✓ |
| `fcn.180002970` | `0x180002970` | 892 | ✓ |
| `fcn.180007df8` | `0x180007df8` | 862 | ✓ |
| `fcn.18000bbc4` | `0x18000bbc4` | 817 | ✓ |
| `fcn.18000ceec` | `0x18000ceec` | 815 | ✓ |
| `fcn.180008cc0` | `0x180008cc0` | 712 | ✓ |
| `fcn.180002120` | `0x180002120` | 689 | ✓ |
| `fcn.180003198` | `0x180003198` | 667 | ✓ |
| `fcn.18000891c` | `0x18000891c` | 623 | ✓ |
| `fcn.180009d54` | `0x180009d54` | 604 | ✓ |
| `fcn.1800063c0` | `0x1800063c0` | 589 | ✓ |
| `fcn.180004a68` | `0x180004a68` | 584 | ✓ |
| `fcn.180005008` | `0x180005008` | 557 | ✓ |
| `fcn.18000ac1c` | `0x18000ac1c` | 555 | ✓ |
| `fcn.180003460` | `0x180003460` | 517 | ✓ |
| `fcn.180008724` | `0x180008724` | 501 | ✓ |

### Decompiled Code Files

- [`code/fcn.1800011c0.c`](code/fcn.1800011c0.c)
- [`code/fcn.180001bf0.c`](code/fcn.180001bf0.c)
- [`code/fcn.180002120.c`](code/fcn.180002120.c)
- [`code/fcn.1800023e0.c`](code/fcn.1800023e0.c)
- [`code/fcn.180002970.c`](code/fcn.180002970.c)
- [`code/fcn.180002dac.c`](code/fcn.180002dac.c)
- [`code/fcn.180002eac.c`](code/fcn.180002eac.c)
- [`code/fcn.180002f3c.c`](code/fcn.180002f3c.c)
- [`code/fcn.180003198.c`](code/fcn.180003198.c)
- [`code/fcn.180003460.c`](code/fcn.180003460.c)
- [`code/fcn.1800045a8.c`](code/fcn.1800045a8.c)
- [`code/fcn.180004a68.c`](code/fcn.180004a68.c)
- [`code/fcn.180005008.c`](code/fcn.180005008.c)
- [`code/fcn.1800063c0.c`](code/fcn.1800063c0.c)
- [`code/fcn.1800066b8.c`](code/fcn.1800066b8.c)
- [`code/fcn.1800066f0.c`](code/fcn.1800066f0.c)
- [`code/fcn.180007df8.c`](code/fcn.180007df8.c)
- [`code/fcn.1800081f4.c`](code/fcn.1800081f4.c)
- [`code/fcn.180008724.c`](code/fcn.180008724.c)
- [`code/fcn.18000891c.c`](code/fcn.18000891c.c)
- [`code/fcn.180008cc0.c`](code/fcn.180008cc0.c)
- [`code/fcn.180009d54.c`](code/fcn.180009d54.c)
- [`code/fcn.18000ac1c.c`](code/fcn.18000ac1c.c)
- [`code/fcn.18000b070.c`](code/fcn.18000b070.c)
- [`code/fcn.18000b5e0.c`](code/fcn.18000b5e0.c)
- [`code/fcn.18000bbc4.c`](code/fcn.18000bbc4.c)
- [`code/fcn.18000c5a0.c`](code/fcn.18000c5a0.c)
- [`code/fcn.18000ceec.c`](code/fcn.18000ceec.c)
- [`code/fcn.18000e0a0.c`](code/fcn.18000e0a0.c)
- [`code/fcn.18000e750.c`](code/fcn.18000e750.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis. The new code provides deeper insight into the malware's anti-analysis techniques, its interaction with the file system, and its sophisticated data-processing routines.

### Updated Analysis Summary: Malware Loader / Information Stealer

The binary remains consistent with a high-capability **malware loader or information stealer**. The additional disassembly reveals more sophisticated "environment hardening" (detecting virtualization) and evidence of systematic file system interaction.

---

### Core Functionality
*   **System Information Gathering:** (Previously identified) The malware continues to gather and obfuscate local system data before transmission.
*   **Network Communication & Masking:** (Previously identified) Use of a high-fidelity User-Agent indicates readiness for C2 communication.
*   **Advanced Data Processing:** Several functions (e.g., `fcn.18000b070` and `fcn.18000bc4`) contain complex nested loops and pointer arithmetic to manipulate memory buffers. This suggests the malware is preparing, aligning, or "packing" stolen data into a specific format before it is sent over the network.
*   **Locale-Aware Operations:** The presence of `GetCPInfo` (in `fcn.180008cc0`) and checks for valid code pages indicates the malware is designed to handle diverse system locales, ensuring it can successfully scrape or process text from the OS regardless of the user's language settings.

### Suspicious and Malicious Behaviors
*   **Enhanced Anti-Analysis & Anti-Virtualization:**
    *   **Hardware Fingerprinting:** In `fcn.180003198`, the code calls several `cpuid` functions (`cpuid_basic_info`, `cpuid_Version_info`, `cpuid_Extended_Feature_Enumeration_info`). It specifically checks for CPU features, model IDs, and instruction sets (like AVX).
    *   **Sandbox Detection:** These `cpuid` checks are a common technique to determine if the code is running on a physical machine or within a virtualized environment/sandbox. If the hardware "features" do not match a standard consumer PC profile, the malware may cease execution or alter its behavior to hide from researchers.
*   **File System Reconnaissance:** 
    *   The function `fcn.180007df8` explicitly utilizes `FindFirstFileExW` and `FindNextFileW`. This indicates the malware is actively searching for files on the disk. In an information stealer, this is often used to find:
        1.  Configuration files or "hidden" instructions from a first-stage dropper.
        2.  Targeted user data (e.g., browser profiles, crypto wallets, or sensitive documents).
*   **Complex Data Serialization:** The large loops and switch-like structures in functions like `fcn.180009d54` suggest the malware is managing a complex state machine or a variety of different "plug-in" behaviors based on internal configuration codes (e.g., 0x2, 0x6, 0xf).

### Notable Techniques & Patterns
*   **Advanced Obfuscation of Logic:** The use of large switch tables and deeply nested loops (seen in `fcn.18000b070`) is designed to frustrate static analysis tools and make it difficult for a human analyst to follow the logic flow without dynamic debugging.
*   **Manual Buffer Management:** The code performs significant manual pointer arithmetic (`puVar6[puVar7 - iVar9]`, `puVar12 = iVar12 + 0x10`). This suggests it is interacting with raw memory structures rather than using standard high-level APIs, a hallmark of "hardened" malware.
*   **Dynamic Response Logic:** The function `fcn.18000ceec` (which interacts with `WriteFile`) contains complex checks for console modes and other environment variables, suggesting the malware adapts how it outputs or logs information based on whether it detects a terminal environment.

### Updated Conclusion
The inclusion of **cpuid-based hardware fingerprinting** confirms that this is not basic "script kiddie" malware; it has been engineered to evade sophisticated automated analysis systems (sandboxes). The combination of **automated file system scanning**, **locale-aware string handling**, and **complex buffer processing** reinforces its classification as a sophisticated information stealer or a multi-stage loader. It is designed to identify high-value data on the local machine while remaining "silent" in the presence of security researchers' tools.

### New Indicators of Compromise (IOC) / Tactics
*   **Technique:** Anti-Virtualization via `cpuid` feature checks.
*   **Technique:** File System Enumeration using `FindFirstFileExW`.
*   **Technique:** Manual memory buffer manipulation to evade simple signature detection.
*   **Targeting:** Likely targeting specific files or system information in a multi-lingual environment (via `GetCPInfo`).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualized Environment Detection | The malware uses `cpuid` instructions to check for specific hardware features and model IDs to determine if it is running in a sandbox or virtual machine. |
| **T1083** | File and Directory Discovery | The use of `FindFirstFileExW` and `FindNextFileW` indicates the malware is actively searching the file system for configuration files or sensitive user data. |
| **T1027** | Obfuscated Files or Packing | The use of complex nested loops, manual pointer arithmetic, and "packing" logic is designed to hide the true intent of the code and bypass static analysis tools. |
| **T1592** | Gather Related Information on Victim | The systematic collection and obfuscation of system information before transmission is used to profile the environment and identify high-value targets. |
| **T1071.001** | Application Layer Protocol: Web Protocols | The use of a "high-fidelity" User-Agent suggests an intent to blend in with legitimate web traffic during command and control (C2) communication. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `https://files.cab` (Extracted from the obfuscated string `https://files.cabE_NYEN_d[NE~YGjhZ]^zIIZBzXX^HH`)

**File paths / Registry keys**
*   *(None identified; standard Windows paths like C:\Windows\System32\ntdll.dll were excluded as per instructions.)*

**Mutex names / Named pipes**
*   *(None found)*

**Hashes**
*   *(None found in the provided text)*

**Other artifacts**
*   **User-Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36`
*   **Anti-Analysis Functions:** `cpuid_basic_info`, `cpuid_Version_info`, `cpuid_Extended_Feature_Enumeration_info` (Used for hardware fingerprinting and anti-virtualization).
*   **Persistence/Discovery API Calls:** `FindFirstFileExW`, `FindNextFileW` (Used for file system reconnaissance).
*   **Environment Check Logic:** `GetCPInfo` (Used for locale-aware string handling/data processing).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `https://files.cabE_NYEN_d[NE~YGjhZ`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: infostealer
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Data Exfiltration Path:** The combination of systematic file system reconnaissance (`FindFirstFileExW`), locale-aware string handling, and complex data serialization/buffer management strongly indicates the primary goal is to gather, package, and exfiltrate sensitive local data.
*   **Advanced Evasion Techniques:** The use of multiple `cpuid` instructions for hardware fingerprinting demonstrates a high level of engineering intended to bypass automated sandbox analysis and identify non-standard (virtualized) environments.
*   **Stealthy Communication Profile:** The use of a "high-fidelity" User-Agent string designed to mimic a standard Chrome browser, combined with the obfuscation of internal logic, points toward an intent to blend in with legitimate web traffic during data exfiltration.
