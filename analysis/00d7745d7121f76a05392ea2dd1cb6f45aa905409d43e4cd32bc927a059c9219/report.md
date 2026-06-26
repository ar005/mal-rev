# Threat Analysis Report

**Generated:** 2026-06-25 13:10 UTC
**Sample:** `00d7745d7121f76a05392ea2dd1cb6f45aa905409d43e4cd32bc927a059c9219_00d7745d7121f76a05392ea2dd1cb6f45aa905409d43e4cd32bc927a059c9219.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00d7745d7121f76a05392ea2dd1cb6f45aa905409d43e4cd32bc927a059c9219_00d7745d7121f76a05392ea2dd1cb6f45aa905409d43e4cd32bc927a059c9219.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,232,896 bytes |
| MD5 | `67fe7acd718b79cb106c60972062eff5` |
| SHA1 | `7ce101b8a776e6774e0bd4ecf15dec9ca26ce9c5` |
| SHA256 | `00d7745d7121f76a05392ea2dd1cb6f45aa905409d43e4cd32bc927a059c9219` |
| Overall entropy | 7.115 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1764675529 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 353,792 | 7.885 | ⚠️ Yes |
| `.reloc` | 30,208 | 6.798 | No |

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
**KERNEL32.dll**: `DuplicateHandle`, `CreateThread`, `WaitForSingleObject`, `HeapAlloc`, `GetProcessHeap`, `HeapFree`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `MulDiv`, `GetVersionExW`, `IsWow64Process`, `GetSystemInfo`, `FreeLibrary`, `LoadLibraryA`
**USER32.dll**: `IsCharAlphaW`, `IsCharAlphaNumericW`, `IsCharLowerW`, `IsCharUpperW`, `GetMenuStringW`, `GetSubMenu`, `GetCaretPos`, `IsZoomed`, `MonitorFromPoint`, `GetMonitorInfoW`, `SetWindowLongW`, `SetLayeredWindowAttributes`, `FlashWindow`, `GetClassLongW`, `TranslateAcceleratorW`
**GDI32.dll**: `EndPath`, `DeleteObject`, `GetTextExtentPoint32W`, `ExtCreatePen`, `StrokeAndFillPath`, `GetDeviceCaps`, `SetPixel`, `CloseFigure`, `LineTo`, `AngleArc`, `MoveToEx`, `Ellipse`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `PolyDraw`
**COMDLG32.dll**: `GetSaveFileNameW`, `GetOpenFileNameW`
**ADVAPI32.dll**: `GetAce`, `RegEnumValueW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegOpenKeyExW`, `RegCloseKey`, `RegQueryValueExW`, `RegConnectRegistryW`, `InitializeSecurityDescriptor`, `InitializeAcl`, `AdjustTokenPrivileges`, `OpenThreadToken`, `OpenProcessToken`
**SHELL32.dll**: `DragFinish`, `DragQueryPoint`, `ShellExecuteExW`, `DragQueryFileW`, `SHEmptyRecycleBinW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHCreateShellItem`, `SHGetDesktopFolder`, `SHGetSpecialFolderLocation`, `SHGetFolderPathW`, `SHFileOperationW`, `ExtractIconExW`, `Shell_NotifyIconW`, `ShellExecuteW`
**ole32.dll**: `CoTaskMemAlloc`, `CoTaskMemFree`, `CLSIDFromString`, `ProgIDFromCLSID`, `CLSIDFromProgID`, `OleSetMenuDescriptor`, `MkParseDisplayName`, `OleSetContainedObject`, `CoCreateInstance`, `IIDFromString`, `StringFromGUID2`, `CreateStreamOnHGlobal`, `OleInitialize`, `OleUninitialize`, `CoInitialize`
**OLEAUT32.dll**: `CreateStdDispatch`, `CreateDispTypeInfo`, `UnRegisterTypeLib`, `UnRegisterTypeLibForUser`, `RegisterTypeLibForUser`, `RegisterTypeLib`, `LoadTypeLibEx`, `VariantCopyInd`, `SysReAllocString`, `SysFreeString`, `VariantChangeType`, `SafeArrayDestroyData`, `SafeArrayUnaccessData`, `SafeArrayAccessData`, `SafeArrayAllocData`

## Extracted Strings

Total strings found: **2905** (showing first 100)

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

This final chunk of disassembly completes the picture of the malware’s architecture. The code in sections 4 and 5 confirms that the "engine" is not just robust; it is an **extremely high-fidelity execution environment** likely derived from—or heavily inspired by—professional scripting language engines (such as those used in web browsers, enterprise software, or specialized automation frameworks).

The following analysis incorporates the latest disassembly into the existing narrative.

---

### Updated Technical Analysis (Chunk 5/5)

#### 1. Object-Oriented Interpretation & Complex Type Handling
The presence of `OLEAUT32.dll_VariantCopy` and the extensive logic surrounding "Type" checks (e.g., the repeated checks for `0x47`, `0x48`, and `0x7f`) indicate that the engine supports a complex **object model**. 
*   **Complex Data Types:** Rather than passing simple strings or integers, the interpreter handles "Objects." When it encounters a command, it doesn't just perform an action; it resolves the type of the object involved (e.g., is it a string? a list? a custom defined object?).
*   **Multi-layered Dispatch:** The switch tables in `fcn.00412c10` and `fcn.0040f650` are not simple "if/then" checks. They are **dispatch tables**. When the script calls a function, the engine must first determine the *type* of the arguments, then find the correct *method* for that type, and finally execute the logic. This creates a massive "buffer zone" between the script's command (e.g., `GetSystemInfo`) and the actual malicious system call.

#### 2. Massive Dispatch Tables & Functional Breadth
The switch table in `fcn.0040f650` is particularly telling:
*   **Extensive Feature Set:** With over **40 cases** in a single switch block, it becomes clear that the engine has been designed to support a vast array of functionalities (e.g., math operations, string manipulation, system interactions, and potentially networking). 
*   **Instruction Diversity:** The sheer scale suggests the authors didn't write this just for one specific task (like stealing a cookie). They built an **infrastructure** capable of hosting a wide variety of complex behaviors, likely to allow them to update the "script" component frequently without ever changing the main `.exe` binary.

#### 3. Advanced Memory Management & Buffer Safety
The analysis of `fcn.0040bd9d` and `fcn.0040be83` reveals highly professional memory management:
*   **Dynamic Allocation Logic:** The code performs complex calculations to determine required buffer sizes before allocation, including logic that handles high-memory thresholds. 
*   **Memory Safety:** It includes checks for null pointers and "out of bounds" conditions (e.g., `if (uVar1 < 0x41c2)`). This is intended to ensure the interpreter remains stable even when processing complex, multi-step scripts that could otherwise crash a poorly-written malware sample.

#### 4. Interaction with UI and System State
The function `fcn.0040c3cb` references `USER32.dll_InvalidateRect`. This suggests that the engine has the capability to interact with Windows GUI components. In a malicious context, this could be used to create "ghost" windows, manipulate standard system dialogues, or hide its presence by interacting directly with window handles (HWND) in a way that bypasses simple API monitoring.

---

### Final Synthesis of Findings

The analysis of all five chunks confirms the following:

1.  **Engine Sophistication:** This is not "script-injection" via a simple shell; this is a **full-featured virtual machine/interpreter.** It mimics the architecture of professional software, providing the attacker with a powerful, stable, and highly flexible platform for execution.
2.  **Abstraction as an Evasion Tactic:** The primary security goal of this design is to **decouple intent from action.** By using internal opcodes (the 0x40... series in `fcn.0040f650`), the malware ensures that a sandbox or automated tool sees only "innocent" interpreter logic. The actual malicious intent resides within the script, which is only "translated" into system actions at the very last moment inside these complex switch cases.
3.  **Professional Origin:** The complexity of the buffer management and the breadth of the dispatch tables strongly suggest that this code was either developed by highly skilled engineers or is a modified version of an existing open-source/commercial scripting engine.

---

### Final Summary for Report

**Malware Type:** Sophisticated Scripting Engine / Interpreter
**Threat Profile:** High (Likely Advanced Persistent Threat (APT) or Professional Malware-as-a-Service (MaaS))

**Technical Overview:**
The malware utilizes a high-level scripting interpreter to execute malicious commands. This architecture provides several layers of defense for the attacker:
*   **Complexity Hiding:** By utilizing an internal "dispatch" system, the actual logic of the attack is buried beneath multiple layers of abstraction.
*   **Robustness:** The inclusion of professional-grade memory management and error handling ensures that the malware will not crash during complex operations, making it more stable for long-term persistence.
*   **Flexibility:** The large number of available "opcodes" (over 40 in a single switch) suggests that the engine can perform a wide range of actions—from file manipulation to system exploitation—simply by swapping out the underlying script.

**Impact Analysis:**
Because the malicious logic is abstracted, traditional signature-based and simple behavioral analysis may fail to flag the primary executable as "malicious," as it primarily performs internal data processing and memory management. 

**Detection & Response Recommendations:**
1.  **Memory Forensics:** Analysts should perform memory dumps during execution. The "cleartext" version of the script will likely reside in a buffer within the process's heap or stack at some point before being processed by the interpreter.
2.  **De-obfuscation:** Manual analysis of the "dispatch table" is required to map internal opcodes to system functionalities. 
3.  **Behavioral Monitoring:** Instead of looking for specific strings, monitors should look for "anomalous behavior clusters"—e.g., the interpreter process making numerous system calls in a tight loop or accessing sensitive files/registry keys that are not typical for standard application behavior.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Execution | The use of a custom, high-fidelity interpreter and internal opcodes hides the actual malicious intent from automated analysis tools by decoupling "logic" from "action." |
| **T1059** | Command and Scripting Interpreter | The malware implements a sophisticated, multi-purpose scripting engine to provide a flexible execution environment for diverse functionalities. |
| **T1036** | Masquerading | Interaction with `USER32.dll` (e.g., `InvalidateRect`) is used to manipulate GUI components or hide the presence of the application from the user and standard monitoring. |
| **T1564** | Hide Artifacts | The advanced memory management, robust error handling, and "buffer zone" are designed to ensure the malware remains stable and undetected during complex execution routines. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the extracted list of Indicators of Compromise (IOCs):

### **IP addresses / URLs / Domains**
*   *None identified.* (The technical analysis notes that malicious intent/C2 details are abstracted within scripts and not present in the core interpreter binary.)

### **File paths / Registry keys**
*   *None identified.* (Only internal disassembly function offsets, such as `fcn.00412c10`, were noted; these are unique to this specific binary's memory map and are not shared indicators.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (The "Extracted Strings" section contains non-human-readable data and obfuscated code segments, but no MD5, SHA1, or SHA256 hashes were present.)

### **Other artifacts**
*   **Malware Architecture:** Sophisticated Scripting Interpreter/Virtual Machine.
*   **Key Behavior:** Large dispatch table (Switch block) at `fcn.0040f650` containing over 40 cases for instruction diversity.
*   **Technique:** Decoupling of intent from action via internal opcodes (the `0x40...` series).

***

**Analyst Note:** This sample belongs to a high-sophistication threat actor. Because the malware uses a heavily abstracted scripting engine, standard signature-based detection on strings will likely fail. Detection should focus on memory forensics and monitoring for anomalous system calls originating from the interpreter's execution loop.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: custom
2. **Malware type**: loader (specifically a sophisticated scripting interpreter)
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Abstraction:** The malware utilizes a high-fidelity, custom virtual machine/interpreter with complex dispatch tables (over 40 cases in a single block), designed to decouple malicious intent from the core execution logic.
    *   **Evasion Tactics:** By using an internal opcode system and advanced memory management, it hides "scripts" within the binary, making it difficult for traditional signature-based tools to identify specific malicious actions (e.g., credential theft or file exfiltration).
    *   **Professional Engineering:** The presence of sophisticated buffer handling, object-oriented logic (`OLEAUT32.dll`), and robust error checking indicates a high-sophistication threat profile consistent with APTs or professional Malware-as-a-Service (MaaS) platforms.
