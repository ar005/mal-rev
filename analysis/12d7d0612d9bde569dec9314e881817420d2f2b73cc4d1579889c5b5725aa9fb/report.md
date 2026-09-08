# Threat Analysis Report

**Generated:** 2026-08-31 20:29 UTC
**Sample:** `12d7d0612d9bde569dec9314e881817420d2f2b73cc4d1579889c5b5725aa9fb_12d7d0612d9bde569dec9314e881817420d2f2b73cc4d1579889c5b5725aa9fb.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12d7d0612d9bde569dec9314e881817420d2f2b73cc4d1579889c5b5725aa9fb_12d7d0612d9bde569dec9314e881817420d2f2b73cc4d1579889c5b5725aa9fb.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 4,393,472 bytes |
| MD5 | `947dfcf02dcdef7dccccd944f7bde97c` |
| SHA1 | `8f65e5c5de4f909165dde1d1d928e5d10620b081` |
| SHA256 | `12d7d0612d9bde569dec9314e881817420d2f2b73cc4d1579889c5b5725aa9fb` |
| Overall entropy | 6.997 |
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
| `CODE` | 481,792 | 6.552 | No |
| `DATA` | 9,728 | 4.433 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 9,216 | 4.882 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.201 | No |
| `.reloc` | 39,424 | 6.603 | No |
| `.rsrc` | 3,851,776 | 6.863 | No |

### Imports

**kernel32.dll**: `Sleep`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WinHelpA`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `ShowCursor`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `GetErrorInfo`, `SysFreeString`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**gdi32.dll**: `WidenPath`, `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`, `SelectPalette`, `SelectObject`
**ole32.dll**: `CoUninitialize`, `CoInitialize`
**comctl32.dll**: `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_SetDragCursorImage`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`

## Extracted Strings

Total strings found: **14361** (showing first 100)

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
TObjectl
TObject`
System

