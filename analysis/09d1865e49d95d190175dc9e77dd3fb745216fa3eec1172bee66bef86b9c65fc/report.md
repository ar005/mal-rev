# Threat Analysis Report

**Generated:** 2026-07-23 15:46 UTC
**Sample:** `09d1865e49d95d190175dc9e77dd3fb745216fa3eec1172bee66bef86b9c65fc_09d1865e49d95d190175dc9e77dd3fb745216fa3eec1172bee66bef86b9c65fc.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `09d1865e49d95d190175dc9e77dd3fb745216fa3eec1172bee66bef86b9c65fc_09d1865e49d95d190175dc9e77dd3fb745216fa3eec1172bee66bef86b9c65fc.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 109,568 bytes |
| MD5 | `0df125c0bf80fff484b7aac57a5bb0ca` |
| SHA1 | `53cb2eaf53a080c4d3797301cabc777be6de9445` |
| SHA256 | `09d1865e49d95d190175dc9e77dd3fb745216fa3eec1172bee66bef86b9c65fc` |
| Overall entropy | 5.911 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768013515 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 57,344 | 6.423 | No |
| `.rdata` | 41,472 | 4.703 | No |
| `.data` | 3,072 | 2.073 | No |
| `.pdata` | 4,096 | 4.788 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.837 | No |

### Imports

**ole32.dll**: `CoInitializeEx`, `CoUninitialize`
**OLEAUT32.dll**: `SafeArrayCreate`, `SafeArrayDestroy`, `SafeArrayGetUBound`, `SafeArrayAccessData`, `SafeArrayUnaccessData`, `VariantClear`, `VariantInit`, `SafeArrayCreateVector`, `SafeArrayPutElement`
**USER32.dll**: `TranslateMessage`, `DispatchMessageA`, `GetMessageA`
**ADVAPI32.dll**: `GetUserNameA`
**KERNEL32.dll**: `CreateFileW`, `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleOutputCP`, `WriteConsoleW`, `FlushFileBuffers`, `SetStdHandle`, `HeapReAlloc`, `HeapSize`, `GetStringTypeW`, `GetFileType`, `WriteFile`, `FlsSetValue`, `CreateFileA`, `GetDiskFreeSpaceExA`

### Exports

`get_hostfxr_path`

## Extracted Strings

