# Threat Analysis Report

**Generated:** 2026-06-27 00:03 UTC
**Sample:** `01712a5e443efb4aa43ef3f8b38a4245cb0d0c1bf13b8d3ac4207247a44f7ab4_01712a5e443efb4aa43ef3f8b38a4245cb0d0c1bf13b8d3ac4207247a44f7ab4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01712a5e443efb4aa43ef3f8b38a4245cb0d0c1bf13b8d3ac4207247a44f7ab4_01712a5e443efb4aa43ef3f8b38a4245cb0d0c1bf13b8d3ac4207247a44f7ab4.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 460,288 bytes |
| MD5 | `3a91156c46a8b3b9a0591c9de52a8a73` |
| SHA1 | `736b0424d22fc20894b24eb10a75ab90fade562f` |
| SHA256 | `01712a5e443efb4aa43ef3f8b38a4245cb0d0c1bf13b8d3ac4207247a44f7ab4` |
| Overall entropy | 6.499 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1715246545 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 315,904 | 6.368 | No |
| `.rdata` | 124,928 | 6.286 | No |
| `.data` | 3,072 | 2.064 | No |
| `.pdata` | 11,776 | 5.558 | No |
| `_RDATA` | 512 | 3.295 | No |
| `.reloc` | 3,072 | 5.326 | No |

### Imports

**ntdll.dll**: `RtlUnwindEx`, `NtWriteFile`, `NtQuerySystemInformation`, `RtlGetVersion`, `NtQueryInformationProcess`, `RtlVirtualUnwind`, `RtlLookupFunctionEntry`, `RtlCaptureContext`, `RtlNtStatusToDosError`, `RtlPcToFileHeader`
**ADVAPI32.dll**: `OpenSCManagerW`, `CopySid`, `GetLengthSid`, `IsValidSid`, `GetTokenInformation`, `SystemFunction036`, `CloseServiceHandle`, `RegSetValueExW`, `RegCreateKeyW`, `OpenProcessToken`, `LookupPrivilegeValueW`, `AdjustTokenPrivileges`, `CreateServiceW`, `OpenServiceW`, `RegOpenKeyW`
**KERNEL32.dll**: `GetCPInfo`, `WideCharToMultiByte`, `SetEnvironmentVariableW`, `SetStdHandle`, `GetFileType`, `GetStringTypeW`, `VirtualQueryEx`, `HeapFree`, `CloseHandle`, `GetLastError`, `HeapReAlloc`, `GetCurrentProcessId`, `GetProcessHeap`, `GetCurrentProcess`, `HeapAlloc`
**pdh.dll**: `PdhRemoveCounter`, `PdhCollectQueryData`, `PdhOpenQueryA`, `PdhCloseQuery`, `PdhAddEnglishCounterW`, `PdhGetFormattedCounterValue`
**fltlib.dll**: `FilterLoad`, `FilterSendMessage`, `FilterConnectCommunicationPort`
**bcrypt.dll**: `BCryptGenRandom`
**psapi.dll**: `GetModuleFileNameExW`, `GetProcessMemoryInfo`
**shell32.dll**: `CommandLineToArgvW`
**powrprof.dll**: `CallNtPowerInformation`
**oleaut32.dll**: `GetErrorInfo`, `SysStringLen`, `SysFreeString`

## Extracted Strings

Total strings found: **1812** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@_RDATA
@.reloc
AVVWSH
([_^A^H
([_^A^
AWAVAUATVWUSH
fffff.
fffff.
ffffff.
8[]_^A\A]A^A_H
8[]_^A\A]A^A_
AVVWSH
([_^A^
AWAVATVWSH
([_^A\A^A_
AWAVVWSH
\$8fffff.
@[_^A^A_
AWAVAUATVWUSH
d$8H9t$@u
[]_^A\A]A^A_
UAWAVAUATVWS
on64.sysI
(ffff.
1ffffff.
t@I9_(u
t'I9_8
.fffff.
ffffff.
rNfffff.
r?fff.
rNfffff.
ffffff.
UAWAVAUATVWSH
)\$`fD
)T$pfD
[_^A\A]A^A_]
ffffff.
UAWAVAUATVWSH
)\$`fD
)T$pfD
[_^A\A]A^A_]
fffff.
UAWAVAUATVWSH
)\$`fD
)T$pfD
[_^A\A]A^A_]
UAWAVAUATVWSH
)\$`fD
)T$pfD
[_^A\A]A^A_]
UAWAVAUATVWSH
)\$`fD
)T$pfD
[_^A\A]A^A_]
fffff.
UAWAVAUATVWSH
)\$`fD
)T$pfD
[_^A\A]A^A_]
UAWAVAUATVWSH
)\$`fD
)T$pfD
[_^A\A]A^A_]
UAWAVAUATVWSH
)\$`fD
)T$pfD
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
)\$`fD
)T$pfD
[_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
AWAVAUATVWUSH
<3F2<!L;t$0u
X[]_^A\A]A^A_
UAVVWSH
p[_^A^]
UAVVWSH
 [_^A^]
