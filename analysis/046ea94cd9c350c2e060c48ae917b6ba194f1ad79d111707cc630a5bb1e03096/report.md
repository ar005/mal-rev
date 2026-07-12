# Threat Analysis Report

**Generated:** 2026-07-11 17:21 UTC
**Sample:** `046ea94cd9c350c2e060c48ae917b6ba194f1ad79d111707cc630a5bb1e03096_046ea94cd9c350c2e060c48ae917b6ba194f1ad79d111707cc630a5bb1e03096.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `046ea94cd9c350c2e060c48ae917b6ba194f1ad79d111707cc630a5bb1e03096_046ea94cd9c350c2e060c48ae917b6ba194f1ad79d111707cc630a5bb1e03096.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 110,080 bytes |
| MD5 | `a8bedd55e56241c0fc1e173e8c0180c0` |
| SHA1 | `36c187e553ab8115593aa25c2088882fe4d354c0` |
| SHA256 | `046ea94cd9c350c2e060c48ae917b6ba194f1ad79d111707cc630a5bb1e03096` |
| Overall entropy | 5.94 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771442739 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 57,856 | 6.414 | No |
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
taHcA<
@USVWATAUAVAWH
@8}t+
A_A^A]A\_^[]
@SUVATAWH
I+_0t|A
A_A\^][
A_A\^][
@SUVWATAUAVAWH
A_A^A]A\_^][
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
| `fcn.180001450` | `0x180001450` | 1386 | ✓ |
| `fcn.1800045e8` | `0x1800045e8` | 1213 | ✓ |
| `fcn.1800019c0` | `0x1800019c0` | 1185 | ✓ |
| `fcn.18000ca18` | `0x18000ca18` | 1171 | ✓ |
| `fcn.180001ee0` | `0x180001ee0` | 1026 | ✓ |
| `fcn.18000bff0` | `0x18000bff0` | 922 | ✓ |
| `fcn.18000e8f0` | `0x18000e8f0` | 920 | ✓ |
| `fcn.18000ba80` | `0x18000ba80` | 920 | ✓ |
| `fcn.1800027a0` | `0x1800027a0` | 892 | ✓ |
| `fcn.180008588` | `0x180008588` | 862 | ✓ |
| `fcn.180006cfc` | `0x180006cfc` | 817 | ✓ |
| `fcn.18000d364` | `0x18000d364` | 815 | ✓ |
| `fcn.1800022f0` | `0x1800022f0` | 779 | ✓ |
| `fcn.1800093b4` | `0x1800093b4` | 712 | ✓ |
| `fcn.180002fc8` | `0x180002fc8` | 667 | ✓ |
| `fcn.180009010` | `0x180009010` | 623 | ✓ |
| `fcn.180001150` | `0x180001150` | 620 | ✓ |
| `fcn.18000a444` | `0x18000a444` | 604 | ✓ |
| `fcn.1800065fc` | `0x1800065fc` | 589 | ✓ |
| `fcn.180004aa8` | `0x180004aa8` | 584 | ✓ |
| `fcn.180005048` | `0x180005048` | 557 | ✓ |
| `fcn.18000b1a8` | `0x18000b1a8` | 555 | ✓ |
| `fcn.1800034a0` | `0x1800034a0` | 517 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001150.c`](code/fcn.180001150.c)
- [`code/fcn.180001450.c`](code/fcn.180001450.c)
- [`code/fcn.1800019c0.c`](code/fcn.1800019c0.c)
- [`code/fcn.180001ee0.c`](code/fcn.180001ee0.c)
- [`code/fcn.1800022f0.c`](code/fcn.1800022f0.c)
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

## Behavioral Analysis

Based on the second portion of the disassembly, I have updated and extended the analysis. This new code confirms several advanced evasion techniques and highlights the specific methods used to handle encrypted data and evade modern security monitoring tools.

### Updated Summary: Advanced Loader Analysis (Updated with Chunk 2)

This is a sophisticated **downloader and unpacker** designed for multi-stage deployment. It exhibits high-level "packer" behaviors, including anti-debugging/anti-VM measures, manual memory mapping of payloads, and active evasion of Endpoint Detection and Response (EDR) systems.

---

### Updated Core Functionality & Purpose
1.  **Evasion & Stealth:** The loader actively modifies system DLLs in memory to blind security tools and performs deep hardware checks to ensure it is running on a physical machine rather than a virtualized sandbox.
2.  **Encryption Handling (CNG API):** Unlike simpler loaders that use standard Windows APIs, this code uses the **BCrypt (Cryptography Next Generation)** library to decrypt segments of data/payloads before they are mapped into memory.
3.  **Manual Mapping & Execution:** The loader performs manual mapping by resolving `ntdll` functions directly, ensuring that common "hooking" points used by antivirus software are bypassed during the injection process.
4.  **Network Fetch & Data Processing:** It fetches remote data and includes complex logic to handle different code pages (encoding/decoding), likely to normalize strings or paths before processing.

---

### New & Enhanced Malicious Behaviors (Updated)

#### 1. Advanced Defense Evasion (EDR Blinding)
The disassembly reveals a very specific and dangerous technique in **`fcn.180001150`**:
*   **ETW Patching:** The code searches for `EtwEventWrite` within `ntdll.dll`. It then uses `VirtualProtect` to change the memory permissions of that function and overwrites it with a specific byte sequence (`0xc033`, `0xc3`). 
    *   **Impact:** This is a known technique used by malware (and advanced tools) to disable **Event Tracing for Windows (ETW)**. By patching this, the loader prevents many EDR and EDR-lite products from receiving telemetry about the processes' actions, effectively "blinding" security software during the execution of the injected payload.

#### 2. Sophisticated Anti-Analysis & Virtualization Detection
Beyond simple string checks, **`fcn.180002fc8`** implements deep hardware fingerprinting:
*   **CPUID Exploitation:** The function performs multiple `CPUID` queries to check for specific CPU features, instruction sets (like SSE4.2), and the "Processor Brand" string. 
*   **VM Detection via Instruction Sets:** It checks if certain bitflags are set that are typically absent or different in virtualized environments. This ensures that the loader won't execute its final payload unless it is confident it is on a physical, non-analyzed machine.

#### 3. Robust Encryption Processing (BCrypt API)
In **`fcn.1800022f0`**, the code explicitly imports and uses a suite of BCrypt functions:
*   **Functions:** `BCryptOpenAlgorithmProvider`, `BCryptSetProperty` (setting "ChainingMode" to CBC), `BCryptGenerateSymmetricKey`, and `BCryptDecrypt`.
*   **Implication:** This indicates that the payload is not just a raw file being downloaded; it is likely encrypted using standard industry algorithms (e.g., AES) during transit or on disk. The loader handles the decryption "in-process" before memory injection occurs.

#### 4. Complex Data/String Manipulation
The functions **`fcn.1800093b4`** and **`fcn.18000d364`** suggest a high level of professional development:
*   **Code Page Handling:** The code checks `IsValidCodePage` and uses `GetCPInfo`. This suggests it is preparing to handle different language encodings or ensuring that internal strings are correctly translated before they are passed to Windows API functions.
*   **Buffer/State Management:** **`fcn.180009010`** contains complex logic involving locks (`LOCK()`) and nested loops, likely managing the state machine of the loader as it moves through different stages of extraction.

---

### Summary of Technical Indicators (IOCs) & Behaviors

| Category | Technique / Indicator | Analysis |
| :--- | :--- | :--- |
| **Defense Evasion** | ETW Patching (`EtwEventWrite`) | Disables system telemetry to hide from EDR/antivirus. |
| **Defense Evasion** | CPUID Fingerprinting | Detects Virtual Machines and emulators via hardware flags. |
| **Execution** | BCrypt (CNG) API Usage | Decrypts payload components in memory using AES-style logic. |
| **Injection** | Manual Mapping | Directly invokes `NtAllocateVirtualMemory` & `NtProtectVirtualMemory`. |
| **Obfuscation** | Code Page Normalization | Ensures compatibility/stealth across different system locales. |
| **Payload Delivery** | WinINet / Mozilla User-Agent | Mimics a standard web browser to download the payload from a remote server. |

### Conclusion of Analysis
This is not a "script kiddie" piece of malware; it is an **enterprise-grade loader**. It uses high-end evasion techniques (ETW patching, hardware fingerprinting) and modern cryptographic libraries (CNG/BCrypt). Its primary goal is to stay silent on the host by blinding security monitoring tools before decrypting and executing a final stage payload. 

**Recommendation:** If this binary is found in an environment, look for "EtwEventWrite" patches or suspicious `ntdll.dll` memory modifications as indicators of compromise (IOCs) associated with sophisticated threats.

---

## MITRE ATT&CK Mapping

Based on your behavioral analysis, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1562.001** | Disable or Modify Security Software | The loader patches `EtwEventWrite` in `ntdll.dll` to disable ETW telemetry, effectively blinding EDR and antivirus tools. |
| **T1497** | Virtualization/Sandbox Evasion | The code uses CPUID fingerprinting and hardware-specific instruction checks to detect and avoid analysis environments. |
| **T1106** | Native API | By directly invoking `ntdll` functions (e.g., `NtAllocateVirtualMemory`) instead of Win32 APIs, the loader bypasses security software that hooks standard system calls. |
| **T1561** | Data Encoding | The use of the BCrypt/CNG library indicates that payloads are encrypted during transit and decrypted in-process before execution. |
| **T1027** | Obfuscated Files or Purposes | Complex code page handling and manual mapping logic are utilized to hide the loader's true functionality and complicate analysis. |
| **T1105** | Ingress Tool Transfer | The use of WinINet with a standard User-Agent allows the loader to fetch remote payloads while mimicking legitimate web traffic. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis mentions `InternetOpenUrlA`, but no specific hardcoded C2 domains or IPs were present in the provided strings.)

### **File paths / Registry keys**
*   *No specific file paths or registry keys were identified.*
*   Note: The binary checks for the presence of several security and analysis tools (e.g., `x64dbg`, `wireshark`, `procmon`), which indicates targeted environment checking.

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
**User-Agents:**
*   `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36`

**Known Anti-Analysis / Evasion Strings:**
The following strings indicate the malware checks for and attempts to evade common security products and analysis environments:
*   **Sandbox/VM Detection:** `sandbox`, `malware`, `cuckoo`, `cuckoosandbox`, `wilbert`, `hapubws`, `systemit`, `bea-vr`
*   **Security Tool Checks:** `sbiedll.dll`, `api_log.dll`, `dir_watch.dll`, `vmcheck.dll`, `SxIn.dll`, `snxhk.dll`, `cmdvrt32.dll`, `cuckoomon.dll`
*   **Debugger/Analyzer Tools:** `x64dbg`, `x32dbg`, `ollydbg`, `windbg`, `ida.exe`, `processhacker`, `fiddler`, `wireshark`, `procmon`, `apimonitor`, `pestudio`

**Behavioral Indicators (Techniques):**
*   **ETW Patching:** The malware specifically targets and patches the `EtwEventWrite` function within `ntdll.dll`. It overwrites it with the byte sequence: `0xc033, 0xc3`. This is a high-confidence indicator of an attempt to blind EDR/AV systems.
*   **Manual Mapping:** Use of `NtAllocateVirtualMemory`, `NtProtectVirtualMemory`, and `NtWriteVirtualMemory` for direct injection, bypassing standard API hooks.
*   **CNG Cryptography (BCrypt):** The use of `BCryptOpenAlgorithmProvider`, `BCryptSetProperty` (specifically setting "ChainingMode" to CBC), `BCryptGenerateSymmetricKey`, and `BCryptDecrypt` indicates high-grade payload encryption (likely AES).
*   **Hardware Fingerprinting:** Use of `CPUID` instructions and check for specific instruction sets (e.g., SSE4.2) to detect virtualized environments.
*   **Code Page Normalization:** The use of `IsValidCodePage` and `GetCPInfo` to manage data encoding before processing.

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1. **Malware family**: custom (loader)
2. **Malware type**: loader / downloader
3. **Confidence**: High
4. **Key evidence**: 
    *   **Advanced Evasion Techniques:** The sample performs specific "EDR blinding" by patching `EtwEventWrite` in `ntdll.dll`, a hallmark of sophisticated, enterprise-grade malware designed to bypass modern security monitoring.
    *   **Sophisticated Execution Logic:** It uses the BCrypt (CNG) library for in-process decryption and implements manual mapping of payloads via direct calls to `ntdll` functions to circumvent standard Windows API hooks.
    *   **Multi-layered Anti-Analysis:** The sample includes robust environmental checks, including CPUID fingerprinting to detect virtual machines/sandboxes and specific checks for a wide range of analysis tools (e.g., `x64dbg`, `wireshark`).