Total strings found: **447** (showing first 100)

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
@USATAUAWH
EHmsco
ELree.
PPD9l$h
A_A]A\[]
@USAUH
@USVWATAUAVAWH
@8}Lt,
A_A^A]A\_^[]
D$Hbin
t}HcH<E3
|$ AVH
A:8ufI
tcA88uVI
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
f9<H}
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
@UATAUAVAWH
A_A^A]A\]
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.18000672c` | `0x18000672c` | 14715 | ✓ |
| `fcn.1800066f4` | `0x1800066f4` | 14710 | ✓ |
| `fcn.180002adc` | `0x180002adc` | 12443 | ✓ |
| `fcn.1800029dc` | `0x1800029dc` | 2846 | ✓ |
| `fcn.180002b6c` | `0x180002b6c` | 2568 | ✓ |
| `fcn.1800086e8` | `0x1800086e8` | 1829 | ✓ |
| `fcn.18000e040` | `0x18000e040` | 1677 | ✓ |
| `fcn.180001b90` | `0x180001b90` | 1514 | ✓ |
| `fcn.1800012c0` | `0x1800012c0` | 1392 | ✓ |
| `fcn.1800043e8` | `0x1800043e8` | 1213 | ✓ |
| `fcn.18000c818` | `0x18000c818` | 1171 | ✓ |
| `fcn.18000bdf0` | `0x18000bdf0` | 922 | ✓ |
| `fcn.18000e6f0` | `0x18000e6f0` | 920 | ✓ |
| `fcn.18000b880` | `0x18000b880` | 920 | ✓ |
| `fcn.1800025a0` | `0x1800025a0` | 892 | ✓ |
| `fcn.180008388` | `0x180008388` | 862 | ✓ |
| `fcn.180006afc` | `0x180006afc` | 817 | ✓ |
| `fcn.18000d164` | `0x18000d164` | 815 | ✓ |
| `fcn.180001830` | `0x180001830` | 753 | ✓ |
| `fcn.1800091b4` | `0x1800091b4` | 712 | ✓ |
| `section..text` | `0x180001000` | 689 | ✓ |
| `fcn.180002dc8` | `0x180002dc8` | 667 | ✓ |
| `fcn.180008e10` | `0x180008e10` | 623 | ✓ |
| `fcn.18000a244` | `0x18000a244` | 604 | ✓ |
| `fcn.1800063fc` | `0x1800063fc` | 589 | ✓ |
| `fcn.1800048a8` | `0x1800048a8` | 584 | ✓ |
| `fcn.180004e48` | `0x180004e48` | 557 | ✓ |
| `fcn.18000afa8` | `0x18000afa8` | 555 | ✓ |
| `fcn.1800032a0` | `0x1800032a0` | 517 | ✓ |
| `fcn.180003098` | `0x180003098` | 509 | ✓ |

### Decompiled Code Files

- [`code/fcn.1800012c0.c`](code/fcn.1800012c0.c)
- [`code/fcn.180001830.c`](code/fcn.180001830.c)
- [`code/fcn.180001b90.c`](code/fcn.180001b90.c)
- [`code/fcn.1800025a0.c`](code/fcn.1800025a0.c)
- [`code/fcn.1800029dc.c`](code/fcn.1800029dc.c)
- [`code/fcn.180002adc.c`](code/fcn.180002adc.c)
- [`code/fcn.180002b6c.c`](code/fcn.180002b6c.c)
- [`code/fcn.180002dc8.c`](code/fcn.180002dc8.c)
- [`code/fcn.180003098.c`](code/fcn.180003098.c)
- [`code/fcn.1800032a0.c`](code/fcn.1800032a0.c)
- [`code/fcn.1800043e8.c`](code/fcn.1800043e8.c)
- [`code/fcn.1800048a8.c`](code/fcn.1800048a8.c)
- [`code/fcn.180004e48.c`](code/fcn.180004e48.c)
- [`code/fcn.1800063fc.c`](code/fcn.1800063fc.c)
- [`code/fcn.1800066f4.c`](code/fcn.1800066f4.c)
- [`code/fcn.18000672c.c`](code/fcn.18000672c.c)
- [`code/fcn.180006afc.c`](code/fcn.180006afc.c)
- [`code/fcn.180008388.c`](code/fcn.180008388.c)
- [`code/fcn.1800086e8.c`](code/fcn.1800086e8.c)
- [`code/fcn.180008e10.c`](code/fcn.180008e10.c)
- [`code/fcn.1800091b4.c`](code/fcn.1800091b4.c)
- [`code/fcn.18000a244.c`](code/fcn.18000a244.c)
- [`code/fcn.18000afa8.c`](code/fcn.18000afa8.c)
- [`code/fcn.18000b880.c`](code/fcn.18000b880.c)
- [`code/fcn.18000bdf0.c`](code/fcn.18000bdf0.c)
- [`code/fcn.18000c818.c`](code/fcn.18000c818.c)
- [`code/fcn.18000d164.c`](code/fcn.18000d164.c)
- [`code/fcn.18000e040.c`](code/fcn.18000e040.c)
- [`code/fcn.18000e6f0.c`](code/fcn.18000e6f0.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

Based on the additional disassembly in chunk 2, I have updated the analysis. The inclusion of these functions confirms several advanced techniques typically found in high-end modular malware (such as those used by APT groups or sophisticated Trojan families).

### Updated Analysis Summary

The binary remains a **sophisticated multi-stage loader**. The addition of this data reveals that the malware employs highly complex internal logic to handle "state" transitions, protects its core strings through custom comparison algorithms, and likely masquerades legitimate traffic or processes.

---

### New Findings & Expanded Analysis

#### 1. Advanced String Obfuscation and Custom Comparison
*   **Function `fcn.180003098`**: This is a classic example of **manual string hashing/comparison**. Instead of using standard library functions like `strcmp`, the code uses complex bitmasking, manual pointer arithmetic, and "SIMD-like" logic (using `pcmpi` style comparisons) to check strings. 
*   **Purpose:** By avoiding standard C libraries for string comparison, the malware evades automated heuristic scanners that flag common API calls during the search/validation of configuration data or internal commands.

#### 2. Dynamic API Resolution & Obfuscation
*   **Function `fcn.180001830`**: This routine is a dedicated **"unpacking" engine for its own imports**. It uses XOR-based decryption loops (e.g., `0x7077706e ^ 0x19`) to decrypt strings in memory before passing them to `GetProcAddress`.
*   **Detection of Masquerading:** The disassembly shows the construction of a **Mozilla/5.0 User-Agent string**. This strongly suggests that the loader is designed to perform network communications (HTTP/HTTPS) while masquerading as a legitimate web browser, making its C2 traffic harder to distinguish from normal user activity.

#### 3. State Machine & Context Handling
*   **Functions `fcn.1800032a0` and `fcn.18000fa8`**: These functions indicate the presence of a **complex internal state machine**. The use of `RtlUnwindEx` (an internal Windows API often used for exception handling or thread context switching) suggests that the malware manages its own execution flow across different "stages" or "modules" internally.
*   **Concurrency/Safety:** The frequent use of `LOCK()` and `UNLOCK()` macros around state updates indicates a multi-threaded design, where the loader may be managing several tasks (e.g., heartbeat to C2, payload decryption, and anti-analysis loops) simultaneously.

#### 4. Integrity & Validation Logic
*   **Function `fcn.180004e48`**: This appears to be a **"Gatekeeper" routine**. It performs multiple checks on the "next" stage of code (using magic numbers like `-0x1f928c9d`) before allowing execution to proceed.
*   **Purpose:** It ensures that the data injected into memory has been correctly decrypted and hasn't been tampered with by security software or debuggers before it is executed as the final payload.

---

### Updated Technical Indicators of Compromise (IOCs) Logic

| Feature | Technical Observation | Threat Significance |
| :--- | :--- | :--- |
| **API Obfuscation** | XOR loops + `GetProcAddress` for core functions. | Hides functionality from static IAT analysis; indicates a professional-grade loader. |
| **Anti-Analysis** | Custom string comparison (no `strcmp`). | Evades heuristic/signature detection of common API calls during config parsing. |
| **Evasion Tactics** | Inclusion of "Mozilla" User-Agent strings. | Intentional masquerading of C2 traffic as legitimate web browsing. |
| **Execution Flow** | Use of `RtlUnwindEx` and state machine logic. | Suggests a modular architecture where multiple payloads can be swapped or managed in one process. |
| **Memory Protection** | Post-decryption "Gatekeeper" checks. | Prevents the execution of corrupted/modified payload segments, ensuring only "clean" malware runs. |

### Summary for Incident Response (Updated)
The inclusion of chunk 2 confirms this is not a simple downloader but a **sophisticated modular loader**. Its use of `RtlUnwindEx` and complex state management suggests it can host multiple functionalities or modules once successfully deployed. The presence of the Mozilla User-Agent string indicates that network forensics should look for HTTP traffic mimicking standard browser headers. Because the malware validates the "integrity" of its next stages before execution, forensic memory analysis should focus on identifying the specific point where the "Gatekeeper" (fcn.180004e48) allows the jump to the primary malicious payload.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in the technical analysis to the relevant MITRE ATT&K techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The malware utilizes custom bitmasking, manual pointer arithmetic for string comparison, and XOR-based loops to hide its logic and configuration from automated scanners. |
| **T1036** | Masquerading | The inclusion of a "Mozilla/5.0" User-Agent string is used to disguise malicious C2 communications as legitimate web browser traffic. |
| **T1497** | Virtualization/Sandbox Evasion | The "Gatekeeper" routine (fcn.180004e48) serves as an anti-analysis check to ensure the payload has not been tampered with by debuggers or security software before execution. |
| **T1568** | Dynamic Resolution | The use of `GetProcAddress` combined with decrypted strings indicates a modular approach to resolve API calls at runtime, hindering static analysis. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have extracted and categorized the relevant Indicators of Compromise (IOCs) from the provided data. 

Note: Standard system files (e.g., `ntdll.dll`) and standard compiler symbols (e.g., `__stdcall`) have been excluded as per your instructions to skip false positives.

### **IP addresses / URLs / Domains**
*   **URL:** `https://files.ca` (Embedded within a complex string: `tbox.moe/0xmk32.dCYH_CHYnAB^HeLCeBXI^BIX~IMHjE@Ihttps://files.ca`)

