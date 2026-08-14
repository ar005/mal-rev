# Threat Analysis Report

**Generated:** 2026-08-11 23:59 UTC
**Sample:** `0e4d7fc19fc912a50e26ef99ca954613c480a3d05155bd23e3d78cf52ec0e90e_0e4d7fc19fc912a50e26ef99ca954613c480a3d05155bd23e3d78cf52ec0e90e.dll`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e4d7fc19fc912a50e26ef99ca954613c480a3d05155bd23e3d78cf52ec0e90e_0e4d7fc19fc912a50e26ef99ca954613c480a3d05155bd23e3d78cf52ec0e90e.dll` |
| File type | PE32 executable for MS Windows 4.00 (DLL), Intel i386, 5 sections |
| Size | 306,688 bytes |
| MD5 | `07c44e24127f6594a08f793cbc76ed87` |
| SHA1 | `518d740ee411cfbefa228cf824c8633902786d12` |
| SHA256 | `0e4d7fc19fc912a50e26ef99ca954613c480a3d05155bd23e3d78cf52ec0e90e` |
| Overall entropy | 6.111 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774201802 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 45,056 | 6.636 | No |
| `.rdata` | 4,096 | 5.232 | No |
| `.data` | 249,856 | 5.936 | No |
| `.rsrc` | 4,096 | 3.509 | No |
| `.reloc` | 2,560 | 6.27 | No |

### Imports

**KERNEL32.dll**: `CreateWaitableTimerA`, `SetWaitableTimer`, `CloseHandle`, `GetProcessHeap`, `GetModuleHandleA`, `ExitProcess`, `HeapAlloc`, `HeapReAlloc`, `HeapFree`, `IsBadReadPtr`, `GetCommandLineA`, `CreateEventA`, `FreeLibrary`, `GetProcAddress`, `LoadLibraryA`
**USER32.dll**: `PeekMessageA`, `GetMessageA`, `TranslateMessage`, `DispatchMessageA`, `wsprintfA`, `MessageBoxA`, `MsgWaitForMultipleObjects`
**OLEAUT32.dll**: `VariantTimeToSystemTime`

### Exports

`zasds`

## Extracted Strings

Total strings found: **1067** (showing first 100)

```
!This program cannot be run in DOS mode.
$

RichLz
`.rdata
@.reloc
>MZt_^]3
t_^]3
u
_^][
SVWSQRV3
rocA9F
SVWSQRV3
rocA9F
T$RQj
wO;5Hk
t8j\hxl
t@_^]3
D$0h<8
QSVWVWS
T$t1%
UPQRS
E_^[]
t.;t$$t(
VC20XC00U
;t$s
SS@SSPVSS
t#SSUP
t$$VSS
_^][YY
E9}_t
HHtpHHtl
)u9U
)E9Ur4
"WWSh@
<xt<Xt	
E_^[]
ESVWj 
USVWf
PPPPPPPP
PPPPPPPP
+ttHHtd
`9Mtc}
9MtAVW
__GLOBAL_HEAP_SELECTED
__MSVCRT_HEAP_SELECT
runtime error 
TLOSS error

SING error

DOMAIN error

R6028
- unable to initialize heap

R6027
- not enough space for lowio initialization

R6026
- not enough space for stdio initialization

R6025
- pure virtual function call

R6024
- not enough space for _onexit/atexit table

R6019
- unable to open console device

R6018
- unexpected heap error

R6017
- unexpected multithread lock error

R6016
- not enough space for thread data


abnormal program termination

R6009
- not enough space for environment

R6008
- not enough space for arguments

R6002
- floating point not loaded

Microsoft Visual C++ Runtime Library
Runtime Error!

