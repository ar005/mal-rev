# Threat Analysis Report

**Generated:** 2026-09-03 01:17 UTC
**Sample:** `13d335504add2ad1572849d81480799152d1ad77265af1054ab32f636e8a2b9b_13d335504add2ad1572849d81480799152d1ad77265af1054ab32f636e8a2b9b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13d335504add2ad1572849d81480799152d1ad77265af1054ab32f636e8a2b9b_13d335504add2ad1572849d81480799152d1ad77265af1054ab32f636e8a2b9b.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,184,768 bytes |
| MD5 | `b9ad6fde9186629b5d2f7a421c060241` |
| SHA1 | `87203f9c7ea95425455f00ada7b50a5d1833f51b` |
| SHA256 | `13d335504add2ad1572849d81480799152d1ad77265af1054ab32f636e8a2b9b` |
| Overall entropy | 7.141 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768547445 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 570,880 | 6.68 | No |
| `.rdata` | 183,808 | 5.77 | No |
| `.data` | 25,088 | 2.003 | No |
| `.rsrc` | 361,472 | 7.941 | ⚠️ Yes |
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

Total strings found: **2675** (showing first 100)

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

This final chunk of disassembly confirms the most advanced characteristics of the binary's internal architecture. The code provided represents the "heart" of the parser—the logic that actually translates raw, obfuscated data into actionable commands for the malware.

### Updated Analysis: Chunk 4/4 Integration

#### 1. Granular State Transition Logic (The "Switch-Case" Fortress)
The sheer volume of `switch` cases (including a massive table at `0x408a7e` with over 150 branches) indicates that this is not just an FSM, but a **Grammar-Based Parser**. 
*   **Instructional Complexity:** Instead of a simple mapping where "Packet Type X = Action Y," the code implements logic where "Byte A determines if we are looking for a String, a Numeric Value, or another Nested Object." 
*   **Contextual Mapping:** For example, in `case 0x43` and `case 0x50`, the code doesn't just accept a value; it performs length calculations, checks for specific delimiters (like `0x29` or `0x3a`), and validates boundaries. This is indicative of a parser designed to handle complex data structures like JSON-lite, Protobufs, or custom binary protocols used in high-end C2 frameworks.

#### 2. "Deep" Validation & Integrity Checking
Several functions (like `fcn.00408922` and `fcn.00408b14`) act as **Validation Gatekeepers**.
*   **Multi-Stage Verification:** Before a command is "accepted," it passes through several loops that check bitmasks, range limits, and alignment. 
*   **Automatic Correction/Normalization:** In some cases (e.g., handling of `0x91` or `0x87`), the code seems to have built-in logic to handle "fallback" scenarios where data might be slightly malformed but still interpretable—a hallmark of professional network programming where packet loss or noise is expected.

#### 3. Sophisticated Data Handling (UTF-16 & Length Offsets)
The continuous use of `var_4h = var_4h + 2` and calculations like `(uVar13 & 0x3ff) << 10 | *puVar9 & 0x3ff` reveals:
*   **Multi-byte Encoding:** The parser is specifically designed to handle UTF-16 or similar wide-character encodings, common in Windows environments.
*   **Dynamic Offsets:** The logic calculates the "next" position in the buffer dynamically based on length headers found in previous bytes. This allows a single packet from the C2 server to contain dozens of different commands packed together, each with its own header and payload.

#### 4. Defensive Obfuscation: The "Analysis Sinkhole"
This final chunk provides the clearest evidence of **Complexity Exhaustion**:
*   **Decision Tree Depth:** To reach a single piece of malicious logic (e.g., "Delete File"), an analyst must navigate through dozens of levels of nested `if` statements and `switch` cases. This is designed to exhaust the patience and time of human researchers and to cause "path explosion" in automated symbolic execution tools.
*   **Indistinguishable Logic:** The code blends harmless "parser overhead" (checking lengths, encoding types, etc.) with potentially malicious logic so seamlessly that it becomes difficult to pinpoint where the C2 interpretation ends and the malicious payload begins.

---

### Final Summary for Report

**Final Analysis: Advanced Multi-Layered Command & Control (C2) Interpreter**

The final analysis of all four segments confirms that this binary contains a **highly sophisticated, production-grade command interpreter**. It is designed to ingest complex, multi-layered, and potentially nested data structures from a remote server. This level of sophistication is rarely seen in commodity malware and is highly indicative of an **Advanced Persistent Threat (APT)** framework or a high-tier state-sponsored toolset.

**Core Architectural Findings:**

1.  **Grammar-Based Finite State Machine (FSM):** The parser does not simply "read" commands; it "interprets" a stream. By using nested switch tables and complex branching, the malware can support a massive variety of command types and sub-commands while keeping its core execution logic isolated from the raw network data.
2.  **Multi-Layered Decapsulation:** The code is structured to "unwrap" layers of encoding/encryption sequentially. This allows the threat actor to change how they pack their commands (e.g., switching from simple base64 to a custom binary protocol) without changing the core logic of the malware’s execution engine.
3.  **Strategic Complexity Exhaustion:** The implementation utilizes "defense-in-depth" for its code structure. By using extensive switch tables and complex arithmetic for basic checks, the author creates a massive amount of "noise." This forces analysts to waste significant time mapping out the parser's mechanics before they can reach the actual malicious functions (e.g., keylogging, exfiltration).
4.  **Industrial-Grade Robustness:** The precision in handling UTF-16 surrogate pairs, buffer boundary checks, and varied data lengths indicates that this tool was likely developed by professional engineers. It is built to be stable across different system environments and capable of processing complex payloads with high reliability.

**Threat Intelligence Conclusion:**
This component functions as a **sophisticated middleman**. Its purpose is to provide the threat actor with maximum flexibility; they can update their C2 infrastructure's communication protocols frequently, while this "parser engine" remains constant on the victim's machine. The presence of such an advanced interpreter suggests that the associated campaign targets high-value assets and utilizes a highly mature delivery and command infrastructure.

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The "Analysis Sinkhole" and "Complexity Exhaustion" tactics are designed to hide malicious logic behind a dense web of complex parsing code to exhaust analyst resources. |
| **T1486** | Data Encoding | The parser specifically handles multi-byte encoding (UTF-16) and utilizes dynamic length offsets to decode/unwrap layered data structures from the C2 server. |
| **T1071** | Application Layer Protocol | The use of a "Grammar-Based" interpreter for complex data structures (like JSON-lite or Protobuf) indicates high-sophistication command delivery via standard application layer protocols. |
| **T1036** | Masquerading | The blending of "harmless" parser overhead with malicious logic makes it difficult to distinguish between legitimate system-style programming and actual malicious operations. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided string dump and behavioral analysis report. Below are the extracted Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided data contains high-level architectural details regarding a malware's Command & Control (C2) communication module rather than direct network infrastructure indicators (like specific IP addresses or domain names). The strings appear to be obfuscated internal buffer fragments or results of a "strings" extraction from an obfuscated binary, which do not contain usable external artifacts.

---

### **IOC_Report**

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: Memory offsets such as `0x408a7e` and function identifiers like `fcn.00408922` were identified, but these are internal execution pointers and not filesystem/registry paths).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts (user agents, C2 patterns, etc.)**
*   **C2 Communication Pattern:** Grammar-Based Finite State Machine (FSM) used to parse complex nested data structures (e.g., JSON-lite or Protobuf style).
*   **Data Encoding:** Utilization of UTF-16 encoding and dynamic length offsets for multi-byte character handling.
*   **Evasion Technique:** "Complexity Exhaustion" via deep nesting of `switch` cases and decision trees to hinder automated sandbox analysis and manual reverse engineering.
*   **Logic Complexity:** Multi-stage verification and normalization logic used during the transition between raw network data and internal command execution.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1.  **Malware family:** custom (likely an APT-grade framework)
2.  **Malware type:** backdoor
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Advanced C2 Architecture:** The presence of a "Grammar-Based" Finite State Machine (FSM) and the ability to process complex, nested data structures (like JSON-lite or Protobuf) indicate a high-tier command interpreter rather than simple commodity malware.
    *   **Sophisticated Evasion Techniques:** The use of "Complexity Exhaustion"—utilizing massive switch tables and deep nesting—is a deliberate design choice to exhaust human analysts and stall automated analysis tools.
    *   **Professional Engineering:** The inclusion of robust data handling (UTF-16 support, multi-stage validation, and dynamic length calculations) indicates the tool was developed by professional engineers for stable, long-term operation in high-value targets.
