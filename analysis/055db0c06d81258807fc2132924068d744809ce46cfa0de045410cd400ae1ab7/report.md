# Threat Analysis Report

**Generated:** 2026-07-13 19:34 UTC
**Sample:** `055db0c06d81258807fc2132924068d744809ce46cfa0de045410cd400ae1ab7_055db0c06d81258807fc2132924068d744809ce46cfa0de045410cd400ae1ab7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `055db0c06d81258807fc2132924068d744809ce46cfa0de045410cd400ae1ab7_055db0c06d81258807fc2132924068d744809ce46cfa0de045410cd400ae1ab7.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 10 sections |
| Size | 92,672 bytes |
| MD5 | `5421716788c33ac20f75e7c26a8f93c4` |
| SHA1 | `8284a87ac72a6cafb294a1e6d1ed4494cf1b772b` |
| SHA256 | `055db0c06d81258807fc2132924068d744809ce46cfa0de045410cd400ae1ab7` |
| Overall entropy | 3.984 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1776918177 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.textbss` | 0 | 0.0 | No |
| `.text` | 51,712 | 4.108 | No |
| `.rdata` | 17,408 | 2.665 | No |
| `.data` | 1,536 | 0.902 | No |
| `.pdata` | 10,240 | 1.742 | No |
| `.idata` | 6,656 | 3.264 | No |
| `.msvcjmc` | 1,024 | 0.772 | No |
| `.00cfg` | 512 | 0.479 | No |
| `.rsrc` | 1,536 | 2.143 | No |
| `.reloc` | 1,024 | 1.232 | No |

### Imports

**USER32.dll**: `SetWindowsHookExA`, `UnhookWindowsHookEx`, `CallNextHookEx`, `MessageBoxA`, `FindWindowA`, `GetWindowTextA`, `InvalidateRect`, `EndPaint`, `BeginPaint`, `GetSystemMetrics`, `EnableWindow`, `KillTimer`, `SetTimer`, `ShowWindow`, `DestroyWindow`
**GDI32.dll**: `Rectangle`, `DeleteObject`, `CreateSolidBrush`, `CreatePen`, `CreateFontA`, `SelectObject`, `SetBkMode`, `SetTextColor`, `MoveToEx`, `TextOutA`, `LineTo`
**MSVCP140D.dll**: `??1_Lockit@std@@QEAA@XZ`, `??0_Lockit@std@@QEAA@H@Z`, `?_Xlength_error@std@@YAXPEBD@Z`
**WINMM.dll**: `PlaySoundA`
**VCRUNTIME140D.dll**: `memcpy`, `__std_exception_copy`, `__std_exception_destroy`, `_CxxThrowException`, `__vcrt_LoadLibraryExW`, `memcmp`, `__C_specific_handler`, `__C_specific_handler_noexcept`, `__std_type_info_destroy_list`, `__current_exception`, `__current_exception_context`, `__vcrt_GetModuleFileNameW`, `__vcrt_GetModuleHandleW`
**VCRUNTIME140_1D.dll**: `__CxxFrameHandler4`
**ucrtbased.dll**: `_configthreadlocale`, `_set_new_mode`, `__p__commode`, `strcpy_s`, `strcat_s`, `__stdio_common_vsprintf_s`, `_seh_filter_dll`, `_initialize_onexit_table`, `_c_exit`, `_execute_onexit_table`, `_crt_atexit`, `_crt_at_quick_exit`, `terminate`, `_wmakepath_s`, `_wsplitpath_s`
**KERNEL32.dll**: `HeapAlloc`, `HeapFree`, `GetStartupInfoW`, `VirtualQuery`, `FreeLibrary`, `GetLastError`, `GetModuleHandleW`, `SetUnhandledExceptionFilter`, `InitializeSListHead`, `GetSystemTimeAsFileTime`, `GetCurrentProcessId`, `QueryPerformanceCounter`, `GetProcAddress`, `WideCharToMultiByte`, `MultiByteToWideChar`

## Extracted Strings

Total strings found: **219** (showing first 100)

```
!This program cannot be run in DOS mode.
$
.textbss
`.rdata
@.data
.pdata
@.idata
@.msvcjmc
.00cfg
@.rsrc
@.reloc
D$pHc@
D$8HcD$ H
@UVWAVH
VAVAWH
 A_A^^
@SUWATAUAVAWH
A_A^A]A\_][
@H9D$Hr
H9D$Hs
$Hc@<H
D$ H9D$(u
 H3D$0H
H9D$ u
D$ Hc@<H
H;D$@v	
L$PfC9
fD9TDPt
USVWATAUAVH
u+L95@
te+}o;>r^
A^A]A\_^[]
@5Genu
@5Auth
|$$$|.
D$8H)
_Alproxy
_Alloc_max
_Masked
_Alproxy
_Proxy
_New_capacity
_New_ptr
Unknown exception
bad array new length
invalid argument
C:\Program Files\Microsoft Visual Studio\18\Insiders\VC\Tools\MSVC\14.50.35717\include\xmemory
string too long
Shell_TrayWnd
SecureLayoutUI
System Notice
C:\Users\oscar\Downloads\Ransomware.wav
Segoe UI
STATIC
C:\Users\oscar\Downloads\FlipperIcon.ico
Oops, your files are encrypted!
This PC has been locked by OscarPlayzGaming 
What happened to my computer?
Your files have been encrypted by Oscar
What could I have done?
Got him a Fipper Zero like you promised
How do I get my computer back?
Easy! Just get me the Flipper Zero!
Unlock
BUTTON
Wrong key
Your pc is fucked!
null pointer cannot point to a block of non-zero size
bad allocation
Stack around the variable '
' was corrupted.
The variable '
' is being used without being initialized.
The value of ESP was not properly saved across a function call.  This is usually a result of calling a function declared with one calling convention with a function pointer declared with a different calling convention.

A cast to a smaller data type has caused a loss of data.  If this was intentional, you should mask the source of the cast with the appropriate bitmask.  For example:  
	char c = (i & 0xFF);
Changing the code in this way will not affect the quality of the resulting optimized code.

Stack memory was corrupted

A local variable was used before it was initialized

Stack memory around _alloca was corrupted

Unknown Runtime Check Error

Unknown Filename
Unknown Module Name
Run-Time Check Failure #%d - %s
Stack corrupted near unknown variable
Stack area around _alloca memory reserved by this function is corrupted


Data: <

Allocation number within this function: 

Size: 

Address: 0x
Stack area around _alloca memory reserved by this function is corrupted
%s%s%p%s%zd%s%d%s%s%s%s%s
A variable is being used without being initialized.
Stack pointer corruption
Cast to smaller type causing loss of data
Stack memory corruption
Local variable used before initialization
Stack around _alloca corrupted
RegOpenKeyExW
RegQueryValueExW
RegCloseKey
PDBOpenValidate5
C:\Users\oscar\source\repos\Ransom\x64\Debug\Ransom.pdb
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140011037` | `0x140011037` | 37029 | ✓ |
| `fcn.14001102d` | `0x14001102d` | 36997 | ✓ |
| `fcn.140011082` | `0x140011082` | 36948 | ✓ |
| `fcn.140011028` | `0x140011028` | 36936 | ✓ |
| `fcn.1400110b4` | `0x1400110b4` | 36934 | ✓ |
| `fcn.14001107d` | `0x14001107d` | 36881 | ✓ |
| `fcn.14001108c` | `0x14001108c` | 36842 | ✓ |
| `fcn.1400111e5` | `0x1400111e5` | 36798 | ✓ |
| `fcn.140011276` | `0x140011276` | 36701 | ✓ |
| `fcn.140011177` | `0x140011177` | 36697 | ✓ |
| `fcn.14001112c` | `0x14001112c` | 36646 | ✓ |
| `fcn.140011163` | `0x140011163` | 36639 | ✓ |
| `fcn.140011131` | `0x140011131` | 36605 | ✓ |
| `fcn.1400111fe` | `0x1400111fe` | 36502 | ✓ |
| `fcn.14001122b` | `0x14001122b` | 36481 | ✓ |
| `fcn.140011320` | `0x140011320` | 36467 | ✓ |
| `fcn.14001129e` | `0x14001129e` | 36432 | ✓ |
| `fcn.140011221` | `0x140011221` | 36419 | ✓ |
| `fcn.140011299` | `0x140011299` | 36389 | ✓ |
| `fcn.1400111cc` | `0x1400111cc` | 36384 | ✓ |
| `fcn.1400111f9` | `0x1400111f9` | 36381 | ✓ |
| `fcn.140011311` | `0x140011311` | 36341 | ✓ |
| `fcn.14001123f` | `0x14001123f` | 36323 | ✓ |
| `fcn.1400112e4` | `0x1400112e4` | 36320 | ✓ |
| `fcn.140011226` | `0x140011226` | 36312 | ✓ |
| `fcn.14001127b` | `0x14001127b` | 36299 | ✓ |
| `fcn.140011285` | `0x140011285` | 36295 | ✓ |
| `fcn.1400112b7` | `0x1400112b7` | 36293 | ✓ |
| `fcn.14001125d` | `0x14001125d` | 36216 | ✓ |
| `fcn.140011460` | `0x140011460` | 36199 | ✓ |

