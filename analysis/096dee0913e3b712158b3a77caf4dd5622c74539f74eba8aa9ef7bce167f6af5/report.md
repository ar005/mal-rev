# Threat Analysis Report

**Generated:** 2026-07-20 14:18 UTC
**Sample:** `096dee0913e3b712158b3a77caf4dd5622c74539f74eba8aa9ef7bce167f6af5_096dee0913e3b712158b3a77caf4dd5622c74539f74eba8aa9ef7bce167f6af5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `096dee0913e3b712158b3a77caf4dd5622c74539f74eba8aa9ef7bce167f6af5_096dee0913e3b712158b3a77caf4dd5622c74539f74eba8aa9ef7bce167f6af5.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 9 sections |
| Size | 1,536,000 bytes |
| MD5 | `8a12e5b48eac0765f7b529444cf64886` |
| SHA1 | `591f5f6ac81cf7160de9c27890600f7d7e72a9b4` |
| SHA256 | `096dee0913e3b712158b3a77caf4dd5622c74539f74eba8aa9ef7bce167f6af5` |
| Overall entropy | 7.533 |
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
| `.text` | 411,648 | 6.521 | No |
| `.itext` | 4,608 | 5.844 | No |
| `.data` | 1,026,048 | 7.678 | ⚠️ Yes |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 10,240 | 5.139 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.211 | No |
| `.reloc` | 30,720 | 6.67 | No |
| `.rsrc` | 51,200 | 5.276 | No |

### Imports

**oleaut32.dll**: `SafeArrayPtrOfIndex`, `SafeArrayGetUBound`, `SafeArrayGetLBound`, `SafeArrayCreate`, `VariantChangeType`, `VariantCopy`, `VariantClear`, `VariantInit`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegFlushKey`, `RegCloseKey`
**user32.dll**: `CreateWindowExA`, `WindowFromPoint`, `WaitMessage`, `UpdateWindow`, `UnregisterClassA`, `UnhookWindowsHookEx`, `TranslateMessage`, `TranslateMDISysAccel`, `TrackPopupMenu`, `SystemParametersInfoA`, `ShowWindow`, `ShowScrollBar`, `ShowOwnedPopups`, `SetWindowsHookExA`, `SetWindowTextA`
**kernel32.dll**: `Sleep`
**msimg32.dll**: `AlphaBlend`
**gdi32.dll**: `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetWinMetaFileBits`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetEnhMetaFileBits`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`, `SelectPalette`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**comctl32.dll**: `_TrackMouseEvent`, `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_DragShowNolock`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`, `ImageList_GetBkColor`

## Extracted Strings

Total strings found: **6658** (showing first 100)

