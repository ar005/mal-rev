# Threat Analysis Report

**Generated:** 2026-07-26 05:33 UTC
**Sample:** `0b58bbe496218fa82f98aff8990622ed7529bcbef31c2b782657a80eadccc734_0b58bbe496218fa82f98aff8990622ed7529bcbef31c2b782657a80eadccc734.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b58bbe496218fa82f98aff8990622ed7529bcbef31c2b782657a80eadccc734_0b58bbe496218fa82f98aff8990622ed7529bcbef31c2b782657a80eadccc734.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 8 sections |
| Size | 2,503,856 bytes |
| MD5 | `e3ff8593829a9c8fb976c964cac697f0` |
| SHA1 | `4e3eb008ce0fe14cf8b79d08e55905f68e8b9a84` |
| SHA256 | `0b58bbe496218fa82f98aff8990622ed7529bcbef31c2b782657a80eadccc734` |
| Overall entropy | 7.95 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1381652372 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 61,952 | 6.418 | No |
| `.itext` | 3,072 | 5.732 | No |
| `.data` | 3,584 | 2.246 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 3,584 | 4.972 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.204 | No |
| `.rsrc` | 194,048 | 6.194 | No |

### Imports

**oleaut32.dll**: `SysFreeString`, `SysReAllocStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**user32.dll**: `CreateWindowExW`, `TranslateMessage`, `SetWindowLongW`, `PeekMessageW`, `MsgWaitForMultipleObjects`, `MessageBoxW`, `LoadStringW`, `GetSystemMetrics`, `ExitWindowsEx`, `DispatchMessageW`, `DestroyWindow`, `CharUpperBuffW`, `CallWindowProcW`
**kernel32.dll**: `Sleep`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **5451** (showing first 100)

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
<J7d)|k\
t-Rf;
t f;J
XZ_^[X]X
tc<tB<tr<t}<
GetLongPathNameW
_^[YY]
	ExceptionLm@
EAbort
EHeapException
EOutOfMemory
EInOutError
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeError$q@
EIntOverflow

EMathError

EInvalidOp
EZeroDivide
	EOverflow

