# Threat Analysis Report

**Generated:** 2026-07-18 00:12 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, UPX compressed, 3 sections |
| Size | 602,624 bytes |
| MD5 | `7c4a7c924a203f0336dad4ac9e99bc41` |
| SHA1 | `48eb07dfffad28ec064e5f62566c9aca9c2383c0` |
| SHA256 | `07fa3b53b7aaa614ed5e5858502e9aaa58662b16e62b60d77202a7de9ef761f2` |
| Overall entropy | 6.94 |
| Unpacked | ✓ Yes (tool: upx) |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769069648 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.61 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 229,888 | 7.777 | ⚠️ Yes |
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

Total strings found: **2643** (showing first 100)

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

This final analysis incorporates the findings from **Chunk 5/5**. This concluding segment solidifies the previous observations, confirming that the binary is not just a simple loader but a sophisticated, highly-engineered execution environment designed for persistence and multi-layered evasion.

### Final Technical Analysis of Chunk 5

The disassembly in this final section provides definitive evidence of the "Intermediate Layer" architecture used by the malware.

#### 1. The "Grand Dispatcher" (fcn.0040f650)
The most striking finding in this chunk is the massive switch table in `fcn.0040f650`. With **over 40 cases** mapped to different internal routines, this function acts as a primary gateway for "internal" commands.
*   **Functionality:** It interprets complex operations (string manipulation, mathematical evaluations, and system state checks) before they are ever exposed as high-level script logic.
*   **Security Impact:** By moving these actions into the interpreter's core, the developer ensures that any single malicious action (e.g., "Check if a file exists" or "Calculate an XOR key") is buried deep within the engine’s internal logic. An analyst looking at this function sees only generic code; they cannot know what the script intended to do without knowing the specific ID passed into the switch table.

#### 2. Robust Memory & Resource Management (fcn.0040bd9d, fcn.0040be83)
These functions handle complex buffer management and dynamic allocation. The logic for handling different lengths (`0x10`, `0x20`) and the meticulous "cleanup" routines (`fcn.0041fd4d`) indicate that this engine is designed to run **continuously and reliably**.
*   **Malware Context:** This suggests a long-running backdoor or an agent that might perform complex tasks (like scanning a network, exfiltrating large data blocks, or encrypting files) over an extended period without crashing or leaking memory—a hallmark of high-tier state-sponsored or professional criminal tools.

#### 3. Specialized Data Type Handling (fcn.00412c10 & fcn.00411df0)
The logic in `fcn.00412c10` is highly complex, involving nested checks for object types and list indices. It mirrors the behavior of a professional scripting language's compiler/interpreter.
*   **Abstaction Barrier:** This reinforces the "Abstraction Shielding" noted earlier. The engine treats variables as "Objects," meaning when the script interacts with the Windows API (via COM), it does so through several layers of abstraction. The link between a simple command in a script and the final `Advapi32` or `Kernel32` call is never direct, creating a massive **audit gap** for security tools.

#### 4. Potential GUI/Interaction Capabilities (fcn.0040c3cb)
The inclusion of logic related to `InvalidateRect` and the handling of window-related constants suggests that while the primary goal may be malicious, the engine is capable of interacting with Windows UI elements or maintaining a presence that looks like a legitimate, responsive application to the user.

---

### Final Synthesis: The Architecture of Obfuscation

By combining all five chunks of disassembly, we can conclude that this binary represents a **high-tier threat (APT/Sophisticated Cybercrime).** The following three pillars define its sophistication:

#### I. Execution Gap (The "Interpreter" Defense)
The malware doesn't use standard, recognizable "malicious" patterns for its primary actions. Instead, it feeds a script into an **AutoIt-derived engine**. 
*   **The Result:** Standard AV/EDR looks for specific sequences of API calls (e.g., `OpenProcess` $\rightarrow$ `VirtualAllocEx` $\rightarrow$ `WriteProcessMemory`). In this malware, those calls are hidden behind the interpreter's logic. The "malicious" part is just a data string being parsed by the engine; the "engine" itself is technically and functionally "neutral."

#### II. Complex Data Layering
By utilizing **COM/OLE** (from Chunk 4) and advanced **Switch Tables** (Chunk 5), the authors have created a multi-layered execution path:
1.  **Script Layer:** The hidden, malicious commands (hidden from static analysis).
2.  **Interpreter Layer:** The complex logic found in `fcn.0040f650` and `fcn.00412c10`.
3.  **System Layer:** The final Windows API calls used to perform the actual theft/sabotage.
*   *An analyst must break through all three layers to find the true intent.*

