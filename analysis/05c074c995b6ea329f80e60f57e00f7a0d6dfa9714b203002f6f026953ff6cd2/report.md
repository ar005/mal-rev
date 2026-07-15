# Threat Analysis Report

**Generated:** 2026-07-14 15:32 UTC
**Sample:** `05c074c995b6ea329f80e60f57e00f7a0d6dfa9714b203002f6f026953ff6cd2_05c074c995b6ea329f80e60f57e00f7a0d6dfa9714b203002f6f026953ff6cd2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05c074c995b6ea329f80e60f57e00f7a0d6dfa9714b203002f6f026953ff6cd2_05c074c995b6ea329f80e60f57e00f7a0d6dfa9714b203002f6f026953ff6cd2.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 86,732,190 bytes |
| MD5 | `fbf7ef6cc7b1c28d0577a15a2ef64eb1` |
| SHA1 | `d93cec15dd505855404c2ab7d202f1cfd4629f33` |
| SHA256 | `05c074c995b6ea329f80e60f57e00f7a0d6dfa9714b203002f6f026953ff6cd2` |
| Overall entropy | 8.0 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1339690570 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 22,528 | 6.459 | No |
| `.rdata` | 12,288 | 4.975 | No |
| `.data` | 3,072 | 2.587 | No |
| `.rsrc` | 28,160 | 5.82 | No |
| `.reloc` | 4,608 | 3.712 | No |

### Imports

**KERNEL32.dll**: `_lclose`, `GetModuleFileNameA`, `_lread`, `_llseek`, `_lopen`, `_lwrite`, `_lcreat`, `CreateDirectoryA`, `SetCurrentDirectoryA`, `lstrcatA`, `FreeLibrary`, `GetProcAddress`, `LoadLibraryA`, `GetDiskFreeSpaceA`, `GetFileAttributesA`
**USER32.dll**: `TranslateMessage`, `DispatchMessageA`, `PeekMessageA`, `wsprintfA`, `LoadCursorA`, `SetCursor`, `MessageBoxA`, `MsgWaitForMultipleObjects`
**ADVAPI32.dll**: `GetTokenInformation`, `OpenProcessToken`
**SHELL32.dll**: `ShellExecuteExA`

## Extracted Strings

Total strings found: **191479** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc
<Tt"<Wt
t"hPr@
t+9}t&9}
u&j^9
j
YQPVh
E9Xt
^SSSSS
t$<"u	3
< tK<	tG
j@j ^V
u,9Et'9
URPQQh
t"SS9] u
;t$,v-
kUQPXY]Y[
v	N+D$
PPPPPPPP
PPPPPPPP
Launcher Error
Could not find setup size
Could not find total size indicator
Could not find compression type indicator
Could not find data segment
Could not find multi-segment indicator
Unable to allocate memory buffer
Unable to open archive file
Failed to read setup engine
Unable to open setup file
Failed to alloc memory.
Failed to read Lua DLL
Unable to write to Lua file.
Unable to open Lua DLL file
Could not find Lua DLL file size
ConvertSidToStringSidA
Advapi32.dll
You must have at least 2MB of free space on your TEMP drive!
lua5.1.dll
irsetup.exe
Could not determine a temp directory name.  Try running setup.exe /T:<Path>
c:\temp
%s\irsetup.exe
%s%s_%d
_ir_sf_temp
Could not start the setup
"__IRSID:%s"
"__IRTSS:%I64u"
"__IRCT:%d"
"__IRAFN:%s"
__IRAOFF:%I64u
CorExitProcess
FlsFree
FlsSetValue
FlsGetValue
FlsAlloc
HH:mm:ss
dddd, MMMM dd, yyyy
MM/dd/yy
December
November
October
September
August
February
January
Saturday
Friday
Thursday
Wednesday
Tuesday
Monday
Sunday
GetProcessWindowStation
GetUserObjectInformationW
GetLastActivePopup
GetActiveWindow
MessageBoxW
 Complete Object Locator'
 Class Hierarchy Descriptor'
 Base Class Array'
 Base Class Descriptor at (
 Type Descriptor'
`local static thread guard'
`managed vector copy constructor iterator'
`vector vbase copy constructor iterator'
`vector copy constructor iterator'
`dynamic atexit destructor for '
`dynamic initializer for '
`eh vector vbase copy constructor iterator'
`eh vector copy constructor iterator'
`managed vector destructor iterator'
`managed vector constructor iterator'
`placement delete[] closure'
`placement delete closure'
`omni callsig'
 delete[]
 new[]
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004023e0` | `0x4023e0` | 6800 | ✓ |
| `fcn.00402320` | `0x402320` | 6455 | ✓ |
| `fcn.0040301d` | `0x40301d` | 1573 | ✓ |
| `fcn.00401b8c` | `0x401b8c` | 1006 | ✓ |
| `fcn.00405bcc` | `0x405bcc` | 887 | ✓ |
| `fcn.0040188b` | `0x40188b` | 769 | ✓ |
| `fcn.00401233` | `0x401233` | 667 | ✓ |
| `fcn.00404547` | `0x404547` | 581 | ✓ |
| `fcn.00405066` | `0x405066` | 489 | ✓ |
| `fcn.004060aa` | `0x4060aa` | 487 | ✓ |
| `fcn.004039b5` | `0x4039b5` | 431 | ✓ |
| `main` | `0x401000` | 419 | ✓ |
| `fcn.00402c44` | `0x402c44` | 419 | ✓ |
| `fcn.0040524f` | `0x40524f` | 410 | ✓ |
| `fcn.0040425b` | `0x40425b` | 410 | ✓ |
| `fcn.00404db4` | `0x404db4` | 400 | ✓ |
| `fcn.004032d0` | `0x4032d0` | 379 | ✓ |
| `entry0` | `0x4029e1` | 375 | ✓ |
| `fcn.0040563b` | `0x40563b` | 364 | ✓ |
| `fcn.004015e0` | `0x4015e0` | 359 | ✓ |
| `fcn.00404b10` | `0x404b10` | 331 | ✓ |
| `fcn.00403fd6` | `0x403fd6` | 330 | ✓ |
| `fcn.00402171` | `0x402171` | 320 | ✓ |
| `fcn.00402e14` | `0x402e14` | 297 | ✓ |
| `fcn.004014ce` | `0x4014ce` | 274 | ✓ |
| `fcn.00403c67` | `0x403c67` | 262 | ✓ |
| `fcn.00405fac` | `0x405fac` | 254 | ✓ |
| `fcn.004062d7` | `0x4062d7` | 231 | ✓ |
| `fcn.0040417f` | `0x40417f` | 220 | ✓ |
| `fcn.00401747` | `0x401747` | 218 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401233.c`](code/fcn.00401233.c)
- [`code/fcn.004014ce.c`](code/fcn.004014ce.c)
- [`code/fcn.004015e0.c`](code/fcn.004015e0.c)
- [`code/fcn.00401747.c`](code/fcn.00401747.c)
- [`code/fcn.0040188b.c`](code/fcn.0040188b.c)
- [`code/fcn.00401b8c.c`](code/fcn.00401b8c.c)
- [`code/fcn.00402171.c`](code/fcn.00402171.c)
- [`code/fcn.00402320.c`](code/fcn.00402320.c)
- [`code/fcn.004023e0.c`](code/fcn.004023e0.c)
- [`code/fcn.00402c44.c`](code/fcn.00402c44.c)
- [`code/fcn.00402e14.c`](code/fcn.00402e14.c)
- [`code/fcn.0040301d.c`](code/fcn.0040301d.c)
- [`code/fcn.004032d0.c`](code/fcn.004032d0.c)
- [`code/fcn.004039b5.c`](code/fcn.004039b5.c)
- [`code/fcn.00403c67.c`](code/fcn.00403c67.c)
- [`code/fcn.00403fd6.c`](code/fcn.00403fd6.c)
- [`code/fcn.0040417f.c`](code/fcn.0040417f.c)
- [`code/fcn.0040425b.c`](code/fcn.0040425b.c)
- [`code/fcn.00404547.c`](code/fcn.00404547.c)
- [`code/fcn.00404b10.c`](code/fcn.00404b10.c)
- [`code/fcn.00404db4.c`](code/fcn.00404db4.c)
- [`code/fcn.00405066.c`](code/fcn.00405066.c)
- [`code/fcn.0040524f.c`](code/fcn.0040524f.c)
- [`code/fcn.0040563b.c`](code/fcn.0040563b.c)
- [`code/fcn.00405bcc.c`](code/fcn.00405bcc.c)
- [`code/fcn.00405fac.c`](code/fcn.00405fac.c)
- [`code/fcn.004060aa.c`](code/fcn.004060aa.c)
- [`code/fcn.004062d7.c`](code/fcn.004062d7.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

Based on my analysis of the provided disassembly and decompiled code, here is a summary of the program's behavior:

### Core Functionality
The binary acts as an **installer or "dropper"** for another application. Its primary purpose is to extract embedded files from its own data section and execute them on the target system. Specifically, it targets two main components: `irsetup.exe` and `lua5.1.dll`.

### Suspicious & Malicious Behaviors
The code exhibits several behaviors common in malware (specifically droppers and loaders):

*   **Payload Extraction (Dropping):** The function `fcn.00401233` acts as a resource extractor. It scans a data segment for specific indicators such as "multi-segment indicator," "compression type indicator," and "setup size." This is a classic method used by malware to unpack hidden components from an initial executable.
*   **File Creation & System Manipulation:** The function `fcn.0040188b` performs several operations related to file system manipulation:
    *   It generates filenames like `_ir_sf_temp` and appends numerical suffixes (e.g., `_ir_sf_temp_1`).
    *   It checks for available disk space (requiring at least 2MB) before proceeding with the installation.
    *   It creates temporary directories and moves files into them to prepare them for execution.
*   **Execution of Dropped Components:** The program uses `ShellExecuteExA` to launch the extracted components (`irsetup.exe`). It includes logic to wait for the launched process (using `MsgWaitForMultipleObjects`) and capture its exit code, ensuring the "setup" completes before the parent continues or exits.
*   **Anti-Analysis/Anti-Debugging:** The inclusion of `IsDebuggerPresent` in the startup and initialization routines is a common anti-analysis technique used to detect if the code is being run in a debugger, commonly used by malware authors to hide their behavior from analysts.

### Notable Techniques & Patterns
*   **Robust Error Handling for Extractions:** The decompiler shows extensive error messaging (e.g., "Could not find data segment," "Unable to write to Lua file") during the unpacking phase. This suggests a sophisticated installer or a packer designed to ensure all components are correctly "unpacked" before the payload runs.
*   **Automatic Path Normalization:** The function `fcn.00401747` ensures that paths are properly formatted (e.g., adding backslashes) and creates missing directories in the path automatically, ensuring the dropper succeeds regardless of where it is launched.
*   **Encryption/Obfuscation Hint:** In `fcn.004014ce`, there is a loop that performs an XOR operation (`^ 7`) on data during the reading process. This suggests that some components (specifically the "setup engine") are weakly encrypted or obfuscated within the binary and are decrypted in memory/on disk just before use.
*   **Standard Library Usage:** The code makes heavy use of `Shell32.dll` for execution and `Advapi32.dll` for privilege/token checks, which are standard but frequently leveraged by malware to perform privileged actions or execute commands stealthily.

### Summary for Incident Response
This binary is a **loader**. It is designed to hide its primary payload (the "setup" software) within its own body. When executed, it performs a series of extraction steps, decodes/writes files to the local disk (likely in the `%TEMP%` or a similar directory), and then launches those components. The presence of **IsDebuggerPresent** confirms that the author intended to hinder analysis of this specific stage of the attack.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1105** | Ingress Tool Transfer | The binary acts as a "dropper" by extracting embedded components (irsetup.exe, lua5.1.dll) from its own data segment to the local system. |
| **T1027** | Obfuscated Files or Information | The use of a bitwise XOR operation (XOR 7) indicates that the payload is intentionally encoded/obfuscated to hide its true content during static analysis. |
| **T1497** | Virtualization/Sandbox Evasion | The inclusion of `IsDebuggerPresent` is a classic anti-analysis technique used to detect and hinder the efforts of security researchers or automated sandboxes. |
| **T1204** | User Execution | The use of `ShellExecuteExA` to launch the extracted components follows a typical installer/loader pattern for executing dropped payloads. |
| **T1083** | File and Directory Discovery | The logic used to scan data segments, verify disk space, and automatically construct paths indicates systematic preparation of the environment for payload deployment. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `irsetup.exe` (Payload filename)
*   `lua5.1.dll` (Dropped library file)
*   `c:\temp` (Staging directory)
*   `_ir_sf_temp` (Naming convention for dropped files, e.g., `_ir_sf_temp_1`)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **XOR Key:** `^ 7` (Identified in `fcn.004014ce` as the key used to decrypt the "setup engine" during extraction).
*   **Anti-Analysis Technique:** `IsDebuggerPresent` (Used to detect and evade debugger analysis).
*   **Internal Identifiers/Logging Strings:** 
    *   `__IRSID`
    *   `__IRTSS`
    *   `__IRCT`
    *   `__IRAFFN`
    *   `__IRAOFF`
*   **Behavioral Pattern:** The application utilizes a specific "Data Segment Extraction" routine to unpack components (specifically `irsetup.exe` and `lua5.1.dll`) from its own binary body before execution via `ShellExecuteExA`.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
* **Payload Extraction & Decryption:** The binary functions as a dedicated dropper/loader by extracting embedded files (`irsetup.exe` and `lua5.1.dll`) from its data segment, applying an XOR 7 decryption to the "setup engine" before executing it via `ShellExecuteExA`.
* **Anti-Analysis Tactics:** The explicit use of `IsDebuggerPresent` and the deliberate obfuscation of payload components indicate a clear intent to evade analysis by security researchers or automated sandboxes.
* **Automated Staging Behavior:** The inclusion of sophisticated file system manipulation (checking for disk space, automatically creating directories, and ensuring path normalization) is indicative of a persistent loader designed to successfully deploy further stages of an attack.
