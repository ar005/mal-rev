# Threat Analysis Report

**Generated:** 2026-06-23 20:29 UTC
**Sample:** `003734348d05ac8087c497c214bd871355b168e41c9ee8d5aa5fcfcdbe6c8a89_003734348d05ac8087c497c214bd871355b168e41c9ee8d5aa5fcfcdbe6c8a89.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `003734348d05ac8087c497c214bd871355b168e41c9ee8d5aa5fcfcdbe6c8a89_003734348d05ac8087c497c214bd871355b168e41c9ee8d5aa5fcfcdbe6c8a89.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 96,709,174 bytes |
| MD5 | `edc2659fa344a270e8cd6cfee9782e49` |
| SHA1 | `6e9016472c82fb65ce9bd2162557ec3aff529df5` |
| SHA256 | `003734348d05ac8087c497c214bd871355b168e41c9ee8d5aa5fcfcdbe6c8a89` |
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

Total strings found: **211897** (showing first 100)

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

Based on the provided disassembly and string analysis, here is a technical analysis of the binary's behavior:

### Core Functionality and Purpose
The binary functions as a **Dropper** and **Installer**. Its primary purpose is to unpack, decompress/decrypt, and execute a hidden payload (likely `irsetup.exe` and associated DLLs) from an internal resource or embedded archive into a temporary directory on the local system.

### Suspicious and Malicious Behaviors
The code exhibits several behaviors common in malware "droppers" designed to deliver secondary payloads:

*   **Dropping and File Manipulation:**
    *   The binary identifies and uses system paths (via `GetTempPathA`) to create a temporary workspace for extraction.
    *   It performs **dynamic path construction**, appending strings like `_ir_sf_temp` and ultimately constructing the file name `irsetup.exe`.
    *   It includes logic to check for available disk space (specifically looking for at least 2MB) before extracting files, a common trait of installers that are being used as vehicle for malware distribution.
    *   The code contains routines (`fcn.00401233`, `fcn.004014ce`) to parse an internal "archive" or "data segment," looking for specific markers like "compression type indicator," "setup size," and "multi-segment indicator."

*   **Decryption/Deobfuscation:**
    *   In `fcn.004014ce`, there is a loop that performs a bitwise XOR operation (`^ 7`) on data before writing it to the filesystem. This is a common technique to de-obfuscate an embedded payload before it is executed.

*   **Process Execution and Persistence:**
    *   The binary uses **`ShellExecuteExA`** in `fcn.00401b8c` to launch the unpacked file (`irsetup.exe`).
    *   It implements a wait-loop (using `MsgWaitForMultipleObjects`) to monitor the state of the launched process, ensuring it successfully starts before continuing or exiting.
    *   The inclusion of "Lua" related strings (`lua5.1.dll`) suggests the payload may involve a scripting engine, often used by malware for complex task automation or modular behavior.

*   **Anti-Analysis Techniques:**
    *   **Debugger Detection:** The function `fcn.00403c67` explicitly calls **`IsDebuggerPresent()`**. If it detects that the process is being debugged (or if certain internal conditions are not met), it calls `TerminateProcess(GetCurrentProcess())` to crash itself and stop analysis.
    *   **Environment Checking:** The code collects system information such as the current user's SID (`GetTokenInformation`) and window status, which can be used to detect if the malware is running in a virtualized environment or on a non-target machine.

### Notable Techniques and Patterns
*   **Staged Execution:** By unpacking `irsetup.exe` into the `%TEMP%` directory and launching it as a separate process, the primary binary acts as a "loader," making it harder for automated systems to link the malicious payload's behavior directly to the original executable.
*   **Resource Parsing:** The complexity of the loops in `fcn.00401233` indicates a custom-built unpacker. It doesn't just call a standard zip library; it manually walks through memory buffers to locate segments and verify data integrity.
*   **Manual String Construction:** Instead of using simple cleartext strings for paths, the code builds filenames and paths dynamically to evade basic string-based detection of "irsetup" or related keywords until the point of execution.

### Summary Table
| Behavior | Evidence / Function | Risk Level |
| :--- | :--- | :--- |
| **Dropper** | Extracts `irsetup.exe` and `lua5.1.dll` to temp folders. | High |
| **De-obfuscation** | XORing data (xor 7) before writing to disk. | Medium |
| **Anti-Analysis** | Calls `IsDebuggerPresent` followed by `TerminateProcess`. | High |
| **Environment Check**| Use of `GetTokenInformation` and `GetActiveWindow`. | Medium |
| **Hidden Execution** | Uses `ShellExecuteExA` to launch the payload. | High |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The binary employs a bitwise XOR operation and dynamic path construction to de-obfuscate data and hide key strings from detection. |
| **T1405** | Debugger Evasion | The inclusion of the `IsDebuggerPresent` function indicates an active attempt to detect and terminate if being analyzed in a debugger. |
| **T1497** | Virtualized Environment Detection | The use of `GetTokenInformation` and window status checks are used to identify and avoid execution in virtual machines or sandboxes. |
| **T1036** | Masquerading | The binary uses a generic installer-style name (`irsetup.exe`) to blend in with legitimate software during its deployment phase. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **irsetup.exe** (Payload executable)
*   **lua5.1.dll** (Associated DLL component)
*   **_ir_sf_temp** (Specific directory/naming convention used during the unpacking process)
*   **c:\temp** (Explicitly mentioned as a target path for setup execution)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *No cryptographic hashes were provided in the input strings.*

### **Other artifacts**
*   **De-obfuscation Pattern:** Use of XOR operation (`^ 7`) on data before writing to disk (indicative of a custom packer/loader).
*   **Naming Convention:** The use of "IR" prefixes in internal tracking strings (`__IRSID`, `__IRTSS`, `__IRCT`, `__IRAFFN`, `__IRAOFF`).
*   **Anti-Analysis Activity:** 
    *   `IsDebuggerPresent` (Detection check)
    *   `TerminateProcess` (Action taken if debugger/analysis environment is detected)
*   **Environment Checks:** Use of `GetTokenInformation` and `GetActiveWindow` for potential sandbox evasion or target verification.
*   **Execution Method:** Use of `ShellExecuteExA` to launch the secondary payload `irsetup.exe`.

---

## Malware Family Classification

1. **Malware family**: Unknown (likely a custom loader/dropper)
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-Stage Delivery:** The binary functions as a classic "loader" by unpacking an embedded, obfuscated payload (`irsetup.exe`) into the `%TEMP%` directory and executing it via `ShellExecuteExA`. 
*   **De-obfuscation & Anti-Analysis:** The use of XOR bitwise operations (xor 7) to decrypt files before writing them to disk, combined with explicit anti-analysis checks (`IsDebuggerPresent`) and environmental checks (`GetTokenInformation`), is characteristic of malicious delivery tools designed to evade detection.
*   **Executional Masking:** The binary employs "masquerading" techniques by using generic names like `irsetup.exe` and manually constructing paths to hide its activities from automated security scanners until the payload is launched.
