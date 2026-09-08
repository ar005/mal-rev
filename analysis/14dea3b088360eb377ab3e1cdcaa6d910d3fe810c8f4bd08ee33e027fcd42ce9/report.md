# Threat Analysis Report

**Generated:** 2026-09-06 09:57 UTC
**Sample:** `14dea3b088360eb377ab3e1cdcaa6d910d3fe810c8f4bd08ee33e027fcd42ce9_14dea3b088360eb377ab3e1cdcaa6d910d3fe810c8f4bd08ee33e027fcd42ce9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14dea3b088360eb377ab3e1cdcaa6d910d3fe810c8f4bd08ee33e027fcd42ce9_14dea3b088360eb377ab3e1cdcaa6d910d3fe810c8f4bd08ee33e027fcd42ce9.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 5 sections |
| Size | 38,067,845 bytes |
| MD5 | `75d6d2b38a8d164866917eefbd9d1e80` |
| SHA1 | `491cc335eba69ffb4b42b210723115dc7f4edd91` |
| SHA256 | `14dea3b088360eb377ab3e1cdcaa6d910d3fe810c8f4bd08ee33e027fcd42ce9` |
| Overall entropy | 8.0 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1296495853 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 4,096 | 5.942 | No |
| `.rdata` | 4,096 | 1.736 | No |
| `.data` | 4,096 | 1.011 | No |
| `.gentee` | 61,440 | 7.833 | ⚠️ Yes |
| `.rsrc` | 20,480 | 6.54 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `WriteFile`, `CreateDirectoryA`, `lstrcpyA`, `CreateFileA`, `GetFileAttributesA`, `lstrlenA`, `GetTempPathA`, `lstrcmpA`, `lstrcatA`, `ExitProcess`, `DeleteFileA`, `FreeLibrary`, `GetProcAddress`, `LoadLibraryA`
**USER32.dll**: `MessageBoxA`, `wsprintfA`
**MSVCRT.dll**: `_exit`, `_XcptFilter`, `exit`, `_acmdln`, `__getmainargs`, `_initterm`, `__setusermatherr`, `_adjust_fdiv`, `__p__commode`, `__p__fmode`, `__set_app_type`, `_except_handler3`, `_controlfp`

## Extracted Strings

Total strings found: **82572** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.gentee
@.rsrc
t=SUW3
|$LVh40@
D$DRWP
\$UV3
j
XPVSS
Gentee Launcher
CloseHandle
WriteFile
CreateDirectoryA
lstrcpyA
CreateFileA
GetFileAttributesA
lstrlenA
GetTempPathA
lstrcmpA
lstrcatA
ExitProcess
DeleteFileA
FreeLibrary
GetProcAddress
LoadLibraryA
GetModuleHandleA
GetFileSize
GetLastError
CreateMutexA
GetModuleFileNameA
VirtualAlloc
VirtualFree
KERNEL32.dll
wsprintfA
MessageBoxA
USER32.dll
_XcptFilter
_acmdln
__getmainargs
_initterm
__setusermatherr
_adjust_fdiv
__p__commode
__p__fmode
__set_app_type
_except_handler3
MSVCRT.dll
_controlfp
GetStartupInfoA
Cannot create gentee.dll!
c:\temp
%s\genteert.dll
launcher_get
lzge_decode
ERROR: 
The executable file does not have a bytecode!
gentee_call
gentee_set
gentee_load
gentee_deinit
gentee_init
Cannot load %s.
The file is corrupted. It was downloaded with errors or otherwise damaged.
Please download it again and make sure that you do not have viruses.
The application has already run.
f#WoV_
8,=f'W
	e"+Q+
bVd[xL
xid4:HA
>*Ouz@3
.4-{(B
m2	zkR
!'
NUgwYsi 6
 *E@1-
[l}\J	lh
9	Tv~
"'v}j]
gva-X/=
w
HPDGHA
5N*4@~
qqbxnz
Lzj-D"
p4j$/c
b0I9glO
{	@:_Y
vO?(Ak
fgMbiu
tU#5}g
EpnovW
)K|1=|}6
TRl&~C
U) (:S@S
zI><./
4jbGPq
gM|%r5
WZB=J9GZ
rafX+&A.
eR^*

es:3ez
```

