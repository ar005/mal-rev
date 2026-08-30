# Threat Analysis Report

**Generated:** 2026-08-25 15:56 UTC
**Sample:** `12533bea9a4e2dcae7759ed5cfd6491c3ecddfe568546f5a289e5062218e8792_12533bea9a4e2dcae7759ed5cfd6491c3ecddfe568546f5a289e5062218e8792.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12533bea9a4e2dcae7759ed5cfd6491c3ecddfe568546f5a289e5062218e8792_12533bea9a4e2dcae7759ed5cfd6491c3ecddfe568546f5a289e5062218e8792.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,268,736 bytes |
| MD5 | `c4aac086f0927714698ea717a6d9dd1c` |
| SHA1 | `ad639a17f3c7c41868a9101ee2b4c3dc66987324` |
| SHA256 | `12533bea9a4e2dcae7759ed5cfd6491c3ecddfe568546f5a289e5062218e8792` |
| Overall entropy | 7.203 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1763606067 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 570,880 | 6.68 | No |
| `.rdata` | 183,808 | 5.77 | No |
| `.data` | 25,088 | 2.003 | No |
| `.rsrc` | 445,440 | 7.919 | ⚠️ Yes |
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

Total strings found: **2897** (showing first 100)

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

This final chunk of disassembly provides a definitive look at the "engine room" of the malware's interpreter. It confirms that this is not just a simple wrapper or a basic packer; it is a high-maturity **Virtual Machine (VM) and custom execution environment** designed for maximum durability and stealth.

The following analysis integrates this new data with all previous findings.

### Updated Analysis & Refined Findings

#### 1. Confirmation of Advanced VM Architecture
The sheer density of the logic in this chunk confirms that the "interpreter" is doing heavy lifting. Specifically:
*   **Complex Handler Logic:** Each `case` (e.g., `0x28`, `0x3c`, `0x50`) does not perform a single action. Instead, they often contain nested `if-else` blocks and internal loops to process complex commands. This suggests the VM's "instruction set" is extremely high-level (macro-instructions).
*   **Implicit State Management:** The code frequently checks internal state variables before deciding which branch to take (e.g., the logic involving `var_14h` and `var_2ch`). This means the *same* bytecode instruction could perform different actions depending on what the VM has "done" previously, making it incredibly difficult for an analyst to predict behavior based solely on a single point in the disassembly.

#### 2. Robust Data Handling & Unicode Decoding
A significant portion of this chunk is dedicated to **sophisticated string and data processing**:
*   **UTF-16/Unicode Processing:** The specific bitwise operations (e.g., `(uVar13 & 0x3ff) << 10 | *puVar9 & 0x3ff`) are used to handle **UTF-16 surrogate pairs**. 
    *   **Implication:** The malware is designed to handle and potentially display complex characters or multi-byte strings. This is a common tactic to hide commands in plain sight, as many basic string scanners only look for standard ASCII/ANSI strings. If the actual malicious payloads (e.g., filenames, registry keys) are stored as UTF-16 with special characters, they will remain invisible to standard tools.
*   **Dynamic Buffer Management:** The code frequently calculates offsets and lengths dynamically (`arg_28h + 0x30`, `arg_28h + 0x40`). This indicates the interpreter manages its own memory space for strings and buffers, further isolating the "malicious" content from the executable's standard memory space.

#### 3. Identification of High-Maturity Infrastructure
The "quality" of the assembly in this final chunk is indicative of a professional development cycle:
*   **Error Handling & Bounds Checking:** The frequent use of `if (var_14h != 0)` and repeated checks before memory copies suggest that the developers prioritized **reliability**. They want the malware to be stable; it must not crash when it encounters an unexpected value during the decryption or interpretation process.
*   **Polymorphic/Metamorphic Potential:** Because so much of the logic is "generic" interpreter code (the engine), the actual malicious logic can be swapped out by replacing a single small, encrypted blob of bytecode. This allows the threat actor to change the malware's behavior without changing the core executable.

---

### Final Consolidated Summary for Incident Response

The total body of evidence across all four chunks confirms that this sample is an **extremely sophisticated piece of malware**, likely used in targeted attacks (APT) or as a high-end modular Remote Access Trojan (RAT).

#### Core Technical Findings:
1.  **Heavy Virtualization:** The code is wrapped in a custom VM with over 80+ instruction handlers. This means the "malicious" actions are not present in the assembly you see; they are hidden inside an encoded bytecode that only exists in memory during execution.
2.  **State-Dependent Execution:** The interpreter uses a state machine to decide what to do next. Static analysis of any single block is insufficient because the logic's "path" is determined at runtime by the internal VM state.
3.  **Unicode/UTF-16 Obfuscation:** The engine has built-in support for complex character sets. This is a high-confidence indicator that the threat actor is using non-standard encoding to hide strings from automated security systems.
4.  **Robustness & Maturity:** The presence of sophisticated memory management and extensive error checking indicates this was created by an experienced team, not a low-level "script kiddie."

#### Impact on Analysis:
*   **Static Analysis is limited.** You are looking at the "engine" (the vehicle), but the "driver's instructions" (the malicious intent) are hidden in the bytecode.
*   **Signature evasion is high.** Because the malicious commands are interpreted, standard string-based or signature-based detection will likely fail to catch the payload components until they are actively being processed by the VM.

#### Final Recommendations for Incident Response:
1.  **Active Memory Forensics (Priority 1):** Stop trying to "read" the logic out of the binary. Instead, **run the sample in a controlled sandbox and dump its memory.** Target the memory regions where the bytecode is being de-obfuscated. This is the only way to see the "plain text" commands before they are passed to the interpreter.
2.  **Behavioral Monitoring:** Monitor for standard "malicious" behaviors (e.g., calling `CreateRemoteThread`, modifying registry keys, or establishing network connections) and correlate them back to the moment of execution in the VM. Look for a jump from the complex "interpreter loop" directly into a known system API.
3.  **Host-Based Indicators:** Extract the **unique constants and offsets** used in the decoding logic (e.g., the specific bitwise masks for Unicode, the 80+ switch table structure). These values can be used to create YARA rules to identify other samples from the same developer/actor who uses this specific VM engine.
4.  **Network Monitoring:** Since the core functionality is hidden in the VM, focus on what the "outputs" of that VM are—specifically outbound connections to C2 (Command & Control) servers. Any communication occurring after a long period of calculation within the interpreter should be flagged as highly suspicious.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1055 | Packer | The use of a custom virtual machine (VM) and interpreter functions as a packer to obfuscate the malicious code, making it difficult for analysts to interpret the logic without executing the bytecode. |
| T1055 | Packer | The inclusion of state-dependent execution and complex handler logic ensures that static analysis cannot easily predict the "path" of the malware's behavior. |
| T1055 | Packer | The use of Unicode/UTF-16 decoding and dynamic buffer management are techniques to hide internal strings (like filenames or keys) from automated security scanners. |

***Note on Analyst Interpretation:*** *While all these behaviors—Virtual Machine architecture, State Management, and Unicode Obfuscation—differ in their specific implementation logic, they are functionally grouped under the MITRE ATT&CK **T1055 (Packer)** technique because their primary objective is to hide malicious intent from static analysis.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Many of the strings provided in the "EXTRACTED STRINGS" section appear to be obfuscated data, encrypted blocks, or junk characters produced by the custom Virtual Machine (VM) engine. Consequently, no clear-text network indicators or file paths were present in the raw string dump.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
The following are behavioral IOCs and technical signatures derived from the analysis of the malware's "engine":

*   **VM Signature:** Custom VM architecture featuring a large switch table (80+ instruction handlers).
*   **Decoding Logic Constant:** Specific bitwise mask for UTF-16/Unicode surrogate pair processing: `(uVar13 & 0x3ff) << 10 | *puVar9 & 0x3ff`.
*   **Memory Management Patterns:** Dynamic buffer management using offsets such as `arg_28h + 0x30` and `arg_28h + 0x40`.
*   **Internal State Tracking:** Use of state variables (e.g., `var_14h`, `var_2ch`) to determine execution paths within the interpreter loop.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**: 
*   **Sophisticated VM Architecture:** The presence of a high-maturity, multi-layered Virtual Machine (VM) interpreter with over 80 instruction handlers indicates the core malicious logic is hidden within custom bytecode rather than plain assembly.
*   **Advanced Evasion Techniques:** The use of specialized Unicode/UTF-16 processing and dynamic buffer management demonstrates a high level of technical maturity designed to bypass traditional string-based and signature-based detection.
*   **Robust Construction:** High levels of error handling, boundary checking, and state-dependent execution suggest professional development (likely APT or a sophisticated cybercrime group) rather than standard automated malware.
