# Threat Analysis Report

**Generated:** 2026-09-07 21:46 UTC
**Sample:** `1582320a0c27d70bde7a97cbe53682dab83efc95124f5e2449bd066960c7e5b9_1582320a0c27d70bde7a97cbe53682dab83efc95124f5e2449bd066960c7e5b9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1582320a0c27d70bde7a97cbe53682dab83efc95124f5e2449bd066960c7e5b9_1582320a0c27d70bde7a97cbe53682dab83efc95124f5e2449bd066960c7e5b9.exe` |
| File type | PE32 executable for MS Windows 6.00 (console), Intel i386, 6 sections |
| Size | 240,128 bytes |
| MD5 | `0eb3bce50d5ec62dbca9ba8787c8206d` |
| SHA1 | `cb09ebd296e08054283dcb81a6c75cd07cfbab7d` |
| SHA256 | `1582320a0c27d70bde7a97cbe53682dab83efc95124f5e2449bd066960c7e5b9` |
| Overall entropy | 6.481 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1752180550 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 159,744 | 6.645 | No |
| `.rdata` | 61,952 | 5.129 | No |
| `.data` | 4,608 | 3.526 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 8,192 | 6.52 | No |
| `.config` | 4,096 | 5.124 | No |

### Imports

**ADVAPI32.dll**: `BackupEventLogW`, `CloseEventLog`, `OpenEventLogW`, `OpenProcessToken`, `AdjustTokenPrivileges`, `DuplicateTokenEx`, `GetTokenInformation`, `ImpersonateLoggedOnUser`, `RevertToSelf`, `LookupPrivilegeValueW`, `CloseServiceHandle`, `ClearEventLogW`, `DeleteService`, `OpenSCManagerA`, `OpenSCManagerW`
**USER32.dll**: `wsprintfW`
**SHELL32.dll**: `SHChangeNotify`
**WS2_32.dll**: `inet_addr`, `WSAStartup`, `InetNtopW`, `WSACleanup`, `inet_ntop`
**IPHLPAPI.DLL**: `IcmpSendEcho`, `IcmpCloseHandle`, `IcmpCreateFile`, `GetAdaptersAddresses`
**NETAPI32.dll**: `NetApiBufferFree`, `NetShareEnum`
**MPR.dll**: `WNetAddConnection2W`, `WNetCancelConnection2W`
**WINSPOOL.DRV**: `WritePrinter`, `EndDocPrinter`, `StartDocPrinterW`, `OpenPrinterW`, `EnumPrintersW`, `StartPagePrinter`, `EndPagePrinter`, `ClosePrinter`
**Secur32.dll**: `GetUserNameExW`
**DNSAPI.dll**: `DnsFree`, `DnsQuery_W`
**ACTIVEDS.dll**: `ord_3`
**ole32.dll**: `CoInitialize`, `CoUninitialize`
**OLEAUT32.dll**: `VariantInit`, `VariantClear`
**ntdll.dll**: `NtRemoveIoCompletion`, `NtSetIoCompletion`, `NtDelayExecution`, `RtlUnwind`
**KERNEL32.dll**: `GetCPInfo`, `GetEnvironmentStringsW`, `FreeEnvironmentStringsW`, `HeapReAlloc`, `GetOEMCP`, `GetACP`, `IsValidCodePage`, `FindFirstFileExW`, `GetStringTypeW`, `GetConsoleMode`, `GetConsoleOutputCP`, `FlushFileBuffers`, `LCMapStringW`, `CompareStringW`, `VirtualProtect`

## Extracted Strings

