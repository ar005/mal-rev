# Threat Analysis Report

**Generated:** 2026-06-24 16:31 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32+ executable for MS Windows 5.02 (console), x86-64 (stripped to external PDB), 3 sections |
| Size | 17,920 bytes |
| MD5 | `2aa341bbbd08b13dc67180290ff3744e` |
| SHA1 | `972f5bccfaed3dc6a34b751c83067fc571de1da1` |
| SHA256 | `0092092221e075cb353dab1ff492ebdfaef387898440ac958979dad93d5b10d0` |
| Overall entropy | 5.734 |
| Unpacked | ✓ Yes (tool: upx) |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 22,016 | 6.123 | No |
| `.data` | 512 | 0.821 | No |
| `.rdata` | 5,632 | 5.141 | No |
| `.pdata` | 1,536 | 3.578 | No |
| `.xdata` | 1,536 | 4.275 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 4,096 | 3.563 | No |
| `.CRT` | 512 | 0.271 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 1,024 | 3.079 | No |

### Imports

**KERNEL32.DLL**: `CloseHandle`, `CopyFileA`, `CreateMutexA`, `CreateThread`, `DeleteCriticalSection`, `DeleteFileA`, `EnterCriticalSection`, `ExitProcess`, `FreeLibrary`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetLastError`, `GetModuleFileNameA`, `GetModuleHandleW`
**ADVAPI32.dll**: `CryptAcquireContextA`, `CryptGenRandom`, `CryptReleaseContext`
**msvcrt.dll**: `__C_specific_handler`, `__getmainargs`, `__initenv`, `__iob_func`, `__lconv_init`, `__set_app_type`, `__setusermatherr`, `_acmdln`, `_amsg_exit`, `_cexit`, `_exit`, `_fmode`, `_initterm`, `_onexit`, `_time64`
**SHELL32.dll**: `SHGetSpecialFolderPathA`
**WS2_32.dll**: `WSACleanup`, `WSAGetLastError`, `WSASocketA`, `WSAStartup`, `bind`, `closesocket`, `connect`, `freeaddrinfo`, `getaddrinfo`, `htons`, `inet_addr`, `inet_ntoa`, `inet_ntop`, `ioctlsocket`, `ntohl`

## Extracted Strings

Total strings found: **345** (showing first 100)

```
!This program cannot be run in DOS mode.
$
P`.data
.rdata
`@.pdata
0@.xdata
0@.bss
.idata
AUATUWVSH
[^_]A\A]
[^_]A\A]
AUATUWVSH
IcL$H)
[^_]A\A]
AWAVAUATUWVSH
[^_]A\A]A^A_
UAWAVAUATWVSH
IcT$H+E
[^_A\A]A^A_]
UAWAVAUATWVSH
IcMH+E
[^_A\A]A^A_]
UAWAVAUATWVSH
Mc]H+E
[^_A\A]A^A_]
AWAVAUATUWVSH
8[^_]A\A]A^A_
8[^_]A\A]A^A_
AWAVAUATUWVSH
8[^_]A\A]A^A_
8[^_]A\A]A^A_
AWAVAUATUWVSH
H[^_]A\A]A^A_
H[^_]A\A]A^A_
AVAUATUWVSH
IcT$H)
[^_]A\A]A^
AWAVAUATUWVSH
IcT$H)
X[^_]A\A]A^A_
AVAUATUWVSH
IcT$H)
P[^_]A\A]A^
AVAUATUWVSH
IcT$H)
[^_]A\A]A^
AVAUATUWVSH
IcT$H)
D$hH3E
p[^_]A\A]A^
AVAUATUWVSH
IcT$H)
[^_]A\A]A^
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
t$HH31t
X[^_]A\A]A^A_
AUATWSH
h[_A\A]
AWAVAUATUWVSH
L$lD9L$h
HcD$PA
[^_]A\A]A^A_
AUATUWVSH
[^_]A\A]
AUATWVSH
[^_A\A]
AUATVSH
[^A\A]
AUATWVSH
[^_A\A]
UAVAUATWVSH
ATUWVSH
0[^_]A\
0[^_]A\
ATUWVSH
P[^_]A\
P[^_]A\
UAWAVAUATWVSH
[^_A\A]A^A_]
ATUWVSH
 [^_]A\
