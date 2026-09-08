# Threat Analysis Report

**Generated:** 2026-09-02 09:19 UTC
**Sample:** `132184d6f05f0d471b6f64c143d3d0bbd94a67ecb79c656c300662dc7274d25d_132184d6f05f0d471b6f64c143d3d0bbd94a67ecb79c656c300662dc7274d25d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `132184d6f05f0d471b6f64c143d3d0bbd94a67ecb79c656c300662dc7274d25d_132184d6f05f0d471b6f64c143d3d0bbd94a67ecb79c656c300662dc7274d25d.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64, 11 sections |
| Size | 14,389,248 bytes |
| MD5 | `da153cfe63cae14a0d66d9150019ce37` |
| SHA1 | `be8a309a090ec662f9b956d9fc7e1e63c1aa6846` |
| SHA256 | `132184d6f05f0d471b6f64c143d3d0bbd94a67ecb79c656c300662dc7274d25d` |
| Overall entropy | 5.989 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1772730492 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 8,560,640 | 5.74 | No |
| `.data` | 718,336 | 4.956 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 20,480 | 4.386 | No |
| `.didata` | 37,376 | 3.855 | No |
| `.edata` | 512 | 1.819 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 1.386 | No |
| `.reloc` | 476,672 | 6.427 | No |
| `.pdata` | 431,616 | 6.49 | No |
| `.rsrc` | 4,142,080 | 4.489 | No |

### Imports

**oleaut32.dll**: `GetErrorInfo`, `SysFreeString`
**advapi32.dll**: `RegUnLoadKeyW`, `RegSetValueExW`, `RegSaveKeyW`, `RegRestoreKeyW`, `RegReplaceKeyW`, `RegQueryValueExW`, `RegQueryInfoKeyW`, `RegOpenKeyExW`, `RegLoadKeyW`, `RegFlushKey`, `RegEnumValueW`, `RegEnumKeyW`, `RegEnumKeyExW`, `RegDeleteValueW`, `RegDeleteKeyW`
**user32.dll**: `EnumDisplayMonitors`, `GetMonitorInfoW`, `MonitorFromPoint`, `MonitorFromRect`, `MonitorFromWindow`
**kernel32.dll**: `Sleep`
**gdi32.dll**: `UnrealizeObject`, `TextOutW`, `StrokePath`, `StretchDIBits`, `StretchBlt`, `StartPage`, `StartDocW`, `SetWindowOrgEx`, `SetWinMetaFileBits`, `SetViewportOrgEx`, `SetTextColor`, `SetTextAlign`, `SetStretchBltMode`, `SetRectRgn`, `SetROP2`
**version.dll**: `VerQueryValueW`, `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`
**ole32.dll**: `CreateStreamOnHGlobal`, `ReleaseStgMedium`, `OleDraw`, `DoDragDrop`, `RevokeDragDrop`, `RegisterDragDrop`, `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoTaskMemAlloc`, `CoCreateInstance`, `CoGetClassObject`, `CoUninitialize`, `CoInitialize`, `IsEqualGUID`
**comctl32.dll**: `InitializeFlatSB`, `FlatSB_SetScrollProp`, `FlatSB_SetScrollPos`, `FlatSB_SetScrollInfo`, `FlatSB_GetScrollPos`, `FlatSB_GetScrollInfo`, `_TrackMouseEvent`, `ImageList_GetImageInfo`, `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_DragMove`
**msvcrt.dll**: `isxdigit`, `isupper`, `isspace`, `ispunct`, `isprint`, `islower`, `isgraph`, `isdigit`, `iscntrl`, `isalpha`, `isalnum`, `toupper`, `tolower`, `strchr`, `strncmp`
**shell32.dll**: `ShellExecuteW`, `Shell_NotifyIconW`, `DragQueryFileW`
**comdlg32.dll**: `PageSetupDlgW`, `PrintDlgW`, `GetSaveFileNameW`, `GetOpenFileNameW`
**winspool.drv**: `GetDefaultPrinterW`
**winmm.dll**: `timeGetTime`
**d3d9.dll**: `Direct3DCreate9`

### Exports

`TMethodImplementationIntercept`, `__dbk_fcall_wrapper`, `dbkFCallWrapperAddr`

## Extracted Strings

Total strings found: **82691** (showing first 100)

```
This program must be run under Win64
$7
`.data
.idata
.didata
.edata
.rdata
@.reloc
B.pdata
@.rsrc
Boolean
System
AnsiChar
ShortInt
SmallInt
Integer
Cardinal
Pointer
UInt64
	NativeInt