Total strings found: **784** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.fptable
.reloc
B.config
D$tj.P
D$|j P
D$(QQQPW
L$0PQW
D$<PhX
.conu

D$HWh0
j2j$Sj
D$$SPh4
L$@_^][3
L$ _^][3
h7ov8W
L$LQPVj
D$8Pj(
D$<SUVW
D$$Pj$
D$,SUVW
l$$_^U
|$ ;t$
t$(#t$8
D$|QPV
D$<QPV
t$$WPh
D$,Ph`
j2j<Sj
D$ PVW
T$,RhD
T$,Rh8
D$,th
L$lQSP
D$Xj
P
 <yt#<Yt
t$$QPj
t$@1T$X
T$h;t$X
3T$,#T$X3
D$81L$
L$,3L$0#
L$`#L$d3
D$D1L$
D$D1L$
3t$(#L$(#t$03
#D$l#L$
D$D1L$
D$43t$`
D$P1L$
#D$0#L$D3
#D$T3L$T#
D$\1L$
D$01L$
#L$,#D$$3
#D$T3t$T#
l$ #D$L3L$L#L$(3
D$<1L$
D$$1L$
L$ #D$ 
#D$X3t$X#
#L$D#D$
D$0;D$0
D$,;D$,
D$X;D$X
D$8;D$8
D$T;D$T
F 3D$0
F$3D$4
F(3D$8
F,3D$<
F03D$@
F43D$D
F83D$H
D$DjPP
D$DSUV
#L$4#L$8#L$<#
Yt
jV
thLA
J9Mr

5ntel
5Genu
t	f99u
QQSVWd
38_^]
E9xt
&9Gv!8E
j<h@[C
9~v@k
URPQQhP5A
kUQPXY]Y[
jh`\C
Mj0Xj
^8uRQ
j0Z9^4t
^8uRQ
j0Z9^4t
^8uRQ
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `main` | `0x402940` | 6625 | ✓ |
| `fcn.004217a7` | `0x4217a7` | 5326 | ✓ |
| `fcn.00409ed0` | `0x409ed0` | 5308 | ✓ |
| `fcn.00424eb0` | `0x424eb0` | 4019 | ✓ |
| `fcn.0040d760` | `0x40d760` | 3112 | ✓ |
| `fcn.0040beb0` | `0x40beb0` | 2851 | ✓ |
| `fcn.00401b70` | `0x401b70` | 2783 | ✓ |
| `fcn.00405fe0` | `0x405fe0` | 2724 | ✓ |
| `fcn.0040c9e0` | `0x40c9e0` | 2573 | ✓ |
| `fcn.00425c68` | `0x425c68` | 2573 | ✓ |
| `fcn.00410178` | `0x410178` | 1764 | ✓ |
| `fcn.00413e4a` | `0x413e4a` | 1571 | ✓ |
| `fcn.0040e390` | `0x40e390` | 1534 | ✓ |
| `fcn.00409440` | `0x409440` | 1511 | ✓ |
| `fcn.00414eda` | `0x414eda` | 1508 | ✓ |
| `fcn.00408670` | `0x408670` | 1496 | ✓ |
| `fcn.00411900` | `0x411900` | 1396 | ✓ |
| `fcn.0040ed40` | `0x40ed40` | 1395 | ✓ |
| `fcn.00408ed0` | `0x408ed0` | 1391 | ✓ |
| `fcn.00407960` | `0x407960` | 1305 | ✓ |
| `fcn.00417f08` | `0x417f08` | 1297 | ✓ |
| `fcn.004212d0` | `0x4212d0` | 1239 | ✓ |
| `fcn.0040f2c0` | `0x40f2c0` | 1179 | ✓ |
| `fcn.00404bc0` | `0x404bc0` | 1093 | ✓ |
| `fcn.00423fa0` | `0x423fa0` | 1084 | ✓ |
| `fcn.00417ac9` | `0x417ac9` | 1082 | ✓ |
| `fcn.004176d2` | `0x4176d2` | 1010 | ✓ |
| `fcn.00401780` | `0x401780` | 1008 | ✓ |
| `fcn.0041de58` | `0x41de58` | 966 | ✓ |
| `fcn.0040b960` | `0x40b960` | 952 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401780.c`](code/fcn.00401780.c)
- [`code/fcn.00401b70.c`](code/fcn.00401b70.c)
- [`code/fcn.00404bc0.c`](code/fcn.00404bc0.c)
- [`code/fcn.00405fe0.c`](code/fcn.00405fe0.c)
- [`code/fcn.00407960.c`](code/fcn.00407960.c)
- [`code/fcn.00408670.c`](code/fcn.00408670.c)
- [`code/fcn.00408ed0.c`](code/fcn.00408ed0.c)
- [`code/fcn.00409440.c`](code/fcn.00409440.c)
- [`code/fcn.00409ed0.c`](code/fcn.00409ed0.c)
- [`code/fcn.0040b960.c`](code/fcn.0040b960.c)
- [`code/fcn.0040beb0.c`](code/fcn.0040beb0.c)
- [`code/fcn.0040c9e0.c`](code/fcn.0040c9e0.c)
- [`code/fcn.0040d760.c`](code/fcn.0040d760.c)
- [`code/fcn.0040e390.c`](code/fcn.0040e390.c)
- [`code/fcn.0040ed40.c`](code/fcn.0040ed40.c)
- [`code/fcn.0040f2c0.c`](code/fcn.0040f2c0.c)
- [`code/fcn.00410178.c`](code/fcn.00410178.c)
- [`code/fcn.00411900.c`](code/fcn.00411900.c)
- [`code/fcn.00413e4a.c`](code/fcn.00413e4a.c)
- [`code/fcn.00414eda.c`](code/fcn.00414eda.c)
- [`code/fcn.004176d2.c`](code/fcn.004176d2.c)
- [`code/fcn.00417ac9.c`](code/fcn.00417ac9.c)
- [`code/fcn.00417f08.c`](code/fcn.00417f08.c)
- [`code/fcn.0041de58.c`](code/fcn.0041de58.c)
- [`code/fcn.004212d0.c`](code/fcn.004212d0.c)
- [`code/fcn.004217a7.c`](code/fcn.004217a7.c)
- [`code/fcn.00423fa0.c`](code/fcn.00423fa0.c)
- [`code/fcn.00424eb0.c`](code/fcn.00424eb0.c)
- [`code/fcn.00425c68.c`](code/fcn.00425c68.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

This updated analysis incorporates the final chunk of disassembly, which provides deeper insight into the malware's data processing pipeline, its sophisticated approach to managing network resources, and confirms several high-level "enterprise-grade" features.

### Updated Summary of Findings
The final segment of code reinforces the conclusion that this binary is a **high-sophistication enterprise attack tool**. The inclusion of batch processing logic, extensive file system enumeration for network shares, and complex bitwise manipulation routines suggests a design meant to maximize impact across a large corporate infrastructure during a ransomware or data exfiltration campaign.

---

### Updated & New Malicious Behaviors

#### 1. Advanced Network Share Orchestration
The code surrounding the first several functions (including those leading into `fcn.00401780`) reveals how the malware handles networked files:
*   **Batch Processing Logic:** The inclusion of strings like `"processing batch %d-%d of %d shares"` and `"all shares processed"` indicates that the malware is designed to handle hundreds, if not thousands, of network shares simultaneously. This is a hallmark of "Big Game Hunting" (targeting large corporations).
*   **Time Logging for Scanning:** The code tracks and logs the time taken for "network scan completed." This suggests an automated operation where the attacker can monitor progress remotely or simply ensure the malware completes its tasks efficiently without stalling.

#### 2. Systematic File System Exploration (The "Search" Engine)
The function `fcn.00401780` implements a heavy-duty search and discovery routine:
*   **Iterative File Enumeration:** Utilizing `FindFirstFileW` and `FindNextFileW`, the malware crawls through directory structures to find files. 
*   **Targeting Network Resources:** The logic specifically identifies and processes "shares." By targeting shares, the malware aims to encrypt data that is stored on local workstations but is accessible from other machines in the organization (e.g., shared folders, department drives).

#### 3. Sophisticated Data Transformation/Encryption Kernels
The function `fcn.0040b960` contains a complex loop involving bitwise shifts and XOR operations:
*   **Obfuscation or Encryption:** The specific mathematical structure (e.g., `(uVar5 >> 0x12 | uVar5 << 0xe) ^ ...`) is characteristic of **custom stream ciphers** or high-level obfuscation techniques used to de-obfuscate internal configuration tables or instructions on the fly.
*   **Instruction Decoding:** This logic may be part of a "packer" or a custom script interpreter, allowing the malware to receive and execute different commands from its C2 server without needing multiple separate executables.

#### 4. High-Volume Data Handling (The "Mover")
The function `fcn.0041de58` appears to be an optimized I/O routine:
*   **Buffer Management:** It handles large buffer writes and potentially manages data chunks. In the context of ransomware, this is often used to read a file into memory, encrypt it, and then write the encrypted version back out, or to "stream" files to a remote server for exfiltration (Double Extortion).

---

### Updated Technical Indicators

| Feature | Detection / Observation | Significance |
| :--- | :--- | :--- |
| **Batch Processing** | `"processing batch %d-%d of %d shares"` | High-scale automation; designed for large corporate networks. |
| **Timing Logs** | `"network scan completed in ... seconds"` | Orchestrated, professional development (not a script kiddie tool). |
| **Network Share Target** | Logic focusing on "shares" and `FindFirstFileW` loops. | Intent to encrypt/exfiltrate data across the entire organizational network. |
| **Bitwise Transformation** | Complex XOR/Shift operations in `fcn.0040b960`. | Likely a custom encryption routine or a method for unpacking secondary payloads. |
| **Large Buffer Handling** | High-frequency `WriteFile` and buffer management logic. | Indicates capability for mass file modification (Encryption) or data exfiltration. |

---

### Final Threat Profile: **High-Impact Enterprise Ransomware & Extortion Tool**

The analysis of all four segments confirms that this is not a simple "loader" but a sophisticated, multi-stage deployment suite. 

1.  **Discovery Phase:** It maps the Active Directory (AD) and identifies reachable hosts.
2.  **Persistence/Expansion Phase:** It uses `sc` and `schtasks` to ensure it survives reboots and spreads to other machines in the domain.
3.  **Targeting Phase:** It specifically seeks out "shares" and networked storage, ensuring that the impact of encryption is maximized across the organization’s infrastructure.
4.  **Execution/Impact Phase:** It uses complex mathematical routines (likely for encryption) and high-volume I/O handling to process data in batches, ensuring that even a massive amount of corporate data can be systematically encrypted or stolen.

The presence of **PDF generation**, **multi-method persistence**, and **batch processing of network shares** strongly suggests this is a product used by professional threat actors (or a Ransomware-as-a-Service - RaaS - affiliate) capable of paralyzing large organizations.

---

### Recommendation for Defense
*   **Network Segmentation:** Strictly limit the ability of workstation machines to reach out and scan other segments for "shares" unless specifically required.
*   **Monitor Service Creation:** Alert on any `sc` or `schtasks` commands involving non-standard service names or paths involving remote UNC shares (`\\`).
*   **EDR/SIEM Rules:** Monitor for frequent calls to `FindFirstFileW`/`FindNextFileW` across a large number of directories in a short period, especially when followed by high-frequency `WriteFile` operations.
*   **Disable LLMNR/NetBIOS:** Disable legacy protocols that allow for easy network discovery and lateral movement via "reachability" checks.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1083** | File and Directory Discovery | The malware uses `FindFirstFileW` and `FindNextFileW` to systematically crawl directories and identify network shares for targeting. |
| **T1486** | Data Encrypted for Impact | The complex bitwise manipulation and XOR kernels are characteristic of the encryption routines used in ransomware to lock user data. |
| **T1027** | Obfuscated Files or Information | Complex mathematical structures are used for de-obfuscating internal configuration tables and potentially unpacking secondary payloads. |
| **T1053** | Scheduled Task/Job | The analysis confirms the use of `schtasks` to ensure the malware survives reboots and maintains a presence on infected machines. |
| **T1543** | Create or Modify System Process | The utilization of the `sc` command indicates an attempt to create or modify system services for persistence and execution. |
| **T1048** | Exfiltration Over Alternative Protocol | The "Mover" routine and mention of "Double Extortion" suggest that large amounts of data are being streamed to remote servers before encryption. |
| **T1018** | Remote System Discovery | The logic for scanning network shares and identifying available infrastructure indicates an active phase of mapping the internal environment. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*   *None identified.* (The text contains placeholders for LDAP domains and network scanning logic, but no hardcoded IP addresses or specific malicious domains were present.)

### **File paths / Registry keys**
*   *None identified.* (While the analysis mentions targeting "network shares" and "remote UNC shares," no specific file paths or registry keys were provided in the raw strings.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (C2 patterns, system commands, etc.)**
*   **Internal Logging/Status Strings:** 
    *   `processing batch %d-%d of %d shares` (Indicates automated batch processing of network shares)
    *   `all shares processed`
    *   `network scan completed`
*   **Persistence Mechanisms:**
    *   Use of `sc` (Service Control Manager) to create/modify services.
    *   Use of `schtasks` (Scheduled Tasks) for persistence and lateral movement.
*   **Discovery & Enumeration Behavior:**
    *   Utilization of `FindFirstFileW` and `FindNextFileW` for recursive directory crawling and network share identification.
    *   LDAP-based reconnaissance logic (`[+] LDAP domain: %ws`, `Failed to bind to rootDSE`).
*   **Cryptographic/Obfuscation Signatures:** 
    *   Implementation of custom bitwise transformation routines (XOR, shift operations) in `fcn.0040b960`.
    *   High-frequency `WriteFile` calls for mass file modification (encryption or exfiltration).

---

### **Analyst Notes**
While this sample contains very few "static" IOCs (like specific IPs or MD5 hashes), it exhibits high-confidence **behavioral indicators** characteristic of enterprise-grade ransomware and "Big Game Hunting" tactics. 

The presence of **PDF generation** components combined with **multi-method persistence** (`sc`, `schtasks`) and **automated network share scanning** suggests a sophisticated multi-stage deployment suite designed for large-scale encryption and data exfiltration within corporate environments.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `https://www.torproject.org/`

**Domains:**
- `vg6xwkmfyirv3l6qtqus7jykcuvgx6imegb73hqny2avxccnmqt5m2id.onion`

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification:

1. **Malware family:** Custom (likely a RaaS - Ransomware-as-a-Service - affiliate payload)
2. **Malware type:** Ransomware / Extortion Tool
3. **Confidence:** High
4. **Key evidence:**
    *   **Enterprise Targeting ("Big Game Hunting"):** The inclusion of batch processing for network shares and "network scan" logging confirms the tool is designed to automate impact across large corporate infrastructures rather than single machines.
    *   **Encryption & Exfiltration Capabilities:** The presence of complex bitwise transformation routines (XOR/Shift) in `fcn.0040b960` combined with high-volume "Mover" logic identifies it as a primary engine for data encryption and "Double Extortion" exfiltration.
    *   **Sophisticated Persistence & Discovery:** The integration of multiple persistence methods (`sc`, `schtasks`), LDAP-based reconnaissance, and systematic file system crawling demonstrates a professional-grade deployment suite rather than a simple loader or script_kiddie tool.