## Disassembly Overview

Functions analyzed: **23** | Decompiled to C: **23**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `main` | `0x4018d0` | 571 | ✓ |
| `fcn.004012b0` | `0x4012b0` | 522 | ✓ |
| `fcn.00401050` | `0x401050` | 508 | ✓ |
| `fcn.004016a0` | `0x4016a0` | 400 | ✓ |
| `entry0` | `0x401d20` | 338 | ✓ |
| `fcn.00401570` | `0x401570` | 252 | ✓ |
| `fcn.00401b50` | `0x401b50` | 203 | ✓ |
| `fcn.004014c0` | `0x4014c0` | 109 | ✓ |
| `fcn.00401c60` | `0x401c60` | 74 | ✓ |
| `fcn.00401260` | `0x401260` | 73 | ✓ |
| `fcn.00401cd0` | `0x401cd0` | 73 | ✓ |
| `section..text` | `0x401000` | 72 | ✓ |
| `fcn.00401530` | `0x401530` | 54 | ✓ |
| `fcn.00401670` | `0x401670` | 47 | ✓ |
| `fcn.00401b20` | `0x401b20` | 34 | ✓ |
| `fcn.00401c20` | `0x401c20` | 23 | ✓ |
| `fcn.00401cb0` | `0x401cb0` | 22 | ✓ |
| `fcn.00401c40` | `0x401c40` | 21 | ✓ |
| `fcn.00401e8a` | `0x401e8a` | 18 | ✓ |
| `sub.MSVCRT.dll__controlfp` | `0x401ea6` | 6 | ✓ |
| `sub.MSVCRT.dll__initterm` | `0x401e84` | 6 | ✓ |
| `sub.MSVCRT.dll__XcptFilter` | `0x401e7e` | 6 | ✓ |
| `fcn.00401e9f` | `0x401e9f` | 1 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401050.c`](code/fcn.00401050.c)
- [`code/fcn.00401260.c`](code/fcn.00401260.c)
- [`code/fcn.004012b0.c`](code/fcn.004012b0.c)
- [`code/fcn.004014c0.c`](code/fcn.004014c0.c)
- [`code/fcn.00401530.c`](code/fcn.00401530.c)
- [`code/fcn.00401570.c`](code/fcn.00401570.c)
- [`code/fcn.00401670.c`](code/fcn.00401670.c)
- [`code/fcn.004016a0.c`](code/fcn.004016a0.c)
- [`code/fcn.00401b20.c`](code/fcn.00401b20.c)
- [`code/fcn.00401b50.c`](code/fcn.00401b50.c)
- [`code/fcn.00401c20.c`](code/fcn.00401c20.c)
- [`code/fcn.00401c40.c`](code/fcn.00401c40.c)
- [`code/fcn.00401c60.c`](code/fcn.00401c60.c)
- [`code/fcn.00401cb0.c`](code/fcn.00401cb0.c)
- [`code/fcn.00401cd0.c`](code/fcn.00401cd0.c)
- [`code/fcn.00401e8a.c`](code/fcn.00401e8a.c)
- [`code/fcn.00401e9f.c`](code/fcn.00401e9f.c)
- [`code/main.c`](code/main.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sub.MSVCRT.dll__XcptFilter.c`](code/sub.MSVCRT.dll__XcptFilter.c)
- [`code/sub.MSVCRT.dll__controlfp.c`](code/sub.MSVCRT.dll__controlfp.c)
- [`code/sub.MSVCRT.dll__initterm.c`](code/sub.MSVCRT.dll__initterm.c)

## Behavioral Analysis

Based on the analysis of the provided disassembly and strings, here is a summary of the findings for this binary.

### Core Functionality and Purpose
The binary functions as a **stub loader or "dropper."** It is designed to act as a preliminary wrapper that prepares the environment and extracts secondary components before executing the primary malicious payload. 

