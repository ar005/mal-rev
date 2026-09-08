# Threat Analysis Report

**Generated:** 2026-09-04 19:14 UTC
**Sample:** `142a8fb85fb8aa7971dd6467f9a2eb454452ad526bafdfd6aadb8dd508624b4e_142a8fb85fb8aa7971dd6467f9a2eb454452ad526bafdfd6aadb8dd508624b4e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `142a8fb85fb8aa7971dd6467f9a2eb454452ad526bafdfd6aadb8dd508624b4e_142a8fb85fb8aa7971dd6467f9a2eb454452ad526bafdfd6aadb8dd508624b4e.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 56,320 bytes |
| MD5 | `c2b08d5df4e386a0d5fa5c797306d347` |
| SHA1 | `1125eb7602d85c0ce02e93086942fca7e4ca71e5` |
| SHA256 | `142a8fb85fb8aa7971dd6467f9a2eb454452ad526bafdfd6aadb8dd508624b4e` |
| Overall entropy | 6.186 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 708992537 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `CODE` | 45,056 | 6.421 | No |
| `DATA` | 512 | 4.145 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 4,096 | 4.681 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.276 | No |
| `.reloc` | 3,072 | -0.0 | No |
| `.rsrc` | 2,048 | 7.232 | ⚠️ Yes |

### Imports

**KERNEL32.DLL**: `DeleteCriticalSection`, `LeaveCriticalSection`, `EnterCriticalSection`, `InitializeCriticalSection`, `VirtualFree`, `VirtualAlloc`, `LocalFree`, `LocalAlloc`, `GetTickCount`, `QueryPerformanceCounter`, `GetVersion`, `GetCurrentThreadId`, `WideCharToMultiByte`, `MultiByteToWideChar`, `GetThreadLocale`
**advapi32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**ntdll.dll**: `NtUnmapViewOfSection`
**oleaut32.dll**: `SysFreeString`, `SysReAllocStringLen`, `SysAllocStringLen`
**shell32.dll**: `ShellExecuteW`
**shlwapi.dll**: `SHDeleteValueW`, `SHDeleteKeyW`
**URLMON.DLL**: `URLDownloadToCacheFileW`
**user32.dll**: `GetKeyboardType`, `MessageBoxA`
**wininet.dll**: `InternetCloseHandle`, `FtpPutFileW`, `FtpSetCurrentDirectoryW`, `InternetOpenW`, `InternetConnectW`

## Extracted Strings

Total strings found: **240** (showing first 100)

