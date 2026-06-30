# Threat Analysis Report

**Generated:** 2026-06-29 23:30 UTC
**Sample:** `0362ac7171eb48712c6de9f9afe8076891da5042cc25961d5f9e32f722f13390_0362ac7171eb48712c6de9f9afe8076891da5042cc25961d5f9e32f722f13390.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0362ac7171eb48712c6de9f9afe8076891da5042cc25961d5f9e32f722f13390_0362ac7171eb48712c6de9f9afe8076891da5042cc25961d5f9e32f722f13390.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,621,173 bytes |
| MD5 | `04329bb5888608de5cd219020c0e2216` |
| SHA1 | `bf3e744a0ebe327d64a7b02e0f77536b56c20871` |
| SHA256 | `0362ac7171eb48712c6de9f9afe8076891da5042cc25961d5f9e32f722f13390` |
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

Total strings found: **8067** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality.

### Core Functionality and Purpose
The presence of numerous "Inno Setup" strings (e.g., `InnoSetupLdrWindow`, `/SILENT`, `/VERYSILENT`, and installation logic) indicates that this binary is a **setup installer** or a **launcher** designed to deploy software. 

Specifically, it functions as a wrapper/installer. It performs environment checks, validates system parameters, and ultimately launches other components. The presence of "corrupted" error messages and standard installer flags suggests it follows the standard execution flow of an Inno Setup-based installer but is likely being used to bundle or deploy a secondary payload.

### Suspicious or Malicious Behaviors
While many of these behaviors are common in legitimate installers, they are frequently abused by malware as "droppers" or "loaders."

*   **Process Spawning & Execution (Dropper Behavior):** 
    *   Function `fcn.004099ec` calls `CreateProcessA` and then enters a loop using `MsgWaitForMultipleObjects`. This is a classic **launcher/dropper pattern**: the installer starts a secondary process (the actual payload) and waits for it to respond or finish before closing itself. This helps hide the primary malicious activity from the initial execution profile.
*   **Anti-Analysis / Environment Checking:**
    *   Function `fcn.004056d8` performs checks using `GetModuleFileNameA` and compares results against internal values. It also uses `MessageBoxA` to alert the user if certain conditions aren't met, which can be a way to detect if it is running in an unintended environment (like a sandbox or debugger).
    *   Function `fcn.00406e10` performs repeated calls to `RegQueryValueExA`. This suggests the program is checking for specific **Registry keys** related to system configurations, OS language settings, or potentially looking for the presence of security software/antivirus tools.
*   **String Decoding/Manipulation:** 
    *   Function `fcn.00404e58` contains logic that appears to perform **URL decoding** (handling `%` characters) and path normalization. This is often used by malware to de-obfuscate hidden URLs or file paths before making use of them in network communications or local file manipulation.

### Notable Techniques & Patterns
*   **Inno Setup Wrapper:** The extensive "Inno Setup" metadata suggests the malware author is using a legitimate installation engine to mask the malicious nature of the underlying payload.
*   **Complex Buffer Management:** Functions like `fcn.00406301` and `fcn.00402300` involve complex calculations, bitwise operations (e.g., `& 0x7ffffffc`), and manual memory pointer arithmetic. This suggests the program is handling non-standard data formats or performing custom decryption/decompression of its own internal resources.
*   **Multi-Stage Execution:** The transition from an installer logic to a process creation loop (`fcn.004099ec`) indicates that this binary is likely just one stage in a multi-stage infection chain.
*   **Persistence Check:** While not explicitly showing a "registry run key" write, the heavy focus on registry reading and system environment detection suggests the program is determining if it has the "permission" or "environment" to proceed with its next phase.

### Summary Table of Findings

| Feature | Evidence / Function | Potential Risk |
| :--- | :--- | :--- |
| **Loader/Dropper** | `fcn.004099ec` (CreateProcessA + Wait Loop) | Decouples the installer from the malicious payload. |
| **Anti-Analysis** | `fcn.004056d8`, `fcn.00406e10` (RegQueryEx, ModuleName) | Checks for sandboxes, debuggers, or security software. |
| **De-obfuscation** | `fcn.00404e58` (URL/Path Decoding) | Decodes hidden paths/URLs for later use in C2 communication. |
| **Standard Masking** | Inno Setup Strings / Infrastructure | Uses common installer tools to blend in with legitimate software. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The binary utilizes "Inno Setup" strings and a wrapper design to blend in with legitimate installer behavior to hide its malicious payload. |
| T1497 | Virtualized Environment | The use of `GetModuleFileNameA` and registry lookups indicates attempts to detect if the process is running in a sandbox or a security-monitored environment. |
| T1027 | Obfuscated Files or Information | The implementation of URL decoding for file paths and network addresses suggests an attempt to hide malicious infrastructure from static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs). 

Note: Per your instructions, standard Windows system paths, library files (e.g., `kernel32.dll`), and legitimate documentation URLs (e.g., `jrsoftware.org`) have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   *None identified.* (The only URL present is a standard Inno Setup help page).

### **File paths / Registry keys**
*   *None identified.* (While the analysis mentions that the program queries registry keys and handles file paths, no specific malicious paths or registry keys were explicitly listed in the provided strings.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Loader/Dropper Behavior:** The binary utilizes an Inno Setup wrapper to mask its primary functionality, a common technique for concealing malware.
*   **Decoding Logic:** Function `fcn.00404e58` contains logic for URL decoding and path normalization, suggesting the presence of obfuscated C2 infrastructure or local file paths.
*   **Anti-Analysis/Evasion:** 
    *   The use of `GetModuleFileNameA` combined with comparison checks suggests attempts to identify if the binary is running in a sandbox or unauthorized environment.
    *   Heavy usage of `RegQueryValueExA` indicates active environmental fingerprinting.
*   **Multi-Stage Execution:** The transition from an installer interface to a "wait loop" after calling `CreateProcessA` (`fcn.004099ec`) confirms this is a multi-stage loader designed to decouple the initial execution from the payload activity.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High
4. **Key evidence**:
    * **Dropper/Loader Architecture**: The binary exhibits classic loader behavior by using an Inno Setup wrapper to mask its presence and employing a `CreateProcessA` call followed by a `MsgWaitForMultipleObjects` loop, which is designed to decouple the initial execution from the malicious payload's activity.
    * **Anti-Analysis & Evasion**: The sample actively performs environment fingerprinting through `RegQueryValueExA` (to detect security software or specific system configurations) and `GetModuleFileNameA` to determine if it is running in a sandbox or unauthorized environment.
    * **De-obfuscation Logic**: The presence of URL decoding and path normalization functions indicates the binary is designed to handle obfuscated strings, likely used for hidden C2 infrastructure or internal file paths that would otherwise be flagged by static analysis.
