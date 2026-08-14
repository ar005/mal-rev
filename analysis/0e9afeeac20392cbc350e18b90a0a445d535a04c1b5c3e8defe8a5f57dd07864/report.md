# Threat Analysis Report

**Generated:** 2026-08-13 17:03 UTC
**Sample:** `0e9afeeac20392cbc350e18b90a0a445d535a04c1b5c3e8defe8a5f57dd07864_0e9afeeac20392cbc350e18b90a0a445d535a04c1b5c3e8defe8a5f57dd07864.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e9afeeac20392cbc350e18b90a0a445d535a04c1b5c3e8defe8a5f57dd07864_0e9afeeac20392cbc350e18b90a0a445d535a04c1b5c3e8defe8a5f57dd07864.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 5,372,928 bytes |
| MD5 | `f44dc980f7a8d900bd1b73a0b00bd19a` |
| SHA1 | `40cda7ff3ea1aa75a53693bbf3205dcc162288e8` |
| SHA256 | `0e9afeeac20392cbc350e18b90a0a445d535a04c1b5c3e8defe8a5f57dd07864` |
| Overall entropy | 7.282 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769463973 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 49,664 | 6.419 | No |
| `.rdata` | 38,912 | 4.666 | No |
| `.data` | 4,905,472 | 7.437 | ⚠️ Yes |
| `.pdata` | 4,096 | 4.405 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 371,200 | 4.295 | No |
| `.reloc` | 2,048 | 4.86 | No |

### Imports

**SHELL32.dll**: `SHGetFolderPathW`, `ShellExecuteW`
**KERNEL32.dll**: `RtlVirtualUnwind`, `WriteConsoleW`, `WriteFile`, `CreateFileW`, `SetFileAttributesW`, `lstrcatW`, `CloseHandle`, `GetCurrentDirectoryW`, `lstrcpyW`, `QueryPerformanceCounter`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetSystemTimeAsFileTime`, `InitializeSListHead`, `SetUnhandledExceptionFilter`

## Extracted Strings

Total strings found: **19605** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
uxHc|
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
WAVAWH
 A_A^_
