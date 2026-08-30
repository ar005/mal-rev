# Threat Analysis Report

**Generated:** 2026-08-15 15:35 UTC
**Sample:** `0ef3b534804f29e45d795cefec2581eb3aa78cbe3eed2cf18676e9ac5513a671_0ef3b534804f29e45d795cefec2581eb3aa78cbe3eed2cf18676e9ac5513a671.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ef3b534804f29e45d795cefec2581eb3aa78cbe3eed2cf18676e9ac5513a671_0ef3b534804f29e45d795cefec2581eb3aa78cbe3eed2cf18676e9ac5513a671.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 787,456 bytes |
| MD5 | `218872bb9d5657b6d5587ea1b5ce7f62` |
| SHA1 | `f1b900acc3753edcab9c30269d7bb60a393da949` |
| SHA256 | `0ef3b534804f29e45d795cefec2581eb3aa78cbe3eed2cf18676e9ac5513a671` |
| Overall entropy | 6.688 |
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
| `CODE` | 382,976 | 6.541 | No |
| `DATA` | 6,656 | 4.551 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 9,216 | 4.962 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.207 | No |
| `.reloc` | 28,672 | 6.659 | No |
| `.rsrc` | 358,400 | 6.241 | No |

### Imports

**kernel32.dll**: `Sleep`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WinHelpA`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `ShowCursor`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `GetErrorInfo`, `SysFreeString`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**gdi32.dll**: `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetWinMetaFileBits`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetMapMode`, `SetEnhMetaFileBits`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`
**ole32.dll**: `CreateStreamOnHGlobal`, `IsAccelerator`, `OleDraw`, `OleSetMenuDescriptor`, `CoCreateInstance`, `CoGetClassObject`, `CoUninitialize`, `CoInitialize`, `IsEqualGUID`
**comctl32.dll**: `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_SetDragCursorImage`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`

## Extracted Strings

Total strings found: **3018** (showing first 100)

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
Variant
TObject
TObject
System

IInterface
System
	IDispatch4
System
TInterfacedObject
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
	Exception@w@
EHeapException
EOutOfMemory
EInOutErrorPx@
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeError
EIntOverflow

EMathError

EInvalidOp
EZeroDividet{@
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
r
t%HtIHtm
_^[YY]
$Z]_^[
QQQQQQSVW3
QQQQQSVW
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00403978` | `0x403978` | 4053 | ✓ |
| `entry0` | `0x45e65c` | 3698 | ✓ |
| `fcn.00444a30` | `0x444a30` | 2312 | ✓ |
| `fcn.00444128` | `0x444128` | 2280 | ✓ |
| `fcn.0041e7fb` | `0x41e7fb` | 2042 | — |
| `fcn.0040a2bc` | `0x40a2bc` | 1921 | ✓ |
| `fcn.004527f4` | `0x4527f4` | 1750 | ✓ |
| `fcn.00424d5c` | `0x424d5c` | 1633 | ✓ |
| `fcn.00412c4c` | `0x412c4c` | 1362 | ✓ |
| `fcn.00412524` | `0x412524` | 1335 | ✓ |
| `fcn.00446474` | `0x446474` | 1183 | ✓ |
| `fcn.00426140` | `0x426140` | 1131 | ✓ |
| `fcn.0040fbec` | `0x40fbec` | 1097 | ✓ |
| `fcn.004106b0` | `0x4106b0` | 1088 | ✓ |
| `fcn.00436834` | `0x436834` | 1085 | ✓ |
| `fcn.0045bfd0` | `0x45bfd0` | 1018 | ✓ |
| `fcn.0043ae28` | `0x43ae28` | 978 | ✓ |
| `fcn.00411e70` | `0x411e70` | 965 | ✓ |
| `fcn.00429c28` | `0x429c28` | 947 | ✓ |
| `fcn.0042bdf4` | `0x42bdf4` | 905 | ✓ |
| `fcn.00454470` | `0x454470` | 902 | ✓ |
| `fcn.004111b4` | `0x4111b4` | 885 | ✓ |
| `fcn.0044dc78` | `0x44dc78` | 852 | ✓ |
| `fcn.00411908` | `0x411908` | 846 | ✓ |
| `fcn.00410cac` | `0x410cac` | 836 | ✓ |
| `fcn.0040900a` | `0x40900a` | 828 | ✓ |
| `fcn.0040ada0` | `0x40ada0` | 795 | ✓ |
| `fcn.0045515c` | `0x45515c` | 784 | ✓ |
| `fcn.0041ba94` | `0x41ba94` | 763 | ✓ |
| `fcn.0044adc0` | `0x44adc0` | 757 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00403978.c`](code/fcn.00403978.c)
- [`code/fcn.0040900a.c`](code/fcn.0040900a.c)
- [`code/fcn.0040a2bc.c`](code/fcn.0040a2bc.c)
- [`code/fcn.0040ada0.c`](code/fcn.0040ada0.c)
- [`code/fcn.0040fbec.c`](code/fcn.0040fbec.c)
- [`code/fcn.004106b0.c`](code/fcn.004106b0.c)
- [`code/fcn.00410cac.c`](code/fcn.00410cac.c)
- [`code/fcn.004111b4.c`](code/fcn.004111b4.c)
- [`code/fcn.00411908.c`](code/fcn.00411908.c)
- [`code/fcn.00411e70.c`](code/fcn.00411e70.c)
- [`code/fcn.00412524.c`](code/fcn.00412524.c)
- [`code/fcn.00412c4c.c`](code/fcn.00412c4c.c)
- [`code/fcn.0041ba94.c`](code/fcn.0041ba94.c)
- [`code/fcn.00424d5c.c`](code/fcn.00424d5c.c)
- [`code/fcn.00426140.c`](code/fcn.00426140.c)
- [`code/fcn.00429c28.c`](code/fcn.00429c28.c)
- [`code/fcn.0042bdf4.c`](code/fcn.0042bdf4.c)
- [`code/fcn.00436834.c`](code/fcn.00436834.c)
- [`code/fcn.0043ae28.c`](code/fcn.0043ae28.c)
- [`code/fcn.00444128.c`](code/fcn.00444128.c)
- [`code/fcn.00444a30.c`](code/fcn.00444a30.c)
- [`code/fcn.00446474.c`](code/fcn.00446474.c)
- [`code/fcn.0044adc0.c`](code/fcn.0044adc0.c)
- [`code/fcn.0044dc78.c`](code/fcn.0044dc78.c)
- [`code/fcn.004527f4.c`](code/fcn.004527f4.c)
- [`code/fcn.00454470.c`](code/fcn.00454470.c)
- [`code/fcn.0045515c.c`](code/fcn.0045515c.c)
- [`code/fcn.0045bfd0.c`](code/fcn.0045bfd0.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, here is the updated analysis. The new data reinforces the previous findings while introducing several specific indicators regarding how the application handles data, interacts with the Windows subsystem, and potentially attempts to evade detection.

---

### Updated Analysis Report (Chunk 1 & 2 Combined)

#### **Core Functionality and Purpose**
The analysis confirms that this is a complex **Windows GUI application** built using the **Embarcadero Delphi (Pascal)** framework. The sheer volume of "switch-case" logic indicates a heavy reliance on the VCL (Visual Component Library).

*   **Sophisticated Data Handling (Variant Types):** The recurring, massive switch blocks (e.g., `fcn.0040fbec`, `fcn.004106b0`, and `fcn.0045bfd0`) are classic markers of the Delphi **Variant** type. This allows the program to handle "multi-type" data (variables that can switch between strings, integers, dates, etc.). In a security context, this is often used when an application interacts with scripting engines or complex COM objects—common in tools designed to process heterogeneous commands from a remote server.
*   **Advanced Graphics Rendering:** Function `fcn.00426140` shows heavy use of `CreateDIBSection`, `CreateCompatibleDC`, and `SelectObject`. This confirms the application is performing advanced graphics manipulation, likely for custom-rendered UI elements or overlaying content onto other windows.
*   **Complex Geometry/Layout Logic:** Functions like `fcn.0043ae28` (handling `IsRectEmpty` and `OffsetRect`) and `fcn.00454470` indicate a robust system for calculating window coordinates and UI layout, often used to create polished "fake" interfaces that mimic standard Windows windows perfectly.

#### **Suspicious or Malicious Behaviors**
The second chunk introduces more specific techniques commonly observed in sophisticated malware samples:

*   **Dynamic API Resolution (Evasion):** Function `fcn.00429c28` is a significant finding. It performs a loop of `GetProcAddress` calls to populate a large array of function pointers from a dynamically loaded library (`LoadLibraryA`). This technique—**hiding the Import Address Table (IAT)**—is used to prevent static analysis tools from seeing which Windows functions the program actually calls until it is running in memory.
*   **Large Data Mapping/Translation:** Function `fcn.0042bdf4` contains a massive switch table (nearly 100 cases) that maps input values into ranges. This could be used for **character set translation**, **instruction decoding**, or mapping internal state machine transitions, which are common in complex packers or trojan droppers.
*   **Potential Scripting/Command Processing:** The high density of `fcn.0045bfd0` (63 cases) suggests the inclusion of a scriptable component or a logic engine capable of processing varied commands.

#### **Techniques and Patterns**
*   **Standard Library Bloat vs. Malicious Logic:** A significant portion of the disassembly consists of standard Delphi runtime code. This "bloat" acts as a natural obfuscation; it makes it difficult for an analyst to distinguish between a legitimate (but complex) GUI routine and malicious logic without deep tracing.
*   **Junk Code/Anti-Analysis:** As noted in the first chunk, the entry point contains repetitive arithmetic. Coupled with the Dynamic API resolution found in chunk 2, this suggests the author intended to frustrate automated sandboxes and static disassemblers.
*   **Advanced Memory Management:** The use of `DIBSection` and manual bit manipulation (seen in the math/floating-point functions like `fcn.00411e70`) indicates that even if the app is a "wrapper," it contains a significant amount of custom logic beyond basic GUI display.

---

### Updated Summary for Report
*   **Nature:** Sophisticated **Delphi-based Trojan/Spyware wrapper**.
*   **Key Capabilities:** 
    *   High-level GUI manipulation and custom graphic rendering (GDI).
    *   Complex data handling via "Variant" types, suggesting interaction with scripts or remote commands.
    *   **Anti-Analysis Techniques:** Utilization of Dynamic API loading (`GetProcAddress`) to hide imports and the use of repetitive logic/junk code to hinder automated analysis.
*   **Malware Indicators:** 
    1.  **IAT Obfuscation:** High likelihood of hidden functionality via dynamically resolved functions.
    2.  **Complex State Logic:** Extensive switch-case trees used for multi-stage execution.
    3.  **Advanced UI Overlay:** Strong evidence of non-standard, highly customized graphics management.

**Risk Assessment:** The presence of dynamic API resolution and a high degree of "hidden" logic suggests this binary is not a simple script; it is likely part-of-a larger malware suite (such as an info-stealer or remote access trojan) designed to bypass basic security filters while providing a complex, interactive interface for the user.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of junk code, repetitive arithmetic, and dynamic API resolution (via `GetProcAddress`) is designed to hinder static analysis and frustrate automated sandboxes. |
| **T1036** | Masquerading | The use of advanced GDI functions to create "fake" interfaces that mimic standard Windows windows allows the application to blend in with legitimate software. |
| **T1059** | Command and Scripting Interpreter | The high density of switch-case logic and variant types suggests a system designed to process complex, multi-type commands or scripts, potentially from a remote source. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Standard Delphi compiler artifacts (e.g., `SOFTWARE\Borland\Delphi\...` and standard system DLLs like `kernel32.dll`) have been excluded as false positives.*

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified (Relevant strings provided were standard application framework paths).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Techniques/Behavioral IOCs:**
    *   **IAT Obfuscation:** Use of `GetProcAddress` and `LoadLibraryA` in a loop to dynamically resolve functions and hide the Import Address Table.
    *   **Advanced Logic Masking:** Extensive use of "Variant" type switch-case blocks (e.g., `fcn.0040fbec`, `fcn.004106b0`) to handle multi-type data, likely for processing remote commands or scripting.
    *   **GDI Graphics Manipulation:** Utilization of `CreateDIBSection` and `CreateCompatibleDC` for advanced UI rendering (potential overlay functionality).
    *   **State Machine Logic:** Large switch tables (nearly 100 cases) used to map input values into internal states, common in multi-stage malware.
    *   **Delphi-based Wrapper:** The binary is identified as a sophisticated Delphi/Pascal construction designed for concealment of malicious logic behind standard library bloat.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader (or backdoor)
3. **Confidence**: Medium

4. **Key evidence**:
*   **Sophisticated Obfuscation & Evasion:** The sample employs advanced techniques to hinder analysis, specifically the use of dynamic API resolution (`GetProcAddress`/`LoadLibraryA`) to hide its Import Address Table (IAT), and "junk code" at the entry point to frustrate automated sandboxes.
*   **Complex Command Logic:** The extensive use of Delphi "Variant" types and massive switch-case tables suggests a robust internal state machine designed to process complex, multi-typed data or commands from a remote server.
*   **Deceptive UI/GDI Manipulation:** The presence of advanced GDI functions (`CreateDIBSection`, `CreateCompatibleDC`) indicates the application is designed to create custom overlays or "fake" interfaces to hide its true activities from the user.
