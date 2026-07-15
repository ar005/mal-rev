# Threat Analysis Report

**Generated:** 2026-07-15 07:49 UTC
**Sample:** `069e573b201730c6f55860843cf175e9b6dd27dbf501946cb33a5a9b25fa630d_069e573b201730c6f55860843cf175e9b6dd27dbf501946cb33a5a9b25fa630d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `069e573b201730c6f55860843cf175e9b6dd27dbf501946cb33a5a9b25fa630d_069e573b201730c6f55860843cf175e9b6dd27dbf501946cb33a5a9b25fa630d.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 27,599,360 bytes |
| MD5 | `e5fc6c703a7da06b5a42f82691570b7e` |
| SHA1 | `5223e290daf9ce1d7d413536fc164711fff812b9` |
| SHA256 | `069e573b201730c6f55860843cf175e9b6dd27dbf501946cb33a5a9b25fa630d` |
| Overall entropy | 7.993 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1757808576 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 65,536 | 6.231 | No |
| `.rdata` | 43,008 | 4.827 | No |
| `.data` | 1,536 | 2.653 | No |
| `.pdata` | 2,560 | 4.784 | No |
| `.rsrc` | 27,485,184 | 7.994 | ⚠️ Yes |
| `.reloc` | 512 | 2.653 | No |

### Imports

