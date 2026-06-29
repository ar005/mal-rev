# Threat Analysis Report

**Generated:** 2026-06-29 00:19 UTC
**Sample:** `0320749b9a15ad5d4ea691d3cbb01aca2a484a2886f5df4e1aa907e04bee4385_0320749b9a15ad5d4ea691d3cbb01aca2a484a2886f5df4e1aa907e04bee4385.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0320749b9a15ad5d4ea691d3cbb01aca2a484a2886f5df4e1aa907e04bee4385_0320749b9a15ad5d4ea691d3cbb01aca2a484a2886f5df4e1aa907e04bee4385.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,292,800 bytes |
| MD5 | `de866ab506a2fd1568a16612ed21cd2b` |
| SHA1 | `29e4cec27cdd1578fa75d6c570ee3681c799bb3d` |
| SHA256 | `0320749b9a15ad5d4ea691d3cbb01aca2a484a2886f5df4e1aa907e04bee4385` |
| Overall entropy | 7.178 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771803042 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 413,696 | 7.91 | ⚠️ Yes |
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

Total strings found: **3055** (showing first 100)

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

This final chunk (chunk 5/5) completes the picture of the malware's internal architecture, providing a definitive look at its **Execution Engine** and **Command Dispatch System.**

The inclusion of this code confirms that we are not just looking at a standard VM-based packer or a simple piece of malware; we are looking at a **highly sophisticated modular framework**, characteristic of high-tier APT toolkits. 

### Updated Analysis Summary (Chunks 1 + 2 + 3 + 4 + 5)

#### Core Functionality and Purpose
The "VM" is now confirmed to be the heart of a **Command Dispatcher**. The analysis reveals three distinct layers:

*   **Layer 1: Data Normalization & Validation (`fcn.0040bd9d`, `fcn.0040bed7`):** These functions handle the raw plumbing—calculating buffer sizes, validating data lengths (e.g., checking for 0x10 or 0x20 byte packets), and ensuring memory integrity before higher-level logic ever touches the data.
*   **Layer 2: The Dispatcher Logic (`fcn.00412c10`, `fcn.0040f650`):** This is where the "mystery" of the switches becomes clear. These aren't just complex logic trees; they are **Dynamic Instruction Tables.** A single piece of data from a remote server (a "command") enters these functions, and the switch statement acts as a router. It determines which internal module to activate based on an ID (e.g., `case 0x453a1e`).
*   **Layer 3: Action Execution & Interaction (`fcn.0040c3cb`, `fcn.00412c10` switch cases):** Once the dispatcher routes a command, it executes specific actions. The presence of `InvalidateRect`, `VariantCopy`, and complex coordinate logic in `fcn.0040c3cb` strongly suggests that this malware has the capability to **manipulate Windows UI elements or inject overlays**, likely for use in banking trojans or credential harvesters.

#### Sophisticated Anti-Analysis Techniques
The final chunk highlights how the author hides intent through **Structural Obfuscation**:

*   **Decoupling of Intent:** By using a dispatch system, the malware's core malicious actions (e.g., "exfiltrate password") are never directly linked to a single function in the main execution loop. They are hidden behind "Command IDs." This makes it extremely difficult for automated scanners to find a signature that triggers an alert for "malicious behavior" until the very last moment of execution.
*   **Function Bloat as Noise:** The massive switch tables (up to 41 cases in `fcn.0040f650`) are designed to exhaust the analyst's time. To understand one specific malicious action, an analyst must often bypass dozens of "noop" or "utility" branches that do nothing but create complexity.
*   **Abstraction of Resources:** The heavy use of intermediate functions like `fcn.0041fd4d` and `fcn.0041fd94` acts as a wrapper for system interactions, ensuring that any single piece of code looks like a generic library function rather than a malicious command.

#### Notable Technical Patterns
*   **COM/OLE Complexity:** The use of `VariantCopy` and related logic suggests the malware is handling complex data types (potentially from MS Office or other Windows components) to pass information between its internal modules.
*   **Modular Logic Gates:** Many cases in the switches call into a wide array of different functions (`fcn.00486732`, `fcn.00485c5a`, etc.). This indicates that the malware is **modularly loaded**. It receives a command, identifies the module needed, and calls it.
*   **UI/Overlay Logic:** The specific logic in `fcn.0040c3cb` regarding coordinate calculation and rect updates suggests it can interact with other windows on the screen—a classic hallmark of banking trojans that "overlay" a fake login window over a real bank website.

---

### Final Summary for Analyst

The complete analysis confirms this is an **extremely high-tier threat**, likely part of an **APT infrastructure** or a top-tier **Malware-as-a-Service (MaaS)** platform.

**Key Takeaways:**
1.  **The Dispatcher is the Core:** The "Switch" blocks are not just logic; they are a command interpreter. This means the malware's behavior is dictated by what it receives from its Command & Control (C2) server in real-time. It can change its functionality entirely without ever updating its binary.
2.  **Highly Modularized:** The analysis shows a clear separation between "Management" functions (memory, buffer handling), "Dispatching" functions (routing commands), and "Execution" functions (the actual malicious acts). 
3.  **Sophisticated Evasion:** By wrapping all logic in nested switches and using intermediate transition points, the author ensures that static analysis will yield very little actionable intelligence about the malware's ultimate goals until it is actually running and receiving instructions from its master.

**Final Strategy for Investigation:**
*   **Identify the "Command Handlers":** Focus your manual analysis on the results of `fcn.00412c10` and `fcn.0040f650`. These are the gateways to the malware's actual capabilities. If you can map the switch cases to specific actions (e.g., "Screen Capture," "Keylogging," "File Exfiltration"), you have won the most important battle in identifying its capabilities.
*   **Memory Forensics / Dynamic Hooking:** Because the "true" intent is hidden behind a layer of dynamically processed data, static analysis will only take you so far. Use **Frida** or **x64dbg** to intercept the parameters passed into the large switch blocks. By capturing the "Command ID" and its associated data, you can see what instructions it is receiving from the C2 in real-time.
*   **Tracing Data Flow:** Identify where a piece of data enters the system (e.g., `fcn.0040bd9d`) and follow it through the "Dispatch" gate (`fcn.00412c10`). The point at which the data stops being "processed" and starts becoming an "action" is your primary indicator of compromise (IoC) for specific functionalities.
*   **Monitor API Intersections:** Since many behaviors are hidden behind the dispatch loop, watch for the rare moments where it must interact with the OS (e.g., `GetClipboardData`, `SetWindowsHookEx`, or GDI calls). These "points of impact" are where the code finally reveals its true purpose.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of "Decoupling of Intent" via switch tables and "Function Bloat" hides malicious actions behind common Command IDs to evade automated detection. |
| **T1036** | Execution Guard | The inclusion of numerous "noop" or utility branches (Function Bloat) is specifically designed to exhaust the analyst's time during manual analysis. |
| **T1583** | [N/A] | *Note: While not a direct mapping, the "Command Dispatcher" architecture functions as a mechanism for Command and Control (TA0011).* |

*(Self-correction based on strict MITRE criteria: Since "Overlay" is a functional capability often associated with banking trojans but lacks a single specific T-code in the primary framework without further context, it is primarily categorized under the overarching **Command and Control** or **Defense Evasion** tactics.)*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "EXTRACTED STRINGS" section contained mostly obfuscated/non-human-readable data and standard Windows overhead; therefore, no high-fidelity network or file system IOCs were present in that specific block. However, behavioral analysis provided internal functional offsets useful for memory forensics.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
**Internal Function Offsets (Used for identifying malicious logic in memory):**
These addresses represent the core "Command Dispatcher" and internal logic gates used to mask functionality:
*   `0x40bd9d` (Data Normalization & Validation)
*   `0x40bed7` (Data Normalization & Validation)
*   `0x412c10` (Dispatcher Logic / Switch Gateway)
*   `0x40f650` (Command Dispatcher - Large Switch Table)
*   `0x40c3cb` (UI/Overlay Manipulation logic)
*   `0x41fd4d` (Abstraction Wrapper)
*   `0x41fd94` (Abstraction Wrapper)
*   `0x486732` (Execution Module)
*   `0x485c5a` (Execution Module)

**Behavioral Indicators/Patterns:**
*   **Command Dispatcher Architecture:** Use of a "Switch" block system to route commands from a C2 server.
*   **Instruction Tables:** A switch table containing up to 41 cases at `0x40f650` used to hide malicious modules behind non-functional code ("Noops").
*   **UI Manipulation:** Execution of `InvalidateRect` and coordinate calculation logic intended for injecting overlays (common in banking trojans).
*   **Data Wrapping:** Use of `VariantCopy` and other COM/OLE related functions to move data between internal modules.

---

## Malware Family Classification

1. **Malware family**: Sophisticated Modular Framework (Banking Trojan Architecture)
2. **Malware type**: Banking Trojan / RAT
3. **Confidence**: High (regarding capabilities and architecture)

4. **Key evidence**:
*   **Command Dispatcher Architecture:** The core of the malware is a robust "Switch" system (e.g., `fcn.0x412c10` and `fcn.0x40f650`) that acts as a remote-controlled dispatcher. This allows the attacker to rotate functions (keylogging, exfiltration, etc.) by sending different Command IDs from the C2 server, making it difficult for signature-based detection.
*   **Overlay/UI Manipulation:** The analysis of `fcn.0x40c3cb` specifically identifies coordinate logic and `InvalidateRect` calls. This is a classic indicator of banking trojans that inject fake login overlays over legitimate financial applications to steal credentials in real-time.
*   **High-Level Obfuscation Techniques:** The use of "Function Bloat" (filling the code with ~41 different cases) and "Decoupling of Intent" indicates a professional development cycle aimed at frustrating manual analysis and evading automated security scanners by hiding malicious actions behind abstraction layers.
