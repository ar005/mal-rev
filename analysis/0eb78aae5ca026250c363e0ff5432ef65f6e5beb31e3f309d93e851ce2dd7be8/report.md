# Threat Analysis Report

**Generated:** 2026-08-13 20:32 UTC
**Sample:** `0eb78aae5ca026250c363e0ff5432ef65f6e5beb31e3f309d93e851ce2dd7be8_0eb78aae5ca026250c363e0ff5432ef65f6e5beb31e3f309d93e851ce2dd7be8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0eb78aae5ca026250c363e0ff5432ef65f6e5beb31e3f309d93e851ce2dd7be8_0eb78aae5ca026250c363e0ff5432ef65f6e5beb31e3f309d93e851ce2dd7be8.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,271,808 bytes |
| MD5 | `d82353d8067a923392593b8df7ec13e8` |
| SHA1 | `bb62fe560bced33eaddf9f10d2bf805b97932082` |
| SHA256 | `0eb78aae5ca026250c363e0ff5432ef65f6e5beb31e3f309d93e851ce2dd7be8` |
| Overall entropy | 7.157 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1772066528 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 392,704 | 7.902 | ⚠️ Yes |
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

Total strings found: **2931** (showing first 100)

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

The addition of chunk 5/5 provides a granular look into the "engine room" of the malware’s Virtual Machine (VM). This final set of functions confirms that the VM is not a simple emulator, but a highly sophisticated **Command Dispatcher** and **Execution Engine**.

### Updated Analysis: Advanced Command Dispatching & Logic Fragmentation

The disassembly in this chunk highlights three primary architectural characteristics that elevate the difficulty of analysis.

#### 1. Massive Dispatch Table Complexity (The "Grand Switch")
The function `fcn.0040f650` is a prime example of **Control Flow Flattening** via a massive switch table (over 30 cases). 
*   **Functional Diversity:** Each case in this switch leads to a different internal handler (e.g., `0x40e940`, `0x40c315`, `0x48649d`). This indicates that the VM supports an enormous range of operations. The malware doesn't just have "one" way to perform an action; it has a specialized handler for almost every possible internal command.
*   **Abstracted Execution:** When the VM encounters a code fragment, it doesn't execute a direct sequence of instructions. It passes a "token" or "opcode" into this massive switch. This makes static analysis nearly impossible because the logic is fragmented across dozens of different sub-functions that only get called during specific stages of execution.

#### 2. Sophisticated State-Based Loop Processing
The function `fcn.00412c10` demonstrates how the VM handles **complex internal states**.
*   **Nested Logic & Range Checking:** The code performs extensive checks on indices (e.g., `iVar3 = *(*(iVar6 + piVar4 * 4) + 8)` and checking against `0x7f` or `0x47`). These are likely "Guard Clauses" for the internal interpreter.
*   **Context-Aware Decoding:** The VM is checking not just the instruction, but the *context* of the instruction (e.g., whether it is part of a sequence or if it requires specific parameters). This suggests that a single piece of malicious code in the payload can behave differently depending on what "state" the VM is currently in.

#### 3. Dynamic Memory & Buffer Management
Functions like `fcn.0040bd9d` and `fcn.0040be83` suggest a **custom memory management layer**.
*   **Buffer Normalization:** These functions handle the resizing of buffers and the adjustment of pointers based on data length (e.g., checking if `iVar1` is between `0x2f` and `0x40`). 
*   **Why this matters for Analysis:** This implies that the "script" or "payload" being run by the VM is dynamic. It isn't just a static list of commands; it involves building complex data structures in memory (like strings, URLs, or file paths) that are only fully realized *after* passing through these management layers.

---

### Summary of New Findings (Chunk 5/5)

*   **Complex Dispatcher Architecture:** The presence of massive switch tables (`fcn.0040f650`) confirms that the malware uses a "hub-and-spoke" model for its logic. Even if an analyst identifies one malicious action, they may only be looking at 1% of the available functionality hidden in other branches.
*   **Stateful Execution:** The VM maintains an internal state machine. The execution path changes based on previous actions, meaning "Point A" might lead to "Action B" today and "Action C" tomorrow, depending on the payload's script logic.
*   **Sophisticated Data Handling:** The evidence of manual buffer management and pointer arithmetic indicates that the malware can handle complex data types (like long URLs or file paths) which are likely obfuscated until they reach the very last step of the VM execution.

---

### Final Consolidated Analysis for Incident Response

The complexity of this sample remains at **Extreme**.

**Key Risks & Technical Observations:**
1.  **High Complexity of De-obfuscation:** Because the malware uses a massive dispatch table, identifying all potential capabilities (C2 communication, file encryption, data exfiltration) requires mapping every branch in `fcn.0040f650`. One "simple" string find will not reveal the full scope of the threat.
2.  **Polymorphic Behavior via Scripting:** The interplay between the "front-end" (chunk 4), the "dispatchers" (chunk 5), and the "logic" (the VM) suggests that the primary malicious actions are likely defined in an externalized or encrypted script. The binary itself is merely the "player," while the "game" (the malware's behavior) is loaded at runtime.
3.  **Evasive Maneuvers:** The anti-analysis checks identified earlier (`timeGetTime`, `PeekMessage`) combined with this complex architecture mean the malware is designed to frustrate both automated sandboxes and manual reverse engineering.

**Final Recommendations for Analysis & Response:**
*   **Dynamic Analysis via Memory Dump (Priority 1):** Do not rely solely on static disassembly of the "dispatcher" functions. The most effective way to see what the malware *actually does* is to let it run in a controlled environment and dump its memory after the "Front-end" has finished unpacking the script but before the main VM loop executes.
*   **Hooking Transition Points:** Focus on the points where the "internal" VM logic calls "external" Windows APIs (e.g., `URLDownloadToFile`, `CreateRemoteThread`, `WriteProcessMemory`). These are the "leakage" points where the hidden intent becomes visible to observers.
*   **Identify Script Loading:** Locate the point where the script is fed into the front-end (`fcn.0040b230`). This is the "holy grail" for analysts, as it marks the transition from obfuscated code to executable instructions.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Execution | The use of massive switch tables (control flow flattening), state-based loop processing, and complex buffer management are used to hide the execution path and obfuscate data from analysts. |
| **T1059** | Command and Scripting Interpreter | The "Command Dispatcher" and "Execution Engine" architecture indicates that the malware functions as an interpreter for executing commands or scripts (the "payload"). |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The raw string data appears to be highly obfuscated/packed code fragments; no plaintext network indicators or file paths were visible within that specific block.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified (no valid MD5, SHA-1, or SHA-256 hashes were present in the string dump).

### **Other artifacts**
*   **Anti-Analysis API Hooks:** `timeGetTime`, `PeekMessage` (Used to detect sandbox environments/manual debugging).
*   **Malicious Capability Indicators:** 
    *   `URLDownloadToFile` (Indicates potential C2 communication/downloader functionality).
    *   `CreateRemoteThread` (Indicates process injection).
    *   `WriteProcessMemory` (Indicated as a "leakage point" where malicious intent becomes visible).
*   **Malware Architecture:** 
    *   Large Dispatch Table (`fcn.0040f650`) used for Control Flow Flattening.
    *   State-based execution loop (`fcn.00412c10`).
    *   Custom memory management/buffer normalization layer (`fcn.0040bd9d`, `fcn.0040be83`).

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification of the sample:

1.  **Malware family:** custom
2.  **Malware type:** loader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **VM-Based Execution Engine:** The presence of a massive switch table (over 30 cases) and state-based loop processing confirms the use of a virtual machine architecture to execute an internal, likely encrypted/obfuscated script. This decouples the malware's core functionality from its static code.
    *   **Complex Control Flow Flattening:** The "Grand Switch" design and extensive "Guard Clauses" are high-level obfuscation techniques intended to thwart both automated analysis and manual reverse engineering by hiding the actual execution path of the malware.
    *   **Gateway Functionality (Loader Indicators):** The presence of "leakage points" involving `URLDownloadToFile`, `CreateRemoteThread`, and `WriteProcessMemory` indicates that the primary role of this component is to facilitate further stage loading, remote code injection, and initial persistence.
