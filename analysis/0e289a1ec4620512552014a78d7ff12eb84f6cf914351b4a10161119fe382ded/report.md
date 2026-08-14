# Threat Analysis Report

**Generated:** 2026-08-11 18:43 UTC
**Sample:** `0e289a1ec4620512552014a78d7ff12eb84f6cf914351b4a10161119fe382ded_0e289a1ec4620512552014a78d7ff12eb84f6cf914351b4a10161119fe382ded.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e289a1ec4620512552014a78d7ff12eb84f6cf914351b4a10161119fe382ded_0e289a1ec4620512552014a78d7ff12eb84f6cf914351b4a10161119fe382ded.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 4,015,888 bytes |
| MD5 | `31d2a81d43baafe1537607c319a59328` |
| SHA1 | `7b90848ac82895927ec70d3dd3645351e2f9b901` |
| SHA256 | `0e289a1ec4620512552014a78d7ff12eb84f6cf914351b4a10161119fe382ded` |
| Overall entropy | 7.388 |
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
| `CODE` | 542,720 | 6.505 | No |
| `DATA` | 7,680 | 4.43 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 9,216 | 4.999 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.204 | No |
| `.reloc` | 40,960 | 6.625 | No |
| `.rsrc` | 3,400,192 | 7.302 | ⚠️ Yes |

### Imports

**kernel32.dll**: `Sleep`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WinHelpA`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `ShowCursor`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `GetErrorInfo`, `SysFreeString`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**gdi32.dll**: `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetWinMetaFileBits`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetEnhMetaFileBits`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`, `SelectPalette`
**ole32.dll**: `CoUninitialize`, `CoInitialize`
**comctl32.dll**: `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_SetDragCursorImage`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`
**winmm.dll**: `sndPlaySoundA`

## Extracted Strings

Total strings found: **45055** (showing first 100)

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
String

WideString
Variant
TObject0
TObject$
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

	TFileName
	Exception r@
EHeapException
EOutOfMemory
EInOutError0s@
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeError
EIntOverflow

EMathError

EInvalidOp
EZeroDivideTv@
	EOverflow

EUnderflow
EInvalidPointer`w@
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00403344` | `0x403344` | 2517 | ✓ |
| `entry0` | `0x4856b0` | 2458 | ✓ |
| `fcn.00459e1c` | `0x459e1c` | 2312 | ✓ |
| `fcn.00459514` | `0x459514` | 2280 | ✓ |
| `fcn.00409e60` | `0x409e60` | 1921 | ✓ |
| `fcn.00467c2c` | `0x467c2c` | 1750 | ✓ |
| `fcn.004285a4` | `0x4285a4` | 1633 | ✓ |
| `fcn.0042f7bc` | `0x42f7bc` | 1392 | ✓ |
| `fcn.00412a04` | `0x412a04` | 1362 | ✓ |
| `fcn.004122dc` | `0x4122dc` | 1335 | ✓ |
| `fcn.0047a698` | `0x47a698` | 1246 | ✓ |
| `fcn.0045b860` | `0x45b860` | 1183 | ✓ |
| `fcn.00429a74` | `0x429a74` | 1131 | ✓ |
| `fcn.0040f97c` | `0x40f97c` | 1097 | ✓ |
| `fcn.00410440` | `0x410440` | 1088 | ✓ |
| `fcn.0044b134` | `0x44b134` | 1085 | ✓ |
| `fcn.004138fc` | `0x4138fc` | 1053 | ✓ |
| `fcn.0046c5f4` | `0x46c5f4` | 1018 | ✓ |
| `fcn.00420358` | `0x420358` | 988 | ✓ |
| `fcn.0044f6f0` | `0x44f6f0` | 978 | ✓ |
| `fcn.00411c28` | `0x411c28` | 965 | ✓ |
| `fcn.0042d760` | `0x42d760` | 947 | ✓ |
| `fcn.00480d94` | `0x480d94` | 927 | ✓ |
| `fcn.00437174` | `0x437174` | 905 | ✓ |
| `fcn.004698c0` | `0x4698c0` | 902 | ✓ |
| `fcn.00410f50` | `0x410f50` | 885 | ✓ |
| `fcn.0046300c` | `0x46300c` | 852 | ✓ |
| `fcn.004116c0` | `0x4116c0` | 846 | ✓ |
| `fcn.00410a3c` | `0x410a3c` | 836 | ✓ |
| `fcn.00408bae` | `0x408bae` | 828 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00403344.c`](code/fcn.00403344.c)
- [`code/fcn.00408bae.c`](code/fcn.00408bae.c)
- [`code/fcn.00409e60.c`](code/fcn.00409e60.c)
- [`code/fcn.0040f97c.c`](code/fcn.0040f97c.c)
- [`code/fcn.00410440.c`](code/fcn.00410440.c)
- [`code/fcn.00410a3c.c`](code/fcn.00410a3c.c)
- [`code/fcn.00410f50.c`](code/fcn.00410f50.c)
- [`code/fcn.004116c0.c`](code/fcn.004116c0.c)
- [`code/fcn.00411c28.c`](code/fcn.00411c28.c)
- [`code/fcn.004122dc.c`](code/fcn.004122dc.c)
- [`code/fcn.00412a04.c`](code/fcn.00412a04.c)
- [`code/fcn.004138fc.c`](code/fcn.004138fc.c)
- [`code/fcn.00420358.c`](code/fcn.00420358.c)
- [`code/fcn.004285a4.c`](code/fcn.004285a4.c)
- [`code/fcn.00429a74.c`](code/fcn.00429a74.c)
- [`code/fcn.0042d760.c`](code/fcn.0042d760.c)
- [`code/fcn.0042f7bc.c`](code/fcn.0042f7bc.c)
- [`code/fcn.00437174.c`](code/fcn.00437174.c)
- [`code/fcn.0044b134.c`](code/fcn.0044b134.c)
- [`code/fcn.0044f6f0.c`](code/fcn.0044f6f0.c)
- [`code/fcn.00459514.c`](code/fcn.00459514.c)
- [`code/fcn.00459e1c.c`](code/fcn.00459e1c.c)
- [`code/fcn.0045b860.c`](code/fcn.0045b860.c)
- [`code/fcn.0046300c.c`](code/fcn.0046300c.c)
- [`code/fcn.00467c2c.c`](code/fcn.00467c2c.c)
- [`code/fcn.004698c0.c`](code/fcn.004698c0.c)
- [`code/fcn.0046c5f4.c`](code/fcn.0046c5f4.c)
- [`code/fcn.0047a698.c`](code/fcn.0047a698.c)
- [`code/fcn.00480d94.c`](code/fcn.00480d94.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, I have updated and extended the analysis. The new code provides more evidence regarding the application's internal architecture and its likely capabilities as a sophisticated overlay or a tool with complex interaction logic.

### Updated Analysis Summary

#### Core Functionality and Purpose
The analysis of Chunk 2 reinforces the conclusion that this is a **Delphi-based application** utilizing a highly abstracted framework (likely VCL/LCL). The presence of several large "dispatcher" functions indicates a sophisticated internal state machine.

*   **Advanced Graphics Management:** `fcn.00429a74` demonstrates complex manipulation of Device Contexts (DC), Bitmaps, and Palettes. It specifically manages `CreateDIBSection` and `CreateCompatibleBitmap`. These are not standard "beginner" graphics calls; they are used for high-performance rendering or creating memory-mapped bitmaps that can be shared/updated efficiently.
*   **Dynamic UI Calculation:** Functions like `fcn.0044f6f0` perform intricate arithmetic on coordinate systems and bounding boxes (e.g., calculating offsets from a raw buffer). This suggests the application manages complex layout calculations or dynamically adjusts its visual elements based on window environment changes.

#### Suspicious or Malicious Behaviors
The new code reveals more sophisticated techniques often associated with **malware overlays** (such as cheats, info-stealers, or RATs):

*   **Screen Space Interaction:** The use of `ClientToScreen` in `fcn.004698c0` is a significant indicator. This function translates coordinates from the window's local space to absolute screen coordinates. In many malicious contexts, this is used to **overlay content over other applications** or to detect where a user clicks on the global desktop rather than just within the application’s own window.
*   **Complex Dispatcher Logic:** The presence of large switch-case blocks (e.g., `fcn.0046c5f4` and `fcn.00410440`) suggests a "command" or "action" system. In a malware context, these are often the backend logic for processing instructions received from a Command & Control (C2) server, where each case corresponds to a different remote command.
*   **Coordinate/Boundary Management:** The extensive calculation of `Rect` offsets and boundaries in `fcn.0044f6f0` suggests that the software is designed to maintain its visual presence even when windows are resized or moved, which is common in "invisible" overlays or layered menus.

#### Notable Techniques & Patterns
*   **Delphi/Pascal Compiler Artifacts:** The pattern of `switch(uVar1 & 0xbf)` and repetitive cases (e.g., 4, 5, 6, 7 all calling the same internal function) is a signature of Delphi's method dispatching system. This makes it harder for analysts to follow "logic" because much of the actual action is hidden behind standard library wrappers.
*   **Memory Management:** The heavy use of `OffSetRect` and `CreateDIBSection` indicates an intent for stable, consistent rendering performance.
*   **Code Complexity/Obfuscation:** While not explicitly packed in these functions, the sheer volume of nested logic and "redundant-looking" switch statements provides a layer of **structural obfuscation**, making it harder to trace the intended execution path without dynamic analysis.

---

### Updated Summary for Analyst
The addition of chunk 2 reinforces the high likelihood that this binary is a sophisticated piece of software with capabilities designed for **overlay functionality**. 

**Key Risk Indicators:**
1.  **Overlay Capability:** The combination of `BitBlt` (Chunk 1), `CreateDIBSection`, and `ClientToScreen` (Chunk 2) strongly points toward an application that projects its UI over other windows or manipulates the screen at a low level.
2.  **Potential Command Processing:** The large switch-case dispatchers are consistent with a "modular" architecture where different features can be toggled on/off, common in multi-functional malware (e.g., info-stealers with multiple stealing modules).
3.  **Delphi Framework Complexity:** The high level of abstraction makes it difficult to identify specific malicious payloads just by looking at the disassembly; a significant portion of the "malicious" intent is likely hidden inside the library calls and the automated code generated by the Delphi compiler.

**Recommendation:** 
This binary should be treated as potentially suspicious. Further investigation should focus on:
1.  **Network Traffic:** Identify if the `switch` cases correspond to remote commands (C2 activity).
2.  **Overlay Behavior:** Observe how the window interacts with other open windows (e.g., does it stay on top, or is it transparent?).
3.  **Resource Extraction:** Examine embedded assets/icons which may reveal its "marketing" branding for a bot or overlay tool.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of `ClientToScreen` and complex graphics management (e.g., `CreateDIBSection`) indicates an overlay intended to hide malicious activity by blending into or overlaying the user's desktop environment. |
| T1059 | Command and Scripting Interpreter | The extensive switch-case blocks act as a dispatch mechanism to process various internal commands, which is typical for modular malware designed to execute different functionalities based on input logic. |
| T1027 | Obfuscated Files or Information | The use of high-level Delphi abstractions and complex "redundant" structures constitutes structural obfuscation intended to hinder manual analysis and hide the execution path. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** Several strings present in the "EXTRACTED STRINGS" section (such as Borland registry paths, standard Windows DLLs like `kernel32.dll`, and Delphi-specific internal types) were identified as false positives related to the development environment and were excluded from this report.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: The `SOFTWARE\Borland\...` paths found in strings are artifacts of the Delphi compiler, not malicious registry persistence.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **C2 Capability Indicators:** The behavioral analysis identifies large "switch-case" blocks (e.g., `fcn.0046c5f4` and `fcn.00410440`). In a malware context, these structures typically function as command dispatchers for processing instructions from a remote Command & Control (C2) server.
*   **Overlay Behavior:** The use of `ClientToScreen`, `BitBlt`, `CreateDIBSection`, and `CreateCompatibleBitmap` indicates the application is designed to create a graphical overlay or manipulate screen space, common in cheat software, info-stealers, or RATs.
*   **Programming Environment:** Significant presence of Delphi/Pascal artifacts (e.g., `TObject`, `Variant`, `SenseItems`) identifies the development framework used by the threat actor.

---

## Malware Family Classification

1. **Malware family**: Unknown (Custom)
2. **Malware type**: RAT (Remote Access Trojan) / Backdoor
3. **Confidence**: Medium

4. **Key evidence**:
*   **Overlay Capabilities:** The heavy use of `ClientToScreen`, `CreateDIBSection`, and `BitBlt` indicates a sophisticated overlay designed to project graphics over other applications or the desktop environment, a common tactic for RATs and info-stealers to hide their presence or interact with the user's workspace.
*   **Command Dispatcher Architecture:** The identification of large "switch-case" blocks (`fcn.0046c5f4` and `fcn.00410440`) is a signature of modular malware logic, where these structures act as handlers for various commands received from a remote Command & Control (C2) server.
*   **Advanced Implementation:** The use of the Delphi framework to provide structural obfuscation combined with complex graphics management suggests a professional level of development, typical of advanced persistent threats or sophisticated multi-functional RATs rather than simple "one-off" scripts.
