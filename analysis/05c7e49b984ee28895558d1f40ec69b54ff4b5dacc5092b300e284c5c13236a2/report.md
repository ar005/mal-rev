# Threat Analysis Report

**Generated:** 2026-07-14 17:14 UTC
**Sample:** `05c7e49b984ee28895558d1f40ec69b54ff4b5dacc5092b300e284c5c13236a2_05c7e49b984ee28895558d1f40ec69b54ff4b5dacc5092b300e284c5c13236a2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05c7e49b984ee28895558d1f40ec69b54ff4b5dacc5092b300e284c5c13236a2_05c7e49b984ee28895558d1f40ec69b54ff4b5dacc5092b300e284c5c13236a2.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 62,827,830 bytes |
| MD5 | `bd71c56b6c0824e7fd86a9c63c779b8e` |
| SHA1 | `b41362e805c992b98622e3bd44a220880a78228a` |
| SHA256 | `05c7e49b984ee28895558d1f40ec69b54ff4b5dacc5092b300e284c5c13236a2` |
| Overall entropy | 7.998 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771716682 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 181,760 | 6.463 | No |
| `.rdata` | 80,896 | 5.755 | No |
| `.data` | 3,584 | 1.816 | No |
| `.pdata` | 9,728 | 5.32 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 1,536 | 5.52 | No |
| `.reloc` | 2,048 | 5.264 | No |

### Imports

**USER32.dll**: `CreateWindowExW`, `ShutdownBlockReasonCreate`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `TranslateMessage`, `PostMessageW`, `GetMessageW`, `MessageBoxW`, `MessageBoxA`, `SystemParametersInfoW`
**COMCTL32.dll**: `ord_380`
**KERNEL32.dll**: `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetFileAttributesExW`, `SetEnvironmentVariableW`, `FlushFileBuffers`, `LCMapStringW`, `CompareStringW`, `VirtualProtect`, `InitializeCriticalSectionEx`, `GetOEMCP`, `GetCPInfo`, `GetLastError`, `FreeLibrary`, `GetProcAddress`
**ADVAPI32.dll**: `OpenProcessToken`, `GetTokenInformation`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `ConvertSidToStringSidW`
**GDI32.dll**: `SelectObject`, `DeleteObject`, `CreateFontIndirectW`

## Extracted Strings

Total strings found: **139041** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
UVWAUAWH
0A_A]_^]
SUVWAVAWH
A_A^_^][
A_A^_^][
\$ UAVAWH
0A_A^]
0A_A^]
L$ SUVWH
L$ SUVWH
T$hfD+D$df+T$`
@SUVWAVH
T$<f+T$4
PA^_^][
@USVWAVH
A^_^[]
|$ AVH
L$ SUVWH
L$ SUVWAV
A^_^][
L$ SUVWAV
A^_^][
L$ SUVWATAUAVAW
A_A^A]A\_^][
L$ SUVWAV
A^_^][
L$ SUVWAV
A^_^][
L$ SUVWATAUAVAW
A_A^A]A\_^][
UVWATAWH
0A_A\_^]
@UVATAU
A]A\^]
L9t$0t
tR@80tMH
L$ SVWH
@SUWAVAW
A_A^_][
H9{ t)
H9{(t(
H9{8t#
H9{@t&
l$ ATAVAWH
 A_A^A\
l$ VWAV
u[HcG0
l$ VATAUAVAWH
0A_A^A]A\^
MLcF0H
@SVAVH
t$ WAVAWH
VWATAVAWH
~#D8e0u
0A_A^A\_^
l$ VWAV
@UVWATAUAVAW
A_A^A]A\_^]
l$ VWATAVAW
A_A^A\_^
|$ AVH
UVWAVAWH
 A_A^_^]
WAVAWH
0A_A^_
@SUVWAV
A^_^][
@VATAUAVAWH
 A_A^A]A\^
@SUATAU
A]A\][
D$hH+D$pHi
|$8fff
SUVWATAUAVAWH
8A_A^A]A\_^][
SUVWATAUAVAWH
MP;H(s
MP;H8s
]Lu*A;|$
L$@E)}P
A;Exsg
E;E8v#A
L$@A9MP
tDE;u$t>H
T$8E+T$
XA_A^A]A\_^][
tHH9
uC
I@L9{8uH
t$HL9{0
~0L9{0
y<L9{0
\$ UVAVH
@USWATAVAWH
fD9 uA
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140018164` | `0x140018164` | 40065 | ✓ |
| `fcn.14001c130` | `0x14001c130` | 37955 | ✓ |
| `fcn.14001c11c` | `0x14001c11c` | 37914 | ✓ |
| `section..text` | `0x140001000` | 17899 | ✓ |
| `fcn.140027400` | `0x140027400` | 12313 | ✓ |
| `fcn.140004b70` | `0x140004b70` | 9279 | ✓ |
| `fcn.14000b6a0` | `0x14000b6a0` | 6161 | ✓ |
| `fcn.140029d90` | `0x140029d90` | 5703 | ✓ |
| `fcn.1400260ec` | `0x1400260ec` | 4735 | ✓ |
| `fcn.140001ca0` | `0x140001ca0` | 2338 | ✓ |
| `fcn.14002308c` | `0x14002308c` | 2201 | ✓ |
| `fcn.14001757c` | `0x14001757c` | 1946 | ✓ |
| `fcn.140012478` | `0x140012478` | 1898 | ✓ |
| `fcn.14001713c` | `0x14001713c` | 1777 | ✓ |
| `fcn.1400028a0` | `0x1400028a0` | 1773 | ✓ |
| `fcn.14002bcf0` | `0x14002bcf0` | 1661 | ✓ |
| `fcn.14000d390` | `0x14000d390` | 1468 | ✓ |
| `fcn.140029e60` | `0x140029e60` | 1451 | ✓ |
| `fcn.140023d8c` | `0x140023d8c` | 1421 | ✓ |
| `fcn.140014e90` | `0x140014e90` | 1397 | ✓ |
| `fcn.140023094` | `0x140023094` | 1353 | ✓ |
| `fcn.140005f70` | `0x140005f70` | 1325 | ✓ |
| `fcn.14000feac` | `0x14000feac` | 1263 | ✓ |
| `fcn.14000b1c0` | `0x14000b1c0` | 1238 | ✓ |
| `fcn.14000ad20` | `0x14000ad20` | 1179 | ✓ |
| `fcn.14001e380` | `0x14001e380` | 1171 | ✓ |
| `fcn.140009fe0` | `0x140009fe0` | 1169 | ✓ |
| `fcn.140025c60` | `0x140025c60` | 1164 | ✓ |
| `fcn.140014a20` | `0x140014a20` | 1133 | ✓ |
| `fcn.14001d810` | `0x14001d810` | 1119 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001ca0.c`](code/fcn.140001ca0.c)
- [`code/fcn.1400028a0.c`](code/fcn.1400028a0.c)
- [`code/fcn.140004b70.c`](code/fcn.140004b70.c)
- [`code/fcn.140005f70.c`](code/fcn.140005f70.c)
- [`code/fcn.140009fe0.c`](code/fcn.140009fe0.c)
- [`code/fcn.14000ad20.c`](code/fcn.14000ad20.c)
- [`code/fcn.14000b1c0.c`](code/fcn.14000b1c0.c)
- [`code/fcn.14000b6a0.c`](code/fcn.14000b6a0.c)
- [`code/fcn.14000d390.c`](code/fcn.14000d390.c)
- [`code/fcn.14000feac.c`](code/fcn.14000feac.c)
- [`code/fcn.140012478.c`](code/fcn.140012478.c)
- [`code/fcn.140014a20.c`](code/fcn.140014a20.c)
- [`code/fcn.140014e90.c`](code/fcn.140014e90.c)
- [`code/fcn.14001713c.c`](code/fcn.14001713c.c)
- [`code/fcn.14001757c.c`](code/fcn.14001757c.c)
- [`code/fcn.140018164.c`](code/fcn.140018164.c)
- [`code/fcn.14001c11c.c`](code/fcn.14001c11c.c)
- [`code/fcn.14001c130.c`](code/fcn.14001c130.c)
- [`code/fcn.14001d810.c`](code/fcn.14001d810.c)
- [`code/fcn.14001e380.c`](code/fcn.14001e380.c)
- [`code/fcn.14002308c.c`](code/fcn.14002308c.c)
- [`code/fcn.140023094.c`](code/fcn.140023094.c)
- [`code/fcn.140023d8c.c`](code/fcn.140023d8c.c)
- [`code/fcn.140025c60.c`](code/fcn.140025c60.c)
- [`code/fcn.1400260ec.c`](code/fcn.1400260ec.c)
- [`code/fcn.140027400.c`](code/fcn.140027400.c)
- [`code/fcn.140029d90.c`](code/fcn.140029d90.c)
- [`code/fcn.140029e60.c`](code/fcn.140029e60.c)
- [`code/fcn.14002bcf0.c`](code/fcn.14002bcf0.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

Based on the addition of the third disassembly chunk, I have further refined the analysis of the binary. The latest code reveals that while the underlying framework is indeed a modified PyInstaller bootloader, it incorporates significant "wrapper" logic designed for heavy data transformation and environment-agnostic execution.

---

### Updated Technical Analysis (Cumulative)

#### Core Functionality and Purpose
The binary remains identified as a **sophisticated Python-bundled executable**. However, the new segment clarifies how the bootloader interacts with its internal payload:

*   **Custom Payload Decryption/Deobfuscation:** The presence of `fcn.140025c60`—which contains extensive bit-shifting, multi-precision arithmetic logic (handling large integers across multiple memory blocks), and modulo operations—strongly indicates that the "payload" is not just bundled; it is **actively processed or decrypted** using complex math before it reaches the Python interpreter.
*   **Robust I/O Handling:** Function `fcn.14001d810` shows sophisticated handling of system input/output, including transitions between Unicode and ANSI encodings and various file-reading methods. This ensures that the internal logic remains consistent across different locales and OS configurations.
*   **"Hidden" Execution Environment:** The inclusion of `"PyInstallerOnefileHiddenWindow"` (in `fcn.140009fe0`) confirms a design intended to run a child process or a sub-component in a hidden window, likely to detach the "main" logic from any UI and ensure it remains invisible during execution.

#### Suspicious or Malicious Behaviors (Expanded)
The following behaviors are highlighted as high-interest for an incident responder:

*   **Multi-Stage Transformation Logic:** The complex logic in `fcn.140025c60` is characteristic of custom encryption layers. If a standard Python script were being loaded, such heavy mathematical lifting would not typically exist at the bootloader level unless it was designed to decrypt an encrypted payload "on-the-fly."
*   **Evidence of Anti-Analysis/Stealth:** The usage of `ShowWindow(..., 0)` and the specific window naming conventions indicate a high degree of intentionality in hiding the process's footprint. It is trying to appear as a background system process or a standard "one-file" utility while masking its true operations.
*   **Complex Dispatch Table logic:** The large switch-style logic in `fcn.140014e90` and `fcn.140014a20` suggests that the bootloader is navigating a very large "vocabulary" of commands or data types, making it difficult to determine the full scope of what the script can do just by looking at the entry point.

#### Notable Techniques & Patterns
*   **Advanced Data Interpretation:** The use of bitwise operations to interpret segments of memory (e.g., `((uVar3 >> 0x10) * 4 + 0x140031760)`) suggests the loader is parsing a highly-packed or non-standard data structure within its internal archive.
*   **Robust I/O Management:** The logic in `fcn.14001d810` for handling `ReadConsoleW`, `ReadFile`, and standard output translation shows that even if the launcher's primary goal is "wrapping" a script, it has been engineered to be highly reliable in various environments—a trait common in professional-grade malware samples.
*   **PyInstaller Modification:** While the string `"PyInstallerOnefileHiddenWindow"` gives away its origin, the vast amount of additional code around this call (handling multi-language support and SIMD-accelerated math) indicates a **customized wrapper**. This is often used to "blend in" with legitimate software while housing high-complexity malicious payloads.

---

### Updated Summary for Analyst
The binary is a **highly engineered, multi-layer bootloader** designed to host an encrypted or heavily obfuscated Python/T1 script. It exhibits the following key characteristics:

1.  **Complex Pre-processing Layer:** The inclusion of advanced bitwise math and SIMD instructions (`fcn.140025c60` & `fcn.140029e60`) implies that the "payload" is likely decrypted or expanded into a usable state in memory before the Python interpreter even starts.
2.  **Hybrid Framework Intent:** The combination of Tcl/Python support and complex internal mapping suggests it is built to be versatile, possibly allowing one bootloader to serve different types of payloads depending on the configuration.
3.  **Intentional Stealth:** The use of hidden windows, specific standard library calls for hidden execution, and robust I/O abstraction are indicators of a mature development cycle aimed at evading casual analysis.

**Updated Recommendation:**
The complexity of the pre-processing suggests that **static analysis of the final "extracted" Python script will be difficult.** Because much of the "unpacking" happens during the boot process:

1.  **Perform Dynamic Memory Dumps:** Capture a memory dump shortly after `fcn.140025c60` and the SIMD-heavy functions are executed to see if it yields a decrypted payload.
2.  **Look for "Stage 2" Execution:** The call to `CreateProcessW` in `fcn.140009fe0` suggests that this bootloader may be creating a second process or a child thread where the real heavy lifting (malicious activity) occurs.
3.  **Identify Key-Exchange/Decryption Keys:** If you find high-entropy data blocks within the internal archive, they are likely candidates for being decrypted by the logic found in `fcn.140025c60`.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the technical analysis to the corresponding MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059.005** | Command and Scripting Interpreter: Python | The analysis confirms the binary is a modified PyInstaller bootloader designed to host and execute a Python/T-script payload. |
| **T1027** | Obfuscated Files or Information | The use of complex bitwise operations, multi-precision math, and large dispatch tables are used to decrypt and hide the logic of the internal payload from analysis. |
| **T1036.005** | Masquerading: System Binaries | The usage of specific hidden window parameters and common PyInstaller naming conventions is designed to blend the malicious process with standard system utilities. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and the behavioral report, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The string dump contains high-entropy/obfuscated data but no plaintext network indicators.)

### **File paths / Registry keys**
*   *None identified.* (Standard system calls were noted in the report, but no specific malicious paths or registry keys were disclosed.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 strings were present in the provided data.)

### **Other artifacts**
*   **Framework Markers:** 
    *   `PyInstallerOnefileHiddenWindow` (Identifies the use of a modified PyInstaller bootloader to hide windows during execution).
*   **Internal Logic Offsets (Behavioral Artifacts):**
    *   `fcn.140025c60`: Identified as the location for core decryption and multi-precision arithmetic logic.
    *   `fcn.140029e60`: Identified as part of the SIMD-accelerated math/decryption routines.
    *   `fcn.14001d810`: Associated with robust I/O handling and terminal output translation.
    *   `fcn.140014e90` / `fcn.140014a20`: Identified as the "Dispatch Table" logic used to navigate internal command sets.

---

### **Analyst Notes:**
The string dump provided consists largely of obfuscated data or junk characters likely used for local decryption during the boot process. No network-based IOCs were found in this specific sample; however, the behavioral analysis indicates that the payload is only revealed in memory after `fcn.140025c60` executes. 

**Recommendation:** To find more "traditional" IOCs (IPs/URLs), a dynamic memory dump should be performed at the point where the multi-step transformation logic completes, specifically just before the call to `CreateProcessW`.

---

## Malware Family Classification

1. **Malware family**: Custom
2. **Malware type**: Loader / Dropper
3. **Confidence**: High (for its role as a loader)

**Key evidence:**
*   **Advanced Obfuscation & Decryption:** The presence of `fcn.140025c60` indicates a complex, multi-layered decryption process using bit-shifting and SIMD-accelerated math to unpack a payload in memory before execution.
*   **Evasive Execution Environment:** The use of "PyInstallerOnefileHiddenWindow" and explicit `ShowWindow(..., 0)` calls demonstrate a deliberate intent to hide the process from the end-user while maintaining long-term persistence/operation.
*   **Sophisticated Wrapper Architecture:** The sample functions as a high-end wrapper for a Python/T-script, utilizing a large dispatch table and robust I/O handling to mask its true functionality and ensure consistent execution across different environments.
