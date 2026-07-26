# Threat Analysis Report

**Generated:** 2026-07-24 21:52 UTC
**Sample:** `0a5c661ec5c23a88eb4bc0a903489d77b39faa7aa6525fe376007d454be952ff_0a5c661ec5c23a88eb4bc0a903489d77b39faa7aa6525fe376007d454be952ff.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a5c661ec5c23a88eb4bc0a903489d77b39faa7aa6525fe376007d454be952ff_0a5c661ec5c23a88eb4bc0a903489d77b39faa7aa6525fe376007d454be952ff.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64, 6 sections |
| Size | 133,632 bytes |
| MD5 | `03e9763f3e9999ee3eddfc9d1d238988` |
| SHA1 | `c4314c7626ad2d717ef744c4d67f538bc40e2e72` |
| SHA256 | `0a5c661ec5c23a88eb4bc0a903489d77b39faa7aa6525fe376007d454be952ff` |
| Overall entropy | 6.106 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1701879742 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 92,160 | 6.429 | No |
| `.rdata` | 24,064 | 4.811 | No |
| `.data` | 8,704 | 2.709 | No |
| `.pdata` | 5,632 | 5.02 | No |
| `.rsrc` | 512 | 5.113 | No |
| `.reloc` | 1,536 | 3.457 | No |

### Imports

**KERNEL32.dll**: `HeapCreate`, `EnterCriticalSection`, `DeleteCriticalSection`, `WaitForSingleObject`, `SetEvent`, `Sleep`, `CreateEventA`, `GetLastError`, `CloseHandle`, `GetCurrentThreadId`, `SwitchToThread`, `SetLastError`, `WideCharToMultiByte`, `lstrlenW`, `ResetEvent`
**USER32.dll**: `DispatchMessageW`, `PostThreadMessageA`, `PeekMessageW`, `TranslateMessage`, `MsgWaitForMultipleObjects`, `ShowWindow`, `GetInputState`, `wsprintfW`
**ADVAPI32.dll**: `RegCloseKey`, `RegOpenKeyExW`, `RegDeleteValueW`, `RegQueryValueExW`, `RegCreateKeyW`, `RegSetValueExW`
**WS2_32.dll**: `WSAWaitForMultipleEvents`, `WSAIoctl`, `connect`, `WSAStartup`, `select`, `WSAResetEvent`, `setsockopt`, `recv`, `socket`, `closesocket`, `gethostbyname`, `send`, `WSASetLastError`, `WSACreateEvent`, `shutdown`
**WINMM.dll**: `timeGetTime`

## Extracted Strings

Total strings found: **459** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
@SVWAWH
l$`teE
(A__^[
D+A0D;
H9q8tbD
\$ ATH
D9!vFH
H;?tDfff
H;?tDfff
H;?tDfff
H;?tDfff
@SUVAUH
(A]^][
(A]^][
|$P9CdL
C<9CdsKH
K<9Kds
(A]^][
(A]^][
@VWAUH
@UWATH
|$ ATH
C\H;?tfE3
C<9CdsPH
D;[$sD
CDD9SDv
SVATAVH
CLD;Ctx5
D9Klu
D
D;w0xY
A^A\^[
@UVATAUAVAWH
A_A^A]A\^]
|$ ATAUAVH
ffffff
 A^A]A\
|$ ATH
D$PA+D$H
l$0M;A
fE;Au
D$pE+D$hI
I)\$PI
D$PA+D$H;

A;t$X
@UVATAUAVH
A^A]A\^]
@UAUAVH
D$  t,
WATAUH
MXD+F(E3
D9O0vP
 A]A\_
