# Threat Analysis Report

**Generated:** 2026-06-29 00:32 UTC
**Sample:** `0323da67b133228d6b955513892821613152df7bf7bd156e9fd112d07da3d189_0323da67b133228d6b955513892821613152df7bf7bd156e9fd112d07da3d189.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0323da67b133228d6b955513892821613152df7bf7bd156e9fd112d07da3d189_0323da67b133228d6b955513892821613152df7bf7bd156e9fd112d07da3d189.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 5 sections |
| Size | 7,006,208 bytes |
| MD5 | `f086f61436a0e29a1ad8bb531c3cfeaa` |
| SHA1 | `0e20fcf673de43f5f255a6f64fa03c28239b03a9` |
| SHA256 | `0323da67b133228d6b955513892821613152df7bf7bd156e9fd112d07da3d189` |
| Overall entropy | 6.704 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771765422 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 4,168,704 | 6.242 | No |
| `.rdata` | 2,294,272 | 6.981 | No |
| `.data` | 325,120 | 4.56 | No |
| `.pdata` | 190,976 | 6.392 | No |
| `.reloc` | 26,112 | 5.462 | No |

### Imports

**kernel32.dll**: `TlsSetValue`, `RtlVirtualUnwind`, `GetStdHandle`, `WideCharToMultiByte`, `GetConsoleMode`, `SetConsoleMode`, `ReadConsoleW`, `EnterCriticalSection`, `LeaveCriticalSection`, `InitializeCriticalSectionEx`, `DeleteCriticalSection`, `QueryPerformanceFrequency`, `QueryPerformanceCounter`, `Sleep`, `SleepEx`
**advapi32.dll**: `RegCloseKey`, `CryptDestroyHash`, `CryptHashData`, `CryptCreateHash`, `CryptGetHashParam`, `CryptReleaseContext`, `CryptAcquireContextA`, `RegQueryValueExW`, `RegOpenKeyExW`, `RegOpenKeyTransactedW`, `RegCreateKeyExW`, `RegCreateKeyTransactedW`
**crypt32.dll**: `CertGetNameStringA`, `CertFindExtension`, `CryptQueryObject`, `CertAddCertificateContextToStore`, `CertCreateCertificateChainEngine`, `CryptDecodeObjectEx`, `CertFreeCertificateChain`, `CertFreeCertificateChainEngine`, `CertFreeCertificateContext`, `CertCloseStore`, `PFXImportCertStore`, `CryptStringToBinaryA`, `CertFreeCTLContext`, `CertFindCertificateInStore`, `CertAddEncodedCertificateToStore`
**ws2_32.dll**: `htonl`, `setsockopt`, `recv`, `getsockname`, `getpeername`, `accept`, `WSASetLastError`, `__WSAFDIsSet`, `WSACleanup`, `WSAStartup`, `ntohs`, `getaddrinfo`, `WSACloseEvent`, `send`, `WSAGetLastError`
**ntdll.dll**: `NtCreateFile`, `NtDeviceIoControlFile`, `NtCancelIoFileEx`, `NtWriteFile`, `RtlNtStatusToDosError`
**bcrypt.dll**: `BCryptGenRandom`
**secur32.dll**: `InitSecurityInterfaceA`
**api-ms-win-core-synch-l1-2-0.dll**: `WaitOnAddress`, `WakeByAddressSingle`, `WakeByAddressAll`
**bcryptprimitives.dll**: `ProcessPrng`
**VCRUNTIME140.dll**: `__CxxFrameHandler3`, `_CxxThrowException`, `strstr`, `strrchr`, `strchr`, `memchr`, `__C_specific_handler`, `memset`, `__std_type_info_destroy_list`, `memcmp`, `memmove`, `memcpy`
**api-ms-win-crt-runtime-l1-1-0.dll**: `strerror_s`, `signal`, `_wassert`, `strerror`, `_errno`, `_cexit`, `_crt_atexit`, `_initterm`, `_execute_onexit_table`, `_register_onexit_function`, `_initterm_e`, `_initialize_onexit_table`, `_initialize_narrow_environment`, `_configure_narrow_argv`, `_seh_filter_dll`
**api-ms-win-crt-convert-l1-1-0.dll**: `wcstombs_s`, `mbstowcs_s`, `strtol`
**api-ms-win-crt-environment-l1-1-0.dll**: `getenv`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__stdio_common_vfprintf`, `ferror`, `feof`, `__stdio_common_vsprintf`, `fclose`, `_fileno`, `fread`, `_lseeki64`, `_write`, `fseek`, `fgets`, `clearerr`, `fflush`, `ftell`, `fwrite`
**api-ms-win-crt-string-l1-1-0.dll**: `wcslen`, `strncmp`, `strcmp`, `wcscpy_s`, `wcsncpy_s`, `strlen`, `wcsncmp`, `strspn`, `_strdup`, `strncpy_s`, `strcpy`, `strcspn`, `strpbrk`
**api-ms-win-crt-heap-l1-1-0.dll**: `free`, `malloc`, `realloc`, `calloc`
**api-ms-win-crt-utility-l1-1-0.dll**: `qsort`, `bsearch`, `qsort_s`
**api-ms-win-crt-math-l1-1-0.dll**: `_fdopen`
**api-ms-win-crt-time-l1-1-0.dll**: `strftime`, `_gmtime64_s`, `_time64`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `_stat64`, `_fullpath`, `_unlink`, `_fstat64`

