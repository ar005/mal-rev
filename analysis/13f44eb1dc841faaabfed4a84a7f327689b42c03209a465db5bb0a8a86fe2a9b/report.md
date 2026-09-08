# Threat Analysis Report

**Generated:** 2026-09-03 21:46 UTC
**Sample:** `13f44eb1dc841faaabfed4a84a7f327689b42c03209a465db5bb0a8a86fe2a9b_13f44eb1dc841faaabfed4a84a7f327689b42c03209a465db5bb0a8a86fe2a9b.dll`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13f44eb1dc841faaabfed4a84a7f327689b42c03209a465db5bb0a8a86fe2a9b_13f44eb1dc841faaabfed4a84a7f327689b42c03209a465db5bb0a8a86fe2a9b.dll` |
| File type | PE32 executable for MS Windows 6.00 (DLL), Intel i386, 6 sections |
| Size | 5,127,088 bytes |
| MD5 | `9b2513eccee4118c0da511d67ea9f533` |
| SHA1 | `da0d7c2eb65e796744458a9d5cbcb58e78fb1ff4` |
| SHA256 | `13f44eb1dc841faaabfed4a84a7f327689b42c03209a465db5bb0a8a86fe2a9b` |
| Overall entropy | 6.861 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1639022343 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 3,384,320 | 6.241 | No |
| `.data` | 56,320 | 4.167 | No |
| `.idata` | 21,504 | 5.784 | No |
| `.didat` | 1,024 | 3.635 | No |
| `.rsrc` | 1,415,168 | 7.55 | ⚠️ Yes |
| `.reloc` | 237,568 | 6.582 | No |

### Imports

**ADVAPI32.dll**: `RegCloseKey`, `RegCreateKeyExW`, `RegSetValueExW`, `RegOpenKeyExW`, `RegEnumValueW`, `RegQueryValueExW`, `RegDeleteKeyW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegEnumKeyW`, `RegQueryValueW`, `RegSetValueW`, `GetFileSecurityW`, `SetFileSecurityW`, `IsTextUnicode`
**KERNEL32.dll**: `IsDebuggerPresent`, `IsProcessorFeaturePresent`, `TerminateProcess`, `QueryPerformanceCounter`, `UnhandledExceptionFilter`, `ExpandEnvironmentStringsA`, `LoadLibraryExA`, `GetSystemTimeAsFileTime`, `InitializeSListHead`, `SetUnhandledExceptionFilter`, `LockResource`, `LoadResource`, `FindResourceW`, `GetLastError`, `InitializeCriticalSectionAndSpinCount`
**VCRUNTIME140.dll**: `__current_exception`, `__current_exception_context`, `_except_handler4_common`, `memcmp`, `wcsrchr`, `wcsstr`, `wcschr`, `_purecall`, `memmove`, `memset`, `memcpy`, `__std_terminate`, `__CxxFrameHandler3`, `__std_type_info_destroy_list`, `_CxxThrowException`
**api-ms-win-crt-runtime-l1-1-0.dll**: `__p___argc`, `_beginthreadex`, `_endthread`, `__p___wargv`, `_resetstkoflw`, `_errno`, `_initterm_e`, `_initterm`, `terminate`, `_cexit`, `_endthreadex`, `abort`, `_crt_atexit`, `_execute_onexit_table`, `_register_onexit_function`
**api-ms-win-crt-string-l1-1-0.dll**: `wcscspn`, `wcsspn`, `_strnicmp`, `_wcsupr_s`, `iswspace`, `wcscmp`, `wmemcpy_s`, `wcsnlen`, `toupper`, `wcscoll`, `_wcsicoll`, `wcsncmp`, `wcscpy_s`, `iswdigit`, `wcspbrk`
**api-ms-win-crt-stdio-l1-1-0.dll**: `fclose`, `ftell`, `__stdio_common_vsprintf`, `__stdio_common_vsprintf_s`, `__stdio_common_vswscanf`, `_get_osfhandle`, `_fileno`, `_open_osfhandle`, `fflush`, `__stdio_common_vswprintf_s`, `__stdio_common_vswprintf`, `fread`, `fseek`, `fgetws`, `fputws`
**api-ms-win-crt-utility-l1-1-0.dll**: `labs`, `abs`, `rand_s`, `ldiv`
**api-ms-win-crt-heap-l1-1-0.dll**: `realloc`, `_msize`, `_expand`, `_recalloc`, `malloc`, `free`, `calloc`
**api-ms-win-crt-convert-l1-1-0.dll**: `_itow_s`, `wcstod`, `wcstoul`, `_wtol`, `wcstol`, `_ltow_s`, `_ultow_s`, `_wtoi`
**api-ms-win-crt-math-l1-1-0.dll**: `ceil`, `exp`, `sqrt`, `atan2`, `cos`, `sin`, `floor`, `_fdopen`, `fabs`
**api-ms-win-crt-time-l1-1-0.dll**: `_localtime64_s`, `_mktime64`, `clock`, `_time64`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `_wfullpath`, `_wmakepath_s`, `_wsplitpath_s`
**api-ms-win-crt-multibyte-l1-1-0.dll**: `_mbscspn`, `_mbsicmp`, `_ismbcspace`, `_mbsstr`, `_mbsrchr`, `_mbscmp`, `_mbscoll`, `_mbschr`, `_mbspbrk`, `_mbsspn`, `_mbsinc`, `_mbsrev`, `_mbsicoll`, `_mbslwr_s`, `_mbsupr_s`
**USER32.dll**: `GetCapture`, `LoadAcceleratorsW`, `TranslateAcceleratorW`, `GetSystemMetrics`, `DestroyMenu`, `LoadMenuW`, `GetSubMenu`, `PostThreadMessageW`, `GetClassInfoW`, `DefWindowProcW`, `GetWindow`, `GetMenuItemCount`, `GetClientRect`, `IsIconic`, `GetForegroundWindow`
**GDI32.dll**: `DeleteMetaFile`, `CloseMetaFile`, `CreateMetaFileW`, `LPtoDP`, `GetCharWidthW`, `CreateFontW`, `StretchDIBits`, `RoundRect`, `CreateEllipticRgn`, `CreateHatchBrush`, `ExtTextOutW`, `Polyline`, `SetDIBColorTable`, `GetDIBits`, `SelectPalette`
**ole32.dll**: `OleRegGetMiscStatus`, `OleRegEnumVerbs`, `CoDisconnectObject`, `CoRegisterMessageFilter`, `CoTreatAsClass`, `SetConvertStg`, `WriteFmtUserTypeStg`, `OleDuplicateData`, `WriteClassStg`, `GetRunningObjectTable`, `OleTranslateAccelerator`, `IsAccelerator`, `OleUninitialize`, `CoFreeUnusedLibraries`, `PropVariantClear`
**OLEAUT32.dll**: `SysAllocStringLen`, `SysAllocString`, `SysStringLen`, `SysFreeString`, `VariantChangeType`, `VariantClear`, `VariantTimeToSystemTime`, `SystemTimeToVariantTime`, `VarParseNumFromStr`, `SafeArrayCreateVector`, `VarBstrFromDec`, `VarDecFromStr`, `VarDateFromStr`, `SafeArrayDestroyDescriptor`, `SafeArrayDestroyData`
**SHLWAPI.dll**: `StrFormatKBSizeW`, `PathFindExtensionW`, `PathFindFileNameW`, `PathRemoveExtensionW`, `PathRemoveFileSpecW`, `PathIsUNCW`, `PathStripToRootW`, `UrlUnescapeW`
**IMM32.dll**: `ImmGetOpenStatus`, `ImmReleaseContext`, `ImmGetContext`
**UxTheme.dll**: `DrawThemeParentBackground`, `GetWindowTheme`, `DrawThemeBackground`, `GetThemeColor`, `OpenThemeData`, `CloseThemeData`, `GetCurrentThemeName`, `GetThemeSysColor`, `DrawThemeText`, `IsThemeBackgroundPartiallyTransparent`, `GetThemePartSize`, `IsAppThemed`

### Exports

`ord_256`, `ord_257`, `ord_258`, `ord_259`, `ord_260`, `ord_261`, `ord_262`, `ord_263`, `ord_264`, `ord_265`, `ord_266`, `ord_267`, `ord_268`, `ord_269`, `ord_270`, `ord_271`, `ord_272`, `ord_273`, `ord_274`, `ord_275`, `ord_276`, `ord_277`, `ord_278`, `ord_279`, `ord_280`, `ord_281`, `ord_282`, `ord_283`, `ord_284`, `ord_285`, `ord_286`, `ord_287`, `ord_288`, `ord_289`, `ord_290`, `ord_291`, `ord_292`, `ord_293`, `ord_294`, `ord_295`, `ord_296`, `ord_297`, `ord_298`, `ord_299`, `ord_300`, `ord_301`, `ord_302`, `ord_303`, `ord_304`, `ord_305`

## Extracted Strings

Total strings found: **11784** (showing first 100)

```
!This program cannot be run in DOS mode.
$
VtRich
`.data
.idata
@.didat
@.reloc
D$+d$SVW
CMFCAutoHideBar
CMFCAutoHideButton
CPaneContainerManager
CPaneDivider
CMFCTabCtrl
tE;o$r
G_^][
l$ u
3
CDaoException
CDaoWorkspace
CDaoTableDef
CDaoQueryDef
CDaoRecordset
CDaoRecordView
CDBException
CDatabase
CRecordset
CLongBinary
CRecordView
COleDBRecordView
D$+d$SVW
D$+d$SVW
;0uc;H
D$+d$SVW
mfc140u.dll
CDaoDatabase
CAnimationBaseObject
CBaseKeyFrame
CBaseTransition
CMFCCaptionBar
CMFCDesktopAlertWnd
CDockSite
CMDIClientAreaWnd
CMFCPrintPreviewToolBar
CMFCPropertyGridToolTipCtrl
CMFCPropertySheetCategoryInfo
CMFCReBar
CD2DResource
CMFCRibbonBar
CMFCRibbonCustomizeCategory
CSettingsStore
CSmartDockingGroupGuidesManager
CSmartDockingStandaloneGuide
CMFCStatusBar
CMFCVisualManager
CDialog
CPropertySheet
CToolTipCtrl
CSplitterWnd
CImageList
CControlBar
CFrameWnd
CGdiObject
CDockablePane
CDockablePaneAdapter
CMFCDropDownToolBar
CMFCMenuBar
CMouseManager
CMFCOutlookBar
CMFCOutlookBarPane
CPaneDialog
CPaneFrameWnd
CMFCPopupMenuBar
CTabbedPane
CMFCTasksPaneToolBar
CMFCTasksPane
CMFCToolBar
CMFCToolBarButton
CUserTool
CByteArray
CDWordArray
CObArray
CStringArray
CWordArray
CDockState
CObList
CStringList
CMapStringToOb
CMapStringToString
CMapWordToOb
CDocItem
CObject
CMFCBaseToolBar
CBasePane
CMFCOutlookBarTabCtrl
CMFCBaseTabCtrl
CCmdTarget
CBaseTabbedPane
CMFCOutlookBarToolBar
G ;F t
ESVjd^
CFrameWndEx
COleCntrFrameWndEx
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.10005fc0` | `0x10005fc0` | 3109696 | ✓ |
| `sym.mfc140u.dll_Ordinal_8738` | `0x100010b0` | 723686 | ✓ |
| `sym.mfc140u.dll_Ordinal_4883` | `0x10005450` | 723260 | ✓ |
| `sym.mfc140u.dll_Ordinal_2537` | `0x100054c0` | 708330 | ✓ |
| `fcn.100053ae` | `0x100053ae` | 699298 | ✓ |
| `sym.mfc140u.dll_Ordinal_4890` | `0x100053e0` | 699252 | ✓ |
| `sym.mfc140u.dll_Ordinal_14588` | `0x10006160` | 697484 | ✓ |
| `sym.mfc140u.dll_Ordinal_2175` | `0x10005ee0` | 696415 | ✓ |
| `sym.mfc140u.dll_Ordinal_7756` | `0x10005400` | 695052 | ✓ |
| `sym.mfc140u.dll_Ordinal_5340` | `0x100052c0` | 636301 | ✓ |
| `sym.mfc140u.dll_Ordinal_5338` | `0x10005540` | 635676 | ✓ |
| `sym.mfc140u.dll_Ordinal_2411` | `0x10019580` | 616952 | ✓ |
| `sym.mfc140u.dll_Ordinal_3838` | `0x10029920` | 551769 | ✓ |
| `fcn.10004ef4` | `0x10004ef4` | 550011 | ✓ |
| `fcn.10004f70` | `0x10004f70` | 549893 | ✓ |
| `fcn.10001000` | `0x10001000` | 524836 | ✓ |
| `sym.mfc140u.dll_Ordinal_11936` | `0x1006e740` | 505202 | ✓ |
| `sym.mfc140u.dll_Ordinal_6973` | `0x100b2150` | 483329 | ✓ |
| `sym.mfc140u.dll_Ordinal_12182` | `0x1003bea0` | 482531 | ✓ |
| `sym.mfc140u.dll_Ordinal_12180` | `0x1003c010` | 482264 | ✓ |
| `sym.mfc140u.dll_Ordinal_14574` | `0x1003bd90` | 477479 | ✓ |
| `sym.mfc140u.dll_Ordinal_12220` | `0x1003bdd0` | 476860 | ✓ |
| `sym.mfc140u.dll_Ordinal_4661` | `0x1003be10` | 475060 | ✓ |
| `sym.mfc140u.dll_Ordinal_2336` | `0x1003bf10` | 473008 | ✓ |
| `sym.mfc140u.dll_Ordinal_2276` | `0x1003bfa0` | 472848 | ✓ |
| `sym.mfc140u.dll_Ordinal_9216` | `0x1003f8f0` | 467346 | ✓ |
| `sym.mfc140u.dll_Ordinal_9213` | `0x1003f740` | 465698 | ✓ |
| `sym.mfc140u.dll_Ordinal_1476` | `0x1003fad0` | 460779 | ✓ |
| `sym.mfc140u.dll_Ordinal_1002` | `0x1003fa00` | 459840 | ✓ |
| `sym.mfc140u.dll_Ordinal_8161` | `0x1003f5b0` | 457327 | ✓ |

