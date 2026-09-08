# Threat Analysis Report

**Generated:** 2026-09-05 06:07 UTC
**Sample:** `1447b57a09a8759ab98c8958b655ed082388bf562261477664f9e90ce87ac2a9_1447b57a09a8759ab98c8958b655ed082388bf562261477664f9e90ce87ac2a9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1447b57a09a8759ab98c8958b655ed082388bf562261477664f9e90ce87ac2a9_1447b57a09a8759ab98c8958b655ed082388bf562261477664f9e90ce87ac2a9.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 1,023,488 bytes |
| MD5 | `c490659944e7a0e96cc158692c6b0d77` |
| SHA1 | `3802ab2c84fcb57e1314f2aebdc0f63e65adbbdf` |
| SHA256 | `1447b57a09a8759ab98c8958b655ed082388bf562261477664f9e90ce87ac2a9` |
| Overall entropy | 7.452 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774106291 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 82,432 | 6.493 | No |
| `.rdata` | 50,688 | 4.77 | No |
| `.data` | 881,152 | 7.597 | ⚠️ Yes |
| `.pdata` | 5,120 | 4.77 | No |
| `_RDATA` | 512 | 1.944 | No |
| `.rsrc` | 512 | 4.772 | No |
| `.reloc` | 2,048 | 5.274 | No |

### Imports

**KERNEL32.dll**: `VirtualProtect`, `GetCurrentProcess`, `VirtualAlloc`, `EnumCalendarInfoA`, `GetLastError`, `LoadLibraryA`, `GetProcAddress`, `SetFilePointer`, `SetEndOfFile`, `UnmapViewOfFile`, `Sleep`, `CreateFileA`, `GetDiskFreeSpaceExW`, `QueryPerformanceFrequency`, `CloseHandle`
**USER32.dll**: `wsprintfW`
**ole32.dll**: `StringFromGUID2`, `CoCreateGuid`
**RPCRT4.dll**: `RpcStringFreeW`, `NdrClientCall3`, `RpcBindingFromStringBindingW`, `RpcExceptionFilter`, `RpcStringBindingComposeW`, `RpcBindingFree`

## Extracted Strings

Total strings found: **2964** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@_RDATA
@.rsrc
@.reloc
L$ SVWH
L$ SVWH
L$ SUVWAVH
@A^_^][
@SVWAVH
uxHcT
 H3E H3E
u0HcH<H
T$uPH
WATAUAVAWH
A_A^A]A\_
WATAUAVAWH
 A_A^A]A\_
ffffff
fffffff
@USVWATAVAWH
D8d$XtH
A_A^A\_^[]
D8t$8tH
D8t$8tH
D$@H;G
|$ AVH
D$0H;G
 t(<#t
<-t
<0uG
 t(<#t
<-t
<0u>
<htl<jt\<lt4<tt$<wt
<htl<jt\<lt4<tt$<wt
t$ WAVAWH
<Ct-<D
<StW@:
<g~{<itd<ntY<ot7<pt
<utT@:
D<P0@:
k4+kP+
0A_A^_
t$ WAVAWH
<Ct-<D
<StW@:
<g~{<itd<ntY<ot7<pt
<utT@:
D<P0@:
k(+sPL
0A_A^_
VWAUAVAWH
s4+sP+
A_A^A]_^
yBgt	3
x ATAVAWH
 A_A^A\
x ATAVAWH
 A_A^A\
WATAWH
0A_A\_
t98tH
x ATAVAWH
< t=<	t9
 A_A^A\
UVWAVAWH
H9:tH
0A_A^_^]
WAVAWH
0A_A^_
	H;^-
u3HcH<H
t$ WAVAWH
 A_A^_
WAVAWH
 A_A^_
x AUAVAWH
@A_A^A]
VWATAVAWH
?D8d$8tH
D8d$8tH
t'D8d$8tH
%D8d$8tH
A_A^A\_^
WATAUAVAWH
 A_A^A]A\_
L$ VWAVH
fD9t$b
@8l$HtH
L$ UVWH
f9
t	H

fA9	t	I
f9
t	H
f9
t	H
WATAUAVAWH
gfffffffH
D8t$htH
A_A^A]A\_
x ATAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140008934` | `0x140008934` | 24876 | ✓ |
| `fcn.140008920` | `0x140008920` | 24836 | ✓ |
| `fcn.14000c174` | `0x14000c174` | 23299 | ✓ |
| `fcn.140011964` | `0x140011964` | 8145 | ✓ |
| `fcn.14001069c` | `0x14001069c` | 4670 | ✓ |
| `fcn.1400132bc` | `0x1400132bc` | 4321 | ✓ |
| `fcn.14000ccac` | `0x14000ccac` | 1705 | ✓ |
| `fcn.140008d50` | `0x140008d50` | 1701 | ✓ |
| `fcn.1400037d0` | `0x1400037d0` | 1685 | ✓ |
| `fcn.140013380` | `0x140013380` | 1451 | ✓ |
| `fcn.14000f1fc` | `0x14000f1fc` | 1260 | ✓ |
| `fcn.140010270` | `0x140010270` | 1065 | ✓ |
| `fcn.1400122c0` | `0x1400122c0` | 949 | ✓ |
| `fcn.140011da0` | `0x140011da0` | 925 | ✓ |
| `fcn.140001b90` | `0x140001b90` | 914 | ✓ |
| `fcn.14000b288` | `0x14000b288` | 896 | ✓ |
| `fcn.14000bc94` | `0x14000bc94` | 828 | ✓ |
| `fcn.140001070` | `0x140001070` | 821 | ✓ |
| `fcn.140012724` | `0x140012724` | 789 | ✓ |
| `fcn.14000c99c` | `0x14000c99c` | 782 | ✓ |
| `fcn.140008a4c` | `0x140008a4c` | 770 | ✓ |
| `fcn.14000fb64` | `0x14000fb64` | 739 | ✓ |
| `fcn.140005f60` | `0x140005f60` | 733 | ✓ |
| `fcn.140013e70` | `0x140013e70` | 710 | ✓ |
| `fcn.14000d68c` | `0x14000d68c` | 697 | ✓ |
| `fcn.140005a74` | `0x140005a74` | 644 | ✓ |
| `fcn.1400018f0` | `0x1400018f0` | 642 | ✓ |
| `fcn.140005158` | `0x140005158` | 630 | ✓ |
| `fcn.14000eb64` | `0x14000eb64` | 618 | ✓ |
| `fcn.140005cf8` | `0x140005cf8` | 614 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001070.c`](code/fcn.140001070.c)
- [`code/fcn.1400018f0.c`](code/fcn.1400018f0.c)
- [`code/fcn.140001b90.c`](code/fcn.140001b90.c)
- [`code/fcn.1400037d0.c`](code/fcn.1400037d0.c)
- [`code/fcn.140005158.c`](code/fcn.140005158.c)
- [`code/fcn.140005a74.c`](code/fcn.140005a74.c)
- [`code/fcn.140005cf8.c`](code/fcn.140005cf8.c)
- [`code/fcn.140005f60.c`](code/fcn.140005f60.c)
- [`code/fcn.140008920.c`](code/fcn.140008920.c)
- [`code/fcn.140008934.c`](code/fcn.140008934.c)
- [`code/fcn.140008a4c.c`](code/fcn.140008a4c.c)
- [`code/fcn.140008d50.c`](code/fcn.140008d50.c)
- [`code/fcn.14000b288.c`](code/fcn.14000b288.c)
- [`code/fcn.14000bc94.c`](code/fcn.14000bc94.c)
- [`code/fcn.14000c174.c`](code/fcn.14000c174.c)
- [`code/fcn.14000c99c.c`](code/fcn.14000c99c.c)
- [`code/fcn.14000ccac.c`](code/fcn.14000ccac.c)
- [`code/fcn.14000d68c.c`](code/fcn.14000d68c.c)
- [`code/fcn.14000eb64.c`](code/fcn.14000eb64.c)
- [`code/fcn.14000f1fc.c`](code/fcn.14000f1fc.c)
- [`code/fcn.14000fb64.c`](code/fcn.14000fb64.c)
- [`code/fcn.140010270.c`](code/fcn.140010270.c)
- [`code/fcn.14001069c.c`](code/fcn.14001069c.c)
- [`code/fcn.140011964.c`](code/fcn.140011964.c)
- [`code/fcn.140011da0.c`](code/fcn.140011da0.c)
- [`code/fcn.1400122c0.c`](code/fcn.1400122c0.c)
- [`code/fcn.140012724.c`](code/fcn.140012724.c)
- [`code/fcn.1400132bc.c`](code/fcn.1400132bc.c)
- [`code/fcn.140013380.c`](code/fcn.140013380.c)
- [`code/fcn.140013e70.c`](code/fcn.140013e70.c)

## Behavioral Analysis

This updated analysis incorporates the newly provided disassembly (chunk 2/2), which confirms several high-level indicators of a sophisticated, multi-stage packer and injector.

### Updated Analysis Summary

#### Core Functionality and Purpose
The sample is confirmed to be a **highly complex packer using a Virtual Machine (VM) based architecture** or a similar custom interpreter. While the first chunk suggested a loader/packer, this second section reveals the specific techniques used:
1.  **Instruction Interpretation:** The extensive use of switch tables and state-dependent branching suggests that the "actual" malicious payload is likely stored as **custom bytecode**. The binary acts as an interpreter for this bytecode (a common high-tier obfuscation technique).
2.  **In-Memory Decryption & Injection:** The presence of `VirtualProtect`, `VirtualAlloc`, and manual decryption loops indicates that the malware does not just "unpack" a file to disk; it deciphers code into memory and prepares it for execution (Process Hollowing or Reflective Loading).

#### Suspicious or Malicious Behaviors
*   **Advanced Memory Manipulation:** 
    *   The function `fcn.140001070` is a critical piece of evidence. It utilizes `VirtualAlloc` to carve out memory regions and `VirtualProtect` to change permissions (likely making a decrypted, non-executable buffer executable). This is the standard procedure for injecting code into the current or another process's address space.
*   **Complex Decryption Loops:** 
    *   In `fcn.140001070`, there is an elaborate loop involving XOR-like operations and "rolling" key logic (`uVar15 = *(uVar16 % 0xb + ...)`). This is used to decrypt the hidden payload in memory, ensuring that a static scan of the file cannot see the final malicious code.
*   **Dynamic API Resolution & Hidden Functionality:** 
    *   The sample uses `GetProcAddress` for functions like `VirtualProtect` and others within the `fcn.140001b90` block. This hides the true capabilities of the malware from basic static analysis tools that look for standard Import Address Table (IAT) entries.
*   **File System Enumeration:** 
    *   The function `fcn.14000c99c` interacts with `FindFirstFileExW` and `FindNextFileW`. This is used to scan the local filesystem, likely searching for specific files or targets (e.g., looking for specific user documents, other executables, or checking if certain "protector" files are present).
*   **Advanced Code Obfuscation:** 
    *   The large `switch` tables and multi-layered jump logic (seen in both chunks) are designed to break the "control flow graph" (CFG). This makes it extremely difficult for a human analyst or an automated tool to follow the execution path without running the code in a debugger.

#### Notable Techniques & Patterns
*   **VM-Style Architecture:** The structure of `fcn.14000bc94` acts as a "dispatcher." It takes a command/byte, determines what it means through several nested logic checks, and jumps to the corresponding routine. This is characteristic of sophisticated malware (like *Emotet* or various *PlugX* variants) designed to hide their core logic behind a layer of interpretation.
*   **Payload "Staging":** The behavior in `fcn.140001070` suggests the code handles multiple stages. It may unpack one piece of code (a stub), which then performs further decryption or network communication before finally executing the main payload.
*   **Anti-Analysis/Evasion:** The use of "junk" floating-point math and complex, useless branching isn't just a hurdle for human analysts; it is designed to frustrate automated symbolic execution tools (like *Angr*) which struggle with complex mathematical paths.

---

### Updated Summary for Security Operations

*   **Type:** **Advanced VM-Loader / Multi-stage Injector.**
*   **Sophistication Level:** High. The use of a custom interpreter and memory-resident decryption points to a professional malware developer or a high-end "malware-as-a-service" (MaaS) toolkit.
*   **Indicators of Compromise (IoCs):**
    *   **Process Behavior:** Monitor for processes that call `VirtualAlloc` followed immediately by `VirtualProtect` on memory regions they just allocated (especially those with `PAGE_EXECUTE_READWRITE` permissions).
    *   **Memory Patterns:** Look for "hidden" or "floating" code in memory—segments of executable code that do not have a corresponding file mapping on disk.
    *   **File System Activity:** Watch for the process enumerating files via `FindFirstFileExW` in common directories like `%APPDATA%`, `%TEMP%`, and public folders.
*   **Detection Strategy:** 
    *   **Static Analysis:** Detection of complex switch-case "dispatch" tables (over 100 cases) or nested logic used to interpret bytecode is a high-confidence indicator of a VM packer.
    *   **Dynamic Analysis:** Use memory forensic tools (e.g., *Volatility*, *Mon_Scan*) to inspect the process's memory for decrypted payloads after it has run for several seconds. Look for "unbacked" executable memory segments.
    *   **Behavioral Detection:** Flag any executable that performs heavy floating-point math in loops and then proceeds to modify its own memory permissions or perform network activity.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Obfuscated Files or Information | The use of a custom VM-based architecture, bytecode interpretation, and "junk" math is designed to hide logic from static analysis and thwart symbolic execution tools. |
| **T1055** | Process Injection | The combination of `VirtualAlloc` and `VirtualProtect` to prepare memory regions for executing decrypted code indicates standard techniques used for in-memory unpacking or injection. |
| **T1083** | File and Directory Discovery | The utilization of `FindFirstFileExW` and `FindNextFileW` shows the malware is searching the filesystem for specific files or potential targets. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Because this sample is heavily obfuscated with a VM-based architecture, traditional "atomic" indicators (like specific IPs or file paths) are absent from the raw strings. The available IOCs are primarily **behavioral signatures** and **TTP-based artifacts**.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: While `%APPDATA%` and `%TEMP%` were mentioned in the analysis, these are standard system variables and not unique IOCs).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Memory Manipulation Patterns:** Execution of `VirtualAlloc` followed by `VirtualProtect` (specifically to transition memory to `PAGE_EXECUTE_READWRITE`).
*   **Dynamic API Resolution:** Use of `GetProcAddress` to resolve and call functions like `VirtualProtect` to hide the Import Address Table (IAT).
*   **VM-Style Architecture:** Detection of a "dispatcher" routine (`fcn.14000bc94`) utilizing large switch tables (100+ cases) to interpret custom bytecode.
*   **Encryption/Decoding Logic:** Presence of "rolling key" logic and XOR operations in `fcn.140001070` used for in-memory payload decryption.
*   **Anti-Analysis Techniques:** Inclusion of "junk" floating-point math and complex, non-functional branching designed to frustrate automated symbolic execution tools.
*   **File System Reconnaissance:** Utilization of `FindFirstFileExW` and `FindNextFileW` to scan the local filesystem for targets or environment checks.

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification of the sample:

1.  **Malware family**: Unknown
2.  **Malware type**: Loader / Packer
3.  **Confidence**: High (for type; Low for specific family identification)
4.  **Key evidence**:
    *   **VM-Based Architecture:** The use of large switch tables and a custom interpreter to execute bytecode is a high-tier obfuscation technique used to hide the primary payload's logic from static analysis.
    *   **In-Memory Execution & Decryption:** The combination of `VirtualAlloc`, `VirtualProtect`, and "rolling key" XOR loops indicates that the sample is designed to decrypt and inject code directly into memory (Reflective Loading/Process Hollowing) rather than executing a plain file on disk.
    *   **Advanced Anti-Analysis:** The implementation of dynamic API resolution (`GetProcAddress`) and "junk" floating-point math confirms it is designed to evade both standard signature-based scanners and automated symbolic execution tools.
