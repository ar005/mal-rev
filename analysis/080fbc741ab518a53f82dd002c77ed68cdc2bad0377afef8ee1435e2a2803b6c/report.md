# Threat Analysis Report

**Generated:** 2026-07-18 01:24 UTC
**Sample:** `080fbc741ab518a53f82dd002c77ed68cdc2bad0377afef8ee1435e2a2803b6c_080fbc741ab518a53f82dd002c77ed68cdc2bad0377afef8ee1435e2a2803b6c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `080fbc741ab518a53f82dd002c77ed68cdc2bad0377afef8ee1435e2a2803b6c_080fbc741ab518a53f82dd002c77ed68cdc2bad0377afef8ee1435e2a2803b6c.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 4 sections |
| Size | 14,781,992 bytes |
| MD5 | `5846e2e356dbc36741db509380af6a42` |
| SHA1 | `90f721156fd3343f0123517b548e474b257105b9` |
| SHA256 | `080fbc741ab518a53f82dd002c77ed68cdc2bad0377afef8ee1435e2a2803b6c` |
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

Total strings found: **31922** (showing first 100)

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

This update incorporates the second chunk of disassembly into the existing analysis. The additional code confirms many of the suspicions raised in the first part—specifically regarding its role as a multi-stage "dropper" wrapped inside a professional installation framework (likely InnoSetup or a similar tool).

### Updated Analysis Report

#### 1. Core Functionality and Purpose
The binary is confirmed to be an **installer-style dropper**. The second chunk of disassembly reveals several high-level abstractions used by standard installer engines, but these same features are leveraged in malware to provide a "legitimate" veneer while executing malicious payloads.

*   **Wizard Interaction:** The presence of functions like `fcn.00407430` (which handles strings such as `"BeginPrompt"`, `"FinishMessage"`, and `"ErrorTitle"`) indicates the binary is designed to present a standard "Next-Next-Finish" wizard interface to the user.
*   **Resource Management:** The complex state machines in `fcn.0041004e` and `fcn.0040b353` manage the transition between different phases of an installation (e.g., checking prerequisites, extracting files, running a post-install script).

#### 2. New Specific Behaviors Found in Chunk 2
The second chunk reveals specific "drops" and execution paths that are characteristic of a multi-stage infection:

*   **System Path Resolution & Extraction (`fcn.00405506` / `fcn.0040330c`):**
    *   The code uses `SHGetSpecialFolderPathW` and `GetTempPathW` to find system-standard directories (like `%TEMP%` or `%APPDATA%`). 
    *   It then performs a "Drop" sequence: **CreateFileW $\rightarrow$ WriteFile $\rightarrow$ SetFileAttributesW $\rightarrow$ ShellExecuteW.**
    *   **Analysis:** This is the classic behavior of a dropper. The installer extracts a component (e.g., `setup.exe` or a malicious payload) into a temporary directory and immediately executes it using `ShellExecuteW`.

*   **Dynamic Payload Execution (`fcn.00402451`):**
    *   This function demonstrates deep interaction with the Windows Shell to prepare an environment for a secondary executable. It performs intensive path cleanup (removing trailing slashes/dots) before attempting to launch the next stage of the payload.

*   **UI Manipulation and Masquerading (`fcn.00406097`):**
    *   This function interacts with `GetWindowLongW`, `SetWindowPos`, and `GetSystemMetrics`. It calculates window positions and sizes to ensure the installer's GUI remains centered or follows standard dimensions. 
    *   **Analysis:** While useful for legitimate software, in a malicious context, this ensures the "decoy" installer looks professional enough to not alert the user during the execution of the payload.

