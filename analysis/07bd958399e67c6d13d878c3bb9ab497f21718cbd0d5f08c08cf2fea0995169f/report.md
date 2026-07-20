# Threat Analysis Report

**Generated:** 2026-07-17 18:40 UTC
**Sample:** `07bd958399e67c6d13d878c3bb9ab497f21718cbd0d5f08c08cf2fea0995169f_07bd958399e67c6d13d878c3bb9ab497f21718cbd0d5f08c08cf2fea0995169f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07bd958399e67c6d13d878c3bb9ab497f21718cbd0d5f08c08cf2fea0995169f_07bd958399e67c6d13d878c3bb9ab497f21718cbd0d5f08c08cf2fea0995169f.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64, 11 sections |
| Size | 5,407,744 bytes |
| MD5 | `68bcbeb83b70f92eae4c464d1670dd56` |
| SHA1 | `5ec940307c4f32c60608f8443ee6dd5c47499de8` |
| SHA256 | `07bd958399e67c6d13d878c3bb9ab497f21718cbd0d5f08c08cf2fea0995169f` |
| Overall entropy | 6.273 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769731340 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 3,608,576 | 5.76 | No |
| `.data` | 313,856 | 4.758 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 19,456 | 4.399 | No |
| `.didata` | 4,096 | 3.154 | No |
| `.edata` | 512 | 1.843 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 1.375 | No |
| `.reloc` | 177,664 | 6.477 | No |
| `.pdata` | 202,240 | 6.334 | No |
| `.rsrc` | 1,079,808 | 6.296 | No |

### Imports

**oleaut32.dll**: `CreateErrorInfo`, `GetErrorInfo`, `SetErrorInfo`, `GetActiveObject`, `SysFreeString`
**advapi32.dll**: `RegUnLoadKeyW`, `RegSetValueExW`, `RegSaveKeyW`, `RegRestoreKeyW`, `RegReplaceKeyW`, `RegQueryValueExW`, `RegQueryInfoKeyW`, `RegOpenKeyExW`, `RegLoadKeyW`, `RegFlushKey`, `RegEnumValueW`, `RegEnumKeyExW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegCreateKeyExW`
**user32.dll**: `EnumDisplayMonitors`, `GetMonitorInfoW`, `MonitorFromPoint`, `MonitorFromRect`, `MonitorFromWindow`
**kernel32.dll**: `Sleep`
**gdi32.dll**: `WidenPath`, `UnrealizeObject`, `TextOutW`, `StrokePath`, `StrokeAndFillPath`, `StretchDIBits`, `StretchBlt`, `StartPage`, `StartDocW`, `SetWindowOrgEx`, `SetWinMetaFileBits`, `SetViewportOrgEx`, `SetTextCharacterExtra`, `SetTextColor`, `SetTextAlign`
**version.dll**: `VerQueryValueW`, `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoTaskMemAlloc`, `ProgIDFromCLSID`, `StringFromCLSID`, `CoCreateInstance`, `CoUninitialize`, `CoInitialize`, `IsEqualGUID`
**comctl32.dll**: `InitializeFlatSB`, `FlatSB_SetScrollProp`, `FlatSB_SetScrollPos`, `FlatSB_SetScrollInfo`, `FlatSB_GetScrollPos`, `FlatSB_GetScrollInfo`, `_TrackMouseEvent`, `ImageList_GetImageInfo`, `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_DragMove`
**shell32.dll**: `Shell_NotifyIconW`
**winspool.drv**: `GetDefaultPrinterW`

### Exports

`TMethodImplementationIntercept`, `__dbk_fcall_wrapper`, `dbkFCallWrapperAddr`

## Extracted Strings

Total strings found: **27598** (showing first 100)

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
&op_Equality
&op_Inequality
Create
	BigEndian
Create
AStartIndex
	BigEndian
PInterfaceEntryh
TInterfaceEntry(
VTable
IOffset
_Filler

ImplGetter
PInterfaceTable@
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
BeforeDestruction
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.005544d4` | `0x5544d4` | 1304231 | ✓ |
| `fcn.004c6ec1` | `0x4c6ec1` | 72162 | ✓ |
| `fcn.0055ca95` | `0x55ca95` | 68287 | ✓ |
| `fcn.004237d0` | `0x4237d0` | 27976 | ✓ |
| `fcn.006d7930` | `0x6d7930` | 7752 | ✓ |
| `fcn.00699570` | `0x699570` | 6882 | ✓ |
| `fcn.00697a70` | `0x697a70` | 6770 | ✓ |
| `fcn.006960bc` | `0x6960bc` | 6506 | ✓ |
| `fcn.0070ac70` | `0x70ac70` | 4776 | ✓ |
| `fcn.00438b4b` | `0x438b4b` | 3644 | ✓ |
| `fcn.006cd3e0` | `0x6cd3e0` | 3456 | ✓ |
| `fcn.00710050` | `0x710050` | 3456 | ✓ |
| `fcn.00432783` | `0x432783` | 3156 | ✓ |
| `fcn.00614438` | `0x614438` | 3133 | ✓ |
| `fcn.0043bf60` | `0x43bf60` | 3124 | ✓ |
| `fcn.0075e080` | `0x75e080` | 3073 | ✓ |
| `fcn.006c29d0` | `0x6c29d0` | 2744 | ✓ |
| `fcn.004553e0` | `0x4553e0` | 2678 | ✓ |
| `fcn.00456240` | `0x456240` | 2552 | ✓ |
| `fcn.00456ea0` | `0x456ea0` | 2522 | ✓ |
| `fcn.00703bd0` | `0x703bd0` | 2503 | ✓ |
| `fcn.00705f50` | `0x705f50` | 2462 | ✓ |
| `fcn.0069b410` | `0x69b410` | 2347 | ✓ |
| `fcn.00599380` | `0x599380` | 2346 | ✓ |
| `fcn.005cdb30` | `0x5cdb30` | 2327 | ✓ |
| `fcn.004f7e33` | `0x4f7e33` | 2271 | ✓ |
| `fcn.0060b180` | `0x60b180` | 2227 | ✓ |
| `fcn.006091b0` | `0x6091b0` | 2224 | ✓ |
| `fcn.0070f4e0` | `0x70f4e0` | 2197 | ✓ |
| `fcn.006cf820` | `0x6cf820` | 2169 | ✓ |

