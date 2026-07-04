# Threat Analysis Report

**Generated:** 2026-07-02 18:34 UTC
**Sample:** `03a5c74e7175b281351b5bef087a53eb5d52e535f715011a747e2656761e3ee9_03a5c74e7175b281351b5bef087a53eb5d52e535f715011a747e2656761e3ee9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `03a5c74e7175b281351b5bef087a53eb5d52e535f715011a747e2656761e3ee9_03a5c74e7175b281351b5bef087a53eb5d52e535f715011a747e2656761e3ee9.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 8 sections |
| Size | 11,778,560 bytes |
| MD5 | `531f845ff475beb225a17a0831f5753f` |
| SHA1 | `10454fe636ddadca6fe850a861838a7f6af9e568` |
| SHA256 | `03a5c74e7175b281351b5bef087a53eb5d52e535f715011a747e2656761e3ee9` |
| Overall entropy | 6.546 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1760143008 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 756,736 | 6.644 | No |
| `.managed` | 3,020,288 | 6.448 | No |
| `.rdata` | 7,284,736 | 5.925 | No |
| `.data` | 324,608 | 3.713 | No |
| `.pdata` | 254,464 | 6.46 | No |
| `_RDATA` | 512 | 3.294 | No |
| `.rsrc` | 2,560 | 3.925 | No |
| `.reloc` | 133,632 | 5.496 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExW`, `RegEnumKeyExW`, `RegEnumValueW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `OpenProcessToken`, `GetTokenInformation`, `OpenThreadToken`, `RevertToSelf`, `ImpersonateLoggedOnUser`, `AllocateAndInitializeSid`, `CheckTokenMembership`
**bcrypt.dll**: `BCryptOpenAlgorithmProvider`, `BCryptImportKey`, `BCryptHashData`, `BCryptGetProperty`, `BCryptFinishHash`, `BCryptExportKey`, `BCryptDecrypt`, `BCryptEncrypt`, `BCryptCreateHash`, `BCryptGenRandom`, `BCryptCloseAlgorithmProvider`, `BCryptDestroyKey`, `BCryptDestroyHash`, `BCryptSetProperty`
**CRYPT32.dll**: `CertFreeCertificateChainEngine`, `CertCloseStore`, `PFXImportCertStore`, `PFXExportCertStore`, `CryptFindOIDInfo`, `CryptQueryObject`, `CryptMsgGetParam`, `CryptMsgClose`, `CryptImportPublicKeyInfoEx2`, `CryptFormatObject`, `CryptDecodeObject`, `CertVerifyTimeValidity`, `CertSetCertificateContextProperty`, `CertSerializeCertificateStoreElement`, `CertSaveStore`
**IPHLPAPI.DLL**: `GetNetworkParams`, `if_nametoindex`, `GetPerAdapterInfo`, `GetAdaptersAddresses`
**KERNEL32.dll**: `InterlockedFlushSList`, `RtlPcToFileHeader`, `RaiseException`, `RtlUnwindEx`, `TlsAlloc`, `TlsGetValue`, `TlsSetValue`, `TlsFree`, `IsDebuggerPresent`, `InitializeSListHead`, `GetCurrentProcessId`, `InitializeCriticalSectionAndSpinCount`, `IsProcessorFeaturePresent`, `SetLastError`, `FormatMessageW`
**ncrypt.dll**: `NCryptDeleteKey`, `NCryptOpenStorageProvider`, `NCryptGetProperty`, `NCryptSetProperty`, `NCryptImportKey`, `NCryptOpenKey`, `NCryptFreeObject`
**ole32.dll**: `CoGetApartmentType`, `CoWaitForMultipleHandles`, `CoTaskMemFree`, `CoUninitialize`, `CoInitializeEx`, `CoTaskMemAlloc`, `CoCreateGuid`
**USER32.dll**: `LoadStringW`
**WS2_32.dll**: `recv`, `WSASend`, `send`, `WSARecv`, `WSAGetOverlappedResult`, `WSAConnect`, `ioctlsocket`, `select`, `shutdown`, `WSAEventSelect`, `WSAIoctl`, `closesocket`, `GetNameInfoW`, `GetAddrInfoW`, `FreeAddrInfoW`
**api-ms-win-crt-heap-l1-1-0.dll**: `free`, `calloc`, `malloc`, `_callnewh`
**api-ms-win-crt-math-l1-1-0.dll**: `log2`, `ceil`, `floor`, `pow`, `modf`
**api-ms-win-crt-string-l1-1-0.dll**: `_wcsicmp`, `wcsncmp`, `strcmp`, `strcpy_s`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_seh_filter_dll`, `_configure_narrow_argv`, `_initialize_narrow_environment`, `_initialize_onexit_table`, `_initterm_e`, `abort`, `exit`, `terminate`, `_initterm`, `_cexit`, `_execute_onexit_table`

### Exports

`__pth_gpointer_locked`, `_pthread_cleanup_dest`, `_pthread_get_state`, `_pthread_invoke_cancel`, `_pthread_key_dest`, `_pthread_set_state`, `_pthread_tryjoin`, `clock_getres`, `clock_getres32`, `clock_getres64`, `clock_gettime`, `clock_gettime32`, `clock_gettime64`, `clock_nanosleep`, `clock_nanosleep32`, `clock_nanosleep64`, `clock_settime`, `clock_settime32`, `clock_settime64`, `nanosleep`, `nanosleep32`, `nanosleep64`, `pthread_attr_destroy`, `pthread_attr_getdetachstate`, `pthread_attr_getinheritsched`, `pthread_attr_getschedparam`, `pthread_attr_getschedpolicy`, `pthread_attr_getscope`, `pthread_attr_getstack`, `pthread_attr_getstackaddr`, `pthread_attr_getstacksize`, `pthread_attr_init`, `pthread_attr_setdetachstate`, `pthread_attr_setinheritsched`, `pthread_attr_setschedparam`, `pthread_attr_setschedpolicy`, `pthread_attr_setscope`, `pthread_attr_setstack`, `pthread_attr_setstackaddr`, `pthread_attr_setstacksize`, `pthread_barrier_destroy`, `pthread_barrier_init`, `pthread_barrier_wait`, `pthread_barrierattr_destroy`, `pthread_barrierattr_getpshared`, `pthread_barrierattr_init`, `pthread_barrierattr_setpshared`, `pthread_cancel`, `pthread_cond_broadcast`, `pthread_cond_destroy`

## Extracted Strings

Total strings found: **189790** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.managed
`.rdata
@.data
.pdata
@_RDATA
@.rsrc
@.reloc
c(I;C0u
c(I;C0u
c8I;C@u
cHI;CPu
c(I;C0u
c8I;C@u
cHI;CPu
cXI;C`u
chI;Cpu
c(I;C0u
c8I;C@u
cHI;CPu
cXI;C`u
chI;Cpu
c(I;C0u
c8I;C@u
cHI;CPu
cXI;C`u
chI;Cpu
c(I;C0u
c8I;C@u
cHI;CPu
cXI;C`u
chI;Cpu
AQAWAVAUATWVSh
L$XAQL
0]AZAZ[^_A\A]A^A_AZ
0]AZAZ[^_A\A]A^A_AZ
AQAWAVAUATWVSh
L$XAQL
0]AZAZ[^_A\A]A^A_AZ
0]AZAZ[^_A\A]A^A_AZ
fffffff
u4H;O#
r+H;N#
|$ AVH
|$ AVH
APAWAVAUATSAPVWUPRH
APAWAVAUATSAPVWUPRH
APAWAVAUATSAPVWUPRH
AWAVAUATSVWUH
AWAVAUATSVWUH
o|$0fD
oD$@fD
oL$PfD
oT$`fD
o\$pfD
]_^[A\A]A^A_
AWAVAUATSVWUH
o|$0fD
oD$@fD
oL$PfD
oT$`fD
o\$pfD
]_^[A\A]A^A_
@SVAWH
t$ WATAUAVAWH
A_A^A]A\_
PAWAVAUATWVSQRUH
8]XX[^_A\A]A^A_XX
8]XX[^_A\A]A^A_XXH
QAWAVAUATWVSh
0]AZAZ[^_A\A]A^A_AZ
SATAUAWH
hA_A]A\[
WAVAWH
 A_A^_
|$ AVH
SUVWATAUAVAWH
A_A^A]A\_^][
WAVAWH
0A_A^_
UWATAVAWH
9Hc9H
 A_A^A\_]
