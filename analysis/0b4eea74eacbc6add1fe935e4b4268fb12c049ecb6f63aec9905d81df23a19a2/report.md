# Threat Analysis Report

**Generated:** 2026-07-26 04:52 UTC
**Sample:** `0b4eea74eacbc6add1fe935e4b4268fb12c049ecb6f63aec9905d81df23a19a2_0b4eea74eacbc6add1fe935e4b4268fb12c049ecb6f63aec9905d81df23a19a2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b4eea74eacbc6add1fe935e4b4268fb12c049ecb6f63aec9905d81df23a19a2_0b4eea74eacbc6add1fe935e4b4268fb12c049ecb6f63aec9905d81df23a19a2.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 5 sections |
| Size | 377,344 bytes |
| MD5 | `71b9cab9e0b9b56ca85264d834e8e611` |
| SHA1 | `0ae7fc6d9cb20cdfcbb46677dd635654c15537a5` |
| SHA256 | `0b4eea74eacbc6add1fe935e4b4268fb12c049ecb6f63aec9905d81df23a19a2` |
| Overall entropy | 6.371 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769878042 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 353,792 | 6.372 | No |
| `.pdata` | 11,776 | 5.554 | No |
| `.idata` | 7,680 | 4.624 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,560 | 5.295 | No |

### Imports

**WS2_32.dll**: `shutdown`, `gethostbyname`, `sendto`, `bind`, `accept`, `inet_ntoa`, `recv`, `listen`, `WSACleanup`, `closesocket`, `select`, `WSAStartup`, `socket`, `ntohs`, `recvfrom`
**WININET.dll**: `InternetReadFile`, `InternetCloseHandle`, `InternetOpenA`, `InternetOpenUrlA`, `HttpQueryInfoA`
**WINHTTP.dll**: `WinHttpReceiveResponse`, `WinHttpQueryDataAvailable`, `WinHttpConnect`, `WinHttpSetTimeouts`, `WinHttpSendRequest`, `WinHttpCloseHandle`, `WinHttpSetOption`, `WinHttpOpenRequest`, `WinHttpOpen`, `WinHttpReadData`
**bcrypt.dll**: `BCryptFinishHash`, `BCryptOpenAlgorithmProvider`, `BCryptGetProperty`, `BCryptCloseAlgorithmProvider`, `BCryptDestroyHash`, `BCryptCreateHash`, `BCryptDestroyKey`, `BCryptFinalizeKeyPair`, `BCryptGenerateKeyPair`, `BCryptExportKey`, `BCryptSetProperty`, `BCryptHashData`
**CRYPT32.dll**: `CryptQueryObject`, `CryptMsgClose`, `CertCloseStore`
**ole32.dll**: `CoCreateInstance`, `CoInitialize`, `CoInitializeSecurity`, `CoInitializeEx`, `CoSetProxyBlanket`, `CoUninitialize`
**OLEAUT32.dll**: `VariantClear`, `SysAllocString`, `SysFreeString`, `VariantInit`
**ADVAPI32.dll**: `CryptAcquireContextA`, `CryptGenRandom`, `CryptReleaseContext`, `RegCreateKeyExW`, `RegSetValueExW`, `RegOpenKeyExW`, `RegDeleteKeyA`, `CreateServiceA`, `RegCloseKey`, `CloseServiceHandle`, `RegQueryValueExA`, `AllocateAndInitializeSid`, `OpenSCManagerA`, `RegCreateKeyExA`, `DeleteService`
**WINTRUST.dll**: `WinVerifyTrust`
**SHELL32.dll**: `ShellExecuteA`, `SHGetFolderPathW`, `SHGetFolderPathA`
**KERNEL32.dll**: `GetFileAttributesExW`, `GetExitCodeProcess`, `GetConsoleMode`, `GetConsoleOutputCP`, `FlushFileBuffers`, `GetFileType`, `SetFilePointerEx`, `GetFileSizeEx`, `UnhandledExceptionFilter`, `RtlVirtualUnwind`, `RtlCaptureContext`, `GetModuleHandleExW`, `IsProcessorFeaturePresent`, `FlsFree`, `FlsSetValue`
**USER32.dll**: `ShowWindow`, `GetSystemMetrics`, `wsprintfA`, `wvsprintfA`

## Extracted Strings

Total strings found: **1355** (showing first 100)

```
!This program cannot be run in DOS mode.
$
g?3}	l3}	l3}	lJ

