# Threat Analysis Report

**Generated:** 2026-07-18 06:01 UTC
**Sample:** `087216ee05746cc264752b0623dc6a1e32cddc0ca088832672e6dd356d394393_087216ee05746cc264752b0623dc6a1e32cddc0ca088832672e6dd356d394393.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `087216ee05746cc264752b0623dc6a1e32cddc0ca088832672e6dd356d394393_087216ee05746cc264752b0623dc6a1e32cddc0ca088832672e6dd356d394393.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 1,727,488 bytes |
| MD5 | `34fe39190f861681e61a46fe8162d3bc` |
| SHA1 | `cb6d7a35e917322401558aed727289423f384876` |
| SHA256 | `087216ee05746cc264752b0623dc6a1e32cddc0ca088832672e6dd356d394393` |
| Overall entropy | 5.948 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1698618444 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,575,424 | 5.695 | No |
| `.rdata` | 27,648 | 5.389 | No |
| `.data` | 115,712 | 7.907 | ⚠️ Yes |
| `.pdata` | 2,560 | 4.63 | No |
| `.rsrc` | 1,536 | 2.846 | No |
| `.reloc` | 3,584 | 0.943 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `WriteConsoleW`, `SetFilePointerEx`, `SetStdHandle`, `GetConsoleMode`, `GetConsoleCP`, `FlushFileBuffers`, `HeapSize`, `LoadLibraryW`, `OutputDebugStringW`, `GetStringTypeW`, `AddAtomA`, `DeleteAtom`, `WaitForMultipleObjects`, `CreateEventA`
**USER32.dll**: `ToUnicodeEx`, `EnumDisplaySettingsA`, `DlgDirListA`, `GetWindow`, `GetShellWindow`, `GetParent`, `GetClassWord`, `SetRect`, `ChildWindowFromPointEx`, `LockWindowUpdate`, `SwitchToThisWindow`, `GetMenuDefaultItem`, `GetMenuItemCount`, `GetSubMenu`, `TranslateAcceleratorA`
**GDI32.dll**: `Polyline`, `LPtoDP`, `GetEnhMetaFileHeader`, `GdiGradientFill`, `PtInRegion`, `PatBlt`, `GetViewportOrgEx`, `RemoveFontMemResourceEx`, `GetCharacterPlacementA`, `GetStretchBltMode`, `GetOutlineTextMetricsA`, `GetMetaRgn`, `GetCharWidthA`, `AnimatePalette`, `OffsetWindowOrgEx`
**gdiplus.dll**: `GdiplusStartup`

### Exports

