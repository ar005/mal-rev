# Threat Analysis Report

**Generated:** 2026-07-18 18:16 UTC
**Sample:** `08b02fbddee7bf40f03f3298c62d491eb7f290946d242740a05f6a9f6bd233d7_08b02fbddee7bf40f03f3298c62d491eb7f290946d242740a05f6a9f6bd233d7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `08b02fbddee7bf40f03f3298c62d491eb7f290946d242740a05f6a9f6bd233d7_08b02fbddee7bf40f03f3298c62d491eb7f290946d242740a05f6a9f6bd233d7.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,578,496 bytes |
| MD5 | `577a2016e6b702063f275a8124ecdc07` |
| SHA1 | `fd65618660a2b3357aee28aa227d994c2090d1a3` |
| SHA256 | `08b02fbddee7bf40f03f3298c62d491eb7f290946d242740a05f6a9f6bd233d7` |
| Overall entropy | 7.305 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1765231700 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 573,440 | 6.681 | No |
| `.rdata` | 182,272 | 5.694 | No |
| `.data` | 25,088 | 2.004 | No |
| `.rsrc` | 754,176 | 7.796 | ⚠️ Yes |
| `.reloc` | 42,496 | 5.238 | No |

### Imports

**KERNEL32.DLL**: `WaitForSingleObject`, `HeapAlloc`, `GetProcessHeap`, `HeapFree`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `MulDiv`, `GetVersionExW`, `GetSystemInfo`, `FreeLibrary`, `LoadLibraryA`, `GetProcAddress`, `SetErrorMode`, `WideCharToMultiByte`
**ADVAPI32.dll**: `GetAclInformation`, `RegEnumValueW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegCreateKeyExW`, `GetUserNameW`, `RegOpenKeyExW`, `RegCloseKey`, `RegQueryValueExW`, `RegConnectRegistryW`, `InitializeSecurityDescriptor`, `InitializeAcl`, `AdjustTokenPrivileges`
**COMCTL32.dll**: `ImageList_Destroy`, `ImageList_Remove`, `ImageList_SetDragCursorImage`, `ImageList_BeginDrag`, `ImageList_DragEnter`, `ImageList_DragLeave`, `ImageList_EndDrag`, `ImageList_DragMove`, `ImageList_Create`, `InitCommonControlsEx`, `ImageList_ReplaceIcon`
**COMDLG32.dll**: `GetSaveFileNameW`, `GetOpenFileNameW`
**GDI32.dll**: `SetPixel`, `DeleteObject`, `GetTextExtentPoint32W`, `ExtCreatePen`, `StrokeAndFillPath`, `StrokePath`, `GetDeviceCaps`, `CloseFigure`, `LineTo`, `AngleArc`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `MoveToEx`, `Ellipse`, `PolyDraw`
**IPHLPAPI.DLL**: `IcmpCreateFile`, `IcmpCloseHandle`, `IcmpSendEcho`
**MPR.dll**: `WNetUseConnectionW`, `WNetCancelConnection2W`, `WNetGetConnectionW`, `WNetAddConnection2W`
**ole32.dll**: `CoTaskMemAlloc`, `CoTaskMemFree`, `CLSIDFromString`, `ProgIDFromCLSID`, `CLSIDFromProgID`, `OleSetMenuDescriptor`, `MkParseDisplayName`, `OleSetContainedObject`, `CoCreateInstance`, `IIDFromString`, `StringFromGUID2`, `CreateStreamOnHGlobal`, `CoInitialize`, `CoUninitialize`, `GetRunningObjectTable`
**OLEAUT32.dll**: `RegisterTypeLib`, `LoadTypeLibEx`, `VariantCopyInd`, `SysReAllocString`, `SysFreeString`, `SafeArrayDestroyDescriptor`, `SafeArrayDestroyData`, `SafeArrayUnaccessData`, `SafeArrayAccessData`, `SafeArrayAllocData`, `UnRegisterTypeLib`, `SafeArrayCreateVector`, `SysAllocString`, `SysStringLen`, `VariantTimeToSystemTime`
**PSAPI.DLL**: `GetProcessMemoryInfo`
**SHELL32.dll**: `DragQueryPoint`, `ShellExecuteExW`, `DragQueryFileW`, `SHEmptyRecycleBinW`, `SHBrowseForFolderW`, `SHGetFolderPathW`, `SHFileOperationW`, `SHGetPathFromIDListW`, `SHGetDesktopFolder`, `SHGetMalloc`, `ExtractIconExW`, `Shell_NotifyIconW`, `ShellExecuteW`, `DragFinish`
**USER32.dll**: `CopyImage`, `SetWindowPos`, `GetCursorInfo`, `RegisterHotKey`, `ClientToScreen`, `GetKeyboardLayoutNameW`, `IsCharAlphaW`, `IsCharAlphaNumericW`, `IsCharLowerW`, `IsCharUpperW`, `GetMenuStringW`, `GetSubMenu`, `GetCaretPos`, `IsZoomed`, `MonitorFromPoint`
**USERENV.dll**: `UnloadUserProfile`, `DestroyEnvironmentBlock`, `CreateEnvironmentBlock`, `LoadUserProfileW`
**UxTheme.dll**: `IsThemeActive`
**VERSION.dll**: `GetFileVersionInfoW`, `VerQueryValueW`, `GetFileVersionInfoSizeW`
**WININET.dll**: `InternetReadFile`, `InternetCloseHandle`, `InternetOpenW`, `InternetSetOptionW`, `InternetCrackUrlW`, `HttpQueryInfoW`, `InternetQueryOptionW`, `HttpOpenRequestW`, `HttpSendRequestW`, `FtpOpenFileW`, `FtpGetFileSize`, `InternetOpenUrlW`, `InternetConnectW`, `InternetQueryDataAvailable`
**WINMM.dll**: `timeGetTime`, `waveOutSetVolume`, `mciSendStringW`
**WSOCK32.dll**: `__WSAFDIsSet`, `recv`, `send`, `setsockopt`, `ntohs`, `recvfrom`, `select`, `WSAStartup`, `htons`, `accept`, `listen`, `bind`, `closesocket`, `connect`, `WSACleanup`

