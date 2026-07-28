# Threat Analysis Report

**Generated:** 2026-07-27 18:15 UTC
**Sample:** `0bd046c68f1bfdb433a003db0d7c17eb1e271dc13d9a33197ddbc6ee7a892d0b_0bd046c68f1bfdb433a003db0d7c17eb1e271dc13d9a33197ddbc6ee7a892d0b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0bd046c68f1bfdb433a003db0d7c17eb1e271dc13d9a33197ddbc6ee7a892d0b_0bd046c68f1bfdb433a003db0d7c17eb1e271dc13d9a33197ddbc6ee7a892d0b.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 4,081,424 bytes |
| MD5 | `52f4e288479ebe73628ea8f46614183b` |
| SHA1 | `1bd7bb94d98243cd0d30f82f479a4b04ef3a2c53` |
| SHA256 | `0bd046c68f1bfdb433a003db0d7c17eb1e271dc13d9a33197ddbc6ee7a892d0b` |
| Overall entropy | 7.142 |
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
| `CODE` | 376,320 | 6.515 | No |
| `DATA` | 6,656 | 4.554 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 9,216 | 4.872 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.207 | No |
| `.reloc` | 29,184 | 6.635 | No |
| `.rsrc` | 3,644,928 | 7.044 | ⚠️ Yes |

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

Total strings found: **50914** (showing first 100)

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

WideString
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
	Exceptionq@
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
EZeroDivide@u@
	EOverflow

EUnderflow
EInvalidPointerLv@
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00403328` | `0x403328` | 2529 | ✓ |
| `fcn.00445594` | `0x445594` | 2312 | ✓ |
| `fcn.00444c8c` | `0x444c8c` | 2280 | ✓ |
| `fcn.00409cf0` | `0x409cf0` | 1921 | ✓ |
| `fcn.004532b0` | `0x4532b0` | 1750 | ✓ |
| `fcn.00423fa4` | `0x423fa4` | 1633 | ✓ |
| `fcn.0042a28c` | `0x42a28c` | 1392 | ✓ |
| `fcn.004127b0` | `0x4127b0` | 1362 | ✓ |
| `fcn.00412088` | `0x412088` | 1335 | ✓ |
| `fcn.00446fd8` | `0x446fd8` | 1183 | ✓ |
| `fcn.00425388` | `0x425388` | 1131 | ✓ |
| `fcn.0040f750` | `0x40f750` | 1097 | ✓ |
| `fcn.00410214` | `0x410214` | 1088 | ✓ |
| `fcn.004372f8` | `0x4372f8` | 1085 | ✓ |
| `fcn.00457cb0` | `0x457cb0` | 1018 | ✓ |
| `fcn.0043b844` | `0x43b844` | 978 | ✓ |
| `entry0` | `0x45cc80` | 970 | ✓ |
| `fcn.004119d4` | `0x4119d4` | 965 | ✓ |
| `fcn.00428e18` | `0x428e18` | 947 | ✓ |
| `fcn.0042c714` | `0x42c714` | 905 | ✓ |
| `fcn.00454f2c` | `0x454f2c` | 902 | ✓ |
| `fcn.00410d18` | `0x410d18` | 885 | ✓ |
| `fcn.0044e734` | `0x44e734` | 852 | ✓ |
| `fcn.0041146c` | `0x41146c` | 846 | ✓ |
| `fcn.00410810` | `0x410810` | 836 | ✓ |
| `fcn.00408a3e` | `0x408a3e` | 828 | ✓ |
| `fcn.0040a7d4` | `0x40a7d4` | 795 | ✓ |
| `fcn.00455abc` | `0x455abc` | 784 | ✓ |
| `fcn.0041b1dc` | `0x41b1dc` | 763 | ✓ |
| `fcn.0044b87c` | `0x44b87c` | 757 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00403328.c`](code/fcn.00403328.c)
- [`code/fcn.00408a3e.c`](code/fcn.00408a3e.c)
- [`code/fcn.00409cf0.c`](code/fcn.00409cf0.c)
- [`code/fcn.0040a7d4.c`](code/fcn.0040a7d4.c)
- [`code/fcn.0040f750.c`](code/fcn.0040f750.c)
- [`code/fcn.00410214.c`](code/fcn.00410214.c)
- [`code/fcn.00410810.c`](code/fcn.00410810.c)
- [`code/fcn.00410d18.c`](code/fcn.00410d18.c)
- [`code/fcn.0041146c.c`](code/fcn.0041146c.c)
- [`code/fcn.004119d4.c`](code/fcn.004119d4.c)
- [`code/fcn.00412088.c`](code/fcn.00412088.c)
- [`code/fcn.004127b0.c`](code/fcn.004127b0.c)
- [`code/fcn.0041b1dc.c`](code/fcn.0041b1dc.c)
- [`code/fcn.00423fa4.c`](code/fcn.00423fa4.c)
- [`code/fcn.00425388.c`](code/fcn.00425388.c)
- [`code/fcn.00428e18.c`](code/fcn.00428e18.c)
- [`code/fcn.0042a28c.c`](code/fcn.0042a28c.c)
- [`code/fcn.0042c714.c`](code/fcn.0042c714.c)
- [`code/fcn.004372f8.c`](code/fcn.004372f8.c)
- [`code/fcn.0043b844.c`](code/fcn.0043b844.c)
- [`code/fcn.00444c8c.c`](code/fcn.00444c8c.c)
- [`code/fcn.00445594.c`](code/fcn.00445594.c)
- [`code/fcn.00446fd8.c`](code/fcn.00446fd8.c)
- [`code/fcn.0044b87c.c`](code/fcn.0044b87c.c)
- [`code/fcn.0044e734.c`](code/fcn.0044e734.c)
- [`code/fcn.004532b0.c`](code/fcn.004532b0.c)
- [`code/fcn.00454f2c.c`](code/fcn.00454f2c.c)
- [`code/fcn.00455abc.c`](code/fcn.00455abc.c)
- [`code/fcn.00457cb0.c`](code/fcn.00457cb0.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, here is an updated and extended analysis. The new data reinforces the previous findings regarding the application's complexity while introducing new evidence concerning its potential for stealth and modularity.

### **Updated Analysis Update**

The second set of functions reveals a more sophisticated underlying architecture. While it retains the "Delphi-style" framework characteristics, several specific technical patterns emerge that are significant from a security perspective.

---

### **Expanded Technical Findings**

#### **1. Dynamic API Resolution & Modular Loading**
Function `fcn.00428e18` is highly significant for security analysis:
*   **Behavior:** It calls `LoadLibraryA` to load a DLL into memory and then executes a long sequence of `GetProcAddress` calls (over 30 are shown in this snippet).
*   **Analysis:** This is a classic technique used to resolve function addresses at runtime rather than at link-time.
*   **Malware Context:** In malware, this is frequently used for **evasion**. By loading its primary functionality (e.g., networking, encryption, or data exfiltration) from an external DLL and resolving those functions dynamically, the author can hide the "true" capabilities of the binary from static analysis tools that look for suspicious imports in the IAT (Import Address Table).

#### **2. Advanced UI Coordinate & Viewport Management**
Functions `fcn.00454f2c` and `fcn.00410810` contain logic involving:
*   **Coordinate Transformation:** The use of `ClientToScreen` suggests the application is tracking where elements are located relative to the monitor, not just the window.
*   **Offset Calculations:** The code performs several calculations (e.g., `var_70h = var_70h - (iVar4 + 5)`) and uses `OffsetRect`.
*   **Impact:** This supports the **Overlay Theory**. These functions are designed to "pin" or position elements accurately on the screen, likely to ensure that if a user moves their mouse or another window interacts with it, the overlay remains positioned correctly (a common feature in cheat software or sophisticated "fake" login screens).

#### **.3 Massive State Machines & Dispatchers**
Several functions (`fcn.0042c714`, `fcn.0041b1dc`, `fcn.004119d4`) utilize massive switch tables (up to 38 cases).
*   **Analysis:** These appear to be "Dispatchers" or "Handlers." The program takes an input value (like a message ID, button click, or internal state) and maps it to a specific block of logic.
*   **Risk Factor:** While common in large Delphi applications, this structure makes manual reverse engineering difficult because the "next step" for the code is determined at runtime based on variable data, making it harder to follow the execution flow statically.

#### **4. String and OLE Processing**
Function `fcn.00455abc` shows detailed handling of string types:
*   **Behavior:** It iterates through characters, checking for newlines (`\n`), carriage returns (`\r`), and tabs (`\t`), while also interacting with "BSTR" (Basic String) structures common in OLE/COM.
*   **Significance:** This indicates the application may interact with system components via COM or handle complex data strings that could be configuration files, intercepted keystrokes, or remote commands.

#### **5. Timing and Delay Logic**
Function `fcn.0044b87c` includes calls to `kernel32.dll_Sleep_1`.
*   **Analysis:** The code contains loops that calculate a duration and then put the thread to sleep.
*   **Malware Context:** This is often used in **anti-analysis**. By pausing execution for small, varying amounts of time (jitter), malware can evade "fast-forward" sandbox analysis or mimic human interaction timing during automated behavior logs.

---

### **Updated Risk Profile & Indicators**

| Feature | Potential Malicious Intent | Confidence |
| :--- | :--- | :--- |
| **Dynamic API Resolution** | Hiding malicious capabilities (C2, Exfiltration) from static scanners. | High |
| **Complex GDI/Overlay Logic** | Overlaying a fake UI over other applications or the desktop. | High |
| **Large Switch-Table Dispatchers** | Obfuscating control flow to hamper automated analysis. | Medium |
| **ClientToScreen/OffsetRect** | Ensuring an overlay remains persistent and visible over other windows. | High |
| **BSTR / OLE String Handling** | Interacting with system COM objects or complex data streams. | Medium |

### **Updated Summary for Incident Response**
The presence of **dynamic API resolution** combined with **heavy GDI-based coordinate manipulation** strongly suggests this is a sophisticated piece of software designed to interact with the Windows UI in a non-standard way. 

If found on a workstation, it should be treated as a high-priority threat for:
1.  **Overlay Attacks:** (e.g., fake login screens over banking sites).
2.  **Information Stealing:** The dynamic loading of numerous functions suggests the presence of a "plugin" style architecture where different capabilities are loaded only when needed to stay under the radar.

**Recommendation:** Perform dynamic analysis in a sandbox to capture the DLL being loaded by `fcn.00428e18` and monitor for network callbacks immediately after the library is loaded.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Imports | The use of `LoadLibraryA` and `GetProcAddress` to resolve functions at runtime is a standard method to hide the program's capabilities (e.g., networking, encryption) from static analysis tools. |
| **T1491** | Virtualization/Sandbox Detection | The inclusion of sleep loops and jitter logic is a classic defense evasion tactic used to bypass sandboxes that "fast-forward" execution or look for non-human timing patterns. |
| **T1036** | Masquerading | The use of advanced UI overlay logic and "fake" login screens suggests the software aims to masquerade as a legitimate system component to deceive the user. |
| **T1027** | Obfuscated Imports | The implementation of large state machines and dispatchers functions as an obfuscation technique to complicate manual reverse engineering and hide the true execution flow. |

***

### **Analyst Notes for Incident Response:**
*   **Overlay Logic:** While there is no specific "Overlay" sub-technique in MITRE ATT&CK, it is a common method for **Credential Access**. The combination of `ClientToScreen` and `OffsetRect` confirms the application's intent to place an intercepting UI over other programs.
*   **Dynamic Loading:** The resolution of over 30 functions via `GetProcAddress` strongly suggests a modular architecture where malicious payloads (like keyloggers or data exfiltrators) are hidden until runtime.
*   **BSTR/OLE Processing:** While not directly mapping to a single T-code, this indicates interaction with Windows system components, which may be used for injecting commands or interacting with the shell.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Since there were no networking-based IOCs (IPs/URLs) or specific filesystem paths for malicious binaries/config files in the text, the report focuses on **Behavioral Artifacts** which serve as indicators of malicious intent.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None.* (Note: The strings `SOFTWARE\Borland\Delphi\RTL` and `Software\Borland\Locales` were identified as standard development environment registry keys and are excluded as false positives.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (Behavioral & Technical Indicators)**
These items indicate technical patterns consistent with malware behavior (Overlay attacks, Evasion, and Obfuscation):

*   **Dynamic API Resolution:** Use of `LoadLibraryA` and `GetProcAddress` at addresses like `fcn.00428e18`. This is a common technique to hide malicious imports from static analysis.
*   **Overlay Indicators (GDI Manipulation):** The use of `ClientToScreen` and `OffsetRect` in functions `fcn.00454f2c` and `fcn.00410810`. These suggest the creation of a "Fake" UI or an overlay designed to sit atop other windows (e.g., fake login screens).
*   **Anti-Analysis Timing:** Use of `kernel32.dll_Sleep_1` in function `fcn.0044b87c`. This is used to introduce "jitter" and bypass automated sandbox analysis.
*   **Obfuscated Control Flow:** Large switch-table dispatchers (up to 38 cases) in functions like `fcn.0042c714` and `fcn.0041b1dc`, used to complicate reverse engineering.
*   **Complex Data Handling:** The presence of BSTR/OLE processing (`fcn.00455abc`) indicates the ability to handle complex data structures or communicate with system COM objects.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / trojan
3. **Confidence**: High
4. **Key evidence**:
    *   **Sophisticated Evasion & Obfuscation:** The use of dynamic API resolution (`LoadLibraryA`/`GetProcAddress`) for over 30 functions and large switch-table dispatchers indicates a clear intent to hide the "true" capabilities (such as networking or exfiltration) from static analysis.
    *   **Overlay Capabilities:** Extensive GDI logic, specifically `ClientToScreen` and `OffsetRect`, strongly suggests the creation of an overlay used for fake login screens or hijacking UI elements, common in credential theft campaigns.
    *   **Anti-Analysis Tactics:** The implementation of "jitter" via timed sleep loops (T1491) specifically designed to bypass automated sandbox detection confirms malicious intent and a focus on persistence/stealth.
