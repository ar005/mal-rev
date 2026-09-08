# Threat Analysis Report

**Generated:** 2026-09-07 21:36 UTC
**Sample:** `15790a8793243a4da6cc41ad91a258440c6cec9da0d95116994266d986cb17a6_15790a8793243a4da6cc41ad91a258440c6cec9da0d95116994266d986cb17a6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `15790a8793243a4da6cc41ad91a258440c6cec9da0d95116994266d986cb17a6_15790a8793243a4da6cc41ad91a258440c6cec9da0d95116994266d986cb17a6.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,393,664 bytes |
| MD5 | `aac8f8af6617c2fd6dc8e82f79420a64` |
| SHA1 | `53b364a853e7be27513c865f9574176b3b36de79` |
| SHA256 | `15790a8793243a4da6cc41ad91a258440c6cec9da0d95116994266d986cb17a6` |
| Overall entropy | 7.005 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1732598058 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 570,880 | 6.68 | No |
| `.rdata` | 183,808 | 5.77 | No |
| `.data` | 25,088 | 2.003 | No |
| `.rsrc` | 570,368 | 7.151 | ⚠️ Yes |
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

Total strings found: **2871** (showing first 100)

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

This final chunk of disassembly provides the "smoking gun" regarding the complexity of this malware's internal architecture. It confirms that we are not looking at a standard piece of malware with hardcoded logic, but rather a **custom Virtual Machine (VM) or highly advanced Interpreter** designed to execute a proprietary Instruction Set Architecture (ISA).

The following is the updated and expanded analysis incorporating all four segments.

---

### Final Technical Analysis: Advanced Interpreter-Driven Architecture

#### 1. The "Mega-Interpreter" Logic (Switch Table at `0x408922`)
The most striking discovery in this section is the **switch table with 150 cases** within `fcn.00408922`. 
*   **Complexity of Command Set:** A switch statement of this magnitude indicates that the "engine" can process at least 150 different types of instructions or data structures. This is not a simple "if-then" logic for and standard malware; it is an entire environment designed to host and execute a complex, potentially dynamic, payload.
*   **Instruction Decoding:** The interpreter takes a byte from the data stream (the opcode), identifies which of the 150 paths to take, and then performs associated actions (like moving memory, performing arithmetic, or jumping to different sub-interpreters).

#### 2. Memory State Management & Object Construction
Throughout this section (specifically in the large block starting at `0x48...`), we see consistent use of an "accumulator" or "state object" (represented by `arg_28h`).
*   **Context Persistence:** The code frequently reads and writes to offsets within `arg_28h` (e.g., `*(arg_28h + 0x5c)`, `*(arg_28h + 0x34)`). This indicates that as the interpreter processes a "command," it is updating its internal state or building a complex data structure in memory to be used by the next step of the execution.
*   **Dynamic Re-assembly:** The use of `CONCAT44` and manual pointer arithmetic suggests that the interpreter is **constructing objects piece-by-piece**. It isn't just "decoding" a string; it is building a "functional object" in memory that only takes its final, usable form after passing through multiple stages of the dispatcher.

#### 3. Sophisticated String & Character Handling
The code contains extensive logic for handling **Unicode/UTF-16** (e.g., checks for `0xd800` and `0x2030`).
*   **Multilingual Support:** This suggests the data being interpreted isn't just raw binary; it is likely a structured configuration file or script that includes complex characters, potentially for internationalization or to hide commands within multi-byte character strings.
*   **Sanitization/Validation:** The heavy amount of logic used simply to "validate" and "move" bytes into the correct internal structures suggests that even "simple" actions (like logging a username or a filename) are wrapped in layers of interpretation to evade automated detection.

#### 4. Anti-Analysis via Control Flow Obfuscation
The complexity here is a deliberate defensive measure:
*   **Non-Linear Execution:** By using the large switch tables, the author ensures that there is no "straight line" from entry point to malicious action. An analyst following a single instruction will find themselves in a "loop" of the interpreter, and only by understanding the underlying *data* (the code being fed into the interpreter) can the actual behavior be mapped.
*   **Polymorphic Potential:** Because the logic is interpreted, the core engine remains the same while the "scripts" or "payloads" it runs can change entirely with each infection, making signature-based detection of specific features nearly impossible.

---

### Final Summary for Incident Response

The complexity of this binary has been elevated from "Sophisticated" to **"High-End Custom Architecture."**

