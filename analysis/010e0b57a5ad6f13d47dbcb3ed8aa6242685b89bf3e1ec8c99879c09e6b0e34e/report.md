# Threat Analysis Report

**Generated:** 2026-06-26 14:53 UTC
**Sample:** `010e0b57a5ad6f13d47dbcb3ed8aa6242685b89bf3e1ec8c99879c09e6b0e34e_010e0b57a5ad6f13d47dbcb3ed8aa6242685b89bf3e1ec8c99879c09e6b0e34e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `010e0b57a5ad6f13d47dbcb3ed8aa6242685b89bf3e1ec8c99879c09e6b0e34e_010e0b57a5ad6f13d47dbcb3ed8aa6242685b89bf3e1ec8c99879c09e6b0e34e.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,257,472 bytes |
| MD5 | `c3cc788bcb45bf0bb697e18f70178f7f` |
| SHA1 | `b315fab3933c383bfba300fbafa081b4aceb7156` |
| SHA256 | `010e0b57a5ad6f13d47dbcb3ed8aa6242685b89bf3e1ec8c99879c09e6b0e34e` |
| Overall entropy | 7.131 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771392173 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.61 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 378,368 | 7.893 | ⚠️ Yes |
| `.reloc` | 30,208 | 6.798 | No |

### Imports

**KERNEL32.DLL**: `DuplicateHandle`, `CreateThread`, `WaitForSingleObject`, `HeapAlloc`, `GetProcessHeap`, `HeapFree`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `MulDiv`, `GetVersionExW`, `IsWow64Process`, `GetSystemInfo`, `FreeLibrary`, `LoadLibraryA`
**ADVAPI32.dll**: `GetAce`, `RegEnumValueW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegOpenKeyExW`, `RegCloseKey`, `RegQueryValueExW`, `RegConnectRegistryW`, `InitializeSecurityDescriptor`, `InitializeAcl`, `AdjustTokenPrivileges`, `OpenThreadToken`, `OpenProcessToken`
**COMCTL32.dll**: `ImageList_ReplaceIcon`, `ImageList_Destroy`, `ImageList_Remove`, `ImageList_SetDragCursorImage`, `ImageList_BeginDrag`, `ImageList_DragEnter`, `ImageList_DragLeave`, `ImageList_EndDrag`, `ImageList_DragMove`, `InitCommonControlsEx`, `ImageList_Create`
**COMDLG32.dll**: `GetSaveFileNameW`, `GetOpenFileNameW`
**GDI32.dll**: `EndPath`, `DeleteObject`, `GetTextExtentPoint32W`, `ExtCreatePen`, `StrokeAndFillPath`, `GetDeviceCaps`, `SetPixel`, `CloseFigure`, `LineTo`, `AngleArc`, `MoveToEx`, `Ellipse`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `PolyDraw`
**IPHLPAPI.DLL**: `IcmpSendEcho`, `IcmpCloseHandle`, `IcmpCreateFile`
**MPR.dll**: `WNetGetConnectionW`, `WNetCancelConnection2W`, `WNetUseConnectionW`, `WNetAddConnection2W`
**ole32.dll**: `CoTaskMemAlloc`, `CoTaskMemFree`, `CLSIDFromString`, `ProgIDFromCLSID`, `CLSIDFromProgID`, `OleSetMenuDescriptor`, `MkParseDisplayName`, `OleSetContainedObject`, `CoCreateInstance`, `IIDFromString`, `StringFromGUID2`, `CreateStreamOnHGlobal`, `OleInitialize`, `OleUninitialize`, `CoInitialize`
**OLEAUT32.dll**: `CreateStdDispatch`, `CreateDispTypeInfo`, `UnRegisterTypeLib`, `UnRegisterTypeLibForUser`, `RegisterTypeLibForUser`, `RegisterTypeLib`, `LoadTypeLibEx`, `VariantCopyInd`, `SysReAllocString`, `SysFreeString`, `VariantChangeType`, `SafeArrayDestroyData`, `SafeArrayUnaccessData`, `SafeArrayAccessData`, `SafeArrayAllocData`
**PSAPI.DLL**: `GetProcessMemoryInfo`
**SHELL32.dll**: `DragFinish`, `DragQueryPoint`, `ShellExecuteExW`, `DragQueryFileW`, `SHEmptyRecycleBinW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHCreateShellItem`, `SHGetDesktopFolder`, `SHGetSpecialFolderLocation`, `SHGetFolderPathW`, `SHFileOperationW`, `ExtractIconExW`, `Shell_NotifyIconW`, `ShellExecuteW`
**USER32.dll**: `IsCharAlphaW`, `IsCharAlphaNumericW`, `IsCharLowerW`, `IsCharUpperW`, `GetMenuStringW`, `GetSubMenu`, `GetCaretPos`, `IsZoomed`, `MonitorFromPoint`, `GetMonitorInfoW`, `SetWindowLongW`, `SetLayeredWindowAttributes`, `FlashWindow`, `GetClassLongW`, `TranslateAcceleratorW`
**USERENV.dll**: `DestroyEnvironmentBlock`, `LoadUserProfileW`, `CreateEnvironmentBlock`, `UnloadUserProfile`
**UxTheme.dll**: `IsThemeActive`
**VERSION.dll**: `GetFileVersionInfoW`, `VerQueryValueW`, `GetFileVersionInfoSizeW`
**WININET.dll**: `HttpOpenRequestW`, `InternetCloseHandle`, `InternetOpenW`, `InternetSetOptionW`, `InternetCrackUrlW`, `HttpQueryInfoW`, `InternetQueryOptionW`, `InternetConnectW`, `HttpSendRequestW`, `FtpOpenFileW`, `FtpGetFileSize`, `InternetOpenUrlW`, `InternetReadFile`, `InternetQueryDataAvailable`
**WINMM.dll**: `timeGetTime`, `waveOutSetVolume`, `mciSendStringW`
**WSOCK32.dll**: `gethostbyname`, `recv`, `send`, `socket`, `ioctlsocket`, `setsockopt`, `ntohs`, `WSACleanup`, `WSAStartup`, `sendto`, `htons`, `__WSAFDIsSet`, `select`, `accept`, `listen`

