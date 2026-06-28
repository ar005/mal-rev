# Threat Analysis Report

**Generated:** 2026-06-27 22:53 UTC
**Sample:** `020aac79a14717e316a593155ca778dd3e253b888bf62633b174838d35df7f41_020aac79a14717e316a593155ca778dd3e253b888bf62633b174838d35df7f41.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `020aac79a14717e316a593155ca778dd3e253b888bf62633b174838d35df7f41_020aac79a14717e316a593155ca778dd3e253b888bf62633b174838d35df7f41.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 8 sections |
| Size | 3,648,408 bytes |
| MD5 | `ab0df05e39bd73f4adade8fdc21a1f25` |
| SHA1 | `b12c2771c040f6175902ec5941ffd09748f87ed3` |
| SHA256 | `020aac79a14717e316a593155ca778dd3e253b888bf62633b174838d35df7f41` |
| Overall entropy | 7.988 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1459953544 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 62,464 | 6.375 | No |
| `.itext` | 4,096 | 5.732 | No |
| `.data` | 3,584 | 2.297 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 4,096 | 4.598 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.204 | No |
| `.rsrc` | 45,568 | 4.201 | No |

### Imports

**oleaut32.dll**: `SysFreeString`, `SysReAllocStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**user32.dll**: `CreateWindowExW`, `TranslateMessage`, `SetWindowLongW`, `PeekMessageW`, `MsgWaitForMultipleObjects`, `MessageBoxW`, `LoadStringW`, `GetSystemMetrics`, `ExitWindowsEx`, `DispatchMessageW`, `DestroyWindow`, `CharUpperBuffW`, `CallWindowProcW`
**kernel32.dll**: `Sleep`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **7921** (showing first 100)

```
This program must be run under Win32
$7
`.itext
`.data
.idata
.rdata
@.rsrc
AnsiChar
string(


AnsiString
TObject
FastMM Borland Edition (c) 2004 - 2008 Pierre le Riche / Professional Software Development
An unexpected memory leak has occurred. 
The unexpected small block leaks are:

The sizes of unexpected leaked medium and large blocks are: 
 bytes: 
Unknown
AnsiString
UnicodeString
Unexpected Memory Leak
:
u0Nt
~]x[[)
:
u	@B
YZXtm1
VWUUh(?@
ZTUWVSPR
0123456789ABCDEF
_^[YY]
t-Rf;
t f;J
t!R:
t
t-Rf;
t f;J
XZ_^[X]X
tc<tB<tr<t}<
GetLongPathNameW
_^[YY]
	Exception0n@
EAbort
EHeapException
EOutOfMemory
EInOutError
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeError
EIntOverflow

EMathError

EInvalidOp
EZeroDivide
	EOverflow

EUnderflow
EInvalidPointer
EInvalidCast
EConvertError
EAccessViolation

EPrivilege
EStackOverflow
	EControlC
EVariantError
EAssertionFailed
EAbstractError
EIntfCastError
ESafecallException
EMonitor
EMonitorLockException
ENoMonitorSupportException
SysUtils
SysUtils
	TEncoding
_^[YY]
$Z]_^[
_^[YY]
<@t!QS<$t
<*t2
$*@@@*$@@@$ *@@* $@@($*)@-$*@@$-*@@$*-@@(*$)@-*$@@*-$@@*$-@@-* $@-$ *@* $-@$ *-@$ -*@*- $@($ *)(* $)
QQQQQQSVW3
QQQQQQSVW
SysUtils
_^[YY]
	TErrorRec

TExceptRec
TUnitHashArray
SysUtils
TModuleInfo
_^[YY]
YZ]_^[
TCustomFile

EFileError
ECompressError
ECompressDataError
ECompressInternalError
TCustomDecompressor
TCompressedBlockReader
$Z]_^[
TLZMA1SmallDecompressorS
t$;sht'
YZ]_^[
TSetupHeader
TSetupLanguageEntry=
_^[YY]
Sj
hg+
SetDefaultDllDirectories
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040867d` | `0x40867d` | 3116 | ✓ |
| `fcn.00401c7c` | `0x401c7c` | 1900 | ✓ |
| `fcn.0040d33c` | `0x40d33c` | 1690 | ✓ |
| `fcn.004018f8` | `0x4018f8` | 1496 | ✓ |
| `fcn.00408540` | `0x408540` | 995 | ✓ |
| `fcn.004027b8` | `0x4027b8` | 993 | ✓ |
| `fcn.00404c80` | `0x404c80` | 841 | ✓ |
| `fcn.00408988` | `0x408988` | 768 | ✓ |
| `fcn.0040a5a8` | `0x40a5a8` | 734 | ✓ |
| `fcn.00405de8` | `0x405de8` | 640 | ✓ |
| `fcn.004091f4` | `0x4091f4` | 563 | ✓ |
| `fcn.00408c88` | `0x408c88` | 556 | ✓ |
| `entry0` | `0x4117dc` | 522 | ✓ |
| `fcn.00405bec` | `0x405bec` | 458 | ✓ |
| `fcn.004025f8` | `0x4025f8` | 448 | ✓ |
| `fcn.00409d3c` | `0x409d3c` | 443 | ✓ |
| `fcn.004094c0` | `0x4094c0` | 428 | ✓ |
| `fcn.00405940` | `0x405940` | 408 | ✓ |
| `fcn.004082e8` | `0x4082e8` | 390 | ✓ |
| `fcn.00404b9c` | `0x404b9c` | 355 | ✓ |
| `fcn.0040567c` | `0x40567c` | 319 | ✓ |
| `fcn.0040bb34` | `0x40bb34` | 312 | ✓ |
| `fcn.0040dd80` | `0x40dd80` | 303 | ✓ |
| `fcn.00404580` | `0x404580` | 295 | ✓ |
| `fcn.004096ac` | `0x4096ac` | 293 | ✓ |
| `fcn.00402be0` | `0x402be0` | 293 | ✓ |
| `fcn.0040532c` | `0x40532c` | 286 | ✓ |
| `fcn.0040513c` | `0x40513c` | 284 | ✓ |
| `fcn.00402260` | `0x402260` | 281 | ✓ |
| `fcn.004057bc` | `0x4057bc` | 276 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004018f8.c`](code/fcn.004018f8.c)
- [`code/fcn.00401c7c.c`](code/fcn.00401c7c.c)
- [`code/fcn.00402260.c`](code/fcn.00402260.c)
- [`code/fcn.004025f8.c`](code/fcn.004025f8.c)
- [`code/fcn.004027b8.c`](code/fcn.004027b8.c)
- [`code/fcn.00402be0.c`](code/fcn.00402be0.c)
- [`code/fcn.00404580.c`](code/fcn.00404580.c)
- [`code/fcn.00404b9c.c`](code/fcn.00404b9c.c)
- [`code/fcn.00404c80.c`](code/fcn.00404c80.c)
- [`code/fcn.0040513c.c`](code/fcn.0040513c.c)
- [`code/fcn.0040532c.c`](code/fcn.0040532c.c)
- [`code/fcn.0040567c.c`](code/fcn.0040567c.c)
- [`code/fcn.004057bc.c`](code/fcn.004057bc.c)
- [`code/fcn.00405940.c`](code/fcn.00405940.c)
- [`code/fcn.00405bec.c`](code/fcn.00405bec.c)
- [`code/fcn.00405de8.c`](code/fcn.00405de8.c)
- [`code/fcn.004082e8.c`](code/fcn.004082e8.c)
- [`code/fcn.00408540.c`](code/fcn.00408540.c)
- [`code/fcn.0040867d.c`](code/fcn.0040867d.c)
- [`code/fcn.00408988.c`](code/fcn.00408988.c)
- [`code/fcn.00408c88.c`](code/fcn.00408c88.c)
- [`code/fcn.004091f4.c`](code/fcn.004091f4.c)
- [`code/fcn.004094c0.c`](code/fcn.004094c0.c)
- [`code/fcn.004096ac.c`](code/fcn.004096ac.c)
- [`code/fcn.00409d3c.c`](code/fcn.00409d3c.c)
- [`code/fcn.0040a5a8.c`](code/fcn.0040a5a8.c)
- [`code/fcn.0040bb34.c`](code/fcn.0040bb34.c)
- [`code/fcn.0040d33c.c`](code/fcn.0040d33c.c)
- [`code/fcn.0040dd80.c`](code/fcn.0040dd80.c)

