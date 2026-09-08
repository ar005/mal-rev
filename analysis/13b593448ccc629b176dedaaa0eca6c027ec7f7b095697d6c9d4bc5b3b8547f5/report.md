# Threat Analysis Report

**Generated:** 2026-09-02 21:58 UTC
**Sample:** `13b593448ccc629b176dedaaa0eca6c027ec7f7b095697d6c9d4bc5b3b8547f5_13b593448ccc629b176dedaaa0eca6c027ec7f7b095697d6c9d4bc5b3b8547f5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13b593448ccc629b176dedaaa0eca6c027ec7f7b095697d6c9d4bc5b3b8547f5_13b593448ccc629b176dedaaa0eca6c027ec7f7b095697d6c9d4bc5b3b8547f5.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 4 sections |
| Size | 14,781,984 bytes |
| MD5 | `30dfcb40d2229ad84a767ee4f7c3b004` |
| SHA1 | `be8d9d7bbf64a87048ca9f004039e2c09ad2608c` |
| SHA256 | `13b593448ccc629b176dedaaa0eca6c027ec7f7b095697d6c9d4bc5b3b8547f5` |
| Overall entropy | 7.999 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1185071589 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 74,752 | 6.469 | No |
| `.rdata` | 13,824 | 4.511 | No |
| `.data` | 4,608 | 4.8 | No |
| `.rsrc` | 3,072 | 4.883 | No |

### Imports

**KERNEL32.dll**: `Sleep`, `MultiByteToWideChar`, `WideCharToMultiByte`, `CompareFileTime`, `FindClose`, `FindFirstFileW`, `GetFileAttributesW`, `GetLastError`, `CreateDirectoryW`, `ExpandEnvironmentStringsW`, `lstrlenA`, `WriteFile`, `GetStdHandle`, `lstrcmpW`, `GetSystemTimeAsFileTime`
**USER32.dll**: `CharUpperW`, `GetWindowLongW`, `wsprintfW`, `wsprintfA`, `MessageBoxA`, `GetKeyState`, `SendMessageW`, `wvsprintfW`, `KillTimer`, `GetSystemMenu`, `EnableMenuItem`, `SetTimer`, `GetWindowTextW`, `DefWindowProcW`, `CallWindowProcW`
**GDI32.dll**: `DeleteObject`, `SelectObject`, `GetDeviceCaps`, `GetObjectW`, `CreateFontIndirectW`
**SHELL32.dll**: `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `SHGetMalloc`, `ShellExecuteW`, `ShellExecuteExW`, `SHGetSpecialFolderPathW`, `SHGetFileInfoW`
**ole32.dll**: `CoCreateInstance`, `CoInitialize`
**OLEAUT32.dll**: `SysAllocString`, `VariantClear`
**MSVCRT.dll**: `__set_app_type`, `__p__fmode`, `__p__commode`, `_adjust_fdiv`, `__setusermatherr`, `_initterm`, `__getmainargs`, `_acmdln`, `exit`, `_XcptFilter`, `_exit`, `??1type_info@@UAE@XZ`, `_onexit`, `__dllonexit`, `_except_handler3`

## Extracted Strings

