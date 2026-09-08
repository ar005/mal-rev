# Threat Analysis Report

**Generated:** 2026-09-05 14:26 UTC
**Sample:** `146cd7ad383cd52d1c66dcbff1d29703456b7b8ac170086908c0a6ff109d0507_146cd7ad383cd52d1c66dcbff1d29703456b7b8ac170086908c0a6ff109d0507.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `146cd7ad383cd52d1c66dcbff1d29703456b7b8ac170086908c0a6ff109d0507_146cd7ad383cd52d1c66dcbff1d29703456b7b8ac170086908c0a6ff109d0507.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 6,884,352 bytes |
| MD5 | `0541e78739c29579f9266daaada067ba` |
| SHA1 | `f2b6cb396af3a72b242d77ada2eaf549e67caa55` |
| SHA256 | `146cd7ad383cd52d1c66dcbff1d29703456b7b8ac170086908c0a6ff109d0507` |
| Overall entropy | 6.783 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1775204813 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 3,940,864 | 6.513 | No |
| `.rdata` | 2,368,000 | 6.781 | No |
| `.data` | 23,552 | 4.492 | No |
| `.pdata` | 273,920 | 6.473 | No |
| `.rsrc` | 272,384 | 3.235 | No |
| `.reloc` | 4,608 | 5.334 | No |

### Imports

**ADVAPI32.dll**: `AdjustTokenPrivileges`, `DeregisterEventSource`, `GetTokenInformation`, `ImpersonateLoggedOnUser`, `LookupPrivilegeValueW`, `OpenProcessToken`, `OpenThreadToken`, `RegCloseKey`, `RegEnumKeyExW`, `RegNotifyChangeKeyValue`, `RegOpenKeyExW`, `RegQueryValueExW`, `RegisterEventSourceW`, `ReportEventW`, `RevertToSelf`
**bcrypt.dll**: `BCryptImportKeyPair`, `BCryptGetProperty`, `BCryptGenRandom`, `BCryptFinishHash`, `BCryptExportKey`, `BCryptDestroyKey`, `BCryptDestroyHash`, `BCryptHashData`, `BCryptCreateHash`, `BCryptCloseAlgorithmProvider`, `BCryptOpenAlgorithmProvider`
**CRYPT32.dll**: `CertNameToStrW`, `CertGetNameStringW`, `CertGetCertificateContextProperty`, `CertGetCertificateChain`, `CertFreeCertificateContext`, `CertOpenStore`, `CryptImportPublicKeyInfoEx2`, `CryptFormatObject`, `CryptFindOIDInfo`, `CryptDecodeObject`, `CertVerifyCertificateChainPolicy`, `CertFreeCertificateChainEngine`, `CertAddCertificateContextToStore`, `CertAddCertificateLinkToStore`, `CertCloseStore`
**IPHLPAPI.DLL**: `ConvertInterfaceNameToLuidW`, `GetAdaptersAddresses`, `GetNetworkParams`, `GetPerAdapterInfo`, `ConvertInterfaceLuidToIndex`
**KERNEL32.dll**: `RtlUnwindEx`, `RtlPcToFileHeader`, `EncodePointer`, `InitializeCriticalSectionAndSpinCount`, `TlsAlloc`, `TlsGetValue`, `TlsSetValue`, `TlsFree`, `InitializeSListHead`, `CancelIoEx`, `CancelSynchronousIo`, `CancelThreadpoolIo`, `CloseHandle`, `CloseThreadpoolIo`, `CloseThreadpoolWait`
**ncrypt.dll**: `NCryptOpenStorageProvider`, `NCryptSetProperty`, `NCryptGetProperty`, `NCryptImportKey`, `NCryptDeleteKey`, `NCryptOpenKey`, `NCryptFreeObject`
**ole32.dll**: `CoCreateGuid`, `CoTaskMemFree`, `CoUninitialize`, `CoGetApartmentType`, `CoTaskMemAlloc`, `CoWaitForMultipleHandles`, `CoInitializeEx`
**Secur32.dll**: `GetUserNameExW`
**WS2_32.dll**: `send`, `select`, `recv`, `setsockopt`, `getsockopt`, `getpeername`, `closesocket`, `bind`, `WSAStartup`, `ioctlsocket`, `WSAEventSelect`, `FreeAddrInfoExW`, `FreeAddrInfoW`, `GetAddrInfoExW`, `GetAddrInfoW`
**api-ms-win-crt-heap-l1-1-0.dll**: `malloc`, `_callnewh`, `_set_new_mode`, `_aligned_free`, `_aligned_malloc`, `calloc`, `free`
**api-ms-win-crt-math-l1-1-0.dll**: `fmodf`, `fmod`, `pow`, `log`, `__setusermatherr`
**api-ms-win-crt-string-l1-1-0.dll**: `strcmp`, `strcpy`, `strlen`, `strcpy_s`, `wcsncmp`, `_stricmp`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__p__commode`, `__stdio_common_vsnprintf_s`, `_set_fmode`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_crt_atexit`, `_initialize_onexit_table`, `_set_app_type`, `terminate`, `_register_onexit_function`, `abort`, `_seh_filter_exe`, `_configure_wide_argv`, `_initialize_wide_environment`, `_register_thread_local_exe_atexit_callback`, `_initterm_e`, `_c_exit`, `_cexit`, `__p___wargv`, `__p___argc`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