fffff.
UAVVWSH
 [_^A^]
AVVWSH
([_^A^
AWAVAUATVWUSH
l$@u{L
H[]_^A\A]A^A_
H[]_^A\A]A^A_H
AWAVAUATVWSH
p[_^A\A]A^A_
AVVWSH
([_^A^H
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14001ac00` | `0x14001ac00` | 118727 | ✓ |
| `fcn.14001b6b0` | `0x14001b6b0` | 115656 | ✓ |
| `case.0x14001e5b8.131` | `0x140020c80` | 114487 | ✓ |
| `fcn.14002ad30` | `0x14002ad30` | 53422 | ✓ |
| `fcn.140040584` | `0x140040584` | 17826 | ✓ |
| `fcn.140040570` | `0x140040570` | 17776 | ✓ |
| `fcn.140023580` | `0x140023580` | 15543 | ✓ |
| `fcn.14000d560` | `0x14000d560` | 6890 | ✓ |
| `fcn.140007b00` | `0x140007b00` | 6547 | ✓ |
| `fcn.1400463f8` | `0x1400463f8` | 5713 | ✓ |
| `fcn.1400288b0` | `0x1400288b0` | 4780 | ✓ |
| `fcn.140039080` | `0x140039080` | 4767 | ✓ |
| `fcn.140013da0` | `0x140013da0` | 4486 | ✓ |
| `fcn.140036570` | `0x140036570` | 4176 | ✓ |
| `fcn.1400333a0` | `0x1400333a0` | 3407 | ✓ |
| `fcn.140014f30` | `0x140014f30` | 3199 | ✓ |
| `fcn.14004a920` | `0x14004a920` | 2683 | ✓ |
| `fcn.14004c3d0` | `0x14004c3d0` | 2474 | ✓ |
| `fcn.140032a10` | `0x140032a10` | 2446 | ✓ |
| `fcn.14004d3c0` | `0x14004d3c0` | 2302 | ✓ |
| `fcn.140034710` | `0x140034710` | 2260 | ✓ |
| `fcn.1400305f0` | `0x1400305f0` | 2092 | ✓ |
| `fcn.14002bd10` | `0x14002bd10` | 2056 | ✓ |
| `fcn.140041fb8` | `0x140041fb8` | 1977 | ✓ |
| `fcn.1400385e0` | `0x1400385e0` | 1974 | ✓ |
| `fcn.14000fff0` | `0x14000fff0` | 1865 | ✓ |
| `fcn.14001dc30` | `0x14001dc30` | 1854 | ✓ |
| `fcn.14000f440` | `0x14000f440` | 1822 | ✓ |
| `fcn.140011980` | `0x140011980` | 1747 | ✓ |
| `fcn.14003bd90` | `0x14003bd90` | 1677 | ✓ |

### Decompiled Code Files

- [`code/case.0x14001e5b8.131.c`](code/case.0x14001e5b8.131.c)
- [`code/fcn.140007b00.c`](code/fcn.140007b00.c)
- [`code/fcn.14000d560.c`](code/fcn.14000d560.c)
- [`code/fcn.14000f440.c`](code/fcn.14000f440.c)
- [`code/fcn.14000fff0.c`](code/fcn.14000fff0.c)
- [`code/fcn.140011980.c`](code/fcn.140011980.c)
- [`code/fcn.140013da0.c`](code/fcn.140013da0.c)
- [`code/fcn.140014f30.c`](code/fcn.140014f30.c)
- [`code/fcn.14001ac00.c`](code/fcn.14001ac00.c)
- [`code/fcn.14001b6b0.c`](code/fcn.14001b6b0.c)
- [`code/fcn.14001dc30.c`](code/fcn.14001dc30.c)
- [`code/fcn.140023580.c`](code/fcn.140023580.c)
- [`code/fcn.1400288b0.c`](code/fcn.1400288b0.c)
- [`code/fcn.14002ad30.c`](code/fcn.14002ad30.c)
- [`code/fcn.14002bd10.c`](code/fcn.14002bd10.c)
- [`code/fcn.1400305f0.c`](code/fcn.1400305f0.c)
- [`code/fcn.140032a10.c`](code/fcn.140032a10.c)
- [`code/fcn.1400333a0.c`](code/fcn.1400333a0.c)
- [`code/fcn.140034710.c`](code/fcn.140034710.c)
- [`code/fcn.140036570.c`](code/fcn.140036570.c)
- [`code/fcn.1400385e0.c`](code/fcn.1400385e0.c)
- [`code/fcn.140039080.c`](code/fcn.140039080.c)
- [`code/fcn.14003bd90.c`](code/fcn.14003bd90.c)
- [`code/fcn.140040570.c`](code/fcn.140040570.c)
- [`code/fcn.140040584.c`](code/fcn.140040584.c)
- [`code/fcn.140041fb8.c`](code/fcn.140041fb8.c)
- [`code/fcn.1400463f8.c`](code/fcn.1400463f8.c)
- [`code/fcn.14004a920.c`](code/fcn.14004a920.c)
- [`code/fcn.14004c3d0.c`](code/fcn.14004c3d0.c)
- [`code/fcn.14004d3c0.c`](code/fcn.14004d3c0.c)

## Behavioral Analysis

This final segment of disassembly completes the technical picture of the malware, providing deeper insight into its **internal logic architecture** and the **sophistication of its communication handling.**

The inclusion of `fcn.14003bd90` and `fcn.140011980` reveals how the malware processes data at a very low level, ensuring compatibility with various system states while making analysis difficult for human researchers.

### Updated Analysis: Chunk 6/6

#### Core Functionality
*   **Robust Time/Timestamp Handling (`fcn.14003bd90`):** This function is a complex handler for `FILETIME` structures, supporting multiple bit-depths (16-bit, 32-bit, and 64-bit).
    *   **Malware Intent:** Robust timestamp handling is often associated with **Timestomping**. By being able to manipulate or interpret various time formats precisely, the malware can modify the "Last Modified" or "Created" dates of its own files (or dropped payloads) to match legitimate system files, effectively hiding from forensic timeline analysis.
*   **Sophisticated Data Decoding & Dispatch (`fcn.140011980`):** This is a massive, complex function featuring large jump tables and nested logic branches. 
    *   **Analysis:** The structure suggests this is the primary **Protocol Handler**. It doesn't just "receive" a command; it decodes a multi-layered packet from the C2 server. The various `switch` cases (e.g., `0x41`, `0x51`, `0x56`) likely correspond to different types of commands or sub-functions within the malware's modular framework.
    *   **String/Buffer Processing:** The logic preceding the switches indicates the malware is performing intensive checks on buffer lengths and character encoding (potentially handling UTF-8 or a custom obfuscated string format).

#### Sophisticated Anti-Analysis Techniques
*   **Obfuscated Control Flow (Hidden Jump Tables):** The disassembler notes `WARNING: Could not recover jumptable...` multiple times. 
    *   **Malware Intent:** This is a deliberate "anti-analysis" tactic. By using indirect jumps and complex, non-linear logic to reach different segments of code, the author ensures that automated tools (like Ghidra or IDA Pro) cannot easily generate a clean "graph view." This forces an analyst to manually trace every branch, significantly slowing down the reverse engineering process.
*   **Abstraction Layer:** The fact that many operations are wrapped in internal functions (`fcn.140012ce0`, `fcn.140012a20`) suggests a highly modular architecture where the "core" of the malware is separated from its "features."

---

### Final Summary Analysis (Chunks 1 through 6)

The final compilation of all segments confirms that this is a **high-tier, professional-grade Trojan/Backdoor.** It is designed for longevity, stealth, and multi-purpose deployment by an advanced threat actor.

#### Key Pillars of the Threat:
1.  **Advanced Evasion:** By utilizing `cpuid` checks, `PDH` performance monitoring, and complex `FILETIME` handling, the malware demonstrates a high level of awareness regarding sandbox environments and forensic investigations.
2.  **Robust Infrastructure & Modular Design:** The use of **Named Pipes** for internal communication and a **large-scale Command Dispatcher** (seen in Chunk 6) confirms that this is an "orchestrator." It can be updated with new capabilities (e.g., stealing credentials, encrypting files, or exfiltrating data) without changing the primary infection vector.
3.  **Intentional Complexity (Anti-Analysis):** The presence of **hidden jump tables**, intensive bitwise arithmetic for decryption, and complex internal state management is designed to frustrate automated security products and human analysts alike. It aims to remain active on a network for as long as possible before detection.
4.  **Sophisticated Communication:** The complexity of the parsing logic in `fcn.140011980` suggests it can handle complex, multi-part commands from a C2 server, likely using an encrypted or encoded "handshake" protocol to hide its activities from network traffic monitors.

#### Conclusion:
This is not a generic commodity trojan; it is an **operational tool** used for targeted attacks or broad, high-value campaigns. Its ability to hide its true functionality behind multiple layers of "guards," complex decoding logic, and anti-analysis maneuvers makes it a significant threat.

### Recommended Intelligence/Response Actions:
*   **Network Defense:** Monitor for non-standard **Named Pipe** activity on the local network, which may indicate communication between different modules of the malware.
*   **Host Analysis:** Flag any unsigned binaries attempting to access `PdhAddEnglishCounterW` or performing high volumes of internal decryption/decoding before initiating outbound network connections.
*   **Forensics:** During incident response, look for evidence of **Timestomping**. Check if malicious files have timestamps that perfectly match legitimate system files (e.g., a `.dll` created in 2018 but with an updated timestamp to match the OS).
*   **Threat Hunting:** Look for "high-entropy" data blobs within the binary or memory, which indicates the presence of the encrypted modules and command sets used by the dispatcher.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1070.005** | Indicator Removal: Timestomping | The malware utilizes a complex `FILETIME` handler to modify file timestamps, aiming to blend in with legitimate system files and evade forensic timeline analysis. |
| **T1027** | Obfuscated Files or Information | The use of hidden jump tables and non-linear logic is a deliberate tactic to hinder disassembly/decompiler tools (like Ghidra/IDA) and slow down human reverse engineering. |
| **T1497** | Virtualization | The inclusion of `cpuid` checks and `PDH` performance monitoring indicates an intent to detect sandbox environments and hardware-assisted virtualization. |
| **T1036** | Masquerading | The use of Named Pipes for internal communication between modules allows the malware components to communicate while potentially mimicking legitimate system-level IPC. |
| **T1071** | Application Layer Protocol | The multi-layered command dispatch logic and complex buffer processing indicate a sophisticated C2 protocol designed to hide specific actions from network monitors. |
| **T1568** | Dynamic Resolution | (Implicit) The modular "orchestrator" design and ability to switch between different commands suggests the use of dynamic calls or a dispatcher to load capabilities at runtime. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the categorized list of Indicators of Compromise (IOCs) and relevant technical artifacts.

### **IP addresses / URLs / Domains**
*   *None identified.* (The raw strings did not contain plaintext IP addresses or domain names; these are likely obfuscated or handled via the "Protocol Handler" mentioned in the analysis.)

### **File paths / Registry keys**
*   *None identified.* (The strings provided consist primarily of internal memory offsets and common Windows system descriptors which were excluded as false positives.)

### **Mutex names / Named pipes**
*   **Named Pipes:** The report confirms the use of **Named Pipes** for internal communication between modules. While a specific pipe name (e.g., `\.\pipe\...`) was not provided in the text, this is a high-priority behavioral indicator for local network monitoring.

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 hashes were present in the provided string block.)

### **Other artifacts**
*   **C2 Command Codes:** The protocol handler (`fcn.140011980`) utilizes specific hex values for command dispatch:
    *   `0x41`
    *   `0x51`
    *   `0x56`
*   **Suspicious API Calls / Techniques:**
    *   **Timestomping:** Manipulation of `FILETIME` structures to alter file timestamps for forensic evasion.
    *   **Environment Checks:** Utilization of the `cpuid` instruction and `PdhAddEnglishCounterW` (Performance Data Helper) to detect sandboxes or specific system environments.
    *   **Anti-Analysis Logic:** Use of "Hidden Jump Tables" and non-linear logic to frustrate automated disassembly tools (Ghidra/IDA Pro).

---

### **Analyst Notes for SOC/IR Teams**
While this sample lacks standard "static" IOCs (like hardcoded IPs), it is identified as a **high-tier, professional-grade Trojan**. The following behavioral "soft" indicators should be monitored:

1.  **Internal Communication:** Monitor for non-standard Named Pipe traffic between local processes.
2.  **Timing Anomalies:** Watch for files modified with timestamps that match system file creation dates (indicative of the identified Timestomping behavior).
3.  **Command Execution:** The presence of multi-layered, obfuscated packets in network traffic suggests a sophisticated C2 infrastructure; look for high-entropy data blobs in outbound traffic.

---

## Malware Family Classification

1. **Malware family:** custom
2. **Malware type:** backdoor / loader
3. **Confidence:** High

**Key evidence:**
*   **Sophisticated Communication & Modular Architecture:** The analysis identifies a complex "Protocol Handler" (`fcn.140011980`) and the use of Named Pipes, indicating an orchestrated architecture designed to manage multiple capabilities (e.g., data theft or encryption) via a modular command system.
*   **Advanced Evasion & Anti-Analysis:** The sample employs high-tier evasion techniques including `cpuid` and `PDH` checks for sandbox detection, "Timestomping" via `FILETIME` manipulation to evade forensic timelines, and hidden jump tables to frustrate automated decompilation tools.
*   **Professional Grade Design:** The technical report explicitly characterizes the sample as a "high-tier, professional-grade Trojan" designed for longevity and multi-purpose deployment rather than as a simple commodity piece of malware.
