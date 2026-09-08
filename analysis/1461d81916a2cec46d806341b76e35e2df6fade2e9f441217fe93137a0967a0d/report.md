# Threat Analysis Report

**Generated:** 2026-09-05 13:45 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 3 sections |
| Size | 38,400 bytes |
| MD5 | `84caa1b6115d0f6a2e96942bc41306e5` |
| SHA1 | `bf827b59131aa2e7fe6a320f7f3ba2f1d430c93e` |
| SHA256 | `1461d81916a2cec46d806341b76e35e2df6fade2e9f441217fe93137a0967a0d` |
| Overall entropy | 6.275 |
| Unpacked | ✓ Yes (tool: upx) |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1775374884 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 44,032 | 6.235 | No |
| `.data` | 512 | 1.024 | No |
| `.rdata` | 17,920 | 6.674 | No |
| `.pdata` | 2,048 | 4.397 | No |
| `.xdata` | 2,560 | 4.157 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 4,096 | 3.651 | No |
| `.CRT` | 512 | 0.341 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 1,024 | 3.006 | No |
| `.reloc` | 512 | 3.298 | No |

### Imports

**KERNEL32.DLL**: `CloseHandle`, `CopyFileA`, `CreateThread`, `DeleteCriticalSection`, `DeleteFileA`, `EnterCriticalSection`, `ExitProcess`, `FreeLibrary`, `GetCurrentProcessId`, `GetLastError`, `GetModuleFileNameA`, `GetModuleHandleW`, `GetProcAddress`, `GetStartupInfoA`, `GetTickCount`
**ADVAPI32.dll**: `CryptAcquireContextA`, `CryptGenRandom`, `CryptReleaseContext`
**msvcrt.dll**: `__C_specific_handler`, `___lc_codepage_func`, `___mb_cur_max_func`, `__getmainargs`, `__initenv`, `__iob_func`, `__lconv_init`, `__set_app_type`, `__setusermatherr`, `_acmdln`, `_amsg_exit`, `_cexit`, `_commode`, `_errno`, `_exit`
**SHELL32.dll**: `SHGetSpecialFolderPathA`
**WS2_32.dll**: `WSACleanup`, `WSAGetLastError`, `WSASocketA`, `WSAStartup`, `bind`, `closesocket`, `connect`, `gethostbyname`, `htons`, `inet_addr`, `inet_ntoa`, `ioctlsocket`, `ntohl`, `ntohs`, `recv`

## Extracted Strings

