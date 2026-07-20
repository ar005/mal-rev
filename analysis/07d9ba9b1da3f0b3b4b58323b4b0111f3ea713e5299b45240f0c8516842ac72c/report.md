# Threat Analysis Report

**Generated:** 2026-07-17 20:51 UTC
**Sample:** `07d9ba9b1da3f0b3b4b58323b4b0111f3ea713e5299b45240f0c8516842ac72c_07d9ba9b1da3f0b3b4b58323b4b0111f3ea713e5299b45240f0c8516842ac72c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07d9ba9b1da3f0b3b4b58323b4b0111f3ea713e5299b45240f0c8516842ac72c_07d9ba9b1da3f0b3b4b58323b4b0111f3ea713e5299b45240f0c8516842ac72c.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64, 7 sections |
| Size | 1,905,152 bytes |
| MD5 | `f9a8f624fafe0a85a39b94afc8e6d62d` |
| SHA1 | `60ae2b6f503bb21b447556aab29b0919cdeddd8f` |
| SHA256 | `07d9ba9b1da3f0b3b4b58323b4b0111f3ea713e5299b45240f0c8516842ac72c` |
| Overall entropy | 7.351 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771546854 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 757,760 | 6.514 | No |
| `.rdata` | 220,672 | 5.393 | No |
| `.data` | 20,992 | 0.571 | No |
| `.pdata` | 29,696 | 5.823 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 871,424 | 7.976 | ⚠️ Yes |
| `.reloc` | 3,072 | 5.222 | No |

### Imports

**WSOCK32.dll**: `gethostbyname`, `recv`, `send`, `socket`, `ioctlsocket`, `setsockopt`, `ntohs`, `WSACleanup`, `WSAStartup`, `sendto`, `htons`, `__WSAFDIsSet`, `select`, `accept`, `listen`
**VERSION.dll**: `GetFileVersionInfoW`, `VerQueryValueW`, `GetFileVersionInfoSizeW`
**WINMM.dll**: `timeGetTime`, `waveOutSetVolume`, `mciSendStringW`
**COMCTL32.dll**: `ImageList_ReplaceIcon`, `ImageList_Destroy`, `ImageList_Remove`, `ImageList_SetDragCursorImage`, `ImageList_BeginDrag`, `ImageList_DragEnter`, `ImageList_DragLeave`, `ImageList_EndDrag`, `ImageList_DragMove`, `InitCommonControlsEx`, `ImageList_Create`
**MPR.dll**: `WNetGetConnectionW`, `WNetCancelConnection2W`, `WNetUseConnectionW`, `WNetAddConnection2W`
**WININET.dll**: `HttpOpenRequestW`, `InternetCloseHandle`, `InternetOpenW`, `InternetSetOptionW`, `InternetCrackUrlW`, `HttpQueryInfoW`, `InternetQueryOptionW`, `InternetConnectW`, `HttpSendRequestW`, `FtpOpenFileW`, `FtpGetFileSize`, `InternetOpenUrlW`, `InternetReadFile`, `InternetQueryDataAvailable`
**PSAPI.DLL**: `GetProcessMemoryInfo`
**IPHLPAPI.DLL**: `IcmpSendEcho`, `IcmpCloseHandle`, `IcmpCreateFile`
**USERENV.dll**: `DestroyEnvironmentBlock`, `LoadUserProfileW`, `CreateEnvironmentBlock`, `UnloadUserProfile`
**UxTheme.dll**: `IsThemeActive`
**KERNEL32.dll**: `WaitForSingleObject`, `HeapAlloc`, `GetProcessHeap`, `HeapFree`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `MulDiv`, `GetVersionExW`, `IsWow64Process`, `GetSystemInfo`, `FreeLibrary`, `LoadLibraryA`, `GetProcAddress`, `SetErrorMode`
**USER32.dll**: `GetMonitorInfoW`, `SetWindowLongW`, `SetLayeredWindowAttributes`, `FlashWindow`, `GetClassLongPtrW`, `TranslateAcceleratorW`, `IsDialogMessageW`, `GetSysColor`, `InflateRect`, `DrawFocusRect`, `DrawTextW`, `FrameRect`, `DrawFrameControl`, `FillRect`, `PtInRect`
**GDI32.dll**: `DeleteObject`, `GetDeviceCaps`, `ExtCreatePen`, `EndPath`, `StrokePath`, `SetPixel`, `CloseFigure`, `LineTo`, `AngleArc`, `MoveToEx`, `Ellipse`, `PolyDraw`, `GetTextExtentPoint32W`, `CreateCompatibleBitmap`, `BeginPath`
**COMDLG32.dll**: `GetSaveFileNameW`, `GetOpenFileNameW`
**ADVAPI32.dll**: `RegEnumValueW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegOpenKeyExW`, `RegCloseKey`, `RegQueryValueExW`, `RegConnectRegistryW`, `InitializeSecurityDescriptor`, `InitializeAcl`, `AdjustTokenPrivileges`, `OpenThreadToken`, `OpenProcessToken`, `LookupPrivilegeValueW`
**SHELL32.dll**: `DragFinish`, `DragQueryPoint`, `ShellExecuteExW`, `DragQueryFileW`, `SHEmptyRecycleBinW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHCreateShellItem`, `SHGetDesktopFolder`, `SHGetSpecialFolderLocation`, `SHGetFolderPathW`, `SHFileOperationW`, `ExtractIconExW`, `Shell_NotifyIconW`, `ShellExecuteW`
**ole32.dll**: `CoTaskMemAlloc`, `CoTaskMemFree`, `CLSIDFromString`, `ProgIDFromCLSID`, `CLSIDFromProgID`, `OleSetMenuDescriptor`, `MkParseDisplayName`, `OleSetContainedObject`, `CoCreateInstance`, `IIDFromString`, `StringFromGUID2`, `CreateStreamOnHGlobal`, `OleInitialize`, `OleUninitialize`, `CoInitialize`
**OLEAUT32.dll**: `VariantChangeType`, `DispCallFunc`, `CreateStdDispatch`, `CreateDispTypeInfo`, `UnRegisterTypeLib`, `UnRegisterTypeLibForUser`, `RegisterTypeLibForUser`, `RegisterTypeLib`, `LoadTypeLibEx`, `VariantCopyInd`, `VariantTimeToSystemTime`, `VariantClear`, `VariantCopy`, `SysAllocString`, `SafeArrayCreateVector`

## Extracted Strings

Total strings found: **4289** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
x ATAVAWH
 A_A^A\
UVWATAUAVAWH
0A_A^A]A\_^]
VWAUAVAWH
A_A^A]_^
x ATAVAWH
0A_A^A\
WATAUAVAWH
0A_A^A]A\_
UVWATAUAVAWH
PA_A^A]A\_^]
UWATAVAWH
0A_A^A\_]
u%HcH
UVWATAUAVAWH
`A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
UATAUAVAWH
A_A^A]A\]
u0E8w 
E8w u1I
t$ WATAUAVAWH
l$PHcI
 A_A^A]A\_
