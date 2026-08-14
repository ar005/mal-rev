# Threat Analysis Report

**Generated:** 2026-08-12 16:44 UTC
**Sample:** `0e6e36bbddb377f477e49c6555b10d0cd7e9c2d5715dd925a31caf1fd6d4706d_0e6e36bbddb377f477e49c6555b10d0cd7e9c2d5715dd925a31caf1fd6d4706d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e6e36bbddb377f477e49c6555b10d0cd7e9c2d5715dd925a31caf1fd6d4706d_0e6e36bbddb377f477e49c6555b10d0cd7e9c2d5715dd925a31caf1fd6d4706d.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 104,448 bytes |
| MD5 | `4978ed03bfc965f76de5e5125db2255f` |
| SHA1 | `7c66035245ca703453e506518599dcb0ca7e58ea` |
| SHA256 | `0e6e36bbddb377f477e49c6555b10d0cd7e9c2d5715dd925a31caf1fd6d4706d` |
| Overall entropy | 5.877 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767628143 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 53,760 | 6.412 | No |
| `.rdata` | 39,936 | 4.68 | No |
| `.data` | 3,072 | 2.096 | No |
| `.pdata` | 4,096 | 4.744 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.848 | No |

### Imports

**WININET.dll**: `InternetOpenA`, `InternetReadFile`, `InternetOpenUrlA`, `InternetCloseHandle`
**USER32.dll**: `DispatchMessageA`, `TranslateMessage`, `GetMessageA`
**KERNEL32.dll**: `IsProcessorFeaturePresent`, `WriteConsoleW`, `CreateFileW`, `SetFilePointerEx`, `GetConsoleMode`, `IsDebuggerPresent`, `CheckRemoteDebuggerPresent`, `CloseHandle`, `Sleep`, `GetCurrentProcess`, `CreateThread`, `FlushInstructionCache`, `GetTickCount`, `VirtualAlloc`, `DisableThreadLibraryCalls`

### Exports

`get_hostfxr_path`

## Extracted Strings

Total strings found: **387** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
.reloc
\$ ATAVAWH
A9OTv 
I+_0t~A
0A_A^A\
0A_A^A\
UVWAVAWH
A_A^_^]
|$ AVH
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
f9)u4H9j
u%@8j(t
v@8k(t
8D$@tH
l$ VWATAVAWH
L$&8\$&t,8Y
A_A^A\_^
t$ WATAUAVAWH
 A_A^A]A\_
fD9t$b
t$ WATAUAVAWH
D!|$xA
A_A^A]A\_
L$ VWAVH
fD94H}aD
@SUVWATAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180005720` | `0x180005720` | 13511 | ✓ |
| `fcn.1800056e8` | `0x1800056e8` | 13506 | ✓ |
| `fcn.180001eec` | `0x180001eec` | 11391 | ✓ |
| `fcn.180001dec` | `0x180001dec` | 2302 | ✓ |
| `fcn.180001f7c` | `0x180001f7c` | 2024 | ✓ |
| `fcn.180007224` | `0x180007224` | 1985 | ✓ |
| `fcn.18000d490` | `0x18000d490` | 1677 | ✓ |
| `fcn.1800035dc` | `0x1800035dc` | 1213 | ✓ |
| `fcn.18000b5d0` | `0x18000b5d0` | 1171 | ✓ |
| `fcn.18000a610` | `0x18000a610` | 922 | ✓ |
| `fcn.18000d0d0` | `0x18000d0d0` | 920 | ✓ |
| `fcn.18000a0a0` | `0x18000a0a0` | 920 | ✓ |
| `fcn.1800019b0` | `0x1800019b0` | 892 | ✓ |
| `fcn.180006e28` | `0x180006e28` | 862 | ✓ |
| `fcn.18000abf4` | `0x18000abf4` | 817 | ✓ |
| `fcn.18000bf1c` | `0x18000bf1c` | 815 | ✓ |
| `section..text` | `0x180001000` | 780 | ✓ |
| `fcn.180007cf0` | `0x180007cf0` | 712 | ✓ |
| `fcn.1800015c0` | `0x1800015c0` | 689 | ✓ |
| `fcn.180001310` | `0x180001310` | 681 | ✓ |
| `fcn.1800021d8` | `0x1800021d8` | 667 | ✓ |
| `fcn.18000794c` | `0x18000794c` | 623 | ✓ |
| `fcn.180008d84` | `0x180008d84` | 604 | ✓ |
| `fcn.1800053f0` | `0x1800053f0` | 589 | ✓ |
| `fcn.180003a9c` | `0x180003a9c` | 584 | ✓ |
| `fcn.18000403c` | `0x18000403c` | 557 | ✓ |
| `fcn.180009c4c` | `0x180009c4c` | 555 | ✓ |
| `fcn.180002490` | `0x180002490` | 517 | ✓ |
| `fcn.180007754` | `0x180007754` | 501 | ✓ |
| `fcn.180003250` | `0x180003250` | 499 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001310.c`](code/fcn.180001310.c)
- [`code/fcn.1800015c0.c`](code/fcn.1800015c0.c)
- [`code/fcn.1800019b0.c`](code/fcn.1800019b0.c)
- [`code/fcn.180001dec.c`](code/fcn.180001dec.c)
- [`code/fcn.180001eec.c`](code/fcn.180001eec.c)
- [`code/fcn.180001f7c.c`](code/fcn.180001f7c.c)
- [`code/fcn.1800021d8.c`](code/fcn.1800021d8.c)
- [`code/fcn.180002490.c`](code/fcn.180002490.c)
- [`code/fcn.180003250.c`](code/fcn.180003250.c)
- [`code/fcn.1800035dc.c`](code/fcn.1800035dc.c)
- [`code/fcn.180003a9c.c`](code/fcn.180003a9c.c)
- [`code/fcn.18000403c.c`](code/fcn.18000403c.c)
- [`code/fcn.1800053f0.c`](code/fcn.1800053f0.c)
- [`code/fcn.1800056e8.c`](code/fcn.1800056e8.c)
- [`code/fcn.180005720.c`](code/fcn.180005720.c)
- [`code/fcn.180006e28.c`](code/fcn.180006e28.c)
- [`code/fcn.180007224.c`](code/fcn.180007224.c)
- [`code/fcn.180007754.c`](code/fcn.180007754.c)
- [`code/fcn.18000794c.c`](code/fcn.18000794c.c)
- [`code/fcn.180007cf0.c`](code/fcn.180007cf0.c)
- [`code/fcn.180008d84.c`](code/fcn.180008d84.c)
- [`code/fcn.180009c4c.c`](code/fcn.180009c4c.c)
- [`code/fcn.18000a0a0.c`](code/fcn.18000a0a0.c)
- [`code/fcn.18000a610.c`](code/fcn.18000a610.c)
- [`code/fcn.18000abf4.c`](code/fcn.18000abf4.c)
- [`code/fcn.18000b5d0.c`](code/fcn.18000b5d0.c)
- [`code/fcn.18000bf1c.c`](code/fcn.18000bf1c.c)
- [`code/fcn.18000d0d0.c`](code/fcn.18000d0d0.c)
- [`code/fcn.18000d490.c`](code/fcn.18000d490.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, I have updated and expanded the analysis. The presence of these specific code blocks confirms that this is a **sophisticated, multi-stage loader** featuring advanced evasion techniques and a "Reflective Loader" mechanism.

---

### Updated Analysis Report

#### 1. Core Functionality and Purpose
*   **In-Memory PE Mapping (Reflective Loading):** The function `fcn.180001310` is a textbook example of a **reflective loader**. It performs the following actions:
    *   Parses the **MZ** header and **PE** structure in memory.
    *   Uses `VirtualAlloc` to allocate space for the payload.
    *   Iterates through sections to copy data into allocated buffers.
    *   Manually resolves imports (`GetProcAddress`) and handles relocation (the logic around `0x18000200` or similar).
    *   Calls `FlushInstructionCache` followed by `CreateThread`.
    *   **Significance:** This allows the malware to execute its "real" payload in memory without ever writing the decrypted executable to the disk, making it very difficult for traditional antivirus (AV) and Endpoint Detection and Response (EDR) systems to detect.

*   **Custom Interpreter / Virtual Machine Engine:** The heavy use of nested loops, jump tables, and repeated checks against specific constants (e.g., `0x3a4`, `0x3a8`, `0x3b5`) in the first section suggests a **custom execution environment**. Instead of executing raw machine code immediately after decryption, the loader may pass the payload to an internal "interpreter" that processes custom opcodes.

*   **Multi-Stage Decryption:** The function `fcn.1800015c0` contains a significant XOR-based decryption loop (`XOR ... & 0xff`). This indicates that even after the data is fetched from the internet (WinINet), it undergoes multiple layers of transformation before being passed to the loader.

#### 2. Advanced Anti-Analysis & Evasion
The second chunk reveals much more sophisticated evasion than simple `IsDebuggerPresent` calls:

*   **Anti-Virtualization & Fingerprinting:** The function `fcn.1800021d8` makes extensive use of the **`CPUID` instruction**. 
    *   It checks for specific processor features and bitmasks (e.g., `0x8000`, `0xffffffffffffffff`).
    *   This is used to detect if the code is running inside a Virtual Machine (VM), an emulator, or a sandbox by checking for hardware "leaks" that occur in virtualized environments.
*   **Execution Flow Obfuscation:** The use of `swi(3)` (Software Interrupts) and complex state-machine logic indicates a desire to break the flow of automated analysis tools. If an automated scanner doesn't perfectly replicate the processor's handling of these interrupts, it will fail to reach the "malicious" part of the code.
*   **Control Flow Flattening:** The repetitive `CONCAT` operations and nested loops (seen in `fcn.1800015c0`) are typical of **LLVM-based obfuscation**. This is designed to exhaust the resources of an analyst trying to trace the logic manually or through a decompiler.

#### 3. Key Technical Indicators
*   **Reflective Loading:** The code explicitly handles the mapping of PE headers and relocation tables into memory (`fcn.180001310`).
*   **Custom XOR Tables:** The use of pre-calculated arrays (likely `auStack_138` in your disassembly) for decryption suggests a complex key schedule rather than a single repeating byte.
*   **Hardware Fingerprinting:** Heavy reliance on `CPUID` and manual register checks to verify the environment's authenticity.

### Updated Summary for Incident Response
The complexity of this binary indicates it is not a common, "low-effort" piece of malware. It belongs to a **sophisticated threat actor** or utilizes a highly professional multi-tool toolkit (like those used by APT groups).

**Key Risks:**
1.  **Fileless Execution:** Because the payload is decrypted and mapped directly into memory (`fcn.180001310`), standard disk scans will **not** find the final malicious component. 
2.  **Sandbox Evasion:** The heavy `CPUID` checks mean that many automated "sandboxes" (like JoeSecurity or Any.Run) may fail to trigger the full payload, as the malware will detect they are not running on a physical workstation.
3.  **Persistence/Payload:** While this specific binary is just the *loader*, its presence confirms an intent to run high-level commands, likely including data exfiltration (via the established WinINet connection), credential theft, or establishing a backdoor.

**Recommended Actions:**
*   **Memory Forensics:** Since the payload is decrypted in memory, perform a memory dump of the process after it has stayed active for some time to capture the "unpacked" stage.
*   **Network Monitoring:** Monitor for outbound connections to `tbox.moe` or related IP ranges identified in the first stage.
*   **EDR Tuning:** Configure EDR solutions to flag "Reflective Loading" behaviors, specifically `VirtualAlloc` followed by `CreateThread` from a memory region that does not have a corresponding file on disk.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1035.005** | Reflective Loader | The malware manually maps PE structures, resolves imports via `GetProcAddress`, and executes the payload in memory to bypass disk-based detection. |
| **T1027** | Obfuscated Files or Programs | The use of multi-stage XOR decryption, a custom VM engine, and control flow flattening are employed to hinder manual analysis and hide the execution logic. |
| **T1497** | Virtualized Environment | The code utilizes `CPUID` instructions and bitmask checks to identify if it is running in a sandbox or virtual machine environment. |
| **T1036** | Dynamic Resolution | The use of `GetProcAddress` within the reflective loader allows the malware to resolve function addresses at runtime rather than using a static import table. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `tbox.moe`
*   `files.ca`
*   `tbox.moe/pp87l9.https://files.ca` (Specific URL pattern/path)

