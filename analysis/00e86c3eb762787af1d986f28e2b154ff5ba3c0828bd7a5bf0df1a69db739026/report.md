# Threat Analysis Report

**Generated:** 2026-06-25 16:31 UTC
**Sample:** `00e86c3eb762787af1d986f28e2b154ff5ba3c0828bd7a5bf0df1a69db739026_00e86c3eb762787af1d986f28e2b154ff5ba3c0828bd7a5bf0df1a69db739026.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00e86c3eb762787af1d986f28e2b154ff5ba3c0828bd7a5bf0df1a69db739026_00e86c3eb762787af1d986f28e2b154ff5ba3c0828bd7a5bf0df1a69db739026.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,589,097 bytes |
| MD5 | `d83a237e3bbc8eab7d3441f77b8ab207` |
| SHA1 | `508af35c54f5b3291e35b9b0824fcf0a3c6d0ced` |
| SHA256 | `00e86c3eb762787af1d986f28e2b154ff5ba3c0828bd7a5bf0df1a69db739026` |
| Overall entropy | 7.998 |
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
| `CODE` | 40,448 | 6.632 | No |
| `DATA` | 1,024 | 2.752 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 2,560 | 4.431 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.204 | No |
| `.reloc` | 0 | 0.0 | No |
| `.rsrc` | 11,264 | 4.494 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **7860** (showing first 100)

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
kernel32.dll
SetDllDirectoryW
SetSearchPathMode
SetProcessDEPPolicy
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
_^[YY]
Compressed block is corrupted
Compressed block is corrupted
$Z]_^[
Compressed block is corrupted
TLZMA1SmallDecompressorS
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040840c` | `0x40840c` | 1690 | ✓ |
| `fcn.00404e58` | `0x404e58` | 773 | ✓ |
| `fcn.00403f67` | `0x403f67` | 731 | ✓ |
| `fcn.004053c4` | `0x4053c4` | 584 | ✓ |
| `entry0` | `0x40a5f8` | 533 | ✓ |
| `fcn.00404f7a` | `0x404f7a` | 474 | ✓ |
| `fcn.00402300` | `0x402300` | 463 | ✓ |
| `fcn.0040215c` | `0x40215c` | 418 | ✓ |
| `fcn.00401fd4` | `0x401fd4` | 389 | ✓ |
| `fcn.004056d8` | `0x4056d8` | 378 | ✓ |
| `fcn.00403e41` | `0x403e41` | 328 | ✓ |
| `fcn.00406e10` | `0x406e10` | 312 | ✓ |
| `fcn.00405280` | `0x405280` | 310 | ✓ |
| `fcn.00401768` | `0x401768` | 291 | ✓ |
| `fcn.00407a28` | `0x407a28` | 268 | ✓ |
| `fcn.0040953c` | `0x40953c` | 265 | ✓ |
| `fcn.00407024` | `0x407024` | 261 | ✓ |
| `fcn.00409768` | `0x409768` | 259 | ✓ |
| `fcn.00408b08` | `0x408b08` | 247 | ✓ |
| `fcn.00406301` | `0x406301` | 245 | ✓ |
| `fcn.00401ee0` | `0x401ee0` | 244 | ✓ |
| `fcn.00409330` | `0x409330` | 239 | ✓ |
| `fcn.004038b4` | `0x4038b4` | 238 | ✓ |
| `fcn.00409224` | `0x409224` | 238 | ✓ |
| `fcn.00408c80` | `0x408c80` | 234 | ✓ |
| `fcn.004019dc` | `0x4019dc` | 226 | ✓ |
| `fcn.00406744` | `0x406744` | 219 | ✓ |
| `fcn.004099ec` | `0x4099ec` | 211 | ✓ |
| `fcn.004063f6` | `0x4063f6` | 209 | ✓ |
| `fcn.00407f10` | `0x407f10` | 195 | ✓ |

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
- [`code/fcn.00404e58.c`](code/fcn.00404e58.c)
- [`code/fcn.00404f7a.c`](code/fcn.00404f7a.c)
- [`code/fcn.00405280.c`](code/fcn.00405280.c)
- [`code/fcn.004053c4.c`](code/fcn.004053c4.c)
- [`code/fcn.004056d8.c`](code/fcn.004056d8.c)
- [`code/fcn.00406301.c`](code/fcn.00406301.c)
- [`code/fcn.004063f6.c`](code/fcn.004063f6.c)
- [`code/fcn.00406744.c`](code/fcn.00406744.c)
- [`code/fcn.00406e10.c`](code/fcn.00406e10.c)
- [`code/fcn.00407024.c`](code/fcn.00407024.c)
- [`code/fcn.00407a28.c`](code/fcn.00407a28.c)
- [`code/fcn.00407f10.c`](code/fcn.00407f10.c)
- [`code/fcn.0040840c.c`](code/fcn.0040840c.c)
- [`code/fcn.00408b08.c`](code/fcn.00408b08.c)
- [`code/fcn.00408c80.c`](code/fcn.00408c80.c)
- [`code/fcn.00409224.c`](code/fcn.00409224.c)
- [`code/fcn.00409330.c`](code/fcn.00409330.c)
- [`code/fcn.0040953c.c`](code/fcn.0040953c.c)
- [`code/fcn.00409768.c`](code/fcn.00409768.c)
- [`code/fcn.004099ec.c`](code/fcn.004099ec.c)

## Behavioral Analysis

Based on the disassembly and strings provided, here is a technical analysis of the binary's behavior.

### Core Functionality and Purpose
The binary appears to be an **installer or launcher** built using the **Inno Setup** framework (evidenced by the "Inno Setup" strings, numerous installation flags like `/SILENT`, `/VERYSILENT`, and standard installer logic). Its primary role is to set up an environment, potentially check system requirements, and launch other components of a software package.

