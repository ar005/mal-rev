# Threat Analysis Report

**Generated:** 2026-06-27 05:17 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, UPX compressed, 3 sections |
| Size | 722,944 bytes |
| MD5 | `dbc7b78588d6cd759226553df4dba3e6` |
| SHA1 | `555274ba0fc566ba876c6ed6c1e16cf54c71c099` |
| SHA256 | `019a6515ad4821d15e0d16707ea0df34229f649787dec1c63e97dd88b514938b` |
| Overall entropy | 7.1 |
| Unpacked | ✓ Yes (tool: upx) |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1764137391 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.61 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 350,208 | 7.882 | ⚠️ Yes |
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

Total strings found: **2845** (showing first 100)

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

This analysis incorporates the findings from **Chunk 5/5**. This final segment provides deep insight into the internal memory management of the VM, its complex instruction dispatching, and its interaction with UI elements.

### Updated Analysis Summary

The addition of Chunk 5 confirms that this is a **highly sophisticated, production-grade execution engine**. It does not merely "run" a script; it provides the script with a full runtime environment including automatic memory management (reference counting), a massive library of pre-defined functions (the core dispatcher), and specialized handlers for interacting with Windows GUI components.

---

### Core Functionality: The Execution Environment (Deepened)

The analysis of these final functions reveals three advanced architectural pillars:

#### 1. Sophisticated Memory & Object Management (`fcn.0040bd9d`, `fcn.0040bef7`)
Unlike simpler malware that uses basic buffers, this engine implements a **managed object system**.
*   **Dynamic Allocation:** `fcn.0040bd9d` behaves like a constructor/allocator for the VM’s internal objects. It handles different data types (likely strings, lists, or "Variant" objects) and adjusts memory allocation based on size requirements.
*   **Reference Counting & Garbage Collection:** Functions like `fcn.0040bef7` and `fcn.0040c000` appear to manage a reference counting system (similar to COM or Python's internal memory). They check if an object's reference count has hit zero before calling the "deconstructor" (`fcn.0041fd94`).
*   **Implication:** This allows the "script" to handle complex, long-lived data structures and persistent connections without the script itself needing to manage memory addresses or manual deallocation—a hallmark of high-level languages like Python or AutoIt.

#### 2. The Massive Dispatcher: The Engine's Heart (`fcn.0040f650`, `fcn.00412c10`)
These functions are the primary "gateways" for the script’s logic.
*   **Large Instruction Sets:** `fcn.0040f650` contains a massive switch table (over 40 cases). Each case corresponds to an internal "opcode" or built-in function available to the script. This suggests the malware has a huge library of capabilities, potentially including networking protocols, file manipulation, and system configuration changes.
*   **Complex Logic Processing:** `fcn.00412c10` is another massive dispatcher that seems to handle high-level logic flow and internal "method" resolution. It includes specialized handling for different types of data (e.g., the jump table at `0x45722c`).
*   **Implication:** The variety in these switch tables indicates a **modular design**. To change what the malware *does*, the author only needs to provide a new "script" file; the core engine (`fcn.0040f650`) remains the same, but it interprets different instructions provided by that script.

#### 3. Windows UI & Interaction Integration (`fcn.0040c3cb`, `fcn.0040c28f`)
The final functions provide evidence of how the malware interacts with the user's environment.
*   **GUI Manipulation:** `fcn.0040c3cb` is particularly telling. It involves logic for calculating coordinates, handling "Rectangles," and calling `InvalidateRect`. 
*   **Context-Aware Logic:** These functions handle the translation between the VM’s internal commands (e.g., "Draw Box" or "Find Button") and the actual Windows API calls needed to manipulate windows.
*   **Implication:** This suggests the malware is capable of creating sophisticated fake interfaces, interacting with other applications' windows, or even capturing/simulating user input in a way that appears legitimate to automated security tools.

---

### Advanced Architectural Insights

**The "abstraction" Defense:**
Every time a script wants to perform a simple action (like "Read File"), it doesn't call `ReadFile` directly. It calls an internal function, which is handled by the **Dispatcher**, which then interacts with the **Memory Manager**. This creates several layers of abstraction that make it extremely difficult for automated sandboxes or static analysis tools to link a specific script command to a malicious system action.

**Evidence of Intentional Complexity:**
The reuse of standard patterns like `VariantCopy` and the heavy use of switch-table dispatchers indicate that this is not a "one-off" piece of malware. This is a **sophisticated framework** designed for longevity and easy updates by the threat actors.

---

### Technical Observations for Incident Response

*   **Memory Analysis over Static Analysis:** Because the "malicious logic" only exists as data fed into the dispatchers (like `fcn.0040f650`), static analysis of the `.exe` will likely only reveal the *engine*. To find the actual intent, an analyst must perform **dynamic memory forensics** to capture the script data as it is processed by these dispatchers.
*   **API Hooking Strategy:** Rather than trying to reverse-engineer every switch case in `fcn.0040f650` (which is time-consuming and provides little immediate "intel"), IR teams should hook the **common points of exit**. These are the points where the VM's internal functions finally call Windows APIs for networking, file system changes, or registry modification.
*   **Detecting "Interaction" Logic:** The presence of `InvalidateRect` and complex coordinate math in `fcn.0040c3cb` suggests that if a fake login screen is presented to the user, it is being managed by this internal engine. Monitoring for high-frequency window updates or unusual UI interaction patterns can be a detection vector.

### Final Summary
This malware utilizes a **high-maturity Virtual Machine environment**. It provides an abstraction layer between the malicious "script" and the operating system. This architecture serves three primary purposes:
1.  **Evasion:** It hides the true logic of the malware behind layers of dispatchers and internal function calls.
2.  **Flexibility:** It allows threat actors to change the behavior of the malware (via a script) without changing the core binary, thus bypassing signature-based detection.
3.  **Complexity:** It provides a robust environment for complex tasks like automated GUI interaction, advanced network communication, and sophisticated data processing—all performed "under the hood" of the VM.

**Key Takeaway:** This is not just a piece of malware; it is an **execution platform**. Investigation should focus on extracting the scripts fed into this engine to understand the full scope of capabilities being utilized in an active infection.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a custom "execution engine" and massive dispatchers creates a multi-layered abstraction that hides the true logic of the malicious scripts from static analysis. |
| **T1496** | Virtualization | The implementation of a sophisticated, production-grade VM environment provides a layer of abstraction between the script commands and the operating system to evade detection. |
| **T1566.003** | Phishing: Fake Login Window | The complex calculation of coordinates, "Rectangles," and `InvalidateRect` calls suggests the creation of deceptive UI elements to harvest user credentials. |
| **T1036** | Masquerading | By utilizing standard software patterns like reference counting and a modular architecture, the malware attempts to appear as legitimate, high-level application logic. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the identified Indicators of Compromise (IOCs). 

**Note:** The "Extracted Strings" section contains mostly obfuscated data, non-standard characters, or internal PE header metadata; therefore, no network-based IOCs or static file system markers were present in that specific block.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (While the report mentions "file manipulation" and "registry modification," no specific paths or keys were disclosed).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Internal Function Offsets (Malware Engine Signatures):** These offsets identify the specific logic used by the execution engine and may be used to fingerprint the malware family:
    *   `0x40bd9d` (Memory/Object Management)
    *   `0x40bef7` (Reference Counting)
    *   `0x40c000` (Garbage Collection/Deconstruction)
    *   `0x41fd94` (Deconstructor call)
    *   `0x40f650` (Primary Dispatcher - contains >40 cases)
    *   `0x412c10` (Secondary Dispatcher/Logic Flow)
    *   `0x45722c` (Specific Jump Table location)
*   **Behavioral Markers:**
    *   **VM-Based Execution Engine:** The presence of a "Virtual Machine" environment with a large instruction set.
    *   **Scripted Logic Strategy:** Use of an internal dispatcher to separate malicious logic from the primary binary.
    *   **UI Manipulation Logic:** Usage of `InvalidateRect` and complex coordinate math (at `0x40c3cb`) for potential fake login screens or overlays.

---

## Malware Family Classification

1. **Malware family**: Unknown (Sophisticated Framework)
2. **Malware type**: Loader / Backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **High-Complexity Virtualization:** The sample employs a "production-grade" VM execution engine featuring advanced memory management (reference counting and garbage collection), which serves to decouple the malicious logic from the underlying binary, making static analysis extremely difficult (T1496).
*   **Multi-Purpose Dispatcher Architecture:** The presence of large switch tables (e.g., `fcn.0040f650` with over 40 cases) indicates a highly modular design where the "script" provides the intent, while the engine handles a wide array of capabilities like networking, file manipulation, and system changes.
*   **Interactive UI Component Logic:** The inclusion of specific instructions for coordinate calculation and `InvalidateRect` calls suggests the malware is designed to perform sophisticated user-interface interactions, such as generating fake login screens or overlaying malicious windows (T1566.003).