\$ AVH
A8H+Q0H;
@UWAVAWH
(A_A^_]
(A_A^_]
|$ ATAVAWH
0A_A^A\
\$ UAVAWH
 A_A^]
 A_A^]
VWATAUAVAWL
A_A^A]A\_^
WAVAWH
 A_A^_
|$ AVH
u6H9-I
\$@t6H
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.18036a720` | `0x18036a720` | 2242736 | ✓ |
| `fcn.1803693d0` | `0x1803693d0` | 2239120 | ✓ |
| `fcn.18015ff10` | `0x18015ff10` | 2172154 | ✓ |
| `fcn.1802d8ce0` | `0x1802d8ce0` | 1984145 | ✓ |
| `fcn.180345d60` | `0x180345d60` | 1963841 | ✓ |
| `fcn.1801b9aa0` | `0x1801b9aa0` | 1960923 | ✓ |
| `fcn.1801bfc90` | `0x1801bfc90` | 1933317 | ✓ |
| `fcn.18019de00` | `0x18019de00` | 1656831 | ✓ |
| `fcn.1801960a0` | `0x1801960a0` | 1629777 | ✓ |
| `fcn.180196840` | `0x180196840` | 1628008 | ✓ |
| `fcn.180217ba0` | `0x180217ba0` | 1581309 | ✓ |
| `fcn.18022a880` | `0x18022a880` | 1504604 | ✓ |
| `fcn.18023d780` | `0x18023d780` | 1421973 | ✓ |
| `fcn.18023b650` | `0x18023b650` | 1134565 | ✓ |
| `fcn.18029c420` | `0x18029c420` | 1067236 | ✓ |
| `fcn.180017190` | `0x180017190` | 630158 | ✓ |
| `fcn.1802d91b0` | `0x1802d91b0` | 586965 | ✓ |
| `fcn.180368f60` | `0x180368f60` | 393981 | ✓ |
| `fcn.1801b9c90` | `0x1801b9c90` | 385768 | ✓ |
| `fcn.180369f20` | `0x180369f20` | 381101 | ✓ |
| `fcn.18036ab20` | `0x18036ab20` | 371133 | ✓ |
| `fcn.18036ed00` | `0x18036ed00` | 369835 | ✓ |
| `fcn.18036c810` | `0x18036c810` | 368980 | ✓ |
| `fcn.18036bca0` | `0x18036bca0` | 367957 | ✓ |
| `fcn.18033d800` | `0x18033d800` | 357803 | ✓ |
| `fcn.180395350` | `0x180395350` | 356365 | ✓ |
| `fcn.1803382b0` | `0x1803382b0` | 355123 | ✓ |
| `fcn.18036fd50` | `0x18036fd50` | 344413 | ✓ |
| `fcn.180370de0` | `0x180370de0` | 336933 | ✓ |
| `fcn.180370760` | `0x180370760` | 336798 | ✓ |

### Decompiled Code Files

- [`code/fcn.180017190.c`](code/fcn.180017190.c)
- [`code/fcn.18015ff10.c`](code/fcn.18015ff10.c)
- [`code/fcn.1801960a0.c`](code/fcn.1801960a0.c)
- [`code/fcn.180196840.c`](code/fcn.180196840.c)
- [`code/fcn.18019de00.c`](code/fcn.18019de00.c)
- [`code/fcn.1801b9aa0.c`](code/fcn.1801b9aa0.c)
- [`code/fcn.1801b9c90.c`](code/fcn.1801b9c90.c)
- [`code/fcn.1801bfc90.c`](code/fcn.1801bfc90.c)
- [`code/fcn.180217ba0.c`](code/fcn.180217ba0.c)
- [`code/fcn.18022a880.c`](code/fcn.18022a880.c)
- [`code/fcn.18023b650.c`](code/fcn.18023b650.c)
- [`code/fcn.18023d780.c`](code/fcn.18023d780.c)
- [`code/fcn.18029c420.c`](code/fcn.18029c420.c)
- [`code/fcn.1802d8ce0.c`](code/fcn.1802d8ce0.c)
- [`code/fcn.1802d91b0.c`](code/fcn.1802d91b0.c)
- [`code/fcn.1803382b0.c`](code/fcn.1803382b0.c)
- [`code/fcn.18033d800.c`](code/fcn.18033d800.c)
- [`code/fcn.180345d60.c`](code/fcn.180345d60.c)
- [`code/fcn.180368f60.c`](code/fcn.180368f60.c)
- [`code/fcn.1803693d0.c`](code/fcn.1803693d0.c)
- [`code/fcn.180369f20.c`](code/fcn.180369f20.c)
- [`code/fcn.18036a720.c`](code/fcn.18036a720.c)
- [`code/fcn.18036ab20.c`](code/fcn.18036ab20.c)
- [`code/fcn.18036bca0.c`](code/fcn.18036bca0.c)
- [`code/fcn.18036c810.c`](code/fcn.18036c810.c)
- [`code/fcn.18036ed00.c`](code/fcn.18036ed00.c)
- [`code/fcn.18036fd50.c`](code/fcn.18036fd50.c)
- [`code/fcn.180370760.c`](code/fcn.180370760.c)
- [`code/fcn.180370de0.c`](code/fcn.180370de0.c)
- [`code/fcn.180395350.c`](code/fcn.180395350.c)

## Behavioral Analysis

Based on the provided disassembly, here is an analysis of the code's functionality and behavior:

### Core Functionality and Purpose
The code appears to be part of a **complex, data-driven execution engine** or a **resource management system**. It does not appear to perform direct malicious actions (like file deletion or socket creation) in this specific snippet, but it provides the infrastructure for a highly structured program to process commands, manage objects, and handle internal state.

Key components include:
*   **Memory Management:** Functions like `fcn.18036a720` and `fcn.1803693d0` are custom implementations of `memmove` or `memcpy`. They handle overlapping memory regions and varied data sizes.
*   **String Processing & Parsing:** Function `fcn.18015ff10` is a robust parser that converts strings into integers, handling various edge cases (like "0x" prefixes and leading zeros). This is typically used for parsing configuration files or command-line arguments.
*   **Object/Resource Lookup:** The "series" of functions (`fcn.18036ed00`, `fcn.18036c810`, `fcn.18036bca0`, etc.) follow a nearly identical pattern: they take an identifier, perform a lookup, and then iterate through a result set to populate a buffer or table. This suggests the code is designed to handle different "types" of objects via a unified interface.
*   **Dynamic Dispatching:** The logic in `fcn.180345d60` suggests a state-aware system where functionality is determined by checking internal flags and data structures before proceeding with an operation.

### Suspicious or Malicious Behaviors
While the code's intent is not explicitly malicious, several patterns are common in sophisticated malware (particularly "Command & Control" (C2) modules or complex Trojans):

*   **Manual Library Implementations:** The use of custom `memcpy` and string parsing functions instead of standard library calls can be a technique to avoid detection by security tools that look for specific API imports, or to ensure the code is portable across different environments.
*   **Abstracted "Action" Handling:** The heavily repetitive nature of the `18036...` series suggests an **abstraction layer**. In malware, this is often used to implement a "plug-and-play" command system where the core logic remains static while various malicious capabilities are added as distinct "modules" or "actions."
*   **Complex State Management:** The depth of checks in `fcn.180345d60` (checking if an object is null, checking its internal state before calling a sub-routine) suggests the program is prepared to handle complex, multi-stage instructions.

### Notable Techniques & Patterns
*   **Data-Driven Architecture:** The code is designed to do very little "hardcoded" logic. Instead, it seems to act as a "worker" that takes an ID (like `0x18089dad0`) and finds the corresponding functionality/data. This makes reverse engineering difficult because the *actual* malicious behavior may not be in these functions but rather in the data files or tables they are designed to process.
*   **High Degree of Modularization:** The very similar structures of `fcn.18036ed00`, `fcn.18036c810`, and `fcn.18036bca0` indicate that the developer used a template or generated code to handle different types of data, which is typical in large-scale software but also common in sophisticated malware frameworks (like those used by APT groups) to maintain a consistent internal API.
*   **Robust Error Handling:** The frequent checks for `NULL` and specific status codes before proceeding indicate a "hardened" application designed to run reliably without crashing, which is a hallmark of professional-grade malware.

### Summary
This code acts as the **internal backbone/engine** for a larger application. It is responsible for memory manipulation, string parsing, and dynamic object resolution. While no overt malicious behavior (like a payload drop or encryption) is seen in this specific snippet, the high level of sophistication and abstraction suggests it belongs to a complex piece of software that could be either a heavy commercial application or a sophisticated piece of malware using a modular "Command & Control" architecture.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of custom implementations for standard functions (like `memcpy` and string parsing) is a common method to bypass signature-based detection and evade analysis tools looking for specific library calls. |
| T1568 | Dynamic Resolution | The ID-based look-up system and "data-driven" architecture allow the program to resolve functionality at runtime, making it harder for analysts to map all potential actions through static analysis. |
| T1036 | Masquerading | The high level of sophistication, robust error handling, and modularity are characteristic of professional-grade malware designed to mimic legitimate complex software while hiding its true capabilities. |
| T1059 | Command and Scripting Interpreter | The "worker" engine design and state-aware dispatching suggest a system capable of processing multi-stage instructions or commands received from an external source. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the identified Indicators of Compromise (IOCs).

**Note:** The "Extracted Strings" section contains a large amount of high-entropy/obfuscated data which does not resolve to human-readable IP addresses, URLs, or file paths. The "Behavioral Analysis" describes architectural techniques rather than specific, actionable indicators.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified (Note: The "fcn" values provided in the analysis are memory offsets/function addresses, not file hashes).

### **Other artifacts**
*   **Behavioral Patterns:** 
    *   Use of custom `memmove`/`memcpy` implementations to evade standard API monitoring.
    *   Custom string-to-integer parsing (handling "0x" prefixes) likely used for processing encrypted configuration files.
    *   Data-driven, modular architecture (objects identified by internal IDs rather than hardcoded strings).

---
**Analyst Note:** The provided text describes a highly sophisticated and abstracted piece of software. While it exhibits behaviors consistent with professional malware (e.g., custom library implementations, dynamic dispatching, and obfuscated data), no specific actionable IOCs (like a hardcoded C2 IP or a specific file path) were present in the source material provided.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Backdoor
3. **Confidence**: Medium

4. **Key evidence**:
*   **Modular "Command & Control" Architecture:** The use of a data-driven engine where functions are called via internal IDs (rather than hardcoded logic) and the presence of a dynamic dispatch system strongly suggest a multi-stage framework typical of advanced backdoors or loaders (e.g., Cobalt Strike-style beacons).
*   **Anti-Analysis & Evasion Techniques:** The implementation of custom versions of standard library functions (like `memcpy` and string-to-integer parsing) is a classic technique used to bypass signature-based detection and evade automated analysis tools that monitor common API imports.
*   **Sophisticated State Management:** The "hardened" nature of the code—characterized by robust error handling, complex state checks, and an abstracted "worker" design—indicates it is intended for reliable, long-term operation in a compromised environment rather than being a simple, one-off malicious script.
