# Threat Analysis Report

**Generated:** 2026-06-29 00:27 UTC
**Sample:** `03224277f831034a084fcbcc5def473d113edef62842e5337db2408b6281d501_03224277f831034a084fcbcc5def473d113edef62842e5337db2408b6281d501.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `03224277f831034a084fcbcc5def473d113edef62842e5337db2408b6281d501_03224277f831034a084fcbcc5def473d113edef62842e5337db2408b6281d501.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 753,152 bytes |
| MD5 | `47aa6081a8c4457ea63993dd092c297f` |
| SHA1 | `f4ba0876034e7f20a8dfafbb6365353e55945d71` |
| SHA256 | `03224277f831034a084fcbcc5def473d113edef62842e5337db2408b6281d501` |
| Overall entropy | 6.184 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766059758 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 444,416 | 6.46 | No |
| `.rdata` | 106,496 | 5.204 | No |
| `.data` | 181,760 | 5.257 | No |
| `.pdata` | 15,360 | 5.7 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 3,584 | 5.375 | No |

### Imports

**KERNEL32.dll**: `GetModuleFileNameA`, `LoadLibraryA`, `GetProcAddress`, `GetCurrentProcess`, `SetEndOfFile`, `QueryPerformanceCounter`, `QueryPerformanceFrequency`, `ReleaseSRWLockExclusive`, `AcquireSRWLockExclusive`, `SleepConditionVariableSRW`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `GetStringTypeW`, `GetLocaleInfoEx`

## Extracted Strings

Total strings found: **2328** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
.reloc
UATAUAVAWH
A_A^A]A\]
WAVAWH
0A_A^_
SVWATAUAVAW
A_A^A]A\_^[
` UAVAWH
WATAUAVAWH
0A_A^A]A\_
L$ SUVWH
CfA9S
CfA9S
x UATAUAVAWH
T$pH;W
A_A^A]A\]
WATAUAVAWH
|$DH9z
uhH9|$xt
u&H9|$`
 L;d$htuA
L;d$hs
A_A^A]A\_
UVWATAUAVAWH
GD$xE3
A_A^A]A\_^]
x UATAUAVAWH
A_A^A]A\]
SVWATAUAVAWH
uNH9|$xt
u&H9|$`
 L;d$htuA
L;d$hs
A_A^A]A\_^[
WATAUAVAWH
 A_A^A]A\_
` AUAVAWH
A_A^A]
x ATAVAWH
 A_A^A\
3333333
x ATAVAWH
0A_A^A\
WAVAWH
 A_A^_
UWATAVAWH
L9}pu{A
L9}puYA
L9}pu7A
A_A^A\_]
WAVAWH
 A_A^_
WAVAWH
 A_A^_
x ATAVAWH
 A_A^A\
UVWATAUAVAWH
L$@I9v 
A_A^A]A\_^]
UATAUAVAWH
L$PL9|$HH
L9|$hH
A_A^A]A\]
UVWATAUAVAWH
f(E8~)
f(E8~)
f(E8~)
f(E8~)
f(E8~)
f(E8~)
L$PL9g 
f(E8~)
f(E8~)
f(E8~)
f(E8~)
A_A^A]A\_^]
WAVAWH
0A_A^_
t$ UWAVH
WAVAWH
0A_A^_
UWATAVAWH
A_A^A\_]
UAVAWH
x ATAVAWH
0A_A^A\
k VWAVH
t$ UWAVH
t$ UWAVH
C@H9C8u
C@H9C8u
x ATAVAWH
 A_A^A\
