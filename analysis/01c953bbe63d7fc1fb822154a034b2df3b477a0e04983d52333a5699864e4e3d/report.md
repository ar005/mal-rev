# Threat Analysis Report

**Generated:** 2026-06-27 13:22 UTC
**Sample:** `01c953bbe63d7fc1fb822154a034b2df3b477a0e04983d52333a5699864e4e3d_01c953bbe63d7fc1fb822154a034b2df3b477a0e04983d52333a5699864e4e3d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01c953bbe63d7fc1fb822154a034b2df3b477a0e04983d52333a5699864e4e3d_01c953bbe63d7fc1fb822154a034b2df3b477a0e04983d52333a5699864e4e3d.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 7 sections |
| Size | 87,342,686 bytes |
| MD5 | `531bbc779602de78cd933a87c3dda65b` |
| SHA1 | `45e655f0192ff2c2c290c4daebcd348b643ddba8` |
| SHA256 | `01c953bbe63d7fc1fb822154a034b2df3b477a0e04983d52333a5699864e4e3d` |
| Overall entropy | 7.378 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1735304282 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 28,481,536 | 6.474 | No |
| `.rdata` | 24,107,520 | 6.171 | No |
| `.data` | 295,424 | 3.911 | No |
| `.pdata` | 1,291,776 | 6.947 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 142,336 | 6.165 | No |
| `.reloc` | 155,648 | 5.495 | No |

### Imports

**dbghelp.dll**: `SymSetSearchPathW`, `SymGetSearchPathW`, `SymGetModuleBase64`, `SymFunctionTableAccess64`, `StackWalk64`, `SymSetOptions`, `SymCleanup`, `SymGetLineFromAddr64`, `MiniDumpWriteDump`, `SymGetOptions`, `SymFromAddr`, `SymInitialize`, `UnDecorateSymbolName`
**WS2_32.dll**: `htonl`, `WSAGetLastError`, `getservbyname`, `getservbyport`, `gethostbyaddr`, `inet_ntoa`, `inet_addr`, `WSACleanup`, `ntohs`, `ntohl`, `closesocket`, `getsockopt`, `socket`, `WSAStartup`, `WSAIoctl`
**CRYPT32.dll**: `CertEnumCertificatesInStore`, `CertCloseStore`, `CertFindCertificateInStore`, `CertDuplicateCertificateContext`, `CertOpenStore`, `CertGetCertificateContextProperty`, `CertFreeCertificateContext`
**ADVAPI32.dll**: `SystemFunction036`, `RegQueryValueExA`, `RegEnumKeyExA`, `RegEnumKeyExW`, `RegQueryInfoKeyW`, `EventWriteTransfer`, `EventSetInformation`, `EventUnregister`, `EventRegister`, `ReportEventW`, `RegisterEventSourceW`, `DeregisterEventSource`, `CryptEnumProvidersW`, `CryptSignHashW`, `CryptDestroyHash`
**USER32.dll**: `DispatchMessageA`, `TranslateMessage`, `GetMessageA`, `MapVirtualKeyW`, `CharUpperA`, `GetProcessWindowStation`, `MessageBoxW`, `GetUserObjectInformationW`, `GetSystemMetrics`
**ole32.dll**: `CoTaskMemFree`
**IPHLPAPI.DLL**: `GetBestRoute2`, `if_nametoindex`, `if_indextoname`, `CancelMibChangeNotify2`, `GetAdaptersAddresses`, `ConvertInterfaceIndexToLuid`, `ConvertInterfaceLuidToNameW`, `NotifyIpInterfaceChange`
**PSAPI.DLL**: `GetModuleFileNameExW`, `EnumProcessModules`
**SHELL32.dll**: `SHGetKnownFolderPath`
**USERENV.dll**: `GetUserProfileDirectoryW`
**bcrypt.dll**: `BCryptGenRandom`
**KERNEL32.dll**: `GetStringTypeW`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `UnhandledExceptionFilter`, `IsProcessorFeaturePresent`, `InitializeSListHead`, `InterlockedPushEntrySList`, `RtlUnwindEx`, `RtlPcToFileHeader`, `InitializeCriticalSectionAndSpinCount`, `ExitProcess`, `GetModuleHandleExW`, `SetStdHandle`, `ExitThread`, `FreeLibraryAndExitThread`
**WINMM.dll**: `timeGetTime`

### Exports

`??$MakeCheckOpString@HH@base@v8@@YAPEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@HHPEBD@Z`, `??$MakeCheckOpString@II@base@v8@@YAPEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@IIPEBD@Z`, `??$MakeCheckOpString@JJ@base@v8@@YAPEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@JJPEBD@Z`, `??$MakeCheckOpString@KK@base@v8@@YAPEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@KKPEBD@Z`, `??$MakeCheckOpString@PEBXPEBX@base@v8@@YAPEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@PEBX0PEBD@Z`, `??$MakeCheckOpString@_J_J@base@v8@@YAPEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@_J0PEBD@Z`, `??$MakeCheckOpString@_K_K@base@v8@@YAPEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@_K0PEBD@Z`, `??$PrintCheckOperand@C@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@C@Z`, `??$PrintCheckOperand@D@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@D@Z`, `??$PrintCheckOperand@E@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@E@Z`, `??$PrintCheckOperand@H@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@H@Z`, `??$PrintCheckOperand@I@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@I@Z`, `??$PrintCheckOperand@J@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@J@Z`, `??$PrintCheckOperand@K@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@K@Z`, `??$PrintCheckOperand@PEAC@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@PEAC@Z`, `??$PrintCheckOperand@PEAD@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@PEAD@Z`, `??$PrintCheckOperand@PEAE@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@PEAE@Z`, `??$PrintCheckOperand@PEBC@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@PEBC@Z`, `??$PrintCheckOperand@PEBD@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@PEBD@Z`, `??$PrintCheckOperand@PEBE@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@PEBE@Z`, `??$PrintCheckOperand@PEBX@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@PEBX@Z`, `??$PrintCheckOperand@_J@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@_J@Z`, `??$PrintCheckOperand@_K@base@v8@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@_K@Z`, `??$SignedDivisionByConstant@I$00@base@v8@@YA?AU?$MagicNumbersForDivision@I@01@I@Z`, `??$SignedDivisionByConstant@_K$00@base@v8@@YA?AU?$MagicNumbersForDivision@_K@01@_K@Z`, `??$TryToCopyAndConvertArrayToCppBuffer@$0DAAAA@H@v8@@YA_NV?$Local@VArray@v8@@@0@PEAHI@Z`, `??$TryToCopyAndConvertArrayToCppBuffer@$0EAAAA@I@v8@@YA_NV?$Local@VArray@v8@@@0@PEAII@Z`, `??$TryToCopyAndConvertArrayToCppBuffer@$0HAAAA@M@v8@@YA_NV?$Local@VArray@v8@@@0@PEAMI@Z`, `??$TryToCopyAndConvertArrayToCppBuffer@$0IAAAA@N@v8@@YA_NV?$Local@VArray@v8@@@0@PEANI@Z`, `??$UnsignedDivisionByConstant@I@base@v8@@YA?AU?$MagicNumbersForDivision@I@01@II@Z`, `??$UnsignedDivisionByConstant@_K@base@v8@@YA?AU?$MagicNumbersForDivision@_K@01@_KI@Z`, `??$ValidateCallbackInfo@VArray@v8@@@internal@v8@@YA_NAEBV?$PropertyCallbackInfo@VArray@v8@@@1@@Z`, `??$ValidateCallbackInfo@VBoolean@v8@@@internal@v8@@YA_NAEBV?$PropertyCallbackInfo@VBoolean@v8@@@1@@Z`, `??$ValidateCallbackInfo@VInteger@v8@@@internal@v8@@YA_NAEBV?$PropertyCallbackInfo@VInteger@v8@@@1@@Z`, `??$ValidateCallbackInfo@VValue@v8@@@internal@v8@@YA_NAEBV?$FunctionCallbackInfo@VValue@v8@@@1@@Z`, `??$ValidateCallbackInfo@VValue@v8@@@internal@v8@@YA_NAEBV?$PropertyCallbackInfo@VValue@v8@@@1@@Z`, `??$ValidateCallbackInfo@X@internal@v8@@YA_NAEBV?$FunctionCallbackInfo@X@1@@Z`, `??$ValidateCallbackInfo@X@internal@v8@@YA_NAEBV?$PropertyCallbackInfo@X@1@@Z`, `??0?$MagicNumbersForDivision@I@base@v8@@QEAA@II_N@Z`, `??0?$MagicNumbersForDivision@_K@base@v8@@QEAA@_KI_N@Z`, `??0?$MemorySpan@$$CBD@v8@@QEAA@XZ`, `??0?$MemorySpan@$$CBE@v8@@QEAA@XZ`, `??0?$MemorySpan@$$CBV?$Local@VContext@v8@@@v8@@@v8@@QEAA@XZ`, `??0?$MemorySpan@$$CBV?$Local@VString@v8@@@v8@@@v8@@QEAA@XZ`, `??0?$MemorySpan@$$CBV?$Local@VValue@v8@@@v8@@@v8@@QEAA@XZ`, `??0?$MemorySpan@$$CBV?$basic_string_view@DU?$char_traits@D@std@@@std@@@v8@@QEAA@XZ`, `??0?$MemorySpan@$$CBVCFunction@v8@@@v8@@QEAA@XZ`, `??0?$MemorySpan@$$CB_K@v8@@QEAA@XZ`, `??0?$MemorySpan@V?$Handle@VObject@internal@v8@@@internal@v8@@@v8@@QEAA@XZ`, `??0?$MemorySpan@V?$MaybeLocal@VValue@v8@@@v8@@@v8@@QEAA@XZ`

## Extracted Strings

Total strings found: **233365** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
aurHuD
aulsu<
  Shu2
anghu*
ai  u"
VIA Padlock x86_64 module, CRYPTOGAMS by <appro@openssl.org>
SUATAUAVAWH
L3f L3n(L3v0L3~8L
L3f L3n(L3v0L3~8L3
L3g L3o(L3w0L3
	OO!OBn
OO!OBn
?mRRUR
0`<
l0`<
\CKK1Kbz
)KK1Kbz
#JJ5Jj
 JJ5Jj
R|

(
P"
Z

(
P"
sg<]]i]
II9Irp
;II9Irp
HH=Hzu
2HH=Hzu
=d__a_
^u}TTMT
FMM)MRd
MM)MRd
LL-LZa
LL-LZa
"4h9
e4h9
NN%NJk
NN%NJk
r,X'
S,X'
		$	H-
A		$	H-
Pu\\m\
3VWSUATAUAVAW
A_A^A]A\][_^
SUATAUAVAWH
D7q/;M
SHA512 block transform for x86_64, CRYPTOGAMS by <appro@openssl.org>
SUATAUAVAWH
SUATAUAVAWH
SUATAUAVAWH
VWSUATAUAVAW
A_A^A]A\][_^
SUATAUAVAWH
8STs
e
	
SHA256 block transform for x86_64, CRYPTOGAMS by <appro@openssl.org>
SUATAUAVAWH
SUATAUAVAWH
SUATAUAVAWH
VWSUATAUAVAW
A_A^A]A\][_^
VWSUATAUAVAW
SUATAUAVAWH
ynl$<M
8STs
eTs
eTs
eTs
eTs
eTs
eTs
eTs
e
LwH'LwH'LwH'LwH'LwH'LwH'LwH'LwH'
8STs
e
SHA256 multi-block transform for x86_64, CRYPTOGAMS by <appro@openssl.org>
VWSUATAUAVAW
A_A^A]A\][_^
VWSUATAUAVAW
SUATAUAVI
D3t$1
D3t$$!
3T$(D!
3l$,D!
D3t$0D!
3l$ D1
D3t$$1
D3t$<F
3l$,D1
D3t$0D1
3T$4D1
D3t$4D
D3t$<1
D3t$ F
D3t$D
D3t$ 1
D3t$8F
3l$(D1
D3t$$D
D3t$,D!
D3t$8D!
3T$<D!
D3t$<D
3l$D!
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.141a5b860` | `0x141a5b860` | 27572563 | ✓ |
| `fcn.1419a2260` | `0x1419a2260` | 26093254 | ✓ |
| `fcn.1419a1bf0` | `0x1419a1bf0` | 26091674 | ✓ |
| `sym.node.exe_adler32_z` | `0x1403ddf90` | 24040012 | ✓ |
| `fcn.141567c00` | `0x141567c00` | 22313942 | ✓ |
| `fcn.141497580` | `0x141497580` | 21525735 | ✓ |
| `fcn.141319360` | `0x141319360` | 19961916 | ✓ |
| `fcn.1413066c0` | `0x1413066c0` | 19754380 | ✓ |
| `fcn.1400d9290` | `0x1400d9290` | 18922223 | ✓ |
| `fcn.141208ee0` | `0x141208ee0` | 18518955 | ✓ |
| `fcn.14119cb70` | `0x14119cb70` | 18402068 | ✓ |
| `fcn.14119c590` | `0x14119c590` | 18401642 | ✓ |
| `fcn.141161000` | `0x141161000` | 18114123 | ✓ |
| `fcn.1417c6f70` | `0x1417c6f70` | 18066014 | ✓ |
| `fcn.1417c9ab0` | `0x1417c9ab0` | 18037300 | ✓ |
| `fcn.1417c5ac0` | `0x1417c5ac0` | 18036082 | ✓ |
| `fcn.1417c71c0` | `0x1417c71c0` | 18029404 | ✓ |
| `fcn.1417c9b00` | `0x1417c9b00` | 18016658 | ✓ |
| `fcn.141765090` | `0x141765090` | 17643575 | ✓ |
| `fcn.1417670c0` | `0x1417670c0` | 17621819 | ✓ |
| `fcn.1417673f0` | `0x1417673f0` | 17617995 | ✓ |
| `fcn.141763830` | `0x141763830` | 17612503 | ✓ |
| `fcn.1417640a0` | `0x1417640a0` | 17593798 | ✓ |
| `fcn.141765d00` | `0x141765d00` | 17588750 | ✓ |
| `fcn.141764160` | `0x141764160` | 17569622 | ✓ |
| `fcn.1402919a0` | `0x1402919a0` | 16843276 | ✓ |
| `fcn.140945b40` | `0x140945b40` | 16777476 | ✓ |
| `fcn.140946850` | `0x140946850` | 16777473 | ✓ |
| `fcn.140946be0` | `0x140946be0` | 16777473 | ✓ |
| `fcn.141821f40` | `0x141821f40` | 16239420 | ✓ |

