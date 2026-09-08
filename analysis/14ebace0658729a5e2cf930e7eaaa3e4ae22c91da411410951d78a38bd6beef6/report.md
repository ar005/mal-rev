# Threat Analysis Report

**Generated:** 2026-09-06 12:52 UTC
**Sample:** `14ebace0658729a5e2cf930e7eaaa3e4ae22c91da411410951d78a38bd6beef6_14ebace0658729a5e2cf930e7eaaa3e4ae22c91da411410951d78a38bd6beef6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14ebace0658729a5e2cf930e7eaaa3e4ae22c91da411410951d78a38bd6beef6_14ebace0658729a5e2cf930e7eaaa3e4ae22c91da411410951d78a38bd6beef6.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 22,219,264 bytes |
| MD5 | `e0c485160c3f2bdcc8024c3843436e9f` |
| SHA1 | `bf446b2d3bf640b219e703496e99c9d9f70a4b0f` |
| SHA256 | `14ebace0658729a5e2cf930e7eaaa3e4ae22c91da411410951d78a38bd6beef6` |
| Overall entropy | 7.822 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769638519 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 50,688 | 6.423 | No |
| `.rdata` | 38,912 | 4.679 | No |
| `.data` | 21,929,984 | 7.843 | ⚠️ Yes |
| `.pdata` | 4,096 | 4.38 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 192,000 | 2.224 | No |
| `.reloc` | 2,048 | 4.859 | No |

### Imports

**SHELL32.dll**: `SHGetFolderPathW`, `ShellExecuteW`
**KERNEL32.dll**: `RtlVirtualUnwind`, `WriteConsoleW`, `WriteFile`, `CreateFileW`, `SetFileAttributesW`, `lstrcatW`, `CloseHandle`, `GetCurrentDirectoryW`, `lstrcpyW`, `QueryPerformanceCounter`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetSystemTimeAsFileTime`, `InitializeSListHead`, `SetUnhandledExceptionFilter`

## Extracted Strings

Total strings found: **68573** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
u0HcH<
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
tfD9y
UVWAVAWH
H9:tH
0A_A^_^]
WAVAWH
fA9,@u
fA9,vu
0A_A^_
u3HcH<H
WAVAWH
 A_A^_
WAVAWH
L3
H3B
 A_A^_
