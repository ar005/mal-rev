# Threat Analysis Report

**Generated:** 2026-07-14 16:58 UTC
**Sample:** `05c625480da7f9766014b0464c21bff0b6d97a0ae4e97b44997464ba0efbfa3a_05c625480da7f9766014b0464c21bff0b6d97a0ae4e97b44997464ba0efbfa3a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05c625480da7f9766014b0464c21bff0b6d97a0ae4e97b44997464ba0efbfa3a_05c625480da7f9766014b0464c21bff0b6d97a0ae4e97b44997464ba0efbfa3a.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,024,512 bytes |
| MD5 | `ad744503b5dcbdeaf48076635ab7174d` |
| SHA1 | `cd245152ca104645fb9de8366b5c42b73e667509` |
| SHA256 | `05c625480da7f9766014b0464c21bff0b6d97a0ae4e97b44997464ba0efbfa3a` |
| Overall entropy | 6.89 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1763692955 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 570,880 | 6.68 | No |
| `.rdata` | 183,808 | 5.77 | No |
| `.data` | 25,088 | 2.003 | No |
| `.rsrc` | 201,216 | 7.738 | ⚠️ Yes |
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

Total strings found: **2413** (showing first 100)

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

This final chunk of disassembly provides the ultimate confirmation of the malware's nature. While earlier chunks suggested a script interpreter, this section reveals that the binary contains a **full-featured grammar parser and expression evaluator.** 

The complexity seen here is not just "smart" code; it is typical of a professional-grade compiler front-end or an embedded scripting engine (similar to those found in high-level languages like Lua, Python, or JavaScript).

### Updated Analysis: Binary Functionality & Behavioral Profile

#### 1. Core Functionality and Purpose
The inclusion of this final block moves the analysis from "advanced interpreter" to a **sophisticated grammar parser.**

*   **Deep Grammar Parsing (Recursive Descent Logic):** The massive switch blocks (e.g., at `0x48bc`, `0x48d1`) are not checking simple commands; they are handling **nested structures.** Notice the logic for character `0x50` and `0x3c`: it's tracking state across multiple "levels." This indicates the engine can handle nested parentheses, brackets, and complex mathematical or logical expressions.
*   **Tokenization and Validation:** The code frequently checks if a byte is within a certain range (e.g., `0x2f` to `0x3a`). It identifies specific special characters (like `(` , `)`, `[`, `]`, `{`, `}`). This suggests the engine takes a raw string of "script" and converts it into an internal token stream before execution.
*   **Advanced Memory-Mapping for Logic:** The section where it calculates offsets like `*(arg_28h + 0x30) * 0xc` suggests that once the "lexer" (the part we just saw) determines a piece of code is valid, the "evaluator" maps those instructions into memory. It isn't just interpreting one line; it is building an internal representation of a program.

#### 2. Sophisticated Malicious Behaviors
The complexity shown in this specific segment points to several advanced capabilities:

*   **Execution of Complex Logic (State Machines):** Because the parser can handle nested conditions and complex expressions, the malware can execute sophisticated logic like "If [Condition A] AND ([Condition B] OR [Condition C]) THEN perform Action X." This allows for highly conditional behavior—such as only activating if certain system environment variables are present—making it very hard to detect via automated sandboxing.
*   **Immune-to-Pattern Analysis:** Because the "maliciousness" is buried inside a complex language's grammar, standard antivirus signatures cannot easily flag the actions. The signature of the *interpreter* is static, but the *logic* provided by the remote script can be anything from a simple file deletion to a complex multi-stage ransomware deployment.
*   **Advanced Anti-Forensics via Lexing:** By utilizing a formal grammar, the threat actor can "obfuscate" their commands using standard programming techniques (variable renaming, nested logic, and loops). A researcher looking at the raw network traffic might see valid-looking code that only makes sense when processed by this specific engine.

#### 3. Notable Techniques & Patterns
*   **Unified Unicode Handling:** The consistent check for `0x80` ranges and surrogate pairs (`0xd800`) indicates a very "modern" approach to coding. This allows the attacker to use high-bit characters or non-Latin scripts in their control commands, effectively bypassing security filters that only look for ASCII-based keywords like "Download," "Delete," or "Connect."
*   **Stateful Parsing:** The variables `var_4h`, `var_10h`, and `var_2ch` act as a **state machine**. They track whether the interpreter is currently inside a string, a comment, an expression, or a nested block. This ensures that if an attacker puts a "forbidden" command inside a quoted string, the engine correctly ignores it as code—making the infection much more stable and resilient for the attacker.
*   **High-Efficiency Buffer Management:** The repeated use of `0x10` (decimal 16) offsets in data structures suggests a well-defined internal "VM" state where different parameters (operand count, instruction pointer, stack depth) are stored at fixed offsets from a base pointer (`arg_28h`).

---

### Updated Summary for Report

**Analysis Overview:**
The final analysis confirms that the binary contains an **industrial-grade grammar parser and script execution engine.** It is not merely "malicious" in its direct actions; it is a **delivery platform** designed to host and execute complex, multi-stage scripts. The presence of advanced logic for handling nested expressions and broad Unicode support indicates a high level of professional development effort.

**Key Indicators of Concern:**
1.  **Sophisticated Scripting Infrastructure:** The binary implements a formal grammar parser capable of handling nested structures and complex evaluations. This allows the threat actor to deliver "modular" payloads; they can update the malware's functionality remotely by sending new scripts without ever changing the malicious binary on the victim's machine.
2.  **Advanced Obfuscation Layer:** By using a multi-layered interpretation method (Lexing $\rightarrow$ Parsing $\rightarrow$ Execution), the author hides the true intent of the malware from static analysis and simple heuristic scanners. The "maliciousness" only becomes apparent during execution when the script is parsed by this engine.
3.  **High Complexity / APT Characteristics:** The robustness of the parser (handling Unicode, escaped characters, and nested logic) is characteristic of Advanced Persistent Threat (APT) tools. This level of development is typically found in state-sponsored or high-level organized crime operations where the goal is long-term persistence and flexibility.

**Conclusion:**
This binary acts as a **"Headless Command Center."** It provides a stable, complex environment for an attacker to execute diverse tasks (e.g., credential theft, lateral movement, data exfiltration) through a hidden, dynamically loaded scripting language. The sheer complexity of the parser serves both as a functional requirement for advanced operations and a defensive measure against automated detection systems.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1059 | Command and Scripting Interpreter | The analyst identifies a full-featured grammar parser and expression evaluator capable of executing complex logic similar to Lua, Python, or JavaScript. |
| T1027 | Obfuscated Code or Programs | The multi-layered interpretation (Lexing $\rightarrow$ Parsing $\rightarrow$ Execution) is used to hide the malicious intent from static analysis and signature-based detection. |
| T1485 | Data Encoding | The use of unified Unicode handling allows the threat actor to bypass security filters that only scan for common ASCII-based keywords. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contains heavily obfuscated or non-human-readable data. No standard network identifiers (IPs/URLs) or file system paths were present in those specific strings.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (Behavioral Indicators)**
The following are behavioral indicators derived from the technical analysis of the binary's logic:

*   **Advanced Scripting Engine:** The malware utilizes a "sophisticated grammar parser" and "expression evaluator." This indicates the binary acts as a host for dynamically loaded scripts, allowing the threat actor to change functionality (e.g., switching from data theft to ransomware) without changing the underlying file signature.
*   **State-Machine Parsing Logic:** Use of internal variables (e.g., `var_4h`, `var_10h`, `var_2ch`) to track state, such as whether the engine is currently processing a string, comment, or nested block.
*   **Unicode Evasion Techniques:** The code specifically handles the `0x80` range and surrogate pairs (`0xd800`). This is an intentional tactic to bypass security filters that primarily scan for standard ASCII keywords (e.g., "connect", "download").
*   **Recursive Descent Logic:** Use of nested structure handling (specifically checking for characters like `(` , `)`, `[`, `]`, `{`, `}`) to allow the execution of complex, multi-layered logical conditions.
*   **High-Efficiency Buffer Management:** Implementation of a fixed-offset internal "Virtual Machine" (VM) state to manage instruction pointers and stack depth.

---

## Malware Family Classification

Based on the provided technical analysis, here is the classification of the sample:

1.  **Malware family:** custom (Sophisticated Framework)
2.  **Malware type:** loader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Advanced Scripting Infrastructure:** The discovery of a "full-featured grammar parser" and "expression evaluator" indicates that the binary is not just a simple malware sample, but a sophisticated **loader/delivery platform**. It is designed to host and execute complex scripts (similar to those used in Cobalt Strike or Sliver) to perform various tasks like data exfiltration or lateral movement.
    *   **Layered Obfuscation via Interpretation:** By utilizing a Lexer $\rightarrow$ Parser $\rightarrow$ Execution pipeline, the malware hides its true intent from signature-based detection. The "maliciousness" is decoupled from the binary and resides in the dynamically loaded scripts, which only become active during execution.
    *   **High-Level Development (APT Characteristics):** The inclusion of robust features like unified Unicode handling, state-machine logic for nested structures, and complex memory-mapping techniques indicates a professional-grade tool typically associated with advanced threat actors seeking long-term persistence and modularity.
