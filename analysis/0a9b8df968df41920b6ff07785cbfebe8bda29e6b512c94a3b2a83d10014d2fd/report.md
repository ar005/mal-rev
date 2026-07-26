# Threat Analysis Report

**Generated:** 2026-07-25 02:09 UTC
**Sample:** `0a9b8df968df41920b6ff07785cbfebe8bda29e6b512c94a3b2a83d10014d2fd_0a9b8df968df41920b6ff07785cbfebe8bda29e6b512c94a3b2a83d10014d2fd.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a9b8df968df41920b6ff07785cbfebe8bda29e6b512c94a3b2a83d10014d2fd_0a9b8df968df41920b6ff07785cbfebe8bda29e6b512c94a3b2a83d10014d2fd.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 233,472 bytes |
| MD5 | `f82649cd2916cf2f28cf450a7c1ca51f` |
| SHA1 | `c68d09dd50e357fd3de17a70b7724f8949441d77` |
| SHA256 | `0a9b8df968df41920b6ff07785cbfebe8bda29e6b512c94a3b2a83d10014d2fd` |
| Overall entropy | 4.562 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1746582712 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 14,336 | 5.634 | No |
| `.rdata` | 10,752 | 4.469 | No |
| `.data` | 512 | 2.023 | No |
| `.pdata` | 2,048 | 3.447 | No |
| `.rsrc` | 204,288 | 4.244 | No |
| `.reloc` | 512 | 1.255 | No |

### Imports

**KERNEL32.dll**: `VirtualProtect`, `GetCurrentProcess`, `WaitForSingleObject`, `Sleep`, `LoadLibraryA`, `CloseHandle`, `CreateThread`, `AddAtomA`, `GetAtomNameA`, `GetProcAddress`, `ExitProcess`, `GetConsoleWindow`, `CreateRemoteThread`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`
**USER32.dll**: `ShowWindow`, `MessageBoxW`
**MSVCP140.dll**: `_Query_perf_frequency`, `?_Xout_of_range@std@@YAXPEBD@Z`, `?_Xlength_error@std@@YAXPEBD@Z`, `_Thrd_sleep`, `_Query_perf_counter`, `_Xtime_get_ticks`
**VCRUNTIME140_1.dll**: `__CxxFrameHandler4`
**VCRUNTIME140.dll**: `__std_exception_copy`, `_CxxThrowException`, `__current_exception_context`, `__current_exception`, `memset`, `memcpy`, `__std_exception_destroy`, `__C_specific_handler`
**api-ms-win-crt-convert-l1-1-0.dll**: `atoi`
**api-ms-win-crt-string-l1-1-0.dll**: `strcat_s`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_register_onexit_function`, `_crt_atexit`, `_cexit`, `terminate`, `__p___argv`, `_initialize_narrow_environment`, `_c_exit`, `_initialize_onexit_table`, `_exit`, `_register_thread_local_exe_atexit_callback`, `_initterm_e`, `_initterm`, `_get_initial_narrow_environment`, `_configure_narrow_argv`, `__p___argc`
**api-ms-win-crt-heap-l1-1-0.dll**: `free`, `malloc`, `_callnewh`, `_set_new_mode`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__p__commode`, `_set_fmode`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

## Extracted Strings