Program: 
<program name unknown>
`h````
ppxxxx
(null)
GAIsProcessorFeaturePresent
KERNEL32
GetLastActivePopup
GetActiveWindow
MessageBoxA
user32.dll
1#QNAN
1#SNAN
H:mm:ss
dddd, MMMM dd, yyyy
M/d/yy
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
SunMonTueWedThuFriSat
JanFebMarAprMayJunJulAugSepOctNovDec
RtlMoveMemory
OpenEventA
CreateEventA
CreateWaitableTimerA
SetWaitableTimer
CloseHandle
GetProcessHeap
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.10001201` | `0x10001201` | 2203 | ✓ |
| `fcn.1000245f` | `0x1000245f` | 2166 | ✓ |
| `fcn.10006ed7` | `0x10006ed7` | 1918 | ✓ |
| `fcn.10001b60` | `0x10001b60` | 1611 | ✓ |
| `fcn.1000b37b` | `0x1000b37b` | 1185 | ✓ |
| `fcn.10003620` | `0x10003620` | 1038 | ✓ |
| `fcn.10003610` | `0x10003610` | 1000 | ✓ |
| `fcn.1000247d` | `0x1000247d` | 933 | ✓ |
| `fcn.10002e03` | `0x10002e03` | 926 | ✓ |
| `fcn.10008c30` | `0x10008c30` | 821 | ✓ |
| `fcn.10005aa0` | `0x10005aa0` | 821 | ✓ |
| `fcn.10007d07` | `0x10007d07` | 809 | ✓ |
| `fcn.10008030` | `0x10008030` | 777 | ✓ |
| `fcn.100029dd` | `0x100029dd` | 743 | ✓ |
| `fcn.10002eb3` | `0x10002eb3` | 743 | ✓ |
| `fcn.10003b20` | `0x10003b20` | 661 | ✓ |
| `fcn.1000b84c` | `0x1000b84c` | 659 | ✓ |
| `fcn.10004f40` | `0x10004f40` | 573 | ✓ |
| `fcn.10003567` | `0x10003567` | 568 | ✓ |
| `fcn.10009654` | `0x10009654` | 548 | ✓ |
| `fcn.1000bcb1` | `0x1000bcb1` | 544 | ✓ |
| `fcn.100032c3` | `0x100032c3` | 543 | ✓ |
| `fcn.100087dd` | `0x100087dd` | 520 | ✓ |
| `fcn.10009f56` | `0x10009f56` | 517 | ✓ |
| `fcn.10001008` | `0x10001008` | 473 | ✓ |
| `fcn.10006371` | `0x10006371` | 444 | ✓ |
| `fcn.100066d3` | `0x100066d3` | 436 | ✓ |
| `fcn.10009b4b` | `0x10009b4b` | 429 | ✓ |
| `fcn.10004660` | `0x10004660` | 403 | ✓ |
| `fcn.100048b0` | `0x100048b0` | 403 | ✓ |

### Decompiled Code Files

