# Threat Analysis Report

**Generated:** 2026-07-15 11:27 UTC
**Sample:** `06c4acccda31358fd172466d6245f827c2b5075dec6496516286f936f22ef771_06c4acccda31358fd172466d6245f827c2b5075dec6496516286f936f22ef771.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `06c4acccda31358fd172466d6245f827c2b5075dec6496516286f936f22ef771_06c4acccda31358fd172466d6245f827c2b5075dec6496516286f936f22ef771.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 998,400 bytes |
| MD5 | `8f66108ec8f997b14f660e576bdca751` |
| SHA1 | `800b1bcb91f794af35e5e823c53d6e58150d2395` |
| SHA256 | `06c4acccda31358fd172466d6245f827c2b5075dec6496516286f936f22ef771` |
| Overall entropy | 6.761 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771395732 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 119,296 | 7.443 | ⚠️ Yes |
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

Total strings found: **2356** (showing first 100)

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

The final chunk of disassembly provides the most definitive evidence yet that this is not a simple "packer" or "obfuscator," but a **highly sophisticated, custom-built scripting interpreter.** 

This data reveals the inner workings of what we can now formally classify as a **Virtual Machine (VM) based Scripting Runtime Environment.** The malware doesn't just hide its logic; it wraps all malicious actions inside a high-level programming language layer.

### Final Analysis: The "Host Engine" Architecture

#### 1. Evidence of a Managed Memory System (Garbage Collection/Reference Counting)
Functions like `fcn.0040be83` and `fcn.0040bef7` are quintessential features of high-level languages (like Python, PHP, or AutoIt). 
*   **Reference Counting:** The logic checking if a counter is zero (`if (*arg_8h_00[3] == 0)`) before calling a "Release" function indicates the engine manages object lifecycles. If a script creates a string or a buffer, the engine tracks how many times it is used and automatically frees the memory when it's no longer needed by the script.
*   **Memory Pooling:** The use of `fcn.0041fd8b` to calculate allocation sizes suggests the engine manages its own internal "heap" or "pool," abstracting away direct calls to `malloc` or `HeapAlloc`.

#### 2. The Core Dispatcher (The Interpreter Loop)
The function `fcn.0040f650` is a "Master Switch" for the script's capabilities. 
*   **Massive Command Library:** This function contains an enormous switch table with over 40 distinct cases. Each case corresponds to a different command available to the underlying malicious script.
*   **Abstraction of Functionality:** Because these cases point to internal functions (e.g., `fcn.00485a1e`, `fcn.004860f7`), an analyst looking at the assembly only sees the *interpreter's* ability to handle a command, not what that command actually does. For example, one case might be "Get_Current_User," and another "Send_HTTP_Request." The script simply says `GET_USER`, and the interpreter handles all the complex logic of querying the OS.

#### 3. Advanced Data Handling (OLE Variants & Complex Structs)
The recurring use of `OLEAUT32.dll_VariantCopy` and the complex indexing in `fcn.00412c10` indicate that the script can handle **complex data types.** It isn't just processing raw bytes; it is likely handling:
*   Multi-byte strings (Unicode/ANSI)
*   Arrays or Lists of objects
*   Complex structures involving nested pointers (as seen in the logic traversing offsets like `0x210` and `0x10c`).

#### 4. Evidence of UI Integration
The presence of `USER32.dll_InvalidateRect` in `fcn.0040c3cb` suggests that the script engine is capable of interacting with the Windows GUI. This could be used to create fake error messages, custom menus, or "ghost" windows to deceive the user while the script executes its primary goals.

---

### Final Comprehensive Summary for Threat Intelligence

The malware utilizes a **Virtual Machine (VM) Based Execution Environment** that functions as a comprehensive scripting runtime (likely based on or heavily modified from AutoIt or a similar framework). This creates a "double-blind" scenario for security analysts:

