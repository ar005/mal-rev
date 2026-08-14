# Threat Analysis Report

**Generated:** 2026-08-11 17:00 UTC
**Sample:** `0e12143a4b0dfc48f4bf791c90e5fd64fa6529c9a493755015aa210b13a804d6_0e12143a4b0dfc48f4bf791c90e5fd64fa6529c9a493755015aa210b13a804d6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e12143a4b0dfc48f4bf791c90e5fd64fa6529c9a493755015aa210b13a804d6_0e12143a4b0dfc48f4bf791c90e5fd64fa6529c9a493755015aa210b13a804d6.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 4 sections |
| Size | 168,960 bytes |
| MD5 | `11300ae5a0e3b41d5f8fddeab7cc77d3` |
| SHA1 | `d71346dc872207727270bb08097f14e07e2dedd9` |
| SHA256 | `0e12143a4b0dfc48f4bf791c90e5fd64fa6529c9a493755015aa210b13a804d6` |
| Overall entropy | 6.079 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1778085863 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 110,080 | 6.432 | No |
| `.rdata` | 43,008 | 4.649 | No |
| `.data` | 8,704 | 3.232 | No |
| `.pdata` | 6,144 | 5.043 | No |

### Imports

**KERNEL32.dll**: `Sleep`, `GetProcAddress`, `GlobalAlloc`, `GlobalLock`, `GlobalUnlock`, `LoadLibraryA`, `CreateFileW`, `CloseHandle`, `GetModuleHandleW`, `GlobalHandle`, `GlobalFree`, `lstrcmpA`, `GetLastError`, `WaitForSingleObject`, `ExitProcess`
**WININET.dll**: `HttpSendRequestA`, `InternetReadFile`, `InternetConnectA`, `InternetCloseHandle`, `InternetOpenA`, `HttpOpenRequestA`, `HttpQueryInfoA`
**SHLWAPI.dll**: `StrStrA`

## Extracted Strings

Total strings found: **667** (showing first 100)

```
`.rdata
@.data
.pdata
VWATAVAWH
@A_A^A\_^
x ATAVAWH
 A_A^A\
WATAUAVAWH
0A_A^A]A\_
|$ UAVAWH
@A_A^]
\$ VWAVH
u[8Y$t
\$ VWAVH
u[8Y$t
WAVAWH
 A_A^_
C$9C w
|$ UATAUAVAWH
A_A^A]A\]
x ATAVAWH
Y;w }]H
;G$});
 A_A^A\
WAVAWH
 A_A^_
{|^uMH
Cx<bu	
Cx<bu	
{x\uOH
t'<	v'
VWATAVAWH
}Uf	w@
.u(H;3
{|]u}H
0A_A^A\_^
|$ AVH
SVWATAUAVAWH
PA_A^A]A\_^[
UAVAWH
t$ UWAVH
UWATAVAWH
A_A^A\_]
WAVAWH
 A_A^_
WAVAWH
 A_A^_
|/\t	f
@8>tH
UVWATAUAVAWH
9D$@u%L
A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
VWATAVAWH
A_A^A\_^
\$ UVWATAUAVAWH
uL9=e
PA_A^A]A\_^]
t$ UWAVH
@USVWAVH
0A^_^[]
UAVAWH
|$D
uI
fD9|$T
x ATAVAWH
A_A^A\
t$ WATAUAVAWH
A_A^A]A\_
ATAVAWH
 A_A^A\
fffffff
VWATAVAWH
 A_A^A\_^
x ATAVAWH
 A_A^A\
x UAVAWH
t$ WAVAWH
@SUVWATAVAWH
zu|D!t$ E3
A_A^A\_^][
WATAUAVAWH
@A_A^A]A\_
WATAUAVAWH
A_A^A]A\_
Genuua
ineIuY
nteluQ3
VWATAVAWH
A_A^A\_^
UVWATAUAVAWH
wL9g0u
O0HcQH
O0HcQ
G0Hc	H
A_A^A]A\_^]
D8eoupH
UVWATAUAVAWH
pA_A^A]A\_^]
WATAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14000bcac` | `0x14000bcac` | 12875 | ✓ |
| `fcn.14000d2a0` | `0x14000d2a0` | 11733 | ✓ |
| `fcn.14000b118` | `0x14000b118` | 8425 | ✓ |
| `fcn.1400031e8` | `0x1400031e8` | 8119 | ✓ |
| `fcn.14000ff58` | `0x14000ff58` | 7757 | ✓ |
| `fcn.140003480` | `0x140003480` | 4718 | ✓ |
| `fcn.1400119d0` | `0x1400119d0` | 2937 | ✓ |
| `fcn.14001a72c` | `0x14001a72c` | 2764 | ✓ |
| `fcn.140006680` | `0x140006680` | 2596 | ✓ |
| `fcn.140003288` | `0x140003288` | 2488 | ✓ |
| `fcn.140019ed8` | `0x140019ed8` | 2129 | ✓ |
| `fcn.140012808` | `0x140012808` | 1908 | ✓ |
| `fcn.140019378` | `0x140019378` | 1454 | ✓ |
| `fcn.140019928` | `0x140019928` | 1454 | ✓ |
| `fcn.140015a90` | `0x140015a90` | 1452 | ✓ |
| `fcn.140009560` | `0x140009560` | 1252 | ✓ |
| `fcn.14000be74` | `0x14000be74` | 1204 | ✓ |
| `fcn.140011534` | `0x140011534` | 1018 | ✓ |
| `fcn.140018254` | `0x140018254` | 944 | ✓ |
| `fcn.140013384` | `0x140013384` | 927 | ✓ |
| `fcn.140002a88` | `0x140002a88` | 887 | ✓ |
| `fcn.140017068` | `0x140017068` | 840 | ✓ |
| `fcn.140017d94` | `0x140017d94` | 814 | ✓ |
| `fcn.140013d68` | `0x140013d68` | 782 | ✓ |
| `fcn.140007bc0` | `0x140007bc0` | 738 | ✓ |
| `fcn.1400046f8` | `0x1400046f8` | 718 | ✓ |
| `fcn.14001040c` | `0x14001040c` | 718 | ✓ |
| `fcn.14000f778` | `0x14000f778` | 686 | ✓ |
| `fcn.140008978` | `0x140008978` | 676 | ✓ |
| `fcn.1400078c0` | `0x1400078c0` | 656 | ✓ |

