# Threat Analysis Report

**Generated:** 2026-07-12 10:40 UTC
**Sample:** `0503023d8a89569f30da4456941166a7a1670e027687349f2584863674725281_0503023d8a89569f30da4456941166a7a1670e027687349f2584863674725281.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0503023d8a89569f30da4456941166a7a1670e027687349f2584863674725281_0503023d8a89569f30da4456941166a7a1670e027687349f2584863674725281.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,886,279 bytes |
| MD5 | `c1cbb7aa64836bf90c2007d98236713e` |
| SHA1 | `211be411c9b719d27267677682fa6622754d53f9` |
| SHA256 | `0503023d8a89569f30da4456941166a7a1670e027687349f2584863674725281` |
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
| `.rsrc` | 11,264 | 4.46 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **8419** (showing first 100)

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

Based on an analysis of the provided assembly and decompiled C code, here is a summary of what this binary does.

### Core Functionality and Purpose
The binary functions as a **software installer stub or launcher** (highly likely created with the **Inno Setup** framework). It is designed to check system environment variables, handle localization/language settings, and eventually launch a secondary application. 

Key functional components include:
*   **Environment Validation:** The code extensively checks for the system's locale, language ID (`GetSystemDefaultLCID`), and regional settings. This is typical of an installer trying to display the correct language for the user.
*   **Resource Management:** Several functions (like `fcn.00407f10` and `fcn.004019dc`) manage memory allocations (`VirtualAlloc`, `LocalFree`) and deallocations, likely for handling compressed installer data or icons/resource files.
*   **Data Decompression:** The presence of LZMA-related strings suggests the binary handles large amounts of compressed data (standard in installation packages).
*   **Registry Interaction:** It uses `RegQueryValueExA` to read configuration keys from the Windows Registry, likely used to determine existing software versions or user preferences.

### Suspicious or Malicious Behaviors
From a pure technical standpoint, there are very few "malicious" behaviors in the code; however, some functions are common in malware that would require further investigation:

*   **Process Execution (Launcher Pattern):** 
    *   Function `fcn.004099a4` calls `CreateProcessA` to launch a secondary program based on a constructed command line. It then enters a loop using `MsgWaitForMultipleObjects` to wait for that process to finish before continuing or exiting itself. 
    *   *Context:* While this is a common "Dropper" technique, in the context of the other strings (Inno Setup), it is almost certainly just the installer launching the application after installation is complete.
*   **Registry Querying:** The use of `RegQueryValueExA` in `fcn.00406e10` allows the program to read data from the registry. 
    *   *Context:* This is a standard way for installers to find system paths, but it can also be used by malware to gather information about the machine or check for security software.
*   **Memory Manipulation:** The use of `VirtualProtect` and `VirtualAlloc` (often hidden in wrapper functions like `fcn.00407f10`) is used to prepare memory space.

### Notable Techniques and Patterns
*   **Inno Setup Framework:** The inclusion of strings like `InnoSetupLdrWindow`, `LZMA` decompressors, and `Wow64DisableWow64FsRedirection` identifies the binary as being wrapped in a standard installer engine. This suggests it is not custom-written malware but rather an automated script/installer tool.
*   **Sophisticated String Handling:** The function `fcn.00404e48` and others indicate heavy use of internal string parsing (handling characters like `%`, `:`, and `.`). This is typical for processing file paths or configuration strings.
*   **Large-Scale Validation Loop:** Function `fcn.00405270` shows a loop designed to iterate through several system parameters, likely ensuring all necessary localization features are available before the "real" program starts.

### Summary Conclusion
This binary appears to be a **legitimate installer wrapper**. It performs extensive environment checks (language/locale), manages local resources and memory, and spawns an additional process at the end of its execution. Unless the secondary process launched in `fcn.004099a4` is hidden or malicious, this binary behaves like standard software installation middleware.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The use of `CreateProcessA` to launch a secondary program is a common method for droppers to execute payloads or transition to subsequent stages. |
| **T1140** | Deobfuscate/Decode Files or Streams | The inclusion of LZMA-related strings indicates the binary handles compressed data, which is frequently used in malware to hide packed code or resources. |
| **T1112** | System Information Discovery | The use of `RegQueryValueExA` allows the application to query configuration details and system settings from the Windows Registry. |
| **T1055** | Process Injection | The use of `VirtualAlloc` and `VirtualProtect` are classic indicators of preparing memory space for executable code, often used in injection techniques. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs).

**Note:** A rigorous filtering process was applied to exclude standard Windows API calls, internal compiler/linker symbols, and common Inno Setup installer framework artifacts.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   *None.* (While registry paths such as `\Control Panel\International` were mentioned in the strings, these are standard Windows system paths and have been excluded as false positives.)

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Framework Identification:** The binary utilizes the **Inno Setup** installer framework (Version 5.5.0). While not a direct IOC for a specific malware campaign, it identifies the method of delivery/packaging.
*   **Behavioral Pattern - Launcher/Dropper:** The analysis notes a "Launcher" pattern where the binary constructs a command line to execute a secondary process (at `fcn.004099a4`) and waits for it to complete.
*   **Data Compression:** Use of **LZMA** decompression logic indicates handling of compressed payload or resources.

---
**Analyst Note:** The provided data suggests this is a standard installer wrapper. No specific malicious infrastructure (IPs, unique file paths, or hardcoded C2 addresses) was identified in the provided text.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper (Installer Wrapper)
3. **Confidence**: High
4. **Key evidence**:
*   **Standard Framework Usage:** The binary is identified as an **Inno Setup** wrapper, utilizing standard components like LZMA decompression and resource management common in legitimate software installers.
*   **Typical Installer Behavior:** Extensive checks for system locale/language and the use of `CreateProcessA` to launch a secondary application are consistent with an installer launching its payload after completion rather than malicious activity.
*   **Absence of Malicious Indicators:** The analysis found no hardcoded C2 infrastructure, suspicious network calls, or unique encryption keys that would indicate a specific malware campaign.
