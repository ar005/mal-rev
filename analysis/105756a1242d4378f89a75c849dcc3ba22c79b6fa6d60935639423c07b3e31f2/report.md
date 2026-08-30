# Threat Analysis Report

**Generated:** 2026-08-18 19:40 UTC
**Sample:** `105756a1242d4378f89a75c849dcc3ba22c79b6fa6d60935639423c07b3e31f2_105756a1242d4378f89a75c849dcc3ba22c79b6fa6d60935639423c07b3e31f2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `105756a1242d4378f89a75c849dcc3ba22c79b6fa6d60935639423c07b3e31f2_105756a1242d4378f89a75c849dcc3ba22c79b6fa6d60935639423c07b3e31f2.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 2,780,672 bytes |
| MD5 | `6d405d6e3d5d991090646e92793a4da6` |
| SHA1 | `e7cec9f2da9fe9a024483e427ae609a1705174e6` |
| SHA256 | `105756a1242d4378f89a75c849dcc3ba22c79b6fa6d60935639423c07b3e31f2` |
| Overall entropy | 7.026 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766687171 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,197,568 | 6.507 | No |
| `.rdata` | 1,340,416 | 7.281 | ⚠️ Yes |
| `.data` | 123,904 | 3.328 | No |
| `.pdata` | 82,432 | 6.108 | No |
| `.rsrc` | 2,560 | 3.923 | No |
| `.reloc` | 32,768 | 5.451 | No |

### Imports

**ADVAPI32.dll**: `DeregisterEventSource`, `RegCloseKey`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryValueExW`, `RegSetValueExW`, `RegisterEventSourceW`, `ReportEventW`, `OpenProcessToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`
**bcrypt.dll**: `BCryptOpenAlgorithmProvider`, `BCryptGenRandom`, `BCryptCloseAlgorithmProvider`, `BCryptCreateHash`, `BCryptDestroyHash`, `BCryptFinishHash`, `BCryptGetProperty`, `BCryptHashData`
**KERNEL32.dll**: `InitializeCriticalSectionEx`, `EncodePointer`, `FlsFree`, `RtlPcToFileHeader`, `InterlockedFlushSList`, `RtlUnwindEx`, `CancelThreadpoolIo`, `CloseHandle`, `CloseThreadpoolIo`, `CloseThreadpoolWork`, `CopyFileExW`, `CreateDirectoryW`, `CreateEventExW`, `CreateFileW`, `CreateThread`
**ole32.dll**: `CoGetApartmentType`, `CoWaitForMultipleHandles`, `CoUninitialize`, `CoTaskMemFree`, `CoTaskMemAlloc`, `CoInitializeEx`, `CoCreateGuid`
**USER32.dll**: `LoadStringW`
**api-ms-win-crt-math-l1-1-0.dll**: `modf`, `log`, `ceil`
**api-ms-win-crt-heap-l1-1-0.dll**: `_callnewh`, `calloc`, `malloc`, `free`
**api-ms-win-crt-string-l1-1-0.dll**: `strcpy_s`, `_stricmp`, `strcmp`, `strcpy`, `strlen`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__stdio_common_vsnprintf_s`
**api-ms-win-crt-runtime-l1-1-0.dll**: `terminate`, `_execute_onexit_table`, `_register_onexit_function`, `_initialize_onexit_table`, `_initialize_narrow_environment`, `_cexit`, `_crt_atexit`, `_configure_narrow_argv`, `_seh_filter_dll`, `_initterm_e`, `abort`, `_initterm`

### Exports

