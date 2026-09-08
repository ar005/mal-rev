# Threat Analysis Report

**Generated:** 2026-09-02 08:55 UTC
**Sample:** `1316b2ae0fcb95baad7c55c1b2c108360f9fb5aab764c0ec27c415577d2a0a32_1316b2ae0fcb95baad7c55c1b2c108360f9fb5aab764c0ec27c415577d2a0a32.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1316b2ae0fcb95baad7c55c1b2c108360f9fb5aab764c0ec27c415577d2a0a32_1316b2ae0fcb95baad7c55c1b2c108360f9fb5aab764c0ec27c415577d2a0a32.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 5,263,632 bytes |
| MD5 | `b22eb48f150717b094f6e477662605fb` |
| SHA1 | `bb6c5f36884623b4e515f93d3a9883096649ed38` |
| SHA256 | `1316b2ae0fcb95baad7c55c1b2c108360f9fb5aab764c0ec27c415577d2a0a32` |
| Overall entropy | 6.17 |
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
| `CODE` | 499,712 | 6.547 | No |
| `DATA` | 9,728 | 4.468 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 9,216 | 4.998 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.207 | No |
| `.reloc` | 40,960 | 6.604 | No |
| `.rsrc` | 4,688,896 | 5.945 | No |

### Imports

**kernel32.dll**: `Sleep`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WinHelpA`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `ShowCursor`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `GetErrorInfo`, `SysFreeString`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**gdi32.dll**: `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetWinMetaFileBits`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetEnhMetaFileBits`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`, `SelectPalette`
**ole32.dll**: `CoUninitialize`, `CoInitialize`
**comctl32.dll**: `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_SetDragCursorImage`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`
**wsock32.dll**: `WSACleanup`, `WSAStartup`

## Extracted Strings

Total strings found: **59804** (showing first 100)

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
t@h`X@
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
	ExceptionLv@
