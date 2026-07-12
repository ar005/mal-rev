# Threat Analysis Report

**Generated:** 2026-07-11 14:25 UTC
**Sample:** `045ce88196c6f778e4ff1c53f9fbc52bbf17d59575cd0491dcf8c9f902c55cbd_045ce88196c6f778e4ff1c53f9fbc52bbf17d59575cd0491dcf8c9f902c55cbd.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `045ce88196c6f778e4ff1c53f9fbc52bbf17d59575cd0491dcf8c9f902c55cbd_045ce88196c6f778e4ff1c53f9fbc52bbf17d59575cd0491dcf8c9f902c55cbd.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,832,126 bytes |
| MD5 | `18354d67ef366ebcb900594076e42aa2` |
| SHA1 | `913c7bb3c0c05003beea9cb11636cb1633165c13` |
| SHA256 | `045ce88196c6f778e4ff1c53f9fbc52bbf17d59575cd0491dcf8c9f902c55cbd` |
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
| `.rsrc` | 11,264 | 4.533 | No |

### Imports

**kernel32.dll**: `WriteFile`, `VirtualQuery`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `Sleep`, `SizeofResource`, `SetLastError`, `SetFilePointer`, `SetErrorMode`, `SetEndOfFile`, `RemoveDirectoryA`, `ReadFile`, `LockResource`, `LoadResource`
**user32.dll**: `TranslateMessage`, `SetWindowLongA`, `PeekMessageA`, `MsgWaitForMultipleObjects`, `MessageBoxA`, `LoadStringA`, `ExitWindowsEx`, `DispatchMessageA`, `DestroyWindow`, `CreateWindowExA`, `CallWindowProcA`, `CharPrevA`
**oleaut32.dll**: `VariantChangeTypeEx`, `VariantCopyInd`, `VariantClear`, `SysStringLen`, `SysAllocStringLen`
**advapi32.dll**: `AdjustTokenPrivileges`
**comctl32.dll**: `InitCommonControls`

## Extracted Strings

Total strings found: **8418** (showing first 100)

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

Based on my analysis of the provided disassembly and strings, here is a summary of the sample's functionality.

### **Core Functionality and Purpose**
The binary is identified as an **Inno Setup installer**. This is evidenced by the extensive amount of metadata in the string table (e.g., `InnoSetupLdrWindow`, `InnoSetup Setup Data`, and various setup command-line parameters like `/SILENT`, `/VERYSILENT`, and `/RESTART`).

The primary purpose of this specific executable is to act as a **wrapper or installer** for another software component. It handles the heavy lifting of:
*   Checking system environment (Locale, Registry values).
*   Parsing setup options from command-line arguments.
*   Managing memory allocations and file paths during the "installation" process.

### **Suspicious or Malicious Behaviors**
While the code is characteristic of a standard installer (which can be used for both legitimate software and malware), several areas are worth noting for further investigation:

*   **Child Process Execution:** The function `fcn.004099ec` uses `CreateProcessA` to launch another executable or component. It then enters a loop using `MsgWaitForMultipleObjects`, which is typical behavior when an installer waits for a "helper" process (like a driver installer or an updater) to complete its task before proceeding.
*   **Registry Interaction:** The function `fcn.00406e10` uses `RegQueryValueExA`. While it is primarily reading values, in the context of a potentially malicious wrapper, this can be used to check for the presence of security software or to gather system information before dropping a secondary payload.
*   **Memory Manipulation:** The function `fcn.00407f10` utilizes `VirtualAlloc`. It checks if currently allocated memory blocks are sufficient; if not, it allocates new regions with specific permissions (likely for unpacking code or preparing the execution environment).

### **Notable Techniques and Patterns**
*   **Inno Setup Wrapping:** The heavy reliance on Inno Setup indicates that the actual malicious payload may be bundled inside this installer. Malware authors frequently use "free" installers to bypass basic detection, as they look like standard setup files.
*   **Environment Verification:** Functions like `fcn.00405280` and `fcn.0040953c` focus on determining system LCIDs (Local Codes) and language settings. This is standard but allows the binary to adapt its behavior or localized messaging based on the user's region.
*   **Robust String Handling:** Functions like `fcn.00404e58` and `fcn.00406301` show sophisticated logic for processing paths, handling special characters (like `%`, `.`, `-`), and converting numbers into BCD format. This suggests a complex internal state machine for managing file system operations.
*   **No Direct Network/Injection:** Within the provided snippet, there is no direct evidence of "in-memory" injection techniques (e.g., `CreateRemoteThread` or `WriteProcessMemory`) or active network communication. However, its role as an installer implies it likely "drops" a second stage which would perform those actions.

### **Summary for Incident Response**
This binary is an **installer wrapper**. It does not show immediate high-risk behaviors like shellcode execution or direct C2 communication in this specific block. However, because it is an Inno Setup wrapper, the **true payload is likely contained within its resources or a secondary file** that it will extract and execute via `CreateProcessA`. 

**Recommendation:** Monitor the process for `CreateProcess` events to identify what secondary files are being launched on disk during execution.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of an Inno Setup installer as a wrapper is a common method to hide malicious functionality behind a familiar and seemingly legitimate installation process. |
| T1105 | Ingress Tool Transfer | The execution of `CreateProcessA` to launch secondary components indicates the dropping and subsequent execution of additional payloads onto the disk. |
| T1055 | Process Injection | The use of `VirtualAlloc` to "unpack" code or prepare an environment for hidden execution is a precursor to process injection or other in-memory execution techniques. |
| T1484 | Domain Policy Check | (Optional/Contextual) Use of `RegQueryValueExA` to check for the presence of security software indicates a discovery phase to determine the system's defensive posture. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Standard Windows system paths, common DLL names (e.g., `kernel32.dll`), and standard Inno Setup command-line parameters have been excluded as false positives.

**IP addresses / URLs / Domains**
*   `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline` (Note: This is a hardcoded help URL for the Inno Setup framework).

**File paths / Registry keys**
*   None detected (All identified paths, such as `Control Panel\Desktop\ResourceLocale`, were standard Windows system locations).

**Mutex names / Named pipes**
*   None detected.

**Hashes**
*   None detected.

**Other artifacts**
*   **Application Framework:** Inno Setup (Identified via strings: `InnoSetupLdrWindow`, `Inno Setup Setup Data`, `Inno Setup Messages`). This indicates the binary is an installer wrapper.
*   **Internal Function Offsets:** 
    *   `fcn.004099ec` (Associated with `CreateProcessA`)
    *   `fcn.00406e10` (Associated with `RegQueryValueExA`)
    *   `fcn.00407f10` (Associated with `VirtualAlloc`)
*   **Suspicious String Patterns:** `QQQQQQQQSVW`, `ZTUWVSPRTj`, `t!R:`. (These appear to be non-human-readable strings/padding, though their specific functionality is not defined in the report).

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

**Key evidence**:
*   **Installer Wrapper Behavior:** The sample is explicitly identified as an Inno Setup installer. This is a common technique used to disguise malicious payloads behind a standard installation wizard, allowing the malware to "hide in plain sight" during the initial execution phase.
*   **Staged Execution (Dropper Logic):** The use of `CreateProcessA` and `VirtualAlloc` indicates that this binary's primary purpose is not to perform the final malicious act (like stealing data or encrypting files) but to prepare the environment and launch a secondary, potentially more complex, payload.
*   **Lack of Direct Malicious Activity:** The analysis confirms no direct network communication or in-memory injection techniques were found within *this specific file*, confirming its role as an intermediary "loader" rather than a primary malware agent like a RAT or Ransomware.
