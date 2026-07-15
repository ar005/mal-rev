# Threat Analysis Report

**Generated:** 2026-07-13 16:15 UTC
**Sample:** `055675d264560c06c4fd434bfb942a23c8a8e73cd4ecba7b8370ef1b45b0c361_055675d264560c06c4fd434bfb942a23c8a8e73cd4ecba7b8370ef1b45b0c361.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `055675d264560c06c4fd434bfb942a23c8a8e73cd4ecba7b8370ef1b45b0c361_055675d264560c06c4fd434bfb942a23c8a8e73cd4ecba7b8370ef1b45b0c361.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,233,920 bytes |
| MD5 | `c7dc3ca416b0dda6ff55f3eea0fb848a` |
| SHA1 | `e58f723950a12dbb9f0adf5f9fb1546e15298024` |
| SHA256 | `055675d264560c06c4fd434bfb942a23c8a8e73cd4ecba7b8370ef1b45b0c361` |
| Overall entropy | 7.036 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1742902110 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 581,120 | 6.676 | No |
| `.rdata` | 188,928 | 5.76 | No |
| `.data` | 20,992 | 1.199 | No |
| `.rsrc` | 412,672 | 7.481 | ⚠️ Yes |
| `.reloc` | 29,184 | 6.779 | No |

### Imports

**WSOCK32.dll**: `WSACleanup`, `socket`, `ioctlsocket`, `setsockopt`, `ntohs`, `recvfrom`, `inet_addr`, `htons`, `WSAStartup`, `__WSAFDIsSet`, `select`, `accept`, `listen`, `bind`, `closesocket`
**VERSION.dll**: `GetFileVersionInfoW`, `GetFileVersionInfoSizeW`, `VerQueryValueW`
**WINMM.dll**: `timeGetTime`, `waveOutSetVolume`, `mciSendStringW`
**COMCTL32.dll**: `ImageList_ReplaceIcon`, `ImageList_Destroy`, `ImageList_Remove`, `ImageList_SetDragCursorImage`, `ImageList_BeginDrag`, `ImageList_DragEnter`, `ImageList_DragLeave`, `ImageList_EndDrag`, `ImageList_DragMove`, `InitCommonControlsEx`, `ImageList_Create`
**MPR.dll**: `WNetUseConnectionW`, `WNetCancelConnection2W`, `WNetGetConnectionW`, `WNetAddConnection2W`
**WININET.dll**: `InternetQueryDataAvailable`, `InternetCloseHandle`, `InternetOpenW`, `InternetSetOptionW`, `InternetCrackUrlW`, `HttpQueryInfoW`, `InternetQueryOptionW`, `HttpOpenRequestW`, `HttpSendRequestW`, `FtpOpenFileW`, `FtpGetFileSize`, `InternetOpenUrlW`, `InternetReadFile`, `InternetConnectW`
**PSAPI.DLL**: `GetProcessMemoryInfo`
**IPHLPAPI.DLL**: `IcmpCreateFile`, `IcmpCloseHandle`, `IcmpSendEcho`
**USERENV.dll**: `DestroyEnvironmentBlock`, `UnloadUserProfile`, `CreateEnvironmentBlock`, `LoadUserProfileW`
**UxTheme.dll**: `IsThemeActive`
**KERNEL32.dll**: `DuplicateHandle`, `CreateThread`, `WaitForSingleObject`, `HeapAlloc`, `GetProcessHeap`, `HeapFree`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `MulDiv`, `GetVersionExW`, `IsWow64Process`, `GetSystemInfo`, `FreeLibrary`, `LoadLibraryA`
**USER32.dll**: `AdjustWindowRectEx`, `CopyImage`, `SetWindowPos`, `GetCursorInfo`, `RegisterHotKey`, `ClientToScreen`, `GetKeyboardLayoutNameW`, `IsCharAlphaW`, `IsCharAlphaNumericW`, `IsCharLowerW`, `IsCharUpperW`, `GetMenuStringW`, `GetSubMenu`, `GetCaretPos`, `IsZoomed`
**GDI32.dll**: `StrokePath`, `DeleteObject`, `GetTextExtentPoint32W`, `ExtCreatePen`, `GetDeviceCaps`, `EndPath`, `SetPixel`, `CloseFigure`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `SelectObject`, `StretchBlt`, `GetDIBits`, `LineTo`, `AngleArc`
**COMDLG32.dll**: `GetOpenFileNameW`, `GetSaveFileNameW`
**ADVAPI32.dll**: `GetAce`, `RegEnumValueW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegOpenKeyExW`, `RegCloseKey`, `RegQueryValueExW`, `RegConnectRegistryW`, `InitializeSecurityDescriptor`, `InitializeAcl`, `AdjustTokenPrivileges`, `OpenThreadToken`, `OpenProcessToken`
**SHELL32.dll**: `DragQueryPoint`, `ShellExecuteExW`, `DragQueryFileW`, `SHEmptyRecycleBinW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHCreateShellItem`, `SHGetDesktopFolder`, `SHGetSpecialFolderLocation`, `SHGetFolderPathW`, `SHFileOperationW`, `ExtractIconExW`, `Shell_NotifyIconW`, `ShellExecuteW`, `DragFinish`
**ole32.dll**: `CoTaskMemAlloc`, `CoTaskMemFree`, `CLSIDFromString`, `ProgIDFromCLSID`, `CLSIDFromProgID`, `OleSetMenuDescriptor`, `MkParseDisplayName`, `OleSetContainedObject`, `CoCreateInstance`, `IIDFromString`, `StringFromGUID2`, `CreateStreamOnHGlobal`, `OleInitialize`, `OleUninitialize`, `CoInitialize`
**OLEAUT32.dll**: `LoadTypeLibEx`, `VariantCopyInd`, `SysReAllocString`, `SysFreeString`, `SafeArrayDestroyDescriptor`, `SafeArrayDestroyData`, `SafeArrayUnaccessData`, `SafeArrayAccessData`, `SafeArrayAllocData`, `SafeArrayAllocDescriptorEx`, `SafeArrayCreateVector`, `RegisterTypeLib`, `CreateStdDispatch`, `DispCallFunc`, `VariantChangeType`

