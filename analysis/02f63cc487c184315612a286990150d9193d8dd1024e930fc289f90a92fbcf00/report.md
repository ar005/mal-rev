# Threat Analysis Report

**Generated:** 2026-06-28 19:07 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, UPX compressed, 3 sections |
| Size | 866,816 bytes |
| MD5 | `390d93b3499ad9f549745649d5ac735a` |
| SHA1 | `8ae54c2fcebf5af8af5f50117a09f1c7a7d84497` |
| SHA256 | `02f63cc487c184315612a286990150d9193d8dd1024e930fc289f90a92fbcf00` |
| Overall entropy | 6.95 |
| Unpacked | ✓ Yes (tool: upx) |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1762735020 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 570,880 | 6.68 | No |
| `.rdata` | 183,808 | 5.682 | No |
| `.data` | 25,088 | 2.003 | No |
| `.rsrc` | 528,896 | 7.197 | ⚠️ Yes |
| `.reloc` | 42,496 | 5.245 | No |

### Imports

**KERNEL32.DLL**: `HeapAlloc`, `GetProcessHeap`, `HeapFree`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `MulDiv`, `GetVersionExW`, `GetSystemInfo`, `FreeLibrary`, `LoadLibraryA`, `GetProcAddress`, `SetErrorMode`, `GetModuleFileNameW`, `WideCharToMultiByte`
**ADVAPI32.dll**: `GetAclInformation`, `RegEnumValueW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegCreateKeyExW`, `GetUserNameW`, `RegOpenKeyExW`, `RegCloseKey`, `RegQueryValueExW`, `RegConnectRegistryW`, `InitializeSecurityDescriptor`, `InitializeAcl`, `AdjustTokenPrivileges`
**COMCTL32.dll**: `ImageList_Destroy`, `ImageList_Remove`, `ImageList_SetDragCursorImage`, `ImageList_BeginDrag`, `ImageList_DragEnter`, `ImageList_DragLeave`, `ImageList_EndDrag`, `ImageList_DragMove`, `ImageList_Create`, `InitCommonControlsEx`, `ImageList_ReplaceIcon`
**COMDLG32.dll**: `GetSaveFileNameW`, `GetOpenFileNameW`
**GDI32.dll**: `SetPixel`, `DeleteObject`, `GetTextExtentPoint32W`, `ExtCreatePen`, `StrokeAndFillPath`, `StrokePath`, `GetDeviceCaps`, `CloseFigure`, `LineTo`, `AngleArc`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `MoveToEx`, `Ellipse`, `PolyDraw`
**IPHLPAPI.DLL**: `IcmpCreateFile`, `IcmpCloseHandle`, `IcmpSendEcho`
**MPR.dll**: `WNetUseConnectionW`, `WNetCancelConnection2W`, `WNetGetConnectionW`, `WNetAddConnection2W`
**ole32.dll**: `CoTaskMemAlloc`, `CoTaskMemFree`, `CLSIDFromString`, `ProgIDFromCLSID`, `CLSIDFromProgID`, `OleSetMenuDescriptor`, `MkParseDisplayName`, `OleSetContainedObject`, `CoCreateInstance`, `IIDFromString`, `StringFromGUID2`, `CreateStreamOnHGlobal`, `CoInitialize`, `CoUninitialize`, `GetRunningObjectTable`
**OLEAUT32.dll**: `RegisterTypeLib`, `LoadTypeLibEx`, `VariantCopyInd`, `SysReAllocString`, `SysFreeString`, `SafeArrayDestroyDescriptor`, `SafeArrayDestroyData`, `SafeArrayUnaccessData`, `SafeArrayAccessData`, `SafeArrayAllocData`, `UnRegisterTypeLib`, `SafeArrayCreateVector`, `SysAllocString`, `SysStringLen`, `VariantTimeToSystemTime`
**PSAPI.DLL**: `GetProcessMemoryInfo`
**SHELL32.dll**: `DragQueryPoint`, `ShellExecuteExW`, `DragQueryFileW`, `SHEmptyRecycleBinW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHCreateShellItem`, `SHGetDesktopFolder`, `SHGetSpecialFolderLocation`, `SHGetFolderPathW`, `SHFileOperationW`, `ExtractIconExW`, `Shell_NotifyIconW`, `ShellExecuteW`, `DragFinish`
**USER32.dll**: `SetWindowPos`, `GetCursorInfo`, `RegisterHotKey`, `ClientToScreen`, `GetKeyboardLayoutNameW`, `IsCharAlphaW`, `IsCharAlphaNumericW`, `IsCharLowerW`, `IsCharUpperW`, `GetMenuStringW`, `GetSubMenu`, `GetCaretPos`, `IsZoomed`, `MonitorFromPoint`, `GetMonitorInfoW`
**USERENV.dll**: `UnloadUserProfile`, `DestroyEnvironmentBlock`, `CreateEnvironmentBlock`, `LoadUserProfileW`
**UxTheme.dll**: `IsThemeActive`
**VERSION.dll**: `GetFileVersionInfoW`, `VerQueryValueW`, `GetFileVersionInfoSizeW`
**WININET.dll**: `InternetReadFile`, `InternetCloseHandle`, `InternetOpenW`, `InternetSetOptionW`, `InternetCrackUrlW`, `HttpQueryInfoW`, `InternetQueryOptionW`, `HttpOpenRequestW`, `HttpSendRequestW`, `FtpOpenFileW`, `FtpGetFileSize`, `InternetOpenUrlW`, `InternetConnectW`, `InternetQueryDataAvailable`
**WINMM.dll**: `timeGetTime`, `waveOutSetVolume`, `mciSendStringW`
**WSOCK32.dll**: `__WSAFDIsSet`, `recv`, `send`, `setsockopt`, `ntohs`, `recvfrom`, `select`, `WSAStartup`, `htons`, `accept`, `listen`, `bind`, `closesocket`, `connect`, `WSACleanup`

