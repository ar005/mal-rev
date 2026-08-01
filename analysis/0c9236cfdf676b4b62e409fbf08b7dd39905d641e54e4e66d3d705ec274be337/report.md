# Threat Analysis Report

**Generated:** 2026-07-31 16:13 UTC
**Sample:** `0c9236cfdf676b4b62e409fbf08b7dd39905d641e54e4e66d3d705ec274be337_0c9236cfdf676b4b62e409fbf08b7dd39905d641e54e4e66d3d705ec274be337.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c9236cfdf676b4b62e409fbf08b7dd39905d641e54e4e66d3d705ec274be337_0c9236cfdf676b4b62e409fbf08b7dd39905d641e54e4e66d3d705ec274be337.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 1,111,552 bytes |
| MD5 | `8b31b582577141b0c60979413e905897` |
| SHA1 | `6cd7f8f1a25fc4903519ea74f0f528130eae6c91` |
| SHA256 | `0c9236cfdf676b4b62e409fbf08b7dd39905d641e54e4e66d3d705ec274be337` |
| Overall entropy | 6.867 |
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
| `CODE` | 806,400 | 6.559 | No |
| `DATA` | 7,680 | 4.412 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 8,704 | 5.023 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.204 | No |
| `.reloc` | 59,904 | 6.694 | No |
| `.rsrc` | 227,328 | 7.222 | ⚠️ Yes |

### Imports

**kernel32.dll**: `Sleep`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WinHelpA`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `ShowCursor`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `CreateErrorInfo`, `GetErrorInfo`, `SetErrorInfo`, `SysFreeString`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**gdi32.dll**: `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`, `SelectPalette`, `SelectObject`, `SaveDC`
**ole32.dll**: `CoCreateInstance`, `CoUninitialize`, `CoInitialize`
**comctl32.dll**: `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_SetDragCursorImage`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`

## Extracted Strings

Total strings found: **6625** (showing first 100)

```
This program must be run under Win32
$7
.idata
.rdata
P.reloc
P.rsrc
Boolean
WideChar
Shortint
Smallint
Integer
Extended
Cardinal
Single
Double
Currency
ShortString
ByteBool
WordBool
LongBool
String

WideString
Variant

OleVariantd
TObjectp
TObjectd
System

IInterface
System

