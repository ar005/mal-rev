# Threat Analysis Report

**Generated:** 2026-08-15 20:49 UTC
**Sample:** `0f43b3de8c5e80bc9d81b9d8b9c67ebab8ac297d0eac10fa3e64831db36ee5b6_0f43b3de8c5e80bc9d81b9d8b9c67ebab8ac297d0eac10fa3e64831db36ee5b6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f43b3de8c5e80bc9d81b9d8b9c67ebab8ac297d0eac10fa3e64831db36ee5b6_0f43b3de8c5e80bc9d81b9d8b9c67ebab8ac297d0eac10fa3e64831db36ee5b6.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 8 sections |
| Size | 5,613,056 bytes |
| MD5 | `cbc8816f7ff5b163d5e58d62b959b631` |
| SHA1 | `fc0d34c8295913a42a79bbc368166c60883a9e21` |
| SHA256 | `0f43b3de8c5e80bc9d81b9d8b9c67ebab8ac297d0eac10fa3e64831db36ee5b6` |
| Overall entropy | 6.907 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1761354798 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 440,320 | 6.654 | No |
| `.managed` | 2,880,000 | 6.461 | No |
| `hydrated` | 0 | 0.0 | No |
| `.rdata` | 2,037,760 | 6.948 | No |
| `.data` | 20,480 | 4.58 | No |
| `.pdata` | 228,352 | 6.401 | No |
| `.rsrc` | 1,536 | 4.388 | No |
| `.reloc` | 3,584 | 5.306 | No |

### Imports

**ADVAPI32.dll**: `RegOpenKeyExW`, `RegQueryValueExW`, `RegCloseKey`, `OpenProcessToken`, `LookupPrivilegeValueW`, `AdjustTokenPrivileges`, `RegEnumKeyExW`, `GetTokenInformation`, `OpenThreadToken`, `RevertToSelf`, `ImpersonateLoggedOnUser`
**bcrypt.dll**: `BCryptSetProperty`, `BCryptImportKeyPair`, `BCryptDestroyKey`, `BCryptImportKey`, `BCryptDestroyHash`, `BCryptFinishHash`, `BCryptHashData`, `BCryptGetProperty`, `BCryptGenRandom`, `BCryptCreateHash`, `BCryptEncrypt`, `BCryptDecrypt`, `BCryptExportKey`, `BCryptOpenAlgorithmProvider`, `BCryptCloseAlgorithmProvider`
**CRYPT32.dll**: `CertFreeCertificateChainEngine`, `CertCloseStore`, `PFXImportCertStore`, `PFXExportCertStore`, `CryptFindOIDInfo`, `CryptQueryObject`, `CryptMsgGetParam`, `CryptMsgClose`, `CryptImportPublicKeyInfoEx2`, `CryptFormatObject`, `CryptDecodeObject`, `CertVerifyTimeValidity`, `CertSetCertificateContextProperty`, `CertSerializeCertificateStoreElement`, `CertSaveStore`
**IPHLPAPI.DLL**: `GetAdaptersAddresses`, `GetPerAdapterInfo`, `GetNetworkParams`, `if_nametoindex`
**KERNEL32.dll**: `RtlPcToFileHeader`, `RaiseException`, `RtlUnwindEx`, `InitializeCriticalSectionAndSpinCount`, `TlsAlloc`, `TlsGetValue`, `TlsSetValue`, `TlsFree`, `IsProcessorFeaturePresent`, `SetUnhandledExceptionFilter`, `UnhandledExceptionFilter`, `EncodePointer`, `IsDebuggerPresent`, `SetLastError`, `FormatMessageW`
**ncrypt.dll**: `NCryptFreeObject`, `NCryptImportKey`, `NCryptOpenKey`, `NCryptDeleteKey`, `NCryptGetProperty`, `NCryptSetProperty`, `NCryptOpenStorageProvider`
**ole32.dll**: `CoInitializeEx`, `CoUninitialize`, `CoTaskMemFree`, `CoTaskMemAlloc`, `CoGetApartmentType`, `CoCreateGuid`, `CoWaitForMultipleHandles`
**Secur32.dll**: `GetUserNameExW`
**WS2_32.dll**: `WSAConnect`, `shutdown`, `setsockopt`, `WSAGetOverlappedResult`, `WSARecv`, `select`, `recv`, `ioctlsocket`, `getsockopt`, `getpeername`, `WSAIoctl`, `send`, `bind`, `closesocket`, `GetNameInfoW`
**api-ms-win-crt-heap-l1-1-0.dll**: `calloc`, `_callnewh`, `free`, `_set_new_mode`, `malloc`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`, `ceil`, `floor`, `pow`, `modf`
**api-ms-win-crt-string-l1-1-0.dll**: `strcpy_s`, `wcsncmp`, `strcmp`, `_stricmp`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_get_initial_wide_environment`, `terminate`, `_crt_atexit`, `_register_onexit_function`, `_initialize_onexit_table`, `_register_thread_local_exe_atexit_callback`, `_c_exit`, `_cexit`, `__p___wargv`, `__p___argc`, `_exit`, `exit`, `_initterm_e`, `_initterm`, `_initialize_wide_environment`
**api-ms-win-crt-stdio-l1-1-0.dll**: `_set_fmode`, `__p__commode`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

### Exports

`DotNetRuntimeDebugHeader`

## Extracted Strings

Total strings found: **22607** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.managed
`hydrated
.rdata
@.data
.pdata
@.rsrc
@.reloc
AQAWAVAUATWVSh
L$XAQL
0]AZAZ[^_A\A]A^A_AZ
0]AZAZ[^_A\A]A^A_AZ
AQAWAVAUATWVSh
L$XAQL
0]AZAZ[^_A\A]A^A_AZ
0]AZAZ[^_A\A]A^A_AZ
fffffff
uoH;_*d
rfH;^*d
H;=c)d
riH;=b)d
r6H;G
fffffff
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
|$ AVH
WATAUAVAWH
 A_A^A]A\_