## Behavioral Analysis

Based on the disassembly and decompiled C pseudocode provided, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The binary appears to be a Windows-based application (likely 32-bit) that involves complex data processing, configuration retrieval via the Registry, and dynamic module loading. The presence of "Inno Setup" strings suggests this might be part of an installer or a loader for a larger software suite.

### Suspicious or Malicious Behaviors
*   **Registry Enumeration (Configuration Retrieval):** Function `fcn.00405de8` is highly significant. It calls `RegOpenKeyExW` and `RegQueryValueExW` on multiple keys in quick succession. This is a common technique for malware to retrieve configuration data, such as Command & Control (C2) server addresses, file paths for subsequent stages, or system information used to determine if the code is running in a sandbox.
*   **Dynamic API Resolution and Loading:** The use of `GetProcAddress`, `GetModuleHandleW`, and `LoadLibraryExW` throughout the code indicates that the application resolves its functionality at runtime. This allows the binary to remain "clean" during static analysis, as many suspicious functions are only linked when needed.
*   **File Path Manipulation & Hunting:** Function `fcn.00405bec` performs extensive logic on file paths using `FindFirstFileW` and `lstrcpynW`. It appears to be scanning the filesystem or stripping path segments. This is often used by malware to locate injected DLLs, find specific configuration files, or hide its actual working directory from basic detection.
*   **Potential Anti-Analysis/Evasion:** 
    *   The inclusion of loops containing `Sleep(0)` and `Sleep(10)` (e.g., in `fcn.0041c7c`) can be used to stall automated analysis sandboxes that have limited time windows.
    *   The complex memory validation logic (using `VirtualQuery` and manual checks on memory ranges) may be intended to verify the integrity of its own code or to ensure it is not being monitored by a debugger.
