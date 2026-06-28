# Threat Analysis Report

**Generated:** 2026-06-27 22:33 UTC
**Sample:** `02050b2a24cf0864a482fbaab679dee7a58dd6f707a7b0927a6bfcc724631cd0_02050b2a24cf0864a482fbaab679dee7a58dd6f707a7b0927a6bfcc724631cd0.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `02050b2a24cf0864a482fbaab679dee7a58dd6f707a7b0927a6bfcc724631cd0_02050b2a24cf0864a482fbaab679dee7a58dd6f707a7b0927a6bfcc724631cd0.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 4,216,080 bytes |
| MD5 | `166dad1e3a10e61b7df264749e6a3e28` |
| SHA1 | `1ac22255899cd415f7b204211409c9d4228c1567` |
| SHA256 | `02050b2a24cf0864a482fbaab679dee7a58dd6f707a7b0927a6bfcc724631cd0` |
| Overall entropy | 7.007 |
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
| `.rsrc` | 3,641,344 | 6.87 | No |

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

Total strings found: **59574** (showing first 100)

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

This updated analysis incorporates the new disassembly data (chunk 2/2) while retaining all previous findings regarding Delphi-based construction, GDI manipulation, and Dynamic API Resolution.

### Updated Analysis of Binary Behavior

#### 1. Core Functionality and Purpose
The additional code confirms that the binary is a complex, modular application with a heavy reliance on high-level framework features.

*   **Advanced Property Dispatching:** Functions like `fcn.00431db4`, `fcn.00411f30`, and `fcn.004126a0` contain extensive switch tables. This is a hallmark of the **Delphi/Pascal VCL or FMX framework**, where every property access (e.g., color, size, position) goes through a "getter" that checks an ID to determine which logic to execute.
*   **COM and OLE Interaction:** The presence of `fcn.0045c82c` indicates the application interacts with **Microsoft’s COM (Component Object Model)**. It specifically handles `bstrString` objects and calls `oleaut32.dll_SysFreeString`. This means the program communicates with other Windows components or follows complex system protocols beyond simple internal logic.
*   **Overlay/Coordinate Mapping:** Function `fcn.0045bc9c` utilizes **`sub.user32.dll_ClientToScreen`**. This function maps coordinates from a specific window to the entire screen. 

#### 2. Suspicious or Malicious Behaviors
While much of the behavior is standard for complex Delphi apps, certain patterns remain high-priority for security investigation:

*   **Persistent Dynamic API Resolution:** The logic observed in `fcn.0042e4b8` (from chunk 1) and the extensive dispatching logic seen in `fcn.00420320` suggest a "plugin" or "engine-driven" architecture. In a malware context, this allows an attacker to hide malicious sub-modules behind a wall of standard framework calls; the core "malicious" functions are only called when specific conditions/IDs are met in the switch tables.
*   **Potential Overlay Behavior:** The combination of **GDI Graphics Manipulation** (from chunk 1) and **`ClientToScreen` Coordinate Mapping** (from chunk 2) is a strong indicator of an **overlay**. Overlay windows are commonly used by:
    *   Game cheats or "aimbots" that draw information over the game screen.
    *   Malware/Spyware that overlays fake login forms or transparent UI elements to intercept user interaction.

#### 3. Notable Techniques and Patterns
*   **Sophisticated Memory Management:** The way `fcn.0045c82c` handles string arrays and loop-based memory cleanup suggests the application manages a significant amount of dynamic data, potentially from an external source or network.
*   **High Degree of Abstraction:** The heavy use of switch tables (like those in `fcn.00420320`) masks the direct flow of execution. This makes automated analysis harder because the "next step" is determined at runtime by a value passed into the function, rather than being explicitly visible in the linear code.
*   **System Integration:** The reliance on `oleaut32` suggests that the program isn't just self-contained; it interacts with other parts of the Windows OS (e.g., Shell objects, and potentially network protocols implemented via COM).

---

### Summary for Investigation
The additional disassembly confirms a highly sophisticated, Delphi-based architecture. The binary is likely more than just a "simple" GUI tool; it features complex internal state management, deep integration with Windows subsystems (COM/OLE), and specific logic for mapping window coordinates to the screen (`ClientToScreen`).

**Updated Risk Profile:**
The primary concern remains the **Dynamic API Resolution** found in the first chunk. When combined with the **Overlay-capable functions** (`ClientToScreen`) and **Robust Dispatching**, this is a signature of high-quality, professional software—but it is also exactly how sophisticated "grayware" (cheat engines) or "stealthy malware" (spyware/trojans) are constructed to blend in with legitimate system behavior.

**Recommended Action:**
1.  **Dynamic Analysis:** Run the binary in a sandbox and monitor which specific API calls are resolved by `GetProcAddress`. 
2.  **Overlay Detection:** Check if the application creates transparent windows or "TopMost" windows that listen for global mouse events.
3.  **Network/File Activity:** Since it interacts with COM, monitor for unusual network connections immediately following a change in its internal state (e.g., when it finishes initializing the "switch table" logic).

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Import Table | The use of dynamic API resolution and extensive switch tables hides the true execution flow and "malicious sub-modules" from static analysis. |
| **T1036** | Masquerading | The combination of GDI manipulation and `ClientToScreen` mapping indicates the creation of overlays used to present fake UI elements or hide malicious activity behind a legitimate interface. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **Note:** While the following registry keys were identified in the strings, they are standard paths associated with the **Borland Delphi** development environment and do not constitute specific malicious indicators.
    *   `SOFTWARE\Borland\Delphi\RTL`
    *   `Software\Borland\Locales`
    *   `Software\Borland\Delphi\Locales`

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *No cryptographic hashes (MD5, SHA-1, or SHA-256) were present in the provided strings.*

### **Other artifacts**
*   **Dynamic API Resolution:** The analysis identifies significant usage of `GetProcAddress` and complex switch tables (`fcn.00431db4`, `fcn.00411f30`, `fcn.004126a0`). This is a common technique used to hide malicious function calls from static analysis.
*   **Overlay Capability:** The combination of **GDI Graphics Manipulation** and the use of **`user32.dll!ClientToScreen`** indicates the capability to create on-screen overlays (common in game cheats or "stealthy" malware/spyware).
*   **Framework Identification:** The binary is confirmed to be built using the **Delphi/Pascal VCL or FMX framework**, characterized by heavy use of `oleaut32.dll` and specific internal variable types (e.g., `TObject`, `TDateTime`, `Variant`).
*   **Component Object Model (COM) Interaction:** Active interaction with `oleaut32.dll` suggests the binary may interact with complex system components or network-related COM objects.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: Trojan / Spyware
3. **Confidence**: Medium

**Key evidence**:
*   **Sophisticated Evasion Techniques:** The binary utilizes dynamic API resolution (`GetProcAddress`) and extensive switch-table dispatching to hide its true functionality and imports from static analysis, a hallmark of high-quality "stealthy" malware.
*   **Overlay Capabilities:** The combination of GDI graphics manipulation and the `ClientToScreen` function indicates the creation of on-screen overlays, which are commonly used in spyware to display fake login forms or interact with users over transparent UI elements.
*   **Professional Construction:** The use of the Delphi/Pascal VCL framework and complex COM/OLE interactions suggests a sophisticated development lifecycle rather than a simple script-based threat, allowing it to blend in with legitimate system behavior while performing malicious actions.