PAWAVAUATWVSQRUH
8]XX[^_A\A]A^A_XX
8]XX[^_A\A]A^A_XXH
QAWAVAUATWVSh
0]AZAZ[^_A\A]A^A_AZ
|$0t,J
|$ AVH
SUVWATAUAVAWH
A_A^A]A\_^][
|$ AVH
SATAUAWH
hA_A]A\[
L+A L;
A(H+Q H;
@UWAVAWH
(A_A^_]
(A_A^_]
H;YiZ
tTH;XiZ
|$ ATAVAWH
0A_A^A\
VWATAUAVAWL
A_A^A]A\_^
|$ AVH
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
SUVWATAUAVAWH
{H9|$ t
8A_A^A]A\_^][
SWAUAVH
8A^A]_[
|$ AVL
|$ AVL
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140091fc0` | `0x140091fc0` | 2714404 | ✓ |
| `fcn.14007be20` | `0x14007be20` | 1972252 | ✓ |
| `fcn.1400037a8` | `0x1400037a8` | 1890435 | ✓ |
| `fcn.140173f00` | `0x140173f00` | 1709274 | ✓ |
| `fcn.1402eedf0` | `0x1402eedf0` | 1654752 | ✓ |
| `fcn.1402b3b60` | `0x1402b3b60` | 1592465 | ✓ |
| `fcn.1402b3c60` | `0x1402b3c60` | 1289377 | ✓ |
| `fcn.1402b3e40` | `0x1402b3e40` | 1262102 | ✓ |
| `fcn.140242980` | `0x140242980` | 938526 | ✓ |
| `fcn.1401af9c0` | `0x1401af9c0` | 877153 | ✓ |
| `fcn.1401b06f0` | `0x1401b06f0` | 874057 | ✓ |
| `fcn.140242270` | `0x140242270` | 832748 | ✓ |
| `fcn.140242150` | `0x140242150` | 803342 | ✓ |
| `fcn.1401d1550` | `0x1401d1550` | 785375 | ✓ |
| `fcn.1401fbe70` | `0x1401fbe70` | 645951 | ✓ |
| `fcn.140231350` | `0x140231350` | 564661 | ✓ |
| `fcn.1402a3bc0` | `0x1402a3bc0` | 516728 | ✓ |
| `fcn.1401657a0` | `0x1401657a0` | 504937 | ✓ |
| `fcn.1403243c0` | `0x1403243c0` | 486365 | ✓ |
| `fcn.14017be40` | `0x14017be40` | 406933 | ✓ |
| `fcn.1401e0970` | `0x1401e0970` | 347045 | ✓ |
| `fcn.140011460` | `0x140011460` | 342658 | ✓ |
| `fcn.1401811f0` | `0x1401811f0` | 287607 | ✓ |
| `fcn.140049730` | `0x140049730` | 221173 | ✓ |
| `fcn.140049740` | `0x140049740` | 219670 | ✓ |
| `fcn.140049550` | `0x140049550` | 218705 | ✓ |
| `fcn.140049710` | `0x140049710` | 218186 | ✓ |
| `fcn.1400497b0` | `0x1400497b0` | 216341 | ✓ |
| `fcn.140049700` | `0x140049700` | 202773 | ✓ |
| `fcn.1401b09a0` | `0x1401b09a0` | 192065 | ✓ |

### Decompiled Code Files

- [`code/fcn.1400037a8.c`](code/fcn.1400037a8.c)
- [`code/fcn.140011460.c`](code/fcn.140011460.c)
- [`code/fcn.140049550.c`](code/fcn.140049550.c)
- [`code/fcn.140049700.c`](code/fcn.140049700.c)
- [`code/fcn.140049710.c`](code/fcn.140049710.c)
- [`code/fcn.140049730.c`](code/fcn.140049730.c)
- [`code/fcn.140049740.c`](code/fcn.140049740.c)
- [`code/fcn.1400497b0.c`](code/fcn.1400497b0.c)
- [`code/fcn.14007be20.c`](code/fcn.14007be20.c)
- [`code/fcn.140091fc0.c`](code/fcn.140091fc0.c)
- [`code/fcn.1401657a0.c`](code/fcn.1401657a0.c)
- [`code/fcn.140173f00.c`](code/fcn.140173f00.c)
- [`code/fcn.14017be40.c`](code/fcn.14017be40.c)
- [`code/fcn.1401811f0.c`](code/fcn.1401811f0.c)
- [`code/fcn.1401af9c0.c`](code/fcn.1401af9c0.c)
- [`code/fcn.1401b06f0.c`](code/fcn.1401b06f0.c)
- [`code/fcn.1401b09a0.c`](code/fcn.1401b09a0.c)
- [`code/fcn.1401d1550.c`](code/fcn.1401d1550.c)
- [`code/fcn.1401e0970.c`](code/fcn.1401e0970.c)
- [`code/fcn.1401fbe70.c`](code/fcn.1401fbe70.c)
- [`code/fcn.140231350.c`](code/fcn.140231350.c)
- [`code/fcn.140242150.c`](code/fcn.140242150.c)
- [`code/fcn.140242270.c`](code/fcn.140242270.c)
- [`code/fcn.140242980.c`](code/fcn.140242980.c)
- [`code/fcn.1402a3bc0.c`](code/fcn.1402a3bc0.c)
- [`code/fcn.1402b3b60.c`](code/fcn.1402b3b60.c)
- [`code/fcn.1402b3c60.c`](code/fcn.1402b3c60.c)
- [`code/fcn.1402b3e40.c`](code/fcn.1402b3e40.c)
- [`code/fcn.1402eedf0.c`](code/fcn.1402eedf0.c)
- [`code/fcn.1403243c0.c`](code/fcn.1403243c0.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is a technical analysis of the binary's functionality.

### Core Functionality and Purpose
The binary appears to be a **loader or a "packer" stub**, likely for malware. The structure suggests that it is not an end-user application but rather a component designed to decrypt/unpack and execute a secondary, hidden payload. Several indicators point toward this:
*   **Runtime Orchestration:** Many functions (e.g., `fcn.1402b3c60`, `fcn.1401811f0`) act as dispatchers or "gatekeepers," checking internal states before allowing a transition to the next stage of execution.
*   **Obfuscation/De-obfuscation:** Several functions (notably `fcn.1402eedf0`) contain complex bitwise operations and loops that are characteristic of **decryption routines**. These are used to "unpack" code segments in memory before they are executed.

### Suspicious or Malicious Behaviors
The following behaviors are indicative of malicious activity:

*   **Payload Decryption/De-obfuscation:** 
    *   `fcn.1402eedf0` performs complex bitwise rotations and shifts (`uVar4 >> 0x38 | (uVar4 & 0xff000000000000) >> 0x28...`). This is a classic technique used to transform encrypted data into executable machine code.
    *   `fcn.1402b3e40` contains logic that swaps and mutates memory blocks, often seen in **"in-place" unpacking**, where the loader modifies its own memory or a mapped buffer to prepare it for execution.

*   **Anti-Analysis/Environment Checks:**
    *   The frequent use of `swi(3)` (Software Interrupt 3) at various points in the code is highly suspicious. In this context, it acts as an "abort" mechanism; if the code detects a debugger, an environment that doesn't meet specific criteria, or an integrity failure, it intentionally crashes via an exception to halt analysis.

*   **Multi-threaded Execution:**
    *   `fcn.1401811f0` calls `CreateThreadpoolWork` and `SubmitThreadpoolWork`. This is a common technique for malware to move malicious tasks (such as network communication, keylogging, or file encryption) into background threads to evade simple detection and ensure the main process remains responsive.

*   **Dynamic Resolution/Indirect Offsets:**
    *   The code frequently uses indirect calls where functions are called via memory addresses calculated at runtime rather than standard imports (e.g., `(**0x140638fc0)(arg2)`). This is used to hide the true API being called from static analysis tools.

### Notable Techniques or Patterns
*   **Managed Code Artifacts:** The presence of the `.managed` string in the dump suggests this might be a **.NET assembly compiled with a custom toolchain** (like IL2CPP) or a heavily mangled managed executable.
*   **Data Parsing Logic:** `fcn.140173f00` contains logic to parse specific byte patterns (e.g., checking for `0x2b`, `0x2e`). This suggests it is processing an internal configuration file or a resource blob that contains the settings for the next stage of the malware's lifecycle.
*   **Instruction/Block Obfuscation:** The repeated use of "jump table" warnings and complex loops in functions like `fcn.1401811f0` suggests a **Virtual Machine (VM) or an emulator-based obfuscation** layer, where the original logic is translated into a custom bytecode that the loader executes.

### Summary for Incident Response
This binary functions as a **dropper/loader**. It uses complex bitwise decryption to unpack a payload in memory and utilizes multi-threading to execute that payload while using "swi(3)" traps and indirect branching to hinder reverse engineering efforts. It is highly likely part of a sophisticated malware suite.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027.001** | Obfuscated Executables | The binary utilizes complex bitwise rotations and "in-place" memory mutation to decrypt and unpack a secondary payload from an obfuscated state. |
| **T1036** | Debugger Detection | The use of `swi(3)` (Software Interrupt 3) as an abort mechanism is designed to crash the process if a debugger or analysis environment is detected. |
| **T1106** | Native API | The implementation of indirect calls and runtime-calculated memory addresses for function execution hides the actual APIs being called from static analysis. |
| **T1568** | Dynamic Resolution | The binary's use of internal dispatchers and dynamic offset calculations to determine function locations at runtime is a common tactic to bypass static import monitoring. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Strings" section contains high volumes of obfuscated/encrypted data; no plaintext IP addresses or clear-text URLs were identified within those segments.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (While internal memory offsets such as `0x140638fc0` were mentioned in the analysis, these are not persistent file paths or registry keys).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Execution Technique:** Use of `CreateThreadpoolWork` and `SubmitThreadpoolWork` (indicative of multi-threaded execution to hide malicious activities in the background).
*   **Anti-Analysis Behavior:** Employment of `swi(3)` (Software Interrupt 3) as a deliberate exception/abort mechanism to detect debuggers or non-standard execution environments.
*   **Obfuscation Technique:** Inclusion of "in-place" unpacking and bitwise rotation routines (`0x38`, `0xff` masks) used to de-obfuscate payload code in memory.
*   **Configuration Parsing:** Internal logic identifies specific byte patterns (`0x2b`, `0x2e`) to parse internal configuration files or resource blobs for the next stage of execution.
*   **Malware Type:** Identified as a **Loader/Packer stub**.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
* **Decryption & Unpacking Logic:** The binary contains sophisticated bitwise rotation routines (`fcn.1402eedf0`) and "in-place" memory mutation, confirming its primary role is to decrypt a hidden payload into memory before execution.
* **Anti-Analysis Techniques:** The use of `swi(3)` (Software Interrupt 3) as an abort mechanism specifically designed to crash the process if a debugger or unauthorized environment is detected highlights its intent to evade analysis.
* **Evasion-Oriented Execution:** The combination of dynamic API resolution (hiding imports), multi-threaded execution via `CreateThreadpoolWork`, and internal configuration parsing indicates it is a professional-grade loader intended to facilitate a more complex secondary payload.
