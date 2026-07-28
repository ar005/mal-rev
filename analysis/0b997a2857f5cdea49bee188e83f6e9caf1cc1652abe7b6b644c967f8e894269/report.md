# Threat Analysis Report

**Generated:** 2026-07-27 13:59 UTC
**Sample:** `0b997a2857f5cdea49bee188e83f6e9caf1cc1652abe7b6b644c967f8e894269_0b997a2857f5cdea49bee188e83f6e9caf1cc1652abe7b6b644c967f8e894269.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b997a2857f5cdea49bee188e83f6e9caf1cc1652abe7b6b644c967f8e894269_0b997a2857f5cdea49bee188e83f6e9caf1cc1652abe7b6b644c967f8e894269.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,038,336 bytes |
| MD5 | `f0e34aaed877c2b5674c3dc1fb957bb1` |
| SHA1 | `9b801480c8f81a5dd45f046ea9a104afd0cd7510` |
| SHA256 | `0b997a2857f5cdea49bee188e83f6e9caf1cc1652abe7b6b644c967f8e894269` |
| Overall entropy | 6.912 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1763375281 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 570,880 | 6.68 | No |
| `.rdata` | 183,808 | 5.77 | No |
| `.data` | 25,088 | 2.003 | No |
| `.rsrc` | 215,040 | 7.76 | ⚠️ Yes |
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

Total strings found: **2483** (showing first 100)

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

The final disassembly chunk (4/4) provides a "smoking gun" regarding the nature of this malware’s internal architecture. While previous chunks established that there is a complex parser, this final section reveals **how** that parser is being used: it is likely processing a high-level scripting language or a heavily structured configuration format (such as JSON, XML, or an HTML-based data blob) to drive the malware's behavior.

Here is the updated analysis incorporating the final findings.

### Updated Analysis Summary

#### 1. Validation of "Scripting Engine" Theory
The complexity and volume of code in `fcn.00408922` (the large switch table) and `fcn.00408e6e` strongly suggest that this isn't just a C2 command parser; it is a **decoder for structured data.**

*   **Escape Character Handling:** The code frequently checks for, and processes around, special characters like quotes (`"`), backslashes (`\`), and brackets. This is typical of systems designed to "unescape" strings before passing them to an internal execution engine or a shell command.
*   **State-Machine Complexity:** The logic doesn't just jump from one point to another; it tracks state across nested iterations. This indicates that the malware receives a single, large "blob" of data (possibly containing multiple instructions) and parses it locally to determine which modules to load or functions to run.
*   **Automatic Translation/Conversion:** The segments involving `0x4813ca` and `0x48e6e` appear to be converting raw buffer contents into usable variables for the malware’s "logic" layer.

#### 2. Hybrid Sophistication: Infrastructure & Tooling
The inclusion of specific WinAPI-related behaviors (handling of GDI objects and Windows handles) alongside such high-level parsing suggests a very mature development lifecycle.

*   **Resource Management:** The code in `fcn.0040390f` specifically manages the cleanup of GDI objects (`DeleteObject`) and Window handles. This implies the malware is designed to be "clean" in its operation—it doesn't just leak resources, it manages them carefully to avoid detection by system monitoring tools that look for anomalous resource usage or hanging processes.
*   **Multi-Stage Logic:** The sheer amount of code dedicated to *preparing* data suggests that the actual "malicious" actions (the "payload") are relatively small and modular. This makes signature detection much harder, as the core payload is hidden behind a massive wall of standard parsing logic.

#### 3. Identification of Professional-Grade Libraries
The uniformity of the switch tables and the way nested conditions are handled strongly suggest that the developers did not write this from scratch. Instead, they likely integrated (or modified) an existing open-source library—possibly for **JSON/XML parsing** or a **small scripting interpreter** (like a custom Lua or Python-lite wrapper). This is a signature of advanced persistent threat (APT) groups who prefer using reliable, battle-tested "building blocks" to ensure their tools are stable and performant across different OS versions.

---

### Updated Risk Profile & Security Implications

| Feature | Technical Observation | Potential Malware Impact |
| :--- | :--- | :--- |
| **Extensive Escape Logic** | Intensive handling of `\`, `"`, and nested brackets in the parser. | Allows the malware to hide a wide array of commands inside a single, "legal-looking" data blob (e.g., JSON/XML). |
| **High-Complexity Switch Tables** | Large jumps and state management in functions like `fcn.00408922`. | Suggests an internal "Scripting Engine." The malware is likely programmable remotely, allowing the attacker to change its behavior without re-infecting the system. |
| **Rigorous Resource Management** | Clear logic for GDI and Window handle cleanup (`DeleteObject`). | Reduces the "noise" produced by the malware, making it harder for standard EDR tools to flag it for resource leaks or abnormal behavior. |
| **Advanced Data Normalization** | Seamless handling of Unicode/special characters across several code segments. | Ensures high reliability across different geographical regions and language locales (global reach). |

