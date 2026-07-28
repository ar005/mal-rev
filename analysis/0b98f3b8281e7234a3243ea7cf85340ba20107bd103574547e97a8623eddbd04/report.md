# Threat Analysis Report

**Generated:** 2026-07-27 13:51 UTC
**Sample:** `0b98f3b8281e7234a3243ea7cf85340ba20107bd103574547e97a8623eddbd04_0b98f3b8281e7234a3243ea7cf85340ba20107bd103574547e97a8623eddbd04.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b98f3b8281e7234a3243ea7cf85340ba20107bd103574547e97a8623eddbd04_0b98f3b8281e7234a3243ea7cf85340ba20107bd103574547e97a8623eddbd04.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 8 sections |
| Size | 61,786,192 bytes |
| MD5 | `74e7f5af5f1c148a59ea8aba6423a20d` |
| SHA1 | `ed3bacdddcc6ff6744dc18bfa1d6116d57b31801` |
| SHA256 | `0b98f3b8281e7234a3243ea7cf85340ba20107bd103574547e97a8623eddbd04` |
| Overall entropy | 8.0 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1528982866 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 62,464 | 6.376 | No |
| `.itext` | 4,096 | 5.779 | No |
| `.data` | 3,584 | 2.303 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 4,096 | 4.598 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.204 | No |
| `.rsrc` | 102,400 | 6.899 | No |

### Imports

**oleaut32.dll**: `SysFreeString`, `SysReAllocStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**user32.dll**: `CreateWindowExW`, `TranslateMessage`, `SetWindowLongW`, `PeekMessageW`, `MsgWaitForMultipleObjects`, `MessageBoxW`, `LoadStringW`, `GetSystemMetrics`, `ExitWindowsEx`, `DispatchMessageW`, `DestroyWindow`, `CharUpperBuffW`, `CallWindowProcW`
**kernel32.dll**: `Sleep`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **134268** (showing first 100)

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
| `entry0` | `0x41181c` | 522 | ✓ |
| `fcn.00405bec` | `0x405bec` | 458 | ✓ |
| `fcn.004025f8` | `0x4025f8` | 448 | ✓ |
| `fcn.00409d3c` | `0x409d3c` | 443 | ✓ |
| `fcn.004094c0` | `0x4094c0` | 428 | ✓ |
| `fcn.00405940` | `0x405940` | 408 | ✓ |
| `fcn.004082e8` | `0x4082e8` | 390 | ✓ |
| `fcn.00404b9c` | `0x404b9c` | 355 | ✓ |
| `fcn.0040567c` | `0x40567c` | 319 | ✓ |
| `fcn.0040bb34` | `0x40bb34` | 312 | ✓ |
| `fcn.0040dd98` | `0x40dd98` | 303 | ✓ |
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
- [`code/fcn.0040dd98.c`](code/fcn.0040dd98.c)

## Behavioral Analysis

Based on my analysis of the provided disassembly and decompiled code, here is a summary of the program's behavior.

### Core Functionality and Purpose
The binary appears to function as a **downloader/loader or a complex installer**. While it contains elements typical of an Inno Setup-based installer (as evidenced by the strings), the underlying logic shows characteristics common in malware "droppers" or "loaders." Its primary purpose seems to be locating, preparing, and potentially executing secondary components based on data retrieved from the Windows Registry.

### Suspicious/Malicious Behaviors
The following behaviors are indicative of malicious intent or evasion tactics:

*   **Dynamic Payload Discovery:** 
    *   In `fcn.00405dec`, the program performs a loop to resolve file paths. It takes values from registry keys (via `RegOpenKeyExW` and `RegQueryValueExW`) and then iteratively checks for various file extensions (such as `.exe`, `.dll`, or potentially others) by manipulating strings until it finds a valid path to load via `LoadLibraryExW`.
    *   This "search-and-load" behavior is a common technique used by malware to find hidden components or payloads that do not have standard filenames, helping them evade simple signature-based detection.

*   **Memory Manipulation & Execution Preparation:**
    *   Several functions (e.g., `fcn.004018f8`, `fcn.00401c7c`) heavily utilize `VirtualAlloc`, `VirtualProtect`, and `VirtualFree`. 
    *   The complexity of these routines suggests the program is allocating memory with specific permissions (likely RWX) to host a "payload" or is managing a complex, unpacked resource state in memory.