**KERNEL32.dll**: `IsDebuggerPresent`, `IsProcessorFeaturePresent`, `TerminateProcess`, `QueryPerformanceCounter`, `UnhandledExceptionFilter`, `RtlVirtualUnwind`, `RtlLookupFunctionEntry`, `RtlCaptureContext`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetSystemTimeAsFileTime`, `InitializeSListHead`, `CloseHandle`, `GetLastError`, `GetCurrentProcess`
**USER32.dll**: `EndPaint`, `BeginPaint`, `GetMessageW`, `MessageBoxW`, `ExitWindowsEx`, `CallWindowProcW`, `SetWindowLongPtrW`, `SendMessageW`, `IsWindowEnabled`, `SetFocus`, `GetDlgItem`, `GetParent`, `GetWindowTextW`, `SetWindowTextW`, `SetTimer`
**GDI32.dll**: `CreateCompatibleDC`, `DeleteDC`, `TextOutW`, `GetTextExtentPoint32W`, `SelectObject`, `CreateFontW`, `SetTextColor`, `SetBkMode`, `DeleteObject`, `CreateCompatibleBitmap`, `CreateSolidBrush`
**COMDLG32.dll**: `GetOpenFileNameW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `OpenProcessToken`, `RegOpenKeyExW`, `RegGetValueW`, `LookupPrivilegeValueW`, `GetTokenInformation`, `RegCloseKey`, `RegCreateKeyExW`, `RegSetValueExW`
**SHELL32.dll**: `SHGetPathFromIDListW`, `SHGetSpecialFolderPathW`, `ShellExecuteW`, `ShellExecuteExW`, `SHBrowseForFolderW`
**ole32.dll**: `CreateStreamOnHGlobal`, `CoTaskMemFree`
**MSVCP140.dll**: `?setstate@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXH_N@Z`, `??0?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAA@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@_N@Z`, `?_Init@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXXZ`, `?sputn@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA_JPEB_W_J@Z`, `?sputc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAG_W@Z`, `??1?$basic_ios@_WU?$char_traits@_W@std@@@std@@UEAA@XZ`, `?showmanyc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAA_JXZ`, `?xsgetn@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAA_JPEA_W_J@Z`, `?xsputn@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAA_JPEB_W_J@Z`, `?good@ios_base@std@@QEBA_NXZ`, `?_Getcat@?$codecvt@_WDU_Mbstatet@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z`, `?unshift@?$codecvt@_WDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z`, `?out@?$codecvt@_WDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEB_W1AEAPEB_WPEAD3AEAPEAD@Z`, `?in@?$codecvt@_WDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEA_W3AEAPEA_W@Z`, `?always_noconv@codecvt_base@std@@QEBA_NXZ`
**gdiplus.dll**: `GdipGetImageHeight`, `GdipLoadImageFromFile`, `GdiplusShutdown`, `GdiplusStartup`, `GdipLoadImageFromStream`, `GdipDrawImageRect`, `GdipCloneImage`, `GdipAlloc`, `GdipDisposeImage`, `GdipSetSmoothingMode`, `GdipSetInterpolationMode`, `GdipFree`, `GdipCreateFromHDC`, `GdipDeleteGraphics`, `GdipGetImageWidth`
**MSIMG32.dll**: `AlphaBlend`
**VCRUNTIME140.dll**: `__current_exception`, `_CxxThrowException`, `__C_specific_handler`, `memset`, `memmove`, `__current_exception_context`, `wcsstr`, `memcpy`, `__std_exception_destroy`, `__std_exception_copy`, `__std_terminate`
**VCRUNTIME140_1.dll**: `__CxxFrameHandler4`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_invoke_watson`, `_initterm`, `_get_wide_winmain_command_line`, `terminate`, `_register_thread_local_exe_atexit_callback`, `exit`, `_configure_wide_argv`, `_exit`, `_set_app_type`, `_seh_filter_exe`, `_cexit`, `_initialize_wide_environment`, `_c_exit`, `_initterm_e`, `_initialize_onexit_table`
**api-ms-win-crt-string-l1-1-0.dll**: `iswspace`, `towlower`
**api-ms-win-crt-stdio-l1-1-0.dll**: `_fseeki64`, `fsetpos`, `ungetc`, `setvbuf`, `fgetpos`, `fwrite`, `fgetwc`, `fgetc`, `ungetwc`, `fputwc`, `_set_fmode`, `fclose`, `fflush`, `__p__commode`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `_unlock_file`, `_lock_file`
**api-ms-win-crt-heap-l1-1-0.dll**: `malloc`, `_set_new_mode`, `free`, `_callnewh`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

## Extracted Strings

Total strings found: **61895** (showing first 100)

```
!This program cannot be run in DOS mode.
$
%0u'aQ
tRichaQ
`.rdata
@.data
.pdata
@.rsrc
@.reloc
fB94Bu
@USVWATAUAVAWH
fD9,ru
A_A^A]A\_^[]
@SVAVAWH
8A_A^^[
8A_A^^[
UVWATAUAVAWH
0A_A^A]A\_^]
@SUVAWH
HA_^][
@USVWATAVAWH
fF9$Bu
fF9$Bu
A_A^A\_^[]
@SUVWH
@USVWATAUAVAWH
fB94Bu
A_A^A]A\_^[]
|$ AVH
fE94Pu
SVAUAWH
HA_A]^[
|$ UATAUAVAWH
fF9,@u
A_A^A]A\]
|$ UATAUAVAWH
A_A^A]A\]
UAVAWH
fF9<@u
@SUVWATAVH
A^A\_^][
USVWATAUAVAWH
fF9,Bu
A_A^A]A\_^[]
s WAVAWH
l$ VAVAWH
0A_A^^
@SUWAWH
HA__][
WATAVAWH
HA_A^A\_
l$ VWAVH
l$ VWAVH
p UWAVH
fF94@u
WAVAWH
0A_A^_
@USVWATAUAVAWH
fF9,Bu
%D9--E
fD9,Xu
1D8-]A
A_A^A]A\_^[]
@SUVWAVH
L90u$H
0A^_^][
H9D$Hf
WATAUAVAWH
0A_A^A]A\_
@SUVAVH
8A^^][
@SUVAWH
8A_^][
l$ VWATAVAWH
UUUUUUUUH
33333333H+
 A_A^A\_^
|$ UAVAWH
A_A^]H
@USVWATAVAWH
A_A^A\_^[]
fB94Bu
@USVWATAUAVAWH
fF94Bu
fF94Bu
fF94Bu
fD94ru
fF94Bu
fD94ru
A_A^A]A\_^[]
@USVWAVH
A^_^[]
UWATAVAWH
A_A^A\_]
@USVWATAUAVAWH
fB94Cu
fB94Bu
fB94Bu
fB94Bu
fB94Bu
fB94Bu
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.std::basic_ofstream_wchar_t__struct_std::char_traits_wchar_t__.virtual_0` | `0x140009a40` | 3980 | ✓ |
| `fcn.14000f85c` | `0x14000f85c` | 3018 | ✓ |
| `fcn.14000f5c0` | `0x14000f5c0` | 2395 | ✓ |
| `fcn.14000f540` | `0x14000f540` | 2053 | ✓ |
| `fcn.140004490` | `0x140004490` | 1775 | ✓ |
| `fcn.140006a40` | `0x140006a40` | 1048 | ✓ |
| `fcn.140004de0` | `0x140004de0` | 1040 | ✓ |
| `method.std::basic_filebuf_wchar_t__struct_std::char_traits_wchar_t__.virtual_56` | `0x140008420` | 741 | ✓ |
| `fcn.140006190` | `0x140006190` | 730 | ✓ |
| `fcn.1400051f0` | `0x1400051f0` | 699 | ✓ |
| `fcn.140006e60` | `0x140006e60` | 690 | ✓ |
| `fcn.14000c370` | `0x14000c370` | 686 | ✓ |
| `fcn.14000f890` | `0x14000f890` | 661 | ✓ |
| `fcn.140009a50` | `0x140009a50` | 621 | ✓ |
| `fcn.140004220` | `0x140004220` | 620 | ✓ |
| `fcn.1400024d0` | `0x1400024d0` | 618 | ✓ |
| `fcn.14000bfa0` | `0x14000bfa0` | 580 | ✓ |
| `fcn.140001080` | `0x140001080` | 542 | ✓ |
| `fcn.14000ef20` | `0x14000ef20` | 530 | ✓ |
| `fcn.140001460` | `0x140001460` | 509 | ✓ |
| `fcn.14000a760` | `0x14000a760` | 509 | ✓ |
| `fcn.140008b90` | `0x140008b90` | 484 | ✓ |
| `fcn.14000a590` | `0x14000a590` | 461 | ✓ |
| `fcn.140003b30` | `0x140003b30` | 456 | ✓ |
| `fcn.140005fd0` | `0x140005fd0` | 448 | ✓ |
| `fcn.140006470` | `0x140006470` | 445 | ✓ |
| `fcn.140003ea0` | `0x140003ea0` | 432 | ✓ |
| `fcn.14000e6a0` | `0x14000e6a0` | 420 | ✓ |
| `fcn.140003d00` | `0x140003d00` | 412 | ✓ |
| `fcn.140008f00` | `0x140008f00` | 410 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001080.c`](code/fcn.140001080.c)
- [`code/fcn.140001460.c`](code/fcn.140001460.c)
- [`code/fcn.1400024d0.c`](code/fcn.1400024d0.c)
- [`code/fcn.140003b30.c`](code/fcn.140003b30.c)
- [`code/fcn.140003d00.c`](code/fcn.140003d00.c)
- [`code/fcn.140003ea0.c`](code/fcn.140003ea0.c)
- [`code/fcn.140004220.c`](code/fcn.140004220.c)
- [`code/fcn.140004490.c`](code/fcn.140004490.c)
- [`code/fcn.140004de0.c`](code/fcn.140004de0.c)
- [`code/fcn.1400051f0.c`](code/fcn.1400051f0.c)
- [`code/fcn.140005fd0.c`](code/fcn.140005fd0.c)
- [`code/fcn.140006190.c`](code/fcn.140006190.c)
- [`code/fcn.140006470.c`](code/fcn.140006470.c)
- [`code/fcn.140006a40.c`](code/fcn.140006a40.c)
- [`code/fcn.140006e60.c`](code/fcn.140006e60.c)
- [`code/fcn.140008b90.c`](code/fcn.140008b90.c)
- [`code/fcn.140008f00.c`](code/fcn.140008f00.c)
- [`code/fcn.140009a50.c`](code/fcn.140009a50.c)
- [`code/fcn.14000a590.c`](code/fcn.14000a590.c)
- [`code/fcn.14000a760.c`](code/fcn.14000a760.c)
- [`code/fcn.14000bfa0.c`](code/fcn.14000bfa0.c)
- [`code/fcn.14000c370.c`](code/fcn.14000c370.c)
- [`code/fcn.14000e6a0.c`](code/fcn.14000e6a0.c)
- [`code/fcn.14000ef20.c`](code/fcn.14000ef20.c)
- [`code/fcn.14000f540.c`](code/fcn.14000f540.c)
- [`code/fcn.14000f5c0.c`](code/fcn.14000f5c0.c)
- [`code/fcn.14000f85c.c`](code/fcn.14000f85c.c)
- [`code/fcn.14000f890.c`](code/fcn.14000f890.c)
- [`code/method.std__basic_filebuf_wchar_t__struct_std__char_traits_wchar_t__.virtual_56.c`](code/method.std__basic_filebuf_wchar_t__struct_std__char_traits_wchar_t__.virtual_56.c)
- [`code/method.std__basic_ofstream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c`](code/method.std__basic_ofstream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The binary appears to be a **Screen Locker** or a form of **Targeted Extortionware**. The presence of the title `"Anna Martina Lock"` (found in `fcn.140001080`) combined with localizable strings ("More info" / "Mehr anzeigen") suggests it is designed to present a full-screen interface to a user, likely demanding some form of action or payment.

### Suspicious and Malicious Behaviors
*   **System Restriction (Anti-Analysis/Anti-Intervention):** 
    *   The function `fcn.14000c370` specifically queries the Registry for `DisableTaskMgr` and `DisableRegistryTools`. This is a common technique in "locker" malware to ensure that the user cannot easily kill the malicious process using Task Manager or bypass its restrictions via the Registry Editor.
*   **Targeted Data Harvesting:** 
    *   The function `fcn.140006e60` creates/references a specific file: `\anna_martina_passwort.txt`. The construction of this filename suggests that the malware targets a specific individual or group ("Anna Martina") and likely saves inputted credentials or "unlock" codes into this text file.
*   **Multimedia Resource Gathering:** 
    *   The function `fcn.140004490` performs a recursive search for common image formats (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`). This is likely used to populate the "Lock" screen with visual content, such as wallpaper or branding, to make the locker more visually convincing or intimidating.
