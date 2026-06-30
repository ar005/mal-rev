# Threat Analysis Report

**Generated:** 2026-06-29 21:45 UTC
**Sample:** `035ca113035ac928f69d90d573c73dba2c589ae4478e0cb8e98e4f14a21a8631_035ca113035ac928f69d90d573c73dba2c589ae4478e0cb8e98e4f14a21a8631.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `035ca113035ac928f69d90d573c73dba2c589ae4478e0cb8e98e4f14a21a8631_035ca113035ac928f69d90d573c73dba2c589ae4478e0cb8e98e4f14a21a8631.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 6 sections |
| Size | 17,408 bytes |
| MD5 | `cc744cba33cf300c7823b7d4774a407b` |
| SHA1 | `824e553d7d9fa1cfce98e1b22ce6c03648811861` |
| SHA256 | `035ca113035ac928f69d90d573c73dba2c589ae4478e0cb8e98e4f14a21a8631` |
| Overall entropy | 5.201 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1772643528 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 7,168 | 6.059 | No |
| `.rdata` | 6,656 | 4.286 | No |
| `.data` | 512 | 2.067 | No |
| `.pdata` | 1,024 | 2.888 | No |
| `.rsrc` | 512 | 4.702 | No |
| `.reloc` | 512 | 1.168 | No |

### Imports

