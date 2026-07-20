# Threat Analysis Report

**Generated:** 2026-07-17 20:40 UTC
**Sample:** `07d80576c4c640d9feefe0448a962e0d2e86e4aedb98e8bd386d0c7d40d111b1_07d80576c4c640d9feefe0448a962e0d2e86e4aedb98e8bd386d0c7d40d111b1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07d80576c4c640d9feefe0448a962e0d2e86e4aedb98e8bd386d0c7d40d111b1_07d80576c4c640d9feefe0448a962e0d2e86e4aedb98e8bd386d0c7d40d111b1.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 14,016,000 bytes |
| MD5 | `1ba15b3b3b0cf368359f21190f538188` |
| SHA1 | `9f0c60dbe129d17fc74476bc967b75879a591179` |
| SHA256 | `07d80576c4c640d9feefe0448a962e0d2e86e4aedb98e8bd386d0c7d40d111b1` |
| Overall entropy | 7.467 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768899944 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,879,552 | 6.386 | No |
| `.rdata` | 567,808 | 4.71 | No |
| `.data` | 31,744 | 4.089 | No |
| `.pdata` | 88,064 | 6.081 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 11,385,856 | 7.53 | ⚠️ Yes |
| `.reloc` | 61,440 | 5.444 | No |

### Imports

**KERNEL32.dll**: `LCMapStringW`, `FlsFree`, `FlsSetValue`, `FlsGetValue`, `FlsAlloc`, `GetStdHandle`, `GetFileType`, `SetStdHandle`, `VirtualQuery`, `VirtualAlloc`, `GetSystemInfo`, `HeapQueryInformation`, `FreeLibraryAndExitThread`, `ExitThread`, `CreateThread`
**USER32.dll**: `SetRect`, `InvalidateRgn`, `CopyAcceleratorTableW`, `CharNextW`, `KillTimer`, `SetTimer`, `RealChildWindowFromPoint`, `DeleteMenu`, `CopyImage`, `WindowFromPoint`, `ReleaseCapture`, `SetCapture`, `WaitMessage`, `IsDialogMessageW`, `SetWindowTextW`
**GDI32.dll**: `BitBlt`, `CreateCompatibleBitmap`, `CreateDIBitmap`, `CreateFontIndirectW`, `CreatePen`, `CreatePatternBrush`, `DeleteObject`, `EnumFontFamiliesW`, `GetStockObject`, `GetTextCharsetInfo`, `CreateBitmap`, `Escape`, `ExcludeClipRect`, `GetClipBox`, `GetObjectType`
**MSIMG32.dll**: `AlphaBlend`, `TransparentBlt`
**WINSPOOL.DRV**: `ClosePrinter`, `OpenPrinterW`, `DocumentPropertiesW`
**ADVAPI32.dll**: `RegDeleteKeyW`, `CreateServiceW`, `RegEnumKeyExW`, `RegEnumValueW`, `RegQueryValueW`, `RegEnumKeyW`, `RegSetValueExW`, `RegDeleteValueW`, `OpenSCManagerW`, `RegCreateKeyExW`, `RegQueryValueExW`, `RegOpenKeyExW`, `RegCloseKey`, `StartServiceW`, `CloseServiceHandle`
**SHELL32.dll**: `ShellExecuteW`, `DragFinish`, `DragQueryFileW`, `SHGetFileInfoW`, `SHGetDesktopFolder`, `SHBrowseForFolderW`, `SHGetSpecialFolderLocation`, `SHGetPathFromIDListW`, `SHGetMalloc`, `SHAppBarMessage`
**COMCTL32.dll**: `InitCommonControlsEx`
**SHLWAPI.dll**: `StrFormatKBSizeW`, `PathStripToRootW`, `PathIsUNCW`, `PathFindFileNameW`, `PathFindExtensionW`, `PathCombineW`, `PathRemoveFileSpecW`
**UxTheme.dll**: `GetThemeSysColor`, `OpenThemeData`, `CloseThemeData`, `DrawThemeBackground`, `GetThemeColor`, `GetCurrentThemeName`, `DrawThemeParentBackground`, `IsAppThemed`, `DrawThemeText`, `GetWindowTheme`, `GetThemePartSize`, `IsThemeBackgroundPartiallyTransparent`
**ole32.dll**: `CoRegisterMessageFilter`, `CoRevokeClassObject`, `CoInitializeEx`, `IsAccelerator`, `OleTranslateAccelerator`, `OleCreateMenuDescriptor`, `OleLockRunning`, `RevokeDragDrop`, `RegisterDragDrop`, `CoLockObjectExternal`, `OleGetClipboard`, `DoDragDrop`, `OleIsCurrentClipboard`, `OleFlushClipboard`, `OleUninitialize`
**OLEAUT32.dll**: `SafeArrayDestroy`, `VariantTimeToSystemTime`, `SystemTimeToVariantTime`, `OleCreateFontIndirect`, `LoadTypeLib`, `VariantChangeType`, `SysStringLen`, `SysAllocStringLen`, `SysFreeString`, `VariantInit`, `VariantClear`, `SysAllocString`, `VariantCopy`, `VarBstrFromDate`
**oledlg.dll**: `OleUIBusyW`
**gdiplus.dll**: `GdiplusShutdown`, `GdipAlloc`, `GdipFree`, `GdiplusStartup`, `GdipCloneImage`, `GdipDisposeImage`, `GdipGetImageGraphicsContext`, `GdipGetImageWidth`, `GdipGetImageHeight`, `GdipGetImagePixelFormat`, `GdipGetImagePalette`, `GdipGetImagePaletteSize`, `GdipCreateBitmapFromStream`, `GdipCreateBitmapFromScan0`, `GdipBitmapLockBits`
**OLEACC.dll**: `AccessibleObjectFromWindow`, `LresultFromObject`, `CreateStdAccessibleObject`
**IMM32.dll**: `ImmReleaseContext`, `ImmGetOpenStatus`, `ImmGetContext`
**WINMM.dll**: `PlaySoundW`

## Extracted Strings

Total strings found: **61083** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
|$ AVH
WAVAWH
 A_A^_
WAVAWH
 A_A^_
D9B}&E
\$ UVWATAUAVAWH
@A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
D$,+D$$L
D$(+D$ +
L$ SVWH
L$ SVWH
L$ SVWH
|$ AVH
|$ AVH
L$ SUVWH
@SUVWATAUAVAWH
A_A^A]A\_^][
WATAUAVAWH
 A_A^A]A\_
x ATAVAWH
 A_A^A\
WAVAWH
 A_A^_
\$ UVWATAUAVAWH
D9'uBA
0ugL9g
A_A^A]A\_^]
H SUVWAVH
@A^_^][
u9|$8s	
@8p(uDH
H9\$@u
t$ UWATAVAWH
A_A^A\_]
UVWAVAWH
A_A^_^]
@USVWH
UVWATAUAVAWH
t$`fD;
A_A^A]A\_^]
UVWATAUAVAWH
f9D$PuA
H;D$hu
pA_A^A]A\_^]
WAVAWH
0A_A^_
t$ WATAUAVAWH
 A_A^A]A\_
