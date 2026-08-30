# Threat Analysis Report

**Generated:** 2026-08-23 22:09 UTC
**Sample:** `11c3fc0e9d2d137e21e157d13ac140d221b2a5f8077f0e4843ae2b62cc91a420_11c3fc0e9d2d137e21e157d13ac140d221b2a5f8077f0e4843ae2b62cc91a420.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11c3fc0e9d2d137e21e157d13ac140d221b2a5f8077f0e4843ae2b62cc91a420_11c3fc0e9d2d137e21e157d13ac140d221b2a5f8077f0e4843ae2b62cc91a420.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,461,377 bytes |
| MD5 | `130e60b7b3f3252da63aa2c3973352ee` |
| SHA1 | `d7e42a5ddbcd67764ba28bba99f984589e07139f` |
| SHA256 | `11c3fc0e9d2d137e21e157d13ac140d221b2a5f8077f0e4843ae2b62cc91a420` |
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
| `.rsrc` | 11,264 | 4.492 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **7620** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality:

### Core Functionality
The binary appears to be a **multi-stage installer or a "dropper" executable**. The presence of numerous Inno Setup configuration strings (e.g., `/SILENT`, `/VERYSILENT`, `InnoSetupLdrWindow`) and LZMA decompression routines indicates that this is likely an installer stub designed to extract, configure, and execute subsequent components.

### Suspicious or Malicious Behaviors
While the code contains many features common in legitimate software installers (like Inno Setup), several patterns are highly indicative of "loader" or "dropper" functionality often seen in malware:

*   **Process Spawning & Execution (`fcn.004099ec`):** This function is a classic example of an execution wrapper. It retrieves the command line, calls `CreateProcessA`, and enters a loop using `MsgWaitForMultipleObjects`. This is used to launch a child process (the "payload") while monitoring its exit code. In a malware context, this is how a "dropper" launches the actual malicious payload after extracting it from a compressed resource.
*   **Memory Manipulation (`fcn.00407f10`):** This function calls `VirtualAlloc`. It performs checks on memory sizes and allocates space that may be intended to house decompressed code or data before execution. The use of "padding" or complex logic around the allocation suggests it might be preparing a region for dynamic code execution (e.g., an unpacked PE file).
*   **Resource Decompression (`LZMA` routines):** The presence of `TLZMA1SmallDecompressorS` indicates that the binary contains compressed data. In malware, this is typically used to hide the primary malicious payload until it is unpacked into memory or onto the disk at runtime.
*   **File System Manipulation (`fcn.00409330`):** This function handles `CreateDirectoryA`. It includes logic to ensure directories exist before continuing. While common in installers, this is a prerequisite step for "dropping" files into specific folders (e.g., `AppData` or `Temp`).
*   **Registry Interaction (`fcn.00406e10`):** This function queries the Windows Registry via `RegQueryValueExA`. It checks for specific keys and values to determine the environment state. In malware, this is often used to check for previous infections, identify security software, or retrieve configuration settings for the next stage of the attack.

### Notable Techniques and Patterns
*   **Inno Setup Wrapper:** The extensive use of Inno Setup-style strings suggests the primary "payload" is likely tucked inside an installer script. This provides a layer of legitimacy as it mimics a standard setup routine to bypass basic heuristic filters.
*   **Dynamic Loading / Indirection:** Function `fcn.00407a28` shows highly complex, nested pointer arithmetic and indirect calls (e.g., `(**(*in_ECX + 8))()`). This is often used to implement a "virtual" table of functions or to obfuscate the control flow, making it harder for automated tools to follow the logic path.
*   **String/Path Processing:** Function `fcn.00404e58` appears to parse complex strings involving symbols like `%`, `&`, and `-`. This is typical for processing paths that may contain environment variables or special characters, common in installers but also useful for dynamically constructing malicious paths.
*   **Localization Logic:** The code includes extensive calls to `GetSystemDefaultLCID` and related logic (e.g., `fcn.00405280`), which ensures the installer behaves correctly across different language locales—a standard feature that can be used by attackers to ensure their malware doesn't crash on a victim's localized OS.

### Summary for Incident Response
The binary is likely a **dropper**. It is designed to:
1.  **Decompress** internal data (via LZMA).
2.  **Prepare the environment** (creating directories and checking registry keys).
3.  **Launch an additional payload** (using `CreateProcessA` in a wrapper that hides the transition from the initial loader).

If this is part of a malware campaign, the "true" malicious logic likely resides in the child process launched by `fcn.004099ec`.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Executables | The use of LZMA decompression to hide payload data and complex pointer arithmetic/indirection to obfuscate control flow are clear indicators of this technique. |
| **T1055.001** | Process Injection (Core) | The use of `VirtualAlloc` to prepare memory space for decompressed code or data before execution is a primary step in the injection and loading process. |
| **T1112** | Modify Registry | The use of `RegQueryValueExA` to query registry keys allows the malware to perform environment checks, identify security software, or retrieve configuration. |
| **T1105** | Ingress Tool Transfer | The logic surrounding `CreateDirectoryA` and path processing for "dropping" files into specific folders is characteristic of dropper behavior. |
| **T1036** | Dynamic Resolution | The use of nested pointer arithmetic and indirect calls to navigate a function table suggests the binary avoids static import tables to hide its API calls. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.* (Note: The URL `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline` was identified but excluded as it is a standard documentation link for the Inno Setup framework).

**File paths / Registry keys**
*   *None.* (The strings `.DEFAULT\Control Panel\International` and `Control Panel\Desktop\ResourceLocale` were identified but excluded as they are standard Windows system paths).

**Mutex names / Named pipes**
*   *None detected.*

**Hashes**
*   *None detected.*

**Other artifacts**
*   **Deployment Framework:** Inno Setup (The binary utilizes heavy Inno Setup components to mask its primary purpose as a "dropper").
*   **Compression Algorithm:** LZMA (Specifically `TLZMA1SmallDecompressorS`, used to unpack the hidden payload).
*   **Malware Behavior Patterns:** 
    *   **Dropper/Loader Logic:** The binary is designed to decompress and launch a secondary, separate process using `CreateProcessA`.
    *   **Evasion Technique:** Use of an "installer" wrapper to mimic legitimate software setup routines.
    *   **Persistence/Discovery Prep:** Presence of calls to `RegQueryValueExA` to check system environment conditions prior to execution.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`
- `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline`

---

## Malware Family Classification

1. **Malware family**: custom (Inno Setup wrapper)
2. **Malware type**: dropper
3. **Confidence**: High

4. **Key evidence**:
* **Wrapper/Stealth Technique:** The binary utilizes the Inno Setup framework as a "mask" to mimic a legitimate software installer while utilizing LZMA decompression to hide a secondary payload within its resources.
* **Execution Logic:** The presence of `fcn.004099ec` (an execution wrapper) and `CreateProcessA` indicates the binary's primary role is to extract, prepare, and launch a secondary malicious payload while monitoring its status.
* **Evasion and Obfuscation:** The use of complex pointer arithmetic for indirect function calls and dynamic memory allocation (`VirtualAlloc`) for decompressed code suggests a sophisticated attempt to bypass static analysis and hide the transition between the loader and the final payload.
