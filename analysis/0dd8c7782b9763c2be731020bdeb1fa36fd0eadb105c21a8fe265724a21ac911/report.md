# Threat Analysis Report

**Generated:** 2026-08-10 16:58 UTC
**Sample:** `0dd8c7782b9763c2be731020bdeb1fa36fd0eadb105c21a8fe265724a21ac911_0dd8c7782b9763c2be731020bdeb1fa36fd0eadb105c21a8fe265724a21ac911.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0dd8c7782b9763c2be731020bdeb1fa36fd0eadb105c21a8fe265724a21ac911_0dd8c7782b9763c2be731020bdeb1fa36fd0eadb105c21a8fe265724a21ac911.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 5,089,552 bytes |
| MD5 | `715002d1290a226e34a4a5197998aa82` |
| SHA1 | `7609dad0e2175b4c9fac073179576238c2b9b5e4` |
| SHA256 | `0dd8c7782b9763c2be731020bdeb1fa36fd0eadb105c21a8fe265724a21ac911` |
| Overall entropy | 6.172 |
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
| `CODE` | 389,632 | 6.553 | No |
| `DATA` | 5,632 | 3.977 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 9,216 | 4.825 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.201 | No |
| `.reloc` | 27,648 | 6.682 | No |
| `.rsrc` | 4,642,304 | 5.968 | No |

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

Total strings found: **6098** (showing first 100)

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
TObjectP
TObjectD
System

IInterface
System
TInterfacedObject
TBoundArray
Systemx
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
t@hlU@
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
EZeroDivide<w@
	EOverflow

EUnderflow
EInvalidPointerHx@
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
_^[YY]
$YZ_^[
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x4600d4` | 4237 | ✓ |
| `fcn.004033d8` | `0x4033d8` | 2577 | ✓ |
| `fcn.00448ea0` | `0x448ea0` | 2312 | ✓ |
| `fcn.00448598` | `0x448598` | 2280 | ✓ |
| `fcn.00409f7c` | `0x409f7c` | 1921 | ✓ |
| `fcn.00456bbc` | `0x456bbc` | 1750 | ✓ |
| `fcn.00426dd8` | `0x426dd8` | 1633 | ✓ |
| `fcn.0042d0c0` | `0x42d0c0` | 1392 | ✓ |
| `fcn.00412e04` | `0x412e04` | 1362 | ✓ |
| `fcn.004126dc` | `0x4126dc` | 1335 | ✓ |
| `fcn.0044a8e4` | `0x44a8e4` | 1183 | ✓ |
| `fcn.004281bc` | `0x4281bc` | 1131 | ✓ |
| `fcn.0040fd7c` | `0x40fd7c` | 1097 | ✓ |
| `fcn.00410840` | `0x410840` | 1088 | ✓ |
| `fcn.0043abd8` | `0x43abd8` | 1085 | ✓ |
| `fcn.0043f150` | `0x43f150` | 978 | ✓ |
| `fcn.00412028` | `0x412028` | 965 | ✓ |
| `fcn.004510a3` | `0x4510a3` | 950 | ✓ |
| `fcn.0042bc4c` | `0x42bc4c` | 947 | ✓ |
| `fcn.0042f548` | `0x42f548` | 905 | ✓ |
| `fcn.00458838` | `0x458838` | 902 | ✓ |
| `fcn.00433f53` | `0x433f53` | 891 | ✓ |
| `fcn.00411350` | `0x411350` | 885 | ✓ |
| `fcn.00452040` | `0x452040` | 852 | ✓ |
| `fcn.00411ac0` | `0x411ac0` | 846 | ✓ |
| `fcn.00410e3c` | `0x410e3c` | 836 | ✓ |
| `fcn.00414378` | `0x414378` | 834 | ✓ |
| `fcn.00408c1e` | `0x408c1e` | 828 | ✓ |
| `fcn.0040e82a` | `0x40e82a` | 815 | ✓ |
| `fcn.0040aa60` | `0x40aa60` | 795 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004033d8.c`](code/fcn.004033d8.c)
- [`code/fcn.00408c1e.c`](code/fcn.00408c1e.c)
- [`code/fcn.00409f7c.c`](code/fcn.00409f7c.c)
- [`code/fcn.0040aa60.c`](code/fcn.0040aa60.c)
- [`code/fcn.0040e82a.c`](code/fcn.0040e82a.c)
- [`code/fcn.0040fd7c.c`](code/fcn.0040fd7c.c)
- [`code/fcn.00410840.c`](code/fcn.00410840.c)
- [`code/fcn.00410e3c.c`](code/fcn.00410e3c.c)
- [`code/fcn.00411350.c`](code/fcn.00411350.c)
- [`code/fcn.00411ac0.c`](code/fcn.00411ac0.c)
- [`code/fcn.00412028.c`](code/fcn.00412028.c)
- [`code/fcn.004126dc.c`](code/fcn.004126dc.c)
- [`code/fcn.00412e04.c`](code/fcn.00412e04.c)
- [`code/fcn.00414378.c`](code/fcn.00414378.c)
- [`code/fcn.00426dd8.c`](code/fcn.00426dd8.c)
- [`code/fcn.004281bc.c`](code/fcn.004281bc.c)
- [`code/fcn.0042bc4c.c`](code/fcn.0042bc4c.c)
- [`code/fcn.0042d0c0.c`](code/fcn.0042d0c0.c)
- [`code/fcn.0042f548.c`](code/fcn.0042f548.c)
- [`code/fcn.00433f53.c`](code/fcn.00433f53.c)
- [`code/fcn.0043abd8.c`](code/fcn.0043abd8.c)
- [`code/fcn.0043f150.c`](code/fcn.0043f150.c)
- [`code/fcn.00448598.c`](code/fcn.00448598.c)
- [`code/fcn.00448ea0.c`](code/fcn.00448ea0.c)
- [`code/fcn.0044a8e4.c`](code/fcn.0044a8e4.c)
- [`code/fcn.004510a3.c`](code/fcn.004510a3.c)
- [`code/fcn.00452040.c`](code/fcn.00452040.c)
- [`code/fcn.00456bbc.c`](code/fcn.00456bbc.c)
- [`code/fcn.00458838.c`](code/fcn.00458838.c)

## Behavioral Analysis

This final segment of disassembly provides a deeper look into the internal logic and "scaffolding" used by the application. The findings here reinforce the previous conclusions while providing more granular detail on how the compiler translates high-level code (Delphi/VCL) into machine instructions.

### Updated Analysis: Technical Breakdown (Chunk 3/3)

#### 1. Massive Parameter Handling & Abstract Data Types
The function **`fcn.0040e82a`** is particularly notable for its signature, which includes an extremely large number of parameters (`param_1` through `param_58`).
*   **Technical Context:** In the context of Delphi, this is not a sign of "malware-style" packing, but rather how the compiler handles **complex structures or records**. Instead of passing a single pointer to a massive structure, the underlying framework may be unpacking these values for immediate use in high-level logic.
*   **Analysis Impact:** For a human analyst, this creates significant noise. It indicates that the code is dealing with very complex "Objects" (likely UI components or state machines). When you see functions like this, it usually means the core logic is wrapped inside multiple layers of abstraction provided by the VCL library.

#### 2. Complex Branching and State Logic
The disassembly for `fcn.0040e82a` and `fcn.0040aa60` shows heavy use of nested conditional checks (`if-else`) and jumps to specific labels (e.g., `code_r0x0040e89f`).
*   **Control Flow Complexity:** The code frequently checks values against internal constants or results from very small, inline helper functions (like `fcn.0040a91c` or `f.0040a7c4`).
*   **Hidden State Machines:** These patterns are characteristic of **message routing**. In a GUI application, when a user clicks a button, the program traverses a tree of "checks" to determine what that specific button does, how it should look, and whether any "hover" or "click" effects should trigger.

#### 3. Evidence of Robust Error Handling/Validation
In **`fcn.0040aa60`**, we see logic involving:
*   **String Comparison/Guard Checks:** Comparisons like `(**0x463690 != 'g')` suggest the program is checking for specific string prefixes or internal identifiers before proceeding to a block of code.
*   **Length and Range Checking:** The loop structure (the `do...while` loop) suggests that the application is iterating through an array or list—likely an array of UI elements, items in a menu, or properties of a loaded object.

---

### Final Cumulative Summary for Report

The final analysis of all three segments confirms that this binary is a **highly structured, complex Delphi-based application.** It leverages a sophisticated framework (VCL) to manage its internal state and graphical presentation.

#### Core Findings:
1.  **Sophisticated GUI/Framework Integration:** The presence of large switch tables, extensive GDI-related math, and massive parameter lists in functions like `fcn.0040e82a` confirms that this is not a simple standalone script or "thin" malware. It uses a heavy framework to manage complex interactions between the user and the display.
2.  **Intentional Complexity (Obfuscation by Compilation):** The analysis highlights how Delphi's compilation style creates significant "analytical noise." High-level features like polymorphism and object-oriented programming result in large, nested logic trees that make it difficult for an analyst to pinpoint specific malicious behaviors without deep knowledge of the VCL framework.
3.  **Dynamic Capability:** As identified in previous chunks (specifically `fcn.0042bc4c`), the program is capable of loading external modules via `LoadLibraryA` and `GetProcAddress`. While common in complex software, this remains a primary area for monitoring during dynamic analysis to see what "extra" functionality is injected at runtime.
4.  **Rich Visual Presence:** The heavy use of GDI calls (`CreateDIBSection`, etc.) suggests the application has high-quality graphics or custom-rendered UI elements, which could be used to build a professional look for legitimate software or an engaging interface for "scareware."

#### Risk Profile & Conclusion:
The binary exhibits characteristics of **sophisticated, professionally developed software**. 
*   **If this is a legitimate tool:** It indicates it is likely a complex enterprise application or game-related component.
*   **If this is malicious:** The use of Delphi and the resulting "complexity" serves as an effective way to hide core logic from automated scanners. The "noise" created by the GUI framework provides a layer of protection, allowing suspicious actions (like those potentially hidden in dynamically loaded DLLs) to be buried deep within standard-looking library code.

#### Recommendations:
*   **Targeted Dynamic Analysis:** Focus on `fcn.0042bc4c` during execution. Monitor which specific DLLs are called and if those DLLs perform network connections or file system modifications.
*   **Memory Dump Comparison:** Perform a memory dump before and after the dynamic loading phase to identify "unpacked" code that only appears in RAM.
*   **Signature Verification:** Since Delphi-heavy binaries are common, compare the core library calls against known Delphi compiler versions to distinguish between standard "bloat" and custom malicious functions.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, the following MITRE ATT&CK techniques have been identified:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Dynamic Resolution | The analyst notes the use of `LoadLibraryA` and `GetProcAddress`, which are primary indicators of dynamically resolving functions to bypass static analysis. |
| **T1027** | Obfuscated Files or Information | The report explicitly states that the complexity of the Delphi VCL framework creates "analytical noise," serving as a means to hide core logic from analysts. |
| **T1059** | Command and Scripting Interpreter | While not directly a command line, the "hidden state machines" and complex branching logic are used to manage internal transitions that can mask the actual execution path of malicious commands. |

***

**Analyst Notes:**
*   **T1036 (Dynamic Resolution)** is the most critical finding for active monitoring; any calls to `GetProcAddress` should be flagged as high-interest targets during dynamic analysis.
*   **T1027 (Obfuscated Files or Information)** applies here in a structural sense: the "intentional complexity" of the compiler's output acts as a layer of protection to bury malicious actions deep within standard library code.

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `SOFTWARE\Borland\Delphi\RTL`
*   `Software\Borland\Locales`
*   `Software\Borland\Delphi\Locales`

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Dynamic Loading Behavior:** Function `fcn.0042bc4c` was identified as utilizing `LoadLibraryA` and `GetProcAddress`. This indicates the application dynamically loads external DLLs or components at runtime.
*   **Framework Identification:** The heavy presence of Delphi/VCL-specific strings (e.g., `TObjectP`, `TInterfacedObject`, `EMemoryError`) confirms the use of the Borland Delphi compiler, which is often used to mask core logic behind standard framework "noise."

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: Medium
4. **Key evidence**:
    * **Evasive "Analysis Noise":** The sample utilizes the Delphi VCL framework to create a high level of structural complexity and "analytical noise," which is a common technique used by malware authors to mask core malicious logic within standard library code.
    * **Dynamic Resolution:** The identification of `LoadLibraryA` and `GetProcAddress` (T1036) in function `fcn.0042bc4c` indicates that the binary is designed to load external modules at runtime, a hallmark of loaders used to fetch secondary payloads or bypass static analysis.
    * **Lack of Direct Payload Indicators:** While the behavior suggests a sophisticated "wrapper" or "scaffolding," no specific C2 infrastructure (IPs/URLs) or immediate malicious actions (encryption, theft) were identified in this segment, suggesting it serves as a delivery vehicle rather than a final-stage malware payload.
