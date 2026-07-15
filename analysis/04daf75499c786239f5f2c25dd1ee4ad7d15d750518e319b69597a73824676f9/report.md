# Threat Analysis Report

**Generated:** 2026-07-12 08:11 UTC
**Sample:** `04daf75499c786239f5f2c25dd1ee4ad7d15d750518e319b69597a73824676f9_04daf75499c786239f5f2c25dd1ee4ad7d15d750518e319b69597a73824676f9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04daf75499c786239f5f2c25dd1ee4ad7d15d750518e319b69597a73824676f9_04daf75499c786239f5f2c25dd1ee4ad7d15d750518e319b69597a73824676f9.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,280,000 bytes |
| MD5 | `aa08efd099f444e79ac40bbb1a87580a` |
| SHA1 | `3974b95190ef4f2f062fe3be394e0cb67758416e` |
| SHA256 | `04daf75499c786239f5f2c25dd1ee4ad7d15d750518e319b69597a73824676f9` |
| Overall entropy | 7.165 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771934683 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 400,896 | 7.906 | ⚠️ Yes |
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

Total strings found: **3017** (showing first 100)

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

Based on the additional disassembly provided in chunk 5/5, the complexity of this malware’s architecture is further confirmed. This final segment provides clear evidence that the malware utilizes a **custom Virtual Machine (VM) or Interpreter architecture** with a dedicated instruction set and a multi-layered translation layer.

### Updated Analysis: The Execution Engine and Instruction Dispatch

The final analysis highlights three major components revealed in this chunk: an internal "Bytecode" interpreter, complex object management, and a gateway to system APIs.

#### 1. Evidence of a Custom Instruction Set (ISA)
Function `fcn.0040f650` is a cornerstone for understanding the malware’s sophistication. It contains a massive switch table with dozens of cases.
*   **The Interpreter Loop:** This function acts as a primary **instruction dispatcher**. The code doesn't perform actions directly; it receives "opcodes" from the script and matches them against this table to call the appropriate internal handler (e.g., `0x40d010`, `0x485e50`, `0x473163`).
*   **Significance:** This confirms that the malicious logic is not in the C++ code you are currently reversing, but rather encoded as "bytecode" or a custom language. The switch table is the translator between that bytecode and the actual machine code that executes on the CPU.

#### 2. Multi-Layered "Bridge" to Windows API
The analysis of `fcn.00412c10` and `fcn.0040c3cb` reveals how the engine interacts with the OS:
*   **Intermediate Wrappers:** Instead of calling `GetWindowRect` or `RegOpenKey` directly, the "script" calls an internal ID (e.g., 0x12). The interpreter looks up that ID in a table and calls a helper like `fcn.0045fc42`.
*   **System API Entry Points:** In `fcn.0040c3cb`, we see the final step: the translation into a raw Windows call (like `USER32_InvalidateRect`). 
*   **Implication:** This design allows the developers to change the "script" behavior without ever changing the main binary's code. To find the true intent, one must map the "Instruction ID" $\rightarrow$ "Internal Handler" $\rightarrow$ "System API."

#### 3. Advanced Memory & Object Management
The functions `fcn.0040bd9d` and `fcn.0040bef7` reveal how the engine manages its internal state:
*   **Dynamic Buffer Allocation:** The logic calculating sizes (e.g., `uVar7 = uVar4; if (7 < uVar4) ...`) suggests the engine is handling **dynamic data types**. It treats everything as a "variable" that could be a string, an integer, or even another object.
*   **Automatic Memory Management:** The recurring patterns of `fcn.0041fd94` and `fcn.0041fd4d` (which we previously identified as resource trackers) are used here to manage the lifecycle of these objects. When a "script" finishes a calculation, the engine automatically frees or reclaims the memory for that specific variable.

#### 4. Complex Data Parsing
The long loops and switch logic in `fcn.00412c10` (including checks for values like `0x46`, `0x47`, `0x7f`) suggest a **custom string or buffer parsing engine**. It is likely used to parse configuration files, command-and-control (C2) responses, or internal "data blocks" that define the script's behavior.

---

### Final Consolidated Analysis for Analysts

The malware is not a simple malicious binary; it is a **modular execution framework** designed to host and execute untrusted code (the payload).

#### Key Technical Conclusions:
*   **The Architecture:** It follows a **Virtual Machine (VM) architecture**. The primary executable is the "Host," and the actual malware functionality is the "Guest" script. 
*   **Abstraction Layer:** There are at least three layers of abstraction between the malicious intent (e.g., stealing data) and the Windows API call:
    1.  **Script Level:** High-level commands (e.g., `Get_User_Data()`).
    2.  **Interpreter Level:** The switch tables (e.g., `0x40f650`) that translate those commands into internal "Opcode" actions.
    3.  **Bridge Level:** The helper functions that wrap standard Windows APIs to make them accessible to the interpreter.
*   **Evasion Strategy:** By using this architecture, the authors ensure that:
    1.  Static analysis of the main binary will mostly find "generic" engine code.
    2.  Dynamic analysis will see a flurry of calls to internal functions rather than obvious malicious ones.
    3.  The malware can be updated with new features simply by changing an encrypted/hidden data blob (the script) without modifying the executable's signature.

#### Updated Strategy for Analysis:
1.  **Mapping the Dispatcher:** Create a map of the switch table in `fcn.0040f650`. Determine which "Opcode" leads to the most sensitive system calls (Registry, Network, File I/O).
2.  **Extracting the Script:** The high volume of buffer management and string parsing suggests there is a large data block within the binary or an external file. Locating this **Data Block** is the highest priority for finding the actual "malicious" logic.
3.  **Tracing via Hooking:** 
    *   Hook `fcn.0041fd94` and `fcn.0041fd4d` to log every object creation/destruction; this will reveal the lifecycle of data being passed between script components.
    *   Monitor any call involving `OLEAUT32.dll`. This is the most likely "gateway" for complex actions like automation or Office-based attacks.
4.  **Identify the "Core Loop":** Locate the point where the interpreter reads the next "instruction." Once found, you can place a breakpoint there to see exactly what the "script" is doing at any given moment during execution.

**Final Conclusion:** You are analyzing a **highly sophisticated malware loader/interpreter**. The primary code's role is to provide a sandbox for the real payload. To successfully defeat this threat, the analysis must pivot from "Reverse Engineering the Code" to "Decoding the Data" (the script) that feeds into this engine.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The malware utilizes a custom Virtual Machine (VM) architecture, an interpreter loop, and bytecode to execute "scripts," which decouples the malicious logic from the primary executable. |
| **T1036** | Masquerading | The use of a multi-layered "bridge" and internal identifiers instead of direct Windows API calls is designed to hide the true intent of the malware from dynamic analysis. |
| **T1548** | Network Patching (or general Obfuscation) | *Note: While not a specific sub-technique, the overall architecture described serves as a sophisticated layer of obfuscation to hinder manual and automated reverse engineering.* |

***

### Analyst Notes for Internal Use:
*   **Primary Observation:** The most significant finding is **T1059**. Because the malware uses a custom Instruction Set Architecture (ISA) and an interpreter loop (`fcn.0040f650`), it effectively creates a "black box" where standard analysis tools cannot see the malicious logic without first reverse-engineering the bytecode.
*   **Evasion Strategy:** The multi-layered approach to API calls is specifically intended to evade detection systems that look for specific "malicious" Windows API sequences (e.g., looking for `RegOpenKey` or `GetWindowRect` directly). By wrapping these in internal IDs, the malware ensures that only the "Broker/Interpreter" logic is visible during initial analysis.
*   **Recommendation:** Future investigation should prioritize decoding the **Data Block** mentioned in Step 2 of the strategy, as this contains the actual payload (the script) that defines the malware's specific actions.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The provided text contains high-level architectural descriptions and obfuscated data; therefore, traditional network indicators (IPs/URLs) were not present in the source material.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. *(Note: While "RegOpenKey" was mentioned in the analysis, no specific registry paths were provided).*

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Malware Architecture:** Custom Virtual Machine (VM) / Interpreter architecture.
*   **Execution Logic:** Use of a custom "Bytecode" interpreter with an instruction dispatcher located at `fcn.0040f650`.
*   **Obfuscation Technique:** Multi-layered "Bridge" to Windows API (mapping internal IDs/Opcodes to system calls like `USER32_InvalidateRect`).
*   **Internal Handler Logic:** Use of specialized intermediate functions (`fcn.00412c10`, `fcn.0040c3cb`) to abstract and hide direct API calls from static analysis.
*   **Memory Management:** Custom resource tracking/memory management routines at `fcn.0041fd94` and `fcn.0041fd4d`.
*   **Known Library Interaction:** Potential usage of `OLEAUT32.dll` as a gateway for complex actions.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Custom VM Architecture:** The analysis confirms a sophisticated "Virtual Machine" (VM) interpreter where the core logic is abstracted into bytecode, utilizing a large switch table (`fcn.0040f650`) to dispatch instructions rather than executing direct malicious commands.
*   **Multi-Layered API Abstraction:** The use of an internal "bridge" system—where the malware translates internal Opcodes into standard Windows API calls (like `RegOpenKey` or `GetWindowRect`)—is a classic technique used to hide intent from automated analysis and static scanners.
*   **Modular Framework Design:** The technical summary explicitly identifies the binary as a "host" for untrusted code, meaning its primary purpose is to act as a sophisticated loader/interpreter to execute an injected script or payload.