**Key Technical Findings:**
1.  **Dual-Layered Execution:** The malware consists of two parts: the **Interpreter Engine** (the code we have analyzed) and the **Malicious Script** (the logic that stays hidden inside the engine). 
2.  **Abstracted API Usage:** Instead of calling `CreateRemoteThread` or `InternetOpenUrl` directly, the script calls high-level internal functions. This renders standard "API Hooking" less effective because the link between a malicious action and the raw OS call is obscured by several layers of translation logic.
3.  **Managed Environment:** The engine includes automatic memory management (reference counting), complex string/data type handling, and sophisticated buffer management. This suggests the developers want to ensure "stability"—the script needs to run reliably without crashing the host process.
4.  **Extensive Capability Set:** The massive switch table in `fcn.0040f650` proves the malware is designed for a wide range of functionalities (file manipulation, network communication, data parsing, and UI interaction), all performed via the "safe" bridge of the interpreter.

### Updated Recommendation for Incident Response & Analysis:
*   **Don't Just Trace API Calls:** Traditional dynamic analysis will only show you what the *interpreter* is capable of doing. To find out what the *malware* is doing, you must find where the script is stored in memory.
*   **Target the Interpreter's Memory Space:** Set hardware breakpoints on the "Switch" tables (like `fcn.0040f650`). By logging which cases are triggered during execution, you can map out the "Command List" of the malware. 
*   **Memory Forensics for Script Extraction:** The most effective way to find the actual logic is to dump the memory of the process and look for patterns associated with known scripting languages (e.g., searching for keywords like `if`, `for`, or common script-related strings).
*   **Behavioral Profiling:** Since the internal "Logic" is hidden, focus on the **outcomes**. Monitor for:
    *   Unexpected network connections from the process.
    *   File system modifications in sensitive directories.
    *   Creation of new processes or injection into other processes.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The malware utilizes a custom-built scripting runtime environment to execute malicious logic through high-level commands rather than direct API calls. |
| **T1027** | Obfuscated Executables | The use of a Virtual Machine (VM)-based architecture creates a "double-blind" layer, hiding the true functionality from static and dynamic analysis tools. |
| **T1036** | Masquerading | The integration of UI capabilities like `InvalidateRect` suggests the ability to display fake error messages or "ghost" windows to deceive users. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contains heavily obfuscated/encoded data typical of a virtualized environment; therefore, no plaintext IP addresses, domains, or file paths were identified in that specific block.

**IP addresses / URLs / Domains**
*   None detected.

**File paths / Registry keys**
*   None detected. (Note: Standard Windows API calls like `OLEAUT32.dll` and `USER32.dll` were identified but are excluded as standard system components).

**Mutex names / Named pipes**
*   None detected.

**Hashes**
*   None detected.

**Other artifacts**
*   **Interpreter Architecture:** VM-based Scripting Runtime Environment (indicates the use of a custom interpreter to hide malicious logic).
*   **Command Dispatcher Offset:** `fcn.0040f650` (Identified as the "Master Switch" or Dispatcher table containing over 40 distinct commands).
*   **Memory Management Artifacts:** Implementation of Reference Counting and Memory Pooling (functions at `fcn.0040be83`, `fcn.0040bef7`, and `fcn.0041fd8b`).
*   **Potential Framework Affinity:** Analysis suggests the environment is likely based on or heavily modified from **AutoIt** or a similar scripting framework.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1.  **Malware family**: **custom** (VM-based Scripting Interpreter)
2.  **Malware type**: **loader**
3.  **Confidence**: **High**
4.  **Key evidence**:
    *   **Virtual Machine Architecture:** The analysis confirms the sample is not a simple packer but a sophisticated "VM-based Scripting Runtime Environment." It uses an interpreter to execute hidden scripts, effectively creating a "double-blind" layer that hides malicious logic from standard security tools.
    *   **Extensive Command Dispatcher:** The identification of a "Master Switch" (`fcn.0040f650`) with over 40 distinct cases indicates the engine is designed to perform a wide range of actions (networking, file manipulation, UI interaction) through an abstracted layer.
    *   **Managed Memory & Framework Affinity:** The presence of reference counting, memory pooling, and OLE variant handling suggests it is built upon or modified from established scripting frameworks (like AutoIt), which are commonly used to build stable, complex loaders for malware campaigns.
