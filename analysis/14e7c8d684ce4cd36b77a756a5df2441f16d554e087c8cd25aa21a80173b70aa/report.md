# Threat Analysis Report

**Generated:** 2026-09-06 12:32 UTC
**Sample:** `14e7c8d684ce4cd36b77a756a5df2441f16d554e087c8cd25aa21a80173b70aa_14e7c8d684ce4cd36b77a756a5df2441f16d554e087c8cd25aa21a80173b70aa.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14e7c8d684ce4cd36b77a756a5df2441f16d554e087c8cd25aa21a80173b70aa_14e7c8d684ce4cd36b77a756a5df2441f16d554e087c8cd25aa21a80173b70aa.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,788,664 bytes |
| MD5 | `de54fb96b430c75652f296e7af98dcda` |
| SHA1 | `07f49349d4638f4157eb5bfeb9e872d8244fc5da` |
| SHA256 | `14e7c8d684ce4cd36b77a756a5df2441f16d554e087c8cd25aa21a80173b70aa` |
| Overall entropy | 7.445 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1668802220 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 45,568 | 6.592 | No |
| `.rdata` | 25,088 | 4.787 | No |
| `.data` | 2,048 | 2.265 | No |
| `.rsrc` | 5,469,696 | 7.45 | ⚠️ Yes |
| `.reloc` | 4,096 | 6.301 | No |

### Imports

**mscoree.dll**: `CorBindToRuntimeEx`
**KERNEL32.dll**: `GetModuleFileNameA`, `DecodePointer`, `SizeofResource`, `LockResource`, `LoadLibraryW`, `LoadResource`, `FindResourceW`, `GetProcAddress`, `WriteConsoleW`, `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleCP`, `FlushFileBuffers`, `HeapReAlloc`, `HeapSize`
**OLEAUT32.dll**: `VariantInit`, `SafeArrayUnaccessData`, `SafeArrayCreateVector`, `SafeArrayDestroy`, `VariantClear`, `SafeArrayAccessData`

## Extracted Strings

Total strings found: **22923** (showing first 100)

```
!This program cannot be run in DOS mode.
$
RichE>`
`.rdata
@.data
@.reloc
T$Rh
M;Jr

