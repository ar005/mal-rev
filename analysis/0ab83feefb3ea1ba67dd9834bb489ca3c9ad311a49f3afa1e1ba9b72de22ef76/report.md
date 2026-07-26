# Threat Analysis Report

**Generated:** 2026-07-25 13:47 UTC
**Sample:** `0ab83feefb3ea1ba67dd9834bb489ca3c9ad311a49f3afa1e1ba9b72de22ef76_0ab83feefb3ea1ba67dd9834bb489ca3c9ad311a49f3afa1e1ba9b72de22ef76.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ab83feefb3ea1ba67dd9834bb489ca3c9ad311a49f3afa1e1ba9b72de22ef76_0ab83feefb3ea1ba67dd9834bb489ca3c9ad311a49f3afa1e1ba9b72de22ef76.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 4 sections |
| Size | 3,185,152 bytes |
| MD5 | `b3a00a3f8432a34f459614aa5dce55ee` |
| SHA1 | `43da4180926c5fdfcc598b5fab2aa29d1ab8a71e` |
| SHA256 | `0ab83feefb3ea1ba67dd9834bb489ca3c9ad311a49f3afa1e1ba9b72de22ef76` |
| Overall entropy | 7.998 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1780656247 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 12,800 | 6.411 | No |
| `.rdata` | 21,504 | 5.125 | No |
| `.pdata` | 1,024 | 2.526 | No |
| `.rsrc` | 3,148,800 | 8.0 | ⚠️ Yes |

### Imports

**KERNEL32.dll**: `FindFirstFileExA`, `ConnectNamedPipe`, `OpenSemaphoreA`, `CloseHandle`, `FindClose`, `GetProcessId`, `QueryPerformanceCounter`, `CreateMutexW`, `CreateSemaphoreA`, `GetEnvironmentStrings`, `GetProcessHeap`, `OpenEventW`, `QueryPerformanceFrequency`, `GetModuleFileNameW`, `ReleaseSemaphore`
**USER32.dll**: `UnregisterClassW`, `GetPropW`, `MoveWindow`, `MapVirtualKeyA`, `SetActiveWindow`, `DialogBoxParamA`, `GetClassInfoW`, `CreateCaret`, `RegisterWindowMessageW`, `EndPaint`, `MapVirtualKeyW`, `SendNotifyMessageA`, `GetWindowLongW`, `SetForegroundWindow`, `MessageBoxA`
**GDI32.dll**: `SelectClipRgn`, `CreateCompatibleDC`, `CreateFontA`, `GetPixel`, `CreateSolidBrush`, `CreateFontIndirectW`, `CreateHatchBrush`, `CreateDIBSection`, `DeleteObject`, `SelectObject`, `RoundRect`, `GetDeviceCaps`, `GetBrushOrgEx`, `SetStretchBltMode`, `OffsetRgn`
**ADVAPI32.dll**: `OpenSCManagerA`, `GetSidSubAuthorityCount`, `OpenServiceA`, `RegFlushKey`, `RevertToSelf`, `RegCreateKeyExA`, `RegSetValueExW`, `CreateWellKnownSid`, `StartServiceW`, `RegQueryInfoKeyA`, `RegNotifyChangeKeyValue`, `RegEnumValueA`, `GetUserNameW`
**SHELL32.dll**: `SHChangeNotify`, `SHGetFileInfoA`, `DragAcceptFiles`, `SHGetFolderPathA`, `SHGetDesktopFolder`, `ExtractIconW`, `SHBrowseForFolderA`, `ShellExecuteA`
**ole32.dll**: `CoTaskMemRealloc`, `CoTaskMemFree`, `CoRevokeClassObject`, `OleCreate`, `OleInitialize`, `CoGetClassObject`
**WINMM.dll**: `midiOutOpen`, `waveInStop`, `waveInOpen`, `timeGetDevCaps`, `waveOutOpen`, `PlaySoundW`, `timeGetTime`, `waveInPrepareHeader`
**COMCTL32.dll**: `ImageList_Add`, `PropertySheetW`, `PropertySheetA`, `ord_2`, `ord_3`

### Exports

`Ora_AllocAsset`, `Ora_AllocClient`, `Ora_AllocConfig`, `Ora_AllocContext`, `Ora_AllocDocument`, `Ora_AllocEntry`, `Ora_AllocEntry700`, `Ora_AllocFile`, `Ora_AllocInvoice`, `Ora_AllocProfile`, `Ora_AllocProfile336`, `Ora_AllocProject`, `Ora_AllocRecord`, `Ora_AllocRecord508`, `Ora_AllocReport`, `Ora_AllocSession`, `Ora_AllocTask`, `Ora_ApproveConfig`, `Ora_ApproveContext`, `Ora_ApproveData`, `Ora_ApproveEntry`, `Ora_ApproveInvoice293`, `Ora_ApproveOrder`, `Ora_ApproveOrder507`, `Ora_ApproveProject`, `Ora_ApproveSession`, `Ora_ApproveTask95`, `Ora_CalculateClient`, `Ora_CalculateContext`, `Ora_CalculateData`, `Ora_CalculateDocument`, `Ora_CalculateFile`, `Ora_CalculateHandle`, `Ora_CalculateInvoice`, `Ora_CalculateInvoice240`, `Ora_CalculateProfile`, `Ora_CalculateProject308`, `Ora_CalculateRecord`, `Ora_CalculateReport`, `Ora_CalculateSession`, `Ora_CalculateSession944`, `Ora_CloseAsset`, `Ora_CloseClient`, `Ora_CloseConfig`, `Ora_CloseConfig660`, `Ora_CloseContext873`, `Ora_CloseData240`, `Ora_CloseDocument`, `Ora_CloseEntry`, `Ora_CloseFile`

## Extracted Strings

Total strings found: **7489** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.pdata
@.rsrc
D$,m7'}
oL$ 1t$4H
1\$41t$8Ai
WATAUAVAWH
ukHcA<
 A_A^A]A\_
UATAUAVAWH
tK9\$hvEH
A;BPs'E
A_A^A]A\]
fC9<CtH
|$ AVH
UVWATAWH
 A_A\_^]
 A_A\_^]
 A_A\_^]
USVWATAUAVAWH
A_A^A]A\_^[]
H9|$`tyH9|$PtrH9|$HtkH9|$ptdH9|$xt]H9}
tWH9|$XtPM
USVWAWH
A__^[]
H9\$pu
+D$H=0u
uLIcG<
A__^[]
WD;PP
WAVAWH
 A_A^_