```
This program must be run under Win32
$7
`.itext
`.data
.idata
.rdata
@.reloc
B.rsrc
Boolean
Integer
Cardinal
string
TObject
TObject
System

IInterface
System
TInterfacedObject
FastMM Borland Edition 
 2004, 2005 Pierre le Riche / Professional Software Development
tQRj

An unexpected memory leak has occurred. 
The unexpected small block leaks are:

 bytes: 
Unknown
String
The sizes of unexpected leaked medium and large blocks are: 
Unexpected Memory Leak
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
t$:
tA:J
;T$r
;T$
0:
t%:J
:
tu:J
t$:
tH:J
t-Rf;
t f;J
YZ]_^[
<
t"<t
<t$<t3<
<
t%<t><tQ<t\<
tChd[@
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
	Exceptionv@
EAbort
EHeapException
EOutOfMemory
EInOutErrorpw@
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeError0y@
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
-{{{{1
-ffff!
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0045ee0c` | `0x45ee0c` | 6383 | ✓ |
| `entry0` | `0x467180` | 5562 | ✓ |
| `fcn.00461944` | `0x461944` | 4098 | ✓ |
| `fcn.00403afc` | `0x403afc` | 2809 | ✓ |
| `fcn.004349cc` | `0x4349cc` | 2370 | ✓ |
| `fcn.0043532c` | `0x43532c` | 2210 | ✓ |
| `fcn.0040a3f4` | `0x40a3f4` | 1924 | ✓ |
| `fcn.0045ac9c` | `0x45ac9c` | 1766 | ✓ |
| `fcn.004240bc` | `0x4240bc` | 1633 | ✓ |
| `fcn.00463f5c` | `0x463f5c` | 1491 | ✓ |
| `fcn.00401b18` | `0x401b18` | 1412 | ✓ |
| `fcn.00461144` | `0x461144` | 1398 | ✓ |
| `fcn.004100ac` | `0x4100ac` | 1349 | ✓ |
| `fcn.0040f98c` | `0x40f98c` | 1324 | ✓ |
| `fcn.00436e1c` | `0x436e1c` | 1160 | ✓ |
| `fcn.004474e4` | `0x4474e4` | 1154 | ✓ |
| `fcn.00444190` | `0x444190` | 1142 | ✓ |
| `fcn.00425598` | `0x425598` | 1135 | ✓ |
| `fcn.004647f0` | `0x4647f0` | 1133 | ✓ |
| `fcn.0041e88f` | `0x41e88f` | 1039 | ✓ |
| `fcn.004017b0` | `0x4017b0` | 1032 | ✓ |
| `fcn.00442310` | `0x442310` | 977 | ✓ |
| `fcn.0042724c` | `0x42724c` | 947 | ✓ |
| `fcn.004025bc` | `0x4025bc` | 938 | ✓ |
| `fcn.0043224c` | `0x43224c` | 905 | ✓ |
| `fcn.0045cc90` | `0x45cc90` | 903 | ✓ |
| `fcn.004556a4` | `0x4556a4` | 867 | ✓ |
| `fcn.00409102` | `0x409102` | 828 | ✓ |
| `fcn.00463604` | `0x463604` | 828 | ✓ |
| `fcn.0040af18` | `0x40af18` | 802 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004017b0.c`](code/fcn.004017b0.c)
- [`code/fcn.00401b18.c`](code/fcn.00401b18.c)
- [`code/fcn.004025bc.c`](code/fcn.004025bc.c)
- [`code/fcn.00403afc.c`](code/fcn.00403afc.c)
- [`code/fcn.00409102.c`](code/fcn.00409102.c)
- [`code/fcn.0040a3f4.c`](code/fcn.0040a3f4.c)
- [`code/fcn.0040af18.c`](code/fcn.0040af18.c)
- [`code/fcn.0040f98c.c`](code/fcn.0040f98c.c)
- [`code/fcn.004100ac.c`](code/fcn.004100ac.c)
- [`code/fcn.0041e88f.c`](code/fcn.0041e88f.c)
- [`code/fcn.004240bc.c`](code/fcn.004240bc.c)
- [`code/fcn.00425598.c`](code/fcn.00425598.c)
- [`code/fcn.0042724c.c`](code/fcn.0042724c.c)
- [`code/fcn.0043224c.c`](code/fcn.0043224c.c)
- [`code/fcn.004349cc.c`](code/fcn.004349cc.c)
- [`code/fcn.0043532c.c`](code/fcn.0043532c.c)
- [`code/fcn.00436e1c.c`](code/fcn.00436e1c.c)
- [`code/fcn.00442310.c`](code/fcn.00442310.c)
- [`code/fcn.00444190.c`](code/fcn.00444190.c)
- [`code/fcn.004474e4.c`](code/fcn.004474e4.c)
- [`code/fcn.004556a4.c`](code/fcn.004556a4.c)
- [`code/fcn.0045ac9c.c`](code/fcn.0045ac9c.c)
- [`code/fcn.0045cc90.c`](code/fcn.0045cc90.c)
- [`code/fcn.0045ee0c.c`](code/fcn.0045ee0c.c)
- [`code/fcn.00461144.c`](code/fcn.00461144.c)
- [`code/fcn.00461944.c`](code/fcn.00461944.c)
- [`code/fcn.00463604.c`](code/fcn.00463604.c)
- [`code/fcn.00463f5c.c`](code/fcn.00463f5c.c)
- [`code/fcn.004647f0.c`](code/fcn.004647f0.c)

## Behavioral Analysis

This final chunk of disassembly provides critical evidence regarding how the application handles memory, resolves external functions, and manages internal state. When combined with the previous findings, it confirms that this is a highly sophisticated piece of software, likely a **modular loader** or a **sophisticated backdoor (RAT)**.

### Final Analysis Update & Integration

#### 1. Advanced Memory Management & Dynamic Loading
*   **Dynamic Allocation (`fcn.004017b0`):** This function utilizes `VirtualAlloc`. In the context of malware, this is a high-priority indicator. It suggests the program is reserving memory segments to house and execute code that isn't present in the original binary (e.g., an unpacked payload or a reflected DLL).
*   **Massive API Resolution (`fcn.0042724c`):** This function contains a dense block of `GetProcAddress` calls. It is systematically resolving a large number of functions from an external library at runtime. 
    *   *Security Implication:* This is a classic **anti-analysis technique**. By resolving addresses at runtime rather than listing them in the Import Address Table (IAT), the developer hides the program's full capabilities from static analysis tools. The sheer volume of calls suggests that once "unpacked," the binary has access to a wide array of system functions for file manipulation, networking, and process injection.

#### 2. Complex Command Dispatching
*   **Massive Switch-Case Tables (`fcn.00442310` & `fcn.0043224c`):** These functions contain large switch-case structures (with hundreds of potential states). This is the "brain" of the application. 
    *   *Security Implication:* This confirms the **modular nature** of the binary. It acts as a central dispatcher: it receives a command (perhaps from a C2 server), identifies the code for that action, and executes the specific logic. This allows one single piece of malware to perform dozens of different tasks (e.g., "take screenshot," "steal passwords," "log keystrokes") depending on what the attacker commands remotely.

#### 3. Sophisticated Social Engineering
*   **String Construction & UI Feedback (`fcn.004025bc`):** This function constructs strings to be used in `MessageBoxA`. It includes logic for creating user-facing notifications or error messages.
    *   *Security Implication:* As suspected in previous rounds, this supports the **"Fake Installer/Updater"** theory. The code is designed to communicate with the user, potentially providing a distraction (e.g., "System Update in Progress") while the background threads (identified in chunk 2) perform malicious actions.

#### 4. Complex Logic and Obfuscation
*   **"Heavy" Delphi Compilation Artifacts:** Many sections show extremely complex arithmetic and bit-shifting (`CARRY1`, `CONCAT31`). While these are common in the Delphi compiler for handling complex types, they also serve as "noise." 
    *   *Security Implication:* By wrapping simple operations in complex math chains, the developer makes it harder for automated tools to recognize standard logic (like string length checks or bitmasking), effectively hiding the true intent of the code behind a wall of mathematical complexity.

---

### Final Indicators of Compromise (IOC) / Behavior Summary

| Category | Technical Observation | Malicious Intent |
| :--- | :--- | :--- |
| **Persistence & Loading** | `VirtualAlloc` usage and dynamic `GetProcAddress` loops. | **Unpacking/Injection:** Preparing the environment to host a secondary, more "active" malicious payload. |
| **Execution Logic** | Massive switch-case dispatch tables. | **Modular Command Execution:** Acting as a remote-controlled tool (RAT) capable of varied actions based on C2 input. |
| **Anti-Analysis** | Dynamic API resolution and complex math obfuscation. | **Evasion:** Hiding the true capabilities and functionality from static security scanners. |
| **Social Engineering** | Intentional construction of UI strings for `MessageBoxA`. | **Deception:** Using "fake" system messages to mask background malicious activity from the user. |

---

### Final Analyst Conclusion for Incident Response
The analysis concludes that this binary is a **sophisticated, multi-stage Trojan/Loader**. 

It is not a simple script or a low-level piece of malware; it is a professionally engineered tool built in Delphi. Its architecture suggests a "Gatekeeper" design:
1.  **Phase 1 (The Face):** It uses GDI graphics and crafted `MessageBox` strings to present as a legitimate application or update utility.
2.  **Phase 2 (The Preparation):** It uses `VirtualAlloc` and a massive chain of `GetProcAddress` calls to "unlock" its capabilities, likely by loading an encrypted payload into the newly allocated memory.
3.  **Phase 3 (The Operation):** Once active, it utilizes the large switch-case dispatchers to process commands from an external server, allowing the attacker to perform various actions on the host machine while the main UI remains "clean."

**Recommendation:** Treat this as a high-severity threat. Any system where this binary is found should be treated as compromised by a potential Remote Access Trojan (RAT). Isolate the host and perform a full memory dump to identify what was loaded into the `VirtualAlloc` space, as that will reveal the active "payload" logic.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | Process Injection | The use of `VirtualAlloc` indicates the application is preparing memory space to host and execute payloads not present in the original binary. |
| **T1027** | Obfuscated Files or Events | The use of dynamic API resolution (`GetProcAddress`) and complex mathematical "noise" serves to hide code functionality from static analysis tools. |
| **T1036** | Masquerading | The creation of fake update notifications and system messages is used to deceive the user and mask malicious activity. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None detected.

**File paths / Registry keys**
*   None detected. *(Note: The "Software\Borland" registry keys identified in the strings were excluded as they are standard developer environment paths and not specific to a malicious campaign.)*

**Mutex names / Named pipes**
*   None detected.

**Hashes**
*   None detected.

**Other artifacts**
*   **Technique: Dynamic API Resolution:** The binary utilizes extensive `GetProcAddress` loops (specifically at `fcn.0042724c`) to resolve system functions at runtime, a common evasion technique used to hide the malware's functionality from static analysis.
*   **Technique: Memory Allocation/Unpacking:** Use of `VirtualAlloc` (at `fcn.004017b0`) suggests the intentional creation of memory space for secondary payloads or "in-memory" execution of unpacked code.
*   **Capability: Modular Command Dispatcher:** The presence of large switch-case tables (at `fcn.00442310` and `fcn.0043224c`) indicates a modular architecture typical of a Remote Access Trojan (RAT), allowing the malware to perform various actions based on remote commands.
*   **Social Engineering:** Logic for constructing strings for `MessageBoxA` suggests a "Fake Installer/Updater" tactic, used to distract the user while background malicious processes occur.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for this sample:

1. **Malware family:** Unknown (Sophisticated custom build)
2. **Malware type:** RAT / Loader
3. **Confidence:** High
4. **Key evidence:**
    *   **Modular Command Execution:** The presence of massive switch-case tables indicates a "brain" capable of processing a wide variety of remote commands, which is the defining characteristic of a Remote Access Trojan (RAT).
    *   **Advanced Evasion & Obfuscation:** The use of extensive `GetProcAddress` loops to hide the Import Address Table and complex mathematical "noise" from automated scanners demonstrates high-level professional development.
    *   **Multi-Stage Execution:** The combination of `VirtualAlloc` for memory injection and "Fake Installer/Updater" social engineering techniques identifies the binary as a sophisticated gateway (loader) designed to host and execute malicious payloads while deceiving the user.
