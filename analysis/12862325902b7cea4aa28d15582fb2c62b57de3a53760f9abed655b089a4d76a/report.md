# Threat Analysis Report

**Generated:** 2026-08-31 15:33 UTC
**Sample:** `12862325902b7cea4aa28d15582fb2c62b57de3a53760f9abed655b089a4d76a_12862325902b7cea4aa28d15582fb2c62b57de3a53760f9abed655b089a4d76a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12862325902b7cea4aa28d15582fb2c62b57de3a53760f9abed655b089a4d76a_12862325902b7cea4aa28d15582fb2c62b57de3a53760f9abed655b089a4d76a.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64, 6 sections |
| Size | 6,128,401 bytes |
| MD5 | `7cb9fc5502ccc5e26749998524f354e5` |
| SHA1 | `ca45ed630842e1c49dc3b19a387e657c7ed30a51` |
| SHA256 | `12862325902b7cea4aa28d15582fb2c62b57de3a53760f9abed655b089a4d76a` |
| Overall entropy | 6.363 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1533043810 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,112 | 6.21 | No |
| `.rdata` | 15,360 | 4.685 | No |
| `.data` | 4,096 | 2.227 | No |
| `.pdata` | 1,536 | 4.252 | No |
| `.rsrc` | 28,672 | 5.876 | No |
| `.reloc` | 1,024 | 3.546 | No |

### Imports

**KERNEL32.dll**: `LoadLibraryA`, `lstrcpyA`, `lstrcatA`, `lstrlenA`, `GetSystemDirectoryA`, `GetProcAddress`, `GetModuleHandleA`, `_lclose`, `GetModuleFileNameA`, `_lread`, `_llseek`, `_lopen`, `_lwrite`, `_lcreat`, `CreateDirectoryA`
**USER32.dll**: `TranslateMessage`, `DispatchMessageA`, `PeekMessageA`, `wsprintfA`, `LoadCursorA`, `SetCursor`, `MessageBoxA`, `MsgWaitForMultipleObjects`
**ADVAPI32.dll**: `GetTokenInformation`, `OpenProcessToken`
**SHELL32.dll**: `ShellExecuteExA`

## Extracted Strings

Total strings found: **16499** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
x UATAUAVAWH
<Tt'<Wt
A_A^A]A\]
@8t$Hu

H;L$8uu
H;L$8t
UWATAUAWH
A_A]A\_]
WATAUAVAWH
@A_A^A]A\_
fffffff
fffffff
WATAUAVAWH
0A_A^A]A\_
ATAUAVH
 A^A]A\
LcA<E3
WATAUAVAWH
A_A^A]A\_
t$ WATAUH
x ATAUAVH
< tG<	tC
 A^A]A\
Hct$@H
s\HcL$HH
ATAUAVH
fD9t$b
A^A]A\
UVWATAUH
^D9d$ 
D$&8\$&t-8X
@A]A\_^]
@SUVWATAUAVH
PA^A]A\_^][
	H;5c
KXH;Wc
K`H;Mc
@UATAUAVAWH
@88tH
!t$(H!t$ A
A_A^A]A\]
@UATAUAVAWH
A_A^A]A\]
Launcher Error
api-ms-win-downlevel-advapi32-l2-1-0.dll
Secur32.dll
PROPSYS.dll
ntmarta.dll
SetDllDirectoryA
SetDefaultDllDirectories
kernel32.dll
Could not find data segment
Could not find setup size
Could not find total size indicator
Could not find compression type indicator
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
m_szTempLaunchPath
"__IRSID:%s"
"__IRTSS:%I64u"
"__IRCT:%d"
"__IRAFN:%s"
__IRAOFF:%I64u
CorExitProcess
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140002980` | `0x140002980` | 6830 | ✓ |
| `fcn.140002514` | `0x140002514` | 3501 | ✓ |
| `fcn.140003798` | `0x140003798` | 1801 | ✓ |
| `section..text` | `0x140001000` | 1131 | ✓ |
| `fcn.140006724` | `0x140006724` | 1006 | ✓ |
| `fcn.140001f78` | `0x140001f78` | 973 | ✓ |
| `fcn.140002a10` | `0x140002a10` | 820 | ✓ |
| `fcn.140001ca4` | `0x140001ca4` | 722 | ✓ |
| `fcn.140004d4c` | `0x140004d4c` | 722 | ✓ |
| `fcn.14000150c` | `0x14000150c` | 716 | ✓ |
| `fcn.140006c8c` | `0x140006c8c` | 714 | ✓ |
| `fcn.140005a90` | `0x140005a90` | 629 | ✓ |
| `fcn.140004040` | `0x140004040` | 605 | ✓ |
| `fcn.1400032f4` | `0x1400032f4` | 562 | ✓ |
| `fcn.140006098` | `0x140006098` | 520 | ✓ |
| `fcn.140005754` | `0x140005754` | 496 | ✓ |
| `fcn.140005d08` | `0x140005d08` | 478 | ✓ |
| `fcn.140004614` | `0x140004614` | 464 | ✓ |
| `fcn.140004990` | `0x140004990` | 463 | ✓ |
| `entry0` | `0x14000301c` | 430 | ✓ |
| `fcn.140002678` | `0x140002678` | 399 | ✓ |
| `fcn.14000547c` | `0x14000547c` | 377 | ✓ |
| `fcn.1400018f4` | `0x1400018f4` | 374 | ✓ |
| `fcn.140006ff0` | `0x140006ff0` | 350 | ✓ |
| `fcn.140003540` | `0x140003540` | 331 | ✓ |
| `fcn.140004860` | `0x140004860` | 304 | ✓ |
| `fcn.1400017d8` | `0x1400017d8` | 283 | ✓ |
| `fcn.140003b84` | `0x140003b84` | 266 | ✓ |
| `fcn.140006b80` | `0x140006b80` | 266 | ✓ |
| `fcn.140001b68` | `0x140001b68` | 265 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.14000150c.c`](code/fcn.14000150c.c)
- [`code/fcn.1400017d8.c`](code/fcn.1400017d8.c)
- [`code/fcn.1400018f4.c`](code/fcn.1400018f4.c)
- [`code/fcn.140001b68.c`](code/fcn.140001b68.c)
- [`code/fcn.140001ca4.c`](code/fcn.140001ca4.c)
- [`code/fcn.140001f78.c`](code/fcn.140001f78.c)
- [`code/fcn.140002514.c`](code/fcn.140002514.c)
- [`code/fcn.140002678.c`](code/fcn.140002678.c)
- [`code/fcn.140002980.c`](code/fcn.140002980.c)
- [`code/fcn.140002a10.c`](code/fcn.140002a10.c)
- [`code/fcn.1400032f4.c`](code/fcn.1400032f4.c)
- [`code/fcn.140003540.c`](code/fcn.140003540.c)
- [`code/fcn.140003798.c`](code/fcn.140003798.c)
- [`code/fcn.140003b84.c`](code/fcn.140003b84.c)
- [`code/fcn.140004040.c`](code/fcn.140004040.c)
- [`code/fcn.140004614.c`](code/fcn.140004614.c)
- [`code/fcn.140004860.c`](code/fcn.140004860.c)
- [`code/fcn.140004990.c`](code/fcn.140004990.c)
- [`code/fcn.140004d4c.c`](code/fcn.140004d4c.c)
- [`code/fcn.14000547c.c`](code/fcn.14000547c.c)
- [`code/fcn.140005754.c`](code/fcn.140005754.c)
- [`code/fcn.140005a90.c`](code/fcn.140005a90.c)
- [`code/fcn.140005d08.c`](code/fcn.140005d08.c)
- [`code/fcn.140006098.c`](code/fcn.140006098.c)
- [`code/fcn.140006724.c`](code/fcn.140006724.c)
- [`code/fcn.140006b80.c`](code/fcn.140006b80.c)
- [`code/fcn.140006c8c.c`](code/fcn.140006c8c.c)
- [`code/fcn.140006ff0.c`](code/fcn.140006ff0.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This analysis covers a binary that functions primarily as a **multi-stage dropper/launcher**. The code is designed to prepare an environment, extract and decrypt hidden components (specifically a Lua-based engine), and execute them in a separate process while attempting to evade detection or analysis.

### Core Functionality
The primary purpose of this binary is to act as a "loader" for a larger application (referred to in strings as "irsetup"). It does not perform the final malicious actions itself; instead, it performs the following steps:
1.  **Environment Preparation:** It checks for sufficient disk space on the temporary drive and creates a workspace in the `%TEMP%` directory.
2.  **Resource Extraction:** It treats its own internal data (or an accompanying archive) as a packed container, reading specific "segments," checking compression types, and extracting files like `irsetup.exe` and `lua5.1.dll`.
3.  **Decryption/Deobfuscation:** It performs simple XOR-based decryption on extracted components to prepare them for execution.
4.  **Execution (Dropping):** It uses `ShellExecuteA` to launch the "real" payload in a separate process, while it remains active as a parent process to monitor the child's lifecycle via `MsgWaitForMultipleObjects`.

### Suspicious and Malicious Behaviors
*   **Anti-Analysis/Anti-Debugging:**
    *   The function `fcn.140002980` explicitly uses `IsDebuggerPresent()`. If a debugger is detected, or if the application encounters certain unhandled exceptions (often used to detect "sandboxes" or "debuggers"), it calls `TerminateProcess`.
    *   It employs custom **Unhandled Exception Filters** (`SetUnhandledExceptionFilter`), a common technique to intercept and bypass debugger-induced crashes or to monitor for debugger activity.
*   **Payload Dropping & Staging:**
    *   The program creates a folder in the System Temp directory (e.g., `...\_ir_sf_temp`). This is a classic tactic used by malware to hide its "working" files from the initial execution path.
    *   It dynamically extracts and moves components into this hidden directory before launching them.
*   **Dynamic Library Loading & Path Manipulation:**
    *   The code manually constructs paths for system DLLs (e.g., `kernel32.dll`, `advapi32.dll`) and calls `SetDllDirectory` / `SetDefaultDllDirectories`. This is often used to ensure the loader can find its internal components or to bypass standard OS security checks for dynamic links.
*   **User Interaction/Environment Checks:**
    *   The code queries `GetActiveWindow`, `GetLastActivePopup`, and `GetProcessWindowStation` (in `fcn.140006098`). These are often used as **anti-analysis checks** to determine if the software is being "clicked" by a human or if it's running in a windowless, automated sandbox environment.

### Notable Techniques and Patterns
*   **Multi-Stage Execution:** By splitting the logic between a "Launcher" (this binary) and an "Engine" (`lua5.1.dll` + `irsetup.exe`), the author ensures that even if the launcher is analyzed, it doesn't contain the full malicious payload.
*   **Embedded Resource Management:** The presence of logic to find "multi-segment indicators" and "compression types" suggests that this binary is a **packer/unpacker**. It treats its own file structure as an archive.
*   **Specific Use of Lua:** The specific extraction and use of `lua5.1.dll` strongly indicates that the actual malicious payload is likely scripted via Lua. This allows the threat actor to update their "malware" by simply changing a script file without recompiling the primary executables.
*   **Fallback Logic:** In `fcn.140001ca4`, if it fails to determine a specific temporary directory name, it falls back to `c:\temp`. This indicates an attempt to be "robust" across various different Windows environments.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors described in your analysis to the relevant MITRE ATT&K techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of XOR-based decryption on extracted components is a classic method to hide malicious functionality from static analysis. |
| **T1106** | File Decompression | The binary's logic to identify "compression types" and extract segments indicates it functions as a packer/unpacker for hidden payloads. |
| **T1497** | Virtualized Environment | The use of `IsDebuggerPresent` and checks for active windows or popups are standard techniques to detect if the malware is running in an automated sandbox or debugger. |
| **T1059** | Command and Scripting Interpreter | The integration of a Lua-based engine indicates that the actual malicious logic is executed via a scripting interpreter to facilitate easy updates and evasion. |
| **T1218** | System Binary Proxy Execution | The use of `ShellExecuteA` to launch the "real" payload in a separate process allows the loader to hand off execution while remaining as a watchdog/parent. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `c:\temp` (Hardcoded fallback directory)
*   `_ir_sf_temp` (Specific subdirectory used for staging dropped files)
*   `%s\irsetup.exe` (Dynamic path pattern for the primary payload)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified in strings)*

