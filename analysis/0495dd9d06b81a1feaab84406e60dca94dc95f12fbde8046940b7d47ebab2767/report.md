# Threat Analysis Report

**Generated:** 2026-07-11 20:04 UTC
**Sample:** `0495dd9d06b81a1feaab84406e60dca94dc95f12fbde8046940b7d47ebab2767_0495dd9d06b81a1feaab84406e60dca94dc95f12fbde8046940b7d47ebab2767.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0495dd9d06b81a1feaab84406e60dca94dc95f12fbde8046940b7d47ebab2767_0495dd9d06b81a1feaab84406e60dca94dc95f12fbde8046940b7d47ebab2767.exe` |
| File type | PE32+ executable for MS Windows 5.02 (console), x86-64 (stripped to external PDB), 10 sections |
| Size | 1,542,144 bytes |
| MD5 | `815c566646b43f4e2eb951ff60f36532` |
| SHA1 | `2b048ccd70054488c149c772eb3e8af68f487077` |
| SHA256 | `0495dd9d06b81a1feaab84406e60dca94dc95f12fbde8046940b7d47ebab2767` |
| Overall entropy | 7.188 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1777964369 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 10,752 | 5.822 | No |
| `.data` | 512 | 0.653 | No |
| `.rdata` | 1,523,712 | 7.2 | ⚠️ Yes |
| `.eh_fram` | 0 | 0.0 | No |
| `.pdata` | 1,024 | 3.178 | No |
| `.xdata` | 1,024 | 3.393 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 3,584 | 3.917 | No |
| `.tls` | 0 | 0.0 | No |
| `.reloc` | 512 | 1.337 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `CreateFileA`, `CreateProcessA`, `DeleteCriticalSection`, `EnterCriticalSection`, `FreeLibrary`, `GetLastError`, `GetModuleHandleA`, `GetProcAddress`, `GetTempPathA`, `InitializeCriticalSection`, `LeaveCriticalSection`, `LoadLibraryA`, `MultiByteToWideChar`, `SetUnhandledExceptionFilter`
**api-ms-win-crt-environment-l1-1-0.dll**: `__p__environ`
**api-ms-win-crt-heap-l1-1-0.dll**: `_set_new_mode`, `calloc`, `free`, `malloc`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-private-l1-1-0.dll**: `__C_specific_handler`, `memcpy`
**api-ms-win-crt-runtime-l1-1-0.dll**: `__p___argc`, `__p___argv`, `_cexit`, `_configure_narrow_argv`, `_crt_atexit`, `_exit`, `_initialize_narrow_environment`, `_set_app_type`, `_initterm`, `_initterm_e`, `_set_invalid_parameter_handler`, `abort`, `exit`, `signal`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__acrt_iob_func`, `__p__commode`, `__p__fmode`, `__stdio_common_vfprintf`, `__stdio_common_vsprintf`, `fclose`, `fopen`, `fwrite`
**api-ms-win-crt-string-l1-1-0.dll**: `strcat`, `strcpy`, `strlen`, `strncmp`, `tolower`, `toupper`
**api-ms-win-crt-time-l1-1-0.dll**: `_time64`
**api-ms-win-crt-utility-l1-1-0.dll**: `rand`, `srand`
**SHELL32.dll**: `SHGetFolderPathA`
**SHLWAPI.dll**: `PathCombineA`

## Extracted Strings

Total strings found: **3677** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.eh_fram
.pdata
@.xdata
.idata
.reloc
f=MZt

9t$Dt	
ATUWVSH
 [^_]A\
AVAUATUWVS
[^_]A\A]A^A_
AUATUWVSH
[^_]A\A]
 =CCG u
libgcc_s_dw2-1.dll
__register_frame_info
__deregister_frame_info
Start-Process -FilePath
-ArgumentList
$%s='%s';%s "$env:TEMP\%s" %s "$env:TEMP\%s" ;$%s='%s'
start /min powershell -w h -e
@echo off
%s %s
igiltbjnnaircgi.exe
vvoxovllh
bkjsmfewekvbyyt
qlarccenmewpctxetddokuxp.bat
"%s" "%s"
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
GMBBBBB
GMBBBBB
RfEsqq
BBBBBBBBBB
BBBBBBBBBBBBBBBBBB
MBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBB
rpqqq6q
BBBBBBBB
rpqqq>
fIqqqyV
Mfaqqq
MBBBBBBBBBBBBBBB
BBBBBB
rpqqqe
BBBBBBBBBB
yOnqqq
SyOrqqq
yOrqqq
@fCdqq
BBBBBBBBBBBB
gMfqqBBBBBBBBBBBBBB
vf
qqqq
vfdpqqJ
BBBBBBBBBB
yOvqqq
yOvqqq
fM~qqJ
bf1uqq
fMwqqJ
f8cqqJ
ff{zqqI
rpqqqI
Bfq`qq
Wqqf>}qq
BBBBBB
jfx|qqq
bf0jqq
rpqqqf
MBBBBBBB
MBBBBBBBBBB
MBBBBBBBBB
qqhBBBBBBB
MBBBBBB
f.pqqJ
MBBBBBBBBBBBB
MBBBBBBB
gyrqq/
Mg&sqq
f%qqqI
f=qqqq
fUpqqq
f^pqqJ
f_EqqMBBBBB/
rpqqqf
BBBBBB
GMBBBBB
rpqqqf
MBBBBBB/
MBBBBBBBBB
rpqqqf
f:Cqq
rpqqqf
~]D]E]@
f^wqqq
t]@]Ax
ze,pq
MqqMBBBBB
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140002372` | `0x140002372` | 894 | ✓ |
| `fcn.140001075` | `0x140001075` | 803 | ✓ |
| `fcn.140001f75` | `0x140001f75` | 734 | ✓ |
| `fcn.1400036c0` | `0x1400036c0` | 536 | ✓ |
| `fcn.14000192e` | `0x14000192e` | 447 | ✓ |
| `fcn.14000149c` | `0x14000149c` | 319 | ✓ |
| `fcn.140001398` | `0x140001398` | 260 | ✓ |
| `fcn.140002cc1` | `0x140002cc1` | 252 | ✓ |
| `fcn.140001710` | `0x140001710` | 228 | ✓ |
| `fcn.140002253` | `0x140002253` | 216 | ✓ |
| `fcn.140001aed` | `0x140001aed` | 212 | ✓ |
| `fcn.14000187d` | `0x14000187d` | 177 | ✓ |
| `fcn.1400026f0` | `0x1400026f0` | 164 | ✓ |
| `fcn.140002c22` | `0x140002c22` | 159 | ✓ |
| `entry1` | `0x140001ce0` | 156 | ✓ |
| `fcn.140002e4c` | `0x140002e4c` | 153 | ✓ |
| `fcn.140002dd0` | `0x140002dd0` | 124 | ✓ |
| `fcn.140003440` | `0x140003440` | 121 | ✓ |
| `fcn.140001c2f` | `0x140001c2f` | 120 | ✓ |
| `fcn.140003310` | `0x140003310` | 107 | ✓ |
| `fcn.140001f10` | `0x140001f10` | 101 | ✓ |
| `fcn.140003380` | `0x140003380` | 90 | ✓ |
| `fcn.140002fab` | `0x140002fab` | 80 | ✓ |
| `fcn.140002ffb` | `0x140002ffb` | 80 | ✓ |
| `fcn.1400017f4` | `0x1400017f4` | 73 | ✓ |
| `fcn.14000232b` | `0x14000232b` | 71 | ✓ |
| `fcn.1400032c0` | `0x1400032c0` | 65 | ✓ |
| `fcn.140003400` | `0x140003400` | 64 | ✓ |
| `fcn.14000183d` | `0x14000183d` | 64 | ✓ |
| `entry2` | `0x140001d99` | 62 | ✓ |

### Decompiled Code Files

- [`code/entry1.c`](code/entry1.c)
- [`code/entry2.c`](code/entry2.c)
- [`code/fcn.140001075.c`](code/fcn.140001075.c)
- [`code/fcn.140001398.c`](code/fcn.140001398.c)
- [`code/fcn.14000149c.c`](code/fcn.14000149c.c)
- [`code/fcn.140001710.c`](code/fcn.140001710.c)
- [`code/fcn.1400017f4.c`](code/fcn.1400017f4.c)
- [`code/fcn.14000183d.c`](code/fcn.14000183d.c)
- [`code/fcn.14000187d.c`](code/fcn.14000187d.c)
- [`code/fcn.14000192e.c`](code/fcn.14000192e.c)
- [`code/fcn.140001aed.c`](code/fcn.140001aed.c)
- [`code/fcn.140001c2f.c`](code/fcn.140001c2f.c)
- [`code/fcn.140001f10.c`](code/fcn.140001f10.c)
- [`code/fcn.140001f75.c`](code/fcn.140001f75.c)
- [`code/fcn.140002253.c`](code/fcn.140002253.c)
- [`code/fcn.14000232b.c`](code/fcn.14000232b.c)
- [`code/fcn.140002372.c`](code/fcn.140002372.c)
- [`code/fcn.1400026f0.c`](code/fcn.1400026f0.c)
- [`code/fcn.140002c22.c`](code/fcn.140002c22.c)
- [`code/fcn.140002cc1.c`](code/fcn.140002cc1.c)
- [`code/fcn.140002dd0.c`](code/fcn.140002dd0.c)
- [`code/fcn.140002e4c.c`](code/fcn.140002e4c.c)
- [`code/fcn.140002fab.c`](code/fcn.140002fab.c)
- [`code/fcn.140002ffb.c`](code/fcn.140002ffb.c)
- [`code/fcn.1400032c0.c`](code/fcn.1400032c0.c)
- [`code/fcn.140003310.c`](code/fcn.140003310.c)
- [`code/fcn.140003380.c`](code/fcn.140003380.c)
- [`code/fcn.140003400.c`](code/fcn.140003400.c)
- [`code/fcn.140003440.c`](code/fcn.140003440.c)
- [`code/fcn.1400036c0.c`](code/fcn.1400036c0.c)

## Behavioral Analysis

### **Analysis Summary**
The binary is a **downloader and dropper** designed to deploy additional malicious payloads onto the system. It utilizes several common malware techniques, including payload unpacking/decoding (Base64), automated file creation in temporary directories, and execution of dropped files with randomized names to evade signature-based detection.

---

### **Core Functionality & Purpose**
The primary purpose of this binary is to act as a "Stage 1" dropper. It extracts hidden components from its own resources (or perhaps from subsequent network communication not shown in this specific snippet) and writes them to the disk before executing them.

- **Payload Deployment:** The code explicitly constructs paths for several files (e.g., `igiltbjnnaircgi.exe`, `vvoxovllh`) and writes them to the system's `%TEMP%` directory using `CreateFileA` and `WriteFile`.
- **Execution of Dropped Files:** After writing these files, it calls `CreateProcessA` to launch them.

---

### **Suspicious & Malicious Behaviors**

*   **Dropping Executables in Temp Folders:** 
    The code uses `GetTempPathA` and appends randomized-looking strings to create filenames like `igiltbjnnaircgi.exe`. The use of `%TEMP%` is a standard technique for malware because it usually provides write permissions to the current user.
*   **Command Execution via PowerShell:** 
    The extracted strings include:
    `start /min powershell -w h -e` 
    - `-w h` (WindowStyle Hidden) hides the console from the user.
    - `-e` (EncodedCommand) allows the execution of a Base64 encoded string, which is often used to hide malicious commands (like downloading more files or executing shellcode).
*   **Memory Manipulation:** 
    Function `fcn.140001f75` contains logic involving `VirtualProtect`. This suggests that the malware checks and modifies memory permissions of specific regions. This is common in "unpackers" where a piece of code is decrypted/decompressed in memory, and its permissions are changed to "Execute" before being run.
*   **Antis-Analysis / Obfuscation:**
    The extensive use of Base64 decoding (`fcn.14000187d`) and the presence of "junk" data or encrypted strings (the large blocks of `B`s and random characters in the string table) indicate an attempt to hinder static analysis.

---

### **Notable Techniques & Patterns**

*   **Randomized Filenames:** The use of non-human-readable strings (e.g., `vvoxovllh`, `bkjsmfewekvbyyt`) for file names suggests a desire to evade detection by looking for specific filenames.
*   **Stage Progression:** The presence of a `.bat` file string (`qlarccenmewpctxetddokuxp.bat`) and the PowerShell commands suggest that this is part of a multi-stage infection chain where the original binary acts as the gateway to further malware.
*   **Environment Interaction:** The use of `MultiByteToWideChar` indicates a professional level of development intended to ensure compatibility with different system locales/languages when handling file paths or strings.
*   **Code Injection Preparation:** The heavy focus on memory scanning and protection changes (`fcn.140001f75`) suggests that even if the payload is not written to disk, it might be designed to "hollow" a process or inject code directly into memory.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Execution System | The use of Base64 encoding, junk data, and encrypted strings is intended to hinder static analysis and hide malicious functionality. |
| **T1059.001** | Command and Scripting Interpreter: PowerShell | The malware utilizes PowerShell with hidden windows (`-w h`) and encoded commands (`-e`) to execute instructions stealthily. |
| **T1036** | Masquerading | Randomized file names (e.g., `igiltbjnnaircgi.exe`) are used to evade signature-based detection and hide the purpose of the files. |
| **T1055** | Process Injection | The use of `VirtualProtect` to modify memory permissions suggests preparation for unpacking, decompressing, or injecting code into a process. |
| **T1106** | Unified Process Injection | (Optional/Contextual) The behavior involving `VirtualProtect` and subsequent execution indicates an intent to execute code in a protected memory space. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `igiltbjnnaircgi.exe` (Dropped executable)
*   `vvoxovllh` (Randomized dropped file)
*   `bkjsmfewekvbyyt` (Randomized dropped file)
*   `qlarccenmewpctxetddokuxp.bat` (Batch file used in infection chain)
*   `%TEMP%` (Target directory for payload dropping)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **PowerShell Command Pattern:** `start /min powershell -w h -e` 
    *   *Note: Indicates execution of a hidden window (`-w h`) with an encoded command (`-e`).*
*   **Potential Dropper Behavior:** Use of the `%TEMP%` environment variable to stage and execute secondary payloads.
*   **Obfuscation Technique:** Usage of high-entropy/randomized strings for filenames (e.g., `vvoxovllh`) to evade signature-based detection.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper / loader
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-Stage Deployment:** The binary functions as a "Stage 1" dropper, utilizing randomized file naming and the `%TEMP%` directory to hide and execute secondary payloads (e.g., `igiltbjnnaircgi.exe`).
*   **Evasive Execution Techniques:** It employs heavily obfuscated PowerShell commands (`-w h -e`) to run encoded scripts in hidden windows, which is a classic method for bypassing security controls during the initial infection phase.
*   **Memory Manipulation & Obfuscation:** The use of `VirtualProtect` indicates preparation for unpacking or process injection, while extensive Base64 decoding and "junk" data are used to hinder static analysis.