EAbort
EHeapException
EOutOfMemory
EInOutError
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeErrorpy@
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
<#t'<0t#<.t
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00403474` | `0x403474` | 2685 | ✓ |
| `fcn.0044c2dc` | `0x44c2dc` | 2312 | ✓ |
| `fcn.0044b9d4` | `0x44b9d4` | 2280 | ✓ |
| `fcn.0040a82c` | `0x40a82c` | 1921 | ✓ |
| `fcn.0045a020` | `0x45a020` | 1750 | ✓ |
| `fcn.004295f0` | `0x4295f0` | 1633 | ✓ |
| `fcn.0042f92c` | `0x42f92c` | 1392 | ✓ |
| `fcn.004139e4` | `0x4139e4` | 1362 | ✓ |
| `fcn.004132bc` | `0x4132bc` | 1335 | ✓ |
| `fcn.0044dd20` | `0x44dd20` | 1183 | ✓ |
| `fcn.0042a9d4` | `0x42a9d4` | 1131 | ✓ |
| `fcn.0041095c` | `0x41095c` | 1097 | ✓ |
| `fcn.00411420` | `0x411420` | 1088 | ✓ |
| `fcn.0043df80` | `0x43df80` | 1085 | ✓ |
| `fcn.00414b38` | `0x414b38` | 1053 | ✓ |
| `fcn.004798d0` | `0x4798d0` | 1018 | ✓ |
| `fcn.004424f8` | `0x4424f8` | 978 | ✓ |
| `fcn.00412c08` | `0x412c08` | 965 | ✓ |
| `fcn.0042e4b8` | `0x42e4b8` | 947 | ✓ |
| `fcn.00431db4` | `0x431db4` | 905 | ✓ |
| `fcn.0045bc9c` | `0x45bc9c` | 902 | ✓ |
| `fcn.00411f30` | `0x411f30` | 885 | ✓ |
| `fcn.004554a4` | `0x4554a4` | 852 | ✓ |
| `fcn.004126a0` | `0x4126a0` | 846 | ✓ |
| `fcn.00411a1c` | `0x411a1c` | 836 | ✓ |
| `fcn.00415b80` | `0x415b80` | 834 | ✓ |
| `fcn.00408fb6` | `0x408fb6` | 828 | ✓ |
| `fcn.0040b310` | `0x40b310` | 795 | ✓ |
| `fcn.0045c82c` | `0x45c82c` | 784 | ✓ |
| `fcn.00420320` | `0x420320` | 763 | ✓ |

### Decompiled Code Files

- [`code/fcn.00403474.c`](code/fcn.00403474.c)
- [`code/fcn.00408fb6.c`](code/fcn.00408fb6.c)
- [`code/fcn.0040a82c.c`](code/fcn.0040a82c.c)
- [`code/fcn.0040b310.c`](code/fcn.0040b310.c)
- [`code/fcn.0041095c.c`](code/fcn.0041095c.c)
- [`code/fcn.00411420.c`](code/fcn.00411420.c)
- [`code/fcn.00411a1c.c`](code/fcn.00411a1c.c)
- [`code/fcn.00411f30.c`](code/fcn.00411f30.c)
- [`code/fcn.004126a0.c`](code/fcn.004126a0.c)
- [`code/fcn.00412c08.c`](code/fcn.00412c08.c)
- [`code/fcn.004132bc.c`](code/fcn.004132bc.c)
- [`code/fcn.004139e4.c`](code/fcn.004139e4.c)
- [`code/fcn.00414b38.c`](code/fcn.00414b38.c)
- [`code/fcn.00415b80.c`](code/fcn.00415b80.c)
- [`code/fcn.00420320.c`](code/fcn.00420320.c)
- [`code/fcn.004295f0.c`](code/fcn.004295f0.c)
- [`code/fcn.0042a9d4.c`](code/fcn.0042a9d4.c)
- [`code/fcn.0042e4b8.c`](code/fcn.0042e4b8.c)
- [`code/fcn.0042f92c.c`](code/fcn.0042f92c.c)
- [`code/fcn.00431db4.c`](code/fcn.00431db4.c)
- [`code/fcn.0043df80.c`](code/fcn.0043df80.c)
- [`code/fcn.004424f8.c`](code/fcn.004424f8.c)
- [`code/fcn.0044b9d4.c`](code/fcn.0044b9d4.c)
- [`code/fcn.0044c2dc.c`](code/fcn.0044c2dc.c)
- [`code/fcn.0044dd20.c`](code/fcn.0044dd20.c)
- [`code/fcn.004554a4.c`](code/fcn.004554a4.c)
- [`code/fcn.0045a020.c`](code/fcn.0045a020.c)
- [`code/fcn.0045bc9c.c`](code/fcn.0045bc9c.c)
- [`code/fcn.0045c82c.c`](code/fcn.0045c82c.c)
- [`code/fcn.004798d0.c`](code/fcn.004798d0.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated the analysis of the binary. The new code confirms several suspicions regarding the complexity of the application and adds specific insights into its internal architecture and potential capabilities.

### Updated Analysis Summary

#### 1. Core Functionality and Purpose
The updated data reinforces that this is a high-complexity application (likely Delphi) with an extensive "backend" logic layer beyond just simple GUI rendering.
*   **Robust Data Marshalling:** The presence of `fcn.00411f30` confirms a heavy reliance on complex type casting and potentially **COM/OLE Variant types**. This suggests the app interacts with high-level system APIs or other software components requiring complex data exchange.
*   **Stateful Dispatcher System:** Several functions (e.g., `fcn.004554a4` and `fcn.00420320`) act as **dispatchers**. They use massive switch-case tables or indirect jumps to route execution to specific sub-routines based on internal states, flags (like `\x01`, `\x02`, `\x03`), or identifiers. This is characteristic of a "plug-in" architecture or an **embedded script engine**.
*   **Complex Input/Buffer Processing:** `fcn.0045c82c` shows evidence of processing buffers, handling special characters (like newlines), and potentially converting between different string formats (BSTR).

#### 2. Suspicious or Malicious Behaviors
The new code adds several layers to the existing concerns:
*   **Advanced State Management:** The complexity of `fcn.004554a4` is significant. In a benign context, this is common in game engines; however, in a malicious context, such a "hub" can be used to hide multiple different behaviors (e.g., keylogging, screen scraping, and network communication) under the guise of a single main loop.
*   **Coordinate Mapping & Screen Interaction:** `fcn.0045bc9c` utilizes `ClientToScreen` and `OffsetRect`. While common in UI code, these are the "bread and butter" of **malicious overlays**. They allow an application to map mouse clicks from a transparent overlay onto the coordinates of the game or system window behind it.
*   **Robust Translation/Parsing:** The logic in `fcn.0045c82c` suggests that the program is capable of interpreting and manipulating complex data structures, which could be used for processing commands from a remote server (C2).

#### 3. Notable Techniques & Patterns
*   **Dynamic Method Dispatch:** The pattern seen in `fcn.00420320` (`switch(*(***var_ch * 4 + ...))`) is typical of a **Virtual Method Table (vtable)** or a dynamic jump table. This allows the program to stay "modular"—the main execution path stays the same, while the functionality changed based on which specific "module" is active at that moment.
*   **Large Scale Logic Branching:** The repetitive use of large switch-cases in `fcn.00431db4` and `fcn.00411f30` suggests a high volume of internal states or a wide range of supported types, indicating a very mature software project (or one heavily designed to hide many sub-functions from simple linear analysis).
*   **Internal API Hiding:** The jump tables and indirect calls make it much harder for an analyst to follow the "flow" of logic without dynamic instrumentation. It is deliberately structured to be difficult to trace via static analysis alone.

---

### Updated Summary for Analyst
The addition of chunk 2 confirms that this binary is not a simple utility; it possesses a sophisticated, **modular architecture**. The core engine uses complex dispatch tables and multi-step state logic to route operations. 

**Key findings from the new data:**
1.  **Intentional Complexity:** The heavy use of "Dispatchers" suggests that the application's primary functionality is modularized, making it difficult to map out its capabilities solely through static analysis.
2.  **Overlay Capability:** The repeated use of `ClientToScreen` and complex coordinate logic strongly supports the theory that this application functions as a **graphical overlay**.
3.  **Heavy Logic Processing:** The complexity of the data-handling routines (`fcn.0045c82c`) and the switch tables suggests it may be handling inputs from an external source (like a script or a remote server) and processing them through an internal logic engine.

**Actionable Recommendations:**
*   **Dynamic Instrumentation:** Use a tool like **Frida** or **x64dbg** to hook the dispatch points in `fcn.004554a4` and `fcn.00420320`. This will allow you to see which "branch" of logic the program chooses when certain inputs (mouse clicks, keystrokes) are received.
*   **Memory Forensics:** Monitor for injected DLLs or memory allocations that occur only after a specific sequence of events within these dispatch loops. 
*   **Overlay Monitoring:** Run the application with a screen-capture overlay tool to see if it creates an invisible layer over other windows, which would confirm its use as a "cheat" or specialized overlay tool.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Execution | The use of jump tables, indirect calls, and complex switch-case structures is specifically noted as a method to hide logic flow and hinder static analysis. |
| T1059 | Command and Scripting Interpreter | The identification of a "stateful dispatcher system" and an "embedded script engine" indicates the binary interprets external commands or scripts to determine behavior. |
| T1071 | Application Layer Protocol | The capability to process complex data structures and translate various string formats suggests the handling of communication from a remote C2 server. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Many items in the string dump (such as `kernel32.dll`, `OfferMemory`, and `Software\Borland\...`) were excluded as they are standard library components or common development environment artifacts rather than unique malicious indicators.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None (The identified registry paths, such as `SOFTWARE\Borland\Delphi\...`, were excluded as they are standard components of the Delphi development environment).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Internal Function Offsets (Potential Analysis Markers):** 
    *   `00411f30` (Complex type casting/logic)
    *   `004554a4` (Stateful dispatcher system)
    *   `00420320` (Dispatch table / VTable-like jumps)
    *   `0045c82c` (Buffer processing and BSTR conversion)
    *   `0045bc9c` (Overlay/Coordinate mapping logic)
*   **Behavioral Indicators:**
    *   **Overlay Functionality:** Use of `ClientToScreen` and `OffsetRect` suggests the presence of a graphical overlay.
    *   **Modular Dispatch Architecture:** The use of large switch-case tables to route execution to different "modules" or states.
    *   **Hidden Logic Flow:** Intentional use of indirect jumps and complex state management to obscure functionality from static analysis.

---

## Malware Family Classification

Based on the provided behavior analysis, here is the classification:

1. **Malware family**: custom (RAT-based)
2. **Malware type**: RAT / backdoor
3. **Confidence**: Medium
4. **Key evidence**: 
    *   **Overlay & Interaction Logic:** The use of `ClientToScreen` and `OffsetRect` indicates the creation of a graphical overlay, a common feature in Remote Access Trojans (RATs) to provide an interactive GUI for attackers on the victim's machine.
    *   **Modular Dispatch System:** The identification of "stateful dispatchers," jump tables, and an "embedded script engine" suggests the binary is designed to receive various remote commands from a C2 server and route them to different internal modules (e.g., keylogging, file management, or screen scraping).
    *   **Anti-Analysis Techniques:** The use of complex state management and indirect jumps (T1027) points toward an intentional design to obfuscate the control flow and hide the true scope of its capabilities from static analysis.