Total strings found: **460** (showing first 100)

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
AVAUATUWVSH
[^_]A\A]A^
UAWAVAUATWVSH
IcT$H+E
[^_A\A]A^A_]
UAWAVAUATWVSH
McFH+E
[^_A\A]A^A_]
UAWAVAUATWVSH
Mc^H+E
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
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
IcT$H)
X[^_]A\A]A^A_
AWAVAUATUWVSH
IcT$H)
X[^_]A\A]A^A_
AVAUATUWVSH
IcT$H)
P[^_]A\A]A^
AVAUATUWVSH
IcT$H)
D$hH+E
p[^_]A\A]A^
AVAUATUWVSH
IcT$H)
[^_]A\A]A^
AWAVAUATUWVSH
IcT$H)
[^_]A\A]A^A_
AWAVAUATUWVSH
IcT$H)
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
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
t$HH+1t
X[^_]A\A]A^A_
AWAVAUATUWVSH
\$hD9\$T
Lc\$DC
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140004ea0` | `0x140004ea0` | 27298 | ✓ |
| `fcn.140005870` | `0x140005870` | 21782 | ✓ |
| `fcn.1400087e0` | `0x1400087e0` | 5850 | ✓ |
| `fcn.140007c30` | `0x140007c30` | 2376 | ✓ |
| `fcn.1400076b0` | `0x1400076b0` | 1394 | ✓ |
| `fcn.1400041f7` | `0x1400041f7` | 1300 | ✓ |
| `fcn.140007210` | `0x140007210` | 1172 | ✓ |
| `fcn.14000b570` | `0x14000b570` | 975 | ✓ |
| `fcn.140006700` | `0x140006700` | 945 | ✓ |
| `fcn.140006b90` | `0x140006b90` | 875 | ✓ |
| `fcn.140001190` | `0x140001190` | 832 | ✓ |
| `fcn.140005530` | `0x140005530` | 817 | ✓ |
| `fcn.14000408a` | `0x14000408a` | 793 | ✓ |
| `fcn.140005310` | `0x140005310` | 544 | ✓ |
| `fcn.14000a7f0` | `0x14000a7f0` | 449 | ✓ |
| `fcn.14000a4e0` | `0x14000a4e0` | 397 | ✓ |
| `fcn.1400022a2` | `0x1400022a2` | 395 | ✓ |
| `fcn.14000242d` | `0x14000242d` | 395 | ✓ |
| `fcn.14000adb0` | `0x14000adb0` | 381 | ✓ |
| `fcn.140004b71` | `0x140004b71` | 373 | ✓ |
| `fcn.1400070a0` | `0x1400070a0` | 368 | ✓ |
| `fcn.140008670` | `0x140008670` | 366 | ✓ |
| `fcn.140003972` | `0x140003972` | 347 | ✓ |
| `fcn.14000a390` | `0x14000a390` | 329 | ✓ |
| `fcn.14000a670` | `0x14000a670` | 302 | ✓ |
| `fcn.1400062d0` | `0x1400062d0` | 296 | ✓ |
| `fcn.140004a53` | `0x140004a53` | 286 | ✓ |
| `fcn.14000470b` | `0x14000470b` | 282 | ✓ |
| `fcn.14000a9c0` | `0x14000a9c0` | 280 | ✓ |
| `fcn.140004ce6` | `0x140004ce6` | 274 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001190.c`](code/fcn.140001190.c)
- [`code/fcn.1400022a2.c`](code/fcn.1400022a2.c)
- [`code/fcn.14000242d.c`](code/fcn.14000242d.c)
- [`code/fcn.140003972.c`](code/fcn.140003972.c)
- [`code/fcn.14000408a.c`](code/fcn.14000408a.c)
- [`code/fcn.1400041f7.c`](code/fcn.1400041f7.c)
- [`code/fcn.14000470b.c`](code/fcn.14000470b.c)
- [`code/fcn.140004a53.c`](code/fcn.140004a53.c)
- [`code/fcn.140004b71.c`](code/fcn.140004b71.c)
- [`code/fcn.140004ce6.c`](code/fcn.140004ce6.c)
- [`code/fcn.140004ea0.c`](code/fcn.140004ea0.c)
- [`code/fcn.140005310.c`](code/fcn.140005310.c)
- [`code/fcn.140005530.c`](code/fcn.140005530.c)
- [`code/fcn.140005870.c`](code/fcn.140005870.c)
- [`code/fcn.1400062d0.c`](code/fcn.1400062d0.c)
- [`code/fcn.140006700.c`](code/fcn.140006700.c)
- [`code/fcn.140006b90.c`](code/fcn.140006b90.c)
- [`code/fcn.1400070a0.c`](code/fcn.1400070a0.c)
- [`code/fcn.140007210.c`](code/fcn.140007210.c)
- [`code/fcn.1400076b0.c`](code/fcn.1400076b0.c)
- [`code/fcn.140007c30.c`](code/fcn.140007c30.c)
- [`code/fcn.140008670.c`](code/fcn.140008670.c)
- [`code/fcn.1400087e0.c`](code/fcn.1400087e0.c)
- [`code/fcn.14000a390.c`](code/fcn.14000a390.c)
- [`code/fcn.14000a4e0.c`](code/fcn.14000a4e0.c)
- [`code/fcn.14000a670.c`](code/fcn.14000a670.c)
- [`code/fcn.14000a7f0.c`](code/fcn.14000a7f0.c)
- [`code/fcn.14000a9c0.c`](code/fcn.14000a9c0.c)
- [`code/fcn.14000adb0.c`](code/fcn.14000adb0.c)
- [`code/fcn.14000b570.c`](code/fcn.14000b570.c)

## Behavioral Analysis

This updated analysis incorporates the findings from the second disassembly chunk into your existing profile of the binary.

### Updated Analysis: Network-Based DDoS Bot & Persistence Mechanism

The additional disassembly confirms that this is not just a simple network tool, but a sophisticated **malicious bot** designed for longevity and scale. The new data highlights specific techniques used to ensure the malware remains active on an infected machine (persistence) and how it manages high-volume network operations.

---

### Core Functionality and Purpose
The primary purpose remains as a **multi-threaded DDoS "bot."** However, chunk 2 adds significant detail regarding its operation:
*   **Persistence Logic:** The tool actively attempts to move or copy itself into the system's **Startup folder**. This ensures that if the infected machine reboots, the bot automatically restarts and reconnects to the Command & Control (C2) server.
*   **Advanced Connection Handling:** It uses sophisticated techniques to manage network connections, including timeout logic for the `connect()` function, ensuring it can handle a high volume of attempts without hanging.

### Suspicious and Malicious Behaviors
*   **Persistence via Startup Folder (High Severity):**
    *   Functions **`fcn.140004b71`** and **`fcn.140004ce6`** are dedicated to identifying the system's "Startup" folder using `SHGetSpecialFolderPathA`. 
    *   The code checks if a copy of itself already exists in that location. If not, it attempts to move/copy its own binary there. This is a classic malware behavior intended to maintain presence on the victim's machine indefinitely.
*   **Sophisticated Multi-threaded Orchestration:**
    *   Functions **`fcn.1400022a2`** and **`fcn.14000242d`** are used to spawn multiple threads for network activity. 
    *   The code allocates memory blocks, prepares IP addresses (using `inet_addr`), and spawns a "worker" thread for each target or connection. This ensures that one unresponsive target doesn't stall the entire attack.