### Decompiled Code Files

- [`code/fcn.004237d0.c`](code/fcn.004237d0.c)
- [`code/fcn.00432783.c`](code/fcn.00432783.c)
- [`code/fcn.00438b4b.c`](code/fcn.00438b4b.c)
- [`code/fcn.0043bf60.c`](code/fcn.0043bf60.c)
- [`code/fcn.004553e0.c`](code/fcn.004553e0.c)
- [`code/fcn.00456240.c`](code/fcn.00456240.c)
- [`code/fcn.00456ea0.c`](code/fcn.00456ea0.c)
- [`code/fcn.004c6ec1.c`](code/fcn.004c6ec1.c)
- [`code/fcn.004f7e33.c`](code/fcn.004f7e33.c)
- [`code/fcn.005544d4.c`](code/fcn.005544d4.c)
- [`code/fcn.0055ca95.c`](code/fcn.0055ca95.c)
- [`code/fcn.00599380.c`](code/fcn.00599380.c)
- [`code/fcn.005cdb30.c`](code/fcn.005cdb30.c)
- [`code/fcn.006091b0.c`](code/fcn.006091b0.c)
- [`code/fcn.0060b180.c`](code/fcn.0060b180.c)
- [`code/fcn.00614438.c`](code/fcn.00614438.c)
- [`code/fcn.006960bc.c`](code/fcn.006960bc.c)
- [`code/fcn.00697a70.c`](code/fcn.00697a70.c)
- [`code/fcn.00699570.c`](code/fcn.00699570.c)
- [`code/fcn.0069b410.c`](code/fcn.0069b410.c)
- [`code/fcn.006c29d0.c`](code/fcn.006c29d0.c)
- [`code/fcn.006cd3e0.c`](code/fcn.006cd3e0.c)
- [`code/fcn.006cf820.c`](code/fcn.006cf820.c)
- [`code/fcn.006d7930.c`](code/fcn.006d7930.c)
- [`code/fcn.00703bd0.c`](code/fcn.00703bd0.c)
- [`code/fcn.00705f50.c`](code/fcn.00705f50.c)
- [`code/fcn.0070ac70.c`](code/fcn.0070ac70.c)
- [`code/fcn.0070f4e0.c`](code/fcn.0070f4e0.c)
- [`code/fcn.00710050.c`](code/fcn.00710050.c)
- [`code/fcn.0075e080.c`](code/fcn.0075e080.c)

## Behavioral Analysis

