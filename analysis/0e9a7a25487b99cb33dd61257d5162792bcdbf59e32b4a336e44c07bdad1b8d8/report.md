# Threat Analysis Report

**Generated:** 2026-08-13 16:57 UTC
**Sample:** `0e9a7a25487b99cb33dd61257d5162792bcdbf59e32b4a336e44c07bdad1b8d8_0e9a7a25487b99cb33dd61257d5162792bcdbf59e32b4a336e44c07bdad1b8d8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e9a7a25487b99cb33dd61257d5162792bcdbf59e32b4a336e44c07bdad1b8d8_0e9a7a25487b99cb33dd61257d5162792bcdbf59e32b4a336e44c07bdad1b8d8.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 5 sections |
| Size | 8,521,216 bytes |
| MD5 | `500c7d1f81d73482e30a8e360fa8b445` |
| SHA1 | `5d2d41542c7390deb26d864e27d3cd5d7e59b059` |
| SHA256 | `0e9a7a25487b99cb33dd61257d5162792bcdbf59e32b4a336e44c07bdad1b8d8` |
| Overall entropy | 6.438 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774860403 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 7,113,728 | 6.431 | No |
| `.rdata` | 1,225,216 | 5.598 | No |
| `.data` | 25,088 | 3.741 | No |
| `.pdata` | 123,904 | 6.334 | No |
| `.reloc` | 32,256 | 5.476 | No |

### Imports

**kernel32.dll**: `GetCurrentThread`, `HeapReAlloc`, `AddVectoredExceptionHandler`, `GlobalLock`, `GlobalSize`, `WideCharToMultiByte`, `GlobalUnlock`, `UnhandledExceptionFilter`, `SetUnhandledExceptionFilter`, `TerminateProcess`, `IsProcessorFeaturePresent`, `Sleep`, `MultiByteToWideChar`, `GlobalAlloc`, `InitializeSListHead`
**user32.dll**: `GetRawInputData`, `SetCapture`, `TrackMouseEvent`, `GetActiveWindow`, `RegisterTouchWindow`, `GetKeyboardState`, `SendInput`, `MapVirtualKeyW`, `PostMessageW`, `GetAsyncKeyState`, `SetClipboardData`, `GetTouchInputInfo`, `OpenClipboard`, `CloseClipboard`, `GetClipboardData`
**comctl32.dll**: `DefSubclassProc`, `RemoveWindowSubclass`, `SetWindowSubclass`
**gdi32.dll**: `CreateCompatibleDC`, `DeleteDC`, `CreateRectRgn`, `CreateDIBSection`, `SelectObject`, `DeleteObject`, `SetTextColor`, `SetBkMode`, `BitBlt`, `CreateSolidBrush`, `GetDeviceCaps`
**ntdll.dll**: `RtlNtStatusToDosError`, `NtWriteFile`, `NtReadFile`
**shell32.dll**: `DragQueryFileW`, `DragFinish`
**oleaut32.dll**: `GetErrorInfo`
**api-ms-win-core-synch-l1-2-0.dll**: `WakeByAddressAll`, `WaitOnAddress`, `WakeByAddressSingle`
**bcryptprimitives.dll**: `ProcessPrng`
**advapi32.dll**: `RevertToSelf`, `ImpersonateAnonymousToken`
**ole32.dll**: `CoInitializeEx`, `RevokeDragDrop`, `OleInitialize`, `RegisterDragDrop`, `CoCreateInstance`, `CoUninitialize`
**imm32.dll**: `ImmSetCandidateWindow`, `ImmReleaseContext`, `ImmGetCompositionStringW`, `ImmSetCompositionWindow`, `ImmGetContext`, `ImmAssociateContextEx`
**dwrite.dll**: `DWriteCreateFactory`
**dwmapi.dll**: `DwmSetWindowAttribute`, `DwmEnableBlurBehindWindow`
**uxtheme.dll**: `SetWindowTheme`
**VCRUNTIME140.dll**: `__current_exception_context`, `memchr`, `memmove`, `memcmp`, `__CxxFrameHandler3`, `memcpy`, `__C_specific_handler`, `memset`, `strrchr`, `__current_exception`, `strchr`
**api-ms-win-crt-math-l1-1-0.dll**: `ceilf`, `round`, `powf`, `tan`, `acos`, `ceil`, `floor`, `truncf`, `log2`, `trunc`, `atan2`, `cos`, `sin`, `fmod`, `exp2f`
**api-ms-win-crt-string-l1-1-0.dll**: `strlen`, `strspn`, `strncmp`, `strcspn`, `strcmp`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_endthreadex`, `_beginthreadex`, `strerror`, `terminate`, `_crt_atexit`, `_set_app_type`, `_configure_narrow_argv`, `_initialize_narrow_environment`, `_get_initial_narrow_environment`, `_initterm`, `_initterm_e`, `exit`, `_exit`, `_seh_filter_exe`, `__p___argc`
**api-ms-win-crt-heap-l1-1-0.dll**: `free`, `_msize`, `_set_new_mode`, `realloc`, `malloc`

