# Threat Analysis Report

**Generated:** 2026-08-13 20:22 UTC
**Sample:** `0eb657033b8d77480d42e76f90271d731f5bd8ef2c1f56276834afa4eb01aa18_0eb657033b8d77480d42e76f90271d731f5bd8ef2c1f56276834afa4eb01aa18.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0eb657033b8d77480d42e76f90271d731f5bd8ef2c1f56276834afa4eb01aa18_0eb657033b8d77480d42e76f90271d731f5bd8ef2c1f56276834afa4eb01aa18.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 4,165,632 bytes |
| MD5 | `c9edf7efdd7a472b29129c42066ef1a4` |
| SHA1 | `498961a998b18e8fc36a0acc47dea958aa5a35f8` |
| SHA256 | `0eb657033b8d77480d42e76f90271d731f5bd8ef2c1f56276834afa4eb01aa18` |
| Overall entropy | 7.043 |
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
| `CODE` | 375,296 | 6.547 | No |
| `DATA` | 5,632 | 3.93 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 8,704 | 4.971 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.207 | No |
| `.reloc` | 26,112 | 6.675 | No |
| `.rsrc` | 3,748,352 | 6.934 | No |

### Imports

**kernel32.dll**: `Sleep`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WinHelpA`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `ShowCursor`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `GetErrorInfo`, `SysFreeString`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**gdi32.dll**: `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`, `SelectPalette`, `SelectObject`, `SaveDC`
**ole32.dll**: `CoUninitialize`, `CoInitialize`
**comctl32.dll**: `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_SetDragCursorImage`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Replace`

## Extracted Strings

Total strings found: **5631** (showing first 100)

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
	ExceptionPx@
EHeapException
EOutOfMemory
EInOutError`y@
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeError {@
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
<Eu
FR
_^[YY]
_^[YY]
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00403a18` | `0x403a18` | 4113 | ✓ |
| `fcn.004466c8` | `0x4466c8` | 2312 | ✓ |
| `fcn.00445dc0` | `0x445dc0` | 2280 | ✓ |
| `entry0` | `0x45c8b8` | 1943 | ✓ |
| `fcn.0040a448` | `0x40a448` | 1921 | ✓ |
| `fcn.004543e4` | `0x4543e4` | 1750 | ✓ |
| `fcn.0042572c` | `0x42572c` | 1633 | ✓ |
| `fcn.0042ca04` | `0x42ca04` | 1494 | ✓ |
| `fcn.0041323c` | `0x41323c` | 1362 | ✓ |
| `fcn.00412b14` | `0x412b14` | 1335 | ✓ |
| `fcn.0044810c` | `0x44810c` | 1183 | ✓ |
| `fcn.00426b10` | `0x426b10` | 1131 | ✓ |
| `fcn.004101b4` | `0x4101b4` | 1097 | ✓ |
| `fcn.00410c78` | `0x410c78` | 1088 | ✓ |
| `fcn.00438014` | `0x438014` | 1085 | ✓ |
| `fcn.0043c47c` | `0x43c47c` | 978 | ✓ |
| `fcn.00412460` | `0x412460` | 965 | ✓ |
| `fcn.0042a5f8` | `0x42a5f8` | 947 | ✓ |
| `fcn.0042eed0` | `0x42eed0` | 905 | ✓ |
| `fcn.00456060` | `0x456060` | 902 | ✓ |
| `fcn.00411788` | `0x411788` | 885 | ✓ |
| `fcn.0044f868` | `0x44f868` | 852 | ✓ |
| `fcn.00411ef8` | `0x411ef8` | 846 | ✓ |
| `fcn.00411274` | `0x411274` | 836 | ✓ |
| `fcn.004147b0` | `0x4147b0` | 834 | ✓ |
| `fcn.004090ea` | `0x4090ea` | 828 | ✓ |
| `fcn.0042d220` | `0x42d220` | 809 | ✓ |
| `fcn.0040af2c` | `0x40af2c` | 795 | ✓ |
| `fcn.00456bf0` | `0x456bf0` | 784 | ✓ |
| `fcn.0041e3ec` | `0x41e3ec` | 763 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00403a18.c`](code/fcn.00403a18.c)
- [`code/fcn.004090ea.c`](code/fcn.004090ea.c)
- [`code/fcn.0040a448.c`](code/fcn.0040a448.c)
- [`code/fcn.0040af2c.c`](code/fcn.0040af2c.c)
- [`code/fcn.004101b4.c`](code/fcn.004101b4.c)
- [`code/fcn.00410c78.c`](code/fcn.00410c78.c)
- [`code/fcn.00411274.c`](code/fcn.00411274.c)
- [`code/fcn.00411788.c`](code/fcn.00411788.c)
- [`code/fcn.00411ef8.c`](code/fcn.00411ef8.c)
- [`code/fcn.00412460.c`](code/fcn.00412460.c)
- [`code/fcn.00412b14.c`](code/fcn.00412b14.c)
- [`code/fcn.0041323c.c`](code/fcn.0041323c.c)
- [`code/fcn.004147b0.c`](code/fcn.004147b0.c)
- [`code/fcn.0041e3ec.c`](code/fcn.0041e3ec.c)
- [`code/fcn.0042572c.c`](code/fcn.0042572c.c)
- [`code/fcn.00426b10.c`](code/fcn.00426b10.c)
- [`code/fcn.0042a5f8.c`](code/fcn.0042a5f8.c)
- [`code/fcn.0042ca04.c`](code/fcn.0042ca04.c)
- [`code/fcn.0042d220.c`](code/fcn.0042d220.c)
- [`code/fcn.0042eed0.c`](code/fcn.0042eed0.c)
- [`code/fcn.00438014.c`](code/fcn.00438014.c)
- [`code/fcn.0043c47c.c`](code/fcn.0043c47c.c)
- [`code/fcn.00445dc0.c`](code/fcn.00445dc0.c)
- [`code/fcn.004466c8.c`](code/fcn.004466c8.c)
- [`code/fcn.0044810c.c`](code/fcn.0044810c.c)
- [`code/fcn.0044f868.c`](code/fcn.0044f868.c)
- [`code/fcn.004543e4.c`](code/fcn.004543e4.c)
- [`code/fcn.00456060.c`](code/fcn.00456060.c)
- [`code/fcn.00456bf0.c`](code/fcn.00456bf0.c)