This final analysis incorporates the disassembly from chunk 4. This last segment provides a definitive look at the **Front-End Interaction Layer**, specifically how the software handles window management, positioning, and multi-layered UI elements.

The inclusion of this code confirms that the application is not just "using" an overlay; it is managing a **complex, dynamic, multi-layered graphical interface** designed to behave consistently regardless of environmental changes (like game resolution shifts or other windows overlapping).

### Updated Summary of Findings

#### 1. Dynamic Overlay Positioning & Persistence
The logic in `fcn.006cf820` reveals an extensive system for calculating and applying window coordinates.
*   **Coordinate Offsetting:** The code performs numerous calculations involving offsets (e.g., `iStack_38`, `iStack_2c - *(arg1_00 + 0x9c)`). This is used to "pin" a menu or HUD onto another window. By calculating the difference between a target window and an offset, the program ensures that if the game window moves or resizes, the overlay follows it perfectly.
*   **Robustness Logic:** The repetitive checks (e.g., `if (iStack_38 < iVar7)`, `if (iStack_60 < iVar12)`) suggest a "fail-safe" mechanism. It is ensuring that even if the math results in coordinates outside of the screen bounds, the window remains positioned correctly within the expected area.

#### 2. Multi-Layered UI Management
The code handles multiple window handles (`arg1_00`, `arg1_01`, and a third hidden at `*(arg1 + 0xd0)`).
*   **State-Based Visibility:** The use of `ShowWindow` with different flags (e.g., `0` for hidden, `5` for showing) indicates that the application manages multiple layers. For example:
    *   Layer 1: A primary transparent overlay (usually always visible to the user).
    *   Layer 2: A secondary "menu" layer (only shown when a key is pressed).
    *   Layer 3: An internal "buffer" or "overlay-base" window that remains hidden from the OS but provides the surface for rendering.
*   **Visibility Syncing:** The code checks if windows are visible before performing updates, ensuring that only the currently active components of the UI are being processed by the engine.

#### 3. Resolution & Aspect Ratio Independence
The frequent usage of `GetWindowRect` followed immediately by calculation blocks indicates a system designed to handle **Resolution Scaling**. Instead of using hard-coded pixel values (which would break on different monitors), it calculates coordinates relative to the current window size, ensuring the GUI looks correct whether the user is in 1080p, 1440p, or ultra-wide resolutions.

#### 4. Continuous State Monitoring (Recurrence)
The final part of `fcn.006cf820` contains a recursive/looping call: `if (bVar3) { fcn.006cf820(arg1); }`.
*   **Implication:** This is an update loop. The application is constantly polling the state of its windows and the game window to ensure that if any window is moved or resized, the overlay "snaps" back into the correct position instantly.

---

### Updated Technical Indicators (Comprehensive)

| Feature | Evidence Location | Analysis / Impact |
| :--- | :--- | :--- |
| **Custom VM** | `fcn.0043b...` (Chunk 3) | Obscures core logic and "cheat" mechanics within a proprietary bytecode layer. |
| **Dispatcher Obfuscation** | `fcn.004553e0`, `fcn.00456240` | Prevents linear analysis of the code by routing execution through complex conditional meshes. |
| **Overlay/Rendering Engine** | `fcn.00703bd0`, `fcn.00599380` | Confirmed use of GDI (BitBlt, GetDC) to render high-performance graphics over other apps. |
| **Dynamic Positioning** | `fcn.006cf820` | Complex math for "pinning" UI elements to the game window regardless of resolution or position. |
| **Multi-Layered GUI** | `fcn.006cf820`, `arg1_00/01` | Management of multiple hidden and visible windows to create a sophisticated, multi-part user interface. |
| **Decompiler Sabotage** | `fcn.004f7e33` | Intentional use of "bad data" and overlapping instructions to crash or confuse analysis tools (IDA/Ghidra). |

---

### Final Conclusion

This binary is a high-end, professionally engineered piece of software with a sophisticated **layered defense architecture**. It has been designed specifically to withstand deep technical scrutiny while providing a seamless user experience.

The relationship between the different parts of the code provides a clear picture of its purpose:
1.  **The Protection Layer:** The VM and Dispatchers ensure that anyone trying to "crack" or reverse-engineer the internal logic (e.g., how it interacts with game memory or anti-cheat systems) faces a massive wall of complexity.
2.  **The Anti-Analysis Layer:** The "decompiler sabotage" acts as a landmine for automated tools, making it difficult for an analyst to even begin looking at the code.
3.  **The Rendering/UI Layer:** The extensive GDI manipulation and dynamic positioning logic confirm that this is a high-fidelity overlay system.

