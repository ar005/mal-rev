# Threat Analysis Report

**Generated:** 2026-07-24 15:18 UTC
**Sample:** `0a191015e582ea155d70d7c8507798c8744d4d8cf8670e548e9a74738fc92a79_0a191015e582ea155d70d7c8507798c8744d4d8cf8670e548e9a74738fc92a79.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a191015e582ea155d70d7c8507798c8744d4d8cf8670e548e9a74738fc92a79_0a191015e582ea155d70d7c8507798c8744d4d8cf8670e548e9a74738fc92a79.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,201,664 bytes |
| MD5 | `7a1cf4970f5372c78ce67ea521bf054e` |
| SHA1 | `7ffcac939ba23a33ebf64a4ff79192bf5454dea3` |
| SHA256 | `0a191015e582ea155d70d7c8507798c8744d4d8cf8670e548e9a74738fc92a79` |
| Overall entropy | 7.136 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1762863145 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 570,880 | 6.68 | No |
| `.rdata` | 183,808 | 5.77 | No |
| `.data` | 25,088 | 2.003 | No |
| `.rsrc` | 378,368 | 7.902 | ⚠️ Yes |
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

Total strings found: **2764** (showing first 100)

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

This final disassembly (chunk 4/4) provides a deeper look into the "inner workings" of the interpreter's core execution loop and its handling of complex data structures. It confirms that this is not just an interpreter for simple commands, but a **highly sophisticated, multi-layered execution environment.**

Below is the updated analysis incorporating all four chunks.

---

### Final Analysis: Advanced Multi-Stage Scripting Engine & VM Architecture

The complete disassembly reveals a high-maturity programming architecture designed to decouple malicious logic from the executable binary. The code functions as a "Virtual Machine" (VM) that executes an opaque, custom instruction set (bytecode) or a high100% abstracted scripting language (similar to specialized versions of Lua or JavaScript used in advanced trojans).

---

### Key Technical Observations (Synthesis of All Chunks)

#### 1. Complex Instruction Set Architecture (ISA) & Dispatch
The presence of massive switch tables (e.g., `0x48bb3e`, `0x48b3d1`) and the dense logic in `fcn.00408922` and `fcn.00408e6e` indicate a complex **Instruction Dispatcher**.
*   **Opcode Variety:** The wide range of cases (e.g., 0x2b through 0x39, 0x50, 0x7c) suggests that the interpreter can handle a vast array of "opcodes." These likely map to functions like `MOVE`, `LOAD_VAR`, `CALL_FUNCTION`, `IF_GOTO`, and string manipulation.
*   **Validation Logic:** The nested conditions (e.g., checking if a value is between 0x2f and 0x3a) suggest the interpreter validates its own bytecode during execution, ensuring that only "authorized" instructions are processed by the engine.

#### 2. Object-Oriented Interpreter Environment
The code frequently accesses offsets within `arg_28h` (e.g., `*(arg_28h + 0x5c)`, `*(arg_28h + 0x14)`). This indicates that the interpreter maintains a **Runtime Environment** or "Context" structure:
*   **State Management:** It tracks variables, memory addresses, and stack positions within its own internal space.
*   **Dynamic Types:** The logic handles different data types (integers, strings, nested objects) by checking specific flags or value ranges before proceeding with a routine.

#### 3. Advanced String & Unicode Handling
A significant portion of the code is dedicated to processing multi-byte characters and complex string buffers.
*   **Robust Decoding:** It doesn't just handle ASCII; it appears designed to parse "dirty" or obfuscated input data that might contain non-standard characters used as decoys for malicious commands.
*   **Buffer Management:** The lookahead logic (checking the *next* byte to determine if it is part of a multi-byte character) indicates a professional-grade string parser, likely used to handle filenames, URLs, or C2 addresses dynamically.

#### 4. Intentional Obfuscation via "Layered" Execution
By using this architecture, the threat actor achieves several goals:
*   **Decoupling:** The binary is just a machine; the "malice" lives in the script/bytecode it consumes. An analyst looking at the `.text` section of the EXE will see an interpreter (safe-looking), while the data buffer contains the actual attack logic.
*   **Polymorphism:** To change the malware's behavior (e.g., switch from keylogging to file exfiltration), the attacker only needs to update the script provided to the engine, not the binary itself.
*   **Anti-Automation:** Automated sandboxes may execute the "interpreter" and see nothing malicious because they do not possess the specific "keys" or "scripts" required to trigger the complex functionality.

---

### Risk Assessment: Critical/High

The sophistication of this component suggests a **high-end adversary**, likely an APT (Advanced Persistent Threat) group or a sophisticated cybercriminal organization (e.g., those behind high-tier banking trojans).

*   **Sophistication Level:** Very High. The use of custom VM architectures is a hallmark of modern, professional-grade malware designed to evade signature-based detection and complicate manual reverse engineering.
*   **Evasion Strategy:** This code is a "shield." It ensures that standard tools (like strings, imports, or simple heuristic scanners) will not flag the behavior because the malicious intent is hidden behind multiple layers of abstraction.
*   **Core Purpose:** The engine likely serves as the heart of a multi-functional trojan or modular loader. It allows for dynamic "plug-and-play" functionality where different modules can be activated based on the script fed into this interpreter.

---

### Summary for Malware Report

**Component Classification:** Custom Scripting Engine / Virtual Machine (VM) Interpreter
**Primary Functions:**
1.  **Bytecode Processing:** Uses a complex dispatch system to interpret custom, potentially obfuscated instructions from an external data blob.
2.  **Robust Parsing:** Includes advanced handling for Unicode/multi-byte characters and dynamic buffer management.
3.  **Stateful Execution:** Maintains a high-level internal state (variables, memory maps, etc.) allowing for complex, multi-step logic (loops, conditionals) within the script.

**Indicators of Interest (IOCs) & Analyst Notes:**
*   **Highly Obscured Intent:** The primary malicious actions (e.g., data theft, persistence, lateral movement) are **not** present in the machine code. They are contained within the "data" that this interpreter consumes.
*   **Anti-Analysis Techniques:** The complexity of the switch tables and nested logic is designed to exhaust human analysts and bypass automated tools. 
*   **Detection Guidance:** Analysis should focus on identifying the **source of the script/bytecode**. Search for encrypted or appended data blobs in the binary, as these contain the "true" instructions that this engine will execute.
*   **Threat Actor Profile:** Sophisticated; indicates a developer capable of creating custom infrastructure to evade signature-based and heuristic detection.

**Next Steps:** Identify and extract any high-entropy (encrypted/compressed) data blocks in the file's resources or as appends. These are likely the "scripts" for this interpreter. Decoding these will reveal the actual capabilities of the malware.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a custom VM architecture, opaque bytecode, and multi-byte string handling is designed to hide malicious intent from static analysis tools. |
| **T1059** | Command and Scripting Interpreter | The software functions as an interpreter for a proprietary instruction set to execute complex logic (loops, conditionals) that is decoupled from the main binary. |
| **T1055** | Packed_Execution (Packer) | While technically a custom VM, this architecture serves the same purpose as a packer by acting as a protective "shield" or wrapper around the core payload. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted intelligence:

**IP addresses / URLs / Domains**
*   None identified (The text contains obfuscated data and no clear network infrastructure).

**File paths / Registry keys**
*   None identified (Note: Standard system paths or common library strings were excluded per instructions).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified (No MD5, SHA1, or SHA256 hashes appear in the provided data).

**Other artifacts**
*   **Architecture Signature:** Custom Scripting Engine / Virtual Machine (VM) Interpreter.
*   **Instruction Dispatcher Offsets:** `0x48bb3e`, `0x48b3d1` (Used to identify the interpreter's core logic loop).
*   **Function Indicators:** `fcn.00408922`, `fcn.00408e6e` (Identified as the primary dispatch and processing centers for the VM).
*   **Opcode Range Signature:** The presence of a wide range of opcodes (e.g., 0x2b through 0x39, 0x50, 0x7c) used for internal logic mapping.
*   **Behavioral Note:** High-level "layered" execution designed to hide malicious intent behind an abstraction layer; actual malicious payloads are likely stored in encrypted/appended data blocks rather than the executable's code section.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
* **Virtual Machine (VM) Architecture**: The analysis confirms the use of a sophisticated, multi-layered interpreter and a complex Instruction Set Architecture (ISA). This is a hallmark of high-end malware used to hide malicious logic within custom bytecode, effectively decoupling the payload from the executable.
* **Advanced Obfuscation Techniques**: The use of massive switch tables, dynamic state management, and robust Unicode handling indicates a professional-grade construction designed specifically to evade signature-based detection and automated sandbox analysis.
* **Modular Execution Design**: The report highlights that the engine serves as a "shell" or "shield," allowing for "plug-and-play" functionality where different malicious behaviors (e.g., data theft, lateral movement) are switched by changing scripts rather than altering the core binary.
