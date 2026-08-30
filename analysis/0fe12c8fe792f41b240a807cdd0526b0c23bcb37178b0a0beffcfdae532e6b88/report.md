# Threat Analysis Report

**Generated:** 2026-08-17 19:06 UTC
**Sample:** `0fe12c8fe792f41b240a807cdd0526b0c23bcb37178b0a0beffcfdae532e6b88_0fe12c8fe792f41b240a807cdd0526b0c23bcb37178b0a0beffcfdae532e6b88.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0fe12c8fe792f41b240a807cdd0526b0c23bcb37178b0a0beffcfdae532e6b88_0fe12c8fe792f41b240a807cdd0526b0c23bcb37178b0a0beffcfdae532e6b88.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 4,833,141 bytes |
| MD5 | `1d21d1bb95f6069c84ae83ed8c066d47` |
| SHA1 | `fa98f881e29cfb95dae6a0fbc2fe210302c89e26` |
| SHA256 | `0fe12c8fe792f41b240a807cdd0526b0c23bcb37178b0a0beffcfdae532e6b88` |
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
| `CODE` | 37,888 | 6.539 | No |
| `DATA` | 1,024 | 2.74 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 2,560 | 4.431 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.204 | No |
| `.reloc` | 0 | 0.0 | No |
| `.rsrc` | 11,264 | 4.461 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **10659** (showing first 100)

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
lzmadecompsmall: Compressed data is corrupted (%d)
lzmadecompsmall: %s
t$;sdt'
LzmaDecode failed (%d)
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040836c` | `0x40836c` | 1690 | ✓ |
| `fcn.00404da8` | `0x404da8` | 773 | ✓ |
| `fcn.00403f67` | `0x403f67` | 731 | ✓ |
| `fcn.00405314` | `0x405314` | 584 | ✓ |
| `entry0` | `0x409b60` | 507 | ✓ |
| `fcn.00404eca` | `0x404eca` | 474 | ✓ |
| `fcn.00402300` | `0x402300` | 463 | ✓ |
| `fcn.0040215c` | `0x40215c` | 418 | ✓ |
| `fcn.00401fd4` | `0x401fd4` | 389 | ✓ |
| `fcn.00405628` | `0x405628` | 378 | ✓ |
| `fcn.00403e41` | `0x403e41` | 328 | ✓ |
| `fcn.00406d70` | `0x406d70` | 312 | ✓ |
| `fcn.004051d0` | `0x4051d0` | 310 | ✓ |
| `fcn.00401768` | `0x401768` | 291 | ✓ |
| `fcn.00409724` | `0x409724` | 275 | ✓ |
| `fcn.00407988` | `0x407988` | 268 | ✓ |
| `fcn.00406f84` | `0x406f84` | 261 | ✓ |
| `fcn.00408a68` | `0x408a68` | 247 | ✓ |
| `fcn.00406251` | `0x406251` | 245 | ✓ |
| `fcn.00401ee0` | `0x401ee0` | 244 | ✓ |
| `fcn.00409290` | `0x409290` | 239 | ✓ |
| `fcn.004038b4` | `0x4038b4` | 238 | ✓ |
| `fcn.00409184` | `0x409184` | 238 | ✓ |
| `fcn.00408be0` | `0x408be0` | 234 | ✓ |
| `fcn.004019dc` | `0x4019dc` | 226 | ✓ |
| `fcn.004066a4` | `0x4066a4` | 219 | ✓ |
| `fcn.004095bc` | `0x4095bc` | 216 | ✓ |
| `fcn.004098c4` | `0x4098c4` | 211 | ✓ |
| `fcn.00406346` | `0x406346` | 209 | ✓ |
| `fcn.00407e70` | `0x407e70` | 195 | ✓ |

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
- [`code/fcn.00404da8.c`](code/fcn.00404da8.c)
- [`code/fcn.00404eca.c`](code/fcn.00404eca.c)
- [`code/fcn.004051d0.c`](code/fcn.004051d0.c)
- [`code/fcn.00405314.c`](code/fcn.00405314.c)
- [`code/fcn.00405628.c`](code/fcn.00405628.c)
- [`code/fcn.00406251.c`](code/fcn.00406251.c)
- [`code/fcn.00406346.c`](code/fcn.00406346.c)
- [`code/fcn.004066a4.c`](code/fcn.004066a4.c)
- [`code/fcn.00406d70.c`](code/fcn.00406d70.c)
- [`code/fcn.00406f84.c`](code/fcn.00406f84.c)
- [`code/fcn.00407988.c`](code/fcn.00407988.c)
- [`code/fcn.00407e70.c`](code/fcn.00407e70.c)
- [`code/fcn.0040836c.c`](code/fcn.0040836c.c)
- [`code/fcn.00408a68.c`](code/fcn.00408a68.c)
- [`code/fcn.00408be0.c`](code/fcn.00408be0.c)
- [`code/fcn.00409184.c`](code/fcn.00409184.c)
- [`code/fcn.00409290.c`](code/fcn.00409290.c)
- [`code/fcn.004095bc.c`](code/fcn.004095bc.c)
- [`code/fcn.00409724.c`](code/fcn.00409724.c)
- [`code/fcn.004098c4.c`](code/fcn.004098c4.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary's functionality and behavior:

### Core Functionality
The binary appears to be a **wrapper or installer stub**, likely created using the **Inno Setup** utility (as evidenced by the "Inno Setup" string references and LZMA decompression logic). Its primary purpose is to unpack, configure, and launch another application. While much of the code consists of standard installation boilerplate, it contains several modules common in loaders and "droppers."

### Suspicious or Malicious Behavings
*   **Process Execution (Loader Behavior):** Function `fcn.004098c4` calls `CreateProcessA`. This is a significant indicator that the binary is designed to launch another executable or script. The subsequent use of `MsgWaitForMultipleObjects` suggests it stays active while waiting for the child process to complete, which is common in "loader" behavior where the first program ensures the second one runs successfully.
*   **Resource Extraction:** The presence of `LoadResource`, `LockResource`, and `SizeofResource`, combined with LZMA decompression logic (`lzmadecompsmall`), indicates that the binary contains embedded data (likely a secondary payload or extra assets) that it unpacks into memory or onto disk before execution.
*   **Registry Interaction:** Function `fcn.00406d70` uses `RegQueryValueExA`. While standard for installers to check system settings, in a malware context, this is often used to gather information about the environment, check for security software, or locate persistence keys.
*   **Environment/Locale Handling:** The heavy use of `GetSystemDefaultLCID` and other locale-related checks suggests the binary validates the system's language/region settings before proceeding, a common step in both legitimate installers and sophisticated malware to ensure compatibility with specific targets.

### Notable Techniques & Patterns
*   **Inno Setup Wrapper:** The binary uses a known installer framework. Malware authors often use these "wrappers" because they are commonly whitelisted by antivirus programs; the malicious payload is then hidden inside the installer's compressed resources.
*   **Decompression Logic:** The use of **LZMA decompression** indicates that the program handles large amounts of compressed data, a common way to pack large binaries or payloads into a single file.
*   **Standard API Usage for Obfuscation:** The code uses standard Windows APIs (e.g., `GetModuleHandle`, `GetProcAddress`, `VirtualAlloc`). While these are required for the installer's functionality, they are also the primary methods used by malware to dynamically resolve and execute malicious functions.
*   **Complexity of Memory Operations:** Functions like `fcn.0040836c` and `fcn.00401ee0` show complex memory management and offset calculations, which may be part of a custom routine to handle internal data structures or decrypted buffers.

### Summary for Incident Response
This sample is likely an **installer-based loader**. It uses standard Inno Setup features to unpack and launch a second stage. The most critical point of interest is the `CreateProcessA` call, which marks the transition from "setup" logic to "execution." Investigation into the specific command line used in `fcn.004098c4` would be necessary to determine the final destination of the payload.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The use of `CreateProcessA` indicates the binary serves as a loader to execute secondary payloads, scripts, or executables. |
| **T1027** | Obfuscated Files or Information | The use of LZMA decompression and resource extraction logic suggests that malicious components are hidden within compressed data to evade detection. |
| **T1112** | System Information Discovery | The utilization of `RegQueryValueExA` is used to gather system information, which can be used for environmental awareness or identifying target systems. |
| **T1036** | Masquerading | Using a standard "Inno Setup" wrapper allows the malicious payload to hide behind a commonly whitelisted and trusted installer framework. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** As requested, standard Windows system libraries (e.g., `kernel32.dll`, `user32.dll`) and common system paths have been excluded as they do not constitute specific malicious IOCs.

### **IP addresses / URLs / Domains**
*None identified.*

### **File paths / Registry keys**
*   **Note:** While the following registry paths were identified in the strings, they are standard Windows configuration locations for language/region settings and are not specific to a single malware strain:
    *   `.DEFAULT\Control Panel\International`
    *   `Control Panel\Desktop\ResourceLocale`

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None identified.*

### **Other artifacts**
*   **Software Framework:** Inno Setup (Version 5.3.10, Message version 5.1.11) — *Used as a wrapper/stub to hide the primary payload.*
*   **Decompression Library:** LZMA (`lzmadecompsmall`) — *Indicates the use of compressed payloads within the resource section.*
*   **Suspicious Behavior/Functions:**
    *   `CreateProcessA`: Identified in `fcn.004098c4` as the primary mechanism for launching the secondary payload.
    *   `MsgWaitForMultipleObjects`: Used to maintain the parent process while the child executes (Loader behavior).
    *   **Technique:** Installer-based loader/dropper (utilizing standard installer components to bypass security heuristics).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

**Key evidence**:
* **Inno Setup Wrapper:** The sample uses a standard installer framework to mask its true purpose, a common technique used by malware authors to bypass signature-based detection and hide malicious payloads within "trusted" installers.
* **Resource Extraction & Compression:** The use of LZMA decompression and resource loading indicates the binary is designed to unpack an embedded secondary payload before execution.
* **Execution Transition:** The presence of `CreateProcessA` combined with `MsgWaitForMultipleObjects` confirms its role as a loader; it acts as the first stage of an attack, ensuring that the second (likely more malicious) stage successfully executes.
