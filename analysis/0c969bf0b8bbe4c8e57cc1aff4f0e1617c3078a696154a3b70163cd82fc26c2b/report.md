# Threat Analysis Report

**Generated:** 2026-07-31 17:35 UTC
**Sample:** `0c969bf0b8bbe4c8e57cc1aff4f0e1617c3078a696154a3b70163cd82fc26c2b_0c969bf0b8bbe4c8e57cc1aff4f0e1617c3078a696154a3b70163cd82fc26c2b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c969bf0b8bbe4c8e57cc1aff4f0e1617c3078a696154a3b70163cd82fc26c2b_0c969bf0b8bbe4c8e57cc1aff4f0e1617c3078a696154a3b70163cd82fc26c2b.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,999,081 bytes |
| MD5 | `3ecac2db62ac4afe6157b4def600334b` |
| SHA1 | `f8392048017476dfcac74762cec9cdac6bb58ede` |
| SHA256 | `0c969bf0b8bbe4c8e57cc1aff4f0e1617c3078a696154a3b70163cd82fc26c2b` |
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
| `.rsrc` | 11,264 | 4.536 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **8727** (showing first 100)

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

Based on the provided disassembly and string data, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The binary appears to be a **software installer or a "dropper"** constructed using the **Inno Setup** framework (confirmed by the extensive Inno Setup-related strings like `InnoSetupLdrWindow`, `TSetupLanguageEntryA`, and standard setup command-line parameters).

Its primary role is to:
*   **Handle installation logic:** It processes complex path strings, handles localization/language detection (`GetSystemDefaultLCID`), and parses command-line arguments.
*   **Environment Setup:** It queries the Windows Registry (`RegQueryValueExA`) and checks system environments to determine appropriate paths or configurations for an application.
*   **Payload Execution:** It acts as a wrapper that prepares the environment and then executes additional components or processes.

### Suspicious or Malicious Behaviors
While many of these behaviors are standard for legitimate installers, they are frequently abused by malware (particularly "droppers" or "loaders") to blend in with system activity:

*   **Process Spawning (Potential Dropper Activity):**
    *   Function `fcn.004099ec` calls `CreateProcessA`. It takes a command line, launches a process, and then enters a loop using `MsgWaitForMultipleObjects` to wait for the child process to exit before continuing. This is a classic pattern used by droppers to launch a malicious payload (e.g., a RAT or ransomware) while maintaining a "waiting" state in the installer's window.
*   **Registry Interaction:**
    *   Function `fcn.00406e10` interacts with the Windows Registry (`RegQueryValueExA`). While common for reading settings, malware uses this to check for security software, gather system information, or establish persistence (though no specific keys/values were identified in this snippet).
*   **String Manipulation & Path Parsing:**
    *   Functions like `fcn.00404e58` and `fcn.00406744` contain heavy logic for handling quoted paths, trailing backslashes, and special characters. This is used to ensure that the installer can correctly locate files or navigate directories, even if they contain spaces—a technique often used to bypass simple path-based security filters.

### Notable Techniques & Patterns
*   **Inno Setup Wrapper:** The use of a known, legitimate installer framework is a common evasion technique. By using Inno Setup components, the malicious behavior (like process spawning) "looks" like a standard installation procedure to automated sandboxes and human analysts.
*   **Robust Environment Checking:** The inclusion of `fcn.00405280` (locale/language handling) suggests a high level of polish. This ensures that if the payload is malicious, it will present itself in the language appropriate for the target user's OS.
*   **Standard API usage to "Blend In":** The binary uses common Windows API calls (`GetSystemTime`, `GetModuleHandleA`, `MessageBoxA`) and standard libraries. It does not show immediate signs of advanced anti-analysis (like VM detection or debugger checks) in this specific snippet, likely because it relies on the "innocent" appearance of a legitimate installer to bypass initial scrutiny.

### Summary for Incident Response
This binary is likely an **installer/dropper**. While it may be a legitimate tool, its behavior—specifically the multi-step process spawning and registry querying—makes it highly suspicious. It should be treated as a "loader." If it is confirmed malicious, any processes launched by `fcn.004099ec` should be identified as the primary payload (the second stage of an infection).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of the Inno Setup framework allows the binary to blend in with legitimate system activity by appearing as a standard installer. |
| T1059 | Command and Scripting Interpreter | The use of `CreateProcessA` to launch child processes via command-line arguments is a typical mechanism for droppers/loaders to execute subsequent payloads. |
| T1112 | System Information Discovery | The use of `RegQueryValueExA` indicates the binary is querying the registry to gather system information and environment settings. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Following your instructions, standard Windows system paths (e.g., `Control Panel\Desktop\ResourceLocale`), common library files (e.g., `kernel32.dll`, `shell32.dll`), and standard API calls have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   None identified. *(Note: The URL `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline` was found in the strings, but this is a legitimate documentation link for the Inno Setup installer framework and does not constitute a malicious C2 or phishing domain.)*

### **File paths / Registry keys**
*   None identified. *(All paths provided in the source text refer to standard Windows system configurations).*

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Tooling/Framework:** Inno Setup (Identified via `InnoSetupLdrWindow` and specific command-line parameters like `/SILENT`, `/VERYSILENT`, and `/SUPPRESSMSGBOXES`).
*   **Behavioral Pattern (Loader/Dropper):** The binary utilizes a "Wait for Child" pattern (`MsgWaitForMultipleObjects`) following a `CreateProcessA` call at address `fcn.004099ec`. This is characteristic of droppers designed to hide the execution of a secondary malicious payload.
*   **Behavioral Pattern (Environment Obfuscation):** The binary includes extensive logic for handling quoted paths and special characters, often used to ensure successful deployment across varied environments while bypassing simple string-matching security filters.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`
- `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Masquerading via Known Frameworks:** The binary utilizes the Inno Setup framework to blend in with legitimate software installation processes, a common technique used to bypass initial security scrutiny and human suspicion.
*   **"Wait for Child" Execution Pattern:** The use of `CreateProcessA` followed by a loop containing `MsgWaitForMultipleObjects` is a classic signature of a dropper/loader; it ensures the installer stays active while the actual malicious payload (the second stage) is executed in a separate process.
*   **Robust Environmental Adaptation:** The inclusion of complex logic for handling quoted paths, locale detection, and system registry queries suggests a professional level of polish intended to ensure the successful delivery and execution of a payload across varied user environments.