*   **User Interface Manipulation:** 
    *   The code uses GDI+ (`fcn.1400051f0`) and standard Windows GDI calls to render text and images. It creates a window with specific dimensions and draws "Welcome" or status messages, indicating a polished GUI intended to interact directly with the victim.

### Notable Techniques and Patterns
*   **Localization:** The inclusion of both English ("Show more") and German ("Mehr anzeigen") strings indicates that the threat actor is targeting multiple regions or using a pre-built "locker" framework.
*   **Environment Hardening:** By checking for `DisableTaskMgr` before proceeding, the malware confirms whether it can successfully restrict the user's ability to intervene in its operation.
*   **Standard API Abuse:** The code utilizes standard Windows APIs (`GetModuleHandleW`, `FindFirstFileW`, `ShellExecute`, and Registry keys) which allows it to blend in with legitimate system activity while performing malicious tasks like restricting system tools.

### Summary of Indicators
*   **Malicious Intent:** High (Screen locker/Extortion).
*   **Targeting:** Specific (References to "Anna Martina").
*   **Defense Evasion:** Yes (Checks for Task Manager/Registry Tool availability).
*   **Data Collection:** Potential credential theft via the `passwort.txt` file creation logic.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1562.001** | Impair Defenses: Disable or Modify Tools | The binary specifically queries registry keys to disable Task Manager and Registry Editor to prevent user intervention and process termination. |
| **T1083** | File and Directory Discovery | The malware performs a recursive search for various image formats (`.jpg`, `.png`, etc.) to gather assets for its display interface. |
| **T1005** | Data from Local System | The creation of the `anna_martina_passwort.txt` file indicates a mechanism for capturing and storing credentials or "unlock" codes on the local system. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   **Registry Keys:** 
    *   `DisableTaskMgr` (Used to disable Task Manager)
    *   `DisableRegistryTools` (Used to block access to Registry Editor)