Its main role is to:
1.  Check for local environment conditions (e.g., ensuring it isn't already running via `CreateMutexA`).
2.  Verify the presence of an internal "bytecode" or resource.
3.  Extract and save a DLL file (`genteert.dll`) from its own resources or data sections to the disk.
4.  Load that dynamically created DLL into memory to perform the actual logic (likely the primary malware functionality).

### Suspicious and Malicious Behaviors
The following behaviors are characteristic of Trojan downloaders or loaders:

*   **Payload Dropping:** The code explicitly checks if `genteert.dll` exists in a temporary path (e.g., `%TEMP%\genteert.dll`). If it doesn't exist, the program creates a directory and "drops" the DLL onto the filesystem via `WriteFile`.
*   **Temporary File Manipulation:** It utilizes system paths like `c:\temp` or the environment’s temp folder to stage its secondary components, a common tactic to hide malicious files in locations often overlooked by basic security scans.
*   **Self-Deleting/Cleanup:** The code contains calls to `DeleteFileA`. This is typically used to delete the "source" data (the bytecode) once it has been loaded into memory or to remove the dropped DLL after execution, minimizing the forensic footprint left on the system.
*   **Dynamic API Resolving:** The use of `GetProcAddress` and `LoadLibraryA` to find functions like `gentee_init`, `gentee_call`, and `gentee_set` indicates that the core functionality is not contained in the main `.exe`. This hides the true intent of the program from static analysis.

### Notable Techniques and Patterns
*   **Stub/Wrapper Architecture:** The "Gentee Launcher" name and the error messages (e.g., *"The executable file does not have a bytecode!"*) suggest a modular design where the launcher is a low-complexity wrapper, and the actual malicious logic resides in the dynamically loaded component.
*   **Resource Extraction:** The complexity of functions like `fcn.004012b0` and its associated helper functions suggests a custom unpacking or decoding routine used to process internal data before it can be saved as a usable DLL.
*   **Evasion through Separation:** By splitting the functionality into a "Launcher" and a "Library," the author ensures that basic antivirus scanners only see a small, less-suspicious piece of code (the launcher) during initial execution.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Executables | The use of a "stub" architecture and custom decoding routines to extract hidden DLLs from internal resources conceals the primary payload's purpose from static analysis. |
| T1106 | Obfuscated Capabilities | The use of `GetProcAddress` and `LoadLibraryA` to dynamically resolve functions hides the program's actual functionality from static scanners. |
| T1497 | Virtualized Environment Detection | The implementation of `CreateMutexA` is used to check for existing instances or identify if the binary is being executed in a controlled analysis environment. |
| T1070.004 | Indicator Removal on Host: File Deletion | The use of `DeleteFileA` to remove "source" data and intermediate files minimizes the forensic footprint left on the system after execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `c:\temp` (Used as a staging directory)
*   `genteert.dll` (The primary payload dropped by the loader)

**Mutex names / Named pipes**
*   *(None specifically named; however, the use of `CreateMutexA` for execution checking was noted in behavioral analysis)*

**Hashes**
*   *(None found in the provided strings)*

**Other artifacts**
*   **Application Name:** Gentee Launcher
*   **Dropped File Name:** `genteert.dll`
*   **Internal Functions (Export/Import points):** 
    *   `gentee_init`
    *   `gentee_call`
    *   `gentee_set`
    *   `gentee_load`
    *   `gentee_deinit`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / dropper
3. **Confidence**: High

**Key evidence**:
*   **Payload Extraction & Deployment:** The binary acts as a classic "stub," specifically designed to extract `genteert.dll` from its own resources and drop it into a temporary directory (`%TEMP%`) for execution.
*   **Evasive Execution:** It utilizes dynamic API resolution (`GetProcAddress`, `LoadLibraryA`) to hide its primary functional calls, ensuring the main logic is contained within a dynamically loaded library rather than the initial executable.
*   **Anti-Forensic Measures:** The use of `CreateMutexA` for environment/instance checking and `DeleteFileA` to remove intermediate "source" data indicates a deliberate attempt to minimize the forensic footprint on the host system.