*   **Robust Network Timeout Logic:**
    *   Function **`fcn.14000470b`** implements an `ioctlsocket` call followed by a `select()` loop to handle a connection timeout. This is common in professional-grade stresser/booter tools; it prevents the bot from "hanging" when trying to connect to targets that are protected by firewalls or have no open ports.
*   **Data Processing & Buffer Management:**
    *   The presence of numerous helper functions (e.g., **`fcn.14000adb0`**, **`fcn.14000a670`**) suggests the bot can parse complex data packets sent by the C2 server, likely to interpret different attack commands or target lists.

### Notable Techniques & Patterns
*   **"Self-Preservation" Checks:** Before performing actions like `MoveFileA`, the code performs checks to see if a file already exists in the destination folder. This prevents the bot from crashing due to "file already exists" errors, ensuring it stays operational as much as possible.
*   **Resource Allocation for Scaling:** The allocation of memory blocks (e.g., `0x48` size buffers) and subsequent thread creation shows a clear design intended to maximize "packet-per-second" (PPS) counts during an attack.
*   **Standard Library Exploitation:** The use of standard string handling routines suggests the author utilized common coding libraries to handle the backend logic, allowing them to focus on the networking and persistence components.

---

### Updated Summary of Indicators (IOCs)
*   **Hardcoded C2 IP:** `45.83.207.194`
*   **Persistence Mechanisms:** 
    *   Calls to `SHGetSpecialFolderPathA` (Startup Folder).
    *   Automated `MoveFileA` or `CopyFileA` operations to ensure persistence.
*   **Key API Imports Identified in Chunk 2:**
    *   `CreateThread` / `SetThreadPriority` (Multi-threading)
    *   `GetModuleFileNameA` (To find its own path for copying)
    *   `ioctlsocket` & `select` (Robust network connection management)
    *   `inet_addr`, `htons` (Network configuration)
*   **Behavioral Patterns:** 
    *   Multi-threaded flooding.
    *   Startup folder infection for persistence.
    *   C2 heartbeat/keepalive logic.
    *   Advanced TCP connection management to bypass simple firewalls during the "handshake" phase.

### Conclusion
The addition of chunk 2 confirms this is a **high-quality DDoS bot**. It possesses two critical traits for malware: **persistence** (it wants to stay on your machine) and **robustness** (it uses advanced socket logic to ensure it can hit targets effectively). The presence of the startup folder copy routine strongly indicates that this binary was designed to be part of a "botnet," where hundreds or thousands of infected machines are managed by a central operator.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Startup Folder | The malware utilizes `SHGetSpecialFolderPathA` to identify and move itself into the system's startup folder to ensure persistence across reboots. |
| **T1071** | Application Layer Protocol | The bot parses complex data packets from a hardcoded C2 IP address (`45.83.207.194`) to interpret attack commands and target lists. |
| **T1498** | Network Denial of Service | The use of multi-threaded "worker" threads and `ioctlsocket`/`select` loops specifically enables the bot to perform high-volume, resilient network flooding. |
| **T1036** | Masquerading | The inclusion of "self-preservation" checks (verifying if a file exists before moving) ensures the malware remains operational and avoids errors during its persistence phase. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the identified Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `45.83.207.194` (Identified as a hardcoded C2 IP)

**File paths / Registry keys**
*   **Windows Startup Folder:** The malware identifies and targets this system path (via `SHGetSpecialFolderPathA`) to move/copy itself for persistence.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **C2 Communication Patterns:** 
    *   Multi-threaded TCP flooding (Terms: `TCP attack`, `TCP-RAND`, `NTCP`).
    *   Advanced handshake management using `ioctlsocket` and `select()` to bypass firewalls.
*   **Persistence Mechanism:** Self-preservation check; the binary checks if its own executable exists in the destination folder before moving/copying it via `MoveFileA` or `CopyFileA`.
*   **Hardcoded Strings (Behavioral Indicators):** 
    *   `Starting optimized TCP attack...`
    *   `Starting optimized TCP-RAND attack...`
    *   `Starting optimized NTCP attack...`
    *   `handshake`, `session`, `client`, `player` (Keywords related to botnet functionality).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**IP addresses:**
- `45.83.207.194`

---

## Malware Family Classification

1. **Malware family**: custom (DDoS Bot)
2. **Malware type**: bot
3. **Confidence**: High

4. **Key evidence**:
*   **Persistence via Startup Folder:** The malware utilizes `SHGetSpecialFolderPathA` and `MoveFileA`/`CopyFileA` to move itself into the system's startup folder, a classic behavior for ensuring long-term presence on a compromised machine to maintain its role in a botnet.
*   **Sophisticated Network Flooding Infrastructure:** The code implements high-performance networking techniques including multi-threaded "worker" threads (`CreateThread`), `ioctlsocket` with `select()` loops for robust connection handling, and specific attack types (TCP-RAND, NTCP), which are characteristic of professional-grade DDoS tools.
*   **C2 Command & Control Logic:** The presence of a hardcoded C2 IP (`45.83.207.194`) combined with keywords like "handshake," "session," and various TCP attack strings indicates the binary is designed to receive commands from a remote server to coordinate distributed attacks.