## Extracted Strings

Total strings found: **18447** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
AVWVUSH
 []^_A^
AVWVUSH
 []^_A^
AVWVUSH
 []^_A^
UAWAVAUATWVSH
([^_A\A]A^A_]
AVWVUSH
 []^_A^
UAWAVWVSH
([^_A^A_]
UAVWVSH
0[^_A^]
UAVWVSH
[^_A^]
AWAVWVUSH
([]^_A^A_
AVWVUSH
 []^_A^
|Abu
UAWAVWVSH
8[^_A^A_]
AWAVAUATWVUSH
[]^_A\A]A^A_
AWAVWVUSH
H[]^_A^A_
L$0;L$@
L$0;L$@
L$0;L$@
L$0;L$@
L$0;L$@
L$0;L$@
L$0;L$@
L$0;L$@
L$0;L$@wPH
L$0;L$@v
AWAVAUATWVUSH
X[]^_A\A]A^A_
AWAVAUATWVUSH
h[]^_A\A]A^A_
L$P;L$`
L$P;L$`wkH
L$P;L$`v
AVWVUSH
0[]^_A^
AVWVUSH
 []^_A^
UAWAVWVSH
H[^_A^A_]
AVWVUSH
@[]^_A^
UAWAVWVSH
([^_A^A_]
AVWVUSH
[]^_A^
gfffffffH
AVWVUSH
 []^_A^
AVWVUSH
 []^_A^
AWAVWVUSH
([]^_A^A_
UAWAVWVSH
H[^_A^A_]
H[^_A^A_]
UAWAVAUWVSH
P[^_A]A^A_]
tD@8?H
L$0;L$@v
AVWVUSH
 []^_A^
C8+C@;
AVWVUSH
0[]^_A^
AWAVAUATWVUSH
8[]^_A\A]A^A_
([]^_I
AVWVUSH
@[]^_A^
AWAVWVUSH
([]^_A^A_
UAWAVAUWVSH
0[^_A]A^A_]
AVWVUSH
 []^_A^
AWAVWVUSH
H[]^_A^A_
AVWVUSH
 []^_A^
UAVWVSH
@[^_A^]
@[^_A^]
AVWVUSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1402ee61c` | `0x1402ee61c` | 3058690 | ✓ |
| `fcn.1400a8180` | `0x1400a8180` | 2796708 | ✓ |
| `fcn.1400ee520` | `0x1400ee520` | 2489850 | ✓ |
| `fcn.140120a88` | `0x140120a88` | 2381187 | ✓ |
| `fcn.14035f7e0` | `0x14035f7e0` | 2315755 | ✓ |
| `fcn.14035e9f4` | `0x14035e9f4` | 2312340 | ✓ |
| `fcn.1401657c0` | `0x1401657c0` | 2097576 | ✓ |
| `fcn.1401540f0` | `0x1401540f0` | 1934108 | — |
| `fcn.140162c60` | `0x140162c60` | 1885498 | ✓ |
| `fcn.1401168ac` | `0x1401168ac` | 1861562 | ✓ |
| `fcn.140058560` | `0x140058560` | 1858316 | ✓ |
| `fcn.14020e210` | `0x14020e210` | 1826329 | ✓ |
| `fcn.1403659c0` | `0x1403659c0` | 1824297 | ✓ |
| `fcn.1401abbac` | `0x1401abbac` | 1787085 | ✓ |
| `fcn.1403650f2` | `0x1403650f2` | 1781658 | ✓ |
| `fcn.14035fe24` | `0x14035fe24` | 1749001 | ✓ |
| `fcn.140176170` | `0x140176170` | 1652303 | ✓ |
| `fcn.140176150` | `0x140176150` | 1651811 | ✓ |
| `fcn.1401d55a0` | `0x1401d55a0` | 1640989 | ✓ |
| `fcn.1402b07d0` | `0x1402b07d0` | 1345422 | ✓ |
| `fcn.14020aa4c` | `0x14020aa4c` | 1338202 | ✓ |
| `fcn.14020f744` | `0x14020f744` | 1319182 | ✓ |
| `fcn.14020a3cc` | `0x14020a3cc` | 1162900 | ✓ |
| `fcn.14021620c` | `0x14021620c` | 1150807 | ✓ |
| `fcn.14020a2b0` | `0x14020a2b0` | 1131750 | ✓ |
| `fcn.14031e21c` | `0x14031e21c` | 932799 | ✓ |
| `fcn.14004bef8` | `0x14004bef8` | 890040 | ✓ |
| `fcn.1402675d4` | `0x1402675d4` | 861376 | ✓ |
| `fcn.14027bfac` | `0x14027bfac` | 803210 | ✓ |
| `fcn.140060fcc` | `0x140060fcc` | 802071 | ✓ |

