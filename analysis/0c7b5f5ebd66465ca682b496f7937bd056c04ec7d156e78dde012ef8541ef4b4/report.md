# Threat Analysis Report

**Generated:** 2026-07-31 15:06 UTC
**Sample:** `0c7b5f5ebd66465ca682b496f7937bd056c04ec7d156e78dde012ef8541ef4b4_0c7b5f5ebd66465ca682b496f7937bd056c04ec7d156e78dde012ef8541ef4b4.dll`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c7b5f5ebd66465ca682b496f7937bd056c04ec7d156e78dde012ef8541ef4b4_0c7b5f5ebd66465ca682b496f7937bd056c04ec7d156e78dde012ef8541ef4b4.dll` |
| File type | PE32 executable for MS Windows 5.00 (DLL), Intel i386, 6 sections |
| Size | 27,112,504 bytes |
| MD5 | `2037857e20d02f17e02ea70de6a297ff` |
| SHA1 | `f66d8189c89f27471bf60d5d9d284fab7363add5` |
| SHA256 | `0c7b5f5ebd66465ca682b496f7937bd056c04ec7d156e78dde012ef8541ef4b4` |
| Overall entropy | 7.528 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1531786734 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 9,937,408 | 6.698 | No |
| `.rdata` | 1,673,728 | 5.805 | No |
| `.data` | 111,104 | 4.869 | No |
| `.unwante` | 3,584 | 4.34 | No |
| `.rsrc` | 2,857,472 | 6.37 | No |
| `.reloc` | 1,081,856 | 7.234 | ⚠️ Yes |

### Imports

**IMM32.dll**: `ImmReleaseContext`, `ImmSetCompositionWindow`, `ImmSetCandidateWindow`, `ImmGetContext`
**KERNEL32.dll**: `GetDiskFreeSpaceA`, `GetModuleHandleW`, `GetTickCount`, `GetCurrentDirectoryW`, `TlsSetValue`, `TlsGetValue`, `TlsAlloc`, `GetFileAttributesW`, `Sleep`, `GetModuleFileNameW`, `OutputDebugStringW`, `IsValidCodePage`, `GetACP`, `WideCharToMultiByte`, `MultiByteToWideChar`
**USER32.dll**: `UnhookWindowsHookEx`, `SetTimer`, `GetQueueStatus`, `RegisterWindowMessageW`, `KillTimer`, `GetIconInfo`, `GetLastInputInfo`, `EnumDisplaySettingsW`, `MonitorFromWindow`, `GetMonitorInfoW`, `NotifyWinEvent`, `SendMessageW`, `GetDesktopWindow`, `DefWindowProcA`, `SetWindowLongA`
**GDI32.dll**: `GetTextMetricsW`, `GetOutlineTextMetricsW`, `GetGlyphOutlineW`, `GetCharWidthI`, `CreateRectRgn`, `GetRgnBox`, `GetWorldTransform`, `IntersectClipRect`, `SetWorldTransform`, `ModifyWorldTransform`, `RestoreDC`, `SaveDC`, `SetGraphicsMode`, `GetCurrentObject`, `SetBkMode`
**SHELL32.dll**: `SHCreateDirectoryExW`, `DragAcceptFiles`, `DragQueryFileW`, `SHGetFileInfoW`, `ExtractIconExW`, `DragFinish`
**ole32.dll**: `ReleaseStgMedium`, `OleGetClipboard`, `CoInitialize`, `CoUninitialize`, `CoCreateInstance`, `OleDuplicateData`
**SHLWAPI.dll**: `PathRemoveFileSpecW`, `PathFindFileNameW`, `PathCombineA`, `PathAppendW`, `SHGetValueW`, `PathIsUNCW`, `PathFileExistsA`, `PathIsUNCA`, `PathFindExtensionW`, `PathRemoveExtensionW`, `PathRenameExtensionW`, `PathGetCharTypeW`, `PathCombineW`, `PathFileExistsW`
**IPHLPAPI.DLL**: `GetAdaptersAddresses`, `NotifyAddrChange`
**WINMM.dll**: `timeEndPeriod`, `timeBeginPeriod`, `timeGetTime`
**WS2_32.dll**: `gethostbyname`, `recv`, `gethostname`, `__WSAFDIsSet`, `getsockname`, `getpeername`, `WSACleanup`, `WSAIoctl`, `ntohs`, `freeaddrinfo`, `getaddrinfo`, `socket`, `bind`, `setsockopt`, `closesocket`
**COMDLG32.dll**: `GetOpenFileNameW`
**ADVAPI32.dll**: `CryptReleaseContext`, `RegisterEventSourceW`, `CryptGenRandom`, `CryptAcquireContextW`, `RegCloseKey`, `RegQueryValueExW`, `RegEnumKeyExW`, `RegOpenKeyExW`, `CryptEnumProvidersW`, `CryptDestroyKey`, `CryptGetProvParam`, `CryptGetUserKey`, `CryptExportKey`, `CryptDestroyHash`, `CryptSignHashW`
**USP10.dll**: `ScriptShape`, `ScriptItemize`, `ScriptPlace`, `ScriptXtoCP`, `ScriptStringAnalyse`, `ScriptStringOut`, `ScriptFreeCache`, `ScriptStringFree`
**VERSION.dll**: `GetFileVersionInfoSizeW`, `VerQueryValueW`, `GetFileVersionInfoW`
**CRYPT32.dll**: `CertCloseStore`, `CertDuplicateCertificateContext`, `CertGetCertificateContextProperty`, `CertEnumCertificatesInStore`, `CertFindCertificateInStore`, `CertOpenStore`, `CertFreeCertificateContext`
**WLDAP32.dll**: `ord_26`, `ord_50`, `ord_60`, `ord_143`, `ord_211`, `ord_30`, `ord_200`, `ord_32`, `ord_35`, `ord_79`, `ord_33`, `ord_301`, `ord_27`, `ord_22`, `ord_41`

### Exports

`wkeAddDirtyArea`, `wkeCanGoBack`, `wkeCanGoForward`, `wkeConfigure`, `wkeCreateWebView`, `wkeCreateWebWindow`, `wkeDestroyWebView`, `wkeDestroyWebWindow`, `wkeEditorCopy`, `wkeEditorCut`, `wkeEditorDelete`, `wkeEditorPaste`, `wkeEditorSelectAll`, `wkeEnableWindow`, `wkeFinalize`, `wkeFireContextMenuEvent`, `wkeFireKeyDownEvent`, `wkeFireKeyPressEvent`, `wkeFireKeyUpEvent`, `wkeFireMouseEvent`, `wkeFireMouseWheelEvent`, `wkeGetCaretRect`, `wkeGetContentHeight`, `wkeGetContentWidth`, `wkeGetCookie`, `wkeGetCookieW`, `wkeGetHeight`, `wkeGetHostWindow`, `wkeGetMediaVolume`, `wkeGetName`, `wkeGetRepaintInterval`, `wkeGetString`, `wkeGetStringW`, `wkeGetTitle`, `wkeGetTitleW`, `wkeGetVersion`, `wkeGetVersionString`, `wkeGetViewDC`, `wkeGetWebView`, `wkeGetWidth`, `wkeGetWindowHandle`, `wkeGetZoomFactor`, `wkeGlobalExec`, `wkeGoBack`, `wkeGoForward`, `wkeInitialize`, `wkeInitializeEx`, `wkeIsAwake`, `wkeIsCookieEnabled`, `wkeIsDirty`

## Extracted Strings

Total strings found: **71104** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.unwante
@.rsrc
@.reloc
t:9M$u
ESVWP
ESVWP
ESVWP
#q1,N
pgl4A3
;]tCVW
E_^[]
A8+A4]
}>;~0t9
};;_0t6
};;_0t6
ur8F<u
}%;~0t 




























































































	
0V 3G$
G(2F($
u#9}u
}WSRPQ
EQRPV
MWSQR













































































































	
MSPQW
ESRPW
D$_[^Y
D$_[^Y
VWu	QS
EPWQS
C98uF
9GtM9E
uN8FtI
URVPW
@RQPW
URVWS
WRSQPV
;Ute3
UWVQR
EQRPS
OPu
V
N0PRVWQ
;C0v!=
0^;Q0s#
;AvLSV
9}~1V
UPQRW
USPQRW
J(WSVQP
EQRWPV
J(WSVQP
F@RVPVj
EQRPS
QRPWVS
PQRWVS
9Y@u&j
G$SVWP
uD8Ft?
8BCtZh

sEPSh
u%8X@t 
JP99u
u-R;y0s

sFPQh
8XCtZh
QRSPWV
QRPSWV
UPQRW
																																																				
							
{,;{4smV
F,;F4s
;>v;~
;>v;~
F@9N@u 
F@9N@u 
uQf9WuK
uQf9_
uK
u
f9_

uSf9WuM
uSf9_
uM
uSf9_
uM
N,+N0_
:
t	KA
M+At
[9>u
^@SWRQP
~@WSRQP
^@SRQP
^0SPRQ
V0SQRj
VWPQRQ
;>v;~
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.wke.dll_wkeSetFileSystem` | `0x10005dd0` | 7717041 | ✓ |
| `fcn.106b5bd0` | `0x106b5bd0` | 6331588 | ✓ |
| `fcn.10569470` | `0x10569470` | 3859516 | ✓ |
| `fcn.103f0da0` | `0x103f0da0` | 3201354 | ✓ |
| `method.WebCore::PlatformStrategies.virtual_12` | `0x10237260` | 3164697 | ✓ |
| `fcn.10243800` | `0x10243800` | 3162250 | ✓ |
| `fcn.104f8280` | `0x104f8280` | 2887303 | ✓ |
| `fcn.1023f9e0` | `0x1023f9e0` | 2532575 | ✓ |
| `fcn.10295260` | `0x10295260` | 2501321 | ✓ |
| `sym.wke.dll_wkeSleep` | `0x10006400` | 2298888 | ✓ |
| `fcn.103bc120` | `0x103bc120` | 2101659 | ✓ |
| `fcn.103bc080` | `0x103bc080` | 2101405 | ✓ |
| `sym.wke.dll_wkeGetRepaintInterval` | `0x100069e0` | 1845495 | ✓ |
| `fcn.10412110` | `0x10412110` | 1786786 | ✓ |
| `fcn.103e7870` | `0x103e7870` | 1772998 | ✓ |
| `fcn.103bc0d0` | `0x103bc0d0` | 1769437 | ✓ |
| `fcn.103e7b80` | `0x103e7b80` | 1749131 | ✓ |
| `fcn.103e75c0` | `0x103e75c0` | 1748501 | ✓ |
| `fcn.103e7cb0` | `0x103e7cb0` | 1669208 | ✓ |
| `fcn.103e7d00` | `0x103e7d00` | 1669160 | ✓ |
| `fcn.103e7170` | `0x103e7170` | 1669147 | ✓ |
| `fcn.1057e990` | `0x1057e990` | 1602223 | ✓ |
| `fcn.10480790` | `0x10480790` | 1419380 | ✓ |
| `sym.wke.dll_wkeGetHostWindow` | `0x100069b0` | 1153828 | ✓ |
| `sym.wke.dll_wkeJSCollectGarbge` | `0x10002480` | 1101523 | ✓ |
| `fcn.104f2a00` | `0x104f2a00` | 1056389 | ✓ |
| `fcn.104f2a20` | `0x104f2a20` | 1056348 | ✓ |
| `fcn.1010d480` | `0x1010d480` | 1014724 | ✓ |
| `fcn.1052b7f0` | `0x1052b7f0` | 917726 | ✓ |
| `fcn.107a1310` | `0x107a1310` | 627371 | ✓ |