## Behavioral Analysis

This second batch of disassembly provides deeper insight into the internal mechanics of the application. While it remains largely consistent with a high-level Delphi/VCL construction, several specific functional areas become clearer in this segment.

### Updated Analysis

#### 1. Advanced GUI Layout & Rendering Logic
A significant portion of the code (e.g., `fcn.00438014`, `fcn.0043c47c`, and `fcn.0042d220`) is dedicated to calculating and rendering visual elements.
*   **Dynamic Layout Calculations:** Functions like `fcn.0043c47c` contain loops that iterate through arrays of objects, checking their dimensions and positions (using functions like `IsRectEmpty`). This suggests the program manages a collection of UI elements—such as buttons in a list, icons in a toolbar, or items in a custom menu system.
*   **Text Rendering & Positioning:** `fcn.0042d220` contains heavy arithmetic for "padding" and "margin" calculations (e.g., checking if values are equal to `0xffffffff`). This is typical of logic used to position text inside a button or box that must dynamically adjust based on the available width/height. It explicitly calls `DrawTextA`, confirming it handles localized or standard system text display.

#### 2. Library Loading and Module Initialization
The function **`fcn.0042a5f8`** is highly significant from a structural standpoint:
*   **Dynamic Linking:** This function acts as a "loader" or "initializer." It calls `LoadLibraryA` to load a DLL into memory and then executes a long sequence of `GetProcAddress` calls. 
*   **Analysis:** While this *can* be used by malware to load malicious payloads, in the context of a Delphi application, it is much more commonly used to initialize third-party components (e.g., a specialized installer engine, an encryption library, or a database driver). The large block of `GetProcAddress` calls indicates that the program relies on a significant amount of functionality provided by this external DLL.

