# Threat Analysis Report

**Generated:** 2026-09-02 14:53 UTC
**Sample:** `1365b90bae53129fdd75373cf05e212455f9e32cea45e8b178eb7d09f0461cd3_1365b90bae53129fdd75373cf05e212455f9e32cea45e8b178eb7d09f0461cd3.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1365b90bae53129fdd75373cf05e212455f9e32cea45e8b178eb7d09f0461cd3_1365b90bae53129fdd75373cf05e212455f9e32cea45e8b178eb7d09f0461cd3.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 5 sections |
| Size | 1,519,144 bytes |
| MD5 | `709f40889270c68811dbd7dd45b90f37` |
| SHA1 | `69588507be1d10329982e160a9d32beecea63b0a` |
| SHA256 | `1365b90bae53129fdd75373cf05e212455f9e32cea45e8b178eb7d09f0461cd3` |
| Overall entropy | 7.892 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1335420503 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.302 | No |
| `.data` | 512 | 4.971 | No |
| `.idata` | 4,608 | 5.022 | No |
| `.rsrc` | 1,475,072 | 7.906 | ⚠️ Yes |
| `.reloc` | 2,560 | 6.274 | No |

### Imports

**ADVAPI32.dll**: `GetTokenInformation`, `RegDeleteValueA`, `RegOpenKeyExA`, `RegQueryInfoKeyA`, `FreeSid`, `OpenProcessToken`, `RegSetValueExA`, `RegCreateKeyExA`, `LookupPrivilegeValueA`, `AllocateAndInitializeSid`, `RegQueryValueExA`, `EqualSid`, `RegCloseKey`, `AdjustTokenPrivileges`
**KERNEL32.dll**: `_lopen`, `_llseek`, `CompareStringA`, `GetLastError`, `GetFileAttributesA`, `GetSystemDirectoryA`, `LoadLibraryA`, `DeleteFileA`, `GlobalAlloc`, `GlobalFree`, `CloseHandle`, `WritePrivateProfileStringA`, `IsDBCSLeadByte`, `GetWindowsDirectoryA`, `SetFileAttributesA`
**GDI32.dll**: `GetDeviceCaps`
**USER32.dll**: `SetWindowLongA`, `GetDlgItemTextA`, `DialogBoxIndirectParamA`, `ShowWindow`, `MsgWaitForMultipleObjects`, `SetWindowPos`, `GetDC`, `GetWindowRect`, `DispatchMessageA`, `GetDesktopWindow`, `CharUpperA`, `SetDlgItemTextA`, `ExitWindowsEx`, `MessageBeep`, `EndDialog`
**msvcrt.dll**: `_controlfp`, `?terminate@@YAXXZ`, `_acmdln`, `_initterm`, `__setusermatherr`, `_except_handler4_common`, `memcpy`, `_ismbblead`, `__p__fmode`, `_cexit`, `_exit`, `exit`, `__set_app_type`, `__getmainargs`, `_amsg_exit`
**COMCTL32.dll**: `ord_17`
**Cabinet.dll**: `ord_22`, `ord_23`, `ord_21`, `ord_20`
**VERSION.dll**: `GetFileVersionInfoA`, `VerQueryValueA`, `GetFileVersionInfoSizeA`

## Extracted Strings

Total strings found: **3492** (showing first 100)

```
!This program cannot be run in DOS mode.
$
(Rich
`.data
.idata
@.rsrc
@.reloc
advapi32.dll
CheckTokenMembership
Reboot
AdvancedINF
Version
setupx.dll
setupapi.dll
SeShutdownPrivilege
advpack.dll
DelNodeRunDLL32
wininit.ini
Software\Microsoft\Windows\CurrentVersion\App Paths
HeapSetInformation
EXTRACTOPT
INSTANCECHECK
VERCHECK
DecryptFileA
LICENSE
<None>
REBOOT
SHOWWINDOW
ADMQCMD
USRQCMD
RUNPROGRAM
POSTRUNPROGRAM
FINISHMSG
LoadString() Error.  Could not load string resource.
CABINET
FILESIZES
PACKINSTSPACE
UPROMPT
IXP%03d.TMP
msdownld.tmp
TMP4351$.TMP
RegServer
UPDFILE%lu
Control Panel\Desktop\ResourceLocale
RSDSE>
u@G= 70
wextract.pdb
.rdata$brc
.CRT$XCA
.CRT$XCAA
.CRT$XCZ
.CRT$XIA
.CRT$XIAA
.CRT$XIY
.CRT$XIZ
.gfids
.rdata
.rdata$sxdata
.rdata$zzzdbg
.text$mn
.xdata$x
.idata$5
.00cfg
.idata$2
.idata$3
.idata$4
.idata$6
.rsrc$01
.rsrc$02
u@G= 70
PQQQQQQh 
PSSSSSSh 
D$<tXh
PVVVVVV
w;Urw
|$$95(
D$HjDj
D$@t	
WWj WWWSW
t;j
Wj
t;<\u
8
<At <Bt
<t<
t
<t<
t
<t<
t
<
t}<ty<tu
<At	<Ut
Sj@Sh@
jXhhr@
j
XPVSh
DSystem\CurrentControlSet\Control\Session Manager
rundll32.exe %sadvpack.dll,DelNodeRunDLL32 "%s"
Software\Microsoft\Windows\CurrentVersion\RunOnce
wextract_cleanup%d
rundll32.exe %s,InstallHinfSection %s 128 %s
PendingFileRenameOperations
DefaultInstall
Command.com /c %s
%s /D:%s
System\CurrentControlSet\Control\Session Manager\FileRenameOperations
SHELL32.DLL
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00405c50` | `0x405c50` | 1406 | ✓ |
| `fcn.00403b8e` | `0x403b8e` | 1101 | ✓ |
| `fcn.00401b04` | `0x401b04` | 957 | ✓ |
| `fcn.004036dc` | `0x4036dc` | 847 | ✓ |
| `fcn.0040555a` | `0x40555a` | 806 | ✓ |
| `fcn.00405933` | `0x405933` | 664 | ✓ |
| `fcn.00402ca1` | `0x402ca1` | 623 | ✓ |
| `fcn.00402033` | `0x402033` | 571 | ✓ |
| `entry0` | `0x406a00` | 489 | ✓ |
| `fcn.00404495` | `0x404495` | 468 | ✓ |
| `fcn.00404204` | `0x404204` | 426 | ✓ |
| `fcn.004028e3` | `0x4028e3` | 415 | ✓ |
| `fcn.00402f10` | `0x402f10` | 410 | ✓ |
| `fcn.00404fa0` | `0x404fa0` | 388 | ✓ |
| `fcn.00402770` | `0x402770` | 371 | ✓ |
| `fcn.00402395` | `0x402395` | 336 | ✓ |
| `fcn.00402aa5` | `0x402aa5` | 333 | ✓ |
| `fcn.00405423` | `0x405423` | 311 | ✓ |
| `fcn.004018c1` | `0x4018c1` | 308 | ✓ |
| `fcn.004067cb` | `0x4067cb` | 305 | ✓ |
| `fcn.00403fdb` | `0x403fdb` | 298 | ✓ |
| `fcn.0040226e` | `0x40226e` | 295 | ✓ |
| `fcn.00406cba` | `0x406cba` | 270 | ✓ |
| `fcn.00405276` | `0x405276` | 233 | ✓ |
| `fcn.004043ae` | `0x4043ae` | 231 | ✓ |
| `fcn.00403a2b` | `0x403a2b` | 231 | ✓ |
| `fcn.0040268a` | `0x40268a` | 230 | ✓ |
| `fcn.00406246` | `0x406246` | 228 | ✓ |
| `fcn.004051a5` | `0x4051a5` | 209 | ✓ |
| `fcn.00404ecb` | `0x404ecb` | 203 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004018c1.c`](code/fcn.004018c1.c)
- [`code/fcn.00401b04.c`](code/fcn.00401b04.c)
- [`code/fcn.00402033.c`](code/fcn.00402033.c)
- [`code/fcn.0040226e.c`](code/fcn.0040226e.c)
- [`code/fcn.00402395.c`](code/fcn.00402395.c)
- [`code/fcn.0040268a.c`](code/fcn.0040268a.c)
- [`code/fcn.00402770.c`](code/fcn.00402770.c)
- [`code/fcn.004028e3.c`](code/fcn.004028e3.c)
- [`code/fcn.00402aa5.c`](code/fcn.00402aa5.c)
- [`code/fcn.00402ca1.c`](code/fcn.00402ca1.c)
- [`code/fcn.00402f10.c`](code/fcn.00402f10.c)
- [`code/fcn.004036dc.c`](code/fcn.004036dc.c)
- [`code/fcn.00403a2b.c`](code/fcn.00403a2b.c)
- [`code/fcn.00403b8e.c`](code/fcn.00403b8e.c)
- [`code/fcn.00403fdb.c`](code/fcn.00403fdb.c)
- [`code/fcn.00404204.c`](code/fcn.00404204.c)
- [`code/fcn.004043ae.c`](code/fcn.004043ae.c)
- [`code/fcn.00404495.c`](code/fcn.00404495.c)
- [`code/fcn.00404ecb.c`](code/fcn.00404ecb.c)
- [`code/fcn.00404fa0.c`](code/fcn.00404fa0.c)
- [`code/fcn.004051a5.c`](code/fcn.004051a5.c)
- [`code/fcn.00405276.c`](code/fcn.00405276.c)
- [`code/fcn.00405423.c`](code/fcn.00405423.c)
- [`code/fcn.0040555a.c`](code/fcn.0040555a.c)
- [`code/fcn.00405933.c`](code/fcn.00405933.c)
- [`code/fcn.00405c50.c`](code/fcn.00405c50.c)
- [`code/fcn.00406246.c`](code/fcn.00406246.c)
- [`code/fcn.004067cb.c`](code/fcn.004067cb.c)
- [`code/fcn.00406cba.c`](code/fcn.00406cba.c)

## Behavioral Analysis

Based on the analysis of the decompiled C code and the associated string data, here is the breakdown of the binary's behavior:

### Core Functionality
The binary appears to be a **downloader or installer stub** (common in both Potentially Unwanted Programs (PUPs) and malware). Its primary purpose is to prepare the environment for other components, verify system compatibility, and handle the "installation" or "cleanup" of files by orchestrating calls via `rundll32.exe`.

### Suspicious and Malicious Behaviors
*   **Persistence & Execution via Registry:** 
    *   The code explicitly targets the `Software\Microsoft\Windows\CurrentVersion\RunOnce` registry key (see `fcn.00402033`). 
    *   It crafts a command string: `rundll32.exe %sadvpack.dll,DelNodeRunDLL32 "%s"`. This is a common technique to ensure that even if the initial process finishes, a secondary action (like "cleanup" or "finalization") is triggered by the system during the next session or immediately after logoff.
*   **Dynamic API Resolution:** 
    *   The binary heavily utilizes `GetProcAddress` and `LoadLibraryA` to resolve functions at runtime rather than importing them directly. This is a common technique used to bypass static analysis and hide the program's true capabilities from simple scanners.
*   **Environment & Capability Probing:** 
    *   Function `fcn.004036dc` checks for specific OS versions, high DPI support, and various system features. This indicates the code is designed to be "aware" of its environment and potentially adapt its behavior based on what it finds (e.g., choosing different installation paths or methods).
*   **File/Resource Manipulation:** 
    *   The binary contains logic for calculating disk space (`GetDiskFreeSpaceA`) and extracting information from resources. This is typical behavior for a "dropper" that extracts a payload to the system.
*   **Execution of System Utilities:**
    *   It constructs command lines involving `Command.com /c %s` and `rundll32.exe`. These are frequently used by malware to bypass security policies or to execute code in an out-of-process context (hiding it from the primary process's memory space).

### Notable Techniques & Patterns
*   **Mutex Protection:** The use of `CreateMutexA` (in `fcn.00402ca1`) ensures that only one instance of the installer/downloader runs at a time, which is standard in both legitimate installers and malware to prevent "collision" during execution.
*   **Temporary File Manipulation:** It uses `GetTempPathA` and handles logic for creating directories and moving files within temporary locations (`fcn.0040551a`, `fcn.00405933`).
*   **Resource Handling:** The code utilizes `FindResourceA`, `LoadResource`, and `LockResource` to interact with internal binary data, potentially decrypting or extracting hidden components before execution.
*   **String Masking/Processing:** Function `fcn.00405c50` shows a sophisticated loop for parsing strings, handling escaped quotes and different spacing. This is often used when the program must parse complex command lines or configuration files from a remote source.

### Summary Table of Evidence
| Feature | Observed Implementation | Significance |
| :--- | :--- | :--- |
| **Persistence** | `RunOnce` Registry key for `advpack.dll` | Ensures execution/persistence. |
| **Evasion** | Dynamic loading (`GetProcAddress`) | Obscures functionality from static analysis. |
| **Injection Point** | `rundll32.exe ... advpack.dll,DelNodeRunDLL32` | Executes logic in a separate process context. |
| **Environment Check** | `GetVersionExA`, GetSystemMetrics | Checks for high DPI and OS specific features. |
| **Data Prep** | Disk space checks & Resource extraction | Standard "dropper" behavior for secondary payloads. |

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the corresponding MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Registry Run Keys / Startup Folder | The binary targets the `RunOnce` registry key to ensure execution or "cleanup" actions occur in subsequent sessions. |
| **T1106** | Obfuscated Capabilities | The use of `GetProcAddress` and `LoadLibraryA` for dynamic API resolution is a tactic used to hide functionality from static analysis tools. |
| **T1497** | Virtualization/Sandbox Evasion | Checking OS versions, DPI support, and system features suggests the binary attempts to detect and adapt to sandbox or non-target environments. |
| **T1218** | System Binary Proxy Execution | The use of `rundll32.exe` is a common method to execute code in a trusted process context to hide it from security monitoring. |
| **T1059** | Command and Scripting Interpreter | The construction of command lines utilizing `Command.com /c` indicates the use of a built-in interpreter to execute commands or scripts. |
| **T1027** | Obfuscated Execution | The sophisticated parsing of strings and extraction of data from resources suggests an attempt to hide malicious code until it is needed during execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   **Registry Key:** `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Used for persistence)
*   **Registry Path/Key:** `System\CurrentControlSet\Control\Session Manager\FileRenameOperations`
*   **File Name:** `advpack.dll` (Specifically associated with the `DelNodeRunDLL32` export)
*   **File Name:** `wininit.ini`
*   **Temporary File Patterns:** 
    *   `IXP%03d.TMP`
    *   `msdownld.tmp`
    *   `TMP4351$.TMP`