### Decompiled Code Files

- [`code/fcn.140011028.c`](code/fcn.140011028.c)
- [`code/fcn.14001102d.c`](code/fcn.14001102d.c)
- [`code/fcn.140011037.c`](code/fcn.140011037.c)
- [`code/fcn.14001107d.c`](code/fcn.14001107d.c)
- [`code/fcn.140011082.c`](code/fcn.140011082.c)
- [`code/fcn.14001108c.c`](code/fcn.14001108c.c)
- [`code/fcn.1400110b4.c`](code/fcn.1400110b4.c)
- [`code/fcn.14001112c.c`](code/fcn.14001112c.c)
- [`code/fcn.140011131.c`](code/fcn.140011131.c)
- [`code/fcn.140011163.c`](code/fcn.140011163.c)
- [`code/fcn.140011177.c`](code/fcn.140011177.c)
- [`code/fcn.1400111cc.c`](code/fcn.1400111cc.c)
- [`code/fcn.1400111e5.c`](code/fcn.1400111e5.c)
- [`code/fcn.1400111f9.c`](code/fcn.1400111f9.c)
- [`code/fcn.1400111fe.c`](code/fcn.1400111fe.c)
- [`code/fcn.140011221.c`](code/fcn.140011221.c)
- [`code/fcn.140011226.c`](code/fcn.140011226.c)
- [`code/fcn.14001122b.c`](code/fcn.14001122b.c)
- [`code/fcn.14001123f.c`](code/fcn.14001123f.c)
- [`code/fcn.14001125d.c`](code/fcn.14001125d.c)
- [`code/fcn.140011276.c`](code/fcn.140011276.c)
- [`code/fcn.14001127b.c`](code/fcn.14001127b.c)
- [`code/fcn.140011285.c`](code/fcn.140011285.c)
- [`code/fcn.140011299.c`](code/fcn.140011299.c)
- [`code/fcn.14001129e.c`](code/fcn.14001129e.c)
- [`code/fcn.1400112b7.c`](code/fcn.1400112b7.c)
- [`code/fcn.1400112e4.c`](code/fcn.1400112e4.c)
- [`code/fcn.140011311.c`](code/fcn.140011311.c)
- [`code/fcn.140011320.c`](code/fcn.140011320.c)
- [`code/fcn.140011460.c`](code/fcn.140011460.c)