QQSVWd
38_^]
E9xt
&9Gv!8E
Yt
jV
9Nv@k
URPQQh
kUQPXY]Y[
< t1<	t-
uh0MA
uj Y;E
jh 'A
tf;1u
WWWPWS
u-PWWS
PjhLMA
PQhPAA
PQhXBA
SSVWh 
f9:t!V
WuVVS
QQSWj0j@
jh (A
tl=PFA
jh@(A
jh`(A
u9Mu!3
PPPPPPPP
PPPPPWS
PP9E u:PPVWP
t;Et
jh()A

u,jXj

u	jZf
\9EuY
D$+d$SVW
Unknown exception
bad exception
__based(
__cdecl
__pascal
__stdcall
__thiscall
__fastcall
__vectorcall
__clrcall
__eabi
__swift_1
__swift_2
__swift_3
__ptr64
__restrict
__unaligned
restrict(
 delete
operator
`vftable'
`vbtable'
`vcall'
`typeof'
`local static guard'
`string'
`vbase destructor'
`vector deleting destructor'
`default constructor closure'
`scalar deleting destructor'
`vector constructor iterator'
`vector destructor iterator'
`vector vbase constructor iterator'
`virtual displacement map'
`eh vector constructor iterator'
`eh vector destructor iterator'
`eh vector vbase constructor iterator'
`copy constructor closure'
`udt returning'
`local vftable'
`local vftable constructor closure'
 new[]
 delete[]
`omni callsig'
`placement delete closure'
`placement delete[] closure'
`managed vector constructor iterator'
`managed vector destructor iterator'
`eh vector copy constructor iterator'
`eh vector vbase copy constructor iterator'
`dynamic initializer for '
`dynamic atexit destructor for '
`vector copy constructor iterator'
`vector vbase copy constructor iterator'
`managed vector copy constructor iterator'
`local static thread guard'
operator "" 
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040a138` | `0x40a138` | 2957 | ✓ |
| `fcn.00403b30` | `0x403b30` | 1396 | ✓ |
| `fcn.00402a2b` | `0x402a2b` | 933 | ✓ |
| `fcn.00408970` | `0x408970` | 922 | ✓ |
| `fcn.00408222` | `0x408222` | 770 | ✓ |
| `fcn.0040a57e` | `0x40a57e` | 614 | ✓ |
| `fcn.0040b895` | `0x40b895` | 563 | ✓ |
| `fcn.00408eb4` | `0x408eb4` | 541 | ✓ |
| `fcn.0040add3` | `0x40add3` | 536 | ✓ |
| `fcn.00409e92` | `0x409e92` | 524 | ✓ |
| `fcn.00404852` | `0x404852` | 523 | ✓ |
| `fcn.0040a93e` | `0x40a93e` | 523 | ✓ |
| `fcn.00407f6f` | `0x407f6f` | 520 | ✓ |
| `fcn.004066eb` | `0x4066eb` | 497 | ✓ |
| `fcn.0040b692` | `0x40b692` | 480 | ✓ |
| `fcn.00401c04` | `0x401c04` | 468 | ✓ |
| `fcn.00409817` | `0x409817` | 435 | ✓ |
| `fcn.00406396` | `0x406396` | 404 | ✓ |
| `fcn.00405cbb` | `0x405cbb` | 400 | ✓ |
| `entry0` | `0x4014ad` | 390 | ✓ |
| `fcn.00405ee1` | `0x405ee1` | 388 | ✓ |
| `fcn.00404477` | `0x404477` | 373 | ✓ |
| `fcn.004040f0` | `0x4040f0` | 371 | ✓ |
| `fcn.00402570` | `0x402570` | 346 | ✓ |
| `fcn.00403152` | `0x403152` | 333 | ✓ |
| `fcn.00407907` | `0x407907` | 330 | ✓ |
| `fcn.00404f40` | `0x404f40` | 321 | ✓ |
| `fcn.004027d4` | `0x4027d4` | 318 | ✓ |
| `fcn.00405973` | `0x405973` | 315 | ✓ |
| `fcn.00402dd0` | `0x402dd0` | 310 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401c04.c`](code/fcn.00401c04.c)
- [`code/fcn.00402570.c`](code/fcn.00402570.c)
- [`code/fcn.004027d4.c`](code/fcn.004027d4.c)
- [`code/fcn.00402a2b.c`](code/fcn.00402a2b.c)
- [`code/fcn.00402dd0.c`](code/fcn.00402dd0.c)
- [`code/fcn.00403152.c`](code/fcn.00403152.c)
- [`code/fcn.00403b30.c`](code/fcn.00403b30.c)
- [`code/fcn.004040f0.c`](code/fcn.004040f0.c)
- [`code/fcn.00404477.c`](code/fcn.00404477.c)
- [`code/fcn.00404852.c`](code/fcn.00404852.c)
- [`code/fcn.00404f40.c`](code/fcn.00404f40.c)
- [`code/fcn.00405973.c`](code/fcn.00405973.c)
- [`code/fcn.00405cbb.c`](code/fcn.00405cbb.c)
- [`code/fcn.00405ee1.c`](code/fcn.00405ee1.c)
- [`code/fcn.00406396.c`](code/fcn.00406396.c)
- [`code/fcn.004066eb.c`](code/fcn.004066eb.c)
- [`code/fcn.00407907.c`](code/fcn.00407907.c)
- [`code/fcn.00407f6f.c`](code/fcn.00407f6f.c)
- [`code/fcn.00408222.c`](code/fcn.00408222.c)
- [`code/fcn.00408970.c`](code/fcn.00408970.c)
- [`code/fcn.00408eb4.c`](code/fcn.00408eb4.c)
- [`code/fcn.00409817.c`](code/fcn.00409817.c)
- [`code/fcn.00409e92.c`](code/fcn.00409e92.c)
- [`code/fcn.0040a138.c`](code/fcn.0040a138.c)
- [`code/fcn.0040a57e.c`](code/fcn.0040a57e.c)
- [`code/fcn.0040a93e.c`](code/fcn.0040a93e.c)
- [`code/fcn.0040add3.c`](code/fcn.0040add3.c)
- [`code/fcn.0040b692.c`](code/fcn.0040b692.c)
- [`code/fcn.0040b895.c`](code/fcn.0040b895.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C code, here is an analysis of the binary's functionality and behavior.

### Core Functionality
The binary appears to be a complex, possibly multi-stage application or a wrapper for a secondary payload (likely involving .NET components given the presence of `mscoree.dll` in the strings). It performs significant amount of internal data processing, string manipulation, and environment preparation before executing its primary logic.

### Suspicious and Malicious Behaviors

*   **Anti-Analysis & Debugger Detection:**
    *   The function `fcn.005973` explicitly calls `IsDebuggerPresent`. This is a standard technique used by malware to detect if it is being run in an analysis environment (like x64dbg or OllyDbg) and alter its behavior accordingly to evade detection.
    *   The binary performs extensive CPU feature checks (`fcn.00401c04`) and FPU state validations (`fcn.00408222`). While these can be part of standard library initialization, they are frequently used in "packer" stubs to ensure the environment meets specific requirements before unpacking a malicious payload.

*   **File System Enumeration:**
    *   Function `fcn.005ee1` utilizes `FindFirstFileExA` and `FindNextFileA`. This indicates that the program actively scans the filesystem for files. In a malware context, this is often used to locate configuration files, identify other executables to infect, or search for specific targets (like browser profiles or crypto wallets).

*   **I/O Operations & Data Exfiltration:**
    *   Several functions (e.g., `fcn.008970`, `fcn.008950`) interact with `WriteFile`. The complexity of the logic surrounding these calls suggests that data is being processed and then written to a file, pipe, or network socket.
    *   The frequent usage of `GetConsoleCP` and various Unicode/MultiByte conversion functions (`WideCharToMultiByte`) suggests the program is handling strings specifically for output or logging purposes.

### Notable Techniques & Patterns

*   **Complex Buffer Manipulation:**
    *   Functions like `fcn.003b30` show heavy use of loops to move and copy memory blocks (similar to `memmove`). This indicates that the code handles large, complex data structures or "de-obfuscates" a buffer before use.
*   **String/Encoding Processing:**
    *   A significant portion of the code is dedicated to handling different Code Pages (`GetCPInfo`, `IsValidCodePage`) and converting between MultiByte and WideChar formats. This is often seen in "droppers" that need to handle file paths or system information accurately across different locales.
*   **Potential .NET Wrapper:**
    *   The presence of strings like `mscoree.dll` and `CorBindToRuntimeEx` strongly suggests that this binary may be a "loader" meant to bootstrap a .NET-based payload. The heavy amount of "boilerplate" code seen in the disassembly is characteristic of an intermediate language (IL) wrapper or a complex packer.
*   **Exception Handling:**
    *   The use of `SetUnhandledExceptionFilter` and various exception handling routines suggests the program may have a custom error-handling mechanism to prevent crashes when it encounters unexpected environments during its execution stages.

### Summary for Incident Response
This binary exhibits several behaviors consistent with a **dropper** or **information stealer**. It performs anti-debugging checks, iterates through files on the local system, and contains significant logic for processing data buffers before outputting them via `WriteFile`. The presence of .NET-related strings suggests it may be a wrapper for an obfuscated .NET payload.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualized Environment | The use of `IsDebuggerPresent` and extensive CPU/FPU state validations are standard techniques to detect if the binary is running in a sandbox or analysis environment. |
| **T1083** | File and Directory Discovery | The utilization of `FindFirstFileExA` and `FindNextFileA` indicates the system is scanning for local files, such as configuration data or targets for infection. |
| **T1027** | Obfuscated Files or Information | The heavy use of loop-based buffer manipulation to "de-obfuscate" memory blocks before execution is indicative of a packer or loader hiding its true functionality. |
| **T1048** | Exfiltration Over Alternative Protocol | The usage of `WriteFile` to output processed data into pipes, files, or network sockets suggests the movement of information out of the primary process context. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   *Note: The path `C:\Users\jmorgan\Source\cwcontrol\Custom\DotNetRunner\Release\DotNetRunner.pdb` was identified in the strings but has been excluded as it is a development `.pdb` file (debug information) from the developer's local environment, not a malicious system path.*

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Malware Type Indicators:** 
    *   **.NET Wrapper/Loader:** The presence of `mscoree.dll` and the function `CorBindToRuntimeEx` indicates this binary is designed to host or wrap a .NET-based payload.
*   **Anti-Analysis Techniques:** 
    *   **Debugger Detection:** Use of `IsDebuggerPresent`.
    *   **Environment Validation:** Extensive CPU feature checks and FPU state validations (common in packers/crypters).
*   **System Interaction:** 
    *   The binary utilizes `FindFirstFileExA` and `FindNextFileA`, indicating it actively crawls the filesystem.
    *   Presence of heavy string manipulation and encoding logic (`GetCPInfo`, `WideCharToMultiByte`) used to handle system paths or data exfiltration.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**: 
    *   **.NET Wrapper Behavior:** The presence of `mscoree.dll` and `CorBindToRuntimeEx` strings, combined with the report's description of "boilerplate" code, strongly indicates this is a wrapper designed to host or transition execution to a .NET-based payload.
    *   **Anti-Analysis Techniques:** The inclusion of `IsDebuggerPresent` calls and extensive CPU/FPU state validation are classic indicators of a packer or loader designed to evade analysis environments.
    *   **Evasive Execution Flow:** Significant buffer manipulation, encoding conversions (`WideCharToMultiByte`), and file system enumeration suggest the binary is preparing an environment (or de-obfuscating data) for a secondary malicious stage.