`04s7JWbKN7xMO7TyuvEQdz8Un`, `5MOU3WobEvArsQmjBUYij5cywU`, `5XF3cmmfRFSVtM7LLybReBF2C3lBn`, `65TzCheOAQnWNtky990Ya`, `6PZ1W5HpRStYpktnkbqXXI`, `8TBBFdzo1IQ7KxQi7lBMeX`, `8uuGQl9dT5JmTa995AlNDtBNs`, `AxlnqajPakErRSfgatZbtQNmGAfhMrx7`, `BGMksTVPXRzTajVEdHQ1JDPz8hV5Hx`, `CoreUICallComputeMaximumMessageSize`, `CoreUICallCreateConversationHost`, `CoreUICallCreateEndpointHost`, `CoreUICallCreateEndpointHostWithSendPriority`, `CoreUICallGetAddressOfParameterInBuffer`, `CoreUICallReceive`, `CoreUICallSend`, `CoreUICallSendVaList`, `CoreUIConfigureTestHost`, `CoreUIConfigureUserIntegration`, `CoreUICreate`, `CoreUICreateAnonymousStream`, `CoreUICreateEx`, `CoreUIInitializeTestService`, `CoreUIOpenExisting`, `CoreUIRouteToTestRegistrar`, `CoreUIUninitializeTestService`, `CreateDispatcherQueueController`, `CreateDispatcherQueueForCurrentThread`, `D5vHNdp0`, `DHpzOwFnRBVJVPnum`, `DllCanUnloadNow`, `DllGetActivationFactory`, `DllGetClassObject`, `Ef5FNsOUqshn0`, `EoVBlMYtDqrWeYIls81hE7YCDtkCkHG`, `F3SK7p4m0hDPXVw5dL7z3LdST`, `FHVFb6QMaTr6C7labadT`, `GetDispatcherQueueForCurrentThread`, `GiThBTpSIpLIIQCJstQZz4eCcNCzal`, `HLfn7duSnQNxGHfkhb3J`, `HSFbPCkSUz8cyP46jbf7Dbb8UnJRP`, `HxjmDwngWwvIOmD4maRMxY`, `Ihf4semrdKr5B`, `Iu2BuH7u5aWcgf9kNDmT`, `LWW2uaUz5RozNsmZBMgXnRzmhsbFkRx6`, `LXticY8z1`, `MsgBlobCreateShared`, `MsgBlobCreateStack`, `MsgBufferShare`, `MsgRelease`

## Extracted Strings

Total strings found: **9145** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
UAWAVAUATWVSH
L$M1~
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
~.tdH
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
AVWVUSH
 []^_A^