**KERNEL32.dll**: `FindClose`, `Sleep`, `CreateFileA`, `DeleteFileA`, `CloseHandle`, `FindNextFileA`, `SetFileAttributesA`, `RemoveDirectoryA`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetSystemTimeAsFileTime`, `WriteFile`, `GetCurrentProcess`, `CreateThread`, `FindFirstFileA`
**USER32.dll**: `MessageBoxA`
**ADVAPI32.dll**: `LookupPrivilegeValueA`, `OpenProcessToken`, `AdjustTokenPrivileges`
**MSVCP140.dll**: `?_Xlength_error@std@@YAXPEBD@Z`
**VCRUNTIME140_1.dll**: `__CxxFrameHandler4`
**VCRUNTIME140.dll**: `__current_exception`, `__std_exception_copy`, `__std_exception_destroy`, `__C_specific_handler`, `__current_exception_context`, `_CxxThrowException`, `memset`, `memcpy`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__p__commode`, `_set_fmode`, `__stdio_common_vsprintf_s`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_cexit`, `_c_exit`, `_register_thread_local_exe_atexit_callback`, `__p___argc`, `_initterm`, `_get_initial_narrow_environment`, `_initterm_e`, `_initialize_onexit_table`, `_register_onexit_function`, `_crt_atexit`, `terminate`, `_initialize_narrow_environment`, `system`, `_exit`, `__p___argv`
**api-ms-win-crt-heap-l1-1-0.dll**: `free`, `_callnewh`, `malloc`, `_set_new_mode`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

## Extracted Strings

Total strings found: **151** (showing first 100)

```
!This program cannot be run in DOS mode.
$
URichy
`.rdata
@.data
.pdata
@.rsrc
@.reloc
D$@p2D
D$\03-Q
D$xu{b
u@8l$~
L$ SVWH
L$ SVWH
@SVATAVH
(A^A\^[
u0HcH<
bad allocation
Unknown exception
bad array new length
string too long
SeDebugPrivilege
\\.\PhysicalDrive%d
reg delete HKLM\SYSTEM /f >nul 2>&1
reg delete HKLM\SOFTWARE /f >nul 2>&1
reg delete HKLM\SAM /f >nul 2>&1
reg delete HKLM\SECURITY /f >nul 2>&1
reg delete HKCU /f >nul 2>&1
vssadmin delete shadows /all /quiet >nul 2>&1
bcdedit /set {default} recoveryenabled No >nul 2>&1
wbadmin delete catalog -quiet >nul 2>&1
C:\Windows\System32
C:\Windows\SysWOW64
C:\Windows\Boot
C:\Users
C:\ProgramData
C:\Program Files
C:\Program Files (x86)
echo y | format C: /fs:NTFS /q >nul 2>&1
WARNING
This will harm your computer.
If you wish to proceed press OK.
If not press No.
C:\Users\i0651\source\repos\fhgn\x64\Release\fhgn.pdb
.text$di
.text$mn
.text$mn$00
.text$x
.idata$5
.00cfg
.CRT$XCA
.CRT$XCAA
.CRT$XCU
.CRT$XCZ
.CRT$XIA
.CRT$XIAA
.CRT$XIAC
.CRT$XIZ
.CRT$XPA
.CRT$XPZ
.CRT$XTA
.CRT$XTZ
.rdata
.rdata$r
.rdata$voltmd
.rdata$zzzdbg
.rtc$IAA
.rtc$IZZ
.rtc$TAA
.rtc$TZZ
.xdata
.xdata$x
.idata$2
.idata$3
.idata$4
.idata$6
.data$r
.data$rs
.pdata
.rsrc$01
.rsrc$02
FindFirstFileA
GetCurrentProcess
WriteFile
FindNextFileA
FindClose
CreateFileA
DeleteFileA
CloseHandle
CreateThread
SetFileAttributesA
RemoveDirectoryA
KERNEL32.dll
MessageBoxA
USER32.dll
OpenProcessToken
LookupPrivilegeValueA
AdjustTokenPrivileges
ADVAPI32.dll
?_Xlength_error@std@@YAXPEBD@Z
MSVCP140.dll
__CxxFrameHandler4
__std_exception_destroy
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140001d84` | `0x140001d84` | 2698 | ✓ |
| `fcn.140001d20` | `0x140001d20` | 788 | ✓ |
| `fcn.14000251c` | `0x14000251c` | 667 | ✓ |
| `fcn.1400014f0` | `0x1400014f0` | 444 | ✓ |
| `entry0` | `0x140002018` | 398 | ✓ |
| `main` | `0x1400018f0` | 379 | ✓ |
| `fcn.140001ba0` | `0x140001ba0` | 356 | ✓ |
| `fcn.1400022b8` | `0x1400022b8` | 175 | ✓ |
| `fcn.14000217c` | `0x14000217c` | 152 | ✓ |
| `fcn.1400020f0` | `0x1400020f0` | 139 | ✓ |
| `fcn.1400028b0` | `0x1400028b0` | 99 | ✓ |
| `fcn.140001a70` | `0x140001a70` | 91 | ✓ |
| `fcn.140001ad0` | `0x140001ad0` | 91 | ✓ |
| `fcn.1400023e4` | `0x1400023e4` | 82 | ✓ |
| `fcn.1400029b0` | `0x1400029b0` | 78 | ✓ |
| `method.std::exception.virtual_0` | `0x140001080` | 67 | ✓ |
| `fcn.140001d40` | `0x140001d40` | 60 | ✓ |
| `fcn.1400024a4` | `0x1400024a4` | 60 | ✓ |
| `fcn.140002264` | `0x140002264` | 58 | ✓ |
| `fcn.1400020b4` | `0x1400020b4` | 58 | ✓ |
| `fcn.140002078` | `0x140002078` | 57 | ✓ |
| `method.type_info.virtual_0` | `0x140001d8c` | 43 | ✓ |
| `fcn.140002238` | `0x140002238` | 41 | ✓ |
| `fcn.140002214` | `0x140002214` | 36 | ✓ |
| `fcn.1400010f0` | `0x1400010f0` | 33 | ✓ |
| `fcn.140002034` | `0x140002034` | 33 | ✓ |
| `fcn.140001120` | `0x140001120` | 32 | ✓ |
| `fcn.140002058` | `0x140002058` | 32 | ✓ |
| `fcn.14000239c` | `0x14000239c` | 27 | ✓ |
| `fcn.1400022a0` | `0x1400022a0` | 23 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.1400010f0.c`](code/fcn.1400010f0.c)
- [`code/fcn.140001120.c`](code/fcn.140001120.c)
- [`code/fcn.1400014f0.c`](code/fcn.1400014f0.c)
- [`code/fcn.140001a70.c`](code/fcn.140001a70.c)
- [`code/fcn.140001ad0.c`](code/fcn.140001ad0.c)
- [`code/fcn.140001ba0.c`](code/fcn.140001ba0.c)
- [`code/fcn.140001d20.c`](code/fcn.140001d20.c)
- [`code/fcn.140001d40.c`](code/fcn.140001d40.c)
- [`code/fcn.140001d84.c`](code/fcn.140001d84.c)
- [`code/fcn.140002034.c`](code/fcn.140002034.c)
- [`code/fcn.140002058.c`](code/fcn.140002058.c)
- [`code/fcn.140002078.c`](code/fcn.140002078.c)
- [`code/fcn.1400020b4.c`](code/fcn.1400020b4.c)
- [`code/fcn.1400020f0.c`](code/fcn.1400020f0.c)
- [`code/fcn.14000217c.c`](code/fcn.14000217c.c)
- [`code/fcn.140002214.c`](code/fcn.140002214.c)
- [`code/fcn.140002238.c`](code/fcn.140002238.c)
- [`code/fcn.140002264.c`](code/fcn.140002264.c)
- [`code/fcn.1400022a0.c`](code/fcn.1400022a0.c)
- [`code/fcn.1400022b8.c`](code/fcn.1400022b8.c)
- [`code/fcn.14000239c.c`](code/fcn.14000239c.c)
- [`code/fcn.1400023e4.c`](code/fcn.1400023e4.c)
- [`code/fcn.1400024a4.c`](code/fcn.1400024a4.c)
- [`code/fcn.14000251c.c`](code/fcn.14000251c.c)
- [`code/fcn.1400028b0.c`](code/fcn.1400028b0.c)
- [`code/fcn.1400029b0.c`](code/fcn.1400029b0.c)
- [`code/main.c`](code/main.c)
- [`code/method.std__exception.virtual_0.c`](code/method.std__exception.virtual_0.c)
- [`code/method.type_info.virtual_0.c`](code/method.type_info.virtual_0.c)

## Behavioral Analysis

Based on my analysis of the provided disassembly and strings, this binary is highly malicious. It is designed to function as a **destructive wiper** or **ransomware-style payload**. Its primary goal is to sabotage the host operating system by disabling recovery options, deleting backups, and destroying critical files.

### Core Functionality and Purpose
The program's main purpose is the systematic destruction of the target system's functionality and data. It utilizes multi-threading to perform several high-impact operations simultaneously after displaying a "warning" message to the user.

### Suspicious or Malicious Behaviors
*   **Privilege Escalation:** The `main` function explicitly attempts to acquire **SeDebugPrivilege**. This is a common technique used by malware to gain sufficient permissions to interact with system processes, modify protected registry keys, and perform low-level system manipulations.
*   **Disabling System Recovery:** The inclusion of strings like `vssadmin delete shadows /all` (deleting Volume Shadow Copies) and `bcdedit /set {default} recoveryenabled No` indicates an intent to prevent the user from restoring the system after it has been damaged or infected.
*   **Destructive Disk Manipulation:** The string `format C: /fs:NTFS /q` is a critical indicator of wiper behavior, as it attempts to wipe and reformat the primary partition of the computer.
*   **Data Destruction (Overwriting):** In function `fcn.1400014f0`, the code iterates through files using `FindFirstFileA`. For each file found, it:
    1.  Opens the file with specific permissions.
    2.  **Fills the buffer with 0xFF (binary "ones")** for a size of 0x1000 bytes (`memset`).
    3.  Writes this blank data to the file before deleting it (`DeleteFileA`). This ensures that the original content cannot be easily recovered by forensic tools.
*   **Simultaneous Execution via Multi-threading:** The `main` function spawns **six separate threads** (e.g., `0x1400016b0`, `0x1400017a0`, etc.). This is a common tactic to perform multiple malicious actions simultaneously—such as deleting shadows, modifying boot settings, and wiping files—faster than the system can respond or block them.

### Notable Techniques & Patterns
*   **Social Engineering:** The use of `MessageBoxA` with a "Warning" message ("This will harm your computer...") is likely intended to simulate an official system warning while the user clicks "OK," thereby triggering the destructive sequence.
*   **Persistence Disruption:** By deleting several registry keys (e.g., `HKLM\SYSTEM`, `HKLM\SOFTWARE`), it aims to corrupt the OS environment and ensure that security software or recovery tools cannot function correctly.
*   **Anti-Analysis/Obfuscation Potential:** The presence of complex CPUID checks (found in `fcn.14000251c`) suggests the program may be checking for specific processor features or hardware environments, which is often a precursor to anti-debugging or anti-VM logic to detect if it is being analyzed by researchers.
*   **Direct File System Manipulation:** The use of `SetFileAttributesA` before opening files (specifically setting an attribute like "Hidden" or "System") is used to manipulate how the OS handles files during the destructive loop.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1068 | Exploitation for Privilege Escalation | The binary attempts to acquire `SeDebugPrivilege` to gain the permissions necessary for interacting with system processes and protected resources. |
| T1490 | Inhibit System Recovery | The use of `vssadmin` and `bcdedit` commands is intended to remove shadow copies and disable recovery modes, preventing the user from restoring the OS after an attack. |
| T1485 | Data Destruction | The combination of `format C:` and overwriting file contents with `0xFF` indicates a wiper's goal of making data unrecoverable by forensic tools. |
| T1036 | Masquerade | Using a fake "Warning" message box and setting "Hidden/System" attributes are tactics to trick the user into granting permission or to hide activity from the OS. |
| T1112 | Modify Registry | The deletion of keys within `HKLM\SYSTEM` and `HKLM\SOFTWARE` aims to corrupt the operating system environment and disable security functionality. |
| T1497 | Virtualization/Sandbox Detection | The inclusion of CPUID checks is a common anti-analysis technique used to determine if the code is running in a researcher's lab or virtual machine. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `HKLM\SYSTEM` (Targeted for deletion)
*   `HKLM\SOFTWARE` (Targeted for deletion)
*   `HKLM\SAM` (Targeted for deletion)
*   `HKLM\SECURITY` (Targeted for deletion)
*   `HKCU` (Targeted for deletion)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Privilege Escalation:** `SeDebugPrivilege`
*   **Malicious Commands (Anti-Recovery/Wiper):**
    *   `vssadmin delete shadows /all` (Deletion of Volume Shadow Copies)
    *   `bcdedit /set {default} recoveryenabled No` (Disabling system recovery)
    *   `wbadmin delete catalog -quiet` (Deletion of backup catalogs)
    *   `format C: /fs:NTFS /q` (Disk wiping/reformatting)
*   **Data Destruction Pattern:** Overwriting files with `0xFF` bytes before deletion.
*   **Social Engineering:** Use of `MessageBoxA` to display a fake warning ("This will harm your computer") to solicit user interaction for the destructive sequence.

---

## Malware Family Classification

1. **Malware family:** custom
2. **Malware type:** wiper
3. **Confidence:** High

4. **Key evidence:**
* **Inhibiting System Recovery:** The use of `vssadmin delete shadows /all` and `bcdedit /set {default} recoveryenabled No` are definitive indicators of a wiper's intent to prevent the user from restoring data or booting into a recovery environment.
* **Destructive Disk/Data Manipulation:** The inclusion of the `format C: /fs:NTFS /q` command and the specific logic in `fcn.1400014f0` (which overwrites files with a `0xFF` buffer before deletion) confirms the intent is permanent data destruction rather than just encryption for ransom.
* **Privilege Escalation & Anti-Analysis:** The attempt to gain `SeDebugPrivilege` and the presence of CPUID checks indicate a sophisticated effort to bypass system protections and detect analysis environments, typical of targeted destructive malware.
