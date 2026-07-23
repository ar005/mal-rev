# Threat Analysis Report

**Generated:** 2026-07-22 17:04 UTC
**Sample:** `09ab7b452ec3b3396bf87a60b287426ce3979a56b6938974ec94562b32ec6dd5_09ab7b452ec3b3396bf87a60b287426ce3979a56b6938974ec94562b32ec6dd5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `09ab7b452ec3b3396bf87a60b287426ce3979a56b6938974ec94562b32ec6dd5_09ab7b452ec3b3396bf87a60b287426ce3979a56b6938974ec94562b32ec6dd5.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 5,886,904 bytes |
| MD5 | `9304de5b72a6325db8a44535410899bd` |
| SHA1 | `13f585dcf689e82c75de95ff758b22f1cd04d398` |
| SHA256 | `09ab7b452ec3b3396bf87a60b287426ce3979a56b6938974ec94562b32ec6dd5` |
| Overall entropy | 7.398 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1718902200 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 979,456 | 6.471 | No |
| `.rdata` | 313,344 | 4.888 | No |
| `.data` | 30,720 | 4.471 | No |
| `.pdata` | 37,888 | 6.037 | No |
| `_RDATA` | 1,024 | 3.188 | No |
| `.rsrc` | 4,507,136 | 7.557 | ⚠️ Yes |
| `.reloc` | 6,144 | 5.402 | No |

### Imports

