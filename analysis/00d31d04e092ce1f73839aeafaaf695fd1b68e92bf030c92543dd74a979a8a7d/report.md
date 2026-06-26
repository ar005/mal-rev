# Threat Analysis Report

**Generated:** 2026-06-25 13:01 UTC
**Sample:** `00d31d04e092ce1f73839aeafaaf695fd1b68e92bf030c92543dd74a979a8a7d_00d31d04e092ce1f73839aeafaaf695fd1b68e92bf030c92543dd74a979a8a7d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00d31d04e092ce1f73839aeafaaf695fd1b68e92bf030c92543dd74a979a8a7d_00d31d04e092ce1f73839aeafaaf695fd1b68e92bf030c92543dd74a979a8a7d.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 107,008 bytes |
| MD5 | `b39c59046edc5d74d806d51d3d02a213` |
| SHA1 | `8571f618eabd32d3f60f1133aa4c278feb958423` |
| SHA256 | `00d31d04e092ce1f73839aeafaaf695fd1b68e92bf030c92543dd74a979a8a7d` |
| Overall entropy | 5.892 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767989490 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 55,808 | 6.402 | No |
| `.rdata` | 40,448 | 4.722 | No |
| `.data` | 3,072 | 2.087 | No |
| `.pdata` | 4,096 | 4.741 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.845 | No |

### Imports

**ole32.dll**: `CoInitializeEx`, `CoUninitialize`
**OLEAUT32.dll**: `SafeArrayCreate`, `SafeArrayDestroy`, `SafeArrayGetUBound`, `SafeArrayAccessData`, `SafeArrayUnaccessData`, `VariantClear`, `VariantInit`, `SafeArrayCreateVector`, `SafeArrayPutElement`
**USER32.dll**: `TranslateMessage`, `DispatchMessageA`, `GetMessageA`
**ADVAPI32.dll**: `GetUserNameA`
**KERNEL32.dll**: `CreateFileW`, `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleOutputCP`, `WriteConsoleW`, `FlushFileBuffers`, `SetStdHandle`, `HeapReAlloc`, `HeapSize`, `GetStringTypeW`, `GetFileType`, `WriteFile`, `InitializeCriticalSectionEx`, `CreateFileA`, `GetDiskFreeSpaceExA`

### Exports

`get_hostfxr_path`

## Extracted Strings

Total strings found: **407** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
.reloc
@USATAUAWH
EHmsco
ELree.
PPD9l$h
A_A]A\[]
D$Hbin
D$ >Oy
HcH<E3
t_HcH<E3
D$HH+D$PHi
D$ R+M
H9D$`r
@USAUH
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180005f00` | `0x180005f00` | 13511 | ✓ |
| `fcn.180005ec8` | `0x180005ec8` | 13506 | ✓ |
| `fcn.1800026bc` | `0x1800026bc` | 11407 | ✓ |
| `fcn.1800025bc` | `0x1800025bc` | 2318 | ✓ |
| `fcn.18000274c` | `0x18000274c` | 2040 | ✓ |
| `fcn.180007a04` | `0x180007a04` | 1985 | ✓ |
| `fcn.18000d8b0` | `0x18000d8b0` | 1677 | ✓ |
| `section..text` | `0x180001000` | 1392 | ✓ |
| `fcn.180003db8` | `0x180003db8` | 1213 | ✓ |
| `fcn.18000bdb0` | `0x18000bdb0` | 1171 | ✓ |
| `fcn.18000adf0` | `0x18000adf0` | 922 | ✓ |
| `fcn.18000df60` | `0x18000df60` | 920 | ✓ |
| `fcn.18000a880` | `0x18000a880` | 920 | ✓ |
| `fcn.180002180` | `0x180002180` | 892 | ✓ |
| `fcn.180007608` | `0x180007608` | 862 | ✓ |
| `fcn.18000b3d4` | `0x18000b3d4` | 817 | ✓ |
| `fcn.18000c6fc` | `0x18000c6fc` | 815 | ✓ |
| `fcn.180001d50` | `0x180001d50` | 753 | ✓ |
| `fcn.1800084d0` | `0x1800084d0` | 712 | ✓ |
| `fcn.180001820` | `0x180001820` | 694 | ✓ |
| `fcn.1800029a8` | `0x1800029a8` | 667 | ✓ |
| `fcn.18000812c` | `0x18000812c` | 623 | ✓ |
| `fcn.180001ae0` | `0x180001ae0` | 609 | ✓ |
| `fcn.180009564` | `0x180009564` | 604 | ✓ |
| `fcn.180005bd0` | `0x180005bd0` | 589 | ✓ |
| `fcn.180004278` | `0x180004278` | 584 | ✓ |
| `fcn.180001570` | `0x180001570` | 580 | ✓ |
| `fcn.180004818` | `0x180004818` | 557 | ✓ |
| `fcn.18000a42c` | `0x18000a42c` | 555 | ✓ |
| `fcn.180002c70` | `0x180002c70` | 517 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001570.c`](code/fcn.180001570.c)
- [`code/fcn.180001820.c`](code/fcn.180001820.c)
- [`code/fcn.180001ae0.c`](code/fcn.180001ae0.c)
- [`code/fcn.180001d50.c`](code/fcn.180001d50.c)
- [`code/fcn.180002180.c`](code/fcn.180002180.c)
- [`code/fcn.1800025bc.c`](code/fcn.1800025bc.c)
- [`code/fcn.1800026bc.c`](code/fcn.1800026bc.c)
- [`code/fcn.18000274c.c`](code/fcn.18000274c.c)
- [`code/fcn.1800029a8.c`](code/fcn.1800029a8.c)
- [`code/fcn.180002c70.c`](code/fcn.180002c70.c)
- [`code/fcn.180003db8.c`](code/fcn.180003db8.c)
- [`code/fcn.180004278.c`](code/fcn.180004278.c)
- [`code/fcn.180004818.c`](code/fcn.180004818.c)
- [`code/fcn.180005bd0.c`](code/fcn.180005bd0.c)
- [`code/fcn.180005ec8.c`](code/fcn.180005ec8.c)
- [`code/fcn.180005f00.c`](code/fcn.180005f00.c)
- [`code/fcn.180007608.c`](code/fcn.180007608.c)
- [`code/fcn.180007a04.c`](code/fcn.180007a04.c)
- [`code/fcn.18000812c.c`](code/fcn.18000812c.c)
- [`code/fcn.1800084d0.c`](code/fcn.1800084d0.c)
- [`code/fcn.180009564.c`](code/fcn.180009564.c)
- [`code/fcn.18000a42c.c`](code/fcn.18000a42c.c)
- [`code/fcn.18000a880.c`](code/fcn.18000a880.c)
- [`code/fcn.18000adf0.c`](code/fcn.18000adf0.c)
- [`code/fcn.18000b3d4.c`](code/fcn.18000b3d4.c)
- [`code/fcn.18000bdb0.c`](code/fcn.18000bdb0.c)
- [`code/fcn.18000c6fc.c`](code/fcn.18000c6fc.c)
- [`code/fcn.18000d8b0.c`](code/fcn.18000d8b0.c)
- [`code/fcn.18000df60.c`](code/fcn.18000df60.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This updated analysis incorporates the additional disassembly provided in chunk 2/2. The new data confirms that this is not just a simple "loader" but a sophisticated **multi-stage encryption engine** designed to perform complex state transitions while avoiding detection from modern endpoint security.

---

### Updated Technical Analysis of Binary Sample

#### Core Functionality and Purpose
The binary functions as a high-complexity, multi-stage loader and packer. It employs a "layered" approach: 
1.  **Environment Probing:** Checking hardware capabilities (CPUID) to ensure the environment is suitable for execution.
2.  **Decryption & De-obfuscation:** A heavy emphasis on in-memory decryption of internal strings and payloads.
3.  **Execution Transition via Exceptions:** Using Vectored Exception Handlers (VEH) to transition between "loader" logic and "payload" execution, a technique designed to bypass standard API hooks.

The presence of `GetCPUID` variations, hardware feature checks (`XCR0`), and complex multi-pass decryption routines strongly indicates this is the front-end for a high-grade **Trojan or Ransomware** payload that utilizes significant anti-analysis techniques.

---

### Updated Suspicious or Malicious Behaviors

*   **Advanced Execution Transition (Vectored Exception Handlers):** 
    The function `fcn.180001820` contains a critical malicious pattern: it uses **`AddVectoredExceptionHandler`**. This is used to intercept exceptions at the system level before they are handled by standard Windows logic. In malware, this is frequently used to "hop" between different stages of unpacked code or to redirect execution flow away from hooked APIs.
*   **Intensive Payload Decryption:** 
    In `fcn.180001570`, a complex decryption routine is performed on a data block (identified as `arg1` of length `arg2`). This involves multiple passes, including:
    *   A custom transformation involving bitwise operations (`& 0x800000ff`).
    *   A substitution/permutation step using pre-calculated tables.
    *   This confirms that the actual malicious payload remains encrypted in memory until the final moment of execution.
*   **Anti-Analysis Hardware Checks:** 
    The function `fcn.1800029a8` performs deep inspection of CPU features via **CPUID**. It checks for specific feature sets (like those related to virtualization or specialized instruction sets). This is commonly used by advanced malware to detect if it is running in a sandbox, emulator, or on a researcher's virtual machine.
*   **Manual Resource Processing & Memory Patching:** 
    The code frequently uses `VirtualProtect` to change memory permissions (e.g., from Read-Only to Execute/Write) and manually patches specific offsets within loaded modules. This "hot-patching" is a classic way to bypass security products that monitor standard entry points.
*   **Time-Based Evasion:** 
    The use of `QueryPerformanceCounter` in `fcn.180001ae0` suggests the loader monitors time intervals between operations. If it detects "delay" (caused by a human researcher debugging or an emulator's slow processing), it can choose to terminate, effectively "ghosting" itself from analysis.

---

### Expanded Technical Nuances

*   **Obfuscated String Management:** 
    The code uses multiple levels of string obfuscation. First, individual characters are XOR-ed with keys (as seen in `fcn.180001820`). Second, it dynamically constructs strings at runtime only when needed. This prevents static analysis tools from identifying malicious IPs or file paths.
*   **Custom Translation Layer:** 
    The large loops and switch-like logic found in functions like `fcn.1800084d0` suggest the loader is handling internal "state" transitions. It seems to be validating local configurations (codepages/locales) before proceeding, a common way for loaders to adapt their behavior based on the victim's environment.
*   **Manual PE Parsing & Mapping:** 
    (From previous analysis) The manual parsing of `ntdll` and standard library mapping suggests an intent to bypass "Hook-based" security by avoiding the high-level Win32 API wrappers entirely.

---

### Updated Summary Conclusion
This is a **highly sophisticated, professional-grade packer/loader**. 

The presence of **Vectored Exception Handlers (VEH)** combined with **multi-pass decryption routines** and **CPUID hardware checks** indicates this loader was designed to evade advanced Endpoint Detection and Response (EDR) systems. It does not simply "run" a payload; it reconstructs the environment for a malicious payload, decrypting it in stages while masking its execution flow through exception handling. 

**Final Assessment:** This is almost certainly part of a sophisticated threat actor's toolkit (such as a RAT, info-stealer, or ransomware loader) and should be treated with high severity.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided analysis to the relevant MITRE ATT&CK techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information or System Artifacts | The multi-pass decryption routines, XORed string management, and use of Vectored Exception Handlers (VEH) are intended to hide the malicious payload's true logic from static and dynamic analysis. |
| **T1055** | Process Injection | The use of `VirtualProtect` to change memory permissions and the "hot-patching" of offsets in loaded modules are classic indicators of attempting to bypass security hooks. |
| **T1497** | [Note: If using specific vendor mapping for Anti-VM] / **T1027** | The use of `CPUID` checks and `QueryPerformanceCounter` (timing attacks) are standard anti-analysis techniques used to detect sandboxes or debuggers. |

***

### Analyst Notes on Mapping:
*   **T1027:** This is the primary technique for this sample. It covers the "Layered" approach mentioned in your report, where the complexity of the decryption and the manual construction of strings are designed specifically to evade detection by automated security tools.
*   **T1055 (Process Injection):** While "Injection" often implies moving code between processes, in threat intelligence contexts, it is also used to describe techniques that manipulate memory permissions (`VirtualProtect`) and modify executable code within a process's own space to bypass EDR monitoring.
*   **Anti-Analysis Tactics:** The specific behaviors of `CPUID` (Hardware check) and `QueryPerformanceCounter` (Time-based evasion) are core components of the **Defense Evasion** tactic; while they don't always have unique sub-techniques in every version of MITRE, they are most accurately categorized under the broad umbrella of obfuscation (**T1027**).

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized for your investigation:

**IP addresses / URLs / Domains**
*   `https://files.ca`
*   `tbox.moe` (Likely part of a URI path or a related domain structure)

**File paths / Registry keys**
*   *None identified.* (Note: `C:\Windows\System32\ntdll.dll` was excluded as it is a standard system file).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None found in the provided strings.*

**Other artifacts**
*   **User Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64)`
*   **Suspicious Function Offsets/Names:**
    *   `fcn.180001820` (Associated with Vectored Exception Handlers)
    *   `fcn.180001570` (Decryption routine)
    *   `fcn.1800029a8` (CPUID/Anti-analysis check)
    *   `fcn.180001ae0` (Time-based evasion)
*   **Malicious Capabilities / Indicators of Behavior:**
    *   Use of `AddVectoredExceptionHandler` to bypass standard API hooks.
    *   Execution of `GetCPUID` for environment/sandbox detection.
    *   Frequent use of `VirtualProtect` for memory permission manipulation (manual patching).
    *   **QueryPerformanceCounter** usage for timing-based evasion.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Evasion Techniques:** The use of Vectored Exception Handlers (VEH) and manual `ntdll` parsing specifically indicates a design intended to bypass standard Windows API hooks used by EDR/AV solutions.
*   **Complex Multi-Stage Loading:** The presence of multi-pass decryption routines, "hot-patching" via `VirtualProtect`, and a custom translation layer confirms the sample is a sophisticated packer/loader designed to decrypt and stage a secondary payload (likely a RAT or Ransomware) in memory.
*   **Robust Anti-Analysis suite:** The integration of `CPUID` checks for virtualization detection and `QueryPerformanceCounter` for timing-based evasion identifies this as a professional-grade tool used by sophisticated threat actors to "ghost" through automated sandboxes.
