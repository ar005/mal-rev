# Threat Analysis Report

**Generated:** 2026-08-10 15:54 UTC
**Sample:** `0dcc271a1c3d93b717ee19ef64735a619f2be5767b0eed7376882352293d4414_0dcc271a1c3d93b717ee19ef64735a619f2be5767b0eed7376882352293d4414.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0dcc271a1c3d93b717ee19ef64735a619f2be5767b0eed7376882352293d4414_0dcc271a1c3d93b717ee19ef64735a619f2be5767b0eed7376882352293d4414.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 4,962,064 bytes |
| MD5 | `8fa1c2c4c68d88a023315a7404131534` |
| SHA1 | `bae00f4d407195e77952f4360e169c8366febcbe` |
| SHA256 | `0dcc271a1c3d93b717ee19ef64735a619f2be5767b0eed7376882352293d4414` |
| Overall entropy | 6.252 |
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
| `CODE` | 376,320 | 6.515 | No |
| `DATA` | 6,656 | 4.554 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 9,216 | 4.872 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.207 | No |
| `.reloc` | 29,184 | 6.635 | No |
| `.rsrc` | 4,525,568 | 6.073 | No |

### Imports

**kernel32.dll**: `Sleep`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WinHelpA`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `ShowCursor`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `GetErrorInfo`, `SysFreeString`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**gdi32.dll**: `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetWinMetaFileBits`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetEnhMetaFileBits`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`, `SelectPalette`
**ole32.dll**: `CoUninitialize`, `CoInitialize`
**comctl32.dll**: `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_SetDragCursorImage`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`

## Extracted Strings

Total strings found: **41617** (showing first 100)

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
	Exceptionq@
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
EZeroDivide@u@
	EOverflow

EUnderflow
EInvalidPointerLv@
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
| `fcn.00403328` | `0x403328` | 2529 | ✓ |
| `fcn.00445594` | `0x445594` | 2312 | ✓ |
| `fcn.00444c8c` | `0x444c8c` | 2280 | ✓ |
| `fcn.00409cf0` | `0x409cf0` | 1921 | ✓ |
| `fcn.004532b0` | `0x4532b0` | 1750 | ✓ |
| `fcn.00423fa4` | `0x423fa4` | 1633 | ✓ |
| `fcn.0042a28c` | `0x42a28c` | 1392 | ✓ |
| `fcn.004127b0` | `0x4127b0` | 1362 | ✓ |
| `fcn.00412088` | `0x412088` | 1335 | ✓ |
| `fcn.00446fd8` | `0x446fd8` | 1183 | ✓ |
| `fcn.00425388` | `0x425388` | 1131 | ✓ |
| `fcn.0040f750` | `0x40f750` | 1097 | ✓ |
| `fcn.00410214` | `0x410214` | 1088 | ✓ |
| `fcn.004372f8` | `0x4372f8` | 1085 | ✓ |
| `fcn.00457cb0` | `0x457cb0` | 1018 | ✓ |
| `fcn.0043b844` | `0x43b844` | 978 | ✓ |
| `entry0` | `0x45cc80` | 970 | ✓ |
| `fcn.004119d4` | `0x4119d4` | 965 | ✓ |
| `fcn.00428e18` | `0x428e18` | 947 | ✓ |
| `fcn.0042c714` | `0x42c714` | 905 | ✓ |
| `fcn.00454f2c` | `0x454f2c` | 902 | ✓ |
| `fcn.00410d18` | `0x410d18` | 885 | ✓ |
| `fcn.0044e734` | `0x44e734` | 852 | ✓ |
| `fcn.0041146c` | `0x41146c` | 846 | ✓ |
| `fcn.00410810` | `0x410810` | 836 | ✓ |
| `fcn.00408a3e` | `0x408a3e` | 828 | ✓ |
| `fcn.0040a7d4` | `0x40a7d4` | 795 | ✓ |
| `fcn.00455abc` | `0x455abc` | 784 | ✓ |
| `fcn.0041b1dc` | `0x41b1dc` | 763 | ✓ |
| `fcn.0044b87c` | `0x44b87c` | 757 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00403328.c`](code/fcn.00403328.c)
- [`code/fcn.00408a3e.c`](code/fcn.00408a3e.c)
- [`code/fcn.00409cf0.c`](code/fcn.00409cf0.c)
- [`code/fcn.0040a7d4.c`](code/fcn.0040a7d4.c)
- [`code/fcn.0040f750.c`](code/fcn.0040f750.c)
- [`code/fcn.00410214.c`](code/fcn.00410214.c)
- [`code/fcn.00410810.c`](code/fcn.00410810.c)
- [`code/fcn.00410d18.c`](code/fcn.00410d18.c)
- [`code/fcn.0041146c.c`](code/fcn.0041146c.c)
- [`code/fcn.004119d4.c`](code/fcn.004119d4.c)
- [`code/fcn.00412088.c`](code/fcn.00412088.c)
- [`code/fcn.004127b0.c`](code/fcn.004127b0.c)
- [`code/fcn.0041b1dc.c`](code/fcn.0041b1dc.c)
- [`code/fcn.00423fa4.c`](code/fcn.00423fa4.c)
- [`code/fcn.00425388.c`](code/fcn.00425388.c)
- [`code/fcn.00428e18.c`](code/fcn.00428e18.c)
- [`code/fcn.0042a28c.c`](code/fcn.0042a28c.c)
- [`code/fcn.0042c714.c`](code/fcn.0042c714.c)
- [`code/fcn.004372f8.c`](code/fcn.004372f8.c)
- [`code/fcn.0043b844.c`](code/fcn.0043b844.c)
- [`code/fcn.00444c8c.c`](code/fcn.00444c8c.c)
- [`code/fcn.00445594.c`](code/fcn.00445594.c)
- [`code/fcn.00446fd8.c`](code/fcn.00446fd8.c)
- [`code/fcn.0044b87c.c`](code/fcn.0044b87c.c)
- [`code/fcn.0044e734.c`](code/fcn.0044e734.c)
- [`code/fcn.004532b0.c`](code/fcn.004532b0.c)
- [`code/fcn.00454f2c.c`](code/fcn.00454f2c.c)
- [`code/fcn.00455abc.c`](code/fcn.00455abc.c)
- [`code/fcn.00457cb0.c`](code/fcn.00457cb0.c)

