# Threat Analysis Report

**Generated:** 2026-08-18 19:51 UTC
**Sample:** `105987492bef48ec9dce03ad6ada29ce8d3b71622cd8110e75f6aa6d55f24538_105987492bef48ec9dce03ad6ada29ce8d3b71622cd8110e75f6aa6d55f24538.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `105987492bef48ec9dce03ad6ada29ce8d3b71622cd8110e75f6aa6d55f24538_105987492bef48ec9dce03ad6ada29ce8d3b71622cd8110e75f6aa6d55f24538.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 358,400 bytes |
| MD5 | `2c8e79969cc426f5f90c0eeb8b5349a9` |
| SHA1 | `32e4bca242d6b071eece71b732138a6e73158b52` |
| SHA256 | `105987492bef48ec9dce03ad6ada29ce8d3b71622cd8110e75f6aa6d55f24538` |
| Overall entropy | 7.571 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1777644301 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 72,192 | 6.396 | No |
| `.rdata` | 41,984 | 4.747 | No |
| `.data` | 235,008 | 7.988 | ⚠️ Yes |
| `.pdata` | 4,608 | 4.873 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 1,024 | 2.974 | No |
| `.reloc` | 2,048 | 4.888 | No |

### Imports

**USER32.dll**: `PostQuitMessage`, `GetMonitorInfoA`, `MonitorFromPoint`, `DestroyIcon`, `LoadIconA`, `GetDesktopWindow`, `GetSysColor`, `SetCaretPos`, `GetCursorPos`, `MessageBoxA`, `GetWindowTextLengthA`, `SetWindowTextA`, `ReleaseDC`, `GetDC`, `TrackPopupMenu`
**KERNEL32.dll**: `GetConsoleMode`, `GetConsoleOutputCP`, `FlushFileBuffers`, `HeapReAlloc`, `HeapSize`, `LCMapStringW`, `LoadLibraryExW`, `GetStringTypeW`, `GetFileType`, `SetStdHandle`, `GetEnvironmentVariableA`, `SetLastError`, `RemoveVectoredExceptionHandler`, `HeapAlloc`, `HeapFree`
**ADVAPI32.dll**: `RegOpenKeyExA`, `RegCloseKey`
**SHELL32.dll**: `SHGetSpecialFolderPathA`
**GDI32.dll**: `GetDeviceCaps`
**COMCTL32.dll**: `InitCommonControlsEx`

## Extracted Strings