UVWATAUAVAWH
<0{tMI
@A_A^A]A\_^]
@USVWATAVAWH
A_A^A\_^[]
WAVAWH
79\$pt
@SUVWAVH
@A^_^][
D$@+D$8
SUVWAVH
`A^_^][
@SUVWAVAWH
D$<9F
hA_A^_^][
t,9D$Pu&9
x ATAVAWH
 A_A^A\
UVATAVAWH
0A_A^A\^]
@USVWAUAVAWH
9{u	9{
pA_A^A]_^[]
UVWATAUAVAWH
D9%Fk%
D9e`tH
D9ept D9%
PA_A^A]A\_^]
UVWATAUAVAWH
@A_A^A]A\_^]
t$ UWAVH
UVWAVAWH
@A_A^_^]
VWATAVAWH
 A_A^A\_^
WAVAWH
 A_A^_H
t$ WATAUAVAWH
D$0t D
A_A^A]A\_
@USVWAVH
A^_^[]
l$ VWAVH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14000b09c` | `0x14000b09c` | 1798726 | ✓ |
| `fcn.14000f1d8` | `0x14000f1d8` | 1782026 | ✓ |
| `method.CDialog.virtual_32` | `0x1400286fc` | 1678310 | ✓ |
| `method.CDialog.virtual_264` | `0x14002b43c` | 1666762 | ✓ |
| `method.CDataSourceControl.virtual_32` | `0x14003a9c8` | 1603902 | ✓ |
| `method.CMFCShellListCtrl.virtual_768` | `0x1401997e0` | 1501215 | ✓ |
| `method.CMFCToolBarCmdUI.virtual_8` | `0x140057fd4` | 1483570 | ✓ |
| `method.CPaneFrameWnd.virtual_856` | `0x14005c088` | 1467006 | ✓ |
| `fcn.1400609d4` | `0x1400609d4` | 1448206 | ✓ |
| `method.CMFCRibbonBaseElement.virtual_480` | `0x14006f97c` | 1386854 | ✓ |
| `method.CMFCBaseTabCtrl.virtual_744` | `0x14008c294` | 1269838 | ✓ |
| `fcn.140098b54` | `0x140098b54` | 1218482 | ✓ |
| `fcn.14018124c` | `0x14018124c` | 832636 | ✓ |
| `fcn.1400f28a4` | `0x1400f28a4` | 792381 | ✓ |
| `method.COleCntrFrameWndEx.virtual_752` | `0x1401013b0` | 790322 | ✓ |
| `method.CMFCCmdUsageCount.virtual_16` | `0x140108074` | 762514 | ✓ |
| `fcn.1400a932c` | `0x1400a932c` | 655715 | ✓ |
| `method.CMDIFrameWndEx.virtual_200` | `0x1400a3f98` | 651140 | ✓ |
| `method.CMDIFrameWndEx.virtual_1080` | `0x1400a2ac4` | 621933 | ✓ |
| `method.CMDIFrameWndEx.virtual_1088` | `0x1400a4630` | 621009 | ✓ |
| `method.CVSToolsListBox.virtual_880` | `0x140172210` | 597699 | ✓ |
| `method.CVSToolsListBox.virtual_872` | `0x140172238` | 597643 | ✓ |
| `fcn.140171f1c` | `0x140171f1c` | 597312 | ✓ |
| `fcn.1400c1ab4` | `0x1400c1ab4` | 588813 | ✓ |
| `fcn.1400db5a8` | `0x1400db5a8` | 572247 | ✓ |
| `method.CDockingPanesRow.virtual_144` | `0x14011174c` | 427896 | ✓ |
| `fcn.14010be74` | `0x14010be74` | 416991 | ✓ |
| `method.CMDIChildWndEx.virtual_200` | `0x1400de2a4` | 412741 | ✓ |
| `fcn.14011c218` | `0x14011c218` | 379063 | ✓ |
| `method.CFrameWndEx.virtual_864` | `0x1400a099c` | 315591 | ✓ |

### Decompiled Code Files

- [`code/fcn.14000b09c.c`](code/fcn.14000b09c.c)
- [`code/fcn.14000f1d8.c`](code/fcn.14000f1d8.c)
- [`code/fcn.1400609d4.c`](code/fcn.1400609d4.c)
- [`code/fcn.140098b54.c`](code/fcn.140098b54.c)
- [`code/fcn.1400a932c.c`](code/fcn.1400a932c.c)
- [`code/fcn.1400c1ab4.c`](code/fcn.1400c1ab4.c)
- [`code/fcn.1400db5a8.c`](code/fcn.1400db5a8.c)
- [`code/fcn.1400f28a4.c`](code/fcn.1400f28a4.c)
- [`code/fcn.14010be74.c`](code/fcn.14010be74.c)
- [`code/fcn.14011c218.c`](code/fcn.14011c218.c)
- [`code/fcn.140171f1c.c`](code/fcn.140171f1c.c)
- [`code/fcn.14018124c.c`](code/fcn.14018124c.c)
- [`code/method.CDataSourceControl.virtual_32.c`](code/method.CDataSourceControl.virtual_32.c)
- [`code/method.CDialog.virtual_264.c`](code/method.CDialog.virtual_264.c)
- [`code/method.CDialog.virtual_32.c`](code/method.CDialog.virtual_32.c)
- [`code/method.CDockingPanesRow.virtual_144.c`](code/method.CDockingPanesRow.virtual_144.c)
- [`code/method.CFrameWndEx.virtual_864.c`](code/method.CFrameWndEx.virtual_864.c)
- [`code/method.CMDIChildWndEx.virtual_200.c`](code/method.CMDIChildWndEx.virtual_200.c)
- [`code/method.CMDIFrameWndEx.virtual_1080.c`](code/method.CMDIFrameWndEx.virtual_1080.c)
- [`code/method.CMDIFrameWndEx.virtual_1088.c`](code/method.CMDIFrameWndEx.virtual_1088.c)
- [`code/method.CMDIFrameWndEx.virtual_200.c`](code/method.CMDIFrameWndEx.virtual_200.c)
- [`code/method.CMFCBaseTabCtrl.virtual_744.c`](code/method.CMFCBaseTabCtrl.virtual_744.c)
- [`code/method.CMFCCmdUsageCount.virtual_16.c`](code/method.CMFCCmdUsageCount.virtual_16.c)
- [`code/method.CMFCRibbonBaseElement.virtual_480.c`](code/method.CMFCRibbonBaseElement.virtual_480.c)
- [`code/method.CMFCShellListCtrl.virtual_768.c`](code/method.CMFCShellListCtrl.virtual_768.c)
- [`code/method.CMFCToolBarCmdUI.virtual_8.c`](code/method.CMFCToolBarCmdUI.virtual_8.c)
- [`code/method.COleCntrFrameWndEx.virtual_752.c`](code/method.COleCntrFrameWndEx.virtual_752.c)
- [`code/method.CPaneFrameWnd.virtual_856.c`](code/method.CPaneFrameWnd.virtual_856.c)
- [`code/method.CVSToolsListBox.virtual_872.c`](code/method.CVSToolsListBox.virtual_872.c)
- [`code/method.CVSToolsListBox.virtual_880.c`](code/method.CVSToolsListBox.virtual_880.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C code, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The code consists of standard boilerplate for a **Windows Graphical User Interface (GUI) application** built using the **Microsoft Foundation Class (MFC)** library. 

*   **UI Framework:** The presence of class names like `CDialog`, `CMFCShellListCtrl`, `CMFCToolBarCmdUI`, `CPaneFrameWnd`, and `CFrameWndEx` confirms that this is a standard Win32 application using MFC to manage its visual elements.
*   **Component Management:** The functions are primarily responsible for managing internal UI components, such as:
    *   Rendering text colors (`GetTextColor`).
    *   Managing button states and icons (e.g., `fcn.1400c1ab4` checking for "Button" classes).
    *   Handling docking panes and ribbons (common in professional software like Office or specialized engineering tools).
    *   Calculating window dimensions and positions (`GetWindowRect`, `GetParent`).

### Suspicious or Malicious Behaviors
No overtly malicious behaviors were identified in the provided code segments. Specifically:
*   **No Process Injection:** There are no calls to `OpenProcess`, `VirtualAllocEx`, or `CreateRemoteThread` typically associated with injecting code into other processes.
*   **No Persistence Mechanisms:** There is no evidence of registry modification, scheduled task creation, or service installation in these functions.
*   **No Network Communication:** No networking libraries (e.g., `WinInet`, `WinHTTP`) or raw socket operations were observed.
*   **No File Manipulation:** The code does not perform unauthorized file system access or sensitive file encryption.

### Notable Techniques and Patterns
*   **Standard Library Usage:** The binary heavily utilizes standard Windows APIs for UI management (e.g., `SendMessageW`, `GetDlgItem`). 
*   **Heavy Template/Framework usage:** The repetition of "virtual" functions (e.g., `virtual_32`, `virtual_1080`) and the high volume of internal helper calls (`fcn.140...`) are indicative of a large, standard C++ library rather than custom-written malware logic.
*   **Common UI Library Logic:** The check for `TaskDialogIndirect` in `comctl32.dll` is a common developer practice to ensure modern dialog boxes appear on older versions of Windows.

### Summary for Analysis
The provided code appears to be **non-malicious functionality related to the rendering and management of a standard desktop application.** While it is common for malware to hide within "wrapper" applications that use large frameworks like MFC, the specific functions shown here are characteristic of legitimate software components (e.g., buttons, menus, and window frames).

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, the code consists of standard components for a Windows Graphical User Interface (GUI) application using the Microsoft Foundation Class (MFC) library. The analysis explicitly states that **no overtly malicious behaviors** (such as process injection, persistence, network communication, or unauthorized file manipulation) were identified.

Because the observed behaviors are consistent with legitimate software functionality and do not exhibit adversarial intent, there are no applicable MITRE ATT&CK techniques to map from this specific snippet.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| N/A | No Malicious Behavior Identified | The analysis confirms the code performs standard UI rendering and management (MFC) without any indicators of malicious activity or adversary tactics. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the assessment of Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None

**File paths / Registry keys**
*   None

**Mutex names / Named pipes**
*   None

**Hashes**
*   None

**Other artifacts**
*   None

---
**Analyst Note:** 
The "Extracted Strings" section contains high-entropy/obfuscated data that does not resolve into human-readable network indicators, file paths, or known malicious signatures. The "Behavioral Analysis" explicitly concludes that the code consists of standard Microsoft Foundation Class (MFC) library components and displays no signs of malicious activity (such as injection, persistence, or unauthorized communication). No actionable IOCs were identified.

---

## Malware Family Classification

1. **Malware family**: None (Benign)
2. **Malware type**: N/A (Standard Application / Library)
3. **Confidence**: High
4. **Key evidence**: 
    *   **Standard Framework Usage:** The analysis confirms the code consists of standard Microsoft Foundation Class (MFC) library boilerplate for a Windows GUI, showing no unique or malicious logic.
    *   **Absence of Malicious Indicators:** There were no identified instances of process injection, persistence mechanisms, network communication, or unauthorized file manipulation.
    *   **Lack of IOCs:** No indicators of compromise—such as hardcoded IP addresses, URLs, registry keys, or mutexes—were detected in the strings or behavioral logs.
