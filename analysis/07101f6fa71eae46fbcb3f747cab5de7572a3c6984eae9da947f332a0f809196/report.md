# Threat Analysis Report

**Generated:** 2026-07-15 18:53 UTC
**Sample:** `07101f6fa71eae46fbcb3f747cab5de7572a3c6984eae9da947f332a0f809196_07101f6fa71eae46fbcb3f747cab5de7572a3c6984eae9da947f332a0f809196.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07101f6fa71eae46fbcb3f747cab5de7572a3c6984eae9da947f332a0f809196_07101f6fa71eae46fbcb3f747cab5de7572a3c6984eae9da947f332a0f809196.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 4,974,399 bytes |
| MD5 | `1260c089ac4c3b8206f8acdce24fae29` |
| SHA1 | `3465807dee07565661629d77e3aa124da28cffb6` |
| SHA256 | `07101f6fa71eae46fbcb3f747cab5de7572a3c6984eae9da947f332a0f809196` |
| Overall entropy | 7.999 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 708992537 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `CODE` | 37,888 | 6.53 | No |
| `DATA` | 1,024 | 2.734 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 2,560 | 4.431 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.204 | No |
| `.reloc` | 0 | 0.0 | No |
| `.rsrc` | 11,264 | 4.462 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **11047** (showing first 100)

```
This program must be run under Win32
$7
.idata
.rdata
P.reloc
P.rsrc
string
InitInstance
CleanupInstance
	ClassType
	ClassName
ClassNameIs
ClassParent
	ClassInfo
InstanceSize
InheritsFrom
Dispatch
MethodAddress

