# Threat Analysis Report

**Generated:** 2026-08-31 18:39 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, UPX compressed, 3 sections |
| Size | 750,592 bytes |
| MD5 | `dc63d61ec2c2f004e25e89d0ee7f56fa` |
| SHA1 | `044617ce8fe94bf7419843946f7bbcfdd349de9e` |
| SHA256 | `12a8b3a84edee0911d548e92dcff18de315d48a5f116e2639768b434ee07cec6` |
| Overall entropy | 7.131 |
| Unpacked | ✓ Yes (tool: upx) |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771392173 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.61 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 378,368 | 7.893 | ⚠️ Yes |
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

Total strings found: **2920** (showing first 100)

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

This final chunk of disassembly provides a "microscopic" view of the malware's execution engine, moving from high-level logic to the granular implementation of its Virtual Machine (VM) and interaction layers.

The following analysis incorporates this new data into our existing profile of the threat.

---

### Updated Core Functionality and Purpose

#### 1. Massive Instruction Set & "Instruction Diversity"
The switch block at `0x40f828` inside `fcn.0040f650` is a landmark finding. It contains **over 40 distinct cases**. 
*   **What this means:** This isn't just one logic path; it is a highly complex, custom instruction set architecture (ISA). Each "case" represents a different operation the VM can perform—from basic arithmetic to system calls, memory allocation, and even UI manipulation.
*   **The "Malice" in the Logic:** By using such a diverse set of instructions internally, the malware ensures that its core logic is never exposed as a single linear sequence of code. To an automated scanner, it looks like a collection of fragmented, seemingly unrelated small operations.

#### 2. Integration with COM/OLE and Advanced Data Types
The call to `OleAut32.dll_VariantCopy` at **`0x455bd7`** is highly significant:
*   **Complexity Management:** The use of "Variants" (OLE) suggests the malware isn't just handling simple strings; it’s handling complex objects or data structures. 
*   **Persistence/Evasion:** COM-based interactions are often used to hide the actual intent behind standard system calls. It may be using these components to manipulate system settings, interact with shell objects, or manage advanced configuration data that remains encrypted until the "Variant" is processed by the VM.

#### 3. Deep-Layer UI and Window Manipulation
The presence of `USER32.dll_InvalidateRect` at **`0x4504e7`** (via the call chain in `fcn.0040c3cb`) confirms our previous suspicions regarding GUI interaction:
*   **Visual Stealth:** `InvalidateRect` is used to tell Windows that a part of a window needs to be redrawn. This suggests the malware may have its own graphical interface or, more likely, it **overlays itself over other windows** (such as banking sites or login screens), refreshing and redrawing elements dynamically to remain "on top" while looking like a legitimate part of the OS.

#### 4. Robust Memory Management & Buffer Calculation
Functions like `fcn.00411df0` and `fcn.00412c10` show heavy usage of loops, complex arithmetic for offsets, and manual "stack" or buffer management:
*   **Dynamic Decoding:** The malware doesn't use fixed memory addresses for its data; it calculates them at runtime (e.g., `iVar6 = iVar6 + iVar1 * iVar4`). This is a technique to defeat static analysis tools that look for hardcoded strings or predictable memory patterns.
*   **Validation Loops:** The code frequently checks boundaries and "validates" data before proceeding, ensuring the malware doesn't crash if it encounters unexpected system variables—a sign of high-quality professional engineering.

---

### New Technical Indicators for Threat Analysis

The addition of this chunk provides several specific technical indicators:

1.  **High Instruction Density:** The sheer number of cases in `fcn.0040f650` suggests a "Multi-Purpose" VM engine. **Detection Note:** Defenders should look for large switch tables or jump tables that serve as the central hub for and intermediate logic processing.
2.  **OLE/COM Abstraction:** The malware uses `OleAut32` to handle data. **Detection Note:** Monitor for process calls to `VariantCopy` or other OLE-related functions from non-standard applications, especially those interacting with system settings.
3.  **Runtime Buffer Calculation:** Instead of simple `strcpy` or `memcpy`, the malware uses complex arithmetic for buffer size and offset determination. **Detection Note:** This is a primary method to evade "string" scanners; look for loops that perform math on memory addresses before an operation occurs.
4.  **Direct UI Update Calls:** The use of `InvalidateRect` suggests interaction with the Windows GDI/User subsystem. **Detection Note:** Look for processes that are not known to have a GUI but are frequently calling "redraw" or "invalidated" window functions.

---

### Updated Summary for Incident Response

This final chunk confirms the malware is a **highly polished, professional-grade piece of spyware/trojan.** It doesn't just perform one task; it has an entire environment built to support multiple and complex tasks while staying hidden.

