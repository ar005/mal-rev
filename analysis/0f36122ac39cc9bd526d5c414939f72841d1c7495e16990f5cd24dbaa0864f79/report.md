# Threat Analysis Report

**Generated:** 2026-08-15 20:11 UTC
**Sample:** `0f36122ac39cc9bd526d5c414939f72841d1c7495e16990f5cd24dbaa0864f79_0f36122ac39cc9bd526d5c414939f72841d1c7495e16990f5cd24dbaa0864f79.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f36122ac39cc9bd526d5c414939f72841d1c7495e16990f5cd24dbaa0864f79_0f36122ac39cc9bd526d5c414939f72841d1c7495e16990f5cd24dbaa0864f79.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 110,080 bytes |
| MD5 | `dfc30c27b902bcc7b03dc54929ad54e7` |
| SHA1 | `66d49b6ac1debec1bb3d1d8357e3b950152f515e` |
| SHA256 | `0f36122ac39cc9bd526d5c414939f72841d1c7495e16990f5cd24dbaa0864f79` |
| Overall entropy | 5.939 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768010033 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 57,856 | 6.424 | No |
| `.rdata` | 41,472 | 4.77 | No |
| `.data` | 3,072 | 2.08 | No |
| `.pdata` | 4,096 | 4.815 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.855 | No |

### Imports

**ole32.dll**: `CoInitializeEx`, `CoUninitialize`
**OLEAUT32.dll**: `SafeArrayCreate`, `SafeArrayDestroy`, `SafeArrayGetUBound`, `SafeArrayAccessData`, `SafeArrayUnaccessData`, `SafeArrayPutElement`, `SafeArrayCreateVector`, `VariantInit`, `VariantClear`
**SHELL32.dll**: `SHGetFolderPathA`
**USER32.dll**: `wsprintfA`, `GetMessageA`, `TranslateMessage`, `DispatchMessageA`
**ADVAPI32.dll**: `GetUserNameA`
**KERNEL32.dll**: `CreateFileW`, `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleOutputCP`, `WriteFile`, `WriteConsoleW`, `SetStdHandle`, `HeapReAlloc`, `HeapSize`, `GetStringTypeW`, `GetFileType`, `GetStdHandle`, `GetProcessHeap`, `FlushFileBuffers`, `FlsSetValue`

### Exports

`GetFileVersionInfoA`, `GetFileVersionInfoByHandle`, `GetFileVersionInfoExA`, `GetFileVersionInfoExW`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoSizeExA`, `GetFileVersionInfoSizeExW`, `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`, `VerFindFileA`, `VerFindFileW`, `VerInstallFileA`, `VerInstallFileW`, `VerLanguageNameA`, `VerLanguageNameW`, `VerQueryValueA`, `VerQueryValueW`

## Extracted Strings

Total strings found: **461** (showing first 100)

