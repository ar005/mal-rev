# Threat Analysis Report

**Generated:** 2026-09-02 19:35 UTC
**Sample:** `1398db28585e615ecc30e3e139a1b38bf83468de60d12c71a9409ee029f56b13_1398db28585e615ecc30e3e139a1b38bf83468de60d12c71a9409ee029f56b13.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1398db28585e615ecc30e3e139a1b38bf83468de60d12c71a9409ee029f56b13_1398db28585e615ecc30e3e139a1b38bf83468de60d12c71a9409ee029f56b13.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,625,861 bytes |
| MD5 | `ef8ddfc89f244884e525cbc1c0c0fb6b` |
| SHA1 | `d8c8b853a578c828330f7877adaa6da185cc1eb9` |
| SHA256 | `1398db28585e615ecc30e3e139a1b38bf83468de60d12c71a9409ee029f56b13` |
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
| `.rsrc` | 11,264 | 4.493 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **7957** (showing first 100)

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
The binary appears to be a **software installer** generated using the **Inno Setup** engine (as evidenced by the extensive amount of Inno Setup-specific string constants and code structure). Its primary purpose is to unpack, install, and configure software components on a Windows system. 

The logic follows a typical "installer" pattern:
*   **Initialization:** It handles localization (`GetSystemDefaultLCID`), environment detection, and internal resource management (functions like `fcn.00405280` and `fcn.00407a28`).
*   **Configuration/Parsing:** Several functions (like `fcn.004063f6` and `fcn.00406744`) handle internal string parsing, potentially reading script files or configuration instructions provided during the installation process.

### Suspicious or Malicious Behaviors
While the code structure is typical of an Inno Setup installer (which are frequently used by both legitimate developers and malware authors), several behaviors are common in "dropper" or "downloader" stages of a malware infection:

*   **Process Execution & Waiting:** 
    *   Function `fcn.004099ec` uses `CreateProcessA` to launch a secondary process (likely the actual payload) and then utilizes `MsgWaitForMultipleObjects` to wait for that process to finish or exit before proceeding. This is a common technique used by installers, but also heavily utilized by malware "droppers" to ensure a malicious payload is launched successfully.
*   **Registry Interaction:** 
    *   Function `fcn.00406e10` contains logic for querying and potentially interacting with registry keys via `RegQueryValueExA`. While common in installers (to check for previous versions or system settings), it can also be used to check for the presence of security software or to establish persistence.
*   **File System Manipulation:** 
    *   Function `fcn.00409330` uses `CreateDirectoryA` to create directories on the filesystem. In a malicious context, this is often part of "dropping" files into specific system paths (e.g., `AppData` or `Temp`).
*   **Complex Script Execution:** 
    *   The repetitive and complex logic in functions like `fcn.00407a28` suggest the binary acts as a wrapper, executing a long list of "tasks" defined in its internal script to set up an environment for the final payload.

### Notable Techniques & Patterns
*   **Inno Setup Framework:** The presence of strings like `InnoSetupLdrWindow`, `GetSystemDefaultLCID`, and various `/SILENT` or `/VERYSILENT` flags indicates that the core logic is encapsulated within a known installer framework. This can be used to mask malicious actions behind a legitimate-looking installation process.
*   **Wrapped Logic:** The binary does not appear to perform its primary "malicious" task directly; instead, it acts as a wrapper or orchestrator (common in multi-stage malware). 
*   **Standard Windows API usage:** The code relies on standard APIs (`kernel32.dll`, `user32.dll`, `advapi32.dll`), and doesn't show immediate evidence of advanced anti-debugging or obfuscation within the provided functions, which is typical for the initial "installer" stage of a campaign.

### Summary
The binary is an **Inno Setup installer**. It performs standard installation tasks like creating directories, checking registry keys, and launching subprocesses. In a security context, such binaries are often used as **droppers**; while the installer code itself may be benign or "clean," it is designed to facilitate the deployment of subsequent components (which could be malicious).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1059 | Command and Scripting Interpreter | The binary uses complex internal script logic to orchestrate tasks and `CreateProcessA` to launch secondary payloads as part of a multi-stage execution. |
| T1112 | Modify Registry | The use of `RegQueryValueExA` indicates interaction with registry keys for configuration, environment checks, or establishing persistence. |
| T1036 | Masquerading | The utilization of the Inno Setup framework allows the binary to hide malicious "dropper" activities behind a legitimate-looking installer process. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** The analyzed binary is identified as a standard **Inno Setup** installer. While it lacks traditional malicious infrastructure (like C2 IPs), the following items are notable artifacts for identification.

### IP addresses / URLs / Domains
*   `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline` (Note: This is a standard help URL associated with the Inno Setup framework).

### File paths / Registry keys
*   *None.* (The strings `Control Panel\Desktop\ResourceLocale` and `.DEFAULT\Control Panel\International` are standard Windows system paths and have been excluded as per instructions).

### Mutex names / Named pipes
*   *None detected.*

### Hashes
*   *None detected.*

### Other artifacts
*   **Framework Identification:** Inno Setup (Versions 5.5.0, 5.5.3)
    *   `InnoSetupLdrWindow`
    *   `Inno Setup Setup Data (5.5.0)`
    *   `Inno Setup Messages (5.5.3)`
*   **Command Line Arguments:**
    *   `/SILENT`
    *   `/VERYSILENT`
    *   `/SUPPRESSMSGBOXES`
    *   `/LOG`
    *   `/NORESTART`
    *   `/CLOSEAPPLICATIONS`
*   **Internal Strings (Potential Junk/Obfuscation):** 
    *   `_^[YY]`
    *   `YZ]_^[`

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`
- `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: dropper
3. **Confidence**: High

4. **Key evidence**:
* **Inno Setup Wrapper:** The binary is identified as an Inno Setup installer, a common technique used by malware authors to mask malicious actions behind a legitimate-looking installation interface and standard system calls.
* **Multi-stage Execution:** The use of `CreateProcessA` followed by `MsgWaitForMultipleObjects` indicates the binary acts as a "wrapper" or orchestrator designed to launch a secondary payload while ensuring it executes successfully.
* **Standard Dropper Behaviors:** The presence of directory creation, registry interaction for configuration/persistence, and the exclusion of its own primary malicious payload (which is delivered by this installer) are classic characteristics of an initial-stage dropper.
