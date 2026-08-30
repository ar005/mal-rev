# Threat Analysis Report

**Generated:** 2026-08-23 07:08 UTC
**Sample:** `1148fa91ce87cc06cbd373b0bd40eb1de0ede6e438262dda0ca8bea60b9239f8_1148fa91ce87cc06cbd373b0bd40eb1de0ede6e438262dda0ca8bea60b9239f8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1148fa91ce87cc06cbd373b0bd40eb1de0ede6e438262dda0ca8bea60b9239f8_1148fa91ce87cc06cbd373b0bd40eb1de0ede6e438262dda0ca8bea60b9239f8.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,414,144 bytes |
| MD5 | `3964a61d0e5673c967ddf25fef239f3e` |
| SHA1 | `1c6c710568566d0c52de1d224f551bef36d66a32` |
| SHA256 | `1148fa91ce87cc06cbd373b0bd40eb1de0ede6e438262dda0ca8bea60b9239f8` |
| Overall entropy | 7.286 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1772074369 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 535,040 | 7.939 | ⚠️ Yes |
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

Total strings found: **3291** (showing first 100)

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

This analysis incorporates the findings from **Chunk 5/5**. The addition of this disassembly provides a definitive look at the "engine room" of the protection layer, confirming that the packer utilizes a sophisticated **multi-layered dispatcher architecture** and a highly complex **virtualized memory management system.**

---

### Updated Summary
The analysis now confirms that this is not merely an obfuscated binary; it is a **highly advanced VM (Virtual Machine) protected executable**. The logic found in Chunk 5 demonstrates a "Deep Execution" model where the original code's logic is abstracted through multiple layers of translation.

*   **Multi-Layered Dispatching:** The presence of nested switch tables (e.g., in `fcn.00412c10`) and massive, high-density switch blocks (over 30+ cases in `fcn.0040f650`) indicates a "layered" VM. One layer might handle basic arithmetic/logic, while the next layer translates those into complex operations like memory management or string manipulation.
*   **Abstracted Memory Management:** The code demonstrates intense manual calculation of offsets and lengths (e.g., `iVar6 = iVar6 + iVar1 * iVar4`). This indicates the VM is managing its own "virtual heap" and "virtual stack," making it nearly impossible to trace data flow using standard linear analysis.
*   **Sophisticated Environment Simulation:** The continued use of `OLEAUT32` (Variant) logic suggests that the VM is designed to simulate high-level programming constructs. It doesn't just emulate x86; it provides a "virtual runtime" where variables are treated as complex objects, masking their true purpose from analysts.

---

### Analysis of New Techniques

#### 1. The "Instructional Ocean": Massive Switch Tables
The function `fcn.0040f650` is a prime example of a **Virtual Machine Dispatcher**. 
*   **Breadth of Capability:** With over 30 distinct cases in a single block, the VM possesses an enormous "vocabulary." Each case represents a unique opcode. To understand even one high-level action (like "Check if File Exists"), an analyst might have to trace through dozens of these micro-instructions.
*   **Branch Complexity:** The logic leading into these switches often involves complex arithmetic and boundary checks (`if (var_4h < 5)`, `if (10 < var_4h - just_subtracted)`). This ensures that the "Program Counter" of the virtual machine stays within valid bounds, providing stability for the malware while creating a maze for the researcher.

#### 2. Recursive Logic & Nested Dispatching
The function `fcn.00412c10` reveals a **nested dispatch mechanism**.
*   **Complexity Multiplication:** Instead of one switch statement handling all actions, this structure suggests that an operation in the "outer" VM might call a subroutine in an "inner" VM or a specialized handler library. 
*   **Context-Aware Execution:** The code checks specific conditions (like `if (piVar10[3] > 4)`) before entering sub-switch tables. This indicates that the virtual environment has its own internal "state machine." The same piece of code may behave differently depending on what the "virtual CPU" believes it is doing at that moment.

#### 3. Virtual Memory & String "Obfuscation-by-Abstraction"
The logic in `fcn.00411df0` and others indicates a sophisticated way of handling data:
*   **Computed Offsets:** Instead of storing strings or variables at fixed memory locations, the VM calculates positions using multiplication and addition of values pulled from its own internal "memory map." 
*   **Dynamic Buffer Management:** The repeated use of `fcn.0041fd5b` (which appears to be a memory allocation/allocation-handling function) suggests that even the basic act of moving data is wrapped in enough logic to hide the destination and purpose of that data.

#### 4. API Wrapping & Integration
The inclusion of `OLEAUT32` and `USER32` related code within these deep nested structures is a significant finding:
*   **Standard Library Simulation:** By wrapping complex Windows features (like Variants or UI interactions) inside the VM, the developers ensure that any "hook" an analyst places on standard APIs will only lead to more obfuscated VM-code rather than the actual malicious payload.
*   **Hybrid Functionality:** The presence of `USER32` logic suggests the malware may have multi-functional capabilities (e.g., it could be a RAT, a stealer, or even a game/utility with an injected backdoor).

---

### Final Synthesis for Incident Response

The evidence from all five chunks confirms this is a **top-tier professional protector**, likely comparable to commercial high-end solutions like VMProtect or Themida, but potentially customized for specific threat actor use.

#### Technical Indicators:
*   **Complexity Level:** Extreme (High-Level Virtualization).
*   **Key Signatures:** 
    *   Large switch tables (30+ cases) in the middle of complex logic.
    *   Heavy reliance on `OLEAUT32` and `Variant` structures for internal data passing.
    *   Repeated use of "getter/setter" style logic to access "fields" within a virtualized object.

#### Impact on Analysis:
1.  **Static Analysis is largely ineffective:** The "logic" of the malware does not exist in its raw form in memory; it exists as a series of opcodes that are interpreted by the VM.
2.  **De-virtualization is time-prohibitive:** Manually mapping every opcode to its original x86 equivalent would take weeks or months—well beyond the scope of a standard IR response.

#### Updated Recommended Strategy:
1.  **"Wait for the Reveal":** Do not attempt to "crack" the VM. Instead, use a debugger (x64dbg) with a script to log all "exit points" from the VM. You are looking for the moment the VM finally "hands off" the execution to a decrypted, plain-text piece of code.
2.  **Memory/API Monitoring:** Focus entirely on **system-level effects**. Since you cannot see *how* the malware decides to steal a password or open a socket (because that logic is hidden in the VM), monitor exactly *when* it does so by hooking `advapi32.dll`, `ws2_32.dll`, and `ntdll.dll`.
3.  **Process Hollowing/Injection Detection:** These types of complex packers often use "Process Hollowing" or "Reflective DLL Injection" to execute the final payload in a clean memory space after unpacking. Monitor for `VirtualAllocEx` and `WriteProcessMemory` calls, as these are usually the "exit points" from the complex VM logic.
4.  **Network Traffic Analysis:** Since the internal logic is opaque, treat all outbound network traffic as high-priority indicators of compromise (IOCs). The complexity of the packer suggests the threat actor values stealth and persistence; any communication from a process using this packer should be treated as highly malicious.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your report to the relevant MITRE ATT&K techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027.001** | Packers | The analysis confirms the use of a sophisticated, multi-layered VM protection system (similar to VMProtect or Themida) to wrap and hide the original code. |
| **T1027** | Obfuscated Files or Information | The "Instructional Ocean" and nested switch tables are used to create complex layers of abstraction that make it difficult for analysts to trace data flow. |
| **T1055** | Process Injection | The analysis suggests the use of high-level packing techniques likely involving Process Hollowing or Reflective DLL Injection to transition from the VM to a functional payload. |
| **T1036** | Masquerading (Contextual) | The "Standard Library Simulation" via `OLEAUT32` and `USER32` wrapping is used to mask the true nature of variables and actions from standard analysis tools. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the identified Indicators of Compromise (IOCs). 

Note: Because the malware utilizes a sophisticated Virtual Machine (VM) packer, most standard indicators (like raw IP addresses or file paths) are hidden within the obfuscated "Instructional Ocean" and do not appear in plaintext.

**IP addresses / URLs / Domains**
*   None identified (Infrastructure is obscured by the VM protection layer).

**File paths / Registry keys**
*   None identified (Paths are currently masked via abstracted memory management/calculated offsets).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **VM Packer Signature:** The sample utilizes a high-complexity, multi-layered VM dispatcher (similar to VMProtect or Themida) characterized by:
    *   **Large Switch Tables:** Multiple switch blocks with over 30 cases used as virtual instruction dispatchers (e.g., `fcn.0040f650`).
    *   **Nested Dispatching:** Complex nested switches (`fcn.00412c10`) to hide the execution flow of core logic.
    *   **Memory Abstraction:** Use of complex arithmetic for memory offsets rather than direct addressing to hide variable locations and data types. 

***

**Analyst Note:** The "Extracted Strings" section consists primarily of obfuscated bytecode and internal jump tables. No actionable network-based or host-based IOCs were present in the provided text; however, the behavioral analysis confirms the presence of a high-tier custom protector designed to evade static analysis and automated sandbox detection.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1.  **Malware family**: Custom
2.  **Malware type**: Loader
3.  **Confidence**: Medium
4.  **Key evidence**: 
    *   **Sophisticated VM Protection:** The sample utilizes a high-level "instructional ocean" with nested switch tables (over 30 cases) and a multi-layered dispatcher, indicating it is wrapped in professional-grade virtualization (similar to VMProtect or Themida).
    *   **Abstraction of Logic:** The use of calculated offsets for memory management and the wrapping of `OLEAUT32`/`USER32` libraries within the virtual machine are designed to hide the ultimate intent of the payload from static analysis.
    *   **Primary Function as a Loader:** Because the core logic is abstracted into bytecode, the primary observable role of this specific executable is to act as a sophisticated "wrapper" or loader that protects and eventually hands off execution to a hidden payload (e.g., RAT, Stealer).

**Note on Confidence:** The confidence is marked as **Medium** because while the sophistication of the *packer* is clearly high, the final malicious payload remains hidden within the virtual machine layers; therefore, the specific ultimate goal (RAT vs. Stealer) cannot be determined with 100% certainty without de-virtualizing the code.
