# Threat Analysis Report

**Generated:** 2026-08-10 16:52 UTC
**Sample:** `0dd6fabb987f0a58550c4b2ef599239947f3f5b5dc9ff496ce52c9f67671c689_0dd6fabb987f0a58550c4b2ef599239947f3f5b5dc9ff496ce52c9f67671c689.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0dd6fabb987f0a58550c4b2ef599239947f3f5b5dc9ff496ce52c9f67671c689_0dd6fabb987f0a58550c4b2ef599239947f3f5b5dc9ff496ce52c9f67671c689.exe` |
| File type | PE32+ executable for MS Windows 5.02 (DLL), x86-64, 6 sections |
| Size | 2,757,632 bytes |
| MD5 | `08835e514e1ce81a3613475eb1099fb9` |
| SHA1 | `62204d9b20a402fa31231ce89cc50de3a57a5417` |
| SHA256 | `0dd6fabb987f0a58550c4b2ef599239947f3f5b5dc9ff496ce52c9f67671c689` |
| Overall entropy | 6.621 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1700323416 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,597,440 | 6.836 | No |
| `.rdata` | 18,944 | 5.054 | No |
| `.data` | 1,134,080 | 5.414 | No |
| `.pdata` | 2,048 | 4.225 | No |
| `.rsrc` | 1,536 | 2.972 | No |
| `.reloc` | 2,560 | 1.336 | No |

### Imports

**KERNEL32.dll**: `UnhandledExceptionFilter`, `LoadLibraryW`, `HeapReAlloc`, `SetUnhandledExceptionFilter`, `IsValidCodePage`, `GetOEMCP`, `GetACP`, `GetCPInfo`, `GetSystemTimeAsFileTime`, `IsDebuggerPresent`, `RtlVirtualUnwind`, `RtlLookupFunctionEntry`, `RtlCaptureContext`, `TerminateProcess`, `GetCurrentProcess`
**USER32.dll**: `CharToOemA`, `IsZoomed`, `DrawTextExA`, `CharUpperA`, `GetMenuState`, `IsChild`, `ScrollWindow`, `TileWindows`, `ToUnicode`, `GetScrollBarInfo`, `SetDlgItemInt`, `WinHelpA`, `EnableScrollBar`, `CharPrevExA`, `GetIconInfo`
**GDI32.dll**: `OffsetClipRgn`, `GetAspectRatioFilterEx`, `ModifyWorldTransform`, `PatBlt`, `LineTo`, `GetTextExtentPointI`, `GetMiterLimit`, `SetLayout`, `OffsetWindowOrgEx`, `PlayEnhMetaFileRecord`, `GetEnhMetaFileA`, `GetCharWidth32A`, `SetBitmapBits`, `Polygon`, `ArcTo`
**ole32.dll**: `CoGetMarshalSizeMax`, `StringFromIID`, `CoResumeClassObjects`, `CoQueryClientBlanket`, `CoGetObject`, `CoGetPSClsid`, `CoInstall`, `OleRegGetMiscStatus`, `CoTestCancel`, `CoGetInstanceFromFile`, `CoSetProxyBlanket`
**gdiplus.dll**: `GdiplusStartup`

### Exports

`AlphaBlend`, `DllInitialize`, `GradientFill`, `TransparentBlt`, `vSetDdrawflag`

## Extracted Strings

Total strings found: **2077** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
D$p=<
LB7*>Sv
>eF}<v~
c:a>u<v
4~WP&}z
$_G[9lu
`5P6Xy
+LJz>t
0<blCz
YY9X`jv
<;?8ls
ToqB#z
H9D$hw
D$ -w
8^O/}<
G^^vG0ada
.

