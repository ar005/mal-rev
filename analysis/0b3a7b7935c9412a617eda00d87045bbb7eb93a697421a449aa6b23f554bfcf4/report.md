# Threat Analysis Report

**Generated:** 2026-07-25 23:10 UTC
**Sample:** `0b3a7b7935c9412a617eda00d87045bbb7eb93a697421a449aa6b23f554bfcf4_0b3a7b7935c9412a617eda00d87045bbb7eb93a697421a449aa6b23f554bfcf4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b3a7b7935c9412a617eda00d87045bbb7eb93a697421a449aa6b23f554bfcf4_0b3a7b7935c9412a617eda00d87045bbb7eb93a697421a449aa6b23f554bfcf4.exe` |
| File type | PE32+ executable for MS Windows 5.02 (console), x86-64 (stripped to external PDB), 11 sections |
| Size | 74,752 bytes |
| MD5 | `409dc58146687eb6f47982ebeaba807c` |
| SHA1 | `cdb51725e43246bc8e34a9315252236e06e9643a` |
| SHA256 | `0b3a7b7935c9412a617eda00d87045bbb7eb93a697421a449aa6b23f554bfcf4` |
| Overall entropy | 6.275 |
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
| `fcn.140001190` | `0x140001190` | 861 | ✓ |
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

This update incorporates the analysis of the second disassembly chunk. The new data confirms several advanced behaviors, specifically regarding **persistence** and **robust multi-threaded execution**, reinforcing the classification of this binary as a sophisticated malicious tool.

### Updated Analysis Summary
The addition of the second chunk provides evidence that this is not just a simple script-like attack tool but a structured piece of malware/malware-adjacent software. It includes mechanisms to ensure it remains active on a system (persistence) and utilizes advanced networking logic to manage concurrent connections efficiently during an attack.

### New & Refined Findings

#### 1. Persistence Mechanism (High Risk)
The functions `fcn.140004b71` and `fcn.140004ce6` contain explicit code intended to ensure the program remains active on the host machine:
*   **Startup Folder Integration:** The tool calls `SHGetSpecialFolderPathA(0)` to identify the Windows **Startup folder**. 
*   **Self-Copying/Moving:** It checks if a copy of itself already exists in that directory. If not, it uses `CopyFileA` or `MoveFileA` to place itself there. 
*   **Purpose:** This is a classic persistence technique. It ensures that the tool (or any associated malicious payloads) starts automatically every time the user logs into Windows.

#### 2. Advanced Multi-threaded Attack Engine
The functions `fcn.1400022a2`, `fcn.14000242d`, and `fcn.140003972` are almost identical in structure but point to different internal subroutines (e.g., `0x140001820` vs `0x140001b5a`).
*   **Parallel Execution:** These functions iterate through a count of threads provided by the user, creating one thread for each "worker."
*   **Priority Boosting:** It calls `SetThreadPriority`, ensuring that the network-flooding threads receive high priority from the CPU to maximize the number of packets sent per second (PPS).
*   **Segmentation:** The fact that there are multiple variations of these loops suggests different code paths for each attack mode (TCP, TCP-RAND, and NTCP).

#### 3. Robust Network Management
The function `fcn.14000470b` reveals a more sophisticated network stack than typical basic stresser tools:
*   **Timeout Handling:** It utilizes `ioctlsocket` and `select`. This indicates the tool doesn't just attempt a connection blindly; it manages timeouts properly to ensure that the "attack" threads don't hang if a target doesn't respond. 
*   **Reliability:** By using `select`, the developer ensures the tool can handle hundreds of simultaneous connections efficiently, which is critical for a successful DoS attack.

---

### Updated Risk Assessment Table

| Feature | Observation | Analysis/Risk |
| :--- | :--- | :--- |
| **DDoS/TDoS Engine** | Multiple multi-threaded loops (`fcn.1400022a2`, `fcn.140003972`) | **High**: Designed for high-volume, concurrent packet flooding. |
| **Persistence** | Copying self to Startup folder via `SHGetSpecialFolderPathA` | **High**: Classic malware behavior to maintain a presence on the host. |
| **C2 Infrastructure** | Hardcoded IP `45.83.207.194` with Heartbeat | **High**: Confirmed communication with an external controller. |
| **Sophisticated Networking** | Use of `ioctlsocket` and `select` for timeout management | **Medium/High**: Indicates a "professional" grade tool designed for reliability in remote attacks. |

### Final Conclusion (Updated)
The binary is a **sophisticated, multi-functional network attack tool.** It is specifically engineered to perform high-volume DDoS attacks using various protocols. The inclusion of **persistence mechanisms** (moving itself into the Startup folder) and **advanced networking logic** (proper timeout handling via `select`) suggests it is part of a professional "booter" or "stresser" service. 

The presence of hardcoded C2 infrastructure confirms that this tool is designed to work within an organized network, where it can report status back to an operator while simultaneously overwhelming target IP addresses.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Scheduled_Task or StartupFolder | The tool uses `SHGetSpecialFolderPathA` to identify and move itself into the Windows Startup folder to ensure persistence across system reboots. |
| T1071 | Application Layer Protocol | The presence of a hardcoded IP address for "heartbeat" signals indicates the use of standard network protocols for command and control (C2) communication. |
| T1498 | Network Denial of Service | The combination of multi-threaded execution, priority boosting, and advanced timeout management is specifically designed to perform high-volume packet flooding. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `45.83.207.194` (Identified as C2 infrastructure used for heartbeats)

**File paths / Registry keys**
*   *None identified.* (While the analysis mentions "Startup folder" and functions like `SHGetSpecialFolderPathA`, no specific hardcoded file paths or registry keys were present in the raw strings.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **C2 Pattern:** Heartbeat signals sent to `45.83.207.194`.
*   **Persistence Mechanism:** Use of `SHGetSpecialFolderPathA(0)` combined with `CopyFileA` or `MoveFileA` to move the executable into the Windows Startup folder.
*   **Attack Vectors/Modes:** 
    *   TCP Attack
    *   TCP-RAND (Randomized TCP)
    *   NTCP (Network Control Protocol)
*   **Notable Functions:**
    *   `fcn.140004b71` & `fcn.140004ce6` (Persistence logic)
    *   `fcn.1400022a2`, `fcn.14000242d`, `fcn.140003972` (Multi-threaded attack loops)
    *   `fcn.14000470b` (Network management using `ioctlsocket` and `select`)

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**IP addresses:**
- `45.83.207.194`

---

## Malware Family Classification

1. **Malware family**: custom (identified as a "booter" or "stresser" tool)
2. **Malware type**: botnet
3. **Confidence**: High
4. **Key evidence**:
    *   **Persistence Mechanisms:** The binary explicitly uses `SHGetSpecialFolderPathA` to locate and move itself into the Windows Startup folder, a hallmark of malware designed to remain active on a host across reboots.
    *   **DDoS Attack Infrastructure:** The analysis identifies specialized multi-threaded loops for TCP, TCP-RAND, and NTCP attacks, combined with `SetThreadPriority` to maximize packet flooding efficiency.
    *   **C2 Communication:** The inclusion of hardcoded IP addresses (`45.83.207.194`) for "heartbeat" signals confirms the tool is part of a managed network (likely a professional stresser service) where it reports status back to an operator.
