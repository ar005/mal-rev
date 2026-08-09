# Threat Analysis Report

**Generated:** 2026-08-06 22:11 UTC
**Sample:** `0d941acd9d96069f3890f69d94c205dc59d8a3b075c90e0931b7e2d9518d76ee_0d941acd9d96069f3890f69d94c205dc59d8a3b075c90e0931b7e2d9518d76ee.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d941acd9d96069f3890f69d94c205dc59d8a3b075c90e0931b7e2d9518d76ee_0d941acd9d96069f3890f69d94c205dc59d8a3b075c90e0931b7e2d9518d76ee.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,439,974 bytes |
| MD5 | `02ed4ae4c851d46a77b1a02c25618048` |
| SHA1 | `633200a081321923deffb43d5be857bb5b41bae5` |
| SHA256 | `0d941acd9d96069f3890f69d94c205dc59d8a3b075c90e0931b7e2d9518d76ee` |
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
| `.rsrc` | 11,264 | 4.491 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **7622** (showing first 100)

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

Based on the provided disassembly and string data, here is the analysis of the binary sample:

### Core Functionality and Purpose
The binary appears to be a **standard software installer** or a "setup" executable. The extensive presence of **Inno Setup** strings (e.g., `/SILENT`, `/VERYSILENT`, `InnoSetupLdrWindow`) and standard installation logic confirms it is designed to install, configure, and initialize an application on a Windows system.

### Key Behaviors
*   **Installer Infrastructure:** The code utilizes the Inno Setup engine to handle common setup tasks such as checking for available disk space, identifying the system's language/region (LCID), and handling various command-line flags (e.g., `/LOG`, `/DIR`, `/PASSWORD`).
*   **Localization & Internationalization:** Several functions (`fcn.0040953c`, `fcn.00405280`) are dedicated to detecting the system's default language and matching it against supported locales in the installer’s resource files.
*   **Environment Variable Expansion:** Function `fcn.00408c80` contains logic specifically designed to identify and process symbols like `%` (e.g., `%SystemRoot%`) and `:` within strings, which is common when resolving file paths or network locations.
*   **File System Interaction:** The code includes routine calls to create directories (`fcn.00409330` calls `CreateDirectoryA`) and manage memory for installer resources (using `VirtualAlloc` in `fcn.00407f10`).
*   **Process Management:** Function `fcn.004099ec` utilizes `CreateProcessA`. In the context of an installer, this is typically used to launch a "launch_wizard" or perform post-installation tasks (like launching the newly installed application).
*   **Configuration Parsing:** The code performs significant amount of string manipulation and parsing (`fcn.00406744`, `fcn.00404e58`) to handle paths, version numbers, and system environment strings.

### Suspicious or Malicious Behaviors
*   **No Immediate Evidence of Injection:** There are no immediate indicators of process injection (e.g., `VirtualAllocEx`, `WriteProcessMemory` into remote processes) or "hollow" techniques in the provided functions. 
*   **Standard Registry Access:** While it accesses the registry (`RegQueryValueExA`), it appears to be doing so to read system information rather than establishing persistence (e.g., creating a "Run" key).
*   **No Obvious Network Communication:** No networking-specific APIs (like `WinInet` or `WS2_32`) are present in the decompiled sections; any network communication would likely occur in specialized modules not shown here.

### Notable Techniques & Patterns
*   **Standard Installer Wrapper:** The heavy reliance on Inno Setup suggests that if this is malicious, it is using a "dropper" or "packer" approach where a legitimate installer framework is used to bundle and deploy the payload.
*   **Dynamic Memory Management:** The code uses standard heap management for processing strings and setup data, which is typical of large Windows installers.
*   **Standard Logic Flow:** The entry point (`entry0`) follows a standard initialization pattern: setting up environment variables, checking system requirements, and then starting the main UI/installation loop.

### Conclusion
The sample displays the behavior of a **standard software installer**. It does not exhibit immediate "loud" malicious behaviors like process injection or automatic persistence in this specific segment; however, because it is an installer, its primary purpose is to modify the filesystem and registry to install a program. 

**Note for analyst:** While the code itself looks like a legitimate Inno Setup wrapper, you should still investigate the files being "installed" by this executable to ensure they do not contain malicious payloads (e.g., info-stealers or backdoors).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The binary utilizes an Inno Setup wrapper, a common technique to disguise malicious functionality as a legitimate software installer. |
| T1105 | Ingress Tool Transfer | The analysis identifies the binary's role as a "dropper" or "wrapper," which is used to bundle and deliver payloads into the environment. |
| T1059 | Command and Scripting Interpreter | The use of `CreateProcessA` to launch subsequent installation wizards or post-installation tasks indicates execution of secondary components. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: Because the behavioral analysis concludes that this is a standard **Inno Setup** installer, many items found in the strings (such as `.Default\Control Panel` or `kernel32.dll`) have been excluded as they are standard Windows system components/paths.

### **IP addresses / URLs / Domains**
*   `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline` (Note: This is the official help documentation for the Inno Setup installer engine).

### **File paths / Registry keys**
*   None (All identified paths, such as `USERPROFILE`, are standard Windows environment variables and do not constitute specific malicious indicators).

### **Mutex names / Named pipes**
*   None found.

### **Hashes**
*   None found.

### **Other artifacts**
*   **Installer Framework:** Inno Setup (Identified via strings `InnoSetupLdrWindow` and standard command-line switches such as `/SILENT`, `/VERYSILENT`, `/SUPPRESSMSGBOXES`).
*   **Known Logic:** The inclusion of `TCompressedBlockReader`, `TLZMA1SmallDecompressorS`, and `lzmadecompsmall` indicates the use of LZMA compression, standard for Inno Setup installers.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`
- `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: dropper
3. **Confidence**: Medium

4. **Key evidence**:
*   **Standard Installer Wrapper:** The sample heavily utilizes the Inno Setup framework (identified via strings like `InnoSetupLdrWindow` and `LZMA` decompression), which is a common method for wrapping payloads into a "standard" installer format to evade basic detection.
*   **Lack of Direct Malicious Payload:** The analysis confirms that this specific binary does not perform active malicious actions such as process injection or direct network communication; however, its role as a wrapper indicates it serves as a delivery mechanism (dropper) for subsequent components.
*   **Ambiguous Intent:** While the behavior is consistent with a legitimate installer, the use of T1036 (Masquerading) and T1105 (Ingress Tool Transfer) in the MITRE mapping suggests that while the file itself is an installer, it is functionally categorized as a dropper in potential attack chains.
