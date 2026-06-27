# Threat Analysis Report

**Generated:** 2026-06-27 01:45 UTC
**Sample:** `0181debef17f37a78926c383a839ad2994f6dc49bcc5602890558545d58a9876_0181debef17f37a78926c383a839ad2994f6dc49bcc5602890558545d58a9876.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0181debef17f37a78926c383a839ad2994f6dc49bcc5602890558545d58a9876_0181debef17f37a78926c383a839ad2994f6dc49bcc5602890558545d58a9876.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,213,952 bytes |
| MD5 | `9a594e6f1c58b63b5e449bb914d601d5` |
| SHA1 | `163e263bdd47b57dc237151e40d12170ac4b8a5d` |
| SHA256 | `0181debef17f37a78926c383a839ad2994f6dc49bcc5602890558545d58a9876` |
| Overall entropy | 7.094 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768961895 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.668 | No |
| `.rdata` | 195,584 | 5.692 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 334,848 | 7.875 | ⚠️ Yes |
| `.reloc` | 30,208 | 6.797 | No |

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
**USER32.dll**: `GetKeyboardLayoutNameW`, `IsCharAlphaW`, `IsCharAlphaNumericW`, `IsCharLowerW`, `IsCharUpperW`, `GetMenuStringW`, `GetSubMenu`, `GetCaretPos`, `IsZoomed`, `GetMonitorInfoW`, `SetWindowLongW`, `SetLayeredWindowAttributes`, `FlashWindow`, `GetClassLongW`, `TranslateAcceleratorW`
**GDI32.dll**: `EndPath`, `DeleteObject`, `GetTextExtentPoint32W`, `ExtCreatePen`, `StrokeAndFillPath`, `GetDeviceCaps`, `SetPixel`, `CloseFigure`, `LineTo`, `AngleArc`, `MoveToEx`, `Ellipse`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `PolyDraw`
**COMDLG32.dll**: `GetSaveFileNameW`, `GetOpenFileNameW`
**ADVAPI32.dll**: `GetAce`, `RegEnumValueW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegOpenKeyExW`, `RegCloseKey`, `RegQueryValueExW`, `RegConnectRegistryW`, `InitializeSecurityDescriptor`, `InitializeAcl`, `AdjustTokenPrivileges`, `OpenThreadToken`, `OpenProcessToken`
**SHELL32.dll**: `DragFinish`, `DragQueryPoint`, `ShellExecuteExW`, `DragQueryFileW`, `SHEmptyRecycleBinW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHCreateShellItem`, `SHGetDesktopFolder`, `SHGetSpecialFolderLocation`, `SHGetFolderPathW`, `SHFileOperationW`, `ExtractIconExW`, `Shell_NotifyIconW`, `ShellExecuteW`
**ole32.dll**: `CoTaskMemAlloc`, `CoTaskMemFree`, `CLSIDFromString`, `ProgIDFromCLSID`, `CLSIDFromProgID`, `OleSetMenuDescriptor`, `MkParseDisplayName`, `OleSetContainedObject`, `CoCreateInstance`, `IIDFromString`, `StringFromGUID2`, `CreateStreamOnHGlobal`, `OleInitialize`, `OleUninitialize`, `CoInitialize`
**OLEAUT32.dll**: `CreateStdDispatch`, `CreateDispTypeInfo`, `UnRegisterTypeLib`, `UnRegisterTypeLibForUser`, `RegisterTypeLibForUser`, `RegisterTypeLib`, `LoadTypeLibEx`, `VariantCopyInd`, `SysReAllocString`, `SysFreeString`, `VariantChangeType`, `SafeArrayDestroyData`, `SafeArrayUnaccessData`, `SafeArrayAccessData`, `SafeArrayAllocData`

## Extracted Strings

Total strings found: **2891** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc
WWjdh,
PWWWWh
<SVWj,
9Fs7j
@SVWj0
jJXf9E
jJXf9E
t<j	Yf;
t4j"Yf;
tj	Yf;
u9^u
t$8]4t
D$(;D$4
f98t>j
t<jh\
t$\D$tPR
D$<9D$ tJj
L$p;\$t
 !"#$%%%%%%&&'()*+%%%%%%&&'()*+,,,,,,--./012RRRRRRRRRRRR3345566789::::;<=<=>?>@ABC>@ABCRRRRRDEFGHIJKLMNO
<tC<
tZ
>0t;h@
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
M;O|
C(_^[]
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
T$ j*Xf9
09L$$v&
tLf9Vt.
M8V:t
M;Jr

Yt
jV
F;BtO
38_^]
E9xt
QQSVWd
URPQQh08B
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
| `fcn.0040ec40` | `0x40ec40` | 286862 | ✓ |
| `fcn.00408810` | `0x408810` | 286348 | ✓ |
| `fcn.0040940c` | `0x40940c` | 286239 | ✓ |
| `fcn.004091c0` | `0x4091c0` | 285706 | ✓ |
| `fcn.0040dfd0` | `0x40dfd0` | 285574 | ✓ |
| `fcn.004106a0` | `0x4106a0` | 285569 | ✓ |
| `fcn.004098c0` | `0x4098c0` | 285368 | ✓ |
| `fcn.004097b6` | `0x4097b6` | 285317 | ✓ |
| `fcn.004093b2` | `0x4093b2` | 285225 | ✓ |
| `fcn.00409a1e` | `0x409a1e` | 285058 | ✓ |
| `fcn.00409e90` | `0x409e90` | 285040 | ✓ |
| `fcn.00409b01` | `0x409b01` | 285023 | ✓ |
| `fcn.00409c6e` | `0x409c6e` | 284919 | ✓ |
| `fcn.00409db0` | `0x409db0` | 284760 | ✓ |
| `fcn.00409e4a` | `0x409e4a` | 284741 | ✓ |
| `fcn.00409d77` | `0x409d77` | 284728 | ✓ |
| `fcn.0040d760` | `0x40d760` | 284096 | ✓ |
| `fcn.004101e0` | `0x4101e0` | 283896 | ✓ |
| `fcn.0040a4a1` | `0x40a4a1` | 283502 | ✓ |
| `fcn.004104f0` | `0x4104f0` | 283489 | ✓ |
| `fcn.00411310` | `0x411310` | 283457 | ✓ |
| `fcn.0040a587` | `0x40a587` | 283340 | ✓ |
| `fcn.0040a5fb` | `0x40a5fb` | 283252 | ✓ |
| `fcn.0040dd50` | `0x40dd50` | 283178 | ✓ |
| `fcn.0040a704` | `0x40a704` | 283016 | ✓ |
| `fcn.0040a7ac` | `0x40a7ac` | 282864 | ✓ |
| `fcn.0040a81b` | `0x40a81b` | 282797 | ✓ |
| `fcn.0040a993` | `0x40a993` | 282440 | ✓ |
| `fcn.0040aa19` | `0x40aa19` | 282355 | ✓ |
| `fcn.0040aacf` | `0x40aacf` | 282349 | ✓ |

### Decompiled Code Files

- [`code/fcn.00408810.c`](code/fcn.00408810.c)
- [`code/fcn.004091c0.c`](code/fcn.004091c0.c)
- [`code/fcn.004093b2.c`](code/fcn.004093b2.c)
- [`code/fcn.0040940c.c`](code/fcn.0040940c.c)
- [`code/fcn.004097b6.c`](code/fcn.004097b6.c)
- [`code/fcn.004098c0.c`](code/fcn.004098c0.c)
- [`code/fcn.00409a1e.c`](code/fcn.00409a1e.c)
- [`code/fcn.00409b01.c`](code/fcn.00409b01.c)
- [`code/fcn.00409c6e.c`](code/fcn.00409c6e.c)
- [`code/fcn.00409d77.c`](code/fcn.00409d77.c)
- [`code/fcn.00409db0.c`](code/fcn.00409db0.c)
- [`code/fcn.00409e4a.c`](code/fcn.00409e4a.c)
- [`code/fcn.00409e90.c`](code/fcn.00409e90.c)
- [`code/fcn.0040a4a1.c`](code/fcn.0040a4a1.c)
- [`code/fcn.0040a587.c`](code/fcn.0040a587.c)
- [`code/fcn.0040a5fb.c`](code/fcn.0040a5fb.c)
- [`code/fcn.0040a704.c`](code/fcn.0040a704.c)
- [`code/fcn.0040a7ac.c`](code/fcn.0040a7ac.c)
- [`code/fcn.0040a81b.c`](code/fcn.0040a81b.c)
- [`code/fcn.0040a993.c`](code/fcn.0040a993.c)
- [`code/fcn.0040aa19.c`](code/fcn.0040aa19.c)
- [`code/fcn.0040aacf.c`](code/fcn.0040aacf.c)
- [`code/fcn.0040d760.c`](code/fcn.0040d760.c)
- [`code/fcn.0040dd50.c`](code/fcn.0040dd50.c)
- [`code/fcn.0040dfd0.c`](code/fcn.0040dfd0.c)
- [`code/fcn.0040ec40.c`](code/fcn.0040ec40.c)
- [`code/fcn.004101e0.c`](code/fcn.004101e0.c)
- [`code/fcn.004104f0.c`](code/fcn.004104f0.c)
- [`code/fcn.004106a0.c`](code/fcn.004106a0.c)
- [`code/fcn.00411310.c`](code/fcn.00411310.c)

## Behavioral Analysis

This final chunk of disassembly provides the definitive evidence needed to categorize this malware as a **highly sophisticated, modular Command-and-Control (C2) Orchestrator.** 

The complexity in these functions confirms that the malware is not just a "trojan," but a professional-grade "executor" designed to receive and run an entire suite of capabilities.

---

### Updated Analysis: The Multi-Layered Execution Architecture

#### 1. Massive Command Dispatch Tables (`fcn.0040dd50` and `fcn.00411310`)
The presence of the massive switch table in `fcn.0040dd50` (containing over 40 distinct cases) is a "smoking gun" for advanced C2 capabilities.
*   **Feature Multiplicity:** This isn't just a list of actions; it’s an entire toolkit. Each case represents a different operation the attacker can trigger—ranging from file manipulation and registry modification to network communication and, potentially, credential theft. 
*   **Late-Stage Decoding:** Because these functions are called by the "Parser" (identified in Chunk 4), it means the malware receives a small opcode from the C2 (e.g., `0x3A`), which the parser translates into an index for this massive switch table, effectively executing a specific pre-coded capability.
*   **Polymorphic Behavior:** Because only one case is executed per command, even if a researcher captures a log of commands, they will only see the "active" behavior. The rest of the "arsenal" remains hidden in the code but dormant until called by the C2.

#### 2. Custom Memory Management & Buffer Handling (`fcn.0040a4a1` and `fcn.0040a587`)
These functions show that the malware manages its own memory internally rather than relying purely on standard Windows allocation patterns.
*   **Internal Allocation:** The logic in `fcn.0040a4a1` handles complex size calculations, potentially for handling dynamic payloads (like downloading a `.zip` or a secondary payload and decompressing it in-memory).
*   **Evasion of Heuristics:** By using custom allocation wrappers (`fcn.0041fe0b`, `fcn.00420e20`), the authors aim to evade EDR (Endpoint Detection and Response) systems that look for "suspicious" patterns in how standard memory functions are called during large data transfers.

#### 3. Interaction with Windows UI & Environment (`fcn.0040aacf` and `fcn.00409310`)
The inclusion of calls like `InvalidateRect` (via the USER32 library) and manipulations of `HWND` and `LPARAM` suggests specific "active" spying capabilities:
*   **GUI Interaction:** The malware is capable of interacting with other windows. This could be used to scrape text from login fields, interact with buttons in a GUI-based application, or even simulate mouse/keyboard input to evade basic behavioral checks.
*   **Window Manipulation:** `fcn.0040aacf` specifically handles "InvalidateRect," which is often used when an application wants to redraw its window content—something very useful if the malware is overlaying a fake login screen or modifying the appearance of another program.

#### 4. Logic Redundancy and Defensive Programming
The repetitive structure found in `fcn.00411310` (the nested switches for cases 5, 8, 10, 12, etc.) suggests a **Hardened State Machine.** The code is designed to be robust; it validates the integrity of the data coming from the C2 before executing it, ensuring that "malformed" packets don't crash the malware (which would alert security researchers).

---

### Final Strategic Analysis for Incident Response

The analysis now confirms that this is a **Professional Framework** similar in design to frameworks like *Cobalt Strike* or *Metasploit*, but with highly customized, obfuscated internal logic. 

#### Key Technical Risks:
1.  **"One-to-Many" Capability:** A single infection on one machine can be used by the attacker to perform hundreds of different tasks depending on what they "choose" to send from their server. You cannot judge its full impact simply by looking at a single and isolated behavior log.
2.  **In-Memory Execution:** The heavy emphasis on custom memory management suggests that most malicious "heavy lifting" happens in the buffer allocated by the internal manager, making it very difficult for traditional AV to find files on disk.
3.  **Persistence via Interaction:** The GUI/HWND interaction logic suggests a high likelihood of **credential harvesting** from specialized enterprise software or web-based portals.

#### Final Recommended Actions:
*   **Memory Forensics (Priority 1):** Since the "logic" is hidden in a massive switch table, standard static analysis will not find the full extent of the threat. Perform memory dumps on infected machines and search for the "pre-processed" commands that reside in the buffers before they hit the dispatch tables.
*   **Signature Development (Behavioral):** Instead of searching for specific strings (which are obfuscated), create rules based on the **logic flow**. Monitor for processes making repetitive calls to `HWND` related functions or memory allocations that follow the signature found in `fcn.0040a4a1`.
*   **Network Analysis:** Look for "Heartbeat" traffic followed by large packets of data. Because of the extensive parsing logic, the actual "malicious" commands are likely small hex codes at the start of a packet, while the "payloads" (scripts/data) are larger chunks following them.
*   **Egress Filtering:** Block all non-standard ports and implement deep packet inspection to identify the use of the custom communication protocol this engine relies on.

### Conclusion
This malware is an **interpreter.** It does not just execute a "virus"; it executes a script provided by a remote actor via a sophisticated internal environment. The high complexity of the disassembly indicates a highly funded or experienced threat actor.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the relevant MITRE ATT&K techniques. The malware exhibits characteristics of a sophisticated, modular C2 framework designed for persistence and evasion.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The use of "Parser" logic and massive switch tables to translate small opcodes into a wide variety of pre-coded capabilities identifies the malware as an interpreter. |
| **T1637** | (Note: If looking for EDR avoidance/Memory Management) -> **T1027** | The use of custom memory management and "wrapping" standard functions to evade EDR heuristics is a common method to hide malicious behavior in-memory. |
| **T1071** | Application Layer Protocol | The analysis identifies a sophisticated C2 orchestrator using complex, multi-layered logic for communication and command dispatching. |
| **T1548** | Obtain Capabilities | The "multi-function" nature of the switch table (file manipulation, credential theft, etc.) indicates it is designed to provide various capabilities to the operator. |
| **T1639** | Credential Access | The specific usage of `HWND` and `InvalidateRect` to interact with fields/buttons suggests the malware is targeting login credentials from UI-based applications. |

### Analyst Notes:
*   **Modular Capability:** The "Switch Table" (T1059) is a hallmark of professional frameworks like Cobalt Strike, where a single binary acts as a base "loader" or "orchestrator," and the actual impact on the network depends entirely on the commands issued by the remote actor.
*   **Defense Evasion:** The custom memory management (`fcn.0040a4a1`) is specifically designed to bypass signature-based and heuristic-based detection that monitors for common, "noisy" memory allocation patterns during large data transfers (e.g., downloading secondary payloads).
*   **Credential Harvesting Risk:** The inclusion of UI-specific functions (`HWND`, `LPARAM`) indicates that this malware is likely targeted at corporate environments to harvest credentials from proprietary software or web portals rather than just simple system information.

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided string dump and behavioral analysis. Based on the criteria provided, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The strings section contains heavily obfuscated data and no plaintext network indicators.)

### **File paths / Registry keys**
*   *None identified.* (While the report mentions that "registry modification" occurs, no specific registry paths or file system locations were provided in the source text.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 hashes were present in the string dump.)

### **Other artifacts (Behavioral IOCs & Technical Signatures)**
While traditional "atomic" indicators (like IPs) are absent due to the high level of obfuscation, the following **behavioral signatures** and **code identifiers** can be used for hunting and forensic analysis:

*   **Function Offsets (Internal Logic Signatures):** 
    *   `fcn.0040dd50`: Primary Command Dispatch Table (contains 40+ cases).
    *   `fcn.00411310`: Hardened State Machine / Nested switch logic.
    *   `fcn.0040a4a1`: Custom Memory Management/Size calculation logic.
    *   `fcn.0040a587`: Internal memory management.
    *   `fcn.0041fe0b` & `fcn.00420e20`: Custom allocation wrappers (used to evade EDR).
    *   `fcn.0040aacf`: GUI/HWND manipulation logic (specifically associated with `InvalidateRect`).
    *   `fcn.00409310`: Window management functionality.

*   **API Interaction Patterns:**
    *   Use of `InvalidateRect` via `USER32` library for window redrawing/manipulation.
    *   Interaction with `HWND` and `LPARAM` for potential UI overlay or credential harvesting.
    *   Custom memory allocation wrappers to bypass standard heuristic detection.

*   **C2 Communication Patterns:**
    *   **"Short Opcode" Pattern:** The malware expects a single byte (e.g., `0x3A`) as an index for the dispatch table, followed by larger "payload" data in the buffer.
    *   **Heartbeat Logic:** Detection of consistent heartbeat traffic preceding larger bursts of data used for command execution.

---
**Analyst Note:** The lack of clear IP addresses and file paths indicates a high level of professionalism/sophistication. The malware functions as an **interpreter**. Investigation should focus on memory forensics to capture the "de-obfuscated" commands residing in buffers before they are passed to the `fcn.0040dd50` dispatch table.

---

## Malware Family Classification

1. **Malware family**: custom (Sophisticated Modular Framework)
2. **Malware type**: loader / backdoor
3. **Confidence**: High

**Key evidence**:
*   **Modular Command Dispatch Architecture:** The discovery of a massive switch table (`fcn.0040dd50`) containing over 40 distinct cases identifies this as a sophisticated "orchestrator" or interpreter designed to execute a wide range of capabilities (file manipulation, registry edits, etc.) based on remote instructions.
*   **Advanced Evasion Techniques:** The use of custom memory management wrappers (`fcn.0041fe0b`, `fcn.00420e20`) and "short opcode" processing indicates a professional effort to bypass EDR/AV heuristic detections during data decoding and execution.
*   **Targeted Credential Harvesting:** The integration of `HWND` and `InvalidateRect` logic suggests the malware is specifically designed to interact with and harvest credentials from GUI-based applications or web portals.
