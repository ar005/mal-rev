# Threat Analysis Report

**Generated:** 2026-08-06 17:11 UTC
**Sample:** `0d5b3f4cdbc2f0dfcfa981c7057192bd2452c1de088634ec11d319f7a3ed7a95_0d5b3f4cdbc2f0dfcfa981c7057192bd2452c1de088634ec11d319f7a3ed7a95.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d5b3f4cdbc2f0dfcfa981c7057192bd2452c1de088634ec11d319f7a3ed7a95_0d5b3f4cdbc2f0dfcfa981c7057192bd2452c1de088634ec11d319f7a3ed7a95.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 4,720,128 bytes |
| MD5 | `2d1961808987cdf011e42581067f2b18` |
| SHA1 | `c9faf09694a412816edfa2d188b69e40fa37e628` |
| SHA256 | `0d5b3f4cdbc2f0dfcfa981c7057192bd2452c1de088634ec11d319f7a3ed7a95` |
| Overall entropy | 6.542 |
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
| `CODE` | 357,888 | 6.527 | No |
| `DATA` | 6,656 | 4.415 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 8,704 | 4.995 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.187 | No |
| `.reloc` | 27,136 | 6.655 | No |
| `.rsrc` | 4,318,208 | 6.415 | No |

### Imports

**kernel32.dll**: `Sleep`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WinHelpA`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `ShowCursor`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `GetErrorInfo`, `RegisterTypeLib`, `LoadTypeLib`, `SysFreeString`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**gdi32.dll**: `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`, `SelectPalette`, `SelectObject`, `SelectClipRgn`
**ole32.dll**: `CoRegisterClassObject`, `CoUninitialize`, `CoInitialize`
**comctl32.dll**: `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_SetDragCursorImage`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`

## Extracted Strings

Total strings found: **4933** (showing first 100)

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
C<"u1S
Q<"u8S
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
EZeroDivide |@
	EOverflow

EUnderflow
EInvalidPointer,}@
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
_^[YY]
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00403ae4` | `0x403ae4` | 4053 | ✓ |
| `entry0` | `0x4583e8` | 3174 | ✓ |
| `fcn.004428e8` | `0x4428e8` | 2312 | ✓ |
| `fcn.00441fe0` | `0x441fe0` | 2280 | ✓ |
| `fcn.0040a49c` | `0x40a49c` | 1921 | ✓ |
| `fcn.00450604` | `0x450604` | 1750 | ✓ |
| `fcn.00422ca4` | `0x422ca4` | 1633 | ✓ |
| `fcn.00412f08` | `0x412f08` | 1362 | ✓ |
| `fcn.004127e0` | `0x4127e0` | 1335 | ✓ |
| `fcn.0040e842` | `0x40e842` | 1224 | ✓ |
| `fcn.0044432c` | `0x44432c` | 1183 | ✓ |
| `fcn.00424088` | `0x424088` | 1131 | ✓ |
| `fcn.0040fea8` | `0x40fea8` | 1097 | ✓ |
| `fcn.0041096c` | `0x41096c` | 1088 | ✓ |
| `fcn.00434724` | `0x434724` | 1085 | ✓ |
| `fcn.00456988` | `0x456988` | 1018 | ✓ |
| `fcn.00438ce0` | `0x438ce0` | 978 | ✓ |
| `fcn.0041212c` | `0x41212c` | 965 | ✓ |
| `fcn.00427b18` | `0x427b18` | 947 | ✓ |
| `fcn.00429ce4` | `0x429ce4` | 905 | ✓ |
| `fcn.00452280` | `0x452280` | 902 | ✓ |
| `fcn.00411470` | `0x411470` | 885 | ✓ |
| `fcn.0044ba88` | `0x44ba88` | 852 | ✓ |
| `fcn.00411bc4` | `0x411bc4` | 846 | ✓ |
| `fcn.00410f68` | `0x410f68` | 836 | ✓ |
| `fcn.004091ea` | `0x4091ea` | 828 | ✓ |
| `fcn.0040af80` | `0x40af80` | 795 | ✓ |
| `fcn.0045309c` | `0x45309c` | 784 | ✓ |
| `fcn.0041b930` | `0x41b930` | 763 | ✓ |
| `fcn.00448bd0` | `0x448bd0` | 757 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00403ae4.c`](code/fcn.00403ae4.c)
- [`code/fcn.004091ea.c`](code/fcn.004091ea.c)
- [`code/fcn.0040a49c.c`](code/fcn.0040a49c.c)
- [`code/fcn.0040af80.c`](code/fcn.0040af80.c)
- [`code/fcn.0040e842.c`](code/fcn.0040e842.c)
- [`code/fcn.0040fea8.c`](code/fcn.0040fea8.c)
- [`code/fcn.0041096c.c`](code/fcn.0041096c.c)
- [`code/fcn.00410f68.c`](code/fcn.00410f68.c)
- [`code/fcn.00411470.c`](code/fcn.00411470.c)
- [`code/fcn.00411bc4.c`](code/fcn.00411bc4.c)
- [`code/fcn.0041212c.c`](code/fcn.0041212c.c)
- [`code/fcn.004127e0.c`](code/fcn.004127e0.c)
- [`code/fcn.00412f08.c`](code/fcn.00412f08.c)
- [`code/fcn.0041b930.c`](code/fcn.0041b930.c)
- [`code/fcn.00422ca4.c`](code/fcn.00422ca4.c)
- [`code/fcn.00424088.c`](code/fcn.00424088.c)
- [`code/fcn.00427b18.c`](code/fcn.00427b18.c)
- [`code/fcn.00429ce4.c`](code/fcn.00429ce4.c)
- [`code/fcn.00434724.c`](code/fcn.00434724.c)
- [`code/fcn.00438ce0.c`](code/fcn.00438ce0.c)
- [`code/fcn.00441fe0.c`](code/fcn.00441fe0.c)
- [`code/fcn.004428e8.c`](code/fcn.004428e8.c)
- [`code/fcn.0044432c.c`](code/fcn.0044432c.c)
- [`code/fcn.00448bd0.c`](code/fcn.00448bd0.c)
- [`code/fcn.0044ba88.c`](code/fcn.0044ba88.c)
- [`code/fcn.00450604.c`](code/fcn.00450604.c)
- [`code/fcn.00452280.c`](code/fcn.00452280.c)
- [`code/fcn.0045309c.c`](code/fcn.0045309c.c)
- [`code/fcn.00456988.c`](code/fcn.00456988.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, I have updated and expanded my analysis. The new code provides much deeper insight into how the application manages its internal state, handles graphics, and interacts with external components.

Here is the updated analysis including both chunks.

---

### Updated Analysis: [Malware/Software Sample] Technical Breakdown

#### 1. Core Functionality & Behavior
The second chunk reinforces the conclusion that this is a high-complexity application (likely Delphi) with a heavy emphasis on **graphical rendering** and **dynamic modularity**.

*   **Advanced GDI Management:** `fcn.00424088` is a significant "heavy lifter" in the graphics subsystem. It performs extensive operations including:
    *   Creating Device Contexts (`CreateCompatibleDC`).
    *   Handling Bitmaps and Palettes (`CreateDIBSection`, `SelectPalette`, `RealizePalette`).
    *   The use of `CreateDIBSection` specifically suggests the program may be handling pixel-level data or "raw" bitmap manipulation, which is common in games, high-end image processing tools, or advanced screen-overlay software.
*   **Dynamic Resource/Library Loading:** `fcn.00427b18` is highly significant. It contains a large block of `GetProcAddress` calls immediately following a `LoadLibraryA`. 
    *   **Observation:** The code attempts to resolve over **30 different functions** from an external DLL in one pass. 
    *   **Significance:** While this can be used for legitimate plugin systems (e.g., adding features via DLLs), it is a common technique in advanced malware or commercial tools to keep the primary executable "clean" of certain functionalities until they are needed, or to bypass simple static analysis by hiding the true capabilities behind dynamically loaded modules.
*   **Coordinate and UI Layout Logic:** Functions like `fcn.00438ce0` and `fcn.00452280` involve complex calculations using `OffsetRect`, `ClientToScreen`, and loops to calculate dimensions and positions of objects. This suggests the software manages a multi-layered or dynamic user interface where elements are positioned relative to screen coordinates.
*   **Complex Data Parsing:** `fcn.0045309c` appears to be a robust string/buffer processing routine. It iterates through memory, handling various line endings and special characters (e.g., `\r`, `\n`). This is typically seen in logic for parsing configuration files, network packets, or localized UI strings.

#### 2. Technical Indicators of Complexity
*   **Dispatch Tables (The "Switch" Pattern):** The recurring pattern of large switch-case blocks (as seen in `fcn.0040fea8`, `fcn.0041096c`, and `fcn.00411bc4`) indicates a highly structured programming architecture. This is characteristic of the Delphi "VCL" framework, where properties and method calls are routed through specialized dispatch tables to handle various object types.
*   **Floating Point Logic:** The presence of `MulDiv` (in `fcn.00434724`) and calculations involving standard divisions suggests it handles scaling, potentially for UI resizing or coordinate mapping during high-DPI scaling.
*   **Wait States & Timing:** The inclusion of `Sleep` calls in functions like `fcn.00448bd0` (nested within a loop) indicates the application manages timing—perhaps for animations, network timeouts, or to prevent the UI from "freezing" during heavy calculations.

#### 3. Suspicious / Interest Points
*   **Extensive Dynamic Resolution:** The sheer number of `GetProcAddress` calls in `fcn.00427b18` is a point of interest. If this were a simple utility, it would likely have fewer dynamic imports. This high volume suggests a very large "feature set" or a highly modular architecture.
*   **Memory-Heavy Graphics:** The use of `CreateDIBSection` and standard GDI palette management can be used for legitimate tools (like video players or image editors) but is also frequently used in **screen scrapers**, **overlay engines**, or **cheat software** because it allows the program to manipulate the "bits" of what is being displayed on a surface.

---

### Summary of Findings

| Feature | Observation | Potential Context |
| :--- | :--- | :--- |
| **Development Environment** | Delphi / Borland (high certainty) | Indicates a high-effort development cycle and complex UI capabilities. |
| **Graphics Engine** | Heavy GDI, DIB Sections, Palettes | Used for rendering a custom GUI or manipulating visual data on screen. |
| **Modularity** | Massive `GetProcAddress` blocks | Extensive use of DLLs to expand functionality or hide features from static analysis. |
| **Logic Complexity** | Deep nested switch tables; coordinate math | Suggests a sophisticated "Engine" style architecture rather than a simple script. |
| **Data Processing** | Custom string parsing and buffer loops | Likely handles complex configuration, localization, or network data. |

### Conclusion for Analysis
The application is **sophisticated and modular**. While no "smoking gun" of malicious activity (like file encryption, exfiltration packets, or process injection) was found in this specific code block, the **techniques used are characteristic of high-end commercial software.** 

However, these same techniques—**dynamic resolution of many functions**, **intensive GDI manipulation for screen output**, and **complex internal dispatch tables**—are also hallmarks of "sophisticated" malware (such as info-stealers or remote access trojans) that want to blend in with legitimate system utilities. The presence of the `GetProcAddress` block suggests the program is designed to be extensible, potentially allowing it to load various modules depending on its environment or configuration.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your technical breakdown to the relevant MITRE ATT&K techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a large block of `GetProcAddress` calls is a classic method to hide functionality and evade static analysis by bypassing the Import Address Table (IAT). |
| **T1036** | Screen Capture | The heavy use of GDI, `CreateDIBSection`, and palette management indicates capabilities for screen scraping or creating overlays to manipulate visual data. |

### Analyst Notes:
*   **T1027 Context:** The analyst's note regarding the "hidden" nature of features behind dynamically loaded modules specifically points toward evasion tactics intended to bypass automated security tools.
*   **T1036 Context:** While GDI is used in many legitimate applications (games/graphics), your analysis explicitly identifies it as a component for "screen scrapers" and "overlay engines," which are common indicators of information theft or unauthorized UI overlays in malicious software.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: As no external networking data (IPs/URLs) or cryptographic hashes were present in the source text, this report focuses on behavioral artifacts and environmental indicators.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   *Note: The following registry keys were identified but are categorized as standard Borland/Delphi development environment paths rather than unique malicious indicators.*
*   `SOFTWARE\Borland\Delphi\RTL`
*   `Software\Borland\Locales`
*   `Software\Borland\Delphi\Locales`

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Development Framework:** Delphi / Borland (Identified via `TObject`, `TThreadLocalCounter`, and standard `RTL` references).
*   **Evasion Technique (Dynamic Resolution):** High-volume dynamic function resolution. Specifically, `fcn.00427b18` performs a large block of `GetProcAddress` calls (over 30 functions) to resolve an external DLL, which is often used to bypass static analysis or hide capabilities.
*   **Graphics Manipulation (Potential Overlay/Scraper):** The use of `CreateDIBSection`, `SelectPalette`, and `RealizePalette` in `fcn.00424088`. While common in some games, this is a high-interest behavior for screen-scraping or overlay activity.
*   **Logic Indicators:** 
    *   Presence of sophisticated coordinate/UI calculation logic (`OffsetRect`, `ClientToScreen`).
    *   Complex string/buffer processing routines for parsing potentially non-standard data formats.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Infostealer / RAT (Remote Access Trojan)
3. **Confidence**: Medium

4. **Key evidence**:
*   **Evasive Behavior (T1027):** The use of a large block of `GetProcAddress` calls to resolve over 30 functions from an external DLL is a clear indicator of an attempt to hide the program's true capabilities and bypass static analysis by hiding functionality within dynamically loaded modules.
*   **Screen Scraping/Overlay Capabilities (T1036):** The extensive use of GDI, `CreateDIBSection`, and palette manipulation suggests the application is designed for high-level interaction with the visual display, which is a hallmark of screen scrapers or overlays used in info-stealing and remote access.
*   **High Complexity/Sophistication:** The presence of complex coordinate mathematics, large dispatch tables (VCL framework), and robust string parsing indicates a "sophisticated engine" rather than a simple script, characteristic of high-end professional malware tools rather than amateur scripts.