`GetFileVersionInfoA`, `GetFileVersionInfoByHandle`, `GetFileVersionInfoExW`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoSizeExW`, `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`, `VerFindFileA`, `VerFindFileW`, `VerInstallFileA`, `VerInstallFileW`, `VerLanguageNameA`, `VerLanguageNameW`, `VerQueryValueA`, `VerQueryValueW`

## Extracted Strings

Total strings found: **1148** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
H9D$XtW
H9D$pu
H;D$ptn
H;D$P~~
D$X5<

D$X-6}
H9D$0t
R?Y`U
r
\Y=qtq
ITdqWY}
hjOZ%}
T7fk@~
Sq=^^y
5WZzy
AU	)Mw
Df\9x
D:<iZ1x
/BO]^Cx
C{@7/{
ZtC5K{
}z2Y>qv
FGVc?|
NJ5`'
ZZ;/@+
Og90%b
	)ab\|Zm
Oxs`v^
]]lF(0
't8IF@
8_=Edo
B:leW
' jw./b
1u:"Yp
[o:](?
+$f?It
*~qx:
3T}b?2
EumuX4
	$fxe
/Yqaq
mz9\[4U
I5fVQ}
:zo.-Vv_
	T[e| 
6Iez#Y
qj|^)
	]l,:}`mCF
}>whXg
iZHB9
kCL2$6
Ts|	bD
rI?Bbw
|'<isi
Cy8eXB
dMz%{
*I6b	|q
LKqvgp
P!br.CQ
9	8F|h
o
	%|]1
*{Vfgn
i?ZZW_Z`_
e^U
]@
Oo!~|v
8GD1(`
3>p7y$N
fjWzyd
Y^Go`\
^{_[,.
 V08v'
M4<pd)
=v]w;$
FHat.O
UvTum~f
z>mnrM
+g|(j5q
C_aQQHo
Ybui.k
)MyJ)M
&r{Ol~s{
tY:No6
Pggk9N
10g.W'
3=So^](	
~s~:@wH
,v[)N3jG
|,n+'FQ
=&uvN

A{_z<
:	F7YG/
>jo`@\9T
{dm1Lm
mv r}3
t*V^
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180002700` | `0x180002700` | 1428925 | — |
| `fcn.18017a994` | `0x18017a994` | 10605 | ✓ |
| `fcn.18017a6ec` | `0x18017a6ec` | 5491 | ✓ |
| `fcn.18017cc48` | `0x18017cc48` | 5375 | ✓ |
| `fcn.18017e850` | `0x18017e850` | 4077 | ✓ |
| `fcn.180001920` | `0x180001920` | 2150 | ✓ |
| `fcn.18017fa18` | `0x18017fa18` | 1908 | ✓ |
| `fcn.180001200` | `0x180001200` | 1821 | ✓ |
| `fcn.18017e880` | `0x18017e880` | 1252 | ✓ |
| `fcn.180002190` | `0x180002190` | 1126 | ✓ |
| `fcn.18017de68` | `0x18017de68` | 1018 | ✓ |
| `fcn.18017e264` | `0x18017e264` | 718 | ✓ |
| `fcn.18017c814` | `0x18017c814` | 686 | ✓ |
| `fcn.18017ccf8` | `0x18017ccf8` | 623 | ✓ |
| `fcn.18017ef88` | `0x18017ef88` | 622 | ✓ |
| `fcn.18017c5b8` | `0x18017c5b8` | 604 | ✓ |
| `fcn.180181058` | `0x180181058` | 603 | ✓ |
| `fcn.18017d380` | `0x18017d380` | 548 | ✓ |
| `fcn.180180c00` | `0x180180c00` | 498 | ✓ |
| `fcn.18017c318` | `0x18017c318` | 481 | ✓ |
| `fcn.18017a384` | `0x18017a384` | 479 | ✓ |
| `fcn.180180e88` | `0x180180e88` | 461 | ✓ |
| `fcn.18017b138` | `0x18017b138` | 455 | ✓ |
| `fcn.18017be20` | `0x18017be20` | 406 | ✓ |
| `fcn.18017aa64` | `0x18017aa64` | 405 | ✓ |
| `fcn.18017e5cc` | `0x18017e5cc` | 357 | ✓ |
| `entry0` | `0x18017a058` | 352 | ✓ |
| `fcn.1801807b0` | `0x1801807b0` | 348 | ✓ |
| `fcn.180179f00` | `0x180179f00` | 341 | ✓ |
| `fcn.18017a76c` | `0x18017a76c` | 307 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.180001200.c`](code/fcn.180001200.c)
- [`code/fcn.180001920.c`](code/fcn.180001920.c)
- [`code/fcn.180002190.c`](code/fcn.180002190.c)
- [`code/fcn.180179f00.c`](code/fcn.180179f00.c)
- [`code/fcn.18017a384.c`](code/fcn.18017a384.c)
- [`code/fcn.18017a6ec.c`](code/fcn.18017a6ec.c)
- [`code/fcn.18017a76c.c`](code/fcn.18017a76c.c)
- [`code/fcn.18017a994.c`](code/fcn.18017a994.c)
- [`code/fcn.18017aa64.c`](code/fcn.18017aa64.c)
- [`code/fcn.18017b138.c`](code/fcn.18017b138.c)
- [`code/fcn.18017be20.c`](code/fcn.18017be20.c)
- [`code/fcn.18017c318.c`](code/fcn.18017c318.c)
- [`code/fcn.18017c5b8.c`](code/fcn.18017c5b8.c)
- [`code/fcn.18017c814.c`](code/fcn.18017c814.c)
- [`code/fcn.18017cc48.c`](code/fcn.18017cc48.c)
- [`code/fcn.18017ccf8.c`](code/fcn.18017ccf8.c)
- [`code/fcn.18017d380.c`](code/fcn.18017d380.c)
- [`code/fcn.18017de68.c`](code/fcn.18017de68.c)
- [`code/fcn.18017e264.c`](code/fcn.18017e264.c)
- [`code/fcn.18017e5cc.c`](code/fcn.18017e5cc.c)
- [`code/fcn.18017e850.c`](code/fcn.18017e850.c)
- [`code/fcn.18017e880.c`](code/fcn.18017e880.c)
- [`code/fcn.18017ef88.c`](code/fcn.18017ef88.c)
- [`code/fcn.18017fa18.c`](code/fcn.18017fa18.c)
- [`code/fcn.1801807b0.c`](code/fcn.1801807b0.c)
- [`code/fcn.180180c00.c`](code/fcn.180180c00.c)
- [`code/fcn.180180e88.c`](code/fcn.180180e88.c)
- [`code/fcn.180181058.c`](code/fcn.180181058.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C code, this binary exhibits characteristics of a **sophisticated multi-stage packer or a primary stage "loader"** for malware. It employs significant anti-analysis techniques to hide its true functionality.

### Core Functionality & Purpose
The primary purpose of this code is to act as a **downloader/packer**. Instead of containing the malicious payload directly, it is designed to:
1.  Unpack and decrypt hidden payloads into memory or onto disk.
2.  Obfuscate the execution flow to hide these actions from automated sandboxes and static analysis tools.
3.  Perform environment checks to ensure it is running on a "real" victim machine rather than an analyst's laboratory.

### Suspicious & Malicious Behaviors

*   **Anti-Analysis & Anti-Debugging:**
    *   **Debugger Detection:** Function `fcn.18017ef88` explicitly calls `IsDebuggerPresent()`. This is a standard technique used to detect if the code is being analyzed by a debugger like x64dbg.
    *   **Sandbox/Environment Evasion:** The binary uses several Win32 API calls (e.g., `GetActiveWindow`, `GetLastActivePopup`, `GetProcessWindowStation`) to determine if there is "human-like" interaction or if the environment behaves like a standard workstation.
    *   **Hardware Compatibility Checks:** Multiple functions (`fcn.18017cc48`, `fcn.18017e850`) use `IsProcessorFeaturePresent(0x17)` and subsequent jumps to determine execution paths. This is often used to detect specific virtual machine (VM) signatures or environments that do not support certain hardware features typical of high-end consumer CPUs but common in sandbox environments.
    *   **Execution Termination:** The code includes checks where, if an environment is deemed "suspicious" or a debugger is detected, it will call `TerminateProcess` or simply exit the execution thread (as seen in several loops within `fcn.18017cc48`).

*   **Dynamic API Resolution & IAT Obfuscation:**
    *   The code heavily utilizes `GetProcAddress` and `LoadLibraryExW` (seen in `fcn.18017ef88`) to resolve functions like `MessageBoxW`. This is done to hide the Import Address Table (IAT), making it harder for static analysis tools to determine what system functions the malware calls at first glance.

*   **Persistence & Payload Execution:**
    *   The presence of `WriteFile` and complex buffer processing in `fcn.18017fa18` suggests that the loader is preparing data (likely a decrypted malicious payload) to be written to disk or injected into another process.
    *   It uses `CreateMutexA` (in `fcn.180001200`) and `CreateEventA`, which are common techniques for ensuring only one instance of the malware is running at once (infection guarding).

### Notable Techniques & Patterns

*   **Junk Code Injection:** Several functions, such as `fcn.180001920` and `fcn.180001200`, contain massive blocks of complex arithmetic, nested loops, and assignments that do not contribute to the final result but serve to confuse automated decompiler engines and time up a human analyst's review.
*   **Custom Memory/Data Processing:** The repetitive use of `fcn.18017b434` on large memory ranges (e.g., in `fcn.18017de68`) indicates that the code is iterating over a "blob" of encrypted data, likely decrypting it step-by-step or performing an XOR/XOR-lite decryption before moving to the next stage.
*   **Decoding/Encoding Layers:** The use of `EncodePointer` and `DecodePointer` suggests a wrapper or custom packer (similar to UPX or VMProtect) that protects strings and function pointers from being visible in the binary's raw data sections.
*   **String Obfuscation:** The presence of high-entropy, nonsensical strings and "junk" data at the top indicates that actual strings (like C2 URLs or file paths) are stored in an encrypted format and only decrypted in memory during execution.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036.005 | Debugger Detection | The use of `IsDebuggerPresent()` is a direct attempt to determine if the binary is being analyzed by a debugger and alter its behavior accordingly. |
| T1497 | Virtualization | The inclusion of hardware capability checks (`IsProcessorFeaturePresent`) and environment queries (e.g., `GetActiveWindow`) indicates attempts to detect and evade sandboxes or virtual machines. |
| T1027 | Obfuscated Files or Information | The use of junk code, encoded pointers, and high-entropy strings are techniques used to hide the application's true logic and purpose from static analysis tools. |
| T1036 | Impair Defenses | The deliberate use of `GetProcAddress` and `LoadLibraryExW` to resolve functions at runtime is intended to hide the Import Address Table (IAT) from analysts. |
| T1620 | Reflective Code Loading | The preparation of data for injection into other processes indicates a method to execute malicious code in memory rather than from a file on disk. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified. (The "EXTRACTED STRINGS" section contains high-entropy/obfuscated data with no discernible network indicators).

**File paths / Registry keys**
*   None identified. (Only internal function identifiers like `fcn.18017ef88` are present, which are artifacts of the disassembly process rather than system-level file paths or registry keys.)

**Mutex names / Named pipes**
*   None identified. (The behavioral analysis confirms the use of `CreateMutexA`, but no specific mutex string was provided in the text.)

**Hashes**
*   None identified.

**Other artifacts**
*   **Malware Type:** Multi-stage packer / Loader.
*   **Anti-Analysis Techniques:** 
    *   `IsDebuggerPresent` check (Execution of `fcn.18017ef88`).
    *   Hardware capability checks (`IsProcessorFeaturePresent(0x17)`) to detect virtualized/sandbox environments.
    *   Dynamic API Resolution via `GetProcAddress` and `LoadLibraryExW`.
*   **Persistence/Infection Guarding:** Use of `CreateMutexA` and `CreateEventA`.
*   **Payload Delivery:** Evidence of a "loader" mechanism involving buffer processing and potential file writing (`WriteFile`).

***Note for Analyst:* The provided strings are heavily obfuscated or represent junk data common in packed binaries. No plaintext network indicators (IPs/URLs) were available for extraction from the raw string dump.**

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

4. **Key evidence**:
* **Sophisticated Evasion Techniques:** The binary employs multiple layers of anti-analysis, including `IsDebuggerPresent` checks, hardware capability testing (`IsProcessorFeaturePresent`) to detect virtual machines, and dynamic API resolution via `GetProcAddress` to hide its Import Address Table (IAT).
* **Loader/Packer Characteristics:** Evidence of "junk code" injection, custom memory decryption loops (fcn.18017b434), and the use of `EncodePointer`/`DecodePointer` indicates the binary's primary role is to wrap or decrypt a secondary malicious payload before execution.
* **Execution Guarding:** The use of `CreateMutexA` and `CreateEventA` combined with "reflection-style" loading suggests the sample is designed to ensure only one instance runs while preparing for memory injection/payload deployment.
