# Threat Analysis Report

**Generated:** 2026-07-27 15:56 UTC
**Sample:** `0bbe245f57c8b85adda154a8bd1561de4167b1863ea999d4c987b4ce5027d8f6_0bbe245f57c8b85adda154a8bd1561de4167b1863ea999d4c987b4ce5027d8f6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0bbe245f57c8b85adda154a8bd1561de4167b1863ea999d4c987b4ce5027d8f6_0bbe245f57c8b85adda154a8bd1561de4167b1863ea999d4c987b4ce5027d8f6.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 4,557,312 bytes |
| MD5 | `05d5932013d1d1884a6dfb562d8d51fe` |
| SHA1 | `0e32f6b8ad5588703ebdf22b32a6e3e1aa56679c` |
| SHA256 | `0bbe245f57c8b85adda154a8bd1561de4167b1863ea999d4c987b4ce5027d8f6` |
| Overall entropy | 6.529 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774806449 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 2,341,376 | 6.481 | No |
| `.rdata` | 1,546,752 | 6.32 | No |
| `.data` | 422,912 | 3.661 | No |
| `.pdata` | 161,280 | 6.314 | No |
| `.rsrc` | 1,536 | 4.261 | No |
| `.reloc` | 82,432 | 5.459 | No |

### Imports

**ADVAPI32.dll**: `AddMandatoryAce`, `AdjustTokenPrivileges`, `CheckTokenMembership`, `CreateWellKnownSid`, `DeregisterEventSource`, `DuplicateTokenEx`, `EqualSid`, `GetAce`, `GetLengthSid`, `GetSidSubAuthority`, `GetSidSubAuthorityCount`, `GetTokenInformation`, `ImpersonateLoggedOnUser`, `InitializeAcl`, `InitializeSecurityDescriptor`
**bcrypt.dll**: `BCryptGetProperty`, `BCryptGenRandom`, `BCryptFinishHash`, `BCryptExportKey`, `BCryptHashData`, `BCryptOpenAlgorithmProvider`, `BCryptCloseAlgorithmProvider`, `BCryptCreateHash`, `BCryptDestroyKey`, `BCryptDestroyHash`, `BCryptImportKeyPair`
**CRYPT32.dll**: `CertEnumCertificatesInStore`, `CertGetCertificateChain`, `CertFreeCertificateContext`, `CertFreeCertificateChainEngine`, `CryptImportPublicKeyInfoEx2`, `CryptFormatObject`, `CryptFindOIDInfo`, `CryptDecodeObject`, `CertVerifyCertificateChainPolicy`, `CertOpenStore`, `CertNameToStrW`, `CertGetNameStringW`, `CertAddCertificateContextToStore`, `CertAddCertificateLinkToStore`, `CertCloseStore`
**IPHLPAPI.DLL**: `ConvertInterfaceNameToLuidW`, `ConvertInterfaceLuidToIndex`
**KERNEL32.dll**: `InitializeSListHead`, `RtlUnwindEx`, `RtlPcToFileHeader`, `EncodePointer`, `InitializeCriticalSectionAndSpinCount`, `TlsAlloc`, `TlsGetValue`, `TlsSetValue`, `TlsFree`, `CancelIoEx`, `CancelSynchronousIo`, `CancelThreadpoolIo`, `CheckRemoteDebuggerPresent`, `CloseHandle`, `CloseThreadpoolIo`
**ncrypt.dll**: `NCryptGetProperty`, `NCryptDeleteKey`, `NCryptOpenKey`, `NCryptOpenStorageProvider`, `NCryptFreeObject`, `NCryptSetProperty`, `NCryptImportKey`
**ole32.dll**: `CoGetApartmentType`, `CoInitializeEx`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoUninitialize`, `CoWaitForMultipleHandles`, `CoCreateGuid`
**Secur32.dll**: `GetUserNameExW`
**USER32.dll**: `LoadStringW`
**WS2_32.dll**: `getsockopt`, `closesocket`, `bind`, `ioctlsocket`, `WSASocketW`, `WSASend`, `shutdown`, `setsockopt`, `recv`, `select`, `WSAStartup`, `WSAConnect`, `FreeAddrInfoExW`, `FreeAddrInfoW`, `GetAddrInfoExW`
**api-ms-win-crt-heap-l1-1-0.dll**: `_callnewh`, `free`, `calloc`, `_set_new_mode`, `malloc`
**api-ms-win-crt-math-l1-1-0.dll**: `log`, `ceil`, `cos`, `floor`, `__setusermatherr`, `tan`, `modf`, `pow`, `sin`
**api-ms-win-crt-string-l1-1-0.dll**: `strcpy`, `strncpy_s`, `_stricmp`, `strcmp`, `strlen`, `strcpy_s`, `wcsncmp`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__stdio_common_vsscanf`, `__stdio_common_vsprintf_s`, `__stdio_common_vfprintf`, `__acrt_iob_func`, `__stdio_common_vsnprintf_s`, `__p__commode`, `_set_fmode`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_set_app_type`, `_initialize_onexit_table`, `_register_onexit_function`, `_register_thread_local_exe_atexit_callback`, `_c_exit`, `_configure_wide_argv`, `_cexit`, `abort`, `_initialize_wide_environment`, `_get_initial_wide_environment`, `_initterm`, `_initterm_e`, `_crt_atexit`, `__p___wargv`, `__p___argc`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

