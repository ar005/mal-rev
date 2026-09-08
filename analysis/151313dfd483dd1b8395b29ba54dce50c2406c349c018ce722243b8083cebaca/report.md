# Threat Analysis Report

**Generated:** 2026-09-06 18:45 UTC
**Sample:** `151313dfd483dd1b8395b29ba54dce50c2406c349c018ce722243b8083cebaca_151313dfd483dd1b8395b29ba54dce50c2406c349c018ce722243b8083cebaca.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `151313dfd483dd1b8395b29ba54dce50c2406c349c018ce722243b8083cebaca_151313dfd483dd1b8395b29ba54dce50c2406c349c018ce722243b8083cebaca.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,760,121 bytes |
| MD5 | `728dbac863ad3360901e75782f5044a2` |
| SHA1 | `8e40a9ae5f00614183f16063c2bbcf1760e08807` |
| SHA256 | `151313dfd483dd1b8395b29ba54dce50c2406c349c018ce722243b8083cebaca` |
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
| `.rsrc` | 11,264 | 4.537 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **8322** (showing first 100)

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

### Analysis Summary
The binary is an **installer executable** created using the **Inno Setup** framework. While it contains standard installer behaviors (such as resource extraction, localization, and registry interaction), certain characteristics of its execution logic could also be associated with a "dropper" or "loader" functionality common in malicious software.

### Core Functionality and Purpose
*   **Installer Framework:** The extensive string presence of "InnoSetup," including options like `/SILENT`, `/VERYSILENT`, and references to `.lzma` decompression, indicates the primary purpose is installing a program.
*   **Resource Management:** The code includes routines for handling compressed data (LZMA) and extracting resources from within the binary's internal files.
*   **System Localization:** It actively checks the system locale (`GetSystemDefaultLCID`, `GetUserDefaultLangID`) to provide a localized experience, which is standard but necessary for valid software.
*   **Process Orchestration:** The function `fcn.004099ec` demonstrates the ability to construct a command line and launch a secondary process using `CreateProcessA`. It then enters a loop to wait for that process to complete (`MsgWaitForMultipleObjects`), a common pattern in installers during the "Launching application..." phase.

### Suspicious or Malicious Behaviors
*   **Potential Dropper/Loader Logic:** The combination of `VirtualAlloc`, `GetProcAddress` usage, and the execution of secondary processes via `CreateProcessA` (in `fcn.004099ec`) are common in multi-stage malware. In a legitimate installer, this is used to launch the installed app; in malware, it is used to drop and execute a payload or "stub."
*   **Resource Extraction:** The presence of LZMA decoding routines suggests that the binary carries compressed payloads within its own resource section, which may be unpacked into temporary directories before execution.

### Notable Techniques and Patterns
*   **Dynamic API Resolution:** The use of `GetProcAddress` (in `fcn.00407024`) indicates that some functions are not resolved at link-time but at runtime. While common in large installers to minimize imports, it can also be used to hide the true capabilities of a binary from basic static analysis.
*   **Registry Interaction:** The code includes routines to query registry keys (`RegQueryValueExA`). This is typically used to check for existing software or system configurations but can also be used by malware for persistence or environment checking.
*   **Memory Management:** Several functions handle internal data structures and memory allocation (e.g., `fcn.00401fd4` and `fcn.00407f10`). These ensure that the installer has enough space to process strings, paths, and file system information during the installation process.
*   **Internal String/Data Parsing:** Functions like `fcn.0040840c` and `fcn.00406301` are heavy-duty string processing routines (likely used for converting raw data into displayable strings or handling path conversions), which is necessary for complex installation scripts.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of LZMA compression and internal resource extraction indicates a method for bundling and potentially concealing payloads within the binary. |
| **T1112** | Modify Registry | The use of `RegQueryValueExA` identifies interaction with the Windows registry to check system configurations or environment settings. |
| **T1059** | Command and Scripting Interpreter | The construction of a command line followed by the execution of `CreateProcessA` is indicative of orchestrating the execution of secondary components or scripts. |
| **T1036** | Masquerading | The use of an Inno Setup framework allows the binary to masquerade as a legitimate installer while potentially functioning as a dropper for malicious payloads. |

***

**Analyst Note:** 
While the behavior is consistent with a standard installer, the specific combination of **T1027** (hidden resources), **T1036** (masking as an installer), and the use of `GetProcAddress` to hide API imports are common indicators used by threat actors to create multi-stage droppers that evade basic static analysis.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline` (Note: This is a standard link associated with the Inno Setup installer framework).

**File paths / Registry keys**
*   None identified. (Note: Path strings like `.DEFAULT\Control Panel\International` and `Control Panel\Desktop\ResourceLocale` were excluded as they are standard Windows system paths).

**Mutex names / Named pipes**
*   None found.

**Hashes**
*   None found.

**Other artifacts**
*   **Framework:** Inno Setup (Versions 5.5.0 and 5.5.3)
*   **Techniques Observed:** 
    *   **Dynamic API Resolution:** Usage of `GetProcAddress` to resolve functions at runtime.
    *   **Resource Extraction:** Implementation of LZMA decompression routines for internal payload extraction.
    *   **Process Manipulation:** Use of `CreateProcessA` and `MsgWaitForMultipleObjects` to manage child processes (common in both installers and droppers).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`
- `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: Medium

**Key evidence**:
*   **Dual-Purpose Behavior:** The sample utilizes the Inno Setup framework, which is a common technique for "Masquerading" (MITRE T1036). While these are legitimate installers, they are frequently used as wrappers to hide malicious payloads from static analysis.
*   **Obfuscation and Extraction Tactics:** The use of LZMA decompression, `GetProcAddress` for dynamic API resolution, and internal resource extraction indicates a multi-stage execution logic typical of droppers meant to unpack a secondary payload.
*   **Process Orchestration:** The combination of `CreateProcessA` and `MsgWaitForMultipleObjects` in the analysis shows that the binary is designed to launch and manage child processes, a core functionality for loaders transitioning from an initial stage to an active payload.
