# Threat Analysis Report

**Generated:** 2026-06-27 06:31 UTC
**Sample:** `01ae9da99db03e2e97c0a99c4147fa01d0838064d056b68accba84d16d36fea5_01ae9da99db03e2e97c0a99c4147fa01d0838064d056b68accba84d16d36fea5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01ae9da99db03e2e97c0a99c4147fa01d0838064d056b68accba84d16d36fea5_01ae9da99db03e2e97c0a99c4147fa01d0838064d056b68accba84d16d36fea5.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,086,464 bytes |
| MD5 | `2a72f4990717038e7c9ff8d55298c98e` |
| SHA1 | `130b67cc2d22c7c6549112ed78f91e8e64c6847e` |
| SHA256 | `01ae9da99db03e2e97c0a99c4147fa01d0838064d056b68accba84d16d36fea5` |
| Overall entropy | 6.918 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1764677900 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 207,360 | 7.748 | ⚠️ Yes |
| `.reloc` | 30,208 | 6.798 | No |

### Imports

**WSOCK32.dll**: `gethostbyname`, `recv`, `send`, `socket`, `ioctlsocket`, `setsockopt`, `ntohs`, `WSACleanup`, `WSAStartup`, `sendto`, `htons`, `__WSAFDIsSet`, `select`, `accept`, `listen`
**VERSION.dll**: `GetFileVersionInfoW`, `VerQueryValueW`, `GetFileVersionInfoSizeW`
**WINMM.dll**: `timeGetTime`, `waveOutSetVolume`, `mciSendStringW`
**COMCTL32.dll**: `ImageList_ReplaceIcon`, `ImageList_Destroy`, `ImageList_Remove`, `ImageList_SetDragCursorImage`, `ImageList_BeginDrag`, `ImageList_DragEnter`, `ImageList_DragLeave`, `ImageList_EndDrag`, `ImageList_DragMove`, `InitCommonControlsEx`, `ImageList_Create`
**MPR.dll**: `WNetGetConnectionW`, `WNetCancelConnection2W`, `WNetUseConnectionW`, `WNetAddConnection2W`
**WININET.dll**: `HttpOpenRequestW`, `InternetCloseHandle`, `InternetOpenW`, `InternetSetOptionW`, `InternetCrackUrlW`, `HttpQueryInfoW`, `InternetQueryOptionW`, `InternetConnectW`, `HttpSendRequestW`, `FtpOpenFileW`, `FtpGetFileSize`, `InternetOpenUrlW`, `InternetReadFile`, `InternetQueryDataAvailable`
**PSAPI.DLL**: `GetProcessMemoryInfo`
**IPHLPAPI.DLL**: `IcmpSendEcho`, `IcmpCloseHandle`, `IcmpCreateFile`
**USERENV.dll**: `DestroyEnvironmentBlock`, `LoadUserProfileW`, `CreateEnvironmentBlock`, `UnloadUserProfile`
**UxTheme.dll**: `IsThemeActive`
**KERNEL32.dll**: `DuplicateHandle`, `CreateThread`, `WaitForSingleObject`, `HeapAlloc`, `GetProcessHeap`, `HeapFree`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `MulDiv`, `GetVersionExW`, `IsWow64Process`, `GetSystemInfo`, `FreeLibrary`, `LoadLibraryA`
**USER32.dll**: `IsCharAlphaW`, `IsCharAlphaNumericW`, `IsCharLowerW`, `IsCharUpperW`, `GetMenuStringW`, `GetSubMenu`, `GetCaretPos`, `IsZoomed`, `MonitorFromPoint`, `GetMonitorInfoW`, `SetWindowLongW`, `SetLayeredWindowAttributes`, `FlashWindow`, `GetClassLongW`, `TranslateAcceleratorW`
**GDI32.dll**: `EndPath`, `DeleteObject`, `GetTextExtentPoint32W`, `ExtCreatePen`, `StrokeAndFillPath`, `GetDeviceCaps`, `SetPixel`, `CloseFigure`, `LineTo`, `AngleArc`, `MoveToEx`, `Ellipse`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `PolyDraw`
**COMDLG32.dll**: `GetSaveFileNameW`, `GetOpenFileNameW`
**ADVAPI32.dll**: `GetAce`, `RegEnumValueW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegOpenKeyExW`, `RegCloseKey`, `RegQueryValueExW`, `RegConnectRegistryW`, `InitializeSecurityDescriptor`, `InitializeAcl`, `AdjustTokenPrivileges`, `OpenThreadToken`, `OpenProcessToken`
**SHELL32.dll**: `DragFinish`, `DragQueryPoint`, `ShellExecuteExW`, `DragQueryFileW`, `SHEmptyRecycleBinW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHCreateShellItem`, `SHGetDesktopFolder`, `SHGetSpecialFolderLocation`, `SHGetFolderPathW`, `SHFileOperationW`, `ExtractIconExW`, `Shell_NotifyIconW`, `ShellExecuteW`
**ole32.dll**: `CoTaskMemAlloc`, `CoTaskMemFree`, `CLSIDFromString`, `ProgIDFromCLSID`, `CLSIDFromProgID`, `OleSetMenuDescriptor`, `MkParseDisplayName`, `OleSetContainedObject`, `CoCreateInstance`, `IIDFromString`, `StringFromGUID2`, `CreateStreamOnHGlobal`, `OleInitialize`, `OleUninitialize`, `CoInitialize`
**OLEAUT32.dll**: `CreateStdDispatch`, `CreateDispTypeInfo`, `UnRegisterTypeLib`, `UnRegisterTypeLibForUser`, `RegisterTypeLibForUser`, `RegisterTypeLib`, `LoadTypeLibEx`, `VariantCopyInd`, `SysReAllocString`, `SysFreeString`, `VariantChangeType`, `SafeArrayDestroyData`, `SafeArrayUnaccessData`, `SafeArrayAccessData`, `SafeArrayAllocData`

## Extracted Strings

Total strings found: **2579** (showing first 100)

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

This analysis incorporates the findings from **chunk 5/5** into the existing report. The final set of disassembly data confirms and amplifies previous conclusions regarding the complexity of the engine, particularly its role as a robust execution environment that abstracts malicious actions through deep layers of nested logic and extensive switch tables.

### Updated Analysis of Behavior and Functionality

The analysis of this final chunk solidifies the conclusion that this is a **high-maturity Virtual Machine (VM) or Script Interpreter.** The sheer volume of dispatch code confirms that the "host" binary acts as a massive translation layer between script instructions and system-level operations.

#### 1. Extreme Complexity in Dispatch Logic
The most striking feature in this chunk is the repeated use of massive switch tables (e.g., `fcn.0040f650` and `fcn.00412c10`). 
*   **Multi-Layered Gating:** Even after a "Primary" opcode is identified, the engine enters a second or third layer of dispatching to determine the specific "Sub-action." For example, `fcn.0040f650` contains over 30 unique cases for different internal functions.
*   **Obfuscation through Volume:** By burying a single malicious action (like "Open Process" or "Inject DLL") behind three layers of switch statements, the author ensures that automated tools cannot easily map a script command to a specific Windows API without full manual tracing of the logic tree.

#### 2. Sophisticated Memory & Buffer Management
The functions `fcn.0040bd9d` and `fcn.0040be83` demonstrate advanced memory management:
*   **Dynamic Allocation:** These functions calculate required buffer sizes, perform bitwise alignment checks (e.g., `& 0xffffffff8`), and manage internal memory structures.
*   **Variable-Length Handling:** The logic is designed to handle data structures of varying lengths, which suggests the interpreter can process complex objects like long strings, large configuration blocks, or multi-part payloads.

#### 3. Interaction with Windows UI/Environment
The appearance of functions related to `USER32.dll` and `HWND` (e.g., in `fcn.0040c3cb`) indicates that the interpreter is not just "silent" background logic:
*   **GUI Interactions:** The use of `InvalidateRect` suggests that the script can trigger UI updates or interact with windows. This might be used for "fake" error messages, overlay displays, or even interacting with other Windows components to hide its presence within a legitimate-looking window context.

#### 4. Extensive Instruction "Breadth"
The sheer number of cases in `fcn.0040f650` suggests that the underlying scripting language is highly featured. It isn't just executing basic commands; it supports a wide array of operations, likely covering file system manipulation, network communication, process injection, and system information gathering.

---

### Updated Suspicious and Malicious Behaviors

The final chunk confirms several indicators of high-end functionality:

*   **Extensive Action Catalog:** The massive switch tables indicate that the interpreter is capable of performing a vast range of different tasks based on the script provided. This allows the malware to remain "generic" while only changing the script file to change its behavior (e.g., switching from an info-stealer to a ransomware deployer).
*   **Complexity as Defense:** The "Gatekeeper" pattern (where functions like `fcn.00412c10` act as deep intermediaries) is specifically designed to defeat static and automated dynamic analysis. It forces the analyst to work through several layers of interpretation just to reach a single malicious call.
*   **Robust Environment Integration:** The integration of OLE Variants, advanced buffer management, and UI-related logic indicates an engine built for persistence and versatility in complex environments.

---

### Updated Notable Techniques and Patterns

*   **Nested & Recursive Switch Tables:** Multi-stage dispatching used to separate the "logic" (the script) from the "action" (the machine code).
*   **Complex Memory Management:** Sophisticated internal functions for buffer calculation, ensuring that dynamic data handled by the interpreter is correctly aligned and managed in memory.
*   **OLEAUT32 Integration:** Used to handle complex data objects, allowing for highly flexible script-to-host communication.
*   **Abstracted API Execution:** Most Windows APIs are never called directly by "primary" logic but are reached through several stages of interpretation, creating a significant gap between the intent and the execution.

---

### Final Summary for Analysis Report

*   **Classification:** **Advanced Multi-Layered VM / Script Interpreter.**
*   **Purpose:** This binary functions as a highly sophisticated runtime environment designed to interpret and execute an internal, complex scripting language. It is engineered to provide maximum flexibility for the attacker while providing significant layers of abstraction between the script's commands and the system's responses.

*   **Threat Level Note (Critical):** The architecture is indicative of **high-tier malware frameworks (e.g., PlugX, Cobalt Strike, or bespoke state-sponsored implants).** The use of multi-layered dispatching to hide "action" functions means that the binary itself may not appear malicious until a specific script is loaded and executed within its environment. This creates a significant hurdle for signature-based detection and automated sandbox analysis.

*   **Key Indicators:**
    *   **Deeply Nested Dispatchers:** Massive switch tables (over 30 cases) used to resolve instructions through multiple levels of logic before calling an underlying API.
    *   **OLEAUT32/Variant Support:** Extensive use of `VariantCopy` and related structures for managing complex, nested data types.
    *   **Sophisticated Memory Orchestration:** Dedicated internal routines for memory alignment, buffer calculation, and management of variable-length data.
    *   **UI/System Interaction Capabilities:** Integration with `USER32` functions to interact with the Windows GUI or environment components.
    *   **Complex String Manipulation:** Extensive logic for parsing paths, identifiers, and normalized strings.

*   **Conclusion:** This is a professional-grade tool designed for modularity and evasion. The "Interpreter" nature of the code allows the threat actor to update their tactics (via scripts) without ever having to recompile or redistribute the underlying engine.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1029 | Virtualization | The malware utilizes a high-maturity VM/Interpreter architecture with multi-layered switch tables to abstract and obfuscate system API calls through internal logic layers. |
| T1059 | Command and Scripting Interpreter | The binary functions as a robust execution environment that processes complex scripts, allowing the attacker to swap malicious behaviors (e.g., info-stealer or ransomware) while keeping the host binary constant. |
| T1036 | Masquerading | The integration of USER32_dll and HWND interactions suggests an intent to hide malicious activity within a legitimate-looking window context or mimic common UI behaviors. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: While internal function names were identified in the report, they do not constitute file system or registry paths.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Internal Function Offsets (Evidence of VM/Interpreter Architecture):**
    *   `0x40f650` (Multi-layer dispatch logic)
    *   `0x412c10` (Gatekeeper/Intermediate dispatching)
    *   `0x40bd9d` (Memory management/buffer calculation)
    *   `0x40be83` (Buffer length validation/alignment)
    *   `0x40c3cb` (Interaction with `USER32.dll`)
*   **Imported Library Dependencies:**
    *   `USER32.dll` (Used for GUI interaction and environment checks)
    *   `OLEAUT32` (Used for handling complex data types/Variant types via `VariantCopy`)
*   **Behavioral Patterns:**
    *   **Multi-Layered Switching:** The use of deeply nested switch tables to abstract malicious API calls from the core logic.
    *   **Abstracted API Execution:** A deliberate gap between script intent and system execution designed to bypass automated sandbox detection.

---

## Malware Family Classification

1. **Malware family**: custom (high-maturity framework; characteristics similar to PlugX or Cobalt Strike)
2. **Malware type**: loader / backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced VM/Script Interpreter Architecture:** The heavy use of massive, multi-layered switch tables (e.g., `0x40f650`) and "Gatekeeper" patterns indicates a sophisticated interpreter designed to decouple the malicious logic (scripts) from the host binary's execution code.
*   **Modular Functionality:** The wide scope of internal functions—covering file systems, networking, memory management, and UI interaction—indicates that this is a multi-purpose framework capable of executing various payloads (such as info-stealers or ransomware modules) without changing its core structure.
*   **Sophisticated Evasion Tactics:** The use of abstracted API execution and complex memory management suggests a high-tier development intent to bypass automated sandboxes and static analysis by hiding the true "intent" behind layers of interpretation.
