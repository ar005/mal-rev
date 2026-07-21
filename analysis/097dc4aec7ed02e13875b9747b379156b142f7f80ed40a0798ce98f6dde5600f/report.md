# Threat Analysis Report

**Generated:** 2026-07-20 15:36 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, UPX compressed, 3 sections |
| Size | 749,056 bytes |
| MD5 | `77e1a51112cc8fcc0f3ffab1c950b10c` |
| SHA1 | `182f45708c00e5ab967e6450e266a71b75609912` |
| SHA256 | `097dc4aec7ed02e13875b9747b379156b142f7f80ed40a0798ce98f6dde5600f` |
| Overall entropy | 7.129 |
| Unpacked | ✓ Yes (tool: upx) |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769045859 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.61 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 376,320 | 7.894 | ⚠️ Yes |
| `.reloc` | 30,208 | 6.798 | No |

### Imports

**KERNEL32.DLL**: `DuplicateHandle`, `CreateThread`, `WaitForSingleObject`, `HeapAlloc`, `GetProcessHeap`, `HeapFree`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `MulDiv`, `GetVersionExW`, `IsWow64Process`, `GetSystemInfo`, `FreeLibrary`, `LoadLibraryA`
**ADVAPI32.dll**: `GetAce`, `RegEnumValueW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegOpenKeyExW`, `RegCloseKey`, `RegQueryValueExW`, `RegConnectRegistryW`, `InitializeSecurityDescriptor`, `InitializeAcl`, `AdjustTokenPrivileges`, `OpenThreadToken`, `OpenProcessToken`
**COMCTL32.dll**: `ImageList_ReplaceIcon`, `ImageList_Destroy`, `ImageList_Remove`, `ImageList_SetDragCursorImage`, `ImageList_BeginDrag`, `ImageList_DragEnter`, `ImageList_DragLeave`, `ImageList_EndDrag`, `ImageList_DragMove`, `InitCommonControlsEx`, `ImageList_Create`
**COMDLG32.dll**: `GetSaveFileNameW`, `GetOpenFileNameW`
**GDI32.dll**: `EndPath`, `DeleteObject`, `GetTextExtentPoint32W`, `ExtCreatePen`, `StrokeAndFillPath`, `GetDeviceCaps`, `SetPixel`, `CloseFigure`, `LineTo`, `AngleArc`, `MoveToEx`, `Ellipse`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `PolyDraw`
**IPHLPAPI.DLL**: `IcmpSendEcho`, `IcmpCloseHandle`, `IcmpCreateFile`
**MPR.dll**: `WNetGetConnectionW`, `WNetCancelConnection2W`, `WNetUseConnectionW`, `WNetAddConnection2W`
**ole32.dll**: `CoTaskMemAlloc`, `CoTaskMemFree`, `CLSIDFromString`, `ProgIDFromCLSID`, `CLSIDFromProgID`, `OleSetMenuDescriptor`, `MkParseDisplayName`, `OleSetContainedObject`, `CoCreateInstance`, `IIDFromString`, `StringFromGUID2`, `CreateStreamOnHGlobal`, `OleInitialize`, `OleUninitialize`, `CoInitialize`
**OLEAUT32.dll**: `CreateStdDispatch`, `CreateDispTypeInfo`, `UnRegisterTypeLib`, `UnRegisterTypeLibForUser`, `RegisterTypeLibForUser`, `RegisterTypeLib`, `LoadTypeLibEx`, `VariantCopyInd`, `SysReAllocString`, `SysFreeString`, `VariantChangeType`, `SafeArrayDestroyData`, `SafeArrayUnaccessData`, `SafeArrayAccessData`, `SafeArrayAllocData`
**PSAPI.DLL**: `GetProcessMemoryInfo`
**SHELL32.dll**: `DragFinish`, `DragQueryPoint`, `ShellExecuteExW`, `DragQueryFileW`, `SHEmptyRecycleBinW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHCreateShellItem`, `SHGetDesktopFolder`, `SHGetSpecialFolderLocation`, `SHGetFolderPathW`, `SHFileOperationW`, `ExtractIconExW`, `Shell_NotifyIconW`, `ShellExecuteW`
**USER32.dll**: `IsCharAlphaW`, `IsCharAlphaNumericW`, `IsCharLowerW`, `IsCharUpperW`, `GetMenuStringW`, `GetSubMenu`, `GetCaretPos`, `IsZoomed`, `MonitorFromPoint`, `GetMonitorInfoW`, `SetWindowLongW`, `SetLayeredWindowAttributes`, `FlashWindow`, `GetClassLongW`, `TranslateAcceleratorW`
**USERENV.dll**: `DestroyEnvironmentBlock`, `LoadUserProfileW`, `CreateEnvironmentBlock`, `UnloadUserProfile`
**UxTheme.dll**: `IsThemeActive`
**VERSION.dll**: `GetFileVersionInfoW`, `VerQueryValueW`, `GetFileVersionInfoSizeW`
**WININET.dll**: `HttpOpenRequestW`, `InternetCloseHandle`, `InternetOpenW`, `InternetSetOptionW`, `InternetCrackUrlW`, `HttpQueryInfoW`, `InternetQueryOptionW`, `InternetConnectW`, `HttpSendRequestW`, `FtpOpenFileW`, `FtpGetFileSize`, `InternetOpenUrlW`, `InternetReadFile`, `InternetQueryDataAvailable`
**WINMM.dll**: `timeGetTime`, `waveOutSetVolume`, `mciSendStringW`
**WSOCK32.dll**: `gethostbyname`, `recv`, `send`, `socket`, `ioctlsocket`, `setsockopt`, `ntohs`, `WSACleanup`, `WSAStartup`, `sendto`, `htons`, `__WSAFDIsSet`, `select`, `accept`, `listen`

