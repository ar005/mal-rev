# Threat Analysis Report

**Generated:** 2026-06-27 19:16 UTC
**Sample:** `01e4174159baf68c3ad3c126e7acc0fe9708dc99387094278ab3b04c6b7d6a09_01e4174159baf68c3ad3c126e7acc0fe9708dc99387094278ab3b04c6b7d6a09.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01e4174159baf68c3ad3c126e7acc0fe9708dc99387094278ab3b04c6b7d6a09_01e4174159baf68c3ad3c126e7acc0fe9708dc99387094278ab3b04c6b7d6a09.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 111,616 bytes |
| MD5 | `98066a046273ded1b0cb92b2175f5573` |
| SHA1 | `b73d3ecf0aeb3b5d5681e9c1fa2d20f0b7264ecb` |
| SHA256 | `01e4174159baf68c3ad3c126e7acc0fe9708dc99387094278ab3b04c6b7d6a09` |
| Overall entropy | 5.911 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769723159 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 58,880 | 6.401 | No |
| `.rdata` | 41,472 | 4.745 | No |
| `.data` | 3,072 | 2.094 | No |
| `.pdata` | 4,608 | 4.546 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.844 | No |

### Imports

**WININET.dll**: `InternetOpenA`, `InternetReadFile`, `InternetOpenUrlA`, `InternetCloseHandle`
**SHELL32.dll**: `SHGetFolderPathA`
**USER32.dll**: `GetMessageA`, `wsprintfA`, `DispatchMessageA`, `TranslateMessage`
**ADVAPI32.dll**: `GetUserNameA`
**KERNEL32.dll**: `CreateFileW`, `SetFilePointerEx`, `WriteConsoleW`, `GetConsoleMode`, `GetConsoleOutputCP`, `WriteFile`, `FlushFileBuffers`, `SetStdHandle`, `EnterCriticalSection`, `CreateDirectoryA`, `CreateFileA`, `GetDiskFreeSpaceExA`, `GetFileAttributesA`, `GetFileSize`, `ReadFile`

### Exports

`DWriteCreateFactory`

## Extracted Strings

Total strings found: **478** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
.reloc
D$`rwer3
D$dcz !
D$peRPx
D$tGRY|
D$xRNrOf
D$PeRPt
D$T[XDR
D$X|RN
D$@xYZX3
D$DhMY\f
D$Xbin
UVWAVAWH
A_A^_^]
D$`rwer3
D$dcz !
D$peRPx
D$tGRY|
D$xRNrOf
D$PeRPt
D$T[XDR
D$X|RN
D$@xYZX3
D$DhMY\f
\$ ATAVAWH
A9OTv 
I+_0t~A
0A_A^A\
0A_A^A\
@USVWATAUAVAWH
@8}Lt,
A_A^A]A\_^[]
|$ AVH
uxHcH
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180006af8` | `0x180006af8` | 14703 | ✓ |
| `fcn.180006ac0` | `0x180006ac0` | 14698 | ✓ |
| `fcn.180002d6c` | `0x180002d6c` | 12759 | ✓ |
| `fcn.180002c6c` | `0x180002c6c` | 3150 | ✓ |
| `fcn.180002dfc` | `0x180002dfc` | 2872 | ✓ |
| `fcn.180008aa8` | `0x180008aa8` | 1829 | ✓ |
| `fcn.18000e400` | `0x18000e400` | 1677 | ✓ |
| `fcn.1800020f0` | `0x1800020f0` | 1514 | ✓ |
| `fcn.1800047a8` | `0x1800047a8` | 1213 | ✓ |
| `fcn.18000cbd8` | `0x18000cbd8` | 1171 | ✓ |
| `fcn.180001a20` | `0x180001a20` | 1054 | ✓ |
| `fcn.18000c1b0` | `0x18000c1b0` | 922 | ✓ |
| `fcn.18000eab0` | `0x18000eab0` | 920 | ✓ |
| `fcn.18000bc40` | `0x18000bc40` | 920 | ✓ |
| `fcn.180002830` | `0x180002830` | 892 | ✓ |
| `fcn.180008748` | `0x180008748` | 862 | ✓ |
| `fcn.180006ebc` | `0x180006ebc` | 817 | ✓ |
| `fcn.18000d524` | `0x18000d524` | 815 | ✓ |
| `fcn.180009574` | `0x180009574` | 712 | ✓ |
| `fcn.180001760` | `0x180001760` | 689 | ✓ |
| `fcn.180001e40` | `0x180001e40` | 681 | ✓ |
| `fcn.180003058` | `0x180003058` | 667 | ✓ |
| `fcn.180001260` | `0x180001260` | 660 | ✓ |
| `fcn.1800091d0` | `0x1800091d0` | 623 | ✓ |
| `fcn.180001500` | `0x180001500` | 607 | ✓ |
| `fcn.18000a604` | `0x18000a604` | 604 | ✓ |
| `section..text` | `0x180001000` | 597 | ✓ |
| `fcn.1800067c8` | `0x1800067c8` | 589 | ✓ |
| `fcn.180004c68` | `0x180004c68` | 584 | ✓ |
| `fcn.180005208` | `0x180005208` | 557 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001260.c`](code/fcn.180001260.c)
- [`code/fcn.180001500.c`](code/fcn.180001500.c)
- [`code/fcn.180001760.c`](code/fcn.180001760.c)
- [`code/fcn.180001a20.c`](code/fcn.180001a20.c)
- [`code/fcn.180001e40.c`](code/fcn.180001e40.c)
- [`code/fcn.1800020f0.c`](code/fcn.1800020f0.c)
- [`code/fcn.180002830.c`](code/fcn.180002830.c)
- [`code/fcn.180002c6c.c`](code/fcn.180002c6c.c)
- [`code/fcn.180002d6c.c`](code/fcn.180002d6c.c)
- [`code/fcn.180002dfc.c`](code/fcn.180002dfc.c)
- [`code/fcn.180003058.c`](code/fcn.180003058.c)
- [`code/fcn.1800047a8.c`](code/fcn.1800047a8.c)
- [`code/fcn.180004c68.c`](code/fcn.180004c68.c)
- [`code/fcn.180005208.c`](code/fcn.180005208.c)
- [`code/fcn.1800067c8.c`](code/fcn.1800067c8.c)
- [`code/fcn.180006ac0.c`](code/fcn.180006ac0.c)
- [`code/fcn.180006af8.c`](code/fcn.180006af8.c)
- [`code/fcn.180006ebc.c`](code/fcn.180006ebc.c)
- [`code/fcn.180008748.c`](code/fcn.180008748.c)
- [`code/fcn.180008aa8.c`](code/fcn.180008aa8.c)
- [`code/fcn.1800091d0.c`](code/fcn.1800091d0.c)
- [`code/fcn.180009574.c`](code/fcn.180009574.c)
- [`code/fcn.18000a604.c`](code/fcn.18000a604.c)
- [`code/fcn.18000bc40.c`](code/fcn.18000bc40.c)
- [`code/fcn.18000c1b0.c`](code/fcn.18000c1b0.c)
- [`code/fcn.18000cbd8.c`](code/fcn.18000cbd8.c)
- [`code/fcn.18000d524.c`](code/fcn.18000d524.c)
- [`code/fcn.18000e400.c`](code/fcn.18000e400.c)
- [`code/fcn.18000eab0.c`](code/fcn.18000eab0.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, the analysis of the binary is significantly deepened. The sample is not just a simple loader; it incorporates advanced **evasion techniques**, **downloader functionality**, and **in-memory execution** components common in sophisticated malware (such as Cobalt Strike beacons or custom modular RATs).

Here is the updated and extended analysis:

### Updated Core Functionality and Purpose
The binary is a **sophisticated multi-stage loader**. It is designed to perform a "Downloader" role—reaching out to a remote server, fetching an encrypted payload into memory, and executing it. Furthermore, it contains advanced **anti-EDR (Endpoint Detection and Response)** techniques, specifically attempting to bypass security software by manually resolving system calls to avoid being caught by API hooks.

---

### New & Advanced Malicious Behaviors

#### 1. Remote Payload Retrieval (Downloader)
The function `fcn.180001760` reveals a complete network-to-memory pipeline:
*   **Internet Interaction:** The code utilizes the `WinINet` library (`InternetOpenA`, `InternetOpenUrlA`) to connect to a remote server.
*   **Hidden URLs:** The destination URL is stored in an encrypted/obfuscated state and only decrypted at runtime (note the repeated XOR operations on local buffer arrays).
*   **In-Memory Decryption:** Once data is downloaded via `InternetReadFile`, it is placed into a memory buffer allocated by `VirtualAlloc`. Crucially, the code then performs a **custom XOR decryption loop** to deobfuscate the payload before use. This ensures that the "real" malicious logic never exists in plain text on the disk.

#### 2. Advanced Anti-EDR & System Call Resolution
The function `section..text` is highly indicative of advanced evasion:
*   **NTDLL Mapping:** The code manually opens a handle to `ntdll.dll`, maps it into memory, and iterates through its sections/exports.
*   **Manual Syscall Extraction:** It specifically searches for the `.text` section and attempts to resolve system call numbers (syscalls). By doing this, the malware intends to bypass EDR hooks—standard security tools monitor "high-level" APIs; by going directly to the `ntdll` syscall level, the malware can perform actions like process injection or memory allocation without triggering alerts.
*   **Dynamic Permission Modification:** It uses `VirtualProtect` to change memory permissions as it processes these system structures.

#### 3. Sophisticated In-Memory Execution (Reflective Loading)
The function `fcn.180001e40` acts as a "loader" stub:
*   **Hidden API Resolving:** It uses a loop to iterate through an internal structure of DLL names and function names, calling `GetProcAddress` on each. 
*   **Dynamic Thread Creation:** After resolving necessary functions (like memory management or thread creation), it creates a new thread to execute the payload in its own memory space. This is a classic **Reflective Loading** technique used to run code without ever "dropping" an `.exe` file onto the hard drive.

#### 4. Low-Level Hardware Fingerprinting
The function `fcn.180003058` demonstrates advanced anti-virtualization:
*   **CPUID Exploitation:** It uses the `cpuid` instruction to query hardware features. 
*   **VM Detection:** It checks specific bitmasks (e.g., `0x106c0`, `0x20660`) which are used to determine if the CPU is being virtualized or emulated by a hypervisor. This helps the malware decide whether it is running on a researcher’s "sandbox" machine or a real user's PC.

---

### Updated Summary of Techniques & Patterns

*   **Reflective Loading:** Use of `VirtualAlloc`, `GetProcAddress`, and manual thread creation to execute code directly from memory.
*   **Runtime De-obfuscation:** Heavy use of XORing on both string constants (to hide URLs/filenames) and, more importantly, on the payload itself after it is fetched from a remote server.
*   **Anti-EDR "Unhooking":** The logic in `section..text` suggests an attempt to bypass security software by manually resolving syscalls inside `ntdll.dll`.
*   **Multi-Stage Decryption:** Evidence of multiple layers of protection; the loader first decodes its internal instructions, then fetches a secondary payload which it decodes again before execution.
*   **Information Harvesting:** (From Chunk 1) The collection of system info (Username, Computer Name, etc.) is used as a "gatekeeper" to ensure the malware only activates on targeted systems.

### Conclusion for Threat Intelligence
This sample is a high-quality **malware loader**. It is designed for stealth and persistence. Its primary characteristics are:
1.  **Detection Evasion:** (VM detection, anti-debugging, and syscall-level evasion).
2.  **Payload Delivery:** (Remote download via WinINet with post-download decryption).
3.  **Stealth Execution:** (In-memory execution to leave a minimal forensic footprint).

This behavior is consistent with modern **Trojanized Loaders** or **Command & Control (C2) Beaconing** modules.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors of the analyzed binary to the MITRE ATT&CK framework based on your technical findings:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files/Information | The malware utilizes custom XOR loops to obfuscate internal strings (URLs) and the primary payload. |
| **T1105** | Ingress Tool Transfer | The binary acts as a downloader by using the WinINet library to retrieve an encrypted payload from a remote server. |
| **T1106** | Native API | The malware bypasses EDR hooks by manually resolving and executing system calls directly from `ntdll.dll`. |
| **T1055** | Process Injection | The "Reflective Loading" stub uses `VirtualAlloc` and `GetProcAddress` to execute the payload in memory without a disk footprint. |
| **T1497** | Virtualization/Sandbox Detection | The binary uses the `cpuid` instruction to check specific bitmasks intended to detect if it is running in a virtualized environment. |
| **T1082** | System Information Discovery | The "gatekeeper" logic collects system details (Username, Computer Name) to verify if the target machine meets specific criteria. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   `tbox.moe/5pzciq.xDM_\JYNwwfBHYDXM_ww|BEOD\Xwwh^YYNE_}NYXBDEwwy^https://files.caeRPfBRENaV[BRrOv` (Note: This appears to be a heavily obfuscated URL/C2 string).

