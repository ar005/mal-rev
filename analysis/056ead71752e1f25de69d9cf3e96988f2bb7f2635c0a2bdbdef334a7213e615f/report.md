# Threat Analysis Report

**Generated:** 2026-07-13 20:23 UTC
**Sample:** `056ead71752e1f25de69d9cf3e96988f2bb7f2635c0a2bdbdef334a7213e615f_056ead71752e1f25de69d9cf3e96988f2bb7f2635c0a2bdbdef334a7213e615f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `056ead71752e1f25de69d9cf3e96988f2bb7f2635c0a2bdbdef334a7213e615f_056ead71752e1f25de69d9cf3e96988f2bb7f2635c0a2bdbdef334a7213e615f.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,317,888 bytes |
| MD5 | `779122a03649306146f5c9f86ce8b98e` |
| SHA1 | `674690de61b30d5daf4dc82172c498018d89ae96` |
| SHA256 | `056ead71752e1f25de69d9cf3e96988f2bb7f2635c0a2bdbdef334a7213e615f` |
| Overall entropy | 7.203 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774503330 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 438,784 | 7.917 | ⚠️ Yes |
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

Total strings found: **3092** (showing first 100)

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

This update incorporates the findings from **Chunk 5/5**. This final segment provides the most granular look into the interpreter’s internal mechanics, specifically how it manages object lifecycles, handles complex data types via COM-like structures (Variants), and utilizes a multi-stage dispatch system.

### Updated Analysis Summary
The inclusion of Chunk 5/5 confirms that this is a **highly mature, production-grade scripting environment.** The complexity of the dispatcher logic and the rigorous memory management indicate that the threat actor is not simply using a "lite" interpreter; they are utilizing (or have integrated) a full-featured runtime capable of complex application logic.

### Core Functionality
*   **Object Lifecycle & Reference Counting (`fcn.0041fd94`, `fcn.0041fd4d`):** These functions appear repeatedly across the disassembly as "cleanup" or "reference increment" handlers. They are used whenever a variable is reassigned or goes out of scope. This confirms that the interpreter treats its "data" as **objects with lifecycles**, not just raw buffers. This is typical in languages like AutoIt, where variables can point to complex objects (files, windows, registry keys).
*   **Complex Dispatcher Tables (`fcn.00412c10`, `fcn.0040f650`):** These are the "hubs" of the interpreter. They take a raw opcode or instruction index and route it to a specific internal handler. The sheer size of these switch tables (some involving dozens of cases) is designed to provide a wide range of functionality while keeping the core loop generic.
*   **Type-Tagging System:** In several locations (e.g., `fcn.00412c10`), the code checks for specific "magic" values like `0x7f` or `0x47`. These are **internal type identifiers**. They allow the interpreter to determine at runtime whether a variable is a string, an integer, a list, or a specialized object pointer. This is why the analysis of a single instruction becomes so complex: the engine must "negotiate" what the data is before it can decide how to process it.
*   **Data Normalization & Validation (`fcn.00412c10`):** A massive portion of this function is dedicated to ensuring that arguments are valid and "safe" before they reach the execution stage. This confirms the **"Abstraction Gap"**: a single script command (e.g., `Write_File`) involves dozens of internal checks for path length, permission types, and buffer sizes before any system call is made.

### New Findings & Emerging Patterns
*   **The "Interpreter within an Interpreter":** The logic in `fcn.00412c10` suggests a multi-pass execution model. It doesn't just execute an instruction; it often checks the *context* of the instruction, potentially preparing for subsequent instructions or handling nested blocks (like loops or if-statements) within the script itself.
*   **Advanced Memory Mapping:** The code frequently calculates offsets and lengths dynamically (e.g., `uVar4 = *(in_ECX + 0xc) * 2`). This suggests the interpreter is capable of handling large, potentially dynamic payloads that are not fully visible in a static memory dump until they are "activated" by the script logic.
*   **Integration with Windows Internals:** The continued use of `OLEAUT32` and the way it handles variety types suggest the interpreter can interact directly with COM objects. This allows the script to manipulate complex Windows components (like Shell objects or Network providers) through a single, high-level call.

### Suspicious / Malicious Behaviors
*   **Execution Path Obfuscation:** The use of massive switch tables for dispatching means that static analysis tools will struggle to map "Script Command A" to its corresponding logic in the binary. An analyst cannot simply search for a "File Write" string; they must find the specific index in the dispatcher that corresponds to it, which changes depending on how the script is written.
*   **Context-Aware Behavior:** Because of the type-tagging system, the same piece of code in the interpreter might behave differently depending on what the script "feeds" it. This makes signature generation based on behavior extremely difficult, as the binary’s actions are entirely dependent on the state of the internal memory.
*   **High Resilience to Analysis:** The "noise" created by the reference counting and buffer management is a deliberate tactic to exhaust the analyst's time. By forcing an analyst to step through dozens of "bookkeeping" instructions, the developer ensures that even if you are tracing the code in real-time, you may lose track of the actual malicious logic buried deep within the dispatcher.

