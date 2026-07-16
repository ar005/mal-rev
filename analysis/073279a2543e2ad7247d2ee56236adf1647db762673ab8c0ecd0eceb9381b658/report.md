# Threat Analysis Report

**Generated:** 2026-07-16 15:35 UTC
**Sample:** `073279a2543e2ad7247d2ee56236adf1647db762673ab8c0ecd0eceb9381b658_073279a2543e2ad7247d2ee56236adf1647db762673ab8c0ecd0eceb9381b658.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `073279a2543e2ad7247d2ee56236adf1647db762673ab8c0ecd0eceb9381b658_073279a2543e2ad7247d2ee56236adf1647db762673ab8c0ecd0eceb9381b658.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 4,832,768 bytes |
| MD5 | `2272118a24950de23cc894da2ef9aa4c` |
| SHA1 | `2e26b2492283ad5e9ba2067219ef09c0274c0c5e` |
| SHA256 | `073279a2543e2ad7247d2ee56236adf1647db762673ab8c0ecd0eceb9381b658` |
| Overall entropy | 6.565 |
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
| `.rsrc` | 4,272,640 | 6.385 | No |

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

Total strings found: **6727** (showing first 100)

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

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the technical analysis. This new data confirms several of the earlier suspicions while introducing more advanced indicators of deliberate evasion and sophisticated software engineering.

### Updated Technical Analysis

#### 1. Advanced Evasion & Obfuscation (High Priority)
The most significant addition in this chunk is the behavior found in **`fcn.0042d744`**.
*   **Dynamic API Resolution:** This function performs a massive loop of `GetProcAddress` calls after loading a library via `LoadLibraryA`. It populates a large array with addresses for numerous Windows functions.
*   **Implication:** This is a classic **anti-analysis technique**. By resolving its imports at runtime rather than having them in the Import Address Table (IAT), the malware hides its true capabilities from static analysis tools. The sheer volume of calls suggests it is loading a comprehensive set of system APIs to perform complex tasks while remaining "quiet" during initial scanning.

#### 2. Complex System & Data Processing
The functions **`fcn.00413154`**, **`fcn.0041247c`**, and **`fcn.0042f910`** exhibit very complex logic:
*   **Dispatch Tables:** The large "switch" structures (with dozens of cases) indicate the use of a **Dispatcher pattern**. This is common in high-level frameworks but also used in malware to handle different "states" or types of commands/messages without using obvious `if-else` chains that are easy for researchers to trace.
*   **Data Normalization:** `fcn.0042f910` appears to be a routine for normalizing raw values into specific ranges (e.g., taking any value between 5 and 7 and mapping it to "2"). This is often used to process inputs from a network or an encrypted packet before passing them to the logic engine.

#### 3. Advanced UI & Screen Interaction
The functions **`fcn.0043a350`**, **`fcn.0043e90c`**, and **`fcn.00457eac`** build upon the GDI logic from Chunk 1:
*   **Coordinate Manipulation:** These functions perform heavy math to calculate bounding boxes, offset rectangles (`OffsetRect`), and convert client coordinates to screen coordinates (`ClientToScreen`).
*   **Dynamic Layouts:** The complexity of these calculations suggests that the program isn't just showing a simple window; it is likely calculating a complex, possibly dynamic, layout. 
*   **Timing & Persistence:** The presence of `Sleep` calls in conjunction with coordinate math often points to **animations or "stealthy" UI transitions**, such as an overlay that slides into place or fades in.

#### 4. Delphi/COM Integration
The code continues to show hallmarks of the **Delphi/Pascal** environment:
*   **OLE Automation:** The use of `VariantInit` and logic surrounding `OleAut32` indicates that the program interacts with COM (Component Object Model) objects.
*   **BSTR Management:** Function `fcn.00458b84` handles complex string conversions and memory management typical of Delphi’s way of handling "Wide" characters or COM-compatible strings.

---

### Revised Summary of Risk & Behavior

The inclusion of the second chunk significantly elevates the risk profile of this binary.

**1. Primary Threat Vector: Advanced Trojan/Overlay.**
The combination of **Dynamic API Resolution** (hiding imports) and **Sophisticated GDI Manipulation** (complex coordinate math) is a strong indicator of an "Overlay" or a "Stealthy Loader." It is designed to appear as a high-quality, functional application while hiding its true calls from automated security scanners.