### Decompiled Code Files

- [`code/fcn.10001000.c`](code/fcn.10001000.c)
- [`code/fcn.10004ef4.c`](code/fcn.10004ef4.c)
- [`code/fcn.10004f70.c`](code/fcn.10004f70.c)
- [`code/fcn.100053ae.c`](code/fcn.100053ae.c)
- [`code/fcn.10005fc0.c`](code/fcn.10005fc0.c)
- [`code/sym.mfc140u.dll_Ordinal_1002.c`](code/sym.mfc140u.dll_Ordinal_1002.c)
- [`code/sym.mfc140u.dll_Ordinal_11936.c`](code/sym.mfc140u.dll_Ordinal_11936.c)
- [`code/sym.mfc140u.dll_Ordinal_12180.c`](code/sym.mfc140u.dll_Ordinal_12180.c)
- [`code/sym.mfc140u.dll_Ordinal_12182.c`](code/sym.mfc140u.dll_Ordinal_12182.c)
- [`code/sym.mfc140u.dll_Ordinal_12220.c`](code/sym.mfc140u.dll_Ordinal_12220.c)
- [`code/sym.mfc140u.dll_Ordinal_14574.c`](code/sym.mfc140u.dll_Ordinal_14574.c)
- [`code/sym.mfc140u.dll_Ordinal_14588.c`](code/sym.mfc140u.dll_Ordinal_14588.c)
- [`code/sym.mfc140u.dll_Ordinal_1476.c`](code/sym.mfc140u.dll_Ordinal_1476.c)
- [`code/sym.mfc140u.dll_Ordinal_2175.c`](code/sym.mfc140u.dll_Ordinal_2175.c)
- [`code/sym.mfc140u.dll_Ordinal_2276.c`](code/sym.mfc140u.dll_Ordinal_2276.c)
- [`code/sym.mfc140u.dll_Ordinal_2336.c`](code/sym.mfc140u.dll_Ordinal_2336.c)
- [`code/sym.mfc140u.dll_Ordinal_2411.c`](code/sym.mfc140u.dll_Ordinal_2411.c)
- [`code/sym.mfc140u.dll_Ordinal_2537.c`](code/sym.mfc140u.dll_Ordinal_2537.c)
- [`code/sym.mfc140u.dll_Ordinal_3838.c`](code/sym.mfc140u.dll_Ordinal_3838.c)
- [`code/sym.mfc140u.dll_Ordinal_4661.c`](code/sym.mfc140u.dll_Ordinal_4661.c)
- [`code/sym.mfc140u.dll_Ordinal_4883.c`](code/sym.mfc140u.dll_Ordinal_4883.c)
- [`code/sym.mfc140u.dll_Ordinal_4890.c`](code/sym.mfc140u.dll_Ordinal_4890.c)
- [`code/sym.mfc140u.dll_Ordinal_5338.c`](code/sym.mfc140u.dll_Ordinal_5338.c)
- [`code/sym.mfc140u.dll_Ordinal_5340.c`](code/sym.mfc140u.dll_Ordinal_5340.c)
- [`code/sym.mfc140u.dll_Ordinal_6973.c`](code/sym.mfc140u.dll_Ordinal_6973.c)
- [`code/sym.mfc140u.dll_Ordinal_7756.c`](code/sym.mfc140u.dll_Ordinal_7756.c)
- [`code/sym.mfc140u.dll_Ordinal_8161.c`](code/sym.mfc140u.dll_Ordinal_8161.c)
- [`code/sym.mfc140u.dll_Ordinal_8738.c`](code/sym.mfc140u.dll_Ordinal_8738.c)
- [`code/sym.mfc140u.dll_Ordinal_9213.c`](code/sym.mfc140u.dll_Ordinal_9213.c)
- [`code/sym.mfc140u.dll_Ordinal_9216.c`](code/sym.mfc140u.dll_Ordinal_9216.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary sample:

### Core Functionality and Purpose
The code is primarily composed of standard **Microsoft Foundation Class (MFC)** library functions. The vast number of "Ordinals" (e.g., `sym.mfc140u.dll_Ordinal_...`) and the accompanying strings indicate that this is a large, standard Windows desktop application developed using Visual C++.

The code focuses on:
*   **GUI Management:** Handling windows, buttons, toolbars, and menu items (e.g., `CMFCToolBar`, `CFrameWnd`, `CDockSite`).
*   **Window Message Processing:** The functions frequently use `SendMessageW` and `GetWindowLongW` to manage the state of UI elements.
*   **Resource Management:** Handling internal application structures, viewer logic, and layout management (e.g., `CView`, `CPropertySheet`).

### Suspicious or Malicious Behaviors
From the provided disassembly segment alone, there are no overt signs of malicious intent such as network communication, file system manipulation, or process injection. However, from a malware analysis perspective, several points are worth noting:

*   **Abundant Bloat/Complexity:** The presence of so many MFC-related components is typical of large legitimate applications (like installers or suite tools), but in some cases, malicious actors use "Franken-bins" or wrap malicious payloads inside large portions of legitimate code to hide their logic among thousands of lines of standard library calls.
*   **Exception Handling (SEH) Construction:** The function `fcn.10005fc0` constructs a table involving error codes like `0xc0000409` (Integer Divide by Zero). While common in high-level C++ to handle crashes gracefully, these structures can be used as an **anti-debugging** technique; debuggers may behave differently when "trapping" specific hardware/software exceptions.
*   **Software Interrupts:** The use of `swi(0x29)` and `swi(3)` are standard ways for the C++ compiler to implement exception handling or `longjmp`. While technically a way to bypass some basic analysis, they are standard in the Microsoft Visual C++ runtime.

### Notable Techniques or Patterns
*   **MFC Framework Utilization:** The heavy reliance on `mfc140u.dll` suggests the developer wanted high-level abstraction for the UI, making it harder for an analyst to quickly find "malicious" code because it is buried inside standard library logic.
*   **Standard Windows API Interaction:** The use of `GetKeyState`, `GetWindowRect`, and `ScreenToClient` are standard for a GUI application but provide basic functionality that any script or tool could also use.
*   **Complexity as Obfuscation:** The sheer volume of code suggests a "busy" binary. If this sample contains significant malicious logic, it is likely hidden deep within the legitimate MFC wrapper or in a separate, less-analyzed module.

### Summary for Incident Response
The provided code shows **no immediate malicious actions**. It appears to be a standard Windows application using the Microsoft Foundation Class library. 

**Recommendation:** If this binary is suspected of being malicious (e.g., part of a dropper), the next step should be to identify where the "custom" logic resides, as it is likely not contained within these specific MFC-wrapper functions but rather in a separate module or a dynamically loaded DLL.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The analyst notes that the inclusion of extensive MFC library code can serve as a "smokescreen" to hide malicious logic within standard, legitimate functions. |
| T1036 | Masquerading | The mention of "Franken-bins" suggests using large amounts of legitimate code as a wrapper to disguise the true nature and intent of the payload. |
| T1056.001 | Keylogging | While standard for UI management, the inclusion of `GetKeyState` provides the capability to capture user input, which can be used for credential harvesting. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs). 

