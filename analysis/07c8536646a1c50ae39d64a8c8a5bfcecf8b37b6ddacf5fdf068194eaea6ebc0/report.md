# Threat Analysis Report

**Generated:** 2026-07-17 19:48 UTC
**Sample:** `07c8536646a1c50ae39d64a8c8a5bfcecf8b37b6ddacf5fdf068194eaea6ebc0_07c8536646a1c50ae39d64a8c8a5bfcecf8b37b6ddacf5fdf068194eaea6ebc0.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07c8536646a1c50ae39d64a8c8a5bfcecf8b37b6ddacf5fdf068194eaea6ebc0_07c8536646a1c50ae39d64a8c8a5bfcecf8b37b6ddacf5fdf068194eaea6ebc0.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 5,641,216 bytes |
| MD5 | `b5047ade94c913e3e456feea0f23d2b4` |
| SHA1 | `0c1913ec3628abc62faa6b88df1d343046a3e27a` |
| SHA256 | `07c8536646a1c50ae39d64a8c8a5bfcecf8b37b6ddacf5fdf068194eaea6ebc0` |
| Overall entropy | 5.885 |
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
| `CODE` | 481,280 | 6.56 | No |
| `DATA` | 9,728 | 4.544 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 9,216 | 4.877 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.201 | No |
| `.reloc` | 39,424 | 6.604 | No |
| `.rsrc` | 5,100,032 | 5.622 | No |

### Imports

**kernel32.dll**: `Sleep`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WinHelpA`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `ShowCursor`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `GetErrorInfo`, `SysFreeString`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**gdi32.dll**: `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`, `SelectPalette`, `SelectObject`, `SelectClipRgn`
**ole32.dll**: `CoUninitialize`, `CoInitialize`
**comctl32.dll**: `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_SetDragCursorImage`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`

## Extracted Strings

Total strings found: **7786** (showing first 100)

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
EInOutErrorX}@
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeError
EIntOverflow

EMathError

EInvalidOp
EZeroDivide|
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
| `fcn.00447ccc` | `0x447ccc` | 2312 | ✓ |
| `fcn.004473c4` | `0x4473c4` | 2280 | ✓ |
| `entry0` | `0x47678c` | 2242 | ✓ |
| `fcn.0040ad58` | `0x40ad58` | 1921 | ✓ |
| `fcn.004559e8` | `0x4559e8` | 1750 | ✓ |
| `fcn.00428034` | `0x428034` | 1633 | ✓ |
| `fcn.00413e7c` | `0x413e7c` | 1362 | ✓ |
| `fcn.00413754` | `0x413754` | 1335 | ✓ |
| `fcn.00449710` | `0x449710` | 1183 | ✓ |
| `fcn.00429418` | `0x429418` | 1131 | ✓ |
| `fcn.00410df4` | `0x410df4` | 1097 | ✓ |
| `fcn.004118b8` | `0x4118b8` | 1088 | ✓ |
| `fcn.00439b08` | `0x439b08` | 1085 | ✓ |
| `fcn.00414fd0` | `0x414fd0` | 1053 | ✓ |
| `fcn.0045ad40` | `0x45ad40` | 1018 | ✓ |
| `fcn.0043e0c4` | `0x43e0c4` | 978 | ✓ |
| `fcn.004130a0` | `0x4130a0` | 965 | ✓ |
| `fcn.0042cefc` | `0x42cefc` | 947 | ✓ |
| `fcn.0042f0c8` | `0x42f0c8` | 905 | ✓ |
| `fcn.00457664` | `0x457664` | 902 | ✓ |
| `fcn.004123c8` | `0x4123c8` | 885 | ✓ |
| `fcn.00450e6c` | `0x450e6c` | 852 | ✓ |
| `fcn.00412b38` | `0x412b38` | 846 | ✓ |
| `fcn.00411eb4` | `0x411eb4` | 836 | ✓ |
| `fcn.00416018` | `0x416018` | 834 | ✓ |
| `fcn.004094e2` | `0x4094e2` | 828 | ✓ |
| `fcn.0040b83c` | `0x40b83c` | 795 | ✓ |
| `fcn.004581f4` | `0x4581f4` | 784 | ✓ |
| `fcn.004207b8` | `0x4207b8` | 763 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00403ab4.c`](code/fcn.00403ab4.c)
- [`code/fcn.004094e2.c`](code/fcn.004094e2.c)
- [`code/fcn.0040ad58.c`](code/fcn.0040ad58.c)
- [`code/fcn.0040b83c.c`](code/fcn.0040b83c.c)
- [`code/fcn.00410df4.c`](code/fcn.00410df4.c)
- [`code/fcn.004118b8.c`](code/fcn.004118b8.c)
- [`code/fcn.00411eb4.c`](code/fcn.00411eb4.c)
- [`code/fcn.004123c8.c`](code/fcn.004123c8.c)
- [`code/fcn.00412b38.c`](code/fcn.00412b38.c)
- [`code/fcn.004130a0.c`](code/fcn.004130a0.c)
- [`code/fcn.00413754.c`](code/fcn.00413754.c)
- [`code/fcn.00413e7c.c`](code/fcn.00413e7c.c)
- [`code/fcn.00414fd0.c`](code/fcn.00414fd0.c)
- [`code/fcn.00416018.c`](code/fcn.00416018.c)
- [`code/fcn.004207b8.c`](code/fcn.004207b8.c)
- [`code/fcn.00428034.c`](code/fcn.00428034.c)
- [`code/fcn.00429418.c`](code/fcn.00429418.c)
- [`code/fcn.0042cefc.c`](code/fcn.0042cefc.c)
- [`code/fcn.0042f0c8.c`](code/fcn.0042f0c8.c)
- [`code/fcn.00439b08.c`](code/fcn.00439b08.c)
- [`code/fcn.0043e0c4.c`](code/fcn.0043e0c4.c)
- [`code/fcn.004473c4.c`](code/fcn.004473c4.c)
- [`code/fcn.00447ccc.c`](code/fcn.00447ccc.c)
- [`code/fcn.00449710.c`](code/fcn.00449710.c)
- [`code/fcn.00450e6c.c`](code/fcn.00450e6c.c)
- [`code/fcn.004559e8.c`](code/fcn.004559e8.c)
- [`code/fcn.00457664.c`](code/fcn.00457664.c)
- [`code/fcn.004581f4.c`](code/fcn.004581f4.c)
- [`code/fcn.0045ad40.c`](code/fcn.0045ad40.c)

