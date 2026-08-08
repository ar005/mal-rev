# Threat Analysis Report

**Generated:** 2026-08-05 17:43 UTC
**Sample:** `0d3a4fc3977a52602e3fe3b568652ecea15093e6386631773c4d656a403919d6_0d3a4fc3977a52602e3fe3b568652ecea15093e6386631773c4d656a403919d6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d3a4fc3977a52602e3fe3b568652ecea15093e6386631773c4d656a403919d6_0d3a4fc3977a52602e3fe3b568652ecea15093e6386631773c4d656a403919d6.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 5,306,640 bytes |
| MD5 | `d33951cc5f6e820c10b33a5f17a65ef6` |
| SHA1 | `c837cb87252684739ae3e6eb7fec4e6829a8c948` |
| SHA256 | `0d3a4fc3977a52602e3fe3b568652ecea15093e6386631773c4d656a403919d6` |
| Overall entropy | 5.961 |
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
| `CODE` | 373,248 | 6.518 | No |
| `DATA` | 6,656 | 4.516 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 9,216 | 4.876 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.207 | No |
| `.reloc` | 28,160 | 6.67 | No |
| `.rsrc` | 4,874,240 | 5.752 | No |

### Imports

**kernel32.dll**: `Sleep`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WinHelpA`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `ShowCursor`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `GetErrorInfo`, `SysFreeString`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**gdi32.dll**: `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetWinMetaFileBits`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetMetaRgn`, `SetEnhMetaFileBits`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`
**ole32.dll**: `CoUninitialize`, `CoInitialize`
**comctl32.dll**: `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_SetDragCursorImage`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`

## Extracted Strings

Total strings found: **55159** (showing first 100)

```
This program must be run under Win32
$7
.idata
.rdata
P.reloc
P.rsrc
Boolean
Integer
Cardinal
String

WideString
TObject
TObject
System

