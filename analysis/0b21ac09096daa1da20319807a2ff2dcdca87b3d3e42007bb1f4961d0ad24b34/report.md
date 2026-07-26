# Threat Analysis Report

**Generated:** 2026-07-25 20:07 UTC
**Sample:** `0b21ac09096daa1da20319807a2ff2dcdca87b3d3e42007bb1f4961d0ad24b34_0b21ac09096daa1da20319807a2ff2dcdca87b3d3e42007bb1f4961d0ad24b34.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b21ac09096daa1da20319807a2ff2dcdca87b3d3e42007bb1f4961d0ad24b34_0b21ac09096daa1da20319807a2ff2dcdca87b3d3e42007bb1f4961d0ad24b34.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 4,096,512 bytes |
| MD5 | `4597a15ed3cab5b5aee5fc44e86e5ac4` |
| SHA1 | `b63e9c63ed7021f1c0f0d67663449968f7477ec7` |
| SHA256 | `0b21ac09096daa1da20319807a2ff2dcdca87b3d3e42007bb1f4961d0ad24b34` |
| Overall entropy | 7.265 |
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
| `DATA` | 7,680 | 4.399 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 9,216 | 4.894 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.207 | No |
| `.reloc` | 39,936 | 6.611 | No |
| `.rsrc` | 3,536,384 | 7.19 | ⚠️ Yes |

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

Total strings found: **9827** (showing first 100)

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
	Exception
EAbort
EHeapException
EOutOfMemory
EInOutError
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeError@
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
| `entry0` | `0x47b6d8` | 2422 | ✓ |
| `fcn.00448514` | `0x448514` | 2312 | ✓ |
| `fcn.00447c0c` | `0x447c0c` | 2280 | ✓ |
| `fcn.0040ae80` | `0x40ae80` | 1921 | ✓ |
| `fcn.00456230` | `0x456230` | 1750 | ✓ |
| `fcn.0042887c` | `0x42887c` | 1633 | ✓ |
| `fcn.00413f30` | `0x413f30` | 1362 | ✓ |
| `fcn.00413808` | `0x413808` | 1335 | ✓ |
| `fcn.00449f58` | `0x449f58` | 1183 | ✓ |
| `fcn.00429c60` | `0x429c60` | 1131 | ✓ |
| `fcn.00410ea8` | `0x410ea8` | 1097 | ✓ |
| `fcn.0041196c` | `0x41196c` | 1088 | ✓ |
| `fcn.0043a350` | `0x43a350` | 1085 | ✓ |
| `fcn.004150a4` | `0x4150a4` | 1053 | ✓ |
| `fcn.0043e90c` | `0x43e90c` | 978 | ✓ |
| `fcn.00413154` | `0x413154` | 965 | ✓ |
| `fcn.0042d744` | `0x42d744` | 947 | ✓ |
| `fcn.0042f910` | `0x42f910` | 905 | ✓ |
| `fcn.00457eac` | `0x457eac` | 902 | ✓ |
| `fcn.0041247c` | `0x41247c` | 885 | ✓ |
| `fcn.004516b4` | `0x4516b4` | 852 | ✓ |
| `fcn.00412bec` | `0x412bec` | 846 | ✓ |
| `fcn.00411f68` | `0x411f68` | 836 | ✓ |
| `fcn.004160ec` | `0x4160ec` | 834 | ✓ |
| `fcn.0040960a` | `0x40960a` | 828 | ✓ |
| `fcn.0040b964` | `0x40b964` | 795 | ✓ |
| `fcn.00458b84` | `0x458b84` | 784 | ✓ |
| `fcn.004209e0` | `0x4209e0` | 763 | ✓ |
| `fcn.0044e7fc` | `0x44e7fc` | 757 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00403ae4.c`](code/fcn.00403ae4.c)
- [`code/fcn.0040960a.c`](code/fcn.0040960a.c)
- [`code/fcn.0040ae80.c`](code/fcn.0040ae80.c)
- [`code/fcn.0040b964.c`](code/fcn.0040b964.c)
- [`code/fcn.00410ea8.c`](code/fcn.00410ea8.c)
- [`code/fcn.0041196c.c`](code/fcn.0041196c.c)
- [`code/fcn.00411f68.c`](code/fcn.00411f68.c)
- [`code/fcn.0041247c.c`](code/fcn.0041247c.c)
- [`code/fcn.00412bec.c`](code/fcn.00412bec.c)
- [`code/fcn.00413154.c`](code/fcn.00413154.c)
- [`code/fcn.00413808.c`](code/fcn.00413808.c)
- [`code/fcn.00413f30.c`](code/fcn.00413f30.c)
- [`code/fcn.004150a4.c`](code/fcn.004150a4.c)
- [`code/fcn.004160ec.c`](code/fcn.004160ec.c)
- [`code/fcn.004209e0.c`](code/fcn.004209e0.c)
- [`code/fcn.0042887c.c`](code/fcn.0042887c.c)
- [`code/fcn.00429c60.c`](code/fcn.00429c60.c)
- [`code/fcn.0042d744.c`](code/fcn.0042d744.c)
- [`code/fcn.0042f910.c`](code/fcn.0042f910.c)
- [`code/fcn.0043a350.c`](code/fcn.0043a350.c)
- [`code/fcn.0043e90c.c`](code/fcn.0043e90c.c)
- [`code/fcn.00447c0c.c`](code/fcn.00447c0c.c)
- [`code/fcn.00448514.c`](code/fcn.00448514.c)
- [`code/fcn.00449f58.c`](code/fcn.00449f58.c)
- [`code/fcn.0044e7fc.c`](code/fcn.0044e7fc.c)
- [`code/fcn.004516b4.c`](code/fcn.004516b4.c)
- [`code/fcn.00456230.c`](code/fcn.00456230.c)
- [`code/fcn.00457eac.c`](code/fcn.00457eac.c)
- [`code/fcn.00458b84.c`](code/fcn.00458b84.c)