` UAUAWH
x ATAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.std::ctype_wchar_t_.virtual_24` | `0x1400215e0` | 119936 | ✓ |
| `fcn.14003e544` | `0x14003e544` | 89906 | ✓ |
| `fcn.140058ca0` | `0x140058ca0` | 55337 | ✓ |
| `fcn.1400563a8` | `0x1400563a8` | 53883 | ✓ |
| `fcn.140056394` | `0x140056394` | 53842 | ✓ |
| `fcn.140053fc0` | `0x140053fc0` | 50983 | ✓ |
| `method.std::basic_stringstream_wchar_t__struct_std::char_traits_wchar_t___class_std::allocator_wchar_t__.virtual_0` | `0x140033d7c` | 40376 | ✓ |
| `method.std::basic_ostringstream_wchar_t__struct_std::char_traits_wchar_t___class_std::allocator_wchar_t__.virtual_0` | `0x140033d94` | 40312 | ✓ |
| `method.std::basic_iostream_wchar_t__struct_std::char_traits_wchar_t__.virtual_0` | `0x140033dac` | 40196 | ✓ |
| `method.std::basic_ostream_wchar_t__struct_std::char_traits_wchar_t__.virtual_0` | `0x140033db8` | 40032 | ✓ |
| `method.std::basic_istream_wchar_t__struct_std::char_traits_wchar_t__.virtual_0` | `0x140033dd0` | 39956 | ✓ |
| `method.std::basic_stringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x140033da0` | 39616 | ✓ |
| `method.std::basic_istringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x140033ddc` | 39588 | ✓ |
| `method.std::basic_iostream_char__struct_std::char_traits_char__.virtual_0` | `0x140033de8` | 39460 | ✓ |
| `method.std::basic_ostream_char__struct_std::char_traits_char__.virtual_0` | `0x140033d88` | 39188 | ✓ |
| `method.std::basic_istream_char__struct_std::char_traits_char__.virtual_0` | `0x140033dc4` | 39148 | ✓ |
| `fcn.140069ae0` | `0x140069ae0` | 38154 | ✓ |
| `fcn.140002b9c` | `0x140002b9c` | 21003 | ✓ |
| `fcn.1400490bc` | `0x1400490bc` | 13584 | ✓ |
| `fcn.14003e8d4` | `0x14003e8d4` | 12418 | ✓ |
| `fcn.140046d84` | `0x140046d84` | 7424 | ✓ |
| `fcn.140023e58` | `0x140023e58` | 7220 | ✓ |
| `fcn.140010624` | `0x140010624` | 5367 | ✓ |
| `fcn.140009970` | `0x140009970` | 5236 | ✓ |
| `fcn.14000b640` | `0x14000b640` | 5036 | ✓ |
| `fcn.1400359a0` | `0x1400359a0` | 4821 | ✓ |
| `fcn.140066994` | `0x140066994` | 4735 | ✓ |
| `fcn.14003cc80` | `0x14003cc80` | 4595 | ✓ |
| `fcn.14000f084` | `0x14000f084` | 4300 | ✓ |
| `fcn.14001aebc` | `0x14001aebc` | 4185 | ✓ |

### Decompiled Code Files

- [`code/fcn.140002b9c.c`](code/fcn.140002b9c.c)
- [`code/fcn.140009970.c`](code/fcn.140009970.c)
- [`code/fcn.14000b640.c`](code/fcn.14000b640.c)
- [`code/fcn.14000f084.c`](code/fcn.14000f084.c)
- [`code/fcn.140010624.c`](code/fcn.140010624.c)
- [`code/fcn.14001aebc.c`](code/fcn.14001aebc.c)
- [`code/fcn.140023e58.c`](code/fcn.140023e58.c)
- [`code/fcn.1400359a0.c`](code/fcn.1400359a0.c)
- [`code/fcn.14003cc80.c`](code/fcn.14003cc80.c)
- [`code/fcn.14003e544.c`](code/fcn.14003e544.c)
- [`code/fcn.14003e8d4.c`](code/fcn.14003e8d4.c)
- [`code/fcn.140046d84.c`](code/fcn.140046d84.c)
- [`code/fcn.1400490bc.c`](code/fcn.1400490bc.c)
- [`code/fcn.140053fc0.c`](code/fcn.140053fc0.c)
- [`code/fcn.140056394.c`](code/fcn.140056394.c)
- [`code/fcn.1400563a8.c`](code/fcn.1400563a8.c)
- [`code/fcn.140058ca0.c`](code/fcn.140058ca0.c)
- [`code/fcn.140066994.c`](code/fcn.140066994.c)
- [`code/fcn.140069ae0.c`](code/fcn.140069ae0.c)
- [`code/method.std__basic_iostream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_iostream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_iostream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c`](code/method.std__basic_iostream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c)
- [`code/method.std__basic_istream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_istream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_istream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c`](code/method.std__basic_istream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c)
- [`code/method.std__basic_istringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c`](code/method.std__basic_istringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c)
- [`code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_ostream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c`](code/method.std__basic_ostream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c)
- [`code/method.std__basic_ostringstream_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_0.c`](code/method.std__basic_ostringstream_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_0.c)
- [`code/method.std__basic_stringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c`](code/method.std__basic_stringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c)
- [`code/method.std__basic_stringstream_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_0.c`](code/method.std__basic_stringstream_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_0.c)
- [`code/method.std__ctype_wchar_t_.virtual_24.c`](code/method.std__ctype_wchar_t_.virtual_24.c)