ATWVSH
([^_A\H
tNHcA<H
tTIcB<L
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00404a10` | `0x404a10` | 13658 | ✓ |
| `fcn.004048a0` | `0x4048a0` | 7298 | ✓ |
| `fcn.00405440` | `0x405440` | 3094 | ✓ |
| `fcn.00403d1a` | `0x403d1a` | 1111 | ✓ |
| `fcn.00401180` | `0x401180` | 866 | ✓ |
| `fcn.00405100` | `0x405100` | 817 | ✓ |
| `fcn.00403b3d` | `0x403b3d` | 789 | ✓ |
| `fcn.00406250` | `0x406250` | 708 | ✓ |
| `fcn.00404ef0` | `0x404ef0` | 528 | ✓ |
| `fcn.0040222a` | `0x40222a` | 404 | ✓ |
| `fcn.004023be` | `0x4023be` | 404 | ✓ |
| `fcn.004036ef` | `0x4036ef` | 379 | ✓ |
| `fcn.00404566` | `0x404566` | 373 | ✓ |
| `fcn.00402fff` | `0x402fff` | 292 | ✓ |
| `fcn.00403450` | `0x403450` | 292 | ✓ |
| `fcn.00404448` | `0x404448` | 286 | ✓ |
| `fcn.00404171` | `0x404171` | 282 | ✓ |
| `fcn.004046db` | `0x4046db` | 274 | ✓ |
| `fcn.00402ef0` | `0x402ef0` | 271 | ✓ |
| `fcn.00403232` | `0x403232` | 271 | ✓ |
| `fcn.00403123` | `0x403123` | 271 | ✓ |
| `fcn.00403341` | `0x403341` | 271 | ✓ |
| `fcn.00405610` | `0x405610` | 250 | ✓ |
| `fcn.00401743` | `0x401743` | 245 | ✓ |
| `fcn.00405a40` | `0x405a40` | 224 | ✓ |
| `fcn.00405f40` | `0x405f40` | 222 | ✓ |
| `fcn.00403c3c` | `0x403c3c` | 222 | ✓ |
| `fcn.0040428b` | `0x40428b` | 220 | ✓ |
| `fcn.00404ac0` | `0x404ac0` | 214 | ✓ |
| `fcn.00405bb0` | `0x405bb0` | 159 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401180.c`](code/fcn.00401180.c)
- [`code/fcn.00401743.c`](code/fcn.00401743.c)
- [`code/fcn.0040222a.c`](code/fcn.0040222a.c)
- [`code/fcn.004023be.c`](code/fcn.004023be.c)
- [`code/fcn.00402ef0.c`](code/fcn.00402ef0.c)
- [`code/fcn.00402fff.c`](code/fcn.00402fff.c)
- [`code/fcn.00403123.c`](code/fcn.00403123.c)
- [`code/fcn.00403232.c`](code/fcn.00403232.c)
- [`code/fcn.00403341.c`](code/fcn.00403341.c)
- [`code/fcn.00403450.c`](code/fcn.00403450.c)
- [`code/fcn.004036ef.c`](code/fcn.004036ef.c)
- [`code/fcn.00403b3d.c`](code/fcn.00403b3d.c)
- [`code/fcn.00403c3c.c`](code/fcn.00403c3c.c)
- [`code/fcn.00403d1a.c`](code/fcn.00403d1a.c)
- [`code/fcn.00404171.c`](code/fcn.00404171.c)
- [`code/fcn.0040428b.c`](code/fcn.0040428b.c)
- [`code/fcn.00404448.c`](code/fcn.00404448.c)
- [`code/fcn.00404566.c`](code/fcn.00404566.c)
- [`code/fcn.004046db.c`](code/fcn.004046db.c)
- [`code/fcn.004048a0.c`](code/fcn.004048a0.c)
- [`code/fcn.00404a10.c`](code/fcn.00404a10.c)
- [`code/fcn.00404ac0.c`](code/fcn.00404ac0.c)
- [`code/fcn.00404ef0.c`](code/fcn.00404ef0.c)
- [`code/fcn.00405100.c`](code/fcn.00405100.c)
- [`code/fcn.00405440.c`](code/fcn.00405440.c)
- [`code/fcn.00405610.c`](code/fcn.00405610.c)
- [`code/fcn.00405a40.c`](code/fcn.00405a40.c)
- [`code/fcn.00405bb0.c`](code/fcn.00405bb0.c)
- [`code/fcn.00405f40.c`](code/fcn.00405f40.c)
- [`code/fcn.00406250.c`](code/fcn.00406250.c)

## Behavioral Analysis

Based on the provided strings and decompiled code, this binary is a **highly sophisticated DDoS (Distributed Denial of Service) bot**. It is designed to be part of a botnet where it receives instructions from a remote server and executes various network attacks against targeted IPs.

### Core Functionality and Purpose
*   **Multi-Vector Attack Tool:** The binary contains logic for multiple types of network attacks, including:
    *   **TCP Attacks:** Standard TCP, "TCP-RAND" (randomized), and "NTCP".
    *   **UDP Attacks:** General UDP, "NUDP", and "UDP Payload" attacks.
    *   **Application-Specific Attacks:** Specialized modules for **Discord**, **TS3 (TeamSpeak 3)**, **SAMP (San Andreas Multiplayer)**, and **PPS** (Packets Per Second) floods.
    *   **ICMP Floods:** Standard Ping floods.
*   **Multi-Threading:** The code uses `CreateThread` and `WaitForMultipleObjects` to launch multiple attack threads simultaneously, maximizing the volume of traffic sent to a target.

### Suspicious and Malicious Behaviors
*   **Command & Control (C&C) Communication:** 
    *   The binary actively attempts to connect to a remote server (e.g., `debug-win.duckdns.org`) using DNS resolution (`getaddrinfo`).
    *   It enters a "wait and retry" loop if the connection fails, ensuring it stays connected to receive instructions.
    *   Upon connection, it sends a check-in packet and waits for commands from the operator.
*   **Persistence Mechanism:** 
    *   The code includes logic to automatically copy itself into the **Windows Startup folder**.
    *   It performs "cleanup" of existing files in the startup directory before moving its own executable there to ensure it remains active after a system reboot.
*   **Connection Manipulation (TCP Killing):**
    *   The binary uses `iphlpapi.dll` (`GetTcpTable` and `SetTcpEntry`) to identify and forcibly "kill" existing TCP connections on specific ports. This is likely used to ensure that local connections do not interfere with the attack or to clear pathways for its own traffic.
*   **Evasion & Anti-Analysis:**
    *   **Mutex Creation:** It creates a global mutex (`Global\MyBotMutex`) to ensure only one instance of the bot is running on a single machine at once.
    *   **Environment Checks:** The use of `RtlGetVersion` and various performance counter checks suggests it may be looking for signs of being run in a virtualized or debugged environment.

### Notable Techniques & Patterns
*   **Modular Attack Logic:** The switch-case block (e.g., at `fcn.00403d1a`) shows how the bot interprets command codes from the C&C server to choose which specific attack module to launch.
*   **Tactic of "Self-Cleaning":** Before establishing its persistence, it attempts to delete its original file and rename itself in the startup folder, a common tactic to hide its origin.
*   **Robust Networking:** The inclusion of `select` logic for connection timeouts (`fcn.00404171`) indicates an attempt to make the C&C communication stable under poor network conditions.

### Summary Table
| Feature | Observation |
| :--- | :--- |
| **Type** | DDoS Bot / Stresser Tool |
| **Persistence** | Startup Folder copy & rename |
| **Network Activity** | C&C Communication (UDP/TCP), DoS Floods (ICMP, UDP, TCP) |
| **Anti-Analysis** | Mutex check, System Version checks |
| **Tools Used** | `iphlpapi.dll` (Table manipulation), `WinSock2` (Network ops) |

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors of the identified DDoS bot to the relevant MITRE ATT&CK techniques and sub-techniques based on your analysis.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1498** | Network Denial of Service | The primary purpose of the binary is to perform multi-vector floods (TCP, UDP, ICMP) against target infrastructure. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys/Startup Folder | The malware copies itself into the Windows Startup folder to ensure persistence after a system reboot. |
| **T1071.001** | Application Layer Protocol: Web Services | The binary communicates with a remote C&C server via network protocols (implied by use of `getaddrinfo` and duckdns) to receive instructions. |
| **T1583.003** | Domain Services: DNS | The bot utilizes `getaddrinfo` and a specific duckdns domain to resolve its Command & Control infrastructure. |
| **T1497** | Virtualization/Sandbox Detection | The use of `RtlGetVersion` and performance counter checks suggests the bot is screening for analysis environments before executing. |
| **T1070.004** | Indicator Removal on Host: File Deletion | The "self-cleaning" behavior where it deletes its original file and renames itself serves to hide its origin from forensic analysis. |
| **T1562.003** | Impair Defenses: Disable or Modify Tools (Network) | The use of `iphlpapi.dll` to "kill" local TCP connections is an attempt to manipulate the network environment to facilitate the attack. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `debug-win.duckdns.org` (Identified as a C&C server)

**File paths / Registry keys**
*   **Startup Folder:** The binary exhibits behavior to copy and rename itself into the Windows Startup folder for persistence.

**Mutex names / Named pipes**
*   `Global\MyBotMutex` (Used to ensure only one instance of the bot is running)

**Hashes**
*   None identified in the provided strings.

**Other artifacts**
*   **C2 Communication Pattern:** Utilization of DuckDNS for dynamic DNS resolution to connect to a remote command server.
*   **Persistence Mechanism:** "Self-cleaning" routine where the binary deletes its original file and renames itself upon moving to the startup directory.
*   **Network Manipulation:** Use of `iphlpapi.dll` (`GetTcpTable`, `SetTcpEntry`) to identify and terminate local TCP connections on specific ports.
*   **Attack Vectors Identified:** 
    *   TCP (Standard, RAND, NTCP)
    *   UDP (Standard, NUDP, Payload)
    *   ICMP Flood
    *   Application-specific targets: Discord, TeamSpeak 3 (TS3), SAMP (San Andreas Multiplayer).

---

## Malware Family Classification

1. **Malware family**: custom (DDoS Bot)
2. **Malware type**: bot
3. **Confidence**: High
4. **Key evidence**: 
*   **Multi-Vector Attack Capabilities:** The binary contains dedicated modules for a wide range of network attacks including TCP, UDP, ICMP, and application-specific floods (Discord, TeamSpeak 3, SAMP).
*   **Command & Control (C&C) Infrastructure:** It employs robust networking logic, including "wait and retry" loops and DuckDNS resolution, to receive instructions from a remote server.
*   **Persistence & Evasion:** The malware utilizes "self-cleaning" tactics (deleting the original file while moving to the Startup folder), mutex creation (`Global\MyBotMutex`), and environmental checks to maintain a presence on the host while evading detection.