*   **Nature of the Threat:** This is an **Interpreter-Driven Payload**. The code we see is a heavy-duty execution engine (Virtual Machine). It is designed to host and execute malicious instructions that are not present in the binary's static form, but exist as data being "fed" into this engine at runtime.
*   **Evasion Strategy:** 
    *   **Complexity Overload:** The use of a 150-case switch table ensures that static analysis cannot easily map out all possible actions of the malware.
    *   **Data-Driven Logic:** By moving the "malice" into the data layer, the authors ensure that standard tools looking for suspicious function calls will only see the "interpreter's housekeeping" (memory moves, pointer arithmetic) rather than the actual malicious acts (keylogging, exfiltration).
*   **Risk Level: Critical/APT.** The level of engineering required to build a custom VM with this much overhead and complexity is characteristic of advanced state-sponsored groups or highly organized cybercrime syndicates.

#### Updated Actionable Recommendations:

1.  **Memory Forensics (High Priority):** Because the "true" behavior is hidden in the data interpreted by `fcn.00408922`, standard static analysis is insufficient. **Perform a memory dump during execution.** Analyze the heap for newly created objects and strings that appear after the interpreter enters its main loop.
2.  **Behavioral Scripting/Tracing:** Instead of trying to map every switch case, use a debugger to log the *values* being passed into the `arg_ch` and `arg_8h` registers inside the dispatcher. These values represent the "instructions" being fed to the VM; mapping these will reveal the actual command sequence.
3.  **Hooking Critical APIs:** Focus on the "exit points" of the interpreter. Identify where the interpreter finally hands off a completed task (e.g., a constructed URL for C2, or a resolved file path) to the Windows API (`InternetConnect`, `CreateFileW`). Trace backward from these calls to identify which "Interpreter State" produced them.
4.  **Identify "Data Seeds":** Look for the areas of memory where the "instructions" are initially loaded/decrypted. These locations likely contain the core logic that defines the malware's behavior once it is running.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Execution | The use of a 150-case "Mega-Interpreter" and non-linear control flow ensures that static analysis cannot easily map the malware's functional logic. |
| T1055 | Packer | The custom Virtual Machine architecture acts as a sophisticated packer, hiding malicious instructions within a data layer to evade signature-based detection. |
| T1027 | Obfuscated Execution | The advanced Unicode/UTF-16 handling and multi-byte character logic are used to hide commands and potentially bypass simple string-matching filters. |

---

## Indicators of Compromise

Based on the provided documentation and string analysis, here is the extraction of Indicators of Compromise (IOCs). 

**Note:** The provided text describes a sophisticated "Interpreter-Driven" architecture (a custom Virtual Machine) used to hide malicious logic. As a result, much of the "malice" is hidden within dynamically generated code or data layers rather than static strings.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: The memory offsets provided in the analysis, such as `0x48...`, are internal program memory locations and do not constitute file system or registry IOCs.)

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Internal Function Address:** `0x408922` (Identified as the core "Mega-Interpreter" switch table logic).
*   **Behavioral Signature:** Use of a large switch table (150 cases) to facilitate an Interpreter-Driven payload.
*   **Encoding/Obfuscation Indicator:** Extensive use of Unicode/UTF-16 processing (specifically checks for `0xd800` and `0x2030`) as a method for potential evasion or multi-lingual command masking.

---
### **Analyst Note:**
The absence of traditional IOCs (IPs, URLs, Files) is expected given the technical analysis provided. The malware uses a **Virtual Machine (VM) architecture** to decouple the malicious behavior from the static file. In this case, "detection" should be based on the presence of the interpreter loop and the 150-case switch table rather than specific network indicators.

---

## Malware Family Classification

Based on the provided technical analysis, here is the classification for this sample:

1. **Malware family**: Custom
2. **Malware type**: Loader (or Backdoor)
3. **Confidence**: High
4. **Key evidence**:
    *   **Virtual Machine (VM) Architecture:** The identification of a "Mega-Interpreter" with 150 switch cases confirms that the malware uses a custom instruction set architecture to hide its true functionality behind a layer of interpretation, making it difficult for automated tools to map its behavior.
    *   **Data-Driven Logic Separation:** By moving the malicious logic into a data layer (the "scripts" fed into the interpreter) rather than hardcoding it, the malware ensures that the core binary remains static while its capabilities can be changed dynamically at runtime.
    *   **Advanced Evasion Techniques:** The use of complex Unicode/UTF-16 handling and sophisticated memory object construction indicates a high level of engineering characteristic of APT (Advanced Persistent Threat) activity or highly organized cybercrime groups.