**File paths / Registry keys**
*   *None identified.* (Note: Internal PE structures such as `.rdata` and `.pdata` were excluded as they are standard system components).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None found in the provided text.*

**Other artifacts**
*   **User Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36`
*   **Reflective Loader Behavior:** Function `fcn.180001310` performs in-memory mapping of the MZ header, PE structure, and manual resolution of imports (GetProcAddress).
*   **Decryption Routine:** XOR-based decryption loop (`XOR ... & 0xff`) located at function `fcn.1800015c0`.
*   **Anti-Analysis Techniques:**
    *   **Hardware Fingerprinting:** Extensive use of the `CPUID` instruction to detect virtualized environments and sandboxes.
    *   **Execution Flow Obfuscation:** Use of `swi(3)` (Software Interrupts) and LLVM-based control flow flattening.
    *   **Memory Execution:** Presence of "Reflective Loading" where the final payload is executed in memory without being written to disk.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `https://files.ca`

---

## Malware Family Classification

Based on the provided analysis results, here is the classification:

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**: 
    *   **Reflective Loading Mechanics:** The sample implements a sophisticated reflective loader (fcn.180001310) that maps PE headers and resolves imports in memory, allowing the payload to run without ever touching the disk.
    *   **Advanced Evasion & Obfuscation:** The inclusion of a custom VM engine/interpreter, LLVM-based control flow flattening, and multi-stage XOR decryption indicates a high level of engineering meant to thwart both automated sandboxes and manual analysis.
    *   **Environment Fingerprinting:** Extensive use of the `CPUID` instruction for hardware checks confirms specific intent to bypass virtualization and sandbox environments (T1497).
