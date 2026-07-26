# Threat Analysis Report

**Generated:** 2026-07-23 13:02 UTC
**Sample:** `09b8759847f39686f345964794d4261529b70f4f0558e2b6741af7bfc4156301_09b8759847f39686f345964794d4261529b70f4f0558e2b6741af7bfc4156301.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `09b8759847f39686f345964794d4261529b70f4f0558e2b6741af7bfc4156301_09b8759847f39686f345964794d4261529b70f4f0558e2b6741af7bfc4156301.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 5,640,704 bytes |
| MD5 | `65bce4af983418a672d19245aa2fecf5` |
| SHA1 | `ac6c7935731a8235f94519345292d7c7366bda9f` |
| SHA256 | `09b8759847f39686f345964794d4261529b70f4f0558e2b6741af7bfc4156301` |
| Overall entropy | 5.947 |
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
| `CODE` | 478,720 | 6.538 | No |
| `DATA` | 7,680 | 4.496 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 9,216 | 5.023 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.201 | No |
| `.reloc` | 34,304 | 6.632 | No |
| `.rsrc` | 5,109,248 | 5.71 | No |

### Imports

**kernel32.dll**: `Sleep`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WinHelpA`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `ShowCursor`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `GetErrorInfo`, `SysFreeString`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**gdi32.dll**: `UnrealizeObject`, `TextOutA`, `StretchBlt`, `SetWindowOrgEx`, `SetWinMetaFileBits`, `SetViewportOrgEx`, `SetTextColor`, `SetTextAlign`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetEnhMetaFileBits`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoUninitialize`, `CoInitialize`
**comctl32.dll**: `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_SetDragCursorImage`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`

## Extracted Strings

Total strings found: **7833** (showing first 100)