Total strings found: **942** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
@USVWATAUAVAWH
EPbcry
ETpt.df
A_A^A]A\_^[]
@SUVWAVAWHcB<I
Z0L+E0
A;JPs(
A_A^_^][
@USVWH
ExntdlH
E|l.dlf
D$XHcG<
Ed; !
Eh;*7;
E`GayS
Edgpp]
E`NtCo
Edntinf
Ed(,9(
El$"#M
D$PNtCl
D$Tose
uxHcx
u0HcH<
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
x ATAVAWH
< t;<	t7
 A_A^A\
UVWAVAWH
H9:tH
0A_A^_^]
u3HcH<H
WAVAWH
 A_A^_
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14000a208` | `0x14000a208` | 16523 | ✓ |
| `fcn.14000a1f4` | `0x14000a1f4` | 16482 | ✓ |
| `fcn.140005150` | `0x140005150` | 3880 | ✓ |
| `fcn.14000bb94` | `0x14000bb94` | 1985 | ✓ |
| `section..text` | `0x140001000` | 1960 | ✓ |
| `fcn.140011e20` | `0x140011e20` | 1677 | ✓ |
| `fcn.140007c0c` | `0x140007c0c` | 1213 | ✓ |
| `fcn.14001028c` | `0x14001028c` | 1171 | ✓ |
| `fcn.14000f750` | `0x14000f750` | 922 | ✓ |
| `fcn.140011a60` | `0x140011a60` | 920 | ✓ |
| `fcn.14000f1e0` | `0x14000f1e0` | 920 | ✓ |
| `fcn.14000b798` | `0x14000b798` | 862 | ✓ |
| `fcn.14000fba4` | `0x14000fba4` | 817 | ✓ |
| `fcn.140010bd8` | `0x140010bd8` | 815 | ✓ |
| `fcn.14000c660` | `0x14000c660` | 712 | ✓ |
| `fcn.140006898` | `0x140006898` | 667 | ✓ |
| `fcn.140006110` | `0x140006110` | 660 | ✓ |
| `fcn.14000c2bc` | `0x14000c2bc` | 623 | ✓ |
| `fcn.14000e434` | `0x14000e434` | 604 | ✓ |
| `fcn.14000974c` | `0x14000974c` | 589 | ✓ |
| `fcn.1400080cc` | `0x1400080cc` | 584 | ✓ |
| `fcn.14000866c` | `0x14000866c` | 557 | ✓ |
| `fcn.14000d814` | `0x14000d814` | 555 | ✓ |
| `fcn.140006b40` | `0x140006b40` | 517 | ✓ |
| `fcn.14000c0c4` | `0x14000c0c4` | 501 | ✓ |
| `fcn.140007880` | `0x140007880` | 499 | ✓ |
| `fcn.140003ef0` | `0x140003ef0` | 471 | ✓ |
| `fcn.140001aa0` | `0x140001aa0` | 468 | ✓ |
| `fcn.14000bddc` | `0x14000bddc` | 462 | ✓ |
| `fcn.1400034d0` | `0x1400034d0` | 454 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001aa0.c`](code/fcn.140001aa0.c)
- [`code/fcn.1400034d0.c`](code/fcn.1400034d0.c)
- [`code/fcn.140003ef0.c`](code/fcn.140003ef0.c)
- [`code/fcn.140005150.c`](code/fcn.140005150.c)
- [`code/fcn.140006110.c`](code/fcn.140006110.c)
- [`code/fcn.140006898.c`](code/fcn.140006898.c)
- [`code/fcn.140006b40.c`](code/fcn.140006b40.c)
- [`code/fcn.140007880.c`](code/fcn.140007880.c)
- [`code/fcn.140007c0c.c`](code/fcn.140007c0c.c)
- [`code/fcn.1400080cc.c`](code/fcn.1400080cc.c)
- [`code/fcn.14000866c.c`](code/fcn.14000866c.c)
- [`code/fcn.14000974c.c`](code/fcn.14000974c.c)
- [`code/fcn.14000a1f4.c`](code/fcn.14000a1f4.c)
- [`code/fcn.14000a208.c`](code/fcn.14000a208.c)
- [`code/fcn.14000b798.c`](code/fcn.14000b798.c)
- [`code/fcn.14000bb94.c`](code/fcn.14000bb94.c)
- [`code/fcn.14000bddc.c`](code/fcn.14000bddc.c)
- [`code/fcn.14000c0c4.c`](code/fcn.14000c0c4.c)
- [`code/fcn.14000c2bc.c`](code/fcn.14000c2bc.c)
- [`code/fcn.14000c660.c`](code/fcn.14000c660.c)
- [`code/fcn.14000d814.c`](code/fcn.14000d814.c)
- [`code/fcn.14000e434.c`](code/fcn.14000e434.c)
- [`code/fcn.14000f1e0.c`](code/fcn.14000f1e0.c)
- [`code/fcn.14000f750.c`](code/fcn.14000f750.c)
- [`code/fcn.14000fba4.c`](code/fcn.14000fba4.c)
- [`code/fcn.14001028c.c`](code/fcn.14001028c.c)
- [`code/fcn.140010bd8.c`](code/fcn.140010bd8.c)
- [`code/fcn.140011a60.c`](code/fcn.140011a60.c)
- [`code/fcn.140011e20.c`](code/fcn.140011e20.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This updated analysis incorporates the additional disassembly from chunk 2/2. The new code segments provide significant evidence regarding the malware's anti-analysis techniques, environment awareness, and internal communication infrastructure.

---

### **Updated Analysis of Malicious Behavior**

#### **1. Advanced Anti-Analysis & Evasion (New Findings)**
*   **CPU Fingerprinting (fcn.140006898):** This function performs deep inspections using `cpuid` instructions (Basic Info, Version Info, and Extended Feature Enumeration). It checks for specific instruction sets (like AVX or SSE) and processor capabilities. In a malware context, this is frequently used to **detect virtual machines (VMs), emulators, or sandbox environments** that may not perfectly emulate advanced CPU features.
*   **Code Integrity/Debugger Checks (fcn.140006110):** This function acts as a "guard." It compares a memory address against a hardcoded value; if the check fails, it triggers a **Software Interrupt (`swi(0x29)`)**. This is a common technique to crash the process or crash a debugger if the code has been tampered with or is being run in an environment that modifies the instruction pointer.
*   **Environment Consistency Checks:** The repeated use of `GetEnvironmentVariableA("TEMP")` followed by strict length checks (e.g., checking for specific lengths like `0x3354` or `0xf69`) suggests the malware is verifying that it is running in a "normal" user environment and not a modified testing shell.

#### **2. Communication & Data Processing**
*   **Heartbeat Mechanism:** The terms "DataBuffer" and "Heartbeat" appear repeatedly (seen in `fcn.140003ef0` and `fcn.140001aa0`). These are often used as internal status markers to indicate that the "heartbeat" (periodic check-in) with the Command & Control (C2) server is active.
*   **Automatic Formatting:** Function `fcn.140010bd8` contains logic to handle newline conversions (`\n` to `\r\n`). This indicates that the malware processes raw data received from a remote source and formats it for local processing or display, which is common in **Remote Access Trojans (RATs)** where instructions are sent over TCP/UDP.
*   **Multi-Threaded Coordination:** The presence of `LOCK()` and `UNLOCK()` macros (in functions like `fcn.14000c2bc`) confirms that the malware is a multi-threaded application. This allows it to perform several actions simultaneously, such as maintaining a C2 connection in one thread while performing file system discovery or keylogging in others.

#### **3. Information Gathering & Reconnaissance**
*   **File System Enumeration:** The logic involving `FindFirstFileExW` and `FindNextFileW` indicates the malware scans specific directories to find other components, configuration files, or perhaps identifying recently used folders to target for data theft.
*   **System Profiling:** The use of `GetComputerNameA`, `GetSystemInfo`, and `InitCommonControlsEx` suggests the malware gathers system metadata to "fingerprint" the infected host, which is then sent back to the C2 server to identify the victim's machine uniquely.

---

### **Technical Patterns & Indicators (Updated)**

*   **Dummy Window Creation:** The code creates a window or "Static" control titled "Heartbeat" but immediately hides it or sets its text length. This is often used as a placeholder for internal status flags in memory, making the malware's internal logic look like standard Windows UI management to less-sophisticated tools.
*   **Instruction Set Awareness:** The complex math and bitwise shifts seen in `fcn.140006898` are designed to verify hardware capabilities. If a sandbox doesn't support specific high-end instructions, the malware may "stall" or exit.
*   **High Obfuscation via Dispatch Tables:** Function `fcn.14000e434` appears to be a **jump table/dispatcher**. Instead of having one long function, it uses an ID-based system to jump to different handlers. This makes "following" the logic during manual analysis significantly more difficult as the execution path is not linear.

---

### **Updated Summary**

*   **Malware Type:** Highly sophisticated Modular Loader / Remote Access Trojan (RAT).
*   **Primary Goal:** The malware is designed for long-term persistence and remote control. It utilizes a complex, multi-threaded architecture to maintain a "heartbeat" with a C2 server while employing advanced anti-VM and anti-debugging checks to evade automated sandboxes.
*   **Risk Level: Critical.** 
    The presence of CPU fingerprinting, manual thread locking for concurrent operations, and robust logic for handling remote data formatting indicates this is a professional-grade piece of malware (likely part of a botnet or targeted espionage operation).

### **Key Indicators for Hunting/Detection:**
1.  **Suspicious API Calls:** `FindFirstFileExW`, `cpuid` usage, `GetProcAddress` (indirectly via the manual dispatch table), and `WriteFile`.
2.  **Behavioral Signatures:**
    *   Creation of "DataBuffer" or "Heartbeat" strings/windows in memory.
    *   Frequent calls to environment variable checks (`TEMP`).
    *   Execution of multi-threaded loops that appear to wait for remote input.
3.  **File System Activity:** Scanning for specific filenames or looking for common user files in the `%TEMP%` directory.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Evasion | The use of `cpuid` for instruction set awareness and checks on the `TEMP` environment variables are designed to detect if the malware is running in a virtualized or analysis-heavy environment. |
| **T1435** | Anti-debug | The "guard" function (fcn.140006110) uses a software interrupt (`swi(0x29)`) to crash the process if it detects debugger presence or code tampering. |
| **T1083** | File and Directory Discovery | The use of `FindFirstFileExW` and `FindNextFileW` indicates searching the file system for configuration files, other modules, or target data. |
| **T1082** | System Information Discovery | The utilization of `GetComputerNameA` and `GetSystemInfo` is used to gather host-specific metadata (fingerprinting) to be sent back to the C2 server. |
| **T1071** | Application Layer Protocol | The "Heartbeat" mechanism and the conversion of newline characters (`\n` to `\r\n`) indicate a formalized protocol for processing instructions received from a remote source. |
| **T1027** | Obfuscated Files or Information | The use of a jump table/dispatch table (fcn.14000e434) is designed to hide the linear execution flow, making manual reverse engineering and analysis more difficult. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

**File paths / Registry keys**
*   *(None specific; common environment variables like "TEMP" were noted but are not unique identifiers.)*

**Mutex names / Named pipes**
*   `Global\Svc_%d` (Note: This appears to be a naming convention for inter-process communication or named objects).

**Hashes**
*   *(None provided in the text)*

**Other artifacts**
*   **Internal Strings/Keywords:** 
    *   `DataBuffer` (Used as an internal memory/buffer identifier)
    *   `Heartbeat` (Related to C2 check-in timing)
*   **C2 Communication Patterns:** 
    *   Conversion of `\n` to `\r\n` (Indicates handling of raw data from a remote source).
    *   "Heartbeat" mechanism for periodic communication.
*   **Anti-Analysis/Evasion Indicators:**
    *   `cpuid` instruction usage for CPU fingerprinting and VM detection.
    *   Software Interrupt `swi(0x29)` (Used as a trap or crash point for debuggers).
    *   Environment variable length validation on the `%TEMP%` path to detect non-standard shells.
*   **Behavioral Signatures:**
    *   Use of multi-threaded locks (`LOCK()` / `UNLOCK()`) for concurrent task execution.
    *   System profiling via `GetComputerNameA`, `GetSystemInfo`, and `InitCommonControlsEx`.
    *   File system enumeration using `FindFirstFileExW` and `FindNextFileW`.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1. **Malware family:** Unknown (Potential custom build or sophisticated framework)
2. **Malware type:** RAT (Remote Access Trojan) / Backdoor
3. **Confidence:** High (for type) / Medium (for family)
4. **Key evidence:**
    *   **Command & Control Architecture:** The presence of a "Heartbeat" mechanism, multi-threaded execution for concurrent tasks, and the conversion of remote data characters (`\n` to `\r\n`) are definitive indicators of a Remote Access Trojan designed to maintain a persistent connection with a C2 server.
    *   **Advanced Evasion Techniques:** The use of `cpuid` for hardware/VM fingerprinting, "guard" functions using software interrupts (`swi(0x29)`), and the implementation of jump tables/dispatchers indicate a high level of sophistication intended to bypass automated sandboxes and manual analysis.
    *   **System Reconnaissance:** The combination of file system enumeration (`FindFirstFileExW`) and system profiling (`GetComputerNameA`, `GetSystemInfo`) is consistent with malware designed for long-term persistence, information gathering, and establishing a unique identity for an infected host within a botnet or targeted operation.
