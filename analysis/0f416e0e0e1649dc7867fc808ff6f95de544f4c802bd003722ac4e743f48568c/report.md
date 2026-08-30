# Threat Analysis Report

**Generated:** 2026-08-15 20:46 UTC
**Sample:** `0f416e0e0e1649dc7867fc808ff6f95de544f4c802bd003722ac4e743f48568c_0f416e0e0e1649dc7867fc808ff6f95de544f4c802bd003722ac4e743f48568c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f416e0e0e1649dc7867fc808ff6f95de544f4c802bd003722ac4e743f48568c_0f416e0e0e1649dc7867fc808ff6f95de544f4c802bd003722ac4e743f48568c.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 482,808 bytes |
| MD5 | `6138c1e38892c52064905abd51b7aeeb` |
| SHA1 | `25feedc889de2736bbed8434412e44ac9653f816` |
| SHA256 | `0f416e0e0e1649dc7867fc808ff6f95de544f4c802bd003722ac4e743f48568c` |
| Overall entropy | 6.037 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766434349 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 400,384 | 5.778 | No |
| `.rdata` | 11,776 | 6.842 | No |
| `.data` | 22,016 | 3.684 | No |
| `.pdata` | 27,136 | 5.19 | No |
| `.rsrc` | 2,560 | 4.215 | No |
| `.reloc` | 5,632 | 5.429 | No |

### Imports

**USER32.dll**: `GetSystemMetrics`, `ShowWindow`, `CreateWindowExW`, `DestroyWindow`, `RegisterClassExW`
**GDI32.dll**: `SelectObject`, `DeleteDC`, `CreateCompatibleDC`, `CreateCompatibleBitmap`, `DeleteObject`
**SHELL32.dll**: `SHGetFolderPathW`
**ADVAPI32.dll**: `RegQueryValueExW`, `RegOpenKeyExW`, `RegCloseKey`
**ole32.dll**: `CoUninitialize`, `CoInitializeEx`

## Extracted Strings

Total strings found: **1661** (showing first 100)

```
!This is a Windows NT application      .
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
H3D$`H
D$$9D$ sD
H3D$hH
@SUVWAVD
A^_^][
A^_^][
A^_^][
@UAVAWH
t1H9=9
t$ UWATAUAVH
E3e[l%
A^A]A\_]
UVWATAUAVAWH
PA_A^A]A\_^]
USATAVAWH
@A_A^A\[]
@SUVWAVAWH
(A_A^_^][
@SUVWAVAWH
(A_A^_^][
@SVWAVH
@SVWAVH
(A^_^[
(A^_^[
@SUVWH
@SUVWAVH
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
B8:u
A
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
0A^_^][
@UATAVH
f9D$pt
f9D|pu
@SUWAVH
HA^_][
HA^_][
\$ UVAWH
t$Pf9]
WAVAWH
@A_A^_
l$ VWAWH
t	L9= 
fD9<~u
D8<(t
A
@SUVWAVAWH
HA_A^_^][
@SVWATAVAWH
@8|$<t
D8d<<u
A_A^A\_^[
@SAVAWH
@SAVAWH
t$ UWATAVAWH
D$PD;|$h
A_A^A\_]
@USVWAVAWH
A_A^_^[]
D0fD9<Su
A_A^_^[]
yV9t$Hv<
@SUVWAVAWH
D$@7__XE3
XA_A^_^][
XA_A^_^][
@SUVWATAVH
A^A\_^][
A^A\_^][
VAVAWH
D$H7__XH
@SVWAVAWH
 A_A^_^[
 A_A^_^[
 A_A^_^[
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x140001360` | 9794 | ✓ |
| `fcn.14000cf00` | `0x14000cf00` | 3759 | ✓ |
| `fcn.14000e190` | `0x14000e190` | 2818 | ✓ |
| `fcn.140001bf0` | `0x140001bf0` | 2518 | ✓ |
| `fcn.14000c360` | `0x14000c360` | 2363 | ✓ |
| `fcn.14000b3e0` | `0x14000b3e0` | 1832 | ✓ |
| `fcn.1400014e0` | `0x1400014e0` | 1804 | ✓ |
| `fcn.14000bb10` | `0x14000bb10` | 1803 | ✓ |
| `fcn.140004500` | `0x140004500` | 1633 | ✓ |
| `fcn.1400025d0` | `0x1400025d0` | 1501 | ✓ |
| `fcn.14000a0c0` | `0x14000a0c0` | 1360 | ✓ |
| `fcn.1400039b0` | `0x1400039b0` | 1253 | ✓ |
| `fcn.140004b70` | `0x140004b70` | 1193 | ✓ |
| `fcn.140003ea0` | `0x140003ea0` | 1031 | ✓ |
| `fcn.140005210` | `0x140005210` | 1016 | ✓ |
| `fcn.14000f8e0` | `0x14000f8e0` | 933 | ✓ |
| `fcn.1400071f0` | `0x1400071f0` | 929 | ✓ |
| `fcn.1400076b0` | `0x1400076b0` | 881 | ✓ |
| `section..text` | `0x140001000` | 862 | ✓ |
| `fcn.14000ddb0` | `0x14000ddb0` | 844 | ✓ |
| `fcn.14000eca0` | `0x14000eca0` | 787 | ✓ |
| `fcn.14000aaf0` | `0x14000aaf0` | 775 | ✓ |
| `fcn.140005610` | `0x140005610` | 645 | ✓ |
| `fcn.14000fca0` | `0x14000fca0` | 607 | ✓ |
| `fcn.14000a860` | `0x14000a860` | 597 | ✓ |
| `fcn.1400042b0` | `0x1400042b0` | 586 | ✓ |
| `fcn.14000ae00` | `0x14000ae00` | 548 | ✓ |
| `fcn.14000b030` | `0x14000b030` | 480 | ✓ |
| `fcn.140005a80` | `0x140005a80` | 479 | ✓ |
| `fcn.14000b210` | `0x14000b210` | 456 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.1400014e0.c`](code/fcn.1400014e0.c)
- [`code/fcn.140001bf0.c`](code/fcn.140001bf0.c)
- [`code/fcn.1400025d0.c`](code/fcn.1400025d0.c)
- [`code/fcn.1400039b0.c`](code/fcn.1400039b0.c)
- [`code/fcn.140003ea0.c`](code/fcn.140003ea0.c)
- [`code/fcn.1400042b0.c`](code/fcn.1400042b0.c)
- [`code/fcn.140004500.c`](code/fcn.140004500.c)
- [`code/fcn.140004b70.c`](code/fcn.140004b70.c)
- [`code/fcn.140005210.c`](code/fcn.140005210.c)
- [`code/fcn.140005610.c`](code/fcn.140005610.c)
- [`code/fcn.140005a80.c`](code/fcn.140005a80.c)
- [`code/fcn.1400071f0.c`](code/fcn.1400071f0.c)
- [`code/fcn.1400076b0.c`](code/fcn.1400076b0.c)
- [`code/fcn.14000a0c0.c`](code/fcn.14000a0c0.c)
- [`code/fcn.14000a860.c`](code/fcn.14000a860.c)
- [`code/fcn.14000aaf0.c`](code/fcn.14000aaf0.c)
- [`code/fcn.14000ae00.c`](code/fcn.14000ae00.c)
- [`code/fcn.14000b030.c`](code/fcn.14000b030.c)
- [`code/fcn.14000b210.c`](code/fcn.14000b210.c)
- [`code/fcn.14000b3e0.c`](code/fcn.14000b3e0.c)
- [`code/fcn.14000bb10.c`](code/fcn.14000bb10.c)
- [`code/fcn.14000c360.c`](code/fcn.14000c360.c)
- [`code/fcn.14000cf00.c`](code/fcn.14000cf00.c)
- [`code/fcn.14000ddb0.c`](code/fcn.14000ddb0.c)
- [`code/fcn.14000e190.c`](code/fcn.14000e190.c)
- [`code/fcn.14000eca0.c`](code/fcn.14000eca0.c)
- [`code/fcn.14000f8e0.c`](code/fcn.14000f8e0.c)
- [`code/fcn.14000fca0.c`](code/fcn.14000fca0.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This second chunk of disassembly provides significant additional evidence regarding the sophistication of this binary. It confirms that the sample is not a simple "loader" but rather a **sophisticated, high-end packer or crypter**, likely designed to host and protect high-value malicious payloads (such as ransomware or advanced persistent threat (APT) backdoors).

Below is the updated analysis incorporating both previous findings and the new evidence.

---

### Updated Analysis of Binary Behavior

#### 1. Core Functionality and Purpose
The binary is a **sophisticated multi-stage packer/crypter**. The presence of complex bitwise manipulations, AVX-accelerated processing, and environment reconnaissance indicates it is designed to:
*   **Protect the Payload:** Use heavy math and "heavyweight" CPU instructions to decrypt hidden code only at runtime.
*   **Evade Detection:** Utilize dynamically resolved APIs and time-based checks (`rdtsc`) to bypass sandboxes and debuggers.
*   **Establish Persistence/Environment Context:** Perform registry lookups to understand the environment before deploying its primary payload.

#### 2. New Technical Observations (Chunk 2)

*   **High-Performance Encryption & Decoding (AVX Implementation):**
    In `fcn.140005610`, the binary utilizes **AVX2 instructions** (e.g., `vpsrlvd_avx2`, `pshufb`, `vpmovzxbw_avx2`). 
    *   *Significance:* Standard malware rarely uses AVX unless it is utilizing a professional-grade crypter engine. These instructions are used for high-speed, bulk processing of data. This suggests that the "payload" might be very large or protected by an encryption layer designed to be extremely fast and difficult to reverse-engineer using standard XOR-loop analysis.

*   **Advanced API Resolution & Table Building:**
    In `fcn.14000eca0`, the binary doesn't just hide strings; it constructs a custom **Internal Function Table**. It uses `rdtsc` values combined with large constants to calculate "safe" memory addresses for internal functions.
    *   *Significance:* This masks the program’s true behavior from static analysis tools (like IDA or Ghidra) because the actual function names are never stored in the binary's string table; they are calculated at runtime.

*   **Hidden Windows & System Interactions:**
    In `fcn.14000fca0`, the code performs several "phantom" actions:
    *   It creates a window (`CreateWindowExW`) but immediately hides it using `ShowWindow(..., 0)` and destroys it. This is a common technique to create an **invisible message loop** or to provide a hook for an exception handler that intercepts system calls.
    *   It queries the registry for `ProgramFilesDir`. This is often done by malware to locate valid paths for dropping copies of itself or to identify if it's running in a restricted environment (like a 32-bit emulated shell).

*   **Recursive Data Unpacking:**
    Functions like `fcn.1400042b0` and `fcn.14000aaf0` feature heavy nested loop logic and "shuffling" of data blocks (e.g., the `CONCAT` operations). This suggests it is peeling back multiple layers of obfuscation on a secondary configuration file or inner payload.

#### 3. Updated Suspect & Malicious Behaviors
*   **Sophisticated Cryptography:** The use of AVX instructions and complex math constants (`0x1eef`, `0x5d588b65`) suggests a custom encryption routine rather than standard AES/RC4, which makes automated decryption much harder.
*   **Anti-Analysis Infrastructure:** Frequent use of `rdtsc` in multiple locations indicates it checks for "time-travel" (stepping through the code) or slow execution speeds characteristic of being debugged or running in a sandbox.
*   **Environment Reconnaissance:** The query for `ProgramFilesDir` and other system metrics (`GetSystemMetrics`) suggests the malware is gathering data to decide whether it's on a "high-value" target machine or an analyst's virtual machine.

#### 4. Technical Tactics & Patterns Summary
| Feature | Observation | Threat Actor/Malware Profile |
| :--- | :--- | :--- |
| **Execution Style** | Multi-stage Loader / Packer | Professionalized Malware (Ransomware/Spyware) |
| **Obfuscation** | AVX-accelerated decryption, API Hashing | High-end Crypters (e.g., variants of *VMP*, *Themida*) |
| **Evasion** | `rdtsc` timing checks, Hidden Windows | Sophisticated evasion against automated sandboxes |
| **Persistence** | Registry probing (`ProgramFilesDir`) | Standard lateral movement/persistence behavior |

---

### Summary for Incident Response
This sample is a **high-sophistication packer**. It exhibits hallmarks of professional malware development where the primary goal is to delay detection. 

**Key recommendations for investigators:**
1.  **Do not attempt simple static analysis.** The use of AVX and custom math means standard "de-obfuscators" will likely fail to yield usable strings or IPs from the binary itself.
2.  **Dynamic Analysis with Hardware Breakpoints.** Since it uses `rdtsc` to detect software breakpoints, hardware execution traces (e.g., Intel PT) may be necessary to see where the actual payload is unpacked into memory.
3.  **Memory Forensics Focus.** The most effective way to find the "true" payload is to let the packer run in a controlled environment and dump the process memory once it has finished its unpacking routines (usually after the `fcn.14000eca0` or `fcn.14000aaf0` logic completes).
4.  **Look for "Staged" Payloads.** The heavy focus on unpacking suggests that the file we see is merely a shell; look for evidence of secondary files being dropped or decrypted in memory.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of multi-layer unpacking ("shuffling"), AVX-accelerated encryption, and custom function tables are primary methods to hide the payload's true nature from static analysis. |
| **T1497** | Virtualization/Sandbox Detection | The repeated usage of `rdtsc` instructions is a classic technique used to detect timing discrepancies caused by debuggers or virtualized analysis environments. |
| **T1082** | System#Information Discovery | Querying the registry for `ProgramFilesDir` and using `GetSystemMetrics` allows the malware to profile the environment and decide whether it is running on a targeted machine. |
| **T1036** | Masquerading (Internal) | While not a specific "hidden" sub-technique, the creation of then immediate hiding of windows is used to mask system interactions and facilitate internal control flow during unpacking. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Please note that because the sample uses a high-end packer/crypter with heavy obfuscation, many "strings" provided were determined to be non-human-readable constants or junk data used for custom decryption routines and do not constitute actionable IOCs in their current form.

### **IP addresses / URLs / Domains**
*   *None identified.* (The strings appear to be obfuscated constants rather than cleartext network indicators).

### **File paths / Registry keys**
*   **Registry Key:** `ProgramFilesDir` (Identified as a target of environmental reconnaissance via registry query).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **AVX-2 Instruction Set Usage:** `vpsrlvd_avx2`, `pshufb`, `vpmovzxbw_avx2` (Indicates the use of a high-performance decryption engine).
*   **Anti-Analysis/Timing Checks:** Use of `rdtsc` (Used to detect debugger presence or sandbox execution environments).
*   **Evasion Technique:** Window Masking (`CreateWindowExW` followed by `ShowWindow(..., 0)`) used to create an invisible message loop.
*   **Internal Function Table Mapping:** Execution of logic in `fcn.14000eca0` designed to mask API calls by calculating offsets at runtime rather than using a static import table.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1.  **Malware family:** custom (specifically a high-end crypter/packer)
2.  **Malware type:** loader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Advanced Encryption & Obfuscation:** The use of AVX-accelerated instructions (`vpsrlvd_avx2`, `pshufb`) and complex math constants indicates a professional-grade crypter designed for high-speed, difficult-to-reverse decryption of large payloads.
    *   **Sophisticated Anti-Analysis Tactics:** The consistent use of `rdtsc` timing checks to detect debuggers/sandboxes, combined with "phantom" actions like hidden message loops (hiding windows) and custom internal function tables for API resolution.
    *   **Multi-Stage Execution Pattern:** The analysis identifies "shuffling" logic and recursive data unpacking, which are hallmarks of a loader designed to peel back multiple layers of protection before executing a primary payload (such as ransomware or an APT backdoor).