NativeUInt
Single
Extended
Double
Currency
ShortString
	PAnsiChar8
	PWideCharX
ByteBool
System
WordBool
System
LongBool
System
string

WideString


AnsiString
Variant

OleVariant

PFixedUInt
TClass
HRESULT
PGUIDh
&op_Equality
&op_Inequality
Create
	BigEndian
Create
AStartIndex
	BigEndian
PInterfaceEntryP
TInterfaceEntry(
VTable
IOffset
_Filler

ImplGetter
PInterfaceTable(
TInterfaceTable

EntryCount
_Filler
Entries
TMethod
&op_Equality
&op_Inequality
&op_GreaterThan
&op_GreaterThanOrEqual
&op_LessThan
&op_LessThanOrEqual
TObject2
Create
	DisposeOf
InitInstance
Instance
CleanupInstance
	ClassType
	ClassName
ClassNameIs
ClassParent
	ClassInfo
InstanceSize
InheritsFrom
AClass
MethodAddress
MethodAddress

MethodName
Address
QualifiedClassName
FieldAddress
FieldAddress
GetInterface
GetInterfaceEntry
GetInterfaceTable
UnitName
	UnitScope
Equals
GetHashCode
ToString
SafeCallException
ExceptObject

ExceptAddr
AfterConstruction
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00947ae7` | `0x947ae7` | 5448538 | ✓ |
| `fcn.009b8279` | `0x9b8279` | 650776 | ✓ |
| `fcn.00704d00` | `0x704d00` | 78818 | ✓ |
| `fcn.004262c0` | `0x4262c0` | 27976 | ✓ |
| `fcn.007a1cc0` | `0x7a1cc0` | 18278 | ✓ |
| `fcn.006fe146` | `0x6fe146` | 17953 | ✓ |
| `fcn.008f7f60` | `0x8f7f60` | 15965 | ✓ |
| `fcn.0079e340` | `0x79e340` | 14621 | ✓ |
| `fcn.0082c4d0` | `0x82c4d0` | 9186 | ✓ |
| `fcn.0076f580` | `0x76f580` | 6870 | ✓ |
| `fcn.00689c50` | `0x689c50` | 6518 | ✓ |
| `fcn.00803fb0` | `0x803fb0` | 6032 | ✓ |
| `fcn.00a607f0` | `0xa607f0` | 5914 | ✓ |
| `fcn.00ae3670` | `0xae3670` | 5815 | ✓ |
| `fcn.0079c1f0` | `0x79c1f0` | 5373 | ✓ |
| `fcn.00718570` | `0x718570` | 4560 | ✓ |
| `fcn.0068d110` | `0x68d110` | 4456 | ✓ |
| `fcn.0068b610` | `0x68b610` | 4429 | ✓ |
| `fcn.00afb35a` | `0xafb35a` | 4382 | ✓ |
| `fcn.00a63d00` | `0xa63d00` | 4262 | ✓ |
| `fcn.0068dbe8` | `0x68dbe8` | 4106 | ✓ |
| `fcn.0068c088` | `0x68c088` | 4090 | ✓ |
| `fcn.006e22d0` | `0x6e22d0` | 4028 | ✓ |
| `fcn.0076e4a0` | `0x76e4a0` | 4000 | ✓ |
| `fcn.00703980` | `0x703980` | 3860 | ✓ |
| `fcn.007fe690` | `0x7fe690` | 3820 | ✓ |
| `fcn.005225c0` | `0x5225c0` | 3773 | ✓ |
| `fcn.00a602c0` | `0xa602c0` | 3762 | ✓ |
| `fcn.0043b974` | `0x43b974` | 3726 | ✓ |
| `fcn.00987850` | `0x987850` | 3656 | ✓ |

### Decompiled Code Files

- [`code/fcn.004262c0.c`](code/fcn.004262c0.c)
- [`code/fcn.0043b974.c`](code/fcn.0043b974.c)
- [`code/fcn.005225c0.c`](code/fcn.005225c0.c)
- [`code/fcn.00689c50.c`](code/fcn.00689c50.c)
- [`code/fcn.0068b610.c`](code/fcn.0068b610.c)
- [`code/fcn.0068c088.c`](code/fcn.0068c088.c)
- [`code/fcn.0068d110.c`](code/fcn.0068d110.c)
- [`code/fcn.0068dbe8.c`](code/fcn.0068dbe8.c)
- [`code/fcn.006e22d0.c`](code/fcn.006e22d0.c)
- [`code/fcn.006fe146.c`](code/fcn.006fe146.c)
- [`code/fcn.00703980.c`](code/fcn.00703980.c)
- [`code/fcn.00704d00.c`](code/fcn.00704d00.c)
- [`code/fcn.00718570.c`](code/fcn.00718570.c)
- [`code/fcn.0076e4a0.c`](code/fcn.0076e4a0.c)
- [`code/fcn.0076f580.c`](code/fcn.0076f580.c)
- [`code/fcn.0079c1f0.c`](code/fcn.0079c1f0.c)
- [`code/fcn.0079e340.c`](code/fcn.0079e340.c)
- [`code/fcn.007a1cc0.c`](code/fcn.007a1cc0.c)
- [`code/fcn.007fe690.c`](code/fcn.007fe690.c)
- [`code/fcn.00803fb0.c`](code/fcn.00803fb0.c)
- [`code/fcn.0082c4d0.c`](code/fcn.0082c4d0.c)
- [`code/fcn.008f7f60.c`](code/fcn.008f7f60.c)
- [`code/fcn.00947ae7.c`](code/fcn.00947ae7.c)
- [`code/fcn.00987850.c`](code/fcn.00987850.c)
- [`code/fcn.009b8279.c`](code/fcn.009b8279.c)
- [`code/fcn.00a602c0.c`](code/fcn.00a602c0.c)
- [`code/fcn.00a607f0.c`](code/fcn.00a607f0.c)
- [`code/fcn.00a63d00.c`](code/fcn.00a63d00.c)
- [`code/fcn.00ae3670.c`](code/fcn.00ae3670.c)
- [`code/fcn.00afb35a.c`](code/fcn.00afb35a.c)

## Behavioral Analysis

This final chunk of disassembly completes the technical profile of the application, providing conclusive evidence regarding its complexity and intended purpose. The code reinforces the conclusion that this is a **highly engineered piece of software**, likely part of a professional suite, a game engine component, or a sophisticated multimedia utility.

### Final Analysis: Advanced Graphics Pipeline & Transformation Engine

The functions in this final segment transition from "user interface logic" to "core rendering and mathematical mapping."

#### 1. Multi-Stage Graphic Rendering (`fcn.00a602c0`)
This is one of the most substantial functions in the disassembly. It represents a sophisticated **Graphics Management Routine**.
*   **HDC Handling:** The function extensively uses `GetWindowDC`, `BitBlt`, and `DrawIconEx`. This isn't just "drawing an icon"; it is managing multiple distinct graphical layers or components (reflected by the repeated logic blocks for different offsets).
*   **Dynamic Icon Resolution:** The code contains logic to fallback through several potential resources (hardcoded IDs and system icons) to ensure a graphic is displayed. 
*   **Coordinate Mapping:** It performs significant arithmetic on coordinates before calling `BitBlt`. This suggests the application handles "relative positioning," where elements are placed relative to parent containers rather than absolute screen coordinates.

#### 2. Geometric Transformation & Scaling (`fcn.0043b974` & `fcn.00987850`)
These functions contain heavy mathematical loops and coordinate transformations:
*   **Nested Mapping:** The use of nested loops to iterate through dimensions (likely width/height or rows/columns) indicates a **Texture Mapping** or **Coordinate Transformation Engine**. 
*   **Scaling Logic:** Calculations like `(iVar14 - iVar13)` and various bit-shifting operations suggest the software is preparing graphics data for display on different resolutions. It likely calculates how to "stretch" or "fit" an image into a specific UI box while maintaining aspect ratios.

#### 3. State-Driven Logic Branching (`fcn.005225c0`)
This function acts as a **Dispatcher/Handler** for various internal types:
*   **Complex Conditionals:** The long chain of `if` statements checking specific constants (e.g., `0x13`, `0xE`, `0x14`) is typical of an "Object Manager." It determines how to handle different "Types" of items within the software's internal database or UI tree.
*   **Internal State Management:** The fact that it calculates lengths and handles specific flags (like `0x5236xx` series) suggests a robust system for managing diverse content types (e.g., different types of buttons, sliders, or notification windows).

---

### Final Risk Assessment Update

*   **Malicious Behavior:** **None detected.** There is no evidence of process injection, hooking, keylogging, or anti-debugging tricks in this final segment. The code is "noisy" because it is functionally dense, not because it is trying to hide.
*   **Forensic Value:** 
    *   **Sophistication Level:** Extremely High. The complexity of the mapping math (`0x43b974`) and the structured way it handles graphics resources indicates a high-budget development cycle.
    *   **Overlay/Modification Potential:** If this is being investigated as part of an "overlay" (common in game cheats), `fcn.00a602c0` is the primary area where the overlay's graphics are blended onto the target application's window or a separate overlay window.

---

### Final Summary for Incident Report

**Application Profile: Professional Multimedia/Graphics Suite.**
The analysis of all 8 chunks confirms that this application is not a simple tool; it possesses an architecture comparable to professional media software, game engines, or advanced system utilities.

*   **Core Components Identified:**
    *   **Advanced Graphics Pipeline (`fcn.00a602c0`):** A sophisticated routine for managing Device Contexts (HDC), drawing icons with fallback logic, and performing multi-layer "BitBlt" operations to composite imagery onto the screen.
    *   **Transformation & Scaling Engine (`fcn.0043b974`, `fcn.00987850`):** Complex mathematical routines used to calculate coordinate maps, likely for ensuring UI elements scale correctly across various resolutions and aspect ratios.
    *   **Stateful Dispatcher (`fcn.005225c0`):** A heavy logic-branching system that manages different types of internal components or "objects," common in large-scale software projects to handle multiple features through a single interface.
    *   **Robust Configuration Handler:** The detection of UTF-8 support, recursion limits, and various "modes" confirms the software was built for multi-language support and professional environments.

*   **Final Risk Level: Low.** 
The code is consistent with high-quality commercial software. While its complexity makes it a significant "heavyweight," there are no indicators of malicious intent or unauthorized system interaction in the provided disassembly.

*   **Technical Conclusion:**
    The application likely uses a professional framework (e.g., Delphi, C++ with a custom UI engine). It is designed for stability and visual polish. If this tool is being audited for "cheat" software, it confirms that the overlay/UI components are professionally rendered but does not provide evidence of malicious functionality beyond its intended purpose as a high-end graphics viewer or interface.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have reviewed the provided behavioral analysis. While the final assessment indicates that the application currently shows **no malicious behavior** and is consistent with high-end commercial software, we can map the specific technical capabilities identified during the disassembly to MITRE ATT&K techniques based on how those functionalities are utilized in both legitimate and adversarial contexts (e.g., sophisticated "cheat" engines or trojanized installers).

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The advanced graphic rendering, use of system icons, and professional UI design are utilized to make the application appear as a legitimate "professional suite" or high-budget tool. |
| **N/A** | *Non-Malicious Technical Functionality* | The geometric transformation and scaling routines (fcn.0043b974 & fcn.00987850) are standard mathematical operations for image processing and do not map to a specific malicious technique. |
| **T1059** | Command and Scripting Interpreter | The "State-Driven Logic Branching" (fcn.005225c0) acts as an internal dispatcher; while here used for UI objects, such complex branching is structurally similar to how malware handles internal command sets. |

### Analyst Notes:
*   **Overlay Capability:** While the technical functionality of `fcn.00a602c0` (BitBlt/GetWindowDC) is standard for any graphics application, in a threat hunting context, this specific capability is frequently flagged when investigating "Overlay" software used to provide graphical menus over other applications (common in game-cheat software).
*   **Complexity vs. Intent:** The analysis highlights that the complexity of the code does not equal malicious intent; however, the high level of sophistication suggests a professional development cycle. If this were part of an attack chain, these techniques would be used to provide "professional" polish to a fraudulent application to increase the success rate of social engineering.

---

## Indicators of Compromise

Based on my analysis of the provided strings and behavioral report, no Indicators of Compromise (IOCs) were identified. 

The content consists of standard programming library definitions (Delphi/C++ style), internal memory offsets for function calls within the binary, and a technical assessment concluding that the software is likely a legitimate professional multimedia or graphics suite with no evidence of malicious intent or unauthorized system interaction.

### IOC Summary:
*   **IP addresses / URLs / Domains:** None detected.
*   **File paths / Registry keys:** None detected (Note: `fcn.` entries are internal memory offsets, not filesystem paths).
*   **Mutex names / Named pipes:** None detected.
*   **Hashes:** None detected.
*   **Other artifacts:** None detected.

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1. **Malware family**: None (Benign / Not Malicious)
2. **Malware type**: Multimedia/Graphics Utility
3. **Confidence**: High
4. **Key evidence**:
    * **No Malicious Indicators:** The behavioral analysis explicitly states that no process injection, hooking, keylogging, or anti-debugging tricks were found in the code. 
    * **Professional Functionality:** The disassembly reveals high-quality engineering consistent with a professional graphics suite or game engine (e.g., advanced bit-blitting, coordinate transformation mapping, and state-driven logic).
    * **Lack of IOCs:** No network indicators, unauthorized file paths, or malicious behaviors were detected; the analysis concludes the software is likely a high-end commercial utility rather than malware.