## Behavioral Analysis

The analysis of the final chunk of disassembly provides a "master view" of how the core engine of this loader operates. While previous chunks revealed the **tools** it uses (JSON parsing, WinINet networking, Steam-specific targeting), this section reveals the **architecture** of the logic that drives those tools.

Here is the updated and expanded analysis.

### Updated Analysis of Binary Characteristics

#### 1. State-Driven Modular Architecture
The sheer complexity and repetitive structure in `fcn.14001aebc` confirm that this is not a simple linear script, but a **modular execution engine**. 
*   **State Machine Logic:** The code frequently checks variables like `iVar9` against specific constants (e.g., `0xb`, `8`, `0xc`). These are likely "Action IDs" or "Command Codes." When the binary receives a command from the C2 server, it identifies the ID and jumps to the corresponding block of code.
*   **Polymorphic Behavior:** This architecture allows the same piece of code to perform vastly different actions (e.g., keylogging in one instance, credential theft in another) simply by changing the instructions sent via JSON from the remote server.

#### 2. Advanced Control Flow Obfuscation
The code utilizes several techniques to hinder manual analysis:
*   **Indirection Layers:** Instead of a straightforward `if/else` or `switch`, the code uses complex table lookups and intermediate variables (like `cVar6`) to decide the next jump. This creates "spaghetti" logic that makes it difficult for an analyst to trace the full execution path statically.
*   **Code Branching:** Many paths are set up but only one is taken based on external input. This means a sandbox or emulator may only ever see 10% of the code’s capabilities because the "trigger" (the C2 command) isn't present during analysis.

#### 3. Robust Error Handling & "Graceful Failure"
The repeated appearance of `swi(3)` calls and specialized exit functions (like `fcn.14003fcc0` or `fcn.140045994`) indicates a sophisticated safety net:
*   **Anti-Crash Design:** If an action fails (e.g., a network timeout, a missing file, or an invalid JSON key), the binary is designed to "fail gracefully." Instead of crashing and alerting the user/AV, it executes a clean exit or skips that specific module and moves to the next available task.
*   **Environment Validation:** The logic ensures that certain conditions are met before entering high-risk functions, likely to ensure that the malware only activates its primary payload when it confirms it is on a "real" victim machine rather than an analysis sandbox.

#### 4. Object-Oriented Wrappers (C++ Artifacts)
The heavy use of `pppuStack` and `auStack` names, combined with complex pointer arithmetic, suggests the code was written in C++ or a similar high-level language before being compiled. 
*   **Abstraction:** The binary treats its tasks as "objects." For example, one block might be for "Network Management," another for "File System Interaction." By wrapping these in objects, the developer can share code across different modules while keeping them logically separated.

---

### Updated Summary Table

| Category | Observation | Significance |
| :--- | :--- | :--- |
| **Core Architecture** | **Modular State Machine** | The binary acts as a "host" for various modules; its behavior is determined by remote commands, making it highly versatile. |
| **Execution Logic** | **Complex Branching/Indirection** | Designed to frustrate static analysis; the full scope of the malware's capabilities cannot be mapped without live C2 traffic. |
| **Stability** | **Sophisticated Error Handling** | Ensures maximum uptime and "stealthy" failures; prevents crashes that would alert a user or security software. |
| **Development Style** | **High-Level Abstraction** | Evidence of professional development (likely C++); the code is modular, organized, and highly engineered. |
| **Infrastructure** | **Steam/Game Context** | Confirms intent to hide within the gaming ecosystem by masquerading as a mod or game utility. |
| **Data Handling** | **JSON-Driven Commands** | Uses high-level data structures for communication, allowing for complex, multi-stage instruction sets from the C2. |

---

### Final Conclusion & Intelligence Synthesis

The final analysis confirms that this is not a "script kiddie" tool; it is a **sophisticated, professional-grade malware framework.** 

**Key Takeaways:**
1.  **Versatility:** It is a "Swiss Army Knife" loader. The logic found in `fcn.14001aebc` functions as a dispatcher. This allows the attackers to update what the malware *does* (e.g., change it from a downloader to an info-stealer) without ever having to re-compile or re-distribute the binary.
2.  **Evasion-Centric Design:** By using a modular architecture and indirect execution paths, the developers have ensured that standard automated analysis is unlikely to uncover all of its features at once. 
3.  **Targeted Operation:** The specific inclusion of Steam-related file checks combined with high-end networking abstractions indicates a sophisticated threat actor targeting the gaming community or utilizing game environments as a haven for their operations.