IInterface
System
TInterfacedObject
TBoundArray
System
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
EAbort
EHeapException
EOutOfMemory
EInOutErrorh}@
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeError(
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
| `fcn.00403ab4` | `0x403ab4` | 4221 | ✓ |
| `fcn.00447cdc` | `0x447cdc` | 2312 | ✓ |
| `fcn.004473d4` | `0x4473d4` | 2280 | ✓ |
| `entry0` | `0x47681c` | 2098 | ✓ |
| `fcn.0040ad68` | `0x40ad68` | 1921 | ✓ |
| `fcn.004559f8` | `0x4559f8` | 1750 | ✓ |
| `fcn.00428044` | `0x428044` | 1633 | ✓ |
| `fcn.00413e8c` | `0x413e8c` | 1362 | ✓ |
| `fcn.00413764` | `0x413764` | 1335 | ✓ |
| `fcn.00449720` | `0x449720` | 1183 | ✓ |
| `fcn.00429428` | `0x429428` | 1131 | ✓ |
| `fcn.00410e04` | `0x410e04` | 1097 | ✓ |
| `fcn.004118c8` | `0x4118c8` | 1088 | ✓ |
| `fcn.00439b18` | `0x439b18` | 1085 | ✓ |
| `fcn.00414fe0` | `0x414fe0` | 1053 | ✓ |
| `fcn.00473ca4` | `0x473ca4` | 1018 | ✓ |
| `fcn.0043e0d4` | `0x43e0d4` | 978 | ✓ |
| `fcn.004130b0` | `0x4130b0` | 965 | ✓ |
| `fcn.0042cf0c` | `0x42cf0c` | 947 | ✓ |
| `fcn.0042f0d8` | `0x42f0d8` | 905 | ✓ |
| `fcn.00457674` | `0x457674` | 902 | ✓ |
| `fcn.004123d8` | `0x4123d8` | 885 | ✓ |
| `fcn.00450e7c` | `0x450e7c` | 852 | ✓ |
| `fcn.00412b48` | `0x412b48` | 846 | ✓ |
| `fcn.00411ec4` | `0x411ec4` | 836 | ✓ |
| `fcn.00416028` | `0x416028` | 834 | ✓ |
| `fcn.004094f2` | `0x4094f2` | 828 | ✓ |
| `fcn.0040b84c` | `0x40b84c` | 795 | ✓ |
| `fcn.00458204` | `0x458204` | 784 | ✓ |
| `fcn.004207c8` | `0x4207c8` | 763 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00403ab4.c`](code/fcn.00403ab4.c)
- [`code/fcn.004094f2.c`](code/fcn.004094f2.c)
- [`code/fcn.0040ad68.c`](code/fcn.0040ad68.c)
- [`code/fcn.0040b84c.c`](code/fcn.0040b84c.c)
- [`code/fcn.00410e04.c`](code/fcn.00410e04.c)
- [`code/fcn.004118c8.c`](code/fcn.004118c8.c)
- [`code/fcn.00411ec4.c`](code/fcn.00411ec4.c)
- [`code/fcn.004123d8.c`](code/fcn.004123d8.c)
- [`code/fcn.00412b48.c`](code/fcn.00412b48.c)
- [`code/fcn.004130b0.c`](code/fcn.004130b0.c)
- [`code/fcn.00413764.c`](code/fcn.00413764.c)
- [`code/fcn.00413e8c.c`](code/fcn.00413e8c.c)
- [`code/fcn.00414fe0.c`](code/fcn.00414fe0.c)
- [`code/fcn.00416028.c`](code/fcn.00416028.c)
- [`code/fcn.004207c8.c`](code/fcn.004207c8.c)
- [`code/fcn.00428044.c`](code/fcn.00428044.c)
- [`code/fcn.00429428.c`](code/fcn.00429428.c)
- [`code/fcn.0042cf0c.c`](code/fcn.0042cf0c.c)
- [`code/fcn.0042f0d8.c`](code/fcn.0042f0d8.c)
- [`code/fcn.00439b18.c`](code/fcn.00439b18.c)
- [`code/fcn.0043e0d4.c`](code/fcn.0043e0d4.c)
- [`code/fcn.004473d4.c`](code/fcn.004473d4.c)
- [`code/fcn.00447cdc.c`](code/fcn.00447cdc.c)
- [`code/fcn.00449720.c`](code/fcn.00449720.c)
- [`code/fcn.00450e7c.c`](code/fcn.00450e7c.c)
- [`code/fcn.004559f8.c`](code/fcn.004559f8.c)
- [`code/fcn.00457674.c`](code/fcn.00457674.c)
- [`code/fcn.00458204.c`](code/fcn.00458204.c)
- [`code/fcn.00473ca4.c`](code/fcn.00473ca4.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, here is the updated analysis. The new code confirms several characteristics of a complex Delphi-based framework while introducing more significant technical indicators regarding how the application handles its internal logic and external resources.

### Updated Analysis Summary

#### 1. Core Functionality and Framework Architecture
The presence of massive switch tables (e.g., in `fcn.00473ca4` with over 60 cases, and `fcn.0042f0d8` with nearly 60 cases) confirms a **highly structured application framework**. In the context of Delphi/Lazarus:
*   **Message Dispatching:** These large tables are typically used to handle Windows messages (WM_*) or internal event types. This allows a single function to act as a "hub," routing various user actions or system events to specific handlers. 
*   **Object Orientation:** The repetitive switch patterns in `fcn.004130b0` and `fcn.00412b48` are consistent with the Delphi compiler's way of handling polymorphic method calls and "type-checking" within a class hierarchy.

#### 2. Dynamic API Resolution (High Interest)
The most significant finding in this chunk is **`fcn.0042cf0c`**. This function performs a large block of `GetProcAddress` calls following a `LoadLibraryA` call:
*   **Dynamic Loading:** The code loads a DLL and immediately maps approximately 30 different function addresses from that DLL into a local table.
*   **Implications:** While this is common in complex Delphi applications to manage optional features or specific hardware drivers, it is also a **classic technique used by malware** to hide the application's true capabilities. By resolving these functions at runtime rather than at compile time, the developer can hide suspicious imports (e.g., networking functions, process injection tools, or keylogging hooks) from static analysis of the Import Address Table (IAT).
*   **Observation:** The fact that so many addresses are being grabbed suggests that the loaded DLL is a primary engine for the application's "core" functionality.

#### 3. Complex UI and Logic Handling
Several functions indicate sophisticated GUI logic:
*   **`fcn.0043e0d4` (Layout/Geometry Calculation):** This function involves heavy math regarding rectangles (`IsRectEmpty`), offset calculations, and iterative loops to process objects in a list. It appears to be calculating the boundaries of UI elements or "hit-testing" for mouse interactions.
*   **`fcn.00458204` (String/Buffer Processing):** This function contains complex logic for handling **BSTRs** (Basic Strings) and internal buffer management. It processes different types of data based on flags, which is common when a program handles multi-language support or complex data input from a network or database.

#### 4. Suspicious or Malicious Behaviors
While the code remains largely "functional" in appearance, several points warrant continued monitoring:
*   **Complexity as Obfuscation:** The sheer volume of "boilerplate" code (the massive switch tables) serves to create "noise." In a malicious sample, this makes it very difficult for an analyst to distinguish between a legitimate GUI update and a piece of malicious logic being executed in the background.
*   **API Shielding via `GetProcAddress`:** The block in `fcn.0042cf0c` is a prime candidate for further investigation. If the DLL loaded at that point is a known system DLL (like `wininet.dll`, `ws2_32.dll`, or `shell32.dll`), it may indicate hidden networking or shell execution capabilities.
*   **Data Wrapping:** The complexity in `fcn.00458204` suggests the application handles structured data objects, which could be used for anything from a standard database interface to exfiltrating stolen credentials in a structured format.

### Updated Summary for Analysis
The sample is confirmed as a **highly complex GUI application** built with the Delphi/Lazarus framework. 

1.  **Sophistication:** The code is not "simple" script-like logic; it utilizes advanced compiler features, extensive resource management, and custom-built dispatch tables.
2.  **Detection Note:** Use the **`GetProcAddress` block in `fcn.0042cf0c`** as a primary point of interest for dynamic analysis. If this function is triggered, the resulting memory space will reveal which specific capabilities the application "unlocks" during execution.
3.  **Refined Threat Profile:** This could be a sophisticated piece of software (like an enterprise management tool) or it could be **malware utilizing a professional framework to hide its intent.** The high density of boilerplate code is effective at making manual reverse-engineering tedious and time-consuming.

**Next Steps for Analysis:**
*   Identify the specific DLL loaded in `fcn.0042cf0c`.
*   Monitor network activity when that block is executed.
*   Check if any of the "offense" indicators (like high-frequency GDI calls) correlate with a change in system state or file creation.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Samples | The use of extensive "boilerplate" code and massive switch tables creates significant noise, intentionally making it difficult for an analyst to distinguish malicious logic from standard GUI operations. |
| **T1027** | Obfuscated Samples (Dynamic API Resolution) | The implementation of `LoadLibraryA` and `GetProcAddress` in `fcn.0042cf0c` is used to hide the application's true capabilities (such as networking or shell execution) from static analysis of the Import Address Table (IAT). |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Standard system libraries (e.g., kernel32.dll), common development paths (Borland/Delphi), and generic API names were excluded as they are standard for the Delphi framework and do not constitute unique malicious indicators.*

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified (Note: The provided strings contained several Borland/Delphi registry paths, but these are considered common compiler artifacts rather than specific malicious indicators).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Dynamic API Resolution Pattern:** The analysis identifies a high-interest behavior at `fcn.0042cf0c` where the application utilizes `GetProcAddress` to resolve approximately 30 functions from a dynamically loaded DLL. This is a technique used to hide functionality (e.g., networking, injection) from static analysis.
*   **Development Framework:** The presence of numerous Delphi-specific identifiers (`TObject`, `Variant`, `TStringDesc`, `_^[YY]`) and heavy use of switch tables confirms the application is built using the Delphi/Lazarus framework. 
*   **Potential Obfuscation via Complexity:** The extensive use of "boilerplate" code and large switch tables (e.g., `fcn.00473ca4`, `fcn.0042f0d8`) is noted as a technique to create noise and complicate manual reverse engineering.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Backdoor
3. **Confidence**: Medium

4. **Key evidence**:
*   **Dynamic API Resolution (T1027):** The use of `LoadLibraryA` and `GetProcAddress` to map over 30 functions into a local table is a classic technique used to hide core malicious capabilities (such as networking, injection, or credential theft) from static analysis.
*   **Sophisticated Obfuscation through Complexity:** The reliance on a heavy Delphi-based framework with massive switch tables and "boilerplate" noise suggests a professional design intended to complicate manual reverse engineering and shield the actual intent of the code.
*   **Advanced Capability Profile:** The combination of complex UI/data handling (BSTR processing) and the high volume of hidden functions indicates this is not a simple script, but rather a robust component typical of sophisticated load modules or persistent backdoors.
