# Threat Analysis Report

**Generated:** 2026-08-22 07:12 UTC
**Sample:** `110c51102f4bf6e94c609d8dbb83dbbf835788e79578badd498ec9e0a62940d9_110c51102f4bf6e94c609d8dbb83dbbf835788e79578badd498ec9e0a62940d9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `110c51102f4bf6e94c609d8dbb83dbbf835788e79578badd498ec9e0a62940d9_110c51102f4bf6e94c609d8dbb83dbbf835788e79578badd498ec9e0a62940d9.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 7 sections |
| Size | 7,794,688 bytes |
| MD5 | `69f416e8f050d82e103f8d27e9e81e3b` |
| SHA1 | `90b4c603a28b8989dc2aa823f30e55766760c43a` |
| SHA256 | `110c51102f4bf6e94c609d8dbb83dbbf835788e79578badd498ec9e0a62940d9` |
| Overall entropy | 6.044 |
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
| `.text` | 1,939,456 | 6.567 | No |
| `.rdata` | 5,736,448 | 5.18 | No |
| `.data` | 7,168 | 3.274 | No |
| `.pdata` | 107,520 | 6.219 | No |
| `_RDATA` | 512 | 2.424 | No |
| `.rsrc` | 512 | 2.875 | No |
| `.reloc` | 2,048 | 4.766 | No |

### Imports

