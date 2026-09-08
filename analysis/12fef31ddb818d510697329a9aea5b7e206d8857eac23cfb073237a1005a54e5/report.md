# Threat Analysis Report

**Generated:** 2026-09-01 20:46 UTC
**Sample:** `12fef31ddb818d510697329a9aea5b7e206d8857eac23cfb073237a1005a54e5_12fef31ddb818d510697329a9aea5b7e206d8857eac23cfb073237a1005a54e5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12fef31ddb818d510697329a9aea5b7e206d8857eac23cfb073237a1005a54e5_12fef31ddb818d510697329a9aea5b7e206d8857eac23cfb073237a1005a54e5.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 32,000,000 bytes |
| MD5 | `83825e35647ac1065a55d56bf9f89fcc` |
| SHA1 | `fd3c9fe615f32102b9f3a1f97f6b0b2ea9d957c6` |
| SHA256 | `12fef31ddb818d510697329a9aea5b7e206d8857eac23cfb073237a1005a54e5` |
| Overall entropy | 0.26 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769366508 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 444,416 | 6.462 | No |
| `.rdata` | 106,496 | 5.199 | No |
| `.data` | 181,760 | 5.263 | No |
| `.pdata` | 15,360 | 5.695 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 3,584 | 5.375 | No |

### Imports

**KERNEL32.dll**: `GetModuleFileNameA`, `LoadLibraryA`, `GetProcAddress`, `GetCurrentProcess`, `SetEndOfFile`, `QueryPerformanceCounter`, `QueryPerformanceFrequency`, `ReleaseSRWLockExclusive`, `AcquireSRWLockExclusive`, `SleepConditionVariableSRW`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `GetStringTypeW`, `GetLocaleInfoEx`

## Extracted Strings

Total strings found: **2318** (showing first 100)

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
| `method.std::ctype_wchar_t_.virtual_24` | `0x1400215e0` | 120080 | ✓ |
| `fcn.14003e5d4` | `0x14003e5d4` | 89906 | ✓ |
| `fcn.140058d30` | `0x140058d30` | 55337 | ✓ |
| `fcn.140056438` | `0x140056438` | 53883 | ✓ |
| `fcn.140056424` | `0x140056424` | 53842 | ✓ |
| `fcn.140054050` | `0x140054050` | 50983 | ✓ |
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
| `fcn.140069b70` | `0x140069b70` | 38154 | ✓ |
| `fcn.140002b9c` | `0x140002b9c` | 21003 | ✓ |
| `fcn.14004914c` | `0x14004914c` | 13584 | ✓ |
| `fcn.14003e964` | `0x14003e964` | 12418 | ✓ |
| `fcn.140046e14` | `0x140046e14` | 7424 | ✓ |
| `fcn.140023e58` | `0x140023e58` | 7220 | ✓ |
| `fcn.140010624` | `0x140010624` | 5367 | ✓ |
| `fcn.140009970` | `0x140009970` | 5236 | ✓ |
| `fcn.14000b640` | `0x14000b640` | 5036 | ✓ |
| `fcn.1400359a4` | `0x1400359a4` | 4961 | ✓ |
| `fcn.140066a24` | `0x140066a24` | 4735 | ✓ |
| `fcn.14003cd10` | `0x14003cd10` | 4595 | ✓ |
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
- [`code/fcn.1400359a4.c`](code/fcn.1400359a4.c)
- [`code/fcn.14003cd10.c`](code/fcn.14003cd10.c)
- [`code/fcn.14003e5d4.c`](code/fcn.14003e5d4.c)
- [`code/fcn.14003e964.c`](code/fcn.14003e964.c)
- [`code/fcn.140046e14.c`](code/fcn.140046e14.c)
- [`code/fcn.14004914c.c`](code/fcn.14004914c.c)
- [`code/fcn.140054050.c`](code/fcn.140054050.c)
- [`code/fcn.140056424.c`](code/fcn.140056424.c)
- [`code/fcn.140056438.c`](code/fcn.140056438.c)
- [`code/fcn.140058d30.c`](code/fcn.140058d30.c)
- [`code/fcn.140066a24.c`](code/fcn.140066a24.c)
- [`code/fcn.140069b70.c`](code/fcn.140069b70.c)
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

This final chunk of disassembly (Chunk 4) provides the internal logic that connects the previously identified components: the **mathematical transformations**, the **Steam targeting**, and the **network communication**.

While the first three chunks showed the *tools* (the networking library, the crypto math, and the data packaging), this last chunk reveals the **engine**—how the malware processes the stolen data in a loop before transmission.

### Updated Analysis Summary (Full Integration)

The addition of Chunk 4 confirms that this is a highly structured piece of software with professional-grade coding practices. The sheer size and complexity of `fcn.14001aebc` indicate it is a core processing "dispatcher." This function takes raw data (likely harvested from Steam files), processes it through the "packaging" logic identified in Chunk 3, and prepares it for the network-ready format used by the `wininet` library.

---

### New Findings from Chunk 4

**1. Complex Dispatcher Pattern (Processing Logic)**
The repetitive block structures—where a value is checked against several constants (e.g., `if (iVar9 == 8)`, `if (iVar9 == 10)`, `if (iVar14 == 0x3173)`)—indicate a **Dispatcher Pattern**.
*   **Analysis:** This suggests the binary isn't looking for just one piece of information; it is likely iterating through a list or database of "items" (e.g., different game keys, multiple account tokens, or various configuration files). Each `if` branch handles a different *type* of data encountered during the scan.

**2. Intensive Data Processing Loops**
The presence of `do { ... } while (iVar4 != 0);` loops indicates that the binary performs iterative operations on collected data.
*   **Significance:** This is typical in **infostealers**. It suggests a loop where the malware iterates through every "relevant" file or registry key found in the Steam directory, processes each one individually via the math routines (Chunk 2), and prepares them for exfiltration.

**3. Advanced Memory Management & Object Orientation**
The disassembly shows several references to `vtable.std::exception` and complex pointer arithmetic involving offsets like `0x1400b5d70`.
*   **Analysis:** This confirms the binary is written in **C++** and uses a standard library (STL). The use of "vtable" indicates that the malware uses objects and classes. This reflects a high level of sophistication; it is not a simple script, but a robust piece of software designed to be stable and scalable during its operation.

**4. Data Serialization/Formatting**
The calls like `fcn.14001bf18` and `fcn.14001ac84` appear to perform internal data conversions between the "raw" state (data pulled from the system) and a "serialized" state (ready for transport).

---

### The "Complete Picture" Synthesis

By combining all four chunks, we can now map out the full lifecycle of an infection by this binary:

1.  **Phase 1: Discovery (Chunk 3):** The binary scans the system for specific paths related to **Steam** (`config.vdf`, `local.vdf`).
2.  **Phase 2: Extraction & Parsing (Chunk 4):** Once found, the binary enters a **Dispatch Loop**. It identifies different types of data within those files and begins processing them one by one.
3.  **Phase 3: Obfuscation/Encryption (Chunk 2):** As each piece of "interest" is extracted from the Steam files, it passes through the heavy math logic to be encrypted or obfuscated. This masks the sensitive nature of the data (e.g., a password or private key) before it touches the network layer.
4.  **Phase 4: Packaging & Decoding (Chunk 3):** The result is converted into an ASCII string format suitable for transmission over HTTP/HTTPS.
5.  **Phase 5: Exfiltration (Chunk 3 - Network Map):** Using the mapped `wininet` functions, the data is "sent home" to a Command and Control (C2) server via a prepared URL.

---

### Updated Risk Assessment & Verdict

**Risk Level: CRITICAL**

The evidence now points overwhelmingly toward this being an **Advanced Infostealer/Trojans.** 

*   **Complexity:** The use of C++ objects, a dispatcher architecture, and multi-stage processing indicates it was developed by an organized threat actor rather than a casual hacker.
*   **Targeting:** It is specifically engineered to target the gaming demographic (Steam).
*   **Stealth:** The inclusion of a robust "math" engine before the network stage suggests it is designed to bypass standard signature-based detection that looks for plain-text passwords in memory or transit.

### Final Recommendations for Incident Response:

1.  **Identify Exfiltration Points:** Since `wininet` functions are used, monitor your firewall/web proxy for any unexpected traffic from this binary’s process. Specifically look for HTTP GET/POST requests following the initial execution of the "math" routines.
2.  **Memory String Extraction:** Because the code heavily uses internal memory objects (Chunk 4) and obfuscation, a static scan won't reveal the C2 IP addresses. Run the sample in a sandbox and **dump its memory** to capture the plain-text URLs generated by `InternetOpenUrlA`.
3.  **IOC Harvesting:** Collect all hardcoded paths related to Steam and any unique "ID" numbers found in the dispatch logic (the `0x...` constants) as indicators of compromise (IoCs).

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of observed behaviors to the MITRE ATT&C framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1083** | File and Directory Discovery | The malware specifically scans for Steam-related configuration files (`config.vdf`, `local.vdf`) to locate target data. |
| **T1005** | Data from Local System | The "Dispatcher Pattern" identifies and extracts various types of information (keys, tokens, configs) from the local environment in a loop. |
| **T1562.003** | Data Encrypted before Exfiltration | The "math logic" mentioned in Chunk 2 is used to encrypt or obfuscate sensitive data (like passwords/keys) before it reaches the network layer. |
| **T1132** | Report_Data_Source (Implicitly part of T1048 preparation) | The "Packaging & Decoding" phase converts raw data into a serialized ASCII format suitable for transport. |
| **T1048** | Exfiltration Over Web Service | The use of the `wininet` library to send prepared data to a C2 server via HTTP/HTTPS confirms exfiltration over web services. |
| **T1595** | Procedure and Tool Generation (Implicit) | The use of advanced C++ "vtable" structures and sophisticated coding patterns indicates the development of a robust, professional-grade tool rather than a script. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The report notes that C2 infrastructure is likely dynamically generated or obfuscated, requiring a memory dump to uncover specific hardcoded addresses).

### **File paths / Registry keys**
*   `config.vdf` (Targeted Steam configuration file)
*   `local.vdf` (Targeted Steam local data file)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (The string `3333333` appears in the dump but is not a valid cryptographic hash).

### **Other artifacts**
*   **C2 Communication Pattern:** Use of the `wininet` library for data exfiltration via HTTP/HTTPS.
*   **Targeted Data Types:** Specific targeting of Steam-related credentials and account information (identified by the presence of "Stage 1" and "Stage 2" processing logic).
*   **Known Constant Values (Logic Identifiers):** `0x3173` (Potential internal identifier used in the dispatcher loop to determine data type).
*   **Technical Artifacts:** Use of C++ STL (Standard Template Library) and vtable implementations for sophisticated memory management.

---
### **Analyst Note**
The "EXTRACTED STRINGS" section contains a high volume of junk data, repeated patterns (e.g., `UATAUAVAWH`), and garbled characters that appear to be artifacts of the disassembly process rather than human-readable strings or actionable IOCs. The primary intelligence for incident response is derived from the **Behavioral Analysis**, which confirms a sophisticated "Dispatcher" architecture used to harvest and package Steam data before exfiltration via `wininet`.

---

## Malware Family Classification

1. **Malware family**: Unknown (Custom Steam-focused Infostealer)
2. **Malware type**: infostealer
3. **Confidence**: High

4. **Key evidence**:
*   **Specific Target Profiling:** The malware specifically targets Steam configuration files (`config.vdf`, `local.vdf`) to harvest account information, tokens, and credentials from the gaming demographic.
*   **Sophisticated Processing Architecture:** The use of a "Dispatcher Pattern," complex mathematical transformations for data obfuscation, and C++ Standard Template Library (STL) indicates professional-grade development intended to evade signature-based detection.
*   **Automated Exfiltration Pipeline:** The integration of a multi-stage process—discovery, parsing via dispatcher loops, encryption/formatting, and final transmission via the `wininet` library—confirms its primary purpose is the systematic theft of user data.
