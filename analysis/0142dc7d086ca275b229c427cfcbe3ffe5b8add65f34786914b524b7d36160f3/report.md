# Threat Analysis Report

**Generated:** 2026-06-26 20:27 UTC
**Sample:** `0142dc7d086ca275b229c427cfcbe3ffe5b8add65f34786914b524b7d36160f3_0142dc7d086ca275b229c427cfcbe3ffe5b8add65f34786914b524b7d36160f3.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0142dc7d086ca275b229c427cfcbe3ffe5b8add65f34786914b524b7d36160f3_0142dc7d086ca275b229c427cfcbe3ffe5b8add65f34786914b524b7d36160f3.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 7 sections |
| Size | 23,817,216 bytes |
| MD5 | `48cacc507827b8916ddc5513b8fc81d4` |
| SHA1 | `86283bb8cc0fa0ac8cfc4c77657ca05b951e0104` |
| SHA256 | `0142dc7d086ca275b229c427cfcbe3ffe5b8add65f34786914b524b7d36160f3` |
| Overall entropy | 7.245 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1408128053 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 9,505,280 | 6.592 | No |
| `.rdata` | 12,198,912 | 7.464 | ⚠️ Yes |
| `.data` | 109,568 | 5.147 | No |
| `.tls` | 512 | -0.0 | No |
| `.qtmetad` | 2,048 | 4.325 | No |
| `_RDATA` | 512 | 3.518 | No |
| `.rsrc` | 1,999,360 | 6.192 | No |

### Imports

**KERNEL32.dll**: `QueryPerformanceCounter`, `QueryPerformanceFrequency`, `GetQueuedCompletionStatus`, `CreateIoCompletionPort`, `PeekNamedPipe`, `CancelIo`, `FindCloseChangeNotification`, `FindFirstChangeNotificationW`, `FindNextChangeNotification`, `GetCurrentProcess`, `GetModuleFileNameW`, `GetProcAddress`, `GetSystemTime`, `CompareStringW`, `GetUserDefaultLCID`
**USER32.dll**: `GetWindowRect`, `ShowWindow`, `SetWindowPos`, `GetDC`, `CreateWindowExW`, `RegisterClassExW`, `DefWindowProcW`, `MessageBoxA`, `GetProcessWindowStation`, `GetUserObjectInformationW`, `RealGetWindowClassW`, `SystemParametersInfoW`, `GetIconInfo`, `CreateIconIndirect`, `DrawIconEx`
**SHELL32.dll**: `SHGetFileInfoW`, `SHGetMalloc`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetSpecialFolderPathW`, `SHFileOperationW`, `ShellExecuteW`, `SHGetFolderPathW`, `CommandLineToArgvW`, `Shell_NotifyIconW`
**ole32.dll**: `CoTaskMemAlloc`, `CoGetMalloc`, `CreateBindCtx`, `ReleaseStgMedium`, `DoDragDrop`, `OleIsCurrentClipboard`, `OleFlushClipboard`, `OleGetClipboard`, `OleSetClipboard`, `OleUninitialize`, `OleInitialize`, `RevokeDragDrop`, `RegisterDragDrop`, `CoLockObjectExternal`, `CoTaskMemFree`
**ADVAPI32.dll**: `OpenProcessToken`, `FreeSid`, `GetLengthSid`, `GetTokenInformation`, `RegCreateKeyExW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegEnumValueW`, `RegFlushKey`, `RegQueryInfoKeyW`, `RegSetValueExW`, `AddAccessAllowedAce`, `AllocateAndInitializeSid`, `InitializeAcl`, `InitializeSecurityDescriptor`
**GDI32.dll**: `AddFontResourceExW`, `GetDIBits`, `CreateDIBSection`, `GetObjectW`, `CombineRgn`, `CreateRectRgn`, `GetRegionData`, `SelectClipRgn`, `GdiFlush`, `BitBlt`, `OffsetRgn`, `GetDeviceCaps`, `GetTextFaceW`, `ExtTextOutW`, `SetWorldTransform`
**gdiplus.dll**: `GdipDeletePen`, `GdipDrawLineI`, `GdipSetCompositingMode`, `GdipDeleteGraphics`, `GdipCreatePen1`, `GdipSetSolidFillColor`, `GdipCreateSolidFill`, `GdipCloneBrush`, `GdipDeleteBrush`, `GdipAlloc`, `GdipFree`, `GdipCreateFromHDC`, `GdipFillRectangleI`, `GdiplusStartup`
**WS2_32.dll**: `getsockopt`, `htonl`, `WSANtohl`, `inet_addr`, `ntohl`, `gethostbyaddr`, `gethostbyname`, `WSAGetLastError`, `WSAAsyncSelect`, `__WSAFDIsSet`, `bind`, `closesocket`, `WSASocketW`, `WSASendTo`, `WSASend`
**OLEAUT32.dll**: `VariantClear`, `SystemTimeToVariantTime`, `VariantChangeType`, `VariantInit`, `SysStringLen`, `SysFreeString`, `SysAllocStringLen`, `SysAllocString`
**IMM32.dll**: `ImmNotifyIME`, `ImmSetCandidateWindow`, `ImmSetCompositionWindow`, `ImmGetCompositionStringW`, `ImmReleaseContext`, `ImmGetDefaultIMEWnd`, `ImmGetContext`
**WINMM.dll**: `waveInReset`, `waveOutReset`, `waveOutRestart`, `waveOutPause`, `PlaySoundW`, `waveOutGetNumDevs`, `waveOutGetDevCapsW`, `waveInGetNumDevs`, `waveInGetDevCapsW`, `waveInOpen`, `waveInClose`, `waveInPrepareHeader`, `waveInUnprepareHeader`, `waveInAddBuffer`, `waveInStart`
**OPENGL32.dll**: `glTexSubImage2D`, `wglShareLists`, `wglMakeCurrent`, `wglGetProcAddress`, `wglGetCurrentDC`, `glBindTexture`, `glBlendFunc`, `glClear`, `glClearColor`, `glClearDepth`, `glClearStencil`, `glColorMask`, `glCopyTexImage2D`, `glCopyTexSubImage2D`, `glCullFace`

