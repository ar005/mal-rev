# Threat Analysis Report

**Generated:** 2026-07-13 20:14 UTC
**Sample:** `056e17a0478ce166200140dbe0165140d8f7c851f0acc0cca6d1f267df1eaeec_056e17a0478ce166200140dbe0165140d8f7c851f0acc0cca6d1f267df1eaeec.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `056e17a0478ce166200140dbe0165140d8f7c851f0acc0cca6d1f267df1eaeec_056e17a0478ce166200140dbe0165140d8f7c851f0acc0cca6d1f267df1eaeec.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 110,080 bytes |
| MD5 | `2f9246f506d28735902f550c58f8b242` |
| SHA1 | `dfb504a58117127bcafff061a09726657271b0b1` |
| SHA256 | `056e17a0478ce166200140dbe0165140d8f7c851f0acc0cca6d1f267df1eaeec` |
| Overall entropy | 5.94 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771444488 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 57,856 | 6.413 | No |
| `.rdata` | 41,472 | 4.775 | No |
| `.data` | 3,072 | 1.912 | No |
| `.pdata` | 4,096 | 4.833 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.851 | No |

### Imports

**USER32.dll**: `DispatchMessageA`, `TranslateMessage`, `GetMessageA`
**ADVAPI32.dll**: `GetUserNameA`
**KERNEL32.dll**: `CreateFileW`, `WriteConsoleW`, `RtlLookupFunctionEntry`, `GetDiskFreeSpaceExA`, `IsDebuggerPresent`, `CheckRemoteDebuggerPresent`, `CloseHandle`, `AddVectoredExceptionHandler`, `HeapAlloc`, `HeapFree`, `GetProcessHeap`, `Sleep`, `GetCurrentProcess`, `CreateThread`, `GetCurrentThread`

### Exports

