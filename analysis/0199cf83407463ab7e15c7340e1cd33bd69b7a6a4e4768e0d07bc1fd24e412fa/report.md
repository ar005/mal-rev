# Threat Analysis Report

**Generated:** 2026-06-27 05:03 UTC
**Sample:** `0199cf83407463ab7e15c7340e1cd33bd69b7a6a4e4768e0d07bc1fd24e412fa_0199cf83407463ab7e15c7340e1cd33bd69b7a6a4e4768e0d07bc1fd24e412fa.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0199cf83407463ab7e15c7340e1cd33bd69b7a6a4e4768e0d07bc1fd24e412fa_0199cf83407463ab7e15c7340e1cd33bd69b7a6a4e4768e0d07bc1fd24e412fa.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,654,203 bytes |
| MD5 | `4bce138970d72c25c7b06d608b7d761a` |
| SHA1 | `cf4e5a3cf58bce47f21119aa26f963814b9f3634` |
| SHA256 | `0199cf83407463ab7e15c7340e1cd33bd69b7a6a4e4768e0d07bc1fd24e412fa` |
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
| `.rsrc` | 11,264 | 4.539 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **8112** (showing first 100)

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

Based on the provided disassembly and strings, here is a summary of the findings:

### Core Functionality and Purpose
The binary appears to be an **installer or loader wrapper**, likely utilizing the **Inno Setup** engine (indicated by the extensive "Inno Setup" related strings and standard setup parameters like `/SILENT`, `/DIR`, etc.). Its primary purpose is to prepare, unpack, and launch another application. 

The inclusion of LZMA decompression strings suggests that the binary contains an embedded payload which it decompresses into memory or onto disk before execution. It performs various system environment checks (such as locale settings via `GetSystemDefaultLCID` and registry lookups) to ensure compatibility before launching a secondary process.

### Suspicious or Malicious Behaviors
While this behavior is common in legitimate installers, these specific patterns are frequently observed in **Droppers** and **Downloader** malware:

*   **Process Execution (Potential Dropper Behavior):** Function `fcn.004099ec` is a clear implementation of process creation using `CreateProcessA`. It takes a command line argument, launches a new process, waits for it to finish (`MsgWaitForMultipleObjects`), and retrieves its exit code. This is the standard way a "wrapper" launches the actual payload (or an installer for that payload).
*   **Registry Interaction:** Function `fcn.00406e10` performs multiple calls to `RegQueryValueExA`. It iterates through registry keys to check for values, handling various errors and buffer sizes. This is used to find system information or verify if the "software" has been previously installed/run (common in checking for persistence).
*   **Payload Decompression:** The presence of strings like `LZMA1SmallDecompressorS` and `"Compressed block is corrupted"` strongly indicates that the binary contains a compressed payload. This multi-stage approach is common in malware to hide the primary malicious payload from simple static analysis.
*   **Environment/Locale Checking:** Functions like `fcn.00405280` and `f.0040953c` verify the system's locale and character set. This ensures that subsequent strings or logic are handled correctly for the specific Windows region.

### Notable Techniques or Patterns
*   **Inno Setup Wrapper:** The binary mimics a standard installer to blend in with legitimate software updates or "fake" installers.
*   **Buffer Management/Memory Allocation:** Function `fcn.00407f10` uses `VirtualAlloc` and performs manual checks on memory sizes before allocation, which is consistent with handling decompressed data buffers.
*   **Wait-on-Process Loop:** In `fcn.004099ec`, the use of a loop to wait for the child process (`MsgWaitForMultipleObjects`) ensures that the wrapper remains active until the payload has finished its initial execution sequence, which can be used to mask startup activity from certain monitoring tools.
*   **String Processing:** Function `fcn.00404e58` shows logic for handling file paths (looking for `%`, `-`, and `.`), likely ensuring that the final path of a decompressed payload is correctly formatted before being passed to the execution engine.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Packed_Data | The use of LZMA decompression and a "loader wrapper" structure indicates the primary payload is hidden within compressed data to evade detection. |
| T1036 | Masquerading | The binary mimics standard Inno Setup behavior and parameters (e.g., `/SILENT`) to blend in with legitimate software installation processes. |
| T1112 | System Information Discovery | The repeated use of `RegQueryValueExA` suggests the intent to gather system information or determine the environment status before execution. |
| T1484 | System Profile Discovery | Specific checks for locale settings and character sets are used to verify system properties and ensure compatibility with the target environment. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** Many items found in the raw strings (such as standard Windows registry paths and Inno Setup configuration flags) have been excluded as they are common to legitimate software and do not constitute malicious indicators in this context.

### **IP addresses / URLs / Domains**
*   *None detected.* (The URL `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline` is a standard help link for the Inno Setup utility and is not considered a malicious C2 or phishing link).

### **File paths / Registry keys**
*   *None detected.* (The paths `Control Panel\Desktop\ResourceLocale` and `.DEFAULT\Control Panel\International` are standard Windows system paths).

### **Mutex names / Named pipes**
*   *None detected.*

### **Hashes**
*   *None detected.*

### **Other artifacts**
*   **Inno Setup Framework:** The presence of strings such as `InnoSetupLdrWindow`, `/SILENT`, `/VERYSILENT`, `/SUPPRESSMSGBOXES`, and `/LOG` indicates the binary uses the Inno Setup installer engine. This is common in both legitimate software and malware (used as a wrapper).
*   **LZMA Decompression:** The strings `LZMA1SmallDecompressorS` and `lzmadecompsmall` indicate the inclusion of an LZMA decompression library, often used by wrappers to unpack secondary payloads.
*   **Execution Logic Flags:** Presence of common installation flags (e.g., `/DIR`, `/RESTART`, `/SKIP_UNINSTALL`) confirms a standard installer wrapper structure.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-stage Loading & Decompression:** The presence of LZMA decompression libraries and the "loader wrapper" architecture indicates the binary is designed to unpack and hide a secondary, potentially more malicious payload from static analysis (T1027).
*   **Masquerading via Inno Setup:** The use of standard installer strings (e.g., `/SILENT`, `InnoSetupLdrWindow`) serves as a common technique to blend in with legitimate software installations while delivering the actual payload.
*   **Process Execution Wrapper:** The implementation of `CreateProcessA` followed by `MsgWaitForMultipleObjects` confirms its role as an intermediary "wrapper" that manages the lifecycle of a secondary executable.
