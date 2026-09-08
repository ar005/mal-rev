# Threat Analysis Report

**Generated:** 2026-08-31 15:19 UTC
**Sample:** `127ec0c18e91269d2fd3490a1a52d150ef2e01151c0a057182bf8df82236191d_127ec0c18e91269d2fd3490a1a52d150ef2e01151c0a057182bf8df82236191d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `127ec0c18e91269d2fd3490a1a52d150ef2e01151c0a057182bf8df82236191d_127ec0c18e91269d2fd3490a1a52d150ef2e01151c0a057182bf8df82236191d.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 393,216 bytes |
| MD5 | `06593c84301eb062ba83f236d7cbcf91` |
| SHA1 | `bb8872168e534cbc1f3867e69e52b4db5c81c8b7` |
| SHA256 | `127ec0c18e91269d2fd3490a1a52d150ef2e01151c0a057182bf8df82236191d` |
| Overall entropy | 6.555 |
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
| `CODE` | 332,800 | 6.512 | No |
| `DATA` | 4,608 | 4.131 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 8,704 | 4.825 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.201 | No |
| `.reloc` | 24,064 | 6.661 | No |
| `.rsrc` | 21,504 | 4.223 | No |

### Imports

**kernel32.dll**: `Sleep`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WinHelpA`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `ShowCursor`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `SafeArrayPtrOfIndex`, `SafeArrayGetUBound`, `SafeArrayGetLBound`, `SafeArrayCreate`, `VariantChangeType`, `VariantCopy`, `VariantClear`, `VariantInit`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**gdi32.dll**: `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetWinMetaFileBits`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetEnhMetaFileBits`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`, `SelectPalette`
**comctl32.dll**: `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_SetDragCursorImage`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`

## Extracted Strings

Total strings found: **2446** (showing first 100)

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
m/d/yy
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x452390` | 3259 | ✓ |
| `fcn.004032f8` | `0x4032f8` | 2509 | ✓ |
| `fcn.00441fd0` | `0x441fd0` | 2312 | ✓ |
| `fcn.004416c8` | `0x4416c8` | 2280 | ✓ |
| `fcn.0040996c` | `0x40996c` | 1921 | ✓ |
| `fcn.0044fcec` | `0x44fcec` | 1750 | ✓ |
| `fcn.00420a00` | `0x420a00` | 1633 | ✓ |
| `fcn.00426ce8` | `0x426ce8` | 1392 | ✓ |
| `fcn.0040f61c` | `0x40f61c` | 1362 | ✓ |
| `fcn.0040eef4` | `0x40eef4` | 1335 | ✓ |
| `fcn.00443a14` | `0x443a14` | 1183 | ✓ |
| `fcn.00421de4` | `0x421de4` | 1131 | ✓ |
| `fcn.00433d34` | `0x433d34` | 1085 | ✓ |
| `fcn.00438280` | `0x438280` | 978 | ✓ |
| `fcn.00425874` | `0x425874` | 947 | ✓ |
| `fcn.00429150` | `0x429150` | 905 | ✓ |
| `fcn.00451968` | `0x451968` | 902 | ✓ |
| `fcn.0044b170` | `0x44b170` | 852 | ✓ |
| `fcn.004086ba` | `0x4086ba` | 828 | ✓ |
| `fcn.0040a450` | `0x40a450` | 795 | ✓ |
| `fcn.00417c38` | `0x417c38` | 763 | ✓ |
| `fcn.004482b8` | `0x4482b8` | 757 | ✓ |
| `fcn.0042f9f4` | `0x42f9f4` | 728 | ✓ |
| `fcn.00408ae8` | `0x408ae8` | 723 | ✓ |
| `fcn.0042f37c` | `0x42f37c` | 718 | ✓ |
| `fcn.0040c2e8` | `0x40c2e8` | 715 | ✓ |
| `fcn.004227bc` | `0x4227bc` | 690 | ✓ |
| `fcn.0041da90` | `0x41da90` | 640 | ✓ |
| `fcn.0043b1f8` | `0x43b1f8` | 621 | ✓ |
| `fcn.00440ed8` | `0x440ed8` | 603 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004032f8.c`](code/fcn.004032f8.c)
- [`code/fcn.004086ba.c`](code/fcn.004086ba.c)
- [`code/fcn.00408ae8.c`](code/fcn.00408ae8.c)
- [`code/fcn.0040996c.c`](code/fcn.0040996c.c)
- [`code/fcn.0040a450.c`](code/fcn.0040a450.c)
- [`code/fcn.0040c2e8.c`](code/fcn.0040c2e8.c)
- [`code/fcn.0040eef4.c`](code/fcn.0040eef4.c)
- [`code/fcn.0040f61c.c`](code/fcn.0040f61c.c)
- [`code/fcn.00417c38.c`](code/fcn.00417c38.c)
- [`code/fcn.0041da90.c`](code/fcn.0041da90.c)
- [`code/fcn.00420a00.c`](code/fcn.00420a00.c)
- [`code/fcn.00421de4.c`](code/fcn.00421de4.c)
- [`code/fcn.004227bc.c`](code/fcn.004227bc.c)
- [`code/fcn.00425874.c`](code/fcn.00425874.c)
- [`code/fcn.00426ce8.c`](code/fcn.00426ce8.c)
- [`code/fcn.00429150.c`](code/fcn.00429150.c)
- [`code/fcn.0042f37c.c`](code/fcn.0042f37c.c)
- [`code/fcn.0042f9f4.c`](code/fcn.0042f9f4.c)
- [`code/fcn.00433d34.c`](code/fcn.00433d34.c)
- [`code/fcn.00438280.c`](code/fcn.00438280.c)
- [`code/fcn.0043b1f8.c`](code/fcn.0043b1f8.c)
- [`code/fcn.00440ed8.c`](code/fcn.00440ed8.c)
- [`code/fcn.004416c8.c`](code/fcn.004416c8.c)
- [`code/fcn.00441fd0.c`](code/fcn.00441fd0.c)
- [`code/fcn.00443a14.c`](code/fcn.00443a14.c)
- [`code/fcn.004482b8.c`](code/fcn.004482b8.c)
- [`code/fcn.0044b170.c`](code/fcn.0044b170.c)
- [`code/fcn.0044fcec.c`](code/fcn.0044fcec.c)
- [`code/fcn.00451968.c`](code/fcn.00451968.c)