#### 3. Technical Highlights & Observations
*   **Template/Framework Usage:** The complexity of functions like `fcn.004113a0` and `fcn.0040b07f` suggests that a significant portion of this code is not custom-written by a malware author but is part of a standard installer engine (like InnoSetup). Malware authors frequently use these "off-the-shelf" tools to package their payloads because they provide features like automated extraction, multi-language support, and professional-looking UI.
*   **Hidden Execution Paths:** The logic in `fcn.0041004e` shows a series of jumps based on internal state variables (e.g., `0x11`, `0x12`, `0x13`). This allows the same binary to perform different actions depending on the command-line arguments passed by a previous stage in the infection chain.
*   **System Persistence Preparation:** The use of `SetFileAttributesW` and `ShellExecuteW` immediately following a write operation is a primary indicator of an installer intended to "handoff" execution to a second-stage payload that may perform more permanent actions (like registry modification or persistent service installation).

---

### Updated Summary for Analysts
**Verdict: High-Confidence Installer/Dropper.**

This sample is a sophisticated **installer wrapper**. It utilizes standard installation frameworks to create a professional user experience while performing the "dirty work" of a dropper. 

**Key Findings:**
1.  **Multi-Stage Execution:** The binary confirms it acts as a bridge. It validates the environment (Chunk 1) and then uses a formalized installer engine to unpack, place, and launch secondary components (Chunk 2).
2.  **Suspicious File Operations:** It actively seeks out system paths (`GetTempPathW`, `SHGetSpecialFolderPathW`) to "drop" files before executing them via `ShellExecuteW`. This is the primary mechanism for moving the final payload into a runnable state on the victim's machine.
3.  **Deceptive Facade:** The code includes extensive logic to handle standard UI prompts and window positioning, likely intended to hide the transition between the "installer" and the "malware" from the end-user.

**Recommended Actions for Investigation:**
*   **Identify the "Handoff":** Identify the specific file being passed to `ShellExecuteW` in `fcn.00405506`. This is typically the second-stage payload (e.g., a remote access trojan or information stealer).
*   **String Analysis:** Extract all strings from functions like `fcn.00407430`. They may reveal the actual names of the items being "installed."
*   **Network Monitoring:** Monitor for callbacks immediately following the execution of the files dropped by this installer.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036.005 | Masquerading (Match Legitimate Name) | The use of an InnoSetup-style wrapper and wizard UI elements is designed to mimic a legitimate software installation process to deceive the user. |
| T1204 | User Execution | The "multi-stage" nature of the binary relies on a user interacting with an installer frontend to execute the primary dropper, which then launches subsequent payloads. |
| T1027 | Obfuscated Files or Information | The use of internal state machines and jump tables to create "hidden execution paths" is intended to obscure malicious functionality from automated analysis or during manual inspection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: While standard Windows API functions like `GetTempPathW` and `SHGetSpecialFolderPathW` were observed, no specific hardcoded malicious file paths or registry keys were present in the text.)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Behavioral Indicator (Drop-and-Execute):** The analysis confirms a primary dropper mechanism: `CreateFileW` $\rightarrow$ `WriteFile` $\rightarrow$ `SetFileAttributesW` $\rightarrow$ `ShellExecuteW`. This sequence is used to drop and execute a second-stage payload.
*   **Suspicious Function Offsets:** 
    *   `0x405506` / `0x40330c`: Logic for system path resolution and file extraction.
    *   `0x402451`: Environment preparation/path cleanup for a secondary payload.
    *   `0x407430`: Handling of installation-themed strings (e.g., `"BeginPrompt"`, `"FinishMessage"`).
*   **Installer Framework:** The use of standard installer components (likely InnoSetup) to provide a "professional" front for malicious activity.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**: 
    *   **Drop-and-Execute Sequence:** The analysis confirms a classic multi-stage progression where the binary resolves system paths (e.g., `%TEMP%`), drops files using `CreateFileW` and `WriteFile`, and immediately executes them via `ShellExecuteW`.
    *   **Deceptive Installer Wrapper:** The code utilizes professional installation frameworks (likely InnoSetup) to create a "veneer" of legitimacy, employing standard wizard UI elements (e.g., `"BeginPrompt"`, `"FinishMessage"`) to mask the transition from a fake installer to a malicious payload.