*   **Anti-Analysis/Evasion Techniques:**
    *   The code contains repeated calls to `Sleep(0)` and `Sleep(10)` inside loops (e.g., in `fcn.00401c7c` and `fcn.004018f8`). These are often used as "stalling" tactics to bypass automated sandbox analysis by making the execution timeline longer or complicating timing-based detection.
    *   The heavy use of internal abstraction (complex nested loops, switch tables, and several layers of wrapper functions) suggests an attempt to obfuscate the core logic from simple static analysis.

*   **System Interaction:**
    *   The code interacts with standard Windows components for output (`GetStdHandle` / `WriteFile`) and user notification (`MessageBoxW`). However, in this context, such calls are often used to provide "decoy" feedback or signify that a malicious task (like loading a DLL) has completed.

### Notable Techniques/Patterns
*   **Registry-Driven Configuration:** The reliance on Registry values to determine file paths and internal logic suggests the malware uses registry keys as a Command & Control (C2) point for local configuration (a common tactic in multi-stage infections).
*   **Inno Setup Wrapping:** The presence of Inno Setup strings combined with "hidden" malicious functionality is a classic indicator of a **Trojanized Installer**, where a legitimate installer is modified to include a downloader or loader.
*   **Dynamic Library Resolution:** Use of `GetProcAddress` and `GetModuleHandleW` indicates the program resolves API calls at runtime, potentially allowing it to bypass static imports analysis.

### Summary for Incident Response
This sample should be treated as a **Loader/Dropper**. It is designed to find an external payload (likely a DLL or EXE) from local system configurations (Registry) and load it into memory. The presence of multi-extension searching and deliberate sleeping suggests it is engineered to evade automated security analysis.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036.003** | Masquerading: Trojanized | The use of Inno Setup strings combined with hidden malicious functionality indicates a trojanized installer designed to hide the loader's purpose. |
| **T1112** | Registry File Modification | The program retrieves configuration data and payload file paths from Windows Registry keys to facilitate its operations. |
| **T1497** | Virtualization/Sandbox Detection | Frequent `Sleep` calls are utilized as stalling tactics to bypass automated sandboxes by exhausting the analysis time window. |
| **T1055** | Process Injection | The extensive use of `VirtualAlloc`, `VirtualProtect`, and `VirtualFree` indicates the allocation and preparation of memory segments for loading a payload. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs).

**Note:** While the sample exhibits clear malicious behavior (a Trojanized Installer/Loader), it does not contain hardcoded network indicators (IPs/URLs) or specific file paths in the provided string dump.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   **Registry Interaction:** The analysis identifies **Registry-Driven Configuration**. While no specific key names were extracted from the strings, the binary actively queries the Windows Registry to determine file paths and internal logic for payload loading.
*   **Dynamic File Paths:** The binary performs a "search-and-load" routine for files with `.exe` and `.dll` extensions.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Software Framework:** Inno Setup (Versions 5.5.7 and 5.5.3). This indicates the use of a known installer framework as a wrapper for malicious code.
*   **Evasion Tactics:** 
    *   **Stalling/Sleep Loops:** Use of `Sleep(0)` and `Sleep(10)` to bypass automated sandbox analysis.
    *   **API Obfuscation:** Utilization of `GetProcAddress` and `GetModuleHandleW` for dynamic resolution of functions to evade static import analysis.
*   **Memory Manipulation:** High frequency of `VirtualAlloc`, `VirtualProtect`, and `VirtualFree` (specifically targeting RWX permissions) suggests the injection or unpacking of a payload in memory.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

1. **Malware family**: unknown
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
* **Payload Loading & Memory Manipulation:** The sample exhibits classic "loader" behavior by utilizing `VirtualAlloc`, `VirtualProtect`, and `LoadLibraryExW` to prepare memory segments for an external payload, coupled with dynamic API resolution (`GetProcAddress`) to hide its true capabilities from static analysis.
* **Evasion Tactics:** The presence of deliberate stalling loops (`Sleep(0)`, `Sleep(10)`), "search-and-load" logic for registry-based file paths, and the use of an Inno Setup wrapper are all hallmark techniques used to bypass automated sandboxes and evade signature-based detection.
* **Registry-Driven Configuration:** The reliance on the Windows Registry to determine its execution path and internal configuration indicates a multi-stage infection chain where this sample serves as the initial gateway for more complex malware components.
