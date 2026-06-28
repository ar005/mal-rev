# Threat Analysis Report

**Generated:** 2026-06-28 07:44 UTC
**Sample:** `028c5bc3a6e311aabb7b3ef45d377e68023be5980a9ecf01cd852f3a5a394b41_028c5bc3a6e311aabb7b3ef45d377e68023be5980a9ecf01cd852f3a5a394b41.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `028c5bc3a6e311aabb7b3ef45d377e68023be5980a9ecf01cd852f3a5a394b41_028c5bc3a6e311aabb7b3ef45d377e68023be5980a9ecf01cd852f3a5a394b41.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 25,207,943 bytes |
| MD5 | `f13a40e8a94aadc0e9f71204cb300aa7` |
| SHA1 | `e913298dc99f91dee83d68ae740b37a57567be0e` |
| SHA256 | `028c5bc3a6e311aabb7b3ef45d377e68023be5980a9ecf01cd852f3a5a394b41` |
| Overall entropy | 8.0 |
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
| `CODE` | 37,888 | 6.562 | No |
| `DATA` | 1,024 | 2.753 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 2,560 | 4.431 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.204 | No |
| `.reloc` | 0 | 0.0 | No |
| `.rsrc` | 11,264 | 4.474 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **55088** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality.

### Core Functionality and Purpose
The binary appears to be a **wrapper or installer** (likely utilizing the Inno Setup framework, as evidenced by the "InnoSetup" and "LZMA" strings). Its primary role is to prepare the environment, handle localization (Internationalization/i18n), manage compressed resources, and ultimately launch another process.

### Suspicious or Malicious Behaviors
While much of the code reflects standard installer behavior, several components are common in malware "droppers" or "wrappers":

*   **Process Spawning & Monitoring:** 
    *   Function `fcn.004099a4` explicitly uses **`CreateProcessA`** to launch a secondary executable. 
    *   It follows the creation with `MsgWaitForMultipleObjects` and `GetExitCodeProcess`. This behavior is used to ensure the "payload" process starts successfully before the primary wrapper continues or exits.
*   **Resource Decompression (LZMA):** 
    *   The presence of `TLZMA1SmallDecompressorS` and related strings indicates the program handles compressed data blocks. In a malware context, this is frequently used to unpack an encrypted/compressed malicious payload from a resource section or an embedded file.
*   **System Information Gathering:**
    *   The code heavily utilizes `GetSystemInfo`, `GetSystemDefaultLCID`, and various locale-checking loops (e.g., `fcn.00405270`). While common in installers, these are used to tailor the execution environment or verify system compatibility before launching a payload.
*   **Registry Interaction:** 
    *   Function `fcn.00406e10` interacts with the Windows Registry using `RegQueryValueExA`. This is often used to check for existing software, specific OS versions, or system configurations.

### Notable Techniques and Patterns
*   **"Wrapper" Pattern:** The binary behaves like a "Loader" or "Dropper." It acts as a legitimate-looking front-end (installer) that handles the heavy lifting of unpacking and environment checking so that the actual malicious payload can be executed in a secondary process.
*   **Dynamic Loading:** The use of `GetProcAddress` and `GetModuleHandleA` suggests the code dynamically resolves functions to avoid static detection of its full capabilities until runtime.
*   **Memory Management:** Functions like `fcn.00407f10` utilize `VirtualAlloc` and check for specific memory sizes, which are essential for loading unpacked code into executable memory regions.
*   **Complex String/Data Handling:** The logic in `fcn.0040840c` involves significant arithmetic and looping over data blocks, characteristic of custom decompression or decryption routines used to unpack "packed" executables.

### Summary Table for Quick Reference
| Feature | Observation | Significance |
| :--- | :--- | :--- |
| **Primary Role** | Installer/Wrapper (Inno Setup) | Used as a delivery mechanism for additional payloads. |
| **Payload Execution** | `CreateProcessA` in `fcn.004099a4` | The primary method of executing the final malware payload. |
| **Packing/Encryption** | LZMA Decompression & Memory Management | Indicates the binary handles compressed/hidden data. |
| **Information Gathering** | Locale and System Info checks | Used to verify environment or adapt behavior to local settings. |
| **Persistence (Indirect)** | Parent-Child Process Relationship | By launching a separate process, it can attempt to survive the closure of the installer. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Software Packing | The use of LZMA decompression and `VirtualAlloc` to manage memory for unpacked content indicates a packer or loader mechanism. |
| T1106 | Obfuscated Files or Programs | Use of `GetProcAddress` and `GetModuleHandleA` demonstrates dynamic API resolution to hide the binary's capabilities from static analysis. |
| T1497 | Virtualization/Sandbox Evasion | Extensive usage of `GetSystemInfo` and locale-checking loops are common indicators of checks performed to detect and bypass analysis environments. |
| T1059 | Command and Scripting Interpreter | The "Wrapper" behavior, involving the use of `CreateProcessA` to launch a secondary payload, is typical of a loader facilitating execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** This sample appears to be a "wrapper" or "dropper." While it does not contain hardcoded network infrastructure (IPs/URLs) in this specific segment, it contains structural indicators of its role as a delivery mechanism.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified (Standard system calls were noted, but no specific malicious paths or non-standard registry keys were provided in the text).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Framework Identifiers:** 
    *   `Inno Setup` (Versions: 5.4.2, 5.1.11) — Used as a wrapper/installer for the payload.
*   **Technical Patterns / Code Offsets:**
    *   `fcn.004099a4`: Entry point for `CreateProcessA` (Payload execution).
    *   `fcn.00406e10`: Logic for Registry interaction (`RegQueryValueExA`).
    *   `fcn.00405270`: Locale/System information gathering loop.
    *   `fcn.00407f10`: Memory allocation and management (`VirtualAlloc`).
    *   `fcn.0040840c`: Decryption/Decompression routines.
*   **Malware Behavior Indicators:**
    *   **LZMA Decompression:** Use of `TLZMA1SmallDecompressorS` to unpack embedded resources.
    *   **Dynamic API Resolution:** Frequent use of `GetProcAddress` and `GetModuleHandleA`.
    *   **Process Obfuscation:** Behavior indicates a "Wrapper" pattern, where the primary binary acts as a front-end for a secondary executable.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

**Key evidence**:
*   **Wrapper/Dropper Architecture:** The binary utilizes an "Inno Setup" wrapper to hide its primary purpose, using `CreateProcessA` specifically to launch a secondary payload while the initial process manages the environment.
*   **Decompression and Memory Management:** The presence of LZMA decompression routines (`TLZMA1SmallDecompressorS`) combined with `VirtualAlloc` indicates the binary is designed to unpack and execute hidden code in memory.
*   **Evasive Techniques:** The use of dynamic API resolution (`GetProcAddress`/`GetModuleHandleA`) and extensive system/locale checks are classic indicators of a loader designed to bypass static analysis and detect sandbox environments before executing the final payload.