### Exports

`z_adler32`, `z_adler32_combine`, `z_adler32_combine64`, `z_compress`, `z_compress2`, `z_compressBound`, `z_crc32`, `z_crc32_combine`, `z_crc32_combine64`, `z_deflate`, `z_deflateBound`, `z_deflateCopy`, `z_deflateEnd`, `z_deflateInit2_`, `z_deflateInit_`, `z_deflateParams`, `z_deflatePrime`, `z_deflateReset`, `z_deflateSetDictionary`, `z_deflateSetHeader`, `z_deflateTune`, `z_get_crc_table`, `z_inflate`, `z_inflateCopy`, `z_inflateEnd`, `z_inflateGetHeader`, `z_inflateInit2_`, `z_inflateInit_`, `z_inflateMark`, `z_inflatePrime`, `z_inflateReset`, `z_inflateReset2`, `z_inflateSetDictionary`, `z_inflateSync`, `z_inflateSyncPoint`, `z_inflateUndermine`, `z_uncompress`, `z_zError`, `z_zlibCompileFlags`, `z_zlibVersion`

## Extracted Strings

Total strings found: **89407** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.qtmetad
P_RDATA
@.rsrc
D$`3WPVV
T$03D$0
L$83L$H
T$<3T$L
T$41T$$
T$81T$(
L$ 3L$0
D$`3WP
T$41T$$
T$81T$(
L$ 3L$0
\$pUVW
L$ URP
_^][3
L$(PQRW
G;Ft
G;|$ |
T$$j@R
D$dj@P
D$$PWWS
L$$QSRP
L$$QVVV
L$$QPPP
MRPWQ
L$4UQP
L$(UPVQ
L$4UQVSj
(WRUQP
D$(WRKP
D$ QRPPP
T$Vu)
u:9G(u5
D$PWSQVV
tP)l$tA
W9l$4tA
9nt/W
D$ SUP
L$4QPSW
jsj~j 
jsjuj 
j~juj 

	

t3VWUS
t(9(t$
9t$Lt"j`h@
|$DrtTh
|$($t#h
3W;|$
3W;|$
T`00P`00P
V++}V++}
L&&jL&&jl66Zl66Z~??A~??A
Oh44\h44\Q
sb11Sb11S*
RF##eF##e
&N''iN''i
X,,tX,,t4
v;;Mv;;M
R)){R)){
>^//q^//q
,@  `@  `
r99Kr99K
f33Uf33U
x<<Dx<<D%
p88Hp88H
uB!!cB!!c 
z==Gz==G
D""fD""fT**~T**~;
;d22Vd22Vt::Nt::N

H$$lH$$l
Cn77Yn77Y
J%%oJ%%o\..r\..r8
|>>B|>>Bq
j55_j55_
P((xP((x
Z--wZ--w
V_^[]
3W;|$
3W;|$
P~AeS~AeS
pHhXpHhX
lZrNlZrN
6-9'6-9'

$6.:$6.:
g
ZwKiZwKi
T~FbT~Fb
*?#1*?#1
>8$4,8$4,
pHl\tHl\t
cU!}R	j
cU!}R	j
cU!}R	j
cU!}USVW
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.006ecd30` | `0x6ecd30` | 5409715 | ✓ |
| `method.QFile.virtual_8` | `0x760a10` | 4890517 | ✓ |
| `method.FlatTextarea.2.virtual_64` | `0x54dd00` | 4574344 | ✓ |
| `fcn.009f7670` | `0x9f7670` | 3665264 | ✓ |
| `fcn.00c73110` | `0xc73110` | 3395742 | ✓ |
| `fcn.00bc7840` | `0xbc7840` | 3245111 | ✓ |
| `fcn.00bc9350` | `0xbc9350` | 3232637 | ✓ |
| `fcn.009afde0` | `0x9afde0` | 3017269 | ✓ |
| `fcn.00bc4d30` | `0xbc4d30` | 2586084 | ✓ |
| `fcn.00484af0` | `0x484af0` | 2026769 | ✓ |
| `fcn.00ab3910` | `0xab3910` | 1738699 | ✓ |
| `fcn.009b93a0` | `0x9b93a0` | 1488993 | ✓ |
| `fcn.009a9010` | `0x9a9010` | 1481204 | ✓ |
| `fcn.008034e0` | `0x8034e0` | 1262469 | ✓ |
| `fcn.0047e400` | `0x47e400` | 1182649 | ✓ |
| `fcn.00b17030` | `0xb17030` | 1179016 | ✓ |
| `fcn.009f9ec0` | `0x9f9ec0` | 1097742 | ✓ |
| `fcn.009f9f30` | `0x9f9f30` | 1097699 | ✓ |
| `method.QStyleSheetStyle.virtual_8` | `0xa0c8c0` | 1022389 | ✓ |
| `fcn.00a253c0` | `0xa253c0` | 1011392 | ✓ |
| `method.QGestureRecognizer.virtual_4` | `0xb411e0` | 926418 | ✓ |
| `fcn.009f7660` | `0x9f7660` | 925895 | ✓ |
| `fcn.009f7620` | `0x9f7620` | 925002 | ✓ |
| `fcn.009f7500` | `0x9f7500` | 924931 | ✓ |
| `fcn.009f6e00` | `0x9f6e00` | 922263 | ✓ |
| `fcn.00b25850` | `0xb25850` | 901242 | ✓ |
| `fcn.00b23330` | `0xb23330` | 900291 | ✓ |
| `fcn.00482ef0` | `0x482ef0` | 851684 | ✓ |
| `fcn.0047cf10` | `0x47cf10` | 834026 | ✓ |
| `fcn.00815a70` | `0x815a70` | 828169 | ✓ |

### Decompiled Code Files

- [`code/fcn.0047cf10.c`](code/fcn.0047cf10.c)
- [`code/fcn.0047e400.c`](code/fcn.0047e400.c)
- [`code/fcn.00482ef0.c`](code/fcn.00482ef0.c)
- [`code/fcn.00484af0.c`](code/fcn.00484af0.c)
- [`code/fcn.006ecd30.c`](code/fcn.006ecd30.c)
- [`code/fcn.008034e0.c`](code/fcn.008034e0.c)
- [`code/fcn.00815a70.c`](code/fcn.00815a70.c)
- [`code/fcn.009a9010.c`](code/fcn.009a9010.c)
- [`code/fcn.009afde0.c`](code/fcn.009afde0.c)
- [`code/fcn.009b93a0.c`](code/fcn.009b93a0.c)
- [`code/fcn.009f6e00.c`](code/fcn.009f6e00.c)
- [`code/fcn.009f7500.c`](code/fcn.009f7500.c)
- [`code/fcn.009f7620.c`](code/fcn.009f7620.c)
- [`code/fcn.009f7660.c`](code/fcn.009f7660.c)
- [`code/fcn.009f7670.c`](code/fcn.009f7670.c)
- [`code/fcn.009f9ec0.c`](code/fcn.009f9ec0.c)
- [`code/fcn.009f9f30.c`](code/fcn.009f9f30.c)
- [`code/fcn.00a253c0.c`](code/fcn.00a253c0.c)
- [`code/fcn.00ab3910.c`](code/fcn.00ab3910.c)
- [`code/fcn.00b17030.c`](code/fcn.00b17030.c)
- [`code/fcn.00b23330.c`](code/fcn.00b23330.c)
- [`code/fcn.00b25850.c`](code/fcn.00b25850.c)
- [`code/fcn.00bc4d30.c`](code/fcn.00bc4d30.c)
- [`code/fcn.00bc7840.c`](code/fcn.00bc7840.c)
- [`code/fcn.00bc9350.c`](code/fcn.00bc9350.c)
- [`code/fcn.00c73110.c`](code/fcn.00c73110.c)
- [`code/method.FlatTextarea.2.virtual_64.c`](code/method.FlatTextarea.2.virtual_64.c)
- [`code/method.QFile.virtual_8.c`](code/method.QFile.virtual_8.c)
- [`code/method.QGestureRecognizer.virtual_4.c`](code/method.QGestureRecognizer.virtual_4.c)
- [`code/method.QStyleSheetStyle.virtual_8.c`](code/method.QStyleSheetStyle.virtual_8.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is a technical analysis of the binary's behavior.

### Core Functionality and Purpose
The binary appears to be a **GUI-based application** developed using the **Qt Framework**. The presence of several specific class names and internal structures confirms this:
*   **Framework Indicators:** The code references `QFile`, `QPlatformScreen`, `QWindowsTheme`, `QStandardItemModel`, and `QGestureRecognizer`. These are standard components of the Qt libraries used for cross-platform UI development.
*   **Graphics Handling:** Function `fcn.00bc4d30` explicitly handles OpenGL contexts (`wglDeleteContext`) and `QPlatformOpenGLContext`, suggesting the application has graphical rendering capabilities (e.g., a game, media player, or complex data visualization tool).
*   **UI Management:** Functions like `method.FlatTextarea.2.virtual_64` and `fcn.0047e400` deal with text area manipulation and coordinate/geometry calculations for UI layout.

### Suspicious or Malicious Behaviors
Based on the provided snippet, there is **no direct evidence** of high-impact malicious activities like process injection, file system tampering (outside of standard library calls), or network communication. However, a few items are noteworthy:

*   **System Tray Interaction:** In `fcn.009f7670`, the code calls `Shell_NotifyIconW` and manages icons (`DestroyIcon`). While commonly used by legitimate apps to display icons in the system tray (e.g., for notification badges), this functionality is also frequently used by malware to maintain a presence on the system while staying out of the primary taskbar view.
*   **Encryption Capabilities:** The extracted strings show `AES for x86, CRYPTOGAMS by <appro@openssl.org>`. This confirms that the application includes libraries for strong encryption/decryption. While this could be used for secure communication, it is also a prerequisite for ransomware or for encrypting and decrypting malicious payloads in transit.

### Notable Techniques and Patterns
*   **Abstraction via Framework:** The code is highly abstracted through the Qt library. This makes static analysis more difficult because many "manual" behaviors (like memory management or complex loops) are hidden behind high-level functions.
*   **Standard Library Padding:** The large number of `fcn.` prefixes and standard logic for handling list types, views, and icons suggest a large, complex application rather than a small piece of targeted malware.
*   **High Complexity in Layout Math:** Function `fcn.0047e400` contains complex arithmetic to calculate positions and sizes (likely used during "window resizing" or "layout refreshing"). This type of complexity is common in heavy GUI applications but can be used as a "noise" tactic to slow down automated analysis tools.

### Summary Table
| Feature | Observation | Note |
| :--- | :--- | :--- |
| **Core Function** | Graphical UI Application | Built with Qt; uses OpenGL for rendering. |
| **Persistence/Stealth** | `Shell_NotifyIconW` | Standard "Tray" icon support, but usable by malware for presence. |
| **Encryption** | AES / OpenSSL | Strong encryption primitives are present in the binary. |
| **Anti-Analysis** | None detected | No immediate evidence of packing or anti-debugging logic in this snippet. |

**Conclusion:** The sample appears to be a legitimate (or "wrapped") application utilizing standard development frameworks. However, because it contains strong encryption capabilities and system tray interaction functionality, it warrants closer inspection of the networking modules (not shown) and any potential for "living off the land" behavior if the intent is malicious.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscation | The use of complex library abstractions and high-level code "noise" is intended to complicate static analysis, while the inclusion of AES/OpenSSL encryption provides a means to hide malicious payload content. |
| T1564 | Hide Artifacts | The implementation of `Shell_NotifyIconW` allows the application to maintain a persistent presence on the system while remaining hidden from the primary taskbar view. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The source material contains many obfuscated string fragments and internal function offsets (e.g., `fcn.00bc4d30`) which were excluded as they are not unique to a threat actor or specific malware instance.

### **IP addresses / URLs / Domains**
*   None detected.

### **File paths / Registry keys**
*   None detected.

### **Mutex names / Named pipes**
*   None detected.

### **Hashes**
*   None detected.

### **Other artifacts**
*   **API Usage (Persistence/Stealth):** `Shell_NotifyIconW` (Used for system tray presence).
*   **Encryption Library:** `AES for x86, CRYPTOGAMS by <appro@openssl.org>` (Indicates the use of OpenSSL libraries for encryption/decryption).
*   **Framework Infrastructure:** Qt Framework (References to `QFile`, `QPlatformScreen`, `QWindowsTheme`).

---
**Analyst Note:** The analysis suggests this may be a legitimate application or a "wrapper" due to the high amount of standard library code and lack of specific malicious infrastructure (IPs/Domains). However, the presence of AES encryption and System Tray functionality are common traits in both utility software and malware.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: Low

**Key evidence**:
*   **Ambiguous Behavior:** The sample utilizes the Qt Framework and OpenGL, characteristics typical of complex, legitimate GUI applications. There is no direct evidence of high-impact malicious behavior (e.g., process injection or unauthorized data exfiltration) in the provided analysis.
*   **Dual-Use Functionalities:** While the inclusion of AES/OpenSSL encryption and `Shell_NotifyIconW` (system tray persistence) are common in malware to hide payloads and maintain a presence, they are also standard features for legitimate software utility components.
*   **Lack of Attribution/IOCs:** No specific indicators of compromise (IPs, domains, or unique strings) were found to link the sample to any known threat actor or specific campaign, suggesting it may be a generic "wrapper" or a legitimate application currently being analyzed for suspicious traits.