UVWATAUAVAWH
A8z(uI
fB9<I}1L
A_A^A]A\_^]
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400055e8` | `0x1400055e8` | 14907 | ✓ |
| `fcn.1400055d4` | `0x1400055d4` | 14866 | ✓ |
| `fcn.14000c690` | `0x14000c690` | 1677 | ✓ |
| `fcn.140006c40` | `0x140006c40` | 1577 | ✓ |
| `fcn.140001780` | `0x140001780` | 1308 | ✓ |
| `section..text` | `0x140001000` | 1280 | ✓ |
| `fcn.14000301c` | `0x14000301c` | 1213 | ✓ |
| `fcn.14000a9ec` | `0x14000a9ec` | 1171 | ✓ |
| `fcn.14000c2d0` | `0x14000c2d0` | 920 | ✓ |
| `fcn.140009f70` | `0x140009f70` | 920 | ✓ |
| `fcn.14000a308` | `0x14000a308` | 817 | ✓ |
| `fcn.14000b338` | `0x14000b338` | 815 | ✓ |
| `fcn.1400074cc` | `0x1400074cc` | 712 | ✓ |
| `fcn.140001c9c` | `0x140001c9c` | 667 | ✓ |
| `fcn.140007128` | `0x140007128` | 623 | ✓ |
| `fcn.1400091c4` | `0x1400091c4` | 604 | ✓ |
| `fcn.140004b44` | `0x140004b44` | 597 | ✓ |
| `fcn.1400034dc` | `0x1400034dc` | 584 | ✓ |
| `fcn.140003a7c` | `0x140003a7c` | 557 | ✓ |
| `fcn.1400085e8` | `0x1400085e8` | 555 | ✓ |
| `fcn.140001f50` | `0x140001f50` | 517 | ✓ |
| `fcn.140006f30` | `0x140006f30` | 501 | ✓ |
| `fcn.140002c90` | `0x140002c90` | 499 | ✓ |
| `fcn.140006c48` | `0x140006c48` | 462 | ✓ |
| `fcn.140009b84` | `0x140009b84` | 445 | ✓ |
| `fcn.140009d8c` | `0x140009d8c` | 437 | ✓ |
| `fcn.1400089f4` | `0x1400089f4` | 434 | ✓ |
| `fcn.14000511c` | `0x14000511c` | 430 | ✓ |
| `fcn.140004574` | `0x140004574` | 418 | ✓ |
| `fcn.140004e9c` | `0x140004e9c` | 413 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001780.c`](code/fcn.140001780.c)
- [`code/fcn.140001c9c.c`](code/fcn.140001c9c.c)
- [`code/fcn.140001f50.c`](code/fcn.140001f50.c)
- [`code/fcn.140002c90.c`](code/fcn.140002c90.c)
- [`code/fcn.14000301c.c`](code/fcn.14000301c.c)
- [`code/fcn.1400034dc.c`](code/fcn.1400034dc.c)
- [`code/fcn.140003a7c.c`](code/fcn.140003a7c.c)
- [`code/fcn.140004574.c`](code/fcn.140004574.c)
- [`code/fcn.140004b44.c`](code/fcn.140004b44.c)
- [`code/fcn.140004e9c.c`](code/fcn.140004e9c.c)
- [`code/fcn.14000511c.c`](code/fcn.14000511c.c)
- [`code/fcn.1400055d4.c`](code/fcn.1400055d4.c)
- [`code/fcn.1400055e8.c`](code/fcn.1400055e8.c)
- [`code/fcn.140006c40.c`](code/fcn.140006c40.c)
- [`code/fcn.140006c48.c`](code/fcn.140006c48.c)
- [`code/fcn.140006f30.c`](code/fcn.140006f30.c)
- [`code/fcn.140007128.c`](code/fcn.140007128.c)
- [`code/fcn.1400074cc.c`](code/fcn.1400074cc.c)
- [`code/fcn.1400085e8.c`](code/fcn.1400085e8.c)
- [`code/fcn.1400089f4.c`](code/fcn.1400089f4.c)
- [`code/fcn.1400091c4.c`](code/fcn.1400091c4.c)
- [`code/fcn.140009b84.c`](code/fcn.140009b84.c)
- [`code/fcn.140009d8c.c`](code/fcn.140009d8c.c)
- [`code/fcn.140009f70.c`](code/fcn.140009f70.c)
- [`code/fcn.14000a308.c`](code/fcn.14000a308.c)
- [`code/fcn.14000a9ec.c`](code/fcn.14000a9ec.c)
- [`code/fcn.14000b338.c`](code/fcn.14000b338.c)
- [`code/fcn.14000c2d0.c`](code/fcn.14000c2d0.c)
- [`code/fcn.14000c690.c`](code/fcn.14000c690.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated the analysis. The presence of these specific functions confirms that the binary is not just a simple dropper, but an **obfuscated multi-stage loader** utilizing advanced techniques to hide its intent from static analysis and automated security tools.

### Updated Analysis of Core Functionality
The second chunk reveals several sophisticated "under-the-hood" mechanisms used by the malware:

*   **Dynamic API Resolution:** The function `fcn.1400089f4` is a custom implementation for resolving functions from system libraries (like `Kernel32.dll`). By manually finding addresses of functions rather than using the standard Import Address Table (IAT), the malware hides its intended capabilities (e.g., networking, file manipulation) from static analysis tools.
*   **Advanced String Decryption:** The functions `fcn.140009b84` and `fcn.140009d8c` suggest a multi-layered approach to handling strings. They appear to handle Unicode/UTF-16 conversions and potentially decode obfuscated paths or commands at runtime. This ensures that malicious URLs, file paths, or registry keys remain hidden until the moment they are needed.
*   **Memory Integrity & Manipulation:** The use of `VirtualProtect` in `fcn.1400089f4` indicates the malware is changing memory permissions (likely from Read/Write to Execute). This is a classic sign of **in-memory unpacking**, where a hidden payload is decrypted and executed directly in RAM to avoid leaving traces on the disk until it is too late for simple scanners.
*   **Complex Execution Branching:** The frequent use of `swi(3)` (Software Interrupts) as jump targets suggests that the code is structured into "blocks." This makes it difficult for a disassembler to follow the logical flow of the program, as the next step in execution isn't always the next line of code.

### Expanded Suspicious and Malicious Behaviors
*   **Evasion of Static Analysis:** By using `fcn.1400089f4` to resolve imports at runtime, the malware hides its "behavioral signature." A researcher looking only at the file's headers won't see the calls it makes to system APIs.
*   **Runtime De-obfuscation:** The complex logic in `fcn.14000511c` and `fcn.140004574` suggests that much of the "intelligence" (the specific commands or targets) is encrypted while stored on disk and only decrypted in memory during execution.
*   **Multi-Stage Execution Hand-off:** The function `fcn.140004e9c` acts as a gateway. It performs checks and then uses interrupts to jump to the next stage of the infection chain, ensuring that even if one "block" is flagged by an automated sandbox, the others may still execute.

### Updated Technical Indicators
| Feature | Detail & Significance |
| :--- | :--- |
| **Dynamic API Resolution** | Uses custom `GetProcAddress` wrappers to hide calls to system APIs (e.g., networking or process injection). |
| **Memory Manipulation** | Employs `VirtualProtect` to modify memory permissions, a hallmark of unpacking and execution of hidden payloads. |
| **String Obfuscation** | Multi-stage decoding for strings/paths; prevents signature-based detection of URLs and file paths. |
| **Anti-Analysis (Flow)** | Use of Software Interrupts (`swi`) to break the linear flow of the code, confusing automated analysis tools. |
| **Complex Parsing** | Robust logic in `fcn.140009d8c` suggests it handles complex paths/configurations for its subsequent stages. |

### Final Summary Table (Updated)
| Category | Findings |
| :--- | :--- |
| **Primary Role** | Sophisticated Multi-stage Dropper & Unpacker |
| **Dropped Files** | `ivlnbis.exe`, `syncappk.exe`, `bnciobys.exe`, `ponbyxs.exe`, `MEGA-CRIMSON_BRUTE.exe` |
| **Evasion Techniques** | Dynamic API Resolution, Memory Protection Manipulation, String Obfuscation |
| **Anti-Analysis** | Software Interrupts (`swi`), potential "trap" logic in code branching |
| **Threat Profile** | High. The complexity suggests a professional malware development style aimed at evading enterprise-grade EDR (Endpoint Detection and Response) systems. |

### Conclusion for the Final Report:
The binary is a highly sophisticated loader designed to deliver multiple pieces of malware while actively defending itself against analysis. It utilizes **dynamic API resolution** to hide its capabilities, **memory manipulation** to execute hidden payloads, and **complex string obfuscation** to hide its communication infrastructure. The naming convention of the dropped files (`ivlnbis`, `bnciobys`) combined with these advanced evasion techniques strongly indicates a targeted or professional-grade malware campaign.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided analysis to the relevant MITRE ATT&CK techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of dynamic API resolution and multi-layered string decryption (Unicode/UTF-16) is designed to hide malicious capabilities, URLs, and file paths from static analysis. |
| **T1055** | Process Injection | The use of `VirtualProtect` to change memory permissions from Read/Write to Execute indicates the execution of unpacked payloads directly in memory to evade disk-based detection. |
| **T1027** | Obfuscated Files or Information | The utilization of Software Interrupts (`swi`) to break linear code flow is a specific obfuscation technique used to hinder automated analysis and manual disassembly. |

### Analyst Notes:
*   **Dynamic API Resolution (T1027):** By bypassing the Import Address Table (IAT) and using custom `GetProcAddress` wrappers, the malware successfully masks its interaction with system APIs (e.g., networking or file manipulation).
*   **Memory Manipulation (T1055):** While T1055 is often associated with injecting into *remote* processes, it is the standard mapping for any behavior involving `VirtualProtect` to facilitate the execution of "hidden" code segments within a process's memory space.
*   **Obfuscation Logic:** The complexity of the decoding functions and the non-linear execution paths suggest a high level of sophistication aimed at defeating both automated sandboxes and human reverse engineers.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified (Note: The report indicates these are heavily obfuscated/encrypted until runtime).

**File paths / Registry keys**
*   *Dropped Files:*
    *   `ivlnbis.exe`
    *   `syncappk.exe`
    *   `bnciobys.exe`
    *   `ponbyxs.exe`
    *   `MEGA-CRIMSON_BRUTE.exe`

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified (Note: Function addresses like `fcn.1400089f4` were identified, but these are internal memory offsets rather than file hashes).

**Other artifacts**
*   **Evasion Techniques:** 
    *   Dynamic API Resolution (Custom `GetProcAddress` wrappers)
    *   Memory Manipulation via `VirtualProtect` (Used for in-memory unpacking/execution)
    *   Software Interrupts (`swi(3)`): Used to break linear execution flow and evade automated analysis.
*   **Behavioral Patterns:**
    *   Multi-stage loader logic.
    *   Automated string decoding for Unicode/UTF-16 conversion of hidden paths/commands.

---

## Malware Family Classification

1. **Malware family**: Custom
2. **Malware type**: Loader
3. **Confidence**: High (for Type) / Medium (for Family)

4. **Key evidence**:
*   **Sophisticated Evasion Techniques:** The use of dynamic API resolution (via custom `GetProcAddress` wrappers), memory manipulation (`VirtualProtect`), and the implementation of software interrupts (`swi`) to break linear execution flow are clear indicators of a high-level, professional loader designed to bypass EDR systems.
*   **Multi-Stage Distribution:** The analysis identifies multiple dropped executables (e.g., `ivlnbis.exe`, `bnciobys.exe`) with randomized naming conventions, confirming its primary role as a "dropper" or multi-stage loader intended to deliver further payloads.
*   **Robust Obfuscation:** The inclusion of complex string decoding for Unicode/UTF-16 values and the intentional hiding of network/file indicators until runtime demonstrate a deliberate attempt to evade static analysis tools and sandbox detection.