### Decompiled Code Files

- [`code/fcn.1400d9290.c`](code/fcn.1400d9290.c)
- [`code/fcn.1402919a0.c`](code/fcn.1402919a0.c)
- [`code/fcn.140945b40.c`](code/fcn.140945b40.c)
- [`code/fcn.140946850.c`](code/fcn.140946850.c)
- [`code/fcn.140946be0.c`](code/fcn.140946be0.c)
- [`code/fcn.141161000.c`](code/fcn.141161000.c)
- [`code/fcn.14119c590.c`](code/fcn.14119c590.c)
- [`code/fcn.14119cb70.c`](code/fcn.14119cb70.c)
- [`code/fcn.141208ee0.c`](code/fcn.141208ee0.c)
- [`code/fcn.1413066c0.c`](code/fcn.1413066c0.c)
- [`code/fcn.141319360.c`](code/fcn.141319360.c)
- [`code/fcn.141497580.c`](code/fcn.141497580.c)
- [`code/fcn.141567c00.c`](code/fcn.141567c00.c)
- [`code/fcn.141763830.c`](code/fcn.141763830.c)
- [`code/fcn.1417640a0.c`](code/fcn.1417640a0.c)
- [`code/fcn.141764160.c`](code/fcn.141764160.c)
- [`code/fcn.141765090.c`](code/fcn.141765090.c)
- [`code/fcn.141765d00.c`](code/fcn.141765d00.c)
- [`code/fcn.1417670c0.c`](code/fcn.1417670c0.c)
- [`code/fcn.1417673f0.c`](code/fcn.1417673f0.c)
- [`code/fcn.1417c5ac0.c`](code/fcn.1417c5ac0.c)
- [`code/fcn.1417c6f70.c`](code/fcn.1417c6f70.c)
- [`code/fcn.1417c71c0.c`](code/fcn.1417c71c0.c)
- [`code/fcn.1417c9ab0.c`](code/fcn.1417c9ab0.c)
- [`code/fcn.1417c9b00.c`](code/fcn.1417c9b00.c)
- [`code/fcn.141821f40.c`](code/fcn.141821f40.c)
- [`code/fcn.1419a1bf0.c`](code/fcn.1419a1bf0.c)
- [`code/fcn.1419a2260.c`](code/fcn.1419a2260.c)
- [`code/fcn.141a5b860.c`](code/fcn.141a5b860.c)
- [`code/sym.node.exe_adler32_z.c`](code/sym.node.exe_adler32_z.c)

