# Threat Analysis Report

**Generated:** 2026-06-28 06:14 UTC
**Sample:** `0270c76c010e9b66c19d2d06cbff2b95a7b558296afe8e1172cc001f4f3aa3ee_0270c76c010e9b66c19d2d06cbff2b95a7b558296afe8e1172cc001f4f3aa3ee.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0270c76c010e9b66c19d2d06cbff2b95a7b558296afe8e1172cc001f4f3aa3ee_0270c76c010e9b66c19d2d06cbff2b95a7b558296afe8e1172cc001f4f3aa3ee.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 4 sections |
| Size | 144,896 bytes |
| MD5 | `21be80c278110af8d5a3fb443dacbca8` |
| SHA1 | `da1b8f3ba074f19ec949147fcc69ed7d2a76ed13` |
| SHA256 | `0270c76c010e9b66c19d2d06cbff2b95a7b558296afe8e1172cc001f4f3aa3ee` |
| Overall entropy | 7.626 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1776557794 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 24,576 | 6.547 | No |
| `.rdata` | 9,216 | 4.694 | No |
| `.data` | 106,496 | 7.902 | ⚠️ Yes |
| `.reloc` | 3,584 | 4.162 | No |

### Imports

**KERNEL32.dll**: `GetModuleHandleA`, `GetProcAddress`, `GetCommandLineA`, `IsProcessorFeaturePresent`, `GetLastError`, `SetLastError`, `InterlockedIncrement`, `InterlockedDecrement`, `GetCurrentThreadId`, `EncodePointer`, `DecodePointer`, `ExitProcess`, `GetModuleHandleExW`, `MultiByteToWideChar`, `GetStdHandle`

## Extracted Strings

Total strings found: **634** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.reloc
SUVWhHq@
Genuu_
ineIuV
nteluM3
~pjCXf
YYhDq@
<v5hB@B
j@j _W
< t8<	t4
u,9Et'9
tf= ?B
u9Mu&3
URPQQh
u&j[9
PP9E u
x$;5d\B
;t$,v-
kUQPXY]Y[
t$jXP
x&;5d\B
~';_t|%3
u;_tr.
xy;5d\B
v	N+D$
kernel32.dll
VirtualAlloc
LoadLibraryA
GetProcAddress
CorExitProcess
GetCurrentPackageId
Sunday
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
January
February
August
September
October
November
December
MM/dd/yy
dddd, MMMM dd, yyyy
HH:mm:ss
MessageBoxW
GetActiveWindow
GetLastActivePopup
GetUserObjectInformationW
GetProcessWindowStation
 !"#$%&'()*+,-./0123456789:;<=>?@abcdefghijklmnopqrstuvwxyz[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`ABCDEFGHIJKLMNOPQRSTUVWXYZ{|}~
 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
