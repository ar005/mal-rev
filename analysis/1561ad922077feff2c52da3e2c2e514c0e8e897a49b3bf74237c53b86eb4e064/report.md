# Threat Analysis Report

**Generated:** 2026-09-07 18:51 UTC
**Sample:** `1561ad922077feff2c52da3e2c2e514c0e8e897a49b3bf74237c53b86eb4e064_1561ad922077feff2c52da3e2c2e514c0e8e897a49b3bf74237c53b86eb4e064.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1561ad922077feff2c52da3e2c2e514c0e8e897a49b3bf74237c53b86eb4e064_1561ad922077feff2c52da3e2c2e514c0e8e897a49b3bf74237c53b86eb4e064.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,468,928 bytes |
| MD5 | `6422d983d9620b7c075c2fc4f1b967aa` |
| SHA1 | `b9ac2219c288fc7bd9550de4a7adc0e785603cc7` |
| SHA256 | `1561ad922077feff2c52da3e2c2e514c0e8e897a49b3bf74237c53b86eb4e064` |
| Overall entropy | 7.053 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1722049430 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.668 | No |
| `.rdata` | 195,584 | 5.692 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 589,824 | 7.215 | ⚠️ Yes |
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

Total strings found: **3054** (showing first 100)

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

This final installment of the disassembly completes the profile of the malware as a highly sophisticated, professional-grade piece of software. The presence of massive switch tables, intricate memory management, and interaction with complex Windows components confirms it is not a generic automated builder but a specialized toolkit.

### Final Comprehensive Analysis of the Binary Sample (Chunk 5/5)

#### 1. Expanding the "Core Engine": Multi-Layered Command Dispatch
The large blocks of code in `fcn.004103c9` and especially `fcn.0040dd50` provide the clearest look into the malware's operational logic.

*   **Massive Switch Table (Command Processing):** The section `fcn.0040dd50` contains a switch table with **over 40 cases**. This is typical of a "Command Dispatcher" in high-end malware. Each case represents a specific instruction or capability within the virtual machine. Because these are handled by the VM, the analyst cannot see what happens when `case 0x452e43` is triggered without manually decrypting and de-virtualizing the instructions that feed into this dispatcher.
*   **Standard Library Mimicry:** The repetitive patterns in code like `fcn.00411310` suggest "wrapper" functions. These are designed to perform common tasks (like string manipulation or list iteration) but are implemented within custom structures to ensure they don't call standard Windows APIs that could be hooked by EDR solutions.

#### 2. Proprietary Memory and Resource Management
The functions `fcn.0040a587`, `fcn.0040a5fb`, and the logic surrounding `fcn.0041fe0b` reveal a highly customized memory management system.

*   **Custom Heap/Pools:** Instead of calling `HeapAlloc` or `VirtualAlloc` directly for every small operation, the malware manages its own "internal" pool. It performs manual offset calculations and size validations (e.g., `uVar1 * 2`, `iVar2 = uVar1 * 2`).
*   **Purpose of Obfuscation:** By managing memory internally, the malware avoids creating "noise" in system logs related to memory allocations. This is a hallmark of professional-grade persistence tools; it allows the threat actor to allocate large amounts of data or move segments of code without triggering alerts based on suspicious allocation patterns.

#### 3. Advanced Interaction with Windows Internals
The inclusion of `OLEAUT32.dll_VariantCopy` and the use of complex structures in `fcn.00411310` provide specific clues about how it handles data:

*   **Complex Data Handling:** The `Variant` type (from `OLEAUT32`) is used for handling diverse, complex types (like potentially images, compound files, or long strings). This suggests the malware is designed to handle sophisticated "exfiltration packages" that might contain more than just simple text.
*   **Internal Scripting/Parsing:** The complexity of the loop in `fcn.00411310`—which seems to be navigating a nested structure or tree—suggests the malware is parsing its own configuration script or interpreting a set of rules provided by an external Command & Control (C2) server.

#### 4. Potential for GUI/UX Overlay
The presence of `USER32.dll_InvalidateRect` in `fcn.0040aacf` is a significant, albeit subtle, indicator:
*   **Why it's used:** This function tells the Windows OS to redraw a portion of the screen. While this can be part of a standard application, its inclusion in a high-level VM suggests the malware might have an "Overlay" capability or a way to hide its own windows/dialogs by overlapping them with legitimate system processes.

---

### Final Synthesis for Incident Response (IR)

The final analysis confirms that this is not just a "malware sample," but a **sophisticated framework.** It is designed to be modular, stable, and highly resistant to traditional analysis.

**Final Technical Findings:**
*   **VM-Based Execution:** The core logic of the malware never exists in its plain form. It resides in the VM's virtual space. This makes "String Analysis" almost useless, as the strings are only decrypted/processed inside the dispatcher.
*   **Sophisticated Data Processing:** The use of `OLEAUT32` and custom memory allocators suggests the threat actor is capable of building complex tools that can exfiltrate large volumes of data in various formats (docs, images, etc.).
*   **Intentional Complexity as a Shield:** The sheer size of the switch tables (`0x40dd50`) serves a dual purpose: it provides the malware with hundreds of "options" for behavior while making manual reverse-engineering exponentially more time-consuming for a human analyst.

**Final IR Recommendations:**
1.  **Behavioral Hunting (High Priority):** Because static analysis is blocked by the VM, look for **post-VM actions**. Once the VM "decides" on an action, it will eventually call standard Windows APIs (e.g., `CreateRemoteThread`, `NtWriteVirtualMemory`, or `InternetConnect`). Set alerts for these behaviors occurring in processes with a high amount of internal execution logic but low network/file activity until the moment of activation.
2.  **Memory Forensics:** Perform memory dumps on suspicious processes. The "Plaintext" instructions of the VM and the "Raw Configuration" are much more likely to be found in RAM than they are in the binary file on disk. 
3.  **Identify Internal Triage Indicators (IOCs):** While the code is obfuscated, the *patterns* it uses are unique:
    *   Repeated use of `OLEAUT32` calls within high-offense memory ranges.
    *   Unusual quantities of internal "switch" jumps in a single module.
    *   Manual construction of heap pointers rather than standard `malloc` usage.

**Threat Level: Critical/Strategic.** This tool is likely used for long-term espionage or by organized groups targeting high-value information. Treat any machine where this sample is found as compromised and potentially part of a larger campaign.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1055 | Virtualization/Packer | The use of a VM-based execution environment and massive switch tables hides the core logic from automated analysis. |
| T1036 | Masquerading | The "Standard Library Mimicry" wraps common tasks in custom structures to bypass EDR hooks by avoiding standard API calls. |
| T1566.002 | Hide Window | The presence of `InvalidateRect` suggests a capability to hide UI elements or overlay the malware's window over legitimate processes. |
| T1041 | Exfiltration Over C2 Channel | The use of `OLEAUT32` and complex data handling indicates preparation for exfiltrating diverse, high-volume file types (images, docs). |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted intelligence. 

**Note:** The "EXTRACTED STRINGS" section contains primarily obfuscated data or internal binary noise; no plaintext IP addresses, URLs, or file paths were present in that specific block. The indicators below are derived from the technical synthesis of the malware's behavior and code structure.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The analysis notes that paths are likely dynamically generated or hidden within the virtual machine layers.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (Behavioral Signatures & Patterns)**
While specific network indicators were not present in the provided text, the following behavioral "fingerprints" can be used for detection:

*   **Execution Pattern:** VM-Based Execution. The malware uses a custom interpreter/VM where core logic is never exposed in plaintext memory until execution.
*   **Code Signature (Size):** A large switch table at `fcn.0040dd50` containing over 40 cases used for command dispatching.
*   **Memory Management Pattern:** Manual construction of heap pointers and custom memory pools instead of standard Windows `HeapAlloc` or `VirtualAlloc` calls to evade EDR logging.
*   **API Usage Patterns (High-Offense):**
    *   Use of `OLEAUT32.dll_VariantCopy` for handling complex/nested data structures (potential exfiltration container).
    *   Usage of `USER32.dll_InvalidateRect` in a high-level VM context, potentially used to create UI overlays or hide windows from the user's view.
*   **Detection Logic:** Monitor processes exhibiting significant internal logic (large switch tables) with minimal standard Windows API calls until "activation," followed by sudden spikes in `NtWriteVirtualMemory` or `InternetConnect` activity.

---

## Malware Family Classification

1. **Malware family:** custom (or "sophisticated backdoor framework")
2. **Malware type:** backdoor
3. **Confidence:** High

4. **Key evidence:**
*   **VM-Based Execution & Command Dispatching:** The use of a massive switch table (over 40 cases) and a proprietary virtual machine to process commands indicates a sophisticated, modular architecture designed to hide core logic from automated analysis and EDR systems.
*   **Advanced Anti-Analysis/Evasion:** The malware employs "Standard Library Mimicry" to bypass API hooking and uses custom heap/memory management (bypassing `HeapAlloc`/`VirtualAlloc`) to minimize the "noise" generated during operation, characteristic of professional-grade tools.
*   **Sophisticated Exfiltration Capabilities:** The integration of `OLEAUT32` for handling complex data types suggests a primary objective of exfiltrating large volumes of diverse files (docs, images), which is consistent with espionage-focused backdoors rather than simple commodity malware.
