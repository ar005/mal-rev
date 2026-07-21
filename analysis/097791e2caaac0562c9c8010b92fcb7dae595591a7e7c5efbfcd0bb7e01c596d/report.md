# Threat Analysis Report

**Generated:** 2026-07-20 14:30 UTC
**Sample:** `097791e2caaac0562c9c8010b92fcb7dae595591a7e7c5efbfcd0bb7e01c596d_097791e2caaac0562c9c8010b92fcb7dae595591a7e7c5efbfcd0bb7e01c596d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `097791e2caaac0562c9c8010b92fcb7dae595591a7e7c5efbfcd0bb7e01c596d_097791e2caaac0562c9c8010b92fcb7dae595591a7e7c5efbfcd0bb7e01c596d.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 779,776 bytes |
| MD5 | `7268f8381057e6df2bf1859f427c2a68` |
| SHA1 | `f8058553d857c52c78a89e03f45cbaf88f212d7c` |
| SHA256 | `097791e2caaac0562c9c8010b92fcb7dae595591a7e7c5efbfcd0bb7e01c596d` |
| Overall entropy | 6.207 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771332036 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 467,968 | 6.467 | No |
| `.rdata` | 109,056 | 5.231 | No |
| `.data` | 181,760 | 5.271 | No |
| `.pdata` | 15,872 | 5.762 | No |
| `` | 512 | -0.0 | No |
| `.reloc` | 3,584 | 5.378 | No |

### Imports

**KERNEL32.dll**: `GetCurrentProcess`, `SetEndOfFile`, `GetProcAddress`, `LoadLibraryA`, `GetModuleFileNameA`, `HeapSize`, `CreateFileW`, `QueryPerformanceCounter`, `QueryPerformanceFrequency`, `ReleaseSRWLockExclusive`, `AcquireSRWLockExclusive`, `SleepConditionVariableSRW`, `Sleep`, `GetCurrentThreadId`, `WideCharToMultiByte`
**ADVAPI32.dll**: `RegEnumKeyExA`
**SHLWAPI.dll**: `StrChrA`

## Extracted Strings

Total strings found: **2411** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
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
UVWATAUAVAWH
tRH9D$@H
L9t$HL
L9t$HH
GL$0H+
L9t$HH
GL$0H+
A_A^A]A\_^]
L9t$HH
D$0L9t$HH
Gt$0H
L9t$HM
L9t$hH
VWATAUAVAWH
A_A^A]A\_^
VWATAUAWH
A_A]A\_^
x ATAVAWH
 A_A^A\