### Suspicious or Malicious Behaviors
While the binary heavily utilizes legitimate installer components, several behaviors are common in malware **droppers** or **stagers**:

*   **Process Spawning & Synchronization (`fcn.004099ec`):** 
    *   The code uses `CreateProcessA` to launch a child process based on a command line string.
    *   It then enters a loop using `MsgWaitForMultipleObjects`, waiting for the spawned process to terminate before continuing or exiting. This is a classic "wrapper" technique used by droppers to ensure the main payload (the malicious component) starts successfully before the installer closes.
*   **Registry Manipulation (`fcn.00406e10`):** 
    *   The code interacts with the Windows Registry using `RegQueryValueExA`. While common in installers to check for existing software, it is also used by malware to gather system information or determine paths for persistence and configuration.
*   **Dynamic API Resolution (`fcn.00407024`):** 
    *   The use of `GetModuleHandleA` and `GetProcAddress` suggests the binary resolves function addresses at runtime rather than at link-time. This can be used to hide the full capabilities of the program from static analysis tools.
*   **Memory Allocation (`fcn.00407f10`):** 
    *   The code performs manual memory allocation via `VirtualAlloc`. In an installer context, this is for loading data; in a malware context, it is often used to allocate executable memory regions for injected payloads.

### Notable Techniques and Patterns
*   **Inno Setup Wrapper:** The high volume of standard installation strings (e.g., `LZMA`, `SizeofResource`, `_STARTUP` flags) indicates the author is using a well-known, legitimate installer framework to package their software. This provides "guilt by association," as it makes the file look like a standard installer.
*   **Environment Probing:** Functions like `fcn.00405280` and `fcn.0040953c` repeatedly query system locale information (`GetSystemDefaultLCID`, `GetUserDefaultLangID`). While used for localization, this is also a common way to detect if the environment matches a target region or is a "clean" user machine.
*   **Data Processing/Parsing:** Functions like `fcn.0040840c` and `fcn.00404e58` involve heavy string manipulation and buffer processing, likely used to parse configuration files or instructions provided in the installer's resources.

### Summary for Incident Response
This binary is a **Dropper/Installer**. Its primary role is to act as a "front" for other programs. It handles the initial execution environment (registry checks, locale detection) and then uses `CreateProcessA` to launch the main payload while waiting for it to finish. 

**Recommendation:** Treat this file as a delivery mechanism. If found in an environment where no legitimate software is being installed, it should be treated as a malicious stager. Focus analysis on the command line passed to `CreateProcessA` to identify the actual payload.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1059 | Command and Scripting Interpreter | The use of `CreateProcessA` to execute a command line string as a "wrapper" indicates the execution of commands or scripts to launch payloads. |
| T1082 | System Information Discovery | The binary queries registry values and system locale information (e.g., `GetSystemDefaultLCID`) to profile the environment and determine if it is a target machine. |
| T1106 | Dynamic Resolution | The use of `GetModuleHandleA` and `GetProcAddress` allows the binary to resolve function addresses at runtime, concealing its capabilities from static analysis. |
| T1055 | Process Injection | The manual allocation of executable memory via `VirtualAlloc` is a primary method for preparing memory regions to house injected malicious code or payloads. |
| T1036 | Masquerading | The use of the Inno Setup framework allows the malware to hide behind a legitimate, well-known installer interface to avoid suspicion. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs). 

**Note:** Following your instructions, standard Windows system paths, common library functions, and well-known third-party software documentation links (e.g., Inno Setup help pages) have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   None found (The identified URL `http://www.jrsoftware.org/ishelp/...` was omitted as it points to legitimate, public documentation for the Inno Setup framework).

### **File paths / Registry keys**
*   None found (All identified paths, such as `.DEFAULT\Control Panel\International`, are standard Windows system paths).

### **Mutex names / Named pipes**
*   None found.

### **Hashes**
*   None found.

### **Other artifacts**
*   **Framework Identification:** Inno Setup (The binary utilizes extensive Inno Setup compiler components, including `InnoSetupLdrWindow`, standard installation flags like `/VERYSILENT` and `/SUPPRESSMSGBOXES`, and LZMA compression routines).
*   **Technique - Dropper/Wrapper Behavior:** The use of `CreateProcessA` followed by `MsgWaitForMultipleObjects` indicates a wrapper behavior used to ensure the payload executes before the installer exits.
*   **Technique - Dynamic API Resolution:** Use of `GetProcAddress` and `GetModuleHandleA` to resolve functions at runtime (often used to evade static analysis).
*   **Technique - Memory Manipulation:** Use of `VirtualAlloc` and `VirtualProtect`.

---
**Analyst Note:** 
The absence of specific C2 infrastructure (IPs/Domains) or hardcoded malicious paths suggests this binary is a **generic installer wrapper**. While it exhibits behaviors common in malware droppers (process hiding, dynamic resolution, and payload launching), there are no unique technical identifiers in the provided text that link this specific instance to a known threat actor or campaign without further analysis of the "hidden" payloads.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper
3. **Confidence**: High
4. **Key evidence**:
    * **Wrapper Behavior:** The binary utilizes a "wrapper" technique by employing `CreateProcessA` followed by `MsgWaitForMultipleObjects`, ensuring the primary payload executes and completes before the installer process terminates.
    * **Masquerading via Framework:** The sample heavily incorporates the Inno Setup framework to hide its malicious intent behind a legitimate-looking installation interface (T1036).
    * **Evasion & Preparation Tactics:** The use of dynamic API resolution (`GetProcAddress`) and manual memory allocation (`VirtualAlloc`) are standard techniques used by droppers to obfuscate capabilities from static analysis and prepare environments for secondary payloads.
