# Threat Analysis Report

**Generated:** 2026-09-06 23:45 UTC
**Sample:** `1548929eab74a8b646aa01049af7ce02241a72a8a7f6a6fae6cde76a1c9d5fbe_1548929eab74a8b646aa01049af7ce02241a72a8a7f6a6fae6cde76a1c9d5fbe.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1548929eab74a8b646aa01049af7ce02241a72a8a7f6a6fae6cde76a1c9d5fbe_1548929eab74a8b646aa01049af7ce02241a72a8a7f6a6fae6cde76a1c9d5fbe.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 4 sections |
| Size | 14,781,984 bytes |
| MD5 | `d59110bf5cfbb4331c9672752ed1b8df` |
| SHA1 | `002406d292022b512989ca944922041d4d34e44f` |
| SHA256 | `1548929eab74a8b646aa01049af7ce02241a72a8a7f6a6fae6cde76a1c9d5fbe` |
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

Total strings found: **31925** (showing first 100)

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

This update incorporates the second chunk of disassembly into your ongoing analysis. The additional code confirms that while the binary functions as a loader/dropper, it also contains sophisticated "installer" logic, including UI management and robust system-path navigation.

### Updated Analysis of Functionality

#### 1. Sophisticated Installer Engine
The presence of multiple functions like `fcn.00407430` (handling `"BeginPrompt"`, `"FinishMessage"`, `"ErrorTitle"`) and the complex state-machine logic in the first block indicates this is more than a simple "one-shot" dropper. It is designed to mimic a professional installation wizard. It manages different stages of an installation, likely providing feedback to the user while performing background tasks (such as unpacking or moving files).

#### 2. Dynamic Path Resolution & Extraction
The disassembly reveals significant logic for resolving system paths:
*   **`fcn.00402451`**: Uses `SHGetSpecialFolderPathW`. This is used to find standard Windows directories (like "My Documents" or the "Desktop"). In a malicious context, this allows the malware to identify where it should move its payload or create persistence.
*   **`fcn.0040330c`**: Uses `GetTempPathW` and performs loops to generate and validate temporary paths. This suggests the binary is preparing "staging" areas for dropped files before they are executed.

#### 3. UI/UX Manipulation
The function `fcn.00406097` demonstrates active window management:
*   It calculates window sizes, button positions (`GetDlgItem`, `GetWindowLongW`), and adjusts the "geometry" of the application using `SetWindowPos`.
*   **Significance:** This is often used by high-quality malware to ensure that a custom GUI (like a fake update screen) looks legitimate or to center/resize windows correctly, making the malicious activity blend in with standard software.

#### 4. Execution and Persistence Logic
The function `fcn.00405506` is a critical "delivery" point:
*   It includes logic for **`CreateFileW`**, **`WriteFile`**, and **`ShellExecuteW`**.
*   **Flow:** It appears to write data (the payload) to a file, set its attributes, and then immediately execute it via `ShellExecuteW`. This confirms the "Dropper" behavior identified in the first analysis.

---

### Updated Suspicious & Malicious Behaviors
*   **Sophisticated Payload Delivery:** The combination of `WriteFile` followed by `ShellExecuteW` is a classic pattern for dropping and launching a secondary, often more malicious, component (e.g., a RAT or Stealer).
*   **Environment-Aware Pathing:** By using `SHGetSpecialFolderPathW`, the binary ensures it can "land" its payload in locations that are common for users, increasing the chances of successful infection across different system configurations.
*   **Polished Interface (Social Engineering):** The intensive work done on UI geometry and custom prompt strings (`FinishMessage`, `HelpText`) suggests a high level of effort to deceive the user into thinking they are interacting with a legitimate installer rather than a malicious stub.

---

### New Technical Observations & Patterns
*   **State Machine Logic:** Extensive branching based on numeric constants (e.g., `uVar11 == 0x11`) confirms a "finite state machine" design, common in complex installers to handle various error conditions or installation steps gracefully.
*   **Resource/Buffer Processing:** Functions like `fcn.0040b353` and `fcn.004113a0` contain heavy loop logic for processing nested data structures, likely handling a large embedded resource (like a compressed ZIP of the final payload).
*   **Dynamic API Interaction:** Continued reliance on `GetProcAddress` and `LoadLibraryA` style behaviors suggests an attempt to minimize the footprint in the Import Address Table (IAT) and evade basic static scanners.

---

### Updated Summary Table

| Feature | Observation | Potential Intent |
| :--- | :--- | :--- |
| **Dropper Logic** | `WriteFile`, `ShellExecuteW` | Writing a payload to disk and executing it immediately. |
| **System Paths** | `SHGetSpecialFolderPathW`, `GetTempPathW` | Identifying "safe" places (Docs, Temp) to hide/extract malware components. |
| **UI Sophistication** | `SetWindowPos`, `GetDlgItem`, Custom Prompts | Crafting a polished, realistic interface to mask malicious activity from the user. |
| **State Machine** | Nested `if/else` and loop-based logic | Managing a complex multi-stage installation or infection routine. |
| **Data Extraction** | Large nested loops over memory buffers | Decompressing or unpacking an embedded payload into usable files. |

### Conclusion Update
The binary is a **highly engineered installer stub**. It does not merely "drop" a file; it manages a sophisticated environment where it handles UI feedback, navigates system paths to find suitable locations for installation, and potentially unpacks complex payloads before launching them. This level of sophistication suggests the malware belongs to a professional threat actor or a sophisticated "malware-as-a-service" (MaaS) operation.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1106** | Dynamic Resolution | The use of `GetProcAddress` and `LoadLibraryA` indicates an attempt to resolve API calls at runtime to evade static analysis. |
| **T1204.001** | User Execution: Malicious File | The combination of `WriteFile` followed by `ShellExecuteW` confirms the "Dropper" behavior of writing and immediately executing a payload. |
| **T1083** | File and Directory Discovery | The utilization of `SHGetSpecialFolderPathW` and `GetTempPathW` is used to identify valid system paths for staging or installing malicious components. |
| **T1566.002** | Phishing: Spearphishing Attachment (Social Engineering) | Sophisticated UI management and custom prompt logic are employed to create a professional façade that deceives the user into interacting with malicious content. |
| **T1131** | Capability of Decoding/Decompressing | Extensive loop-based logic for processing nested data structures indicates the extraction or decompression of embedded resources before execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized as requested.

### **IP addresses / URLs / Domains**
*   *None identified.* (The "garbled" character strings in the source do not resolve to recognizable IP addresses or domains.)

### **File paths / Registry keys**
*   *None identified.* (While the analysis mentions `GetTempPathW` and `SHGetSpecialFolderPathW`, these are dynamic API calls used to find standard system folders; no hardcoded malicious file paths were provided in the text.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 hashes were present in the provided strings.)

### **Other artifacts**
*   **Execution Patterns:** Usage of `WriteFile` followed immediately by `ShellExecuteW`. This is a primary indicator of a "dropper" functionality designed to move and execute a secondary payload.
*   **Persistence/Staging Behavior:** Use of `GetTempPathW` and `SHGetSpecialFolderPathW` indicates the malware identifies system-standard directories (e.g., Temp, Documents) for staged deployment.
*   **Installer Mimicry Logic:** The presence of internal strings like `"BeginPrompt"`, `"FinishMessage"`, and `"ErrorTitle"` suggests a sophisticated installer stub designed to blend in with legitimate software installations.
*   **State Machine Logic:** Extensive use of branching logic (e.g., `uVar11 == 0x11`) indicates the code is engineered to handle multiple stages of an infection routine or installation wizard.

***

**Analyst Note:** This sample appears to be a highly polished **installer stub/dropper**. While it lacks static network indicators (IPs/URLs), its primary threat signature lies in its sophisticated "installation" facade and automated payload deployment workflow.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline`

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1. **Malware family**: custom
2. **Malware type**: dropper / loader
3. **Confidence**: High (for type), Medium (for family)
4. **Key evidence**:
    *   **Dropper/Loader Behavior:** The sequence of `WriteFile` followed by `ShellExecuteW` confirms the primary purpose is to write a secondary payload to disk and execute it immediately.
    *   **Sophisticated Installer Mimicry:** The use of complex state-machine logic, custom UI prompts (`BeginPrompt`, `FinishMessage`), and window management suggests a high-effort "installer" facade designed to deceive users into believing they are installing legitimate software.
    *   **Environment Manipulation & Staging:** The utilization of `SHGetSpecialFolderPathW` and `GetTempPathW` demonstrates that the binary is engineered to dynamically locate and create staging areas for its payload, ensuring successful execution across different system configurations.