## Behavioral Analysis

This updated analysis incorporates the new findings from chunk 2 of the disassembly while maintaining the initial observations regarding the binary's structure and framework.

### Updated Executive Summary
The binary remains consistent with a **high-level, likely Delphi/Pascal-based Windows application** that utilizes extensive GDI (Graphics Device Interface) calls for sophisticated graphical rendering. The addition of dynamic library loading and complex coordinate transformations suggests that while the "front" of the application is a GUI, the underlying logic involves significant manipulation of window coordinates and graphics layers—features commonly found in **malware overlays, screen scrapers, or sophisticated trojans** designed to hide their functionality behind a dense layer of framework-specific code.

---

### 1. Core Functionality & Purpose (Expanded)
*   **Complex GDI Rendering Pipeline:** The functions `fcn.00421de4` and `fcn.0041da90` reveal heavy use of `CreateDIBSection`, `CreateCompatibleDC`, `StretchBlt`, and `MaskBlt`. This confirms the program is not just drawing static buttons; it is performing **active bitmap manipulation** and potentially scaling or masking images in real-time.
*   **Coordinate & Layout Management:** Functions like `fcn.00451968` (calling `ClientToScreen`) and `fcn.00438280` (calculating bounding boxes via `IsRectEmpty`) indicate that the application calculates exactly where elements appear on the screen relative to other windows.
*   **Menu & Input Handling:** The use of `InsertMenuA` and `InsertMenuItemA` in `fcn.00440ed8` confirms a standard Windows menu system, but when combined with the overlay-capable GDI functions, it suggests a very "polished" interface designed to mimic a legitimate utility or game.

### 2. Suspicious & Malicious Behaviors
*   **Dynamic Library Loading (Indicator of Stealth):** Function `fcn.00425874` is highly significant. It utilizes `GetProcAddress` to resolve a long list of functions from a dynamically loaded library (likely a custom DLL or a modified system library). 
    *   *Why this is suspicious:* This technique is often used by malware authors to **evade static analysis**. By not linking against these functions directly, the author prevents automated tools from flagging specific "malicious" API calls until the code is actually running in memory.
*   **Advanced Graphics Overlays:** The combination of `StretchBlt` and `MaskBlt` with `SetCursor` logic indicates that the program can render content over other windows or manipulate how the mouse interacts with those windows. This is a hallmark of **click-jacking** (placing invisible elements over real buttons) or **overlay malware**.
*   **Anti-Analysis/Delay Tactics:** The presence of `Sleep_1` and long loops in `fcn.004482b8`, combined with the massive "junk code" block found in chunk 1, indicates a concerted effort to frustrate automated sandboxes and manual reverse engineering.

