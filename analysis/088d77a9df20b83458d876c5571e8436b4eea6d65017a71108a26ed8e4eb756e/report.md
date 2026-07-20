# Threat Analysis Report

**Generated:** 2026-07-18 14:11 UTC
**Sample:** `088d77a9df20b83458d876c5571e8436b4eea6d65017a71108a26ed8e4eb756e_088d77a9df20b83458d876c5571e8436b4eea6d65017a71108a26ed8e4eb756e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `088d77a9df20b83458d876c5571e8436b4eea6d65017a71108a26ed8e4eb756e_088d77a9df20b83458d876c5571e8436b4eea6d65017a71108a26ed8e4eb756e.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 4,796,416 bytes |
| MD5 | `9deea16f393abf006add15682991e092` |
| SHA1 | `83b65d89795976c24c61a92e6b62edf1b9dd1405` |
| SHA256 | `088d77a9df20b83458d876c5571e8436b4eea6d65017a71108a26ed8e4eb756e` |
| Overall entropy | 6.81 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766839358 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 2,231,296 | 6.312 | No |
| `.rdata` | 2,496,000 | 6.69 | No |
| `.data` | 4,096 | 1.84 | No |
| `.pdata` | 39,424 | 6.056 | No |
| `.fptable` | 0 | 0.0 | No |
| `.reloc` | 24,576 | 5.447 | No |

### Imports

**kernel32.dll**: `GetTimeZoneInformationForYear`
**api-ms-win-core-synch-l1-2-0.dll**: `WakeByAddressAll`, `WaitOnAddress`, `WakeByAddressSingle`
**bcryptprimitives.dll**: `ProcessPrng`
**ADVAPI32.dll**: `RegCloseKey`, `SystemFunction036`, `GetUserNameW`, `RegQueryValueExW`, `RegOpenKeyExW`
**KERNEL32.dll**: `CloseHandle`, `GetSystemInfo`, `GlobalMemoryStatusEx`, `GetModuleHandleW`, `CreateProcessW`, `GetComputerNameExW`, `LoadLibraryExW`, `GetProcAddress`, `FreeLibrary`, `RtlVirtualUnwind`, `GetCurrentThread`, `GetProcessHeap`, `HeapFree`, `HeapReAlloc`, `CreateFileW`
**bcrypt.dll**: `BCryptGenRandom`
**GDI32.dll**: `CreateCompatibleDC`, `CreateCompatibleBitmap`, `SelectObject`, `BitBlt`, `GetDIBits`, `DeleteObject`, `DeleteDC`
**USER32.dll**: `GetSystemMetrics`, `GetDC`, `ReleaseDC`
**ws2_32.dll**: `recv`, `ioctlsocket`, `getsockopt`, `WSAGetLastError`, `setsockopt`, `freeaddrinfo`, `getpeername`, `getsockname`, `send`, `accept`, `bind`, `listen`, `connect`, `WSAStartup`, `WSACleanup`
**ntdll.dll**: `NtCreateNamedPipeFile`, `NtOpenFile`, `NtReadFile`, `RtlNtStatusToDosError`, `NtWriteFile`

## Extracted Strings