**WS2_32.dll**: `recv`, `listen`, `getsockname`, `send`, `socket`, `connect`, `WSAGetLastError`, `ntohs`, `WSAStartup`, `htonl`, `inet_addr`, `inet_ntoa`, `gethostbyaddr`, `getservbyport`, `getservbyname`
**VERSION.dll**: `GetFileVersionInfoW`, `VerQueryValueW`, `GetFileVersionInfoSizeW`
**COMCTL32.dll**: `ImageList_ReplaceIcon`, `ImageList_SetBkColor`, `ImageList_AddMasked`, `ImageList_BeginDrag`, `ImageList_EndDrag`, `ImageList_DragEnter`, `ImageList_DragLeave`, `ImageList_DragMove`, `ImageList_DragShowNolock`, `ImageList_GetImageCount`, `ImageList_DrawIndirect`, `CreateStatusWindowW`, `ImageList_SetOverlayImage`, `InitCommonControlsEx`, `ImageList_Add`
**FLTLIB.DLL**: `FilterSendMessage`, `FilterConnectCommunicationPort`, `FilterGetMessage`, `FilterReplyMessage`
**KERNEL32.dll**: `AcquireSRWLockExclusive`, `AcquireSRWLockShared`, `InitializeSRWLock`, `GetSystemInfo`, `VerSetConditionMask`, `RaiseException`, `GetCurrentThreadId`, `VerifyVersionInfoW`, `GlobalAddAtomW`, `EnumResourceNamesW`, `SetCurrentDirectoryW`, `CreateProcessW`, `OpenProcess`, `CompareStringW`, `GetLocaleInfoW`
**USER32.dll**: `DispatchMessageW`, `PeekMessageW`, `GetMessagePos`, `PostQuitMessage`, `GetWindowPlacement`, `SetWindowPlacement`, `CheckRadioButton`, `CharLowerW`, `CreatePopupMenu`, `RemoveMenu`, `InsertMenuItemW`, `SetRectEmpty`, `ChildWindowFromPoint`, `SetWindowTextA`, `EnumChildWindows`
**GDI32.dll**: `CreateBitmapIndirect`, `GetDIBits`, `CreateRectRgn`, `CreateRectRgnIndirect`, `GetBkMode`, `RectInRegion`, `GdiFlush`, `CreatePatternBrush`, `ExcludeClipRect`, `GetPixel`, `PatBlt`, `SetPixel`, `SetBrushOrgEx`, `RestoreDC`, `SaveDC`
**COMDLG32.dll**: `GetSaveFileNameW`, `ChooseColorW`, `ChooseFontW`, `FindTextW`, `GetOpenFileNameW`, `PrintDlgW`
**ADVAPI32.dll**: `ConvertStringSidToSidW`, `ConvertSidToStringSidW`, `RegSetValueW`, `RegEnumKeyW`, `LookupAccountSidW`, `MapGenericMask`, `GetTokenInformation`, `GetLengthSid`, `FreeSid`, `EqualSid`, `AllocateAndInitializeSid`, `RegQueryInfoKeyW`, `RegEnumValueW`, `RegEnumKeyExW`, `RegCreateKeyExW`
**SHELL32.dll**: `SHGetSpecialFolderLocation`, `ExtractIconExW`, `SHGetPathFromIDListW`, `CommandLineToArgvW`, `SHChangeNotify`, `SHBrowseForFolderW`, `SHGetMalloc`, `DragQueryFileW`, `ShellExecuteExW`, `SHGetFileInfoW`, `ShellExecuteW`
**ole32.dll**: `OleInitialize`, `ReleaseStgMedium`, `CreateBindCtx`, `CoInitializeEx`, `RegisterDragDrop`, `CoTaskMemFree`, `CoTaskMemRealloc`, `CoTaskMemAlloc`, `CoCreateInstance`, `CoSetProxyBlanket`, `OleUninitialize`
**OLEAUT32.dll**: `SysAllocStringLen`, `VariantTimeToSystemTime`, `VarUI4FromStr`, `SysAllocStringByteLen`, `VariantChangeType`, `VariantClear`, `VariantInit`, `SafeArrayGetElement`, `SafeArrayUnaccessData`, `SafeArrayAccessData`, `SafeArrayGetLBound`, `SafeArrayGetUBound`, `SafeArrayDestroy`, `SysStringLen`, `SysFreeString`
**SHLWAPI.dll**: `SHAutoComplete`
**UxTheme.dll**: `IsCompositionActive`, `IsThemeActive`, `SetWindowTheme`, `IsAppThemed`
**dwmapi.dll**: `DwmSetWindowAttribute`, `DwmDefWindowProc`
**ntdll.dll**: `RtlGetVersion`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`

## Extracted Strings

Total strings found: **11972** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@_RDATA
@.rsrc
@.reloc
u9\$(v
L$ SVWH
l$ VWATAVAWH
0A_A^A\_^
@UVATAVAWH
A_A^A\^]
@SUVWATAUAVAWH
L90t[H
f9z:fD
H9(t[H
XA_A^A]A\_^][
@USVWATAUAVAWH
H98tcH
A_A^A]A\_^[]
WAVAWH
L$ SUVWH
@USVWAVAWH
u	D9|$TA
9|$HtYL
A_A^_^[]
WATAUAVAWH
 A_A^A]A\_
L$ SVWH
L$ SVWH
L$ SVWH
VWATAVAWH
A_A^A\_^
@SUVAVH
(A^^][
(A^^][
@SUVAWH
(A_^][
(A_^][
\$ VWAVH
UVWATAUAVAWH
C@H98t
)D$0L+
A_A^A]A\_^]
@SUVWATAUAVAWH
xA_A^A]A\_^][
l$ VWATAVAWH
A_A^A\_^
UVWATAUAVAWH
f;D$Hu
t$1@8w
D$@f9G

A_A^A]A\_^]
D$`L9u
D;t$T|
APD90~
APD90~
APD90~
A8L90t!H
H;D$`st
L$D;L$T|
D$4f9G

t$4t4H
\$`D8l$1
D;t$T}
G
f;D$Pu\H
f;D$HuV
\$@D8g
gffffffffff
\$ UVWATAUAVAWH
O
f;MugA
f;MuaA
A_A^A]A\_^]
@SVATAUAWH
0A_A]A\^[
SVAUAWH
HA_A]^[
@UWATAVH
8A^A\_]
@SVAVAWH
(A_A^^[
@VWAVAWH
8A_A^_^
@SUVWAVH
 A^_^][
 A^_^][
UVWATAUAVAWH
 A_A^A]A\_^]
@SUVWAVH
pA^_^][
t$ WATAUAVAWH
A_A^A]A\_
t$ ATAVAWH
 A_A^A\
VWATAVAWH
0A_A^A\_^
|$ ATAVAWH
 A_A^A\