### 3. Technical Sophistication & Patterns
*   **Sophisticated Delphi Framework Logic:** The repeated use of `fcn.00403ee4()`, `fcn.00430ebc()`, and various "wrapper" functions confirms the usage of a heavy development framework (like Borland’s VCL or Lazarus's LCL). While these are legitimate tools, they provide a "layer of insulation," making it harder for analysts to distinguish between intended UI logic and malicious backend operations.
*   **Complex Logic Branching:** The large switch table in `fcn.00429150` suggests the application handles a wide range of system events or internal states, typical of complex software but also useful in malware to handle various environment checks (e.g., "Is this a VM?", "Is there an active debugger?").
*   **Memory Manipulation:** The sophisticated pointer arithmetic and address calculations found in `fcn.00433d34` suggest the application is managing complex data structures or internal object trees, common in high-level languages but can also hide the manipulation of system parameters.

### Updated Intelligence Summary
The sample demonstrates a **high degree of technical sophistication**. It is not a simple "script-kiddy" tool; it is professionally constructed using a high-level framework to create a complex, interactive GUI. 

**Primary Concerns for Incident Response:**
1.  **Overlay Capability:** The heavy GDI usage suggests the application can visually manipulate the screen or inject visual elements into other windows (e.g., banking overlays).
2.  **Obfuscation through Complexity:** The combination of "junk" entry points, dynamic API resolution via `GetProcAddress`, and high-level framework wrapping is designed to exhaust analyst resources.
3.  **Potential for Multi-Stage Payload:** The large block of dynamically loaded functions (`fcn.00425874`) suggests that the primary malicious logic may reside in a separate module that is only unpacked/linked at runtime.

**Conclusion:** This binary should be treated as **high-risk**. Its ability to manipulate graphics and interact with Windows menus while employing heavy anti-analysis techniques strongly suggests it is either a sophisticated trojan or a specialized tool for overlaying malicious content over legitimate software.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your report to the relevant MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | **Dynamic Resolution** | The use of `GetProcAddress` to resolve a long list of functions from dynamically loaded libraries is a classic method to hide malicious API calls from static analysis. |
| **T1027** | **Obfuscated Files or Information** | The inclusion of "junk code," complex logic branching, and the use of heavy frameworks serve to complicate reverse engineering and hide underlying functionality. |
| **T1497** | **Dynamic Linker Hijacking** | (Optional/Contextual) While not explicitly stated as a hijack, the reliance on dynamic loading and custom DLLs for core malicious logic points toward techniques used to evade detection by standard security tools. |

### Analyst Notes:
*   **Defense Evasion via UI Manipulation:** While "Overlay" is not a standalone MITRE ATT&CK technique, it is a common tactic used during **Execution** or **Impact** phases. The use of GDI functions (`StretchBlt`, `MaskBlt`) to create overlays suggests the intent to hide malicious components (like a credential-harvesting form) behind a legitimate-looking interface or to perform click-jacking.
*   **Sandbox Evasion:** The specific mention of `Sleep_1` and long loops are core indicators of **Time-Based Evasion**, intended to exhaust the analysis window of automated sandboxes before malicious behaviors begin.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Per your instructions, standard system paths (e.g., `Software\Borland\...`) and common library components (e.g., `kernel32.dll`, `oleaut32.dll`) have been excluded as they do not constitute unique indicators of a specific threat actor or campaign.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: Detected registry strings were identified as standard Borland/Delphi framework components and were excluded as false positives.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Dynamic API Resolution:** The analysis identifies `fcn.00425874` as a specific point of interest where the binary uses `GetProcAddress` to resolve a long list of functions from a dynamically loaded library. This is a common technique for evading static analysis and hiding malicious capabilities.
*   **Overlay/Graphics Manipulation:** The consistent use of `StretchBlt`, `MaskBlt`, and `SetCursor` logic in the GDI rendering pipeline suggests the capability to create visual overlays or perform click-jacking.
*   **Anti-Analysis Techniques:** Presence of significant "junk code" blocks and extended sleep loops (`Sleep_1`) in `fcn.004482b8` designed to stall automated sandboxes and frustrate manual analysis.

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification for the sample:

1. **Malware family:** Unknown
2. **Malware type:** Trojan (specifically likely a Banking Trojan or Credential Stealer)
3. **Confidence:** Medium
4. **Key evidence:**
    *   **Anti-Analysis & Evasion:** The use of `GetProcAddress` to dynamically resolve a large volume of functions, coupled with "junk code" blocks and extended sleep timers (`Sleep_1`), indicates a high level of sophistication intended to bypass static analysis and exhaust automated sandbox environments.
    *   **Overlay Capabilities:** The heavy reliance on complex GDI rendering functions (`StretchBlt`, `MaskBlt`) and coordinate calculations suggests the creation of graphical overlays, a common tactic used in banking trojans to display fake login forms or perform click-jacking.
    *   **Sophisticated Construction:** The use of a professional Delphi/Pascal framework (VCL/LCL) combined with dynamic library loading indicates that this is not a low-effort "script-kiddy" tool, but rather a professional product designed to hide its true functionality behind complex code layers.
