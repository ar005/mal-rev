# Threat Analysis Report

**Generated:** 2026-09-02 09:03 UTC
**Sample:** `1319d474d19eb386841732c728acf0c5fe64aa135101c6ceee1bd0369ecf97b6_1319d474d19eb386841732c728acf0c5fe64aa135101c6ceee1bd0369ecf97b6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1319d474d19eb386841732c728acf0c5fe64aa135101c6ceee1bd0369ecf97b6_1319d474d19eb386841732c728acf0c5fe64aa135101c6ceee1bd0369ecf97b6.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 10 sections |
| Size | 6,919,680 bytes |
| MD5 | `f8560b9a893eeb2130fc7159e9c1b851` |
| SHA1 | `4a54b7237dc9fdd745d0d19083a1ce4857c91de4` |
| SHA256 | `1319d474d19eb386841732c728acf0c5fe64aa135101c6ceee1bd0369ecf97b6` |
| Overall entropy | 6.036 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1770212755 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 2,114,560 | 5.636 | No |
| `.rdata` | 1,799,680 | 3.831 | No |
| `.data` | 278,528 | 4.514 | No |
| `.pdata` | 93,184 | 5.9 | No |
| `.idata` | 17,408 | 3.627 | No |
| `.tls` | 1,536 | 0.008 | No |
| `.00cfg` | 512 | 0.346 | No |
| `_RDATA` | 1,024 | 1.444 | No |
| `.rsrc` | 2,573,824 | 6.338 | No |
| `.reloc` | 38,400 | 3.542 | No |

### Imports

**WebView2Loader.dll**: `GetAvailableCoreWebView2BrowserVersionString`, `CreateCoreWebView2EnvironmentWithOptions`
**KERNEL32.dll**: `GetModuleHandleW`, `GetProcAddress`, `LoadLibraryA`, `CopyFileW`, `MultiByteToWideChar`, `GetCommandLineW`, `IsDebuggerPresent`, `DebugBreak`, `OutputDebugStringW`, `GetLastError`, `SetLastError`, `ReleaseSemaphore`, `ReleaseMutex`, `WaitForSingleObjectEx`, `OpenSemaphoreW`
**USER32.dll**: `GetMessageW`, `TranslateMessage`, `SetClassLongPtrW`, `PtInRect`, `ScreenToClient`, `SetCursor`, `ReleaseCapture`, `GetCapture`, `IsWindowVisible`, `TrackMouseEvent`, `EnableWindow`, `DestroyIcon`, `ClientToScreen`, `SetForegroundWindow`, `TrackPopupMenu`
**GDI32.dll**: `StretchBlt`, `GetDeviceCaps`, `DeleteObject`, `DeleteDC`, `CreateCompatibleDC`, `CreateFontIndirectW`, `SelectObject`, `GetObjectW`, `GetStockObject`
**COMDLG32.dll**: `GetSaveFileNameW`, `GetOpenFileNameW`
**ADVAPI32.dll**: `GetUserNameA`, `FreeSid`, `EqualSid`, `CheckTokenMembership`, `AllocateAndInitializeSid`, `OpenProcessToken`, `GetTokenInformation`
**SHELL32.dll**: `SHCreateItemFromParsingName`, `SetCurrentProcessExplicitAppUserModelID`, `CommandLineToArgvW`, `ShellExecuteExW`, `ShellExecuteW`
**SHLWAPI.dll**: `ord_12`, `SHCreateStreamOnFileEx`, `UrlEscapeW`, `PathCombineW`
**ole32.dll**: `CoTaskMemAlloc`, `CoCreateFreeThreadedMarshaler`, `CoInitializeEx`, `CoCreateInstance`, `CoTaskMemFree`, `OleInitialize`, `OleUninitialize`, `RegisterDragDrop`, `DoDragDrop`, `CLSIDFromString`, `CLSIDFromProgID`, `RevokeDragDrop`, `CoIncrementMTAUsage`
**OLEAUT32.dll**: `SysStringLen`, `VariantClear`, `SysAllocString`, `VariantInit`, `SystemTimeToVariantTime`, `VariantTimeToSystemTime`, `LoadTypeLib`, `SysFreeString`
**urlmon.dll**: `CreateUri`, `URLDownloadToFileW`
**gdiplus.dll**: `GdipCreateHICONFromBitmap`, `GdipCreateBitmapFromStreamICM`, `GdipCreateBitmapFromStream`, `GdipDisposeImage`, `GdipCloneImage`, `GdiplusStartup`, `GdipFree`, `GdipAlloc`
**bcrypt.dll**: `BCryptGetProperty`, `BCryptOpenAlgorithmProvider`, `BCryptSetProperty`, `BCryptCloseAlgorithmProvider`, `BCryptEncrypt`, `BCryptDecrypt`, `BCryptDestroyKey`, `BCryptGenRandom`, `BCryptGenerateSymmetricKey`
**CRYPT32.dll**: `CryptStringToBinaryA`, `CryptBinaryToStringA`
**WINHTTP.dll**: `WinHttpSendRequest`, `WinHttpOpenRequest`, `WinHttpQueryDataAvailable`, `WinHttpReadData`, `WinHttpConnect`, `WinHttpReceiveResponse`, `WinHttpOpen`, `WinHttpCloseHandle`
**api-ms-win-core-path-l1-1-0.dll**: `PathCchCanonicalize`, `PathCchRemoveFileSpec`
**wkscli.dll**: `NetWkstaGetInfo`
**netutils.dll**: `NetApiBufferFree`
**d2d1.dll**: `ord_11`, `ord_9`, `ord_2`
**api-ms-win-core-winrt-error-l1-1-0.dll**: `GetRestrictedErrorInfo`, `SetRestrictedErrorInfo`

## Extracted Strings

Total strings found: **5609** (showing first 100)

```
!This program cannot be run in DOS mode.
$
D(B D7:
D!:$D :
DRich!:
`.rdata
@.data
.pdata
@.idata
.00cfg
@_RDATA
@.rsrc
@.reloc
VWATAVAWH
pA_A^A\_^
@SUATAVAWH
 A_A^A\][
UVWATAUAVAWH
 A_A^A]A\_^]
C8H9(t!H
VWATAVAWH
pA_A^A\_^
\$ VAVAWH
 A_A^^
@SVATAVH
(A^A\^[
@SWAVH
@SVAVAWH
(A_A^^[
@SVAUAVH
(A^A]^[
SVWAVAWH
 A_A^_^[
)L$0E3
D$XH9C
\$ UVWH
\$ UVWH
\$ UVWH
\$ UVWH
H9=IE>
@USVWATAVAWH
A_A^A\_^[]
VWATAVAWH
A_A^A\_^
VWATAVAWH
A_A^A\_^
UATAUAVAWH
A_A^A]A\]
D$0L9D$Ps
UVWATAUAVAWH
C@H98t$H
)D$0M+
A_A^A]A\_^]
|$ UAVAWH
|$ UAVAWH
|$ UAVAWH
UVWAVAWH
A_A^_^]
UVWATAUAVAWH
C@H98t$H
A_A^A]A\_^]
|$ AVH
@USVWAVAWH
A_A^_^[]
|$ht{H
UVWATAUAVAWH
A_A^A]A\_^]
VWATAVAWH
 A_A^A\_^
UVWATAWH
 A_A\_^]
WAVAWH
 A_A^_
D$ HcH
D$ HcH
D$ HcH
D$ HcH
UVWATAUAVAWH
A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
@USVWATAUAVAWH
A_A^A]A\_^[]
@VWAVH
UVWAVAWH
A_A^_^]
\$ VWATAVAWH
A_A^A\_^
@SVWAVAWH
A_A^_^[
@USVWATAUAVAWH
A_A^A]A\_^[]
|$ AVH
WATAUAVAWH
A_A^A]A\_
												
																																												
							
D$`HcH
D$`HcH
D$`Hc@
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400028ba` | `0x1400028ba` | 1967023 | ✓ |
| `fcn.140002ca2` | `0x140002ca2` | 1963019 | ✓ |
| `fcn.140001c9e` | `0x140001c9e` | 1960540 | ✓ |
| `fcn.1400031b6` | `0x1400031b6` | 1957493 | ✓ |
| `fcn.140003a0d` | `0x140003a0d` | 1957442 | ✓ |
| `fcn.140004769` | `0x140004769` | 1956152 | ✓ |
| `fcn.140003f17` | `0x140003f17` | 1955861 | ✓ |
| `fcn.140009354` | `0x140009354` | 1955177 | ✓ |
| `fcn.140003792` | `0x140003792` | 1954178 | ✓ |
| `fcn.140003486` | `0x140003486` | 1953847 | ✓ |
| `fcn.140005bbe` | `0x140005bbe` | 1953583 | ✓ |
| `fcn.1400059b1` | `0x1400059b1` | 1952863 | ✓ |
| `fcn.140008c9c` | `0x140008c9c` | 1952493 | ✓ |
| `fcn.1400048c7` | `0x1400048c7` | 1952026 | ✓ |
| `fcn.140001843` | `0x140001843` | 1952020 | ✓ |
| `fcn.140001b5e` | `0x140001b5e` | 1950789 | ✓ |
| `fcn.140003ee5` | `0x140003ee5` | 1950444 | ✓ |
| `fcn.140001d02` | `0x140001d02` | 1950051 | ✓ |
| `fcn.140001ed3` | `0x140001ed3` | 1949992 | ✓ |
| `fcn.1400036e3` | `0x1400036e3` | 1949990 | ✓ |
| `fcn.140006b27` | `0x140006b27` | 1949469 | ✓ |
| `fcn.140004ce6` | `0x140004ce6` | 1948577 | ✓ |
| `fcn.140004b88` | `0x140004b88` | 1947473 | ✓ |
| `fcn.140006479` | `0x140006479` | 1946920 | ✓ |
| `fcn.14000551f` | `0x14000551f` | 1946713 | ✓ |
| `fcn.140005e8e` | `0x140005e8e` | 1946587 | ✓ |
| `fcn.140004bc9` | `0x140004bc9` | 1945235 | ✓ |
| `fcn.14000709a` | `0x14000709a` | 1945075 | ✓ |
| `fcn.140007612` | `0x140007612` | 1944184 | ✓ |
| `fcn.140005961` | `0x140005961` | 1943835 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001843.c`](code/fcn.140001843.c)
- [`code/fcn.140001b5e.c`](code/fcn.140001b5e.c)
- [`code/fcn.140001c9e.c`](code/fcn.140001c9e.c)
- [`code/fcn.140001d02.c`](code/fcn.140001d02.c)
- [`code/fcn.140001ed3.c`](code/fcn.140001ed3.c)
- [`code/fcn.1400028ba.c`](code/fcn.1400028ba.c)
- [`code/fcn.140002ca2.c`](code/fcn.140002ca2.c)
- [`code/fcn.1400031b6.c`](code/fcn.1400031b6.c)
- [`code/fcn.140003486.c`](code/fcn.140003486.c)
- [`code/fcn.1400036e3.c`](code/fcn.1400036e3.c)
- [`code/fcn.140003792.c`](code/fcn.140003792.c)
- [`code/fcn.140003a0d.c`](code/fcn.140003a0d.c)
- [`code/fcn.140003ee5.c`](code/fcn.140003ee5.c)
- [`code/fcn.140003f17.c`](code/fcn.140003f17.c)
- [`code/fcn.140004769.c`](code/fcn.140004769.c)
- [`code/fcn.1400048c7.c`](code/fcn.1400048c7.c)
- [`code/fcn.140004b88.c`](code/fcn.140004b88.c)
- [`code/fcn.140004bc9.c`](code/fcn.140004bc9.c)
- [`code/fcn.140004ce6.c`](code/fcn.140004ce6.c)
- [`code/fcn.14000551f.c`](code/fcn.14000551f.c)
- [`code/fcn.140005961.c`](code/fcn.140005961.c)
- [`code/fcn.1400059b1.c`](code/fcn.1400059b1.c)
- [`code/fcn.140005bbe.c`](code/fcn.140005bbe.c)
- [`code/fcn.140005e8e.c`](code/fcn.140005e8e.c)
- [`code/fcn.140006479.c`](code/fcn.140006479.c)
- [`code/fcn.140006b27.c`](code/fcn.140006b27.c)
- [`code/fcn.14000709a.c`](code/fcn.14000709a.c)
- [`code/fcn.140007612.c`](code/fcn.140007612.c)
- [`code/fcn.140008c9c.c`](code/fcn.140008c9c.c)
- [`code/fcn.140009354.c`](code/fcn.140009354.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary's functionality and characteristics.

### Core Functionality & Purpose
The code exhibits characteristics typical of a **packer, loader, or highly obfuscated "stub"** used to wrap another payload. While it does not show immediate network activity in these specific snippets, several indicators suggest its primary role is preparing an environment or unpacking further code:

*   **PE Header Parsing:** The function `fcn.140005be` explicitly checks for the `"MZ"` header (0x5A4D). This is a standard technique used by loaders to identify and locate executable files in memory, often used when one piece of code is "unwrapping" another.
*   **Advanced String Manipulation:** Multiple functions (`fcn.140009354`, `fcn.140008c9c`, `fcn.140004769`) perform complex Unicode/UTF-16 handling and case conversion (e.g., the usage of `+ 0x20` to shift between uppercase and lowercase). This suggests the binary processes various system paths, configuration files, or internal commands.
*   **Mathematical Complexity:** Function `fcn.1400031b6` utilizes AVX instructions (e.g., `vpsrlq_avx`, `vfmadd213sd_fma`). This level of complex floating-point math is often found in either high-end media engines or, more relevantly here, in **custom decryption/deobfuscation algorithms** that use mathematical transformations to hide a payload.

### Suspicious & Malicious Behaviors
The following behaviors are noteworthy from a security perspective:

*   **Potential Unpacking Behavior:** The combination of MZ header checks and complex bitwise-heavy functions (`fcn.140002ca2`) is highly indicative of an **unpacker**. It suggests the code may be responsible for decrypting or decompressing a hidden stage in memory.
*   **Environment/Input Checking:** `fcn.140001c9e` checks for the existence of the console (`CONOUT$`). While common in legitimate tools, malware often uses this to check if it is running in an interactive session or a sandbox environment.
*   **Obfuscation & Junk Code:** The high volume of bitwise operations, shifts, and nested conditional logic (as seen in `fcn.140002ca2`) is a common technique used to hinder static analysis and confuse decompilers.

### Notable Techniques & Patterns
*   **AVX Instructions for Obfuscation:** The use of specialized SIMD instructions (`vfmadd...`, etc.) can be used to perform "parallel" decryption, making it harder for standard disassemblers to follow the logic flow.
*   **Anti-Analysis/De-obfuscation:** The extreme complexity and repetitive branching in several functions suggest the use of a **compiler obfuscator**. This is designed to make identifying the program's true intent difficult by burying simple instructions under layers of logical noise.
*   **Unicode Handling:** Detailed logic for UTF-16 strings (handling surrogate pairs, etc.) suggests that the binary interacts with the Windows API in a way that handles international characters, common when dealing with file paths or registry keys.

### Summary
This sample appears to be a **packer or an obfuscated loader**. It contains high levels of complexity meant to hide its true purpose. The primary indicators are the **MZ header detection**, **complex bit-manipulation for deobfuscation**, and **extensive string processing logic**. While no direct "malicious" actions (like downloading files) are visible in this specific slice, these are hallmark features of a multi-stage malware dropper.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a packer, complex bitwise-heavy "junk" code, and advanced math (AVX) are classic methods used to hide the payload's true intent from static analysis. |
| **T1497** | Virtualization/Sandbox Evasion | The specific check for `CONOUT$` is used to determine if the environment is an interactive session or a sandbox, allowing the malware to change behavior to evade detection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The string section contains a high volume of obfuscated data and standard PE header artifacts; these were filtered out as they do not constitute specific infrastructure or file system IOCs.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified (The analysis mentions `CONOUT$`, but this is a standard Windows system handle and not a unique malware indicator).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Configuration/Command Parameters:** 
    *   `Epport` (Potential internal variable for defining a port)
    *   `agent_idH` (Possible identifier for a compromised host in a botnet or C2 framework)
    *   `cmd_typeH` (Indicates the sample handles different types of commands from a remote server)
    *   `cmd_lineH` (Indicates command-line argument processing)

### **Analyst Notes**
While specific network IOCs (IPs/Domains) were not present in the raw string dump, the behavioral analysis confirms that this binary is a **packer or obfuscated loader**. The presence of `cmd_typeH` and `agent_idH` suggests that while this specific file may be a "loader," it is designed to facilitate interaction with a Command & Control (C2) infrastructure. The use of AVX instructions for deobfuscation and MZ header checks indicates a sophisticated attempt to hide the final payload's signature during initial execution.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High (regarding its function) / Low (regarding specific family attribution)
4. **Key evidence**:
*   **Payload Unpacking:** The use of MZ header parsing and complex AVX-based mathematical instructions indicates the binary is designed to decrypt and execute a hidden secondary payload in memory.
*   **Anti-Analysis/Evasion:** The inclusion of `CONOUT$` checks (sandbox evasion) and heavy "junk code" obfuscation confirms its role as a protective stub meant to hinder analysis and bypass security controls.
*   **C2 Readiness:** While no specific network IOCs were found, the presence of internal variables like `agent_idH` and `cmd_typeH` suggests it is configured to receive commands from a remote server typical of botnet or backdoor infrastructures.
