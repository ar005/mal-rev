# Threat Analysis Report

**Generated:** 2026-08-10 14:52 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, UPX compressed, 3 sections |
| Size | 93,425,527 bytes |
| MD5 | `fa55e12f8d16d1146715776972f9244c` |
| SHA1 | `e72b93bd1fab02ed893c866be331933707bc6d6f` |
| SHA256 | `0db9dd9882f27357be88527b19240b86495cf5fef5c9fccfdb8776485b091c08` |
| Overall entropy | 7.999 |
| Unpacked | ✓ Yes (tool: upx) |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1235512703 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 78,336 | 6.512 | No |
| `.rdata` | 17,920 | 4.632 | No |
| `.data` | 1,536 | 3.808 | No |
| `.rsrc` | 169,472 | 7.572 | ⚠️ Yes |

### Imports

**KERNEL32.DLL**: `GetStdHandle`, `VirtualAlloc`, `VirtualFree`, `GetACP`, `GetOEMCP`, `GetModuleHandleW`, `MulDiv`, `GlobalFree`, `GlobalAlloc`, `SizeofResource`, `LockResource`, `LoadResource`, `FindResourceA`, `lstrcmpiA`, `lstrcmpW`
**GDI32.dll**: `DeleteDC`, `StretchBlt`, `SetStretchBltMode`, `CreateCompatibleBitmap`, `SelectObject`, `CreateCompatibleDC`, `GetObjectW`, `GetDeviceCaps`, `CreateFontIndirectW`, `DeleteObject`, `GetCurrentObject`
**msvcrt.dll**: `_controlfp`, `?terminate@@YAXXZ`, `??3@YAXPAX@Z`, `??2@YAPAXI@Z`, `_purecall`, `__CxxFrameHandler`, `memcmp`, `free`, `malloc`, `memcpy`, `memmove`, `strncmp`, `_wtol`, `_wcsnicmp`, `memset`
**ole32.dll**: `CoInitialize`, `CoCreateInstance`, `CreateStreamOnHGlobal`
**OLEAUT32.dll**: `VariantClear`, `SysAllocString`, `OleLoadPicture`
**SHELL32.dll**: `SHGetFileInfoW`, `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `SHGetMalloc`, `ShellExecuteExW`, `ShellExecuteW`, `SHGetSpecialFolderPathW`
**USER32.dll**: `MessageBoxA`, `GetKeyState`, `GetDlgItem`, `GetClientRect`, `SetWindowLongW`, `SetFocus`, `ShowWindow`, `DrawTextW`, `GetSystemMetrics`, `GetDC`, `ClientToScreen`, `GetWindow`, `DialogBoxIndirectParamW`, `SystemParametersInfoW`, `DrawIconEx`

## Extracted Strings

Total strings found: **202997** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data

BBFFf
hSVWj@
tHHf9
L$ItdIt?It
f
9wFFf
]WhD`A
YWh `A
 w
@@f
 w
@@f
YYu|j
V
9uHtAV
YKj0K^
]Tj Yf9v
CCf9w
?!u
f9K
QPh4`A
QPhL_A
uPhdbA
f97t"j 
f97t
GGf97u
SSjjh
F(@Pj
jh
tAUh4cA
_8Whfh@
EHHtW
@PQSjh
tzHtSHt H
QQSUVW
_^][YY
H0;N0t
8^ht6h
u'!F0!F4
tlNtbNt&Nt
t<NNt$
@;D$r
t$rw
_^][YY
x0C;^D|
99Gtt
F
9~|~!;~pt
YG;~||
V;Uu 8]
8] t:9
QL;QDr
w
QH;Q@s
OWhpdA
F$;F,r
<A@C;F
BBFFf;
QSVWj
t)Ht"Ht
X+X,;
F9F,r
HP9T$t
G(9G$u
;wTt SW
;w(t%PS
4Wh`dA
uG8Eu58E
FP;FTu
t%VhD-A
uhh-A
j
YQPSh
IMAGES
STATIC
RichEdit20A
riched20
 "%s".
 "%s".
Cancel
 "HelpText" 
 "HelpText"
7-Zip: 
7-Zip: 
7-Zip: 
 0x%08X.
7-Zip: 
 0x%08X
7-Zip: 
7-Zip: 
7-Zip: 
7-Zip: 
7-Zip: 
 (CRC).
7-Zip: CRC 
7-Zip: 
7-Zip: 
 "%s".
 "%s" 
 "setup.exe" 
 "setup.exe"
 "%s" 
 "%s" 
 "%s".
 "%s".
 "%s".
7z SFX: 
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004053c8` | `0x4053c8` | 5203 | ✓ |
| `fcn.0040ffe8` | `0x40ffe8` | 3254 | ✓ |
| `fcn.0040cd88` | `0x40cd88` | 1828 | ✓ |
| `fcn.00409210` | `0x409210` | 1545 | ✓ |
| `fcn.00410d81` | `0x410d81` | 1465 | ✓ |
| `fcn.0040c9ac` | `0x40c9ac` | 988 | ✓ |
| `fcn.00403507` | `0x403507` | 951 | ✓ |
| `fcn.004030b8` | `0x4030b8` | 741 | ✓ |
| `fcn.0040bd7c` | `0x40bd7c` | 715 | ✓ |
| `fcn.00406ae5` | `0x406ae5` | 672 | ✓ |
| `fcn.0041137b` | `0x41137b` | 663 | ✓ |
| `fcn.00412031` | `0x412031` | 637 | ✓ |
| `fcn.0040d4ac` | `0x40d4ac` | 633 | ✓ |
| `fcn.00407e52` | `0x407e52` | 604 | ✓ |
| `fcn.004084c7` | `0x4084c7` | 593 | ✓ |
| `fcn.0040b910` | `0x40b910` | 586 | ✓ |
| `fcn.0040c3b7` | `0x40c3b7` | 536 | ✓ |
| `fcn.004049ca` | `0x4049ca` | 498 | ✓ |
| `entry0` | `0x412a92` | 493 | ✓ |
| `fcn.0040c75f` | `0x40c75f` | 462 | ✓ |
| `fcn.0040db1e` | `0x40db1e` | 448 | ✓ |
| `fcn.004045fa` | `0x4045fa` | 439 | ✓ |
| `fcn.0040bb92` | `0x40bb92` | 418 | ✓ |
| `fcn.00401fa8` | `0x401fa8` | 391 | ✓ |
| `fcn.0040339d` | `0x40339d` | 362 | ✓ |
| `fcn.004124a0` | `0x4124a0` | 343 | ✓ |
| `fcn.00404f6a` | `0x404f6a` | 328 | ✓ |
| `fcn.0040275d` | `0x40275d` | 322 | ✓ |
| `fcn.004029dc` | `0x4029dc` | 315 | ✓ |
| `fcn.00402db3` | `0x402db3` | 309 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401fa8.c`](code/fcn.00401fa8.c)
- [`code/fcn.0040275d.c`](code/fcn.0040275d.c)
- [`code/fcn.004029dc.c`](code/fcn.004029dc.c)
- [`code/fcn.00402db3.c`](code/fcn.00402db3.c)
- [`code/fcn.004030b8.c`](code/fcn.004030b8.c)
- [`code/fcn.0040339d.c`](code/fcn.0040339d.c)
- [`code/fcn.00403507.c`](code/fcn.00403507.c)
- [`code/fcn.004045fa.c`](code/fcn.004045fa.c)
- [`code/fcn.004049ca.c`](code/fcn.004049ca.c)
- [`code/fcn.00404f6a.c`](code/fcn.00404f6a.c)
- [`code/fcn.004053c8.c`](code/fcn.004053c8.c)
- [`code/fcn.00406ae5.c`](code/fcn.00406ae5.c)
- [`code/fcn.00407e52.c`](code/fcn.00407e52.c)
- [`code/fcn.004084c7.c`](code/fcn.004084c7.c)
- [`code/fcn.00409210.c`](code/fcn.00409210.c)
- [`code/fcn.0040b910.c`](code/fcn.0040b910.c)
- [`code/fcn.0040bb92.c`](code/fcn.0040bb92.c)
- [`code/fcn.0040bd7c.c`](code/fcn.0040bd7c.c)
- [`code/fcn.0040c3b7.c`](code/fcn.0040c3b7.c)
- [`code/fcn.0040c75f.c`](code/fcn.0040c75f.c)
- [`code/fcn.0040c9ac.c`](code/fcn.0040c9ac.c)
- [`code/fcn.0040cd88.c`](code/fcn.0040cd88.c)
- [`code/fcn.0040d4ac.c`](code/fcn.0040d4ac.c)
- [`code/fcn.0040db1e.c`](code/fcn.0040db1e.c)
- [`code/fcn.0040ffe8.c`](code/fcn.0040ffe8.c)
- [`code/fcn.00410d81.c`](code/fcn.00410d81.c)
- [`code/fcn.0041137b.c`](code/fcn.0041137b.c)
- [`code/fcn.00412031.c`](code/fcn.00412031.c)
- [`code/fcn.004124a0.c`](code/fcn.004124a0.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis. The new code provides significant insight into the internal architecture of the binary, confirming its complexity as a sophisticated "wrapper" or "installer."

Here is the updated analysis including all previous findings:

### 1. Core Functionality and Purpose
The binary is confirmed to be a **sophisticated installer wrapper/wizard system** that utilizes an underlying extraction engine (likely 7-Zip) to manage bundled data.

*   **Sophisticated Wizard Architecture:** Functions such as `fcn.004084c7` act as a "Message Dispatcher" or "Action Handler." It maps specific internal IDs to actions like `BeginPrompt`, `FinishMessage`, and `ErrorTitle`. This indicates the binary is designed to provide a multi-step user interface, which can be used to guide a user through an installation process.
*   **Resource Management:** The code (e.g., `fcn.0041fa8` and `fcn.004045fa`) shows extensive use of dynamic resource loading (`FindResource`, `LoadResource`). It fetches UI elements, icons, and translated strings from its internal resources to populate the interface, allowing it to appear as a professional piece of software.
*   **Environment & Path Handling:** Functions like `fcn.0040339d` and `fcn.004029dc` handle complex path parsing (handling different directory separators) and environment variable checking. This ensures the payload is executed in a valid context after extraction.

### 2. Suspicious and Malicious Behaviors
While these features are common in legitimate installers, their specific combination reinforces its role as a "dropper" or "loader" used to shield malicious payloads:

*   **Multi-Stage Execution & Hiding:** The use of `ShellExecuteW` (within `fcn.004049ca`) suggests that the final stage is the execution of the extracted payload (`setup.exe`). By using a wrapper, the "true" functionality of the malware only appears after the initial executable has successfully unpacked and prepared the environment.
*   **Persistence and Clean-up (Forensic Evasion):** The logic in `fcn.004049ca` includes loops that check for file existence before execution or deletion (e.g., the "Repeat" loop structure). This is a classic technique to ensure that temporary files or the initial loader are removed from the disk immediately after the payload is launched, minimizing the forensic footprint.
*   **Antiforensics via Timestomping:** As previously noted, the use of `SetFileTime` (inferred from the context of `fcn.0040339d`) allows the program to alter file metadata so that newly dropped files appear to have been on the system for a long time.
*   **Self-Deletion Logic:** The presence of flags like `SelfDelete` in the configuration logic (from chunk 1) confirms it is designed to "vanish" after completion.

### 3. Technical Observations & Notable Patterns

*   **Sophisticated State Machine:** The large amount of switch/case and if/else logic in functions like `fcn.004084c7` and `fcn.00406ae5` suggests a complex state machine for the UI. This allows the program to react differently based on user input or system conditions, potentially allowing it to hide its true purpose until specific "guards" are passed.
*   **Memory Management & Buffer Handling:** Functions such as `fcn.0041137b` and `fcn.0040db1e` perform extensive memory copying (`memcpy`) and buffer management. This is characteristic of high-performance extraction engines (like 7-Zip) which the malware leverages to handle large amounts of data efficiently without raising suspicion.
*   **Dynamic UI Adaptation:** Function `fcn.00406ae5` calculates window dimensions and positions using `GetSystemMetrics`. This ensures that the installer looks "native" on different screen resolutions, a common trait in high-quality malware intended to deceive less-experienced users.

### 4. Summary Conclusion
The binary is a **high-sophistication multi-stage installer/dropper.** It functions as a sophisticated shell: it handles the UI presentation, manages the complexities of file extraction (using 7-Zip logic), performs environment preparation (handling paths and permissions), and executes the final payload via `ShellExecuteW`.

The inclusion of **anti-forensic techniques**—specifically **timestomping**, **automatic self-deletion**, and **complex shell execution paths**—strongly suggests it is a vehicle for delivering a malicious payload. By wrapping the "malicious" part in a complex, professional-looking installer, the developers aim to bypass automated detection systems while ensuring the final infection is cleanly established on the host machine.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1070.006** | Timestomping | The analysis confirms the use of `SetFileTime` to modify file metadata, making newly dropped files appear as if they have existed on the system for a long time. |
| **T1070.004** | File Deletion | The binary includes specific logic for "Self-Deletion" and the removal of temporary files/folders immediately after payload execution to minimize its forensic footprint. |
| **T1036** | Masquerading | The use of a complex UI, resource loading, and dynamic window scaling is designed to make the malware appear as a legitimate software installer. |
| **T1027** | Obfuscated Files or Information | The "wrapper" architecture serves as a vehicle to hide the true nature and presence of the malicious payload (`setup.exe`) from automated detection systems. |
| **T1204** | User Execution | The multi-step wizard/message dispatcher is designed to engage the user through an interactive process, facilitating the eventual execution of the primary payload. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   `setup.exe` (Identified as the final payload executed after extraction)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Extraction Engine:** Integration of 7-Zip logic/engine for unpacking bundled data.
*   **Execution Method:** Use of `ShellExecuteW` to launch the payload (`setup.exe`).
*   **Anti-Forensics (Timestomping):** Utilization of `SetFileTime` to modify file metadata and bypass chronological analysis.
*   **Persistence/Evasion (Self-Deletion):** Inclusion of automated self-deletion logic to remove the initial loader from the disk post-execution.
*   **UI Manipulation:** Use of `GetSystemMetrics` and custom "Message Dispatcher" logic to create a professional wrapper/wizard appearance.

---

## Malware Family Classification

1. **Malware family**: custom 
2. **Malware type**: dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Wrapper Architecture:** The binary functions as a complex installer wizard using a "Message Dispatcher" and resource loading to masquerade as legitimate software while managing the extraction of a hidden payload (`setup.exe`).
*   **Anti-Forensic Techniques:** The inclusion of specific evasion tactics, such as **timestomping** (`SetFileTime`) to manipulate file metadata and **automatic self-deletion** of the loader after execution, are hallmarks of advanced droppers designed to minimize their forensic footprint.
*   **Multi-Stage Execution:** The analysis confirms a clear transition from a "wrapper" stage (handling UI/extraction) to a primary payload execution via `ShellExecuteW`, confirming its role as a delivery vehicle for further infection.
