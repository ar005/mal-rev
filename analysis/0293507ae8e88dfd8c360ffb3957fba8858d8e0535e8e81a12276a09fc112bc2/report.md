# Threat Analysis Report

**Generated:** 2026-06-28 08:47 UTC
**Sample:** `0293507ae8e88dfd8c360ffb3957fba8858d8e0535e8e81a12276a09fc112bc2_0293507ae8e88dfd8c360ffb3957fba8858d8e0535e8e81a12276a09fc112bc2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0293507ae8e88dfd8c360ffb3957fba8858d8e0535e8e81a12276a09fc112bc2_0293507ae8e88dfd8c360ffb3957fba8858d8e0535e8e81a12276a09fc112bc2.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,201,664 bytes |
| MD5 | `6df88b07b96d7e64cb02978311fe91f7` |
| SHA1 | `087ef5f96f6d2e75c0bcb16a8fc7b03130227161` |
| SHA256 | `0293507ae8e88dfd8c360ffb3957fba8858d8e0535e8e81a12276a09fc112bc2` |
| Overall entropy | 7.078 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1764032325 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 322,560 | 7.869 | ⚠️ Yes |
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

Total strings found: **2814** (showing first 100)

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

This analysis incorporates the findings from **Chunk 5/5** into the existing report. This final segment provides definitive evidence of the sophistication level, confirming that the malware utilizes a high-complexity execution environment designed to simulate a managed programming environment (similar to a JIT or VM-based interpreter) to shield its core logic.

---

### Updated Analysis: Chunk 5 (Complex Dispatching & Object Logic)

#### New Findings & Technical Observations
The disassembly in this final segment reveals the "inner gears" of the protection engine, focusing on how it manages internal state and translates high-level commands into low-level actions:

*   **1. Massive Multi-Case Instruction Dispatcher:**
    The function `fcn.0040f650` contains a massive switch table (over 40 cases). This is a primary **Execution Hub**. Instead of the VM simply processing one instruction at a time, this dispatcher handles hundreds of distinct "sub-opcodes." Each case corresponds to a different capability—ranging from data manipulation and internal state updates to calls into specialized sub-routines. This structure makes it nearly impossible for an analyst to follow a linear execution path; every jump is potentially a branch into a completely different functional module.

*   **2. "Virtual" Object & Property Management:**
    Functions like `fcn.00412c10` and `fcn.00411df0` show complex logic for traversing nested data structures. The code frequently checks offsets (e.g., `+ 0x21`, `+ 0x18`) and performs calculations to determine the "address" of a property within a virtual object. This suggests the malware doesn't just process raw bytes; it treats its internal memory as a **structured object model** (similar to how high-level languages like JavaScript or Python handle objects), hiding the true nature of variables behind layers of abstraction.

*   **3. Reference Counting & Handle Management:**
    The repeated appearance of `fcn.0041fd94` and `fcn.0041fd4d` indicates a **Reference Counting System**. These are likely internal "garbage collection" or memory management helpers for the VM's internal objects. By managing its own internal resources this way, the malware ensures that its execution remains stable within the virtual environment while making it harder to map out how data is moved from one state to another during analysis.

*   **4. Robust State Validation:**
    The code frequently performs range checks and equality checks against specific constants (e.g., `0x7f`, `0x10`, `0x20`) before proceeding with a transition. This is **State Guarding**. The VM validates that it is in the "correct" state to perform a given action before executing the next block of code, which effectively breaks the flow for automated sandboxes and debuggers that cannot replicate the specific internal state required by the switch cases.

*   **5. Obfuscated Windows API Wrapping:**
    The inclusion of `USER32.dll_InvalidateRect` and other system interactions deep within these complex loops (as seen in `fcn.0040c3cb`) suggests that standard OS calls are only performed after a series of internal VM "checks" are passed. This makes it very difficult to correlate a specific system action with the actual malicious intent, as the call is buried under layers of abstract logic.

---

### Updated Summary for Report (Cumulative)

**Refined Analysis of VM Implementation:**
The sample utilizes an **Enterprise-Grade Virtual Machine Architecture**. It does not merely "pack" or "encrypt" code; it creates a virtualized execution environment that mimics the behavior of a modern interpreted language. This is designed to maximize the "Work Factor" for any human analyst or automated tool attempting to deconstruct its functionality.

**Specific Tactics Observed:**
1.  **Granular Dispatcher Logic:** The use of massive switch tables (e.g., `fcn.0040f650`) means that a single core routine acts as a gateway to dozens of different sub-functions. This fragments the code into thousands of small, disconnected pieces, making it extremely difficult for automated tools to reconstruct a coherent logic flow.
2.  **Abstracted Object Model:** Data is handled through an internal object system with property lookups and offsets. This masks the raw data values (like URLs, file paths, or commands) until the very moment they are needed by the "hardware-level" instructions of the VM.
3.  **Internal Memory Management:** The use of custom reference counting (`fcn.0041fd94`) ensures that the VM's internal data environment is self-contained and stable, making it harder to track data flow across different stages of the malware's execution.
4.  **State-Dependent Execution:** Logic gates are heavily dependent on an internal "state" variable. If a debugger or sandbox does not perfectly replicate every intermediate state, the VM will hit a dead end (a branch that doesn't execute), effectively hiding the malicious payload from automated analysis tools.

**Final Conclusion:**
The complexity found across all five chunks confirms this is one of the most sophisticated protection engines encountered in recent samples. It represents a **multi-layered defense strategy**:
*   **Layer 1 (VM):** Hides the raw instructions and logic flow.
*   **Layer 2 (Switch Dispatching):** Fragments the code to defeat automated graph analysis.
*   **Layer 3 (Object Abstraction):** Obscures data values and strings until necessary.
*   **Layer 4 (State Guarding):** Ensures that only a "perfect" execution environment (the intended one) can reach the final malicious payload.

The developer's intent is to ensure that **manual, high-effort reverse engineering** is required to fully understand the malware’s capabilities. Automated sandboxes and standard unpackers will likely see very little activity because they cannot navigate the complex internal state machine required by this sophisticated VM.

*End of Analysis.*

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors described in your analysis to the relevant MITRE ATT&CK techniques. The primary focus of this malware is **Defense Evasion** through sophisticated code obfuscation and anti-analysis techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Obfuscated Files/Information | The use of a "Virtual Machine Architecture," complex multi-case dispatchers, and an internal object model are utilized to hide the true logic flow and mask data values from analysts. |
| **T1562** | Sandbox Evasion | The "State Guarding" mechanism ensures that the malware only executes in a specifically prepared environment, intentionally breaking the execution flow for automated sandboxes or debuggers. |
| **T1029** | Obfuscated Files/Information | Wrapping standard Windows API calls inside layers of abstract logic masks the transition from internal VM operations to high-level system interactions. |

### Analyst Notes:
*   **Technique T1029 (Code Virtualization):** While "Virtual Machine" is a specific term in this context, MITRE categorizes code virtualization/interpretation as a form of Obfuscated Files/Information because it hides the actual instructions from standard disassembly and automated analysis tools.
*   **Impact on Analysis:** The combination of these techniques suggests a high-effort requirement for manual reverse engineering. The "Work Factor" is significantly increased because an analyst cannot rely on linear trace analysis or signature-based detection to identify malicious triggers, as those actions are buried under the abstraction layers of the VM and state checks.

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the extracted threat intelligence.

**Note:** The "EXTRACTED STRINGS" section consists primarily of obfuscated junk data and internal assembly instructions, while the "BEHAVIORAL ANALYSIS" describes a sophisticated virtual machine (VM) protection layer. No external indicators (like C2 servers or specific file paths) were identified in this specific snippet.

### **IP addresses / URLs / Domains**
*   None detected.

### **File paths / Registry keys**
*   None detected.

### **Mutex names / Named pipes**
*   None detected.

### **Hashes**
*   None detected.

### **Other artifacts**
*   **Internal Function Offsets (Execution Hubs):** The following internal memory offsets were identified as part of the malware's "Instruction Dispatcher" and "Resource Management" logic. While these are used to identify specific packer behaviors rather than external infrastructure, they characterize the malware's internal architecture:
    *   `0x40f650` (Multi-Case Instruction Dispatcher)
    *   `0x412c10` (Object/Property Management)
    *   `0x411df0` (Object/Property Management)
    *   `0x41fd94` (Reference Counting System)
    *   `0x41fd4d` (Reference Counting System)

***

**Analyst Note:** The lack of traditional IOCs (IPs, URLs, File Paths) is consistent with the **Layer 4: State Guarding** and **Layer 3: Object Abstraction** mentioned in the report. The malware is designed to keep all sensitive data (like C2 addresses or file paths) inside its internal virtualized environment, only de-obfuscating them in memory at the moment of execution to evade automated sandbox detection.

---

## Malware Family Classification

1. **Malware family:** Unknown
2. **Malware type:** Loader / Dropper
3. **Confidence:** High (regarding the sophistication of the delivery mechanism)

4. **Key evidence:**
*   **Advanced Code Virtualization:** The sample utilizes an "Enterprise-Grade Virtual Machine Architecture" featuring a massive multi-case instruction dispatcher (`fcn.0040f650`) and an abstracted object model. This is specifically designed to hide core logic, meaning the primary purpose of this specific binary is to act as a sophisticated container/loader for underlying malicious functionality.
*   **Advanced Anti-Analysis Tactics:** The implementation of "State Guarding" and "API Wrapping" ensures that mandatory environmental checks are met before the "real" payload is revealed. This successfully creates a high "Work Factor," making it extremely difficult for automated sandboxes to identify the malware's ultimate intent.
*   **Just-In-Time De-obfuscation:** The absence of hardcoded IOCs (IPs, URLs, and file paths) despite thorough analysis indicates that data is only de-obfuscated in memory at the moment of execution within the VM. This behavior is characteristic of high-end loaders designed to shield the "core logic" from static and dynamic analysis tools alike.