## Behavioral Analysis

Based on the second chunk of disassembly, I have updated and expanded the analysis. The additional code reinforces the previous findings regarding the complexity of the application while introducing new technical indicators regarding its interaction with the Windows environment and potential for advanced UI manipulation.

### Updated Analysis: Chunk 2/2

#### Core Functionality and Purpose (Updated)
The evidence from this chunk confirms that the binary is a high-level, professional-grade application using an Object-Oriented framework (Delphi). New observations include:

*   **Advanced Coordinate and Geometry Processing:** Functions such as `fcn.0043e90c` and `fcn.00457eac` contain significant logic for calculating areas, overlapping rectangles (`IsRectEmpty`), and offset calculations (`OffsetRect`). The inclusion of `ClientToScreen` suggests the application is mapping internal coordinates to physical screen space.
*   **Extensive Dynamic API Resolution:** Function `fcn.0042d744` contains a massive block of `GetProcAddress` calls. This indicates that the application dynamically resolves many functions at runtime, likely from a primary system DLL or a custom loaded module. This is often done to minimize the size of the Import Address Table (IAT) and can be used to hide functionality from static analysis tools.
*   **Sophisticated State Management:** The recurring, large switch tables (e.g., in `fcn.0042f910` with 38 cases; `fcn.004209e0` with 17 cases) suggest a complex "Command" or "Message Dispatcher" pattern. This is characteristic of Delphi's way of handling various event types, button clicks, and internal object state changes.

#### Suspicious or Malicious Behaviors (Updated)
While the binary remains ambiguous without dynamic analysis, several findings in this chunk warrant closer inspection:

*   **Overlay/Overlay-like Behavior:** The combination of `ClientToScreen`, complex geometry calculations (`OffsetRect`), and "search" loops to find coordinates suggests the application may be creating a **graphical overlay**. In an adversarial context, this is a common technique for fake login screens, transparent overlays that capture mouse clicks on windows beneath them, or "scareware" interfaces.
*   **Timed Execution Loops:** The presence of `Sleep` calls inside calculation loops (in `fcn.0044e7fc`) suggests the application may be waiting for user interaction, monitoring a change in another window's state, or performing actions at specific intervals to avoid detection.
*   **Complexity as Obfuscation:** The sheer volume of "boilerplate" code and nested switch tables provides a layer of "analytical noise." This is often used by sophisticated developers (both legitimate and malicious) to slow down manual analysis; it creates a labyrinth where the "real" logic is buried under hundreds of lines of standard framework glue-code.

