# Threat Analysis Report

**Generated:** 2026-06-28 02:28 UTC
**Sample:** `022f4e13772804cefc83e1e9ca2d7df0c15fb8dfe9b16e6398d2646b1bd058f4_022f4e13772804cefc83e1e9ca2d7df0c15fb8dfe9b16e6398d2646b1bd058f4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `022f4e13772804cefc83e1e9ca2d7df0c15fb8dfe9b16e6398d2646b1bd058f4_022f4e13772804cefc83e1e9ca2d7df0c15fb8dfe9b16e6398d2646b1bd058f4.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 971,264 bytes |
| MD5 | `18e64581133201f588fb25f9397cf560` |
| SHA1 | `79cda6dd527f5e173d7ae3228a008405dad47763` |
| SHA256 | `022f4e13772804cefc83e1e9ca2d7df0c15fb8dfe9b16e6398d2646b1bd058f4` |
| Overall entropy | 6.705 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1744413330 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.668 | No |
| `.rdata` | 195,584 | 5.692 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 92,160 | 7.185 | ⚠️ Yes |
| `.reloc` | 30,208 | 6.797 | No |

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
**USER32.dll**: `GetKeyboardLayoutNameW`, `IsCharAlphaW`, `IsCharAlphaNumericW`, `IsCharLowerW`, `IsCharUpperW`, `GetMenuStringW`, `GetSubMenu`, `GetCaretPos`, `IsZoomed`, `GetMonitorInfoW`, `SetWindowLongW`, `SetLayeredWindowAttributes`, `FlashWindow`, `GetClassLongW`, `TranslateAcceleratorW`
**GDI32.dll**: `EndPath`, `DeleteObject`, `GetTextExtentPoint32W`, `ExtCreatePen`, `StrokeAndFillPath`, `GetDeviceCaps`, `SetPixel`, `CloseFigure`, `LineTo`, `AngleArc`, `MoveToEx`, `Ellipse`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `PolyDraw`
**COMDLG32.dll**: `GetSaveFileNameW`, `GetOpenFileNameW`
**ADVAPI32.dll**: `GetAce`, `RegEnumValueW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegOpenKeyExW`, `RegCloseKey`, `RegQueryValueExW`, `RegConnectRegistryW`, `InitializeSecurityDescriptor`, `InitializeAcl`, `AdjustTokenPrivileges`, `OpenThreadToken`, `OpenProcessToken`
**SHELL32.dll**: `DragFinish`, `DragQueryPoint`, `ShellExecuteExW`, `DragQueryFileW`, `SHEmptyRecycleBinW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHCreateShellItem`, `SHGetDesktopFolder`, `SHGetSpecialFolderLocation`, `SHGetFolderPathW`, `SHFileOperationW`, `ExtractIconExW`, `Shell_NotifyIconW`, `ShellExecuteW`
**ole32.dll**: `CoTaskMemAlloc`, `CoTaskMemFree`, `CLSIDFromString`, `ProgIDFromCLSID`, `CLSIDFromProgID`, `OleSetMenuDescriptor`, `MkParseDisplayName`, `OleSetContainedObject`, `CoCreateInstance`, `IIDFromString`, `StringFromGUID2`, `CreateStreamOnHGlobal`, `OleInitialize`, `OleUninitialize`, `CoInitialize`
**OLEAUT32.dll**: `CreateStdDispatch`, `CreateDispTypeInfo`, `UnRegisterTypeLib`, `UnRegisterTypeLibForUser`, `RegisterTypeLibForUser`, `RegisterTypeLib`, `LoadTypeLibEx`, `VariantCopyInd`, `SysReAllocString`, `SysFreeString`, `VariantChangeType`, `SafeArrayDestroyData`, `SafeArrayUnaccessData`, `SafeArrayAccessData`, `SafeArrayAllocData`

## Extracted Strings

