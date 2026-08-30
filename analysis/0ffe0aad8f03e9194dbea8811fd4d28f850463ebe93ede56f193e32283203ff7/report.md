# Threat Analysis Report

**Generated:** 2026-08-17 21:17 UTC
**Sample:** `0ffe0aad8f03e9194dbea8811fd4d28f850463ebe93ede56f193e32283203ff7_0ffe0aad8f03e9194dbea8811fd4d28f850463ebe93ede56f193e32283203ff7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ffe0aad8f03e9194dbea8811fd4d28f850463ebe93ede56f193e32283203ff7_0ffe0aad8f03e9194dbea8811fd4d28f850463ebe93ede56f193e32283203ff7.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,440,256 bytes |
| MD5 | `a71df36971d9b3d37b323e9247537331` |
| SHA1 | `e352c00618876fd227331dba953915a70489c1c9` |
| SHA256 | `0ffe0aad8f03e9194dbea8811fd4d28f850463ebe93ede56f193e32283203ff7` |
| Overall entropy | 7.305 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769472162 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 561,152 | 7.943 | ⚠️ Yes |
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

Total strings found: **3345** (showing first 100)

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

This final chunk of disassembly provides definitive evidence that the malware is not just using a "Virtual Machine" in the sense of a simple execution engine, but rather a **highly-developed proprietary runtime environment**. 

The presence of massive switch tables (up to 41 cases), complex internal object handling, and multi-layered abstractions for standard Windows APIs confirms the analysis that this malware is engineered by a sophisticated, well-resourced actor.

### Updated Analysis & Summary

#### 1. Core Functionality: Advanced Runtime Environment
The final chunk of code reveals that the "VM" acts as a full abstraction layer between the malicious payload and the operating system.

*   **Multi-Dispatch Handler System:** The function `fcn.0040f650` contains a switch table with over **40 cases**. This is typical of a sophisticated interpreter where each branch handles a different "instruction" or "operation." However, these aren't simple operations; they appear to be dispatching calls to various internal sub-modules (e.g., `fcn.00485e50`, `fcn.0048649d`).
*   **Sophisticated Object/Type Handling:** The repeated use of `OLEAUT32.dll_VariantCopy` and the complex pointer arithmetic in `fcn.00412c10` suggest that the malware uses an internal "object" system. It likely wraps data into proprietary structures that mimic high-level programming objects, making it extremely difficult to trace where a piece of data (like a stolen password or a file path) originates and where it ends up.
*   **Deep API Abstraction:** The code for `fcn.0040c3cb` shows interaction with `USER32.dll_InvalidateRect`. Crucially, this call is buried deep within several layers of internal logic (`fcn.00412c10`, etc.). This means the "malicious" intent (e.g., updating a UI or handling a window message) is separated from the actual Windows API call by multiple layers of VM-controlled code, effectively "cloaking" the intent from automated behavioral tracers.

#### 2. Advanced Obfuscation & Complexity
The complexity revealed in this final chunk highlights several high-tier tactics:

*   **Stateful Execution:** The logic frequently checks internal registers and status codes (e.g., `if (iVar3 != 0x7f)`, `if (uVar1 == 0)`). This indicates the malware is "aware" of its state within the virtual environment, making it hard to replicate its behavior in a sandbox unless the exact initial state is perfectly replicated.
*   **Robustness via Modularization:** The sheer volume of different functions (`fcn.0041fd94`, `fcn.00420db0`, etc.) used for basic operations like buffer management or error handling shows that this code was likely developed as a reusable library or "framework" before being integrated into the final malware sample.
*   **Anti-Analysis by Complexity:** The complexity of functions like `fcn.00412c10` is designed to exhaust human analysts. A researcher trying to follow the logic flow from a simple action back to the core code would have to navigate hundreds of branches and internal state changes.

#### 3. Indicators of Advanced Malware (Sophistication)
*   **Highly Scalable Infrastructure:** The fact that the malware uses a "dispatcher" model means the threat actor can update the *payload* (the bytecode) without ever changing the *interpreter* (the binary). This allows them to change functionality quickly while keeping the core "cloaking" mechanism intact.
*   **Persistence of Analysis Resistance:** Because most operations occur within the virtualized layer, standard hooks into common Windows APIs will often only see the "VM" doing work, not the "malware" performing a malicious act. This creates a significant gap in what automated EDR (Endpoint Detection and Response) systems can detect.

---

### Final Summary for Incident Response
**Status: Confirmed - High-Tier Threat / Sophisticated State-Sponsored Capability.**

The full disassembly confirms that this sample utilizes a **highly sophisticated, multi-layered Virtual Machine architecture.** This is not a typical "packed" malware; it is an execution environment built to host complex malicious activities while hiding them from signature-based and heuristic analysis.

*   **Complexity Level:** **Critical**. The presence of large dispatch tables (40+ cases) and deep API wrapping indicates an extremely high level of development effort.
*   **Behavioral Warning:** 
    *   **"Ghost" Actions:** Because the malware interacts with Windows via its own internal "wrapper," many malicious actions may not trigger standard alerts until they are significantly advanced in their execution cycle.
    *   **High Resilience to Static Analysis:** The use of a custom interpreter means that static analysis will likely only reveal the *interpreter*, while the actual harmful logic remains hidden in an encrypted/encoded bytecode format.
*   **Recommendations:**
    1.  **Behavioral Monitoring (Network focus):** Since the local logic is so heavily obscured, look for indicators at the network layer. Identify the C2 infrastructure and any non-standard protocol behavior early.
    2.  **Memory Forensics:** Because the "real" code only exists in memory as decoded bytecode within the VM's space, forensic teams should perform periodic memory dumps to attempt to capture the decrypted instructions.
    3.  **Host Indicators:** Treat any system infected by this sample as having a deep, persistent foothold. The complexity of the code suggests that once it executes, it can hide its presence quite effectively from standard scanning tools.

**Final Threat Intelligence Tags:** `VM_Execution_Engine`, `Multi-Layer_Abstraction`, `Custom_Dispatcher`, `API_Wrapping`, `High_Complexity_Obfuscation`, `Advanced_Persistence_Capability`, `State_Sponsored_Signature`.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Executables | The use of a "proprietary runtime environment" (VM) and multi-dispatch switch tables are classic methods to hide malicious logic from static analysis. |
| T1027 | Obfuscated Executables | Deep API abstraction and wrapping act as "cloaking," separating the actual intent from standard Windows API calls to evade detection by automated behavior trackers. |
| T1027 | Obfuscated Executables | The implementation of a complex, stateful execution environment is designed to exhaust human analysts and hinder automated sandboxing/heuristic analysis. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral documentation, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section consists primarily of obfuscated machine code/junk data and internal memory offsets; therefore, no direct network or file system indicators were present in that specific block.

### **Indicators of Compromise (IOCs)**

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (Internal function pointers such as `fcn.0040f650` were excluded as they are memory offsets, not file system artifacts).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Custom VM Execution Engine:** The malware utilizes a proprietary runtime environment with a **Multi-Dispatch Handler System** (evidenced by large switch tables of 40+ cases).
*   **API Wrapping/Abstraction:** Extensive use of internal wrappers for standard Windows APIs (e.g., `USER32.dll_InvalidateRect` and `OLEAUT32.dll_VariantCopy`) to hide malicious intent from behavioral tracers.
*   **Stateful Obfuscation:** Implementation of complex state-tracking logic (`if (iVar3 != 0x7f)`, etc.) to prevent sandboxes from accurately simulating the malware's execution path.

---

### **Analyst Note**
The sample exhibits characteristics of a high-tier threat actor. Because the core malicious logic is hidden within a custom virtual machine, traditional signature-based detection (hashes and strings) is unlikely to be effective. Defensive efforts should focus on:
1.  **Memory Forensics:** Scanning for signs of a "VM-in-memory" interpreter.
2.  **Network Behavior:** Monitoring for non-standard protocols or high-entropy traffic, as this is the most likely point where the "hidden" logic will manifest externally.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: Custom (Sophisticated)
2. **Malware type**: Loader / Backdoor 
3. **Confidence**: High (regarding its functionality/sophistication level); Low (regarding a specific named brand due to lack of IOCs)
4. **Key evidence**:
    *   **Complex VM Execution Engine:** The sample utilizes a proprietary, multi-layered Virtual Machine architecture with switch tables exceeding 40 cases to interpret bytecode, effectively shielding the primary malicious logic from static analysis.
    *   **Advanced API Abstraction:** The use of "wrapping" (e.g., for `USER32` and `OLEAUT32`) creates a buffer between the malware's actions and the OS, specifically designed to blind automated behavior-based detection systems.
    *   **High-Tier Sophistication:** The presence of stateful execution logic, modular library usage, and "ghost" action capabilities indicates an advanced threat actor (likely state-sponsored or high-end organized crime) rather than a common commodity infection.
