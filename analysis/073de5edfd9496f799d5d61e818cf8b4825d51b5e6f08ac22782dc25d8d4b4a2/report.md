# Threat Analysis Report

**Generated:** 2026-07-16 15:53 UTC
**Sample:** `073de5edfd9496f799d5d61e818cf8b4825d51b5e6f08ac22782dc25d8d4b4a2_073de5edfd9496f799d5d61e818cf8b4825d51b5e6f08ac22782dc25d8d4b4a2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `073de5edfd9496f799d5d61e818cf8b4825d51b5e6f08ac22782dc25d8d4b4a2_073de5edfd9496f799d5d61e818cf8b4825d51b5e6f08ac22782dc25d8d4b4a2.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 5 sections |
| Size | 199,168 bytes |
| MD5 | `e1b159dd347eaa90a80480055c8edcd2` |
| SHA1 | `5ee07cbf8677b4561e9434937c4aea75ae3f1d5a` |
| SHA256 | `073de5edfd9496f799d5d61e818cf8b4825d51b5e6f08ac22782dc25d8d4b4a2` |
| Overall entropy | 5.934 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766008923 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 129,024 | 6.616 | No |
| `.rdata` | 30,208 | 4.788 | No |
| `.data` | 6,656 | 3.762 | No |
| `.rsrc` | 1,024 | 3.85 | No |
| `.reloc` | 31,232 | 1.958 | No |

### Imports

**SHLWAPI.dll**: `PathCombineW`
**WININET.dll**: `InternetCloseHandle`, `HttpQueryInfoW`, `InternetReadFile`, `InternetOpenUrlW`, `InternetOpenW`
**NETAPI32.dll**: `NetApiBufferFree`, `NetShareEnum`
**SHELL32.dll**: `SHGetSpecialFolderPathW`, `ShellExecuteExW`
**ole32.dll**: `CoUninitialize`, `CoCreateInstance`, `CoInitialize`
**USER32.dll**: `wsprintfW`
**KERNEL32.dll**: `LoadLibraryExW`, `OutputDebugStringW`, `EnumSystemLocalesEx`, `IsValidLocaleName`, `LCMapStringEx`, `LoadLibraryW`, `GetConsoleCP`, `GetConsoleMode`, `SetFilePointerEx`, `SetStdHandle`, `WriteConsoleW`, `FlushFileBuffers`, `EncodePointer`, `GetUserDefaultLocaleName`, `CompareStringEx`

## Extracted Strings

Total strings found: **685** (showing first 100)

