# Threat Analysis Report

**Generated:** 2026-07-02 21:29 UTC
**Sample:** `03cf3b904fa5ab697555ec0c6ee3c0cb6bbb42a01876e2d093bd78edc4cbe3f0_03cf3b904fa5ab697555ec0c6ee3c0cb6bbb42a01876e2d093bd78edc4cbe3f0.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `03cf3b904fa5ab697555ec0c6ee3c0cb6bbb42a01876e2d093bd78edc4cbe3f0_03cf3b904fa5ab697555ec0c6ee3c0cb6bbb42a01876e2d093bd78edc4cbe3f0.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,256,960 bytes |
| MD5 | `88aca4c9d81410e3f6df04aad1d8ec75` |
| SHA1 | `315e57d682ad745b64db3a2de9daed1801f982bf` |
| SHA256 | `03cf3b904fa5ab697555ec0c6ee3c0cb6bbb42a01876e2d093bd78edc4cbe3f0` |
| Overall entropy | 7.141 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769475546 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 377,856 | 7.895 | ⚠️ Yes |
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

Total strings found: **2932** (showing first 100)

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

This updated analysis incorporates the findings from **Chunk 5/5**, which provides the final piece of the puzzle regarding the malware's internal architecture. The inclusion of these functions solidifies the conclusion that this is a high-end, **Reflection-based Execution Environment**.

### Updated Summary of Findings

#### 1. Core Functionality and Purpose (Advanced Interpretation)
The analysis of Chunk 5 reveals that the "Scripting Engine" is not just a translation layer for COM; it is a **full-featured Virtual Machine (VM)** designed to provide **Instructional Indirection**.

*   **Polymorphic Command Mapping:** The large switch tables (e.g., `fcn.0040f650` with over 41 cases) act as a "Gateway." Instead of the malware calling a direct API like `ShellExecute`, it calls a generic function with an ID. The switch table then translates that ID into a specific action. This allows the attacker to change the behavior of the malware by simply updating the script (the data) without changing the binary (the code).
*   **Type-Aware Execution:** Functions like `fcn.00411df0` and `fcn.00412c10` show that the engine is aware of "Types." It doesn't just treat data as a blob; it identifies if a variable is a string, an integer, or a COM object, and then selects the appropriate handling logic (e.g., length checks, buffer allocations, or pointer offsets).
*   **Internal Logic Decoupling:** The repeated use of "wrapper" functions like `fcn.0041fd4d` and `fcn.0041fd94` suggests a very stable, polished architecture. These are likely used for error handling, memory cleanup, or state management after every script-driven action is performed.

#### 2. Suspicious and Malicious Behaviors
The logic in Chunk 5 highlights several advanced evasion and persistence techniques:

*   **Multi-Stage Dispatching:** A single "instruction" from a script might pass through three different layers of logic before hitting a Windows API. This makes it extremely difficult for automated sandboxes to map the full "execution tree" because only one path is revealed at a time.
*   **Dynamic Property Resolution:** The code handles complex property lookups (e.g., `0x4131f4`). This means the script can interact with any Windows property that a COM object supports, including registry keys, file system attributes, or network configurations.
*   **Environment Interaction via UI Components:** The presence of `USER32.dll_InvalidateRect` and related logic suggests the malware may have capabilities to manipulate GUI elements or windows, potentially for overlaying content or interacting with standard Windows notifications/dialogs in a way that mimics legitimate software.

#### 3. Technical Indicators & Patterns
| Feature | Observation | Analysis / Interpretation |
| :--- | :--- | :--- |
| **Extensive Switch Tables** | `fcn.0040f650` (41+ cases), `0x4562b3`, `0x4131f4`. | **"Complexity as Defense."** The volume of switch cases hides the true intent by scattering "malicious" actions across a vast sea of "benign-looking" logical transitions. |
| **COM/OLE Wrapper Hubs** | Frequent calls to `VariantCopy` and custom wrappers for COM objects. | Ensures that the malware interacts with Windows as a "trusted" application, leveraging legitimate system APIs rather than raw, suspicious low-level calls. |
| **Memory Isolation** | Complex calculations for buffer sizes (`0x40bd9d`) and offset adjustments. | Indicates a focus on stability; the malware is designed to run consistently on various versions of Windows without crashing during complex operations. |
| **Abstraction Layer** | Use of "Descriptor" patterns (e.g., `piVar10` being used as an object handler). | The code doesn't work with raw data; it works with "Descriptors." This means the script interacts with a virtual representation of the system, which is only converted to real actions at the very last moment. |

---

### Detailed Deep-Dive on Chunk 5 Highlights:

*   **The "Master Dispatcher" (`fcn.0040f650`):** This function is a textbook example of an **Interpreter Gateway**. Each case in this switch table likely represents one "Command" in the malware's language. Because there are over 40 cases, it suggests a massive capability list (e.g., file I/O, networking, registry manipulation, process injection, etc.).
*   **The Object Handler (`fcn.00412c10`):** This function is highly complex and appears to handle the **lifecycle of a COM object**. It ensures that when the script "grabs" a system resource (like a FileSystemObject), it is properly wrapped in a structure that the VM can understand, including error checking and memory management.
*   **Robust Memory Management:** The code contains logic for handling buffer overflows and ensuring that string operations stay within bounds. This level of polish is characteristic of **APT-level tools** or sophisticated **Ransomware/Trojans** where high reliability in the wild is paramount.

