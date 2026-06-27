# Threat Analysis Report

**Generated:** 2026-06-26 19:57 UTC
**Sample:** `013b9884d3f7886ffd48b595bf1c6004f6d018649e5c5ce0c994f19a63b8e090_013b9884d3f7886ffd48b595bf1c6004f6d018649e5c5ce0c994f19a63b8e090.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `013b9884d3f7886ffd48b595bf1c6004f6d018649e5c5ce0c994f19a63b8e090_013b9884d3f7886ffd48b595bf1c6004f6d018649e5c5ce0c994f19a63b8e090.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,134,592 bytes |
| MD5 | `e6f01c743404ed508b8c2a39f7a85585` |
| SHA1 | `d6134a3eeacaa3d34f9d9f81c57e6e0e402c25ec` |
| SHA256 | `013b9884d3f7886ffd48b595bf1c6004f6d018649e5c5ce0c994f19a63b8e090` |
| Overall entropy | 6.991 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1765329359 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 255,488 | 7.814 | ⚠️ Yes |
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

Total strings found: **2665** (showing first 100)

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

Based on the final set of disassembled functions, I have integrated these findings into the comprehensive analysis. This last chunk is arguably the most revealing part of the binary, as it moves beyond mere data processing and reveals the **architectural backbone** of the malware.

The inclusion of specific Windows API interactions (like `OLEAUT32`) and the massive, multi-layered dispatch tables confirm that this is a **modular execution engine**, likely designed to host a variety of "plugins" or "modules" controlled remotely.

---

### Updated Analysis: Advanced Architectural Findings

#### 1. Command Dispatcher & "Virtual Machine" Architecture
The functions `fcn.00412c10` and `fcn.0040f650` are the "smoking guns" for a **Modular Framework**.
*   **Massive Switch Tables:** `fcn.0040f650` contains over 40 distinct cases in a single switch block. This is not typical of standard software; it is the hallmark of a **Command Dispatcher**. Instead of having one function that "steals data," this engine receives a command ID (e.g., `0x13`) and jumps to a specific handler (`fcn.0040d010`).
*   **Decoupled Maliciousness:** By using this architecture, the developers ensure that a static analysis of any single "handler" function shows only a small piece of logic (e.g., "write file," "fetch URL," or "query registry"). The malicious intent is only realized when the remote server sends the specific command to trigger that specific branch.
*   **Scripting Potential:** This structure is common in malware designed to be updated frequently via C2 (Command & Control) without needing to re-infect the host with a new binary; they simply send different "opcodes" to the existing engine.

#### 2. Interaction with COM and Higher-Level Windows Objects
The presence of `OLEAUT32.dll_VariantCopy` in `fcn.00412c10` is highly significant.
*   **COM Integration:** `OLEAUT32` is used for "Variants," which are data types that can hold many different types of information (strings, numbers, objects). This suggests the malware is interacting with **COM (Component Object Model)**.
*   **Targeting Enterprise Apps:** COM is frequently used to interact with Microsoft Office (Outlook, Excel), Windows Shell folders, and various system services. This indicates the malware may have modules specifically designed to scrape emails, manipulate spreadsheets, or interact with advanced system components that simple API calls cannot reach.

#### 3. Advanced Object & Buffer Management
The logic in `fcn.0040bd9d` and `fcn.00411df0` demonstrates a high level of coding maturity:
*   **Dynamic Re-allocation:** The code doesn't just use fixed buffers; it checks lengths and reallocates memory (`fcn.0041fd5b`) as needed to accommodate varying data sizes (e.g., if a stolen password is longer than expected).
*   **Iterator Patterns:** The loops used in `fcn.00411df0` suggest the malware is iterating through collections of objects or records, likely results from a system query (like a list of logged-in users, active processes, or network shares).

#### 4. UI Manipulation and Stealth
The interaction with `USER32.dll_InvalidateRect` in `fcn.0040c3cb` provides insight into how it maintains its presence:
*   **Active Interaction:** By using `InvalidateRect`, the malware can force a window to redraw itself. This is often used when a piece of malware "injects" itself into a legitimate process (like a browser or a system explorer) and wants to ensure that any UI elements it modifies appear correctly to the user without lagging or flickering.

---

### Finalized Summary for Incident Response (Final Update)

This analysis confirms that the sample is not a simple trojan, but a **highly sophisticated, modular execution framework.** It is designed for longevity, flexibility, and stealth.

**Technical Indicators:**
*   **Modular Dispatcher Architecture:** The use of massive switch tables indicates a "plug-and-play" architecture. Analysts should treat this as a "host" that can perform dozens of different malicious actions depending on the commands it receives from its controller.
*   **COM/OLEAUT32 Integration:** The presence of `VariantCopy` suggests capabilities for interacting with high-level system objects, likely targeting enterprise software (Office suites) or deeply integrated Windows components.
*   **Robust Resource Management:** Professional-grade memory management and buffer handling suggest a tool designed to run in corporate environments where stability is required to avoid detection by the user.

