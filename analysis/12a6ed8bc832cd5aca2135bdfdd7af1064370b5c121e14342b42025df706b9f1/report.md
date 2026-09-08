# Threat Analysis Report

**Generated:** 2026-08-31 18:29 UTC
**Sample:** `12a6ed8bc832cd5aca2135bdfdd7af1064370b5c121e14342b42025df706b9f1_12a6ed8bc832cd5aca2135bdfdd7af1064370b5c121e14342b42025df706b9f1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12a6ed8bc832cd5aca2135bdfdd7af1064370b5c121e14342b42025df706b9f1_12a6ed8bc832cd5aca2135bdfdd7af1064370b5c121e14342b42025df706b9f1.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 3,264,512 bytes |
| MD5 | `61e4062d260d0020e6164c274e94b1ba` |
| SHA1 | `ad922a7f919fddce08fd71b88cc508c5b7d91350` |
| SHA256 | `12a6ed8bc832cd5aca2135bdfdd7af1064370b5c121e14342b42025df706b9f1` |
| Overall entropy | 6.955 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1714922011 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 2,515,968 | 6.475 | No |
| `.rdata` | 732,160 | 7.991 | ⚠️ Yes |
| `.data` | 7,680 | 3.52 | No |
| `.pdata` | 2,560 | 4.666 | No |
| `.rsrc` | 1,536 | 2.732 | No |
| `.reloc` | 3,584 | 0.945 | No |

### Imports

**KERNEL32.dll**: `LCMapStringEx`, `FlushFileBuffers`, `GetConsoleCP`, `GetConsoleMode`, `SetStdHandle`, `SetFilePointerEx`, `WriteConsoleW`, `CloseHandle`, `ExitProcess`, `HeapSize`, `LoadLibraryW`, `OutputDebugStringW`, `GetStringTypeW`, `HeapReAlloc`, `HeapAlloc`
**USER32.dll**: `GetAltTabInfoA`, `DrawAnimatedRects`, `SetDlgItemTextA`, `GetClipboardData`, `OemToCharBuffA`, `DrawIcon`, `GetScrollPos`, `GetWindowContextHelpId`, `MapWindowPoints`, `SetSysColors`, `SubtractRect`, `EqualRect`
**GDI32.dll**: `GetTextExtentExPointI`, `GetDCOrgEx`, `GetTextFaceA`, `SetBitmapDimensionEx`, `WidenPath`, `SetArcDirection`, `SelectClipPath`, `ArcTo`, `GdiGradientFill`, `SetTextCharacterExtra`, `SetPaletteEntries`, `GetLayout`, `SetBitmapBits`, `SetDCPenColor`, `PtInRegion`
**ole32.dll**: `CLSIDFromProgID`, `CoRevokeClassObject`, `CoGetCurrentProcess`, `StringFromGUID2`, `CoInvalidateRemoteMachineBindings`, `CoTaskMemAlloc`, `CoRevokeInitializeSpy`, `CoDosDateTimeToFileTime`, `CoFileTimeNow`, `BindMoniker`, `CoInstall`, `MonikerCommonPrefixWith`, `OleGetIconOfClass`, `OleDoAutoConvert`, `CoGetInterceptor`
**gdiplus.dll**: `GdiplusStartup`

### Exports

`GetFileVersionInfoA`, `GetFileVersionInfoByHandle`, `GetFileVersionInfoExW`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoSizeExW`, `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`, `VerFindFileA`, `VerFindFileW`, `VerInstallFileA`, `VerInstallFileW`, `VerLanguageNameA`, `VerLanguageNameW`, `VerQueryValueA`, `VerQueryValueW`

## Extracted Strings

Total strings found: **3407** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
H9D$xt
H9D$xt2
D$ -
H9D$Pt
H9D$Ht
H9D$Ht(
D$ 5z

D$,%xd
H9D$ht
H9D$pt
H9D$XtcH
H9D$Xt
x.B6Ep
K*8vR-x
+[ cA<z
CkwB2q
hiJm)~
&Sv<!O|
e&
 e}