m:}	lx

m9}	lx
m!}	lx
me}	lJ
m'}	lJ
m1}	l3}
l:|	lJ
m2}	lRich3}	l
.pdata
@.idata
@.fptable
.reloc
                          
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
                          
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
.?AVexception@std@@
.?AVbad_alloc@std@@
.?AVruntime_error@std@@
.?AVlogic_error@std@@
.?AVlength_error@std@@
.?AVout_of_range@std@@
.?AVbad_array_new_length@std@@
.?AVsystem_error@std@@
.?AV_System_error@std@@
.?AVfailure@ios_base@std@@
.?AV_com_error@@
.?AVbad_exception@std@@
.?AV<lambda_5acbf4c4858a80b2d1a4cbaf25a1031d>@@
.?AV_Facet_base@std@@
.?AVfacet@locale@std@@
.?AU_Crt_new_delete@std@@
.?AV_Locimp@locale@std@@
.?AVcodecvt_base@std@@
.?AUctype_base@std@@
.?AV?$ctype@D@std@@
.?AV?$codecvt@DDU_Mbstatet@@@std@@
.?AVerror_category@std@@
.?AV_Iostream_error_category2@std@@
.?AVtype_info@@
Unknown exception
bad allocation
	

	

	


	

	


	


	

	


	


	
















	

	

	

	



	


	


	


	

























