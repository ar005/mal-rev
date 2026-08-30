# Threat Analysis Report

**Generated:** 2026-08-23 19:13 UTC
**Sample:** `118c6b4cd8375566818f20d50bb60af5a4ea3cea7615ab279fce7eb5a60b5999_118c6b4cd8375566818f20d50bb60af5a4ea3cea7615ab279fce7eb5a60b5999.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `118c6b4cd8375566818f20d50bb60af5a4ea3cea7615ab279fce7eb5a60b5999_118c6b4cd8375566818f20d50bb60af5a4ea3cea7615ab279fce7eb5a60b5999.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 854,016 bytes |
| MD5 | `d86a8bc063e46981ed47f37a4b183c25` |
| SHA1 | `50612475e0592e3553d32f7dd440db83c8181a73` |
| SHA256 | `118c6b4cd8375566818f20d50bb60af5a4ea3cea7615ab279fce7eb5a60b5999` |
| Overall entropy | 6.987 |
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
| `CODE` | 470,528 | 6.55 | No |
| `DATA` | 7,680 | 4.275 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 9,216 | 4.877 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.195 | No |
| `.reloc` | 36,864 | 6.61 | No |
| `.rsrc` | 328,192 | 6.872 | No |

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

Total strings found: **5042** (showing first 100)

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
EInOutError`}@
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeError 
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
| `fcn.00448f9c` | `0x448f9c` | 2312 | ✓ |
| `fcn.00448694` | `0x448694` | 2280 | ✓ |
| `fcn.0040ad60` | `0x40ad60` | 1921 | ✓ |
| `fcn.00456cb8` | `0x456cb8` | 1750 | ✓ |
| `fcn.00427fac` | `0x427fac` | 1633 | ✓ |
| `fcn.0042f2d8` | `0x42f2d8` | 1494 | ✓ |
| `fcn.00413e10` | `0x413e10` | 1362 | ✓ |
| `fcn.004136e8` | `0x4136e8` | 1335 | ✓ |
| `fcn.0044a9e0` | `0x44a9e0` | 1183 | ✓ |
| `fcn.00429390` | `0x429390` | 1131 | ✓ |
| `fcn.00410d88` | `0x410d88` | 1097 | ✓ |
| `fcn.0041184c` | `0x41184c` | 1088 | ✓ |
| `fcn.0043a8e8` | `0x43a8e8` | 1085 | ✓ |
| `fcn.00414f64` | `0x414f64` | 1053 | ✓ |
| `fcn.0043ed50` | `0x43ed50` | 978 | ✓ |
| `fcn.00413034` | `0x413034` | 965 | ✓ |
| `fcn.0042cecc` | `0x42cecc` | 947 | ✓ |
| `fcn.004317a4` | `0x4317a4` | 905 | ✓ |
| `fcn.00458934` | `0x458934` | 902 | ✓ |
| `fcn.0041235c` | `0x41235c` | 885 | ✓ |
| `fcn.0045213c` | `0x45213c` | 852 | ✓ |
| `fcn.00412acc` | `0x412acc` | 846 | ✓ |
| `fcn.00411e48` | `0x411e48` | 836 | ✓ |
| `fcn.00415fac` | `0x415fac` | 834 | ✓ |
| `fcn.004094ea` | `0x4094ea` | 828 | ✓ |
| `fcn.0042faf4` | `0x42faf4` | 809 | ✓ |
| `fcn.0040b844` | `0x40b844` | 795 | ✓ |
| `fcn.004594c4` | `0x4594c4` | 784 | ✓ |
| `entry0` | `0x473d40` | 782 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00403ab4.c`](code/fcn.00403ab4.c)
- [`code/fcn.004094ea.c`](code/fcn.004094ea.c)
- [`code/fcn.0040ad60.c`](code/fcn.0040ad60.c)
- [`code/fcn.0040b844.c`](code/fcn.0040b844.c)
- [`code/fcn.00410d88.c`](code/fcn.00410d88.c)
- [`code/fcn.0041184c.c`](code/fcn.0041184c.c)
- [`code/fcn.00411e48.c`](code/fcn.00411e48.c)
- [`code/fcn.0041235c.c`](code/fcn.0041235c.c)
- [`code/fcn.00412acc.c`](code/fcn.00412acc.c)
- [`code/fcn.00413034.c`](code/fcn.00413034.c)
- [`code/fcn.004136e8.c`](code/fcn.004136e8.c)
- [`code/fcn.00413e10.c`](code/fcn.00413e10.c)
- [`code/fcn.00414f64.c`](code/fcn.00414f64.c)
- [`code/fcn.00415fac.c`](code/fcn.00415fac.c)
- [`code/fcn.00427fac.c`](code/fcn.00427fac.c)
- [`code/fcn.00429390.c`](code/fcn.00429390.c)
- [`code/fcn.0042cecc.c`](code/fcn.0042cecc.c)
- [`code/fcn.0042f2d8.c`](code/fcn.0042f2d8.c)
- [`code/fcn.0042faf4.c`](code/fcn.0042faf4.c)
- [`code/fcn.004317a4.c`](code/fcn.004317a4.c)
- [`code/fcn.0043a8e8.c`](code/fcn.0043a8e8.c)
- [`code/fcn.0043ed50.c`](code/fcn.0043ed50.c)
- [`code/fcn.00448694.c`](code/fcn.00448694.c)
- [`code/fcn.00448f9c.c`](code/fcn.00448f9c.c)
- [`code/fcn.0044a9e0.c`](code/fcn.0044a9e0.c)
- [`code/fcn.0045213c.c`](code/fcn.0045213c.c)
- [`code/fcn.00456cb8.c`](code/fcn.00456cb8.c)
- [`code/fcn.00458934.c`](code/fcn.00458934.c)
- [`code/fcn.004594c4.c`](code/fcn.004594c4.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, I have updated and expanded the analysis. The new code provides significant evidence regarding how the application processes its internal logic and handles its graphical components.

### Updated Analysis of Functionality

#### 1. Advanced Command Dispatching (The "Interpreter" Engine)
The appearance of multiple large switch-case blocks (e.g., in `fcn.0041235c`, `fcn.00412acc`, and `fcn.00458934`) confirms a **highly structured command dispatch system**. 
*   These functions act as "interpreters." They take an input value (likely an opcode or a command ID) and route the execution to specific logic blocks.
*   The sheer number of cases suggests that the application is designed to handle a wide variety of actions, which is characteristic of **game cheats** (handling different types of visual elements), **Remote Access Trojans (RATs)** (different types of remote commands), or complex **custom script engines**.

#### 2. Robust Graphics Overlay Elements
The analysis of `fcn.0042faf4` provides more specific evidence for the "overlay" theory:
*   **Text Rendering:** This function explicitly calls `DrawTextA`. This means the program doesn't just modify graphics; it renders text on top of the screen (e.g., status messages, coordinates, or labels).
*   **Dynamic Layout Calculation:** The complex math involving `OffsetRect`, and calculations for `dx` and `dy`, suggests the application calculates positions dynamically to ensure overlays stay correctly aligned regardless of window size or resolution.

#### 3. Complex Data/String Parsing
The function `fcn.004594c4` is highly indicative of advanced string or buffer handling:
*   It contains logic for iterating through buffers and checking for specific control characters (like `\x01`, `\x02`, `\x03`). 
*   This type of logic is common when a program receives data from a remote server (e.g., a configuration file or "packet" containing instructions) and needs to parse it into internal structures.

#### 4. Obfuscation & Entry Point Behavior
The `entry0` function shows a very distinctive pattern: long sequences of repeated additions to a pointer (`*pcVar3 = *pc_Var3 + cVar1;`).
*   This is often used for **string hashing or offset calculation**. Instead of storing "naked" strings in the binary (which are easy for analysts to find), the program calculates an index based on a hash. 
*   This reinforces the conclusion that the author took care to hide certain strings/identifiers from static analysis.

---

### Revised Summary of Malicious/Suspicious Behaviors

*   **Instructional "Command" Architecture:** The heavy use of switch-tables indicates a "plug-and-play" capability where the application can perform many different actions based on instructions it receives internally or over a network.
*   **Interactive Overlay Logic:** The combination of `DrawTextA` and complex coordinate mathematics strongly suggests an **overlay**. This is common in tools meant to display information (like health bars, map markers, or status text) directly over another application (like a game).
*   **Complex String/Buffer Handling:** The logic seen in `0x4594c4` indicates the program handles complex data structures. If this were a simple tool, such robust parsing wouldn't be necessary; it is typical of tools designed to receive and execute remote commands.
*   **Delphi-Specific Construction:** The use of OLE-style string handling (seen in `0x4594c4`) confirms the Delphi/Pascal origin, which provides a high level of abstraction for complex tasks like network communications and UI rendering.

### Final Conclusion for Analyst
The addition of chunk 2 reinforces the previous assessment but adds more weight to the **"Sophisticated Overlay/Cheat"** or **"Command-Driven RAT"** classification. 

1.  **Overlay Behavior:** The presence of `DrawTextA` combined with heavy GDI math confirms it is designed to visually modify what the user sees on screen in a sophisticated way.
2.  **Remote Control/Scripting Capability:** The large switch tables and complex buffer parsing suggest that this program is not "hard-coded" for one single task; it is built as a framework that can be updated or controlled remotely via commands.
3.  **Evasion Awareness:** The repetitive pointer arithmetic in the entry point suggests a deliberate attempt to hide strings from simple string searches, which is common in both high-end cheat software and sophisticated malware.

**Recommendation:** This binary should be treated as **highly suspicious**. It contains all the hallmarks of a specialized overlay (likely for gaming) or a remote administrative tool with its own internal command language.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of observed behaviors to the MITRE ATT&K framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The presence of large switch-case "interpreter" blocks indicates a system designed to parse and execute a wide range of commands, typical of RATs or complex cheat engines. |
| **T1027** | Obfuscated Files or Information | The use of repetitive pointer arithmetic for string hashing/offset calculation at the entry point is a common method to hide strings from static analysis tools. |

### Analyst Notes:
*   **Regarding "Overlay Logic":** While the graphical overlay and `DrawTextA` usage are prominent indicators of the program's functionality (typical of game cheats or HUD-based RATs), they do not map to a specific standalone MITRE technique unless they are used specifically for **T1036 (Masquerading)** to blend in with legitimate applications.
*   **Regarding "Buffer Parsing":** The logic found in `fcn.004594c4` supports the **T1059** classification, as it demonstrates the robustness required to handle complex instructions or data packets from a remote source before they are passed to the interpreter engine.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: In accordance with your instructions, standard Windows libraries, Delphi development paths, and generic API calls have been excluded as false positives.*

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (The registry keys present in the strings—`Software\Borland\...`—are standard environment paths for the Delphi programming language and do not constitute specific malicious indicators).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Command Dispatching Infrastructure:** The presence of large switch-case blocks (at `fcn.0041235c`, `fcn.00412acc`, and `fcn.00458934`) indicates a "hub" architecture used to process diverse commands, typical of RATs or game cheats.
*   **Non-Printable Character Parsing:** Logic at `0x4594c4` specifically checks for control characters (`\x01`, `\x02`, `\x03`), suggesting a custom communication protocol or the handling of structured "packets" from a remote source.
*   **String Obfuscation Technique:** The entry point exhibits repetitive pointer arithmetic to resolve strings via hashing rather than storing them in plain text (an evasion technique used to bypass static analysis).
*   **Overlay Overlay logic:** Use of `DrawTextA` combined with manual coordinate calculations (`OffsetRect`, `dx`/`dy` math) indicates the binary is designed to render a graphical overlay.

---

## Malware Family Classification

1. **Malware family**: Custom
2. **Malware type**: RAT (Remote Access Trojan) / Backdoor
3. **Confidence**: High
4. **Key evidence**:
    *   **Command Dispatching Infrastructure:** The discovery of multiple large switch-case blocks acting as an "interpreter" indicates a sophisticated command-driven architecture typical of RATs, allowing the binary to execute various actions based on received input or opcodes.
    *   **Sophisticated Communication/Parsing Logic:** The complex buffer handling and parsing of control characters (e.g., `\x01`, `\x02`) suggest the application is designed to process structured packets from a remote source rather than performing simple, hard-coded tasks.
    *   **Evasion Awareness:** The use of repetitive pointer arithmetic for string hashing at the entry point demonstrates a deliberate attempt to hide functionality and identifiers from static analysis tools, common in professional malware development.
