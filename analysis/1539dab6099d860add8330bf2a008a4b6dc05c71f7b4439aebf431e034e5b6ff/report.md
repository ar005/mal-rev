# Threat Analysis Report

**Generated:** 2026-09-06 20:34 UTC
**Sample:** `1539dab6099d860add8330bf2a008a4b6dc05c71f7b4439aebf431e034e5b6ff_1539dab6099d860add8330bf2a008a4b6dc05c71f7b4439aebf431e034e5b6ff.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1539dab6099d860add8330bf2a008a4b6dc05c71f7b4439aebf431e034e5b6ff_1539dab6099d860add8330bf2a008a4b6dc05c71f7b4439aebf431e034e5b6ff.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 545,752 bytes |
| MD5 | `af470dc806e59bd1079151674ac1128f` |
| SHA1 | `54c72a92f6251fe44bc03f928c6d6e31cc1a646f` |
| SHA256 | `1539dab6099d860add8330bf2a008a4b6dc05c71f7b4439aebf431e034e5b6ff` |
| Overall entropy | 5.713 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1761846782 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 289,792 | 5.571 | No |
| `.rdata` | 164,864 | 4.257 | No |
| `.data` | 5,632 | 4.554 | No |
| `.pdata` | 27,648 | 5.453 | No |
| `.rsrc` | 45,056 | 4.356 | No |
| `.reloc` | 1,024 | 4.821 | No |

### Imports

**urlmon.dll**: `URLDownloadToFileW`
**KERNEL32.dll**: `K32GetProcessImageFileNameW`, `OpenProcess`, `CreateToolhelp32Snapshot`, `MultiByteToWideChar`, `GetTickCount64`, `Process32NextW`, `K32GetModuleBaseNameW`, `DeleteFileW`, `Process32FirstW`, `CloseHandle`, `K32EnumProcesses`, `GetWindowsDirectoryW`, `GetProcAddress`, `LocalFree`, `SystemTimeToFileTime`
**USER32.dll**: `SetForegroundWindow`, `TranslateMessage`, `DispatchMessageW`, `RegisterClassExW`, `SendMessageW`, `CreateWindowExW`, `DefWindowProcW`, `GetMessageW`, `FindWindowW`, `SendInput`, `GetCursorPos`, `SystemParametersInfoW`, `CharUpperBuffW`, `GetLastInputInfo`, `DestroyWindow`
**ADVAPI32.dll**: `CryptAcquireContextW`, `RegOpenKeyA`, `RegCreateKeyExW`, `SetNamedSecurityInfoW`, `GetNamedSecurityInfoW`, `CryptCreateHash`, `CryptHashData`, `RegSetValueExW`, `CryptDestroyHash`, `OpenProcessToken`, `RegOpenKeyExW`, `RegGetValueW`, `ConvertSidToStringSidW`, `RegDeleteValueW`, `CryptGetHashParam`
**SHELL32.dll**: `ShellExecuteW`, `SHChangeNotify`, `ShellExecuteExW`, `CommandLineToArgvW`
**ole32.dll**: `CoAllowSetForegroundWindow`, `CoInitializeEx`, `CLSIDFromString`, `CoRegisterClassObject`, `CoCreateFreeThreadedMarshaler`, `CoCreateInstance`
**OLEAUT32.dll**: `SysAllocString`, `SysFreeString`, `SetErrorInfo`, `GetErrorInfo`, `SysStringLen`
**MSVCP140.dll**: `_Xtime_get_ticks`, `?_Getcoll@_Locinfo@std@@QEBA?AU_Collvec@@XZ`, `??1_Locinfo@std@@QEAA@XZ`, `??0_Locinfo@std@@QEAA@PEBD@Z`, `??Bid@locale@std@@QEAA_KXZ`, `?_Throw_Cpp_error@std@@YAXH@Z`, `?_Xinvalid_argument@std@@YAXPEBD@Z`, `?_Xout_of_range@std@@YAXPEBD@Z`, `?_Xlength_error@std@@YAXPEBD@Z`, `_Cnd_do_broadcast_at_thread_exit`, `_Thrd_id`, `_Thrd_join`, `?_Xbad_function_call@std@@YAXXZ`, `_Wcscoll`, `??1_Lockit@std@@QEAA@XZ`
**VCRUNTIME140_1.dll**: `__CxxFrameHandler4`
**VCRUNTIME140.dll**: `_CxxThrowException`, `__current_exception_context`, `__current_exception`, `memset`, `memmove`, `strchr`, `wcsstr`, `_purecall`, `__std_exception_copy`, `__std_exception_destroy`, `__C_specific_handler`, `memcmp`, `memcpy`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_initterm`, `_initterm_e`, `_exit`, `_c_exit`, `_register_thread_local_exe_atexit_callback`, `_get_narrow_winmain_command_line`, `_set_app_type`, `exit`, `abort`, `_seh_filter_exe`, `_configure_narrow_argv`, `_cexit`, `_beginthreadex`, `_initialize_narrow_environment`, `_crt_atexit`
**api-ms-win-crt-convert-l1-1-0.dll**: `wcstol`, `_itow_s`, `wcstoul`
**api-ms-win-crt-string-l1-1-0.dll**: `iswspace`, `wcscat_s`, `_wcsicmp`, `wcsncpy_s`, `strncpy_s`, `_wcslwr_s`, `wcscpy_s`, `wcsncmp`
**api-ms-win-crt-heap-l1-1-0.dll**: `_set_new_mode`, `malloc`, `_callnewh`, `free`, `realloc`
**api-ms-win-crt-stdio-l1-1-0.dll**: `_set_fmode`, `__stdio_common_vswprintf_s`, `__stdio_common_vswprintf`, `__p__commode`
**api-ms-win-crt-time-l1-1-0.dll**: `_localtime64_s`, `_time64`
**api-ms-win-crt-math-l1-1-0.dll**: `ceilf`, `__setusermatherr`, `log2`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