D$0u3
\$8t	H
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
K0H;z
K8H;p
K@H;f
KHH;\
KhH;j
KpH;`
KxH;V
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
| `fcn.140005948` | `0x140005948` | 14907 | ✓ |
| `fcn.140005934` | `0x140005934` | 14866 | ✓ |
| `section..text` | `0x140001000` | 2135 | ✓ |
| `fcn.14000c9f0` | `0x14000c9f0` | 1677 | ✓ |
| `fcn.140006fa0` | `0x140006fa0` | 1577 | ✓ |
| `fcn.140001ae0` | `0x140001ae0` | 1308 | ✓ |
| `fcn.14000337c` | `0x14000337c` | 1213 | ✓ |
| `fcn.14000ad4c` | `0x14000ad4c` | 1171 | ✓ |
| `fcn.14000c630` | `0x14000c630` | 920 | ✓ |
| `fcn.14000a2d0` | `0x14000a2d0` | 920 | ✓ |
| `fcn.14000a668` | `0x14000a668` | 817 | ✓ |
| `fcn.14000b698` | `0x14000b698` | 815 | ✓ |
| `fcn.14000782c` | `0x14000782c` | 712 | ✓ |
| `fcn.140001ffc` | `0x140001ffc` | 667 | ✓ |
| `fcn.140007488` | `0x140007488` | 623 | ✓ |
| `fcn.140009524` | `0x140009524` | 604 | ✓ |
| `fcn.140004ea4` | `0x140004ea4` | 597 | ✓ |
| `fcn.14000383c` | `0x14000383c` | 584 | ✓ |
| `fcn.140003ddc` | `0x140003ddc` | 557 | ✓ |
| `fcn.140008948` | `0x140008948` | 555 | ✓ |
| `fcn.1400022b0` | `0x1400022b0` | 517 | ✓ |
| `fcn.140007290` | `0x140007290` | 501 | ✓ |
| `fcn.140002ff0` | `0x140002ff0` | 499 | ✓ |
| `fcn.140006fa8` | `0x140006fa8` | 462 | ✓ |
| `fcn.140009ee4` | `0x140009ee4` | 445 | ✓ |
| `fcn.14000a0ec` | `0x14000a0ec` | 437 | ✓ |
| `fcn.140008d54` | `0x140008d54` | 434 | ✓ |
| `fcn.14000547c` | `0x14000547c` | 430 | ✓ |
| `fcn.1400048d4` | `0x1400048d4` | 418 | ✓ |
| `fcn.1400051fc` | `0x1400051fc` | 413 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001ae0.c`](code/fcn.140001ae0.c)
- [`code/fcn.140001ffc.c`](code/fcn.140001ffc.c)
- [`code/fcn.1400022b0.c`](code/fcn.1400022b0.c)
- [`code/fcn.140002ff0.c`](code/fcn.140002ff0.c)
- [`code/fcn.14000337c.c`](code/fcn.14000337c.c)
- [`code/fcn.14000383c.c`](code/fcn.14000383c.c)
- [`code/fcn.140003ddc.c`](code/fcn.140003ddc.c)
- [`code/fcn.1400048d4.c`](code/fcn.1400048d4.c)
- [`code/fcn.140004ea4.c`](code/fcn.140004ea4.c)
- [`code/fcn.1400051fc.c`](code/fcn.1400051fc.c)
- [`code/fcn.14000547c.c`](code/fcn.14000547c.c)
- [`code/fcn.140005934.c`](code/fcn.140005934.c)
- [`code/fcn.140005948.c`](code/fcn.140005948.c)
- [`code/fcn.140006fa0.c`](code/fcn.140006fa0.c)
- [`code/fcn.140006fa8.c`](code/fcn.140006fa8.c)
- [`code/fcn.140007290.c`](code/fcn.140007290.c)
- [`code/fcn.140007488.c`](code/fcn.140007488.c)
- [`code/fcn.14000782c.c`](code/fcn.14000782c.c)
- [`code/fcn.140008948.c`](code/fcn.140008948.c)
- [`code/fcn.140008d54.c`](code/fcn.140008d54.c)
- [`code/fcn.140009524.c`](code/fcn.140009524.c)
- [`code/fcn.140009ee4.c`](code/fcn.140009ee4.c)
- [`code/fcn.14000a0ec.c`](code/fcn.14000a0ec.c)
- [`code/fcn.14000a2d0.c`](code/fcn.14000a2d0.c)
- [`code/fcn.14000a668.c`](code/fcn.14000a668.c)
- [`code/fcn.14000ad4c.c`](code/fcn.14000ad4c.c)
- [`code/fcn.14000b698.c`](code/fcn.14000b698.c)
- [`code/fcn.14000c630.c`](code/fcn.14000c630.c)
- [`code/fcn.14000c9f0.c`](code/fcn.14000c9f0.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated the analysis. The new code reveals significant advancements in the sophistication of the malware, specifically regarding **multi-threading**, **API obfuscation**, and **advanced string processing**.

Here is the updated analysis:

### Updated Core Functionality and Purpose
The binary remains a **sophisticated multi-stage loader/dropper**. However, the second chunk of code reveals that it isn't just a simple "drop and run" script; it contains internal infrastructure to manage complex operations, handle multiple concurrent tasks, and dynamically resolve system functions to evade detection.

### New Suspicious Behaviors Identified
*   **Dynamic API Resolution & Obfuscation:** 
    The function `fcn.140008d54` specifically implements a mechanism to call `LoadLibraryExW` and `GetProcAddress`. This is a classic technique used by malware to hide its true capabilities from static analysis. By resolving functions at runtime rather than listing them in the Import Address Table (IAT), the author hides which system functions (e.g., for networking, keylogging, or file manipulation) are being called.
*   **Memory Manipulation (VirtualProtect):** 
    In `fcn.140008d54`, the malware calls `VirtualProtect`. This is often used to change the permissions of a memory region (e.g., from "Read/Write" to "Execute"). In this context, it likely prepares a space in memory where one of the dropped payloads or an injected module will be executed.
*   **Multi-Threaded Execution:** 
    The repeated use of `LOCK()` and `UNLOCK()` macros (found in `fcn.140008948` and `fcn.140006fa8`) confirms that the malware utilizes **multi-threading**. This allows the malware to perform several tasks simultaneously, such as maintaining a connection to a Command & Control (C2) server while scanning for files or executing multiple components of its "arsenal" at once.
*   **Sophisticated String Processing Engine:** 
    The functions `fcn.140007290`, `fcn.140009ee4`, and `fcn.14000a0ec` contain complex logic for handling strings. This isn't just standard string concatenation; it appears to be a custom engine for handling various encodings (like UTF-8 or Unicode) and potentially decoding obfuscated data "on the fly." This suggests that many of the strings used by the malware—such as C2 URLs, IP addresses, and commands—are likely encrypted/encoded in the binary's memory.

### Updated Notable Techniques and Patterns
*   **Advanced Unpacking Logic:** The combination of `VirtualProtect` and `GetProcAddress` strongly suggests a "packer" or "loader" architecture where the primary functionality is hidden behind layers of obfuscation that only unpack during execution.
*   **Robust State Management:** Functions like `fcn.140006fa8` involve copying blocks of data while maintaining internal counters and state flags. This indicates the malware handles complex data structures, likely to manage its various stages of infection or communication protocols.
*   **Fallback Mechanisms:** The code includes several "if-else" chains that check for specific conditions before falling back to alternative functions (e.g., in `fcn.140008d54`). This is a common technique to ensure the malware remains functional even if certain system environment variables or protections are active.

### Updated Summary of Findings
The binary is a **highly sophisticated, multi-threaded dropper and loader**. It serves as the primary entry point for a complex malware suite. 

**Key technical highlights from the expanded analysis:**
1.  **Evasion Layer:** It uses dynamic API resolution to hide its interactions with the Windows OS.
2.  **Persistence of Activity:** The use of multi-threading suggests it can perform multiple malicious actions simultaneously without alerting the user or system monitors through high CPU spikes on a single thread.
3.  **Hidden Configuration:** The complex string processing routines suggest that the "true" configuration (C2 details, target list) is heavily encoded and only decoded in memory during runtime.
4.  **Payload Delivery:** It continues to exhibit the behavior of unpacking/dropping multiple executables, but it now is clear that those payloads are supported by a robust internal architecture designed for stealth and reliability.

**Conclusion:** This is not a "script kiddie" tool; it is a professional-grade piece of malware intended to bypass both automated security scanners and manual forensic analysis through layers of obfuscation and sophisticated coding practices.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of dynamic API resolution (via `GetProcAddress`) and a custom string processing engine masks critical information such as C2 infrastructure and system interactions from static analysis. |
| T1055 | Process Injection | The utilization of `VirtualProtect` to modify memory permissions indicates the malware is preparing an environment to execute unpacked payloads or injected modules in-memory. |
| T1106 | Fileless | The sophisticated "loader" architecture, characterized by dynamic resolution and memory manipulation, suggests a design intended to execute malicious code without leaving traditional artifacts on disk. |

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The "Extracted Strings" section contains a significant amount of obfuscated binary data and standard compiler library strings. No explicit IP addresses, URLs, or file hashes were found in the raw text; however, several technical indicators regarding the malware's behavior were identified.

### **IP addresses / URLs / Domains**
*   *None identified.* (The report notes that C2 infrastructure is likely encrypted/encoded and only decoded in memory during runtime).

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (Behavioral Indicators & Evidence of Malignancy)**
*   **Dynamic API Resolution:** Use of `LoadLibraryExW` and `GetProcAddress` to hide imports from the IAT (Import Address Table).
*   **Memory Manipulation:** Usage of `VirtualProtect` to change memory permissions (e.g., transitioning regions from Read/Write to Execute) for payload execution.
*   **Multi-threading Activity:** Implementation of `LOCK()` and `UNLOCK()` macros to manage concurrent operations (facilitating background C2 communication and file processing).
*   **Sophisticated String Processing Engine:** Custom routines identified at `fcn.140007290`, `fcn.140009ee4`, and `fcn.14000a0ec` for handling obfuscated/encoded data (likely used to hide C2 commands).
*   **Evasion Techniques:** Implementation of "fall-back" logic in code blocks to bypass environmental checks or security software detections.

---

## Malware Family Classification

**Malware classification:**

1. **Malware family:** custom
2. **Malware type:** loader / dropper
3. **Confidence:** High
4. **Key evidence:**
    * **Advanced Evasion Techniques:** The use of dynamic API resolution (`GetProcAddress`, `LoadLibraryExW`) combined with `VirtualProtect` memory manipulation indicates a sophisticated multi-stage architecture designed to hide functionality from static analysis and execute payloads in-memory (fileless behavior).
    * **Sophisticated Infrastructure:** The presence of custom string processing engines, multi-threading capabilities, and "fall-back" logic confirms this is not a basic script but a professional-grade tool built for persistence and stealth.
    * **Payload Delivery Focus:** The analysis explicitly identifies the binary as a primary entry point designed to unpack/drop additional executables while hiding its own configuration (C2 details) until runtime.