S80mMu
>O,W|z
z}rKm'|
's*Fcz
,R-D|q
U
;Tc}
O?yGTv
LGw9;p
S=@mB)?KiV
^nUyvx5
#nVcOo5
SD|c%x
>?iWC

QC[Q\k
Sm*EJL
^ZXwLl
Qf^r	SD
f`ZNA4
@ckMMW
3h1m0h
j:+abM
P]U:2U
i@ZT?F@
TcVtB]A
hb2w=)Y
NeNXw[
XSk'HSR
0fD[!DAH
`IZf[)`
MOPH\K
C03(YX
>0]w@|
T$Y5XYFu-Q
M#~lg{|_W
~$2P6}
_c(oz:X
#@,5)*

AuW~<
6">36d
:-h$%B
wtTM	K
hk]Q>S^
cAWzb
L$>KysA
\,v'x
>Dp
'N
?wj!j7
A^%c1O
%Wg
"4
UaOGn[6}
i"c&6
%O_(}z
GpWMpT
u.MS_c
f<iiF:
3Jpnn

Zg13`1
t)'T/9
<sDR~y
K`jZ*
vkoac
uia7-#
Z255C;
8A}:JyH%
?3i]f1
i=1k=u
*J6V'I
FV|u$d
u4G.}S
q&C0~f
g_UF01
v`Py'#
PL6?|