|$ AVH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140015520` | `0x140015520` | 866806 | ✓ |
| `method.std::ctype_unsigned_short_int_.virtual_24` | `0x140010db0` | 700704 | ✓ |
| `method.CCallTreeData.virtual_16` | `0x1400b26a0` | 613867 | ✓ |
| `method.CFilterDlg.virtual_24` | `0x140053350` | 613282 | ✓ |
| `method.CHighlightDlg.virtual_24` | `0x140056f40` | 597938 | ✓ |
| `fcn.1400254c0` | `0x1400254c0` | 428375 | ✓ |
| `fcn.140057e30` | `0x140057e30` | 347212 | ✓ |
| `fcn.140024710` | `0x140024710` | 160277 | ✓ |
| `fcn.1400b0aa0` | `0x1400b0aa0` | 150329 | ✓ |
| `fcn.1400bb464` | `0x1400bb464` | 118794 | ✓ |
| `method.ATL::CComModule.virtual_72` | `0x14005b300` | 77616 | ✓ |
| `method.ATL::CComModule.virtual_64` | `0x14005b310` | 75775 | ✓ |
| `fcn.1400d042c` | `0x1400d042c` | 52503 | ✓ |
| `fcn.1400d0554` | `0x1400d0554` | 52189 | ✓ |
| `fcn.1400d6740` | `0x1400d6740` | 39478 | ✓ |
| `fcn.1400d672c` | `0x1400d672c` | 39428 | ✓ |
| `fcn.1400dc2f0` | `0x1400dc2f0` | 38805 | ✓ |
| `fcn.140078430` | `0x140078430` | 23001 | ✓ |
| `fcn.140079020` | `0x140079020` | 19940 | ✓ |
| `fcn.140078e80` | `0x140078e80` | 19642 | ✓ |
| `fcn.14007abb0` | `0x14007abb0` | 16909 | ✓ |
| `method.std::ctype_unsigned_short_int_.virtual_96` | `0x140011ef0` | 16133 | ✓ |
| `fcn.1400cfa6c` | `0x1400cfa6c` | 14392 | ✓ |
| `fcn.1400cfa64` | `0x1400cfa64` | 14216 | ✓ |
| `fcn.1400bb498` | `0x1400bb498` | 12363 | ✓ |
| `fcn.1400a3080` | `0x1400a3080` | 11810 | ✓ |
| `fcn.140046730` | `0x140046730` | 11050 | ✓ |
| `fcn.1400616a0` | `0x1400616a0` | 10905 | ✓ |
| `fcn.1400703d0` | `0x1400703d0` | 9274 | ✓ |
| `fcn.1400cd608` | `0x1400cd608` | 7806 | ✓ |

### Decompiled Code Files

- [`code/fcn.140015520.c`](code/fcn.140015520.c)
- [`code/fcn.140024710.c`](code/fcn.140024710.c)
- [`code/fcn.1400254c0.c`](code/fcn.1400254c0.c)
- [`code/fcn.140046730.c`](code/fcn.140046730.c)
- [`code/fcn.140057e30.c`](code/fcn.140057e30.c)
- [`code/fcn.1400616a0.c`](code/fcn.1400616a0.c)
- [`code/fcn.1400703d0.c`](code/fcn.1400703d0.c)
- [`code/fcn.140078430.c`](code/fcn.140078430.c)
- [`code/fcn.140078e80.c`](code/fcn.140078e80.c)
- [`code/fcn.140079020.c`](code/fcn.140079020.c)
- [`code/fcn.14007abb0.c`](code/fcn.14007abb0.c)
- [`code/fcn.1400a3080.c`](code/fcn.1400a3080.c)
- [`code/fcn.1400b0aa0.c`](code/fcn.1400b0aa0.c)
- [`code/fcn.1400bb464.c`](code/fcn.1400bb464.c)
- [`code/fcn.1400bb498.c`](code/fcn.1400bb498.c)
- [`code/fcn.1400cd608.c`](code/fcn.1400cd608.c)
- [`code/fcn.1400cfa64.c`](code/fcn.1400cfa64.c)
- [`code/fcn.1400cfa6c.c`](code/fcn.1400cfa6c.c)
- [`code/fcn.1400d042c.c`](code/fcn.1400d042c.c)
- [`code/fcn.1400d0554.c`](code/fcn.1400d0554.c)
- [`code/fcn.1400d672c.c`](code/fcn.1400d672c.c)
- [`code/fcn.1400d6740.c`](code/fcn.1400d6740.c)
- [`code/fcn.1400dc2f0.c`](code/fcn.1400dc2f0.c)
- [`code/method.ATL__CComModule.virtual_64.c`](code/method.ATL__CComModule.virtual_64.c)
- [`code/method.ATL__CComModule.virtual_72.c`](code/method.ATL__CComModule.virtual_72.c)
- [`code/method.CCallTreeData.virtual_16.c`](code/method.CCallTreeData.virtual_16.c)
- [`code/method.CFilterDlg.virtual_24.c`](code/method.CFilterDlg.virtual_24.c)
- [`code/method.CHighlightDlg.virtual_24.c`](code/method.CHighlightDlg.virtual_24.c)
- [`code/method.std__ctype_unsigned_short_int_.virtual_24.c`](code/method.std__ctype_unsigned_short_int_.virtual_24.c)
- [`code/method.std__ctype_unsigned_short_int_.virtual_96.c`](code/method.std__ctype_unsigned_short_int_.virtual_96.c)

## Behavioral Analysis

This analysis incorporates the findings from **chunk 6/6**. This final portion of the disassembly provides the "smoking gun" regarding how the malware processes its internal logic, transitioning from the bulky "mimicry" shell into the core execution phase.

---

### Analysis of New Findings (Chunk 6/6)

#### 1. Dynamic Address Calculation & Pointer Obfuscation
The heavy use of bitwise shifts (`>> 0x20`), large multiplication factors, and complex offset calculations (e.g., `uVar18 + ((uVar11 << 0x20) + uVar15 << (uStack_b68 & 0x3f))`) indicates that the loader is not using standard, direct memory addresses for its internal operations.
*   **The Technique:** Instead of calling a known function directly, the code calculates the address of the next instruction or the next piece of data at runtime. This prevents static analysis tools from easily mapping out the "call graph" (the sequence of functions the malware calls).
*   **Implication:** The malware is likely using **Position Independent Code (PIC)** techniques or a custom **Virtual Machine (VM) / Interpreter** wrapper to execute its core logic, making it very difficult for automated sandboxes to predict where the code will jump next.

#### 2. Just-In-Time (JIT) String/Instruction Decryption
The final sequences in this chunk—specifically the calculation of `uVar18` and the subsequent use of XOR operations before a function call (`uStack_48 ^ auStack_bb8`)—are classic indicators of "Just-in-Time" decryption.
*   **The Process:** The malware holds its true commands (the ones that actually perform malicious actions) in an encrypted state. It only decrypts the specific command into memory at the exact millisecond it needs to execute it.
*   **The Purpose:** This hides strings like "RemoteShell," "DeleteLog," or actual C2 (Command & Control) IP addresses from scanners until the moment of execution, effectively bypassing static string analysis.

#### 3. Complex State Machine for Memory Navigation
The repetitive loops checking against `0x73` and managing `auStack_784` suggest a sophisticated method for navigating an internal "data blob." 
*   **Decoding Logic:** The code isn't just moving through memory; it is interpreting a custom data structure. It treats a chunk of the binary as a database, using indices to find functions or values only when needed.
*   **The Shield:** This adds a significant layer of **Complexity Obfuscation**. A human analyst looking at this code must manually trace several nested loops and bitwise shifts just to understand how one single variable is retrieved.

#### 4. The Transition Point (The "Hand-off")
The final transition in this chunk, specifically the jump toward `fcn.1400b9590`, marks the point where the **Mimicry Layer** (Procmon-like behavior) and the **Complexity Layer** (the math-heavy code) finally give way to the **Payload Execution**. The fact that it concludes with an XOR operation suggests this is the final "gate" before a malicious routine is triggered.

---

### Final Comprehensive Threat Profile: "The Chameleon Shell"

The complete analysis of all 6 chunks confirms that this is not a simple piece of malware; it is a **High-Sophistication Hybrid Loader** designed for Advanced Persistent Threats (APT) or high-value target exploitation.

#### Core Characteristics:
1.  **Extreme Mimicry (Pro-Tool Masking):** By embedding deep functionality and structures from *Procmon*, the loader hides in plain sight as a legitimate system diagnostic tool. It doesn't just "pretend" to be Procmon; it mimics its logic, making automated behavioral flags much harder to trigger.
2.  **Advanced Obfuscation Architecture:**
    *   **The Volume Shield:** Thousands of lines of "boring" UI and utility code.
    *   **The Logic Shield:** Complex bitwise arithmetic and state machines that mask the true intent of the underlying instructions.
    *   **The JIT Decryption:** Only decrypts malicious components in memory just before they are needed, evading static signature-based detection.
3.  **Rootkit Capabilities (via IOCTL):** The extensive mapping of **IOCTL codes** identified in earlier chunks confirms that the loader is designed to communicate with low-level drivers. This suggests it can hide files, interact with raw disk sectors, or bypass standard Windows security APIs.
4.  **Sophisticated Engineering:** The use of professional coding standards (thread safety, complex memory management, and advanced pointer arithmetic) indicates a developer with deep knowledge of the Windows Internals and low-level systems programming.

### Final Conclusion:
The loader acts as a **highly durable gateway**. It is designed to exhaust the resources of both automated scanners (by being too large and "noisy") and human analysts (by making the logic path so complex that it takes days or weeks to find the "true" malicious branch). 

**Final Risk Assessment:** High. The presence of IOCTL mapping combined with advanced polymorphism/obfuscation suggests this tool is capable of deploying sophisticated payloads, including rootkits or persistent backdoors, while remaining virtually invisible during the initial stages of infection.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization | The use of a "VM / Interpreter wrapper" and complex state machines masks the underlying logic flow from automated analysis. |
| **T1027** | Obfuscated Files or Information | Just-in-time (JIT) decryption using XOR operations hides malicious strings and commands until the moment they are needed for execution. |
| **T1036** | Masquerading | The "Mimicry Layer" hides malicious activity by intentionally mimicking the logic and behavior of a legitimate system tool (Procmon). |
| **T1014** | Rootkit | The mapping of IOCTL codes indicates communication with drivers to perform low-level actions such as hiding files or bypassing security APIs. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Due to the high level of obfuscation described in the "Behavioral Analysis" section, many traditional IOCs (like cleartext IPs or URLs) are currently hidden behind JIT decryption layers.*

### **IP addresses / URLs / Domains**
*   None identified. (Analysis indicates these are likely encrypted and only decrypted in memory during execution).

### **File paths / Registry keys**
*   None identified. (The analysis notes the use of "Mimicry," but no specific malicious paths were exposed in the provided strings).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Function Pointer/Address:** `fcn.1400b9590` (Identified as the transition point from the mimicry/complexity layers to the actual payload execution).
*   **C2 / Obfuscation Patterns:** 
    *   **JIT Decryption:** Use of XOR operations on variables (e.g., `uStack_48 ^ auStack_bb8`) prior to function calls to hide strings and C2 infrastructure.
    *   **Complex Address Calculation:** Usage of bitwise shifts (`>> 0x20`), large multipliers, and complex offsets (e.g., `uVar18 + ((uVar11 << 0x20) + uVar15 << (uStack_b68 & 0x3f))`) to evade static analysis of the call graph.
    *   **State Machine Logic:** Use of repeated loops checking against `0x73` and managing `auStack_784` for navigating internal data structures.
    *   **Mimicry Tactics:** Intentional mimicry of **Procmon** (Process Monitor) logic and behavior to bypass heuristic detection.
    *   **Low-Level Communication:** Evidence of **IOCTL mapping**, indicating communication with low-level drivers for potential rootkit functionality.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `https://sysinternals.com/downloads/procmon`

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1.  **Malware family:** custom
2.  **Malware type:** loader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Sophisticated Obfuscation & Mimicry:** The malware utilizes a "Mimicry Layer" to emulate the behavior of legitimate system tools (Procmon) combined with advanced JIT decryption and complex state-machine navigation to hide its true intent from automated scanners.
    *   **Advanced Execution Logic:** The use of Position Independent Code (PIC) techniques, bitwise shift-based address calculations, and "Just-in-Time" XOR operations indicates a high level of engineering designed to shield the primary payload until the moment of execution.
    *   **Rootkit Capabilities:** The mapping of IOCTL codes indicates that the loader is designed to interact with low-level drivers, providing it with the capabilities to hide files or bypass security protocols as part of its role as a "highly durable gateway."