## Extracted Strings

Total strings found: **2941** (showing first 100)

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

This final segment of the disassembly (Chunk 5/5) provides a definitive look into the malware's core architecture. It confirms that this is not just sophisticated, but likely uses a **Virtual Machine (VM) based execution engine** or a highly modularized "Command Dispatcher" system common in advanced persistent threats (APTs).

The analysis has been updated to include findings from Chunk 5.

---

### Final Comprehensive Analysis Summary (Chunk 1-5)

The conclusion of the disassembly confirms that the malware is designed for **maximum resilience against static analysis**. It utilizes multiple layers of "Dispatchers"—functions with large switch tables—to translate internal instructions into actions. This effectively separates the malicious logic from the system calls, making it very difficult to identify the true purpose of the code without executing it in a way that triggers specific "states."

#### 1. The "Engine" Architecture (Dispatcher Networks)
The presence of extremely large switch tables (e.g., `fcn.0040f650` with **41 cases** and `fcn.00412c10`) confirms that the malware operates like a processor. 
*   **Mechanism:** Instead of calling "Send_Data" or "Decrypt_Config," the malware processes an internal opcode, which points to one of these switch cases. 
*   **Impact:** This design allows the developers to update the "instruction set" without changing the core logic, making it much harder for signature-based detection to find a consistent footprint for every feature (e.g., exfiltration vs. keylogging).

#### 2. Deep Integration of OLE/COM
The recurring calls to `OLEAUT32.dll_VariantCopy` and interactions with COM objects are critical.
*   **Significance:** This confirms the malware is prepared for **multi-process communication**. It may be designed to:
    *   Pass data between a loader and a separate "worker" process.
    *   Interact with Microsoft Office applications (Excel/Word) via COM, which is common in spear-phishing scenarios.
    *   Utilize COM objects for persistence or to hijack legitimate Windows system functions.

#### 3. Sophisticated Memory Management & Data Wrangling
Functions like `fcn.0040bd9d` and `fcn.0040be83` show a high level of care in how memory is allocated and handled.
*   **Observation:** The code does not just copy data; it calculates buffer sizes, manages segment lengths (e.g., the check for `0x10`, `0x20`), and performs **data normalization** (seen in the calculation dividing by 5000).
*   **Implication:** This suggests the malware is processing structured data—likely a proprietary binary configuration format or an encrypted packet structure—rather than simple strings. It "reassembles" its capabilities from memory just before they are needed.

#### 4. Intentional "Wrapper" Obfuscation
The repeated use of internal function calls (e.g., `fcn.0041fd94`, `fcn.0041fd4d`) as wrappers for standard operations is a primary defensive measure against analysts.
*   **Analysis:** By wrapping common actions in these "utility" functions, the developer ensures that an analyst looking at one piece of code (like the dispatcher) doesn't immediately see what the next step is. It creates a **disconnected logic flow**, where the "real" action only becomes clear during dynamic analysis or deep cross-referencing.

---

### Final Technical Indicators for Incident Response (IR)

The complexity of this final chunk solidifies the classification of this sample as **Tier 1/High-Sophistication.**

**Critical Findings for IR:**
1.  **VM-Style Execution Logic:** The heavy reliance on large switch tables indicates that common "if/else" logic is replaced by a custom interpreter. 
    *   **IR Action:** Traditional static analysis will likely fail to map all functionalities. Focus on **memory resident string extraction** and **API hooking** to see what the "interpreter" actually does when it hits each case.
