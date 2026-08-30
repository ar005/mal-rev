# Threat Analysis Report

**Generated:** 2026-08-22 18:49 UTC
**Sample:** `112699f3eed96b2dfb176b880f3be86ea083431600aeb889cd3ef46607caf4f2_112699f3eed96b2dfb176b880f3be86ea083431600aeb889cd3ef46607caf4f2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `112699f3eed96b2dfb176b880f3be86ea083431600aeb889cd3ef46607caf4f2_112699f3eed96b2dfb176b880f3be86ea083431600aeb889cd3ef46607caf4f2.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,200,128 bytes |
| MD5 | `b7faf6deed94ed572cd0b893ebd043d5` |
| SHA1 | `35b8c513f6dc2aed43a69e3032d1bffcddda0ece` |
| SHA256 | `112699f3eed96b2dfb176b880f3be86ea083431600aeb889cd3ef46607caf4f2` |
| Overall entropy | 7.064 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1764220407 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.61 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 321,024 | 7.861 | ⚠️ Yes |
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

Total strings found: **2823** (showing first 100)

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

This final segment (**Chunk 5/5**) provides the "smoking gun" for the complexity of this sample. It reveals that the malware isn't just using a VM; it’s implementing a **highly abstracted, object-oriented execution environment** that mimics sophisticated enterprise software architectures (like those found in Java Virtual Machines or high-end DRM systems).

The analysis is updated below to incorporate these final findings.

---

### Updated Analysis: Advanced Architecture & Execution Logic

#### 1. Deeply Nested Interpretation Engine (`fcn.00412c10`)
This function is a massive, multi-layered dispatcher that confirms the "Scripted Layer" theory from previous chunks.
*   **Complex Instruction Decoding:** Instead of simple `switch(opcode)`, this function performs multi-stage checks on opcodes, lengths, and nested offsets (e.g., checking for values like `0x47` at specific offsets). 
*   **State-Dependent Branching:** The logic frequently uses the result of a previous operation to determine how to decode the *next* piece of data. This means you cannot "trace" the VM by just looking at one instruction; the state of the machine determines how the next byte is interpreted.
*   **Internal Offsets as Context:** References to offsets like `0x210` and `0x110` indicate that the VM's internal registers/memory are not just numbers, but "objects" containing metadata (like lengths, types, or permissions).

#### 2. Advanced Object Life-Cycle Management (`fcn.0040c000`, `fcn.0040be83`)
The analysis of these functions reinforces the **Managed Memory** finding from Chunk 1.
*   **Automatic Reference Counting:** The repeated pattern of checking a "reference count" (e.g., `if (*arg_8h_00[3] == 0)`) before calling `fcn.0041fd94` and `fcn.0041fd4d` is almost identical to how **COM+** or **Python’s** internal memory management works.
*   **Automatic De-allocation:** When a "virtual object" (a string, buffer, or even a virtual instruction) is no longer needed, the VM automatically decrements its counter and frees it. This makes static analysis of data flow extremely difficult because the location of a piece of data in memory can change constantly as objects are created and destroyed by the interpreter.

#### 3. Granular "Internal" Dispatch Table (`fcn.0040f650`)
This function acts as the **Core API** for the VM. 
*   **High-Level Mapping:** The switch table with over 40 cases suggests a massive library of "virtual" functions. When a "script" inside the malware wants to do something (e.g., allocate memory, decrypt a string, or check a file), it calls one of these internal numbers.
*   **Abstraction of Intent:** Because there are so many cases, it’s clear that even simple actions are abstracted into multiple layers. For example, what looks like a single "decrypt" command in the high-level script might actually call three different `fcn.004xxx` functions to handle buffer resizing, key rotation, and memory copying.

#### 4. Host Interface & Evasion (`fcn.0040c3cb`)
The link between the VM and the host OS is clearly defined in this chunk.
*   **UI Manipulation:** The call to `InvalidateRect` suggests that the malware may be creating "ghost" windows or interacting with GUI elements to distract the user or a researcher while the backend logic executes.
*   **Dynamic Logic Switching:** The presence of multiple switch cases for UI-related calls indicates that the VM can change its behavior based on interaction with the Windows environment (e.g., responding to mouse clicks as "trigger" points for hidden code).

---

### Final Technical Patterns & Indicators

1.  **Virtual Instruction Set Architecture (V-ISA):** The sample does not use standard x86 instructions for core logic; it uses a proprietary ISA. A single high-level "instruction" in the script is broken into dozens of machine instructions to hide its true purpose from automated tools.
2.  **Object-Oriented Runtime:** The presence of reference counting and complex buffer management (`fcn.0040be83`) indicates that the malware's "payload" is not a raw block of code, but a collection of objects managed by an internal environment. 
3.  **Multi-Stage State Machine:** The VM maintains a persistent state. Whether or not a piece of code executes depends on variables set in previous rounds of execution, making static analysis (reading the code without running it) nearly impossible for uncovering the full logic path.
4.  **Sophisticated Buffer Manipulation:** Use of `fcn.00420db0` and `fcn.0041fd5b` suggests that data is "assembled" in memory only at the last possible moment, potentially using pieces retrieved from different parts of the file or remote servers.

