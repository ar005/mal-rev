# Threat Analysis Report

**Generated:** 2026-07-18 14:06 UTC
**Sample:** `08887f949d9a15dba1d89e4a0a4e37435856cd0de5f3d739f1fad40382bed71b_08887f949d9a15dba1d89e4a0a4e37435856cd0de5f3d739f1fad40382bed71b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `08887f949d9a15dba1d89e4a0a4e37435856cd0de5f3d739f1fad40382bed71b_08887f949d9a15dba1d89e4a0a4e37435856cd0de5f3d739f1fad40382bed71b.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 8 sections |
| Size | 23,367,680 bytes |
| MD5 | `9f64ea9bfd8954057df175532d27088a` |
| SHA1 | `58e348df4088d9fdcf7a7d37eec0a04575127a8b` |
| SHA256 | `08887f949d9a15dba1d89e4a0a4e37435856cd0de5f3d739f1fad40382bed71b` |
| Overall entropy | 7.143 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1772969062 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 534,016 | 6.619 | No |
| `.managed` | 9,993,728 | 6.435 | No |
| `hydrated` | 0 | 0.0 | No |
| `.rdata` | 10,454,016 | 7.245 | ⚠️ Yes |
| `.data` | 77,824 | 5.276 | No |
| `.pdata` | 818,176 | 6.752 | No |
| `.rsrc` | 2,048 | 3.546 | No |
| `.reloc` | 1,486,848 | 4.072 | No |

### Imports

**ADVAPI32.dll**: `OpenProcessToken`, `GetTokenInformation`, `RegOpenKeyExW`, `RegQueryValueExW`, `RegCloseKey`, `RegEnumKeyExW`, `OpenThreadToken`, `RevertToSelf`, `ImpersonateLoggedOnUser`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`
**bcrypt.dll**: `BCryptDestroyKey`, `BCryptOpenAlgorithmProvider`, `BCryptImportKeyPair`, `BCryptImportKey`, `BCryptHashData`, `BCryptDestroyHash`, `BCryptFinishHash`, `BCryptExportKey`, `BCryptDecrypt`, `BCryptEncrypt`, `BCryptCreateHash`, `BCryptGenRandom`, `BCryptCloseAlgorithmProvider`, `BCryptSetProperty`, `BCryptGetProperty`
**CRYPT32.dll**: `CertFreeCertificateChainEngine`, `CertCloseStore`, `PFXImportCertStore`, `PFXExportCertStore`, `CryptFindOIDInfo`, `CryptQueryObject`, `CryptMsgGetParam`, `CryptMsgClose`, `CryptImportPublicKeyInfoEx2`, `CryptFormatObject`, `CryptDecodeObject`, `CertVerifyTimeValidity`, `CertSetCertificateContextProperty`, `CertSerializeCertificateStoreElement`, `CertSaveStore`
**IPHLPAPI.DLL**: `GetAdaptersAddresses`, `GetPerAdapterInfo`, `GetNetworkParams`, `if_nametoindex`
**KERNEL32.dll**: `RtlUnwindEx`, `InitializeSListHead`, `InterlockedFlushSList`, `RtlPcToFileHeader`, `RaiseException`, `FlsFree`, `EncodePointer`, `K32GetProcessMemoryInfo`, `GetProcessGroupAffinity`, `SetLastError`, `GetLastError`, `CloseHandle`, `GetCurrentProcess`, `WaitForSingleObject`, `GetCurrentProcessId`
**ncrypt.dll**: `NCryptImportKey`, `NCryptDeleteKey`, `NCryptOpenStorageProvider`, `NCryptFreeObject`, `NCryptSetProperty`, `NCryptGetProperty`, `NCryptOpenKey`
**ole32.dll**: `CoUninitialize`, `CoInitializeEx`, `CoTaskMemFree`, `CoTaskMemAlloc`, `CoGetContextToken`, `CoCreateGuid`, `CoWaitForMultipleHandles`, `CoGetApartmentType`
**OLEAUT32.dll**: `VariantClear`, `SysFreeString`, `SysAllocStringLen`
**WS2_32.dll**: `WSASend`, `WSARecv`, `WSAGetOverlappedResult`, `WSAConnect`, `shutdown`, `setsockopt`, `send`, `select`, `GetAddrInfoW`, `ioctlsocket`, `getsockopt`, `getpeername`, `bind`, `WSAIoctl`, `WSAEventSelect`
**api-ms-win-crt-heap-l1-1-0.dll**: `calloc`, `_callnewh`, `malloc`, `realloc`, `free`
**api-ms-win-crt-math-l1-1-0.dll**: `tanf`, `atanf`, `asinf`, `acosf`, `nanf`, `_dclass`, `cbrtf`, `_fdclass`, `fmod`, `fmodf`, `log10f`, `nan`, `ceil`, `cos`, `exp`
**api-ms-win-crt-string-l1-1-0.dll**: `strcmp`, `_stricmp`, `strlen`, `strcpy_s`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_initterm`, `_initterm_e`, `_seh_filter_dll`, `_configure_narrow_argv`, `_initialize_narrow_environment`, `_initialize_onexit_table`, `_register_onexit_function`, `_execute_onexit_table`, `_crt_atexit`, `_cexit`, `terminate`, `abort`

