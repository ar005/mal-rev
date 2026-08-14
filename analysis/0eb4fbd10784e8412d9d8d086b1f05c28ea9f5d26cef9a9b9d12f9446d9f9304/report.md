# Threat Analysis Report

**Generated:** 2026-08-13 20:11 UTC
**Sample:** `0eb4fbd10784e8412d9d8d086b1f05c28ea9f5d26cef9a9b9d12f9446d9f9304_0eb4fbd10784e8412d9d8d086b1f05c28ea9f5d26cef9a9b9d12f9446d9f9304.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0eb4fbd10784e8412d9d8d086b1f05c28ea9f5d26cef9a9b9d12f9446d9f9304_0eb4fbd10784e8412d9d8d086b1f05c28ea9f5d26cef9a9b9d12f9446d9f9304.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 5 sections |
| Size | 1,480,192 bytes |
| MD5 | `dc303c158d64ba00cd7db4290d72db72` |
| SHA1 | `e47d472f2fcdf26cfde7f032786050e82c217026` |
| SHA256 | `0eb4fbd10784e8412d9d8d086b1f05c28ea9f5d26cef9a9b9d12f9446d9f9304` |
| Overall entropy | 7.969 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767499745 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,396,224 | 8.0 | ⚠️ Yes |
| `.rdata` | 43,008 | 4.892 | No |
| `.data` | 7,680 | 7.981 | ⚠️ Yes |
| `.pdata` | 7,168 | 7.977 | ⚠️ Yes |
| `.rsrc` | 25,088 | 6.318 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `HeapAlloc`, `HeapFree`, `GetProcessHeap`, `Sleep`, `ExitProcess`, `GetTickCount`, `GetModuleFileNameW`, `GetProcAddress`, `LoadLibraryA`, `lstrcmpiW`, `CreateToolhelp32Snapshot`, `Process32FirstW`, `Process32NextW`, `DuplicateHandle`
**USER32.dll**: `GetMessageW`, `TranslateMessage`, `DispatchMessageW`

## Extracted Strings

Total strings found: **3328** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
ddreHcH<f
D$P9D$
` UAVAWH
0A_A^]
|$ UAVAWH
0A_A^]
H7c$}EJ4a
I8d%~FK5b
1 Lf.3
D3_ yAF0]
E4`!zBG1^
F5a"{CH2_
G6b#|DI3`
H7c$}EJ4a
I8d%~FK5b
1 Lf.3
D3_ yAF0]
E4`!zBG1^
F5a"{CH2_
G6b#|DI3`
H7c$}EJ4a
I8d%~FK5b
1 Lf.3
D3_ yAF0]
E4`!zBG1^
F5a"{CH2_
G6b#|DI3`
H7c$}EJ4a
I8d%~FK5b
1 Lf.3
D3_ yAF0]
E4`!zBG1^
F5a"{CH2_
G6b#|DI3`
H7c$}EJ4a
I8d%~FK5b
1 Lf.3
D3_ yAF0]
E4`!zBG1^
F5a"{CH2_
G6b#|DI3`
H7c$}EJ4a
I8d%~FK5b
1 Lf.3
D3_ yAF0]
E4`!zBG1^
F5a"{CH2_
G6b#|DI3`
H7c$}EJ4a
I8d%~FK5b
1 Lf.3
D3_ yAF0]
E4`!zBG1^
F5a"{CH2_
G6b#|DI3`
H7c$}EJ4a
I8d%~FK5b
1 Lf.3
D3_ yAF0]
E4`!zBG1^
F5a"{CH2_
G6b#|DI3`
H7c$}EJ4a
I8d%~FK5b
1 Lf.3
D3_ yAF0]
E4`!zBG1^
F5a"{CH2_
G6b#|DI3`
H7c$}EJ4a
I8d%~FK5b
1 Lf.3
D3_ yAF0]
E4`!zBG1^
F5a"{CH2_
G6b#|DI3`
H7c$}EJ4a
I8d%~FK5b
1 Lf.3
D3_ yAF0]
E4`!zBG1^
F5a"{CH2_
G6b#|DI3`
H7c$}EJ4a
I8d%~FK5b
1 Lf.3
D3_ yAF0]
E4`!zBG1^
F5a"{CH2_
G6b#|DI3`
H7c$}EJ4a
I8d%~FK5b
1 Lf.3
D3_ yAF0]
E4`!zBG1^
```