```
!This program cannot be run in DOS mode.
$
=Richq
`.rdata
@.data
.pdata
@.fptable
.reloc
D$HH+D$PHi
D$ R+M
H9D$`r
@USAUH
D$Hbin
@USATAUAWH
EHmsco
ELree.
PPD9l$h
A_A]A\[]
HcH<E3
t_HcH<E3
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
	H;rY
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180006778` | `0x180006778` | 13503 | ✓ |
| `fcn.180006740` | `0x180006740` | 13498 | ✓ |
| `fcn.180002dfc` | `0x180002dfc` | 11719 | ✓ |
| `fcn.180002cfc` | `0x180002cfc` | 2622 | ✓ |
| `fcn.180002e8c` | `0x180002e8c` | 2344 | ✓ |
| `fcn.180008274` | `0x180008274` | 1985 | ✓ |
| `fcn.18000e120` | `0x18000e120` | 1677 | ✓ |
| `fcn.180001830` | `0x180001830` | 1392 | ✓ |
| `fcn.180004628` | `0x180004628` | 1213 | ✓ |
| `fcn.18000c620` | `0x18000c620` | 1171 | ✓ |
| `fcn.180002060` | `0x180002060` | 1054 | ✓ |
| `fcn.18000b660` | `0x18000b660` | 922 | ✓ |
| `fcn.18000e7d0` | `0x18000e7d0` | 920 | ✓ |
| `fcn.18000b0f0` | `0x18000b0f0` | 920 | ✓ |
| `fcn.1800028c0` | `0x1800028c0` | 892 | ✓ |
| `fcn.180007e78` | `0x180007e78` | 862 | ✓ |
| `fcn.18000bc44` | `0x18000bc44` | 817 | ✓ |
| `fcn.18000cf6c` | `0x18000cf6c` | 815 | ✓ |
| `fcn.1800012d0` | `0x1800012d0` | 753 | ✓ |
| `fcn.180008d40` | `0x180008d40` | 712 | ✓ |
| `fcn.180001da0` | `0x180001da0` | 694 | ✓ |
| `fcn.1800030e8` | `0x1800030e8` | 667 | ✓ |
| `fcn.180002480` | `0x180002480` | 660 | ✓ |
| `fcn.18000899c` | `0x18000899c` | 623 | ✓ |
| `fcn.180001060` | `0x180001060` | 609 | ✓ |
| `fcn.180009dd4` | `0x180009dd4` | 604 | ✓ |
| `fcn.1800015d0` | `0x1800015d0` | 596 | ✓ |
| `fcn.180006448` | `0x180006448` | 589 | ✓ |
| `fcn.180004ae8` | `0x180004ae8` | 584 | ✓ |
| `fcn.180005088` | `0x180005088` | 557 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001060.c`](code/fcn.180001060.c)
- [`code/fcn.1800012d0.c`](code/fcn.1800012d0.c)
- [`code/fcn.1800015d0.c`](code/fcn.1800015d0.c)
- [`code/fcn.180001830.c`](code/fcn.180001830.c)
- [`code/fcn.180001da0.c`](code/fcn.180001da0.c)
- [`code/fcn.180002060.c`](code/fcn.180002060.c)
- [`code/fcn.180002480.c`](code/fcn.180002480.c)
- [`code/fcn.1800028c0.c`](code/fcn.1800028c0.c)
- [`code/fcn.180002cfc.c`](code/fcn.180002cfc.c)
- [`code/fcn.180002dfc.c`](code/fcn.180002dfc.c)
- [`code/fcn.180002e8c.c`](code/fcn.180002e8c.c)
- [`code/fcn.1800030e8.c`](code/fcn.1800030e8.c)
- [`code/fcn.180004628.c`](code/fcn.180004628.c)
- [`code/fcn.180004ae8.c`](code/fcn.180004ae8.c)
- [`code/fcn.180005088.c`](code/fcn.180005088.c)
- [`code/fcn.180006448.c`](code/fcn.180006448.c)
- [`code/fcn.180006740.c`](code/fcn.180006740.c)
- [`code/fcn.180006778.c`](code/fcn.180006778.c)
- [`code/fcn.180007e78.c`](code/fcn.180007e78.c)
- [`code/fcn.180008274.c`](code/fcn.180008274.c)
- [`code/fcn.18000899c.c`](code/fcn.18000899c.c)
- [`code/fcn.180008d40.c`](code/fcn.180008d40.c)
- [`code/fcn.180009dd4.c`](code/fcn.180009dd4.c)
- [`code/fcn.18000b0f0.c`](code/fcn.18000b0f0.c)
- [`code/fcn.18000b660.c`](code/fcn.18000b660.c)
- [`code/fcn.18000bc44.c`](code/fcn.18000bc44.c)
- [`code/fcn.18000c620.c`](code/fcn.18000c620.c)
- [`code/fcn.18000cf6c.c`](code/fcn.18000cf6c.c)
- [`code/fcn.18000e120.c`](code/fcn.18000e120.c)
- [`code/fcn.18000e7d0.c`](code/fcn.18000e7d0.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, I have updated the analysis. The binary continues to exhibit highly sophisticated behaviors consistent with a professional-grade malware sample, specifically targeting the bypass of advanced security monitors (EDR/AV).

### Updated Analysis Summary

#### Core Functionality and Purpose
The binary is a **multi-stage downloader and stealthy execution loader**. It incorporates high-level evasion techniques to ensure that even if it is executed by an automated sandbox or monitored by EDR, its primary malicious actions (payload retrieval and persistence) are delayed or hidden.

### New & Enhanced Findings (Chunk 2)

*   **Sophisticated Hook Evasion via Exception Handling:**
    In `fcn.180001da0`, the binary performs a very specific sequence: it finds a signature in memory, uses `VirtualProtect` to modify permissions, and then calls **`AddVectoredExceptionHandler` (AVH)**. This is followed by retrieving the thread context (`GetThreadContext`) and modifying it via `SetThreadContext`.
    *   **Significance:** This technique is often used to bypass "inline hooks" placed by security software. By using a Vectored Exception Handler, the malware can intercept transitions or exceptions that would otherwise trigger an EDR's monitoring logic.

*   **Advanced Environment Fingerprinting (Anti-VM/Sandbox):**
    Function `fcn.1800030e8` is heavily involved in **CPUID instructions**. It checks for specific hardware features, bitfields in the CPU's reported capabilities, and extended feature enumerations. 
    *   **Significance:** This confirms a high level of maturity; the malware is "fingerprinting" the hardware to detect if it is running inside a virtual machine (VMWare/VirtualBox) or an emulated sandbox environment before executing its main payload.

*   **Timing-based Evasion:**
    In `fcn.1800015d0`, there is a clear call to `Sleep()` following a series of initial checks. 
    *   **Significance:** This "sleep" tactic is designed to outlast the analysis window of automated sandboxes, which typically monitor a file for only a few minutes.

*   **Heavy Resource Processing & State Management:**
    The logic in `fcn.180008d40` and several other functions suggests that the binary manages complex internal states or configuration files. It uses extensive loops to iterate through memory blocks, applying bitwise masks and adjustments to internal structures.

*   **Staged Execution Pipeline:**
    Function `fcn.1800015d0` acts as a primary "orchestrator." It confirms the sequence of operations: 
    1.  Initial environmental checks (`fcn.180001060`).
    2.  Wait/Sleep (to bypass sandboxes).
    3.  Core logic processing and memory manipulation.
    4.  Persistence logic (`fcn.180002060` from Chunk 1).

### Updated Summary Table

| Feature | Observation | Risk Level | Detection Difficulty |
| :--- | :--- | :--- | :--- |
| **Persistence** | Creates `\Programs` folders and moves files via `CopyFileA`. | High | Medium |
| **Evasion (Anti-Hook)** | Uses `AddVectoredExceptionHandler` and `SetThreadContext` to bypass EDR hooks. | Critical | High |
| **Evasion (Anti-VM)** | Extensive CPUID checks to detect virtualization/sandboxes. | High | High |
| **Obfuscation** | Multiple layers of XOR-based string decryption for all API calls and data. | Medium | Medium |
| **Staging** | Deliberate sleep cycles and multi-step logic flow to evade automated analysis. | High | High |

### Technical Conclusion (Updated)
The addition of **AVH manipulation**, **CPUID-based environment fingerprinting**, and the **orchestrated execution sequence** confirms this is a high-tier threat. The malware isn't just trying to hide its strings; it is actively looking for signs of analysis tools and bypassing the low-level hooks that security products use to intercept system calls.

The presence of the "Mozilla/5.0" string combined with these evasion techniques suggests the final payload may involve a browser-based component or an HTTP/HTTPS-based command and control (C2) communication designed to blend in with legitimate web traffic.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided analysis to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1562** | Impair Defenses | The use of `AddVectoredExceptionHandler` and `SetThreadContext` is a specific technique to bypass inline hooks used by security products. |
| **T1562** | Impair Defenses | The implementation of CPUID instructions serves as an environment fingerprinting method to detect and evade analysis in VMs or sandboxes. |
| **T1562** | Impair Defenses | The use of `Sleep()` functions is a standard evasion tactic used to outlast the monitoring window of automated sandbox environments. |
| **T1027** | Obfuscated Files or Information | The use of multiple layers of XOR-based decryption for strings and API calls hides the malware's functionality from static analysis. |
| **T1547** | Boot or Logon Autostart Execution | The creation of specific directories (e.g., `\Programs`) and moving files via `CopyFileA` indicates a strategy to establish persistence on the system. |
| **T1030** | Data Manipulation | *(Alternative for Staging)* While "Staged" is a tactic, the complex multi-step logic flow and state management can also be viewed as part of the internal orchestration of the malware's execution. |

*(Note: Because "Staging," "Anti-Hook," and "Anti-VM/Sandbox" are all fundamentally methods to circumvent security controls or analysis tools, they all map primarily to the **T1562 (Impair Defenses)** technique in the MITRE ATT&CK framework.)*

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral reports, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `https://files.ca` (Extracted from obfuscated string)

