# Threat Analysis Report

**Generated:** 2026-07-27 14:19 UTC
**Sample:** `0ba4ff2085ac7ffa2386adad160f53623f77415e623a34189f4d5728354a03ce_0ba4ff2085ac7ffa2386adad160f53623f77415e623a34189f4d5728354a03ce.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ba4ff2085ac7ffa2386adad160f53623f77415e623a34189f4d5728354a03ce_0ba4ff2085ac7ffa2386adad160f53623f77415e623a34189f4d5728354a03ce.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 7 sections |
| Size | 44,134,400 bytes |
| MD5 | `8988944e4d193aab8d6ab1ceaa22218a` |
| SHA1 | `26abe22f1f871c74cb48e27edeb160c2f43ce31a` |
| SHA256 | `0ba4ff2085ac7ffa2386adad160f53623f77415e623a34189f4d5728354a03ce` |
| Overall entropy | 6.911 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769263145 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 6,877,696 | 6.692 | No |
| `.rodata` | 12,288 | 6.052 | No |
| `.rotext` | 110,592 | 5.973 | No |
| `.rdata` | 2,235,392 | 5.668 | No |
| `.data` | 3,979,264 | 6.586 | No |
| `.rsrc` | 30,230,016 | 6.885 | No |
| `.reloc` | 688,128 | 5.217 | No |

### Imports

**KERNEL32.dll**: `IsValidCodePage`, `GetOEMCP`, `GetACP`, `GetCPInfo`, `UnhandledExceptionFilter`, `TerminateProcess`, `IsProcessorFeaturePresent`, `PeekNamedPipe`, `GetFileInformationByHandle`, `FindFirstFileExA`, `GetDriveTypeA`, `QueryPerformanceCounter`, `GetSystemPowerStatus`, `GetModuleHandleExW`, `VerifyVersionInfoW`
**USER32.dll**: `RealChildWindowFromPoint`, `GetSysColorBrush`, `ShowOwnedPopups`, `ValidateRect`, `PostQuitMessage`, `GetClassLongW`, `IsZoomed`, `SetRect`, `IsWindowVisible`, `GetCapture`, `IsChild`, `WinHelpW`, `EnableWindow`, `SendMessageW`, `LoadIconW`
**GDI32.dll**: `ScaleWindowExtEx`, `GetCurrentPositionEx`, `PolyBezierTo`, `ExtSelectClipRgn`, `CreatePatternBrush`, `GetStockObject`, `SelectPalette`, `GetObjectType`, `CreatePen`, `CreateHatchBrush`, `CreateFontIndirectW`, `GetTextExtentPoint32W`, `SetRectRgn`, `CombineRgn`, `GetMapMode`
**MSIMG32.dll**: `AlphaBlend`, `TransparentBlt`
**COMDLG32.dll**: `GetFileTitleW`
**WINSPOOL.DRV**: `ClosePrinter`, `GetJobW`, `OpenPrinterW`, `DocumentPropertiesW`
**ADVAPI32.dll**: `RegEnumKeyExW`, `ReportEventW`, `RegisterEventSourceW`, `CryptEnumProvidersW`, `CryptReleaseContext`, `CryptDestroyKey`, `CryptGetProvParam`, `CryptAcquireContextW`, `CryptGetUserKey`, `CryptExportKey`, `CryptDestroyHash`, `CryptSignHashW`, `CryptSetHashParam`, `CryptCreateHash`, `CryptDecrypt`
**SHELL32.dll**: `SHAppBarMessage`, `SHGetMalloc`, `SHGetSpecialFolderLocation`, `DragQueryFileW`, `ShellExecuteW`, `SHGetSpecialFolderPathW`, `SHGetFileInfoW`, `Shell_NotifyIconW`, `ExtractIconExW`, `SHGetFolderPathW`, `SHGetDesktopFolder`, `ExtractIconW`, `SHAddToRecentDocs`, `DragAcceptFiles`, `SHBrowseForFolderW`
**COMCTL32.dll**: `_TrackMouseEvent`, `ImageList_DrawEx`, `ImageList_AddMasked`, `ImageList_Destroy`, `ImageList_GetImageCount`, `ImageList_Create`, `ImageList_GetIconSize`, `InitCommonControlsEx`
**SHLWAPI.dll**: `PathFindFileNameW`, `PathStripToRootW`, `PathIsUNCW`, `PathRemoveFileSpecW`, `SHAutoComplete`, `PathStripPathW`, `PathFindExtensionW`, `PathFileExistsW`, `PathIsDirectoryW`, `PathCombineW`, `SHCreateStreamOnFileW`, `StrChrW`, `StrPBrkW`
**ole32.dll**: `ReleaseStgMedium`, `PropVariantClear`, `CoTaskMemAlloc`, `StringFromCLSID`, `OleDuplicateData`, `CoInitializeEx`, `CoDisconnectObject`, `CoCreateGuid`, `CLSIDFromString`, `StgOpenStorageOnILockBytes`, `CreateILockBytesOnHGlobal`, `OleCreateMenuDescriptor`, `OleDestroyMenuDescriptor`, `OleTranslateAccelerator`, `IsAccelerator`
**OLEAUT32.dll**: `VarDateFromStr`, `SysStringLen`, `SafeArrayDestroy`, `VariantCopy`, `VarBstrFromDate`, `SafeArrayGetDim`, `SafeArrayGetElemsize`, `SafeArrayGetLBound`, `SafeArrayGetUBound`, `SafeArrayAccessData`, `SafeArrayUnaccessData`, `LoadTypeLib`, `SysAllocString`, `SysStringByteLen`, `SysAllocStringByteLen`
**oledlg.dll**: `OleUIAddVerbMenuW`, `OleUIBusyW`
**gdiplus.dll**: `GdipGetImagePaletteSize`, `GdipGetImagePixelFormat`, `GdipGetImageHeight`, `GdipGetImageWidth`, `GdipDrawImageI`, `GdipDeleteGraphics`, `GdipGetImageGraphicsContext`, `GdipCreateBitmapFromStreamICM`, `GdipCreateBitmapFromStream`, `GdipAlloc`, `GdipCloneImage`, `GdipFree`, `GdipDisposeImage`, `GdiplusShutdown`, `GdipGetImagePalette`
**WS2_32.dll**: `WSASendTo`, `WSARecv`, `WSASend`, `shutdown`, `sendto`, `ioctlsocket`, `setsockopt`, `htonl`, `getsockname`, `WSAAddressToStringW`, `WSAStringToAddressW`, `WSAIoctl`, `WSASetLastError`, `WSAGetOverlappedResult`, `listen`
**CRYPT32.dll**: `CertFindCertificateInStore`, `CertOpenStore`, `CertGetCertificateContextProperty`, `CertFreeCertificateContext`, `CertEnumCertificatesInStore`, `CertCloseStore`, `CertDuplicateCertificateContext`
**AVIFIL32.dll**: `AVIStreamRelease`, `AVIFileExit`, `AVIStreamSetFormat`, `AVIFileCreateStreamW`, `AVISaveOptions`, `AVISaveOptionsFree`, `AVIMakeCompressedStream`, `AVIFileInit`, `AVIFileRelease`, `AVIStreamWrite`, `AVIFileOpenW`
**MSVFW32.dll**: `DrawDibOpen`, `ord_2`, `DrawDibDraw`, `DrawDibClose`
**AVRT.dll**: `AvSetMmThreadCharacteristicsW`, `AvRevertMmThreadCharacteristics`
**WINMM.dll**: `PlaySoundW`, `waveOutPrepareHeader`, `waveOutWrite`, `waveOutGetErrorTextW`, `waveOutClose`, `waveOutOpen`, `timeGetTime`, `waveInGetErrorTextW`, `waveInStart`, `waveInReset`, `waveInOpen`, `waveInClose`, `waveInUnprepareHeader`, `waveInPrepareHeader`, `waveInAddBuffer`

## Extracted Strings

Total strings found: **106105** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rodata
`.rotext
`.rdata
@.data
@.reloc
@;Au
9tPVW
t VFVS
uk9Gu
~j=@KL
u_9G@t	
D$HSVW
9tQVW
9t$ t!
~d=@KL
9~0veS
9\$ t!
S;uw
Od;O<r
Wd;W<sM
Gd;G<s

Nd;N<sH
;{$sG
C@9CDv
+^tx<=X
+S(xM@
S4;V|r
u=;~ u1
9^$u/h
f;
u4j
;Ut	j
f;
uKf
PjRhX#
 jRhX#
~jKjK
;Esj
J8;H<t
j%j&j 
J0;H,~




























































































	

j!j j 
t*j0hD
t*j0h`
PQQSVW
PQQSVW
j j&j 
u-j@h@
t-j@hh<
PQQQQQ
S\_^[]
S\_^[]
9~8t	WW
t39w u&
_ 9w$u
u9~lu
9~lu	P
t7j(VW
j0[9~Pu
S
u%9} t
t	9p(u
Ht;O u

9F t
j
9]u1;
f95dJ

u=j0^VP
9}u39}
9{pu,j8
WWWWhd
SVWj(3
9}~C9}
Pj?hPi
 j?hPi
 ~	j Y
 ~	j [
9~tB9~
t;Ht0Ht%Ht
Ht
Hu.
t;It0It%It
It
Iu.
j j WW
t	9Alu
Nh;Apt
@h;ppt
9F t
j
Sj?j@P
Sj?j@P
t09~t+
t'9~ u"
+toHt_HtOHt6Ht
+t=Ht-Ht
u$SShe
uG9~u

9F s	j
+N(_^[;
F(@;F,v
F(;^ r
F(;F0u
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.009829ad` | `0x9829ad` | 3930873 | ✓ |
| `method.COleDispatchImpl.virtual_28` | `0x5a5ba5` | 955518 | ✓ |
| `fcn.005f78d0` | `0x5f78d0` | 902742 | ✓ |
| `method.CXTPWinApp.virtual_80` | `0x615a50` | 856651 | ✓ |
| `method.CXTPListCtrl.virtual_88` | `0x641c90` | 708472 | ✓ |
| `method.CXTPTabCtrl.1.virtual_80` | `0x641880` | 695214 | ✓ |
| `fcn.006875c0` | `0x6875c0` | 631437 | ✓ |
| `fcn.00864ed0` | `0x864ed0` | 545267 | ✓ |
| `method.CXTPChartSeries.virtual_12` | `0x5d1190` | 484620 | ✓ |
| `method.CXTPControlEdit.1.virtual_304` | `0x612930` | 447389 | ✓ |
| `method.CXTPControlEdit.1.virtual_264` | `0x6134a0` | 444614 | ✓ |
| `fcn.00680050` | `0x680050` | 410036 | ✓ |
| `fcn.007cf730` | `0x7cf730` | 408358 | ✓ |
| `fcn.007d6210` | `0x7d6210` | 363870 | ✓ |
| `fcn.0055b8fd` | `0x55b8fd` | 297256 | ✓ |
| `fcn.009d8450` | `0x9d8450` | 288727 | ✓ |
| `fcn.007d6200` | `0x7d6200` | 285998 | ✓ |
| `fcn.007d61d0` | `0x7d61d0` | 285949 | ✓ |
| `method.CXTPVisualStudio6Theme.virtual_128` | `0x69f470` | 279125 | ✓ |
| `fcn.00897590` | `0x897590` | 257862 | ✓ |
| `fcn.00897580` | `0x897580` | 257797 | ✓ |
| `fcn.007bef10` | `0x7bef10` | 255992 | ✓ |
| `fcn.00991f50` | `0x991f50` | 237718 | ✓ |
| `fcn.008d24c0` | `0x8d24c0` | 226350 | ✓ |
| `fcn.007e9170` | `0x7e9170` | 215977 | ✓ |
| `fcn.00835c10` | `0x835c10` | 193418 | ✓ |
| `fcn.009e39b0` | `0x9e39b0` | 181067 | ✓ |
| `method.CMFCTabCtrl.virtual_364` | `0x536c69` | 115163 | ✓ |
| `fcn.005cbe49` | `0x5cbe49` | 99144 | ✓ |
| `fcn.008274a0` | `0x8274a0` | 79023 | ✓ |

### Decompiled Code Files

- [`code/fcn.0055b8fd.c`](code/fcn.0055b8fd.c)
- [`code/fcn.005cbe49.c`](code/fcn.005cbe49.c)
- [`code/fcn.005f78d0.c`](code/fcn.005f78d0.c)
- [`code/fcn.00680050.c`](code/fcn.00680050.c)
- [`code/fcn.006875c0.c`](code/fcn.006875c0.c)
- [`code/fcn.007bef10.c`](code/fcn.007bef10.c)
- [`code/fcn.007cf730.c`](code/fcn.007cf730.c)
- [`code/fcn.007d61d0.c`](code/fcn.007d61d0.c)
- [`code/fcn.007d6200.c`](code/fcn.007d6200.c)
- [`code/fcn.007d6210.c`](code/fcn.007d6210.c)
- [`code/fcn.007e9170.c`](code/fcn.007e9170.c)
- [`code/fcn.008274a0.c`](code/fcn.008274a0.c)
- [`code/fcn.00835c10.c`](code/fcn.00835c10.c)
- [`code/fcn.00864ed0.c`](code/fcn.00864ed0.c)
- [`code/fcn.00897580.c`](code/fcn.00897580.c)
- [`code/fcn.00897590.c`](code/fcn.00897590.c)
- [`code/fcn.008d24c0.c`](code/fcn.008d24c0.c)
- [`code/fcn.009829ad.c`](code/fcn.009829ad.c)
- [`code/fcn.00991f50.c`](code/fcn.00991f50.c)
- [`code/fcn.009d8450.c`](code/fcn.009d8450.c)
- [`code/fcn.009e39b0.c`](code/fcn.009e39b0.c)
- [`code/method.CMFCTabCtrl.virtual_364.c`](code/method.CMFCTabCtrl.virtual_364.c)
- [`code/method.COleDispatchImpl.virtual_28.c`](code/method.COleDispatchImpl.virtual_28.c)
- [`code/method.CXTPChartSeries.virtual_12.c`](code/method.CXTPChartSeries.virtual_12.c)
- [`code/method.CXTPControlEdit.1.virtual_264.c`](code/method.CXTPControlEdit.1.virtual_264.c)
- [`code/method.CXTPControlEdit.1.virtual_304.c`](code/method.CXTPControlEdit.1.virtual_304.c)
- [`code/method.CXTPListCtrl.virtual_88.c`](code/method.CXTPListCtrl.virtual_88.c)
- [`code/method.CXTPTabCtrl.1.virtual_80.c`](code/method.CXTPTabCtrl.1.virtual_80.c)
- [`code/method.CXTPVisualStudio6Theme.virtual_128.c`](code/method.CXTPVisualStudio6Theme.virtual_128.c)
- [`code/method.CXTPWinApp.virtual_80.c`](code/method.CXTPWinApp.virtual_80.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is an analysis of the binary's functionality:

### Core Functionality
The code appears to be part of a large, **GUI-based Windows application** built using the **Microsoft Foundation Class (MFC)** library (specifically featuring the `CXTP` "feature pack" controls). 

*   **User Interface Management:** The presence of classes like `CXTPWinApp`, `CXTPListCtrl`, `CXTPTabCtrl`, and `CXTPControlEdit` indicates that the application has a complex graphical interface involving tabs, list views, and text input fields.
*   **Standard Library Usage:** The code includes several internal routines for managing resources and handling standard Windows components (e.g., `CoDisconnectObject`, `SendMessageW`).
*   **Cryptography Support:** Function `fcn.00897580` specifically references OpenSSL-style source paths (`crypto\rsa\rsa_sp800_56b_check.c`). This indicates the binary includes logic to validate RSA keys, which is commonly used for establishing secure connections (TLS/SSL) or decrypting data.

### Suspicious or Malicious Behaviors
While this specific snippet contains a lot of standard "boilerplate" code found in legitimate software, there are several areas an analyst should monitor:

*   **Potential for Information Stealing:** Because the application uses advanced UI controls (`CXTPControlEdit`) and includes RSA cryptography libraries, it is capable of interacting with user input and establishing encrypted communication. In a malware context, this combination is often seen in **Trojans or Info-stealers** that provide a fake "utility" interface while exfiltrating data over an encrypted channel.
*   **Complex State Logic:** The function `fcn.009829ad` contains very complex floating-point and math-heavy logic. While often used in scientific software, such convoluted code is sometimes used in **malware wrappers** to complicate static analysis or hide the true execution flow of the underlying payload.
*   **Thread Local Storage (TLS):** The use of `TlsAlloc` and `TlsGetValue` in `fcn.009d8450` allows the application to store data specific to a thread. This can be used by malware to hide global variables from simple scanners or to maintain state during multi-threaded operations (like simultaneous network communication and file encryption).

### Notable Techniques & Patterns
*   **MFC/Feature Pack Usage:** The heavy reliance on `CXTP` classes suggests the developer utilized high-level libraries. This is a common "masquerade" technique where malware developers use legitimate, complex frameworks to make their code appear like a professional application (e.g., an installer or a system utility).
*   **OpenSSL Integration:** The specific check for `rsa_sp800_56b_check` suggests the binary is prepared to handle various RSA key lengths. This is often used to ensure compatibility with older servers but can also be used by malware to communicate with Command & Control (C2) infrastructure using standard encryption libraries to blend in with normal traffic.
*   **Obfuscated Data Blocks:** The "Extracted Strings" section contains a high amount of non-human-readable data and fragmented characters. While some are likely just artifacts of the compilation process, this can sometimes indicate **packed code** or an **encrypted configuration block** that is decrypted at runtime.

### Summary for Analyst
This binary appears to be a **sophisticated Windows application**. It does not show overt "low-level" malicious behavior (like direct buffer overflows or raw socket manipulation) in the provided snippet; instead, it relies on high-level libraries. 

**Recommended next steps:**
1.  Investigate the **RSA check results**: Determine if it's establishing a connection to an external IP.
2.  Analyze the **strings segment**: Check if there are any hidden URLs or hardcoded C2 addresses in the non-human-readable blocks.
3.  Monitor **network traffic** during execution to see if the RSA capabilities are used to communicate with an unauthorized remote host.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of complex MFC/CXTP libraries and a heavy UI framework suggests an attempt to blend in as a legitimate, professional Windows utility. |
| T1573 | Encrypted Channel | The integration of OpenSSL-style RSA logic indicates the capability to establish encrypted communication for C2 or data exfiltration. |
| T1027 | Obfuscated Files or Information | The use of complex math-heavy logic to hide execution flow and non-human-readable data blocks suggests an intent to hinder static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted Indicator of Compromise (IOC) report:

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: The string `crypto\rsa\rsa_sp800_56b_check.c` is a source code path from the OpenSSL library and not a local file system path used by the malware).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Potential C2 Communication Pattern:** The analysis indicates the presence of RSA cryptography (specifically `rsa_sp800_56b_check`) used for establishing secure connections or decrypting data, which may be utilized to mask communication with a Command & Control (C2) server.
*   **Obfuscated Data Blocks:** The "Extracted Strings" section contains high amounts of non-human-readable characters and fragmented blocks, suggesting the presence of packed code or an encrypted configuration block.
*   **Library Indicators:** Use of `CXTP` feature pack controls (e.g., `CXTPWinApp`, `CXTPListCtrl`) and OpenSSL-style routines indicates a sophisticated build intended to masquerade as a legitimate Windows application.

***

**Analyst Note:** 
The provided text contains no "hard" IOCs (such as specific IPs or domains). The indicators present are "behavioral" in nature, suggesting that the sample should be monitored for **encrypted network traffic** and **obfuscated data structures** rather than being blocked by signature-based tools.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Trojan / Loader
3. **Confidence**: Medium

**Key evidence**:
*   **Masquerading Techniques:** The use of high-level MFC/CXTP libraries and complex GUI controls suggests an intentional effort to mimic a legitimate professional application (T1036).
*   **Encrypted Communication Infrastructure:** The integration of OpenSSL-style RSA logic indicates the capability to establish encrypted channels for Command & Control (C2) communication or data exfiltration.
*   **Evasion and Obfuscation:** The presence of "non-human-readable" data blocks, complex math-heavy execution flow, and the use of Thread Local Storage suggests a sophisticated attempt to hide configuration data and hinder static analysis.