## Behavioral Analysis

Based on the provided strings and decompiled code, here is an analysis of the binary sample:

### Core Functionality and Purpose
The binary is a **Ransomware** application. Its primary purpose is to encrypt a victim's files and display a ransom note demanding payment or specific actions (in this case, themed around "OscarPlayzGaming" and a "Flipper Zero" device). 

The presence of standard Windows GUI functions (`CreateWindowExA`, `RegisterClassA`, `SetTimer`) combined with the explicit ransom-related strings suggests the program is designed to:
1.  Perform file encryption (implied by the narrative in the strings).
2.  Display a localized user interface (UI) to inform the victim of the lock.
3.  Play audio files (`Ransomware.wav`) and display icons to engage the victim.

### Suspicious and Malicious Behaviors
*   **Ransomware Activity:** The strings explicitly confirm malicious intent:
    *   *"Oops, your files are encrypted!"*
    *   *"This PC has been locked by OscarPlayzGaming"*
    *   *"Your files have been encrypted by Oscar"*
*   **Persistence & Configuration:** The inclusion of `RegOpenKeyExW`, `RegQueryValueExW`, and `RegCloseKey` indicates the malware interacts with the Windows Registry. This is commonly used to check for system configuration, ensure persistence, or determine if it is running in a sandbox/virtual environment.
*   **Anti-Analysis/Evasion:** The presence of **`IsDebuggerPresent`** is a classic anti-debugging technique. It allows the malware to detect if it is being run inside a debugger (like x64dbg) and potentially change its behavior or terminate to prevent analysis by security researchers.
*   **User Interaction Manipulation:** 
    *   The use of `MessageBoxA` and various UI elements suggests a "lock screen" experience where the user cannot easily interact with their PC without complying with the demands.
    *   **`PlaySoundA`** is used to play audio files, which can be used to alert or distress the victim immediately upon infection.