*   **File Paths/Names:**
    *   `\anna_martina_passwort.txt` (Potential credential/password storage file)
*   **Development Artifacts:**
    *   `C:\Users\samso\source\repos\anna martina lock new\x64\Release\anna martina lock new.pdb` (Note: This is a local development path, but confirms the malware's internal naming convention).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None provided in the source material.*

**Other artifacts**
*   **Malware Identifier/Title:** "Anna Martina Lock" (Identified as a screen locker/extortion tool).
*   **File Search Patterns:** The malware performs recursive searches for the following image extensions to populate its UI: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`.
*   **Localization Strings:** Includes both English ("Show more") and German ("Mehr anzeigen") support.

---
**Analyst Note:** 
The presence of specific registry keys (`DisableTaskMgr`) combined with a hardcoded filename (`anna_martina_passwort.txt`) indicates a targeted "Locker" style malware campaign designed to restrict user interaction with the OS while localizing data or passwords for its operators.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://ns.adobe.com/exif/1.0/`
- `http://ns.adobe.com/photoshop/1.0/`
- `http://ns.adobe.com/tiff/1.0/`
- `http://ns.adobe.com/xap/1.0/`
- `http://ns.adobe.com/xap/1.0/mm/`
- `http://ns.adobe.com/xap/1.0/sType/ResourceEvent#`
- `http://ns.adobe.com/xap/1.0/sType/ResourceRef#`
- `http://purl.org/dc/elements/1.1/`
- `http://www.w3.org/1999/02/22-rdf-syntax-ns#`

---

## Malware Family Classification

1. **Malware family**: Custom (Targeted Extortion)
2. **Malware type**: Locker (Screen Locker)
3. **Confidence**: High
4. **Key evidence**: 
    *   **Anti-Intervention Tactics:** The binary specifically checks for and attempts to disable system tools (`DisableTaskMgr` and `DisableRegistryTools`), a hallmark of "Locker" malware designed to prevent the user from terminating the malicious process or bypassing restrictions.
    *   **Targeted Extortion Branding:** The consistent use of the name "Anna Martina Lock" across the UI, file creation logic, and development artifacts suggests a targeted campaign rather than a generic commodity strain.
    *   **Interactive Extortion Interface:** The use of GDI+ to render images and text, combined with localized strings ("Show more"/"Mehr anzeigen"), indicates a polished UI designed to present a lockout screen or demand for payment/action to the victim.
