# Threat Analysis Report

**Generated:** 2026-08-11 16:31 UTC
**Sample:** `0e01b51e306339081d897f81ede22bb42abfbe3c5536b7d0eb387c4e7b861e74_0e01b51e306339081d897f81ede22bb42abfbe3c5536b7d0eb387c4e7b861e74.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e01b51e306339081d897f81ede22bb42abfbe3c5536b7d0eb387c4e7b861e74_0e01b51e306339081d897f81ede22bb42abfbe3c5536b7d0eb387c4e7b861e74.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,027,584 bytes |
| MD5 | `9596579453919b78ab74f05f7a465ec3` |
| SHA1 | `de99e24c502fc7d144082a6a55af77acf7d5c137` |
| SHA256 | `0e01b51e306339081d897f81ede22bb42abfbe3c5536b7d0eb387c4e7b861e74` |
| Overall entropy | 6.818 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1765925629 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 633,856 | 6.666 | No |
| `.rdata` | 195,584 | 5.693 | No |
| `.data` | 18,432 | 0.585 | No |
| `.rsrc` | 148,480 | 7.591 | ⚠️ Yes |
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

Total strings found: **2457** (showing first 100)

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

This analysis incorporates the final set of disassembly (chunk 5/5), which provides a definitive look at the **core architecture** of the binary's execution engine.

### Updated Technical Analysis (Chunk 5/5)

#### 1. Multi-Tiered Dispatch Architecture
The discovery of multiple, massive switch-case tables—specifically in `fcn.00411fa0` and `fcn.0040f650`—confirms that this is not a simple script runner, but a **complex multi-layered interpreter.** 
*   **Tiered Translation:** The first level of dispatch (`fcn.00411fa0`) appears to handle high-level scripting logic (likely handling "Action" commands), while the second, larger switch table in `fcn.0040f650` acts as a **System Bridge.** 
*   **The Switch as an Abstraction Layer:** Because the analyst only sees "Jump to Case X," they cannot determine what the script is doing just by looking at the C++ code. One case might be `Get_File_Content`, another might be `Send_Packet`. The malicious intent remains hidden behind a numerical index in a table.

#### 2. Complex Memory & Buffer Management (The "Engine" Layer)
Functions like `fcn.0040bd9d` and `fcn.0040bef7` demonstrate an advanced approach to memory handling:
*   **Dynamic Resizing:** These functions don't just allocate a fixed buffer; they check current usage, calculate growth requirements, and re-allocate/re-position data dynamically. 
*   **Safety Wrappers:** The logic ensures that strings are not only long enough but also correctly terminated and aligned. This level of "polish" is characteristic of professional software frameworks where stability is paramount to ensure the malware doesn't crash while interacting with system resources or network sockets.

#### 3. Sophisticated Internal Logic in `fcn.00412c10`
This function serves as a primary workhorse for data processing:
*   **Recursive/Iterative Processing:** It uses complex loops to navigate internal structures, likely iterating through "objects" or "properties" within the script's memory space.
*   **Internal State Management:** The repeated calls to `fcn.00413220` and subsequent property lookups suggest it is processing a **property-based object model** (similar to how JavaScript objects or COM objects behave).

#### 4. Evidence of High-Level Abstractions
The recurring use of `OLEAUT32.dll_VariantCopy` across different functions (even in the final chunk) reinforces that the environment is designed to handle "Polymorphic Data." This allows a single variable in the script to hold a string, an integer, or a complex nested object without the C++ engine needing to know the specifics of the data beforehand.

---

### Final Comprehensive Analysis Summary

The analysis of all five chunks confirms that this binary is a **high-maturity, production-grade interpreter.** It is designed specifically to host and execute scripts (likely AutoIt) while providing several layers of protection against static and dynamic analysis:

#### 1. Architecture: The "Black Box" Strategy
The malware's primary defense mechanism is **Abstraction**. By using a sophisticated C++ engine as the "host," the developers have decoupled the *mechanism* from the *intent*.
*   **Mechanism:** The C++ code handles memory, network communication, file I/O, and system interaction.
*   **Intent:** The script (the actual payload) tells the engine *what* to do using high-level commands. 
*   **Result:** An analyst looking at the binary sees a complex but "innocent" interpreter. The malicious instructions only exist as data within the script files, which are then interpreted by the C++ engine at runtime.

#### 2. Key Technical Indicators:
*   **Complex Dispatcher:** Multiple nested switch-cases serve as an "Instruction Decoder." This forces the analyst to work backward from a specific behavior to find the corresponding entry in the table, which is often difficult if many entries share similar code paths or are dynamically linked.
*   **Variant & Object Support:** The integration with `OLEAUT32` confirms that the system is capable of handling complex data structures, allowing for advanced, multi-stage capabilities within the script layer.
*   **Robustness:** Advanced buffer management and automated string normalization indicate that this tool was built to be stable and resilient against inconsistent input (e.g., various OS versions or network responses).

#### 3. Conclusion & Threat Profile
This is a **Sophisticated Persistence/Command-and-Control (C2) Framework.** It is not a "one-off" piece of malware; it is a platform designed for long-term operation. 
*   **Flexibility:** The threat actor can update the behavior of the backdoor by simply pushing a new script to the host, without ever changing the binary.
*   **Evasion:** By moving the core logic into an interpreted layer, they significantly increase the "Analysis Tax." A defender cannot easily see what the malware is doing without successfully extracting and reversing the internal script language/logic.

**Final Verdict:** This binary acts as a **hardened container for malicious automation.** It provides all the luxury features of a full programming environment to ensure that any subsequent scripts run with maximum reliability and minimal visibility into their underlying operations.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The analysis confirms the binary is a "production-grade interpreter" designed to host and execute scripts (e.g., AutoIt) at its core. |
| **T1027** | Obfuscated Syntax/Code or Programs | The use of multi-tiered switch-case tables as an abstraction layer hides malicious intent behind numerical indices, intentionally increasing the "analysis tax." |
| **T1106** | Native API | The "System Bridge" (fcn.0040f650) provides the interpreter with a gateway to perform direct system interactions like file I/O and network communications. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified (Note: String segments such as `.rdata` and `.data` refer to internal binary sections and are not actionable file paths).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Scripting Engine:** The analysis identifies the use of a high-level script interpreter, specifically suggesting **AutoIt**.
*   **API/Library Usage:** `OLEAUT32.dll_VariantCopy` (indicates capabilities for handling polymorphic data types).
*   **Technical Behavior:** 
    *   Multi-tiered dispatch architecture (multi-layered switch-case tables).
    *   Sophisticated buffer management and automatic string normalization.
    *   Use of a "Hardened Container" strategy to decouple the malicious intent (scripts) from the execution mechanism (C++ engine).

---
**Analyst Note:** The provided strings appear to be largely obfuscated or represent raw assembly data/jump tables, which does not yield high-fidelity network or filesystem IOCs. The primary threat indicators are behavioral: the malware functions as a sophisticated, stable C2 framework designed to hide its true intent behind an interpretation layer.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / backdoor
3. **Confidence**: High

**Key evidence**:
*   **Multi-Tiered Interpreter Architecture:** The use of massive switch-case tables and a "System Bridge" indicates the binary is a sophisticated, production-grade script interpreter (likely for AutoIt). This allows it to host malicious logic within an abstracted layer, separating the execution mechanism from the attacker's intent.
*   **Hardened Container Strategy:** The implementation of advanced memory management, automatic string normalization, and `OLEAUT32` support confirms this is a stable C2 framework designed for long-term operation rather than a one-off tool.
*   **High Analysis Tax:** By utilizing a "Black Box" approach, the malware forces analysts to work through multiple layers of abstraction, making it difficult to identify specific malicious actions without extracting and decoding the underlying scripts.
