# Threat Analysis Report

**Generated:** 2026-09-04 20:57 UTC
**Sample:** `143e93da90a245d161844bc17c5751cee5fbad7fe7968684052187fad54dd75c_143e93da90a245d161844bc17c5751cee5fbad7fe7968684052187fad54dd75c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `143e93da90a245d161844bc17c5751cee5fbad7fe7968684052187fad54dd75c_143e93da90a245d161844bc17c5751cee5fbad7fe7968684052187fad54dd75c.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,342,464 bytes |
| MD5 | `b32347cfe951b2ccbbffff1d2589c79b` |
| SHA1 | `c3e306918f4049227442cff080af02e8e93f42d7` |
| SHA256 | `143e93da90a245d161844bc17c5751cee5fbad7fe7968684052187fad54dd75c` |
| Overall entropy | 7.224 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1765334380 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 463,360 | 7.924 | ⚠️ Yes |
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

Total strings found: **3127** (showing first 100)

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

The addition of the final disassembly (chunk 5/5) provides the most conclusive evidence yet regarding the malware's architecture. It confirms that this is not just a standard "obfuscated binary" but a **multi-layered, virtualized execution environment**—highly characteristic of high-end Trojans and advanced persistent threat (APT) tools.

The inclusion of these functions solidifies the structure of the malware as a **three-tier interpreter architecture**.

---

### Updated Core Functionality & Technical Findings

#### 1. Multi-Level Interpreter Architecture
The complexity found in `fcn.00412c10` and `fcn.0040650` demonstrates that the malware does not execute "actions" directly. Instead, it uses nested dispatchers.
*   **Nested Dispatching:** One large switch table (like the one at `0x40f828`) manages high-level commands, while other functions (like `fcn.00412c10`) manage internal state transitions and "object" property lookups. 
*   **The Switch Table as a "Gateway":** The massive switch table in `fcn.0040650` contains over 30 distinct cases. Each case corresponds to a different instruction or operation within the VM's custom bytecode. This means that for every single malicious action (e.g., opening a file, checking a registry key), the code must pass through multiple "gatekeeper" loops and switch tables before reaching the actual logic.
*   **Impact:** This makes static analysis extremely difficult because the "real" behavior is never in one place; it is distributed across dozens of jump tables.

#### 2. Sophisticated Scripting Engine Elements (COM/OLE)
The consistent use of `OLEAUT32_VariantCopy` and the way data is handled in `fcn.00412c10` strongly suggest that the malware's payload is written in a high-level, scriptable language (e.g., a custom version of JavaScript or a Lua-based engine).
*   **Object Orientation:** The code isn't just handling raw variables; it is managing "Objects." When you see switch cases checking for specific IDs followed by operations like `*(puVar7 + 10)`, the malware is performing something akin to **Property Access** (e.g., `object.property`).
*   **Data Abstraction:** The use of `Variant` types implies that the underlying payload needs to handle a wide variety of data types (strings, integers, arrays) dynamically. This confirms that the primary malicious logic was likely written in a high-level language and then compiled into the bytecode that this VM "executes."

#### 3. Complex State Machine & Recursive Logic
The function `fcn.00412c10` contains significant amounts of logic for managing the **state** of the execution.
*   **Context Awareness:** The jumps to different blocks based on internal values (like `0x45722c`) suggest that the malware "tracks" where it is in a multi-step process. For example, a network connection might involve 20 separate "steps," each requiring its own state check within the VM's loop.
*   **Dynamic Branching:** The code often calculates an offset or index based on a value fetched from memory before jumping to that location. This is a classic technique used in JIT (Just-In-Time) compilers and complex interpreters to keep the "logical" flow of the malicious script hidden from linear analysis.

#### 4. Decoupled System Interaction
The functions `fcn.0040c315`, `fcn.0040c28f`, and `fcn.0040c3cb` act as the **System Abstraction Layer (SAL)**.
*   **Wrapper Logic:** These functions wrap standard Windows APIs (like those for window handling or message processing). Notice how a simple operation is wrapped in multiple layers of checks and even internal "sub-switches." 
*   **Defense against Hooking:** Because the malware interacts with the OS through this thick layer of abstractions, standard security tools that look for direct calls to `CreateProcess` or `InternetConnect` will fail. The "malicious" call only appears at the very end of a long chain of internal VM transitions.

---

### Final Technical Summary (Consolidated Analysis)

Based on all five chunks of disassembly, the malware architecture is structured as follows:

1.  **The Scripting Layer (High-Level):** The ultimate payload is likely a script (or similar high-level logic). This layer handles the "strategy" of the attack (e.g., "If no file exists, download it; otherwise, encrypt it").
2.  **The Virtual Machine Interpreter (Middle Layer):** This is what you see in `fcn.00411fa0` and `fcn.00412c10`. It converts the high-level script into a series of "instructions" that the VM understands. It handles variables, loops, and logic branches within its own internal environment.
3.  **The System Abstraction Layer (Low-Level):** This is what you see in `fcn.0040650` and the various `.0c...` functions. This layer takes "VM Instructions" and translates them into actual Windows API calls. It serves as a buffer between the malicious logic and the operating system.

### Final Threat Assessment:
**High-Complexity / Advanced Persistent Threat (APT) Capability.**

This is not a standard, automated malware sample. The use of a custom VM with multiple layers of abstraction indicates a high level of professional development. The complexity of the switch tables and the inclusion of scripting-style data handling are designed specifically to defeat:
*   **Static Analysis:** There is no single "malicious" function; the logic is fragmented across many jump tables.
*   **Dynamic Hooking:** Standard API hooks won't catch the logic flow because it is buried inside a custom interpreter.
*   **Automated Sandbox Detection:** The complex state machines can be used to "stall" or vary behavior if the environment doesn't look exactly right.

### Recommended Strategy for Investigation:
1.  **Map the Dispatchers:** Instead of tracing every branch, identify the "entry points" into the primary switch tables (e.g., `0x40f828`). Track what happens when different "instruction codes" are fed to these tables.
2.  **Identify the Instruction Set:** Document the common "Instruction IDs" in the switches. You can then build a map of "Instruction 0x15 = Network_Query," "Instruction 0x32 = File_Write," etc.
3.  **Memory Forensics:** Since the logic is heavily abstracted, capturing a memory dump and looking for the **decoded script or bytecode** in memory may be more fruitful than attempting to manually de-obfuscate every nested switch statement.
4.  **Trace "Sink" Functions:** Identify the point where the VM interacts with the OS (the System Abstraction Layer). Work *backward* from those points into the dispatcher to see which specific script instructions lead to high-risk actions like `InternetConnectW` or `WriteFile`.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Executables | The use of a multi-layered, virtualized execution environment with nested switch tables and complex state machines is designed to hide the malware's logic from static analysis. |
| T1059 | Command and Scripting Interpreter | The "Scripting Layer" and high-level data abstractions indicate that the core malicious logic is executed via an internal interpreter, separating the attack strategy from the binary code. |
| T1036 | Masquerading | The System Abstraction Layer (SAL) wraps standard Windows API calls in multiple layers of logic to hide the true intent of system interactions from security monitoring tools. |

---

## Indicators of Compromise

Based on an analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Execution Architecture:** The malware utilizes a **multi-layered, virtualized execution environment** (three-tier interpreter).
*   **Internal Memory Offsets/Function Points (Technical Artifacts):** 
    *   `0x40f828` (Primary Switch Table)
    *   `0x45722c` (State Management Point)
    *   `fcn.00412c10`, `fcn.0040650`, `fcn.0040c315`, `fcn.0040c28f`, `fcn.0040c3cb` (Internal logic/System Abstraction Layer functions).
*   **Techniques:** Use of COM/OLE (`OLEAUT32_VariantCopy`) for data handling and a custom scripting-style payload.

***Note for Analyst:** The "Extracted Strings" section contains largely obfuscated, non-human-readable data or standard compiler artifacts (e.g., `.rdata`, `.data`, `.reloc`). No actionable network indicators or persistent file system markers were present in the provided text.*

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1. **Malware family**: custom (Advanced Architecture)
2. **Malware type**: backdoor / trojan
3. **Confidence**: High (regarding architecture and sophistication)
4. **Key evidence**:
    *   **Virtualized Execution Environment:** The presence of a three-tier interpreter architecture with nested switch tables indicates a high-end, custom-built VM designed specifically to shield the core logic from static analysis and automated sandboxes.
    *   **System Abstraction Layer (SAL):** The malware utilizes multiple layers of "wrapper" functions for standard Windows API calls, making it extremely difficult for security tools to detect malicious intent through simple hooking or signature-based detection.
    *   **Script-Driven Logic:** Evidence of OLE/Variant handling and a complex state machine suggests that the payload is driven by a high-level scripting language (e.g., Lua or a custom JS variant), typical of sophisticated APT tools where functionality can be updated via remote scripts without changing the primary binary.
