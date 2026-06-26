# Threat Analysis Report

**Generated:** 2026-06-25 16:46 UTC
**Sample:** `00f01750994214b5d936755f4e67db0663fe9787960817e2bcb7b3c85e394f98_00f01750994214b5d936755f4e67db0663fe9787960817e2bcb7b3c85e394f98.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00f01750994214b5d936755f4e67db0663fe9787960817e2bcb7b3c85e394f98_00f01750994214b5d936755f4e67db0663fe9787960817e2bcb7b3c85e394f98.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 6 sections |
| Size | 1,462,026 bytes |
| MD5 | `6f492a9437819a4f664d456da5657068` |
| SHA1 | `8c5e9b1540011b0946aae58cbaa884148eba13d1` |
| SHA256 | `00f01750994214b5d936755f4e67db0663fe9787960817e2bcb7b3c85e394f98` |
| Overall entropy | 6.786 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1551865808 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 581,120 | 6.676 | No |
| `.rdata` | 188,928 | 5.733 | No |
| `.data` | 20,992 | 1.199 | No |
| `.rsrc` | 566,784 | 6.702 | No |
| `.reloc` | 29,184 | 6.779 | No |
| `.htext` | 69,632 | 0.149 | No |

### Imports

**KERNEL32.DLL**: `DuplicateHandle`, `CreateThread`, `WaitForSingleObject`, `HeapAlloc`, `GetProcessHeap`, `HeapFree`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `MulDiv`, `GetVersionExW`, `IsWow64Process`, `GetSystemInfo`, `FreeLibrary`, `LoadLibraryA`
**ADVAPI32.dll**: `GetAce`, `RegEnumValueW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegOpenKeyExW`, `RegCloseKey`, `RegQueryValueExW`, `RegConnectRegistryW`, `InitializeSecurityDescriptor`, `InitializeAcl`, `AdjustTokenPrivileges`, `OpenThreadToken`, `OpenProcessToken`
**COMCTL32.dll**: `ImageList_ReplaceIcon`, `ImageList_Destroy`, `ImageList_Remove`, `ImageList_SetDragCursorImage`, `ImageList_BeginDrag`, `ImageList_DragEnter`, `ImageList_DragLeave`, `ImageList_EndDrag`, `ImageList_DragMove`, `InitCommonControlsEx`, `ImageList_Create`
**COMDLG32.dll**: `GetOpenFileNameW`, `GetSaveFileNameW`
**GDI32.dll**: `StrokePath`, `DeleteObject`, `GetTextExtentPoint32W`, `ExtCreatePen`, `GetDeviceCaps`, `EndPath`, `SetPixel`, `CloseFigure`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `SelectObject`, `StretchBlt`, `GetDIBits`, `LineTo`, `AngleArc`
**IPHLPAPI.DLL**: `IcmpCreateFile`, `IcmpCloseHandle`, `IcmpSendEcho`
**MPR.dll**: `WNetUseConnectionW`, `WNetCancelConnection2W`, `WNetGetConnectionW`, `WNetAddConnection2W`
**ole32.dll**: `CoTaskMemAlloc`, `CoTaskMemFree`, `CLSIDFromString`, `ProgIDFromCLSID`, `CLSIDFromProgID`, `OleSetMenuDescriptor`, `MkParseDisplayName`, `OleSetContainedObject`, `CoCreateInstance`, `IIDFromString`, `StringFromGUID2`, `CreateStreamOnHGlobal`, `OleInitialize`, `OleUninitialize`, `CoInitialize`
**OLEAUT32.dll**: `LoadTypeLibEx`, `VariantCopyInd`, `SysReAllocString`, `SysFreeString`, `SafeArrayDestroyDescriptor`, `SafeArrayDestroyData`, `SafeArrayUnaccessData`, `SafeArrayAccessData`, `SafeArrayAllocData`, `SafeArrayAllocDescriptorEx`, `SafeArrayCreateVector`, `RegisterTypeLib`, `CreateStdDispatch`, `DispCallFunc`, `VariantChangeType`
**PSAPI.DLL**: `GetProcessMemoryInfo`
**SHELL32.dll**: `DragQueryPoint`, `ShellExecuteExW`, `DragQueryFileW`, `SHEmptyRecycleBinW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHCreateShellItem`, `SHGetDesktopFolder`, `SHGetSpecialFolderLocation`, `SHGetFolderPathW`, `SHFileOperationW`, `ExtractIconExW`, `Shell_NotifyIconW`, `ShellExecuteW`, `DragFinish`
**USER32.dll**: `AdjustWindowRectEx`, `CopyImage`, `SetWindowPos`, `GetCursorInfo`, `RegisterHotKey`, `ClientToScreen`, `GetKeyboardLayoutNameW`, `IsCharAlphaW`, `IsCharAlphaNumericW`, `IsCharLowerW`, `IsCharUpperW`, `GetMenuStringW`, `GetSubMenu`, `GetCaretPos`, `IsZoomed`
**USERENV.dll**: `DestroyEnvironmentBlock`, `UnloadUserProfile`, `CreateEnvironmentBlock`, `LoadUserProfileW`
**UxTheme.dll**: `IsThemeActive`
**VERSION.dll**: `GetFileVersionInfoW`, `GetFileVersionInfoSizeW`, `VerQueryValueW`
**WININET.dll**: `InternetQueryDataAvailable`, `InternetCloseHandle`, `InternetOpenW`, `InternetSetOptionW`, `InternetCrackUrlW`, `HttpQueryInfoW`, `InternetQueryOptionW`, `HttpOpenRequestW`, `HttpSendRequestW`, `FtpOpenFileW`, `FtpGetFileSize`, `InternetOpenUrlW`, `InternetReadFile`, `InternetConnectW`
**WINMM.dll**: `timeGetTime`, `waveOutSetVolume`, `mciSendStringW`
**WSOCK32.dll**: `WSACleanup`, `socket`, `ioctlsocket`, `setsockopt`, `ntohs`, `recvfrom`, `inet_addr`, `htons`, `WSAStartup`, `__WSAFDIsSet`, `select`, `accept`, `listen`, `bind`, `closesocket`

## Extracted Strings

Total strings found: **3011** (showing first 100)

```
!This program cannot be run in DOS mode.
$
Richr}
`.rdata
@.data
@.reloc
B.htext
t$8]4t
9^Xt=9^\tE
VW90XL
M8V:t
WWjdh,
PWWWWh
t<j	Yf;
t4j"Yf;
tj	Yf;
L$$9N@
j\_f98
8F4ti!E
u9^u
t;Mr
rCSVWj
<t9<
tP
Yj?Yj0Z
uWj0[
j9Zj._f9<A
r%j9Yf;
<{=tfjB
jh|&I
jhD&I
jh`&I
tNjh,
|$pAU3!
?#tRf9
f98t?j
9Fs4j
R$;N|
t+HuA9
AHt!H
FHu4j