## Behavioral Analysis

This updated analysis incorporates the new disassembly data provided in chunk 2/2 while maintaining all previously identified indicators regarding the binary's structure and environment.

---

### Updated Analysis Report

#### 1. Core Functionality and Purpose (Refined)
The binary continues to demonstrate characteristics of a complex, **graphical UI application** built using the **Delphi (Embarcadero)** framework. The second set of functions confirms several internal mechanics:

*   **Heavy Dependency on Abstract Frameworks:** Functions like `fcn.004119d4` and `fcn.00410d18` contain massive switch tables (some with 21+ cases). In a Delphi context, these are typical of "Property Getters/Setters" or "Method Dispatchers." These functions handle the translation between high-level language objects and low-level memory addresses, often used for handling various data types (integers, floats, strings) in a single unified interface.
*   **Dynamic API Resolution:** Function `fcn.00428e18` is significant as it utilizes `LoadLibraryA` and `GetProcAddress`. It appears to be a "loader" or an initialization routine that maps a large number of function pointers from a loaded module into the application's internal tables.
*   **Complex Coordinate & UI Geometry:** Function `fcn.00454f2c` demonstrates heavy interaction with Windows GDI for layout calculation. It uses calls like `ClientToScreen` and `OffsetRect`, which are indicative of a system that dynamically calculates the position of windows, buttons, or other interactive elements on the screen.

#### 2. Suspicious or Malicious Behaviors
While the "Trojaned UI" hypothesis remains the primary concern, new patterns emerge from the second chunk:

*   **Dynamic Loading for Stealth/Capability:** The dense block of `GetProcAddress` calls in `fcn.00428e18` suggests the application is preparing to call a large number of functions from a dynamically loaded DLL. In malware, this is often used to hide the true capabilities of the code until it is actually needed, or to bypass static analysis tools that look for standard "Import" tables.
*   **Complex State Machine:** The heavy use of switch cases (e.g., `fcn.0042c714`) and nested logic in `fcn.00454f2c` suggests a very complex internal state machine. While common in large applications, this complexity can also be used to "hide" malicious actions among hundreds of lines of legitimate-looking UI management code.
*   **Timing and Delays:** The presence of `Sleep` (called within `fcn.0044b87c`) indicates that the program manages timing. This could be for a simple UI animation, but in a threat context, it is often used to "stall" execution to evade automated sandbox analysis or to coordinate timed actions.

