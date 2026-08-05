# Threat Analysis Report

**Generated:** 2026-08-04 18:49 UTC
**Sample:** `0cf1d46ebb1eebd5bf79489157f02aa719d5b50445f3eca3fac20f3cb0a581e8_0cf1d46ebb1eebd5bf79489157f02aa719d5b50445f3eca3fac20f3cb0a581e8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0cf1d46ebb1eebd5bf79489157f02aa719d5b50445f3eca3fac20f3cb0a581e8_0cf1d46ebb1eebd5bf79489157f02aa719d5b50445f3eca3fac20f3cb0a581e8.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 118,272 bytes |
| MD5 | `51e78c20682e05f93fdd911531217711` |
| SHA1 | `9c0723d56cb3fb9e144af29dc5fbbcb2cb8761ac` |
| SHA256 | `0cf1d46ebb1eebd5bf79489157f02aa719d5b50445f3eca3fac20f3cb0a581e8` |
| Overall entropy | 5.921 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1770037112 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 62,976 | 6.409 | No |
| `.rdata` | 44,032 | 4.72 | No |
| `.data` | 3,072 | 2.08 | No |
| `.pdata` | 4,608 | 4.532 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.832 | No |

### Imports

**WININET.dll**: `InternetCloseHandle`, `InternetOpenUrlA`, `InternetReadFile`, `InternetOpenA`
**ole32.dll**: `CoUninitialize`, `CoInitializeEx`
**OLEAUT32.dll**: `SafeArrayCreate`, `SafeArrayDestroy`, `SafeArrayGetUBound`, `SafeArrayAccessData`, `SafeArrayUnaccessData`, `SafeArrayPutElement`, `SafeArrayCreateVector`, `VariantInit`, `VariantClear`
**SHELL32.dll**: `SHGetFolderPathA`
**USER32.dll**: `wsprintfW`, `GetMessageA`, `TranslateMessage`, `DispatchMessageA`, `wsprintfA`
**ADVAPI32.dll**: `RegSetValueExW`, `RegQueryValueExW`, `RegOpenKeyExW`, `RegCreateKeyExW`, `RegCloseKey`, `GetUserNameA`, `FreeSid`, `CheckTokenMembership`, `AllocateAndInitializeSid`
**KERNEL32.dll**: `FlushFileBuffers`, `SetStdHandle`, `HeapReAlloc`, `HeapSize`, `GetStringTypeW`, `GetFileType`, `WriteFile`, `GetProcessHeap`, `LCMapStringW`, `GetConsoleOutputCP`, `GetConsoleMode`, `SetFilePointerEx`, `CreateFileW`, `WriteConsoleW`, `GetStdHandle`

### Exports

`timeBeginPeriod`, `timeEndPeriod`, `timeGetTime`

## Extracted Strings

Total strings found: **494** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
.reloc
HcH<E3
t_HcH<E3
UVWATAUAVAWH
tE WHc
fD9dE u
A_A^A]A\_^]
@USVWATAUAVAWH
@8}Lt,
A_A^A]A\_^[]
UVWAVAWH
A_A^_^]
@USATAUAWH
EHmsco
ELree.
PPD9l$h
A_A]A\[]
|$ AVH
uxHcx
A:8ufI
tcA88uVI
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
f9<H}
t98t H
u3HcH<H
x ATAVAWH
< t;<	t7
 A_A^A\
UVWAVAWH
H9:tH
0A_A^_^]
	H;zV
WAVAWH
L3
H3B
 A_A^_
D$0u3
\$8t	H
@UATAUAVAWH
A_A^A]A\]
D$0@8{
u$D8r(tH
D81u`L9r
uPD8r(tH
vWD8s(tH
u$D8r(tH
fD91u_L9r
uPD8r(tH
vVD8s(tH
UVWATAUAVAWH
PA_A^A]A\_^]
WATAUAVAWH
0A_A^A]A\_
H9>u+A
@USVWATAUAVH
,/<-w
H
D8t$ht
H
D8t$ht
H
A^A]A\_^[]
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180007a60` | `0x180007a60` | 14903 | ✓ |
| `fcn.180007a28` | `0x180007a28` | 14898 | ✓ |
| `fcn.18000393c` | `0x18000393c` | 13679 | ✓ |
| `fcn.18000383c` | `0x18000383c` | 2846 | ✓ |
| `fcn.1800039cc` | `0x1800039cc` | 2568 | ✓ |
| `fcn.180009ad8` | `0x180009ad8` | 1829 | ✓ |
| `fcn.18000f650` | `0x18000f650` | 1677 | ✓ |
| `fcn.180002180` | `0x180002180` | 1618 | ✓ |
| `fcn.1800018d0` | `0x1800018d0` | 1514 | ✓ |
| `fcn.1800012c0` | `0x1800012c0` | 1451 | ✓ |
| `fcn.1800027e0` | `0x1800027e0` | 1392 | ✓ |
| `fcn.180005248` | `0x180005248` | 1213 | ✓ |
| `fcn.18000de28` | `0x18000de28` | 1171 | ✓ |
| `fcn.18000d400` | `0x18000d400` | 922 | ✓ |
| `fcn.18000fd00` | `0x18000fd00` | 920 | ✓ |
| `fcn.18000ce90` | `0x18000ce90` | 920 | ✓ |
| `fcn.180002f20` | `0x180002f20` | 917 | ✓ |
| `fcn.180003400` | `0x180003400` | 892 | ✓ |
| `fcn.180009778` | `0x180009778` | 862 | ✓ |
| `fcn.180007d8c` | `0x180007d8c` | 817 | ✓ |
| `fcn.18000e774` | `0x18000e774` | 815 | ✓ |
| `fcn.18000a5a4` | `0x18000a5a4` | 712 | ✓ |
| `section..text` | `0x180001000` | 694 | ✓ |
| `fcn.180001ec0` | `0x180001ec0` | 689 | ✓ |
| `fcn.180003c28` | `0x180003c28` | 667 | ✓ |
| `fcn.1800069a0` | `0x1800069a0` | 642 | ✓ |
| `fcn.18000a200` | `0x18000a200` | 623 | ✓ |
| `fcn.18000b634` | `0x18000b634` | 604 | ✓ |
| `fcn.180007730` | `0x180007730` | 589 | ✓ |
| `fcn.180005708` | `0x180005708` | 584 | ✓ |

### Decompiled Code Files

- [`code/fcn.1800012c0.c`](code/fcn.1800012c0.c)
- [`code/fcn.1800018d0.c`](code/fcn.1800018d0.c)
- [`code/fcn.180001ec0.c`](code/fcn.180001ec0.c)
- [`code/fcn.180002180.c`](code/fcn.180002180.c)
- [`code/fcn.1800027e0.c`](code/fcn.1800027e0.c)
- [`code/fcn.180002f20.c`](code/fcn.180002f20.c)
- [`code/fcn.180003400.c`](code/fcn.180003400.c)
- [`code/fcn.18000383c.c`](code/fcn.18000383c.c)
- [`code/fcn.18000393c.c`](code/fcn.18000393c.c)
- [`code/fcn.1800039cc.c`](code/fcn.1800039cc.c)
- [`code/fcn.180003c28.c`](code/fcn.180003c28.c)
- [`code/fcn.180005248.c`](code/fcn.180005248.c)
- [`code/fcn.180005708.c`](code/fcn.180005708.c)
- [`code/fcn.1800069a0.c`](code/fcn.1800069a0.c)
- [`code/fcn.180007730.c`](code/fcn.180007730.c)
- [`code/fcn.180007a28.c`](code/fcn.180007a28.c)
- [`code/fcn.180007a60.c`](code/fcn.180007a60.c)
- [`code/fcn.180007d8c.c`](code/fcn.180007d8c.c)
- [`code/fcn.180009778.c`](code/fcn.180009778.c)
- [`code/fcn.180009ad8.c`](code/fcn.180009ad8.c)
- [`code/fcn.18000a200.c`](code/fcn.18000a200.c)
- [`code/fcn.18000a5a4.c`](code/fcn.18000a5a4.c)
- [`code/fcn.18000b634.c`](code/fcn.18000b634.c)
- [`code/fcn.18000ce90.c`](code/fcn.18000ce90.c)
- [`code/fcn.18000d400.c`](code/fcn.18000d400.c)
- [`code/fcn.18000de28.c`](code/fcn.18000de28.c)
- [`code/fcn.18000e774.c`](code/fcn.18000e774.c)
- [`code/fcn.18000f650.c`](code/fcn.18000f650.c)
- [`code/fcn.18000fd00.c`](code/fcn.18000fd00.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This updated analysis incorporates the additional disassembly provided in chunk 2. The addition of these functions confirms that this binary is not merely a "defense-evasion" tool; it is a **multi-stage malware dropper/loader** with significant capabilities for remote communication and payload execution.

### Updated Analysis Summary

The malware utilizes a sophisticated "wrapper" or framework (likely a large library like .NET or an equivalent heavy C++ framework) to mask its core functionality. While the first chunk revealed intense anti-analysis and environment hardening, this second chunk reveals the **primary infection mechanisms**: network communication, payload decryption, and system interaction.

---

### New Core Functionalities Identified

#### 1. Network Payload Downloader & Decryption (`fcn.180002f20`)
This is a critical finding. This function implements a complete "downloader" routine:
*   **Network Connection:** It uses `InternetOpenA` and `InternetOpenUrlA`. The fact that it uses the WinINet API suggests it's designed to communicate over standard HTTP/HTTPS protocols, making its traffic harder to distinguish from normal web browsing.
*   **Memory Allocation for Payload:** It calls `VirtualAlloc` to reserve a large chunk of memory (at least 0x100000 bytes). This is where the downloaded data is stored.
*   **Data Retrieval:** It uses `InternetReadFile` in a loop to pull data from a remote server into the newly allocated memory.
*   **In-Memory Decryption/De-obfuscation:** Immediately after the download, it performs a series of mathematical operations (XOR and subtraction) on the buffer:
    `*puVar2 = *pu14 - *[key]` followed by `*puVar2 = *puVar2 ^ *[key]`.
    This confirms that the malware downloads an **encrypted payload** and decrypts it in memory before execution, a technique used to bypass static file scanners.

#### 2. Execution Gatekeeping & Anti-Debugging (`fcn.180003400`)
The code includes "gatekeeper" functions like `fcn.180003400`. 
*   These functions perform checks on memory values before allowing the execution flow to continue. 
*   If a check fails, the code enters a block containing a **Software Interrupt (`swi(0x29)`)**. In many contexts, this is used as an "anti-analysis" trap; it can crash the process or confuse debuggers/disassemblers if they attempt to step through the code.

#### 3. File System Interaction and Parsing (`fcn.180009778`)
This function handles file system operations, including `FindFirstFileExW`. This is commonly used for:
*   **Target Hunting:** Searching for specific documents or sensitive files to exfiltrate.
*   **Configuration Parsing:** Looking for local configuration files (e.g., saved credentials or "next-hop" C2 addresses).

#### 4. Complex Library Logic (`fcn.18000b634`, `fcn.180007d8c`, `fcn.18000a5a4`)
These functions show a high level of complexity, involving nested loops and complex bitwise logic to navigate internal tables. 
*   **Why this is important:** This indicates the malware likely uses a large, legitimate library as its "host." By wrapping malicious commands inside thousands of lines of standard library code (like those found in .NET or advanced C++ frameworks), the author makes it significantly harder for automated tools to pinpoint exactly where the malicious behavior begins.

---

### Updated Summary of Malicious Behaviors

| Category | Specific Technique Found | Purpose |
| :--- | :--- | :--- |
| **Defense Evasion** | `ntdll` unhooking, `swi` trap doors, and anti-analysis string checks. | Protects the malware from being analyzed or detected by local security tools during its startup phase. |
| **Persistence & Prep** | Disabling Windows Defender via Registry; running `gpupdate`. | Ensures system protections are turned off before the main payload is executed. |
| **Network/C2** | Use of `InternetOpenUrlA` and `InternetReadFile`. | Connects to a remote server to download secondary payloads or updates. |
| **Payload Handling** | In-memory XOR/Subtraction decryption loop. | Decrypts the downloaded payload in memory so it never touches the disk in its "plain" form (Fileless execution). |
| **Stealth** | Use of large, complex library structures. | Masks malicious functionality within thousands of lines of seemingly legitimate code. |

---

### Final Conclusion and Risk Assessment
This binary is a **highly sophisticated primary-stage dropper**. It serves as the "scout" for an infection: it validates that the environment is not being monitored (Anti-Analysis), silences local alarms (disabling Defender), and then fetches a secondary, likely more specialized, payload from a remote server.

The use of **in-memory decryption** combined with **unhooking `ntdll`** indicates that this malware is designed to target environments with advanced EDR (Endpoint Detection and Response) systems. 

**Recommended Actions:**
1.  **Network Monitoring:** Look for outgoing connections to suspicious IPs/domains via the WinINet library.
2.  **Memory Analysis:** Since it performs in-memory decryption, traditional disk scans may miss the final payload. Memory scanning (e.g., YARA rules on memory) is essential.
3.  **Indicator of Compromise (IoC) Hunting:** Monitor for changes to Windows Defender registry keys and unauthorized `gpupdate` commands.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your report to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1105** | Ingress Tool Transfer | The malware uses `InternetOpenUrlA` and `InternetReadFile` to fetch additional payloads from a remote server. |
| **T1614** | Reflective Code Loading | The use of `VirtualAlloc` followed by in-memory XOR/subtraction decryption indicates the payload is executed in memory to avoid disk detection. |
| **T1497** | Virtualization, Debugger, or Sandbox Evasion | The inclusion of "gatekeeper" functions and `swi(0x29)` trap doors are designed to crash or deceive debuggers and analysis tools. |
| **T1083** | File and Directory Discovery | The use of `FindFirstFileExW` indicates the malware is searching for specific documents, sensitive files, or local configuration data. |
| **T1562.001** | Disable or Remove Security Software | The malware specifically targets Windows Defender via Registry modifications and the `gpupdate` command to disable system protections. |
| **T1027** | Software Packing | The use of a large, complex "wrapper" library is employed to obfuscate malicious functionality within thousands of lines of legitimate code. |
| **T1568** | Dynamic Resolution | While not explicitly detailed as a function, the use of `ntdll` unhooking is an evasion technique used to bypass EDR monitoring by resolving system calls directly. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `https://litter.cCLRCreateInstancatbox.moe/cfgqad` (Suspicious C2 or payload delivery URL)

**File paths / Registry keys**
*   `MicrosoftEdgeUpdateCore` (Scheduled Task name used for persistence)
*   Note: The analysis mentions "Disabling Windows Defender via Registry," though specific registry paths were not explicitly provided in the raw strings.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **User Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36`
*   **Command Line Patterns:** `schtasks.exe /create /tn "MicrosoftEdgeUpdateCore" /tr "rundll32.exe \"%s\",get_hostfxr_path" /sc onlogon /rl highest /f`
*   **Anti-Analysis/Sandbox Indicators:** 
    *   Strings: `cuckoo`, `cuckoosandbox`, `vmcheck`, `wilbert`, `analysis`, `sample`.
    *   Tools detected in code: `x64dbg`, `x32dbg`, `ollydbg`, `windbg`, `processhacker`, `fiddler`, `wireshark`, `procmon`, `apimonitor`, `pestudio`.
*   **Malware Behavior Markers:** 
    *   In-memory XOR/Subtraction decryption loops.
    *   `swi(0x29)` software interrupt trap doors (used to crash debuggers).
    *   Use of `InternetOpenUrlA` and `InternetReadFile` for remote payload retrieval.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `https://litter.cCLRCreateInstancatbox.moe/cfgqad`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader (or dropper)
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-stage Execution & In-Memory Decryption:** The malware exhibits classic "loader" behavior by fetching a remote payload via `InternetReadFile` and decrypting it in memory using XOR/subtraction operations, ensuring the final malicious payload never touches the disk in an unencrypted state.
*   **Advanced Anti-Analysis Infrastructure:** The inclusion of "gatekeeper" functions with `swi(0x29)` trap doors, combined with checks for common analysis tools (e.g., x64dbg, Wireshark), indicates a high level of sophistication designed to evade both automated sandboxes and manual reverse engineering.
*   **Persistence & Defense Evasion:** The malware actively modifies the system environment by disabling Windows Defender via registry keys and creating a scheduled task (`MicrosoftEdgeUpdateCore`) to ensure it—or its subsequent payload—remains active on the host.