**Mutex names / Named pipes**
*   *None explicitly identified (Note: The behavior analysis confirms the use of `CreateMutexA`, but no specific mutex string was provided).*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Command Line Pattern:** `rundll32.exe %sadvpack.dll,DelNodeRunDLL32 "%s"` (Used for executing logic in a separate process context and maintaining persistence).
*   **Dynamic API Resolution:** Use of `GetProcAddress` and `LoadLibraryA` to obfuscate functionality.
*   **Execution Pattern:** Use of `Command.com /c %s` to execute system commands via the command shell.

---

## Malware Family Classification

1. **Malware family**: custom (Generic Dropper/Loader)
2. **Malware type**: dropper / loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Dropper Functionality:** The binary performs classic "dropper" behaviors, including resource extraction, disk space checks (`GetDiskFreeSpaceA`), and the preparation of a secondary component (`advpack.dll`).
    *   **Evasion & Obfuscation:** It utilizes dynamic API resolution (`GetProcAddress`/`LoadLibraryA`) to hide its capabilities and employs environmental awareness (OS version/DPI checks) to potentially bypass sandbox detection.
    *   **Execution Steganography:** The use of `rundll32.exe` for proxy execution and the manipulation of the `RunOnce` registry key are standard techniques used to execute malicious payloads in a separate process context while ensuring persistence or completion of a multi-stage infection.