**File paths / Registry keys**
*   *None identified.* (Note: `ntdll.dll` and `%s\Programs` were excluded as standard Windows system paths).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **User-Agent String:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36`
*   **Anti-Analysis/Sandbox Indicators:** 
    *   Strings: `cuckoosandbox`, `willbert`, `sandbox`, `malware`.
    *   Tools detected: `x64dbg`, `x32dbg`, `ollydbg`, `windbg`, `processhacker`, `fiddler`, `wireshark`, `procmon`, `apimonitor`, `pestudio`.
*   **Security Software/Service Checks:** 
    *   Detected DLLs: `sbiedll.dll`, `vmcheck.dll`, `cuckoomon.dll` (Used to identify and bypass security products).
*   **Behavioral Markers:**
    *   **Reflective Loading:** Use of `VirtualAlloc`, `GetProcAddress`, and manual thread creation for in-memory execution.
    *   **Syscall Unhooking:** Manual mapping of `ntdll` to bypass EDR hooks.
    *   **Hardware Fingerprinting:** Use of the `cpuid` instruction with specific bitmask checks (`0x106c0`, `0x20660`) for VM detection.
    *   **Network Protocol:** Usage of `WinINet` library (`InternetOpenA`, `InternetOpenUrlA`, `InternetReadFile`).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**: 
    *   **Advanced Evasion & Anti-EDR:** The sample employs sophisticated techniques to bypass security software, including manual `ntdll.dll` mapping and syscall resolution to circumvent API hooking.
    *   **Reflective Loading/In-Memory Execution:** It utilizes `VirtualAlloc`, `GetProcAddress`, and custom decryption loops to fetch, decrypt, and execute remote payloads directly in memory, ensuring no malicious files are saved to the disk.
    *   **Multi-Stage Delivery & Gatekeeping:** The binary acts as a downloader using the `WinINet` library and includes "gatekeeper" logic (system info gathering) to ensure it only activates on specific target systems.
