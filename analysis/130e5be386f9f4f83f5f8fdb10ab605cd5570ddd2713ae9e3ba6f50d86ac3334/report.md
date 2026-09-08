# Threat Analysis Report

**Generated:** 2026-09-02 08:42 UTC
**Sample:** `130e5be386f9f4f83f5f8fdb10ab605cd5570ddd2713ae9e3ba6f50d86ac3334_130e5be386f9f4f83f5f8fdb10ab605cd5570ddd2713ae9e3ba6f50d86ac3334.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `130e5be386f9f4f83f5f8fdb10ab605cd5570ddd2713ae9e3ba6f50d86ac3334_130e5be386f9f4f83f5f8fdb10ab605cd5570ddd2713ae9e3ba6f50d86ac3334.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,905,384 bytes |
| MD5 | `aaa0261b336118665d110bfe48d9f848` |
| SHA1 | `cf51de2c4d0b40ef316902931504cc280a9e877f` |
| SHA256 | `130e5be386f9f4f83f5f8fdb10ab605cd5570ddd2713ae9e3ba6f50d86ac3334` |
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
| `CODE` | 37,888 | 6.561 | No |
| `DATA` | 1,024 | 2.739 | No |
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

Total strings found: **8436** (showing first 100)

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
| `fcn.00404e48` | `0x404e48` | 773 | ✓ |
| `fcn.00403f67` | `0x403f67` | 731 | ✓ |
| `fcn.004053b4` | `0x4053b4` | 584 | ✓ |
| `entry0` | `0x409c40` | 512 | ✓ |
| `fcn.00404f6a` | `0x404f6a` | 474 | ✓ |
| `fcn.00402300` | `0x402300` | 463 | ✓ |
| `fcn.0040215c` | `0x40215c` | 418 | ✓ |
| `fcn.00401fd4` | `0x401fd4` | 389 | ✓ |
| `fcn.004056c8` | `0x4056c8` | 378 | ✓ |
| `fcn.00403e41` | `0x403e41` | 328 | ✓ |
| `fcn.00406e10` | `0x406e10` | 312 | ✓ |
| `fcn.00405270` | `0x405270` | 310 | ✓ |
| `fcn.00401768` | `0x401768` | 291 | ✓ |
| `fcn.00407a28` | `0x407a28` | 268 | ✓ |
| `fcn.0040953c` | `0x40953c` | 265 | ✓ |
| `fcn.00407024` | `0x407024` | 261 | ✓ |
| `fcn.00408b08` | `0x408b08` | 247 | ✓ |
| `fcn.004062f1` | `0x4062f1` | 245 | ✓ |
| `fcn.00401ee0` | `0x401ee0` | 244 | ✓ |
| `fcn.00409330` | `0x409330` | 239 | ✓ |
| `fcn.004038b4` | `0x4038b4` | 238 | ✓ |
| `fcn.00409224` | `0x409224` | 238 | ✓ |
| `fcn.00408c80` | `0x408c80` | 234 | ✓ |
| `fcn.004019dc` | `0x4019dc` | 226 | ✓ |
| `fcn.00406744` | `0x406744` | 219 | ✓ |
| `fcn.00409768` | `0x409768` | 216 | ✓ |
| `fcn.004099a4` | `0x4099a4` | 211 | ✓ |
| `fcn.004063e6` | `0x4063e6` | 209 | ✓ |
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
- [`code/fcn.00404e48.c`](code/fcn.00404e48.c)
- [`code/fcn.00404f6a.c`](code/fcn.00404f6a.c)
- [`code/fcn.00405270.c`](code/fcn.00405270.c)
- [`code/fcn.004053b4.c`](code/fcn.004053b4.c)
- [`code/fcn.004056c8.c`](code/fcn.004056c8.c)
- [`code/fcn.004062f1.c`](code/fcn.004062f1.c)
- [`code/fcn.004063e6.c`](code/fcn.004063e6.c)
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
- [`code/fcn.004099a4.c`](code/fcn.004099a4.c)

## Behavioral Analysis

### Analysis Summary
Based on the provided disassembly and strings, this binary functions as an **installer or "wrapper"** utility. While its primary purpose appears to be preparing a system for a software installation (likely using the Inno Setup framework), these components are frequently utilized by malware as a **dropper/downloader** to unpack and execute a malicious payload while hiding the original malware's presence behind a legitimate-looking setup routine.