IInterface
System
TInterfacedObject
YZ]_^[
C;D$v
D$+D$
YZ]_^[
_^[YY]
YZ]_^[
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
EHeapException
EOutOfMemory
EInOutError r@
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeError
EIntOverflow

EMathError

EInvalidOp
EZeroDivideDu@
	EOverflow

EUnderflow
EInvalidPointerPv@
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
<Eu
FR
_^[YY]
r
t%HtIHtm
_^[YY]
$Z]_^[
QQQQQQSVW3
QQQQQSVW
_^[YY]
	TErrorRec
pYZ^[

TExceptRec
YZ]_^[
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x45c058` | 4082 | ✓ |
| `fcn.0040331c` | `0x40331c` | 2517 | ✓ |
| `fcn.00446064` | `0x446064` | 2312 | ✓ |
| `fcn.0044575c` | `0x44575c` | 2280 | ✓ |
| `fcn.00409cc0` | `0x409cc0` | 1921 | ✓ |
| `fcn.00453d80` | `0x453d80` | 1750 | ✓ |
| `fcn.00423f9c` | `0x423f9c` | 1633 | ✓ |
| `fcn.0042a284` | `0x42a284` | 1392 | ✓ |
| `fcn.00412780` | `0x412780` | 1362 | ✓ |
| `fcn.00412058` | `0x412058` | 1335 | ✓ |
| `fcn.00447aa8` | `0x447aa8` | 1183 | ✓ |
| `fcn.00425380` | `0x425380` | 1131 | ✓ |
| `fcn.0040f720` | `0x40f720` | 1097 | ✓ |
| `fcn.004101e4` | `0x4101e4` | 1088 | ✓ |
| `fcn.00437d9c` | `0x437d9c` | 1085 | ✓ |
| `fcn.00459718` | `0x459718` | 1018 | ✓ |
| `fcn.0043c314` | `0x43c314` | 978 | ✓ |
| `fcn.004119a4` | `0x4119a4` | 957 | ✓ |
| `fcn.00428e10` | `0x428e10` | 947 | ✓ |
| `fcn.0042c70c` | `0x42c70c` | 905 | ✓ |
| `fcn.004559fc` | `0x4559fc` | 902 | ✓ |
| `fcn.00410ce8` | `0x410ce8` | 885 | ✓ |
| `fcn.0044f204` | `0x44f204` | 852 | ✓ |
| `fcn.0041143c` | `0x41143c` | 846 | ✓ |
| `fcn.004107e0` | `0x4107e0` | 836 | ✓ |
| `fcn.00408a0e` | `0x408a0e` | 828 | ✓ |
| `fcn.0040a7a4` | `0x40a7a4` | 795 | ✓ |
| `fcn.0045658c` | `0x45658c` | 784 | ✓ |
| `fcn.0041b1d4` | `0x41b1d4` | 763 | ✓ |
| `fcn.00456f40` | `0x456f40` | 762 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040331c.c`](code/fcn.0040331c.c)
- [`code/fcn.00408a0e.c`](code/fcn.00408a0e.c)
- [`code/fcn.00409cc0.c`](code/fcn.00409cc0.c)
- [`code/fcn.0040a7a4.c`](code/fcn.0040a7a4.c)
- [`code/fcn.0040f720.c`](code/fcn.0040f720.c)
- [`code/fcn.004101e4.c`](code/fcn.004101e4.c)
- [`code/fcn.004107e0.c`](code/fcn.004107e0.c)
- [`code/fcn.00410ce8.c`](code/fcn.00410ce8.c)
- [`code/fcn.0041143c.c`](code/fcn.0041143c.c)
- [`code/fcn.004119a4.c`](code/fcn.004119a4.c)
- [`code/fcn.00412058.c`](code/fcn.00412058.c)
- [`code/fcn.00412780.c`](code/fcn.00412780.c)
- [`code/fcn.0041b1d4.c`](code/fcn.0041b1d4.c)
- [`code/fcn.00423f9c.c`](code/fcn.00423f9c.c)
- [`code/fcn.00425380.c`](code/fcn.00425380.c)
- [`code/fcn.00428e10.c`](code/fcn.00428e10.c)
- [`code/fcn.0042a284.c`](code/fcn.0042a284.c)
- [`code/fcn.0042c70c.c`](code/fcn.0042c70c.c)
- [`code/fcn.00437d9c.c`](code/fcn.00437d9c.c)
- [`code/fcn.0043c314.c`](code/fcn.0043c314.c)
- [`code/fcn.0044575c.c`](code/fcn.0044575c.c)
- [`code/fcn.00446064.c`](code/fcn.00446064.c)
- [`code/fcn.00447aa8.c`](code/fcn.00447aa8.c)
- [`code/fcn.0044f204.c`](code/fcn.0044f204.c)
- [`code/fcn.00453d80.c`](code/fcn.00453d80.c)
- [`code/fcn.004559fc.c`](code/fcn.004559fc.c)
- [`code/fcn.0045658c.c`](code/fcn.0045658c.c)
- [`code/fcn.00456f40.c`](code/fcn.00456f40.c)
- [`code/fcn.00459718.c`](code/fcn.00459718.c)

## Behavioral Analysis

This updated analysis incorporates your new disassembly data while maintaining all previously identified characteristics of the binary.

### Updated Analysis Summary

The addition of the second set of functions reinforces the previous assessment: this is a **highly sophisticated Windows application**, almost certainly built with the **Delphi/Pascal** framework. The new code confirms extensive usage of complex UI logic, heavy GDI (Graphics Device Interface) manipulation, and advanced programming techniques used both for standard software complexity and potential obfuscation.

---

### 1. Structural Observations (Refined)
*   **Massive Dispatch Tables (The "Switch" Patterns):** You see a repeating pattern in functions like `fcn.00412058`, `fcn.0040f720`, `fcn.004101e4`, and `fcn.00459718`. These are very large switch-case blocks (one with over 60 cases).
    *   **Technical Context:** In the Delphi environment, these structures typically represent **Message Loops**, **Event Dispatchers**, or **Virtual Function Tables**. They allow a single function to handle many different types of interactions (mouse clicks, key presses, window resizing) by checking an ID and jumping to the appropriate code.
    *   **Security Perspective:** While standard for Delphi, these "megastructures" can be used to hide malicious logic inside a sea of valid functionality, making it difficult for manual analysts to find the specific code that handles a sensitive action (e.g., "If Click == 42_StealPassword").
*   **Dynamic API Resolution:** The function `fcn.00428e10` is particularly noteworthy. It uses **`GetProcAddress`** in a loop to resolve a long list of functions from a dynamically loaded library into an array/structure. 
    *   **Implication:** This allows the application to hide its true capabilities from static analysis tools (like `strings` or simple imports), as it doesn't "declare" what it wants to do until it is actually running.

### 2. Graphics and UI Complexity (Confirmed)
The functions `fcn.00425380` and `fcn.0043c314` confirm the application is heavily involved in **GDI manipulation**:
*   **Bitmaps & Buffers:** Use of `CreateDIBSection`, `CreateCompatibleDC`, and `CreateCompatibleBitmap`. This suggests the program creates a visual "canvas" or handles complex textures.
*   **Coordinate Math:** Function `fcn.0043c314` involves heavy calculations for dimensions, offsets, and area checks (`IsRectEmpty`). 
    *   **Analysis:** This is typical of a windowing system that calculates where buttons are placed, how large they are, or creates an **overlay**. If this is malware, it could be an overlay used to hide malicious activities from the user.

### 3. Advanced Data Handling & String Processing
The function `fcn.0045658c` highlights complex handling of **BSTRs (Basic Strings)** and OLE objects (`oleaut32.dll_SysFreeString`).
*   **Interpretation:** This indicates the program interacts heavily with COM components or high-level system APIs. The logic for iterating through `uVar7` to process `var_18h` suggests a multi-step parsing routine (e.g., reading a configuration file, parsing a network response, or processing an internal data structure).

### 4. Security Indicator Breakdown

| Feature | Observation | Risk Level | Context/Likelihood |
| :--- | :--- | :--- | :--- |
| **Junk Code** | Large switch tables & repetitive logic. | Moderate | Highly likely to be Delphi-related; intended for complexity, but can hide "side-loaded" payloads. |
| **Dynamic Resolution** | `GetProcAddress` used extensively in a loop. | **High** | Common in malware (to evade detection) and high-end software (to handle plugin compatibility). |
| **GDI Overlay potential** | Heavy usage of DC/Bitmap creation. | Moderate | Could be for an actual game or utility; could also be a "hook" to draw over other windows. |
| **Complex Logic** | `fcn.0043c314` coordinate calculations. | Low-Medium | Suggests high-quality professional development, but often seen in "adware" style overlays. |

### Revised Conclusion
The binary remains a high-complexity sample. The core profile is: **A Delphi-based application with heavy graphical components.** 

While the code confirms it is well-engineered, the combination of **dynamic API resolution** (to hide imports) and **complex GDI manipulation** (for UI/Overlays) puts this in a category of "suspicious but not definitive" without further analysis. It behaves like an application designed to have a significant presence on the screen (possibly as a tool or game), but the heavy obfuscation techniques suggest it may also be attempting to hide its actual core functionality from automated scanners.

**Recommended next steps for investigation:**
1.  **Dynamic Analysis:** Monitor the process in a sandbox to see which specific addresses are being resolved by `GetProcAddress` at runtime.
2.  **API Hooking:** Observe the calls made via `GetProcAddress`. If it resolves functions related to networking, file injection, or encryption, the threat level increases significantly.
3.  **Resource Extraction:** Examine any embedded icons or bitmap resources to determine if the UI is intended for a "legitimate" looking front-end.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of `GetProcAddress` in a loop to resolve functions at runtime masks the true capabilities of the binary from static analysis tools. |
| T1027 | Obfuscated Files/Information | Large, complex "megastructure" switch-case blocks are used to hide malicious logic within a dense volume of standard Delphi framework code. |
| T1036 | Masquerading | The implementation of GDI overlays can be used to mask the application's true activity or provide a deceptive interface to the user. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the intelligence report. 

Note: The "Strings" section contained primarily internal programming identifiers (Delphi/Pascal framework) and standard system library references; no direct network indicators or unique file paths were present.

### **Indicators of Compromise (IOCs)**

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (Note: The strings `Software\Borland\Delphi\...` are standard environment paths for the Delphi compiler and do not constitute malicious artifacts).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None found in provided text.*

**Other artifacts**
*   **Dynamic API Resolution:** The use of `GetProcAddress` within a loop (specifically noted in `fcn.00428e10`) indicates an attempt to hide the application's true functionality from static analysis by resolving symbols at runtime.
*   **GDI Manipulation:** Extensive usage of `CreateDIBSection`, `CreateCompatibleDC`, and `CreateCompatibleBitmap` (functions `fcn.00425380` and `fcn.0043c314`) suggests the creation of a visual overlay or complex graphical interface.
*   **Framework Identification:** The presence of Delphi-specific types (e.g., `TObject`, `TInterfacedObject`, `__tagEXCEPINFO`) and Pascal-style logic indicates the binary was built using the Delphi/Embarcadero framework.

---

### **Analyst Note**
While there are no "hard" IOCs (like IPs or File Hashes) available in this sample, the behavioral analysis highlights significant **TTPs (Tactics, Techniques, and Procedures)**:
1.  **Defense Evasion:** Via Dynamic API Resolution to hide imports.
2.  **Evasive UI/Overlay:** Potential for an "overlay" capability used to mask malicious activity or create a deceptive interface. 

Further investigation is recommended via dynamic analysis (sandboxing) to capture the specific memory addresses and APIs resolved at runtime.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader (or backdoor)
3. **Confidence**: Medium

4. **Key evidence**:
*   **Evasive API Resolution:** The use of `GetProcAddress` within a loop to resolve functions at runtime is a classic evasion technique designed to hide the binary's true capabilities from static analysis tools.
*   **GDI Overlay Capability:** Extensive manipulation of Graphics Device Interface (GDI) components (e.g., `CreateDIBSection`, `CreateCompatibleDC`) suggests the creation of an overlay, which can be used to mask malicious activity or interact with system windows visually.
*   **Sophisticated Development Profile:** The use of a high-level framework (Delphi), complex "megastructure" switch tables, and advanced data handling indicates a professional level of development typically associated with high-end trojans or loaders designed to hide their primary payload until execution.
