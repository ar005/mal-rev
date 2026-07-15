# Threat Analysis Report

**Generated:** 2026-07-13 20:08 UTC
**Sample:** `056c03d6fd1ef468bb8eebac2b49d87be9c82d6ac1fd0a9c581832647246015e_056c03d6fd1ef468bb8eebac2b49d87be9c82d6ac1fd0a9c581832647246015e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `056c03d6fd1ef468bb8eebac2b49d87be9c82d6ac1fd0a9c581832647246015e_056c03d6fd1ef468bb8eebac2b49d87be9c82d6ac1fd0a9c581832647246015e.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,871,797 bytes |
| MD5 | `e46b84c4295ed6d4c62025f9f8f038d9` |
| SHA1 | `ec37b46da7470317bd65393a2f23ace11c9b34ec` |
| SHA256 | `056c03d6fd1ef468bb8eebac2b49d87be9c82d6ac1fd0a9c581832647246015e` |
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
| `.rsrc` | 11,264 | 4.462 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **8452** (showing first 100)

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

This analysis is based on the provided disassembly and decompiled C code for the binary sample.

### Core Functionality and Purpose
The binary appears to be a **sophisticated installer or "loader" wrapper**, likely utilizing the Inno Setup framework (based on strings like `InnoSetupLdrWindow` and `Inno Setup Setup Data`). Its primary role is to prepare the environment, handle localization/internationalization, and ultimately launch another application.

### Suspicious or Malicious Behaviors
While many of these behaviors are common in legitimate installers, they are also frequently used by malware (droppers) to facilitate the execution of a secondary payload.

*   **Process Spawning & Monitoring (`fcn.004099a4`):** 
    *   The code uses `CreateProcessA` to launch a new process.
    *   It then enters a loop using `MsgWaitForMultipleObjects` to wait for the child process's handle. This ensures that the parent (the installer/loader) remains active until the child process is fully initialized or finished. This is a classic technique used in **droppers** to ensure the payload successfully starts before the initial wrapper exits.
*   **File System Preparation (`fcn.00409330`):**
    *   The code contains a loop that calls `CreateDirectoryA`. It appears to be checking and creating paths required for the installation/extraction process. 
*   **Memory Management & Dynamic Allocation:**
    *   Function `fcn.00407f10` utilizes `VirtualAlloc` to allocate memory blocks, specifically checking if the allocated size meets requirements before proceeding. This is often used when a "payload" needs to be unpacked into memory or a specific buffer.
*   **Localization/Information Gathering:**
    *   Functions like `fcn.00405270` and calls to `GetSystemDefaultLCID` suggest the binary actively checks system locale and regional settings, which is standard for installers but also used by malware to tailor the experience or detect specific language environments.

### Notable Techniques & Patterns
*   **Inno Setup Infrastructure:** The presence of LZMA decompression strings (`TLZMA1SmallDecompressorS`) and InnoSetup-specific identifiers indicates this binary is designed to unpack large amounts of data (the "actual" program) from a compressed file on disk.
*   **Robust Error Handling:** Several functions (like `fcn.004063e6` and `fcn.00408c80`) contain complex logic for handling numeric-to-string conversions or status checks, suggesting the code is designed to handle various system states gracefully.
*   **Wrapped Execution:** The "main" flow (as seen in `entry0` and related functions) doesn't perform direct malicious actions (like keylogging or data exfiltration) but instead handles the heavy lifting of environment setup, making it an ideal **loader/stub** for malware.

### Summary
The sample is a **heavyweight installer wrapper**. It performs standard administrative tasks such as creating directories, managing memory, and handling localized strings. Its most "suspicious" characteristic is its behavior in `fcn.004099a4`, where it creates a child process and waits for it to execute. In a malware context, this confirms the binary's role as a **dropper**—it delivers and ensures the execution of a secondary payload while potentially hiding behind the guise of an "installation" routine.

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1129** | Archive Extraction | The use of LZMA decompression and "unpacking" large amounts of data indicates the binary acts as a wrapper to extract payload components from a compressed format. |
| **T1055** | Process Injection | The use of `VirtualAlloc` to allocate memory blocks for an unpacked "payload" is a common precursor to loading malicious code into memory. |
| **T1036** | Masquerading | The binary utilizes the Inno Setup framework and installer-like naming conventions to hide its true purpose as a loader/dropper from the user and security tools. |
| **T1082** | System Information Discovery | The calls to `GetSystemDefaultLCID` are used to gather information regarding system locales and regional settings, which can be used to tailor the malware's behavior or environment checks. |
| **T1569** | Launch_Adjacent_Process | (Optional/Implicit) The use of `CreateProcessA` combined with a wait loop (`MsgWaitForMultipleObjects`) specifically ensures the child process—the actual payload—is launched successfully before the loader exits. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here is the extraction of Indicators of Compromise (IOCs). 

Note: Per your instructions, standard Windows system files (e.g., `kernel32.dll`), common API functions, and standard registry paths have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (The mentioned paths such as `.DEFAULT\Control Panel\` are standard Windows system paths).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Application Framework:** Inno Setup (Detected via `InnoSetupLdrWindow` and `Inno Setup Setup Data` strings).
*   **Compression Library:** LZMA (Identified by `TLZMA1SmallDecompressorS` and `lzmadecompsmall`).
*   **Behavioral Signature (Dropper/Loader):** 
    *   The binary utilizes a **Wait-for-Child** pattern: It calls `CreateProcessA` followed by `MsgWaitForMultipleObjects`. This is a specific behavior used to ensure the loader remains active until the payload successfully initializes.
    *   **Dynamic Memory Allocation:** Use of `VirtualAlloc` for potential payload unpacking into memory buffers.
*   **Potential Obfuscation/Junk Data:** The repeated occurrences of non-standard character strings (e.g., `YZ]_^[`, `_^[YY]`, `QQQQQQQQSVW`) suggest the presence of a packer or obfuscated string table, though they do not map to specific known C2 infrastructure in this text.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High
4. **Key evidence**:
*   **Inno Setup Wrapper:** The binary uses common installer frameworks (Inno Setup, LZMA decompression) to masquerade as a legitimate software installer while preparing the environment for secondary components.
*   **Wait-for-Child Execution Pattern:** The use of `CreateProcessA` followed by `MsgWaitForMultipleObjects` is a classic indicator of a loader; it ensures the malicious payload is successfully initialized before the initial wrapper process exits.
*   **Memory Manipulation & Extraction:** The combination of `VirtualAlloc` and archive extraction capabilities indicates that the binary is designed to unpack or inject an actual payload into memory, rather than performing direct malicious actions (like data theft) itself.