## Behavioral Analysis

The addition of chunk 4 confirms and deepens the previous findings, specifically by moving from general "parsing" to highly specific **protocol normalization** and **network-to-object mapping**. This section acts as the bridge between the raw data received over the wire and the high level of abstraction required by the malware's internal state machine.

### Updated Analysis: Protocol Normalization & Data Mapping Integration

The final chunk reveals two distinct, yet highly sophisticated, stages of the "pre-processing" pipeline before an instruction is ever executed.

#### 1. Robust Unicode/UTF-8 Handling (De-obfuscation)
In `fcn.140946be0`, we see extremely granular logic for handling character encoding:
*   **Multi-byte Decoding:** The presence of complex bitwise checks—such as `(uVar4 | 0x20) - 0x31` and the detection of values below `0x80` vs. those requiring multi-byte processing—indicates that this function is a **Unicode/UTF-8 normalization routine**.
*   **Surrogate Pair Handling:** The logic involving `0xd800`, `0x3ff`, and `0xfffd` confirms the malware is prepared to handle full UTF-16 surrogate pairs. 
*   **Security Implication:** By using a robust Unicode parser, the threat actor ensures that commands or configuration strings (e.g., file paths, registry keys, or stolen data) remain consistent across different locales and can bypass simple string-based security filters that might only look for standard ASCII patterns.