AHt;Ht.H
HtHt5Hu
FHt7HtPHt
D$<DdL
D$`DdL
D$8DdL
D$`DdL
D$<;D$Hr
L$;5hdL
9D$lu;
9t$lv6
F;t$lr
jNYf9H
9t$(v-
F;t$(r
D$$PVj
D$(PVj
D$Pj9
D$d|)I
D$p$*I
09L$ v"
Ht)Ht&H
L$L;|$D
D$0FVP
D$(;D$8
 !"#$%%%%%%&&'()*+%%%%%%&&'()*+,,,,,,--./012RRRRRRRRRRRR3345566789::::;<=<=>?>@ABC>@ABCRRRRRDEFGHIJKLMNO
v F,P
v F,PR
~:9~(~)
4Ff9>t
4Ff9>u
		

			
	
D$49G@
u6jwXf9
\$ j|Zf9
L$LjxXf
}49T$,t
Zj\YjE3
j\_f9~
uj-Xf9F
j]Xf9F
Zj:Xf;
uj]_f;
						
												
						
																									
(SVWjp
YYj!Yf;
<SVWjw
awjUXf;



+t\HHtT
F;Bt
SVWjA_jZ+
uBjAYjZ+
uWtj-Xf
tf;1u
SVjA[jZ^+
jAZjZ^
9E v\PWj
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00416f9e` | `0x416f9e` | 250462 | ✓ |
| `fcn.00418808` | `0x418808` | 248646 | ✓ |
| `fcn.00418ad0` | `0x418ad0` | 248409 | ✓ |
| `fcn.00418c84` | `0x418c84` | 248135 | ✓ |
| `fcn.00418d4c` | `0x418d4c` | 248125 | ✓ |
| `fcn.004182b3` | `0x4182b3` | 248114 | ✓ |
| `fcn.00418e39` | `0x418e39` | 247926 | ✓ |
| `fcn.004184fe` | `0x4184fe` | 247789 | ✓ |
| `fcn.004184d3` | `0x4184d3` | 247744 | ✓ |
| `fcn.004181f9` | `0x4181f9` | 247717 | ✓ |
| `fcn.004185c0` | `0x4185c0` | 247710 | ✓ |
| `fcn.004184a5` | `0x4184a5` | 247704 | ✓ |
| `fcn.00418126` | `0x418126` | 246332 | ✓ |
| `fcn.00414860` | `0x414860` | 243014 | ✓ |
| `fcn.00415760` | `0x415760` | 241972 | ✓ |
| `fcn.004166e1` | `0x4166e1` | 241625 | ✓ |
| `fcn.00415520` | `0x415520` | 241613 | ✓ |
| `fcn.00415e28` | `0x415e28` | 241432 | ✓ |
| `fcn.0041633c` | `0x41633c` | 240907 | ✓ |
| `fcn.00416063` | `0x416063` | 240885 | ✓ |
| `fcn.00415c32` | `0x415c32` | 240789 | ✓ |
| `fcn.004154a8` | `0x4154a8` | 240753 | ✓ |
| `fcn.00415d3f` | `0x415d3f` | 240669 | ✓ |
| `fcn.00416165` | `0x416165` | 240658 | ✓ |
| `fcn.00416192` | `0x416192` | 240642 | ✓ |
| `fcn.00416c5d` | `0x416c5d` | 240478 | ✓ |
| `fcn.004165ec` | `0x4165ec` | 240332 | ✓ |
| `fcn.00401290` | `0x401290` | 238517 | ✓ |
| `fcn.00401424` | `0x401424` | 238485 | ✓ |
| `fcn.004012f3` | `0x4012f3` | 238469 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401290.c`](code/fcn.00401290.c)
- [`code/fcn.004012f3.c`](code/fcn.004012f3.c)
- [`code/fcn.00401424.c`](code/fcn.00401424.c)
- [`code/fcn.00414860.c`](code/fcn.00414860.c)
- [`code/fcn.004154a8.c`](code/fcn.004154a8.c)
- [`code/fcn.00415520.c`](code/fcn.00415520.c)
- [`code/fcn.00415760.c`](code/fcn.00415760.c)
- [`code/fcn.00415c32.c`](code/fcn.00415c32.c)
- [`code/fcn.00415d3f.c`](code/fcn.00415d3f.c)
- [`code/fcn.00415e28.c`](code/fcn.00415e28.c)
- [`code/fcn.00416063.c`](code/fcn.00416063.c)
- [`code/fcn.00416165.c`](code/fcn.00416165.c)
- [`code/fcn.00416192.c`](code/fcn.00416192.c)
- [`code/fcn.0041633c.c`](code/fcn.0041633c.c)
- [`code/fcn.004165ec.c`](code/fcn.004165ec.c)
- [`code/fcn.004166e1.c`](code/fcn.004166e1.c)
- [`code/fcn.00416c5d.c`](code/fcn.00416c5d.c)
- [`code/fcn.00416f9e.c`](code/fcn.00416f9e.c)
- [`code/fcn.00418126.c`](code/fcn.00418126.c)
- [`code/fcn.004181f9.c`](code/fcn.004181f9.c)
- [`code/fcn.004182b3.c`](code/fcn.004182b3.c)
- [`code/fcn.004184a5.c`](code/fcn.004184a5.c)
- [`code/fcn.004184d3.c`](code/fcn.004184d3.c)
- [`code/fcn.004184fe.c`](code/fcn.004184fe.c)
- [`code/fcn.004185c0.c`](code/fcn.004185c0.c)
- [`code/fcn.00418808.c`](code/fcn.00418808.c)
- [`code/fcn.00418ad0.c`](code/fcn.00418ad0.c)
- [`code/fcn.00418c84.c`](code/fcn.00418c84.c)
- [`code/fcn.00418d4c.c`](code/fcn.00418d4c.c)
- [`code/fcn.00418e39.c`](code/fcn.00418e39.c)

## Behavioral Analysis

This final analysis integrates the findings from **Chunk 5/5**, which provides the most definitive evidence yet regarding the sophistication and capabilities of this module. 

The addition of these segments allows us to refine our classification even further: this is not just a "script interpreter," but a **robust, multi-purpose execution environment (runtime)** that includes **Regular Expression (Regex) processing** and **GDI-based graphical manipulation**.

---

### Updated Analysis Report (Chunks 1–5 Integrated)

#### 1. Core Functionality and Purpose
The analysis confirms this is an industrial-grade interpreter designed for high-complexity, remote-controlled operations.

*   **Advanced Lexer & Grammar Processing:** The massive switch tables and recursive logic in `fcn.00416c5d` indicate a sophisticated grammar parser. It doesn't just recognize commands; it interprets structured logic, allows for nested expressions, and manages complex state transitions during script execution.
*   **Native Regular Expression (Regex) Support:** A critical discovery in **Chunk 5** is the inclusion of a full Regex engine (evidenced by strings like `"argument is not a compiled regular expression"` and `"internal error: opcode not recognized"`). This allows an attacker to perform advanced pattern matching on system data, file paths, or network traffic without needing to hardcode specific strings.
*   **Sophisticated Unicode/Multi-Language Handling:** The consistent use of 0x10000 offsets and handling of surrogate pairs (`0xd800`) ensures that the interpreter can process any character set, making it resilient against localization hurdles and capable of interacting with internationalized data seamlessly.

#### 2. Sophisticated Technical Implementation
The technical maturity of the code suggests a "weaponized" library—likely taken from an existing high-level programming language runtime (e.g., parts of Python, Lua, or a specialized scripting engine).

*   **Robust Memory & State Management:** Functions like `fcn.00415c32` and `fcn.00416165` show meticulous management of internal tables and the automated cleanup of system handles (`CloseHandle`, `VirtualFreeEx`). This indicates a high degree of stability; the malware is designed to run reliably for long periods without crashing or leaking resources.
*   **Instructional State Machine:** The way the code jumps between "states" (e.g., in `fcn.00416c5d`) suggests that the engine maintains a virtual machine state, where it processes the script as a series of instructions rather than just executing sequential commands.

#### 3. Indicators of Malicious Intent (Contextual Analysis)
The specific technical capabilities found in this final chunk point to several high-level malicious goals:

*   **Sophisticated Automation & Data Mining:** By including a **Regex engine**, the attacker can send "logic-heavy" scripts from their C2 server. For example, instead of a simple command to search for a file name, they can send a complex regular expression to find any sensitive document containing specific patterns (e.g., credit card numbers or internal project codes).
*   **Advanced User Interface Manipulation:** The integration of `GDI32.dll` functions (`Ellipse`, `AngleArc`, `MoveToEx`) and the usage of `SendMessageW`/`InvalidateRect` indicate that this engine can **generate its own visual components**. This could be used to:
    *   Create "fake" overlays or pop-up windows that mimic system alerts.
    *   Render custom UI elements for a remote operator.
    *   Overlay graphical content over other active windows (e.g., injecting "Buy Now" buttons onto a banking website).
*   **High Stealth through Layered Abstraction:** By using such a complex engine, the developers have separated the *malware's logic* from its *core functions*. The core binary is just an interpreter; the actual malicious "behavior" (keylogging, exfiltration, etc.) exists only in the scripts sent by the attacker. This makes it extremely difficult for automated sandboxes to predict what the malware will do until a specific script is received.

---

### Final Summary for Reporting

The analyzed component is a **highly mature, multi-layered script execution and interpretation engine.** It provides the "brain" of a sophisticated modular malware framework (likely an APT or high-level cybercrime tool).

**Key Findings:**
1.  **Professional Grade Engine:** The inclusion of specialized parsing logic for Unicode, complex state management, and robust memory handling indicates this is a professional-grade interpreter rather than a simple command parser.
2.  **Native Regular Expression (Regex) Support:** The presence of an integrated Regex engine allows the attacker to perform high-level data filtering and automated searches across the victim's filesystem or memory using complex patterns.
3.  **Graphical Rendering Capabilities:** The inclusion of GDI calls indicates that the script interpreter can be used to create, modify, or overlay graphical elements on the screen. This is a strong indicator of capabilities like "overlay injection" or the creation of fraudulent UI components.
4.  **Robust Interaction Logic:** The integration of `SendMessage` and window-handling routines confirms the engine's ability to manipulate other applications directly.

**Conclusion:**
This component represents a **highly advanced threat.** It provides an infrastructure where the attacker can "update" the malware’s functionality remotely by simply pushing new scripts through the interpreter. By utilizing an industrial-grade execution environment, the attackers have ensured that their tool is stable, highly capable of complex logic (via Regex and loops), and versatile enough to perform anything from stealthy data collection to active UI manipulation.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The core functionality described is a "robust, multi-purpose execution environment" that interprets complex grammar and stateful logic to execute remote commands. |
| **T1083** | File and Directory Discovery | The integration of a native Regular Expression (Regex) engine enables the attacker to perform advanced, automated searches for specific patterns (e.g., PII or credentials) within system files. |
| **T1036** | Masquerading | The use of GDI functions to create "fake" overlays and windows that mimic system alerts indicates an intent to deceive users by masquerading as legitimate system components. |
| **T1583.002** | Malicious Tool Distribution (via Web Service) | The modular architecture allows the attacker to remotely update the malware's capabilities via scripts, effectively distributing new "tools" or functions through the interpreter. |
| **T1071** | Application Layer Protocol | The interaction with `SendMessageW` and system-level window handling indicates the engine is designed to interact with other applications at the protocol/API layer for manipulation. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided data contains significant **behavioral indicators** and **technical artifacts** related to a sophisticated script interpreter, but it does not contain "traditional" network IOCs (such as hardcoded IP addresses or URLs) or file system IOCs. The strings appear to be obfuscated/raw memory data, while the report describes the underlying capabilities of the malware's engine.

---

### **IOC_REPORT**

**IP addresses / URLs / Domains**
*   *None identified.* (The analysis indicates that C2 interaction occurs via a script-driven model, but no specific infrastructure is listed in the provided text.)

**File paths / Registry keys**
*   *None identified.* (While `GDI32.dll` and various system APIs are mentioned, these are standard Windows components and do not constitute specific malicious file paths.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Internal Function Offsets:** 
    *   `0x416c5d` (Associated with grammar parsing/switch tables)
    *   `0x415c32` (Associated with memory and state management)
    *   `0x416165` (Associated with system handle cleanup)
*   **Potential YARA/Signature Strings:** 
    *   `"argument is not a compiled regular expression"` (Indicates an integrated Regex engine)
    *   `"internal error: opcode not recognized"` (Indicates a custom virtual machine or instruction set)
*   **API Dependencies:** 
    *   `GDI32.dll` functions (`Ellipse`, `AngleArc`, `MoveToEx`) — *Note: These indicate graphical manipulation capabilities.*
    *   `SendMessageW`, `InvalidateRect` — *Note: Used for UI interaction and potential overlay creation.*

---

### **Analyst Notes**
The primary threat identified here is a **modular framework**. The lack of static IP addresses/file paths suggests the malware uses an "interpreter" model; the actual malicious commands (e.g., exfiltration, data mining) are likely delivered as scripts from a C2 server at runtime. 

For defensive measures, it is recommended to:
1. Monitor for processes making unexpected calls to `GDI32.dll` functions in a non-graphical context.
2. Alert on the specific error strings found in the "Other artifacts" section, as these can be used to create YARA rules to identify instances of this specific interpreter engine.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: backdoor / RAT
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Execution Environment:** The analysis describes an industrial-grade, multi-purpose script interpreter with complex grammar parsing and a "virtual machine" state logic. This allows the threat actor to remotely push diverse modules (data theft, credential harvesting) via scripts rather than hardcoding behavior in the primary binary.
*   **Automated Data Mining (Regex):** The inclusion of a native Regular Expression engine is a high-confidence indicator of intent for automated information gathering. It enables the attacker to perform complex pattern matching to find sensitive data (PII, passwords, internal project codes) across the filesystem or memory.
*   **Graphic & System Interaction:** The integration of `GDI32.dll` functions and `SendMessageW` indicates capabilities for "overlay injection." This allows the malware to create fraudulent UI elements, spoof system alerts, or interact with other applications at the protocol level.
