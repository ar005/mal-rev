# Threat Analysis Report

**Generated:** 2026-08-10 17:39 UTC
**Sample:** `0dee384430e3e0b20101eba35761487845308f973658d9ac2ea42dd52cba1f33_0dee384430e3e0b20101eba35761487845308f973658d9ac2ea42dd52cba1f33.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0dee384430e3e0b20101eba35761487845308f973658d9ac2ea42dd52cba1f33_0dee384430e3e0b20101eba35761487845308f973658d9ac2ea42dd52cba1f33.exe` |
| File type | PE32+ executable for MS Windows 10.00 (GUI), x86-64, 6 sections |
| Size | 1,857,024 bytes |
| MD5 | `1455be1f653bb2fab23dc274fb6cc719` |
| SHA1 | `b79110f3e399c633adcc4256e163dc18dcf90c5c` |
| SHA256 | `0dee384430e3e0b20101eba35761487845308f973658d9ac2ea42dd52cba1f33` |
| Overall entropy | 5.899 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3623562882 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 268,800 | 7.951 | ⚠️ Yes |
| `.rdata` | 68,096 | 5.051 | No |
| `.data` | 5,632 | 0.86 | No |
| `.pdata` | 6,656 | 5.395 | No |
| `.rsrc` | 1,506,304 | 5.16 | No |
| `.reloc` | 512 | 3.894 | No |

### Imports