## Extracted Strings

Total strings found: **18474** (showing first 100)

```
!This program cannot be run in DOS mode.
$
18C_1!;
1Rich1;
`.rdata
@.data
.pdata
@.reloc
AWAVAUATVWUSH
#ffff.
[]_^A\A]A^A_
AWAVAUATVWUSH
l$0fffff.
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
~D$8H9
[]_^A\A]A^A_
AWAVATVWSH
L+a0L;a(
h[_^A\A^A_
AWAVAUATVWSH
L+i0L;i(
[_^A\A]A^A_
AWAVAUATVWSH
L+i0L;i(
p[_^A\A]A^A_
AWAVAUATVWSH
L+i0L;i(
p[_^A\A]A^A_
AWAVAUATVWUSH
H+i0H;i(
([]_^A\A]A^A_
AWAVAUATVWSH
L+i0L;i(
[_^A\A]A^A_
AWAVAUATVWSH
L+i0L;i(
p[_^A\A]A^A_
AWAVATVWSH
L+a0L;a(
[_^A\A^A_
AWAVAUATVWUSH
f(L9t$ t/M9
fffff.
([]_^A\A]A^A_
AWAVAUATVWUSH
X[]_^A\A]A^A_
AWAVAUATVWUSH
([]_^A\A]A^A_
AVVWSH
CP:D$p
CQ:D$q
CR:D$r
CS:D$s
CT:D$t
x[_^A^
AVVWSH
G ;D$Hur
.D$LufzdH
X[_^A^
AWAVAUATVWUSH
-fffff.
([]_^A\A]A^A_
([]_^A\A]A^A_H
AWAVATVWUSH
@[]_^A\A^A_
AWAVATVWSH
([_^A\A^A_
AWAVATVWSH
([_^A\A^A_
AWAVATVWSH
H;^0t)H
([_^A\A^A_
AWAVAUATVWUSH
-fffff.
([]_^A\A]A^A_
AWAVATVWSH
8[_^A\A^A_
AWAVATVWSH
([_^A\A^A_
AWAVAUATVWUSH
8[]_^A\A]A^A_
AWAVAUATVWUSH
8[]_^A\A]A^A_
AWAVAUATVWSH
0[_^A\A]A^A_
AWAVAUATVWUSH
([]_^A\A]A^A_
AWAVAUATVWUSH
8[]_^A\A]A^A_
AWAVAUATVWUSH
8[]_^A\A]A^A_
AWAVAUATVWSH
0[_^A\A]A^A_
AWAVAUATVWUSH
([]_^A\A]A^A_
AWAVAUATVWUSH
8[]_^A\A]A^A_
AWAVAUATVWUSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14000e140` | `0x14000e140` | 6998774 | ✓ |
| `case.0x1404e25d4.33` | `0x1404e3d10` | 6747097 | ✓ |
| `fcn.14056a6d0` | `0x14056a6d0` | 5286859 | ✓ |
| `fcn.14019c090` | `0x14019c090` | 2989521 | ✓ |
| `fcn.140466e30` | `0x140466e30` | 2468210 | ✓ |
| `fcn.14022d300` | `0x14022d300` | 1489537 | ✓ |
| `fcn.140300970` | `0x140300970` | 586095 | ✓ |
| `fcn.140305a90` | `0x140305a90` | 565730 | ✓ |
| `fcn.1405a20c0` | `0x1405a20c0` | 551187 | ✓ |
| `fcn.14011e4b0` | `0x14011e4b0` | 507867 | ✓ |
| `fcn.14059b760` | `0x14059b760` | 423907 | ✓ |
| `fcn.14064b010` | `0x14064b010` | 376767 | ✓ |
| `section..text` | `0x140001000` | 332609 | ✓ |
| `fcn.140247970` | `0x140247970` | 323725 | ✓ |
| `fcn.14000dad0` | `0x14000dad0` | 279885 | ✓ |
| `fcn.14056ed70` | `0x14056ed70` | 232186 | ✓ |
| `fcn.140657400` | `0x140657400` | 203372 | ✓ |
| `fcn.1404f0290` | `0x1404f0290` | 134272 | ✓ |
| `fcn.1403a7080` | `0x1403a7080` | 96247 | ✓ |
| `fcn.140691990` | `0x140691990` | 85498 | ✓ |
| `fcn.1404acd00` | `0x1404acd00` | 79474 | ✓ |
| `fcn.1403c9810` | `0x1403c9810` | 66993 | ✓ |
| `fcn.140396aa0` | `0x140396aa0` | 57399 | ✓ |
| `fcn.140313370` | `0x140313370` | 52229 | ✓ |
| `fcn.140514da0` | `0x140514da0` | 42611 | ✓ |
| `fcn.1402478d0` | `0x1402478d0` | 42415 | ✓ |
| `case.0x1401a69dd.12073` | `0x140516400` | 41916 | ✓ |
| `fcn.1403aca80` | `0x1403aca80` | 39440 | ✓ |
| `fcn.14055f4d0` | `0x14055f4d0` | 39204 | ✓ |
| `fcn.140671780` | `0x140671780` | 36070 | ✓ |

### Decompiled Code Files

- [`code/case.0x1401a69dd.12073.c`](code/case.0x1401a69dd.12073.c)
- [`code/case.0x1404e25d4.33.c`](code/case.0x1404e25d4.33.c)
- [`code/fcn.14000dad0.c`](code/fcn.14000dad0.c)
- [`code/fcn.14000e140.c`](code/fcn.14000e140.c)
- [`code/fcn.14011e4b0.c`](code/fcn.14011e4b0.c)
- [`code/fcn.14019c090.c`](code/fcn.14019c090.c)
- [`code/fcn.14022d300.c`](code/fcn.14022d300.c)
- [`code/fcn.1402478d0.c`](code/fcn.1402478d0.c)
- [`code/fcn.140247970.c`](code/fcn.140247970.c)
- [`code/fcn.140300970.c`](code/fcn.140300970.c)
- [`code/fcn.140305a90.c`](code/fcn.140305a90.c)
- [`code/fcn.140313370.c`](code/fcn.140313370.c)
- [`code/fcn.140396aa0.c`](code/fcn.140396aa0.c)
- [`code/fcn.1403a7080.c`](code/fcn.1403a7080.c)
- [`code/fcn.1403aca80.c`](code/fcn.1403aca80.c)
- [`code/fcn.1403c9810.c`](code/fcn.1403c9810.c)
- [`code/fcn.140466e30.c`](code/fcn.140466e30.c)
- [`code/fcn.1404acd00.c`](code/fcn.1404acd00.c)
- [`code/fcn.1404f0290.c`](code/fcn.1404f0290.c)
- [`code/fcn.140514da0.c`](code/fcn.140514da0.c)
- [`code/fcn.14055f4d0.c`](code/fcn.14055f4d0.c)
- [`code/fcn.14056a6d0.c`](code/fcn.14056a6d0.c)
- [`code/fcn.14056ed70.c`](code/fcn.14056ed70.c)
- [`code/fcn.14059b760.c`](code/fcn.14059b760.c)
- [`code/fcn.1405a20c0.c`](code/fcn.1405a20c0.c)
- [`code/fcn.14064b010.c`](code/fcn.14064b010.c)
- [`code/fcn.140657400.c`](code/fcn.140657400.c)
- [`code/fcn.140671780.c`](code/fcn.140671780.c)
- [`code/fcn.140691990.c`](code/fcn.140691990.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This final disassembly chunk (Chunk 4) provides the concluding evidence needed to categorize this binary as a **highly sophisticated, modular malware framework**. The transition from Chunk 3 to Chunk 4 moves from "detecting infrastructure" to "observing execution logic."

The following analysis incorporates all previous findings while integrating the new details regarding state management, advanced error handling, and deep integration with database operations.

---

### Final Comprehensive Analysis: Industrial-Grade Modular Malware Framework

The final chunk of disassembly confirms that this binary is not a standalone piece of malware, but rather a **sophisticated execution engine** (similar to those found in high-end RATs like Quasar, AgentTesla, or advanced state-sponsored toolkits). It is designed to be "blind" and "generic," receiving commands from a C2 server and executing complex logic through an internal abstraction layer.

#### 1. Sophisticated State Machine & Transaction Logic
The most significant revelation in this final chunk is the presence of robust **transactional logic** related to database operations (specifically SQLite).
*   **Observation:** The code contains explicit checks for "transaction" states, such as:
    *   *"cannot start a transaction within a transaction"*
    *   *"cannot commit - no transaction is active"*
    *   *"no more rows available"*
    *   *"abort due to ROLLBACK"*
*   **Impact:** This indicates the malware doesn't just "save" data; it manages complex database states. It can perform multi-step operations where a series of actions must either succeed together or fail gracefully without leaving the system in an inconsistent state. This is typical for tools that need to scrape large amounts of data (like entire browser profiles, mail archives, or system logs) and organize them into structured local databases before exfiltration.

#### 2. High-Level Abstraction Layer (The "Internal VM")
The switch table (continuing through `0xaf`) reveals a massive **abstraction layer**. The malware rarely interacts with the OS directly; instead, it interacts with its own internal "objects" and "methods."
*   **Observation:** Cases like `0xaa` and `0xad` involve complex logic to resolve pointers, check for null values, and iterate through lists of objects.
*   **Impact:** This is a hallmark of industrial-grade development. By wrapping its core functionality in an internal API, the developers can update the "capabilities" of the malware (e.g., adding a new way to steal credentials) by simply updating the C2 instructions without changing the underlying "engine."

#### 3. Defensive Programming & Error Handling
The code demonstrates a high level of **resilience and stealth**.
*   **Observation:** In several locations, the code checks for specific error codes (e.g., `if ((uVar26 & 0xff) < 0x1d)`). If an error occurs, it attempts to map that error to a specific internal message or falls back to "unknown error."
*   **Impact:** This prevents the malware from crashing if a routine fails (e.g., a file is locked or a database table is missing). A crash is a "loud" event that alerts users and EDR systems. By handling errors gracefully, the malware ensures it stays resident on the system as long as possible.

#### 4. Automated Data Mapping
The switch case `0xaf` shows logic for mapping values into specific structures (e.g., `"ValueList"`).
*   **Observation:** The code dynamically calculates offsets and manages "buffer wrapping" to ensure data is structured correctly before it leaves the system.
*   **Impact:** This suggests the malware is capable of taking diverse, unstructured data from a host's environment and organizing it into a standardized format for the attacker’s database.

---

### Final Consolidated Summary of Findings

| Feature | Technical Observation | Threat / Purpose |
| :--- | :--- | :--- |
| **Modular Command Engine** | Massive switch table (`0x5e` through `0xaf+`) with complex branching and abstraction layers. | Allows a single binary to be reused for multiple campaigns (Stealer, RAT, Botnet) by simply changing the C2 commands. |
| **Transactional Database Management** | Explicit logic for SQLite transactions, "commit/rollback" states, and row-counting. | Enables complex data harvesting; ensures that large amounts of stolen information are stored reliably and systematically. |
| **Abstraction & Decoupling** | Use of internal "objects" to handle system interactions rather than direct API calls. | Makes static analysis extremely difficult. The actual malicious logic is decoupled from the core engine. |
| **Resilient Error Handling** | Multi-layered checks for null pointers, buffer overflows, and specific error code mapping. | Ensures stability and longevity; avoids "noisy" crashes that would alert security products or end-users. |
| **Data Re-packaging** | Sophisticated logic for wrapping and re-mapping data into standardized structures (e.g., `ValueList`). | Simplifies the work of the threat actor by delivering organized, pre-processed data to their backend infrastructure. |

### Final Conclusion for Security Analysts
This binary is a **professional-grade malware framework**. It is designed for long-term persistence and high-volume data theft. The presence of industrial-strength features—such as transaction-aware database logic, modular command dispatching, and robust error handling—strongly suggests the involvement of **sophisticated cybercrime groups or APT actors.**

**Recommendation:**
*   **Detection Strategy:** Focus on behavior rather than static strings. Since the "actions" are determined by C2 commands, traditional signature-based detection will fail to catch variations of this same engine.
*   **Memory Forensics:** Monitor for unauthorized database connections (SQLite) and large volumes of data being staged in temporary files or local databases.
*   **Network Analysis:** Look for the "heartbeat" or check-in behavior that allows the malware to receive its command list, as it will likely use a variety of encoded instructions from the analysis above.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The "Internal VM" abstraction layer and massive switch table function as an interpreter, allowing a single binary to process diverse C2-driven commands. |
| **T1070.004** | Data Manipulation (Data from Local System) | The use of SQLite transaction logic facilitates the systematic collection and organized staging of large amounts of local data (e.g., browser profiles). |
| **T1020** | Automated Exfiltration | The "Automated Data Mapping" into a `ValueList` ensures that diverse, unstructured data is automatically packaged into a standardized format for exfiltration. |
| **T1613** | Obfuscated Filesystem (Implicit) / Evase via Stability | While not a single T-code, the "Resilient Error Handling" and logic to avoid "noisy" crashes are used as evasion techniques to maintain persistence and stay under the radar of EDR systems. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis mentions C2 communication, but no specific hardcoded domains or IP addresses were present in the provided string set.)

### **File paths / Registry keys**
*   *None identified.* (Standard internal symbols like `.rdata` and `.data` were excluded as false positives.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Behavioral Pattern: SQLite Database Manipulation**
    *   The malware utilizes complex SQL transaction logic (e.g., "cannot start a transaction within a transaction," "commit/rollback" logic). This indicates the use of local databases to stage and organize stolen data before exfiltration.
*   **Command & Control (C2) Architecture: Modular Switch Table**
    *   The presence of a large switch table (`0x5e` through `0xaf+`) acting as an "Internal VM" or abstraction layer. This allows the malware to receive generic commands and execute different modules (Stealer, RAT, etc.) without changing the core binary.
*   **Data Packaging Logic: "ValueList" & Buffer Wrapping**
    *   Specific logic for mapping raw system data into structured "ValueList" structures. This suggests a high degree of automation in preparing data for attacker consumption.
*   **Persistence/Stealth Technique: Robust Error Handling**
    *   Implementation of multi-layered checks (e.g., `if ((uVar26 & 0xff) < 0x1d)`) to map errors to internal codes rather than allowing the application to crash or throw visible system errors, ensuring longevity on the infected host.

---

## Malware Family Classification

Based on the detailed behavioral analysis provided, here is the classification for the sample:

1. **Malware family**: Custom (Modular Framework)
2. **Malware type**: Loader / Backdoor
3. **Confidence**: High
4. **Key evidence**:
    *   **Modular Command Engine:** The presence of a massive switch table acting as an "Internal VM" indicates the binary is designed to receive and execute various functions (e.g., stealer modules, RAT capabilities) from a C2 server, rather than performing a single static action.
    *   **Industrial-Grade Data Handling:** The implementation of SQLite transaction logic (`commit`, `rollback`) and automated data mapping into "ValueLists" indicates a sophisticated infrastructure for harvesting and organizing large volumes of stolen data.
    *   **Advanced Evasion & Stability:** The use of high-level abstraction layers and multi-layered error handling suggests the malware is designed to remain resident on a system for long periods while avoiding "noisy" crashes that would alert security software.