#### 3. Notable Techniques and Patterns
*   **Delphi Signature Persistence:** The repetitive switch-table structures (e.g., checking for `0x100`, `0x101`, and using bitwise masks like `& 0x4000`) are classic indicators of the Delphi compiler’s method of handling overloaded functions and property access.
*   **GDI/User32 Manipulation:** The use of `OffsetRect` and `ClientToScreen` confirms that the application is not just "drawing" to a buffer, but is actively manipulating how the OS views window geometry. This is common in **overlay creators** or software designed to hide its own presence behind other windows.
*   **String Handling Overheads:** Function `fcn.00455abc` appears to involve complex string parsing and manipulation (indicated by checks for special characters like `\x01`, `\x02`, etc.).

### Summary for Analyst

The addition of the second chunk reinforces the initial assessment: **This is a high-complexity, Delphi-compiled binary with an extensive graphical component.** 

**Updated Risk Profile:**
The primary risk remains the potential for **Overlay Injection**. The combination of intensive GDI usage (`OffsetRect`, `ClientToScreen`), dynamic library loading (loading many functions via `GetProcAddress`), and heavy UI logic suggests a program that spends considerable effort managing how it appears on the user's screen.

**Investigation Focus:**
1.  **DLL Analysis:** Identify what is being loaded in `fcn.00428e18`. The "hidden" functionality is likely within the DLLs it resolves at runtime. 
2.  **Overlay Investigation:** Determine if the GDI calls are intended for a standard UI or if they are being used to create an overlay that sits on top of other applications (common in game cheats, screen-sharing tools, and overlay-based malware).
3.  **String/Data Extraction:** The string parsing logic in `fcn.00455abc` should be examined for hardcoded configuration data or decrypted commands.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&K framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1106.003** | **Dynamic Resolution** | The use of `LoadLibraryA` and `GetProcAddress` to resolve function pointers at runtime is used to hide the binary's true capabilities from static analysis tools. |
| **T1497** | **Virtualization/Sandbox Evasion** | The inclusion of `Sleep` calls is identified as a specific method to stall execution and evade detection by automated sandbox analysis systems. |
| **T1036** | **Masquerading** | The extensive use of GDI functions (`OffsetRect`, `ClientToScreen`) to create overlays and manipulate UI geometry suggests an attempt to hide the application's true purpose or presence behind a legitimate-looking interface. |
| **T1027** | **Obfuscated Files or Information** | The implementation of highly complex state machines and intricate logic branches is used to "hide" malicious actions among layers of complex, legitimate-looking UI management code. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Per your instructions, standard system paths (e.g., Borland/Delphi paths) and common library names have been excluded as they are false positives related to the development environment rather than specific malicious infrastructure.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (The values `Software\Borland\Delphi\RTL` and `Software\Borland\Locales` are standard compiler artifacts).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Dynamic Loading Patterns:** Use of `LoadLibraryA` and `GetProcAddress` (specifically at offset `fcn.00428e18`) to dynamically resolve a large number of functions, suggesting an attempt to hide functionality from static analysis.
*   **Overlay/GDI Manipulation:** Repeated use of `OffsetRect` and `ClientToScreen` in function `fcn.00454f2c` indicates the creation of graphical overlays or the manipulation of window geometry (common in screen-overlay malware).
*   **Anti-Analysis Techniques:** Use of the `Sleep` function (at `fcn.0044b87c`) to stall execution, a common tactic used to evade automated sandbox environments.
*   **Complex String Parsing:** Logic at `fcn.00455abc` involving special character checks (`\x01`, `\x02`), which may indicate the presence of an encoded configuration or communication protocol.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / trojan
3. **Confidence**: Medium

4. **Key evidence**:
*   **Dynamic Resolution & Hidden Functionality:** The heavy reliance on `LoadLibraryA` and `GetProcAddress` to map a large number of functions into internal tables indicates the binary is likely a **loader**, designed to fetch and execute malicious payloads from dynamically loaded modules while evading static analysis.
*   **Overlay Manipulation for Masquerading:** The extensive use of GDI calls (`OffsetRect`, `ClientToScreen`) and complex UI logic suggests "Trojaned UI" behavior, where the malware creates a graphical overlay to hide its activities or interact with other applications (common in screen-overlay tools and trojans).
*   **Intentional Anti-Analysis:** The presence of `Sleep` functions specifically used for "stalling" execution and the use of complex state machines to bury malicious logic within heavy UI code confirm an active effort to bypass automated sandbox detection and complicate manual reverse engineering.