The combination of **hidden backend logic (VM)** + **hardened front-end mechanics (Dispatcher/Anti-Analysis)** + **advanced graphical rendering (GDI Offsets)** confirms the classification: This is likely a **premium, professional-grade game cheat or specialized internal utility.** The level of care put into "hiding" the code while ensuring the overlay remains stable and responsive across different screen resolutions is characteristic of software intended for use in environments with active anti-tamper measures.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the relevant MITRE ATT&CK techniques. The primary focus of this malware’s design is **Defense Evasion**, specifically through complex obfuscation and anti-analysis measures intended to hinder reverse engineering.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a **Custom VM** and **Dispatcher Obfuscation** masks the core logic and "cheat" mechanics behind proprietary bytecode and complex execution paths. |
| **T1027** | Obfuscated Files or Information | **Decompiler Sabotage** (using "bad data" and overlapping instructions) is a deliberate tactic to crash or mislead common analysis tools like IDA Pro and Ghidra. |
| **T1036** | Masquerading | The use of a **Multi-Layered UI** with hidden "buffer" windows allows the application to separate its backend operations from the visible interface, complicating the identification of its full capabilities. |

### Analyst Notes:
*   **Defense Evasion Focus:** The most prominent behaviors (VM, Dispatcher, and Decompiler Sabotage) fall under **T1027**. This indicates a high level of sophistication; the author is not just trying to hide from an end-user but specifically attempting to defeat professional security researchers.
*   **Persistence via Overlay:** While "Overlay" isn't a standalone technique in MITRE ATT&CK, the behavior described in **Dynamic Positioning** and **Continuous State Monitoring** indicates a high degree of reliability. In a malware context, this ensures that the malicious overlay remains "glued" to the target application (the game) regardless of user actions or system changes.
*   **Target Environment:** The combination of these techniques suggests an environment where the adversary expects detection by automated systems and manual analysis (e.g., anti-cheat software or security researchers), necessitating a "layered defense" approach.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The provided text contains high-level technical descriptions and internal code signatures rather than network-based or filesystem-based IOCs (such as hardcoded C2 IPs or specific file paths).

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: System strings like `System` and `.data` are standard library components and were excluded as false positives.)

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
The following represent specific internal code offsets and technical signatures used to identify the behavior of this specific sample:

*   **Internal Function Offsets (Evidence of specific logic):**
    *   `fcn.006cf820` (Dynamic Positioning / Multi-layered GUI)
    *   `fcn.0043b...` (Custom VM implementation)
    *   `fcn.004553e0` (Dispatcher Obfuscation)
    *   `fcn.00456240` (Dispatcher Obfuscation)
    *   `fcn.00703bd0` (GDI Rendering Engine)
    *   `fcn.00599380` (GDI Rendering Engine)
    *   `fcn.004f7e33` (Decompiler Sabotage/Anti-Analysis)
*   **Behavioral Indicators:**
    *   **Custom VM Usage:** Use of a proprietary bytecode layer to hide core logic.
    *   **Decompiler Sabotage:** Intentional use of "bad data" and overlapping instructions to crash analysis tools (IDA/Ghidra).
    *   **Multi-Layered Window Management:** Specific handling of multiple window handles (`arg1_00`, `arg1_01`, and `*(arg1 + 0xd0)`) to hide UI layers.
    *   **State Tracking:** Iterative usage of `ShowWindow` with specific flags (e.g., `0` and `5`).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: overlay / game cheat
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Anti-Analysis Techniques:** The sample employs highly sophisticated "defense" mechanisms including a **Custom VM**, **Dispatcher Obfuscation**, and **Decompiler Sabotage**. These are signature techniques used to hide complex logic from security researchers and anti-cheat software.
*   **Sophisticated Graphical Overlay:** Analysis of `fcn.006cf820` and GDI calls (`BitBlt`, `GetDC`) confirms a multi-layered rendering system designed to "pin" a GUI onto a target window while remaining independent of resolution changes—a hallmark of high-end cheat software.
*   **Lack of Traditional Malware Payload:** The absence of C2 infrastructure (IPs/URLs) and the specific focus on UI management and environment-agnostic positioning indicate that the primary objective is local functionality for a game environment rather than remote data exfiltration or system destruction.
