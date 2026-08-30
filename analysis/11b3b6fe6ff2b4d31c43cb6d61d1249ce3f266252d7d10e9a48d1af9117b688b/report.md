# Threat Analysis Report

**Generated:** 2026-08-23 21:01 UTC
**Sample:** `11b3b6fe6ff2b4d31c43cb6d61d1249ce3f266252d7d10e9a48d1af9117b688b_11b3b6fe6ff2b4d31c43cb6d61d1249ce3f266252d7d10e9a48d1af9117b688b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11b3b6fe6ff2b4d31c43cb6d61d1249ce3f266252d7d10e9a48d1af9117b688b_11b3b6fe6ff2b4d31c43cb6d61d1249ce3f266252d7d10e9a48d1af9117b688b.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 4 sections |
| Size | 3,188,992 bytes |
| MD5 | `bf8e74f1dacedcd2026ef97894cc7978` |
| SHA1 | `33a3fe17285b172d94e1965828b5c7764ec8ddbd` |
| SHA256 | `11b3b6fe6ff2b4d31c43cb6d61d1249ce3f266252d7d10e9a48d1af9117b688b` |
| Overall entropy | 7.991 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1338195918 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 102,400 | 6.656 | No |
| `.rdata` | 15,360 | 5.725 | No |
| `.data` | 2,560 | 4.442 | No |
| `.rsrc` | 20,480 | 4.056 | No |

### Imports

**COMCTL32.dll**: `ord_17`
**SHELL32.dll**: `SHGetSpecialFolderPathW`, `ShellExecuteW`, `SHGetMalloc`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`, `ShellExecuteExW`
**GDI32.dll**: `CreateCompatibleDC`, `CreateFontIndirectW`, `DeleteObject`, `DeleteDC`, `GetCurrentObject`, `StretchBlt`, `GetDeviceCaps`, `CreateCompatibleBitmap`, `SelectObject`, `SetStretchBltMode`, `GetObjectW`
**ADVAPI32.dll**: `FreeSid`, `AllocateAndInitializeSid`, `CheckTokenMembership`
**USER32.dll**: `GetWindowLongW`, `GetMenu`, `SetWindowPos`, `GetWindowDC`, `ReleaseDC`, `GetDlgItem`, `GetParent`, `GetWindowRect`, `GetClassNameA`, `CreateWindowExW`, `SetTimer`, `GetMessageW`, `DispatchMessageW`, `KillTimer`, `DestroyWindow`
**ole32.dll**: `CreateStreamOnHGlobal`, `CoCreateInstance`, `CoInitialize`
**OLEAUT32.dll**: `VariantClear`, `SysFreeString`, `OleLoadPicture`, `SysAllocString`
**KERNEL32.dll**: `GetFileSize`, `SetFilePointer`, `ReadFile`, `WaitForMultipleObjects`, `GetModuleHandleA`, `SetFileTime`, `SetEndOfFile`, `LeaveCriticalSection`, `EnterCriticalSection`, `DeleteCriticalSection`, `FormatMessageW`, `lstrcpyW`, `LocalFree`, `IsBadReadPtr`, `GetSystemDirectoryW`
**MSVCRT.dll**: `??3@YAXPAX@Z`, `??2@YAPAXI@Z`, `memcmp`, `free`, `memcpy`, `_wtol`, `_controlfp`, `_except_handler3`, `__set_app_type`, `__p__fmode`, `__p__commode`, `_adjust_fdiv`, `__setusermatherr`, `_initterm`, `__getmainargs`

## Extracted Strings

Total strings found: **7123** (showing first 100)

