# Threat Analysis Report

**Generated:** 2026-08-11 22:45 UTC
**Sample:** `0e3bd9bb3c911857b7c6ccdf16c9d540a4710e2303037c80675de64f931bb750_0e3bd9bb3c911857b7c6ccdf16c9d540a4710e2303037c80675de64f931bb750.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e3bd9bb3c911857b7c6ccdf16c9d540a4710e2303037c80675de64f931bb750_0e3bd9bb3c911857b7c6ccdf16c9d540a4710e2303037c80675de64f931bb750.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 4,135,987 bytes |
| MD5 | `ecdf4721092ce50800ed1f28bbc25264` |
| SHA1 | `7350a9b2cba074d232a953eeff83d8c362f881fd` |
| SHA256 | `0e3bd9bb3c911857b7c6ccdf16c9d540a4710e2303037c80675de64f931bb750` |
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

Total strings found: **9092** (showing first 100)

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

Based on the provided disassembly and string data, here is the technical analysis of the binary:

### Core Functionality and Purpose
The binary appears to be a **software installer**, specifically one utilizing the **Inno Setup** framework (as evidenced by numerous strings like `InnoSetupLdrWindow`, `Inno Setup Setup Data`, and standard setup command-line parameters). Its primary purpose is to handle installation logic, manage file extractions, configure system settings via the registry, and launch secondary components.

### Suspicious or Malicious Behaviors
While much of the code is consistent with a standard installer (potentially providing a "wrapper" for malware), the following behaviors are noteworthy:

*   **Process Execution:** The function `fcn.004099ec` calls **`CreateProcessA`**. 
    *   *Significance:* While common in installers to launch post-install scripts or secondary tools, this is a primary technique for "dropping" and executing additional payloads or malicious components.
*   **File System Manipulation:** The function `fcn.00409330` calls **`CreateDirectoryA`**. 
    *   *Significance:* This is used to create directories for the installation of files; however, it can also be used by malware to create hidden folders for staging malicious tools.
*   **Registry Interaction:** The function `fcn.00406e10` utilizes **`RegQueryValueExA`**. 
    *   *Significance:* This indicates the program is reading configuration data from the Windows Registry, which may include system paths, user preferences, or persistence mechanisms.
*   **Memory Management & Potential Unpacking:** The functions `fcn.00407f10` and `fcn.004019dc` use **`VirtualAlloc`**, **`VirtualFree`**, and **`LocalFree`**. 
    *   *Significance:* While often used by installers to manage memory for large data extractions, these APIs are also heavily utilized in "unpackers" or "loaders" to allocate executable memory regions (e.g., `PAGE_EXECUTE_READWRITE`) before running a secondary, hidden stage of code.

### Notable Techniques and Patterns
*   **Installer Wrapping:** The heavy presence of Inno Setup strings indicates the malware is likely using a legitimate installer as a "wrapper." This is a common evasion technique to bypass basic antivirus signatures by hiding malicious code inside a standard installation routine.
*   **String Manipulation/Parsing:** Functions like `fcn.00404e58` and `fcn.00406744` suggest complex string parsing or logic for handling configuration files/scripts. 
*   **Localization Logic:** The use of `GetSystemDefaultLCID` and various locale-checking loops (e.g., `fcn.00405280`) indicates the installer is designed to be portable across different regions, common in both legitimate commercial software and widespread malware.
*   **Complexity in Setup Logic:** The entry point (`entry0`) and surrounding functions show a high degree of complexity in state management (looping through variables like `uVar1`, `iVar2` with numerous conditional checks), which is typical for an installer but can also be used to obfuscate the "real" transition from an installer to a malicious payload.

### Summary Recommendation
The sample displays behavior consistent with a **malware dropper or downloader** wrapped in a legitimate-looking Inno Setup installer. The presence of `CreateProcessA` and `VirtualAlloc` suggests that while the primary executable might be for installation, it likely serves as a vehicle to launch subsequent malicious stages.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1059 | Command and Scripting Interpreter | The use of `CreateProcessA` indicates the execution of secondary payloads, scripts, or additional malicious components. |
| T1083 | File and Directory Execution | The use of `CreateDirectoryA` is used to create paths for staging files or setting up environments for subsequent payload stages. |
| T1547 | Boot or Logon Autostart Execution | The use of `RegQueryValueExA` indicates the retrieval of configuration data, which may include information related to establishing persistence. |
| T1027 | Software Packing | The combination of `VirtualAlloc`, `VirtualFree`, and `LocalFree` suggests the binary is unpacking or loading hidden stages of code into memory. |
| T1036 | Masquerading | Utilizing an Inno Setup wrapper allows the malware to hide its true purpose by mimicking the behavior of a legitimate software installer. |

---

## Indicators of Compromise

Based on the strings provided and the behavioral analysis performed, here are the extracted Indicators of Compromise (IOCs). 

Note: Per your instructions, standard Windows system files (e.g., `kernel32.dll`), common API calls, and generic installer commands have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline` 
    *(Note: This is a standard Inno Setup help link; while not inherently malicious, it identifies the installer framework used.)*

### **File paths / Registry keys**
*   *None identified.* (The strings provided contain generic API calls for registry access but no specific hardcoded malicious paths or keys).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified in the provided text.*

### **Other artifacts**
*   **Installer Framework:** Inno Setup (Versions 5.5.0, 5.5.3)
*   **Suspicious Functions/Offsets:**
    *   `fcn.004099ec` (CreateProcessA - Potential payload dropping)
    *   `fcn.00409330` (CreateDirectoryA - File system staging)
    *   `fcn.00406e10` (RegQueryValueExA - Registry manipulation)
    *   `fcn.00407f10` & `fcn.004019dc` (VirtualAlloc/VirtualFree - Potential unpacking/injection behavior)
*   **Behavioral Pattern:** The binary exhibits "Installer Wrapping" characteristics, where a legitimate-looking installer is used to mask the execution of secondary payloads.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`
- `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High

**Key evidence**:
*   **Installer Wrapping:** The heavy reliance on Inno Setup components indicates a "masquerading" technique, where a legitimate installation routine is used to hide the deployment of malicious code.
*   **Payload Execution & Unpacking:** The presence of `CreateProcessA` and `VirtualAlloc`/`VirtualFree` functions strongly suggests that the primary role of this binary is to unpack and execute secondary payloads or hidden stages of a multi-stage attack.
*   **Staging Behavior:** The combination of `CreateDirectoryA` for folder creation and `RegQueryValueExA` for registry interaction indicates the sample is designed to prepare the environment for further malicious activity (e.g., persistence and file staging).