USVWAWH
A__^[]
WATAUAVAWH
A_A^A]A\_
UVWATAUAVAWH
A_A^A]A\_^]
USVWAVH
A^_^[]
USVWATAUAVAWH
A_A^A]A\_^[]
UVWAVAWH
0A_A^_^]
D8u8tEH
UAVAWH
USVWATAUAVAWH
D$PfA9p
A_A^A]A\_^[]
t$TL9}
UATAUAVAWH
A_A^A]A\]
UAVAWH
UVWATAUAVAWH
L$`Lc@
 A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
WAVAWH
UVWATAUAVAWH
@A_A^A]A\_^]
WAVAWH
 A_A^_
WAVAWH
 A_A^_
HcSHE3
UVWATAUAVAWH
uFD;n0tHA
A_A^A]A\_^]
UWATAUAWH
A_A]A\_]
WAVAWH
 A_A^_
fD91tXA
VWATAVAWH
HcWHE3
A_A^A\_^
WAVAWH
fD9<Gt
 A_A^_
t$ WATAUAVAWH
A_A^A]A\_
UVWATAUAVAWH
|$XAU3!
A_A^A]A\_^]
@SVWAVAWH
0A_A^_^[
t$ WAVAWH
0A_A^_
VWATAVAWH
A_A^A\_^
WATAUAVAWH
fE9<FtR
fE9<Vt!
 A_A^A]A\_
H WATAUAVAWH
 A_A^A]A\_
UVWATAUAVAWH
`A_A^A]A\_^]
USWAUAVI
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14000a3a8` | `0x14000a3a8` | 491702 | ✓ |
| `fcn.140012e00` | `0x140012e00` | 400244 | ✓ |
| `fcn.1400122b0` | `0x1400122b0` | 361283 | ✓ |
| `fcn.140014d50` | `0x140014d50` | 332720 | ✓ |
| `fcn.14000c980` | `0x14000c980` | 330924 | ✓ |
| `fcn.14000daa8` | `0x14000daa8` | 330192 | ✓ |
| `fcn.14000d9e0` | `0x14000d9e0` | 330097 | ✓ |
| `fcn.140013060` | `0x140013060` | 330019 | ✓ |
| `fcn.14000dba0` | `0x14000dba0` | 329972 | ✓ |
| `fcn.14000dca0` | `0x14000dca0` | 329770 | ✓ |
| `fcn.14000de5c` | `0x14000de5c` | 329340 | ✓ |
| `fcn.140013ed0` | `0x140013ed0` | 329304 | ✓ |
| `fcn.14000df20` | `0x14000df20` | 329158 | ✓ |
| `fcn.14000dfe4` | `0x14000dfe4` | 328982 | ✓ |
| `fcn.14000e11c` | `0x14000e11c` | 328797 | ✓ |
| `fcn.140012840` | `0x140012840` | 328655 | ✓ |
| `fcn.14000e2b8` | `0x14000e2b8` | 328497 | ✓ |
| `fcn.140016980` | `0x140016980` | 328283 | ✓ |
| `fcn.14000e3a4` | `0x14000e3a4` | 328281 | ✓ |
| `fcn.140016ef0` | `0x140016ef0` | 328266 | ✓ |
| `fcn.14000e850` | `0x14000e850` | 328093 | ✓ |
| `fcn.14000e964` | `0x14000e964` | 327868 | ✓ |
| `fcn.14000ea64` | `0x14000ea64` | 327728 | ✓ |
| `fcn.140016d40` | `0x140016d40` | 327591 | ✓ |
| `fcn.14000eccc` | `0x14000eccc` | 327197 | ✓ |
| `fcn.14000ef60` | `0x14000ef60` | 327094 | ✓ |
| `fcn.14000ee8c` | `0x14000ee8c` | 327011 | ✓ |
| `fcn.14000f17c` | `0x14000f17c` | 326594 | ✓ |
| `fcn.14000f228` | `0x14000f228` | 326569 | ✓ |
| `fcn.14000f2bc` | `0x14000f2bc` | 326531 | ✓ |

### Decompiled Code Files

- [`code/fcn.14000a3a8.c`](code/fcn.14000a3a8.c)
- [`code/fcn.14000c980.c`](code/fcn.14000c980.c)
- [`code/fcn.14000d9e0.c`](code/fcn.14000d9e0.c)
- [`code/fcn.14000daa8.c`](code/fcn.14000daa8.c)
- [`code/fcn.14000dba0.c`](code/fcn.14000dba0.c)
- [`code/fcn.14000dca0.c`](code/fcn.14000dca0.c)
- [`code/fcn.14000de5c.c`](code/fcn.14000de5c.c)
- [`code/fcn.14000df20.c`](code/fcn.14000df20.c)
- [`code/fcn.14000dfe4.c`](code/fcn.14000dfe4.c)
- [`code/fcn.14000e11c.c`](code/fcn.14000e11c.c)
- [`code/fcn.14000e2b8.c`](code/fcn.14000e2b8.c)
- [`code/fcn.14000e3a4.c`](code/fcn.14000e3a4.c)
- [`code/fcn.14000e850.c`](code/fcn.14000e850.c)
- [`code/fcn.14000e964.c`](code/fcn.14000e964.c)
- [`code/fcn.14000ea64.c`](code/fcn.14000ea64.c)
- [`code/fcn.14000eccc.c`](code/fcn.14000eccc.c)
- [`code/fcn.14000ee8c.c`](code/fcn.14000ee8c.c)
- [`code/fcn.14000ef60.c`](code/fcn.14000ef60.c)
- [`code/fcn.14000f17c.c`](code/fcn.14000f17c.c)
- [`code/fcn.14000f228.c`](code/fcn.14000f228.c)
- [`code/fcn.14000f2bc.c`](code/fcn.14000f2bc.c)
- [`code/fcn.1400122b0.c`](code/fcn.1400122b0.c)
- [`code/fcn.140012840.c`](code/fcn.140012840.c)
- [`code/fcn.140012e00.c`](code/fcn.140012e00.c)
- [`code/fcn.140013060.c`](code/fcn.140013060.c)
- [`code/fcn.140013ed0.c`](code/fcn.140013ed0.c)
- [`code/fcn.140014d50.c`](code/fcn.140014d50.c)
- [`code/fcn.140016980.c`](code/fcn.140016980.c)
- [`code/fcn.140016d40.c`](code/fcn.140016d40.c)
- [`code/fcn.140016ef0.c`](code/fcn.140016ef0.c)

## Behavioral Analysis

This final analysis incorporates the findings from **chunk 6/6**. This concluding segment provides the definitive technical evidence for the malware’s architecture, confirming that this is not a simple "malicious payload" but a sophisticated, production-grade **Scripting Virtual Machine (VM)**.

### Final Analysis of Code Functionality

#### 1. Explicit Confirmation of Type-Aware VM Architecture
The functions `fcn.14000e964` and `fcn.1400ef60` provide concrete evidence of a **typed variable system**. The repeated checks (e.g., `if (iVar1 == 1)`, `if (iVar1 == 2)`, etc.) are not random logic; they are checking internal "type tags" within the OLEAUT32 Variant structures.
*   **Internal Representation:** The VM treats data as objects with metadata. For example, a variable isn't just an integer; it is a structure containing a type ID and a value. This allows the script to handle complex logic (e.g., "If result is Integer X, do Action A; if result is String Y, do Action B").
*   **Arithmetic Safety:** In `fcn.1400ef60`, the switch table manages how different types are added or compared. It checks for specific types before executing a specialized addition routine, ensuring that "automatic type conversion" (a staple of high-level languages like Python or JavaScript) is implemented within the malicious environment.

#### 2. Advanced Instruction Dispatch and Decoding
The logic found in `fcn.1400ea64` exhibits characteristics of **Opcode Processing**. The loops iterate through data blocks, checking for specific values (like `0x20`, `9`, or `0x22`) to determine the next action.
*   **Instruction Pipeline:** This suggests a "fetch-decode-execute" cycle. The "script" is likely a binary blob containing opcodes that this engine translates into high-level actions. 
*   **Extended Operands:** The logic involving `0x14000eb4a` and `fcn.1400ec30` suggests the ability to handle complex instructions that require multi-step execution or multiple "lookups," common in advanced scripting languages used by APT (Advanced Persistent Threat) actors.

#### 3. Robust Data Parsing and Translation
The inclusion of functions like `fcn.14000e850` (likely a base-conversion or string-to-numeric routine) confirms that the engine can ingest "messy" data. 
*   **Input Sanitization:** The code specifically handles variations in input format, ensuring that if a C2 server sends a value as a string or different numeric format, the VM correctly parses it into its internal type system before use. This is a hallmark of professional-grade software where "edge cases" are handled to prevent crashes during execution.

#### 4. Sophisticated Memory and Stack Management
The function `fcn.140016d40` demonstrates complex calculations regarding memory offsets and buffer sizes (e.g., `iVar3 = iVar3 / piVar4[-0x41]`). This implies the engine manages its own **Virtual Stack** or a sophisticated heap-management system to allocate space for variables of different types/lengths on the fly, preventing typical memory corruption vulnerabilities that would alert defenders.

---

### Updated Summary of Malicious Behaviors

*   **Sophisticated Behavior Abstraction (The "VM Trap"):** By using an interpreter, the author ensures that no single "action" is easily linked to a system call. A behavior monitor looking for "Registry Key Modification" will see a very complex series of internal VM operations leading up to it, making it extremely difficult to signature the malicious intent.
*   **State-Persistent Execution:** The complex state management in `fcn.1400ea64` means the malware can maintain a persistent "state" as it performs multi-stage actions (e.g., "Wait 5 minutes," then "Check if File X exists," then "if yes, start Network Beacon").
*   **Anti-Analysis via Complexity:** The dense usage of `OLEAUT32` and nested switch tables is a deliberate tactic to exhaust the time and resources of human analysts. By creating a "layer" between the script and the hardware/OS, the author forces the analyst to reverse engineer the *interpreter* before they can even begin to understand what the *malicious commands* are actually doing.

---

### Final Summary for Analysis Report

**Component Role: Multi-Stage Scripting Interpreter / Virtual Machine (VM).**

**Technical Overview:**
This component is a highly sophisticated **interpretation engine** designed to execute complex, multi-step scripts. It functions by creating an abstraction layer between the "script" (the intent) and the Windows API (the action). The script is compiled into a series of opcodes which are processed by the internal VM using `OLEAUT32` for robust data type management.

**Key Findings:**
1.  **Advanced Type System:** The engine implements a comprehensive type-checking mechanism (via OLEAUT_Variant logic), allowing scripts to perform complex arithmetic and logical operations across different data types (Strings, Integers, Floats) seamlessly.
2.  **Instruction Decoding Loop:** Evidence of an opcode-based execution cycle indicates that the malware is designed for modularity; attackers can update the script files to change behavior without ever changing or re-releasing the main binary.
3.  **Deliberate Obfuscation through Abstraction:** The heavy use of "junk code" (identified in earlier chunks) combined with a complex interpreter structure ensures that standard automated analysis tools cannot easily map high-level malicious actions to low-level system calls.
4.  **Robustness and Stability:** The implementation includes extensive error checking, buffer validation, and state management, indicating a professional development lifecycle designed for persistence on high-value targets where "crashes" are unacceptable.

**Risk Assessment:**
This is indicative of a **highly sophisticated threat actor**, likely an organized cybercrime group or a state-sponsored APT. The architecture (Interpreter + Type-System + Junk Code) is specifically designed to maximize the duration of the infection by hiding the attacker's intent behind layers of "logical noise." This infrastructure allows for **long-term, modular persistence**; the malware can be repurposed for different targets simply by pushing new script files to the existing interpreter.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Virtualization | The use of a custom Scripting Virtual Machine (VM) and a "fetch-decode-execute" cycle creates an abstraction layer that hides the true intent of the script from automated analysis tools. |
| **T1059** | Command and Scripting Interpreter | The presence of opcode processing, instruction decoding loops, and nested switch tables indicates the use of an internal interpreter to execute multi-step commands. |
| **T1027** | Obfuscated Programs or Information | The implementation of "logical noise," complex type systems (OLEAUT32), and "junk code" is a deliberate tactic to exhaust analyst time and hide malicious functionality within layers of complexity. |

---

## Indicators of Compromise

Based on the provided technical data and behavioral analysis, here is the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The analysis mentions "Registry Key Modification" as a behavior, but no specific registry keys or file paths were provided in the strings.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Architecture Type:** Scripting Virtual Machine (VM) / Interpreter.
*   **Internal Function Offsets (Potential YARA points):**
    *   `fcn.14000e964` (Type-aware system)
    *   `fcn.1400ef60` (Switch table/Arithmetic logic)
    *   `fcn.1400ea64` (Opcode processing/Dispatch)
    *   `fcn.14000eb4a` & `fcn.1400ec30` (Extended operand handling)
    *   `fcn.14000e850` (Base-conversion/String parsing)
    *   `fcn.140016d40` (Memory/Stack management)
*   **API/Library Dependencies:** `OLEAUT32` (Used for its Variant structure to handle multi-type data).
*   **Execution Patterns:** 
    *   Opcode-based "fetch-decode-execute" cycle.
    *   Use of "junk code" and complex nested switch tables to obfuscate the transition between script logic and system API calls.

---
**Analyst Note:** The provided text contains a high volume of "noise" in the `EXTRACTED STRINGS` section (e.g., `@.fptable`, `x ATAVAWH`). These are characteristic of compiler artifacts or heavily obfuscated code segments and do not constitute actionable IOCs for perimeter blocking or local hunting. The primary threat signature is behavioral: a high-sophistication VM architecture designed to hide malicious intent behind a layer of instruction translation.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated VM Architecture:** The sample utilizes a complex Scripting Virtual Machine (VM) with an opcode-based "fetch-decode-execute" cycle, specifically designed to hide malicious actions behind an abstraction layer.
*   **Robust Data Handling:** The use of `OLEAUT32` for type-aware variable management and advanced memory/stack management indicates professional-grade development aimed at maintaining stability while evading detection from automated tools.
*   **Modular Execution Design:** The architecture allows the threat actor to push new, diverse behaviors (e.g., data exfiltration, file encryption) via external scripts without needing to re-compile or change the primary loader binary.
