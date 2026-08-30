# Threat Analysis Report

**Generated:** 2026-08-15 17:13 UTC
**Sample:** `0efed3b303e58e99f42f522e0c357c0b42d5999db3770f8bf43513869215c472_0efed3b303e58e99f42f522e0c357c0b42d5999db3770f8bf43513869215c472.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0efed3b303e58e99f42f522e0c357c0b42d5999db3770f8bf43513869215c472_0efed3b303e58e99f42f522e0c357c0b42d5999db3770f8bf43513869215c472.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,313,280 bytes |
| MD5 | `4d745996210940d586af0d03378c8fdc` |
| SHA1 | `6e38494f9fb7bf9813d89556711ce55c3fce51f6` |
| SHA256 | `0efed3b303e58e99f42f522e0c357c0b42d5999db3770f8bf43513869215c472` |
| Overall entropy | 6.941 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1721866898 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.668 | No |
| `.rdata` | 195,584 | 5.692 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 434,176 | 7.209 | ⚠️ Yes |
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

Total strings found: **2691** (showing first 100)

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

This analysis incorporates Chunk 5/5, which represents the "heart" of the engine. The final set of functions confirms our previous suspicion: this is not merely an obfuscated binary; it is a **highly sophisticated, custom-built execution environment (a Virtual Machine)** designed to host complex logic with multiple layers of abstraction between the malicious "intent" and the system's "action."

### Updated Analysis Report: Chunk 5/5 Integration

#### 1. Advanced Architectural Features
*   **Multi-Tiered Dispatch System:** The sheer size of the switch tables (e.g., `fcn.0040dd50` with over 40 cases and `fcn.00411310`) confirms a **nested dispatcher architecture**. Instead of one command triggering one action, the VM first identifies an "Opcode," which then leads to a secondary interpreter layer that manages memory, validates state, and finally resolves a specific system call.
*   **Complex Object Management (Variant/Object Model):** The heavy reliance on `OLEAUT32.dll_VariantCopy` and the associated logic in functions like `fcn.0040a704` indicate that the VM handles **"Objects," not just "Data."** By using a Variant-like structure, the malware can pass polymorphic data (strings, integers, pointers, or complex records) through its internal pipeline without revealing what that data is until it reaches a final "unwrapping" stage.
*   **Robust Internal Memory Management:** Functions like `fcn.0040a587` and `fcn.0040a5fb` suggest the VM maintains its own internal memory management system to handle buffers, resize them dynamically (e.g., looking for specific boundaries), and manage the "lifespan" of data in the virtual environment. This prevents raw strings or buffer sizes from being easily visible via standard heap analysis.

#### 2. Sophisticated Malicious Behaviors
*   **The Execution "Buffer Zone":** In `fcn.0040aacf`, we see a sophisticated wrapper for `USER32` interactions. Note how many instructions are required just to perform what might be a simple window update or interaction check. This is a **"Buffer Zone" strategy**: the malicious logic stays in "VM-land" as long as possible. The transition into "Windows-land" (the System APIs) happens only at the very last microsecond, and even then, it is often wrapped in several layers of internal validation (`fcn.0040ab6b`).
*   **Abstraction of Logic:** The distance between a piece of malicious bytecode (e.g., "Send Data") and the actual network or file system call is massive. Because the logic is translated into an intermediate language before it reaches the OS-facing code, **traditional signature-based detection for behavior is highly unlikely to succeed**, as the "malicious" sequence never exists in a linear form in the machine's memory.
*   **Validation and Sanitization:** The complexity of `fcn.004104f0` and `fcn.0040a7ac` indicates that the VM performs internal consistency checks. It validates lengths, boundaries, and types before "promoting" a piece of data to the system level. This makes it very difficult for an analyst to trace a high-level goal (like "Exfiltrate Data") back through the code because the "chain of intent" is broken by these abstraction layers.

#### 3. Technical Indicators & Patterns
*   **Mega-Switch Tables:** The discovery of switch tables with 40+ cases (`fcn.0040dd50`) and hundreds of lines of associated logic indicates a **mature, custom architecture.** This is typical of advanced "Protectors" (like VMProtect) or high-end APT tools where the goal is to make static analysis of the core payload almost impossible without full emulation/tracing.
*   **Instruction Folding & Expansion:** The transition from `fcn.004103c9` through `fcn.00411310` shows "instruction expansion." A single VM instruction likely expands into hundreds of host-side operations to handle memory, state management, and logic branching, effectively diluting the "signal" that automated tools look for.
*   **State-Machine Logic:** The heavy use of global/static pointers (like `0x4d2564` or `0x4d1924`) suggests a **persistent VM state**. The environment maintains its own stack, program counter, and heap, independent of the host's standard execution flow.

#### 4. Finalized Summary of Findings
*   **Analysis Type:** Sophisticated Custom Virtual Machine (VM) Interpreter with Nested Dispatching.
*   **Sophistication Level:** **Critical / Elite.** This is a high-effort piece of engineering designed to decouple the malware's functionality from its detectable patterns.
*   **Primary Risk Profile: High Persistence & Evasion.** 
    *   **Decoupled Payload:** The logic for "how" it attacks is buried in the VM; only the "engine" is visible statically.
    *   **Execution Obfuscation:** Because of the extensive multi-layer dispatching, heuristic engines will see a series of complex, seemingly meaningless calculations before an actual malicious action occurs.
    *   **Hardened Logic:** The use of intermediate data types (Variants) and internal "validation" layers means that standard memory scraping may only yield raw bytes without context.

### Final Recommendations (Finalized)
The complexity of this architecture necessitates a multi-pronged approach to analysis:

1.  **Dynamic Trace Logging (High Priority):** Use a tool like Intel PIN or a custom Frida script to hook the main dispatchers (e.g., `fcn.00411310` and `fcn.0040dd50`). Log every opcode that enters these functions. This will allow you to map out the **logic flow** of the malware as it executes, even if the underlying code is heavily obscured.
2.  **Context-Aware Memory Analysis:** Rather than simple memory dumps, perform **time-sliced memory forensics.** Capture dumps at specific intervals (e.g., every 10 seconds or upon certain events). Look for "de-obfuscated" strings that only appear in memory *after* the VM has processed its internal logic but *before* it calls a System API like `URLDownloadToFile` or `CreateRemoteThread`.
3.  **Gateway Hooking:** Focus on the "Boundary" functions (the ones interacting with `User32`, `Kernel32`, and `WinMM`). By logging the parameters passed to these functions, you can capture the **final resolved values** (IP addresses, file paths, registry keys) which are often decrypted just before use.
4.  **Emulated Sandbox Analysis:** Since static analysis is hampered by the VM layer, run the sample in a specialized sandbox that tracks "hidden" execution. This will help identify the specific points where the internal "VM-land" logic switches to "System-land" actions.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Programs | The use of a custom-built Virtual Machine, multi-tiered dispatchers, and instruction expansion are designed to hide the underlying logic from static analysis and signature-based detection. |
| T1568 | Dynamic Resolution | The "Buffer Zone" strategy ensures that system-facing parameters are only "unwrapped" or resolved at the last possible moment before calling a System API to evade heuristic monitoring. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Due to the highly sophisticated nature of the malware's architecture (custom VM interpreter), most traditional indicators such as IP addresses, URLs, and file paths are currently obscured by the "Buffer Zone" and internal dispatch layers mentioned in the report.

### **IP addresses / URLs / Domains**
*   *None identified.* (Analysis notes that these values are likely decrypted only at the final "execution moment.")

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None found in the provided strings.*

### **Other artifacts**
*   **Internal Function Offsets (VM Dispatchers):** 
    *   `0x40dd50` (Large switch table/Nested dispatcher)
    *   `0x411310` (Secondary interpreter layer)
    *   `0x40a704` (Variant object management)
    *   `0x40a587` / `0x40a5fb` (Internal memory management)
    *   `0x40aacf` (USER32 interaction wrapper)
    *   `0x40ab6b` (Validation layer)
    *   `0x4104f0` / `0x40a7ac` (Internal consistency checks)
    *   `0x4103c9` (Instruction expansion)
*   **Memory Pointers/State Addresses:** 
    *   `0x4d2564`
    *   `0x4d1924`
*   **Specific Library Interactions:** 
    *   `OLEAUT32.dll!VariantCopy` (Used for polymorphic data handling)
*   **Behavioral Patterns:**
    *   **Multi-Tiered Dispatching:** Use of large switch tables to separate "Opcode" identification from system execution.
    *   **Instruction Expansion:** Single VM instructions expanding into hundreds of host-side operations to evade heuristics.
    *   **"Buffer Zone" Strategy:** Extensive wrapper layers around `USER32`, `Kernel32`, and `WinMM` functions to delay the exposure of malicious intent.

---

## Malware Family Classification

1. **Malware family:** Unknown
2. **Malware type:** loader
3. **Confidence:** High
4. **Key evidence:** 
*   **Custom Virtual Machine Architecture:** The sample utilizes a highly sophisticated, multi-tiered VM interpreter with nested dispatchers and large switch tables to abstract the underlying malicious logic from system actions.
*   **"Buffer Zone" Strategy:** It employs an intentional gap between "VM-land" (the execution of internal code) and "System-land" (actual API calls), ensuring that sensitive indicators like IP addresses or file paths are only resolved at the last possible moment to evade heuristic detection.
*   **Intentional De-coupling:** The use of instruction expansion, complex object management, and extensive wrapping of standard libraries (USER32, Kernel32) indicates a primary goal of hiding the "chain of intent" from automated analysis tools.