```
This program must be run under Win32
$7
.idata
.rdata
P.reloc
P.rsrc
Boolean
Smallint
Integer
Cardinal
Double
Currency
String

WideString
Variant
TObjectP
TObjectD
System

IInterface
System
TInterfacedObject
TBoundArray
Systemx
	TDateTime
YZ]_^[
C;D$v
D$+D$
YZ]_^[
_^[YY]
YZ]_^[
tHt Ht.
:
u0Nt
~KxI[)
                                                                
SOFTWARE\Borland\Delphi\RTL
FPUMaskValue
_^[YY]
r;pt
:
u	@B
YZXtm1
ZTUWVSPRTj
t!R:
t
t-Rf;
t f;J
tVSVWU
t-Rf;
t f;J
<
t"<t
<t$<t3<
<
t%<t><tQ<t\<
t@h\@
kernel32.dll
GetLongPathNameA
Software\Borland\Locales
Software\Borland\Delphi\Locales
_^[YY]

odSelected
odGrayed
odDisabled	odChecked	odFocused	odDefault
odHotLight
odInactive	odNoAccelodNoFocusRectodReserved1odReserved2
odComboBoxEdit
Windows
TOwnerDrawState
Magellan MSWHEEL
MouseZ
MSWHEEL_ROLLMSG
MSH_WHEELSUPPORT_MSG
MSH_SCROLL_LINES_MSG
	Exception
EHeapException
EOutOfMemory
EInOutError
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeError
EIntOverflow

EMathError

EInvalidOp
EZeroDivide<~@
	EOverflow

EUnderflow
EInvalidPointerH
EInvalidCast
EConvertError
EAccessViolation

EPrivilege
EStackOverflow
	EControlC
EVariantError
EAssertionFailed
EAbstractError
EIntfCastError
EOSError
ESafecallException
SysUtils
SysUtils
TThreadLocalCounter
$TMultiReadExclusiveWriteSynchronizer
<*t"<0r=<9w9i
INFNAN
$*@@@*$@@@$ *@@* $@@($*)@-$*@@$-*@@$*-@@(*$)@-*$@@*-$@@*$-@@-* $@-$ *@* $-@$ *-@$ -*@*- $@($ *)(* $)
<'t$<"t 
<#t&<0t%<.t,<,t3<'t5<"t1<Et:<et6<;tF
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00403a50` | `0x403a50` | 4113 | ✓ |
| `fcn.00447d5c` | `0x447d5c` | 2312 | ✓ |
| `fcn.00447454` | `0x447454` | 2280 | ✓ |
| `fcn.0040a9c8` | `0x40a9c8` | 1921 | ✓ |
| `fcn.00455b08` | `0x455b08` | 1750 | ✓ |
| `fcn.0045c460` | `0x45c460` | 1678 | ✓ |
| `fcn.00427808` | `0x427808` | 1633 | ✓ |
| `fcn.004138bc` | `0x4138bc` | 1362 | ✓ |
| `fcn.00413194` | `0x413194` | 1335 | ✓ |
| `fcn.004497a0` | `0x4497a0` | 1183 | ✓ |
| `fcn.00428bec` | `0x428bec` | 1131 | ✓ |
| `fcn.00410834` | `0x410834` | 1097 | ✓ |
| `fcn.00469690` | `0x469690` | 1089 | ✓ |
| `fcn.004112f8` | `0x4112f8` | 1088 | ✓ |
| `fcn.00439b98` | `0x439b98` | 1085 | ✓ |
| `entry0` | `0x475c54` | 1019 | ✓ |
| `fcn.00472f68` | `0x472f68` | 1018 | ✓ |
| `fcn.0043e154` | `0x43e154` | 978 | ✓ |
| `fcn.00412ae0` | `0x412ae0` | 965 | ✓ |
| `fcn.0042c67c` | `0x42c67c` | 947 | ✓ |
| `fcn.0042f14c` | `0x42f14c` | 905 | ✓ |
| `fcn.00457784` | `0x457784` | 902 | ✓ |
| `fcn.00411e08` | `0x411e08` | 885 | ✓ |
| `fcn.004628f4` | `0x4628f4` | 874 | ✓ |
| `fcn.00450efc` | `0x450efc` | 852 | ✓ |
| `fcn.00412578` | `0x412578` | 846 | ✓ |
| `fcn.004118f4` | `0x4118f4` | 836 | ✓ |
| `fcn.00414e30` | `0x414e30` | 834 | ✓ |
| `fcn.0040931e` | `0x40931e` | 828 | ✓ |
| `fcn.0040b4ac` | `0x40b4ac` | 795 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00403a50.c`](code/fcn.00403a50.c)
- [`code/fcn.0040931e.c`](code/fcn.0040931e.c)
- [`code/fcn.0040a9c8.c`](code/fcn.0040a9c8.c)
- [`code/fcn.0040b4ac.c`](code/fcn.0040b4ac.c)
- [`code/fcn.00410834.c`](code/fcn.00410834.c)
- [`code/fcn.004112f8.c`](code/fcn.004112f8.c)
- [`code/fcn.004118f4.c`](code/fcn.004118f4.c)
- [`code/fcn.00411e08.c`](code/fcn.00411e08.c)
- [`code/fcn.00412578.c`](code/fcn.00412578.c)
- [`code/fcn.00412ae0.c`](code/fcn.00412ae0.c)
- [`code/fcn.00413194.c`](code/fcn.00413194.c)
- [`code/fcn.004138bc.c`](code/fcn.004138bc.c)
- [`code/fcn.00414e30.c`](code/fcn.00414e30.c)
- [`code/fcn.00427808.c`](code/fcn.00427808.c)
- [`code/fcn.00428bec.c`](code/fcn.00428bec.c)
- [`code/fcn.0042c67c.c`](code/fcn.0042c67c.c)
- [`code/fcn.0042f14c.c`](code/fcn.0042f14c.c)
- [`code/fcn.00439b98.c`](code/fcn.00439b98.c)
- [`code/fcn.0043e154.c`](code/fcn.0043e154.c)
- [`code/fcn.00447454.c`](code/fcn.00447454.c)
- [`code/fcn.00447d5c.c`](code/fcn.00447d5c.c)
- [`code/fcn.004497a0.c`](code/fcn.004497a0.c)
- [`code/fcn.00450efc.c`](code/fcn.00450efc.c)
- [`code/fcn.00455b08.c`](code/fcn.00455b08.c)
- [`code/fcn.00457784.c`](code/fcn.00457784.c)
- [`code/fcn.0045c460.c`](code/fcn.0045c460.c)
- [`code/fcn.004628f4.c`](code/fcn.004628f4.c)
- [`code/fcn.00469690.c`](code/fcn.00469690.c)
- [`code/fcn.00472f68.c`](code/fcn.00472f68.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, I have updated and expanded the analysis. The new data provides more technical depth regarding how the application handles internal logic and its interaction with the operating system.

### Updated Analysis Summary

#### 1. Core Functionality and Purpose (Expanded)
The initial assessment that this is a **Delphi/Pascal-based GUI application** remains accurate. However, chunk 2 reveals deeper layers of how that GUI is managed:
*   **Extensive Dispatcher Logic:** Functions like `fcn.00412ae0` and `fcn.00412578` utilize large "switch tables." In Delphi, this is common for handling **Message Loops** or **Component Classes**. It allows the application to take a single input (like a mouse click or keypress) and route it to hundreds of different internal UI handlers.
*   **Complex Geometry & Clipping:** The logic in `fcn.00457784` involves frequent use of `OffsetRect` and checks for coordinate overlaps. This confirms the presence of a sophisticated custom-drawn UI, likely handling complex items like list views or nested panels.

#### 2. Suspicious or Malicious Behaviors (Updated)
While no direct "malware" actions (like file deletion or remote execution) were seen in chunk 1, **chunk 2 introduces a significant red flag for an analyst:**

*   **Manual Dynamic Linker (API Obfuscation):** Function `fcn.0042c67c` is highly noteworthy. It performs a large sequence of:
    1.  `LoadLibraryA`
    2.  `GetProcAddress` calls for over 30 different functions from a single DLL.
    *   **Analysis:** This is a classic technique used to **hide the Import Address Table (IAT)**. By manually resolving addresses at runtime, the developer can hide which system APIs the program actually uses until it is already running in memory. In many cases, this is done to hide "noisy" functions like `WriteProcessMemory`, `CreateRemoteThread`, or networking functions that would alert automated scanners.
*   **Data Obfuscation/Deciphering:** Function `fcn.0042f14c` contains a massive switch table that maps many inputs to specific values. This is often characteristic of **custom encoding/decoding routines** for strings or resources, used to hide internal configuration or hardcoded indicators (like C2 addresses) from static string analysis.

#### 3. Notable Techniques and Patterns
*   **Code Bloat as a Shield:** The sheer volume of "wrapper" code (the switch tables in `fcn.004118f4` and `fcn.00412ae0`) functions as a "smokescreen." For an analyst, this means that the actual "malicious" logic is likely buried deep within these nested structures or hidden behind the dynamically resolved pointers from `GetProcAddress`.
*   **Complex State Management:** The variables in `fcn.00457784` suggest a state machine. This is common in games and complex software, but also used in **malware loaders** to manage different stages of an infection (e.g., "Is the environment safe?", "Is the sample being debugged?").
*   **Standard Library Padding:** The code still shows heavy use of Pascal-standard libraries (`TObject`, `SysUtils`). This reinforces the idea that if this is a Trojan, it is wrapped in a very thick layer of legitimate-looking Delphi framework code.

---

### Summary Conclusion (Updated)

The analysis confirms that this binary is highly complex and likely uses **layered obfuscation**. 

While the first chunk suggested a heavy reliance on GDI/Graphics as a potential "distraction" or "wrapper," the second chunk reveals a sophisticated mechanism for **API Obfuscation** (`GetProcAddress` chain). This indicates that while much of the code is indeed related to UI rendering, there is a clear design choice to hide specific functionalities from static analysis.

**Analyst's Note:** The presence of the manual `GetProcAddress` loop in `fcn.0042c67c` identifies this as a high-priority area for dynamic analysis. An analyst should hook `GetProcAddress` during execution to see which specific functions are being resolved, as those will reveal the "true" capabilities of the software (e.g., process injection, keylogging, or network communication).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or System Tools | The use of a manual `GetProcAddress` loop to hide the Import Address Table (IAT) and large switch tables for decoding strings/resources are clear indicators of an effort to evade static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted list of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   *Note: The following were identified in the strings but are excluded as they are standard Delphi/Borland software library paths.*
*   `SOFTWARE\Borland\Delphi\RTL` (Excluded - Standard Library)
*   `Software\Borland\Locales` (Excluded - Standard path)
*   `Software\Borland\Delphi\Locales` (Excluded - Standard path)

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **API Obfuscation Technique:** Use of `LoadLibraryA` and a long chain of `GetProcAddress` calls (identified in `fcn.0042c67c`) to resolve over 30 functions from a single DLL at runtime. This is used to hide the Import Address Table (IAT) and conceal "noisy" functions like those related to network communication or process injection.
*   **String/Data Obfuscation:** Use of large switch tables (`fcn.0042f14c`) for decoding internal strings or hardcoded values, likely used to hide C2 infrastructure or other indicators from static analysis.
*   **Delphi Framework Usage:** Extensive use of Delphi-specific libraries (`TObject`, `SysUtils`, `Variants`), indicating the tool is built using the Delphi/Pascal environment.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family:** Custom
2. **Malware type:** Loader
3. **Confidence:** Medium
4. **Key evidence:**
    * **API Obfuscation:** The use of a `GetProcAddress` loop to resolve over 30 functions at runtime is a classic technique used to hide "noisy" Windows APIs (e.g., those related to process injection or network communication) from static analysis tools.
    * **Data/String Masking:** The presence of large switch tables for decoding internal strings and resources indicates an intentional effort to hide C2 infrastructure, configuration data, or other indicators of compromise (IOCs).
    * **"Smokescreen" Design:** The combination of a complex Delphi-based GUI and heavy code bloat suggests the malware is designed to look like legitimate software while shielding malicious functionality behind layers of common library code.