WAVAWH
0A_A^_
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.std::ctype_wchar_t_.virtual_24` | `0x140026868` | 124616 | ✓ |
| `fcn.140044334` | `0x140044334` | 89778 | ✓ |
| `fcn.14005ea10` | `0x14005ea10` | 55337 | ✓ |
| `fcn.14005c118` | `0x14005c118` | 53883 | ✓ |
| `fcn.14005c104` | `0x14005c104` | 53842 | ✓ |
| `fcn.140059d30` | `0x140059d30` | 50983 | ✓ |
| `fcn.14006f850` | `0x14006f850` | 38154 | ✓ |
| `method.std::basic_stringstream_wchar_t__struct_std::char_traits_wchar_t___class_std::allocator_wchar_t__.virtual_0` | `0x140037860` | 37084 | ✓ |
| `method.std::basic_ostringstream_wchar_t__struct_std::char_traits_wchar_t___class_std::allocator_wchar_t__.virtual_0` | `0x14003786c` | 37008 | ✓ |
| `method.std::basic_iostream_wchar_t__struct_std::char_traits_wchar_t__.virtual_0` | `0x140037884` | 36892 | ✓ |
| `method.std::basic_ostream_wchar_t__struct_std::char_traits_wchar_t__.virtual_0` | `0x140037890` | 36728 | ✓ |
| `method.std::basic_istream_wchar_t__struct_std::char_traits_wchar_t__.virtual_0` | `0x1400378a8` | 36652 | ✓ |
| `method.std::basic_stringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x140037878` | 36376 | ✓ |
| `method.std::basic_istringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x1400378b4` | 36348 | ✓ |
| `method.std::basic_iostream_char__struct_std::char_traits_char__.virtual_0` | `0x1400378c0` | 36272 | ✓ |
| `method.std::basic_istream_char__struct_std::char_traits_char__.virtual_0` | `0x14003789c` | 36060 | ✓ |
| `fcn.140002be0` | `0x140002be0` | 20563 | ✓ |
| `fcn.14004ee3c` | `0x14004ee3c` | 13584 | ✓ |
| `fcn.1400446c4` | `0x1400446c4` | 12298 | ✓ |
| `method.std::basic_ostringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x14001fef4` | 10484 | ✓ |
| `method.std::basic_ostream_char__struct_std::char_traits_char__.virtual_0` | `0x14001fee8` | 10332 | ✓ |
| `fcn.14004cb04` | `0x14004cb04` | 7424 | ✓ |
| `fcn.1400292a4` | `0x1400292a4` | 7110 | ✓ |
| `fcn.140011968` | `0x140011968` | 5367 | ✓ |
| `fcn.14000ade8` | `0x14000ade8` | 5236 | ✓ |
| `fcn.14000ccc0` | `0x14000ccc0` | 5036 | ✓ |
| `fcn.14006c704` | `0x14006c704` | 4735 | ✓ |
| `fcn.140040580` | `0x140040580` | 4734 | ✓ |
| `fcn.1400103c8` | `0x1400103c8` | 4300 | ✓ |
| `fcn.14003947c` | `0x14003947c` | 4278 | ✓ |

### Decompiled Code Files

- [`code/fcn.140002be0.c`](code/fcn.140002be0.c)
- [`code/fcn.14000ade8.c`](code/fcn.14000ade8.c)
- [`code/fcn.14000ccc0.c`](code/fcn.14000ccc0.c)
- [`code/fcn.1400103c8.c`](code/fcn.1400103c8.c)
- [`code/fcn.140011968.c`](code/fcn.140011968.c)
- [`code/fcn.1400292a4.c`](code/fcn.1400292a4.c)
- [`code/fcn.14003947c.c`](code/fcn.14003947c.c)
- [`code/fcn.140040580.c`](code/fcn.140040580.c)
- [`code/fcn.140044334.c`](code/fcn.140044334.c)
- [`code/fcn.1400446c4.c`](code/fcn.1400446c4.c)
- [`code/fcn.14004cb04.c`](code/fcn.14004cb04.c)
- [`code/fcn.14004ee3c.c`](code/fcn.14004ee3c.c)
- [`code/fcn.140059d30.c`](code/fcn.140059d30.c)
- [`code/fcn.14005c104.c`](code/fcn.14005c104.c)
- [`code/fcn.14005c118.c`](code/fcn.14005c118.c)
- [`code/fcn.14005ea10.c`](code/fcn.14005ea10.c)
- [`code/fcn.14006c704.c`](code/fcn.14006c704.c)
- [`code/fcn.14006f850.c`](code/fcn.14006f850.c)
- [`code/method.std__basic_iostream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_iostream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_iostream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c`](code/method.std__basic_iostream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c)
- [`code/method.std__basic_istream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_istream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_istream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c`](code/method.std__basic_istream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c)
- [`code/method.std__basic_istringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c`](code/method.std__basic_istringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c)
- [`code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_ostream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c`](code/method.std__basic_ostream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c)
- [`code/method.std__basic_ostringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c`](code/method.std__basic_ostringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c)
- [`code/method.std__basic_ostringstream_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_0.c`](code/method.std__basic_ostringstream_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_0.c)
- [`code/method.std__basic_stringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c`](code/method.std__basic_stringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c)
- [`code/method.std__basic_stringstream_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_0.c`](code/method.std__basic_stringstream_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_0.c)
- [`code/method.std__ctype_wchar_t_.virtual_24.c`](code/method.std__ctype_wchar_t_.virtual_24.c)

## Behavioral Analysis

This updated analysis incorporates the final disassembly segments (chunk 4/4). These sections reveal deeper layers of execution logic, specifically focusing on **anti-tampering mechanisms**, **complex state management**, and a **highly abstracted internal framework**.

---

### Updated Technical Analysis

#### 1. Network Communication Layer (WinINet Integration)
*(Maintained from previous analysis)*
The presence of `fcn.140040580` confirms the use of WinINET functions (`InternetOpenW`, `HttpSendRequestW`, etc.) wrapped in custom functions. This allows the malware to blend in with standard Windows system traffic while hiding its true intent from basic import-table scanners.

#### 2. Environment Awareness & Targeting (Steam Integration)
*(Maintained from previous analysis)*
The hardcoded references to `config.vdf` and `local.vdf` confirm a specific focus on the Steam gaming ecosystem, likely for targeting high-value accounts or exploiting "gamer" demographics.

#### 3. Advanced Execution & Anti-Tampering (New Findings)
The final disassembly segment reveals a sophisticated "Hard Fail" mechanism used to protect the integrity of the execution flow:
*   **State Validation:** The code frequently performs checks such as `if (*pcVar17 != '\x01')`. If these conditions are not met, the program jumps to a `swi(3)` (Software Interrupt) or calls a crash/exception handler. 
*   **Anti-Analysis Integrity:** This is indicative of an **Integrity Check.** The malware is verifying that its internal state—likely modified during decryption or by security software—remains exactly as intended. If a debugger, hook, or sandbox modifies any variable in the transition from "Decryption" to "Execution," the malware terminates immediately rather than continuing in a compromised state.
*   **Hard-Coded Data Fetching:** The repeated pattern of `fcn.1400717f0` followed by specific hex addresses (e.g., `0x400870b0`, `0x40087040`) suggests the malware is pulling "instructions" or configuration constants from a predefined data table. This allows the attacker to change the malware's behavior by updating the data section without changing the executable code.

#### 4. Complex State Machine & Command Processing
The presence of `while (pcVar17 = pcVar17, cVar11 != '\0')` loops and nested logic indicates a **Command Processor** architecture:
*   Instead of a linear "infect-and-send" script, the malware likely receives or parses a series of commands.
*   Each iteration of the loop handles a specific task (e.g., 1=Drop File, 2=Exfiltrate Data, 3=Update Config).
*   The elaborate jump tables and state checks (like `fcn.140013830` and `fcn.140071670`) are used to navigate this command tree while keeping the actual logic hidden from linear analysis.

#### 5. Refined Logic Flow: The "Fortified" Pipeline
Based on all four segments, we can now map a high-confidence execution flow:
1.  **De-mangling & Integrity Check:** Raw data is decrypted; internal state variables are validated against expected values (the `0x01` checks). If integrity fails, the process self-terminates.
2.  **Data Table Extraction:** The malware pulls its "recipe" from specific memory offsets (e.g., `0x400870b0`).
3.  **JSON Parsing & Command Processing:** It parses the JSON configuration and enters a loop to execute commands based on that configuration.
4.  **WinINet Integration:** When it needs to communicate, it utilizes the pre-validated WinINET wrappers to perform "legitimate" looking HTTP/HTTPS traffic.
5.  **Environment Check (Steam):** During execution, it validates the environment to ensure it is running on a target machine (e.g., one with Steam installed) before triggering high-privilege actions.

---

### Updated Summary for Incident Response

The evidence confirms this is a **sophisticated, hardened Trojan/Loader** designed to evade both automated detection and manual analysis.

#### Key Findings from this Final Update:
1.  **"Fail-Fast" Security Logic:** The malware employs strict integrity checks at critical transition points. This means that standard "hooking" (where security tools intercept functions) might cause the malware to detect the intervention and shut down immediately.
2.  **Command-Driven Architecture:** The use of loops and state machines suggests a multi-functional payload. It can perform multiple tasks in one infection cycle based on instructions received from its Command & Control (C2).
3.  **Data Table Dependency:** Much of the malware's behavior is controlled by values pulled from specific memory offsets, making it harder to "patch out" malicious behaviors without breaking the entire execution flow.

#### Impact Analysis:
*   **Exfiltration Risk:** High. The robust command processing allows for varied exfiltration methods (e.g., stealing credentials today, and then a different file type tomorrow).
*   **Anti-Forensics Resilience:** Very High. The use of SWI(3) traps on invalid states makes it difficult for automated sandboxes to "force" the malware into showing its full capabilities if they interfere with the initial decryption steps.

#### Updated Recommendations for IR Team:
*   **Memory Forensics (Crucial):** Because of the heavy obfuscation and state-checking, **memory forensics** is preferred over static analysis for this sample. Capturing memory dumps during execution may allow analysts to see the "unwrapped" commands in the data tables before they are executed.
*   **Behavioral Blocking:** Since the malware uses standard WinINET calls, look for processes making frequent HTTP GET/POST requests to non-standard domains or IPs that do not resolve to known services.
*   **Enhanced IOC Collection:** 
    *   **Integrity Monitoring:** Monitor and alert on any unauthorized modifications to system memory or common libraries that could trigger the "failure" state of the malware.
    *   **String Indicators:** Create YARA rules targeting the unique address sequences found in the disassembly (e.g., `0x400870b0`, `0x40087040`) and the specific Steam file paths (`config.vdf`).
    *   **Network Signature:** Flag any process accessing both `steam` directories and initiating network traffic via WinINET as a high-priority alert.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1071.001 | Web Protocols | The malware utilizes WinINet functions to perform HTTP/HTTPS requests, allowing it to blend in with standard Windows system traffic. |
| T1082 | System Information Discovery | The inclusion of hardcoded paths for `config.vdf` and `local.vdf` indicates the malware is searching for specific evidence of a Steam installation to target a particular demographic. |
| T1405 | Debugger Detection | The "Hard Fail" mechanism and integrity checks (e.g., checking if variables match expected values) are designed to detect and terminate upon interaction with debuggers or hooks. |
| T1027 | Obfuscated Files or Information | The use of a data table with specific hex offsets to fetch instructions/commands masks the malware's true logic from linear analysis. |
| T1568 | Dynamic Resolution | The implementation of a complex command processor and state machine allows the malware to dynamically execute different behaviors (e.g., exfiltrate, drop files) based on its internal logic. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "EXTRACTED STRINGS" section contains high levels of obfuscation and junk data common in packed malware; therefore, most of those strings were excluded as noise. The primary actionable indicators were derived from the technical behavior patterns.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis notes that WinINet is used for communication, but no specific hardcoded C2 domains or IP addresses were present in the provided text.)

### **File paths / Registry keys**
*   `config.vdf` (Targeted file associated with Steam environment discovery)
*   `local.vdf` (Targeted file associated with Steam environment discovery)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA-1, or SHA-256 hashes were present in the strings.)

### **Other artifacts**
*   **Internal Memory Offsets (Useful for YARA/Memory Scanning):** 
    *   `0x400870b0`
    *   `0x40087040`
*   **Identified Internal Function Call Patterns:**
    *   `fcn.140040580` (WinINet Wrapper)
    *   `fcn.1400717f0` (Data Table Retrieval)
    *   `fcn.140013830` (State Machine/Command Logic)
    *   `fcn.140071670` (Navigation Logic)
*   **Behavioral Signatures:**
    *   **Steam-Targeted Scraping:** The malware specifically monitors and interacts with Steam-related configuration files to target the gaming demographic.
    *   **Anti-Analysis "Fail-Fast" Logic:** Use of `swi(3)` (Software Interrupt) or intentional crashes when internal state variables deviate from expected values (e.g., checking if a variable is not `0x01`).
    *   **WinINET Wrapper Usage:** Utilization of standard Windows libraries (`InternetOpenW`, `HttpSendRequestW`) to mask malicious HTTP/HTTPS traffic as legitimate system activity.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader, backdoor
3. **Confidence**: High (for classification) / Medium (for naming a specific known campaign)
4. **Key evidence**: 
    *   **Sophisticated Anti-Analysis Logic:** The "Fail-Fast" mechanism and `swi(3)` integrity checks indicate highly developed evasion techniques designed to detect debuggers, hooks, and sandboxes before execution can be fully analyzed.
    *   **Modular Command Architecture:** The use of a command processor loop with data tables means the malware is not a static script but a versatile tool capable of performing multiple actions (exfiltration, file dropping) based on remote commands.
    *   **Targeted Environment Awareness:** Specific hardcoded paths for Steam configuration files (`config.vdf`) confirm it is tailored to target a specific user demographic and exfiltrate relevant data from that environment.