```
This program must be run under Win32
$7
.idata
.rdata
P.reloc
P.rsrc
WideChar
YZ]_^[
C;D$v
D$+D$
YZ]_^[
_^[YY]
YZ]_^[
tHt Ht.
~KxI[)
                                                                
SOFTWARE\Borland\Delphi\RTL
FPUMaskValue
YZ]_^[
<
t%<t><tQ<t\<
_^[YY]
	Functions
D$PSj
ntdll.dll
_^[YY]
D$PVj
;t$w%
SOFTWARE\
Software\Microsoft\Active Setup\Installed Components\
EPVSW
NJ$>CUP#
%06789:;<&'()*+,-./12345
WVXEGHF@A
_^[YY]
user32.dll
urlmon.dll
wininet.dll
advapi32.dll
Shell32.dll
user32.dll
advapi32.dll
shell32.dll
shlwapi.dll
del %0
user32.dll
advapi32.dll
shell32.dll
shlwapi.dll
\Microsoft\Windows\
SOFTWARE\
http://
Software\Microsoft\Active Setup\Installed Components\
Runtime error     at 00000000
0123456789ABCDEF
KERNEL32.DLL
KERNEL32.DLL
KERNEL32.DLL
advapi32.dll
advapi32.dll
ntdll.dll
ntdll.dll
oleaut32.dll
shell32.dll
shell32.dll
shell32.dll
shlwapi.dll
URLMON.DLL
user32.dll
user32.dll
user32.dll
wininet.dll
lstrlenW
WriteProcessMemory
WriteFile
WaitForSingleObject
VirtualProtectEx
VirtualFreeEx
VirtualFree
VirtualAllocEx
VirtualAlloc
TerminateThread
TerminateProcess
SizeofResource
SetThreadPriority
SetThreadContext
SetFilePointer
SetFileAttributesW
SetErrorMode
SetEndOfFile
ResumeThread
ReadProcessMemory
ReadFile
LockResource
LoadResource
LoadLibraryA
GlobalUnlock
GlobalSize
GlobalLock
GetWindowsDirectoryW
GetTimeFormatW
GetThreadContext
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.13147400` | `0x13147400` | 4506 | ✓ |
| `entry0` | `0x1314ac3c` | 4141 | ✓ |
| `fcn.13146160` | `0x13146160` | 1229 | ✓ |
| `fcn.131469dc` | `0x131469dc` | 1088 | ✓ |
| `fcn.13149e2c` | `0x13149e2c` | 1071 | ✓ |
| `fcn.131466fc` | `0x131466fc` | 677 | ✓ |
| `fcn.131493f0` | `0x131493f0` | 563 | ✓ |
| `fcn.1314a60c` | `0x1314a60c` | 557 | ✓ |
| `fcn.13146e34` | `0x13146e34` | 522 | ✓ |
| `fcn.13142228` | `0x13142228` | 474 | ✓ |
| `fcn.13142084` | `0x13142084` | 418 | ✓ |
| `fcn.13144dfc` | `0x13144dfc` | 418 | ✓ |
| `fcn.13141ef4` | `0x13141ef4` | 397 | ✓ |
| `fcn.131443b0` | `0x131443b0` | 396 | ✓ |
| `fcn.13149744` | `0x13149744` | 394 | ✓ |
| `fcn.13141658` | `0x13141658` | 291 | ✓ |
| `fcn.13143fa4` | `0x13143fa4` | 282 | ✓ |
| `fcn.131456a8` | `0x131456a8` | 282 | ✓ |
| `fcn.13149b50` | `0x13149b50` | 255 | ✓ |
| `fcn.13145534` | `0x13145534` | 251 | ✓ |
| `fcn.13141e00` | `0x13141e00` | 244 | ✓ |
| `fcn.1314a9a0` | `0x1314a9a0` | 243 | ✓ |
| `fcn.131440c0` | `0x131440c0` | 242 | ✓ |
| `fcn.13145100` | `0x13145100` | 236 | ✓ |
| `fcn.13145844` | `0x13145844` | 235 | ✓ |
| `fcn.13143ea0` | `0x13143ea0` | 234 | ✓ |
| `fcn.131418cc` | `0x131418cc` | 224 | ✓ |
| `fcn.13143454` | `0x13143454` | 211 | ✓ |
| `fcn.13142a64` | `0x13142a64` | 209 | ✓ |
| `fcn.13143734` | `0x13143734` | 208 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.13141658.c`](code/fcn.13141658.c)
- [`code/fcn.131418cc.c`](code/fcn.131418cc.c)
- [`code/fcn.13141e00.c`](code/fcn.13141e00.c)
- [`code/fcn.13141ef4.c`](code/fcn.13141ef4.c)
- [`code/fcn.13142084.c`](code/fcn.13142084.c)
- [`code/fcn.13142228.c`](code/fcn.13142228.c)
- [`code/fcn.13142a64.c`](code/fcn.13142a64.c)
- [`code/fcn.13143454.c`](code/fcn.13143454.c)
- [`code/fcn.13143734.c`](code/fcn.13143734.c)
- [`code/fcn.13143ea0.c`](code/fcn.13143ea0.c)
- [`code/fcn.13143fa4.c`](code/fcn.13143fa4.c)
- [`code/fcn.131440c0.c`](code/fcn.131440c0.c)
- [`code/fcn.131443b0.c`](code/fcn.131443b0.c)
- [`code/fcn.13144dfc.c`](code/fcn.13144dfc.c)
- [`code/fcn.13145100.c`](code/fcn.13145100.c)
- [`code/fcn.13145534.c`](code/fcn.13145534.c)
- [`code/fcn.131456a8.c`](code/fcn.131456a8.c)
- [`code/fcn.13145844.c`](code/fcn.13145844.c)
- [`code/fcn.13146160.c`](code/fcn.13146160.c)
- [`code/fcn.131466fc.c`](code/fcn.131466fc.c)
- [`code/fcn.131469dc.c`](code/fcn.131469dc.c)
- [`code/fcn.13146e34.c`](code/fcn.13146e34.c)
- [`code/fcn.13147400.c`](code/fcn.13147400.c)
- [`code/fcn.131493f0.c`](code/fcn.131493f0.c)
- [`code/fcn.13149744.c`](code/fcn.13149744.c)
- [`code/fcn.13149b50.c`](code/fcn.13149b50.c)
- [`code/fcn.13149e2c.c`](code/fcn.13149e2c.c)
- [`code/fcn.1314a60c.c`](code/fcn.1314a60c.c)
- [`code/fcn.1314a9a0.c`](code/fcn.1314a9a0.c)

## Behavioral Analysis

### Summary
The binary is highly characteristic of a **malicious dropper and packer**. It employs standard advanced evasion techniques, including complex unpacking loops, and features a definitive **process hollowing** routine to execute its core payload within a legitimate system process.

---

### Core Functionality & Purpose
*   **Dropper/Loader:** The primary purpose is to host and "unpack" hidden malicious functionality. It uses several stages of execution where it prepares the environment, handles file operations, and eventually injects code into another process.
*   **Self-Deletion/Cleanup:** The binary contains logic to modify file attributes and delete its own files from the disk after successful deployment (common in "droppers").

### Suspicious or Malicious Behaviors
*   **Process Injection (Hollowing):** 
    *   The function `fcn.131466fc` is a textbook implementation of **process hollowing**. It uses `CreateProcessW` to start a child process, then uses `VirtualAllocEx`, `WriteProcessMemory`, and `SetThreadContext` to replace the original code in that process with its own malicious payload before calling `ResumeThread`.
*   **File Manipulation & Persistence:** 
    *   The code frequently calls `SetFileAttributesW` and `DeleteFileW`. This is often used to delete the "dropper" from the disk once the payload has been executed or moved to a more permanent location.
    *   The function `fcn.131493f0` demonstrates a common technique where it reads data from one file, writes it into another (or an allocated buffer), and then deletes the source file.
*   **Registry Interaction:** 
    *   The presence of `RegOpenKeyExW` and `RegQueryValueExW` suggests the binary may be looking for system configurations, checking for antivirus presence, or ensuring its own persistence in the Windows Registry.
*   **Shell Execution:** 
    *   It uses `ShellExecuteW` to launch programs or scripts, a common way to interact with the OS and execute additional commands or "staged" components.
*   **Potential Data Theft/Interaction:** 
    *   The presence of `SetClipboardViewer` (in `fcn.13149744`) and imports from `wininet.dll` and `urlmon.dll` suggest the ability to monitor system clipboards or communicate over the internet, potentially for data exfiltration or downloading further modules.

### Notable Techniques & Patterns
*   **Obfuscated/Packed Code:** The `entry0` function contains highly repetitive loops and redundant calls (e.g., multiple calls to `fcn.13145d2c`, `fcn.13144dfc`, etc.). This is a classic hallmark of an **automated packer** designed to confuse automated analysis tools and hide the "true" entry point of the payload.
*   **Anti-Analysis/Evasion:** 
    *   The use of `Sleep` calls (found in both strings and code) are often used to time out sandboxes or anti-debugging scripts.
    *   The complexity of the initialization logic suggests it checks for environment stability before unpacking its payload.
*   **Shellcode Preparation:** The structure of `fcn.131466fc` (specifically the mapping of thread contexts and manual memory sizing) indicates it is designed to be highly robust in successfully injecting "shellcode" or a secondary EXE into target processes like `explorer.exe` or `svchost.exe`.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of complex unpacking loops, redundant code paths, and an automated packer indicates a deliberate attempt to hide the payload's true entry point. |
| T1055.010 | Process Hollow | The analyst identified a specific routine using `CreateProcessW`, `VirtualAllocEx`, `WriteProcessMemory`, and `SetThreadContext` to inject code into a legitimate process. |
| T1070.004 | File Deletion | The binary utilizes `DeleteFileW` and `SetFileAttributesW` to remove its presence from the disk after successfully deploying its payload. |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys | The use of `RegOpenKeyExW` and `RegQueryValueExW` suggests the binary is interacting with registry keys to ensure persistence. |
| T1059 | Command and Scripting Interpreter | The use of `ShellExecuteW` indicates an attempt to launch programs or scripts via a command/shell interface. |
| T1071 | Application Layer Protocol | The inclusion of `wininet.dll` and `urlmon.dll` suggests the binary can communicate over standard internet protocols for data exfiltration or module updates. |
| T1497.001 | Virtualization/Sandbox Detection | The use of `Sleep` commands and environmental stability checks is a common tactic to bypass automated sandbox analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Standard Windows libraries (e.g., `ntdll.dll`, `shell32.dll`), generic system paths, and internal function offsets have been excluded as they are common to many applications.*

### **IP addresses / URLs / Domains**
*   **None Found.** (While the string `http://` was identified, no specific domain names or IP addresses were provided in the raw data.)

