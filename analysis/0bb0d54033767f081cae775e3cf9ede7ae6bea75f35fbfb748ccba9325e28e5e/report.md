# Threat Analysis Report

**Generated:** 2026-07-27 14:57 UTC
**Sample:** `0bb0d54033767f081cae775e3cf9ede7ae6bea75f35fbfb748ccba9325e28e5e_0bb0d54033767f081cae775e3cf9ede7ae6bea75f35fbfb748ccba9325e28e5e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0bb0d54033767f081cae775e3cf9ede7ae6bea75f35fbfb748ccba9325e28e5e_0bb0d54033767f081cae775e3cf9ede7ae6bea75f35fbfb748ccba9325e28e5e.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 5 sections |
| Size | 574,464 bytes |
| MD5 | `859c4b85ed85e6cc4eadb1a037a61e16` |
| SHA1 | `da1c3e92f69e6ca0e4f4823525905cb6969a44ad` |
| SHA256 | `0bb0d54033767f081cae775e3cf9ede7ae6bea75f35fbfb748ccba9325e28e5e` |
| Overall entropy | 7.742 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769155939 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 61,440 | 6.462 | No |
| `.rdata` | 41,472 | 4.651 | No |
| `.data` | 463,872 | 7.894 | ⚠️ Yes |
| `.pdata` | 4,608 | 4.722 | No |
| `.reloc` | 2,048 | 4.924 | No |

### Imports

**KERNEL32.dll**: `WriteFile`, `CloseHandle`, `GetLastError`, `ReleaseMutex`, `WaitForSingleObject`, `GetFileAttributesW`, `CreateProcessW`, `VirtualAlloc`, `VirtualFree`, `lstrcpyW`, `lstrlenW`, `WriteConsoleW`, `CreateFileW`, `CreateDirectoryW`, `CreateMutexA`
**ADVAPI32.dll**: `RegCreateKeyExW`, `RegCloseKey`, `RegSetValueExW`

### Exports

`UIClassRegister`, `hXts`

## Extracted Strings

Total strings found: **5260** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.reloc
UWATAVAWH
A_A^A\_]
UATAVH
uxHcl
|$ AVH
WATAUAVAWH
A_A^A]A\_
WATAUAVAWH
 A_A^A]A\_
VWATAVAWH
 A_A^A\_^
WATAUAVAWH
A_A^A]A\_
H;XXs
H;xXu5
AUAVAWH
9;|
HcC
u4I9}(
;I9}(tiH
0A_A^A]
UVWATAUAVAWH
`A_A^A]A\_^]
@USVWATAUAVAWH
K0HcQD
C0Hc	H
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
@SVWATAUAVAWH
L!|$(L!
D$0HcH
pA_A^A]A\_^[
A9	uaA
B(I9A(u
A9	u3A
SVWATAUAVAWH
0A_A^A]A\_^[
t$ WATAUAVAWH
E0Lc`I
E0HcHD
 A_A^A]A\_
D$0uH
D$0@8{
f9
t	H
f9
tvH
f9
t	H
t98t H
u3HcH<H
WATAUAVAWH
< t=<	t9
 A_A^A]A\_
UVWAVAWH
H9:tH
0A_A^_^]
WAVAWH
 A_A^_
WAVAWH
L3
H3B
 A_A^_
p0R^G'
u$D8r(tH
D81uUL9r
uED8r(tH
vAD8s(tH
u$D8r(tH
fD91uTL9r
uED8r(tH
v@D8s(tH
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
WATAUAVAWH
 A_A^A]A\_
p0R^G'
fD9t$b
t$ WATAUAVAWH
D!|$xA
A_A^A]A\_
L$ VWAVH
fD94H}aD
KHH;x
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180002348` | `0x180002348` | 15125 | ✓ |
| `fcn.180006c90` | `0x180006c90` | 12846 | ✓ |
| `fcn.180006c58` | `0x180006c58` | 12832 | ✓ |
| `fcn.1800023d8` | `0x1800023d8` | 3392 | ✓ |
| `fcn.180008568` | `0x180008568` | 1977 | ✓ |
| `fcn.180002278` | `0x180002278` | 1817 | ✓ |
| `fcn.18000f0d0` | `0x18000f0d0` | 1661 | ✓ |
| `fcn.180002e84` | `0x180002e84` | 1594 | ✓ |
| `fcn.1800044cc` | `0x1800044cc` | 1231 | ✓ |
| `fcn.18000c578` | `0x18000c578` | 1141 | ✓ |
| `fcn.18000b1f0` | `0x18000b1f0` | 1038 | ✓ |
| `fcn.18000b790` | `0x18000b790` | 937 | ✓ |
| `fcn.18000f770` | `0x18000f770` | 920 | ✓ |
| `fcn.18000817c` | `0x18000817c` | 845 | ✓ |
| `fcn.18000bbf4` | `0x18000bbf4` | 817 | ✓ |
| `fcn.18000cea0` | `0x18000cea0` | 774 | ✓ |
| `fcn.180002994` | `0x180002994` | 714 | ✓ |
| `fcn.180001918` | `0x180001918` | 701 | ✓ |
| `fcn.180009024` | `0x180009024` | 701 | ✓ |
| `fcn.180009f58` | `0x180009f58` | 633 | ✓ |
| `fcn.18000159c` | `0x18000159c` | 627 | ✓ |
| `fcn.180008c80` | `0x180008c80` | 623 | ✓ |
| `fcn.18000499c` | `0x18000499c` | 621 | ✓ |
| `fcn.18000e708` | `0x18000e708` | 614 | ✓ |
| `fcn.180006714` | `0x180006714` | 585 | ✓ |
| `fcn.180004f84` | `0x180004f84` | 573 | ✓ |
| `fcn.18000a98c` | `0x18000a98c` | 555 | ✓ |
| `fcn.180003118` | `0x180003118` | 535 | ✓ |
| `fcn.180004138` | `0x180004138` | 511 | ✓ |
| `fcn.180008a98` | `0x180008a98` | 487 | ✓ |

### Decompiled Code Files

- [`code/fcn.18000159c.c`](code/fcn.18000159c.c)
- [`code/fcn.180001918.c`](code/fcn.180001918.c)
- [`code/fcn.180002278.c`](code/fcn.180002278.c)
- [`code/fcn.180002348.c`](code/fcn.180002348.c)
- [`code/fcn.1800023d8.c`](code/fcn.1800023d8.c)
- [`code/fcn.180002994.c`](code/fcn.180002994.c)
- [`code/fcn.180002e84.c`](code/fcn.180002e84.c)
- [`code/fcn.180003118.c`](code/fcn.180003118.c)
- [`code/fcn.180004138.c`](code/fcn.180004138.c)
- [`code/fcn.1800044cc.c`](code/fcn.1800044cc.c)
- [`code/fcn.18000499c.c`](code/fcn.18000499c.c)
- [`code/fcn.180004f84.c`](code/fcn.180004f84.c)
- [`code/fcn.180006714.c`](code/fcn.180006714.c)
- [`code/fcn.180006c58.c`](code/fcn.180006c58.c)
- [`code/fcn.180006c90.c`](code/fcn.180006c90.c)
- [`code/fcn.18000817c.c`](code/fcn.18000817c.c)
- [`code/fcn.180008568.c`](code/fcn.180008568.c)
- [`code/fcn.180008a98.c`](code/fcn.180008a98.c)
- [`code/fcn.180008c80.c`](code/fcn.180008c80.c)
- [`code/fcn.180009024.c`](code/fcn.180009024.c)
- [`code/fcn.180009f58.c`](code/fcn.180009f58.c)
- [`code/fcn.18000a98c.c`](code/fcn.18000a98c.c)
- [`code/fcn.18000b1f0.c`](code/fcn.18000b1f0.c)
- [`code/fcn.18000b790.c`](code/fcn.18000b790.c)
- [`code/fcn.18000bbf4.c`](code/fcn.18000bbf4.c)
- [`code/fcn.18000c578.c`](code/fcn.18000c578.c)
- [`code/fcn.18000cea0.c`](code/fcn.18000cea0.c)
- [`code/fcn.18000e708.c`](code/fcn.18000e708.c)
- [`code/fcn.18000f0d0.c`](code/fcn.18000f0d0.c)
- [`code/fcn.18000f770.c`](code/fcn.18000f770.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated the analysis. The new code confirms several sophisticated techniques used to obfuscate behavior, decrypt payloads, and bypass security controls.

---

# Updated Malware Analysis Report (Combined)

## Core Functionality
The binary continues to exhibit characteristics of a **sophisticated loader or a multi-stage Trojan**. It uses a "layered" approach where the primary executable acts as a wrapper for more complex, hidden logic.

*   **Multi-Stage Decoding/Deobfuscation:** 
    *   Function `18000159c` contains a classic **XOR-decryption loop** (`^ 0x43`). This is used to process and "unpack" data in memory before it is utilized or written to disk.
    *   The code frequently processes blocks of memory (e.g., `0x47`, `0x200` bytes) using repeated loops, which indicates the processing of encrypted configuration files or secondary executable payloads.
*   **Script/Instruction Interpreter:** As noted previously, the use of large switch-case tables and indirect jumps suggests an internal "virtual machine" (VM) architecture. This allows the malware to execute complex logic while keeping its true intent hidden from simple static analysis.
*   **System Interaction & Persistence:** 
    *   The code makes explicit calls to `CreateFileW` and `WriteFile`. This confirms that the loader can drop files or modify existing ones on the system.
    *   The integration of `VirtualFree` following a write operation suggests it is cleaning up its temporary buffers after extracting an executable payload from memory.

## Suspicious and Malicious Behaviors
The second chunk of code introduces more aggressive anti-analysis and evasion tactics:

*   **Sophisticated Exception Manipulation:**
    *   Function `18000e708` constructs a complex structure for the **`RaiseException`** system call. It uses extensive bitwise operations (shifts, ANDs, ORs) to manipulate flags before triggering an exception. 
    *   **Security Implication:** This is often used in "exception-based" execution. By intentionally throwing an exception and catching it internally, the malware can jump to different sections of code based on how the environment handles that specific error—a technique designed to crash or confuse standard debuggers and sandboxes.
*   **Advanced Environment Validation (Guard Rails):**
    *   Several functions (e.g., `180004f84`) contain checks against "magic" constants (like `-0x1f928c9d`). 
    *   **Security Implication:** These are not standard values. They act as "gates." If the malware detects a debugger, an emulator, or a non-target OS version, it will simply stop executing or follow a "dead" code path to hide its true behavior from analysts.
*   **Data Transformation & Obfuscation:** 
    *   Function `180008a98` shows complex bit manipulation over large buffers (e.g., `0x100` iterations). This suggests it is decoding a specialized data structure, possibly a configuration block that tells the malware which targets to infect or which C2 servers to contact.
    *   **Encoding Awareness:** The calls to `GetCPInfo` and related logic suggest the malware is designed to be "portable," ensuring it can decode its own strings regardless of the victim's regional language settings (locales).

## Notable Techniques and Patterns
*   **In-Memory Payload Reconstruction:** The sequence of `VirtualAlloc` $\rightarrow$ XOR Decoding $\rightarrow$ `WriteFile` $\rightarrow$ `VirtualFree` is a textbook "Dropper" pattern. It decodes a payload in memory, writes it to the filesystem (or a hidden location), and then wipes its tracks from RAM.
*   **Control Flow Flattening:** The heavy use of switch tables and indirect jumps makes it extremely difficult for an analyst to follow the logic linearly. The malware isn't just "hiding" a string; it is hiding its entire execution path.
*   **Dynamic State Management:** Functions like `180008c80` manage internal state counters and memory offsets, ensuring that even if the analysis of one function is halted, the overall logic remains consistent during execution.

## Summary Table of Indicators

| Feature | Observation | Potential Risk |
| :--- | :--- | :--- |
| **Decryption Logic** | XOR-based loops (`^ 0x43`) and nested bitwise manipulations. | Hides encrypted payloads, C2 commands, or malicious scripts from static scanners. |
| **Anti-Analysis** | "Magic" constants (e.g., `-0x1f928c9d`) and `RaiseException` manipulation. | Designed to crash debuggers, evade sandboxes, and detect analysis environments. |
| **Execution Model** | Switch-case dispatching/Interpreter logic. | Hides malicious intent behind a "virtual" layer of code (VM obfuscation). |
| **Persistence/Dropper** | `CreateFileW`, `WriteFile`, and `VirtualFree` workflows. | Used to drop secondary malware components or persistent backdoors onto the host disk. |
| **Robust Encoding** | Interaction with `GetCPInfo`. | Ensures consistent execution across different locales, common in global malware campaigns. |

### Final Conclusion
This binary is a **highly sophisticated loader**. It employs multiple layers of obfuscation (VM-like interpreter, XOR decryption, and exception-based evasion) to hide its true purpose. Its primary role is likely to act as a "gatekeeper," checking the environment for security tools before decrypting and dropping the final malicious payload onto the host system.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of XOR-decryption loops and complex bit manipulation is used to hide configuration data and malicious payloads from static analysis. |
| **T1027** | Obfuscated Files or Information (Control Flow) | The implementation of a custom VM architecture with switch-case tables and control flow flattening hides the execution logic and intended path of the malware. |
| **T1483** | Environment Keying | The use of "magic" constants as guard rails to detect debuggers, emulators, or non-target systems prevents analysis by switching to a "dead" code path. |
| **T1027** | Obfuscated Files or Information (Loader) | The multi-stage decoding and memory-buffer management (VirtualAlloc/WriteFile) act as an obfuscation layer for the final malicious payload before it is written to disk. |
| **T1483** | Environment Keying | The use of complex `RaiseException` logic serves as a check against debugger presence, allowing the malware to sense and evade analysis tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Strings" section contained largely obfuscated data, compiler artifacts (e.g., `__stdcall`, `.rdata`), and common library identifiers which were excluded as false positives.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The analysis mentions the use of `CreateFileW` and `WriteFile`, but no specific file paths or registry keys were disclosed in the provided text.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (Note: While memory addresses such as `18000159c` were mentioned, these are internal offsets and not file/string hashes.)

### **Other artifacts**
*   **XOR Decryption Key:** `0x43` (Used in the decryption loop to unpack data in memory).
*   **Anti-Analysis "Magic" Constant:** `-0x1f928c9d` (Identified as a guard rail/gate used to detect debuggers or non-target environments).
*   **C2/Payload Loader Patterns:** 
    *   The sequence `VirtualAlloc` $\rightarrow$ XOR Decoding $\rightarrow$ `WriteFile` $\rightarrow$ `VirtualFree` (Classic Dropper behavior).
    *   Use of `RaiseException` with manipulated bitwise flags for anti-debugging.
    *   Usage of `GetCPInfo` to ensure consistent string decoding across different locales.
*   **Control Flow Obfuscation:** Extensive use of switch-case tables and indirect jumps (Virtual Machine/Interpreter architecture).

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1.  **Malware family**: custom
2.  **Malware type**: loader
3.  **Confidence**: High
4.  **Key evidence**:
    *   **Dropper/Loader Behavior:** The execution flow follows a classic "loader" pattern: `VirtualAlloc` $\rightarrow$ XOR decoding (key `0x43`) $\rightarrow$ `WriteFile` $\rightarrow$ `VirtualFree`. This confirms its primary role is to decrypt and deploy a secondary payload while cleaning up its own memory traces.
    *   **Sophisticated Evasion Techniques:** The use of "magic" constants (`-0x1f928c9d`) as environment guards and complex `RaiseException` manipulation indicates a high level of intent to bypass automated sandboxes and manual debugging tools.
    *   **Advanced Obfuscation:** The implementation of a VM-like interpreter architecture (switch-case tables and indirect jumps) is a signature of sophisticated, custom-developed malware designed to hide its true functionality from static analysis.