|$ ATAVAWH
 A_A^A\
<9=t!A
yKx+rmLTZSozailc2VpGIwbYUFveq54QHAjEgNn3O7hCtDRfsXM6kB0JdWP81u9/qLuJFYS6vLwtexyD50gHvxyDFYyHUjyDUMK7FYHOvYSDZLAk5TK6lj1feYwAv0XNv0ifeJyRU0uDz076z07A5nrRqLAso2==
GbuPvbXtUp1BzEyHom57enVf5JaHGN2HaGyRa+tHw0NRiE28ZTH0ixgH2YKseLwYFbSzvY2fiGaJzEa0ZxAzpmViGxsHeLNCFpKTFbiCeMgH20AMe0BNz6rMaxdszEyRaxKGUbFAqngfiGaJzEa0
50NRvTVkqxWgeLs=
prwKVy==
.text$mn
.idata$5
.rdata
.rdata$voltmd
.rdata$zzzdbg
.xdata
.edata
.idata
.idata$2
.idata$3
.idata$4
.idata$6
.pdata
.rsrc$01
.rsrc$02
ProjectM2HdbF.exe
Ora_AllocAsset
Ora_AllocClient
Ora_AllocConfig
Ora_AllocContext
Ora_AllocDocument
Ora_AllocEntry
Ora_AllocEntry700
Ora_AllocFile
Ora_AllocInvoice
Ora_AllocProfile
Ora_AllocProfile336
Ora_AllocProject
Ora_AllocRecord
Ora_AllocRecord508
Ora_AllocReport
Ora_AllocSession
Ora_AllocTask
Ora_ApproveConfig
Ora_ApproveContext
Ora_ApproveData
Ora_ApproveEntry
Ora_ApproveInvoice293
Ora_ApproveOrder
Ora_ApproveOrder507
Ora_ApproveProject
Ora_ApproveSession
Ora_ApproveTask95
Ora_CalculateClient
Ora_CalculateContext
Ora_CalculateData
Ora_CalculateDocument
Ora_CalculateFile
Ora_CalculateHandle
Ora_CalculateInvoice
Ora_CalculateInvoice240
Ora_CalculateProfile
Ora_CalculateProject308
Ora_CalculateRecord
Ora_CalculateReport
Ora_CalculateSession
Ora_CalculateSession944
Ora_CloseAsset
Ora_CloseClient
Ora_CloseConfig
```

## Disassembly Overview

Functions analyzed: **29** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140002a00` | `0x140002a00` | 3319 | ✓ |
| `fcn.1400020f0` | `0x1400020f0` | 2309 | ✓ |
| `entry0` | `0x1400014a0` | 1330 | ✓ |
| `section..text` | `0x140001000` | 821 | ✓ |
| `fcn.140001e30` | `0x140001e30` | 703 | ✓ |
| `fcn.140003f20` | `0x140003f20` | 695 | ✓ |
| `fcn.140003700` | `0x140003700` | 674 | ✓ |
| `fcn.140003ca0` | `0x140003ca0` | 628 | ✓ |
| `fcn.140001c80` | `0x140001c80` | 419 | ✓ |
| `fcn.140003b10` | `0x140003b10` | 397 | ✓ |
| `fcn.1400039b0` | `0x1400039b0` | 344 | ✓ |
| `fcn.140001340` | `0x140001340` | 201 | ✓ |
| `fcn.140001bb0` | `0x140001bb0` | 199 | ✓ |
| `fcn.140001ab0` | `0x140001ab0` | 128 | ✓ |
| `fcn.140001b30` | `0x140001b30` | 124 | ✓ |
| `fcn.140001a80` | `0x140001a80` | 46 | ✓ |
| `fcn.1400019e0` | `0x1400019e0` | 42 | ✓ |
| `fcn.140001a10` | `0x140001a10` | 34 | ✓ |
| `fcn.140001a60` | `0x140001a60` | 30 | ✓ |
| `fcn.140001a40` | `0x140001a40` | 23 | ✓ |
| `sym.ProjectM2HdbF.exe_Ora_AllocAsset` | `0x140001440` | 8 | ✓ |
| `sym.ProjectM2HdbF.exe_Ora_AllocContext` | `0x140001460` | 6 | ✓ |
| `sym.ProjectM2HdbF.exe_Ora_AllocProfile` | `0x140001450` | 6 | ✓ |
| `sym.ProjectM2HdbF.exe_Ora_AllocRecord` | `0x140001430` | 6 | ✓ |
| `sym.ProjectM2HdbF.exe_Ora_CalculateContext` | `0x140001470` | 6 | ✓ |
| `sym.ProjectM2HdbF.exe_Ora_CloseContext873` | `0x140001490` | 6 | ✓ |
| `sym.ProjectM2HdbF.exe_Ora_CopyOrder` | `0x140001480` | 6 | ✓ |
| `sym.ProjectM2HdbF.exe_Ora_AllocClient` | `0x140001410` | 3 | ✓ |
| `sym.ProjectM2HdbF.exe_Ora_AllocConfig` | `0x140001420` | 3 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.140001340.c`](code/fcn.140001340.c)
- [`code/fcn.1400019e0.c`](code/fcn.1400019e0.c)
- [`code/fcn.140001a10.c`](code/fcn.140001a10.c)
- [`code/fcn.140001a40.c`](code/fcn.140001a40.c)
- [`code/fcn.140001a60.c`](code/fcn.140001a60.c)
- [`code/fcn.140001a80.c`](code/fcn.140001a80.c)
- [`code/fcn.140001ab0.c`](code/fcn.140001ab0.c)
- [`code/fcn.140001b30.c`](code/fcn.140001b30.c)
- [`code/fcn.140001bb0.c`](code/fcn.140001bb0.c)
- [`code/fcn.140001c80.c`](code/fcn.140001c80.c)
- [`code/fcn.140001e30.c`](code/fcn.140001e30.c)
- [`code/fcn.1400020f0.c`](code/fcn.1400020f0.c)
- [`code/fcn.140002a00.c`](code/fcn.140002a00.c)
- [`code/fcn.140003700.c`](code/fcn.140003700.c)
- [`code/fcn.1400039b0.c`](code/fcn.1400039b0.c)
- [`code/fcn.140003b10.c`](code/fcn.140003b10.c)
- [`code/fcn.140003ca0.c`](code/fcn.140003ca0.c)
- [`code/fcn.140003f20.c`](code/fcn.140003f20.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sym.ProjectM2HdbF.exe_Ora_AllocAsset.c`](code/sym.ProjectM2HdbF.exe_Ora_AllocAsset.c)
- [`code/sym.ProjectM2HdbF.exe_Ora_AllocClient.c`](code/sym.ProjectM2HdbF.exe_Ora_AllocClient.c)
- [`code/sym.ProjectM2HdbF.exe_Ora_AllocConfig.c`](code/sym.ProjectM2HdbF.exe_Ora_AllocConfig.c)
- [`code/sym.ProjectM2HdbF.exe_Ora_AllocContext.c`](code/sym.ProjectM2HdbF.exe_Ora_AllocContext.c)
- [`code/sym.ProjectM2HdbF.exe_Ora_AllocProfile.c`](code/sym.ProjectM2HdbF.exe_Ora_AllocProfile.c)
- [`code/sym.ProjectM2HdbF.exe_Ora_AllocRecord.c`](code/sym.ProjectM2HdbF.exe_Ora_AllocRecord.c)
- [`code/sym.ProjectM2HdbF.exe_Ora_CalculateContext.c`](code/sym.ProjectM2HdbF.exe_Ora_CalculateContext.c)
- [`code/sym.ProjectM2HdbF.exe_Ora_CloseContext873.c`](code/sym.ProjectM2HdbF.exe_Ora_CloseContext873.c)
- [`code/sym.ProjectM2HdbF.exe_Ora_CopyOrder.c`](code/sym.ProjectM2HdbF.exe_Ora_CopyOrder.c)

