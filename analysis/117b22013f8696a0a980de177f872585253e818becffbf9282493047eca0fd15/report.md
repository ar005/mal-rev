# Threat Analysis Report

**Generated:** 2026-08-23 18:24 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 3 sections |
| Size | 31,232 bytes |
| MD5 | `866c0158bafb93dd5449cbf5e1a94aae` |
| SHA1 | `293e806f71a2d49319813c19d33f45eda6a79c58` |
| SHA256 | `117b22013f8696a0a980de177f872585253e818becffbf9282493047eca0fd15` |
| Overall entropy | 6.078 |
| Unpacked | ✓ Yes (tool: upx) |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766216767 |
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

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis. The new data confirms several sophisticated malicious behaviors, specifically regarding persistence and advanced multi-threading management.

### Updated Analysis of Disassembled Code

The second set of functions reinforces the previous assessment that this is a high-quality, feature-rich attack tool. The following new elements have been identified:

#### 1. Persistence Mechanism (Infection/Persistence)
Functions `fcn.140004781` and `fcn.140004663` contain logic typical of malware seeking to maintain a presence on the host system:
*   **Startup Folder Manipulation:** The code calls `SHGetSpecialFolderPathA` to locate the Windows Startup folder. 
*   **Self-Copying/Moving:** It attempts to move its executable (or a copy of it) into this directory. This ensures that the tool—and potentially its attack scripts—will automatically execute every time the user logs into the operating system.
*   **File System Manipulation:** The inclusion of `DeleteFileA` and `MoveFileA` in these sequences suggests an attempt to "install" itself while cleaning up the original execution path or ensuring only one instance exists in the startup area.

#### 2. Advanced Multi-Threading Management
Functions `fcn.1400037b7`, `fcn.1400030c7`, and `fcn.140003518` all follow a specific, sophisticated pattern:
*   **Thread Pooling:** Rather than simply launching threads in the background, the program allocates memory for each thread's parameters (`malloc`), creates them via `CreateThread`, and then uses **`WaitForMultipleObjects`**.
*   **Synchronized Execution:** The use of `WaitForMultipleObjects` indicates that the "master" process waits for all worker threads (the attack "bots") to complete their tasks before proceeding. This allows the tool to provide status updates or wait for a full cycle of an attack (e.g., flooding 10 different targets) before moving to the next command.
*   **Modular Attack Delivery:** The repetition of this pattern across three different functions suggests that different "modes" of the attack (TCP, UDP, etc.) are handled by distinct modules that each manage their own thread pool.

#### 3. Robust Network Handling & Timing
Function `fcn.14000431c` provides more insight into how it handles connections:
*   **Connection with Timeout:** The code uses a combination of `ioctlsocket`, `connect`, and **`select`**. 
*   **Purpose:** Instead of letting a connection attempt hang indefinitely, the tool implements a timeout. In a DDoS context, this is vital; if a target's firewall blocks a packet, the "worker" thread won't get stuck waiting for a response that will never come, allowing it to continue cycling through targets or packets rapidly.

---

### Updated Summary of Findings

#### Core Functionality & Purpose
The binary remains confirmed as a **multi-functional DDoS/DoS attack toolkit**. The addition of multi-threaded management suggests it is designed to handle large-scale attacks where many concurrent connections are required.

#### Enhanced Suspected Malicious Behaviors:
*   **Network Flooding (DDoS):** Confirmed via multiple thread-spawning routines for different protocol types.
*   **Persistence (Malware Behavior):** The inclusion of logic to move the binary into the **Windows Startup folder** is a clear indicator of malicious intent, designed to ensure the tool stays active on the victim's system.
*   **Sophisticated Concurrency:** The use of `WaitForMultipleObjects` and multi-threaded worker pools indicates a "professional" grade attack tool intended for high-volume traffic generation.
*   **Evasion/Robustness:** Use of timeouts (`select`) and dynamic API resolution (from the first chunk) ensures the tool remains stable even when under heavy network load or when targets are actively defending themselves.