GetModuleHandleA
GetProcAddress
GetCommandLineA
IsProcessorFeaturePresent
GetLastError
SetLastError
InterlockedIncrement
InterlockedDecrement
GetCurrentThreadId
EncodePointer
DecodePointer
ExitProcess
GetModuleHandleExW
MultiByteToWideChar
GetStdHandle
WriteFile
GetModuleFileNameW
GetProcessHeap
GetFileType
InitializeCriticalSectionAndSpinCount
DeleteCriticalSection
InitOnceExecuteOnce
GetStartupInfoW
GetModuleFileNameA
QueryPerformanceCounter
GetSystemTimeAsFileTime
GetTickCount64
GetEnvironmentStringsW
FreeEnvironmentStringsW
WideCharToMultiByte
UnhandledExceptionFilter
SetUnhandledExceptionFilter
FlsAlloc
FlsGetValue
FlsSetValue
FlsFree
GetCurrentProcess
TerminateProcess
GetModuleHandleW
EnterCriticalSection
LeaveCriticalSection
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004048b0` | `0x4048b0` | 4840 | ✓ |
| `fcn.00401f7c` | `0x401f7c` | 4358 | ✓ |
| `fcn.00405fe2` | `0x405fe2` | 2122 | ✓ |
| `fcn.00401200` | `0x401200` | 1604 | ✓ |
| `fcn.00405022` | `0x405022` | 896 | ✓ |
| `fcn.00403b6c` | `0x403b6c` | 501 | ✓ |
| `fcn.004053a2` | `0x4053a2` | 489 | ✓ |
| `fcn.004046ba` | `0x4046ba` | 482 | ✓ |
| `section..text` | `0x401000` | 481 | ✓ |
| `fcn.004022e4` | `0x4022e4` | 443 | ✓ |
| `fcn.00404290` | `0x404290` | 437 | ✓ |
| `fcn.004039be` | `0x4039be` | 430 | ✓ |
| `fcn.0040378b` | `0x40378b` | 398 | ✓ |
| `fcn.0040286d` | `0x40286d` | 380 | ✓ |
| `fcn.00401b41` | `0x401b41` | 347 | ✓ |
| `fcn.0040331a` | `0x40331a` | 346 | ✓ |
| `entry0` | `0x401844` | 334 | ✓ |
| `fcn.00402144` | `0x402144` | 303 | ✓ |
| `fcn.00403d61` | `0x403d61` | 291 | ✓ |
| `fcn.00404ebd` | `0x404ebd` | 252 | ✓ |
| `fcn.004059d7` | `0x4059d7` | 249 | ✓ |
| `fcn.00405dfc` | `0x405dfc` | 247 | ✓ |
| `fcn.00406b9d` | `0x406b9d` | 243 | ✓ |
| `fcn.00405ef3` | `0x405ef3` | 239 | ✓ |
| `fcn.004055ed` | `0x4055ed` | 236 | ✓ |
| `fcn.004029e9` | `0x4029e9` | 225 | ✓ |
| `fcn.00406ce9` | `0x406ce9` | 215 | ✓ |
| `fcn.004058b6` | `0x4058b6` | 213 | ✓ |
| `fcn.004045fc` | `0x4045fc` | 190 | ✓ |
| `fcn.00403fd0` | `0x403fd0` | 186 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401200.c`](code/fcn.00401200.c)
- [`code/fcn.00401b41.c`](code/fcn.00401b41.c)
- [`code/fcn.00401f7c.c`](code/fcn.00401f7c.c)
- [`code/fcn.00402144.c`](code/fcn.00402144.c)
- [`code/fcn.004022e4.c`](code/fcn.004022e4.c)
- [`code/fcn.0040286d.c`](code/fcn.0040286d.c)
- [`code/fcn.004029e9.c`](code/fcn.004029e9.c)
- [`code/fcn.0040331a.c`](code/fcn.0040331a.c)
- [`code/fcn.0040378b.c`](code/fcn.0040378b.c)
- [`code/fcn.004039be.c`](code/fcn.004039be.c)
- [`code/fcn.00403b6c.c`](code/fcn.00403b6c.c)
- [`code/fcn.00403d61.c`](code/fcn.00403d61.c)
- [`code/fcn.00403fd0.c`](code/fcn.00403fd0.c)
- [`code/fcn.00404290.c`](code/fcn.00404290.c)
- [`code/fcn.004045fc.c`](code/fcn.004045fc.c)
- [`code/fcn.004046ba.c`](code/fcn.004046ba.c)
- [`code/fcn.004048b0.c`](code/fcn.004048b0.c)
- [`code/fcn.00404ebd.c`](code/fcn.00404ebd.c)
- [`code/fcn.00405022.c`](code/fcn.00405022.c)
- [`code/fcn.004053a2.c`](code/fcn.004053a2.c)
- [`code/fcn.004055ed.c`](code/fcn.004055ed.c)
- [`code/fcn.004058b6.c`](code/fcn.004058b6.c)
- [`code/fcn.004059d7.c`](code/fcn.004059d7.c)
- [`code/fcn.00405dfc.c`](code/fcn.00405dfc.c)
- [`code/fcn.00405ef3.c`](code/fcn.00405ef3.c)
- [`code/fcn.00405fe2.c`](code/fcn.00405fe2.c)
- [`code/fcn.00406b9d.c`](code/fcn.00406b9d.c)
- [`code/fcn.00406ce9.c`](code/fcn.00406ce9.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

### Executive Summary
The analyzed binary is a multi-functional malicious sample, likely categorized as **Spyware** or an **Information Stealer**. The code contains significant infrastructure for anti-analysis techniques, information gathering from the user's desktop environment, and internal obfuscation/unpacking routines.

---

### Core Functionality & Purpose
The primary purpose of this code appears to be monitoring the user's interaction with their system. It implements several layers of data processing:
*   **Environment Fingerprinting:** The binary checks for specific hardware features (`IsProcessorFeaturePresent`) and environment details (Console modes, Code Pages).
*   **Data Processing & Translation:** A significant portion of the code is dedicated to complex string conversions (e.g., `MultiByteToWideChar`, `WriteFile` wrappers) and buffer management. This is often used to prepare stolen data for transmission or local logging.
*   **System Interaction:** The inclusion of logic for capturing active windows suggests it targets information currently in use by the user.

### Suspicious & Malicious Behaviors
The following behaviors are indicative of malicious intent:

*   **Information Gathering (Spyware):** 
    *   Function `fcn.004046ba` explicitly imports and uses `GetActiveWindow`, `GetLastActivePopup`, and `GetUserObjectInformationW`. These functions are commonly used to identify which applications the user is currently interacting with, potentially for stealing credentials from login fields or tracking active windows.
*   **Anti-Analysis & Anti-Debugging:** 
    *   The code explicitly calls **`IsDebuggerPresent`**. It branches its logic based on whether it detects a debugger, a common tactic to hide malicious behavior during analysis.
    *   Function `fcn.00403fd0` accesses the thread information block (via `unaff_FS_OFFSET`), which is a technique used to detect the presence of debuggers or specific analysis tools by checking for artifacts in memory.
*   **Persistence & File Manipulation:** 
    *   The code utilizes `WriteFile`, `GetModuleFileNameW`, and `GetProcessHeap`. The combination suggests the binary may be preparing to write stolen data to a file (a "drop" or local log) or move/modify system files for persistence.
*   **Execution in Memory (Unpacking):** 
    *   The `.text` section shows logic involving **`VirtualAlloc`**, `GetProcAddress`, and `LoadLibraryA`. This pattern is typical of a "packer" or "loader," where the primary malicious payload is decrypted/decompressed into memory at runtime to evade static detection.

### Notable Techniques & Patterns
*   **Obfuscated Data Blobs:** The extracted strings contain a massive, repetitive block of text starting with `Security_Key_99Global`. This indicates an encrypted or XOR-encoded data structure (likely a configuration file, an embedded payload, or internal tables) that is processed during the initialization phase.
*   **Custom Wrapper Functions:** Instead of calling standard Win32 APIs directly throughout the code, it uses several "wrapper" functions (e.g., `fcn.00405fe2`, `fcn.004053a2`). This is a common technique to hide the true nature of API calls from automated scanners and complicates static analysis.
*   **Dynamic API Resolution:** The code uses `GetProcAddress` for several high-risk functions (like those in `user32.dll`), ensuring that the Import Address Table (IAT) remains "clean" or minimal, which helps evade basic heuristic detection.
*   **Complexity as Obfuscation:** The highly repetitive and complex loops in functions like `fcn.00401200` and `fcn.00405fe2` are designed to waste the analyst's time during manual code review, a common tactic used by advanced malware authors.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtualization/Sandbox Evasion | The inclusion of `IsDebuggerPresent` and environmental checks like `IsProcessorFeaturePresent` are used to detect analysis tools or virtualized environments. |
| T1056 | System Information Discovery | The use of `GetActiveWindow` and `GetLastActivePopup` allows the malware to identify what applications the user is currently interacting with. |
| T1055 | Process Injection | The use of `VirtualAlloc`, `LoadLibraryA`, and `GetProcAddress` indicates a packer/loader mechanism used to run payload code in memory to evade static detection. |
| T1106 | Native API | The implementation of custom wrapper functions and the use of `GetProcAddress` for dynamic resolution are used to hide actual API calls from automated scanners. |
| T1083 | File and Directory Discovery | The combination of `WriteFile` and `GetModuleFileNameW` suggests the binary is preparing to stage stolen data or modify files on the local system. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.*

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Unique Configuration Strings:** 
    *   `Security_Key_99Global` (and various mangled/obfuscated iterations such as `Surity_Ke`, `SecUri,y_Kay`, and `bal_Security_Key_99Global_Security_`). This indicates a specific configuration block or decryption key used by the malware.
*   **Malicious Function Offsets (Internal logic markers):**
    *   `fcn.004046ba`: Identified as the primary routine for information gathering (Spyware activity) using `GetActiveWindow` and `GetLastActivePopup`.
    *   `fcn.00403fd0`: Identified as the anti-analysis/anti-debugging routine.
    *   `fcn.00405fe2` / `fcn.004053a2`: Identified as custom wrapper functions used to obfuscate standard Win32 API calls.
*   **Behavioral Patterns:**
    *   **Packer/Loader Behavior:** The use of `VirtualAlloc`, `GetProcAddress`, and `LoadLibraryA` in the `.text` section indicates a multi-stage payload or unpacker routine.
    *   **Anti-Analysis Logic:** Explicit calls to `IsDebuggerPresent` and manual checks of the thread information block (`unaff_FS_OFFSET`).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: infostealer
3. **Confidence**: High

**Key evidence**:
*   **Information Gathering/Spyware Functionality:** The sample explicitly utilizes `GetActiveWindow` and `GetLastActivePopup` to monitor user interaction with specific applications, a primary behavior of info-stealers looking for credentials or sensitive data in active windows.
*   **Advanced Evasion Techniques:** The code implements multiple layers of anti-analysis (e.g., `IsDebuggerPresent`, manual thread information block checks) and obfuscation tactics (custom wrapper functions and dynamic API resolution via `GetProcAddress`) to bypass security software and hide its true intent.
*   **Loader/Packer Characteristics:** The presence of `VirtualAlloc` and `LoadLibraryA` in the `.text` section, combined with large encrypted data blobs, indicates a multi-stage execution where the primary malicious payload is decrypted or unpacked into memory at runtime to evade static detection.