**Recommended Action:** This binary should be treated as a **High-Threat Component**. Any systems where this is found should be checked for secondary payloads, and traffic to its associated C2 infrastructure should be blocked at the perimeter. The "multi-tool" nature of the loader suggests that the presence of this file may indicate a compromise in progress or part of a larger, coordinated campaign.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The state-machine logic using "Action IDs" allows the binary to interpret different remote commands and execute specific modules (e.g., keylogging or credential theft). |
| **T1027** | Obfuscated Execution | The use of indirection layers, complex table lookups, and indirect jumps is specifically designed to hinder manual analysis and hide the logic path from static tools. |
| **T1497** | Virtualization, Sandbox, or Availability Escape | The "Environment Validation" checks ensure that the high-risk payload only executes on a physical machine rather than an automated analysis sandbox. |
| **T1036** | Masquerading | The inclusion of Steam-specific files and functionality suggests the malware is designed to blend into the gaming ecosystem as a legitimate utility or mod. |
| **T1071** | Application Layer Protocol | The use of JSON-driven data structures for multi-stage instructions indicates high-level communication over standard application protocols to facilitate complex C2 interaction. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the organized report of Indicators of Compromise (IOCs). 

**Note:** The "EXTRACTED STRINGS" section contains a high volume of obfuscated data and junk characters (e.g., `UATAUAVAWH`, `H9\$xH`) likely intended to hinder automated analysis or represent artifacts of a packer/obfuscator. These do not constitute unique, actionable IOCs like specific IPs or file paths.

### **Indicators of Compromise**

#### **IP addresses / URLs / Domains**
*   *None identified.* (The provided text contains no plaintext IP addresses or URLs).

#### **File paths / Registry keys**
*   *None identified.* (While the analysis mentions "Steam-specific targeting," no specific malicious file paths or registry keys were extracted from the strings).

#### **Mutex names / Named pipes**
*   *None identified.*

#### **Hashes**
*   *None identified.* (The string `3333333` is not a standard MD5, SHA-1, or SHA-256 hash format).

#### **Other artifacts**
*   **C2 Communication Method:** The malware utilizes **JSON-driven commands** to determine its behavior. This indicates a modular "loader" architecture where the C2 server can push different payloads (e.g., info-stealing, keylogging) to the same binary.
*   **Networking Library:** Use of `WinINet` for network communication.
*   **Target Environment:** High affinity for **Steam/Gaming infrastructure**. The malware is designed to blend into gaming environments or appear as a game mod/utility.
*   **Execution Logic Artifacts:** 
    *   Modular State Machine (identified in function `fcn.14001aebc`).
    *   Complex branching/indirect calls used to evade static analysis.
    *   Robust "Graceful Failure" logic to ensure the binary does not crash when encountering unexpected environments, thereby avoiding detection by basic sandboxes.

---

### **Analyst Summary**
The provided data describes a **sophisticated multi-functional loader**. While it lacks traditional hard IOCs (like specific IPs or file paths) in this specific snippet—likely due to the use of dynamic C2 instructions and heavy obfuscation—the behavioral artifacts indicate a high-level threat actor. 

**Recommendation:** Monitor for processes utilizing `WinINet` to fetch JSON payloads, particularly those interacting with Steam-related files/directories. Any binary exhibiting modular behavior (handling multiple "Action IDs") should be flagged as a potential downloader or loader for further memory forensics.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Modular State-Machine Architecture:** The binary utilizes a "Swiss Army Knife" design where it acts as a dispatcher for various modules (e.g., keylogging, credential theft). By using Action IDs and JSON-driven commands from a C2 server, the same binary can perform multiple distinct malicious functions without being recompiled.
*   **Sophisticated Evasion & Stability:** The code employs advanced control flow obfuscation (indirection layers), environment validation to bypass sandboxes, and "graceful failure" logic. These features are hallmarks of high-end malware designed to remain stable and undetected during automated analysis.
*   **Targeted Distribution Context:** Analysis confirms the malware specifically targets the Steam/gaming ecosystem. It is engineered to masquerade as a legitimate game utility or mod while utilizing professional-grade C++ development practices to maintain its foothold in a niche, high-traffic environment.