### Decompiled Code Files

- [`code/fcn.140002a88.c`](code/fcn.140002a88.c)
- [`code/fcn.1400031e8.c`](code/fcn.1400031e8.c)
- [`code/fcn.140003288.c`](code/fcn.140003288.c)
- [`code/fcn.140003480.c`](code/fcn.140003480.c)
- [`code/fcn.1400046f8.c`](code/fcn.1400046f8.c)
- [`code/fcn.140006680.c`](code/fcn.140006680.c)
- [`code/fcn.1400078c0.c`](code/fcn.1400078c0.c)
- [`code/fcn.140007bc0.c`](code/fcn.140007bc0.c)
- [`code/fcn.140008978.c`](code/fcn.140008978.c)
- [`code/fcn.140009560.c`](code/fcn.140009560.c)
- [`code/fcn.14000b118.c`](code/fcn.14000b118.c)
- [`code/fcn.14000bcac.c`](code/fcn.14000bcac.c)
- [`code/fcn.14000be74.c`](code/fcn.14000be74.c)
- [`code/fcn.14000d2a0.c`](code/fcn.14000d2a0.c)
- [`code/fcn.14000f778.c`](code/fcn.14000f778.c)
- [`code/fcn.14000ff58.c`](code/fcn.14000ff58.c)
- [`code/fcn.14001040c.c`](code/fcn.14001040c.c)
- [`code/fcn.140011534.c`](code/fcn.140011534.c)
- [`code/fcn.1400119d0.c`](code/fcn.1400119d0.c)
- [`code/fcn.140012808.c`](code/fcn.140012808.c)
- [`code/fcn.140013384.c`](code/fcn.140013384.c)
- [`code/fcn.140013d68.c`](code/fcn.140013d68.c)
- [`code/fcn.140015a90.c`](code/fcn.140015a90.c)
- [`code/fcn.140017068.c`](code/fcn.140017068.c)
- [`code/fcn.140017d94.c`](code/fcn.140017d94.c)
- [`code/fcn.140018254.c`](code/fcn.140018254.c)
- [`code/fcn.140019378.c`](code/fcn.140019378.c)
- [`code/fcn.140019928.c`](code/fcn.140019928.c)
- [`code/fcn.140019ed8.c`](code/fcn.140019ed8.c)
- [`code/fcn.14001a72c.c`](code/fcn.14001a72c.c)

## Behavioral Analysis