```
!This program cannot be run in DOS mode.
$
C;Rich1
`.rdata
@.data
@.reloc
D$XSVW
t$,FVj
t$,FVj
t$,FVj
t$,FVj
uT9FTtOV
																									
																			
																												
																												
9\u(A;
D$@SVW
8\u.@;
8\u,@;
8\u,@;
8\u,@;
8\u,@;
8\u,@;
8\u,@;
8\u,@;
8\u,@;
8\u,@;
8\u.@;
8\u,@;
8\u,@;
n9~|iW
8\u,@;
uT9FTtOV
8\u,@;
8\u,@;
8\u,@;
w(_^[]
8\u,@;
8\u,@;
8\u,@;
FH<_u`
FH<.tN<[tJ<\tF<*tB<|t><^t:<$t6
FH<(t'<)t#<+t
8\u,@;
8\u,@;
8\u,@;
9\u%A;
;}t;S
YYhL B
jhPjB
SVjA[jZ^+
jAZjZ^+
D$+d$SVW
D$+d$SVW
QQSVWd
u&j[9
j hpjB
"u
SSSSS
"u
WWWWW
F;Bt
PP9E u
u,9Et'9
PPPPPPPP
D$tQf
~pjCXf
uPVWh68A
jdh kB
j@j _W
QQSVWh
j"_f9y
y3h,;B
Genuu_
ineIuV
nteluM3
jh@kB
jh`kB
]h\@B
tyPVj@W
_tcPVj@
u#j,Xf;
>Cu/f9F
w$hT@B
uj;Yf9
jh@mB
tf90u
RVSQSWV
HtHu(
,SVWj0X
Wj0XPV
	<et<Et
SVWjA_jZ+
uBjAYjZ+
u9Mu&3
URPQQh
u9Mu!3
t VV9u
<0|o<9
GPj3S
G Pj*S
G$Pj+S
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004126ad` | `0x4126ad` | 26536 | ✓ |
| `fcn.00412190` | `0x412190` | 23829 | ✓ |
| `fcn.00412bd4` | `0x412bd4` | 12285 | ✓ |
| `fcn.0040fd39` | `0x40fd39` | 5877 | ✓ |
| `fcn.0041df92` | `0x41df92` | 2500 | ✓ |
| `fcn.0041b605` | `0x41b605` | 2122 | ✓ |
| `fcn.0041a287` | `0x41a287` | 2033 | ✓ |
| `fcn.0041d816` | `0x41d816` | 1867 | ✓ |
| `fcn.0040e060` | `0x40e060` | 1604 | ✓ |
| `fcn.0040edc0` | `0x40edc0` | 1604 | ✓ |
| `fcn.00405be0` | `0x405be0` | 1457 | ✓ |
| `fcn.0041cd36` | `0x41cd36` | 1392 | ✓ |
| `fcn.0041d2a6` | `0x41d2a6` | 1392 | ✓ |
| `fcn.00409f50` | `0x409f50` | 1290 | ✓ |
| `fcn.00406540` | `0x406540` | 1076 | ✓ |
| `fcn.0040cac0` | `0x40cac0` | 998 | ✓ |
| `fcn.004161f8` | `0x4161f8` | 923 | ✓ |
| `fcn.004159d7` | `0x4159d7` | 920 | ✓ |
| `fcn.00419e8b` | `0x419e8b` | 896 | ✓ |
| `fcn.00417f4c` | `0x417f4c` | 858 | ✓ |
| `fcn.00403c70` | `0x403c70` | 801 | ✓ |
| `fcn.0041e9ff` | `0x41e9ff` | 768 | ✓ |
| `fcn.0041513d` | `0x41513d` | 739 | ✓ |
| `fcn.00408b70` | `0x408b70` | 671 | ✓ |
| `fcn.00409160` | `0x409160` | 663 | ✓ |
| `fcn.0040bf10` | `0x40bf10` | 652 | ✓ |
| `fcn.00415750` | `0x415750` | 647 | ✓ |
| `fcn.00406230` | `0x406230` | 625 | ✓ |
| `fcn.00407140` | `0x407140` | 619 | ✓ |
| `fcn.00411998` | `0x411998` | 619 | ✓ |

### Decompiled Code Files

- [`code/fcn.00403c70.c`](code/fcn.00403c70.c)
- [`code/fcn.00405be0.c`](code/fcn.00405be0.c)
- [`code/fcn.00406230.c`](code/fcn.00406230.c)
- [`code/fcn.00406540.c`](code/fcn.00406540.c)
- [`code/fcn.00407140.c`](code/fcn.00407140.c)
- [`code/fcn.00408b70.c`](code/fcn.00408b70.c)
- [`code/fcn.00409160.c`](code/fcn.00409160.c)
- [`code/fcn.00409f50.c`](code/fcn.00409f50.c)
- [`code/fcn.0040bf10.c`](code/fcn.0040bf10.c)
- [`code/fcn.0040cac0.c`](code/fcn.0040cac0.c)
- [`code/fcn.0040e060.c`](code/fcn.0040e060.c)
- [`code/fcn.0040edc0.c`](code/fcn.0040edc0.c)
- [`code/fcn.0040fd39.c`](code/fcn.0040fd39.c)
- [`code/fcn.00411998.c`](code/fcn.00411998.c)
- [`code/fcn.00412190.c`](code/fcn.00412190.c)
- [`code/fcn.004126ad.c`](code/fcn.004126ad.c)
- [`code/fcn.00412bd4.c`](code/fcn.00412bd4.c)
- [`code/fcn.0041513d.c`](code/fcn.0041513d.c)
- [`code/fcn.00415750.c`](code/fcn.00415750.c)
- [`code/fcn.004159d7.c`](code/fcn.004159d7.c)
- [`code/fcn.004161f8.c`](code/fcn.004161f8.c)
- [`code/fcn.00417f4c.c`](code/fcn.00417f4c.c)
- [`code/fcn.00419e8b.c`](code/fcn.00419e8b.c)
- [`code/fcn.0041a287.c`](code/fcn.0041a287.c)
- [`code/fcn.0041b605.c`](code/fcn.0041b605.c)
- [`code/fcn.0041cd36.c`](code/fcn.0041cd36.c)
- [`code/fcn.0041d2a6.c`](code/fcn.0041d2a6.c)
- [`code/fcn.0041d816.c`](code/fcn.0041d816.c)
- [`code/fcn.0041df92.c`](code/fcn.0041df92.c)
- [`code/fcn.0041e9ff.c`](code/fcn.0041e9ff.c)

## Behavioral Analysis

This updated analysis incorporates the new disassembly provided in Chunk 3. While the previous findings confirmed the binary's role as a **Downloader/Dropper**, this latest data reveals that the underlying infrastructure is significantly more sophisticated than a simple "one-trick" downloader. It indicates the presence of a **complex processing engine** and **advanced environmental fingerprinting**.

---

### Updated Analysis: Technical Findings

#### 1. Confirmed Downloader & Dropper Logic (Retained)
The core malicious functionality identified in the previous step remains central to the threat profile:
*   **C2 Interaction:** Targeting `196.251.107.104` via `WinINet`.
*   **Payload Validation:** Explicitly checking for the `0x5A 0x4D` (MZ) header before execution.
*   **Evasion via Sleep:** Using `GetTickCount()` to calculate randomized delays.

#### 2. Sophisticated Parsing & Interpreter Infrastructure (New Finding)
The functions `fcn.00409160`, `fcn.00408b70`, and `fcn.0040bf10` reveal a massive, complex logic structure that is not typical of simple malware. 
*   **State Machine/Interpreter Logic:** The large `switch-case` block in `fcn.00409160` (handling over 21 cases) and the repetitive loops in `fcn.00408b70` strongly suggest a **custom interpreter or a heavy parsing engine** (e.g., for JSON, XML, or a proprietary configuration language).
*   **Robust String Handling:** The presence of several functions dedicated solely to traversing memory buffers and performing complex comparisons indicates that the loader is designed to process extensive amounts of data/commands from the C2 server, rather than just executing a single hardcoded command.

#### 3. Advanced Environmental Fingerprinting (New Finding)
The function `fcn.0041e9ff` shows highly specific logic regarding **FPU Control Words**.
*   **Sandbox Detection:** Manipulation of FPU control words is a classic technique used to detect "headless" environments, specific virtual machine hypervisors, or automated analysis sandboxes. If the hardware's floating-point state does not match what the malware expects (due to emulation), it will likely terminate or alter its behavior.
*   **Sophisticated Library Usage:** The use of `MultiByteToWideChar` (`fcn.00411998`) and other high-level string conversion routines suggests the author utilized a professional C++ development environment, indicating a well-funded actor or a "malware-as-a-service" (MaaS) builder.

#### 4. Modular Complexity
The code in `fcn.00415750` and `fcn.00407140` suggests the loader is checking for specific features or "modules." It isn't just looking for a file; it is looking for specific **identifiers** (e.g., checking if strings start with specific prefixes). This indicates that this loader can be multi-purpose—it could potentially host different modules (e.g., a credential stealer, a remote access trojan, or an info-stealer) depending on the response from the C2 server.

---

### Updated Summary of Malicious Behaviors

| Feature | Observation | Significance |
| :--- | :--- | :--- |
| **C2 Communication** | Uses `InternetOpenUrlW` to contact a hardcoded IP (`196.251.107.104`). | Direct communication with an attacker-controlled server. |
| **Payload Dropping** | Downloads/saves content and verifies the "MZ" header before execution via `ShellExecuteW`. | Standard behavior for a "Downloader" or "Stager." |
| **Interpreter Engine** | Complex switch-cases and state machines (`fcn.00409160`, `fcn.00408b70`). | Indicates the loader can process complex, multi-step commands from the C2. |
| **Environmental Checks** | FPU Control Word manipulation and specialized string processing. | Designed to detect/evade automated sandboxes and analysis labs. |
| **Evasion Tactics** | Calculated `Sleep()` calls based on system tick counts. | Circumvents "fast-scan" sandbox analysis tools. |

---

### Final Conclusion for Analysis
The binary is a **high-sophistication, modular downloader**. 

While the initial triage suggested a simple dropper, the full disassembly reveals a highly professional architecture. It doesn't just fetch and run; it contains the infrastructure to interpret complex instructions and perform environmental checks to ensure it is running on a "real" victim machine rather than in an analyst's lab. 

**Key Threat Indicators (TTPs):**
1.  **Persistence/Evasion:** Use of randomized sleep and FPU state checking to bypass automated security systems.
2.  **Modular Capabilities:** The presence of heavy parsing logic suggests the loader is a "plug-and-play" platform for various types of malware payloads.
3.  **Direct C2 Communication:** Usage of hardcoded IPs bypasses standard DNS sinkholing methods.

**Recommended Investigation Paths:**
1.  **Network Capture (PCAP):** Observe what specific commands the server at `196.251.107.104` sends back to the loader to see which "branch" of the switch-case logic is activated.
2.  **Memory Forensics:** Dump the process memory after it has executed a few loops in `fcn.00408b70` to identify the internal configuration or "instructions" it is parsing.
3.  **Sandbox Evasion Profile:** Note that standard sandboxes may fail to trigger the payload if they do not correctly emulate the specific FPU states checked in `fcn.0041e9ff`.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors described in your technical report to the corresponding MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1071.001** | Application Layer Protocol: Web Protocols | The malware uses `WinINet` (specifically `InternetOpenUrlW`) to communicate with a hardcoded IP address for data retrieval. |
| **T1105** | Ingress Tool Transfer | The binary functions as a downloader by fetching, saving, and validating the "MZ" header of a payload before execution. |
| **T1497** | Virtualization/Sandbox Detection | The use of FPU Control Word manipulation is a specific technique to identify and evade "headless" or emulated analysis environments. |
| **T1620** | [Note: Often categorized under T1497] **Anti-Analysis / Sandbox Evasion** | Use of `GetTickCount()` for randomized sleep durations is intended to bypass automated sandboxes with limited timeout periods. |
| **T1059** | Command and Scripting Interpreter | The extensive switch-case blocks and state machine logic indicate a custom interpreter designed to process complex, multi-step commands from the C2. |
| **T1036** | Masquerading | (Optional/Contextual) The modular nature of the loader allows it to masquerade as various types of malware depending on the server's response. |

### Analyst Notes:
*   **Complexity Marker:** The jump from a "simple" dropper to an **Interpreter-based loader** is a key indicator of high-sophistication. By using a command interpreter (T1059), the threat actor can change the functionality of the malware post-infection without changing the binary, significantly increasing its lifespan in the wild.
*   **Evasion Strategy:** The combination of **T1497** (FPU checks) and time-based delays suggests a high degree of operational security (OPSEC), specifically targeting automated forensic pipelines.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `196.251.107.104` (C2_Server)

**File paths / Registry keys**
*   *None identified.* (The list provided in the "Extracted Strings" section consists of standard system error messages and obfuscated character blocks, not specific malicious file paths or registry keys.)

**Mutex names / Named pipes**
*   *None detected.*

**Hashes**
*   *None detected.*

**Other artifacts (user agents, C2 patterns, etc.)**
*   **C2 Communication Protocol:** Use of `WinINet` and the function `InternetOpenUrlW` for remote communication.
*   **Evasion Techniques:** 
    *   FPU Control Word manipulation (identified in `fcn.0041e9ff`) to detect sandboxes/virtualized environments.
    *   Randomized sleep intervals calculated via `GetTickCount()` to bypass "fast-scan" automated analysis.
*   **Execution Logic:** 
    *   Verification of the `0x5A 0x4D` (MZ) header before executing downloaded payloads.
    *   Use of `ShellExecuteW` for payload execution.
*   **Instructional Parsing:** Presence of a complex state machine/interpreter logic (`fcn.00409160`, `fcn.00408b70`) indicating the loader can process multi-step commands and modular payloads.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://%s/%d.exe`

**IP addresses:**
- `196.251.107.104`

---

## Malware Family Classification

Based on the provided behavioral analysis and technical findings, here is the classification for the sample:

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Modular Interpreter Architecture:** The discovery of a large switch-case block (over 21 cases) and state machine logic indicates the binary is not a simple downloader but a sophisticated "loader" designed to interpret complex command sets from a C2 server, allowing it to host various modular payloads (e.g., RATs or info-stealers).
    *   **Advanced Anti-Analysis:** The use of FPU Control Word manipulation and `GetTickCount()` for randomized sleep intervals demonstrates intentional effort to bypass automated sandboxes and "headless" analysis environments.
    *   **Sophisticated Execution Flow:** The inclusion of MZ header validation before execution via `ShellExecuteW` combined with dedicated string handling routines points toward a professional-grade, multi-purpose delivery platform rather than a one-time use script.