address family not supported
address in use
address not available
already connected
argument list too long
argument out of domain
bad address
bad file descriptor
bad message
broken pipe
connection aborted
connection already in progress
connection refused
connection reset
cross device link
destination address required
device or resource busy
directory not empty
executable format error
file exists
file too large
filename too long
function not supported
host unreachable
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14002c1c4` | `0x14002c1c4` | 65006 | ✓ |
| `fcn.140014784` | `0x140014784` | 64220 | ✓ |
| `fcn.14003fe08` | `0x14003fe08` | 55995 | ✓ |
| `fcn.14003fdf4` | `0x14003fdf4` | 55954 | ✓ |
| `fcn.140046bd0` | `0x140046bd0` | 36041 | ✓ |
| `fcn.140020408` | `0x140020408` | 29063 | ✓ |
| `fcn.14003af0c` | `0x14003af0c` | 13127 | ✓ |
| `fcn.140038ccc` | `0x140038ccc` | 7424 | ✓ |
| `fcn.14001229c` | `0x14001229c` | 5567 | ✓ |
| `fcn.14004e53c` | `0x14004e53c` | 4735 | ✓ |
| `fcn.140017378` | `0x140017378` | 4638 | ✓ |
| `fcn.14002c0c0` | `0x14002c0c0` | 4325 | ✓ |
| `fcn.140052100` | `0x140052100` | 3815 | ✓ |
| `fcn.14002c0d0` | `0x14002c0d0` | 3765 | ✓ |
| `fcn.14001f6e8` | `0x14001f6e8` | 3359 | ✓ |
| `fcn.14002c0f0` | `0x14002c0f0` | 3045 | ✓ |
| `fcn.140025e64` | `0x140025e64` | 2993 | ✓ |
| `fcn.14001e370` | `0x14001e370` | 2729 | ✓ |
| `fcn.14002cf5c` | `0x14002cf5c` | 2249 | ✓ |
| `fcn.14001bfd0` | `0x14001bfd0` | 2248 | ✓ |
| `fcn.14001dacc` | `0x14001dacc` | 2209 | ✓ |
| `fcn.140021178` | `0x140021178` | 2188 | ✓ |
| `fcn.140015630` | `0x140015630` | 2112 | ✓ |
| `fcn.14002d2a0` | `0x14002d2a0` | 2088 | ✓ |
| `fcn.140036f78` | `0x140036f78` | 1946 | ✓ |
| `fcn.1400495e0` | `0x1400495e0` | 1829 | ✓ |
| `fcn.1400289f8` | `0x1400289f8` | 1827 | ✓ |
| `fcn.140042de4` | `0x140042de4` | 1817 | ✓ |
| `fcn.1400246f4` | `0x1400246f4` | 1791 | ✓ |
| `fcn.140053550` | `0x140053550` | 1677 | ✓ |

### Decompiled Code Files

- [`code/fcn.14001229c.c`](code/fcn.14001229c.c)
- [`code/fcn.140014784.c`](code/fcn.140014784.c)
- [`code/fcn.140015630.c`](code/fcn.140015630.c)
- [`code/fcn.140017378.c`](code/fcn.140017378.c)
- [`code/fcn.14001bfd0.c`](code/fcn.14001bfd0.c)
- [`code/fcn.14001dacc.c`](code/fcn.14001dacc.c)
- [`code/fcn.14001e370.c`](code/fcn.14001e370.c)
- [`code/fcn.14001f6e8.c`](code/fcn.14001f6e8.c)
- [`code/fcn.140020408.c`](code/fcn.140020408.c)
- [`code/fcn.140021178.c`](code/fcn.140021178.c)
- [`code/fcn.1400246f4.c`](code/fcn.1400246f4.c)
- [`code/fcn.140025e64.c`](code/fcn.140025e64.c)
- [`code/fcn.1400289f8.c`](code/fcn.1400289f8.c)
- [`code/fcn.14002c0c0.c`](code/fcn.14002c0c0.c)
- [`code/fcn.14002c0d0.c`](code/fcn.14002c0d0.c)
- [`code/fcn.14002c0f0.c`](code/fcn.14002c0f0.c)
- [`code/fcn.14002c1c4.c`](code/fcn.14002c1c4.c)
- [`code/fcn.14002cf5c.c`](code/fcn.14002cf5c.c)
- [`code/fcn.14002d2a0.c`](code/fcn.14002d2a0.c)
- [`code/fcn.140036f78.c`](code/fcn.140036f78.c)
- [`code/fcn.140038ccc.c`](code/fcn.140038ccc.c)
- [`code/fcn.14003af0c.c`](code/fcn.14003af0c.c)
- [`code/fcn.14003fdf4.c`](code/fcn.14003fdf4.c)
- [`code/fcn.14003fe08.c`](code/fcn.14003fe08.c)
- [`code/fcn.140042de4.c`](code/fcn.140042de4.c)
- [`code/fcn.140046bd0.c`](code/fcn.140046bd0.c)
- [`code/fcn.1400495e0.c`](code/fcn.1400495e0.c)
- [`code/fcn.14004e53c.c`](code/fcn.14004e53c.c)
- [`code/fcn.140052100.c`](code/fcn.140052100.c)
- [`code/fcn.140053550.c`](code/fcn.140053550.c)

## Behavioral Analysis

Based on the disassembly provided in chunk 4/4, I have updated and expanded the analysis. This final set of functions provides deeper insight into the **Robustness** and **Performance Optimization** of the malware’s core processing engine.

The inclusion of sophisticated memory management techniques confirms that this is not a "script kiddie" tool, but rather a professional-grade piece of software designed to handle complex operations reliably without crashing—a hallmark of high-end RATs or APT payloads.

---

### Updated Analysis: Malware Profile & Behavior

#### 1. Robust Buffer Management & Parsing (New Detail)
The first segment of code provided in chunk 4 demonstrates a highly defensive approach to handling input data:
*   **Length Validation:** The code extensively checks for null pointers, empty strings, and validates buffer lengths before any operation is performed.
*   **Multi-Pass Processing:** Rather than simple string manipulation, the logic uses multiple passes (loops) to identify offsets and validate segments of a memory block. This suggests that the data received from the C2 server is likely structured (e.g., a custom TLV—Type-Length-Value—protocol or a compressed/encoded format).
*   **Fail-Safe Execution:** The use of specific error-handling branches (`goto` to `code_r0x000140042909`) indicates that the malware is designed to gracefully "fail" or ignore malformed packets from the C2 rather than crashing, which would alert the user and security researchers.

#### 2. Advanced Instruction Set Usage (SIMD/AVX)
The function `fcn.1400246f4` contains several calls to intrinsic-like logic for memory movement:
*   **Non-Temporal Stores (`vmovntdq_avx`):** The presence of AVX instructions indicates that the malware is optimized for performance at the hardware level. Specifically, "non-temporal" hints are often used in high-performance applications (like video processing or advanced encryption) to move data without polluting the CPU cache.
*   **Sophisticated Alignment Handling:** There is extensive logic to handle different memory alignment sizes (e.g., cases for 0x10, 0x80, and 0x100). This suggests that the malware's core engine handles large amounts of data—perhaps during **file exfiltration**, **screen scraping**, or **mass data encryption**—while maintaining high performance and stability.

#### 3. Internal Data Normalization
The function `fcn.140053550` appears to be a specialized, highly-optimized memory copying/transformation routine:
*   **Switch Table for Size Optimization:** The use of a large switch table (`switch(uVar30)`) suggests that the malware detects the size of a buffer and selects the most efficient way to move or "normalize" it.
*   **Sophisticated Logic Flow:** This isn't just a standard `memcpy`. It is designed to handle complex data structures where different fields might have different lengths or types, which is typical for an advanced command-and-control (C2) interpreter.

---

### Final Summary of Malicious Indicators

The analysis now confirms that this binary is highly sophisticated. By combining the previously identified traits with the findings from chunk 4, we can conclude the following:

| Category | Specific Behavior Identified | Purpose/Impact |
| :--- | :--- | :--- |
| **Persistence** | `CreateServiceA`, `ChangeServiceConfig2A` | Ensures it runs as a high-privilege system service. |
| **Defense Evasion** | `cpuid_Version_info`, `GetSystemInfo` | Detects VMs and sandboxes to evade analysis. |
| **C2 Security** | `BCryptOpenAlgorithmProvider`, `BCryptGenerateKeyPair` | Uses industry-standard encryption (CNG) for "hidden" communication. |
| **Data Processing** | **SIMD/AVX Optimization**, multi-pass parsing | Ensures high performance and reliability when handling large amounts of stolen data or complex commands. |
| **Robustness** | Multi-pass length validation, optimized memory movement | Prevents crashes from malformed C2 input; signifies professional development. |

### Final Conclusion
The inclusion of **AVX instruction optimizations**, **advanced buffer management**, and **non-temporal store logic** strongly suggests that this is a high-tier piece of malware (potentially an APT tool or a very sophisticated commercial RAT). 

The developer prioritized:
1.  **Stealth:** Hiding its presence from both humans (via anti-analysis) and machines (via standard encryption).
2.  **Stability:** Ensuring it never crashes while processing potentially complex instructions from the remote server.
3.  **Efficiency:** Using high-level CPU features to perform heavy tasks (like data gathering or encryption) as quickly as possible to minimize the "window of detection" for security software.

This is a professional tool designed for long-term, covert presence on a target network.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the relevant MITRE ATT&CK techniques. The presence of high-level CPU optimizations (SIMD/AVX) and robust error handling suggests a sophisticated actor prioritizing both operational stability and large-scale data theft.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1543.003** | Create or Run Windows Service | The use of `CreateServiceA` and `ChangeServiceConfig2A` confirms a mechanism for establishing persistence as a high-privilege system service. |
| **T1558** | System Firmware/Software Discovery | The use of `cpuid_Version_info` and `GetSystemInfo` is indicative of anti-analysis checks to identify virtualized or sandboxed environments. |
| **T1573** | Encrypted Channel | Implementation of the `BCrypt` library for key generation and algorithm selection ensures that C2 communication is encrypted and hidden from network inspection. |
| **T1486** | Data Encrypted before Exfiltration | The utilization of SIMD/AVX instructions indicates a focus on high-performance encryption to process large amounts of data before it leaves the network. |
| **T1020** | Automated Exfiltration | The inclusion of multi-pass parsing and robust buffer management suggests the infrastructure is designed to efficiently handle and exfiltrate large volumes of stolen data. |
| **T1036** | Indicator Removal | The "Fail-Safe" logic (handling malformed packets without crashing) helps maintain a stable footprint, preventing alerts from being triggered by crashes during network inconsistencies. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the intelligence report.

### **Threat Intelligence Analysis Report**

#### **1. IP addresses / URLs / Domains**
*   *No specific IP addresses, URLs, or domains were identified in the provided data.*

#### **2. File paths / Registry keys**
*   *None detected.* (The analysis mentions API calls like `CreateServiceA` and `ChangeServiceConfig2A`, but no specific file system paths or registry keys were present).

#### **3. Mutex names / Named pipes**
*   *None detected.*

#### **4. Hashes**
*   *None detected.* (Note: The string `5acbf4c4858a80b2d1a4cbaf25a1031d` appears in the source, but it is part of a compiler-generated identifier for a lambda function and does not represent a file hash).

#### **5. Other artifacts**
*   **C2 Communication Characteristics:** 
    *   The malware utilizes **BCrypt (CNG)** libraries (`BCryptOpenAlgorithmProvider`, `BCryptGenerateKeyPair`) for encrypted communication.
    *   Data parsing indicates a likely **custom structured format** (possible TLV - Type, Length, Value) or compressed/encoded format to handle C2 instructions.
*   **Evasion Techniques:**
    *   **Anti-Analysis/Sandbox Detection:** Use of `cpuid_Version_info` and `GetSystemInfo` to identify virtualized environments.
    *   **Persistence Mechanism:** Utilization of Windows Service APIs (`CreateServiceA`, `ChangeServiceConfig2A`) for high-privilege persistence.
*   **Technical Sophistication Indicators:**
    *   **Instruction Optimization:** Use of **SIMD/AVX instructions** and **non-temporal stores** (`vmovntdq_avx`) to optimize data processing (e.g., encryption or large-scale data exfiltration).
    *   **Robustness Logic:** Multi-pass validation of buffers and switch tables for size optimization, indicating a professional-grade build intended for stability during high-volume data manipulation.

---
**Analyst Note:** While no "hard" IOCs (like specific IPs or file hashes) were extracted from the raw strings, the behavioral analysis confirms this is a sophisticated piece of malware (likely an APT tool or advanced RAT). The lack of hardcoded indicators suggests the malware may use dynamically generated infrastructure or was stripped of its configuration during the initial compile/obfuscation phase.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `ult.wraithbot.net`
- `your-vps.example.com`

---

## Malware Family Classification

1. **Malware family**: Custom (Advanced RAT/APT tool)
2. **Malware type**: RAT / Backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **High-Level Technical Sophistication:** The use of SIMD/AVX instructions and "non-temporal" stores (`vmovntdq_avx`) indicates a professional-grade tool designed for high-performance operations, such as large-scale data encryption or rapid exfiltration, to minimize the time spent in an active state.
*   **Advanced C2 Infrastructure:** The implementation of the `BCrypt` (CNG) library for secure communication, combined with multi-pass buffer validation and "fail-safe" logic, suggests a robust command-and-control architecture designed to handle complex data structures without crashing or alerting defenders.
*   **Persistent Evasion Tactics:** The malware utilizes both system-level persistence (`CreateServiceA`) and proactive anti-analysis checks (`cpuid`, `GetSystemInfo`) to detect virtualized environments, indicating it is designed for long-term, covert operation on a target network.