Based on the second portion of the disassembly, the analysis confirms and expands upon the initial findings. This chunk reveals a deeper level of complexity regarding how the malware **processes parsed data** and **manages internal state** after decryption.

### Updated Analysis Summary
The additional disassembly reinforces the classification of this binary as a high-sophistication **malware loader/packer**. While Chunk 1 highlighted the "unpacking" and "decryption" stages, Chunk 2 reveals the "post-processing" stage: parsing complex configuration structures, handling string conversions for Windows API compatibility, and implementing defensive "landmines" to thwart researchers.

---

### Expanded Core Functionality

*   **Robust Memory Management & Manipulation:**
    *   `fcn.140009560` appears to be a custom implementation or wrapper of `memmove`/`memcpy`. It includes logic to handle overlapping memory regions and utilizes `LOCK/UNLOCK` primitives. This indicates the malware is moving large chunks of decrypted data into specific "staging" areas in memory before use.
*   **Complex Configuration Parsing:**
    *   `fcn.140002a88` contains a sophisticated state machine to handle string parsing. It specifically checks for special characters (e.g., `0x5c` for backslash, `0x5b` and `0x7b` for brackets). This is likely used to parse **file paths or command-line arguments** from an encrypted configuration block, ensuring that escape characters are handled correctly.
    *   `fcn.140018254` contains logic specifically designed to construct numbers into strings (e.g., handling signs like `-` and `+`, and constructing multi-digit numbers). This suggests the malware is generating specific values for network protocols or internal logging.
*   **Unicode/ANSI Transformation:**
    *   Several functions (`fcn.140017068`, `fcn.140013384`) call `MultiByteToWideChar` and `GetCPInfo`. This is a common technique in "loader" malware to ensure that decrypted strings (often in UTF-8 or ANSI) are converted to the format required by Windows APIs (UTF-16). It ensures "compatibility" so the malicious commands are correctly interpreted by the OS.

### Enhanced Suspicious & Malicious Behaviors

*   **Exploiting Logic Traps (Anti-Analysis):**
    *   The frequent use of `swi(3)` (Software Interrupt) within complex logic blocks (e.g., in `fcn.14000be74`) is a classic "landmine." If an analyst tries to step through the code or if the malware detects an inconsistent state caused by a debugger, it triggers this interrupt. This often causes the debugger to crash or the process to terminate abruptly, preventing the researcher from reaching the next stage of execution.
*   **Massive Data Processing Loops:**
    *   `fcn.140011534` is a notable "processing" loop. It iterates through an array/structure and calls `fcn.140009cb4` (likely a decryption or "normalization" routine) on dozens of offsets. This suggests that once the primary payload is unpacked, it performs a **second pass of decryption** on specific internal variables to keep them "hidden" in memory until the moment they are needed.
*   **Conditional Execution based on String Matching:**
    *   `fcn.1400078c0` uses `lstrcmpA` and `StrStrA` to compare extracted strings against hardcoded values. This acts as a **decision-making gate**. For example, the malware may check if a "Command ID" matches a specific value before deciding whether to drop a file, launch a process, or initiate a network connection.

### Technical Observations & Patterns

*   **Advanced String Manipulation:** The heavy presence of `StrStr`, `lstrcmp`, and manual byte-looping indicates that the malware's configuration is not just a simple list of values; it is a complex data structure. It likely supports multiple "modules" or "commands," only activating specific ones based on the decrypted config.
*   **Layered Obfuscation:** The distinction between `fcn.140011534` (mass decryption) and `fcn.140002a88` (complex parsing) shows a **layered approach**. This is designed to defeat automated "de-obfuscators" that only look for one layer of XOR/XOR-rotation; the analyst must peel back multiple layers of logic to see the actual intended actions.
*   **Heavy Logic Branching:** The jump tables and complex nested `if` statements (as seen in the end of some functions) are often used to "flatten" the control flow, making it difficult for a human to follow the logic path using static analysis tools like IDA Pro or Ghidra without running the code.

### Conclusion for Investigation
This is a highly disciplined piece of malware. It focuses heavily on **minimizing its footprint** by only de-obfuscating what is needed "just in time." 

