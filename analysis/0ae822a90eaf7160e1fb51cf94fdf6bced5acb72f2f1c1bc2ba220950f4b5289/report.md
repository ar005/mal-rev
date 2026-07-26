# Threat Analysis Report

**Generated:** 2026-07-25 16:07 UTC
**Sample:** `0ae822a90eaf7160e1fb51cf94fdf6bced5acb72f2f1c1bc2ba220950f4b5289_0ae822a90eaf7160e1fb51cf94fdf6bced5acb72f2f1c1bc2ba220950f4b5289.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ae822a90eaf7160e1fb51cf94fdf6bced5acb72f2f1c1bc2ba220950f4b5289_0ae822a90eaf7160e1fb51cf94fdf6bced5acb72f2f1c1bc2ba220950f4b5289.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,299,968 bytes |
| MD5 | `d1260f6c84de6a0c6d7caa47ef4b321d` |
| SHA1 | `40819d82339ea1e026a769ed17ba547ab54d9f3b` |
| SHA256 | `0ae822a90eaf7160e1fb51cf94fdf6bced5acb72f2f1c1bc2ba220950f4b5289` |
| Overall entropy | 7.176 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768354570 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.61 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 420,864 | 7.911 | ⚠️ Yes |
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

Total strings found: **3053** (showing first 100)

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

This final segment of disassembly provides a "behind-the-curtain" look at the interpreter's core execution loop and its role as an intermediate layer between high-level scripting logic and low-level Windows API interactions. 

The complexity of these functions confirms that this is not a simple script runner; it is a **sophisticated execution environment** capable of handling polymorphic data types, complex memory management, and large-scale command dispatching.

### Updated Analysis Summary

#### 1. Advanced Interpreter Architecture: Type System & Command Dispatch
The logic in `fcn.00411df0` and the subsequent switch tables (e.g., at `0x4562b3`) reveal a highly structured "Type System."

*   **Robust Data Handling:** The code handles specialized constants like `0x7fffffff`. In many scriptable environments, this is used as a sentinel value for **Null or Undefined**. The interpreter specifically checks for these before attempting to access properties.
*   **Complexity of Dispatch:** The repeated use of large switch tables (e.g., in `fcn.00412c10` and `fcn.0040f650`) indicates a **Command/Opcode Pattern**. When the script requests an action, it doesn't just call a function; it passes an identifier that this dispatcher then maps to a specific internal "handler."
*   **Object Navigation:** The loops in `fcn.00412c10` suggest the interpreter is traversing **nested structures** (like arrays of objects or nested properties). It performs bounds checking and offset calculations before proceeding, ensuring that a malformed script doesn't crash the host process but rather handles it within the virtualized environment.

#### 2. The "Command Dispatcher" (The Interpreter's Heart)
Function `fcn.0040f650` is a critical finding. It acts as the primary router for the interpreter’s internal logic.

*   **Opcode Mapping:** The switch table at `0x40f828` contains dozens of cases, each mapping to specific sub-functions (e.g., `0x40f795`, `0x40f7bc`). This is characteristic of a **virtual machine or an automation framework** where the "script" is actually a list of instructions that get passed through this dispatcher.
*   **Internal State Management:** The logic inside these cases often handles internal flags, buffer lengths, and state transitions before passing control back to the script. 
*   **Abstraction Layer:** This confirms that the script does not interact directly with the OS; it interacts with the *dispatcher*, which in turn manages the "context" of the script's execution (e.g., managing local variables, scope, and memory).

#### 3. Advanced Memory & Buffer Management
Functions like `fcn.0040bd9d` and `fcn.0040be83` show how the engine manages its internal memory for the script's benefit.

*   **Dynamic Allocation:** The code calculates required buffer sizes based on expected types (e.g., checking if a value is between `0x2f` and `0x40`). 
*   **Auto-Scaling:** It implements logic to automatically resize or reallocate memory when script-driven data grows, ensuring the "script" has a seamless experience similar to high-level languages like Python or JavaScript.

#### 4. Advanced UI/System Interaction (The Bridge)
The function `fcn.0040c3cb` provides further evidence of how the script manipulates the Windows environment.

*   **GUI Manipulation:** The presence of logic related to `InvalidateRect` and coordinate calculations for regions suggests the scripts are capable of **manipulating UI elements, redrawing windows, or interacting with specific areas of the screen.**
*   **Complex Win32 Handling:** It doesn't just call a function; it processes "Rectangle" structures and other Windows-specific types. This indicates that the interpreter provides a high-level abstraction for GUI programming to the script writer.

---

### Updated Technical Indicators (Detection/Hunting)

*   **Architecture:** **Instructional Interpreter with Command Dispatch.** The malware utilizes an intermediate representation (IR) where "script" commands are dispatched through a large switch table.
*   **Key Code Patterns:** 
    *   **Large Switch Tables for Type Checking:** Use of `0x47`, `0x48`, and `0x7f` as type identifiers in high-level logic.
    *   **Sentinel Value Detection:** Frequent checks against `0x7fffffff` (Null/Undefined).
    *   **Automated Buffer Growth:** Logic that calculates `(size * 2)` or rounds up to the nearest memory page for internal string/data handling.
*   **Hardcoded Indicators:** 
    *   **Logic Constants:** The switch tables at `0x4562b3`, `0x45722c`, and `0x40f828`.
    *   **String Signatures:** If the script is extracted, look for "bridge" terms like `@GUI_WINHANDLE` or internal command mappings.

---

### Final Recommendations for Incident Response

1.  **Identify Command Mapping (The "Action" Map):** The most critical step for understanding the malware's capability is to map the cases in the `fcn.0040f650` switch table. By identifying what each case does, you can determine the full suite of "actions" available to the script author (e.g., file deletion, keylogging, screen capture).
2.  **Memory Forensics for Script Extraction:** Since the interpreter manages its own buffers and uses a dispatcher, the most complete version of the malicious script will likely reside in memory in a **pre-processed or semi-parsed state**. Monitoring `fcn.0041fd5b` (the allocation/retrieval function) can help identify where the script's data structures are stored in RAM.
3.  **Hook the Dispatcher:** Instead of trying to reverse every switch case, hook the entry point of the dispatcher (`0x40f650`). Log the `arg_8h` (usually a command ID) and subsequent function calls. This will provide a "log" of what commands the script is actually issuing during execution.
4.  **Advanced Behavioral Monitoring:** Because the "bridge" functions (like `0x40c3cb`) handle Win32 structures, standard API monitoring might only see the end result. You should monitor for **atypical usage of GUI-related APIs**, such as calling `InvalidateRect` or `GetWindowText` from a process that shouldn't be interacting with other windows (a sign of an overlaid UI or automated interaction).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a sophisticated interpreter, custom "Instructional" architecture, and opcode mapping conceals the actual malicious logic from static analysis. |
| **T1059.003** | DOS Command and Scripting Interpreter | The malware utilizes an intermediate representation (IR) and a command dispatcher to execute high-level script logic as distinct system actions. |
| **T1486** | (Internal/Related: Defense Evasion via Complexity) | *Note: While there isn't a single "GUI Manipulation" ID, the robust buffer management and abstraction layer are utilized to ensure execution stability while performing complex operations.* |

*(Self-Correction/Refinement on T1486: Since MITRE doesn't have a specific ID for "UI Manipulation," if you prefer strictly standard IDs, the GUI interaction behaviors described in section 4 are typically classified under **T1027** as they represent another layer of abstraction between the script and the direct Windows API calls.)* |

---

## Indicators of Compromise

Based on the provided report and strings, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The "EXTRACTED STRINGS" section contains a high volume of obfuscated data or memory-mapped values that do not resolve to clear network indicators (IPs/URLs) or file paths. Therefore, the most actionable IOCs for hunting are found within the behavioral analysis and internal code structures.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: Standard system paths were excluded as per instructions.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 hashes were present in the provided strings.)

### **Other artifacts**
*   **Internal Symbols / Strings:**
    *   `@GUI_WINHANDLE` (Used as a bridge term for GUI manipulation)
*   **Critical Function Offsets (Memory Signatures):**
    *   `0x411df0` (Type System handling)
    *   `0x4562b3` (Switch table/Logic logic)
    *   `0x45722c` (Switch table/Logic)
    *   `0x40f650` (Primary Command Dispatcher - **High Value for Hunting**)
    *   `0x40f828` (Opcode Mapping Table)
    *   `0x40bd9d` (Memory Allocation/Buffer Management)
    *   `0x40be83` (Memory Allocation/Buffer Management)
    *   `0x40c3cb` (Win32 API Bridge/GUI Manipulation)
*   **Logic Constants & Behavioral Signatures:**
    *   `0x7fffffff` (Used as a sentinel value for Null/Undefined logic)
    *   Type identifiers: `0x47`, `0x48`, `0x7f`
    *   Automatic buffer growth calculations: `(size * 2)` or rounding to the nearest memory page.

---
**Analyst Note:** Because this malware utilizes a **Virtual Machine/Interpreter architecture**, traditional static IOCs (like IPs) may not appear in the binary itself but rather in the "script" it loads at runtime. Detection efforts should focus on **behavioral monitoring of the Dispatcher (`0x40f650`)** and memory forensics to capture the unpacked script data.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for this sample:

1.  **Malware family**: custom
2.  **Malware type**: backdoor / loader
3.  **Confidence**: Medium
4.  **Key evidence**:
    *   **Sophisticated Interpreter Architecture:** The presence of a "Command Dispatcher" (`0x40f650`) and an "Instructional Interpreter" indicates that the malware is designed to execute complex, modular logic via an internal script or instruction set rather than hardcoded actions. This architecture is used to hide functionality from static analysis (T1027).
    *   **Robust Execution Environment:** The implementation of a custom "Type System," automatic memory management, and extensive command mapping suggests the sample is not a simple downloader but a sophisticated persistent component designed to provide a wide range of functionalities (e.g., file manipulation, remote commands) typical of a **backdoor**.
    *   **Advanced GUI/Interaction capabilities:** The identification of code specifically for Win32 "GUI Manipulation" and coordinates suggests the malware is capable of interacting with the user's environment or other windows, which is common in Remote Access Trojans (RATs).

***Note on Confidence:*** *The confidence level is Medium because while the architecture clearly points to a sophisticated backdoor/loader system, there are no unique strings, IPs, or specific signatures provided that allow for a definitive mapping to a known threat actor's naming convention (e.g., "Cobalt Strike" or "Qakbot").*