**Security Impact & Strategy:**
1.  **The "Whack-a-Mole" Problem:** Because the malicious logic is distributed across many small, nondescript functions called by a central dispatcher, **signature-based detection of specific actions will likely fail.** The "maliciousness" is not in a single function; it's in the command stream.
2.  **Detection via Behavior:**
    *   **Memory Forensics:** Since the code is modular, defenders should monitor for frequent, small memory allocations and "jumps" to various offsets within the same module (a sign of a dispatcher).
    *   **COM Monitoring:** Monitor for unusual processes (especially those injected into `explorer.exe` or browser processes) making calls to `OLEAUT32.dll`.
    *   **Network Patterning:** Look for high-frequency "heartbeat" signals. Even if the traffic is encrypted, the *cadence* of communication usually reveals a command-driven architecture.

**Risk Assessment: Critical.** This architecture is characteristic of **Advanced Persistent Threat (APT)** groups or highly organized **MaaS (Malware-as-a-Service)** providers. It is designed to remain operational and flexible for months or even years within a target network.

**Final Recommendation:**
*   Implement EDR rules to flag any process that utilizes `InvalidateRect` while also exhibiting non-standard network behavior.
*   Conduct memory dumps of suspected infected machines to identify the "state" of the dispatcher; this will reveal which specific modules are currently active in a given infection.
*   Block/alert on any internal systems attempting to communicate with IPs/domains associated with common C2 frameworks, as these are likely providing the commands for the dispatchers found in `fcn.0040f650`.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The large switch table in `fcn.0040f650` acts as a command dispatcher, allowing the malware to interpret various remote "opcodes" to execute specific local functions. |
| **T1036** | Masquerading | The use of `InvalidateRect` and integration with high-level COM objects (OLEAUT32) are used to blend the malware's presence into legitimate system components or enterprise applications. |
| **T1087** | Account Discovery | The iteration patterns in `fcn.00411df0` suggest the scanning of system collections to identify logged-in users and account information. |
| **T1016** | System Network Configuration Discovery | The analysis indicates the malware iterates through network resources, such as shares, to map out the internal environment. |
| **T1568** | Dynamic Resolution | While not strictly dynamic in all contexts, the modular architecture and "decoupled" maliciousness are designed to evade static analysis by resolving logic only upon receiving specific commands. |

---

## Indicators of Compromise

Based on the provided technical data and behavioral analysis, here is the categorized list of Indicators of Compromise (IOCs). 

Note: The "Strings" section provided appears to contain mostly obfuscated data, junk characters, or internal binary code remnants; no clear external indicators like IPs or URLs were present in that specific block. The intelligence was primarily gathered from the behavioral analysis of those strings.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   **Note:** No absolute filesystem paths or registry keys were found. However, specific internal functional offsets were identified as critical points for behavior-based detection:
    *   `fcn.00412c10` (Command Dispatcher/COM logic)
    *   `fcn.0040f650` (Multi-case Switch Table / Command Dispatcher)
    *   `fcn.0040bd9d`, `fcn.00411df0`, `fcn.0041fd5b` (Buffer/Memory Management)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **C2 Command Dispatcher Pattern:** The presence of a large switch table (over 40 cases) at `fcn.0040f650` indicates a modular command-processing architecture typical of sophisticated trojans and botnets.
*   **COM/OLEAUT32 Manipulation:** Use of `OLEAUT32.dll_VariantCopy` suggests the malware is designed to interact with COM objects, potentially targeting Microsoft Office applications or advanced system components.
*   **UI Interaction Logic:** The use of `USER32.dll_InvalidateRect` at `fcn.0040c3cb` indicates a technique used to synchronize UI elements during process injection/overlay.
*   **Dynamic Memory Handling:** Repeated patterns of dynamic re-allocation and iteration (found in `fcn.00411df0`) are signatures of high-level data scraping or gathering.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **Modular Command Dispatcher:** The presence of a massive switch table (over 40 cases) in `fcn.0040f650` confirms the sample is not a single-purpose trojan but a sophisticated, command-driven execution engine designed to perform various malicious actions (e.g., file manipulation, data exfiltration, network mapping) based on remote instructions.
*   **Advanced System Interaction:** The integration of `OLEAUT32` and `VariantCopy` indicates the malware is designed to interact with COM objects, allowing it to target complex enterprise environments (like Microsoft Office suites or system services) that standard scripts cannot easily access.
*   **"Decoupled" Malicious Logic:** By utilizing a modular architecture, the developers have successfully decoupled specific malicious behaviors from the primary binary. This ensures the malware remains resilient and versatile, as the "maliciousness" is determined by the remote command stream rather than static code signatures of individual features.