### Decompiled Code Files

- [`code/fcn.14004bef8.c`](code/fcn.14004bef8.c)
- [`code/fcn.140058560.c`](code/fcn.140058560.c)
- [`code/fcn.140060fcc.c`](code/fcn.140060fcc.c)
- [`code/fcn.1400a8180.c`](code/fcn.1400a8180.c)
- [`code/fcn.1400ee520.c`](code/fcn.1400ee520.c)
- [`code/fcn.1401168ac.c`](code/fcn.1401168ac.c)
- [`code/fcn.140120a88.c`](code/fcn.140120a88.c)
- [`code/fcn.140162c60.c`](code/fcn.140162c60.c)
- [`code/fcn.1401657c0.c`](code/fcn.1401657c0.c)
- [`code/fcn.140176150.c`](code/fcn.140176150.c)
- [`code/fcn.140176170.c`](code/fcn.140176170.c)
- [`code/fcn.1401abbac.c`](code/fcn.1401abbac.c)
- [`code/fcn.1401d55a0.c`](code/fcn.1401d55a0.c)
- [`code/fcn.14020a2b0.c`](code/fcn.14020a2b0.c)
- [`code/fcn.14020a3cc.c`](code/fcn.14020a3cc.c)
- [`code/fcn.14020aa4c.c`](code/fcn.14020aa4c.c)
- [`code/fcn.14020e210.c`](code/fcn.14020e210.c)
- [`code/fcn.14020f744.c`](code/fcn.14020f744.c)
- [`code/fcn.14021620c.c`](code/fcn.14021620c.c)
- [`code/fcn.1402675d4.c`](code/fcn.1402675d4.c)
- [`code/fcn.14027bfac.c`](code/fcn.14027bfac.c)
- [`code/fcn.1402b07d0.c`](code/fcn.1402b07d0.c)
- [`code/fcn.1402ee61c.c`](code/fcn.1402ee61c.c)
- [`code/fcn.14031e21c.c`](code/fcn.14031e21c.c)
- [`code/fcn.14035e9f4.c`](code/fcn.14035e9f4.c)
- [`code/fcn.14035f7e0.c`](code/fcn.14035f7e0.c)
- [`code/fcn.14035fe24.c`](code/fcn.14035fe24.c)
- [`code/fcn.1403650f2.c`](code/fcn.1403650f2.c)
- [`code/fcn.1403659c0.c`](code/fcn.1403659c0.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is an analysis of the binary's functionality.

### Core Functionality and Purpose
The code appears to consist primarily of **low-level system abstractions, data parsing logic, and internal runtime management**. Rather than direct "malicious" actions (like sending a packet or deleting a file), these functions look like "glue" code—the kind found in large frameworks (such as the .NET Common Language Runtime) or complex system libraries.

*   **Data Structure Management:** Several functions (`fcn.14035f7e0`, `fcn.14035e9f4`, `fcn.1401657c0`) are responsible for initializing, validating, and populating internal objects or buffers. They set specific offsets (e.g., `+0x20`, `+0x18`) to define properties of an object.
*   **Numeric/String Parsing:** Function **`fcn.140162c60`** is a complex parsing routine. It handles logic for identifying numbers, skipping decimal points (`.`), handling leading zeros (e.g., `0x30`), and processing signs. This type of function is commonly used to parse configuration strings, IP addresses, or port numbers.
*   **Collection/Buffer Operations:** Functions like **`fcn.140058560`** iterate through linked lists or arrays to perform actions on each item, while **`fcn.14021620c`** performs a standard "compare" operation between two buffers (checking for equality and length).

### Suspicious or Malicious Behaviors
Based strictly on the provided code segment, there is no evidence of overt malicious activity such as process injection, file encryption, or direct network communication. However, there are patterns relevant to malware analysis:

*   **Infrastructure Evidence:** The frequent use of `swi(3)` (a "Software Interrupt" used by decompilers to represent indirect jumps they cannot resolve) and the structure of the functions strongly suggest this is **JIT-compiled code** or a heavily abstracted high-level language runtime. This is common in malware written in C# or C++ using complex frameworks to hide the underlying logic.
*   **Obfuscated String Data:** The provided string section contains a large amount of non-human-readable, repetitive character blocks (e.g., `AVWVUSH`, `UAWAVAUATWVSH`). This is typical of **packed or encrypted data**. While not "malicious" in itself, it suggests the binary contains hidden payloads or encrypted configuration blocks that are decrypted at runtime.
*   **Evasive Complexity:** The sheer complexity and volume of the internal logic (especially in `fcn.14020f744`) may be intended to frustrate analysts by burying actual malicious logic deep within a "wall" of legitimate-looking library functions.

### Notable Techniques or Patterns Observed
*   **Standard Library Logic:** The code contains very high-quality, standard implementation patterns for buffer management and string manipulation. This suggests the binary is not a standalone piece of malware but likely incorporates standard libraries to perform its tasks.
*   **Indirect Dispatching:** Several functions use jump tables (implied by "Too many branches" warnings) or indirect calls (e.g., `**0x14069a190`). This technique is often used in malware to implement "plug-and-play" functionality where the binary can switch behaviors based on environmental checks.
*   **Data Normalization:** The heavy emphasis on parsing and validating buffer lengths (`fcn.14027bfac`) suggests that the code handles data from an untrusted source, ensuring it fits into internal structures before use—a common step in both legitimate software and complex malware loaders.

### Summary for Lead Analyst
The provided sample appears to be a **component of a larger framework or a highly-obfuscated loader**. It contains robust parsing logic (likely for networking or configuration) and heavy data manipulation routines. While no direct "smoking gun" malicious actions are present in this specific block, the presence of high-complexity code, "junk" string blocks, and evidence of JIT compilation suggests it may be a component of a sophisticated piece of malware (such as a downloader or an encrypted payload handler).

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The presence of non-human-readable string blocks suggests packed/encrypted data, and the "wall" of complex logic is used to hide malicious functionality from analysts. |
| **T1036** | Masquerading | The binary uses extensive "standard library logic" and high-quality code patterns to mimic a legitimate system component or framework (like .NET) to evade detection. |
| **T1059** | Command and Scripting Interpreter | *Note: Potential Correlation:* While not explicitly confirmed as malicious, the robust parsing of "untrusted" input for configuration/logic suggests preparation for script-based execution or automated command processing. |

### Analyst Notes:
*   **Complexity as Evasion:** The analysis highlights a common tactic where high complexity is used specifically to exhaust analyst resources (a form of anti-analysis). This falls squarely under **T1027**.
*   **Loader Characteristics:** The description of the binary as a potential "loader" or "payload handler" suggests that while this specific module performs "clean" tasks (parsing, buffer management), it is designed to facilitate the execution of subsequent malicious stages.

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Based on your requirements, here is the extraction of Indicators of Compromise (IOCs):

### **Indicators of Compromise**

*   **IP addresses / URLs / Domains:**
    *   None identified.
*   **File paths / Registry keys:**
    *   None identified. (Note: The memory offsets provided in the analysis, e.g., `0x14035f7e0`, are internal function addresses and do not constitute persistent file system or registry IOCs.)
*   **Mutex names / Named pipes:**
    *   None identified.
*   **Hashes:**
    *   None identified.
*   **Other artifacts (user agents, C2 patterns, etc.):**
    *   **Obfuscated Data Blocks:** The strings `AVWVUSH`, `UAWAVAUATWVSH`, and associated alphanumeric sequences are identified as packed/encrypted data. While these do not provide direct C2 infrastructure, they indicate the presence of a "packer" or "crypter" layer intended to hide functionality.
    *   **JIT-Compilation/Indirect Dispatch:** The analysis notes the use of `swi(3)` and indirect jumps (e.g., `**0x14069a190`). While not a traditional IOC like an IP, these are behavioral indicators of high-level framework usage (like .NET) or intentional obfuscation to hide the control flow.

---
**Analyst Note:** The sample appears to be a "loader" or a component of a larger framework. Because the strings are heavily encrypted/obfuscated and no hardcoded network infrastructure (IPs/Domains) was found in this specific snippet, further dynamic analysis (sandboxing) is recommended to observe the payload after it is unpacked in memory.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for this sample:

1. **Malware family:** Unknown
2. **Malware type:** Loader
3. **Confidence:** Medium
4. **Key evidence:** 
    *   **Loader Characteristics:** The code functions primarily as "glue" logic—handling buffer management, data normalization, and complex parsing—which are primary indicators of a loader designed to process, de-obfuscate, and prepare an internal payload for execution.
    *   **Obfuscation & Anti-Analysis:** The presence of high-complexity "wall of code" tactics (T1036), non-human-readable string blocks (T1027), and indirect jump logic indicates a sophisticated attempt to hide malicious intent within standard library-like abstractions.
    *   **Lack of Direct Malice:** No direct C2 communication or payload execution was found in the provided segment, but the infrastructure for handling "untrusted" input suggests it is a precursor stage (downloader/loader) intended to facilitate further infection.