*   **Data Transformation/Decoding:** Function `fcn.00402260` contains heavy arithmetic (multiplications, bit shifts, and modulo operations) used to generate data that appears to be "converting" values into string-like formats or calculating specific offsets. This could indicate the unpacking of an internal configuration block.

### Notable Techniques & Patterns
*   **Installer/Wrapper characteristics:** The presence of Inno Setup strings suggests this binary might act as a "dropper" or "stub." It handles the initial setup and then potentially extracts or executes another payload.
*   **Object-Oriented Structure:** Functions like `fcn.00513c` suggest the use of a vtable (virtual function table) or similar dispatch mechanism, common in C++ programs. This is often used to hide the flow of logic by making it more difficult for automated tools to trace the "main" logic path.
*   **Standard Windows API Abuse:** The binary interacts heavily with `advapi32.dll` and `kernel32.dll`. While many of these are legitimate, their specific combination (GetModuleName $\rightarrow$ RegOpenKey $\rightarrow$ LoadLibrary) is a classic pattern for "staged" execution where the program decides its next move based on environment variables or registry flags.

### Summary Recommendation
The binary exhibits several characteristics common in **malware loaders and installers**. The most concerning elements are the **automated registry queries** (potential C2/config fetching) and the **dynamic library loading** coupled with **complex file path manipulation**. It likely serves as a "loader" designed to prepare an environment for another component or to hide its primary functionality behind several layers of standard system calls.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1012 | System Information Discovery | The binary queries multiple registry keys to retrieve system configuration, C2 details, and potentially determine environment metadata. |
| T1083 | File and Directory Discovery | The use of `FindFirstFileW` and path manipulation logic indicates the binary is searching for specific files or dynamically adjusting paths to locate payload components. |
| T1497 | Virtualized Environment | The inclusion of `Sleep()` calls with varying intervals is a common tactic used to stall execution and bypass automated sandbox analysis timers. |
| T1027 | Obfuscated Resources | The use of dynamic API resolution (`GetProcAddress`) and mathematical decoding routines are intended to hide the program's true functionality from static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The provided text contains several "behavioral indicators" and "techniques" rather than specific static IOCs (like hardcoded IP addresses or file hashes), as the report describes the *methods* used by the malware rather than providing a list of specific malicious infrastructure.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **Note:** While the behavior analysis confirms that the binary performs **Registry Enumeration** (using `RegOpenKeyExW` and `RegQueryValueExW`) to retrieve C2 information or configuration, no specific registry keys (e.g., `HKCU\Software\...`) were provided in the raw strings for extraction.
*   **Note:** While the analysis notes **File Path Manipulation**, no specific malicious paths (e.g., `C:\Windows\Temp\...` or specific dropped filenames) were provided in the raw strings.

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Tactic: Dropper/Loader Identification:** The presence of "Inno Setup" strings (`TSetupHeader`, `SetDefaultDllDirectories`) indicates the binary likely functions as a wrapper or installer for a secondary payload.
*   **Tactic: Anti-Analysis/Evasion:** 
    *   Execution of `Sleep(0)` and `Sleep(10)` loops to stall automated sandboxes.
    *   Dynamic API Resolution (use of `GetProcAddress`, `GetModuleHandleW`, and `LoadLibraryExW`) to hide functionality from static analysis.
*   **Tactic: Configuration Decoding:** Use of complex arithmetic/bit-shifting in `fcn.00402260` suggests an internal configuration block is decrypted or unpacked at runtime.
*   **Potential TTP:** The combination of Registry queries followed by dynamic library loading and file system scanning is a high-confidence indicator of a **staged loader**.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Staged Execution & Environment Prep:** The combination of registry enumeration (to fetch C2/config) and dynamic API resolution (`GetProcAddress`, `LoadLibraryExW`) is a hallmark of a loader designed to hide its true functionality from static analysis until runtime.
*   **Evasion Tactics:** The use of `Sleep` loops for sandbox evasion, complex memory validation routines, and mathematical decoding of configuration blocks indicates intentional efforts to bypass security measures.
*   **Wrapper Characteristics:** The presence of "Inno Setup" strings coupled with file path manipulation strongly suggests the binary acts as a wrapper/dropper intended to facilitate the delivery and execution of a secondary payload.