## Behavioral Analysis

This updated analysis incorporates the second chunk of disassembly. The new data provides significant evidence supporting the initial theories regarding **sophisticated anti-analysis techniques**, **dynamic API resolution**, and a **"Virtual Machine" (VM) or complex state machine** architecture common in high-end malware loaders and packers.

---

### **Updated Analysis Summary**

The addition of Chunk 2 reinforces the conclusion that this binary is not a standard application but a highly engineered piece of software—likely a **malware loader/dropper** or an **advanced crypter**. The code demonstrates significant efforts to hide its true capabilities from static analysis by using several advanced techniques:
1.  **Dynamic API Resolution:** Importing functions at runtime rather than in the Import Address Table (IAT).
2.  **Command Dispatching:** Using massive switch-case tables to route logic, characteristic of a "VM" architecture.
3.  **Complex Data Handling:** Extensive use of Delphi/Pascal `Variant` types and COM objects (`oleaut32`).
4.  **Overlay Logic:** Geometric calculations for UI manipulation or "ghosting."

---

### **Newly Identified Malicious Behaviors & Techniques**

#### **1. Dynamic API Resolution (High-Confidence Indicator)**
In function `fcn.0042cefc`, there is a clear and extensive block of code calling `GetProcAddress` in a tight sequence:
*   **Observation:** The code calls `LoadLibraryA(0x42d2c0)` followed by nearly 30 consecutive `GetProcAddress` calls (e.g., `0x42d300`, `0x42d310`, `0x42d330`).
*   **Malicious Context:** This is a classic **anti-analysis technique**. By resolving functions at runtime, the malware hides its true capabilities from basic static analysis tools (like `strings` or standard header extractors). It is likely populating an internal table of "hidden" functions to be used later for network communication, file manipulation, or process injection.

#### **2. Advanced Dispatcher Logic (State Machine/VM)**
Several functions (`fcn.0045ad40`, `fcn.0042f0c8`, `fcn.004207b8`) contain massive switch-case tables.
*   **Observation:** `fcn.0045ad40` contains a 63-case switch table where multiple adjacent cases point to the same handler (`fcn.00406764`). Similarly, `fcn.0042f0c8` handles over 60 possible states/inputs.
*   **Malicious Context:** This is indicative of a **Virtual Machine (VM) or Command Dispatcher**. Instead of the code following a linear path (which is easy for analysts to trace), it interprets "opcodes" from an internal buffer. The actual logic only becomes visible at runtime as the program processes its own internally-generated instruction set.

#### **3. Graphics & Overlay Geometry Logic**
Function `fcn.0043e0c4` contains complex calculations involving:
*   **Logic:** Iterating through objects, checking for empty rectangles (`IsRectEmpty`), and calculating offsets/subtractions (e.g., `var_18h = in_EAX[0x13] - (var_51h - var_59h)`).
*   **Malicious Context:** This logic is consistent with **Overlay behavior**. It suggests the software is calculating how to "overlap" its own windows or elements over other active applications. This is frequently used in:
    *   Creating fake error messages (to steal credentials).
    *   Injecting overlays onto web browsers/game clients.
    *   Hiding malicious activity behind a legitimate-looking UI window.

#### **4. Heavy Use of "Variant" and COM Handling**
The functions `fcn.00414fd0` and `fcn.00457664` interact heavily with `oleaut32` (the core library for handling Variants).
*   **Observation:** The code performs repeated checks on types and uses `VariantInit`.
*   **Technical Analysis:** This confirms the use of a high-level language like **Delphi**. In malware, this is often used to create "multi-tool" payloads. By using the Variant type, the author can pass different data types (strings, integers, pointers) through the same logic gates, making the disassembly harder for an analyst to follow as it tries to determine what data type is currently being processed.