### Decompiled Code Files

- [`code/fcn.1010d480.c`](code/fcn.1010d480.c)
- [`code/fcn.1023f9e0.c`](code/fcn.1023f9e0.c)
- [`code/fcn.10243800.c`](code/fcn.10243800.c)
- [`code/fcn.10295260.c`](code/fcn.10295260.c)
- [`code/fcn.103bc080.c`](code/fcn.103bc080.c)
- [`code/fcn.103bc0d0.c`](code/fcn.103bc0d0.c)
- [`code/fcn.103bc120.c`](code/fcn.103bc120.c)
- [`code/fcn.103e7170.c`](code/fcn.103e7170.c)
- [`code/fcn.103e75c0.c`](code/fcn.103e75c0.c)
- [`code/fcn.103e7870.c`](code/fcn.103e7870.c)
- [`code/fcn.103e7b80.c`](code/fcn.103e7b80.c)
- [`code/fcn.103e7cb0.c`](code/fcn.103e7cb0.c)
- [`code/fcn.103e7d00.c`](code/fcn.103e7d00.c)
- [`code/fcn.103f0da0.c`](code/fcn.103f0da0.c)
- [`code/fcn.10412110.c`](code/fcn.10412110.c)
- [`code/fcn.10480790.c`](code/fcn.10480790.c)
- [`code/fcn.104f2a00.c`](code/fcn.104f2a00.c)
- [`code/fcn.104f2a20.c`](code/fcn.104f2a20.c)
- [`code/fcn.104f8280.c`](code/fcn.104f8280.c)
- [`code/fcn.1052b7f0.c`](code/fcn.1052b7f0.c)
- [`code/fcn.10569470.c`](code/fcn.10569470.c)
- [`code/fcn.1057e990.c`](code/fcn.1057e990.c)
- [`code/fcn.106b5bd0.c`](code/fcn.106b5bd0.c)
- [`code/fcn.107a1310.c`](code/fcn.107a1310.c)
- [`code/method.WebCore__PlatformStrategies.virtual_12.c`](code/method.WebCore__PlatformStrategies.virtual_12.c)
- [`code/sym.wke.dll_wkeGetHostWindow.c`](code/sym.wke.dll_wkeGetHostWindow.c)
- [`code/sym.wke.dll_wkeGetRepaintInterval.c`](code/sym.wke.dll_wkeGetRepaintInterval.c)
- [`code/sym.wke.dll_wkeJSCollectGarbge.c`](code/sym.wke.dll_wkeJSCollectGarbge.c)
- [`code/sym.wke.dll_wkeSetFileSystem.c`](code/sym.wke.dll_wkeSetFileSystem.c)
- [`code/sym.wke.dll_wkeSleep.c`](code/sym.wke.dll_wkeSleep.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C code, here is an analysis of the sample:

### Core Functionality and Purpose
The code belongs to a **web rendering engine** component (likely a subset of WebKit or a similar browser engine framework). The naming conventions (e.g., `WebCore`, `wkeSetFileSystem`, `wkeJSCollectGarbge`, `wkeGetRepaintInterval`) strongly indicate that this binary is designed to provide the infrastructure for rendering web content, handling JavaScript, and managing graphical output.

The primary functions are dedicated to:
*   **Resource Management:** Managing memory, heap allocations, and internal data structures for the engine.
*   **Graphics Rendering:** Handling repaint intervals and utilizing GDI (via `SaveDC`) for drawing operations on the screen.
*   **JavaScript Execution Environment:** Specifically, it includes logic for "Garbage Collection" (`wkeJSCollectGarbge`), which is a standard part of JavaScript engines like V8 or JavaScriptCore.
*   **Hardware/Platform Abstraction:** The `PlatformStrategies` and `wkeSetFileSystem` functions suggest an abstraction layer to make the web engine portable across different operating systems.

### Suspicious or Malicious Behaviors
From the specific code snippets provided, there are **no overt malicious behaviors** such as process injection, registry persistence, or direct network communication. The logic is characteristic of a large, complex library rather than a standalone piece of malware. 

However, in a security context:
*   **Evasion through Legitimacy:** Malware authors often "wrap" legitimate components like web engines (e.g., Chromium/WebKit) to display sophisticated interactive content or to bypass security filters by rendering malicious instructions within a trusted process's graphics context.
*   **Complex State Management:** The use of heavy switch tables and complex pointer arithmetic (seen in `fcn.10569470` and `fcn.103bc0d0`) is standard for high-performance engines but can be used to obfuscate the execution flow from simple automated analysis tools.

### Notable Techniques or Patterns
*   **Modular Architecture:** The code uses a very structured approach, with internal functions being called to manage specific state transitions. This indicates it is likely part of a large DLL or framework.
*   **Jump Tables/Dispatchers:** `fcn.10569470` implements what appears to be a manual jump table for dispatching commands based on an index. This is common in C++ "virtual" functions and complex engine logic.
*   **Standard Library Wrapping:** Functions like `wkeSleep` act as wrappers for system calls, likely intended to keep the main thread responsive while performing internal tasks.
*   **GDI Usage:** The inclusion of `SaveDC` (from `gdi32.dll`) confirms that the code is responsible for rendering visual elements directly to a window or surface.

### Summary
The binary appears to be a **web browser engine component**. While the code itself does not exhibit malicious traits like "dropper" behavior or "backdoor" functionality, its presence in a suspicious file could indicate it is being used as a component to provide a sophisticated UI for a loader or to render web-based content within a potentially malicious application.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of a legitimate web rendering engine as a wrapper allows malicious functions to blend in with standard browser behaviors and bypass security filters. |
| T1027 | Obfuscated Files or Information | The implementation of complex jump tables and intricate pointer arithmetic is used to hide execution flow from automated analysis tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the assessment of Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided data consists primarily of internal code structures, jump tables, and components of a web rendering engine. The behavioral analysis explicitly states that no overt malicious behaviors (such as process injection, registry persistence, or direct network communication) were identified in the sample. 

Consequently, there are no actionable indicators for traditional security monitoring.

---

### **Indicators of Compromise**

**IP addresses / URLs / Domains**
*   None found.

**File paths / Registry keys**
*   None found. (The string `sfSWh\` is an internal identifier and does not constitute a file path).

**Mutex names / Named pipes**
*   None found.

**Hashes**
*   None found.

**Other artifacts**
*   **Internal Function Names:** `wkeSetFileSystem`, `wkeJSCollectGarbge`, `wkeGetRepaintInterval` (Note: These are standard library/engine functions and are not considered IOCs).
*   **API Calls:** `SaveDC` (Standard GDI function for graphics rendering).

---
**Analyst Note:** The sample appears to be a legitimate—albeit complex—library component for web rendering. While these components can occasionally be wrapped by malware to provide interactive UI or bypass filters, the binary itself does not contain indicators of malicious intent or command-and-control (C2) infrastructure.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Non-malicious (Library/Utility Component)
3. **Confidence**: High

4. **Key evidence**:
* **Lack of Malicious Functionality:** The analysis explicitly states that no overt malicious behaviors—such as process injection, registry persistence, or direct network communication (C2)—were identified in the code.
* **Standard Library Indicators:** The naming conventions (e.g., `WebCore`, `wkeSetFileSystem`, `wkeJSCollectGarbge`) are consistent with legitimate web rendering engines (like WebKit or Chromium) rather than signature-based malware families.
* **Absence of IOCs:** There were no suspicious IP addresses, URLs, file paths, or mutexes found; the only identified calls (e.g., `SaveDC`) are standard for graphical rendering and do not inherently indicate malicious intent.