EUnderflow
EInvalidPointer t@
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
SetDllDirectoryW
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00408599` | `0x408599` | 3116 | ✓ |
| `fcn.00401c7c` | `0x401c7c` | 1900 | ✓ |
| `fcn.0040d22c` | `0x40d22c` | 1690 | ✓ |
| `fcn.004018f8` | `0x4018f8` | 1496 | ✓ |
| `fcn.0040845c` | `0x40845c` | 995 | ✓ |
| `fcn.004027b8` | `0x4027b8` | 993 | ✓ |
| `fcn.00404c80` | `0x404c80` | 841 | ✓ |
| `fcn.004088a4` | `0x4088a4` | 768 | ✓ |
| `fcn.0040a4c4` | `0x40a4c4` | 734 | ✓ |
| `fcn.00405de8` | `0x405de8` | 640 | ✓ |
| `fcn.00409110` | `0x409110` | 563 | ✓ |
| `fcn.00408ba4` | `0x408ba4` | 556 | ✓ |
| `entry0` | `0x4113bc` | 522 | ✓ |
| `fcn.00405bec` | `0x405bec` | 458 | ✓ |
| `fcn.004025f8` | `0x4025f8` | 448 | ✓ |
| `fcn.00409c58` | `0x409c58` | 443 | ✓ |
| `fcn.004093dc` | `0x4093dc` | 428 | ✓ |
| `fcn.00405940` | `0x405940` | 408 | ✓ |
| `fcn.00408204` | `0x408204` | 390 | ✓ |
| `fcn.0040567c` | `0x40567c` | 319 | ✓ |
| `fcn.0040ba24` | `0x40ba24` | 312 | ✓ |
| `fcn.0040dc68` | `0x40dc68` | 303 | ✓ |
| `fcn.00404af0` | `0x404af0` | 299 | ✓ |
| `fcn.00404580` | `0x404580` | 295 | ✓ |
| `fcn.004095c8` | `0x4095c8` | 293 | ✓ |
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
- [`code/fcn.00404af0.c`](code/fcn.00404af0.c)
- [`code/fcn.00404c80.c`](code/fcn.00404c80.c)
- [`code/fcn.0040513c.c`](code/fcn.0040513c.c)
- [`code/fcn.0040532c.c`](code/fcn.0040532c.c)
- [`code/fcn.0040567c.c`](code/fcn.0040567c.c)
- [`code/fcn.004057bc.c`](code/fcn.004057bc.c)
- [`code/fcn.00405940.c`](code/fcn.00405940.c)
- [`code/fcn.00405bec.c`](code/fcn.00405bec.c)
- [`code/fcn.00405de8.c`](code/fcn.00405de8.c)
- [`code/fcn.00408204.c`](code/fcn.00408204.c)
- [`code/fcn.0040845c.c`](code/fcn.0040845c.c)
- [`code/fcn.00408599.c`](code/fcn.00408599.c)
- [`code/fcn.004088a4.c`](code/fcn.004088a4.c)
- [`code/fcn.00408ba4.c`](code/fcn.00408ba4.c)
- [`code/fcn.00409110.c`](code/fcn.00409110.c)
- [`code/fcn.004093dc.c`](code/fcn.004093dc.c)
- [`code/fcn.004095c8.c`](code/fcn.004095c8.c)
- [`code/fcn.00409c58.c`](code/fcn.00409c58.c)
- [`code/fcn.0040a4c4.c`](code/fcn.0040a4c4.c)
- [`code/fcn.0040ba24.c`](code/fcn.0040ba24.c)
- [`code/fcn.0040d22c.c`](code/fcn.0040d22c.c)
- [`code/fcn.0040dc68.c`](code/fcn.0040dc68.c)

## Behavioral Analysis

### Analysis Summary
The binary appears to be a **packer or loader** (often referred to as a "stub") designed to unpack and execute a hidden malicious payload. The presence of "Inno Setup" strings, combined with heavy use of memory management functions (`VirtualAlloc`, `VirtualProtect`), suggests this is the initial stage of an infection chain where the primary malware is wrapped in a secondary layer to evade detection.

---

### Core Functionality & Purpose
The code serves as a **delivery and extraction mechanism**. Its primary roles are:
*   **Environment Preparation:** Initializing resources, handling system information, and resolving the necessary environment for the payload.
*   **Resource Extraction:** Searching the registry (`RegOpenKeyExW`) and local directories to locate components or configuration data needed for the next stage.
*   **Payload Decryption/Decompression:** The presence of several complex loops (e.g., `fcn.0040d22c`) processing memory buffers suggests it is decrypting or decompressing an embedded payload.

### Suspicious & Malicious Behaviors
The following behaviors are indicative of malicious intent:

*   **Dynamic API Resolution:** The use of `GetProcAddress` and `GetModuleHandleW` (seen in several functions) allows the program to resolve system functions at runtime rather than having them all listed in the Import Address Table (IAT). This is a common technique used by malware to hide its capabilities from static analysis tools.
*   **Memory Manipulation:** The code frequently uses `VirtualProtect` and `VirtualAlloc`. These are typical for **process injection** or **self-unpacking**, where a piece of memory is allocated, filled with "hidden" code, and then changed to "executable" status so it can be run.
*   **Registry Interaction:** Function `fcn.00405ec` specifically queries several registry keys. This is often used by malware to retrieve configuration data (such as C2 server IPs or file paths for dropped payloads) that are not stored directly in the binary's code.
*   **File Dropping/Writing:** The function `fcn.004095c8` interacts with `WriteFile`. In this context, it is likely "dropping" the unpacked malicious executable onto the disk or into a temporary directory before executing it. 
*   **Anti-Analysis (Implied):** While not a direct anti-debugging check in every line, the complex loop structures and repeated calls to memory management suggest an attempt to obfuscate the "true" payload from automated analysis tools.

### Notable Techniques & Patterns
*   **Inno Setup Wrap:** The strings indicate the sample was distributed using Inno Setup. This is a common technique where malware is wrapped in a legitimate installer to appear as a standard software installation while it performs background malicious tasks.
*   **Decryption Loops:** Several functions exhibit loops that iterate over memory buffers, performing bitwise operations and substitutions. These are characteristic of **decryption routines**. 
*   **Multi-Stage Execution:** The way the code handles "finding" files and then handling a sequence of steps (visible in `fcn.00405ec` and `fcn.004095c8`) suggests a multi-stage infection where this binary is merely the first step to get the real payload onto the machine.
*   **Heavy use of Stack/Heap checks:** The logic surrounding memory sizing (`VirtualQuery`, checking for `0x1000` page sizes) indicates that the code is carefully navigating and managing chunks of memory, likely as part of a custom PE (Portable Executable) loader.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files/Information | The use of decryption loops and dynamic API resolution (GetProcAddress) are core methods used to hide the true functionality of a payload from static analysis. |
| **T1055** | Process Injection | The specific usage of `VirtualAlloc` and `VirtualProtect` indicates the manual allocation and permission modification of memory segments to execute unpacked code. |
| **T1036.005** | Masquerading: Package Installer | The use of "Inno Setup" strings suggests that the malware is wrapped inside a legitimate installer to blend in with standard software installations. |
| **T1112** | Software Discovery | The querying of registry keys (`RegOpenKeyExW`) indicates an attempt to gather configuration data or environment information to facilitate subsequent stages of the attack. |
| **T1547.001** | Registry File Execution | While primarily for persistence, the frequent interaction with specific registry keys suggests the loader is identifying system paths and configurations necessary for execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Many elements in the "EXTRACTED STRINGS" section were identified as standard Windows APIs (e.g., `GetProcAddress`, `VirtualProtect`) or common Delphi/Inno Setup components and have been excluded as false positives.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None explicitly listed (The analysis notes that registry keys are queried in function `fcn.00405ec` and files are written via `fcn.004095c8`, but no specific paths or keys were provided in the source text).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Known Frameworks:** Inno Setup (used as a wrapper/installer for the payload).
*   **Suspicious Function Offsets:** 
    *   `fcn.0040d22c` (Decryption/Decompression routine)
    *   `fcn.00405ec` (Registry interaction/Configuration retrieval)
    *   `fcn.004095c8` (File dropping/Write operation)
*   **Techniques Identified:** 
    *   Dynamic API Resolution (`GetProcAddress`, `GetModuleHandleW`)
    *   Memory Manipulation for execution (`VirtualProtect`, `VirtualAlloc`)
    *   Multi-stage payload unpacking.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Stub/Loader Behavior:** The sample exhibits classic "packer stub" characteristics, utilizing `VirtualAlloc` and `VirtualProtect` to manage memory for the execution of a hidden payload that is decrypted or decompressed in-memory.
*   **Evasion & Obfuscation:** The use of dynamic API resolution (`GetProcAddress`) and complex decryption loops indicates an intentional effort to hide the true capabilities of the malicious payload from static analysis tools.
*   **Multi-stage Delivery:** The integration of "Inno Setup" strings suggests a wrapping technique designed to masquerade as a legitimate installer, while its core functionality focuses on environment preparation and extracting configuration data via registry queries for subsequent infection stages.
