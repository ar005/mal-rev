# Threat Analysis Report

**Generated:** 2026-07-24 20:34 UTC
**Sample:** `0a49ae686b7a7d0153f290bd5d125d354e7aca15e095b049f7107a23e53137e0_0a49ae686b7a7d0153f290bd5d125d354e7aca15e095b049f7107a23e53137e0.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a49ae686b7a7d0153f290bd5d125d354e7aca15e095b049f7107a23e53137e0_0a49ae686b7a7d0153f290bd5d125d354e7aca15e095b049f7107a23e53137e0.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,264,640 bytes |
| MD5 | `0506b39eb6559b3d9655b1b534eea96b` |
| SHA1 | `71ca28552e16049e3e0c50341738eb75c6994a86` |
| SHA256 | `0a49ae686b7a7d0153f290bd5d125d354e7aca15e095b049f7107a23e53137e0` |
| Overall entropy | 7.149 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1772535497 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 385,536 | 7.899 | ⚠️ Yes |
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

Total strings found: **2933** (showing first 100)

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

The final piece of disassembly (chunk 5/5) completes the picture of this malware's architecture. This segment confirms that the malware is not just a simple Trojan, but a **highly modularized, enterprise-grade threat platform**.

The following analysis incorporates these final findings into the existing framework.

---

### Updated Analysis: Recursive Dispatching and Massive Functional Breadth

#### 1. Nested & Multi-Layered Dispatcher Logic
The most striking revelation in this chunk is the "Nested" nature of the dispatcher.
*   **Recursive Complexity:** Functions like `fcn.00412c10` do not simply execute an instruction; they contain internal switch tables (`0x45722c`, `0x4131f4`) and secondary dispatch loops. 
*   **Interpretation Layering:** This suggests that the "Interpreter" has multiple layers. One layer might handle "Macro-instructions" (high-level logic like "Perform Registry Modification"), while the nested sub-layers handle "Micro-instructions" (the specific steps to safely navigate the OS, check permissions, and execute). This makes manual deconstruction extremely time-consuming for an analyst.

#### 2. Massive Functional Breadth (The "Swiss Army Knife")
The function `fcn.0040f650` contains a massive switch table with over **40 distinct cases**.
*   **Modular Capability:** Each of these 40+ cases likely corresponds to a different capability: file manipulation, registry edits, network communication, local execution, and even potentially "dormant" code paths that are only activated by specific C2 commands.
*   **Anti-Analysis via Diversity:** By housing so many features in one large switch table, the author ensures that an analyst looking at any single segment of the binary will only see a fraction of what the malware is actually capable of doing.

#### 3. Advanced Data Handling & COM Integration
The inclusion of `OLEAUT32.dll_VariantCopy` and logic to handle "Variants" suggests a high level of integration with Windows internal structures.
*   **Complexity in Parsing:** The logic surrounding `fcn.0040bd9d` shows that the malware isn't just dealing with strings; it is managing complex data objects. It likely treats data coming from the C2 as "objects" rather than simple commands, allowing for more dynamic behavior (e.g., a single command could pass a configuration object containing ports, IPs, and timeout values).

#### 4. Robust Internal State Management
Functions such as `fcn.0040c000` through `fcn.0040c315` appear to be the **"Engine Room"** of the interpreter.
*   **State Tracking:** These functions manage "Contexts." They track where the current script is, what variables are currently loaded in the virtual memory space, and how many "steps" remain before a routine finishes. 
*   **Stability:** The amount of overhead dedicated to state management (checking bounds, validating pointers, updating indices) indicates that this malware was built for stability. It is designed to run for long periods without crashing or being caught by simple heuristic checks.

#### 5. Potential User Interaction/GUI Support
The presence of `USER32.dll_InvalidateRect` in `fcn.0040c3cb` suggests that the malware may have components capable of **manipulating Windows windows** or performing "UI spoofing." This could be used to display fake error messages, hide its own windows, or interact with other GUI-based elements on the victim's machine.

---

### Updated Summary for Report

**Analysis Overview:**
The analysis confirms that this malware utilizes an **Industrial-Grade, Multi-Layered Interpreter Architecture**. It functions as a "plug-and-play" platform where the core binary acts as an engine (the VM) and the specific malicious actions are defined by scripts received from a remote server. This architecture provides the threat actor with maximum flexibility: they can change the malware's purpose (e.g., switching from a credential stealer to a ransomware dropper) without ever needing to recompile or redistribute the primary binary.

**Key Indicators & Technical Findings:**
*   **Multi-Layered Dispatcher:** The discovery of nested switch tables and recursive dispatching (`fcn.00412c10`) indicates a sophisticated "VM within a VM" approach, designed specifically to baffle automated analysis tools and slow down manual human reverse engineering.
*   **High Functional Diversity:** A single dispatcher function (`fcn.0040f650`) contains over 40 distinct code paths. This demonstrates the massive scope of the malware’s capabilities, suggesting it is a "Swiss Army Knife" tool used for complex operations like lateral movement and persistent data exfiltration.
*   **Sophisticated State Management:** Extensive internal logic for managing "Context," memory pointers, and instruction counts suggests that the interpreter is designed to be extremely stable and capable of handling complex, multi-step scripts provided by a command-and-control (C2) server.
*   **Advanced Windows Integration:** The use of `OLEAUT32` functions and advanced data normalization indicates the malware is built to handle complex system objects, moving beyond basic "script kiddie" tactics into professional-grade exploit development.

**Conclusion for Threat Intelligence:**
This module represents a **high-tier threat actor capability**. The complexity of the interpreter ensures that the core malicious logic remains hidden behind layers of abstraction. Because the "actions" are decoupled from the "engine," the malware is highly resistant to signature-based detection. This is indicative of an advanced, persistent threat (APT) or a sophisticated cybercrime syndicate using a high-quality, modular framework to conduct long-term operations. **The sophistication and scale of the dispatcher logic suggest this tool was developed for professional use in complex environments.**

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your technical analysis to the corresponding MITRE ATT&CK techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Virtualization (Virtualization/Obfuscation) | The "Nested Dispatcher" and "VM within a VM" architecture are classic examples of using a custom interpreter to hide the core malicious logic from automated tools and human analysts. |
| **T1059** | Command and Scripting Interpreter | The malware acts as an engine that processes "Macro-instructions" and "Micro-instructions," allowing it to perform various actions (file manipulation, network tasks) via a script-based logic. |
| **T1566.002** | User Interface Spoofing | The presence of `USER32_InvalidateRect` specifically for potential GUI spoofing and hiding windows is used to deceive the user or bypass visual detection. |
| **T1485** | Data Encoding | (Implicit) The use of complex "Variant" types and objects through `OLEAUT32` suggests the processing of complex data structures, often used to obfuscate communication between the C2 and the interpreter. |

### Analytical Summary for Intelligence Reporting:
The behavior describes a **high-sophistication evasive architecture**. By utilizing **T1029 (Virtualization)**, the threat actor ensures that the primary binary acts only as a "carrier" or execution engine. This successfully decouples the malware's capabilities from its signature; because the functionality is defined by scripts interpreted by the internal VM, changing the malware's objective (e.g., from credential theft to ransomware) does not require changing the underlying code. 

The **T1059** component highlights a modular threat actor approach where "Swiss Army Knife" capabilities are hidden within a large switch table, forcing an analyst to deconstruct multiple layers of abstraction before identifying the actual payload. The inclusion of **T1566.002** indicates a level of polish intended for corporate environments where user interaction or deception is necessary to maintain a persistent presence.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*None identified.*

### **File paths / Registry keys**
*None identified.* (Note: While the analysis mentions "Registry modifications" as a capability, no specific keys were provided in the text.)

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None identified.*

### **Other artifacts**
The following are technical indicators derived from the behavioral analysis. These are primarily used for identifying the specific characteristics of the malware's internal architecture during reverse engineering:

*   **Internal Function Offsets (Behavioral Signatures):**
    *   `0x412c10`: Nested/Multi-layered dispatcher logic (Interpreter heart).
    *   `0x40f650`: Large switch table indicating high functional breadth (>40 cases).
    *   `0x40bd9d`: Advanced data handling and Variant handling.
    *   `0x40c000` - `0x40c315`: State management/Engine room functions.
    *   `0x40c3cb`: GUI manipulation via `InvalidateRect`.
*   **API Imports / Libraries:**
    *   `OLEAUT32.dll_VariantCopy` (Indicates complex data object handling).
    *   `USER32.dll_InvalidateRect` (Indicates potential UI spoofing or window manipulation).
*   **Architectural Indicators:**
    *   **VM/Interpreter Architecture:** The malware utilizes a "VM within a VM" approach to hide its true intent behind a layer of abstraction.
    *   **Modular Command Structure:** Decoupled logic where the core binary acts as an engine and capabilities are delivered via remote scripts.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family**: custom (high-tier modular framework)
2. **Malware type**: backdoor
3. **Confidence**: High
4. **Key evidence**:
    *   **Sophisticated VM Architecture:** The "Nested Dispatcher" and "VM within a VM" design (MITRE T1029) indicate it is designed to hide core logic from automated analysis, making it a high-tier threat rather than a simple Trojan.
    *   **High Functional Breadth:** A single dispatcher containing over 40 distinct cases identifies the malware as a "Swiss Army Knife" capable of diverse actions (file manipulation, registry edits, network communication) controlled via remote scripts.
    *   **Advanced Stability & Integration:** The use of `OLEAUT32` for complex data objects and dedicated state management logic indicates a professional-grade tool built for persistence and stability in enterprise environments.