---

### **Refined Technical Summary**

| Feature | Evidence Location(s) | Significance |
| :--- | :--- | :--- |
| **Dynamic API Resolution** | `fcn.0042cefc` | **High.** Bypasses static analysis of the IAT; indicates a sophisticated loader or packer. |
| **Command Dispatcher** | `fcn.0045ad40`, `fcn.0042f0c8` | **High.** Implements a "Virtual Machine" to hide actual logic flow from analysts. |
| **Overlay Support** | `fcn.0043e0c4` | **Medium-High.** Suggests interaction with other windows, likely for UI deception/overlay. |
| **Delphi Framework Usage** | `fcn.00414fd0`, `fcn.00457664` | **Low (Profiling).** Identifies the author's toolkit; suggests a professional-grade malware development environment. |

---

### **Updated Recommendations for Investigation**

1.  **Dynamic Analysis (Hooking):** Monitor the results of the `GetProcAddress` calls in `fcn.0042cefc`. By hooking this call, you can identify exactly which functions are being resolved (e.g., is it resolving `InternetOpen`, `WriteProcessMemory`, or `CreateRemoteThread`?).
2.  **Memory Forensics:** Since the code uses a dispatcher/VM approach, static analysis of the "dispatch" function won't reveal what it *actually does* until the "opcodes" are loaded into memory. Perform a memory dump at several points during execution to find the de-obfuscated instruction buffer.
3.  **Graphic Hooking:** Monitor `gdi32.dll` calls. Specifically, look for calls that calculate coordinates near other windows (like Chrome/Edge or login prompts) to confirm if it is creating a malicious overlay.
4.  **String Decryption:** Many of the "Variant" handling functions likely deal with decrypted strings. Watch for memory regions where `oleaut32` operations are occurring; these areas will often contain the decrypted C2 addresses and configuration data.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the corresponding MITRE ATT&CK techniques. 

Because several of these behaviors are methods used specifically to hinder reverse engineering and hide functionality from security tools, they fall under the primary "Obfuscated Files or Information" category, while the UI manipulation falls under "Masquerading."

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | Obfuscated Files or Information | The use of `GetProcAddress` to resolve functions at runtime hides the malware's true capabilities from static analysis tools. |
| **T1055** | Obfuscated Files or Information | The "Virtual Machine" (VM) and complex state machine architecture are used to hide the execution logic behind a proprietary instruction set. |
| **T1036** | Masquerading | The overlay geometry calculations are used to mask malicious activity by layering windows over legitimate applications or creating fake UI elements. |
| **T1055** | Obfuscated Files or Information | The heavy use of `Variant` types and complex COM handling is utilized to complicate the analysis of data flow and type-checking logic. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Per your instructions, standard system paths (e.g., `kernel32.dll`), common library strings (e.g., Delphi/Borland internal labels), and generic software installation paths were excluded as false positives.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The registry paths found, such as `Software\Borland\Delphi`, are standard compiler artifacts and do not constitute specific malicious indicators.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (Technical Indicators & Behaviors)**
The following represent behavioral IOCs derived from the disassembly analysis:

*   **Dynamic API Resolution:** 
    *   Location: `0x0042cefc`
    *   Detail: A sequence of ~30 `GetProcAddress` calls used to resolve and hide functionality (e.g., network or process injection) from static analysis.
*   **Command Dispatcher / VM Architecture:** 
    *   Locations: `0x0045ad40`, `0x0042f0c8`, `0x004207b8`
    *   Detail: Large switch-case tables (up to 63 cases) indicating a "Virtual Machine" or custom command dispatcher used to obfuscate the execution flow.
*   **Overlay Geometry Logic:** 
    *   Location: `0x0043e0c4`
    *   Detail: Complex calculations for overlapping windows, typically indicative of UI manipulation, fake error messages, or "ghosting" over other applications.
*   **Sophisticated Data Handling (Delphi/Oleaut32):** 
    *   Locations: `0x00414fd0`, `0x00457664`
    *   Detail: Extensive use of Variant types and COM objects to facilitate multi-type data passing, complicating manual analysis.

---

## Malware Family Classification

Based on the provided technical analysis, here is the classification:

1.  **Malware family:** custom (Advanced Loader)
2.  **Malware type:** loader / dropper
3.  **Confidence:** High
4.  **Key evidence:** 
    *   **VM/Command Dispatcher Architecture:** The presence of large switch-case tables used to interpret an internal instruction set (Virtual Machine architecture) is a hallmark of sophisticated, multi-stage loaders designed to hide core malicious logic from automated and manual analysis.
    *   **Evasive API Resolution:** The extensive use of `GetProcAddress` for dynamic resolution indicates a deliberate attempt to bypass static analysis tools and hide the "true" capabilities (such as networking or process injection) of the binary.
    *   **Overlay & UI Manipulation:** The inclusion of complex geometric calculations for window overlays suggests functionality used to deceive users (e.g., fake login prompts) or mask malicious behavior by overlaying windows over legitimate applications.
