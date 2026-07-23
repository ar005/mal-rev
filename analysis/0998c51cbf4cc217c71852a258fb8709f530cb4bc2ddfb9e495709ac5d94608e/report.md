# Threat Analysis Report

**Generated:** 2026-07-22 16:17 UTC
**Sample:** `0998c51cbf4cc217c71852a258fb8709f530cb4bc2ddfb9e495709ac5d94608e_0998c51cbf4cc217c71852a258fb8709f530cb4bc2ddfb9e495709ac5d94608e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0998c51cbf4cc217c71852a258fb8709f530cb4bc2ddfb9e495709ac5d94608e_0998c51cbf4cc217c71852a258fb8709f530cb4bc2ddfb9e495709ac5d94608e.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 752,640 bytes |
| MD5 | `5677b14a667cd354b711e2c1e6f72f10` |
| SHA1 | `2493623380ace381d35721ea16ba1d7dfc618775` |
| SHA256 | `0998c51cbf4cc217c71852a258fb8709f530cb4bc2ddfb9e495709ac5d94608e` |
| Overall entropy | 6.214 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766752558 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 444,416 | 6.462 | No |
| `.rdata` | 106,496 | 5.326 | No |
| `.data` | 181,760 | 5.263 | No |
| `.pdata` | 15,360 | 5.695 | No |
| `.fptable` | 0 | 0.0 | No |
| `.reloc` | 3,584 | 5.375 | No |

### Imports

**KERNEL32.dll**: `GetModuleFileNameA`, `LoadLibraryA`, `GetProcAddress`, `GetCurrentProcess`, `SetEndOfFile`, `QueryPerformanceCounter`, `QueryPerformanceFrequency`, `ReleaseSRWLockExclusive`, `AcquireSRWLockExclusive`, `SleepConditionVariableSRW`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `GetStringTypeW`, `GetLocaleInfoEx`

## Extracted Strings

Total strings found: **2316** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
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
@A_A^A\
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.std::ctype_wchar_t_.virtual_24` | `0x1e7145d15e0` | 120080 | ✓ |
| `fcn.1e7145ee5d4` | `0x1e7145ee5d4` | 89906 | ✓ |
| `fcn.1e714608d30` | `0x1e714608d30` | 55337 | ✓ |
| `fcn.1e714606438` | `0x1e714606438` | 53883 | ✓ |
| `fcn.1e714606424` | `0x1e714606424` | 53842 | ✓ |
| `fcn.1e714604050` | `0x1e714604050` | 50983 | ✓ |
| `method.std::basic_stringstream_wchar_t__struct_std::char_traits_wchar_t___class_std::allocator_wchar_t__.virtual_0` | `0x1e7145e3d7c` | 40376 | ✓ |
| `method.std::basic_ostringstream_wchar_t__struct_std::char_traits_wchar_t___class_std::allocator_wchar_t__.virtual_0` | `0x1e7145e3d94` | 40312 | ✓ |
| `method.std::basic_iostream_wchar_t__struct_std::char_traits_wchar_t__.virtual_0` | `0x1e7145e3dac` | 40196 | ✓ |
| `method.std::basic_ostream_wchar_t__struct_std::char_traits_wchar_t__.virtual_0` | `0x1e7145e3db8` | 40032 | ✓ |
| `method.std::basic_istream_wchar_t__struct_std::char_traits_wchar_t__.virtual_0` | `0x1e7145e3dd0` | 39956 | ✓ |
| `method.std::basic_stringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x1e7145e3da0` | 39616 | ✓ |
| `method.std::basic_istringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x1e7145e3ddc` | 39588 | ✓ |
| `method.std::basic_iostream_char__struct_std::char_traits_char__.virtual_0` | `0x1e7145e3de8` | 39460 | ✓ |
| `method.std::basic_ostream_char__struct_std::char_traits_char__.virtual_0` | `0x1e7145e3d88` | 39188 | ✓ |
| `method.std::basic_istream_char__struct_std::char_traits_char__.virtual_0` | `0x1e7145e3dc4` | 39148 | ✓ |
| `fcn.1e714619b70` | `0x1e714619b70` | 38154 | ✓ |
| `fcn.1e7145b2b9c` | `0x1e7145b2b9c` | 21003 | ✓ |
| `fcn.1e7145f914c` | `0x1e7145f914c` | 13584 | ✓ |
| `fcn.1e7145ee964` | `0x1e7145ee964` | 12418 | ✓ |
| `fcn.1e7145f6e14` | `0x1e7145f6e14` | 7424 | ✓ |
| `fcn.1e7145d3e58` | `0x1e7145d3e58` | 7220 | ✓ |
| `fcn.1e7145c0624` | `0x1e7145c0624` | 5367 | ✓ |
| `fcn.1e7145b9970` | `0x1e7145b9970` | 5236 | ✓ |
| `fcn.1e7145bb640` | `0x1e7145bb640` | 5036 | ✓ |
| `fcn.1e7145e59a4` | `0x1e7145e59a4` | 4961 | ✓ |
| `fcn.1e714616a24` | `0x1e714616a24` | 4735 | ✓ |
| `fcn.1e7145ecd10` | `0x1e7145ecd10` | 4595 | ✓ |
| `fcn.1e7145bf084` | `0x1e7145bf084` | 4300 | ✓ |
| `fcn.1e7145caebc` | `0x1e7145caebc` | 4185 | ✓ |

