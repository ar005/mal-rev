# Threat Analysis Report

**Generated:** 2026-07-13 18:35 UTC
**Sample:** `055b2574f0bee2eda19ce1d45aed9372a7277719ffe346c1a8b52f5acc9ed3bc_055b2574f0bee2eda19ce1d45aed9372a7277719ffe346c1a8b52f5acc9ed3bc.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `055b2574f0bee2eda19ce1d45aed9372a7277719ffe346c1a8b52f5acc9ed3bc_055b2574f0bee2eda19ce1d45aed9372a7277719ffe346c1a8b52f5acc9ed3bc.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 9 sections |
| Size | 6,411,776 bytes |
| MD5 | `5336158a1998df7985395e3d043c2400` |
| SHA1 | `d6174eeb298b4b0f421860093ebb0721f6a8c29a` |
| SHA256 | `055b2574f0bee2eda19ce1d45aed9372a7277719ffe346c1a8b52f5acc9ed3bc` |
| Overall entropy | 6.942 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1763583087 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 495,616 | 6.624 | No |
| `.managed` | 3,109,376 | 6.427 | No |
| `hydrated` | 0 | 0.0 | No |
| `.rdata` | 2,508,800 | 7.026 | ⚠️ Yes |
| `.data` | 23,040 | 4.762 | No |
| `.pdata` | 268,800 | 6.401 | No |
| `_RDATA` | 512 | 3.329 | No |
| `.rsrc` | 1,024 | 4.998 | No |
| `.reloc` | 3,584 | 5.417 | No |

### Imports