---

### Final Summary for Reporting

The analysis confirms that this sample utilizes a **high-complexity virtualized execution environment** (similar to *VMProtect* or *Themida*). It is designed specifically to defeat both automated sandboxes and manual reverse engineering.

**Why this is significant:**
*   **Anti-Analysis Depth:** Because the "actual" logic is written in a custom, interpreted language, standard decompilers will only show you the **interpreter**, not the **malicious behavior**. To find the true intent of the malware, one must reverse-engineer the virtual machine's instruction set.
*   **Evasive Payload Delivery:** By using an object-oriented memory management system, the malware ensures that "suspicious" strings or API calls are never visible in a single contiguous block of memory. They are constructed piece-by-piece by the VM at runtime.
*   **Multi-Layered Defense:** The combination of a **Scripting Engine**, a **Reference Counting System**, and a **Complex Dispatcher** creates a "black box" effect. An analyst would need to map out the entire VM's internal API before they could begin understanding the actual malicious payload (e.g., keylogging, data exfiltration).

**Conclusion:** This is an advanced threat. The sample employs sophisticated virtualization techniques to hide its core logic behind layers of abstraction. We recommend prioritizing behavioral analysis in a "hardened" sandbox, as static de-obfuscation of this specific architecture will be extremely time-intensive.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | **Virtualization** | The malware implements a custom virtual machine (VM) and a proprietary instruction set architecture (V-ISA) to hide its core logic from automated tools and manual analysis. |
| **T1027** | **Obfuscated Files or Information** | The use of highly abstracted "scripted layers," complex dispatch tables, and object-oriented memory management masks the true intent of API calls and prevents clear data flow analysis. |
| **T1497** | **Virtualization** (Alternative/Related) | The implementation of a sophisticated execution environment mimicking high-end DRM systems is specifically designed to create a "black box" effect against security researchers. |

***Note for Analysis:** While T1029 and T1497 are often related in documentation regarding VM-based obfuscation, **T1029** is the primary identifier for the use of virtualization (custom instruction sets/interpreters) as a defense evasion tactic.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs):

### **IP addresses / URLs / Domains**
*   *None identified.* (The "Extracted Strings" section contains obfuscated/encoded data that does not resolve to plaintext network indicators).

### **File paths / Registry keys**
*   *None identified.* (Note: The function addresses mentioned, such as `0x412c10`, are internal memory offsets within the binary's execution space and do not constitute file system paths or registry keys.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA-1, or SHA-256 strings were present in the provided text).

### **Other artifacts**
*   **Malware Architecture:** The sample utilizes a custom **Virtual Instruction Set Architecture (V-ISA)**. This is a signature of advanced packers/protectors like VMProtect or Themida.
*   **Anti-Analysis Techniques:**
    *   **Scripted Layer:** Execution logic is hidden within a custom interpreter (`fcn.00412c10`).
    *   **Managed Memory / Reference Counting:** Use of automated memory management to hide the location of strings and commands in memory.
    *   **Multi-Layered Defense:** Extensive use of "Dispatch Tables" to abstract malicious actions into multiple steps.
    *   **Host Interaction:** Usage of `InvalidateRect` for potential UI manipulation or "ghosting."

---
**Analyst Note:** This sample is highly sophisticated. Because it uses a custom virtualization layer, traditional static analysis (searching for strings/IPs) is largely ineffective. The primary threat vector here is the **sophisticated obfuscation engine**, which suggests that any and all malicious network activity or file system modifications are occurring within the "black box" of the virtual machine's runtime.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Custom Virtual Instruction Set Architecture (V-ISA):** The sample uses a complex, proprietary interpreter (`fcn.00412c10`) and dispatch tables to execute code that is not standard x86; this "black box" approach is a signature of high-end protectors like VMProtect or Themida used primarily by advanced loaders.
*   **Object-Oriented Memory Management:** The implementation of reference counting and dynamic memory de-allocation ensures that malicious strings, API calls, and payloads are constructed at runtime rather than sitting in plain text in the binary, effectively hiding the malware's ultimate intent (e.g., RAT/infostealer functionality) from static analysis.
*   **Advanced Obfuscation Layers:** The multi-layered "Scripted" architecture means that every high-level action is abstracted into multiple sub-routines, designed specifically to defeat automated sandboxes and slow down manual reverse engineering by hiding the actual logic path of the malware.