## Disassembly Overview

Functions analyzed: **12** | Decompiled to C: **12**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400013d4` | `0x1400013d4` | 323 | ✓ |
| `fcn.140001164` | `0x140001164` | 306 | ✓ |
| `fcn.140001298` | `0x140001298` | 213 | ✓ |
| `fcn.1400010b4` | `0x1400010b4` | 174 | ✓ |
| `entry2` | `0x14013c530` | 140 | ✓ |
| `entry0` | `0x140148850` | 100 | ✓ |
| `fcn.140001378` | `0x140001378` | 89 | ✓ |
| `entry1` | `0x14000103c` | 46 | ✓ |
| `fcn.14000106c` | `0x14000106c` | 42 | ✓ |
| `fcn.140001098` | `0x140001098` | 28 | ✓ |
| `fcn.140107fe4` | `0x140107fe4` | 9 | ✓ |
| `fcn.140001370` | `0x140001370` | 5 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/entry1.c`](code/entry1.c)
- [`code/entry2.c`](code/entry2.c)
- [`code/fcn.14000106c.c`](code/fcn.14000106c.c)
- [`code/fcn.140001098.c`](code/fcn.140001098.c)
- [`code/fcn.1400010b4.c`](code/fcn.1400010b4.c)
- [`code/fcn.140001164.c`](code/fcn.140001164.c)
- [`code/fcn.140001298.c`](code/fcn.140001298.c)
- [`code/fcn.140001370.c`](code/fcn.140001370.c)
- [`code/fcn.140001378.c`](code/fcn.140001378.c)
- [`code/fcn.1400013d4.c`](code/fcn.1400013d4.c)
- [`code/fcn.140107fe4.c`](code/fcn.140107fe4.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C code, here is an analysis of the binary's functionality:

### Core Functionality
This binary functions primarily as a **malware loader or packer**. Its main purpose is to decrypt and resolve hidden components (such as malicious strings, file paths, or further stages of execution) that are obfuscated within its own data sections. 

Instead of calling standard Windows APIs directly in a way that can be easily seen by static analysis tools, it uses several layers of indirection to hide its true intent until runtime.

### Suspicious and Malicious Behaviors

*   **Layered Obfuscation & Decryption:**
    *   The function `fcn.140001164` is a dedicated **XOR-based decryption routine**. It uses a hardcoded 40-byte key to decrypt data in memory. This is a common technique used by malware to hide strings such as C2 (Command & Control) domains, file paths, or registry keys from automated scanners.
    *   The use of a rolling index/offset (`uStack_34`) during the XOR operation suggests a slightly more complex decryption loop than a simple static key, intended to hinder basic "de-obfuscation" scripts.

*   **Dynamic API Resolution:**
    *   The function `fcn.1400010b4` appears to be a **custom API resolver**. Rather than importing standard functions directly (e.g., `GetProcAddress`), the code iterates through a table of strings and compares them to find the addresses of system functions at runtime. This is used to bypass Import Address Table (IAT) analysis and hide what system capabilities (like networking or process injection) the malware has.

*   **Signature Scanning for Hidden Data:**
    *   The function `fcn.140001378` performs a scan of memory looking for specific "magic" byte patterns (a signature). Once it finds these signatures, it treats the following data as valid parameters for the core logic (`entry1`). This suggests that the binary contains several "modules" or hidden payloads that are only activated if certain conditions/signatures are met.

*   **Anti-Analysis / Evasion Techniques:**
    *   The entry points `entry0` and `entry2` contain highly irregular code, including complex bitwise arithmetic on registers and calls to software interrupts (`swi`). These are characteristic of **anti-debugging or anti-VM (Virtual Machine) checks**. 
    *   These routines are designed to crash standard debuggers or detect the presence of a sandbox before the "real" payload is decrypted and executed.

### Notable Techniques & Patterns

*   **Data Masking:** The code extensively uses manual offset calculations (e.g., `arg1 + 0x35`, `arg1 + 0x2d`) to access data structures, which helps hide the meaning of variables from automated decompilers.
*   **Payload Processing:** In function `fcn.1400013d4`, there is a loop that processes what appears to be an array of "objects" (potentially files or network configurations). It iterates 12 times, checking each for validity before calling the decryption routine on them.
*   **Instruction Overlap/Garbage Code:** The `entry0` and `entry2` functions contain "bad instruction" flags in your report, which often occur when malware authors intentionally overlap instructions or use "junk code" to confuse disassemblers like IDA Pro or Ghidra.

### Summary of Risk
This binary is **highly suspicious**. It exhibits the hallmarks of a sophisticated loader used in high-level threats (such as Ransomware, Spyware, or Trojan Droppers). Its primary tactics are:
1.  **Hiding its intent** through custom decryption and dynamic API resolution.
2.  **Protecting itself from analysis** using anti-debugging logic at the entry point.
3.  **Carrying hidden payloads** that remain encrypted in memory until the specific "signature" is found during execution.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the corresponding MITRE ATT&K techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a custom XOR-based decryption routine and "magic" byte scanning hides critical data (C2s, paths, payloads) from static analysis. |
| **T1027** | Obfuscated Files or Information | The inclusion of junk code and overlapping instructions is a specific obfuscation tactic designed to hinder disassembly and manual reverse engineering. |
| **T1027** | Obfuscated Files or Information | Implementing a custom API resolver hides the binary's true capabilities by bypassing standard Import Address Table (IAT) analysis. |
| **T1497** | Virtualization/Sandbox Detection | The presence of `swi` calls and complex bitwise arithmetic at entry points indicates active checks for debugger environments or virtual machines. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** Because the malware uses heavy obfuscation and encryption (as noted in the analysis), several potential IOCs (C2 domains, file paths) remain encrypted within the binary and do not appear in plaintext in the provided report.

### **IP addresses / URLs / Domains**
*   None identified (Values are currently hidden via XOR decryption).

### **File paths / Registry keys**
*   None identified (Values are currently hidden via XOR decryption).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts (Behavioral Indicators & Technical Signatures)**
The following internal offsets and behaviors can be used to create YARA rules or behavioral signatures for detection:

*   **Encryption Routine:** `fcn.140001164` (XOR-based decryption with a 40-byte hardcoded key).
*   **Custom API Resolver:** `fcn.1400010b4` (Used to bypass IAT analysis and resolve system functions at runtime).
*   **Signature Scanning Logic:** `fcn.140001378` (Scans memory for "magic" byte patterns to activate modules/payloads).
*   **Anti-Analysis Entry Points:** `entry0` and `entry2` (Contain anti-debugging and anti-VM logic, specifically utilizing complex bitwise arithmetic and software interrupts `swi`).
*   **Payload Processing Loop:** `fcn.1400013d4` (Iterates 12 times to validate and decrypt objects/configurations).
*   **Obfuscated String Block:** The recurring strings (e.g., `H7c$}EJ4a`, `I8d%~FK5b`, `1 L\f.3`) are likely part of the encrypted data or "junk code" used to hinder automated disassembly.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Layered Obfuscation & Dynamic Resolution:** The sample utilizes a custom XOR-based decryption routine and a manual API resolution system to bypass Import Address Table (IAT) analysis, which are classic indicators of a loader designed to hide its primary payload.
*   **Anti-Analysis Techniques:** The use of `swi` instructions and complex bitwise arithmetic at the entry points specifically targets debuggers and virtualized environments, typical of sophisticated loaders protecting underlying malicious components.
*   **Payload Staging:** The presence of a signature scanning routine (`fcn.140001378`) and a loop to process multiple "objects" indicates that the primary purpose is to identify, decrypt, and execute hidden payloads rather than performing standalone malicious actions like data theft or encryption directly.