### Exports

`0Ol9Ijk4ZjzGTSRJB3yC3VfR0DWvTW`, `0pm7yRyADSugd2xCNW`, `1syqCjGdWjHjyuUx1HY2`, `2MNBSbkY8Pm`, `2OCZmmo7PgNI3Wo`, `50SfyPe64VLW9BD9pTK0zBfRf5`, `5NS0hqAbUGuZ8cJmOC1`, `5cUMIfXdP937Dw`, `5gUY4dr5QCG6zD9J7uAyQ5ICW6qm8`, `6TX0TNk`, `7q12tIjUxjeoxdptTIuT`, `8PdVXnyrQ1XnuMvmgTMYf5xkYG`, `A8OvIqpV5x7mQ1hZHpd7dT3n1HUO`, `B9sytjCt`, `CLwHHyI7wfWyInf`, `COYkJTuUYvThgECOCSeUJv`, `Ch44muGXof1pgahuKm1xZR0F`, `Ck0gaPn04G9mIcnIlhR6ui5xA`, `D0h7DRUjdUEQyfSTE5fwM`, `DKtwSqRLHkfhazG0O`, `DsPPur4AbJdmwmrwgzh8mBa13Q2`, `GetUtfMode`, `HWKCLhpxjimkOiywkpHhXyRqg`, `HixMgoSBIvFtU`, `IhkH5IQVDL1R24K5jX5oiRWitM5`, `JCuq4MonIrO5gaa4hK`, `KCaCSvUG2PJ2MIByDHkyTD`, `KfO6xFNAE0EdMKloxca8WW9EdfQr`, `LookupStringInFixedSet`, `NCe9jjcLV`, `NPqo06yZ73A4A2X`, `OJXZOHQR`, `P7TTVGo`, `PSa2gYmgOyVlKxmu3mQvfba`, `RcpghVTbm6ECiQ2z`, `SKPwkOX`, `Sm0G77cHH6Xtry`, `T0GQqvktKgZDmbm`, `TASXik1wCl6h2R1xx`, `TEk3pJKK85rteuh`, `UCUHaEi7dQXx9qy5`, `VyFWTaAQ`, `WFaZDDs9SLV8rc0j0KrdyuXgXJqLUn`, `WInCPKM4ZAiVzMi29eRTK`, `WLfa62HUpCYH72jxr1W8`, `WeZV9IYDQ8LBq4bem5x6Y`, `Y5Em6ephhQzmjWzp7CnL`, `YyqpnGpCaNrrBq4ykOU96RF`, `Zsq5EzwltzZ0KFFSkCRbMfR3o`, `afKZkUOBY0N`

## Extracted Strings