Total strings found: **618** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
HkD$(dH
D$@HcD$@H=X
HcD$PHcL$DL
D$THcD$L
|$0	t
HcD$ H
t#HcD$ HcL$ H
HcD$ H
L$8H9H
D$`H9D$(v
H9D$Xv
D$PH9D$(w
u/HcH<H
T$u[H
bad allocation
Unknown exception
bad array new length
string too long
kernel32.dll
WaitForSingleObject
2300212021792276228822802248204820482048211321292113212821302129213421202097225821492120218721302144212021872130207221202187213020802120218721622128212020632231212221222125209722492120209722402220210821452172205020922080211322412249206021132049224122742285213021132129212021872130208021872114210821202049225621502177216820722059205021652162218721762184204820482048212021812240216421512120204922562128218721202072211621872112208021212049225622752134212023032249211321872100218421202049226221252097224921202097224022202113224122492060211320492241210422722165228921242051212420842056211721052257216522642136211621872112208421212049225621502113218720602120211621872112207621212049225621132187205221842120204922562113213621132136214221372138211321362113213721132138212021792284208021132130230322722136211321372138212021872066228121272303230323032141215420482121223821352153215821532158214921642048211321342121218522782124218522892113223421982254228921202303226121202097224921202097225821252097224021252097224921132128211321282113223422182250219522952303226122832163213821202185224121132232222420822048204821252097224921132129211321292154205121132129211322342167213222282277230322612283213721392120218522412120209722582121218522642125209722492130215220482050211221802130213021132234221520692097205623032261212021852246212021792243212821542058214321202185228921202185226621212247224023032303230323032125209722492130213021132234221420782197213523032261218122402063218122052049204820482120230322552063218021882049204820482283225922812276204920482048228022102303230323032095216521502150215221682160213121692048211520632193221422072269220022612283215522682297225321212234218222952213216620982250206920892186211422782048205220922241222120732244229521542225226022882157225122782294205221902211225321822183225121042229213921582277216121292295218521332294226021312233215422392259213322922290204821332163214921622093211321512149215821642106208021252159217021532156215621452095210120942096208020882125214521472153215821642159216321522107208021212158216421492156208021252145214720802127213120802136208020972096214320972101214321032089208021132160216021562149213521492146212321532164209521012099210320942099210220802088212321202132212521242092208021562153215521492080211921492147215521592089208021152152216221592157214920952105209820942096209421002100210320982094209720972100208021312145215021452162215320952101209921032094209921022061205820482058220521372128226021672130218621952065225320502245219422782211209620522296213721432168206421372129212321912164230121302301222220552098220722372145216721982120225021082170208821272135217821592078212321342078217121542252225221982051208321012229212821412132206522292078215422942113218022622244215021442292208622202249220822292282226222292191218721802234226721272223221620772118212820742129218820952136212520602274210921912186210822862263220921102077215522892123210922752248222121192095214122352097225321112110228721262072204822692126215122912269218822012203224822082064209422562298224420522173228820772295208220732289215422682146209621732249229320792243213720732244227520482113223821872127207022842303226121202097224922342048204821122048211322322048206420482048211322332112204820482048211322342222213020862198230322612120219521312131212021852279212021852289212021852266211322322048208020482048212121852297211322342279221922602106230322612120217922442080218122402164223021502187205521202049224321812240216522632136213621362120205320482048204820482128224322802207230123032303210121052094209720972096209421032094209920982048
invalid string position
RSDS'
E:\miansha\SingleSC\x64\Release\check1.pdb
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
VirtualProtect
GetCurrentProcess
WaitForSingleObject
LoadLibraryA
CloseHandle
CreateThread
AddAtomA
GetAtomNameA
GetProcAddress
ExitProcess
GetConsoleWindow
CreateRemoteThread
KERNEL32.dll
ShowWindow
MessageBoxW
USER32.dll
_Query_perf_frequency
?_Xout_of_range@std@@YAXPEBD@Z
?_Xlength_error@std@@YAXPEBD@Z
_Thrd_sleep
_Query_perf_counter
_Xtime_get_ticks
MSVCP140.dll
__CxxFrameHandler4
__std_exception_destroy
__std_exception_copy
__C_specific_handler
_CxxThrowException
__current_exception
__current_exception_context
memset
VCRUNTIME140_1.dll
VCRUNTIME140.dll
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140003908` | `0x140003908` | 2944 | ✓ |
| `fcn.140001680` | `0x140001680` | 553 | ✓ |
| `fcn.140002440` | `0x140002440` | 498 | ✓ |
| `fcn.14000421c` | `0x14000421c` | 428 | ✓ |
| `entry0` | `0x140003b9c` | 398 | ✓ |
| `fcn.140003f90` | `0x140003f90` | 331 | ✓ |
| `fcn.140003610` | `0x140003610` | 294 | ✓ |
| `fcn.140002df0` | `0x140002df0` | 283 | ✓ |
| `fcn.1400034c0` | `0x1400034c0` | 261 | ✓ |
| `main` | `0x1400019e0` | 246 | ✓ |
| `fcn.1400033d0` | `0x1400033d0` | 239 | ✓ |
| `fcn.140001510` | `0x140001510` | 237 | ✓ |
| `fcn.1400022e0` | `0x1400022e0` | 224 | ✓ |
| `fcn.140002050` | `0x140002050` | 224 | ✓ |
| `fcn.140002cd0` | `0x140002cd0` | 217 | ✓ |
| `fcn.140003190` | `0x140003190` | 217 | ✓ |
| `fcn.140003270` | `0x140003270` | 211 | ✓ |
| `fcn.1400021b0` | `0x1400021b0` | 206 | ✓ |
| `fcn.1400030c0` | `0x1400030c0` | 202 | ✓ |
| `fcn.140001cd0` | `0x140001cd0` | 197 | ✓ |
| `fcn.140002860` | `0x140002860` | 174 | ✓ |
| `fcn.140003e68` | `0x140003e68` | 172 | ✓ |
| `fcn.14000374c` | `0x14000374c` | 156 | ✓ |
| `fcn.1400013e0` | `0x1400013e0` | 154 | ✓ |
| `fcn.140001940` | `0x140001940` | 152 | ✓ |
| `fcn.140003d2c` | `0x140003d2c` | 152 | ✓ |
| `fcn.140001da0` | `0x140001da0` | 141 | ✓ |
| `fcn.140003ca0` | `0x140003ca0` | 139 | ✓ |
| `fcn.140002720` | `0x140002720` | 138 | ✓ |
| `fcn.140002f10` | `0x140002f10` | 134 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.1400013e0.c`](code/fcn.1400013e0.c)
- [`code/fcn.140001510.c`](code/fcn.140001510.c)
- [`code/fcn.140001680.c`](code/fcn.140001680.c)
- [`code/fcn.140001940.c`](code/fcn.140001940.c)
- [`code/fcn.140001cd0.c`](code/fcn.140001cd0.c)
- [`code/fcn.140001da0.c`](code/fcn.140001da0.c)
- [`code/fcn.140002050.c`](code/fcn.140002050.c)
- [`code/fcn.1400021b0.c`](code/fcn.1400021b0.c)
- [`code/fcn.1400022e0.c`](code/fcn.1400022e0.c)
- [`code/fcn.140002440.c`](code/fcn.140002440.c)
- [`code/fcn.140002720.c`](code/fcn.140002720.c)
- [`code/fcn.140002860.c`](code/fcn.140002860.c)
- [`code/fcn.140002cd0.c`](code/fcn.140002cd0.c)
- [`code/fcn.140002df0.c`](code/fcn.140002df0.c)
- [`code/fcn.140002f10.c`](code/fcn.140002f10.c)
- [`code/fcn.1400030c0.c`](code/fcn.1400030c0.c)
- [`code/fcn.140003190.c`](code/fcn.140003190.c)
- [`code/fcn.140003270.c`](code/fcn.140003270.c)
- [`code/fcn.1400033d0.c`](code/fcn.1400033d0.c)
- [`code/fcn.1400034c0.c`](code/fcn.1400034c0.c)
- [`code/fcn.140003610.c`](code/fcn.140003610.c)
- [`code/fcn.14000374c.c`](code/fcn.14000374c.c)
- [`code/fcn.140003908.c`](code/fcn.140003908.c)
- [`code/fcn.140003ca0.c`](code/fcn.140003ca0.c)
- [`code/fcn.140003d2c.c`](code/fcn.140003d2c.c)
- [`code/fcn.140003e68.c`](code/fcn.140003e68.c)
- [`code/fcn.140003f90.c`](code/fcn.140003f90.c)
- [`code/fcn.14000421c.c`](code/fcn.14000421c.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, this binary appears to be a **malicious loader or packer**. It contains several indicators common in malware designed to execute a malicious payload while evading detection and hiding its presence from the user.

### Core Functionality and Purpose
The primary purpose of this code is to prepare the environment for the execution of a hidden "payload." Rather than performing useful tasks (like a standard application), it focuses on:
*   **Environment preparation:** Validating system capabilities.
*   **Payload Execution:** Decoupling the malicious activity from the main logic using remote thread injection.
*   **Stealth:** Hiding its presence immediately after starting.

### Suspicious and Malicious Behaviors

*   **Process Injection / Remote Thread Execution:** 
    In `fcn.140001680`, the code performs a classic process injection sequence:
    *   It calls **`VirtualProtect`** to change the permissions of a memory region (likely making it executable).
    *   It retrieves its own handle via **`GetCurrentProcess`**.
    *   It calls **`CreateRemoteThread`** to execute a specific function address (`0x140001660`). This is a common technique to run code in a new thread, often used to hide the primary execution flow from basic debuggers.
*   **Evasion and Anti-Analysis:**
    *   **Hardware/Feature Checking:** `fcn.14000421c` uses `cpuid` instructions (wrapped in functions like `cpuid_basic_info`) to check for specific CPU features. This is often used by malware to detect if it's running in a virtual machine or an emulator.
    *   **Anti-Debugging:** Functions like `fcn.140003f90` and `fcn.140003610` contain logic that appears to handle environment checks and potentially intercepting debugger events (using `SetUnhandledExceptionFilter`).
*   **Stealth/Evasion Techniques:**
    *   **Console Hiding:** In the `main` function, after showing a `MessageBoxW`, the code immediately calls **`GetConsoleWindow`** followed by **`ShowWindow(..., 0)`**. This is intended to hide the console window from the user as soon as they click "OK" on the message box, allowing the malware to run in the background without any visible interface.

### Notable Techniques and Patterns
*   **Standard Packer/Loader Pattern:** The sequence of `MessageBox` $\rightarrow$ `ShowWindow(hidden)` $\rightarrow$ `CreateRemoteThread` is a classic behavior for an "initial stager." It interacts with the user briefly to look like a legitimate process before moving into its hidden malicious phase.
*   **Complex Instruction Logic:** The presence of extensive "internal" logic (like the large number of `fcn.` labels) suggests that this code might be part of a larger toolkit or was compiled from a source that used heavy template usage, common in modern commercial packers.
*   **Memory Manipulation:** The use of `VirtualProtect` specifically before calling `CreateRemoteThread` indicates that the payload is likely stored as "data" (not yet executable) and must be manually marked as code before it can run.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1055 | Process Injection | The use of `VirtualProtect` and `CreateRemoteThread` to execute code in a separate thread is a primary method for injecting malicious payloads into memory. |
| T1496 | Virtualization/Sandbox Evasion | The use of `cpuid` instructions to check CPU features indicates an attempt to detect if the sample is running within a virtual machine or emulator. |
| T1036 | Debugger Evasion | The implementation of custom exception handling via `SetUnhandledExceptionFilter` is used to intercept and bypass debugger activities. |
| T1027 | Software Packing | The analysis identifies the binary as a packer/loader, which uses wrapping techniques to hide functionality until execution. |
| T1059 | Command and Scripting Interpreter (Implicit) | While not explicitly a script, the "initial stager" behavior is often used to facilitate remote execution or secondary payloads via common system interpreters. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `E:\miansha\SingleSC\x64\Release\check1.pdb` (Note: This is a PDB path; while internal to the build process, it serves as an artifact of the developer environment.)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified. (The long string of digits provided in the text does not conform to standard MD5, SHA-1, or SHA-256 formats and appears to be obfuscated data or a memory dump.)

**Other artifacts**
*   **Execution Logic/Off-set:** Function `fcn.140001680` utilizes `CreateRemoteThread` targeting specific memory address `0x140001660`.
*   **Stealth Behavior:** Use of the sequence `MessageBoxW` $\rightarrow$ `GetConsoleWindow` $\rightarrow$ `ShowWindow(..., 0)` to hide the console window immediately after user interaction.
*   **Evasion Modules:** Specific internal functions identified as anti-analysis/evasion points:
    *   `fcn.14000421c` (cpuid/environment checking)
    *   `fcn.140003f90` (potential debugger interception)
    *   `fcn.140003610` (environmental checks)

---

## Malware Family Classification

1. **Malware family**: Unknown (or custom)
2. **Malware type**: Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Process Injection Techniques:** The use of `VirtualProtect` followed by `CreateRemoteThread` to execute code at a specific memory address is a definitive indicator of loader behavior, designed to inject and run a payload while separating it from the main process.
*   **Anti-Analysis & Evasion:** The presence of `cpuid` instructions for environment/VM detection and custom exception handlers (`SetUnhandledExceptionFilter`) confirms the sample's intent to evade detection by security researchers or automated sandboxes.
*   **Stealthy Execution Pattern:** The sequence of displaying a `MessageBoxW` followed immediately by hiding the console window via `ShowWindow` is a classic "initial stager" tactic used to provide a brief, seemingly legitimate interaction before performing hidden malicious activities in the background.
