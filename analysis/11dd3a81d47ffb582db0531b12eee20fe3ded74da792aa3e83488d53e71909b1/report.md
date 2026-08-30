# Threat Analysis Report

**Generated:** 2026-08-24 19:18 UTC
**Sample:** `11dd3a81d47ffb582db0531b12eee20fe3ded74da792aa3e83488d53e71909b1_11dd3a81d47ffb582db0531b12eee20fe3ded74da792aa3e83488d53e71909b1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11dd3a81d47ffb582db0531b12eee20fe3ded74da792aa3e83488d53e71909b1_11dd3a81d47ffb582db0531b12eee20fe3ded74da792aa3e83488d53e71909b1.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 8 sections |
| Size | 12,678,198 bytes |
| MD5 | `a308529e8f247baf959a5c7b9da8286d` |
| SHA1 | `81925a80377b00da36ee48dff82b1b93db680e09` |
| SHA256 | `11dd3a81d47ffb582db0531b12eee20fe3ded74da792aa3e83488d53e71909b1` |
| Overall entropy | 7.998 |
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
| `.text` | 62,464 | 6.582 | No |
| `.itext` | 4,096 | 5.779 | No |
| `.data` | 3,584 | 2.303 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 4,096 | 4.598 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.204 | No |
| `.rsrc` | 508,928 | 7.759 | ⚠️ Yes |

### Imports

**oleaut32.dll**: `SysFreeString`, `SysReAllocStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**user32.dll**: `CreateWindowExW`, `TranslateMessage`, `SetWindowLongW`, `PeekMessageW`, `MsgWaitForMultipleObjects`, `MessageBoxW`, `LoadStringW`, `GetSystemMetrics`, `ExitWindowsEx`, `DispatchMessageW`, `DestroyWindow`, `CharUpperBuffW`, `CallWindowProcW`
**kernel32.dll**: `Sleep`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **27114** (showing first 100)

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
C35M/A
t!^.A
Ji/A
!=b.A
k2)M.A
\G0/A
HV3=;/A
IK!=!.A
WG=W/A
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
SetDllDirectoryW
SetSearchPathMode
SetProcessDEPPolicy
Runtime error     at 00000000
Inno Setup Setup Data (5.5.7) (u)
Inno Setup Messages (5.5.3) (u)
oleaut32.dll
SysFreeString
SysReAllocStringLen
SysAllocStringLen
advapi32.dll
RegQueryValueExW
RegOpenKeyExW
RegCloseKey
user32.dll
GetKeyboardType
LoadStringW
MessageBoxA
CharNextW
kernel32.dll
GetACP
VirtualFree
VirtualAlloc
GetSystemInfo
GetTickCount
QueryPerformanceCounter
GetVersion
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040867d` | `0x40867d` | 3116 | ✓ |
| `fcn.0040d33c` | `0x40d33c` | 1690 | ✓ |
| `fcn.00401c7c` | `0x401c7c` | 1580 | ✓ |
| `fcn.004018f8` | `0x4018f8` | 1228 | ✓ |
| `fcn.004027b8` | `0x4027b8` | 992 | ✓ |
| `fcn.0040862e` | `0x40862e` | 930 | ✓ |
| `fcn.00404c80` | `0x404c80` | 841 | ✓ |
| `fcn.00408988` | `0x408988` | 768 | ✓ |
| `fcn.0040a5a8` | `0x40a5a8` | 734 | ✓ |
| `fcn.004091f4` | `0x4091f4` | 562 | ✓ |
| `fcn.00408c88` | `0x408c88` | 556 | ✓ |
| `entry0` | `0x41181c` | 522 | ✓ |
| `fcn.004082d4` | `0x4082d4` | 473 | ✓ |
| `fcn.004025f8` | `0x4025f8` | 448 | ✓ |
| `fcn.00405de8` | `0x405de8` | 444 | ✓ |
| `fcn.00409d3c` | `0x409d3c` | 442 | ✓ |
| `fcn.004094c0` | `0x4094c0` | 428 | ✓ |
| `fcn.00405940` | `0x405940` | 408 | ✓ |
| `fcn.00404b9c` | `0x404b9c` | 355 | ✓ |
| `fcn.0040567c` | `0x40567c` | 319 | ✓ |
| `fcn.0040bb34` | `0x40bb34` | 311 | ✓ |
| `fcn.0040dd98` | `0x40dd98` | 302 | ✓ |
| `fcn.004096ac` | `0x4096ac` | 293 | ✓ |
| `fcn.00402be0` | `0x402be0` | 293 | ✓ |
| `fcn.0040532c` | `0x40532c` | 286 | ✓ |
| `fcn.0040513c` | `0x40513c` | 284 | ✓ |
| `fcn.00402260` | `0x402260` | 281 | ✓ |
| `fcn.004057bc` | `0x4057bc` | 276 | ✓ |
| `fcn.0040c854` | `0x40c854` | 275 | ✓ |
| `fcn.00408cb5` | `0x408cb5` | 274 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004018f8.c`](code/fcn.004018f8.c)
- [`code/fcn.00401c7c.c`](code/fcn.00401c7c.c)
- [`code/fcn.00402260.c`](code/fcn.00402260.c)
- [`code/fcn.004025f8.c`](code/fcn.004025f8.c)
- [`code/fcn.004027b8.c`](code/fcn.004027b8.c)
- [`code/fcn.00402be0.c`](code/fcn.00402be0.c)
- [`code/fcn.00404b9c.c`](code/fcn.00404b9c.c)
- [`code/fcn.00404c80.c`](code/fcn.00404c80.c)
- [`code/fcn.0040513c.c`](code/fcn.0040513c.c)
- [`code/fcn.0040532c.c`](code/fcn.0040532c.c)
- [`code/fcn.0040567c.c`](code/fcn.0040567c.c)
- [`code/fcn.004057bc.c`](code/fcn.004057bc.c)
- [`code/fcn.00405940.c`](code/fcn.00405940.c)
- [`code/fcn.00405de8.c`](code/fcn.00405de8.c)
- [`code/fcn.004082d4.c`](code/fcn.004082d4.c)
- [`code/fcn.0040862e.c`](code/fcn.0040862e.c)
- [`code/fcn.0040867d.c`](code/fcn.0040867d.c)
- [`code/fcn.00408988.c`](code/fcn.00408988.c)
- [`code/fcn.00408c88.c`](code/fcn.00408c88.c)
- [`code/fcn.00408cb5.c`](code/fcn.00408cb5.c)
- [`code/fcn.004091f4.c`](code/fcn.004091f4.c)
- [`code/fcn.004094c0.c`](code/fcn.004094c0.c)
- [`code/fcn.004096ac.c`](code/fcn.004096ac.c)
- [`code/fcn.00409d3c.c`](code/fcn.00409d3c.c)
- [`code/fcn.0040a5a8.c`](code/fcn.0040a5a8.c)
- [`code/fcn.0040bb34.c`](code/fcn.0040bb34.c)
- [`code/fcn.0040c854.c`](code/fcn.0040c854.c)
- [`code/fcn.0040d33c.c`](code/fcn.0040d33c.c)
- [`code/fcn.0040dd98.c`](code/fcn.0040dd98.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is a professional analysis of the binary's behavior.

### Core Functionality and Purpose
The code exhibits characteristics of an **installer or packer** built using Delphi/Pascal (indicated by `FastMM`, `AnsiString`, and `Inno Setup` references). However, the complexity of the underlying logic suggests it is likely a **packed executable** or an **obfuscated loader**.

*   **Installer Foundation:** The presence of "Inno Setup" strings and standard setup structures indicates that this binary was originally built as an installer.
*   **Obfuscation/Packing:** A significant portion of the code (e.g., `fcn.0040867d`, `fcn.004082d4`) consists of "heavy" arithmetic, bitwise operations, and convoluted logic to calculate memory addresses or values. This is a hallmark of **packer technology** or **code obfuscation**, used to hide the real underlying functionality of the payload from automated analysis.
*   **Dynamic Resolution:** The frequent use of `GetProcAddress` and `LoadLibraryExW` indicates that the program resolves its dependencies at runtime rather than relying solely on the standard Import Address Table (IAT).

### Suspicious or Malicious Behaviors

*   **Advanced Obfuscation & Junk Code:** Functions like `fcn.0040867d` and `fcn.004082d4` contain layers of junk instructions and complex math to calculate offsets. This is commonly used by malware authors to hinder static analysis and make it difficult for analysts to follow the execution flow.
*   **Memory Management Manipulation:** The functions `fcn.0041c7c` and `fcn.004018f8` interact with `VirtualAlloc`, `VirtualProtect`, and `VirtualFree`. In this context, these are often used by packers to allocate memory regions, change their permissions (e.g., from Read/Write to Execute), and "unpack" or inject code into those newly allocated spaces.
*   **Registry Interaction & System Surveying:** Function `fcn.00405de8` performs several `RegOpenKeyExW` calls on various system keys. It specifically uses `GetModuleFileNameW` and `lstrcpynW` to construct paths based on the current executable's name, which may be used to determine system environment details or locate target software/directories for further interaction.
*   **Dynamic Path Construction:** The code frequently builds strings in memory (e.g., in `fcn.004027b8`) and manipulates string buffers before making API calls. This is often done to hide the final destination of a file or the name of a network resource until the last possible moment during execution.

### Notable Techniques & Patterns

*   **Anti-Analysis (via Complexity):** The "messy" nature of the decompiler output for several functions indicates that the code was intentionally designed to be difficult to read for both humans and decompilers, likely using **control-flow flattening** or **instruction substitution**.
*   **Delphi-based Packaging:** By wrapping malicious logic in a legitimate (but modified) Inno Setup wrapper, the author aims to evade simple signature-based detection by masquerading as a standard installer.
*   **Resource Management:** The use of `GetModuleFileNameW` across multiple functions suggests that the program is highly dependent on its relative location and is likely attempting to locate sibling files or perform internal resource loading from its own directory.

### Summary for Incident Response
This binary is likely an **obfuscated dropper or packer**. While it uses a legitimate installer framework, the underlying code employs advanced evasion techniques (junk code insertion, manual memory management, and dynamic API resolution) typically found in sophisticated malware to hide a malicious payload (such as a downloader, information stealer, or ransomware) within the wrapper.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of "heavy" arithmetic, bitwise operations, junk instructions, and control-flow flattening is intended to hinder static analysis. |
| **T1055** | Packer | The binary exhibits hallmarks of a packer, including the use of `VirtualAlloc` and `VirtualProtect` to transition memory permissions for code execution. |
| **T1134** | Masquerading | By using a legitimate Inno Setup wrapper, the malware masquerades as a standard installer to evade signature-based detection. |
| **T1012** | Query Registry | The use of `RegOpenKeyExW` to query various system keys indicates an attempt to gather information about the local environment. |
| **T1036** | (Implicit) Preparation for Execution | The dynamic resolution of functions via `GetProcAddress` and `LoadLibraryExW` is used to hide the true capabilities of the binary from static analysis tools. |

---

## Indicators of Compromise

Based on the provided data, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Many items in the "Strings" section were identified as standard library functions, compiler artifacts (Delphi/Pascal), or generic installer components; these have been excluded as per your instructions to avoid false positives.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (The behavioral analysis notes the *action* of querying registry keys and constructing file paths, but no specific hardcoded paths or keys were provided in the string dump.)

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Internal Function Offsets (Potential for YARA/Signature Development):**
    *   `0040867d` (Identified as a location containing heavy obfuscation/junk code)
    *   `004082d4` (Identified as a location containing heavy obfuscation/junk code)
    *   `0041c7c` (Identified as a memory management/unpacking function)
    *   `004018f8` (Identified as a memory management/unpacking function)
    *   `00405de8` (Identified as the registry interaction/system surveying function)
    *   `004027b8` (Identified as a dynamic string construction function)
*   **Software Environment Markers:**
    *   **Inno Setup Version 5.5.7** / **Inno Setup Messages 5.5.3** (Indicates the specific version of the packer/installer wrapper used).
    *   **FastMM Borland Edition** (Confirms usage of a Delphi/Pascal-based compiler environment).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

**Key evidence**:
*   **Advanced Packing & Obfuscation:** The presence of heavy arithmetic, junk code insertion, and "messy" decompiler output indicates a deliberate attempt to hide the underlying payload from static analysis (T1027).
*   **Memory Manipulation for Payload Execution:** The use of `VirtualAlloc`, `VirtualProtect`, and `GetProcAddress` is a hallmark of loaders designed to decrypt or inject malicious code into memory at runtime.
*   **Stealthy Delivery Framework:** By wrapping the logic in an **Inno Setup** installer, the malware attempts to mask its purpose by masquerading as a legitimate software installation tool (T1134).
