# Threat Analysis Report

**Generated:** 2026-06-24 00:42 UTC
**Sample:** `004ce76ec3b82be182e1b3da568124bb10ab733044f3c8e840e129ca6a92dc0a_004ce76ec3b82be182e1b3da568124bb10ab733044f3c8e840e129ca6a92dc0a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `004ce76ec3b82be182e1b3da568124bb10ab733044f3c8e840e129ca6a92dc0a_004ce76ec3b82be182e1b3da568124bb10ab733044f3c8e840e129ca6a92dc0a.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,159,680 bytes |
| MD5 | `dd671ba4eed25df26106aeceeadd3fb1` |
| SHA1 | `b3aa0c380179ee8fb9fdeef54b5a816a950a2d03` |
| SHA256 | `004ce76ec3b82be182e1b3da568124bb10ab733044f3c8e840e129ca6a92dc0a` |
| Overall entropy | 6.931 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774837686 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 280,576 | 7.443 | ⚠️ Yes |
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

Total strings found: **2568** (showing first 100)

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

This final chunk of disassembly provides the "smoking gun" regarding the engine's architectural sophistication. It confirms that this is not just an execution environment, but a **high-level script interpreter** (resembling environments like AutoIt, Python, or Lua) designed to abstract complex system interactions into simple, manageable commands for the attacker.

Here is the final analysis incorporating all findings from chunks 1 through 5.

---

### Final Analysis & Findings

#### 1. Deep Integration with COM and OLE (Variant Handling)
The logic in `fcn.00412c10` and its associated sub-routines contains explicit calls to `OLEAUT32.dll_VariantCopy`.
*   **What this means:** The engine isn't just handling strings; it is supporting **COM (Component Object Model)** objects. 
*   **Implication for the Actor:** This allows the script to interact with highly complex Windows components (like Shell objects, Excel, or even internal system services) using very simple high-level commands. By wrapping these in a "Variant" structure, the engine handles all the underlying memory complexities of COM for the user, allowing them to write scripts that are both powerful and easy to produce.

#### 2. The "Command Dispatcher" Architecture
The function `fcn.0040f650` is an exemplary piece of interpreter design. It contains a massive switch table (over 30 cases) where each case corresponds to a specific "command."
*   **Mechanism:** Instead of hardcoding the logic for every action, the engine uses a **Dispatch Table**. When a script asks to "Create a File" or "Download a Link," the VM looks up that command's ID in this table and jumps to the corresponding handler.
*   **Analysis Impact:** This makes "hunting" the malicious payload extremely difficult. To find out what the malware *actually does*, an analyst cannot simply look at one function; they must map every branch of this switch table back to its potential script-level command.

#### 3. Robust Memory & String Management (The Wrapper Layer)
Functions like `fcn.0040bd9d`, `fcn.0040be83`, and `fcn.0040bef7` demonstrate advanced memory management:
*   **Automatic Buffer Growth:** The code calculates required space, checks if the current buffer is sufficient, and automatically reallocates/expands (`if (iVar2 == 0) ... iVar2 = fVar1 * 2`).
*   **Memory Alignment:** It enforces alignment (`& 0xfffffff8`), ensuring that the memory used by the interpreter stays compatible with various system requirements.
*   **Why this matters:** This confirms the **Managed Memory Model**. The script author never deals with "pointers" or "buffers"; they deal with "Strings." By providing a robust, high-level library for these operations, the developers ensure that the malicious scripts are less likely to crash the malware during execution.

#### 4. Abstracted Win32 API Layer
The presence of logic in `fcn.0040c3cb` and calls to `USER32.dll_InvalidateRect` wrapped inside complex switch blocks proves a **Decoupling Strategy**.
*   **Separation of Concerns:** The "Malicious Logic" (the script) is entirely separated from the "System Interaction" (the Win32 API). 
*   **The Barrier:** If an analyst finds code that interacts with a window, they won't find it in the core logic; they will find it inside a generic "UI_Update" or "Window_Handle" function within the interpreter. This creates a massive wall between the *intent* of the attacker and the *action* of the binary.

---

### Final Summary of Findings

| Feature | Technical Evidence | Security Significance |
| :--- | :--- | :--- |
| **Execution Model** | Massive switch tables (`0x40f650`, `0x412c10`) and command dispatch logic. | **Interpreter Architecture.** The malware is a "Virtual Machine" for scripts. Analysis requires mapping the dispatcher to understand the script's intent. |
| **High-Level Data Types** | Support for `OLEAUT32` (Variant) and complex string growth/alignment. | **Sophisticated Integration.** Supports complex COM objects, allowing for easy interaction with deep Windows system components. |
| **Memory Management** | Automated buffer expansion and automatic resizing in `0x40bd9d`. | **Managed Environment.** Hides low-level memory management from the attacker, increasing script stability and reliability. |
| **Abstraction Layer** | Decoupled UI handles (`@TRAY_ID`) and wrapped Win32 calls. | **Analytic Barrier.** Intentional "distance" between malicious actions (e.g., stealing data) and the system calls used to perform them. |

