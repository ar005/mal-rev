# Threat Analysis Report

**Generated:** 2026-06-25 15:20 UTC
**Sample:** `00dcb399c586c167e4b979b4ea1ffb1847889c1f610a3c4d02223f0aadbf92b9_00dcb399c586c167e4b979b4ea1ffb1847889c1f610a3c4d02223f0aadbf92b9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00dcb399c586c167e4b979b4ea1ffb1847889c1f610a3c4d02223f0aadbf92b9_00dcb399c586c167e4b979b4ea1ffb1847889c1f610a3c4d02223f0aadbf92b9.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 5,419,520 bytes |
| MD5 | `936ae0a47bd03a733baf225089daf8e1` |
| SHA1 | `0cfc104c4c50ca844bd121d92b40e0e6c369d461` |
| SHA256 | `00dcb399c586c167e4b979b4ea1ffb1847889c1f610a3c4d02223f0aadbf92b9` |
| Overall entropy | 6.085 |
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
| `CODE` | 501,760 | 6.556 | No |
| `DATA` | 7,680 | 4.401 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 9,216 | 4.896 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.207 | No |
| `.reloc` | 39,936 | 6.613 | No |
| `.rsrc` | 4,859,392 | 5.839 | No |

### Imports

**kernel32.dll**: `Sleep`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WinHelpA`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `ShowCursor`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `CreateErrorInfo`, `GetErrorInfo`, `SetErrorInfo`, `SysFreeString`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**gdi32.dll**: `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`, `SelectPalette`, `SelectObject`, `SelectClipRgn`
**ole32.dll**: `CoCreateInstance`, `CoUninitialize`, `CoInitialize`
**comctl32.dll**: `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_SetDragCursorImage`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`

## Extracted Strings

Total strings found: **7308** (showing first 100)

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
	IDispatch
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
	Exception$}@
EAbort
EHeapException
EOutOfMemory
EInOutError
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeErrorH
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00403ae4` | `0x403ae4` | 4221 | ✓ |
| `entry0` | `0x47b6fc` | 2386 | ✓ |
| `fcn.0044851c` | `0x44851c` | 2312 | ✓ |
| `fcn.00447c14` | `0x447c14` | 2280 | ✓ |
| `fcn.0040ae88` | `0x40ae88` | 1921 | ✓ |
| `fcn.00456238` | `0x456238` | 1750 | ✓ |
| `fcn.00428884` | `0x428884` | 1633 | ✓ |
| `fcn.00413f38` | `0x413f38` | 1362 | ✓ |
| `fcn.00413810` | `0x413810` | 1335 | ✓ |
| `fcn.00449f60` | `0x449f60` | 1183 | ✓ |
| `fcn.00429c68` | `0x429c68` | 1131 | ✓ |
| `fcn.00410eb0` | `0x410eb0` | 1097 | ✓ |
| `fcn.00411974` | `0x411974` | 1088 | ✓ |
| `fcn.0043a358` | `0x43a358` | 1085 | ✓ |
| `fcn.004150ac` | `0x4150ac` | 1053 | ✓ |
| `fcn.0043e914` | `0x43e914` | 978 | ✓ |
| `fcn.0041315c` | `0x41315c` | 965 | ✓ |
| `fcn.0042d74c` | `0x42d74c` | 947 | ✓ |
| `fcn.0042f918` | `0x42f918` | 905 | ✓ |
| `fcn.00457eb4` | `0x457eb4` | 902 | ✓ |
| `fcn.00412484` | `0x412484` | 885 | ✓ |
| `fcn.004516bc` | `0x4516bc` | 852 | ✓ |
| `fcn.00412bf4` | `0x412bf4` | 846 | ✓ |
| `fcn.00411f70` | `0x411f70` | 836 | ✓ |
| `fcn.004160f4` | `0x4160f4` | 834 | ✓ |
| `fcn.00409612` | `0x409612` | 828 | ✓ |
| `fcn.0040b96c` | `0x40b96c` | 795 | ✓ |
| `fcn.00458b8c` | `0x458b8c` | 784 | ✓ |
| `fcn.004209e8` | `0x4209e8` | 763 | ✓ |
| `fcn.0044e804` | `0x44e804` | 757 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00403ae4.c`](code/fcn.00403ae4.c)
- [`code/fcn.00409612.c`](code/fcn.00409612.c)
- [`code/fcn.0040ae88.c`](code/fcn.0040ae88.c)
- [`code/fcn.0040b96c.c`](code/fcn.0040b96c.c)
- [`code/fcn.00410eb0.c`](code/fcn.00410eb0.c)
- [`code/fcn.00411974.c`](code/fcn.00411974.c)
- [`code/fcn.00411f70.c`](code/fcn.00411f70.c)
- [`code/fcn.00412484.c`](code/fcn.00412484.c)
- [`code/fcn.00412bf4.c`](code/fcn.00412bf4.c)
- [`code/fcn.0041315c.c`](code/fcn.0041315c.c)
- [`code/fcn.00413810.c`](code/fcn.00413810.c)
- [`code/fcn.00413f38.c`](code/fcn.00413f38.c)
- [`code/fcn.004150ac.c`](code/fcn.004150ac.c)
- [`code/fcn.004160f4.c`](code/fcn.004160f4.c)
- [`code/fcn.004209e8.c`](code/fcn.004209e8.c)
- [`code/fcn.00428884.c`](code/fcn.00428884.c)
- [`code/fcn.00429c68.c`](code/fcn.00429c68.c)
- [`code/fcn.0042d74c.c`](code/fcn.0042d74c.c)
- [`code/fcn.0042f918.c`](code/fcn.0042f918.c)
- [`code/fcn.0043a358.c`](code/fcn.0043a358.c)
- [`code/fcn.0043e914.c`](code/fcn.0043e914.c)
- [`code/fcn.00447c14.c`](code/fcn.00447c14.c)
- [`code/fcn.0044851c.c`](code/fcn.0044851c.c)
- [`code/fcn.00449f60.c`](code/fcn.00449f60.c)
- [`code/fcn.0044e804.c`](code/fcn.0044e804.c)
- [`code/fcn.004516bc.c`](code/fcn.004516bc.c)
- [`code/fcn.00456238.c`](code/fcn.00456238.c)
- [`code/fcn.00457eb4.c`](code/fcn.00457eb4.c)
- [`code/fcn.00458b8c.c`](code/fcn.00458b8c.c)

## Behavioral Analysis

This analysis incorporates the newly provided disassembly (chunk 2/2) into the existing profile of the binary.

### Updated Analysis Overview
The additional code reinforces the previous conclusion that this is a large, complex application built with **Delphi / Pascal**. The new functions exhibit high levels of abstraction, sophisticated memory management for strings (BSTR), and extensive graphics calculation logic.

---

### New Technical Observations

#### 1. Extensive use of Dynamic Linking
**Function:** `fcn.0042d74c`  
This function contains a massive block of `GetProcAddress` calls. It is loading dozens of functions from an external DLL into memory at runtime. 
*   **Why this matters:** While dynamic loading is common in legitimate software to handle optional features or interface with system APIs, such a large number of imports suggests the application relies heavily on an external library for its core functionality (e.g., a graphics engine, a database driver, or a complex UI framework).

#### 2. Complex State Machine & Polymorphism
**Functions:** `fcn.0041315c`, `fcn.00412484`, `fcn.004209e8`, and `fcn.0042f918`.
These functions utilize "Switch Table" logic where a single function handles many different cases (some with up to 38 cases).
*   **Delphi Context:** This is highly characteristic of the **Delphi VCL (Visual Component Library)**. In Pascal, this pattern is used to implement polymorphism and message handling efficiently—one piece of code manages multiple types of UI elements (buttons, text fields, etc.) by checking an internal "Type" ID before executing specific logic.
*   **Switch Table `fcn.0042f918`:** This appears to be a translation or mapping table, potentially converting input values into internal indices or constants.

#### 3. Advanced Graphics & Geometry Processing
**Functions:** `fcn.0043e914`, `fcn.00457eb4`.
These functions perform heavy calculations regarding:
*   **Clipping and Rectangles:** The use of `OffsetRect` and logic to calculate "dirty regions" (areas of the screen that need redrawing) indicates a sophisticated custom UI or graphics rendering engine.
*   **Coordinate Math:** Significant bit-shifting and arithmetic are used to adjust positions, which is common in high-performance GUI rendering.

#### 4. Complex String & OLE Management
**Functions:** `fcn.004150ac`, `fcn.00458b8c`.
*   The inclusion of `oleaut32.dll_VariantInit` and several `SysFreeString` operations confirms the use of **OLE/COM standards**. 
*   **Function `fcn.00458b8c`** is specifically dealing with complex string construction, likely handling different types of strings (Unicode, ANSI, or System strings) which are common in Delphi applications interacting with Windows' underlying API.

---

### Summary Table of New Observations

| Feature | Observation | Context/Significance |
| :--- | :--- | :--- |
| **Dynamic Linking** | Mass `GetProcAddress` calls in `fcn.0042d74c`. | Indicates heavy reliance on external DLLs for core features. |
| **Polymorphic Handling** | Deeply nested switch tables (e.g., `fcn.004209e8`). | Standard Delphi VCL behavior for managing complex UI objects. |
| **Graphics Pipeline** | Complex rect/clip logic in `fcn.00457eb4`. | Indicates a robust GUI or custom graphics rendering engine. |
| **Memory Management** | Explicit `Variant` and `SysFreeString` handling. | Standard high-level language behavior for data persistence and OLE support. |

---

### Updated Risk Assessment

*   **Malicious Behavior:** Still **not detected.** 
    *   The functions identified are "heavyweight" library functions. While they are complex, there is no evidence of malicious intent (e.g., keylogging, stealing credentials, or unauthorized file modification).
*   **Evasion Techniques:** The use of `GetProcAddress` could be used by malware to hide its true intentions from static analysis, but in the context of the other findings (VCL-style switch tables and OLE support), it is much more likely that the program is simply a large piece of legitimate software.
*   **Complexity Note:** The sheer amount of "boilerplate" code confirms this is not a simple script or a small downloader; it is a full-featured application, likely a commercial product or a complex utility.

### Conclusion Update
The analysis remains consistent: **The binary appears to be a professional Delphi/VCL application.** 

While the complexity of the switch tables and the volume of dynamic linking are high, they align with the expected behavior of a large enterprise-grade Windows application. No specific malicious routines were found in this second chunk of disassembly. The logic remains focused on **UI management, graphics rendering, and internal state handling.**

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1106.003 | Dynamic Resolution | The extensive use of `GetProcAddress` to resolve a large number of functions at runtime is used to obscure the application's dependencies from static analysis. |
| T1027 | Obfuscated Executables | The use of complex switch tables and highly abstracted logic (polymorphism) increases the complexity of the code, which can hinder manual reverse engineering. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*None identified.*

**File paths / Registry keys**
*None.* (Note: The registry paths `SOFTWARE\Borland\Delphi\...` were identified in the strings but are classified as false positives, as they refer to standard Borland/Delphi development environment paths rather than malicious configuration.)

**Mutex names / Named pipes**
*None identified.*

**Hashes**
*None identified.*

**Other artifacts (user agents, C2 patterns, etc.)**
*None identified.*

---
**Analyst Note:** 
The analysis indicates that the binary is a standard, large-scale application developed using the **Delphi/Pascal** framework. While the behavior includes techniques like dynamic linking (`GetProcAddress`) and complex state machines, these are characteristic of high-level UI development (VCL) rather than malicious activity. No specific indicators of a command-and-control (C2) infrastructure, malicious persistence mechanisms, or unauthorized communication were detected in the provided data.

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1.  **Malware family:** None (Benign)
2.  **Malware type:** Not applicable (Potentially False Positive / Benign Software)
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Standard Framework Behavior:** The "suspicious" indicators, such as large switch tables and extensive use of `GetProcAddress`, were identified as standard behaviors of the **Delphi VCL (Visual Component Library)** for managing UI elements and complex graphics, rather than intentional evasion techniques.
    *   **Lack of Malicious Functionality:** Analysis confirmed no evidence of common malware behaviors such as keylogging, credential theft, unauthorized file encryption, or command-and-control (C2) communication.
    *   **Legitimate Application Logic:** The presence of sophisticated graphics rendering logic and standard memory management (`Variant`, `SysFreeString`) suggests a large, professional piece of software rather than a malicious tool.