### **File paths / Registry keys**
*   *(No specific non-standard file paths or registry keys were identified.)*

### **Mutex names / Named pipes**
*   *(None identified.)*

### **Hashes**
*   *(No standard MD5, SHA1, or SHA256 hashes were present in the provided strings.)*

### **Other artifacts**
*   **User-Agent String:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64)` (Used to mask C2 traffic as legitimate web browsing).
*   **Anti-Analysis / Sandbox Detection Strings:** 
    *   `sandbox`
    *   `malware`
    *   `cuckoo`
    *   `cuckoosandbox`
    *   `wilbert`
    *   `hapubws`
    *   `systemit`
    *   `bea-vr`
    *   `sample`
    *   `analysis`
*   **Analysis Tool Detection (Known Security Tools):**
    *   `x64dbg`
    *   `x32dbg`
    *   `ollydbg`
    *   `windbg`
    *   `ida.exe`
    *   `processhacker`
    *   `fiddler`
    *   `wireshark`
    *   `procmon`
    *   `apimonitor`
    *   `pestudio`
*   **Specific Library/Module Checks:** 
    *   `vmcheck.dll` (Indicates VM detection)
    *   `cuckoomon.dll` (Cuckoo sandbox monitoring)
    *   `snxhk.dll`
    *   `cmdvrt32.dll`
    *   `sbiedll.dll`
    *   `api_log.dll`
    *   `dir_watch.dll`
    *   `pstorec.dll`
    *   `SxIn.dll`
    *   `Sf2.dll`

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `https://files.caCLRCreateInstancbE_NYEN_d[NE~YGj`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Modular Architecture:** The use of complex state machines, `RtlUnwindEx` for context management, and "Gatekeeper" integrity checks indicates a sophisticated multi-stage loader designed to host and manage various payloads (e.g., RATs or miners) while maintaining execution flow.
*   **Professional Obfuscation & Evasion:** The malware avoids standard libraries for string comparison, utilizes XOR-based dynamic API resolution, and employs "Mozilla/5.0" User-Agent strings to mask its C2 communications as legitimate web traffic.
*   **Robust Anti-Analysis Suite:** The identification of numerous anti-debugging (x64dbg, IDA) and anti-sandbox (Cuckoo, QEMU indicators) strings confirms it is a high-end protection layer designed to evade both automated security systems and manual forensic analysis.