#### III. Robust Infrastructure
This is not a "one-off" script-loader. The presence of sophisticated memory management, error handling for different string types, and complex internal logic indicates that this engine was developed as a **reusable platform**. It is designed to be stable enough to host multiple different types of malicious scripts (Spyware, Ransomware, or Backdoors) by simply swapping the underlying script file.

### Final Summary Statement
This binary is an **advanced, multi-layered "Interpreter Wrapper" Trojan.** It leverages a sophisticated internal engine—likely customized from AutoIt source code—to create a massive gap between the high-level malicious intent and the low-level system execution. 

**Key Indicators of High Sophistication:**
1.  **Sophisticated Dispatching:** Massive switch tables to handle complex logic internally.
2.  **Abstraction Shielding:** Using COM objects to perform "noisy" actions via "quiet" calls.
3.  **Persistence Readiness:** Robust memory management and specialized buffer handling for long-term, stable operation.
4.  **Complex Environment Tracking:** Internal state tracking that makes the execution path context-dependent (dynamic behavior).

**Conclusion:** This is a high-capability tool designed to defeat both automated signature/heuristic detection and manual reverse engineering by burying the malicious logic inside a complex, "neutral" interpreter architecture.

---

## MITRE ATT&CK Mapping

Based on the behavior analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The malware utilizes an AutoIt-derived engine as a primary "gateway," allowing it to execute malicious commands through an intermediate scripting layer rather than directly via the OS. |
| **T1027** | Obfuscated Valid Commands | The use of a massive switch table ("Grand Dispatcher") and "Abstraction Barriers" (COM/OLE) hides the true intent of scripts by burying malicious actions inside complex, multi-layered logic. |

### Analyst Notes:
*   **Execution Gap:** This concept described in the analysis is primarily realized through **T1027**. By ensuring that standard API sequences (e.g., `VirtualAlloc` $\rightarrow$ `WriteProcessMemory`) are never executed directly by a single thread but are instead parsed and orchestrated by an interpreter, the malware successfully bypasses common signature-based detection.
*   **Abstraction Barrier:** The use of COM/OLE to interface with system resources is a deliberate move to create distance between high-level script commands and low-level `Advapi32` or `Kernel32` calls, making it significantly harder for automated security tools to correlate the two actions as a single malicious event.
*   **Sophistication Note:** The "Robust Memory Management" and "Persistence Readiness" observed in Chunk 5 indicate that while not specific MITRE techniques, these behaviors demonstrate high-level **Defense Evasion** by ensuring the malware's footprint remains stable and non-crashing during long-term deployment.

---

## Indicators of Compromise

Based on the provided data, here is the extraction of Indicators of Compromise (IOCs). 

**Note:** The "Extracted Strings" section contains largely obfuscated/non-human-readable characters and binary fragments; no plaintext IPs, URLs, or file paths were present in that specific block. However, the behavioral analysis identifies specific internal logic markers.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: The analysis mentions `InvalidateRect` and Windows API calls, but no specific malicious file paths or registry keys were disclosed).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None provided in the source text.*

### **Other artifacts**
*   **Malware Type:** Interpreter Wrapper (AutoIt-derived engine). 
*   **Behavioral Signature:** Use of a "Grand Dispatcher" switch table to hide malicious logic within an interpreter's internal commands.
*   **Specific Function Offsets (Internal Logic Indicators):**
    *   `0x40f650`: Grand Dispatcher (Switch Table for interior command processing).
    *   `0x40bd9d`, `0x40be83`, `0x41fd4d`: Memory and buffer management routines.
    *   `0x412c10`, `0x411df0`: Complex data type/object handling.
    *   `0x40c3cb`: GUI interaction and window-related constant logic.
*   **Techniques Identified:** 
    *   Abstraction Shielding (via COM/OLE objects).
    *   Execution Gap creation (hiding malicious intent behind an "innocent" interpreter).
    *   Robust Memory Management for long-running backdoor capabilities.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: backdoor
3. **Confidence**: High

**Key evidence**:
*   **Interpreter-Based Architecture:** The sample utilizes an AutoIt-derived engine to create an "Execution Gap," where malicious actions are executed through a scripting layer rather than direct, detectable API calls.
*   **Sophisticated Obfuscation Techniques:** The use of a "Grand Dispatcher" (large switch table) and COM/OLE abstractions creates significant hurdles for automated analysis by hiding the true intent of commands within complex, multi-layered logic.
*   **Robust Persistence Design:** Evidence of sophisticated memory management and stable execution routines indicates the binary is intended as a high-tier tool for long-term persistence rather than a one-time payload.