'OEB^^/!
[-n`V5
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180002b00` | `0x180002b00` | 1760061 | — |
| `fcn.180260304` | `0x180260304` | 10605 | ✓ |
| `fcn.18026005c` | `0x18026005c` | 5491 | ✓ |
| `fcn.1802625b8` | `0x1802625b8` | 5375 | ✓ |
| `fcn.1802641c0` | `0x1802641c0` | 4077 | ✓ |
| `fcn.180001950` | `0x180001950` | 1938 | ✓ |
| `fcn.180265388` | `0x180265388` | 1908 | ✓ |
| `fcn.180002240` | `0x180002240` | 1259 | ✓ |
| `fcn.180001080` | `0x180001080` | 1258 | ✓ |
| `fcn.1802641f0` | `0x1802641f0` | 1252 | ✓ |
| `fcn.1802637d8` | `0x1802637d8` | 1018 | ✓ |
| `fcn.180001570` | `0x180001570` | 983 | ✓ |
| `fcn.180002730` | `0x180002730` | 972 | ✓ |
| `fcn.180263bd4` | `0x180263bd4` | 718 | ✓ |
| `fcn.180262184` | `0x180262184` | 686 | ✓ |
| `fcn.180262668` | `0x180262668` | 623 | ✓ |
| `fcn.1802648f8` | `0x1802648f8` | 622 | ✓ |
| `fcn.180261f28` | `0x180261f28` | 604 | ✓ |
| `fcn.1802669c8` | `0x1802669c8` | 603 | ✓ |
| `fcn.180262cf0` | `0x180262cf0` | 548 | ✓ |
| `fcn.180266570` | `0x180266570` | 498 | ✓ |
| `fcn.180261c88` | `0x180261c88` | 481 | ✓ |
| `fcn.18025fcf4` | `0x18025fcf4` | 479 | ✓ |
| `fcn.1802667f8` | `0x1802667f8` | 461 | ✓ |
| `fcn.180260aa8` | `0x180260aa8` | 455 | ✓ |
| `fcn.180261790` | `0x180261790` | 406 | ✓ |
| `fcn.1802603d4` | `0x1802603d4` | 405 | ✓ |
| `fcn.180263f3c` | `0x180263f3c` | 357 | ✓ |
| `entry0` | `0x18025f9c8` | 352 | ✓ |
| `fcn.180266120` | `0x180266120` | 348 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.180001080.c`](code/fcn.180001080.c)
- [`code/fcn.180001570.c`](code/fcn.180001570.c)
- [`code/fcn.180001950.c`](code/fcn.180001950.c)
- [`code/fcn.180002240.c`](code/fcn.180002240.c)
- [`code/fcn.180002730.c`](code/fcn.180002730.c)
- [`code/fcn.18025fcf4.c`](code/fcn.18025fcf4.c)
- [`code/fcn.18026005c.c`](code/fcn.18026005c.c)
- [`code/fcn.180260304.c`](code/fcn.180260304.c)
- [`code/fcn.1802603d4.c`](code/fcn.1802603d4.c)
- [`code/fcn.180260aa8.c`](code/fcn.180260aa8.c)
- [`code/fcn.180261790.c`](code/fcn.180261790.c)
- [`code/fcn.180261c88.c`](code/fcn.180261c88.c)
- [`code/fcn.180261f28.c`](code/fcn.180261f28.c)
- [`code/fcn.180262184.c`](code/fcn.180262184.c)
- [`code/fcn.1802625b8.c`](code/fcn.1802625b8.c)
- [`code/fcn.180262668.c`](code/fcn.180262668.c)
- [`code/fcn.180262cf0.c`](code/fcn.180262cf0.c)
- [`code/fcn.1802637d8.c`](code/fcn.1802637d8.c)
- [`code/fcn.180263bd4.c`](code/fcn.180263bd4.c)
- [`code/fcn.180263f3c.c`](code/fcn.180263f3c.c)
- [`code/fcn.1802641c0.c`](code/fcn.1802641c0.c)
- [`code/fcn.1802641f0.c`](code/fcn.1802641f0.c)
- [`code/fcn.1802648f8.c`](code/fcn.1802648f8.c)
- [`code/fcn.180265388.c`](code/fcn.180265388.c)
- [`code/fcn.180266120.c`](code/fcn.180266120.c)
- [`code/fcn.180266570.c`](code/fcn.180266570.c)
- [`code/fcn.1802667f8.c`](code/fcn.1802667f8.c)
- [`code/fcn.1802669c8.c`](code/fcn.1802669c8.c)

## Behavioral Analysis

This analysis describes the functionality of the provided code snippet based on the decompiled C pseudocode.

### Core Functionality and Purpose
The binary appears to be a **sophisticated loader or packer** (dropper/downloader). It is designed to execute obfuscated logic, perform environment checks, and potentially drop or write data to the filesystem. 

A significant amount of the code is dedicated to "unpacking" or managing internal structures rather than performing a high-level application task. The use of heavily obscured memory addresses (e.g., `0x180321068`) and manual pointer decoding suggests that much of the actual payload logic is hidden behind layers of obfuscation.

### Suspicious or Malicious Behaviors

*   **Anti-Analysis & Anti-Debugging:**
    *   **Debugger Detection:** Function `fcn.1802648f8` explicitly calls `IsDebuggerPresent()` and checks if the process is being debugged before proceeding with certain actions.
    *   **Environment Checks:** This same function resolves several `USER32` functions (`GetActiveWindow`, `GetLastActivePopup`, `GetProcessWindowStation`). These are commonly used by malware to determine if it is running in a sandbox or an automated analysis environment (e.g., checking if the active window belongs to a known analysis tool).
    *   **Forced Termination:** Multiple functions (`fcn.1802625b8`, `fcn.1802641c0`) contain logic that leads to `TerminateProcess` or internal "kill" switches, likely triggered if the malware detects an analyst's presence.

*   **File Manipulation & Payload Delivery:**
    *   **Data Writing:** Function `fcn.180265388` and its related components perform extensive buffer manipulation and call `WriteFile`. Given the preceding obfuscation, this is likely used to write a decrypted payload or secondary stage onto the disk.
    *   **Dynamic String/Resource Handling:** Functions like `fcn.1802637d8` and `fcn.180263f3c` handle complex multi-byte to wide-character conversions, potentially used to reconstruct strings or system paths that are only visible in memory at runtime.

*   **Potential Persistence/Injection Prep:**
    *   The code frequently calculates offsets and uses "decoded" pointers to interact with the Windows API. This is a common pattern in **process hollowing** or **reflective DLL injection**, where the malware prepares a malicious payload in memory before executing it.

### Notable Techniques and Patterns

*   **Control-Flow Flattening/Obfuscation:** Function `fcn.180001950` is a classic example of "opaque predicates" and control-flow obfuscation. It uses complex, seemingly random arithmetic (e.g., `uStack_d8 = 0x7791f5fad7e51f`) to determine the path of execution. This is designed to confuse decompilers and automated analysis tools.
*   **Dynamic API Resolution:** The code avoids a standard Import Address Table (IAT). Instead, it uses `DecodePointer` and `GetProcAddress`-style logic (via `_sym.imp.KERNEL32.dll`) to resolve functions at runtime. This hides the program's true capabilities from static analysis tools.
*   **Heavy Use of "Stolen" Instructions:** The frequent use of manual address calculations for standard actions (like writing a string or closing a handle) indicates that the original source code was heavily transformed by an obfuscator to hide its intent.
*   **Code Integrity/Checksumming:** There are several loops checking values against constants (e.g., `0x180321068`). This is often used as a "gatekeeper" mechanism—if the program's memory is modified by an analyst or tool, these checks will fail, and the program will exit.

### Summary for Security Operations
This sample exhibits high-confidence indicators of **malware (likely a loader/packer)**. It employs sophisticated anti-analysis techniques to hide its true purpose, which appears to be dropping a secondary payload or establishing a foothold by manipulating files via `WriteFile`. The presence of complex obfuscation confirms it is likely intended for targeted attacks or automated infection campaigns.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of control-flow flattening, opaque predicates, and "stolen" instructions is intended to hide the program's logic from decompilers and automated analysis. |
| **T1027.002** | Dynamic API Resolution | The code avoids a standard Import Address Table (IAT) by using `DecodePointer` and custom logic to resolve system functions at runtime. |
| **T1105** | Ingress Tool Transfer | The use of the `WriteFile` function following decryption indicates the delivery of a secondary payload or tool onto the disk. |
| **T1055** | Process Injection | The preparation of "decoded" pointers and memory offsets suggests the binary is preparing to perform process hollowing or reflective DLL injection. |
| **T1036** | Masquerading | (Implied) The analysis notes it behaves as a "sophisticated loader/packer," which often masks the malicious nature of the primary payload. |

### Analyst Notes:
*   **Anti-Analysis Context:** While "Antis-Debugging" and "Environment Checks" (e.g., `IsDebuggerPresent`, `GetActiveWindow`) do not have individual unique sub-technique IDs in the current MITRE ATT&CK framework, they are primary indicators of **Defense Evasion**.
*   **Loader/Packer behavior:** The combination of T1027 and T1105 strongly suggests a multi-stage attack where this binary serves as the initial "dropper" or "loader" for a secondary, more specialized malware payload.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (While `WriteFile` is mentioned in the behavior, no specific file paths were provided).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **C2/Persistence Indicators:** None identified.
*   **Anti-Analysis Techniques:** 
    *   `IsDebuggerPresent()` check (Function `fcn.1802648f8`)
    *   Environment checks via `GetActiveWindow`, `GetLastActivePopup`, and `GetProcessWindowStation`.
    *   Control-Flow Flattening/Obfuscation (Function `fcn.180001950`).
    *   Dynamic API Resolution (avoidance of standard IAT).
*   **Malware Type:** Identified as a sophisticated loader/packer using "stolen" instructions and internal memory offsets to hide payload delivery.

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1.  **Malware family:** Unknown (Loader/Packer)
2.  **Malware type:** Loader / Dropper
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Advanced Evasion & Anti-Analysis:** The sample employs sophisticated techniques including `IsDebuggerPresent` checks, environment-specific "kill switches" (checking for sandbox/analysis tools), and complex control-flow flattening to hide its true logic from analysts.
    *   **Obfuscated Payload Delivery:** The use of dynamic API resolution (avoiding the IAT), "stolen" instructions, and `WriteFile` operations following decryption indicates it is designed to unpack and drop a secondary malicious payload onto the filesystem.
    *   **Multi-stage Infrastructure:** The combination of advanced obfuscation (`T1027`) and preparation for process injection (`T1055`) confirms its role as a first-stage "gatekeeper" designed to establish a foothold or deliver more specialized malware (like a RAT or Ransomware).