**File paths / Registry keys**
*   `%s\Programs` 
*   `%s\Programs\Common`
*(Note: These are used for staging and persistence.)*

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   No cryptographic hashes were present in the provided data.

**Other artifacts**
*   **User-Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64)`
*   **Evasion Techniques:**
    *   **Anti-Hooking:** Use of `AddVectoredExceptionHandler` and `SetThreadContext` to bypass EDR monitoring.
    *   **Anti-VM/Sandbox:** Extensive use of `CPUID` instructions for hardware fingerprinting.
    *   **Time Delay:** Implementation of `Sleep()` cycles to outlast automated sandbox analysis windows.
    *   **Staged Execution:** A multi-step pipeline involving environment checks, sleep cycles, and subsequent persistence logic.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `https://files.caCLRCreateInstancbE_NYEN_d[NE~YGjeRPfBRENaV[BRrOv`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: Loader (or "Unknown" if requiring a specific branded name)
2. **Malware type**: Loader / Downloader
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Evasion Tactics:** The use of `AddVectoredExceptionHandler` and `SetThreadContext` specifically targets the bypass of EDR inline hooks, combined with intensive `CPUID` fingerprinting to detect virtualized or sandbox environments.
    *   **Multi-stage Execution Logic:** The analysis confirms a "staged" architecture involving deliberate sleep cycles (to outlast automated sandboxes), XOR-based string obfuscation, and a dedicated pipeline for environmental checks before executing persistence mechanisms.
    *   **Infection Strategy:** The presence of a standard User-Agent (`Mozilla/5.0`) combined with the identification of it as a "multi-stage downloader" indicates its primary role is to establish a foothold and pull down further malicious payloads (such as a RAT or info-stealer) while evading security controls.