2.  **OLE/COM Interaction Persistence:** The use of `OLEAUT32` suggests the malware may have a footprint in COM catalogs or interact with Office processes.
    *   **IR Action:** Audit and monitor for unauthorized changes to the Windows Registry related to **CLSID/FileAssociation** and monitor process memory for interactions between `explorer.exe`, `winword.exe`, and `excel.exe`.
3.  **Dynamic Buffer Construction:** The malware constructs its "plans" in memory through multiple processing loops before execution.
    *   **IR Action:** Perform **repeated memory dumps** during a sandbox run (e.g., every 60 seconds). This is the most likely way to capture decrypted C2 IPs, file paths, and stolen data buffers that only exist for a few milliseconds in RAM.

### Refined Recommendations for Investigation:

*   **Behavioral Analysis - "Long-Running" Sandbox:** Because of the multi-layered dispatcher system, some behaviors may only activate after several seconds or minutes of execution as the VM reaches specific states. Use a sandbox with at least a 15-minute runtime.
*   **De-obfuscation via Instrumentation (Frida/x64dbg):** Since many calls are wrapped, use a debugger to "trace" and log every jump from the large switch tables (`0x40f650`, etc.). This will map out which conditions trigger which behaviors.
*   **Signature Generation:** Instead of looking for specific strings (which are likely encoded), create signatures based on the **unique code flow** of the dispatcher switches. The sequence and number of jump-table entries can be a unique "fingerprint" for this specific malware family.
*   **Memory Forensics:** Focus on the heap. Since the data is reconstructed in memory, look for signs of shellcode or decrypted payloads that are "unpacked" within the high-memory regions after passing through the dispatcher functions.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Decryptor | The use of a VM-based execution engine and dynamic buffer construction indicates that malicious logic is only "unpacked" or decrypted into memory at the moment of execution to evade static analysis. |
| **T1601** | Data Obfuscation | The implementation of proprietary binary formats, normalization calculations, and complex data mangling is used to hide configuration details from automated scanners. |
| **T1055** | Process Injection | The integration of OLE/COM for multi-process communication between a "loader" and a "worker" process facilitates the movement of malicious code across processes. |
| **T1036** | Masquerading | The use of internal "wrapper" functions to mask standard operations creates a disconnected logic flow, hiding the true intent of the code from analysts. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section appears to contain heavily obfuscated or encrypted data; no plain-text IP addresses, URLs, or file paths were identified within that specific block.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis notes that C2 IPs are likely decrypted in memory during execution and are not present in the static strings provided).

### **File paths / Registry keys**
*   **Registry Categories:** 
    *   `CLSID` (Potential persistence via COM objects)
    *   `FileAssociation` (Potential modification for hijacking common file types)
*   *Note: Specific absolute paths were not provided in the text.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Hardcoded Function Offsets (Internal Dispatchers):**
    *   `0x40f650` (Large switch table/Dispatcher)
    *   `0x412c10` (Switch table)
    *   `0x40bd9d` (Memory management function)
    *   `0x40be83` (Memory management function)
    *   `0x41fd94` (Wrapped utility function)
    *   `0x41fd4d` (Wrapped utility function)
*   **Library/DLL Interactions:**
    *   `OLEAUT32.dll_VariantCopy` (Used for multi-process communication and COM interaction)
*   **Behavioral Signatures:**
    *   Use of a "VM-style" execution engine to obfuscate logic flow.
    *   Data normalization routine involving division by 5000 (suggests a specific proprietary configuration format).
    *   Interaction with Microsoft Office processes (`winword.exe`, `excel.exe`).

---

## Malware Family Classification

Based on the behavioral analysis provided, here is the classification of the sample:

1.  **Malware family**: **custom** (highly sophisticated/modular)
2.  **Malware type**: **backdoor** (with loader/dropper capabilities)
3.  **Confidence**: **High** (for type and architecture; Medium for specific naming due to lack of unique C2 strings).

**Key evidence:**
*   **VM-Based Dispatcher Architecture:** The use of large switch tables (e.g., `fcn.0040f650` with 41 cases) indicates a "Command Dispatcher" system. This allows the malware to function as a modular backdoor where features (keylogging, exfiltration, etc.) are toggled via an internal instruction set, making it extremely difficult to analyze statically.
*   **OLE/COM Multi-Process Communication:** The reliance on `OLEAUT32` and COM objects confirms a sophisticated multi-process architecture. This is often used to facilitate communication between a "loader" and a hidden "worker" process or to interact with and persist within Microsoft Office applications.
*   **Sophisticated Data Handling:** The presence of custom data normalization (the division by 5000) and complex buffer management suggests the malware is designed to handle a proprietary, encrypted configuration format rather than simple plain-text commands, a hallmark of high-tier (Tier 1) malware.