### Core Functionality
The code focuses on environment preparation, path construction, and process management:
*   **Environment Detection:** The binary contains extensive logic for checking system localization (LCID), default languages, and active codes pages (`GetSystemDefaultLCID`, `GetUserDefaultLangID`). This is used to determine the correct configuration for the installation.
*   **Data Parsing & Transformation:** Functions like `fcn.004063e6` and `fcn.00404e48` suggest heavy manipulation of strings, likely converting internal data or offsets into valid file paths or system commands (handling characters like `%`, `.`, and `-`).
*   **Resource Management:** The code includes several memory management routines (`fcn.00401fd4`, `fcn.0040215c`) to handle dynamically allocated buffers for data processing.

### Suspicious or Malicious Behaviors
While the binary may not be a "malware-in-itself" (it might just be an installer), it exhibits several behaviors common in **droppers** and **installers used in malware campaigns**:

*   **Process Spawning (Dropper Behavior):** 
    *   The function `fcn.004099a4` explicitly calls `CreateProcessA`. It takes a dynamically constructed command line (`fcn.00403414()`), launches a new process, and then uses `MsgWaitForMultipleObjects` to wait for that process to finish. 
    *   **Malware Context:** This is a classic technique to "drop" and execute an executable (the payload) while the current process handles the heavy lifting of extraction/unpacking.
*   **Registry Interaction:** 
    *   The function `fcn.00406e10` uses `RegQueryValueExA` to query specific registry values. While common in installers for finding paths, it is also used by malware to check for the presence of security software or to determine system privileges.
*   **Dynamic API Resolution:** 
    *   The usage of `GetProcAddress` and `GetModuleHandleA` (found in `fcn.00407024`) suggests that the program resolves certain functions at runtime rather than linking them statically. This is often done to evade static analysis or because the functionality depends on external components not present at compile-time.
*   **Complex String Decoding/Formatting:** 
    *   The extensive loops and logic in `fcn.0040840c` suggest that some part of the application's configuration or payload path is "packed" or requires complex decoding before it can be used by the OS, which helps hide the final destination of the files on disk from simple string scanners.

### Notable Techniques and Patterns
*   **Inno Setup Wrapper:** The presence of `InnoSetupLdrWindow` and numerous "Setup" related strings indicates this binary is likely a standard installer produced by Inno Setup. Malware authors frequently use these because they are widely trusted and often bypassed by basic heuristics.
*   **Wait-for-Process Loop:** The logic in `fcn.004099a4` ensures the "launcher" (this code) stays active until the launched process finishes. This is used to ensure that a malicious payload has successfully initialized before the installer closes itself.
*   **LZMA Compression:** The string references to `TLZMA1SmallDecompressorS` indicate the binary handles compressed data, often used in installers to pack large amounts of content into a small installer file.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1204** | User Execution | The binary functions as a dropper by utilizing `CreateProcessA` and a wait loop to execute a secondary payload. |
| **T1112** | System Information Discovery | The use of `RegQueryValueExA` is employed to gather system details, such as paths and the presence of security software. |
| **T1027** | Obfuscated Files or Information | Dynamic API resolution (`GetProcAddress`) and complex string decoding are used to hide functionality from static analysis tools. |
| **T1036** | Masquerading | The use of an Inno Setup wrapper allows the malicious activity to hide behind a common, trusted installation framework. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the identified Indicators of Compromise (IOCs) categorized by your requirements:

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   *Note: The registry keys found in the strings (`.DEFAULT\Control Panel\International` and `Control Panel\Desktop\ResourceLocale`) are standard Windows system paths/keys and have been excluded per your instructions.*

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Framework Identification:** Inno Setup (specifically version 5.5.0). This indicates the malware utilizes a common installer wrapper to hide its functionality and bypass basic heuristics.
*   **Compression Method:** LZMA (evidenced by `TLZMA1SmallDecompressorS`). This is used for packing data or payload components within the binary.
*   **Behavioral Indicators:** 
    *   **Process Spawning Routine:** The use of `CreateProcessA` combined with `MsgWaitForMultipleObjects` to wait for a child process is a specific pattern identifying "dropper" behavior.
    *   **Dynamic API Resolution:** Use of `GetProcAddress` and `GetModuleHandleA` indicates attempts to bypass static analysis or hide functionality from simple IAT (Import Address Table) scans.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High (regarding its function as a loader/dropper)
4. **Key evidence**:
    *   **Drop and Wait Behavior:** The use of `CreateProcessA` combined with `MsgWaitForMultipleObjects` is a classic "drop" pattern where the installer stays active until the malicious payload has successfully initialized.
    *   **Evasion Techniques:** The implementation of dynamic API resolution (`GetProcAddress`/`GetModuleHandleA`) and complex string decoding are intentional tactics to bypass static analysis and hide the final destination of payloads.
    *   **Masquerading via Inno Setup:** The utilization of a legitimate installer framework (Inno Setup) allows the malware to blend in with normal software installation processes while it decodes and executes hidden components.
