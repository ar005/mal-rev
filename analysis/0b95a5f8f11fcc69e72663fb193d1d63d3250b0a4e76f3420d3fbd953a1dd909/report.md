# Threat Analysis Report

**Generated:** 2026-07-27 13:34 UTC
**Sample:** `0b95a5f8f11fcc69e72663fb193d1d63d3250b0a4e76f3420d3fbd953a1dd909_0b95a5f8f11fcc69e72663fb193d1d63d3250b0a4e76f3420d3fbd953a1dd909.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b95a5f8f11fcc69e72663fb193d1d63d3250b0a4e76f3420d3fbd953a1dd909_0b95a5f8f11fcc69e72663fb193d1d63d3250b0a4e76f3420d3fbd953a1dd909.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 110,080 bytes |
| MD5 | `926a0f9e832cb9c03d21c4bc31d0c328` |
| SHA1 | `e5edb77e8f31d3230d99f7af7e5cfc40c7f707b8` |
| SHA256 | `0b95a5f8f11fcc69e72663fb193d1d63d3250b0a4e76f3420d3fbd953a1dd909` |
| Overall entropy | 5.939 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771838913 |
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

Total strings found: **475** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
.reloc
@SUVWATAUAVAWH
A_A^A]A\_^][
@USVWATAUAVAWH
@8}t+
A_A^A]A\_^[]
taHcA<
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
| `fcn.180001310` | `0x180001310` | 1386 | ✓ |
| `fcn.1800045e8` | `0x1800045e8` | 1213 | ✓ |
| `fcn.180002000` | `0x180002000` | 1185 | ✓ |
| `fcn.18000ca18` | `0x18000ca18` | 1171 | ✓ |
| `fcn.180001910` | `0x180001910` | 1026 | ✓ |
| `fcn.18000bff0` | `0x18000bff0` | 922 | ✓ |
| `fcn.18000e8f0` | `0x18000e8f0` | 920 | ✓ |
| `fcn.18000ba80` | `0x18000ba80` | 920 | ✓ |
| `fcn.1800027a0` | `0x1800027a0` | 892 | ✓ |
| `fcn.180008588` | `0x180008588` | 862 | ✓ |
| `fcn.180006cfc` | `0x180006cfc` | 817 | ✓ |
| `fcn.18000d364` | `0x18000d364` | 815 | ✓ |
| `section..text` | `0x180001000` | 779 | ✓ |
| `fcn.1800093b4` | `0x1800093b4` | 712 | ✓ |
| `fcn.180002fc8` | `0x180002fc8` | 667 | ✓ |
| `fcn.180009010` | `0x180009010` | 623 | ✓ |
| `fcn.180001d20` | `0x180001d20` | 620 | ✓ |
| `fcn.18000a444` | `0x18000a444` | 604 | ✓ |
| `fcn.1800065fc` | `0x1800065fc` | 589 | ✓ |
| `fcn.180004aa8` | `0x180004aa8` | 584 | ✓ |
| `fcn.180005048` | `0x180005048` | 557 | ✓ |
| `fcn.18000b1a8` | `0x18000b1a8` | 555 | ✓ |
| `fcn.1800034a0` | `0x1800034a0` | 517 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001310.c`](code/fcn.180001310.c)
- [`code/fcn.180001910.c`](code/fcn.180001910.c)
- [`code/fcn.180001d20.c`](code/fcn.180001d20.c)
- [`code/fcn.180002000.c`](code/fcn.180002000.c)
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

Based on the additional disassembly provided in chunk 2/2, I have updated the analysis. The new code reveals significant advancements in the malware's sophistication, specifically regarding **cryptographic operations**, **advanced EDR evasion**, and **environment fingerprinting**.

### Updated Malware Analysis Report (Revised)

**Core Functionality and Purpose**
The binary is a sophisticated **downloader and loader** designed for high-level evasion. It utilizes a multi-stage execution chain where a remote payload is downloaded, decrypted using standard Windows cryptographic libraries, and injected into memory. The presence of complex switch tables and heavy use of `ntdll` functions suggests the malware uses a "loader" architecture common in advanced persistent threats (APTs) and high-end commodity malware (e.g., IcedID, Qakbot).

**Suspicious and Malicious Behaviors**

*   **Anti-Analysis & Anti-Debugging:**
    *   **Debugger/Sandbox Detection:** (Previously identified) `IsDebuggerPresent`, `GetTickCount` loops, and blacklist checks for "vmware", "cuckoosandbox", etc.
    *   **Hardware Fingerprinting (CPUID):** The function `fcn.180002fc8` performs multiple **CPUID** queries. It checks for specific processor features and hardware identifiers to detect if the code is running on a virtual machine or a specific type of emulator/hardware often used in sandboxes.
    *   **Timing-based Evasion:** Implementation of delays and complex conditional loops (e.g., `fcn.18000d364`) designed to frustrate automated behavioral analysis tools.

*   **Network Communication & Payload Processing:**
    *   **Decryption Routine (`bcrypt.dll`):** The sample links against `bcrypt.dll` and resolves functions like `BCryptOpenAlgorithmProvider`, `BCryptGenerateSymmetricKey`, and **`BCryptDecrypt`**. This indicates that the payload fetched from the remote server is encrypted (likely via AES or a similar symmetric algorithm). The loader decrypts this data in memory before it is ever written to disk.
    *   **Standard Web Integration:** Uses `wininet.dll` and "Mozilla" User-Agents to blend into normal traffic.