**Other artifacts**
*   **File Names:** 
    *   `irsetup.exe` (Primary malicious binary/loader)
    *   `lua5.1.dll` (Scripting engine used for payload execution)
*   **C2 / Persistence Patterns:** 
    *   Use of **Lua scripting** to host the actual malicious logic (enables easy updates to functionality without changing the primary loader).
    *   **Multi-segment unpacking** logic (indicates a custom packer or wrapper).
*   **Anti-Analysis Techniques:**
    *   `IsDebuggerPresent()` check.
    *   Custom **Unhandled Exception Filters** used to evade sandboxes.
    *   Environment checks via `GetActiveWindow`, `GetLastActivePopup`, and `GetProcessWindowStation`.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family:** Unknown
2. **Malware type:** Loader / Dropper
3. **Confidence:** High

**Key evidence:**
*   **Multi-stage Execution & Decryption:** The binary acts as a wrapper that performs XOR decryption and extraction of hidden components (`irsetup.exe` and `lua5.1.dll`) to hide the primary malicious payload from static analysis.
*   **Scripting Engine Integration:** The use of `lua5.1.dll` is a significant indicator of modularity; it allows the threat actor to update the malware's behavior via scripts without re-compiling or changing the core loader logic.
*   **Sophisticated Anti-Analysis:** The sample employs several layers of defense, including `IsDebuggerPresent()` checks, custom exception filters to evade sandboxes, and environmental queries (e.g., `GetActiveWindow`) to detect if it is being executed in a controlled environment rather than by a human user.