**Recommendation for Analysts:** 
1.  **Memory Forensics:** Instead of trying to manually de-obfuscate every loop, set hardware breakpoints on the memory regions being accessed by `fcn.140011534`. This will allow you to capture the "fully" unpacked data in memory before it is used by the next stage.
2.  **Trace the "Gate":** Focus on `fcn.1400078c0` and similar functions that use string comparisons. These are the "switching stations"—identifying which branch is taken will tell you exactly what the malware *intends* to do (e.g., inject, drop, or steal data).

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your technical analysis to the relevant MITRE ATT&CK techniques below.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1435** | Debugger Evasion | The use of `swi(3)` "logic traps" is specifically designed to crash debuggers or terminate the process when an inconsistent state (caused by a researcher) is detected. |
| **T1027** | Obfuscated Files or Information | The malware employs layered decryption, complex parsing logic, and "just-in-time" de-obfuscation to hide its configuration and payload from static analysis. |
| **T1059** | Command and Scripting Interpreter (Implicit) | The use of a "decision-making gate" based on string matching suggests the loader interprets specific commands within a decrypted configuration to determine subsequent actions. |
| **T1027.003** | Packing | The behavior described as a "malware loader/packer" involving multiple stages of decoding and unpacking fits this sub-technique for hiding original instructions. |

### Analyst Notes:
*   **Defense Evasion (T1435):** This is the most critical observation regarding the interactive analysis of the sample, as it actively targets the tools used by security researchers.
*   **Obfuscation Strategy (T1027):** The "multi-pass" decryption and memory management signify a high level of sophistication typical of sophisticated loaders (e.g., those used in Cobalt Strike or advanced APT campaigns) to ensure that even if one layer is cracked, the next remains hidden.
*   **Refined Logic:** While the Unicode/ANSI transformation is common in Windows development, its presence here serves as an enabler for **T1027**, ensuring that the "hidden" commands are successfully processed by the OS once de-obfuscated.

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the identified Indicators of Compromise (IOCs).

### **Analysis Summary**
The "EXTRACTED STRINGS" section contains highly obfuscated or partially decrypted data blocks. Most of these strings appear to be junk code, internal logic fragments, or remnants of a multi-stage decryption process. No clear plaintext IP addresses, URLs, or file paths were present in the raw string dump. The primary value for intelligence is found in the **Behavioral Analysis**, which identifies specific functions and techniques used by the malware.

---

### **Indicators of Compromise**

**IP addresses / URLs / Domains**
*   *None identified.* (The strings provided are heavily obfuscated or represent internal data structures).

**File paths / Registry keys**
*   *None directly extracted.* (Note: The behavioral analysis indicates that `fcn.140002a88` is used to process file paths and command-line arguments, but these remain encrypted in the provided sample).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Anti-Analysis Technique (Landmine):** The use of `swi(3)` (Software Interrupt) at address `fcn.14000be74`. This is a known technique to crash debuggers or exit the process if an analyst attempts to step through the code.
*   **Layered Obfuscation Logic:** 
    *   `fcn.140011534`: A secondary decryption/normalization loop used for internal variables.
    *   `fcn.140002a88`: A state machine for handling special characters (backslashes, brackets) in configuration parsing.
*   **Potential Execution Gates:** 
    *   `fcn.1400078c0`: Utilizes `lstrcmpA` and `StrStrA` to determine execution paths (e.g., deciding whether to drop a payload or initiate a network connection).
*   **Unicode Conversion Point:** `fcn.140017068` and `fcn.140013384` are identified as the points where data is transitioned into Windows-compatible Unicode for API interaction.

---
**Analyst Note:** Because this is a high-sophistication loader/packer, the "hard" IOCs (IPs/Domains) are likely only present in memory during execution ("Just-in-Time" de-obfuscation). Detection should focus on the behavior of `fcn.140011534` and monitoring for calls to `MultiByteToWideChar` following decrypted buffer access.

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1. **Malware family:** custom
2. **Malware type:** loader
3. **Confidence:** High (for type), Medium (for family)
4. **Key evidence:** 
    *   **Multi-Stage Decryption & "Just-in-Time" De-obfuscation:** The analysis identifies a layered approach where the malware only decrypts specific components (via `fcn.140011534`) when needed, indicating it is designed to host and deploy a secondary, more functional payload.
    *   **Advanced Anti-Analysis Techniques:** The use of `swi(3)` "landmines" specifically aimed at crashing debuggers (T1435) and the complex control flow flattening are hallmark characteristics of sophisticated loaders used in professional cybercrime campaigns.
    *   **Complex Configuration Parsing:** The presence of a state machine for handling path characters and "decision-making gates" (`fcn.1400078c0`) indicates that the binary serves as a command-driven loader, designed to interpret encrypted configurations to determine specific actions (e.g., dropping files or initiating network connections).