## Extracted Strings

Total strings found: **2920** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc
tLf9Vt.
T$ j*Xf9
09L$$v&
M;O|
C(_^[]
WWjdh,
PWWWWh
<SVWj,
 SVWj0
jJXf9E
jJXf9E
9Fs7j
t<j	Yf;
t4j"Yf;
tj	Yf;
u9^u
t$8]4t
D$(;D$4
f98t>j
t<jhx
F(F P
D$lD$tPVWR
D$<9D$ tJj
L$p;\$t
 !"#$%%%%%%&&'()*+%%%%%%&&'()*+,,,,,,--./012RRRRRRRRRRRR3345566789::::;<=<=>?>@ABC>@ABCRRRRRDEFGHIJKLMNO
<tC<
tZ
utjf;}
|$D;|$@
D$<f9D$H
D$D9D$8
D$Hf9D$<
D$ PVj
D$hD%M
D$dD%M
D$@f9D$D
D$\f9D$x
D$`D%M
D$dD%M
L$@9D$hr
D$xf9D$\s'
D$xf9D$\
D$xf9D$\s#
L$$PWVj
9D$Hu;
D$09D$H
D$0;D$H
\$(j|Xf9
L$@jxXf
j?Xf9F
j#Xf9F
j\Xf9F
uj-Xf9F
jEYf9N
jQYf9N
j#Xj(Yj?Zf9N
j]Xf9F
						
												
						
																									
YYj!Yf;
awjUXf;
8_u.Vj
		

			
	

            
tf9Uta
jOXf9E
M8V:t
M;Jr

Yt
jV
F;BtO
38_^]
E9xt
QQSVWd
URPQQh
tH9] uC
u PWQR
9Ov:k
;t$,v-
kUQPXY]Y[
SVWjA_jZ+
uBjAYjZ+
tj-ZCf
u0jAXf;
u0jAXf;
tf;1u
	<et<Et
<ot<ut
Tt1jhZ;
Tt1jhZ;
^$+^8+
t	j-Xf
atjA_f;
t0jXXf
tjAXf;
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00410540` | `0x410540` | 283497 | ✓ |
| `fcn.0040a180` | `0x40a180` | 282866 | ✓ |
| `fcn.0040ad7c` | `0x40ad7c` | 282757 | ✓ |
| `fcn.0040ab30` | `0x40ab30` | 282224 | ✓ |
| `fcn.0040f8d0` | `0x40f8d0` | 282209 | ✓ |
| `fcn.00411fa0` | `0x411fa0` | 282204 | ✓ |
| `fcn.0040b230` | `0x40b230` | 281886 | ✓ |
| `fcn.0040b126` | `0x40b126` | 281835 | ✓ |
| `fcn.0040ad22` | `0x40ad22` | 281743 | ✓ |
| `fcn.0040b7e0` | `0x40b7e0` | 281595 | ✓ |
| `fcn.0040b38e` | `0x40b38e` | 281576 | ✓ |
| `fcn.0040b471` | `0x40b471` | 281541 | ✓ |
| `fcn.0040b5c1` | `0x40b5c1` | 281486 | ✓ |
| `fcn.0040b703` | `0x40b703` | 281327 | ✓ |
| `fcn.0040b79d` | `0x40b79d` | 281308 | ✓ |
| `fcn.0040b6ca` | `0x40b6ca` | 281295 | ✓ |
| `fcn.0040f060` | `0x40f060` | 280731 | ✓ |
| `fcn.00411ae0` | `0x411ae0` | 280531 | ✓ |
| `fcn.0040bd9d` | `0x40bd9d` | 280141 | ✓ |
| `fcn.00411df0` | `0x411df0` | 280124 | ✓ |
| `fcn.00412c10` | `0x412c10` | 280092 | ✓ |
| `fcn.0040be83` | `0x40be83` | 279979 | ✓ |
| `fcn.0040bef7` | `0x40bef7` | 279891 | ✓ |
| `fcn.0040f650` | `0x40f650` | 279813 | ✓ |
| `fcn.0040c000` | `0x40c000` | 279655 | ✓ |
| `fcn.0040c0a8` | `0x40c0a8` | 279503 | ✓ |
| `fcn.0040c117` | `0x40c117` | 279436 | ✓ |
| `fcn.0040c28f` | `0x40c28f` | 279079 | ✓ |
| `fcn.0040c315` | `0x40c315` | 278994 | ✓ |
| `fcn.0040c3cb` | `0x40c3cb` | 278988 | ✓ |

### Decompiled Code Files

- [`code/fcn.0040a180.c`](code/fcn.0040a180.c)
- [`code/fcn.0040ab30.c`](code/fcn.0040ab30.c)
- [`code/fcn.0040ad22.c`](code/fcn.0040ad22.c)
- [`code/fcn.0040ad7c.c`](code/fcn.0040ad7c.c)
- [`code/fcn.0040b126.c`](code/fcn.0040b126.c)
- [`code/fcn.0040b230.c`](code/fcn.0040b230.c)
- [`code/fcn.0040b38e.c`](code/fcn.0040b38e.c)
- [`code/fcn.0040b471.c`](code/fcn.0040b471.c)
- [`code/fcn.0040b5c1.c`](code/fcn.0040b5c1.c)
- [`code/fcn.0040b6ca.c`](code/fcn.0040b6ca.c)
- [`code/fcn.0040b703.c`](code/fcn.0040b703.c)
- [`code/fcn.0040b79d.c`](code/fcn.0040b79d.c)
- [`code/fcn.0040b7e0.c`](code/fcn.0040b7e0.c)
- [`code/fcn.0040bd9d.c`](code/fcn.0040bd9d.c)
- [`code/fcn.0040be83.c`](code/fcn.0040be83.c)
- [`code/fcn.0040bef7.c`](code/fcn.0040bef7.c)
- [`code/fcn.0040c000.c`](code/fcn.0040c000.c)
- [`code/fcn.0040c0a8.c`](code/fcn.0040c0a8.c)
- [`code/fcn.0040c117.c`](code/fcn.0040c117.c)
- [`code/fcn.0040c28f.c`](code/fcn.0040c28f.c)
- [`code/fcn.0040c315.c`](code/fcn.0040c315.c)
- [`code/fcn.0040c3cb.c`](code/fcn.0040c3cb.c)
- [`code/fcn.0040f060.c`](code/fcn.0040f060.c)
- [`code/fcn.0040f650.c`](code/fcn.0040f650.c)
- [`code/fcn.0040f8d0.c`](code/fcn.0040f8d0.c)
- [`code/fcn.00410540.c`](code/fcn.00410540.c)
- [`code/fcn.00411ae0.c`](code/fcn.00411ae0.c)
- [`code/fcn.00411df0.c`](code/fcn.00411df0.c)
- [`code/fcn.00411fa0.c`](code/fcn.00411fa0.c)
- [`code/fcn.00412c10.c`](code/fcn.00412c10.c)

## Behavioral Analysis

This analysis continues from the previous findings, incorporating the final chunk of disassembly. This new data provides definitive confirmation that the module is not merely a simple "task runner," but a **high-level execution environment**—likely a scripting engine or a virtual machine (VM) core.

The inclusion of these functions confirms the sophistication of the architecture and the professional quality of the implementation.

---

### Updated Analysis of Behavioral Patterns

#### 1. Multi-Tiered Dispatch Architecture
The most striking addition in this chunk is the presence of multiple, massive "Master" dispatchers (e.g., `fcn.00412c10` and `fcn.0040f650`).
*   **Hierarchical Execution:** Instead of a single loop handling all logic, the engine uses a tiered system. A script instruction is first identified by a primary code (e.g., in `fcn.0040f650`), which then points to a secondary specialized handler or a sub-routine that performs specific calculations before returning control to the main state machine.
*   **Complexity as Safety:** The extensive switch tables and nested checks are classic "Gatekeeper" logic. This ensures that before an operation is executed, it is validated for type compatibility, memory safety, and valid range—a requirement for any engine hosting third-party code (like a JS engine or a SQL processor).

#### 2. Complex Object & Variant Handling
The functions `fcn.0040c000` through `fcn.0040c315` indicate the existence of an **Object System** (potentially similar to .NET "Variants" or COM objects).
*   **Type Checking and Casting:** The logic in these functions frequently checks offsets like `+ 8`, `+ 12`, and `+ 0x20`. This is the standard way engines manage polymorphic data—the first few bytes of an object define its "type," which then determines how the remaining bytes are interpreted.
*   **Safety Wrappers:** The code frequently checks if values are within certain bounds (e.g., the check for `0x7fffffff` or `5000`) before performing arithmetic. This prevents buffer overflows and out-of-bounds memory access, suggesting a "safe" execution environment for scripts.

#### 3. Dynamic Memory Management
The functions `fcn.0040bd9d`, `fcn.0040be83`, and `fcn.0040bef7` are the **Engine's Infrastructure**.
*   **Automatic Buffer Expansion:** These functions handle "growing" memory blocks when a string or data structure exceeds its current allocated size (using `fcn.0041fd8b`). 
*   **Smart Allocation:** The logic doesn't just allocate a fixed buffer; it calculates necessary space based on the input and then re-maps the internal pointers. This is a high-level engineering practice used in professional compilers to handle variable-length inputs efficiently.

#### 4. Bridge to System/GUI Interaction
The presence of `InvalidateRect` (via `fcn.0040c3cb`) and other Win32 calls inside the logic flow indicates how the script engine communicates with the "Host" application's UI.
*   **Action-Based Rendering:** When a script executes an action that affects the interface, the engine doesn't just draw pixels; it updates its internal state and then notifies the Windows OS to refresh only the necessary regions of the screen (via `InvalidateRect`).

---

### Final Summary for Report

#### **Primary Function: Advanced Scripting Engine / Virtual Machine**
The module is a sophisticated piece of software designed to host, interpret, and execute a complex language or scripting system. It handles everything from low-level memory management and "Type" validation to high-level instruction dispatching. 

*   **Key Technical Indicators:**
    *   **Complex Dispatch Tables:** The use of large switch tables (over 40 cases in `fcn.0040f650`) suggests a wide range of supported commands or instructions within the engine's grammar.
    *   **Robust Memory Management:** Dedicated routines for buffer resizing and safety checks indicate a stable, high-performance codebase intended to prevent crashes when processing untrusted input.
    *   **Object Abstraction:** The code treats data as "objects" with specific types (likely using an internal ID system), allowing the engine to process different types of data through the same general execution logic.
    *   **Integration Hooks:** The inclusion of Win32 UI calls indicates this is a host-facing library, meant to provide functionality for a GUI application that utilizes scripts for logic or configuration.

#### **Analysis of Intent**
The code's complexity is significantly higher than what would be expected in typical "malware" loaders (which usually favor simple, obfuscated jumps). This is consistent with high-end commercial software such as:
1.  **A specialized Scripting Engine** (e.g., a custom implementation of Lua or Python used for internal tooling).
2.  **An Enterprise Application Framework** (handling complex database logic or automation scripts).
3.  **A Game Engine Component** (managing scripted events and character behaviors).

#### **Maliciousness Assessment: Low/None**
The modularity, the use of standardized "Safe" coding patterns (like length-checking before memory copies), and the highly structured nature of the dispatch tables strongly suggest a legitimate software product. 

While such an engine *could* be used as a container for malicious scripts (by hiding the payload inside the script files rather than the EXE itself), the **binary code provided is a characteristic implementation of a professional interpretation environment.** It provides the "tools" to run instructions, but it does not inherently perform any malicious actions.

**Final Note:** This module acts as the "Heart" of the application's logic. If this software is part of an investigation, the focus should shift from the **binary itself** (which appears to be a standard engine) to the **data files/scripts** that are fed into this interpreter, as those would contain the specific instructions being executed by these dispatchers.

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The "Multi-Tiered Dispatch Architecture" and "Master" dispatchers are used to identify and execute script instructions within a dedicated engine. |
| **T1497** | Virtualization | The analysis identifies the module as a high-level execution environment and a "virtual machine (VM) core" designed to host and interpret complex code. |
| **T1027** | Obfuscated Executables or Files | The use of extensive switch tables, nested checks, and abstraction layers serves to complicate manual analysis and hide the underlying logic's intent. |

---

## Indicators of Compromise

Based on my analysis of the provided strings and behavioral report, here is the extraction of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: The mentioned "fcn" entries are internal memory offsets/addresses, not system file paths or registry keys.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Functional Signature:** The analysis identifies a highly sophisticated **Scripting Engine / Virtual Machine (VM) core**. 
*   **Internal Offsets (Behavioral markers):** 
    *   `fcn.00412c10` & `fcn.0040f650`: Primary Dispatchers/Gatekeepers.
    *   `fcn.0040c000` – `fcn.0040c315`: Object System / Variant handling.
    *   `fcn.0040bd9d`, `fcn.0040be83`, `fcn.0040bef7`: Memory Management/Buffer Expansion routines.
    *   `fcn.0040c3cb`: Win32 API bridge (`InvalidateRect`).

---

**Analyst Note:** 
The provided data contains **no actionable network or file-system IOCs**. The "strings" section appears to contain scrambled/obfuscated characters and standard compiler test strings (e.g., the ASCII sequence `012RRRRR...ABC`). The behavioral analysis concludes that while the code is complex, it functions as a legitimate software framework (like a game engine or enterprise tool) rather than a standalone piece of malware. No immediate malicious indicators were found in the provided text.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Interpreter (Specifically: Scripting Engine / VM Core)
3. **Confidence**: Medium

4. **Key evidence**:
*   **Sophisticated Architecture:** The presence of multi-tiered dispatch tables and a "Master" dispatcher indicates a professional-grade execution environment designed to interpret complex scripts, rather than a simple, one-off malicious payload.
*   **Robust Engineering Patterns:** The implementation includes high-level features such as automated buffer expansion, safety checks for memory access (e.g., `0x7fffffff` checks), and a formal Object System, which are typical of legitimate software like game engines or enterprise frameworks.
*   **Lack of Direct Malicious Actions:** No hardcoded C2 infrastructure, exfiltration logic, or destructive behaviors were identified; the analysis concludes that while this "Interpreter" *could* host malicious scripts (making it a vehicle for malware), the binary itself is a standard execution engine.