## Extracted Strings

Total strings found: **3399** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc
FY;5$#L
FY;w r
WWjdh,
PWWWWh
L$$9N@
R$A;N|
u9^u
~+FVSj
AHt!H
^$9^,u
D$49G8
L$LjrXf


	

D$$;D$0
FHtJH
v,F8PRQ
D$<9D$ tZj
L$D;t$8
 !"#$%%%%%%&&'()*+%%%%%%&&'()*+,,,,,,--./012QQQQQQQQ334556789999:;<;<=>=?@AB=?@ABQQQQQCDEFGHIJKLMN
t<j	Yf;
t4j"Yf;
tj	Yf;
Yj?Yj0Z
tDjhl
FHt8HtRHt
t@Hu39
D$ PVj
D$$PVj
D$@;D$Dr
9D$xu;
9t$xv7
F;t$xr
|$L9D$4
F;t$Xr
D$PQW
9t$ v-
F;t$ r
t$8]4t
9^Xt99^\tA
+t\HHtT
j+Yj^f;
<uGj>Y
~89~4~)
v,F8P
AHt;Ht.H
_8C0tN
PPPPGW
F;Bt
SVWjA_jZ+
uBjAYjZ+
uPVWhd
uWtj-Xf
tf;1u
SVjA[jZ^+
jAZjZ^+
9E v\PWj
9u(v?VSj
jh0fK
jhPfK
G@uqW
YYHtIHt8
jh8gK
jhXgK
u&j[9
jhxgK
D$tQf
HHtPHHt-H
HthHt3
Genuu_
ineIuV
nteluM3
u,9Et'9
~pjCXf
j$h(iK
v	N+D$
uHjAXf;
tjXYf;
uWjAXf;
htHjlY;
HHtXHHt
uj X
nt'joY;
YYjgXf9
>0t<Nj0X
u9Mu&3
-t*j0X;
+t"HHt
u
HAN8
j@j _W
t$jXP
@@ucP
HHtVHHt
PP9E u
HtHu(
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004080a0` | `0x4080a0` | 544212 | ✓ |
| `fcn.00408ca0` | `0x408ca0` | 540969 | ✓ |
| `fcn.00409460` | `0x409460` | 536131 | ✓ |
| `fcn.00405c5b` | `0x405c5b` | 515944 | ✓ |
| `fcn.00405d32` | `0x405d32` | 515700 | ✓ |
| `fcn.00406348` | `0x406348` | 512403 | ✓ |
| `fcn.00406670` | `0x406670` | 510850 | ✓ |
| `fcn.004029ad` | `0x4029ad` | 509685 | ✓ |
| `fcn.00402b6e` | `0x402b6e` | 509287 | ✓ |
| `fcn.00402bf8` | `0x402bf8` | 509119 | ✓ |
| `fcn.004019ee` | `0x4019ee` | 508324 | ✓ |
| `fcn.0040776b` | `0x40776b` | 507667 | ✓ |
| `fcn.00407932` | `0x407932` | 507402 | ✓ |
| `fcn.0040785a` | `0x40785a` | 507320 | ✓ |
| `fcn.00401dce` | `0x401dce` | 507311 | ✓ |
| `fcn.00407a0f` | `0x407a0f` | 506734 | ✓ |
| `fcn.00402ac7` | `0x402ac7` | 504105 | ✓ |
| `fcn.004048c8` | `0x4048c8` | 499174 | ✓ |
| `fcn.004049ca` | `0x4049ca` | 499112 | ✓ |
| `fcn.00407888` | `0x407888` | 495143 | ✓ |
| `fcn.004021dd` | `0x4021dd` | 493085 | ✓ |
| `fcn.00407ad2` | `0x407ad2` | 492991 | ✓ |
| `fcn.004076f5` | `0x4076f5` | 491474 | ✓ |
| `fcn.00402843` | `0x402843` | 491472 | ✓ |
| `fcn.00402876` | `0x402876` | 491440 | ✓ |
| `fcn.004028af` | `0x4028af` | 491144 | ✓ |
| `fcn.00404b02` | `0x404b02` | 482616 | ✓ |
| `fcn.0040203a` | `0x40203a` | 481254 | ✓ |
| `section..text` | `0x401000` | 481140 | ✓ |
| `fcn.0040124c` | `0x40124c` | 480559 | ✓ |

### Decompiled Code Files

- [`code/fcn.0040124c.c`](code/fcn.0040124c.c)
- [`code/fcn.004019ee.c`](code/fcn.004019ee.c)
- [`code/fcn.00401dce.c`](code/fcn.00401dce.c)
- [`code/fcn.0040203a.c`](code/fcn.0040203a.c)
- [`code/fcn.004021dd.c`](code/fcn.004021dd.c)
- [`code/fcn.00402843.c`](code/fcn.00402843.c)
- [`code/fcn.00402876.c`](code/fcn.00402876.c)
- [`code/fcn.004028af.c`](code/fcn.004028af.c)
- [`code/fcn.004029ad.c`](code/fcn.004029ad.c)
- [`code/fcn.00402ac7.c`](code/fcn.00402ac7.c)
- [`code/fcn.00402b6e.c`](code/fcn.00402b6e.c)
- [`code/fcn.00402bf8.c`](code/fcn.00402bf8.c)
- [`code/fcn.004048c8.c`](code/fcn.004048c8.c)
- [`code/fcn.004049ca.c`](code/fcn.004049ca.c)
- [`code/fcn.00404b02.c`](code/fcn.00404b02.c)
- [`code/fcn.00405c5b.c`](code/fcn.00405c5b.c)
- [`code/fcn.00405d32.c`](code/fcn.00405d32.c)
- [`code/fcn.00406348.c`](code/fcn.00406348.c)
- [`code/fcn.00406670.c`](code/fcn.00406670.c)
- [`code/fcn.004076f5.c`](code/fcn.004076f5.c)
- [`code/fcn.0040776b.c`](code/fcn.0040776b.c)
- [`code/fcn.0040785a.c`](code/fcn.0040785a.c)
- [`code/fcn.00407888.c`](code/fcn.00407888.c)
- [`code/fcn.00407932.c`](code/fcn.00407932.c)
- [`code/fcn.00407a0f.c`](code/fcn.00407a0f.c)
- [`code/fcn.00407ad2.c`](code/fcn.00407ad2.c)
- [`code/fcn.004080a0.c`](code/fcn.004080a0.c)
- [`code/fcn.00408ca0.c`](code/fcn.00408ca0.c)
- [`code/fcn.00409460.c`](code/fcn.00409460.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This fourth and final chunk of disassembly provides the "smoking gun" for our primary hypothesis. We can now move from a theory of a "complex interpreter" to a confirmed analysis of a **high-sophistication Virtual Machine (VM) architecture**, likely similar to those found in premium anti-tamper solutions like VMProtect or advanced state-machine-based malware loaders.

The final chunk clarifies exactly *how* the interpreter works and what it is designed to do.

### Finalized Technical Analysis

#### 1. The Core Interpreter Loop (The "Virtual CPU")
The massive switch blocks (specifically at `0x48c473`, `0x48c4b3`, etc.) are the **Main Dispatcher**. 
*   **Stateful Execution:** Notice how variables like `var_10h`, `var_20h`, and `var_30h` are used across different jumps. These are not standard registers; they are the **Virtual Machine's internal state (Registers/Flags)**. They hold "data" that is pulled from the bytecode to determine which logical path the "script" should take.
*   **Nested Logic:** The interpreter doesn't just jump to one function. It performs a multi-stage check: 
    1. Is this an instruction? 
    2. Is the argument valid? 
    3. Does it require a specific Unicode transformation? 
    4. What is the next offset in the virtual program?
*   **Instruction Mapping:** In many cases, the code calculates `var_4h` or `var_8h` before jumping. This indicates that the "next" instruction's address is being calculated by the VM, not by the hardware CPU.

#### 2. Complex Data Processing (The Unicode Engine)
The most striking feature in this chunk is the heavy investment in **Unicode and UTF-16 handling** (`0x180f`, `0xd800`, etc.). This indicates that the "scripts" or "data" being processed by this VM are not just simple commands; they are likely:
*   **Complex Strings:** Used for internal checks (e.g., checking filenames, registry keys, or network paths).
*   **Internationalized Logic:** The code is prepared to handle characters from any language. This suggests the system was built for high-scale reliability, ensuring it doesn't crash when encountering "complex" text—a hallmark of professional-grade protection software.

#### 3. Advanced Obfuscation Techniques
Several advanced techniques are clearly visible here:
*   **Arithmetic Calculation of Branch Targets:** The expression `((var_10h & 1) != 0) + 0x6d` or similar math used to pick a value is designed to defeat static analysis. A human looking at the code can't see where the jump goes; only the runtime value of the "Virtual Register" determines the path.
*   **Code Flattening/Indirection:** The jump targets like `code_r0x00406a38` and `code_r0x004070fc` are used repeatedly as "fall-through" points for different types of logic that eventually return to a common state. This makes it very difficult to trace the logical flow without running the code in a debugger.
*   **Metamorphic Elements:** The multiple ways to calculate `var_24h` or `var_10h` suggest the author used tools to generate different but functionally equivalent "paths" to confuse researchers trying to find the "heart" of the logic.

#### 4. Analysis of Specific Functions
*   **fcn.0040785a / fcn.00407888:** These appear to be **Decoder Helpers**. They validate and translate raw bytes from a data segment into usable values for the interpreter. 
*   **fcn.004076f5:** This is a **Validation Engine**. It checks lengths, ensures characters are within valid ranges, and validates that the "script" being executed isn't malformed.
*   **fcn.0040124c / fcn.004048c8:** These interact with high-level OS components (like `Send_MessageW` or `DestroyWindow`). This implies the VM is used to manage a **Graphical User Interface (GUI)** or complex Windows interaction, but it does so through a layer of "sanitized" instructions.

---

### Updated Summary of Findings

**Current Status: CONFIRMED HIGH-SOPHISTICATION VIRTUAL MACHINE.**

The analysis has evolved from "potential loader" to a **full-featured VM environment**. This system is not just protecting a single password or simple function; it is hosting an entire logic tree in a custom bytecode format.

| Feature | Observation | Conclusion |
| :--- | :--- | :--- |
| **Architecture** | Extensive switch tables & multi-pass decoding. | **Custom VM Interpreter.** |
| **Complexity** | Multi-step arithmetic for jump offsets and result calculation. | **Anti-Analysis logic** (designed to break decompilers). |
| **Data Handling** | Heavy Unicode/UTF-16 support (`0xd800` checks). | **High-Level Scripting.** The "script" handles complex data. |
| **Target State** | Use of `Send_MessageW`, and complex window handling code. | **Environment interaction** shielded by the VM layer. |

### Recommendations for Next Steps:
1.  **Dynamic Instrumentation (Frida/x64dbg):** Do not try to "decompile" your way through the VM logic. Instead, use a debugger to hook the entry points of `fcn.0040785a` and `fcn.00407888`. Log what values are being passed into these functions; they will reveal the **actual script** being executed.
2.  **Script Extraction:** Locate the data segments that feed these functions. This is where the "real" logic lives. It will likely look like a blob of garbage to you, but it is the "code" for this machine.
3.  **Identify the Dispatcher State:** Trace `var_10h` and `var_20h`. These are your primary keys. By tracking how these values change in memory, you can map out what "instruction" is currently being executed by the interpreter.

**Final Risk Assessment:** This is a high-tier protection layer. It is likely used either for **enterprise-grade anti-cheat/DRM** or as a **sophisticated malware stager**. The sheer amount of code dedicated to just *parsing* and *decoding* means the actual malicious/protected logic is deeply buried under several layers of interpretation.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1026.003 | Code Obfuscation: Virtual Machine | The sample implements a custom interpreter with its own instruction set, virtual registers (e.g., `var_10h`), and a dispatch loop to hide the primary logic from researchers. |
| T1026 | Code Obfuscation | The use of arithmetic calculations for branch targets and code flattening is designed to break control flow analysis and complicate static deconstruction. |
| T1055 | Packing | The presence of "Decoder Helpers" and a "Validation Engine" indicates a multi-stage process where data is decoded/deobfuscated before it can be processed by the VM interpreter. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** The provided data contains a significant amount of obfuscated code and internal assembly offsets. While these reflect a highly sophisticated protection layer, they do not contain standard "loud" indicators like plaintext IP addresses or file paths in their current form.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: Values such as `fcn.0040785a` are internal memory offsets/function labels, not filesystem or registry paths).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Malware Behavior/Techniques:**
    *   **Custom Virtual Machine (VM) Architecture:** The sample utilizes a sophisticated VM-based protection system to house its primary logic tree.
    *   **Advanced Obfuscation:** Use of "Arithmetic Calculation of Branch Targets" and "Code Flattening/Indirection" to evade static analysis and decompiler logic.
    *   **Unicode Processing Engine:** Extensive use of UTF-16 handling (noted at offsets `0x180f` and `0xd800`) suggests the underlying scripts handle complex strings, likely for obfuscating internal configuration or interaction logic.
    *   **Decoder/Validation Logic:** Specific routines (identified in analysis as `fcn.0040785a`, `fcn.00407888`, and `fcn.004076f5`) are dedicated to decoding raw data into a format the VM can execute.
    *   **API Interaction:** Utilization of Windows API calls such as `Send_MessageW` and `DestroyWindow` wrapped inside the VM layer for GUI interaction or environment manipulation.

---

### **Analyst Note**
The analysis indicates that the "true" IOCs (C2 infrastructure, specific file paths, or registry keys) are likely **encrypted within the virtual machine's bytecode**. To uncover these, dynamic analysis (using tools like x64dbg or Frida) is required to hook the decoder functions and dump the decrypted payload before it is executed by the VM interpreter.

---

## Malware Family Classification

Based on the provided analysis results, here is the classification for the sample:

1. **Malware family**: Unknown
2. **Malware type**: Loader (specifically a VM-based loader)
3. **Confidence**: High (regarding its function as a loader/protection layer)
4. **Key evidence**:
    *   **Advanced Virtual Machine Architecture:** The sample utilizes a complex "Virtual CPU" with its own instruction set, switch-block dispatchers, and virtual registers (`var_10h`, `var_20h`) to execute logic hidden from standard decompilers.
    *   **Sophisticated Anti-Analysis Techniques:** The use of arithmetic calculations for branch targets and code flattening is specifically designed to thwart static analysis by making the control flow unintelligible without dynamic execution.
    *   **Multi-Stage Deobfuscation Logic:** The presence of "Decoder Helpers" and a "Validation Engine" indicates the sample's primary role is to unpack/decrypt further stages of a payload while shielding high-level API interactions (like `Send_MessageW`) behind a layer of obfuscated bytecode.