#### 2. Network Integration & Buffer Processing
The function `fcn.141821f40` contains a critical link to the external world:
*   **Direct Socket Interaction:** The code references `reloc.WS2_32.dll_recv`. This confirms that this layer of the code is directly involved in **receiving and processing raw network packets**. 
*   **Dynamic Buffer Management:** The loops iterating through `uVar16` to manage offsets within a buffer indicate the malware is designed to handle variable-length data from the C2 server. It doesn't just expect a fixed "packet"; it parses a stream of data, identifying and extracting components dynamically.

#### 3. Data Mapping (The Translation Layer)
The final block of `fcn.141821f40` consists of a massive series of assignments (`arg1_00[0x14] = puVar13[0x14]`, etc.). This is highly significant:
*   **From "Wire Format" to "Internal Object":** This represents the transition from raw, unpacked data into a **Structured Data Object**. The code takes the results of the parsing/normalization and maps them into a structured memory space used by the core engine. 
*   **Complexity as a Buffer:** By decoupling the *parsing* (handling network quirks) from the *execution* (interpreting commands), the developers ensure that if one part of the system needs to change (e.g., switching from a TCP-based protocol to an HTTP-long-polling protocol), only the mapping logic needs to be updated, while the "brain" of the malware remains intact.

---

### Updated Summary for Incident Response