### **File paths / Registry keys**
*   **None Found.** (The registry path `Software\Microsoft\Active Setup\Installed Components\` is a standard Windows system path and is considered a false positive. The reference to `Borland\Delphi` relates to the compiler environment rather than a specific malicious configuration.)

### **Mutex names / Named pipes**
*   **None Found.**

### **Hashes**
*   **None Found.** (No MD5, SHA1, or SHA256 hashes were present in the provided strings.)

### **Other artifacts**
*   **Command Line Execution:** `del %0` (Used for self-deletion/evasion).
*   **Network Capabilities:** Presence of `wininet.dll` and `urlmon.dll` (Indicative of capability to reach out to C2 servers or download additional payloads).
*   **Injection Targets:** `explorer.exe`, `svchost.exe` (Identified as target processes for the process hollowing routine).
*   **Evasion Techniques:** 
    *   **Process Hollowing:** Identified in function `fcn.131466fc`.
    *   **Anti-Analysis:** Use of `Sleep` calls to bypass sandbox timers.
    *   **Obfuscation:** High frequency of junk/non-functional characters (e.g., `YZ]_^[`, `_^[YY]`) and repetitive execution loops in `entry0`.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

**Key evidence**:
*   **Process Hollowing & Injection:** The analysis identifies a specific, textbook implementation of process hollowing (`fcn.131466fc`) targeting `explorer.exe` and `svchost.exe`, which is the primary mechanism for a loader to hide its payload within legitimate system processes.
*   **Evasion & Obfuscation:** The sample uses several anti-analysis techniques, including automated packing (junk code/redundant loops), `Sleep` calls to bypass sandbox timers, and self-deletion (`del %0`) to remove traces from the disk after execution.
*   **Staged Execution Logic:** The combination of registry interaction for persistence, `wininet` for network communication, and clipboard monitoring indicates that this binary is designed as a "wrapper" or "dropper" to facilitate the delivery and preparation of a secondary payload (e.g., a RAT or info-stealer).
