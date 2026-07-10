# Threat Analysis Report

**Generated:** 2026-07-09 19:06 UTC
**Sample:** `0419882ed9dc550b5b6e18b123cb3b53e9b276bbf42d567bd88720d2f526c6ff_0419882ed9dc550b5b6e18b123cb3b53e9b276bbf42d567bd88720d2f526c6ff.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0419882ed9dc550b5b6e18b123cb3b53e9b276bbf42d567bd88720d2f526c6ff_0419882ed9dc550b5b6e18b123cb3b53e9b276bbf42d567bd88720d2f526c6ff.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,034,752 bytes |
| MD5 | `55b447ccc96fa4f85e61b443054adae9` |
| SHA1 | `fb86a2a9213cbd88a593c982ee39599394ae1ce6` |
| SHA256 | `0419882ed9dc550b5b6e18b123cb3b53e9b276bbf42d567bd88720d2f526c6ff` |
| Overall entropy | 6.831 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1764073097 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 155,648 | 7.619 | ⚠️ Yes |
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

Total strings found: **2483** (showing first 100)

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

This final chunk of disassembly confirms the preceding analysis while providing a definitive look into the internal "engine room" of the binary. The presence of massive switch tables and complex object-handling logic in this final section solidifies the conclusion that this is not just any "scripting-enabled" tool, but a **sophisticated, multi-layered execution environment.**

The following update integrates the findings from chunk 5 into the existing analysis.

---

### Updated Technical Analysis of the Binary Sample

#### 1. The Interpreter Dispatcher (Core Architecture)
Chunk 5 provides clear evidence of an "Instruction Set" architecture. Functions like `fcn.0040f650` and `fcn.00412c10` function as central dispatch hubs:
*   **The Switch-Table Explosion:** The presence of a switch table with dozens of cases (as seen in `fcn.0040f650`) indicates that the binary does not perform linear execution. Instead, it receives an "Opcode" or "Command ID" from a script and jumps to a specific handler.
*   **Decoupled Logic:** This means the malicious behavior is never "hard-coded" in one sequence of assembly. One switch statement handles everything from UI updates (`InvalidateRect`) to network logic, memory allocation, and file manipulation. The actual "malicious path" is only determined at runtime by the script data being fed into these switches.

#### 2. Advanced OLE/COM & Variant Handling
The repeated references to `OLEAUT32.dll_VariantCopy` and the processing of complex structures in `fcn.00412c10` confirm a deep integration with Windows **Variant types**.
*   **Multi-Type Support:** The engine is designed to handle data that could be anything—a string, an integer, a date, or even an embedded object—within the same variable structure. 
*   **Standardized Logic for Complex Data:** By using `VariantCopy`, the interpreter ensures that it can pass complex data structures between different parts of the "script" without the programmer having to worry about memory types, which is common in high-level languages like **AutoIt, VBA, or VBScript**.

#### 3. Automated Memory Management & Robustness
Several functions (`fcn.0040bd9d`, `fcn.0040be83`, `fcn.0040bef7`) are dedicated to **buffer lifecycle management**:
*   **Dynamic Growth:** The code doesn't just allocate a fixed buffer; it checks if the current buffer is sufficient (`if (in_ECX[2] < uVar1)`) and automatically grows/re-allocates memory if necessary. 
*   **Safety Wrappers:** These functions act as "safety nets," ensuring that when the script requests long strings or large data blocks, the underlying interpreter handles the allocation safely, preventing common buffer overflows while allowing for complex operations.

#### 4. Advanced Calculation & State Management
Function `fcn.00411df0` reveals a highly technical approach to state:
*   **Complex Scale Calculations:** The loops calculating values based on indices (like `iVar1 * iVar4`) suggest the engine is performing complex calculations—perhaps for rendering, UI layout, or processing multi-part data structures. 
*   **Pre-validation of Data:** It appears to validate "quantities" and "dimensions" before proceeding with memory operations, a hallmark of a mature, professional software framework rather than a crude malware sample.

---

### Summary of Findings for Report

The analysis confirms that this binary is a **high-complexity, industrial-grade scripting interpreter.** It is designed to provide a robust environment where high-level logic (scripts) can be executed with high functionality and safety.

#### Key Technical Indicators:
1.  **Sophisticated Command Dispatching:** The use of massive switch tables (e.g., `fcn.0040f650`) shows that the binary acts as a "Swiss Army Knife." A single executable can perform hundreds of different actions based on which "command" it receives from the accompanying script files.
2.  **Advanced Data Abstraction:** Extensive support for **OLE/COM Variant types** allows the interpreter to handle complex, multi-type data structures seamlessly, typical of environments like **AutoIt**.
3.  **Robust Buffer Management:** The presence of dedicated logic for dynamic buffer growth and validation indicates that the environment is designed to handle "heavy" payloads or complex configurations without crashing.

#### Security Implications:
*   **Evasion via Structural Obfuscation:** The complexity of the interpreter creates a massive barrier for analysts. Because the actual malicious intent (e.g., exfiltrating data, injecting code) is hidden within the script's logic and only "activated" by the interpreter's switch-table jumps, static analysis of the binary alone cannot reveal the full scope of the threat.
*   **Multi-Functionality (Modular Malware):** Because the engine is so feature-rich, a single piece of malware can be used for multiple different purposes depending on what script is loaded into it at runtime. This allows an attacker to use one "tool" for many different campaigns.
*   **Abstraction Barrier:** The interpreter acts as a buffer between the analyst and the malicious action. An analyst sees code that handles "string length validation," while the script being processed by that code may be performing a sophisticated credential theft.

#### Conclusion:
This component is likely part of a **sophisticated malware framework** (likely involving **AutoIt** or a similar automation tool). The architecture is designed to provide maximum flexibility for the attacker while maximizing the complexity for the defender. It prioritizes **abstraction-based evasion**, where the "malice" resides in the data interpreted by the engine, rather than the binary code itself.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors described in your technical analysis to the following MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The binary functions as a sophisticated execution engine that interprets "Opcode" or "Command IDs" to perform diverse actions (network, file system, UI) via a central dispatch hub. |
| **T1027** | Obfuscated Files or Information | The use of a complex interpreter creates an abstraction barrier where the actual malicious logic is hidden in script data rather than being explicitly hard-coded in the binary's assembly. |
| **T1583** | Acquire System Information (Implicit) | While not directly mentioned as an action, the "Robust Buffer Management" and "Advanced Calculation" indicate the engine is built to handle complex system queries and high-volume data processing for malicious purposes. |
| **T1036** | Masquerading (Contextual) | The architecture allows a single "Swiss Army Knife" binary to masquerade as various tools or functions by simply swapping out the script file provided at runtime. |

### Analytical Notes:
*   **Primary Technique (T1059):** This is the core finding of your analysis. The switch-table explosion and logic decoupling are classic indicators of a "loader" or "interpreter" designed to host third-party scripts, a common tactic in sophisticated malware frameworks like those utilizing AutoIt, VBScript, or custom Python wrappers.
*   **Evasion Strategy (T1027):** Your analysis highlights that the "malice" resides in the data interpreted by the engine. In threat hunting terms, this means the binary itself may appear "benign" or "generic" during static analysis because its true functionality is only activated when paired with a specific script.
*   **Structural Obfuscation:** The "Robust Buffer Management" and "Advanced Data Abstraction" (via `OLEAUT32`) suggest an industrial-grade tool intended for longevity and reliability, which often indicates a professional threat actor or a high-end malware commoditized for multiple campaigns.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** The "EXTRACTED STRINGS" section contains significant amounts of high-entropy/garbled data and assembly-related artifacts that do not contain actionable network indicators or file paths.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: The reference to `OLEAUT32.dll` is a standard Windows system library and is excluded as a false positive.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Function Offsets (Internal Logic):** 
    *   `0040f650` (Switch-table/Interpreter Dispatcher)
    *   `00412c10` (Variant Handling/Logic)
    *   `0040bd9d`, `0040be83`, `0040bef7` (Memory Management routines)
    *   `00411df0` (Calculation/State management)
*   **Identified Framework Behavior:** 
    *   Evidence of an **AutoIt-based** or similar scripting interpreter.
    *   Usage of **OLE/COM Variant types** (`OLEAUT32.dll_VariantCopy`) for multi-type data handling.
    *   Presence of large switch tables indicating a "Swiss Army Knife" architecture for dynamic command execution.

---

## Malware Family Classification

Based on the detailed technical analysis provided, here is the classification of the sample:

1. **Malware family**: AutoIt-based Loader (or Scripting Wrapper)
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Interpreter Architecture:** The presence of massive switch tables and "Instruction Set" logic indicates that the binary is not a standalone piece of malware but an interpreter designed to execute external scripts (similar to AutoIt or VBScript).
    *   **Decoupled Logic/Swiss Army Knife Design:** By using a command-dispatch model, the binary acts as a modular "host." The actual malicious intent is hidden within the data (scripts) fed into the engine rather than being hard-coded in the assembly.
    *   **Advanced Infrastructure:** The heavy reliance on `OLEAUT32` Variant types and sophisticated buffer management indicates an industrial-grade framework designed for high reliability and multi-purpose deployment across different campaigns.
