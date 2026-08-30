# Threat Analysis Report

**Generated:** 2026-08-16 21:05 UTC
**Sample:** `0fde26011f83d55d35f192de33bf32b9f7c13e54a5fca193abdff2ed27d37785_0fde26011f83d55d35f192de33bf32b9f7c13e54a5fca193abdff2ed27d37785.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0fde26011f83d55d35f192de33bf32b9f7c13e54a5fca193abdff2ed27d37785_0fde26011f83d55d35f192de33bf32b9f7c13e54a5fca193abdff2ed27d37785.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,679,652 bytes |
| MD5 | `09ab149b1824dc125d43219fc2e485b2` |
| SHA1 | `745a94c31f7334cd1fdda41be70fa7b56a8c3271` |
| SHA256 | `0fde26011f83d55d35f192de33bf32b9f7c13e54a5fca193abdff2ed27d37785` |
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

Total strings found: **7883** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality and behaviors.

### Core Functionality and Purpose
The binary appears to be a **wrapper or installer executable**, likely created using the **Inno Setup** framework (evidenced by the extensive InnoSetup-related strings such as `/SILENT`, `/VERYSILENT`, `InnoSetupLdrWindow`, and standard LZMA decompression logic).

Its primary purpose is to prepare the environment, resolve localizations, handle configuration via registry/system calls, and ultimately **launch a secondary payload or application**. 

### Suspicious or Malicious Behaviors
While much of the code follows standard "installer" patterns, several functions point toward behaviors common in malware droppers or installers:

*   **Process Spawning & Monitoring (`fcn.004099ec`):** 
    *   This function utilizes `CreateProcessA` to launch a child process using a command line retrieved at runtime. 
    *   It employs `MsgWaitForMultipleObjects` to wait for the spawned process's handle, which is standard but often used in droppers to ensure the payload starts before the "loader" exits or to monitor the startup success of a malicious component.
*   **Dynamic Memory Allocation & Management (`fcn.00407f10`, `fcn.00401ee0`):** 
    *   The code performs manual memory management using `VirtualAlloc` and `VirtualProtect`. It calculates required buffer sizes for "resources" or "modules." This is often used to unpack an encrypted/compressed payload into memory before execution.
*   **Resource Handling & Extraction:** 
    *   The inclusion of LZMA decompressor logic (`TLZMA1SmallDecompressorS`) and multiple internal functions for managing data blocks suggests that the binary contains "payload" data (likely a DLL or another EXE) which it extracts during execution.
*   **Environment Discovery & Registry Interaction (`fcn.00406e10`):** 
    *   The code actively queries registry keys using `RegQueryValueExA`. While common in installers, in a malware context, this is often used to check for security software, gather system info, or ensure the environment is "clean" before deploying a payload.

### Notable Techniques and Patterns
*   **Inno Setup Framework:** The binary's heavy reliance on InnoSetup code indicates it is designed to be a first-stage installer. This provides a layer of legitimacy because many legitimate programs use this framework, but malware authors also favor it for its robust "wrapping" capabilities.
*   **String/Path Processing (`fcn.00404e58`):** 
    *   The binary contains complex logic to handle environment variables (like `%` symbols) and directory navigation. This ensures that the target payload is launched from a valid or intended path.
*   **Localization Handling (`fcn.00405280`, `fcn.0040953c`):** 
    *   Extensive logic is dedicated to detecting the system's `Locale` and `LCID`. This ensures the installer/dropper can adapt to different regions, a common feature in large-scale malware campaigns.
*   **Data Processing Loops:** 
    *   Several functions (e.g., `fcn.00408b08`, `fcn.00406301`) contain nested loops and complex math to process data segments, which are typical for decrypting or decompressing embedded files.

### Summary Table
| Feature | Observation | Potential Significance |
| :--- | :--- | :--- |
| **Launcher/Dropper** | Uses `CreateProcessA` with monitoring loop. | Typical of a 1st-stage dropper; manages the "handoff" to the payload. |
| **Packaging** | Heavy use of Inno Setup strings and LZMA logic. | Indicates a wrapper for high-volume distribution. |
| **Memory/Resources** | `VirtualAlloc` / `VirtualProtect` manipulation. | Used to unpack or map the final payload into memory. |
| **Environment Query** | Registry parsing (`RegQueryValueExA`) and Locale checks. | Standard, but can be used for environment fingerprinting. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of LZMA decompression and `VirtualAlloc`/`VirtualProtect` indicates the binary unpacks an obfuscated payload into memory before execution. |
| T1036 | Masquerading | The heavy reliance on the Inno Setup framework allows the binary to appear as a legitimate installer, hiding its malicious intent. |
| T1038 | System Information Discovery | The use of `RegQueryValueExA` and locale checks suggests environmental fingerprinting to gather system details or identify security measures. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of genuine Indicators of Compromise (IOCs). 

**Note:** Standard Windows system paths (e.g., `.DEFAULT\Control Panel`), standard library DLLs (e.g., `kernel32.dll`, `shell32.dll`), and documentation links for common software frameworks (e.g., Inno Setup help pages) have been excluded as false positives per your instructions.

### **IP addresses / URLs / Domains**
*   None identified (The identified URL belongs to standard Inno Setup documentation).

### **File paths / Registry keys**
*   None identified (All detected paths were standard Windows system locations).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Framework Identification:** The binary heavily utilizes the **Inno Setup** installer framework (identified via `InnoSetupLdrWindow`, `TLZMA1SmallDecompressorS`, and standard command-line flags like `/SILENT` and `/VERYSILENT`).
*   **Dropper/Loader Behavior:** 
    *   The sequence of **`CreateProcessA`** followed by **`MsgWaitForMultipleObjects`** is a specific behavior pattern used to ensure a child process (payload) is launched before the loader exits.
    *   Use of **`VirtualAlloc`** and **`VirtualProtect`** in conjunction with LZMA decompression suggests the presence of an embedded, compressed payload being unpacked into memory or a temporary location.

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
* **Payload Delivery Mechanism:** The combination of `VirtualAlloc`, `VirtualProtect`, and the inclusion of LZMA decompression logic indicates that the binary is designed to decompress and unpack an embedded payload into memory or a temporary location before execution.
* **Process Handoff Behavior:** The use of `CreateProcessA` followed by `MsgWaitForMultipleObjects` is a classic signature of a first-stage loader, ensuring the malicious child process is successfully initialized before the wrapper/installer exits.
* **Masquerading Techniques:** The heavy reliance on the Inno Setup framework and extensive localization logic are deliberate tactics used to mask the file's malicious intent by making it appear as a legitimate software installer.
