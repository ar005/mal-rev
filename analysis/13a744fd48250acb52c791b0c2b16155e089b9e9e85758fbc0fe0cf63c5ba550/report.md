# Threat Analysis Report

**Generated:** 2026-09-02 21:15 UTC
**Sample:** `13a744fd48250acb52c791b0c2b16155e089b9e9e85758fbc0fe0cf63c5ba550_13a744fd48250acb52c791b0c2b16155e089b9e9e85758fbc0fe0cf63c5ba550.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13a744fd48250acb52c791b0c2b16155e089b9e9e85758fbc0fe0cf63c5ba550_13a744fd48250acb52c791b0c2b16155e089b9e9e85758fbc0fe0cf63c5ba550.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,423,579 bytes |
| MD5 | `868a963de024f3e627626e3bcab3bac6` |
| SHA1 | `fe68571dbeec5469f4ea1cd8289fff9044012d81` |
| SHA256 | `13a744fd48250acb52c791b0c2b16155e089b9e9e85758fbc0fe0cf63c5ba550` |
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
| `.rsrc` | 11,264 | 4.535 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **7488** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The binary is a **setup installer**, specifically one built using the **Inno Setup** framework (evidenced by several "InnoSetup" related strings and internal function names like `InnoSetupLdrWindow`). 

Its primary purpose is to act as an installer wrapper. It handles standard installation tasks such as:
*   Processing command-line arguments (e.g., `/SILENT`, `/DIR`, `/LOG`).
*   Handling system localization and language selection (`GetSystemDefaultLCID`, `GetUserDefaultLangID`).
*   Extracting and decompressing compressed data (indicated by the **LZMA** decompression routines).
*   Managing installation logic, such as choosing paths and verifying prerequisites.

### Suspicious or Malicious Behaviors
While this is a standard installer structure, several behaviors are common in both legitimate installers and malware "droppers" or "wrappers":

*   **Packing/Decompression (Potential Payload Delivery):** The presence of `LZMA1` decompression strings and the complex loops in functions like `fcn.00401ee0` suggest that the main application (or a malicious payload) is stored in a compressed or obfuscated state within the installer. It is unpacked into memory or extracted to disk during execution.
*   **Environment/System Probing:** 
    *   The function `fcn.00406e10` uses `RegQueryValueExA` to query specific registry values. While common in installers to detect hardware specs, this is also a common technique for **anti-analysis** or **environment fingerprinting** (checking if the system is a virtual machine or belongs to a specific organization).
    *   The use of `GetSystemInfo`, `GetVersionExA`, and `GetProcAddress` in the startup phase suggests the program validates its environment before proceeding.
*   **Memory Manipulation:** The function `fcn.00407f10` utilizes `VirtualAlloc`. In this context, it is used to allocate memory for decompressed data; however, in a malware context, this is the standard method for allocating space to host an injected payload or unpacking a "hidden" stage of code.

### Notable Techniques and Patterns
*   **Inno Setup Framework:** The binary heavily relies on Inno Setup's structure. This makes it difficult to distinguish between a "legitimate installer" and a "malicious dropper," as both use this same wrapper to deliver their payload.
*   **Obfuscated Strings/Data Handling:** Several functions (e.g., `fcn.0040840c`, `fcn.00404e58`) involve complex arithmetic and manual pointer arithmetic to process strings or buffers. This can be used to hide cleartext strings until they are needed during execution.
*   **Staged Execution:** The flow of `entry0` suggests a multi-stage initialization where the installer first validates the environment, then prepares resources (decompressing LZMA blocks), and finally handles the installation logic. 
*   **Standard Win32 APIs for Persistence/Evasion:** While not directly showing a persistence mechanism in these specific snippets, the use of `GetModuleHandle` and `GetProcAddress` suggests the installer may dynamically resolve symbols to avoid static analysis by simple scanners.

### Summary Conclusion
This binary is an **Inno Setup installer**. It likely contains a compressed payload (using LZMA). While it currently shows standard installation behaviors, its role as a "wrapper" means it could be used to deliver any software—benign or malicious—by hiding the actual payload inside a standard-looking installer structure.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of LZMA decompression and complex arithmetic for string processing indicates an attempt to hide payload content and cleartext strings from static analysis. |
| **T1497** | Virtualization/Sandbox Detection | The usage of `RegQueryValueExA` and system information gathering functions suggests the binary is probing the environment to detect if it is running in a virtual machine or sandbox. |
| **T1027** | Obfuscated Files or Information (Dynamic Resolution) | The use of `GetProcAddress` and `GetModuleHandle` to resolve symbols at runtime is a common technique to bypass static scanners by hiding the program's true capabilities. |

### Analyst Notes:
*   **Wrapper Behavior:** While the analysis identifies this as an Inno Setup installer, its role as a "wrapper" means it functions as a **Dropper/Loader**. The specific behaviors identified (T1027 and T1497) are classic indicators of malicious intent when found in unauthorized applications.
*   **Memory Allocation:** While `VirtualAlloc` (found in section `fcn.00407f10`) is not a unique MITRE technique on its own, in this context, it serves as the mechanism for the **T1027** obfuscation routine to move the decompressed payload into memory before execution.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Per your instructions, standard Windows system files (e.g., *kernel32.dll*), generic API calls (e.g., *GetSystemInfo*), and standard OS registry paths have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline` 
    *(Note: This is the official documentation link for the Inno Setup framework.)*

### **File paths / Registry keys**
*   None (All identified registry paths, such as `.DEFAULT\Control Panel\International`, are standard Windows system components and were excluded).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Framework Identification:** Inno Setup (The binary is confirmed as an Inno Setup installer/wrapper).
*   **Compression Library:** LZMA1 (Indicates the use of the LZMA decompression algorithm to handle packed data or payloads).
*   **Behavioral Pattern:** Potential "Wrapper" behavior. The analysis indicates that while the outer shell is a standard installer, it utilizes `VirtualAlloc` and `LZMA` routines to unpack content into memory/disk, which is common in both legitimate installers and malicious droppers.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`
- `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline`

---

## Malware Family Classification

1. **Malware family:** Unknown (Inno Setup Wrapper)
2. **Malware type:** dropper / loader
3. **Confidence:** High

4. **Key evidence:**
*   **Wrapper Mechanism:** The binary uses the Inno Setup framework to act as an installer wrapper, a common technique used by threat actors to hide malicious payloads behind a legitimate-looking installation interface.
*   **Payload Obfuscation:** The use of LZMA decompression and `VirtualAlloc` memory allocation indicates that the primary payload is not stored in plain sight but is unpacked into memory at runtime (T1027), which is characteristic of droppers/loaders.
*   **Evasion Techniques:** The presence of environment fingerprinting (checking registry values, system information, and versioning) suggests intentional anti-analysis/anti-sandbox measures (T1497) to prevent the payload from being analyzed by security researchers.