*   **Process Injection & Payload Execution:**
    *   **Manual Mapping / Reflective Loading:** (Previously identified) Handles PE header parsing, section mapping, and memory protection via `VirtualProtect`.
    *   **System Call Hook Evasion (ETW Patching):** In function `fcn.180001d20`, the malware specifically targets **`ntdll.dll`**. It identifies the address of **`EtwEventWrite`** and uses `VirtualProtect` to overwrite it with a "jump" or "no-op" sequence (`0xc033 0xc3`).
        *   **Impact:** This is a specific technique used to **disable Event Tracing for Windows (ETW)**. Many modern EDR (Endpoint Detection and Response) systems rely on ETW to monitor suspicious system calls; by patching this function, the malware "blinds" the security software.

*   **Evasive Loading Techniques:**
    *   **Custom Virtual Machine (VM) / Interpreter:** The complexity of functions like `fcn.18000d364` and `fcn.18000a444` strongly suggests the presence of a **custom VM or a custom packer engine**. These are used to execute "stub" code that handles complex logic (like decryption, unpacking, and environment checks) in a way that is nearly impossible for static analyzers to map correctly.
    *   **Dynamic API Resolution:** Continues to use `GetProcAddress` to hide its intent from the Import Address Table (IAT).

---

### New Technical Observations & Indicators

| Feature | Detail | Significance |
| :--- | :--- | :--- |
| **Cryptographic Operations** | Use of `BCryptDecrypt` via `bcrypt.dll`. | Confirms the payload is encrypted; indicates a sophisticated multi-stage infection chain. |
| **ETW Disabling** | Patching `ntdll!EtwEventWrite` with `0xc033 0xc3`. | High confidence of intent to bypass EDR/SOC monitoring by silencing telemetry. |
| **Hardware Fingerprinting** | Extensive use of `CPUID` instructions (e.g., `feature_enabled`). | Used to identify virtualization, specific CPU types, and sandbox-specific hardware signatures. |
| **Execution Complexity** | Large switch tables and heavily obfuscated logic in `fcn.18000a444`. | Indicates a custom "packer" or "loader engine" to hide the true payload's behavior until it is fully unpacked. |

### Conclusion & Threat Context
The addition of **ETW patching** and **BCrypt decryption** confirms this is not a simple downloader, but a professional-grade **malware loader**. The author has prioritized "silent execution" by both hiding from automated analysis (via `CPUID` and anti-debug) and proactively blinding security software (by disabling ETW). 

The presence of the custom interpreter/VM logic suggests that even if the first stage is caught, the final payload may be highly complex. This malware is likely a precursor to high-impact payloads such as **Ransomware**, a **Cobalt Strike Beacon**, or an **Information Stealer**.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Escape | The use of `CPUID` instructions and checks for strings like "vmware" or "cuckoosandbox" are used to detect and evade virtualized analysis environments. |
| **T1027** | Obfuscated Files or Information | The integration of `bcrypt.dll` for payload decryption and the use of a custom VM/interpreter both serve to hide the malware's true functionality from static analysis. |
| **T1562.001** | Disable or Modify Tools | Patching `ntdll!EtwEventWrite` is a specific technique used to disable Event Tracing for Windows (ETW) to "blind" EDR and security monitoring tools. |
| **T1055** | Process Injection | The use of manual mapping, reflective loading, and `VirtualProtect` indicates the malware injects its payload directly into memory to avoid disk-based detection. |
| **T1036** | Masquerading | The use of a standard "Mozilla" User-Agent is intended to blend malicious network traffic with legitimate web browsing. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Standard system libraries (e.g., `ntdll.dll`), Windows API functions (e.g., `NtCreateThreadEx`), and common development macros were excluded as they do not constitute unique indicators for this specific threat.

### **IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

### **File paths / Registry keys**
*   *(None identified; all file references were to standard Windows system libraries.)*

### **Mutex names / Named pipes**
*   *(None identified)*

### **Hashes**
*   **0xc033 0xc3** (Note: This is the specific jump/nop instruction sequence used to patch `EtwEventWrite` in memory, rather than a file hash.)

### **Other artifacts**
*   **User-Agent String:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36`
*   **ETW Patching Signature:** Target: `ntdll!EtwEventWrite` | Patch: `0xc033 0xc3` (Used to blind EDR systems).
*   **Anti-Analysis / Sandbox Detection Strings:**
    *   `cuckoosandbox`
    *   `wireshark`
    *   `x64dbg`
    *   `x32dbg`
    *   `ollydbg`
    *   `processhacker`
    *   `fiddler`
    *   `apimonitor`
    *   `pestudio`
    *   `sbiedll.dll` (Security software check)
    *   `vmcheck.dll`
    *   `cuckoomon.dll`
*   **Cryptographic Behavior:** Use of `bcrypt.dll` for **`BCryptDecrypt`** suggests an encrypted payload delivered via HTTP/S.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Evasion Techniques:** The sample employs sophisticated methods to "blind" security software, specifically by patching `ntdll!EtwEventWrite` (ETW Patching) and utilizing `CPUID` instructions for hardware fingerprinting to detect virtualized environments.
    *   **Sophisticated Payload Handling:** Use of the `bcrypt.dll` library for decrypting remote payloads in memory and the presence of a custom VM/interpreter indicate a high level of development intended to hide core functionality from static analysis.
    *   **In-Memory Execution:** The combination of manual mapping, reflective loading, and `VirtualProtect` usage confirms it is designed to execute and inject payloads directly into memory to bypass traditional file-based detection.