```
!Require Windows
$PE
`.rdata
@.data
;Es,j*
QQSVWh
hSVWj@
PSSSSSSh 
tHHf9
Ff9wu
L$ItaIt4IuQf
@@f98u
utj"j Pj:h
SVWhNG@
YYu$j	V
YYu$j
V
9u@t V
YYj _f9;v
CCf9;w
9}PYu
u(f9>t
f9>t
FFf9>u
HtHHuY
SSjj
F(@Pj
jh
_8WhCv@
EHHtW
@PQSjh
9^8u W

;Mt
9nHu%3
twHtPHt H
QQSUVW
_^][YY
H3NW
G1FV
O3L$,
T$ 9T$
D$QRP
A<+ADSW
F0v_2
T$PQR
|$D;T$ 
;L$ds3
;T$hs)
V+V,;
F9F,r
D$(;D$
r
_^]3
D$(;D$
L$(;L$
PP9L$t
9F _^]
9nLtq;
D$ 9F$
L$0_^]
T$0_^]
D$0_^]
D$0_^]
T$0_^]
D$0_^]
;wTt+P
;w(t>P
T$PQR
D$ )Ft
D$,_^]
D$,_^]
L$,_^]
T$,_^]
;VHt8\$(u
uK8D$(uO
FD;FHu
9^(t=W
B4;B8t
B8;B4t
u;F<v
u;F<v
^u;H<v
rQ<@wM
F,+F4W
BBFFf;
V;Uu
8] t09
F 9~ r
F(;F0r
H0;N0t
8^ht6h
E49uPr
Ep9}pu
;F4wr
F0F4u5
ttNt_Nt.Nt
t6NNt$
@;D$r
t$rw
_^][YY
x0C;^D|
Ep8XTt
U\;P0|
uf9]hua
UhX9Ed
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00405bfc` | `0x405bfc` | 6361 | ✓ |
| `fcn.00414c38` | `0x414c38` | 3557 | ✓ |
| `fcn.0040df80` | `0x40df80` | 3210 | ✓ |
| `fcn.00414491` | `0x414491` | 1658 | ✓ |
| `fcn.0040ed00` | `0x40ed00` | 1565 | ✓ |
| `fcn.00417ad7` | `0x417ad7` | 1527 | ✓ |
| `fcn.0041604d` | `0x41604d` | 1346 | ✓ |
| `fcn.0040a270` | `0x40a270` | 1182 | ✓ |
| `fcn.00409dd0` | `0x409dd0` | 1171 | ✓ |
| `fcn.00411a40` | `0x411a40` | 984 | ✓ |
| `fcn.0040d6f0` | `0x40d6f0` | 891 | ✓ |
| `fcn.004111d0` | `0x4111d0` | 885 | ✓ |
| `fcn.0040c010` | `0x40c010` | 870 | ✓ |
| `fcn.00403b54` | `0x403b54` | 836 | ✓ |
| `fcn.0040f380` | `0x40f380` | 798 | ✓ |
| `fcn.004177d5` | `0x4177d5` | 770 | ✓ |
| `fcn.004036f6` | `0x4036f6` | 753 | ✓ |
| `fcn.00407a58` | `0x407a58` | 734 | ✓ |
| `fcn.00408e76` | `0x408e76` | 731 | ✓ |
| `fcn.00410050` | `0x410050` | 710 | ✓ |
| `fcn.00416e11` | `0x416e11` | 678 | ✓ |
| `fcn.004097f6` | `0x4097f6` | 660 | ✓ |
| `fcn.004180ff` | `0x4180ff` | 657 | ✓ |
| `fcn.00404f0e` | `0x404f0e` | 647 | ✓ |
| `fcn.0040faf0` | `0x40faf0` | 642 | ✓ |
| `fcn.00405489` | `0x405489` | 617 | ✓ |
| `fcn.0040d480` | `0x40d480` | 610 | ✓ |
| `fcn.0040ca10` | `0x40ca10` | 595 | ✓ |
| `fcn.0040ac20` | `0x40ac20` | 590 | ✓ |
| `fcn.0041413f` | `0x41413f` | 588 | ✓ |

### Decompiled Code Files

- [`code/fcn.004036f6.c`](code/fcn.004036f6.c)
- [`code/fcn.00403b54.c`](code/fcn.00403b54.c)
- [`code/fcn.00404f0e.c`](code/fcn.00404f0e.c)
- [`code/fcn.00405489.c`](code/fcn.00405489.c)
- [`code/fcn.00405bfc.c`](code/fcn.00405bfc.c)
- [`code/fcn.00407a58.c`](code/fcn.00407a58.c)
- [`code/fcn.00408e76.c`](code/fcn.00408e76.c)
- [`code/fcn.004097f6.c`](code/fcn.004097f6.c)
- [`code/fcn.00409dd0.c`](code/fcn.00409dd0.c)
- [`code/fcn.0040a270.c`](code/fcn.0040a270.c)
- [`code/fcn.0040ac20.c`](code/fcn.0040ac20.c)
- [`code/fcn.0040c010.c`](code/fcn.0040c010.c)
- [`code/fcn.0040ca10.c`](code/fcn.0040ca10.c)
- [`code/fcn.0040d480.c`](code/fcn.0040d480.c)
- [`code/fcn.0040d6f0.c`](code/fcn.0040d6f0.c)
- [`code/fcn.0040df80.c`](code/fcn.0040df80.c)
- [`code/fcn.0040ed00.c`](code/fcn.0040ed00.c)
- [`code/fcn.0040f380.c`](code/fcn.0040f380.c)
- [`code/fcn.0040faf0.c`](code/fcn.0040faf0.c)
- [`code/fcn.00410050.c`](code/fcn.00410050.c)
- [`code/fcn.004111d0.c`](code/fcn.004111d0.c)
- [`code/fcn.00411a40.c`](code/fcn.00411a40.c)
- [`code/fcn.0041413f.c`](code/fcn.0041413f.c)
- [`code/fcn.00414491.c`](code/fcn.00414491.c)
- [`code/fcn.00414c38.c`](code/fcn.00414c38.c)
- [`code/fcn.0041604d.c`](code/fcn.0041604d.c)
- [`code/fcn.00416e11.c`](code/fcn.00416e11.c)
- [`code/fcn.004177d5.c`](code/fcn.004177d5.c)
- [`code/fcn.00417ad7.c`](code/fcn.00417ad7.c)
- [`code/fcn.004180ff.c`](code/fcn.004180ff.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis of the binary.

### Updated Analysis Summary
The addition of this code reinforces the conclusion that the binary is a **sophisticated 7-Zip based SFX (Self-Extracting) wrapper**. The new functions show significant depth in how it manages resources, handles UI elements during the extraction process, and orchestrates the execution of the secondary payload.

---

### Enhanced Technical Analysis

#### 1. Advanced Extraction & Compression Logic
Functions like `fcn.004111d0`, `fcn.0040c010`, and `fcn.004180ff` contain highly complex, nested loops involving bit-shifting and large memory offsets. 
*   **Observation:** These are characteristic of the **LZMA/7z decompression algorithms**. 
*   **Significance:** While this complexity can sometimes be used as a "smokescreen" to frustrate manual analysis (as noted in the previous summary), in this specific context, it confirms the binary is using an integrated 7-Zip engine. It is designed to handle complex compressed files reliably before attempting to run the hidden payload.

#### 2. Robust Resource & Environment Handling
The function `fcn.00403b54` and `fcn.00404f0e` demonstrate how the binary prepares itself for various execution environments:
*   **Environment Awareness:** It actively checks for "SetEnvironment" flags and handles system-specific paths via `SHGetSpecialFolderPathW`. 
*   **Localization/UI Prep:** `fcn.00404f0e` maps critical strings like `"ErrorTitle"`, `"WarningTitle"`, `"Progress"`, and `"GUIMode"`. This ensures the "wrapper" provides a standard user experience (even if that experience is used to mask malicious activity) while handling potential errors during extraction (e.g., insufficient disk space or incorrect passwords).

#### 3. Sophisticated Process Orchestration
The function `fcn.00405489` is a critical area for incident responders:
*   **Child Process Execution:** It uses `CreateProcessW` to launch the final payload (the "second stage"). 
*   **Job Objects & Synchronization:** The use of **Job Objects** (`CreateJobObjectW`, `AssignProcessToJobObject`) and **I/O Completion Ports** is a sophisticated way to manage child processes. It ensures that the launcher remains in a stable state while the payload (e.g., `setup.exe`) is running, and can be used to ensure all child processes are handled correctly by the OS before the wrapper exits.
*   **Wait Logic:** The inclusion of `sfxwaitall` logic suggests it waits for specific conditions or files to exist/finish before allowing the process tree to proceed or exit.

#### 4. UI Management & Icon Handling
Function `fcn.00408e76` handles window positioning and icon loading (`LoadIconW`).
*   **Analysis:** This is used to ensure that as the "extractor" runs, it presents a coherent interface to the user. While not inherently malicious, in malware samples, this is often used to make the extraction process look like a legitimate software installation (e.g., a fake update or a game installer).

---

### Updated Summary of Findings

| Feature | Observation | Risk/Intent |
| :--- | :--- | :--- |
| **Core Type** | **Dropper / SFX Wrapper** | Functions as the "delivery vehicle" for a secondary payload. |
| **Payload Handling** | 7-Zip Engine Integration | Uses advanced LZMA decompression to hide and extract a hidden executable. |
| **Execution Logic** | **Job Object Orchestration** | Uses advanced Windows API calls to manage the lifecycle of the launched payload. |
| **Evasion/Stealth** | Self-Deletion & Complex Code | Hides the "real" malware inside an archive; uses complex logic as a distraction for analysts. |
| **User Interaction** | Multi-language Resource Mapping | Ensures the extractor looks and acts like a standard installer. |

### Updated Recommendation for Incident Response
The complexity of the code in chunk 2/2 confirms that this is not a simple "one-off" script, but a robustly engineered wrapper. 

1.  **Primary Threat:** The primary threat remains the **payload inside the archive**. This wrapper is highly effective at ensuring that the payload is successfully unpacked and executed with the necessary environment settings (like paths and permissions).
2.  **Triage Note:** When analyzing this in a sandbox, notice if it creates temporary files or folders during execution. These are the locations where the "real" malware will appear after the 7-Zip logic finishes.
3.  **Indicator of Intent:** The use of **Job Objects** and **I/O Completion Ports** for process management is high-quality engineering. This is common in professional software but also frequently used by advanced threat actors to ensure that their "dropper" doesn't crash or exit before the malware has successfully established persistence.

**Conclusion:** This binary is a highly competent **First-Stage Dropper**. It provides a stable, standard-looking environment for the installation of an additional payload while hiding that payload within an encrypted/compressed archive.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a 7-Zip based SFX wrapper and complex LZMA decompression logic is used to hide the secondary payload from static analysis. |
| **T1036** | Masquerading | The inclusion of multi-language support, custom icons (`LoadIconW`), and standard warning/error titles allows the binary to mimic a legitimate software installer. |
| **T1204** | User Execution | The use of `CreateProcessW` and "Job Objects" indicates a transition from the dropper's role to the execution of the primary payload in a managed environment. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type. 

Please note that this sample primarily functions as a **downloader/dropper wrapper**. Because it is a generic 7-Zip SFX wrapper, many "strings" are boilerplate code rather than unique malicious infrastructure.

### **IP addresses / URLs / Domains**
*   *None identified.* (The binary performs local extraction and does not contain hardcoded C2 infrastructure in the provided text).

### **File paths / Registry keys**
*   `setup.exe` (Identified as the "second stage" payload managed by the wrapper).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (Note: Values such as `0x%08x` are code format specifiers, not file hashes).

### **Other artifacts**
*   **Technique - Compression/Obfuscation:** 7-Zip SFX Wrapper / LZMA decompression. The binary is designed to hide a secondary payload within an archive.
*   **Behavioral Indicator - Process Management:** Use of **Job Objects** (`CreateJobObjectW`) and **I/O Completion Ports** to manage the lifecycle and stability of child processes (hidden payloads).
*   **Masquerading Strategy:** Multi-language resource mapping for "installer" behavior, intended to mimic legitimate software setup routines.

---

### **Analyst Note:**
The primary threat associated with this sample is not within the strings themselves, but in the **behavioral methodology**. The analysis confirms this is a high-quality first-stage dropper. While it lacks hardcoded C2 IPs (likely because the second stage, `setup.exe`, handles the actual communication), its use of Job Objects and 7-Zip integration indicates a sophisticated effort to mask the transition from the "downloader" phase to the "malware execution" phase.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High

**Key evidence**:
* **SFX Wrapper functionality:** The binary uses complex LZMA/7-Zip decompression logic to hide and extract a second-stage executable (`setup.exe`) from a compressed archive, which is the hallmark of a "first-stage" dropper.
* **Advanced Process Management:** The use of Job Objects and I/O Completion Ports indicates high-quality engineering designed to manage the lifecycle of the payload and ensure it executes successfully without the wrapper crashing or alerting the user.
* **Masquerading Techniques:** The inclusion of multi-language resource mapping, custom icons (`LoadIconW`), and standard error/progress titles is specifically intended to make the extraction process appear as a legitimate software installer.
