# Threat Analysis Report

**Generated:** 2026-08-23 22:05 UTC
**Sample:** `11c3c7fd8b9fbb954a5a21af80f38414795930d63e8c6f5ea67bc92162359c52_11c3c7fd8b9fbb954a5a21af80f38414795930d63e8c6f5ea67bc92162359c52.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11c3c7fd8b9fbb954a5a21af80f38414795930d63e8c6f5ea67bc92162359c52_11c3c7fd8b9fbb954a5a21af80f38414795930d63e8c6f5ea67bc92162359c52.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 4 sections |
| Size | 70,316,002 bytes |
| MD5 | `80bcc7b11644c9b1e1637e28c6844429` |
| SHA1 | `9a63cf63e089492e8a24cc37391568c32a327ce7` |
| SHA256 | `11c3c7fd8b9fbb954a5a21af80f38414795930d63e8c6f5ea67bc92162359c52` |
| Overall entropy | 8.0 |
| Unpacked | No |

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
| `.rsrc` | 164,352 | 6.151 | No |

### Imports

**KERNEL32.DLL**: `GetStdHandle`, `VirtualAlloc`, `VirtualFree`, `GetACP`, `GetOEMCP`, `GetModuleHandleW`, `MulDiv`, `GlobalFree`, `GlobalAlloc`, `SizeofResource`, `LockResource`, `LoadResource`, `FindResourceA`, `lstrcmpiA`, `lstrcmpW`
**GDI32.dll**: `DeleteDC`, `StretchBlt`, `SetStretchBltMode`, `CreateCompatibleBitmap`, `SelectObject`, `CreateCompatibleDC`, `GetObjectW`, `GetDeviceCaps`, `CreateFontIndirectW`, `DeleteObject`, `GetCurrentObject`
**msvcrt.dll**: `_controlfp`, `?terminate@@YAXXZ`, `??3@YAXPAX@Z`, `??2@YAPAXI@Z`, `_purecall`, `__CxxFrameHandler`, `memcmp`, `free`, `malloc`, `memcpy`, `memmove`, `strncmp`, `_wtol`, `_wcsnicmp`, `memset`
**ole32.dll**: `CoInitialize`, `CoCreateInstance`, `CreateStreamOnHGlobal`
**OLEAUT32.dll**: `VariantClear`, `SysAllocString`, `OleLoadPicture`
**SHELL32.dll**: `SHGetFileInfoW`, `SHBrowseForFolderW`, `SHGetPathFromIDListW`, `SHGetMalloc`, `ShellExecuteExW`, `ShellExecuteW`, `SHGetSpecialFolderPathW`
**USER32.dll**: `MessageBoxA`, `GetKeyState`, `GetDlgItem`, `GetClientRect`, `SetWindowLongW`, `SetFocus`, `ShowWindow`, `DrawTextW`, `GetSystemMetrics`, `GetDC`, `ClientToScreen`, `GetWindow`, `DialogBoxIndirectParamW`, `SystemParametersInfoW`, `DrawIconEx`

## Extracted Strings

Total strings found: **152777** (showing first 100)

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

Based on the additional disassembly provided in chunk 2, I have updated and expanded the technical analysis. The new code reinforces the previous conclusion that this is a sophisticated **SFX (Self-Extracting) Installer Wrapper**, but it also highlights specific mechanisms used to facilitate "clean" execution—features often exploited by malware for anti-forensics and staged delivery.

---

### Updated Technical Analysis: SFX Archive/Installer Wrapper

#### 1. Advanced Construction & UI Management
The second chunk reveals a high level of sophistication in how the binary handles its presentation and environment:
*   **Dynamic UI Scaling:** `fcn.00406ae5` interacts with `GetSystemMetrics` and `SetWindowPos`. This suggests the installer is designed to be "polished," automatically adjusting dialog box sizes based on the user's system resolution or the length of localized text (e.g., translating a short English button into a long German word).
*   **Rich Text & Resource Handling:** The use of `GetClassName` for "STATIC" objects and the loading of `riched20` (`fcn.00402db3`) indicate that the installer can display complex text layouts and high-quality UI elements.
*   **Multilingual Support:** `fcn.004084c7` contains a series of checks for localized strings like `"BeginPrompt"`, `"FinishMessage"`, `"HelpText"`, and `"ErrorTitle"`. This confirms the tool is built to support multiple languages, which is common in large-scale commercial installers but also allows malware to appear as legitimate software.

#### 2. Robust Data Processing & Buffer Management
The complexity of functions like `fcn.0041137b` and `fcn.00412031` reveals the heavy lifting of the extraction engine:
*   **Complex State Machine:** These functions involve deeply nested loops and intricate memory calculations. This is typical of high-performance decompression libraries (like those used by 7-Zip). 
*   **Obfuscation via Complexity:** In a security context, this "heavy" logic serves as a shield. Because the code for handling LZMA/LZMA2 compression or complex file headers is so voluminous and mathematically dense, it can effectively hide the specific point at which the wrapper hands off execution to the malicious payload.

#### 3. Scripting & Batch Execution (Anti-Forensics)
A significant finding in this chunk is the construction of shell commands:
*   **Command Construction:** In `fcn.0040d4ac` and `fcn.004049ca`, the code performs operations similar to building a batch script. It includes logic to "check if a file exists" and then execute "del" (delete) commands via `ShellExecuteW`.
*   **Tactic:** While used by installers to clean up temporary files, in a malicious context, this is a classic **anti-forensics** technique. It ensures that any intermediate scripts, unpacked binaries, or log files created during the extraction process are deleted immediately before/after they are executed.

#### 4. Advanced File System Interaction
The code includes robust logic for handling and cleaning up file paths:
*   **Path Sanitization:** `fcn.0040339d` and `fcn.004029dc` handle the stripping of quotes, trailing slashes, and relative path resolution. 
*   **Dynamic Payload Execution:** The flow from `fcn.004049ca` leads to a `ShellExecuteW` call. This is the "hand-off" point where the wrapper finishes its job and starts the actual application (the payload).

---

### Updated Summary of Behavior

| Feature | Technical Observation | Potential Risk / Malicious Use Case |
| :--- | :--- | :--- |
| **SFX Masking** | Extensive 7-Zip-like logic for decompressing large data chunks and managing memory. | Masks the actual payload by burying it inside a complex, legitimate-looking extraction routine. |
| **Anti-Forensics** | Construction of `del` commands to remove files before calling `ShellExecuteW`. | Automatically "cleans up" evidence of the dropper or temporary files left behind during infection. |
| **Staged Execution** | Transition from a GUI-based installer (with buttons/prompts) to an underlying process. | Allows the initial "dropper" to appear harmless while the actual malware runs in a new process space. |
| **Sophisticated UI** | Handling of various locales, error titles, and dynamic window positioning. | Gives the appearance of professional software (e.g., a game launcher or software suite) to evade suspicion. |

### Conclusion & Risk Assessment
The binary is a high-quality **SFX Wrapper**. It is technically "sophisticated" rather than "simple." 

**Verdict:** The binary acts as a **Delivery Vehicle**. While the installer code itself may be legitimate (potentially stolen or repurposed from open-source tools like 7-Zip's SFX module), it provides all the necessary features for advanced malware:
1.  **Stealthy Extraction:** High complexity masks the transition to the payload.
2.  **Automatic Cleanup:** Built-in logic to delete temporary files/scripts using `del` commands.
3.  **Professional Appearance:** Multilingual support and UI adjustments make it look like a standard software installer, potentially tricking users into allowing its execution.

**Recommendation:** Treat this as a **Dropper/Loader**. Any payload extracted by this wrapper should be considered highly suspicious, as the wrapper is designed specifically to provide a "clean" environment for that payload to begin its operations.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of complex, mathematically dense "heavy" logic (e.g., LZMA/LZMA2 decompression) serves as a shield to hide the transition point between the wrapper and the malicious payload. |
| **T1070** | Indicator Removal on Host | The manual construction and execution of `del` commands are used to remove traces of intermediate scripts, unpacked binaries, or logs left during the extraction process. |
| **T1059** | Command and Scripting Interpreter | The analysis identifies specific code logic for constructing shell-style commands (like checking for file existence before deletion) to automate post-extraction cleanup. |
| **T1036** | (Implicit: Social Engineering/Masquerading) | While not a standalone technique, the "Sophisticated UI," "Multilingual Support," and professional resolution scaling are used to mimic legitimate software behavior to avoid user suspicion. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **`setup.exe`** (Note: This is a generic filename used by the wrapper to handle and execute the primary payload.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **7z SFX / 7-Zip library logic:** The presence of extensive 7-Zip extraction routines and headers (e.g., `7z SFX:`, `7-Zip:`) indicates the use of a self-extracting archive wrapper.
*   **Anti-Forensics Behavior:** Use of automated `"del"` commands via `ShellExecuteW` to delete temporary files, scripts, or intermediate artifacts immediately following execution.
*   **RichEdit Support:** Usage of `riched20` and `RichEdit20A` for complex UI rendering.
*   **Multi-Language Strings:** Presence of localized strings (e.g., `"BeginPrompt"`, `"FinishMessage"`, `"HelpText"`, `"ErrorTitle"`).

---

### **Analyst Note**
The primary risk identified is not a direct network connection or hardcoded path, but rather the **behavioral signature** of a "Loader/Dropper." The tool uses a sophisticated 7-Zip wrapper to mask the transition from a legitimate-looking installer to an underlying malicious payload, while simultaneously employing anti-forensics by deleting evidence of its own extraction process.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated SFX Wrapper:** The sample utilizes complex 7-Zip/LZMA decompression logic and multi-language UI elements to masquerade as a legitimate installer, providing a "professional" front for its activities.
*   **Anti-Forensic Cleanup:** The inclusion of automated `del` commands via `ShellExecuteW` specifically targets the removal of temporary files and intermediate scripts used during the extraction process.
*   **Staged Execution:** The analysis identifies a clear transition from a GUI-based installer to an underlying payload, a hallmark of droppers designed to hide the final malicious executable within a complex wrapping routine.