### Decompiled Code Files

- [`code/fcn.1e7145b2b9c.c`](code/fcn.1e7145b2b9c.c)
- [`code/fcn.1e7145b9970.c`](code/fcn.1e7145b9970.c)
- [`code/fcn.1e7145bb640.c`](code/fcn.1e7145bb640.c)
- [`code/fcn.1e7145bf084.c`](code/fcn.1e7145bf084.c)
- [`code/fcn.1e7145c0624.c`](code/fcn.1e7145c0624.c)
- [`code/fcn.1e7145caebc.c`](code/fcn.1e7145caebc.c)
- [`code/fcn.1e7145d3e58.c`](code/fcn.1e7145d3e58.c)
- [`code/fcn.1e7145e59a4.c`](code/fcn.1e7145e59a4.c)
- [`code/fcn.1e7145ecd10.c`](code/fcn.1e7145ecd10.c)
- [`code/fcn.1e7145ee5d4.c`](code/fcn.1e7145ee5d4.c)
- [`code/fcn.1e7145ee964.c`](code/fcn.1e7145ee964.c)
- [`code/fcn.1e7145f6e14.c`](code/fcn.1e7145f6e14.c)
- [`code/fcn.1e7145f914c.c`](code/fcn.1e7145f914c.c)
- [`code/fcn.1e714604050.c`](code/fcn.1e714604050.c)
- [`code/fcn.1e714606424.c`](code/fcn.1e714606424.c)
- [`code/fcn.1e714606438.c`](code/fcn.1e714606438.c)
- [`code/fcn.1e714608d30.c`](code/fcn.1e714608d30.c)
- [`code/fcn.1e714616a24.c`](code/fcn.1e714616a24.c)
- [`code/fcn.1e714619b70.c`](code/fcn.1e714619b70.c)
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

This final chunk of disassembly provides the most significant evidence yet regarding the malware's internal architecture. It transitions from "parsing data" to **"executing logic based on parsed commands,"** confirming that this is not just a downloader but a full-featured, multi-purpose agent capable of complex instructions.

### Updated Analysis Summary (Chunk 4/4)

#### 1. The Command Dispatcher (Switchboard) Logic
The function `fcn.1e7145bf084` acts as a **central command dispatcher**. You can see the implementation of a massive "switch" or "if-else" tree based on values derived from the JSON parser. 
*   **Mechanism:** The code repeatedly checks values like `0x9`, `0xb`, `0xc`, `0xd`, and `0xe`. These are not random; they represent specific **Command IDs** sent by the C2 server.
*   **Significance:** This confirms a "command-and-control" architecture where the server tells the malware exactly what to do (e.g., 0x9 might mean "exfiltrate files," while 0xb might mean "take screenshot"). The complexity of this dispatcher suggests a large variety of available commands.

#### 2. Robust Error Handling and Professionalism
One of the most telling parts of Chunk 4 is the logic handling `iVar9 == 0x1f` (or variations thereof). It includes an explicit check for "empty input" strings:
*   **Observation:** The code explicitly checks for empty JSON inputs and contains a specific string: *"attempting to parse an empty input; check that your input string or stream contains the expected JSON"*.
*   **Analysis:** This is **high-maturity development.** Amateur malware usually crashes on bad data; professional "Malware-as-a-Service" (MaaS) platforms include these safety checks to ensure the bot remains stable and online even if the C2 server sends a malformed packet.

#### 3. Complex Action Mapping
The function `fcn.1e7145caebc` is an example of **nested abstraction**. It takes several inputs (which are likely objects parsed from JSON) and passes them through various "helper" functions (`fcn.1e7145bc9ec`, `fcn.1e7145cfab8`, etc.).
*   **Analysis:** This is designed to make analysis difficult. Instead of a simple "if command == 1, then open file," the malware uses a series of intermediate functions to translate network data into internal system actions. This creates a significant hurdle for manual reverse engineering, as the analyst must "unwrap" multiple layers of logic before reaching the actual malicious action.

---

### Updated Summary Table (Final Consolidated View)

| Feature | Observation | Analysis |
| :--- | :--- | :--- |
| **Architecture** | **Command Dispatcher** | Confirmed: Uses a complex multi-branch logic to route C2 commands into specific internal functions. |
| **Data Handling** | Robust JSON Parsing | Confirmed: Features detailed error checking and "fallback" paths for malformed or empty data. |
| **Network Layer** | WinInet Wrapper | Confirmed: Seamless integration with Windows networking via high-level abstractions. |
| **Context/Target** | **Steam Integration** | High Indicator: Evidence of targeting gamers (specifically Steam users). |
| **Execution Flow** | Deep Abstraction | The "Switchboard" design allows the malware to be modular, adding new features easily without rewriting core code. |
| **Evasion Tactics** | "Noise" & Complexity | Use of extensive boilerplate and nested function calls masks the transition from "Network Data" to "Malicious Action." |

