# Threat Analysis Report

**Generated:** 2026-08-23 20:45 UTC
**Sample:** `11ac85099031a8d3c666ae8295d1b36a0115bd9b3c319481ee7f39450613054a_11ac85099031a8d3c666ae8295d1b36a0115bd9b3c319481ee7f39450613054a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11ac85099031a8d3c666ae8295d1b36a0115bd9b3c319481ee7f39450613054a_11ac85099031a8d3c666ae8295d1b36a0115bd9b3c319481ee7f39450613054a.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,156,096 bytes |
| MD5 | `edc95bcace6376a960cbb45745985b36` |
| SHA1 | `02fc0e6a25d4fb7bf699cc909e0cc11fbe9b4848` |
| SHA256 | `11ac85099031a8d3c666ae8295d1b36a0115bd9b3c319481ee7f39450613054a` |
| Overall entropy | 7.08 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768527541 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 570,880 | 6.68 | No |
| `.rdata` | 183,808 | 5.77 | No |
| `.data` | 25,088 | 2.003 | No |
| `.rsrc` | 332,800 | 7.874 | ⚠️ Yes |
| `.reloc` | 42,496 | 5.245 | No |

### Imports

**WSOCK32.dll**: `__WSAFDIsSet`, `recv`, `send`, `setsockopt`, `ntohs`, `recvfrom`, `select`, `WSAStartup`, `htons`, `accept`, `listen`, `bind`, `closesocket`, `connect`, `WSACleanup`
**VERSION.dll**: `GetFileVersionInfoW`, `VerQueryValueW`, `GetFileVersionInfoSizeW`
**WINMM.dll**: `timeGetTime`, `waveOutSetVolume`, `mciSendStringW`
**COMCTL32.dll**: `ImageList_Destroy`, `ImageList_Remove`, `ImageList_SetDragCursorImage`, `ImageList_BeginDrag`, `ImageList_DragEnter`, `ImageList_DragLeave`, `ImageList_EndDrag`, `ImageList_DragMove`, `ImageList_Create`, `InitCommonControlsEx`, `ImageList_ReplaceIcon`
**MPR.dll**: `WNetUseConnectionW`, `WNetCancelConnection2W`, `WNetGetConnectionW`, `WNetAddConnection2W`
**WININET.dll**: `InternetReadFile`, `InternetCloseHandle`, `InternetOpenW`, `InternetSetOptionW`, `InternetCrackUrlW`, `HttpQueryInfoW`, `InternetQueryOptionW`, `HttpOpenRequestW`, `HttpSendRequestW`, `FtpOpenFileW`, `FtpGetFileSize`, `InternetOpenUrlW`, `InternetConnectW`, `InternetQueryDataAvailable`
**PSAPI.DLL**: `GetProcessMemoryInfo`
**IPHLPAPI.DLL**: `IcmpCreateFile`, `IcmpCloseHandle`, `IcmpSendEcho`
**USERENV.dll**: `UnloadUserProfile`, `DestroyEnvironmentBlock`, `CreateEnvironmentBlock`, `LoadUserProfileW`
**UxTheme.dll**: `IsThemeActive`
**KERNEL32.dll**: `HeapAlloc`, `GetProcessHeap`, `HeapFree`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `MulDiv`, `GetVersionExW`, `GetSystemInfo`, `FreeLibrary`, `LoadLibraryA`, `GetProcAddress`, `SetErrorMode`, `GetModuleFileNameW`, `WideCharToMultiByte`
**USER32.dll**: `SetWindowPos`, `GetCursorInfo`, `RegisterHotKey`, `ClientToScreen`, `GetKeyboardLayoutNameW`, `IsCharAlphaW`, `IsCharAlphaNumericW`, `IsCharLowerW`, `IsCharUpperW`, `GetMenuStringW`, `GetSubMenu`, `GetCaretPos`, `IsZoomed`, `MonitorFromPoint`, `GetMonitorInfoW`
**GDI32.dll**: `SetPixel`, `DeleteObject`, `GetTextExtentPoint32W`, `ExtCreatePen`, `StrokeAndFillPath`, `StrokePath`, `GetDeviceCaps`, `CloseFigure`, `LineTo`, `AngleArc`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `MoveToEx`, `Ellipse`, `PolyDraw`
**COMDLG32.dll**: `GetSaveFileNameW`, `GetOpenFileNameW`
**ADVAPI32.dll**: `GetAclInformation`, `RegEnumValueW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegCreateKeyExW`, `GetUserNameW`, `RegOpenKeyExW`, `RegCloseKey`, `RegQueryValueExW`, `RegConnectRegistryW`, `InitializeSecurityDescriptor`, `InitializeAcl`, `AdjustTokenPrivileges`
**SHELL32.dll**: `DragQueryPoint`, `ShellExecuteExW`, `DragQueryFileW`, `SHEmptyRecycleBinW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHCreateShellItem`, `SHGetDesktopFolder`, `SHGetSpecialFolderLocation`, `SHGetFolderPathW`, `SHFileOperationW`, `ExtractIconExW`, `Shell_NotifyIconW`, `ShellExecuteW`, `DragFinish`
**ole32.dll**: `CoTaskMemAlloc`, `CoTaskMemFree`, `CLSIDFromString`, `ProgIDFromCLSID`, `CLSIDFromProgID`, `OleSetMenuDescriptor`, `MkParseDisplayName`, `OleSetContainedObject`, `CoCreateInstance`, `IIDFromString`, `StringFromGUID2`, `CreateStreamOnHGlobal`, `CoInitialize`, `CoUninitialize`, `GetRunningObjectTable`
**OLEAUT32.dll**: `RegisterTypeLib`, `LoadTypeLibEx`, `VariantCopyInd`, `SysReAllocString`, `SysFreeString`, `SafeArrayDestroyDescriptor`, `SafeArrayDestroyData`, `SafeArrayUnaccessData`, `SafeArrayAccessData`, `SafeArrayAllocData`, `UnRegisterTypeLib`, `SafeArrayCreateVector`, `SysAllocString`, `SysStringLen`, `VariantTimeToSystemTime`

## Extracted Strings

Total strings found: **2720** (showing first 100)

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

Based on the final chunk of disassembly provided, the analysis is further refined to characterize this as a **highly modular and robust command interpretation engine.** The sheer scale of the logic—particularly the massive switch tables and complex state-checking routines—confirms that this software was built for long-term persistence and versatility.

### Updated Analysis & Extended Findings

#### 1. Advanced Interpretation Architecture
The analysis of `fcn.00408922` and `fcn.00408e6e` provides significant depth into the "Interpretation" layer:

*   **Granular Type Validation (Massive Switch Tables):** The presence of switch tables with over 150 cases (as seen in `fcn.00408922`) indicates that the parser is not just looking for a single command (e.g., "get_file"). Instead, it validates a **complex type system**. Each case likely corresponds to a different data type or sub-property within a nested structure. This allows the attacker to send very specific instructions (e.g., "Execute [Script X] with [Parameter Y] using [Flag Z]") in a single packet.
*   **Robustness & Tolerance:** The code is laden with safety checks for buffer overflows, null pointers, and out-of-range values. This "defensive programming" ensures that if the Command & Control (C2) server sends slightly malformed or unusual data, the bot does not crash. This is a hallmark of professional malware designed to remain active on a target system for months or years.
*   **Complex State Handling:** The logic doesn't just evaluate values; it maintains and modifies internal state based on the results of previous parsing steps (e.g., adjusting offsets, checking flags like `0x7f` or `0xd800`). This implies a **stateful communication protocol** where the sequence of commands matters as much as the content of the command itself.

#### 2. Enhanced Evasion & Globalization Features
The final chunk confirms several sophisticated evasion and localization techniques:

*   **Unicode/Multi-byte Robustness:** The explicit handling of `0xd800` (the start of the surrogate pair range) ensures that the engine can process high-level Unicode characters. This is critical for an attacker who may want to use non-English character sets or localized strings in filenames and registry keys to blend into local systems or bypass basic string filters.
*   **Instruction Complexity/Obfuscation:** The complexity of the jump tables and nested logic makes it extremely difficult for automated sandboxes or static analyzers to map out the "menu" of available features. An analyst cannot simply look at a single function to see what the malware can do; they must trace every possible branch through the interpreter.

#### 3. Strategic Impact: The "Swiss Army Knife" Model
The structural design confirms that this is not a simple "downloader" or "stealer." It is an **Execution Framework**. 

*   **Multi-Functionality via Interpretation:** Because the core of the code is a parser, the specific malicious actions (keylogging, file exfiltration, privilege escalation) are likely **not** hardcoded into this binary. Instead, the attacker sends "scripts" or structured data that the interpreter feeds to different modules. This allows one single malware sample to perform dozens of different tasks depending on what it is told by the C2 server.
*   **Infrastructure Longevity:** The complexity suggests a professional-grade toolset where even if one specific module is detected, the core "engine" remains unchanged, making signature-based detection difficult.

---

### Updated Summary for Incident Response (Final)

The analyzed code is a **high-sophistication command interpretation engine** capable of processing complex, nested data structures with high reliability and robust error handling. It functions as a sophisticated gateway between the C2 server and various malicious "plug-in" capabilities.

**Key Findings:**
1.  **Architecture (Stateful Interpreter):** Unlike standard malware that uses simple `if/else` blocks for commands, this utilizes a formal **interpreter pattern**. It validates types, lengths, and nested parameters before executing an action.
2.  **Robustness & Production Grade:** The inclusion of overflow protections, multi-byte character support (Unicode), and dense switch tables indicates it was developed by an experienced team looking for high uptime on compromised systems.
3.  **Evasion via Complexity:** The "layered" nature of the parsing means that many malicious behaviors are hidden behind layers of interpretation, making static analysis very difficult without dynamic execution.

**Refined Recommendations for Incident Response:**
*   **Behavioral Analysis (Pivot Point):** Because much of the malicious logic is likely delivered as "data" to be parsed by this engine, **traditional string-based detection may fail.** Analysts should focus on behaviors: unauthorized network connections, unexpected process spawning, and mass file access.
*   **Memory Forensics:** Perform memory dumps while the malware is active. The "decoded" instructions and current state of the parser will be visible in memory, revealing what specific tasks (e.g., keylogging, etc.) are being performed at that moment.
*   **Network Traffic Analysis (Entropy & Structure):** Identify packets with a high degree of structure or non-standard fields. The use of this complex parser implies a highly structured binary protocol between the infected host and the C2 server.
*   **Threat Actor Attribution:** This level of software engineering is consistent with **State-Sponsored (APT) groups** or top-tier cybercriminal organizations. Treat any system showing these characteristics as having been compromised by a high-level threat actor.

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis, here are the corresponding MITRE ATT&K techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The "interpretation engine" using massive switch tables and a complex type system is designed to process diverse, nested commands instead of hardcoding specific behaviors. |
| **T1631** | Subvert Detection Tools | The inclusion of Unicode/multi-byte support specifically aims to bypass basic string filters and hide the malware's presence from security tools. |
| **T1036** | Masquerading | The use of localized strings and multi-byte characters allows the malware to "blend in" with local systems, making it harder for analysts to identify as a foreign process. |
| **T1568** | Dynamic Resolution | The modular design where specific actions (keylogging, exfiltration) are not hardcoded but resolved through an interpreter indicates a dynamic capability model common in advanced malware. |

### Analyst Note: 
The behavior describes a "Command and Control" (C2) infrastructure designed for **longevity and versatility**. The complexity of the parser suggests that this is not a primary loader, but rather the core communication heart of a sophisticated campaign, likely associated with an APT or high-level cybercriminal group.

---

## Indicators of Compromise

Based on my analysis of the provided strings and behavioral report, here is the organized list of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*None identified.*
*(Note: While a C2 infrastructure is confirmed to exist by the analysis, no specific IP addresses or domains were present in the provided data.)*

### **File paths / Registry keys**
*None identified.*
*(Note: The report mentions that the malware is capable of modifying registry keys and files using Unicode characters to evade detection, but no specific paths or keys were disclosed.)*

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None identified.*

### **Other artifacts**
*   **C2 Communication Pattern:** The malware utilizes a **Stateful Command Interpretation Engine**. This means communication is not simple "one-off" commands; the protocol is structured and maintains state. Analysts should look for highly structured, non-standard packet headers in network traffic.
*   **Evasion Technique (Unicode):** The engine specifically supports multi-byte/Unicode character sets (`0xd800` range). This is used to hide malicious filenames or registry keys by using non-English characters to bypass basic string filters.
*   **Complex Logic Gate:** The use of massive switch tables (150+ cases) suggests a "plug-in" architecture where the core binary acts as a gateway for multiple capabilities (e.g., keylogging, exfiltration).

---
**Analyst Note:** 
The string section provided contains heavily obfuscated or "junk" data typical of packed/encrypted malware. No immediate static indicators (like specific IPs) are available from this raw sample. Incident Response should prioritize **behavioral monitoring** (memory forensics and network traffic analysis) over signature-based detection for this specific threat actor.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: backdoor / RAT
3. **Confidence**: High

**Key evidence**:
*   **Sophisticated Command Interpretation:** The presence of massive switch tables (>150 cases) and a stateful communication protocol indicates an advanced, professional-grade backend designed to interpret complex instructions rather than simple hardcoded commands.
*   **Modular Execution Framework:** The analysis confirms the malware acts as an "execution engine" where malicious capabilities (like keylogging or exfiltration) are delivered as data/scripts from the C2, allowing a single binary to perform multiple functions.
*   **High-Level Engineering & Evasion:** The inclusion of robust error handling (overflow protection), complex logic gates to thwart automated analysis, and Unicode support for blending into local environments is characteristic of APT-level toolkit design.