## Extracted Strings

Total strings found: **2824** (showing first 100)

```
!This program cannot be run in DOS mode.
$
Richr}
`.rdata
@.data
@.reloc
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
9u(v?VSj
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

This final chunk of disassembly completes the picture of a highly sophisticated, modular malware framework. It confirms that this isn't just a command-executor; it is a **miniature operating system for malicious logic**.

The addition of these functions provides definitive evidence of advanced capabilities in **pattern matching (Regex)**, **multi-byte data handling**, and **process/resource management**.

### Updated Analysis & Findings (Final Integration)

#### 1. Advanced Data Parsing & Normalization
The code reveals that the "Translation Layer" identified earlier is even more robust than initially thought.
*   **Multi-Byte & Escape Handling:** The `switch` statements containing loops looking for `0x77` and logic handling `uVar9 + 0x4a5470` indicate that the interpreter can handle complex, non-standard string formats (e.g., escaped characters, specific Unicode encodings).
*   **Unicode/UTF-8 Normalization:** Function `fcn.00415d3f` contains logic specifically for handling high-bit character shifts (`(uVar1 & 0x3ff) << 10`). This ensures the malware can handle diverse file paths and system strings regardless of how they are encoded in the OS, a hallmark of professional-grade tools designed to work across different localized versions of Windows.

#### 2. Powerful Pattern Matching (Regex Engine)
The presence of `fcn.00416192` is a major "red flag" for high-level sophistication. The code explicitly mentions **"compiled regular expressions."**
*   **Technical Observation:** This function checks for specific magic constants and handles complex regex state logic. 
*   **Malware Implication:** Instead of simple string matching, the attacker can use Regular Expressions to filter files, identify network traffic patterns, or locate specific processes. This allows for very "surgical" actions—for example, "Delete all .txt files that contain the word 'password' in their filename."

#### 3. Persistence & Process Management
Function `fcn.00416165` is a dedicated **cleanup routine** for injected code.
*   **Technical Observation:** It iterates through an array and calls `VirtualFreeEx` and `CloseHandle`.
*   **Malware Implication:** This suggests the malware injects code into other processes (e.g., `explorer.exe` or `svchost.exe`). The routine ensures that when a task is finished, it "mops up" after itself by freeing memory and closing handles in the host process to avoid leaving detectable artifacts in memory dumps.

#### 4. Graphics & Overlay Capabilities
The functions `fcn.0041290`, `fcn.00401424`, and `fcn.004012f3` interact heavily with the **GDI (Graphics Device Interface)** library.
*   **Technical Observation:** We see calls to `Rectangle`, `Ellipse`, `MoveToEx`, `AngleArc`, and `SetPixel`. 
*   **Malware Implication:** This is an unusual find for a standard "backdoor." This suggests one of two things:
    1.  **UI Overlay:** The malware can draw over the screen, perhaps to create a fake UI or hide its own presence (common in game-cheats or sophisticated "scareware").
    2.  **Visual Obfuscation:** It might be used to render "fake" windows that look like legitimate system dialogs to deceive the user while it performs malicious tasks in the background.

---

### Updated Summary of Findings

| Feature | Observation from Code | Significance for Analysis |
| :--- | :--- | :--- |
| **Robust Interpretation** | Complex `switch` logic and multi-byte handling (`0x77` loops). | Ensures the "scripts" sent by the C2 can contain complex formatting without breaking. |
| **Regex Support** | Explicit logic for "compiled regular expressions" in `fcn.00416192`. | Allows for surgical, highly specific actions (complex filtering) via remote commands. |
| **Unicode Handling** | Hardcoded shifts and masks for high-bit character processing (`fcn.00415d3f`). | Ensures functionality across different locales and consistent "find" capabilities on the filesystem. |
| **Memory Management** | `VirtualFreeEx` loop in `fcn.00416165`. | Indicates advanced injection techniques where the malware cleans up its footprint in remote processes. |
| **GDI Rendering** | Extensive use of GDI calls (`Rectangle`, `AngleArc`) in `fcn.00401424`. | Suggests capabilities for creating overlays or fake system UI to deceive the user. |

---

### Final Conclusion on Malware Profile

This malware is a **Highly Sophisticated, Modular Framework (APT-Level).** 

The analyst's initial suspicion of a "professional" architecture is confirmed by the final disassembly. This isn't just a piece of malware; it’s a **Command & Control Platform.** It features:
1.  **A Custom Virtual Machine/Interpreter:** To decouple the malicious "actions" from the binary itself.
2.  **Advanced Scripting Capabilities:** Including Regex and complex string manipulation, allowing for dynamic behavior changes without updating the file.
3.  **Evasive Maneuvers:** Using memory-cleaning routines to hide traces in injected processes and GDI-based rendering to potentially deceive the user or hide its presence visually.

**Final Threat Assessment:** 
The primary threat is **flexibility**. Because the "maliciousness" is stored as data (the scripts) and processed by a sophisticated engine, security tools cannot easily flag it based on behavior alone, because the behavior can be changed instantly by the attacker via the C2 server. This architecture is designed to stay active in an environment for months or years while its capabilities evolve remotely.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The "Translation Layer" acts as a custom interpreter (VM) to process complex, multi-byte command strings delivered via C2. |
| **T1083** | File and Directory Discovery | The integrated Regex engine allows the attacker to perform "surgical" discovery by filtering files or data based on specific patterns. |
| **T1055** | Process Injection | The use of `VirtualFreeEx` and `CloseHandle` confirms the malware injects code into other processes and manages memory to hide its presence. |
| **T1027** | Obfuscated Files or Information | The sophisticated handling of multi-byte characters and Unicode normalization ensures the payload remains functional while evading simple string analysis. |
| **Defense Evasion** | (General Category) | The GDI rendering capabilities are used to create fake UI overlays or hide activities from the user, providing a layer of visual deception. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "EXTRACTED STRINGS" section contains mostly obfuscated data or junk bytes common in packed/malware samples; no clear plaintext IP addresses, URLs, or file paths were identified.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: Strings like `.rdata`, `.data`, and `.reloc` are standard PE header segments and have been excluded as false positives.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No valid MD5, SHA1, or SHA256 hashes were found in the provided strings.)