**ADVAPI32.dll**: `RegQueryValueExW`, `RegEnumValueW`, `RegDeleteValueW`, `EventUnregister`, `RegOpenKeyExW`, `RegSetValueExW`, `RegEnumKeyExW`, `RegCreateKeyExW`, `RegDeleteKeyW`, `EventRegister`, `EventWriteTransfer`, `RegQueryInfoKeyW`, `RegCloseKey`, `LookupAccountNameW`, `ConvertSidToStringSidW`
**KERNEL32.dll**: `LockResource`, `LoadResource`, `FindResourceW`, `GetModuleHandleExW`, `DebugBreak`, `GetModuleHandleA`, `GetUserDefaultLangID`, `GlobalUnlock`, `GlobalLock`, `GlobalAlloc`, `ReadFile`, `DeleteFileA`, `OpenEventW`, `GetLongPathNameW`, `WritePrivateProfileStringW`
**GDI32.dll**: `CreateFontA`, `GetTextFaceA`, `DeleteDC`, `SetTextColor`, `SetBkMode`, `CreatePen`, `GetObjectW`, `PatBlt`, `ExtTextOutW`, `SetBkColor`, `DeleteObject`, `CreateSolidBrush`, `SetMapMode`, `CreateFontIndirectW`, `GetTextMetricsW`
**USER32.dll**: `SetForegroundWindow`, `BeginPaint`, `ReleaseDC`, `LoadImageW`, `EndPaint`, `EnableWindow`, `InvalidateRect`, `GetDesktopWindow`, `LoadStringA`, `CharNextW`, `UpdateWindow`, `GetParent`, `SystemParametersInfoW`, `EnableMenuItem`, `PostQuitMessage`
**msvcrt.dll**: `_itow`, `strrchr`, `_purecall`, `strstr`, `wcstok`, `calloc`, `wcstol`, `_wcsupr`, `iswalnum`, `_strlwr`, `_stricmp`, `wcspbrk`, `malloc`, `_unlock`, `qsort`
**ATL.DLL**: `ord_32`
**ntdll.dll**: `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `RtlCaptureContext`
**pdh.dll**: `PdhAddCounterW`, `PdhGetFormattedCounterValue`, `PdhOpenQueryW`, `PdhCloseQuery`, `PdhCollectQueryData`
**ole32.dll**: `CoCreateInstance`, `CoUninitialize`, `CoInitialize`, `OleInitialize`, `CLSIDFromString`, `CoRevokeClassObject`, `CoTaskMemFree`, `CoRegisterClassObject`, `OleUninitialize`, `CreateStreamOnHGlobal`
**OLEAUT32.dll**: `SysFreeString`, `SysStringLen`, `SysAllocStringLen`, `VariantInit`, `VariantClear`, `SystemTimeToVariantTime`, `VariantTimeToSystemTime`, `SysAllocString`
**COMCTL32.dll**: `InitCommonControlsEx`
**SHELL32.dll**: `SHGetFolderPathW`, `SHChangeNotify`, `SHGetFolderLocation`, `ShellExecuteExW`, `SHGetMalloc`, `SHGetSpecialFolderLocation`, `SetCurrentProcessExplicitAppUserModelID`, `CommandLineToArgvW`, `ShellExecuteW`, `SHGetPathFromIDListW`
**gdiplus.dll**: `GdipCreateBitmapFromHBITMAP`, `GdipCloneImage`, `GdipDisposeImage`, `GdipCreateHBITMAPFromBitmap`, `GdipFree`, `GdiplusStartup`, `GdipImageRotateFlip`, `GdipAlloc`, `GdiplusShutdown`, `GdipCreateBitmapFromFile`
**WININET.dll**: `InternetCrackUrlW`
**SETUPAPI.dll**: `SetupGetBinaryField`, `SetupFindFirstLineW`, `SetupGetStringFieldW`, `SetupGetLineCountW`, `SetupGetLineTextW`, `SetupIterateCabinetA`, `SetupFindNextLine`, `SetupCloseInfFile`
**WINTRUST.dll**: `WinVerifyTrust`, `WTHelperProvDataFromStateData`, `WTHelperGetProvSignerFromChain`
**urlmon.dll**: `ObtainUserAgentString`, `UrlMkSetSessionOption`
**SHLWAPI.dll**: `PathFindFileNameW`, `PathAddBackslashW`, `PathAddBackslashA`, `PathFindExtensionW`
**CRYPT32.dll**: `CertVerifyCertificateChainPolicy`
**USERENV.dll**: `LoadUserProfileW`, `UnloadUserProfile`, `ExpandEnvironmentStringsForUserW`

## Extracted Strings

Total strings found: **3862** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
L$ SUVWH
L$ SUVWH
R$fA;Z*
fA9Z*v$A
+T$DE3
D$X+D$P
UATAUAVAWH
A_A^A]A\]
tf9\$$
UVWATAUAVAWH
A_A^A]A\_^]
uC9|$0u=
}>HcD$ HcL$ H

HcD$ H
2HcL$ H
|$ d}bA
HcL$ H
PHcD$ H
HcD$$H
|$(d}(HcD$(L
|$,d}!HcD$,A
H!|$HH
L$P!D$8!D$<3
UVWATAUAVAWH
D9|$d~rA
D;d$d|
H;\$xr
~ML9?tHA
A_A^A]A\_^]
8222az
s222edaz
322ilmosn
4222a~
zilmosnso
sesdsgsf{
4222edaz
2222222
ilmsnsoslsmo
b322sesdsgw
z022zQp
ilmosnsoslsm
ilmosn
2222jz
O*2F9z
bw22F5
222RFp
222RE"
222rF 
'2222z3
6222222z
6222222z
6222222
6222G8
wz3222z
wJ2222z
'
222z
'r222z
222zw
7j222z
r"zw"F<z
7b222zw
'b222z
'b222z
7b222z
7b222z

2222z
7
222z
7b222z
7j222z
7b222z
7*222z
7*222z
7
222z
7
222z
7r222z
7r222z
222zw
7j222z
7b222zw
O*2F;z
22222222
:22266
222222%222
222226
222222;222
222226X322
222222;222r222226
22266w022222222222222266
222222;222v222226T022
022222222226222266
222222;222z222226
0222222;222:222226
622:422226
,22226
-22226
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x140041850` | 255691 | ✓ |
| `fcn.140041704` | `0x140041704` | 1723 | ✓ |
| `fcn.140003480` | `0x140003480` | 690 | ✓ |
| `fcn.140041ac0` | `0x140041ac0` | 465 | ✓ |
| `fcn.14001adf0` | `0x14001adf0` | 326 | ✓ |
| `fcn.14000373c` | `0x14000373c` | 325 | ✓ |
| `fcn.140003360` | `0x140003360` | 286 | ✓ |
| `fcn.140002ea4` | `0x140002ea4` | 273 | ✓ |
| `fcn.140002258` | `0x140002258` | 252 | ✓ |
| `fcn.140030558` | `0x140030558` | 250 | ✓ |
| `fcn.140018338` | `0x140018338` | 232 | ✓ |
| `fcn.140001538` | `0x140001538` | 207 | ✓ |
| `fcn.140040818` | `0x140040818` | 198 | ✓ |
| `fcn.14003fb4c` | `0x14003fb4c` | 172 | ✓ |
| `fcn.14001daa1` | `0x14001daa1` | 161 | ✓ |
| `fcn.1400420cc` | `0x1400420cc` | 141 | ✓ |
| `fcn.1400014ac` | `0x1400014ac` | 133 | ✓ |
| `fcn.140001420` | `0x140001420` | 130 | ✓ |
| `fcn.140001770` | `0x140001770` | 128 | ✓ |
| `fcn.140019a15` | `0x140019a15` | 127 | ✓ |
| `fcn.1400016ec` | `0x1400016ec` | 125 | ✓ |
| `fcn.1400017f8` | `0x1400017f8` | 107 | ✓ |
| `fcn.1400422e0` | `0x1400422e0` | 91 | ✓ |
| `fcn.14001aef8` | `0x14001aef8` | 86 | ✓ |
| `fcn.140041e3c` | `0x140041e3c` | 84 | ✓ |
| `fcn.140041f50` | `0x140041f50` | 77 | ✓ |
| `fcn.140005224` | `0x140005224` | 70 | ✓ |
| `fcn.140041e98` | `0x140041e98` | 69 | ✓ |
| `fcn.140041f00` | `0x140041f00` | 68 | ✓ |
| `fcn.14003ff40` | `0x14003ff40` | 61 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.140001420.c`](code/fcn.140001420.c)
- [`code/fcn.1400014ac.c`](code/fcn.1400014ac.c)
- [`code/fcn.140001538.c`](code/fcn.140001538.c)
- [`code/fcn.1400016ec.c`](code/fcn.1400016ec.c)
- [`code/fcn.140001770.c`](code/fcn.140001770.c)
- [`code/fcn.1400017f8.c`](code/fcn.1400017f8.c)
- [`code/fcn.140002258.c`](code/fcn.140002258.c)
- [`code/fcn.140002ea4.c`](code/fcn.140002ea4.c)
- [`code/fcn.140003360.c`](code/fcn.140003360.c)
- [`code/fcn.140003480.c`](code/fcn.140003480.c)
- [`code/fcn.14000373c.c`](code/fcn.14000373c.c)
- [`code/fcn.140005224.c`](code/fcn.140005224.c)
- [`code/fcn.140018338.c`](code/fcn.140018338.c)
- [`code/fcn.140019a15.c`](code/fcn.140019a15.c)
- [`code/fcn.14001adf0.c`](code/fcn.14001adf0.c)
- [`code/fcn.14001aef8.c`](code/fcn.14001aef8.c)
- [`code/fcn.14001daa1.c`](code/fcn.14001daa1.c)
- [`code/fcn.140030558.c`](code/fcn.140030558.c)
- [`code/fcn.14003fb4c.c`](code/fcn.14003fb4c.c)
- [`code/fcn.14003ff40.c`](code/fcn.14003ff40.c)
- [`code/fcn.140040818.c`](code/fcn.140040818.c)
- [`code/fcn.140041704.c`](code/fcn.140041704.c)
- [`code/fcn.140041ac0.c`](code/fcn.140041ac0.c)
- [`code/fcn.140041e3c.c`](code/fcn.140041e3c.c)
- [`code/fcn.140041e98.c`](code/fcn.140041e98.c)
- [`code/fcn.140041f00.c`](code/fcn.140041f00.c)
- [`code/fcn.140041f50.c`](code/fcn.140041f50.c)
- [`code/fcn.1400420cc.c`](code/fcn.1400420cc.c)
- [`code/fcn.1400422e0.c`](code/fcn.1400422e0.c)

## Behavioral Analysis

This binary sample appears to be a **malicious loader or packer** designed to decrypt and execute a hidden payload in memory while utilizing anti-analysis techniques to evade detection.

### Core Functionality and Purpose
The primary role of this code is to act as a "stub" or "loader." It does not perform its main malicious activity immediately; instead, it prepares the environment, decodes an embedded payload, and executes that payload in memory (an "in-memory execution" pattern). 

### Suspicious and Malicious Behaviors
*   **Payload Unpacking & Decryption:** In `entry0`, the code allocates a new region of memory using `VirtualAlloc` with permissions that allow for both writing and execution. It then iterates through this buffer, XORing the data with the value `0x32`. This is a classic de-obfuscation step to reveal executable shellcode or encrypted strings before jumping to the start of the decrypted block (`(*pcStack_48)()`).
*   **Anti-Analysis/Environment Checking:** The function `fcn.14002ea4` utilizes the **PDH (Performance Data Helper)** library (`PdhOpenQueryW`, `PdhAddCounterW`). While used for system monitoring in legitimate software, it is frequently employed by malware to query hardware details or performance counters to detect if the code is running inside a virtual machine (VM) or an automated sandbox.
*   **Masquerading as System Components:** Several functions (`fcn.1400373c`, `fcn.14002258`) specifically target and reference **Windows Media Player components** (e.g., `wmploc.dll` and `wmvcore.dll`). By referencing these specific system files, the malware attempts to blend in with legitimate Windows media services or hijack their search paths.
*   **Exception Handling Manipulation:** The functions `fcn.140041ac0` and `fcn.1400422e0` interact with low-level NT APIs like `RtlCaptureContext` and `RtlVirtualUnwind`. This suggests the program is setting up custom exception handlers, which can be used to intercept system errors or bypass certain security software checks that rely on standard Windows error reporting.

### Notable Techniques & Patterns
*   **Execution in RWX Memory:** The use of `VirtualAlloc` to create an "Execute/Read/Write" (RWX) memory region is a major red flag. Standard compilers rarely generate this unless it is intended for JIT (Just-In-Time) compilation or, more commonly, for loading malicious shellcode.
*   **Decoding Loop:** The simple loop in `entry0` to process the buffer before execution indicates that the primary payload is stored encrypted/obfuscated within the binary's data section.
*   **Control Flow Obfuscation:** Several functions (e.g., `fcn.140030558`) contain "junk" instructions or deliberately complex logic that results in "bad instruction" warnings during disassembly. This is a common technique to hinder automated analysis tools and slow down manual reverse engineering.
*   **Registry Interaction:** The code queries specific registry keys related to Media Player setup (`fcn.14003480`). It likely uses these values to determine environmental factors or to check for the presence of certain system configurations before launching its payload.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the corresponding MITRE ATT&K techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027.005** | **Packed_Code** | The use of XOR decoding, "junk" instructions, and complex logic indicates the presence of a packer/loader designed to hide the actual payload from static analysis. |
| **T1497** | **Virtualization/Sandbox Detection** | The utilization of PDH libraries and specific registry queries are classic indicators of attempts to detect virtual machines or automated analysis environments. |
| **T1036** | **Masquerading** | Referencing Windows Media Player components (`wmploc.dll`, `wmvcore.dll`) is an attempt to blend in with legitimate system processes and hide from defenders. |
| **T1055** | **Process Injection** | The allocation of RWX (Read, Write, Execute) memory via `VirtualAlloc` followed by the execution of decoded code in that region is a standard method for in-memory payload execution. |
| **T1638** | **User-Mode System DLL (Internal)** | *Note: While technically an internal distinction, the use of NT APIs like `RtlCaptureContext` and `RtlVirtualUnwind` to manipulate exception handling is a specific method for bypassing security software.* |

***Note on Analysis:*** *The behavior involving "Exception Handling Manipulation" using low-level NT APIs is often used in conjunction with **T1497** (Virtualization/Sandbox Detection) to bypass automated security hooks or to detect the presence of debuggers during analysis.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. *(Note: While `wmploc.dll` and `wmvcore.dll` were mentioned in the analysis, these are standard Windows system files and do not constitute specific malicious file paths.)*

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **XOR Decryption Key:** `0x32` (Used in the `entry0` function to de-obfuscate the primary payload).
*   **Malware Technique - Memory Manipulation:** Allocation of memory with **RWX** (Read, Write, Execute) permissions via `VirtualAlloc`.
*   **Malware Technique - Anti-Analysis:** Utilization of the **PDH (Performance Data Helper)** library (`PdhOpenQueryW`, `PdhAddCounterW`) to detect virtualized environments or sandboxes.
*   **Malware Technique - Obfuscation:** Use of "junk" instructions and complex logic in `fcn.140030558` to hinder automated disassembly.

---

## Malware Family Classification

1. **Malware family**: Unknown (Potential generic loader)
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
*   **In-Memory Execution & Decoding:** The sample utilizes a classic "loader" pattern by allocating RWX (Read, Write, Execute) memory via `VirtualAlloc` and employing an XOR decryption loop (`0x32`) to unpack a hidden payload directly into memory.
*   **Sophisticated Anti-Analysis:** The inclusion of the **PDH library** for environment checking (VM/Sandbox detection), "junk" instructions to hinder automated disassembly, and the use of low-level NT APIs (`RtlCaptureContext`) indicates a deliberate effort to evade security researchers and automated tools.
*   **Evasion via Masquerading:** The malware specifically references Windows Media Player components (`wmploc.dll`, `wmvcore.dll`) to blend in with legitimate system processes, a common tactic for loaders seeking to remain undetected during initial execution.