| Feature | Analysis & Impact |
| :--- | :--- |
| **Architecture** | **Decoupled Parsing/Execution Pipeline.** The analysis confirms a clear separation between communication handling, data normalization (Unicode/UTF16), and command execution. This makes "finding the core" harder as there are multiple layers of translation. |
| **Data Processing** | **Sophisticated Unicode Normalization.** The malware explicitly handles complex multi-byte characters. This suggests it is built for high reliability across different operating system versions and international locales, a hallmark of professional tooling. |
| **Communication** | **Robust Network Buffer Handling.** Integration with `recv` and manual buffer offset management indicates the malware can handle inconsistent or variable data streams from a C2 server, likely to avoid detection by simple protocol-anomaly scanners. |
| **Threat Profile** | **High-End Professional Infrastructure.** The presence of dedicated "translation" layers (moving from raw packets $\rightarrow$ normalized strings $\rightarrow$ internal objects) indicates a sophisticated development lifecycle typical of APT groups or high-tier cybercrime syndicates. |

---

### Technical Conclusion for Responders

The final chunk confirms that the malware possesses a **sophisticated front-end** designed to sanitize and organize data before it reaches the execution core. 

1.  **Obfuscation via Transformation:** The use of complex UTF-8/Unicode normalization means that "plain" strings are likely not stored in the binary; they are constructed or decoded from multi-byte sequences during runtime.
2.  **The "Black Box" Barrier:** Because there is a heavy translation layer between the network and the "brain," simple static analysis of the executable will rarely reveal the full scope of functionality until the code actually reaches the execution stage.