Total strings found: **82722** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
.pdata
@.fptable
.reloc
AWAVAUATVWUS
H9t$0t
fffff.
$(fffff.
, B:,)t
, B:,)t
fffff.
,0B:,9t
,0B:,9t
H9t$0t
[]_^A\A]A^A_
AWAVAUATVWUS
H9D$Pt
fffff.
tH;T$x
fffff.
u"ffffff.
fffff.
t~H;U
tfH;U
tNH;U
t6H;U
[]_^A\A]A^A_
AWAVAUATVWUSH
%fffff.
\$/
\$.
\$-H
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
x[]_^A\A]A^A_
AWAVAUATVWUSH
D$0L;d$xI
[]_^A\A]A^A_
AWAVAUATVWUSH
tffffff.
L;t$hI
G0L;|$`I
D$pH;D$h
[]_^A\A]A^A_
AWAVVWSH
[_^A^A_
AWAVAUATVWUSH
!ffff.
"fffff.
Gfffff.
X[]_^A\A]A^A_
AVVWSH
X[_^A^
X[_^A^
AWAVAUATVWSH
0[_^A\A]A^A_
0[_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AVVWSH
ffffff.
|$Hfff.
AWAVAUATVWUSH
,"C:,(t
fffff.
,"C:,(t
ffffff.
,:C:, t
,:C:, t
[]_^A\A]A^A_
AWAVAUATVWUSH
ffffff.
l$8t!H
L9=/jG
[]_^A\A]A^A_
L9=QhG
AWAVAUATVWSH
7fffff.
[_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
4)D:4*t
,)D:,*t
,!B:,*t
,!B:,*t
[]_^A\A]A^A_
AWAVAUATVWUSH
H9D$0t
H9D$Hu
H
[]_^A\A]A^A_
AWAVAUATVWUSH
D$@H9D$@
H9D$(u
[]_^A\A]A^A_
H9D$(u
H
AWAVAUATVWUS
ffffff.
L9l$@t
>fffff.
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14000da90` | `0x14000da90` | 2148942 | ✓ |
| `fcn.14003ace0` | `0x14003ace0` | 1708855 | ✓ |
| `fcn.14003acd0` | `0x14003acd0` | 1708775 | ✓ |
| `fcn.14003acc0` | `0x14003acc0` | 1708620 | ✓ |
| `fcn.14003acb0` | `0x14003acb0` | 1708578 | ✓ |
| `fcn.1400669d0` | `0x1400669d0` | 1564781 | ✓ |
| `fcn.14020a6d8` | `0x14020a6d8` | 920458 | ✓ |
| `fcn.14020a6ec` | `0x14020a6ec` | 919614 | ✓ |
| `fcn.14020a700` | `0x14020a700` | 916370 | ✓ |
| `fcn.14020a0dc` | `0x14020a0dc` | 915502 | ✓ |
| `fcn.14003b5f0` | `0x14003b5f0` | 420658 | ✓ |
| `fcn.1401e4a40` | `0x1401e4a40` | 247256 | ✓ |
| `fcn.14000b630` | `0x14000b630` | 241552 | ✓ |
| `fcn.14008dcf0` | `0x14008dcf0` | 157779 | ✓ |
| `fcn.14009cd70` | `0x14009cd70` | 81468 | ✓ |
| `fcn.14009e0a0` | `0x14009e0a0` | 77333 | ✓ |
| `fcn.1401e2cb0` | `0x1401e2cb0` | 64196 | ✓ |
| `fcn.1400a2040` | `0x1400a2040` | 59458 | ✓ |
| `fcn.1400be900` | `0x1400be900` | 57389 | ✓ |
| `fcn.1401a80b0` | `0x1401a80b0` | 55430 | ✓ |
| `fcn.1401e7540` | `0x1401e7540` | 54599 | ✓ |
| `fcn.1400a3d10` | `0x1400a3d10` | 53299 | ✓ |
| `fcn.1401260e0` | `0x1401260e0` | 48621 | ✓ |
| `fcn.1400e0640` | `0x1400e0640` | 44380 | ✓ |
| `fcn.1400e0870` | `0x1400e0870` | 44093 | ✓ |
| `fcn.1400a62a0` | `0x1400a62a0` | 42824 | ✓ |
| `fcn.1400f03f0` | `0x1400f03f0` | 41154 | ✓ |
| `fcn.1401df610` | `0x1401df610` | 39553 | ✓ |
| `fcn.1401e4d70` | `0x1401e4d70` | 38276 | ✓ |
| `fcn.140066b30` | `0x140066b30` | 37376 | ✓ |

### Decompiled Code Files