## Behavioral Analysis

Based on the second chunk of disassembly provided, I have updated and expanded my analysis of the binary's behavior. The new code confirms several high-risk indicators related to **reflective loading** and **multi-stage payload execution**.

### Updated Analysis Summary

#### 1. Core Functionality (Refined)
The binary is confirmed as a **complex loader/orchestrator**. While the first chunk established it as a "dropper," this disassembly reveals that it is specifically designed to find, map, and execute hidden executable components within its own memory space or a nearby process.

*   **Embedded Payload Execution:** The code doesn't just drop a file; it actively parses an embedded "hidden" PE (Portable Executable) file.
*   **Reflective Loading Architecture:** The logic in `fcn.140001340` is a classic implementation for finding and loading an internal payload. It scans the memory of the process to find valid "MZ" headers and validates the section table before attempting to execute the code.

#### 2. Suspicious and Malicious Behaviors
*   **Base64-Encoded Payload Storage:** In `fcn.140003f20`, a large, hardcoded Base64 string is present. The complex bitwise math (`uVar7 >> 4 | cVar14 << 2`) confirms this is the primary method for storing the "hidden" payload (likely encrypted shellcode or a secondary DLL).
*   **Internal PE Parsing:** `fcn.140001340` performs manual parsing of the Windows Portable Executable (PE) header. Specifically:
    *   It looks for the **MZ** (`0x5a4d`) and **PE** (`0x4550`) signatures.
    *   It iterates through the Section Table to find specific headers. 
    *   This is a hallmark of "reflective DLL injection" or "modular malware," where the malicious functionality is hidden inside a second, differently-named layer.