### Notable Techniques and Patterns
*   **Thematic/Scripted Ransom Note:** The strings suggest a "scavenger hunt" or specific theme (referencing a "Flipper Zero"). This is often seen in "troll" malware or localized ransomware campaigns designed to target specific communities.
*   **Standard Library Usage:** The decompiled code shows the use of standard C libraries (`ucrtbased.dll`, `VCRUNTIME140D.dll`). While these are standard, they indicate that the code was likely compiled using Microsoft Visual Studio (confirmed by the PDB path: `C:\Users\oscar\source\repos\Ransom\...`).
*   **Evidence of Development:** The presence of a PDB (Program Database) path in the strings (`.../Ransom.pdb`) suggests that this might be a "proof-of-concept" or a sample from a developer's local machine, as professional malware usually strips these paths to hide the original file structure.

### Summary Table
| Category | Observations |
| :--- | :--- |
| **Malware Type** | Ransomware / Locker |
| **Primary Goal** | File encryption and extortion via ransom notes. |
| **Evasion Techniques** | `IsDebuggerPresent` (Anti-debugging). |
| **User Interaction** | Audio alerts (`PlaySoundA`), GUI creation, and "Unlock" buttons. |
| **Persistence/Config** | Registry manipulation (`RegOpenKeyExW`). |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1486 | Data Encrypted for Impact | The binary is explicitly identified as ransomware that encrypts files and displays a ransom note to extort the user. |
| T1497 | Virtualization/Sandbox Evasion | The use of `IsDebuggerPresent` is a common method to detect if the malware is being analyzed in a debugger or virtual environment. |
| T1112 | Modify Registry | The inclusion of `RegOpenKeyExW`, `RegQueryValueExW`, and `RegCloseKey` indicates interaction with the Windows Registry for configuration or persistence. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `C:\Users\oscar\Downloads\Ransomware.wav`
*   `C:\Users\oscar\Downloads\FlipperIcon.ico`
*   `C:\Users\oscar\source\repos\Ransom\x64\Debug\Ransom.pdb`

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Campaign/Actor Identity Strings:** "OscarPlayzGaming", "Flipper Zero" (used in ransom notes).
*   **Anti-Analysis Techniques:** `IsDebuggerPresent` (Function used to detect debugger presence).
*   **Hardcoded UI Text:** "Oops, your files are encrypted!", "This PC has been locked by OscarPlayzGaming", "Your files have been encrypted by Oscar".

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: ransomware
3. **Confidence**: High
4. **Key evidence**:
    *   **Explicit Ransomware Behavior:** The sample contains hardcoded strings explicitly stating that files are encrypted and displaying demands from "OscarPlayzGaming," which is characteristic of locker-style behavior.
    *   **Evasion & Persistence:** The inclusion of `IsDebuggerPresent` for anti-debugging and registry manipulation (`RegOpenKeyExW`) indicates intentional functionality to evade analysis and manage system state.
    *   **Development Artifacts:** The presence of a PDB path (`C:\Users\oscar\source\repos\...`) and unique branding suggests this is a custom-built sample or a "troll" tool rather than a widely distributed, automated malware strain like LockBit or Conti.
