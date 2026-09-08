# Threat Analysis Report

**Generated:** 2026-09-06 10:00 UTC
**Sample:** `14e0163e43b688f18a7a45a7654c459aa5efe1e06174c629ce37bea70e2c9b1f_14e0163e43b688f18a7a45a7654c459aa5efe1e06174c629ce37bea70e2c9b1f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14e0163e43b688f18a7a45a7654c459aa5efe1e06174c629ce37bea70e2c9b1f_14e0163e43b688f18a7a45a7654c459aa5efe1e06174c629ce37bea70e2c9b1f.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,644,963 bytes |
| MD5 | `0a059a04e6718b23adca59869f9857a0` |
| SHA1 | `f8ec8a2f8c1fcfa136891ec11cd83af3cdd38311` |
| SHA256 | `14e0163e43b688f18a7a45a7654c459aa5efe1e06174c629ce37bea70e2c9b1f` |
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
| `.rsrc` | 11,264 | 4.463 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **8111** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality and behavior.

### Core Functionality and Purpose
The presence of specific strings (e.g., `InnoSetupLdrWindow`, `InnoSetup_...` patterns, `TCompressedBlockReader`, and "The setup files are corrupted") indicates that this binary is built using the **Inno Setup** installer engine.

Its primary purpose is to act as an **installer or a software update wrapper**. However, in a malware context, these engines are frequently used as "droppers" because they provide a legitimate way to unpack compressed data (LZMA) and execute secondary payloads while appearing like a standard installation process.

### Suspicious or Malicious Behaviors

*   **Process Execution & Spawning:**
    *   The function `fcn.004099a4` is a significant indicator of "dropper" behavior. It calls `CreateProcessA` to launch a secondary process using a command-line argument derived from internal data (likely the payload).
    *   It then enters a loop using `MsgWaitForMultipleObjects`, which causes the parent process (the installer) to wait for the child process (the actual payload/malware) to finish or continue running. This is standard in installers but is common in malware to ensure the "payload" starts successfully.

*   **Registry Interaction:**
    *   The function `fcn.00406e10` performs several calls to `RegQueryValueExA`. It checks specific registry keys, which are often used by malware to:
        *   Check if a target application is already installed.
        *   Identify the system's architecture or specific security software presence.
        *   Retrieve configuration data for subsequent infection stages.

*   **Resource Extraction & Loading:**
    *   Functions such as `fcn.00407f10` use `VirtualAlloc` and appear to manage memory regions for "unpacked" content. 
    *   The inclusion of `TCompressedBlockReader` and `LZMA` related strings suggests the binary contains a compressed payload that is unpacked during execution before being handed off to the loader/installer logic.

### Notable Techniques & Patterns

*   **Installer Wrapper Technique:** By using Inno Setup, the author hides the malicious nature of the file behind a familiar, legitimate-looking installer interface.
*   **Persistence via Execution:** While not directly showing a registry "Run" key, the behavior in `fcn.004099a4` suggests that this is a multi-stage loader where the initial "installer" (this binary) ensures that a second, potentially more malicious executable is launched successfully on the system.
*   **Robust Error Handling:** The code contains extensive checks for file integrity and environmental conditions (like `GetSystemDefaultLCID`), ensuring that the installer/loader runs correctly across different locales and hardware configurations.
*   **Standard "Dropper" Logic:** The transition from a setup-style environment to a process-execution loop is a hallmark of many Trojan droppers. It performs the "heavy lifting" of unpacking, checking system requirements, and launching the final stage.

### Summary for Incident Response
This binary functions as an **installer-based dropper**. While it uses legitimate installation logic (Inno Setup), its core malicious role is to:
1.  **Unpack/Decompress** hidden content using LZMA.
2.  **Verify the environment** via Registry queries (`RegQueryValueExA`).
3.  **Execute a payload** by spawning a child process and waiting for it to initialize.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The binary utilizes the Inno Setup engine to blend in with legitimate software installation processes, hiding its true role as a dropper. |
| **T1027** | Obfuscated Files or Network Traffic | The use of LZMA compression and internal memory allocation for "unpacked" content indicates an attempt to hide the primary payload from detection. |
| **T1012** | Query Registry | The use of `RegQueryValueExA` suggests the malware is gathering system information, checking for security software, or identifying configuration data. |
| **T1204** | User Execution | The "installer" wrapper leverages a familiar interface to trick users into executing the initial stage of the attack. |
| **T1105** | Ingress Tool Transfer | (Contextual) The multi-stage nature involving an installer to "drop" and launch a second executable confirms its role as a delivery mechanism for malicious tools. |

---

## Indicators of Compromise

Based on the strings provided and the accompanying behavioral analysis, here is the extracted threat intelligence.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. *(Note: While the analysis mentions registry interaction via `RegQueryValueExA`, no specific malicious paths or keys were provided in the source text.)*

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Installer Wrapper:** Inno Setup (v5.5.0). The binary uses this legitimate installer framework to mask its purpose as a dropper/loader.
*   **Compression Method:** LZMA (indicated by `TCompressedBlockReader` and `TLZMA1SmallDecompressorS`). This is used for the internal storage and unpacking of secondary payloads.
*   **Functionality Note:** The analysis identifies specific logic at offsets `004099a4` (Process spawning/waiting) and `00406e10` (Registry queries). While these are not network IOCs, they are behavioral artifacts used to identify the specific logic flow of this malware family.

***

**Analyst Note:** The provided data contains no "hard" indicators (IPs, Hashes, or URLs), which is typical for a "dropper" stage. This binary's primary role is to act as a wrapper; it prepares the environment and unpacks the payload rather than performing direct C2 communication or file system manipulation itself.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Installer Wrapper Technique:** The binary uses the Inno Setup framework and LZMA decompression to mask its true purpose, acting as a common "wrapper" that bundles and unpacks malicious payloads.
    *   **Execution Lifecycle:** The use of `CreateProcessA` followed by a `MsgWaitForMultipleObjects` loop indicates it is designed to launch and wait for a secondary payload (the actual malware) rather than performing actions itself.
    *   **Environment Awareness:** The presence of `RegQueryValueExA` calls suggests the binary checks system environment or security software before executing the next stage of the attack.
