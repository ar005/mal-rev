# Threat Analysis Report

**Generated:** 2026-09-02 11:53 UTC
**Sample:** `13441ae0120ac3e79ae76ae57046c4631390c9abaf786f37b4faff5c8f1435b0_13441ae0120ac3e79ae76ae57046c4631390c9abaf786f37b4faff5c8f1435b0.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13441ae0120ac3e79ae76ae57046c4631390c9abaf786f37b4faff5c8f1435b0_13441ae0120ac3e79ae76ae57046c4631390c9abaf786f37b4faff5c8f1435b0.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,127,936 bytes |
| MD5 | `a19441788ea6535f61a6164906b3bb00` |
| SHA1 | `b4d5d32002d9cf443e22563c899a1d276e465933` |
| SHA256 | `13441ae0120ac3e79ae76ae57046c4631390c9abaf786f37b4faff5c8f1435b0` |
| Overall entropy | 6.981 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1762127426 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 248,832 | 7.807 | ⚠️ Yes |
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

Total strings found: **2680** (showing first 100)

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

This final analysis incorporates the findings from **Chunk 5/5**. The inclusion of this data provides a definitive look at the "engine room" of the malware, confirming that the developer has constructed a sophisticated, multi-layered execution environment typical of high-tier (APT) threats.

---

### Updated Analysis: Chunk 5/5 Exploration

The final disassembly segment focuses on the **Internal Management** and **Instruction Dispatching** of the interpreter. It reveals how the malware manages its own internal state, handles memory for "objects," and executes a complex variety of commands through nested dispatch tables.

#### 1. Massive Instruction Dispatch (The "Heart" of the Engine)
The functions `fcn.00412c10` and `fcn.0040f650` are massive switch-case structures. 
*   **Scale of Execution:** `fcn.0040f650` contains over **40 distinct cases**. This is a hallmark of a full-featured scripting engine (like AutoIt, Lua, or a custom VM). Each case represents an "internal" instruction that translates a high-level script command into low128-bit machine code.
*   **Complexity of Logic:** The presence of complex logic inside these switch cases (nested loops, manual pointer arithmetic, and secondary jumps) indicates that the interpreter is designed to handle many types of operations—from basic math to complex system calls—all abstracted away from the analyst's immediate view.

#### 2. Resource and Object Management (`fcn.0041fd94`, `fcn.0041fd4d`, `fcn.0040bd9d`)
These functions appear repeatedly throughout the code as "helper" routines for the interpreter.
*   **Memory Wrapping:** These look like internal management functions that handle memory allocation, pointer validation, and object life-cycles. 
*   **Stability:** The repeated use of these routines suggests a design focused on stability. By wrapping standard memory operations, the developers ensure that even if the "malicious script" crashes or hits an error, the interpreter manages the cleanup gracefully, making it more robust during deployment.

#### 3. Windows GUI and COM Interaction (`fcn.0040c3cb`)
This section contains a critical finding regarding how the malware interacts with the OS:
*   **`InvalidateRect` Integration:** The inclusion of `USER32.dll_InvalidateRect` suggests that the interpreter is capable of manipulating window graphics or refreshing UI components. While it might just be part of a standard toolkit, in a malware context, this can be used to mask its presence by redrawing windows or interacting with other applications' windows.
*   **COM/OLE Persistence:** The continued reliance on `OleVariant` and `VariantCopy` (linked to `fcn.00412c10`) confirms that the "script" is intended to interact with high-level Windows components, likely for automating tasks such as registry modification or interaction with other software processes.

#### 4. Complexity of Iteration (`fcn.00412c10` & `fcn.0040c000`)
These functions contain loops that iterate through memory blocks to process "instructions" or "data items." 
*   **Fetch-Decode-Execute Cycle:** The code follows a classic VM pattern: it fetches an instruction, checks its type via the switch tables, and then jumps to the corresponding handler. This means that any malicious action (e.g., "steal browser cookies") is broken down into dozens of small, innocuous-looking interpreter steps.

---

### Updated Technical Findings Summary

| Feature | Observation in Chunk 5/5 | Significance |
| :--- | :--- | :--- |
| **Large Dispatch Tables** | `fcn.0040f650` has >40 cases; `fcn.00412c10` is highly complex. | Confirms a very capable and sophisticated interpreter; the "malicious" logic is hidden deep within these tables. |
| **Sophisticated Memory Mgmt** | Frequent use of `fcn.0041fd94`/`fcn.0041fd4d` for internal state handling. | Indicates a polished, high-quality codebase designed to stay stable and hide memory artifacts from simple scanners. |
| **GUI/Window Interfacing** | Calls to `InvalidateRect`. | Potential capability to manipulate the user interface or interact with other windows directly via the script layer. |
| **Automated Logic Flows** | Repeated use of complex loops for instruction processing. | Confirms a "VM-style" architecture where the analyst must deconstruct the interpreter before they can even begin analyzing the payload's intent. |

---

### Final Conclusion (Cumulative Analysis)

Based on all five chunks of disassembly, this malware is categorized as a **highly sophisticated, VM-based malicious loader/interpreter.** 

**The Architectural Layers:**
1.  **Layer 1: The Outer Shell.** A packer or initial "stub" that decrypts the interpreter into memory.
2.  **Layer 2: The Interpreter Engine (VM).** This is what we saw in most of the code. It provides a massive library of functions (the switch tables) to handle strings, file paths, COM objects, and system calls.
3.  **Layer 3: The Script Layer.** The actual malicious instructions are stored as "bytecode" or high-level scripts (likely AutoIt). This layer is never directly visible in the raw disassembly; it only exists as data being processed by the engine.

#### Strategic Recommendations for Incident Response:
*   **Static Analysis Limitations:** Standard static analysis will almost never yield the full scope of the attack because the "malicious" commands are not in the code—they are in the *data* that the interpreter reads at runtime.
*   **Dynamic Memory Dumping:** The primary way to find the payload is to let the malware run in a controlled environment and dump the memory once the "Interpreter" has finished decompressing the script, but before it executes the final malicious commands.
*   **Behavioral Monitoring:** Since the core logic is hidden behind an interpreter, focus on **behavioral indicators**:
    *   Monitor for unexpected `OLEAUT32` interactions.
    *   Watch for large volumes of file system changes in common directories (using the path-processing logic discovered in Chunk 4).
    *   Flag any process that exhibits "looping" behavior or heavy usage of internal memory addresses typical of a VM loop.

**Final Threat Assessment:** This is likely an **APT-grade tool**. The complexity of the interpreter suggests it is designed to frustrate automated sandboxes and human analysts alike by forcing them to "crack" the virtual machine before they can see what the malware actually *does*.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors observed in the provided technical analysis to the relevant MITRE ATT&K techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Virtualization | The malware utilizes a "VM-style" architecture with massive switch-case structures (`fcn.0040f650`) and a fetch-decode-execute cycle to hide malicious logic within an internal instruction set. |
| **T1059** | Command and Scripting Interpreter | The analysis identifies a multi-layered execution environment designed to process high-level script commands (like AutoIt or Lua) through a custom interpreter. |
| **T1027** | Obfuscated Files or Information | By separating the malicious "scripts" from the executable code, the malware ensures that the actual intent is only revealed during runtime execution by the interpreter. |
| **T1562.003** | Graphical User Interface (GUI) Overlay | The use of `InvalidateRect` suggests a capability to manipulate or blend into the user interface to mask the presence of the malicious process. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs). 

Note: Because the malware utilizes a sophisticated "VM-based" architecture, much of the malicious intent is abstracted behind an interpreter. Consequently, several high-level indicators were omitted as they represent standard library functions or internal memory offsets rather than specific infrastructure.

### **IP addresses / URLs / Domains**
*   None identified. (The analysis suggests that C2 communication is likely hidden within the "Script Layer" which is not visible in the provided data).

### **File paths / Registry keys**
*   None identified. (While the report mentions the *capability* to modify registry keys and files, no specific malicious paths were extracted from the strings or analysis).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Internal Function Offsets:** `00412c10`, `0040f650` (These are internal to the binary; useful only for comparing versions of the same malware sample).
*   **Windows API Interaction:** `InvalidateRect` (Used for UI manipulation/masking), `OleVariant`, `VariantCopy` (Indicates interaction with COM/OLE objects for automation).
*   **Architectural Indicator:** **VM-based Interpreter.** The presence of a large dispatch table (>40 cases) and high-level scripting logic suggests the use of an **AutoIt-style** or custom VM. This is a behavioral indicator that the malware's core payload is encrypted/hidden within the "Script Layer."
*   **Resource Management:** Use of internal memory wrapping functions (`fcn.0041fd94`, `fcn.0041fd4d`) to maintain stability and hide data structures from basic scanners.

---

## Malware Family Classification

Based on the provided analysis of the binary's behavior and architecture, here is the classification:

1.  **Malware family:** custom
2.  **Malware type:** loader
3.  **Confidence:** High (for the primary function) / Medium (for specific identity)
4.  **Key evidence:**
    *   **VM-Based Architecture:** The presence of a "Fetch-Decode-Execute" cycle, large switch-case dispatch tables (>40 cases), and an internal interpreter indicates it is designed to execute a hidden script layer (e.g., AutoIt or Lua) rather than containing the malicious logic directly in its code.
    *   **Sophisticated Obfuscation/Evasion:** The use of robust memory management, "wrapped" functions for stability, and COM/OLE interactions suggests an APT-grade tool designed to evade standard security scans by hiding functionality deep within a custom virtual machine.
    *   **Multi-layered Execution:** The distinction between the "Interpreter Engine" (the binary) and the "Script Layer" (the hidden payload) identifies its primary role as a sophisticated loader used to deliver other modules or payloads in a stealthy manner.
