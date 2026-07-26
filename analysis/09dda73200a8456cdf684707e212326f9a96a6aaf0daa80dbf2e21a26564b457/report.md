# Threat Analysis Report

**Generated:** 2026-07-23 16:15 UTC
**Sample:** `09dda73200a8456cdf684707e212326f9a96a6aaf0daa80dbf2e21a26564b457_09dda73200a8456cdf684707e212326f9a96a6aaf0daa80dbf2e21a26564b457.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `09dda73200a8456cdf684707e212326f9a96a6aaf0daa80dbf2e21a26564b457_09dda73200a8456cdf684707e212326f9a96a6aaf0daa80dbf2e21a26564b457.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 4,494,402 bytes |
| MD5 | `f2f5e18474c0ccda742a1fc80be19b75` |
| SHA1 | `78546e37890ccf9cb4f6e53e5bf93906e3c1a0a0` |
| SHA256 | `09dda73200a8456cdf684707e212326f9a96a6aaf0daa80dbf2e21a26564b457` |
| Overall entropy | 7.999 |
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
| `.rsrc` | 11,264 | 4.463 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **9943** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The code identifies as a **software installer or wrapper**, specifically utilizing the **Inno Setup** framework. Its primary purpose is to manage the installation process, handle localization (different languages), extract compressed data (likely using LZMA compression), and eventually launch an executable.

### Behavioral Breakdown

*   **Installer Stub Logic:** The inclusion of "InnoSetup" strings and various decompression-related functions (`LZMA1SmallDecompressorS`) indicates that this binary is designed to unpack and install another application.
*   **Process Spawning & Execution:** 
    *   The function `fcn.004099a4` is a significant behavior: it calls `CreateProcessA` using a command line (retrieved from internal logic) and then enters a loop using `MsgWaitForMultipleObjects`. This ensures the installer waits for the newly launched application to finish or stay active before continuing its own cleanup.
*   **Localization & Internationalization:** 
    *   The code contains extensive routines (`fcn.00405270`, `fcn.0040953c`) to check the system's default locale, language ID (LCID), and regional settings. It likely does this to display the correct language for setup prompts or "Success" messages.
*   **System Information Gathering:** 
    *   The code uses `RegQueryValueExA` (`fcn.00406e10`) to query values from the Windows Registry. This is commonly used by installers to check if a specific software version is already installed or to gather system information to determine hardware compatibility.
*   **Memory Management:** 
    *   The code uses `VirtualAlloc` and `VirtualProtect` via internal wrappers. This is common in installer stubs to allocate space for decompressing files in memory before writing them to disk.

### Suspicious or Malicious Behaviors
While the behavior described above is consistent with a legitimate installer, it is also the **standard architecture for malware "droppers" and "wrappers."**

*   **Wrapper/Dropper Potential:** The use of `CreateProcessA` followed by waiting for the child process suggests this binary acts as a first-stage dropper. It installs or extracts a payload and then launches it.
*   **Obfuscation via Generic Tools:** By using the Inno Setup framework, the author can hide malicious intent behind a "standard" installer's behavior (e.g., if a user sees an Installer window, they are less likely to suspect a Trojan).
*   **Persistence/System Interaction:** While there is no direct evidence of registry-based persistence in this specific snippet, the use of `RegQueryValueExA` indicates it interacts with the system environment beyond basic file execution.

### Notable Techniques & Patterns
*   **Standard Installer Framework:** The heavy reliance on InnoSetup structures means much of the code's complexity is due to the installer's "boilerplate" logic (handling errors, icons, and UI components) rather than custom malicious functionality.
*   **Robust Error Handling:** Many functions include loops and checks for common system failures (e.g., "file not found," "access denied") which are typical of installers meant to run on a wide variety of end-user machines.
*   **Dynamic Loading Logic:** The use of `GetProcAddress` in `fcn.00407024` is a standard way for installers to handle compatibility across different Windows versions (e.g., finding the correct API for both 32-bit and 64-bit systems).

### Summary
This binary is an **installer wrapper**. Its main task is to handle the "heavy lifting" of installation: checking system settings, localizing the UI, decompressing files, and launching the final application. From a malware analysis perspective, this should be treated as a **dropper**; the actual malicious payload is likely hidden within the compressed data that this installer extracts and executes.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files | The use of the Inno Setup framework and LZMA decompression acts as a wrapper to hide the true nature of the payload from static analysis. |
| **T1055** | Process Injection | The utilize of `VirtualAlloc` and `VirtualProtect` indicates memory preparation commonly used by droppers to unpack or decompress a payload into memory before execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None detected.

**File paths / Registry keys**
*   None detected (Note: The string `.DEFAULT\Control Panel\International` was identified but excluded as a standard Windows system path).

**Mutex names / Named pipes**
*   None detected.

**Hashes**
*   None detected.

**Other artifacts**
*   **Tool/Framework Identification:** Inno Setup (The binary functions as an installer wrapper/dropper using the Inno Setup framework).
*   **Compression Method:** LZMA (Specifically `LZMA1SmallDecompressorS`) used for unpacking embedded payloads.
*   **Behavioral Indicator:** Dropper logic detected (Use of `CreateProcessA` followed by a loop to wait for child process execution, common in first-stage malware).

***

**Analyst Note:** The provided data describes a **wrapper/dropper**. While there are no specific network indicators (IPs/Domains) or unique file paths present in this sample, the use of Inno Setup and LZMA decompression indicates that the primary malicious payload is likely compressed within the installer's resources.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

1. **Malware family**: Unknown (The binary utilizes the common Inno Setup framework, which is agnostic to specific threat actors).
2. **Malware type**: Dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Wrapper Functionality:** The heavy reliance on Inno Setup and LZMA decompression indicates the binary's primary role is to wrap and unpack an embedded payload, a classic "first-stage" behavior.
    *   **Execution Flow:** The use of `CreateProcessA` followed by a loop using `MsgWaitForMultipleObjects` confirms it is designed to launch a secondary executable while maintaining its own process presence until the child finishes.
    *   **Obfuscation via Legitimate Tools:** By mimicking a standard software installer, the malware hides its malicious intent (the actual payload) behind legitimate system-level behaviors like localization and memory management.