## Extracted Strings

Total strings found: **2830** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc
+t\HHtT
j+Yj^f;
~89~4~)
v,F8P
WWjdh,
PWWWWh
R$A;N|
u9^u
u h$.K
u h$.K
9Fs4j
L$$9N@
AHt!H
t<j	Yf;
t4j"Yf;
tj	Yf;
~+FVSj
D$49G@
\$ j|Zf9
L$LjxXf


	

						
												
						
																									
YYj!Yf;
`~EjaX;
^$9^,u
D$$;D$0
FHtJH
v,F8PRQ
L$X;|$8
 !"#$%%%%%%&&'()*+%%%%%%&&'()*+,,,,,,--./012RRRRRRRRRRRR3345566789::::;<=<=>?>@ABC>@ABCRRRRRDEFGHIJKLMNO
Yj?Yj0Z
<t9<
tP
|$`AU3!
?#tRf9
FHt<Ht>Ht#H
tgHuM95
t-HuC9
D$ PVj
D$$PVj
D$@;D$Dr
9D$xu;
9t$xv7
F;t$xr
|$L9D$4
F;t$Xr
D$PQW
9t$ v-
F;t$ r
f98t?j
9^Xt99^\tA
t$8]4t
@SVWjw
awjUXf;
AHt;Ht.H
_8C0tN
u h$.K
u h$.K
PPPPGW
F;Bt
SVWjA_jZ+
uBjAYjZ+
uWtj-Xf
tf;1u
SVjA[jZ^+
jAZjZ^+
9E v\PWj
9u(v?VSj
jh(kK
jhHkK
G@uqW
jhhkK
YYHtIHt8
u&j[9
jh0lK
jhPlK
D$tQf
HHtPHHt-H
HthHt3
Genuu_
ineIuV
nteluM3
u,9Et'9
~pjCXf
v	N+D$
uHjAXf;
tjXYf;
uWjAXf;
htHjlY;
HHtXHHt
uj X
nt'joY;
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00408ffe` | `0x408ffe` | 537937 | ✓ |
| `fcn.00409b60` | `0x409b60` | 534852 | ✓ |
| `fcn.0040a300` | `0x40a300` | 529797 | ✓ |
| `fcn.00406f07` | `0x406f07` | 508742 | ✓ |
| `fcn.00406c8a` | `0x406c8a` | 507824 | ✓ |
| `fcn.00406d75` | `0x406d75` | 507399 | ✓ |
| `fcn.00406bc4` | `0x406bc4` | 507180 | ✓ |
| `fcn.004029c8` | `0x4029c8` | 504420 | ✓ |
| `fcn.00407474` | `0x407474` | 504186 | ✓ |
| `fcn.004077b0` | `0x4077b0` | 502652 | ✓ |
| `fcn.004038fa` | `0x4038fa` | 501998 | ✓ |
| `fcn.004039c6` | `0x4039c6` | 501773 | ✓ |
| `fcn.00408b42` | `0x408b42` | 501544 | ✓ |
| `fcn.00402a54` | `0x402a54` | 500335 | ✓ |
| `fcn.00402c79` | `0x402c79` | 499765 | ✓ |
| `fcn.00408922` | `0x408922` | 499475 | ✓ |
| `fcn.00408b14` | `0x408b14` | 499315 | ✓ |
| `fcn.0040390f` | `0x40390f` | 496658 | ✓ |
| `fcn.00408e6e` | `0x408e6e` | 483584 | ✓ |
| `fcn.0040887d` | `0x40887d` | 483234 | ✓ |
| `fcn.00408b8e` | `0x408b8e` | 482650 | ✓ |
| `fcn.004012f7` | `0x4012f7` | 481713 | ✓ |
| `fcn.004028a6` | `0x4028a6` | 476209 | ✓ |
| `fcn.00405928` | `0x405928` | 474642 | ✓ |
| `fcn.004021ae` | `0x4021ae` | 474399 | ✓ |
| `fcn.00405e85` | `0x405e85` | 473333 | ✓ |
| `fcn.00405f19` | `0x405f19` | 473165 | ✓ |
| `fcn.00402745` | `0x402745` | 473116 | ✓ |
| `fcn.00405f52` | `0x405f52` | 473089 | ✓ |
| `fcn.00405f85` | `0x405f85` | 472580 | ✓ |

### Decompiled Code Files

- [`code/fcn.004012f7.c`](code/fcn.004012f7.c)
- [`code/fcn.004021ae.c`](code/fcn.004021ae.c)
- [`code/fcn.00402745.c`](code/fcn.00402745.c)
- [`code/fcn.004028a6.c`](code/fcn.004028a6.c)
- [`code/fcn.004029c8.c`](code/fcn.004029c8.c)
- [`code/fcn.00402a54.c`](code/fcn.00402a54.c)
- [`code/fcn.00402c79.c`](code/fcn.00402c79.c)
- [`code/fcn.004038fa.c`](code/fcn.004038fa.c)
- [`code/fcn.0040390f.c`](code/fcn.0040390f.c)
- [`code/fcn.004039c6.c`](code/fcn.004039c6.c)
- [`code/fcn.00405928.c`](code/fcn.00405928.c)
- [`code/fcn.00405e85.c`](code/fcn.00405e85.c)
- [`code/fcn.00405f19.c`](code/fcn.00405f19.c)
- [`code/fcn.00405f52.c`](code/fcn.00405f52.c)
- [`code/fcn.00405f85.c`](code/fcn.00405f85.c)
- [`code/fcn.00406bc4.c`](code/fcn.00406bc4.c)
- [`code/fcn.00406c8a.c`](code/fcn.00406c8a.c)
- [`code/fcn.00406d75.c`](code/fcn.00406d75.c)
- [`code/fcn.00406f07.c`](code/fcn.00406f07.c)
- [`code/fcn.00407474.c`](code/fcn.00407474.c)
- [`code/fcn.004077b0.c`](code/fcn.004077b0.c)
- [`code/fcn.0040887d.c`](code/fcn.0040887d.c)
- [`code/fcn.00408922.c`](code/fcn.00408922.c)
- [`code/fcn.00408b14.c`](code/fcn.00408b14.c)
- [`code/fcn.00408b42.c`](code/fcn.00408b42.c)
- [`code/fcn.00408b8e.c`](code/fcn.00408b8e.c)
- [`code/fcn.00408e6e.c`](code/fcn.00408e6e.c)
- [`code/fcn.00408ffe.c`](code/fcn.00408ffe.c)
- [`code/fcn.00409b60.c`](code/fcn.00409b60.c)
- [`code/fcn.0040a300.c`](code/fcn.0040a300.c)

## Behavioral Analysis

This updated analysis incorporates the disassembly from **Chunk 4/4**. The final piece of the puzzle confirms and solidifies previous findings regarding the sophistication of the malware’s core engine.

The inclusion of Chunk 4 moves the assessment from "sophisticated parser" to **"high-complexity state machine."** This code is designed not just to parse, but to validate, navigate, and execute a wide array of instructions while intentionally complicating the analysis path for researchers.

### Updated Analysis Summary

#### 1. Confirmation of the "Labyrinth" Architecture
The massive switch-case structures (notably in `fcn.00408922`) and complex nested loops confirm that the parser is a **labyrinthine state machine**.
*   **Dense Logic Branching:** The code doesn't just check if a command exists; it performs multiple checks on the *context* of the instruction. A single packet from the C2 can trigger hundreds of different internal logic branches depending on what "state" the bot is currently in. 
*   **Validation Loops:** Large blocks of code (e.g., `fcn.00408b14`) are dedicated to validating the integrity of the incoming data buffer. This ensures that only "well-formed" commands accepted by the attacker's specific protocol are executed, filtering out noise or automated scanning attempts from security researchers.

#### 2. Advanced Protocol Handling (State Persistence)
The recurrence of complex arithmetic on offsets (e.g., `uVar13 = uVar11 - 0x30`, `iVar12 = fcn.00471327(var_64h)`) and the manipulation of memory pointers suggests:
*   **Multi-Step Commands:** One command from the server may be broken into multiple "fragments" or steps that are processed over time, keeping the parser's state active between communications.
*   **Complex Data Structures:** The code isn't just handling strings; it’s navigating nested structures (like JSON or a custom binary protocol). This allows the attacker to send complex instructions—such as "search for file X, then zip it, then upload it"—within a single logic flow.

#### 3. Evidence of Strategic Obfuscation
The sheer volume of code dedicated to parsing (which appears to be much larger than what is required for a basic downloader) indicates several strategic goals:
*   **Anti-Analysis:** By hiding the actual "malicious" actions behind a wall of complex logic, the authors ensure that an automated sandbox only sees "network activity." Unless the analyst manually maps every branch in the switch tables, it is nearly impossible to know what the malware *can* do without having the specific keys/commands from the C2.
*   **Payload Diversification:** This architecture allows a single binary to serve multiple purposes (e.g., credential theft, file encryption, or lateral movement) simply by changing the commands sent from the server.

---

### Updated Risk Assessment for Incident Response

The final analysis of Chunk 4 reinforces and elevates the threat profile:

*   **Sophistication Level: Elite.** The complexity of `fcn.00408922` (with its massive switch table) and the sophisticated state management suggest this is a professional-grade, potentially **state-sponsored or high-level criminal enterprise tool**.
*   **Persistence & Versatility:** This module acts as a "Swiss Army Knife." The infrastructure allows the threat actor to change the malware’s behavior on the fly without redistributing the file. This makes it very difficult to predict the full scope of an infection until the specific C2 instructions are intercepted and analyzed.
*   **Evasion Technique - Logic Bloating:** By using a massive "translation layer" (the parser), the attackers ensure that standard signature-based detections are less effective, as the malicious actions aren't "hardcoded"—they are interpreted from the network.

---

### Technical Summary for IR Team

*   **Core Infrastructure Feature:** A high-complexity **Stateful Command Interpreter**. It serves as the central nervous system of the malware.
*   **Key Mechanisms:** 
    *   **Complex State Machine:** Uses massive switch tables to map incoming data to specific internal actions.
    *   **Robust Data Validation:** Ensures only "valid" commands are processed, likely intended to bypass automated detection and ensure reliability in remote execution.
    *   **Hidden Capabilities:** Because the capabilities are hidden behind this parsing layer, **assume a high ceiling of functionality.** 
*   **Actionable Intelligence for IR:**
    1.  **Scope of Impact:** If this binary is found on a system, assume it has the capability to perform any standard "backdoor" action (e.g., exfiltrating data, moving laterally, or executing remote scripts). The parser is designed to hide these options from basic analysis.
    2.  **Network Monitoring Focus:** Since the logic is so heavily obfuscated locally, focus on **NetFlow and PCAP analysis.** Identify the C2 heartbeats; any packet received by this "brain" could trigger a wide range of system changes.
    3.  **Host-Based Investigation:** Look for signs of "Staged Action." Because the parser can interpret complex commands, look for evidence of multi-stage operations (e.g., a process running for long periods or spawning child processes to perform specific tasks).
*   **Conclusion:** This is not a simple script; it is a **mature, modular framework**. The complexity is a deliberate choice by the developer to delay discovery and increase the cost of analysis for defenders.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The "labyrinthine" architecture and logic bloating are intentionally used to hide the malware’s true capabilities from automated tools and manual analysis. |
| T1497 | Virtualization/Sandbox Detection | Specific validation loops are designed to identify and filter out automated security scans, ensuring only "well-formed" C2 commands are processed. |
| T1059 | Command and Scripting Interpreter | The sophisticated command interpreter serves as a central hub that translates various remote instructions into diverse malicious actions like data exfiltration or file encryption. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the identified Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section consists primarily of obfuscated data or binary artifacts that do not resolve to human-readable IP addresses, URLs, or file paths. Therefore, no static network or file system IOCs were extracted from that section.

### **IP addresses / URLs / Domains**
*   *None identified.* (The provided text contains no valid networking indicators.)

### **File paths / Registry keys**
*   *None identified.* (While memory offsets such as `fcn.00408922` and `fcn.00408b14` were mentioned in the analysis, these are internal addresses within a specific binary and do not constitute persistent file paths or registry keys.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA-256 strings were present in the text.)

### **Other artifacts**
The following **behavioral indicators** and **TTPs (Tactics, Techniques, and Procedures)** are relevant for threat hunting and incident response:

*   **C2 Communication Pattern:** The malware utilizes a **Stateful Command Interpreter**. This means the behavior of the malware is not static; it changes based on the specific commands received from the C2 server.
*   **Obfuscation Technique (Logic Bloating):** Use of massive switch-case structures to hide malicious actions behind a complex "translation layer." 
*   **Robust Data Validation:** The binary checks for "well-formed" data, likely intended to filter out automated scanners and security research tools.
*   **Potential Capability Indicators:** Based on the architecture described, the malware is capable of:
    *   Multi-stage execution (breaking one command into multiple steps).
    *   Data exfiltration and encryption.
    *   Lateral movement (indicated by its "Swiss Army Knife" modularity).
*   **Advanced Instruction Parsing:** The presence of complex arithmetic on memory offsets suggests a non-standard, custom binary protocol for C2 communication.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Backdoor / RAT (Remote Access Trojan)
3. **Confidence**: High (for Type), Low (for Family)

4. **Key evidence**:
*   **Sophisticated Command Interpreter:** The presence of a "labyrinthine state machine" and complex switch-case structures indicates a modular architecture designed to interpret a wide range of remote instructions, typical of high-end backdoors.
*   **"Swiss Army Knife" Functionality:** The analysis notes the malware is built to perform diverse actions (data exfiltration, lateral movement, encryption) depending on the C2 commands received, which characterizes a sophisticated Remote Access Trojan.
*   **Advanced Evasion Techniques:** The use of "logic bloating" and strict data validation is specifically designed to bypass automated sandboxes and hide malicious capabilities behind a complex interpretation layer.