`GetFileVersionInfoA`, `GetFileVersionInfoByHandle`, `GetFileVersionInfoExA`, `GetFileVersionInfoExW`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoSizeExA`, `GetFileVersionInfoSizeExW`, `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`, `VerFindFileA`, `VerFindFileW`, `VerInstallFileA`, `VerInstallFileW`, `VerLanguageNameA`, `VerLanguageNameW`, `VerQueryValueA`, `VerQueryValueW`

## Extracted Strings

Total strings found: **476** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
.reloc
@USVWATAUAVAWH
@8}t+
A_A^A]A\_^[]
taHcA<
@SUVWATAUAVAWH
A_A^A]A\_^][
@SUVATAWH
I+_0t|A
A_A\^][
A_A\^][
|$ AVH
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
	H;bX
	H;>X
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.18000692c` | `0x18000692c` | 14715 | ✓ |
| `fcn.1800068f4` | `0x1800068f4` | 14710 | ✓ |
| `fcn.180002cdc` | `0x180002cdc` | 12443 | ✓ |
| `fcn.180002bdc` | `0x180002bdc` | 2846 | ✓ |
| `fcn.180002d6c` | `0x180002d6c` | 2568 | ✓ |
| `fcn.1800088e8` | `0x1800088e8` | 1829 | ✓ |
| `fcn.18000e240` | `0x18000e240` | 1677 | ✓ |
| `section..text` | `0x180001000` | 1386 | ✓ |
| `fcn.1800045e8` | `0x1800045e8` | 1213 | ✓ |
| `fcn.180001b80` | `0x180001b80` | 1185 | ✓ |
| `fcn.18000ca18` | `0x18000ca18` | 1171 | ✓ |
| `fcn.1800020a0` | `0x1800020a0` | 1026 | ✓ |
| `fcn.18000bff0` | `0x18000bff0` | 922 | ✓ |
| `fcn.18000e8f0` | `0x18000e8f0` | 920 | ✓ |
| `fcn.18000ba80` | `0x18000ba80` | 920 | ✓ |
| `fcn.1800027a0` | `0x1800027a0` | 892 | ✓ |
| `fcn.180008588` | `0x180008588` | 862 | ✓ |
| `fcn.180006cfc` | `0x180006cfc` | 817 | ✓ |
| `fcn.18000d364` | `0x18000d364` | 815 | ✓ |
| `fcn.180001870` | `0x180001870` | 779 | ✓ |
| `fcn.1800093b4` | `0x1800093b4` | 712 | ✓ |
| `fcn.180002fc8` | `0x180002fc8` | 667 | ✓ |
| `fcn.180009010` | `0x180009010` | 623 | ✓ |
| `fcn.180001600` | `0x180001600` | 620 | ✓ |
| `fcn.18000a444` | `0x18000a444` | 604 | ✓ |
| `fcn.1800065fc` | `0x1800065fc` | 589 | ✓ |
| `fcn.180004aa8` | `0x180004aa8` | 584 | ✓ |
| `fcn.180005048` | `0x180005048` | 557 | ✓ |
| `fcn.18000b1a8` | `0x18000b1a8` | 555 | ✓ |
| `fcn.1800034a0` | `0x1800034a0` | 517 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001600.c`](code/fcn.180001600.c)
- [`code/fcn.180001870.c`](code/fcn.180001870.c)
- [`code/fcn.180001b80.c`](code/fcn.180001b80.c)
- [`code/fcn.1800020a0.c`](code/fcn.1800020a0.c)
- [`code/fcn.1800027a0.c`](code/fcn.1800027a0.c)
- [`code/fcn.180002bdc.c`](code/fcn.180002bdc.c)
- [`code/fcn.180002cdc.c`](code/fcn.180002cdc.c)
- [`code/fcn.180002d6c.c`](code/fcn.180002d6c.c)
- [`code/fcn.180002fc8.c`](code/fcn.180002fc8.c)
- [`code/fcn.1800034a0.c`](code/fcn.1800034a0.c)
- [`code/fcn.1800045e8.c`](code/fcn.1800045e8.c)
- [`code/fcn.180004aa8.c`](code/fcn.180004aa8.c)
- [`code/fcn.180005048.c`](code/fcn.180005048.c)
- [`code/fcn.1800065fc.c`](code/fcn.1800065fc.c)
- [`code/fcn.1800068f4.c`](code/fcn.1800068f4.c)
- [`code/fcn.18000692c.c`](code/fcn.18000692c.c)
- [`code/fcn.180006cfc.c`](code/fcn.180006cfc.c)
- [`code/fcn.180008588.c`](code/fcn.180008588.c)
- [`code/fcn.1800088e8.c`](code/fcn.1800088e8.c)
- [`code/fcn.180009010.c`](code/fcn.180009010.c)
- [`code/fcn.1800093b4.c`](code/fcn.1800093b4.c)
- [`code/fcn.18000a444.c`](code/fcn.18000a444.c)
- [`code/fcn.18000b1a8.c`](code/fcn.18000b1a8.c)
- [`code/fcn.18000ba80.c`](code/fcn.18000ba80.c)
- [`code/fcn.18000bff0.c`](code/fcn.18000bff0.c)
- [`code/fcn.18000ca18.c`](code/fcn.18000ca18.c)
- [`code/fcn.18000d364.c`](code/fcn.18000d364.c)
- [`code/fcn.18000e240.c`](code/fcn.18000e240.c)
- [`code/fcn.18000e8f0.c`](code/fcn.18000e8f0.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

Based on the second chunk of disassembly, I have updated the analysis. This new data confirms that the binary is not just a simple loader but contains several advanced techniques designed to evade modern EDR (Endpoint Detection and Response) systems and specialized security monitoring.

### **Updated Analysis & New Findings**

The additional disassembly provides evidence of three major high-level malicious behaviors: **Advanced Anti-Analysis**, **Security Feature Disabling**, and **Symmetric Decryption of Payloads**.

#### **1. Advanced Anti-Analysis (Hypervisor Detection)**
In `fcn.180002fc8`, the binary performs a deep dive into CPU capabilities using the `CPUID` instruction:
*   **Hypervisor Check:** The code specifically checks for "Hypervisor" signatures in the CPU's reported features. It looks for specific bit patterns (like `49 65 6e 69`) to determine if it is running inside a virtualized environment (e.g., KVM, VMware, or Hyper-V).
*   **Advanced Feature Enumeration:** It queries the "Extended Feature Enumeration" and checks the status of various CPU flags (like `XCR0`). This allows the malware to fingerprint the specific type of virtualization it is running in, a common tactic used by advanced persistent threats (APTs) to avoid analysis labs.

#### **2. Disabling System Monitoring (ETW Patching)**
In `fcn.180001600`, a highly sophisticated evasion technique was identified:
*   **ETW Tampering:** The binary locates `ntdll.dll` and specifically targets the function `EtwEventWrite`. It uses `VirtualProtect` to change memory permissions and then **overwrites the start of the function with shellcode/instructions (`0xc033`, `0xc3`)**.
*   **Purpose:** `EtwEventWrite` is a primary source for ETW (Event Tracing for Windows). By "patching" this function in memory, the malware effectively blinds many EDR and EPP solutions that rely on ETW to detect suspicious activities like process injection or network connections.

#### **3. Symmetric Payload Decryption**
In `fcn.180001870`, the binary's use of the Windows Cryptography API is confirmed:
*   **BCrypt Library:** It resolves several functions from `bcrypt.dll` (e.g., `BCryptOpenAlgorithmProvider`, `BCryptGenerateSymmetricKey`, and `BCryptDecrypt`).
*   **CBC Mode:** The code explicitly sets the "ChainingMode" to **CBC** (Cipher Block Chaining). 
*   **Conclusion:** This confirms that a significant portion of the malicious payload is likely encrypted on disk or within the binary. The loader decrypts this content into memory using a symmetric key before "manually mapping" it.

#### **4. Data Processing and Formatting**
In `fcn.18000d364`, there are signs of data preparation:
*   **Line Ending Conversion:** The code contains logic to scan for carriage returns (`\r`) or line feeds (`\n`). This is often used when the malware prepares strings or configuration data for writing to a file or sending over a network, ensuring compatibility with different OS standards.

---

### **Updated Summary of Risks**

| Category | Observed Behavior | Technical Detail | Significance |
| :--- | :--- | :--- | :--- |
| **Evasion (Advanced)** | Hypervisor & CPU Feature checks (`CPUID`) | Detects KVM/VMware and specific hardware environments. | **Critical**: Prevents analysis in automated sandboxes. |
| **EDR Evasion** | Patching `ntdll!EtwEventWrite` | Overwrites ETW functions to blind security monitoring tools. | **Critical**: A high-end technique to bypass modern EDRs. |
| **Payload Protection** | BCrypt Symmetric Decryption (CBC) | Uses `bcrypt.dll` to decrypt a hidden payload in memory. | **High**: Protects the actual malware from static analysis. |
| **Network/File Prep** | Line Endings Conversion & Buffer Processing | Ensures data is correctly formatted for C2 communication or logging. | **Medium**: Indicates preparation of stolen data or config. |
| **Injection** | Manual Mapping via `Nt...` functions | Bypasses standard Windows Loader to run code in memory. | **Critical**: Core mechanism for payload execution. |

### **Final Conclusion Update**
The presence of **ETW patching** combined with **BCrypt-based decryption** and **Hypervisor detection** suggests this is a high-sophistication piece of malware (likely a primary loader/dropper for an APT or advanced ransomware). It is specifically designed to resist "low-hanging" analysis by hiding its core functionality until it confirms the environment is a physical, non-monitored machine.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtualization | The malware performs CPUID and feature checks to detect if it is running in a virtualized environment like KVM, VMware, or Hyper-V. |
| T1562.001 | Disable or Modify System Management Tools | The binary patches the `EtwEventWrite` function in `ntdll.dll` to blind security tools that rely on Event Tracing for Windows (ETW). |
| T1027 | Obfuscated Files/Information | The use of BCrypt, CBC mode, and symmetric keys indicates the payload is encrypted to evade static analysis. |
| T1055 | Process Injection | "Manual mapping" is used to bypass standard Windows loaders when injecting the decrypted payload into memory. |
| T1430 | Encryption | The specific use of a known cryptographic library (BCrypt) to encrypt and decrypt data for obfuscation purposes. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Several strings were identified as standard Windows system files or common developer tools used for anti-analysis; these have been excluded from the final list as requested.*

### **IP addresses / URLs / Domains**
*   *None identified.* (The alphanumeric noise in the "Extracted Strings" section appears to be obfuscated data/garbage and does not resolve to usable network indicators.)

### **File paths / Registry keys**
*   *None identified.* (Standard system paths like `ntdll.dll` and `wininet.dll` were excluded as false positives.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **User-Agent String:** 
    *   `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36`
*   **ETW Patching Pattern:** 
    *   The binary specifically targets `ntdll!EtwEventWrite` and patches it with the hex sequence: `0xc033, 0xc3`. (This is used to blind EDR solutions).
*   **Anti-Analysis/Sandbox Detection Strings:** 
    *   The following terms are present in the binary as indicators of active environment checks: `cuckoo`, `cuckoosandbox`, `vmcheck.dll`, `x64dbg`, `ollydbg`, `wireshark`, `procmon`.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High

4. **Key evidence**:
* **Advanced EDR Evasion:** The binary employs sophisticated techniques to blind security monitoring, specifically patching `ntdll!EtwEventWrite` and using "manual mapping" to execute the payload in memory while bypassing standard Windows loaders.
* **Robust Anti-Analysis:** The presence of hypervisor checks (via `CPUID`), detection of debugger/monitoring tools (x64dbg, procmon), and the use of `bcrypt.dll` for symmetric decryption indicates a high-effort attempt to hide from automated sandboxes and manual analysis.
* **Multi-Stage Behavior:** The behavior of decrypting a payload in memory and preparing data via line-ending conversion is characteristic of a sophisticated loader designed to deliver downstream threats such as ransomware or an APT-level backdoor.