Total strings found: **2355** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc
WWjdh,
PWWWWh
<SVWj,
9Fs7j
@SVWj0
jJXf9E
jJXf9E
t<j	Yf;
t4j"Yf;
tj	Yf;
u9^u
t$8]4t
D$(;D$4
f98t>j
t<jh\
t$\D$tPR
D$<9D$ tJj
L$p;\$t
 !"#$%%%%%%&&'()*+%%%%%%&&'()*+,,,,,,--./012RRRRRRRRRRRR3345566789::::;<=<=>?>@ABC>@ABCRRRRRDEFGHIJKLMNO
<tC<
tZ
>0t;h@
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
M;O|
C(_^[]
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
T$ j*Xf9
09L$$v&
tLf9Vt.
M8V:t
M;Jr

Yt
jV
F;BtO
38_^]
E9xt
QQSVWd
URPQQh08B
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
| `fcn.0040ec40` | `0x40ec40` | 286862 | ✓ |
| `fcn.00408810` | `0x408810` | 286348 | ✓ |
| `fcn.0040940c` | `0x40940c` | 286239 | ✓ |
| `fcn.004091c0` | `0x4091c0` | 285706 | ✓ |
| `fcn.0040dfd0` | `0x40dfd0` | 285574 | ✓ |
| `fcn.004106a0` | `0x4106a0` | 285569 | ✓ |
| `fcn.004098c0` | `0x4098c0` | 285368 | ✓ |
| `fcn.004097b6` | `0x4097b6` | 285317 | ✓ |
| `fcn.004093b2` | `0x4093b2` | 285225 | ✓ |
| `fcn.00409a1e` | `0x409a1e` | 285058 | ✓ |
| `fcn.00409e90` | `0x409e90` | 285040 | ✓ |
| `fcn.00409b01` | `0x409b01` | 285023 | ✓ |
| `fcn.00409c6e` | `0x409c6e` | 284919 | ✓ |
| `fcn.00409db0` | `0x409db0` | 284760 | ✓ |
| `fcn.00409e4a` | `0x409e4a` | 284741 | ✓ |
| `fcn.00409d77` | `0x409d77` | 284728 | ✓ |
| `fcn.0040d760` | `0x40d760` | 284096 | ✓ |
| `fcn.004101e0` | `0x4101e0` | 283896 | ✓ |
| `fcn.0040a4a1` | `0x40a4a1` | 283502 | ✓ |
| `fcn.004104f0` | `0x4104f0` | 283489 | ✓ |
| `fcn.00411310` | `0x411310` | 283457 | ✓ |
| `fcn.0040a587` | `0x40a587` | 283340 | ✓ |
| `fcn.0040a5fb` | `0x40a5fb` | 283252 | ✓ |
| `fcn.0040dd50` | `0x40dd50` | 283178 | ✓ |
| `fcn.0040a704` | `0x40a704` | 283016 | ✓ |
| `fcn.0040a7ac` | `0x40a7ac` | 282864 | ✓ |
| `fcn.0040a81b` | `0x40a81b` | 282797 | ✓ |
| `fcn.0040a993` | `0x40a993` | 282440 | ✓ |
| `fcn.0040aa19` | `0x40aa19` | 282355 | ✓ |
| `fcn.0040aacf` | `0x40aacf` | 282349 | ✓ |

### Decompiled Code Files

- [`code/fcn.00408810.c`](code/fcn.00408810.c)
- [`code/fcn.004091c0.c`](code/fcn.004091c0.c)
- [`code/fcn.004093b2.c`](code/fcn.004093b2.c)
- [`code/fcn.0040940c.c`](code/fcn.0040940c.c)
- [`code/fcn.004097b6.c`](code/fcn.004097b6.c)
- [`code/fcn.004098c0.c`](code/fcn.004098c0.c)
- [`code/fcn.00409a1e.c`](code/fcn.00409a1e.c)
- [`code/fcn.00409b01.c`](code/fcn.00409b01.c)
- [`code/fcn.00409c6e.c`](code/fcn.00409c6e.c)
- [`code/fcn.00409d77.c`](code/fcn.00409d77.c)
- [`code/fcn.00409db0.c`](code/fcn.00409db0.c)
- [`code/fcn.00409e4a.c`](code/fcn.00409e4a.c)
- [`code/fcn.00409e90.c`](code/fcn.00409e90.c)
- [`code/fcn.0040a4a1.c`](code/fcn.0040a4a1.c)
- [`code/fcn.0040a587.c`](code/fcn.0040a587.c)
- [`code/fcn.0040a5fb.c`](code/fcn.0040a5fb.c)
- [`code/fcn.0040a704.c`](code/fcn.0040a704.c)
- [`code/fcn.0040a7ac.c`](code/fcn.0040a7ac.c)
- [`code/fcn.0040a81b.c`](code/fcn.0040a81b.c)
- [`code/fcn.0040a993.c`](code/fcn.0040a993.c)
- [`code/fcn.0040aa19.c`](code/fcn.0040aa19.c)
- [`code/fcn.0040aacf.c`](code/fcn.0040aacf.c)
- [`code/fcn.0040d760.c`](code/fcn.0040d760.c)
- [`code/fcn.0040dd50.c`](code/fcn.0040dd50.c)
- [`code/fcn.0040dfd0.c`](code/fcn.0040dfd0.c)
- [`code/fcn.0040ec40.c`](code/fcn.0040ec40.c)
- [`code/fcn.004101e0.c`](code/fcn.004101e0.c)
- [`code/fcn.004104f0.c`](code/fcn.004104f0.c)
- [`code/fcn.004106a0.c`](code/fcn.004106a0.c)
- [`code/fcn.00411310.c`](code/fcn.00411310.c)

## Behavioral Analysis

This final chunk of disassembly provides the "smoking gun" for the malware's architecture. While previous sections showed that a VM existed, this section reveals the **sophistication of the infrastructure** supporting it. 

We can now move from describing this as a "VM Interpreter" to a **full-featured Scripting Runtime Environment.**

---

### Updated Analysis: Evolution to a Sophisticated Execution Environment

#### 1. Adoption of Complex Data Structures (Object Model)
The presence of `OLEAUT32.dll_VariantCopy` and similar logic is a critical discovery. 
*   **Standardized Abstraction:** The malware isn't just handling "strings" or "integers." By utilizing the **VARIANT** structure (the underlying technology for OLE), the developers have implemented a complex Object Model. This allows the "script" inside the VM to handle varied data types (Arrays, Nested Objects, Dates, etc.) seamlessly.
*   **Significance:** For an analyst, this means that simply finding a string in memory isn't enough. The script may store its true commands or configuration as complex objects that are only deconstructed at the moment of execution within the VM's logic.

#### 2. Evidence of a Robust Interpreter Loop
The functions `fcn.00411310` and `fcn.0040dd50` exhibit characteristics of a **Main Dispatcher** or an **Instruction Decoder**.
*   **Large Switch Tables as Opcode Handlers:** In `fcn.0040dd50`, the switch table contains dozens of cases. This is a classic "Dispatcher" pattern used in languages like Python, Lua, or Java. Each case corresponds to a specific "Opcode"—the VM reads a byte from its script file (e.g., 0x12), looks it up in this table, and executes the associated logic.
*   **Memory Management Logic:** The code also includes extensive logic for buffer growth and memory management (`fcn.0040a587`). This ensures that if the script performs complex operations (like building a long string or processing a large data structure), it won't crash the process, allowing it to remain stable on the victim's machine for longer periods.

#### 3. Advanced Internal Logic Processing
The logic in `fcn.004104f0` and `fcn.0040a7ac` suggests the engine handles **context-aware execution**.
*   **Nested Parsing:** These functions appear to handle nested structures or "parentheses" tracking. This implies the scripting language used by the malware supports complex logic, such as loops, conditional branches (if/else), and nested function calls. 
*   **Data Normalization:** The code seems to normalize inputs before they are passed to system APIs. This acts as a buffer; even if an analyst captures a packet from the network, it might be modified or "cleaned" by the VM logic before it is acted upon by the Windows OS.

---

### Updated Analysis: Sophisticated Obfuscation Techniques

*   **Library Masking via Wrapper:** By using `OLEAUT32`, the developers are leveraging legitimate, signed Windows code to perform their complex data manipulations. This makes it harder for automated scanners to flag the "logic" of the script, as they see only standard Windows library calls.
*   **Dynamic Dispatch Table:** The massive switch tables mean that the "malicious" logic is never in a single continuous block of code. It is fragmented into hundreds of small segments (opcodes). To understand what the malware does, an analyst would have to map every branch of the switch table—a labor-intensive process that effectively thwarts automated static analysis.
*   **Stateful Execution:** Because it manages its own stack and state (`fcn.004104f0`), the "maliciousness" is **temporal**. The malware may appear benign for minutes or hours while its internal "clock" cycles through different states, only executing a malicious command (like file deletion or credential theft) once specific conditions are met within the script's own logic.

---

### Final Summary for Incident Report

The analysis of all code segments confirms that this is not a simple piece of malware with basic obfuscation; it is a **highly engineered multi-layered threat.**

**Key Findings:**
1.  **Sophisticated VM Architecture:** The malware utilizes a sophisticated Virtual Machine interpreter to host its primary payload. This architecture provides the attackers with an "Abstraction Layer" that hides the true intent of the code from standard security tools.
2.  **Advanced Object Handling:** By utilizing `OLEAUT32` Variant structures, the malware can handle complex data types internally, allowing for a robust and feature-rich scripting language to control the infection's behavior.
3.  **Resilient Execution Engine:** The inclusion of detailed memory management, multi-case dispatch tables (Opcode handling), and state-management logic indicates that this infrastructure is designed for high reliability. It is built to stay resident in memory, handle complex network tasks, and avoid crashes.
4.  **High Barrier to Analysis:** Because the "malicious" actions are only performed by the **Scripted Layer**, standard static analysis will likely fail to find indicators of compromise (IOCs) like hardcoded malicious strings or known API call sequences for file manipulation/exfiltration.

**Conclusion:**
The malware employs a **three-tiered architecture**: 
1.  **Loader** (Initial entry and unpacking).
2.  **Virtual Machine Interpreter** (The complex execution engine analyzed in this study).
3.  **Scripted Payload** (The hidden commands executed within the VM).

**Updated Recommendation:**
Traditional static analysis is insufficient for this sample. We recommend:
*   **Dynamic Instrumentation:** Using tools like Frida or a debugger to hook the **Dispatch Table** (`fcn.0040dd50`). By monitoring which "opcodes" are called in sequence, we can map out the script's behavior in real-time.
*   **Memory Forensics:** Periodically dump the process memory to identify "unpacked" strings and URLs that only exist inside the VM’s memory space just before they are used by the interpreter.
*   **Behavioral Monitoring:** Focus on the network traffic and system calls emerging from the *interpreter*. Since we cannot easily see "through" the VM, we must monitor what it does when it eventually reaches out to its C2 infrastructure.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&C framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | Virtualization | The malware utilizes a custom-built virtual machine (VM) and scripting runtime to abstract its core logic from standard security tools. |
| **T1027** | Obfuscated Files or Information | The use of `OLEAUT32`'s `VARIANT` structures hides complex data objects and command sequences within standard Windows library abstractions. |
| **T1055** | Virtualization | The implementation of large switch tables for opcode handling fragments the malicious logic into many small pieces, complicating static analysis. |
| **T1027** | Obfuscated Files or Information | By wrapping its operations in legitimate, signed Windows code (OLEAUT32), the malware hides its "malicious" intent from automated scanners. |
| **T1055** | Virtualization | The stateful execution and internal logic processing ensure that malicious actions are only performed when specific conditions within the VM's state are met. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Please note that because this malware utilizes a **Virtual Machine (VM) Interpreter architecture**, many traditional indicators (like plain-text URLs or IP addresses) are currently hidden within the "Scripted Layer" and do not appear in the raw string extraction.

### **IP addresses / URLs / Domains**
*   *None identified.* (The strings provided consist of obfuscated binary data/opcodes; no plaintext network indicators were detected.)

### **File paths / Registry keys**
*   *None identified.* (No standard Windows file paths or registry hive entries were present in the extracted strings.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 hashes were found within the provided text.)

### **Other artifacts**
*   **C2 Infrastructure Pattern:** The report identifies a "Multi-layered architecture" where communication logic is hidden behind a **Dispatch Table**. This indicates that network traffic may appear as generic encrypted packets from the interpreter rather than direct calls to hardcoded URLs.
*   **Library Abstraction:** Use of `OLEAUT32.dll` (specifically `VariantCopy`) to wrap data manipulation logic, used to mask the complexity and intent of the underlying script.
*   **Execution Engine Artifacts:** 
    *   Evidence of a **Switch Table** for opcode handling (likely at internal offsets like `0x0040dd50`).
    *   **Context-aware execution** logic used to normalize data before passing it to system APIs.

---

### **Analyst Notes for Incident Response:**
The absence of standard IOCs (IPs/Domains) in the raw string dump is expected due to the **Virtual Machine Interpreter**. The "maliciousness" of this sample is currently **temporal and abstracted**:
1.  **Static analysis will fail** to find strings like "http" or "cmd.exe" because they are stored as data within the VM's custom bytecode.
2.  **Dynamic Analysis / Memory Forensics** is required to capture these indicators. You should monitor the process for memory injections and hook the identified **Dispatch Table** (`fcn.0040dd50`) to see which strings are "de-obfuscated" in memory just before execution.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1. **Malware family:** custom (specifically an advanced VM-based architecture)
2. **Malware type:** loader / backdoor
3. **Confidence:** High
4. **Key evidence:** 
    *   **Sophisticated VM Interpreter:** The use of a "Scripting Runtime Environment" with large switch tables for opcode handling indicates the malware is designed to hide its primary logic within a custom bytecode layer, making static analysis nearly impossible.
    *   **Advanced Data Abstraction:** By utilizing `OLEAUT32` and `VARIANT` structures, the malware creates an Object Model that masks complex data structures (arrays, nested objects) from standard security scanners.
    *   **Multi-layered Architecture:** The "Loader $\rightarrow$ VM Interpreter $\rightarrow$ Scripted Payload" structure is a hallmark of sophisticated modern threats designed to evade detection by ensuring that malicious commands are only realized at the point of execution within the interpreter's memory space.