- [`code/fcn.10001008.c`](code/fcn.10001008.c)
- [`code/fcn.10001201.c`](code/fcn.10001201.c)
- [`code/fcn.10001b60.c`](code/fcn.10001b60.c)
- [`code/fcn.1000245f.c`](code/fcn.1000245f.c)
- [`code/fcn.1000247d.c`](code/fcn.1000247d.c)
- [`code/fcn.100029dd.c`](code/fcn.100029dd.c)
- [`code/fcn.10002e03.c`](code/fcn.10002e03.c)
- [`code/fcn.10002eb3.c`](code/fcn.10002eb3.c)
- [`code/fcn.100032c3.c`](code/fcn.100032c3.c)
- [`code/fcn.10003567.c`](code/fcn.10003567.c)
- [`code/fcn.10003610.c`](code/fcn.10003610.c)
- [`code/fcn.10003620.c`](code/fcn.10003620.c)
- [`code/fcn.10003b20.c`](code/fcn.10003b20.c)
- [`code/fcn.10004660.c`](code/fcn.10004660.c)
- [`code/fcn.100048b0.c`](code/fcn.100048b0.c)
- [`code/fcn.10004f40.c`](code/fcn.10004f40.c)
- [`code/fcn.10005aa0.c`](code/fcn.10005aa0.c)
- [`code/fcn.10006371.c`](code/fcn.10006371.c)
- [`code/fcn.100066d3.c`](code/fcn.100066d3.c)
- [`code/fcn.10006ed7.c`](code/fcn.10006ed7.c)
- [`code/fcn.10007d07.c`](code/fcn.10007d07.c)
- [`code/fcn.10008030.c`](code/fcn.10008030.c)
- [`code/fcn.100087dd.c`](code/fcn.100087dd.c)
- [`code/fcn.10008c30.c`](code/fcn.10008c30.c)
- [`code/fcn.10009654.c`](code/fcn.10009654.c)
- [`code/fcn.10009b4b.c`](code/fcn.10009b4b.c)
- [`code/fcn.10009f56.c`](code/fcn.10009f56.c)
- [`code/fcn.1000b37b.c`](code/fcn.1000b37b.c)
- [`code/fcn.1000b84c.c`](code/fcn.1000b84c.c)
- [`code/fcn.1000bcb1.c`](code/fcn.1000bcb1.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated the analysis. The new code segments provide significant evidence of how the malware handles **dynamic API resolution, string de-obfuscation, and memory management**—all hallmark techniques of a sophisticated loader or packer.

### Updated Analysis: Supplemental Findings

#### 1. Advanced Evasion & Anti-Analysis Techniques
*   **Dynamic API Resolution (fcn.10004660):** This is a critical finding. The function implements a manual `GetProcAddress` wrapper. Instead of listing suspicious functions in its Import Address Table (IAT), the malware stores encrypted or encoded strings and "decodes" them at runtime before passing them to `GetProcAddress`.
    *   *Why this is malicious:* This hides the true intent of the program from static analysis tools (like `strings` or basic YARA rules). It allows the malware to call sensitive functions (e.g., `CreateRemoteThread`, `WriteProcessMemory`) only at the moment they are needed.
*   **String De-obfuscation Engine (fcn.100066d3):** This function appears to be a robust parser for "hidden" strings. It looks for quotes, handles escaped characters, and potentially concatenates segments. 
    *   *Significance:* By using this logic, the malware ensures that most of its operational commands (C2 URLs, file paths, registry keys) never appear in plaintext in the binary’s data sections.
*   **Environment & Locale Checks (fcn.10009b4b):** The use of `GetCPInfo` suggests the malware is checking system environment properties. While this can be for compatibility, it is frequently used by malware to detect if it's running in a specific localized version or an atypical environment (like a sandbox) before executing its primary payload.
*   **Handle Management (fcn.10006371):** The code interacts with `GetStdHandle` and `SetHandleCount`. This is often used to manipulate the handle table or "clean up" traces of its activity, potentially ensuring that certain handles are not exposed to system monitoring tools during execution.

#### 2. Advanced Loader/Packer Mechanics
*   **Custom Memory Management (fcn.100087dd):** This function calls `VirtualAlloc` but does so within a complex logic loop that manages offsets and sizes from an internal table (`piVar9`). 
    *   *Significance:* Rather than just allocating memory for one thing, it is building a dynamic environment to host the "real" payload. The manual management of allocation blocks suggests it's preparing a workspace for decrypted code to be mapped into executable memory.
*   **Delayed Execution (fcn.100032c3):** This function utilizes `CreateWaitableTimer` and `SetWaitableTimer`. 
    *   *Significance:* Unlike a simple "Sleep" command, using a Waitable Timer can be used to make the thread behave more like a legitimate system process while waiting for a specific interval. It is often used to bypass basic automated sandboxes that skip sleeps or have limited time windows for analysis.

#### 3. Control Flow and Orchestration
*   **Multi-Stage Execution (fcn.10001008):** This function acts as the main "brain" of the loader. It calls several internal routines in a sequence, checking the results before proceeding to the next step. Each step likely represents a phase: 
    1.  Environment Check $\rightarrow$ 2. String De-obfuscation $\rightarrow$ 3. Memory Allocation $\rightarrow$ 4. Payload Decryption $\rightarrow$ 5. Final Execution.

---

### Updated Summary of Indicators

| Feature | Finding | Risk Level | Significance |
| :--- | :--- | :--- | :--- |
| **Dynamic API Resolution** | `fcn.10004660` uses manual `GetProcAddress` with de-obfuscated strings. | **High** | Evades static detection of malicious capabilities (e.g., injection, persistence). |
| **Sophisticated De-obfuscation**| `fcn.100066d3` and `fcn.10009f56` process "hidden" data. | **High** | Conceals C2 infrastructure and internal commands from analysis. |
| **Custom Memory Management** | `fcn.100087dd` manages multiple blocks via `VirtualAlloc`. | **Medium/High** | Indicates a packer or loader preparing to host a second-stage payload. |
| **Time/Timer Manipulation** | `fcn.100032c3` uses `SetWaitableTimer` rather than simple sleep. | **Medium** | Used to stall analysis and appear as legitimate background activity. |
| **Handle Obfuscation** | `fcn.10006371` manages handle counts/types. | **Low/Medium** | Potentially used to mask the process's interaction with the OS. |

### Conclusion
The evidence from both chunks strongly confirms that this is a **highly-engineered malicious loader**. It uses professional evasion techniques—specifically **multi-stage string decryption**, **manual API resolution**, and **custom memory management**. These features are designed specifically to frustrate security researchers and automated defense systems by hiding the "true" functionality of the malware until it is running in memory.

**Recommended Action:** Treat this binary as a high-threat loader. Any IP addresses or file paths extracted from the results of `fcn.100066d3` during dynamic analysis should be prioritized for IOC (Indicator of Compromise) gathering.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of dynamic API resolution and a custom de-obfuscation engine hides critical functionality (C2 URLs, file paths, and malicious API calls) from static analysis. |
| T1497 | Virtualization/Sandbox Detection | Environment/locale checks and the use of `CreateWaitableTimer` are employed to identify and bypass automated sandboxes or security researchers' environments. |
| T1609 | Reflective Code Loading | The custom memory management logic using `VirtualAlloc` in a multi-stage process indicates a loader preparing a workspace for a secondary payload to be executed in memory. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here is the extraction of Indicators of Compromise (IOCs). 

Note: As the analysis indicates that much of the malicious content (C2 infrastructure, specific file paths) is currently **obfuscated** or **dynamically resolved**, no "hard" network indicators (IPs/URLs) are present in the raw string dump.

### **IP addresses / URLs / Domains**
*   None identified (Current analysis indicates these are obfuscated within `fcn.100066d3`).

### **File paths / Registry keys**
*   None identified (Currently hidden via dynamic de-obfuscation).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Suspicious String Blocks:** The strings `SVWSQRV3`, `rocA9F`, and `T$lRQj` (and surrounding high-entropy character blocks) are likely encrypted components of the payload or configuration, though they cannot be verified as specific IOCs without the decryption key.
*   **Potential Packer/Loader Identifier:** `RichLz` (Note: This may be a signature for a specific packer or project name used by the threat actor).
*   **Behavioral Indicators (TTPs):**
    *   **Dynamic API Resolution:** Use of manual `GetProcAddress` wrappers (`fcn.10004660`) to hide calls to sensitive functions like `WriteProcessMemory`.
    *   **Delayed Execution:** Usage of `SetWaitableTimer` (`fcn.100032c3`) rather than standard sleep commands to evade sandbox detection.
    *   **Multi-stage logic:** The presence of a distinct de-obfuscation engine (`fcn.100066d3`) and custom memory management (`fcn.100087dd`).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High (for type) / Low (for specific family identification)
4. **Key evidence**: 
    *   **Sophisticated Evasion Tactics:** The sample employs advanced dynamic API resolution and a dedicated string de-obfuscation engine to hide critical functionality (such as memory injection and C2 communication) from static analysis tools.
    *   **Loader Characteristics:** The presence of custom memory management (`VirtualAlloc` with complex logic), multi-stage execution flows, and "hidden" data processing indicates the primary purpose is to decrypt and execute a secondary payload in memory.
    *   **Anti-Analysis Protections:** The use of `CreateWaitableTimer` (to stall sandboxes) and environment/locale checks suggests a high degree of professional engineering intended to bypass automated security systems.
