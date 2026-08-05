# Threat Analysis Report

**Generated:** 2026-08-03 12:43 UTC
**Sample:** `0cb41498169b1cf30b931d7c067fcd372169d9e38515920efb34dddc24bd8f1e_0cb41498169b1cf30b931d7c067fcd372169d9e38515920efb34dddc24bd8f1e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0cb41498169b1cf30b931d7c067fcd372169d9e38515920efb34dddc24bd8f1e_0cb41498169b1cf30b931d7c067fcd372169d9e38515920efb34dddc24bd8f1e.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 38,400 bytes |
| MD5 | `272815fcb3cba0c66b43068f00a68356` |
| SHA1 | `1116db74b5b640075f0b6991380fed9e84389bfb` |
| SHA256 | `0cb41498169b1cf30b931d7c067fcd372169d9e38515920efb34dddc24bd8f1e` |
| Overall entropy | 5.734 |
| Unpacked | No |

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
| `fcn.00401180` | `0x401180` | 832 | ✓ |
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

### Overview
The analyzed binary is a **DDoS (Distributed Denial of Service) Bot**. Its primary purpose is to join a botnet and perform various network-based attacks against targets specified by a Command & Control (C&C) server. It includes multiple modules for different types of flooding attacks and contains functionality for local persistence and internal networking management.

### Core Functionality
*   **Multi-Vector Attack Suite:** The code contains specific logic for several types of DDoS attacks, including:
    *   **TCP & TCP-RAND:** Standard TCP flooding.
    *   **UDP & NUDP:** UDP-based flooding.
    *   **ICMP Flood:** Ping flooding.
    *   **Targeted Attacks:** Specific modules exist for "SAMP" (likely targeting gaming servers), "Discord," and "TS3" (TeamSpeak 3).
*   **C&C Communication:** The malware resolves a domain via `getaddrinfo`, establishes a connection to a remote server, and enters a loop to receive commands. It sends local system information (like the Windows version) to the controller upon connecting.
*   **Multi-threading:** The binary utilizes `CreateThread` to launch various attack types simultaneously, allowing it to perform multiple tasks or manage multiple threads for a single high-volume attack.

### Suspicious and Malicious Behaviors
*   **Persistence Mechanism:** 
    *   The code specifically targets the **Windows Startup folder**. It uses `SHGetSpecialFolderPathA` to find this directory and contains logic to copy, rename, or move its own executable into that folder to ensure it starts automatically every time the system boots.
*   **C&C Communication & "Bot" Logic:** 
    *   The use of a **Global Mutex** (`Global\MyBotMutex`) is a common technique to ensure only one instance of the malware is running on a single machine at a time.
    *   The inclusion of a "retry" logic for DNS resolution and socket creation indicates it is designed to stay active even if connection attempts are initially blocked.
*   **Network Disruption (TCP Killing):** 
    *   The binary uses `iphlpapi.dll` (specifically `GetTcpTable` and `SetTcpEntry`) to scan the system for active TCP connections on specific ports and forcibly terminate them ("killing" the connection). This is often used in "stresser" tools to clear local connections or disrupt network flows.
*   **System Reconnaissance:** 
    *   The use of `RtlGetVersion` suggests it checks the OS version, which can be used for fingerprinting the target environment or as a rudimentary anti-analysis check to see if the environment is "standard" enough to operate in.

### Notable Techniques & Patterns
*   **Modular Attack Design:** The large `switch` statement (found in `fcn.00403d1a`) shows it acts as a "swiss army knife" for DDoS attacks, switching between different methods based on received instructions or configuration.
*   **Standard Botnet Architecture:** The flow of *Mutex check $\rightarrow$ Local Env Gathering $\rightarrow$ C&C Connection $\rightarrow$ Remote Instruction Reception $\rightarrow$ Multithreaded Attack Execution* is a classic pattern found in Mirai-style botnets and similar malware.
*   **Internal Management:** Function `fcn.00405100` calls `VirtualProtect`, suggesting it may be managing memory permissions for the various attack modules or dynamically loading/executing code blocks to stay active.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1498.001** | Network DoS: Flood | The binary contains specific modules for TCP, UDP, and ICMP flooding to overwhelm target network services. |
| **T1547.001** | Boot or Logon Autostart Execution: Startup Folder | The malware copies itself into the Windows Startup folder to ensure persistence across system reboots. |
| **T1071** | Application Layer Protocol | The binary establishes a connection to a remote C&C server and enters a loop to receive instructions via standard protocols. |
| **T1568.002** | DNS | The malware uses `getaddrinfo` to resolve the domain name of the Command & Control server before establishing a connection. |
| **T1038** | System Information Discovery | The use of `RtlGetVersion` indicates an attempt to gather OS details for fingerprinting or basic environment checks. |
| **T1106** | Native API | The use of `VirtualProtect` suggests the malware is manipulating memory permissions to manage its internal modules or execute code blocks. |
| **T1498** | Network DoS | The "TCP Killing" functionality using `iphlpapi.dll` aims to disrupt network flows and terminate active connections. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `debug-win.duckdns.org` (Identified as a C&C communication point)

**File paths / Registry keys**
*   **Startup Folder:** The malware specifically targets and utilizes the Windows Startup directory for persistence by moving/copying its executable into this location.

**Mutex names / Named pipes**
*   `Global\MyBotMutex` (Used to ensure only one instance of the bot is running)

**Hashes**
*   *None identified in the provided text.*

**Other artifacts**
*   **C2 Behavior:** The malware employs `getaddrinfo` for DNS resolution and includes retry logic for both DNS resolution and socket creation when connection attempts fail.
*   **Persistence Mechanism:** Use of the `SHGetSpecialFolderPathA` API to identify and target the Startup folder.
*   **Network Manipulation:** Integration of `iphlpapi.dll` (specifically functions `GetTcpTable` and `SetTcpEntry`) to identify and "kill" local TCP connections.
*   **Environment Check:** Use of `RtlGetVersion` for environment fingerprinting.
*   **Malicious Functionality:** The binary contains specific modules/hardcoded strings for various DDoS attack vectors:
    *   TCP & TCP-RAND
    *   NTCP
    *   UDP & NUDP
    *   ICMP Flood
    *   Targeted services: SAMP, Discord, and TS3 (TeamSpeak 3).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `debug-win.duckdns.org`

---

## Malware Family Classification

1. **Malware family**: Unknown (Note: While it follows a "Mirai-style" architecture common in DDoS botnets, no specific brand name like "Mantis" or similar was identified).
2. **Malware type**: bot (DDoS Bot)
3. **Confidence**: High
4. **Key evidence**:
    *   **Multi-Vector Attack Capabilities:** The binary contains explicit modules for various flood types (TCP, UDP, ICMP) and specifically targets gaming and communication platforms like SAMP, Discord, and TeamSpeak 3.
    *   **Botnet Infrastructure:** It exhibits classic botnet behaviors including a Command & Control (C&C) loop, the use of Global Mutexes (`Global\MyBotMutex`) to manage instances, and automatic persistence via the Windows Startup folder.
    *   **Network Manipulation:** The inclusion of "TCP Killing" functionality using `iphlpapi.dll` is characteristic of "stresser" tools used to disrupt network flows or clear local connections during an attack.
