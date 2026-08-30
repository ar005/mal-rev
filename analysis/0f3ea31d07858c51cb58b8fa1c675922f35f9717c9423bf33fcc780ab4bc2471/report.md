# Threat Analysis Report

**Generated:** 2026-08-15 20:28 UTC
**Sample:** `0f3ea31d07858c51cb58b8fa1c675922f35f9717c9423bf33fcc780ab4bc2471_0f3ea31d07858c51cb58b8fa1c675922f35f9717c9423bf33fcc780ab4bc2471.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f3ea31d07858c51cb58b8fa1c675922f35f9717c9423bf33fcc780ab4bc2471_0f3ea31d07858c51cb58b8fa1c675922f35f9717c9423bf33fcc780ab4bc2471.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 8 sections |
| Size | 665,379 bytes |
| MD5 | `4aeee792a7fe99de7b07f6e90c862924` |
| SHA1 | `25e1706155cbb7b98bac9546ea4f9904d7ede456` |
| SHA256 | `0f3ea31d07858c51cb58b8fa1c675922f35f9717c9423bf33fcc780ab4bc2471` |
| Overall entropy | 7.786 |
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
| `.rsrc` | 57,344 | 4.27 | No |

### Imports

**oleaut32.dll**: `SysFreeString`, `SysReAllocStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**user32.dll**: `CreateWindowExW`, `TranslateMessage`, `SetWindowLongW`, `PeekMessageW`, `MsgWaitForMultipleObjects`, `MessageBoxW`, `LoadStringW`, `GetSystemMetrics`, `ExitWindowsEx`, `DispatchMessageW`, `DestroyWindow`, `CharUpperBuffW`, `CallWindowProcW`
**kernel32.dll**: `Sleep`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **1525** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality and characteristics.

### Core Functionality
The binary appears to be a **downloader or a multi-stage "loader" component**, likely part of a larger malware suite (evidenced by its construction in Inno Setup). Its primary purpose is to locate, verify, and load additional modules (DLLs) based on paths and parameters stored in the Windows Registry.

### Suspicious & Malicious Behaviors
*   **Registry-Based Payload Discovery:** The function `fcn.00405de8` is highly indicative of malware behavior. It performs multiple calls to `RegOpenKeyExW` across different hives/keys (e.g., `hkey_current_user` and `hkey_local_machine`). It specifically looks for values at specific offsets (`0x406068`, `0x40609c`, etc.) to construct paths for the next stage of execution.
*   **Dynamic DLL Loading:** After retrieving data from the registry, the code uses `lstrcpynW` to manipulate these strings (likely removing extensions or appending required filenames) and then attempts to load them using `LoadLibraryExW`. This is a common technique used by "droppers" to find and execute hidden components.
*   **Path Obfuscation/Normalization:** The logic in `fcn.00405bc8` involves complex loops to handle directory separators and path lengths. This allows the malware to dynamically resolve where its next stage is located, making it harder for automated tools to trace the final execution path.
*   **Fall-back Logic for Hidden Components:** The nested `if` statements and multiple attempts at loading different paths (using `lstrcpynW`) suggest a "failover" system; if the primary hidden location isn't found, it tries secondary locations or alternate names to ensure the payload is successfully loaded.
*   **Potential Anti-Analysis/Stealth:** The use of `GetModuleFileNameW` combined with relative path manipulation suggests the binary may be trying to hide its true source directory from simple analysis by resolving paths only at runtime.

### Notable Techniques & Patterns
*   **Inno Setup Framework:** The presence of strings like `"Inno Setup Setup Data"` and various Delphi-related compiler artifacts (`AnsiString`, `TObject`) suggests the binary was packaged using Inno Setup. Malware authors frequently use this because it provides a professional "installer" appearance for their delivery chain.
*   **Dynamic Resolution via GetProcAddress:** The inclusion of `GetProcAddress` and `GetModuleHandleW` along with `VirtualAlloc` / `VirtualProtect` (seen in several sub-functions) indicates the binary is capable of resolving API functions dynamically or manipulating memory permissions to execute shellcode or unpacked code.
*   **Interaction with System Handles:** Function `fcn.004096ac` interacts directly with the standard output handle (`-0xc`) and uses `WriteFile`. This could be used for logging errors during the "installation" of a malicious payload or, in some cases, to communicate over unconventional channels.
*   **Standard Window Messaging/Dialogs:** The use of `MessageBoxW` and `LoadStringW` suggest that while the core logic is automated, there may be interaction points (like an error message if the loader fails) to provide a seamless "user experience" during infection.

### Summary Conclusion
This binary is likely a **loader or installer component** used in a multi-stage infection chain. It does not seem to perform high-level and complex encryption itself; instead, it acts as the **bridge**, reaching out into the Registry to find its actual payload (the "payload" being whatever malicious functionality—like a stealer, miner, or ransomware—it loads via `LoadLibraryExW`).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1631 | Dynamic Resolution | The use of `GetProcAddress`, `LoadLibraryExW`, and `VirtualAlloc` indicates the binary resolves function addresses and loads modules at runtime to evade static analysis. |
| T1027 | Obfuscated Files or Information | The implementation of complex path normalization, "fall-back" logic, and registry-based construction hides the final payload's location from automated detection tools. |
| T1036 | Masquerading | By utilizing the Inno Setup framework and `GetModuleFileNameW` to resolve paths at runtime, the binary attempts to blend in with legitimate system installers. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (Note: While the behavior mentions the use of `hkey_current_user` and `hkey_local_machine`, no specific sub-keys or file paths were provided in the strings.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Installer Framework:** Inno Setup (Versions 5.5.7 and 5.5.3)
*   **Development Environment:** Borland FastMM, Delphi-related strings (`AnsiString`, `TObject`, `TErrorRec`)
*   **Suspicious Behavior Patterns:** 
    *   Dynamic DLL Loading via `LoadLibraryExW` and `GetProcAddress`.
    *   Memory manipulation using `VirtualAlloc` and `VirtualProtect`.
    *   Registry-based payload discovery (scanning multiple keys to resolve paths).
    *   Use of `lstrcpynW` for dynamic path normalization/obfuscation.
*   **Internal Function Offsets (for forensic mapping):** 
    *   `00405de8` (Registry/Payload Discovery)
    *   `00405bc8` (Path Obfuscation logic)
    *   `004096ac` (Standard output/WriteFile interactions)

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Downloader
3. **Confidence**: High

**Key evidence**:
*   **Registry-Based Payload Discovery:** The binary performs systematic lookups in `hkey_current_user` and `hkey_local_machine` to resolve paths for subsequent modules, a classic hallmark of a multi-stage loader designed to hide the final payload.
*   **Dynamic Execution & Obfuscation:** The use of `GetProcAddress`, `LoadLibraryExW`, and `VirtualProtect` indicates it is designed to load and execute code (such as DLLs or shellcode) while bypassing static analysis.
*   **Stealth Packaging:** The integration with the Inno Setup framework and the implementation of complex "fall-back" logic for path normalization are common tactics used to ensure a successful infection even if certain files or paths have been modified by security software.