**ADVAPI32.dll**: `DeregisterEventSource`, `RegCloseKey`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryValueExW`, `RegSetValueExW`, `RegisterEventSourceW`, `ReportEventW`, `OpenProcessToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`
**bcrypt.dll**: `BCryptGetProperty`, `BCryptGenRandom`, `BCryptFinishHash`, `BCryptCloseAlgorithmProvider`, `BCryptHashData`, `BCryptCreateHash`, `BCryptDestroyHash`, `BCryptOpenAlgorithmProvider`
**KERNEL32.dll**: `TlsFree`, `TlsSetValue`, `TlsGetValue`, `TlsAlloc`, `InitializeCriticalSectionAndSpinCount`, `EncodePointer`, `RaiseException`, `RtlPcToFileHeader`, `InterlockedFlushSList`, `CancelThreadpoolIo`, `CloseHandle`, `CloseThreadpoolIo`, `CloseThreadpoolWork`, `CopyFileW`, `CreateDirectoryW`
**ole32.dll**: `CoUninitialize`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CoGetApartmentType`, `CoCreateGuid`, `CoWaitForMultipleHandles`, `CoInitializeEx`
**USER32.dll**: `LoadStringW`
**api-ms-win-crt-heap-l1-1-0.dll**: `_callnewh`, `malloc`, `free`, `calloc`
**api-ms-win-crt-math-l1-1-0.dll**: `ceil`, `log`, `modf`
**api-ms-win-crt-string-l1-1-0.dll**: `strcpy_s`, `_stricmp`, `strcmp`, `wcsncmp`, `strlen`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_seh_filter_dll`, `_initterm_e`, `terminate`, `_cexit`, `abort`, `_crt_atexit`, `_execute_onexit_table`, `_register_onexit_function`, `_initialize_onexit_table`, `_initialize_narrow_environment`, `_configure_narrow_argv`, `_initterm`

### Exports

`03qxfsyO6mM11VI8NVrzBye`, `0eR2Z9gwHCsK0pyB9mj1me`, `0kdT42iAaVYgRFriNGBI23V1MKq8fyVy`, `128raBey`, `14oPkBnh`, `18HLUDVoE`, `1wB6f89i3jHnBCy3JbdTqky`, `1xQvEm5k4LNm4qux4k`, `2QbfGTAEFCFgXOIepkNdsU`, `2pUCWojN3k774ff1Twj3`, `3M8fM18CyWFgEQeZqJxWzl3tCq2tvY`, `5G3rb5KRseXh0HRnPxrPdUfbj64`, `5JWeBT5iOzEcmU3zba3582hH`, `5LYfxnGHVjwOml`, `5NTWmcpquv69roXyQQhsWGC3y0C8riI`, `6FV5aB7sHkeLyHiEssk9WXP`, `6eoEJOgZFyAki16Dx`, `6tuKXBYCyf7vRZ`, `7qWT67qHXc9CCkh950FElS2`, `88ziRa28DDTT4lYfRozq4`, `8Nfadwj9e0vSqiiYYE`, `8VRssUL4OL`, `8WFo2U6xqyccDu`, `9RBlSrzsENvD4YQnVR38peJJ`, `9jre5T0Ap`, `9kFTwzGLOJmMKxYEOnjRKI8T7SY`, `ABDE6Y6DXGDu4JYlQ`, `AF2DQdx19d8fiu2ShTVreRQqeZTYiHnP`, `AUVFkEpHiMmf6VzRiJ`, `BEAufHyGhaqu1VKa`, `BMbW2KE633MrYqGL2zqc1rrBuEIS`, `BoWUO3zz4SQ4d`, `C838tdop6vzNjrQQhkaRk0hL2`, `Cxz7ojucYJdD`, `DS0oPn9WK9qywfimo2mAif`, `DUhzQM2e`, `DfhhRnK`, `ELMqQXe`, `EQdiMoQPSqyj1`, `FNs9HDwRXvhm`, `G633U0I2kAux2cCF9wa7FrEjbH0s`, `GeEZNAnRj4aWrp9Wmj`, `Hbn7u27y7THvDF2IaebZzLPFmd`, `HdHlleauJbVDETZ5q5h23S9h2nsYqRzq`, `IewUfWYxX7vyZl3tsh9J5Vqk0zw`, `IvRIagn5bnEhPkqF64Tl4wRP`, `J4CctXmWAYcjXFyDV`, `JER08Ik`, `JqpWttvxEjl7c3PFC8Eb5w2yLIAFPu`, `JupV3sb0AN8Jxnn7siK`

## Extracted Strings

Total strings found: **12676** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@_RDATA
@.rsrc
@.reloc
UAWAVAUATWVSH
X[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
AWAVWVUSH
([]^_A^A_
L$8;L$H
L$8;L$H
L$8;L$H
L$8;L$HwnH
S(HcR 
AWAVAUATWVUSH
h[]^_A\A]A^A_
L$H;L$X
L$H;L$XwnH
LcA$L;
AWAVWVUSH
X[]^_A^A_
L$@;L$P
L$@;L$P
L$@;L$P
L$@;L$PwnH
AWAVAUWVUSH
C(Hc@ H
0[]^_A]A^A_
AWAVAUATWVUSH
8[]^_A\A]A^A_
8[]^_A\A]A^A_
AWAVWVUSH
([]^_A^A_H
([]^_A^A_
AWAVAUWVUSH
@[]^_A]A^A_
@[]^_A]A^A_
AWAVAUATWVUSH
H[]^_A\A]A^A_
H[]^_A\A]A^A_
AWAVWVUSH
([]^_A^A_H
([]^_A^A_
AWAVWVUSH
([]^_A^A_H
([]^_A^A_
AWAVAUWVUSH
@[]^_A]A^A_
@[]^_A]A^A_
AWAVAUWVUSH
 []^_A]A^A_H
 []^_A]A^A_
AWAVWVUSH
([]^_A^A_H
([]^_A^A_
AWAVWVUSH
I(Hcq 
H[]^_A^A_
AWAVWVUSH
H+CxHi
H[]^_A^A_
H[]^_A^A_
I(HcI H
I(HcI H
L$0;L$@
L$0;L$@wnH
AWAVAUATWVUSH
@(HcH I
8[]^_A\A]A^A_
AWAVAUATWVUSH
@(Lc@ I
([]^_A\A]A^A_
L$@;L$P
L$@;L$P
L$@;L$P
L$@;L$P
L$@;L$P
L$@;L$P
L$@;L$P
L$@;L$P
L$@;L$P
L$@;L$Pw_H
L$@;L$P
L$@;L$P
L$@;L$PwzH
AWAVAUWVUSH
0[]^_A]A^A_
@(Lc@ I
0[]^_A]A^A_
0[]^_A]A^A_
L$P;L$`
L$P;L$`
L$P;L$`wnH
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUWVSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.18000c5c0` | `0x18000c5c0` | 1865539 | ✓ |
| `fcn.18000c5d0` | `0x18000c5d0` | 1865535 | ✓ |
| `fcn.18000c490` | `0x18000c490` | 1473268 | ✓ |
| `fcn.180173174` | `0x180173174` | 1439415 | ✓ |
| `fcn.18017306c` | `0x18017306c` | 1439320 | ✓ |
| `fcn.180041150` | `0x180041150` | 1263256 | ✓ |
| `fcn.180049a70` | `0x180049a70` | 1220597 | ✓ |
| `fcn.180052450` | `0x180052450` | 1184581 | ✓ |
| `fcn.180175840` | `0x180175840` | 1126185 | ✓ |
| `fcn.180037900` | `0x180037900` | 1082690 | ✓ |
| `fcn.180173a5a` | `0x180173a5a` | 1025982 | ✓ |
| `fcn.1801737a8` | `0x1801737a8` | 1013757 | ✓ |
| `fcn.18000d3e0` | `0x18000d3e0` | 411000 | ✓ |
| `fcn.180180240` | `0x180180240` | 342053 | ✓ |
| `fcn.1801837f0` | `0x1801837f0` | 328919 | ✓ |
| `fcn.180046f00` | `0x180046f00` | 258971 | ✓ |
| `fcn.1801b8670` | `0x1801b8670` | 232165 | ✓ |
| `fcn.18015d7b0` | `0x18015d7b0` | 223795 | ✓ |
| `fcn.1801b86a0` | `0x1801b86a0` | 223013 | ✓ |
| `fcn.1801b86b0` | `0x1801b86b0` | 221574 | ✓ |
| `fcn.1801b84b0` | `0x1801b84b0` | 220593 | ✓ |
| `fcn.1801b8680` | `0x1801b8680` | 220106 | ✓ |
| `fcn.180087900` | `0x180087900` | 219214 | ✓ |
| `fcn.1800877b0` | `0x1800877b0` | 218805 | ✓ |
| `fcn.1801b8720` | `0x1801b8720` | 218133 | ✓ |
| `fcn.18003c230` | `0x18003c230` | 130969 | ✓ |
| `fcn.18002c820` | `0x18002c820` | 115957 | ✓ |
| `fcn.1800663e0` | `0x1800663e0` | 110646 | ✓ |
| `fcn.180013290` | `0x180013290` | 103485 | ✓ |
| `fcn.180077dd0` | `0x180077dd0` | 98071 | ✓ |

### Decompiled Code Files

- [`code/fcn.18000c490.c`](code/fcn.18000c490.c)
- [`code/fcn.18000c5c0.c`](code/fcn.18000c5c0.c)
- [`code/fcn.18000c5d0.c`](code/fcn.18000c5d0.c)
- [`code/fcn.18000d3e0.c`](code/fcn.18000d3e0.c)
- [`code/fcn.180013290.c`](code/fcn.180013290.c)
- [`code/fcn.18002c820.c`](code/fcn.18002c820.c)
- [`code/fcn.180037900.c`](code/fcn.180037900.c)
- [`code/fcn.18003c230.c`](code/fcn.18003c230.c)
- [`code/fcn.180041150.c`](code/fcn.180041150.c)
- [`code/fcn.180046f00.c`](code/fcn.180046f00.c)
- [`code/fcn.180049a70.c`](code/fcn.180049a70.c)
- [`code/fcn.180052450.c`](code/fcn.180052450.c)
- [`code/fcn.1800663e0.c`](code/fcn.1800663e0.c)
- [`code/fcn.180077dd0.c`](code/fcn.180077dd0.c)
- [`code/fcn.1800877b0.c`](code/fcn.1800877b0.c)
- [`code/fcn.180087900.c`](code/fcn.180087900.c)
- [`code/fcn.18015d7b0.c`](code/fcn.18015d7b0.c)
- [`code/fcn.18017306c.c`](code/fcn.18017306c.c)
- [`code/fcn.180173174.c`](code/fcn.180173174.c)
- [`code/fcn.1801737a8.c`](code/fcn.1801737a8.c)
- [`code/fcn.180173a5a.c`](code/fcn.180173a5a.c)
- [`code/fcn.180175840.c`](code/fcn.180175840.c)
- [`code/fcn.180180240.c`](code/fcn.180180240.c)
- [`code/fcn.1801837f0.c`](code/fcn.1801837f0.c)
- [`code/fcn.1801b84b0.c`](code/fcn.1801b84b0.c)
- [`code/fcn.1801b8670.c`](code/fcn.1801b8670.c)
- [`code/fcn.1801b8680.c`](code/fcn.1801b8680.c)
- [`code/fcn.1801b86a0.c`](code/fcn.1801b86a0.c)
- [`code/fcn.1801b86b0.c`](code/fcn.1801b86b0.c)
- [`code/fcn.1801b8720.c`](code/fcn.1801b8720.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The code appears to be part of a **highly structured execution engine or dispatcher**, possibly for an internal script interpreter or a modular "task" system common in complex malware. 
*   Instead of linear logic, the code uses a **dispatch pattern**: functions check specific IDs (e.g., `0x180799d80`, `0x180799cb0`) to decide which sub-routine or "handler" to execute.
*   This structure is typical in malware that handles various commands from a Command & Control (C2) server, where the core logic remains static while specific tasks are swapped out.

### Suspicious and Malicious Behaviors
*   **Multi-Threaded Execution (Thread Pool):** The code explicitly utilizes the Windows **Threadpool API** (`CreateThreadpoolWork`, `SubmitThreadpoolWork`) in function `fcn.180046f00`. 
    *   *Analysis:* This is a common technique used by modern malware to perform tasks—such as network communication, data exfiltration, or anti-analysis checks—asynchronously in the background. Using the system's thread pool helps hide these activities from some basic monitoring tools that only look for new thread creation via `CreateThread`.
*   **Heavy String Obfuscation:** The "Extracted Strings" section shows significant evidence of obfuscation/packing. The repetitive, high-entropy characters (e.g., `UAWAVAUATWVSH`) suggest the presence of a custom encoding or an XORed data block that is only decrypted in memory during execution.
*   **Complexity and Obfuscated Control Flow:** Functions like `fcn.1800663e0` contain extensive branching logic to handle different "states" or "opcodes." This suggests the binary acts as a "loader" or "orchestrator," meaning the primary malicious payload may be encrypted or modularized and called by this dispatcher.

### Notable Techniques and Patterns
*   **Dispatcher/Interpreter Pattern:** The repetitive nature of functions like `fcn.1801b8670` and `fcn.1801b8680` (which iterate through lists and call handlers based on internal logic) strongly suggests a bytecode-style execution or a plugin-based architecture. This is used to evade static detection of specific malicious behaviors by hiding the actual "actions" behind a generic execution loop.
*   **Synchronization Mechanisms:** The frequent use of `LOCK()` and `UNLOCK()` macro equivalents around shared memory locations (e.g., in `fcn.180046f00` and `fcn.180049a70`) indicates the code is designed to handle concurrent access to a global state, common when multiple threads are performing separate malicious tasks simultaneously.
*   **Anti-Analysis/Defense Evasion:** The use of "junk" or repeated code blocks (observed in several functions) can be used as a technique to confuse automated de-compilers and human analysts by creating complex but ultimately meaningless logic paths.

### Summary Table for Quick Reference
| Feature | Observation | Potential Threat Impact |
| :--- | :--- | :--- |
| **Execution Logic** | Complex Dispatcher / Interpreter | Hides core malicious intent behind a "generic" execution layer. |
| **Threading** | Windows Threadpool API usage | Enables background tasks (C2, exfiltration) while evading some basic detection. |
| **Obfuscation** | Encoded/Garbage strings and repeated code blocks | Evades signature-based detection and hampers manual analysis. |
| **Concurrency** | Explicit memory locking for shared state | Indicates a multi-component malware capable of concurrent operations. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of high-entropy strings, XORed data blocks, and junk code segments is intended to hinder manual analysis and evade signature-based detection. |
| T1059 | Command and Scripting Interpreter | The "Dispatcher/Interpreter" pattern indicates the binary acts as a central hub to process various commands or tasks, common in malware communicating with a C2 server. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the intelligence assessment. 

Because the provided text consists primarily of obfuscated code fragments (high-entropy noise) and a high-level behavior summary, there are no specific, actionable static IOCs (such as hardcoded IP addresses or file paths) present in this specific dataset.

### **Indicators of Compromise (IOCs)**

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Behavioral Patterns:**
    *   **Dispatcher/Interpreter Logic:** The binary utilizes a dispatch pattern (e.g., `fcn.1801b8670`) to hide intent, suggesting the use of an internal script or bytecode system for command execution.
    *   **Threadpool API Usage:** Use of `CreateThreadpoolWork` and `SubmitThreadpoolWork` suggests concurrent execution of tasks (C2 communication, exfiltration) intended to evade simple thread-creation monitoring.
    *   **High Entropy Strings:** The presence of repetitive strings like `UAWAVAUATWVSH` indicates heavily obfuscated or XORed data blocks used for evasion.

---
**Analyst Note:** The sample appears to be a loader or "orchestrator" component. Because the code is currently in an obfuscated state, traditional static indicators (IPs/Paths) are likely hidden within the encrypted payload and will only become visible after the dispatcher decodes the next stage of execution in memory.

---

## Malware Family Classification

1. **Malware family:** Custom
2. **Malware type:** Loader / Orchestrator
3. **Confidence:** Medium

4. **Key evidence:**
*   **Dispatcher/Interpreter Architecture:** The use of an internal execution engine and a "dispatch pattern" to handle commands indicates the binary is designed as a modular framework rather than a single-purpose malware, which is characteristic of sophisticated loaders or droppers.
*   **Evasion through Obfuscation:** The heavy string obfuscation (high entropy) and the deliberate use of the Windows Threadpool API suggest a primary goal of evading automated detection while performing background tasks like C2 communication.
*   **Modular Tasking:** The "orchestrator" nature—where specific actions are hidden behind an interpreter layer—indicates that this sample likely serves as the first stage of an infection, responsible for decrypting and executing subsequent malicious modules (e.g., credential theft or remote access).
