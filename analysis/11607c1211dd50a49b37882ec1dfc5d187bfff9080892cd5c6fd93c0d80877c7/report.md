# Threat Analysis Report

**Generated:** 2026-08-23 17:53 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 3 sections |
| Size | 31,232 bytes |
| MD5 | `dbae439a80cd9eb811fe4d4939f2e89f` |
| SHA1 | `ce6505c4ff4295ed38ccba649efbfd799f9440b8` |
| SHA256 | `11607c1211dd50a49b37882ec1dfc5d187bfff9080892cd5c6fd93c0d80877c7` |
| Overall entropy | 6.078 |
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
| `.text` | 42,496 | 6.242 | No |
| `.data` | 512 | 1.001 | No |
| `.rdata` | 6,656 | 5.453 | No |
| `.pdata` | 2,048 | 4.282 | No |
| `.xdata` | 2,048 | 4.593 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 4,096 | 3.733 | No |
| `.CRT` | 512 | 0.341 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 1,024 | 3.086 | No |
| `.reloc` | 512 | 1.755 | No |

### Imports

**KERNEL32.DLL**: `CloseHandle`, `CopyFileA`, `CreateMutexA`, `CreateThread`, `DeleteCriticalSection`, `DeleteFileA`, `EnterCriticalSection`, `ExitProcess`, `FreeLibrary`, `GetCurrentProcessId`, `GetLastError`, `GetModuleFileNameA`, `GetModuleHandleW`, `GetProcAddress`, `GetStartupInfoA`
**ADVAPI32.dll**: `CryptAcquireContextA`, `CryptGenRandom`, `CryptReleaseContext`
**msvcrt.dll**: `__C_specific_handler`, `___lc_codepage_func`, `___mb_cur_max_func`, `__getmainargs`, `__initenv`, `__iob_func`, `__lconv_init`, `__set_app_type`, `__setusermatherr`, `_acmdln`, `_amsg_exit`, `_cexit`, `_commode`, `_errno`, `_exit`
**SHELL32.dll**: `SHGetSpecialFolderPathA`
**WS2_32.dll**: `WSACleanup`, `WSAGetLastError`, `WSASocketA`, `WSAStartup`, `bind`, `closesocket`, `connect`, `freeaddrinfo`, `getaddrinfo`, `htons`, `inet_addr`, `inet_ntoa`, `inet_ntop`, `ioctlsocket`, `ntohl`

## Extracted Strings