## Extracted Strings

Total strings found: **923** (showing first 100)

```
!This program cannot be run in DOS mode.
$
pRich
`.rdata
@.data
.pdata
@.rsrc
@.reloc
D$xH9D$h
D$xH9D$hr

D$8H9D$(uH
H9D$(v"H
HcD$DA
H9D$xsLH
|$@
u2
D$HH9D$@t-H
D$8H9D$0t
H9D$Pu
H9D$Pw]H
H9D$pw
L$8H9H
H+D$PH;D$Hs
H+D$PH;D$Hs
H+D$HH;D$Ps
D$HH9D$PsMH
D$HH9D$`w
H9D$PvH
H9D$hv
H+D$8H;
D$8H9D$hsdH
D$0H9D$hsdH
D$`H9D$(v
H9D$Xv
D$`H9D$(v
H9D$Xv
D$0H9D$(u'H
D$ H9D$Hw
H9D$@v
D$@H9D$ u
H+D$8H;
D$PH9D$(w
HcD$0Hk
D$8H9D$0t$H
|$ ~
D$$HcD$$H
s!HcD$$H
9D$ sXHcD$ Hk
HcD$ Hk
H9D$Pu
9D$ uS3
D$(H9D$8u
D$ 9D$0u
D$(H9D$0u'H
HH;D$8v
H9D$8wH
H+D$HH;
H9D$Xs
H9D$Xs
D$8H9D$(uH
D$0H9D$(v
|HcD$ H;D$(v1H
?HcD$ H;D$(u)H

HcD$ H
D$hH9D$`
D$HH9D$@
|$ tx
@ H9D$Pu H
D$$9D$ sR
H+D$ H
H+D$ H
HcD$ H
D$0H9D$(
|$T
w"
D$H9D$ s)
HcD$THcL$TL
HcD$TH
HcD$ H
<$	wHHc
H9D$8w
H9D$Pu
H9D$(scH
D$hH9D$@
H9D$Pw]H
H+D$HH;D$Ps
H9D$0u
D$PH9D$Ht
D$PH9D$Ht
H+D$8H;
H+D$8H;
D$(H9D$8t
D$(H9D$ t
H9D$hv
H9D$@v
UUUUUUU
UUUUUUU
H9D$@v
HkD$@0H
D$0H9D$(t*H
(HkD$@0H
H9D$ u
H9D$ u
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14000a640` | `0x14000a640` | 13070 | ✓ |
| `fcn.140007a40` | `0x140007a40` | 4540 | ✓ |
| `fcn.140008c00` | `0x140008c00` | 4248 | ✓ |
| `method.winrt::impl::heap_implements_struct_callback_.virtual_8` | `0x14001bf30` | 3049 | ✓ |
| `fcn.140034870` | `0x140034870` | 2989 | ✓ |
| `method.callback_factory.1.virtual_8` | `0x14001bf20` | 2905 | ✓ |
| `method.winrt::implements_struct_callback__struct_INotificationActivationCallback_.virtual_8` | `0x14001bf10` | 2793 | ✓ |
| `fcn.140021900` | `0x140021900` | 2421 | ✓ |
| `fcn.140009cf0` | `0x140009cf0` | 2173 | ✓ |
| `fcn.14001f850` | `0x14001f850` | 2147 | ✓ |
| `fcn.14001f050` | `0x14001f050` | 2048 | ✓ |
| `fcn.14000e920` | `0x14000e920` | 1869 | ✓ |
| `fcn.140026640` | `0x140026640` | 1616 | ✓ |
| `fcn.140040bf0` | `0x140040bf0` | 1506 | ✓ |
| `fcn.1400271b0` | `0x1400271b0` | 1502 | ✓ |
| `fcn.140017150` | `0x140017150` | 1449 | ✓ |
| `fcn.14003ab00` | `0x14003ab00` | 1346 | ✓ |
| `fcn.1400145e0` | `0x1400145e0` | 1322 | ✓ |
| `fcn.140014b20` | `0x140014b20` | 1294 | ✓ |
| `fcn.1400319a0` | `0x1400319a0` | 1287 | ✓ |
| `fcn.140026140` | `0x140026140` | 1270 | ✓ |
| `fcn.140017e10` | `0x140017e10` | 1259 | ✓ |
| `fcn.140041090` | `0x140041090` | 1217 | ✓ |
| `fcn.140005d50` | `0x140005d50` | 1204 | ✓ |
| `fcn.140032300` | `0x140032300` | 1160 | ✓ |
| `fcn.1400208e0` | `0x1400208e0` | 1113 | ✓ |
| `fcn.140025ba0` | `0x140025ba0` | 1056 | ✓ |
| `fcn.1400214c0` | `0x1400214c0` | 1042 | ✓ |
| `fcn.14002fb70` | `0x14002fb70` | 1012 | ✓ |
| `fcn.14003fdf0` | `0x14003fdf0` | 1012 | ✓ |

### Decompiled Code Files

- [`code/fcn.140005d50.c`](code/fcn.140005d50.c)
- [`code/fcn.140007a40.c`](code/fcn.140007a40.c)
- [`code/fcn.140008c00.c`](code/fcn.140008c00.c)
- [`code/fcn.140009cf0.c`](code/fcn.140009cf0.c)
- [`code/fcn.14000a640.c`](code/fcn.14000a640.c)
- [`code/fcn.14000e920.c`](code/fcn.14000e920.c)
- [`code/fcn.1400145e0.c`](code/fcn.1400145e0.c)
- [`code/fcn.140014b20.c`](code/fcn.140014b20.c)
- [`code/fcn.140017150.c`](code/fcn.140017150.c)
- [`code/fcn.140017e10.c`](code/fcn.140017e10.c)
- [`code/fcn.14001f050.c`](code/fcn.14001f050.c)
- [`code/fcn.14001f850.c`](code/fcn.14001f850.c)
- [`code/fcn.1400208e0.c`](code/fcn.1400208e0.c)
- [`code/fcn.1400214c0.c`](code/fcn.1400214c0.c)
- [`code/fcn.140021900.c`](code/fcn.140021900.c)
- [`code/fcn.140025ba0.c`](code/fcn.140025ba0.c)
- [`code/fcn.140026140.c`](code/fcn.140026140.c)
- [`code/fcn.140026640.c`](code/fcn.140026640.c)
- [`code/fcn.1400271b0.c`](code/fcn.1400271b0.c)
- [`code/fcn.14002fb70.c`](code/fcn.14002fb70.c)
- [`code/fcn.1400319a0.c`](code/fcn.1400319a0.c)
- [`code/fcn.140032300.c`](code/fcn.140032300.c)
- [`code/fcn.140034870.c`](code/fcn.140034870.c)
- [`code/fcn.14003ab00.c`](code/fcn.14003ab00.c)
- [`code/fcn.14003fdf0.c`](code/fcn.14003fdf0.c)
- [`code/fcn.140040bf0.c`](code/fcn.140040bf0.c)
- [`code/fcn.140041090.c`](code/fcn.140041090.c)
- [`code/method.callback_factory.1.virtual_8.c`](code/method.callback_factory.1.virtual_8.c)
- [`code/method.winrt__impl__heap_implements_struct_callback_.virtual_8.c`](code/method.winrt__impl__heap_implements_struct_callback_.virtual_8.c)
- [`code/method.winrt__implements_struct_callback__struct_INotificationActivationCallback_.virtual_8.c`](code/method.winrt__implements_struct_callback__struct_INotificationActivationCallback_.virtual_8.c)

## Behavioral Analysis

This final analysis incorporates the third chunk of disassembly, completing the picture of this module's role within the application.

### Updated Analysis Overview
The addition of these functions solidifies the identity of this binary as a **Core System Integration and Compatibility Layer**. While earlier chunks established it as an orchestrator for UI notifications and external processes, this final chunk reveals the "why" behind those actions: the module is responsible for identifying specific file types (specifically related to PDF forms/metadata) and ensuring the Windows environment is correctly configured to handle them.

### New Functionality & Logic Flow
The new functions reveal three critical underlying systems:

**1. Registry Integration & Shell Notification (`fcn.140026140`):**
This function handles the "glue" between the software and the Windows OS. 
*   **Registry Manipulation:** It uses `RegOpenKeyExW`, `RegCreateKeyExW`, and `RegSetValueExW` to modify registry keys for "Progid" (Program ID) and "Hash." These are standard methods for registering how a system should handle specific file associations or shell protocols.
*   **System Refresh:** After modifying the registry, it calls `SHChangeNotify`. This tells Windows that a configuration change has occurred (like a new print driver or application protocol), forcing the OS to refresh its icons and associations.
*   **Triggering Logic:** Notably, if the registry update is successful, it then calls `fcn.140026640` (the "Drop and Execute" function from chunk 2). This links the registration process directly to the deployment of a helper tool or driver.

**2. Specialized File-Type Mapping (`fcn.140025ba0`):**
This is an extensive, hardcoded check for specialized extensions:
*   **Extensions detected:** `.pdfxml`, `.acrobatsecuritysettings`, `.fdf`, `.xfdf`, `.xdp`, `.pdx`, `.api`, `.secstore`, `.sequ`, `.rmf`, and `.bpdx`.
*   **Significance:** These are not standard office files; they are specific to **PDF Forms, XFA data, and Adobe-specific metadata**. This confirms that this module is specifically targeting the "Forms" or "Interactive PDF" features of the software.

**3. Command Dispatching (`fcn.1400208e0`):**
This function utilizes a switch table to handle over 13 different internal commands based on an ID. This suggests that even within the specific "Form/PDF" logic, there are many sub-states (e.g., different ways to fail gracefully, different types of help screens, or various intermediate installation steps).

---

### Updated Security Analysis

**1. System Configuration Persistence:**
The use of `RegCreateKeyExW` and `RegSetValueExW` confirms that this component is intended to leave a lasting footprint on the system's configuration. While common in legitimate software for installer routines, it requires monitoring because it modifies core OS behavior (how files are opened).

**2. "Drop-and-Execute" Pipeline:**
The full logic flow is now clear: 
1.  Detect a specific file type (e.g., `.fdf`) $\rightarrow$ 2. Check/Create corresponding Registry Keys $\rightarrow$ 3. Notify Windows of the change $\rightarrow$ 4. Drop and execute a helper process for final setup.
This "Chain" is a classic pattern in complex installer suites to move from a high-privilege or core-process context into a specific utility context (like a printer driver wrapper).

**3. Contextual Confirmation:**
The presence of `.fdf` and `.xfdf` files confirms this module is likely part of the **Adobe Acrobat "Forms" suite**. The logic ensures that when a user interacts with a form, the system correctly identifies the data format and triggers the necessary internal components or external plugins.

---

### Final Summary for Analyst

**Technical Role:** 
The code functions as a **System Integration Engine**. It is responsible for recognizing specific document formats (PDF Forms/XFA), registering those capabilities within the Windows Registry, and ensuring the OS recognizes these new "capabilities" via `SHChangeNotify`.

**Key Features identified across all chunks:**
*   **Context-Aware UI:** A complex state machine determines what to show the user based on their licensing and hardware (Chunk 1).
*   **Process Orchestration:** A "Drop-and-Execute" mechanism facilitates transitions between different helper tools or drivers (Chunk 2).
*   **Registry & Shell Integration:** Automated updates to Windows registry keys to ensure proper file associations (Chunk 3).
*   **Specialized Data Handling:** Specific logic for identifying and handling non-standard PDF metadata formats like `.fdf` and `.pdfxml`.

**Security Assessment:**
The module exhibits behavior typical of a high-end commercial installer (e.g., Adobe, Microsoft). While it uses "high-interest" techniques—such as dropping files into temp folders and modifying registry keys—these are wrapped in specific logic for a clearly defined purpose: **enabling functionality for specialized PDF form types.**

**Risk Profile:** 
Low-Medium (Context Dependent). The "Drop-and-Execute" behavior is technically similar to malware delivery, but the presence of specific branding and standard Windows registration patterns suggests a legitimate enterprise deployment tool.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547 | Boot or Logon Autostart Execution | The use of `RegCreateKeyExW` and `RegSetValueExW` to modify "Progid" and "Hash" values ensures that the system persists specific file associations and configurations across reboots. |
| T1059 | Command and Scripting Interpreter | The "Drop-and-Execute" pipeline is used to transition from a core process context to external helper tools or drivers, which typically involves executing commands to facilitate multi-step installation logic. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: While the behavior describes a "Drop-and-Execute" pattern often seen in malware, the technical context indicates these are likely components of an Adobe Acrobat installation suite.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **Registry Keys:** The report confirms the use of `RegOpenKeyExW`, `RegCreateKeyExW`, and `RegSetValueExW` to modify "Progid" (Program ID) and "Hash" values. (*Note: Specific registry paths were not provided in the source text.*)
*   **Targeted File Extensions:** The following extensions are specifically targeted/monitored by the logic:
    *   `.pdfxml`
    *   `.acrobatsecuritysettings`
    *   `.fdf`
    *   `.xfdf`
    *   `.xdp`
    *   `.pdx`
    *   `.api`
    *   `.secstore`
    *   `.sequ`
    *   `.rmf`
    *   `.bpdx`

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified. (The strings provided in the "Extracted Strings" section appear to be memory offsets or obfuscated data rather than standard MD5/SHA-1/SHA-256 hashes.)*

### **Other artifacts**
*   **WinAPI Functions:** 
    *   `RegOpenKeyExW`
    *   `RegCreateKeyExW`
    *   `RegSetValueExW`
    *   `SHChangeNotify` (Used to trigger OS shell refresh)
*   **Behavioral Patterns:**
    *   **Drop-and-Execute:** The module utilizes a "Drop and Execute" pipeline to transition from high-privilege installation contexts to specialized utility contexts.
    *   **Persistence Mechanism:** Manipulation of Registry keys for file association and persistence of system configurations.
    *   **Feature Detection:** A complex switch table (found in `fcn.1400208e0`) handling 13+ internal commands/states for error handling and installation steps.

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification:

1. **Malware family**: None (Benign / False Positive)
2. **Malware type**: Not applicable (Installer / System Integration Component)
3. **Confidence**: High
4. **Key evidence**: 
*   **Specific Domain Correlation:** The module specifically targets extensions like `.fdf`, `.xfdf`, and `.pdfxml`. These are non-standard but well-known file types specific to Adobe Acrobat’s "Forms" and "Interactive PDF" features.
*   **Contextual Justification of Techniques:** While the "Drop-and-Execute" pipeline and Registry modifications (`RegCreateKeyExW`) are common in malware, the analysis confirms these are used here for legitimate software installation routines (e.g., registering a new print driver or updating shell icons via `SHChangeNotify`).
*   **Complex State Machine:** The presence of over 13 different internal commands to handle errors and hardware/software compatibility is characteristic of high-end enterprise software rather than typical malware scripts.