**Refined Recommendations for IR Teams:**
1.  **Identify Decryption/Normalization Points:** Instead of trying to reverse every bitwise operation in `fcn.140946be0`, identify where this function *ends*. This is the point where "safe" (but still malicious) data is handed off to the internal dispatcher. 
2.  **Monitor Memory for "Object Mapping":** Focus on the memory space related to `arg1_00` in `fcn.141821f40`. By dumping memory at this specific point, you can see the **fully reconstructed command objects**, which will be much easier to analyze than the raw, wrapped data coming from the network.
3.  **Enhanced Network Logging:** Because the malware handles complex buffer lengths and multi-byte characters, standard "signature-based" IDS may fail. Use behavior-based detection (e.g., identifying the long-lived, variable-length TCP connections typical of this type of heartbeating/command structure).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of complex Unicode/UTF-8 normalization and multi-byte decoding is specifically designed to bypass string-based security filters and hide command content. |
| T1568 | Dynamic Resolution | The implementation of dynamic buffer management and offset calculation for handling variable-length network packets hides the internal state machine from static analysis. |
| T1027 | Obfuscated Files or Information | The "Translation Layer" (decoupling parsing/execution) creates a "black box" barrier that complicates reverse engineering by separating raw data processing from core functionality. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the categorized list of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The text mentions network communication and C2 interaction generally, but no specific IP addresses or domain names were present in the data.)

### **File paths / Registry keys**
*   *None identified.* (While the analysis notes that the malware handles file paths and registry keys to avoid detection, no specific malicious paths or keys were listed.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (The strings provided consist primarily of standard cryptographic library descriptors and obfuscated internal data.)

### **Other artifacts**
*   **C2 Communication Patterns:** 
    *   **Variable-Length Buffer Handling:** The malware utilizes a manual buffer management system for incoming network packets, indicating it is designed to process non-standard or fluctuating packet sizes from the C2 server.
    *   **Direct Socket Interaction:** Utilization of `WS2_32.dll` (specifically `recv`) suggests direct TCP/UDP communication rather than high-level API calls that might be easier to hook or monitor.
*   **Detection Evasion Techniques:**
    *   **Unicode/UTF-16 Normalization:** The malware uses a robust, multi-byte decoding routine (`fcn.140946be0`) for "pre-processing" data. This is intended to mask the actual commands sent by the C2 from simple string-based security filters.
    *   **Decoupled Pipeline Architecture:** The separation of the "parsing/normalization" layer from the "execution" core indicates a sophisticated development approach meant to shield the core functionality of the malware from static analysis.

---
### **Analyst Note for Incident Response**
While there are no "hard" IOCs (like IPs or Hashes) to block immediately, the behavior suggests that detection should focus on **anomalous network traffic patterns**. Specifically, look for long-lived connections utilizing non-standard buffer lengths and the presence of multi-byte characters in communication streams, as these indicate the active use of the identified "translation" layer.

---

## Malware Family Classification

1. **Malware family**: Unknown (Sophisticated custom framework)
2. **Malware type**: RAT / Backdoor
3. **Confidence**: High
4. **Key evidence**:
    *   **Decoupled Command Architecture:** The malware utilizes a sophisticated "translation layer" that separates raw network communication from the internal command execution engine, making it difficult to analyze via standard static methods.
    *   **Sophisticated Evasion Mechanisms:** The implementation of robust Unicode/UTF-16 normalization specifically aimed at hiding command strings from security filters is a hallmark of high-end professional tooling.
    *   **Advanced Network Handling:** Use of `WS2_32.dll` for direct socket interaction and manual buffer management to process variable-length "wire format" data indicates a robust, custom C2 infrastructure typical of APT groups or advanced cybercrime syndicates.