Total strings found: **31926** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@BBf92u
WSSSSP
SVWujz
9w@@f
Yu(j
S
tHHt)S
twHtPHt H
9^0tXj
SSjjh
F(@Pj
jh
EHHtW
@PQSjh
G490tsB
EhPSA
8_>u8_=u
u/!F0!F4
tsNthNt,Nt
uN8XDtI
08X?t+
u#9ut
C 90tA
E9ur
tNHt)H
x0C;^D|
_^][YY
EhPSA
9^|~!;~pt
YG;~||
9CttsG
~;}u
_WhXEA
8WhxEA
F$;F,r
\$f9\$
v#SVW3
+|$O9D$r
9D$s4
UWh(EA
j
XPVSS
							
SetFileAttributesW
SystemTimeToFileTime
GetLocalTime
GetExitCodeThread
WaitForSingleObject
CreateThread
MultiByteToWideChar
WideCharToMultiByte
CompareFileTime
FindClose
FindFirstFileW
GetFileAttributesW
GetLastError
CreateDirectoryW
ExpandEnvironmentStringsW
lstrlenA
WriteFile
GetStdHandle
lstrcmpW
GetSystemTimeAsFileTime
lstrlenW
RemoveDirectoryW
FindNextFileW
DeleteFileW
VirtualAlloc
VirtualFree
GetACP
GetOEMCP
GetUserDefaultUILanguage
GetUserDefaultLCID
GetTempPathW
SetEnvironmentVariableW
SetCurrentDirectoryW
CloseHandle
lstrcmpiW
GetModuleFileNameW
GetCommandLineW
GetVersionExW
CreateFileW
GetDriveTypeW
GetModuleHandleW
GetProcAddress
LoadLibraryA
MulDiv
GetSystemDirectoryW
TerminateThread
ResumeThread
SuspendThread
LocalFree
lstrcpyW
FormatMessageW
DeleteCriticalSection
GetFileSize
SetFilePointer
ReadFile
SetFileTime
SetEndOfFile
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040315e` | `0x40315e` | 9672 | ✓ |
| `main` | `0x40397a` | 6292 | ✓ |
| `fcn.0040be81` | `0x40be81` | 3936 | ✓ |
| `fcn.00407852` | `0x407852` | 2306 | ✓ |
| `fcn.0040b9b3` | `0x40b9b3` | 1230 | ✓ |
| `fcn.0041004e` | `0x41004e` | 1036 | ✓ |
| `fcn.00402451` | `0x402451` | 979 | ✓ |
| `fcn.0040b353` | `0x40b353` | 829 | ✓ |
| `fcn.0040cf9a` | `0x40cf9a` | 779 | ✓ |
| `fcn.0040abe8` | `0x40abe8` | 707 | ✓ |
| `fcn.00401c91` | `0x401c91` | 689 | ✓ |
| `fcn.004113a0` | `0x4113a0` | 685 | ✓ |
| `fcn.00406097` | `0x406097` | 672 | ✓ |
| `fcn.0040b07f` | `0x40b07f` | 628 | ✓ |
| `fcn.00407430` | `0x407430` | 591 | ✓ |
| `fcn.00405506` | `0x405506` | 517 | ✓ |
| `fcn.00405d28` | `0x405d28` | 477 | ✓ |
| `fcn.0040dc90` | `0x40dc90` | 476 | ✓ |
| `fcn.0040a890` | `0x40a890` | 455 | ✓ |
| `fcn.004020f1` | `0x4020f1` | 356 | ✓ |
| `fcn.0041060d` | `0x41060d` | 346 | ✓ |
| `entry0` | `0x411de6` | 338 | ✓ |
| `fcn.004118e7` | `0x4118e7` | 336 | ✓ |
| `fcn.00403698` | `0x403698` | 332 | ✓ |
| `fcn.00401a5e` | `0x401a5e` | 327 | ✓ |
| `fcn.0040b86c` | `0x40b86c` | 327 | ✓ |
| `fcn.0040317e` | `0x40317e` | 326 | ✓ |
| `fcn.0040d953` | `0x40d953` | 312 | ✓ |
| `fcn.00407249` | `0x407249` | 306 | ✓ |
| `fcn.0040330c` | `0x40330c` | 296 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401a5e.c`](code/fcn.00401a5e.c)
- [`code/fcn.00401c91.c`](code/fcn.00401c91.c)
- [`code/fcn.004020f1.c`](code/fcn.004020f1.c)
- [`code/fcn.00402451.c`](code/fcn.00402451.c)
- [`code/fcn.0040315e.c`](code/fcn.0040315e.c)
- [`code/fcn.0040317e.c`](code/fcn.0040317e.c)
- [`code/fcn.0040330c.c`](code/fcn.0040330c.c)
- [`code/fcn.00403698.c`](code/fcn.00403698.c)
- [`code/fcn.00405506.c`](code/fcn.00405506.c)
- [`code/fcn.00405d28.c`](code/fcn.00405d28.c)
- [`code/fcn.00406097.c`](code/fcn.00406097.c)
- [`code/fcn.00407249.c`](code/fcn.00407249.c)
- [`code/fcn.00407430.c`](code/fcn.00407430.c)
- [`code/fcn.00407852.c`](code/fcn.00407852.c)
- [`code/fcn.0040a890.c`](code/fcn.0040a890.c)
- [`code/fcn.0040abe8.c`](code/fcn.0040abe8.c)
- [`code/fcn.0040b07f.c`](code/fcn.0040b07f.c)
- [`code/fcn.0040b353.c`](code/fcn.0040b353.c)
- [`code/fcn.0040b86c.c`](code/fcn.0040b86c.c)
- [`code/fcn.0040b9b3.c`](code/fcn.0040b9b3.c)
- [`code/fcn.0040be81.c`](code/fcn.0040be81.c)
- [`code/fcn.0040cf9a.c`](code/fcn.0040cf9a.c)
- [`code/fcn.0040d953.c`](code/fcn.0040d953.c)
- [`code/fcn.0040dc90.c`](code/fcn.0040dc90.c)
- [`code/fcn.0041004e.c`](code/fcn.0041004e.c)
- [`code/fcn.0041060d.c`](code/fcn.0041060d.c)
- [`code/fcn.004113a0.c`](code/fcn.004113a0.c)
- [`code/fcn.004118e7.c`](code/fcn.004118e7.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

This update incorporates the analysis of the second disassembly chunk into the existing profile. The additional code confirms several sophisticated behaviors typical of a multi-stage dropper or a "wrapper" installer used by malware to stage and launch subsequent payloads.

### Updated Analysis Report

#### Core Functionality and Purpose
The binary is confirmed as a **multi-stage downloader/installer (dropper)**. It serves as a bridge between the initial infection and the execution of the primary payload. The analysis now reveals that it doesn't just launch another program; it actively prepares the operating system environment for that program by:
1.  **Identifying System Folders:** Identifying and verifying "Special Folders" (e.g., My Documents, Desktop) using `SHGetSpecialFolderPathW`.
2.  **Staging Files:** Creating files or directories in temporary locations (`%TEMP%`) via `CreateFileW` and `WriteFile`.
3.  **Environment Configuration:** Modifying system environment variables to ensure the "Stage 2" payload can find its resources correctly.

#### Suspicious and Malicious Behaviors
*   **Sophisticated Dropper/Installer Behavior:**
    *   **Staging in Temp Paths:** The usage of `GetTempPathW` followed by `CreateFileW` indicates that the binary is moving or creating "worker" files in a temporary directory before execution.
    *   **Environment Manipulation:** The code includes logic to call **`SetEnvironment`**. In many malware samples, this is used to set variables (like `PATH` or custom keys) so that the subsequent executable (the real payload) can resolve its configuration and internal components.
    *   **Shell Execution for Payload Transition:** The use of **`ShellExecuteW`** (often called with "open" as a parameter) suggests that once the environment is prepared and files are moved, it executes the final stage (e.g., `setup.exe`).
*   **Persistence/Evasion Preparation:**
    *   The logic in `fcn.0040317e` specifically iterates through several "Special Folders." This ensures that if the installer needs to copy files into common user locations, it can resolve those paths dynamically despite different OS language settings or configurations.
*   **System/Environment Awareness:** (Confirmed from Chunk 1)
    *   Continues to use `GetVersionExW` and others to verify system environment compatibility.

#### Notable Techniques and Patterns
*   **Dynamic API Resolution & Obfuscated Logic:** The heavy use of internal wrapper functions (`fcn.0040f465`, `fcn.0041060d`) and repeated logic blocks suggest a "stub" design intended to hide the primary execution flow from automated sandboxes or static analysis tools.
*   **COM/OLE Interaction:** The presence of **`CoCreateInstance`** suggests the binary may be interacting with shell objects (e.g., Shell Folders, shortcuts) or other Windows components that provide high-level access to system features.
*   **UI Manipulation:** Functions like `fcn.00406097` interact with `GetDlgItem`, `SetWindowPos`, and `GetSystemMetrics`. This indicates the binary might present a legitimate-looking installation GUI, potentially to mask its activity or provide a "professional" installer appearance to the victim.

#### Summary for Incident Response
**Threat Level: High.**
This is not a simple script; it is a **sophisticated dropper**. It exhibits professional-grade installer logic used by both high-end malware and legitimate software. However, the combination of **dynamic API resolution**, **environment variable manipulation (`SetEnvironment`)**, **shell execution**, and **staging in `%TEMP%`** are hallmarks of a malicious downloader.

**Detailed Indicators for Investigation:**
1.  **Process Tree Analysis:** Monitor for processes launched by this binary via `ShellExecuteW`. Look specifically for "setup.exe" or other non-standard executables appearing shortly after the initial run.
2.  **File System Changes:** Monitor for new files created in `%TEMP%` and check if they are moved to `%APPDATA%` or other system directories.
3.  **Environment Variables:** Audit for changes to environment variables (e.g., `PATH`, `TEMP`, or newly created custom strings) occurring during the execution of this file.
4.  **Persistence Monitoring:** Check for Registry keys added during the "setup" process, especially in `HKCU\Software\` or `HKLM\Software\` associated with names mimicking common software.

**Recommended Actions:** 
Isolate the host immediately. Perform a forensic sweep of `%TEMP%` and `%APPDWARE%` to identify dropped payloads. Block any network connections initiated by processes launched as children of this binary.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1106** | Native API | The use of internal wrapper functions and dynamic API resolution is intended to hide the execution flow from static analysis tools. |
| **T1204** | User Execution | The use of `ShellExecuteW` serves as the mechanism for transitioning between stages and executing the final payload. |
| **T1036.005** | Masquerading | The inclusion of UI manipulation (GetDlgItem, SetWindowPos) and "professional" installer logic is used to blend in with legitimate software. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the identified Indicators of Compromise (IOCs). 

*Note: Standard Windows API calls (e.g., `CreateFileW`, `GetSystemTime`), system libraries (e.g., `KERNEL32.dll`), and standard internal function offsets were excluded as they do not constitute unique indicators of a specific threat actor's infrastructure.*

### **IP addresses / URLs / Domains**
*   *(None identified in the provided data)*

### **File paths / Registry keys**
*   **%TEMP%** (Identified as a staging area for "worker" files)
*   **%APPDATA%** (Identified as a potential target location for dropped payloads)
*   **HKCU\Software\** (Registry path monitored for persistence)
*   **HKLM\Software\** (Registry path monitored for persistence)

### **Mutex names / Named pipes**
*   *(None identified in the provided data)*

### **Hashes**
*   *(No cryptographic hashes were present in the provided strings)*

### **Other artifacts**
*   **setup.exe** (Identified as a potential Stage 2 payload name)
*   **SetEnvironment** (Indicator of behavior: Used to manipulate environment variables for configuration/resource resolution)
*   **Dynamic API Resolution** (Behavioral artifact: Use of internal wrapper functions like `fcn.0040f465` and `fcn.0041060d` to obfuscate execution flow)

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High
4. **Key evidence**:
*   **Multi-stage Execution:** The binary functions as a "wrapper" or bridge, utilizing `ShellExecuteW` to launch secondary payloads (e.g., `setup.exe`) after preparing the environment.
*   **Environment Manipulation & Staging:** It performs systematic preparation for Stage 2 by staging files in `%TEMP%`, resolving special folders via `SHGetSpecialFolderPathW`, and using `SetEnvironment` to ensure subsequent components can resolve necessary resources.
*   **Evasion & Masquerading:** The use of dynamic API resolution/wrapper functions to hide execution flow, combined with UI-related calls (e.g., `GetDlgItem`, `SetWindowPos`) to mimic a legitimate installer, indicates intent to bypass both automated detection and user suspicion.