Total strings found: **415** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
.reloc
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
D$hH+E
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
t$HH+1t
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
P[^_]A\
P[^_]A\
UAWAVAUATWVSH
[^_A\A]A^A_]
ATWVSH
([^_A\H
tNHcA<H
tTIcB<L
t	HcA<
tCHcA<H
@' t	M
tKIcA<L
tSIcK<L
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140004ac0` | `0x140004ac0` | 27026 | ✓ |
| `fcn.140005490` | `0x140005490` | 21774 | ✓ |
| `fcn.140008400` | `0x140008400` | 5850 | ✓ |
| `fcn.140007850` | `0x140007850` | 2376 | ✓ |
| `fcn.1400072d0` | `0x1400072d0` | 1394 | ✓ |
| `fcn.140006e30` | `0x140006e30` | 1172 | ✓ |
| `fcn.140003ec5` | `0x140003ec5` | 1111 | ✓ |
| `fcn.140006320` | `0x140006320` | 945 | ✓ |
| `fcn.1400067b0` | `0x1400067b0` | 875 | ✓ |
| `fcn.140001190` | `0x140001190` | 832 | ✓ |
| `fcn.140005150` | `0x140005150` | 817 | ✓ |
| `fcn.140003c7a` | `0x140003c7a` | 793 | ✓ |
| `fcn.14000b190` | `0x14000b190` | 700 | ✓ |
| `fcn.140004f30` | `0x140004f30` | 544 | ✓ |
| `fcn.14000a410` | `0x14000a410` | 449 | ✓ |
| `fcn.140002286` | `0x140002286` | 404 | ✓ |
| `fcn.14000241a` | `0x14000241a` | 404 | ✓ |
| `fcn.14000a100` | `0x14000a100` | 397 | ✓ |
| `fcn.14000a9c0` | `0x14000a9c0` | 381 | ✓ |
| `fcn.1400037b7` | `0x1400037b7` | 379 | ✓ |
| `fcn.140004781` | `0x140004781` | 373 | ✓ |
| `fcn.140006cc0` | `0x140006cc0` | 368 | ✓ |
| `fcn.140008290` | `0x140008290` | 366 | ✓ |
| `fcn.140009fb0` | `0x140009fb0` | 329 | ✓ |
| `fcn.14000a290` | `0x14000a290` | 302 | ✓ |
| `fcn.140005ef0` | `0x140005ef0` | 296 | ✓ |
| `fcn.1400030c7` | `0x1400030c7` | 292 | ✓ |
| `fcn.140003518` | `0x140003518` | 292 | ✓ |
| `fcn.140004663` | `0x140004663` | 286 | ✓ |
| `fcn.14000431c` | `0x14000431c` | 282 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001190.c`](code/fcn.140001190.c)
- [`code/fcn.140002286.c`](code/fcn.140002286.c)
- [`code/fcn.14000241a.c`](code/fcn.14000241a.c)
- [`code/fcn.1400030c7.c`](code/fcn.1400030c7.c)
- [`code/fcn.140003518.c`](code/fcn.140003518.c)
- [`code/fcn.1400037b7.c`](code/fcn.1400037b7.c)
- [`code/fcn.140003c7a.c`](code/fcn.140003c7a.c)
- [`code/fcn.140003ec5.c`](code/fcn.140003ec5.c)
- [`code/fcn.14000431c.c`](code/fcn.14000431c.c)
- [`code/fcn.140004663.c`](code/fcn.140004663.c)
- [`code/fcn.140004781.c`](code/fcn.140004781.c)
- [`code/fcn.140004ac0.c`](code/fcn.140004ac0.c)
- [`code/fcn.140004f30.c`](code/fcn.140004f30.c)
- [`code/fcn.140005150.c`](code/fcn.140005150.c)
- [`code/fcn.140005490.c`](code/fcn.140005490.c)
- [`code/fcn.140005ef0.c`](code/fcn.140005ef0.c)
- [`code/fcn.140006320.c`](code/fcn.140006320.c)
- [`code/fcn.1400067b0.c`](code/fcn.1400067b0.c)
- [`code/fcn.140006cc0.c`](code/fcn.140006cc0.c)
- [`code/fcn.140006e30.c`](code/fcn.140006e30.c)
- [`code/fcn.1400072d0.c`](code/fcn.1400072d0.c)
- [`code/fcn.140007850.c`](code/fcn.140007850.c)
- [`code/fcn.140008290.c`](code/fcn.140008290.c)
- [`code/fcn.140008400.c`](code/fcn.140008400.c)
- [`code/fcn.140009fb0.c`](code/fcn.140009fb0.c)
- [`code/fcn.14000a100.c`](code/fcn.14000a100.c)
- [`code/fcn.14000a290.c`](code/fcn.14000a290.c)
- [`code/fcn.14000a410.c`](code/fcn.14000a410.c)
- [`code/fcn.14000a9c0.c`](code/fcn.14000a9c0.c)
- [`code/fcn.14000b190.c`](code/fcn.14000b190.c)

## Behavioral Analysis

This update incorporates the analysis of the second disassembly chunk into the existing profile of the binary. The new code reinforces the conclusion that this is a sophisticated, multi-threaded "booter" tool with specific mechanisms for high-volume traffic and potential persistence/self-maintenance.

### Updated Analysis Overview
The additional code confirms several advanced characteristics:
1.  **Heavy Multi-threading Architecture:** The presence of multiple distinct functions for spawning thread pools indicates a modular design where different attack vectors (e.g., UDP vs. TCP) are handled by dedicated threads.
2.  **Resource Management & Persistence:** Evidence of interacting with "Startup" folders and performing file movements suggests the binary aims to stay active on the system or manage its local presence effectively.
3.  **Advanced Packet Crafting:** Complex mathematical operations on memory buffers suggest that rather than sending simple packets, the tool manipulates packet data at a granular level to bypass filters or maximize impact.

---

### New Findings from Chunk 2/2

#### 1. Multi-Threaded Execution Engines
Functions **`fcn.1400037b7`**, **`fcn.1400030c7`**, and **`fcn.140003518`** all follow a similar pattern:
*   They iterate through a count of intended threads.
*   Each iteration allocates memory (`malloc`) for thread parameters.
*   They call `CreateThread` to spawn workers.
*   They use `WaitForMultipleObjects` and `CloseHandle`.
*   **Significance:** This is a "worker-thread" model. By spawning hundreds of threads simultaneously, the malware can flood thousands of ports at once without being blocked by the local OS for "too many open files/sockets" in a single thread.

#### 2. Persistence and System Manipulation
Function **`fcn.140004781`** (and its relative **`fcn.140004663`**) shows highly suspicious behavior:
*   The code calls `SHGetSpecialFolderPathA(0)`, which typically retrieves the path to the **Windows Startup folder**.
*   It then uses `MoveFileA` and `DeleteFileA` to move or delete files in that directory.
*   **Significance:** This is a signature of "booter" tools trying to ensure they have persistent access or are checking if they are successfully "installed" in a way that allows them to run automatically upon reboot.

#### 3. Sophisticated Packet Manipulation/Buffer Logic
Functions **`fcn.140008290`**, **`fcn.14000a290`**, and **`fcn.140009fb0`** contain complex loops involving bitwise shifts (`>>`, `&`) and arithmetic on buffer lengths:
*   These functions are likely calculating packet offsets, adjusting header sizes, or distributing "payload" data across a range of packets.
*   **Significance:** This indicates the tool is capable of generating sophisticated network traffic (e.g., varying packet lengths or randomized headers) to bypass simple IP-based or signature-based firewalls.

#### 4. Network Connection Resilience
Function **`fcn.14000431c`** implements a robust connection routine:
*   It uses `ioctlsocket`, followed by `connect`.
*   Crucially, it utilizes **`select()`** to manage timeouts for connecting to remote targets.
*   **Significance:** This allows the tool to attempt to connect to thousands of targets rapidly; if a target doesn't respond within a few milliseconds (a "timeout"), the `select` logic allows the program to move on immediately rather than hanging, ensuring the "flood" continues uninterrupted.

---

### Updated Summary for Incident Response

**Classification:** **Malicious Network Stresser / Booter Tool.**

**New Technical Indicators:**
*   **Persistence Mechanism:** The binary actively interacts with system startup paths (`SHGetSpecialFolderPathA`) and performs file operations to manage its location on the disk. 
*   **High-Concurrency Model:** Multiple thread spawning loops confirm a highly concurrent architecture designed for massive volume throughput.
*   **Advanced Networking Logic:** The use of `select()` for timeouts and complex bitwise arithmetic for packet buffer manipulation suggests a sophisticated effort to bypass network security measures.

**Risk Assessment:** 
This binary is not typical "malware" in the sense of data theft or encryption; it is a specialized **cyber-weapon**. It is designed specifically to disrupt web services, game servers, and network infrastructure. Its presence on a network indicates an active attempt to launch a Denial of Service (DoS) attack from that machine.

**Recommended Actions:**
1.  **Isolate the Host:** The machine running this binary should be isolated immediately from the local network to prevent it from being used as a "bot" or "zombie" in a larger DDoS cluster.
2.  **Block Outbound Traffic:** Block all non-essential outbound traffic (especially on ports typically targeted by such tools, like 80, 443, and various gaming ports).
3.  **Search for Associated Files:** Look for other files moved to or residing in the Startup directory as a result of the `MoveFileA` logic observed in `fcn.140004781`.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1546 | Scheduled_Task | The interaction with the "Startup" folder via `SHGetSpecialFolderPathA` is a standard method to achieve persistence by ensuring the binary executes automatically upon system reboot. |
| T1562 | Impersonation | *Correction: Not applicable.* |
| (Defense Evasion) | Multi-threaded Execution | The use of a "worker-thread" model to bypass local OS limitations on open files/sockets is a technique used to evade system constraints during high-volume network flooding. |
| (Defense Evasion) | Packet Manipulation | The use of complex bitwise arithmetic and buffer manipulation is designed to circumvent firewalls or security filters by crafting non-standard packet headers. |

***Note for the Analyst:*** *Because "Multi-threading" and "Packet Crafting" are often architectural choices used specifically for evasion in "booter" tools, they fall under the **Defense Evasion** tactic. While there isn't a single specific sub-technique ID that exclusively covers "multi-threaded polling," it is functionally mapped to Defense Evasion as it is used to bypass local resource monitoring.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: This specific sample does not contain hardcoded IP addresses, URLs, or file hashes in the provided text; however, it contains significant behavioral indicators and functional identifiers.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **Windows Startup Folder:** The binary interacts with `SHGetSpecialFolderPathA(0)` to identify and manipulate files within the system's startup directory for persistence.

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (behavioral patterns & identifiers)**
*   **Attack Modules/Strings:** The following strings indicate specific attack modules used by the tool:
    *   `TCP-RAND`
    *   `NTCP`
    *   `UDP Attack`
    *   `SAMP Attack`
    *   `PPS Attack`
    *   `Discord Attack`
    *   `NUDP Attack`
*   **Network Logic:** 
    *   Use of `select()` for managing connection timeouts during high-volume flooding.
    *   Advanced packet crafting using bitwise shifts (`>>`, `&`) and arithmetic to manipulate buffer lengths/headers.
*   **Persistence Actions:** Use of `MoveFileA` and `DeleteFileA` specifically targeting the startup folder logic.
*   **Multi-threading Logic:** Implementation of a "worker-thread" model using `CreateThread` and `WaitForMultipleObjects` to bypass local OS limits on open sockets/files during an attack.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `draft22.duckdns.org`

---

## Malware Family Classification

1. **Malware family**: Booter / Stresser
2. **Malware type**: Botnet (specifically a DDoS/DoS tool)
3. **Confidence**: High
4. **Key evidence**:
    *   **Specific Attack Modules:** The presence of strings such as `UDP Attack`, `SAMP Attack`, `Discord Attack`, and `TCP-RAND` explicitly identifies the binary as a tool designed for launching Denial of Service (DoS) attacks against specific platforms and protocols.
    *   **High-Concurrency Architecture:** The use of a "worker-thread" model, including `CreateThread` and `WaitForMultipleObjects`, combined with `select()` for connection timeouts, is a hallmark of stresser tools designed to flood thousands of targets simultaneously while bypassing OS limitations.
    *   **Persistence & Evasion:** The integration of `SHGetSpecialFolderPathA` to target the Windows Startup folder and the use of bitwise arithmetic to manipulate packet headers indicate an intent to remain persistent on a host as part of a "zombie" network or to bypass security filters during an attack.