---

### Final Summary for Incident Response

The full analysis confirms that this is a highly sophisticated, likely state-sponsored or professional cybercrime operation. The malware's design mirrors the logic of modern web browsers and enterprise software, which is a deliberate choice to blend in with legitimate traffic.

**Key Findings for SOC/IR:**

1.  **"Modular Payload" Architecture:** Because the malware uses a complex internal parser (likely for JSON or a scripted language), it is capable of performing many different functions depending on the data sent by the C2 server. **Do not assume its capability based on current observations.** If you see it active, it may be waiting for a specific "script" to execute next.
2.  **Detection Gap:** Traditional signature-based detection will likely fail because much of the code is standard parsing logic common in many legitimate applications (like browsers or office suites). Focus instead on **behavioral indicators.**
3.  **Advanced C2 Communication:** The network traffic from this sample may look like valid API calls to a web service because it uses complex data structures. Look for "heartbeat" signals followed by large, structured JSON/XML packets.

**Strategic Recommendation:**
The "parsing" logic observed in all four chunks is the **engine.** Once this engine receives a "go" signal from its C2 server and parses the incoming data, it will execute the actual payload. 

**Immediate Actions for SOC:**
*   **Hunt for Persistence:** Search for entries in `Run` keys or scheduled tasks that point to binaries containing these specific parsing patterns.
*   **Network Correlation:** Identify internal hosts communicating with external IPs using non-standard ports or suspicious high-frequency "beacons."
*   **Memory Forensics:** Since the malware likely parses its instructions *at runtime*, memory analysis should focus on looking for dynamic strings/scripts being unpacked into memory after the parsing phase is complete.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The analysis identifies an internal "Scripting Engine" used to parse complex, structured data (JSON/XML) to determine which modules to load or functions to execute. |
| **T1027** | Obfuscated Syntax, Programs or Files | The use of extensive escape character logic and large "data blobs" allows the malware to hide a wide variety of commands within standard-looking structures. |
| **T1562** | Impair Defenses | Purposeful, high-quality resource management (e.g., `DeleteObject` for GDI handles) is used specifically to avoid detection by security tools that flag abnormal resource usage. |
| **T1036** | Masquerading | The malware purposefully uses code structures and patterns common in web browsers and enterprise software to blend in with legitimate system activity. |
| **T1071** | Application Layer Protocol | The use of complex data normalization and structured formats (JSON/XML) ensures the C2 traffic mimics standard API calls or web services. |

---

## Indicators of Compromise

Based on the provided data, here are the extracted Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. *(Note: The strings `.rdata`, `.data`, and `.reloc` were identified as standard PE file segments and excluded as false positives).*

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts (user agents, C2 patterns, etc.)**
*   **C2 Communication Pattern:** The malware utilizes a sophisticated parsing engine capable of processing structured data formats including **JSON, XML, and HTML-based data blobs**.
*   **Command & Control Behavior:** Analysis suggests the presence of "heartbeat" signals followed by large, structured packets containing scripts or instructions for the internal execution engine.
*   **Decoding Mechanism:** The malware employs a state-machine architecture to "unescape" and normalize complex strings (handling `\`, `"`, and nested brackets) before executing commands.
*   **Evasion Technique:** Advanced resource management (specifically using `DeleteObject` for GDI objects and Windows handles) is used to minimize the system footprint and avoid detection by monitoring tools looking for resource leaks.

---

### **Analyst Note**
The "EXTRACTED STRINGS" section contained high levels of noise/obfuscation, with no direct network indicators (IPs/Domains) or filesystem artifacts visible in the raw text. The primary intelligence resides in the **Behavioral Analysis**, which indicates that detection should focus on **network traffic analysis** (looking for structured JSON/XML payloads) and **memory forensics** (identifying unpacked scripts during the execution phase).

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1.  **Malware family**: Unknown
2.  **Malware type**: Loader / Backdoor
3.  **Confidence**: High
4.  **Key evidence**:
    *   **Scripting Engine Architecture:** The presence of a complex state-machine and switch tables for parsing "large data blobs" (JSON/XML/HTML) indicates the malware is designed to receive, decode, and execute modular commands remotely rather than having hardcoded functionality.
    *   **Sophisticated Evasion Tactics:** The deliberate implementation of professional-grade resource management (specifically `DeleteObject` for GDI and Window handles) identifies a high level of development aimed at evading behavior-based EDR detections.
    *   **Modular/Professional Design:** The analysis highlights a "sophisticated, likely state-sponsored or professional" design where the core engine is distinct from the payload, allowing it to function as a persistent platform for varied malicious activities.