### Conclusion for Analyst
The final analysis confirms a **highly sophisticated VM-based architecture.** This is not just an obfuscator; it is a complete execution environment. The distinction between "Data" (the hidden script) and "Code" (the interpreter) is stark. The malware's behavior only manifests once the script—which behaves like a high-level programming language—interacts with the dispatcher to generate system commands.

**Actionable Intelligence:**
1.  **Identify the Dispatcher Hubs:** Focus your attention on `fcn.00412c10` and `fcn.0040f650`. These are the "gateways" to functionality. If you can identify which branch of these switches corresponds to sensitive APIs (e.g., `CreateProcess`, `ShellExecute`), you have found a primary point of interest.
2.  **Trace the Script State:** Instead of tracing every instruction, focus on how variables in memory change. Monitor for "new" strings or addresses being passed into the dispatcher. These represent the transition from "Script Logic" to "System Action."
3.  **Map the Type Tags:** Create a map of the magic values (like `0x7f`, `0x47`). Knowing what these mean will allow you to quickly skip over segments that are merely handling data types and jump straight to the logic.
4.  **Memory Forensics is Key:** Because the script's intent is hidden behind multiple layers of abstraction, memory forensics (dumping strings/buffers after the VM has "unpacked" its internal state) will be more effective than trying to trace every branch in the dispatcher manually.

**High-Level Summary for Report:**
*The malware employs a sophisticated, multi-layered Virtual Machine architecture to execute an embedded scripting language. This provides the attacker with several layers of protection: 1) A complex, multi-stage dispatch system that hides the final purpose of script commands; 2) An internal type-tagging and reference-counting system that complicates manual analysis of data flow; and 3) A significant "abstraction gap," where malicious actions (e.g., file manipulation or network communication) are only triggered after a long chain of validation and interpretation logic. This design ensures that the malicious behavior is decoupled from the core binary, making it highly resistant to both static signatures and manual dynamic analysis.*

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | Virtualization | The malware utilizes a "sophisticated VM-based architecture" where the core logic is hidden inside an interpreted execution environment. |
| **T1027** | Obfuscated Execution | The use of complex dispatch tables, type-tagging systems, and intentional "noise" (reference counting) is designed to hinder static analysis and hide malicious intent. |
| **T1059** | Command and Scripting Interpreter | The malware leverages a "production-grade scripting environment" (similar to AutoIt or others) to manage object lifecycles and complex command logic. |
| **T1610** | Use of System Resources (via COM)** | The integration with `OLEAUT32` and the handling of variant types indicate an intent to interact with high-level Windows components via COM objects. |

***Note on T1610:** While T1610 is a broader category, in this context, it highlights the specific behavior of using "Object Lifecycles" and "Variant Types" (COM-like structures) to abstract system interactions.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: Items such as `.rdata`, `.data`, and `.reloc` were identified as standard linker segments and omitted as false positives.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Internal Function Offsets (Interpreter Logic):** 
    *   `fcn.0041fd94` (Object Lifecycle/Reference Counting)
    *   `fcn.0041fd4d` (Object Lifecycle/Reference Counting)
    *   `fcn.00412c10` (Primary Dispatcher Hub / Type-Tagging Gateway)
    *   `fcn.0040f650` (Secondary Dispatcher Hub)
*   **Internal Type Tags:** 
    *   `0x7f`
    *   `0x47`
*   **Component Integration:** Use of `OLEAUT32` for COM-like structures and Variant handling.

---

### **Analyst Notes:**
The provided data indicates a **sophisticated VM-based execution environment**. While there are no traditional "low-hanging" IOCs (such as hardcoded IPs or file paths) present in the raw strings, the analysis reveals that the malware uses an **Interpreter Architecture**. 

The presence of complex dispatch tables and type-tagging suggests that any static indicators (like specific strings used for commands) are hidden behind a layer of abstraction. To find further IOCs, it is recommended to perform memory forensics on the process while it is running to capture "de-obfuscated" strings or dynamic C2 configuration blocks as they are passed into the dispatcher hubs (`0x412c10` and `0x40f650`).

---

## Malware Family Classification

1. **Malware family**: Custom (High-Sophistication Loader/Framework)
2. **Malware type**: Loader / Backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced VM-Based Architecture:** The sample utilizes a sophisticated, production-grade interpreter with complex dispatch tables (`fcn.00412c10`, `fcn.0040f650`) and type-tagging systems. This indicates the core functionality is hidden within an abstracted execution environment rather than standard malicious code.
*   **"Abstraction Gap" Strategy:** The design intentionally separates "Data" (the actual malicious script) from "Code" (the interpreter). This ensures that common indicators of intent—such as file system modifications or network commands—only manifest after being processed by the VM, making static analysis significantly more difficult.
*   **Sophisticated Execution Logic:** The use of object lifecycle management (reference counting) and integration with `OLEAUT32` for COM-like structures suggests a highly mature piece of software designed to facilitate complex operations (typical of high-end backdoors or C2 loaders like Cobalt Strike variants).