#### 3. String Management and COM Interop
The function **`fcn.00456bf0`** contains logic for handling **BSTR (Basic String)** types:
*   **System Integration:** The use of `SysFreeString_1`, processing of Unicode/ANSI conversions, and the specific check for the high-bit character (`0x80`) indicate that the application is interacting with Windows COM objects or lower-level system APIs.
*   **Implication:** This suggests the app may interact with "higher" levels of the OS, such as shell folders, file system attributes via advanced APIs, or internal COM interfaces.

#### 4. High-Level Dispatcher Patterns
Several functions (`fcn.00412460`, `fcn.00411788`, and `fcn.0041e3ec`) are "Dispatchers":
*   **Complexity via Architecture:** These use large `switch` tables (based on ID values) to route internal requests to specific functions. This confirms a highly modular architecture where the UI thread determines which logic "block" to execute based on a user's click or an internal state change.

---

### Updated Risk Assessment

*   **Malicious Indicators:** **Still None.** There are no signs of shellcode, process injection, raw socket manipulation, or direct registry tampering in this segment.
*   **Sophistication level:** The code is "heavy" and complex, but this complexity is a hallmark of the Delphi VCL framework rather than manual obfuscation. The developer likely used standard UI libraries to build a feature-rich interface.
*   **Behavioral Profile:** This continues to look like a **professional installer or a large utility tool.** The extensive GDI math suggests a customized UI (not just a standard Windows form), and the dynamic loading of a DLL with many exported functions suggests the inclusion of specialized features (like compression, file system interaction, or networking).

### Summary for Triage
The addition of this code confirms that the application is part of a **substantial software suite**. It contains complex logic for UI layout and likely integrates third-party components via DLLs. While it possesses the "complex" look that can sometimes mimic malware's obfuscation, the specific patterns found here (GDI calculation loops, BSTR handling, and VCL dispatchers) are much more indicative of a **legitimate installer or heavy-duty utility application.**

**Key Indicator for Further Investigation:** If you have access to the symbol names or if the DLL loaded in `fcn.0042a5f8` can be identified, it would reveal exactly what "feature" (e.g., an updater, a codec, etc.) is being added by that module.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1106 | Native API | The application utilizes `LoadLibraryA` and a sequence of `GetProcAddress` calls to dynamically load modules and resolve function pointers at runtime. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the assessment of Indicators of Compromise (IOCs).

### **Threat Intelligence Assessment**
The provided data describes a sophisticated but evidently legitimate application (likely a Delphi-based installer or utility). The behavioral analysis explicitly states that no malicious indicators were found. Per your instructions to skip false positives (such as standard Windows paths and library strings), the following sections are empty:

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (Note: The registry paths `SOFTWARE\Borland\...` were excluded as they are standard development environment artifacts, not evidence of malicious activity.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts (user agents, C2 patterns, etc.)**
*   *None identified.* 

---
**Analyst Note:** The analysis identifies a dynamic loading routine in `fcn.0042a5f8` involving `LoadLibraryA` and `GetProcAddress`. While these functions can be used by malware to mask imports, the context provided indicates they are being utilized for standard third-party component integration within a Delphi environment. No specific malicious filenames or C2 communication patterns were identified in the provided text.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: None (Not Malicious)
3. **Confidence**: High
4. **Key evidence**:
    *   **Absence of Malicious Indicators:** The analysis explicitly states that no signs of shellcode, process injection, raw socket manipulation, or unauthorized registry tampering were found in the code segment.
    *   **Standard Framework Behavior:** The "complex" code identified (GDI math, BSTR handling, and dispatcher patterns) is attributed to standard Delphi VCL framework requirements for creating high-quality user interfaces rather than manual obfuscation techniques used by malware.
    *   **Contextual Utility Inference:** The behavior of the application—including dynamic library loading and sophisticated GUI management—aligns with a professional installer or a large utility suite rather than a malicious payload like a dropper or backdoor.