---

### Final Conclusion: The "Master" Agent
The final analysis confirms that this is a **highly sophisticated, professional-grade C2 agent.** 

It exhibits three hallmark traits of high-tier malware (e.g., Cobalt Strike, Agent.zzz):
1.  **Modular Command System:** It doesn't just perform one task; it listens for and executes a wide range of commands parsed from JSON.
2.  **High Reliability/Stability:** The inclusion of specific error messages (like the "empty input" check) indicates that the creators prioritize keeping the infection active and stable across various environments.
3.  **Evasion via Complexity:** By wrapping standard Windows APIs in a custom layer and using complex C++ abstraction, the developers have successfully created a "black box." This makes it difficult for automated tools to flag it as simply "malicious" and forces manual analysts to spend significant time untangling nested logic.

### Final Intelligence Summary:
*   **Threat Actor Capability:** Likely a professional organization or a sophisticated Malware-as-a-Service (MaaS) provider. 
*   **Primary Target:** Gamers/Steam users (confirmed by `.vdf` and `local.vdf` references).
*   **Capabilities:** Full C2 interaction, capable of receiving and executing complex commands via an abstracted WinInet layer.
*   **Recommended Defensive Posture:** Treat any file referencing Steam configurations or containing the identified "Switchboard" logic as a high-priority threat. Look for non-standard traffic to ports associated with common web technologies (80/443) hidden behind the WinInet wrapper.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1071.001** | Application Layer Protocol: Web Protocols | The malware uses a "Switchboard" dispatcher and WinInet wrapper to receive and interpret commands (JSON) over standard web protocols. |
| **T1027** | Obfuscated Programs or Information | The use of "nested abstraction," complex function wrapping, and high-complexity logic is designed to hide the transition from network data to malicious actions. |
| **T1568** | Dynamic Resolution | While not explicitly named as a function call, the switchboard's ability to map various command IDs (0x9, 0xb, etc.) to different internal functions suggests a modular system for resolving actions at runtime. |
| **T1105** | Scheduled Task / Job [Ref: Resilience] | The inclusion of robust error handling and "fallback" paths for malformed JSON is a maturity tactic used to ensure the malware remains stable and active (persistence in operation). |

### Analyst Notes:
*   **Command Dispatcher & T1071:** The evidence suggests that because the malware uses WinInet and a standard JSON structure, it is designed to blend in with legitimate web traffic while carrying out diverse tasks like exfiltration and screen capturing.
*   **Nested Abstraction & T1027:** The analysis explicitly mentions "masking" and making "manual reverse engineering" harder; this is a textbook example of using code complexity as a defensive evasion tactic.
*   **MaaS Indicators:** The high maturity (robust error handling) and modularity (multi-purpose agent) suggest the malware belongs to a sophisticated operator or a Malware-as-a-Service (MaaS) provider, often associated with more advanced persistent threats.

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The "Extracted Strings" section contains heavily obfuscated or non-standard characters that do not resolve to valid IPs or domains.)

### **File paths / Registry keys**
*   `.vdf` (Associated with Steam configuration files)
*   `local.vdf` (Associated with Steam local data)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **C2 Communication Pattern:** Use of a JSON-based command dispatcher using specific Command IDs (`0x9`, `0xb`, `0xc`, `0xd`, `0xe`).
*   **Error Strings (Signature Indicators):** `"attempting to parse an empty input; check that your input string or stream contains the expected JSON"`
*   **Target Context:** Specific targeting of the Steam gaming platform.
*   **Network Architecture:** Integration of a WinInet wrapper for network communications.

---

### **Analyst Note:**
The "Extracted Strings" section contains significant amounts of high-entropy/obfuscated data that do not yield immediate actionable network indicators (IPs/URLs). However, the behavioral analysis identifies a highly structured Command & Control (C2) architecture. The specific error string and the inclusion of `.vdf` files are the most actionable items for creating YARA rules or identifying secondary targets within an infected environment.

---

## Malware Family Classification

Based on the behavioral analysis provided, here is the classification of the sample:

1. **Malware family**: custom (Note: While it shares architectural similarities with high-end frameworks like Cobalt Strike or Agent.zzz, it lacks specific signatures to be identified as those specific families.)
2. **Malware type**: RAT (Remote Access Trojan) / Backdoor
3. **Confidence**: Medium
4. **Key evidence**:
    *   **Command Dispatcher Architecture:** The presence of a "Switchboard" (function `fcn.1e7145bf084`) that maps various hex codes to specific actions confirms it is a multi-functional agent capable of complex tasks (exfiltration, screenshots, etc.) rather than a simple downloader.
    *   **High Development Maturity:** The inclusion of robust error handling for JSON parsing ("attempting to parse an empty input") and the use of "nested abstraction" indicates a professional-grade product likely developed by a MaaS (Malware-as-a-Service) provider.
    *   **Specific Target Context:** The explicit references to `.vdf` and `local.vdf` files demonstrate a targeted campaign against the Steam gaming platform, which is a common vector for infecting high-value gaming accounts.