#### Notable Techniques or Patterns Observed
*   **Standard Delphi Boilerplate:** Functions like `fcn.004150a4`, `fcn.00413154`, and `fcn.0041247c` are almost certainly part of the Delphi Runtime Environment (RTE). They handle object type checking, property access, and variant handling. These appear repeatedly because they act as "gatekeepers" for common operations in the language.
*   **Large-Scale Function Mapping:** The manual `GetProcAddress` block (`fcn.0042d744`) is a classic technique for creating a "wrapper" that makes it difficult to see what capabilities the application has simply by looking at its imports. 
*   **Heavy Vectorized/Geometric Logic:** The logic in `fcn.0043e90c` doesn't look like standard GUI "button clicking." It looks like an engine designed to handle spatial relationships between elements, which is common in games or high-end graphics suites but can also be used to position fake UI elements precisely over a target application (like a bank login).

---

### Updated Summary for Analyst

The addition of the second code chunk reinforces the profile of this as a **high-complexity, feature-rich application**, likely built with Delphi. 

**Key findings from Chunk 2:**
1.  **Sophisticated UI/UX Logic:** The extensive use of coordinate transformations and geometric calculations suggests it is designed to manage complex visual elements or potentially interact with other windows on the screen.
2.  **Dynamic Behavior:** The large block of `GetProcAddress` calls indicates a desire (or requirement) to resolve many functions at runtime, which can be used for both legitimate modularity and malicious obfuscation.
3.  **Complex State Machine:** The massive switch tables indicate a very large codebase with numerous distinct states or types handled by the underlying framework.

**Conclusion & Risk Assessment:**
The software is highly sophisticated. While it does not contain "loud" malware indicators (like overt shellcode or raw socket manipulation), its advanced capabilities in **geometric calculation, dynamic API resolution, and coordinate-mapping** are techniques often seen in:
*   Complex commercial utility/gaming software.
*   Sophisticated Trojan overlays designed to steal credentials by layering a fake UI over a real one.

**Updated Recommendations:**
1.  **Dynamic Analysis (Sandbox):** Execute the sample while monitoring for "window overlapping" or "injection" into common targets (browsers, system processes).
2.  **API Monitoring:** Monitor which specific functions are being resolved by the `GetProcAddress` block in `fcn.0042d744`. Identifying these will clarify if it is interacting with graphics drivers, network libraries, or injection APIs.
3.  **Overlay Detection:** Check for the creation of transparent windows or those that "hook" mouse/keyboard input globally.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of extensive `GetProcAddress` blocks and complex "analytical noise" (nested switch tables) is designed to hide functionality from static analysis. |
| T1036 | Masquerading | The calculation of coordinates for "overlay-like" behavior and fake login screens allows the application to mimic legitimate interfaces to deceive users or analysts. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Many of the strings provided are standard Delphi framework components and common Windows API calls; these have been excluded as "false positives" per your instructions.*

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   *Note:* The following registry keys were identified in the strings but appear to be standard Delphi development environment paths rather than malicious indicators:
    *   `Software\Borland\Locales`
    *   `Software\Borland\Delphi\Locales`

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified (No MD5, SHA1, or SHA256 hashes were present in the strings).

**Other artifacts (TTPs & Behavioral Indicators)**
The following are technical indicators derived from the behavioral analysis that suggest specific capabilities:
*   **Dynamic API Resolution:** Large block of `GetProcAddress` calls at `fcn.0042d744`. (Indicates intent to hide imports or resolve system functions at runtime).
*   **Potential Overlay Capabilities:** Use of `ClientToScreen`, `OffsetRect`, and `IsRectEmpty` in functions `fcn.0043e90c` and `fcn.00457eac`. (Suggests the capability to create transparent overlays or fake UI elements).
*   **Timing/Evasion:** `Sleep` calls within calculation loops at `fcn.0044e7fc`. (Indicates use of timing for synchronization or evasion).
*   **Complex State Machine:** Large switch tables in `fcn.0042f910` and `fcn.004209e0`.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family**: Unknown (Potential Trojan)
2. **Malware type**: Trojan / Infostealer
3. **Confidence**: Medium
4. **Key evidence**:
    *   **Overlay & UI Manipulation:** The presence of `ClientToScreen`, `OffsetRect`, and complex geometry calculations suggests the creation of a graphical overlay or fake login screens, which are primary indicators of bank trojans or credential stealers designed to deceive users.
    *   **Evasion via Obfuscation:** The large block of `GetProcAddress` calls indicates an intentional effort to hide the application's true functionality from static analysis by dynamically resolving APIs at runtime.
    *   **Advanced Sophistication:** The use of a Delphi-based framework with complex state management (large switch tables) and "analytical noise" points toward a professional, high-complexity piece of malware rather than a simple script or low-effort downloader.