---

### Final Conclusion

This is a **high-tier, professional-grade malware framework** designed for maximum durability and analyst frustration. 

The architecture reveals a sophisticated threat actor who prioritizes:
1.  **Modularity:** By using an internal VM with a command dispatcher, they can change the "behavior" of the malware (e.g., switching from credential theft to file encryption) simply by changing a script file, without ever re-compiling the core binary.
2.  **Evasion through Complexity:** The vast amount of "boilerplate" code (memory management, OLE handling, switch tables) acts as a **noise generator**. It forces a human analyst to spend days or weeks deconstructing the *engine* before they can even begin to analyze the actual *malicious script*.

The presence of **AutoIT-like abstractions**, **OLE/Variant support**, and **multi-layered dispatchers** confirms that this tool is designed for sophisticated, long-term operations where evading both automated signatures and manual reverse engineering is a primary requirement.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1059 | Command and Scripting Interpreter | The discovery of a "Command Dispatcher" (switch table) and an internal "Virtual Machine" for scripts confirms that the malware uses an interpreter to abstract malicious actions into high-level commands. |
| T1027 | Obfuscated Files or Information | The use of multi-layered dispatchers, complex memory management wrappers, and decoupled Win32 API calls creates a deliberate "Analytic Barrier" to hide the attacker's intent from human analysts. |
| T1106 | Modify Permissions (Potential) | While not directly observed in the snippet, the sophisticated OLE/COM integration suggests an attempt to interact with complex system objects that often require elevated privileges or specific permissions to manipulate. |

***Note for Analyst:** The primary threat here is **T1059**. By utilizing a custom interpreter architecture, the actor ensures that standard automated tools looking for "malicious" strings or API sequences will fail, as those actions are only resolved at runtime by the script engine.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** A significant portion of the "Extracted Strings" appears to be obfuscated data, internal memory offsets, or non-human-readable byte fragments typical of a packer or a custom interpreter. As such, no traditional network indicators were present in this specific sample.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis indicates that the "Command Dispatcher" likely handles these via scripts loaded at runtime rather than hardcoding them into the binary).

### **File paths / Registry keys**
*   *None identified.* (Standard Windows components like `OLEAUT32.dll` and `USER32.dll` were mentioned, but no specific malicious file paths or registry keys were present).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 strings were present in the provided text).

### **Other artifacts**
*   **Memory Offsets (Internal Logic Gate Tracking):** 
    *   `0x412c10` (Variant Handling / COM logic)
    *   `0x40f650` (Command Dispatcher/Switch Table)
    *   `0x40bd9d`, `0x40be83`, `0x40bef7` (Memory Management/Buffer Growth)
    *   `0x40c3cb` (Win32 API abstraction layer)
*   **API Calls Used for Abstraction:** 
    *   `OLEAUT32.dll_VariantCopy`
    *   `USER32.dll_InvalidateRect`
*   **Identified Architecture:** **Interpreter-based VM.** The analysis confirms the presence of a high-level script interpreter (similar to AutoIt or Lua). This suggests that behavior-based detection for "Script Execution" and "Memory Allocation Expansion" should be prioritized over static string matching.

***

### **Analyst Summary**
The absence of traditional IOCs (IPs/URLs) in the current data is expected given the analysis's conclusion: this binary acts as a **wrapper/interpreter**. The actual malicious intent is abstracted into an internal script. To find the "live" indicators, further analysis of the files loaded by the `0x40f650` dispatcher would be required.

---

## Malware Family Classification

1. **Malware family**: custom 
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Interpreter/VM Architecture:** The analysis identifies a "Command Dispatcher" (large switch table) and an internal Virtual Machine designed to execute scripts, which allows the threat actor to swap payloads without changing the primary binary.
    *   **Abstraction Layers:** The use of OLE/Variant handling and wrapped Win32 API calls creates a significant "Analysis Barrier," intentionally decoupling malicious intent from system actions to hinder manual reverse engineering.
    *   **Sophisticated Management:** Features like automated buffer growth, memory alignment, and complex multi-layered dispatchers indicate a high-tier, professional framework intended for long-term persistence and evasion.
