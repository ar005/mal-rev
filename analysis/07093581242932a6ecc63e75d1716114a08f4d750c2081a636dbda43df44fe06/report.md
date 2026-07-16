# Threat Analysis Report

**Generated:** 2026-07-15 18:48 UTC
**Sample:** `07093581242932a6ecc63e75d1716114a08f4d750c2081a636dbda43df44fe06_07093581242932a6ecc63e75d1716114a08f4d750c2081a636dbda43df44fe06.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07093581242932a6ecc63e75d1716114a08f4d750c2081a636dbda43df44fe06_07093581242932a6ecc63e75d1716114a08f4d750c2081a636dbda43df44fe06.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 3,801,360 bytes |
| MD5 | `3cc7de41c36c1fcfced3eb952f092056` |
| SHA1 | `cc91138af26230288b939710fd2bb344466497f1` |
| SHA256 | `07093581242932a6ecc63e75d1716114a08f4d750c2081a636dbda43df44fe06` |
| Overall entropy | 7.491 |
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
| `.rsrc` | 3,226,624 | 7.435 | ⚠️ Yes |

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

Total strings found: **12785** (showing first 100)

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

This updated analysis incorporates the findings from chunk 2, building upon the previously identified evidence of a complex Delphi-based application with significant indicators of evasive techniques and advanced functionality.

### Updated Analysis Summary

The additional disassembly confirms that this application is not a simple "wrapper" or basic utility; it contains sophisticated internal logic for state management, data processing, and potentially interacting with system components via COM/OLE interfaces. The complexity of the code suggests a highly developed software architecture, which is often used in both high-end commercial software and advanced malware to hide primary malicious routines behind layers of legitimate-looking "noise."

---

### Expanded Technical Analysis

#### 1. Logic Normalization & Obfuscation (`fcn.00431db4`)
The function `fcn.00431db4` contains a massive switch-case table (nearly 40 cases) designed to map a wide range of input values into a smaller, simplified range of integers.
*   **Observation:** Inputs like 2, 3, and 4 are all mapped to the value `1`; inputs 5, 6, and 7 to `2`. It also calculates a secondary offset (`(param_2 & 0xff) - iVar1 + 1`).
*   **Significance:** This is a technique used to **"flatten" or "normalize" data.** In the context of malware, this often hides the actual logic being executed. An analyst looking at high-level logs might see one consistent value (e.g., `1`), while the underlying code is actually handling many different commands or states. This masks the diversity of internal actions from automated analysis tools.

#### 2. Advanced String Processing and COM/OLE Interaction (`fcn.0045c82c`)
The function `fcn.0045c82c` exhibits highly complex logic involving string manipulation and what appears to be **COM (Component Object Model) or OLE (Object Linking and Embedding)** handling.
*   **Observation:** The code handles specific byte-level checks, identifies special characters (like `0x48`), manages a `bstrString` buffer, and interacts with memory segments in a way that suggests it is processing complex data structures rather than simple plain-text strings.
*   **Significance:** Interaction with OLE/COM is common in Delphi applications but is also a high-value target for malware. It can be used to interact with the Windows Shell, manipulate and host web content via Internet Explorer components (used in "droppers"), or communicate with other system services using established system protocols.

#### 3. Complex Command Dispatching (`fcn.00420320`)
This function serves as a secondary dispatcher. It compares internal values against specific constants to decide which sub-routine to execute.
*   **Observation:** Unlike a standard `if/else` chain, this uses a "jump table" style of execution where the result of one check immediately leads into another specialized function (e.g., `fcn.0041f210`, `fcn.00417dc4`).
*   **Significance:** This indicates a **modular state machine.** It allows the program to behave very differently depending on internal states that aren't immediately obvious from one single function call. In malware, this is used to create "multi-stage" payloads where different behaviors (e.g., keylogging vs. exfiltration) are activated only under specific conditions or timeframes.

---

### Updated Suspicious & Malicious Behaviors

*   **Dynamic API Resolution (Confirmed/High):** As previously noted, the heavy use of `GetProcAddress` remains a primary indicator of intent to hide functionality from static analysis.
*   **Obfuscation through Complexity (New High Significance):** The extensive use of switch-case "normalization" (`fcn.00431db4`) and jump-table dispatching (`fcn.00420320`) serves as a significant barrier to manual analysis. By collapsing multiple inputs into single logic paths, the author makes it harder for an analyst to map the full range of the program's capabilities without deep dynamic tracing.
*   **Potential System Component Interaction (New Medium Significance):** The inclusion of `bstrString` handling and OLE-like logic (`fcn.0045c82c`) suggests that the malware may have capabilities beyond simple UI—specifically, it might be designed to interact with Windows system components to perform more complex actions like file manipulation or network activity disguised as standard OS behavior.

---

### Conclusion
The addition of chunk 2 reinforces the conclusion that this is a sophisticated piece of software. The hallmark of its design is **complexity-based evasion**: it uses large, nested switch tables and dynamic API resolution to hide its true "mission." 

**Recommended Next Steps:**
1.  **Dynamic Analysis (Sandboxing):** Execute the sample in a controlled environment while monitoring for network traffic and process injection to see which specific functions called by `fcn.00420320` are triggered during different periods of time.
2.  **API Hooking:** Monitor calls related to COM/OLE objects (like `CoCreateInstance`) during execution to determine if it is attempting to interact with and manipulate system resources.
3.  **String Recovery:** Use a tool like Floss or manually extract all strings to see what the "normalized" values in `fcn.00431db4` actually refer to (e.g., specific commands, file paths, or URLs).

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the technical analysis to the relevant MITRE ATT&CK techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of "logic normalization" (switch-case tables) and Dynamic API Resolution (`GetProcAddress`) are specifically designed to hide the program's true capabilities and execution paths from static analysis. |
| **T1219** | System Services | Interaction with COM/OLE components allows the malware to leverage standard Windows system services to perform complex actions like shell manipulation or network activities while appearing as legitimate OS behavior. |

### Analyst Notes:
*   **Complexity-based Evasion:** The "Complex Command Dispatching" (`fcn.00420320`) and "Logic Normalization" (`fcn.00431db4`) are high-level forms of **T1027**. By collapsing multiple distinct inputs into single logical paths, the author forces an analyst to perform extensive dynamic tracing to understand the full scope of the malware's capabilities.
*   **System Integration:** The presence of `bstrString` handling and OLE logic suggests a move toward "living off the land" by using standard Windows APIs that are often overlooked by basic security filters, making it harder to distinguish malicious commands from legitimate system requests.

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs).

**Note:** Several elements found in the source text (such as `kernel32.dll`, Borland registry keys, and standard Delphi error codes) were identified as false positives or standard system components and have been excluded from this list.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Reported paths like `Software\Borland\...` are standard development environment keys).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Internal Function Offsets (Behavioral Markers):** The following offsets indicate complex logic, jump tables, and dispatching mechanisms often used to obfuscate the execution path in advanced malware:
    *   `fcn.00431db4` (Logic Normalization/Flattening)
    *   `fcn.0045c82c` (Complex String Processing & OLE/COM interaction)
    *   `fcn.00420320` (Multi-stage Command Dispatching)
*   **Detected Capabilities:** 
    *   **Dynamic API Resolution:** The presence of `GetProcAddress` usage to hide functionality from static analysis.
    *   **COM/OLE Interaction:** Use of `bstrString` and potential interaction with Windows system components via OLE.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: Medium

**Key evidence**:
*   **Sophisticated Obfuscation Techniques:** The use of "logic normalization" (collapsing multiple inputs into a single logic path) and dynamic API resolution (`GetProcAddress`) are high-level techniques used to hide the true functionality of the code from static analysis tools.
*   **Multi-Stage Command Dispatching:** The identification of a modular state machine in `fcn.00420320` suggests the application is designed to receive and execute various commands, which is characteristic of a loader or a backdoor acting as a "gatekeeper" for further malicious payloads.
*   **Advanced System Interaction:** The use of COM/OLE components and `bstrString` handling indicates that the malware is likely attempting to "live off the land" by utilizing standard Windows services to perform its tasks, making it harder for traditional security software to flag its activities as malicious.