*   **Integrity & Environment Checks:** `fcn.140001c80` performs several calls with specific hardcoded hex values (e.g., `0xec6fc7f7`, `0x11f6ff3f`). It then checks if the results match specific constants (`0x419` or `0x423`). This is a common "anti-analysis" or "anti-sandbox" check to ensure the malware isn't being run in a debugger or an emulated environment.
*   **Dynamic Function Resolution:** The code frequently retrieves function pointers and calls them via offsets (e.g., `(*pcVar6)(0x10)`). This is done to hide the actual API imports from static analysis tools like `strings` or standard cross-referencing.

#### 3. Notable Techniques & Patterns
*   **Manual Memory Manipulation:** Functions like `fcn.1400039b0` and `fcn.140001ab0` appear to be custom implementations of common memory operations (like string comparison or buffer copying). By not using standard Windows API calls (like `memcpy` or `strstr`), the author makes it harder for automated security tools to flag the binary's behavior as suspicious.
*   **Advanced Decoding Loop:** The logic in `fcn.140003f20` isn't just a simple Base64 decode; it handles multi-byte shifting and bitmasking, suggesting that the payload might be partially obfuscated even after the initial "Base64" layer is stripped away.
*   **Decoy Persistence:** The Oracle-branded functions (`Ora_AllocAsset`, `Ora_AllocContext`) remain in the binary but are clearly not being used for database management. They exist solely to provide a "safe" profile during manual inspection by an analyst who might be looking for known business logic.

---

### Updated Summary for Incident Response
**Confidence Level: High (Malicious)**