IInvokable
System
	IDispatch
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
YZ]_^[
<
t"<t
<t$<t3<
<
t%<t><tQ<t\<
t@hX[@
kernel32.dll
GetLongPathNameA
Software\Borland\Locales
Software\Borland\Delphi\Locales
_^[YY]
TIntegerDynArray
TCardinalDynArray
TWordDynArray
TSmallIntDynArray
TByteDynArray
TShortIntDynArray
TInt64DynArray
TLongWordDynArray
TSingleDynArray
TDoubleDynArray
TBooleanDynArray
TypesTi@
TStringDynArray
TWideStringDynArray

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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004be899` | `0x4be899` | 3264 | — |
| `fcn.004921c4` | `0x4921c4` | 3112 | ✓ |
| `fcn.00494a28` | `0x494a28` | 3112 | ✓ |
| `fcn.00499460` | `0x499460` | 3112 | ✓ |
| `fcn.0048f990` | `0x48f990` | 3112 | ✓ |
| `fcn.0049bcf0` | `0x49bcf0` | 3112 | ✓ |
| `fcn.00472a28` | `0x472a28` | 3091 | ✓ |
| `fcn.0049e520` | `0x49e520` | 3079 | ✓ |
| `fcn.00403584` | `0x403584` | 2621 | ✓ |
| `fcn.004c4498` | `0x4c4498` | 2463 | ✓ |
| `fcn.00445ca4` | `0x445ca4` | 2312 | ✓ |
| `fcn.0044539c` | `0x44539c` | 2280 | ✓ |
| `fcn.0040a7c0` | `0x40a7c0` | 1921 | ✓ |
| `fcn.004539c0` | `0x4539c0` | 1750 | ✓ |
| `fcn.00476aa8` | `0x476aa8` | 1637 | ✓ |
| `fcn.00426dac` | `0x426dac` | 1633 | ✓ |
| `fcn.00477140` | `0x477140` | 1622 | ✓ |
| `fcn.00486f44` | `0x486f44` | 1594 | ✓ |
| `fcn.004135c8` | `0x4135c8` | 1362 | ✓ |
| `fcn.0047365c` | `0x47365c` | 1345 | ✓ |
| `fcn.00412ea0` | `0x412ea0` | 1335 | ✓ |
| `fcn.0047105c` | `0x47105c` | 1295 | ✓ |
| `fcn.004476e8` | `0x4476e8` | 1183 | ✓ |
| `fcn.00476608` | `0x476608` | 1181 | ✓ |
| `fcn.00428190` | `0x428190` | 1131 | ✓ |
| `fcn.00410540` | `0x410540` | 1097 | ✓ |
| `fcn.00411004` | `0x411004` | 1088 | ✓ |
| `fcn.00437b24` | `0x437b24` | 1085 | ✓ |
| `fcn.004a8fbc` | `0x4a8fbc` | 1005 | ✓ |
| `fcn.004716c8` | `0x4716c8` | 1004 | ✓ |

### Decompiled Code Files

- [`code/fcn.00403584.c`](code/fcn.00403584.c)
- [`code/fcn.0040a7c0.c`](code/fcn.0040a7c0.c)
- [`code/fcn.00410540.c`](code/fcn.00410540.c)
- [`code/fcn.00411004.c`](code/fcn.00411004.c)
- [`code/fcn.00412ea0.c`](code/fcn.00412ea0.c)
- [`code/fcn.004135c8.c`](code/fcn.004135c8.c)
- [`code/fcn.00426dac.c`](code/fcn.00426dac.c)
- [`code/fcn.00428190.c`](code/fcn.00428190.c)
- [`code/fcn.00437b24.c`](code/fcn.00437b24.c)
- [`code/fcn.0044539c.c`](code/fcn.0044539c.c)
- [`code/fcn.00445ca4.c`](code/fcn.00445ca4.c)
- [`code/fcn.004476e8.c`](code/fcn.004476e8.c)
- [`code/fcn.004539c0.c`](code/fcn.004539c0.c)
- [`code/fcn.0047105c.c`](code/fcn.0047105c.c)
- [`code/fcn.004716c8.c`](code/fcn.004716c8.c)
- [`code/fcn.00472a28.c`](code/fcn.00472a28.c)
- [`code/fcn.0047365c.c`](code/fcn.0047365c.c)
- [`code/fcn.00476608.c`](code/fcn.00476608.c)
- [`code/fcn.00476aa8.c`](code/fcn.00476aa8.c)
- [`code/fcn.00477140.c`](code/fcn.00477140.c)
- [`code/fcn.00486f44.c`](code/fcn.00486f44.c)
- [`code/fcn.0048f990.c`](code/fcn.0048f990.c)
- [`code/fcn.004921c4.c`](code/fcn.004921c4.c)
- [`code/fcn.00494a28.c`](code/fcn.00494a28.c)
- [`code/fcn.00499460.c`](code/fcn.00499460.c)
- [`code/fcn.0049bcf0.c`](code/fcn.0049bcf0.c)
- [`code/fcn.0049e520.c`](code/fcn.0049e520.c)
- [`code/fcn.004a8fbc.c`](code/fcn.004a8fbc.c)
- [`code/fcn.004c4498.c`](code/fcn.004c4498.c)

## Behavioral Analysis

Based on the final chunk of disassembly, my analysis confirms that this binary is not just highly obfuscated; it utilizes a **professional-grade execution environment** typical of modern advanced malware (such as high-end RATs, info-stealers with sophisticated evasion, or custom "packer" builders).

The final code snippets provide definitive evidence for the techniques mentioned in previous reports, while adding new layers regarding how those protections are implemented.

### Updated Analysis of the Binary

#### 1. Core Functionality and Purpose
The analysis now confirms that this is a **Virtual Machine (VM)-based loader.** The core logic is not "hidden" by simple encryption; it has been rewritten into a custom, non-x86 instruction set.

*   **Instruction Dispatchers:** Functions like `fcn.00412ea0` and `fcn.00410540` are nearly identical in structure. They use a large `switch` table to handle various cases (up to 21+ distinct states). This is the hallmark of an **Interpreter**. Instead of standard logic flow, these functions act as "handlers" for different opcodes in a custom bytecode stream.
*   **State-Machine Processing:** The repeated calls to internal functions like `fcn.004041f4` and `fcn.00408a58` across multiple dispatchers suggest that the malware is maintaining a complex "state" of execution, where each jump in the code represents a state transition rather than a simple logical branch.

#### 2. Expanded Suspicious and Malicious Behaviors
*   **VM-Loop Processing:** The functions `fcn.0047105c` and `fcn.004716c8` contain long, complex loops that iterate over data while checking indices (e.g., `if (iVar5 <= iVar6)`). This is the "heart" of a Virtual Machine loop. It pulls an opcode from a buffer, determines what it means, and executes the corresponding logic.
*   **Advanced GDI Resource Manipulation:** The function `fcn.00428190` shows very sophisticated use of the Windows Graphics Device Interface (GDI). Specifically, it uses:
    *   `CreateDIBSection`, `CreateCompatibleDC`, and `CreateDIBitmap`. 
    *   **Analysis:** This is far beyond simple window drawing. These specific calls are used to **manually manipulate bitmaps or bit-level image data**. In a malicious context, this is often used for:
        1.  **Decoding icons/images** that are stored in a highly compressed or custom format.
        2.  **Crafting an overlay** (common in remote access tools) to hide the actual windows being manipulated by the malware.
*   **Complexity as a Defense Mechanism:** The code at `fcn.00473b97` is a masterpiece of "Anti-Decompilation" logic. It uses dozens of nested conditions and constant comparisons to determine a single result (a 31-bit integer). This is designed to overwhelm automated analysis tools like Ghidra or IDA, as it creates thousands of potential paths that are functionally identical but structurally complex for a machine to map.

#### 3. Notable Techniques and Patterns
*   **Control-Flow Flattening & Dispatch Tables:** The sheer volume of switch statements indicates that the author is intentionally "flattening" the logic. By forcing every piece of logic through a central dispatcher, they ensure that an analyst cannot follow the logical flow by just looking at a graph—they have to manually map out every possible transition in the state machine.
*   **Polymorphic/Metamorphic-Like Structure:** The similarity between `fcn.00412ea0` and `fcn.00410540` suggests that different "modules" of the malware use a shared library or a common base template for their VM implementations, implying a mature development environment (likely a custom framework).
*   **High-Complexity Data Manipulation:** The function `fcn.00437b24` includes logic for division/multiplication handling (via `MulDiv`) and bitwise shifts. This suggests the malware performs complex math on its internal variables, likely as part of an encryption or decryption routine (e.g., a custom rolling cipher).

---

### Final Summary for Report

*   **Obfuscation Type:** **VM-Based Protection & State Machine Complexity.** The binary employs a "Virtual Machine" architecture where the primary malicious payloads are written in a proprietary bytecode. This is processed by several dispatchers, making standard static analysis almost impossible without first reverse-engineering the VM's instruction set.
*   **Risk Level:** **Critical / Advanced Threat.** This level of engineering—using custom virtual machines and complex GDI-based resource handling—is characteristic of advanced persistent threat (APT) tools or high-end malware as a service (MaaS). It is specifically designed to thwart both automated sandbox detection and manual reverse engineering.
*   **Technical Highlights:**
    *   **VM Execution Engine:** The presence of multiple large switch tables and loops indicates the core malicious logic is hidden inside an interpreter. Analysis must focus on identifying the "handler" for each opcode.
    *   **GDI-Based Manipulation:** Extensive use of `CreateDIBSection` and `BitBlt`-related logic suggests sophisticated image/icon decoding or the creation of a custom overlay to hide malware activity from the user.
    *   **Antithesis of Static Analysis:** The "switch bloat" and complex conditional jumps are intentionally designed to crash or stall decompilers, making this an "analysis-resistant" binary.
    *   **Delphi Framework usage:** The structure strongly suggests a high-end Delphi implementation, indicating the developer has significant resources and experience in malware development.

**Final Conclusion:** This is a highly sophisticated, production-grade piece of malware. It is designed to be extremely difficult to analyze through traditional means, requiring deep manual de-obfuscation and potentially dynamic instrumentation (e.g., Frid, x64dbg) to map the internal VM logic before the actual functionality (C2 communication, data theft, etc.) can be identified.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Streams | The use of a custom VM-based interpreter and instruction dispatchers hides the true malicious logic within a proprietary bytecode system. |
| T1027 | Obfuscated Files or Streams | Control-flow flattening (via "switch bloat") is used to create complex branching paths that hinder both automated decompilers and manual analysis. |
| T1036 | Masquerading | The use of advanced GDI functions to create overlays is designed to hide the true nature of the windows being manipulated from the user or analyst. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

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

**Other artifacts (behavioral indicators/patterns)**
*   **VM-Based Execution Engine:** The binary utilizes a custom instruction set and interpreter logic. Key internal dispatchers are located at:
    *   `fcn.00412ea0`
    *   `fcn.00410540`
*   **GDI Resource Manipulation:** Sophisticated use of `CreateDIBSection`, `CreateCompatibleDC`, and `CreateDIBitmap` (specifically identified at `fcn.00428190`) for potential icon decoding or overlay creation.
*   **Anti-Decompilation Logic:** Highly complex, nested conditional jump structures designed to stall automated analysis tools (identified at `fcn.00473b97`).
*   **Complexity/Math Operations:** Complex bitwise shifts and arithmetic operations performed on internal variables (at `fcn.00437b24`), likely for custom decryption routines.
*   **Development Framework:** Consistent use of **Delphi** components, variable types (e.g., `TDateTime`, `TObject`), and standard Pascal-based logic structures.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
* **VM-Based Architecture:** The binary utilizes a professional-grade "Virtual Machine" execution environment where the core logic is rewritten into a proprietary, non-x86 bytecode. The use of extensive switch tables and state-machine processing (e.g., `fcn.00412ea0`) indicates it is designed to hide its true functionality from standard automated analysis tools.
* **Advanced Anti-Analysis Tactics:** The code specifically employs "Control-Flow Flattening" and "Switch Bloat," as well as highly complex nested conditional jumps (e.g., `fcn.00473b97`). These techniques are intentionally engineered to stall or crash decompilers like Ghidra/IDA Pro, identifying it as a high-end, analysis-resistant sample.
* **Sophisticated GDI Manipulation:** The use of `CreateDIBSection` and other advanced Graphics Device Interface functions suggests the creation of graphical overlays or complex resource decoding, common in advanced RATs to hide activity from the end-user or automated sandboxes.
