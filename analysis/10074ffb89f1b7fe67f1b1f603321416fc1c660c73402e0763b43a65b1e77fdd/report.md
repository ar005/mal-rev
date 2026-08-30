# Threat Analysis Report

**Generated:** 2026-08-17 21:39 UTC
**Sample:** `10074ffb89f1b7fe67f1b1f603321416fc1c660c73402e0763b43a65b1e77fdd_10074ffb89f1b7fe67f1b1f603321416fc1c660c73402e0763b43a65b1e77fdd.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10074ffb89f1b7fe67f1b1f603321416fc1c660c73402e0763b43a65b1e77fdd_10074ffb89f1b7fe67f1b1f603321416fc1c660c73402e0763b43a65b1e77fdd.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,227,264 bytes |
| MD5 | `46a179e12c11babcff94511c022ece7e` |
| SHA1 | `cfcd26a0fe8623a2bf371c8b466643ae7634baf9` |
| SHA256 | `10074ffb89f1b7fe67f1b1f603321416fc1c660c73402e0763b43a65b1e77fdd` |
| Overall entropy | 7.097 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1763964287 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.61 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 348,160 | 7.879 | ⚠️ Yes |
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

Total strings found: **2877** (showing first 100)

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

This final analysis incorporates the findings from **Chunk 5/5**, completing the technical picture of the malware's architecture.

The addition of these segments confirms that the malware utilizes a sophisticated "Execution Maze" designed to separate the *intent* of the malicious code from the *actual system calls* made by the processor.

---

### Updated Analysis Report (Final Comprehensive View)

#### 1. Advanced Architecture: The Multi-Layered Execution Maze
The analysis of the switch tables in this final chunk (e.g., at `0x4562b3`, `0x45722c`, and especially the massive table at `0x40f828`) confirms a **highly complex, multi-layered dispatching system.**

*   **The "Maze" Effect:** The presence of multiple large switch tables (some with over 40 cases) indicates that an instruction is not simply "decoded once." It passes through several stages:
    1.  **Instruction Fetch:** Pulls a raw byte/opcode.
    2.  **Primary Dispatch:** Determines the high-level category of the command (e.g., "File System," "Network," or "UI Manipulation").
    3.  **Micro-Op Dispatch:** Breaks down the command into specific sub-actions.
*   **Gateway Synthesis:** The repeated usage of `fcn.0041fd94` and `fcn.0041fd4d` across these tables suggests they act as "Gateways." These functions likely handle the final transition from the virtualized environment to a physical system action (like setting up memory regions or validating handles).

#### 2. Large-Scale Command Interpreter (The Scripting Engine)
The function `fcn.0040f650` is a critical discovery. With over **41 cases** in its switch table, it serves as the primary **Command Interpreter**.

*   **Functionality:** This is where the "script" lives. Each case likely corresponds to a command found in an internal configuration or script file.
*   **Sophistication:** The sheer number of cases indicates that this isn't just a simple VM; it is a full-featured execution environment capable of handling diverse operations (e.g., persistence, information theft, and interaction with other processes) through a single abstracted interface.

#### 3. Sophisticated Memory & Resource Management
The functions `fcn.0040bd9d`, `fcn.0040be83`, and `fcn.0040bef7` provide evidence of a **custom memory management system**.

*   **Abstraction from System API:** Instead of using standard Windows `malloc` or `HeapAlloc` for every operation, the malware calculates offsets and manages its own internal buffer pool (e.g., checking lengths like `0x10`, `0x20`, etc.).
*   **Signature Evasion:** By managing its own memory "pool," the malware makes it much harder for automated tools to detect malicious behavior via heap-scanning, as all operations appear to take place within a single, large allocated block.

#### 4. Complex COM/OLE and Windows UI Manipulation
The extensive logic in `fcn.00412c10` and its interaction with `OLEAUT32.dll_VariantCopy` confirms the malware's ability to handle complex data types.

*   **Data Encapsulation:** By using `VARIANT` types, the malware can pass multi-type data (strings, integers, pointers) between different "modules" of the VM without those values being exposed as simple constants in memory.
*   **GUI/System Interaction:** The logic and switch cases associated with 0x45722c suggest complex interactions with Windows handles, likely for creating hidden windows, tray icons (as seen in earlier chunks), or interacting with COM-based system services.

---

### Final Summary of Findings

| Feature | Evidence Found | Technical Implication |
| :--- | :--- | :--- |
| **Massive Dispatch Tables** | Switch tables at `0x4562b3` and `0x40f828` (41+ cases). | A massive "Instruction Set" exists. Analysts cannot find a single "malicious loop"; the logic is dispersed across dozens of sub-handlers. |
| **Gateway Functions** | Repeated calls to `fcn.0041fd94/4d`. | These are the only points where the VM interacts with the OS. Monitoring these specific addresses provides the highest signal for identifying malicious behavior. |
| **Custom Memory Pooling** | Complex buffer logic in `fcn.0040bd9d` and `fcn.0040be83`. | Intentional attempt to evade heap-analysis tools by hiding many operations inside a single allocated memory region. |
| **Scripting/Command Logic** | The multi-case structure of `fcn.0040f650`. | High probability of an embedded scripting language (e.g., a customized version of AutoIt or Lua) used to deliver modular payloads. |
| **COM/OLE Integration** | Heavy use of `VariantCopy` and complex switch logic. | Capability to handle complex data structures, likely for C2 communication or interacting with advanced Windows features. |

---

### Final Technical Conclusion for Analysts

This malware is a high-tier threat characterized by its **heavy reliance on abstraction.** It does not behave like typical "packer" code; it behaves like a fully realized **Virtual Machine System.**

**1. Analysis Strategy:**
Traditional "linear" analysis (following an API call back to its source) will fail because the "source" of many actions is just another entry in a switch table, which eventually leads back into the VM's dispatcher. 

**2. Recommended Methodology:**
*   **De-virtualization focus:** The goal should be to identify and log the **Instruction Fetcher**. This is the loop that pulls data from the "script" and feeds it into the first switch table. By logging these inputs, you can reconstruct the high-level logic of the attacker's commands.
*   **Gatekeeper Monitoring:** Treat `fcn.0041fd94` and `fcn.0041fd4d` as the primary "Hot Zones." Every time these are hit, a call to the "real world" is being prepared. These should be heavily instrumented with debuggers/trace tools.
*   **Memory Forensics:** Since it uses a custom memory management system, focus on the memory region(s) used for its internal buffer pools, as this is where the unencrypted "script" commands will reside during execution.

**3. Threat Actor Profile:**
The combination of multi-layered dispatchers, custom memory allocators, and extensive COM/OLE integration strongly suggests an **Advanced Persistent Threat (APT)** or a highly sophisticated criminal organization. The malware is designed to frustrate automated sandboxes and intermediate-level human analysts by burying the malicious logic under layers of architectural complexity.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1029 | Obfuscated Files or Information | The "Execution Maze" and multi-layered dispatch tables are used to decouple malicious intent from system calls, a hallmark of virtualization for evasion. |
| T1059 | Command and Scripting Interpreter | The high number of cases in the `fcn.0040f650` function indicates an internal scripting engine used to execute modular commands (e.g., persistence, theft). |
| T1029 | Obfuscated Files or Information | The custom memory management and buffer pooling are specifically designed to evade heap-scanning tools by hiding multiple operations within a single allocated block. |
| T1059 | Command and Scripting Interpreter | Use of COM/OLE and `VariantCopy` logic suggests the internal engine is capable of processing complex data structures for multifaceted malicious actions. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Because this is a highly obfuscated "Virtual Machine" based malware sample, traditional network IOCs (IPs/Domains) were not present in the provided text. The available indicators are primarily **behavioral** and **structural**.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (Internal Offsets & Behavioral Patterns)**
The following are internal memory offsets and architectural markers used by the malware's dispatcher. These are useful for identifying specific samples of this family during reverse engineering:

*   **Gateway Functions:** 
    *   `fcn.0041fd94`
    *   `fcn.0041fd4d`
*   **Command Interpreter:** 
    *   `fcn.0040f650` (Identified as the primary script interpreter with over 41 switch cases).
*   **Memory Management Functions:**
    *   `fcn.0040bd9d`
    *   `fcn.0040be83`
    *   `fcn.0040bef7`
*   **Switch Tables (Instruction Dispatch):** 
    *   `0x4562b3`
    *   `0x45722c`
    *   `0x40f828`
*   **System Interaction Logic:**
    *   `OLEAUT32.dll_VariantCopy` (Used for complex data encapsulation).

---

## Malware Family Classification

1. **Malware family:** Custom (VM-based)
2. **Malware type:** Loader / Backdoor
3. **Confidence:** High

4. **Key evidence:**
*   **Complex Virtualization Architecture:** The presence of multiple, large switch tables (e.g., `0x40f828`) and the "Execution Maze" indicate a sophisticated virtual machine (VM) environment where malicious logic is decoupled from system calls to evade traditional analysis.
*   **Advanced Command Interpreter:** The discovery of a command interpreter with over 41 cases (`fcn.0040f650`) suggests a modular framework capable of executing complex, varied tasks (e.g., persistence, exfiltration) through an internal scripting engine.
*   **Evasive Memory Management:** The use of custom memory pools and "Gateway" functions (`fcn.0041fd94/4d`) demonstrates a high-tier effort to bypass heuristic analysis and heap scanning by abstracting the malware's interactions with the Windows OS.