q4,
|hXZS
gO"kTL
"g]-hT%%
1	)([x
ce>?av
(2uEMJ
/|g](r7
*7y8BD
>s3Db*
UdJ`w
ie2D%?
fG-E9}
X/HT?o
#;:H /
"A*x(d
U+68-Z
AAYmb.
p\*$`
8?BYp0-
{TzW1o
j].)B^
zI-!tuJ
z&*SiP
YJBr/+
+v 93t
>Bg(E}'e
[E""2z
lXt1Ps]
X8't6pF
W|;x7G
z3f	q 
mFQ.<mM
|"S-sj
u/)Y-co! 
t.2P)fG
 B\AA`
(_51,L
JsNwqH
X:|K3&
?tHelj
M@ lJw
[jBzVS
%g[2}V
Eb^VBA
\^*/W\q
>aQ
u	
LSjV#
i
$t5dBE
d@kjy0
	"D@bX
\s,H'w
+wPfv\t
pqNbrH
c}m5ov
8(Y]"K
treJ%
w&T>Tx
f=awao
(")Fae/m
PCL?;<W}s
PH+6;@V
eW<(D
A%@zC
GW	v@|
/$A:x8
Z(m&(?
X'u-(
;x&O1H
Hx:P=[
5ZBrQd
mA |w&
\5\U+C
qc,M$*
c	o.$Cc
Tm5u&
{6	H+G
%q&JgD
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1800034c0` | `0x1800034c0` | 936163 | — |
| `fcn.180181a58` | `0x180181a58` | 8645 | ✓ |
| `fcn.1801814a0` | `0x1801814a0` | 5887 | ✓ |
| `fcn.180001370` | `0x180001370` | 3714 | ✓ |
| `fcn.180185350` | `0x180185350` | 2406 | ✓ |
| `fcn.180002b90` | `0x180002b90` | 1717 | ✓ |
| `fcn.1800e7e70` | `0x1800e7e70` | 1562 | ✓ |
| `fcn.1800025a0` | `0x1800025a0` | 1514 | ✓ |
| `fcn.1801863a4` | `0x1801863a4` | 1276 | ✓ |
| `fcn.180184708` | `0x180184708` | 1006 | ✓ |
| `fcn.180002200` | `0x180002200` | 916 | ✓ |
| `fcn.180001030` | `0x180001030` | 830 | ✓ |
| `fcn.180185380` | `0x180185380` | 820 | ✓ |
| `fcn.180181d90` | `0x180181d90` | 722 | ✓ |
| `fcn.180184df0` | `0x180184df0` | 714 | ✓ |
| `fcn.180185e78` | `0x180185e78` | 712 | ✓ |
| `fcn.1801834cc` | `0x1801834cc` | 629 | ✓ |
| `fcn.180003250` | `0x180003250` | 610 | ✓ |
| `fcn.1801842b4` | `0x1801842b4` | 605 | ✓ |
| `fcn.180183c50` | `0x180183c50` | 562 | ✓ |
| `fcn.180185744` | `0x180185744` | 520 | ✓ |
| `fcn.1801830ec` | `0x1801830ec` | 496 | ✓ |
| `fcn.18018287c` | `0x18018287c` | 483 | ✓ |
| `fcn.180183744` | `0x180183744` | 478 | ✓ |
| `fcn.180182208` | `0x180182208` | 463 | ✓ |
| `fcn.1801861d4` | `0x1801861d4` | 461 | ✓ |
| `fcn.1800e8490` | `0x1800e8490` | 445 | ✓ |
| `fcn.180181bbc` | `0x180181bbc` | 399 | ✓ |
| `fcn.180182e14` | `0x180182e14` | 377 | ✓ |
| `fcn.180185154` | `0x180185154` | 350 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001030.c`](code/fcn.180001030.c)
- [`code/fcn.180001370.c`](code/fcn.180001370.c)
- [`code/fcn.180002200.c`](code/fcn.180002200.c)
- [`code/fcn.1800025a0.c`](code/fcn.1800025a0.c)
- [`code/fcn.180002b90.c`](code/fcn.180002b90.c)
- [`code/fcn.180003250.c`](code/fcn.180003250.c)
- [`code/fcn.1800e7e70.c`](code/fcn.1800e7e70.c)
- [`code/fcn.1800e8490.c`](code/fcn.1800e8490.c)
- [`code/fcn.1801814a0.c`](code/fcn.1801814a0.c)
- [`code/fcn.180181a58.c`](code/fcn.180181a58.c)
- [`code/fcn.180181bbc.c`](code/fcn.180181bbc.c)
- [`code/fcn.180181d90.c`](code/fcn.180181d90.c)
- [`code/fcn.180182208.c`](code/fcn.180182208.c)
- [`code/fcn.18018287c.c`](code/fcn.18018287c.c)
- [`code/fcn.180182e14.c`](code/fcn.180182e14.c)
- [`code/fcn.1801830ec.c`](code/fcn.1801830ec.c)
- [`code/fcn.1801834cc.c`](code/fcn.1801834cc.c)
- [`code/fcn.180183744.c`](code/fcn.180183744.c)
- [`code/fcn.180183c50.c`](code/fcn.180183c50.c)
- [`code/fcn.1801842b4.c`](code/fcn.1801842b4.c)
- [`code/fcn.180184708.c`](code/fcn.180184708.c)
- [`code/fcn.180184df0.c`](code/fcn.180184df0.c)
- [`code/fcn.180185154.c`](code/fcn.180185154.c)
- [`code/fcn.180185350.c`](code/fcn.180185350.c)
- [`code/fcn.180185380.c`](code/fcn.180185380.c)
- [`code/fcn.180185744.c`](code/fcn.180185744.c)
- [`code/fcn.180185e78.c`](code/fcn.180185e78.c)
- [`code/fcn.1801861d4.c`](code/fcn.1801861d4.c)
- [`code/fcn.1801863a4.c`](code/fcn.1801863a4.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C pseudocode, here is an analysis of the binary's functionality and behavior.

### Core Functionality and Purpose
The binary appears to be a **sophisticated loader or "dropper"** designed with significant layers of obfuscation. Its primary purpose seems to be navigating a complex internal state to decrypt data/code in memory and then interacting with the system's UI components—likely as part of a multi-stage infection chain where it prepares for or executes a secondary malicious payload.

### Suspicious and Malicious Behaviors
The following behaviors are highly indicative of malware:

*   **Anti-Analysis & Anti-Debugging:**
    *   **Direct Debugger Detection:** Function `fcn.18018530` explicitly calls `IsDebuggerPresent()`. If a debugger is detected, the code enters logic to set an unhandled exception filter and then intentionally terminates the process with a specific error code (`0xc0000409`).
    *   **Execution Profiling:** The use of `RtlCaptureContext` and `RtlLookupFunctionEntry` in several functions suggests the malware is inspecting its own execution context, likely to detect if it is being "traced" or manipulated by an analysis tool.
    *   **Trap-based Evasion:** Several locations (e.g., `fcn.1801842b4`) contain conditional branches that lead to `swi(3)` calls or forced crashes if certain internal checks fail, a technique used to break automated sandboxes and debuggers.

*   **Obfuscated File System Activity:**
    *   **Non-Human Readable Paths:** The code interacts with files in highly randomized directory structures, such as: 
        *   `Mx\SuCDhh\VrK6r1V\Tabulate` (in `fcn.1800e7e70`)
        *   `Freightage\Monembryonic\sensu\mP6y\FjFWTx` (in `fcn.1800025a0`)
    *   These "garbage" paths are a common technique used by malware to hide the location of dropped components or configuration files from casual observation.

*   **Environment/UI Awareness:**
    *   The code imports and uses several functions via `GetProcAddress` to query the GUI environment: `GetActiveWindow`, `GetLastActivePopup`, `GetUserObjectInformationW`, and `GetProcessWindowStation`. This is often used in **"Spyware" or "Banking Trojans"** to determine which window the user is currently interacting with (e.g., a web browser or a banking application).

### Notable Techniques and Patterns
*   **Massive Decoding Loops:** Function `fcn.180184708` contains an extremely long loop that calls a handler (`fcn.180181820`) on a large sequence of memory offsets. This is typical for **decryption or de-obfuscation** of internal resource tables or "unpacking" the next stage of the payload in memory.
*   **Control Flow Obfuscation:** Functions like `fcn.180001370` are filled with "junk code"—mathematical operations on local variables that result in no meaningful change to the program state but make it difficult for a human analyst to follow the logic or identify the underlying API calls (like `DrawTextExA`).
*   **Dynamic Resource Management:** The frequent use of `CreateMutex`, `CreateEvent`, and custom memory management routines (`fcn.180183744`) indicates the malware is managing its own internal state to avoid creating a static footprint in the Import Address Table (IAT).
*   **String Obfuscation:** The presence of large, high-entropy data blocks (visible in the string dump) and the specific logic seen in `fcn.180183c50` suggest that almost all strings used by the malware are decrypted at runtime rather than being stored as plain text.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Execution Guard | The use of `IsDebuggerPresent()`, forced `swi(3)` crashes, and trap-based branches are specifically designed to detect and hinder analysis by debuggers and sandboxes. |
| **T1497** | Virtualization/Sandbox Detection | The inclusion of `RtlCaptureContext` and `RtlLookupFunctionEntry` indicates the malware is checking for signs of instrumentation or execution in a non-native environment. |
| **T1564** | Hide Artifacts | The utilization of randomized, "garbage" file paths (e.g., `Mx\SuCDhh...`) conceals the location of dropped components from manual human inspection. |
| **T1027** | Obfuscated Files/Service | The extensive decoding loops, large high-entropy data blocks (string obfuscation), and "junk code" are used to hide functionality and avoid detection during static analysis. |
| **T1036** | Execution Guard | The use of `GetActiveWindow` and `GetLastActivePopup` functions helps the malware determine if a target application (like a banking site) is active before proceeding with malicious actions. |

***Note on Overlap:** While "Execution Guard" and "Obfuscated Files/Service" are broad categories, they are used here to capture multiple specific behaviors mentioned in your analysis: T1036 addresses the active evasion of tools, while T1027 covers the structural obfuscation of the code itself.*

---

## Indicators of Compromise

Based on the provided string dump and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   (None identified)

**File paths / Registry keys**
*   `Mx\SuCDhh\VrK6r1V\Tabulate` (Obfuscated/Junk path used for hiding components)
*   `Freightage\Monembryonic\sensu\mP6y\FjFWTx` (Obfuscated/Junk path used for hiding components)

**Mutex names / Named pipes**
*   (None identified - note: while the analysis mentions the use of `CreateMutex`, no specific mutex strings were provided in the dump.)

**Hashes**
*   (None identified)

**Other artifacts**
*   **Anti-Analysis/Debug Detection:** Use of `IsDebuggerPresent()`, `RtlCaptureContext`, and `RtlLookupFunctionEntry`.
*   **Evasion Techniques:** Implementation of `swi(3)` calls to break automated sandboxes.
*   **Spyware/Banking Trojan Indicators:** Usage of specific APIs via `GetProcAddress` to monitor UI interaction:
    *   `GetActiveWindow`
    *   `GetLastActivePopup`
    *   `GetUserObjectInformationW`
    *   `GetProcessWindowStation`
*   **Decoding Behavior:** Large, high-entropy data blocks indicating a multi-stage unpacking/decryption routine.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-Stage Payload Execution:** The presence of large, high-entropy data blocks and extensive decoding loops indicates the binary is designed to decrypt and unpack a secondary payload in memory.
*   **Advanced Evasion Tactics:** The sample employs sophisticated anti-analysis techniques, including `IsDebuggerPresent` checks, `RtlCaptureContext` for environment profiling, and "trap-based" code paths intended to crash automated sandboxes.
*   **Information Gathering/Spyware Behavior:** The inclusion of specific API calls (`GetActiveWindow`, `GetLastActivePopup`) suggests the malware is prepared to identify user activity or target specific applications (like banking sites) once the primary payload is deployed.
