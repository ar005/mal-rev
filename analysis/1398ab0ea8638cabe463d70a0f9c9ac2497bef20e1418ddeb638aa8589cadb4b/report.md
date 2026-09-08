# Threat Analysis Report

**Generated:** 2026-09-02 19:31 UTC
**Sample:** `1398ab0ea8638cabe463d70a0f9c9ac2497bef20e1418ddeb638aa8589cadb4b_1398ab0ea8638cabe463d70a0f9c9ac2497bef20e1418ddeb638aa8589cadb4b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1398ab0ea8638cabe463d70a0f9c9ac2497bef20e1418ddeb638aa8589cadb4b_1398ab0ea8638cabe463d70a0f9c9ac2497bef20e1418ddeb638aa8589cadb4b.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 5 sections |
| Size | 1,502,760 bytes |
| MD5 | `a780276638a8882ab1168c1c9ad080d2` |
| SHA1 | `62bccb364e1af498e72d522d7ab569a405992f9b` |
| SHA256 | `1398ab0ea8638cabe463d70a0f9c9ac2497bef20e1418ddeb638aa8589cadb4b` |
| Overall entropy | 7.91 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1537751781 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 6.302 | No |
| `.data` | 512 | 4.971 | No |
| `.idata` | 4,608 | 5.022 | No |
| `.rsrc` | 1,458,688 | 7.924 | ⚠️ Yes |
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

Total strings found: **3463** (showing first 100)

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

Based on the provided disassembly and strings, here is an analysis of the binary's functionality.

### Core Functionality
The binary appears to be a **dropper or installer** (possibly for potentially unwanted programs or malware). Its primary role is to prepare a system environment, extract/install components, and then perform "cleanup" operations to remove evidence of its presence.

### Suspicious or Malicious Behaviors

*   **Persistence and Execution via Registry:**
    *   The code specifically targets the `Software\Microsoft\Windows\CurrentVersion\RunOnce` registry key (seen in functions `fcn.00402033` and `fcn.0040226e`). 
    *   It uses this key to schedule a command involving `rundll32.exe`. Specifically, it builds a command like: `rundll32.exe %sadvpack.dll,DelNodeRunDLL32 "%s"`. This is a common technique to ensure that a cleanup routine or a secondary payload executes immediately after the current process finishes or upon the next login.

*   **Self-Deletion and Cleanup:**
    *   The function `fcn.00402395` contains a loop that iterates through files in a directory, sets their attributes (likely to make them hidden or system files), and calls `DeleteFileA`. 
    *   Following this, it calls `RemoveDirectoryA`. This indicates an attempt to "wipe" temporary files or the original installer's footprint from the disk after the payload has been successfully deployed.

*   **Environment Manipulation:**
    *   The binary performs several system checks typical of an automated installer: checking for available disk space (`GetDiskFreeSpaceA`), verifying Windows version information, and ensuring required directories exist (using `CreateDirectoryA` in `fcn.00405423`).
    *   It uses `SetFileAttributesA` to modify the attributes of files (likely hiding them) before moving or deleting them.

*   **Resource Extraction:**
    *   The code frequently interacts with `FindResourceA`, `LoadResource`, and `LockResource`. This suggests that the primary payload is embedded as a resource within this binary and is being "unpacked" into memory or onto the disk during execution.

### Notable Techniques & Patterns

*   **Use of Windows Installer Logic:** The strings (`InstallHinfSection`, `DelNodeRunDLL32`, `advpack.dll`) suggest the author used components from standard Windows installation frameworks (like `setupapi.dll` and `msi.dll`). This is common in "Grayware" or malware to blend in with legitimate software installers.
*   **Dynamic API Resolution:** The presence of `GetProcAddress` and `GetModuleHandleA` combined with the logic in `fcn.00402ca1` suggests the binary resolves certain functions at runtime, which is a common technique to bypass simple static analysis or hide its true capabilities until it is running.
*   **Wrapper/Staging Behavior:** The code structure indicates it acts as a "loader." It prepares paths, creates temporary directories (using `GetTempPathA`), and uses `CreateProcessA` to launch components, while the main binary stays active enough to ensure the process succeeds before cleaning up its own files.

### Summary of Risk
This sample is highly characteristic of a **dropper**. Its primary risk involves:
1.  **Payload Delivery:** Extracting hidden resources and executing them on the system.
2.  **Evasion:** Using `RunOnce` and file-deletion loops to remove traces of its existence after the initial infection/installation. 
3.  **System Manipulation:** Altering file attributes and registry keys to ensure the intended behavior (malicious or otherwise) persists on the host machine.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1546.003 | RunKey | The binary targets the `RunOnce` registry key to ensure that specific commands or cleanup routines execute automatically. |
| T1070.004 | File Deletion | The code contains a loop using `DeleteFileA` and `RemoveDirectoryA` to remove its tracks from the file system after execution. |
| T1564.001 | Hide Files and Directories | The use of `SetFileAttributesA` suggests an attempt to mask the presence of files by altering their attributes before deletion or movement. |
| T1137 | Dynamic Resolution | The use of `GetProcAddress` and `GetModuleHandleA` allows the binary to resolve API calls at runtime, helping to evade static analysis. |
| T1027 | Obfuscated Files or Information | The inclusion of a payload within resources (requiring extraction) is used to hide the true functionality of the primary malicious component. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   **Registry Key:** `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Used for persistence/execution of cleanup tasks).
*   **File Artifacts (Temporary Files):** 
    *   `IXP%03d.TMP`
    *   `msdownld.tmp`
    *   `TMP4351$.TMP`
*   **Note:** Other paths like `Control Panel\Desktop\ResourceLocale` and standard System Manager paths were excluded as they are common Windows system defaults.

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None provided in the source text.*

**Other artifacts**
*   **Command Execution Pattern:** `rundll32.exe %sadvpack.dll,DelNodeRunDLL32 "%s"` (Used to trigger hidden cleanup routines).
*   **Behavioral Artifacts:** 
    *   Utilization of `advpack.dll` and `DelNodeRunDLL32` for post-installation "cleanup" or anti-forensics.
    *   Usage of the `GetTempPathA` and `CreateProcessA` functions to stage files in temporary directories before execution.
    *   Systematic modification of file attributes (making files hidden/system) prior to deletion via `RemoveDirectoryA`.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Resource Extraction and Staging:** The binary utilizes `FindResourceA`, `LoadResource`, and `LockResource` to extract an embedded payload, which is then staged in temporary directories (using `GetTempPathA`) before being executed via `CreateProcessA`.
*   **Anti-Forensics/Cleanup Logic:** The sample exhibits clear "self-deletion" behavior by manipulating file attributes with `SetFileAttributesA`, utilizing the `RunOnce` registry key to trigger cleanup commands, and executing a loop to delete its own components and directories from the disk.
*   **Evasion Techniques:** The use of dynamic API resolution (`GetProcAddress`/`GetModuleHandleA`) and the intentional naming conventions (e.g., `advpack.dll`) indicate an attempt to mask functionality from static analysis while blending in with legitimate installer behaviors.