*   **Threat Actor Profile:** The sophistication of the reflective loading, custom memory manipulation, and the use of high-quality "fake" branding suggests a professional threat actor or a sophisticated malware group.
*   **Primary Indicator - Reflective Loader:** The binary is not just a simple downloader; it is designed to host other malicious components in memory, making traditional disk-based antivirus scans ineffective against the secondary stage of the attack.
*   **Payload Detection:** There is a significant Base64-encoded block within `fcn.140003f20`. **Recommendation:** Extract this string and decode it to identify the secondary payload (likely an `.exe` or `.dll`).
*   **Evasion Tactic:** The binary uses "Anti-Analysis" checks in `fcn.140001c80` to detect analysis environments.
*   **Recommended Actions:** 
    1.  Isolate any systems where this binary is found immediately.
    2.  Perform a memory dump of the process while it is running; look for "MZ" headers in non-file-backed memory segments (this will reveal the second stage).
    3.  Monitor for network connections originating from processes that exhibit high amounts of memory manipulation and lack standard database signatures.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1620** | Reflective Loader | The binary performs manual PE header parsing and section table validation to load and execute an internal, hidden payload directly in memory. |
| **T1027** | Obfuscated Executables | The use of Base64 encoding combined with complex bitwise shifting logic hides the primary payload from initial static analysis. |
| **T1546** | Sandbox Evasion | The "Integrity & Environment Checks" involving specific hex constants are designed to detect and bypass automated sandbox or analysis environments. |
| **T1036** | Masquerading | The inclusion of unused Oracle-branded functions serves as a decoy to make the binary appear as legitimate software during manual investigation. |
| **T1106** | Unified Fileed Loading | By using custom memory manipulation and avoiding standard Windows API calls (like `memcpy`), the malware attempts to bypass security tools that monitor common execution patterns. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted list of Indicators of Compromise (IOCs):

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   `ProjectM2HdbF.exe` (Identified as the primary malicious binary/loader)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *No MD5, SHA-1, or SHA-256 hashes were present in the provided strings.*

### **Other artifacts**
*   **Base64 Encoded Payloads:** (These are high-priority indicators of hidden second-stage payloads)
    *   `yKx+rmLTZSozailc2VpGIwbYUFveq54QHAjEgNn3O7hCtDRfsXM6kB0JdWP81u9/qLuJFYS6vLwtexyD50gHvxyDFYyHUjyDUMK7FYHOvYSDZLAk5TK6lj1feYwAv0XNv0ifeJyRU0uDz076z07A5nrRqLAso2==`
    *   `GbuPvbXtUp1BzEyHom57enVf5JaHGN2HaGyRa+tHw0NRiE28ZTH0ixgH2YKseLwYFbSzvY2fiGaJzEa0ZxAzpmViGxsHeLNCFpKTFbiCeMgH20AMe0BNz6rMaxdszEyRaxKGUbFAqngfiGaJzEa`
    *   `50NRvTVkqxWgeLs=`
    *   `prwKVy==`
*   **Anti-Analysis Constants:** (Used in `fcn.140001c80` to detect debuggers/sandboxes)
    *   `0xec6fc7f7`
    *   `0x11f6ff3f`
    *   `0x419`
    *   `0x423`
*   **Decoy Function Strings (Oracle Branding):** 
    *   The presence of approximately 80+ `Ora_` functions (e.g., `Ora_AllocAsset`, `Ora_AllocateContext`, `Ora_CalculateReport`) serves as an indicator of a **deception tactic** used to mimic legitimate database software and evade manual analysis.
*   **Reflective Loading Indicators:**
    *   Execution of logic in `fcn.140001340` specifically looking for `MZ` (`0x5a4d`) and `PE` (`0x4550`) headers within memory segments is a strong behavioral indicator of reflective DLL injection.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Reflective Loading Architecture:** The binary performs manual PE header parsing (searching for "MZ" and "PE" signatures) to execute hidden, embedded components directly in memory, a hallmark of sophisticated modular malware.
    *   **Advanced Evasion & Obfuscation:** The sample employs multi-layered protection including complex bitwise operations on Base64 strings, dynamic function resolution to hide API imports, and specific hex constants used for anti-debugging/anti-sandbox checks.
    *   **Deception Tactics:** The inclusion of over 80 "Oracle-branded" functions serves as a decoy to mask the malicious nature of the code during manual inspection by masquerading as legitimate database software.