### **Other artifacts**
The following are behavioral indicators and technical "fingerprints" derived from the analysis of the malware's functionality:

*   **Technical Logic Markers:** 
    *   `fcn.00415d3f`: Function associated with Unicode/UTF-8 normalization (bit shifting `0x3ff`).
    *   `fcn.00416192`: Function identifying a "compiled regular expression" engine.
    *   `fcn.00416165`: Cleanup routine for injected code (utilizing `VirtualFreeEx` and `CloseHandle`).
    *   `fcn.0041290`, `fcn.00401424`, `fcn.004012f3`: Functions associated with GDI graphics rendering (`Rectangle`, `Ellipse`, `MoveToEx`, `AngleArc`, `SetPixel`).
*   **C2 Interaction Patterns:** 
    *   The malware utilizes a "Translation Layer" and complex `switch` logic to process remote commands.
    *   Support for multi-byte data handling (specifically identifying the `0x77` byte) indicates custom command processing from a C2 server.
*   **Capabilities/Behaviors:**
    *   **Regex Filtering:** The malware can perform targeted file system actions based on complex regular expressions.
    *   **Process Injection:** Evidence of evidence of injected code and routine "mop-up" of memory handles to evade detection.
    *   **Visual Obfuscation:** Use of GDI libraries suggests the potential for creating fake system dialogs or UI overlays to deceive users.

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification of the sample:

1. **Malware family**: Custom (Advanced Modular Framework)
2. **Malware type**: Backdoor / RAT
3. **Confidence**: High
4. **Key evidence**:
    *   **Modular Command & Control Architecture:** The presence of a "Translation Layer" and a custom interpreter/VM indicates the malware is not a simple one-off tool but a sophisticated platform designed to execute complex scripts sent from a C2 server, allowing for dynamic behavior updates.
    *   **Advanced Evasion & Persistence:** The use of `VirtualFreeEx` logic specifically designed to "mop up" memory after process injection and the inclusion of a robust Regex engine for "surgical" data discovery indicate high-level sophistication typical of APT (Advanced Persistent Threat) tools.
    *   **Deceptive Capabilities:** The integration of GDI rendering functions (`Rectangle`, `Ellipse`, etc.) suggests the ability to create fake system dialogs or visual overlays to deceive users and mask malicious activity in real-time.