- [`code/fcn.14000b630.c`](code/fcn.14000b630.c)
- [`code/fcn.14000da90.c`](code/fcn.14000da90.c)
- [`code/fcn.14003acb0.c`](code/fcn.14003acb0.c)
- [`code/fcn.14003acc0.c`](code/fcn.14003acc0.c)
- [`code/fcn.14003acd0.c`](code/fcn.14003acd0.c)
- [`code/fcn.14003ace0.c`](code/fcn.14003ace0.c)
- [`code/fcn.14003b5f0.c`](code/fcn.14003b5f0.c)
- [`code/fcn.1400669d0.c`](code/fcn.1400669d0.c)
- [`code/fcn.140066b30.c`](code/fcn.140066b30.c)
- [`code/fcn.14008dcf0.c`](code/fcn.14008dcf0.c)
- [`code/fcn.14009cd70.c`](code/fcn.14009cd70.c)
- [`code/fcn.14009e0a0.c`](code/fcn.14009e0a0.c)
- [`code/fcn.1400a2040.c`](code/fcn.1400a2040.c)
- [`code/fcn.1400a3d10.c`](code/fcn.1400a3d10.c)
- [`code/fcn.1400a62a0.c`](code/fcn.1400a62a0.c)
- [`code/fcn.1400be900.c`](code/fcn.1400be900.c)
- [`code/fcn.1400e0640.c`](code/fcn.1400e0640.c)
- [`code/fcn.1400e0870.c`](code/fcn.1400e0870.c)
- [`code/fcn.1400f03f0.c`](code/fcn.1400f03f0.c)
- [`code/fcn.1401260e0.c`](code/fcn.1401260e0.c)
- [`code/fcn.1401a80b0.c`](code/fcn.1401a80b0.c)
- [`code/fcn.1401df610.c`](code/fcn.1401df610.c)
- [`code/fcn.1401e2cb0.c`](code/fcn.1401e2cb0.c)
- [`code/fcn.1401e4a40.c`](code/fcn.1401e4a40.c)
- [`code/fcn.1401e4d70.c`](code/fcn.1401e4d70.c)
- [`code/fcn.1401e7540.c`](code/fcn.1401e7540.c)
- [`code/fcn.14020a0dc.c`](code/fcn.14020a0dc.c)
- [`code/fcn.14020a6d8.c`](code/fcn.14020a6d8.c)
- [`code/fcn.14020a6ec.c`](code/fcn.14020a6ec.c)
- [`code/fcn.14020a700.c`](code/fcn.14020a700.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis. The new code confirms several sophisticated evasion techniques and high-level complexity typically found in professional-grade malware loaders (such as those used by advanced persistent threat (APT) groups or high-end "crypter" services).

### Updated Analysis of Functionality and Behavior

#### 1. Advanced Cryptographic Processing (AVX Implementation)
The first large block of code reveals a massive amount of **SIMD (Single Instruction, Multiple Data)** logic using AVX instructions (`vpaddd_avx`, `vpsrld_avx`, `vpshufd_avx`). 
*   **Bulk Decryption:** This is not standard programming. The use of AVX means the loader is designed to decrypt a very large amount of data (the payload) extremely quickly.
*   **Complex Transformation:** The repetitive patterns of bit-shifting, XORing, and shuffling (`vpshufd`, `vpsrld`) suggest a custom encryption algorithm or a heavily modified standard one (like ChaCha20 or a TEA-variant). This confirms the "heavy cryptographic logic" noted in the first analysis but adds that it is optimized for high-performance bulk processing.

#### 2. Anti-Sandbox & Stall Tactics
The function `fcn.1401df610` reveals specific anti-analysis techniques:
*   **Waitable Timer Abuse:** The use of `CreateWaitableTimerExW`, `SetWaitableTimer`, and `WaitForSingleObject` is a classic **anti-sandbox** technique. By setting a timer, the malware can "sleep" for a long duration or until an external signal occurs. This is designed to time out automated sandbox environments that only monitor a program for a few minutes.
*   **Sleep Logic:** The inclusion of `Sleep` functions in conjunction with these timers provides multiple layers of stalling to bypass automated analysis systems.

#### 3. Anti-Debugging & Timing Analysis
The function `fcn.1401e4d70` utilizes:
*   **QueryPerformanceCounter / QueryPerformanceFrequency:** These are used to obtain high-precision timing. In the context of a loader, this is almost certainly used for **timing checks**. The malware compares the time taken between two operations; if the difference is too large (indicating human interaction or the overhead of a debugger), it will alter its behavior or terminate.

#### 4. Massive State Machine / Command Dispatcher
The functions `fcn.1400a62a0` and `fcn.1400f03f0` contain:
*   **Large Jump Tables:** The notes indicate switch tables with "9 cases" and, more significantly, **"512 cases."** 
*   **Control Flow Flattening:** This confirms the previous suspicion of VM-style protection. A switch table with 512 branches suggests a highly complex internal state machine. It handles dozens or hundreds of different "commands" or "states," making it nearly impossible for an analyst to map out the logic by hand.

---

### Summary of Technical Indicators (Updated)

| Category | Observed Technique | Specific Indicator/Observation |
| :--- | :--- | :--- |
| **Encryption** | Advanced SIMD-Accelerated Decryption | Extensive use of `vpaddd_avx`, `vpshufd_avx` for bulk data transformation. |
| **Evasion** | Anti-Sandbox Stall | Usage of `SetWaitableTimer` and `Sleep` to time out automated analysis. |
| **Evasion** | Timing Checks | Use of `QueryPerformanceCounter` to detect debugger/manual interaction. |
| **Obfuscation** | Control Flow Flattening / VM Dispatch | Massive switch tables (up to 512 cases) to hide the execution path. |
| **Complexity** | Multi-stage Loader Engine | Robust internal logic for managing complex data structures and states. |

### Conclusion
The addition of this code confirms that the binary is not a simple "dropper" but a **highly sophisticated, professional loader**. It is engineered to resist both automated analysis (via time-based stalling) and manual analysis (via heavy SIMD obfuscation and massive state machine complexity). The sheer scale of the jump tables and the specialized use of AVX instructions suggest this tool was designed for high-value targets where evading detection from advanced security products is a primary requirement.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of SIMD-accelerated bulk decryption (AVX) and complex state machines/control flow flattening is used to hide the malware's true functionality from analysts. |
| **T1497** | Virtualization/Sandbox | The implementation of `SetWaitableTimer`, `Sleep` functions, and `QueryPerformanceCounter` timing checks are designed to bypass automated sandboxes and detect manual debugging. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the intelligence report. 

**Note:** The "Extracted Strings" section appears to contain heavily obfuscated or junk data (likely from a packed/encrypted section of the binary), resulting in no high-fidelity network or file system IOCs within that specific block.

### **Indicators of Compromise (IOCs)**

#### **IP addresses / URLs / Domains**
*   None identified.

#### **File paths / Registry keys**
*   None identified. (Note: Internal memory offsets such as `fcn.1401df610` were observed but are not persistent filesystem indicators).

#### **Mutex names / Named pipes**
*   None identified.

#### **Hashes**
*   None identified. (The string "fffff." and various character strings do not correspond to MD5, SHA-1, or SHA-256 formats).

#### **Other artifacts**
*   **Anti-Analysis API Patterns:** 
    *   `CreateWaitableTimerExW` / `SetWaitableTimer` (Used for anti-sandbox stalling)
    *   `WaitForSingleObject` (Used in conjunction with timers to stall execution)
    *   `QueryPerformanceCounter` / `QueryPerformanceFrequency` (Used for high-precision timing checks to detect debuggers/human interaction)
*   **Instruction Set Signatures:** 
    *   Extensive use of AVX instructions (`vpaddd_avx`, `vpsrld_avx`, `vpshufd_avx`) indicates a sophisticated, high-performance encryption/decryption routine for large data payloads.
*   **Structural Indicators:**
    *   Control Flow Flattening: Presence of massive switch tables (up to 512 cases) suggests a custom virtual machine or highly complex state machine used to obfuscate execution logic.

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification of the sample:

1.  **Malware family:** custom
2.  **Malware type:** loader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Advanced Cryptographic Handling:** The use of AVX (SIMD) instructions (`vpaddd_avx`, `vpshufd_avx`) for bulk decryption indicates the primary purpose is to decrypt and manage a large, complex payload in memory rather than performing direct malicious actions like file encryption or data exfiltration.
    *   **Robust Anti-Analysis Suite:** The implementation of "Waitable Timer" abuse for sandbox timeouts and `QueryPerformanceCounter` for timing analysis confirms it is designed to bypass automated security systems and detect the presence of human analysts/debuggers.
    *   **Sophisticated Code Obfuscation:** The presence of control flow flattening with massive switch tables (up to 512 cases) suggests a professional-grade "crypter" or loader architecture designed to hide the execution logic from manual reverse engineering.