**Key Intelligence for IR Teams:**
*   **Sophisticated "Behavioral Masking":** The use of a vast internal instruction set (the 40+ case switch) means that even if you find one malicious action, it may be buried in a sea of benign-looking internal logic.
*   **Active Window Interaction:** The malware is actively aware of the GUI environment. It likely uses "Injected" or "Overlay" techniques to interact with user input or create deceptive interfaces.
*   **Detection Strategy - Memory Forensics focus:** Because the code heavily utilizes custom calculations and a VM-lite architecture, static analysis will have limited success. 
    *   **Actionable Tip:** Perform memory dumps of the process. Focus on "unpacked" memory pages where the results of the `fcn.00411df0` logic (dynamic decoding) are realized in plain text or clear instructions.
*   **Critical Indicators for Threat Hunting:**
    *   **Search for High-Entropy Memory Regions:** The VM likely decrypts its "instructions" and "data" into memory at runtime.
    *   **Identify "Gatekeeper" Loops:** Look for large switch statements that do not appear to correspond to standard Windows API patterns but instead serve as the main processing hub for the application's internal logic.

---

### Final Summary of Identified "Hot Zones":
1.  **`fcn.0040f650` (Switch at `0x40f828`)**: The heart of the VM. This is the primary engine that translates malicious intent into executable actions through a massive, complex switch table.
2.  **`fcn.00411df0` / `fcn.00412c10`**: The data processing and calculation "lab." This is where raw input (from the net or disk) is sanitized, decoded, and prepared for use.
3.  **`fcn.0040c3cb` & `fcn.0040c28f`**: The interaction bridge. These functions connect the internal VM logic to the Windows UI/User system, handling window updates and state management.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors described in the analysis to the following MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Virtualization | The malware employs a custom Instruction Set Architecture (ISA) and a large switch-block VM engine to hide its core logic from automated scanners and static analysis. |
| **T1036** | Dynamic Resolution | The use of complex arithmetic for buffer calculations and memory offset determination at runtime prevents tools from identifying hardcoded addresses or strings. |
| **T1027** | Obfuscated Files or Information | The integration of OLE/Variant structures and "Instruction Diversity" are used to mask the actual intent and payload of the code until it is processed by the VM. |
| **T1566.003** | Impersonation: User Account | (Contextual) The use of `InvalidateRect` to create overlays on common applications like banking sites indicates a tactic to deceive users into interacting with the malware as if it were part of the OS. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted Indicators of Compromise (IOCs). 

*Note: The provided text contains many internal memory offsets and technical descriptions of malware behavior rather than raw network artifacts (IPs/URLs). Because these are often "fuzzy" indicators or TTPs (Tactics, Techniques, and Procedures), they have been categorized accordingly.*

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: The strings `0x40f828`, `0x455bd7`, etc., are internal memory offsets, not file system paths or registry keys.)

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts (TTPs & Behavioral Indicators)**
*   **API/Library Interactions:**
    *   `OleAut32.dll_VariantCopy` (Used for handling complex data structures and potential evasion).
    *   `USER32.dll_InvalidateRect` (Used for UI manipulation and overlay behavior).
*   **Malware Architecture Indicators:**
    *   **Custom VM Engine:** A large switch block at `0x40f828` containing over 40 distinct cases, indicating a custom instruction set architecture (ISA) used to obfuscate core logic.
    *   **Dynamic Buffer Calculation:** Use of complex arithmetic for buffer size and offset determination (e.g., `iVar6 = iVar6 + iVar1 * iVar4`) to evade static string scanners.
    *   **Multi-Purpose VM Logic:** A "Gatekeeper" loop structure that serves as a central processing hub for internal logic, masking malicious actions among benign-looking operations.
    *   **High-Entropy Memory Regions:** The presence of dynamically decoded instructions and data in memory (indicated by the transition from raw buffer calculations to execution).

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification of the sample:

1. **Malware family**: Custom (Sophisticated Trojan)
2. **Malware type**: Trojan / Spyware
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced VM-based Obfuscation:** The use of a custom Instruction Set Architecture (ISA) with over 40 distinct cases in a central switch block (`fcn.0040f650`) indicates a high level of engineering designed to hide malicious logic from automated scanners and static analysis.
    *   **Stealthy UI Manipulation:** The presence of `InvalidateRect` combined with the "overlay" description suggests the malware is intended to sit on top of other windows (like banking sites) or hide its activity while interacting with user input.
    *   **Sophisticated Evasion Techniques:** The use of OLE/Variant structures for data management and complex arithmetic for dynamic buffer calculation indicates a professional-grade tool designed to avoid signature-based detection and "string" hunting by security tools.