### Final Risk Assessment: **Critical / High-End Advanced Threat**
The analysis now confirms that this is not a simple piece of malware; it is a **sophisticated, scriptable framework.** 

By utilizing a custom VM to wrap COM/OLE operations, the attackers have achieved several goals:
1.  **Code Decoupling:** They can update the "features" of the malware by changing the remote script without recompiling the binary.
2.  **Signature Evasion:** Because the core logic is in the "script," standard signature-based detection has a very low chance of catching all possible behaviors.
3.  **Complexity as Defense:** The multi-layered switch tables and abstraction layers create a "maze" for reverse engineers, requiring significant time to map out every possible action the script can take.

### Recommendations for Further Investigation:
1.  **Map the Dispatcher:** Attempt to identify what each of the 40+ cases in `fcn.0040f650` does by tracing them at runtime with a debugger (x64dbg).
2.  **Identify the Script Payload:** Look for encrypted blobs or files on disk that contain the "instructions" passed to this VM. These are the true "brain" of the malware.
3.  **Monitor COM Traffic:** Use **SpyDog** or **Process Monitor** specifically looking for `ole32.dll` calls. Even if the script is hidden, the final execution *must* eventually call a standard Windows function to perform its task (e.g., creating a file).
4.  **Extract String Literals:** Search for any remaining hardcoded strings or IP addresses that may be used as fallbacks in the "Default" cases of the switch tables.

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Interpreted Code | The malware utilizes a "Scripting Engine" and a custom "Virtual Machine" (VM) to provide instruction indirection, allowing it to execute commands via an interpreted layer rather than direct execution. |
| **T1036** | Masquerading | The use of COM/OLE wrapper hubs allows the malware to interact with system components through legitimate APIs to appear as a "trusted" application. |
| **T1055** | Packer | The "Complexity as Defense" approach, utilizing extensive switch tables and multi-layer dispatching, is used to obfuscate the execution path and hinder manual reverse engineering. |

### Analyst Notes:
*   **T1027 (Interpreted Code):** This is the primary mechanism for the malware's core architecture. By using a VM to interpret a custom language, the attackers decouple the "logic" (the script) from the "engine" (the binary), making it significantly harder to signature or detect during static analysis.
*   **T1036 (Masquerading):** This specifically relates to the finding that the malware uses "wrapper functions" and standard COM objects. By wrapping suspicious actions in common Windows API calls, the malware attempts to blend in with legitimate system behavior.
*   **T1055 (Packer/Obfuscation):** While often associated with packers, this technique also encompasses the use of complex, layered logic (like the 40+ case switch tables) to hide "malicious" actions within a "sea of benign-looking transitions."

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs). 

**Note:** The "EXTRACTED STRINGS" section contains largely obfuscated or non-human-readable data that does not resolve into standard network indicators (IPs/URLs) or file system paths. The "BEHAVIORAL ANALYSIS" describes the internal logic of a custom Virtual Machine (VM), which identifies structural characteristics rather than static indicators like IPs.

--- INDICATORS OF COMPROMISE ---

**IP addresses / URLs / Domains**
*   None detected.

**File paths / Registry keys**
*   None detected.

**Mutex names / Named pipes**
*   None detected.

**Hashes**
*   None detected.

**Other artifacts**
*   **Technical Signatures (Memory Offsets):** 
    *   `0x40f650` (Identified as the "Master Dispatcher" / Interpreter Gateway)
    *   `0x4131f4` (Identified as an "Object Handler" logic point)
    *   `0x40bd9d` (Used for buffer size calculations)
*   **Behavioral Artifacts:**
    *   **Custom Scripting Engine/VM:** The presence of a multi-layered translation layer and extensive switch tables (40+ cases) serves as a structural signature for high-end, modular malware.
    *   **COM/OLE Wrapping:** Routine use of `VariantCopy` and custom wrappers to mask interaction with standard system resources.

---

## Malware Family Classification

1. **Malware family**: Unknown (Sophisticated Custom Framework)
2. **Malware type**: Loader / Backdoor
3. **Confidence**: Medium

4. **Key evidence**:
*   **Advanced VM Architecture:** The sample utilizes a "Scripting Engine" and "Master Dispatcher" switch tables to create a high-level abstraction layer. This allows the malware to execute complex operations (like file I/O or network calls) via interpreted scripts, making it extremely difficult for static analysis tools to map out its full capabilities.
*   **Decoupled Logic & Polymorphism:** By using "Instructional Indirection," the core binary serves as a vehicle; the actual malicious behavior is defined by data (the script). This allows attackers to update the malware's functionality without changing the underlying code, significantly increasing the lifespan of the campaign.
*   **APT-Level Evasion:** The use of COM/OLE wrapper hubs and "Complexity as Defense" tactics indicates a high level of maturity. These techniques are designed to mask malicious system calls within legitimate Windows API calls, typical of advanced persistent threats (APTs) or high-end RATs.