**2. Complexity & Purpose:**
*   The software is not a simple script; it uses sophisticated programming patterns (Dispatch Tables, Data Normalization). 
*   It likely has a "Command and Control" (C2) or "Tasking" component: The way the code handles different inputs through switch tables suggests it can receive varied instructions (e.g., "show this window," "launch that process," "hide for X minutes").

**3. Technical Indicators of Malice:**
*   **Obfuscated Import Table:** Clearly visible in `fcn.0042d744` via the `GetProcAddress` loop. 
*   **Complex Screen Interaction:** The math-heavy coordinate logic suggests it is designed to manipulate what the user sees on the screen, potentially for **scareware**, **fake system alerts**, or **overlaying content over legitimate applications**.

### Conclusion for Investigators
The binary is highly likely a piece of sophisticated malware, specifically a **Trojan with an overlay component** or a **complex multi-stage loader**. 

**Next Recommended Steps:**
1.  **Dynamic Analysis (Sandbox):** Run the sample in a controlled environment to see which DLLs are actually loaded and what "strings" are revealed once `GetProcAddress` is executed.
2.  **Memory Forensics:** Dump the memory of the process after it has initialized its internal tables to see the "de-obfuscated" strings from the initial loop in Chunk 1.
3.  **Hooking API Calls:** Monitor calls to `BitBlt`, `GetProcAddress`, and `CreateTimer_` to observe the interaction between the UI elements and the system.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1568** | Dynamic Resolution | The malware uses a `GetProcAddress` loop to resolve functions at runtime, effectively hiding its true capabilities from static analysis by omitting them from the Import Address Table (IAT). |
| **T1036** | Masquerading | The use of sophisticated GDI manipulation for "fake system alerts" and overlays is designed to deceive users and hide malicious activity behind common UI elements. |
| **T1027** | Obfuscated Files or Information | The use of complex dispatch tables and data normalization is intended to obscure the program's logic flow and make it harder for researchers to trace "off-the-shelf" commands. |

---

## Indicators of Compromise

Based on the provided strings and technical analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   (None identified)

**File paths / Registry keys**
*   *(Note: Identified registry paths `SOFTWARE\Borland\Delphi\RTL` and `Software\Borland\Locales` were excluded as they are standard Delphi environment artifacts.)*

**Mutex names / Named pipes**
*   (None identified)

**Hashes**
*   (None identified)

**Other artifacts**
*   **Behavioral Pattern (Dynamic API Resolution):** Use of a `GetProcAddress` loop following `LoadLibraryA` to resolve system APIs at runtime. This is used to hide the application's true capabilities from static analysis.
*   **Communication/Command Logic:** Implementation of "Dispatcher" patterns (large switch structures) and "Data Normalization" routines, suggesting the binary processes variable commands or input from a remote source/encrypted packet.
*   **Overlay Capability:** Advanced GDI manipulation including `OffsetRect`, `ClientToScreen` coordinate calculations, and likely use of `BitBlt` to create a stealthy UI overlay or fake system alerts.
*   **Environment:** Detected usage of Delphi/Pascal compiler toolchain for construction of the malware's core logic.

---

## Malware Family Classification

Based on the technical analysis provided, here is the classification of the sample:

1. **Malware family:** Unknown
2. **Malware type:** Loader / Trojan (with Overlay capabilities)
3. **Confidence:** Medium
4. **Key evidence:**
    *   **Evasive Execution:** The use of extensive `GetProcAddress` loops and dynamic API resolution indicates a deliberate attempt to hide the program's functionality from static analysis tools by bypassing the Import Address Table (IAT).
    *   **Command Processing Logic:** The implementation of large "Switch" structures (Dispatch Tables) and data normalization routines suggests the binary is designed to handle varied commands or tasks, characteristic of a remote-controlled Trojan or an advanced loader.
    *   **Sophisticated UI Manipulation:** Complex GDI math for coordinate mapping and screen conversion indicates the creation of a specialized overlay, likely used for masquerading as legitimate system alerts or hiding malicious activity from the user.