Total strings found: **64750** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.managed(|
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
SATAUAWH
hA_A]A\[
|$ AVH
UVWATAUAVAWH
A_A^A]A\_^]
|$ AVH
L+A L;
A(H+Q H;
@WAUAVAWH
(A_A^A]_
(A_A^A]_
|$ ATAVAWH
0A_A^A\
VWATAUAVAWH
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
SUVWATAUAVH
{H9|$ t
@A^A]A\_^][
SWAUAVH
8A^A]_[
|$ AVL
|$ AVL
|$ AVH
VAVAWH
 A_A^^
\$Dt
A
d$P9AXs7
T$Hu:A
\$ UVWH
(D$@E3
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.18009ede0` | `0x18009ede0` | 9498249 | ✓ |
| `fcn.180183de0` | `0x180183de0` | 8573065 | ✓ |
| `fcn.1801480f0` | `0x1801480f0` | 7930014 | ✓ |
| `fcn.18085f4e0` | `0x18085f4e0` | 7296597 | ✓ |
| `fcn.1802da980` | `0x1802da980` | 7276932 | ✓ |
| `fcn.180213540` | `0x180213540` | 6666597 | ✓ |
| `fcn.1801318e0` | `0x1801318e0` | 5902938 | ✓ |
| `fcn.180400920` | `0x180400920` | 5688250 | ✓ |
| `fcn.18087dd20` | `0x18087dd20` | 5256305 | ✓ |
| `fcn.1804e1880` | `0x1804e1880` | 5097973 | ✓ |
| `fcn.180191b40` | `0x180191b40` | 4763222 | ✓ |
| `fcn.18087f390` | `0x18087f390` | 4690673 | ✓ |
| `fcn.18087f580` | `0x18087f580` | 4658614 | ✓ |
| `fcn.1800062ff` | `0x1800062ff` | 4640396 | ✓ |
| `fcn.180279dc0` | `0x180279dc0` | 4411596 | ✓ |
| `fcn.18059e970` | `0x18059e970` | 4302615 | ✓ |
| `fcn.1809ad950` | `0x1809ad950` | 3727490 | ✓ |
| `fcn.1806485c0` | `0x1806485c0` | 3631662 | ✓ |
| `fcn.18010f720` | `0x18010f720` | 3455806 | ✓ |
| `fcn.180647eb0` | `0x180647eb0` | 3217196 | ✓ |
| `fcn.180444990` | `0x180444990` | 3196609 | ✓ |
| `fcn.180445900` | `0x180445900` | 3192937 | ✓ |
| `fcn.180647d90` | `0x180647d90` | 3162094 | ✓ |
| `fcn.1804736c0` | `0x1804736c0` | 3122735 | ✓ |
| `fcn.1804a6c10` | `0x1804a6c10` | 2949599 | ✓ |
| `fcn.180745700` | `0x180745700` | 2636155 | ✓ |
| `fcn.18094baa0` | `0x18094baa0` | 2477922 | ✓ |
| `fcn.18094f2a0` | `0x18094f2a0` | 2471017 | ✓ |
| `fcn.180955180` | `0x180955180` | 2466713 | ✓ |
| `fcn.18094ee60` | `0x18094ee60` | 2465898 | ✓ |

### Decompiled Code Files

- [`code/fcn.1800062ff.c`](code/fcn.1800062ff.c)
- [`code/fcn.18009ede0.c`](code/fcn.18009ede0.c)
- [`code/fcn.18010f720.c`](code/fcn.18010f720.c)
- [`code/fcn.1801318e0.c`](code/fcn.1801318e0.c)
- [`code/fcn.1801480f0.c`](code/fcn.1801480f0.c)
- [`code/fcn.180183de0.c`](code/fcn.180183de0.c)
- [`code/fcn.180191b40.c`](code/fcn.180191b40.c)
- [`code/fcn.180213540.c`](code/fcn.180213540.c)
- [`code/fcn.180279dc0.c`](code/fcn.180279dc0.c)
- [`code/fcn.1802da980.c`](code/fcn.1802da980.c)
- [`code/fcn.180400920.c`](code/fcn.180400920.c)
- [`code/fcn.180444990.c`](code/fcn.180444990.c)
- [`code/fcn.180445900.c`](code/fcn.180445900.c)
- [`code/fcn.1804736c0.c`](code/fcn.1804736c0.c)
- [`code/fcn.1804a6c10.c`](code/fcn.1804a6c10.c)
- [`code/fcn.1804e1880.c`](code/fcn.1804e1880.c)
- [`code/fcn.18059e970.c`](code/fcn.18059e970.c)
- [`code/fcn.180647d90.c`](code/fcn.180647d90.c)
- [`code/fcn.180647eb0.c`](code/fcn.180647eb0.c)
- [`code/fcn.1806485c0.c`](code/fcn.1806485c0.c)
- [`code/fcn.180745700.c`](code/fcn.180745700.c)
- [`code/fcn.18085f4e0.c`](code/fcn.18085f4e0.c)
- [`code/fcn.18087dd20.c`](code/fcn.18087dd20.c)
- [`code/fcn.18087f390.c`](code/fcn.18087f390.c)
- [`code/fcn.18087f580.c`](code/fcn.18087f580.c)
- [`code/fcn.18094baa0.c`](code/fcn.18094baa0.c)
- [`code/fcn.18094ee60.c`](code/fcn.18094ee60.c)
- [`code/fcn.18094f2a0.c`](code/fcn.18094f2a0.c)
- [`code/fcn.180955180.c`](code/fcn.180955180.c)
- [`code/fcn.1809ad950.c`](code/fcn.1809ad950.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C pseudocode, here is an analysis of the binary's behavior and characteristics.

### **Core Functionality**
The code appears to be part of a highly obfuscated **malware loader or an execution stub**. Rather than performing high-level logic directly, the primary purpose of these functions is to manage a complex internal state machine, resolve symbols/functions dynamically, and navigate through "flattened" control flows.

### **Suspicious & Malicious Behaviors**
*   **API Hashing / Dynamic Resolution:** 
    *   Function `fcn.18010f720` is a classic example of an **API resolver**. It compares internal identifiers (e.g., `0x180bc6708`, `0x180bc3d28`) against constants to decide which functionality or value to return. This technique is used to hide calls to sensitive Windows APIs (like those for process injection, file manipulation, or network communication) from static analysis tools.
*   **Complex Dispatcher Logic:** 
    *   Function `fcn.18009ede0` acts as a complex dispatcher. It uses nested conditional logic and numerous internal jumps to decide the next step of execution. This is typical in malware designed to hide its true purpose behind layers of "decisions" that are only resolved at runtime.
*   **Information Obfuscation:** 
    *   The `EXTRACTED STRINGS` section shows high-entropy, non-human-readable character sets. This suggests the presence of **packed data**, encrypted strings, or a custom virtual machine (VM) instruction set where the code operates on "opcodes" rather than standard text.
*   **State Machine Navigation:** 
    *   Functions like `fcn.180213540` and `fcn.180745700` contain deep loops and switch-like structures to navigate internal data tables. This is often indicative of **Control Flow Flattening**, a technique used to make the program's logical path nearly impossible to follow in a standard decompiler.

### **Notable Techniques & Patterns**
*   **Control Flow Flattening (CFF):** The heavy use of jump tables and indirect calls (`UNRECOVERED_JUMPTABLE`) suggests the code has been processed by an obfuscator like **LLVM-Obfuscator (OLLVM)** or similar tools. This makes it difficult to determine the "true" logic path during analysis.
*   **Internal Table Lookups:** Functions `fcn.18094baa0` and `fcn.18094ee60` share very similar structures, likely used for resolving internal offsets or handling different types of system resources by iterating through a table and checking status codes.
*   **Data-Driven Execution:** The code frequently checks flags (e.g., `if (iVar2 != 0)` or `if (uVar13 == 0)`) before jumping to various handlers. This suggests the malware's behavior changes based on environmental factors or internal "tasks" assigned during execution.
*   **Manual String/Buffer Processing:** Function `fcn.180400920` contains logic for manual string validation and conversion (detecting hex, calculating lengths). This is often used to process configuration files or C2 (Command & Control) commands.

### **Summary of Evidence**
The presence of **API Hashing**, **Control Flow Flattening**, and a heavy reliance on **internal state-machine dispatchers** indicates this is likely an advanced malware sample designed for evasion. It aims to prevent automated analysis tools from mapping its full capabilities until it is executed in memory.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Capabilities | The use of API hashing, control flow flattening, and complex dispatcher logic are employed to hide the binary's true functionality from static analysis. |
| T1027.001 | Compile Obfuscated Virtual Machine | The presence of high-entropy character sets and code that operates on "opcodes" suggests a custom VM is used to execute commands in an obfuscated manner. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral reports, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*None identified.* (The behavior report mentions C2 communication, but no specific network indicators were present in the provided text.)

### **File paths / Registry keys**
*None identified.*

### **Mutex names / Named pipes**
*None identified.* (While several non-human-readable strings were present, such as `AQAWAVAUATWVSh` and `L$XAQL`, they do not follow standard naming conventions for mutexes or named pipes and appear to be obfuscated internal data/opcodes.)

### **Hashes**
*None identified.* (No MD5, SHA1, or SHA256 hashes were present in the provided strings.)

### **Other artifacts**
*   **Malicious Techniques:**
    *   **API Hashing / Dynamic Resolution:** The binary uses a resolver (`fcn.18010f720`) to hide its calls to sensitive Windows APIs by comparing internal constants (e.g., `0x180bc6708`, `0x180bc3d28`).
    *   **Control Flow Flattening (CFF):** The sample uses complex jump tables and indirect calls, likely via **OLLVM**, to obscure its logic path.
    *   **Obfuscated Instruction Set:** High-entropy strings suggest a custom VM or a packed/encrypted payload.
    *   **Manual String Validation:** Logic exists specifically for processing potentially encoded C2 commands or configuration data.
*   **Internal Offsets (Not External IOCs, but significant for behavioral tracking):**
    *   `fcn.18010f720` (API Resolver)
    *   `fcn.18009ede0` (Dispatcher)
    *   `fcn.180213540` / `fcn.180745700` (State Machine Navigation)

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1. **Malware family**: Unknown (Potential custom loader)
2. **Malware type**: Loader
3. **Confidence**: High (regarding its role as a loader), Medium (regarding specific family identification)
4. **Key evidence**:
    *   **Advanced Evasion Techniques:** The use of Control Flow Flattening (CFF), API hashing, and dynamic resolution indicates the sample is designed specifically to evade static analysis and hide its true functionality until execution.
    *   **Stub/Loader Characteristics:** The behavior analysis highlights that the code lacks high-level logic but excels at state-machine navigation and manual string processing—core characteristics of a loader or "stub" intended to unpack or decrypt subsequent payloads.
    *   **Complex Architecture:** The presence of potential custom VM instruction sets (high-entropy data/opcodes) and complex dispatcher logic suggests an advanced, sophisticated design typically found in modern malware infrastructure used to facilitate multi-stage infections.