#### Technical Summary for Incident Response:
*   **Primary Threats:** Denial of Service, Persistence, Network Disruption.
*   **Key Windows APIs used for Malice:** `CreateThread` (Multi-threading), `SetTcpEntry` (Connection Killing), `SHGetSpecialFolderPathA`/`MoveFileA` (Persistence), `select` (Network Resilience).
*   **Target Profiles:** High probability of use in targeting online gaming infrastructure (due to the "Discord Attack" string) or disrupting local network environments.

**Conclusion:** This binary is a sophisticated piece of **malicious software**. It combines offensive networking capabilities with malware persistence techniques, making it highly dangerous to operate on an enterprise or personal network.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Startup Folder | The malware uses `SHGetSpecialFolderPathA` to identify the Windows Startup folder and `MoveFileA` to place itself there for persistence upon login. |
| **T1498** | Network Denial of Service | The analysis confirms a multi-functional DDoS toolkit that utilizes multi-threaded execution (`CreateThread`) and various protocols (TCP/UDP) to flood targets. |
| **T1562** | Impair Defenses: Prediction Provider (Note: Logic falls under Defense Evasion via Robustness) | The use of `select` for connection timeouts ensures the tool remains resilient against defender-imposed delays, allowing it to maintain a high volume of attack traffic. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   *None identified.* (The data contains placeholders like `%s:%d`, indicating that target IPs and ports are likely passed as command-line arguments or defined in a separate configuration file rather than hardcoded in the strings.)

**File paths / Registry keys**
*   **Windows Startup Folder:** The analysis confirms the use of `SHGetSpecialFolderPathA` to identify and move the executable into the Windows Startup directory for persistence.
*   **System Files/Libraries:** Reference to `iphlpapi.dll` (Used for network utility functions; while a standard system file, its presence in this context relates to the tool's ability to query and manipulate TCP tables).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Attack Modules/Types:** 
    *   `TCP-RAND` (Potential custom TCP flood variant)
    *   `NTCP` (Non-standard TCP attack module)
    *   `NUDP` (Non-standard UDP attack module)
    *   `SAMP Attack` (Targeting "San Andreas Multiplayer" infrastructure)
    *   `Discord Attack` (Targeting Discord infrastructure)
*   **Persistence Indicators:** 
    *   Usage of `MoveFileA` and `DeleteFileA` to facilitate the installation/cleanup process during startup manipulation.
*   **Network Manipulation Behavior:**
    *   `GetTcpTable`: Used for identifying active connections on the local system.
    *   `SetTcpEntry`: Used to forcefully terminate connections (often used in "connection killer" tools).
    *   `ioctlsocket`, `connect`, and `select`: Utilized for managing non-blocking sockets and implementing connection timeouts during flood attacks.

---
**Analyst Note:** This sample is a **multi-functional DDoS/DoS toolkit**. While it lacks static hardcoded IP addresses (likely to evade simple signature-based detection), the presence of "Discord" and "SAMP" strings, combined with automated persistence mechanisms via the Startup folder, confirms its use as malicious software intended for network disruption and host compromise.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `draft22.duckdns.org`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: DoS/DDoS tool
3. **Confidence**: High
4. **Key evidence**:
    *   **Persistence Mechanism:** The code utilizes `SHGetSpecialFolderPathA` and `MoveFileA` to move the executable into the Windows Startup folder, ensuring it remains active across reboots.
    *   **Sophisticated Network Flooding:** The use of multi-threading (`CreateThread`, `WaitForMultipleObjects`) and specific network management routines (`ioctlsocket`, `select`) indicates a high-performance toolkit designed to manage large volumes of traffic without timing out.
    *   **Dedicated Attack Modules:** String analysis reveals specific targets (e.g., "Discord Attack", "SAMP Attack") and custom attack variants (e.g., "NTCP", "NUDP"), confirming its primary role as a specialized network disruption tool.