**Note:** As noted in the behavioral analysis, the sample appears to consist primarily of standard Microsoft Foundation Class (MFC) library code. Consequently, there are no high-confidence malicious IOCs (such as C2 infrastructure or unique malicious paths) present in the provided text.

### **IP addresses / URLs / Domains**
*   None

### **File paths / Registry keys**
*   None (Note: `Kernel32.dll` and `mfc140u.dll` were identified but are standard Windows system/library files and thus excluded as false positives.)

### **Mutex names / Named pipes**
*   None

### **Hashes**
*   None

### **Other artifacts**
*   **Software Interrupts:** `swi(0x29)`, `swi(3)` (Note: These are standard for C++ exception handling but were identified in the technical analysis).
*   **Exception Codes:** `0xc0000409` (Integer Divide by Zero).

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader (Potential)
3. **Confidence**: Low

4. **Key evidence**:
*   **Smokescreen/Franken-bin Tactics:** The heavy reliance on MFC (`mfc140u.dll`) and large amounts of standard Windows logic suggest a "smokescreen" strategy, where malicious code is buried within extensive legitimate library calls to evade automated analysis.
*   **Lack of Direct Malicious Behavior:** No clear indicators of malicious activity (such as C2 communication or file system manipulation) were found in this specific segment; the analyst notes that if it is part of a larger attack chain, the actual payload likely resides in an external module.
*   **Ambiguous Capabilities:** The presence of `GetKeyState` and complex exception handling (`swi` instructions) are dual-use features; while common in standard software, they provide capabilities for keylogging and anti-debugging respectively.