### Exports

`DotNetRuntimeDebugHeader`

## Extracted Strings

Total strings found: **14559** (showing first 100)

```
!This program cannot be run in DOS mode.
$
*@5Rich
`.rdata
@.data
.pdata
@.rsrc
@.reloc
AVWVUSH
 []^_A^
UAWAVAUATWVSH
([^_A\A]A^A_]
UAWAVWVSH
([^_A^A_]
AVWVUSH
 []^_A^
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
AVWVUSH
 []^_A^
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVWVSH
t$ S 
x[^_A^A_]
x[^_A^A_]
x[^_A^A_]
AVWVUSH
@[]^_A^
AWAVAUWVUSH
@[]^_A]A^A_
t$8@86H
T$ DK H
T$ DK H
UAWAVWVSH
e([^_A^A_]
e([^_A^A_]
UAWAVAUATWVSH
|ID;m8
eX[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
AVWVUSH
 []^_A^
 []^_A^
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
eh[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAVWVSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14004d310` | `0x14004d310` | 2001955 | ✓ |
| `fcn.14004d320` | `0x14004d320` | 2001945 | ✓ |
| `fcn.14004d340` | `0x14004d340` | 2001943 | ✓ |
| `fcn.14004d330` | `0x14004d330` | 2001935 | ✓ |
| `fcn.14004d350` | `0x14004d350` | 2001933 | ✓ |
| `fcn.14004d360` | `0x14004d360` | 2001923 | ✓ |
| `fcn.1401ae3f0` | `0x1401ae3f0` | 1710506 | ✓ |
| `fcn.14004d250` | `0x14004d250` | 1673835 | ✓ |
| `fcn.1401e44a0` | `0x1401e44a0` | 1633187 | ✓ |
| `fcn.1401e3654` | `0x1401e3654` | 1629696 | ✓ |
| `fcn.140042580` | `0x140042580` | 1474818 | ✓ |
| `fcn.14008fdf0` | `0x14008fdf0` | 1398952 | ✓ |
| `fcn.1401b50c0` | `0x1401b50c0` | 1368976 | ✓ |
| `fcn.14001d6c0` | `0x14001d6c0` | 1285420 | ✓ |
| `fcn.1401d3380` | `0x1401d3380` | 1284772 | ✓ |
| `fcn.14008aa40` | `0x14008aa40` | 1225706 | ✓ |
| `fcn.1401e56f0` | `0x1401e56f0` | 1221849 | ✓ |
| `fcn.1400c0690` | `0x1400c0690` | 1196917 | ✓ |
| `fcn.140092cd0` | `0x140092cd0` | 1178742 | ✓ |
| `fcn.14012b7f0` | `0x14012b7f0` | 1124881 | ✓ |
| `fcn.1401e51b8` | `0x1401e51b8` | 1082572 | ✓ |
| `fcn.14012e560` | `0x14012e560` | 1069627 | ✓ |
| `fcn.1401e4a20` | `0x1401e4a20` | 1067941 | ✓ |
| `fcn.1401913a0` | `0x1401913a0` | 1047858 | ✓ |
| `fcn.140105c90` | `0x140105c90` | 917469 | ✓ |
| `fcn.1400bdd20` | `0x1400bdd20` | 760161 | ✓ |
| `fcn.1400be8c0` | `0x1400be8c0` | 757385 | ✓ |
| `fcn.1400be860` | `0x1400be860` | 757134 | ✓ |
| `fcn.140127a30` | `0x140127a30` | 751182 | ✓ |
| `fcn.14017b750` | `0x14017b750` | 738140 | ✓ |

### Decompiled Code Files

- [`code/fcn.14001d6c0.c`](code/fcn.14001d6c0.c)
- [`code/fcn.140042580.c`](code/fcn.140042580.c)
- [`code/fcn.14004d250.c`](code/fcn.14004d250.c)
- [`code/fcn.14004d310.c`](code/fcn.14004d310.c)
- [`code/fcn.14004d320.c`](code/fcn.14004d320.c)
- [`code/fcn.14004d330.c`](code/fcn.14004d330.c)
- [`code/fcn.14004d340.c`](code/fcn.14004d340.c)
- [`code/fcn.14004d350.c`](code/fcn.14004d350.c)
- [`code/fcn.14004d360.c`](code/fcn.14004d360.c)
- [`code/fcn.14008aa40.c`](code/fcn.14008aa40.c)
- [`code/fcn.14008fdf0.c`](code/fcn.14008fdf0.c)
- [`code/fcn.140092cd0.c`](code/fcn.140092cd0.c)
- [`code/fcn.1400bdd20.c`](code/fcn.1400bdd20.c)
- [`code/fcn.1400be860.c`](code/fcn.1400be860.c)
- [`code/fcn.1400be8c0.c`](code/fcn.1400be8c0.c)
- [`code/fcn.1400c0690.c`](code/fcn.1400c0690.c)
- [`code/fcn.140105c90.c`](code/fcn.140105c90.c)
- [`code/fcn.140127a30.c`](code/fcn.140127a30.c)
- [`code/fcn.14012b7f0.c`](code/fcn.14012b7f0.c)
- [`code/fcn.14012e560.c`](code/fcn.14012e560.c)
- [`code/fcn.14017b750.c`](code/fcn.14017b750.c)
- [`code/fcn.1401913a0.c`](code/fcn.1401913a0.c)
- [`code/fcn.1401ae3f0.c`](code/fcn.1401ae3f0.c)
- [`code/fcn.1401b50c0.c`](code/fcn.1401b50c0.c)
- [`code/fcn.1401d3380.c`](code/fcn.1401d3380.c)
- [`code/fcn.1401e3654.c`](code/fcn.1401e3654.c)
- [`code/fcn.1401e44a0.c`](code/fcn.1401e44a0.c)
- [`code/fcn.1401e4a20.c`](code/fcn.1401e4a20.c)
- [`code/fcn.1401e51b8.c`](code/fcn.1401e51b8.c)
- [`code/fcn.1401e56f0.c`](code/fcn.1401e56f0.c)

## Behavioral Analysis

Based on the provided disassembly and string data, here is an analysis of the binary sample:

### Core Functionality and Purpose
The code appears to be part of a **malware loader or a packed executable**. While a significant portion of the decompiled functions represents standard C Runtime (CRT) library boilerplate—specifically for math operations, memory management, and thread pool handling—the surrounding structure indicates that it is designed to wrap and hide malicious functionality.

The binary's primary role is likely to unpack/decrypt an embedded payload or decrypt subsequent stages of a multi-stage infection.

### Suspicious or Malicious Behaviors
*   **String Obfuscation & Encoding:** 
    *   The `EXTRACTED STRINGS` section contains repetitive, non-human-readable character sequences (e.g., `UAWAVAUATWVSH`). This is a classic indicator of an **encrypted string table**. These strings are likely decrypted into memory at runtime to reveal commands, IP addresses, or file paths.
    *   Function `fcn.1401b50c0` contains complex bit-shifting and shifting logic (e.g., `uVar3 = uVar4 >> 0x38 | ...`). This is commonly used for **custom string decoding** or handling multi-byte character sets in a way that evades standard string analysis tools.
*   **Anti-Analysis / Evasion Techniques:**
    *   **Exception-Based Control Flow:** Multiple functions (e.g., `fcn.14004d250`, `fcn.1401e3654`) conclude with or contain a call to `swi(3)` (Software Interrupt 3). In a malware context, this is often used for **exception-based branching**. Instead of using standard conditional jumps (which are easy to follow), the code intentionally triggers an exception and uses a custom handler to determine the next execution step.
    *   **Dead Code/Junk Code:** The use of `while(true)` loops in functions like `fcn.1401d3380` (intended for "do nothing" blocks) and complex, multi-layered conditional checks on memory addresses suggests a technique to confuse automated analysis tools and human researchers by obscuring the true execution path.
*   **Thread Pool Manipulation:**
    *   The use of `CreateThreadpoolWork` and `SubmitThreadpoolWork` (seen in `fcn.140092cd0`) is used to move tasks into background threads. In malware, this is often used to **hide execution from the primary thread**, making it harder for analysts to track malicious activity like network communication or file encryption.

### Notable Techniques and Patterns
*   **Obfuscated API Resolution:** The code frequently calculates offsets (e.g., `0x1402d39e8`, `0x1403c6838`) and performs indirect jumps through these addresses. This suggests that the binary does not call standard APIs directly but resolves them at runtime to evade static analysis of the Import Address Table (IAT).
*   **Complex Memory Parsing:** Function `fcn.1401b50c0` shows heavy manipulation of memory blocks, which is characteristic of a **custom packer's unpacking routine**, where it manages different segments of code as they are decrypted into memory.
*   **Symbolic/Numeric Obfuscation:** The inclusion of several math functions (`sin`, `cos`, `pow`, `tan`) and the logic in `fcn.1401e56f0` suggests that calculations may be used to generate decryption keys or calculate jump offsets for a "virtualized" instruction set common in modern packers (like VMProtect or Themida).

### Summary of Findings
*   **Type:** Loader / Packer.
*   **Evasion Tactics:** Exception-based flow control, encrypted string tables, and obfuscated API calls.
*   **Risk Level:** High; the presence of these specific indicators suggests the binary is designed to hide a secondary payload from security software.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of non-human-readable character sequences and custom bit-shifting logic indicates an attempt to hide configuration data like IPs and commands. |
| **T1028** | Packing | The analysis identifies the binary as a loader/packer that utilizes complex memory parsing and mathematical functions to wrap and protect the primary payload. |
| **T1106** | Dynamic Resolution | The behavior of calculating offsets and using indirect jumps instead of standard IAT calls is a classic method for resolving APIs at runtime to evade static analysis. |
| **T1497** | (Optional/Contextual) Obfuscated Execution Paths | The use of exception-based control flow (`swi(3)`) and "junk" code loops are specific methods used to confuse automated disassemblers and hinder manual analysis. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   None identified. (Note: The technical analysis indicates that strings are encrypted/obfuscated; any C2 infrastructure is likely hidden within these encoded blocks and only revealed in memory at runtime.)

### **File paths / Registry keys**
*   None identified.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Execution Patterns:**
    *   **Exception-based Control Flow:** Use of `swi(3)` (Software Interrupt 3) for non-standard branching to evade automated analysis.
    *   **Obfuscated API Resolution:** Calculation of memory offsets (e.g., `0x1402d39e8`, `0x1403c6838`) and indirect jumps rather than direct Import Address Table (IAT) calls.
    *   **Thread Pool Manipulation:** Use of `CreateThreadpoolWork` and `SubmitThreadpoolWork` to hide malicious activity in background threads.
*   **Obfuscation Techniques:**
    *   **Encrypted String Tables:** The presence of repeating, high-entropy sequences (e.g., `UAWAVAUATWVSH`) indicates a packed or encrypted payload.
    *   **Dead Code/Junk Code:** Utilization of infinite loops (`while(true)`) and complex redundant checks to hinder static analysis.
    *   **Potential Virtualization:** Inclusion of math functions (`sin`, `cos`, `pow`, `tan`) used in conjunction with custom decoding logic suggests the use of a packer like VMProtect or Themida.

---
**Analyst Note:** This sample is identified as a **Loader/Packer**. Because the strings are heavily obfuscated, this report focuses on the *behavioral* indicators. The lack of static network IOCs suggests that this stage is intended only to decrypt and launch a secondary payload.

---

## Malware Family Classification

1. **Malware family:** Unknown
2. **Malware type:** Loader / Packer
3. **Confidence:** High

4. **Key evidence:**
*   **Advanced Evasion Techniques:** The use of `swi(3)` for exception-based control flow, "junk code" loops, and complex math functions to calculate jump offsets indicates a sophisticated effort to defeat automated disassemblers and static analysis tools (common in protectors like VMProtect or Themida).
*   **Obfuscated Execution Path:** The sample utilizes dynamic API resolution (calculating offsets rather than using a standard IAT) and encrypted string tables, which are classic hallmarks of a loader designed to hide its final payload and networking capabilities from initial inspection.
*   **Stealthy Behavior:** The integration of thread pool manipulation (`CreateThreadpoolWork`) suggests the binary is designed to move malicious operations into background threads to evade detection by monitoring tools that focus on the primary execution thread.