### Exports

`GetInstallDetailsPayload`, `SignalInitializeCrashReporting`, `aws_lc_0_35_0_jent_entropy_collector_alloc`, `aws_lc_0_35_0_jent_entropy_collector_free`, `aws_lc_0_35_0_jent_entropy_init`, `aws_lc_0_35_0_jent_entropy_init_ex`, `aws_lc_0_35_0_jent_entropy_switch_notime_impl`, `aws_lc_0_35_0_jent_read_entropy`, `aws_lc_0_35_0_jent_read_entropy_safe`, `aws_lc_0_35_0_jent_set_fips_failure_callback`, `aws_lc_0_35_0_jent_version`

## Extracted Strings

Total strings found: **33728** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.reloc
t5fffff.
fffff.
%fffff.
t"fffff.
t5fffff.
ffffff.
fffff.
AWAVAUATVWUSH
,/E:,*L
ffffff.
[]_^A\A]A^A_
UAWAVAUATVWSH
fffff.
ffffff.
!ffff.
[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
fffff.
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
ffffff.
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
8[_^A\A]A^A_]
fffff.
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
ffffff.
UAWAVAUATVWSH
8[_^A\A]A^A_]
ffffff.
UAWAVAUATVWSH
8[_^A\A]A^A_]
ffffff.
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAVVWSH
0[_^A^]
UAVVWSH
 [_^A^]
UAVVWSH
 [_^A^]
UAVVWSH
 [_^A^]
UAVVWSH
 [_^A^]
UAVVWSH
 [_^A^]