MethodName
FieldAddress
DefaultHandler
NewInstance
FreeInstance
TObject
YZ]_^[
C;D$v
D$+D$
YZ]_^[
YZ]_^[
_^[YY]
YZ]_^[
:
u0Nt
:
u	@B
ZTUWVSPRTj
t!R:
t
tVSVWU
D$PSWj
tHt Ht.
0123456789ABCDEF3
	Exception
EAbort
EOutOfMemory
EInOutError
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
EExternalException
m/d/yy
mmmm d, yyyy
:mm:ss
_^[YY]
INFNANU
$*@@@*$@@@$ *@@* $@@($*)@-$*@@$-*@@$*-@@(*$)@-*$@@*-$@@*$-@@-* $@-$ *@* $-@$ *-@$ -*@*- $@($ *)(* $)U
<'t$<"t 

<#t&<0t%<.t,<,t3<'t5<"t1<Et:<et6<;tF

<#t'<0t#<.t
<Et$<et <;tS

<Eu
FR
_^[YY]
YZ]_^[
_^[YY]
_^[YY]
USERPROFILE
GetUserDefaultUILanguage
kernel32.dll
.DEFAULT\Control Panel\International
Locale
Control Panel\Desktop\ResourceLocale
[ExceptObject=nil]
TCustomFile

EFileError
File I/O error %d
ECompressError
ECompressDataError
ECompressInternalError
TCustomDecompressor
TCompressedBlockReader
Compressed block is corrupted
Compressed block is corrupted
$Z]_^[
Compressed block is corrupted
TLZMADecompressor
lzma: 
lzma: Compressed data is corrupted (%d)
t$;sdt'
LzmaDecode failed (%d)
YZ]_^[
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00408330` | `0x408330` | 1690 | ✓ |
| `fcn.00404da8` | `0x404da8` | 773 | ✓ |
| `fcn.00403f67` | `0x403f67` | 731 | ✓ |
| `fcn.00405314` | `0x405314` | 584 | ✓ |
| `entry0` | `0x409b24` | 507 | ✓ |
| `fcn.00404eca` | `0x404eca` | 474 | ✓ |
| `fcn.00402300` | `0x402300` | 463 | ✓ |
| `fcn.0040215c` | `0x40215c` | 418 | ✓ |
| `fcn.00401fd4` | `0x401fd4` | 389 | ✓ |
| `fcn.00405628` | `0x405628` | 378 | ✓ |
| `fcn.00403e41` | `0x403e41` | 328 | ✓ |
| `fcn.00406d70` | `0x406d70` | 312 | ✓ |
| `fcn.004051d0` | `0x4051d0` | 310 | ✓ |
| `fcn.00401768` | `0x401768` | 291 | ✓ |
| `fcn.004096e8` | `0x4096e8` | 275 | ✓ |
| `fcn.0040794c` | `0x40794c` | 268 | ✓ |
| `fcn.00406f84` | `0x406f84` | 261 | ✓ |
| `fcn.00408a2c` | `0x408a2c` | 247 | ✓ |
| `fcn.00406251` | `0x406251` | 245 | ✓ |
| `fcn.00401ee0` | `0x401ee0` | 244 | ✓ |
| `fcn.00409254` | `0x409254` | 239 | ✓ |
| `fcn.004038b4` | `0x4038b4` | 238 | ✓ |
| `fcn.00409148` | `0x409148` | 238 | ✓ |
| `fcn.00408ba4` | `0x408ba4` | 234 | ✓ |
| `fcn.004019dc` | `0x4019dc` | 226 | ✓ |
| `fcn.004066a4` | `0x4066a4` | 219 | ✓ |
| `fcn.00409580` | `0x409580` | 216 | ✓ |
| `fcn.00409888` | `0x409888` | 211 | ✓ |
| `fcn.00406346` | `0x406346` | 209 | ✓ |
| `fcn.00407dfc` | `0x407dfc` | 195 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401768.c`](code/fcn.00401768.c)
- [`code/fcn.004019dc.c`](code/fcn.004019dc.c)
- [`code/fcn.00401ee0.c`](code/fcn.00401ee0.c)
- [`code/fcn.00401fd4.c`](code/fcn.00401fd4.c)
- [`code/fcn.0040215c.c`](code/fcn.0040215c.c)
- [`code/fcn.00402300.c`](code/fcn.00402300.c)
- [`code/fcn.004038b4.c`](code/fcn.004038b4.c)
- [`code/fcn.00403e41.c`](code/fcn.00403e41.c)
- [`code/fcn.00403f67.c`](code/fcn.00403f67.c)
- [`code/fcn.00404da8.c`](code/fcn.00404da8.c)
- [`code/fcn.00404eca.c`](code/fcn.00404eca.c)
- [`code/fcn.004051d0.c`](code/fcn.004051d0.c)
- [`code/fcn.00405314.c`](code/fcn.00405314.c)
- [`code/fcn.00405628.c`](code/fcn.00405628.c)
- [`code/fcn.00406251.c`](code/fcn.00406251.c)
- [`code/fcn.00406346.c`](code/fcn.00406346.c)
- [`code/fcn.004066a4.c`](code/fcn.004066a4.c)
- [`code/fcn.00406d70.c`](code/fcn.00406d70.c)
- [`code/fcn.00406f84.c`](code/fcn.00406f84.c)
- [`code/fcn.0040794c.c`](code/fcn.0040794c.c)
- [`code/fcn.00407dfc.c`](code/fcn.00407dfc.c)
- [`code/fcn.00408330.c`](code/fcn.00408330.c)
- [`code/fcn.00408a2c.c`](code/fcn.00408a2c.c)
- [`code/fcn.00408ba4.c`](code/fcn.00408ba4.c)
- [`code/fcn.00409148.c`](code/fcn.00409148.c)
- [`code/fcn.00409254.c`](code/fcn.00409254.c)
- [`code/fcn.00409580.c`](code/fcn.00409580.c)
- [`code/fcn.004096e8.c`](code/fcn.004096e8.c)
- [`code/fcn.00409888.c`](code/fcn.00409888.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is a technical analysis of the binary's behavior.

### Core Functionality and Purpose
The sample appears to be a **setup installer** or a wrapper for an executable, likely built using the **Inno Setup** engine (evidenced by several internal references like `InnoSetupLdrWindow` and specialized string formatting). 

Its primary role is to:
*   Initialize the environment by checking system locales (`GetSystemDefaultLCID`).
*   Manage and decompress internal resources (indicated by **LZMA decompression** strings).
*   Parse installation paths, handle command-line arguments, and perform file/folder creation.
*   Act as a "bootstrapper" or installer that ultimately launches the primary application via `CreateProcessA`.

### Suspicious or Malicious Behaviors
While the binary appears to be a standard installer at first glance, several functions exhibit behaviors common in malware droppers or loaders:

*   **Process Execution (Potential Dropper/Loader):** 
    The function `fcn.00409888` calls `CreateProcessA`. It takes a command line (likely constructed during the setup phase) and launches a new process, then enters a wait loop (`MsgWaitForMultipleObjects`) until that process terminates or returns an exit code. This is common in multi-stage malware where the installer downloads/extracts a payload and then executes it.
*   **File System Manipulation:** 
    Function `fcn.00409254` contains calls to `CreateDirectoryA`. While standard for installers, this is used to prepare the file system for the placement of files or the creation of "landing zones" for malicious payloads.
*   **Registry Interaction:** 
    Function `fcn.00406d70` interacts with the Windows Registry via `RegQueryValueExA`. It performs specific logic to check/validate registry keys. In a malicious context, this is often used to check for the presence of security software or to establish persistence (e.g., checking "Run" keys).
*   **Resource Extraction:** 
    The inclusion of LZMA decompression routines and `VirtualAlloc` calls in functions like `fcn.00407dfc` suggests that the binary may be extracting compressed data from its own resource section into memory or onto disk before execution.

### Notable Techniques & Patterns
*   **Inno Setup Framework:** The presence of specific strings (e.g., `InnoSetupLdrWindow`, `TCompressedBlockReader`) strongly indicates the use of a known installer framework. This is common in both legitimate software and "wrapped" malware to provide a professional-looking installation experience.
*   **LZMA Compression:** The reliance on LZMA suggests that the binary contains bundled resources that need decompression, a technique used by installers to package files and by packers/droppers to hide payloads.
*   **Wait Loops for Child Processes:** In `fcn.00409888`, the use of `MsgWaitForMultipleObjects` to wait for a child process is a standard way to ensure that an installer finishes its "work" (or a dropper hides its activity) before exiting.
*   **Localization/Environment Mapping:** The extensive loops in `fcn.004051d0` and others to resolve LCIDs suggest the binary is designed to work across various regional settings, ensuring maximum reach for the software it installs.

### Summary of Findings
The binary functions as an **installer wrapper**. It possesses the capabilities required to manipulate the file system, interact with the registry, and spawn child processes. While its behavior aligns with a legitimate installer (specifically using Inno Setup), its structure—unpacking data via LZMA and launching secondary processes—is identical to the behavior of a **malware dropper** used to deliver a primary payload in a staged attack.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of LZMA decompression and `VirtualAlloc` indicates that the binary is decompressing and potentially extracting payloads into memory to hide their true nature. |
| **T1082** | System Information Discovery | The use of `RegQueryValueExA` to check for security software and other registry keys is a method used to gather information about the system's defenses and environment. |
| **T1106** | Native API | The utilization of `CreateProcessA` and `VirtualAlloc` allows the binary to interact directly with the operating system to manage multi-stage execution and memory management for subsequent payloads. |
| **T1547** | Boot or Logon Autostar (General context) | While not explicitly a "creation" action, the analyst notes the registry checks are often used to verify/establish persistence in startup locations. |

***Note on Analytical Context:*** *The behavior described—an Inno Setup wrapper that uses decompression, memory allocation for staging, and subsequent process execution—is classic signature behavior for a **Dropper** or **Loader**. While "Dropper" is not a specific MITRE technique (it is an adversary tactic), the combination of T1027, T1082, and T1106 effectively maps the technical mechanisms used to achieve that role.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: As this sample appears to be an **Inno Setup** wrapper/installer, many of the technical artifacts relate to the installer framework rather than specific C2 infrastructure. No specific IP addresses, URLs, or unique file hashes were present in the provided data.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   **Note:** The strings contained standard Windows system paths (e.g., `\Control Panel\International`) and environment variables (`USERPROFILE`). These were excluded as they are considered false positives/standard system components. No specific malicious registry keys or unique file paths were identified.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Framework Identification:** Inno Setup (identified via `InnoSetupLdrWindow`, `TCompressedBlockReader`, and `TLZMADecompressor`).
*   **Compression Method:** LZMA (used for decompressing internal resources/payloads).
*   **Behavioral Pattern - Dropper/Loader logic:** 
    *   The use of `CreateProcessA` followed by `MsgWaitForMultipleObjects` indicates a multi-stage execution pattern where the installer waits for a secondary payload to execute.
    *   Use of `VirtualAlloc` and `VirtualProtect` in conjunction with LZMA decompression suggests "in-memory" unpacking of components.
*   **Behavioral Pattern - Registry/Environment Probing:** 
    *   Usage of `RegQueryValueExA` for environment checks.
    *   System locale resolution via `GetSystemDefaultLCID`.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

1. **Malware family**: custom 
2. **Malware type**: dropper
3. **Confidence**: High

**Key evidence**:
*   **Wrapper Functionality:** The sample utilizes the Inno Setup framework combined with LZMA decompression and `VirtualAlloc` to bundle, unpack, and potentially hide a primary payload within its own resources.
*   **Multi-stage Execution:** The use of `CreateProcessA` followed by `MsgWaitForMultipleObjects` is a classic indicator of a dropper or loader; it ensures the "installer" remains active until the secondary (malicious) payload has successfully launched.
*   **Evasion and Persistence Prep:** The inclusion of registry queries (`RegQueryValueExA`) and environment checks indicates the binary is preparing the system for the primary payload, checking for security software or establishing initial persistence requirements.