AWAVWVUSH
([]^_A^A_
([]^_A^A_
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
[^_A\A]A^A_]
UAWAVAUWVSH
e [^_A]A^A_]
e [^_A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVWVSH
h[^_A^A_]
AWAVAUATWVUSH
L3N L3N0L
H3~(H3~8H
L3V L3V0L3V@L
L3N(L3N8L3NHL
^ M1L
H3F H3F0H3F@L
L3F(L3F8L3FHL
H3V H3V0H3V@L
L3^(L3^8L3^HH
[]^_A\A]A^A_
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUWVSH
@[^_A]A^A_]
AWAVAUWVUSH
`[]^_A]A^A_
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.18000e970` | `0x18000e970` | 1115287 | ✓ |
| `fcn.18000e8b0` | `0x18000e8b0` | 833083 | ✓ |
| `fcn.1800d8f14` | `0x1800d8f14` | 803703 | ✓ |
| `fcn.1800d8dd0` | `0x1800d8dd0` | 803548 | ✓ |
| `fcn.18003d300` | `0x18003d300` | 640456 | ✓ |
| `fcn.18003e840` | `0x18003e840` | 632865 | ✓ |
| `fcn.1800bdac0` | `0x1800bdac0` | 629941 | ✓ |
| `fcn.180043580` | `0x180043580` | 613889 | ✓ |
| `fcn.1800b9da0` | `0x1800b9da0` | 593808 | ✓ |
| `fcn.18004ad30` | `0x18004ad30` | 582505 | ✓ |
| `fcn.1800d9920` | `0x1800d9920` | 527529 | ✓ |
| `fcn.180033880` | `0x180033880` | 500690 | ✓ |
| `fcn.1800d94b8` | `0x1800d94b8` | 461132 | ✓ |
| `fcn.1800d911c` | `0x1800d911c` | 449057 | ✓ |
| `fcn.18000f690` | `0x18000f690` | 366709 | ✓ |
| `fcn.180083cd0` | `0x180083cd0` | 352717 | ✓ |
| `fcn.1800a38e0` | `0x1800a38e0` | 284554 | ✓ |
| `fcn.1800e7530` | `0x1800e7530` | 244470 | ✓ |
| `fcn.1800e7580` | `0x1800e7580` | 244390 | ✓ |
| `fcn.18011e380` | `0x18011e380` | 229909 | ✓ |
| `fcn.1800e6860` | `0x1800e6860` | 229189 | ✓ |
| `fcn.18011e390` | `0x18011e390` | 223285 | ✓ |
| `fcn.18011e3a0` | `0x18011e3a0` | 221830 | ✓ |
| `fcn.18011e1c0` | `0x18011e1c0` | 220881 | ✓ |
| `fcn.18011e410` | `0x18011e410` | 218709 | ✓ |
| `fcn.1800e9a10` | `0x1800e9a10` | 217415 | ✓ |
| `fcn.180041590` | `0x180041590` | 208906 | ✓ |
| `fcn.180099f00` | `0x180099f00` | 191326 | ✓ |
| `fcn.1800c5dc0` | `0x1800c5dc0` | 185635 | ✓ |
| `fcn.1800382c0` | `0x1800382c0` | 119017 | ✓ |

### Decompiled Code Files

- [`code/fcn.18000e8b0.c`](code/fcn.18000e8b0.c)
- [`code/fcn.18000e970.c`](code/fcn.18000e970.c)
- [`code/fcn.18000f690.c`](code/fcn.18000f690.c)
- [`code/fcn.180033880.c`](code/fcn.180033880.c)
- [`code/fcn.1800382c0.c`](code/fcn.1800382c0.c)
- [`code/fcn.18003d300.c`](code/fcn.18003d300.c)
- [`code/fcn.18003e840.c`](code/fcn.18003e840.c)
- [`code/fcn.180041590.c`](code/fcn.180041590.c)
- [`code/fcn.180043580.c`](code/fcn.180043580.c)
- [`code/fcn.18004ad30.c`](code/fcn.18004ad30.c)
- [`code/fcn.180083cd0.c`](code/fcn.180083cd0.c)
- [`code/fcn.180099f00.c`](code/fcn.180099f00.c)
- [`code/fcn.1800a38e0.c`](code/fcn.1800a38e0.c)
- [`code/fcn.1800b9da0.c`](code/fcn.1800b9da0.c)
- [`code/fcn.1800bdac0.c`](code/fcn.1800bdac0.c)
- [`code/fcn.1800c5dc0.c`](code/fcn.1800c5dc0.c)
- [`code/fcn.1800d8dd0.c`](code/fcn.1800d8dd0.c)
- [`code/fcn.1800d8f14.c`](code/fcn.1800d8f14.c)
- [`code/fcn.1800d911c.c`](code/fcn.1800d911c.c)
- [`code/fcn.1800d94b8.c`](code/fcn.1800d94b8.c)
- [`code/fcn.1800d9920.c`](code/fcn.1800d9920.c)
- [`code/fcn.1800e6860.c`](code/fcn.1800e6860.c)
- [`code/fcn.1800e7530.c`](code/fcn.1800e7530.c)
- [`code/fcn.1800e7580.c`](code/fcn.1800e7580.c)
- [`code/fcn.1800e9a10.c`](code/fcn.1800e9a10.c)
- [`code/fcn.18011e1c0.c`](code/fcn.18011e1c0.c)
- [`code/fcn.18011e380.c`](code/fcn.18011e380.c)
- [`code/fcn.18011e390.c`](code/fcn.18011e390.c)
- [`code/fcn.18011e3a0.c`](code/fcn.18011e3a0.c)
- [`code/fcn.18011e410.c`](code/fcn.18011e410.c)

## Behavioral Analysis

Based on the analysis of the provided decompiled code, here is a summary of the findings.

### Core Functionality and Purpose
The binary appears to be part of a large, complex software framework (likely a game engine or a high-level system library) rather than a standalone piece of malware. The functions perform low-level memory management, data structure traversal, and coordinate calculations involving time and offsets. 

*   **Memory & Data Management:** Many functions (e.g., `fcn.1800bdac0`, `fcn.1800d94b8`) involve complex checks on buffer sizes, bitmask validations, and pointer arithmetic to navigate nested data structures.
*   **Time/Duration Calculation:** Function `fcn.1800382c0` contains a specific calculation involving the multiplier `864,000,000,000`. This is a common constant used in high-precision systems to convert days into microseconds (or similar units), suggesting it handles scheduling or timestamp calculations.
*   **State Management:** The code frequently checks internal "state" values against hardcoded memory addresses and constants to decide which logic path to take.

### Suspicious or Malicious Behaviors
No immediate "smoking gun" indicators of malicious activity (such as process injection, file deletion, or network communication) were found in the provided sample. 

*   **No Direct Network Activity:** There are no calls related to sockets, HTTP/HTTPS requests, or DNS resolution.
*   **No Process Manipulation:** There is no evidence of `OpenProcess`, `WriteProcessMemory`, or other common injection techniques.
*   **No Persistence Logic:** No registry modifications or service creation code was detected.

### Notable Techniques and Patterns
While the code does not appear to be a "malware" in the traditional sense, it exhibits several characteristics typical of complex software that is often used as a base for sophisticated malware:

*   **Table-Driven Logic:** The extensive use of indirect jumps (e.g., `(**0x180126618)`) and large switch statements based on internal codes suggests a highly modular, state-driven architecture.
*   **Complex Validation Checks:** Many functions perform heavy bitwise operations and multi-step comparisons before proceeding. In a malware context, this is sometimes used to "hide" the true logic of a function from automated scanners (anti-analysis).
*   **Manual Resource Management:** The use of `LOCK()` and `UNLOCK()` macros indicates that the code is designed to be thread-safe and manage shared memory resources effectively.
*   **Obfuscated String/Data Handling:** While not explicitly shown in the C, the logic in `fcn.1800d9920` and `fcn.1800bdac0` suggests that the code is designed to handle data that may be non-trivial or requires specific parsing rules before it can be used by the application.

### Summary for Analysts
The provided code appears to be **legitimate but complex**. It resembles the logic found in a sophisticated game engine (like Unreal Engine) or an enterprise-level multimedia framework. The complexity of the logic and the lack of standard malicious APIs suggest this is likely not a standalone piece of malware, but if it were found in an unexpected location, it could be a highly-obfuscated "packer" or "stub" designed to hide other functions.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors described in your analysis to the MITRE ATT&CK framework. While the report concludes that the binary may be legitimate software (like a game engine), several characteristics identified—specifically those intended to "hide" logic or handle complex, non-standard data—map directly to techniques used by adversaries to evade detection.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Valid Data | The use of table-driven logic (indirect jumps) and complex multi-step validation checks are noted as methods to "hide" the true logic from automated scanners. |
| **T1027** | Obfuscated Valid Data | The handling of non-trivial data via specific parsing rules in `fcn.1800d9920` and `fcn.1800bdac0` suggests a method to hide information from simple analysis tools. |

### Analyst Notes:
*   **Contextual Interpretation:** While the code currently maps to **T1027 (Obfuscated Valid Data)**, it is important to note that in a "clean" application (like a game engine), these techniques are used for software complexity and modularity. In a malicious context, they are used to hinder static and dynamic analysis by complicating the execution flow for automated tools.
*   **Potential for Packing:** The mention of the binary potentially acting as a "packer" or "stub" is an indicator that if this code were found in a suspicious file, it would be classified as part of a **Defense Evasion** tactic, specifically to wrap malicious payloads within layers of complex logic.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the IOC report:

### **IOC Analysis Summary**
After a thorough review of both the raw string data and the behavioral analysis provided, **no genuine Indicators of Compromise (IOCs) were identified.**

The "Extracted Strings" section contains primarily obfuscated data, repetitive junk characters (e.g., `UAWAVAUATWVSH`), and memory-related constants that do not resolve to actionable intelligence. The "Behavioral Analysis" confirms the absence of network indicators, persistence mechanisms, or malicious system manipulations.

---

### **Categorized IOCs**

*   **IP addresses / URLs / Domains:** 
    *   None identified.
*   **File paths / Registry keys:** 
    *   None identified. (Note: `.rdata` and `.data` are standard PE section headers, not file paths).
*   **Mutex names / Named pipes:** 
    *   None identified.
*   **Hashes:** 
    *   None identified.
*   **Other artifacts (user agents, C2 patterns, etc.):** 
    *   None identified.

---
**Analyst Note:** The analysis suggests the sample is likely a component of a legitimate but complex software framework (such as a game engine). While the code exhibits high complexity and "table-driven" logic—techniques sometimes used by malware to evade analysis—there are no active indicators linking this specific sample to a known threat actor or malicious campaign.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family**: None (Benign)
2. **Malware type**: N/A
3. **Confidence**: High
4. **Key evidence**:
    *   **Absence of Malicious Indicators:** The behavioral analysis confirms a total lack of standard malicious indicators, including no network communication (no IPs/domains), no persistence mechanisms (no registry/service changes), and no process manipulation (no injection or evasion attempts).
    *   **Complex but Legitimate Logic:** The code exhibits characteristics typical of high-level software frameworks—such as game engines or system libraries—including complex state management, advanced memory handling, and high-precision time calculations, rather than the concise, functional logic typically seen in malware.
    *   **Zero Actionable IOCs:** No indicators of compromise (IOCs) were found during string analysis; the only "obfuscation" noted is consistent with standard software complexity and modular programming rather than intentional evasion for a threat actor.