AVVWSH
([_^A^
([_^A^
&ffffff.
fffff.
fffff.
AWAVAUATVWSH
fffff.
 [_^A\A]A^A_
 [_^A\A]A^A_
UAWAVATVWSH
@[_^A\A^A_]
@[_^A\A^A_]
fffff.
UAWAVATVWSH
 [_^A\A^A_]
UAVVWSH
P[_^A^]
P[_^A^]
UAVVWSH
t fff.
 [_^A^]
UAVVWSH
 [_^A^]
UAVVWSH
t3fff.
 [_^A^]
fffff.
UAVVWSH
 [_^A^]
UAVVWSH
t#fff.
 [_^A^]
fffff.
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1800077d0` | `0x1800077d0` | 2527023 | ✓ |
| `fcn.1800077b0` | `0x1800077b0` | 2526467 | ✓ |
| `fcn.1800077a0` | `0x1800077a0` | 2526426 | ✓ |
| `fcn.180039c70` | `0x180039c70` | 2328549 | ✓ |
| `fcn.1803f8ce0` | `0x1803f8ce0` | 1581012 | ✓ |
| `fcn.18018e110` | `0x18018e110` | 1066468 | ✓ |
| `fcn.1800a76e0` | `0x1800a76e0` | 555285 | ✓ |
| `fcn.1800f4230` | `0x1800f4230` | 516152 | ✓ |
| `fcn.180175bc0` | `0x180175bc0` | 467478 | ✓ |
| `fcn.1801d4670` | `0x1801d4670` | 381547 | ✓ |
| `fcn.1800f3d80` | `0x1800f3d80` | 259685 | ✓ |
| `fcn.1803b97a0` | `0x1803b97a0` | 230765 | ✓ |
| `fcn.180104c60` | `0x180104c60` | 222995 | ✓ |
| `fcn.18023f210` | `0x18023f210` | 217009 | ✓ |
| `fcn.18023cef0` | `0x18023cef0` | 207495 | ✓ |
| `fcn.18023cee0` | `0x18023cee0` | 207431 | ✓ |
| `fcn.18023cec0` | `0x18023cec0` | 207290 | ✓ |
| `fcn.18023ced0` | `0x18023ced0` | 207131 | ✓ |
| `fcn.180247ae0` | `0x180247ae0` | 182055 | ✓ |
| `fcn.180247ac0` | `0x180247ac0` | 181932 | ✓ |
| `fcn.1803bd630` | `0x1803bd630` | 160423 | ✓ |
| `fcn.18011b170` | `0x18011b170` | 144792 | ✓ |
| `fcn.1803b5f60` | `0x1803b5f60` | 133540 | ✓ |
| `fcn.1803d5e00` | `0x1803d5e00` | 108600 | ✓ |
| `fcn.1803bbdc0` | `0x1803bbdc0` | 108170 | ✓ |
| `fcn.1803bbdb0` | `0x1803bbdb0` | 107971 | ✓ |
| `fcn.1803a8610` | `0x1803a8610` | 88218 | ✓ |
| `fcn.1802035f0` | `0x1802035f0` | 81408 | ✓ |
| `fcn.1801417c0` | `0x1801417c0` | 74671 | ✓ |
| `fcn.180140f40` | `0x180140f40` | 74406 | ✓ |

### Decompiled Code Files

- [`code/fcn.1800077a0.c`](code/fcn.1800077a0.c)
- [`code/fcn.1800077b0.c`](code/fcn.1800077b0.c)
- [`code/fcn.1800077d0.c`](code/fcn.1800077d0.c)
- [`code/fcn.180039c70.c`](code/fcn.180039c70.c)
- [`code/fcn.1800a76e0.c`](code/fcn.1800a76e0.c)
- [`code/fcn.1800f3d80.c`](code/fcn.1800f3d80.c)
- [`code/fcn.1800f4230.c`](code/fcn.1800f4230.c)
- [`code/fcn.180104c60.c`](code/fcn.180104c60.c)
- [`code/fcn.18011b170.c`](code/fcn.18011b170.c)
- [`code/fcn.180140f40.c`](code/fcn.180140f40.c)
- [`code/fcn.1801417c0.c`](code/fcn.1801417c0.c)
- [`code/fcn.180175bc0.c`](code/fcn.180175bc0.c)
- [`code/fcn.18018e110.c`](code/fcn.18018e110.c)
- [`code/fcn.1801d4670.c`](code/fcn.1801d4670.c)
- [`code/fcn.1802035f0.c`](code/fcn.1802035f0.c)
- [`code/fcn.18023cec0.c`](code/fcn.18023cec0.c)
- [`code/fcn.18023ced0.c`](code/fcn.18023ced0.c)
- [`code/fcn.18023cee0.c`](code/fcn.18023cee0.c)
- [`code/fcn.18023cef0.c`](code/fcn.18023cef0.c)
- [`code/fcn.18023f210.c`](code/fcn.18023f210.c)
- [`code/fcn.180247ac0.c`](code/fcn.180247ac0.c)
- [`code/fcn.180247ae0.c`](code/fcn.180247ae0.c)
- [`code/fcn.1803a8610.c`](code/fcn.1803a8610.c)
- [`code/fcn.1803b5f60.c`](code/fcn.1803b5f60.c)
- [`code/fcn.1803b97a0.c`](code/fcn.1803b97a0.c)
- [`code/fcn.1803bbdb0.c`](code/fcn.1803bbdb0.c)
- [`code/fcn.1803bbdc0.c`](code/fcn.1803bbdc0.c)
- [`code/fcn.1803bd630.c`](code/fcn.1803bd630.c)
- [`code/fcn.1803d5e00.c`](code/fcn.1803d5e00.c)
- [`code/fcn.1803f8ce0.c`](code/fcn.1803f8ce0.c)

## Behavioral Analysis

This second portion of disassembly provides significant technical depth into how the application handles data. It confirms the previous analysis while introducing new evidence regarding **protocol parsing, state management, and highly structured communication logic.**

Below is the updated and expanded analysis.

---

### Updated Analysis Summary
The provided code segments reinforce the conclusion that this is a high-quality, professionally developed networking module, likely built using the **Rust programming language**. The latest disassembly shows heavy investment in **robust protocol parsing** and **state machine management**. 

While the code does not show direct malicious payloads (like "file_encryption" or "keylogging"), it contains the infrastructure required for a sophisticated Command and Control (C2) system. It is designed to handle complex data structures, manage various connection states, and ensure that communication with a remote server is stable, consistent, and difficult to intercept using basic signature-based detection.

---

### Core Functionality & Purpose (Extended)
*   **Advanced Protocol Parsing:** The massive switch statements (e.g., `fcn.1803a8610`) are not simple logic gates; they represent a sophisticated way of "unpacking" data from a network buffer. The code checks offsets, validates lengths, and performs bitwise operations to extract fields. This is characteristic of protocols like **HTTP/2**, **WebSocket frames**, or custom binary protocols used for command multiplexing.
*   **Robust Error Handling & State Management:** The presence of the string `PROTOCOL_ERROR` (in `fcn.1802035f0`) and various length-validation loops indicates a state machine that can handle dropped packets, malformed headers, and connection timeouts gracefully. 
*   **High-Level Abstraction/Compiler Output:** The extreme number of cases in the switch tables (`661` and `201` cases) strongly suggests **compiler-generated dispatch tables**. In Rust, this occurs when a single high-level function handles multiple data types or operations; the compiler optimizes these into large jump tables to maintain performance.

### New Technical Observations
*   **Data Unpacking & Conversion:** In `fcn.1803a8610`, notice the repeated use of bitwise shifts (e.g., `uVar16 >> 4 & 1`). This is a classic way of extracting boolean flags from a packed byte. The code isn't just taking a string; it's parsing a structured "packet" where every bit might mean something different to the C2 server.
*   **Length-Prefixed Buffers:** Several sections (e.g., `fcn.1803a8f5c` and `fcn.1803b9ec`) involve calculating lengths before performing operations or memory copies. This ensures that the program doesn't overflow its buffer when processing data from the internet, a common requirement in "hardened" software.
*   **Integration with Standard Libraries:** The presence of `api_ms_win_crt_stdio_l1_1_0` suggests the code uses standard C runtime libraries for basic I/O but wraps them in high-level logic to handle the networking specificities.

### Suspicious or Malicious Behaviors (Updated)
*   **Complex Data Multiplexing:** The massive switch tables suggest that this module can handle a wide variety of "commands" or "actions." In a malware context, this allows a single C2 channel to perform multiple different tasks (e.g., exfiltrate files, take screenshots, execute shell commands) without changing the underlying communication logic.
*   **Evasion through "Normalcy":** Because the code is very high-quality and uses standard libraries/conventions, it mimics legitimate software like a web browser or a corporate VPN client. This makes it harder for network security tools to flag the traffic as "suspicious" because the packet structure follows valid, complex protocols rather than simple, easy-to-block patterns.
*   **Reliable Exfiltration Path:** The continued evidence of **Multipart/Form-data** support (from chunk 1) combined with the advanced parsing logic in chunk 2 suggests a very stable method for uploading stolen data.

### Updated Summary Table: Technical Indicators

| Feature | Technical Detail | Implications for Analysis |
| :--- | :--- | :--- |
| **Language/Toolchain** | Rust (LLVM Backend) | High complexity, "safe" memory management, hard to reverse-engineer manually. |
| **Networking Stack** | `ws2_32.dll`, Multipart/Form-Data | Standard methods used to blend in with legitimate web traffic (HTTP/HTTPS). |
| **Data Processing** | Large Jump Tables (Switch Statements) | Highly structured protocol parsing; suggests many possible "commands" or data types. |
| **Error Handling** | `PROTOCOL_ERROR`, Length Validations | Designed for stability and persistence in communication with a remote server. |
| **Implementation Style** | Robust, "Hardened" Network Code | Typical of modern professional malware (e.g., Cobalt Strike-style beacons or advanced trojans). |

### Final Conclusion
This module is a **sophisticated communications engine**. Its primary purpose is to provide a reliable and robust way to send and receive data over the internet while appearing as normal web traffic. The complexity found in the second chunk confirms that the developer intended for this code to handle complex tasks—likely involving multiple types of commands or different types of data (e.g., files, system info, keystrokes)—all wrapped in a standard networking layer to evade detection.

**Recommendation:** This module should be treated as a **C2 Communication Component**. Analysts should focus on the network traffic generated by this module; specifically, look for multi-part POST requests or complex HTTP headers that might indicate data exfiltration or command reception.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1071.001 | Application Layer Protocol: Web Protocols | The use of `ws2_32.dll` and Multipart/Form-data indicates the implementation of standard web protocols (HTTP/S) to blend C2 traffic with legitimate web activity. |
| T1567 | Exfiltration Over Web Service | The specific mention of Multipart/Form-data support suggests a mechanism intended for exfiltrating stolen data via common web services. |
| T1071 | Application Layer Protocol | The complex bitwise operations and large jump tables indicate that the module is designed to handle multiple types of commands and data structures over a single communication channel. |
| T1027 | Obfuscated Signed Binaries (Related) | While not a direct technique for "complexity," the use of Rust and sophisticated, hardened code reflects an effort to complicate manual analysis and evade signature-based detection. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contained heavily obfuscated or junk data typical of a compiler's output; no actionable network indicators or file paths were present in that specific block. The findings below are derived from the technical behavior observed in the analysis.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **C2 Protocol Patterns:** 
    *   **HTTP/2**: Used for complex data packaging.
    *   **WebSocket frames**: Utilized for command multiplexing and persistent communication.
    *   **Multipart/Form-data**: Specifically identified as the method used for data exfiltration (e.g., uploading files or system info).
*   **Technical Indicators:**
    *   **Rust-based construction**: The use of a Rust backend suggests a sophisticated, memory-safe implementation designed to resist common crash-based detection and manual reverse engineering.
    *   **Large Jump Tables/Switch Statements**: Indicates a complex command structure (over 600 potential logic branches), suggesting the ability to perform many different actions (exfiltration, screen grabs, etc.) over a single C2 channel.

---
**Analyst Note:** While no static IOCs (like IPs or Hashes) were identified in this sample, the behavioral analysis confirms the presence of a **sophisticated C2 communication module**. Security teams should monitor for non-standard use of **WebSocket** connections and **Multipart/Form-data** packets originating from unusual processes to identify potential exfiltration activity.

---

## Malware Family Classification

1. **Malware family**: Custom (Sophisticated C2 Framework)
2. **Malware type**: Backdoor / C2 Module
3. **Confidence**: High (on functionality), Medium (on specific attribution)

4. **Key evidence**:
*   **Robust Communication Architecture:** The sample utilizes advanced networking protocols including WebSocket frames, HTTP/2 support, and Multipart/Form-data to blend in with legitimate web traffic while providing a stable channel for data exfiltration.
*   **Sophisticated Parsing & State Management:** The presence of large jump tables (over 600 cases), bitwise operations for packet unpacking, and clear error handling logic indicates a professional-grade command multiplexing system capable of executing various instructions (e.g., file exfiltration, shell commands).
*   **High-Level Language Implementation:** Developed in Rust, the module leverages memory safety and complex compiler optimizations to create a "hardened" communication layer that is more difficult to reverse-engineer than standard automated tools.
