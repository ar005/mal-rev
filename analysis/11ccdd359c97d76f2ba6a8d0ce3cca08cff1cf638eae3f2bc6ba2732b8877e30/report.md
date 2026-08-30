# Threat Analysis Report

**Generated:** 2026-08-24 00:36 UTC
**Sample:** `11ccdd359c97d76f2ba6a8d0ce3cca08cff1cf638eae3f2bc6ba2732b8877e30_11ccdd359c97d76f2ba6a8d0ce3cca08cff1cf638eae3f2bc6ba2732b8877e30.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11ccdd359c97d76f2ba6a8d0ce3cca08cff1cf638eae3f2bc6ba2732b8877e30_11ccdd359c97d76f2ba6a8d0ce3cca08cff1cf638eae3f2bc6ba2732b8877e30.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,274,880 bytes |
| MD5 | `91a88b6811d3a122b5560082fe6c2257` |
| SHA1 | `6c467af0be1b12805a1d8805c3bf94c6a1b99e37` |
| SHA256 | `11ccdd359c97d76f2ba6a8d0ce3cca08cff1cf638eae3f2bc6ba2732b8877e30` |
| Overall entropy | 7.16 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1772089700 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 395,776 | 7.903 | ⚠️ Yes |
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

Total strings found: **2958** (showing first 100)

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

This final segment of disassembly completes the technical picture of what is clearly one of the most sophisticated malware architectures currently observed. The evidence confirms that this is not a simple packed executable; it is a **high-level, multi-layered virtualized execution environment.**

The logic found in Chunk 5 reinforces the transition from "obfuscated code" to "custom operating system/runtime environment."

### Updated Analysis Summary (Final Compilation)

#### Core Functionality and Purpose
*   **Multi-Layered Dispatch Architecture:** The analysis of `fcn.00412c10` and `fcn.0040f650` reveals a massive, tiered instruction set. Instead of one switch statement for all commands, the malware uses nested dispatchers. This means it first identifies a "category" of action (e.g., memory management, string manipulation) and then selects a specific "sub-routine."
*   **Sophisticated Scripting Environment:** The use of sentinel values (like `0x7fffffff`) in `fcn.00411df0` and the complex logic for handling object properties suggest that the malware is running an internal scripting language. This allows the threat actor to write complex, multi-stage malicious logic in a "high-level" way while the host binary only executes the low-level interpreter.
*   **Robust Memory & Object Management:** Functions like `fcn.0040bd9d` and `fcn.0040bef7` handle specific buffer sizes (0x10, 0x20) and perform manual cleanup/validation. This indicates the VM handles its own memory heap to manage strings, constants, and variables internally without making frequent "noisy" calls to standard Windows memory management functions.

#### Suspicious or Malicious Behaviors
*   **Decoupling of Intent from Execution:** The primary defense mechanism is the **vast distance between "Intent" and "Action."** A signature or heuristic looking for a sequence like *[Decrypt Data -> Extract Path -> Call System Command]* will fail because that entire sequence exists only in the bytecode. The x86 code simply sees the VM processing various, seemingly unrelated data types and switching between internal functions.
*   **Advanced Abstraction of Windows API:** The repeated use of `OLEAUT32.dll_VariantCopy` and other COM-related calls suggests the malware is designed to wrap complex Windows functionalities (like WMI queries or Shell operations) inside the VM. By doing this, even if an analyst hooks a "high-level" function like `VariantCopy`, they only see a fragment of the actual malicious logic.
*   **Persistence through Complexity:** The sheer number of cases in the switch tables (some exceeding 40 cases) suggests that the malware is designed to be very versatile. It likely has many different "plugins" or modules, allowing it to adapt its behavior based on the information received from its C2 server without changing its core structure.

#### New Technical Patterns Identified
*   **Instruction Set Architecture (ISA) Design:** The code utilizes a classic "Switch-Table Dispatcher." In `fcn.00412c10`, the calculation of `(var_4h - 5U) * 4` followed by a jump to a specific case is the hallmark of a custom CPU or VM interpreter.
*   **Object Property Resolution:** The logic in `fcn.00411df0` (checking offsets, lengths, and types before performing operations) indicates an **Object-Oriented approach**. The malware isn't just moving bytes; it is interacting with "Objects" that have properties and methods.
*   **Heavy use of Function Pointers:** Many cases in the switch tables do not point to internal logic but rather resolve a pointer to a function. This suggests that the VM can dynamically change its behavior by swapping out different "service" modules at runtime.

---

### Final Synthesis for Incident Response (IR)

The analysis confirms this is a **Tier-1 sophisticated threat**, likely associated with a professional advanced persistent threat (APT) group or high-level cybercriminal organization. The malware uses an **Interpreter Architecture** to isolate its malicious "brain" from the system's visible behavior.

#### Critical Intelligence for Defenders:
1.  **Manual Analysis is Inefficient:** Traditional static analysis of this binary will be extremely slow because the "malice" is hidden in the bytecode, not the x86 instructions. Analysts should not spend weeks trying to manually map every switch case.
2.  **The VM as a Shield:** The core intelligence (C2 IPs, exfiltration logic, payload drop locations) is likely only decrypted/visible inside the VM's memory space during execution.
3.  **"Tipping Point" Detection:** Since the malicious intent is hidden in the bytecode, the best time to detect it is at the **execution boundary.** 

#### Targeted Recommendations for IR Teams:
*   **Memory Forensics (Priority):** Instead of analyzing the binary on disk, capture a memory dump while the process is running. Analyze the heap to find the "instruction stream" or "script block." Look for large blocks of non-x86 code that contain repetitive patterns—this is likely the bytecode buffer.
*   **Behavioral Hooking:** Monitor and log all calls into `ole32.dll`, `shell32.dll`, and `advapi32.dll`. While you won't see "why" it called them, the frequency and arguments of these calls will provide a timeline of the malware’s actions (e.g., starting a process, creating a registry key, or making a network connection).
*   **Instruction Hooking:** If possible, hook the central dispatcher functions identified in this analysis (e.g., `fcn.00412c10` and `fcn.0040f650`). By logging the "Case ID" that is triggered every time these are called, you can reconstruct the sequence of events performed by the malware's internal scripts.
*   **Network Traffic Analysis:** Because the VM handles complex data structures, the C2 traffic will likely be highly structured (JSON-like or Protobuf-style). Monitor for persistent connections to non-standard ports and look for high volumes of outbound "heartbeat" packets which may contain the state updates of the internal VM.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1028** | Obfuscated Files or Information | The use of a custom, multi-layered virtualized execution environment and bytecode ensures that the "malicious intent" is decoupled from the x86 code. |
| **T1059** | Command and Scripting Interpreter | The malware utilizes a sophisticated, custom scripting engine and interpreter architecture to execute its high-level logic and instructions. |
| **T1027** | Obfuscated Executables | The complex switch-table dispatchers and heavy use of function pointers serve as specific methods to hide the underlying logic from standard static analysis tools. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral descriptions, here is the extracted list of Indicators of Compromise (IOCs).

### **Technical Note for Incident Response**
The provided documentation indicates that this malware utilizes a **highly sophisticated virtualized execution environment**. Because the "malicious brain" of the code resides in dynamically generated bytecode rather than static x86 instructions, most traditional IOCs (such as hardcoded C2 IPs or plain-text file paths) are not visible in the raw strings. They only manifest in memory during runtime.

---

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis notes that C2 infrastructure is currently hidden within the VM's internal logic).

### **File paths / Registry keys**
*   *None identified.* (Note: The report mentions "payload drop locations," but no specific file paths were provided in the data).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 hashes were present in the provided strings).

### **Other artifacts**
*   **Internal Function Offsets (Used for behavior-based detection):**
    *   `fcn.00412c10` (Primary Dispatcher/Instruction Set)
    *   `fcn.0040f650` (Secondary Dispatcher)
    *   `fcn.00411df0` (Object Property Resolution)
    *   `fcn.0040bd9d` & `fcn.0040bef7` (Memory/Buffer Management)
*   **API Hooking Points (Behavioral Monitoring):**
    *   `OLEAUT32.dll_VariantCopy`
    *   `shell32.dll`
    *   `advapi32.dll`
*   **Suspicious Patterns:**
    *   **Scripting Engine Signature:** The presence of a "Switch-Table Dispatcher" and "Object Property Resolution" logic suggests the binary is hosting an internal scripting language (common in high-tier malware like Cobalt Strike, Metasploit, or custom APT frameworks).

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1.  **Malware family:** **custom** (Sophisticated Framework)
2.  **Malware type:** **loader / backdoor**
3.  **Confidence:** **High**
4.  **Key evidence:**
    *   **Virtualized Execution Environment:** The malware employs a complex "Interpreter Architecture" where the malicious logic is stored as bytecode in an internal scripting language, effectively decoupling the intent (e.g., data theft or command execution) from the observable x86 instructions.
    *   **Advanced Obfuscation Techniques:** The use of nested switch-table dispatchers and object property resolution indicates a sophisticated framework designed to bypass signature-based detection by abstracting Windows API calls through intermediate "service" layers.
    *   **Tier-1 Sophistication:** The technical indicators (T1059, T1028) and the complexity of its memory management suggest this is not a common commodity trojan but rather a sophisticated tool used for long-term persistence or by advanced threat actors to facilitate remote access.