**ADVAPI32.dll**: `RegCreateKeyExW`, `RegOpenKeyExW`, `RegQueryValueExW`, `RegSetValueExW`, `RegCloseKey`, `OpenProcessToken`, `LookupPrivilegeValueW`, `AdjustTokenPrivileges`, `RegEnumKeyExW`, `RegEnumValueW`
**bcrypt.dll**: `BCryptOpenAlgorithmProvider`, `BCryptHashData`, `BCryptDestroyHash`, `BCryptFinishHash`, `BCryptGetProperty`, `BCryptGenRandom`, `BCryptCreateHash`, `BCryptCloseAlgorithmProvider`
**KERNEL32.dll**: `TlsFree`, `TlsSetValue`, `TlsGetValue`, `TlsAlloc`, `InitializeCriticalSectionAndSpinCount`, `EncodePointer`, `RaiseException`, `RtlPcToFileHeader`, `SetLastError`, `GetLastError`, `QueryPerformanceCounter`, `GetTickCount64`, `FormatMessageW`, `LocalFree`, `GetCPInfoExW`
**ole32.dll**: `CoGetApartmentType`, `CoTaskMemAlloc`, `CoUninitialize`, `CoInitializeEx`, `CoCreateGuid`, `CoWaitForMultipleHandles`
**USER32.dll**: `LoadStringW`
**api-ms-win-crt-heap-l1-1-0.dll**: `malloc`, `free`, `_set_new_mode`, `calloc`, `_callnewh`
**api-ms-win-crt-math-l1-1-0.dll**: `_fdclass`, `fmod`, `_dclass`, `nanf`, `nan`, `modf`, `tan`, `sin`, `__setusermatherr`, `cos`, `pow`, `ceil`, `floor`, `fmodf`
**api-ms-win-crt-string-l1-1-0.dll**: `strcmp`, `wcsncmp`, `strcpy_s`, `strlen`, `_stricmp`, `strncpy_s`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-runtime-l1-1-0.dll**: `terminate`, `_crt_atexit`, `_register_onexit_function`, `_initialize_onexit_table`, `abort`, `_register_thread_local_exe_atexit_callback`, `_c_exit`, `_cexit`, `__p___wargv`, `__p___argc`, `_exit`, `exit`, `_initterm_e`, `_initterm`, `_get_initial_wide_environment`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__acrt_iob_func`, `__stdio_common_vsscanf`, `__p__commode`, `__stdio_common_vsprintf_s`, `__stdio_common_vfprintf`, `_set_fmode`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

## Extracted Strings

Total strings found: **24979** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.managed
`hydrated
.rdata
@.data
.pdata
@_RDATA
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
rfH;}
rfH;z
fffffff
PAWAVAUATWVSQRUH
8]XX[^_A\A]A^A_XX
8]XX[^_A\A]A^A_XXH
QAWAVAUATWVSh
0]AZAZ[^_A\A]A^A_AZ
|$ AVH
WATAUAVAWH
 A_A^A]A\_
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
|$ AVH
UVWATAUAVAWH
A_A^A]A\_^]
|$ AVH
L+A L;
A(H+Q H;
SATAUAWH
hA_A]A\[
@WAUAVAWH
(A_A^A]_
(A_A^A]_
tTH;h
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140002f1d` | `0x140002f1d` | 1775294 | ✓ |
| `fcn.140152520` | `0x140152520` | 1581121 | ✓ |
| `fcn.140254400` | `0x140254400` | 1104283 | ✓ |
| `fcn.14032f0c0` | `0x14032f0c0` | 1023720 | ✓ |
| `fcn.140256880` | `0x140256880` | 927146 | ✓ |
| `fcn.14018f740` | `0x14018f740` | 839857 | ✓ |
| `fcn.1401b4af0` | `0x1401b4af0` | 711999 | ✓ |
| `fcn.1400cf140` | `0x1400cf140` | 691106 | ✓ |
| `fcn.1402aaca0` | `0x1402aaca0` | 683100 | ✓ |
| `fcn.140351810` | `0x140351810` | 682240 | ✓ |
| `fcn.1401d8df0` | `0x1401d8df0` | 596863 | ✓ |
| `fcn.1402c3af0` | `0x1402c3af0` | 587740 | ✓ |
| `fcn.1403531e0` | `0x1403531e0` | 586880 | ✓ |
| `fcn.140358270` | `0x140358270` | 551630 | ✓ |
| `fcn.140358a70` | `0x140358a70` | 534613 | ✓ |
| `fcn.140009a70` | `0x140009a70` | 425934 | ✓ |
| `fcn.140009b00` | `0x140009b00` | 425796 | ✓ |
| `fcn.1400129d0` | `0x1400129d0` | 389098 | ✓ |
| `fcn.1402e0780` | `0x1402e0780` | 361819 | ✓ |
| `fcn.14016a660` | `0x14016a660` | 358837 | ✓ |
| `fcn.1402e0490` | `0x1402e0490` | 326277 | ✓ |
| `fcn.14016dad0` | `0x14016dad0` | 312535 | ✓ |
| `fcn.1401c2a00` | `0x1401c2a00` | 305957 | ✓ |
| `fcn.1401c2b70` | `0x1401c2b70` | 305369 | ✓ |
| `fcn.14004b140` | `0x14004b140` | 227317 | ✓ |
| `fcn.14004b150` | `0x14004b150` | 225798 | ✓ |
| `fcn.14004af60` | `0x14004af60` | 224833 | ✓ |
| `fcn.14004b120` | `0x14004b120` | 224314 | ✓ |
| `fcn.14004b1c0` | `0x14004b1c0` | 222469 | ✓ |
| `fcn.14004b110` | `0x14004b110` | 203173 | ✓ |

### Decompiled Code Files

- [`code/fcn.140002f1d.c`](code/fcn.140002f1d.c)
- [`code/fcn.140009a70.c`](code/fcn.140009a70.c)
- [`code/fcn.140009b00.c`](code/fcn.140009b00.c)
- [`code/fcn.1400129d0.c`](code/fcn.1400129d0.c)
- [`code/fcn.14004af60.c`](code/fcn.14004af60.c)
- [`code/fcn.14004b110.c`](code/fcn.14004b110.c)
- [`code/fcn.14004b120.c`](code/fcn.14004b120.c)
- [`code/fcn.14004b140.c`](code/fcn.14004b140.c)
- [`code/fcn.14004b150.c`](code/fcn.14004b150.c)
- [`code/fcn.14004b1c0.c`](code/fcn.14004b1c0.c)
- [`code/fcn.1400cf140.c`](code/fcn.1400cf140.c)
- [`code/fcn.140152520.c`](code/fcn.140152520.c)
- [`code/fcn.14016a660.c`](code/fcn.14016a660.c)
- [`code/fcn.14016dad0.c`](code/fcn.14016dad0.c)
- [`code/fcn.14018f740.c`](code/fcn.14018f740.c)
- [`code/fcn.1401b4af0.c`](code/fcn.1401b4af0.c)
- [`code/fcn.1401c2a00.c`](code/fcn.1401c2a00.c)
- [`code/fcn.1401c2b70.c`](code/fcn.1401c2b70.c)
- [`code/fcn.1401d8df0.c`](code/fcn.1401d8df0.c)
- [`code/fcn.140254400.c`](code/fcn.140254400.c)
- [`code/fcn.140256880.c`](code/fcn.140256880.c)
- [`code/fcn.1402aaca0.c`](code/fcn.1402aaca0.c)
- [`code/fcn.1402c3af0.c`](code/fcn.1402c3af0.c)
- [`code/fcn.1402e0490.c`](code/fcn.1402e0490.c)
- [`code/fcn.1402e0780.c`](code/fcn.1402e0780.c)
- [`code/fcn.14032f0c0.c`](code/fcn.14032f0c0.c)
- [`code/fcn.140351810.c`](code/fcn.140351810.c)
- [`code/fcn.1403531e0.c`](code/fcn.1403531e0.c)
- [`code/fcn.140358270.c`](code/fcn.140358270.c)
- [`code/fcn.140358a70.c`](code/fcn.140358a70.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled pseudocode, here is a technical analysis of the sample's behavior:

### Core Functionality and Purpose
The primary purpose of the analyzed code is **evasion and obfuscation** via a **Virtual Machine (VM) based packer/protector**. 

The binary does not perform "direct" malicious actions (like downloading files or injecting processes) in the provided functions. Instead, it serves as a wrapper or "stub." The core logic of the malware has been converted into a custom bytecode and is executed by an internal interpreter. This makes static analysis extremely difficult because the actual malicious intent is hidden within the virtualized instructions rather than standard x86_64 assembly.

### Suspicious or Malicious Behaviors
*   **Virtual Machine (VM) Execution:** Functions such as `fcn.140254400` and `fcn.1402e0780` exhibit the classic hallmarks of a virtual machine interpreter. They utilize large `switch` tables to process "opcodes." For example, the switch cases (e.g., `case 5`, `case 6`, `case 9`) perform bitwise operations and arithmetic on register-like structures to simulate standard CPU instructions.
*   **Anti-Analysis via Code Complexity:** By wrapping functionality in a VM, the author ensures that automated tools and human analysts see only the "interpreter" logic rather than the actual malicious payload (e.g., the actual network protocols or encryption keys).
*   **Implicit Logic Hiding:** The use of various `fcn.1400...` functions indicates a high degree of modularity designed to hide the data flow. For example, any interaction with strings or system resources is likely piped through these intermediate "handler" functions rather than calling Windows APIs directly (or only doing so via decrypted addresses).

### Notable Techniques and Patterns
*   **Interpreter Dispatch Loop:** Functions like `fcn.140254400` use a nested loop/switch structure to fetch, decode, and execute virtual opcodes. This is a common technique used by advanced protectors (e.g., VMProtect or Themida) and high-end malware families (like those from Lazarus Group).
*   **Data Structure Abstraction:** Functions like `fcn.14004b140` and `fcn.14004b150` iterate through memory structures to process data. The use of different constants (e.g., `0x1400135e0`, `0x140013610`) suggests that the code is jumping to different "handler" functions based on a bytecode instruction, effectively hiding the nature of the operation (like moving data vs. adding values).
*   **String/Data Obfuscation:** Function `fcn.14004af60` appears to handle multi-byte data or encoded strings. The logic suggests it is reconstructing data or navigating a jump table, which is often used to hide hardcoded C2 (Command & Control) domains or IP addresses.
*   **Control Flow Flattening:** Many functions contain "state" checks and complex branching that do not correspond to logical application flow but rather to the requirements of the underlying VM engine.

### Summary for Security Reporting
The sample is highly sophisticated. It utilizes **custom bytecode execution** (VM-based obfuscation) to shield its primary functionality. The presence of this technique indicates a high level of professionalism in the development, likely intended to bypass automated sandboxes and frustrate manual reverse engineering. The actual payload remains "hidden" inside the virtualized environment.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1026.003 | Packing | The sample uses a VM-based packer/protector to wrap the core malicious functionality into custom bytecode, making static analysis extremely difficult. |
| T1026 | Obfuscated Files or Information | The use of control flow flattening and complex interpreter dispatch loops is designed to hide the actual logic and requirements of the malware's operation. |
| T1028 | Dynamic Resolution | System resources and functions are accessed through intermediate handler functions rather than direct API calls to mask the intent of the code from automated tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the categorized list of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   None identified (The extracted strings appear to be encoded/obfuscated; no plaintext C2 infrastructure was revealed in the provided text).

### **File paths / Registry keys**
*   None identified.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Obfuscation Technique:** VM-based packer/protector (Custom bytecode execution).
*   **Malware Behavior:** Interpreter Dispatch Loop (utilized to hide actual malicious intent from static analysis).
*   **Malware Behavior:** Control Flow Flattening (used to obscure the logic flow of the application).
*   **Internal Offsets (Potential for identifying similar variants):** 
    *   `0x1400135e0`
    *   `0x140013610`
*   **Note:** The analysis indicates that while C2 domains and IP addresses are likely present in the binary, they are hidden behind custom bytecode instructions and multi-byte data reconstruction (function `fcn.14004af60`).

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: Medium

4. **Key evidence**:
*   **VM-Based Obfuscation:** The sample utilizes a sophisticated virtual machine (VM) protector/packer that converts core logic into custom bytecode, which is common in high-end loaders to hide the true payload from static and dynamic analysis.
*   **Evasive Infrastructure:** The presence of interpreter dispatch loops, control flow flattening, and dynamic resolution indicates it is designed primarily as a "stub" or "wrapper" to protect secondary malicious code (e.g., RATs or info-stealers) rather than performing direct malicious actions itself.
*   **Sophisticated Protection:** The use of complex switch tables and multi-byte data reconstruction to hide indicators like C2 infrastructure suggests the sample is likely a component of a professional malware campaign intended to frustrate manual reverse engineering.