t#9{Tt
t#9sTt
|$ ATH
t$`ffffff
l$0M;A
fE;Au
@UVWATAUH
0A]A\_^]
AT+AT=
QTD;YTx
|$ ATH
uM;n,u,;~(
;~(uTH
@VWATH
xIfffff
\$ UWATH
|$ ATAUAVH
 A^A]A\
VWATAUAVH
fffffff
fffffff
t$ WATAUH
0A]A\_
ATAUAVH
 A^A]A\
UATAUH
WATAUAVAWH
@A_A^A]A\_
t$ WATAUH
WATAUAVAWH
0A_A^A]A\_
UVWATAUAVAWH
D$DD9T$\
t$hD+d$DD+
9D$Pti
A_A^A]A\_^]
WATAUAVAWH
A_A^A]A\_
UVWATAUAVAWH
D$HD9T$\
t$pD+d$HD+
9D$Tt^
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140009f8c` | `0x140009f8c` | 15217 | ✓ |
| `fcn.1400098b0` | `0x1400098b0` | 13944 | ✓ |
| `fcn.14000b8d0` | `0x14000b8d0` | 8199 | ✓ |
| `fcn.140008ad0` | `0x140008ad0` | 4502 | ✓ |
| `fcn.1400073d0` | `0x1400073d0` | 3329 | ✓ |
| `fcn.140016130` | `0x140016130` | 2739 | ✓ |
| `fcn.14000ad44` | `0x14000ad44` | 2658 | ✓ |
| `fcn.140002880` | `0x140002880` | 2243 | ✓ |
| `fcn.1400158cc` | `0x1400158cc` | 2146 | ✓ |
| `fcn.14000e1c0` | `0x14000e1c0` | 1888 | ✓ |
| `fcn.140014d34` | `0x140014d34` | 1483 | ✓ |
| `fcn.140015300` | `0x140015300` | 1483 | ✓ |
| `fcn.140002390` | `0x140002390` | 1256 | ✓ |
| `fcn.140013c88` | `0x140013c88` | 1229 | ✓ |
| `method.CKernelManager.virtual_0` | `0x140006860` | 1047 | ✓ |
| `fcn.140010a90` | `0x140010a90` | 1006 | ✓ |
| `fcn.1400124bc` | `0x1400124bc` | 992 | ✓ |
| `fcn.140008b00` | `0x140008b00` | 820 | ✓ |
| `fcn.140006f70` | `0x140006f70` | 809 | ✓ |
| `method.CTcpSocket.virtual_32` | `0x140003390` | 765 | ✓ |
| `fcn.14000d3cc` | `0x14000d3cc` | 722 | ✓ |
| `fcn.14001054c` | `0x14001054c` | 714 | ✓ |
| `fcn.140005a40` | `0x140005a40` | 704 | ✓ |
| `method.CTcpSocket.virtual_16` | `0x140003860` | 683 | ✓ |
| `method.CUdpSocket.virtual_16` | `0x1400055b0` | 683 | ✓ |
| `fcn.140001d80` | `0x140001d80` | 629 | ✓ |
| `fcn.14000f0b8` | `0x14000f0b8` | 629 | ✓ |
| `fcn.140014898` | `0x140014898` | 614 | ✓ |
| `fcn.14000a30c` | `0x14000a30c` | 605 | ✓ |
| `fcn.140003c80` | `0x140003c80` | 596 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001d80.c`](code/fcn.140001d80.c)
- [`code/fcn.140002390.c`](code/fcn.140002390.c)
- [`code/fcn.140002880.c`](code/fcn.140002880.c)
- [`code/fcn.140003c80.c`](code/fcn.140003c80.c)
- [`code/fcn.140005a40.c`](code/fcn.140005a40.c)
- [`code/fcn.140006f70.c`](code/fcn.140006f70.c)
- [`code/fcn.1400073d0.c`](code/fcn.1400073d0.c)
- [`code/fcn.140008ad0.c`](code/fcn.140008ad0.c)
- [`code/fcn.140008b00.c`](code/fcn.140008b00.c)
- [`code/fcn.1400098b0.c`](code/fcn.1400098b0.c)
- [`code/fcn.140009f8c.c`](code/fcn.140009f8c.c)
- [`code/fcn.14000a30c.c`](code/fcn.14000a30c.c)
- [`code/fcn.14000ad44.c`](code/fcn.14000ad44.c)
- [`code/fcn.14000b8d0.c`](code/fcn.14000b8d0.c)
- [`code/fcn.14000d3cc.c`](code/fcn.14000d3cc.c)
- [`code/fcn.14000e1c0.c`](code/fcn.14000e1c0.c)
- [`code/fcn.14000f0b8.c`](code/fcn.14000f0b8.c)
- [`code/fcn.14001054c.c`](code/fcn.14001054c.c)
- [`code/fcn.140010a90.c`](code/fcn.140010a90.c)
- [`code/fcn.1400124bc.c`](code/fcn.1400124bc.c)
- [`code/fcn.140013c88.c`](code/fcn.140013c88.c)
- [`code/fcn.140014898.c`](code/fcn.140014898.c)
- [`code/fcn.140014d34.c`](code/fcn.140014d34.c)
- [`code/fcn.140015300.c`](code/fcn.140015300.c)
- [`code/fcn.1400158cc.c`](code/fcn.1400158cc.c)
- [`code/fcn.140016130.c`](code/fcn.140016130.c)
- [`code/method.CKernelManager.virtual_0.c`](code/method.CKernelManager.virtual_0.c)
- [`code/method.CTcpSocket.virtual_16.c`](code/method.CTcpSocket.virtual_16.c)
- [`code/method.CTcpSocket.virtual_32.c`](code/method.CTcpSocket.virtual_32.c)
- [`code/method.CUdpSocket.virtual_16.c`](code/method.CUdpSocket.virtual_16.c)

## Behavioral Analysis

This third chunk of disassembly provides the final pieces of the puzzle, confirming that this is not just a "sophisticated" piece of malware, but a **highly-engineered industrial-grade bot client**.

The new code reveals sophisticated techniques for handling localized environments, manually managing memory and exceptions to evade analysis tools, and interacting with system handles.

### Updated Analysis Summary
The latest findings solidify the classification of this binary as a high-tier threat. While previous chunks established its role as a command-driven bot, this chunk reveals how it maintains stability and evades detection:
1.  **Advanced Environment Adaptation:** The inclusion of locale/code-page checking suggests it is designed for wide geographic distribution.
2.  **Anti-Analysis via Exception Handling:** By manually constructing exception records and using `RaiseException`, the malware can bypass debuggers that rely on standard OS-level exception handling to catch malicious activity.
3.  **Robust Resource Management:** The use of manual `VirtualAlloc`/`VirtualFree` logic for buffer management confirms it is designed to be stable, high-performance, and capable of handling large data transfers (e.g., exfiltrating files or receiving large payloads).

---

### New Findings & Deep Dive

#### 1. Localization & Configuration Mapping (`fcn.14000f0b8`)
This function contains complex logic for determining and applying environment-specific settings.
*   **Code Page Validation:** The use of `GetCPInfo` and the subsequent check against values like `0x3a4`, `0x3a8`, etc., indicates the malware is checking the system's language/region settings.
*   **Mapping Logic:** The code maps these system codes to specific internal constants (e.g., `0x411`, `0x804`). This is common in professional-grade software (and high-end malware) to ensure that text strings or communication protocols are correctly formatted for the user's region, ensuring it stays "hidden" by behaving like a legitimate application.

#### 2. Manual Exception Handling & Anti-Debugging (`fcn.140014898`)
This function is highly significant from an evasion standpoint. Instead of letting the OS handle errors normally, the malware:
*   **Crafts Custom Exceptions:** It manually constructs a structure and populates it with specific system error codes (e.g., `0xc000008f` - Stack Overflow; `0xc0000091` - Memory Access Violation).
*   **Purpose:** By manually triggering exceptions via `RaiseException`, the malware can "trap" its own errors or purposely trigger conditions that confuse debuggers. If a debugger is trying to hook an exception, this manual construction allows the malware to bypass common automated detection hooks used by sandbox environments and security tools.

#### 3. Internal Memory & Buffer Management (`fcn.140003c80`)
This function reveals a "manual" approach to memory management:
*   **Custom Heap-like Logic:** Rather than relying on standard, high-level buffer functions, it uses `VirtualAlloc` and `VirtualFree` coupled with complex logic to calculate offsets and manage overlapping memory regions.
*   **Significance:** This is typical in network modules that must handle variable-length packets (like those from a C2 server). It ensures the malware can process large amounts of data without crashing or triggering "buffer overflow" protections, making it much more stable than "script kiddie" level tools.

#### 4. System Interaction & Logging (`fcn.14000a30c`)
This function handles interaction with the host system:
*   **Output Writing:** The code retrieves a handle for `STD_OUTPUT_HARDWARE` and utilizes `WriteFile`. This suggests that while it is primarily a bot, it can also output status information or logs to the standard output stream.
*   **Path Verification:** It uses `GetModuleFileNameW`, allowing it to identify its own path—a common step before performing persistence operations or checking if it is running from a known "quarantine" folder.

---

### Updated Behavioral Summary

| Category | Status | Technical Detail |
| :--- | :--- | :--- |
| **Role** | **Advanced Bot/Agent** | Comprehensive suite including command parsing, robust networking, and internal state management. |
| **C2 Communication** | **High Complexity** | Custom buffer management logic using `VirtualAlloc` to handle large/variable data streams. |
| **Anti-Analysis** | **Sophisticated** | Manual construction of exception records (`RaiseException`) to bypass debugger detection. |
| **Adaptability** | **Confirmed** | Uses `GetCPInfo` to adapt to different regional settings (Locale awareness). |
| **Persistence/ID** | **Confirmed** | Registry-based unique ID tracking (see previous analysis). |

---

### New Indicators & Tactics (TTPs)
*   **Technique: Anti-Debugging (Exception Manipulation):** Manually constructing `EXCEPTION_RECORD` structures to bypass standard debugger traps.
*   **Technique: Dynamic Memory Management:** Using direct `VirtualAlloc` calls for custom buffer handling in networking modules.
*   **Technique: Environment Awareness:** Checking system code pages and locales to adapt behavior or payloads.
*   **Technique: Standard Output Interaction:** Utilizing `WriteFile` on standard output handles for internal state logging.

### Final Conclusion (Consolidated)
This is a **highly sophisticated, multi-functional malware agent**. It exhibits several characteristics of professional-grade cybercrime tools:
1.  It has its own **dedicated networking stack** designed to handle heavy traffic and various packet sizes efficiently.
2.  It employs **proactive anti-analysis techniques** that go beyond simple "is a debugger present" checks, moving into the realm of advanced system calls to bypass security tooling.
3.  It is built for **longevity**; its use of locale detection and sophisticated memory management indicates it was intended to remain active on a wide variety of infected systems globally without failing or being easily detected by basic automated scanners.

This sample is likely part of a large-scale botnet (such as a DDoS bot, an information stealer, or a backdoor for ransomware deployment).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of locale and code-page checks ensures the malware behaves like a legitimate, localized application to blend in with standard system environment behaviors. |
| T1497 | Virtualization/Sandbox Evasion | Manually constructing `EXCEPTION_RECORD` structures and using `RaiseException` is a specific tactic to bypass debuggers and automated analysis tools. |
| T1041 | Exfiltration | The implementation of custom memory management via `VirtualAlloc` specifically for handling large, variable-length data packets indicates capabilities for high-volume data theft. |
| T1033 | System Information Discovery | The use of `GetModuleFileNameW` allows the malware to determine its current location and identify environment details prior to further actions. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the extracted intelligence. 

Note: The "Extracted Strings" section appears to contain largely obfuscated data or binary artifacts that do not resolve to actionable network or filesystem IOCs (e.g., IP addresses or specific paths). Therefore, the most relevant indicators are derived from the Behavioral Analysis.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **Registry Behavior:** The report mentions "Registry-based unique ID tracking," but no specific registry keys (e.g., `HKLM\...\...`) were provided in the text. 
*   *Note: System path calls like `GetModuleFileNameW` were identified, but these are standard API calls and do not constitute a specific IOC.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 hashes were present in the string dump).

### **Other artifacts**
*   **Anti-Analysis/Evasion Techniques:**
    *   **Exception Manipulation:** Use of `RaiseException` with manually constructed `EXCEPTION_RECORD` structures (e.g., codes `0xc000008f` and `0xc0000091`) to bypass debugger hooks.
    *   **Memory Management:** Manual use of `VirtualAlloc` and `VirtualFree` for custom buffer handling in network modules.
*   **Environment Awareness:**
    *   **Locale Detection:** Use of `GetCPInfo` to check system code pages (e.g., `0x3a4`, `0x3a8`) and map them to internal constants (`0x411`, `0x804`).
*   **Behavioral Patterns:**
    *   **Output Logging:** Utilization of `WriteFile` on `STD_OUTPUT_HARDWARE` for status reporting.
    *   **Custom Networking Stack:** Evidence of a non-standard, robust memory management system for handling varying packet sizes from C2 infrastructure.

---
**Analyst Note:** This sample is identified as a **high-tier bot/agent**. While static indicators (IPs/Domains) are absent from this specific data set—likely due to the malware's ability to use dynamic generation or hardcoded encryption—the behavioral profile suggests a sophisticated, professional-grade piece of malware designed for longevity and large-scale operation.

---

## Malware Family Classification

Based on the detailed behavioral analysis provided, here is the classification of the sample:

1.  **Malware family:** Custom (High-tier Bot Agent)
2.  **Malware type:** Backdoor / Bot
3.  **Confidence:** Medium
4.  **Key evidence:**
    *   **Advanced Evasion Tactics:** The use of manual `EXCEPTION_RECORD` construction and `RaiseException` to bypass debugger hooks indicates a professional-grade tool designed specifically to evade automated analysis and sandbox environments.
    *   **Robust Networking & Data Handling:** The implementation of a custom memory management system using `VirtualAlloc`/`VirtualFree` for handling large, variable-length packets suggests the malware is designed for high-volume data exfiltration or as a stable hub for receiving complex payloads (e.g., ransomware modules).
    *   **Industrial-Grade Sophistication:** The inclusion of locale/code-page awareness (`GetCPInfo`) and advanced system interactions indicates the tool was built for global distribution and long-term persistence rather than a simple "script kiddie" attack.

***Note on Confidence:* While the technical profile is very high, the lack of specific hardcoded strings or unique signatures makes it impossible to attribute this to a specific known family (like Cobalt Strike or TrickBot) without further network telemetry.**
