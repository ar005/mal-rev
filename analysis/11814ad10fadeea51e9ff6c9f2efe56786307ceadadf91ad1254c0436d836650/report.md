# Threat Analysis Report

**Generated:** 2026-08-23 18:53 UTC
**Sample:** `11814ad10fadeea51e9ff6c9f2efe56786307ceadadf91ad1254c0436d836650_11814ad10fadeea51e9ff6c9f2efe56786307ceadadf91ad1254c0436d836650.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11814ad10fadeea51e9ff6c9f2efe56786307ceadadf91ad1254c0436d836650_11814ad10fadeea51e9ff6c9f2efe56786307ceadadf91ad1254c0436d836650.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 5,894,416 bytes |
| MD5 | `1cd6b36d516c507d51b82ccec97ed208` |
| SHA1 | `66f65c0bce9ac325ce658be5f3b8666210cb4f97` |
| SHA256 | `11814ad10fadeea51e9ff6c9f2efe56786307ceadadf91ad1254c0436d836650` |
| Overall entropy | 5.547 |
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
| `.rsrc` | 5,457,920 | 5.314 | No |

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

Total strings found: **52960** (showing first 100)

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

Based on the additional disassembly provided in chunk 2, I have updated and expanded the analysis. The presence of more "mega-switch" structures and heavy string manipulation further confirms certain architectural traits while providing more detail on how the application handles its internal logic.

### Updated Analysis Summary

#### Core Functionality & Architecture
The evidence reinforces that this is a **sophisticated, high-level application**, likely built with the Delphi/Pascal framework. The code exhibits several "high-level" patterns common in complex software:

*   **Massive Command Dispatchers (Switch Case Pattern):** Several functions (`fcn.004119d4`, `fcn.00410d18`, `fcn.0041146c`, `fcn.00410810`, and `fcn.0041b1dc`) are nearly identical in structure. They feature large switch-case blocks that act as **dispatchers**. 
    *   *Meaning:* These functions receive a "Type ID" or "Action Code" (e.g., from a file, a network packet, or a UI interaction) and branch to the appropriate logic. This is a standard way for software to handle diverse commands using a unified interface.
*   **Dynamic API Mapping & Library Loading:** Function `fcn.00428e18` shows a significant amount of code dedicated to calling `GetProcAddress` repeatedly in a block. 
    *   *Meaning:* This is the standard method by which the Delphi runtime resolves functions from system DLLs at startup. The sheer number of calls suggests the application links against many internal components or external libraries, typical for large software suites (like games or professional tools).
*   **Sophisticated String & Memory Management:** Function `fcn.00455abc` handles complex logic involving "BSTR" strings and memory freeing (`SysFreeString`). 
    *   *Meaning:* The code is handling long or complex strings, potentially during a parsing phase or when preparing data to be displayed in the UI.
*   **Geometric Calculations & Coordinate Mapping:** Function `fcn.00454f2c` utilizes `ClientToScreen` and `OffsetRect`. 
    *   *Meaning:* This confirms the **GUI focus**. The code is calculating where elements appear on the screen relative to a window, common in game engines or complex desktop applications with custom UI components.

#### Technical Findings from Chunk 2
*   **Complexity as a Feature (not necessarily malice):** The repetitive nature of the "Switch Tables" might look like obfuscation at first glance, but they are more characteristic of **compiler-generated code**. When an application has many different types of objects or actions, the compiler generates these large tables to route logic efficiently.
*   **Timing and State Management:** Function `fcn.0044b87c` includes calls to `Sleep` inside loops that involve calculation offsets. This suggests a system for managing **frame-timing, animations, or asynchronous tasks**, ensuring the UI doesn't "freeze" while waiting for an action to complete.
*   **Dense Logic in Script/Data Handling:** The function `fcn.0044e734` contains nested loops and several check points against specific values (like `\x01`, `\x02`). This indicates the engine is likely processing a **data file or script** to determine how objects should behave in the software's environment.

#### Security Analysis & Observation
*   **Obfuscation Profile:** The code does not show typical "malware-specific" obfuscation (like junk-code insertion designed to confuse an analyst or encryption of strings). Instead, it shows **complexity through architecture**. It is complex because it is a large project with many components.
*   **Risk Assessment remains Moderate/Contextual:** 
    *   The `GetProcAddress` block in `fcn.00428e18` means the program is loading many capabilities into memory. While this is normal for a game or suite, an analyst should check *which* DLLs are being loaded. If it loads unusual system libraries (like `wininet.dll`, `ws2_32.dll`) alongside common graphics ones, further investigation into its networking/file-access behavior would be warranted.
    *   The use of `ClientToScreen` and `OffsetRect` confirms the ability to interact with window coordinates—useful for UI but also used in "overlay" type software (such as gaming cheats or remote access tools).

### Summary Table: Key Function Analysis (Chunk 2)

| Function | Primary Logic | Significance |
| :--- | :--- | :--- |
| `fcn.004119d4` / `0x410d18` / `0x41146c` | Dispatch Tables | Core engine logic; handles multi-type inputs/actions. |
| `fcn.00428e18` | DLL/API Resolution | Bootstrapping the application's capabilities. |
| `fcn.00454f2c` | Geometry/Windowing | Mapping internal game/app coordinates to screen space. |
| `fcn.00455abc` | String Processing | Managing complex data strings (likely from a parser). |
| `fcn.0044b87c` | Timing & Intervals | Handling animations, delays, or state updates. |

**Final Synthesis:** The program is highly structured and appears to be part of a professional-grade **graphical application suite**. It uses complex logic to manage various system types (likely via the Delphi framework). While it possesses complexity that *could* hide intent, the current indicators point toward a high-overhead software environment rather than an intentional attempt to hide malicious functionality.

---

## MITRE ATT&CK Mapping

Based on the behavior analysis provided, here is the mapping to the MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1106 | Native API | The use of `GetProcAddress` in large blocks indicates dynamic resolution of system functions at runtime, a common method for loading capabilities while avoiding certain static analysis checks. |
| T1059 | Command and Scripting Interpreter | The presence of "Massive Command Dispatchers" that route logic based on "Type ID" or "Action Code" mirrors the way multi-functional software (and malware) processes internal commands. |
| T1412 | System Timing | The inclusion of `Sleep` calls within loops is a common behavior for managing frame timing, animations, or intentionally delaying execution to evade detection. |
| T1027 | Obfuscated Files or Information | Sophisticated string management (BSTR) and complex parsing logic often indicate the handling of complex data structures or the decoding of potentially obfuscated information. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the assessment of Indicators of Compromise (IOCs).

### **Analysis Summary**
The analysis indicates that the binary is a sophisticated application developed using the **Delphi/Pascal framework**. While the code contains complex "mega-switch" structures and dynamic API mapping, these are characteristic of large-scale commercial software (such as games or professional utility suites) rather than malicious obfuscation.

### **Extracted IOCs**

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: References to `Software\Borland\Delphi\...` were excluded as these are standard, non-malicious registry paths for Delphi-compiled applications.)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **None identified.** (The analysis confirms that while the application uses techniques like `GetProcAddress` and `ClientToScreen`, these are standard system calls for GUI-based applications.)

---
**Analyst Note:** No actionable indicators of compromise were found in the provided data. The technical complexity observed is attributed to the software's architecture rather than malicious intent.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Non-malicious / Potential Game Tool (No evidence of malicious intent)
3. **Confidence**: High

4. **Key evidence**:
* **Lack of Malicious Indicators:** The analysis found no hardcoded C2 infrastructure, IP addresses, domain names, or suspicious registry keys/mutexes typically associated with malware families like Emotet or Cobalt Strike.
* **Architectural Complexity vs. Obfuscation:** The "mega-switch" structures and extensive `GetProcAddress` blocks are identified as standard artifacts of the Delphi/Pascal compiler for large applications rather than intentional evasion techniques used to hide malicious logic.
* **Functional Context:** The presence of `ClientToScreen`, `OffsetRect`, and complex string handling suggests a legitimate graphical interface or game engine environment, which is common in "overlay" tools but does not inherently indicate malicious capabilities like data theft or unauthorized access.
